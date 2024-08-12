# MANUAL TÉCNICO


<img src="CopoDeNieve.png" alt="drawing"> 

Se utilizó un modelo de copo de nieve debido a que se normalizaron algunas tablas. Basado en la estructura de la base de datos y en los datos del archivo, se concluyó que el modelo de copo de nieve es óptimo. Aunque las consultas pueden ser más complejas en este modelo en comparación con el modelo estrella, se eligió el modelo de copo de nieve para garantizar la persistencia de datos y evitar la incoherencia o duplicación de datos en la base de datos.

### Tablas de Dimensiones

#### Dimension Aereopuerto

Tabla para guardar los aereopuertos

<img src="./Imagenes/dimaereopuerto.png" alt="drawing" >
<img src="./Imagenes/aereopuerto.png" alt="drawing" >

#### Dimension Continente

Tabla para almacenar los continentes

<img src="./Imagenes/dimcontinente.png" alt="drawing" >
<img src="./Imagenes/continente.png" alt="drawing" >


#### Dimension Fecha
Tabla para almacenar las fechas de los vuelos

<img src="./Imagenes/dimfecha.png" alt="drawing" >
<img src="./Imagenes/fecha.png" alt="drawing" >

#### Dimension Genero

Tabla para almacenar el genero de una persona 

<img src="./Imagenes/dimgenero.png" alt="drawing" >
<img src="./Imagenes/genero.png" alt="drawing" >

#### Dimension Nacionalidad
Tabl para almacenar la nacionalidad de una persona

<img src="./Imagenes/dimnacionalidad.png" alt="drawing" >
<img src="./Imagenes/nacionalidad.png" alt="drawing" >

#### Dimension Pais
Tabla para almacenar el pais de un vuelo

<img src="./Imagenes/dimpais.png" alt="drawing" >
<img src="./Imagenes/pais.png" alt="drawing" >

#### Dimension Estado
Tabla para almacenar el estado de un vuelo

<img src="./Imagenes/dimstatus.png" alt="drawing" >
<img src="./Imagenes/estado.png" alt="drawing" >

## Tabla de Hechos

#### Hechos Vuelos
Tabla de hechos unica, en la cual se hace referencia a todas las dimensiones.
<img src="./Imagenes/FactVuelos.png" alt="drawing" >
<img src="./Imagenes/vuelo.png" alt="drawing" >


