# usuario = input("Digite o nome de usuário: ")
# senha = input("Digite a senha: ")
 
# while senha == usuario:
#     print("ERRO: A senha não pode ser igual ao nome de usuário. Tente novamente.")
#     usuario = input("Digite o nome de usuário: ")
#     senha = input("Digite a senha: ")
 
# print("Cadastro realizado com sucesso!")

 
turmas = int(input("Quantidade de turmas?:"))
alunos = int(input("Quantidade de alunos por turma?:"))

media = alunos / turmas
print(media)