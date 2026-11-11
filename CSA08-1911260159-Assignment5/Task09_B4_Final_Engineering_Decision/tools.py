import re
from collections import Counter
POS={"good","clean","fast","helpful","improved"}; NEG={"bad","dirty","slow","rude","smoke","broken"}; NEGATORS={"not","never","no"}
STOP={"the","is","are","was","and","but","near","my","here","today","there","of","a","to"}
def score(text):
    words=re.findall(r"[a-z']+",text.lower()); total=0
    for i,x in enumerate(words):
        value=1 if x in POS else -1 if x in NEG else 0
        if i and words[i-1] in NEGATORS:value=-value
        total+=value
    return total
def label(text):
    n=score(text); return "positive" if n>0 else "negative" if n<0 else "neutral"
def summarise(text,k=3):
    sentences=[x.strip() for x in re.split(r"(?<=[.!?])\s+",text) if x.strip()]
    counts=Counter(x for x in re.findall(r"[a-z']+",text.lower()) if x not in STOP and len(x)>2)
    ranked=sorted(enumerate(sentences),key=lambda pair:(-sum(counts[w] for w in re.findall(r"[a-z']+",pair[1].lower())),pair[0]))
    chosen={i for i,_ in ranked[:k]}
    return " ".join(s for i,s in enumerate(sentences) if i in chosen)
