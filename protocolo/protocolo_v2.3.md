# EMENDA 2.3 AO PROTOCOLO DE REVISÃO DE ESCOPO: COLETA MANUAL NO PORTAL DE PERIÓDICOS DA CAPES E REGRA LEXICAL DE INCORPORAÇÃO

Breno Heleno Ferreira

Belo Horizonte, 20 de novembro de 2026

1 MOTIVO E ALCANCE DA EMENDA

Esta emenda registra a terceira alteração do protocolo da revisão de escopo sobre autoridade sintética, autoridade cognitiva, autoridade epistêmica e explicabilidade, e responde a duas circunstâncias que a versão 2.2 havia deixado em aberto. A primeira é operacional, porque a busca integrada do Portal de Periódicos da CAPES interrompia a consulta sempre que a expressão combinava mais de um operador booleano, o que havia permitido recuperar apenas sessenta registros de três expressões simples e impedido a execução das demais. A segunda é metodológica, porque a decisão sobre incorporar ou não os registros recuperados na coleta manual exigia um critério declarado antes da leitura, e não uma escolha posterior orientada pelo que os resumos pareciam prometer. O alcance da emenda é, portanto, duplo: substitui a coleta frustrada por uma coleta manual integral e fixa, para a incorporação, uma regra lexical auditável, aplicada de modo uniforme a todos os candidatos novos.

2 PROCEDIMENTO DE COLETA MANUAL

A coleta foi executada em 20 de novembro de 2026 na interface de busca avançada do Portal, autenticada pelo acesso remoto da Universidade Federal de Minas Gerais, com a opção Escopo da Busca, o campo Contém e o conector AND em cada linha de filtro, restrição a artigos no Tipo de Material e o filtro de acesso aberto desmarcado, para não excluir registros de revistas assinadas que não oferecem versão aberta. Cada consulta foi registrada com código, expressão exata, data, total exibido e número de registros exportados, e a exportação foi feita em arquivo RIS, formato que preserva autores, ano, veículo, identificador digital e resumo. Como o Portal limita a exportação a cem registros por operação, as consultas com mais resultados exigiram paginação e foram exportadas em lotes sucessivos, o que produziu dezoito arquivos, entre eles o reenvio de uma consulta que havia falhado. Dois arquivos, com cem e 26 registros, foram exportados antes da consulta C5a e não puderam ser atribuídos a uma expressão específica, e essa circunstância é registrada aqui em vez de suprimida, porque o conjunto permanece identificável pelo conteúdo e auditável pelo arquivo de origem.


**Quadro 1 - Consultas executadas no Portal de Periódicos da CAPES em 20 de novembro de 2026**


**Fonte: Elaboração própria (2026).**

3 CONSOLIDAÇÃO E TRIAGEM

A consolidação reuniu 1.146 registros exportados, dos quais 284 eram duplicatas internas ao próprio Portal, 514 já constavam do corpus reunido nas fases anteriores e 348 permaneceram como candidatos novos. A triagem dos candidatos foi feita em três passos sucessivos e independentes, todos registrados em arquivo, com o mesmo desenho de dois revisores automáticos que a versão 2.2 havia adotado para as bases novas. O primeiro passo avaliou a pertinência temática de cada candidato ao escopo da revisão e aprovou 135 dos 348; o segundo atribuiu nota de centralidade de zero a três, com 96 registros na nota máxima, 28 na nota dois, nove na nota um e dois na nota zero; o terceiro decidiu a inclusão entre os 124 que haviam alcançado nota maior ou igual a dois, e aprovou 69. Os resumos foram recuperados por identificador digital na OpenAlex, o que permitiu avaliar 312 dos 348 candidatos com texto de resumo disponível, e as decisões limítrofes foram conferidas manualmente.

4 REGRA LEXICAL DE INCORPORAÇÃO

A leitura dos 69 aprovados mostrou concentração de estudos sobre autoridade religiosa digital, com fatwas, hádices, tafsir e autoridade interpretativa em comunidades muçulmanas, e sobre autoridade judicial e direito à explicação, o que ampliaria o corpus em direção distinta da pergunta desta revisão, voltada à autoridade atribuída a sistemas de informação e de inteligência artificial. Em vez de decidir caso a caso, o que reintroduziria o juízo ad hoc que a emenda pretendia evitar, fixou-se uma regra lexical declarada antes da seleção e aplicável a todos os aprovados, com três condições cumulativas: a presença de termo de inteligência artificial no título ou no resumo, a densidade de pelo menos três termos de autoridade no conjunto formado por título e resumo e o tamanho do resumo igual ou superior a 500 caracteres, condição que preserva a possibilidade de avaliar o argumento e não apenas o rótulo. Aplicada aos 69 aprovados, a regra reteve 38 registros, dos quais se incorporaram vinte, escolhidos pela ordem de prioridade que a própria regra estabelece, isto é, pela presença de termos de explicabilidade e contestação, pela densidade de termos de autoridade e pela nota de centralidade, com desempate pelo ano de publicação. A lista dos 38 elegíveis, com as três métricas de cada registro, está depositada no repositório, de modo que a retenção dos vinte possa ser refeita e contestada.


**Quadro 2 - Estudos retidos pela regra lexical e incorporados ao corpus**


**Fonte: Elaboração própria (2026). Dens. = densidade de termos de autoridade; Expl. = termos de explicabilidade e contestação no título e no resumo.**

5 EFEITOS SOBRE O FLUXO DE SELEÇÃO

Com a incorporação dos vinte estudos, o conjunto identificado passa de 6.745 para 7.831 registros, porque os sessenta registros recuperados na tentativa anterior foram substituídos pelos 1.146 da coleta manual; as duplicatas passam de 916 para 1.654; os registros únicos, de 5.829 para 6.177; os registros lidos por título e resumo, de 1.281 para 1.629; e os estudos incluídos, de 105 para 125. Permanecem inalterados os 1.303 registros excluídos na etapa automática e os 3.245 que ficaram abaixo do corte de leitura, de modo que o total de não incluídos passa a 6.052 registros, e a principal restrição de recall da revisão continua sendo a leitura parcial do conjunto ordenado por pertinência.

6 PENDÊNCIAS REGISTRADAS

Três pendências ficam registradas para a próxima versão do protocolo, e nenhuma delas altera os resultados desta emenda. A primeira é a atribuição dos dois arquivos exportados antes da consulta C5a, com cem e 26 registros, que permanecem identificados pelo conteúdo mas sem consulta de origem. A segunda é o total declarado da consulta C4b, que exibiu cem registros e pode ter segunda página não exportada, circunstância que a coleta manual não permitiu confirmar. A terceira é a execução futura das expressões da LISA, preservadas no protocolo desde a versão 2.2, porque a base não integra a assinatura institucional disponível.

7 DISPONIBILIDADE

Os arquivos RIS, a planilha de registro das consultas, o consolidado com a situação de cada registro, os candidatos com resumo, os três arquivos de triagem, a lista dos 38 elegíveis e o script que aplica a regra lexical estão depositados no repositório público da revisão, sob licença CC BY 4.0 para os dados e MIT para os scripts, com versão identificada no momento do depósito. Esta emenda integra o protocolo na versão 2.3, de 20 de novembro de 2026, e substitui, quanto à coleta no Portal de Periódicos da CAPES, o registro correspondente da versão 2.2.
