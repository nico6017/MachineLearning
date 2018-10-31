# Caso de estudio: Tarjetas Impagas

![](./images/credit.jpg)

## El problema

En inglés se le denomina "Default of Credit Card" cuando un cliente de una tarjeta de crédito se atrasa en sus pagos con respecto a la fecha de vencimiento de los mismos. Particularmente se utiliza el concepto de "default" cuando el cliente se atrasa por más de 180 días, provocando que sus deudas crezcan exponencialmente y que le sea quitada su línea de crédito.

Podemos ver algo más sobre este problema en el siguiente link:

- https://www.thebalance.com/what-is-credit-card-default-960209

## El caso

Este estudio apunta a estimar la probabilidad real de "default" de un nuevo cliente en Taiwan, conocida una base de datos de casos previos.

## El Dataset

El conjunto de datos cuenta con 30.000 casos y una variable objetivo "default" en la que sabemos si realmente el cliente llegó a esa situación (1) o no (0)

### Atributos:

Datos personales de los clientes como:

- Género
- Nivel educativo
- Estado civil
- Edad

Información crediticia:

- Historial de pagos de los últimos 6 meses (monto por mes)
- El nivel de atraso en los pagos (en cantidad de meses)
- Estados de cuenta de los útimos 6 meses (monto por mes)
- Pagos previos realizados en los últimos meses (monto por mes)

## Paso a paso:

### Preparación de los datos:

Como primer paso los atributos estaban en el conjunto de datos con variables desde X1 a X25 por lo cual removimos la cabecera y pusimos una propia con los nombres de cada atributo

En segundo lugar convertimos el archivo original desde un XLS a CSV para ser posteriormente procesado










