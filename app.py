from valida_login import *
from cryptographyFramework import *


def main():
    while True:
        username = input("Digite seu nome de usuário: ")
        if validate_username(username):
            break
        else:
            print("O nome de usuário deve ter a primeira letra maiúscula, sem caracteres especiais e sem espaços e no máximo 30 caracteres.")

    while True:
        password = input("Digite sua senha: ")
        if validate_password(password):
            break
        else:
            print("A senha deve ter pelo menos 10 caracteres, um caracter especial, um número, ao menos uma letra maiúscula e uma letra minúscula.")

    while True:
        message = input("Digite a mensagem a criptografar (máximo 70 caracteres): ")
        if len(message) <= 70:
            break
        else:
            print("A mensagem deve ter no máximo 70 caracteres.")

    encryptedText = encryptMessage(username, password, message)
    saveNewLine(encryptedText)

if __name__ == '__main__':
    main()