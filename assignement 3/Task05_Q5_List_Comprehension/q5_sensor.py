import random,time,sys
def loop(a):
    v=[]
    for x in a:
        if -50<=x<=50: v.append(x)
    return v,[(x*9/5)+32 for x in v]
def comp(a):
    v=[x for x in a if -50<=x<=50]
    return v,[(x*9/5)+32 for x in v]
def mapped(a):
    v=list(filter(lambda x:-50<=x<=50,a))
    return v,list(map(lambda x:x*9/5+32,v))
def main():
    a=[4.5,9,55,-60,7,1.5,51]; result=comp(a)
    print("Q5 List comprehension"); print("Valid:",result[0]); print("Fahrenheit:",[round(x,2) for x in result[1]])
    print("Alarm minutes:",[i for i,x in enumerate(a) if x<2 or x>8])
    print("Same results:",loop(a)==comp(a)==mapped(a))
    for n in (10000,100000,1000000):
        data=[random.uniform(-60,60) for _ in range(n)]; times=[]
        for f in (loop,comp,mapped):
            t=time.perf_counter(); f(data); times.append(time.perf_counter()-t)
        print(f"n={n}: loop={times[0]:.5f}s comp={times[1]:.5f}s map/filter={times[2]:.5f}s")
    g=(x for x in a if -50<=x<=50)
    print("List bytes:",sys.getsizeof([x for x in a if -50<=x<=50]),"Generator bytes:",sys.getsizeof(g))
if __name__=="__main__": main()
