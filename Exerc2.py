limite_inferior = int(input("Digite o limite inferior: "))
limite_superior = int(input("Digite o limite superior: "))

for num in range(limite_inferior, limite_superior + 1):
    if num % 2 == 0:
        print(num)