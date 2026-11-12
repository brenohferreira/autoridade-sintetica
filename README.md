# Autoridade sintética na IA generativa e explicabilidade como direito

**Uma revisão de escopo com dados e materiais abertos**

Este repositório reúne o artigo, o protocolo, os dados e os scripts de uma revisão de escopo sobre a autoridade que os usuários atribuem à inteligência artificial generativa e sobre as condições em que a explicabilidade permite examinar e contestar suas respostas. O objetivo do depósito é permitir que qualquer pessoa refaça o percurso, verifique as decisões de triagem e reutilize a matriz de extração.

- **Versão:** 1.1.0 (12 de novembro de 2026)
- **Licença do texto e dos dados:** CC BY 4.0
- **Licença dos scripts:** MIT
- **Idioma:** português brasileiro

## O que está depositado

| Pasta | Conteúdo |
|---|---|
| `artigo/` | Artigo completo em DOCX e PDF, na versão ABNT integral e na versão de 15 páginas |
| `protocolo/` | Protocolo v1.0, redigido antes das buscas definitivas, em DOCX, PDF e Markdown |
| `dados/01_buscas/` | Expressões exatas, filtros, totais por consulta, registros brutos, rastreamento de citações e os 2.567 registros da Web of Science |
| `dados/02_triagem/` | Registros únicos após deduplicação, candidatos avaliados, triagem da Web of Science e estatísticas do corpus |
| `dados/03_extracao/` | Matriz de extração com 80 estudos, localizadores de página e uso de cada fonte |
| `dados/04_planilha/` | Planilha auditável com as abas de buscas, triagem, extração e fluxo |
| `figuras/` | Diagrama de seleção (PRISMA-ScR) e distribuição temporal, em 300 dpi |
| `scripts/` | Rotinas de coleta, deduplicação, triagem, verificação de metadados, extração e geração das figuras |
| `checklist/` | Lista de verificação PRISMA-ScR preenchida, item por item |
| `fontes/` | Metadados verificados em Crossref e registro dos downloads de textos completos |

## Números da revisão

Foram identificados 4.040 registros: 1.239 na OpenAlex (oito consultas), 2.567 na Web of Science Core Collection (oito consultas), 49 na BRAPCI (nove consultas), 80 no Google Acadêmico, 106 por rastreamento de citações e 19 por busca nominal dirigida. Após a remoção de 649 duplicatas, restaram 3.391 registros únicos; a triagem por título e resumo excluiu 3.311 registros, o que resultou em 80 estudos incluídos, publicados entre 1983 e 2026, dos quais 35 tiveram o texto completo examinado e 45 foram incorporados a partir do resumo. A expressão exata *synthetic authority* não retornou nenhum registro na Web of Science, o que sustenta a leitura de que o rótulo é incipiente.

## Autoria

**Breno Heleno Ferreira** é doutorando em Ciência da Informação pela Universidade Federal de Minas Gerais, mestre em Educação e Docência pela mesma instituição, com MBAs em Data Science e Analytics e em Gestão de Projetos pela USP. Contato: brenohferreira@ufmg.br. Currículo: http://lattes.cnpq.br/5720093855838869. GitHub: https://github.com/brenohferreira.

## Como citar

A citação do repositório está descrita no arquivo `CITATION.cff`. Enquanto o depósito não receber um identificador persistente, use:

> FERREIRA, Breno. **Autoridade sintética na IA generativa e explicabilidade como direito: uma revisão de escopo — dados e materiais**. Versão 1.1.0. 2026. Repositório GitHub. Disponível em: https://github.com/brenohferreira/autoridade-sintetica. Acesso em: [data].

## Reprodutibilidade

Os scripts foram escritos em Python 3.11 e dependem de `requests`, `beautifulsoup4`, `openpyxl`, `python-docx` e `matplotlib`.

```bash
pip install -r requirements.txt
python scripts/harvest.py        # coleta nas bases e registro das consultas
python scripts/triagem.py        # deduplicação e triagem de primeiro nível
python scripts/verificar.py      # conferência de metadados no Crossref
python scripts/gerar_xlsx.py     # planilha auditável
python scripts/figuras.py        # figuras 1 e 2
python scripts/gerar_docx.py     # artigo em ABNT
```

As consultas ao Google Acadêmico foram feitas por navegador e não podem ser reexecutadas por script, pois a plataforma bloqueia acesso automatizado; por isso, as expressões, as datas e os totais exibidos estão registrados em `dados/01_buscas/consultas.csv`, e os registros recuperados, em `dados/01_buscas/registros_brutos.csv`.

## Limitações declaradas

A busca na Web of Science foi executada em 12 de novembro de 2026, com acesso institucional, e a busca na Scopus não foi executada por exigir assinatura própria. A triagem foi feita por um revisor, com apoio de script na etapa de exclusão automática, sem dupla triagem independente, e 45 dos 80 estudos foram acessados apenas pelo resumo, hipótese registrada na coluna `acesso` da matriz de extração. O processo contou com apoio de um agente de inteligência artificial para coleta, deduplicação, conferência de metadados e geração das figuras; as decisões de elegibilidade e a redação permaneceram sob responsabilidade do autor.

## Licenças

O texto do artigo, o protocolo, as figuras e as tabelas de dados estão licenciados sob **Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)**, cujo texto integral está em `LICENSE`. Os scripts estão licenciados sob **MIT**, em `LICENSE-CODE`. O uso dos dados exige apenas a atribuição e a indicação de eventuais alterações.

## Como contribuir

Correções de metadados, identificação de páginas ausentes e sugestões de estudos não recuperados são bem-vindas pela aba *Issues*. Alterações aceitas são registradas em `CHANGELOG.md` e publicadas em nova versão.
