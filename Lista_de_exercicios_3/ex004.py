entrada = input("digite um numero: ")
x = int(entrada)
status= 0
for var in range(2, x):
    if x % var == 0:
        print("Não é numero primo")
        status=1
        break
if status == 0:
    print("É numero primo")
