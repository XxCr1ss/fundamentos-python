
with open("Archivos\\texto_de_cristian.txt", 'a', encoding="UTF-8") as archivo:
    #Agreagando un esapacio de linea
    archivo.write('\n')
    # Usando un bucle para agregar varias lineas al archivo .txt
    for i in range(5): 
        archivo.write(f"Linea {i} agregada\n")
