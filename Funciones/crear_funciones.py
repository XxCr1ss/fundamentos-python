
#Creando una funcion simple
def saludar():
    print("hola lucas, mi maestro ¿Como estas?")

#Ejecutando una función simple
saludar()

#Creando una funcion que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "monstruo" 
    else:
        adjetivo = "amor"  

    print(f"hola {nombre}, mi {adjetivo} ¿Como estas?")

saludar("Cristian", "hombre")
saludar("Hoyos", "mujer")
saludar("Steven", "bi")

#Crear una funcion que nos retorne multiples valores
def crearContraseñaRandom(num):
    chars = "abcdefghij"
    numEnero = str(num)
    num = int(numEnero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}" 
    return contraseña, num

#Desempaquetamos la funcion
password, numero = crearContraseñaRandom(87)

#Mostramos los resultados
frase = f"Tu contraseña nueva es: {password} y el primer numero es {numero}"
print(frase)
