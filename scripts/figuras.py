import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.family"] = "DejaVu Sans"

# ---------------- Figura 1: fluxo PRISMA-ScR ----------------
fig, ax = plt.subplots(figsize=(8.2, 5.9))
ax.set_xlim(0, 10); ax.set_ylim(0.55, 9.35); ax.axis("off")

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
    ["BRAPCI: 49 registros (9 consultas)  |  OpenAlex: 1.219 registros (8 consultas)",
     "Google Acadêmico: 80 examinados  |  Rastreamento de citações: 106  |  Busca dirigida: 19",
     "Total identificado: 1.473 registros"])
box(0.9, 5.95, 8.2, 1.15, "Triagem por título e resumo",
    ["Registros após remoção de 41 duplicatas: 1.432",
     "Excluídos: 1.377 (idioma, período, tema não central, tipo de publicação)"])
box(0.9, 4.35, 8.2, 1.15, "Elegibilidade",
    ["Textos completos ou resumos avaliados: 68",
     "Excluídos após leitura: 13 (E2: 5; E4: 4; E5: 4)"])
box(0.9, 2.55, 8.2, 1.35, "Inclusão",
    ["Estudos incluídos na síntese: 55",
     "Fundamentos 13  |  Autoridade e IA 19  |  Explicabilidade e direito 14  |  Educação 9"])
arrow(7.5, 7.14)
arrow(5.9, 5.54)
arrow(4.3, 3.94)
ax.text(0.9, 1.05, "E1 tema não central  |  E2 contribuição apenas técnica  |  E3 duplicata\nE4 sem texto ou resumo acessível  |  E5 metadados não verificáveis  |  E6 comentário sem argumentação",
        fontsize=6.8, va="top", color="#444444")
plt.tight_layout()
plt.savefig("/home/ubuntu/review/figuras/fig1_fluxo.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()

# ---------------- Figura 2: distribuicao temporal ----------------
st = json.load(open("/home/ubuntu/review/triagem/estatisticas.json"))
anos = {int(k): v for k, v in st["anos"].items()}
faixas = [("<2000", lambda y: y < 2000), ("2000-2009", lambda y: 2000 <= y <= 2009),
          ("2010-2014", lambda y: 2010 <= y <= 2014), ("2015-2019", lambda y: 2015 <= y <= 2019),
          ("2020-2024", lambda y: 2020 <= y <= 2024), ("2025-2026", lambda y: y >= 2025)]
vals = [sum(v for y, v in anos.items() if f(y)) for _, f in faixas]
labels = [l for l, _ in faixas]

fig, ax = plt.subplots(figsize=(6.4, 2.3))
bars = ax.bar(labels, vals, color=["#9DB2D3", "#9DB2D3", "#7C96C4", "#5E7DB4", "#3C5D9E", "#1F3864"], width=0.62)
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width() / 2, v + 8, str(v), ha="center", fontsize=7.5, color="#1F3864")
ax.set_ylabel("Registros únicos", fontsize=8)

ax.tick_params(labelsize=7.5)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
ax.set_ylim(0, max(vals) * 1.18)
plt.tight_layout()
plt.savefig("/home/ubuntu/review/figuras/fig2_periodo.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print("figuras ok", vals)
