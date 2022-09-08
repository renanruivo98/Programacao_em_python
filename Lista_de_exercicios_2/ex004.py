entrada = input ("digite o preço do produto 1 ")
produto1 = float (entrada)
entrada= input ("digite o preço do produto 2 ")
produto2 = float (entrada)
entrada = input ("digite  o preço do produto 3 ")
produto3 = float (entrada)
if produto1 < produto2 and  produto1 < produto3:
    print("O produto mais barato é o 1")
elif produto2 < produto1 and  produto2 < produto3:
    print("O produto mais barato é o 2")
else:
    print("O produto mais barato é o 3")


