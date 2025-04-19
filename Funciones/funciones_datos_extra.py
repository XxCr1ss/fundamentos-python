
#Creando una funcion con tres palametros 
def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

#Utilizando keyword arguments
frase_resultante = frase(apellido = "Cabrera", nombre = "Cristian", adjetivo =  "chill")
print(frase_resultante)

#Creando la misma funcion con un parametro opcional y un avalor por defecto
def frase(nombre, apellido, adjetivo = "no chill"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante = frase("Cristian", "Cabrera")
print(frase_resultante)