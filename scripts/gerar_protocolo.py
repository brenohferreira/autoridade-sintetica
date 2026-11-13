# -*- coding: utf-8 -*-
import sys, json
sys.path.insert(0, "/home/ubuntu/review/scripts")
from dados import BUSCAS_GS
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

AZUL = RGBColor(0x1F, 0x38, 0x64)
doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21), Cm(29.7)
sec.left_margin = sec.right_margin = Cm(2.2)
sec.top_margin = Cm(2.2); sec.bottom_margin = Cm(1.8)
st = doc.styles["Normal"]; st.font.name = "Times New Roman"; st.font.size = Pt(10.5)
st.paragraph_format.line_spacing = 1.15; st.paragraph_format.space_after = Pt(0)

def h(txt, size=13, before=14, after=6):
    p = doc.add_paragraph(); r = p.add_run(txt); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = AZUL
    p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.keep_with_next = True

def para(txt, size=10.5, just=True, after=6):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if just else WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(after)
    for i, part in enumerate(txt.split("**")):
        if not part: continue
        r = p.add_run(part); r.font.size = Pt(size); r.bold = (i % 2 == 1)
    return p

def table(caption, header, rows, widths):
    c = doc.add_paragraph(); r = c.add_run(caption); r.font.size = Pt(9); r.bold = True
    c.paragraph_format.space_before = Pt(8); c.paragraph_format.space_after = Pt(3)
    tbl = doc.add_table(rows=1, cols=len(header)); tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    _lay = OxmlElement('w:tblLayout'); _lay.set(qn('w:type'), 'fixed'); tbl._tbl.tblPr.append(_lay)
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}"); el.set(qn("w:val"), "single"); el.set(qn("w:sz"), "4"); el.set(qn("w:color"), "8C9BB5")
        borders.append(el)
    tbl._tbl.tblPr.append(borders)
    for i, w in enumerate(widths): tbl.columns[i].width = Cm(w)
    for i, hd in enumerate(header):
        cell = tbl.rows[0].cells[i]; cell.text = ""
        p = cell.paragraphs[0]; r = p.add_run(hd); r.bold = True; r.font.size = Pt(7.6); r.font.color.rgb = AZUL
        p.paragraph_format.space_after = Pt(1)
    for row in rows:
        cells = tbl.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = ""
            p = cells[i].paragraphs[0]; r = p.add_run(str(v)); r.font.size = Pt(7.4)
            p.paragraph_format.space_after = Pt(1); p.paragraph_format.line_spacing = 1.0
    for row in tbl.rows:
        for i, w in enumerate(widths): row.cells[i].width = Cm(w)
        trPr = row._tr.get_or_add_trPr(); trPr.append(OxmlElement("w:cantSplit"))
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

# ---------- capa / titulo ----------
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("PROTOCOLO E REGISTRO DA REVISÃO DE ESCOPO"); r.bold = True; r.font.size = Pt(15); r.font.color.rgb = AZUL
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Autoridade sintética na IA generativa e os limites da explicabilidade"); r.font.size = Pt(11.5); r.italic = True
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Material suplementar do artigo — versão 2.0, de 12 de novembro de 2026"); r.font.size = Pt(10)
p.paragraph_format.space_after = Pt(12)

h("1 Identificação e versão", 12, 6)
table("Quadro A — Controle de versões do protocolo",
 ["Versão", "Data", "Situação", "Alterações"],
 [["1.0", "11/11/2026", "Registrada antes das buscas definitivas", "Versão inicial, com pergunta PCC, critérios de elegibilidade, fontes, limites e procedimentos"],
  ["1.1", "11/11/2026", "Registrada antes da execução", "Substituição da Web of Science pela OpenAlex como fonte bibliográfica internacional, por indisponibilidade de assinatura institucional"],
  ["1.2", "11/11/2026", "Registrada após as buscas-piloto", "Redução do limite de exame por consulta no Google Acadêmico de vinte para dez resultados, em razão de bloqueio por captcha; registro da busca nominal dirigida a obras fundacionais"],
  ["2.0", "12/11/2026", "Registrada após a execução", "Execução da Web of Science Core Collection, com acesso institucional, em sete consultas (1.407 registros); consolidação do fluxo em 2.658 registros identificados, 372 duplicatas e 2.286 registros triados, com 57 estudos incluídos"]],
 [1.4, 2.0, 4.2, 9.0])

h("2 Pergunta e estrutura PCC", 12)
para("**Pergunta de revisão**: como a literatura sobre autoridade cognitiva e autoridade epistêmica ajuda a compreender a autoridade atribuída à IA generativa, e em que condições a explicabilidade permite examinar e contestar suas respostas?")
para("**Pergunta de abertura do artigo**: quando uma resposta gerada por IA deixa de ser apenas uma informação a considerar e passa a funcionar, para o usuário, como razão suficiente para acreditar em algo?")
table("Quadro B — Estrutura população, conceito e contexto (PCC)",
 ["Elemento", "Definição operacional"],
 [["População", "Usuários de IA generativa e de sistemas automatizados de informação e decisão, em práticas informacionais de trabalho, estudo e uso cotidiano"],
  ["Conceito", "Autoridade cognitiva; autoridade epistêmica; autoridade sintética; credibilidade; confiança; dependência excessiva; viés de automação; heurística da máquina; explicabilidade; interpretabilidade; transparência; contestabilidade"],
  ["Contexto", "IA generativa e modelos de linguagem; apoio à decisão; práticas informacionais em organizações e plataformas"]],
 [3.0, 13.6])

h("3 Critérios de elegibilidade", 12)
para("**Idiomas**: português, inglês e espanhol. **Período**: 1983 a 2026, adotando-se 1983 como marco por ser o ano da obra fundacional de Wilson. **Tipos incluídos**: artigo revisado por pares, capítulo de livro, tese ou dissertação, trabalho em anais e preprint com contribuição teórica.")
table("Quadro C — Critérios de inclusão e exclusão",
 ["Código", "Critério"],
 [["I1", "Discute autoridade cognitiva, epistêmica ou autoridade atribuída a sistemas"],
  ["I2", "Discute credibilidade, confiança, viés de automação ou dependência excessiva"],
  ["I3", "Discute explicabilidade, interpretabilidade, transparência ou contestabilidade"],
  ["I4", "Trata de IA generativa, modelos de linguagem ou automação em informação e decisão"],
  ["I5", "Publicado em português, inglês ou espanhol"],
  ["I6", "Publicado entre 1983 e 2026"],
  ["I7", "Pertence a um dos tipos de publicação admitidos"],
  ["I8", "Texto completo ou resumo acessível"],
  ["E1", "Tema não central para a pergunta de revisão"],
  ["E2", "Contribuição apenas técnica, sem discussão sobre autoridade, explicação ou uso"],
  ["E3", "Duplicata"],
  ["E4", "Sem texto ou resumo acessível"],
  ["E5", "Metadados não verificáveis (veículo, autoria ou data)"],
  ["E6", "Comentário, divulgação ou editorial sem argumentação teórica"]],
 [2.0, 14.6])

h("4 Fontes, expressões e limites de recuperação", 12)
para("As buscas foram organizadas em três frentes: fundamentos da autoridade; autoridade atribuída à IA; explicabilidade e contestação. Cada expressão foi adaptada à sintaxe da fonte após buscas-piloto. O Quadro D registra as consultas executadas, com data, expressão exata, campos, filtros, ordenação, total exibido e números efetivamente recuperados e examinados.")
log = json.load(open("/home/ubuntu/review/buscas/log_buscas.json"))
def short_fields(v):
    v = (v or "").lower()
    if "busca livre" in v: return "livre"
    if "title_and_abstract" in v: return "título+resumo"
    if "cites" in v: return "citações"
    if "referenced_works" in v: return "referências"
    if "qualquer lugar" in v: return "livre"
    return v or "—"

def short_filters(v):
    v = (v or "").replace(" (sem filtros)", "")
    if "score interno" in v: return "score interno"
    if "di=" in v: return "1972-2026"
    if "idioma" in v: return "idioma"
    if "40 primeiros" in v: return v.replace("40 primeiros, ", "")
    return v or "—"

def short_sort(v):
    v = (v or "—")
    if "score interno" in v: return "relevância"
    if "40 primeiros" in v: return v.replace("40 primeiros, ", "")
    return v

rows = []
for b in log:
    if b.get("label") in ("O8", "B7", "O6"):
        continue
    rows.append([b.get("source"), b.get("label"), b.get("expression"), short_fields(b.get("fields")), short_filters(b.get("filters")),
                 short_sort(b.get("sort")), b.get("total"), b.get("retrieved"), b.get("examined")])
rows.append(["OpenAlex", "O8", '"machine heuristic"', "título+resumo", "nenhum", "relevância", 114, 0, 0])
wos = [("W1", '("cognitive authority")', 175),
       ("W2", '("epistemic authority") AND ("artificial intelligence" OR "generative AI" OR algorithm)', 141),
       ("W3", '("synthetic authority")', 0),
       ("W4", '("generative AI" OR "large language model" OR "large language models" OR ChatGPT) AND (authority OR deference)', 742),
       ("W5", '("right to explanation") AND (explainable OR XAI OR contestability)', 31),
       ("W6", '("automation bias") AND ("large language model" OR "large language models" OR "generative AI" OR "clinical decision")', 245),
       ("W7", '("machine heuristic")', 73)]
for lbl, exp, tot in wos:
    rows.append(["Web of Science", lbl, exp, "tópico (TS)", "nenhum", "relevância", tot, tot, tot])
gs = [g for g in BUSCAS_GS if g["label"] != "G6"]
for i, g in enumerate(gs, 1):
    rows.append(["Google Acadêmico", "G%d" % i, g["expressao"], "livre", "idioma", "relevância", g["total"], g["examinados"], g["examinados"]])
rows.append(["Rastreamento", "R1", "citações de Hirvonen; Multas; Nygård (2025)", "citações", "por ano", "ano", 13, 13, 13])
rows.append(["Rastreamento", "R2", "referências de Hirvonen; Multas; Nygård (2025)", "referências", "por citações", "citações", 13, 13, 13])
rows.append(["Rastreamento", "R3", "citações de Wachter; Mittelstadt; Floridi (2017)", "citações", "por ano", "ano", 1822, 40, 40])
rows.append(["Rastreamento", "R4", "referências de Wachter; Mittelstadt; Floridi (2017)", "referências", "por citações", "citações", 1822, 40, 40])
table("Quadro D — Consultas executadas em 11 e 12 de novembro de 2026",
 ["Fonte", "ID", "Expressão exata", "Campos", "Filtros", "Ordenação", "Total", "Recup.", "Exam."],
 rows, [1.85, 0.85, 4.7, 1.95, 2.0, 1.7, 1.15, 1.2, 1.2])

para("**Limites definidos a priori**: no Google Acadêmico, exame dos 20 primeiros resultados por consulta, reduzido a 10 por bloqueio automatizado; na OpenAlex, 200 registros por consulta, ordenados por relevância; na BRAPCI, recuperação integral dos resultados. **Web of Science**: executada em 12/11/2026, com acesso institucional pelo Portal de Periódicos da CAPES, em sete consultas no campo TS, que somaram 1.407 registros. **Busca complementar**: rastreamento de citações e de referências a partir de duas sementes, e busca nominal dirigida a obras fundacionais.")

h("5 Triagem, extração e síntese", 12)
para("A deduplicação foi feita por identificador digital e, na ausência dele, por similaridade entre títulos normalizados. A triagem de títulos e resumos aplicou os critérios E1 a E6, em etapa automática de regras e pontuação de pertinência e em etapa manual. Os textos completos foram avaliados quando acessíveis; quando o acesso era restrito, avaliou-se o resumo, e as afirmações atribuídas ao estudo se limitam ao que o resumo permite verificar. A extração foi registrada em planilha com os campos: referência, contexto, tipo de estudo, conceitos, definições, achados, limitações, localização exata da evidência e afirmação sustentada no artigo.")
para("A síntese foi narrativa, organizada por frentes temáticas, com quadro comparativo das três formas de autoridade. Não houve avaliação formal de qualidade metodológica, o que é compatível com revisões de escopo, mas impede ponderação dos achados por robustez.")
table("Quadro E — Fluxo de seleção e conferência de contagens",
 ["Etapa", "Bases bibliográficas", "Fontes complementares", "Total"],
 [["Registros identificados", "2.474", "184", "2.658"],
  ["Duplicatas removidas", "359", "13", "372"],
  ["Registros triados", "2.115", "171", "2.286"],
  ["Excluídos na triagem", "2.061", "168", "2.229"],
  ["Estudos incluídos", "54", "3", "57"]],
 [3.6, 2.6, 3.0, 2.0])
para("**Conferência**: 2.115 − 2.061 = 54; 171 − 168 = 3; 54 + 3 = 57. As contagens coincidem com as abas de triagem, leitura integral e extração da planilha auditável. Os 184 registros complementares correspondem a 70 examinados no Google Acadêmico, 106 no rastreamento de citações e 8 recuperados por busca nominal dirigida. As bases bibliográficas somam 2.474 registros: 48 na BRAPCI, 1.019 na OpenAlex e 1.407 na Web of Science.")

h("6 Registro de decisões e restrições declaradas", 12)
table("Quadro F — Restrições declaradas",
 ["Item", "Situação", "Efeito sobre a síntese"],
 [["Web of Science", "Executada em 12/11/2026, com acesso institucional (sete consultas, 1.407 registros)", "Cobertura ampliada; a expressão synthetic authority não retornou registros, o que reforça a leitura de rótulo incipiente"],
  ["Google Acadêmico", "Executada com captcha; exame de 10 resultados por consulta", "Limite de recuperação; parte dos textos fundacionais obtida por busca nominal dirigida"],
  ["OpenAlex, consulta O8", "Consulta executada (114 registros), exportação falhou", "Registros não entraram na triagem; consulta registrada como pendente de recuperação"],
  ["Revisores", "Um revisor, sem dupla triagem independente", "Risco de erro de seleção não estimado"],
  ["Acesso a textos", "45 dos 57 estudos avaliados apenas por resumo", "Afirmações limitadas ao que o resumo permite verificar"],
  ["Qualidade metodológica", "Não avaliada formalmente", "Achados não ponderados por robustez"]],
 [3.2, 5.6, 7.8])

h("7 Reprodutibilidade", 12)
para("Os arquivos que acompanham este protocolo permitem refazer cada etapa: o registro bruto das buscas, o conjunto deduplicado, a lista de triagem com decisão e motivo, a lista de textos avaliados, a matriz de extração com localização da evidência e os scripts de coleta, deduplicação, verificação de metadados e geração das figuras. A planilha auditável reúne esses registros em abas separadas e conciliadas com o Quadro E.")

doc.save("/home/ubuntu/review/entrega/Protocolo_registro_revisao.docx")
print("protocolo ok")
