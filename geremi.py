salario = float(input("Digite o seu  salario:"))
 
if salario <= 1280.00:
    porcentagem = 1.20
elif salario <= 1700.00:
    porcentagem = 1.15
elif salario <=2500.00:
    porcentagem = 1.10
else:
    porcentagem = 1.05
 
valor = salario*porcentagem 
valor_a = valor - salario
porcen = (porcentagem - 1) *100
 
print(f"O seu antigo salário era R$ {salario:.2f} e com o reajuste de {porcen:.0f}% ficaria R$ {valor:.2f}")
print(f"valor acrecentado foi de: R$ {valor_a:.2f}")