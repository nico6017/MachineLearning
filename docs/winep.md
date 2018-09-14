# Pre-Procesamiento en Pyhton

`HERRAMIENTA UTILIZADA: PYTHON`

![](./wine.png)


## Objetivo

En este ejercicio se desea practicar las técnicas de pre procesamiento y obtención estadísticas de un conjunto de datos utilizando funciones en Python. En este caso, se tomarán datos de análisis químicos de diferentes vinos

## Conjunto de datos

Archivo CSV con los resultados de un análisis químico realizados sobre vinos creados en la misma región de Italia, pero que derivan de trés cocechas diferentes

**Clases:**

178 registros divididos en 3 clases:
Cosecha 1: 59 registros
Cosecha 2: 71 registros
Cosecha 3: 48 registros

**Valores nulos:**
No

**Outliers:**
Si

**Atributos:**

                
+ Alcohol
+ Acido Malico
+ Ceniza
+ Alcalinidad de Ceniza
+ Magnesio
+ Fenoles totales
+ Fenoles no flavonoides
+ Proanthocyanidins
+ Intensidad del Color
+ Cue
+ OD280/OD315
+ Proline

## Impresión de registros

En python podremos utilizar el siguiente método para poder imprimir una X cantidad de registros de nuestro archivo CSV


```pyhton
def imprime10(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        a = 10
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
            a = a - 1
            print (row)
            if a == 0:
                break
        return dataset
```
