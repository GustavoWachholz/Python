produtos = []
precos = []
quantidades = []
subtotais = []

adicionarProduto = True

while adicionarProduto:
    produto = input("Insira um produto: \n")
    produtos.append(produto)
    print(f"Insira o preco do produto {produto}")
    preco = float(input())
    precos.append(preco)
    print(f"Insira a quantidade do produto {produto}")
    quantidade = int(input())
    quantidades.append(quantidade)
    subtotal = float(preco * quantidade)
    subtotais.append(subtotal)

    menu = """
    O que você quer fazer agora?
    1 - Adicionar um novo produto
    2 - Mostrar subtotal
    3 - Mostrar total parcial
    4 - Finalizar compra
    """
    print(menu)
    acao = input()

    while True:
        if acao == "1":
            adicionarProduto = True
            break
        elif acao == "2":
            print(f"O subtotal do produto é de R$ {subtotal}")
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