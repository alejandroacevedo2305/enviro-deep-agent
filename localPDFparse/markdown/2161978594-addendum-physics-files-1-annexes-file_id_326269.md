---
title: Sin título
author: Nico Rebolledo
date: D:20240809120659-04'00'
language: es
type: report
pages: 50
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ADENDA EN RESPUESTA AL INFORME CONSOLIDADO DE SOLICITUD DE ACLARACIONES, RECTIFICACIONES Y/O AMPLIACIONES A LA DECLARACIÓN DE IMPACTO AMBIENTAL PROYECTO PLANTA FOTOVOLTAICA VERNAZZA QUINTERO - PUCHUNCAVI ANEXO A-5.1-C MODELACIÓN DE DISPERSIÓN DE CONTAMINANTES
  - Modelación de Dispersión de Contaminantes Declaración de Impacto Ambiental ICSARA 1 _“Planta Fotovoltaica Vernazza”_
-->

# ADENDA EN RESPUESTA AL INFORME CONSOLIDADO DE SOLICITUD DE ACLARACIONES, RECTIFICACIONES Y/O AMPLIACIONES A LA DECLARACIÓN DE IMPACTO AMBIENTAL PROYECTO PLANTA FOTOVOLTAICA VERNAZZA QUINTERO - PUCHUNCAVI ANEXO A-5.1-C MODELACIÓN DE DISPERSIÓN DE CONTAMINANTES

## Agosto 2024

# Modelación de Dispersión de Contaminantes Declaración de Impacto Ambiental ICSARA 1 _“Planta Fotovoltaica Vernazza”_

### Julio 2024

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

**ÍNDICE**

ICSARA 1

Julio 2024

Índice de Tablas .......................................................................................................................................................... 4

Índice de Figuras ......................................................................................................................................................... 5

1. Introducción ...................................................................................................................................................... 6

2. Antecedentes Generales del Proyecto ............................................................................................................. 8

2.1. Descripción ............................................................................................................................................... 8

2.2. Localización .............................................................................................................................................. 8

2.3. Cronograma general ................................................................................................................................ 8

2.3.1. Fase de construcción .......................................................................................................................... 9

2.3.2. Fase de operación ............................................................................................................................... 9

2.3.3. Fase de cierre ...................................................................................................................................... 9

3. Modelación de Dispersión de Contaminantes ............................................................................................... 10

3.1. Descripción de los Modelos Utilizados. ................................................................................................ 10

3.1.1. WRF ................................................................................................................................................... 10

3.1.2. CALPUFF ............................................................................................................................................ 10

3.2. Normas de Calidad del Aire .................................................................................................................... 11

3.3. Dominio de Modelación ......................................................................................................................... 12

3.4. Análisis de Incertidumbre ...................................................................................................................... 14

3.4.1. Análisis Cualitativo ............................................................................................................................ 16

3.4.1.1. Series de Tiempo ..................................................................................................................................... 17

3.4.1.2. Ciclos Diarios .......................................................................................................................................... 19

3.4.1.3. Rosas de Viento ...................................................................................................................................... 21

3.4.1.1. Ciclo Estacional ...................................................................................................................................... 25

3.4.2. Análisis Cuantitativo.......................................................................................................................... 26

3.5. Escenario de Modelación ...................................................................................................................... 28

3.6. Receptores Discretos ............................................................................................................................ 32

3.7. Resultados.............................................................................................................................................. 34

3.7.1. Material Particulado Respirable Fino (MP2,5) ................................................................................. 34

3.7.1.1. Resultados en Receptores Discretos .................................................................................................... 34

3.7.1.2. Curvas de Isoconcentración .................................................................................................................. 35

3.7.2. Material Particulado Respirable (MP10) .......................................................................................... 37

3.7.2.1. Resultados en Receptores Discretos .................................................................................................... 37

3.7.2.2. Curvas de Isoconcentración .................................................................................................................. 38

3.7.3. Material Particulado Sedimentable (MPS) ....................................................................................... 40

3.7.3.1. Resultados en Receptores Discretos .................................................................................................... 40

3.7.3.2. Curvas de Isodepositación..................................................................................................................... 41

3.7.4. Cobre (Cu) ......................................................................................................................................... 42

3.7.4.1. Resultados en Receptores Discretos .................................................................................................... 42

3.7.5. Zinc (Zn) ............................................................................................................................................. 42

3.7.5.1. Resultados en Receptores Discretos .................................................................................................... 42

3

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

3.7.6. Manganeso (Mn)............................................................................................................................... 43

3.7.6.1. Resultados en Receptores Discretos .................................................................................................... 43

3.7.7. Hierro (Fe) ......................................................................................................................................... 43

3.7.7.1. Resultados en Receptores Discretos .................................................................................................... 43

3.7.8. Molibdeno (Mo) ................................................................................................................................ 44

3.7.8.1. Resultados en Receptores Discretos .................................................................................................... 44

3.7.9. Cadmio (Cd) ....................................................................................................................................... 44

3.7.9.1. Resultados en Receptores Discretos .................................................................................................... 44

3.7.10. Mercurio (Hg) ............................................................................................................................... 45

3.7.10.1. Resultados en Receptores Discretos .................................................................................................... 45

3.7.11. Níquel (Ni) ......................................................................................................................................... 45

3.7.11.1. Resultados en Receptores Discretos .................................................................................................... 45

3.7.12. Plomo (Pb) .................................................................................................................................... 46

3.7.12.1. Resultados en Receptores Discretos .................................................................................................... 46

3.7.13. Vanadio (V) ................................................................................................................................... 46

3.7.13.1. Resultados en Receptores Discretos .................................................................................................... 46

3.7.14. Selenio (Se)................................................................................................................................... 47

3.7.14.1. Resultados en Receptores Discretos .................................................................................................... 47

3.7.15. Arsénico (As) ................................................................................................................................ 47

3.7.15.1. Resultados en Receptores Discretos .................................................................................................... 47

3.7.16. Antimonio (Sb) ............................................................................................................................. 48

3.7.16.1. Resultados en Receptores Discretos .................................................................................................... 48

3.8. Verificación Significancia Aporte Proyecto ........................................................................................... 48

4. Conclusiones .................................................................................................................................................... 49

5. Referencias ...................................................................................................................................................... 50

6. Anexos ............................................................................................................................................................. 50

**Índice de Tablas**

Tabla 1 - Cronograma Fase de Construcción. ........................................................................................... 9
Tabla 2 - Cronograma Fase de Operación. ............................................................................................... 9
Tabla 3 - Cronograma Fase de Cierre. ...................................................................................................... 9
Tabla 4 - Normas Primarias de Calidad del Aire. ..................................................................................... 11
Tabla 5 - Normas Secundarias de Calidad del Aire. ................................................................................. 12
Tabla 6 - Estación Meteorológica Valle Alegre (SINCA). ....................................................................... 16
Tabla 7 - Resumen Datos Observados y Modelados en Estación Valle Alegre (SINCA) (SINCA). Periodo
01/01/23 al 31/12/23. ................................................................................................................................... 16
Tabla 8 - Series de Tiempo Observadas y Modeladas en Estación Valle Alegre (SINCA). Periodo
01/01/23 al 31/12/23. .................................................................................................................................... 17
Tabla 9 - Ciclos Diarios Observados y Modelados en Estación Valle Alegre (SINCA). Periodo 01/01/23
al 31/12/23. ................................................................................................................................................. 19
Tabla 10 - Rosas de Viento Observadas y Modeladas en Estación Valle Alegre (SINCA). Periodo
01/01/23 al 31/12/23. .................................................................................................................................... 21
Tabla 11 - Ciclos Estacionales Observados y Modelados en Estación Valle Alegre (SINCA). Periodo
01/01/23 al 31/12/23. ................................................................................................................................... 25

4

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

Tabla 12 - Estadísticos análisis cuantitativo. Estación Valle Alegre (SINCA). ........................................ 27
Tabla 13 - Fuentes de Emisión MP2.5, MP10 y MPS. .............................................................................. 29
Tabla 14 - Fuentes de Emisión Metales Pesados.................................................................................... 30
Tabla 15 - Receptores Discretos. ............................................................................................................ 32
Tabla 16 - Resultados Aporte Modelo en Receptores Discretos para MP2,5. ...................................... 34
Tabla 17 - Resultados Aporte Modelo en Receptores Discretos para MP10. ....................................... 37
Tabla 18 - Resultados Aporte Modelo en Receptores Discretos para MPS. ........................................ 40
Tabla 19 - Resultados Aporte Modelo en Receptores Discretos para Cu. ............................................ 42
Tabla 20 - Resultados Aporte Modelo en Receptores Discretos para Zn. ........................................... 42
Tabla 21 - Resultados Aporte Modelo en Receptores Discretos para Mn. ........................................... 43
Tabla 22 - Resultados Aporte Modelo en Receptores Discretos para Fe. ............................................ 43
Tabla 23 - Resultados Aporte Modelo en Receptores Discretos para Mo. .......................................... 44
Tabla 24 - Resultados Aporte Modelo en Receptores Discretos para Cd. ........................................... 44
Tabla 25 - Resultados Aporte Modelo en Receptores Discretos para Hg. ........................................... 45
Tabla 26 - Resultados Aporte Modelo en Receptores Discretos para Ni. ............................................ 45
Tabla 27 - Resultados Aporte Modelo en Receptores Discretos para Pb............................................. 46
Tabla 28 - Resultados Aporte Modelo en Receptores Discretos para V. ............................................. 46
Tabla 29 - Resultados Aporte Modelo en Receptores Discretos para Se. ............................................ 47
Tabla 30 - Resultados Aporte Modelo en Receptores Discretos para As. ........................................... 47
Tabla 31 - Resultados Aporte Modelo en Receptores Discretos para Sb. ............................................ 48

**Índice de Figuras**

Figura 1 - Dominio de Modelación. ..........................................................................................................13
Figura 2 - Estación Meteorológica Valle Alegre (SINCA). .......................................................................15
Figura 3 - Fuentes de Emisión. .................................................................................................................31
Figura 4 - Receptores Discretos. ............................................................................................................ 33
Figura 5 - Curva de Isoconcentración MP2,5 P98 24 horas. .................................................................. 35
Figura 6 - Curva de Isoconcentración MP2,5 Anual. .............................................................................. 36
Figura 7 - Curva de Isoconcentración MP10 P98 24 horas. ................................................................... 38
Figura 8 - Curva de Isoconcentración MP10 Anual. ............................................................................... 39
Figura 9 - Curva de Isodepositación MPS Anual. ................................................................................... 41

5

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**1.** **Introducción**

En este informe se presenta la modelación de dispersión de contaminantes atmosféricos para el año
de mayor emisión asociado a la Declaración de Impacto Ambiental (DIA) del Proyecto “ _Planta_
_Fotovoltaica Vernazza_ ”, ubicado en la comuna de Quintero, Región de Valparaíso. A continuación, se

describe el contenido del documento:

En primer lugar, se presentan los antecedentes generales del Proyecto; descripción, localización y
cronograma. Posteriormente, se presenta el desarrollo de la modelación de dispersión de
contaminantes atmosféricos, elaborada utilizando para ello el modelo refinado de calidad del aire
WRF-CALPUFF, en un dominio de modelación de 20x20 kilómetros, para el cual se definió una grilla
de receptores con resolución de 1x1 kilómetros. De manera adicional, se presenta la estimación del
aporte del proyecto en 14 receptores discretos, 6 que corresponden a viviendas identificadas en el
Estudio de Ruido, 1 que corresponde a una estación de calidad del aire (sobre los cuales se verifica el
cumplimiento de normativa primaria de calidad del aire) y 7 que corresponden a recursos naturales
identificados en el estudio de Caracterización de Flora y Vegetación (sobre los cuales se verifica el
cumplimiento de normativa secundaria de calidad del aire).

Con el fin de validar la información meteorológica modelada elaborada a partir del modelo WRF
( _Weather Research and Forecasting_ ), la cual se utiliza como información de entrada para el modelo de
calidad del aire CALPUFF, se presenta un análisis de incertidumbre, en el cual se compara de manera
cualitativa y cuantitativa la capacidad del modelo de representar variables meteorológicas de
superficie registradas en una estación meteorológica cercana al proyecto.

A partir de los resultados de la modelación, se presentan tablas con el aporte en concentración y
depositación (según corresponda) de los diferentes contaminantes atmosféricos generados a
consecuencia de la ejecución del año de mayor emisión del Proyecto en cada receptor discreto, y se
las compara con las normativas de calidad del aire primarias y secundarias aplicables. Adicionalmente,
se presentan las curvas de isoconcentración e isodepositación para cada contaminante según
corresponda.

La siguiente tabla muestra los contaminantes considerados en este estudio de modelación, que
corresponden a material particulado en sus diferentes fracciones* (3) y además se considera la
modelación de metales pesados** (12), cuyas tasas de emisión fueron calculadas a partir de muestras
de suelo que se hicieron en la zona de emplazamiento del proyecto:

-Níquel (Ni)**

-Plomo (Pb)**

-Vanadio (V)**

-Selenio (Se)**

-Arsénico (As)**

-Antimonio (Sb)**

-Material Particulado Respirable
Fino (MP2.5)*

-Material Particulado Respirable
(MP10)*

-Material Particulado

Sedimentable (MPS)*

-Cobre (Cu)**

-Zinc (Zn)**

-Hierro (Fe)**

-Molibdeno (Mo)**

-Cadmio (Cd)**

-Mercurio (Hg)**

Cabe mencionar, que en este estudio se considerado un escenario asociado a la evaluación de la
potencial ejecución de la construcción del proyecto al mismo tiempo de otros dos proyectos cercanos
actualmente en evaluación, con el objetivo de evaluar el escenario más conservador y así tener una
estimación del aporte sinérgico de los 3 proyectos sobre todos los receptores identificados.

6

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

Luego, se presenta la verificación de significancia de aporte en concentración, con el fin de evaluar el
riesgo prexistente, considerando que la zona de estudio fue declarada saturada según el Decreto
Supremo N°10/2015 del Ministerio del Medio Ambiente.

Por último, se presentan las principales conclusiones del estudio.

Finalmente, es importante mencionar que este estudio fue realizado siguiendo los lineamientos de la
“Guía para el Uso de Modelos de Calidad del Aire en el SEIA” (SEA, 2023) y de la “Guía para la
Evaluación Ambiental del Riesgo para la Salud de la Población” (SEA 2, 2023).

7

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**2.** **Antecedentes Generales del Proyecto**

**2.1.** **Descripción**
El Proyecto sometido a evaluación ambiental, consiste en la construcción y operación de una central
solar fotovoltaica para la producción de 152,97 MWp de energía (potencia nominal instalada), y que
proveerá aproximadamente 90 MW (potencia neta) a la Subestación Puchuncaví para su
aprovechamiento por el Sistema Eléctrico Nacional (SEN). Adicionalmente el Proyecto contará con
un sistema de almacenamiento de energía mediante baterías de iones de litio del tipo BESS (Battery
Energy System Storage), lo que permitirá inyectar parte de la energía producida durante el día en
horarios de mayor demanda eléctrica, que normalmente corresponden a periodos nocturnos. Es
posible también que los sistemas BESS presten otros tipos de servicio a la red, como control de
tensión y frecuencia, recuperación de servicio, entre otros.

El Proyecto para la producción de energía utilizará 216.972 paneles fotovoltaicos de 705 Wp de
potencia nominal (216.972 x 705 Wp = 152,97 MWp), los cuales estarán montados sobre estructuras
con seguimiento solar con eje este-oeste, agrupados en un total de 7.749 string (cantidad de paneles
fotovoltaicos conectados en paralelo) de 1x28 y 2x28 módulos, lo que en conjunto corresponde a la
potencia nominal.

Finalmente, la energía producida, convertida y transformada, será conducida por medio una línea de
alta tensión aérea (línea de evacuación) de 110 kV y aproximadamente 2,75 kilómetros de longitud,
hasta conectar con la subestación Puchuncaví.

Además de los paneles fotovoltaicos, la subestación elevadora y sus elementos de conexión, el
presente Proyecto requerirá de un cerco perimetral, un portón de acceso, equipos de videovigilancia
y sistema de vigilancia SCADA (Supervisor y Control And Data Acquisition).

**2.2.** **Localización**

El Proyecto se emplazará en un área rural, al interior de una parte de los predios ubicados en la
Reserva del Fundo Valle Alegre que se compone de los siguientes potreros y parcelas: El Peumo Uno,
El Peumo Dos, Santa Teresa, El Centro, El Ruz, El Molino, Lagunillas y parte de Los Arriendos excluidos
los Lotes 3, 6, 7, 8 y 10 expropiados por el Fisco de Chile, en la comuna de Quintero, región de
Valparaíso, un una superficie total de 145,83 hectáreas. Al proyecto se accede por un camino
derivado de la Ruta F-190. El Proyecto se emplazará en un área rural, de acuerdo con lo establecido
en el Plan Regulador Comunal (PRC) de Quintero y la línea de alta tensión atraviesa un área rural de
la comuna de Puchuncaví, de acuerdo también con su PRC.

**2.3.** **Cronograma general**
La construcción se realizará en un plazo estimado máximo de doce (12) meses, mientras que la
operación del Proyecto estará programada para treinta (30) años bajo la modalidad de operación y
vigilancia remota y en tiempo real, no contemplándose la presencia de trabajadores en las
instalaciones, salvo para las labores de mantención.

8

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**2.3.1.** **Fase de construcción**

Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de construcción,
se establece el cronograma presentado en la Tabla 1:

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **2.3.1.** **Fase de construcción** Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de construcción, se establece el cronograma presentado en la Tabla 1: -->

**Tabla 1: - Cronograma Fase de Construcción.**

| Actividad | Mes<br>1 | Mes<br>2 | Mes<br>3 | Mes<br>4 | Mes<br>5 | Mes<br>6 | Mes<br>7 | Mes<br>8 | Mes<br>9 | Mes<br>10 | Mes<br>11 | Mes<br>12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Habilitación instalaciones de faena |  |  |  |  |  |  |  |  |  |  |  |  |
| Montaje instalación de faenas |  |  |  |  |  |  |  |  |  |  |  |  |
| Cierre perimetral y señalización |  |  |  |  |  |  |  |  |  |  |  |  |
| Corta o despeje de vegetación en el<br>área del Proyecto |  |  |  |  |  |  |  |  |  |  |  |  |
| Habilitación de caminos |  |  |  |  |  |  |  |  |  |  |  |  |
| Atravieso vehicular |  |  |  |  |  |  |  |  |  |  |  |  |
| Preparación del terreno |  |  |  |  |  |  |  |  |  |  |  |  |
| Obras Civiles |  |  |  |  |  |  |  |  |  |  |  |  |
| Montaje de equipos y cabinas |  |  |  |  |  |  |  |  |  |  |  |  |
| Hincado de las estructuras de<br>soporte y excavaciones de<br>cableado |  |  |  |  |  |  |  |  |  |  |  |  |
| Montaje de la línea de evacuación<br>de alta tensión |  |  |  |  |  |  |  |  |  |  |  |  |
| Montaje de estructuras de soporte<br>e instalación de paneles<br>fotovoltaicos |  |  |  |  |  |  |  |  |  |  |  |  |
| Construcción de Subestación<br>Elevadora |  |  |  |  |  |  |  |  |  |  |  |  |
| Retiro de las instalaciones de faena |  |  |  |  |  |  |  |  |  |  |  |  |

<!-- Estadísticas: 14 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- **2.3.2.** **Fase de operación** Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de operación, se establece el cronograma presentado en la Tabla 2: -->
<!-- FIN TABLA 1 -->


Tabla 1 - Cronograma Fase de Construcción.

|Actividad|Mes<br>1|Mes<br>2|Mes<br>3|Mes<br>4|Mes<br>5|Mes<br>6|Mes<br>7|Mes<br>8|Mes<br>9|Mes<br>10|Mes<br>11|Mes<br>12|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Habilitación instalaciones de faena|||||||||||||
|Montaje instalación de faenas|||||||||||||
|Cierre perimetral y señalización|||||||||||||
|Corta o despeje de vegetación en el<br>área del Proyecto|||||||||||||
|Habilitación de caminos|||||||||||||
|Atravieso vehicular|||||||||||||
|Preparación del terreno|||||||||||||
|Obras Civiles|||||||||||||
|Montaje de equipos y cabinas|||||||||||||
|Hincado de las estructuras de<br>soporte y excavaciones de<br>cableado|||||||||||||
|Montaje de la línea de evacuación<br>de alta tensión|||||||||||||
|Montaje de estructuras de soporte<br>e instalación de paneles<br>fotovoltaicos|||||||||||||
|Construcción de Subestación<br>Elevadora|||||||||||||
|Retiro de las instalaciones de faena|||||||||||||

**2.3.2.** **Fase de operación**

Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de operación,
se establece el cronograma presentado en la Tabla 2:

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **2.3.2.** **Fase de operación** Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de operación, se establece el cronograma presentado en la Tabla 2: -->

**Tabla 2: - Cronograma Fase de Operación.**

| Actividades | Años | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividades** | **1 ** | **2 ** | **3 ** | **... ** | **10** | **20** | **... ** | **30** |
| Prueba y puesta en servicio |  |  |  |  |  |  |  |  |
| Operación planta |  |  |  |  |  |  |  |  |
| Actividades de mantención |  |  |  |  |  |  |  |  |
| Instalación módulos de<br>almacenamiento de baterías |  |  |  |  |  |  |  |  |
| Des energización de la planta |  |  |  |  |  |  |  |  |

<!-- Estadísticas: 6 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **2.3.3.** **Fase de cierre** Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de cierre, se establece el cronograma presentado en la Tabla 3: -->
<!-- FIN TABLA 2 -->


Tabla 2 - Cronograma Fase de Operación.

|Actividades|Años|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Actividades**|**1 **|**2 **|**3 **|**... **|**10**|**20**|**... **|**30**|
|Prueba y puesta en servicio|||||||||
|Operación planta|||||||||
|Actividades de mantención|||||||||
|Instalación módulos de<br>almacenamiento de baterías|||||||||
|Des energización de la planta|||||||||

**2.3.3.** **Fase de cierre**

Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de cierre, se
establece el cronograma presentado en la Tabla 3:

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **2.3.3.** **Fase de cierre** Sobre la base de las principales partes, obras y acciones presupuestadas para la fase de cierre, se establece el cronograma presentado en la Tabla 3: -->

**Tabla 3: - Cronograma Fase de Cierre.**

| Actividad | Mes 1 | Mes 2 | Mes 3 | Mes 4 | Mes 5 | Mes 6 | Mes 7 | Mes 8 | Mes 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Habilitación e implementación de<br>la instalación de faena |  |  |  |  |  |  |  |  |  |
| Actividades de desmantelamiento |  |  |  |  |  |  |  |  |  |
| Desmontaje LAT |  |  |  |  |  |  |  |  |  |
| Actividades de descompactación |  |  |  |  |  |  |  |  |  |

<!-- Estadísticas: 4 filas, 10 columnas -->
<!-- Contexto posterior: -->
<!-- 9 Modelación de Dispersión de Contaminantes -->
<!-- FIN TABLA 3 -->


Tabla 3 - Cronograma Fase de Cierre.

|Actividad|Mes 1|Mes 2|Mes 3|Mes 4|Mes 5|Mes 6|Mes 7|Mes 8|Mes 9|
|---|---|---|---|---|---|---|---|---|---|
|Habilitación e implementación de<br>la instalación de faena||||||||||
|Actividades de desmantelamiento||||||||||
|Desmontaje LAT||||||||||
|Actividades de descompactación||||||||||

9

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.** **Modelación de Dispersión de Contaminantes**

**3.1.** **Descripción de los Modelos Utilizados.**

**3.1.1.** **WRF**

El modelo WRF (por sus siglas en inglés _Weather Research and Forecasting Model_ ), es uno de los
modelos meteorológicos de pronóstico más avanzados y completos, operado y mantenido por el
_National Center for Atmospheric Research y el National Oceanic and Atmospheric Administration_
(NCAR/NOAA) de los Estados Unidos, es utilizado a nivel global y se encuentra en continuo
desarrollo.

De acuerdo con el inciso 4.3.1 de la “Guía para el uso de modelos de calidad del aire en el SEIA” (SEA,
2023), el modelo numérico recomendado para la generación de datos meteorológicos es WRF, el
cual fue utilizado para generar la grilla de datos meteorológicos para un año completo (2023), la cual
se utiliza como dato de entrada para la modelación de dispersión de contaminantes.

Por otro lado, el inciso 4.5 de la misma guía indica que los modelos deben ser configurados para cada
aplicación, considerando periodo y dominio geográfico de simulación, resolución espacial horizontal
y vertical, parametrizaciones físicas, entre otros. Para verificar todo lo anterior, se adjunta con este
documento el “ _**Anexo Digital A - Archivos Digitales de Modelación**_ ”, donde se entrega el respaldo de
los archivos utilizados para este estudio.

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

10

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.2.** **Normas de Calidad del Aire**

A continuación, en la Tabla 4 se presenta la normativa primaria de calidad del aire vigente a utilizar
para comparar los resultados de la modelación y de esta forma verificar cumplimiento normativo
sobre la salud de la población. Cabe mencionar, que durante la revisión bibliográfica se encontró
normativa nacional únicamente para MP2,5, MP10 y Plomo (Pb), para el resto de los metales pesados
evaluados en este estudio, se determinó usar a modo de referencia las normas de calidad del aire
ambiente de Ontario Canadá, las normas de calidad del aire para la unión Europea y también el Real
Decreto 102/2011, de 28 de enero, relativo a la mejora de la calidad del aire (España).

Tabla 4 - Normas Primarias de Calidad del Aire.

|Contaminante|Decreto Aplicable|Norma|Col4|Periodo de Evaluación de Cumplimiento<br>de Norma|
|---|---|---|---|---|
|**Contaminante**|**Decreto Aplicable**|**Valor**|**Unidad**|**Unidad**|
|Material Particulado<br>Respirable Fino<br>(MP2,5)|Decreto Supremo N°12/2010 del Ministerio del<br>Medio Ambiente1|50|μg/m3|Percentil 98 de las concentraciones de<br>24 horas|
|Material Particulado<br>Respirable Fino<br>(MP2,5)|Decreto Supremo N°12/2010 del Ministerio del<br>Medio Ambiente1|20|20|Promedio anual|
|Material Particulado<br>Respirable (MP10)|Decreto Supremo N°12/2022 del Ministerio del<br>Medio Ambiente2|130|μg/m3N|Percentil 98 de las concentraciones de<br>24 horas|
|Material Particulado<br>Respirable (MP10)|Decreto Supremo N°12/2022 del Ministerio del<br>Medio Ambiente2|50|50|Promedio anual|
|Cobre (Cu)|Ambient Air Quality Criteria - Ontario, Canada3|50|μg/m3|Concentración 24 horas|
|Zinc (Zn)|Ambient Air Quality Criteria - Ontario, Canada|120|μg/m3|Concentración 24 horas|
|Manganeso (Mn)|Ambient Air Quality Criteria - Ontario, Canada|0,2|μg/m3|Concentración 24 horas|
|Manganeso (Mn)|Air Quality Guidelines for Europe Second Edition<br>(OMS)4|0,15|μg/m3|Promedio anual|
|Hierro (Fe)|Ambient Air Quality Criteria - Ontario, Canada|4|μg/m3|Concentración 24 horas|
|Molibdeno (Mo)|Ambient Air Quality Criteria - Ontario, Canada|120|μg/m3|Concentración 24 horas|
|Cadmio (Cd)|Ambient Air Quality Criteria - Ontario, Canada|0,025|μg/m3|Concentración 24 horas|
|Cadmio (Cd)|Real Decreto 102/2011, de 28 de enero, relativo a<br>la mejora de la calidad del aire (España)5|0,005|μg/m3|Promedio anual|
|Mercurio (Hg)|Ambient Air Quality Criteria - Ontario, Canada|4|μg/m3|Concentración 24 horas|
|Mercurio (Hg)|Air Quality Guidelines for Europe Second Edition<br>(OMS)|1|μg/m3|Concentración 24 horas|
|Níquel (Ni)|Ambient Air Quality Criteria - Ontario, Canada|0,1|μg/m3|Concentración 24 horas|
|Níquel (Ni)|Real Decreto 102/2011, de 28 de enero, relativo a<br>la mejora de la calidad del aire (España)|0,02|μg/m3|Promedio anual|
|Plomo (Pb)|Ambient Air Quality Criteria - Ontario, Canada|4|μg/m3|Concentración 24 horas|
|Plomo (Pb)|Decreto Supremo N° 136/2000 del Ministerio<br>Secretaría General de la Presidencia6|0,5|μg/m3|Promedio anual|
|Vanadio (V)|Ambient Air Quality Criteria - Ontario, Canada|2|μg/m3|Concentración 24 horas|
|Selenio (Se)|Ambient Air Quality Criteria - Ontario, Canada|10|μg/m3|Concentración 24 horas|
|Arsénico (As)|Ambient Air Quality Criteria - Ontario, Canada|0,3|μg/m3|Concentración 24 horas|
|Arsénico (As)|Real Decreto 102/2011, de 28 de enero, relativo a<br>la mejora de la calidad del aire (España)|0,006|μg/m3|Promedio anual|
|Antimonio (Sb)|Ambient Air Quality Criteria - Ontario, Canada|25|μg/m3|Concentración 24 horas|

1 [Enlace web: https://www.bcn.cl/leychile/navegar?idNorma=1025202](https://www.bcn.cl/leychile/navegar?idNorma=1025202)
2 [Enlace web: https://www.bcn.cl/leychile/navegar?idNorma=1176988](https://www.bcn.cl/leychile/navegar?idNorma=1176988)
3 [Enlace web: https://www.airqualityontario.com/downloads/AmbientAirQualityCriteria.pdf](https://www.airqualityontario.com/downloads/AmbientAirQualityCriteria.pdf)
4 [Enlace web: https://www.who.int/publications/i/item/9789289013581](https://www.who.int/publications/i/item/9789289013581)
5 [Enlace web: https://www.boe.es/buscar/act.php?id=BOE-A-2011-1645](https://www.boe.es/buscar/act.php?id=BOE-A-2011-1645)
6 [Enlace web: https://www.bcn.cl/leychile/navegar?idNorma=179878](https://www.bcn.cl/leychile/navegar?idNorma=179878)

11

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

Por su parte, con el fin de verificar cumplimiento normativo sobre la conservación del medio
ambiente y la preservación de la naturaleza, ante la ausencia de una normativa secundaria que
aplique específicamente a la Región de Valparaíso, a modo referencial en la Tabla 5 se presentan las
normas secundarias a tomar en cuenta para Material Particulado Sedimentable (MPS), para de esta
forma considerar perspectivas internacionales:

Tabla 5 - Normas Secundarias de Calidad del Aire.

|Contaminante|Decreto Aplicable|Norma|Col4|Periodo de Evaluación de<br>Cumplimiento de Norma|
|---|---|---|---|---|
|**Contaminante**|**Decreto Aplicable**|**Valor**|**Unidad**|**Unidad**|
|Material Particulado Sedimentable<br>(MPS)|Norma Argentina|333|mg/m2/día|Promedio mensual|
|Material Particulado Sedimentable<br>(MPS)|Norma Confederación Suiza|200|mg/m2/día|Promedio anual|

**3.3.** **Dominio de Modelación**

En la Figura 1 se presenta el dominio de modelación, que corresponde a un área de 20x20 km con 400

celdas de 1x1 km. El dominio cubre las principales fuentes de emisión del Proyecto, los 6 receptores

de interés identificados en el Estudio de Ruido, además de la ubicación de una estación EMPR y a la

vez meteorológica con datos de suficiente disponibilidad y calidad para elaborar el análisis de

incertidumbre y los receptores identificados en el estudio de Caracterización de Flora y Vegetación.

12

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

Figura 1 - Dominio de Modelación.

ICSARA 1

Julio 2024

13

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

**3.4.** **Análisis de Incertidumbre**

ICSARA 1

Julio 2024

En base al inciso 6 de la “Guía para el uso de modelos de calidad del aire en el SEIA” (SEA, 2023), todos
los modelos tienen asociados errores e incertidumbres, por lo que es de gran importancia evaluar
dichos errores comparando los resultados del modelo con las observaciones en forma cualitativa y

cuantitativa.

Con el fin de validar la capacidad del modelo WRF de representar la meteorología local, se presenta
en este inciso el análisis de incertidumbre meteorológico. Para desarrollar el análisis, se ha
determinado utilizar una estación meteorológica dentro del dominio de modelación con información
cuya calidad y disponibilidad se ajustan para un análisis de este tipo. La estación utilizada para el
análisis corresponde a la Estación Valle Alegre (SINCA) ubicada en la comuna de Quintero, propiedad
de Codelco División Ventanas- AESGENER.S.A y operada por SGS Chile Ltda., cuyos datos son de
acceso público a través de su sitio web [7] .Los datos modelados se extraen a partir de los resultados del
modelo WRF para el mismo punto donde está ubicada la estación.

Cabe mencionar que, ante la indisponibilidad de datos públicos de meteorología de altura observados
dentro del dominio de modelación, se presenta el análisis de incertidumbre con enfoque en la
comparación de variables meteorológicas de superficie.

7 [https://sinca.mma.gob.cl/index.php/estacion/index/id/203](https://sinca.mma.gob.cl/index.php/estacion/index/id/203)

14

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

En la Figura 2 se presenta un mapa con la ubicación de la estación meteorológica respecto a la
ubicación del Proyecto:

Figura 2 - Estación Meteorológica Valle Alegre (SINCA).

15

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

A continuación, en la Tabla 6 se presentan las coordenadas de ubicación de la estación, el periodo de
monitoreo considerado para el estudio y las variables meteorológicas disponibles para analizar.
Luego, en la Tabla 7 se presenta un resumen con datos de interés para las variables analizadas.

Tabla 6 - Estación Meteorológica Valle Alegre (SINCA).

|Estación|Coordenadas UTM WGS 84 - 19S|Col3|Periodo considerado<br>para el análisis|Variables meteorológicas de<br>superficie|
|---|---|---|---|---|
|**Estación**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Valle<br>Alegre<br>(SINCA)|271.889|6.367.413|01/01/23 - 31/12/23|- Velocidad del viento (m/s)<br>- Dirección del viento (°)|

Tabla 7 - Resumen Datos Observados y Modelados en Estación Valle Alegre (SINCA) (SINCA).

Periodo 01/01/23 al 31/12/23.

|Variable|Parámetro|Observado|Modelado|
|---|---|---|---|
|Velocidad del Viento|N° Datos Disponibles|8.760|8.760|
|Velocidad del Viento|N° Datos Válidos|8.754|8.760|
|Velocidad del Viento|Porcentaje de Datos Válidos|100%|100%|
|Velocidad del Viento|Promedio (m/s)|0,7|1,9|
|Velocidad del Viento|Máximo (m/s)|5,0|9,1|
|Velocidad del Viento|Mínimo (m/s)|0,0|0,0|
|Velocidad del Viento|Porcentaje de Calmas|55%|15%|
|Dirección del Viento|N° Datos Disponibles|8.760|8.760|
|Dirección del Viento|N° Datos Válidos|8.754|8.760|
|Dirección del Viento|Porcentaje de Datos Válidos|100%|100%|

**3.4.1.** **Análisis Cualitativo**

A continuación, se presenta el análisis de incertidumbre cualitativo, cuyo objetivo corresponde a
comparar las series de tiempo, ciclos diarios, rosas de viento y ciclos estacionales observados y
modelados para las variables meteorológicas de superficie de interés disponibles; velocidad del
viento y dirección del viento.

16

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.4.1.1.** **Series de Tiempo**

A modo de verificación de la completitud del set de datos utilizados en el análisis de incertidumbre, en la Tabla 8 se presenta la comparación de las series
de tiempo observadas y modeladas para las variables meteorológicas velocidad del viento y dirección del viento. De la tabla se puede comprobar una alta
completitud de datos observados, lo que concuerda con lo presentado en la Tabla 7.

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Estación|Coordenadas UTM WGS 84 - 19S|Col3|Periodo considerado<br>para el análisis|Variables meteorológicas de<br>superficie| |---|---|---|---|---| |**Estación**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**| |Valle<br>Alegre<br>(SINCA)|271.889|6.367.413|01/01/23 - 31/12/23|- Velocidad del viento (m/s)<br>- Dirección del viento (°)| -->

**Tabla 7: - Resumen Datos Observados y Modelados en Estación Valle Alegre (SINCA) (SINCA).**

| Variable | Parámetro | Observado | Modelado |
| --- | --- | --- | --- |
| Velocidad del Viento | N° Datos Disponibles | 8.760 | 8.760 |
| Velocidad del Viento | N° Datos Válidos | 8.754 | 8.760 |
| Velocidad del Viento | Porcentaje de Datos Válidos | 100% | 100% |
| Velocidad del Viento | Promedio (m/s) | 0,7 | 1,9 |
| Velocidad del Viento | Máximo (m/s) | 5,0 | 9,1 |
| Velocidad del Viento | Mínimo (m/s) | 0,0 | 0,0 |
| Velocidad del Viento | Porcentaje de Calmas | 55% | 15% |
| Dirección del Viento | N° Datos Disponibles | 8.760 | 8.760 |
| Dirección del Viento | N° Datos Válidos | 8.754 | 8.760 |
| Dirección del Viento | Porcentaje de Datos Válidos | 100% | 100% |

<!-- Estadísticas: 10 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **3.4.1.** **Análisis Cualitativo** A continuación, se presenta el análisis de incertidumbre cualitativo, cuyo objetivo corresponde a comparar las series de tiempo, ciclos diarios, rosas de viento y ciclos estacionales observados y -->
<!-- FIN TABLA 7 -->


Tabla 8 - Series de Tiempo Observadas y Modeladas en Estación Valle Alegre (SINCA). Periodo 01/01/23 al 31/12/23.

|Variable|Observado|Modelado|
|---|---|---|
|Velocidad del<br>Viento|||

17

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

|Variable|Observado|Modelado|
|---|---|---|
|Dirección del<br>Viento|||

18

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.4.1.2.** **Ciclos Diarios**

En la Tabla 9 se presenta la comparación de los ciclos diarios, los que permiten visualizar los cambios en las variables meteorológicas a lo largo del día.

Tabla 9 - Ciclos Diarios Observados y Modelados en Estación Valle Alegre (SINCA). Periodo 01/01/23 al 31/12/23.

|Variable|Observado|Modelado|
|---|---|---|
|Velocidad del<br>Viento|||

19

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

|Variable|Observado|Modelado|
|---|---|---|
|Dirección del<br>Viento|||

A continuación, se describe la comparación de los ciclos diarios presentados:

ICSARA 1

Julio 2024

- **Ciclos diarios de velocidad del viento:** se aprecia que el modelo tiene la capacidad de representar los momentos del día donde se dan las mayores
velocidades de viento, los que corresponden al periodo diurno, particularmente en horas de la tarde. Por su parte, representa adecuadamente los
periodos del día con menores velocidades del viento, los que ocurren durante la madrugada y la noche. A su vez, se aprecia que el modelo
meteorológico tiende a sobrestimar la magnitud de la velocidad del viento observada en la Estación Valle Alegre (SINCA), a lo largo del día.

- **Ciclos diarios de dirección del viento:** en los histogramas presentados es posible apreciar que el modelo representa de manera precisa los vientos
predominantes observados, tanto en dirección como en frecuencia particularmente entre las 09:00 y las 19:00 horas.

20

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.4.1.3.** **Rosas de Viento**

En la Tabla 10 se presenta la comparación de rosas de viento observadas y modeladas para el periodo de estudio. En primer lugar, se muestran rosas para
el año completo (considerando todos los datos) y luego se presenta la comparación de rosas separada por periodo del día; madrugada, mañana, tarde y
noche.

Tabla 10 - Rosas de Viento Observadas y Modeladas en Estación Valle Alegre (SINCA). Periodo 01/01/23 al 31/12/23.

|Periodo|Observado|Modelado|
|---|---|---|
|Año<br>completo<br>(todos los<br>datos)|||

21

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

|Periodo|Observado|Modelado|
|---|---|---|
|Madrugada<br>(00:00-<br>05:00)|||
|Mañana<br>(06:00-<br>11:00)|||

22

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

|Periodo|Observado|Modelado|
|---|---|---|
|Tarde<br>(12:00-<br>17:00)|||
|Noche<br>(18:00-<br>23:00)|||

23

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

A continuación, se presenta la descripción de la comparación de las rosas de viento observadas y
modeladas:

 - **Año completo:** en ambas figuras se aprecia predominancia de vientos provenientes del oeste
suroeste. El modelo tiende a sobrestimar la velocidad del viento y a la vez a subestimar los
vientos provenientes del oeste y este noreste, en desmedro de una sobrestimación de los
vientos provenientes del suroeste. Sin embargo, la similitud en forma de ambas rosas de
viento indica una alta capacidad del modelo para representar la dirección y velocidad del
viento predominante para el set completo de datos.

 - **Madrugada (00:00-05:00):** el modelo representa de manera correcta la predominancia de
vientos provenientes del noreste, este noreste y este observados, pero subestima su
frecuencia. Por otro lado, el modelo sobrestima la frecuencia de vientos provenientes del
oeste suroeste, suroeste y sur sureste. En ambas rosas la velocidad del viento es de baja
magnitud, sin embargo, el modelo tiende a sobrestimarla.

 - **Mañana (06:00-11:00):** el modelo representa de buena forma los vientos observados durante
la mañana lo que se refleja en la similitud de ambas rosas y en que ambas muestran un
aumento en velocidad del viento respecto a la madrugada. A nivel específico, el modelo
sobrestima la velocidad del viento y sobrestima la frecuencia de vientos provenientes del
oeste suroeste y suroeste mientras que subestima la frecuencia de vientos provenientes del
este noreste y este. Al igual que en la madrugada, el modelo representa satisfactoriamente
la dirección y velocidad del viento en la mañana.

 - **Tarde (12:00-17:00):** durante la tarde la forma de ambas rosas de viento es notablemente
parecida en cuanto a las frecuencias predominantes, donde ambas muestran vientos con
mayor frecuencia provenientes del oeste suroeste. Además, ambas muestran un aumento
en la magnitud de la velocidad del viento comparado con lo que se tiene para horas de la
mañana y la madrugada. A nivel específico, el modelo sobrestima la velocidad del viento y la
frecuencia de vientos provenientes del suroeste, en desmedro de una subestimación de la
frecuencia de vientos que provienen del oeste.

 - **Noche (18:00-23:00):** el modelo representa de manera satisfactoria la reducción en la
magnitud de la velocidad del viento observada si se compara a lo que se presenta durante la
tarde, sin embargo, continúa sobrestimando esta variable. En relación con la dirección del
viento, ambas rosas tienen una forma parecida con predominancia de vientos del primer y
tercer cuadrante, donde el modelo subestima los vientos provenientes del este noreste y el
este, en desmedro de una sobrestimación de los vientos provenientes del oeste suroeste y
del suroeste.

En términos generales se aprecia de forma cualitativa que el modelo representa de manera adecuada
los vientos predominantes tanto para el año completo como para el desglose por hora del día, tal y
como se mostró en los ciclos diarios presentados en el inciso anterior, donde en este caso se vuelve
a demostrar la correcta capacidad del modelo de representar las direcciones y velocidades de viento
observadas, para las cuales si bien existen sobrestimaciones de la magnitud de la velocidad del
viento, esto se mantiene dentro de un rango normal y aceptable para un modelo meteorológico de
este tipo. A su vez, se demostró que el modelo muestra su mejor rendimiento en horas de la mañana
y la tarde, lo que coincide con los momentos del día donde se llevará a cabo la jornada laboral del
Proyecto. Por lo que se puede trabajar bajo el supuesto de que el periodo a modelar corresponde al
cual el modelo representa de mejor manera la meteorología de superficie observada.

24

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

**3.4.1.1.** **Ciclo Estacional**

ICSARA 1

Julio 2024

En la Tabla 11 se presenta la comparación del ciclo estacional de velocidad y dirección del viento, el que permite visualizar los cambios en las variables
meteorológicas a lo largo del año.

Tabla 11 - Ciclos Estacionales Observados y Modelados en Estación Valle Alegre (SINCA). Periodo 01/01/23 al 31/12/23.

|Variable|Observado|Modelado|
|---|---|---|
|Velocidad y<br>dirección del<br>viento|||

25

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

A continuación, se presenta la descripción de la comparación de los ciclos estacionales presentados:

 - **Ciclo estacional de vientos:** las flechas indican que el modelo presenta un buen desempeño

a la hora de representar la dirección del viento observada a lo largo de todo el año, donde se

ve que durante horas de la noche y la madrugada predominan vientos provenientes del

noreste, este y este noreste, mientras que en la mañana y en la tarde predominan vientos

provenientes del suroeste, oeste y sur suroeste. Además, se aprecia que el modelo

sobrestima la magnitud de la velocidad de viento observada, sin embargo, este representa

de manera adecuada los momentos del día y del año donde se esperan mayores velocidades

de viento, las que ocurren principalmente en el periodo diurno durante los meses de verano.

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

A continuación, en la Tabla 12 se presentan los resultados del cálculo de estadísticos para la variable
meteorológica de superficie velocidad del viento, comparando todos los datos observados y
modelados en la Estación Valle Alegre (SINCA) tanto para las series de tiempo como para los ciclos
diarios:

26

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

Tabla 12 - Estadísticos análisis cuantitativo. Estación Valle Alegre (SINCA).

ICSARA 1

Julio 2024

|Estadístico|Velocidad del Viento (m/s)|Col3|
|---|---|---|
|**Estadístico**|**Serie de Tiempo**|**Ciclo Diario**|
|Sesgo|1,13|1,13|
|Error Cuadrático Medio|1,65|1,31|
|Coeficiente de Correlación|0,71|0,99|

De la tabla anterior, se aprecia que el modelo tiene un sesgo de 1,13 m/s para la serie de tiempo y para
el ciclo diario de la velocidad del viento, lo que indica que el modelo sobrestima esta variable, tal y
como se mostró en el análisis cualitativo. Por su parte, se tiene un alto coeficiente de correlación
(0,71 para la serie de tiempo y 0,99 para el ciclo diario) y un error cuadrático medio de baja magnitud
(1,65 m/s para la serie de tiempo y 1,31 m/s para el ciclo diario). Lo anterior implica que el modelo si
bien sobrestima la velocidad de viento observada, tiene la capacidad suficiente para representar los
cambios en tendencias y logra replicar el ciclo diario observado para esta variable. Tal y como se
mostró en el análisis cualitativo, representa de manera satisfactoria los periodos del día con bajas y
altas velocidades de viento.

A modo de resumen, se aprecia de manera cualitativa y cuantitativa que el modelo meteorológico
WRF tiene la capacidad de representar las variables meteorológicas de superficie analizadas
(velocidad del viento y dirección del viento) de manera similar a lo observado en la estación
meteorológica Valle Alegre (SINCA) para el periodo de estudio (año 2023), particularmente durante
las horas donde se realizarán las actividades del Proyecto (periodo diurno), por lo que se cuenta con
un sustento técnico que respalda el uso de la información meteorológica WRF modelada como dato
de entrada para la modelación de calidad del aire presentada a continuación en los siguientes incisos.

27

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.5.** **Escenario de Modelación**

En este estudio se evalúa el escenario de modelación más conservador y desfavorable, que considera
el Proyecto en evaluación “Planta Fotovoltaica Vernazza” y además considera otros dos proyectos
cercanos; “Planta Fotovoltaica Manarola” [8] y “Planta Fotovoltaica Corniglia” [9] . El objetivo de evaluar
este escenario es determinar el potencial impacto sinérgico que podría generar la eventual
construcción de los tres proyectos de manera simultánea.

En base a información georreferenciada de cada Proyecto, se han diseñado las siguientes fuentes de
emisión que serán consideradas para la modelación:

 - **Fuentes Areales:** A estas fuentes se les asignan las emisiones asociadas a movimientos de

tierra, utilización de maquinaria y grupos generadores.

 - **Fuentes de Camino:** A estas fuentes se le asignan las emisiones asociadas a combustión
(motores vehículos) y resuspensión de polvo por tránsito vehicular (tránsito no
pavimentados y tránsito pavimentados).

De esta forma, se han definido 2 tipos de fuentes principales asociadas al Proyecto a las que serán
asignadas emisiones de acuerdo con sus características y su variabilidad temporal, para esta última
con el fin de modelar un escenario conservador se configuró el modelo tomando en cuenta las 52
semanas del año, jornada laboral de lunes a viernes (5 días por semana) y 8 horas de trabajo diarias.

El cálculo de la tasa de emisión para cada contaminante se realiza según las siguientes fórmulas.

**Fuentes Areales:**

[1 (día)]

8 (horas) [⋅1 (hora)] 3600 (seg)

[⋅1 (hora)] 3600 (seg) [⋅10] 1 (t) [6] [(g)]

1 (t)

[⋅1 (semana)] 5 (días) ⋅ 8 (horas) [1 (día)]

[g]

sm [2] [) = Emisión ] ~~[( ]~~ [t]

1 1 (año)

Área (m [2] ) [⋅] 52 (semanas) [⋅1 (semana)] 5 (días)

Tasa de Emisión ( [g]

1
año [t] [) ⋅]

**Fuentes Caminos:**

[1 (día)]

8 (horas) [⋅1 (hora)] 3600 (seg)

[⋅1 (hora)] 3600 (seg) [⋅10] 1 (t) [6] [(g)]

1 (t)

[g]

sm [) = Emisión ] ~~[( ]~~ [t]

⋅ [1 (día)]
5 (días) 8 (horas)

Tasa de Emisión ( [g]

1 1 (año)
año [t] [) ⋅] Largo (m) [⋅] 52 (semanas) [⋅1 (semana)] 5 (días)

Cabe señalar que para modelar la depositación de Material Particulado Sedimentable (MPS), se han
utilizado los valores de “ _geometric mass mean diameter_ ” y “ _geometric standard deviation_ ”, indicados
en bibliografía de referencia [10], cuyos valores corresponden a 20 y 1,24 respectivamente.

8 Enlace web al expediente de evaluación ambiental:
[https://seia.sea.gob.cl/expediente/ficha/fichaPrincipal.php?modo=normal&id_expediente=2161050349](https://seia.sea.gob.cl/expediente/ficha/fichaPrincipal.php?modo=normal&id_expediente=2161050349)
9 Enlace web al expediente de evaluación ambiental:
[https://seia.sea.gob.cl/expediente/ficha/fichaPrincipal.php?modo=normal&id_expediente=2161404028](https://seia.sea.gob.cl/expediente/ficha/fichaPrincipal.php?modo=normal&id_expediente=2161404028)
10 Guideline for Plume Dispersion Modeling, Barrie Lawrence, Government of Newfoundland and Labrador, Department of
Enviroment & Conservation, 2012.

28

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

El detalle de cada fuente, tipo, dimensiones, emisiones totales (obtenidas a partir del estudio de
estimación de emisiones de cada proyecto) y tasas de emisión de MP2,5, MP10 y MPS, se presenta a
continuación en la Tabla 13.

<!-- INICIO TABLA 13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- El detalle de cada fuente, tipo, dimensiones, emisiones totales (obtenidas a partir del estudio de estimación de emisiones de cada proyecto) y tasas de emisión de MP2,5, MP10 y MPS, se presenta a continuación en la Tabla 13. -->

**Tabla 13: - Fuentes de Emisión MP2.5, MP10 y MPS.**

| Proyecto | Fuente | Tipo | Dimensiones | Col5 | Emisiones Totales (t/año) | Col7 | Col8 | Tasas de Emisión | Col10 | Col11 | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Proyecto** | **Fuente** | **Tipo** | **Largo (m)** | **Área (m2) ** | **MP2.5** | **MP10** | **MPS** | **MP2.5** | **MP10** | **MPS** | **MPS** |
| Planta<br>Fotovoltaica<br>Vernazza | Ruta 1 | Camino | 10.763,1 | - | 0,03 | 0,09 | 0,47 | 3,42E-07 | 1,18E-06 | 5,80E-06 | g/sm |
| Planta<br>Fotovoltaica<br>Vernazza | Ruta 2 | Camino | 11.200,0 | - | 0,08 | 0,30 | 1,51 | 9,14E-07 | 3,53E-06 | 1,80E-05 | g/sm |
| Planta<br>Fotovoltaica<br>Vernazza | Ruta 4 | Camino | 10.763,1 | - | 3,45E-03 | 0,01 | 0,06 | 4,28E-08 | 1,47E-07 | 7,22E-07 | g/sm |
| Planta<br>Fotovoltaica<br>Vernazza | Ruta 5 | Camino | 1.975,7 | - | 0,08 | 0,79 | 2,58 | 5,42E-06 | 5,34E-05 | 1,74E-04 | g/sm |
| Planta<br>Fotovoltaica<br>Vernazza | Ruta 6.A | Camino | 681,5 | - | 0,02 | 0,16 | 0,53 | 3,22E-06 | 3,17E-05 | 1,03E-04 | g/sm |
| Planta<br>Fotovoltaica<br>Vernazza | Ruta 6.B | Camino | 1.821,6 | - | 0,01 | 0,13 | 0,43 | 9,74E-07 | 9,59E-06 | 3,13E-05 | g/sm |
| Planta<br>Fotovoltaica<br>Vernazza | Ruta 6.C | Camino | 1.810,1 | - | 0,01 | 0,14 | 0,45 | 1,04E-06 | 1,03E-05 | 3,35E-05 | g/sm |
| Planta<br>Fotovoltaica<br>Vernazza | Ruta 7 | Camino | 1.153,8 | - | 1,96E-04 | 7,36E-04 | 3,74E-03 | 2,27E-08 | 8,52E-08 | 4,32E-07 | g/sm |
| Planta<br>Fotovoltaica<br>Vernazza | Ruta 8 | Camino | 2.001,0 | - | 5,02E-03 | 0,05 | 0,16 | 3,35E-07 | 3,33E-06 | 1,09E-05 | g/sm |
| Planta<br>Fotovoltaica<br>Vernazza | Ruta 9a | Camino | 790,5 | - | 6,43E-05 | 6,31E-04 | 2,06E-03 | 1,09E-08 | 1,07E-07 | 3,48E-07 | g/sm |
| Planta<br>Fotovoltaica<br>Vernazza | Ruta 9b | Camino | 1.616,9 | - | 7,44E-05 | 6,41E-04 | 2,07E-03 | 6,14E-09 | 5,29E-08 | 1,71E-07 | g/sm |
| Planta<br>Fotovoltaica<br>Vernazza | Ruta 10 | Camino | 8.313,0 | - | 8,47E-04 | 3,18E-03 | 0,02 | 1,36E-08 | 5,11E-08 | 2,60E-07 | g/sm |
| Planta<br>Fotovoltaica<br>Vernazza | Proyecto<br>Movimientos de<br>Tierra | Area | - | 1.337.284,5 | 0,15 | 0,40 | 1,38 | 1,50E-08 | 4,01E-08 | 1,38E-07 | g/sm2 |
| Planta<br>Fotovoltaica<br>Vernazza | Proyecto<br>Maquinaria | Area | Area | Area | 0,35 | 0,35 | 0,35 | 3,50E-08 | 3,50E-08 | 3,50E-08 | g/sm2 |
| Planta<br>Fotovoltaica<br>Corniglia | Ruta 1 | Camino | 10.763,1 | - | 2,80E-03 | 9,67E-03 | 0,05 | 3,48E-08 | 1,20E-07 | 5,92E-07 | g/sm |
| Planta<br>Fotovoltaica<br>Corniglia | Ruta 2 | Camino | 11.200,0 | - | 0,02 | 0,07 | 0,36 | 2,16E-07 | 8,42E-07 | 4,32E-06 | g/sm |
| Planta<br>Fotovoltaica<br>Corniglia | Ruta 3.A | Camino | 1.880,0 | - | 2,00E-04 | 6,84E-04 | 3,37E-03 | 1,42E-08 | 4,86E-08 | 2,39E-07 | g/sm |
| Planta<br>Fotovoltaica<br>Corniglia | Ruta 3.B | Camino | 280,0 | - | 5,64E-05 | 2,12E-04 | 1,08E-03 | 2,69E-08 | 1,01E-07 | 5,14E-07 | g/sm |
| Planta<br>Fotovoltaica<br>Corniglia | Ruta 3.C | Camino | 120,0 | - | 1,51E-03 | 0,02 | 0,05 | 1,68E-06 | 1,68E-05 | 5,47E-05 | g/sm |
| Planta<br>Fotovoltaica<br>Corniglia | Ruta 4 | Camino | 20.638,2 | - | 1,02E-03 | 3,86E-03 | 0,02 | 6,61E-09 | 2,50E-08 | 1,27E-07 | g/sm |
| Planta<br>Fotovoltaica<br>Corniglia | Ruta 5.A | Camino | 1.047,9 | - | 0,01 | 0,14 | 0,46 | 1,83E-06 | 1,81E-05 | 5,90E-05 | g/sm |
| Planta<br>Fotovoltaica<br>Corniglia | Ruta 5.B | Camino | 350,0 | - | 4,73E-03 | 0,05 | 0,15 | 1,80E-06 | 1,79E-05 | 5,83E-05 | g/sm |
| Planta<br>Fotovoltaica<br>Corniglia | Ruta 6.A | Camino | 1.201,8 | - | 7,80E-04 | 7,69E-03 | 0,03 | 8,67E-08 | 8,55E-07 | 2,79E-06 | g/sm |
| Planta<br>Fotovoltaica<br>Corniglia | Ruta 6.B | Camino | 622,0 | - | 1,15E-04 | 1,13E-03 | 3,70E-03 | 2,47E-08 | 2,43E-07 | 7,94E-07 | g/sm |
| Planta<br>Fotovoltaica<br>Corniglia | Proyecto<br>Movimientos de<br>Tierra | Area | - | 188.961,6 | 0,04 | 0,11 | 0,34 | 2,69E-08 | 7,86E-08 | 2,41E-07 | g/sm2 |
| Planta<br>Fotovoltaica<br>Corniglia | Proyecto<br>Maquinaria | Area | - | - | 0,04 | 0,04 | 0,04 | 2,68E-08 | 2,68E-08 | 2,68E-08 | g/sm2 |
| Planta<br>Fotovoltaica<br>Manarola | Ruta 1 | Camino | 10763,1 | - | 3,23E-03 | 0,01 | 0,05 | 4,01E-08 | 1,37E-07 | 6,72E-07 | g/sm |
| Planta<br>Fotovoltaica<br>Manarola | Ruta 2 | Camino | 11200 | - | 0,02 | 0,06 | 0,31 | 1,85E-07 | 7,30E-07 | 3,75E-06 | g/sm |
| Planta<br>Fotovoltaica<br>Manarola | Ruta 3.A | Camino | 1880 | - | 2,05E-04 | 6,94E-04 | 3,41E-03 | 1,45E-08 | 4,93E-08 | 2,42E-07 | g/sm |

<!-- Estadísticas: 30 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- 29 Modelación de Dispersión de Contaminantes -->
<!-- FIN TABLA 13 -->


Tabla 13 - Fuentes de Emisión MP2.5, MP10 y MPS.

|Proyecto|Fuente|Tipo|Dimensiones|Col5|Emisiones Totales (t/año)|Col7|Col8|Tasas de Emisión|Col10|Col11|Unidad|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Proyecto**|**Fuente**|**Tipo**|**Largo (m)**|**Área (m2) **|**MP2.5**|**MP10**|**MPS**|**MP2.5**|**MP10**|**MPS**|**MPS**|
|Planta<br>Fotovoltaica<br>Vernazza|Ruta 1|Camino|10.763,1|-|0,03|0,09|0,47|3,42E-07|1,18E-06|5,80E-06|g/sm|
|Planta<br>Fotovoltaica<br>Vernazza|Ruta 2|Camino|11.200,0|-|0,08|0,30|1,51|9,14E-07|3,53E-06|1,80E-05|g/sm|
|Planta<br>Fotovoltaica<br>Vernazza|Ruta 4|Camino|10.763,1|-|3,45E-03|0,01|0,06|4,28E-08|1,47E-07|7,22E-07|g/sm|
|Planta<br>Fotovoltaica<br>Vernazza|Ruta 5|Camino|1.975,7|-|0,08|0,79|2,58|5,42E-06|5,34E-05|1,74E-04|g/sm|
|Planta<br>Fotovoltaica<br>Vernazza|Ruta 6.A|Camino|681,5|-|0,02|0,16|0,53|3,22E-06|3,17E-05|1,03E-04|g/sm|
|Planta<br>Fotovoltaica<br>Vernazza|Ruta 6.B|Camino|1.821,6|-|0,01|0,13|0,43|9,74E-07|9,59E-06|3,13E-05|g/sm|
|Planta<br>Fotovoltaica<br>Vernazza|Ruta 6.C|Camino|1.810,1|-|0,01|0,14|0,45|1,04E-06|1,03E-05|3,35E-05|g/sm|
|Planta<br>Fotovoltaica<br>Vernazza|Ruta 7|Camino|1.153,8|-|1,96E-04|7,36E-04|3,74E-03|2,27E-08|8,52E-08|4,32E-07|g/sm|
|Planta<br>Fotovoltaica<br>Vernazza|Ruta 8|Camino|2.001,0|-|5,02E-03|0,05|0,16|3,35E-07|3,33E-06|1,09E-05|g/sm|
|Planta<br>Fotovoltaica<br>Vernazza|Ruta 9a|Camino|790,5|-|6,43E-05|6,31E-04|2,06E-03|1,09E-08|1,07E-07|3,48E-07|g/sm|
|Planta<br>Fotovoltaica<br>Vernazza|Ruta 9b|Camino|1.616,9|-|7,44E-05|6,41E-04|2,07E-03|6,14E-09|5,29E-08|1,71E-07|g/sm|
|Planta<br>Fotovoltaica<br>Vernazza|Ruta 10|Camino|8.313,0|-|8,47E-04|3,18E-03|0,02|1,36E-08|5,11E-08|2,60E-07|g/sm|
|Planta<br>Fotovoltaica<br>Vernazza|Proyecto<br>Movimientos de<br>Tierra|Area|-|1.337.284,5|0,15|0,40|1,38|1,50E-08|4,01E-08|1,38E-07|g/sm2|
|Planta<br>Fotovoltaica<br>Vernazza|Proyecto<br>Maquinaria|Area|Area|Area|0,35|0,35|0,35|3,50E-08|3,50E-08|3,50E-08|g/sm2|
|Planta<br>Fotovoltaica<br>Corniglia|Ruta 1|Camino|10.763,1|-|2,80E-03|9,67E-03|0,05|3,48E-08|1,20E-07|5,92E-07|g/sm|
|Planta<br>Fotovoltaica<br>Corniglia|Ruta 2|Camino|11.200,0|-|0,02|0,07|0,36|2,16E-07|8,42E-07|4,32E-06|g/sm|
|Planta<br>Fotovoltaica<br>Corniglia|Ruta 3.A|Camino|1.880,0|-|2,00E-04|6,84E-04|3,37E-03|1,42E-08|4,86E-08|2,39E-07|g/sm|
|Planta<br>Fotovoltaica<br>Corniglia|Ruta 3.B|Camino|280,0|-|5,64E-05|2,12E-04|1,08E-03|2,69E-08|1,01E-07|5,14E-07|g/sm|
|Planta<br>Fotovoltaica<br>Corniglia|Ruta 3.C|Camino|120,0|-|1,51E-03|0,02|0,05|1,68E-06|1,68E-05|5,47E-05|g/sm|
|Planta<br>Fotovoltaica<br>Corniglia|Ruta 4|Camino|20.638,2|-|1,02E-03|3,86E-03|0,02|6,61E-09|2,50E-08|1,27E-07|g/sm|
|Planta<br>Fotovoltaica<br>Corniglia|Ruta 5.A|Camino|1.047,9|-|0,01|0,14|0,46|1,83E-06|1,81E-05|5,90E-05|g/sm|
|Planta<br>Fotovoltaica<br>Corniglia|Ruta 5.B|Camino|350,0|-|4,73E-03|0,05|0,15|1,80E-06|1,79E-05|5,83E-05|g/sm|
|Planta<br>Fotovoltaica<br>Corniglia|Ruta 6.A|Camino|1.201,8|-|7,80E-04|7,69E-03|0,03|8,67E-08|8,55E-07|2,79E-06|g/sm|
|Planta<br>Fotovoltaica<br>Corniglia|Ruta 6.B|Camino|622,0|-|1,15E-04|1,13E-03|3,70E-03|2,47E-08|2,43E-07|7,94E-07|g/sm|
|Planta<br>Fotovoltaica<br>Corniglia|Proyecto<br>Movimientos de<br>Tierra|Area|-|188.961,6|0,04|0,11|0,34|2,69E-08|7,86E-08|2,41E-07|g/sm2|
|Planta<br>Fotovoltaica<br>Corniglia|Proyecto<br>Maquinaria|Area|-|-|0,04|0,04|0,04|2,68E-08|2,68E-08|2,68E-08|g/sm2|
|Planta<br>Fotovoltaica<br>Manarola|Ruta 1|Camino|10763,1|-|3,23E-03|0,01|0,05|4,01E-08|1,37E-07|6,72E-07|g/sm|
|Planta<br>Fotovoltaica<br>Manarola|Ruta 2|Camino|11200|-|0,02|0,06|0,31|1,85E-07|7,30E-07|3,75E-06|g/sm|
|Planta<br>Fotovoltaica<br>Manarola|Ruta 3.A|Camino|1880|-|2,05E-04|6,94E-04|3,41E-03|1,45E-08|4,93E-08|2,42E-07|g/sm|

29

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

|Proyecto|Fuente|Tipo|Dimensiones|Col5|Emisiones Totales (t/año)|Col7|Col8|Tasas de Emisión|Col10|Col11|Unidad|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Proyecto**|**Fuente**|**Tipo**|**Largo (m)**|**Área (m2) **|**MP2.5**|**MP10**|**MPS**|**MP2.5**|**MP10**|**MPS**|**MPS**|
|**Proyecto**|Ruta 3.B|Camino|280|-|5,75E-05|2,15E-04|1,09E-03|2,74E-08|1,03E-07|5,20E-07|g/sm|
|**Proyecto**|Ruta 3.C|Camino|120|-|1,86E-03|0,02|0,06|2,07E-06|2,07E-05|6,77E-05|g/sm|
|**Proyecto**|Ruta 4|Camino|10763,1|-|1,25E-03|4,28E-03|0,02|1,55E-08|5,31E-08|2,62E-07|g/sm|
|**Proyecto**|Ruta 5|Camino|3300,8|-|0,04|0,42|1,38|1,72E-06|1,70E-05|5,56E-05|g/sm|
|**Proyecto**|Ruta 6|Camino|377,7|-|8,05E-04|7,93E-03|0,03|2,84E-07|2,80E-06|9,15E-06|g/sm|
|**Proyecto**|Proyecto - Parque|Area|-|193.416,6|0,16|0,47|1,11|1,10E-07|3,27E-07|7,69E-07|g/sm2|
|**Proyecto**|Proyecto - LMT|Area|-|47.410,4|0,02|0,05|0,20|6,11E-08|1,53E-07|5,70E-07|g/sm2|

Además, para poder estimar el aporte del Proyecto en relación a los metales pesados, en el contexto
de los Estudios de Suelo se realizaron calicatas con muestras de suelo en varios puntos que
representan el área de cada Proyecto. Estas muestras fueron llevadas al Laboratorio de la Facultad
de Agronomía y Sistemas Naturales de la Pontificia Universidad Católica de Chile para poder analizar
el contenido de metales pesados en cada una. A partir de este análisis, se estimó la tasa de emisión
de cada metal pesado para cada Proyecto como fracción del Material Particulado Respirable (MP10),
las cuales se presentan a continuación en la Tabla 14.

<!-- INICIO TABLA 14 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- de Agronomía y Sistemas Naturales de la Pontificia Universidad Católica de Chile para poder analizar el contenido de metales pesados en cada una. A partir de este análisis, se estimó la tasa de emisión de cada metal pesado para cada Proyecto como fracción del Material Particulado Respirable (MP10), las cuales se presentan a continuación en la Tabla 14. -->

**Tabla 14: - Fuentes de Emisión Metales Pesados.**

| Metal Pesado | Tasa de Emisión Proyecto<br>Vernazza (g/sm2) | Tasa de Emisión Proyecto<br>Corniglia (g/sm2) | Tasa de Emisión Proyecto<br>Manarola (g/sm2) |
| --- | --- | --- | --- |
| Cobre (Cu) | 6,21E-12 | 1,22E-11 | 3,62E-11 |
| Zinc (Zn) | 4,46E-12 | 8,75E-12 | 3,34E-11 |
| Manganeso (Mn) | 2,23E-11 | 4,37E-11 | 2,55E-10 |
| Hierro (Fe) | 1,35E-09 | 2,64E-09 | 1,19E-08 |
| Molibdeno (Mo) | 6,62E-14 | 1,30E-13 | 4,17E-13 |
| Cadmio (Cd) | 2,46E-14 | 4,84E-14 | 2,03E-13 |
| Mercurio (Hg) | 2,40E-15 | 4,72E-15 | 2,70E-14 |
| Níquel (Ni) | 3,00E-13 | 5,88E-13 | 2,38E-12 |
| Plomo (Pb) | 9,36E-13 | 1,84E-12 | 7,50E-12 |
| Vanadio (V) | 3,84E-12 | 7,55E-12 | 3,83E-11 |
| Selenio (Se) | 5,56E-15 | 1,09E-14 | 5,31E-14 |
| Arsénico (As) | 7,81E-13 | 1,53E-12 | 5,65E-12 |
| Antimonio (Sb) | 1,07E-13 | 2,10E-13 | 4,21E-12 |

<!-- Estadísticas: 13 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- 30 Modelación de Dispersión de Contaminantes -->
<!-- FIN TABLA 14 -->


Tabla 14 - Fuentes de Emisión Metales Pesados.

|Metal Pesado|Tasa de Emisión Proyecto<br>Vernazza (g/sm2)|Tasa de Emisión Proyecto<br>Corniglia (g/sm2)|Tasa de Emisión Proyecto<br>Manarola (g/sm2)|
|---|---|---|---|
|Cobre (Cu)|6,21E-12|1,22E-11|3,62E-11|
|Zinc (Zn)|4,46E-12|8,75E-12|3,34E-11|
|Manganeso (Mn)|2,23E-11|4,37E-11|2,55E-10|
|Hierro (Fe)|1,35E-09|2,64E-09|1,19E-08|
|Molibdeno (Mo)|6,62E-14|1,30E-13|4,17E-13|
|Cadmio (Cd)|2,46E-14|4,84E-14|2,03E-13|
|Mercurio (Hg)|2,40E-15|4,72E-15|2,70E-14|
|Níquel (Ni)|3,00E-13|5,88E-13|2,38E-12|
|Plomo (Pb)|9,36E-13|1,84E-12|7,50E-12|
|Vanadio (V)|3,84E-12|7,55E-12|3,83E-11|
|Selenio (Se)|5,56E-15|1,09E-14|5,31E-14|
|Arsénico (As)|7,81E-13|1,53E-12|5,65E-12|
|Antimonio (Sb)|1,07E-13|2,10E-13|4,21E-12|

30

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

Por su parte, en la Figura 3 se presenta un mapa con la ubicación de cada fuente:

Figura 3 - Fuentes de Emisión.

ICSARA 1

Julio 2024

31

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

**3.6.** **Receptores Discretos**

ICSARA 1

Julio 2024

Se han identificado 14 receptores discretos cercanos al Proyecto, de los cuales los seis primeros
corresponden a viviendas cercanas al proyecto identificadas en el Estudio de Ruido y el séptimo
corresponde a la estación EMRP Valle Alegre, en estos siete receptores se evaluarán las normas
primarias de calidad del aire.

Luego, los siguientes siete puntos corresponden a receptores identificados en el Estudio de
Caracterización de Flora y Vegetación, en los cuales se evaluarán las normas secundarias de calidad

del aire.

La Tabla 15 resume los receptores discretos, el tipo de norma de calidad del aire a evaluar en cada
uno y sus correspondientes coordenadas de ubicación geográfica.

Tabla 15 - Receptores Discretos.

|ID<br>Receptor|Descripción|Tipo de<br>Norma a<br>Evaluar|Coordenadas de Ubicación<br>(Datum WGS84)|Col5|
|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Tipo de**<br>**Norma a**<br>**Evaluar**|**Este (m)**|**Norte (m)**|
|RP1|Receptor 1|Primaria|269.798|6.367.679|
|RP2|Receptor 2|Primaria|271.544|6.368.233|
|RP3|Receptor 3|Primaria|269.132|6.369.438|
|RP4|Receptor 4|Primaria|267.982|6.369.575|
|RP5|Receptor 5|Primaria|267.311|6.370.101|
|RP6|Receptor 6|Primaria|266.580|6.371.009|
|RP7|Estación Valle Alegre (SINCA)|Primaria|271.889|6.367.413|
|RS1|Alstroemeria pulchra|Secundaria|270.070|6.368.420|
|RS2|Alstroemeria pulchra|Secundaria|271.162|6.369.432|
|RS3|Puya chilensis|Secundaria|270.097|6.370.294|
|RS4|Puya chilensis|Secundaria|270.073|6.370.360|
|RS5|Adiantum chilense|Secundaria|270.353|6.370.361|
|RS6|Cultivo de Cítricos|Secundaria|270.280|6.368.234|
|RS7|Plantación Eucaliptos|Secundaria|272.351|6.369.926|

Por su parte, en la Figura 4 se presenta un mapa con la ubicación de los receptores discretos:

32

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

Figura 4 - Receptores Discretos.

ICSARA 1

Julio 2024

33

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

**3.7.** **Resultados**

ICSARA 1

Julio 2024

En este inciso se presentan los resultados de la modelación de dispersión de contaminantes de
acuerdo con la información presentada en los incisos anteriores.

Para cada contaminante se presenta una tabla que compara el aporte del modelo en concentración
para cada receptor con la normativa de calidad del aire de acuerdo con las que fueron presentadas
en la Tabla 4, posteriormente se presentan las curvas de isoconcentración o isodepositación (según
corresponda), las que permiten visualizar la distribución del contaminante en el dominio de
modelación.

**3.7.1.** **Material Particulado Respirable Fino (MP2,5)**

**3.7.1.1.** **Resultados en Receptores Discretos**

En la Tabla 16 se presentan los resultados de la modelación de MP2,5 para el percentil 98 de 24 horas
y el periodo anual comparados con sus respectivas normativas primarias de calidad del aire.

Tabla 16 - Resultados Aporte Modelo en Receptores Discretos para MP2,5.

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Material Particulado Respirable (MP2.5)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto**|**Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este**<br>**(m)**|**Norte**<br>**(m)**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|
|RP1|Receptor 1|269.798|6.367.679|0,4|0,1|50|20|1%|0%|
|RP2|Receptor 2|271.540|6.368.241|0,2|0,1|0,1|0,1|0%|0%|
|RP3|Receptor 3|269.132|6.369.438|0,1|0,0|0,0|0,0|0%|0%|
|RP4|Receptor 4|267.975|6.369.581|0,0|0,0|0,0|0,0|0%|0%|
|RP5|Receptor 5|267.311|6.370.101|0,0|0,0|0,0|0,0|0%|0%|
|RP6|Receptor 6|266.580|6.371.009|0,0|0,0|0,0|0,0|0%|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|0,1|0,0|0,0|0,0|0%|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de MP2,5 para el
percentil 98 de 24 horas son de baja magnitud, siendo el máximo aporte de un 1% para el receptor 1,
para el resto de los receptores en el mismo periodo y para todos los receptores en periodo anual, el
aporte se considera nulo.

34

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.7.1.2.** **Curvas de Isoconcentración**

En la Figura 5 se presentan las curvas de isoconcentración para el percentil 98 de 24 horas de MP2,5:

Figura 5 - Curva de Isoconcentración MP2,5 P98 24 horas.

35

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

En la Figura 6 se presentan las curvas de isoconcentración para periodo anual de MP2,5:

Figura 6 - Curva de Isoconcentración MP2,5 Anual.

ICSARA 1

Julio 2024

36

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.7.2.** **Material Particulado Respirable (MP10)**

**3.7.2.1.** **Resultados en Receptores Discretos**

En la Tabla 17 se presentan los resultados de la modelación de MP10 para el percentil 98 de 24 horas
y el periodo anual comparados con sus respectivas normativas primarias de calidad del aire.

Tabla 17 - Resultados Aporte Modelo en Receptores Discretos para MP10.

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Material Particulado Respirable (MP10)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración**<br>**(μg/m3N) - Norma de**<br>**Calidad**|**Concentración**<br>**(μg/m3N) - Norma de**<br>**Calidad**|**Porcentaje de la**<br>**Norma de Calidad**|**Porcentaje de la**<br>**Norma de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|
|RP1|Receptor 1|269.798|6.367.679|1,3|0,3|130|50|1%|1%|
|RP2|Receptor 2|271.540|6.368.241|1,4|0,2|0,2|0,2|1%|0%|
|RP3|Receptor 3|269.132|6.369.438|0,4|0,0|0,0|0,0|0%|0%|
|RP4|Receptor 4|267.975|6.369.581|0,1|0,0|0,0|0,0|0%|0%|
|RP5|Receptor 5|267.311|6.370.101|0,0|0,0|0,0|0,0|0%|0%|
|RP6|Receptor 6|266.580|6.371.009|0,0|0,0|0,0|0,0|0%|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|0,3|0,0|0,0|0,0|0%|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de MP10 para el percentil
98 de 24 horas son de baja magnitud, siendo el máximo aporte de un 1% para el receptor 1 y el receptor
2. Para periodo anual el máximo aporte corresponde a un 1% en el receptor 1, para el resto de los
receptores el aporte se considera nulo.

37

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.7.2.2.** **Curvas de Isoconcentración**

En la Figura 7 se presentan las curvas de isoconcentración para el percentil 98 de 24 horas de MP10:

Figura 7 - Curva de Isoconcentración MP10 P98 24 horas.

38

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

En la Figura 8 se presentan las curvas de isoconcentración para periodo anual de MP10:

Figura 8 - Curva de Isoconcentración MP10 Anual.

ICSARA 1

Julio 2024

39

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.7.3.** **Material Particulado Sedimentable (MPS)**

**3.7.3.1.** **Resultados en Receptores Discretos**

En la Tabla 18 se presentan los resultados de la modelación de MPS para el periodo anual comparado
con las normativas secundarias internacionales de calidad del aire.

Tabla 18 - Resultados Aporte Modelo en Receptores Discretos para MPS.

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Material Particulado Sedimentable (MPS)|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Depositación (mg/m2-**<br>**día) - Aporte del**<br>**Proyecto**|Depositación (mg/m2-día) -<br>Norma de Calidad|Depositación (mg/m2-día) -<br>Norma de Calidad|**Porcentaje de la Norma de**<br>**Calidad**|**Porcentaje de la Norma de**<br>**Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este**<br>**(m)**|**Norte**<br>**(m)**|**Anual**|**Norma**<br>**Internacional**<br>**1 **|**Norma**<br>**Internacional**<br>**2 **|**Norma**<br>**Internacional**|**Norma**<br>**Internacional**|
|RS1|Alstroemeria pulchra|270.070|6.368.420|3,6|333|200|1%|2%|
|RS2|Alstroemeria pulchra|271.162|6.369.432|15,5|15,5|15,5|5%|8%|
|RS3|Puya chilensis|270.097|6.370.294|0,1|0,1|0,1|0%|0%|
|RS4|Puya chilensis|270.073|6.370.360|0,1|0,1|0,1|0%|0%|
|RS5|Adiantum chilense|270.353|6.370.361|0,4|0,4|0,4|0%|0%|
|RS6|Cultivo de Cítricos|270.280|6.368.234|6,5|6,5|6,5|2%|3%|
|RS7|Plantación Eucaliptos|272.351|6.369.926|0,1|0,1|0,1|0%|0%|

De la tabla anterior, se aprecia que los aportes del modelo en depositación de MPS para el periodo
anual alcanza como máximo aporte un 5% de la norma Argentina y un 8% para la norma internacional
Suiza en el receptor 2.

40

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

**3.7.3.2.** **Curvas de Isodepositación**

En la Figura 9 se presentan las curvas de isodepositación para periodo anual de MPS:

Figura 9 - Curva de Isodepositación MPS Anual.

ICSARA 1

Julio 2024

41

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.7.4.** **Cobre (Cu)**

**3.7.4.1.** **Resultados en Receptores Discretos**

En la Tabla 19 se presentan los resultados de la modelación de Cu para el periodo de 24 horas
comparado con su respectiva normativa primaria de calidad del aire.

Tabla 19 - Resultados Aporte Modelo en Receptores Discretos para Cu.

|ID<br>Receptor|Descripción|Coordenadas de Ubicación<br>(Datum WGS84)|Col4|Cobre (Cu)|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto**|**Concentración**<br>**(μg/m3) - Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**24 horas**|**24 horas**|**24 horas**|
|RP1|Receptor 1|269.798|6.367.679|1,3E-04|50|0%|
|RP2|Receptor 2|271.540|6.368.241|1,1E-04|1,1E-04|0%|
|RP3|Receptor 3|269.132|6.369.438|6,0E-05|6,0E-05|0%|
|RP4|Receptor 4|267.975|6.369.581|8,6E-06|8,6E-06|0%|
|RP5|Receptor 5|267.311|6.370.101|2,6E-06|2,6E-06|0%|
|RP6|Receptor 6|266.580|6.371.009|9,0E-07|9,0E-07|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|1,1E-05|1,1E-05|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de Cu para el periodo de
24 horas se pueden considerar nulos.

**3.7.5.** **Zinc (Zn)**

**3.7.5.1.** **Resultados en Receptores Discretos**

En la Tabla 20 se presentan los resultados de la modelación de Zn para el periodo de 24 horas
comparado con su respectiva normativa primaria de calidad del aire.

Tabla 20 - Resultados Aporte Modelo en Receptores Discretos para Zn.

|ID<br>Receptor|Descripción|Coordenadas de Ubicación<br>(Datum WGS84)|Col4|Zinc (Zn)|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto**|**Concentración**<br>**(μg/m3) - Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**24 horas**|**24 horas**|**24 horas**|
|RP1|Receptor 1|269.798|6.367.679|1,2E-04|120|0%|
|RP2|Receptor 2|271.540|6.368.241|9,1E-05|9,1E-05|0%|
|RP3|Receptor 3|269.132|6.369.438|5,2E-05|5,2E-05|0%|
|RP4|Receptor 4|267.975|6.369.581|7,0E-06|7,0E-06|0%|
|RP5|Receptor 5|267.311|6.370.101|2,1E-06|2,1E-06|0%|
|RP6|Receptor 6|266.580|6.371.009|7,2E-07|7,2E-07|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|8,6E-06|8,6E-06|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de Zn para el periodo de
24 horas se pueden considerar nulos.

42

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.7.6.** **Manganeso (Mn)**

**3.7.6.1.** **Resultados en Receptores Discretos**

En la Tabla 21 se presentan los resultados de la modelación de Mn para el periodo de 24 horas y el
periodo anual comparados con sus respectivas normativas primarias de calidad del aire.

Tabla 21 - Resultados Aporte Modelo en Receptores Discretos para Mn.

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Manganeso (Mn)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Porcentaje de la Norma de**<br>**Calidad**|**Porcentaje de la Norma de**<br>**Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este**<br>**(m)**|**Norte**<br>**(m)**|**24 horas**|**Periodo**<br>**Anual**|**24 horas**|**Periodo**<br>**Anual**|**24 horas**|**Periodo**<br>**Anual**|
|RP1|Receptor 1|269.798|6.367.679|8,1E-04|7,9E-05|0,2|0,15|3%|2%|
|RP2|Receptor 2|271.540|6.368.241|6,1E-04|1,1E-05|1,1E-05|1,1E-05|2%|0%|
|RP3|Receptor 3|269.132|6.369.438|3,6E-04|7,8E-06|7,8E-06|7,8E-06|1%|0%|
|RP4|Receptor 4|267.975|6.369.581|4,5E-05|1,2E-06|1,2E-06|1,2E-06|0%|0%|
|RP5|Receptor 5|267.311|6.370.101|1,4E-05|5,4E-07|5,4E-07|5,4E-07|0%|0%|
|RP6|Receptor 6|266.580|6.371.009|4,5E-06|2,7E-07|2,7E-07|2,7E-07|0%|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|5,4E-05|4,0E-06|4,0E-06|4,0E-06|0%|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de Mn para el periodo
de 24 horas y anual son de baja magnitud, siendo el máximo aporte de un 3% y un 2% en el receptor 1
respectivamente.

**3.7.7.** **Hierro (Fe)**

**3.7.7.1.** **Resultados en Receptores Discretos**

En la Tabla 22 se presentan los resultados de la modelación de Fe para el periodo de 24 horas
comparado con su respectiva normativa primaria de calidad del aire.

Tabla 22 - Resultados Aporte Modelo en Receptores Discretos para Fe.

|ID<br>Receptor|Descripción|Coordenadas de Ubicación<br>(Datum WGS84)|Col4|Hierro (Fe)|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto**|**Concentración**<br>**(μg/m3) - Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**24 horas**|**24 horas**|**24 horas**|
|RP1|Receptor 1|269.798|6.367.679|4,0E-02|4|1%|
|RP2|Receptor 2|271.540|6.368.241|3,1E-02|3,1E-02|1%|
|RP3|Receptor 3|269.132|6.369.438|1,8E-02|1,8E-02|0%|
|RP4|Receptor 4|267.975|6.369.581|2,3E-03|2,3E-03|0%|
|RP5|Receptor 5|267.311|6.370.101|7,1E-04|7,1E-04|0%|
|RP6|Receptor 6|266.580|6.371.009|2,4E-04|2,4E-04|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|2,8E-03|2,8E-03|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de Fe para el periodo de
24 horas son de baja magnitud, siendo el máximo aporte de un 1% en los receptores 1 y 2. Para los
otros receptores el aporte se puede considerar nulo.

43

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.7.8.** **Molibdeno (Mo)**

**3.7.8.1.** **Resultados en Receptores Discretos**

En la Tabla 23 se presentan los resultados de la modelación de Mo para el periodo de 24 horas
comparado con su respectiva normativa primaria de calidad del aire.

Tabla 23 - Resultados Aporte Modelo en Receptores Discretos para Mo.

|ID<br>Receptor|Descripción|Coordenadas de Ubicación<br>(Datum WGS84)|Col4|Molibdeno (Mo)|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto**|**Concentración**<br>**(μg/m3) - Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**24 horas**|**24 horas**|**24 horas**|
|RP1|Receptor 1|269.798|6.367.679|1,5E-06|120|0%|
|RP2|Receptor 2|271.540|6.368.241|1,2E-06|1,2E-06|0%|
|RP3|Receptor 3|269.132|6.369.438|6,7E-07|6,7E-07|0%|
|RP4|Receptor 4|267.975|6.369.581|9,6E-08|9,6E-08|0%|
|RP5|Receptor 5|267.311|6.370.101|2,9E-08|2,9E-08|0%|
|RP6|Receptor 6|266.580|6.371.009|9,9E-09|9,9E-09|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|1,2E-07|1,2E-07|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de Mo para el periodo
de 24 horas se pueden considerar nulos.

**3.7.9.** **Cadmio (Cd)**

**3.7.9.1.** **Resultados en Receptores Discretos**

En la Tabla 24 se presentan los resultados de la modelación de Cd para el periodo de 24 horas y el
periodo anual comparados con sus respectivas normativas primarias de calidad del aire.

Tabla 24 - Resultados Aporte Modelo en Receptores Discretos para Cd.

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Cadmio (Cd)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Porcentaje de la Norma de**<br>**Calidad**|**Porcentaje de la Norma de**<br>**Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este**<br>**(m)**|**Norte**<br>**(m)**|**24 horas**|**Periodo**<br>**Anual**|**24 horas**|**Periodo**<br>**Anual**|**24 horas**|**Periodo**<br>**Anual**|
|RP1|Receptor 1|269.798|6.367.679|6,9E-07|6,6E-08|0,025|0,005|0%|0%|
|RP2|Receptor 2|271.540|6.368.241|5,4E-07|1,0E-08|1,0E-08|1,0E-08|0%|0%|
|RP3|Receptor 3|269.132|6.369.438|3,1E-07|7,3E-09|7,3E-09|7,3E-09|0%|0%|
|RP4|Receptor 4|267.975|6.369.581|4,1E-08|1,1E-09|1,1E-09|1,1E-09|0%|0%|
|RP5|Receptor 5|267.311|6.370.101|1,2E-08|5,0E-10|5,0E-10|5,0E-10|0%|0%|
|RP6|Receptor 6|266.580|6.371.009|4,2E-09|2,6E-10|2,6E-10|2,6E-10|0%|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|5,0E-08|3,7E-09|3,7E-09|3,7E-09|0%|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de Cd para el periodo de
24 horas y anual se pueden considerar nulos.

44

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.7.10.** **Mercurio (Hg)**

**3.7.10.1.** **Resultados en Receptores Discretos**

En la Tabla 25 se presentan los resultados de la modelación de Hg para el periodo de 24 horas y el
periodo anual comparados con sus respectivas normativas primarias de calidad del aire.

Tabla 25 - Resultados Aporte Modelo en Receptores Discretos para Hg.

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Mercurio (Hg)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Porcentaje de la Norma de**<br>**Calidad**|**Porcentaje de la Norma de**<br>**Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este**<br>**(m)**|**Norte**<br>**(m)**|**24 horas**|**Periodo**<br>**Anual**|**24 horas**|**Periodo**<br>**Anual**|**24 horas**|**Periodo**<br>**Anual**|
|RP1|Receptor 1|269.798|6.367.679|8,6E-08|8,4E-09|4|1|0%|0%|
|RP2|Receptor 2|271.540|6.368.241|6,5E-08|1,2E-09|1,2E-09|1,2E-09|0%|0%|
|RP3|Receptor 3|269.132|6.369.438|3,9E-08|8,3E-10|8,3E-10|8,3E-10|0%|0%|
|RP4|Receptor 4|267.975|6.369.581|4,8E-09|1,3E-10|1,3E-10|1,3E-10|0%|0%|
|RP5|Receptor 5|267.311|6.370.101|1,5E-09|5,7E-11|5,7E-11|5,7E-11|0%|0%|
|RP6|Receptor 6|266.580|6.371.009|4,8E-10|2,9E-11|2,9E-11|2,9E-11|0%|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|5,7E-09|4,3E-10|4,3E-10|4,3E-10|0%|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de Hg para el periodo de
24 horas y anual se pueden considerar nulos.

**3.7.11.** **Níquel (Ni)**

**3.7.11.1.** **Resultados en Receptores Discretos**

En la Tabla 26 se presentan los resultados de la modelación de Ni para el periodo de 24 horas y el
periodo anual comparados con sus respectivas normativas primarias de calidad del aire.

Tabla 26 - Resultados Aporte Modelo en Receptores Discretos para Ni.

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Niquel (Ni)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Porcentaje de la Norma de**<br>**Calidad**|**Porcentaje de la Norma de**<br>**Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este**<br>**(m)**|**Norte**<br>**(m)**|**24 horas**|**Periodo**<br>**Anual**|**24 horas**|**Periodo**<br>**Anual**|**24 horas**|**Periodo**<br>**Anual**|
|RP1|Receptor 1|269.798|6.367.679|8,1E-06|7,8E-07|0,1|0,02|0%|0%|
|RP2|Receptor 2|271.540|6.368.241|6,4E-06|1,2E-07|1,2E-07|1,2E-07|0%|0%|
|RP3|Receptor 3|269.132|6.369.438|3,6E-06|8,7E-08|8,7E-08|8,7E-08|0%|0%|
|RP4|Receptor 4|267.975|6.369.581|4,9E-07|1,4E-08|1,4E-08|1,4E-08|0%|0%|
|RP5|Receptor 5|267.311|6.370.101|1,5E-07|6,0E-09|6,0E-09|6,0E-09|0%|0%|
|RP6|Receptor 6|266.580|6.371.009|5,0E-08|3,1E-09|3,1E-09|3,1E-09|0%|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|6,0E-07|4,4E-08|4,4E-08|4,4E-08|0%|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de Ni para el periodo de
24 horas y anual se pueden considerar nulos.

45

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.7.12.** **Plomo (Pb)**

**3.7.12.1.** **Resultados en Receptores Discretos**

En la Tabla 27 se presentan los resultados de la modelación de Pb para el periodo de 24 horas y el
periodo anual comparados con sus respectivas normativas primarias de calidad del aire.

Tabla 27 - Resultados Aporte Modelo en Receptores Discretos para Pb.

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Plomo (Pb)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Porcentaje de la Norma de**<br>**Calidad**|**Porcentaje de la Norma de**<br>**Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este**<br>**(m)**|**Norte**<br>**(m)**|**24 horas**|**Periodo**<br>**Anual**|**24 horas**|**Periodo**<br>**Anual**|**24 horas**|**Periodo**<br>**Anual**|
|RP1|Receptor 1|269.798|6.367.679|2,5E-05|2,4E-06|4|0,5|0%|0%|
|RP2|Receptor 2|271.540|6.368.241|2,0E-05|3,8E-07|3,8E-07|3,8E-07|0%|0%|
|RP3|Receptor 3|269.132|6.369.438|1,1E-05|2,7E-07|2,7E-07|2,7E-07|0%|0%|
|RP4|Receptor 4|267.975|6.369.581|1,5E-06|4,3E-08|4,3E-08|4,3E-08|0%|0%|
|RP5|Receptor 5|267.311|6.370.101|4,6E-07|1,9E-08|1,9E-08|1,9E-08|0%|0%|
|RP6|Receptor 6|266.580|6.371.009|1,6E-07|9,6E-09|9,6E-09|9,6E-09|0%|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|1,9E-06|1,4E-07|1,4E-07|1,4E-07|0%|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de Pb para el periodo de
24 horas y anual se pueden considerar nulos.

**3.7.13.** **Vanadio (V)**

**3.7.13.1.** **Resultados en Receptores Discretos**

En la Tabla 28 se presentan los resultados de la modelación de V para el periodo de 24 horas
comparado con su respectiva normativa primaria de calidad del aire.

Tabla 28 - Resultados Aporte Modelo en Receptores Discretos para V.

|ID<br>Receptor|Descripción|Coordenadas de Ubicación<br>(Datum WGS84)|Col4|Vanadio (V)|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto**|**Concentración**<br>**(μg/m3) - Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**24 horas**|**24 horas**|**24 horas**|
|RP1|Receptor 1|269.798|6.367.679|1,2E-04|2|0%|
|RP2|Receptor 2|271.540|6.368.241|9,5E-05|9,5E-05|0%|
|RP3|Receptor 3|269.132|6.369.438|5,6E-05|5,6E-05|0%|
|RP4|Receptor 4|267.975|6.369.581|7,1E-06|7,1E-06|0%|
|RP5|Receptor 5|267.311|6.370.101|2,2E-06|2,2E-06|0%|
|RP6|Receptor 6|266.580|6.371.009|7,1E-07|7,1E-07|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|8,6E-06|8,6E-06|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de V para el periodo de
24 horas se pueden considerar nulos.

46

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.7.14.** **Selenio (Se)**

**3.7.14.1.** **Resultados en Receptores Discretos**

En la Tabla 29 se presentan los resultados de la modelación de Se para el periodo de 24 horas
comparado con su respectiva normativa primaria de calidad del aire.

Tabla 29 - Resultados Aporte Modelo en Receptores Discretos para Se.

|ID<br>Receptor|Descripción|Coordenadas de Ubicación<br>(Datum WGS84)|Col4|Selenio (Se)|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto**|**Concentración**<br>**(μg/m3) - Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**24 horas**|**24 horas**|**24 horas**|
|RP1|Receptor 1|269.798|6.367.679|1,7E-07|10|0%|
|RP2|Receptor 2|271.540|6.368.241|1,3E-07|1,3E-07|0%|
|RP3|Receptor 3|269.132|6.369.438|7,8E-08|7,8E-08|0%|
|RP4|Receptor 4|267.975|6.369.581|1,0E-08|1,0E-08|0%|
|RP5|Receptor 5|267.311|6.370.101|3,1E-09|3,1E-09|0%|
|RP6|Receptor 6|266.580|6.371.009|1,0E-09|1,0E-09|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|1,2E-08|1,2E-08|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de Se para el periodo de
24 horas se pueden considerar nulos.

**3.7.15.** **Arsénico (As)**

**3.7.15.1.** **Resultados en Receptores Discretos**

En la Tabla 30 se presentan los resultados de la modelación de As para el periodo de 24 horas y el
periodo anual comparados con sus respectivas normativas primarias de calidad del aire.

Tabla 30 - Resultados Aporte Modelo en Receptores Discretos para As.

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Arsénico (As)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Concentración (μg/m3) -**<br>**Norma de Calidad**|**Porcentaje de la Norma de**<br>**Calidad**|**Porcentaje de la Norma de**<br>**Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este**<br>**(m)**|**Norte**<br>**(m)**|**24 horas**|**Periodo**<br>**Anual**|**24 horas**|**Periodo**<br>**Anual**|**24 horas**|**Periodo**<br>**Anual**|
|RP1|Receptor 1|269.798|6.367.679|2,0E-05|1,9E-06|0,3|0,006|0%|0%|
|RP2|Receptor 2|271.540|6.368.241|1,6E-05|3,0E-07|3,0E-07|3,0E-07|0%|0%|
|RP3|Receptor 3|269.132|6.369.438|8,8E-06|2,2E-07|2,2E-07|2,2E-07|0%|0%|
|RP4|Receptor 4|267.975|6.369.581|1,2E-06|3,4E-08|3,4E-08|3,4E-08|0%|0%|
|RP5|Receptor 5|267.311|6.370.101|3,6E-07|1,5E-08|1,5E-08|1,5E-08|0%|0%|
|RP6|Receptor 6|266.580|6.371.009|1,2E-07|7,7E-09|7,7E-09|7,7E-09|0%|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|1,5E-06|1,1E-07|1,1E-07|1,1E-07|0%|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de As para el periodo de
24 horas y anual se pueden considerar nulos.

47

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**3.7.16.** **Antimonio (Sb)**

**3.7.16.1.** **Resultados en Receptores Discretos**

En la Tabla 31 se presentan los resultados de la modelación de Sb para el periodo de 24 horas y el
periodo anual comparados con sus respectivas normativas primarias de calidad del aire.

Tabla 31 - Resultados Aporte Modelo en Receptores Discretos para Sb.

|ID<br>Receptor|Descripción|Coordenadas de Ubicación<br>(Datum WGS84)|Col4|Antimonio (Sb)|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto**|**Concentración**<br>**(μg/m3) - Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Periodo Anual**|**Periodo Anual**|**Periodo Anual**|
|RP1|Receptor 1|269.798|6.367.679|1,2E-05|25|0%|
|RP2|Receptor 2|271.540|6.368.241|8,2E-06|8,2E-06|0%|
|RP3|Receptor 3|269.132|6.369.438|5,4E-06|5,4E-06|0%|
|RP4|Receptor 4|267.975|6.369.581|5,6E-07|5,6E-07|0%|
|RP5|Receptor 5|267.311|6.370.101|1,8E-07|1,8E-07|0%|
|RP6|Receptor 6|266.580|6.371.009|5,2E-08|5,2E-08|0%|
|RP7|Estación Valle Alegre (SINCA)|271.889|6.367.413|6,8E-07|6,8E-07|0%|

De la tabla anterior, se aprecia que los aportes del modelo en concentración de Sb para el periodo de
24 horas se pueden considerar nulos.

**3.8.** **Verificación Significancia Aporte Proyecto**

En consideración a la “Guía para la Evaluación Ambiental del Riesgo para la Salud a la Población”
(SEA 2, 2023) aplicable a la zona de estudio por tratarse de un área declarada saturada según el
Decreto Supremo N°10/2015 del Ministerio del Medio Ambiente que Declara Zona Saturada y Latente
a las Comunas de Concón, Quintero y Puchuncaví, de acuerdo al inciso 4 de dicha guía “Criterios para
Evaluar la Significancia del Aporte de Emisiones de Material Particulado Respirable, MP10 y MP2,5”,
en su segundo párrafo señala: “ _Cabe recordar que, independiente de la duración del impacto, los_
_valores sólo serán aplicables cuando las concentraciones obtenidas en los receptores humanos_
_analizados estén por encima, en concentración y periodo, de las establecidas en las normas primarias de_
_calidad ambiental para MP10 y MP2,5 vigentes al momento de la evaluación”_ .

Tomando en cuenta los resultados presentados en el inciso anterior, se demostró que en todos los
receptores evaluados tanto para las normas de periodo diario como anual, los aportes del Proyecto
no superan ninguna de las normas primarias ni secundarias para todos los contaminantes evaluados,
por lo que no aplica la evaluación del criterio de esta guía, toda vez que los aportes están muy lejos
de ser equivalentes a una condición de latencia y más aún de superar las normas primarias y
secundarias de calidad del aire vigentes. Lo anterior, implica que a partir de los resultados del
estudio, se comprueba técnicamente que la ejecución del año de mayor emisión del Proyecto no va
a generar riesgos a la salud de la población.

48

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**4.** **Conclusiones**

En este documento se ha presentado la modelación de dispersión de contaminantes atmosféricos
del proyecto _“Planta Fotovoltaica Vernazza”_ para los contaminantes MP2,5, MP10, MPS, Cu, Zn, Fe,
Mo, Cd, Hg, Ni, Pb, V, Se, As y Sb. A partir de los resultados presentados en este informe, se tienen
las siguientes conclusiones:

 - Respecto al análisis de incertidumbre, se concluye que el modelo WRF en el dominio de

20x20km tiene la capacidad de representar la meteorología observada, en particular, se

comparó de forma cualitativa y cuantitativa los resultados del modelo meteorológico con
registros observados en la estación meteorológica Valle Alegre (SINCA). A partir del análisis,

se concluye que el modelo representa de manera aceptable las variables meteorológicas de

superficie velocidad del viento y dirección del viento.

 - A partir de los resultados de la modelación de dispersión de contaminantes atmosféricos, se

concluye que para el primer año, que corresponde al año de mayor emisión del Proyecto

(fase de construcción y operación), en ninguno de los contaminantes evaluados (MP2,5,
MP10, MPS, Cu, Zn, Fe, Mo, Cd, Hg, Ni, Pb, V, Se, As y Sb) se superan los límites establecidos
en las normativas primarias ni secundarias de calidad del aire (tanto nacionales como
internacionales de referencia), tampoco se alcanza condición de latencia, sino más bien se

alcanzan aportes muy bajos en magnitud, en el escenario más conservador evaluado que

considera el efecto sinérgico del Proyecto “Planta Fotovoltaica Vernazza” y los proyectos

cercanos “Planta Fotovoltaica Manarola” y “Planta Fotovoltaica Corniglia”.

 - Además, se comprobó que el aporte del proyecto sobre la Estación Valle Alegre (SINCA) se

puede considerar nulo, por lo que se espera que su ejecución no modifique la condición base

de esta estación de calidad del aire, la cual corresponde a la estación EMRP más cercana al

Proyecto.

 - Finalmente, se concluye en base al estudio presentado que la ejecución del Proyecto “Planta

Fotovoltaica Vernazza” no propenderá a generar un aumento en concentración de

contaminantes atmosféricos que pueda suponer riesgos en la salud de la población ni

tampoco a recursos naturales, por lo que su ejecución no va a generar cambios de

significancia en la calidad del aire de la zona.

49

Modelación de Dispersión de Contaminantes

_DIA “Planta Fotovoltaica Vernazza”_

ICSARA 1

Julio 2024

**5.** **Referencias**

SEA 2. (2023). _Guía para la Evaluación Ambiental del Riesgo para la Salud de la Población._ Servicio de

Evaluación Ambiental.

SEA. (2023). _Guía para uso de Modelos de Calidad del Aire en el SEIA._ Servicio de Evaluación Ambiental.

**6.** **Anexos**

A continuación, a modo de respaldo se presentan los nombres de los anexos digitales incluidos con
este informe, a partir de los cuales la Autoridad podrá tener respaldo de los archivos requeridos
según la “Guía para uso de modelos de calidad del aire en el SEIA”.

 - Anexo Digital A - Archivos Digitales de Modelación ICSARA 1

50

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4: - Normas Primarias de Calidad del Aire.**

| Contaminante | Decreto Aplicable | Norma | Col4 | Periodo de Evaluación de Cumplimiento<br>de Norma |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Decreto Aplicable** | **Valor** | **Unidad** | **Unidad** |
| Material Particulado<br>Respirable Fino<br>(MP2,5) | Decreto Supremo N°12/2010 del Ministerio del<br>Medio Ambiente1 | 50 | μg/m3 | Percentil 98 de las concentraciones de<br>24 horas |
| Material Particulado<br>Respirable Fino<br>(MP2,5) | Decreto Supremo N°12/2010 del Ministerio del<br>Medio Ambiente1 | 20 | 20 | Promedio anual |
| Material Particulado<br>Respirable (MP10) | Decreto Supremo N°12/2022 del Ministerio del<br>Medio Ambiente2 | 130 | μg/m3N | Percentil 98 de las concentraciones de<br>24 horas |
| Material Particulado<br>Respirable (MP10) | Decreto Supremo N°12/2022 del Ministerio del<br>Medio Ambiente2 | 50 | 50 | Promedio anual |
| Cobre (Cu) | Ambient Air Quality Criteria - Ontario, Canada3 | 50 | μg/m3 | Concentración 24 horas |
| Zinc (Zn) | Ambient Air Quality Criteria - Ontario, Canada | 120 | μg/m3 | Concentración 24 horas |
| Manganeso (Mn) | Ambient Air Quality Criteria - Ontario, Canada | 0,2 | μg/m3 | Concentración 24 horas |
| Manganeso (Mn) | Air Quality Guidelines for Europe Second Edition<br>(OMS)4 | 0,15 | μg/m3 | Promedio anual |
| Hierro (Fe) | Ambient Air Quality Criteria - Ontario, Canada | 4 | μg/m3 | Concentración 24 horas |
| Molibdeno (Mo) | Ambient Air Quality Criteria - Ontario, Canada | 120 | μg/m3 | Concentración 24 horas |
| Cadmio (Cd) | Ambient Air Quality Criteria - Ontario, Canada | 0,025 | μg/m3 | Concentración 24 horas |
| Cadmio (Cd) | Real Decreto 102/2011, de 28 de enero, relativo a<br>la mejora de la calidad del aire (España)5 | 0,005 | μg/m3 | Promedio anual |
| Mercurio (Hg) | Ambient Air Quality Criteria - Ontario, Canada | 4 | μg/m3 | Concentración 24 horas |
| Mercurio (Hg) | Air Quality Guidelines for Europe Second Edition<br>(OMS) | 1 | μg/m3 | Concentración 24 horas |
| Níquel (Ni) | Ambient Air Quality Criteria - Ontario, Canada | 0,1 | μg/m3 | Concentración 24 horas |
| Níquel (Ni) | Real Decreto 102/2011, de 28 de enero, relativo a<br>la mejora de la calidad del aire (España) | 0,02 | μg/m3 | Promedio anual |
| Plomo (Pb) | Ambient Air Quality Criteria - Ontario, Canada | 4 | μg/m3 | Concentración 24 horas |
| Plomo (Pb) | Decreto Supremo N° 136/2000 del Ministerio<br>Secretaría General de la Presidencia6 | 0,5 | μg/m3 | Promedio anual |
| Vanadio (V) | Ambient Air Quality Criteria - Ontario, Canada | 2 | μg/m3 | Concentración 24 horas |
| Selenio (Se) | Ambient Air Quality Criteria - Ontario, Canada | 10 | μg/m3 | Concentración 24 horas |
| Arsénico (As) | Ambient Air Quality Criteria - Ontario, Canada | 0,3 | μg/m3 | Concentración 24 horas |
| Arsénico (As) | Real Decreto 102/2011, de 28 de enero, relativo a<br>la mejora de la calidad del aire (España) | 0,006 | μg/m3 | Promedio anual |
| Antimonio (Sb) | Ambient Air Quality Criteria - Ontario, Canada | 25 | μg/m3 | Concentración 24 horas |

**Tabla 5: - Normas Secundarias de Calidad del Aire.**

| Contaminante | Decreto Aplicable | Norma | Col4 | Periodo de Evaluación de<br>Cumplimiento de Norma |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Decreto Aplicable** | **Valor** | **Unidad** | **Unidad** |
| Material Particulado Sedimentable<br>(MPS) | Norma Argentina | 333 | mg/m2/día | Promedio mensual |
| Material Particulado Sedimentable<br>(MPS) | Norma Confederación Suiza | 200 | mg/m2/día | Promedio anual |

**Tabla 6: - Estación Meteorológica Valle Alegre (SINCA).**

| Estación | Coordenadas UTM WGS 84 - 19S | Col3 | Periodo considerado<br>para el análisis | Variables meteorológicas de<br>superficie |
| --- | --- | --- | --- | --- |
| **Estación** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| Valle<br>Alegre<br>(SINCA) | 271.889 | 6.367.413 | 01/01/23 - 31/12/23 | - Velocidad del viento (m/s)<br>- Dirección del viento (°) |

**Tabla 8: - Series de Tiempo Observadas y Modeladas en Estación Valle Alegre (SINCA). Periodo 01/01/23 al 31/12/23.**

| Variable | Observado | Modelado |
| --- | --- | --- |
| Velocidad del<br>Viento |  |  |

**Tabla 9: - Ciclos Diarios Observados y Modelados en Estación Valle Alegre (SINCA). Periodo 01/01/23 al 31/12/23.**

| Variable | Observado | Modelado |
| --- | --- | --- |
| Velocidad del<br>Viento |  |  |

**Tabla 10: - Rosas de Viento Observadas y Modeladas en Estación Valle Alegre (SINCA). Periodo 01/01/23 al 31/12/23.**

| Periodo | Observado | Modelado |
| --- | --- | --- |
| Año<br>completo<br>(todos los<br>datos) |  |  |

**Tabla 11: - Ciclos Estacionales Observados y Modelados en Estación Valle Alegre (SINCA). Periodo 01/01/23 al 31/12/23.**

| Variable | Observado | Modelado |
| --- | --- | --- |
| Velocidad y<br>dirección del<br>viento |  |  |

**Tabla 12: - Estadísticos análisis cuantitativo. Estación Valle Alegre (SINCA).**

| Estadístico | Velocidad del Viento (m/s) | Col3 |
| --- | --- | --- |
| **Estadístico** | **Serie de Tiempo** | **Ciclo Diario** |
| Sesgo | 1,13 | 1,13 |
| Error Cuadrático Medio | 1,65 | 1,31 |
| Coeficiente de Correlación | 0,71 | 0,99 |

**Tabla 15: - Receptores Discretos.**

| ID<br>Receptor | Descripción | Tipo de<br>Norma a<br>Evaluar | Coordenadas de Ubicación<br>(Datum WGS84) | Col5 |
| --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Tipo de**<br>**Norma a**<br>**Evaluar** | **Este (m)** | **Norte (m)** |
| RP1 | Receptor 1 | Primaria | 269.798 | 6.367.679 |
| RP2 | Receptor 2 | Primaria | 271.544 | 6.368.233 |
| RP3 | Receptor 3 | Primaria | 269.132 | 6.369.438 |
| RP4 | Receptor 4 | Primaria | 267.982 | 6.369.575 |
| RP5 | Receptor 5 | Primaria | 267.311 | 6.370.101 |
| RP6 | Receptor 6 | Primaria | 266.580 | 6.371.009 |
| RP7 | Estación Valle Alegre (SINCA) | Primaria | 271.889 | 6.367.413 |
| RS1 | Alstroemeria pulchra | Secundaria | 270.070 | 6.368.420 |
| RS2 | Alstroemeria pulchra | Secundaria | 271.162 | 6.369.432 |
| RS3 | Puya chilensis | Secundaria | 270.097 | 6.370.294 |
| RS4 | Puya chilensis | Secundaria | 270.073 | 6.370.360 |
| RS5 | Adiantum chilense | Secundaria | 270.353 | 6.370.361 |
| RS6 | Cultivo de Cítricos | Secundaria | 270.280 | 6.368.234 |
| RS7 | Plantación Eucaliptos | Secundaria | 272.351 | 6.369.926 |

**Tabla 16: - Resultados Aporte Modelo en Receptores Discretos para MP2,5.**

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Material Particulado Respirable (MP2.5) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto** | **Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este**<br>**(m)** | **Norte**<br>**(m)** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 0,4 | 0,1 | 50 | 20 | 1% | 0% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 0,2 | 0,1 | 0,1 | 0,1 | 0% | 0% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 0,1 | 0,0 | 0,0 | 0,0 | 0% | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 0,0 | 0,0 | 0,0 | 0,0 | 0% | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 0,0 | 0,0 | 0,0 | 0,0 | 0% | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 0,0 | 0,0 | 0,0 | 0,0 | 0% | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 0,1 | 0,0 | 0,0 | 0,0 | 0% | 0% |

**Tabla 17: - Resultados Aporte Modelo en Receptores Discretos para MP10.**

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Material Particulado Respirable (MP10) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración**<br>**(μg/m3N) - Norma de**<br>**Calidad** | **Concentración**<br>**(μg/m3N) - Norma de**<br>**Calidad** | **Porcentaje de la**<br>**Norma de Calidad** | **Porcentaje de la**<br>**Norma de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 1,3 | 0,3 | 130 | 50 | 1% | 1% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 1,4 | 0,2 | 0,2 | 0,2 | 1% | 0% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 0,4 | 0,0 | 0,0 | 0,0 | 0% | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 0,1 | 0,0 | 0,0 | 0,0 | 0% | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 0,0 | 0,0 | 0,0 | 0,0 | 0% | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 0,0 | 0,0 | 0,0 | 0,0 | 0% | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 0,3 | 0,0 | 0,0 | 0,0 | 0% | 0% |

**Tabla 18: - Resultados Aporte Modelo en Receptores Discretos para MPS.**

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Material Particulado Sedimentable (MPS) | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Depositación (mg/m2-**<br>**día) - Aporte del**<br>**Proyecto** | Depositación (mg/m2-día) -<br>Norma de Calidad | Depositación (mg/m2-día) -<br>Norma de Calidad | **Porcentaje de la Norma de**<br>**Calidad** | **Porcentaje de la Norma de**<br>**Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este**<br>**(m)** | **Norte**<br>**(m)** | **Anual** | **Norma**<br>**Internacional**<br>**1 ** | **Norma**<br>**Internacional**<br>**2 ** | **Norma**<br>**Internacional** | **Norma**<br>**Internacional** |
| RS1 | Alstroemeria pulchra | 270.070 | 6.368.420 | 3,6 | 333 | 200 | 1% | 2% |
| RS2 | Alstroemeria pulchra | 271.162 | 6.369.432 | 15,5 | 15,5 | 15,5 | 5% | 8% |
| RS3 | Puya chilensis | 270.097 | 6.370.294 | 0,1 | 0,1 | 0,1 | 0% | 0% |
| RS4 | Puya chilensis | 270.073 | 6.370.360 | 0,1 | 0,1 | 0,1 | 0% | 0% |
| RS5 | Adiantum chilense | 270.353 | 6.370.361 | 0,4 | 0,4 | 0,4 | 0% | 0% |
| RS6 | Cultivo de Cítricos | 270.280 | 6.368.234 | 6,5 | 6,5 | 6,5 | 2% | 3% |
| RS7 | Plantación Eucaliptos | 272.351 | 6.369.926 | 0,1 | 0,1 | 0,1 | 0% | 0% |

**Tabla 19: - Resultados Aporte Modelo en Receptores Discretos para Cu.**

| ID<br>Receptor | Descripción | Coordenadas de Ubicación<br>(Datum WGS84) | Col4 | Cobre (Cu) | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto** | **Concentración**<br>**(μg/m3) - Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **24 horas** | **24 horas** | **24 horas** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 1,3E-04 | 50 | 0% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 1,1E-04 | 1,1E-04 | 0% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 6,0E-05 | 6,0E-05 | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 8,6E-06 | 8,6E-06 | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 2,6E-06 | 2,6E-06 | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 9,0E-07 | 9,0E-07 | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 1,1E-05 | 1,1E-05 | 0% |

**Tabla 20: - Resultados Aporte Modelo en Receptores Discretos para Zn.**

| ID<br>Receptor | Descripción | Coordenadas de Ubicación<br>(Datum WGS84) | Col4 | Zinc (Zn) | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto** | **Concentración**<br>**(μg/m3) - Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **24 horas** | **24 horas** | **24 horas** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 1,2E-04 | 120 | 0% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 9,1E-05 | 9,1E-05 | 0% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 5,2E-05 | 5,2E-05 | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 7,0E-06 | 7,0E-06 | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 2,1E-06 | 2,1E-06 | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 7,2E-07 | 7,2E-07 | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 8,6E-06 | 8,6E-06 | 0% |

**Tabla 21: - Resultados Aporte Modelo en Receptores Discretos para Mn.**

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Manganeso (Mn) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Porcentaje de la Norma de**<br>**Calidad** | **Porcentaje de la Norma de**<br>**Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este**<br>**(m)** | **Norte**<br>**(m)** | **24 horas** | **Periodo**<br>**Anual** | **24 horas** | **Periodo**<br>**Anual** | **24 horas** | **Periodo**<br>**Anual** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 8,1E-04 | 7,9E-05 | 0,2 | 0,15 | 3% | 2% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 6,1E-04 | 1,1E-05 | 1,1E-05 | 1,1E-05 | 2% | 0% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 3,6E-04 | 7,8E-06 | 7,8E-06 | 7,8E-06 | 1% | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 4,5E-05 | 1,2E-06 | 1,2E-06 | 1,2E-06 | 0% | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 1,4E-05 | 5,4E-07 | 5,4E-07 | 5,4E-07 | 0% | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 4,5E-06 | 2,7E-07 | 2,7E-07 | 2,7E-07 | 0% | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 5,4E-05 | 4,0E-06 | 4,0E-06 | 4,0E-06 | 0% | 0% |

**Tabla 22: - Resultados Aporte Modelo en Receptores Discretos para Fe.**

| ID<br>Receptor | Descripción | Coordenadas de Ubicación<br>(Datum WGS84) | Col4 | Hierro (Fe) | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto** | **Concentración**<br>**(μg/m3) - Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **24 horas** | **24 horas** | **24 horas** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 4,0E-02 | 4 | 1% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 3,1E-02 | 3,1E-02 | 1% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 1,8E-02 | 1,8E-02 | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 2,3E-03 | 2,3E-03 | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 7,1E-04 | 7,1E-04 | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 2,4E-04 | 2,4E-04 | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 2,8E-03 | 2,8E-03 | 0% |

**Tabla 23: - Resultados Aporte Modelo en Receptores Discretos para Mo.**

| ID<br>Receptor | Descripción | Coordenadas de Ubicación<br>(Datum WGS84) | Col4 | Molibdeno (Mo) | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto** | **Concentración**<br>**(μg/m3) - Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **24 horas** | **24 horas** | **24 horas** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 1,5E-06 | 120 | 0% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 1,2E-06 | 1,2E-06 | 0% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 6,7E-07 | 6,7E-07 | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 9,6E-08 | 9,6E-08 | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 2,9E-08 | 2,9E-08 | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 9,9E-09 | 9,9E-09 | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 1,2E-07 | 1,2E-07 | 0% |

**Tabla 24: - Resultados Aporte Modelo en Receptores Discretos para Cd.**

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Cadmio (Cd) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Porcentaje de la Norma de**<br>**Calidad** | **Porcentaje de la Norma de**<br>**Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este**<br>**(m)** | **Norte**<br>**(m)** | **24 horas** | **Periodo**<br>**Anual** | **24 horas** | **Periodo**<br>**Anual** | **24 horas** | **Periodo**<br>**Anual** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 6,9E-07 | 6,6E-08 | 0,025 | 0,005 | 0% | 0% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 5,4E-07 | 1,0E-08 | 1,0E-08 | 1,0E-08 | 0% | 0% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 3,1E-07 | 7,3E-09 | 7,3E-09 | 7,3E-09 | 0% | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 4,1E-08 | 1,1E-09 | 1,1E-09 | 1,1E-09 | 0% | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 1,2E-08 | 5,0E-10 | 5,0E-10 | 5,0E-10 | 0% | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 4,2E-09 | 2,6E-10 | 2,6E-10 | 2,6E-10 | 0% | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 5,0E-08 | 3,7E-09 | 3,7E-09 | 3,7E-09 | 0% | 0% |

**Tabla 25: - Resultados Aporte Modelo en Receptores Discretos para Hg.**

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Mercurio (Hg) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Porcentaje de la Norma de**<br>**Calidad** | **Porcentaje de la Norma de**<br>**Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este**<br>**(m)** | **Norte**<br>**(m)** | **24 horas** | **Periodo**<br>**Anual** | **24 horas** | **Periodo**<br>**Anual** | **24 horas** | **Periodo**<br>**Anual** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 8,6E-08 | 8,4E-09 | 4 | 1 | 0% | 0% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 6,5E-08 | 1,2E-09 | 1,2E-09 | 1,2E-09 | 0% | 0% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 3,9E-08 | 8,3E-10 | 8,3E-10 | 8,3E-10 | 0% | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 4,8E-09 | 1,3E-10 | 1,3E-10 | 1,3E-10 | 0% | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 1,5E-09 | 5,7E-11 | 5,7E-11 | 5,7E-11 | 0% | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 4,8E-10 | 2,9E-11 | 2,9E-11 | 2,9E-11 | 0% | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 5,7E-09 | 4,3E-10 | 4,3E-10 | 4,3E-10 | 0% | 0% |

**Tabla 26: - Resultados Aporte Modelo en Receptores Discretos para Ni.**

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Niquel (Ni) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Porcentaje de la Norma de**<br>**Calidad** | **Porcentaje de la Norma de**<br>**Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este**<br>**(m)** | **Norte**<br>**(m)** | **24 horas** | **Periodo**<br>**Anual** | **24 horas** | **Periodo**<br>**Anual** | **24 horas** | **Periodo**<br>**Anual** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 8,1E-06 | 7,8E-07 | 0,1 | 0,02 | 0% | 0% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 6,4E-06 | 1,2E-07 | 1,2E-07 | 1,2E-07 | 0% | 0% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 3,6E-06 | 8,7E-08 | 8,7E-08 | 8,7E-08 | 0% | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 4,9E-07 | 1,4E-08 | 1,4E-08 | 1,4E-08 | 0% | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 1,5E-07 | 6,0E-09 | 6,0E-09 | 6,0E-09 | 0% | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 5,0E-08 | 3,1E-09 | 3,1E-09 | 3,1E-09 | 0% | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 6,0E-07 | 4,4E-08 | 4,4E-08 | 4,4E-08 | 0% | 0% |

**Tabla 27: - Resultados Aporte Modelo en Receptores Discretos para Pb.**

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Plomo (Pb) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Porcentaje de la Norma de**<br>**Calidad** | **Porcentaje de la Norma de**<br>**Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este**<br>**(m)** | **Norte**<br>**(m)** | **24 horas** | **Periodo**<br>**Anual** | **24 horas** | **Periodo**<br>**Anual** | **24 horas** | **Periodo**<br>**Anual** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 2,5E-05 | 2,4E-06 | 4 | 0,5 | 0% | 0% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 2,0E-05 | 3,8E-07 | 3,8E-07 | 3,8E-07 | 0% | 0% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 1,1E-05 | 2,7E-07 | 2,7E-07 | 2,7E-07 | 0% | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 1,5E-06 | 4,3E-08 | 4,3E-08 | 4,3E-08 | 0% | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 4,6E-07 | 1,9E-08 | 1,9E-08 | 1,9E-08 | 0% | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 1,6E-07 | 9,6E-09 | 9,6E-09 | 9,6E-09 | 0% | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 1,9E-06 | 1,4E-07 | 1,4E-07 | 1,4E-07 | 0% | 0% |

**Tabla 28: - Resultados Aporte Modelo en Receptores Discretos para V.**

| ID<br>Receptor | Descripción | Coordenadas de Ubicación<br>(Datum WGS84) | Col4 | Vanadio (V) | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto** | **Concentración**<br>**(μg/m3) - Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **24 horas** | **24 horas** | **24 horas** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 1,2E-04 | 2 | 0% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 9,5E-05 | 9,5E-05 | 0% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 5,6E-05 | 5,6E-05 | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 7,1E-06 | 7,1E-06 | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 2,2E-06 | 2,2E-06 | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 7,1E-07 | 7,1E-07 | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 8,6E-06 | 8,6E-06 | 0% |

**Tabla 29: - Resultados Aporte Modelo en Receptores Discretos para Se.**

| ID<br>Receptor | Descripción | Coordenadas de Ubicación<br>(Datum WGS84) | Col4 | Selenio (Se) | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto** | **Concentración**<br>**(μg/m3) - Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **24 horas** | **24 horas** | **24 horas** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 1,7E-07 | 10 | 0% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 1,3E-07 | 1,3E-07 | 0% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 7,8E-08 | 7,8E-08 | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 1,0E-08 | 1,0E-08 | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 3,1E-09 | 3,1E-09 | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 1,0E-09 | 1,0E-09 | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 1,2E-08 | 1,2E-08 | 0% |

**Tabla 30: - Resultados Aporte Modelo en Receptores Discretos para As.**

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Arsénico (As) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Concentración (μg/m3) -**<br>**Norma de Calidad** | **Porcentaje de la Norma de**<br>**Calidad** | **Porcentaje de la Norma de**<br>**Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este**<br>**(m)** | **Norte**<br>**(m)** | **24 horas** | **Periodo**<br>**Anual** | **24 horas** | **Periodo**<br>**Anual** | **24 horas** | **Periodo**<br>**Anual** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 2,0E-05 | 1,9E-06 | 0,3 | 0,006 | 0% | 0% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 1,6E-05 | 3,0E-07 | 3,0E-07 | 3,0E-07 | 0% | 0% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 8,8E-06 | 2,2E-07 | 2,2E-07 | 2,2E-07 | 0% | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 1,2E-06 | 3,4E-08 | 3,4E-08 | 3,4E-08 | 0% | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 3,6E-07 | 1,5E-08 | 1,5E-08 | 1,5E-08 | 0% | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 1,2E-07 | 7,7E-09 | 7,7E-09 | 7,7E-09 | 0% | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 1,5E-06 | 1,1E-07 | 1,1E-07 | 1,1E-07 | 0% | 0% |

**Tabla 31: - Resultados Aporte Modelo en Receptores Discretos para Sb.**

| ID<br>Receptor | Descripción | Coordenadas de Ubicación<br>(Datum WGS84) | Col4 | Antimonio (Sb) | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Concentración**<br>**(μg/m3) - Aporte del**<br>**Proyecto** | **Concentración**<br>**(μg/m3) - Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Periodo Anual** | **Periodo Anual** | **Periodo Anual** |
| RP1 | Receptor 1 | 269.798 | 6.367.679 | 1,2E-05 | 25 | 0% |
| RP2 | Receptor 2 | 271.540 | 6.368.241 | 8,2E-06 | 8,2E-06 | 0% |
| RP3 | Receptor 3 | 269.132 | 6.369.438 | 5,4E-06 | 5,4E-06 | 0% |
| RP4 | Receptor 4 | 267.975 | 6.369.581 | 5,6E-07 | 5,6E-07 | 0% |
| RP5 | Receptor 5 | 267.311 | 6.370.101 | 1,8E-07 | 1,8E-07 | 0% |
| RP6 | Receptor 6 | 266.580 | 6.371.009 | 5,2E-08 | 5,2E-08 | 0% |
| RP7 | Estación Valle Alegre (SINCA) | 271.889 | 6.367.413 | 6,8E-07 | 6,8E-07 | 0% |
