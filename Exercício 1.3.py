"""
#Exercício 1.3: Sistema de Gerenciamento de Zoológico

# Contexto:
# Você foi encarregado de desenvolver um sistema para gerenciar os animais de um zoológico. O zoológico tem vários tipos de animais, e eles precisam de uma forma organizada de acompanhar informações básicas sobre esses animais, como espécie, dieta, idade e habitat.

# Requisitos:

# Crie uma classe Animal que tenha os seguintes atributos:

# nome (nome do animal)
# especie (por exemplo, "Leão", "Pinguim", "Cobra")
# idade
# dieta (por exemplo, "Carnívoro", "Herbívoro", "Onívoro")
# A classe Animal também deve ter um método descricao que retorna uma string formatada, descrevendo o animal (por exemplo, "Leo é um Leão de 5 anos que é Carnívoro").

# Crie uma classe Zoologico que tenha os seguintes atributos:

# animais (uma lista para armazenar instâncias da classe Animal)
# A classe Zoologico deve ter os seguintes métodos:

# adicionar_animal(self, animal): para adicionar um novo animal ao zoológico.
# remover_animal(self, nome): para remover um animal do zoológico usando seu nome.
# listar_animais(self): para listar todos os animais no zoológico e suas informações.
# Desafio:

# Adicione um atributo habitat à classe Animal (por exemplo, "Savana", "Tundra", "Floresta Tropical"). Modifique o método descricao para incluir essa informação.
# Na classe Zoologico, adicione um método buscar_por_especie(self, especie) que retorna uma lista de animais dessa espécie específica.
# Implemente a possibilidade de listar todos os animais em um habitat específico.
# Dicas:

# Ao adicionar ou remover animais da lista em Zoologico, lembre-se de usar os métodos da lista, como append ou remove.
# Ao listar os animais, use um loop para iterar sobre todos os animais e chamar o método descricao de cada animal.
"""

class Animal:
    def __init__(self, nome, especie, idade, dieta, habitat=None):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.dieta = dieta
        self.habitat = habitat

    def descricao(self):
        if self.habitat:
            return f"{self.nome} é um(a) {self.especie} de {self.idade} anos que é {self.dieta} e habita a {self.habitat}."
        else:
            return f"{self.nome} é um(a) {self.especie} de {self.idade} anos que é {self.dieta}." #aqui eu coloquei tanto pro feminino quanto pro masculino pra definir os animais de uma forma de melhor entendimento 

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)
        print(f"{animal.nome} foi adicionado ao zoológico.")

    def remover_animal(self, nome):
        for animal in self.animais:
            if animal.nome == nome:
                self.animais.remove(animal)
                print(f"{animal.nome} foi removido do zoológico.")
                return
        print(f"Animal com nome {nome} não encontrado no zoológico.")

    def listar_animais(self):
        print("Animais no zoológico:")
        for animal in self.animais:
            print(animal.descricao())

    def buscar_por_especie(self, especie):
        animais_da_especie = []
        for animal in self.animais:
            if animal.especie == especie:
                animais_da_especie.append(animal)
        return animais_da_especie

    def listar_animais_por_habitat(self, habitat):
        animais_no_habitat = []
        for animal in self.animais:
            if animal.habitat == habitat:
                animais_no_habitat.append(animal)
        return animais_no_habitat

zoo = Zoologico()

leao = Animal("Leo", "Leão", 5, "Carnívoro", "Savana")
pinguim = Animal("Pingu", "Pinguim", 3, "Piscívoro", "Tundra")
cobra = Animal("Cobi", "Cobra", 2, "Carnívoro")

zoo.adicionar_animal(leao)
zoo.adicionar_animal(pinguim)
zoo.adicionar_animal(cobra)

zoo.listar_animais()

print("\nAnimais da espécie 'Leão':")
leoes = zoo.buscar_por_especie("Leão")
for leao in leoes:
    print(leao.descricao())

print("\nAnimais na 'Savana':")
animais_na_savana = zoo.listar_animais_por_habitat("Savana")
for animal in animais_na_savana:
    print(animal.descricao())

zoo.remover_animal("Cobi")

print("\nAnimais no zoológico após a remoção:")
zoo.listar_animais()