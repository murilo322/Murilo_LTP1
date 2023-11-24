n = int(input("Digite um número inteiro positivo: "))
soma = 0

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        soma += i

print(f"A soma dos números inteiros positivos de 1 a {n} divisíveis por 3 ou 5 é {soma}")
