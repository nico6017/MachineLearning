# Pre-Procesamiento en Pyhton

`HERRAMIENTAS UTILIZADAS: PYTHON Y PANDAS`

[**HERRAMIENTA PANDAS**](./pandas.md)

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
+ Flavanoids
+ Fenoles no flavonoides
+ Proanthocyanidins
+ Intensidad del Color
+ Cue
+ OD280/OD315
+ Proline	

## Limpieza y análisis previo en archivos CSV

Normalmente los archivos CSV requieren de un procesamiento previo por cuestiones de formato.

En este caso se utilizó la herraminta Excel para insertarle un cabezal cuyas columnnas correspondan a cada atributo.


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

Sin embargo, utilizando la herramienta Pandas ya mencionada, la tarea de imprimir ciertos registros se reduce a un código mucho más simple:

```pyhton
def PandasPrint(dataset):
    data = pd.read_csv(dataset)
    print(data.head(10))
    return data
```

## Máximos y mínimos por columna



```pyhton
def minmaxCol(dataset):
    data = pd.read_csv(dataset)
    print("Maximos por columna ")
    print("------------------- ")
    print(data.max(axis=0))
    print("                    ")
    print("Minimos por columna ")
    print("------------------- ")
    print(data.min(axis=0))
    return data
```

## Conclusiones
