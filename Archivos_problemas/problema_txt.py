
# Guardamos esta información en un .txt
with open("Archivos_problemas\\nombres_apellidos.txt", "w", encoding="UTF-8") as archivo:
    # Creamos las listas nombres y apellidos
    nombres = ["Crsitian", "David", "Kevin", "Junior"]
    apellidos = ["Cabrera", "Pantoja", "Jordan", "Cantor"]
    
    # Indicamos la forma utilizada
    archivo.write("Forma 1: \n\n")
    archivo.write("Los nombres son: \n\n")
    
    # Forma casi optima
    for nombre, apellido in zip(nombres, apellidos):
        archivo.write(f"------------\n- {nombre} {apellido} \n")
    
    # Indicamos la forma utilizada
    archivo.write("\nForma 2: \n\n")
    archivo.write("Los nombres son: \n\n")
    
    # Forma optima
    [archivo.write(f"------------\n- {nombre} {apellido} \n") for nombre,apellido in zip(nombres,apellidos)]