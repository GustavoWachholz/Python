produtos = []
precos = []
quantidades = []
subtotais = []

adicionarProduto = True

while adicionarProduto:
    menu = """
    O que você quer fazer agora?
    1 - Adicionar um novo produto
    2 - Mostrar lista de produtos
    3 - Mostrar valor total do carrinho
    4 - Finalizar compra
    """
    print(menu)
    acao = input()

    while True:
        if acao == "1":
            produto = input("Insira um produto: \n")
            produtos.append(produto)
            print(f"Insira o preco do produto {produto}:")
            preco = float(input())
            precos.append(preco)
            print(f"Insira a quantidade do produto {produto}:")
            quantidade = int(input())
            quantidades.append(quantidade)
            subtotal = float(preco * quantidade)
            subtotais.append(subtotal)
            break
        elif acao == "2":
            for indice, produto in enumerate(produtos):
                print(f"Produto: {produtos[indice]} - Subtotal: R$ {precos[indice] * quantidades[indice]}")
        elif acao == "3":
            print(f"O total da compra até o momento é de R$ {sum(subtotais)}")
        elif acao == "4":
            adicionarProduto = False
            break
        else:
            print("Opção inválida, tente novamente")
        
        print(menu)
        acao = input()


for indice, produto in enumerate(produtos):

    mensagem = f"""    ----------------------
    Produto: {produtos[indice]}
    Quantidade: {quantidades[indice]}
    Valor unitário: {precos[indice]}
    Subtotal: {subtotais[indice]}"""

    print(mensagem)

    valorTotal = sum(subtotais)

print(f"\nO valor total da compra foi de R$ {valorTotal}")