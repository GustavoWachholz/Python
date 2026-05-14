import random

numero_secreto = random.randint(1, 10)
palpite = 0
tentativas = 0
tentativas_restantes = 3

while palpite != numero_secreto:
    palpite = int(input("Insira um número de 1 a 10: "))
    if palpite != numero_secreto:
        print("Errou, tente novamente")
        tentativas_restantes -= 1
        if tentativas_restantes == 0:
            break
    tentativas += 1
    
if tentativas_restantes > 0:
    print(f"Você acertou em {tentativas} tentativa(s)!")
else:
    print("Tentativas esgotadas!")