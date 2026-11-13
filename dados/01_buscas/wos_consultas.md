# Registro das consultas à Web of Science

Base: Web of Science Core Collection, Editions: All. Data de execução: 12/11/2026.
Campo: TS= (tópico). Filtros de tipo e idioma não aplicados na recuperação; a restrição de escopo foi feita na triagem.

| Consulta | Expressão | Total bruto | Exportados | Novos após deduplicação |
|---|---|---|---|---|
| W1 | `TS=("cognitive authority")` | 175 | 175 | 111 |
| W2 | `TS=("epistemic authority") AND TS=("artificial intelligence" OR "generative AI" OR algorithm)` | 141 | 141 | 83 |
| W3 | `TS=("synthetic authority")` | 0 | 0 | 0 |
| W3b (sensibilidade) | `TS=(synthetic AND authority)` | 1.550 | não exportada | não aplicável: usos de "synthetic" em outros sentidos (biologia sintética, dados sintéticos) |
| W4 | `TS=("generative AI" OR "large language model" OR "large language models" OR ChatGPT) AND TS=(authority OR deference)` | 742 | 742 | 636 |
| W5 | `TS=("right to explanation") AND TS=("explainable AI" OR XAI OR contestability)` | 31 | 31 | 9 |
| W6 | `TS=("automation bias") AND TS=("large language model" OR "large language models" OR "generative AI" OR "clinical decision")` | 245 | 245 | 178 |
| W7 | `TS=("machine heuristic")` | 73 | 73 | 73 |
| **Total** | | **1.407** | **1.407** | **1.090** |

Dos 1.090 registros novos, 1.071 tinham metadados suficientes para a triagem; os 19 restantes foram descartados por ausência de resumo ou de identificador. A triagem automática e manual está em `../../02_triagem/wos_triagem.csv` e as exclusões automáticas, em `../../02_triagem/wos_excluidos.csv`.

## Observações registradas no protocolo

1. A W3 retornou zero, o que indica ausência da expressão "synthetic authority" na literatura indexada na Web of Science; a verificação de sensibilidade (W3b) mostra que os dois termos só coocorrem em outros sentidos.
2. A W1 não tem registro anterior a 2008, o que confirma a cobertura recente da base e explica a ausência dos textos fundadores, recuperados por busca nominal dirigida.
3. As expressões foram construídas para replicar, no campo de tópico, as frentes conceituais consultadas nas demais bases, com adaptação à sintaxe booleana da plataforma.
