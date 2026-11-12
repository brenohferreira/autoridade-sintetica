# -*- coding: utf-8 -*-
"""Gera o artigo em ABNT (NBR 14724, NBR 6027, NBR 10520, NBR 6022)."""
import sys, os, re, unicodedata
sys.path.insert(0, "/home/ubuntu/review/scripts")
from dados import ESTUDOS
from texto_a import BLOCO_A
from texto_b import BLOCO_B
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

PRETO = RGBColor(0, 0, 0)
MODO = os.environ.get("MODO", "abnt")
CORPO = 10 if MODO == "compacto" else 12
ESP = 1.0 if MODO == "compacto" else 1.5
TAB = 8 if MODO == "compacto" else 9
LEG = 9 if MODO == "compacto" else 10
SAIDA = "/home/ubuntu/review/entrega/Artigo_autoridade_sintetica_15paginas.docx" if MODO == "compacto" else "/home/ubuntu/review/entrega/Artigo_autoridade_sintetica.docx"
doc = Document()

# ---------------- página: A4, margens 3-3-2-2 ----------------
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21), Cm(29.7)
sec.top_margin = Cm(3); sec.left_margin = Cm(3)
sec.right_margin = Cm(2); sec.bottom_margin = Cm(2)
sec.header_distance = Cm(1.5); sec.footer_distance = Cm(1.25)

st = doc.styles["Normal"]
st.font.name = "Times New Roman"; st.font.size = Pt(CORPO)
st.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
pf = st.paragraph_format
pf.line_spacing = ESP; pf.space_before = Pt(0); pf.space_after = Pt(0)

def numero_pagina(section):
    """Número da página no canto superior direito, a 2 cm da borda."""
    p = section.header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(); run.font.size = Pt(10); run.font.name = "Times New Roman"
    fld1 = OxmlElement("w:fldChar"); fld1.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve"); instr.text = " PAGE "
    fld2 = OxmlElement("w:fldChar"); fld2.set(qn("w:fldCharType"), "end")
    run._r.append(fld1); run._r.append(instr); run._r.append(fld2)

numero_pagina(sec)

def add_rich(p, text, size=None, base_bold=False):
    size = CORPO if size is None else size
    """Interpreta **negrito** e *itálico*."""
    for part in re.split(r"(\*\*.+?\*\*|\*[^*]+?\*)", text):
        if not part: continue
        if part.startswith("**") and part.endswith("**"):
            r = p.add_run(part[2:-2]); r.bold = True
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            r = p.add_run(part[1:-1]); r.italic = True
        else:
            r = p.add_run(part); r.bold = base_bold
        r.font.size = Pt(size); r.font.name = "Times New Roman"

def corpo(texto, espacamento=None, recuo=Cm(1.25), size=None, antes=0, depois=0):
    espacamento = ESP if espacamento is None else espacamento
    size = CORPO if size is None else size
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = espacamento
    p.paragraph_format.first_line_indent = recuo
    p.paragraph_format.space_before = Pt(antes); p.paragraph_format.space_after = Pt(depois)
    add_rich(p, texto, size)
    return p

def citacao_longa(texto):
    """Citação com mais de três linhas: recuo de 4 cm, corpo 10, espaço simples."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(4)
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_before = Pt(12); p.paragraph_format.space_after = Pt(12)
    add_rich(p, texto, LEG)

def titulo_secao(texto):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(18); p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(texto.upper()); r.bold = True; r.font.size = Pt(CORPO); r.font.name = "Times New Roman"

def subtitulo_secao(texto):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(12); p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(texto); r.bold = True; r.font.size = Pt(CORPO); r.font.name = "Times New Roman"

def legenda(texto, alinhamento=WD_ALIGN_PARAGRAPH.LEFT, antes=12, depois=6, keep=False):
    p = doc.add_paragraph()
    p.alignment = alinhamento
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_before = Pt(antes); p.paragraph_format.space_after = Pt(depois)
    if keep: p.paragraph_format.keep_with_next = True
    add_rich(p, texto, LEG)

def tabela(header, rows, widths):
    tbl = doc.add_table(rows=1, cols=len(header))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tbl._tbl.tblPr.append(lay)
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}"); el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4"); el.set(qn("w:color"), "000000")
        borders.append(el)
    tbl._tbl.tblPr.append(borders)
    for i, w in enumerate(widths):
        tbl.columns[i].width = Cm(w)
    for i, h in enumerate(header):
        cell = tbl.rows[0].cells[i]; cell.text = ""
        p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.line_spacing = 1.0
        r = p.add_run(h); r.bold = True; r.font.size = Pt(TAB); r.font.name = "Times New Roman"
    for row in rows:
        cells = tbl.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = ""
            p = cells[i].paragraphs[0]; p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.line_spacing = 1.0
            r = p.add_run(str(val)); r.font.size = Pt(TAB); r.font.name = "Times New Roman"
    for row in tbl.rows:
        for i, w in enumerate(widths):
            row.cells[i].width = Cm(w)
        trPr = row._tr.get_or_add_trPr(); trPr.append(OxmlElement("w:cantSplit"))
    trPr = tbl.rows[0]._tr.get_or_add_trPr(); trPr.append(OxmlElement("w:tblHeader"))

# ---------------- renderização ----------------
for bloco in BLOCO_A + BLOCO_B:
    kind = bloco[0]
    if kind == "title":
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(bloco[1].upper()); r.bold = True; r.font.size = Pt(CORPO); r.font.name = "Times New Roman"
    elif kind == "subtitle":
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(12)
        r = p.add_run(bloco[1]); r.italic = True; r.font.size = Pt(CORPO); r.font.name = "Times New Roman"
    elif kind == "author":
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(18)
        r = p.add_run(bloco[1]); r.font.size = Pt(10); r.font.name = "Times New Roman"
    elif kind == "h1":
        titulo_secao(bloco[1] if not bloco[1].lower().startswith("resumo") else "RESUMO")
    elif kind == "h2":
        subtitulo_secao(bloco[1])
    elif kind == "p":
        if bloco[1].startswith("**Palavras-chave**"):
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(0)
            add_rich(p, bloco[1], CORPO)
        elif bloco[1].startswith("**Fonte**"):
            legenda(bloco[1], WD_ALIGN_PARAGRAPH.LEFT, antes=3, depois=12)
        else:
            corpo(bloco[1])
    elif kind == "quote":
        # texto do próprio autor (pergunta e definição): parágrafo normal, com destaque
        corpo(bloco[1])
    elif kind == "fig":
        caminho, cap = bloco[1], bloco[2]
        if ". Fonte:" in cap:
            titulo_fig, fonte = cap.split(". Fonte:", 1)
            fonte = "Fonte:" + fonte
        else:
            titulo_fig, fonte = cap, None
        legenda(titulo_fig.replace(" — ", ": ").replace(" – ", ": "), WD_ALIGN_PARAGRAPH.CENTER, antes=12, depois=6, keep=True)
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(3)
        p.add_run().add_picture(caminho, width=Cm(10.5 if 'fig2' in caminho else 14.5))
        if fonte:
            legenda(fonte, WD_ALIGN_PARAGRAPH.CENTER, antes=0, depois=12)
    elif kind == "tab":
        cap, header, rows, widths = bloco[1], bloco[2], bloco[3], bloco[4]
        legenda(cap.replace(" — ", ": ").replace(" – ", ": "), WD_ALIGN_PARAGRAPH.LEFT, antes=12, depois=6, keep=True)
        tabela(header, rows, widths)
        doc.add_paragraph().paragraph_format.space_after = Pt(0)

# ---------------- referências (NBR 6023) ----------------
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(18); p.paragraph_format.space_after = Pt(12)
r = p.add_run("REFERÊNCIAS"); r.bold = True; r.font.size = Pt(CORPO); r.font.name = "Times New Roman"

refs = [e["ref"] for e in ESTUDOS]
refs += [
 "PETERS, M. D. J. et al. Updated methodological guidance for the conduct of scoping reviews. JBI Evidence Synthesis, v. 18, n. 10, p. 2119-2126, 2020. DOI: 10.11124/JBIES-20-00167.",
 "TRICCO, A. C. et al. PRISMA Extension for Scoping Reviews (PRISMA-ScR): checklist and explanation. Annals of Internal Medicine, v. 169, n. 7, p. 467-473, 2018. DOI: 10.7326/M18-0850.",
]
def chave(s):
    s2 = unicodedata.normalize("NFKD", s)
    s2 = "".join(c for c in s2 if not unicodedata.combining(c))
    return re.sub(r"[^A-Za-z ]", "", s2).upper()

for ref in sorted(refs, key=chave):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run(ref); r.font.size = Pt(CORPO); r.font.name = "Times New Roman"

doc.save(SAIDA)
print("docx ABNT ok, refs:", len(refs))
