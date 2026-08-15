# Utilizando tratamento de exceções, crie um programa que, dado um valor inteiro informado pelo usuário, retorne a divisão de 1 por este. Se o valor informado for zero, o programa deve informar “Infinito” como resultado.        


a = 0
try:
    divisao = 1 / int(a)

except TypeError:
    print("Valor não pode ser utilizado numa expressão com tipos incompatíveis")
except ValueError:
    print("Valor não pode ser convertido!")
except ZeroDivisionError:
    print("Não da pra dividir por zero(0)")
except Exception:
    print("Ocorreu um erro")