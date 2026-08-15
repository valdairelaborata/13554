

try:
    numero = int(input("Digite um número inteiro: "))
    print(1 / numero)
except ZeroDivisionError:
    print("Infinito")
except ValueError:
    print("Entrada inválida")
except Exception:
    print("Ocoreu um erro")
 