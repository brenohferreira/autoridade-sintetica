# Dicionário de dados

Todos os arquivos estão em UTF-8, e os CSV usam ponto e vírgula como separador e vírgula como decimal, para abertura direta no Excel em português.

## `01_buscas/consultas.csv`

Registro de cada consulta executada, com a expressão exata e os números efetivamente obtidos.

| Campo | Descrição |
|---|---|
| `n` | Número de ordem da consulta no registro |
| `fonte` | Base ou plataforma consultada (BRAPCI, OpenAlex, Google Acadêmico, rastreamento, busca nominal) |
| `rotulo` | Identificador da consulta no protocolo (B1 a B9, O1 a O8, G1 a G8) |
| `expressao` | Expressão exata submetida, com operadores e aspas |
| `campos` | Campos de busca utilizados |
| `filtros` | Filtros aplicados, incluindo recorte temporal e tipo de documento |
| `ordenacao` | Critério de ordenação dos resultados |
| `total_exibido` | Total informado pela plataforma |
| `recuperados` | Registros efetivamente recuperados |
| `examinados` | Registros efetivamente examinados |
| `data` | Data e hora da execução, em UTC |
| `url` | Endereço da consulta ou do endpoint utilizado |

## `01_buscas/registros_brutos.csv`

Um registro por linha recuperada, antes de qualquer deduplicação. Contém fonte, consulta, identificador na base, título, autores, ano, veículo, tipo, DOI, resumo e URL.

## `01_buscas/rastreamento_citacoes.csv`

Rastreamento para frente e para trás a partir de duas sementes (Hirvonen, Multas e Nygård, 2025; Wachter, Mittelstadt e Floridi, 2017).

| Campo | Descrição |
|---|---|
| `semente` | Estudo de partida |
| `direcao` | `citado por` (para frente) ou `referência de` (para trás) |
| `titulo` | Título do registro encontrado |
| `ano` | Ano de publicação |
| `doi` | DOI, quando disponível |

## `02_triagem/registros_unicos.csv`

Conjunto após deduplicação por identificador digital e por similaridade de título, com 1.026 registros de BRAPCI e OpenAlex.

| Campo | Descrição |
|---|---|
| `fonte` | Base em que o registro foi recuperado |
| `consulta` | Rótulo da consulta de origem |
| `id` | Identificador na base de origem |
| `titulo`, `autores`, `ano`, `veiculo`, `tipo` | Metadados bibliográficos |
| `doi`, `url` | Identificadores de localização |

## `02_triagem/estatisticas.json`

Fluxo consolidado da versão 2.2.0, com os registros identificados por fonte, as duplicatas removidas, os registros triados, os lidos por título e resumo, os estudos incluídos por tipo de documento, a distribuição do corpus único por faixa de ano, a contagem de preprints por repositório e o bloco de incorporação das bases novas.

## `02_triagem/estatisticas_corpus_completo.json`
Distribuição por ano dos 6.250 registros únicos do corpus completo, dos quais 5.652 com ano informado, com a contagem de preprints por repositório. É o arquivo lido pela figura 2 e pode ser regerado por `scripts/estat_corpus.py`.
## `02_triagem/candidatos_avaliados.csv`

Registros que passaram à avaliação de texto completo ou resumo, com a decisão de triagem nas colunas `decisao` e `motivo`, referentes ao corpus inicial.

## `03_extracao/matriz_extracao.csv`

Um registro por estudo incluído, com a passagem que sustenta cada afirmação do artigo.

| Campo | Descrição |
|---|---|
| `id` | Código do estudo (F01 a F13, A01 a A19, E01 a E14, D01 a D09) |
| `estudo` | Citação abreviada |
| `ano` | Ano de publicação |
| `tipo` | Tipo de documento (artigo, livro, capítulo, preprint, norma) |
| `fonte_de_origem` | Como o estudo foi recuperado |
| `acesso` | Nível de acesso: texto completo, resumo ou definição citada em fonte primária consultada |
| `frente` | Frente temática: fundamentos, autoridade e IA, explicabilidade e direito, educação |
| `conceito` | Conceito central do estudo |
| `achado` | Achado ou tese registrada |
| `localizador` | Página, seção, quadro ou artigo de lei em que a passagem se encontra |
| `uso_no_artigo` | Afirmação do artigo que a passagem sustenta |
| `referencia_completa` | Referência em formato ABNT |

## `01_buscas/scopus/`, `01_buscas/lista/` e `01_buscas/capes/`

Registros recuperados e quadros de consultas das três bases incorporadas na versão 2.2.0, com um arquivo de registros e um arquivo de consultas por base. O arquivo de consultas tem as colunas `consulta` (S1 a S6, A1 a A6 e C1 a C6), `expressao`, `campos`, `filtros`, `ordenacao`, `situacao`, `total_declarado` pela plataforma, `registros_unicos` que permaneceram no arquivo após a deduplicação interna, `data` e `url`. A diferença entre as duas últimas colunas de contagem decorre da remoção de registros repetidos dentro da própria base e, no caso da Scopus e da LISTA, do teto de 200 registros aplicado às consultas de explicabilidade. Os quadros podem ser regerados por `scripts/consultas_v220.py`.

## `02_triagem/novas_bases_deduplicadas.csv`

Os 2.649 registros novos que permaneceram após a remoção de 65 duplicatas entre as bases novas e de 344 duplicatas em relação ao corpus anterior, no mesmo esquema de campos dos registros brutos.

## `02_triagem/triagem_bases_novas.jsonl` e `02_triagem/triagem_bases_novas.csv`

Triagem dos 2.649 registros novos, um registro por linha, com os mesmos campos dos registros brutos e três campos adicionais, a saber, `pontuacao`, `motivo` e `decisao`, em que a decisão 1 indica candidato à leitura de título e resumo e a decisão 0 indica exclusão. O arquivo em CSV traz os mesmos dados em ponto e vírgula.

## `02_triagem/estatisticas_bases_novas.json` e `02_triagem/triagem_bases_novas_stats.json`

O primeiro consolida a incorporação, com os totais por base, as duplicatas internas e contra o corpus anterior, os registros novos e o total após a incorporação. O segundo registra os totais da triagem das bases novas, com os excluídos, os candidatos e a distribuição dos candidatos por fonte.

## `03_extracao/novas_incluidas.csv`

Os 42 estudos incorporados na versão 2.2.0, com as colunas `id`, `source`, `query`, `title`, `authors`, `year`, `venue`, `type`, `doi`, `eixo`, `tipo_contribuicao`, `abstract` e `ref`.

## `04_planilha/Planilha_auditavel_revisao.xlsx`

Planilha com as abas de buscas, buscas das bases novas, triagem, triagem das bases novas, texto completo, extração, estudos incluídos novos, fluxo PRISMA-ScR e bibliometria, com fórmulas de conferência entre as abas.

## `fontes/metadados_verificados.json`

Metadados de cada referência conferidos em Crossref ou na página do editor, com o DOI efetivamente válido.

## `fontes/download_log.json`

Registro das tentativas de obtenção de texto completo, com código de resposta HTTP e origem do arquivo.

## `artigo/`

Artigo completo na versão 2.2.0, em DOCX e PDF, com as figuras incorporadas e a lista de referências atualizada.

## 05_bibliometria.csv

Um registro por estudo incluído do corpus inicial. Campos: `id` (identificador interno), `veiculo` (periódico, anais ou livro), `area` (área do conhecimento atribuída ao veículo), `paises` (códigos ISO das instituições de afiliação, separados por ponto e vírgula), `instituicoes`, `tipo` (tipologia do OpenAlex) e `ano`.

## 05_bibliometria_resumo.csv

Totais por área do veículo, país de afiliação e instituição, no formato `agrupamento; categoria; estudos`.
