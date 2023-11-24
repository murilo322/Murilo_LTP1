"""

# Dicionário
# Lista
# Tupla
# String

import array as ar

obj = ar.array('i', [1,2,3])
print(type(obj), obj)

obj2 = ar.array('u', 'IESGO')
print(type(obj2), obj2)

obj3 = ar.array('d', [1.233, 1.1334, 3.3])
print(type(obj3), obj3)

"""

import array as arr

# Criar um array de inteiros vazio
meu_array = arr.array('i')
print(meu_array)

#Adicionar 5 números no ao array
for i in range(5):
    num = int(input("Insira um número inteiro: "))
    meu_array.append(num)


print("Array resultante: ", meu_array)

# Somar números no Array
print(sum(meu_array))

# Enscontrar o min e o max
min_valor = min(meu_array)
max_valor = max(meu_array)
print(f"O menor valor é: {min_valor}\n0 maior valor é: {max_valor}")

# Remover o último elemento
print(meu_array)
meu_array.pop()
print("Removido o último elemento", meu_array)

# Inverter a ordem
meu_array.reverse()
print("Lista invertida", meu_array)