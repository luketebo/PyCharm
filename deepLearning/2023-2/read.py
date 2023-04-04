def Gettext():
    with open("hamlet.txt", "r") as f:
        txt = f.read()
    txt = txt.lower()
    for ch in '!"#$%()*+,-./:;<=>?@[\\]^_"{|}~':
        txt = txt.replace(ch, " ")
    return txt


hamletTxt = Gettext()
words = hamletTxt.split()
print(words)
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(len(items)):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
