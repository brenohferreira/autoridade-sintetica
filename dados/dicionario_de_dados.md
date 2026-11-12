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

Conjunto após deduplicação por identificador digital e por similaridade de título, com 1.227 registros.

| Campo | Descrição |
|---|---|
| `fonte` | Base em que o registro foi recuperado |
| `consulta` | Rótulo da consulta de origem |
| `id` | Identificador na base de origem |
| `titulo`, `autores`, `ano`, `veiculo`, `tipo` | Metadados bibliográficos |
| `doi`, `url` | Identificadores de localização |

## `02_triagem/estatisticas.json`

Distribuição dos registros únicos por ano, total de registros e contagem por repositório de preprint (Zenodo, SSRN, arXiv, ResearchGate).

## `02_triagem/estatisticas_corpus_completo.json`
Distribuição por ano dos 3.391 registros únicos do corpus completo, isto é, a união dos registros das bases bibliográficas com os registros novos da Web of Science, com total de registros, registros sem ano e contagem de preprints. É o arquivo lido pela figura 2 e pode ser regerado por `scripts/estat_corpus.py`.
## `02_triagem/candidatos_avaliados.csv`

Registros que passaram à avaliação de texto completo ou resumo, com a decisão de triagem.

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

## `04_planilha/Planilha_auditavel_revisao.xlsx`

Planilha com as abas de buscas, triagem, extração, fluxo PRISMA-ScR e referências verificadas, com fórmulas de conferência entre as abas.

## `fontes/metadados_verificados.json`

Metadados de cada referência conferidos em Crossref ou na página do editor, com o DOI efetivamente válido.

## `fontes/download_log.json`

Registro das tentativas de obtenção de texto completo, com código de resposta HTTP e origem do arquivo.

## 05_bibliometria.csv

Um registro por estudo incluído. Campos: `id` (identificador interno), `veiculo` (periódico, anais ou livro), `area` (área do conhecimento atribuída ao veículo), `paises` (códigos ISO das instituições de afiliação, separados por ponto e vírgula), `instituicoes`, `tipo` (tipologia do OpenAlex) e `ano`.

## 05_bibliometria_resumo.csv

Totais por área do veículo, país de afiliação e instituição, no formato `agrupamento; categoria; estudos`.
