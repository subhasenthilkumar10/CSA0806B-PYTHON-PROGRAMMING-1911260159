import random, time
def naive(a,w=7): return [sum(a[i:i+w])/w for i in range(len(a)-w+1)] if len(a)>=w else []
def running(a,w=7):
    if len(a)<w: return []
    total=sum(a[:w]); out=[total/w]
    for i in range(w,len(a)):
        total += a[i]-a[i-w]; out.append(total/w)
    return out
def main():
    random.seed(10); r=[round(random.uniform(0,30),1) for _ in range(365)]
    weeks=[sum(r[i:i+7]) for i in range(0,len(r),7)]
    print("Q1 Rainfall"); print("Weekly totals:",weeks[:5])
    print("Wettest week:",max(range(len(weeks)),key=weeks.__getitem__)+1)
    print("Driest week:",min(range(len(weeks)),key=weeks.__getitem__)+1)
    print("Moving average count:",len(running(r)))
    print("Dry days:",[i+1 for i,x in enumerate(r) if x==0])
    print("Slice [7:14]:",r[7:14]); print("Last 7:",r[-7:]); print("Every 7th:",r[::7][:5])
    for n in (365,36500,365000):
        a=[random.random()*30 for _ in range(n)]
        t=time.perf_counter(); naive(a); x=time.perf_counter()-t
        t=time.perf_counter(); running(a); y=time.perf_counter()-t
        print(f"n={n}: naive={x:.5f}s running={y:.5f}s")
    print("Empty:",running([]),"Short:",running([1,2,3]))
if __name__=="__main__": main()
