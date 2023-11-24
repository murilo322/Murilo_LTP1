def calcular_o_numero_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

numero = int(input("Digite um número inteiro: "))
resultados = calcular_o_numero_fatorial(numero)
print(f'O fatorial de {numero} é {resultados}')
