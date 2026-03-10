import os 

os.system("cls")

renda = float(input("Digite sua renda mensal: "))
emprestimo = float(input("Digite o valor do emprestimo: "))
prestacoes = int(input("Digite o numero de prestacoes: "))

prestacao = emprestimo / prestacoes

limite_emprestimo = renda * 10
limite_pretacao = renda * 0.30

if emprestimo <= limite_emprestimo and prestacao <=limite_pretacao:
    print("Emprestimo pode ser concedido")
else:
    print("Emprestimo nao pode ser concedido")