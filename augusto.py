import os

os.mkdir("Aula Python")
 
os.chdir("Aula Python")
 
arquivo = open("aula01.txt","w", encoding="utf-8")
arquivo.write("Aula sobre criar diretório",)
 
 
arquivo = open("aula02.txt","w")
arquivo.write("Aula sobre criar arquivos")
 
 
arquivo = open("aula03.txt","w")
arquivo.write("Aula sobre criar texto")