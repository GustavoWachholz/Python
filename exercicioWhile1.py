while True:
    idade = int(input("Digite uma idade entre 0 e 120: "))
    
    if idade < 0 or idade > 120:
        continue
    else:
        print(idade)
        break