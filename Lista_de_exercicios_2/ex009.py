nome = input ("Digite o seu nome: ")

sexo = input ("Digite seu sexo, f para feminino e m para masculino: ")

civil= input ("Digite seu estado civil, se for casado digite c, e se for solteiro digite s ")




if  sexo == "f" and  civil == "c" :

	tempo = input ("Informe o tempo de casada")
	
	print("O nome é :"+str (nome))
	print("O sexo é: "+str (sexo))
	print("O estado civil é casada")
	print("O tempo de relacionamento é: "+str (tempo))
else:
	print("O nome é :"+str (nome))
	print("O sexo é:"+str (sexo))
	print( "O estado civil é :"+str (civil))

print ("fim do programa")
