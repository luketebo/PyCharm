import nltk
from nltk.corpus import webtext
import jieba

with open("D:\\Code-repository\\PyCharm\\NLP\\nltk\\SkyDragon.txt") as f:
    word = f.read()
    text = jieba.cut(word, cut_all=False)


fdist = nltk.FreqDist(text)
print(fdist)