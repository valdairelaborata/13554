# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário. Mostre uma mensagem de erro e volte a pedir as informações.

usuario = " "
senha = " "

contador = 0

while senha == usuario:  

    if contador > 0:
        print("usuario e senha não pode ser iqual")
 
    usuario = input("digite o seu usuario: ")
    senha = input("digite sua senha: ")   
    contador = contador + 1


print("aprovado")  