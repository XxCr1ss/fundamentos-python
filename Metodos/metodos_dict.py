diccionario = {
    "nombre" : 'Cristian',
    "apellido" : 'Carbera',
    "pajas" : 100000 
}

#Devuelve un objeto dict_item (Tambien nos sirve para iterar)
claves = diccionario.keys()

#Obteniendo un elemento con get() (No me lanza una excepcion y si no encuentra nada el programa continua)
valorDeLaClave = diccionario.get("nombre")

#Eliminando todo el diccionario
#diccionario.clear()

#Eliminando un elemento del diccionario
#diccionario.pop("nombre")

#Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)