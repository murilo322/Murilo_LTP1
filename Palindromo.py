def palindromo(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

entrada = input("Digite uma palavra: ")

if palindromo(entrada):
    print(f"{entrada} é um palíndromo!")
else:
    print(f"{entrada} não é um palíndromo.")