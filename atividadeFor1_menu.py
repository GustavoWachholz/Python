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

    adicionar = input("Quer adicionar mais um produto? sim ou não: \n")

    if adicionar == "sim":
        adicionarProduto = True
    else:
        adicionarProduto = False

for indice, produto in enumerate(produtos):

    mensagem = f"""    ----------------------
    Produto: {produtos[indice]}
    Quantidade: {quantidades[indice]}
    Valor unitário: {precos[indice]}
    Subtotal: {subtotais[indice]}"""

    print(mensagem)

    valorTotal = sum(subtotais)

print(f"\nO valor total da compra foi de R$ {valorTotal}")