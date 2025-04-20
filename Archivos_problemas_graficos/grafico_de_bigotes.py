
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Archivos_problemas_graficos\\bigotes.csv")

# Creando el grafio
sns.boxplot(x="categoria",y="valor",data=df)

# Mostrando el grafico
plt.show()
