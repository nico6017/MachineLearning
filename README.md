
Portfolio Machine Learning

# Portfolio Machine Learning

**[Introducción](./README.md#introducción)**

+ [¿Qué es Machine Learning?](./README.md#qué-es-machine-learning)
+ [Diferencias con la Inteligencia Artificial](./README.md#qué-tiene-en-común-y-en-qué-se-diferencia-de-la-inteligencia-artificial)
+ [Diferencias con Análisis Estadístico](./README.md#qué-lo-diferencia-del-análisis-estadístico)
+ [Diferencias con Data Mining](./README.md#cómo-se-diferencia-con-data-mining)
+ [Aplicaciones de Machine Learning](./README.md#en-qué-se-aplica)
       

##  Trabajos Prácticos




 
||**Valores Nulos**|**Outliers**|**RapidMiner**|**Tunning de Parámetros**|
|:-:|:-:|:-:|:-:|:-:|
|**Preparación de los Datos**|||||
|[Caso: Supervivencia en el Titanic](./docs/Missing.md)|[✓](./docs/Missing.md#tratamiento-de-valores-nulos)| [✓](./docs/Missing.md#tratamiento-de-outliers)|✓||
|[Caso: Análisis Químico de Vinos](./docs/winep.md)|||||
|**Algoritmos Lineales**|||||
|[Regresión Lineal](./docs/regresion.md)|||||
|[Descenso de Gradiente](./docs/grad.md#descenso-de-gradiente)|||||
|[Caso: Goleador de Futbol](./docs/goles.md)|||||
|[Caso: Aplicando Descenso](./docs/grad.md#descenso-de-gradiente#caso-de-análisis)|||||



## Introducción  

### ¿Qué es Machine Learning?  

Entendemos al Machine Learning como una rama de la **Inteligencia Artificial**, es por eso que para tener una clara referencia de lo que estamos hablando, tenemos que definir la Inteligencia Artificial.

Si bien hay muchas definiciones, podemos encontrar un tronco común que define a la inteligencia artificial como la rama de la informática que busca la creación de máquinas que puedan **imitar comportamientos Inteligentes**.

En este marco entonces, el **Machine Learning** o “Aprendizaje Automático” es el campo de la Inteligencia Artificial que busca **dotar a esas máquinas, capacidad de aprendizaje**


### ¿Qué tiene en común y en qué se diferencia de la Inteligencia Artificial?
 La respuesta es que Machine Learning es una disciplina dentro de la Inteligencia Artificial, es decir que la Inteligencia Artificial es un concepto más macro.

 Podemos comenzar por un punto común que ambos conceptos persiguen:
 - la creación de dispositivos o algoritmos que omiten o reemplacen al ser humano emulando sus funciones cognitivas
 
Yendo al punto donde ambos conceptos se distancian, la inteligencia artificial engloba la idea de que las máquinas realicen acciones emulando el comportamiento humano. mientras que machine learning es la disciplina que trata puntualmente el area del aprendizaje. se podría decir que machine learning es el motor de la inteligencia artificial


### ¿Qué lo diferencia del análisis estadístico?
Si bien Machine Learning utiliza estadísticas para la resolución de problemas, aborda cuestiones totalmente por fuera del campo de la estadística, como por ejemplo mantener conversaciones como si se tratase de un humano, reconocer patrones, reconocer imágenes, dirigir vehículos.


### ¿Cómo se diferencia con Data Mining?
En pocas palabras podríamos decir que Data Mining se trata de algo más puntual con un objetivo particular.
La minería de datos, se focaliza en descubrir ciertas propiedades a partir de un conjunto de datos, se realiza sobre un set de datos en particular, con un criterio y objetivo específico. Por otra parte, Machine Learning está enfocada en el diseño de algoritmos que puedan aprender y realizar predicciones a partir de un conjunto de datos.


### ¿En qué se aplica?
En pocas palabras podríamos decir que Data Mining se trata de algo más puntual con un objetivo particular.
La minería de datos, se focaliza en descubrir ciertas propiedades a partir de un conjunto de datos, se realiza sobre un set de datos en particular, con un criterio y objetivo específico. Por otra parte, Machine Learning está enfocada en el diseño de algoritmos que puedan aprender y realizar predicciones a partir de un conjunto de datos.

Hoy se dice que la Inteligencia Artificial es el futuro de la tecnología y eso se debe las múltiples aplicaciones que tiene y a la posibilidad de ser aplicada en todos los ámbitos de la vida.

A continuación, veamos algunas de las aplicaciones más relevantes de hoy en día:

![](./docs/images/Mal.png)

#### 1- Seguridad de los datos

* Si bien el software malicioso aumenta día a día, la mayoría del malware suele contener patrones y código en común, para lo cual se utiliza Machine Learning en la detección de dichas similitudes.

#### 2- Seguridad personal

* Aeropuertos, edificios con zonas de seguridad adicional, datacenters y muchos otros lugares que poseen ingreso de personas las cuales deben de ser revisadas mediante detectores de metales, scaners y otros dispositivos de seguridad. Allí el machine learning es aplicado para aligerar dichos controles de seguridad, ya que puede ayudar a eliminar falsas alarmas y detectar anomalías en las proyecciones de seguridad

#### 3- Mercado de valores

* Poder predecir diferentes variables del mercado de divisas sin dudas que es atractivo. Hoy en día se está usando Machine Learning con el objetivo de intentar deducir movimientos en la bolsa de valores, incluso en la realización de bots para operar en dichos mercados.

#### 4- Cuidados de la Salud

* Otro campo en el cual Machine Learning tiene muchísimo para crecer y aportar es la Salud. La predicción de enfermedades, ataques cardíacos, posibilidad de contraer enfermedades en el futuro y un sin fin de usos que mejorarán la atención médica en el futuro.

#### 5- Marketing

* En el área del marketing el Machine Learning también encuentra un nicho importante y es que se intenta ir hacia el marketing personalizado, el cual se basa en un sencillo principio: mientras más se pueda saber sobre el cliente y su comportamiento, mejor se le podrá atender y se traducirá en más ventas.

#### 6- Detección de Fraudes

* Se utiliza para detectar posibles casos de fraude en diferentes campos. Por ejemplo, PayPal ya utiliza el machine learning para combatir el blanqueo de dinero; la compañía tiene herramientas que comparan millones de transacciones y pueden distinguir con precisión entre transacciones legítimas y fraudulentas, entre compradores y vendedores.

#### 7- Recomendaciones en e-commerce

* Los algoritmos de machine learning permiten analizar la actividad de un usuario en plataformas como Amazon, Ebay, MercadoLibre, etc y compararla con la del resto de usuarios para determinar qué le gustaría ver o comprar en próximas ocasiones. En este campo los avances son increíbles, por ejemplo, gracias a esos algoritmos las plataformas pueden detectar que un usuario está comprando un artículo que no es para él, sino para regalar.

#### 8- Búsquedas en la web

* No podía faltar en un ranking de los usos más importantes, el uso más famoso del Machine Learning. Google y sus competidores mejoran constantemente lo que entiende el motor de búsqueda. Cada vez que se ejecuta una búsqueda en Google, el programa observa cómo responde a los resultados. Si un usuario hace clic en el resultado superior y permanece en esa página web, podemos suponer que obtuvo la información que estaba buscando y que la búsqueda fue un éxito.
Si, por otro lado, hace clic en la segunda página de resultados, o escribe una nueva cadena de búsqueda sin hacer clic en ninguno de los resultados, podemos deducir que el motor de búsqueda no proporcionó los resultados que deseaba, y el programa puede aprender de ese error para ofrecer un mejor resultado en el futuro.

#### 9- Vehículos Inteligentes

* Se espera que en 2025 ya podamos ver coches inteligentes y autónomos en muchas partes del mundo. En este marco, un coche inteligente no solo se integraría en IoT, sino que también aprendería sobre su propietario y su entorno. Estos vehículos podrían ajustar la configuración interna (temperatura, audio, posición del asiento, etc.) de forma automática en función del conductor, informar e incluso solucionar problemas, y conducir y ofrecer asesoramiento en tiempo real sobre el tráfico y las condiciones de la carretera.



