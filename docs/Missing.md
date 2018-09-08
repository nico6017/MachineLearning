# Preparación de los datos

## Tratamiento de Valores Nulos

Parto de un dataset que cuenta con varios **atributos con valores nulos**. A continuación voy a proceder a ejecutar diversas acciones para el tratamiento de dichos valores.

Lo primero que voy a hacer es **descartar** dos atributos que cuentan con muchos valores nulos **por estar fuertemente relacionados con el label del dataset.**

Para ello utilizo el **operador** **select attributes** conectado al dataset y me quedo con todos los atributos menos esos dos.

Para resolver los valores faltantes del atributo age, que tiene bastantes, utilizo otra de las técnicas normalmente usadas: reemplazar valores nulos por el promedio del resto de los valores.
Para realizar esto, voy a utilizar el operador replace missing values, teniendo en cuenta como parámetro single que significa remplazar por el promedio.
Por último con los restantes valores nulos que aún me quedan, como se trata de una cantidad muy pequeña y despreciable los voy a descartar.
Voy a tomar el operador Filter Examples y en las opciones avanzadas selecciono no missing valúes lo que borra las tuplas sin valores.

## Tratamiento de Outliers

[Volver](./../README.md)
