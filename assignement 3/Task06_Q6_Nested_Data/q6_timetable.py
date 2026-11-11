import time
from collections import defaultdict
trains={
"12601":{"name":"Chennai Express","stops":[("Chennai","06:00","06:10"),("Katpadi","08:00","08:05"),("Bengaluru","11:00","11:10")],"days":{"Mon","Wed","Fri"}},
"12602":{"name":"Kaveri Express","stops":[("Chennai","07:00","07:15"),("Erode","12:00","12:05"),("Mysuru","15:00","15:10")},"days":{"Tue","Thu","Sat"}},
"12603":{"name":"Nilgiri Express","stops":[("Chennai","08:00","08:10"),("Salem","13:00","13:05"),("Coimbatore","16:00","16:10")},"days":{"Mon","Tue","Wed","Thu","Fri","Sat","Sun"}},
"12604":{"name":"West Coast","stops":[("Chennai","09:00","09:10"),("Erode","14:00","14:05"),("Mangaluru","18:00","18:10")},"days":{"Sun","Tue","Thu"}},
"12605":{"name":"Intercity","stops":[("Chennai","10:00","10:05"),("Katpadi","11:30","11:35"),("Vellore","12:00","12:05")},"days":{"Mon","Tue","Wed","Thu","Fri"}}}
def make_index(data):
    index=defaultdict(list)
    for no,d in data.items():
        for station,arr,dep in d["stops"]: index[station].append((no,arr,dep))
    return index
def main():
    print("Q6 Nested timetable"); index=make_index(trains); found=[]
    for no,d in trains.items():
        if "Tue" in d["days"]:
            for s,a,b in d["stops"]:
                if s=="Erode": found.append((b,no,d["name"]))
    for row in sorted(found,key=lambda x:x[0]): print(row)
    print("Unknown station:",index.get("Unknown",[]))
    print("Third stop departure:",trains["12601"]["stops"][2][2])
    for n in (100,1000,10000):
        data={str(i):{"name":"Train"+str(i),"stops":[(f"Station{j%100}","08:00","08:05") for j in range(10)],"days":{"Mon"}} for i in range(n)}
        t=time.perf_counter(); scan=[no for no,d in data.items() for s,a,b in d["stops"] if s=="Station25"]; x=time.perf_counter()-t
        t=time.perf_counter(); idx=make_index(data); y=time.perf_counter()-t
        print(f"trains={n}: scan={x:.5f}s index-build={y:.5f}s matches={len(idx['Station25'])}")
if __name__=="__main__": main()
