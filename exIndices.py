frutas = []

repeticoes = int(input("Quantas frutas você quer inserir?"))

for fruta in range(repeticoes):
    fruta = input("Digite o nome da fruta:")
    frutas.append(fruta)

for fruta in frutas:
    print(fruta)