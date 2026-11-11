POSITIVE={"good","clean","fast","helpful","improved"}
NEGATIVE={"bad","dirty","slow","rude","smoke","broken"}
NEGATORS={"not","never","no"}
def score(text):
    words=text.lower().replace("."," ").replace(","," ").split()
    total=0
    for i,word in enumerate(words):
        value=1 if word in POSITIVE else -1 if word in NEGATIVE else 0
        if i>0 and words[i-1] in NEGATORS: value *= -1
        total += value
    return total
def label(text):
    s=score(text)
    return "positive" if s>0 else "negative" if s<0 else "neutral"
