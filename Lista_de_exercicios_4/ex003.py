nota= int(input("informe a nota do aluno: "))
if nota < 0 or nota > 100:
    raise Exception ("A nota não pode ser menor que 0 ou maior que 100")
