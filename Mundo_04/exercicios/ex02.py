# Declaração de class
class Gafanhoto():
    """
Essa classe cria um gafanhoto, que é uma pessoa com Nome e Idade.

Para criar uma nova pessoa, use 
variavel = Gafanhoto(nome,idade)
    """
    def __init__(self, nome = "", idade = 0): # Metodo construtor
        # Atributo de instância
        self.nome = nome
        self.idade = idade 

    # Metodo de instância
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): # Dunder Method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

    def __getstate__(self):
        return f"Estado: Nome = {self.nome} ; idade = {self.idade}"

# Declaração de Objetos
g1 = Gafanhoto("Arthur",21)
g1.aniversario()
print(g1.__dict__) # Attribute
print(g1.__getstate__()) # Method
print(g1.__class__)
print(g1.__doc__) # Dunder attribute

