import time
def phone_key(value):
    digits="".join(c for c in (value or "") if c.isdigit())
    return digits[-10:] if digits.startswith("91") and len(digits)>10 else digits
def merge(contacts):
    result={}
    for c in contacts:
        name=c.get("name","").strip(); phone=phone_key(c.get("phone","")); email=c.get("email","").strip().lower()
        key=phone if phone else "name:"+ " ".join(name.lower().replace("."," ").split())
        if key=="name:": continue
        if key not in result: result[key]={"names":set(),"numbers":set(),"emails":set()}
        if name: result[key]["names"].add(name)
        if phone: result[key]["numbers"].add(phone)
        if email: result[key]["emails"].add(email)
    return result
def main():
    contacts=[{"name":"Dr. Ravi","phone":"+91 98400 12345","email":"Ravi@example.com"},{"name":"Meena","phone":"9876543210","email":"meena@example.com"},{"name":"ravi kumar","phone":"9840012345","email":"ravi.work@example.com"},{"name":"Meena","phone":"+91-9876543210","email":""},{"name":"Karthik","phone":"","email":"karthik@example.com"}]
    print("Q7 Contact merging")
    result=merge(contacts)
    for k,v in result.items(): print(k,v)
    for n in (1000,100000):
        data=[{"name":f"Person {i}","phone":f"+91 90000 {i:05d}","email":""} for i in range(n)]
        t=time.perf_counter(); result=merge(data); elapsed=time.perf_counter()-t
        print(f"n={n}: dictionary={elapsed:.5f}s groups={len(result)}")
    # Pairwise comparison is demonstrated only on a small sample to avoid excessive runtime.
    small=contacts[:]
    t=time.perf_counter(); pairs=0
    for i in range(len(small)):
        for j in range(i+1,len(small)):
            if phone_key(small[i].get("phone"))==phone_key(small[j].get("phone")): pairs+=1
    print("Small pairwise duplicate pairs:",pairs)
if __name__=="__main__": main()
