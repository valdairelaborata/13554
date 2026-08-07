usuario = input("Usuario:")
senha = input("insira sua senha:")
 
if senha == usuario:
    while usuario != senha:
        print("ERRO: senha deve ser diferente do usuario")
 
else:
    print("senha aceita")