# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário. Mostre uma mensagem de erro e volte a pedir as informações.

usuario = " "
senha = " "

while senha == usuario:  

    usuario = input("digite o seu usuario: ")
    senha = input("digite sua senha: ")   
    if usuario == senha:
        print("ERRO: A senha deve ser diferente do nome de usuário.")


print("aprovado")  