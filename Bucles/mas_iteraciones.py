
#Creando las listas
frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = "Soy Cristian"
numeros = [2, 5, 8, 10]

#Evitando que se coma una manzana ocn la sentencia continue
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"me voy a comer una{fruta}")

#Evitar que elbucle siga ejecutandose (El else no se ejecuta)
for fruta in frutas:
    print(f"me voy a comer una{fruta}")
    if fruta == "pera":
        break
else:
    print("terminado")
    
#Recorrer una dcadena de texto
for letra in cadena:
    print(letra)

#for en uuna sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
