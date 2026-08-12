arquivo = open("ips.txt", "r")
conteudo = arquivo.read()
arquivo.close()
 
 
arquivo = open("ip.txt", "w")
arquivo.write("[Endereços validos:]\n 200.135.80.9\n 192.168.1.1\n 8.35.67.74\n 257.32.4.5\n")
arquivo.write("\n[Endereços invalidos:]\n 85.345.1.2\n 1.2.3.4\n 9.8.234.5\n 192.168.0.256\n")
arquivo.close()