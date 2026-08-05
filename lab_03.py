# 1 - Criar um dicionário que armazene informações sobre uma pessoa (nome, idade, e cidade) e exiba essas informações.

# pessoa = {
#     "nome": "Fulano de Tal",
#     "idade": 25,
#     "cidade": "Curitiba"
# }

# print("Nome: ", pessoa["nome"], " ", pessoa["idade"], " ", pessoa["cidade"])



# 2 - Criar um dicionário que contenha outros dicionários como valores e acessar os elementos.

turma = {
    "aluno1":{
        "nome": "Aluno 01",
        "media": 8
    },
    "aluno2":{
        "nome": "Aluno 02",
        "media": 7
    },
    "aluno3":{
        "nome": "Aluno 03",
        "media": 9
    }
}

# print(turma["aluno2"]["nome"])


 
frutas = {
    "banana" : 1,
    "laranja" : 3,
    "maçãs" : {"gala" : 2,
             "fuji" : 1,
             "verde" : 4,
              "medida": "Unidade" }}
 
print(frutas)
 

