numero = int(input("Digite um número inteiro positivo: "))
quadrados = {i: i * i for i in range(1, numero + 1)}

print("Quadrados dos números inteiros positivos:")
for i, quadrado in quadrados.items():
    print(f"{i}: {quadrado}")
