import re, sys, os

def pages(path):
    txt = open(path, encoding="utf-8", errors="ignore").read()
    return txt.split("\f")

def find(path, pattern, maxhits=6, width=420):
    ps = pages(path)
    n = 0
    for i, p in enumerate(ps, 1):
        p = re.sub(r"\s+", " ", p)
        for m in re.finditer(pattern, p, re.I):
            s = max(0, m.start() - width // 3)
            e = min(len(p), m.end() + width)
            frag = re.sub(r"\s+", " ", p[s:e])
            print(f"[{os.path.basename(path)}] p.{i}: ...{frag}...\n")
            n += 1
            if n >= maxhits: return
    if n == 0: print(f"[{os.path.basename(path)}] NENHUM achado para {pattern}")

if __name__ == "__main__":
    path = sys.argv[1]; pat = sys.argv[2]
    mx = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    find(path, pat, mx)
