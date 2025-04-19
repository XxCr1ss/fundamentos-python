animales = {"gato", "perro", "loro", "cocodrilo"}
numeros = {52, 16, 14, 72}

#Recorriendo la conjunto animales
for animal in animales:
    print(f"Ahora la variable es {animal}")

#Recorreiendo la conjunto numeros y multiplicamos por 10 
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#Recorriendo dos conjuntos al mismo tiempo
for numero, animal in zip(animales, numeros):
    print(f"Recorriendo conjunto 1: {animales}")
    print(f"Recorriendo conjunto 2: {animal}")

#Forma correcta de recorrer una conjunto por su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es {indice} y elvalor es {valor}')

#Forma practica y elegante
for num,i in enumerate(numeros):
    print(f'El indice es {num} y elvalor es {i}')

#Usando el for/ else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle termino")

#Todo lo anterior funciona exactamente igual con conjuntos y tuplas
