import sqlite3

def criar_tabela():
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            ano_publicacao INTEGER
        )
    ''')

    conexao.commit()
    conexao.close()


def inserir_livro():
    titulo = input("Insira o título do livro: ")
    autor = input("Insira o autor do livro: ")
    ano_publicacao = int(input("Insira o ano de publicação do livro: "))

    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano_publicacao)
        VALUES (?, ?, ?)
    ''', (titulo, autor, ano_publicacao))

    conexao.commit()
    conexao.close()

def exibir_livros():
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()

    for livro in livros:
        print(f"ID: {livro[0]} - Título: {livro[1]} - Autor: {livro[2]} - Ano de Publicação: {livro[3]}")

    conexao.close()


def remover_livro():
    id_livro = int(input("Insira o ID do livro que deseja remover: "))

    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM livros WHERE id = ?', (id_livro,))

    conexao.commit()
    conexao.close()


def main():
    criar_tabela()

    while True:
        print("\n=== Sistema de Gerenciamento de Livros ===")
        print("1. Inserir novo livro")
        print("2. Consultar todos os livros")
        print("3. Remover livro")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_livro()
        elif opcao == '2':
            exibir_livros()
        elif opcao == '3':
            remover_livro()
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
