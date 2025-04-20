
import re

texto = '''Hola maestro. esta es la cadena 1. como estas mi capitan
Esta es la linea 2 de texto.
Y esta es la final (linea 334) definitiva mi capitan'''

# Haciendo un abusqueda simple
resultado = re.findall("Hola", texto)

#\d -> busca digito numerios del 0 - 9
resultado = re.findall(r"\d", texto)

#\D -> busca todo menos digitos no numericos del 0 - 9
resultado = re.findall(r"\D", texto)

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w", texto)

#\W -> busca todo menos caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\W", texto)

#\s -> busca los espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r"\s", texto)

#\S -> busca todo menos los espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r"\S", texto)

#. -> busca todo menos saltos de linea
resultado = re.findall(r".", texto)

#\n -> busca saltos de linea
resultado = re.findall(r"\n", texto)

#\ -> canselamos los caracteres especiales
resultado = re.findall(r"\.", texto)

# Armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall('\d\.\s', texto)

# Buscando el principio de una linea
# ^ -> busca el comienzo de una linea (buscando Hola al principio de una linea)
# flags=re.M activa la multilinea
resultado = re.findall('^Hola', texto, flags=re.M)

# Buscando el final de una linea
# $ -> busca el final de una linea (buscando capitan al final de una linea)
# flagas.M activa la multilinea
resultado = re.findall('capitan$', texto, flags=re.M)

# {n} -> busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}',texto)

# {n,m} -> al menos n, como maximo m
resultado = re.findall(r'\d{3,4}',texto)

#  | -> busca una cosa o la otra
resultado = re.findall(r'\d{2,4}|Hola',texto)

print(resultado)
