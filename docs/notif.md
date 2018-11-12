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

El conjunto de datos es bien sencillo, se trata de un excel con 2 hojas:

La primera enfocada en las campañas con **3 atributos**

- *CampaignID* que identifica cada una de las campañas
- *Type* Tipo o medio por el cual se realizó la campaña
- *Month* Mes en el que se realizó

La segunda enfocada en las respuestas obtenidas con **2 atributos**

- El *id paciente* que identifica de cuál de los 99 pacientes se trata
- La campaña a la cual el paciente respondió (realizó la sincronización que se le pedía) del 1 al 32

##  Paso a Paso

###  Importar herramientas a utilizar

- Librería Pandas
- Librería Numpy
- Librería Sklearn
- Librería plotly (para realizar gráficas)

```from pandas import read_excel, merge
from numpy import arange
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode()
```

###  Cargar los datos

Cargamos por un lado los datos sobre las campañas (hoja1) y por otro los datos de las respuestas (hoja2).
Luego y para trabajar sobre un solo conjunto hacemos un merge de ambos conjuntos, sobre el atributo que tienen en común

```
df_campaign = read_excel("PatientResponse.xlsx", sheet_name = 0)
df_response = read_excel("PatientResponse.xlsx", sheet_name = 1)
df_response["n"] = 1
df_campaign.tail()
df_response.tail()
df = merge(df_campaign, df_response, on = "CampaignID")
```

Luego de mezclar, nuestro conjunto de datos quedaría así:

|  | CampaignID | Type | Month  | Patient |  n |
|------------|------|-------------|----------|----|---|
| 319        | 31   | WhatsApp    | December | 99 | 1 |
| 320        | 32   | Long letter | December | 16 | 1 |
| 321        | 32   | Long letter | December | 29 | 1 |
| 322        | 32   | Long letter | December | 46 | 1 |
| 323        | 32   | Long letter | December | 99 | 1 |




[Volver](./../README.md)
