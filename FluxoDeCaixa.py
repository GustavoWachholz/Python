produtos = []
precos = []
quantidades = []
subtotais = []
while True:
    menu = """========================================
                 MENU
========================================
[ 1 ] Cadastrar Produto
[ 2 ] Visualizar Produtos
[ 3 ] Criar Carrinho
[ 4 ] Finalizar Compra
[ 0 ] Sair
----------------------------------------
Digite a opção desejada: """
    opcao = input(menu)
    opcao = int(opcao)

    if opcao == 1:
        nome = input('Digite o nome do produto: ')
        produtos.append(nome)
        preco = float(input('Insira o preço do produto: '))
        precos.append(preco)
    elif opcao == 2:
        print("\n========================================")
        print("          CATÁLOGO DE PRODUTOS")
        print("========================================")
        print("CÓDIGO | NOME                 | PREÇO")
        print("----------------------------------------")

        for i in enumerate(produtos):
            nome = produtos[i]
            preco = precos[i]
            print(f"[{i}]    | {nome:<20} | R$ {preco:.2f}")
    elif opcao == 3:
        print("\n========================================")
        print("          CATÁLOGO DE PRODUTOS")
        print("========================================")
        print("CÓDIGO | NOME                 | PREÇO")
        print("----------------------------------------")

        for i in enumerate(produtos):
            nome = produtos[i]
            preco = precos[i]
            print(f"[{i}]    | {nome:<20} | R$ {preco:.2f}")

        
    elif opcao == 4:
    elif opcao == 0:
    else:
        print('Opção inválida, tente novamente.')
        continue