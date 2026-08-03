pessoa1 = input("Nome da primeira pessoa:")
idade1 = int(input("Informe a idade da primeira pessoa:"))

pessoa2 = input("Nome da segunda pessoa:")
idade2 = int(input("Informe a idade da segunda pessoa:"))

print(pessoa1, " é mais velho que ", pessoa2, " ?", idade1 > idade2  )
print("Possuem a mesma idade? ", idade1 == idade2)

ambos_maior_idade = (idade1 >= 18) and (idade2 >= 18) 

print("Ambos são maior de idade?: ", ambos_maior_idade)