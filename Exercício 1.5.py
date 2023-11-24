"""
#Exercício 1.5:  Sistema de Gerenciamento de Estudantes

# Contexto:
# Você está construindo um software para gerenciar estudantes em uma escola. Cada estudante tem um nome, idade, nota e um ID único. A escola deseja realizar várias operações com esses estudantes, como adicionar uma nota a um estudante, calcular a média da turma e encontrar o estudante com a maior nota.

# Objetivo:
# Crie uma classe para representar um estudante e uma classe para representar uma turma de estudantes. Use métodos dentro dessas classes para executar as operações necessárias.

# Requisitos:

# Crie uma classe chamada Estudante com os seguintes atributos:

# nome
# idade
# nota
# id
# Crie uma classe chamada Turma com o seguinte atributo:

# estudantes: uma lista para armazenar objetos da classe Estudante.
# Adicione os seguintes métodos à classe Turma:

# adicionar_estudante(self, estudante): adiciona um estudante à turma.
# remover_estudante(self, id): remove um estudante usando sua ID.
# media_da_turma(self): calcula e retorna a média das notas dos estudantes.
# melhor_estudante(self): retorna o estudante com a maior nota.
# Desafio:
# Adicione os seguintes métodos à classe Estudante:

# alterar_nota(self, nova_nota): modifica a nota do estudante.
# informacoes(self): imprime informações básicas sobre o estudante.

"""

class Estudante:
    def __init__(self, nome, idade, nota, id):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.id = id

    def alterar_nota(self, nova_nota):
        self.nota = nova_nota

    def informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Nota: {self.nota}, ID: {self.id}"

class Turma:
    def __init__(self):
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)
        print(f"Legal! O estudante {estudante.nome} foi adicionado à turma.")

    def remover_estudante(self, id):
        for estudante in self.estudantes:
            if estudante.id == id:
                self.estudantes.remove(estudante)
                print(f"O estudante {estudante.nome} foi removido da turma.")
                return
        print(f"Desculpe, mas o estudante com ID {id} não foi encontrado na turma.")

    def media_da_turma(self):
        if len(self.estudantes) == 0:
            return 0
        total_notas = sum(estudante.nota for estudante in self.estudantes)
        return total_notas / len(self.estudantes)

    def melhor_estudante(self):
        if len(self.estudantes) == 0:
            return None
        melhor = max(self.estudantes, key=lambda estudante: estudante.nota)
        return melhor

turma = Turma()

estudante1 = Estudante("Alice", 18, 95, 1)
estudante2 = Estudante("Bob", 17, 88, 2)
estudante3 = Estudante("Carol", 19, 92, 3)

turma.adicionar_estudante(estudante1)
turma.adicionar_estudante(estudante2)
turma.adicionar_estudante(estudante3)

media = turma.media_da_turma()
print(f"A média da turma é: {media:.2f}")

melhor = turma.melhor_estudante()
if melhor:
    print(f"O melhor estudante é: {melhor.nome} (Nota: {melhor.nota})")

turma.remover_estudante(2)

print("\nEstudantes na turma:")
for estudante in turma.estudantes:
    print(estudante.informacoes())