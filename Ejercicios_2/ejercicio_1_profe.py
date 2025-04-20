
#El profesor faltó a clases, por lo que el profesor será el mayor y el asistente el menor de los compañeros

#Pedir el nombre de los compañeros y devolver el profesor y el asistente
def obtenerCompañeros(cantidad_compañeros):
    compañeros = []
    for i in range(cantidad_compañeros):
        nombre = input("Dame el nombre: ")
        edad = int(input("Dame la edad: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x: x[1])
    profesor = compañeros[-1]
    asistente = compañeros[0]
    return profesor, asistente

#Llamamos a la función y desempaquetamos los valores
profesor, asistente = obtenerCompañeros(4)

#Mostramos la respuesta
print(f"El profesor es {profesor[0]} y tiene {profesor[1]} años, el asistente es {asistente[0]} y tiene {asistente[1]} años")
