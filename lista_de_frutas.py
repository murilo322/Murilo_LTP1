lista = []
while True:
    fruta = input("""Insira a fruta que você deseja ou digite "sair" """)
    if fruta == "sair":
        print(lista)
        break
    lista.append(fruta)
    print(lista)