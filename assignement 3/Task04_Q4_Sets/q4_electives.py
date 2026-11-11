import time
ai={"192311001","192311004","192311007","192311009"}
iot={"192311002","192311004","192311009","192311010"}
all_students={f"1923110{i:02d}" for i in range(1,11)}
def main():
    print("Q4 Sets")
    both=ai & iot
    one=ai^iot; neither=all_students-(ai|iot)
    print("clash:",sorted(both)); print("exactly one:",sorted(one)); print("neither:",sorted(neither))
    print("Methods agree:",both==ai.intersection(iot) and one==ai.symmetric_difference(iot))
    for n in (10000,100000,1000000):
        a=[str(i) for i in range(n)]; s=set(a); target=str(n-1)
        t=time.perf_counter(); x=target in a; lt=time.perf_counter()-t
        t=time.perf_counter(); y=target in s; st=time.perf_counter()-t
        print(f"n={n}: list={lt:.7f}s set={st:.7f}s same={x==y}")
if __name__=="__main__": main()
