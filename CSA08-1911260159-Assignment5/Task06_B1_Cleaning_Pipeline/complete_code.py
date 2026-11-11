import csv, io
RAW = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-02,NA
Adyar,2026-10-03,
Guindy,2026-10-01,95
Guindy,2026-10-02,-5
Guindy,2026-10-03,121
Guindy,2026-10-04,1200
"""
def load_clean(text):
    rows=[]
    for row in csv.DictReader(io.StringIO(text)):
        raw=(row.get("pm25") or "").strip()
        if raw.upper() in ("","NA"): continue
        try: value=float(raw)
        except ValueError: continue
        if value < 0 or value > 999: continue
        rows.append((row["station"].strip(),row["date"].strip(),value))
    return rows
def min_max(values):
    if not values: return []
    low,high=min(values),max(values)
    if low==high: return [0.0 for _ in values]
    return [round((v-low)/(high-low),3) for v in values]
clean=load_clean(RAW)
print(clean)
print(min_max([pm for _,_,pm in clean]))
