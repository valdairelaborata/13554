# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.



quantidade_turmas = int(input("Digite a quantidade de turma:"))
quantidade_turmas_inicial = quantidade_turmas
quantidade_total_alunos = 0

while quantidade_turmas > 0:

    quantidade_aluno = int(input(f"Digite a quantidade de alunos (turma {quantidade_turmas}): "))

    if quantidade_aluno > 0 and quantidade_aluno <= 40:            
        quantidade_turmas = quantidade_turmas - 1
        quantidade_total_alunos = quantidade_total_alunos + quantidade_aluno    
    else:
        print("As turmas não podem ter mais de 40 alunos!")

print("Todas as turmas estão com os alunos informados!")

media_alunos = int(quantidade_total_alunos/quantidade_turmas_inicial)

print(f"Número médio de alunos por turma: {media_alunos}")
