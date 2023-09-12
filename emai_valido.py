import re

def validar_email(email):

    padrao = r'^\S+@\S+\.\S+$'

    if re.match(padrao, email):
        return True
    else:
        return False

email = input("Digite um email: ")

if validar_email(email):
    print(f"O email '{email}' é válido.")
else:
    print(f"O email '{email}' não é válido.")
