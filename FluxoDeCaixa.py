produtos = []
precos = []
produtosSelecionados = []
quantidadesProdutosSelecionados = []
subtotaisProdutosSelecionados = []
total = 0
while True:
    menu = """========================================
                 MENU
========================================
[ 1 ] Cadastrar Produto
[ 2 ] Visualizar Produtos
[ 3 ] Criar Carrinho
[ 4 ] Visualizar Carrinho
[ 5 ] Finalizar Compra
[ 0 ] Sair
----------------------------------------
Digite a opção desejada: """
    opcao = input(menu)
    opcao = int(opcao)

    if opcao == 1:
        while True:
            nome = input('Digite o nome do produto: ')
            produtos.append(nome)
            preco = float(input('Insira o preço do produto: '))
            precos.append(preco)
        
            novoProduto = input("Deseja inserir um novo produto? S ou N: ")
            
            if novoProduto == "S":
                continue
            else:
                break
        
    elif opcao == 2:
        print("\n========================================")
        print("          CATÁLOGO DE PRODUTOS")
        print("========================================")
        print("CÓDIGO | NOME                 | PREÇO")
        print("----------------------------------------")

        for i, produto in enumerate(produtos):
            nome = produtos[i]
            preco = precos[i]
            print(f"[{i}]    | {nome:<20} | R$ {preco:.2f}")
    elif opcao == 3:
        while True:
            print("\n========================================")
            print("          CATÁLOGO DE PRODUTOS")
            print("========================================")
            print("CÓDIGO | NOME                 | PREÇO")
            print("----------------------------------------")

            for i, produto in enumerate(produtos):
                nome = produtos[i]
                preco = precos[i]
                print(f"[{i}]    | {nome:<20} | R$ {preco:.2f}")
                
            codigoProduto = int(input("Selecione o código do produto: "))
            quantidadeProduto = int(input("Informe a quantidade do produto: "))
            
            produtosSelecionados.append(produtos[codigoProduto])
            quantidadesProdutosSelecionados.append(quantidadeProduto)
            subtotaisProdutosSelecionados.append(quantidadeProduto * precos[codigoProduto])
            
            novoProduto = input("Deseja inserir um novo produto? S ou N: ")
            
            if novoProduto == "S":
                continue
            else:
                total = sum(subtotaisProdutosSelecionados)
                break
            
    elif opcao == 4:
        print("\n========================================")
        print("          CATÁLOGO DE PRODUTOS")
        print("========================================")
        print("CÓDIGO | NOME                 | PREÇO")
        print("----------------------------------------")

        for i, produtoSelecionado in enumerate(produtosSelecionados):
            nome = produtosSelecionados[i]
            subtotalProdutoSelecionado = subtotaisProdutosSelecionados[i]
            print(f"[{i}]    | {nome:<20} | R$ {subtotalProdutoSelecionado:.2f}")
            
    #elif opcao == 0:
    #else:
    #    print('Opção inválida, tente novamente.')
        continue