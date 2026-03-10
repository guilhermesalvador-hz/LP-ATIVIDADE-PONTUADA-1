import os

os.system

a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

soma = a + b

if soma < c:
    print("A soma de a + b e menor que c")
else:
    print("A soma de a + b e maior que c")