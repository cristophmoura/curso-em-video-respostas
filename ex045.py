import random

escolhas = ["pedra", "papel", "tesoura"]

jogador_escolha = input("Escolha pedra, papel ou tesoura: ")
computador_escolha = random.choice(escolhas)

if jogador_escolha == "pedra":
    if computador_escolha == "pedra":
        print("Empate!")
    elif computador_escolha == "papel":
        print("Você perdeu!")
    else:
        print("Você ganhou!")
elif jogador_escolha == "papel":
    if computador_escolha == "pedra":
        print("Você ganhou!")
    elif computador_escolha == "papel":
        print("Empate!")
    else:
        print("Você perdeu!")
elif jogador_escolha == "tesoura":
    if computador_escolha == "pedra":
        print("Você perdeu!")
    elif computador_escolha == "papel":
        print("Você ganhou!")
    else:
        print("Empate!")
else:
    print("Escolha inválida.")
