salario = float(input("Digite seu salario: "))
if salario <= 1280.00:
    porcentagem_do_aumento = 20
elif salario > 1280.00 and salario <= 1700.00:
    porcentagem_do_aumento = 15
elif salario > 1700.00 and salario <= 2500.00:
    porcentagem_do_aumento = 10
elif salario > 2500.00:
    porcentagem_do_aumento = 5
valor = (salario * (porcentagem_do_aumento / 100))
total = salario + valor
 
print("O seu salario de", (salario), "recebeu um aumento de", (porcentagem_do_aumento), "%")
print("o valor aumentado foi de: ", (total - salario), "$")
print("Seu novo salario é: ", (total), "$")