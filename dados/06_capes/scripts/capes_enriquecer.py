# -*- coding: utf-8 -*-
"""Enriquece os candidatos do Portal da CAPES com resumos e metadados da OpenAlex."""
import csv
import json
import re
import time
import urllib.parse
import urllib.request

BASE = "/home/ubuntu/review/emenda/novas_bases/capes_manual"
ENTRADA = f"{BASE}/capes_consolidado.csv"
SAIDA = f"{BASE}/candidatos_capes.csv"
CACHE = f"{BASE}/openalex_cache.json"


def resumo(indice):
    if not indice:
        return ""
    posicoes = {}
    for palavra, lugares in indice.items():
        for lugar in lugares:
            posicoes[lugar] = palavra
    return " ".join(posicoes[k] for k in sorted(posicoes))


def consultar(dois):
    filtro = "doi:" + "|".join(dois)
    url = ("https://api.openalex.org/works?filter=" + urllib.parse.quote(filtro, safe=":|/.-_")
           + "&per-page=50&select=doi,title,publication_year,abstract_inverted_index,"
             "primary_location,authorships,type")
    pedido = urllib.request.Request(url, headers={"User-Agent": "revisao-autoridade-sintetica/1.0 (mailto:brenohferreira@ufmg.br)"})
    for tentativa in range(4):
        try:
            with urllib.request.urlopen(pedido, timeout=60) as resposta:
                return json.loads(resposta.read().decode("utf-8"))
        except Exception:
            time.sleep(3 + 3 * tentativa)
    return {"results": []}


def main():
    linhas = [l for l in csv.DictReader(open(ENTRADA, encoding="utf-8")) if l["situacao"] == "candidato"]
    print("candidatos:", len(linhas), flush=True)
    try:
        cache = json.load(open(CACHE))
    except Exception:
        cache = {}
    dois = [l["doi"] for l in linhas if l["doi"] and l["doi"] not in cache]
    for i in range(0, len(dois), 50):
        bloco = dois[i:i + 50]
        dados = consultar(bloco)
        for obra in dados.get("results", []):
            d = (obra.get("doi") or "").replace("https://doi.org/", "").lower()
            cache[d] = {
                "titulo": obra.get("title") or "",
                "ano": obra.get("publication_year") or "",
                "resumo": resumo(obra.get("abstract_inverted_index")),
                "veiculo": ((obra.get("primary_location") or {}).get("source") or {}).get("display_name") or "",
                "autores": "; ".join(a["author"]["display_name"] for a in obra.get("authorships", [])[:8]),
                "tipo": obra.get("type") or "",
            }
        print("consultados", min(i + 50, len(dois)), "de", len(dois), flush=True)
        time.sleep(0.4)
    json.dump(cache, open(CACHE, "w"), ensure_ascii=False)

    with open(SAIDA, "w", newline="", encoding="utf-8") as fh:
        campos = ["source", "query", "query_string", "id", "title", "authors", "year", "venue",
                  "type", "doi", "abstract", "url"]
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        com_resumo = 0
        for l in linhas:
            meta = cache.get(l["doi"], {})
            res = meta.get("resumo", "")
            if res:
                com_resumo += 1
            w.writerow({
                "source": "Portal CAPES",
                "query": l["consulta"],
                "query_string": l["consulta"],
                "id": l["id"] or l["doi"],
                "title": l["titulo"] or meta.get("titulo", ""),
                "authors": meta.get("autores", l["autores"]),
                "year": l["ano"] or meta.get("ano", ""),
                "venue": l["veiculo"] or meta.get("veiculo", ""),
                "type": meta.get("tipo", "article"),
                "doi": l["doi"],
                "abstract": res,
                "url": ("https://doi.org/" + l["doi"]) if l["doi"] else "",
            })
    print("com resumo:", com_resumo, "de", len(linhas))


if __name__ == "__main__":
    main()
