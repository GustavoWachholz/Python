valor = float(input("Digite o valor do pedido: "))

if valor <= 100:
    print(f"O valor da compra foi de R$ {valor}, não tendo desconto aplicávell.")
    exit()

elif valor > 100 and valor < 300:
    desconto = 0.90

else:
    desconto = 0.85
    
total = valor * desconto
percentualDesconto = (1 - desconto) * 100
print(f"O valor total da compra foi de R$ {round(valor, 2)}. \nValor total foi de: R$ {round(total, 2)}. \nO deconto foi de: {round(percentualDesconto)}%")