import os

os.system("cls")

operacao = input("Digite a operacao (+,-,/<:,*)")

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))


if operacao == "+":
    resultado = a + b
elif operacao == "-":
    resultado = a - b
elif operacao == "*":
    resultado = a * b
elif operacao == "/":
    resultado = a /b
else:
    print("Operacao invalida: ")
    resultado = 0
    
if resultado != 0:
    print("Resultado", resultado)