
import re

# Detectando un numero CABA y ocultandolo
texto = "Hola Cristian, mi numero es: +54 11 4321-4321 +54 11 4321-4321"

pattern = r'\+\d{2}\s\d{2}\s\d{4}-\d{4}'

remplazo = re.sub(pattern,"(Numero oculto)",texto)

print(remplazo)
