import random

print("-----------Jogo de adivinha -----------")
print("----------- Tente adivinhar o número que estou pensando -----------")

c ="S"
while (c == "S"):
    numeroMisterioso = random.randint(1,100)

    acerto = "Errou"
    while (acerto == "Errou"):
        
        resposta = int(input("Adivinhe um numero entre 1 e 100: "))

        if resposta > numeroMisterioso:
            print("O número que estou pensando é menor")
            acerto = "Errou"
        elif resposta < numeroMisterioso:
            print("O número que estou pensando é maior")
            acerto = "Errou"
        else:
            print("Você Acertou o número !!")
            acerto = "Acertou"

    c = input("Quer mais uma rodada? (S/N) ")
