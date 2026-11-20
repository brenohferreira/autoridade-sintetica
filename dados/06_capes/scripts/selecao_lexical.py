#!/usr/bin/env python3
"""Aplica a regra lexical auditavel aos 124 registros da decisao final (CAPES).

Regra aprovada pelo autor (opcao do meio):
  R1) termo de IA no titulo ou no resumo;
  R2) densidade de termos de autoridade >= 3 ocorrencias no conjunto titulo+resumo;
  R3) resumo com pelo menos 500 caracteres.
Priorizacao: eixo de explicabilidade e contestacao; desempate por nota e ano.
Saidas: selecao_capes.csv (todos os 124 com as metricas) e selecao_final.csv (retidos).
"""
import csv, json, re, unicodedata

BASE = "/home/ubuntu/review/emenda/novas_bases/capes_manual"

TERMOS_IA = [
    "artificial intelligence", "inteligencia artificial", "inteligência artificial",
    "machine learning", "aprendizado de maquina", "aprendizagem de maquina",
    "large language model", "modelo de linguagem", "llm", "chatgpt", "gpt",
    "algorithm", "algoritmo", "automated decision", "decisao automatizada",
    "decisão automatizada", "expert system", "sistema especialista", "robot",
    "robô", "robotic", "neural network", "rede neural", "generative ai",
    "ia generativa", "intelligent system", "sistema inteligente", "bot",
]

TERMOS_AUTORIDADE = [
    "authority", "autoridade", "authoritative", "autoritativo", "autorizacao",
    "autorização", "legitimacy", "legitimidade", "legitimar", "credibilidade",
    "credibility", "confianca", "confiança", "trust", "deference", "deferencia",
    "deferência", "hierarchy", "hierarquia", "jurisdiction", "jurisdicao",
    "jurisdição", "soberania", "sovereignty", "poder", "power", "command",
    "comando", "obediencia", "obediência", "obedience", "normatividade",
    "normativity", "validade", "validity", "reconhecimento", "recognition",
    "expertise", "perito", "expert", "especialista", "magisterio", "magistério",
    "teaching authority", "autoridade docente", "magisterium", "fatwa", "hadith",
    "hadice", "hádice", "tafsir", "sharia", "shari'a", "fiqh", "ulema", "ulama",
    "caliphate", "califado", "imam", "imame", "pontificio", "pontifício",
    "episcopal", "conciliar", "concílio", "concilio", "cânon", "canon",
    "interpretacao autentica", "interpretação autêntica", "autenticidade",
    "authenticity", "delegacao", "delegação", "delegation", "mandato", "mandate",
    "arbitrio", "arbítrio", "discretion", "discricionariedade", "pericia",
    "perícia", "technocracy", "tecnocracia", "governanca", "governança",
    "governance", "accountability", "responsabilizacao", "responsabilização",
]

TERMOS_EXPLICABILIDADE = [
    "explainab", "explicab", "explanation", "explicacao", "explicação",
    "transparen", "transparên", "contestab", "contestacao", "contestação",
    "accountab", "interpretab", "interpretabilidade", "justific", "justifica",
    "auditab", "auditoria", "audit", "rastreab", "rastreabilidade",
    "traceab", "revisab", "revisabilidade", "recurso", "appeal", "remedy",
    "due process", "devido processo", "supervisao humana", "supervisão humana",
    "human oversight", "human in the loop", "opacidade", "opacity", "caixa preta",
    "black box", "responsabil", "prestacao de contas", "prestação de contas",
]


def norm(s):
    s = unicodedata.normalize("NFKD", (s or "").lower())
    return "".join(c for c in s if not unicodedata.combining(c))


def contar(texto, termos):
    t = norm(texto)
    n = 0
    for termo in termos:
        base = norm(termo)
        if not base:
            continue
        n += len(re.findall(r"\b" + re.escape(base), t))
    return n


def main():
    recs = [json.loads(l) for l in open(f"{BASE}/triagem_capes_3.jsonl")]
    linhas = []
    for r in recs:
        titulo = r.get("title") or ""
        resumo = r.get("abstract") or ""
        texto = titulo + " " + resumo
        ia = contar(texto, TERMOS_IA) > 0
        dens = contar(texto, TERMOS_AUTORIDADE)
        explic = contar(texto, TERMOS_EXPLICABILIDADE)
        longo = len(resumo) >= 500
        aprovado = r.get("decisao") == 1
        atende = aprovado and ia and dens >= 3 and longo
        # pontuacao de prioridade: explicabilidade/contestacao, densidade e nota
        score = (4 if explic >= 2 else 3 if explic == 1 else 0) + min(dens, 8) + 2 * int(r.get("nota") or 0)
        linhas.append({
            "id": r.get("id"), "ano": r.get("year"), "titulo": titulo,
            "veiculo": r.get("venue"), "doi": r.get("doi"),
            "eixo": r.get("eixo"), "nota": r.get("nota"), "decisao": r.get("decisao"),
            "termo_ia": "sim" if ia else "nao",
            "densidade_autoridade": dens,
            "termos_explicabilidade": explic,
            "tam_resumo": len(resumo),
            "atende_regra": "sim" if atende else "nao",
            "score": score,
            "resumo": resumo,
        })
    linhas.sort(key=lambda d: (d["atende_regra"] == "sim", d["score"], d["ano"] or 0), reverse=True)
    with open(f"{BASE}/selecao_capes.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[k for k in linhas[0] if k != "resumo"])
        w.writeheader()
        for l in linhas:
            w.writerow({k: v for k, v in l.items() if k != "resumo"})
    eleg = [l for l in linhas if l["atende_regra"] == "sim"]
    print("registros", len(linhas), "aprovados na decisao", sum(1 for l in linhas if l["decisao"] == 1))
    print("atendem a regra lexical", len(eleg))
    print("top20:")
    for l in eleg[:20]:
        print(f'{l["score"]:>3} {l["ano"]} d={l["densidade_autoridade"]} e={l["termos_explicabilidade"]} n={l["nota"]} | {l["titulo"][:95]}')
    with open(f"{BASE}/selecao_final.json", "w") as f:
        json.dump(eleg, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
