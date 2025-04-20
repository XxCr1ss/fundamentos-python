
# Creando funcion que suma numeros
def sumar_dos():
    while True:
        # Pedimos numeros
        a = input("Numero 1: ")
        b = input("NUmero 2: ")
        # Intentamos convertirlos a enteros y sumarlos
        try:
            resultado = int(a)  + int(b)
        #Si lanza una excepcion, pedirle que reingrese los datos
        except Exception as e:  # noqa: E722
            print("Te pedi un numero salame, no te hagas el gil")
            # Mostramos el error
            print(f"Error: {e}")
            # Mostramos el nombre del error
            print(f"Nombre del error: {type(e).__name__}")
        # Si todo salioi bien terminamos el bucle
        else:
            break
        # finally se ejecuta siempre
        finally:
            print("Manejo de excepcion finalizado")

    return resultado

print(sumar_dos())
