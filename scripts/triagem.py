import json, re, unicodedata, csv, os
from collections import defaultdict

BASE = "/home/ubuntu/review"
recs = json.load(open(f"{BASE}/buscas/registros_brutos.json"))
print("registros brutos:", len(recs))

def norm(s):
    s = (s or "").lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

# ---- dedupe
by_key = {}
dups = 0
for r in recs:
    doi = (r.get("doi") or "").lower().strip()
    key = "doi:" + doi if doi else "t:" + norm(r.get("title"))[:90] + "|" + str(r.get("year"))
    if key in by_key:
        dups += 1
        # keep first, register additional source
        by_key[key]["tambem_em"] = (by_key[key].get("tambem_em") or "") + ";" + r["source"] + "/" + r["query"]
        continue
    r = dict(r); r["key"] = key; r["tambem_em"] = ""
    by_key[key] = r
uniq = list(by_key.values())
print("duplicatas removidas:", dups, "| registros unicos:", len(uniq))

# ---- idioma / ano
def lang_ok(r):
    t = (r.get("title") or "") + " " + (r.get("abstract") or "")
    lang = (r.get("language") or "")
    if lang in ("en", "pt", "es"): return True
    if not lang:
        # heuristica: presenca de palavras funcionais
        pt = len(re.findall(r"\b(que|para|com|dos|das|uma|não|informação)\b", t, re.I))
        en = len(re.findall(r"\b(the|and|of|with|this|that|information)\b", t, re.I))
        es = len(re.findall(r"\b(los|las|para|con|este|esta|información)\b", t, re.I))
        return max(pt, en, es) > 0
    return False

AUTH = ["authority", "autoridade", "autoridad", "credib", "credenc", "trust", "confian", "confianza",
        "deferen", "deferên", "deferenc", "persuas", "epistemic", "epistêmic", "epistémic", "expertise",
        "overreliance", "dependên", "dependenc", "heuristic", "heurístic"]
AI = ["artificial intelligence", "inteligência artificial", "inteligencia artificial", "ai ", " ia ",
      "generative", "gerativa", "generativ", "large language", "llm", "chatgpt", "gpt", "algorithm",
      "algoritm", "machine learning", "aprendizado de máquina", "automation", "automação", "automated",
      "chatbot", "model", "modelo", "xai", "explainab", "explicab", "interpretab", "black box", "caixa-preta",
      "decision support", "recommender", "recomendação"]

def has(t, terms):
    return any(x in t for x in terms)

f1, f2, f3 = [], [], []
for r in uniq:
    if not lang_ok(r):
        r["motivo"] = "E_idioma"; f1.append(r); continue
    y = r.get("year")
    try: y = int(str(y)[:4])
    except: y = None
    r["ano"] = y
    if y and (y < 1983 or y > 2026):
        r["motivo"] = "E_periodo"; f1.append(r); continue
    t = norm((r.get("title") or "") + " " + (r.get("abstract") or ""))
    ttl = norm(r.get("title") or "")
    # fundamentos: autoridade no titulo
    fund = ("authority" in ttl or "autoridade" in ttl or "autoridad" in ttl) and not has(ttl, ["synthetic authority in religion"])
    top = has(t, AUTH) and has(t, AI)
    if fund or top:
        f2.append(r)
    else:
        r["motivo"] = "E1_tema"; f3.append(r)

print("excluidos por idioma/periodo:", len(f1))
print("excluidos na triagem 1 (E1-tema):", len(f3))
print("elegiveis para leitura de titulo/resumo:", len(f2))

json.dump(uniq, open(f"{BASE}/triagem/registros_unicos.json", "w"), ensure_ascii=False, indent=1)
json.dump(f2, open(f"{BASE}/triagem/candidatos_t1.json", "w"), ensure_ascii=False, indent=1)

with open(f"{BASE}/triagem/candidatos_t1.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["#", "id", "fonte", "ano", "titulo", "autores", "veiculo", "doi", "tipo"])
    for i, r in enumerate(sorted(f2, key=lambda x: -(x.get("cited_by") or 0)), 1):
        w.writerow([i, r.get("id"), r.get("source"), r.get("year"), r.get("title"), r.get("authors"),
                    r.get("venue"), r.get("doi"), r.get("type")])

# lista compacta para revisao manual
for i, r in enumerate(sorted(f2, key=lambda x: -(x.get("cited_by") or 0)), 1):
    print(f"{i}\t{r.get('year')}\t{(r.get('title') or '')[:95]}\t{r.get('source')}")
