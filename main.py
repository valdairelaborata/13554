
import os


# ambiente = os.getcwd()

# ambiente = os.listdir()


# inicio = os.getcwd()

# for root, dirs, files in os.walk(inicio):
#     print("Root " + str(root))
#     print("Dirs " + str(dirs))
#     print("Files " + str(files))



# ambiente = os.getcwd()
# print("Inicial " + str(ambiente))

# os.chdir("lab")

# os.mkdir("exercicios")

# os.chdir("exercicios")

# os.makedirs("lab/exercicios")

# os.chdir("lab")
# os.rmdir("exercicios")

# os.removedirs("lab/exercicios")


# ambiente = os.getcwd()
# print("Final " + str(ambiente))




# script = __file__

# print(script)

# base = os.path.basename(__file__)

# print(base)

# base = os.path.dirname(__file__)

# print(base)

base = os.path.abspath(__file__)

print(base)