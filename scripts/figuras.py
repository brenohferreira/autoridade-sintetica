# -*- coding: utf-8 -*-
"""Figuras da versão enxuta: 57 estudos analisados, com o fluxo recalculado
para o recorte de fundamentos, autoridade e IA e explicabilidade."""
import json, sys, collections
sys.path.insert(0, "/home/ubuntu/review/scripts")
from dados import ESTUDOS
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.family"] = "DejaVu Sans"

# ---------------- Figura 1: fluxo PRISMA-ScR ----------------
fig, ax = plt.subplots(figsize=(8.2, 5.9))
ax.set_xlim(0, 10); ax.set_ylim(0.35, 9.35); ax.axis("off")

def box(x, y, w, h, title, lines, fc="#F2F5FA"):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.08",
                       linewidth=1.1, edgecolor="#1F3864", facecolor=fc)
    ax.add_patch(p)
    ax.text(x + 0.2, y + h - 0.26, title, fontsize=9, weight="bold", color="#1F3864", va="top")
    ty = y + h - 0.58
    for ln in lines:
        ax.text(x + 0.2, ty, ln, fontsize=7.6, va="top", color="#222222")
        ty -= 0.26

def arrow(y1, y2):
    ax.add_patch(FancyArrowPatch((5, y1), (5, y2), arrowstyle="-|>", mutation_scale=12,
                                 linewidth=1.0, color="#1F3864"))

box(0.9, 7.55, 8.2, 1.55, "Identificação",
    ["BRAPCI: 48 (8 consultas)  |  OpenAlex: 1.019 (7 consultas)  |  Web of Science: 1.407 (7 consultas)",
     "Google Acadêmico: 70 examinados  |  Rastreamento de citações: 106  |  Busca dirigida: 8",
     "Total identificado: 2.658 registros"])
box(0.9, 5.95, 8.2, 1.15, "Remoção de duplicatas",
    ["Duplicatas removidas: 372 (42 entre bases; 317 na Web of Science; 13 no rastreamento)",
     "Registros únicos submetidos à triagem: 2.286"])
box(0.9, 4.35, 8.2, 1.15, "Triagem por título e resumo",
    ["Triados: 2.286  |  Excluídos: 2.229",
     "Motivos: tipo de documento, domínio alheio ao escopo, tema não central"])
box(0.9, 2.55, 8.2, 1.35, "Inclusão",
    ["Estudos incluídos na revisão: 57 (12 com texto completo; 45 a partir do resumo)",
     "Fundamentos 18  |  Autoridade e IA 30  |  Explicabilidade e contestação 9"])
arrow(7.5, 7.14)
arrow(5.9, 5.54)
arrow(4.3, 3.94)
ax.text(0.9, 1.85, "Estudos analisados neste artigo: 57",
        fontsize=7.2, va="top", color="#1F3864", weight="bold")
ax.text(0.9, 1.05, "E1 tema não central  |  E2 contribuição apenas técnica  |  E3 duplicata\nE4 sem texto ou resumo acessível  |  E5 metadados não verificáveis  |  E6 comentário sem argumentação",
        fontsize=6.8, va="top", color="#444444")
plt.tight_layout()
plt.savefig("/home/ubuntu/review/figuras/fig1_fluxo_sx.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()

# ---------------- Figura 2: temporal e areas (57 estudos) ----------------
EXC = ("BRASIL. LEI", "BRASIL. CONSELHO", "UNIÃO EUROPEIA. REGULAMENTO", "WACHTER", "GOODMAN",
       "KAMINSKI", "EDWARDS", "NANNINI", "KIM, T", "YU, L", "CHEN, X")
idx_ok = [i for i, e in enumerate(ESTUDOS)
          if not e["ref"].upper().startswith(tuple(t.upper() for t in EXC))
          and not e["frente"].startswith("4")]
linhas = [l for i, l in enumerate(json.load(open("/home/ubuntu/review/biblio/linhas_biblio.json", encoding="utf-8")))
          if i in set(idx_ok)]

d = json.load(open("/home/ubuntu/review/buscas/distribuicao_limpa.json", encoding="utf-8"))
labels = ["<2000", "2000-09", "2010-14", "2015-19", "2020-24", "2025-26"]
vals = [d["faixas"][l] for l in labels]
areas = collections.Counter(l["area"] for l in linhas)
ordem = ["Computação e IHC", "Ciência da Informação", "Filosofia", "Comunicação",
         "Livros e anais", "Gestão e saúde", "Outros veículos"]
areas_vals = [areas[k] for k in ordem]

fig, (ax, ax2) = plt.subplots(1, 2, figsize=(6.1, 2.15), gridspec_kw={"width_ratios": [1.0, 1.15]})
bars = ax.bar(labels, vals, color=["#9DB2D3", "#9DB2D3", "#7C96C4", "#5E7DB4", "#3C5D9E", "#1F3864"], width=0.64)
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width() / 2, v + 30, f"{v:,}".replace(",", "."), ha="center", fontsize=6.2, color="#1F3864")
ax.set_ylabel("Registros únicos", fontsize=6.6)
ax.tick_params(labelsize=6, axis="x", labelrotation=40)
ax.tick_params(labelsize=6, axis="y")
ax.set_title("A) Registros triados, por período", fontsize=6.8, loc="left", color="#1F3864")
for sp in ["top", "right"]:
    ax.spines[sp].set_visible(False)
ax.set_ylim(0, max(vals) * 1.20)

y = range(len(ordem))
hb = ax2.barh(list(y), areas_vals, color="#5E7DB4", height=0.66)
for b, v in zip(hb, areas_vals):
    ax2.text(b.get_width() + 0.5, b.get_y() + b.get_height() / 2, str(v), va="center", fontsize=6, color="#1F3864")
ax2.set_yticks(list(y)); ax2.set_yticklabels(ordem, fontsize=6)
ax2.invert_yaxis()
ax2.set_xlim(0, max(areas_vals) * 1.22)
ax2.tick_params(labelsize=6)
ax2.set_title("B) Estudos analisados, por área do veículo", fontsize=6.8, loc="left", color="#1F3864")
for sp in ["top", "right"]:
    ax2.spines[sp].set_visible(False)
plt.tight_layout()
plt.savefig("/home/ubuntu/review/figuras/fig2_periodo_sx.png", dpi=400, bbox_inches="tight", facecolor="white")
plt.close()
print("figuras sx ok", dict(zip(ordem, areas_vals)), dict(zip(labels, vals)))
