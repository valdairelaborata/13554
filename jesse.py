# usuario = input("digite o seu usuario: ")
# senha = input("digite sua senha: ")
# while senha == usuario:
#     print("usuario e senha não pode ser iqual")
 
#     usuario = input("digite o seu usuario: ")
#     senha = input("digite sua senha: ")
# print("aprovado")  

while True:
    alunos_quantidades = int(input("informe a quantidades de alunos: "))
    turma_quantidades = int(input("informe a quantidades de turma: "))
    media = (alunos_quantidades / turma_quantidades)
    if media > 40:
        print("não pode passar de 40")
    else:
        print(f'você digitou {turma_quantidades} turma! Cada turma terá {media:.0f} alunos')
    break
 