# contador = 1
 
# while contador == 1:
 
#     print()
#     print()
 
#     nome   = input( "Nome ......: " )
#     senha  = input( "Senha .....: " )
 
#     if nome != senha:
 
#         print( "Nome difere da Senha!"  )
       
#         print()
#         print()
 
#     elif nome == senha:
 
#         contador = 2
 




# Nº Médio alunos x turma
# Input() de qtde turmas e qtde alunos de cada turma (máx 40 alunos)
 
qtos_alunos = 0
qtas_turmas = 0
 
print()
print()
 
qtas_turmas  = int(input( "Qtde turmas .....: " ))
 
contador = 0
total_alunos = 0
 
while contador < qtas_turmas:
 
    contador = contador + 1
         
    print("Turma ..........: " + str(contador))
    qtos_alunos = int(input( "Qtde alunos ....: " ))
 
    if qtos_alunos > 40:
 
        print()
        print()
 
        print("Muita gente na sala de aula!!!")
        contador = contador - 1
 
    elif qtos_alunos < 40:
 
        total_alunos = total_alunos + qtos_alunos
        qtos_alunos = 0  
 
print()
print()
 
media = total_alunos / qtas_turmas
 
print(f"Média por turma ...: {media}")
 
print()
print()
 