entrada = input ("digite o valor de A:  ")
a = int (entrada)
entrada = input ("digite o  valor de B: ")
b = int (entrada)
entrada = input ("digite o  valor de c: ")
c = int (entrada)


if  (a  + b) < c:
    resposta= a + b
    print ("O resultado da soma de a + b  é menor que c ($c), o resultado é :" +str (resposta) )
else: 
	resposta= a + b
	print("O resultado da soma de a + b é maior que c , o resultado é a:" +str (resposta) )
