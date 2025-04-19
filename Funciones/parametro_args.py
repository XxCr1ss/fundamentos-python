
#Forma no optima de sumar valores 
def suma(lista):
    numerosSumados = 0
    for numero in lista:
        numerosSumados += numero 
    return numerosSumados

resultado = suma([5, 3, 9])
print(resultado)

#Forma optima de sumar valores 
def suma(numeros):
    return sum([*numeros])

resultado = suma([5, 3, 9])
print(resultado)

#Lo mismo de arriba, pero utilizando el operador * como argumento (*args)
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es {sum(numeros)}"

resultado = suma("Cristian", 5, 3, 9)
print(resultado)