"""
#Exercício 1.4: Plataforma de Jogos de Azar Online

# Contexto:
# Você está desenvolvendo um software para gerenciar uma plataforma de jogos de azar online. Cada jogo tem um nome, uma categoria (por exemplo, "Pôquer", "Caça-Níqueis", "Roleta"), uma taxa de entrada e uma identificação única. Você gostaria de imprimir facilmente os detalhes dos jogos de uma maneira legível.

# Objetivo:
# Crie classes para representar um jogo e um catálogo de jogos. Use a função _str_() para personalizar a saída quando um jogo é impresso.

# Requisitos:

# Crie uma classe chamada Jogo com os seguintes atributos:

# nome
# categoria
# taxa_entrada
# id
# Implemente o método _str_(self) para a classe Jogo. Quando você imprimir um objeto da classe Jogo, deve retornar uma string no formato: "Nome: [nome], Categoria: [categoria], Taxa de Entrada: [taxa_entrada], ID: [id]".

# Crie uma classe chamada Plataforma com o seguinte atributo:

# jogos: uma lista para armazenar objetos da classe Jogo.
# Adicione os seguintes métodos à classe Plataforma:

# adicionar_jogo(self, jogo): adiciona um jogo à lista.
# remover_jogo(self, id): remove um jogo usando sua ID.
# listar_jogos(self): imprime todos os jogos na plataforma usando um loop e aproveitando a função _str_() da classe Jogo.
# Desafio:

# Implemente o método _str_(self) para a classe Plataforma também. Ao imprimir um objeto da classe Plataforma, deve mostrar quantos jogos existem na plataforma.
"""

class Jogo:
    def __init__(self, nome, categoria, taxa_entrada, id):
        self.nome = nome
        self.categoria = categoria
        self.taxa_entrada = taxa_entrada
        self.id = id

    def _str_(self):
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Taxa de Entrada: {self.taxa_entrada}, ID: {self.id}"

class Plataforma:
    def __init__(self):
        self.jogos = []

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)
        print(f"Jogo {jogo.nome} adicionado à plataforma.")

    def remover_jogo(self, id):
        for jogo in self.jogos:
            if jogo.id == id:
                self.jogos.remove(jogo)
                print(f"Jogo {jogo.nome} removido da plataforma.")
                return
        print(f"Jogo com ID {id} não encontrado na plataforma.")

    def listar_jogos(self):
        print("Jogos na plataforma:")
        for jogo in self.jogos:
            print(jogo)

    def _str_(self):
        return f"Total de Jogos na Plataforma: {len(self.jogos)}"

plataforma = Plataforma()

jogo1 = Jogo("Pôquer", "Cartas", 10.0, 1)
jogo2 = Jogo("Caça-Níqueis", "Slots", 5.0, 2)
jogo3 = Jogo("Roleta", "Mesa", 20.0, 3)

plataforma.adicionar_jogo(jogo1)
plataforma.adicionar_jogo(jogo2)
plataforma.adicionar_jogo(jogo3)

plataforma.listar_jogos()

plataforma.remover_jogo(2)

plataforma.listar_jogos()

print(plataforma)