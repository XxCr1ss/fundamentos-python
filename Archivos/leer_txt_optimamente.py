
# Abriendo el archivo con with open
with open("Archivos\\texto_de_cristian.txt", encoding="UTF-8") as archivo:
    
    # Leemos el archivo
    contenido = archivo.read()
    
    # Mostramos el archivo
    print(contenido)

# No es necesario cerrarlo utilizando with open
