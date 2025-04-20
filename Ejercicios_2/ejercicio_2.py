#Creando una funcion que nos devueve los numeros primos
#Entre 0 y el argumento que pasemos

#Función que devuelve el numero si es primo
def esPrimo(num):
    for i in range(2, num-1):   
        if (num%i==0):
            break
    return num

#Funcion que devuelve una lista de primos desde 2 hasta el argumento
def primosHasta(num):
    numeros = [esPrimo(i) for i in range(2, num + 1)]
    return numeros

#Llamamos e imprimimos el resultado
resultado = primosHasta(100)
print(resultado)
