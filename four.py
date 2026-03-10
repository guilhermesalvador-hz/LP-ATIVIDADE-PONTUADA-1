import os 

os.system("cls")

morango = float(input("Quantidade de morangos (KG): "))
maca = float(input("Quantidade de macas (KG) : "))

if morango <= 5:
    preco_morango = morango * 2.50
else:
    preco_morango = morango * 2.20
    
if maca <= 5:
        preco_morango = maca * 1.80
else:
    preco_maca = maca * 1.50   
    
    
total_kg = morango + maca
total = preco_morango + preco_maca

if total_kg >= 10 or total > 15:
    total = total * 0.9
    
print("Valor total a pagat: R$", total)

