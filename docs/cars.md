# Evaluación de Autos y Camionetas

![](./images/check.jpeg)

## El problema

En el rubro automotor, la oferta de vehículos cero kilómetro es muy amplia y cada vez más accesible convirtiéndose en un mercado cada día más grande.

Así como el mercado crece, crecen las posibilidades en cuanto a marcas y prestaciones.

Cada vehículo a su vez, posee una serie de carcterísticas que lo hacen elegible o no según las necesidades del cliente.

El problema se presenta a la hora de evaluar todas esas características en todas las opciones que el cliente busca.

## El Caso

Se desea poder realizar entonces una evaluación automática del vehículo basándose en las características mencionadas.

## El Dataset

El conjunto de datos cuenta con 1728 casos y una variable objetivo "eval" que define qué tan bueno es el vehículo:
- Inaceptable (unacc)
- Aceptable (acc)
- Bueno (good)
- Muy Bueno (v.good)

### Atributos

El modelo evalua cada vehículo según la siguiente estructura:

   EVAL                   Aceptabilidad del Auto
   . buying               Precio de compra (v-high, high, med, low)
   . maint                Precio de mantenimiento (v-high, high, med, low)
   . doors                Número de puertas (2 a 5)
   . persons              Capacidad en personas (2 a 5)
   . lug_boot             Tamaño de la valija (small, med, big)
   . safety               Seguridad (low, med, high)

## Paso a paso

### Preparación de los datos:

El conjunto de datos original debe ser preparado en algunos aspectos para poder realizar un trabajo más cómodo.

En este caso:

1) Se le insertaron los títulos de cada atributo, ya que en un principio no los contiene
2) El atributo "doors" contiene los valores: 2, 3, 4 y 5, pero también "5more", por ende fue suplantado este último por solo "5"
3) Algo similar acontece con el atributo persons, que contiene la palabra "more" por lo cual fue suplantado por "5" para cualquier vehículo que pueda transportar 5 o más personas.

### Procesamiento

Para resolver este problema de clasificación, utilizaremos la técnica **"VOTE"** que lo que permite es realizar un ensamble de varios algoritmos, de manera de que cada uno "vota" sobre la predicción de la/s clases objetivo. De esta manera, se decide por mayoría entre el resultado de la ejecución de dichos algoritmos.

![](./images/captu.png)

Como vemos a priori el proceso es bastante sencillo.

Dentro del operador *Cross Validation* deberemos ingresar el *vote* que es dónde se van a poner a trabajar a los diferentes algoritmos como vemos en la siguiente imagen:

![](./images/vote.png)

Utilizaremos entonces 4 diferentes algoritmos, de los cuales ya hemos hablado en otros casos de estudio, que participarán en la decisión de aceptabilidad de los autos del conjunto de datos.

## Resultados obtenidos

![](./images/Resensa.png)


Como vemos, la composición de algoritmos (el ensamble) a la hora de tomar decisiones, colaboró para obtener un rendimiento aceptable a la hora de clasificar.


[Volver](./../README.md)
