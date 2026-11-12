# -*- coding: utf-8 -*-
"""Estatísticas do corpus único completo, usadas na Figura 2.

Lê os registros únicos das bases (dados/02_triagem/registros_unicos_bases.csv) e os
registros novos da Web of Science (dados/01_buscas/wos_registros_novos.csv), ambos
separados por ponto e vírgula, e grava a distribuição por ano em
dados/02_triagem/estatisticas_corpus_completo.json.
"""
import csv, json, re, collections, os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASES = os.path.join(RAIZ, "dados", "02_triagem", "registros_unicos_bases.csv")
WOS = os.path.join(RAIZ, "dados", "01_buscas", "wos_registros_novos.csv")
SAIDA = os.path.join(RAIZ, "dados", "02_triagem", "estatisticas_corpus_completo.json")

def ler(caminho):
    with open(caminho, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))

def ano(reg):
    m = re.search(r"(19|20)\d{2}", str(reg.get("ano") or ""))
    return int(m.group(0)) if m else None

registros = ler(BASES) + ler(WOS)
anos = collections.Counter()
for r in registros:
    a = ano(r)
    if a:
        anos[str(a)] += 1

PREP = ("zenodo", "ssrn", "arxiv", "preprint", "preprints", "osf", "research square", "scielo preprints")
def preprint(r):
    v = (r.get("veiculo") or "").lower()
    return any(k in v for k in PREP)

dados = {
    "total_registros": len(registros),
    "com_ano": sum(anos.values()),
    "sem_ano": len(registros) - sum(anos.values()),
    "anos": dict(sorted(anos.items())),
    "preprints": sum(1 for r in registros if preprint(r)),
}
json.dump(dados, open(SAIDA, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

FAIXAS = [("<2000", lambda y: y < 2000), ("2000-2009", lambda y: 2000 <= y <= 2009),
          ("2010-2014", lambda y: 2010 <= y <= 2014), ("2015-2019", lambda y: 2015 <= y <= 2019),
          ("2020-2024", lambda y: 2020 <= y <= 2024), ("2025-2026", lambda y: y >= 2025)]
print("registros:", len(registros), "| sem ano:", dados["sem_ano"], "| preprints:", dados["preprints"])
for rotulo, teste in FAIXAS:
    print(f"  {rotulo}: {sum(v for y, v in anos.items() if teste(int(y)))}")
