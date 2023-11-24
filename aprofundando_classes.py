# File handling (gestão de arquivos)
# Quais as funções básicas para gestão de arquivo?
### ler (read)
### criar (create)
### escrever (write)
### acrescentar (append)



minha_lista = "minhalista.txt"

f = open(minha_lista)
print(f.readline())
f.close()