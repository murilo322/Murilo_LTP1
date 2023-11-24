#Exercício: criação de um arquivo de texto via Terminal

#Objetivo: Criar um arquivo de texto chamado "meuarquivo.txt"

nome_do_arquivo = "meuarquivo.txt"

with open(nome_do_arquivo, "w") as arquivo:
    arquivo.write("Este é o conteúdo do arquivo")

print(f"O arquivo {nome_do_arquivo} foi criado com sucesso!")