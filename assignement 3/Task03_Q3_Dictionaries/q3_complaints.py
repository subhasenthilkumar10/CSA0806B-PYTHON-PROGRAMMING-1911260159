import random,string,time
from collections import Counter,defaultdict
calls=["seeds not received seeds delayed","fertiliser price high","seeds price high subsidy not received"]
STOP={"not","high"}
def frequencies(texts,stop):
    d={}
    for text in texts:
        for word in text.lower().translate(str.maketrans("","",string.punctuation)).split():
            if word not in stop: d[word]=d.get(word,0)+1
    return d
def top(d,k): return sorted(d.items(),key=lambda x:(-x[1],x[0]))[:k]
def main():
    print("Q3 Dictionaries"); print("Top words:",top(frequencies(calls,STOP),3))
    groups=defaultdict(list)
    for district,msg in [("Erode","seed delay"),("Salem","price high"),("Erode","fertiliser issue")]: groups[district].append(msg)
    print("District counts:",{k:len(v) for k,v in groups.items()})
    random.seed(3); words=["seed","water","price","crop","rain"]
    for n in (1000,10000,100000):
        texts=[" ".join(random.choices(words,k=8)) for _ in range(n)]
        t=time.perf_counter(); d=frequencies(texts,set()); dt=time.perf_counter()-t
        allw=" ".join(texts).split(); unique=set(allw)
        t=time.perf_counter(); slow={w:allw.count(w) for w in unique}; st=time.perf_counter()-t
        t=time.perf_counter(); c=Counter(allw); ct=time.perf_counter()-t
        print(f"n={n}: dict={dt:.5f}s list.count={st:.5f}s Counter={ct:.5f}s same={d==slow==dict(c)}")
    print("Empty:",frequencies([""],STOP),"Case:",frequencies(["SEEDS seeds"],STOP))
if __name__=="__main__": main()
