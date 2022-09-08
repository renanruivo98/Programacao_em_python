import os
contador= 0
if os.path.exists("atividade1006.txt"):
    f=open("atividade1006.txt","r")
    for linha in f:
       print(linha)
       contador=contador+1 
    print("o numero de linhas é: "+ str (contador))
    f.close()
    f=open("atividade1006.txt","a")
    f.write("ue os rivais do time da marginal sem número, que até pouco tempo,""\n"
    "lutavam para não cair, os rivais do decadente time da Vila Sônia, cuja as glórias,""\n"
    "realmente estão só no passado, e os peixinhos,""\n" 
    "que nadaram, nadaram e morreram na praia,""\n" 
    "continuem repetindo aos quatro ventos: O Palmeiras não tem mundial!""\n")
    f.close()
else:
    f=open("atividade1006.txt","w")
    f.close()
    f=open("atividade1006.txt","a")
    f.write("O palmeiras não tem mundial""\n"
    "Palmeiras não tem mundial""\n"
    "Não tem copinha, não tem mundial""\n"
    "Não tem copinha, não tem mundial""\n")
    f.close()
