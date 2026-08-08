# Dada a String “Houveram 12325 visitantes ontem.”, crie uma nova lista contendo apenas os dígitos.


texto = "Houveram 12325 visitantes ontem"

digitos = [char for char in texto if char.isdigit()]

print(digitos)