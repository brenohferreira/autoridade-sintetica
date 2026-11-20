# -*- coding: utf-8 -*-
"""Gera os quadros de consultas da Scopus, da LISTA e do Portal de Periódicos da CAPES.

Os totais declarados por consulta vêm do registro de execução da emenda v2.2; a coluna
de registros únicos é contada diretamente sobre os arquivos de registros recuperados,
de modo que a diferença entre as duas colunas corresponde à deduplicação interna de cada base.
"""
import collections
import csv

DATA = "2026-11-20T00:00:00+00:00"
CABECALHO = ["consulta", "expressao", "campos", "filtros", "ordenacao", "situacao",
             "total_declarado", "registros_unicos", "data", "url"]

SCOPUS_URL = "https://www.scopus.com/results/results.uri"
LISTA_URL = "https://search.ebscohost.com"
CAPES_URL = "https://www.periodicos.capes.gov.br"


def contar(caminho):
    with open(caminho, encoding="utf-8") as arquivo:
        return collections.Counter(linha["query"] for linha in csv.DictReader(arquivo))


SCOPUS = [
    ("S1", '"cognitive authority"', "título, resumo e palavras-chave (TITLE-ABS-KEY)",
     "nenhum filtro de tipo ou idioma", "relevância", "executada", "181"),
    ("S2", '"epistemic authority" AND ("artificial intelligence" OR "generative AI" OR algorithm)',
     "título, resumo e palavras-chave (TITLE-ABS-KEY)", "nenhum filtro de tipo ou idioma", "relevância", "executada", "185"),
    ("S3", '"synthetic authority"', "título, resumo e palavras-chave (TITLE-ABS-KEY)",
     "nenhum filtro de tipo ou idioma", "relevância", "executada", "3"),
    ("S4", '("generative AI" OR "large language model" OR ChatGPT) AND (authority OR deference)',
     "título, resumo e palavras-chave (TITLE-ABS-KEY)", "nenhum filtro de tipo ou idioma", "relevância", "executada", "1.142"),
    ("S5", '"right to explanation" OR "explainable AI" OR XAI OR contestability',
     "título, resumo e palavras-chave (TITLE-ABS-KEY)",
     "teto de 200 registros, ordenados por relevância", "relevância",
     "executada com teto de 200", "43.627"),
    ("S6", '"automation bias" OR "machine heuristic" OR "algorithmic authority"',
     "título, resumo e palavras-chave (TITLE-ABS-KEY)", "nenhum filtro de tipo ou idioma", "relevância", "executada", "1.090"),
]

LISTA = [
    ("A1", '"cognitive authority"', "título e resumo", "nenhum filtro de tipo ou idioma", "relevância", "executada", "59"),
    ("A2", '"epistemic authority" AND ("artificial intelligence" OR "generative AI" OR algorithm)',
     "título e resumo", "nenhum filtro de tipo ou idioma", "relevância", "executada", "3"),
    ("A3", '"synthetic authority"', "título e resumo", "nenhum filtro de tipo ou idioma", "relevância", "executada", "24"),
    ("A4", '("generative AI" OR "large language model" OR ChatGPT) AND (authority OR deference)',
     "título e resumo", "nenhum filtro de tipo ou idioma", "relevância", "executada", "38"),
    ("A5", '"right to explanation" OR "explainable AI" OR XAI OR contestability',
     "título e resumo", "teto de 200 registros, ordenados por relevância", "relevância",
     "executada com teto de 200", "354"),
    ("A6", '"automation bias" OR "machine heuristic" OR "algorithmic authority"',
     "título e resumo", "nenhum filtro de tipo ou idioma", "relevância", "executada", "22"),
]

CAPES = [
    ("C1", '"cognitive authority"', "todos os campos", "nenhum filtro de tipo ou idioma", "relevância", "executada", "94"),
    ("C2", '"epistemic authority" AND "artificial intelligence"', "todos os campos",
     "nenhum filtro de tipo ou idioma", "relevância", "executada", "80"),
    ("C3", '"synthetic authority"', "todos os campos", "nenhum filtro de tipo ou idioma", "relevância",
     "executada sem resultados", "0"),
    ("C4", '("generative AI" OR "large language model" OR ChatGPT) AND (authority OR deference)',
     "todos os campos", "nenhum filtro de tipo ou idioma", "relevância",
     "bloqueada pelo firewall do serviço, HTTP 403", "não disponível"),
    ("C5", '"right to explanation" OR "explainable AI" OR XAI OR contestability',
     "todos os campos", "nenhum filtro de tipo ou idioma", "relevância",
     "bloqueada pelo firewall do serviço, HTTP 403", "não disponível"),
    ("C6", '"automation bias" OR "machine heuristic" OR "algorithmic authority"',
     "todos os campos", "nenhum filtro de tipo ou idioma", "relevância",
     "bloqueada pelo firewall do serviço, HTTP 403", "não disponível"),
]


def escrever(caminho, linhas, contagem, url):
    with open(caminho, "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow(CABECALHO)
        for consulta, expressao, campos, filtros, ordenacao, situacao, total in linhas:
            escritor.writerow([consulta, expressao, campos, filtros, ordenacao, situacao,
                               total, contagem.get(consulta, 0), DATA, url])
    print(caminho, sum(contagem.values()))


if __name__ == "__main__":
    escrever("dados/01_buscas/scopus/scopus_consultas.csv", SCOPUS,
             contar("dados/01_buscas/scopus/scopus_registros.csv"), SCOPUS_URL)
    escrever("dados/01_buscas/lista/lista_consultas.csv", LISTA,
             contar("dados/01_buscas/lista/lista_registros.csv"), LISTA_URL)
    escrever("dados/01_buscas/capes/capes_consultas.csv", CAPES,
             contar("dados/01_buscas/capes/capes_registros.csv"), CAPES_URL)
