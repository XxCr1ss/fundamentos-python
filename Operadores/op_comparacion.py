esIgualQue = 5 == 6

esDistintoQue = 5 != 6

mayorQue = 5 > 6

menorQue = 5 < 6

mayorOIgual = 5 >= 6

menorOIgual = 5 <= 6

#Imprimimos nuestros datos
miLista = [esIgualQue, esDistintoQue, mayorQue, menorQue, mayorOIgual, menorOIgual]
for i in miLista:
    print(i)

#Calculos combinados

a = 5
b = 10 
c = 20
comparacion = a + b < c
print(comparacion)

#Compara usuarios
usuarioDeBasesDeDatos = "Cristian David"
usuarioEscrito = "David Cristian"
print(usuarioDeBasesDeDatos == usuarioEscrito)
nuevoUsuarioEscrito = "Cristian David"
print(nuevoUsuarioEscrito == usuarioDeBasesDeDatos)
