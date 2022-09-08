entrada = input ("digite o primeiro numero ")
n1 = int (entrada)
entrada = input ("digite o primeiro numero ")
n2 = int (entrada)
entrada = input ("digite o primeiro numero ")
n3= int (entrada)

 
if  n1 == n2 and  n1 == n3:

	print ("Os 3 numeros são iguais")
elif n1 == n2 or n1 == n3 or n2 == n3:
    print ("2 numeros são iguais")
else:
	print ("todos numeros diferentes")
