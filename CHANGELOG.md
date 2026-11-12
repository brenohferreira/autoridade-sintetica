# Registro de alterações
## 1.3.0 — 12 de novembro de 2026
Correção dos números do corpus e das figuras.
- A figura 2 passou a ser calculada sobre os 3.391 registros únicos do corpus completo, e não sobre os 1.227 registros das bases bibliográficas, com a distribuição de 2.388 registros (70,6%) em 2025-2026, 701 (20,7%) em 2020-2024 e 295 (8,7%) antes de 2020.
- A contagem de preprints foi refeita sobre o corpus completo, com 223 registros (6,6%), dos quais 91 em Zenodo, 78 em SSRN e 29 em arXiv.
- A figura 1 recebeu redação que descreve a remoção das 649 duplicatas sem ordenar as fontes no tempo.
- A aba de fluxo da planilha auditável identifica as colunas pelo nome das bases, e o leia-me da planilha deixou de se referir a bases anteriores.
- Acréscimo de `dados/02_triagem/estatisticas_corpus_completo.json` e de `scripts/estat_corpus.py`, que regera esse arquivo a partir dos dois conjuntos de registros.
- Correção do total da OpenAlex no README, de 1.239 para 1.219 registros, que é o valor compatível com os 4.040 registros identificados.

## 1.2.0 — 12 de novembro de 2026

O depósito passa a ser exclusivamente de dados.

- As versões do artigo em DOCX e PDF foram retiradas do repositório; o depósito reúne apenas os dados, o protocolo e os scripts da revisão.
- Os arquivos exportados da Web of Science foram incorporados como dados originais, em `dados/01_buscas/wos_bruto/`, com nomes que identificam a consulta de origem e um leia-me próprio.
- Os arquivos de busca e de triagem receberam nomes que distinguem as bases bibliográficas da Web of Science, e a matriz de extração passou a referir os 80 estudos incluídos.
- A identificação do autor foi completada no `CITATION.cff`, neste registro e na página do projeto.

## 1.1.0 — 12 de novembro de 2026

- Incorporação das oito consultas à Web of Science Core Collection, com 2.567 registros e 2.164 novos após deduplicação.
- Correção da consulta W6, que havia recuperado 22 mil registros por erro de sintaxe, e nova exportação com 1.160 registros.
- Triagem em duas etapas, com script de apoio, e inclusão de 25 estudos, o que levou o corpus a 80 estudos e 4.040 registros identificados.
- Protocolo atualizado para a versão 1.3, com emenda registrada antes da execução das buscas na Web of Science.
- Planilha auditável com as abas de buscas e triagem da Web of Science, e figuras refeitas com os novos totais.

## 1.0.0 — 12 de novembro de 2026

Primeira versão pública do depósito.

- Protocolo v1.0, redigido antes das buscas definitivas.
- Registro das consultas executadas, com expressões, filtros, datas e totais.
- 1.227 registros únicos após deduplicação e lista de candidatos avaliados.
- Matriz de extração com localizadores de página e uso de cada fonte.
- Planilha auditável com as abas de buscas, triagem, extração e fluxo.
- Figuras 1 e 2 em 300 dpi.
- Scripts de coleta, deduplicação, verificação de metadados, extração e geração das figuras.
- Lista de verificação PRISMA-ScR preenchida.
- Metadados verificados em Crossref e registro de downloads de textos completos.
