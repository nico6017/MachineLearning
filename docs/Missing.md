
# Supervivencia en el Titanic	

`HERRAMIENTA UTILIZADA: RAPIDMINER`


![](./Interior3.jpg)

## Objetivo

Dentro del Pre-procesamiento de datos podemos encontrar dos grandes categorías:
La mezcla y la limpieza.
El objetivo de este trabajo es probar diversas técnicas dentro de éstas categorías y realizar una comparación para determinar cuánto influye en la predicción de la variable objetivo.
En este caso, se desea predecir si un pasajero del Titanic sobrevive o no conociendo ciertas variables del mismo.


### Conjunto de datos

Datos correspondientes a 1309 pasajeros

**Clases:**

2 clases: Si o No

**Valores nulos:**
Si

**Outliers:**
Si

**Atributos:**
                
+ Clase del Pasajero
+ Nombre
+ Sexo
+ Edad
+ Numero de ticket
+ Cabina
+ Costo
+ Puerto de embarque
+ Bote Salvavidas
+ **Sobrevive** (Variable Objetivo)


## Tratamiento de Valores Nulos

Como mencionamos anteriormente, parto de un conjunto de datos que cuenta con varios **atributos con valores nulos**.

A continuación voy a proceder a ejecutar diversas acciones para el tratamiento de dichos valores.

Lo primero que voy a hacer es **DESCARTAR** dos atributos del conjunto de datos ya que ambos cuentan con demasiados valores nulos y por lo tanto no me son útiles. 

Descarto entonces:

+ Bote Salvavidas
+ Cabina

> Para descartar utilizo el **operador** **select attributes** y con el parámetro **subset** filtro todos los atributos menos esos dos.

En el conjunto de datos también tenemos algunos faltantes en el atributo **edad**.

Para resolver esto voy a utilizar otra de las técnicas normalmente usadas: **REEMPLAZAR POR EL PROMEDIO** del resto de los valores.

Reemplazo entonces:

+ Valores nulos de EDAD por valores promedio

Para realizar esto, voy a utilizar el operador replace missing values, teniendo en cuenta como parámetro single que significa remplazar por el promedio.
Por último con los restantes valores nulos que aún me quedan, como se trata de una cantidad muy pequeña y despreciable los voy a descartar.
Voy a tomar el operador Filter Examples y en las opciones avanzadas selecciono no missing valúes lo que borra las tuplas sin valores.

## Tratamiento de Outliers

[Volver](./../README.md)
