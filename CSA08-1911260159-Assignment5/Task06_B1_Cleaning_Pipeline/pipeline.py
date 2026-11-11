import csv, sqlite3, statistics
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE=Path(__file__).parent; OUT=HERE/"output"; OUT.mkdir(exist_ok=True)
def clean_file(path):
    with open(path,encoding="utf-8",newline="") as f:
        reader=csv.DictReader(f)
        needed={"station","date","hour","pm25","pm10","no2","temperature"}
        if not reader.fieldnames or not needed.issubset(reader.fieldnames): raise ValueError("Missing CSV columns")
        source=list(reader)
    good=[]; rejected=[]; seen=set()
    for line,row in enumerate(source,2):
        try:
            station=row["station"].strip().title(); day=row["date"].strip(); hour=int(row["hour"])
            if not station or not day or not 0<=hour<=23: raise ValueError("invalid station/date/hour")
            vals={}
            for col in ("pm25","pm10","no2"):
                raw=(row[col] or "").strip()
                if raw.upper() in ("","NA","N/A"): vals[col]=None
                else:
                    x=float(raw)
                    if x<0 or x>999: raise ValueError(col+" outside range")
                    vals[col]=x
            temp=float(row["temperature"])
            if temp>=70: temp=(temp-32)*5/9
            key=(station,day,hour)
            if key in seen: rejected.append((line,"duplicate")); continue
            seen.add(key)
            good.append(dict(station=station,date=day,hour=hour,**vals,temperature_c=temp))
        except (ValueError,TypeError,KeyError) as e: rejected.append((line,str(e)))
    for col in ("pm25","pm10","no2"):
        med={}
        for r in good:
            if r[col] is not None: med.setdefault(r["station"],[]).append(r[col])
        med={s:statistics.median(v) for s,v in med.items()}
        for r in good:
            if r[col] is None and r["station"] in med: r[col]=med[r["station"]]
    return source,good,rejected
def store(rows):
    db=sqlite3.connect(OUT/"air_quality.db")
    db.executescript("""CREATE TABLE IF NOT EXISTS stations(id INTEGER PRIMARY KEY,name TEXT UNIQUE);
    CREATE TABLE IF NOT EXISTS readings(station_id INTEGER,day TEXT,hour INTEGER,pm25 REAL,pm10 REAL,no2 REAL,temp_c REAL,
    UNIQUE(station_id,day,hour),FOREIGN KEY(station_id) REFERENCES stations(id));""")
    for s in sorted({r["station"] for r in rows}): db.execute("INSERT OR IGNORE INTO stations(name) VALUES(?)",(s,))
    ids=dict(db.execute("SELECT name,id FROM stations"))
    db.executemany("INSERT OR REPLACE INTO readings VALUES(?,?,?,?,?,?,?)",
      [(ids[r["station"]],r["date"],r["hour"],r["pm25"],r["pm10"],r["no2"],r["temperature_c"]) for r in rows])
    db.commit()
    q1=db.execute("SELECT AVG(pm25) FROM readings JOIN stations ON id=station_id WHERE name=? AND day BETWEEN ? AND ?",("Adyar","2026-10-01","2026-10-31")).fetchone()[0]
    q2=db.execute("SELECT name,day,AVG(pm25) FROM readings JOIN stations ON id=station_id GROUP BY name,day").fetchall()
    q3=db.execute("SELECT name,day,hour,pm25 FROM readings JOIN stations ON id=station_id ORDER BY pm25 DESC LIMIT 5").fetchall()
    daily=db.execute("SELECT name,day,MIN(pm25),MAX(pm25),AVG(pm25),COUNT(pm25) FROM readings JOIN stations ON id=station_id GROUP BY name,day").fetchall()
    db.close(); return q1,q2,q3,daily
def charts(rows):
    valid=[r for r in rows if r["pm25"] is not None]
    if not valid:return
    plt.figure(); plt.plot([r["hour"] for r in valid],[r["pm25"] for r in valid],"o-"); plt.title("PM2.5 trend"); plt.xlabel("Hour"); plt.ylabel("PM2.5"); plt.savefig(OUT/"trend.png"); plt.close()
    names=sorted({r["station"] for r in valid}); means=[statistics.mean([r["pm25"] for r in valid if r["station"]==s]) for s in names]
    plt.figure(); plt.bar(names,means); plt.title("Station comparison"); plt.xlabel("Station"); plt.ylabel("Mean PM2.5"); plt.savefig(OUT/"stations.png"); plt.close()
    plt.figure(); plt.scatter([r["temperature_c"] for r in valid],[r["pm25"] for r in valid]); plt.title("Temperature vs PM2.5"); plt.xlabel("Temperature C"); plt.ylabel("PM2.5"); plt.savefig(OUT/"temperature.png"); plt.close()
    hours=sorted({r["hour"] for r in valid})
    plt.figure(); plt.bar([str(h) for h in hours],[statistics.mean([r["pm25"] for r in valid if r["hour"]==h]) for h in hours]); plt.title("PM2.5 by hour"); plt.xlabel("Hour"); plt.ylabel("Mean PM2.5"); plt.savefig(OUT/"hours.png"); plt.close()
if __name__=="__main__":
    raw,rows,bad=clean_file(HERE/"input"/"raw.csv")
    print("Raw rows:",len(raw),"Clean rows:",len(rows),"Rejected:",bad)
    print("Cleaned:",rows)
    print("SQL results:",store(rows))
    charts(rows)
