print("Insirao nome da primeira pessoa: ")
nome01 = str(input())
print("Informe a idade:")
idade01 = int(input())
 
print("Insirao nome da segunda pessoa: ")
nome02 = str(input())
print("Informe a idade:")
idade02 = int(input())
 
maior = idade01 > idade02
iguais = idade01 == idade02
maior_idade = idade01 & idade02 >= 18
 
 
print(nome01, " e Maior que ", nome02, "?" , bool(maior))
print("Possuem a mesma idade? ",  bool(iguais))
print("Ambos são maiores de idade? " , bool(maior_idade))