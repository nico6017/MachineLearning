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



[Volver](./../README.md)
