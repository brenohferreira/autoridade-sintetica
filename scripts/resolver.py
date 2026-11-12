import requests, json, sys, time, os

BASE = "/home/ubuntu/review/fontes"
os.makedirs(BASE, exist_ok=True)

def find(title, year=None):
    p = {"search": title, "per_page": 5, "mailto": "revisao@example.org"}
    if year: p["filter"] = f"publication_year:{year}"
    d = requests.get("https://api.openalex.org/works", params=p, timeout=90).json()
    out = []
    for w in d.get("results", []):
        src = ((w.get("primary_location") or {}).get("source") or {})
        b = w.get("best_oa_location") or {}
        out.append({
            "title": w.get("title"), "year": w.get("publication_year"),
            "venue": src.get("display_name"), "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
            "authors": [a["author"]["display_name"] for a in w.get("authorships", [])[:6]],
            "oa_pdf": b.get("pdf_url"), "oa_url": b.get("landing_page_url"),
            "cited": w.get("cited_by_count"), "id": w["id"].split("/")[-1],
        })
    return out

if __name__ == "__main__":
    items = json.load(open(sys.argv[1]))
    res = {}
    for key, q, yr in items:
        try:
            cand = find(q, yr)
        except Exception as e:
            cand = [{"error": str(e)}]
        res[key] = cand
        print("\n##", key, "|", q, "|", yr)
        for c in cand[:3]:
            print("   ", c.get("year"), "|", (c.get("title") or "")[:90], "|", c.get("venue"), "|", c.get("doi"), "| pdf:", bool(c.get("oa_pdf")))
        time.sleep(0.15)
    json.dump(res, open("/home/ubuntu/review/fontes/resolvidos.json", "w"), ensure_ascii=False, indent=1)
