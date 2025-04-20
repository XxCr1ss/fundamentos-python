
#Usando Open para abrir un archivo con codificacion universal (UTF-8) a "Archivos"
archivo = open("Archivos\\texto_de_Cristian.txt", encoding="UTF-8")

#Leer archivo completo
archivo_leido = archivo.read()

#leer una sola linea
#linea = archivo.readline()

#Leer linea por linea
#lineas = archivo.readlines()

#Cerrar el archivo
archivo.close()

print(archivo_leido)
