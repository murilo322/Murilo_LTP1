def contador_de_letras_do_nome():
    nome = input("Digite um texto: ").lower()
    nome_composto = "seu_nome"  
    contador = 0

    for letra in nome:
        if letra in nome_composto:
            contador += 1

    return contador

letras_no_nome = contador_de_letras_do_nome()
print(f"O número de letras que compõem o seu nome no texto é: {letras_no_nome}")
