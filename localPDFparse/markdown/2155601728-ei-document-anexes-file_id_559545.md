---
title: Sin título
author: Users-Pre-Installed
date: D:20220414095910-04'00'
language: es
type: report
pages: 74
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME
-->

# INFORME

## Estudio de Impacto Odorante “Plantel Porcino El Charco”

### Agrícola El Pihuelo SpA

**14 de abril de 2022**

**Inf03E02.O-21-049**

### Datos del Proyecto

**Empresa** **:** Agrícola El Pihuelo.

**Plantel** **:** El Charco.

**Coordinador** **:** Marina González - Mejores Prácticas SpA.

**Subgerente Ing. Olores :** Miguel Gatica Rivera (MGR).

**Jefe de Proyecto** **:** Claudio Burdiles Melgarejo (CBM).

**Ingeniero de Proyecto** **:** Carolina Freire Ávila (CFA).

**Fecha** **:** 14 de abril de 2022.

|Emisión|Datos|Preparó|Revisó|Aprobó|
|---|---|---|---|---|
|Rev.0 Final|Nombre|CFA|CBM|CBM|
|Rev.0 Final|Fecha|14-04-2022|14-04-2022|14-04-2022|

Inf03E02.O-21-049.EIO.Plantel.El.Charco 2 de 74

**Índice General**

**1** **Resumen ............................................................................................................................. 7**

**2** **Introducción ..................................................................................................................... 10**

**3** **Objetivo General .............................................................................................................. 11**

Objetivos específicos .................................................................................................. 11
**4** **Metodología ...................................................................................................................... 11**

Caracterización de las fuentes de emisión de olor. ..................................................... 11

Estimación de emisiones ............................................................................................. 12

Evaluación de la dispersión de las emisiones de olor. ................................................. 13
4.3.1 Selección del modelo ....................................................................................... 13

4.3.2 Recopilación de los antecedentes para la modelación ..................................... 14

4.3.3 Variables meteorológicas y geofísicas ............................................................. 14

4.3.4 Evaluación de los resultados ........................................................................... 15

4.3.5 Área de Influencia y receptores de interés ....................................................... 16

Evaluación del desempeño del archivo de pronóstico utilizado ................................... 17
**5** **Resultados ....................................................................................................................... 18**

Caracterización de las fuentes de emisión .................................................................. 18

Emisiones de olor ........................................................................................................ 20

5.2.1 Emisiones consideradas en el modelo ............................................................. 20

5.2.2 Características fuentes de emisión ingresadas al modelo ................................ 29

5.2.3 Resumen de emisiones ................................................................................... 43

Evaluación de la dispersión de olores del plantel de cerdos ........................................ 44
5.3.1 Resultados emisión de olor del plantel ............................................................. 44

Análisis del desempeño del archivo de pronóstico utilizado ........................................ 52
**6** **Conclusiones ................................................................................................................... 54**

**7** **Anexos .............................................................................................................................. 55**

Anexo No1. Esquema de funcionamiento Calpuff y elementos de modelación ............ 55
Anexo No2. Análisis de receptores. ............................................................................. 59
Anexo No3. Descripción meteorológica y geofísica de la zona .................................... 60
7.3.1 Cantidad de datos ............................................................................................ 60

7.3.2 Gráficos Ciclo diario ......................................................................................... 62

7.3.3 Gráfico Distribución de Vientos ........................................................................ 63

7.3.4 Rosa de los vientos ......................................................................................... 64

7.3.5 Gráficos ciclo estacional .................................................................................. 66

7.3.6 Elevación de Terreno ....................................................................................... 67

Anexo No4. Análisis incertidumbre .............................................................................. 69

7.4.1 Ciclos Diarios promedios ................................................................................. 70

Inf03E02.O-21-049.EIO.Plantel.El.Charco 3 de 74

7.4.2 Promedio Mensuales ....................................................................................... 71

7.4.3 Dirección del viento ......................................................................................... 73

7.4.4 Análisis cuantitativo ......................................................................................... 73

**Índice de Tablas**

**Tabla No 1** . Emisiones promedio del plantel de cerdos El Charco. ........................................... 7
**Tabla No 2** . Concentración receptores (Percentil 98). ............................................................... 9
**Tabla No 3** . Informes de referencia de mediciones históricas Plantel de Cerdos San Agustín
del Arbolillo. ............................................................................................................................ 12
**Tabla No 4** . Informes de referencia de mediciones históricas Plantel de Cerdos Las Astas. ... 13
**Tabla No 5** . Variables de entrada consideradas en la modelación. ......................................... 14
**Tabla No 6.** Características del archivo meteorológico WRF. ................................................. 14
**Tabla No 7** . Límites de inmisión establecidos en la Norma de los países bajos. Percentil 98 . 15
**Tabla No 8** . Descripción fuentes generadoras de olor, plantel de cerdos El Charco. .............. 18
**Tabla No 9** . Coordenadas de referenciales de las fuentes modeladas. ................................... 19
**Tabla No 10** . Tasa de emisión medida en diciembre y enero en San Agustín del Arbolillo. .... 20
**Tabla No 11** . Tasa de emisión medida en febrero y marzo en San Agustín del Arbolillo. ........ 21
**Tabla No 12** . Tasa de emisión medida en abril y mayo en San Agustín del Arbolillo............... 22
**Tabla No 13** . Tasa de emisión medida en junio y julio en San Agustín del Arbolillo. ............... 23
**Tabla No 14** . Tasa de emisión medida en agosto y septiembre en San Agustín del Arbolillo. . 24
**Tabla No 15** . Tasa de emisión medida en octubre y noviembre en San Agustín del Arbolillo. . 25
**Tabla No 16** . Emisiones Zona de Transferencia. .................................................................... 26
**Tabla No 17** . Características de los ventiladores de la zona de transferencia. ........................ 26
**Tabla No 18** . Emisiones Laguna de Acumulación. .................................................................. 26
**Tabla No 19** . Emisiones Zona de Riego. ................................................................................. 27
**Tabla No 20** . Chimeneas tipo túnel. ........................................................................................ 29
**Tabla No 21** . Edades de los cerdos consideradas por pabellón. ............................................. 29
**Tabla No 22** . Edades de los cerdos consideradas por pabellón. ............................................. 30
**Tabla No 23** . Tasa de emisión pabellón N°1. .......................................................................... 31
**Tabla No 24** . Tasa de emisión pabellón N°2. .......................................................................... 32
**Tabla No 25** . Tasa de emisión pabellón N°3. .......................................................................... 33
**Tabla No 26** . Tasa de emisión pabellón N°4. .......................................................................... 34
**Tabla No 27** . Tasa de emisión pabellón N°5. .......................................................................... 35
**Tabla No 28** . Tasa de emisión pabellón N°6. .......................................................................... 36
**Tabla No 29** . Tasa de emisión pabellón N°7. .......................................................................... 37
**Tabla No 30** . Tasa de emisión pabellón N°8. .......................................................................... 38
**Tabla No 31** . Tasa de emisión pabellón N°9. .......................................................................... 39
**Tabla No 32** . Tasa de emisión pabellón N°10. ........................................................................ 40
**Tabla No 33** . Tasa de emisión pabellón N°11. ........................................................................ 41
**Tabla No 34** . Tasa de emisión pabellón N°12. ........................................................................ 42
**Tabla No 35** . Emisiones promedio del plantel de cerdos El Charco. ....................................... 43
**Tabla No 36** . Máxima concentración del plantel de cerdos. .................................................... 46
**Tabla No 37** . Receptores identificados en la caracterización de receptores. ........................... 47
**Tabla No 38** . Concentración receptores. Percentil 98. ............................................................ 49
**Tabla No 39.** Protocolo FIDOL con base a receptores definidos. ............................................ 51
**Tabla No 40** . Dimensiones de los pabellones. ........................................................................ 57
**Tabla No 41.** Datos de la estación meteorológica considerada. .............................................. 60
**Tabla No 42.** Datos válidos estación meteorológica Curicó. .................................................... 61

Inf03E02.O-21-049.EIO.Plantel.El.Charco 4 de 74

**Tabla No 43.** Análisis cuantitativo. .......................................................................................... 74

**Índice de Figuras**
**Figura No 1** . Mapa de concentración de olor generada por las fuentes de emisión del plantel
de cerdos (Percentil 98). ........................................................................................................... 8
**Figura No 2** . Área de estudio de impacto odorante. ................................................................ 10
**Figura No 3** . Esquema resumen de las metodologías para estimar las emisiones de olor. ..... 12
**Figura No 4** . Fuentes consideradas para modelación. ............................................................ 19
**Figura No 5** . Fuentes de emisión modeladas.......................................................................... 28
**Figura No 6** . Fuentes consideradas en el estudio. .................................................................. 43
**Figura No 7** . Mapa de concentración de olor generado por las fuentes de emisión del plantel
de cerdos. Promedio horario (percentil 98). ............................................................................ 45
**Figura No 8** . Área de Influencia del plantel de cerdos. ............................................................ 46
**Figura No 9** . Receptores de interés analizados. ..................................................................... 48
**Figura No 10** . Mapa de horas sobre 8 OU E /m3 generado por las fuentes de emisión del plantel
de cerdos. Promedio horario (percentil 98). ............................................................................ 50
**Figura No 11** . Estación Meteorológica utilizada en el Análisis de Incertidumbre. .................... 53
**Figura No 12** . Esquema funcionamiento CALPUFF. ............................................................... 55
**Figura No 13** . Esquema efecto downwash. ............................................................................ 56
**Figura No 14** . Esquema de los pabellones modelados. .......................................................... 57
**Figura No 15** . Esquema de la zona de transferencia. ............................................................. 57
**Figura No 16** . Zona de riego modelada. ................................................................................. 58
**Figura No 17** . Concentraciones horarias (OUE/m [3] ), Distribución horaria. Receptor No11. ...... 59
**Figura No 18** . Concentraciones horarias (OUE/m [3] ), Distribución horaria. Receptor No34. ...... 59
**Figura No 19.** Serie de tiempo velocidad del viento - datos observados estación Curicó - año
2020. ...................................................................................................................................... 60
**Figura No 20.** Serie de tiempo dirección del viento - datos observados estación Curicó - año
2020. ...................................................................................................................................... 61
**Figura No 21.** Serie de tiempo temperatura - datos observados estación Curicó - año 2020.
............................................................................................................................................... 61
**Figura No 22.** Ciclo diario para velocidad de viento Curicó. .................................................... 62
**Figura No 23.** Ciclo diario para dirección del viento estación Curicó. ...................................... 62
**Figura No 24.** Ciclo diario para temperatura estación Curicó. ................................................. 63
**Figura No 25.** Distribución velocidades de viento estación Curicó. ......................................... 64
**Figura No 26.** Rosa de los vientos Anual. Estación Curicó. .................................................... 64
**Figura No 27.** Rosas de los vientos por estación del año. ...................................................... 66
**Figura No 28.** Ciclo estacional - datos observados estación Curicó - Año 2020. ................... 67
**Figura No 29.** Elevación de terreno archivo WRF. .................................................................. 68
**Figura No 30.** Comparación ciclo diario de velocidad del viento entre datos observados y
proyectados para la estación de Curicó. ................................................................................. 70
**Figura No 31.** Comparación ciclo diario de dirección de viento entre datos observados y
proyectados para la estación de Curicó. ................................................................................. 70
**Figura No 32.** Comparación ciclo diario de temperatura entre los datos observados y
proyectados para la estación de Curicó. ................................................................................. 71
**Figura No 33.** Comparación moda mensual de velocidad de viento entre datos observados y
proyectados para la estación de Curicó. ................................................................................. 71
**Figura No 34.** Comparación moda mensual de dirección del viento entre datos observados y
proyectados para la estación de Curicó. ................................................................................. 72

Inf03E02.O-21-049.EIO.Plantel.El.Charco 5 de 74

**Figura No 35.** Comparación moda mensual de temperatura entre los datos observados y
proyectados para la estación de Curicó. ................................................................................. 72
**Figura No 36.** Comparación Rosas de viento. ........................................................................ 73

Inf03E02.O-21-049.EIO.Plantel.El.Charco 6 de 74

**1** **Resumen**

MEJORES PRÁCTICAS, solicitó los servicios de Proterm S.A para llevar a cabo un Estudio
de Impacto Odorante. El presente estudio tiene como objetivo determinar y/o descartar la
posible afectación a la calidad de vida de las personas, producto de la futura operación del
plantel de cerdos El Charco, ubicado en la comuna de Sagrada Familia, provincia de Curicó,
región del Maule.

Para determinar las emisiones de olor del plantel El Charco fue necesario utilizar emisiones de
referencias obtenidas a partir de los muestreos realizados en el plantel de cerdos San Agustín
del Arbolillo ubicado en la comuna de San Javier (Región del Maule) y del plantel de cerdos Las
Astas ubicado en Huépil (Región del BioBío); es importante señalar que dichos muestreos se
realizaron bajo la NCh N°3386:2015 y N°3431:2020, para posteriormente realizar un análisis
olfatométrico bajo la NCh N°3190:2010 en el laboratorio de Proterm S.A. Los muestreos has
sido realizados desde octubre del año 2020 a noviembre del año 2021 en las diferentes

estaciones del año.

A continuación, se presentan las emisiones determinadas del plantel de cerdos El Charco.

**Tabla No 1** . Emisiones promedio del plantel de cerdos El Charco.

|Fuente|Emisión 1<br>(OU /s)<br>E|
|---|---|
|Pabellones de cerdos (12)|245.063|
|Zona de Transferencia|3.728|
|Laguna de Acumulación|130.169|
|Zona de Riego|672.313|

Una vez obtenida la tasa de emisión de olor (OU E /s) de las fuentes, estas fueron ingresadas a
un modelo de dispersión atmosférica calpuff para obtener las concentraciones de inmisión de
olor. Los resultados de las concentraciones de olor (OU E /m [3] ) arrojadas por el modelo de
dispersión, fueron comparados con el límite establecido en la norma de los Países Bajos, donde
se indica un límite de inmisión de 8 OU E /m [3] (Percentil 98).

La dispersión de las emisiones de olor del plantel de cerdos indica que el área de influencia
cubre un área total de 9,52 km [2], distribuyéndose entre los pabellones, laguna de acumulación,
zona de transferencia y riego, con una longitud aproximada de 4,93 km en dirección noreste. El
área corresponde a la superficie circunscrita por 1 OU E /m [3], establecida en la “Guía para la
predicción y evaluación de impactos por olor en SEIA” del año 2017, indica la concentración en
donde el 50% de la población puede comenzar a detectar un olor.

La distribución de la pluma se acentúa hacia el noreste con una longitud aproximada de 4,83
km. Las isodoras pueden alcanzar valores entre 1,0 a 53 OU E /m [3] alcanzando su mayor

1 Promedio anual de las emisiones de los 12 pabellones

Inf03E02.O-21-049.EIO.Plantel.El.Charco 7 de 74

concentración en la zona de riego ubicada al sureste de los pabellones. Fuera de los límites del
plantel las isodoras trazan valores entre 1,0 a 8 OU E /m [3] .

**Figura No 1** . Mapa de concentración de olor generada por las fuentes de emisión del plantel

de cerdos (Percentil 98).

En base a lo mencionado anteriormente, en la siguiente Tabla, se presenta en forma detallada
las concentraciones de inmisión de olor en los receptores, donde se puede observar que
ninguno supera el límite establecido en la norma de los Países Bajos de 8 OU E /m [3 ] (Percentil
98).

Inf03E02.O-21-049.EIO.Plantel.El.Charco 8 de 74

**Tabla No 2** . Concentración receptores (Percentil 98).

|No|Concentración de<br>inmisión<br>(OU /m3)<br>E|Horas al año<br>>8 OU /m3<br>E|Límite de inmisión<br>Norma de los Países<br>Bajos|
|---|---|---|---|
|R1|0,22|0 (0,00%)|8|
|R2|0,35|0 (0,00%)|0 (0,00%)|
|R3|0,19|0 (0,00%)|0 (0,00%)|
|R4|0,16|0 (0,00%)|0 (0,00%)|
|R5|0,14|0 (0,00%)|0 (0,00%)|
|R6|0,10|0 (0,00%)|0 (0,00%)|
|R7|0,12|0 (0,00%)|0 (0,00%)|
|R8|0,23|0 (0,00%)|0 (0,00%)|
|R9|0,12|0 (0,00%)|0 (0,00%)|
|R10|0,59|3 (0,03%)|3 (0,03%)|
|R11|1,59|8 (0,09%)|8 (0,09%)|
|R12|0,46|0 (0,00%)|0 (0,00%)|
|R13|0,52|0 (0,00%)|0 (0,00%)|
|R14|0,23|0 (0,00%)|0 (0,00%)|
|R15|0,23|0 (0,00%)|0 (0,00%)|
|R16|0,22|0 (0,00%)|0 (0,00%)|
|R17|0,20|0 (0,00%)|0 (0,00%)|
|R18|0,20|0 (0,00%)|0 (0,00%)|
|R19|0,26|0 (0,00%)|0 (0,00%)|
|R20|0,04|0 (0,00%)|0 (0,00%)|
|R21|0,05|0 (0,00%)|0 (0,00%)|
|R22|0,17|0 (0,00%)|0 (0,00%)|
|R23|0,22|0 (0,00%)|0 (0,00%)|
|R24|0,10|0 (0,00%)|0 (0,00%)|
|R25|0,10|0 (0,00%)|0 (0,00%)|
|R26|0,18|0 (0,00%)|0 (0,00%)|
|R27|0,18|0 (0,00%)|0 (0,00%)|
|R28|0,11|0 (0,00%)|0 (0,00%)|
|R29|0,09|0 (0,00%)|0 (0,00%)|
|R30|0,08|0 (0,00%)|0 (0,00%)|
|R31|0,08|0 (0,00%)|0 (0,00%)|
|R32|0,21|0 (0,00%)|0 (0,00%)|
|R33|0,14|0 (0,00%)|0 (0,00%)|
|R34|2,15|22 (0,25%)|22 (0,25%)|

Dado los resultados anteriores, las concentraciones en las comunidades cercanas no superan
el límite de 8 OU E /m3 (Percentil 98) establecido en la Norma de los Países Bajos.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 9 de 74

**2** **Introducción**

Mejores Prácticas solicitó los servicios de Proterm S.A para llevar a cabo un Estudio de
Impacto Odorante del proyecto futuro plantel porcino El Charco. El presente estudio tiene
como objetivo determinar y/o descartar posible afectación a la calidad de vida de las
personas, producto de la operación del plantel, ubicado en la comuna de Sagrada Familia,
provincia de Curicó, región del Maule.

A continuación, se detalla la ubicación espacial del área considerada para el estudio de impacto
odorante.

**Figura No 2** . Área de estudio de impacto odorante.

El presente informe evalúa la dispersión de las emisiones de olor que podrían ser generadas
por la operación del plantel de cerdos El Charco.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 10 de 74

**3** **Objetivo General**

Evaluar las emisiones de olor generadas por plantel porcino El Charco sobre la salud de la
población cercana, sistema de vida, costumbres, población protegida y turismo.

**Objetivos específicos**

 Estimar las emisiones de olor generadas por el plantel de cerdos El Charco.

 Determinar la dispersión de las emisiones generadas por el plantel de cerdos El Charco.

 Comparar los valores de concentración de inmisión de olor, con la normativa de

referencia.

**4** **Metodología**

A continuación, se presenta la metodología utilizada que permitió evaluar el efecto de las
emisiones de olor que serán generadas por el plantel de cerdos El Charco.

**Caracterización de las fuentes de emisión de olor.**

Para poder caracterizar las fuentes generadoras de olor del plantel, se utilizaron las siguientes
metodologías:

 - Detección satelital: mediante Google Earth Pro [2], se identificaron las superficies de las
fuentes generadoras de olor y la distancia de los receptores con respecto al plantel.

 - Emisiones de referencia: como lo señala la Guía para la predicción y evaluación de
olores en el SEIA (2017), para proyectos nuevos se debe priorizar la utilización de
emisiones de referencia por sobre factores de emisión, lo anterior porque representan
de mejor forma el comportamiento de las fuentes generadoras de olor. Frente a lo
anteriormente señalado, se utilizaron las emisiones de olor muestreadas en el plantel
de cerdos San Agustín del Arbolillo, entre diciembre de 2020 y noviembre de 2021 para
los pabellones, zona de riego y zona de transferencia, mientras que para la laguna de
acumulación se consideraron las emisiones de la laguna de acumulación del plantel de
cerdos Las Astas, cuyo muestreo fue realizado previo a la aplicación de bacterias.

 - Solicitud de información al cliente: donde se especifican periodos de funcionamiento de
las fuentes, dimensiones, características, operación de los ventiladores y receptores.

2 Versión 7.1.5.1557 de Google Earth

Inf03E02.O-21-049.EIO.Plantel.El.Charco 11 de 74

**Estimación de emisiones**

Para conocer las emisiones del “Proyecto” se utilizaron emisiones de referencia obtenidas a
partir de los muestreos históricos realizados en los planteles de cerdos San Agustín del Arbolito
y Las Astas ubicados en San Javier y Huépil, respectivamente.

Revisión
Proyectos
Coexca S.A

Identificación

de emisiones

de referencia

Modelo de

dispersión
atmosférica

Calpuff

Unidades

de olor
(OUe/s)

**Figura No 3** . Esquema resumen de las metodologías para estimar las emisiones de olor.

En las siguientes tablas se detallan los informes utilizados como referencia tanto para los
pabellones, laguna de acumulación, zona de transferencia y zona de riego:

**Tabla No 3** . Informes de referencia de mediciones históricas Plantel de Cerdos San Agustín

del Arbolillo.

|Código informe|Descripción|Fecha de<br>muestreo|
|---|---|---|
|Inf02E02.O-20-067|Estudio de Impacto Odorante “Plantel porcino San<br>Agustín del Arbolito”|28 y 29 de<br>diciembre 2020|
|Inf01E01.O-21-003|Estudio de Impacto Odorante “Plantel porcino San<br>Agustín del Arbolito”|18,19 y 20 de<br>enero 2021|
|Inf03E01.O-21-003|Estudio de Impacto Odorante “Plantel porcino San<br>Agustín del Arbolito”|04 y 05 de<br>febrero 2021|
|Inf05E01.O-21-003|Estudio de Impacto Odorante “Plantel porcino San<br>Agustín del Arbolito”|08 y 09 de marzo<br>2021|
|Inf07E01.O-21-003|Estudio de Impacto Odorante “Plantel porcino San<br>Agustín del Arbolito”|12 y 13 de abril<br>2021|
|Inf09E01.O-21-003|Estudio de Impacto Odorante “Plantel porcino San<br>Agustín del Arbolito”|04 y 05 de mayo<br>2021|
|Inf11E01.O-21-003|Estudio de Impacto Odorante “Plantel porcino San<br>Agustín del Arbolito”|07 y 08 de junio<br>2021|
|Inf13E01.O-21-003|Estudio de Impacto Odorante “Plantel porcino San<br>Agustín del Arbolito”|07 y 08 de julio<br>2021|
|Inf15E01.O-21-003|Estudio de Impacto Odorante “Plantel porcino San<br>Agustín del Arbolito”|04 y 05 de agosto<br>2021|
|Inf02E01.O-21-051|Estudio de Impacto Odorante “Plantel porcino San<br>Agustín del Arbolito”|01, 02 y 21 de<br>septiembre 2021|
|Inf04E01.O-21-051|Estudio de Impacto Odorante “Plantel porcino San<br>Agustín del Arbolito”|04 y 05 de<br>octubre 2021|
|Inf06E01.O-21-051|Estudio de Impacto Odorante “Plantel porcino San<br>Agustín del Arbolito”|09 y 10 de<br>noviembre 2021|

Inf03E02.O-21-049.EIO.Plantel.El.Charco 12 de 74

**Tabla No 4** . Informes de referencia de mediciones históricas Plantel de Cerdos Las Astas.

|Código informe|Descripción|Fecha de<br>muestreo|
|---|---|---|
|Inf08E01.O-20-048|Estudio de Impacto Odorante “Plantel de Cerdos Monte<br>Verde Bajo”|07, 09 y 11 de<br>diciembre de<br>2020|
|Inf10E01.O-20-048|Estudio de Impacto Odorante “Plantel de Cerdos Monte<br>Verde Bajo”|11 al 14 de enero<br>de 2021|
|Inf12E02.O-20-048|Estudio de Impacto Odorante “Plantel de Cerdos Monte<br>Verde Bajo”|01 al 03 de<br>febrero y 03 de<br>marzo de 2021|
|Inf14E01.O-20-048|Estudio de Impacto Odorante “Plantel de Cerdos Monte<br>Verde Bajo”|02 y el 05 de<br>marzo de 2021|
|Inf02E02.O-21-027|Estudio de Impacto Odorante “Plantel de Cerdos Monte<br>Verde Bajo”|entre 06 y el 25<br>de mayo de 2021|
|Inf04E01.O-21-027|Estudio de Impacto Odorante “Plantel de Cerdos Monte<br>Verde Bajo”|entre el10 de<br>agosto y el 30 de<br>septiembre de<br>2021|

**Evaluación de la dispersión de las emisiones de olor.**

Para evaluar la dispersión atmosférica de las emisiones de olor generadas por las fuentes, se
realizaron las siguientes actividades.

**4.3.1 Selección del modelo**

Para seleccionar el modelo se consideraron los lineamientos que establece la Guía para el uso
de modelos de calidad del aire en el SEIA, publicada por el Servicio de Evaluación Ambiental
el año 2012.

Se consideró un modelo tipo Puff, el cual es una combinación entre los modelos Gaussiano y
Lagrangiano, en el sentido que esencialmente calculan la dispersión de gases provenientes de
una emisión instantánea, llamada “Puff”, a lo largo de una trayectoria. Su aproximación
matemática consiste en estimar la dispersión en forma Gaussiana en cada punto de una
trayectoria. Es decir, a diferencia de los modelos Lagrangianos que necesitan el cálculo de un
gran número de trayectorias para una fuente, los modelos tipo “Puff” sólo requieren una
trayectoria por “Puff”, lo que hace su cálculo mucho más rápido [3] .

Para la modelación se utilizó el software Calpuff versión 7.2.1 junto a los módulos CALPOST
7.1.0. y CALRANK 7.0.0. Además, para efectos de la interacción gráfica de los módulos, se usó
el software interactivo CALPUFF View 8.5.0.

En el Anexo N°1 se presenta el esquema del modelo utilizado y los elementos de la modelación.

3 Guía para el uso de modelos de calidad del aire, 2012

Inf03E02.O-21-049.EIO.Plantel.El.Charco 13 de 74

**4.3.2** **Recopilación de los antecedentes para la modelación**

Para conocer la dispersión que tendrán los gases en un área determinada es preciso incorporar
en el modelo seleccionando distintos parámetros de manera que la simulación sea lo más
parecida a las condiciones reales. Las variables o entradas que requirió el modelo se detallan
a continuación.

**Tabla No 5** . Variables de entrada consideradas en la modelación.

|Variable|Parámetros|Fuente|
|---|---|---|
|Meteorológicas|Dirección de Viento|Tal como lo establece la guía, el modelo<br>numérico recomendado para la generación de<br>datos meteorológicos es el Weather Research<br>and Forecasting Model (WRF). WRF es uno de<br>los modelos meteorológicos de pronóstico más<br>avanzados y completos que es mantenido por<br>NCAR/NOAA de Estados Unidos.|
|Meteorológicas|Velocidad de Viento|Velocidad de Viento|
|Meteorológicas|Temperatura|Temperatura|
|Meteorológicas|Presión|Presión|
|Meteorológicas|Precipitación|Precipitación|
|Geofísicas|Elevación del Terreno|Elevación del Terreno|
|Geofísicas|Uso de Suelo|Uso de Suelo|
|Características<br>de la fuente|Descripción del proceso|Información de fuentes consideradas en el<br>escenario evaluado.|
|Características<br>de la fuente|Emisiones de olor|Emisiones de olor|
|Características<br>de la fuente|Periodo de operación|Periodo de operación|
|Características<br>de la fuente|Temperatura de los gases|Temperatura de los gases|
|Características<br>de la fuente|Ubicación de las fuentes|Ubicación de las fuentes|
|Características<br>de la fuente|Velocidad de salida de los<br>gases|Velocidad de salida de los<br>gases|
|Receptores<br>Discretos|Coordenadas de los receptores|Se definieron los poblados cercanos al plantel.<br>Es importante señalar que los receptores fueron<br>proporcionados por personal del plantel.|

**4.3.3 Variables meteorológicas y geofísicas**

Tal como se mencionó en el punto 4.3.2, se utilizó la meteorología de pronóstico WRF en
formato calmet.dat, de esta forma se incorporó el archivo directamente al programa. El archivo
meteorológico tiene su centro en la comuna de Sagrada Familia. Para la ejecución del modelo
se modeló una zona más pequeña en comparación al WRF, es importante destacar que la zona
modelada tiene una dimensión de grilla de 250 metros (26 x 30 km). En la siguiente Tabla se
presentan las características del archivo meteorológico.

**Tabla No 6.** Características del archivo meteorológico WRF.

|Datos|Archivo Meteorológico|
|---|---|
|Comuna Central|Sagrada Familia|
|Dimensión grilla|66 x 66 km|
|Espaciado grilla|1 km|

Inf03E02.O-21-049.EIO.Plantel.El.Charco 14 de 74

|Datos|Col2|Archivo Meteorológico|
|---|---|---|
|Fecha-Hora inicio|Fecha-Hora inicio|01-01-2020 00:00|
|Fecha-Hora fin|Fecha-Hora fin|31-12-2020 23:00|
|Coordenadas NO4|Este|237.216|
|Coordenadas NO4|Norte|6.139.122|
|Coordenadas NE5|Este|303.519|
|Coordenadas NE5|Norte|6.140.164|
|Coordenadas SO6|Este|238.425|
|Coordenadas SO6|Norte|6.073.099|
|Coordenadas SE7|Este|305.001|
|Coordenadas SE7|Norte|6.073.798|

**4.3.4 Evaluación de los resultados**

Los resultados de la concentración de olor (OU E /m [3] ), modelados y registrados fueron
comparados con los límites de referencia, específicos para crianza de animales.

Se realizaron las comparaciones con la normativa de referencia de la Ley ganadera de los
Países Bajos. Esta norma establece como límite de inmisión “8 OU E /m [3] ” [ 8] el cual considera el
percentil 98, tal como lo recomienda la Norma de Países bajos para crianza de animales.

Criterios de impacto de olor en Países Bajos [9]

**Tabla No 7** . Límites de inmisión establecidos en la Norma de los países bajos. Percentil 98 [10]

|Límite de inmisión (OU /m3)<br>E|Uso de Suelo|
|---|---|
|2,0|Zona Urbana sin Ganadería|
|3,0|Zona Urbana con Ganadería|
|8,0|Fuera de la Zona Urbana|
|14,0|Zona Ganadera|

4 Coordenadas WGS-84 Huso 19.
5 Coordenadas WGS-84 Huso 19.
6 Coordenadas WGS-84 Huso 19.
7 Coordenadas WGS-84 Huso 18
8 Tabla resumen normativa internacional publicada por el SEIA.
9 Wet geurhinder en veehouderij - Artikel 3.1.
10 El percentil es una medida de tendencia central usada en estadística que indica, una vez ordenados los datos de
[menor a mayor, el valor de la variable por debajo del cual se encuentra un porcentaje dado de observaciones en un](https://es.wikipedia.org/wiki/Porcentaje)
grupo de observaciones. El Percentil 98 es el valor sobre el cual se encuentra el 98 % de los datos horarios de olor
registrados durante un año. (8760 datos)

Inf03E02.O-21-049.EIO.Plantel.El.Charco 15 de 74

Es por lo anteriormente señalado que los resultados de la concentración de olor (OU E /m [3] ),
modelados y registrados fueron comparados con los límites de inmisión de 8 OU E /m [3], percentil
98, establecido en la norma de los Países Bajos.

El límite mencionado anteriormente fue evaluado en receptores sensibles al olor. De acuerdo
con lo establecido en la Guía para la predicción y evaluación de impacto por olor en el SEIA,
donde se señala que _“La evaluación de los impactos ambientales por olor debe realizarse según_
_las consideraciones y criterios establecidos en los artículos 5 al 9 del Reglamento del SEIA,_
_según lo siguiente”:_

 _Población en cuanto a la salud de la población (letra a)._

 _Grupos humanos, en cuanto a los sistemas de vida y costumbres (letra c)._

 _Población protegida (letra d)._

 _Visitantes o turistas, en cuanto componente el valor turístico de una zona (letra e)._

En consecuencia, se indicarán los resultados sobre los sectores identificados bajo los puntos
anteriores.

Junto a los resultados de concentración de olor, se identificará el área de influencia de la
operación del plantel. Tal como lo indica la guía, el área de Influencia se debe circunscribir en
el espacio contenido por la isodora de 1 OU E /m [3], que corresponde al umbral de detección del
olor compuesto.

Los resultados de las concentraciones de olores (OU E /m [3] ) modeladas y registradas serán
comparados con el límite de inmisión establecido en la norma de los Países Bajos, donde se
indica un límite de 8 OU E /m [3] y factor de frecuencia el percentil 98.

**4.3.5 Área de Influencia y receptores de interés**

Una vez ejecutado el modelo de dispersión de olor, se realizó el análisis de post-proceso
obteniendo las curvas iso-concentración de la dispersión anual. Tal como lo indica la guía el
Área de Influencia se debe circunscribir en el espacio contenido por la isodora de 1 OU E /m [3],
que corresponde al umbral de detección del olor compuesto.

Una vez determinada el área de influencia, se realizó una descripción general y significativa del
Área de Influencia, para cada elemento del medio ambiente considerando los efectos,
características o circunstancias establecidos en el artículo 11 de la Ley N°19.300 como
población, población protegida, grupos humanos y visitantes o turistas.

De acuerdo con lo establecido en la Guía para la predicción y evaluación de impacto por olor
en el SEIA, donde se señala que _“La evaluación de los impactos ambientales por olor deben_
_realizarse según las consideraciones y criterios establecidos en los artículos 5 al 9 del_
_Reglamento del SEIA, según lo siguiente”:_

 _Población en cuanto a la salud de la población (letra a)._

 _Grupos humanos, en cuanto a los sistemas de vida y costumbres (letra c)._

Inf03E02.O-21-049.EIO.Plantel.El.Charco 16 de 74

 _Población protegida (letra d)._

 _Visitantes o turistas, en cuanto componente el valor turístico de una zona (letra e)._

**Evaluación del desempeño del archivo de pronóstico utilizado**

El modelo numérico recomendado para la generación de datos meteorológicos es el Weather
Research and Forecasting Model (WRF). WRF es uno de los modelos meteorológicos de
pronóstico más avanzados y completos, el cual es mantenido por NCAR/NOAA de Estados

Unidos.

Todos los modelos tienen asociados errores e incertidumbre. Los resultados del modelo se

analizan con base a la comparación de los gráficos indicados en los puntos 6.6.3 y 6.7 de la
“Guía para uso de modelos de Calidad del aire en el SEIA”. Con base a la comparación de los
ciclos diarios de las variables meteorológicas observadas y simuladas, en la misma, ubicación,
se debe caracterizar la capacidad del modelo de reproducir las observaciones tanto en
magnitud como en su variabilidad.

Para cumplir con lo indicado por la guía para uso de modelos de dispersión del SEA, se realizó
un análisis del desempeño de la meteorología de pronóstico WRF utilizada para la modelación.
Este análisis permite detectar posibles desviaciones en el modelo de pronóstico que podrían
causar efectos en los resultados del modelo de dispersión. Para este informe se contrastaron
las variables de viento respecto a los registros de la estación pública Curicó del SINCA.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 17 de 74

**5** **Resultados**

A continuación, se presentan los resultados que permitieron evaluar el efecto de las emisiones
de olor del plantel de cerdos El Charco.

**Caracterización de las fuentes de emisión**

A continuación, se presenta una breve descripción y ubicación de las fuentes consideradas en
la modelación, mientras que en la cartografía se presenta la ubicación espacial de cada una de
ellas. Lo anterior de acuerdo con lo señalado en el punto 3.3 de guía para la predicción y
evaluación de olores.

**Tabla No 8** . Descripción fuentes generadoras de olor, plantel de cerdos El Charco.

|Fuentes|Descripción|
|---|---|
|Pabellones<br>de cerdos|Se estima que cada pabellón tendrá 1.850 cerdos, cuya edad varía de 20 a 180<br>días.<br>Los pabellones presentaran tecnología tipo túnel y contaran con 6 extractores<br>con diámetro de 1,7 m.|
|Zona de<br>Transferencia|Una vez alcanzada una edad de 180 días y un peso entre 95 a 135 kg, los<br>cerdos son trasladados a la zona de transferencia.|
|Laguna de<br>acumulación|En los meses en que el purín tratado no es aplicado para el riego de cultivos,<br>este es conducido hacia una laguna de acumulación impermeabilizada, hasta<br>cuando los cultivos necesiten nuevamente el correspondiente riego.|
|Zona de riego|Se regará una superficie de 5 has por día en un periodo comprendido entre<br>septiembre y abril.|

Inf03E02.O-21-049.EIO.Plantel.El.Charco 18 de 74

**Tabla No 9** . Coordenadas de referenciales de las fuentes modeladas.

|Ubicación referencial de las fuentes|Coordenada<br>UTM Huso 19S Datum WGS84|Col3|
|---|---|---|
|**Ubicación referencial de las fuentes**|**Este (m)**|**Norte (m)**|
|Pabellones de cerdos|271.920|6.107.425|
|Zona de Transferencia|271.579|6.105.664|
|Laguna de Acumulación|272.316|6.107.270|
|Zona de Riego|270.933|6.106.704|

**Figura No 4** . Fuentes consideradas para modelación.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 19 de 74

**Emisiones de olor**

**5.2.1 Emisiones consideradas en el modelo**

Dado que el plantel de cerdos El Charco es un proyecto nuevo, se utilizaron las emisiones de
olor obtenidas a partir de las mediciones realizadas en el plantel de cerdos San Agustín del
Arbolillo, tal como lo muestran las siguientes tablas:

**Tabla No 10** . Tasa de emisión medida en diciembre y enero en San Agustín del Arbolillo.

|Hora|Emisión (OU /s)<br>E|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Hora**|**Diciembre 202011 **|**Diciembre 202011 **|**Diciembre 202011 **|**Diciembre 202011 **|**Enero 202112 **|**Enero 202112 **|**Enero 202112 **|**Enero 202112 **|
|**Hora**|**Pabellón**<br>**N°1**<br>**52 días13 **|**Pabellón**<br>**N°10**<br>**153 días**|**Pabellón**<br>**N°15**<br>**86 días**|**Pabellón**<br>**N°21**<br>**51 días**|**Pabellón**<br>**N°2**<br>**48 días**|**Pabellón**<br>**N°5**<br>**35 días**|**Pabellón**<br>**N°15**<br>**108 días**|**Pabellón**<br>**N°21**<br>**72 días**|
|**1 **|18.546|22.177|11.006|614|25.787|15.278|36.871|20.468|
|**2 **|10.737|19.813|8.882|614|22.922|14.034|31.453|17.817|
|**3 **|2.115|18.913|7.917|614|21.044|13.146|28.743|17.081|
|**4 **|3.905|17.224|6.372|614|18.970|12.613|27.212|14.725|
|**5 **|2.115|15.535|5.213|614|19.958|11.725|26.269|14.872|
|**6 **|2.603|13.959|4.055|614|16.401|11.370|23.324|12.958|
|**7 **|1.952|17.111|7.530|614|17.586|11.370|25.563|13.842|
|**8 **|4.230|28.932|16.219|614|10.473|18.831|40.405|25.769|
|**9 **|17.408|36.925|31.280|614|17.685|21.318|47.120|35.635|
|**10**|34.652|44.580|43.252|614|24.107|21.318|47.120|44.028|
|**11**|44.576|45.030|60.050|1.841|32.011|21.318|47.120|56.102|
|**12**|53.199|45.030|76.463|6.904|39.520|19.897|47.120|58.900|
|**13**|62.960|45.030|77.235|12.274|39.520|18.476|47.120|58.900|
|**14**|65.075|45.030|77.235|15.189|39.520|31.089|47.120|58.900|
|**15**|65.075|45.030|77.235|16.570|39.520|71.060|47.120|58.900|
|**16**|65.075|45.030|77.235|16.570|39.520|71.060|47.120|58.900|
|**17**|65.075|45.030|77.235|15.649|39.520|71.060|47.120|58.900|
|**18**|65.075|45.030|68.546|7.978|39.520|71.060|47.120|58.900|
|**19**|65.075|40.077|37.459|614|39.520|71.060|47.120|58.900|
|**20**|58.405|29.607|25.681|614|28.454|71.060|47.120|51.390|
|**21**|42.299|26.005|22.398|614|14.721|70.705|46.531|27.830|
|**22**|34.652|22.965|15.833|614|9.287|53.650|39.934|23.118|
|**23**|28.145|18.800|10.620|614|6.718|40.504|36.047|20.762|
|**24**|23.752|26.568|16.606|614|28.850|16.877|46.060|25.474|

11 Emisiones históricas. Informe Inf02E01.O-20-67.
12 Emisiones históricas. Informe Inf02E01.O-21-003.
13 Edad cerdos.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 20 de 74

**Tabla No 11** . Tasa de emisión medida en febrero y marzo en San Agustín del Arbolillo.

|Hora|Emisión (OU /s)<br>E|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Hora**|**Febrero 202114 **|**Febrero 202114 **|**Febrero 202114 **|**Febrero 202114 **|**Marzo 202115 **|**Marzo 202115 **|**Marzo 202115 **|**Marzo 202115 **|
|**Hora**|**Pabellón**<br>**N°2**<br>**64 días16 **|**Pabellón**<br>**N°5**<br>**50 días**|**Pabellón**<br>**N°15**<br>**124 días**|**Pabellón N°21**<br>**89 días**|**Pabellón**<br>**N°4**<br>**87 días**|**Pabellón**<br>**N°13**<br>**43 días**|**Pabellón**<br>**N°16**<br>**149 días**|**Pabellón**<br>**N°22**<br>**118 días**|
|**1 **|35.445|42.402|62.066|35.484|20.944|7.219|39.330|40.642|
|**2 **|28.609|39.814|51.067|30.574|19.141|6.822|38.937|35.030|
|**3 **|21.267|37.102|48.710|26.296|15.951|6.029|33.922|29.589|
|**4 **|16.963|37.718|45.175|23.287|13.778|5.553|29.498|27.888|
|**5 **|14.431|26.008|39.872|24.554|12.575|4.997|26.744|26.528|
|**6 **|13.165|37.595|40.068|25.029|10.125|4.284|22.811|25.337|
|**7 **|13.165|33.281|37.515|23.445|9.224|3.570|21.435|26.018|
|**8 **|25.318|14.545|54.799|31.524|11.165|2.538|23.795|27.548|
|**9 **|48.103|15.654|76.012|51.484|15.951|3.094|32.152|41.832|
|**10**|78.484|15.778|78.565|63.365|23.579|2.776|38.445|62.068|
|**11**|101.017|15.778|78.565|63.365|27.185|4.839|39.330|68.020|
|**12**|100.510|16.108|78.565|63.365|27.740|5.791|39.330|68.020|
|**13**|101.270|16.271|78.565|63.365|25.382|7.774|39.330|68.020|
|**14**|101.270|16.271|78.565|63.365|27.185|7.933|39.330|68.020|
|**15**|101.270|14.915|78.565|63.365|27.740|7.933|39.330|68.020|
|**16**|101.270|16.271|78.565|63.365|27.740|7.933|39.330|68.020|
|**17**|88.105|16.640|78.565|63.365|27.740|7.933|39.330|68.020|
|**18**|85.826|16.764|78.565|63.365|27.740|7.933|39.330|68.020|
|**19**|87.092|16.764|78.565|63.365|27.740|7.933|39.330|68.020|
|**20**|56.711|16.764|78.565|60.672|27.740|7.933|39.330|65.639|
|**21**|37.976|11.503|71.494|41.979|27.740|7.853|39.330|63.089|
|**22**|31.394|17.133|58.531|32.791|23.995|7.139|39.330|59.688|
|**23**|22.786|17.257|50.674|27.881|17.199|6.187|39.330|68.020|
|**24**|39.242|46.100|73.655|41.504|23.302|7.298|39.330|45.743|

14 Emisiones históricas. Informe Inf04E01.O-21-003.
15 Emisiones históricas. Informe Inf06E01.O-21-003.
16 Edad cerdos.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 21 de 74

**Tabla No 12** . Tasa de emisión medida en abril y mayo en San Agustín del Arbolillo.

|Hora|Emisión (OU /s)<br>E|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Hora**|**Abril 202117 **|**Abril 202117 **|**Abril 202117 **|**Abril 202117 **|**Mayo 202118 **|**Mayo 202118 **|**Mayo 202118 **|**Mayo 202118 **|
|**Hora**|**Pabellón**<br>**N°1**<br>**137 días19 **|**Pabellón**<br>**N°21**<br>**157 días**|**Pabellón**<br>**N°6**<br>**111 días**|**Pabellón**<br>**N°13**<br>**78 días**|**Pabellón**<br>**N°6**<br>**133 días**|**Pabellón**<br>**N°13**<br>**100 días**|**Pabellón**<br>**N°14**<br>**43 días**|**Pabellón**<br>**N°24**<br>**164 días**|
|**1 **|13.959|31.202|23.070|11.837|14.188|16.046|773|4.446|
|**2 **|13.341|33.237|21.875|11.172|14.971|19.333|773|4.446|
|**3 **|10.072|30.863|19.669|8.246|13.895|19.333|773|4.446|
|**4 **|9.719|30.015|18.658|10.640|12.525|13.919|773|4.446|
|**5 **|8.393|28.319|16.636|11.172|11.742|14.499|773|4.446|
|**6 **|8.835|29.336|15.901|9.443|8.709|13.919|773|4.446|
|**7 **|8.835|28.828|16.636|9.310|9.100|17.786|773|4.446|
|**8 **|14.843|31.880|19.669|7.847|10.861|13.919|773|4.446|
|**9 **|22.794|42.733|23.346|9.709|14.678|12.953|773|4.446|
|**10**|28.360|64.778|27.390|13.433|16.537|13.533|773|4.446|
|**11**|34.633|64.778|34.467|20.216|20.255|24.166|773|5.113|
|**12**|35.340|67.830|36.765|33.782|25.930|27.259|773|10.115|
|**13**|35.340|67.830|36.765|49.077|29.159|34.219|773|15.672|
|**14**|35.340|67.830|36.765|53.200|33.367|42.532|2.320|21.785|
|**15**|35.340|67.830|36.765|53.200|36.694|52.391|3.867|27.121|
|**16**|35.340|67.830|36.765|53.200|32.388|45.818|3.287|23.453|
|**17**|35.340|67.830|36.765|53.200|27.887|37.698|967|16.784|
|**18**|35.340|67.830|36.765|47.082|23.680|26.679|773|11.115|
|**19**|35.340|67.830|36.765|32.585|20.842|23.392|773|9.448|
|**20**|31.718|60.369|36.765|23.541|17.515|19.526|773|8.114|
|**21**|23.766|44.768|34.651|18.487|16.635|23.779|773|6.224|
|**22**|22.883|42.224|27.666|15.960|15.656|17.399|773|5.113|
|**23**|19.172|32.389|24.081|16.492|15.656|19.139|773|4.446|
|**24**|15.903|32.898|23.713|10.241|14.286|19.333|773|4.446|

17 Emisiones históricas. Informe Inf08E01.O-21-003.
18 Emisiones históricas. Informe Inf10E01.O-21-003.
19 Edad cerdos.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 22 de 74

**Tabla No 13** . Tasa de emisión medida en junio y julio en San Agustín del Arbolillo.

|Hora|Emisión (OU /s)<br>E|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Hora**|**Junio 202120 **|**Junio 202120 **|**Junio 202120 **|**Junio 202120 **|**Julio 202121 **|**Julio 202121 **|**Julio 202121 **|**Julio 202121 **|
|**Hora**|**Pabellón**<br>**N°8**<br>**158 días22 **|**Pabellón**<br>**N°13**<br>**134 días**|**Pabellón**<br>**N°14**<br>**76 días**|**Pabellón**<br>**N°20**<br>**43 días**|**Pabellón**<br>**N°6**<br>**22 días**|**Pabellón**<br>**N°13**<br>**164 días**|**Pabellón**<br>**N°15**<br>**100 días**|**Pabellón**<br>**N°21**<br>**68 días**|
|**1 **|1.710|10.750|1.094|131|136|3.595|3.937|1.154|
|**2 **|1.710|8.102|1.094|131|136|3.513|4.168|1.154|
|**3 **|1.710|11.373|1.094|131|136|3.885|4.400|1.154|
|**4 **|1.710|8.413|1.094|131|136|3.885|4.245|1.154|
|**5 **|1.710|11.062|1.094|131|136|3.761|4.400|1.154|
|**6 **|1.710|6.154|1.094|131|136|3.967|4.631|1.154|
|**7 **|1.710|10.594|1.094|131|136|3.361|3.602|1.154|
|**8 **|1.710|9.582|1.094|131|136|3.637|4.052|1.154|
|**9 **|1.710|10.517|1.094|131|136|3.595|4.979|1.154|
|**10**|1.710|13.633|1.094|131|136|3.141|6.561|1.154|
|**11**|4.574|17.761|2.736|131|136|3.141|7.719|1.154|
|**12**|7.225|19.631|4.651|131|136|3.141|10.266|1.154|
|**13**|8.465|20.644|5.472|131|136|3.141|13.276|1.154|
|**14**|9.662|22.747|5.563|131|136|3.141|18.525|1.635|
|**15**|10.132|21.189|5.654|131|136|3.141|17.908|2.405|
|**16**|8.849|19.397|5.198|131|136|3.141|17.522|1.635|
|**17**|6.840|17.060|4.104|131|136|3.141|14.280|1.154|
|**18**|5.985|15.346|3.192|131|136|3.141|11.347|1.154|
|**19**|5.173|14.256|2.918|131|136|3.141|9.263|1.154|
|**20**|4.403|14.022|2.827|131|136|3.141|9.031|1.154|
|**21**|3.249|14.645|3.374|131|136|3.141|8.877|1.154|
|**22**|3.078|16.047|3.739|131|136|3.141|9.263|1.154|
|**23**|2.009|16.982|3.830|131|136|3.141|9.031|1.154|
|**24**|1.710|9.738|1.094|131|136|3.637|4.245|1.154|

20 Emisiones históricas. Informe Inf012E01.O-21-003.
21 Emisiones históricas. Informe Inf14E01.O-21-003.
22 Edad cerdos.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 23 de 74

**Tabla No 14** . Tasa de emisión medida en agosto y septiembre en San Agustín del Arbolillo.

|Hora|Emisión (OU /s)<br>E|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Hora**|**Agosto 202123 **|**Agosto 202123 **|**Agosto 202123 **|**Agosto 202123 **|**Septiembre 202124 **|**Septiembre 202124 **|**Septiembre 202124 **|**Septiembre 202124 **|
|**Hora**|**Pabellón**<br>**N°3**<br>**66 días25 **|**Pabellón**<br>**N°8**<br>**39 días**|**Pabellón**<br>**N°14**<br>**134 días**|**Pabellón**<br>**N°20**<br>**101 días**|**Pabellón**<br>**N°6**<br>**78 días**|**Pabellón**<br>**N°12**<br>**37 días**|**Pabellón**<br>**N°17**<br>**145 días**|**Pabellón**<br>**N°24**<br>**111 días**|
|**1 **|955|252|4.554|3.336|2.238|1.545|7.250|6.803|
|**2 **|955|252|4.286|2.832|2.238|1.545|7.250|5.267|
|**3 **|955|252|4.019|2.392|2.238|1.545|7.250|5.267|
|**4 **|955|252|3.483|1.825|2.238|1.545|7.250|5.267|
|**5 **|955|252|5.269|2.266|2.238|1.545|7.250|5.267|
|**6 **|955|252|5.537|2.518|2.238|1.545|7.250|5.267|
|**7 **|955|252|5.090|2.895|2.238|1.545|7.250|5.267|
|**8 **|955|252|5.894|2.643|2.238|1.545|7.250|5.267|
|**9 **|955|252|6.965|2.706|2.238|1.545|9.667|13.606|
|**10**|955|252|8.305|4.217|2.238|1.545|20.140|21.945|
|**11**|955|252|11.163|6.294|2.238|1.545|36.051|37.087|
|**12**|955|252|11.163|7.993|11.191|1.545|45.516|55.082|
|**13**|955|252|12.145|10.196|19.165|1.545|55.788|65.177|
|**14**|955|252|12.591|10.762|24.900|1.545|59.413|71.541|
|**15**|955|252|11.877|10.133|26.019|1.545|63.441|74.394|
|**16**|955|252|11.698|9.252|20.284|1.545|63.642|68.249|
|**17**|955|252|11.252|7.553|7.694|1.545|58.406|44.109|
|**18**|955|252|11.252|6.357|2.238|1.545|42.093|23.701|
|**19**|955|252|11.341|6.168|2.238|1.545|22.557|16.898|
|**20**|955|252|10.627|5.790|2.238|1.545|18.932|12.948|
|**21**|955|252|10.002|5.853|2.238|1.545|12.688|8.120|
|**22**|955|252|10.537|5.979|2.238|1.545|7.250|5.267|
|**23**|955|252|10.091|6.357|2.238|1.545|7.653|5.267|
|**24**|955|252|5.090|3.713|2.238|1.545|7.855|12.070|

23 Emisiones históricas. Informe Inf016E01.O-21-003.
24 Emisiones históricas. Informe Inf02E01.O-21-051.
25 Edad cerdos.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 24 de 74

**Tabla No 15** . Tasa de emisión medida en octubre y noviembre en San Agustín del Arbolillo.

|Hora|Emisión (OU /s)<br>E|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Hora**|**Octubre 202126 **|**Octubre 202126 **|**Octubre 202126 **|**Octubre 202126 **|**Noviembre 202127 **|**Noviembre 202127 **|**Noviembre 202127 **|**Noviembre 202127 **|
|**Hora**|**Pabellón**<br>**N°6**<br>**110 días28 **|**Pabellón**<br>**N°11**<br>**79 días**|**Pabellón**<br>**N°16**<br>**36 días**|**Pabellón**<br>**N°22**<br>**153 días**|**Pabellón**<br>**N°6**<br>**145 días**|**Pabellón**<br>**N°12**<br>**111 días**|**Pabellón**<br>**N°17**<br>**78 días**|**Pabellón**<br>**N°24**<br>**37 días**|
|**1 **|3.962|6.504|761|5.400|13.634|5.310|2.354|419|
|**2 **|3.962|6.504|761|4.985|12.646|4.848|2.354|419|
|**3 **|3.962|6.504|761|4.985|12.449|4.001|2.354|419|
|**4 **|3.962|6.504|761|4.985|11.955|3.386|2.354|419|
|**5 **|3.962|6.504|761|4.985|10.374|2.924|2.354|419|
|**6 **|3.962|6.504|761|4.985|12.646|3.078|2.354|419|
|**7 **|3.962|6.504|761|4.985|15.512|4.771|2.354|2.199|
|**8 **|3.962|6.504|761|4.985|16.895|7.310|2.354|3.771|
|**9 **|3.962|6.504|761|4.985|36.062|12.312|2.354|3.771|
|**10**|3.962|6.504|761|4.985|36.260|17.083|2.354|8.693|
|**11**|3.962|6.504|761|4.985|2.371|22.854|7.455|18.224|
|**12**|13.645|6.504|761|11.446|39.520|26.009|13.928|33.621|
|**13**|41.101|18.427|761|28.108|39.520|30.395|28.445|419|
|**14**|57.607|40.106|761|44.862|39.520|30.780|33.742|524|
|**15**|62.229|59.617|761|50.816|39.520|30.780|37.273|2.828|
|**16**|34.663|86.716|3.044|55.385|39.520|30.780|50.613|3.875|
|**17**|6.933|69.373|1.332|52.616|39.520|30.780|46.493|2.828|
|**18**|7.098|51.488|761|55.385|39.520|30.780|38.058|1.047|
|**19**|5.612|36.312|761|51.923|38.828|29.472|25.110|419|
|**20**|2.971|14.633|761|33.923|29.245|21.623|8.043|419|
|**21**|825|6.504|761|27.277|17.290|14.544|2.354|419|
|**22**|660|6.504|761|20.216|14.721|13.235|2.354|419|
|**23**|660|6.504|761|15.369|14.128|11.619|2.354|419|
|**24**|4.292|6.504|761|7.615|14.721|6.772|2.354|419|

Zona de transferencia

Se considera una emisión anual, de lunes a viernes entre 07:00 a 14:00 hrs hasta diciembre y
desde enero de 07:00 a 19:00 hrs. A continuación, se presenta la tasa de emisión modelada
para la zona de transferencia.

26 Emisiones históricas. Informe Inf016E01.O-21-003.
27 Emisiones históricas. Informe Inf02E01.O-21-051.
28 Edad cerdos.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 25 de 74

**Tabla No 16** . Emisiones Zona de Transferencia.

|Mes|N° de ventiladores|Tasa de emisión<br>OU /s<br>E|
|---|---|---|
|Diciembre 2020|9|6.053|
|Enero 2021|9|2.788|
|Febrero 2021|9|3.338|
|Marzo 2021|9|3.338|
|Abril 2021|9|1.787|
|Mayo 2021|9|5.074|
|Junio 2021|9|1.997|
|Julio 2021|9|4.180|
|Agosto 2021|9|4.849|
|Septiembre 2021|9|4.849|
|Octubre 2021|9|2.044|
|Noviembre 2021|9|4.434|

A continuación, se presenta una tabla con las características de los ventiladores de la zona de
transferencia.

**Tabla No 17** . Características de los ventiladores de la zona de transferencia.

|Característica|Valor|
|---|---|
|Número de ventiladores|9|
|Altura|1,25 m|
|Temperatura|20°C|
|Diámetro|1,5 m/s|
|Velocidad promedio|7,07 m/s|

Laguna de Acumulación

A continuación, se presenta la tasa de emisión de olor (OU E /s) considerada en cada mes del

año.

**Tabla No 18** . Emisiones Laguna de Acumulación.

|Mes|Tasa de emisión (OU /s)<br>E|
|---|---|
|Diciembre 2020|140.529|
|Enero 2021|129.133|
|Febrero 2021|50.338|
|Marzo 2021|101.978|
|Abril 2021|176.670|
|Mayo 2021|176.670|
|Junio 2021|176.670|

Inf03E02.O-21-049.EIO.Plantel.El.Charco 26 de 74

|Mes|Tasa de emisión (OU /s)<br>E|
|---|---|
|Julio 2021|139.682|
|Agosto 2021|139.682|
|Septiembre 2021|139.682|
|Octubre 2021|85.307|
|Noviembre 2021|105.690|

Zona de Riego

A continuación, se presenta la tasa de emisión de olor (OU E /s) considerada entre septiembre y
abril para la zona de riego.

**Tabla No 19** . Emisiones Zona de Riego.

|Mes|Tasa de emisión<br>OU /s<br>E|
|---|---|
|Diciembre 2020|468.500|
|Enero 2021|466.000|
|Febrero 2021|109.000|
|Marzo 2021|332.500|
|Abril 2021|221.500|
|Mayo 2021|0|
|Junio 2021|0|
|Julio 2021|0|
|Agosto 2021|0|
|Septiembre 2021|654.000|
|Octubre 2021|1.742.500|
|Noviembre 2021|1.384.500|

Inf03E02.O-21-049.EIO.Plantel.El.Charco 27 de 74

**Figura No 5** . Fuentes de emisión modeladas.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 28 de 74

**5.2.2 Características fuentes de emisión ingresadas al modelo** **[29]**

Pabellones recría-finalización

La emisión de cada pabellón se considera a mediante la tecnología tipo túnel ubicadas a una
altura aproximada de 1,25 m. Se consideran las siguientes características.

**Tabla No 20** . Chimeneas tipo túnel.

|Característica|Valor|
|---|---|
|Número de ventiladores|6|
|Altura|1,25 m|
|Temperatura|20°C|
|Diámetro|1,5 m/s|
|Velocidad promedio|7,07 m/s|

En la siguiente tabla, se presentan las edades informadas por el titular y que fueron
consideradas en la modelación de olor.

**Tabla No 21** . Edades de los cerdos consideradas por pabellón [30] .

|Pabellones|Enero|Febrero|Marzo|Abril|Mayo|Junio|
|---|---|---|---|---|---|---|
|**1 **|21-49|49-77|77-112|112-140|140-168|168-182|
|**2 **|21-42|42-70|70-105|105-133|133-161|161-182|
|**3 **|182|35-63|63-98|98-126|126-154|154-182|
|**4 **|175-182|28-56|56-91|91-119|119-147|147-182|
|**5 **|168-182|21-49|49-84|84-112|112-140|140-175|
|**6 **|161-182|21-42|42-77|77-105|105-133|133-168|
|**7 **|154-182|182|35-70|70-98|98-126|126-161|
|**8 **|147-175|175-182|28-63|63-91|91-119|119-154|
|**9 **|140-168|168-182|21-56|56-84|84-112|112-147|
|**10**|133-161|161-182|21-49|49-77|77-105|105-140|
|**11**|126-154|154-182|182|42-70|70-98|98-133|
|**12**|119-147|147-175|175-182|35-63|63-91|91-126|

29 Información entregada por Coexca S.A.
30 Información proporcionada por el titular.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 29 de 74

**Tabla No 22** . Edades de los cerdos consideradas por pabellón [31] .

|Pabellones|Julio|Agosto|Septiembre|Octubre|Noviembre|Diciembre|
|---|---|---|---|---|---|---|
|**1 **|28-56|56-91|91-119|119-147|147-182|182|
|**2 **|21-49|49-84|84-112|112-140|140-175|175-182|
|**3 **|21-42|42-77|77-105|105-133|133-168|168-182|
|**4 **|182|35-70|70-98|98-126|126-161|161-182|
|**5 **|175-182|28-63|63-91|91-119|119-154|154-182|
|**6 **|168-182|21-56|56-84|84-112|112-147|147-182|
|**7 **|161-182|21-49|49-77|77-105|105-140|140-175|
|**8 **|154-182|182|42-70|70-98|98-133|133-168|
|**9 **|147-175|175-182|35-63|63-91|91-126|126-161|
|**10**|140-168|168-182|28-56|56-84|84-119|119-154|
|**11**|133-161|161-182|21-49|49-77|77-112|112-140|
|**12**|126-154|154-182|21-42|42-70|70-105|105-133|

31 Información proporcionada por el titular.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 30 de 74

**Tabla No 23** . Tasa de emisión pabellón N°1. [32]

|Col1|Emisión de olor Pabellón N°1|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**Enero**<br>|**Febrero**|**Marzo**<br>|**Abril**|**Mayo**<br>|**Junio**|**Julio**<br>|**Agosto**|**Septiembre**<br>|**Octubre**|**Noviembre**<br>|**Diciembre**|
|**Edad**|**21-49**|**49-77**|**77-112**|**112-140**|**140-168**|**168-182**|**28-56**|**56-91**|**91-119**|**119-147**|**147-182**|**182**|
|**1 **|25.787|35.445|20.944|13.959|4.446|1.710|136|955|6.803|3.962|13.634|22.177|
|**2 **|22.922|28.609|19.141|13.341|4.446|1.710|136|955|5.267|3.962|12.646|19.813|
|**3 **|21.044|21.267|15.951|10.072|4.446|1.710|136|955|5.267|3.962|12.449|18.913|
|**4 **|18.970|16.963|13.778|9.719|4.446|1.710|136|955|5.267|3.962|11.955|17.224|
|**5 **|19.958|14.431|12.575|8.393|4.446|1.710|136|955|5.267|3.962|10.374|15.535|
|**6 **|16.401|13.165|10.125|8.835|4.446|1.710|136|955|5.267|3.962|12.646|13.959|
|**7 **|17.586|13.165|9.224|8.835|4.446|1.710|136|955|5.267|3.962|15.512|17.111|
|**8 **|10.473|25.318|11.165|14.843|4.446|1.710|136|955|5.267|3.962|16.895|28.932|
|**9 **|17.685|48.103|15.951|22.794|4.446|1.710|136|955|13.606|3.962|36.062|36.925|
|**10**|24.107|78.484|23.579|28.360|4.446|1.710|136|955|21.945|3.962|36.260|44.580|
|**11**|32.011|101.017|27.185|34.633|5.113|4.574|136|955|37.087|3.962|2.371|45.030|
|**12**|39.520|100.510|27.740|35.340|10.115|7.225|136|955|55.082|13.645|39.520|45.030|
|**13**|39.520|101.270|25.382|35.340|15.672|8.465|136|955|65.177|41.101|39.520|45.030|
|**14**|39.520|101.270|27.185|35.340|21.785|9.662|136|955|71.541|57.607|39.520|45.030|
|**15**|39.520|101.270|27.740|35.340|27.121|10.132|136|955|74.394|62.229|39.520|45.030|
|**16**|39.520|101.270|27.740|35.340|23.453|8.849|136|955|68.249|34.663|39.520|45.030|
|**17**|39.520|88.105|27.740|35.340|16.784|6.840|136|955|44.109|6.933|39.520|45.030|
|**18**|39.520|85.826|27.740|35.340|11.115|5.985|136|955|23.701|7.098|39.520|45.030|
|**19**|39.520|87.092|27.740|35.340|9.448|5.173|136|955|16.898|5.612|38.828|40.077|
|**20**|28.454|56.711|27.740|31.718|8.114|4.403|136|955|12.948|2.971|29.245|29.607|
|**21**|14.721|37.976|27.740|23.766|6.224|3.249|136|955|8.120|825|17.290|26.005|
|**22**|9.287|31.394|23.995|22.883|5.113|3.078|136|955|5.267|660|14.721|22.965|
|**23**|6.718|22.786|17.199|19.172|4.446|2.009|136|955|5.267|660|14.128|18.800|
|**24**|28.850|39.242|23.302|15.903|4.446|1.710|136|955|12.070|4.292|14.721|26.568|

32 En caso de que en algún mes no se haya muestreado un pabellón con el rango de edad indicado, se consideró el valor más alto del mes.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 31 de 74

**Tabla No 24** . Tasa de emisión pabellón N°2. [33]

|Col1|Emisión de olor Pabellón N°2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**Enero**<br>|**Febrero**|**Marzo**<br>|**Abril**|**Mayo**<br>|**Junio**|**Julio**<br>|**Agosto**|**Septiembre**<br>|**Octubre**|**Noviembre**<br>|**Diciembre**|
|**Edad**|**21-42**|**42-70**|**70-105**|**105-133**|**133-161**|**161-182**|**21-49**|**49-84**|**84-112**|**112-140**|**140-175**|**175-182**|
|**1 **|15.278|35.445|20.944|23.070|14.188|1.710|136|955|6.803|3.962|13.634|22.177|
|**2 **|14.034|28.609|19.141|21.875|14.971|1.710|136|955|5.267|3.962|12.646|19.813|
|**3 **|13.146|21.267|15.951|19.669|13.895|1.710|136|955|5.267|3.962|12.449|18.913|
|**4 **|12.613|16.963|13.778|18.658|12.525|1.710|136|955|5.267|3.962|11.955|17.224|
|**5 **|11.725|14.431|12.575|16.636|11.742|1.710|136|955|5.267|3.962|10.374|15.535|
|**6 **|11.370|13.165|10.125|15.901|8.709|1.710|136|955|5.267|3.962|12.646|13.959|
|**7 **|11.370|13.165|9.224|16.636|9.100|1.710|136|955|5.267|3.962|15.512|17.111|
|**8 **|18.831|25.318|11.165|19.669|10.861|1.710|136|955|5.267|3.962|16.895|28.932|
|**9 **|21.318|48.103|15.951|23.346|14.678|1.710|136|955|13.606|3.962|36.062|36.925|
|**10**|21.318|78.484|23.579|27.390|16.537|1.710|136|955|21.945|3.962|36.260|44.580|
|**11**|21.318|101.017|27.185|34.467|20.255|4.574|136|955|37.087|3.962|2.371|45.030|
|**12**|19.897|100.510|27.740|36.765|25.930|7.225|136|955|55.082|13.645|39.520|45.030|
|**13**|18.476|101.270|25.382|36.765|29.159|8.465|136|955|65.177|41.101|39.520|45.030|
|**14**|31.089|101.270|27.185|36.765|33.367|9.662|136|955|71.541|57.607|39.520|45.030|
|**15**|71.060|101.270|27.740|36.765|36.694|10.132|136|955|74.394|62.229|39.520|45.030|
|**16**|71.060|101.270|27.740|36.765|32.388|8.849|136|955|68.249|34.663|39.520|45.030|
|**17**|71.060|88.105|27.740|36.765|27.887|6.840|136|955|44.109|6.933|39.520|45.030|
|**18**|71.060|85.826|27.740|36.765|23.680|5.985|136|955|23.701|7.098|39.520|45.030|
|**19**|71.060|87.092|27.740|36.765|20.842|5.173|136|955|16.898|5.612|38.828|40.077|
|**20**|71.060|56.711|27.740|36.765|17.515|4.403|136|955|12.948|2.971|29.245|29.607|
|**21**|70.705|37.976|27.740|34.651|16.635|3.249|136|955|8.120|825|17.290|26.005|
|**22**|53.650|31.394|23.995|27.666|15.656|3.078|136|955|5.267|660|14.721|22.965|
|**23**|40.504|22.786|17.199|24.081|15.656|2.009|136|955|5.267|660|14.128|18.800|
|**24**|16.877|39.242|23.302|23.713|14.286|1.710|136|955|12.070|4.292|14.721|26.568|

33 En caso de que en algún mes no se haya muestreado un pabellón con el rango de edad indicado, se consideró el valor más alto del mes.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 32 de 74

**Tabla No 25** . Tasa de emisión pabellón N°3. [34]

|Col1|Emisión de olor Pabellón N°3|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**Enero**|**Febrero**|**Marzo**<br>|**Abril**|**Mayo**<br>|**Junio**|**Julio**|**Agosto**|**Septiembre**|**Octubre**|**Noviembre**|**Diciembre**|
|**Edad**|**182**|**35-63**|**63-98**|**98-126**|**126-154**|**154-182**|**21-42**|**42-77**|**77-105**|**105-133**|**133-168**|**168-182**|
|**1 **|36.871|35.445|20.944|23.070|14.188|1.710|136|955|2.238|3.962|13.634|22.177|
|**2 **|31.453|28.609|19.141|21.875|14.971|1.710|136|955|2.238|3.962|12.646|19.813|
|**3 **|28.743|21.267|15.951|19.669|13.895|1.710|136|955|2.238|3.962|12.449|18.913|
|**4 **|27.212|16.963|13.778|18.658|12.525|1.710|136|955|2.238|3.962|11.955|17.224|
|**5 **|26.269|14.431|12.575|16.636|11.742|1.710|136|955|2.238|3.962|10.374|15.535|
|**6 **|23.324|13.165|10.125|15.901|8.709|1.710|136|955|2.238|3.962|12.646|13.959|
|**7 **|25.563|13.165|9.224|16.636|9.100|1.710|136|955|2.238|3.962|15.512|17.111|
|**8 **|40.405|25.318|11.165|19.669|10.861|1.710|136|955|2.238|3.962|16.895|28.932|
|**9 **|47.120|48.103|15.951|23.346|14.678|1.710|136|955|2.238|3.962|36.062|36.925|
|**10**|47.120|78.484|23.579|27.390|16.537|1.710|136|955|2.238|3.962|36.260|44.580|
|**11**|47.120|101.017|27.185|34.467|20.255|4.574|136|955|2.238|3.962|2.371|45.030|
|**12**|47.120|100.510|27.740|36.765|25.930|7.225|136|955|11.191|13.645|39.520|45.030|
|**13**|47.120|101.270|25.382|36.765|29.159|8.465|136|955|19.165|41.101|39.520|45.030|
|**14**|47.120|101.270|27.185|36.765|33.367|9.662|136|955|24.900|57.607|39.520|45.030|
|**15**|47.120|101.270|27.740|36.765|36.694|10.132|136|955|26.019|62.229|39.520|45.030|
|**16**|47.120|101.270|27.740|36.765|32.388|8.849|136|955|20.284|34.663|39.520|45.030|
|**17**|47.120|88.105|27.740|36.765|27.887|6.840|136|955|7.694|6.933|39.520|45.030|
|**18**|47.120|85.826|27.740|36.765|23.680|5.985|136|955|2.238|7.098|39.520|45.030|
|**19**|47.120|87.092|27.740|36.765|20.842|5.173|136|955|2.238|5.612|38.828|40.077|
|**20**|47.120|56.711|27.740|36.765|17.515|4.403|136|955|2.238|2.971|29.245|29.607|
|**21**|46.531|37.976|27.740|34.651|16.635|3.249|136|955|2.238|825|17.290|26.005|
|**22**|39.934|31.394|23.995|27.666|15.656|3.078|136|955|2.238|660|14.721|22.965|
|**23**|36.047|22.786|17.199|24.081|15.656|2.009|136|955|2.238|660|14.128|18.800|
|**24**|46.060|39.242|23.302|23.713|14.286|1.710|136|955|2.238|4.292|14.721|26.568|

34 En caso de que en algún mes no se haya muestreado un pabellón con el rango de edad indicado, se consideró el valor más alto del mes.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 33 de 74

**Tabla No 26** . Tasa de emisión pabellón N°4. [ 35]

|Col1|Emisión de olor Pabellón N°4|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**Enero**<br>|**Febrero**|**Marzo**<br>|**Abril**|**Mayo**<br>|**Junio**|**Julio**<br>|**Agosto**|**Septiembre**|**Octubre**|**Noviembre**|**Diciembre**|
|**Edad**|**175-182**|**28-56**|**56-91**|**91-119**|**119-147**|**147-182**|**182**|**35-70**|**70-98**|**98-126**|**126-161**|**161-182**|
|**1 **|36.871|42.402|20.944|23.070|14.188|1.710|3.595|955|2.238|3.962|13.634|22.177|
|**2 **|31.453|39.814|19.141|21.875|14.971|1.710|3.513|955|2.238|3.962|12.646|19.813|
|**3 **|28.743|37.102|15.951|19.669|13.895|1.710|3.885|955|2.238|3.962|12.449|18.913|
|**4 **|27.212|37.718|13.778|18.658|12.525|1.710|3.885|955|2.238|3.962|11.955|17.224|
|**5 **|26.269|26.008|12.575|16.636|11.742|1.710|3.761|955|2.238|3.962|10.374|15.535|
|**6 **|23.324|37.595|10.125|15.901|8.709|1.710|3.967|955|2.238|3.962|12.646|13.959|
|**7 **|25.563|33.281|9.224|16.636|9.100|1.710|3.361|955|2.238|3.962|15.512|17.111|
|**8 **|40.405|14.545|11.165|19.669|10.861|1.710|3.637|955|2.238|3.962|16.895|28.932|
|**9 **|47.120|15.654|15.951|23.346|14.678|1.710|3.595|955|2.238|3.962|36.062|36.925|
|**10**|47.120|15.778|23.579|27.390|16.537|1.710|3.141|955|2.238|3.962|36.260|44.580|
|**11**|47.120|15.778|27.185|34.467|20.255|4.574|3.141|955|2.238|3.962|2.371|45.030|
|**12**|47.120|16.106|27.740|36.765|25.930|7.225|3.141|955|11.191|13.645|39.520|45.030|
|**13**|47.120|16.271|25.382|36.765|29.159|8.465|3.141|955|19.165|41.101|39.520|45.030|
|**14**|47.120|16.271|27.185|36.765|33.367|9.662|3.141|955|24.900|57.607|39.520|45.030|
|**15**|47.120|14.915|27.740|36.765|36.694|10.132|3.141|955|26.019|62.229|39.520|45.030|
|**16**|47.120|16.271|27.740|36.765|32.388|8.849|3.141|955|20.284|34.663|39.520|45.030|
|**17**|47.120|16.640|27.740|36.765|27.887|6.840|3.141|955|7.694|6.933|39.520|45.030|
|**18**|47.120|16.764|27.740|36.765|23.680|5.985|3.141|955|2.238|7.098|39.520|45.030|
|**19**|47.120|16.764|27.740|36.765|20.842|5.173|3.141|955|2.238|5.612|38.828|40.077|
|**20**|47.120|16.764|27.740|36.765|17.515|4.403|3.141|955|2.238|2.971|29.245|29.607|
|**21**|46.531|11.505|27.740|34.651|16.635|3.249|3.141|955|2.238|825|17.290|26.005|
|**22**|39.934|17.133|23.995|27.666|15.656|3.078|3.141|955|2.238|660|14.721|22.965|
|**23**|36.047|17.257|17.199|24.081|15.656|2.009|3.141|955|2.238|660|14.128|18.800|
|**24**|46.060|46.100|23.302|23.713|14.286|1.710|3.637|955|2.238|4.292|14.721|26.568|

35 En caso de que en algún mes no se haya muestreado un pabellón con el rango de edad indicado, se consideró el valor más alto del mes.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 34 de 74

**Tabla No 27** . Tasa de emisión pabellón N°5. [ 36]

|Col1|Emisión de olor Pabellón N°5|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**Enero**|**Febrero**|**Marzo**<br>|**Abril**|**Mayo**<br>|**Junio**|**Julio**|**Agosto**|**Septiembre**<br>|**Octubre**|**Noviembre**|**Diciembre**|
|**Edad**|**168-182**|**21-49**|**49-84**|**84-112**|**112-140**|**140-175**|**175-182**|**28-63**|**63-91**|**91-119**|**119-154**|**154-182**|
|**1 **|36.871|42.402|20.944|23.070|14.188|1.710|3.595|955|2.238|3.962|13.634|22177|
|**2 **|31.453|39.814|19.141|21.875|14.971|1.710|3.513|955|2.238|3.962|12.646|19813|
|**3 **|28.743|37.102|15.951|19.669|13.895|1.710|3.885|955|2.238|3.962|12.449|18913|
|**4 **|27.212|37.718|13.778|18.658|12.525|1.710|3.885|955|2.238|3.962|11.955|17224|
|**5 **|26.269|26.008|12.575|16.636|11.742|1.710|3.761|955|2.238|3.962|10.374|15535|
|**6 **|23.324|37.595|10.125|15.901|8.709|1.710|3.967|955|2.238|3.962|12.646|13959|
|**7 **|25.563|33.281|9.224|16.636|9.100|1.710|3.361|955|2.238|3.962|15.512|17.111|
|**8 **|40.405|14.545|11.165|19.669|10.861|1.710|3.637|955|2.238|3.962|16.895|28.932|
|**9 **|47.120|15.654|15.951|23.346|14.678|1.710|3.595|955|2.238|3.962|36.062|36.925|
|**10**|47.120|15.778|23.579|27.390|16.537|1.710|3.141|955|2.238|3.962|36.260|44.580|
|**11**|47.120|15.778|27.185|34.467|20.255|4.574|3.141|955|2.238|3.962|2.371|45.030|
|**12**|47.120|16.106|27.740|36.765|25.930|7.225|3.141|955|11.191|13.645|39.520|45.030|
|**13**|47.120|16.271|25.382|36.765|29.159|8.465|3.141|955|19.165|41.101|39.520|45.030|
|**14**|47.120|16.271|27.185|36.765|33.367|9.662|3.141|955|24.900|57.607|39.520|45.030|
|**15**|47.120|14.915|27.740|36.765|36.694|10.132|3.141|955|26.019|62.229|39.520|45.030|
|**16**|47.120|16.271|27.740|36.765|32.388|8.849|3.141|955|20.284|34.663|39.520|45.030|
|**17**|47.120|16.640|27.740|36.765|27.887|6.840|3.141|955|7.694|6.933|39.520|45.030|
|**18**|47.120|16.764|27.740|36.765|23.680|5.985|3.141|955|2.238|7.098|39.520|45.030|
|**19**|47.120|16.764|27.740|36.765|20.842|5.173|3.141|955|2.238|5.612|38.828|40.077|
|**20**|47.120|16.764|27.740|36.765|17.515|4.403|3.141|955|2.238|2.971|29.245|29.607|
|**21**|46.531|11.505|27.740|34.651|16.635|3.249|3.141|955|2.238|825|17.290|26.005|
|**22**|39.934|17.133|23.995|27.666|15.656|3.078|3.141|955|2.238|660|14.721|22.965|
|**23**|36.047|17.257|17.199|24.081|15.656|2.009|3.141|955|2.238|660|14.128|18.800|
|**24**|46.060|46.100|23.302|23.713|14.286|1.710|3.637|955|2.238|4.292|14.721|26.568|

36 En caso de que en algún mes no se haya muestreado un pabellón con el rango de edad indicado, se consideró el valor más alto del mes.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 35 de 74

**Tabla No 28** . Tasa de emisión pabellón N°6. [ 37]

|Col1|Emisión de olor Pabellón N°6|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**Enero**|**Febrero**|**Marzo**<br>|**Abril**|**Mayo**<br>|**Junio**|**Julio**<br>|**Agosto**|**Septiembre**<br>|**Octubre**|**Noviembre**<br>|**Diciembre**|
|**Edad**|**161-182**|**21-42**|**42-77**|**77-105**|**105-133**|**133-168**|**168-182**|**21-56**|**56-84**|**84-112**|**112-147**|**147-182**|
|**1 **|36.871|42.402|7.219|11.837|14.188|1.710|3.595|252|2.238|3.962|13.634|22.177|
|**2 **|31.453|39.814|6.822|11.172|14.971|1.710|3.513|252|2.238|3.962|12.646|19.813|
|**3 **|28.743|37.102|6.029|8.246|13.895|1.710|3.885|252|2.238|3.962|12.449|18.913|
|**4 **|27.212|37.718|5.553|10.640|12.525|1.710|3.885|252|2.238|3.962|11.955|17.224|
|**5 **|26.269|26.008|4.997|11.172|11.742|1.710|3.761|252|2.238|3.962|10.374|15.535|
|**6 **|23.324|37.595|4.284|9.443|8.709|1.710|3.967|252|2.238|3.962|12.646|13.959|
|**7 **|25.563|33.281|3.570|9.310|9.100|1.710|3.361|252|2.238|3.962|15.512|17.111|
|**8 **|40.405|14.545|2.538|7.847|10.861|1.710|3.637|252|2.238|3.962|16.895|28.932|
|**9 **|47.120|15.654|3.094|9.709|14.678|1.710|3.595|252|2.238|3.962|36.062|36.925|
|**10**|47.120|15.778|2.776|13.433|16.537|1.710|3.141|252|2.238|3.962|36.260|44.580|
|**11**|47.120|15.778|4.839|20.216|20.255|4.574|3.141|252|2.238|3.962|2.371|45.030|
|**12**|47.120|16.106|5.791|33.782|25.930|7.225|3.141|252|11.191|13.645|39.520|45.030|
|**13**|47.120|16.271|7.774|49.077|29.159|8.465|3.141|252|19.165|41.101|39.520|45.030|
|**14**|47.120|16.271|7.933|53.200|33.367|9.662|3.141|252|24.900|57.607|39.520|45.030|
|**15**|47.120|14.915|7.933|53.200|36.694|10.132|3.141|252|26.019|62.229|39.520|45.030|
|**16**|47.120|16.271|7.933|53.200|32.388|8.849|3.141|252|20.284|34.663|39.520|45.030|
|**17**|47.120|16.640|7.933|53.200|27.887|6.840|3.141|252|7.694|6.933|39.520|45.030|
|**18**|47.120|16.764|7.933|47.082|23.680|5.985|3.141|252|2.238|7.098|39.520|45.030|
|**19**|47.120|16.764|7.933|32.585|20.842|5.173|3.141|252|2.238|5.612|38.828|40.077|
|**20**|47.120|16.764|7.933|23.541|17.515|4.403|3.141|252|2.238|2.971|29.245|29.607|
|**21**|46.531|11.505|7.853|18.487|16.635|3.249|3.141|252|2.238|825|17.290|26.005|
|**22**|39.934|17.133|7.139|15.960|15.656|3.078|3.141|252|2.238|660|14.721|22.965|
|**23**|36.047|17.257|6.187|16.492|15.656|2.009|3.141|252|2.238|660|14.128|18.800|
|**24**|46.060|46.100|7.298|10.241|14.286|1.710|3.637|252|2.238|4.292|14.721|26.568|

37 En caso de que en algún mes no se haya muestreado un pabellón con el rango de edad indicado, se consideró el valor más alto del mes.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 36 de 74

**Tabla No 29** . Tasa de emisión pabellón N°7. [ 38]

|Col1|Emisión de olor Pabellón N°7|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**Enero**<br>|**Febrero**<br>|**Marzo**<br>|**Abril**<br>|**Mayo**<br>|**Junio**|**Julio**<br>|**Agosto**|**Septiembre**|**Octubre**|**Noviembre**|**Diciembre**|
|**Edad**|**154-182**|**182**|**35-70**|**70-98**|**98-126**|**126-161**|**161-182**|**21-49**|**49-77**|**77-105**|**105-140**|**140-175**|
|**1 **|36.871|62.066|7.219|11.837|16.046|1.710|3.595|252|2.238|6.504|5.310|22.177|
|**2 **|31.453|51.067|6.822|11.172|19.333|1.710|3.513|252|2.238|6.504|4.848|19.813|
|**3 **|28.743|48.710|6.029|8.246|19.333|1.710|3.885|252|2.238|6.504|4.001|18.913|
|**4 **|27.212|45.175|5.553|10.640|13.919|1.710|3.885|252|2.238|6.504|3.386|17.224|
|**5 **|26.269|39.872|4.997|11.172|14.499|1.710|3.761|252|2.238|6.504|2.924|15.535|
|**6 **|23.324|40.068|4.284|9.443|13.919|1.710|3.967|252|2.238|6.504|3.078|13.959|
|**7 **|25.563|37.515|3.570|9.310|17.786|1.710|3.361|252|2.238|6.504|4.771|17.111|
|**8 **|40.405|54.799|2.538|7.847|13.919|1.710|3.637|252|2.238|6.504|7.310|28.932|
|**9 **|47.120|76.012|3.094|9.709|12.953|1.710|3.595|252|2.238|6.504|12.312|36.925|
|**10**|47.120|78.565|2.776|13.433|13.533|1.710|3.141|252|2.238|6.504|17.083|44.580|
|**11**|47.120|78.565|4.839|20.216|24.166|4.574|3.141|252|2.238|6.504|22.854|45.030|
|**12**|47.120|78.565|5.791|33.782|27.259|7.225|3.141|252|11.191|6.504|26.009|45.030|
|**13**|47.120|78.565|7.774|49.077|34.219|8.465|3.141|252|19.165|18.427|30.395|45.030|
|**14**|47.120|78.565|7.933|53.200|42.532|9.662|3.141|252|24.900|40.106|30.780|45.030|
|**15**|47.120|78.565|7.933|53.200|52.391|10.132|3.141|252|26.019|59.617|30.780|45.030|
|**16**|47.120|78.565|7.933|53.200|45.818|8.849|3.141|252|20.284|86.716|30.780|45.030|
|**17**|47.120|78.565|7.933|53.200|37.698|6.840|3.141|252|7.694|69.373|30.780|45.030|
|**18**|47.120|78.565|7.933|47.082|26.679|5.985|3.141|252|2.238|51.488|30.780|45.030|
|**19**|47.120|78.565|7.933|32.585|23.392|5.173|3.141|252|2.238|36.312|29.472|40.077|
|**20**|47.120|78.565|7.933|23.541|19.526|4.403|3.141|252|2.238|14.633|21.623|29.607|
|**21**|46.531|71.494|7.853|18.487|23.779|3.249|3.141|252|2.238|6.504|14.544|26.005|
|**22**|39.934|58.531|7.139|15.960|17.399|3.078|3.141|252|2.238|6.504|13.235|22.965|
|**23**|36.047|50.674|6.187|16.492|19.139|2.009|3.141|252|2.238|6.504|11.619|18.800|
|**24**|46.060|73.655|7.298|10.241|19.333|1.710|3.637|252|2.238|6.504|6.772|26.568|

38 En caso de que en algún mes no se haya muestreado un pabellón con el rango de edad indicado, se consideró el valor más alto del mes.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 37 de 74

**Tabla No 30** . Tasa de emisión pabellón N°8. [ 39]

|Col1|Emisión de olor Pabellón N°8|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**Enero**<br>|**Febrero**|**Marzo**<br>|**Abril**|**Mayo**<br>|**Junio**|**Julio**<br>|**Agosto**|**Septiembre**<br>|**Octubre**|**Noviembre**<br>|**Diciembre**|
|**Edad**|**147-175**|**175-182**|**28-63**|**63-91**|**91-119**|**119-154**|**154-182**|**182**|**42-70**|**70-98**|**98-133**|**133-168**|
|**1 **|36.871|62.066|7.219|11.837|16.046|10.750|3.595|4.554|1.545|6.504|5.310|22.177|
|**2 **|31.453|51.067|6.822|11.172|19.333|8.102|3.513|4.286|1.545|6.504|4.848|19.813|
|**3 **|28.743|48.710|6.029|8.246|19.333|11.373|3.885|4.019|1.545|6.504|4.001|18.913|
|**4 **|27.212|45.175|5.553|10.640|13.919|8.413|3.885|3.483|1.545|6.504|3.386|17.224|
|**5 **|26.269|39.872|4.997|11.172|14.499|11.062|3.761|5.269|1.545|6.504|2.924|15.535|
|**6 **|23.324|40.068|4.284|9.443|13.919|6.154|3.967|5.537|1.545|6.504|3.078|13.959|
|**7 **|25.563|37.515|3.570|9.310|17.786|10.594|3.361|5.090|1.545|6.504|4.771|17.111|
|**8 **|40.405|54.799|2.538|7.847|13.919|9.582|3.637|5.894|1.545|6.504|7.310|28.932|
|**9 **|47.120|76.012|3.094|9.709|12.953|10.517|3.595|6.965|1.545|6.504|12.312|36.925|
|**10**|47.120|78.565|2.776|13.433|13.533|13.633|3.141|8.305|1.545|6.504|17.083|44.580|
|**11**|47.120|78.565|4.839|20.216|24.166|17.761|3.141|11.163|1.545|6.504|22.854|45.030|
|**12**|47.120|78.565|5.791|33.782|27.259|19.631|3.141|11.163|1.545|6.504|26.009|45.030|
|**13**|47.120|78.565|7.774|49.077|34.219|20.644|3.141|12.145|1.545|18.427|30.395|45.030|
|**14**|47.120|78.565|7.933|53.200|42.532|22.747|3.141|12.591|1.545|40.106|30.780|45.030|
|**15**|47.120|78.565|7.933|53.200|52.391|21.189|3.141|11.877|1.545|59.617|30.780|45.030|
|**16**|47.120|78.565|7.933|53.200|45.818|19.397|3.141|11.698|1.545|86.716|30.780|45.030|
|**17**|47.120|78.565|7.933|53.200|37.698|17.060|3.141|11.252|1.545|69.373|30.780|45.030|
|**18**|47.120|78.565|7.933|47.082|26.679|15.346|3.141|11.252|1.545|51.488|30.780|45.030|
|**19**|47.120|78.565|7.933|32.585|23.392|14.256|3.141|11.341|1.545|36.312|29.472|40.077|
|**20**|47.120|78.565|7.933|23.541|19.526|14.022|3.141|10.627|1.545|14.633|21.623|29.607|
|**21**|46.531|71.494|7.853|18.487|23.779|14.645|3.141|10.002|1.545|6.504|14.544|26.005|
|**22**|39.934|58.531|7.139|15.960|17.399|16.047|3.141|10.537|1.545|6.504|13.235|22.965|
|**23**|36.047|50.674|6.187|16.492|19.139|16.982|3.141|10.091|1.545|6.504|11.619|18.800|
|**24**|46.060|73.655|7.298|10.241|19.333|9.738|3.637|5.090|1.545|6.504|6.772|26.568|

39 En caso de que en algún mes no se haya muestreado un pabellón con el rango de edad indicado, se consideró el valor más alto del mes.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 38 de 74

**Tabla No 31** . Tasa de emisión pabellón N°9. [ 40]

|Col1|Emisión de olor Pabellón N°9|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**Enero**<br>|**Febrero**|**Marzo**<br>|**Abril**|**Mayo**<br>|**Junio**|**Julio**<br>|**Agosto**|**Septiembre**<br>|**Octubre**|**Noviembre**<br>|**Diciembre**|
|**Edad**|**140-168**|**168-182**|**21-56**|**56-84**|**84-112**|**112-147**|**147-175**|**175-182**|**35-63**|**63-91**|**91-126**|**126-161**|
|**1 **|36.871|62.066|7.219|11.837|16.046|10.750|3.595|4.554|1.545|6.504|5.310|22.177|
|**2 **|31.453|51.067|6.822|11.172|19.333|8.102|3.513|4.286|1.545|6.504|4.848|19.813|
|**3 **|28.743|48.710|6.029|8.246|19.333|11.373|3.885|4.019|1.545|6.504|4.001|18.913|
|**4 **|27.212|45.175|5.553|10.640|13.919|8.413|3.885|3.483|1.545|6.504|3.386|17.224|
|**5 **|26.269|39.872|4.997|11.172|14.499|11.062|3.761|5.269|1.545|6.504|2.924|15.535|
|**6 **|23.324|40.068|4.284|9.443|13.919|6.154|3.967|5.537|1.545|6.504|3.078|13.959|
|**7 **|25.563|37.515|3.570|9.310|17.786|10.594|3.361|5.090|1.545|6.504|4.771|17.111|
|**8 **|40.405|54.799|2.538|7.847|13.919|9.582|3.637|5.894|1.545|6.504|7.310|28.932|
|**9 **|47.120|76.012|3.094|9.709|12.953|10.517|3.595|6.965|1.545|6.504|12.312|36.925|
|**10**|47.120|78.565|2.776|13.433|13.533|13.633|3.141|8.305|1.545|6.504|17.083|44.580|
|**11**|47.120|78.565|4.839|20.216|24.166|17.761|3.141|11.163|1.545|6.504|22.854|45.030|
|**12**|47.120|78.565|5.791|33.782|27.259|19.631|3.141|11.163|1.545|6.504|26.009|45.030|
|**13**|47.120|78.565|7.774|49.077|34.219|20.644|3.141|12.145|1.545|18.427|30.395|45.030|
|**14**|47.120|78.565|7.933|53.200|42.532|22.747|3.141|12.591|1.545|40.106|30.780|45.030|
|**15**|47.120|78.565|7.933|53.200|52.391|21.189|3.141|11.877|1.545|59.617|30.780|45.030|
|**16**|47.120|78.565|7.933|53.200|45.818|19.397|3.141|11.698|1.545|86.716|30.780|45.030|
|**17**|47.120|78.565|7.933|53.200|37.698|17.060|3.141|11.252|1.545|69.373|30.780|45.030|
|**18**|47.120|78.565|7.933|47.082|26.679|15.346|3.141|11.252|1.545|51.488|30.780|45.030|
|**19**|47.120|78.565|7.933|32.585|23.392|14.256|3.141|11.341|1.545|36.312|29.472|40.077|
|**20**|47.120|78.565|7.933|23.541|19.526|14.022|3.141|10.627|1.545|14.633|21.623|29.607|
|**21**|46.531|71.494|7.853|18.487|23.779|14.645|3.141|10.002|1.545|6.504|14.544|26.005|
|**22**|39.934|58.531|7.139|15.960|17.399|16.047|3.141|10.537|1.545|6.504|13.235|22.965|
|**23**|36.047|50.674|6.187|16.492|19.139|16.982|3.141|10.091|1.545|6.504|11.619|18.800|
|**24**|46.060|73.655|7.298|10.241|19.333|9.738|3.637|5.090|1.545|6.504|6.772|26.568|

40 En caso de que en algún mes no se haya muestreado un pabellón con el rango de edad indicado, se consideró el valor más alto del mes.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 39 de 74

**Tabla No 32** . Tasa de emisión pabellón N°10. [ 41]

|Col1|Emisión de olor Pabellón N°10|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**Enero**<br>|**Febrero**|**Marzo**<br>|**Abril**|**Mayo**<br>|**Junio**|**Julio**<br>|**Agosto**|**Septiembre**<br>|**Octubre**|**Noviembre**<br>|**Diciembre**|
|**Edad**|**133-161**|**161-182**|**21-49**|**49-77**|**77-105**|**105-140**|**140-168**|**168-182**|**28-56**|**56-84**|**84-119**|**119-154**|
|**1 **|36.871|62.066|7.219|11.837|16.046|10.750|3.595|4.554|1.545|6.504|5.310|22.177|
|**2 **|31.453|51.067|6.822|11.172|19.333|8.102|3.513|4.286|1.545|6.504|4.848|19.813|
|**3 **|28.743|48.710|6.029|8.246|19.333|11.373|3.885|4.019|1.545|6.504|4.001|18.913|
|**4 **|27.212|45.175|5.553|10.640|13.919|8.413|3.885|3.483|1.545|6.504|3.386|17.224|
|**5 **|26.269|39.872|4.997|11.172|14.499|11.062|3.761|5.269|1.545|6.504|2.924|15.535|
|**6 **|23.324|40.068|4.284|9.443|13.919|6.154|3.967|5.537|1.545|6.504|3.078|13.959|
|**7 **|25.563|37.515|3.570|9.310|17.786|10.594|3.361|5.090|1.545|6.504|4.771|17.111|
|**8 **|40.405|54.799|2.538|7.847|13.919|9.582|3.637|5.894|1.545|6.504|7.310|28.932|
|**9 **|47.120|76.012|3.094|9.709|12.953|10.517|3.595|6.965|1.545|6.504|12.312|36.925|
|**10**|47.120|78.565|2.776|13.433|13.533|13.633|3.141|8.305|1.545|6.504|17.083|44.580|
|**11**|47.120|78.565|4.839|20.216|24.166|17.761|3.141|11.163|1.545|6.504|22.854|45.030|
|**12**|47.120|78.565|5.791|33.782|27.259|19.631|3.141|11.163|1.545|6.504|26.009|45.030|
|**13**|47.120|78.565|7.774|49.077|34.219|20.644|3.141|12.145|1.545|18.427|30.395|45.030|
|**14**|47.120|78.565|7.933|53.200|42.532|22.747|3.141|12.591|1.545|40.106|30.780|45.030|
|**15**|47.120|78.565|7.933|53.200|52.391|21.189|3.141|11.877|1.545|59.617|30.780|45.030|
|**16**|47.120|78.565|7.933|53.200|45.818|19.397|3.141|11.698|1.545|86.716|30.780|45.030|
|**17**|47.120|78.565|7.933|53.200|37.698|17.060|3.141|11.252|1.545|69.373|30.780|45.030|
|**18**|47.120|78.565|7.933|47.082|26.679|15.346|3.141|11.252|1.545|51.488|30.780|45.030|
|**19**|47.120|78.565|7.933|32.585|23.392|14.256|3.141|11.341|1.545|36.312|29.472|40.077|
|**20**|47.120|78.565|7.933|23.541|19.526|14.022|3.141|10.627|1.545|14.633|21.623|29.607|
|**21**|46.531|71.494|7.853|18.487|23.779|14.645|3.141|10.002|1.545|6.504|14.544|26.005|
|**22**|39.934|58.531|7.139|15.960|17.399|16.047|3.141|10.537|1.545|6.504|13.235|22.965|
|**23**|36.047|50.674|6.187|16.492|19.139|16.982|3.141|10.091|1.545|6.504|11.619|18.800|
|**24**|46.060|73.655|7.298|10.241|19.333|9.738|3.637|5.090|1.545|6.504|6.772|26.568|

41 En caso de que en algún mes no se haya muestreado un pabellón con el rango de edad indicado, se consideró el valor más alto del mes.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 40 de 74

**Tabla No 33** . Tasa de emisión pabellón N°11. [ 42]

|Col1|Emisión de olor Pabellón N°11|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**Enero**|**Febrero**<br>|**Marzo**|**Abril**<br>|**Mayo**|**Junio**|**Julio**<br>|**Agosto**|**Septiembre**<br>|**Octubre**|**Noviembre**<br>|**Diciembre**|
|**Edad**|**126-154**|**154-182**|**182**|**42-70**|**70-98**|**98-133**|**133-161**|**161-182**|**21-49**|**49-77**|**77-112**|**112-140**|
|**1 **|36.871|62.066|39.330|11.837|16.046|10.750|3.595|4.554|1.545|6.504|5.310|22.177|
|**2 **|31.453|51.067|38.937|11.172|19.333|8.102|3.513|4.286|1.545|6.504|4.848|19.813|
|**3 **|28.743|48.710|33.922|8.246|19.333|11.373|3.885|4.019|1.545|6.504|4.001|18.913|
|**4 **|27.212|45.175|29.498|10.640|13.919|8.413|3.885|3.483|1.545|6.504|3.386|17.224|
|**5 **|26.269|39.872|26.744|11.172|14.499|11.062|3.761|5.269|1.545|6.504|2.924|15.535|
|**6 **|23.324|40.068|22.811|9.443|13.919|6.154|3.967|5.537|1.545|6.504|3.078|13.959|
|**7 **|25.563|37.515|21.435|9.310|17.786|10.594|3.361|5.090|1.545|6.504|4.771|17.111|
|**8 **|40.405|54.799|23.795|7.847|13.919|9.582|3.637|5.894|1.545|6.504|7.310|28.932|
|**9 **|47.120|76.012|32.152|9.709|12.953|10.517|3.595|6.965|1.545|6.504|12.312|36.925|
|**10**|47.120|78.565|38.445|13.433|13.533|13.633|3.141|8.305|1.545|6.504|17.083|44.580|
|**11**|47.120|78.565|39.330|20.216|24.166|17.761|3.141|11.163|1.545|6.504|22.854|45.030|
|**12**|47.120|78.565|39.330|33.782|27.259|19.631|3.141|11.163|1.545|6.504|26.009|45.030|
|**13**|47.120|78.565|39.330|49.077|34.219|20.644|3.141|12.145|1.545|18.427|30.395|45.030|
|**14**|47.120|78.565|39.330|53.200|42.532|22.747|3.141|12.591|1.545|40.106|30.780|45.030|
|**15**|47.120|78.565|39.330|53.200|52.391|21.189|3.141|11.877|1.545|59.617|30.780|45.030|
|**16**|47.120|78.565|39.330|53.200|45.818|19.397|3.141|11.698|1.545|86.716|30.780|45.030|
|**17**|47.120|78.565|39.330|53.200|37.698|17.060|3.141|11.252|1.545|69.373|30.780|45.030|
|**18**|47.120|78.565|39.330|47.082|26.679|15.346|3.141|11.252|1.545|51.488|30.780|45.030|
|**19**|47.120|78.565|39.330|32.585|23.392|14.256|3.141|11.341|1.545|36.312|29.472|40.077|
|**20**|47.120|78.565|39.330|23.541|19.526|14.022|3.141|10.627|1.545|14.633|21.623|29.607|
|**21**|46.531|71.494|39.330|18.487|23.779|14.645|3.141|10.002|1.545|6.504|14.544|26.005|
|**22**|39.934|58.531|39.330|15.960|17.399|16.047|3.141|10.537|1.545|6.504|13.235|22.965|
|**23**|36.047|50.674|39.330|16.492|19.139|16.982|3.141|10.091|1.545|6.504|11.619|18.800|
|**24**|46.060|73.655|39.330|10.241|19.333|9.738|3.637|5090|1.545|6.504|6.772|26.568|

42 En caso de que en algún mes no se haya muestreado un pabellón con el rango de edad indicado, se consideró el valor más alto del mes.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 41 de 74

**Tabla No 34** . Tasa de emisión pabellón N°12. [ 43]

|Col1|Emisión de olor Pabellón N°12|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**Enero**<br>|**Febrero**|**Marzo**<br>|**Abril**|**Mayo**<br>|**Junio**|**Julio**<br>|**Agosto**|**Septiembre**<br>|**Octubre**|**Noviembre**<br>|**Diciembre**|
|**Edad**|**119-147**|**147-175**|**175-182**|**35-63**|**63-91**|**91-126**|**126-154**|**154-182**|**21-42**|**42-70**|**70-105**|**105-133**|
|**1 **|36.871|62.066|39.330|11.837|16.046|10.750|3.595|4.554|1.545|6.504|2.354|22.177|
|**2 **|31.453|51.067|38.937|11.172|19.333|8.102|3.513|4.286|1.545|6.504|2.354|19.813|
|**3 **|28.743|48.710|33.922|8.246|19.333|11.373|3.885|4.019|1.545|6.504|2.354|18.913|
|**4 **|27.212|45.175|29.498|10.640|13.919|8.413|3.885|3.483|1.545|6.504|2.354|17.224|
|**5 **|26.269|39.872|26.744|11.172|14.499|11.062|3.761|5.269|1.545|6.504|2.354|15.535|
|**6 **|23.324|40.068|22.811|9.443|13.919|6.154|3.967|5.537|1.545|6.504|2.354|13.959|
|**7 **|25.563|37.515|21.435|9.310|17.786|10.594|3.361|5.090|1.545|6.504|2.354|17.111|
|**8 **|40.405|54.799|23.795|7.847|13.919|9.582|3.637|5.894|1.545|6.504|2.354|28.932|
|**9 **|47.120|76.012|32.152|9.709|12.953|10.517|3.595|6.965|1.545|6.504|2.354|36.925|
|**10**|47.120|78.565|38.445|13.433|13.533|13.633|3.141|8.305|1.545|6.504|2.354|44.580|
|**11**|47.120|78.565|39.330|20.216|24.166|17.761|3.141|11.163|1.545|6.504|7.455|45.030|
|**12**|47.120|78.565|39.330|33.782|27.259|19.631|3.141|11.163|1.545|6.504|13.928|45.030|
|**13**|47.120|78.565|39.330|49.077|34.219|20.644|3.141|12.145|1.545|18.427|28.445|45.030|
|**14**|47.120|78.565|39.330|53.200|42.532|22.747|3.141|12.591|1.545|40.106|33.742|45.030|
|**15**|47.120|78.565|39.330|53.200|52.391|21.189|3.141|11.877|1.545|59.617|37.273|45.030|
|**16**|47.120|78.565|39.330|53.200|45.818|19.397|3.141|11.698|1.545|86.716|50.613|45.030|
|**17**|47.120|78.565|39.330|53.200|37.698|17.060|3.141|11.252|1.545|69.373|46.493|45.030|
|**18**|47.120|78.565|39.330|47.082|26.679|15.346|3.141|11.252|1.545|51.488|38.058|45.030|
|**19**|47.120|78.565|39.330|32.585|23.392|14.256|3.141|11.341|1.545|36.312|25.110|40.077|
|**20**|47.120|78.565|39.330|23.541|19.526|14.022|3.141|10.627|1.545|14.633|8.043|29.607|
|**21**|46.531|71.494|39.330|18.487|23.779|14.645|3.141|10.002|1.545|6.504|2.354|26.005|
|**22**|39.934|58.531|39.330|15.960|17.399|16.047|3.141|10.537|1.545|6.504|2.354|22.965|
|**23**|36.047|50.674|39.330|16.492|19.139|16.982|3.141|10.091|1.545|6.504|2.354|18.800|
|**24**|46.060|73.655|39.330|10.241|19.333|9.738|3.637|5.090|1.545|6.504|2.354|26.568|

43 En caso de que en algún mes no se haya muestreado un pabellón con el rango de edad indicado, se consideró el valor más alto del mes.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 42 de 74

**5.2.3 Resumen de emisiones**

A continuación, se presenta el resumen de las emisiones generadas por fuente en el plantel de
cerdos El Charco.

**Tabla No 35** . Emisiones promedio del plantel de cerdos El Charco.

|Fuente|Emisión<br>(OU /s)<br>E|
|---|---|
|Pabellones de cerdos|245.063|
|Zona de Transferencia|3.728|
|Laguna de Acumulación|130.169|
|Zona de Riego|672.313|

En la siguiente figura, se presenta la distribución porcentual de las emisiones de olor del plantel
de cerdos.

**Figura No 6** . Fuentes consideradas en el estudio.

En la figura anterior se puede observar la distribución de las emisiones de olor generadas en el
plantel de cerdos El Charco, el 64% de las emisiones se generan en la zona de riego, un 23%
en los pabellones de cerdos, un 13% en la laguna de acumulación y un 0,1% en la zona de
transferencia.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 43 de 74

**Evaluación de la dispersión de olores del plantel de cerdos**

En el presente apartado se presentan los resultados de la dispersión de las emisiones de olores
generadas en el plantel de cerdos El Charco, según las fuentes mencionadas en el punto 5.1
del presente estudio. Los resultados muestran la pluma de dispersión de los olores en torno al
plantel, las cuales, además de simular la dispersión de los gases, entregan las concentraciones
de olor (OU E /m [3] ) en el espacio.

Se presenta una cartografía de dispersión de olor, la que registra el percentil 98 de las
concentraciones horarias, con el objetivo de poder comparar los resultados con el límite de 8
OU E /m [3] establecido en la norma de los Países Bajos.

A continuación, se presentan los resultados de la evaluación del modelo de dispersión de las
fuentes del plantel de cerdos.

**5.3.1 Resultados emisión de olor del plantel**

**5.3.1.1 Dispersión de emisiones**

El límite de referencia indicado en la norma de los Países Bajos establece un valor de 8 OU E /m [3]
para periodos horarios con percentil 98.

Tal como se puede apreciar en la siguiente cartografía, la distribución de la pluma se acentúa
hacia el noreste con una longitud aproximada de 4,93 km. Las isodoras pueden alcanzar valores
entre 1,0 a 53 OU E /m [3] alcanzando su mayor concentración en la zona de riego ubicada al
suroeste de los pabellones. Fuera de los límites del plantel las isodoras trazan valores entre 1,0
a 8 OU E /m [3] . Se observa que la isodora de 8 OU E /m [3 ] no circunscribe ningún receptor sensible.

La isodora de 8 OU E /m3 alcanza una superficie aproximada de 1,94 km [2] alrededor de los
pabellones, zona de riego y zona de transferencia.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 44 de 74

**Figura No 7** . Mapa de concentración de olor generado por las fuentes de emisión del plantel

de cerdos. Promedio horario (percentil 98).

Con base en la dispersión de emisiones del escenario evaluado, se determinó un área de
influencia definida según la “Guía para la predicción y evaluación de impactos por olor en el
SEIA” [44], como el espacio contenido por la isodora de 1 OU E /m [3], que corresponde al umbral de
detección del olor compuesto. En la siguiente figura se presenta el área de influencia
determinada.

44 Publicada el 2017 por el Servicio de Evaluación Ambiental.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 45 de 74

**Figura No 8** . Área de Influencia del plantel de cerdos.

La isodora de 1 OU E /m3, valor que indica la concentración desde el cual el 50% de la población
puede percibir un olor, cubre una superficie de 9,52 km [2] . La distribución de la pluma se acentúa
en sentido noreste con una longitud aproximada de 4,93 km.

Como se mencionó anteriormente, el área de influencia, determinada por la curva de isoconcentración de 1 OU E /m3, se circunscribe hacia el noreste de los pabellones. El área de
influencia circunscribe a un receptor (R11 y R34).

La máxima concentración se produce al interior del predio, específicamente en la zona de riego
alcanzando una concentración de 53 OU E /m [3] .

**Tabla No 36** . Máxima concentración del plantel de cerdos.

|Descripción|UTM 19H - WGS84|Col3|Concentración de<br>inmisión<br>(OU /m3)<br>E|
|---|---|---|---|
|**Descripción**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|Predio plantel de cerdos El Charco|270.603|6.106.343|53|

Inf03E02.O-21-049.EIO.Plantel.El.Charco 46 de 74

**5.3.1.2 Receptores discretos considerados en la modelación**

A continuación, se presentan los receptores considerados en la modelación.

**Tabla No 37** . Receptores identificados en la caracterización de receptores.

|No|Proyección UTM Huso 19S<br>Datum WGS84|Col3|Distancia al plantel (km)|
|---|---|---|---|
|**No**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|R1|271.665|6.104.222|2,65|
|R2|270.853|6.104.814|2,02|
|R3|269.718|6.104.321|2,88|
|R4|269.532|6.104.116|3,14|
|R5|269.272|6.104.046|3,34|
|R6|268.659|6.104.444|3,43|
|R7|268.697|6.105.533|2,76|
|R8|269.540|6.106.691|1,59|
|R9|268.705|6.107.041|2,44|
|R10|270.034|6.107.479|1,28|
|R11|270.735|6.107.654|0,93|
|R12|270.627|6.109.346|2,58|
|R13|270.734|6.109.318|2,54|
|R14|273.056|6.113.648|7,10|
|R15|273.488|6.113.649|7,24|
|R16|274.803|6.113.898|7,98|
|R17|269.841|6.109.504|2,98|
|R18|275.923|6.113.158|7,97|
|R19|275.050|6.111.847|6,42|
|R20|282.813|6.109.812|12,07|
|R21|282.777|6.108.622|11,80|
|R22|272.221|6.103.516|3,46|
|R23|271.907|6.104.103|2,81|
|R24|268.185|6.106.844|2,94|
|R25|268.114|6.106.497|3,03|
|R26|269.745|6.109.590|3,11|
|R27|269.676|6.109.405|2,98|
|R28|268.801|6.108.552|2,91|
|R29|268.522|6.108.276|2,99|
|R30|268.296|6.108.249|3,18|
|R31|268.145|6.108.216|3,30|
|R32|275.405|6.114.012|8,37|
|R33|269.328|6.109.305|0,14|
|R34|271.240|6.106.154|-|

Inf03E02.O-21-049.EIO.Plantel.El.Charco 47 de 74

**Figura No 9** . Receptores de interés analizados.

En la siguiente tabla, se presenta el resultado del Percentil 98 de las concentraciones horarias
para cada receptor identificado.

Tal como se puede apreciar en la siguiente tabla, la operación del plantel generaría
concentraciones de inmisión por debajo del límite establecido en la norma de los Países Bajos
(8 OU E /m [3] ).

Inf03E02.O-21-049.EIO.Plantel.El.Charco 48 de 74

**Tabla No 38** . Concentración receptores. Percentil 98.

|No|Concentración de<br>inmisión<br>(OU /m3)<br>E|Horas al año<br>>8 OU /m3<br>E|Límite de inmisión<br>Norma de los Países<br>Bajos|
|---|---|---|---|
|R1|0,22|0 (0,00%)|8|
|R2|0,35|0 (0,00%)|0 (0,00%)|
|R3|0,19|0 (0,00%)|0 (0,00%)|
|R4|0,16|0 (0,00%)|0 (0,00%)|
|R5|0,14|0 (0,00%)|0 (0,00%)|
|R6|0,10|0 (0,00%)|0 (0,00%)|
|R7|0,12|0 (0,00%)|0 (0,00%)|
|R8|0,23|0 (0,00%)|0 (0,00%)|
|R9|0,12|0 (0,00%)|0 (0,00%)|
|R10|0,59|3 (0,03%)|3 (0,03%)|
|R11|1,59|8 (0,09%)|8 (0,09%)|
|R12|0,46|0 (0,00%)|0 (0,00%)|
|R13|0,52|0 (0,00%)|0 (0,00%)|
|R14|0,23|0 (0,00%)|0 (0,00%)|
|R15|0,23|0 (0,00%)|0 (0,00%)|
|R16|0,22|0 (0,00%)|0 (0,00%)|
|R17|0,20|0 (0,00%)|0 (0,00%)|
|R18|0,20|0 (0,00%)|0 (0,00%)|
|R19|0,26|0 (0,00%)|0 (0,00%)|
|R20|0,04|0 (0,00%)|0 (0,00%)|
|R21|0,05|0 (0,00%)|0 (0,00%)|
|R22|0,17|0 (0,00%)|0 (0,00%)|
|R23|0,22|0 (0,00%)|0 (0,00%)|
|R24|0,10|0 (0,00%)|0 (0,00%)|
|R25|0,10|0 (0,00%)|0 (0,00%)|
|R26|0,18|0 (0,00%)|0 (0,00%)|
|R27|0,18|0 (0,00%)|0 (0,00%)|
|R28|0,11|0 (0,00%)|0 (0,00%)|
|R29|0,09|0 (0,00%)|0 (0,00%)|
|R30|0,08|0 (0,00%)|0 (0,00%)|
|R31|0,08|0 (0,00%)|0 (0,00%)|
|R32|0,21|0 (0,00%)|0 (0,00%)|
|R33|0,14|0 (0,00%)|0 (0,00%)|
|R34|2,15|22 (0,25%)|22 (0,25%)|

En el Anexo N°2 se presenta el análisis de la variación horaria del olor en los receptores
cercanos que presentaron valores más altos de concentración.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 49 de 74

**5.3.1.3 Frecuencia de percepción de olor**

**Figura No 10** . Mapa de horas sobre 8 OU E /m3 generado por las fuentes de emisión del plantel

de cerdos. Promedio horario (percentil 98).

En la figura anterior se puede observar las horas al año sobre las 8 OU E /m3. Dicha figura indica
que los lugares sobre un 2% de frecuencia (176 horas), se encuentran superior a la excedencia
entregada por el percentil 98 (en verde oscuro, verde claro, amarillo, naranjo y rojo). Las zonas
al interior de esta curva corresponden a sectores al interior del plantel (alrededor de los
pabellones, zona de transferencia y de la zona de riego), territorio que no se encuentra habitado.
Todas las viviendas cercanas (indicadas por una cruz amarilla, receptores) se encuentran bajo
las 176 horas sobre 8 OU E /m3, lo que indica que ninguna zona usada como residencia supera
el 2% de horas por sobre el umbral de molestia.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 50 de 74

**5.3.1.4 Análisis FIDOL**

**Tabla No 39.** Protocolo FIDOL con base a receptores definidos.

|Parámetro|Con respecto a receptores discretos.|
|---|---|
|Frecuencia|El plantel operará durante todos los días del año. Sin embargo, durante el 98% de las<br>horas del año no se prevé superación de las 8 OUE/m3. Los eventos de superación son<br>puntuales sin observarse una frecuencia constante.|
|Intensidad|Ningún receptor se encuentra sobre las 8 unidades de olor (8 OUE/m3) en el percentil<br>98.|
|Duración|En cuanto a la duración, la superación de 8 OUE/m3 ocurre en eventos puntuales en<br>periodos no continuos durante el año. No obstante, las concentraciones no afectan a la<br>población debido a que ningún receptor supera el umbral de 8 OUE/m3 bajo el percentil<br>98.|
|Ofensividad|A pesar de que los olores del plantel presentan una intensidad fuerte y un tono hedónico<br>que varía de moderadamente desagradable a desagradable, la combinación de<br>frecuencia, duración e intensidad no representaría ofensividad.|
|Localización|El territorio circunscrito al Área de Influencia presenta un uso principalmente de carácter<br>rural por lo que se encuentra fuera del plan regulador de la comuna de Sagrada Familia.|

Inf03E02.O-21-049.EIO.Plantel.El.Charco 51 de 74

**Análisis del desempeño del archivo de pronóstico utilizado**

La “Guía para el Uso de Modelos de Calidad de Aire en el SEIA en su capítulo 7” requiere que
se realice una comparación de los registros WRF con información meteorológica local. Para
ello se utilizan los datos disponibles de las estaciones de monitoreo ubicadas en la zona de
interés para el estudio.

La estación utilizada corresponde a Curicó del Sistema Nacional de Calidad del Aire (SINCA) a
32 km del plantel de cerdos. Esta estación presenta datos de temperatura, dirección y velocidad
de viento, las que serán utilizadas para validar el modelo meteorológico de pronóstico WRF, no

siendo usadas como entradas al modelo.

En el Anexo N°3 se presentan las variables meteorológicas y geofísicas del emplazamiento del
plantel y en el Anexo No4 se presenta una comparación cualitativa y cuantitativa entre la
meteorología de pronóstico y los datos observados en la estación meteorológica.

De acuerdo con las comparaciones realizadas en forma cualitativa de ciclo diario, promedio
mensual rosa de los vientos y ciclos estacionales, para los parámetros temperatura, velocidad
y dirección de viento para la estación Curicó se puede indicar que tanto el modelo WRF y los
datos observados presentan valores y patrones similares, que permiten indicar que los datos
del archivo WRF se ajustan a la realidad y pueden ser utilizados en la modelación.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 52 de 74

**Figura No 11** . Estación Meteorológica utilizada en el Análisis de Incertidumbre.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 53 de 74

**6** **Conclusiones**

Con respecto a la modelación de dispersión de olores del plantel de cerdos el Charco, se
concluye lo siguiente:

1. Las curvas de isoconcentración del percentil 98, indican que las concentraciones de olor

producidas en los alrededores del plantel varían entre 1,0 y 53 OU E /m [3], presentándose
la máxima concentración dentro del plantel, entre la zona de riego ubicada al sureste de
los pabellones, con un valor de 53 OU E /m [3] . Fuera de los límites del predio las
concentraciones alcanzan valores entre 1,0 y 8 OU E /m [3] .

2. En el escenario evaluado no se presenta superación del límite de 8 OU E /m [3] (percentil

98) en ninguno de los receptores identificados. El receptor que presenta la
concentración más alta es el receptor 34 (R34) alcanzando una concentración de 2,15
OU E /m [3] .

3. El área de influencia, descrita por la isodora de 1 OU E /m [3], circunscribe a los pabellones,

laguna de acumulación, zona de riego y zona de transferencia. El área de influencia
cubre una superficie de 9,52 km [2] y presenta una longitud de 4,93 km en sentido noreste
y circunscribe a dos receptores (R11 y R34).

4. Con base al modelo de dispersión de emisiones del plantel de cerdos, se puede indicar

que no se presenta superación del límite de 8 OU E /m [3] (percentil 98) en ningún receptor

sensible.

En relación con la validación meteorológica del modelo de pronóstico WRF:

5. Se puede concluir a partir del análisis cualitativo y cuantitativo, que el modelo de

pronóstico WRF presenta valores de temperatura, dirección y velocidad de viento
similares a los datos observados. Al analizar las velocidades promedio y direcciones
frecuentes del viento, los valores modelados concuerdan con los datos observados. Por
lo tanto, de acuerdo con lo presentado en el análisis cuantitativo y cualitativo de la
estación Curicó, el modelo WRF utilizado para el análisis de dispersión atmosférica es
adecuado y concuerda con las condiciones de la realidad.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 54 de 74

**7** **Anexos**

**Anexo No1. Esquema de funcionamiento Calpuff y elementos de modelación**

El presente Anexo contiene el archivo magnético el cual presenta la información que se utilizó
para realizar la modelación atmosférica, dicha información corresponde a los input y output
ingresados para la modelación de los módulos del modelo (CALPUFF, CALPOST y CALRANK)
y el archivo Meteorológico WRF.

Por lo tanto, en el caso de que se requiera replicar la modelación realizada, esta se podrá hacer
utilizando los archivos presentes en este Anexo.

**Figura No 12** . Esquema funcionamiento CALPUFF.

Estructuras y efecto downwash.

La dispersión de emisiones descargadas por chimeneas puede ser afectada por la presencia
de edificios cercanos que representan obstáculos a la circulación del aire, como se muestra en
la siguiente figura:

Inf03E02.O-21-049.EIO.Plantel.El.Charco 55 de 74

**Figura No 13** . Esquema efecto downwash.

Se aprecia una zona viento arriba, donde el viento es influenciado por la alta presión
desarrollada en la pared del edificio que enfrenta el viento, una zona de cavidad con
recirculación viento abajo, alta turbulencia y baja velocidad del viento, y una estela turbulenta,
donde las propiedades del flujo y de la turbulencia se van aproximando continuamente a los
valores ambientales de la circulación del viento lejos del edificio.

Los algoritmos de cálculo utilizados por CALPUFF provienen de la formulación original de ISC3,
y se usan 36 sectores angulares para caracterizar las dimensiones que el viento ‘ve’ en cada
edificio según la dirección que trae. El módulo BPIP (Building Profile Input Program) se utilizó
para determinar esas dimensiones de manera automática.

En la siguiente figura (en azul) se presentan las edificaciones significativas del plantel de cerdos
que fueron consideradas para evaluar su efecto sobre la dispersión de las emisiones de olor,
mientras que en la tabla se adjuntan las alturas y dimensiones de las edificaciones.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 56 de 74

**Figura No 14** . Esquema de los pabellones modelados .

**Figura No 15** . Esquema de la zona de transferencia.

**T** **abla No 40** . Dimensiones de los pabellones.

|Pabellón|Altura (m)|Longitud X (m)|Longitud Y (m)|
|---|---|---|---|
|Recría-finalización|2,4|105|13,1|
|Zona Transferencia|2,4|44,8|12,6|

Inf03E02.O-21-049.EIO.Plantel.El.Charco 57 de 74

**Figura No 16** . Zona de riego modelada.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 58 de 74

**Anexo No2. Análisis de receptores.**

A continuación, se presentan los gráficos ciclo diario de las concentraciones de olor, para los
tres receptores que presentaron la concentración más alta (R11 y R34). Estos gráficos permiten
detectar las horas en donde ocurren las mayores concentraciones durante el día, respecto al
90% observado del tiempo (variación entre el percentil 5 y percentil 95).

**Receptor 11**

**Figura No 17** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No11.

En la figura anterior se muestra, el comportamiento de las concentraciones de olor durante el
día. Acá se puede observar que los mayores valores se presentan entre las 08:00 y las 17:00
hrs, la mayor concentración se presenta a las 17:00 hrs y alcanza las 2,5 OU E /m3.

**Receptor 34**

**Figura No 18** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No34.

En la figura anterior se muestra, el comportamiento de las concentraciones de olor durante el
día. Acá se puede observar que los mayores valores se presentan entre las 08:00 y las 17:00
hrs, con una concentración máxima de 2,9 OU E /m3.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 59 de 74

**Anexo No3. Descripción meteorológica y geofísica de la zona**

En el siguiente anexo se presenta el análisis de la meteorología de la zona modelada. Los datos
expresados a continuación fueron extraídos por la plataforma SINCA (Sistema de Información
Nacional de Calidad del Aire), específicamente de la estación de monitoreo Curicó.

**Tabla No 41.** Datos de la estación meteorológica considerada.

|Estación Meteorológica|Col2|Curicó|
|---|---|---|
|Coordenada UTM Datum WGS 84|Zona|19H|
|Coordenada UTM Datum WGS 84|Este (m)|296.068|
|Coordenada UTM Datum WGS 84|Norte (m)|6.127.456|
|"Periodo del registro<br>(desde DD/MM/AA - hasta DD/MM/AA)"|"Periodo del registro<br>(desde DD/MM/AA - hasta DD/MM/AA)"|01/01/2020 hasta 31/12/2020|
|Distancia desde el Plantel (km)|Distancia desde el Plantel (km)|32|
|Meteorología|Meteorología|Velocidad del Viento (VV)<br>Dirección del Viento (DV)<br>Temperatura (TA)|

**7.3.1 Cantidad de datos**

Para realizar el análisis meteorológico y el análisis de incertidumbre es necesario verificar la
cantidad de datos presentes en las mediciones ambientales de las estaciones. A continuación,
se muestran los datos de las estaciones en la serie de tiempo para comprobar que no existen
periodos extensos sin datos durante el año de análisis.

**Estación Curicó:**

**Figura No 19.** Serie de tiempo velocidad del viento - datos observados estación Curicó - año

2020.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 60 de 74

**Figura No 20.** Serie de tiempo dirección del viento - datos observados estación Curicó - año

2020.

**Figura No 21.** Serie de tiempo temperatura - datos observados estación Curicó - año 2020.

**Tabla No 42.** Datos válidos estación meteorológica Curicó.

|Porcentaje de datos meteorológicos disponibles - EM Curicó|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Pará/mes|E|F|M|A|M|J|J|A|S|O|N|D|**Total**|
|VV|99%|100%|100%|100%|100%|99%|100%|100%|100%|100%|100%|97%|**100%**|
|DV|99%|100%|100%|100%|100%|99%|100%|100%|100%|100%|100%|97%|**100%**|
|T|99%|100%|100%|100%|100%|99%|100%|100%|100%|100%|100%|97%|**100%**|

La estación Curicó posee una cantidad de datos mínima de 97%, durante el mes de diciembre,
para las variables temperatura, velocidad y dirección del viento, lo que es superior al 75%
sugerido por la Guía para modelos de calidad del aire del SEA.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 61 de 74

**7.3.2 Gráficos Ciclo diario**

En los siguientes gráficos se presentan los ciclos diarios promedios de temperatura, velocidad
y dirección del viento; junto con su variabilidad entre el percentil 5% a 95% (Rango 90%
observado).

Velocidad de viento

**Figura No 22.** Ciclo diario para velocidad de viento Curicó.

En relación con el ciclo diario promedio de la velocidad del viento, de la estación Curicó, se
observa una velocidad promedio mínima de 1,0 m/s durante la mañana y una velocidad máxima
promedio de 2,2 m/s en las horas de la tarde. Durante el año, la velocidad del viento puede
variar entre calmas y 4,0 m/s en el rango de 90% observado.

Dirección del viento

**Figura No 23.** Ciclo diario para dirección del viento estación Curicó.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 62 de 74

En relación con el ciclo diario de la dirección de viento de la estación Curicó, se observa que
durante todo el día predominan los vientos provenientes desde el sur y en menor frecuencia
desde el suroeste; dicha condición indica que los gases se dispersan hacia el norte y hacia el

noreste.

Temperatura

**Figura No 24.** Ciclo diario para temperatura estación Curicó.

Respecto al ciclo diario de la temperatura, en la estación Curicó, se observa una temperatura
promedio variable de 10°C a 23°C.

La temperatura máxima ocurre a las 17:00 horas mientras que la mínima sucede a las 08:00
horas. Durante el año, la temperatura puede variar en ±10°C respecto al promedio, alcanzando
máximas de 34 °C y mínimas de 2°C, respecto al 90% observado.

**7.3.3 Gráfico Distribución de Vientos**

La siguiente figura muestra la distribución de los vientos en la estación: Curicó. De aquí se
puede concluir que los periodos de calma representan un 7,8%, las velocidades de viento que
van entre 0,5 y 2,1 m/s representan un 66,4% y finalmente las velocidades que van entre 2,1 y
3,6 m/s representan un 23% del total. Las condiciones favorecen la dispersión del olor generada
por el plantel de cerdos.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 63 de 74

**Figura No 25.** Distribución velocidades de viento estación Curicó.

**7.3.4 Rosa de los vientos**

De la rosa de los vientos anual, realizada para la estación Curicó, se puede concluir que el
viento predominante proviene desde el suroeste y sur, alcanzando una frecuencia de un 20%.
Cabe destacar que los vientos alcanzan una velocidad que va entre periodos de calma y 5,7
m/s.

**Figura No 26.** Rosa de los vientos Anual. Estación Curicó.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 64 de 74

**Por estación**

En los gráficos siguientes se muestra una comparación de las rosas de los vientos para cada
estación del año.

 - En otoño los vientos provienen principalmente desde el sur y suroeste, seguidos en
menor frecuencia por los vientos provenientes desde el noreste. Cabe destacar que las
velocidades promedio alcanzan los 3,6 y 5,7 m/s, por lo que en este periodo la dispersión
de emisiones se da principalmente al norte y noreste.

 En invierno los vientos tienen un comportamiento similar al otoño. Cabe destacar que
las velocidades promedio pueden alcanzar los 3,6 y 5,7 m/s en menor proporción.

 - En primavera y verano, los vientos provienen desde el suroeste principalmente
alcanzando una frecuencia de un 25% en primavera y 19% en verano. Cabe destacar
que las mayores velocidades del viento pueden alcanzar entre 3,6 y 5,7 m/s,
favoreciendo la dispersión de los gases hacia el noreste.

En los gráficos siguientes se muestran las rosas de los vientos para cada estación del año.

(a) Otoño - EM Curicó 2020. (b) Invierno - EM Curicó 2020.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 65 de 74

(c) Primavera - EM Curicó 2020. (d) Verano - EM Curicó 2020.
**Figura No 27.** Rosas de los vientos por estación del año.

**7.3.5 Gráficos ciclo estacional**

En el siguiente gráfico, se observa la variación estacional de los ciclos de velocidad y dirección
de viento. En relación a la dirección de viento en los meses de primavera y verano, se mantiene
el ciclo diario con vientos desde el sur y suroeste durante todo el día, mientras que en los meses
de junio y julio predominan la inestabilidad con vientos provenientes desde el sur y norte.

Respecto a la velocidad del viento, durante las horas del día en primavera y verano ocurren las
mayores velocidades, las que pueden alcanzar los 3,5 m/s mientras que en horas de la noche
se presentan velocidades del viento inferior a 1,5 m/s en los datos observados. En invierno las
velocidades fluctúan entre 1m/s en la noche y 1,5 m/s en la tarde.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 66 de 74

**Figura No 28.** Ciclo estacional - datos observados estación Curicó - Año 2020. [45]

**7.3.6 Elevación de Terreno**

La zona modelada corresponde a un sector ubicado en Villa Prat perteneciente a la comuna
Sagrada Familia ubicada en la zona costera, específicamente en el secano interior de la
provincia de Curicó, región del Maule. El plantel de cerdos Villa Prat se emplaza entre los 200
y 300 msnm, es importante señalar que la comuna más cercana ubicada al noreste del plantel
corresponde a Sagrada Familia.

45 Las flechas indican hacia donde se dirige el viento.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 67 de 74

**Figura No 29.** Elevación de terreno archivo WRF.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 68 de 74

**Anexo No4. Análisis incertidumbre**

La “Guía para el Uso de Modelos de Calidad de Aire en el SEIA en su capítulo 7” requiere que
se realice una comparación de los registros WRF con información meteorológica local. Para
ello se utilizan los datos disponibles en las estaciones de monitoreo ubicadas en la zona de
interés para el estudio.

La estación meteorológica analizada (Curicó) se encuentran a 32 km al noreste del plantel de
cerdos. Los parámetros monitoreados por dicha estación corresponden a radiación global,
humedad, temperatura, velocidad y dirección del viento. Para la evaluación del desempeño se
realiza una comparación entre las variables temperatura, velocidad y dirección de viento, ya
que éstas son las variables de mayor interés.

Con el fin de evaluar el desempeño, se realiza un análisis cualitativo de los parámetros de
interés mediante la comparación de los ciclos diarios promedios, mensuales, ciclos estacionales
y rosas de los vientos.

Definiciones

**Datos observados:** Se refiere a los datos provenientes desde una estación de monitoreo
durante un periodo de interés.

**Datos modelados:** Se refiere a los datos meteorológicos provenientes desde un modelo de
pronóstico como WRF o MM5.

**Rango 90% observado:** Se refiere a la variación de los datos entre el percentil 5 y percentil 95
en una hora o mes específico.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 69 de 74

**7.4.1 Ciclos Diarios promedios**

Velocidad del viento

**Figura No 30.** Comparación ciclo diario de velocidad del viento entre datos observados y

proyectados para la estación de Curicó.

De la figura anterior se puede concluir que el ciclo diario promedio de velocidad del viento entre
los datos observados y los datos modelados presenta valores similares con una diferencia de
±1 m/s en el WRF en comparación a los datos observados en la estación meteorológica Curicó.
Se puede concluir que los datos presentan una variación diaria de velocidad con un patrón
similar en el modelo de pronóstico y el observado.

Dirección del Viento

**Figura No 31.** Comparación ciclo diario de dirección de viento entre datos observados y

proyectados para la estación de Curicó.

De la figura anterior se puede concluir que la moda diaria de dirección del viento entre los datos
observados y los datos modelados presentan valores con diferencias de ± 45° en promedio.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 70 de 74

Dado estas circunstancias, respecto a la moda diaria de dirección de viento, el modelo se
considera adecuado.

Temperatura

**Figura No 32.** Comparación ciclo diario de temperatura entre los datos observados y

proyectados para la estación de Curicó.

De las figuras anteriores, se puede concluir que el ciclo diario promedio de temperatura entre
los datos observados y los datos modelados presentan valores similares con una diferencia de
±2°C. Además, la variación diaria de temperatura posee el mismo patrón del modelo de
pronóstico y el observado. Dado estas circunstancias, respecto al ciclo diario promedio de
temperatura, el modelo es adecuado.

**7.4.2 Promedio Mensuales**

Velocidad del viento

**Figura No 33.** Comparación moda mensual de velocidad de viento entre datos observados y

proyectados para la estación de Curicó.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 71 de 74

De la figura anterior se puede concluir que el promedio mensual de velocidad de viento entre
los datos observados y los datos modelados presentan una tendencia similar, sin embargo, se
observa una sobreestimación de ±1 m/s en los datos modelados en comparación a los datos
observados en la estación Curicó.

Dirección del Viento

**Figura No 34.** Comparación moda mensual de dirección del viento entre datos observados y

proyectados para la estación de Curicó.

De las figuras anteriores se puede concluir que la moda mensual de dirección del viento entre
los datos observados y los datos modelados presentan valores similares la mayor parte del año,
con una diferencia de ± 45° en promedio. Dado estas circunstancias, respecto a la moda
mensual de dirección de viento, el modelo se considera adecuado.

Temperatura

**Figura No 35.** Comparación moda mensual de temperatura entre los datos observados y

proyectados para la estación de Curicó.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 72 de 74

De la figura anterior, se puede concluir que los promedios mensuales de temperatura entre los
datos observados y los datos modelados presentan una tendencia similar, sin embargo, se
observa una subestimación de ±2°C en los datos modelados en comparación a los observados.
Dado estas circunstancias, respecto al promedio mensual de temperatura, el modelo se

considera adecuado.

**7.4.3 Dirección del viento**

Rosas de los vientos

(a) EM Curicó - OBS (b) EM Curicó - WRF
**Figura No 36.** Comparación Rosas de viento.

De las rosas de los vientos mostradas, se puede observar que en la estación meteorológica
Curicó predominan los vientos provenientes desde el sur y suroeste. En general el modelo y los
datos observados son similares incluyendo la frecuencia de las velocidades del viento. El
modelo presenta un patrón similar de viento por lo que se puede indicar que el modelo es
adecuado.

**7.4.4 Análisis cuantitativo**

El análisis de los registros de temperatura, dirección y velocidad del viento fue realizado
comparado los ciclos diarios, ciclos estacionales, gráficos de distribución y rosas de los vientos.
Además, se realizó un análisis numérico de los promedios diarios de acuerdo con las
recomendaciones de la guía EPA para el uso de modelos numéricos del tiempo en Calpuff [46],
cuyos resultados se presentan en la siguiente tabla:

46 PRELIMINARY Deaft Users Manual, The MMIFstat Statistical Analysis Package. Sección 2.2.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 73 de 74

**Tabla No 43.** Análisis cuantitativo.

|Parámetro|Variable Estadística|Curicó|Col4|
|---|---|---|---|
|**Parámetro**|**Variable Estadística**|**Horario**|**Diario**|
|**Velocidad del viento**|** RMSE**|1,02 m/s|0,70 m/s|
|**Velocidad del viento**|**BIAS**|0,40 m/s|0,40 m/s|
|**Dirección del viento**|**BIAS**|5,27°|6,51°|
|**Temperatura**|**BIAS**|-2,33 K|-2,34 K|

**Conclusión**

A partir del análisis cualitativo (ciclo diario, promedio mensual, rosa de los vientos y ciclos
estacionales) y cuantitativo, se puede concluir que los datos de pronóstico WRF y datos
observados presentan valores similares para las velocidades promedio, direcciones frecuentes
y temperatura ambiente. Por lo tanto, de acuerdo a lo presentado en el análisis de la estación
meteorológica Curicó, el modelo WRF utilizado en la dispersión atmosférica es adecuado y

concuerda con las condiciones de la realidad.

Inf03E02.O-21-049.EIO.Plantel.El.Charco 74 de 74