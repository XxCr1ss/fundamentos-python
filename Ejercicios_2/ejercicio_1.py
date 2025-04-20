# Pedimos la edad de los compañeros al usuario
compañerosNombres = input("Dame los nombres de los compañeros que vinieron a clase: ")
compañerosEdades = input("Dame las edades de los compañeros que vinieron a clase: ")

# Agregamos los valores a listas
compañerosNombres = compañerosNombres.split(", ")
compañerosEdades = compañerosEdades.split(", ")

# Pasamos las edades a enteros
compañerosEdades = [int(compañero) for compañero in compañerosEdades]

# Creamos tuplas de los compañeros
compañeros = []
for i, nom in enumerate(compañerosNombres):
    nombre = nom
    edad = compañerosEdades[i]
    compañero = nombre, edad
    compañeros.append(compañero)

# Ordenamos según la edad
compañeros.sort(key=lambda x: x[1])

# Obtenemos al profesor y el asistente
profesor = compañeros[-1]
asistente = compañeros[0]

# Mostramos la respuesta
print(
    f'El profesor es {profesor[0]} y tiene {profesor[1]} años, '
    f'el asistente es {asistente[0]} y tiene {asistente[1]}'
)
