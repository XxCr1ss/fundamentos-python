ingresoMensual = 90000
gastoMensual = 87000

#if anidado y elif
if ingresoMensual > 10000:
    if ingresoMensual - gastoMensual < 0:
        print("Estas en deficit")
    elif ingresoMensual - gastoMensual > 3000:
        print("Bien pa, estas bien")
    else:
        print("Estas gastando una banda, hay que ver si te alanza")
elif ingresoMensual > 1000:
    print("Estas bien en Latinoamerica")
elif ingresoMensual > 500:
    print("Estas bien en Argentina")
elif ingresoMensual > 200:
    print("Estas bien en Venezuela")
else:
    print("Eres pobre")
    