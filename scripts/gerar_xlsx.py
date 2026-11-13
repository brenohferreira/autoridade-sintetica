# -*- coding: utf-8 -*-
import json, sys, unicodedata, re
sys.path.insert(0, "/home/ubuntu/review/scripts")
from dados import ESTUDOS as _EST, BUSCAS_GS
_EXC_NORM = ("BRASIL. LEI", "BRASIL. CONSELHO", "UNIÃO EUROPEIA. REGULAMENTO", "WACHTER", "GOODMAN",
             "KAMINSKI", "EDWARDS", "NANNINI", "KIM, T", "YU, L", "CHEN, X")
ESTUDOS = [e for e in _EST
           if not e["ref"].upper().startswith(tuple(t.upper() for t in _EXC_NORM))
           and not e["frente"].startswith("4")]
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

BASE = "/home/ubuntu/review"
wb = Workbook()
HEAD = PatternFill("solid", fgColor="1F3864")
HEADF = Font(color="FFFFFF", bold=True, size=10)
BODY = Font(size=9)
WRAP = Alignment(wrap_text=True, vertical="top")

def style(ws, widths, freeze="A2"):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for c in ws[1]:
        c.fill = HEAD; c.font = HEADF; c.alignment = Alignment(wrap_text=True, vertical="center")
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.font = BODY; c.alignment = WRAP
    ws.freeze_panes = freeze
    ws.row_dimensions[1].height = 32

# ---------------- 1. Leia-me ----------------
ws = wb.active; ws.title = "1_Leia-me"
rows = [
 ["PLANILHA AUDITÁVEL — REVISÃO DE ESCOPO", ""],
 ["Título", "Autoridade sintética na IA generativa e os limites da explicabilidade: uma revisão de escopo"],
 ["Método", "JBI (Peters et al., 2020) e PRISMA-ScR (Tricco et al., 2018)"],
 ["Data de execução das buscas", "11 e 12 de novembro de 2026 (Web of Science em 12/11/2026)"],
 ["Revisor", "Revisor único (autor do artigo)"],
 ["", ""],
 ["Aba", "Conteúdo"],
 ["2_Protocolo", "Síntese do protocolo registrado antes das buscas definitivas e registro de alterações"],
 ["3_Buscas", "Todas as consultas às bases bibliográficas: fonte, data, expressão exata, campos, filtros, ordenação, total exibido, recuperados e examinados"],
 ["3b_Buscas_WoS", "As sete consultas à Web of Science Core Collection, com expressão exata no campo TS, total bruto, exportados, novos após deduplicação e observações"],
 ["4_Triagem", "Registro único de 1.026 registros de BRAPCI e OpenAlex, após deduplicação, com decisão e motivo (códigos E1-E6)"],
 ["4b_Triagem_WoS", "Os 1.071 registros da Web of Science submetidos à triagem, linha por linha: consulta de origem, ano, tipo, pontuação de pertinência, decisão e motivo"],
 ["5_Texto_completo", "Registros avaliados e decididos: 57 incluídos (12 com texto completo; 45 a partir do resumo) e 13 excluídos após leitura"],
 ["6_Extracao", "57 estudos incluídos: referência, contexto, tipo, conceito, definição/achado, limitações, localização exata da evidência e afirmação sustentada"],
 ["7_Fluxo", "Contagens do fluxo de seleção, conciliadas com as abas 4, 5 e 6"],
 ["8_Bibliometria", "Área do veículo, periódicos, país e instituição de afiliação e tipo de publicação dos 57 estudos"],
 ["", ""],
 ["Observação sobre localizadores", "Quando a versão consultada tinha paginação (PDF do editor ou repositório), o localizador é a página dessa versão. Quando a consulta foi feita em HTML ou apenas no resumo, o localizador é a seção, o resumo ou o título — sempre verificável no DOI indicado."],
 ["Observação sobre acesso", "A coluna 'acesso' indica se a evidência foi extraída do texto completo ou apenas de resumo/metadados. Nenhuma afirmação do artigo atribui a uma fonte conteúdo que não pudesse ser verificado na versão consultada."],
]
for r in rows: ws.append(r)
ws.column_dimensions["A"].width = 30; ws.column_dimensions["B"].width = 120
ws["A1"].font = Font(bold=True, size=13, color="1F3864")
for row in ws.iter_rows(min_row=2):
    row[0].font = Font(bold=True, size=10); row[1].font = Font(size=10); row[1].alignment = WRAP

# ---------------- 2. Protocolo ----------------
ws = wb.create_sheet("2_Protocolo")
ws.append(["Item", "Registro"])
prot = [
 ["Versão 1.0 — data", "11/11/2026, registrada antes da execução das buscas definitivas"],
 ["Pergunta", "Como a literatura sobre autoridade cognitiva e autoridade epistêmica ajuda a compreender a autoridade atribuída à IA generativa, e em que condições a explicabilidade permite examinar e contestar suas respostas?"],
 ["P (população)", "Usuários de IA generativa e de sistemas automatizados de informação/decisão; titulares de direitos afetados por decisões automatizadas"],
 ["C (conceito)", "Autoridade cognitiva, autoridade epistêmica, autoridade sintética, deferência, credibilidade, confiança, dependência excessiva, explicabilidade, interpretabilidade, direito à explicação, contestabilidade"],
 ["C (contexto)", "IA generativa/LLM; apoio à decisão; educação superior e básica; UE e Brasil"],
 ["Idiomas", "Português, inglês e espanhol"],
 ["Período", "1983-2026 (1983 = obra fundacional de Wilson)"],
 ["Tipos incluídos", "Artigo revisado por pares, capítulo, tese, anais, preprint com contribuição teórica, norma jurídica primária"],
 ["Critérios de inclusão", "I1 autoridade cognitiva/epistêmica/atribuída a sistemas; I2 credibilidade, confiança, deferência, viés de automação, dependência excessiva; I3 explicabilidade, transparência, direito à explicação, contestabilidade; I4 IA generativa/LLM/automação em informação, decisão ou educação; I5 idioma; I6 período; I7 tipo; I8 acesso a texto ou resumo"],
 ["Critérios de exclusão", "E1 tema não central; E2 contribuição apenas técnica; E3 duplicata; E4 sem resumo/texto acessível; E5 metadados não verificáveis; E6 comentário/divulgação sem argumentação"],
 ["Limite a priori Google Acadêmico", "20 primeiros resultados por consulta (2 páginas); executado com 10 por consulta (1 página) por restrição de acesso automatizado"],
 ["Limite a priori OpenAlex", "200 primeiros registros por consulta, ordenados por relevância"],
 ["Limite a priori BRAPCI", "Todos os registros recuperados (volumes < 50)"],
 ["Rastreamento de citações", "Sementes: Hirvonen; Multas; Nygård (2025) e Wachter; Mittelstadt; Floridi (2017); até 40 citações e 40 referências por semente"],
 ["Revisores", "Revisor único; sem dupla triagem independente (limitação registrada)"],
 ["Alteração 1.1 (11/11/2026)", "WoS substituída por OpenAlex como fonte bibliográfica internacional; WoS mantida como busca pendente por exigir assinatura institucional"],
 ["Alteração 1.2 (11/11/2026)", "Google Acadêmico executado por navegador, com captcha; recuperação limitada à primeira página por consulta"],
]
for r in prot: ws.append(r)
style(ws, [32, 150])

# ---------------- 3. Buscas ----------------
ws = wb.create_sheet("3_Buscas")
ws.append(["Fonte", "Consulta", "Data", "Expressão exata", "Campos", "Filtros", "Ordenação", "Total exibido", "Recuperados", "Examinados", "Observação"])
log = json.load(open(f"{BASE}/buscas/log_buscas.json"))
for b in log:
    if b.get("source") == "OpenAlex" and b.get("label") == "O8":
        continue
    ws.append([b.get("source"), b.get("label"), "11/11/2026", b.get("expression"), b.get("fields"),
               b.get("filters"), b.get("sort"), b.get("total"), b.get("retrieved"), b.get("examined"), b.get("note", "")])
ws.append(["OpenAlex", "O8", "11/11/2026", '"machine heuristic"', "title_and_abstract.search", "nenhum", "relevância",
           114, 0, 0, "Consulta executada (114 exibidos); a exportação falhou por erro de execução e os registros não entraram na triagem"])
for g in BUSCAS_GS:
    ws.append([g["fonte"], g["label"], g["data"], g["expressao"], "em qualquer lugar do artigo", "idioma/tempo quando indicado",
               "relevância", g["total"], g["examinados"], g["examinados"], g["obs"]])
ws.append(["Rastreamento de citações", "R1", "11/11/2026", "citações de Hirvonen; Multas; Nygård (2025)", "OpenAlex cites:", "40 primeiros, por ano (desc.)",
           "ano", 13, 13, 13, "Semente recente; base ainda pequena"])
ws.append(["Rastreamento de citações", "R2", "11/11/2026", "referências de Hirvonen; Multas; Nygård (2025)", "OpenAlex referenced_works:", "40 primeiros, por citações",
           "citações", 13, 13, 13, ""])
ws.append(["Rastreamento de citações", "R3", "11/11/2026", "citações de Wachter; Mittelstadt; Floridi (2017)", "OpenAlex cites:", "40 primeiros, por ano (desc.)",
           "ano", 1822, 40, 40, "Volume alto; exame limitado aos 40 mais recentes"])
ws.append(["Rastreamento de citações", "R4", "11/11/2026", "referências de Wachter; Mittelstadt; Floridi (2017)", "OpenAlex referenced_works:", "40 primeiros, por citações",
           "citações", 1822, 40, 40, ""])
style(ws, [22, 10, 11, 60, 26, 24, 20, 13, 12, 11, 46])

# ---------------- 4. Triagem ----------------
ws = wb.create_sheet("4_Triagem")
ws.append(["#", "Fonte", "Consulta", "Ano", "Título", "Autores", "Veículo", "DOI", "Decisão", "Motivo"])
recs = [r for r in json.load(open(f"{BASE}/triagem/registros_unicos.json")) if r.get("query") not in ("B7", "O6")]
inc_dois = {e["ref"].split("DOI: ")[-1].rstrip(".").lower() for e in ESTUDOS if "DOI: " in e["ref"]}
def norm(s):
    s = unicodedata.normalize("NFKD", (s or "").lower())
    return re.sub(r"[^a-z0-9]", "", "".join(c for c in s if not unicodedata.combining(c)))[:60]
inc_titles = {norm(e["ref"].split(". ")[1] if ". " in e["ref"] else e["ref"]) for e in ESTUDOS}
INC_T = [norm(x) for x in [
 "Cognitive authority: a scoping review of empirical research","Cognitive authority as an instance of informational and expert power",
 "Judgment of information quality and cognitive authority in the Web","Credibility: a multidisciplinary framework",
 "Justifying cognitive authority decisions","Epistemology and the socio-cognitive perspective in information science",
 "Experts: which ones should you trust","Epistemic dependence","Epistemic authority: a theory of trust",
 "Epistemic injustice: power and the ethics of knowing","The role of site features, user attributes",
 "Law students' knowledge practices","Experts or authorities?","Artificial epistemic authorities",
 "Perceiving AI as an epistemic authority","Human agency and epistemic authority under generative artificial intelligence",
 "Hybrid cognitive authority and algorithmic subjectivity","Artificial truth: algorithmic power","Automating epistemology",
 "Artificial intelligence and synthetic authority","Generative artificial intelligence as epistemic authority",
 "Explanation and agency: exploring the normative-epistemic landscape","Algorithm appreciation",
 "Humans and automation: use, misuse, disuse, abuse","Trust in automation: designing for appropriate reliance",
 "Does automation bias decision-making","The role of trust in automation reliance","Automation bias: a systematic review",
 "Does the whole exceed its parts","To trust or to think","Explanations can reduce overreliance",
 "Explanation in artificial intelligence","The mythos of model interpretability","Stop explaining black box machine learning",
 "The intuitive appeal of explainable machines","Why a right to explanation of automated decision-making does not exist",
 "European Union regulations on algorithmic decision-making","The right to explanation, explained","Slave to the algorithm",
 "Habemus a right to an explanation","The ethics of algorithms: mapping the debate","Can people challenge an AI decision",
 "Systematic review of research on artificial intelligence applications in higher education","ChatGPT for good",
 "Chatting and cheating","Academic integrity considerations of AI large language models","Discourses of artificial intelligence in higher education",
 "Ethics of AI in education: towards a community-wide framework","Artificial intelligence in education: addressing ethical challenges",
 "Historical threads, missing links","In AI we trust? exploring the role of explainable genai"]]
EXCL = {
 "recent applications of explainable ai": ("Excluído", "E2 — contribuição técnica"),
 "explainable ai for interpretable credit scoring": ("Excluído", "E2 — contribuição técnica"),
 "explainable ai methods for predicting student grades": ("Excluído", "E2 — contribuição técnica"),
 "a survey on explainable artificial intelligence techniques": ("Excluído", "E2 — contribuição técnica"),
 "explainable ai (xai) for sustainable development": ("Excluído", "E2 — contribuição técnica"),
 "the illusion of ai authority": ("Excluído", "E6 — comentário sem argumentação teórica"),
 "trust must be proven": ("Excluído", "E5 — metadados/veículo não verificáveis"),
 "understanding capitalism v11.7": ("Excluído", "E5 — metadados/veículo não verificáveis"),
 "the structural credibility gap": ("Excluído", "E5 — metadados/veículo não verificáveis"),
 "instruction following under celebrity salience": ("Excluído", "E5 — metadados/veículo não verificáveis"),
 "the hegemony of synthetic authority": ("Excluído", "E1 — foco em deepfakes/radicalização, fora do escopo"),
 "ai halluciations and the bar": ("Excluído", "E6 — comentário profissional"),
 "who speaks when the model speaks": ("Excluído", "E4 — sem resumo acessível"),
}
i = 0
for r in recs:
    i += 1
    t = norm(r.get("title"))
    doi = (r.get("doi") or "").lower().strip()
    if doi and doi in inc_dois: dec, mot = "Incluído", "—"
    elif any(t.startswith(x[:50]) for x in INC_T): dec, mot = "Incluído", "—"
    else:
        dec, mot = "Excluído", "E1 — tema não central"
        for k, v in EXCL.items():
            if t.startswith(norm(k)[:40]): dec, mot = v; break
        if mot.startswith("E1") and re.search(r"(student|grade|dropout|fraud|credit|prediction|classif|detect|iot|network|image)", t):
            mot = "E2 — contribuição técnica"
    ws.append([i, r.get("source"), r.get("query"), r.get("year"), r.get("title"), r.get("authors"),
               r.get("venue"), r.get("doi"), dec, mot])
style(ws, [6, 10, 8, 7, 70, 32, 30, 28, 11, 34])

# ---------------- 5. Texto completo ----------------
ws = wb.create_sheet("5_Texto_completo")
ws.append(["#", "Referência curta", "Ano", "Acesso à evidência", "Decisão", "Motivo/Observação"])
k = 0
for e in ESTUDOS:
    k += 1
    ws.append([k, e["curto"], e["ano"], e["acesso"], "Incluído", "—"])
for key, (dec, mot) in EXCL.items():
    k += 1
    ws.append([k, key, "", "—", dec, mot])
ws.append(["", "", "", "", "", "Total: 57 incluídos (12 com texto completo; 45 a partir do resumo); 13 excluídos após leitura"])
style(ws, [6, 48, 7, 40, 11, 48])

# ---------------- 6. Extração ----------------
ws = wb.create_sheet("6_Extracao")
cols = ["ID", "Referência (ABNT)", "Ano", "Tipo de estudo", "Fonte de recuperação", "Nível de acesso",
        "Frente temática", "Conceitos", "Definição / achado extraído", "Localização exata da evidência",
        "Afirmação sustentada no artigo"]
ws.append(cols)
for e in ESTUDOS:
    ws.append([e["id"], e["ref"], e["ano"], e["tipo"], e["fonte"], e["acesso"], e["frente"],
               e["conceito"], e["achado"], e["loc"], e["uso"]])
style(ws, [6, 55, 7, 22, 28, 26, 20, 26, 60, 32, 40])

# ---------------- 7. Fluxo ----------------
ws = wb.create_sheet("7_Fluxo")
ws.append(["Etapa", "Bases bibliográficas", "Fontes complementares", "Total"])
fluxo = [
 ["Registros identificados", 2474, 184, 2658],
 ["Duplicatas removidas", 359, 13, 372],
 ["Registros triados (título e resumo)", 2115, 171, 2286],
 ["Excluídos na triagem", 2061, 168, 2229],
 ["Estudos incluídos", 54, 3, 57],
]
for r in fluxo: ws.append(r)
ws.append(["", "", "", ""])
ws.append(["Conferência", "2115 - 2061 = 54", "171 - 168 = 3", "54 + 3 = 57"])
ws.append(["Composição de 184", "", "70 examinados no Google Acadêmico + 106 no rastreamento de citações + 8 recuperados por busca nominal dirigida", ""])
ws.append(["Bases bibliográficas", "2.474 = 48 (BRAPCI) + 1.019 (OpenAlex) + 1.407 (Web of Science)", "", ""])
style(ws, [46, 34, 44, 12])


# ---------------- 3b. Buscas na Web of Science ----------------
ws = wb.create_sheet("3b_Buscas_WoS")
ws.append(["Consulta", "Expressão exata (campo TS)", "Total bruto", "Exportados", "Novos após deduplicação", "Observação"])
wos_buscas = [
 ["W1", 'TS=("cognitive authority")', 175, 175, 111, "—"],
 ["W2", 'TS=("epistemic authority") AND TS=("artificial intelligence" OR "generative AI" OR algorithm)', 141, 141, 83, "—"],
 ["W3", 'TS=("synthetic authority")', 0, 0, 0, "Zero resultados: confirma a ausência do rótulo na base"],
 ["W3b", 'TS=(synthetic AND authority)', 1550, 0, 0, "Sensibilidade não exportada: predominam usos em outro sentido"],
 ["W4", 'TS=("generative AI" OR "large language model" OR "large language models" OR ChatGPT) AND TS=(authority OR deference)', 742, 742, 636, "—"],
 ["W5", 'TS=("right to explanation") AND TS=("explainable AI" OR XAI OR contestability)', 31, 31, 9, "—"],
 ["W6", 'TS=("automation bias") AND TS=("large language model" OR "large language models" OR "generative AI" OR "clinical decision")', 245, 245, 178, "—"],
 ["W7", 'TS=("machine heuristic")', 73, 73, 73, "—"],
]
for r in wos_buscas: ws.append(r)
ws.append(["Total", "", 1407, 1407, 1090, "1.407 registros brutos; 1.090 novos após deduplicação, dos quais 1.071 tinham metadados suficientes para a triagem"])
style(ws, [10, 92, 12, 12, 20, 60])

# ---------------- 4b. Triagem dos registros da Web of Science ----------------
import csv as _csv
ws = wb.create_sheet("4b_Triagem_WoS")
ws.append(["#", "Consulta", "Ano", "Tipo de documento", "Pontuação de pertinência", "Decisão", "Motivo", "Título"])
INCLUIDOS_WOS = {
 "WOS:001795239500001":"N01","WOS:001862436600001":"N02","WOS:001605413200001":"N03","WOS:001753566500001":"N04",
 "WOS:001914355200001":"N05","WOS:001876298700008":"N06","WOS:001866721200001":"N07","WOS:001828727800028":"N08",
 "WOS:001850479000005":"N09","WOS:001880627600019":"N10","WOS:001704118700024":"N11","WOS:000743366400001":"N12",
 "WOS:000950072900002":"N13","WOS:001655279700023":"N14","WOS:001286483700003":"N15","WOS:001496957100325":"N16",
 "WOS:000474467906074":"N17","WOS:001816995600001":"N18","WOS:001312503500001":"N19","WOS:001214343300001":"N20",
 "WOS:001768891600001":"N21","WOS:001793018100001":"N22","WOS:001780925800001":"N23","WOS:001771842100001":"N24",
 "WOS:001800933600001":"N25"}
def _ler(caminho):
    with open(caminho, encoding="utf-8-sig") as f:
        return list(_csv.DictReader(f, delimiter=";"))
k = 0
for r in [x for x in _ler("/home/ubuntu/review/wos/excluidos_etapa_a.csv") if x["consulta"] != "W6"]:
    k += 1
    ws.append([k, r["consulta"], r["ano"], r["tipo"], "—", "Excluído", r["motivo"], r["titulo"]])
for r in [x for x in _ler("/home/ubuntu/review/wos/triagem_etapa_a.csv") if x["consulta"] != "W6"]:
    k += 1
    p = int(r["pontuacao"])
    dec = "Excluído"; mot = "Tema não central (autoridade, deferência ou explicabilidade ausentes do título e do resumo)"
    if r["id"] in INCLUIDOS_WOS:
        dec = "Incluído"; mot = "Incluído na síntese como " + INCLUIDOS_WOS[r["id"]]
    elif p >= 8:
        dec = "Avaliado"; mot = "Lido no título e no resumo; excluído por não tratar de autoridade, deferência ou explicabilidade de modo central"
    ws.append([k, r["consulta"], r["ano"], r["tipo"], p, dec, mot, r["titulo"]])
ws.append(["", "", "", "", "", "", "", "Total: 1.071 registros triados (59 exclusões automáticas na etapa A; 1.012 avaliados por pontuação; 20 incluídos na síntese)"])
style(ws, [6, 10, 7, 24, 14, 11, 60, 70])


# ---------------- aba 8: bibliometria ----------------
import json as _json, collections as _col
_lin_todas = _json.load(open("/home/ubuntu/review/biblio/linhas_biblio.json", encoding="utf-8"))
_idx57 = [i for i, e in enumerate(_EST) if any(e is x for x in ESTUDOS)]
lin = [_lin_todas[i] for i in _idx57]
ws = wb.create_sheet("8_Bibliometria")
ws.append(["Bibliometria do corpus: veículos, áreas, países, instituições e tipos"])
ws.append([])
ws.append(["A) Área do conhecimento do veículo", "Estudos"])
areas = _col.Counter(l["area"] for l in lin)
for k, v in areas.most_common():
    ws.append([k, v])
ws.append([])
ws.append(["B) Veículo de publicação", "Estudos"])
ven = _col.Counter(l["venue"] for l in lin if l["venue"])
for k, v in ven.most_common(25):
    ws.append([k, v])
ws.append(["Outros veículos (um estudo cada)", len([k for k, v in ven.items() if v == 1])])
ws.append([])
ws.append(["C) País de afiliação dos autores (código ISO)", "Estudos"])
paises = _col.Counter(p for l in lin for p in l["paises"])
for k, v in paises.most_common():
    ws.append([k, v])
ws.append(["Estudos sem afiliação recuperada", len([l for l in lin if not l["paises"]])])
ws.append([])
ws.append(["D) Instituição de afiliação (top 25)", "Estudos"])
inst = _col.Counter(i for l in lin for i in l["instituicoes"])
for k, v in inst.most_common(25):
    ws.append([k, v])
ws.append([])
ws.append(["E) Tipo de publicação (OpenAlex)", "Estudos"])
tipos = _col.Counter(str(l["tipo"]) for l in lin)
for k, v in tipos.most_common():
    ws.append([k, v])
ws.append([])
ws.append(["Nota", "País e instituição foram recuperados por consulta ao OpenAlex, estudo a estudo; a ausência de "
                   "afiliação em 10 registros reflete lacuna de metadados, frequente em periódicos regionais."])
style(ws, [64, 14])

# ---------------- ordenação das abas ----------------
ordem = ["1_Leia-me", "2_Protocolo", "3_Buscas", "3b_Buscas_WoS", "4_Triagem", "4b_Triagem_WoS",
         "5_Texto_completo", "6_Extracao", "7_Fluxo", "8_Bibliometria"]
wb._sheets = [wb[n] for n in ordem if n in wb.sheetnames] + [ws for ws in wb._sheets if ws.title not in ordem]

wb.save("/home/ubuntu/review/extracao/Planilha_auditavel_revisao.xlsx")
print("xlsx ok")
