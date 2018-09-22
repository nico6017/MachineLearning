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

| iteracion | X | Y | b0      | b1      | prediccion | tasa de ap | error    | error2   | b0+1    | b1+1    |
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



[Volver](./../README.md)
