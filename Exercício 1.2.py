"""
#2
#Exercício 1.2: Gerenciador de Pedidos de Restaurante

# Contexto:
# Você está ajudando um pequeno restaurante a digitalizar seus processos. Eles querem um programa simples que gerencie os pedidos de seus clientes. Cada pedido pode ter vários itens, e cada item tem um preço associado.

# Objetivo:
# Crie um programa que permite ao usuário adicionar pedidos, adicionar itens aos pedidos e calcular o total de um pedido.

# Requisitos:

# O programa deve ter um dicionário de itens_menu onde as chaves são nomes de itens e os valores são os preços. Por exemplo: {"hamburger": 5.50, "batata frita": 2.00, "refrigerante": 1.50}.
# Os pedidos podem ser armazenados em um dicionário chamado pedidos, onde as chaves são números de pedido e os valores são outro dicionário contendo os itens pedidos e suas quantidades.
# O programa deve permitir que o usuário:
# Adicione um novo pedido.
# Adicione itens a um pedido existente.
# Calcule e exiba o total de um pedido.
# Instruções:

# Inicialize o dicionário itens_menu com pelo menos 5 itens e seus preços.
# Permita que o usuário adicione novos pedidos. Um pedido deve ser outro dicionário com itens e quantidades. Por exemplo: {1: {"hamburger": 2, "refrigerante": 1}} representa um pedido com 2 hambúrgueres e 1 refrigerante.
# Permita que o usuário adicione itens a um pedido existente, especificando o número do pedido, o item e a quantidade.
# Implemente uma função chamada calcular_total_pedido que aceita um número de pedido e retorna o total desse pedido, multiplicando preços e quantidades e somando todos os itens.
# Desafio:

# Implemente uma funcionalidade que permite ao usuário remover itens de um pedido ou alterar a quantidade de um item em um pedido.
# Permita que o usuário visualize todos os pedidos atuais e seus totais.
# Dicas:

# Lembre-se de verificar se um item adicionado pelo usuário realmente existe no menu.
# Ao calcular o total, lembre-se de multiplicar o preço do item pela quantidade e, em seguida, somar os totais para todos os itens.
"""
class Restaurante:
    def __init__(self):
        self.itens_menu = {
            "hamburguer": 5.50,
            "batata frita": 2.00,
            "refrigerante": 1.50,
            "pizza": 8.00,
            "salada": 3.00
        }
        self.pedidos = {}
        self.numero_pedido = 1

    def adicionar_pedido(self):
        pedido = {}
        while True:
            item = input("Digite o nome do item (ou 'fim' para concluir o pedido): ").lower()
            if item == 'fim':
                break
            if item in self.itens_menu:
                quantidade = int(input(f"Quantidade de {item}: "))
                pedido[item] = quantidade
            else:
                print("Item não encontrado no menu. Por favor, escolha novamente.")

        if pedido:
            self.pedidos[self.numero_pedido] = pedido
            self.numero_pedido += 1
            print(f"Pedido {self.numero_pedido - 1} adicionado com sucesso!")

    def adicionar_item_pedido(self):
        numero_pedido = int(input("Digite o número do pedido: "))
        if numero_pedido in self.pedidos:
            pedido = self.pedidos[numero_pedido]
            while True:
                item = input("Digite o nome do item (ou 'fim' para concluir): ").lower()
                if item == 'fim':
                    break
                if item in self.itens_menu:
                    quantidade = int(input(f"Quantidade de {item}: "))
                    if item in pedido:
                        pedido[item] += quantidade
                    else:
                        pedido[item] = quantidade
                else:
                    print("Item não encontrado no menu. Por favor, escolha novamente.")
            print("Itens adicionados ao pedido.")
        else:
            print("Pedido não encontrado.")

    def calcular_total_pedido(self, numero_pedido):
        if numero_pedido in self.pedidos:
            pedido = self.pedidos[numero_pedido]
            total = sum(self.itens_menu[item] * quantidade for item, quantidade in pedido.items())
            return total
        else:
            return None

    def listar_pedidos(self):
        for numero, pedido in self.pedidos.items():
            total = self.calcular_total_pedido(numero)
            print(f"Pedido {numero}: {pedido} - Total: R${total:.2f}")


restaurante = Restaurante()

while True:
    print("aqui nos temos hamburguer: 5.50, batata frita: 2.00, refrigerante: 1.50, pizza: 8.00, salada: 3.00")
    print("\nEscolha uma opção:")
    print("1. Adicionar um novo pedido")
    print("2. Adicionar itens a um pedido existente")
    print("3. Calcular o total de um pedido")
    print("4. Listar todos os pedidos")
    print("5. Sair")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        restaurante.adicionar_pedido()
    elif opcao == "2":
        restaurante.adicionar_item_pedido()
    elif opcao == "3":
        numero_pedido = int(input("Digite o número do pedido: "))
        total = restaurante.calcular_total_pedido(numero_pedido)
        if total is not None:
            print(f"Total do Pedido {numero_pedido}: R${total:.2f}")
        else:
            print("Pedido não encontrado.")
    elif opcao == "4":
        restaurante.listar_pedidos()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Digite 1, 2, 3, 4 ou 5.")