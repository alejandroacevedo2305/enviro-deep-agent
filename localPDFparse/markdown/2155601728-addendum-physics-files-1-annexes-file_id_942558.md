---
title: Sin título
author: Users-Pre-Installed
date: D:20211012151222-03'00'
language: es
type: report
pages: 67
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME Estudio de Impacto Odorante “Plantel de Cerdos Monte Verde Bajo” 12 de octubre del 2021 Inf04E01.O-21-027
-->

# INFORME Estudio de Impacto Odorante “Plantel de Cerdos Monte Verde Bajo” 12 de octubre del 2021 Inf04E01.O-21-027

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 1 de 67

## Datos del Proyecto

**Empresa** **:** Agrícola y Forestal Las Astas S.A.
Agrícola Coexca S.A.

**Plantel** **:** Plantel Monte Verde Bajo

**Coordinador** **:** Rienzi Catalán - Agrícola Coexca S.A.
César Contreras - Agrícola Coexca S.A.
María Paz Pérez - Agrícola Coexca S.A.

**Jefe de Proyecto** **:** Miguel Gatica Rivera (MGR).
Claudio Burdiles Melgarejo (CBM).

**Ingeniero de Proyecto** **:** Carolina Freire Ávila (CFA).

**Fecha** **:** 12 de octubre del 2021.

|Emisión|Datos|Preparó|Revisó|Aprobó|
|---|---|---|---|---|
|RevA. Para<br>Revisión Cliente|Nombre|CFA|CBM|CBM|
|RevA. Para<br>Revisión Cliente|Fecha|12-10-2021|12-10-2021|12-10-2021|

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 2 de 67

**Índice General**

**1** **Resumen ............................................................................................................................. 7**

**2** **Introducción ..................................................................................................................... 10**

**3** **Objetivo General .............................................................................................................. 11**

Objetivos específicos .................................................................................................. 11
**4** **Metodología ...................................................................................................................... 11**

Caracterización de las fuentes de emisión de olor. ..................................................... 11

Estimación de concentración y emisiones de olor ....................................................... 12
Evaluación de la dispersión de las emisiones de olor. ................................................. 14

4.3.1 Selección del modelo ....................................................................................... 14

4.3.2 Recopilación de los antecedentes para la modelación ..................................... 15

4.3.3 Variables meteorológicas y geofísicas ............................................................. 16

4.3.4 Evaluación de los resultados ........................................................................... 17

4.3.5 Área de Influencia. ........................................................................................... 19

Evaluación del desempeño del archivo de pronóstico utilizado ................................... 19
**5** **Resultados ....................................................................................................................... 19**

Caracterización de las fuentes de emisión .................................................................. 19

Emisiones de olor ........................................................................................................ 22

5.2.1 Emisiones muestreadas plantel de cerdos Monte Verde Bajo. Campaña
Invierno. ...................................................................................................................... 22

5.2.2 Factores utilizados para el cálculo de emisión ................................................. 24

5.2.3 Emisiones del plantel Monte Verde Bajo. Campaña Invierno ........................... 24

5.2.4 Características y Emisiones de las fuentes ingresadas en el modelo .............. 26

5.2.5 Emisiones de las fuentes ingresadas en el modelo .......................................... 28

Evaluación de la dispersión de olor del plantel de cerdos ........................................... 31

5.3.1 Resultados emisión de olor generada en el plantel de cerdos. ........................ 31

Análisis del desempeño del archivo de pronóstico utilizado ........................................ 36
**6** **Conclusiones ................................................................................................................... 38**

**7** **Anexos .............................................................................................................................. 39**

Anexo No1. Esquema de funcionamiento Calpuff y elementos de modelación ............ 39
Anexo No2. Cálculo del flujo de los pabellones. ........................................................... 40
Anexo No3. Descripción meteorológica y geofísica de la zona .................................... 41

7.3.1 Cantidad de datos ............................................................................................ 41

7.3.2 Gráficos Ciclo diario ......................................................................................... 44

7.3.3 Gráficos Distribución de Vientos ...................................................................... 47

7.3.4 Rosa de los vientos ......................................................................................... 49

7.3.5 Gráficos ciclo estacional .................................................................................. 52

7.3.6 Elevación de Terreno ....................................................................................... 53

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 3 de 67

Anexo No4. Análisis incertidumbre .............................................................................. 55

7.4.1 Ciclos Diarios promedios ................................................................................. 56

7.4.2 Promedio Mensuales ....................................................................................... 59

7.4.3 Dirección de viento .......................................................................................... 62

7.4.4 Análisis cuantitativo ......................................................................................... 65

Anexo No4. Análisis de receptores. ............................................................................. 66

**Índice de Tablas**

**Tabla No 1** . Emisiones de olor. Campaña de Invierno. ............................................................. 7
**Tabla No 2** . Concentración receptores. Percentil 98. ................................................................ 8
**Tabla No 3.** Distribución de la toma de muestra en fuentes difusas pasivas de área. ............. 13
**Tabla No 4.** Distribución de la toma de muestra en fuentes difusas pasivas de volumen. ....... 14
**Tabla No 5** . Variables de entrada consideradas en la modelación. ......................................... 15
**Tabla No 6** . Campañas de muestreo y modelación. ................................................................ 15
**Tabla No 7.** Características del archivo meteorológico WRF. ................................................. 16
**Tabla No 8.** Receptores discretos considerados en la modelación. ........................................ 18
**Tabla No 9** . Descripción fuentes generadoras de olor del plantel de Cerdos - Monte Verde
Bajo. ....................................................................................................................................... 20
**Tabla No 10.** Emisión de olor en fuentes difusas pasivas de Volumen. .................................. 23
**Tabla No 11.** Emisión de olor en fuentes difusas pasivas de área. ......................................... 23
**Tabla No 12.** Factores de emisión por pabellón. ..................................................................... 24
**Tabla No 13.** Emisión de olor en fuentes difusas pasivas de Volumen. .................................. 24
**Tabla No 14.** Emisión de olor en fuentes difusas pasivas de área. ......................................... 25
**Tabla No 15** . Cortinas pabellones. .......................................................................................... 26
**Tabla No 16** . Procedencia de las concentraciones consideradas en el modelo. ..................... 28
**Tabla No 17** . Emisión por pabellón. ........................................................................................ 29
**Tabla No 18** . Emisión por fuente. ............................................................................................ 30
**Tabla No 19** . Emisión de olor zona de aplicación de purín tratado y laguna de acumulación. . 30
**Tabla No 20** . Edad de las pilas, septiembre 2021. .................................................................. 31
**Tabla No 21** . Punto de máxima concentración. ....................................................................... 34
**Tabla No 22** . Concentración receptores. Percentil 98. ............................................................ 34
**Tabla No 23.** Protocolo FIDOL en base a receptores definidos. .............................................. 36
**Tabla No 24.** Flujo considerado en los pabellones. ................................................................. 40
**Tabla No 25.** Datos meteorológicos. ....................................................................................... 41
**Tabla No 26.** Datos válidos estación meteorológica Los Ángeles Oriente. .............................. 43
**Tabla No 27.** Datos válidos estación meteorológica Progreso. ............................................... 44
**Tabla No 28.** Análisis cuantitativo. .......................................................................................... 65

**Índice de Figuras**

**Figura No 1** . Concentración de olor generada por las fuentes del plantel de cerdos................. 9
**Figura No 2** . Área del estudio de impacto odorante. ............................................................... 10
**Figura No 3** . Diagrama metodología de caracterización de olor. ............................................ 13
**Figura No 4** . Ubicación de receptores discretos. .................................................................... 18
**Figura No 5** . Diagrama de proceso aprobado en escenario futuro RCA N°068/2019. ............. 20
**Figura No 6** . Fuentes consideradas en el estudio. .................................................................. 22
**Figura No 7** . Distribución emisiones de olor. .......................................................................... 26

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 4 de 67

**Figura No 8** . Concentración de olor generada por las fuentes del plantel de cerdos............... 32
**Figura No 9** . Área de Influencia del plantel de cerdos. ............................................................ 33
**Figura No 10** . Horas sobre 8 OU E /m3 generadas por las fuentes de emisión del plantel de
cerdos. Promedio horario (percentil 98). ................................................................................. 35
**Figura No 11** . Estación Meteorológica utilizada en el Análisis de Incertidumbre. .................... 37
**Figura No 12** . Esquema funcionamiento CALPUFF. ............................................................... 39
**Figura No 13** . Serie de tiempo anual para velocidad de viento. Estación Los Ángeles Oriente.
............................................................................................................................................... 41
**Figura No 14** . Serie de tiempo anual para dirección de viento. Estación Los Ángeles Oriente.
............................................................................................................................................... 42
**Figura No 15** . Serie de tiempo anual para temperatura. Estación Los Ángeles Oriente. ......... 42
**Figura No 16** . Serie de tiempo anual para velocidad de viento. Estación Progreso. ............... 43
**Figura No 17** . Serie de tiempo anual para dirección de viento. Estación Progreso. ................ 43
**Figura No 18** . Serie de tiempo anual para temperatura. Estación Progreso. .......................... 44
**Figura No 19** . Ciclo diario velocidad viento - datos observados estación Los Ángeles Oriente
- Año 2014. ............................................................................................................................ 45
**Figura No 20** . Ciclo diario velocidad viento - datos observados estación Progreso- Año 2014.
............................................................................................................................................... 45
**Figura No 21** . Ciclo diario dirección viento - datos observados estación Los Ángeles OrienteAño 2014. ............................................................................................................................... 46
**Figura No 22** . Ciclo diario dirección viento - datos observados estación Progreso - Año 2014.
............................................................................................................................................... 46
**Figura No 23** . Ciclo diario temperatura - datos observados estación Los Ángeles OrienteAño 2014. ............................................................................................................................... 47
**Figura No 24** . Ciclo diario temperatura - datos observados estación Progreso - Año 2014. .. 47
**Figura No 25** . Distribución de vientos - datos observados estación Los Ángeles Oriente - Año
2014. ...................................................................................................................................... 48
**Figura No 26** . Distribución de vientos - datos observados estación Progreso - Año 2014. .... 48
**Figura No 27** . Rosa de los vientos - datos observados estación Los Ángeles Oriente - Año
2014. ...................................................................................................................................... 49
**Figura No 28** . Rosa de los vientos - datos observados estación Progreso - Año 2014. ......... 49
**Figura No 29** . Rosa de los vientos por estación. ..................................................................... 51
**Figura No 30** . Ciclos estacionales - datos observados estación Los Ángeles Oriente - Año
2014. ...................................................................................................................................... 52
**Figura No 31** . Ciclos estacionales - datos observados estación Progreso - Año 2014. ......... 53
**Figura No 32** . Elevación de terreno WRF. .............................................................................. 54
**Figura No 33** . Comparación ciclo diario de velocidad de viento entre modelación observada y
proyectada para la estación Los Ángeles Oriente. .................................................................. 56
**Figura No 34** . Comparación ciclo diario de velocidad de viento entre modelación observada y
proyectada para la estación Progreso. ................................................................................... 56
**Figura No 35** . Comparación ciclo diario de dirección de viento entre modelación observada y
proyectada para la estación Los Ángeles Oriente. .................................................................. 57
**Figura No 36** . Comparación ciclo diario de dirección de viento entre modelación observada y
proyectada para la estación Progreso. ................................................................................... 57
**Figura No 37** . Comparación ciclo diario de temperatura entre modelación observada y
proyectada para la estación Los Ángeles Oriente. .................................................................. 58
**Figura No 38** . Comparación ciclo diario de temperatura entre modelación observada y
proyectada para la estación Progreso. ................................................................................... 58

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 5 de 67

**Figura No 39** . Comparación promedio mensual de velocidad de viento entre modelación
observada y proyectada para la estación Los Ángeles Oriente. .............................................. 59
**Figura No 40** . Comparación promedio mensual de velocidad de viento entre modelación
observada y proyectada para la estación Progreso. ............................................................... 59
**Figura No 41** . Comparación moda mensual de dirección de viento entre modelación
observada y proyectada para la estación Los Ángeles Oriente. .............................................. 60
**Figura No 42** . Comparación moda mensual de dirección de viento entre modelación
observada y proyectada para la estación Progreso. ............................................................... 60
**Figura No 43** . Comparación promedio mensual de temperatura entre modelación observada y
proyectada para la estación Los Ángeles Oriente. .................................................................. 61
**Figura No 44** . Comparación promedio mensual de temperatura entre modelación observada y
proyectada para la estación Progreso. ................................................................................... 61
**Figura No 45** . Comparación Rosas de viento. ........................................................................ 62
**Figura No 46** . Variación estacional de velocidad y dirección de viento. Datos observados. .... 63
**Figura No 47** . Variación estacional de velocidad y dirección de viento. Datos modelados. ..... 64
**Figura No 48** . Variación estacional de velocidad y dirección de viento. Datos observados. .... 64
**Figura No 49** . Variación estacional de velocidad y dirección de viento. Datos modelados. ..... 65
**Figura No 50** . Concentraciones horarias (OUE/m [3] ), Distribución horaria. Receptor No3. ........ 66
**Figura No 51** . Concentraciones horarias (OUE/m [3] ), Distribución horaria. Receptor No4. ........ 67
**Figura No 52** . Concentraciones horarias (OUE/m [3] ), Distribución horaria. Receptor No6. ........ 67

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 6 de 67

**1** **Resumen**

En el marco de un diagnóstico y compromisos adquiridos en resoluciones de calificación
ambiental Agrícola y Forestal Las Astas S.A., solicitó los servicios de Proterm S.A para llevar a
cabo un Estudio de Impacto Odorante del plantel de cerdos Monte Verde Bajo, con el objetivo
de determinar y/o descartar posible afectación a la calidad de vida de las personas, producto
de la operación del plantel ubicado en la comuna de Tucapel, región del BioBío. Actualmente,
el plantel en operación, tiene una capacidad de producción de 1.200 madres (ampliable a
2.000), conformadas por 15 pabellones: de maternidad, gestación, recría, crianza y engorda;
una planta de tratamiento de RILes, un sistema de lombrifiltro, una zona de acopio de cama
estabilizada, zonas de aplicación de riego de purín tratado y una laguna de acumulación.

Para obtener las emisiones del plantel de cerdos Monte Verde Bajo, se contemplan 3 campañas
de medición de olor a realizar en forma trimestral. Para lo anterior, se realizó un muestreo
estático bajo la NCh N°3386:2015 y NCh N°3431:2020, para posteriormente realizar un análisis
olfatométrico bajo la NCh N°3190:2010, en el laboratorio de Proterm. La toma de muestra en
las fuentes generadoras de olor, del plantel de cerdos, se llevó a cabo entre el 10 de agosto y
el 30 de septiembre de 2021, lo que representa la campaña de invierno.

Los resultados del estudio son presentados en dos informes: (A) “Toma de muestra y resultados
de concentración de olor mediante olfatometría dinámica en Plantel de Cerdos Monte Verde

Bajo” (Inf03E01.O-21-027) y (B) “Estudio de Impacto Odorante Plantel de Cerdos Monte Verde
Bajo”, este último corresponde al presente informe.

A continuación, se presenta una tabla que resume las emisiones de olor generadas por el
plantel de cerdos durante la campaña de invierno:

**Tabla No 1** . Emisiones de olor. Campaña de Invierno.

|Fuente|Emisión<br>(OU /s)<br>E|Cantidad|Emisión Total<br>(OU /s)<br>E|
|---|---|---|---|
|Maternidad|4.219|1|4.219|
|Gestación|3.951|2,51|9.878|
|Recría|4.575|1|4.575|
|Engorda|5.656|9,30|52.622|
|Planta de tratamiento de RILes|5.432|1|5.432|
|Laguna de Acumulación<br>(Agosto)|200.429|-|200.429|
|Laguna de Acumulación<br>(Septiembre)|23.827|-|23.827|
|Zona de Acopio (5 días)|995|-|995|
|Zona de Acopio (2 meses)|2.214|-|2.214|
|Zona de Acopio (6 meses)|Zona de Acopio (6 meses)|Zona de Acopio (6 meses)|Zona de Acopio (6 meses)|

1 Son 3 pabellones que se usan a la capacidad de 2 y medio (se deben retirar 60 hembras a maternidad por lo que
queda un "medio" de pabellón libre, esto se realiza 2 veces a la semana rotándose entre los 3 pabellones).

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 7 de 67

|Fuente|Emisión<br>(OU /s)<br>E|Cantidad|Emisión Total<br>(OU /s)<br>E|
|---|---|---|---|
|Zona de Riego|8,063|-|8.063|

Una vez obtenida la tasa de emisión de olor (OU E /s), de la campaña de invierno, en las fuentes
consideradas en el estudio, complementadas con las emisiones determinadas en las campañas
anteriores [2], estas fueron ingresadas a un modelo de dispersión atmosférica para obtener las
concentraciones (inmisión) de olor. Los resultados de las concentraciones de olor (OU E /m [3] )
arrojadas por el modelo de dispersión, fueron comparados con el límite establecido en la
resolución de calificación ambiental N° 068/2019 de 8 OU E /m [3] (Percentil 98).

La dispersión de las emisiones de olor del plantel de cerdos indica que el área de influencia
cubre un área total de 1.389 ha, distribuyéndose en forma ovalada alrededor de los pabellones,
zona de riego y laguna de acumulación. El área circunscrita por 1 OU E /m [3], establecida en la
“Guía para la predicción y evaluación de impactos por olor en SEIA” del año 2017, indica la
concentración en donde el 50% de la población puede comenzar a detectar un olor.

Fuera de los límites del predio se alcanzan concentraciones que van entre 1 y 68 OU E /m [3] . A
pesar de lo anteriormente señalado, en ningún receptor se supera el límite de inmisión,
establecido como 8 OU E /m [3] .

En base a lo mencionado anteriormente, en la siguiente Tabla, se presenta en forma detallada
la concentración en los receptores y, por otro lado, en la imagen se observa una cartografía de
las curvas de isoconcentración.

**Tabla No 2** . Concentración receptores. Percentil 98.

|No|Descripción|Distancia a los<br>pabellones (m)|Concentración de<br>inmisión<br>(OU /m3)<br>E|Horas al año<br>>8 OU /m3<br>E|
|---|---|---|---|---|
|R1|Sector Huequete 1|1,93|2,67|32 (0,37%)|
|R2|Sector Huequete 2|2,88|0,60|0 (0,00%)|
|R3|Sector San Luis 1|1,51|4,79|91 (1,04%)|
|R4|Sector Huequén|2,35|7,57|167 (1,91%)|
|R5|Sector Huequete 3|2,19|1,54|24 (0,27%)|
|R6|Sector San Luis 2|0,33|4,26|89 (1,02%)|
|R7|Sector Carrizal|0,53|2,07|32 (0,37%)|
|R8|Fuerte San Diego|3,95|0,45|0 (0,00%)|

2 Las emisiones modeladas contemplan las emisiones determinadas en las campañas de otoño, invierno, primavera
y verano. Para efectos de este informe, se utilizaron todas las campañas medidas el año 2020 y 2021
correspondiente a septiembre, octubre, noviembre, diciembre, enero, febrero, marzo y mayo.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 8 de 67

**Figura No 1** . Concentración de olor generada por las fuentes del plantel de cerdos.

(Percentil 98).

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 9 de 67

**2** **Introducción**

Agrícola y Forestal Las Astas S.A., solicitó los servicios de Proterm S.A. para cuantificar las
emisiones odorantes del plantel de cerdos Monte Verde Bajo operado por Agrícola Coexca S.A.
Lo anterior con el objetivo de evaluar los efectos de las actuales emisiones de olor generadas
en el plantel.

El plantel de cerdos cuenta con dos resoluciones exentas de calificación ambiental: (1)
“Establecimiento Plantel de Cerdos Monte Verde Bajo” RCA N°016/2008, (2) “Mejoramiento del
desempeño ambiental del plantel de cerdos Monte Verde, a través de la recuperación de
nutrientes para el riego, y el manejo de animales muertos” RCA N°068/2019.

A continuación, se presenta la ubicación espacial del área de estudio considerada en el estudio
de impacto odorante.

**Figura No 2** . Área del estudio de impacto odorante.

Para cuantificar las emisiones del plantel, se realizarán campañas de medición por estación del
año, correspondiendo este muestreo a la campaña de invierno. Se realizó un muestreo estático
bajo la NCh N°3386:2015 y NCh N°3431:2020, para posteriormente realizar un análisis

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 10 de 67

olfatométrico bajo la NCh N°3190:2010 en el laboratorio de Proterm S.A. Cabe destacar que la
toma de muestra en las fuentes generadoras de olor del plantel de cerdos se realizó entre el 10
de agosto y el 30 de septiembre de 2021, cuyos resultados se presentan en el informe (A) Toma
de muestra y resultados de concentración de olor mediante olfatometría dinámica en plantel de
Cerdos Monte Verde Bajo (Inf03E01.O-21-027). En forma adicional, para calcular las emisiones
de olor, se realizó una medición de flujo entre el 12 y 13 de agosto de 2021, en cuatro horarios
de 08:00 a 10:00 hrs, de 11:00 a 15:00 hrs, de 18:00 a 20:00 hrs y de 00:00 a 02:00 hrs en los
pabellones de Maternidad, Gestación, Recría y Engorda.

El presente informe evalúa la dispersión de las emisiones de olor de las actuales instalaciones
del plantel de cerdos correspondiente a pabellones, lombrifiltro, planta de tratamiento de RILes,
laguna de acumulación, zona de aplicación de efluente tratado (en adelante riego) y acopio de
camas estabilizadas de cerdos.

**3** **Objetivo General**

Evaluar las emisiones de olor generadas por el plantel de cerdos Monte Verde Bajo, sobre la
calidad de vida de la población cercana, sistema de vida, costumbres, población protegida y
turismo.

**Objetivos específicos**

 - Determinar la tasa de emisión de olor de las fuentes monitoreadas.

 Determinar la dispersión de las emisiones de olor del plantel de cerdos Monte Verde
Bajo.

 Comparar los valores de concentración de inmisión de olor, con lo establecido en la
RCA N°068/2019.

**4** **Metodología**

A continuación, se presenta la metodología utilizada que permitió evaluar el efecto de las
emisiones de olor del plantel de cerdos Monte Verde Bajo.

**Caracterización de las fuentes de emisión de olor.**

Para poder caracterizar las fuentes generadoras de olor del plantel, se utilizaron las siguientes
metodologías:

 - Detección satelital: mediante Google Earth Pro [3], se identificaron las superficies de las
fuentes generadoras de emisión y la distancia de los receptores con respecto al plantel.

3 Versión 7.1.5.1557 de Google Earth

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 11 de 67

 - Toma de muestra: entre el 10 de agosto y el 30 de septiembre de 2021, se realizó un
muestreo en el plantel de cerdos con su posterior análisis olfatométrico, con la finalidad
de obtener la concentración de olor y con ello la emisión generada por las fuentes.

 Medición de flujo: entre el 12 y 13 de agosto se realizó una medición de flujo en cuatro
horarios distintos en los pabellones de maternidad, gestación, recría y engorda, con la
finalidad de modelar la emisión en forma más representativa.

 Revisión bibliográfica: Se revisó la documentación presentada al Servicio de Evaluación
Ambiental, en la DIA “Mejoramiento del desempeño ambiental del plantel de cerdos
Monte Verde Bajo, a través de la recuperación de nutrientes para el riego, y el manejo
de animales muertos” RCA N°068/2019.

 - Solicitud de información al cliente: donde se especifican periodos de funcionamiento de
las fuentes y sus dimensiones.

**Estimación de concentración y emisiones de olor**

Se realizó un muestreo estático en las fuentes que existen en el plantel de cerdos; lo anterior
acorde a las normas NCh N°3386:2015 y NCh N°3431:2020, para posteriormente realizar un
análisis olfatométrico acorde a la NCh N°3190:2010, en el laboratorio de Proterm [4] . La toma de
muestra de las emisiones de olor se llevó a cabo entre el 10 de agosto y el 30 de septiembre
de 2021; cuyos resultados son presentados en el informe Inf03E01.O-21-027. (“Toma de
muestra y resultados de concentración de olor mediante olfatometría dinámica en Plantel de
Cerdos Monte Verde Bajo”).

4 Laboratorio acreditado ISO17025:2017

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 12 de 67

**Figura No 3** . Diagrama metodología de caracterización de olor.

**Tabla No 3.** Distribución de la toma de muestra en fuentes difusas pasivas de área [5] .

|Fuente|Fecha|Condición|N° de<br>Puntos|N° de<br>Muestras|Coordenada<br>referencial<br>Proyección UTM<br>Huso 19S|Col7|Hora de<br>inicio|Hora de<br>término|
|---|---|---|---|---|---|---|---|---|
|**Fuente**|**Fecha**|**Condición**|**N° de**<br>**Puntos**|**N° de**<br>**Muestras**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Laguna de<br>Acumulación<br>(Agosto)|10-08-<br>2021|-|6|6|239.730|5.870.520|11:10|12:00|
|Laguna de<br>Acumulación<br>(Septiembre)|30-09-<br>2021|-|6|6|239.730|5.870.520|11:17|12:20|
|Zona de<br>acopio<br>estabilización<br>cama<br>caliente<br>|23-09-<br>2021|5 días|3|3|238.269|5.871.197|11:26|11:56|
|Zona de<br>acopio<br>estabilización<br>cama<br>caliente<br>|23-09-<br>2021|2 meses|3|3|3|3|11:53|12:23|
|Zona de<br>acopio<br>estabilización<br>cama<br>caliente<br>|23-09-<br>2021|6 meses|3|3|3|3|12:22|12:52|

5 De acuerdo a la Guía para la predicción y evaluación de impactos por olor en el SEIA, los tipos de fuentes se
describen como fuentes puntuales, difusas pasivas, difusas activas y fugitivas. No obstante, de acuerdo a la NCh
3386:2015 “Calidad de aire Muestreo estático para olfatometría”, describe la fuente pasiva como fuente con
dimensiones definidas (fuente de área, fuentes de volumen) que no tienen un flujo de aire de salida definida, tales
como depósitos de desechos, lagunas, campos después de esparcir estiércol, pilas de compost no aireados,
edificaciones. Junto a lo anterior en la sección 6.3.3. se detalla la toma de muestra en “Fuentes de Volumen”, la cual
fue aplicada para las edificaciones en este estudio.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 13 de 67

|Fuente|Fecha|Condición|N° de<br>Puntos|N° de<br>Muestras|Coordenada<br>referencial<br>Proyección UTM<br>Huso 19S|Col7|Hora de<br>inicio|Hora de<br>término|
|---|---|---|---|---|---|---|---|---|
|**Fuente**|**Fecha**|**Condición**|**N° de**<br>**Puntos**|**N° de**<br>**Muestras**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Riego|23-09-<br>2021|99% agua<br>1% purín|6|6|238.846|5.870.626|15:00|15:49|

**Tabla No 4.** Distribución de la toma de muestra en fuentes difusas pasivas de volumen.

|Fuente|Fecha|N° de<br>Puntos|N° de<br>Muestras|Coordenada referencial<br>Proyección UTM<br>Huso 19S|Col6|Hora de<br>inicio|Hora de<br>término|
|---|---|---|---|---|---|---|---|
|**Fuente**|**Fecha**|**N° de**<br>**Puntos**|**N° de**<br>**Muestras**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Maternidad6|12-08-2021|6|6|238.012|5.872.078|13:27|14:01|
|Gestación|12-08-2021|6|6|237.963|5.872.132|14:49|15:25|
|Recría|12-08-2021|6|6|237.959|5.872.058|14:10|14:43|
|Engorda|10-08-2021|6|6|238.098|5.871.751|12:55|13:45|
|Planta<br>Tratamiento Riles|23-09-2021|1|3|237.873|5.872.258|13:46|14:16|

**Evaluación de la dispersión de las emisiones de olor.**

Para evaluar la dispersión atmosférica, de las emisiones de olor generadas por las fuentes, se
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
trayectoria por “Puff”, lo que hace su cálculo mucho más rápido [7] .

Para la modelación se utilizó el software Calpuff versión 7.2.1 junto a los módulos CALPOST
7.1.0. y CALRANK 7.0.0. Además para efectos de la interacción gráfica de los módulos, se usó
el software interactivo CALPUFF View 8.5.0.

En el Anexo N°1 se presenta el esquema del modelo utilizado y los elementos de la modelación.

6 En los pabellones de Maternidad, Gestación, Recría y Engorda se realizó un barrido de seis muestras a lo largo de
cada uno de ellos.
7 Guía para el uso de modelos de calidad del aire, 2012

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 14 de 67

**4.3.2** **Recopilación de los antecedentes para la modelación**

Para conocer la dispersión que tendrán los gases en un área determinada es preciso incorporar,
en el modelo seleccionando, distintos parámetros de manera que la simulación sea lo más
parecida a las condiciones reales. Las variables o entradas que requirió el modelo se detallan
a continuación.

**Tabla No 5** . Variables de entrada consideradas en la modelación.

|Variable|Parámetros|Fuente|
|---|---|---|
|Meteorológicas|Dirección de Viento|Tal como lo establece la guía el modelo numérico<br>recomendado para la generación de datos<br>meteorológicos es el Weather Research and<br>Forecasting Model (WRF). WRF es uno de los<br>modelos meteorológicos de pronóstico más<br>avanzados<br>y <br>completos<br>mantenido<br>por<br>NCAR/NOAA de Estados Unidos.|
|Meteorológicas|Velocidad de Viento|Velocidad de Viento|
|Meteorológicas|Temperatura|Temperatura|
|Meteorológicas|Presión|Presión|
|Meteorológicas|Precipitación|Precipitación|
|Geofísicas|Elevación del Terreno|Elevación del Terreno|
|Geofísicas|Uso de Suelo|Uso de Suelo|
|Características<br>de la fuente|Descripción del proceso|Información de fuentes consideradas en el<br>escenario evaluado.|
|Características<br>de la fuente|Emisiones de olor|Emisiones de olor|
|Características<br>de la fuente|Periodo de operación|Periodo de operación|
|Características<br>de la fuente|Ubicación de las fuentes|Ubicación de las fuentes|
|Receptores<br>Discretos|Coordenadas de los receptores|Se definieron las viviendas cercanas al plantel, y<br>los receptores ubicados en el interior de la<br>superficie del área de influencia del proyecto.<br>Cabe destacar que los receptores fueron<br>proporcionados por el titular del proyecto.|

A continuación, se presenta una tabla que resume las campañas de medición de olor que fueron
consideradas en la modelación:

**Tabla No 6** . Campañas de muestreo y modelación.

|Campaña|Meses considerados|Periodo de muestreo|Código informe|
|---|---|---|---|
|Otoño|Abril, mayo y junio|06 al 25 de abril de<br>2021|Inf01E01.O-21-027|
|Otoño|Abril, mayo y junio|06 al 25 de abril de<br>2021|Inf02E01-O-21-027|
|Invierno|Julio, agosto y<br>septiembre|10 de agosto al 30 de<br>septiembre de 2021|Inf03E01.O-21-027|
|Invierno|Julio, agosto y<br>septiembre|10 de agosto al 30 de<br>septiembre de 2021|Inf04E01.O-21-027|
|Primavera|Octubre|07 al 09 de octubre<br>2020|Inf03E01.O-20-048|
|Primavera|Octubre|07 al 09 de octubre<br>2020|Inf04E04.O-20-048|
|Primavera|Noviembre|04 al 20 de noviembre<br>2020|Inf05E01.O-20-048|
|Primavera|Noviembre|04 al 20 de noviembre<br>2020|Inf06E03.O-20-048|
|Primavera|Diciembre||Inf05E01-O-20-012|

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 15 de 67

|Campaña|Meses considerados|Periodo de muestreo|Código informe|
|---|---|---|---|
|||07, 09 y 11 de<br>diciembre 2020|Inf06E01-O-20-012|
|<br> <br> <br>Verano|Enero|11 al 14 de enero 2021|Inf09E01.O-20-048|
|<br> <br> <br>Verano|Enero|11 al 14 de enero 2021|Inf10E01.O-20-048|
|<br> <br> <br>Verano|Febrero|01 al 03 de febrero y<br>03 de marzo 2021|Inf11E01.O-20-048|
|<br> <br> <br>Verano|Febrero|01 al 03 de febrero y<br>03 de marzo 2021|Inf12E01.O-20-048|
|<br> <br> <br>Verano|Marzo|02 al 05 de marzo de<br>2021|Inf13E01.O-20-048|
|<br> <br> <br>Verano|Marzo|02 al 05 de marzo de<br>2021|Inf14E01.O-20-048|

Es importante señalar que, el presente informe, corresponde a la modelación que incluye las
mediciones realizadas durante la campaña invierno.

**4.3.3 Variables meteorológicas y geofísicas**

Tal como se mencionó en el punto 4.3.2, se utilizó la meteorología de pronóstico WRF en
formato calmet.dat, de esta forma se incorporó el archivo directamente al programa. El archivo
meteorológico contiene a la comuna de Tucapel. Para la ejecución del modelo se modeló una
zona más pequeña en comparación al WRF, es importante destacar que la zona modelada
tiene una dimensión de grilla de 250 metros (5 x 5 km) y 500 metros (13 x 13 km). En la Tabla
N°7 se presentan las características del archivo meteorológico, mientras que en la figura N°1
se presentan los límites indicados (figura en apartado “introducción”).

**Tabla No 7.** Características del archivo meteorológico WRF.

|Datos|Col2|Archivo Meteorológico|
|---|---|---|
|Comuna Central|Comuna Central|Yungay|
|Dimensión grilla|Dimensión grilla|62 x 62|
|Espaciado grilla|Espaciado grilla|1 km|
|Fecha-Hora inicio|Fecha-Hora inicio|01-01-2014 00:00|
|Fecha-Hora fin|Fecha-Hora fin|30-12-2014 23:00|
|Coordenadas NO8|Este|721.787|
|Coordenadas NO8|Norte|5.847.998|
|Coordenadas NE9|Este|251.423|
|Coordenadas NE9|Norte|5.909.017|
|Coordenadas SO10|Este|721.757|
|Coordenadas SO10|Norte|5.847.979|
||Este|251.398|

8 Coordenadas WGS-84 Huso 18.
9 Coordenadas WGS-84 Huso 19.
10 Coordenadas WGS-84 Huso 18.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 16 de 67

|Datos|Col2|Archivo Meteorológico|
|---|---|---|
|Coordenadas SE11|Norte|5.909.180|

**4.3.4 Evaluación de los resultados**

Los resultados de la concentración de olor (OU E /m [3] ) modelados y registrados fueron
comparados con los límites de inmisión indicados en la evaluación del proyecto “Mejoramiento
del desempeño ambiental del plantel de cerdos Monte Verde, a través de la recuperación de
nutrientes para el riego, y el manejo de animales muertos” aprobado con la resolución de
calificación ambiental RCA N°068/2019.

En la evaluación indicada se realizaron las comparaciones con el valor de inmisión de 8 OU E /m [3]
(percentil 98). El límite mencionado anteriormente fue evaluado en receptores sensibles al olor
indicado en la RCA N°068/2019.

11 Coordenadas WGS-84 Huso 19.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 17 de 67

**Figura No 4** . Ubicación de receptores discretos.

**Tabla No 8.** Receptores discretos considerados en la modelación.

|No|Descripción del Receptor|Distancia desde los<br>galpones de cerdos<br>(km)|Coordenadas UTM WGS-84<br>Huso 19 S|Col5|
|---|---|---|---|---|
|**No**|**Descripción del Receptor**|**Distancia desde los**<br>**galpones de cerdos**<br>**(km)**|**Este (m)**|**Norte (m)**|
|R1|Sector Huequete 1|1,93|240.083|5.871.543|
|R2|Sector Huequete 2|2,88|240.992|5.871.260|
|R3|Sector San Luis 1|1,51|238.753|5.870.342|
|R4|Sector Huequén|2,35|239.579|5.869.871|
|R5|Sector Huequete 3|2,19|240.336|5.871.482|
|R6|Sector San Luis 2|0,33|237.892|5.871.388|
|R7|Sector Carrizal|0,53|238.241|5.872.643|
|R8|Fuerte San Diego|3,95|239.153|5.867.863|

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 18 de 67

**4.3.5 Área de Influencia.**

Una vez ejecutado el modelo de dispersión de olor, se realizó el análisis de post-proceso
obteniendo las curvas iso-concentración de la dispersión anual. Tal como lo indica la guía, el
Área de Influencia se debe circunscribir en el espacio contenido por la isodora de 1 OU E /m [3],
que corresponde al umbral de detección del olor compuesto.

**Evaluación del desempeño del archivo de pronóstico utilizado**

El modelo numérico recomendado para la generación de datos meteorológicos es el Weather
Research and Forecasting Model (WRF). WRF, es uno de los modelos meteorológicos de
pronóstico más avanzados y completos, el cual es mantenido por NCAR/NOAA de Estados
Unidos.

Todos los modelos tienen asociados errores e incertidumbre. Los resultados del modelo se

analizan en base a la comparación de los gráficos indicados en los puntos 6.6.3 y 6.7 de la
“Guía para uso de modelos de Calidad del aire en el SEIA”. En base a la comparación de los
ciclos diarios de las variables meteorológicas observadas y simuladas, en la misma, ubicación,
se debe caracterizar la capacidad del modelo de reproducir las observaciones tanto en
magnitud como en su variabilidad.

Para cumplir con lo indicado por la guía para uso de modelos de dispersión del SEA, se realizó
un análisis del desempeño de la meteorología de pronóstico WRF utilizada para la modelación.
Este análisis permite detectar posibles desviaciones en el modelo de pronóstico que podrían
causar efectos en los resultados del modelo de dispersión.

Las estaciones meteorológicas del sistema SINCA al interior del dominio WRF, se encuentran
a distancias sobre 30 km del proyecto. La estación meteorológica Los Ángeles Oriente y
Progreso, ubicada al interior de Los Ángeles y Cabrero respectivamente, son estaciones con
datos meteorológicos de temperatura, dirección y velocidad del viento. En el Anexo 2 se
presenta una descripción de la meteorología, mientras que en el Anexo 3 se presenta una
comparación entre la meteorología de pronóstico y los datos observados en la estación
meteorológica.

**5** **Resultados**

A continuación, se presentan los resultados que permitieron evaluar el efecto de las emisiones
de olor del plantel de cerdos Monte Verde Bajo.

**Caracterización de las fuentes de emisión**

El plantel de crianza de cerdos del Fundo Las Astas que se encuentra aprobado por RCA
N°016/2008 contempla la producción de cerdos de un grupo de 2.000 madres. De acuerdo a lo
informado en la Declaración de Impacto Ambiental, el plantel contempla las etapas de
reproducción, gestación, maternidad, recría y engorda de los cerdos.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 19 de 67

Los cambios propuestos en la RCA N°068/2019 aprobado ambientalmente están ligados al
tratamiento de los cerdos muertos y el uso de nutrientes para riego. Respecto al sistema de
tratamiento de purines, se integra una laguna de acumulación de 1,5 ha (de 45.000 m [3] ) para el
almacenamiento de purín tratado que se utilizará como riego.

**Figura No 5** . Diagrama de proceso aprobado en escenario futuro RCA N°068/2019.

A continuación, se describe las fuentes generadoras de olor de las instalaciones actuales del
plantel de cerdos. En la siguiente tabla, se detallan las fuentes consideradas en la modelación
y en la cartografía se presenta su ubicación espacial. Lo anterior de acuerdo a lo señalado en
el punto 3.3 de la guía para la predicción y evaluación de olores en el SEIA.

**Tabla No 9** . Descripción fuentes generadoras de olor del plantel de Cerdos - Monte Verde

Bajo.

|Fuentes|Descripción|
|---|---|
|Pabellones<br>Gestación|Corresponde a un pabellón, donde las hembras se alojan en jaulas<br>individuales de gestación, durante 114 +/- 2 días y permanecen durante 112<br>días.<br>Los pabellones de gestación, se encuentran sobre piso de concreto con grutter<br>para eliminar correctamente las excretas y la regulación de temperatura se<br>realiza mediante sistema de cortinas.|
|Pabellones<br>Maternidad|Dos días antes del parto las hembras son ingresadas a la sección maternidad<br>y colocadas en jaulas parideras individuales, que permite la recolección y<br>evacuación de purines. La temperatura de los pabellones se mantiene<br>mediante calefactores eléctricos y sistema de cortinas.<br>La lactancia dura 21 días y luego los lechones con un peso aproximadamente<br>de 6 kg son destetados y enviados a los pabellones de recría. Las madres son<br>trasladadas nuevamente al pabellón de reproducción al cuarto día después<br>del destete, para ser nuevamente inseminadas.|

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 20 de 67

|Fuentes|Descripción|
|---|---|
|Pabellones<br>Recría|Esta etapa se inicia a los 21 días de edad de los lechones con un peso<br>aproximado de 6 kg y finaliza más o menos a los 50 días cuando ya pesan<br>entre 28 y 30 kg.<br>Los pabellones poseen corrales con fosas de recepción de excretas y<br>evacuación de purines. Se les proporciona además, calor adicional por medio<br>de calefactores eléctricos y regulados por un sistema de ventilación manual.|
|Pabellones<br>Engorda|Se inicia con la llegada de los cerdos con una edad promedio de 70 días, los<br>que se mantienen en 9 pabellones de engorda con corrales de capacidad para<br>50 cerdos cada uno. El ciclo es de aproximadamente 95 días, tiempo en que<br>los cerdos alcanzan un promedio de 90 - 115 kg. Es importante señalar que,<br>durante la campaña realizada en invierno, el cliente mencionó que se estaba<br>utilizando el pabellón de crianza para almacenar cerdos de engorda, por ende<br>contaban con 10 pabellones de engorda.<br>La alimentación tipo seco-húmedo se realiza con comederos automáticos de<br>líneas transportadoras que distribuyen el alimento. El piso de estos pabellones<br>es de cemento cubierto con paja de trigo, la cual al mezclarse con las excretas<br>proporciona calor a los cerdos. Después de algunos ciclos la cama es retirada<br>y llevada a una zona de acopio, donde se forman pilas para la obtención de<br>una cama estabilizada y su aplicación en el suelo del predio.|
|Planta de<br>Tratamiento de<br>RILes|Todo el purín generado en los pabellones de gestación, maternidad y recría,<br>son llevados a la Planta de Tratamiento de RILes, donde se separa la fracción<br>sólida de la líquida por medio de un filtro parabólico y prensa, luego un<br>tratamiento físico-químico y finalmente por desinfección por rayos UV.|
|Lombrifiltro|La parte líquida del purín tratado es enviado a un Lombrifiltro. Este sistema<br>tiene la función de remover la materia orgánica presente en el purín<br>acondicionado, utilizando para ello las características morfológicas y función<br>degradadora de la lombriz roja Eisennia foetida.|
|Zona de acopio de<br>cama estabilizada|Corresponde a una zona de acopio de pilas provenientes de Engorda, que<br>consiste en paja semi-compostada, lo que permite la obtención de un compost<br>maduro.|
|Zona de Aplicación<br>de Purín tratado|El purín tratado es aplicado mediante pivotes para el riego de cultivos (como:<br>achicoria, maíz, trigo, avena, alfalfa, entre otros), en los meses de diciembre<br>a abril, y acumulados en piscina impermeabilizada entre mayo y enero.|
|Laguna de<br>acumulación|En los meses en que el purín tratado no es aplicado para el riego de cultivos,<br>este es conducido hacia una laguna de acumulación impermeabilizada, hasta<br>cuando los cultivos necesiten nuevamente el correspondiente riego.|

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 21 de 67

**Figura No 6** . Fuentes consideradas en el estudio.

**Emisiones de olor**

**5.2.1 Emisiones muestreadas plantel de cerdos Monte Verde Bajo. Campaña Invierno.**

Entre el 10 de agosto y el 30 de septiembre de 2021, se realizó un muestreo de olor en las
fuentes del plantel; lo anterior bajo la NCh No 3386:2015 y NCh N°3431:2020 por personal de
Proterm S.A. Las muestras fueron analizadas mediante la técnica de olfatometría dinámica
según la NCh No3190:2010 en el laboratorio de Proterm S.A. [12]

Para las características técnicas del muestreo y análisis de olor consultar el informe
Inf03E01.O-21-027. (“Toma de muestra y resultados de concentración de olor mediante
olfatometría dinámica en Plantel de Cerdos Monte Verde Bajo).

A continuación, se expresan los resultados de las mediciones de las fuentes de Volumen,
determinadas mediante la aplicación del método directo de la NCh 3431:2020.

12 Laboratorio acreditado ISO17025:2017 para olfatometría dinámica.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 22 de 67

**Tabla No 10.** Emisión de olor en fuentes difusas pasivas de Volumen.

|Fuente|Concentración<br>Promedio<br>(OU /m3)<br>E|Área<br>emisión<br>(m2)|Velocidad de<br>salida 13<br>(m/s)|Flujo 14<br>(m3/s)|Emisión 15<br>(OU /s)<br>E|
|---|---|---|---|---|---|
|Maternidad|474|19,4416|0,46|8,9|4.219|
|Gestación|118|84,99|0,39|33,48|3.951|
|Recría|244|31,8017|0,59|18,75|4.575|
|Engorda|67|134|0,63|84,42|5.656|
|Planta de<br>Tratamiento de<br>RILes|10.864|1,46|0,34|0,50|5.432|

A continuación, se expresan los resultados de las mediciones de las fuentes difusas pasivas de
área, determinadas mediante la aplicación de los métodos indicados en la NCh 3386:2015.

**Tabla No 11.** Emisión de olor en fuentes difusas pasivas de área.

|Fuente|Condición|Concentración<br>Promedio<br>(OU /m3)<br>E|Emisión<br>(OU /m2/s)<br>E|Área emisión<br>(m2)|Emisión<br>(OU /s)<br>E|
|---|---|---|---|---|---|
|Zona de acopio de <br>cama estabilizada|5 días|67|0,56|1.777,618|995|
|Zona de acopio de <br>cama estabilizada|2 meses|43|0,48|4.612,819|2.214|
|Zona de acopio de <br>cama estabilizada|6 meses|78|78|78|78|
|Laguna de<br>Acumulación<br>(Agosto)|-|2.574|21,45|9.344|200.429|
|Laguna de<br>Acumulación<br>(Septiembre)|-|306|2,55|9.344|23.827|
|Zona de Riego|99% agua<br>1% purín|129|1,075|7500|8.063|

En la tabla anterior, se puede observar que la principal fuente de emisión corresponde a la
laguna de acumulación muestreada en agosto con 200.429 OU E /s, en segundo lugar la laguna
de acumulación muestreada en septiembre 23.827 OU E /s y en tercer lugar la zona de riego con
8.063 OU E /s.

En relación a las pilas, es importante señalar que la emisión generada por el acopio de 5 días
representa la emisión de las pilas recién llegadas hasta el primer mes; por otro lado, el promedio

13 Promedio
14 Flujo = Velocidad x Área emisión
15 Emisión = Flujo x Concentración
16 El área de emisión corresponde al largo del pabellón 110 m x la abertura promedio (ponderada por la velocidad).
Se considera una reducción dado que una de las doce salas de maternidad se encuentra vacía.
17 El área de emisión corresponde al largo del pabellón 110 m x la abertura promedio (ponderada por la velocidad).
Se considera una reducción dado que una de las ocho salas de recría se encuentra vacía.
18 Se considera una superficie aproximada de acuerdo a lo observado en terreno.
19 Se considera una superficie aproximada de acuerdo a lo observado en terreno.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 23 de 67

de la emisión generada por el acopio de 2 y 6 meses representa la emisión generada entre el
primer y noveno mes.

**5.2.2 Factores utilizados para el cálculo de emisión**

Por otro lado, el 12 y 13 de agosto se realizó una medición de velocidad de salida del olor y se
midió la abertura en los pabellones de maternidad, gestación, recría y engorda, con la finalidad
de calcular el flujo en cuatro horarios, de tal forma de obtener un factor de emisión, tal como se
presenta a continuación:

**Tabla No 12.** Factores de emisión por pabellón [20] .

|Pabellón|Hora|Col3|Col4|Col5|
|---|---|---|---|---|
|**Pabellón**|**01:00 - 03:00**|**08:00 - 10:00**|**12:00 - 15:00**|**20:00 - 23:00**|
|Maternidad|0,40|0,64|1|<br> 0,27|
|Gestación|0,18|0,40|1|0,01|
|Recría|0,41|0,53|1|0,41|
|Engorda|0,05|0,54|1|0,05|

Es importante señalar, que durante la campaña de invierno se mencionó que en el pabellón de
crianza habían cerdos de engorda por lo que durante el mes de julio, agosto y septiembre se
modeló la emisión generada por los cerdos de engorda, mientras que el resto del año, se
consideró un promedio de las emisiones obtenidas en recría y engorda. Para mayor información

revisar Anexo N°2.

**5.2.3 Emisiones del plantel Monte Verde Bajo. Campaña Invierno**

A partir de las mediciones realizadas, se homologaron las emisiones del resto de las fuentes,
determinándose la tasa de emisión total. A continuación, se presenta la tabla resumen de las
emisiones y el gráfico de distribución.

**Tabla No 13.** Emisión de olor en fuentes difusas pasivas de Volumen.

|Fuente|Emisión<br>(OU /s)<br>E|Cantidad|Emisión<br>Total<br>(OU /s)<br>E|
|---|---|---|---|
|Maternidad|4.219|1|4.219|
|Gestación|3.951|2,521|9.878|
|Recría|4.575|1|4.575|
|Engorda|5.656|9,30|52.622|
|Planta de tratamiento de RILes|5.432|1|5.432|

20 Los factores de emisión se obtuvieron a partir de las mediciones realizadas durante el mes de diciembre de 2020.
21 Son 3 pabellones que se usan a la capacidad de 2 y medio (se deben retirar 60 hembras a maternidad por lo que
queda un "medio" de pabellón libre, esto se realiza 2 veces a la semana rotándose entre los 3 pabellones).

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 24 de 67

**Tabla No 14.** Emisión de olor en fuentes difusas pasivas de área.

|Fuente|Condición|Concentración<br>Promedio<br>(OU /m3)<br>E|Emisión<br>(OU /m2/s)<br>E|Área emisión<br>(m2)|Emisión<br>(OU /s)<br>E|
|---|---|---|---|---|---|
|Zona de acopio de <br>cama estabilizada|5 días|67|0,56|1.777,622|995|
|Zona de acopio de <br>cama estabilizada|2 meses|43|0,48|4.612,823|2.214|
|Zona de acopio de <br>cama estabilizada|6 meses|78|78|78|78|
|Laguna de<br>acumulación<br>(Agosto)|-|2.574|21,45|9.344|200.429|
|Laguna de<br>acumulación<br>(Septiembre)|-|306|2,55|9.344|23.827|
|Zona de Riego|99% agua<br>1% purín|129|1,075|7.500|8.063|

En relación a las pilas, es importante señalar que no se consideran pilas sobre 9 meses ya que
el olor determinado para las pilas de 11 meses y 2 años corresponde netamente a nylonplástico. Es importante señalar que, la emisión generada por el acopio de 5 días representa la
emisión de las pilas recién llegadas hasta el primer mes; por otro lado, el promedio de la emisión
generada por el acopio de 2 y 6 meses representa la emisión generada entre el primer y noveno

mes.

De las tablas anteriores, se puede observar que las mayores emisiones se producen en la
laguna de acumulación muestreada en agosto con 200.429 OU E /s (70%) y en los pabellones
de engorda con 52.622 OU E /s (18%). Las fuentes mencionadas anteriormente representan el
88% de las emisiones generadas durante la campaña de invierno, las que se contabilizan en
288.427 OU E /s. Es importante señalar que para este cálculo se consideró la máxima emisión
generada en la laguna de acumulación, la que fue muestreada durante el mes de agosto.

En el siguiente gráfico se presenta la distribución de las emisiones de olor generadas durante
la campaña de invierno.

22 Se considera una superficie aproximada de acuerdo a lo observado en terreno.
23 Se considera una superficie aproximada de acuerdo a lo observado en terreno.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 25 de 67

**Figura No 7** . Distribución emisiones de olor.

**5.2.4 Características y Emisiones de las fuentes ingresadas en el modelo**

Pabellones

La emisión de los pabellones se considera a través de cortinas laterales en las cuales se
produce la renovación de aire.

A continuación, se presentan las dimensiones de las cortinas de cada pabellón:

**Tabla No 15** . Cortinas pabellones.

|Fuente|Largo (m)|Ancho (m)|
|---|---|---|
|Maternidad24.|110|1|
|Gestación25|110|1|
|Recría26|110|1|
|Engorda27|100|1,1|

24 Para efectos del modelo se considera que medio pabellón no genera emisiones. El medio pabellón vacío varía a
lo largo del año entre los 3 pabellones.
25 Para efectos del modelo se considera la división en 12 salas de maternidad. 1 sala no emite emisiones. La sala
vacía varía a lo largo del año.
26 Para efectos del modelo se considera la división en 8 salas. 1 sala no emite emisiones. La sala vacía varía a lo
largo del año.
27 Para efectos del modelo en invierno se considera que 6 pabellones están a plena capacidad, 1 pabellón a 95% de
capacidad, 1 pabellón a 86% de capacidad, 1 pabellón a 51% capacidad y 1 pabellón a un 25% de capacidad. Esta
condición varía entre los pabellones a lo largo del año.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 26 de 67

|Fuente|Largo (m)|Ancho (m)|
|---|---|---|
|Crianza28|110|1|

Lombrifiltro

El proceso de goteo de efluente en el lombrifiltro se realiza todos los días. En verano y otoño
opera 5 horas desde el mediodía, mientras que en invierno y primavera se realiza 2 horas
durante la mañana. Actualmente, el lombrifiltro se encuentra tapado, proporcionando 3
aberturas laterales semitapadas para proveer oxígeno a las lombrices. Es importante señalar
que durante el muestreo realizado durante la campaña de invierno no se encontraba operativo
el lombrifiltro por lo que para efectos de la modelación se consideraron las emisiones de la
campaña anterior.

Aplicación de riego purín tratado

Se contempla regar entre los meses de septiembre y abril, en horario diurno 8 horas en verano
y 5 horas en otoño. El proceso de riego abarca 0,75 ha diarias las que se van regando día a
día hasta alcanzar las 180 ha disponibles. Se utilizan los pivotes 2, 3, 4 indicados en la figura
N°6. Es importante señalar que durante el mes de abril se regó en tres días, por lo que en el
modelo se consideraron tres días de riego, los que corresponden al 8, 15 y 16 de abril. Por otro
en septiembre se comenzó a regar el 22 de septiembre por lo que el riego no se consideró
durante todo el mes de septiembre.

Acopio de cama estabilizada

De acuerdo a lo indicado por el titular, la cama permanece durante 18 meses para su proceso
de estabilización. La edad de los acopios de cama varía. Se considera que el primer mes tiene
la emisión más alta, mientras que el resto de los meses su emisión disminuye hasta los nueve

meses.

Para efectos del modelo en otoño se considera que 6 pabellones están a plena capacidad, 1 pabellón a 38%
capacidad, 1 pabellón a 14% capacidad y 1 pabellón vacío. Esta condición varía entre los pabellones a lo largo del
año.
En invierno 6 pabellones están a plena capacidad, uno a 4/5 capacidad, uno a 2/3 capacidad y uno vacío.
En octubre 6 pabellones están a plena capacidad, uno a 83% capacidad, uno a 58% capacidad y uno vacío.
En noviembre 6 pabellones están a plena capacidad, uno a 54% capacidad, uno a 43% capacidad y uno vacío.
En diciembre 6 pabellones están a plena capacidad, uno a 83% capacidad, uno a 55% capacidad y uno a 16% de
capacidad.
En enero 7 pabellones están a plena capacidad, uno a 55% capacidad, y uno vacío.
En febrero 7 pabellones en plena capacidad, 1 pabellón a 61% de capacidad y otro a un 7% de capacidad.
En marzo 6 pabellones se encontraban a plena capacidad, uno a 73,5%, otro a 34% y otro vacío.
28 Durante la campaña de invierno se almacenaron pabellones de engorda.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 27 de 67

Laguna acumulación

Emisión durante todo el año. Es importante señalar que a partir del 20 de agosto del 2021 se
comenzó a aplicar bacterias a la laguna con la finalidad de disminuir el olor.

**5.2.5 Emisiones de las fuentes ingresadas en el modelo**

A continuación, en la siguiente tabla, se indica la procedencia de las concentraciones de olor
utilizadas para el cálculo de las emisiones consideradas en el modelo:

**Tabla No 16** . Procedencia de las concentraciones consideradas en el modelo.

|Mes<br>modelado|Código<br>informe|Descripción|Periodo de<br>muestreo|
|---|---|---|---|
|Abril, mayo y<br>junio|Inf01E02.<br>O-21-027|Toma de muestra y resultados de concentración de<br>olor mediante olfatometría dinámica en Plantel de<br>Cerdos Monte Verde Bajo.|06 al 25 de<br>abril de 2021|
|Julio, agosto<br>y septiembre|Inf03E01.<br>O-21-027|Toma de muestra y resultados de concentración de<br>olor mediante olfatometría dinámica en Plantel de<br>Cerdos Monte Verde Bajo.|10 de agosto<br>al 30 de<br>septiembre de<br>2021|
|Octubre|Inf01E02.<br>O-20-048|Toma de muestra y resultados de concentración de<br>olor mediante olfatometría dinámica en Plantel de<br>Cerdos Monte Verde Bajo.|07 al 09 de<br>octubre de<br>2020|
|Noviembre|Inf05E01.<br>O-20-048|Toma de muestra y resultados de concentración de<br>olor mediante olfatometría dinámica en Plantel de<br>Cerdos Monte Verde Bajo.|04 al 20 de<br>noviembre de<br>2020|
|Diciembre|Inf07E01.<br>O-20-048|Toma de muestra y resultados de concentración de<br>olor mediante olfatometría dinámica en Plantel de<br>Cerdos Monte Verde Bajo.|07, 09 y 11 de<br>diciembre de<br>2020|
|Enero|Inf09E01.<br>O-20-048|Toma de muestra y resultados de concentración de<br>olor mediante olfatometría dinámica en Plantel de<br>Cerdos Monte Verde Bajo.|11 al 14 de<br>enero de 2021|
|Febrero|Inf11E01.<br>O-20-048|Toma de muestra y resultados de concentración de<br>olor mediante olfatometría dinámica en Plantel de<br>Cerdos Monte Verde Bajo.|01 de febrero<br>al 03 de marzo<br>de 2021|
|Marzo|Inf13E01.<br>O-20-048|Toma de muestra y resultados de concentración de<br>olor mediante olfatometría dinámica en Plantel de<br>Cerdos Monte Verde Bajo.|02 al 05 de<br>marzo de 2021|

A continuación, se presentan las emisiones de los pabellones por cada estación del año.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 28 de 67

**Tabla No 17** . Emisión por pabellón.

|Fuente|Periodo|Emisión de olor (OU /s)<br>E|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Fuente**|**Periodo**|**Otoño**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|**Verano**|**Verano**|**Verano**|
|**Fuente**|**Periodo**|**Abril-**<br>**Junio**|**Julio-**<br>**Septiembre29 **|**Octubre**|**Noviembre**|**Diciembre**|**Enero**|**Febrero**|**Marzo**|
|Maternidad|00:00 -<br>05:00|12|**1.686**|2.345|1.715|975|567|4.476|11.242|
|Maternidad|06:00 -<br>11:00|1.644|**2.711**|8.499|6.216|3.535|1.134|1.593|6.650|
|Maternidad|12:00 -<br>17:00|7.713|**4.219**|29.308|21.436|12.191|10.101|5.823|23.579|
|Maternidad|18:00 -<br>23:00|586|**1.156**|32.825|24.008|13.653|587|4.176|12.617|
|Gestación|00:00 -<br>05:00|1|**701**|598|176|313|74|1.383|1.609|
|Gestación|06:00 -<br>11:00|470|**1.598**|4.315|1.269|2.261|46|988|1.918|
|Gestación|12:00 -<br>17:00|1.466|**3.951**|6.639|1.953|3.478|2.999|5.850|2.726|
|Gestación|18:00 -<br>23:00|44|**22**|4.382|1.289|2.296|247|521|1.915|
|Recría|00:00 -<br>05:00|27|**1.870**|2.082|1.192|2.908|1.076|2.530|3.773|
|Recría|06:00 -<br>11:00|2.283|**2.410**|3.239|1.855|4.523|1.990|1.880|4.356|
|Recría|12:00 -<br>17:00|6.959|**4.575**|11.569|6.626|16.154|7.695|3.392|7.871|
|Recría|18:00 -<br>23:00|142|**1.855**|8.677|4.970|12.116|538|1.138|5.262|
|Engorda|00:00 -<br>05:00|775|**279**|2.778|947|1.684|207|17.681|5.403|
|Engorda|06:00 -<br>11:00|3.236|**3.030**|8.057|2.746|4.883|4.270|10.674|4.187|
|Engorda|12:00 -<br>17:00|5.131|**5.656**|13.891|4.734|8.420|4973|15.010|6.190|
|Engorda|18:00 -<br>23:00|1.585|**271**|2.778|947|1.684|791|5.472|3.564|
|Crianza|00:00 -<br>05:00|401|**279**|2.430|1.070|2.296|642|10.106|4.588|
|Crianza|06:00 -<br>11:00|2.760|**3.030**|5.648|2.301|4.703|3.130|6.277|4.272|
|Crianza|12:00 -<br>17:00|6.045|**5.656**|12.730|5.680|12.287|6.334|9.201|7.031|
|Crianza|18:00 -<br>23:00|863|**271**|5.728|2.959|6.900|665|3.305|4.413|

29 Durante el muestreo realizado en la campaña de invierno, se indicó que el pabellón de crianza estaba
almacenando cerdos de engorda, por lo que se consideraron las emisiones obtenidas en los pabellones de engorda.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 29 de 67

Por otro lado, en las siguientes tablas se presentan las emisiones consideradas en el
lombrifiltro, en la planta de tratamiento de RILes, en la zona de acopio de cama estabilizada,
en la zona de aplicación de purín tratado y en la laguna de acumulación.

**Tabla No 18** . Emisión por fuente.

|Fuente|Condición|Emisión (OU /s)<br>E|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Fuente**|**Condición**|**Otoño**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|**Verano**|**Verano**|**Verano**|
|**Fuente**|**Condición**|**Abril -**<br>**Junio**|**Julio -**<br>**Septiembre**|**Octubre**|**Noviembre**|**Diciembre**|**Enero**|**Febrero**|**Marzo**|
|Lombrifiltro|-|35|1.494|10.923|1.019|4.024|773|272|224|
|Planta<br>de<br>Tratamiento<br>de RILes|- <br>|3.247|5.432|15.602|3.913|<2.032|<375|1.664|11.475|
|Zona<br>de<br>acopio<br>de<br>cama<br>estabilizada|0-1 mes|41|995|1.248|43|1.158|213|3.631|-|
|Zona<br>de<br>acopio<br>de<br>cama<br>estabilizada|1-9<br>meses|679|2.214|2.709|529|2.715|1.462|3.180|2.780|

**Tabla No 19** . Emisión de olor zona de aplicación de purín tratado y laguna de acumulación.

|Mes|Emisión (OU /s)<br>E|Col3|
|---|---|---|
|**Mes**|**Zona de aplicación de purín**<br>**tratado**|**Laguna de acumulación**|
|Enero|4.125|185.323|
|Febrero|6.300|72.229|
|Marzo|20.175|146.327|
|Abril|7.020|253.503|
|Mayo|-|253.503|
|Junio|-|253.503|
|Julio|-|200.429|
|Agosto|-|200.429|
|Septiembre|8.063|23.82730|
|Octubre|9.176|122.406|
|Noviembre|9.176|151.606|
|Diciembre|9.375|201.644|

En relación con la zona de acopio de cama estabilizada, es importante señalar que no se
consideran pilas sobre 9 meses (promedio entre 7 y 11 meses) ya que el olor determinado para
las pilas de 11 meses y 2 años corresponde netamente a nylon-plástico. Es importante señalar
que, la emisión generada por el acopio de 5 días representa la emisión de las pilas recién
llegadas hasta el primer mes; por otro lado, el promedio de la emisión generada por el acopio
de 2 y 6 meses representa la emisión generada entre el primer y noveno mes.

En la siguiente tabla se indica la edad aproximada de las pilas identificadas en el catastro

8

realizado en el mes de septiembr

30 Durante el mes de septiembre disminuyeron las emisiones de la laguna de acumulación porque durante
el mes de agosto se comenzó a aplicar bacterias.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 30 de 67

**Tabla No 20** . Edad de las pilas, septiembre 2021 [31] .

|N°|Edad de la pila|N°|Edad de la pila|N°|Edad de la pila|
|---|---|---|---|---|---|
|1|1 año|20|Sin identificación|39|Sin identificación|
|2|1 año y 2 meses|21|Sin identificación|40|Sin identificación|
|3|1 año y 2 meses|22|Sin identificación|41|Sin identificación|
|4|2 años y 4 meses|23|Sin identificación|42|Sin identificación|
|5|6 meses|24|Sin identificación|43|Sin identificación|
|6|4 meses|25|1 año y 4 meses|44|1 año y 3 meses|
|7|4 meses|26|1 año y 1 mes|45|Sin identificación|
|8|3 meses|27|1 año y 1 mes|46|2 meses|
|9|3 meses|28|Sin identificación|47|2 meses|
|10|2 años y 1 mes|29|Sin identificación|48|Sin identificación|
|11|3 meses|30|Sin identificación|49|Sin identificación|
|12|2 meses|31|Sin identificación|50|Sin identificación|
|13|2 meses|32|Recién llegada|51|Sin identificación|
|14|9 meses|33|Sin identificación|52|Sin identificación|
|15|9 meses|34|Sin identificación|53|Sin identificación|
|16|11 meses|35|Sin identificación|54|Sin identificación|
|17|Sin identificación|36|Sin identificación|55|Sin identificación|
|18|Sin identificación|37|Sin identificación|||
|19|10 meses|38|Sin identificación|Sin identificación|Sin identificación|

**Evaluación de la dispersión de olor del plantel de cerdos**

En el presente apartado se presentan los resultados de la dispersión de las emisiones de olor
generadas en el plantel de Cerdos Monte Verde Bajo, según las fuentes mencionadas en el
punto 5.2 del presente estudio. Los resultados muestran la pluma de dispersión de los olores
en torno al plantel, las que además de simular la dispersión de los gases, entrega las
concentraciones de olor (OU E /m [3] ) en el espacio.

Se presenta un mapa de dispersión de olor, el cual registra el percentil 98 de las
concentraciones horarias, con el objetivo de poder comparar los resultados con el límite de 8
OU E /m [3] establecido por el SEA.

A continuación, se presentan los resultados de la evaluación del modelo de dispersión de las
actuales fuentes del plantel de cerdos.

**5.3.1 Resultados emisión de olor generada en el plantel de cerdos.**

**5.3.1.1 Dispersión de emisiones de olor**

El límite indicado en la RCA N° 068/2019 establece un valor de 8 OU E /m [3] para periodos horarios
con percentil 98.

31 Según el catastro realizado por personal de Proterm, en febrero de 2021.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 31 de 67

Tal como se puede apreciar en la siguiente cartografía, la distribución de la pluma se produce
en forma radial con un centro en los pabellones, abarcando el sector de aplicación de riego y
otro centro en el sector de la laguna de acumulación. El radio de la pluma alcanza 1,48 km [32]
desde el centro de los pabellones y un radio que alcanza 2,06 km [33] desde la laguna de
acumulación. Las isodoras pueden alcanzar valores entre 1 y 68 OU E /m [3] alcanzando la
concentración máxima en el sector donde se emplaza la laguna de acumulación. Fuera de los
límites del proyecto las isodoras trazan valores entre 1 y 68 OU E /m [3] ; a pesar de lo anteriormente
señalado, el receptor que alcanza la mayor concentración alcanza las 7,57 OU E /m [3],
concentración que se encuentra bajo el límite de inmisión de 8 OU E /m [3] .

La isodora de 8 OU E /m3 (valor indicado en la RCA N° 068/2019) alcanza una superficie
aproximada de 33,39 ha alrededor de los pabellones y 124,74 ha alrededor de la laguna de
acumulación.

**Figura No 8** . Concentración de olor generada por las fuentes del plantel de cerdos.

Promedio horario (percentil 98).

32 Distancia referencial.
33 Distancia referencial.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 32 de 67

Con base en la dispersión de emisiones actual del plantel, se determinó un área de influencia
definida según la “Guía para la predicción y evaluación de impactos por olor en el SEIA” [34], como
el espacio contenido por la isodora de 1 OU E /m [3], que corresponde al umbral de detección del
olor compuesto. En la siguiente figura se presenta el área de influencia determinada.

**Figura No 9** . Área de Influencia del plantel de cerdos.

La isodora de 1 OU E /m3, valor que indica la concentración desde el cual el 50% de la población
puede percibir un olor, cubre una superficie de 1.389 ha. La distribución de la pluma es ovalada,
abarcando los pabellones, la zona de aplicación de riego y la laguna de acumulación, con una
longitud aproximada de 4,72 km en dirección noroeste y sureste.

Como se mencionó anteriormente, el área de influencia, determinada por la curva de isoconcentración de 1 OU E /m3, se circunscribe de forma ovalada entre los pabellones y la laguna
de acumulación principalmente, cubriendo un área rural y/o forestal. El área de influencia
circunscribe los receptores que se indican a continuación con su respectiva descripción:

 R1: Sector Huequete 1.

 - R3: Sector San Luis 1.

34 Publicada el 2017 por el Servicio de Evaluación Ambiental.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 33 de 67

 - R4: Sector Huequén.

 - R5: Sector Huequete 3.

 - R6: Sector San Luis 2.

 - R7: Sector Carrizal.

El resto de los receptores (R2 y R8), considerados en la modelación, presentan
concentraciones inferiores a 1 OU E /m3, por lo que se encuentran fuera del área de influencia.

La máxima concentración se produce al interior del predio, cerca de la laguna de acumulación
alcanzando una concentración de 68,15 OU E /m [3] .

**Tabla No 21** . Punto de máxima concentración.

|Descripción|UTM 19S - WGS84|Col3|Concentración de<br>inmisión<br>(OU /m3)<br>E|
|---|---|---|---|
|**Descripción**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|Predio Las Astas|239.632|5.870.574|68,15|

**5.3.1.2 Receptores discretos considerados en la modelación**

En la siguiente tabla se presenta el resultado del Percentil 98 de las concentraciones horarias
para cada receptor al interior del área de influencia y aledaño a ésta.

Tal como se puede apreciar en la siguiente tabla, la operación del plantel de cerdos produce la
concentración de inmisión más alta en el sector Huequén (R4), donde alcanza las 7,57 OU E /m [3],
valor que supera el límite de inmisión de 8 OU E /m [3], establecido en la resolución de calificación
ambiental N° 068/2019. Por otro lado, los receptores R1, R3, R5, R6 y R7 presentan una
concentración de inmisión superior a 1 OU E /m [3], mientras que dos receptores (R2 y R8)
presentan una concentración inferior a 1 OU E /m [3] .

**Tabla No 22** . Concentración receptores. Percentil 98.

|No|Descripción|Distancia a los<br>pabellones (m)|Concentración de<br>inmisión<br>(OU /m3)<br>E|Horas al año<br>>8 OU /m3<br>E|
|---|---|---|---|---|
|R1|Sector Huequete 1|1,93|2,67|32 (0,37%)|
|R2|Sector Huequete 2|2,88|0,60|0 (0,00%)|
|R3|Sector San Luis 1|1,51|4,79|91 (1,04%)|
|R4|Sector Huequén|2,35|7,57|167 (1,91%)|
|R5|Sector Huequete 3|2,19|1,54|24 (0,27%)|
|R6|Sector San Luis 2|0,33|4,26|89 (1,02%)|
|R7|Sector Carrizal|0,53|2,07|32 (0,37%)|
|R8|Fuerte San Diego|3,95|0,45|0 (0,00%)|

En el Anexo N°4, se presenta el análisis de la variación horaria del olor en los receptores
cercanos, al plantel de cerdos, que presentaron valores más altos de concentración.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 34 de 67

**5.3.1.3 Frecuencia de percepción de olor**

**Figura No 10** . Horas sobre 8 OU E /m3 generadas por las fuentes de emisión del plantel de

cerdos. Promedio horario (percentil 98).

En la figura anterior se puede observar las horas al año sobre las 8 OU E /m3. Dicha figura indica
que los lugares sobre un 2% de frecuencia (175 horas), se encuentran superior a la excedencia
entregada por el percentil 98. Las curvas que rodean a los pabellones y a la laguna de
acumulación no circunscriben a ningún receptor; es por lo anteriormente señalado y bajo las
condiciones modeladas, los ocho receptores se encuentran bajo el 2% de las horas
consideradas como umbral de molestia para 8 OU E /m [3] .

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 35 de 67

**5.3.1.4 Análisis FIDOL de la situación actual del plantel de cerdos**

**Tabla No 23.** Protocolo FIDOL en base a receptores definidos.

|Parámetro|Con respecto a receptores discretos.|
|---|---|
|Frecuencia|El plantel opera durante todos los días del año. Sin embargo, ninguno de los receptores<br>presenta superación de las 8 OUE/m3, por sobre el 2% de horas del año.|
|Intensidad|Los ocho receptores considerados en la modelación presentaron concentraciones de<br>inmisión por debajo de 8 OUE/m3. Y las muestras obtenidas directamente de la fuente<br>presentaron una intensidad de olor que variaba entre débil y fuerte.|
|Duración|En relación a la duración, los eventos de olor ocurren en forma intermitente y son<br>mejores al 2% del año en los ocho receptores.|
|Ofensividad|La ofensividad de las fuentes varía desde ligeramente desagradable en la mayoría de<br>las fuentes a desagradable en la planta de tratamiento de RILes y en la laguna de<br>acumulación.|
|Localización|El territorio circunscrito al Área de Influencia presenta un uso principalmente de carácter<br>rural/forestal.|

**Análisis del desempeño del archivo de pronóstico utilizado**

La “Guía para el Uso de Modelos de Calidad de Aire en el SEIA en su capítulo 7” requiere que
se realice una comparación de los registros WRF con información meteorológica local. Para
ello se utilizan los datos disponibles de las estaciones de monitoreo ubicadas en la zona de
interés para el estudio.

Las estaciones utilizadas corresponden a Los Ángeles Oriente y Progreso del sistema SINCA,
ubicadas a 39 km y 36 km del plantel respectivamente. Estas estaciones presentan datos de
temperatura, dirección y velocidad de viento, las cuales serán utilizadas para validar el modelo
meteorológico de pronóstico WRF, no siendo usadas como entradas al modelo.

En el Anexo N°2 se presentan las variables meteorológicas y geofísicas del emplazamiento del
proyecto y en el Anexo No3 se presenta una comparación cualitativa y cuantitativa entre la
meteorología de pronóstico y los datos observados en la estación meteorológica.

De acuerdo a las comparaciones realizadas en forma cualitativa de ciclo diario, promedio
mensual rosa de los vientos y ciclos estacionales, para los parámetros temperatura, velocidad
y dirección de viento para la estación de Los Ángeles Oriente y Progreso se puede indicar que
tanto el modelo WRF y los datos observados presentan valores y patrones similares, que
permiten indicar que los datos WRF se ajustan a la realidad y pueden ser utilizados en la
modelación.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 36 de 67

**Figura No 11** . Estación Meteorológica utilizada en el Análisis de Incertidumbre.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 37 de 67

**6** **Conclusiones**

Con respecto a la modelación de dispersión de olores para el escenario evaluado se concluye
lo siguiente:

1. Las curvas de isoconcentración del percentil 98, indican que las concentraciones de olor

producidas en el plantel varían entre 1 a 68 OU E /m [3], presentándose la máxima
concentración cerca de la laguna de acumulación, con un valor de 68,15 OU E /m [3] .

2. Ningún receptor supera el límite de 8 OU E /m [3], en el percentil 98. El receptor que

presenta la máxima concentración es R4 (Sector Huequén) y alcanza las 7,57 OU E /m [3] .

3. El área de influencia, descrita por la isodora de 1 OU E /m [3], presenta una forma ovalada

abarcando los pabellones, la zona de aplicación de riego y la laguna de acumulación,
cubriendo un área rural y/o forestal. El área de influencia posee una longitud aproximada
de 4,72 km con dirección noroeste y sureste; es importante señalar que el área de
influencia posee una superficie de 1.389 ha y circunscribe a seis receptores (R1, R3,
R4, R5, R6 y R7).

4. A partir del análisis cualitativo y cuantitativo, se puede concluir que el modelo de

pronóstico WRF presenta valores de dirección y velocidad de viento similares a los datos
observados. Al analizar las velocidades promedio y direcciones frecuentes del viento,
los valores modelados concuerdan con las observaciones. Por lo tanto, de acuerdo a lo
mostrado en el análisis cuantitativo y cualitativo de la estación de Los Ángeles Oriente
y Progreso, el modelo WRF utilizado para el análisis de dispersión atmosférica es
adecuado y concuerda con las condiciones de la realidad.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 38 de 67

**7** **Anexos**

**Anexo No1. Esquema de funcionamiento Calpuff y elementos de modelación**

El presente Anexo contiene el archivo magnético el cual contiene la información que se utilizó
para realizar la modelación atmosférica, dicha información corresponde a los input y output
ingresados para la modelación de los módulos del modelo (CALPUFF, CALPOST y CALRANK)
y el archivo Meteorológico WRF.

Por lo tanto, en el caso que se requiera replicar la modelación realizada, esta se podrá hacer
utilizando los archivos presentes en este Anexo.

**Figura No 12** . Esquema funcionamiento CALPUFF.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 39 de 67

**Anexo No2. Cálculo del flujo de los pabellones.**

En la siguiente tabla, se presentan los parámetros considerados para calcular el flujo en los
cuatro pabellones, medidos el pasado 12 y 13 de agosto:

**Tabla No 24.** Flujo considerado en los pabellones.

|Pabellón|Hora|Área<br>(m2)|Velocidad<br>(m/s)|Flujo<br>(m3/s)|Factor de<br>emisión|
|---|---|---|---|---|---|
|Maternidad35|00:20|11,72|0,304|3,88|0,40|
|Maternidad35|09:16|20,45|0,280|6,24|0,64|
|Maternidad35|12:24|19,44|0,458|9,71|1,00|
|Maternidad35|21:00|11,31|0,216|2,66|0,27|
|Gestación|00:35|14,86|0,400|5,94|0,18|
|Gestación|09:43|35,73|0,379|13,54|0,40|
|Gestación|12:54|84,99|0,394|33,48|1,00|
|Gestación|21:20|1,20|0,158|0,19|0,01|
|Recría36|00:55|35,15|0,218|8,76|0,41|
|Recría36|09:55|32,42|0,305|11,29|0,53|
|Recría36|12:44|31,80|0,590|21,43|1,00|
|Recría36|21:30|38,85|0,196|8,69|0,41|
|Engorda|01:10|14,00|0,297|4,16|0,05|
|Engorda|08:35|117,15|0,386|45,22|0,54|
|Engorda|12:00|134,00|0,630|84,42|1,00|
|Engorda|21:50|14,00|0,289|4,05|0,05|

Cabe señalar, que en las mediciones realizadas no se consideró el pabellón de crianza porque
durante la campaña de invierno se almacenaron cerdos de engorda.

35 Para calcular la emisión se aplica un factor de 11/12, correspondiente a las salas en uso. La medición de flujo se
realizó en el pabellón completo.
36 Para calcular la emisión se aplica un factor de 7/8, correspondiente a las salas en uso. La medición de flujo se
realizó en el pabellón completo.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 40 de 67

**Anexo No3. Descripción meteorológica y geofísica de la zona**

En el siguiente anexo se presenta el análisis de la meteorología de la zona modelada. Los datos
de meteorología expresados a continuación fueron extraídos desde el SINCA en la estación de
Los Ángeles Oriente y Progreso.

**Tabla No 25.** Datos meteorológicos.

|Nombre de la Estación|Col2|EM Los Ángeles Oriente|EM Progreso|
|---|---|---|---|
|Coordenada UTM,<br>Datum WGS 84 -<br>Zona Horaria 18H|Este (m)|736.622 m E|740.990 m E|
|Coordenada UTM,<br>Datum WGS 84 -<br>Zona Horaria 18H|Norte (m)|5.850.392 m S|5.894.115 m S|
|Distancia con respecto a la fuente|Distancia con respecto a la fuente|39,4|36,8|
|"Periodo del registro<br>(desde DD/MM/AA - hasta<br>DD/MM/AA)"|"Periodo del registro<br>(desde DD/MM/AA - hasta<br>DD/MM/AA)"|01/01/2014 - hasta<br>31/12/2014|01/01/2014 - hasta<br>31/12/2014|
|Meteorología|Meteorología|Velocidad Viento (VV)<br>Dirección Viento (DV)<br>Temperatura (TA)|Velocidad Viento (VV)<br>Dirección Viento (DV)<br>Temperatura (TA)|

**7.3.1 Cantidad de datos**

Para realizar el análisis meteorológico y el análisis de incertidumbre es necesario verificar la
cantidad de datos presentes en las mediciones ambientales de las estaciones. A continuación,
se muestran los datos de las estaciones en la serie de tiempo para comprobar que no existen
periodos extensos sin datos durante el año de análisis.

**Estación Los Ángeles Oriente:**

**Figura No 13** . Serie de tiempo anual para velocidad de viento. Estación Los Ángeles Oriente.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 41 de 67

**Figura No 14** . Serie de tiempo anual para dirección de viento. Estación Los Ángeles Oriente.

**Figura No 15** . Serie de tiempo anual para temperatura. Estación Los Ángeles Oriente.

A partir de las gráficas de serie de tiempo de los parámetros temperatura, velocidad y dirección
de viento se evidencia que no existen periodos extensos sin datos, presentándose sólo
ausencias de forma puntual. De acuerdo a la tabla a continuación, las gráficas indican una
cantidad de datos mínima de 99,9% en el periodo de un año para cada variable, superior al
70% sugerido por la Guía para modelos de calidad del aire del SEA.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 42 de 67

**Tabla No 26.** Datos válidos estación meteorológica Los Ángeles Oriente.

|Porcentaje de datos meteorológicos disponibles - EM Los Ángeles Oriente|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Parám<br>/mes|E|F|M|A|M|J|J|A|S|O|N|D|Total|
|VV|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|
|DV|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|
|T|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|

**Estación Progreso:**

**Figura No 16** . Serie de tiempo anual para velocidad de viento. Estación Progreso.

**Figura No 17** . Serie de tiempo anual para dirección de viento. Estación Progreso.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 43 de 67

**Figura No 18** . Serie de tiempo anual para temperatura. Estación Progreso.

**Tabla No 27.** Datos válidos estación meteorológica Progreso.

|Porcentaje de datos meteorológicos disponibles - EM Progreso|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Parám<br>/mes|E|F|M|A|M|J|J|A|S|O|N|D|Total|
|VV|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|
|DV|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|
|T|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|

A partir de las gráficas de serie de tiempo de los parámetros temperatura, velocidad y dirección
de viento se evidencia que no existen periodos extensos sin datos, presentándose sólo
ausencias de forma puntual. De acuerdo a la tabla a continuación, las gráficas indican una
cantidad de datos mínima de 99,9% en el periodo de un año para cada variable, superior al
70% sugerido por la Guía para modelos de calidad del aire del SEA.

**7.3.2 Gráficos Ciclo diario**

Velocidad de viento

En los siguientes gráficos se presenta los ciclos diarios promedios de temperatura, velocidad y
dirección del viento; junto con su variabilidad entre el percentil 5% a 95% (Rango 90%
observado).

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 44 de 67

**Figura No 19** . Ciclo diario velocidad viento - datos observados estación Los Ángeles Oriente

- Año 2014.

**Figura No 20** . Ciclo diario velocidad viento - datos observados estación Progreso- Año 2014.

En relación al ciclo diario promedio de la velocidad de viento se observa una velocidad promedio
mínima de 1 m/s en las horas de la noche y una velocidad máxima promedio de 2,5 m/s en las
horas de la tarde. Durante el año, la velocidad del viento puede variar entre calmas y 5 m/s. La
velocidad de viento en dicha zona, favorece la dispersión de emisiones.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 45 de 67

Dirección de viento

**Figura No 21** . Ciclo diario dirección viento - datos observados estación Los Ángeles OrienteAño 2014.

**Figura No 22** . Ciclo diario dirección viento - datos observados estación Progreso - Año 2014.

En relación al ciclo diario de la dirección de viento se observa que durante el día predominan
los vientos provenientes del suroeste y/o el noreste dependiendo de la estación. Esta condición
indica que los contaminantes se dispersan favorablemente en las direcciones hacia sureste y
el noreste dependiendo de la estación.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 46 de 67

Temperatura

**Figura No 23** . Ciclo diario temperatura - datos observados estación Los Ángeles OrienteAño 2014.

**Figura No 24** . Ciclo diario temperatura - datos observados estación Progreso - Año 2014.

Respecto al ciclo diario de la temperatura, se observa una temperatura promedio variable de
8°C a 20°C. La temperatura máxima ocurre a las 16:00 horas mientras que la mínima sucede
a las 7:00 horas. Durante el año, la temperatura puede variar entre ±10°C respecto al promedio,
alcanzando máximos de 3 °C y mínimas de 0°C, respecto al 90% observado.

**7.3.3 Gráficos Distribución de Vientos**

En las siguientes figuras se muestra la distribución de vientos en las estaciones meteorológicas
existentes. De las figuras se concluye que los vientos en calma representan entre un 10 % y
15%, mientras que la mayor parte de las velocidades ocurren en el rango de 0,5 a 4 m/s
correspondiente a más de un 73% en promedio. La velocidad más frecuente corresponde al
rango entre 0,5 - 2 m/s con un 35% en promedio. Estas condiciones favorecen levemente la
dispersión de emisiones.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 47 de 67

**Figura No 25** . Distribución de vientos - datos observados estación Los Ángeles Oriente - Año

2014.

**Figura No 26** . Distribución de vientos - datos observados estación Progreso - Año 2014.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 48 de 67

**7.3.4 Rosa de los vientos**

De la rosa de los vientos se puede concluir que los vientos varían principalmente entre el
suroeste (componente principal) y noreste, dependiendo de la estación. Los vientos con mayor
velocidad provienen desde el norte y noreste en invierno, pero los vientos desde el sur
presentan mayor frecuencia.

**Figura No 27** . Rosa de los vientos - datos observados estación Los Ángeles Oriente - Año

2014.

**Figura No 28** . Rosa de los vientos - datos observados estación Progreso - Año 2014.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 49 de 67

Las condiciones anteriormente descritas, indican que la dispersión de emisiones ocurrirá
principalmente hacia el norte y/o noreste en el verano, sur-suroeste de la planta en el invierno,
lo que puede corroborar con los resultados del modelo de dispersión.

**Por estación**

En los gráficos siguientes se muestran las rosa de los vientos para cada estación del año.

(a) Otoño - EM Los Ángeles Oriente 2014. (b) Otoño - EM Progreso 2014.

(c) Invierno - EM Los Ángeles Oriente 2014. (d) Invierno - EM Progreso 2014.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 50 de 67

(e) Primavera - EM Los Ángeles Oriente

2014.

(f) Primavera - EM Progreso 2014.

(g) Verano - EM Los Ángeles Oriente 2014. (h) Verano - EM Progreso 2014.

**Figura No 29** . Rosa de los vientos por estación.

De acuerdo a las rosas de los vientos anteriores, se puede indicar lo siguiente:

 - En otoño e invierno los vientos provienen tanto desde el noreste como el sureste, debido
a los periodos de inestabilidad, presentándose además las velocidades más altas del
año con vientos por sobre los 6 m/s. Por lo tanto en estos periodos la dispersión de
emisiones puede darse tanto hacia el noreste como del suroeste. En otoño son más

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 51 de 67

frecuentes los vientos desde el sur mientras que en invierno son más frecuentes los
vientos desde el norte.

 - En primavera y verano los vientos provienen principalmente desde el suroeste. Por lo
tanto en estos periodos la dispersión de emisiones ocurre principalmente hacia el

noreste.

**7.3.5 Gráficos ciclo estacional**

En las figuras presentes a continuación se observa la variación estacional de los ciclos de
velocidad y dirección de viento. En relación a la dirección de viento en los meses de primavera
y verano, se mantiene el ciclo diario con vientos desde el suroeste en las horas del día. Durante
los meses de mayo a septiembre los vientos varían entre el suroeste y noreste. Lo anterior
indica que la dispersión de contaminantes ocurrirá hacia el suroeste en los meses de invierno,
y noreste en meses de verano.

Respecto a la velocidad del viento, durante las horas del día en primavera y verano ocurren las
mayores velocidades, sobre los 3 m/s, mientras que en la noche la velocidad desciende en
promedio a 1 m/s. En los meses de invierno las velocidades también varían durante el día
alcanzando un máximo de 2 m/s en las horas de la tarde para luego disminuir a calmas o 1 m/s
durante la noche y la mañana.

**Figura No 30** . Ciclos estacionales - datos observados estación Los Ángeles Oriente - Año

2014.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 52 de 67

**Figura No 31** . Ciclos estacionales - datos observados estación Progreso - Año 2014. [ 37]

**7.3.6 Elevación de Terreno**

La zona modelada corresponde a un sector ubicado en el valle central cercano a la cordillera.
En la zona del proyecto se observan una altura promedio de 300 metros sobre el nivel del mar
no observándose variaciones abruptas de nivel a un radio de 20 km de distancia desde la fuente
hacia el este y 30 km hacia el oeste.

37 La flechas indican hacia donde sopla el viento

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 53 de 67

**Figura No 32** . Elevación de terreno WRF.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 54 de 67

**Anexo No4. Análisis incertidumbre**

La “Guía para el Uso de Modelos de Calidad de Aire en el SEIA en su capítulo 7” requiere que
se realice una comparación de los registros WRF con información meteorológica local. Para
ello se utilizan los datos disponibles en las estaciones de monitoreo ubicadas en la zona de
interés para el estudio.

Las estaciones de monitoreo analizadas Los Ángeles Oriente y Progreso se encuentran a 39,4
y 36,8 km del plantel de. Los parámetros monitoreados por dicha estación corresponden a
temperatura, velocidad y dirección de viento. Para la evaluación del desempeño se realiza una
comparación entre las variables temperatura, velocidad y dirección de viento, ya que éstas son
las variables de mayor interés.

Con el fin de evaluar el desempeño, se realiza un análisis cualitativo de los parámetros de
interés. El análisis cualitativo se desarrolla mediante la comparación entre los ciclos diarios
promedios, mensuales, ciclos estacionales y rosa de los vientos.

Definiciones

**Datos observados:** Se refiere a los datos provenientes desde una estación de monitoreo
durante un periodo de interés.

**Datos modelados:** Se refiere a los datos meteorológicos provenientes desde un modelo de
pronóstico como WRF o MM5.

**Rango 90% observado:** Se refiere a la variación de los datos entre el percentil 5 y percentil 95
en una hora o mes específico.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 55 de 67

**7.4.1 Ciclos Diarios promedios**

Velocidad de viento

**Figura No 33** . Comparación ciclo diario de velocidad de viento entre modelación observada y

proyectada para la estación Los Ángeles Oriente.

**Figura No 34** . Comparación ciclo diario de velocidad de viento entre modelación observada y

proyectada para la estación Progreso.

De la figura se puede concluir que el ciclo diario promedio de velocidad de viento entre los datos
observados y los datos modelados presentan valores similares con una diferencia de ±1,5 m/s.
El modelo WRF considera velocidades más altas que los datos observados. Respecto a la
variación de velocidad del ciclo diario, el modelo WRF y los datos observados poseen el mismo
patrón del modelo de pronóstico y el observado. Dado estas circunstancias, respecto al ciclo
diario promedio de velocidad, el modelo es adecuado.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 56 de 67

Dirección de Viento

De la figura se puede concluir que el ciclo diario considerando la moda de la dirección de viento
entre los datos observados y los datos modelados presentan valores similares con una
diferencia máxima de ±45°. Respecto a la variación de dirección de viento del ciclo diario, el
modelo WRF y los datos observados poseen el mismo patrón del modelo de pronóstico y el
observado. Dado estas circunstancias, respecto al ciclo diario de dirección, el modelo es
adecuado.

**Figura No 35** . Comparación ciclo diario de dirección de viento entre modelación observada y

proyectada para la estación Los Ángeles Oriente.

**Figura No 36** . Comparación ciclo diario de dirección de viento entre modelación observada y

proyectada para la estación Progreso.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 57 de 67

Temperatura

**Figura No 37** . Comparación ciclo diario de temperatura entre modelación observada y

proyectada para la estación Los Ángeles Oriente.

**Figura No 38** . Comparación ciclo diario de temperatura entre modelación observada y

proyectada para la estación Progreso.

De las figuras se puede concluir que los ciclos diarios promedios de temperatura entre los datos
observados y los datos modelados presentan valores similares con una diferencia de ±3°C.
Además, la variación diaria de temperatura posee el mismo patrón del modelo de pronóstico y
el observado. Dado estas circunstancias, respecto al ciclo diario promedio de temperatura, el
modelo es adecuado.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 58 de 67

**7.4.2 Promedio Mensuales**

Velocidad de viento

De la figura se puede concluir que el promedio mensual de velocidad de viento entre los datos
observados y los datos modelados presentan valores similares con una diferencia de ±1,5 m/s.
El modelo WRF considera velocidades más altas que los datos observados. Respecto a la
variación de velocidad del ciclo diario, el modelo WRF y los datos observados poseen el mismo
patrón del modelo de pronóstico y el observado. Dado estas circunstancias, respecto al ciclo
diario promedio de velocidad, el modelo es adecuado.

**Figura No 39** . Comparación promedio mensual de velocidad de viento entre modelación

observada y proyectada para la estación Los Ángeles Oriente.

**Figura No 40** . Comparación promedio mensual de velocidad de viento entre modelación

observada y proyectada para la estación Progreso.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 59 de 67

Dirección de viento

De la figura se puede concluir que la moda mensual de la dirección de viento entre los datos
observados y los datos modelados presentan valores similares con una diferencia en el mes de
agosto. Respecto a la variación de dirección de viento del ciclo diario, el modelo WRF y los
datos observados poseen el mismo patrón del modelo de pronóstico y el observado. Dado estas
circunstancias, respecto al ciclo diario de dirección, el modelo es adecuado.

**Figura No 41** . Comparación moda mensual de dirección de viento entre modelación

observada y proyectada para la estación Los Ángeles Oriente.

**Figura No 42** . Comparación moda mensual de dirección de viento entre modelación

observada y proyectada para la estación Progreso.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 60 de 67

Temperatura

**Figura No 43** . Comparación promedio mensual de temperatura entre modelación observada y

proyectada para la estación Los Ángeles Oriente.

**Figura No 44** . Comparación promedio mensual de temperatura entre modelación observada y

proyectada para la estación Progreso.

De las figuras se puede concluir que los promedios mensuales de temperatura entre los datos
observados y los datos modelados presentan valores similares con una diferencia de ±3°C.
Además, la variación diaria de temperatura posee el mismo patrón del modelo de pronóstico y
el observado. Dado estas circunstancias, respecto al ciclo diario promedio de temperatura, el
modelo es adecuado.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 61 de 67

**7.4.3 Dirección de viento**

Rosa de los vientos

|(a) Los Ángeles Oriente - OBS|(b) Los Ángeles Oriente - WRF|
|---|---|
|(c) Progreso - OBS|<br> <br>(d) Progreso - WRF|

**Figura No 45** . Comparación Rosas de viento.

De las rosas de los vientos mostradas, se puede observar que predominan los vientos
principalmente desde el sur y sureste, y de forma secundaria desde el norte. En general el
modelo de pronóstico y los datos observados son similares exceptuando la mayor presencia de
los vientos del norte. Ambos modelos presentan similar patrón de viento, no obstante, los datos
modelados indican velocidades sobre los 6 m/s como una componente importante, mientras

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 62 de 67

que los datos observados no predominan sobre las otras velocidades. Esto último puede
observarse mejor en el análisis de los gráficos de ciclo estacionales. Finalmente, respecto a la
dirección de los vientos el modelo WRF es adecuado.

Gráficos Ciclo estacionales

En las figuras siguientes se muestran las variaciones de la velocidad y dirección del viento, en
forma diaria y estacional. De los gráficos se puede concluir que el modelo de pronóstico WRF
presenta valores similares a los datos observados, dado el patrón similar en forma horaria y
mensual.

En referencia al patrón de las velocidades de viento, se observa que ambos modelos presentan
las mayores velocidades durante los meses de verano (en horas de la tarde) y el mes de junio.
Las gráficas indican que durante el año la velocidad del viento es más alta en 1,5 m/s que en
los datos modelados.

Respecto a la dirección del viento a lo largo del año se observan direcciones similares,
provenientes principalmente desde el sur y en los meses de invierno desde el norte. Como se
puede observar tanto el modelo WRF y los datos observados presentan direcciones similares.

**Figura No 46** . Variación estacional de velocidad y dirección de viento. Datos observados.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 63 de 67

**Figura No 47** . Variación estacional de velocidad y dirección de viento. Datos modelados.

**Figura No 48** . Variación estacional de velocidad y dirección de viento. Datos observados.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 64 de 67

**Figura No 49** . Variación estacional de velocidad y dirección de viento. Datos modelados.

**7.4.4 Análisis cuantitativo**

De acuerdo a lo solicitado por la Guía para uso de modelos de calidad del aire en el SEIA, se
presenta el análisis cuantitativo de las variables meteorológicas involucradas en la modelación.
En el análisis se incluye las variables temperatura y velocidad de viento, con las métricas
solicitadas: Sesgo (error medio), coeficiente de correlación y error medio cuadrático.

**Tabla No 28.** Análisis cuantitativo.

|Parámetro|Métrica|Los Ángeles Oriente|Col4|Progreso|Col6|
|---|---|---|---|---|---|
|**Parámetro**|**Métrica**|**Horario**|**Diario**|**Horario**|**Diario**|
|**Velocidad**|** RMSE (m/s)**|1,62|1,30|1,98|1,68|
|**Velocidad**|**BIAS (m/s)**|0,98|0,98|1,45|1,45|
|**Dirección**|**RMSE (°)**|1,84|12,96|-2,88|5,22|
|**Temperatura**|**BIAS (°C)**|-0,28|-0,28|0,03|0,03|

De acuerdo a las comparaciones realizadas en forma cualitativa de ciclo diario, promedio
mensual rosa de los vientos y ciclos estacionales, y cuantitativa para los parámetros
temperatura, velocidad y dirección de viento se puede indicar que tanto el modelo WRF y los
datos observados presentan valores y patrones similares, que permiten indicar que los datos
WRF se ajustan a la realidad y pueden ser utilizados en la modelación.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 65 de 67

**Anexo No4. Análisis de receptores.**

A continuación, se presentan los gráficos ciclo diario de las concentraciones de olor, para los
tres receptores que presentaron las concentraciones más altas (R3, R4 y R6 correspondientes
a los sectores San Luis 1, Huequén y San Luis 2, respectivamente). Estos gráficos permiten
detectar las horas en donde ocurren las mayores concentraciones durante el día, respecto al
90% observado del tiempo (variación entre el percentil 5 y percentil 95).

A continuación, se muestra el comportamiento diario de los tres receptores que presentaron las
concentraciones más altas.

Receptor 3 - Sector San Luis 1

**Figura No 50** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No3.

En la figura anterior, se muestra el comportamiento de las concentraciones de olor durante el
día. Acá se puede observar que los mayores valores se presentan durante la madrugada, entre
las 00:00 y las 06:00 de la mañana, alcanzando las 4,9 OU E /m3, mientras que las horas de
menor concentración de olor se registran entre las 10:00 y las 18:00 hrs.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 66 de 67Receptor 4 Sector Huequén.

**Figura No 51** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No4.

En la figura anterior se muestra, el comportamiento de las concentraciones de olor durante el
día. Acá se puede observar que los mayores valores se presentan durante la noche y la
madrugada, entre las 20:00 y las 08:00 hrs, alcanzando las 6,6 OU E /m3, mientras que las horas
de menor concentración de olor se registran entre las 09:00 y las 19:00 hrs.

Receptor 6 - Sector San Luis 2.

**Figura No 52** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No6.

En la figura anterior se muestra, el comportamiento de las concentraciones de olor durante el
día. Acá se puede observar que los mayores valores se presentan durante la noche y
madrugada, entre las 20:00 y las 08:00 hrs, alcanzando las 4,2 OU E /m3, mientras que las horas
de menor concentración de olor se registran entre las 09:00 y las 19:00 hrs.

Inf04E01.O-21-027.EIO.Plantel Monte Verde Bajo.Modelación.cfa 67 de 67