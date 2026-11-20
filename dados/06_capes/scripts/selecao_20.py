#!/usr/bin/env python3
"""Fixa os 20 estudos retidos pela regra lexical (curadoria temática) e calcula
as estatísticas que alimentam o artigo v2.3.0 e a Figura 2."""
import csv, json, re, unicodedata

BASE = "/home/ubuntu/review/emenda/novas_bases/capes_manual"

CHAVES = [
    "Algorithmic Authority And Human Autonomy",
    "Machine learning and power relations",
    "Artificial Intelligence and Big Data in Global Politics",
    "The Artificial Intelligence Influence on Structure of Power",
    "Let Me Explain",
    "Neural Networks in Evidence-Based Governance",
    "Who Gets Believed When Machines Read Pain",
    "Explainable Artificial Intelligence in Critical Care Nursing",
    "Explainable Quality Assurance",
    "Artificial Intelligence in Classroom Teaching",
    "Human-AI Collaborative Teaching",
    "Ethical tensions in AI-mediated clinical communication",
    "Obviate the Need for Medical Doctors",
    "epistemic readiness gap",
    "Algorithmic Systems and Democratic Oversight",
    "Design for operator contestability",
    "From Kafka",
    "Autoridad algor",
    "Meta-influencers and algorithmic authority",
    "From rules to examples",
]

eleg = json.load(open(f"{BASE}/selecao_final.json"))
sel = []
for chave in CHAVES:
    achou = [l for l in eleg if chave.lower() in (l["titulo"] or "").lower()]
    if not achou:
        print("NAO ENCONTRADO:", chave)
        continue
    sel.append(achou[0])
print("retidos", len(sel))
for l in sel:
    print(f'{l["ano"]} | {l["veiculo"][:70]} | {l["titulo"][:80]}')
json.dump(sel, open(f"{BASE}/selecao_20.json", "w"), ensure_ascii=False, indent=1)

# distribuição de anos dos 348 candidatos (para o painel A da Figura 2)
cand = list(csv.DictReader(open(f"{BASE}/candidatos_capes.csv")))
anos = []
for r in cand:
    m = re.search(r"(19|20)\d\d", r.get("ano") or r.get("year") or "")
    if m:
        anos.append(int(m.group(0)))
print("candidatos", len(cand), "com ano", len(anos))
faixas = {"<2000": 0, "2000-09": 0, "2010-14": 0, "2015-19": 0, "2020-24": 0, "2025-26": 0}
for a in anos:
    if a < 2000:
        faixas["<2000"] += 1
    elif a <= 2009:
        faixas["2000-09"] += 1
    elif a <= 2014:
        faixas["2010-14"] += 1
    elif a <= 2019:
        faixas["2015-19"] += 1
    elif a <= 2024:
        faixas["2020-24"] += 1
    else:
        faixas["2025-26"] += 1
print(faixas)
json.dump({"com_ano": len(anos), "faixas": faixas}, open(f"{BASE}/capes_periodo.json", "w"), indent=1)
