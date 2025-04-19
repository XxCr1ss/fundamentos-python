
#Creando diccionarios con dict()
diccionario = dict(nombre="Cristian", apellido="Cabrera")

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Cristian", "Puerro"]): "xd"}

#Creando diccionarios con frontkeys() valor por defecto : none
diccionario = dict.fromkeys(["nombre", "apellido", "subscrictores"])
print(diccionario)

#Creando diccionarios con frontkeys() cambiando el valor por defecto a "No sé"
diccionario = dict.fromkeys(["nombre", "apellido", "subscrictores"], "No sé")
print(diccionario)
