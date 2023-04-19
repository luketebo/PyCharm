from nltk.corpus import PlaintextCorpusReader
import jieba
import re
import matplotlib.pyplot as plt

luxun = PlaintextCorpusReader(".", "Luxun.txt")
luxun_s = luxun.raw('Luxun.txt')
luxun_s = re.sub("[^\u4e00-\u9fa5]+", "", luxun_s)

luxun_s = jieba.lcut(luxun_s)

def Bigram(w1):
    w1 = re.sub("[^\u4e00-\u9fa5]+", "", w1)
    w1 = jieba.lcut(w1)
    Ps = 1
    for i in range(len(w1) - 1):
        count = luxun_s.count(f"{w1[i + 1]}")
        if count == 0:
            Ps = 0
            break
        Ps *= (find_count(luxun_s, w1[i + 1], w1[i]) + 1) / (float) (count + len(set(luxun_s)))
    return Ps

def find_count(ls:list, w1, w2):
    count = 0
    for i in range(len(ls)):
        if w1 == ls[i] and w2 == ls[i-1]:
            count += 1
    return count

def find_countTri(ls:list, w1, w2, w3):
    count = 0
    for i in range(len(ls)):
        if w1 == ls[i] and w2 == ls[i-1] and w3 == ls[i-2]:
            count += 1
    return count

def trigram(w1):
    w1 = re.sub("[^\u4e00-\u9fa5]+", "", w1)
    w1 = jieba.lcut(w1)
    Ps = 1
    for i in range(len(w1) - 2):
        count = find_count(luxun_s, w1[i + 1], w1[i])
        if count == 0:
            Ps = 0
            break
        Ps *= (find_countTri(luxun_s, w1[i + 2], w1[i + 1], w1[i]) + 1) / (float) (count + len(set(luxun_s)))
    return Ps

val = ["猛兽总是独行，牛羊才成群结队。",
"从来如此，便对么？",
"我寄你的信，总要送往邮局，不喜欢放在街边的绿色邮筒中，我总疑心那里会慢一点。",
"学医救不了中国人。"]

# print(len(set(luxun_s)))

# print(find_count(val_, "总是", "野兽"))

y = []
for item in val:
    y.append(trigram(item))
    

x = ['a', 'b', 'c', 'd']

plt.bar(range(len(y)), y, log=True)
plt.show()