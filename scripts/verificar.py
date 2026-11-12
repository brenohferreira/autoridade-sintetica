import requests, json, time, sys

DOIS = {
 "hirvonen2025": "10.1002/asi.24942",
 "savolainen2021": "10.1515/libri-2020-0128",
 "rieh2002": "10.1002/asi.10017",
 "mckenzie2003": "10.1086/603418",
 "ferrario2024": "10.1007/s11023-024-09681-1",
 "milella2026": "10.3390/make8020036",
 "wachter2017": "10.1093/idpl/ipx009",
 "miller2019": "10.1016/j.artint.2018.07.007",
 "bansal2021": "10.1145/3411764.3445717",
 "bucinca2021": "10.1145/3449287",
 "vasconcelos2023": "10.1145/3579605",
 "goddard2012": "10.1136/amiajnl-2011-000089",
 "kasneci2023": "10.1016/j.lindif.2023.102274",
 "startari2025": "10.2139/ssrn.5258399",
 "palese2026": "10.3390/soc16030102",
 "shin2026": "10.1007/s00146-025-02560-y",
 "hauswald2025": "10.1080/02691728.2025.2449602",
 "keymolen2022": "10.1007/s10676-022-09671-w",
 "nannini2024": "10.1609/aies.v7i1.31700",
 "zawacki2019": "10.1186/s41239-019-0171-0",
 "perkins2023": "10.1007/s40979-023-00127-2",
 "cotton2024": "10.1080/14703297.2023.2190148",
 "bearman2023": "10.1007/s10734-022-00937-2",
 "selbst2018": "10.2139/ssrn.3126971",
 "lipton2018": "10.1145/3233231",
 "rudin2019": "10.1038/s42256-019-0048-x",
 "logg2019": "10.1016/j.obhdp.2019.01.002",
 "parasuraman1997": "10.1518/001872097778543886",
 "lee2004": "10.1518/hfes.46.1.50_30392",
 "skitka1999": "10.1006/ijhc.1999.0252",
 "dzindolet2003": "10.1016/S1071-5819(03)00038-7",
 "goldman2001": "10.1111/j.1933-1592.2001.tb00094.x",
 "hardwig1985": "10.2307/2026523",
 "hjorland2002": "10.1002/asi.10042",
 "fricker2007": "10.1093/acprof:oso/9780198237907.001.0001",
 "zagzebski2012": "10.1093/acprof:oso/9780199936472.001.0001",
 "flanagin2007": "10.1177/1461444807076972",
 "rieh2007": "10.1002/aris.2007.1440410114",
 "sundar2019": "10.1145/3290607.3299038",
 "mittelstadt2016": "10.1177/2053951716679679",
 "goodman2017": "10.1609/aimag.v38i3.2741",
 "holmes2022": "10.1007/s40593-021-00239-1",
 "akgun2022": "10.1007/s43681-021-00096-7",
 "williamson2020": "10.1080/17439884.2020.1694945",
 "gadzinski2026": "10.1007/s10676-026-09890-5",
}

if __name__ == "__main__":
    out = {}
    for k, doi in DOIS.items():
        try:
            r = requests.get(f"https://api.crossref.org/works/{doi}", timeout=40,
                             headers={"User-Agent": "scoping-review/1.0 (mailto:revisao@example.org)"})
            if r.status_code != 200:
                out[k] = {"doi": doi, "status": r.status_code}
                print(f"XX {k:16s} {doi} -> HTTP {r.status_code}")
                continue
            m = r.json()["message"]
            rec = {
                "doi": doi, "title": (m.get("title") or [""])[0],
                "authors": [f"{a.get('family','')}, {a.get('given','')}" for a in m.get("author", [])],
                "year": (m.get("issued", {}).get("date-parts", [[None]])[0][0]),
                "container": (m.get("container-title") or [""])[0],
                "volume": m.get("volume"), "issue": m.get("issue"), "page": m.get("page"),
                "publisher": m.get("publisher"), "type": m.get("type"),
                "article_number": m.get("article-number"),
            }
            out[k] = rec
            print(f"OK {k:16s} {rec['year']} | {rec['title'][:72]:72s} | {rec['container'][:34]:34s} | v{rec['volume']} n{rec['issue']} p{rec['page']} art{rec['article_number']}")
        except Exception as e:
            out[k] = {"doi": doi, "error": str(e)}
            print(f"ER {k} {doi} {e}")
        time.sleep(0.12)
    json.dump(out, open("/home/ubuntu/review/fontes/metadados_verificados.json", "w"), ensure_ascii=False, indent=1)
