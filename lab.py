# 1)	Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def numero (a):
    if a > 0:
        return "P"
    else:
        return "N"
 
x = float(input("digite um numero positivo ou negativo: "))
print(numero(x))


# 2)	Faça uma função anônima que informe a quantidade de dígitos de um determinado número inteiro informado.

digitos = lambda a: len(str(abs(a)))
 
numero = int(input("digite um numero: "))

print(digitos(numero))


# 3)	Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos. 

