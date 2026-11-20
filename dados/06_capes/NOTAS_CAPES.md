# Coleta manual no Portal de Periódicos da CAPES (20 nov. 2026)

## Consultas executadas e totais declarados

| Código | Expressão | Total | Exportado | Já no corpus | Candidatos |
|---|---|---|---|---|---|
| C1 | "cognitive authority" | 94 | 30 | — | — |
| C2 | "epistemic authority" AND "artificial intelligence" | 80 | 30 | — | — |
| C3 | "synthetic authority" | 0 | 0 | — | — |
| C4a | "generative AI" AND authority | 145 | 142 | 100 | 42 |
| C4b | "large language model" AND authority | ≥100 | 100 | 77 | 23 |
| C4c | ChatGPT AND authority | 89 | 89 | 57 | 32 |
| C4d | "generative AI" AND deference | 2 | 2 | — | — |
| C5a | "right to explanation" | 63 | 63 | 40 | 23 |
| C5b | "explainable AI" AND authority | 38 | 38 | 2 | 36 |
| C5c | XAI AND authority | 89 | 89 | 24 | 65 |
| C5d | contestability AND "artificial intelligence" | 70 | 70 | 6 | 64 |
| C6a | "automation bias" | 325 | 325 | 239 | 86 |
| C6b | "machine heuristic" | 53 | 53 | 46 | 7 |
| C6c | "algorithmic authority" | 46 | 46 | — | — |
| (5) | não identificada | 100 | 100 | — | — |
| (6) | não identificada | 26 | 26 | — | — |

Arquivos RIS em `/home/ubuntu/upload/Periodicos-CAPES-RIS*.ris`, cópias nomeadas em `capes_manual/`.

## Consolidação

- 1.146 registros exportados; 994 únicos entre consultas; 132 duplicados internos.
- 514 duplicados do corpus anterior; 348 candidatos novos.
- Total identificado da fonte: 1.146 (contra 60 registrados na emenda v2.2).

## Triagem em três passos (LLM)

1. Pertinência (gpt-5-nano, lote 25): 348 avaliados, 135 aprovados.
2. Centralidade 0 a 3 (gpt-5-mini, lote 12): 135 avaliados, notas 3=96, 2=28, 1=9, 0=2.
3. Decisão final (gpt-5-mini, lote 10): 124 avaliados, 69 aprovados, 55 rejeitados.

Arquivos: `triagem_capes_1.jsonl`, `triagem_capes_1b.jsonl`, `triagem_capes_2.jsonl`, `triagem_capes_3.jsonl`, `candidatos_capes.csv` (com resumos da OpenAlex, 312 de 348).

## Pendências

- Identificar as consultas (5), de 100 registros, e (6), de 26.
- Total declarado da C4b (exportou 100, pode haver segunda página).
- Decidir se a incorporação ao artigo será integral (69 estudos, corpus 174) ou limitada por regra lexical auditável (cerca de 20, corpus 125), com atualização para a versão 2.3.0.
