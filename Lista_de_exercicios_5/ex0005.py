class Aluno:
    nome = "aluno" 
    idade = 18 
    matricula = 123456 
    telefone = None
    def __init__ (self, n, i, m, t):
        self.nome = n 
        self.idade = i 
        self.matricula = m 
        self.telefone = t 
    def colocarNome(self,nom):
        self.nome= nom
    def colocarIdade(self,id):
        self.idade= id
    def colocarMatricula(self,matri):
        self.matricula= matri
    def colocartelefone(self,tel):
        self.telefone= tel
    def imprimir (self):
        print(self.nome)
        print(self.idade)
        print(self.matricula)
        print(self.telefone)
renan = Aluno("Renan Ruivo", 19, 2555, 3599735658)
renan.imprimir()
renan2 = Aluno("Renan Ruivo Anselmo", 19, 6666666, 3599735658)
renan2.imprimir()
