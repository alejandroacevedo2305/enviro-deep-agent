---
title: Sin título
author: Nico Rebolledo
date: D:20240909133631-03'00'
language: es
type: report
pages: 38
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - PROYECTO PLANTA FOTOVOLTAICA CHIETI SOLAR COLINA
-->

## ADENDA COMPLEMENTARIA EN RESPUESTA AL SEGUNDO INFORME CONSOLIDADO DE SOLICITUD DE ACLARACIONES, RECTIFICACIONES Y/O AMPLIACIONES A LA DECLARACIÓN DE IMPACTO AMBIENTAL

# PROYECTO PLANTA FOTOVOLTAICA CHIETI SOLAR COLINA

## ANEXO AC-5.1-C MODELACIÓN DE DISPERSIÓN DE CONTAMINANTES

### Septiembre 2024

## Modelación de Dispersión de Contaminantes Declaración de Impacto Ambiental Adenda 1 _“Planta Fotovoltaica Chieti Solar”_

#### Mayo 2024

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

**ÍNDICE**

Adenda 1

Mayo 2024

ÍNDICE DE TABLAS ...................................................................................................................................................... 4

ÍNDICE DE FIGURAS .................................................................................................................................................... 4

1. INTRODUCCIÓN ................................................................................................................................................ 5

2. ANTECEDENTES GENERALES DEL PROYECTO ................................................................................................. 6

2.1. Descripción ............................................................................................................................................... 6

2.2. Localización .............................................................................................................................................. 6

2.3. Cronograma general ................................................................................................................................ 6

2.3.1. Fase de construcción .......................................................................................................................... 7

2.3.2. Fase de operación ............................................................................................................................... 8

2.3.3. Fase de cierre ...................................................................................................................................... 8

3. MODELACIÓN DE DISPERSIÓN DE CONTAMINANTES .................................................................................... 9

3.1. Descripción de los modelos utilizados. ................................................................................................... 9

3.1.1. WRF ..................................................................................................................................................... 9

3.1.2. CALPUFF .............................................................................................................................................. 9

3.2. Normas de calidad del aire .................................................................................................................... 10

3.3. Dominio de Modelación ........................................................................................................................ 10

3.4. Análisis de Incertidumbre ....................................................................................................................... 12

3.4.1. Análisis Cualitativo ............................................................................................................................ 14

3.4.1.1. Series de Tiempo ..................................................................................................................................... 15

3.4.1.2. Ciclos Diarios ........................................................................................................................................... 17

3.4.1.3. Rosas de Viento ..................................................................................................................................... 20

3.4.1.1. Ciclo Estacional ...................................................................................................................................... 24

3.4.2. Análisis Cuantitativo.......................................................................................................................... 26

3.5. Fuentes de Emisión ................................................................................................................................ 28

3.6. Receptores Discretos ............................................................................................................................ 30

3.7. Resultados............................................................................................................................................... 31

3.7.1. Material Particulado Respirable Fino (MP2,5) .................................................................................. 31

3.7.1.1. Resultados en Receptores Discretos ..................................................................................................... 31

3.7.1.2. Curvas de Isoconcentración .................................................................................................................. 32

3.7.2. Material Particulado Respirable (MP10) .......................................................................................... 34

3.7.2.1. Resultados en Receptores Discretos .................................................................................................... 34

3.7.2.2. Curvas de Isoconcentración .................................................................................................................. 35

3.8. Verificación Significancia Aporte MP2,5 y MP10 ................................................................................... 37

4. CONCLUSIONES .............................................................................................................................................. 38

5. REFERENCIAS .................................................................................................................................................. 38

ANEXOS ..................................................................................................................................................................... 38

3

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**ÍNDICE DE TABLAS**

Tabla 1 - Cronograma Fase de Construcción. ........................................................................................... 7
Tabla 2 - Cronograma Fase de Operación. ............................................................................................... 8
Tabla 3 - Cronograma Fase de Cierre. ...................................................................................................... 8
Tabla 4 - Normas de Calidad del Aire. .................................................................................................... 10
Tabla 5 - Estación Meteorológica Pudahuel (DMC). .............................................................................. 14
Tabla 6 - Resumen Datos Observados y Modelados en Estación Pudahuel (DMC). Periodo 01/01/22 al
31/12/22...................................................................................................................................................... 14
Tabla 7 - Series de Tiempo Observadas y Modeladas en Estación Pudahuel (DMC). Periodo 01/01/22 al
31/12/22.......................................................................................................................................................15
Tabla 8 - Ciclos Diarios Observados y Modelados en Estación Pudahuel (DMC). Periodo 01/01/22 al
31/12/22....................................................................................................................................................... 17
Tabla 9 - Rosas de Viento Observadas y Modeladas en Estación Pudahuel (DMC). Periodo 01/01/22 al
31/12/22...................................................................................................................................................... 20
Tabla 10 - Ciclos Estacionales Observados y Modelados en Estación Pudahuel (DMC). Periodo 01/01/22
al 31/12/22. ................................................................................................................................................. 24
Tabla 11 - Estadísticos análisis cuantitativo. Estación Pudahuel (DMC). ............................................... 26
Tabla 12 - Fuentes de Emisión. ................................................................................................................ 29
Tabla 13 - Receptores Discretos. ............................................................................................................ 30
Tabla 14 - Resultados Aporte Modelo en Receptores Discretos para MP2,5. .......................................31
Tabla 15 - Resultados Aporte Modelo en Receptores Discretos para MP10. ....................................... 34
Tabla 16 - Evaluación de aportes del proyecto sobre receptores de acuerdo a Tabla 2 del Criterio de
Evaluación en el SEIA “Impacto de emisiones en zonas saturadas por material particulado respirable
MP10 y material particulado fino respirable MP2,5” ............................................................................. 37

**ÍNDICE DE FIGURAS**

Figura 1 - Dominio de Modelación. .......................................................................................................... 11
Figura 2 - Estación Meteorológica Pudahuel (DMC). .............................................................................13
Figura 3 - Fuentes de Emisión. ................................................................................................................ 29
Figura 4 - Receptores Discretos. ............................................................................................................ 30
Figura 5 - Curva de Isoconcentración MP2,5 P98 24 horas. .................................................................. 32
Figura 6 - Curva de Isoconcentración MP2,5 Anual. .............................................................................. 33
Figura 7 - Curva de Isoconcentración MP10 P98 24 horas. ................................................................... 35
Figura 8 - Curva de Isoconcentración MP10 Anual. ............................................................................... 36

4

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**1.** **INTRODUCCIÓN**

En este informe se presenta la modelación de dispersión de contaminantes atmosféricos para el año
de mayor emisión asociado a la Declaración de Impacto Ambiental (DIA) del Proyecto “ _Planta_
_Fotovoltaica Chieti Solar_ ”, la cual fue ingresada al Sistema de Evaluación de Impacto Ambiental el 24
de Enero de 2024. El día 3 de Marzo de 2024, se emitió el Informe consolidado de solicitud de
aclaraciones, rectificaciones y/o ampliaciones a la DIA (ICSARA), en el cual se realizaron
observaciones principalmente al estudio de emisiones atmosféricas las cuales son subsanadas en su
totalidad y en consecuencia, considerando los cambios que tuvo dicho estudio, se presenta en este
informe la actualización de la Modelación de Dispersión de Contaminantes.

En primer lugar, se presentan los antecedentes generales del Proyecto; descripción, localización y
cronograma. Posteriormente, se presenta el desarrollo de la modelación de dispersión de
contaminantes atmosféricos, elaborada utilizando para ello el modelo refinado de calidad del aire
CALPUFF, en un dominio de modelación de 20x15 kilómetros, para el cual se definió una grilla de
receptores con resolución de 1x1 kilómetros. De manera adicional, se presenta la estimación del
aporte del proyecto en 4 receptores discretos, 3 que corresponden a puntos de interés identificados
en el estudio de ruido y 1 que corresponde a una estación de calidad del aire.

Con el fin de validar la información meteorológica modelada elaborada a partir del modelo WRF
( _Weather Research and Forecasting_ ), la cual se utiliza como información de entrada para el modelo de
calidad del aire CALPUFF, se presenta un análisis de incertidumbre, en el cual se compara de manera
cualitativa y cuantitativa la capacidad del modelo de representar variables meteorológicas de
superficie registradas en la estación meteorológica Pudahuel, de la Dirección Meteorológica de Chile
(DMC).

A partir de los resultados de la modelación, se presentan tablas con el aporte en concentración de
los diferentes contaminantes atmosféricos (Material Particulado Respirable Fino - MP2,5 y Material
Particulado Respirable - MP10) generados a consecuencia de la ejecución del año de mayor emisión
del Proyecto en cada receptor, y se las compara con las normativas de calidad del aire aplicables.
Adicionalmente, se presentan las curvas de isoconcentración para cada contaminante según
corresponda. Por último, se presentan las principales conclusiones del estudio.

Finalmente, es importante mencionar que este estudio fue realizado siguiendo los lineamientos de la
“Guía para el uso de modelos de calidad del aire en el SEIA” (SEA, 2023).

5

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**2.** **ANTECEDENTES GENERALES DEL PROYECTO**

**2.1.** **Descripción**
El proyecto _“Planta Fotovoltaica Chieti Solar”_ consiste en la construcción y operación de una central
solar fotovoltaica para la producción de 14,43 MWp de energía (potencia nominal instalada), y que
proveerá aproximadamente 9 MW (potencia neta) al Sistema Eléctrico Nacional (SEN).
Adicionalmente el Proyecto contará con un sistema de almacenamiento de energía mediante
baterías de iones de litio del tipo BESS (Battery Energy System Storage), lo que permitirá inyectar
parte de la energía producida durante el día en horarios de mayor demanda eléctrica, que
normalmente corresponden a periodos nocturnos. Es posible también que los sistemas BESS presten
otros tipos de servicio a la red, como control de tensión y frecuencia, recuperación de servicio, entre

otros.

El Proyecto para la producción de energía utilizará 20.664 paneles fotovoltaicos de 705 Wp de
potencia nominal (20.664 x 705 Wp = 14,57 MWp), los cuales estarán montados sobre estructuras
con seguimiento solar con eje este-oeste, agrupados en un total de 738 string (cantidad de paneles
fotovoltaicos conectados en paralelo) de 1x28 y 2x28 módulos, lo que en conjunto corresponde a la
potencia nominal. Luego, la transformación de la corriente continua (DC) generada por los paneles
fotovoltaicos a corriente alterna (AC) se realizará mediante inversores, mientras que el aumento a
media tensión (23 kV) se realizará por medio de transformadores.

Finalmente, la energía producida, convertida y transformada, será conducida por medio una línea de
media tensión aérea (línea de evacuación) de 23 kV y aproximadamente 570 metros de longitud,
hasta conectar con el SEN en un punto de conexión establecido, presente en el Anexo 2 Planos.

Además de los paneles fotovoltaicos y sus elementos de conexión, el presente Proyecto requerirá
de un cerco perimetral, un portón de acceso, equipos de videovigilancia y sistema de vigilancia
SCADA (Supervisor y Control And Data Acquisition).

**2.2.** **Localización**

El Proyecto se emplazará en un área rural, de acuerdo con lo establecido en el Plan Regulador
Comunal (PRC) de la comuna de Colina, al interior de las parcelas número 112-EV, 113-EV, 114-EV, 115EV, 138-EV, 139-EV, 140-EV, 141-EV, 142-EV, 145-EV, 146-EV, 148-EV, 149-EV, 151-EV, 152-EV, 154-EV, 155EV, 116-EV y 117-EV del plano sector El Valle archivado en este Conservador bajo el N° treinta y cuatro
mil seiscientos noventa y ocho-G de la comuna de Colina, región Metropolitana y parcelas número
218-LV, 219-LV, 220-LV, 221-LV, 222-LV, 223-LV y 224-LV del plano sector La Virgen archivado en este
Conservador bajo el N° treinta y cuatro mil seiscientos noventa y ocho -I, comuna de Colina, región
Metropolitana, todas las parcelas ubicadas en la comuna de Colina, Provincia de Chacabuco, Región
Metropolitana. En una superficie total de 19,62 hectáreas. Al proyecto se accede por un camino
derivado de la Avenida “El Valle”.

**2.3.** **Cronograma general**
La construcción se realizará en un plazo estimado máximo de seis (6) meses, mientras que la
operación del Proyecto estará programada para treinta (30) años bajo la modalidad de operación y
vigilancia remota y en tiempo real, no contemplándose la presencia de trabajadores en las
instalaciones, salvo para las labores de mantención. El Proyecto no requiere de sistemas particulares
de producción y distribución de agua potable y/o de recolección, tratamiento y disposición de aguas
servidas.

6

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**2.3.1.** **Fase de construcción**

Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de construcción, se establece el cronograma presentado en la Tabla 1:

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **2.3.1.** **Fase de construcción** Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de construcción, se establece el cronograma presentado en la Tabla 1: -->

**Tabla 1: - Cronograma Fase de Construcción.**

| Actividad | Mes 1 | Mes 2 | Mes 3 | Mes 4 | Mes 5 | Mes 6 |
| --- | --- | --- | --- | --- | --- | --- |
| Habilitación instalaciones de faena | <br> | <br> | <br> | <br> | <br> | <br> |
| Montaje instalación de faenas | <br> | <br> | <br> | <br> | <br> | <br> |
| Cierre perimetral y señalización |  |  |  |  |  |  |
| Corta o despeje de vegetación en el área del Proyecto | <br> | <br> | <br> | <br> | <br> | <br> |
| Habilitación de caminos | <br> | <br> | <br> | <br> | <br> | <br> |
| Atravieso vehicular | <br> | <br> | <br> | <br> | <br> | <br> |
| Preparación del terreno |  |  |  |  |  |  |
| Hincado de las estructuras de soporte y excavaciones de<br>cableado |  |  |  |  |  |  |
| Montaje de la línea de evacuación de media tensión |  |  |  |  |  |  |
| Montaje de estructuras de soporte e instalación de paneles<br>fotovoltaicos | <br> | <br> | <br> | <br> | <br> | <br> |
| Montaje de equipos y cabinas | <br> | <br> | <br> | <br> | <br> | <br> |
| Retiro de las instalaciones de faena |  |  |  |  |  |  |

<!-- Estadísticas: 12 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- 7 Modelación de Dispersión de Contaminantes -->
<!-- FIN TABLA 1 -->


Tabla 1 - Cronograma Fase de Construcción.

|Actividad|Mes 1|Mes 2|Mes 3|Mes 4|Mes 5|Mes 6|
|---|---|---|---|---|---|---|
|Habilitación instalaciones de faena|<br>|<br>|<br>|<br>|<br>|<br>|
|Montaje instalación de faenas|<br>|<br>|<br>|<br>|<br>|<br>|
|Cierre perimetral y señalización|||||||
|Corta o despeje de vegetación en el área del Proyecto|<br>|<br>|<br>|<br>|<br>|<br>|
|Habilitación de caminos|<br>|<br>|<br>|<br>|<br>|<br>|
|Atravieso vehicular|<br>|<br>|<br>|<br>|<br>|<br>|
|Preparación del terreno|||||||
|Hincado de las estructuras de soporte y excavaciones de<br>cableado|||||||
|Montaje de la línea de evacuación de media tensión|||||||
|Montaje de estructuras de soporte e instalación de paneles<br>fotovoltaicos|<br>|<br>|<br>|<br>|<br>|<br>|
|Montaje de equipos y cabinas|<br>|<br>|<br>|<br>|<br>|<br>|
|Retiro de las instalaciones de faena|||||||

7

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**2.3.2.** **Fase de operación**

Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de operación, se establece el cronograma presentado en la Tabla 2:

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **2.3.2.** **Fase de operación** Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de operación, se establece el cronograma presentado en la Tabla 2: -->

**Tabla 2: - Cronograma Fase de Operación.**

| Actividades | Años | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividades** | **1 **<br> | **2 **<br> | **3 **<br> | **... **<br> | **10**<br> | **20**<br> | **... **<br> | **30**<br> |
| Prueba y puesta en servicio | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| Operación planta | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| Actividades de mantención |  |  |  |  |  |  |  |  |
| Instalación módulos de almacenamiento de<br>baterías* | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| Desenergización de la planta |  |  |  |  |  |  |  |  |

<!-- Estadísticas: 6 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **2.3.3.** **Fase de cierre** Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de cierre, se establece el cronograma presentado en la Tabla 3: -->
<!-- FIN TABLA 2 -->


Tabla 2 - Cronograma Fase de Operación.

|Actividades|Años|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Actividades**|**1 **<br>|**2 **<br>|**3 **<br>|**... **<br>|**10**<br>|**20**<br>|**... **<br>|**30**<br>|
|Prueba y puesta en servicio|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|
|Operación planta|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|
|Actividades de mantención|||||||||
|Instalación módulos de almacenamiento de<br>baterías*|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|
|Desenergización de la planta|||||||||

**2.3.3.** **Fase de cierre**

Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de cierre, se establece el cronograma presentado en la Tabla 3:

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **2.3.3.** **Fase de cierre** Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de cierre, se establece el cronograma presentado en la Tabla 3: -->

**Tabla 3: - Cronograma Fase de Cierre.**

| Actividad | Año 1 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **1 ** | **2 ** | **3 ** | **4 ** | **... ** | **12** |
| Habilitación instalación de faena |  |  |  |  |  |  |
| Actividades de desmantelamiento |  |  |  |  |  |  |
| Actividades de descompactación y revegetación |  |  |  |  |  |  |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- 8 Modelación de Dispersión de Contaminantes -->
<!-- FIN TABLA 3 -->


Tabla 3 - Cronograma Fase de Cierre.

|Actividad|Año 1|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Actividad**|**1 **|**2 **|**3 **|**4 **|**... **|**12**|
|Habilitación instalación de faena|||||||
|Actividades de desmantelamiento|||||||
|Actividades de descompactación y revegetación|||||||

8

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**3.** **MODELACIÓN DE DISPERSIÓN DE CONTAMINANTES**

**3.1.** **Descripción de los modelos utilizados.**

**3.1.1.** **WRF**

El modelo WRF (por sus siglas en inglés _Weather Research and Forecasting Model_ ), es uno de los
modelos meteorológicos de pronóstico más avanzados y completos, operado y mantenido por el
_National Center for Atmospheric Research y el National Oceanic and Atmospheric Administration_
(NCAR/NOAA) de los Estados Unidos, es utilizado a nivel global y se encuentra en continuo
desarrollo.

De acuerdo con el inciso 4.3.1 de la “Guía para el uso de modelos de calidad del aire en el SEIA” (SEA,
2023), el modelo numérico recomendado para la generación de datos meteorológicos es WRF, el
cual fue utilizado para generar la grilla de datos meteorológicos para un año completo (2022), la cual
se utiliza como dato de entrada para la modelación de dispersión de contaminantes.

Por otro lado, el inciso 4.5 de la misma guía indica que los modelos deben ser configurados para cada
aplicación, considerando periodo y dominio geográfico de simulación, resolución espacial horizontal
y vertical, parametrizaciones físicas, entre otros. Para verificar todo lo anterior, se adjunta con este
documento el “ _Anexo Digital A - Archivos Digitales de Modelación ICSARA 1_ ”, donde se entrega el
respaldo de los archivos utilizados para este estudio.

**3.1.2.** **CALPUFF**

Para ejecutar la modelación de calidad del aire, se ha determinado utilizar el modelo tipo puff
llamado CALPUFF, el cual corresponde a un modelo de libre disposición, desarrollado por _Exponent_
Inc, distribuido por _Atmospheric Studies Group - TRC Solutions_ . Este modelo ha sido adoptado por la
US-EPA como un modelo adecuado para simular el transporte de contaminantes de largo alcance.
CALPUFF es un modelo Lagrangiano-Gaussiano, no estacionario y multicapa que tiene la capacidad
de modelar múltiples especies, pudiendo simular los efectos del tiempo y en el espacio, de las
diversas condiciones meteorológicas en el transporte de contaminantes. Dentro de sus principales
capacidades se tiene la simulación de procesos complejos (fumigación, estancamiento y
recirculación) y la incorporación de efectos de terreno complejo en la dispersión. Posee un módulo
para realizar el post-procesamiento de datos, llamado CALPOST, el cual permite calcular las
concentraciones en los receptores discretos, permitiendo de esta forma gestionar los datos para
cada contaminante y poder así comparar los resultados del modelo con normativas de calidad del
aire vigentes y aplicables al Proyecto.

De acuerdo con el inciso 3.2 de la “Guía para el uso de modelos de calidad del aire en el SEIA” (SEA,
2023), el modelo tipo “puff” recomendado corresponde a CALPUFF, el cual en base a dicha
recomendación es el modelo seleccionado para realizar el presente estudio, toda vez que la zona de
emplazamiento del Proyecto corresponde una topografía compleja.

9

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

**3.2.** **Normas de calidad del aire**

Adenda 1

Mayo 2024

A continuación, en la Tabla 4 se presenta la normativa de calidad del aire vigente a utilizar para

comparar los resultados de la modelación y de esta forma verificar cumplimiento normativo.

Tabla 4 - Normas de Calidad del Aire.

|Contaminante|Decreto<br>Aplicable|Norma|Col4|Periodo de Evaluación de<br>Cumplimiento de Norma|
|---|---|---|---|---|
|**Contaminante**|**Decreto**<br>**Aplicable**|**Valor**|**Unidad**|**Unidad**|
|Material Particulado<br>Respirable Fino (MP2,5)|Decreto<br>Supremo<br>N°12/2010|50|μg/m3|Percentil 98 de las concentraciones de<br>24 horas|
|Material Particulado<br>Respirable Fino (MP2,5)|Decreto<br>Supremo<br>N°12/2010|20|20|Concentración anual|
|Material Particulado<br>Respirable (MP10)|Decreto<br>Supremo<br>N°12/2022|130|μg/m3N|Percentil 98 de las concentraciones de<br>24 horas|
|Material Particulado<br>Respirable (MP10)|Decreto<br>Supremo<br>N°12/2022|50|50|Concentración anual|

**3.3.** **Dominio de Modelación**

En la Figura 1 se presenta el dominio de modelación, que corresponde a un área de 20x15 km con 300

celdas de 1x1 km. El dominio cubre las principales fuentes de emisión del Proyecto, receptores de

interés identificados en el estudio de ruido y además la ubicación de una estación meteorológica con

datos de suficiente disponibilidad y calidad para elaborar el análisis de incertidumbre.

10

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Figura 1 - Dominio de Modelación.

Adenda 1

Mayo 2024

11

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

**3.4.** **Análisis de Incertidumbre**

Adenda 1

Mayo 2024

En base al inciso 6 de la “Guía para el uso de modelos de calidad del aire en el SEIA” (SEA, 2023), todos
los modelos tienen asociados errores e incertidumbres, por lo que es de gran importancia evaluar
dichos errores comparando los resultados del modelo con las observaciones en forma cualitativa y

cuantitativa.

Con el fin de validar la capacidad del modelo WRF de representar la meteorología local, se presenta
en este inciso el análisis de incertidumbre meteorológico. Para desarrollar el análisis, se ha
determinado utilizar una estación meteorológica dentro del dominio de modelación con información
cuya calidad y disponibilidad se ajustan para un análisis de este tipo. La estación utilizada para el
análisis corresponde a la Estación Pudahuel (DMC) ubicada en la comuna de Pudahuel, propiedad de
la Dirección Meteorológica de Chile y operada por la misma entidad, cuyos datos son de acceso
público a través de su sitio web [1] .Los datos modelados se extraen a partir de los resultados del modelo
WRF para el mismo punto donde está ubicada la estación.

Cabe mencionar que, ante la indisponibilidad de datos públicos de meteorología de altura observados
dentro del dominio de modelación, se presenta el análisis de incertidumbre con enfoque en la
comparación de variables meteorológicas de superficie.

1 [https://climatologia.meteochile.gob.cl/application/informacion/fichaDeEstacion/330021](https://climatologia.meteochile.gob.cl/application/informacion/fichaDeEstacion/330021)

12

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

En la Figura 2 se presenta un mapa con la ubicación de la estación meteorológica respecto a la
ubicación del Proyecto:

Figura 2 - Estación Meteorológica Pudahuel (DMC).

13

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

A continuación, en la Tabla 5 se presentan las coordenadas de ubicación de la estación, el periodo de
monitoreo considerado para el estudio y las variables meteorológicas disponibles para analizar.
Luego, en la Tabla 6 se presenta un resumen con datos de interés para las variables analizadas.

Tabla 5 - Estación Meteorológica Pudahuel (DMC).

|Estación|Coordenadas UTM WGS 84 - 19S|Col3|Periodo considerado<br>para el análisis|Variables meteorológicas de<br>superficie|
|---|---|---|---|---|
|**Estación**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Pudahuel<br>(DMC)|333.699|6.305.342|01/01/22 - 31/12/22|- Velocidad del viento (m/s)<br>- Dirección del viento (°)<br>- Temperatura (°C)|

Tabla 6 - Resumen Datos Observados y Modelados en Estación Pudahuel (DMC). Periodo

01/01/22 al 31/12/22.

|Variable|Parámetro|Observado|Modelado|
|---|---|---|---|
|Velocidad del Viento|N° Datos Disponibles|8.760|8.760|
|Velocidad del Viento|N° Datos Válidos|7.439|8.760|
|Velocidad del Viento|Porcentaje de Datos Válidos|85%|100%|
|Velocidad del Viento|Promedio (m/s)|3,0|1,8|
|Velocidad del Viento|Máximo (m/s)|10,3|8,0|
|Velocidad del Viento|Mínimo (m/s)|0,0|0,0|
|Velocidad del Viento|Porcentaje de Calmas|2%|19%|
|Dirección del Viento|N° Datos Disponibles|8.760|8.760|
|Dirección del Viento|N° Datos Válidos|7.439|8.760|
|Dirección del Viento|Porcentaje de Datos Válidos|85%|100%|
|Temperatura|N° Datos Disponibles|88|8.760|
|Temperatura|N° Datos Válidos|8.760|8.760|
|Temperatura|Porcentaje de Datos Válidos|100%|100%|
|Temperatura|Promedio (m/s)|15,1|13,7|
|Temperatura|Máximo (m/s)|35,5|28,9|
|Temperatura|Mínimo (m/s)|-2,5|0,3|

**3.4.1.** **Análisis Cualitativo**

A continuación, se presenta el análisis de incertidumbre cualitativo, cuyo objetivo corresponde a
comparar las series de tiempo, ciclos diarios, rosas de viento y ciclos estacionales observados y
modelados para las variables meteorológicas de superficie de interés disponibles; velocidad del
viento y dirección del viento.

14

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**3.4.1.1.** **Series de Tiempo**

A modo de verificación de la completitud del set de datos utilizados en el análisis de incertidumbre, en la **¡Error! La autoreferencia al marcador no es válida.**
se presenta la comparación de las series de tiempo observadas y modeladas para las variables meteorológicas velocidad del viento, dirección del viento y
temperatura. De la tabla se puede comprobar una alta completitud de datos observados, los que presentan patrones similares a las series de tiempo
modeladas. A pesar de lo anterior, se comprueba que la estación presenta ausencia de datos de velocidad y dirección del viento durante enero y parte del
mes de febrero del año 2022 lo que pudo deberse a problemas en el funcionamiento del sensor que registra estas variables. Lo anterior, explica la
disponibilidad de datos de 85% presentada en la Tabla 6.

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Estación|Coordenadas UTM WGS 84 - 19S|Col3|Periodo considerado<br>para el análisis|Variables meteorológicas de<br>superficie| |---|---|---|---|---| |**Estación**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**| |Pudahuel<br>(DMC)|333.699|6.305.342|01/01/22 - 31/12/22|- Velocidad del viento (m/s)<br>- Dirección del viento (°)<br>- Temperatura (°C)| -->

**Tabla 6: - Resumen Datos Observados y Modelados en Estación Pudahuel (DMC). Periodo**

| Variable | Parámetro | Observado | Modelado |
| --- | --- | --- | --- |
| Velocidad del Viento | N° Datos Disponibles | 8.760 | 8.760 |
| Velocidad del Viento | N° Datos Válidos | 7.439 | 8.760 |
| Velocidad del Viento | Porcentaje de Datos Válidos | 85% | 100% |
| Velocidad del Viento | Promedio (m/s) | 3,0 | 1,8 |
| Velocidad del Viento | Máximo (m/s) | 10,3 | 8,0 |
| Velocidad del Viento | Mínimo (m/s) | 0,0 | 0,0 |
| Velocidad del Viento | Porcentaje de Calmas | 2% | 19% |
| Dirección del Viento | N° Datos Disponibles | 8.760 | 8.760 |
| Dirección del Viento | N° Datos Válidos | 7.439 | 8.760 |
| Dirección del Viento | Porcentaje de Datos Válidos | 85% | 100% |
| Temperatura | N° Datos Disponibles | 88 | 8.760 |
| Temperatura | N° Datos Válidos | 8.760 | 8.760 |
| Temperatura | Porcentaje de Datos Válidos | 100% | 100% |
| Temperatura | Promedio (m/s) | 15,1 | 13,7 |
| Temperatura | Máximo (m/s) | 35,5 | 28,9 |
| Temperatura | Mínimo (m/s) | -2,5 | 0,3 |

<!-- Estadísticas: 16 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **3.4.1.** **Análisis Cualitativo** A continuación, se presenta el análisis de incertidumbre cualitativo, cuyo objetivo corresponde a comparar las series de tiempo, ciclos diarios, rosas de viento y ciclos estacionales observados y -->
<!-- FIN TABLA 6 -->


Tabla 7 - Series de Tiempo Observadas y Modeladas en Estación Pudahuel (DMC). Periodo 01/01/22 al 31/12/22.

|Variable|Observado|Modelado|
|---|---|---|
|Velocidad del<br>Viento|||

15

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

|Variable|Observado|Modelado|
|---|---|---|
|Dirección del<br>Viento|||
|Temperatura|||

16

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**3.4.1.2.** **Ciclos Diarios**

En la Tabla 8 se presenta la comparación de los ciclos diarios, los que permiten visualizar los cambios en las variables meteorológicas a lo largo del día. Es
importante mencionar que, con el objetivo de presentar ciclos adecuados y poder compararlos con los ciclos modelados, para el periodo entre enero y
febrero del año 2022 donde se registró ausencia de datos, se completó la serie con los datos del año 2021 para el mismo periodo, asumiendo que la velocidad
y dirección del viento no deberían cambiar significativamente de un año a otro, lo anterior permitirá un mejor análisis de incertidumbre.

Tabla 8 - Ciclos Diarios Observados y Modelados en Estación Pudahuel (DMC). Periodo 01/01/22 al 31/12/22.

|Variable|Observado|Modelado|
|---|---|---|
|Velocidad del<br>Viento|||

17

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

|Variable|Observado|Modelado|
|---|---|---|
|Dirección del<br>Viento|||
|Temperatura|||

18

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

A continuación, se describe la comparación de los ciclos diarios presentados:

Adenda 1

Mayo 2024

- **Ciclos diarios de velocidad del viento:** se aprecia que el modelo tiene la capacidad de
representar los momentos del día donde se dan las mayores velocidades de viento, los que
corresponden al periodo diurno, particularmente en horas de la tarde. Por su parte,
representa adecuadamente los periodos del día con menores velocidades del viento, los que
ocurren durante la madrugada y la noche. A su vez, se aprecia que el modelo meteorológico
tiende a subestimar la magnitud de la velocidad del viento observada en la Estación Pudahuel
(DMC), particularmente durante la tarde.

- **Ciclos diarios de dirección del viento:** en los histogramas presentados es posible apreciar
que el modelo representa de manera precisa los vientos predominantes observados, tanto
en dirección como en frecuencia particularmente entre las 08:00 y las 21:00 horas.

- **Ciclos diarios de temperatura:** se aprecia que el modelo tiene la capacidad de representar
los momentos del día donde se dan las mayores temperaturas, los que corresponden al
periodo diurno, particularmente a partir del mediodía y durante la tarde. Por su parte,
representa adecuadamente los periodos del día con menores temperaturas, los que ocurren
durante la madrugada y la noche. A su vez, se aprecia que el modelo meteorológico tiende a
subestimar ligeramente la magnitud de la temperatura observada en la Estación Pudahuel
(DMC), particularmente durante la tarde.

19

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**3.4.1.3.** **Rosas de Viento**

En la Tabla 9 se presenta la comparación de rosas de viento observadas y modeladas para el periodo de estudio. En primer lugar, se muestran rosas para el
año completo (considerando todos los datos) y luego se presenta la comparación de rosas separada por periodo del día; madrugada, mañana, tarde y
noche. Es importante mencionar que con el objetivo de presentar rosas adecuadas y poder compararlas con las rosas modeladas, para el periodo entre
enero y febrero del año 2022 donde se registró ausencia de datos, se completó la serie con los datos del año 2021 para el mismo periodo, asumiendo que la
velocidad y dirección del viento no deberían cambiar significativamente de un año a otro, lo anterior permitirá un mejor análisis de incertidumbre.

Tabla 9 - Rosas de Viento Observadas y Modeladas en Estación Pudahuel (DMC). Periodo 01/01/22 al 31/12/22.

|Periodo|Observado|Modelado|
|---|---|---|
|Año<br>completo<br>(todos los<br>datos)|||

20

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

|Periodo|Observado|Modelado|
|---|---|---|
|Madrugada<br>(00:00-<br>05:00)|||
|Mañana<br>(06:00-<br>11:00)|||

21

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

|Periodo|Observado|Modelado|
|---|---|---|
|Tarde<br>(12:00-<br>17:00)|||
|Noche<br>(18:00-<br>23:00)|||

22

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

A continuación, se presenta la descripción de la comparación de las rosas de viento observadas y
modeladas:

 - **Año completo:** en ambas figuras se aprecia predominancia de vientos provenientes del
sursuroeste, sur y sursureste. El modelo tiende a subestimar la velocidad del viento
ligeramente y a la vez a subestimar los vientos provenientes del sursureste. Sin embargo, se
aprecia una alta capacidad del modelo para representar la dirección y velocidad del viento
predominante para el set completo de datos.

 - **Madrugada (00:00-05:00):** el modelo representa de manera correcta la predominancia de
vientos observados, los cuales provienen principalmente desde el sursureste. Se aprecia que
el modelo subestima ligeramente la velocidad del viento y sobrestima la frecuencia de
vientos sureste en desmedro de una subestimación de vientos del sur. Sin embargo, estos
vientos ocurren con mucha menor frecuencia y la capacidad del modelo para representar la
dirección y velocidad del viento durante la madrugada es satisfactoria.

 - **Mañana (06:00-11:00):** el modelo representa de buena forma los vientos observados durante
la mañana lo que se refleja en la similitud de ambas rosas. A nivel específico el modelo
subestima ligeramente la velocidad del viento y sobrestima la frecuencia de vientos
provenientes del sursuroeste mientras que subestima la frecuencia de vientos provenientes
del sursuroeste y también del norte y nornoreste ligeramente. Al igual que en la madrugada,
el modelo representa satisfactoriamente la dirección y velocidad del viento en la mañana.

 - **Tarde (12:00-17:00):** durante la tarde el modelo subestima la velocidad del viento, sobrestima
la frecuencia de los vientos provenientes del sursuroeste y subestima la frecuencia de los
vientos provenientes del sur y del suroeste. Al igual que en la madrugada y en la mañana, el
modelo subestima ligeramente la velocidad del viento. A pesar de lo anterior, se demuestra
la correcta capacidad del modelo de representar la predominancia de vientos provenientes
del segundo y tercer cuadrante, además de interpretar el aumento en velocidad del viento
observado respecto a la madrugada y la mañana.

 - **Noche (18:00-23:00):** el modelo representa de manera satisfactoria los vientos provenientes
del segundo cuadrante, sin embargo, al igual que el resto del día el modelo subestima la
magnitud de la velocidad del viento. Particularmente en este horario nocturno, el modelo
sobrestima la frecuencia de los vientos provenientes del sureste y subestima vientos que
provienen del sursureste y sursuroeste.

En términos generales se aprecia de forma cualitativa que el modelo representa de manera adecuada
los vientos predominantes, tal y como se mostró en los ciclos diarios presentados en el inciso
anterior, donde en este caso se vuelve a demostrar la correcta capacidad del modelo de representar
las direcciones y velocidades de viento observadas, para las cuales existen ligeras subestimaciones
de la magnitud de la velocidad del viento, lo cual se mantiene dentro de un rango normal y aceptable
para un modelo meteorológico de este tipo.

A su vez, se demostró que el modelo muestra un mejor rendimiento en horas de la mañana y la tarde,
lo que coincide con los momentos del día donde se llevará a cabo la jornada laboral del Proyecto. Por
lo que se puede trabajar bajo el supuesto de que el periodo a modelar corresponde al cual el modelo
representa de mejor manera la meteorología de superficie observada.

23

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

**3.4.1.1.** **Ciclo Estacional**

Adenda 1

Mayo 2024

En la Tabla 10 se presenta la comparación del ciclo estacional de velocidad y dirección del viento, el que permite visualizar los cambios en las variables
meteorológicas a lo largo del año. Es importante mencionar que con el objetivo de presentar ciclos adecuados y poder compararlos con los ciclos modelados,
para el periodo entre enero y febrero del año 2022 donde se registró ausencia de datos, se completó la serie con los datos del año 2021 para el mismo
periodo, asumiendo que la velocidad y dirección del viento no deberían cambiar significativamente de un año a otro, lo anterior permitirá un mejor análisis

de incertidumbre.

Tabla 10 - Ciclos Estacionales Observados y Modelados en Estación Pudahuel (DMC). Periodo 01/01/22 al 31/12/22.

|Variable|Observado|Modelado|
|---|---|---|
|Velocidad y<br>dirección del<br>viento|||

24

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

|Variable|Observado|Modelado|
|---|---|---|
|Temperatura|||

A continuación, se presenta la descripción de la comparación de los ciclos estacionales presentados:

Adenda 1

Mayo 2024

- **Ciclo estacional de vientos:** las flechas indican que el modelo presenta un buen desempeño a la hora de representar la dirección del viento observada

a lo largo de todo el año, donde se ve que predominan provenientes del sur, sursuroeste y sursureste, sin embargo, se aprecian algunas diferencias

respecto a la magnitud de la velocidad del viento, donde el modelo sobrestima esta variable ligeramente respecto a los registros observados. A

pesar de lo anterior, el modelo representa de manera adecuada los momentos del día y del año donde se esperan mayores velocidades de viento,

las que ocurren principalmente en el periodo diurno durante los meses de verano.

- **Ciclo estacional de temperatura:** se demuestra que el modelo logra representar de manera satisfactoria la temperatura observada, toda vez que

en ambas figuras se aprecian las mayores temperaturas en el periodo diurno para los meses de verano y primavera. Por el contrario, ambas figuras

muestran las menores temperaturas en el periodo nocturno en los meses de invierno.

25

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**3.4.2.** **Análisis Cuantitativo**

Para el análisis cuantitativo se presenta el cálculo de los estadísticos indicados en el inciso 6.2.2 de la
“Guía para el uso de modelos de calidad del aire en el SEIA” (SEA, 2023); sesgo, coeficiente de
correlación y error medio cuadrático, los cuales se definen a continuación:

 - **Sesgo:** representa la tendencia del modelo meteorológico a subestimar o sobrestimar
los datos observados según se muestra en la siguiente ecuación, si su resultado es
negativo significa que el modelo subestima los valores observados y si el resultado es
positivo significa que el modelo sobrestima los valores observados (N: cantidad de
datos, M: valor modelado, O: valor observado):

N

Sesgo = [1]

N [∑(M] [i] [ −O] [i] [)]

i=1

 - **Coeficiente de correlación (r):** a partir de este coeficiente se mide la relación lineal entre
la variable generada por el modelo de meteorológico y la variable observada en la
estación de superficie. El resultado de este coeficiente se encuentra en el intervalo [-1,
1], mientras más cercano a 1 esté el valor mejor será la correlación entre las variables. La
fórmula para calcularlo es la siguiente (N: cantidad de datos, M valor modelado, O: Valor
observado, σ: Desviación Estándar).

N

[1]

N [ ∑] [(][M] [i] [ −] σ [M)(] σ [O] [i] [ −] [O)]

r = [1]

i=1

σ M σ o

- **Error medio cuadrático:** representa la diferencia promedio entre los valores promedios
del modelo de pronóstico y observados, el cual se calcula según la siguiente ecuación (N:
cantidad de datos, M: valor modelado, O: valor observado):

N

i=1

ECM = √∑

N

(M i −O i ) [2]

N

i=1

A continuación, en la Tabla 11 se presentan los resultados del cálculo de estadísticos para la variable
meteorológica de superficie velocidad del viento y temperatura, comparando todos los datos
observados y modelados en la Estación Pudahuel (DMC) tanto para las series de tiempo como para
los ciclos diarios:

Tabla 11 - Estadísticos análisis cuantitativo. Estación Pudahuel (DMC).

|Estadístico|Velocidad del Viento (m/s)|Col3|Temperatura (°C)|Col5|
|---|---|---|---|---|
|**Estadístico**|**Serie de**<br>**Tiempo**|**Ciclo Diario**|**Serie de**<br>**Tiempo**|**Ciclo Diario**|
|Sesgo|-1,36|-1,37|-1,37|-1,37|
|Error Cuadrático Medio|1,95|1,48|3,19|2,18|
|Coeficiente de Correlación|0,75|0,94|0,93|0,94|

26

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

De la tabla anterior, se aprecia que el modelo tiene un sesgo de -1,36 m/s para la serie de tiempo y de
-1,37 m/s para el ciclo diario de la velocidad del viento respectivamente, lo que indica que el modelo
subestima ligeramente esta variable, tal y como se mostró en el análisis cualitativo. Por su parte, se
tiene un alto coeficiente de correlación (0,75 para la serie de tiempo y 0,94 para el ciclo diario) y un
error cuadrático medio de baja magnitud (1,95 m/s para la serie de tiempo y 1,48 m/s para el ciclo
diario). Lo anterior implica que el modelo si bien subestima la velocidad de viento observada, tiene
la capacidad suficiente para representar los cambios en tendencias y logra replicar el ciclo diario
observado para esta variable. Tal y como se mostró en el análisis cualitativo, representa de manera
satisfactoria los periodos del día con bajas y altas velocidades de viento.

Respecto a la temperatura, el modelo tiene un sesgo de -1,37°C para la serie de tiempo y el ciclo diario,
lo que indica que el modelo subestima ligeramente esta variable, tal y como se mostró en el análisis
cualitativo. Por su parte, se tiene un alto coeficiente de correlación (0,93 para la serie de tiempo y
0,94 para el ciclo diario) y un error cuadrático medio de baja magnitud (3,19°C para la serie de tiempo
y 2,18°C para el ciclo diario). Lo anterior implica que el modelo si bien subestima la temperatura
observada, tiene la capacidad suficiente para representar los cambios en tendencias y logra replicar
el ciclo diario observado para esta variable. Tal y como se mostró en el análisis cualitativo, representa
de manera satisfactoria los periodos del día con bajas y altas temperaturas.

A modo de resumen, se aprecia de manera cualitativa y cuantitativa que el modelo meteorológico
WRF tiene la capacidad de representar las variables meteorológicas de superficie analizadas
(velocidad del viento, dirección del viento y temperatura) de manera similar a lo observado en la
estación meteorológica Pudahuel (DMC) para el periodo de estudio (año 2022), particularmente
durante las horas donde se realizarán las actividades (periodo diurno), por lo que se cuenta con un
sustento técnico que respalda el uso de la información meteorológica modelada como dato de
entrada para la modelación de calidad del aire presentada a continuación en los siguientes incisos.

27

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

**3.5.** **Fuentes de Emisión**

Adenda 1

Mayo 2024

Con el objetivo de estimar la dispersión de contaminantes atmosféricos que será generada a
consecuencia de la ejecución del Proyecto, se deben modelar las fuentes de emisión asociadas al
mismo. Para modelar el peor escenario, se han considerado las fuentes asociadas al primer año del
Proyecto (6 meses fase de construcción y 6 meses fase de operación), que corresponde al año de
mayor emisión.

En base a información georreferenciada del Proyecto, se han diseñado las siguientes fuentes de
emisión que serán consideradas para la modelación:

 - **Fuentes Areales:** A estas fuentes se les asignan las emisiones asociadas a movimientos
de tierra, utilización de maquinaria y grupos generadores.

 - **Fuentes de Camino:** A estas fuentes se le asignan las emisiones asociadas a combustión
(motores vehículos) y resuspensión de polvo por tránsito vehicular (tránsito no
pavimentados y tránsito pavimentados).

De esta forma, se han definido 2 tipos de fuentes principales asociadas al Proyecto a las que serán
asignadas emisiones de acuerdo con sus características y su variabilidad temporal, para esta última
con el fin de modelar un escenario conservador se configuró el modelo tomando en cuenta los 12
meses del año, jornada laboral de 25 días al mes, 8 horas de trabajo diarias.

De esta forma, el cálculo de la tasa de emisión para cada contaminante se realiza según las siguientes
fórmulas.

**Fuentes Areales:**

[⋅1 (día)] 8 (horas) [⋅1 (hora)] 3600 (seg)

[⋅1 (hora)] 3600 (seg) [⋅10] 1 (t) [6] [(g)]

1 (t)

[⋅1 (mes)] 25 (días) [⋅1 (día)] 8 (horas)

[g]

sm [2] [) = Emisión ] ~~[( ]~~ [t]

1 1 (año)

Área (m [2] ) [⋅] 12 (meses) [⋅1 (mes)] 25 (días)

Tasa de Emisión ( [g]

1
año [t] [) ⋅]

**Fuentes Caminos:**

[⋅1 (día)] 8 (horas) [⋅1 (hora)] 3600 (seg)

[⋅1 (hora)] 3600 (seg) [⋅10] 1 (t) [6] [(g)]

1 (t)

[g]

sm [) = Emisión ] ~~[( ]~~ [t]

[⋅1 (mes)] 25 (días) [⋅1 (día)] 8 (horas)

Tasa de Emisión ( [g]

1 1 (año)
año [t] [) ⋅] Largo (m) [⋅] 12 (meses) [⋅1 (mes)] 25 (días)

El detalle de cada fuente, tipo, dimensiones, emisiones totales (obtenidas a partir del estudio de
estimación de emisiones) y tasas de emisión se presenta a continuación en la Tabla 12. Por su parte,

<!-- INICIO TABLA 12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Modelación de Dispersión de Contaminantes _DIA “Planta Fotovoltaica Chieti Solar”_ -->

**Tabla 12: - Fuentes de Emisión.**

| Fuente | Tipo | Dimensiones | Col4 | Emisiones Totales (t/año) | Col6 | Tasas de Emisión | Col8 | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | **Tipo** | **Largo (m)** | **Área (m2) ** | **PM2.5** | **PM10** | **PM2.5** | **PM10** | **PM10** |
| Ruta 1 | Camino | 24.299,9 | - | 0,02 | 0,07 | 1,00E-07 | 3,38E-07 | g/sm |
| Ruta 2. A | Camino | 3.394,2 | - | 4,23E-03 | 0,02 | 1,44E-07 | 5,62E-07 | g/sm |
| Ruta 2. B | Camino | 22.720,3 | - | 3,25E-03 | 0,01 | 1,65E-08 | 5,59E-08 | g/sm |
| Ruta 3. A | Camino | 28.361,0 | - | 3,20E-03 | 0,01 | 1,31E-08 | 4,42E-08 | g/sm |
| Ruta 4. A | Camino | 14.092,7 | - | 3,73E-03 | 0,01 | 3,07E-08 | 1,04E-07 | g/sm |
| Ruta 5. A | Camino | 21.255,7 | - | 3,56E-04 | 1,20E-03 | 1,94E-09 | 6,56E-09 | g/sm |
| Ruta 6 | Camino | 2.543,6 | - | 0,07 | 0,68 | 3,10E-06 | 3,08E-05 | g/sm |
| Proyecto | Área | - | 194.436,6 | 0,14 | 0,32 | 8,29E-08 | 1,90E-07 | g/sm2 |

<!-- Estadísticas: 9 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Figura 3 - Fuentes de Emisión. 29 -->
<!-- FIN TABLA 12 -->

en la Figura 3 se presenta un mapa con la ubicación de cada fuente:

28

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Tabla 12 - Fuentes de Emisión.

Adenda 1

Mayo 2024

|Fuente|Tipo|Dimensiones|Col4|Emisiones Totales (t/año)|Col6|Tasas de Emisión|Col8|Unidad|
|---|---|---|---|---|---|---|---|---|
|**Fuente**|**Tipo**|**Largo (m)**|**Área (m2) **|**PM2.5**|**PM10**|**PM2.5**|**PM10**|**PM10**|
|Ruta 1|Camino|24.299,9|-|0,02|0,07|1,00E-07|3,38E-07|g/sm|
|Ruta 2. A|Camino|3.394,2|-|4,23E-03|0,02|1,44E-07|5,62E-07|g/sm|
|Ruta 2. B|Camino|22.720,3|-|3,25E-03|0,01|1,65E-08|5,59E-08|g/sm|
|Ruta 3. A|Camino|28.361,0|-|3,20E-03|0,01|1,31E-08|4,42E-08|g/sm|
|Ruta 4. A|Camino|14.092,7|-|3,73E-03|0,01|3,07E-08|1,04E-07|g/sm|
|Ruta 5. A|Camino|21.255,7|-|3,56E-04|1,20E-03|1,94E-09|6,56E-09|g/sm|
|Ruta 6|Camino|2.543,6|-|0,07|0,68|3,10E-06|3,08E-05|g/sm|
|Proyecto|Área|-|194.436,6|0,14|0,32|8,29E-08|1,90E-07|g/sm2|

Figura 3 - Fuentes de Emisión.

29

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

**3.6.** **Receptores Discretos**

Adenda 1

Mayo 2024

A partir del estudio de ruido, se han identificado 3 receptores discretos cercanos al Proyecto.
Adicionalmente, se considera como receptor discreto la Estación Quilicura (SINCA). La Tabla 13
resume los receptores y sus correspondientes coordenadas de ubicación geográfica:

Tabla 13 - Receptores Discretos.

|ID<br>Receptor|Descripción|Coordenadas de Ubicación<br>(Datum WGS84)|Col4|
|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|
|R1|Receptor 1|346.995|6.316.063|
|R2|Receptor 2|345.810|6.315.262|
|R3|Receptor 3|345.264|6.313.891|
|R4|Estación Quilicura (SINCA)|339.594|6.308.625|

Por su parte, en la Figura 4 se presenta un mapa con la ubicación de los receptores discretos, en
conjunto con las fuentes de emisión definidas para el proyecto:

Figura 4 - Receptores Discretos.

30

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

**3.7.** **Resultados**

Adenda 1

Mayo 2024

En este inciso se presentan los resultados de la modelación de dispersión de contaminantes para el
año de mayor emisión del Proyecto (año 1 el cual incluye construcción + operación) de acuerdo con
la información presentada en los incisos anteriores.

Para cada contaminante se presenta una tabla que compara el aporte del modelo en concentración
para cada receptor con la normativa de calidad del aire de acuerdo con las que fueron presentadas
en la Tabla 4, posteriormente se presentan las curvas de isoconcentración, las que permiten
visualizar la distribución del contaminante en el dominio de modelación.

**3.7.1.** **Material Particulado Respirable Fino (MP2,5)**

**3.7.1.1.** **Resultados en Receptores Discretos**

En la Tabla 14 se presentan los resultados de la modelación de MP2,5 para el percentil 98 de 24 horas
y el periodo anual comparados con sus respectivas normativas primarias de calidad del aire.

Tabla 14 - Resultados Aporte Modelo en Receptores Discretos para MP2,5.

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Material Particulado Respirable Fino (MP2.5)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Porcentaje de la**<br>**Norma de Calidad**|**Porcentaje de la**<br>**Norma de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil**<br>**98 24**<br>**horas**|**Períod**<br>**o Anual**|
|R1|Receptor 1|346.995|6.316.063|0,06|0,01|50|20|0,1%|0,0%|
|R2|Receptor 2|345.810|6.315.262|0,07|0,01|0,01|0,01|0,1%|0,0%|
|R3|Receptor 3|345.264|6.313.891|0,03|0,00|0,00|0,00|0,1%|0,0%|
|R4|Estación<br>Quilicura<br>(SINCA)|339.594|6.308.625|0,00|0,00|0,00|0,00|0,0%|0,0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de MP2,5 para el
percentil 98 de 24 horas son de baja magnitud, siendo el máximo aporte de un 0,1% en el percentil 98
de 24 horas para los receptores 1, 2 y 3 ubicados cerca del proyecto. Para periodo anual, se consideran
aportes nulos en estos 3 receptores.

Por otro lado, el aporte en la Estación Quilicura (SINCA) se considera nulo ya que su valor representa
un 0% de aporte para las normas diaria y anual.

31

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**3.7.1.2.** **Curvas de Isoconcentración**

En la Figura 5 se presentan las curvas de isoconcentración para el percentil 98 de 24 horas de MP2,5:

Figura 5 - Curva de Isoconcentración MP2,5 P98 24 horas.

32

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

En la Figura 6 se presentan las curvas de isoconcentración para periodo anual de MP2,5:

Figura 6 - Curva de Isoconcentración MP2,5 Anual.

Adenda 1

Mayo 2024

33

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**3.7.2.** **Material Particulado Respirable (MP10)**

**3.7.2.1.** **Resultados en Receptores Discretos**

En la Tabla 15 se presentan los resultados de la modelación de MP10 para el percentil 98 de 24 horas
y el periodo anual comparados con sus respectivas normativas primarias de calidad del aire.

Tabla 15 - Resultados Aporte Modelo en Receptores Discretos para MP10.

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Material Particulado Respirable (MP10)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Porcentaje de la**<br>**Norma de Calidad**|**Porcentaje de la**<br>**Norma de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil**<br>**98 24**<br>**horas**|**Períod**<br>**o Anual**|
|R1|Receptor 1|346.995|6.316.063|0,26|0,03|130|50|0,2%|0,1%|
|R2|Receptor 2|345.810|6.315.262|0,33|0,03|0,03|0,03|0,3%|0,1%|
|R3|Receptor 3|345.264|6.313.891|0,16|0,02|0,02|0,02|0,1%|0,0%|
|R4|Estación<br>Quilicura<br>(SINCA)|339.594|6.308.625|0,01|0,00|0,00|0,00|0,0%|0,0%|

De la tabla anterior, se aprecia que el aporte del modelo en concentración de MP10 tanto para el
percentil 98 de 24 horas como para periodo anual es de baja magnitud, siendo el máximo aporte de
un 0,3% y 0,1% respectivamente en el Receptor 2.

Por otro lado, el aporte en la Estación Quilicura (SINCA) se considera nulo ya que su valor representa
un 0% de aporte para las normas diaria y anual.

34

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**3.7.2.2.** **Curvas de Isoconcentración**

En la Figura 7 se presentan las curvas de isoconcentración para el percentil 98 de 24 horas de MP10:

Figura 7 - Curva de Isoconcentración MP10 P98 24 horas.

35

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

En la Figura 8 se presentan las curvas de isoconcentración para periodo anual de MP10:

Figura 8 - Curva de Isoconcentración MP10 Anual.

Adenda 1

Mayo 2024

36

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**3.8.** **Verificación Significancia Aporte MP2,5 y MP10**

En consideración a la “Guía para la Evaluación Ambiental del Riesgo para la Salud a la Población”
(SEA 2, 2023) aplicable a la zona de estudio por tratarse de un área declarada saturada según el
Decreto Supremo N°10/2015 del Ministerio del Medio Ambiente que Declara Zona Saturada y Latente
a las Comunas de Concón, Quintero y Puchuncaví, de acuerdo al inciso 4 de dicha guía “Criterios para
Evaluar la Significancia del Aporte de Emisiones de Material Particulado Respirable, MP10 y MP2,5”,
en su segundo párrafo señala: “ _Cabe recordar que, independiente de la duración del impacto, los_
_valores sólo serán aplicables cuando las concentraciones obtenidas en los receptores humanos_
_analizados estén por encima, en concentración y periodo, de las establecidas en las normas primarias de_
_calidad ambiental para MP10 y MP2,5 vigentes al momento de la evaluación”_ .

Tomando en cuenta los resultados presentados en la Tabla 14 y la Tabla 15 para MP2,5 y MP10, se
demostró que en todos los receptores evaluados tanto para las normas primarias de periodo diario
y anual, los aportes del Proyecto no superan el 0,5%, por lo que no aplica la evaluación del criterio de
esta guía toda vez que los aportes están muy lejos de ser equivalentes a una condición de latencia y
más aún de superar las normas primarias de calidad del aire vigente. Lo anterior, implica que, a partir
de los resultados del estudio, se comprueba técnicamente que la ejecución del año de mayor emisión
del Proyecto no va a generar riesgos a la salud de la población.

Finalmente, se concluye en base al estudio presentado que la ejecución del Proyecto “Planta
Fotovoltaica Chieti Solar” no propenderá a generar un aumento en concentración de contaminantes
atmosféricos que pueda suponer riesgos en la salud de la población, por lo que su ejecución no va a
generar cambios relevantes en la calidad del aire de la zona una vez se ejecute el primer año, esto se
confirma tomando en cuenta el Criterio de evaluación en el SEIA “Impacto de emisiones en zonas
saturadas por material particulado respirable MP10 y material particulado fino respirable MP2,5”, al
tomar en cuenta que las mayores emisiones del proyecto se generan en la etapa de construcción, la
cual dura un máximo de seis meses, por lo que se hace uso de la Tabla 2 del criterio de evaluación,

como se muestra a continuación:

Tabla 16 - Evaluación de aportes del proyecto sobre receptores de acuerdo a Tabla 2 del Criterio de
Evaluación en el SEIA “Impacto de emisiones en zonas saturadas por material particulado respirable

MP10 y material particulado fino respirable MP2,5”

|Duración Impacto|Col2|Col3|MP 10 (μg/m3)|Col5|MP 2,5 (μg/m3)|Col7|
|---|---|---|---|---|---|---|
|Año|Mes|Proporcional|24 horas|Anual|24 horas|Anual|
|1|12|1,0|10,00|3,00|5,13|0,99|
|Aportes del Proyecto sobre Receptores|Aportes del Proyecto sobre Receptores|Aportes del Proyecto sobre Receptores|Aportes del Proyecto sobre Receptores|Aportes del Proyecto sobre Receptores|Aportes del Proyecto sobre Receptores|Aportes del Proyecto sobre Receptores|
|Receptor 1|Receptor 1|Receptor 1|0,26|0,03|0,06|0,01|
|Receptor 2|Receptor 2|Receptor 2|0,33|0,03|0,07|0,01|
|Receptor 3|Receptor 3|Receptor 3|0,16|0,02|0,03|0,00|
|Estación Quilicura (SINCA)|Estación Quilicura (SINCA)|Estación Quilicura (SINCA)|0,01|0,00|0,00|0,00|

37

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Chieti Solar”_

Adenda 1

Mayo 2024

**4.** **CONCLUSIONES**

En este documento se ha presentado la modelación de dispersión de contaminantes atmosféricos
del proyecto _“Planta Fotovoltaica Chieti Solar”_ para los contaminantes MP2,5 y MP10, considerando
la versión actualizada del Estudio de Emisiones Atmosféricas para el ICSARA 1. A partir de los
resultados presentados en este informe, se tienen las siguientes conclusiones:

 - Respecto al análisis de incertidumbre, se concluye que el modelo WRF en el dominio de

20x15km tiene la capacidad de representar la meteorología observada, en particular, se

comparó de forma cualitativa y cuantitativa los resultados del modelo meteorológico con
registros observados en la estación meteorológica Pudahuel (DMC). A partir del análisis, se

concluye que el modelo representa de manera aceptable las variables meteorológicas de

superficie velocidad del viento, dirección del viento y temperatura.

 - A partir de los resultados de la modelación de dispersión de contaminantes atmosféricos, se

concluye que para el primer año, que corresponde al año de mayor emisión del Proyecto

(fase de construcción y operación), en ninguno de los contaminantes evaluados (MP2,5, y
MP10) se superan los límites establecidos en las normativas primarias de calidad del aire,

tampoco se alcanza condición de latencia, sino más bien se alcanzan aportes en

concentración que no alcanzan a superar el 1% de las normas evaluadas en todos los

receptores evaluados. Además, se comprobó que el aporte del proyecto sobre la Estación

Quilicura (SINCA) es nulo, por lo que se espera que su ejecución no modifique la condición

base de esta.

 - Finalmente, se concluye en base al estudio presentado que la ejecución del Proyecto “Planta

Fotovoltaica Chieti Solar” no propenderá a generar un aumento en concentración de

contaminantes atmosféricos que pueda suponer riesgos en la salud de la población, por lo

que su ejecución no va a generar cambios relevantes en la calidad del aire de la zona una vez

se ejecute el primer año.

**5.** **REFERENCIAS**

SEA. (2023). _Guía para uso de Modelos de Calidad del Aire en el SEIA._ Servicio de Evaluación Ambiental.

**ANEXOS**

A continuación, a modo de respaldo se presentan los nombres de los anexos digitales incluidos con
este informe, a partir de los cuales la Autoridad podrá tener respaldo de los archivos requeridos
según la “Guía para uso de modelos de calidad del aire en el SEIA”.

 - Anexo Digital A - Archivos Digitales de Modelación ICSARA 1

38

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4: - Normas de Calidad del Aire.**

| Contaminante | Decreto<br>Aplicable | Norma | Col4 | Periodo de Evaluación de<br>Cumplimiento de Norma |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Decreto**<br>**Aplicable** | **Valor** | **Unidad** | **Unidad** |
| Material Particulado<br>Respirable Fino (MP2,5) | Decreto<br>Supremo<br>N°12/2010 | 50 | μg/m3 | Percentil 98 de las concentraciones de<br>24 horas |
| Material Particulado<br>Respirable Fino (MP2,5) | Decreto<br>Supremo<br>N°12/2010 | 20 | 20 | Concentración anual |
| Material Particulado<br>Respirable (MP10) | Decreto<br>Supremo<br>N°12/2022 | 130 | μg/m3N | Percentil 98 de las concentraciones de<br>24 horas |
| Material Particulado<br>Respirable (MP10) | Decreto<br>Supremo<br>N°12/2022 | 50 | 50 | Concentración anual |

**Tabla 5: - Estación Meteorológica Pudahuel (DMC).**

| Estación | Coordenadas UTM WGS 84 - 19S | Col3 | Periodo considerado<br>para el análisis | Variables meteorológicas de<br>superficie |
| --- | --- | --- | --- | --- |
| **Estación** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| Pudahuel<br>(DMC) | 333.699 | 6.305.342 | 01/01/22 - 31/12/22 | - Velocidad del viento (m/s)<br>- Dirección del viento (°)<br>- Temperatura (°C) |

**Tabla 7: - Series de Tiempo Observadas y Modeladas en Estación Pudahuel (DMC). Periodo 01/01/22 al 31/12/22.**

| Variable | Observado | Modelado |
| --- | --- | --- |
| Velocidad del<br>Viento |  |  |

**Tabla 8: - Ciclos Diarios Observados y Modelados en Estación Pudahuel (DMC). Periodo 01/01/22 al 31/12/22.**

| Variable | Observado | Modelado |
| --- | --- | --- |
| Velocidad del<br>Viento |  |  |

**Tabla 9: - Rosas de Viento Observadas y Modeladas en Estación Pudahuel (DMC). Periodo 01/01/22 al 31/12/22.**

| Periodo | Observado | Modelado |
| --- | --- | --- |
| Año<br>completo<br>(todos los<br>datos) |  |  |

**Tabla 10: - Ciclos Estacionales Observados y Modelados en Estación Pudahuel (DMC). Periodo 01/01/22 al 31/12/22.**

| Variable | Observado | Modelado |
| --- | --- | --- |
| Velocidad y<br>dirección del<br>viento |  |  |

**Tabla 11: - Estadísticos análisis cuantitativo. Estación Pudahuel (DMC).**

| Estadístico | Velocidad del Viento (m/s) | Col3 | Temperatura (°C) | Col5 |
| --- | --- | --- | --- | --- |
| **Estadístico** | **Serie de**<br>**Tiempo** | **Ciclo Diario** | **Serie de**<br>**Tiempo** | **Ciclo Diario** |
| Sesgo | -1,36 | -1,37 | -1,37 | -1,37 |
| Error Cuadrático Medio | 1,95 | 1,48 | 3,19 | 2,18 |
| Coeficiente de Correlación | 0,75 | 0,94 | 0,93 | 0,94 |

**Tabla 13: - Receptores Discretos.**

| ID<br>Receptor | Descripción | Coordenadas de Ubicación<br>(Datum WGS84) | Col4 |
| --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** |
| R1 | Receptor 1 | 346.995 | 6.316.063 |
| R2 | Receptor 2 | 345.810 | 6.315.262 |
| R3 | Receptor 3 | 345.264 | 6.313.891 |
| R4 | Estación Quilicura (SINCA) | 339.594 | 6.308.625 |

**Tabla 14: - Resultados Aporte Modelo en Receptores Discretos para MP2,5.**

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Material Particulado Respirable Fino (MP2.5) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Porcentaje de la**<br>**Norma de Calidad** | **Porcentaje de la**<br>**Norma de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil**<br>**98 24**<br>**horas** | **Períod**<br>**o Anual** |
| R1 | Receptor 1 | 346.995 | 6.316.063 | 0,06 | 0,01 | 50 | 20 | 0,1% | 0,0% |
| R2 | Receptor 2 | 345.810 | 6.315.262 | 0,07 | 0,01 | 0,01 | 0,01 | 0,1% | 0,0% |
| R3 | Receptor 3 | 345.264 | 6.313.891 | 0,03 | 0,00 | 0,00 | 0,00 | 0,1% | 0,0% |
| R4 | Estación<br>Quilicura<br>(SINCA) | 339.594 | 6.308.625 | 0,00 | 0,00 | 0,00 | 0,00 | 0,0% | 0,0% |

**Tabla 15: - Resultados Aporte Modelo en Receptores Discretos para MP10.**

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Material Particulado Respirable (MP10) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Porcentaje de la**<br>**Norma de Calidad** | **Porcentaje de la**<br>**Norma de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil**<br>**98 24**<br>**horas** | **Períod**<br>**o Anual** |
| R1 | Receptor 1 | 346.995 | 6.316.063 | 0,26 | 0,03 | 130 | 50 | 0,2% | 0,1% |
| R2 | Receptor 2 | 345.810 | 6.315.262 | 0,33 | 0,03 | 0,03 | 0,03 | 0,3% | 0,1% |
| R3 | Receptor 3 | 345.264 | 6.313.891 | 0,16 | 0,02 | 0,02 | 0,02 | 0,1% | 0,0% |
| R4 | Estación<br>Quilicura<br>(SINCA) | 339.594 | 6.308.625 | 0,01 | 0,00 | 0,00 | 0,00 | 0,0% | 0,0% |

**Tabla 16: - Evaluación de aportes del proyecto sobre receptores de acuerdo a Tabla 2 del Criterio de**

| Duración Impacto | Col2 | Col3 | MP 10 (μg/m3) | Col5 | MP 2,5 (μg/m3) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Año | Mes | Proporcional | 24 horas | Anual | 24 horas | Anual |
| 1 | 12 | 1,0 | 10,00 | 3,00 | 5,13 | 0,99 |
| Aportes del Proyecto sobre Receptores | Aportes del Proyecto sobre Receptores | Aportes del Proyecto sobre Receptores | Aportes del Proyecto sobre Receptores | Aportes del Proyecto sobre Receptores | Aportes del Proyecto sobre Receptores | Aportes del Proyecto sobre Receptores |
| Receptor 1 | Receptor 1 | Receptor 1 | 0,26 | 0,03 | 0,06 | 0,01 |
| Receptor 2 | Receptor 2 | Receptor 2 | 0,33 | 0,03 | 0,07 | 0,01 |
| Receptor 3 | Receptor 3 | Receptor 3 | 0,16 | 0,02 | 0,03 | 0,00 |
| Estación Quilicura (SINCA) | Estación Quilicura (SINCA) | Estación Quilicura (SINCA) | 0,01 | 0,00 | 0,00 | 0,00 |
