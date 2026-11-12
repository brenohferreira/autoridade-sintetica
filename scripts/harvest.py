import requests, json, csv, time, os, re
from datetime import datetime

BASE = "/home/ubuntu/review"
OUT = os.path.join(BASE, "buscas")
os.makedirs(OUT, exist_ok=True)
NOW = datetime.now().astimezone().isoformat(timespec="seconds")

def inv2text(inv):
    if not inv: return ""
    pos = []
    for w, idxs in inv.items():
        for i in idxs: pos.append((i, w))
    pos.sort()
    return " ".join(w for _, w in pos)

def brapci(q, label):
    u = "https://cip.brapci.inf.br/api/brapci/search"
    recs, total, start = [], None, 0
    while True:
        r = requests.get(u, params={"q": q, "di": "1972", "df": "2026", "start": start}, timeout=90)
        d = r.json()
        total = d.get("total")
        works = d.get("works", [])
        if not works: break
        for w in works:
            dd = w.get("data", {})
            recs.append({
                "source": "BRAPCI", "query": label, "query_string": q,
                "id": dd.get("ID"), "title": dd.get("TITLE"), "authors": dd.get("AUTHORS"),
                "year": dd.get("year") or w.get("year"), "venue": dd.get("JOURNAL"),
                "type": dd.get("CLASS") or w.get("type"), "doi": dd.get("DOI"),
                "abstract": (dd.get("ABSTRACT") or "")[:4000],
                "url": f"https://www.brapci.inf.br/v/{dd.get('ID')}",
            })
        if len(recs) >= (total or 0) or len(works) < 10: break
        start += 10
        time.sleep(0.3)
    return {"source": "BRAPCI", "label": label, "expression": q,
            "fields": "busca livre (titulo, resumo, palavras-chave e texto completo)",
            "filters": "di=1972; df=2026", "sort": "relevancia (score interno)",
            "total": total, "retrieved": len(recs), "examined": len(recs),
            "date": NOW, "url": "https://cip.brapci.inf.br/api/brapci/search"}, recs

def openalex(q, label, cap=200):
    u = "https://api.openalex.org/works"
    recs, total, cursor = [], None, "*"
    while len(recs) < cap:
        r = requests.get(u, params={
            "filter": f"title_and_abstract.search:{q}",
            "per_page": min(200, cap - len(recs)),
            "cursor": cursor,
            "mailto": "revisao.autoridade@example.org",
            "select": "id,doi,title,publication_year,publication_date,authorships,primary_location,type,abstract_inverted_index,cited_by_count,language,ids",
        }, timeout=120)
        d = r.json()
        total = d["meta"]["count"]
        res = d.get("results", [])
        if not res: break
        for w in res:
            auths = "; ".join(a["author"]["display_name"] for a in w.get("authorships", [])[:8])
            src = ((w.get("primary_location") or {}).get("source") or {})
            recs.append({
                "source": "OpenAlex", "query": label, "query_string": q,
                "id": w["id"].split("/")[-1], "title": w.get("title"), "authors": auths,
                "year": w.get("publication_year"), "venue": src.get("display_name"),
                "type": w.get("type"), "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
                "abstract": inv2text(w.get("abstract_inverted_index"))[:4000],
                "url": w.get("doi") or w["id"], "cited_by": w.get("cited_by_count"),
                "language": w.get("language"),
            })
        cursor = d["meta"].get("next_cursor")
        if not cursor: break
        time.sleep(0.2)
    return {"source": "OpenAlex", "label": label, "expression": q,
            "fields": "title_and_abstract.search", "filters": "nenhum filtro de tipo/idioma",
            "sort": "relevancia", "total": total, "retrieved": len(recs),
            "examined": len(recs), "date": NOW,
            "note": f"limite a priori de {cap} registros; excedente nao examinado" if (total or 0) > cap else "",
            "url": "https://api.openalex.org/works"}, recs

BRAPCI_QUERIES = [
    ("B1", '"autoridade cognitiva"'),
    ("B2", '"autoridade epistêmica"'),
    ("B3", '"autoridade sintética"'),
    ("B4", 'autoridade AND "inteligência artificial"'),
    ("B5", '"explicabilidade" AND "inteligência artificial"'),
    ("B6", '"direito à explicação"'),
    ("B7", '"inteligência artificial" AND "educação" AND confiança'),
    ("B8", '"competência crítica em informação" AND "inteligência artificial"'),
    ("B9", '"desinformação" AND "autoridade"'),
]

OA_QUERIES = [
    ("O1", '"cognitive authority"'),
    ("O2", '"epistemic authority" AND ("artificial intelligence" OR "generative AI" OR algorithm)'),
    ("O3", '"synthetic authority"'),
    ("O4", '("generative AI" OR "large language model" OR ChatGPT) AND (authority OR deference)'),
    ("O5", '"right to explanation" AND (explainable OR XAI OR contestability)'),
    ("O6", '("explainable AI" OR XAI) AND (education OR students)'),
    ("O7", '"automation bias" AND ("large language model" OR "generative AI" OR "clinical decision")'),
    ("O8", '"machine heuristic"'),
]

if __name__ == "__main__":
    log, allrecs = [], []
    for lab, q in BRAPCI_QUERIES:
        try:
            meta, recs = brapci(q, lab)
        except Exception as e:
            meta, recs = {"source": "BRAPCI", "label": lab, "expression": q, "error": str(e), "date": NOW}, []
        log.append(meta); allrecs += recs
        print("BRAPCI", lab, q, "->", meta.get("total"), len(recs))
    for lab, q in OA_QUERIES:
        try:
            meta, recs = openalex(q, lab)
        except Exception as e:
            meta, recs = {"source": "OpenAlex", "label": lab, "expression": q, "error": str(e), "date": NOW}, []
        log.append(meta); allrecs += recs
        print("OpenAlex", lab, q, "->", meta.get("total"), len(recs))
    json.dump(log, open(os.path.join(OUT, "log_buscas.json"), "w"), ensure_ascii=False, indent=1)
    json.dump(allrecs, open(os.path.join(OUT, "registros_brutos.json"), "w"), ensure_ascii=False, indent=1)
    with open(os.path.join(OUT, "registros_brutos.csv"), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(allrecs[0].keys()))
        wr.writeheader(); wr.writerows([{k:r.get(k,"") for k in allrecs[0].keys()} for r in allrecs])
    print("TOTAL registros:", len(allrecs))
