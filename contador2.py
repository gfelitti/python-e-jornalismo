#coding=UTF-8
file=open("arquivo.rtf","r+", encoding="utf-8-sig")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k in wordcount.items():
    print(k)
print(wordcount["TERMO1"])
print(wordcount["TERMO2"])
print(wordcount["TERMO3"])
print(wordcount["TERMO4"])
