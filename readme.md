# Programa Simulación de lo Clasico a lo Cuantico
Librería Experimentos seccion 3

##1. Los experimentos de la canicas con coeficiente booleanos

    matriz = np.array(([[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1],
               [0, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0],
               [1, 0, 0, 0, 1, 0]])
    estado = [6, 2, 1, 5, 3, 10]
    Despues de 1 click: [0, 0, 12, 5, 1, 9]

##2. Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
    
    rendijas = 2
    objetivos = 5
    resultado = [0.0, 0.0, 0.0, 0.2, 0.2, 0.2, 0.2, 0.2]

##3. Experimento de las múltiples rendijas cuántico.

    rendijas = 2
    objetivos = 5
    resultado =[0.0, 0.0, 0.0, 0.19999999999999993, 0.19999999999999993, 0.19999999999999993, 0.19999999999999993, 0.19999999999999993])
  

###4. Cree una función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados. La imagen se debe poder guardar en el computador con un formato de imagen
Estas graficas se incluyeron en el archivo de pruebas, por lo que para cada funcion y su resultado se
genera un grafico de barras con la libreria _**matlibplot**_

## Pre-requisitos: 
Se requiere de conocimientos de sistemas deterministicos y probablisticos normales y cuanticos

Se requiere de lenguaje de programación Python de preferencia version 3 o superior.  

Esta libreria puede ser ejecutada en el IDLE preinstalado de Python o en el entorno de PyCharm.

## Autores

**Isabella Manrique** - _Libreria primer tercio_