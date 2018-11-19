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

   - **EVAL**                   Aceptabilidad del Auto
   - **buying**               Precio de compra (v-high, high, med, low)
   - **maint**                Precio de mantenimiento (v-high, high, med, low)
   - **doors**                Número de puertas (2 a 5)
   - **persons**              Capacidad en personas (2 a 5)
   - **lug_boot**             Tamaño de la valija (small, med, big)
   - **safety**               Seguridad (low, med, high)

## Paso a paso


[Volver](./../README.md)
