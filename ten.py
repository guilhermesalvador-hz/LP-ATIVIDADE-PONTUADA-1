import os

os.system("cls")

litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustivel (A-alcool / G-gasolina)")

if tipo.upper () == "a":
    preco = 3
    
    incompleto