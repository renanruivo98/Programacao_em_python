class Disciplina:
    nome = "disciplina" 
    cargaHoraria = 18 
    notaMinima = 6
    turma = "3redes"
   
    def colocarNome(self,nom):
        self.nome= nom
    def colocarCargaHoraria(self,cg):
        self.cargaHoraria= cg
    def colocarnotaMinima(self, mini):
        self.notaMinima= mini
    def colocartuma(self,tur):
        self.turma= tur
    def imprimir (self):
        print(self.nome)
        print(self.cargaHoraria)
        print(self.notaMinima)
        print(self.turma)
programacao= Disciplina()
programacao.colocarNome("programacao")
programacao.colocarCargaHoraria(33)
programacao.colocarnotaMinima(6)
programacao.colocartuma("1redes")
programacao.imprimir()
programacao2= Disciplina()
programacao.colocarNome("programacao2")
programacao.colocarCargaHoraria(66)
programacao.colocarnotaMinima(6)
programacao.colocartuma("3redes")
programacao2.imprimir()

