contadoridade= 0
contador= 0
while contador < 10:
    entrada = input ("digite uma idade ")
    idade = int (entrada)

    if idade >= 18:
        contadoridade=contadoridade + 1

    contador=contador +1
    
print ("O numero de maiores de idades são: ",end="")
print (contador)
    
