import copy, sys, time
rows,cols=3,4
bad=[[0]*cols]*rows; bad[0][1]=7
good=[[0 for _ in range(cols)] for _ in range(rows)]; good[0][1]=7
stops={(13.0827,80.2707):"Chennai Central",(13.0418,80.2341):"T. Nagar"}
def main():
    print("Q2 Tuples and copying"); print("bad:",bad); print("good:",good)
    print("Same row object:",bad[0] is bad[1],good[0] is good[1])
    print("Bus stop:",stops[(13.0418,80.2341)])
    a=[[1,2],[3,4]]; alias=a; shallow=copy.copy(a); deep=copy.deepcopy(a); a[0][0]=99
    print("Alias:",alias,"Shallow:",shallow,"Deep:",deep)
    inside=([1,2],"stop"); inside[0].append(3); print("List inside tuple:",inside)
    values=list(range(1000000)); tup=tuple(values)
    print("List bytes:",sys.getsizeof(values),"Tuple bytes:",sys.getsizeof(tup))
    try: stops[[13.0418,80.2341]]="bad"
    except TypeError as e: print("List key error:",e)
if __name__=="__main__": main()
