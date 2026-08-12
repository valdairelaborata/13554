# def V_numero(valor):
#     """Função que recebe e retorna um número:
#         'P' se o número for positivo
#         'N' se for zero ou negativo"""
#     if valor > 0:
#         return 'P'
#     else:
#         return 'N'

    
# numero = int(input("Digite um número: "))
# resultado = V_numero(numero)
# print(f"O resultado é: {resultado}")



# Faça uma função anônima que informe a quantidade de dígitos de um determinado número inteiro informado.

# digitos = lambda numero: len(str(abs(numero)))

# numero = int(input("Digite um número inteiro: "))

# print(f"O número {numero} possui {digitos(numero)} dígito(s).")


def numeros(*args):
    """Função que soma três números."""
    return sum(args)


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
 
resultado = numeros(numero1,  numero3)
 
print(f"A soma dos três números é: {resultado}")

 