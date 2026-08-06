salario = float(input("Digite seu salario: "))
if salario <= 1280.00:
    porcentagem = 20
    total = valor = (salario * (porcentagem / 100))
    Tot = salario + valor
elif salario <= 1700.00:
    porcentagem = 15
    total = valor = (salario * (porcentagem / 100))
    Tot = salario + valor
elif salario <= 2500.00:
    porcentagem = 10
    total = valor = (salario * (porcentagem / 100))
    Tot = salario + valor
else :
    porcentagem = 5
    total = valor = (salario * (porcentagem / 100))
    Tot = salario + valor
print(Tot)