contador = 1
 
while contador == 1:
 
    print()
    print()
 
    nome   = input( "Nome ......: " )
    senha  = input( "Senha .....: " )
 
    if nome != senha:
 
        print( "Nome difere da Senha!"  )
       
        print()
        print()
 
    elif nome == senha:
 
        contador = 2
 