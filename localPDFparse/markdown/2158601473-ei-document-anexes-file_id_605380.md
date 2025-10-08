---
title: Evaluación DS146
author: Jorge Pulgar
date: D:20230206111211-03'00'
language: es
type: report
pages: 52
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - DECLARACIÓN DE IMPACTO AMBIENTAL PROYECTO “Autorización Zonas de Acopio Transitorio de Mercancías Peligrosas”
-->

# DECLARACIÓN DE IMPACTO AMBIENTAL PROYECTO “Autorización Zonas de Acopio Transitorio de Mercancías Peligrosas”

## ANEXO 3.3. ESTUDIO DE MODELACIÓN ATMOSFÉRICA DE LA CALIDAD DEL AIRE

**Febrero 2023**

**Sustentable S.A.**
Asesoría y Gestión Ambiental

www.sustentable.cl

**ÍNDICE** **DE** **CONTENIDOS**

1. MODELACIÓN DE LA DISPERSIÓN DE LAS EMISIONES .................................................................. 1

1.1. I NTRODUCCIÓN 1

1.2. O BJETIVO 2

1.3. A NTECEDENTES G ENERALES DEL P ROYECTO 2

1.3.1. D ESCRIPCIÓN B REVE DEL P ROYECTO ........................................................................................................ 2

1.3.2. L OCALIZACIÓN .......................................................................................................................................... 3

2. METEOROLOGÍA WRF MODELADA DE LA ZONA DE ESTUDIO ....................................................... 4

2.1. A NÁLISIS D ESCRIPTIVO V ELOCIDAD Y D IRECCIÓN DEL V IENTO P UNTO N°1: Z ONA S ÓLIDO 6

2.1.1. S ERIES DE T IEMPO ................................................................................................................................... 6

2.2. A NÁLISIS D ESCRIPTIVO V ELOCIDAD Y D IRECCIÓN DEL V IENTO P UNTO N°2: Z ONA IMO 1 L ÍQUIDO 11

2.2.1. S ERIES DE T IEMPO ................................................................................................................................. 11

2.3. A NÁLISIS D ESCRIPTIVO V ELOCIDAD Y D IRECCIÓN DEL V IENTO P UNTO N°3: Z ONA IMO 2 L ÍQUIDO 16

2.3.1. S ERIES DE T IEMPO ................................................................................................................................. 16

2.4. A NÁLISIS D ESCRIPTIVO V ELOCIDAD Y D IRECCIÓN DEL V IENTO P UNTO N°4: Z ONA DE S EGURIDAD CON C ÁMARA DE

C ONTENCIÓN 21

2.4.1. S ERIES DE T IEMPO ................................................................................................................................. 21

2.5. A NÁLISIS G LOBAL DE LA V ELOCIDAD Y D IRECCIÓN DEL V IENTO 26

3. MODELACIÓN DE LA DISPERSIÓN .................................................................................................. 31

3.2. B ASE T EÓRICA DEL M ODELO DE D ISPERSIÓN A TMOSFÉRICA S ISTEMA WRF-C ALPUFF 31

3.2.1. M ODELO A TMOSFÉRICO WRF ................................................................................................................. 31

3.2.2. M ODELO DE D ISPERSIÓN CALPUFF ....................................................................................................... 31

3.3. V ARIABLES DE E NTRADA I NGRESADAS A LA M ODELACIÓN 32

3.3.1. E MISIONES Y F UENTES C ONSIDERADAS EN EL E SCENARIO M ODELADO ..................................................... 32
3.3.2. T OPOGRAFÍA DEL Á REA DE M ODELACIÓN ................................................................................................. 33

3.4. R ESULTADOS DE LA M ODELACIÓN 35

3.4.1. P LUMA D ISPERSIÓN Z ONA IMO S OLIDOS ................................................................................................. 35

3.4.2. P LUMA D ISPERSIÓN Z ONA IMO 1 L ÍQUIDOS ............................................................................................. 38

3.4.3. P LUMA D ISPERSIÓN Z ONA IMO 2 L ÍQUIDOS ............................................................................................. 41

3.4.4. P LUMA D ISPERSIÓN Z ONA P ISCINA C ONTENCIÓN ..................................................................................... 44

4. CONCLUSIONES ............................................................................................................................... 48

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** i

**ÍNDICE** **DE** **TABLAS**

T ABLA 1. C OORDENADAS VÉRTICES DEL ÁREA DE MODELACIÓN DEL P ROYECTO .................................................................. 4

T ABLA 2. L OCALIZACIÓN DE REFERENCIA Y VARIABLES METEOROLÓGICAS MODELADAS ....................................................... 5

**ÍNDICE** **DE** **FIGURAS**

F IGURA 1. D IVISIÓN P OLÍTICO -A DMINISTRATIVA EN QUE SE INSERTA EL P ROYECTO ............................................................. 3

F IGURA 2. P UNTOS ANALIZADOS ........................................................................................................................................ 5

F IGURA 3. S ERIE DE TIEMPO MODELADA DE VELOCIDAD Y DIRECCIÓN DEL VIENTO - Z ONA S ÓLIDO P ERIODO 01 ENERO - 31

DICIEMBRE 2021 ............................................................................................................................................................... 6

F IGURA 4. V ARIABILIDAD TEMPORAL DEL VIENTO MODELADO - Z ONA S ÓLIDO ...................................................................... 8

F IGURA 5. C ICLO ESTACIONAL DEL VIENTO MODELADO - Z ONA S ÓLIDO P ERIODO 01 ENERO - 31 DICIEMBRE 2021 .............. 9

F IGURA 6. C ICLO DIARIO DE LA VELOCIDAD DEL VIENTO MODELADA - Z ONA S ÓLIDO P ERIODO 01 ENERO - 31 DICIEMBRE 2021

...................................................................................................................................................................................... 10

F IGURA 7. S ERIE DE TIEMPO MODELADA DE VELOCIDAD Y DIRECCIÓN DEL VIENTO - Z ONA IMO 1 LÍQUIDO P ERIODO 01 ENERO

- 31 DICIEMBRE 2021 ..................................................................................................................................................... 11

F IGURA 8. V ARIABILIDAD TEMPORAL DEL VIENTO MODELADO - Z ONA IMO 1 LÍQUIDO ......................................................... 13

F IGURA 9. C ICLO ESTACIONAL DEL VIENTO MODELADO - Z ONA IMO 1 LÍQUIDO P ERIODO 01 ENERO - 31 DICIEMBRE 2021 . 14

F IGURA 10. C ICLO DIARIO DE LA VELOCIDAD DEL VIENTO MODELADA - Z ONA S ÓLIDO P ERIODO 01 ENERO - 31 DICIEMBRE 2021

...................................................................................................................................................................................... 15

F IGURA 11. S ERIE DE TIEMPO MODELADA DE VELOCIDAD Y DIRECCIÓN DEL VIENTO - Z ONA IMO 2 LÍQUIDO P ERIODO 01 ENERO

- 31 DICIEMBRE 2021 ..................................................................................................................................................... 16

F IGURA 12. V ARIABILIDAD TEMPORAL DEL VIENTO MODELADO - Z ONA IMO 2 LÍQUIDO ....................................................... 18

F IGURA 13. C ICLO ESTACIONAL DEL VIENTO MODELADO - Z ONA IMO 2 LÍQUIDO P ERIODO 01 ENERO - 31 DICIEMBRE 2021 19

F IGURA 14. C ICLO DIARIO DE LA VELOCIDAD DEL VIENTO MODELADA - Z ONA S ÓLIDO P ERIODO 01 ENERO - 31 DICIEMBRE 2021

...................................................................................................................................................................................... 20

F IGURA 15. S ERIE DE TIEMPO MODELADA DE VELOCIDAD Y DIRECCIÓN DEL VIENTO - Z ONA DE S EGURIDAD CON C ÁMARA DE

C ONTENCIÓN - P ERIODO 01 ENERO - 31 DICIEMBRE 2021 ............................................................................................... 21

F IGURA 16. V ARIABILIDAD TEMPORAL DEL VIENTO MODELADO - Z ONA DE S EGURIDAD CON C ÁMARA DE C ONTENCIÓN ........ 23

F IGURA 17. C ICLO ESTACIONAL DEL VIENTO MODELADO - Z ONA DE S EGURIDAD CON C ÁMARA DE C ONTENCIÓN P ERIODO 01

ENERO - 31 DICIEMBRE 2021 .......................................................................................................................................... 24

F IGURA 18. C ICLO DIARIO DE LA VELOCIDAD DEL VIENTO MODELADA - Z ONA DE S EGURIDAD CON C ÁMARA DE C ONTENCIÓN

P ERIODO 01 ENERO - 31 DICIEMBRE 2021 ...................................................................................................................... 25

F IGURA 19. V ARIABILIDAD DE LA VELOCIDAD Y DIRECCIÓN DEL VIENTO PERIODO DIURNO P ERIODO 01 ENERO - 31 DICIEMBRE

2021 .............................................................................................................................................................................. 27

F IGURA 20. V ARIABILIDAD DE LA VELOCIDAD Y DIRECCIÓN DEL VIENTO PERIODO NOCTURNO P ERIODO 01 ENERO - 31

DICIEMBRE 2021 ............................................................................................................................................................. 29

F IGURA 21. L OCALIZACIÓN DE LAS Z ONAS CONSIDERADAS COMO F UENTES DE E MISIÓN .................................................... 32

F IGURA 22. T OPOGRAFÍA DEL ÁREA DE MODELACIÓN ....................................................................................................... 34

F IGURA 23. P LUMA DISPERSIÓN P ROMEDIO A NUAL Z ONA IMO S OLIDOS ........................................................................... 35

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** ii

F IGURA 24. P LUMA DISPERSIÓN P ROMEDIO M ENSUAL Z ONA IMO S ÓLIDOS P ERIODO E NERO - J UNIO 2021 ...................... 36

F IGURA 25. P LUMA DISPERSIÓN P ROMEDIO M ENSUAL Z ONA IMO S ÓLIDOS . P ERIODO J ULIO - D ICIEMBRE 2021 ................ 37

F IGURA 26. P LUMA DISPERSIÓN P ROMEDIO A NUAL Z ONA IMO 1 L ÍQUIDOS ....................................................................... 38

F IGURA 27. P LUMA DISPERSIÓN P ROMEDIO M ENSUAL Z ONA IMO 1 L ÍQUIDOS P ERIODO E NERO - J UNIO 2021 ................... 39

F IGURA 28. P LUMA DISPERSIÓN P ROMEDIO M ENSUAL Z ONA IMO 1 L ÍQUIDOS P ERIODO J ULIO - D ICIEMBRE 2021 ............. 40

F IGURA 29. P LUMA DISPERSIÓN P ROMEDIO A NUAL Z ONA IMO 2 L ÍQUIDOS ....................................................................... 41

F IGURA 30. P LUMA DISPERSIÓN P ROMEDIO M ENSUAL Z ONA IMO 2 L ÍQUIDOS P ERIODO E NERO - J UNIO 2021 ................... 42

F IGURA 31. P LUMA DISPERSIÓN P ROMEDIO M ENSUAL Z ONA IMO 2 L ÍQUIDOS P ERIODO J ULIO - D ICIEMBRE 2021 ............. 43

F IGURA 32. P LUMA DISPERSIÓN P ROMEDIO A NUAL Z ONA P ISCINA C ONTENCIÓN ............................................................... 44

F IGURA 33. P LUMA DISPERSIÓN P ROMEDIO M ENSUAL Z ONA P ISCINA C ONTENCIÓN P ERIODO E NERO - J UNIO 2021 .......... 45

F IGURA 34. P LUMA DISPERSIÓN P ROMEDIO M ENSUAL Z ONA P ISCINA C ONTENCIÓN P ERIODO J ULIO - D ICIEMBRE 2021 ..... 46

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** iii

**1.** **MODELACIÓN DE LA DISPERSIÓN DE LAS EMISIONES**

**1.1.** **Introducción**

El objetivo de este informe es mostrar la representación de un modelo que permita evaluar la dispersión de la pluma
toxica en caso de una emergencia como incendio y/o derrame, considerando las condiciones meteorológicas
prevalentes de la zona de emplazamiento de los sitios donde se almacenan las sustancias clasificadas como IMO [1]
sólidas y líquidas que desembarcan en San Antonio Terminal Internacional S.A. (STI), en adelante el proyecto.

Para la modelación de dispersión se consideró la utilización del modelo Calpuff el cual fue alimentado por las variables
meteorológicas obtenidas por medio del modelo meteorológico de pronóstico Weather Research and Forecasting
Model (WRF) para el año 2021, con todos los parámetros indicados en la “Guía para el Uso de Modelos de Calidad
del Aire en el SEIA, 2012”. Además la modelación de dispersión Calpuff se realizó con todos los requerimientos de la
“Guía para el Uso de Modelos de Calidad del Aire en el SEIA, 2012” del Servicio de Evaluación Ambiental. Esta Guía
indica como opción la aplicación del sistema de modelación atmosférica “WRF - CALPUFF”, sistema de modelación
que a su vez está definido por la agencia EPA como sistema de referencia para simular la dispersión de contaminantes
provenientes de centros industriales ubicados en terreno complejo.

Los sitios considerados en la modelación como fuentes de emisión corresponden a Zona IMO líquidos, Zona IMO
solidos (superficie de 1.600 m [2] ) y el área de Seguridad de la Piscina de contención.

1 Las mercancías peligrosas o mercancías IMO (International Maritime Organization) son aquellas que por sus propiedades y
características, representan un riesgo para la seguridad y la salud de las personas.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 1

**1.2.** **Objetivo**

Por medio de una modelación matemática evaluar la dispersión de la pluma toxica en caso de una emergencia como
incendio y/o derrame, considerando las condiciones meteorológicas prevalentes de la zona de emplazamiento de los
sitios donde se almacenan las sustancias IMO sólidas y líquidas que desembarcan en San Antonio Terminal
Internacional S.A. (STI).

**1.3.** **Antecedentes Generales del Proyecto**

**1.3.1.** **Descripción Breve del Proyecto**

San Antonio Terminal Internacional S.A. (STI) opera desde hace 20 años en las instalaciones de la Empresa Portuaria
de San Antonio S.A. (EPSA), a través de una concesión, prestando servicios integrales de logística portuaria a líneas
navieras, empresas importadores y exportadores, transportistas y a todos los usuarios directos e indirectos del terminal,
incorporando permanentemente tecnología e innovando en las operaciones y procesos.

STI tiene considerado desarrollar el proyecto denominado **“Autorización Zonas de Acopio Transitorio de**
**Mercancías Peligrosas”** en adelante, el “Proyecto”, el cual tiene como objetivo redistribuir y ordenar las mercancías
peligrosas (MERPEL) o también denominadas cargas IMO de acuerdo a la clasificación de la Gobernación Marítimo
Internacional (IMO en sus siglas en inglés) y la construcción de un área de seguridad para la contención de un posible
derrame de cargas IMO.

Es preciso señalar que el ingreso de la presente DIA da respuesta a la solicitado por la Armada de Chile a través del
Ordinario 12000/787 que autoriza el Mantenimiento Temporal de Mercancías Peligrosas en San Antonio Terminal
Internacional (STI).

Para la obtención de la Autorización de la Armada y como parte de esta DIA sometida a evaluación ambiental, se
realizará la redistribución de las cargas IMO y la construcción de un (1) área de seguridad, la cual cuenta con una (1)
piscina de contención y desconsolidación.

De esta manera el Proyecto contempla la autorización de una (1) zona de almacenamiento de contenedores
clasificados como mercancías peligrosas sólidas (IMO sólido), en la zona denominada B3 y dos (2) zonas de
almacenamiento y de contenedores clasificados como mercancías peligrosas líquidas (IMO líquido) en las zonas
denominadas J2 y J3.

Además, de un área de seguridad para el control de derrames y desconsolidación de cargas IMO, zona en la que se
proyectan obras de seguridad destinadas a la captación, conducción y almacenamiento temporal de derrames con el
objetivo de evitar que éstos lleguen al mar, que se encuentra a un costado del Molo Sur.

Según información entregada por STI para los últimos 5 años, se visualiza que agosto del año 2018, fue el momento
en que se recibió la mayor cantidad de contenedores con cargas IMO, por lo que se tomó este periodo para analizar
las cantidades de cargas IMO a almacenar y así diseñar la redistribución y el área de seguridad (piscina de contención
y desconsolidación).

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 2

**1.3.2.** **Localización**

La ubicación político - administrativa del Proyecto es la siguiente:

**Región:** Valparaíso

**Provincia:** San Antonio

**Comuna:** San Antonio

El Proyecto se emplaza en las instalaciones de la Empresa Portuaria San Antonio Terminal Internacional S.A, ubicada
en la comuna de San Antonio, Provincia de San Antonio, Región de Valparaíso y su zonificación según el PRC de San
Antonio corresponde a la Zona ZP clasificada como Zona Portuaria.

**Figura 1. División Político-Administrativa en que se inserta el Proyecto**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 3

**2.** **METEOROLOGÍA WRF MODELADA DE LA ZONA DE ESTUDIO**

La modelación atmosférica predice el estado del tiempo resolviendo mediante métodos numéricos las ecuaciones
matemáticas para la física y la dinámica de la atmósfera a partir de condiciones previas. De esta manera, mediante el
modelo meteorológico de pronóstico Weather Research and Forecasting Model (WRF) se han modelado y analizado
las variables meteorológicas de mayor incidencia en la dispersión de las emisiones generadas por el Proyecto.

El modelo WRF es un modelo de predicción numérica del tiempo diseñado para la investigación y para aplicaciones
operativas. Diversas instituciones han contribuido y siguen contribuyendo a su desarrollo, con el firme objetivo de
construir el modelo de pronóstico numérico de mesoescala de la siguiente generación, para lograr un avance en el
entendimiento de los procesos atmosféricos y en la predicción de tiempo. Los principales componentes de este modelo
son las fuentes externas de datos, como son los datos de entrada y la información geográfica, el sistema de preprocesamiento, el modelo WRF-ARW y los sistemas de post-procesamiento.

Las fuentes externas de datos contienen información necesaria para inicializar WRF. Éstos corresponden a las
observaciones convencionales o satélites de la atmósfera. De estos datos se obtienen las condiciones iniciales y de
borde para las simulaciones del WRF. También es necesario entregarle datos sobre el terreno que contengan
información sobre la orografía, uso de suelo, relieve y vegetación, entre otros.

Este modelo se encuentra recomendado por la “Guía para el uso de modelos de calidad del aire en el SEIA”, para la
generación de datos meteorológicos, ya que, según indica, es uno de los modelos meteorológicos de pronóstico más
avanzados y completos, siendo empleado en la mayoría de los proyectos relacionados con modelación atmosférica
encargados por organismos estatales como el Ministerio del Medio Ambiente (MMA) y la ex Comisión Nacional de
Energía (CNE) (ahora Ministerio de Energía).

Para generar la modelación meteorológica, se utilizan cuatro dominios anidados, donde cada celda es de 27, 9, 3 y 1
kilómetros respectivamente, centrados en el Proyecto para un año calendario (2021) y resolución horaria.

En la siguiente tabla se muestran las coordenadas de los vértices del área de modelación WRF.

**Tabla 1. Coordenadas vértices del área de modelación del Proyecto**

|Vértice|Coordenadas UTM (Datum WGS-84 Huso 19S)|Col3|
|---|---|---|
|**Vértice**|**Norte (m)**|**Este (m)**|
|Noreste|6315709,45|291787,06|
|Noroeste|6313951,02|778456,13|
|Suroeste|6242119,63|776110,17|
|Sureste|6243891,15|293607,52|

Fuente: Elaboración propia.

Dado que es la meteorología la que media entre las emisiones y su impacto en los puntos receptores, se realiza a
continuación un análisis cualitativo y cuantitativo de la velocidad y dirección del viento modelada, en los puntos centro
de cada zona de almacenamiento IMO. En la siguiente tabla se exponen las coordenadas de los puntos de cada área

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 4

considerados para extraer la información meteorológica del modelo para su análisis descriptivo que a continuación se

desarrolla.

**Tabla 2. Localización de referencia y variables meteorológicas modeladas**

|ID|Punto modelado|Coordenadas UTM|Col4|Variables|Periodo|
|---|---|---|---|---|---|
|**ID**|**Punto modelado**|**Norte (m)**|**Este (m)**|**Este (m)**|**Este (m)**|
|1|Zona sólidos|256.619|6.280.275|Velocidad del viento<br>Dirección del viento|01 de enero al 31 de<br>diciembre 2021|
|2|Zona IMO 1 Líquido|256.620|6.279.900|6.279.900|6.279.900|
|3|Zona IMO 2 Líquido|256.640|6.279.846|6.279.846|6.279.846|
|4|Zona Piscina<br>Contenedora|256.539|6.280.517|6.280.517|6.280.517|

Fuente: Elaboración propia.

A continuación, en la Figura 2 se presenta la ubicación espacial de los puntos analizados

**Figura 2. Puntos analizados**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 5

**2.1.** **Análisis Descriptivo Velocidad y Dirección del Viento Punto N°1: Zona Sólido**

**2.1.1.** **Series de Tiempo**

La serie temporal de la velocidad del viento modelada muestra un leve ciclo anual, con las mayores velocidades
registradas entre septiembre y diciembre, alcanzando valores que superan 8 m/s. En términos generales las
velocidades varían en promedio entre 2 y 6 m/s.

Con respecto a la dirección del viento se observan que, la mayor frecuencia de vientos corresponde al tercer cuadrante,
es decir, vientos desde el Sur (S), Sur Suroeste (SSO), Suroeste (SO), Oeste Suroeste (OSO), Oeste (O),
correspondiendo a los datos centrados entre 180° y 300°.

|Col1|Figura 3. Serie de tiempo modelada de velocidad y dirección del viento - Zona Sólido Periodo 01 enero - 31 diciembre 2021|
|---|---|
|**VELOCIDAD**||
|**DIRECCIÓN**||

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 6

**2.1.1.1.** **Rosas de Viento**

A continuación, se muestran los campos de viento anual y para diferentes periodos del día, los que muestran la
variabilidad temporal del viento modelado entre el primero de enero al 31 de diciembre del 2021 en el punto Zona
Sólidos, indicando los porcentajes de frecuencia que el viento sopla en sus diferentes direcciones.

A partir del comportamiento desde las 00:00 a 23:00 horas, los registros muestran que la dirección de máxima
frecuencia corresponde a vientos procedentes desde muchas direcciones, principalmente desde el tercer cuadrante,
es decir, vientos desde el Sur (S), Sur Suroeste (SSO), Suroeste (SO), Oeste Suroeste (OSO), Oeste (O), explicando
en conjunto un 60% de la frecuencia total.

Al observar el comportamiento espacial de los vientos en los diferentes periodos del día, Figura 4, se puede apreciar
que en términos generales no existe un patrón dominante en la procedencia del viento, ya que este llega de todas las
direcciones a lo largo de todo el día. Se observa un leve patrón entre el ciclo diurno y nocturno, con vientos desde el
Este y sus variaciones durante la noche y vientos desde el Oeste y sus variaciones durante el día. Entre las 12:00 y
17:00 horas se observa un leve patrón más marcado con vientos desde el suroeste (SO) y Oeste Suroeste (OSO) sin
embargo, se registran vientos en menor medida desde el Oeste (O), Oeste Noroeste (ONO) y Noroeste (NO).

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 7

**Figura 4. Variabilidad temporal del viento modelado - Zona Sólido**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 8

**2.1.1.2.** **Ciclo Estacional**

La Figura 5 muestra la evolución estacional y diaria de la velocidad y dirección del viento modelado en el punto Zona
Sólidos, presentando en el eje “x” las horas del día y en el eje “y” los meses del año. Es posible identificar un leve ciclo
anual, con las máximas velocidades centradas los meses desde septiembre a octubre llegando a 6 m/s. Para el periodo
nocturno las velocidades se mantienen relativamente homogéneas a lo largo del año con velocidades que se

mantienen alrededor de 2 m/s.

En cuanto a la dirección del viento, se observa para el periodo nocturno vientos desde todas las direcciones, mientras
que, en horas del día, principalmente entre 11:00 y 17:00 horas el viento proviene desde el Oeste (O), Suroeste (SO)
y Noroeste (NO).

**Figura 5. Ciclo estacional del viento modelado - Zona Sólido**

**Periodo 01 enero - 31 diciembre 2021**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 9

**2.1.1.3.** **Ciclo Diario de Velocidad del Viento**

En la siguiente figura se presentan los ciclos diarios promedio de la velocidad y dirección del viento modelado en el
punto Zona Sólidos. Al apreciar la curva de velocidad promedio, se puede observar los valores mínimos se presentan
en el periodo nocturno con magnitudes que se mantienen relativamente constantes entre las 00:00 y 07:00 horas,
momento en que la velocidad comienza a aumentar levemente hasta alcanzar el máximo diario a las 14:00 horas con
una magnitud promedio de 4,0 m/s.

Respecto al ciclo diario de dirección del viento se puede observar que, durante toda la noche no existe una frecuencia
de vientos dominantes, ya que estos provienen desde cualquier dirección, sin embargo, entre las 11:00 y 18:00 horas
existe predominancia de vientos desde el Sur Suroeste (SSO), suroeste (SO) y Oeste Suroeste (OSO) llegando a
explicar el 30% de la frecuencia total.

**Figura 6. Ciclo diario de la velocidad del viento modelada - Zona Sólido**

**Periodo 01 enero - 31 diciembre 2021**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 10

**2.2.** **Análisis Descriptivo Velocidad y Dirección del Viento Punto N°2: Zona IMO 1 Líquido**

**2.2.1.** **Series de Tiempo**

La serie temporal de la velocidad del viento modelada en el punto de control Zona IMO 1 Líquido muestra el mismo
comportamiento descrito anteriormente, con un leve ciclo anual, con las mayores velocidades registradas entre
septiembre y diciembre, alcanzando valores que superan 8 m/s. En términos generales las velocidades varían en
promedio entre 2 y 6 m/s.

Con respecto a la dirección del viento se observan que, la mayor frecuencia de vientos corresponde al tercer cuadrante,
es decir, vientos desde el Sur (S), Sur Suroeste (SSO), Suroeste (SO), Oeste Suroeste (OSO), Oeste (O),
correspondiendo a los datos centrados entre 180° y 300°.

**Figura 7. Serie de tiempo modelada de velocidad y dirección del viento - Zona IMO 1 líquido**

|Col1|Periodo 01 enero - 31 diciembre 2021|
|---|---|
|**VELOCIDAD**||
|**DIRECCIÓN**||

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 11

**2.2.1.1.** **Rosas de Viento**

A continuación, se muestran los campos de viento anual y para diferentes periodos del día, los que muestran la
variabilidad temporal del viento modelado durante el periodo entre enero y diciembre de 2021 en el punto Zona IMO 1
líquidos, indicando los porcentajes de frecuencia que el viento sopla en sus diferentes direcciones. Cabe señalar que
el comportamiento es coincidente con el descrito anteriormente en el punto Zona Sólidos.

A partir del comportamiento desde las 00:00 a 23:00 horas, los registros muestran que la dirección de máxima
frecuencia corresponde a vientos procedentes desde muchas direcciones, principalmente desde el tercer cuadrante,
es decir, vientos desde el Sur (S), Sur Suroeste (SSO), Suroeste (SO), Oeste Suroeste (OSO), Oeste (O), explicando
en conjunto un 60% de la frecuencia total.

Al observar el comportamiento espacial de los vientos en los diferentes periodos del día, Figura 8, se puede apreciar
que en términos generales no existe un patrón dominante en la procedencia del viento, ya que este llega de todas las
direcciones a lo largo de todo el día. Se observa un leve patrón entre el ciclo diurno y nocturno, con vientos desde el
Este y sus variaciones durante la noche y vientos desde el Oeste y sus variaciones durante el día. Entre las 12:00 y
17:00 horas se observa un leve patrón más marcado con vientos desde el suroeste (SO) y Oeste Suroeste (OSO), sin
embargo, se registran vientos en menor medida desde el Oeste (O), Oeste Noroeste (ONO) y Noroeste (NO).

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 12

**Figura 8. Variabilidad temporal del viento modelado - Zona IMO 1 líquido**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 13

**2.2.1.2.** **Ciclo Estacional**

La Figura 9 muestra la evolución estacional y diaria de la velocidad y dirección del viento modelado en el punto Zona
IMO 1 Líquido, presentando en el eje “x” las horas del día y en el eje “y” los meses del año. Es posible identificar un
leve ciclo anual, con las máximas velocidades centradas los meses desde agosto a octubre llegando a 6 m/s. Para el
periodo nocturno las velocidades se mantienen relativamente homogéneas a lo largo del año con velocidades que se

mantienen alrededor de 2 m/s.

En cuanto a la dirección del viento, se observa para el periodo nocturno vientos desde todas las direcciones, mientras
que, en horas del día, principalmente entre 11:00 y 17:00 horas el viento proviene desde el Oeste (O), Suroeste (SO)
y Noroeste (NO).

**Figura 9. Ciclo estacional del viento modelado - Zona IMO 1 líquido**

**Periodo 01 enero - 31 diciembre 2021**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 14

**2.2.1.3.** **Ciclo Diario de Velocidad del Viento**

En la siguiente figura se presentan los ciclos diarios promedio de la velocidad y dirección del viento modelado en el
punto Zona IMO 1 Líquido. Al apreciar la curva de velocidad promedio, se puede observar los valores mínimos se
presentan en el periodo nocturno con magnitudes que se mantienen relativamente constantes entre las 00:00 y 07:00
horas, momento en que la velocidad comienza a aumentar levemente hasta alcanzar el máximo diario a las 14:00
horas con una magnitud promedio de 4,0 m/s.

Respecto al ciclo diario de dirección del viento se puede observar que, durante toda la noche no existe una frecuencia
de vientos dominantes, ya que estos provienen desde cualquier dirección, sin embargo, entre las 11:00 y 18:00 horas
existe predominancia de vientos desde el Sur Suroeste (SSO), suroeste (SO) y Oeste Suroeste (OSO) llegando a
explicar el 30% de la frecuencia total.

**Figura 10. Ciclo diario de la velocidad del viento modelada - Zona Sólido**

**Periodo 01 enero - 31 diciembre 2021**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 15

**2.3.** **Análisis Descriptivo Velocidad y Dirección del Viento Punto N°3: Zona IMO 2 Líquido**

**2.3.1.** **Series de Tiempo**

La serie temporal de la velocidad del viento modelada en el punto de control Zona IMO 2 Líquido no muestra un ciclo
anual aparente, ya que las velocidades presentan un comportamiento similar a lo largo de todo el año, observando un
leve aumento entre octubre y diciembre alcanzando valores que superan 8 m/s. En términos generales las velocidades
varían en promedio entre 2 y 4 m/s.

Con respecto a la dirección del viento no se observa ningún patrón anual, ya que las direcciones varían entre los 120
y 360° a lo largo del año, es decir, se observan vientos desde todas direcciones.

**Figura 11. Serie de tiempo modelada de velocidad y dirección del viento - Zona IMO 2 líquido**

|Col1|Periodo 01 enero - 31 diciembre 2021|
|---|---|
|**VELOCIDAD**||
|**DIRECCIÓN**||

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 16

**2.3.1.1.** **Rosas de Viento**

A continuación, se muestran los campos de viento anual y para diferentes periodos del día, los que muestran la
variabilidad temporal del viento modelado durante el periodo entre enero y diciembre de 2021 en el punto Zona IMO 2
líquidos, indicando los porcentajes de frecuencia que el viento sopla en sus diferentes direcciones.

A partir del comportamiento desde las 00:00 a 23:00 horas, los registros muestran que la dirección de máxima
frecuencia corresponde a vientos procedentes desde todos los cuadrantes, sin embargo, los de mayor frecuencia
corresponde al segundo y tercer cuadrante, con vientos de mayor frecuencia desde el Suroeste (SO), Oeste Suroeste
(OSO), Oeste (O), Oeste Noroeste (ONO) y Noroeste (NO), explicando en conjunto un 50% de la frecuencia total.

Al observar el comportamiento espacial de los vientos en los diferentes periodos del día, Figura 12, se puede apreciar
que en términos generales no existe un patrón dominante en la procedencia del viento, ya que este llega de todas las
direcciones a lo largo de todo el día. Se observa un leve patrón entre el ciclo diurno y nocturno, con vientos desde el
Este y sus variaciones durante la noche y vientos desde el Oeste y sus variaciones durante el día. Entre las 12:00 y
17:00 horas se observa un leve patrón más marcado con vientos desde el suroeste (SO) y Oeste Suroeste (OSO), sin
embargo, se registran vientos en menor medida desde el Oeste (O), Oeste Noroeste (ONO) y Noroeste (NO).

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 17

**Figura 12. Variabilidad temporal del viento modelado - Zona IMO 2 líquido**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 18

**2.3.1.2.** **Ciclo Estacional**

La Figura 13 muestra la evolución estacional y diaria de la velocidad y dirección del viento modelado en el punto Zona
IMO 2 Líquido, presentando en el eje “x” las horas del día y en el eje “y” los meses del año. Es posible identificar un
leve ciclo anual, con las máximas velocidades centradas los meses desde septiembre a noviembre llegando a 4 m/s.
Para el periodo nocturno las velocidades se mantienen relativamente homogéneas a lo largo del año con velocidades
que se mantienen alrededor de 2 m/s.

En cuanto a la dirección del viento, se observa para el periodo nocturno vientos desde todas las direcciones, mientras
que, en horas del día, principalmente entre 11:00 y 17:00 horas el viento proviene desde el Oeste (O), Suroeste (SO)
y Noroeste (NO).

**Figura 13. Ciclo estacional del viento modelado - Zona IMO 2 líquido**

**Periodo 01 enero - 31 diciembre 2021**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 19

**2.3.1.3.** **Ciclo Diario de Velocidad del Viento**

En la siguiente figura se presentan los ciclos diarios promedio de la velocidad y dirección del viento modelado en el
punto Zona IMO 2 Líquido. Al apreciar la curva de velocidad promedio, se puede observar los valores mínimos se
presentan en el periodo nocturno con magnitudes que se mantienen relativamente constantes entre las 00:00 y 07:00
horas, momento en que la velocidad comienza a aumentar levemente hasta alcanzar el máximo diario a las 14:00
horas con una magnitud promedio de 3,7 m/s.

Respecto al ciclo diario de dirección del viento se puede observar que, durante toda la noche no existe una frecuencia
de vientos dominantes, ya que estos provienen desde cualquier dirección, sin embargo, entre las 12:00 y 18:00 horas
existe predominancia de vientos desde el Sur Suroeste (SSO), suroeste (SO) y Oeste Suroeste (OSO) llegando a
explicar el 30% de la frecuencia total.

**Figura 14. Ciclo diario de la velocidad del viento modelada - Zona Sólido**

**Periodo 01 enero - 31 diciembre 2021**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 20

**2.4.** **Análisis Descriptivo Velocidad y Dirección del Viento Punto N°4: Zona de Seguridad con Cámara de**

**Contención**

**2.4.1.** **Series de Tiempo**

La serie temporal de la velocidad del viento modelada en el punto de control Zona de Seguridad con Cámara de
Contención se muestra un leve ciclo anual, con las mayores velocidades registradas entre septiembre y noviembre,
con valores que superan 8 m/s. En términos generales las velocidades varían en promedio entre 2 y 4 m/s.

Con respecto a la dirección del viento no se observa ningún patrón anual, ya que las direcciones varían entre los 180
y 360° a lo largo del año, es decir, se observan vientos desde todas direcciones.

**Figura 15. Serie de tiempo modelada de velocidad y dirección del viento - Zona de Seguridad con Cámara de**

|Col1|Contención - Periodo 01 enero - 31 diciembre 2021|
|---|---|
|**VELOCIDAD**||
|**DIRECCIÓN**||

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 21

**2.4.1.1.** **Rosas de Viento**

A continuación, se muestran los campos de viento anual y para diferentes periodos del día, los que muestran la
variabilidad temporal del viento modelado durante el periodo entre enero y diciembre de 2021 en el punto Zona de
Seguridad con Cámara de Contención, indicando los porcentajes de frecuencia que el viento sopla en sus diferentes
direcciones. Cabe señalar que el comportamiento es coincidente con el descrito anteriormente en el punto Zona IMO
2 Líquidos.

A partir del comportamiento desde las 00:00 a 23:00 horas, los registros muestran que la dirección de máxima
frecuencia corresponde a vientos procedentes desde todos los cuadrantes, sin embargo, los de mayor frecuencia
corresponde al segundo y tercer cuadrante, con vientos de mayor frecuencia desde el Sur (S), Suroeste (SO), Oeste
Suroeste (OSO), Oeste (O), Oeste Noroeste (ONO) y Noroeste (NO), explicando en conjunto un 65% de la frecuencia

total.

Al observar el comportamiento espacial de los vientos en los diferentes periodos del día, Figura 12, se puede apreciar
que en términos generales no existe un patrón dominante en la procedencia del viento, ya que este llega de todas las
direcciones a lo largo de todo el día, a excepción del rango de hora entre las 12:00 y 17:00 horas, donde el viento
dominante proviene desde el Suroeste (SO). Se observa un leve patrón entre el ciclo diurno y nocturno, con vientos
desde el Este y sus variaciones durante la noche y vientos desde el Oeste y sus variaciones durante el día. Entre las
12:00 y 17:00 horas se observa un leve patrón más marcado con vientos desde el suroeste (SO) y Oeste Suroeste
(OSO), sin embargo, se registran vientos en menor medida desde el Oeste (O), Oeste Noroeste (ONO) y Noroeste
(NO).

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 22

**Figura 16. Variabilidad temporal del viento modelado - Zona de Seguridad con Cámara de Contención**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 23

**2.4.1.2.** **Ciclo Estacional**

La Figura 17 muestra la evolución estacional y diaria de la velocidad y dirección del viento modelado en el punto Zona
Piscina Contenedora, presentando en el eje “x” las horas del día y en el eje “y” los meses del año. Es posible identificar
un marcado ciclo anual, con las máximas velocidades centradas los meses desde septiembre a noviembre llegando a
6 m/s. Para el periodo nocturno las velocidades se mantienen relativamente homogéneas a lo largo del año con
velocidades que se mantienen alrededor de 3 m/s.

En cuanto a la dirección del viento, se observa para el periodo nocturno vientos desde todas las direcciones, mientras
que, en horas del día, principalmente entre 11:00 y 17:00 horas el viento proviene desde el Oeste (O), Suroeste (SO)
y Noroeste (NO).

**Figura 17. Ciclo estacional del viento modelado - Zona de Seguridad con Cámara de Contención**

**Periodo 01 enero - 31 diciembre 2021**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 24

**2.4.1.3.** **Ciclo Diario de Velocidad del Viento**

En la siguiente figura se presentan los ciclos diarios promedio de la velocidad y dirección del viento modelado en el
punto Zona Piscina Contenedora. Al apreciar la curva de velocidad promedio, se puede observar los valores mínimos
se presentan en el periodo nocturno con magnitudes que se mantienen relativamente constantes entre las 00:00 y
07:00 horas, momento en que la velocidad comienza a aumentar levemente hasta alcanzar el máximo diario a las
16:00 horas con una magnitud promedio de 4,2 m/s.

Respecto al ciclo diario de dirección del viento se puede observar que, durante toda la noche no existe una frecuencia
de vientos dominantes, ya que estos provienen desde cualquier dirección, sin embargo, entre las 12:00 y 18:00 horas
existe predominancia de vientos desde el Suroeste (SO) llegando a explicar el 40% de la frecuencia total.

**Figura 18. Ciclo diario de la velocidad del viento modelada - Zona de Seguridad con Cámara de Contención**

**Periodo 01 enero - 31 diciembre 2021**

Fuente: Elaboración propia

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 25

**2.5.** **Análisis Global de la Velocidad y Dirección del Viento**

Con el fin de caracterizar el régimen de vientos de manera local se presentan las rosas de los vientos en conjunto para
el periodo diurno y nocturno en los cuatro puntos de interés, estableciendo patrones en toda el área de interés. Se ha
considerado como “día” entre las 08:00 y 20:00 horas y como “noche” entre las 20:00 y 08:00 horas.

La Figura 19 y

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 26

Figura 20 muestra en conjunto el comportamiento de la dirección y velocidad del viento en cada punto evaluado para
el periodo diurno y nocturno. Durante el día, se observa en los cuatro puntos analizados que el viento proviene
principalmente desde el segundo y tercer cuadrante. Este decir, vientos desde el Oeste y sus diferentes variaciones,
tales como Noroeste (NO), Oeste Noroeste (ONO), Oeste (O), Suroeste (SO) y Oeste Suroeste (OSO),
correspondiendo la componente de máxima frecuencia a vientos desde el Suroeste (O) con velocidades que varían
principalmente entre 2,1 y 8,8 m/s, llegando incluso hasta 11 m/s. Cabe mencionar que, debido a la cercanía de los
puntos, la data para el Punto Zona sólidos y Zona IMO 1 Líquidos corresponde a valores similares, así como los datos
de los puntos zona IMO 2 líquido y zona de seguridad con cámara de contención.

Durante el periodo nocturno es posible observar una disminución en la velocidad del viento, variando entre 0,5 y 2,1
m/s en los cuatros puntos evaluados. En cuanto a la dirección, se mantiene el patrón observado durante el día, sin
embargo, la frecuencia de ocurrencia disminuye. Por otro lado, aparecen nuevas componentes con vientos desde el
primer y cuarto cuadrante, es decir, vientos desde el Este (E) y sus variaciones tales como: Este Noreste (ENE),
Noreste (NE), Este (E), Este Sureste (ESE), Sureste (SE) y Sur Sureste (SSE).

**Figura 19. Variabilidad de la velocidad y dirección del viento periodo diurno**

**Periodo 01 enero - 31 diciembre 2021**

|Zona Sólido|Zona IMO 1 Líquido|
|---|---|
|||
|**Zona IMO 2 Líquido**|**Zona de Seguridad con Cámara de Contención**|
|||

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 27

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 28

**Figura 20. Variabilidad de la velocidad y dirección del viento periodo nocturno**

**Periodo 01 enero - 31 diciembre 2021**

|Zona Sólido|Zona IMO 1 Líquido|
|---|---|
|||
|**Zona IMO 2 Líquido**|**Zona de Seguridad con Cámara de Contención**.|
|||

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 29

Fuente: Elaboración propia.

Se ha analizado la extensión temporal de datos de velocidad y dirección del viento modelados en cuatro puntos de
interés, desde enero a diciembre 2021. En términos de circulación general del viento se realizaron mapas espaciales
de la distribución de la velocidad del viento con el fin de entender de manera global la circulación de este, obteniendo
una satisfactoria correspondencia entre los cuatro puntos analizadas, observando en conjunto un claro ciclo del viento.

En término del análisis descriptivo, se observa un marcado ciclo diario para la velocidad del viento, con un
comportamiento homogéneo de la velocidad durante la noche, con velocidades que bordean 1,5 m/s en todos los
puntos evaluados, aumentando significativamente a partir de las 09:00 horas hasta alcanzar un máximo entre las 15:00
y 16:00 horas.

Respecto al ciclo diurno y nocturno se obtiene el mismo patrón en los cuatro puntos evaluados, donde los vientos en
términos generales provienen desde todas las direcciones, variando su frecuencia de ocurrencia según el periodo
evaluado. Entre las 08:00 y 20:00 horas los vientos dominantes provienen en su mayoría desde el segundo y tercer
cuadrante, es decir, vientos desde el Norte Noroeste (NNO), Noroeste (NO), Oeste Noroeste (ONO), Oeste (O), Oeste
Suroeste (OSO), Suroeste (SO), Sur Suroeste (SSO). Por otro lado, para el periodo nocturno entre las 00:00 y 09:00
horas y 21:00 y 23:00 horas, los vientos de mayor frecuencia corresponden a vientos desde el primero y cuarto
cuadrante, es decir, vientos desde el Norte (N), Norte Noroeste (NNO), Noroeste (NO), Este Noroeste (ENO), Este (E),
Este Sureste (ESE), Sureste (SE) y sur sureste (SSE).

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 30

**3.** **MODELACIÓN DE LA DISPERSIÓN**

**3.2.** **Base Teórica del Modelo de Dispersión Atmosférica Sistema WRF-Calpuff**

La aplicación de modelos de dispersión atmosférica permite determinar el aporte de las emisiones provenientes de
fuentes emisoras, en localidades y sectores aledaños a las instalaciones de un determinado proyecto, permitiendo de
este modo, asignar las cuotas de responsabilidad en los niveles de calidad del aire medidos en su entorno.

**3.2.1.** **Modelo Atmosférico WRF**

WRF es un modelo numérico de pronóstico e investigación atmosférica, desarrollado por las el Centro Nacional para
la investigación Atmosférica (NCAR) y los Centros Nacionales para la Predicción Medioambiental (NCEP), ambas

entidades norteamericanas.

Destaca sobre otros modelos porque considera los efectos de la superficie terrestre, lo que permite resolver o
pronosticar los fenómenos meteorológicos inducidos o influenciados por esa estructura. Su uso está aceptado por el
Servicio de Evaluación Ambiental en Chile, para ser aplicado dentro del Sistema de Evaluación de Impacto Ambiental,
ya que permite cubrir la necesidad de ampliar la resolución espacial que poseen las estaciones de monitoreo.

La forma de trabajo de WRF comprende la resolución de las ecuaciones primitivas de la atmósfera, utilizando una
descripción euleriana. Además, es un modelo no hidrostático, es decir, incluye la variación de presión en el eje vertical
de la atmósfera dentro de sus ecuaciones. Su manejo comprende dos componentes importantes, el primero de ellos
corresponde al WRF Pre-processing System (WPS) donde se preparan los archivos de entrada para las simulaciones
y el WRF Model (núcleo dinámico) donde se integran las ecuaciones dinámicas y termodinámicas, modelos de nubes,
superficie, radiación, microfísica, entre otros.

Las variables meteorológicas más importantes que inciden en la dispersión de las emisiones atmosféricas
corresponden a la temperatura, velocidad del viento y estabilidad atmosférica de la localidad sometida a evaluación.
Estas variables son utilizadas como entradas en los modelos de dispersión de contaminantes, necesarios para predecir
y evaluar los impactos ambientales actuales o de futuros proyectos. Es por esta razón que es necesario introducir los
resultados obtenidos del modelo WRF al modelo CALPUFF por lo que el modelo WRF genera una salida única de
archivo tipo paquete que trae cifrada toda la información necesaria para ser ingresada directamente al modelo de
dispersión Calpuff sin necesidad de procesarla, disminuyendo de esta manera la pérdida de calidad de los datos.

**3.2.2.** **Modelo de Dispersión CALPUFF**

El modelo CALPUFF es un sistema avanzado de modelación meteorológica y de calidad el aire, no estacionario,
desarrollado por Sigma Research Corporation (SRC) a fines de la década de 1980 (url: http://www.src.com). La versión
número seis del modelo está aprobada por la Agencia de Protección Ambiental de los Estados Unidos (EPA), lo que
convierte a este modelo en una herramienta ampliamente utilizada a nivel mundial. De forma particular, al igual que
WRF, el modelo CALPUFF está aprobado por el Servicio de Evaluación Ambiental en Chile, para poder emplearlo
dentro del Sistema de Evaluación de Impacto Ambiental.

CALPUFF modela el transporte y dispersión de contaminantes emitidos por las fuentes emisoras en forma de paquetes
o puff de material, procesándolos a través del dominio de modelación. Este modelo incluye tres componentes
principales: WRF, CALPUFF y CALPOST, además de una larga selección de preprocesadores, diseñados para incluir
datos meteorológicos y geofísicos en el modelo, simula campos de viento y temperatura en un dominio de modelación
engrillado y tridimensional pero en menor resolución que el modelo WRF. En el caso de la modelación de dispersión,

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 31

CALPUFF modela la dispersión de contaminantes y su post procesador CALPOST procesa las salidas de CALPUFF
creando archivos con las tabulaciones necesarias que permitan la evaluación de resultados.

**3.3.** **Variables de Entrada Ingresadas a la Modelación**

**3.3.1.** **Emisiones y Fuentes Consideradas en el Escenario Modelado**

Corresponde al valor emitido por cada fuente considerada en los diferentes escenarios de modelación y su localización
en el territorio. Para el presente estudio, cuyo objetivo es evaluar el comportamiento que presentaría la pluma de
dispersión en caso de que ocurriera un incendio en los sectores de almacenamiento Zona IMO líquidos, zona IMO
sólidos y área de seguridad con Piscina de contención del proyecto. A continuación se muestra una imagen del plano
de localización dentro del proyecto de las zonas consideradas como fuentes para el caso del presente estudio.

**Figura 21. Localización de las Zonas consideradas como Fuentes de Emisión**

Fuente: Planos DIA, Lamina 001, edición 0,Zonas de Deposito Temporal de Marpel.

Con respecto al cálculo de emisiones a considerar en caso de un incendio, al revisar las planillas de registro de
materiales almacenados entre los años 2018 y 2022 en estas zonas, no se logró establecer una sustancia
predominante dada la gran variedad de sustancias que se almacenan temporalmente en estas zonas, por lo que para
establecer y determinar una tasa de emisión asociada a algún tipo de sustancia se utilizó el cálculo que se realizó en
el Estudio de modelación de calidad del aire del proyecto Puerto Central, puerto de similares características al proyecto

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 32

que en este informe se evalúa, donde se caracterizaron las emisiones de la sustancia química acetona ya que era la
que tenía un predominio por sobre el resto de compuestos que este puerto almacena.

En este estudio se determinó por medio de las fórmulas de entalpias de evaporación y combustión de la sustancia, la
tasa de emisión de acuerdo con las propiedades químicas de la acetona, la fórmula utilizada se expone a continuación:

10 [−3] ∙h c
m=
C P ∙∆T+ h v

Donde:

m: pérdida de masa del líquido o combustible por unidad de suoerficie.

hc: Calor de Combustión (J/kg)

Cp: Calor especifico a presión constante (J/kg K)

∆T: Diferencia entre la temperatura promedio ambiental y la temperatura de ebullición de la sustancia (K).

hv: Calor de Vaporización (J/kg)

De acuerdo con la formula antes expuestas y en base a las características químicas de la acetona se obtiene que las
emisiones son de 51,5 g/m2s.

De esta manera para la modelación se realizó por separado para cada área de estudio y considerando la emisión antes
calculada por cada metro cuadrado de la superficie de las zonas de almacenamiento.

**3.3.2.** **Topografía del Área de Modelación**

En la Figura 22 se presenta la topografía del área de modelación en tres dimensiones, en la cual se observan las
principales variaciones topográficas del terreno. Las curvas de terreno están espaciadas cada 50 metros.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 33

**Figura 22. Topografía del área de modelación**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 34

**3.4.** **Resultados de la Modelación**

Los resultados de la modelación de la pluma fueron evaluados para el promedio anual y promedio mensual de cada
mes del año. A continuación se muestran las imágenes de plumas de dispersión para cada sector modelado, todas las
imágenes presentan la misma escala de la simbología para que puedan ser comparables.

**3.4.1.** **Pluma Dispersión Zona IMO Solidos**

A continuación se expone la pluma de dispersión promedio anual de la modelación de la zona IMO sólidos, es
importante recalcar que esta pluma representa un promedio, es decir que muestra la forma en que se mueve el
penacho de dispersión acumulada durante el año. De esta manera se puede concluir que no existe una tendencia
marcada en la orientación de la pluma, ya que al mostrarse los niveles de concentración homogéneos con una ligera
tendencia hacia el Norte, registra que los vientos no tienen una orientación predominante que marque la dirección
hacia donde se dispersarán las emisiones.

Con respecto a los niveles alcanzados se observa que los mayores niveles se posan dentro de la zona industrial y no
alcanzan en concentraciones considerables las zonas habitadas, esto dada la magnitud el nivel menor en la imagen.

**Figura 23. Pluma dispersión Promedio Anual Zona IMO Solidos**

Fuente: Elaboración propia.

A continuación se exponen las plumas de dispersión promedio mensuales del año 2021 para la modelación del área
de la zona IMO sólidos, esto con la finalidad de observar alguna orientación predominante durante los meses del año.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 35

**Figura 24. Pluma dispersión Promedio Mensual Zona IMO Sólidos**

**Periodo Enero - Junio 2021**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 36

**Figura 25. Pluma dispersión Promedio Mensual Zona IMO Sólidos.**

**Periodo Julio - Diciembre 2021**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 37

De las plumas de dispersión mes a mes se puede observar que entre enero y abril se marca de manera moderada una
tendencia de dispersión hacia el Suroeste - Noreste, en mayo se incorporó un predominio de dispersión hacia el Norte,
durante junio y julio predomina la dirección Suroeste que se modera al pasar a agosto, hasta octubre no muestra una
tendencia de dirección estable, por lo que se dispersa homogéneamente para todas las direcciones, durante noviembre
la dirección predominante de dispersión se marca de manera moderada hacia una dirección Noreste y en diciembre
se marca una tendencia moderada hacia el Suroeste y Sureste.

**3.4.2.** **Pluma Dispersión Zona IMO 1 Líquidos**

En el caso de la pluma de dispersión promedio anual de la modelación de la zona IMO 1 líquidos, es importante recalcar
que esta pluma representa un promedio, es decir que muestra la forma en que se mueve el penacho de dispersión
acumulado durante el año. De esta manera se puede concluir que no existe una tendencia muy marcada en la
orientación de la pluma, ya que al mostrarse los niveles de concentración homogéneos con una tendencia entre
Suroeste y Norestes.

Con respecto a los niveles alcanzados se observa que los mayores niveles se posan dentro de la zona industrial y no
alcanzan en concentraciones considerables las zonas habitadas, esto dada la magnitud del menor nivel en la imagen.

**Figura 26. Pluma dispersión Promedio Anual Zona IMO 1 Líquidos**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 38

A continuación se exponen las plumas de dispersión promedio mensuales del año 2021 para la modelación del área
de la zona IMO 1 líquidos, esto con la finalidad de observar alguna orientación predominante durante los meses del

año.

**Figura 27. Pluma dispersión Promedio Mensual Zona IMO 1 Líquidos**

**Periodo Enero - Junio 2021**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 39

**Figura 28. Pluma dispersión Promedio Mensual Zona IMO 1 Líquidos**

**Periodo Julio - Diciembre 2021**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 40

De las plumas de dispersión mes a mes se puede observar que entre enero y abril se marca de manera moderada una
tendencia de dispersión hacia el Suroeste - Noreste, en mayo se incorporó un predominio de dispersión hacia el Norte,
durante junio y julio predomina la dirección Suroeste que se modera al pasar a agosto, hasta octubre no muestra una
tendencia de dirección estable, por lo que se dispersa homogéneamente para todas las direcciones, durante noviembre
la dirección predominante de dispersión se marca de manera moderada hacia una dirección Noreste y en diciembre
se marca una tendencia moderada hacia el Suroeste y Sureste.

**3.4.3.** **Pluma Dispersión Zona IMO 2 Líquidos**

En el caso de la pluma de dispersión promedio anual de la modelación de la zona IMO 2 líquidos, se puede observar
que no existe una tendencia muy marcada en la orientación de la pluma, ya que al mostrarse los niveles de
concentración homogéneos con una tendencia Noroestes.

Con respecto a los niveles alcanzados se observa que los mayores niveles se posan dentro de la zona industrial y no
alcanzan en concentraciones considerables las zonas habitadas, esto dada la magnitud del menor nivel en la imagen.

**Figura 29. Pluma dispersión Promedio Anual Zona IMO 2 Líquidos**

Fuente: Elaboración propia.

A continuación se exponen las plumas de dispersión promedio mensuales del año 2021 para la modelación del área
de la zona IMO 2 líquidos, esto con la finalidad de observar alguna orientación predominante durante los meses del

año.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 41

**Figura 30. Pluma dispersión Promedio Mensual Zona IMO 2 Líquidos**

**Periodo Enero - Junio 2021**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 42

**Figura 31. Pluma dispersión Promedio Mensual Zona IMO 2 Líquidos**

**Periodo Julio - Diciembre 2021**

Fuente: Elaboración propia.

De las plumas de dispersión mes a mes se puede observar que entre enero y abril se marca de manera moderada una
tendencia de dispersión hacia el Suroeste - Noreste, en mayo se incorporó un predominio de dispersión hacia el Norte,
durante junio y julio predomina la dirección Noroeste que se marca al pasar a agosto, hasta octubre no muestra una

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 43

tendencia de dirección estable, por lo que se dispersa homogéneamente para todas las direcciones, durante noviembre
la dirección predominante de dispersión se marca de manera moderada hacia una dirección Noreste y en diciembre

se marca una tendencia moderada hacia el Suroeste.

**3.4.4.** **Pluma Dispersión Zona Piscina Contención**

En el caso de la pluma de dispersión promedio anual de la modelación de la zona Piscina de Contención, se puede
observar que no existe una tendencia muy marcada en la orientación de la pluma, ya que al mostrarse los niveles de
concentración homogéneos con una tendencia Suroestes.

Con respecto a los niveles alcanzados se observa que los mayores niveles se posan dentro de la zona industrial y no
alcanzan en concentraciones considerables las zonas habitadas, esto dada la magnitud del menor nivel en la imagen.
También se observa que al estar expuesta la fuente en una península las concentraciones disminuyen, es decir que
hay una mayor dispersión de la pluma dada unas mejores condiciones de ventilación esto se explica ya que en la
península se encuentra más expuesta a los vientos sin encontrar ninguna barrera de contención que disminuya la
magnitud de estos.

**Figura 32. Pluma dispersión Promedio Anual Zona Piscina Contención**

Fuente: Elaboración propia.

A continuación se exponen las plumas de dispersión promedio mensuales del año 2021 para la modelación del área
de la zona piscina de contención, esto con la finalidad de observar alguna orientación predominante durante los meses
del año, estas imágenes mantienen los niveles de la escala para ser comparables.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 44

**Figura 33. Pluma dispersión Promedio Mensual Zona Piscina Contención**

**Periodo Enero - Junio 2021**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 45

**Figura 34. Pluma dispersión Promedio Mensual Zona Piscina Contención**

**Periodo Julio - Diciembre 2021**

Fuente: Elaboración propia.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 46

De las plumas de dispersión mes a mes se puede observar que entre enero y mayo se marca de manera moderada
una tendencia de dispersión hacia el Suroeste, durante junio predomina la dirección Noroeste, al pasar a agosto se
muestra que disminuye la concentración habiendo mejores condiciones de dispersión (mayores vientos) que cambia
solo en septiembre pero vuele y se mantiene hasta diciembre. La pluma de dispersión no muestra una tendencia de
dirección estable, por lo que se dispersa homogéneamente para todas las direcciones.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 47

**4.** **CONCLUSIONES**

De los resultados obtenidos al evaluar la modelación de las plumas de dispersión de los sectores de almacenamiento
de sustancias peligrosas IMO en el proyecto se concluye que la dispersión se ve afectada por la topografía donde se
localizan las zonas de acopio, en especial por encontrarse a borde de costa en una península expuesta a los vientos
que provienen del océano donde se genera el viento llamado virazón que es un viento de los llamados mareros, ya
que soplan desde el mar hacia la tierra y tendría un comportamiento similar a los vientos altanos, que son los que se
levantan en tierra, corren al mar y vuelven de nuevo a tierra. De acuerdo con esto es que se concluye que no se puede
establecer una dirección predominante de la pluma ya que tienen un comportamiento muy variable. Pero esta condición
característica de la costa, facilita una mejor ventilación, es decir que no permite que se generen altas concentraciones
de la pluma ya que no se estancan en un lugar específico, es decir una mayor difusión de los gases tóxicos en la

atmósfera.

**DIA PROYECTO “AUTORIZACIÓN ZONAS DE ACOPIO TRANSITORIO DE MERCANCÍAS PELIGROSAS"** 48

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Coordenadas vértices del área de modelación del Proyecto****

| Vértice | Coordenadas UTM (Datum WGS-84 Huso 19S) | Col3 |
| --- | --- | --- |
| **Vértice** | **Norte (m)** | **Este (m)** |
| Noreste | 6315709,45 | 291787,06 |
| Noroeste | 6313951,02 | 778456,13 |
| Suroeste | 6242119,63 | 776110,17 |
| Sureste | 6243891,15 | 293607,52 |

**Tabla 2.: Localización de referencia y variables meteorológicas modeladas****

| ID | Punto modelado | Coordenadas UTM | Col4 | Variables | Periodo |
| --- | --- | --- | --- | --- | --- |
| **ID** | **Punto modelado** | **Norte (m)** | **Este (m)** | **Este (m)** | **Este (m)** |
| 1 | Zona sólidos | 256.619 | 6.280.275 | Velocidad del viento<br>Dirección del viento | 01 de enero al 31 de<br>diciembre 2021 |
| 2 | Zona IMO 1 Líquido | 256.620 | 6.279.900 | 6.279.900 | 6.279.900 |
| 3 | Zona IMO 2 Líquido | 256.640 | 6.279.846 | 6.279.846 | 6.279.846 |
| 4 | Zona Piscina<br>Contenedora | 256.539 | 6.280.517 | 6.280.517 | 6.280.517 |
