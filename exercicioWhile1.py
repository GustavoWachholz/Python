idade = int(input("Insira uma idade entre 0 e 120: "))

while idade < 0 or idade > 120:
    idade = int(input("Idade inválida, insira novamente: "))

print(idade)