
# a = 10

# if a > 0:
#     print(a)


# texto = "Vovó foi a feira"

# numero = int(texto)

# arquivo = open("teste.txt","r")

try:
    arquivo = open("teste.txt","r")
except:
    arquivo = open("teste.txt","w")
finally:
    arquivo.close()


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