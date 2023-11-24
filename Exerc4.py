def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

Numero = int(input(" Digite um número inteiro, por gentileza: "))

print(f"Divisores primos de {Numero}:")
for i in range(1, Numero + 1):
    if Numero % i == 0 and is_prime(i):
        print(i)