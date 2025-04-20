
#Importando un modulo y asigandole el nombre "m_saludar"
#import modulo_saludar as m_saludar

#Desde ese modulo, importamos dos funciones y les cambiamos el nombre
from modulo_saludar import saludar as saludarNormal, saludarRaro as saludarComoElSocio

#Creamos las variables con los resultados
saludo = saludarNormal("Cristian")
saludoRaro = saludarComoElSocio("David")

#Imprimimos los resultados
print(saludo)
print(saludoRaro)

#Para ver todas las propiedades y metodos del namespace
#print((dir(namespace)))

#Accedemos al nombre de este modulo 
print(__name__)

#Accedemos al nombre del modulo llamado
#Print(m_saludar.__name__)