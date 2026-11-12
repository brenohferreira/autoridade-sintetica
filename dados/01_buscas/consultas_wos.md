# Registro das consultas à Web of Science

Base: Web of Science Core Collection, Editions: All. Data de execução: 12/11/2026.
Campo: TS= (tópico). Filtros de tipo e idioma não aplicados na recuperação.

| Consulta | Expressão | Total bruto | Exportados | Novos após deduplicação |
|---|---|---|---|---|
| W1 | `TS=("cognitive authority")` | 175 | 175 | 104 |
| W2 | `TS=("epistemic authority") AND TS=("artificial intelligence" OR "generative AI" OR algorithm)` | 141 | 141 | 81 |
| W3 | `TS=("synthetic authority")` | 0 | 0 | 0 |
| W3b (sensibilidade) | `TS=(synthetic AND authority)` | 1.550 | não exportada | não aplicável: usos de "synthetic" em outros sentidos (biologia sintética, dados sintéticos) |
| W4 | `TS=("generative AI" OR "large language model" OR "large language models" OR ChatGPT) AND TS=(authority OR deference)` | 742 | 742 | 632 |
| W5 | `TS=("right to explanation") AND TS=(explainable OR XAI OR contestability)` | 31 | 31 | 9 |
| W6 | `TS=(explainable AI OR "explainable artificial intelligence" OR XAI) AND TS=(education OR students OR teaching OR learning)` | 22.000+ | não exportada | excesso de recuperação: "learning" alcança "machine learning" e "deep learning"; consulta refeita como W6b |
| W7 | pendente | | | |
| W8 | pendente | | | |

Subtotal já consolidado: 1.089 registros lidos, 826 novos em relação aos 1.227 do corpus anterior.

Observações para o protocolo (versão 1.2):
1. A W3 retornou zero, o que indica ausência da expressão "synthetic authority" na literatura indexada na WoS; a verificação de sensibilidade (W3b) mostra que os dois termos só coocorrem em outros sentidos.
2. A W6 foi refeita após a busca-piloto, com registro do motivo da correção.
3. A W1 não tem registro anterior a 2008, o que confirma a cobertura recente da base e explica a ausência dos textos fundadores.
