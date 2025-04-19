
numeros = [1,2,3,4,5,6,7,8,9]

#Creando una funcion lambda para multiplicar por dos
multiplicando_por_dos = lambda x : x*2
print(multiplicando_por_dos(6))

#Creando una funcion común que diga si es par o no
def esPar(num):
    if (num%2==0):
        return True

#Usando filter con una funcion comun
numerosPares = filter(esPar, numeros)
print(list(numerosPares))

#HacnumerosPares = filter(esPar, numeros)
numerosPares = filter(lambda numero: numero%2 == 0, numeros)
print(list(numerosPares))