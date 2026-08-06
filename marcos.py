#salario = float() - recebe o valor do salario
#percent = float() - de acordo com a faixa do salário, recebe a porcentagem
#new_salario = float() - é o salário + o acréscimo
 
 
salario = float( input( "Qual é o salário? R$ " ) )
 
if   salario  <=  1280.00:
     percent   =  1.20
elif salario   >  1280.00   and  salario  <=  1700.00:
     percent   =  1.15
elif salario   >  1700.00   and  salario  <=  2500.00:
     percent   =  1.10
elif salario   >  2500.00:
     percent   =  1.05
 
new_salario = salario + (salario * percent )    
diferenca   = new_salario - salario
 
print()
print()
print( "O acréscimo será de ...: R$ " + str(  ( percent * 100 ) - 100    ) + " %" )
print( "O novo salário será ...: R$ " + str(    new_salario              )        )
print( "A diferença será de ...: R$ " + str(    new_salario-salario      )        )
print()
print()
 
print( f"Parabéns pelo aumento de R$ {new_salario - salario} !!!" )
print()
 
 