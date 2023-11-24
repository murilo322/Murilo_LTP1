"""
#1
#Exercício 1.1: Sistema de Biblioteca
# Contexto:
# Você foi contratado para criar um simples sistema de gerenciamento para uma pequena biblioteca. Os requisitos iniciais são criar um programa que permita ao usuário gerenciar livros e membros da biblioteca.

# Requisitos:

# A biblioteca deve ser capaz de armazenar informações sobre os livros, como título, autor e status (emprestado ou disponível).
# A biblioteca deve também ser capaz de armazenar informações sobre os membros, como nome e os livros que eles emprestaram.
# Implemente funcionalidades para adicionar livros, emprestar livros a membros e retornar livros.

# Instruções:

# Crie uma classe chamada Livro que tenha os seguintes atributos: titulo, autor e status. Por padrão, todos os livros devem ter o status "disponível".

# Crie uma classe chamada Membro que tenha os seguintes atributos: nome e livros_emprestados (uma lista).

# Crie uma classe chamada Biblioteca que tenha os seguintes atributos: livros (um dicionário com o título do livro como chave e a instância do livro como valor) e membros (um dicionário com o nome do membro como chave e a instância do membro como valor).

# Na classe Biblioteca, crie os seguintes métodos:

# adicionar_livro(self, livro): Adiciona um livro ao dicionário de livros.
# registrar_membro(self, membro): Adiciona um membro ao dicionário de membros.
# emprestar_livro(self, titulo_livro, nome_membro): Empresta um livro para um membro se o livro estiver disponível.
# retornar_livro(self, titulo_livro, nome_membro): Retorna um livro que estava emprestado.


# Desafio:

# Adicione funcionalidades para remover livros ou membros.
# Implemente uma busca para encontrar um livro ou membro por nome.
# Dicas:

# Use dicionários para armazenar livros e membros na classe Biblioteca para fácil acesso.
# Ao emprestar um livro, atualize o status do livro e a lista de livros emprestados do membro.
# Ao retornar um livro, faça o processo inverso do empréstimo.
"""
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = "disponível"

class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.membros = {}

    def adicionar_livro(self, livro):
        self.livros[livro.titulo] = livro

    def registrar_membro(self, membro):
        self.membros[membro.nome] = membro

    def emprestar_livro(self, titulo_livro, nome_membro):
        if titulo_livro in self.livros and nome_membro in self.membros:
            livro = self.livros[titulo_livro]
            if livro.status == "disponível":
                membro = self.membros[nome_membro]
                livro.status = "emprestado"
                membro.livros_emprestados.append(livro)
                return f"{titulo_livro} emprestado para {nome_membro}."
            else:
                return f"{titulo_livro} não está disponível para empréstimo."
        else:
            return "Livro ou membro não encontrados."

    def retornar_livro(self, titulo_livro, nome_membro):
        if titulo_livro in self.livros and nome_membro in self.membros:
            livro = self.livros[titulo_livro]
            membro = self.membros[nome_membro]
            if livro in membro.livros_emprestados:
                livro.status = "disponível"
                membro.livros_emprestados.remove(livro)
                return f"{titulo_livro} retornado por {nome_membro}."
            else:
                return f"{titulo_livro} não foi emprestado para {nome_membro}."
        else:
            return "Livro ou membro não encontrados."

def operacao_livro(biblioteca, operacao):
    while True:
        titulo_livro = input("Digite o título do livro: ")
        if titulo_livro in biblioteca.livros:
            nome_membro = input("Digite o nome do membro: ")
            if nome_membro in biblioteca.membros:
                if operacao == "emprestar":
                    print(biblioteca.emprestar_livro(titulo_livro, nome_membro))
                elif operacao == "retornar":
                    print(biblioteca.retornar_livro(titulo_livro, nome_membro))
                break
            else:
                print("Membro não encontrado.")
        else:
            print("Livro não encontrado.")

livro1 = Livro("Dom Quixote", "Miguel de Cervantes")
livro2 = Livro("1984", "George Orwell")
livro3 = Livro("A Revolução dos Bichos", "George Orwell")

membro1 = Membro(input(" cadastre o seu nome: "))

biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.registrar_membro(membro1)

while True:
    print("\nEscolha uma operação:")
    print("1. Emprestar livro")
    print("2. Retornar livro")
    print("3. Sair")
    escolha = input("Digite o número da operação desejada: ")

    if escolha == "1":
        operacao_livro(biblioteca, "emprestar")
    elif escolha == "2":
        operacao_livro(biblioteca, "retornar")
    elif escolha == "3":
        break
    else:
        print("Opção inválida. Digite 1, 2 ou 3.")
