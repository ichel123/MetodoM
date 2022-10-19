#Autor: Ichel Delgado

#Librerías a utilizar
import matplotlib.pyplot as plt
import numpy as np

#Se define el rango y el dominio de los ejes
rango = 5
x = np.arange(-rango,rango,0.1)
y = np.arange(-rango,rango,0.1)

#Se dibujan dos líneas, una horizontal y una vertical que serán los ejes x e y respectivamente
plt.axhline(color='black', lw=0.5)
plt.axvline(color='black', lw=0.5)

#-------------------------------------------------------
#Se define una función y1, y2, y3 según la cantidad de funciones que sean.
#Con linestyle se define el estilo de linea, si es punteada o no
#Con la función grid se crea la cuadricula de fondo para ayudar a ubicarse en el plano
#Con plot() y show() se crea y se muestra el plano
#-------------------------------------------------------

#Se empiezan a graficar las soluciones de las desigualdades

# 1)
# y1 = 3-3*x
# plt.plot(0.4,1.8,'ro') 
# plt.plot(0.6,1.2,'ro') 
# plt.plot(x, y1)
# plt.grid()
# plt.show()

#2)
# y1 = 3-3*x
# plt.plot(1.8,-2.4,'ro') 
# plt.plot(0.6,1.2,'ro') 
# plt.plot(x, y1)
# plt.grid()
# plt.show()

