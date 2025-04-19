esteCurso = 1.5
otrosCursosMax = 7
otrosCursosMin = 2.5
otrosCursosMedia = 4

print("------------\n")
porcentajeMax = (esteCurso / otrosCursosMax) * 100
print(f"La diferencia de porcentaje de este curso respecto al curso maximo es de: {100 - porcentajeMax}%")
porcentajeMin = (esteCurso / otrosCursosMin) * 100
print(f"La diferencia de porcentaje de este curso respecto al curso minimo es de: {100 - porcentajeMin}%")
porcentajeMedia = (esteCurso / otrosCursosMedia) * 100
print(f"La diferencia de porcentaje de este curso respecto a la media de cursos es de: {100 - porcentajeMedia}%\n")

print("------------\n")
crudoOtrosCursosMedia = 5
crudoEsteCurso = 3.5
porcentajeUtilizadoEnEsteCurso = (esteCurso / crudoEsteCurso) * 100
print(f"El porcentaje decechado de este curso es {100 - porcentajeUtilizadoEnEsteCurso}%")
porcentajeUtilizadoEnLaMediaDeOtrosCursos = (otrosCursosMedia / crudoOtrosCursosMedia) * 100
print(f"El porcentaje decechado de este curso es {100 - porcentajeUtilizadoEnLaMediaDeOtrosCursos}%\n")

print("------------\n")
porcentajeRespectoAOtrosCursos = (otrosCursosMedia / esteCurso) 
diezHorasDeEsteCurso = 10 * porcentajeRespectoAOtrosCursos
print(f"Ver 10 horas de este curso equivale a ver {diezHorasDeEsteCurso} de otros cursos")
diezHorasDeOtrosCurso  = 10 * porcentajeMedia / 100
print(f"Ver 10 horas de otros cursos equivale a ver {diezHorasDeOtrosCurso} de este curso")