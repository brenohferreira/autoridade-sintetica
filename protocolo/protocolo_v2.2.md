# PROTOCOLO DE REVISÃO DE ESCOPO, VERSÃO 2.2

**Título:** Autoridade sintética na IA generativa e os limites da explicabilidade: uma revisão de escopo

**Método de referência:** JBI (Peters et al., 2020; Aromataris & Munn, 2020) e diretriz de relato PRISMA-ScR (Tricco et al., 2018)

**Versão:** 2.2, de 20 de novembro de 2026

**Responsável:** revisor único (autor do artigo), com apoio de rotinas automáticas de deduplicação e de classificação.

**Documentos desta versão:** `Emenda_ampliacao_de_fontes.pdf` e `Emenda_ampliacao_de_fontes.docx`, com o mesmo conteúdo deste registro, e as versões anteriores em `protocolo_v1.0.md` e `Protocolo_registro_revisao.pdf`.

## 1. Escopo do registro

Esta versão não altera a pergunta de revisão, os critérios de elegibilidade nem as definições operacionais fixadas na versão 1.0 e mantidas no registro da versão 2.0, aos quais se remete o leitor. A alteração recai apenas sobre a cobertura de fontes, sobre o registro das consultas efetivamente executadas e sobre as decisões tomadas durante a coleta, de modo que o percurso possa ser refeito e contestado. A versão 2.1 havia previsto quatro fontes adicionais, a Biblioteca Digital Brasileira de Teses e Dissertações, a LISTA, a Scopus e a busca integrada do Portal de Periódicos da CAPES, das quais apenas a primeira havia sido executada; a versão 2.2 conclui a execução, registra o bloqueio parcial de uma delas e fixa o teto de recuperação aplicado às consultas de explicabilidade.

## 2. Situação das fontes previstas

| Fonte | Situação | Registros | Observação |
|---|---|---|---|
| BRAPCI | executada | 48 | oito consultas em busca livre |
| OpenAlex | executada | 1.019 | teto de 200 registros nas consultas amplas |
| Google Acadêmico | executada | 70 | consulta por navegador, primeiros resultados |
| Web of Science Core Collection | executada | 1.407 | sete consultas no campo de tópico, com acesso institucional |
| Scopus | executada | 2.671 | seis consultas, 2.801 recuperados |
| LISTA | executada | 327 | seis consultas, 500 recuperados |
| Portal de Periódicos da CAPES | executada com bloqueio parcial | 60 | C1 e C2 executadas, C3 sem resultados, C4 a C6 bloqueadas |
| BDTD | executada | 1.029 | doze consultas em todos os campos |
| Rastreamento de citações | executada | 106 | dois estudos-semente |
| Busca nominal dirigida | executada | 8 | recuperação de textos fundacionais |

## 3. Consultas executadas na Scopus

| Consulta | Expressão aplicada a título, resumo e palavras-chave | Resultados |
|---|---|---|
| S1 | `"cognitive authority"` | 181 |
| S2 | `"epistemic authority" AND ("artificial intelligence" OR "generative AI" OR algorithm)` | 185 |
| S3 | `"synthetic authority"` | 3 |
| S4 | `("generative AI" OR "large language model" OR ChatGPT) AND (authority OR deference)` | 1.142 |
| S5 | `"right to explanation" OR "explainable AI" OR XAI OR contestability` | 43.627, com teto de 200 |
| S6 | `"automation bias" OR "machine heuristic" OR "algorithmic authority"` | 1.090 |
| Total | seis consultas | 2.801 recuperados |

## 4. Consultas executadas na LISTA

| Consulta | Expressão aplicada a título e resumo | Resultados |
|---|---|---|
| A1 | `"cognitive authority"` | 59 |
| A2 | `"epistemic authority" AND ("artificial intelligence" OR "generative AI" OR algorithm)` | 3 |
| A3 | `"synthetic authority"` | 24 |
| A4 | `("generative AI" OR "large language model" OR ChatGPT) AND (authority OR deference)` | 38 |
| A5 | `"right to explanation" OR "explainable AI" OR XAI OR contestability` | 354, com teto de 200 |
| A6 | `"automation bias" OR "machine heuristic" OR "algorithmic authority"` | 22 |
| Total | seis consultas | 500 recuperados |

## 5. Consultas executadas no Portal de Periódicos da CAPES

| Consulta | Expressão aplicada a todos os campos | Situação |
|---|---|---|
| C1 | `"cognitive authority"` | 94 resultados, 30 recuperados |
| C2 | `"epistemic authority" AND "artificial intelligence"` | 80 resultados, 30 recuperados |
| C3 | `"synthetic authority"` | nenhum resultado |
| C4 | `("generative AI" OR "large language model" OR ChatGPT) AND (authority OR deference)` | bloqueada pelo firewall do serviço |
| C5 | `"right to explanation" OR "explainable AI" OR XAI OR contestability` | bloqueada pelo firewall do serviço |
| C6 | `"automation bias" OR "machine heuristic" OR "algorithmic authority"` | bloqueada pelo firewall do serviço |

## 6. Resultados da coleta e incorporação

A Scopus devolveu 2.801 registros, dos quais 2.671 permaneceram únicos após a remoção de duplicatas internas, e a LISTA devolveu 500 registros, dos quais 327 permaneceram únicos. O Portal de Periódicos da CAPES devolveu 60 registros, cuja maior parte corresponde a identificadores já indexados na OpenAlex, o que se explica pela natureza integrada do buscador.

A consolidação das três bases que produziram registros somou 3.058 identificados, com 65 duplicatas entre as bases novas e 344 duplicatas em relação ao corpus anterior, o que resultou em 2.649 registros novos. Somados aos 3.601 registros únicos já reunidos, o corpus passou a 6.250 registros, dos quais 5.829 permaneceram após a deduplicação integral e foram submetidos à triagem. A triagem das bases novas eliminou 1.033 registros por tipo de documento e por domínio alheio ao escopo, submeteu 1.616 candidatos à leitura de título e resumo e incorporou 42 estudos, 40 provenientes da Scopus e dois da LISTA, elevando o corpus de estudos incluídos de 63 para 163.

## 7. Decisões metodológicas registradas

A primeira decisão diz respeito ao teto de recuperação. As consultas de explicabilidade da Scopus e da LISTA ultrapassaram em muito a capacidade de leitura do estudo, com 43.627 e 354 resultados, de modo que se adotou o limite de 200 registros por consulta, ordenados por relevância, decisão equivalente à que já havia sido aplicada à OpenAlex e ao Google Acadêmico. O teto está declarado nas figuras de fluxo e na seção de limitações do artigo.

A segunda decisão diz respeito ao Portal de Periódicos da CAPES. Três das seis expressões foram bloqueadas pelo firewall do serviço, que recusou toda consulta com mais de um operador booleano, inclusive após a codificação dos parênteses e a reescrita distributiva dos termos. Como as consultas executadas devolveram registros em grande parte sobrepostos às bases já coletadas, a fonte foi mantida no protocolo com o registro do bloqueio, sem prejuízo para a cobertura temática.

## 8. Histórico de versões

| Versão | Data | Alteração |
|---|---|---|
| 1.0 | 11 nov. 2026 | protocolo inicial, com oito bases previstas e critérios E1 a E6 |
| 1.1 | 12 nov. 2026 | inclusão da Web of Science Core Collection e registro das oito consultas |
| 2.0 | 12 nov. 2026 | reformulação do escopo, com exclusão do eixo normativo e da frente de educação |
| 2.1 | 19 nov. 2026 | ampliação de fontes, com a BDTD executada e quatro fontes pendentes de acesso institucional |
| 2.2 | 20 nov. 2026 | execução da Scopus, da LISTA e do Portal de Periódicos da CAPES e teto de 200 registros nas consultas de explicabilidade |

## 9. Registro de execução

As consultas foram executadas em 20 de novembro de 2026, por acesso remoto autenticado na Universidade Federal de Minas Gerais, com registro dos totais declarados por consulta, dos registros efetivamente recuperados e das respostas brutas de cada interface. Os arquivos permanecem depositados no repositório público do estudo, com os scripts de coleta, de deduplicação, de triagem e de geração das figuras, de modo que qualquer leitor possa refazer o percurso, confrontar os totais e contestar as decisões aqui registradas.

## 10. Arquivos desta versão no repositório

| Arquivo | Conteúdo |
|---|---|
| `protocolo/Emenda_ampliacao_de_fontes.pdf` | emenda completa em PDF |
| `protocolo/Emenda_ampliacao_de_fontes.docx` | emenda completa em DOCX |
| `protocolo/protocolo_v1.0.md` | protocolo inicial em Markdown |
| `protocolo/Protocolo_registro_revisao.pdf` | registro do protocolo na versão 2.0 |
| `dados/01_buscas/scopus/scopus_consultas.csv` | quadro das consultas da Scopus e registros únicos por expressão |
| `dados/01_buscas/lista/lista_consultas.csv` | quadro das consultas da LISTA e registros únicos por expressão |
| `dados/01_buscas/capes/capes_consultas.csv` | quadro das consultas do Portal da CAPES, com o registro do bloqueio |
| `dados/02_triagem/estatisticas_bases_novas.json` | consolidação da incorporação das bases novas |
| `dados/02_triagem/triagem_bases_novas_stats.json` | totais da triagem das bases novas |
