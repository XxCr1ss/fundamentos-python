
# Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("Archivos_problemas\\datos.csv")

# Convertimos a string los datos de la columna edad
df['edad'] = df['edad'].astype(str)

# Mostramos el tipo de dato del primer elemento de la columna edad
# print(type(df['edad'][0]))

# Remplazando los datos "cristian" con "david" en la columna 'nombre'
df['nombre'].replace('cristian','david', inplace=True)
print(df['nombre'])

# Eliminando las filas con datos faltantes, dropna(axis=1) si se quiere eliminar las columnas
df = df.dropna()

# Eliminando las filas repetidas
df = df.drop_duplicates()

# Creando un CSV con el dataframe resultante (limpio)
df.to_csv("Archivos_problemas\\datos_limpios.csv")