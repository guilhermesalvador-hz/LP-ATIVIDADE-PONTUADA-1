import os 

os.system("cls")

produto = input("Nome do produto")
quantidade = int(input("Quantidade a comprar"))
preco = float(input("Preco unitario"))

total = quantidade * preco

if quantidade <= 5:
    desconto = total * 0.002
elif quantidade <= 10:
    desconto = total * 0.003
else:
    desconto = total * 0.005
    
    
total_pagar = total - desconto

print("Produto", produto)
print("Total", total)
print("Desconto", desconto)
print("Total a pagar", total_pagar)