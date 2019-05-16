class Carro:

    #torna a variavel privada do objeto
    #__nome = "" 

    #construtor da classe
    def __init__(self, nome,ano):
        self.nome = nome
        self.ano = ano

    #métodos get set
    def setNome(self, nome):
        self.__nome = nome

    def setAno (self, ano):
        self.ano = ano

    def getNome(self):
        return self.nome
    
    def getAno(self):
        return self.ano

carro = Carro('celta',2012)
print(carro.getNome())
print(carro.getAno())

def oi():
    print('oi')


#Exemplo de herança de classes
class ClassePai:
    var1 = "Pai"

#ClasseFilho herda de ClassePai
class ClasseFilho(ClassePai):
    pass#não faz nada mas executa o for

p = ClassePai()
f  = ClasseFilho()
print(p.var1)
print(f.var1)