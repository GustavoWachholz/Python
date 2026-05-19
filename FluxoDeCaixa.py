produtos = []
precos = []
produtosSelecionados = []
quantidadesProdutosSelecionados = []
subtotaisProdutosSelecionados = []
total = 0
valorFinal = 0
formaPagamento = ""
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
    menu_pagamento = """Formas de Pagamento disponíveis:
[ 1 ] Dinheiro (12% de desconto)
[ 2 ] Pix (10% de desconto)
[ 3 ] Débito (Valor normal)
[ 4 ] Crédito (10% de acréscimo)
----------------------------------------
Digite a opção desejada: """
    menu_confirmacao = """[ 1 ] Confirmar Pagamento
[ 2 ] Selecionar nova forma de pagamento
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
            
    elif opcao == 5:
        print("\n========================================")
        print("           RESUMO DA COMPRA")
        print("========================================")
        print("QTD | PRODUTO              | SUBTOTAL")
        print("----------------------------------------")
        
        for i, produtoSelecionado in enumerate(produtosSelecionados):
            quantidade = quantidadesProdutosSelecionados[i]
            nome = produtosSelecionados[i]
            subtotal = subtotaisProdutosSelecionados[i]
            print(f"{quantidade:<3} | {nome:<20} | R$ {subtotal:.2f}")
            
        print("----------------------------------------")
        print(f"VALOR TOTAL: R$ {total:.2f}")
        print("========================================\n")
        
        while True:
            print(menu_pagamento)
            formaPagamentoSelecionada = input()
            while True:
                if formaPagamentoSelecionada == "1":
                    formaPagamento = "Dinheiro"
                    valorFinal = total * 0.88
                    break
                elif formaPagamentoSelecionada == "2":
                    formaPagamento = "Pix"
                    valorFinal = total * 0.90
                    break
                elif formaPagamentoSelecionada == "3":
                    formaPagamento = "Cartão de Débito"
                    valorFinal = total
                    break
                elif formaPagamentoSelecionada == "4":
                    formaPagamento = "Cartão de Crédito"
                    valorFinal = total * 1.1
                    break
                else:
                    print('Opção inválida, tente novamente.')
                    continue
                
            print("\n========================================")
            print("           RECIBO DE COMPRA")
            print("========================================")
            print("QTD | PRODUTO              | SUBTOTAL")
            print("----------------------------------------")
            
            for i, produtoSelecionado in enumerate(produtosSelecionados):
                quantidade = quantidadesProdutosSelecionados[i]
                nome = produtosSelecionados[i]
                subtotal = subtotaisProdutosSelecionados[i]
                print(f"{quantidade:<3} | {nome:<20} | R$ {subtotal:.2f}")
            
            print("----------------------------------------")
            print(f"Subtotal bruto:        R$ {total:.2f}")
            print(f"Forma de Pagamento:    {formaPagamento}")
            print("========================================")
            print(f"VALOR TOTAL LÍQUIDO:   R$ {valorFinal:.2f}")
            print("========================================\n")
            
            finalizar = input(menu_confirmacao)
            
            if finalizar == "1":
                produtosSelecionados.clear()
                quantidadesProdutosSelecionados.clear()
                subtotaisProdutosSelecionados.clear()
                total = 0
                valorFinal = 0
                formaPagamento = ""
                break
            elif finalizar == "2":
                valorFinal = sum(subtotaisProdutosSelecionados)
                continue
            else:
                print('Opção inválida, tente novamente.')
                continue
        break
            
    else:
        print('Opção inválida, tente novamente.')
        continue
    
print("TRANSAÇÃO FINALIZADA COM SUCESSO!")