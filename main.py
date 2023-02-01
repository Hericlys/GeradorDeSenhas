from string import ascii_letters, digits, punctuation
from random import choice


def generate_password(length):
    # gera a senha
    chars = ascii_letters + digits + punctuation
    password = ''.join(choice(chars) for i in range(length))
    return password


def check_int(msg):
    # verifica o o valor fornecido é um numero inteiro.
    while True:
        try:
            r = int(input(msg))
        except ValueError:
            print("O valor fornecido nao é um numero inteiro, tente novamente.")
            continue
        break
    return r


def main():
    msg = 'digite a quantidade de caracteres que deseja na senha: '
    password_length = check_int(msg)
    password = generate_password(password_length)
    print(f"A senha gerada é: {password}")


if __name__ == "__main__":
    main()
