import os

os.system("cls")

cor = input("Digite a cor do CD (verde, azul, amarelo, vermelho: ")

if cor.lower() == "verde":
    preco = 10
elif cor.lower() == "azul":
    preco = 20
elif cor.lower() == "vermelho":
    preco = 30
elif cor.lower() == "amarelo":
    preco = 40
else:
    preco = 0
    print("cor invalida")
    
if preco != 0:
    print("Preco do CD R$", preco)