from __future__ import annotations
import csv, json, random
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def project_hyperedges(nodes, hyperedges):
    adj={str(n):set() for n in nodes}
    for edge in hyperedges:
        ns=list(dict.fromkeys(map(str,edge)))
        for i,u in enumerate(ns):
            for v in ns[i+1:]: adj[u].add(v); adj[v].add(u)
    return adj
def global_efficiency(nodes, adj, removed=frozenset()):
    avail=[str(x) for x in nodes if str(x) not in removed]; n=len(avail)
    if n<2:return 0.0
    total=pairs=0
    for i,src in enumerate(avail):
        dist={src:0}; q=[src]
        for u in q:
            for v in adj.get(u,()):
                if v not in removed and v not in dist: dist[v]=dist[u]+1; q.append(v)
        for dst in avail[i+1:]:
            pairs+=1; d=dist.get(dst); total += 0 if not d else 1/d
    return total/pairs
def load_curve():
    with (ROOT/'data/derived/primary_results.csv').open() as f:return list(csv.DictReader(f))
def load_summary():return json.loads((ROOT/'results/empirical_summary.json').read_text())
def validate_bundle():
    rows=load_curve(); return len(rows)==5 and all(float(r['targeted_retained_efficiency'])<float(r['random_mean']) for r in rows)
