import nltk.draw
from nltk.corpus import webtext
from nltk.corpus import PlaintextCorpusReader
from nltk import Text
import jieba
import matplotlib  # 注意这个也要import一次
import matplotlib.pyplot as plt

plt.rc('font', family='YouYuan')
root = r"D:\\Code-repository\\PyCharm\\NLP\\nltk\\zh"
wordlist = PlaintextCorpusReader(root, ".*")
i = 0
for item in wordlist.fileids():
    i += 1
    if i == 4:
        word = wordlist.raw(item)

tokens = jieba.lcut(word)

t = Text(tokens)
print(t.count("包不同"))
keyword = "包不同"
nltk.Text(tokens).dispersion_plot(['包不同'])
plt.show()
