# Autoridade sintética na IA generativa e explicabilidade como direito

Este repositório reúne os dados, o protocolo e os scripts produzidos para a revisão de escopo sobre a autoridade que os usuários atribuem à inteligência artificial generativa e sobre as condições em que a explicabilidade permite examinar e contestar suas respostas. O texto do artigo não é redistribuído aqui.

## Objetivo

Compreender como a literatura sobre autoridade cognitiva e autoridade epistêmica permite interpretar a autoridade atribuída à IA generativa e em que condições a explicabilidade possibilita examinar e contestar suas respostas, distinguindo o que o usuário efetivamente faz ao tratar uma resposta como razão daquilo que tornaria essa atribuição justificada.

## Estrutura do Repositório

- **dados/01_buscas/**: expressões exatas, filtros, totais por consulta, registros brutos das bases e rastreamento de citações.
- **dados/01_buscas/wos_bruto/**: as oito exportações originais da Web of Science Core Collection, no formato de texto da Clarivate, e os registros convertidos em JSON.
- **dados/02_triagem/**: registros únicos após deduplicação, candidatos avaliados, triagem e exclusões da Web of Science e estatísticas do corpus.
- **dados/03_extracao/**: matriz de extração com os 80 estudos incluídos, localizadores de página e uso de cada fonte.
- **dados/04_planilha/**: planilha auditável com as abas de buscas, triagem, extração e fluxo.
- **protocolo/**: protocolo v1.3, redigido antes das buscas definitivas, com a emenda que incorpora a Web of Science, em DOCX, PDF e Markdown.
- **figuras/**: diagrama de seleção (PRISMA-ScR) e distribuição temporal dos estudos, em 300 dpi.
- **scripts/**: rotinas de coleta, deduplicação, triagem, verificação de metadados, extração e geração das figuras.
- **checklist/**: lista de verificação PRISMA-ScR preenchida, item por item.
- **fontes/**: metadados verificados em Crossref e registro dos downloads de textos completos.

## Dados

As buscas foram executadas em oito fontes e percursos: OpenAlex, BRAPCI, Google Acadêmico, Web of Science Core Collection, rastreamento de citações a partir de dois estudos-semente e busca nominal dirigida. As expressões, os filtros e os totais de cada consulta estão em `dados/01_buscas/consultas_bases.csv` e, no caso da Web of Science, em `dados/01_buscas/wos_consultas.md`.

As exportações da Web of Science são redistribuídas exatamente como saíram da plataforma, sem edição de conteúdo, e receberam nomes que identificam a consulta de origem:

| Arquivo | Registros | Consulta |
|---|---|---|
| `W01_autoridade_cognitiva.txt` | 175 | `TS=("cognitive authority")` |
| `W01b_autoridade_cognitiva_complemento.txt` | parte final de W01 | continuação da exportação anterior, dividida pelo limite da plataforma |
| `W02_autoridade_epistemica_ia.txt` | 25 | autoridade epistêmica combinada com inteligência artificial |
| `W04_ia_generativa_llm.txt` | 1.550 | IA generativa, modelos de linguagem e autoridade |
| `W05_direito_a_explicacao.txt` | 132 | direito à explicação e explicabilidade |
| `W06_explicabilidade_educacao.txt` | 1.160 | explicabilidade aplicada à educação, exportada em três partes |
| `W07_vies_de_automacao.txt` | 640 | viés de automação e confiança excessiva |
| `W08_heuristica_da_maquina.txt` | 480 | heurística da máquina e autoridade sintética |

As consultas ao Google Acadêmico foram feitas por navegador e não podem ser reexecutadas por script, pois a plataforma bloqueia acesso automatizado; por isso, as datas e os totais exibidos ficaram registrados no arquivo de consultas. A busca na Scopus não foi executada, por exigir assinatura própria.

## Metodologia

A revisão seguiu a metodologia do JBI e as orientações de relato do PRISMA-ScR, com protocolo redigido e datado antes das buscas definitivas. Cada base recebeu oito consultas, com expressões exatas entre aspas e campos de busca equivalentes, e a triagem ocorreu em duas etapas: exclusão automática por script, a partir de critérios de escopo declarados no protocolo, e leitura de títulos, resumos e textos completos. A extração registrou, para cada estudo, a linha de investigação, o tipo de evidência, o uso no argumento e o localizador de página quando o texto completo estava disponível.

## Números da revisão

Foram identificados 4.040 registros: 1.219 na OpenAlex, 2.567 na Web of Science Core Collection, 49 na BRAPCI, 80 no Google Acadêmico, 106 por rastreamento de citações e 19 por busca nominal dirigida. Após a remoção de 649 duplicatas, restaram 3.391 registros únicos, e a triagem excluiu 3.311, o que resultou em 80 estudos incluídos, publicados entre 1983 e 2026, dos quais 35 tiveram o texto completo examinado e 45 foram incorporados a partir do resumo. A expressão exata *synthetic authority* não retornou nenhum registro na Web of Science. Dos 3.391 registros únicos, 2.388 (70,6%) foram publicados em 2025 ou 2026, 701 (20,7%) entre 2020 e 2024 e 295 (8,7%) antes de 2020, e 223 (6,6%) provêm de repositórios de preprint.

## Reprodutibilidade

Os scripts foram escritos em Python 3.11 e dependem de `requests`, `beautifulsoup4`, `openpyxl`, `python-docx` e `matplotlib`. A reprodução das análises pode ser realizada pela execução sequencial dos scripts disponíveis na pasta `scripts/`.

```bash
pip install -r requirements.txt
python scripts/harvest.py        # coleta nas bases e registro das consultas
python scripts/triagem.py        # deduplicação e triagem de primeiro nível
python scripts/verificar.py      # conferência de metadados no Crossref
python scripts/gerar_xlsx.py     # planilha auditável
python scripts/estat_corpus.py   # distribuição por ano do corpus completo (figura 2)
python scripts/figuras.py        # figuras 1 e 2
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

A citação do depósito está descrita no arquivo `CITATION.cff`. Enquanto não houver identificador persistente, use:

> FERREIRA, Breno Heleno. **Autoridade sintética na IA generativa e explicabilidade como direito: dados, protocolo e scripts de uma revisão de escopo**. Versão 1.2.0. 2026. Repositório GitHub. Disponível em: https://github.com/brenohferreira/autoridade-sintetica. Acesso em: [data].

## Licença

Os dados, o protocolo e as figuras estão licenciados sob **Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)**, cujo texto integral está em `LICENSE`. Os scripts estão licenciados sob **MIT**, em `LICENSE-CODE`.
