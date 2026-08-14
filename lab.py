# Crie um diretório e nele crie 3 arquivos .txt. 


import os
os.makedirs("diretorio")

os.chdir("diretorio")

arquivo_01 = open("arquivo_01.txt", "w")
arquivo_01.close()

arquivo_02 = open("arquivo_02.txt", "w")
arquivo_02.close()

arquivo_03 = open("arquivo_03.txt", "w")
arquivo_03.close()
