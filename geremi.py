# usuario = ""
# senha = ""
 
# while usuario == senha:
#     usuario = input("Digite o nome de usuário: ")
#     senha = input("Digite a senha: ")
 
#     if usuario == senha:
#         print("ERRO: A senha deve ser diferente do nome de usuário.")
 
# print("Senha aceita!")

turmas = int(input("Digite quantas turmas você tem este ano escolar:"))
 
 
while turmas:
    alunos = int(input("Digite quantos alunos tem esta turma: "))
 
media_de_alunos = alunos / turmas
 
print(f"o numero de alunos em cada turma é de {media_de_alunos}")