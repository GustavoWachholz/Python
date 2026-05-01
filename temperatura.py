temperatura = int(input("Gidite a temperatura atual:"))

if temperatura <= 15:
    print("Está frio, ligar aquecedor")

elif temperatura > 15 and temperatura < 25:
    print("Agradável")

else:
    print("Calor, ligar o ar condicionado")