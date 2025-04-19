
numeros = [4, 7, 1, 42, 15]

#Encontrando el numero mayor de una lista
numeros_mas_alto = max(numeros)
print(numeros_mas_alto)

#Encontrando el numero medor de una lista
numeros_min_alto = min(numeros)
print(numeros_min_alto)

#Redondeando a seis decimales
numero = round(12.345678, 3)
print(numero)

#Retorna False -> 0 , vacio, False, None / True -> distinto a 0, True, cadena, datos no vacios
resultado_bool = bool("fas;d")
print(resultado_bool)

#Retrona True, si todos los valores son verdaderos
resultado_all = all([4, "fads", True, []])
print(resultado_all)

#Suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)