# Estado da revisão após a incorporação da Web of Science (12/11/2026)

## Números consolidados

| Etapa | Valor |
|---|---|
| Registros identificados | 4.040 |
| Duplicatas removidas | 649 (246 entre bases anteriores; 403 da WoS) |
| Registros únicos triados | 3.391 |
| Excluídos na triagem | 3.311 |
| Estudos incluídos | 80 |
| Texto completo examinado | 35 |
| Incorporados pelo resumo | 45 |
| Fundamentos | 18 |
| Autoridade e IA | 30 |
| Explicabilidade e direito | 20 |
| Educação | 12 |

Composição da identificação: BRAPCI 49, OpenAlex 1.219, Google Acadêmico 80, rastreamento de citações 106,
busca dirigida 19, Web of Science 2.567.

## Consultas à Web of Science (12/11/2026, Core Collection, campo TS)

| Consulta | Total bruto | Exportados | Novos |
|---|---|---|---|
| W1 "cognitive authority" | 175 | 175 | 104 |
| W2 epistemic authority + IA | 141 | 141 | 81 |
| W3 "synthetic authority" | 0 | 0 | 0 |
| W3b synthetic AND authority (sensibilidade) | 1.550 | não exportada | usos em outro sentido |
| W4 generative AI + authority/deference | 742 | 742 | 632 |
| W5 right to explanation + XAI | 31 | 31 | 9 |
| W6 explainable AI + educação (versão corrigida) | 1.160 | 1.160 | 1.093 |
| W7 automation bias + LLM | 245 | 245 | 172 |
| W8 "machine heuristic" | 73 | 73 | 73 |
| **Total** | **2.567** | **2.567** | **2.164** |

Tentativas descartadas e registradas: W6 original com "learning" (22 mil, excesso por machine learning);
W6 com TI= (7 mil, mesmo motivo); W3 exata = 0.

## Arquivos

- `wos/registros_wos.json` — 2.567 registros da WoS com marcação de duplicidade.
- `wos/novos.csv` — 2.164 registros novos, com resumo.
- `wos/triagem_etapa_a.csv` — 2.051 elegíveis com pontuação de pertinência.
- `wos/excluidos_etapa_a.csv` — 113 exclusões automáticas com motivo.
- `wos/registro_consultas.md` — tabela de consultas e observações para o protocolo.
- `scripts/dados_wos.py` — 25 estudos incluídos (N01 a N25), com referência ABNT, achado e localizador.
- `scripts/texto_a.py`, `scripts/texto_b.py` — artigo atualizado (4.040/3.391/80; seção 2.2 com a WoS;
  parágrafo sobre o uso do Manus; seis parágrafos novos integrando os estudos de 2026).
- `figuras/fig1_fluxo.png` — fluxo atualizado; `figuras/fig2_periodo.png`.
- `entrega/Artigo_autoridade_sintetica.docx` e `.pdf` — versão ABNT integral, 30 páginas.
- `entrega/Artigo_autoridade_sintetica_15paginas.docx` e `.pdf` — versão compacta, 15 páginas.

## Pendências

1. Protocolo: subir para a versão 1.2, registrando a execução da WoS, a correção da W6 e a triagem assistida.
2. Planilha auditável: regenerar com 82 estudos e as abas da WoS.
3. Checklist PRISMA-ScR: atualizar os números dos itens 7, 8, 14 e 15.
4. GitHub: criar o repositório `autoridade-sintetica` (o conector não tem permissão de criação) e publicar
   como versão 1.1.0, com os dados da WoS e o artigo novo.
