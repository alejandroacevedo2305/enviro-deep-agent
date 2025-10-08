---
title: Sin título
author: Jasmine
date: D:20230529205105-04'00'
language: es
type: report
pages: 45
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - E S T U D I O D E D I S P E R S I Ó N D E C O N T A M I N A N T E S A T M O S F É R I C O S
-->

# E S T U D I O D E D I S P E R S I Ó N D E C O N T A M I N A N T E S A T M O S F É R I C O S

## ESTUDIO DE IMPACTO AMBIENTAL MACRO LOTEO LOS ÁNGELES

INFORME TÉCNICO ELABORADO PARA:

382-IEP23

Estudio de Dispersión de Contaminantes Atmosféricos

Declaración de Impacto Ambiental, Proyecto “Macro Loteo Los Ángeles”

Comuna de Los Ángeles, Provincia del Biobío, Región del Biobío.

**© SICAM Ingeniería**

Estudios Técnicos en Medio Ambiente

Casa matriz: Prieto Sur 965, Temuco. Chile.

Teléfono (045) 2 668119

[Página web: www.sicam,cl](http://www.sicam,cl/)

[Contacto: cvarela@sicam.cl](mailto:cvarela@sicam.cl)

Mayo, 2023

**Equipo Técnico**

**MSc. Cristian Varela Bruce**

Ingeniero Ambiental
Jefe Modelación

Elaboración de informe.

**Ing. Jasmine Bastidas Muñoz**
Ingeniero Ambiental
Análisis de calidad del aire.

Elaboración de informe.

|Versión|Fecha|Elaborado por|Revisado por|Aprobado por|
|---|---|---|---|---|
|V.1|29-05-2023|Cristian Varela B.|Jasmine Bastidas||
||||||

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 2

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**ÍNDICE**

1 ANTECEDENTES GENERALES DEL ESTUDIO ...................................................................................................... 6

1.1 Identificación de la empresa consultora ....................................................................................................... 6

1.2 Objetivos de la consultoría................................................................................................................................. 6

1.3 Alcances del Informe ............................................................................................................................................ 6

2 DESCRIPCIÓN GENERAL DEL PROYECTO .......................................................................................................... 7

3 MARCO NORMATIVO ............................................................................................................................................... 8

4 METODOLOGÍA DE MODELACIÓN ...................................................................................................................... 9

4.1 Modelo Meteorológico........................................................................................................................................ 9

4.2 Características del Dominio de Modelación y su Entorno .................................................................... 10

4.2.1 Dominio de Modelación............................................................................................................................... 10

4.2.2 Topografía y Uso de Suelo .......................................................................................................................... 11

5 CARACTERIZACIÓN METEOROLÓGICA ............................................................................................................ 12

5.1 Información Meteorológica ............................................................................................................................. 12

5.2 Rosas de Los Vientos .......................................................................................................................................... 14

5.2.1 Series de Tiempo y ciclos diarios .............................................................................................................. 15

5.2.2 Ciclos Estacionales .......................................................................................................................................... 18

5.2.3 Ciclos estacionales de datos en altura .................................................................................................... 20

6 CARACTERIZACIÓN DE CALIDAD DEL AIRE .................................................................................................... 22

7 CARACTERIZACIÓN DE LA FUENTE Y SUS EMISIONES ............................................................................... 27

7.1 Identificación de las fuentes emisoras ......................................................................................................... 27

7.2 Perfil Temporal...................................................................................................................................................... 27

8 RESULTADOS DE LA MODELACIÓN ................................................................................................................... 28

8.1 Validación Meteorológica ................................................................................................................................. 28

8.2 Resultados de la Modelación Meteorológica ............................................................................................ 30

8.3 Resultados de la Modelación de Dispersión de Contaminantes ........................................................ 35

8.3.1 Determinación de concentración en el punto de Máximo Impacto Etapa según etapa. ..... 35

8.3.2 Mapas de Isoconcentraciones Construcción ........................................................................................ 35

8.3.3 Determinación de receptores y concentración de inmisión ........................................................... 41

8.3.4 Determinación de impactos y área de influencia ................................................................................ 43

9 CONCLUSIONES ........................................................................................................................................................ 44

10 REFERENCIAS......................................................................................................................................................... 45

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 3

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**ÍNDICE DE FIGURAS**

Figura 1. Ubicación del Proyecto .................................................................................................................................... 7
Figura 2. Protocolo de Modelación ................................................................................................................................ 9
Figura 3. Esquema general de funcionamiento de WRF-ARW ........................................................................... 10
Figura 4. Dominio de modelación WRF/CALPUFF .................................................................................................. 11
Figura 5. Topografía del área de modelación 3D .................................................................................................... 12
Figura 6. Ubicación Estaciones de Monitoreo .......................................................................................................... 13
Figura 7. Rosas de los vientos estacionales (A: verano, B: otoño, C: Invierno, D: Primavera).................. 14
Figura 8. Series de tiempo horaria de variables meteorológicas año 2022 .................................................. 16
Figura 9. Ciclos diarios de variables meteorológicas año 2022 ......................................................................... 17
Figura 10. Variación estacional del ciclo diario de la Temperatura .................................................................. 18
Figura 11. Variación estacional del ciclo diario de la velocidad del viento ................................................... 19
Figura 12. Variación estacional del ciclo diario de la dirección del viento .................................................... 19
Figura 13. Variación estacional del perfil vertical de temperatura.................................................................... 20
Figura 14. Variación estacional del perfil vertical de velocidad de viento ..................................................... 21
Figura 15. Evaluación de Norma Anual y Diaria para MP2,5............................................................................... 23
Figura 16. Serie de tiempo MP2,5 año 2020-2022 ................................................................................................. 23
Figura 17. Ciclo diario de concentraciones de MP2,5 año 2022 ........................................................................ 24
Figura 18. Evaluación de Norma Anual y Diaria para MP10................................................................................ 25
Figura 19. Serie de tiempo MP10 año 2020-2022 .................................................................................................. 26
Figura 20. Ciclo diario de concentraciones de MP10 año 2019 ......................................................................... 26
Figura 21. Temperatura observada v/s modelada serie anual ........................................................................... 28
Figura 22. Correlación temperatura observada v/s modelada serie anual .................................................... 28
Figura 23. velocidad del viento modelada v/s modelada serie anual ............................................................. 29
Figura 24. Correlación Velocidad del viento observada v/s modelada serie anual .................................... 29
Figura 25. Precipitaciones modelada v/s modelada serie anual ........................................................................ 29
Figura 26. Campos de viento estación: Verano-periodo nocturno .................................................................. 31
Figura 27. Campos de viento estación: Verano-periodo diurno ....................................................................... 31
Figura 28. Campos de viento estación: Otoño-periodo nocturno .................................................................... 32
Figura 29. Campos de viento estación: Otoño-periodo diurno ......................................................................... 32
Figura 30. Campos de viento estación: Invierno-periodo nocturno ................................................................ 33
Figura 31. Campos de viento estación: Invierno-periodo diurno ..................................................................... 33
Figura 32. Campos de viento estación: Primavera-periodo nocturno ............................................................. 34
Figura 33. Campos de viento estación: Primavera-periodo diurno .................................................................. 34
Figura 34. Modelación de Dispersión de MP10 P98 promedio 24 hrs. Fase Construcción. .................... 36
Figura 35. Modelación de Dispersión de MP2.5 P98 promedio 24 hrs. Fase Construcción. ................... 37
Figura 36. Modelación de Dispersión de CO promedio 1 hora Fase Construcción. .................................. 38
Figura 37. Modelación de Dispersión de SO 2 P99 promedio 24 hora Fase Construcción ....................... 39
Figura 38. Modelación de Dispersión de NOx máximo horario Fase Construcción. .................................. 40
Figura 39. Receptores evaluados en el proyecto .................................................................................................... 41
Figura 40. Área de influencia MP2,5 ............................................................................................................................ 43

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 4

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**ÍNDICE DE TABLAS**

Tabla 1. Norma de calidad del aire para Material Particulado y gases. ............................................................ 8
Tabla 2. Coordenadas vértices del área de modelación del proyecto (Huso 18/19- WGS84) ............... 11
Tabla 3. Estaciones meteorológicas y calidad del aire para datos en superficie cercanas al proyecto

................................................................................................................................................................................................... 12

Tabla 4. Ubicación Estación de Radiosondeo para datos de altura ................................................................. 13

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La información meteorológica utilizada proviene de estaciones de superficie cercanas al área del proyecto y en altura de una estación de radio sondeo. A continuación, en la Tabla 3 y -->

**Tabla 4: , se detallan las fuentes de información y sus características, para datos de calidad**

| Nombre Estación | Coordenadas UTM (18<br>H) | Col3 | Calidad del<br>Aire | Col5 | Variables<br>meteorológicas | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nombre Estación | ~~UTM-E~~ | ~~UTM-S~~ | ~~MP2,5~~ | ~~MP10~~ | ~~RG~~ | ~~HR~~ | ~~TA~~ | ~~DV~~ | ~~VV~~ | ~~PP*~~ |
| ~~21 Mayo (MMA)~~ | ~~ 733331~~ | ~~5849585~~ | ~~x ~~ | ~~x ~~ | ~~x ~~ | ~~x ~~ | ~~x ~~ | ~~x ~~ | ~~x ~~ |  |
| ~~Human (AGROMET)~~ |  |  |  |  |  |  |  |  |  | ~~x ~~ |

<!-- Estadísticas: 3 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- RG: Radiación global; HR: humedad relativa; TA: Temperatura ambiente; DV: dirección del viento; VV: velocidad del viento; PP: Precipitación Acumulada SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 12 -->
<!-- FIN TABLA 4 -->

Tabla 5. Parámetros de cumplimiento de norma de MP2,5 años 2020-2022 .............................................. 22
Tabla 6. Parámetros de cumplimiento de norma de MP10 años 2020-2022 ............................................... 25
Tabla 7. Fuentes de emisiones atmosféricas, durante etapa de construcción del Proyecto. .................. 27
Tabla 8. Días de funcionamiento de la fuente.......................................................................................................... 27

Tabla 9. Estadísticos de Desempeño del Modelo Meteorológico .................................................................... 30
Tabla 10. Resultados de la modelación de calidad del aire (máximo impacto). .......................................... 35
Tabla 11. Identificación de los receptores discretos .............................................................................................. 41
Tabla 12. Resultados de la modelación de calidad del aire (MP10) Construcción ..................................... 42
Tabla 13. Resultados de la modelación de calidad del aire (MP2,5) Construcción .................................... 42

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 5

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**1** **ANTECEDENTES GENERALES DEL ESTUDIO**

**1.1** **Identificación de la empresa consultora**

|Nombre|: SICAM INGENIERÍA|
|---|---|
|RUT|: 76.244.668-5|
|Dirección|: PRIETO SUR 965|
|Comuna|: TEMUCO|
|Región|: ARAUCANÍA|
|Email|: servicios@sicam.cl|
|Teléfono|: 61575998|
|WEB|: www.sicam.cl|

**1.2** **Objetivos de la consultoría**

Determinar, mediante modelación WRF/CALPUFF, la dispersión de los contaminantes

atmosféricos generados por las actividades asociadas a la etapa de construcción y operación

del proyecto “Macroloteo Los Ángeles”, sobre las poblaciones circundantes.

**1.3** **Alcances del Informe**

El presente informe da cuenta del resultado de la modelación de dispersión de

contaminantes criterio, generados por las distintas actividades del Proyecto Macroloteo Los

Ángeles. Al respecto, es importante señalar, que analizado el estudio de emisiones

atmosféricas del Proyecto se determinó que las emisiones relevante se presentan en la etapa

de construcción, siendo en la etapa de operación mínimas, correspondiente solo a tránsito

de vehículos particulares, asociados a la ocupación de las viviendas, por lo que la modelación

se realiza solo para la etapa de construcción.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 6

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**2** **DESCRIPCIÓN GENERAL DEL PROYECTO**

El proyecto “Macro Loteo Los Ángeles”, cuya titularidad le pertenece a la empresa

Constructora José Miguel García y Cía. Ltda. consiste en la Modificación de un proyecto

inmobiliario de Lote X5-C con 222 viviendas incorporando el Lote X7, el cual consiste en la

construcción y habilitación de 612 viviendas, emplazado en una superficie total de

11,37 hectáreas aproximadamente. En la Figura 1, se presenta el área de ubicación del

Proyecto.

Figura 1 **.** Ubicación del Proyecto

Fuente: Elaboración propia.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 7

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**3** **MARCO NORMATIVO**

Según la ley de bases del medio ambiente, las normas de calidad primaria son instrumentos

de gestión ambiental que establecen los límites para proteger la salud de las personas. En

la Tabla 1 se puede verificar los valores establecidos en las normas chilenas de

contaminantes criterio y sus formas de verificación. En el presente informe, las

concentraciones modeladas se compararon con los valores entregados por la normativa, en

relación a los contaminantes aplicables al proyecto.

Tabla 1. Norma de calidad del aire para Material Particulado y gases.

|Contaminante|Valor|Periodo de<br>Evaluación|Forma de Verificación|Fuente<br>Normativa|
|---|---|---|---|---|
|Material<br>particulado<br>respirable<br>(MP10)|130 μg<br>/m3N|Promedio aritmético<br>de 24 hrs.|Percentil 98 de valores de un<br>año o más de 7 días en un año.|D.S. N° 12/2022<br>del<br>Ministerio<br>del<br>medio<br>Ambiente.|
|Material<br>particulado<br>respirable<br>(MP10)|50 μg /m~~3~~N|Promedio aritmético<br>anual|Promedio aritmético de 3 años<br>consecutivos.|Promedio aritmético de 3 años<br>consecutivos.|
|Material<br>particulado fino<br>(MP2.5)|50 μg /m~~3~~|~~Promedio aritmético~~<br>de 24 hrs.|~~Percentil 98 de valores de 1~~<br>año.|~~D.S. N° 12/2011~~<br>del<br>Ministerio<br>del<br>medio<br>Ambiente.|
|Material<br>particulado fino<br>(MP2.5)|20 μg /m~~3~~ <br>|Promedio aritmético<br>anual.|Promedio aritmético de 3 años<br>consecutivos.|Promedio aritmético de 3 años<br>consecutivos.|
|~~Dióxido de~~<br>azufre (SO2)|~~80 μg /m3N ~~|~~Media aritmética~~<br>anual|~~Promedio de tres años del~~<br>percentil 99 de las<br>concentraciones de 24 horas.|~~D.S.~~<br>No113/2002<br>del<br>MINSEGPRES|
|~~Dióxido de~~<br>azufre (SO2)|250 μg<br>/m3N|Media aritmética<br>diaria|~~Promedios de tres años del~~<br>percentil 99 de los máximos<br>diarios promedios de 8 horas.|~~Promedios de tres años del~~<br>percentil 99 de los máximos<br>diarios promedios de 8 horas.|
|Monóxido de<br>Carbono<br>(CO)|30 mg/<br>m3N|Media aritmética<br>horaria|Promedio de tres años del<br>percentil 99 de los máximos<br>diarios de 1 hora.|D.S.<br>No115/2002<br>del<br>MINSEGPRES|
|Monóxido de<br>Carbono<br>(CO)|10 mg/<br>m3N|Promedio móvil de 8<br>hrs.|Promedios de tres años del<br>percentil 99 de los máximos<br>diarios promedios de 8 horas.|Promedios de tres años del<br>percentil 99 de los máximos<br>diarios promedios de 8 horas.|
|~~Dióxido de~~<br>nitrógeno (NO2)|~~100 μg~~<br>/m3N|~~Media aritmética~~<br>anual|~~Promedio aritmético de 3 años~~<br>consecutivos.|~~D.S.~~<br>No114/2002<br>del<br>MINSEGPRES|
|~~Dióxido de~~<br>nitrógeno (NO2)|~~400 μg~~<br>/m3N|~~Concentración de 1~~<br>hora|~~Promedio de tres años del~~<br>percentil 99 de los máximos<br>diarios de 1 hora|~~Promedio de tres años del~~<br>percentil 99 de los máximos<br>diarios de 1 hora|

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 8

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**4** **METODOLOGÍA DE MODELACIÓN**

El sistema de modelación propuesto considera el protocolo, WRF/CALPUFF, los cuales han

sido adaptados a las condiciones del área de estudio.

Se aplicó el modelo meteorológico WRF ( _Weather Research and Forecasting_ ), para lo cual se

elaboraron escenarios de campos de vientos que sirven de base para el entendimiento de la

meteorología del área de estudio. Por otra parte, se realizó un procesamiento espacial de

inventarios de emisiones para ser utilizado en el modelo de dispersión de contaminantes.

CALPUFF es un modelo dinámico tipo _puff_, concordante con las recomendaciones

entregadas en la Guía para el Uso de Modelos de Calidad del Aire del SEIA [1] (en adelante,

Guía de Modelación del SEIA), que asume que de una sola fuente sale una bocanada ( _puff_ ),

la cual va sufriendo alteraciones a medida que se dispersa y transporta, a través de

mecanismos de advección, difusión, recirculación y transformaciones químicas.

La Figura 2 muestra el protocolo de modelación utilizado en el presente estudio.

Figura 2. Protocolo de Modelación

Fuente: Elaboración propia

**4.1** **Modelo Meteorológico**

La modelación meteorológica se realizó utilizando WRF ( _Weather Research and Forecasting_

_Model_, por sus siglas en inglés) en base a los criterios y recomendaciones establecidos por

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 9

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

la US EPA ( _Guidance on the Use of Models and Other Analyses for Demonstrating Attainment_

_of Air Quality Goals for Ozone, PM2.5, and Regional Haze, 2007_ ) y según se indica en la Guía

de Modelación del SEIA.

En términos esenciales, el modelo WRF consta de tres módulos principales, WPS, WRF-Var y

ARW-WRF, tal como se aprecia en el esquema presentado en la Figura 3.

Figura 3. Esquema general de funcionamiento de WRF-ARW

Fuente: Elaboración propia en base a información del Manual del Usuario de WRF

**4.2** **Características del Dominio de Modelación y su Entorno**

De acuerdo a los requerimientos metodológicos, el consultor recopiló, procesó y seleccionó

los datos de entrada, necesarios para alimentar el modelo meteorológico y de dispersión,

ajustando al formato correspondiente. A continuación, se presenta la data utilizada,

haciendo referencia de los criterios de selección empleados, y describiendo aquellos

elementos que tienen incidencia en los procesos de transporte y dispersión de

contaminantes.

**4.2.1** **Dominio de Modelación**

Para efecto de evaluar el impacto en la calidad del aire provocado por el proyecto, se ha

seleccionado un dominio de modelación en función de la disponibilidad de información

meteorológica y cercanía a receptores de interés. Posee una dimensión de 50 x 50 km, con

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 10

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

un tamaño de celda de 1 x 1 km. La Tabla 2 muestra las coordenadas de los vértices del

dominio de modelación.

Figura 4. Dominio de modelación WRF/CALPUFF

Fuente: Elaboración propia

Tabla 2. Coordenadas vértices del área de modelación del proyecto (Huso 18/19- WGS84)

|Identificación|Coordenada E (m)|Coordenada S (m)|
|---|---|---|
|NO|708368|5875119|
|NE|755728|5873819|
|SO|707162|5828117|
|~~SE~~|~~754408~~|~~5826807~~|

Fuente: Elaboración propia

**4.2.2** **Topografía y Uso de Suelo**

La topografía del dominio fue obtenida de las bases satelitales topográfica SRTM1 que

poseen una cobertura global con aproximadamente 90 m de resolución y las bases de uso

de suelo GLCC con 1 km de resolución. La representación en tres dimensiones en la Figura

5 da cuenta del área de estudio, en general con bajo relieve, asociada al área se aprecia la

ciudad de Los Ángeles en el centro del dominio y las principales zonas.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 11

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 5. Topografía del área de modelación 3D

Fuente: Elaboración propia

**5** **CARACTERIZACIÓN METEOROLÓGICA**

**5.1** **Información Meteorológica**

La información meteorológica utilizada proviene de estaciones de superficie cercanas al área

del proyecto y en altura de una estación de radio sondeo. A continuación, en la Tabla 3 y

Tabla 4, se detallan las fuentes de información y sus características, para datos de calidad

del aire y variables meteorológicas de superficie y altura, respectivamente, para el año base

2022.

Tabla 3. Estaciones meteorológicas y calidad del aire para datos en superficie cercanas al proyecto

|Nombre Estación|Coordenadas UTM (18<br>H)|Col3|Calidad del<br>Aire|Col5|Variables<br>meteorológicas|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|Nombre Estación|~~UTM-E~~|~~UTM-S~~|~~MP2,5~~|~~MP10~~|~~RG~~|~~HR~~|~~TA~~|~~DV~~|~~VV~~|~~PP*~~|
|~~21 Mayo (MMA)~~|~~ 733331~~|~~5849585~~|~~x ~~|~~x ~~|~~x ~~|~~x ~~|~~x ~~|~~x ~~|~~x ~~||
|~~Human (AGROMET)~~||||||||||~~x ~~|

RG: Radiación global; HR: humedad relativa; TA: Temperatura ambiente; DV: dirección del viento; VV: velocidad del viento; PP:
Precipitación Acumulada

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 12

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Tabla 4. Ubicación Estación de Radiosondeo para datos de altura

|Nombre Estación|Coordenadas UTM (19 H)|Col3|
|---|---|---|
|Nombre Estación|~~UTM-E~~|~~UTM-N~~|
|~~Santo Domingo ~~|~~257969~~|~~6273039~~|

Fuente: Elaboración propia

La Figura 6 presenta la ubicación de las estaciones de monitoreo utilizadas para la

caracterización meteorológica del área de estudio. La principal corresponde a la Estación 21

de Mayo del MMA, sin embargo, ésta no presenta registro de precipitaciones, por lo que se

utilizaron los datos de este parámetro registrados en la Estación Human, de Agromet.

Figura 6. Ubicación Estaciones de Monitoreo

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 13

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**5.2** **Rosas de Los Vientos**

De los datos meteorológicos utilizados por el modelo, los más relevantes son la velocidad y

dirección del viento preponderante de la zona. A continuación, en los gráficos siguientes se

presenta la rosa de los vientos en un análisis estacional (verano, otoño, invierno, primavera),

Los datos analizados corresponden a los registrados por la Estación 21 de Mayo, de la

comuna de Los Ángeles, para el año 2022, perteneciente a la red de monitoreo

meteorológico y de calidad del aire del Ministerio de Medio Ambiente (SINCA), la cual

corresponde a la estación más cercana a la fuente, que presenta registro de datos horarios.

Por otra parte, es importante mencionar que para la elaboración de las rosas de los vientos

se empleó la opción de “ _blowing from_ ”, es decir que el vector sopla desde el origen hacia la

estación.

**A** **B**

**C** **D**

Figura 7. Rosas de los vientos estacionales (A: verano, B: otoño, C: Invierno, D: Primavera)

Fuente: Elaboración propia a partir de la data de estación 21 de Mayo

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 14

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

De las rosas de los vientos estacionales se puede observar cierta variabilidad entre las

estaciones cálidas (primavera-verano) y las frías (otoño-invierno). Las rosas muestran

predominancia de los vientos que soplan desde suroeste en la estación de verano y

primavera. En cambio, para las estaciones de otoño e invierno el viento presenta su origen

en suroeste, pero también noreste, mostrando mayor distribución tanto en la dirección,

como en las velocidades.

Respecto a la velocidad del viento registrada en la estación, se observa que en todas las

estaciones del año predominan los vientos en el rango de 0,5 a 3,6 m/s y distribuidos de

forma uniforme en ambos periodos para épocas frías y cálidas, existiendo las mayores

intensidades en época de invierno periodo en conjunto con otoño, que ostenta las mayores

cantidades de calmas.

**5.2.1** **Series de Tiempo y ciclos diarios**

A continuación, se presentan los gráficos de series de tiempo y ciclos diarios de las variables

meteorológicas temperatura, humedad relativa, radiación global, precipitaciones, velocidad

y dirección del viento en términos de valores horarios, para el año 2022.

De la serie de tiempo de temperatura, se observa una marcada estacionalidad, apreciándose

los valores mínimos entre los meses de abril a septiembre, encontrándose que los valores

horarios fluctúan entre -3 y 28°C en este periodo. Las máximas, por otro lado, se presentan

a partir de octubre hasta marzo, teniendo sus mayores registros entre enero y febrero, con

valores sobre los 30°C y máximas cercanas a los 38°C.

En relación a la humedad relativa es posible observar variabilidad estacionalidad,

encontrándose los niveles de humedad más altos en torno a los meses de junio y agosto,

coincidiendo con los meses que registran los menores niveles de radiación global.

Respecto a las precipitaciones, es posible observarlas con mayor frecuencias entre los meses

de mayo a agosto, encontrándose la mayoría de los valores horarios, con precipitaciones

menores a 10 mm de agua caída, durante el periodo evaluado.

Para la variable velocidad del viento, se puede apreciar que para el año 2022 los valores

máximos horarios se registran en meses de invierno llegando a _peaks_ cercanos a 9 m/s. En

general, los valores observados dan cuenta de que los vientos en el área de estudio

presentan alta variación a lo largo de las estaciones frías.

En general, en análisis de las variables meteorológicas que caracterizan el área de estudio

indican una marcada estacionalidad, apreciándose diferencias a través de los meses, lo que

es característico de zonas ubicadas en el sur del país.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 15

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 8. Series de tiempo horaria de variables meteorológicas año 2022

Fuente: Elaboración propia a partir de la data de estación 21 de Mayo (T, HR, RG, VV) y Human (PP).

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 16

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Del ciclo diario de temperatura, se observa un perfil que representa 3 fases marcadas con

valores mínimos hasta las 6 am, a partir de donde comienza a aumentar la temperatura

desde las 8 am hasta las 14 pm, en donde se presentan los valores máximos hasta las 16 pm,

luego de lo cual comienza el descenso hasta la madrugada. La amplitud del intervalo en las

horas de mayor temperatura, dan cuenta de su variabilidad estacional. Respecto a la

velocidad del viento los valores dan cuenta de dos periodos diurno/nocturno con variaciones

de +/- 1 m/s entre las 7 am y 17 pm. Por otra parte, y tal como se pudo observar en las rosas

de los vientos, existe una frecuencia importante de vientos entre los 180° y 200° (suroeste).

|11%|10%|10%|11%|8%|10%|13%|13%|14%|17%|20%|20%|18%|17%|13%|12%|11%|11%|11%|17%|17%|14%|13%|11%|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~0%~~<br>|~~1%~~<br>|~~1%~~<br>|~~3%~~<br>|~~5%~~<br>|~~6%~~<br>|~~6%~~<br>|~~10%~~<br>|~~10%~~<br>|~~10%~~<br>|~~9%~~<br>|~~8%~~<br>|~~8%~~<br>|~~9%~~<br>|~~5%~~<br>|~~2%~~<br>|~~1%~~<br>|~~2%~~<br>|~~1%~~<br>|
|~~0%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~2%~~<br>|~~1%~~<br>|~~1%~~<br>|~~2%~~<br>|~~4%~~<br>|~~4%~~<br>|~~4%~~<br>|~~6%~~<br>|~~8%~~<br>|~~10%~~<br>|~~7%~~<br>|~~8%~~<br>|~~6%~~<br>|~~2%~~<br>|~~2%~~<br>|~~2%~~<br>|~~1%~~<br>|~~1%~~<br>|
|~~0%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~2%~~<br>|~~3%~~<br>|~~1%~~<br>|~~2%~~<br>|~~4%~~<br>|~~4%~~<br>|~~4%~~<br>|~~4%~~<br>|~~3%~~<br>|~~4%~~<br>|~~4%~~<br>|~~3%~~<br>|~~2%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~0%~~<br>|
|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~0%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~2%~~<br>|~~1%~~<br>|~~2%~~<br>|~~2%~~<br>|~~3%~~<br>|~~4%~~<br>|~~5%~~<br>|~~4%~~<br>|~~5%~~<br>|~~5%~~<br>|~~3%~~<br>|~~2%~~<br>|~~3%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|
|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~2%~~<br>|~~1%~~<br>|~~3%~~<br>|~~2%~~<br>|~~2%~~<br>|~~3%~~<br>|~~5%~~<br>|~~4%~~<br>|~~4%~~<br>|~~4%~~<br>|~~3%~~<br>|~~2%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|
|~~2%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~2%~~<br>|~~2%~~<br>|~~2%~~<br>|~~2%~~<br>|~~3%~~<br>|~~4%~~<br>|~~6%~~<br>|~~4%~~<br>|~~2%~~<br>|~~5%~~<br>|~~5%~~<br>|~~6%~~<br>|~~4%~~<br>|~~4%~~<br>|~~2%~~<br>|~~1%~~<br>|~~1%~~<br>|~~2%~~<br>|~~2%~~<br>|
|~~26%~~<br>|~~24%~~<br>|~~ 24%~~<br>|~~ 20%~~<br>|~~19%~~<br>|~~20%~~<br>|~~ 23%~~<br>|~~27%~~<br>|~~ 33%~~<br>|~~38%~~<br>|~~40%~~<br>|~~34%~~<br>|~~35%~~<br>|~~36%~~<br>|~~34%~~<br>|~~35%~~<br>|~~36%~~<br>|~~32%~~<br>|~~ 29%~~<br>|~~31%~~<br>|~~36%~~<br>|~~ 35%~~<br>|~~ 35%~~<br>|~~ 28%~~<br>|
|~~23%~~<br>|~~ 25%~~<br>|~~ 23%~~<br>|~~9%~~<br>|~~ 25%~~<br>|~~ 25%~~<br>|~~ 26%~~<br>|~~21%~~<br>|~~19%~~<br>|~~12%~~<br>|~~6%~~<br>|~~7%~~<br>|~~5%~~<br>|~~6%~~<br>|~~5%~~<br>|~~6%~~<br>|~~7%~~<br>|~~13%~~<br>|~~16%~~<br>|~~15%~~<br>|~~14%~~<br>|~~16%~~<br>|~~16%~~<br>|~~ 20%~~<br>|
|~~3%~~<br>|~~4%~~<br>|~~7%~~<br>|~~8%~~<br>|~~9%~~<br>|~~6%~~<br>|~~4%~~<br>|~~4%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~2%~~<br>|~~3%~~<br>|~~4%~~<br>|~~3%~~<br>|~~3%~~<br>|~~3%~~<br>|~~5%~~<br>|
|~~2%~~<br>|~~2%~~<br>|~~3%~~<br>|~~3%~~<br>|~~2%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~0%~~<br>|~~0%~~<br>|~~0%~~<br>|~~0%~~<br>|~~1%~~<br>|~~0%~~<br>|~~0%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~0%~~<br>|~~1%~~<br>|~~2%~~<br>|~~0%~~<br>|~~1%~~<br>|
|~~2%~~<br>|~~1%~~<br>|~~2%~~<br>|~~1%~~<br>|~~2%~~<br>|~~2%~~<br>|~~2%~~<br>|~~1%~~<br>|~~0%~~<br>|~~0%~~<br>|~~0%~~<br>|~~0%~~<br>|~~0%~~<br>|~~0%~~<br>|~~0%~~<br>|~~1%~~<br>|~~0%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~0%~~<br>|~~1%~~<br>|~~2%~~<br>|~~1%~~<br>|
|~~1%~~<br>|~~1%~~<br>|~~0%~~<br>|~~1%~~<br>|~~2%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~0%~~<br>|~~0%~~<br>|~~1%~~<br>|~~0%~~<br>|~~1%~~<br>|~~0%~~<br>|~~0%~~<br>|~~0%~~<br>|~~0%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|
|~~3%~~<br>|~~1%~~<br>|~~2%~~<br>|~~2%~~<br>|~~2%~~<br>|~~3%~~<br>|~~2%~~<br>|~~2%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~0%~~<br>|~~0%~~<br>|~~0%~~<br>|~~0%~~<br>|~~1%~~<br>|~~0%~~<br>|~~1%~~<br>|~~1%~~<br>|~~2%~~<br>|~~1%~~<br>|~~2%~~<br>|~~2%~~<br>|
|~~3%~~<br>|~~3%~~<br>|~~2%~~<br>|~~5%~~<br>|~~5%~~<br>|~~4%~~<br>|~~2%~~<br>|~~3%~~<br>|~~2%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~0%~~<br>|~~0%~~<br>|~~1%~~<br>|~~1%~~<br>|~~0%~~<br>|~~1%~~<br>|~~1%~~<br>|~~2%~~<br>|~~1%~~<br>|~~3%~~<br>|~~4%~~<br>|~~4%~~<br>|
|~~6%~~<br>|~~7%~~<br>|~~6%~~<br>|~~6%~~<br>|~~7%~~<br>|~~7%~~<br>|~~4%~~<br>|~~4%~~<br>|~~4%~~<br>|~~3%~~<br>|~~1%~~<br>|~~1%~~<br>|~~1%~~<br>|~~2%~~<br>|~~1%~~<br>|~~1%~~<br>|~~3%~~<br>|~~2%~~<br>|~~4%~~<br>|~~2%~~<br>|~~4%~~<br>|~~4%~~<br>|~~5%~~<br>|~~6%~~<br>|
|~~15%~~<br>|~~15%~~<br>|~~17%~~<br>|~~13%~~<br>|~~13%~~<br>|~~13%~~<br>|~~13%~~<br>|~~12%~~<br>|~~13%~~<br>|~~10%~~<br>|~~9%~~<br>|~~8%~~<br>|~~7%~~<br>|~~7%~~<br>|~~8%~~<br>|~~8%~~<br>|~~7%~~<br>|~~8%~~<br>|~~8%~~<br>|~~10%~~<br>|~~11%~~<br>|~~14%~~<br>|~~14%~~<br>|~~14%~~<br>|
|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|~~0%~~|

Figura 9. Ciclos diarios de variables meteorológicas año 2022
Fuente: Elaboración propia en base a datos meteorológicos año 2022, Estación 21 de Mayo Los Ángeles

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 17

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**5.2.2** **Ciclos Estacionales**

A continuación, se presenta la variación estacional de los ciclos diarios de las variables

temperatura, velocidad y dirección del viento.

La variación estacional del ciclo diario de la temperatura muestra una marcada variación

mensual y horaria. Encontrándose las mayores temperaturas entre los meses de noviembre

a marzo, entre las 13:00 y las 18:00 horas.

Hora local

Figura 10. Variación estacional del ciclo diario de la Temperatura
Fuente: Elaboración propia en base a datos meteorológicos año 2022, Estación 21 de Mayo Los Ángeles

El gráfico de la variación estacional del ciclo diario de la velocidad del viento, presentado en

la Figura 11, demuestra la diferencia tanto mensual como a lo largo del día, en el área de

estudio. Encontrándose durante el periodo nocturno menores velocidades que durante el

día, con los valores máximos entre las 15:00 y las 19:00 en los meses entre enero a marzo.

Mientras que durante los meses fríos (abril a agosto) se encuentran velocidades menores, lo

que propicia condiciones para generar episodios de contaminación, asociado a la mala

ventilación del ambiente.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 18

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Hora local

Figura 11. Variación estacional del ciclo diario de la velocidad del viento

Fuente: Elaboración propia en base a datos meteorológicos año 2022, Estación 21 de Mayo Los Ángeles

En lo que respecta a la variación de la dirección del viento, se aprecia marcadamente una

tendencia a presentarse vientos durante el horario diurno, sobre todo en los meses cálidos

de septiembre hasta abril, con origen desde el suroeste (180 a 270°), mientras que, durante

el periodo nocturno y madrugada, se aprecian direcciones más tendientes al sureste (90 a

180 °) durante todo el año.

Hora local

Figura 12. Variación estacional del ciclo diario de la dirección del viento
Fuente: Elaboración propia en base a datos meteorológicos año 2022, Estación 21 de Mayo Los Ángeles

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 19

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**5.2.3** **Ciclos estacionales de datos en altura**

A continuación, se presenta el ciclo estacional del perfil vertical de las variables temperatura

y velocidad del viento.

La variación estacional de los datos de altura de la variable temperatura, presentada en la

Figura 13, da cuenta de una tendencia homogénea, a lo largo de cada nivel de altura, durante

el año, alcanzándose en general, los 15°C hasta los 2000 m de altura. Mientras que los 0° se

alcanzan a la altura cercana a los 5000 m.

Figura 13. Variación estacional del perfil vertical de temperatura
Fuente: Elaboración propia en base a datos meteorológicos año 2022 radiosonda Santo Domingo

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 20

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

La variación estacional de los datos de altura de la velocidad de viento, presentada en la

Figura 14, da cuenta de una variación en los distintos meses en estudio. En general, hasta

los 4.000 m de altura, las velocidades del viento se consideran con poca variación entre los

distintos meses de monitoreo. Mientras que, sobre los 7.000 m de altura, la velocidad del

viento varía, de acuerdo al periodo del año en que se mida. De esta manera, entre diciembre

y marzo, se aprecian menores velocidades que entre los meses de abril y noviembre,

alcanzándose velocidades tan altas como 50 m/s, durante los meses de junio a agosto, en

altura sobre los 10.000 m.

Figura 14. Variación estacional del perfil vertical de velocidad de viento
Fuente: Elaboración propia en base a datos meteorológicos año 2022radiosonda Santo Domingo

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 21

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**6** **CARACTERIZACIÓN DE CALIDAD DEL AIRE**

Para la caracterización de la calidad del aire se consideró la información entregada por la

estación de monitoreo “21 de Mayo”, de propiedad del Ministerio del Medio Ambiente, la

cual corresponde a la estación con datos validados, más cercana a la ubicación del proyecto.

Para la caracterización se emplearon los datos de concentración de material particulado

MP2,5 y MP10.

**Material Particulado MP2,5**

El D.S. N°12/11 [2], establece que la norma primaria de calidad del aire para el contaminante

Material Particulado Fino MP2,5, es 50 μg/m [3] N como concentración de 24 horas,

considerándose sobrepasada cuando el percentil 98 de las concentraciones de 24 horas

registradas durante un período anual en cualquier estación monitora calificada EMRP, sea

mayor a 50 μg/m [3] .

Asimismo, la norma establece el límite de 20 μg/m [3] N, como concentración anual,

considerándose sobrepasada cuando el promedio trianual [1] de las concentraciones anuales

sea mayor a 20 μg/m [3], en cualquier estación monitora calificada como EMRP.

La información respecto a la evaluación de la norma de calidad primaria de MP2,5, para la

ciudad de Los Ángeles, de acuerdo a los datos registrados en la estación de monitoreo 21

de Mayo se presenta en la Tabla 5.

Tabla 5. Parámetros de cumplimiento de norma de MP2,5 años 2020-2022

|Parámetro|2020|2021|2022|
|---|---|---|---|
|Norma anual|Norma anual|Norma anual|Norma anual|
|Promedio Anual (μg/m3 N)|27|27|25|
|No datos validados|349|357|360|
|% datos validados|96%|98%|99%|
|Promedio Trianual (μg/m3 N)|26|26|26|
|Norma|20|20|20|
|% norma|131%|131%|131%|
|Norma diaria|Norma diaria|Norma diaria|Norma diaria|
|Percentil 98|122|137|126|
|Norma|50|50|50|
|% norma<br>|244%<br>|274%<br>|252%<br>|

[Fuente: Elaboración propia en base a la data de calidad del aire de la estación 21 de Mayo, www.sinca.cl](http://www.sinca.cl/)

1 Promedio trianual corresponde al promedio aritmético de tres años calendario consecutivos de la concentración anual, en
cualquier estación monitora.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 22

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Los resultados dan cuenta de que la norma diaria, se encuentra sobrepasada para los 3 años

evaluados.

En relación a la evaluación de la norma anual, se puede observar que el límite se encuentra

sobrepasado, por cuanto el promedio trianual se encuentra 131% respecto a la norma.

Figura 15. Evaluación de Norma Anual y Diaria para MP2,5
Fuente: Elaboración propia en base a datos Estación 21 de Mayo Los Ángeles

La serie de tiempo de las concentraciones diarias de MP2,5 para los años 2017 a 2019,

presentada en la Figura 16, da cuenta de que existe una marcada estacionalidad asociada a

las concentraciones de este contaminante, lo que cuenta de que la principal fuente

corresponde a la combustión residencial de leña, por observar los mayores niveles de

concentración durante los meses fríos del año, entre abril y agosto de cada año.

Figura 16. Serie de tiempo MP2,5 año 2020-2022
Fuente: Elaboración propia en base a datos Estación 21 de Mayo Los Ángeles

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 23

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

El ciclo diario de las concentraciones de MP2,5, presentado en la Figura 17, permite observar

la marcada variación durante las horas del día, apreciándose los mayores valores de

concentración máximos entre las 20:00 y las 23:00 horas, encontrándose el máximo

promedio en 32,4 μg/m [3] a las 01:00 horas.

Figura 17. Ciclo diario de concentraciones de MP2,5 año 2022
Fuente: Elaboración propia en base a datos Estación 21 de Mayo Los Ángeles

**Material Particulado MP10**

El D.S. N° 11/22 del MMA, que establece que la norma primaria de calidad del aire para el

contaminante Material Particulado Respirable MP10 y deroga el D.S. N°59/1998 del

MINSEGPRES, establece que una norma de 130 μg/m [3] N como concentración de 24 horas.

Se considerará sobrepasada la norma de calidad del aire para Material Particulado Respirable
cuando el percentil 98 de las concentraciones de 24 horas registradas durante un período
anual en cualquier estación monitora calificada como estación de monitoreo de Material
Particulado Respirable MP10 con representatividad poblacional, EMRP, sea mayor o igual a
130 μ g/m [3] N.

Asimismo, se considerará superada la norma, si antes que concluyese el primer período
anual de mediciones de las estaciones monitoras de Material Particulado Respirable MP10
calificadas como EMRP, se registrase un número de días con mediciones sobre el valor de
130 μg/m [3] N mayor que siete (7).

La información respecto a la evaluación de la norma de calidad primaria de MP10 para la

ciudad de Los Ángeles, de acuerdo a los datos registrados en la estación de monitoreo 21

de Mayo, se presenta en la Tabla 6.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 24

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Tabla 6. Parámetros de cumplimiento de norma de MP10 años 2020-2022

|Parámetro|2020|2021|2022|
|---|---|---|---|
|Norma anual|Norma anual|Norma anual|Norma anual|
|Promedio Anual (μg/m3 N)|43|42|38|
|No datos validados|356|360|360|
|% datos validados|98%|98%|99%|
|Promedio Trianual (μg/m3 N)*|41|41|41|
|Norma|50|50|50|
|% norma|82%|82%|82%|
|Norma diaria|Norma diaria|Norma diaria|Norma diaria|
|Percentil 98|133|149|135|
|Norma|150|150|130|
|% norma<br>|89%<br>|99%<br>|104%<br>|

[Fuente: Elaboración propia en base a la data de calidad del aire de la estación 21 de Mayo, www.sinca.cl](http://www.sinca.cl/)

Los resultados dan cuenta de que la norma diaria, se encuentra cumpliendo los niveles

establecidos para los 3 años en estudio, encontrándose bajo el 50% de la norma. En tanto

la norma anual se encuentra en estado de latencia, debido a que se encuentra en un 100%

respecto al límite.

Figura 18. Evaluación de Norma Anual y Diaria para MP10
[Fuente: Elaboración propia en base a la data de calidad del aire de la estación 21 de Mayo, www.sinca.cl](http://www.sinca.cl/)

La serie de tiempo de las concentraciones diarias de MP10 para los años 2017 a 2019,

presentada en la Figura 19 da cuenta de que existe una marcada estacionalidad asociada a

las concentraciones de este contaminante, dado que la principal fuente corresponde a la

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 25

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

combustión residencial de leña, por observar los mayores niveles de concentración durante

los meses fríos del año, entre abril y agosto de cada año.

Figura 19. Serie de tiempo MP10 año 2020-2022
Fuente: Elaboración propia en base a datos Estación 21 de Mayo Los Ángeles

El ciclo diario de las concentraciones de MP10, presentado en la Figura 20, permite observar

la marcada variación durante las horas del día, apreciándose los mayores valores de

concentración entre las 20:00 y las 24:00 horas, encontrándose el máximo promedio en 45,8

μg/m [3] a las 20:00 horas.

Figura 20. Ciclo diario de concentraciones de MP10 año 2019

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 26

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**7** **CARACTERIZACIÓN DE LA FUENTE Y SUS EMISIONES**

**7.1** **Identificación de las fuentes emisoras**

Tabla 7. Fuentes de emisiones atmosféricas, durante etapa de construcción del Proyecto.

|Tipo de<br>Emisión|Actividad|Tipo de<br>Contaminante|
|---|---|---|
|Emisiones<br>directas|~~Escarpe~~|~~MP 10, MP 2.5~~|
|Emisiones<br>directas|~~Excavaciones~~|~~MP 10, MP 2.5~~|
|Emisiones<br>directas|~~Carguío de camiones y transferencia de material~~|~~MP 10, MP 2.5~~|
|Emisiones<br>directas|~~Erosión de material en pila~~|~~MP 10, MP 2.5~~|
|Emisiones<br>directas|~~Tránsito por caminos no pavimentados al interior del sitio~~<br>donde se emplaza el Proyecto (vehículos pesados)|MP 10, MP 2.5|
|Emisiones<br>directas|~~Emisiones de gases de combustión de maquinaria y~~<br>vehículos.|~~MP 10, MP 2.5 y~~<br>gases de combustión|
|Emisiones<br>indirectas|~~Tránsito por caminos no pavimentados fuera del sitio~~<br>donde se emplaza el Proyecto (vehículos pesados y<br>livianos)|MP 10, MP 2.5 y<br>gases de combustión|

Fuente: Elaboración propia en base a Estudio de Estimación de Emisiones Atmosféricas.

Las emisiones de material particulado y gases de combustión para la fase de operación están

dadas solo por el tránsito de vehículos livianos de propiedad de los residentes, cuyas

emisiones son presentadas en el Anexo “Estimación de Emisiones Atmosféricas Proyecto

Macroloteo Los Ángeles”, considerándose mínimas.

**7.2** **Perfil Temporal**

El perfil temporal correspondiente a la fase de construcción fue determinado de acuerdo

con la información entregada por el Titular, definiéndose un funcionamiento con 8 horas de

trabajos, según se presenta en la Tabla 8. Respecto a las emisiones mensuales, éstas se basan

directamente en el cronograma presente en el anexo “Estimación de Emisiones Atmosféricas

Proyecto Macroloteo Los Ángeles”.

Tabla 8. Días de funcionamiento de la fuente

|Horario|SEMANA|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|<br>**Horario**|~~Lun~~|~~Mar.~~|~~Mie.~~|~~Jue.~~|~~Vie.~~|~~Sab.~~|~~Dom.~~|
|~~8-9~~||||||||
|~~9-10~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|||
|~~10-11~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|||
|~~11-12~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|||
|~~12-13~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|||
|~~13-14~~||||||||
|~~14-15~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|||
|~~15-16~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|||
|~~16-17~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|||
|~~17-18~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|~~X ~~|||

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 27

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**8** **RESULTADOS DE LA MODELACIÓN**

**8.1** **Validación Meteorológica**

Las siguientes figuras presentan los resultados para la comparación de variables observadas

y modeladas, respecto a temperatura y velocidad del viento.

Figura 21. Temperatura observada v/s modelada serie anual

Fuente: Elaboración propia

y = 0,5353x + 6,3794

~~0~~

|35 T Mod vs T|R2 = 0,834 T Real|
|---|---|
|30<br>||
|25<br>||
|20<br>||
|15<br>||
|10<br>||
|5<br>||
|~~0~~<br>||

-10 -5 0 5 10 15 20 25 30 35 40

Figura 22. Correlación temperatura observada v/s modelada serie anual

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 28

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 23. velocidad del viento modelada v/s modelada serie anual

Fuente: Elaboración propia

Figura 24. Correlación Velocidad del viento observada v/s modelada serie anual

Fuente: Elaboración propia

Figura 25. Precipitaciones modelada v/s modelada serie anual

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 29

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

De acuerdo a lo observado en las figuras para la velocidad del viento, es posible apreciar

que la correlación llega a 0,8. Las mejores correlaciones para temperaturas se registran en

verano y primavera. Para ambas variables es posible evidenciar un comportamiento similar

entre el observado y modelado habiendo un problema del modelo para captar los máximos

de temperatura. La elevada correlación y captura de máximos y mínimos para velocidad del

viento da cuenta de que la información meteorológica es adecuada para capturar las

condiciones de dispersión que imperan en la zona de estudio.

La Tabla 9 presenta los resultados del análisis cuantitativo para las métricas estadísticas del

sesgo (error medio o BIAS), error absoluto medio (MAE) y la raíz del error cuadrático medio

(RMSE), comparándolo con los valores de referencia.

Se observa un adecuado desempeño del modelo meteorológico en relación al análisis

estadístico presentado.

Tabla 9. Estadísticos de Desempeño del Modelo Meteorológico

|Estadístico|Velocidad Viento|Col3|Temperatura|Col5|
|---|---|---|---|---|
|Estadístico|Referencia|Valor obtenido|Referencia|Valor obtenido|
|BIAS|-2,5; 2,5 (m/s)|2,3|-4,4 (°C)|-0,1|
|MAE|≤3|2,4|≤4|2,9|
|RMSE|≤3,5|2,9|≤4,5|3,7|
|Coeficiente correlación (r)|>0,6|0,51|>0,8|0,83|

Fuente: Elaboración propia

**8.2** **Resultados de la Modelación Meteorológica**

A continuación, se presentan los resultados obtenidos con el modelo WRF aplicado para el

año base 2022, considerando 365 días de procesamiento. Las siguientes figuras representan

los campos de viento estacionales y horarios entregados por la simulación. Es posible

observar que el modelo estima de manera adecuada el comportamiento de las variables

meteorológicas ejemplificadas en los campos de viento, puesto que se mantiene la

tendencia observada en las rosas de los vientos y los gráficos de variación estacional de los

ciclos diarios. De manera general, es posible apreciar que las condiciones de estabilidad se

ven favorecidas principalmente en el periodo de invierno, generando peores condiciones de

ventilación, lo que incide en la generación de episodios de contaminación como queda de

manifiesto en el análisis de calidad del aire. En contraposición, los meses más cálidos

presentan condiciones que favorecen la dispersión de contaminantes.

Los campos de vientos permiten determinar posteriormente la dispersión de los

contaminantes, por medio de la aplicación del modelo CALPUFF.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 30

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 26. Campos de viento estación: Verano-periodo nocturno

Fuente: Elaboración propia

Figura 27. Campos de viento estación: Verano-periodo diurno

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 31

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 28. Campos de viento estación: Otoño-periodo nocturno

Fuente: Elaboración propia

Figura 29. Campos de viento estación: Otoño-periodo diurno

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 32

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 30. Campos de viento estación: Invierno-periodo nocturno

Fuente: Elaboración propia

Figura 31. Campos de viento estación: Invierno-periodo diurno

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 33

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 32. Campos de viento estación: Primavera-periodo nocturno

Fuente: Elaboración propia

Figura 33. Campos de viento estación: Primavera-periodo diurno

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 34

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**8.3** **Resultados de la Modelación de Dispersión de Contaminantes**

**8.3.1** **Determinación de concentración en el punto de Máximo Impacto Etapa según**

**etapa.**

En respuesta al objetivo del estudio, a continuación, se presentan los valores modelados

para los contaminantes con mayor relevancia para el área de estudio, determinado en el

punto de máximo impacto, contrastando respecto a los límites de las Normas Primarias de

Calidad del Aire. Se presentan los resultados para MP10 y MP2,5 como percentil 98 de las

concentraciones anuales del promedio de 24 horas, y como promedio anual.

Tabla 10. Resultados de la modelación de calidad del aire (máximo impacto).

|Periodo|Contaminante|Construcción|Col4|
|---|---|---|---|
|Periodo|Contaminante|Máx. (μg/m3)|% r/Norma|
|Diario|MP10|0,503|0,39%|
|Diario|MP2,5|0,103|0,21%|
|Anual<br>|MP10|0,207|0,41%|
|Anual<br>|MP2,5<br>|0,043|0,22%|

Fuente: Elaboración propia

**8.3.2** **Mapas de Isoconcentraciones Construcción**

En los gráficos siguientes, se muestran las concentraciones de contaminante modelados

según las normativas de referencia. En ellas se observa cómo se dispersa la pluma

contaminante desde su fuente generadora (principalmente Resuspensión de MP en sus

fracciones normadas), hasta llegar a sectores colindantes, donde, es posible apreciar un bajo

impacto al contrastar con la normativa nacional para cada contaminante y/o con los índices

considerados inseguros para la salud de la población. También se observa que el impacto

de la fuente solo está presente en la zona inmediatamente adyacente a la zona de

construcción y transporte de materiales, sin evidenciarse concentraciones relevantes en las

rutas modeladas (bajo 1 g/m [3] para MP10) A continuación, se presentan los mapas de

Isoconcentraciones que dan cuenta las concentraciones del proyecto y permite

contextualizar el impacto de las fuentes en función de los distintos contaminantes

normados.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 35

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

|CALPUFF View - Lakes Environmental Software|Col2|
|---|---|
|<br>CALPUFF View - Lakes Environmental Software|Titular<br>|
|<br>CALPUFF View - Lakes Environmental Software|Modeler<br>|
|<br>CALPUFF View - Lakes Environmental Software|Scale: 1:55.000<br>|
|<br>CALPUFF View - Lakes Environmental Software|Proyect N°:<br>382-IEP23|

Figura 34. Modelación de Dispersión de MP10 P98 promedio 24 hrs. Fase Construcción.

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 36

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

|CALPUFF View - Lakes Environmental Software|Col2|
|---|---|
|<br>CALPUFF View - Lakes Environmental Software|Titular<br>|
|<br>CALPUFF View - Lakes Environmental Software|Modeler<br>|
|<br>CALPUFF View - Lakes Environmental Software|Scale: 1:55.000<br>|
|<br>CALPUFF View - Lakes Environmental Software|Proyect N°:<br>382-IEP23|

Figura 35. Modelación de Dispersión de MP2.5 P98 promedio 24 hrs. Fase Construcción.

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 37

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

|CALPUFF View - Lakes Environmental Software|Col2|
|---|---|
|<br>CALPUFF View - Lakes Environmental Software|Titular<br>|
|<br>CALPUFF View - Lakes Environmental Software|Modeler<br>|
|<br>CALPUFF View - Lakes Environmental Software|Scale: 1:55.000<br>|
|<br>CALPUFF View - Lakes Environmental Software|Proyect N°:<br>382-IEP23|

Figura 36. Modelación de Dispersión de CO promedio 1 hora Fase Construcción.

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 38

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

|CALPUFF View - Lakes Environmental Software|Col2|
|---|---|
|<br>CALPUFF View - Lakes Environmental Software <br>|Titular<br>|
|<br>CALPUFF View - Lakes Environmental Software <br>|Modeler<br>|
|<br>CALPUFF View - Lakes Environmental Software <br>|Scale: 1:55.000<br>|
|<br>CALPUFF View - Lakes Environmental Software <br>|Proyect N°:<br>382-IEP23<br>|

Figura 37. Modelación de Dispersión de SO 2 P99 promedio 24 hora Fase Construcción

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 39

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

|CALPUFF View - Lakes Environmental Software|Col2|
|---|---|
|<br>CALPUFF View - Lakes Environmental Software <br><br>|Titular<br>|
|<br>CALPUFF View - Lakes Environmental Software <br><br>|Modeler<br>|
|<br>CALPUFF View - Lakes Environmental Software <br><br>|Scale: 1:55.000<br>|
|<br>CALPUFF View - Lakes Environmental Software <br><br>|Proyect N°:<br>382-IEP23<br>|

Figura 38. Modelación de Dispersión de NOx máximo horario Fase Construcción.

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 40

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**8.3.3** **Determinación de receptores y concentración de inmisión**

Considerando todo el dominio de modelación, se determinaron los receptores que pudieran

determinar una zona de impacto del proyecto en función de su exposición. Así se definieron

7 ubicaciones donde existen viviendas y/o lugares de alojamiento que representan los

principales centros poblados aledaños al proyecto.

|CALPUFF View - Lakes Environmental Software|Col2|
|---|---|
|<br>CALPUFF View - Lakes Environmental Software <br>|Titular<br>|
|<br>CALPUFF View - Lakes Environmental Software <br>|Modeler<br>|
|<br>CALPUFF View - Lakes Environmental Software <br>|Scale: 1:30.000<br>|
|<br>CALPUFF View - Lakes Environmental Software <br>|Proyect N°:<br>382-IEP23|

Figura 39. Receptores evaluados en el proyecto

Fuente: Elaboración propia

Tabla 11. Identificación de los receptores discretos

|Receptor|Col2|Col3|Col4|
|---|---|---|---|
|~~ID~~|~~Tipo~~|~~Coordenada UTM E~~|~~Coordenada UTM S~~|
|R1|Viviendas|731262|5850375|
|R2|Viviendas|731451|5850590|
|~~R3~~|~~Viviendas~~|~~731570~~|~~5850814~~|
|R4|Viviendas|731481|5851032|
|R5|Viviendas|731134|5851920|
|~~R6~~|~~Viviendas~~|~~730387~~|~~5850395~~|
|R7|Viviendas|732666|5850691|

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 41

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Tabla 12. Resultados de la modelación de calidad del aire (MP10) Construcción

|Receptor|Concentración ( g/m3)|
|---|---|
|~~MP10 (p 98 promedio 24 hrs)~~|~~MP10 (p 98 promedio 24 hrs)~~|
|~~R1~~|0,190|
|~~R2~~|0,503|
|~~R3~~|0,203|
|~~R4~~|0,187|
|~~R5~~|0,009|
|~~R6~~|0,003|
|~~R7~~|0,006|
|~~MP10 (promedio anual)~~|~~MP10 (promedio anual)~~|
|~~R1~~|0,047|
|~~R2~~|0,207|
|~~R3~~|0,049|
|~~R4~~|0,083|
|~~R5~~|0,001|
|~~R6~~|0,000|
|~~R7~~|0,002|

Fuente: Elaboración propia

Tabla 13. Resultados de la modelación de calidad del aire (MP2,5) Construcción

|Receptor|Concentración ( g/m3)|
|---|---|
|MP2,5 (p 98 promedio 24 hrs)|MP2,5 (p 98 promedio 24 hrs)|
|R1|0,039|
|R2|0,103|
|~~R3~~|0,042|
|~~R4~~|0,039|
|~~R5~~|0,002|
|~~R6~~|0,001|
|~~R7~~|0,002|
|~~MP2,5 (promedio anual)~~|~~MP2,5 (promedio anual)~~|
|~~R1~~|0,010|
|~~R2~~|0,043|
|~~R3~~|0,010|
|~~R4~~|0,017|
|~~R5~~|0,000|
|~~R6~~|0,000|
|~~R7~~|0,001|

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 42

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**8.3.4** **Determinación de impactos a la salud y área de influencia**

Para determinar el área de influencia del proyecto, se ha considerado el escenario de

construcción dónde las concentraciones llegan a 0,503 g/m [3 ] en el polígono de

Isoconcentraciones, de este modo se fija una superficie de 38,7 ha. Es importante mencionar

que las mayores concentraciones de MP10 y MP2,5 ocurren durante de la etapa construcción

y estas están influenciadas por las emisiones de actividades de movimiento de tierra y

tránsito de vehículos. El área de influencia entonces queda demarcada hacia el sur del

Proyecto.

Los riesgos relativos (RR) para la zona de estudio están basados en un incremental de 10

μg/m3, tanto para MP10 como MP2.5, debido a lo anterior los cambios en las

concentraciones en la zona de estudio son insuficientes como para generar un desbalance

en factor actual de riesgo a la salud de la población, en virtud de las diversas patologías

relacionadas y los intervalos etarios sobre los que se basan los RR.

|CALPUFF View - Lakes Environmental Software|Col2|
|---|---|
|<br>CALPUFF View - Lakes Environmental Software <br>|Titular<br>|
|<br>CALPUFF View - Lakes Environmental Software <br>|Modeler<br>|
|<br>CALPUFF View - Lakes Environmental Software <br>|Scale: 1:10.000<br>|
|<br>CALPUFF View - Lakes Environmental Software <br>|Proyect N°:<br>382-IEP23|

Figura 40. Área de influencia MP2,5

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 43

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**9** **CONCLUSIONES**

Con los resultados obtenidos mediante la modelación es posible concluir que las emisiones

provenientes del proyecto Macroloteo Los Ángeles, no provocarán un aporte significativo

sobre las concentraciones de contaminantes criterio en la zona del proyecto, para las etapas

de construcción y operación, dado que, en su operación, donde las emisiones representan

el peor escenario, no alcanzan a provocar un riesgo para la salud de la población basándose

en los niveles de concentración alcanzados.

Lo anterior se sustenta, en que el punto de mayor impacto de MP10 y MP2,5 se encuentra

inmediatamente alrededor de la zona de faenas de construcción y operación, alcanzando

ahí 0,5 μg/m3 para MP10 y 0,1 μg/m3 para MP2,5 como máxima concentración percentil 98

del promedio 24h para el año evaluado con información meteorológica 2022.

Con todo lo anterior, se puede concluir que el proyecto no provocará efectos adversos

significativos sobre la salud de la población ubicada tanto en el área circundante al proyecto

como en los receptores evaluados.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 44

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**10** **REFERENCIAS**

[1] SEIA, «Guía para el Uso de Modelos de Calidad del Aire en el SEIA,» Servicio de

Evaluación Ambiental, Chile, 2023.

[2] MMA, «D.S.N° 12/11 Establece Norma Primaria de Calidad del Aire para Material

Particulado Fino MP2,5.,»

[3] MMA «D.S. N° 12/2022 Establece Norma de Calidad Primara para Material Particulado

Respirable MP10, en Especial de los Valores que Definen Situaciones de Emergencia,»

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 45

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Norma de calidad del aire para Material Particulado y gases.**

| Contaminante | Valor | Periodo de<br>Evaluación | Forma de Verificación | Fuente<br>Normativa |
| --- | --- | --- | --- | --- |
| Material<br>particulado<br>respirable<br>(MP10) | 130 μg<br>/m3N | Promedio aritmético<br>de 24 hrs. | Percentil 98 de valores de un<br>año o más de 7 días en un año. | D.S. N° 12/2022<br>del<br>Ministerio<br>del<br>medio<br>Ambiente. |
| Material<br>particulado<br>respirable<br>(MP10) | 50 μg /m~~3~~N | Promedio aritmético<br>anual | Promedio aritmético de 3 años<br>consecutivos. | Promedio aritmético de 3 años<br>consecutivos. |
| Material<br>particulado fino<br>(MP2.5) | 50 μg /m~~3~~ | ~~Promedio aritmético~~<br>de 24 hrs. | ~~Percentil 98 de valores de 1~~<br>año. | ~~D.S. N° 12/2011~~<br>del<br>Ministerio<br>del<br>medio<br>Ambiente. |
| Material<br>particulado fino<br>(MP2.5) | 20 μg /m~~3~~ <br> | Promedio aritmético<br>anual. | Promedio aritmético de 3 años<br>consecutivos. | Promedio aritmético de 3 años<br>consecutivos. |
| ~~Dióxido de~~<br>azufre (SO2) | ~~80 μg /m3N ~~ | ~~Media aritmética~~<br>anual | ~~Promedio de tres años del~~<br>percentil 99 de las<br>concentraciones de 24 horas. | ~~D.S.~~<br>No113/2002<br>del<br>MINSEGPRES |
| ~~Dióxido de~~<br>azufre (SO2) | 250 μg<br>/m3N | Media aritmética<br>diaria | ~~Promedios de tres años del~~<br>percentil 99 de los máximos<br>diarios promedios de 8 horas. | ~~Promedios de tres años del~~<br>percentil 99 de los máximos<br>diarios promedios de 8 horas. |
| Monóxido de<br>Carbono<br>(CO) | 30 mg/<br>m3N | Media aritmética<br>horaria | Promedio de tres años del<br>percentil 99 de los máximos<br>diarios de 1 hora. | D.S.<br>No115/2002<br>del<br>MINSEGPRES |
| Monóxido de<br>Carbono<br>(CO) | 10 mg/<br>m3N | Promedio móvil de 8<br>hrs. | Promedios de tres años del<br>percentil 99 de los máximos<br>diarios promedios de 8 horas. | Promedios de tres años del<br>percentil 99 de los máximos<br>diarios promedios de 8 horas. |
| ~~Dióxido de~~<br>nitrógeno (NO2) | ~~100 μg~~<br>/m3N | ~~Media aritmética~~<br>anual | ~~Promedio aritmético de 3 años~~<br>consecutivos. | ~~D.S.~~<br>No114/2002<br>del<br>MINSEGPRES |
| ~~Dióxido de~~<br>nitrógeno (NO2) | ~~400 μg~~<br>/m3N | ~~Concentración de 1~~<br>hora | ~~Promedio de tres años del~~<br>percentil 99 de los máximos<br>diarios de 1 hora | ~~Promedio de tres años del~~<br>percentil 99 de los máximos<br>diarios de 1 hora |

**Tabla 2.: Coordenadas vértices del área de modelación del proyecto (Huso 18/19- WGS84)**

| Identificación | Coordenada E (m) | Coordenada S (m) |
| --- | --- | --- |
| NO | 708368 | 5875119 |
| NE | 755728 | 5873819 |
| SO | 707162 | 5828117 |
| ~~SE~~ | ~~754408~~ | ~~5826807~~ |

**Tabla 4.: Ubicación Estación de Radiosondeo para datos de altura**

| Nombre Estación | Coordenadas UTM (19 H) | Col3 |
| --- | --- | --- |
| Nombre Estación | ~~UTM-E~~ | ~~UTM-N~~ |
| ~~Santo Domingo ~~ | ~~257969~~ | ~~6273039~~ |

**Tabla 5.: Parámetros de cumplimiento de norma de MP2,5 años 2020-2022**

| Parámetro | 2020 | 2021 | 2022 |
| --- | --- | --- | --- |
| Norma anual | Norma anual | Norma anual | Norma anual |
| Promedio Anual (μg/m3 N) | 27 | 27 | 25 |
| No datos validados | 349 | 357 | 360 |
| % datos validados | 96% | 98% | 99% |
| Promedio Trianual (μg/m3 N) | 26 | 26 | 26 |
| Norma | 20 | 20 | 20 |
| % norma | 131% | 131% | 131% |
| Norma diaria | Norma diaria | Norma diaria | Norma diaria |
| Percentil 98 | 122 | 137 | 126 |
| Norma | 50 | 50 | 50 |
| % norma<br> | 244%<br> | 274%<br> | 252%<br> |

**Tabla 6.: Parámetros de cumplimiento de norma de MP10 años 2020-2022**

| Parámetro | 2020 | 2021 | 2022 |
| --- | --- | --- | --- |
| Norma anual | Norma anual | Norma anual | Norma anual |
| Promedio Anual (μg/m3 N) | 43 | 42 | 38 |
| No datos validados | 356 | 360 | 360 |
| % datos validados | 98% | 98% | 99% |
| Promedio Trianual (μg/m3 N)* | 41 | 41 | 41 |
| Norma | 50 | 50 | 50 |
| % norma | 82% | 82% | 82% |
| Norma diaria | Norma diaria | Norma diaria | Norma diaria |
| Percentil 98 | 133 | 149 | 135 |
| Norma | 150 | 150 | 130 |
| % norma<br> | 89%<br> | 99%<br> | 104%<br> |

**Tabla 7.: Fuentes de emisiones atmosféricas, durante etapa de construcción del Proyecto.**

| Tipo de<br>Emisión | Actividad | Tipo de<br>Contaminante |
| --- | --- | --- |
| Emisiones<br>directas | ~~Escarpe~~ | ~~MP 10, MP 2.5~~ |
| Emisiones<br>directas | ~~Excavaciones~~ | ~~MP 10, MP 2.5~~ |
| Emisiones<br>directas | ~~Carguío de camiones y transferencia de material~~ | ~~MP 10, MP 2.5~~ |
| Emisiones<br>directas | ~~Erosión de material en pila~~ | ~~MP 10, MP 2.5~~ |
| Emisiones<br>directas | ~~Tránsito por caminos no pavimentados al interior del sitio~~<br>donde se emplaza el Proyecto (vehículos pesados) | MP 10, MP 2.5 |
| Emisiones<br>directas | ~~Emisiones de gases de combustión de maquinaria y~~<br>vehículos. | ~~MP 10, MP 2.5 y~~<br>gases de combustión |
| Emisiones<br>indirectas | ~~Tránsito por caminos no pavimentados fuera del sitio~~<br>donde se emplaza el Proyecto (vehículos pesados y<br>livianos) | MP 10, MP 2.5 y<br>gases de combustión |

**Tabla 8.: Días de funcionamiento de la fuente**

| Horario | SEMANA | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <br>**Horario** | ~~Lun~~ | ~~Mar.~~ | ~~Mie.~~ | ~~Jue.~~ | ~~Vie.~~ | ~~Sab.~~ | ~~Dom.~~ |
| ~~8-9~~ |  |  |  |  |  |  |  |
| ~~9-10~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ |  |  |
| ~~10-11~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ |  |  |
| ~~11-12~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ |  |  |
| ~~12-13~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ |  |  |
| ~~13-14~~ |  |  |  |  |  |  |  |
| ~~14-15~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ |  |  |
| ~~15-16~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ |  |  |
| ~~16-17~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ |  |  |
| ~~17-18~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ | ~~X ~~ |  |  |

**Tabla 9.: Estadísticos de Desempeño del Modelo Meteorológico**

| Estadístico | Velocidad Viento | Col3 | Temperatura | Col5 |
| --- | --- | --- | --- | --- |
| Estadístico | Referencia | Valor obtenido | Referencia | Valor obtenido |
| BIAS | -2,5; 2,5 (m/s) | 2,3 | -4,4 (°C) | -0,1 |
| MAE | ≤3 | 2,4 | ≤4 | 2,9 |
| RMSE | ≤3,5 | 2,9 | ≤4,5 | 3,7 |
| Coeficiente correlación (r) | >0,6 | 0,51 | >0,8 | 0,83 |

**Tabla 10.: Resultados de la modelación de calidad del aire (máximo impacto).**

| Periodo | Contaminante | Construcción | Col4 |
| --- | --- | --- | --- |
| Periodo | Contaminante | Máx. (μg/m3) | % r/Norma |
| Diario | MP10 | 0,503 | 0,39% |
| Diario | MP2,5 | 0,103 | 0,21% |
| Anual<br> | MP10 | 0,207 | 0,41% |
| Anual<br> | MP2,5<br> | 0,043 | 0,22% |

**Tabla 11.: Identificación de los receptores discretos**

| Receptor | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| ~~ID~~ | ~~Tipo~~ | ~~Coordenada UTM E~~ | ~~Coordenada UTM S~~ |
| R1 | Viviendas | 731262 | 5850375 |
| R2 | Viviendas | 731451 | 5850590 |
| ~~R3~~ | ~~Viviendas~~ | ~~731570~~ | ~~5850814~~ |
| R4 | Viviendas | 731481 | 5851032 |
| R5 | Viviendas | 731134 | 5851920 |
| ~~R6~~ | ~~Viviendas~~ | ~~730387~~ | ~~5850395~~ |
| R7 | Viviendas | 732666 | 5850691 |

**Tabla 12.: Resultados de la modelación de calidad del aire (MP10) Construcción**

| Receptor | Concentración ( g/m3) |
| --- | --- |
| ~~MP10 (p 98 promedio 24 hrs)~~ | ~~MP10 (p 98 promedio 24 hrs)~~ |
| ~~R1~~ | 0,190 |
| ~~R2~~ | 0,503 |
| ~~R3~~ | 0,203 |
| ~~R4~~ | 0,187 |
| ~~R5~~ | 0,009 |
| ~~R6~~ | 0,003 |
| ~~R7~~ | 0,006 |
| ~~MP10 (promedio anual)~~ | ~~MP10 (promedio anual)~~ |
| ~~R1~~ | 0,047 |
| ~~R2~~ | 0,207 |
| ~~R3~~ | 0,049 |
| ~~R4~~ | 0,083 |
| ~~R5~~ | 0,001 |
| ~~R6~~ | 0,000 |
| ~~R7~~ | 0,002 |

**Tabla 13.: Resultados de la modelación de calidad del aire (MP2,5) Construcción**

| Receptor | Concentración ( g/m3) |
| --- | --- |
| MP2,5 (p 98 promedio 24 hrs) | MP2,5 (p 98 promedio 24 hrs) |
| R1 | 0,039 |
| R2 | 0,103 |
| ~~R3~~ | 0,042 |
| ~~R4~~ | 0,039 |
| ~~R5~~ | 0,002 |
| ~~R6~~ | 0,001 |
| ~~R7~~ | 0,002 |
| ~~MP2,5 (promedio anual)~~ | ~~MP2,5 (promedio anual)~~ |
| ~~R1~~ | 0,010 |
| ~~R2~~ | 0,043 |
| ~~R3~~ | 0,010 |
| ~~R4~~ | 0,017 |
| ~~R5~~ | 0,000 |
| ~~R6~~ | 0,000 |
| ~~R7~~ | 0,001 |
