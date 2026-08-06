# Lab 2
# 2) Faça um programa que dado o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

# a) Salários até R$ 1280,00 (incluindo) : aumento de 20%
# b) Salários entre R$ 1280,00 e R$ 1700,00 : aumento de 15%
# c) Salários entre R$ 1700,00 e R$ 2500,00 : aumento de 10%
# d) Salários de R$ 2501,00 em diante : aumento de 5% 
# Após o aumento ser realizado, informe na tela:
# a) O salário antes do reajuste;
# b) O percentual de aumento aplicado;
# c) O valor do aumento;
# d) O novo salário, após o aumento.


salario_atual = float(input("Digite o seu  salario:"))

porcentagem_do_aumento = None

if salario_atual <= 1280.00:
    porcentagem_do_aumento = 1.20
elif salario_atual <= 1700.00:
    porcentagem_do_aumento = 1.15
elif salario_atual <= 2500.00:
    porcentagem_do_aumento = 1.10
else:
    porcentagem_do_aumento = 1.05    

valor_do_novo_salario = salario_atual * porcentagem_do_aumento
valor_do_aumento = valor_do_novo_salario - salario_atual
percentual_de_aumento = int((porcentagem_do_aumento - 1) * 100)

print(f"O salário antes do reajuste: {salario_atual}")
print(f"O percentual de aumento aplicado: {percentual_de_aumento}")
print(f"O valor do aumento {valor_do_aumento}")
print(f"O novo salário, após o aumentoo {valor_do_novo_salario}")

