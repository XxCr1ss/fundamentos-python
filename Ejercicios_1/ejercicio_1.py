esteCurso = 1.5
otrosCursosMax = 7
otrosCursosMin = 2.5
otrosCursosMedia = 4

print("------------\n")
porcentajeMax = round((esteCurso / otrosCursosMax) * 100, 3)
print(f"La diferencia de porcentaje de este curso respecto al curso maximo es de: {100 - porcentajeMax}%")
porcentajeMin = round((esteCurso / otrosCursosMin) * 100, 3)
print(f"La diferencia de porcentaje de este curso respecto al curso minimo es de: {100 - porcentajeMin}%")
porcentajeMedia = round((esteCurso / otrosCursosMedia) * 100, 3)
print(f"La diferencia de porcentaje de este curso respecto a la media de cursos es de: {100 - porcentajeMedia}%\n")

print("------------\n")
crudoOtrosCursosMedia = 5
crudoEsteCurso = 3.5
porcentajeUtilizadoEnEsteCurso = round((esteCurso / crudoEsteCurso) * 100, 3)
print(f"El porcentaje decechado de este curso es {100 - porcentajeUtilizadoEnEsteCurso}%")
porcentajeUtilizadoEnLaMediaDeOtrosCursos = round((otrosCursosMedia / crudoOtrosCursosMedia) * 100, 3)
print(f"El porcentaje decechado de este curso es {100 - porcentajeUtilizadoEnLaMediaDeOtrosCursos}%\n")

print("------------\n")
porcentajeRespectoAOtrosCursos = round((otrosCursosMedia / esteCurso), 3)
diezHorasDeEsteCurso = round(10 * porcentajeRespectoAOtrosCursos, 3)
print(f"Ver 10 horas de este curso equivale a ver {diezHorasDeEsteCurso} de otros cursos")
diezHorasDeOtrosCurso  = round(10 * porcentajeMedia / 100, 3)
print(f"Ver 10 horas de otros cursos equivale a ver {diezHorasDeOtrosCurso} de este curso")