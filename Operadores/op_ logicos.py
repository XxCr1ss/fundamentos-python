#AND
Resultado = True & True #Dovolver True
Resultado2 = False & False #Dovolver False
Resultado3 = True & False #Dovolver False
Resultado4 = False & True #Dovolver False

#OR
Resultado5 = True | True #Dovolver True
Resultado6 = False | False #Dovolver False
Resultado7 = True | False #Dovolver True
Resultado8 = False | True #Dovolver True

#NOT
Resultado9 = not True  #Dovolver False
Resultado10 = not False #Dovolver True

#Imprimimos nuestros datos
miLista = [Resultado, Resultado2, Resultado3, Resultado4, Resultado5, Resultado6, Resultado7, Resultado8, Resultado9, Resultado10]
for i in miLista:
    print(i)
