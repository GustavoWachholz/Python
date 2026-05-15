executar = True
numeros = []
while executar:
    while True:
        numero = input("Digite um número. Digite 0 para parar: ")
        if numero != "":
            numero = int(numero)
            if numero != 0:
                numeros.append(numero)
            else:
                break
        else:
            print("É necessário digitar um número")

    print(f"Quantidade de números digitados: {len(numeros)}")
    for indice, numero in enumerate(numeros):
        print(numeros[indice])
    
    input("Tecle enter para continuar")
    
    while True:
        tentarNovamente = input("Deseja fazer novamente? (s ou n): ")

        if tentarNovamente == "s":
            break
        elif tentarNovamente == "n":
            executar = False
            break
        else:
            print("Opção inválida, insira uma opção válida.")