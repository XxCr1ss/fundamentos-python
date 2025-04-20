
#Calcular la serie de Fibonacci desde el 0 hasta
#un numero dado

#Funcion que devuelve la lista de los numeros de fibonacci entre 0 y num
def serieFibonacci(num):
    value1, value2 = 0, 1
    serieFibonacci = [0, 1]
    while(num>serieFibonacci[-1]):
        newValue = value1 + value2
        value1, value2 = value2, newValue
        if newValue>num:
            break
        serieFibonacci.append(newValue)
    return serieFibonacci

#Llamamos e imprimimos la función
resultado = serieFibonacci(100)
print(resultado)
