import csv,io,sqlite3
from pathlib import Path
from sentiment import label
for name,text in {"missing_column":"station,date\nAdyar,2026-10-01","wrong_delimiter":"station;date;pm25\nAdyar;2026-10-01;40","empty":""}.items():
    reader=csv.DictReader(io.StringIO(text))
    if not reader.fieldnames or not {"station","date","pm25"}.issubset(reader.fieldnames): print(name,"rejected: missing required columns")
p=Path("bad_encoding.csv"); p.write_bytes(b"station,date,pm25\nAdyar,\xff,50")
try:p.read_text(encoding="utf-8")
except UnicodeDecodeError as e:print("encoding handled:",type(e).__name__)
finally:p.unlink(missing_ok=True)
db=sqlite3.connect(":memory:"); db.execute("CREATE TABLE aq(station TEXT,pm25 REAL)")
db.executemany("INSERT INTO aq VALUES(?,?)",[("Adyar",48),("Guindy",95)])
attack="Adyar' OR '1'='1"
unsafe="SELECT * FROM aq WHERE station='"+attack+"'"
print("unsafe rows:",db.execute(unsafe).fetchall())
print("safe rows:",db.execute("SELECT * FROM aq WHERE station=?",(attack,)).fetchall())
for s in ["Great, another day of smoke.","This is not not good.","The air is clean but service is rude."]:print(label(s),s)
