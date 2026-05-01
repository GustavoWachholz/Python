import math

nome = input("Digite o seu nome: ")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

media = round((nota1 + nota2 + nota3) / 3, 1)

print(f"Sua média foi: {media}")
if media >= 7:
    print(f"Parabéns, {nome}, você foi aprovado!. Sua média foi {media}")

elif media < 7 and media >= 5:
    print("Recuperação")
    notaRecuperacao = float(input("Digite a nota da recuperação:"))
    mediaFinal = (media + notaRecuperacao) / 2
    if mediaFinal >= 5:
        print("Aprovado")

    else:
        print("Reprovado")

else:
    print("Reprovado!")
