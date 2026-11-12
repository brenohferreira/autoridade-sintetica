import requests, os, json, subprocess, time

OUT = "/home/ubuntu/review/fontes/pdf"
os.makedirs(OUT, exist_ok=True)
H = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}

DOIS = {
 "rieh2002": "10.1002/asi.10017",
 "hirvonen2025": "10.1002/asi.24942",
 "savolainen2021": "10.1515/libri-2020-0128",
 "mckenzie2003": "10.1086/603418",
 "ferrario2024": "10.1007/s11023-024-09681-1",
 "milella2026": "10.3390/make8020036",
 "wachter2017": "10.1093/idpl/ipx005",
 "miller2019": "10.1016/j.artint.2018.07.007",
 "bansal2021": "10.1145/3411764.3445717",
 "bucinca2021": "10.1145/3449287",
 "vasconcelos2023": "10.1145/3579605",
 "goddard2012": "10.1136/amiajnl-2011-000089",
 "kasneci2023": "10.1016/j.lindif.2023.102274",
 "safarov2025": "10.1177/00187208251401773",
 "palese2026": "10.3390/soc16030102",
 "ozer2026": "10.55982/openpraxis.18.3.1149",
 "hauswald2025": "10.1080/02691728.2025.2449602",
 "nannini2024": "10.1609/aies.v7i1.31700",
 "zawacki2019": "10.1186/s41239-019-0171-0",
 "cotton2024": "10.1080/14703297.2023.2190148",
 "bearman2023": "10.1007/s10734-022-00937-2",
 "rudin2019": "10.1038/s42256-019-0048-x",
 "lipton2018": "10.1145/3233231",
 "selbst2018": "10.2139/ssrn.3126971",
 "startari2025": "10.2139/ssrn.5258399",
 "sun2025": "10.1108/jkm-02-2025-0252",
 "shin2026": "10.1007/s00146-025-02560-y",
 "perkins2023": "10.53761/1.20.02.07",
 "cooper2024": "10.4324/9781003440178-7",
 "jongepier2022": "10.1007/s10676-022-09654-x",
}

def oa(doi):
    try:
        r = requests.get(f"https://api.openalex.org/works/https://doi.org/{doi}",
                         params={"mailto": "revisao@example.org"}, timeout=60)
        if r.status_code != 200: return None, None
        w = r.json()
        b = w.get("best_oa_location") or {}
        urls = [b.get("pdf_url"), b.get("landing_page_url")]
        for loc in w.get("locations", []):
            urls.append(loc.get("pdf_url"))
        return [u for u in urls if u], w
    except Exception as e:
        return None, None

log = {}
for k, doi in DOIS.items():
    urls, w = oa(doi)
    if not urls:
        log[k] = {"doi": doi, "status": "sem_localizacao_OA"}
        print(f"-- {k}: sem OA"); continue
    ok = False
    for u in urls[:4]:
        try:
            r = requests.get(u, headers=H, timeout=90, allow_redirects=True)
            if r.status_code == 200 and r.content[:4] == b"%PDF":
                p = f"{OUT}/{k}.pdf"
                open(p, "wb").write(r.content)
                subprocess.run(["pdftotext", "-layout", p, f"{OUT}/{k}.txt"], check=False)
                n = 0
                try:
                    n = int(subprocess.run(["pdfinfo", p], capture_output=True, text=True).stdout.split("Pages:")[1].split()[0])
                except Exception: pass
                log[k] = {"doi": doi, "status": "ok", "url": u, "pages": n}
                print(f"OK {k}: {n} pág. <- {u[:90]}")
                ok = True; break
        except Exception as e:
            continue
    if not ok:
        log[k] = {"doi": doi, "status": "pdf_indisponivel", "tentativas": urls[:4]}
        print(f"-- {k}: PDF indisponível ({urls[0][:80] if urls else ''})")
    time.sleep(0.3)

json.dump(log, open("/home/ubuntu/review/fontes/download_log.json", "w"), ensure_ascii=False, indent=1)
print("\nresumo:", sum(1 for v in log.values() if v["status"] == "ok"), "de", len(DOIS))
