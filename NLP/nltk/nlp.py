import nltk
from nltk.corpus import webtext

for fileid in webtext.fileids():
    print(fileid)
    words = webtext.words(fileid)
    print(words)
    print(f"文件长度: {len(words)} 单词数量: {len(set(words))} 词汇表长度: {len(set(words))}\n")