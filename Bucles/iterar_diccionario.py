
diccionario = {
    "nombre": "Cristian",
    "apellido": "Cabrera",
    "subs": 10000
}

#Obteniendo los valores de un diccionario
for key in diccionario:
    print(diccionario[key])

#Recorriendo el diccionario para obtener la clave 
for key in diccionario:
    print(f"La clave es: {key}")
    
#Recorriendo el diccionario con items() para obtener la clave y el valor 
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor es {value}")
