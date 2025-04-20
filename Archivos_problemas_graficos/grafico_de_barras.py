
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Archivos_problemas_graficos\\cofla_ingresos.csv")

# Creando el grafio
sns.barplot(x="fuente",y="ingresos",data=df)

# Sumamos el total de ingresos
total_ingresos = df['ingresos'].sum()

# Mostramos el total
print(f"el total de ingresos es de: ${total_ingresos}")

# Mostrando el grafico
plt.show()
