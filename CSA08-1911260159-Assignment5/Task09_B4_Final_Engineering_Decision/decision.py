import csv,sqlite3,time
from pathlib import Path
from tools import label,summarise
HERE=Path(__file__).parent
with open(HERE/"complaints.csv",encoding="utf-8") as f: rows=list(csv.DictReader(f))
correct=sum(label(r["text"])==r["human_label"] for r in rows)
print(f"Agreement: {correct}/{len(rows)} ({correct/len(rows)*100:.1f}%)")
with open(HERE/"sentiment_results.csv","w",newline="",encoding="utf-8") as f:
    wr=csv.writer(f); wr.writerow(["id","text","actual","predicted"])
    for r in rows: wr.writerow([r["id"],r["text"],r["human_label"],label(r["text"])])
print("Summary:",summarise(" ".join(r["text"]+"." for r in rows[:12])))
print("Example lexicon weakness: 'Great, another day of smoke' may be sarcastic but scores negative.")
db=sqlite3.connect(":memory:"); db.execute("CREATE TABLE readings(station,day,pm25)")
db.executemany("INSERT INTO readings VALUES(?,?,?)",((f"S{i%100}",f"2026-10-{i%28+1:02d}",i%150) for i in range(100000)))
query="SELECT AVG(pm25) FROM readings WHERE station=? AND day=?"; args=("S50","2026-10-15")
t=time.perf_counter()
for _ in range(80):db.execute(query,args).fetchone()
before=time.perf_counter()-t
db.execute("CREATE INDEX idx_station_day ON readings(station,day)"); db.commit()
t=time.perf_counter()
for _ in range(80):db.execute(query,args).fetchone()
after=time.perf_counter()-t
print(f"80 queries before index: {before:.6f}s; after index: {after:.6f}s")
db.close()
