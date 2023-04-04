import os

import jieba

dir = "D:\\Code-repository\\PyCharm\\NLP\\nltk\\zh"
ls_dir = os.listdir("D:\\Code-repository\\PyCharm\\NLP\\nltk\\zh")

for item in ls_dir:
    with open(dir + "\\" + item) as f:
        word = f.read()
    word += word

f = open("SkyDragon.txt", "w")
f.write(word)
f.close()
