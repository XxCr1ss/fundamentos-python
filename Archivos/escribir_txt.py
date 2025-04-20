
# 
with open("Archivos\\texto_de_cristian.txt", 'w', encoding="UTF-8") as archivo:
    # Sovreescribiendo el archivo
    #archivo.write("Te la re hice")
    
    # Agregando 2 lineas con writelines
    archivo.writelines(["- Hola Cristian como andas\n", "- Hola buenas\n"])
    
    #Agregando otras 2 lineas
    archivo.writelines(["- Tengo sueño\n", "- Yo también\n"])
