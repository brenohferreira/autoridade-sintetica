# -*- coding: utf-8 -*-
"""Consolida os arquivos RIS exportados manualmente do Portal de Periódicos da CAPES."""
import csv
import re
import unicodedata

BASE = "/home/ubuntu/upload"
ARQ = [
    ("C4a", "Periodicos-CAPES-RIS.ris"),
    ("C4a", "Periodicos-CAPES-RIS(1).ris"),
    ("C4b", "Periodicos-CAPES-RIS(3).ris"),
    ("C4c", "Periodicos-CAPES-RIS(4).ris"),
    ("C4d?", "Periodicos-CAPES-RIS(5).ris"),
    ("indef", "Periodicos-CAPES-RIS(6).ris"),
    ("indef", "Periodicos-CAPES-RIS(7).ris"),
    ("C5a", "Periodicos-CAPES-RIS(8).ris"),
    ("C5b", "Periodicos-CAPES-RIS(9).ris"),
    ("C5c", "Periodicos-CAPES-RIS(10).ris"),
    ("C5d", "Periodicos-CAPES-RIS(11).ris"),
    ("C6a", "Periodicos-CAPES-RIS(12).ris"),
    ("C6a", "Periodicos-CAPES-RIS(13).ris"),
    ("C6a", "Periodicos-CAPES-RIS(14).ris"),
    ("C6a", "Periodicos-CAPES-RIS(15).ris"),
    ("C6b", "Periodicos-CAPES-RIS(16).ris"),
    ("C6c", "Periodicos-CAPES-RIS(17).ris"),
]
CAMPOS = {"DO": "doi", "TI": "titulo", "AU": "autores", "PY": "ano", "JO": "veiculo", "ID": "id"}


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]", " ", s).split()


def ler(caminho):
    txt = open(caminho, encoding="utf-8", errors="replace").read()
    registros = []
    for bloco in [x for x in re.split(r"\nER  -", txt) if "TY  -" in x]:
        d = {}
        for tag, campo in CAMPOS.items():
            m = re.search(r"^%s  - (.*)$" % tag, bloco, re.M)
            d[campo] = m.group(1).strip() if m else ""
        d["doi"] = d["doi"].lower()
        registros.append(d)
    return registros


def main():
    corpus, titulos = set(), set()
    for caminho, sep, col in [
        ("/home/ubuntu/review/github/autoridade-sintetica/dados/02_triagem/registros_unicos_bases.csv", ";", ("doi", "titulo")),
        ("/home/ubuntu/review/github/autoridade-sintetica/dados/02_triagem/novas_bases_deduplicadas.csv", ",", ("doi", "title")),
    ]:
        for linha in csv.DictReader(open(caminho, encoding="utf-8-sig"), delimiter=sep):
            d = (linha.get(col[0]) or "").strip().lower()
            if d:
                corpus.add(d)
            titulos.add(" ".join(norm(linha.get(col[1]))[:8]))

    linhas, vistos = [], {}
    for consulta, arquivo in ARQ:
        for r in ler(f"{BASE}/{arquivo}"):
            chave = r["doi"] or " ".join(norm(r["titulo"])[:8])
            situacao = "duplicado_corpus" if (r["doi"] in corpus or " ".join(norm(r["titulo"])[:8]) in titulos) else "candidato"
            if chave in vistos:
                linhas[vistos[chave]]["situacao"] = "duplicado_interno"
                continue
            vistos[chave] = len(linhas)
            linhas.append(dict(consulta=consulta, arquivo=arquivo, situacao=situacao, **r))

    saida = "/home/ubuntu/review/emenda/novas_bases/capes_manual/capes_consolidado.csv"
    with open(saida, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["consulta", "arquivo", "situacao", "id", "doi", "titulo", "autores", "ano", "veiculo"])
        w.writeheader()
        w.writerows(linhas)

    from collections import Counter
    print("registros lidos:", sum(1 for _ in linhas))
    print("por situação:", Counter(x["situacao"] for x in linhas))
    print("por consulta:", Counter(x["consulta"] for x in linhas))
    print("candidatos:", sum(1 for x in linhas if x["situacao"] == "candidato"))
    print("salvo em", saida)


if __name__ == "__main__":
    main()
