# -*- coding: utf-8 -*-
"""Estatísticas do corpus único completo (base inicial + Web of Science sem duplicatas)."""
import json, re, collections

base = json.load(open("/home/ubuntu/review/triagem/registros_unicos.json"))
wos = [r for r in json.load(open("/home/ubuntu/review/wos/registros_wos.json")) if not r.get("duplicado")]

def ano(x):
    v = x.get("year") or x.get("ano") or ""
    m = re.search(r"(19|20)\d{2}", str(v))
    return int(m.group(0)) if m else None

anos = collections.Counter()
for r in base + wos:
    a = ano(r)
    if a:
        anos[str(a)] += 1

PREP = ("zenodo", "ssrn", "arxiv", "preprint", "preprints", "osf", "research square", "scielo preprints")
def prep(r):
    v = (r.get("venue") or r.get("veiculo") or "").lower()
    return any(k in v for k in PREP)

prep_total = sum(1 for r in base + wos if prep(r))
prep_bases = collections.Counter((r.get("venue") or r.get("veiculo") or "").lower().split(" (")[0]
                                 for r in base + wos if prep(r))

dados = {
    "total_registros": len(base) + len(wos),
    "com_ano": sum(anos.values()),
    "sem_ano": len(base) + len(wos) - sum(anos.values()),
    "anos": dict(sorted(anos.items())),
    "preprints": prep_total,
    "preprints_por_veiculo": dict(prep_bases.most_common(6)),
}
json.dump(dados, open("/home/ubuntu/review/triagem/estatisticas_corpus_completo.json", "w"),
          ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in dados.items() if k != "anos"}, ensure_ascii=False, indent=1))
faixas = [("<2000", lambda y: y < 2000), ("2000-2009", lambda y: 2000 <= y <= 2009),
          ("2010-2014", lambda y: 2010 <= y <= 2014), ("2015-2019", lambda y: 2015 <= y <= 2019),
          ("2020-2024", lambda y: 2020 <= y <= 2024), ("2025-2026", lambda y: y >= 2025)]
for lab, f in faixas:
    print(lab, sum(v for y, v in anos.items() if f(int(y))))
