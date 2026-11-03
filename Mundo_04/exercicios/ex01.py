# Declaração de classes

class Gafanhoto:
    def __init__(self):  # Metodo construtor
        # Atributo de instância

        self.nome = ""
        self.idade = 0

    # Metodo de instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
# Declaração de objetos

g1 = Gafanhoto()
g1.nome = "Arthur"
g1.idade = 21
g1.aniversario()
print(g1.mensagem())
