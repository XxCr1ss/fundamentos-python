#Creando una lista (Se pueden modificar)
lista = ["Cristian David", "Melo", True, 1.85]
print(lista)
print(lista[0])

#Modificando una lista
lista[0] = "Cabrera Pantoja"
print(lista)

#Creando una tupla (Esto no se puede modificar)
tupla = ("Cristian David", "Melo", True, 1.85)
print(tupla)
print(tupla[0])

#Esto no se puede hacer
#tupla[0] = "Cabrera Pantoja"

#Creando un conjunto (set) (No se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"Cristian David", "Melo", True, 1.85, "Cristian David"}
print(conjunto)

#Creando un diccionarios (dict) (La estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "Cristian David",
    'canal' : "CristianDC",
    'esta_emocionado' : True,
    'dato_duplicado' : "Cristian David"
}
print(diccionario)
print(diccionario['nombre'])
print(diccionario['canal'])
print(diccionario['esta_emocionado'])
print(diccionario['dato_duplicado'])
