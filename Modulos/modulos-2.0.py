
# Si el mudulo estuviera en una carpeta en la misma ruta
import Funciones_buenas.saludar as m_saludar

#Si el modulo está en otra ruta se agrega al path 
#import sys
#sys.path.append('Dirección_de_la_carpeta')
#import "nombre_modulo" as "como_lo_quiera_nombrar"

print(m_saludar.saludar("Cristian"))
