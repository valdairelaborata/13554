# 1) Faça um programa que receba uma letra e verifique se esta é vogal ou consoante.

letra = input("A: ").lower()

vogais = ["a", "e", "i", "o", "u"]
 
if letra in vogais:
    print("É uma vogal")
else:
    print("É uma consoante")