#!/usr/bin/env python3
"""Gera as referências ABNT (NBR 6023) dos 20 estudos retidos pela regra lexical."""
import csv, html, json, re, unicodedata

BASE = "/home/ubuntu/review/emenda/novas_bases/capes_manual"
meta = {r["id"]: r for r in csv.DictReader(open(f"{BASE}/candidatos_capes.csv"))}
sel = json.load(open(f"{BASE}/selecao_20.json"))

PARTICULAS = {"de", "da", "do", "das", "dos", "van", "von", "der", "den", "di", "del", "la", "le"}


def abreviar(nome):
    nome = nome.strip()
    if not nome:
        return ""
    partes = nome.split()
    if len(partes) == 1:
        return partes[0].upper()
    # sobrenome: última parte, incorporando partículas anteriores em minúscula
    i = len(partes) - 1
    while i - 1 > 0 and partes[i - 1].lower() in PARTICULAS:
        i -= 1
    sobrenome = " ".join(partes[i:]).upper()
    prenome = " ".join(partes[:i])
    iniciais = " ".join(p[0].upper() + "." for p in prenome.split() if p)
    return f"{sobrenome}, {prenome}" if len(prenome.split()) <= 2 else f"{sobrenome}, {iniciais}"


def autores(campo):
    campo = (campo or "").strip()
    if not campo:
        return "AUTOR DESCONHECIDO"
    lista = [a.strip() for a in re.split(r";| and ", campo) if a.strip()]
    lista = lista[:3]
    return "; ".join(abreviar(a) for a in lista)


def limpar(t):
    t = html.unescape(t or "").replace("\u2019", "’").strip()
    t = re.sub(r"\s+", " ", t)
    return t.rstrip(".")


refs = []
for l in sel:
    m = meta[l["id"]]
    aut = autores(m["authors"])
    titulo = limpar(l["titulo"])
    veiculo = limpar(html.unescape(l["veiculo"] or "")).rstrip(".")
    ano = l["ano"]
    doi = (l["doi"] or "").strip()
    aut = aut.rstrip(".")
    fim = "" if titulo.endswith(("?", "!")) else "."
    ref = f"{aut}. {titulo}{fim} {veiculo}, {ano}."
    if doi:
        ref += f" DOI: {doi}."
    refs.append({"ref": ref, "titulo": titulo, "ano": ano})

refs.sort(key=lambda d: unicodedata.normalize("NFKD", d["ref"]).encode("ascii", "ignore").decode().lower())
for r in refs:
    print(r["ref"])
json.dump([r["ref"] for r in refs], open(f"{BASE}/refs20.json", "w"), ensure_ascii=False, indent=1)
print("\ntotal", len(refs))
