#coding=UTF-8
arq = open("arquivo.rtf")
texto = arq.read()
texto = texto.lower()
arq.close()
import string

for c in ",./?:;,\/[]{}":
    texto = texto.replace(c, " ")

texto = texto.split()

dic ={ }
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1

#print(dic)
print(dic["nao"])
print(dic["sim"])