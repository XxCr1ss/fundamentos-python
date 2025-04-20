
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Archivos_problemas_graficos\\pedos.csv")

# Creando el grafio
sns.lineplot(x="fecha",y="pedos",data=df)

# Creando un punto en el punto mas alto
plt.plot("01-09",17,"o")

# Mostrando el grafico
plt.show()
