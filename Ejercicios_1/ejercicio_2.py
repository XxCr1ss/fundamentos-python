texto = input("Dame un texto: ")
textoLista = texto.split(" ")
numeroPalabras = len(textoLista)
tiempoDeDecirElTexto = numeroPalabras / 2

print("------------\n")
print(f"Se tarda decir esta frase {tiempoDeDecirElTexto} segundos")
print(f"Dijo {numeroPalabras} palabras\n")

if (tiempoDeDecirElTexto > 60):
    print("------------\n")
    print("Para flaco, tampoco te pedi un textamento\n")

tiempoDalto = tiempoDeDecirElTexto * 1.3

print("------------\n")
print(f"Dalto se demoraría {tiempoDalto} segundos en decir esta frase")