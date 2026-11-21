# AUTORIDADE SINTÉTICA NA INTELIGÊNCIA ARTIFICIAL GENERATIVA: UMA REVISÃO DE ESCOPO SOBRE AUTORIDADE COGNITIVA, AUTORIDADE EPISTÊMICA E EXPLICABILIDADE

Este repositório reúne os dados, o protocolo, as figuras e os scripts produzidos para a revisão de escopo sobre a autoridade que os usuários atribuem à inteligência artificial generativa e sobre as condições em que a explicabilidade permite examinar e contestar suas respostas. O artigo que sintetiza os resultados é redistribuído na pasta `artigo/`, na versão 2.3.0, em DOCX e PDF, ao lado da emenda ao protocolo que registra a execução das bases incorporadas nesta versão.

## Objetivo

Compreender como a literatura sobre autoridade cognitiva e autoridade epistêmica permite interpretar a autoridade atribuída à IA generativa e em que condições a explicabilidade possibilita examinar e contestar suas respostas, distinguindo o que o usuário efetivamente faz ao tratar uma resposta como razão daquilo que tornaria essa atribuição justificada.

## Registro do protocolo na OSF

O protocolo desta revisão está registrado e público na OSF, como OSF Preregistration, em [https://osf.io/kvzqd/](https://osf.io/kvzqd/), com vinculação ao ORCID do autor, [0000-0003-0285-7414](https://orcid.org/0000-0003-0285-7414), e com link de visualização compartilhável que dispensa conta na plataforma, em https://osf.io/kvzqd/overview?view_only=df74f9344b324e5081c78fcf52d63e09. O registro reúne as questões de pesquisa, a estrutura população, conceito e contexto, o desenho em cinco etapas, a estratégia de amostragem com os critérios de elegibilidade, as variáveis e os índices derivados, o plano de análise e as declarações de financiamento, de conflitos de interesse, de disponibilidade de dados e de uso de inteligência artificial, e foi declarado retrospectivo, com justificativa das providências adotadas para reduzir o risco de influência do conhecimento dos resultados sobre o plano. A versão integral do protocolo permanece nesta pasta, em `protocolo/Protocolo_registro_revisao_v2.3.0.pdf` e em `protocolo/Protocolo_registro_revisao_v2.3.0.docx`, e a página publicada deste repositório serve o mesmo arquivo em https://brenohferreira.github.io/autoridade-sintetica/protocolo/Protocolo_registro_revisao_v2.3.0.pdf.

## Estrutura do Repositório

- **artigo/**: artigo completo na versão 2.3.0, em DOCX e PDF, com as figuras incorporadas e a lista de referências atualizada.
- **dados/01_buscas/**: expressões exatas, filtros, totais por consulta, registros brutos das bases e rastreamento de citações.
- **dados/01_buscas/wos_bruto/**: as sete exportações originais da Web of Science Core Collection, no formato de texto da Clarivate, e os registros convertidos em JSON.
- **dados/01_buscas/bdtd/**, **dados/01_buscas/scopus/**, **dados/01_buscas/lista/** e **dados/01_buscas/capes/**: registros recuperados e quadros de consultas das bases incorporadas nas versões 2.1.0 e 2.2.0, com o total declarado por expressão e o número de registros únicos que permaneceram após a deduplicação interna de cada base.
- **dados/02_triagem/**: registros únicos após deduplicação, candidatos avaliados, triagem e exclusões da Web of Science, triagem das bases incorporadas na versão 2.2.0 e estatísticas do corpus.
- **dados/06_capes/**: coleta manual no Portal de Periódicos da CAPES, com os dezoito arquivos RIS, o consolidado dos 1.146 registros exportados, os 348 candidatos com resumo, os três arquivos de triagem, a lista dos 38 elegíveis pela regra lexical, os 20 estudos incorporados e os scripts que aplicam a regra.
- **dados/03_extracao/**: matriz de extração do corpus inicial, com 57 estudos, localizadores de página e uso de cada fonte, e a relação dos 42 estudos incorporados na versão 2.2.0.
- **dados/04_planilha/**: planilha auditável com as abas de buscas, buscas das bases novas, triagem, triagem das bases novas, texto completo, extração, estudos incluídos novos, fluxo e bibliometria.
- **dados/05_bibliometria.csv** e **dados/05_bibliometria_resumo.csv**: veículo, área do conhecimento, país e instituição de afiliação dos estudos do corpus inicial, com os totais agregados.
- **protocolo/**: protocolo registrado antes das buscas definitivas e emenda de ampliação de fontes na versão 2.3, em DOCX, PDF e Markdown.
- **figuras/**: diagrama de seleção (PRISMA-ScR) e figura de distribuição temporal e por área do conhecimento, em 300 dpi, refeitos para os totais da versão 2.3.0.
- **scripts/**: rotinas de coleta, deduplicação, triagem, verificação de metadados, extração e geração das figuras.
- **checklist/**: lista de verificação PRISMA-ScR preenchida, item por item.
- **fontes/**: metadados verificados em Crossref e registro dos downloads de textos completos.

## Dados

As buscas foram executadas em dez fontes e percursos, a saber, BRAPCI, OpenAlex, Google Acadêmico, Web of Science Core Collection, Scopus, LISTA, Portal de Periódicos da CAPES, Biblioteca Digital Brasileira de Teses e Dissertações, rastreamento de citações a partir de dois estudos-semente e busca nominal dirigida. As expressões, os filtros e os totais de cada consulta estão em `dados/01_buscas/consultas_bases.csv`, no caso da Web of Science em `dados/01_buscas/wos_consultas.md` e, para as bases incorporadas nas duas últimas versões, nos quadros de consultas publicados nas pastas `bdtd/`, `scopus/`, `lista/` e `capes/`.

As exportações da Web of Science são redistribuídas exatamente como saíram da plataforma, sem edição de conteúdo, e receberam nomes que identificam a consulta de origem:

| Arquivo | Registros | Consulta |
|---|---|---|
| `W01_autoridade_cognitiva.txt` | 175 | `TS=("cognitive authority")` |
| `W01b_autoridade_cognitiva_complemento.txt` | parte final de W01 | continuação da exportação anterior, dividida pelo limite da plataforma |
| `W02_autoridade_epistemica_ia.txt` | 141 | `TS=("epistemic authority") AND TS=("artificial intelligence" OR "generative AI" OR algorithm)` |
| `W04_ia_generativa_llm.txt` | 742 | `TS=("generative AI" OR "large language model" OR "large language models" OR ChatGPT) AND TS=(authority OR deference)` |
| `W05_direito_a_explicacao.txt` | 31 | `TS=("right to explanation") AND TS=("explainable AI" OR XAI OR contestability)` |
| `W06_vies_de_automacao.txt` | 245 | `TS=("automation bias") AND TS=("large language model" OR "large language models" OR "generative AI" OR "clinical decision")` |
| `W07_heuristica_da_maquina.txt` | 73 | `TS=("machine heuristic")` |

As consultas ao Google Acadêmico foram feitas por navegador e não podem ser reexecutadas por script, pois a plataforma bloqueia acesso automatizado, de modo que as datas e os totais exibidos ficaram registrados no arquivo de consultas. A Scopus, a LISTA e o Portal de Periódicos da CAPES foram executados em 20 de novembro de 2026, por acesso remoto autenticado na Universidade Federal de Minas Gerais,.

### Quadro de status das bases

| Base | Situação | Registros | Observação |
|---|---|---|---|
| BRAPCI | executada | 48 | interface pública de busca, oito consultas |
| OpenAlex | executada | 1.019 | interface pública, teto de 200 registros nas consultas amplas |
| Google Acadêmico | executada | 70 | consulta por navegador, primeiros resultados de cada expressão |
| Web of Science Core Collection | executada | 1.407 | acesso institucional, sete consultas no campo de tópico |
| Scopus | executada | 2.671 | seis consultas, 2.801 recuperados; a consulta de explicabilidade declarou 43.627 resultados e recebeu teto de 200 |
| LISTA | executada | 327 | seis consultas pela EBSCO, 500 recuperados; a consulta de explicabilidade declarou 354 resultados e recebeu teto de 200 |
| Portal de Periódicos da CAPES | executada com bloqueio parcial | 60 | C1 e C2 executadas, com 94 e 80 resultados e 30 recuperados cada; C3 sem resultados; C4, C5 e C6 bloqueadas pelo firewall CloudFront |
| BDTD | executada | 1.029 | doze consultas em todos os campos, teto de 240 registros por consulta |
| Rastreamento de citações | executada | 106 | dois estudos-semente |
| Busca nominal dirigida | executada | 8 | recuperação de textos fundacionais pelo nome |

O bloqueio de três consultas do Portal de Periódicos da CAPES também está registrado no protocolo, porque o firewall do serviço recusou toda expressão com mais de um operador booleano, inclusive após a codificação dos parênteses e a reescrita distributiva dos termos, e as consultas executadas devolveram registros em grande parte sobrepostos às bases já coletadas.

## Metodologia

A revisão seguiu a metodologia do JBI e as orientações de relato do PRISMA-ScR, com protocolo redigido e datado antes das buscas definitivas e emendas registradas a cada ampliação de fontes, na versão 2.3 de 20 de novembro de 2026. Cada base recebeu expressões construídas para as mesmas frentes conceituais, com termos entre aspas e campos de busca equivalentes, e a triagem ocorreu em duas etapas, a saber, exclusão automática por script, a partir dos critérios de escopo declarados no protocolo, e leitura de títulos, resumos e textos completos. A extração registrou, para cada estudo, a linha de investigação, o tipo de evidência, o uso no argumento e o localizador de página quando o texto completo estava disponível.

## Números da revisão

Foram identificados 7.831 registros, assim distribuídos: 2.671 na Scopus, 1.407 na Web of Science Core Collection, 1.146 no Portal de Periódicos da CAPES, 1.029 na BDTD, 1.019 na OpenAlex, 327 na LISTA, 106 por rastreamento de citações, 70 no Google Acadêmico, 48 na BRAPCI e 8 por busca nominal dirigida. Após a remoção de 1.654 duplicatas, restaram 6.177 registros triados, dos quais 1.629 foram lidos por título e resumo, e a triagem resultou em 125 estudos incluídos, sendo 119 artigos, capítulos e trabalhos em anais e 6 teses e dissertações.

A incorporação das bases novas somou 3.058 registros identificados, com 65 duplicatas entre elas e 344 em relação ao corpus anterior, o que resultou em 2.649 registros novos e elevou o corpus único de 3.601 para 6.250 registros. A triagem dessas bases excluiu 1.033 registros por tipo de documento e por domínio alheio ao escopo, submeteu 1.616 candidatos à leitura de título e resumo e incorporou 42 estudos, sendo 40 provenientes da Scopus e 2 da LISTA, de modo que os 125 estudos correspondem aos 57 estudos do corpus inicial, às 6 teses e dissertações recuperadas na BDTD, aos 42 estudos incorporados na versão 2.2.0 e aos 20 incorporados na versão 2.3.0.

A coleta no Portal de Periódicos da CAPES foi refeita manualmente em 20 de novembro de 2026, com doze expressões na busca avançada e exportação em arquivo RIS, o que recuperou 1.146 registros, dos quais 284 eram duplicatas internas, 514 já constavam do corpus e 348 permaneceram como candidatos. A triagem desses candidatos, feita em três passos com apoio de modelos de linguagem e conferência manual das decisões limítrofes, aprovou 69 registros, aos quais se aplicou uma regra lexical declarada antes da seleção, com três condições cumulativas, a presença de termo de inteligência artificial no título ou no resumo, a densidade de pelo menos três termos de autoridade e o resumo com 500 caracteres ou mais. A regra reteve 38 registros, dos quais 20 foram incorporados, o que elevou o corpus de 105 para 125 estudos, e a lista completa dos elegíveis, com as métricas de cada registro, está em `dados/06_capes/`.


O intervalo temporal dos 125 estudos vai de 1983 a 2026, com 80 deles, ou 64,0%, publicados em 2025 ou 2026. Entre os 6.000 registros únicos com ano informado, 3.985, ou 66,4%, foram publicados em 2025 ou 2026, 1.366, ou 22,8%, entre 2020 e 2024 e 649, ou 10,8%, antes de 2020, e 193 registros, ou 3,2%, provinham de repositórios de preprint ou de publicação não revisada por pares, com destaque para Zenodo, com 77 registros, SSRN, com 76, e arXiv, com 36. A expressão exata *synthetic authority* retornou três registros declarados na Scopus, 24 na LISTA e nenhum na Web of Science, no Portal de Periódicos da CAPES e na BDTD, o que confirma o caráter incipiente do termo.

## Reprodutibilidade

Os scripts foram escritos em Python 3.11 e dependem de `requests`, `beautifulsoup4`, `openpyxl`, `python-docx` e `matplotlib`. A reprodução das análises pode ser realizada pela execução sequencial dos scripts disponíveis na pasta `scripts/`.

```bash
pip install -r requirements.txt
python scripts/harvest.py         # coleta nas bases e registro das consultas
python scripts/triagem.py         # deduplicação e triagem de primeiro nível
python scripts/consultas_v220.py  # quadros de consultas da Scopus, da LISTA e da CAPES
python scripts/verificar.py       # conferência de metadados no Crossref
python scripts/gerar_xlsx.py      # planilha auditável
python scripts/estat_corpus.py    # distribuição por ano do corpus completo (figura 2)
python scripts/figuras.py         # figuras 1 e 2
```

## Autor

**Breno Heleno Ferreira**

Doutorando em Ciência da Informação (UFMG)
Mestre em Educação e Docência (UFMG)
MBA em Data Science e Analytics (USP)
MBA em Gestão de Projetos (USP)

📧 brenohferreira@ufmg.br

GitHub: https://github.com/brenohferreira
Lattes: http://lattes.cnpq.br/5720093855838869

## Como citar

A citação do depósito está descrita no arquivo `CITATION.cff`. Enquanto não houver identificador persistente atribuído pela OSF, use:
> FERREIRA, Breno Heleno. **AUTORIDADE SINTÉTICA NA INTELIGÊNCIA ARTIFICIAL GENERATIVA: UMA REVISÃO DE ESCOPO SOBRE AUTORIDADE COGNITIVA, AUTORIDADE EPISTÊMICA E EXPLICABILIDADE: dados, protocolo e scripts**. Versão 2.3.0. 2026. Repositório GitHub. Disponível em: https://github.com/brenohferreira/autoridade-sintetica. Acesso em: [data].
O protocolo registrado na OSF cita-se como:
> FERREIRA, Breno Heleno. **Protocolo e registro da revisão de escopo: autoridade sintética, autoridade cognitiva e autoridade epistêmica na inteligência artificial generativa (versão 2.3)**. OSF Preregistration. 2026. Disponível em: https://osf.io/kvzqd/. Acesso em: [data].

## Licença

Os dados, o protocolo, as figuras e o artigo estão licenciados sob **Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)**, cujo texto integral está em `LICENSE`. Os scripts estão licenciados sob **MIT**, em `LICENSE-CODE`.
