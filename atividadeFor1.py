produtos = ['Caderno', 'Caneta', 'Lapis', 'Borracha', 'Régua', 'Apontador']
precos = [10.00, 1.99, 1.49, 0.50, 4.00, 5.00]
quantidades = [2, 1, 2, 1, 2, 1]
subtotais = []

for indice, produto in enumerate(produtos):
    subtotal = precos[indice] * quantidades[indice]
    subtotais.append(subtotal)

    mensagem = f"""    ----------------------
    Produto: {produtos[indice]}
    Quantidade: {quantidades[indice]}
    Valor unitário: {precos[indice]}
    Subtotal: {subtotal}"""

    print(mensagem)

valorTotal = sum(subtotais)

print(f"\nO valor total da compra foi de R$ {valorTotal}")