import os

os.system

nome = input("Digite o nome: ")
sexo = input("DIgite o sexo (M/F): ")
estado_civil = input("Digite o estado civil: ")

tempo_casada = ""
if sexo.upper() == "F" and estado_civil.upper() == "Casada":
    tempo_casada = input("Digite o tempo de casada em anos: ")
    
print("====== Dados do usuario =====")
print("Nome:", nome)
print("Sexo:", sexo)  
print("Estado civil:", estado_civil)

if tempo_casada != "":
    print("Tempo de casado: ",tempo_casada, "anos")
    
    
    