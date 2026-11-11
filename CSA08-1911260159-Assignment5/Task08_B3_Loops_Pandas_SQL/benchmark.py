import csv,sqlite3,time,cProfile,pstats,io,random
from pathlib import Path
try: import pandas as pd
except ImportError: pd=None
OUT=Path("output"); OUT.mkdir(exist_ok=True)
def generate(stations):
    path=OUT/f"data_{stations}.csv"; rng=random.Random(7)
    with open(path,"w",newline="",encoding="utf-8") as f:
        wr=csv.writer(f); wr.writerow(["station","date","pm25"])
        for s in range(stations):
            for day in range(365):
                date=f"2025-{day//30+1:02d}-{day%30+1:02d}"
                for hour in range(24): wr.writerow([f"S{s:03d}",date,round(rng.uniform(5,150),2)])
    return path
def python_group(path):
    totals={}
    with open(path,encoding="utf-8") as f:
        for r in csv.DictReader(f):
            k=(r["station"],r["date"]); total,count=totals.get(k,(0.0,0))
            totals[k]=(total+float(r["pm25"]),count+1)
    return {k:v/c for k,(v,c) in totals.items()}
def pandas_group(path):
    return pd.read_csv(path).groupby(["station","date"])["pm25"].mean()
def sql_group(path):
    db=sqlite3.connect(":memory:"); db.execute("CREATE TABLE r(station,day,pm25)")
    with open(path,encoding="utf-8") as f:
        db.executemany("INSERT INTO r VALUES(?,?,?)",((r["station"],r["date"],float(r["pm25"])) for r in csv.DictReader(f)))
    out=db.execute("SELECT station,day,AVG(pm25) FROM r GROUP BY station,day").fetchall(); db.close()
    return {(a,b):c for a,b,c in out}
if __name__=="__main__":
    for n in (1,12,120):
        path=generate(n); t=time.perf_counter(); a=python_group(path); py=time.perf_counter()-t
        if pd is not None:
            t=time.perf_counter(); b=pandas_group(path); pt=time.perf_counter()-t
            key=next(iter(a)); assert abs(a[key]-b.loc[key])<1e-8
        else: pt="pandas not installed"
        t=time.perf_counter(); c=sql_group(path); st=time.perf_counter()-t
        key=next(iter(a)); assert abs(a[key]-c[key])<1e-8
        print(n,"stations",n*8760,"rows","python",round(py,3),"pandas",pt,"SQL+load",round(st,3),"groups",len(a))
    prof=cProfile.Profile(); prof.enable(); python_group(generate(1)); prof.disable()
    stream=io.StringIO(); pstats.Stats(prof,stream=stream).sort_stats("cumulative").print_stats(10)
    (OUT/"profile.txt").write_text(stream.getvalue()); print(stream.getvalue())
