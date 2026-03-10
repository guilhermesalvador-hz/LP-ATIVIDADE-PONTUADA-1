import os

os.system("cls")

nota_um = float(input("Digite sua primeira nota: "))
nota_dois = float(input("Digite sua segunda nota: "))

media = (nota_um + nota_dois) / 2

print("Media: ", media)

if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Recuperacao")
else:
    print("Reprovado")