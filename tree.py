import os 

os.system("cls")

a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))

if a == b:
    c = a + b
else:
    c= a * b
    
print("Valor de c:", c)