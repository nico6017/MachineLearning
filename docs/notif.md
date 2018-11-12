# SmartWatch HealthCare App Sync Evaluation

##  El problema

En este ejemplo se tienen 99 pacientes que monitorean variables de su salud, utilizando una aplicación en un **reloj inteligente** (el ritmo cardíaco, entre otras). El equipo a cargo de esta investigación, les solicita a los pacientes, que sincronicen los datos de la aplicación con bases de datos utilizadas para la investigación. Los datos son tomados continuamente, por lo cual la sincronización también debe ser constante. Vale mencionar que este ejemplo funciona igual que la respuesta de 99 clientes a una campaña de marketing.

Para solicitarles a los pacientes la sincronización de sus datos, se realizan un total de 32 campañas por año, utilizando un medio diferente para cada una como ser:
- Mensajes de texto
- Correos Electrónicos
- Mensajes de Whatsapp
- Carta
- Llamada telefónica
- Etc

Cuando el paciente realiza la sincronización solicitada, se guarda un registro como forma de medir la respuesta a las campañas.

##  El objetivo

El objetivo es entonces agrupar a los pacientes según la campaña a la cual responden, para ajustar los recordatorios para el año próximo.

##  El Dataset

El conjunto de datos es bien sencillo y posee **2 atributos**

- El *id paciente* que identifica de cuál de los 99 pacientes se trata
- La campaña a la cual el paciente respondió (realizó la sincronización que se le pedía) del 1 al 32

##  Paso a Paso



[Volver](./../README.md)
