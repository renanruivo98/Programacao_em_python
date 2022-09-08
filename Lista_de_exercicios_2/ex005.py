entrada = input ("digite o mês  ")
mes = int (entrada)
entrada = input ("digite o dia ")
dia = int (entrada)
entrada = input ("digite o ano ")
ano  = int (entrada)

if mes >= 1 and  mes  <= 12:
    print("mes valido")
    if  mes == 2:
        if dia  >= 1 and dia  <= 28:
            print ("dia valido")
        else:
             print ("dia invalido")
        
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 9 or  mes == 12:
        
        if dia  >= 1 and dia  <= 31:
            print ("dia valido")
        else:
             print ("dia invalido") 
    
    if mes == 4 or mes == 6 or mes == 9 or mes == 12: 
         
        if dia  >= 1 and dia  <= 30:
            print ("dia valido")
        else:
             print ("dia invalido") 
if ano >= 0:
    print ("ano valido")   
else:
             print ("dia invalido") 
