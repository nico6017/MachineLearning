# Descenso de Gradiente

El algoritmo de descenso de gradiente, es uno de los algoritmos de optimización más utilizados en el Machine Learning.

El algoritmo busca optimizar una función, minimizándola.

En otras palabras, si tenemos un problema, el algoritmo nos ayuda para encontrar la solución tal que se trate de una minima distancia, minimo coste, minimo gasto, etc, dependiendo el contexto del problema que intentemos resolver.

Como ejemplo imaginemos que estemos parados en un terreno montañoso y que nuestro objetivo sea encontrar el punto más bajo de toda la superficie sin contar con el mapa del terreno.

¿Cómo resolvemos este problema?

Podríamos ver hacia dónde va la pendiente de mayor inclinación y caminar en esa dirección.

Luego nos paramos en una nueva posición y volvemos a repetir el proceso, así hasta encontrar el mínimo global. De esa forma funciona el algoritmo descenso de gradiente.

Con un enfoque más matemático, calcular la pendiente de cada punto implica obtener la derivada parcial de la función en ese punto. El conjunto de todas esas derivadas, determinan un vector en el que la pendiente asciende al que se le denomina vector gradiente. Como lo que estamos buscando es descender, tomamos el gradiente en sentido contrario.

Para completar el modelo debemos de agregar también un último parámetro, el ratio de aprendizaje, en otras palabras: cuánto avanzamos en cada paso. Este parámetro es muy importante ya que representa la "distancia" entre cada iteración. Digamos entonces que si estamos yendo hacia un mínimo local y utilizamos un ratio de aprendizaje muy grande o muy pequeño, es posible que el algoritmo nunca converja.

# Caso de Análisis

Dado un conjunto de Valores X e Y como se muestra en la siguiente tabla:

| X | Y |
|---|---|
| 1 | 1 |
| 3 | 2 |
| 2 | 3 |
| 4 | 3 |
| 6 | 2 |
| 5 | 5 |

Sabiendo los valores de Y, se buscará ejecutar distintas iteraciones del algoritmo buscando que las predicciones mejoren minimizando el error.

Dado que es una regresión la ecuación será:

#### y = a + bx

Llamaremos **b0 y b1** a nuestros **a y b**

Tendremos entonces:

- b0 (comenzando desde 0)
- b1 (comenzando desde 0)
- Predicción (y = b0 + b1 * x)
- Tasa de aprendizaje (el ratio mencionado anteriormente)
- El error (La predicción - el valor real)
- Error2: el error elevado al cuadrado
- El nuevo b0 (el anterior b0 - tasa de aprendizaje * error)
- El nuevo b1 (el anterior b1 - tasa de aprendizaje * error)

Realizando los calculos obtenemos los siguientes resultados:

| iter| X | Y | b0      | b1      | pred | tasa de ap | error    | error2   | b0+1    | b1+1    |
|-----------|---|---|---------|---------|------------|------------|----------|----------|---------|---------|
| 1         | 1 | 1 | 0,00000 | 0,00000 | 0,00000    | 0,01000    | -1,00000 | 1,00000  | 0,01000 | 0,01000 |
| 2         | 3 | 2 | 0,01000 | 0,01000 | 0,04000    | 0,01000    | -1,96000 | 3,84160  | 0,02960 | 0,06880 |
| 3         | 2 | 3 | 0,02960 | 0,06880 | 0,16720    | 0,01000    | -2,83280 | 8,02476  | 0,05793 | 0,12546 |
| 4         | 4 | 3 | 0,05793 | 0,12546 | 0,55975    | 0,01000    | -2,44025 | 5,95481  | 0,08233 | 0,22307 |
| 5         | 6 | 2 | 0,08233 | 0,22307 | 1,42073    | 0,01000    | -0,57927 | 0,33556  | 0,08812 | 0,25782 |
| 6         | 5 | 5 | 0,08812 | 0,25782 | 1,37724    | 0,01000    | -3,62276 | 13,12443 | 0,12435 | 0,43896 |
| 7         | 1 | 1 | 0,12435 | 0,43896 | 0,56331    | 0,01000    | -0,43669 | 0,19070  | 0,12872 | 0,44333 |
| 8         | 3 | 2 | 0,12872 | 0,44333 | 1,45870    | 0,01000    | -0,54130 | 0,29301  | 0,13413 | 0,45957 |
| 9         | 2 | 3 | 0,13413 | 0,45957 | 1,05326    | 0,01000    | -1,94674 | 3,78978  | 0,15360 | 0,49850 |
| 10        | 4 | 3 | 0,15360 | 0,49850 | 2,14760    | 0,01000    | -0,85240 | 0,72658  | 0,16212 | 0,53260 |
| 11        | 6 | 2 | 0,16212 | 0,53260 | 3,35770    | 0,01000    | 1,35770  | 1,84336  | 0,14855 | 0,45113 |
| 12        | 5 | 5 | 0,14855 | 0,45113 | 2,40422    | 0,01000    | -2,59578 | 6,73808  | 0,17450 | 0,58092 |
| 13        | 1 | 1 | 0,17450 | 0,58092 | 0,75543    | 0,01000    | -0,24457 | 0,05982  | 0,17695 | 0,58337 |
| 14        | 3 | 2 | 0,17695 | 0,58337 | 1,92706    | 0,01000    | -0,07294 | 0,00532  | 0,17768 | 0,58556 |
| 15        | 2 | 3 | 0,17768 | 0,58556 | 1,34879    | 0,01000    | -1,65121 | 2,72648  | 0,19419 | 0,61858 |
| 16        | 4 | 3 | 0,19419 | 0,61858 | 2,66852    | 0,01000    | -0,33148 | 0,10988  | 0,19750 | 0,63184 |
| 17        | 6 | 2 | 0,19750 | 0,63184 | 3,98855    | 0,01000    | 1,98855  | 3,95434  | 0,17762 | 0,51253 |
| 18        | 5 | 5 | 0,17762 | 0,51253 | 2,74026    | 0,01000    | -2,25974 | 5,10642  | 0,20022 | 0,62552 |
| 19        | 1 | 1 | 0,20022 | 0,62552 | 0,82573    | 0,01000    | -0,17427 | 0,03037  | 0,20196 | 0,62726 |
| 20        | 3 | 2 | 0,20196 | 0,62726 | 2,08373    | 0,01000    | 0,08373  | 0,00701  | 0,20112 | 0,62475 |
| 21        | 2 | 3 | 0,20112 | 0,62475 | 1,45061    | 0,01000    | -1,54939 | 2,40060  | 0,21662 | 0,65573 |
| 22        | 4 | 3 | 0,21662 | 0,65573 | 2,83955    | 0,01000    | -0,16045 | 0,02574  | 0,21822 | 0,66215 |
| 23        | 6 | 2 | 0,21822 | 0,66215 | 4,19113    | 0,01000    | 2,19113  | 4,80105  | 0,19631 | 0,53068 |
| 24        | 5 | 5 | 0,19631 | 0,53068 | 2,84973    | 0,01000    | -2,15027 | 4,62367  | 0,21781 | 0,63820 |
| 25        | 1 | 1 | 0,21781 | 0,63820 | 0,85601    | 0,01000    | -0,14399 | 0,02073  | 0,21925 | 0,63964 |
| 26        | 3 | 2 | 0,21925 | 0,63964 | 2,13816    | 0,01000    | 0,13816  | 0,01909  | 0,21787 | 0,63549 |
| 27        | 2 | 3 | 0,21787 | 0,63549 | 1,48885    | 0,01000    | -1,51115 | 2,28356  | 0,23298 | 0,66572 |
| 28        | 4 | 3 | 0,23298 | 0,66572 | 2,89584    | 0,01000    | -0,10416 | 0,01085  | 0,23402 | 0,66988 |
| 29        | 6 | 2 | 0,23402 | 0,66988 | 4,25331    | 0,01000    | 2,25331  | 5,07742  | 0,21149 | 0,53468 |
| 30        | 1 | 1 | 0,21149 | 0,53468 | 0,74617    | 0,01000    | -0,25383 | 0,06443  | 0,21403 | 0,53722 |
| 31        | 3 | 2 | 0,21403 | 0,53722 | 1,82569    | 0,01000    | -0,17431 | 0,03038  | 0,21577 | 0,54245 |
| 32        | 2 | 3 | 0,21577 | 0,54245 | 1,30067    | 0,01000    | -1,69933 | 2,88772  | 0,23276 | 0,57644 |
| 33        | 4 | 3 | 0,23276 | 0,57644 | 2,53851    | 0,01000    | -0,46149 | 0,21297  | 0,23738 | 0,59490 |
| 34        | 6 | 2 | 0,23738 | 0,59490 | 3,80676    | 0,01000    | 1,80676  | 3,26437  | 0,21931 | 0,48649 |
| 35        | 5 | 5 | 0,21931 | 0,48649 | 2,65177    | 0,01000    | -2,34823 | 5,51420  | 0,24279 | 0,60390 |




[Volver](./../README.md)
