#Creando una lista con list
lista = list(["hola", "Cristian", 34])

#Devuelve la cantidad de elementos de la lista
cantidadElementos = len(lista)

#Agregando un elemento a la lista
lista.append("JAJAJAJ")

#Agregando un elementos a la lista en un indice especifico
lista.insert(2, "Toma mama")

#Agregtando varios elementos a la lista
lista.extend([False, 2023])

#Eliminando un elemento de la lista (Por indice)
lista.pop(-1) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo, y asi

#Removiendo un elemento de la lista por su valor
lista.remove("Toma mama")

#Eliminando todos los elementos de la lista
#lista.clear()

#Ordenando una lista de forma ascendente (Si usamos el parametro reverse=True lo ordena en reversa)
listaN = [3, 35, 23523, 4, 56]
listaN.sort()

#Invirtiendo los elementos de una lista
lista.reverse()

#Verificando si un elemento se envuentra en la lista devolviendo su posicion
elementoEcontrado = lista.index("Cristian")

print(elementoEcontrado)