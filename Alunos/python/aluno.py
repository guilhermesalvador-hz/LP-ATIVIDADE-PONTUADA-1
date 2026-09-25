from dataclasses import dataclass


@dataclass
class Aluno:
    nome: str
    idade: int
    curso: str

    
    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Curso: {self.curso}")


nome_input = input("Digite o nome do aluno: ")
idade_input = int(input("Digite a idade do aluno: "))
curso_input = input("Digite o curso do aluno: ")


aluno1 = Aluno(nome=nome_input, idade=idade_input, curso=curso_input)


print("\nInformações do aluno:")
aluno1.mostrar_informacoes()

@dataclass
class Professor:

    nome: str
    idade: int
    disciplina: str

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Disciplina: {self.disciplina}")

nome_professor = input("Digite o nome do professor: ")
idade_professor = int(input("Digite a idade do professor: "))
disciplina_professor = input("Digite a disciplina do professor: ")

professor1 = Professor(nome=nome_professor, idade=idade_professor, disciplina=disciplina_professor)

print("\nInformações do professor:")
professor1.mostrar_informacoes()


