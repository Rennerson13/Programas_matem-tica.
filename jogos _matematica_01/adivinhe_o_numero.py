 # teoria de boole 

import random

def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    print("Jogador 1, pense em um número entre 1 e 100.")
    numero_secreto = int(input("Jogador 1, digite o número secreto: "))

    print("\n" * 50)

    print("Jogador 2, é a sua vez de adivinhar!")

    tentativas = 0
    adivinhou = False

    while not adivinhou:
        tentativa = int(input("Jogador 2, faça uma suposição: "))
        tentativas += 1

        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
            adivinhou = True
        elif tentativa < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

    reiniciar = input("Deseja jogar novamente? (S/N): ").strip().upper()
    if reiniciar == "S":
        jogo_adivinhacao()
    else:
        print("Obrigado por jogar!")

if __name__ == "__main__":
    jogo_adivinhacao()
