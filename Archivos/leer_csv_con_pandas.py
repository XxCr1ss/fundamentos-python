import pandas as pd

# Usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("Archivos\\datos.csv")
df2 = pd.read_csv("Archivos\\datos.csv")

# Obteniendo la columna nombre
nombres = df["nombre"]

# Ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

# Ordenandolo de forma descendente
df_orden_descendente = df.sort_values("edad", ascending=False)

# Concatenando los dos dataframes
df_concatenado = pd.concat([df, df2])

# Accediendo a las primeras 3 filas con head()
primeras_fila = df.head(3) 

# Accediento a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

# Accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape

# Obteniendo data estadistica del dataframe
df_info = df.describe()

# Accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2, "edad"]

# Accediendo a la columna 2 (edad) de la fila 2
elemento_especifico_iloc = df.iloc[2, 2]

# Accediendo a las filas de todas las columnas con loc
apellidos_loc = df.loc[:, "apellido"]

# Accediendo a las filas de todas las columnas
apellidos_iloc = df.iloc[:, 1]

# Accediendo a la fila 3 con loc
fila_3_loc = df.loc[2, :]

# Accediendo a la fila 3 con iloc
fila_3_iloc = df.iloc[2, :]

# Accediendo a filas con edad >30 años
mayor_que_30 = df.loc[df["edad"]>30, :]

print(mayor_que_30)
