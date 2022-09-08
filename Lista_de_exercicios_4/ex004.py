x = 12
y =0
try:
    z = x/y
    print(z)
except ZeroDivisionError:
    print("Divisão por zero não é permitida")
try:
    arq = open("data/arquivo.txt", "r")
    print("arquivo encontrado")
except FileNotFoundError:
    print("Erro: arquivo não encontrado")
try:
    import tree
    print("Comando importado")
except ImportError:
    print("Erro de importação")
try:
    lista=[0] * 1000000000000000000
    print(lista)
except MemoryError:
    print("Erro de memoria")
Int = 10
Str = "10"
try:
    resultado= Int / Str
    print(resultado)
except TypeError:
    print("Erro:dois tipos diferentes de dados combinados")    
