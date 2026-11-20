# Registro de alterações

Todas as versões do depósito são identificadas por etiqueta no repositório e correspondem a um estado completo dos dados, do protocolo e dos scripts.

## 2.3.0: 20 de novembro de 2026
Coleta manual no Portal de Periódicos da CAPES, regra lexical de incorporação e ampliação do corpus de 105 para 125 estudos.
- Coleta manual na busca avançada do Portal, autenticada pelo acesso remoto da Universidade Federal de Minas Gerais, com doze expressões, de C1 a C6c, e exportação em dezoito arquivos RIS, o que recuperou 1.194 registros declarados e 1.146 exportados.
- Consolidação com 284 duplicatas internas ao Portal, 514 registros já presentes no corpus e 348 candidatos novos.
- Triagem em três passos, com 348 candidatos avaliados na pertinência, 135 aprovados, notas de centralidade 3 (96), 2 (28), 1 (9) e 0 (2) e 69 aprovados na decisão final.
- Regra lexical auditável com três condições cumulativas, aplicada aos 69 aprovados, que reteve 38 registros e incorporou 20 estudos, com prioridade para o eixo de explicabilidade e contestação.
- Atualização do fluxo para 7.831 registros identificados, 1.654 duplicatas, 6.177 registros únicos, 1.629 lidos por título e resumo e 125 estudos incluídos, com 134 referências.
- Artigo reescrito na versão 2.3.0 no padrão tipográfico da versão revisada e normalizada, com o Quadro 4 das consultas ao Portal, a renumeração do quadro das três formas de autoridade e as figuras refeitas.

## 2.2.0: 20 de novembro de 2026

Ampliação de fontes com a execução da Scopus, da LISTA e do Portal de Periódicos da CAPES, a declaração de indisponibilidade da LISA e a ampliação do corpus de 63 para 163 estudos.

- Execução da Scopus em seis consultas no campo de título, resumo e palavras-chave, com 181, 185, 3, 1.142, 43.627 e 1.090 resultados declarados e 2.801 registros recuperados, dos quais 2.671 permaneceram únicos.
- Execução da LISTA em seis consultas no campo de título e resumo, com 59, 3, 24, 38, 354 e 22 resultados declarados e 500 registros recuperados, dos quais 327 permaneceram únicos.
- Execução parcial do Portal de Periódicos da CAPES, com 94 resultados e 30 recuperados na consulta C1, 80 resultados e 30 recuperados na C2, nenhum resultado na C3 e bloqueio das consultas C4, C5 e C6 pelo firewall CloudFront do serviço, o que totalizou 60 registros.
- Declaração de indisponibilidade da LISA, uma vez que a assinatura ProQuest da Universidade Federal de Minas Gerais, de identificador 134127, oferece apenas Coronavirus Research Database, Ebook Central, Education Research Index e Publicly Available Content Database, sem a Library and Information Science Abstracts; as expressões permanecem registradas no protocolo para execução futura.
- Adoção do teto de 200 registros por consulta nas expressões de explicabilidade da Scopus, com 43.627 resultados declarados, e da LISTA, com 354 resultados declarados, decisão equivalente à já aplicada à OpenAlex, ao Google Acadêmico e à BDTD e declarada nas figuras de fluxo e nas limitações do artigo.
- Consolidação da incorporação: 3.058 registros identificados nas bases novas, 65 duplicatas entre elas e 344 em relação ao corpus anterior, o que resultou em 2.649 registros novos e elevou o corpus único a 6.250 registros.
- Triagem das bases novas com 1.033 registros excluídos, 1.616 candidatos submetidos à leitura de título e resumo e 100 estudos incluídos, sendo 98 da Scopus e 2 da LISTA.
- Recálculo integral do fluxo: 6.745 registros identificados, 916 duplicatas removidas, 5.829 registros triados, 2.211 lidos por título e resumo, 5.666 não incluídos e 163 estudos incluídos, dos quais 157 artigos, capítulos e trabalhos em anais e 6 teses e dissertações, publicados entre 1983 e 2026, com 113 estudos, ou 69,3%, de 2025 ou 2026.
- Estatísticas do corpus completo atualizadas para 6.250 registros únicos, dos quais 5.652 com ano informado e 193 provenientes de repositórios de preprint.
- Figuras 1 e 2 refeitas para os novos totais, com o quadro das dez fontes e percursos e a distribuição temporal dos 5.652 registros com ano.
- Planilha auditável regerada, com as abas de buscas das bases novas, triagem das bases novas e estudos incluídos novos conciliadas com o fluxo.
- Emenda ao protocolo atualizada para a versão 2.2, de 20 de novembro de 2026, com os quadros de consultas da Scopus, da LISTA e do Portal de Periódicos da CAPES, o registro das decisões metodológicas e o histórico de versões.
- Artigo incorporado ao depósito na versão 2.2.0, em DOCX e PDF, na pasta artigo/.
- Dados de coleta e de triagem das bases novas publicados em dados/01_buscas/scopus/, dados/01_buscas/lista/, dados/01_buscas/capes/, dados/02_triagem/ e dados/03_extracao/.

## 2.1.0 — 19 de novembro de 2026
Ampliação de fontes e correção do recorte temporal do artigo.
- Execução da BDTD em doze consultas de todos os campos, sem filtros, que somaram 1.029 registros e 740 elegíveis após deduplicação e exclusão automática.
- Inclusão de seis teses e dissertações brasileiras: 2015 (autoridade cognitiva em redes sociais), 2023 (padrões de autoridade em fóruns), 2025 (duas, confiança em IA e explicações geradas por LLM), 2025 (autoridade algorítmica) e 2026 (explicabilidade e confiança de investidores).
- Recálculo integral do fluxo: 3.687 registros identificados, 507 duplicatas removidas, 3.180 triados, 3.117 não incluídos e 63 estudos incluídos, dos quais 12 com texto completo e 51 pelo resumo.
- Bibliometria atualizada: 56 estudos com afiliação recuperada, 24 países, Brasil com 6 estudos e computação e interação humano-computador com 23 estudos.
- Figuras 1 e 2 refeitas para os novos totais.
- Acrescentado o documento de emenda ao protocolo, com as expressões pendentes para LISA, LISTA, Scopus e Portal de Periódicos da CAPES.
- Dados brutos e de triagem da BDTD publicados em dados/01_buscas/bdtd/.
## 2.0.1 — 12 de novembro de 2026
- Figura 1 substituída pela versão final publicada no artigo: fluxograma em funil com os totais por fonte, as 372 duplicatas discriminadas, os 2.229 registros não incluídos, a composição dos 57 estudos e os critérios de exclusão E1 a E6.
- Nenhuma alteração nos dados, no protocolo ou nos totais; a versão preserva a reconciliação com as abas de triagem e extração da planilha.
## 2.0.0 — 12 de novembro de 2026

Consolidação do depósito no recorte final do artigo: a autoridade atribuída à IA generativa e os limites da explicabilidade.

- Execução da Web of Science Core Collection, com acesso institucional pelo Portal de Periódicos da CAPES, em sete consultas no campo de tópico, que somaram 1.407 registros e 1.090 novos após deduplicação.
- Recálculo integral do fluxo de seleção: 2.658 registros identificados, 372 duplicatas removidas, 2.286 registros triados, 2.229 excluídos e 57 estudos incluídos.
- Substituição do corpus anterior, com nova matriz de extração, novos localizadores de evidência e nova redação das afirmações sustentadas.
- Bibliometria refeita sobre os 57 estudos: 44 veículos, 23 países de afiliação, 23 estudos em computação e interação humano-computador e nenhum estudo de instituição brasileira.
- Figuras 1 e 2 refeitas: o diagrama de seleção incorpora as sete consultas da Web of Science e a figura 2 passou a apresentar, em dois painéis, a distribuição temporal dos 2.286 registros únicos e a distribuição por área do conhecimento dos 57 estudos.
- Protocolo atualizado para a versão 2.0, com o registro das emendas e o quadro de consultas renumerado.
- Planilha auditável regerada, com as abas de buscas, triagem, extração, fluxo e bibliometria conciliadas com os novos totais.
- Exportações brutas da Web of Science renumeradas de acordo com as sete consultas efetivas.

## 1.0.0 — 11 de novembro de 2026

Primeira versão pública do depósito.

- Protocolo v1.0, redigido e datado antes das buscas definitivas.
- Registro das consultas executadas em BRAPCI, OpenAlex, Google Acadêmico, rastreamento de citações e busca nominal dirigida, com expressões, filtros, datas e totais.
- 1.026 registros únicos após deduplicação e lista de candidatos avaliados.
- Matriz de extração com localizadores de página e uso de cada fonte.
- Planilha auditável com as abas de buscas, triagem, extração e fluxo.
- Figuras 1 e 2 em 300 dpi.
- Scripts de coleta, deduplicação, verificação de metadados, extração e geração das figuras.
- Lista de verificação PRISMA-ScR preenchida.
- Metadados verificados em Crossref e registro de downloads de textos completos.
