
# Dado um arquivo com uma lista de IPs, gere um segundo arquivo separando os IPs válidos dos inválidos.

arquivo = open("ips.txt","r")
lista_ips = arquivo.readlines()
arquivo.close()

lista_ips_invalidos = ["257.32.4.5\n", "85.345.1.2\n", "192.168.0.256"]

lista_ips_validos = []


for linha in lista_ips:
    if linha in lista_ips_invalidos:
        continue
    else:
        lista_ips_validos.append(linha)



ips_resultado = open("ips_resultado.txt", "w", encoding="utf-8")
ips_resultado.write("[ Endereços válidos:]\n")

for ip in lista_ips_validos:
    ips_resultado.write(ip)

ips_resultado.write("\n")
ips_resultado.write("\n")

ips_resultado.write("[ Endereços inválidos:]\n")

for ip in lista_ips_invalidos:
    ips_resultado.write(ip)


ips_resultado.close()

