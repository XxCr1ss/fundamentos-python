cadena1 = "Hola,bb,soy,Cristian"
cadena2 = "Bienvenido bb"

#Convierte a mayusculas
mayus = cadena1.upper()

#Convierte a minusculas
minus = cadena1.lower()

#Primera letra a mayuscula
primerLetraMayusculas = cadena1.capitalize()

#Buscar una cadena en otra cadena, si no hay considencias devuelve -1
busquedaFind = cadena1.find("a")

#Buscar una cadena en otra cadena, si no hay considencias lanza una excepcion
busquedaIndex = cadena1.index("")

#Si es numerico, devolvemos true, sino devolvemos false
esNumerico = cadena1.isnumeric()

#Si es alfanumerico devolvemos true, sino devolvemos false
esAlfanumerico = cadena1.isalpha()

#Contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contarCoincidencias = cadena1.count("a")

#Contamos cuantos caracteres tiene una cadena
contarCaracteres = len(cadena1)

#Verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empiezaCon = cadena1.startswith("Hola")

#Verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
terminaCon = cadena1.endswith("Cristian")

#Si el valor 1, se  encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadenaNueva = cadena1.replace("Cristian", "Cristian")

#Separa cadenas con la cadena que le pasemos
cadenaSeparada = cadena1.split(",")

print(cadenaSeparada)
