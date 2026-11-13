# Exportações originais da Web of Science

Esta pasta guarda os arquivos como saíram da Web of Science Core Collection, em 12 de novembro de 2026, com acesso institucional, sem qualquer edição de conteúdo. Cada arquivo corresponde a uma das consultas do protocolo e recebeu um nome que indica o assunto pesquisado; a expressão exata de cada uma está em `../wos_consultas.md`.

| Arquivo | Registros | Consulta |
|---|---|---|
| `W01_autoridade_cognitiva.txt` | 175 | `TS=("cognitive authority")` |
| `W01b_autoridade_cognitiva_complemento.txt` | parte final de W01 | continuação da exportação anterior, dividida pelo limite da plataforma |
| `W02_autoridade_epistemica_ia.txt` | 141 | autoridade epistêmica combinada com inteligência artificial |
| `W04_ia_generativa_llm.txt` | 742 | IA generativa, modelos de linguagem e autoridade |
| `W05_direito_a_explicacao.txt` | 31 | direito à explicação e explicabilidade |
| `W06_vies_de_automacao.txt` | 245 | viés de automação e confiança excessiva |
| `W07_heuristica_da_maquina.txt` | 73 | heurística da máquina |

## Formato

Os arquivos seguem o formato de exportação em texto da Clarivate, com campos de duas letras no início de cada linha (`PT`, `AU`, `TI`, `SO`, `PY`, `DI`, `AB`, `ER`) e registros separados por `ER`. A leitura pode ser feita com qualquer parser de texto delimitado; o script `scripts/wos_ingest.py` do diretório de trabalho original foi o responsável pela conversão.

## Conversão para JSON

`registros_parseados.json` reúne os 1.407 registros das sete consultas já convertidos, com os campos normalizados usados na deduplicação (título, autores, periódico, ano, DOI e identificador da Web of Science). Os registros que não apareceram nas demais bases estão em `../wos_registros_novos.csv`, e o resultado da triagem, em `../../02_triagem/wos_triagem.csv`.
