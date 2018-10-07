# Ejercicio de aplicación CART: Predicción del Clima

![](./images/weather.png)

## Herramienta KNIME

KNIME o Konstanz Information Miner por sus siglas es una plataforma de datamining similar a Rapidminer, que permite el desarrollo de modelos en un entorno gráfico.
Está construido bajo la plataforma Eclipse y es una herramienta de software libre por lo cual puede ser descargada y utilizada gratuitamente

## El dataset

Tenemos un conjunto de datos (.csv) compuesto por **1094 mediciones** de variables relacionadas al clima de un día.

Sus atributos son:

- La presión atmosférica en la mañana
- La temperatura en la mañana
- La dirección promedio del viento en la mañana
- La velocidad promedio del viento en la mañana
- La velocidad máxima del viento en la mañana
- La acumulación de lluvia en la mañana
- La humedad relativa en la mañana
- La humedad relativa en la tarde

## Objetivo

El objetivo es determinar si un día cualquiera, será o no un día de baja humedad, dados ciertos parámetros.

## Paso a Paso con KNIME

#### 1- Ingreso de datos

Levanto el archivo .csv utilizando el operador *File Reader*, realizando las configuraciones necesarias (lectura de ids y encabezados, establecer el limitador entre columnas, etc)

#### 2- Manejo de valores nulos

Nuestro dataset tiene para algunas mediciones, valores nulos por lo cual decidimos quitarlos.

Para ello, vamos a utilizar el parámetro *remove row*, del operador *Missing Value*

#### 3- Conversión a variable categórica

Nuestro objetivo es determinar si un día tiene o no baja humedad, sin embargo nuestro conjunto de datos tiene múltiples valores de humedad. Lo que vamos a hacer entonces es "convertir" los valores de humedad en dos *bins* o clases: humedad baja y humedad no baja

Nos valemos del operador *Numeric Biner*: vamos a modificar entonces los valores de la columna humedad relativa en la tarde.

![](./images/nbiner.png)

Establecemos el corte entre baja y no baja en 25% y como se vé en la imagen creamos una columna adicional que va a ser nuestra variable objetivo.

Para ver el progreso hasta el momento, vamos a tomar estadísticas conectando el operador *Statistics* con el dataset original y otro luego de los cambios realizados.

![](./images/statis.png)

Como vemos, originalmente el conjunto de datos poseía valores nulos, ahora ya no.

![](./images/low.png)

Además si vamos a las variables nominales en las estadísticas luego de los cambios, podemos observar la nueva columna creada "low humidity", la cual a priori con el corte establecido, tiene una distribución de valores 50-50



[Volver](./../README.md)

