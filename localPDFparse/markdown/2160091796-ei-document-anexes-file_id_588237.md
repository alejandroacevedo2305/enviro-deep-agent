---
title: Sin título
author: Raquel Tamara Saavedra Pino
date: D:20230915165833-03'00'
language: es
type: report
pages: 79
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - DECLARACIÓN DE IMPACTO AMBIENTAL Proyecto “PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS, SECTOR LA COMPAÑÍA - REINGRESO”. ANEXO 2.14 ESTUDIO DE MODELACION DE EMISIONES ATMOSFÉRICAS
  - Índice de Contenido
  - Índice de tablas
  - 1. Introducción
  - 2. Objetivos
  - 3. Marco regulatorio
  - 4. Metodología de modelación
  - 5. Resultados
  - 6. Conclusión
  - 7. Bibliografía
  ... y 2 secciones más
-->

# DECLARACIÓN DE IMPACTO AMBIENTAL Proyecto “PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS, SECTOR LA COMPAÑÍA - REINGRESO”. ANEXO 2.14 ESTUDIO DE MODELACION DE EMISIONES ATMOSFÉRICAS

**Septiembre, 2023.**

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

# Índice de Contenido

**1. INTRODUCCIÓN .............................................................................................. 7**

**2. OBJETIVOS ...................................................................................................... 9**

**3. MARCO REGULATORIO .................................................................................. 10**

3.1. M ATERIAL P ARTICULADO FINO (MP2.5): .................................................................. 10

3.2. M ATERIAL P ARTICULADO GRUESO (MP10): ............................................................... 11

3.3. M ATERIAL P ARTICULADO SEDIMENTABLE (MPS): ........................................................ 11

3.4. M ONÓXIDO DE C ARBONO (CO): ............................................................................. 12

3.5. D IÓXIDO DE A ZUFRE (SO 2 ): .................................................................................. 13

3.6. D IÓXIDO DE N ITRÓGENO (NO 2 ): ............................................................................ 14

**4. METODOLOGÍA DE MODELACIÓN .................................................................. 16**

4.1. M ODELOS UTILIZADOS ......................................................................................... 16

4.1.1. Modelo meteorológico ............................................................................... 16

4.1.2. Modelo de dispersión de contaminantes ...................................................... 16

4.2. C ARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN Y SU ENTORNO .................................... 17

4.2.1. Dominio de modelación ............................................................................. 17

4.2.2. Topografía y uso de suelo .......................................................................... 20

4.2.3. Elevación del terreno ................................................................................. 22

4.2.4. Receptores discretos ................................................................................. 22

4.2.5. Estaciones mete meteorológica y de calidad del aire .................................... 25

4.3. E SCENARIO DE MODULACIÓN ................................................................................. 27

4.4. A NÁLISIS DE DATOS OBSERVADOS Y MODELADOS ........................................................ 30

4.5. A NÁLISIS DE INCERTIDUMBRE ................................................................................ 45

**5. RESULTADOS ................................................................................................. 46**

5.1. S ITUACIÓN BASAL CALIDAD DEL AIRE ....................................................................... 46

5.2. C ONCENTRACIONES MODELADAS ............................................................................. 47

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 1 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

5.2.1. Material Particulado ................................................................................... 47

5.2.2. Gases ....................................................................................................... 55

5.3. E VALUACIÓN DISCRETA DE LOS NIVELES DE CONCENTRACIÓN ......................................... 64

5.3.1. Material Particulado ................................................................................... 64

5.3.2. Gases ....................................................................................................... 66

5.4. A NÁLISIS DE SIGNIFICANCIA .................................................................................. 70

5.5. Á REA DE INFLUENCIA ........................................................................................... 72

**6. CONCLUSIÓN................................................................................................. 74**

**7. BIBLIOGRAFÍA .............................................................................................. 75**

**8. ANEXO ........................................................................................................... 76**

Página 2 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

# Índice de tablas

T ABLA 1. N ORMA PRIMARIA DE CALIDAD AMBIENTAL PARA MATERIAL PARTICULADO FINO RESPIRABLE

MP2,5. ..................................................................................................................... 10

T ABLA 2. N ORMA PRIMARIA DE CALIDAD AMBIENTAL PARA MATERIAL PARTICULADO RESPIRABLE MP10.

............................................................................................................................... 11

T ABLA 3. V ALORES LIMITES AMBIENTALES PARA M ATERIAL P ARTICULA S USPENDIDO (MPS). ........... 12

T ABLA 4. N ORMA PRIMARIA DE CALIDAD DE AIRE PARA M ONÓXIDO DE C ARBONO (CO). ................. 12

T ABLA 5. N ORMA PRIMARIA DE CALIDAD DE AIRE PARA DIÓXIDO DE AZUFRE (SO2). ...................... 13

T ABLA 6. N ORMA PRIMARIA DE CALIDAD DE AIRE PARA D IÓXIDO DE N ITRÓGENO (NO 2 ). ................ 14

T ABLA 7. C ARACTERÍSTICAS DEL DOMINIO METEOROLÓGICO WRF. ........................................... 18

T ABLA 8 . U SO DE SUELO EN EL DOMOMINIO DE MODELACION . ................................................. 20

T ABLA 9 . C ARACTERÍSTICAS DE RECEPTORES DISCRETOS . ...................................................... 23

T ABLA 10 . E STACION METEREOLOGICA Y DE CALIDAD DEL AIRE . .............................................. 25

T ABLA 11. E MISIONES ESTIMADAS PARA EL AÑO MODELADO . ................................................... 27

T ABLA 12. A GRUPACIÓN DE ACTIVIDAD EMISORA PARA CADA FUETE DE EMISIÓN . .......................... 28

T ABLA 13. T ASA DE EMISION INGRESADAS A C ALPUFF . ........................................................... 30

T ABLA 14 . E STACIÓN METEOROLÓGICA A ERÓDROMO L A I NDEPENDENCIA, R ANCAGUA . .................. 31

T ABLA 15. A NÁLISIS ESTADÍSTICO E STACIÓN A ERÓDROMO L A I NDEPENDENCIA, R ANCAGUA . ........... 45

T ABLA 16 . P ORCENTAJE DE REGISTROS VALIDOS PARA CADA CONTAMINANTE EN LA ESTACION DE

CALIDAD DEL AIRE R ANCAGUA I. ....................................................................................... 46

T ABLA 17 . S ITUACION BASAL TRIANUAL . ........................................................................... 46

T ABLA 18 . P ORCENTAJE DE CUMPLIMIENTO DE LIMITE D.S. N°12/2011 MMA. .......................... 47

T ABLA 19 . P ORCENTAJE DE CUMPLIMIENTO DE LIMITE D.S. N°12/2021 MMA. .......................... 48

T ABLA 20 . P ORCENTAJE DE CUMPLIMIENTO DE LIMITE PARA MPS (C ONFEDERACIÓN S UIZA ). .......... 49

T ABLA 21 .P ORCENTAJE DE CUMPLIMIENTO DE LIMITE D.S. N°115/2002 MINSEGPRES. ............. 55

T ABLA 22 . P ORCENTAJE DE CUMPLIMIENTO DE LIMITE D.S. N°104/2018 MMA.......................... 56

T ABLA 23 . P ORCENTAJE DE CUMPLIMIENTO DE LIMITE D.S. N°114/2002 MINSGPRES. .............. 56

T ABLA 24. MP2,5 [ ΜG / M 3] PROMEDIO ANUAL . .................................................................... 64

Página 3 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

T ABLA 25. MP2,5 [ ΜG / M 3] PERCENTIL 98, 24 HORAS . ......................................................... 65

T ABLA 26. MP10[ ΜG / M 3] PROMEDIO ANUAL . ..................................................................... 65

T ABLA 27. MP10[ ΜG / M 3] PERCENTIL 98, 24 HORAS . ........................................................... 66

T ABLA 28. C ONCENTRACIÓN DIARIA [ ΜG / M 3]. .................................................................... 66

T ABLA 29. CO, P ERCENTIL 99, 1 HORA . ............................................................................ 67

T ABLA 30. CO, P ERCENTIL 99, 8 HORAS . ........................................................................... 67

T ABLA 31. SO 2, P ROMEDIO ANUAL . .................................................................................. 68

T ABLA 32. SO 2, P ERCENTIL 99, 24 HORAS . ........................................................................ 68T ABLA 33. SO 2, P ERCENTIL 98,5 1 HORA . ....................................................................... 68

T ABLA 34. NO 2, P ROMEDIO ANUAL . .................................................................................. 69

T ABLA 35. NO 2, P ERCENTIL 99, 1 HORA . ........................................................................... 69

T ABLA 36. A NÁLISIS DE SIGNIFICANCIA . ............................................................................. 71

Página 4 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Índice de figuras**

F IGURA 1 . E MPLAZAMIENTO DEL PROYECTO . ........................................................................ 8

F IGURA 2 .D OMINIO DE MODELACIÓN . ............................................................................... 19

F IGURA 3. T OPOGRAFÍA DEL ÁREA DE MODELACIÓN 3D. ......................................................... 20

F IGURA 5 . U SO DE SUELO DEL DOMINIO DE MODELACION . ...................................................... 21

F IGURA 5. E LEVACIÓN DEL TERRENO DEL D OMINIO DE M ODELACIÓN . ........................................ 22

F IGURA 6. U BICACIÓN DE RECEPTORES DISCRETOS . .............................................................. 24

F IGURA 7 . E STACION METEREOLOGICA Y DE CALIDAD DEL AIRE . ............................................... 26

F IGURA 8 . F UENTES DE EMISIÓN . .................................................................................... 29

F IGURA 9 . R OSA DE VIENTO 2019 DATOS OBSERVADOS ( IZQUIERDA ) Y MODELADOS ( DERECHA ) EN LA

ESTACION A ERODROMO L A INDEPENDENCIA, R ANCAGUA . ........................................................ 33

F IGURA 10. C OMPARACIÓN SERIE DE TIEMPO DE TEMPERATURA, DATOS OBSERVADOS ( ARRIBA ) Y

MODELADOS ( ABAJO ). .................................................................................................... 34

F IGURA 11. C OMPARACIÓN SERIE DE TIEMPO DE DIRECCIÓN DEL VIENTO, DATOS OBSERVADOS ( ARRIBA )

Y MODELADOS ( ABAJO ). ................................................................................................. 35

F IGURA 12. C OMPARACIÓN SERIE DE TIEMPO DE VELOCIDAD DEL VIENTO, DATOS OBSERVADOS ( ARRIBA )

Y MODELADOS ( ABAJO ). ................................................................................................. 36

F IGURA 13. C OMPARACIÓN CICLO DIARIO DE TEMPERATURA DATOS WRF Y ESTACIÓN A ERODROMO L A

I NDEPENDENCIA, R ANCAGUA . .......................................................................................... 38

F IGURA 14. C OMPARACIÓN CICLO DIARIO DE DIRECCIÓN DEL VIENTO DATOS WRF Y ESTACIÓN

A ERÓDROMO L A I NDEPENDENCIA, R ANCAGUA . ..................................................................... 39

F IGURA 15 . C OMPARACIÓN CICLO DIARIO DE VELOCIDAD DEL VIENTO DATOS WRF Y ESTACIÓN

A ERODROMO L A I NDEPENDENCIA, R ANCAGUA . ..................................................................... 40

F IGURA 16 . C ICLO ESTACIONAL DE TEMPERATURA DATOS OBSERVADOS ( ARRIBA ) Y MODELADOS ( ABAJO ).

............................................................................................................................... 42

F IGURA 17. C ICLO ESTACIONAL DE DIRECCIÓN DEL VIENTO DATOS OBSERVADOS ( ARRIBA ) Y MODELADOS
( ABAJO ). .................................................................................................................... 43

F IGURA 18 . C ICLO ESTACIONAL DE VELOCIDAD DEL VIENTO DATOS OBSERVADOS ( ARRIBA ) Y MODELADOS
( ABAJO ). .................................................................................................................... 44

F IGURA 20. MP2.5 [ ΜG / M [3] ] PROMEDIO ANUAL . ................................................................... 50

F IGURA 21. MP2.5 [ ΜG / M [3] ] P ERCENTIL 98, 24 HORAS . ........................................................ 51

Página 5 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

F IGURA 22. MP10 [ ΜG / M [3] ] P ROMEDIO ANUAL . ................................................................... 52

F IGURA 23. MP10 [ ΜG / M [3] ] P ERCENTIL 98, 24 HORAS . ......................................................... 53

F IGURA 24. MPS [ ΜG / M [3] ], P ROMEDIO, 24 HORAS . .............................................................. 54

F IGURA 24. CO [ ΜG / M 3], P ERCENTIL 99, 1 HORA ............................................................... 57

F IGURA 25 . CO [ ΜG / M [3] ] P ERCENTIL 99, 8 HORAS . .............................................................. 58

F IGURA 26 . SO2 [ ΜG / M 3], P ROMEDIO ANUAL . .................................................................. 59

F IGURA 27. SO2 [ ΜG / M 3], P ERCENTIL 99, 24 HORAS ........................................................... 60

F IGURA 28. SO2 [ ΜG / M 3], P ERCENTIL 98.5, 1 HORA . .......................................................... 61

F IGURA 29. NO 2 [ ΜG / M 3], P ROMEDIO ANUAL . .................................................................... 62

F IGURA 30. NO 2 [ ΜG / M 3], P ERCENTIL 99, 1 HORA .............................................................. 63

F IGURA 31 Á REA DE INFLUENCIA . ..................................................................................... 73

Página 6 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

# 1. Introducción

En la localidad del sector La Compañía, se presenta una urgente necesidad de abordar la
cuestión del saneamiento sanitario. Por lo tanto, la Ilustre Municipalidad de Graneros se
somete a la evaluación del proyecto titulado "Planta de tratamiento de aguas servidas,
sector la compañía - reingreso", como respuesta a esta imperante demanda. Es importante
destacar que los suelos de esta área carecen de la capacidad necesaria para absorber
adecuadamente el agua tratada. Como resultado, se hace necesario que las aguas tratadas
sean procesadas y posteriormente incorporadas a un curso de agua preexistente.

El objetivo principal de este informe es presentar una evaluación exhaustiva de la dispersión
y concentración de los contaminantes liberados en la atmósfera dentro del área de estudio,
en consonancia con la normativa vigente. Para lograr este propósito, se han utilizado
herramientas de modelación recomendadas por el Servicio de Evaluación Ambiental,
siguiendo las directrices establecidas en la Guía para el Uso de Modelos de Calidad del Aire
en el SEIA [1] . Además, se ha consultado la normativa en cuanto a la calidad primaria de
partículas (MP10 [2], MP2.5 [3] ), gases (SO 2 [4], NOx [5], CO [6] ) y la normativa internacional de Material
Particulado Suspendido (MPS) de la Confederación Suiza [7] .

Los datos relativos a las emisiones de contaminantes han sido obtenidos del Estudio de

Emisiones Atmosféricas, Anexo X de la DIA. Estos datos desempeñan un papel fundamental
en el análisis y la evaluación de los posibles impactos ambientales asociados con el proyecto
en cuestión.

La ubicación precisa del proyecto se encuentra en el Sector La Compañía, dentro de la
comuna de Graneros, en la Provincia de Cachapoal, Región del Libertador General Bernardo
O'Higgins. Para obtener una visión más detallada de la disposición geográfica de esta área,
se puede consultar la Figura 1.

1 https://sea.gob.cl/sites/default/files/imce/archivos/2023/02.FEB/28/Guia-Calidad-del-aire_V.4-final.pdf
2 https://www.bcn.cl/leychile/navegar?idNorma=1176988
3 https://www.bcn.cl/leychile/navegar?idNorma=1025202
4 https://www.bcn.cl/leychile/navegar?idNorma=1131641
5 https://www.bcn.cl/leychile/navegar?idNorma=208185
6 https://www.bcn.cl/leychile/navegar?idNorma=202437
7 https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1986/208_208_208/20220101/en/pdf-a/fedlex-dataadmin-ch-eli-cc-1986-208_208_208-20220101-en-pdf-a.pdf

Página 7 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Figura 1 . Emplazamiento del proyecto.**

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 8 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

# 2. Objetivos

El presente estudio persigue como objetivo fundamental la evaluación del impacto en la
atmósfera derivado de las emisiones de contaminantes provenientes del proyecto "Planta
de tratamiento de aguas servidas, sector la compañía - reingreso.". El propósito central
radica en el análisis exhaustivo de cualquier posible implicación para la salud y la calidad de
vida de las personas involucradas en actividades en las cercanías del área del proyecto.

Objetivos específicos:

I. Evaluar la extensión de la dispersión de diversos contaminantes, como el material

particulado (MP10, MP2,5 y MPS), el monóxido de carbono (CO), el dióxido de nitrógeno
(NO 2 ) y el dióxido de azufre (SO 2 ). Este análisis tiene como meta identificar y prever
áreas con impacto tanto máximo como mínimo, ofreciendo una comprensión clara de
cómo estos contaminantes se propagan en el entorno atmosférico.

II. Determinar la fiabilidad de los datos modelados al contrastarlos con las observaciones

reales. Este objetivo busca garantizar la precisión y validez de las simulaciones de
dispersión atmosférica, permitiendo una evaluación confiable y robusta de las posibles
implicaciones en la calidad del aire y la salud pública.

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 9 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

# 3. Marco regulatorio

A continuación, se exponen los límites y alcances de las normas de calidad primaria
relacionadas con el componente del aire. Estas normas definen los valores máximos o
mínimos permitidos para diversas concentraciones y periodos de contaminantes
atmosféricos, asegurando la protección de la salud pública y el entorno. Asimismo, se
presenta la norma de referencia Suiza para material particulado suspendido en el aire.

**3.1.** **Material Particulado fino (MP2.5):**

El material particulado fino (MP2.5) corresponde a un contaminante secundario producido
como resultado de las reacciones químicas a partir de precursores (SO 2, NOx, NH 3 y COVs),
y cuyos efectos sobre la salud de la población se refleja en enfermedades respiratorias y

cardiovasculares.

La normativa D.S. N°12/2011 del Ministerio del Medio Ambiente regula este tipo de
partículas, estableciendo límites normativos de superación y criterios para situaciones de
emergencia. Estos parámetros se detallan en la siguiente tabla.

**Tabla 1. Norma primaria de calidad ambiental para material particulado fino respirable**

**MP2,5.**

|Limite (Articulo n°3)|Col2|Norma8|
|---|---|---|
|**Promedio anual**|20 (μg/m3)|D.S. N°12/2011<br>Ministerio del medio<br>Ambiente|
|**Percentil 98, diario**|50 (μg/m3)|50 (μg/m3)|
|**Situaciones de emergencia (Articulo n°5)**<br>**Concentración 24 horas.**|**Situaciones de emergencia (Articulo n°5)**<br>**Concentración 24 horas.**|**Situaciones de emergencia (Articulo n°5)**<br>**Concentración 24 horas.**|
|**Alerta**|80-109 (μg/m3)|80-109 (μg/m3)|
|**Preemergencia**|110-169 (μg/m3)|110-169 (μg/m3)|
|**Emergencia**|>170 (μg/m3)|>170 (μg/m3)|

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

No obstante, la superación del límite normativo no es motivo de condiciones de superación
de la norma, sino que se considera que la norma es incumplida bajo las siguientes

condiciones:

I. Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 20 [μg/m3].

II. Si el percentil 98 (P98) de las de 24 horas durante un año sea igual o superior a

50 [μg/m3].

8 https://www.bcn.cl/leychile/navegar?idNorma=1025202

Página 10 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**3.2.** **Material Particulado grueso (MP10):**

El material particulado respirable (MP10) es un tipo de contaminante primario que se
compone de partículas sólidas o líquidas, como polvo, cenizas, hollín, partículas metálicas,
cemento y polen, entre otros. Este tipo de partículas ejerce sus efectos directamente en la
salud, afectando especialmente las vías respiratorias de las personas.

La normativa D.S. N°12/2021 del Ministerio del Medio Ambiente regula este tipo de
partículas, estableciendo límites normativos de superación y criterios para situaciones de
emergencia. Estos parámetros se detallan en la siguiente tabla.

**Tabla 2. Norma primaria de calidad ambiental para material particulado respirable**

**MP10.**

|Limite (Articulo n°3)|Col2|Norma9|
|---|---|---|
|**Promedio anual**|50 (μg/m3)|D.S. N°12/2021 Ministerio del<br>medio Ambiente|
|**Percentil 98, diario**|130 (μg/m3)|130 (μg/m3)|
|**Situaciones de emergencia (Articulo n°5)**<br>**Concentración 24 horas.**|**Situaciones de emergencia (Articulo n°5)**<br>**Concentración 24 horas.**|**Situaciones de emergencia (Articulo n°5)**<br>**Concentración 24 horas.**|
|**Alerta**|180-229 (μg/m3)|180-229 (μg/m3)|
|**Preemergencia**|230-329 (μg/m3)|230-329 (μg/m3)|
|**Emergencia**|>330 (μg/m3)|>330 (μg/m3)|

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

No obstante, la superación del límite normativo no es motivo de condiciones de superación
de la norma, sino que se considera que la norma es incumplida bajo las siguientes

condiciones:

I. Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 50 [μg/m3].

II. Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea igual

o superior a 130 [μg/m3].

III. Si durante un año se registrasen siete o más días cuya concentración sea mayor a

130 [μg/m3].

**3.3.** **Material Particulado sedimentable (MPS):**

El Material Particulado sedimentable (MPS) corresponde a partículas de tamaño mayor a 10
μm. Actualmente no existe normativa para la regulación de emisión de este contaminante,
por lo cual en virtud al Articulo n° 11 del D.S. N°40/2012 MMA [10], se aplica la normativa de
la confederación suiza para “Total dust deposition”.

9 https://www.bcn.cl/leychile/navegar?idNorma=1176988
10 https://www.bcn.cl/leychile/navegar?idNorma=1053563

Página 11 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

La siguiente tabla detalla el valor limite ambiental para MPS en aire.

**Tabla 3. Valores limites ambientales para Material Particula Suspendido (MPS).**

|Parámetro|Limite|Norma11|
|---|---|---|
|**Deposición seca**|200 (mg/m2x día)|Ordinance on Air Pollution<br>Control (OAPC)<br>The Swiss Federal Council.<br>(814.318.142.1)|

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

**3.4.** **Monóxido de Carbono (CO):**

El monóxido de carbono (CO) es un tipo de contaminante primario producido en la
combustión de gas natural, propano, gasolina, petróleo, queroseno, madera o carbón. Este
contaminante afecta a la salud de las personas al reducir la capacidad de sangre de
transportar oxigeno junto con retardo del desarrollo postnatal.

La normativa D.S. N°115/2002 del Ministerio Secretaría General de la Presidencia regula
este contaminante, estableciendo límites normativos de superación y criterios para
situaciones de emergencia. Estos parámetros se detallan en la siguiente tabla.

**Tabla 4. Norma primaria de calidad de aire para Monóxido de Carbono (CO).**

|Limite (Artículos n°3 y n°4)|Col2|Norma12|
|---|---|---|
|**Percentil 99, horario**|26 ppmv; 30 (mg/m3N)|D.S. N°115/2002<br>MINSEGRPRES|
|**Percentil 99, 8 horas**|9 ppmv; 10 (mg/m3N)|9 ppmv; 10 (mg/m3N)|
|**Situaciones de emergencia (Artículos n°3 y n°4)**<br>**Concentración Percentil 99, 8 horas**|**Situaciones de emergencia (Artículos n°3 y n°4)**<br>**Concentración Percentil 99, 8 horas**|**Situaciones de emergencia (Artículos n°3 y n°4)**<br>**Concentración Percentil 99, 8 horas**|
|**Nivel I**|15 - 29 ppmv; 17 - 33 (mg/m3N)|15 - 29 ppmv; 17 - 33 (mg/m3N)|
|**Nivel II**|30 - 34 ppmv; 34 - 39 (mg/m3N)|30 - 34 ppmv; 34 - 39 (mg/m3N)|
|**Nivel III**|>35 ppmv; >40 (mg/m3N)|>35 ppmv; >40 (mg/m3N)|

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

No obstante, la superación del límite normativo no es motivo de condiciones de superación
de la norma, sino que se considera que la norma es incumplida bajo las siguientes

condiciones:

I. Cuando la concentración de 8 horas, del promedio aritmético de tres periodos de 12

meses, es mayor o igual a 10 (mg/m [3] N)
II. Cuando la concentración de 1 hora, del promedio aritmético de tres periodos de 12

meses, es mayor o igual a 30 (mg/m [3] N)

11 https://planesynormas.mma.gob.cl/archivos/2016/proyectos/814.318.142.1_version_en_ingles.pdf
12 https://www.bcn.cl/leychile/navegar?idNorma=202437

Página 12 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**3.5.** **Dióxido de Azufre (SO** **2** **):**

El Dióxido de Azufre (SO 2 ) es un tipo de contaminante primario producido por la combustión
de combustibles fósiles y la actividad volcánica natural. Este contaminante afecta a la salud
de las personas al irritar la piel y las membras de las mucosas de los ojos, nariz, garganta y
pulmones.

La normativa D.S. N°104/2018 del Ministerio del Medio Ambiente regula este contaminante,
estableciendo límites normativos de superación y criterios para situaciones de emergencia.
Estos parámetros se detallan en la siguiente tabla.

**Tabla 5. Norma primaria de calidad de aire para dióxido de azufre (SO2).**

|Limite (Artículos n°3, n°4 y n°5)|Col2|Norma|
|---|---|---|
|**Promedio Anual**|23 ppbv; 60 (μg/m3N)|D.S. N°104/2018<br>Ministerio del medio<br>Ambiente|
|**Percentil 99, diario**|57 ppbv; 150 (μg/m3N)|57 ppbv; 150 (μg/m3N)|
|**Concentración de 1 hora**|134 ppbv; 250 (μg/m3N)|134 ppbv; 250 (μg/m3N)|
|**Situaciones de emergencia (Artículo n°8)**|**Situaciones de emergencia (Artículo n°8)**|**Situaciones de emergencia (Artículo n°8)**|
|**Alerta**|500 - 649 (μg/m3N)|500 - 649 (μg/m3N)|
|**Preemergencia**|650 - 949 (μg/m3N)|650 - 949 (μg/m3N)|
|**Emergencia**|> 950 (μg/m3N)|> 950 (μg/m3N)|

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

No obstante, se considerará sobrepasada la norma primaria de calidad de aire para dióxido
de azufre como **concentración anual**, cuando ocurra al menos, una de las siguientes

condiciones:

I. El promedio aritmético de tres años calendario sucesivos de los valores de

concentración anual, fuere mayor o igual al valor de la norma que se establece (60

[μg/m3].).

II. Si en un año calendario, el valor de la concentración anual, fuere mayor o igual al

doble del valor de la norma que se establece (60 [μg/m3].).

Por otro lado, se considerará sobrepasada la norma primaria de calidad de aire para dióxido
de azufre como **concentración 24 horas**, cuando ocurra al menos, una de las siguientes

condiciones:

I. El promedio aritmético de tres años calendario sucesivos de los valores del percentil

99 de las concentraciones de 24 horas registradas cada año, fuere mayor o igual al
valor de la norma que se establece (150 [μg/m3].).

II. Si en un año calendario, el valor correspondiente al percentil 99 de las

concentraciones de 24 horas registradas, fuere mayor o igual al doble del valor de
la norma que se establece (150 [μg/m3].).

Página 13 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

Finalmente, se considerará sobrepasada la norma primaria de calidad de aire para dióxido
de azufre como **concentración de 1 hora**, cuando ocurra al menos, una de las siguientes

condiciones:

I. El promedio aritmético de tres años calendario sucesivos de los valores del percentil

98,5 de las concentraciones de 1 hora registradas cada año, fuere mayor o igual al
valor de la norma que se establece. A partir del cuarto año calendario de publicada
la norma en el Diario Oficial, se considera un percentil 99 para evaluar esta condición
(350 [μg/m3].).

II. Si en un año calendario, el valor correspondiente al percentil 98,5 de las

concentraciones de 1 hora registradas, fuere mayor o igual al doble del valor de la
norma que se establece. A partir del cuarto año calendario de publicada la norma en
el Diario Oficial, se considera un percentil 99 para evaluar esta condición (350

[μg/m3].).

**3.6.** **Dióxido de Nitrógeno (NO** **2** **):**

El Dióxido de Nitrógeno (NO 2 ) es un tipo de contaminante primario emitido en pequeñas
cantidades junto con el NO, pero fundamentalmente se origina por oxidación del NO en la
atmósfera. Este contaminante afecta a la salud de las personas al irritar los pulmones y al

disminuir la resistencia a enfermedades infecciosas.

La normativa D.S. N°114/2002 Ministerio Secretaría General de la Presidencia regula este
contaminante, estableciendo límites normativos de superación y criterios para situaciones
de emergencia. Estos parámetros se detallan en la siguiente tabla.

**Tabla 6. Norma primaria de calidad de aire para Dióxido de Nitrógeno (NO** **2** **).**

|Limite (Artículos n°3 y N°4)|Col2|Norma|
|---|---|---|
|**Promedio Anual**|53 ppbv; 100 (μg/m3N)|D.S. N°114/2002<br>MINSEGRPRES|
|**Percentil 99, horario**<br>|213 ppbv; 400 (μg/m3N)<br>|213 ppbv; 400 (μg/m3N)<br>|
|**Situaciones de emergencia (Articulo n°5)**|**Situaciones de emergencia (Articulo n°5)**|**Situaciones de emergencia (Articulo n°5)**|
|**Nivel 1**|601 - 1201 ppbv|601 - 1201 ppbv|
|**Nivel 2**|1202 - 1595 ppbv|1202 - 1595 ppbv|
|**Nivel 3**|>1596 ppbv|>1596 ppbv|

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

No obstante, la superación del límite normativo no es motivo de condiciones de superación
de la norma, sino que se considera que la norma es incumplida bajo las siguientes

condiciones:

I. Cuando la concentración de anual, del promedio aritmético de tres periodos de 12

meses consecutivos, es mayor o igual a 100 (μg/m [3] N).

Página 14 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

II. Cuando la concentración de 1 hora, del promedio aritmético de tres periodos de 12

meses del percentil 99 de los máximos diarios, es mayor o igual a 400 (μg/m [3] N).

Página 15 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

# 4. Metodología de modelación

**4.1.** **Modelos utilizados**

**4.1.1.Modelo meteorológico**

El modelo Weather Research and Forecasting (WRF), es un modelo numérico recomendado
para la generación de datos meteorológicos y uno de los modelos de pronóstico
meteorológicos más avanzados.

Debido a la falta de una red robusta de estaciones meteorológicas, la Guía para el Uso de
Modelos de Calidad del Aire [13] en el SEIA recomienda el uso de WRF por sobre el modelo
meteorológico CALMET. Además, el mismo documento, sugiere el uso del WRF para la
modelación de dispersión de contaminantes con CALPUFF.

**4.1.2.Modelo de dispersión de contaminantes**

La modelación de dispersión de contaminantes emitidos por el Proyecto, se realizó con un
modelo tipo “Puff”, específicamente el modelo CALPUFF.

Tal como lo define la Guía para el Uso de Modelos de Calidad del Aire en el SEIA, los modelos
tipo “puff” son una combinación entre los modelos Gaussianos y los modelos Lagrangeanos,
en el sentido de que esencialmente calculan la dispersión de contaminantes y odorantes
provenientes de una emisión instantánea, llamada “puff”, a lo largo de una trayectoria. Su
aproximación matemática consiste en estimar la dispersión en forma Gaussiana en cada
punto de una trayectoria; es decir, los modelos tipo “puff” sólo requieren una trayectoria
por “puff”, lo que hace su cálculo mucho más rápido. En el caso de emisiones continuas, se
simulan las trayectorias y la dispersión Gaussiana de muchos “puffs”.

Así mismo, es un modelo completo que incorpora herramientas para procesar datos
meteorológicos y geofísicos, modelos de dispersión y post procesamiento. Dicho modelo es
recomendado por la Agencia de Protección Ambiental de los Estados Unidos (EPA) para
modelar transporte a larga distancia de contaminantes.

CALPUFF se compone de tres módulos:

**CALMET:** Es un modelo meteorológico que desarrolla campos horarios de viento y
temperatura en una grilla de tres dimensiones, también asocia campos en dos dimensiones
de altura y usos de suelo. Sin embargo, este módulo puede ser reemplazado por el modelo
meteorológico WRF, el que es recomendado por la Guía para el Uso de Modelos de Calidad

del Aire en el SEIA.

**CALPUFF:** Es un modelo de transporte y dispersión emitido desde fuentes modeladas,
simulando procesos de dispersión y transformación. CALPUFF utiliza los datos generados

13
https://sea.gob.cl/sites/default/files/imce/archivos/2023/02.FEB/28/Guia-Calidad-del-aire_V.4-final.pdf

Página 16 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

por CALMET. Los archivos de salida de CALPUFF contienen las concentraciones horarias o
deposición por hora de flujos evaluados en receptores seleccionados.

**CALPOST:** Es usado para procesar aquellos archivos generados por CALMET y CALPUFF,
produciendo tabulaciones que resumen los resultados de la simulación.

Ecuación del modelo CALPUFF:

La ecuación básica que utiliza el modelo para realizar las modelaciones es la siguiente:

Ecuación 2.

[−d] 2σ y [2][c2] []]

Q
C=
2πσ x σ y

g exp

~~[~~ [−d] 2σ x [2][a2]

[−d] 2σ x [2][a2] [] exp] ~~[[]~~ [−d] 2σ y [2][c2]

∞

Ecuación 3.

2
g=

1
2 σ z

∑exp ~~[~~ [−(H] [e] 2σ [+ 2nh)] z [2] [2]

(2π ~~)~~

n=−∞

[+ 2nh)] [2]

2σ z [2] ]

Dónde:

C, es concentración a nivel del suelo (g/m [3] ).

Q, es masa de contaminantes (g) en la nube.

σx, es desviación estándar (m) de la distribución de Gauss en el viento a lo largo de la
dirección.

σy, es desviación estándar (m) de la distribución de Gauss en el viento de costado

σz, es desviación estándar (m) de la distribución de Gauss en la dirección vertical.

da, es distancia (m) del centro de la nube al receptor en la dirección del viento a lo largo.

dc, es distancia (m) del centro de la nube al receptor en la dirección de viento cruzado.

g, es el término vertical (m) de la ecuación Gaussiana.

H, es la altura afectiva (m) desde el nivel del suelo del hojaldre.

h, es la altura de la capa de mezcla.

Considerando las características del terreno, las distintas unidades geomorfológicas del área
de influencia del Proyecto y el dominio de la modelación consideraron utilizar el modelo
CALPUFF para simular la dispersión de odorantes presentes.

**4.2.** **Características del dominio de modelación y su entorno**

**4.2.1.Dominio de modelación**

Se determinó un dominio de modelación WRF que incluyó el área circundante a la zona de
emplazamiento del proyecto, es decir la comuna de Graneros. De esta forma el dominio de
la modelación meteorológica quedó definido en una extensión de 50 x 50 [km [2] ], con

Página 17 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

resolución de 1 km. En la figura a continuación, se observa la ubicación espacial del dominio
de la modelación, cuyas características se presentan en la siguiente tabla.

**Tabla 7. Características del dominio meteorológico WRF.**

|Datos|Col2|Archivo meteorológico|
|---|---|---|
|Dimensión grilla|Dimensión grilla|50 [km] x 50 [km]|
|Espaciado grilla|Espaciado grilla|1 [km]|
|Fe/hora inicio - Fecha/Hora fin|Fe/hora inicio - Fecha/Hora fin|01/01/2019 00:00 - 01/01/2020 20:00|
|Coordenada SO|Este [m]|312.407,24|
|Coordenada SO|Norte [m]|6.193.204,60|
|Coordenada SE|Este [m]|362.513,63|
|Coordenada SE|Norte [m]|6.194.078,25|
|Coordenada NO|Este [m]|311.543,16|
|Coordenada NO|Norte [m]|6.243.085,60|
|Coordenada NE|Este [m]|361.648,86|
|Coordenada NE|Norte [m]|6.243.949,16|

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

Página 18 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Figura 2 .Dominio de modelación.**

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 19 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**4.2.2.Topografía y uso de suelo**

La topografía del dominio fue obtenida de las bases satelitales topográfica SRTM1 que
poseen una cobertura global con aproximadamente 90 m de resolución y las bases de uso
de suelo GLCC con 1 km de resolución.

La representación en tres dimensiones en la siguiente figura da cuenta de los principales
accidentes topográficos de la zona de estudio

**Figura 3. Topografía del área de modelación 3D.**

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

Además, se obtuvo la descripción de suelo en el dominio de modelación. La siguiente tabla
y figura detalla las categorías de uso de suelo.

**Tabla 8 . Uso de suelo en el domominio de modelacion.**

|Agrupación|Descripción (MAKEGEO Land Use model)|
|---|---|
|Urbano|Residential; Commercial Services; Industrial; Transportation,<br>Communications; Industrial and Commercial; Mixed Urban or Built-Up Land;<br>Other Urban or Built-Up Land|
|Agricola|Cropland and Pasture; Orchards, Groves, Vineyards, Nurseries; Confined<br>Feeding Operations; Other Agricultural Land|
|Pastizal|Herbaceous Rangeland; Shrub and Brush Rangeland; Mixed Rangeland|
|Bosque|Deciduous Forest Land; Evergreen Forest Land; Mixed Forest Land|
|Terrenos Baldíos<br>mixtos|Dry Salt Flats; Beaches; Sandy Areas Other than Beaches; Bare Exposed<br>Rock; Strip Mines, Quarries, and Gravel Pits; Transitional Areas; Mixed<br>Barren Land|

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 20 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Figura 4 . Uso de suelo del dominio de modelacion.**

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 21 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**4.2.3.Elevación del terreno**

En la siguiente figura se puede observar una vista trasversal de topografía dentro del
dominio de modelación meteorológica. Se observa que la topografía en general del dominio
varia de 2.376,5 a 300 m.s.n.m.

**Figura 5. Elevación del terreno del Dominio de Modelación** **.**

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

**4.2.4.Receptores discretos**

Para analizar los resultados de la modelación de dispersión de MP2,5, MP10, NO2 y SO2, se
realizan mapas de iso-concentraciones de las emisiones generadas por las actividades del
proyecto. Dichos mapas permiten evaluar los niveles de concentración en toda el área de

estudio.

Es importante señalar que los mapas nacen de la modelación del dominio, representado a
través de una grilla de resolución 1 km, la que entrega datos de concentración de cada
vértice de la misma. Dadas las características de la grilla, los mapas son el resultado de la
interpolación entre los datos de modelación en cada vértice. Además, los datos de
concentración generados por el modelo son el resultado de la concentración promedio de la

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 22 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

primara capa de modelación, la que tiene lugar desde 0 m nivel del suelo hasta los 20 m.

Por todo lo antes indicado, el mapa de isoconcentración debe ser considerado como una
representación espacial de la pluma y no como referencia concreta de la concentración. Por
el contrario, la evaluación de la concentración en puntos discretos ofrece un sentido de la
magnitud más libre de distorsiones. Por esta razón y con objeto de analizar el impacto en
la calidad del aire en las poblaciones más cercanas, se realizó una modelación discreta, en
receptores específicos.

Los receptores identificados corresponden a las poblaciones más cercanas al proyecto,
juntos con los receptores sensibles como centros educacionales y de salud. Cabe señalar
que la grilla de los receptores corresponde al de tipo 2, con un espaciado de 50 m para
perímetros de 0,5 km, tal como se detalla en el apartado 4.5.2 de la “Guía Para El Uso De

Modelos De Calidad Del Aire En El SEIA” II Ed. - 2023.

En la siguiente tabla, se presentan las coordenadas y la distancia al proyecto de cada uno
de los puntos evaluados. Así mismo, en la Figura 6, se puede observar su ubicación espacial
de los receptores.

**Tabla 9 . Características de receptores discretos.**

|Receptor|Distancia<br>al<br>perímetro<br>de la<br>planta<br>(km)|Altura<br>(m.s.n.m)|Coordenadas<br>[m] UTM WGS-<br>84, Huso 19S|Col5|Descripción|
|---|---|---|---|---|---|
|**Receptor**|**Distancia**<br>**al**<br>**perímetro**<br>**de la**<br>**planta**<br>**(km)**|**Altura**<br>**(m.s.n.m)**|**Este**|**Norte**|**Norte**|
|Re1|0,15|487|344633|6225424|Centro De Restauración Y<br>Rehabilitación Casa Betel|
|Re2|0,33|485|344253|6225476|Vivienda|
|Re3|1,10|480|343363|6225175|Fundo El Parronal, Camino Sta.<br>Margarita|
|Re4|0,38|489|345012|6225246|Vivienda|
|Re5|0,45|487|344909|6224852|Vivienda|
|Re6|0,48|486|344834|6224745|Vivienda|
|Re7|0,53|487|344768|6224653|Vivienda|
|Re8|6,01|462|338517|6224401|Escuela de Tuniche|
|Re9|6,33|472|339495|6221288|CESFAM N°8 Dr. Nicolás Díaz|
|Re10|5.620|498|342431|6219932|CESFAM N°6 Ignacio Caroca|

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

Página 23 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Figura 6. Ubicación de receptores discretos.**

**Fuente** : Elaboración Ambiente Social, agosto 2023.

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 24 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**4.2.5.Estaciones mete meteorológica y de calidad del aire**

De acuerdo a los criterios establecidos por la Guía para el uso de modelos de calidad del
aire en el SEIA14, se recomienda seleccionar un modelo que pueda representar de manera
adecuada la heterogeneidad de la meteorología en el área de interés. En el caso de los
contaminantes primarios y considerando un rango de 5 km desde la fuente de emisión, se
menciona la utilización de modelos tipo puff como CALPUFF.

La Tabla 10 y Figura 7 informan las estaciones meteorológicas y de calidad del aire más
cercanas al Proyecto.

**Tabla 10 . Estacion metereologica y de calidad del aire.**

|Estación|Distancia desde<br>Proyecto (km)|Latitud E|Longitud S|
|---|---|---|---|
|**Estación**|**Distancia desde**<br>**Proyecto (km)**|**UTM Huso 19S [m]**|**UTM Huso 19S [m]**|
|Aeródromo La Independencia**15**|10,78|336.861,02|6.217.578,94|
|Rancagua I16|5,66|342.014,62|6.220.035,35|

**Fuente:** Ambiente Social, agosto 2023.

A partir de la información entregada previamente, la estación Aeródromo La Independencia,
Rancagua, es la más idónea para evaluar los datos meteorológicos modelados, aun cuando
excede el límite de 5 km señalado por la guía.

En primer lugar, la estación se encuentra relativamente cerca del Proyecto, lo que significa
que puede ofrecer información valiosa sobre las condiciones meteorológicas en la zona de
interés. Aunque la heterogeneidad de la meteorología puede aumentar con la distancia, la
estación aún puede proporcionar una estimación razonable de los patrones generales del
viento y las condiciones atmosféricas locales.

Además, la guía señala que se deben considerar las características topográficas del área de
interés, como la orografía, el uso del suelo, la presencia de cuerpos de agua y la vegetación.
La estación Aeródromo La Independencia, Rancagua, al estar ubicada en una zona cercana
al Proyecto, puede capturar algunas de estas características topográficas y proporcionar
información relevante sobre la rugosidad superficial y otros factores que pueden influir en
la dispersión de las especies contaminantes.

Al mismo tiempo, es importante destacar que la estación de monitoreo de calidad del aire
Rancagua I se distingue por ser aquella que registra la mayor cantidad de contaminantes
normadas, incluyendo el material particulado MP10 y MP2.5, así como el monóxido de
carbono (CO) y el dióxido de azufre (SO2).

En las siguientes secciones se evaluará la validez del modelo WRF a partir de los datos
observados en la estación Aeródromo La Independencia, Rancagua.

14 https://sea.gob.cl/sites/default/files/imce/archivos/2023/02.FEB/28/Guia-Calidad-del-aire_V.4-final.pdf
15 https://agrometeorologia.cl
16 https://sinca.mma.gob.cl

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 25 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Figura 7 . Estacion metereologica y de calidad del aire.**

**Fuente** : Elaboración Ambiente Social, septiembre 2023.

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 26 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**4.3.** **Escenario de modulación**

Según los resultados derivados de la estimación de emisiones, los cuales están disponibles
para consulta en el Estudio de Emisiones Atmosféricas, Anexo X de la DIA y considerando
la obligación impuesta por la normativa vigente de llevar a cabo un análisis anual del impacto
resultante de las emisiones de un proyecto, se ha establecido un escenario de modelación
representativo para el año de mayor emisión del proyecto. En este contexto, dicho año
coincide con la totalidad de la fase de construcción, y ocho meses de la fase de operación.

La siguiente tabla proporciona un desglose detallado de las emisiones estimadas para el año
de mayor emisión. Se considera el peor escenario, es decir, sin la aplicación de Bischofita.

**Tabla 11. Emisiones estimadas para el año modelado.**

|Fase|MP10|MP2.5|MPS|NOX|SO<br>2|NH<br>3|CO|COV|
|---|---|---|---|---|---|---|---|---|
|Construcción|0.538|0.147|1.508|0.325|0.006|0.000|0.156|0.025|
|Operación|0.465|0.053|1.387|0.044|0.002|0.000|0.009|0.003|
|**Total**|**1.003**|**0.200**|**2.895**|**0.369**|**0.008**|**0.000**|**0.165**|**0.028**|

**Fuente:** Ambiente Social, septiembre 2023.

Las emisiones anuales (t/año) se han distribuido en un escenario temporal mensual-horario.
En la fase de construcción, este escenario contempla un período de 4 meses, con 20 días
laborales al mes y 560 horas laborales al mes. Por otro lado, durante la operación, se ha
considerado un período de 6 meses, con 7 días laborables a la semana y 24 horas laborales
diarias, dado que la Planta de Tratamiento de Aguas Servidas (PTAS) opera con jornadas

laborales de 3 turnos.

Con respecto a las fuentes de emisión, estas se dividen en tres categorías principales: área,
puntual y camino.

Dentro de la categoría de emisiones de área, se incluyen las siguientes fuentes: excavación
(EXC), zona de acopio (AC) y movimiento de tierra (MT).

En la categoría de fuentes de emisiones de tipo puntual, se encuentran tres grupos
electrógenos, dos de los cuales se utilizan durante la fase de construcción (GE-CO1 y GECO2), y uno en la fase de operación (GE-OP).

En cuanto a las fuentes relacionadas a camino, se dividen en dos tipos: caminos no
pavimentados y caminos pavimentados. La fuente de camino no pavimentado (RI) se
refieren a la ruta interna hacia el proyecto, que se extiende desde la ruta H15G hasta la
entrada del proyecto. Por otro lado, las fuentes asociadas a la ruta pavimentada, se
subdividen en un tramo norte (H15G-N) y tramos sur (H15G-S).

A continuación, la Tabla 12 muestra la relación entre la actividad emisora y la fuente de
emisión, tanto para la fase de construcción como para la operación. Además, la Figura 8
representa gráficamente la ubicación de estas fuentes de emisión.

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 27 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Tabla 12. Agrupación de actividad emisora para cada fuete de emisión.**

|Actividad emisora|Construcción|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Operación|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad emisora**|**EXC**|**MT**|**AC**|**GE-**<br>**CO1**|**GE-**<br>**CO2**|**RI**|**HAP5G**<br>**-N**|**HAP5G**<br>**-S**|**RI**|**HAP5G**<br>**-N**|**HAP5G**<br>**-S**|**GE-OP**|
|Escarpe|NA|AP|NA|NA|NA|NA|NA|NA|NA|NA|NA|NA|
|Excavaciones|AP|NA|NA|NA|NA|NA|NA|NA|NA|NA|NA|NA|
|Erosión Material en Pila|NA|NA|AP|NA|NA|NA|NA|NA|NA|NA|NA|NA|
|Carguío y volteo de material|NA|NA|AP|NA|NA|NA|NA|NA|NA|NA|NA|NA|
|Compactación|NA|AP|NA|NA|NA|NA|NA|NA|NA|NA|NA|NA|
|Nivelación|NA|AP|NA|NA|NA|NA|NA|NA|NA|NA|NA|NA|
|Tránsito de vehículos caminos<br>no pavimentados.|NA|NA|NA|NA|NA|AP|NA|NA|AP|NA|NA|NA|
|Tránsito de vehículos caminos<br>pavimentados.|NA|NA|NA|NA|NA|NA|AP|AP|NA|AP|AP|NA|
|Combustión de vehículos en<br>ruta|NA|NA|NA|NA|NA|AP|AP|AP|AP|AP|AP|NA|
|Combustión de vehículos<br>fuera de ruta|AP|AP|NA|NA|NA|NA|NA|NA|NA|NA|NA|NA|
|Combustión grupo<br>electrógeno|NA|NA|NA|AP|AP|NA|NA|NA|NA|NA|NA|AP|
|AP: Aplica;<br>NA: No Aplica|AP: Aplica;<br>NA: No Aplica|AP: Aplica;<br>NA: No Aplica|AP: Aplica;<br>NA: No Aplica|AP: Aplica;<br>NA: No Aplica|AP: Aplica;<br>NA: No Aplica|AP: Aplica;<br>NA: No Aplica|AP: Aplica;<br>NA: No Aplica|AP: Aplica;<br>NA: No Aplica|AP: Aplica;<br>NA: No Aplica|AP: Aplica;<br>NA: No Aplica|AP: Aplica;<br>NA: No Aplica|AP: Aplica;<br>NA: No Aplica|

**Fuente:** Ambiente Social, septiembre 2023.

Página 28 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 8 . Fuentes de emisión.**

**Fuente:** Ambiente Social, septiembre 2023.

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 29 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

La siguiente tabla presenta un desglose de las emisiones honoraria que se introdujeron en
el modelo Calpuff, clasificadas por su fuente de origen.

Para más detalles consultar la planilla de cálculo del Apéndice n°2.

**Tabla 13. Tasa de emision ingresadas a Calpuff.**

|Fuente<br>de<br>emisión|Unidad|Construcción|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Fuente**<br>**de**<br>**emisión**|**Unidad**|**MP10 **|**MP25 **|**MPS**|**NOX **|**SOX **|**NH3 **|**CO**|**COV**|
|EXC|g/s*m2|2E-06|5E-07|4E-06|2E-07|5E-10|1E-10|2E-07|2E-08|
|MT|g/s*m2|9E-08|3E-08|2E-07|2E-07|5E-10|1E-10|2E-07|2E-08|
|AC|g/s*m2|9E-08|1E-08|7E-07|0E+00|0E+00|0E+00|0E+00|0E+00|
|GE-CO1|g/s|4E-05|4E-05|4E-05|5E-04|3E-05|0E+00|1E-04|4E-05|
|GE-CO2|g/s|4E-05|4E-05|4E-05|5E-04|3E-05|0E+00|1E-04|4E-05|
|RI|g/s*m|5E-07|5E-08|5E-07|2E-08|2E-11|1E-11|4E-09|8E-10|
|H15G-N|g/s*m|5E-08|1E-08|2E-07|4E-08|4E-11|3E-11|8E-09|1E-09|
|H15G-S|g/s*m|3E-08|6E-05|1E-03<br>|2E-04<br>|2E-07|1E-07|4E-05|7E-06|
|||||||||||
|**Fuente**<br>**de**<br>**emisión**|**Unidad**|**Operación**|**Operación**|**Operación**|**Operación**|**Operación**|**Operación**|**Operación**|**Operación**|
|**Fuente**<br>**de**<br>**emisión**|**Unidad**|**MP10 **|**MP25 **|**MPS**|**NOX **|**SOX **|**NH3 **|**CO**|**COV**|
|RI|g/s*m|3E-06|3E-07|8E-06|3E-09|4E-12|4E-12|6E-10|1E-10|
|H15G-N|g/s*m|1E-08|3E-09|5E-08|3E-09|4E-12|4E-12|7E-10|1E-10|
|H15G-S|g/s*m|4E-09|1E-09|2E-08|1E-09|2E-12|2E-12|3E-10|5E-11|
|GE-OP|g/s|1E-05|1E-05|1E-05|1E-04|9E-06|0E+00|3E-05|1E-05|

**Fuente:** Ambiente Social, septiembre 2023.

**4.4.** **Análisis de datos observados y modelados**

La Guía para el Uso de Modelos de Calidad de Aire en el SEIA [17], en su capítulo 6, establece
la necesidad de realizar una comparación entre los registros del modelo WRF y la
información meteorológica local. Para llevar a cabo esta comparación, se utilizan los datos
disponibles de las estaciones de monitoreo ubicadas en la zona de interés del estudio.

Dentro del dominio del modelo WRF utilizado, se encuentra la estación meteorológica del
Aeródromo La Independencia, Rancagua, perteneciente al INIA [18], ubicada a una distancia
de 11 kilómetros del Proyecto. Es relevante destacar que, esta misma estación también fue
empleada en el estudio de estimación de emisiones, ya que la estación de Calidad del Aire
Rancagua I de la Red SINCA [19], que se encuentra a 6 kilómetros del proyecto, carece de
registros de precipitación acumulada desde el año 2018.

La elección de utilizar los datos meteorológicos provenientes de la estación Aeródromo La
Independencia para la validación del modelo meteorológico WRF, se tomó con el propósito
de garantizar coherencia en la declaración de emisiones. Es relevante subrayar que, dado

17 https://sea.gob.cl/sites/default/files/imce/archivos/2023/02.FEB/28/Guia-Calidad-del-aire_V.4-final.pdf
18 https://agrometeorologia.cl
19 https://sinca.mma.gob.cl

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 30 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

que el uso de los datos observados de la estación meteorológica busca estimar la
incertidumbre de los datos del modelo meteorológico, la selección de una estación
meteorológica más distante del proyecto, pero aún dentro del dominio de modelación, es

adecuada.

Los datos de la meteorología observada, que se analizaran a continuación, fueron obtenidos
de la red Agroclimatología INIA, en la estación meteorológica Aeródromo La Independencia,
Rancagua. Las características específicas de esta estación se presentan en la tabla siguiente.

**Tabla 14 . Estación meteorológica Aeródromo La Independencia, Rancagua.**

|Parámetro|Col2|Col3|
|---|---|---|
|Coordenada UTM, Huso 19S,<br>Datum WGS84|Este [m]|336.861,00|
|Coordenada UTM, Huso 19S,<br>Datum WGS84|Norte [m]|6.217.578,90|
|Distancia desde el proyecto [km]|Distancia desde el proyecto [km]|22,2|
|Periodo de registro|Periodo de registro|1/1/2019 1:00:00 AM - 1/1/2020 0:00:00 AM|
|Variables meteorológicas|Variables meteorológicas|Temperatura, velocidad y dirección del viento|

**Fuente:** Ambiente Social, septiembre 2023.

Es importante destacar que la estación posee un registro válido del 81% de los datos, lo
cual cumple con el valor límite establecido por la Guía para Modelos de Calidad del Aire del
SEA, que exige al menos un 75% de los datos válidos. Para obtener información más
detallada, se puede consultar el Apéndice n° 4.

**Rosa de los vientos**

Basándonos en los datos de dirección del viento, tanto observados como modelados, que
se muestran en la Figura 9, es posible señalar que los registros observados exhiben una
prevalencia de vientos procedentes del sur, en contraste con los datos modelados que
indican un origen de viento desde la dirección suroeste.

**Series de tiempo**

A partir de la Figura 10, se puede deducir que las series temporales de temperatura exhiben
promedios similares entre los datos observados y los datos del modelo WRF (10,9 y 13,9 °C
respectivamente). Además, el comportamiento de la temperatura sigue el mismo patrón
tanto en el modelo de pronóstico como en el de datos observados, excepto en el mes de
febrero de ultimo, donde existe una notable falta de mediciones. Dadas estas circunstancias
y en relación a la serie de tiempo de temperatura, se puede afirmar que el modelo resulta
apropiado.

A partir de la Figura 11, se puede inferir que las series temporales de dirección del viento
muestran promedios con valores similares entre los datos observados y los datos del modelo
WRF (166 y 206° respectivamente). Además, el comportamiento de la dirección del viento
sigue un patrón similar tanto en el modelo de pronóstico como en las observaciones, con la
excepción del mes de febrero en los datos observados, donde se observa una marcada falta
de mediciones. Dadas estas circunstancias y considerando la serie de tiempo de la dirección

Página 31 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

del viento, se puede concluir que el modelo es apropiado.

A partir de la Figura 12, se puede llegar a la conclusión de que las series temporales de
velocidad del viento exhiben promedios con valores similares entre los datos observados y
los datos del modelo WRF (1,6 y 1,5 m/s respectivamente). Además, el comportamiento de
la velocidad del viento sigue un patrón similar tanto en el modelo de pronóstico como en
las observaciones, a pesar de que se observa una marcada falta de mediciones en durante
febrero. Dadas estas circunstancias y considerando la serie de tiempo de la velocidad del
viento, se puede afirmar que el modelo es adecuado.

Página 32 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Figura 9 . Rosa de viento 2019 datos observados (izquierda) y modelados (derecha) en la estacion Aerodromo La independencia,**

**Rancagua.**

**Fuente:** Ambiente Social, septiembre 2023.

Página 33 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Figura 10. Comparación serie de tiempo de temperatura, datos observados (arriba) y modelados (abajo).**

**Fuente:** Ambiente Social, septiembre 2023.

Página 34 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 11. Comparación serie de tiempo de dirección del viento, datos observados (arriba) y modelados**

**(abajo).**

**Fuente:** Ambiente Social, septiembre 2023.

Página 35 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 12. Comparación serie de tiempo de velocidad del viento, datos observados (arriba) y modelados**

**(abajo).**

**Fuente:** Ambiente Social, septiembre 2023.

Página 36 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Ciclos diarios**

La Figura 13 refleja que los ciclos diarios promedio de temperatura exhiben similitudes entre
los datos observados y los datos del modelo WRF. Además, la variación diaria de la
temperatura sigue un patrón similar tanto en el modelo de pronóstico como en las
observaciones. Considerando estas circunstancias, en cuanto al ciclo diario promedio de
temperatura, el modelo es apropiado.

En relación a la Figura 14, se deduce que los ciclos diarios de dirección del viento presentan
valores cercanos entre los datos observados y los datos WRF en la estación. Por lo tanto,
para la zona representada por la estación Aeródromo La Independencia, el modelo es
adecuado en cuanto a la dirección del viento.

La Figura 15 indica que los ciclos diarios promedio de velocidad del viento muestran
tendencias similares entre los datos observados y los datos del modelo WRF. Además, la
variación diaria de la velocidad sigue el mismo patrón tanto en el modelo de pronóstico
como en las observaciones. En relación al ciclo diario promedio de velocidad, el modelo es
adecuado. Sin embargo, es importante señalar que, al modelar velocidades más bajas, los
resultados pueden subestimar los valores reales esperados.

Es relevante mencionar que en los tres tipos de medidas (temperatura, velocidad de viento
y dirección del viento) se presenta una falta de datos observados, lo cual es posible de
observar en el gráfico de los promedios mensuales.

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 37 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Figura 13. Comparación ciclo diario de temperatura datos WRF y estación Aerodromo La Independencia, Rancagua.**

**Fuente:** Ambiente Social, septiembre 2023.

Página 38 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 14. Comparación ciclo diario de dirección del viento datos WRF y estación Aeródromo La Independencia, Rancagua.**

**Fuente:** Ambiente Social, septiembre 2023.

Página 39 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 15 . Comparación ciclo diario de velocidad del viento datos WRF y estación Aerodromo La Independencia, Rancagua.**

**Fuente:** Ambiente Social, septiembre 2023.

Página 40 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**5.1.1.4. Ciclos estacionales**

De la Figura 16 conjunta de los valores predichos por el modelo WRF y los datos medidos
por la estación Aeródromo La Independencia para la temperatura, se concluye una alta
correlación entre los patrones mensuales de temperatura mostrándose en ambos casos las
temperaturas mínimas durante las mañanas del mes de julio, mientras que los máximos se
registran durante diciembre entre las 14 y 16 horas coincidiendo las tendencias modeladas
y observadas.

En la Figura 17, se aprecia el comportamiento estacional de la dirección del viento,
comparando los valores previstos por el modelo WRF y los datos recolectados en la estación
Aeródromo La Independencia. La relación moderada entre los patrones mensuales de
dirección del viento revela que las direcciones predominantes en invierno se sitúan entre
140° y 160°, mientras que en verano, tanto datos observados como modelados indican
predominancia de direcciones entre 150° y 200°. Es relevante señalar que los meses de
febrero y enero presentan carencia significativa de registros observados, lo que afecta la
evaluación en la distribución del mapa de color en el gráfico, pero no a la representatividad

del modelo.

En la Figura 18, al examinar los ciclos estacionales de velocidad del viento, se evidencia una
concordancia entre los datos observados y los modelados. Ambos indican máximos en
enero-diciembre, aproximadamente entre las 15 y 17 horas. Durante el invierno, ambas
gráficas revelan una disminución en las velocidades del viento, destacando julio como el
mes con las velocidades más bajas a lo largo del día. Por tanto, se concluye que existe una
notable correlación entre los datos observados de velocidad del viento en la estación

Aeródromo La Independencia, a pesar de la carencia de datos observados durante el mes

de febrero.

Página 41 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Figura 16 . Ciclo estacional de temperatura datos observados (arriba) y modelados (abajo).**

**Fuente:** Ambiente Social, septiembre 2023.

Página 42 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 17. Ciclo estacional de dirección del viento datos observados (arriba) y modelados (abajo).**

**Fuente:** Ambiente Social, septiembre 2023.

Página 43 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 18 . Ciclo estacional de velocidad del viento datos observados (arriba) y modelados (abajo).**

**Fuente:** Ambiente Social, septiembre 2023.

Página 44 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**4.5.** **Análisis de incertidumbre**

El análisis de los registros de temperatura, dirección y velocidad de viento fue realizado
comparando los ciclos diarios, ciclos estacionales, gráficos de distribución y rosa de los
vientos. Además, se realizó un análisis numérico de los promedios diarios de acuerdo con
las recomendaciones de la guía EPA para el uso de modelos numéricos del tiempo en
Calpuff [20] .

La ecuación a continuación describe el cálculo de Bias Error, pero para más detalles sobre
el método de cálculo de incerteza, consultar el Apéndice n°3.

J

I

Bias Error (B) = [1]

i −O
j

i )

IJ [∑∑(P] [j]

Ecuación 1.

j=1

i=1

Donde,
P, corresponde al valor modelado
O, corresponde al valor observado

De los valores recomendados, el modelo WRF cumple con la velocidad del viento, como se
observa en la Tabla 15.

Con respecto a la temperatura, el estadístico diario muestra un valor mayor a lo
recomendado, confirmando una discrepancia entre los datos observados y los modelados,
lo cual se puede asociar a la falta de registros diarios en la estación Aeródromo la
Independencia, Rancagua, durante febrero y enero.

**Tabla 15. Análisis estadístico Estación Aeródromo La Independencia, Rancagua.**

|Parámetro|Variable Estadística|Diario|Recomendación|
|---|---|---|---|
|Velocidad|BIAS (m/s)|1,01|≤ 2 (m/s)|
|Dirección|BIAS (°)|26,68|≤ 30 (°)|
|Temperatura|BIAS (°C)<br>|5,32<br>|≤ 2 (°C)|

**Fuente:** Ambiente Social, septiembre 2023.

Para más detalles sobre la metodología empleada para el análisis de incertidumbres,
consular el Apéndice n°3.

20 _PRELIMINARY Draft Users Manual, The MMIFstat Statistical Analysis Package. Sección 2.2._

Página 45 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

# 5. Resultados

**5.1.** **Situación basal calidad del aire**

Con el fin de asegurar una interpretación precisa de los resultados modelados, se ha
efectuado un análisis de la línea base o situación basal de los contaminantes regulados. Este
análisis se basa en los datos recopilados de la estación de monitoreo de calidad del aire
Rancagua I, perteneciente a la red SINCA. Es relevante mencionar que esta estación
proporciona registros para MP2.5, MP10, SO 2 y CO.

A continuación, se presenta una descripción detallada de la validez de los datos
correspondientes a cada contaminante, según el año de muestreo.

Para más detalles, consultar el Apéndice n°5.

**Tabla 16 . Porcentaje de registros validos para cada contaminante en la estacion de**

**calidad del aire Rancagua I.**

|Contaminante|Parámetro|Año|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|**2022**|
|**MP2.5**|Registros validos|8461|8544|8513|8450|
|**MP2.5**|Registros totales|8760|8784|8760|8760|
|**MP2.5**|**% validos**|**97%**|**97%**|**97%**|**96%**|
|**MP10**|Registros validos|8497|8538|8455|8453|
|**MP10**|Registros totales|8760|8760|8760|8760|
|**MP10**|**% validos**|**97%**|**97%**|**97%**|**96%**|
|**CO**|Registros validos|8130|8178|8659|8621|
|**CO**|Registros totales|8760|8784|8760|8760|
|**CO**|**% validos**|**93%**|**93%**|**99%**|**98%**|
|**SO2**|Registros validos|8328|8608|8631|8607|
|**SO2**|Registros totales|8761|8784|8760|8760|
|**SO2**|**% validos**<br>|**95%**<br>|**98%**<br>|**99%**|**98%**|

**Fuente:** Ambiente Social, septiembre 2023

También se llevó a cabo una evaluación del cumplimiento de las normas de calidad primaria
para los registros trianuales de los contaminantes monitoreados por la estación. A partir de
este análisis se pudo determinar que se sobrepasan los límites para el promedio anual de
MP2.5, así como para el percentil 98 diario de este mismo contaminante, además del
promedio anual de MP10. La tabla siguiente proporciona un resumen del análisis de
cumplimiento correspondiente a los años 2020, 2021 y 2022.

Para obtener una comprensión más detallada sobre el procesamiento de datos, se
recomienda consultar los Apéndices n°5 y n°6.

**Tabla 17 . Situacion basal trianual.**

|Contaminant<br>e|Parámetro|Año|Col4|Col5|Col6|Superació<br>n|Cumplimient<br>o|
|---|---|---|---|---|---|---|---|
|**Contaminant**<br>**e **|**Parámetro**|**202**<br>**0 **|**202**<br>**1 **|**202**<br>**2 **|**Medi**<br>**a **|**Medi**<br>**a **|**Medi**<br>**a **|
||Promedio anual|22.0|25.1|23.5|23.5|20 [μg/m3]|No|

Página 46 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

|Contaminant<br>e<br>MP2.5<br>[μg/m3N]|Parámetro|Año|Col4|Col5|Col6|Superació<br>n|Cumplimient<br>o|
|---|---|---|---|---|---|---|---|
|**Contaminant**<br>**e **<br>**MP2.5**<br>**[μg/m3N]**|**Parámetro**|**202**<br>**0 **|**202**<br>**1 **|**202**<br>**2 **|**Medi**<br>**a **|**Medi**<br>**a **|**Medi**<br>**a **|
|**Contaminant**<br>**e **<br>**MP2.5**<br>**[μg/m3N]**|Percentil 98, diario|75.7|94.6|77.8|82.7|50 [μg/m3]|No|
|**MP10**<br>**[μg/m3N]**|Promedio anual|54.7|49.6|58.6|54.3|50 [μg/m3]|No|
|**MP10**<br>**[μg/m3N]**|Percentil 98, diario|109.7|122.1|132.0|121.3|130 [μg/m3]|Si|
|**MP10**<br>**[μg/m3N]**|N° días [MP10] > 130<br>[μg/m3]|3|6|5|5|7 días|Si|
|**CO ppm**|Percentil 99, 1 hora|2.5|2.5|2.0|2.3|26 ppm|Si|
|**CO ppm**|Percentil 99, 8 horas|2.3|2.2|1.6|2.0|9 ppm|Si|
|**SO2**<br>**[μg/m3N]**|Promedio anual|1.0|1.0|1.0|1.0|60 [μg/m3]|Si|
|**SO2**<br>**[μg/m3N]**|Percentil 99, diario|1.8|1.3|1.4|1.5|150 [μg/m3]|Si|
|**SO2**<br>**[μg/m3N]**|Percentil 98.5, 1 hora<br>|1.04<br>|1.01<br>|1.02<br>|1.04<br>|350 [μg/m3]|Si|

**Fuente:** Ambiente Social, septiembre 2023

Cabe señalar que la situación basal para MP2.5 y MP10 promedio anual, junto con MP2.5
percentil 98 diario, ya presenta un incumplimiento de la norma de calidad primaria.

**5.2.** **Concentraciones modeladas**

A continuación, se presentan los resultados de la pluma de dispersión e isoconcentraciónes
obtenida para material particulado y gases.

**5.2.1.Material Particulado**

Material Particulado Fino (MP2.5)

A partir de los resultados obtenidos de la modelación, es posible señalar que para ninguno
de los receptores discretos ocurre superación de la norma de calidad para MP2,5, ya sea
para el promedio anual o bien del percentil 98 diario.

Las Figura 19 y Figura 20 dan cuenta de la pluma de dispersión, y a su vez, la Tabla 18
detalla la concentración modelada para cada receptor discreto.

**Tabla 18 . Porcentaje de cumplimiento de limite D.S. N°12/2011 MMA.**

|Promedio anual|Col2|Col3|Col4|Percentil 98, diario|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Receptor|Valor<br>modelado<br>[μg/m3]|Norma<br>[μg/m3N]|% de<br>norma|Receptor|Valor<br>modelado<br>[μg/m3]|Norma<br>[μg/m3N]|% de<br>norma|
|Re1|1.00E-02|20<br>|0.05%|Re1|1.00E-01|50|0.20%|
|Re2|1.00E-02|1.00E-02|0.05%|Re2|1.00E-01|1.00E-01|0.20%|
|Re3|0.00E+00|0.00E+00|0.00%|Re3|0.00E+00|0.00E+00|0.00%|
|Re4|1.00E-01|1.00E-01|0.50%|Re4|1.00E+00|1.00E+00|2.00%|
|Re5|1.00E-01|1.00E-01|1.50%|Re5|1.20E+00|1.20E+00|4.00%|
|Re6|7.00E-02|7.00E-02|0.35%|Re6|5.00E-01|5.00E-01|1.00%|
|Re7|3.00E-02|3.00E-02|0.15%|Re7|4.00E-01|4.00E-01|0.80%|
|Re8|0.00E+00|0.00E+00|0.00%|Re8|0.00E+00|0.00E+00|0.00%|
|Re9|0.00E+00|0.00E+00|0.00%|Re9|0.00E+00|0.00E+00|0.00%|
|Re10|7.00E-02|7.00E-02|0.35%<br>|Re10<br>|6.00E-01<br>|6.00E-01<br>|1.20%|

**Fuente:** Ambiente Social, septiembre 2023

Página 47 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

Material Particulado Grueso (MP10)

A partir de los resultados obtenidos de la modelación, es posible señalar que para ninguno
de los receptores discretos ocurre superación de la norma de calidad para MP10, ya sea
para el promedio anual o bien del percentil 98 diario.

Las Figura 21 y Figura 22 dan cuenta de la pluma de dispersión, y a su vez, la Tabla 19
detalla la concentración modelada para cada receptor discreto.

**Tabla 19 . Porcentaje de cumplimiento de limite D.S. N°12/2021 MMA.**

|Promedio anual|Col2|Col3|Col4|Percentil 98, diario|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Receptor|Valor<br>modelado<br>[μg/m3]|Norma<br>[μg/m3N]|% de norma|Receptor|Valor<br>modelado<br>[μg/m3]|Norma<br>[μg/m3N]|% de<br>norma|
|Re1|6.00E-02|50|0.12%|Re1|3.00E-01|130|0.23%|
|Re2|6.00E-02|6.00E-02|0.12%|Re2|3.00E-01|3.00E-01|0.23%|
|Re3|6.00E-03|6.00E-03|0.01%|Re3|3.00E-02|3.00E-02|0.02%|
|Re4|6.00E-02|6.00E-02|0.12%|Re4|1.00E-01|1.00E-01|0.08%|
|Re5|8.00E-02|8.00E-02|0.20%|Re5|2.00E-01|2.00E-01|0.38%|
|Re6|1.00E-01|1.00E-01|0.20%|Re6|1.00E-01|1.00E-01|0.08%|
|Re7|2.00E-02|2.00E-02|0.04%|Re7|1.00E-01|1.00E-01|0.08%|
|Re8|0.00E+00|0.00E+00|0.00%|Re8|0.00E+00|0.00E+00|0.00%|
|Re9|0.00E+00|0.00E+00|0.00%|Re9|0.00E+00|0.00E+00|0.00%|
|Re10|0.00E+00|0.00E+00|0.00%|Re10|0.00E+00|0.00E+00|0.00%|

**Fuente:** Ambiente Social, septiembre 2023

Material Particulado sedimentable (MPS)

A partir de los resultados obtenidos de la modelación, es posible señalar que para ninguno
de los receptores discretos ocurre superación del límite definido por la Confederación suiza
para el MPS.

La Figura 23 da cuenta de la pluma de dispersión, y a su vez, la Tabla 20 detalla la
concentración modelada para cada receptor discreto.

Página 48 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Tabla 20 . Porcentaje de cumplimiento de limite para MPS (Confederación Suiza).**

|Concentración diaria|Col2|Col3|Col4|
|---|---|---|---|
|Receptor|Valor modelado<br>[μg/m3]|Norma [μg/m3N]*|% de norma|
|Re1|1.00E+01|1.25E+05<br>|0.01%|
|Re2|8.00E+00|8.00E+00|0.01%|
|Re3|1.51E+00|1.51E+00|0.00%|
|Re4|3.00E+01|3.00E+01|0.02%|
|Re5|1.00E+02|1.00E+02|0.08%|
|Re6|3.00E+01|3.00E+01|0.02%|
|Re7|1.00E+01|1.00E+01|0.01%|
|Re8|0.00E+00|0.00E+00|0.00%|
|Re9|0.00E+00|0.00E+00|0.00%|
|Re10|3.00E+01<br>|3.00E+01<br>|0.02%|
|*Considera una altura de receptor de 1.6m <br>|*Considera una altura de receptor de 1.6m <br>|*Considera una altura de receptor de 1.6m <br>|*Considera una altura de receptor de 1.6m <br>|

**Fuente:** Ambiente Social, septiembre 2023

Página 49 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Figura 19. MP2.5 [μg/m** **[3]** **] promedio anual.**

**Fuente:** Ambiente Social, septiembre 2023

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 50 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 20. MP2.5 [μg/m** **[3]** **] Percentil 98, 24 horas.**

**Fuente:** Ambiente Social, septiembre 2023.

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 51 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 21. MP10 [μg/m** **[3]** **] Promedio anual.**

**Fuente:** Ambiente Social, septiembre 2023

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 52 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 22. MP10 [μg/m** **[3]** **] Percentil 98, 24 horas.**

**Fuente:** Ambiente Social, septiembre 2023

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 53 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 23. MPS [μg/m** **[3]** **], Promedio, 24 horas.**

**Fuente:** Ambiente Social, septiembre 2023

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 54 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**5.2.2.Gases**

Monóxido de carbono (CO)

A partir de los resultados obtenidos de la modelación, es posible señalar que para ninguno
de los receptores discretos ocurre superación de la norma de calidad para CO para el
percentil 99, ya sea de 1 u 8 horas.

Las Figura 24 y Figura 25 dan cuenta de la pluma de dispersión, y a su vez, la Tabla 21
detalla la concentración modelada para cada receptor discreto.

**Tabla 21 .Porcentaje de cumplimiento de limite D.S. N°115/2002 MINSEGPRES.**

|Percentil 99, horario|Col2|Col3|Col4|Percentil 99, 8 horas|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Receptor|Valor<br>modelado<br>[mg/m3]|Norma<br>[mg/m3N]|% de<br>norma|Receptor|Valor<br>modelado<br>[mg/m3]|Norma<br>[mg/m3N]|% de<br>norma|
|Re1|9.00E-05|30|0.00%|Re1|2.00E-04|10|0.00%|
|Re2|5.66E-05|5.66E-05|0.00%|Re2|1.00E-04|1.00E-04|0.00%|
|Re3|0.00E+00|0.00E+00|0.00%|Re3|0.00E+00|0.00E+00|0.00%|
|Re4|5.00E-04|5.00E-04|0.00%|Re4|1.00E-03|1.00E-03|0.01%|
|Re5|1.00E-03|1.00E-03|0.00%|Re5|5.00E-03|5.00E-03|0.05%|
|Re6|3.00E-04|3.00E-04|0.00%|Re6|7.00E-04|7.00E-04|0.01%|
|Re7|1.00E-04|1.00E-04|0.00%|Re7|5.00E-04|5.00E-04|0.01%|
|Re8|0.00E+00|0.00E+00|0.00%|Re8|0.00E+00|0.00E+00|0.00%|
|Re9|0.00E+00|0.00E+00|0.00%|Re9|0.00E+00|0.00E+00|0.00%|
|Re10|1.00E-03|1.00E-03|0.00%|Re10|1.00E-03|1.00E-03|0.01%|

**Fuente:** Ambiente Social, septiembre 2023

Dióxido de Azufre (SO 2 )

A partir de los resultados obtenidos de la modelación, es posible señalar que para ninguno
de los receptores discretos ocurre superación de la norma de calidad para SO 2, ya sea para
el promedio anual o el Percentil 99 diario.

Las Figura 26, Figura 27 y Figura 28 dan cuenta de la pluma de dispersión, y a su vez, la
Tabla 22 detalla la concentración modelada para cada receptor discreto.

Dióxido de Nitrógeno (NO 2 )

A partir de los resultados obtenidos de la modelación, es posible señalar que para ninguno
de los receptores discretos ocurre superación de la norma de calidad para NO 2, ya sea para
el promedio anual o el Percentil 99 horario.

Las Figura 29 y Figura 30 dan cuenta de la pluma de dispersión, y a su vez, la Tabla 22 .
Porcentaje de cumplimiento de limite D.S. N°104/2018 MMA.

**Promedio anual** **Percentil 99, diario** **Percentil 98,5 horario**

Página 55 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

|Recep<br>tor|Valor<br>model<br>ado<br>[μg/m<br>3]|Norma<br>[μg/m<br>3N]|% de<br>norm<br>a|Recep<br>tor|Valor<br>model<br>ado<br>[μg/m<br>3]|Norma<br>[μg/m<br>3N]|% de<br>norm<br>a|Recep<br>tor|Valor<br>model<br>ado<br>[μg/m<br>3]|Norma<br>[μg/m<br>3N]|% de<br>norm<br>a|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Re1|1.00E-<br>04|60|0.000<br>%|Re1|1.00E-<br>03|150<br>|0.001<br>%|Re1|1.00E-<br>03|350|0.001<br>%|
|Re2|1.00E-<br>04|1.00E-<br>04|0.000<br>%|Re2|1.00E-<br>03|1.00E-<br>03|0.001<br>%|Re2|1.00E-<br>03|1.00E-<br>03|0.001<br>%|
|Re3|1.21E-<br>05|1.21E-<br>05|0.000<br>%|Re3|0.00E<br>+00|0.00E<br>+00|0.000<br>%|Re3|0.00E<br>+00|0.00E<br>+00|0.000<br>%|
|Re4|3.00E-<br>04|3.00E-<br>04|0.001<br>%|Re4|5.00E-<br>03|5.00E-<br>03|0.003<br>%|Re4|3.00E-<br>03|3.00E-<br>03|0.002<br>%|
|Re5|8.00E-<br>04|8.00E-<br>04|0.001<br>%|Re5|1.00E-<br>02|1.00E-<br>02|0.007<br>%|Re5|5.00E-<br>03|5.00E-<br>03|0.003<br>%|
|Re6|1.00E-<br>04|1.00E-<br>04|0.000<br>%|Re6|6.00E-<br>03|6.00E-<br>03|0.004<br>%|Re6|1.00E-<br>03|1.00E-<br>03|0.001<br>%|
|Re7|1.00E-<br>04|1.00E-<br>04|0.000<br>%|Re7|2.00E-<br>03|2.00E-<br>03|0.001<br>%|Re7|1.00E-<br>03|1.00E-<br>03|0.001<br>%|
|Re8|0.00E<br>+00|0.00E<br>+00|0.000<br>%|Re8|0.00E<br>+00|0.00E<br>+00|0.000<br>%|Re8|0.00E<br>+00|0.00E<br>+00|0.000<br>%|
|Re9|0.00E<br>+00|0.00E<br>+00|0.000<br>%|Re9|0.00E<br>+00|0.00E<br>+00|0.000<br>%|Re9|0.00E<br>+00|0.00E<br>+00|0.000<br>%|
|Re10|1.00E-<br>04|1.00E-<br>04|0.000<br>% <br>|Re10<br>|2.00E-<br>03<br>|2.00E-<br>03<br>|0.001<br>% <br>|Re10<br>|1.00E-<br>03|1.00E-<br>03|0.001<br>%|

**Fuente:** Ambiente Social, septiembre 2023

Tabla 23 detalla la concentración modelada para cada receptor discreto.

Página 56 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Tabla 22 . Porcentaje de cumplimiento de limite D.S. N°104/2018 MMA.**

|Promedio anual|Col2|Col3|Col4|Percentil 99, diario|Col6|Col7|Col8|Percentil 98,5 horario|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Receptor|Valor<br>modelado<br>[μg/m3]|Norma<br>[μg/m3N]|% de<br>norma|Receptor|Valor<br>modelado<br>[μg/m3]|Norma<br>[μg/m3N]|% de<br>norma|Receptor|Valor<br>modelado<br>[μg/m3]|Norma<br>[μg/m3N]|% de<br>norma|
|Re1|1.00E-04|60|0.000%|Re1|1.00E-03|150<br>|0.001%|Re1|1.00E-03|350|0.001%|
|Re2|1.00E-04|1.00E-04|0.000%|Re2|1.00E-03|1.00E-03|0.001%|Re2|1.00E-03|1.00E-03|0.001%|
|Re3|1.21E-05|1.21E-05|0.000%|Re3|0.00E+00|0.00E+00|0.000%|Re3|0.00E+00|0.00E+00|0.000%|
|Re4|3.00E-04|3.00E-04|0.001%|Re4|5.00E-03|5.00E-03|0.003%|Re4|3.00E-03|3.00E-03|0.002%|
|Re5|8.00E-04|8.00E-04|0.001%|Re5|1.00E-02|1.00E-02|0.007%|Re5|5.00E-03|5.00E-03|0.003%|
|Re6|1.00E-04|1.00E-04|0.000%|Re6|6.00E-03|6.00E-03|0.004%|Re6|1.00E-03|1.00E-03|0.001%|
|Re7|1.00E-04|1.00E-04|0.000%|Re7|2.00E-03|2.00E-03|0.001%|Re7|1.00E-03|1.00E-03|0.001%|
|Re8|0.00E+00|0.00E+00|0.000%|Re8|0.00E+00|0.00E+00|0.000%|Re8|0.00E+00|0.00E+00|0.000%|
|Re9|0.00E+00|0.00E+00|0.000%|Re9|0.00E+00|0.00E+00|0.000%|Re9|0.00E+00|0.00E+00|0.000%|
|Re10|1.00E-04|1.00E-04|0.000%|Re10<br>|2.00E-03<br>|2.00E-03<br>|0.001%<br>|Re10|1.00E-03|1.00E-03|0.001%|

**Fuente:** Ambiente Social, septiembre 2023

**Tabla 23 . Porcentaje de cumplimiento de limite D.S. N°114/2002 MINSGPRES.**

|Promedio anual|Col2|Col3|Col4|Percentil 99, horario|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Receptor|Valor modelado<br>[μg/m3]|Norma [μg/m3N]|% de norma|Receptor|Valor modelado<br>[μg/m3]|Norma [μg/m3N]|% de norma|
|Re1|3.00E-02|100|0.05%|Re1|2.83E-01|400|0.19%|
|Re2|1.16E-02|1.16E-02|0.02%|Re2|2.83E-01|2.83E-01|0.19%|
|Re3|0.00E+00|0.00E+00|0.00%|Re3|0.00E+00|0.00E+00|0.00%|
|Re4|3.00E-01|3.00E-01|0.50%|Re4|2.00E+00|2.00E+00|1.33%|
|Re5|8.00E-01|8.00E-01|1.33%|Re5|1.00E+01|1.00E+01|6.67%|
|Re6|1.00E-01|1.00E-01|0.17%|Re6|1.00E+00|1.00E+00|0.67%|
|Re7|1.00E-01|1.00E-01|0.17%|Re7|1.00E+00|1.00E+00|0.67%|
|Re8|0.00E+00|0.00E+00|0.00%|Re8|0.00E+00|0.00E+00|0.00%|
|Re9|0.00E+00|0.00E+00|0.00%|Re9|0.00E+00|0.00E+00|0.00%|
|Re10|1.00E-01|1.00E-01|0.17%<br>|Re10<br>|6.00E+00|6.00E+00|4.00%|

**Fuente:** Ambiente Social, septiembre 2023

Página 57 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 24. CO [μg/m3], Percentil 99, 1 hora**

**Fuente:** Ambiente Social, septiembre 2023

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 58 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 25 . CO [μg/m** **[3]** **] Percentil 99, 8 horas.**

**Fuente:** Ambiente Social, septiembre 2023

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 59 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 26 . SO2 [μg/m3], Promedio anual.**

**Fuente:** Ambiente Social, septiembre 2023

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 60 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 27. SO2 [μg/m3], Percentil 99, 24 horas.**

**Fuente:** Ambiente Social, septiembre 2023

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 61 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 28. SO2 [μg/m3], Percentil 98.5, 1 hora.**

**Fuente:** Ambiente Social, septiembre 2023

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 62 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 29. NO** **2** **[μg/m3], Promedio anual.**

**Fuente:** Ambiente Social, septiembre 2023

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 63 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Figura 30. NO** **2** **[μg/m3], Percentil 99, 1 hora**

**Fuente:** Ambiente Social, septiembre 2023

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 64 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**5.3.** **Evaluación discreta de los niveles de concentración**

A continuación, se exponen las tablas que muestran las concentraciones de contaminantes
calculadas para cada receptor de interés en relación a los contaminantes bajo estudio.
Además, se resalta el punto de máximo impacto (PMI) identificado en cada caso.

Estas tablas también contienen los aportes derivados de la situación basal, así como los
provenientes de otros proyectos con Resolución de Calificación Ambiental (RCA) favorable
en la comuna de Graneros. Estos proyectos en cuestión son Nueva Línea 2x220 kV
Candelaria - Nueva Tuniche y la Subestación (SE) Nueva Tuniche 220 kV [21], y Planta
Fotovoltaica Nan [22]

**5.3.1.Material Particulado**

Material Particulado Fino (MP2.5)

Basándonos en la información presentada en la Tabla 24 y Tabla 25, se puede concluir que
las concentraciones finales de MP2.5, tanto en su promedio anual como en el percentil 98
diario, exceden los límites establecidos para la norma de calidad primaria (D.S. n°12/2011
MMA) en cada uno de los receptores analizados, todo lo anterior al considerar el escenario
de situación basal, aportes de proyectos con RCA aprobada y las emisiones del proyecto en
evaluación. Es importante destacar que este escenario se debe en gran medida a las
condiciones basales de la región, ya que, previamente se ha declarado que la zona se
encuentra saturada para MP2.5 atmosférico (D.S. n°42/2017 MMA23).

**Tabla 24. MP2,5 [μg/m3] promedio anual.**

|Receptor|Valor<br>modelado<br>[μg/m3]|Línea<br>Base<br>[μg/m3N]|Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[μg/m3N]|Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S|Col8|
|---|---|---|---|---|---|---|---|
|Receptor|Valor<br>modelado<br>[μg/m3]|Línea<br>Base<br>[μg/m3N]|Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[μg/m3N]|Este|Norte|
|Re1|1,00E-02|23,5|0,3015|23,80|20|344633|6225424|
|Re2|1,00E-02|1,00E-02|1,00E-02|23,80|23,80|344253|6225476|
|Re3|0,00E+00|0,00E+00|0,00E+00|23,79|23,79|343363|6225175|
|Re4|1,00E-01|1,00E-01|1,00E-01|23,89|23,89|345012|6225246|
|Re5 - PMI|3,00E-01|3,00E-01|3,00E-01|24,09|24,09|344909|6224852|
|Re6|7,00E-02|7,00E-02|7,00E-02|23,86|23,86|344834|6224745|
|Re7|3,00E-02|3,00E-02|3,00E-02|23,82|23,82|344768|6224653|
|Re8|0,00E+00|0,00E+00|0,00E+00|23,79|23,79|338517|6224401|
|Re9|0,00E+00|0,00E+00|0,00E+00|23,79|23,79|339495|6221288|
|Re10|7,00E-02|7,00E-02|7,00E-02|23,86|23,86|342431|6219932|

**Fuente:** Ambiente Social, septiembre 2023

21 https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2149094292
22 https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2146015261
23 https://ppda.mma.gob.cl/wp-content/uploads/2023/03/DS-42_2017_DECLARA-ZONA-SATURADA-POR-MATERIALPARTICULADO-FINO-RESPIRABLE-MP25-COMO-CONCENTRACION-ANUAL-Y-DE-24-HORAS-AL-VALLE-CENTRAL-DE-LAREGION-DE-OHIGGINS.pdf

Página 65 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Tabla 25. MP2,5 [μg/m3] percentil 98, 24 horas.**

|Receptor|Valor<br>modelado<br>[μg/m3]|Línea<br>Base<br>[μg/m3N]|Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[μg/m3N]|Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S|Col8|
|---|---|---|---|---|---|---|---|
|Receptor|Valor<br>modelado<br>[μg/m3]|Línea<br>Base<br>[μg/m3N]|Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[μg/m3N]|Este|Norte|
|Re1|1,00E-01|77,8|1,5|79,40|50|344633|6225424|
|Re2|1,00E-01|1,00E-01|1,00E-01|79,40|79,40|344253|6225476|
|Re3|0,00E+00|0,00E+00|0,00E+00|79,30|79,30|343363|6225175|
|Re4|1,00E+00|1,00E+00|1,00E+00|80,30|80,30|345012|6225246|
|Re5 - PMI|2,00E+00|2,00E+00|2,00E+00|81,30|81,30|344909|6224852|
|Re6|5,00E-01|5,00E-01|5,00E-01|79,80|79,80|344834|6224745|
|Re7|4,00E-01|4,00E-01|4,00E-01|79,70|79,70|344768|6224653|
|Re8|0,00E+00|0,00E+00|0,00E+00|79,30|79,30|338517|6224401|
|Re9|0,00E+00|0,00E+00|0,00E+00|79,30|79,30|339495|6221288|
|Re10|6,00E-01|6,00E-01|6,00E-01|79,90|79,90|342431|6219932|

**Fuente:** Ambiente Social, septiembre 2023

Material Particulado Grueso (MP10)

Basándonos en la información presentada en la Tabla 26 y Tabla 27, se puede concluir que
las concentraciones finales de MP10, tanto en su promedio anual como en el percentil 98
diario, exceden los límites establecidos para la norma de calidad primaria (D.S. n°12/2021
MMA) en cada uno de los receptores analizados, todo lo anterior al considerar el escenario
de situación basal, aportes de proyectos con RCA aprobada y las emisiones del proyecto en
evaluación. Es importante destacar que este escenario se debe en gran medida a las
condiciones basales de la región, ya que previamente se ha declarado que la zona se
encuentra saturada para MP10 atmosférico (D.S. n°07/2009 MINSEGPRES [24] ).

**Tabla 26. MP10[μg/m3] promedio anual.**

|Receptor|Valor<br>modelado<br>[μg/m3]|Línea Base<br>[μg/m3N]|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[μg/m3N]|Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S|Col8|
|---|---|---|---|---|---|---|---|
|Receptor|Valor<br>modelado<br>[μg/m3]|Línea Base<br>[μg/m3N]|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[μg/m3N]|Este|Norte|
|Re1|0,06|58,60|0,45|59,1|50|344633|6225424|
|Re2|0,06|0,06|0,06|59,1|59,1|344253|6225476|
|Re3|0,01|0,01|0,01|59,1|59,1|343363|6225175|
|Re4|0,06|0,06|0,06|59,1|59,1|345012|6225246|
|Re5 - PMI|0,10|0,10|0,10|59,1|59,1|344909|6224852|
|Re6 - PMI|0,10|0,10|0,10|59,1|59,1|344834|6224745|
|Re7|0,02|0,02|0,02|59,1|59,1|344768|6224653|
|Re8|0,00|0,00|0,00|59,0|59,0|338517|6224401|
|Re9|0,00|0,00|0,00|59,0|59,0|339495|6221288|
|Re10|0,00|0,00|0,00|59,0|59,0|342431|6219932|

24 https://ppda.mma.gob.cl/wp-content/uploads/2023/03/DS-42_2017_DECLARA-ZONA-SATURADA-POR-MATERIALPARTICULADO-FINO-RESPIRABLE-MP25-COMO-CONCENTRACION-ANUAL-Y-DE-24-HORAS-AL-VALLE-CENTRAL-DE-LAREGION-DE-OHIGGINS.pdf

Página 66 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Fuente:** Ambiente Social, septiembre 2023

**Tabla 27. MP10[μg/m3] percentil 98, 24 horas.**

|Receptor|Valor<br>modelado<br>[μg/m3]|Línea Base<br>[μg/m3N]|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[μg/m3N]|Coordenadas<br>[+N18:U18m]<br>UTM WGS-84,<br>Huso 19S|Col8|
|---|---|---|---|---|---|---|---|
|Receptor|Valor<br>modelado<br>[μg/m3]|Línea Base<br>[μg/m3N]|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[μg/m3N]|Este|Norte|
|Re1|0,3|131,99|2,23|134,5|130|344633|6225424|
|Re2|0,3|0,3|0,3|134,5|134,5|344253|6225476|
|Re3|0,0|0,0|0,0|134,2|134,2|343363|6225175|
|Re4|0,1|0,1|0,1|134,3|134,3|345012|6225246|
|Re5 - PMI|0,5|0,5|0,5|134,7|134,7|344909|6224852|
|Re6|0,1|0,1|0,1|134,3|134,3|344834|6224745|
|Re7|0,1|0,1|0,1|134,3|134,3|344768|6224653|
|Re8|0,0|0,0|0,0|134,2|134,2|338517|6224401|
|Re9|0,0|0,0|0,0|134,2|134,2|339495|6221288|
|Re10|0,0|0,0|0,0|134,2|134,2|342431|6219932|

**Fuente:** Ambiente Social, septiembre 2023

Material Particulado sedimentable (MPS)

Siguiendo las pautas establecidas por la norma de referencia de la Confederación Suiza, se
puede concluir que el límite estipulado para la deposición seca de MPS no es superado. Al
normalizar dicho límite a la altura de un receptor promedio y, por consiguiente, al expresarlo
en términos de concentración, se observa que las concentraciones modeladas también se
mantienen por debajo de este límite.

**Tabla 28. Concentración diaria [μg/m3].**

|Receptor|Valor<br>modelado<br>[μg/ m3]|Línea Base<br>[μg/m 3N]|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final<br>[μg/m 3N]|*Norma<br>[μg/m 3N]|Coordenadas [m] UTM<br>WGS-84, Huso 19S|Col8|
|---|---|---|---|---|---|---|---|
|Receptor|Valor<br>modelado<br>[μg/m3]<br>|Línea Base<br>[μg/m3N]<br>|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final<br>[μg/m3N]<br>|*Norma<br>[μg/m3N]<br>|Este|Norte|
|Re1|10,0|Sin<br>registros|Sin<br>registros|10,0|1,25E+05|344633|6225424|
|Re2|8,0|8,0|8,0|8,0|8,0|344253|6225476|
|Re3|1,5|1,5|1,5|1,5|1,5|343363|6225175|
|Re4|30,0|30,0|30,0|30,0|30,0|345012|6225246|
|Re5 - PMI|100,0|100,0|100,0|100,0|100,0|344909|6224852|
|Re6|30,0|30,0|30,0|30,0|30,0|344834|6224745|
|Re7|10,0|10,0|10,0|10,0|10,0|344768|6224653|
|Re8|0,0|0,0|0,0|0,0|0,0|338517|6224401|
|Re9|0,0|0,0|0,0|0,0|0,0|339495|6221288|
|Re10|30,0|30,0|30,0|30,0|30,0|342431|6219932|
|* Altura de 1.6m|* Altura de 1.6m|* Altura de 1.6m|* Altura de 1.6m|* Altura de 1.6m|* Altura de 1.6m|* Altura de 1.6m|* Altura de 1.6m|

**5.3.2.Gases**

Monóxido de carbono (CO)

**Fuente:** Ambiente Social, septiembre 2023

Página 67 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

Basándonos en la información presentada en la Tabla 29 y Tabla 30, se puede concluir que
las concentraciones finales de CO para el Percentil 99, tanto en su medida de 1 hora como
la de 8 horas, no exceden los límites establecidos para la norma de calidad primaria (D.S.
n°115/2002 MINSEGPRES) en cada uno de los receptores analizados.

**Tabla 29. CO, Percentil 99, 1 hora.**

|Receptor|Valor<br>modelado<br>[μg/m3]|Línea Base<br>[μg/m3N]|Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[mg/m3N]|Coordenadas<br>[m] UTM WGS-<br>84, Huso 19S|Col8|
|---|---|---|---|---|---|---|---|
|Receptor|Valor<br>modelado<br>[μg/m3]|Línea Base<br>[μg/m3N]|Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[mg/m3N]|Este|Norte|
|Re1|0,09|1,97|22,57|24,63|30|344633|6E+06|
|Re2|0,06|0,06|0,06|24,60|24,60|344253|6E+06|
|Re3|0,00|0,00|0,00|24,54|24,54|343363|6E+06|
|Re4|0,50|0,50|0,50|25,04|25,04|345012|6E+06|
|Re5 - PMI|1,00|1,00|1,00|25,54|25,54|344909|6E+06|
|Re6|0,30|0,30|0,30|24,84|24,84|344834|6E+06|
|Re7|0,10|0,10|0,10|24,64|24,64|344768|6E+06|
|Re8|0,00|0,00|0,00|24,54|24,54|338517|6E+06|
|Re9|0,00|0,00|0,00|24,54|24,54|339495|6E+06|
|Re10 - PMI|1,00|1,00|1,00|25,54|25,54|342431|6E+06|

**Fuente:** Ambiente Social, septiembre 2023

**Tabla 30. CO, Percentil 99, 8 horas.**

|Receptor|Valor<br>modelado<br>[μg/m3]|Línea Base<br>[μg/m3N]|Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[mg/m3N]|Coordenadas<br>[m] UTM WGS-<br>84, Huso 19S|Col8|
|---|---|---|---|---|---|---|---|
|Receptor|Valor<br>modelado<br>[μg/m3]|Línea Base<br>[μg/m3N]|Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[mg/m3N]|Este|Norte|
|Re1|0,2|1,63|15,80|17,63|10|344633|6E+06|
|Re2|0,1|0,1|0,1|17,53|17,53|344253|6E+06|
|Re3|0|0|0|17,43|17,43|343363|6E+06|
|Re4|1|1|1|18,43|18,43|345012|6E+06|
|Re5 - PMI|5|5|5|22,43|22,43|344909|6E+06|
|Re6|0,7|0,7|0,7|18,13|18,13|344834|6E+06|
|Re7|0,5|0,5|0,5|17,93|17,93|344768|6E+06|
|Re8|0|0|0|17,43|17,43|338517|6E+06|
|Re9|0|0|0|17,43|17,43|339495|6E+06|
|Re10|1|1|1|18,43|18,43|342431|6E+06|

**Fuente:** Ambiente Social, septiembre 2023

Dióxido de Azufre (SO 2 )

Basándonos en la información presentada en la Tabla 31, Tabla 32 y Tabla 33, se puede
concluir que las concentraciones finales de SO 2, tanto en su promedio anual como en el
percentil 99 diario y percentil 98,5 horario, no exceden los límites establecidos para la norma
de calidad primaria (D.S. n°104/2018 MMA) en cada uno de los receptores analizados.

Página 68 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

**Tabla 31. SO** **2** **, Promedio anual.**

|Receptor|Valor<br>modelado<br>[μg/m3]|Línea Base<br>[μg/m3N]|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[μg/m3N]|Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S|Col8|
|---|---|---|---|---|---|---|---|
|||||||Este|Norte|
|Re1|1,0E-04|1,02|0,12|1,14|60|344633|6225424|
|Re2|1,0E-04|1,0E-04|1,0E-04|1,14|1,14|344253|6225476|
|Re3|1,2E-05|1,2E-05|1,2E-05|1,14|1,14|343363|6225175|
|Re4|3,0E-04|3,0E-04|3,0E-04|1,14|1,14|345012|6225246|
|Re5 - PMI|8,0E-04|8,0E-04|8,0E-04|1,14|1,14|344909|6224852|
|Re6|1,0E-04|1,0E-04|1,0E-04|1,14|1,14|344834|6224745|
|Re7|1,0E-04|1,0E-04|1,0E-04|1,14|1,14|344768|6224653|
|Re8|0,0E+00|0,0E+00|0,0E+00|1,14|1,14|338517|6224401|
|Re9|0,0E+00|0,0E+00|0,0E+00|1,14|1,14|339495|6221288|
|Re10|1,0E-04|1,0E-04|1,0E-04|1,14|1,14|342431|6219932|

**Fuente:** Ambiente Social, septiembre 2023

**Tabla 32. SO** **2** **, Percentil 99, 24 horas.**

|Receptor|Valor<br>modelado<br>[μg/m3]|Línea Base<br>[μg/m3N]|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[μg/m3N]|Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S|Col8|
|---|---|---|---|---|---|---|---|
|Receptor|Valor<br>modelado<br>[μg/m3]|Línea Base<br>[μg/m3N]|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]|Norma<br>[μg/m3N]|Este|Norte|
|Re1|1,0E-03|1,36|0,59|1,95|150|344633|6225424|
|Re2|1,0E-03|1,0E-03|1,0E-03|1,95|1,95|344253|6225476|
|Re3|0,0E+00|0,0E+00|0,0E+00|1,95|1,95|343363|6225175|
|Re4|5,0E-03|5,0E-03|5,0E-03|1,95|1,95|345012|6225246|
|Re5 - PMI|1,0E-02|1,0E-02|1,0E-02|1,96|1,96|344909|6224852|
|Re6|6,0E-03|6,0E-03|6,0E-03|1,95|1,95|344834|6224745|
|Re7|2,0E-03|2,0E-03|2,0E-03|1,95|1,95|344768|6224653|
|Re8|0,0E+00|0,0E+00|0,0E+00|1,95|1,95|338517|6224401|
|Re9|0,0E+00|0,0E+00|0,0E+00|1,95|1,95|339495|6221288|
|Re10|2,0E-03|2,0E-03|2,0E-03|1,95|1,95|342431|6219932|

**Fuente:** Ambiente Social, septiembre 2023

**Tabla 33. SO** **2** **, Percentil 98,5 - 1 hora.**

|Rece ptor|Valor<br>modelado<br>[μg/ m3]|Línea Base<br>[μg/m 3N]|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg /m3N]|Norma<br>[μg/m 3N]|Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S|Col8|
|---|---|---|---|---|---|---|---|
|Receptor<br>|Valor<br>modelado<br>[μg/m3]<br>|Línea Base<br>[μg/m3N]<br>|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]<br>|Norma<br>[μg/m3N]<br>|Este|Norte|
|Re1|1,0E-03|1,02|0,00|1,948|350|344633|6225424|
|Re2|1,0E-03|1,0E-03|1,0E-03|1,948|1,948|344253|6225476|
|Re3|0,0E+00|0,0E+00|0,0E+00|1,947|1,947|343363|6225175|
|Re4|3,0E-03|3,0E-03|3,0E-03|1,950|1,950|345012|6225246|
|Re5 - PMI|5,0E-03|5,0E-03|5,0E-03|1,952|1,952|344909|6224852|
|Re6|1,0E-03|1,0E-03|1,0E-03|1,948|1,948|344834|6224745|

Página 69 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

|Rece ptor|Valor<br>modelado<br>[μg/ m3]|Línea Base<br>[μg/m 3N]|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg /m3N]|Norma<br>[μg/m 3N]|Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S|Col8|
|---|---|---|---|---|---|---|---|
|Receptor<br>|Valor<br>modelado<br>[μg/m3]<br>|Línea Base<br>[μg/m3N]<br>|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]<br>|Norma<br>[μg/m3N]<br>|Este|Norte|
|Re7|1,0E-03|1,0E-03|1,0E-03|1,948|1,948|344768|6224653|
|Re8|0,0E+00|0,0E+00|0,0E+00|1,947|1,947|338517|6224401|
|Re9|0,0E+00|0,0E+00|0,0E+00|1,947|1,947|339495|6221288|
|Re10|1,0E-03|1,0E-03|1,0E-03|1,948|1,948|342431|6219932|

**Fuente:** Ambiente Social, agosto 2023

Dióxido de Nitrógeno (NO 2 )

Basándonos en la información presentada en la Tabla 34 y Tabla 35, se puede concluir que
las concentraciones finales de NO 2, tanto en su promedio anual como en el percentil 99 de
1 hora, no exceden los límites establecidos para la norma de calidad primaria (D.S.
n°114/2002 MINSEGPRES) en cada uno de los receptores analizados.

**Tabla 34. NO** **2** **, Promedio anual.**

|Rece ptor|Valor<br>modelado<br>[μg/ m3]|Línea Base<br>[μg/m 3N]|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg /m3N]|Norma<br>[μg/m 3N]|Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S|Col8|
|---|---|---|---|---|---|---|---|
|Receptor<br>|Valor<br>modelado<br>[μg/m3]<br>|Línea Base<br>[μg/m3N]<br>|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]<br>|Norma<br>[μg/m3N]<br>|Este|Norte|
|Re1|3E-02|Sin<br>registros|3,64|3,67|100|344633|6225424|
|Re2|1E-02|1E-02|1E-02|3,65|3,65|344253|6225476|
|Re3|0E+00|0E+00|0E+00|3,64|3,64|343363|6225175|
|Re4|3E-01|3E-01|3E-01|3,94|3,94|345012|6225246|
|Re5 - PMI|8E-01|8E-01|8E-01|4,44|4,44|344909|6224852|
|Re6|1E-01|1E-01|1E-01|3,74|3,74|344834|6224745|
|Re7|1E-01|1E-01|1E-01|3,74|3,74|344768|6224653|
|Re8|0E+00|0E+00|0E+00|3,64|3,64|338517|6224401|
|Re9|0E+00|0E+00|0E+00|3,64|3,64|339495|6221288|
|Re10|1E-01|1E-01|1E-01|3,74|3,74|342431|6219932|

**Fuente:** Ambiente Social, septiembre 2023

**Tabla 35. NO** **2** **, Percentil 99, 1 hora.**

|Rece ptor|Valor<br>modelado<br>[μg/ m3]|Línea Base<br>[μg/m 3N]|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg /m3N]|Norma<br>[μg/m 3N]|Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S|Col8|
|---|---|---|---|---|---|---|---|
|Receptor<br>|Valor<br>modelado<br>[μg/m3]<br>|Línea Base<br>[μg/m3N]<br>|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]<br>|Norma<br>[μg/m3N]<br>|Este|Norte|
|Re1|3E-01|Sin<br>registros|18,19|18,47|400|344633|6225424|
|Re2|3E-01|3E-01|3E-01|18,47|18,47|344253|6225476|
|Re3|0E+00|0E+00|0E+00|18,19|18,19|343363|6225175|
|Re4|2E+00|2E+00|2E+00|20,19|20,19|345012|6225246|
|Re5 - PMI|1E+01|1E+01|1E+01|28,19|28,19|344909|6224852|
|Re6|1E+00|1E+00|1E+00|19,19|19,19|344834|6224745|
|Re7|1E+00|1E+00|1E+00|19,19|19,19|344768|6224653|
|Re8|0E+00|0E+00|0E+00|18,19|18,19|338517|6224401|

Página 70 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

|Rece ptor|Valor<br>modelado<br>[μg/ m3]|Línea Base<br>[μg/m 3N]|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg /m3N]|Norma<br>[μg/m 3N]|Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S|Col8|
|---|---|---|---|---|---|---|---|
|Receptor<br>|Valor<br>modelado<br>[μg/m3]<br>|Línea Base<br>[μg/m3N]<br>|Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N]|Concentración<br>final [μg/m3N]<br>|Norma<br>[μg/m3N]<br>|Este|Norte|
|Re9|0E+00|0E+00|0E+00|18,19|18,19|339495|6221288|
|Re10|6E+00|6E+00|6E+00|24,19|24,19|342431|6219932|

**Fuente:** Ambiente Social, septiembre 2023

**5.4.** **Análisis de significancia**

De acuerdo a los resultados del presente estudio, se ha evidenciado que las emisiones
estimadas para el proyecto no superan los límites normativos establecidos para cada
receptor. Sin embargo, al considerar el escenario que abarca la situación basal y las
emisiones de proyectos con RCA favorable, se han excedido los límites en relación con las
partículas MP2.5 y MP10. Es fundamental resaltar que esta superación se debe al riesgo
preexistente en la zona y no implica necesariamente la generación de Efectos,
Características y Circunstancias (ECC) según lo establecido en el artículo 11, letra a), de la
Ley N°19.300.

Para evaluar de manera más precisa esta superación y determinar su significancia, se ha
realizado un análisis conforme a las pautas descritas en el estudio titulado "Evaluación de
la Significancia del Impacto de las Emisiones de un Proyecto o Actividad en Zonas Saturadas
en el Marco del SEIA". Este análisis ha empleado los Niveles de Impacto Significativo (SIL)
detallados en la tabla 0-8. Los resultados de esta evaluación revelan que el valor máximo
modelado se encuentra por debajo del incremento significativo, ver columna 6 de la Tabla

36.

Página 71 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Tabla 36. Análisis de significancia.**

|Contaminante|Periodo|Límite de<br>superación|Concentración<br>ambiental<br>2022<br>[μg/m3]|cumplimiento|Incremento<br>significativo<br>en la<br>concentración<br>[μg/m3]25|Valor<br>modelado<br>[μg/m3]26|Cumplimiento<br>bajo el<br>incremento<br>significativo|
|---|---|---|---|---|---|---|---|
|MP2,5|24 horas|50 [μg/m3]|77,8|No|1,7|0,105|si|
|MP2,5|anual|20 [μg/m3]|23,5|No|0,3|0,029|si|
|MP10|24 horas|130 [μg/m3]|132|No|5|1,040|si|
|MP10|anual|50 [μg/m3]|58,6|No|1|0,240|si|
|NO2|1 hora|400 [μg/m3]|Sin registros|Si|16|3,770|si|
|NO2|anual|100 [μg/m3]|Sin registros|Si|1|0,069|si|
|CO|1 hora|26 ppm|2,3 ppm|Si|1500,0|0,006|si|
|CO|anual|9 ppm|2,0 ppm|Si|488,9|0,014|si|
|SO2|24 horas|150 [μg/m3]|1,4|Si|2|0,008|si|
|SO2|anual|60 [μg/m3]|1,0|Si|1,2|0,001|si|

**Fuente:** Ambiente Social, septiembre 2023.

25 https://www.sea.gob.cl/sites/default/files/imce/archivos/2022/03/21/18fa27dd74-6bc2-4b96-9960-1ee4f178c967.pdf

26 Valor máximo de pluma de dispersión otorgado por el Modelo Calpuff View. Se aclara que este valor no corresponde a la concentración que

perciben los receptores.

Página 72 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**5.5.** **Área de influencia**

El Área de influencia para el componente Aire, se definió como aquella superficie que
representa el mayor valor porcentual de la norma de calidad primaria para MP10, de forma
tal que el área influencia corresponde a la pluma de dispersión del percentil 98 diario de
MP10, cuya superficie corresponde a 0,5 km [2] .

La siguiente figura informa el área de influencia del proyecto.

Página 73 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

**Figura 31 Área de influencia.**

**Fuente:** Ambiente Social, septiembre 2023

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Página 74 de 87

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

# 6. Conclusión

La presente evaluación ha profundizado en el análisis del impacto atmosférico ocasionado
por las emisiones de contaminantes derivadas del proyecto " Planta de tratamiento de aguas
servidas, sector la compañía - reingreso". Se ha enfocado en dos aspectos principales: la
extensión de la dispersión de diversos contaminantes y la fiabilidad de los datos modelados
en comparación con las observaciones reales.

En el primer enfoque, se ha llevado a cabo un análisis minucioso del entorno de modelación,
considerando factores como topografía, uso del suelo, tipos de receptores y estaciones
meteorológicas y de calidad del aire. Además, se ha definido el alcance del modelo
meteorológico (WRF) y se ha establecido el escenario de modelación, alineado con el
informe de estimación de emisiones atmosféricas. Esto ha incluido tasas y fuentes de
emisión.

En el segundo enfoque, se ha corroborado que el modelo meteorológico (WRF) se ajusta a
los datos observados de la estación meteorológica Aeródromo La Independencia en lo que
respecta a temperatura, velocidad y dirección del viento. Esta concordancia se ha
evidenciado en las rosas de viento, series de tiempo, ciclos diarios y estacionales. A pesar
de una falta de datos en la estación durante febrero 2019, esta validación ha sido sólida.

Adicionalmente, se ha evaluado la exposición de los receptores discretos a las
concentraciones de los contaminantes analizados, detallando el cumplimiento normativo
para cada uno. Asimismo, se ha estudiado el contexto normativo en un escenario que
contempla únicamente las emisiones proyectadas por el proyecto, y otro que además incluye
las reportadas en la situación basal a partir de la estación de calidad del aire (Rancagua I)
y las declaradas por otros proyectos con RCA favorable en los receptores.

En este contexto, se ha evidenciado que las emisiones estimadas para el proyecto no
superan los límites normativos establecidos para cada receptor. Sin embargo, al considerar
el escenario que abarca la situación basal y las emisiones de proyectos con RCA favorable,
se han excedido los límites en relación con las partículas MP2.5 y MP10. Es fundamental
resaltar que esta superación se debe al riesgo preexistente en la zona y no implica
necesariamente la generación de Efectos, Características y Circunstancias (ECC) según lo
establecido en el artículo 11, letra a), de la Ley N°19.300.

Para evaluar de manera más precisa esta superación y determinar su significancia, se ha
realizado un análisis conforme a las pautas descritas en el estudio titulado "Evaluación de
la Significancia del Impacto de las Emisiones de un Proyecto o Actividad en Zonas Saturadas
en el Marco del SEIA". Este análisis ha empleado los Niveles de Impacto Significativo (SIL)
detallados en la tabla 0-8. Los resultados de esta evaluación revelan que el valor máximo
modelado se encuentra por debajo del incremento significativo.

Página 75 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector La Compañía” .

# 7. Bibliografía

SEA (Sistema de Evaluación Ambiental) (2023), “Guía para el uso de modelos de Calidad del
Aire en el SEIA”, Ministerio del Medio Ambiente de Chile.

Evaluación significancia del impacto de las emisiones de un proyecto o actividad en zonas
saturadas en el marco del SEIA.

Página 76 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

# 8. Anexo

**Apéndice n°1:** Archivos de modelo generados por Calpuff

**Apéndice n°2:** Planilla Tasa de emisiones modeladas

**Apéndice n°3:** Procesamiento de datos para la validación del modelo meteorológico

**Apéndice n°4:** Validación estación meteorológica

**Apéndice n°5:** Situación basal estación Rancagua I

**Apéndice n°6:** Evaluación discreta de los niveles de concentración.

**Apéndice n°7:** KMZ plumas de dispersión

Página 77 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

Estudio de Modelación de Emisiones Atmosféricas
Proyecto “Planta de tratamiento de aguas servidas, sector la compañía”

Informe elaborado por

Raquel Tamara Saavedra Pino

Química Ambiental

# Ambiente Social, Asesoría y Consultoría Ambiental contacto@ambientesocial.cl www.ambientesocial.cl

Página 78 de 87

**Asesoría y Consultoría Ambiente-Social**
Sucursal Virtual: Barros Arana 492. Of 78, Concepción.

contacto@ambientesocial.cl - www.ambientesocial.cl

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Norma primaria de calidad ambiental para material particulado fino respirable****

| Limite (Articulo n°3) | Col2 | Norma8 |
| --- | --- | --- |
| **Promedio anual** | 20 (μg/m3) | D.S. N°12/2011<br>Ministerio del medio<br>Ambiente |
| **Percentil 98, diario** | 50 (μg/m3) | 50 (μg/m3) |
| **Situaciones de emergencia (Articulo n°5)**<br>**Concentración 24 horas.** | **Situaciones de emergencia (Articulo n°5)**<br>**Concentración 24 horas.** | **Situaciones de emergencia (Articulo n°5)**<br>**Concentración 24 horas.** |
| **Alerta** | 80-109 (μg/m3) | 80-109 (μg/m3) |
| **Preemergencia** | 110-169 (μg/m3) | 110-169 (μg/m3) |
| **Emergencia** | >170 (μg/m3) | >170 (μg/m3) |

**Tabla 2.: Norma primaria de calidad ambiental para material particulado respirable****

| Limite (Articulo n°3) | Col2 | Norma9 |
| --- | --- | --- |
| **Promedio anual** | 50 (μg/m3) | D.S. N°12/2021 Ministerio del<br>medio Ambiente |
| **Percentil 98, diario** | 130 (μg/m3) | 130 (μg/m3) |
| **Situaciones de emergencia (Articulo n°5)**<br>**Concentración 24 horas.** | **Situaciones de emergencia (Articulo n°5)**<br>**Concentración 24 horas.** | **Situaciones de emergencia (Articulo n°5)**<br>**Concentración 24 horas.** |
| **Alerta** | 180-229 (μg/m3) | 180-229 (μg/m3) |
| **Preemergencia** | 230-329 (μg/m3) | 230-329 (μg/m3) |
| **Emergencia** | >330 (μg/m3) | >330 (μg/m3) |

**Tabla 3.: Valores limites ambientales para Material Particula Suspendido (MPS).****

| Parámetro | Limite | Norma11 |
| --- | --- | --- |
| **Deposición seca** | 200 (mg/m2x día) | Ordinance on Air Pollution<br>Control (OAPC)<br>The Swiss Federal Council.<br>(814.318.142.1) |

**Tabla 4.: Norma primaria de calidad de aire para Monóxido de Carbono (CO).****

| Limite (Artículos n°3 y n°4) | Col2 | Norma12 |
| --- | --- | --- |
| **Percentil 99, horario** | 26 ppmv; 30 (mg/m3N) | D.S. N°115/2002<br>MINSEGRPRES |
| **Percentil 99, 8 horas** | 9 ppmv; 10 (mg/m3N) | 9 ppmv; 10 (mg/m3N) |
| **Situaciones de emergencia (Artículos n°3 y n°4)**<br>**Concentración Percentil 99, 8 horas** | **Situaciones de emergencia (Artículos n°3 y n°4)**<br>**Concentración Percentil 99, 8 horas** | **Situaciones de emergencia (Artículos n°3 y n°4)**<br>**Concentración Percentil 99, 8 horas** |
| **Nivel I** | 15 - 29 ppmv; 17 - 33 (mg/m3N) | 15 - 29 ppmv; 17 - 33 (mg/m3N) |
| **Nivel II** | 30 - 34 ppmv; 34 - 39 (mg/m3N) | 30 - 34 ppmv; 34 - 39 (mg/m3N) |
| **Nivel III** | >35 ppmv; >40 (mg/m3N) | >35 ppmv; >40 (mg/m3N) |

**Tabla 5.: Norma primaria de calidad de aire para dióxido de azufre (SO2).****

| Limite (Artículos n°3, n°4 y n°5) | Col2 | Norma |
| --- | --- | --- |
| **Promedio Anual** | 23 ppbv; 60 (μg/m3N) | D.S. N°104/2018<br>Ministerio del medio<br>Ambiente |
| **Percentil 99, diario** | 57 ppbv; 150 (μg/m3N) | 57 ppbv; 150 (μg/m3N) |
| **Concentración de 1 hora** | 134 ppbv; 250 (μg/m3N) | 134 ppbv; 250 (μg/m3N) |
| **Situaciones de emergencia (Artículo n°8)** | **Situaciones de emergencia (Artículo n°8)** | **Situaciones de emergencia (Artículo n°8)** |
| **Alerta** | 500 - 649 (μg/m3N) | 500 - 649 (μg/m3N) |
| **Preemergencia** | 650 - 949 (μg/m3N) | 650 - 949 (μg/m3N) |
| **Emergencia** | > 950 (μg/m3N) | > 950 (μg/m3N) |

**Tabla 6.: Norma primaria de calidad de aire para Dióxido de Nitrógeno (NO** **2** **).****

| Limite (Artículos n°3 y N°4) | Col2 | Norma |
| --- | --- | --- |
| **Promedio Anual** | 53 ppbv; 100 (μg/m3N) | D.S. N°114/2002<br>MINSEGRPRES |
| **Percentil 99, horario**<br> | 213 ppbv; 400 (μg/m3N)<br> | 213 ppbv; 400 (μg/m3N)<br> |
| **Situaciones de emergencia (Articulo n°5)** | **Situaciones de emergencia (Articulo n°5)** | **Situaciones de emergencia (Articulo n°5)** |
| **Nivel 1** | 601 - 1201 ppbv | 601 - 1201 ppbv |
| **Nivel 2** | 1202 - 1595 ppbv | 1202 - 1595 ppbv |
| **Nivel 3** | >1596 ppbv | >1596 ppbv |

**Tabla 7.: Características del dominio meteorológico WRF.****

| Datos | Col2 | Archivo meteorológico |
| --- | --- | --- |
| Dimensión grilla | Dimensión grilla | 50 [km] x 50 [km] |
| Espaciado grilla | Espaciado grilla | 1 [km] |
| Fe/hora inicio - Fecha/Hora fin | Fe/hora inicio - Fecha/Hora fin | 01/01/2019 00:00 - 01/01/2020 20:00 |
| Coordenada SO | Este [m] | 312.407,24 |
| Coordenada SO | Norte [m] | 6.193.204,60 |
| Coordenada SE | Este [m] | 362.513,63 |
| Coordenada SE | Norte [m] | 6.194.078,25 |
| Coordenada NO | Este [m] | 311.543,16 |
| Coordenada NO | Norte [m] | 6.243.085,60 |
| Coordenada NE | Este [m] | 361.648,86 |
| Coordenada NE | Norte [m] | 6.243.949,16 |

**Tabla 8: . Uso de suelo en el domominio de modelacion.****

| Agrupación | Descripción (MAKEGEO Land Use model) |
| --- | --- |
| Urbano | Residential; Commercial Services; Industrial; Transportation,<br>Communications; Industrial and Commercial; Mixed Urban or Built-Up Land;<br>Other Urban or Built-Up Land |
| Agricola | Cropland and Pasture; Orchards, Groves, Vineyards, Nurseries; Confined<br>Feeding Operations; Other Agricultural Land |
| Pastizal | Herbaceous Rangeland; Shrub and Brush Rangeland; Mixed Rangeland |
| Bosque | Deciduous Forest Land; Evergreen Forest Land; Mixed Forest Land |
| Terrenos Baldíos<br>mixtos | Dry Salt Flats; Beaches; Sandy Areas Other than Beaches; Bare Exposed<br>Rock; Strip Mines, Quarries, and Gravel Pits; Transitional Areas; Mixed<br>Barren Land |

**Tabla 9: . Características de receptores discretos.****

| Receptor | Distancia<br>al<br>perímetro<br>de la<br>planta<br>(km) | Altura<br>(m.s.n.m) | Coordenadas<br>[m] UTM WGS-<br>84, Huso 19S | Col5 | Descripción |
| --- | --- | --- | --- | --- | --- |
| **Receptor** | **Distancia**<br>**al**<br>**perímetro**<br>**de la**<br>**planta**<br>**(km)** | **Altura**<br>**(m.s.n.m)** | **Este** | **Norte** | **Norte** |
| Re1 | 0,15 | 487 | 344633 | 6225424 | Centro De Restauración Y<br>Rehabilitación Casa Betel |
| Re2 | 0,33 | 485 | 344253 | 6225476 | Vivienda |
| Re3 | 1,10 | 480 | 343363 | 6225175 | Fundo El Parronal, Camino Sta.<br>Margarita |
| Re4 | 0,38 | 489 | 345012 | 6225246 | Vivienda |
| Re5 | 0,45 | 487 | 344909 | 6224852 | Vivienda |
| Re6 | 0,48 | 486 | 344834 | 6224745 | Vivienda |
| Re7 | 0,53 | 487 | 344768 | 6224653 | Vivienda |
| Re8 | 6,01 | 462 | 338517 | 6224401 | Escuela de Tuniche |
| Re9 | 6,33 | 472 | 339495 | 6221288 | CESFAM N°8 Dr. Nicolás Díaz |
| Re10 | 5.620 | 498 | 342431 | 6219932 | CESFAM N°6 Ignacio Caroca |

**Tabla 10: . Estacion metereologica y de calidad del aire.****

| Estación | Distancia desde<br>Proyecto (km) | Latitud E | Longitud S |
| --- | --- | --- | --- |
| **Estación** | **Distancia desde**<br>**Proyecto (km)** | **UTM Huso 19S [m]** | **UTM Huso 19S [m]** |
| Aeródromo La Independencia**15** | 10,78 | 336.861,02 | 6.217.578,94 |
| Rancagua I16 | 5,66 | 342.014,62 | 6.220.035,35 |

**Tabla 11.: Emisiones estimadas para el año modelado.****

| Fase | MP10 | MP2.5 | MPS | NOX | SO<br>2 | NH<br>3 | CO | COV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Construcción | 0.538 | 0.147 | 1.508 | 0.325 | 0.006 | 0.000 | 0.156 | 0.025 |
| Operación | 0.465 | 0.053 | 1.387 | 0.044 | 0.002 | 0.000 | 0.009 | 0.003 |
| **Total** | **1.003** | **0.200** | **2.895** | **0.369** | **0.008** | **0.000** | **0.165** | **0.028** |

**Tabla 12.: Agrupación de actividad emisora para cada fuete de emisión.****

| Actividad emisora | Construcción | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Operación | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad emisora** | **EXC** | **MT** | **AC** | **GE-**<br>**CO1** | **GE-**<br>**CO2** | **RI** | **HAP5G**<br>**-N** | **HAP5G**<br>**-S** | **RI** | **HAP5G**<br>**-N** | **HAP5G**<br>**-S** | **GE-OP** |
| Escarpe | NA | AP | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| Excavaciones | AP | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| Erosión Material en Pila | NA | NA | AP | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| Carguío y volteo de material | NA | NA | AP | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| Compactación | NA | AP | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| Nivelación | NA | AP | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| Tránsito de vehículos caminos<br>no pavimentados. | NA | NA | NA | NA | NA | AP | NA | NA | AP | NA | NA | NA |
| Tránsito de vehículos caminos<br>pavimentados. | NA | NA | NA | NA | NA | NA | AP | AP | NA | AP | AP | NA |
| Combustión de vehículos en<br>ruta | NA | NA | NA | NA | NA | AP | AP | AP | AP | AP | AP | NA |
| Combustión de vehículos<br>fuera de ruta | AP | AP | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| Combustión grupo<br>electrógeno | NA | NA | NA | AP | AP | NA | NA | NA | NA | NA | NA | AP |
| AP: Aplica;<br>NA: No Aplica | AP: Aplica;<br>NA: No Aplica | AP: Aplica;<br>NA: No Aplica | AP: Aplica;<br>NA: No Aplica | AP: Aplica;<br>NA: No Aplica | AP: Aplica;<br>NA: No Aplica | AP: Aplica;<br>NA: No Aplica | AP: Aplica;<br>NA: No Aplica | AP: Aplica;<br>NA: No Aplica | AP: Aplica;<br>NA: No Aplica | AP: Aplica;<br>NA: No Aplica | AP: Aplica;<br>NA: No Aplica | AP: Aplica;<br>NA: No Aplica |

**Tabla 13.: Tasa de emision ingresadas a Calpuff.****

| Fuente<br>de<br>emisión | Unidad | Construcción | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente**<br>**de**<br>**emisión** | **Unidad** | **MP10 ** | **MP25 ** | **MPS** | **NOX ** | **SOX ** | **NH3 ** | **CO** | **COV** |
| EXC | g/s*m2 | 2E-06 | 5E-07 | 4E-06 | 2E-07 | 5E-10 | 1E-10 | 2E-07 | 2E-08 |
| MT | g/s*m2 | 9E-08 | 3E-08 | 2E-07 | 2E-07 | 5E-10 | 1E-10 | 2E-07 | 2E-08 |
| AC | g/s*m2 | 9E-08 | 1E-08 | 7E-07 | 0E+00 | 0E+00 | 0E+00 | 0E+00 | 0E+00 |
| GE-CO1 | g/s | 4E-05 | 4E-05 | 4E-05 | 5E-04 | 3E-05 | 0E+00 | 1E-04 | 4E-05 |
| GE-CO2 | g/s | 4E-05 | 4E-05 | 4E-05 | 5E-04 | 3E-05 | 0E+00 | 1E-04 | 4E-05 |
| RI | g/s*m | 5E-07 | 5E-08 | 5E-07 | 2E-08 | 2E-11 | 1E-11 | 4E-09 | 8E-10 |
| H15G-N | g/s*m | 5E-08 | 1E-08 | 2E-07 | 4E-08 | 4E-11 | 3E-11 | 8E-09 | 1E-09 |
| H15G-S | g/s*m | 3E-08 | 6E-05 | 1E-03<br> | 2E-04<br> | 2E-07 | 1E-07 | 4E-05 | 7E-06 |
|  |  |  |  |  |  |  |  |  |  |
| **Fuente**<br>**de**<br>**emisión** | **Unidad** | **Operación** | **Operación** | **Operación** | **Operación** | **Operación** | **Operación** | **Operación** | **Operación** |
| **Fuente**<br>**de**<br>**emisión** | **Unidad** | **MP10 ** | **MP25 ** | **MPS** | **NOX ** | **SOX ** | **NH3 ** | **CO** | **COV** |
| RI | g/s*m | 3E-06 | 3E-07 | 8E-06 | 3E-09 | 4E-12 | 4E-12 | 6E-10 | 1E-10 |
| H15G-N | g/s*m | 1E-08 | 3E-09 | 5E-08 | 3E-09 | 4E-12 | 4E-12 | 7E-10 | 1E-10 |
| H15G-S | g/s*m | 4E-09 | 1E-09 | 2E-08 | 1E-09 | 2E-12 | 2E-12 | 3E-10 | 5E-11 |
| GE-OP | g/s | 1E-05 | 1E-05 | 1E-05 | 1E-04 | 9E-06 | 0E+00 | 3E-05 | 1E-05 |

**Tabla 14: . Estación meteorológica Aeródromo La Independencia, Rancagua.****

| Parámetro | Col2 | Col3 |
| --- | --- | --- |
| Coordenada UTM, Huso 19S,<br>Datum WGS84 | Este [m] | 336.861,00 |
| Coordenada UTM, Huso 19S,<br>Datum WGS84 | Norte [m] | 6.217.578,90 |
| Distancia desde el proyecto [km] | Distancia desde el proyecto [km] | 22,2 |
| Periodo de registro | Periodo de registro | 1/1/2019 1:00:00 AM - 1/1/2020 0:00:00 AM |
| Variables meteorológicas | Variables meteorológicas | Temperatura, velocidad y dirección del viento |

**Tabla 15.: Análisis estadístico Estación Aeródromo La Independencia, Rancagua.****

| Parámetro | Variable Estadística | Diario | Recomendación |
| --- | --- | --- | --- |
| Velocidad | BIAS (m/s) | 1,01 | ≤ 2 (m/s) |
| Dirección | BIAS (°) | 26,68 | ≤ 30 (°) |
| Temperatura | BIAS (°C)<br> | 5,32<br> | ≤ 2 (°C) |

**Tabla 16: . Porcentaje de registros validos para cada contaminante en la estacion de****

| Contaminante | Parámetro | Año | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** | **2022** |
| **MP2.5** | Registros validos | 8461 | 8544 | 8513 | 8450 |
| **MP2.5** | Registros totales | 8760 | 8784 | 8760 | 8760 |
| **MP2.5** | **% validos** | **97%** | **97%** | **97%** | **96%** |
| **MP10** | Registros validos | 8497 | 8538 | 8455 | 8453 |
| **MP10** | Registros totales | 8760 | 8760 | 8760 | 8760 |
| **MP10** | **% validos** | **97%** | **97%** | **97%** | **96%** |
| **CO** | Registros validos | 8130 | 8178 | 8659 | 8621 |
| **CO** | Registros totales | 8760 | 8784 | 8760 | 8760 |
| **CO** | **% validos** | **93%** | **93%** | **99%** | **98%** |
| **SO2** | Registros validos | 8328 | 8608 | 8631 | 8607 |
| **SO2** | Registros totales | 8761 | 8784 | 8760 | 8760 |
| **SO2** | **% validos**<br> | **95%**<br> | **98%**<br> | **99%** | **98%** |

**Tabla 17: . Situacion basal trianual.****

| Contaminant<br>e | Parámetro | Año | Col4 | Col5 | Col6 | Superació<br>n | Cumplimient<br>o |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminant**<br>**e ** | **Parámetro** | **202**<br>**0 ** | **202**<br>**1 ** | **202**<br>**2 ** | **Medi**<br>**a ** | **Medi**<br>**a ** | **Medi**<br>**a ** |
|  | Promedio anual | 22.0 | 25.1 | 23.5 | 23.5 | 20 [μg/m3] | No |

**Tabla 18: . Porcentaje de cumplimiento de limite D.S. N°12/2011 MMA.****

| Promedio anual | Col2 | Col3 | Col4 | Percentil 98, diario | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Valor<br>modelado<br>[μg/m3] | Norma<br>[μg/m3N] | % de<br>norma | Receptor | Valor<br>modelado<br>[μg/m3] | Norma<br>[μg/m3N] | % de<br>norma |
| Re1 | 1.00E-02 | 20<br> | 0.05% | Re1 | 1.00E-01 | 50 | 0.20% |
| Re2 | 1.00E-02 | 1.00E-02 | 0.05% | Re2 | 1.00E-01 | 1.00E-01 | 0.20% |
| Re3 | 0.00E+00 | 0.00E+00 | 0.00% | Re3 | 0.00E+00 | 0.00E+00 | 0.00% |
| Re4 | 1.00E-01 | 1.00E-01 | 0.50% | Re4 | 1.00E+00 | 1.00E+00 | 2.00% |
| Re5 | 1.00E-01 | 1.00E-01 | 1.50% | Re5 | 1.20E+00 | 1.20E+00 | 4.00% |
| Re6 | 7.00E-02 | 7.00E-02 | 0.35% | Re6 | 5.00E-01 | 5.00E-01 | 1.00% |
| Re7 | 3.00E-02 | 3.00E-02 | 0.15% | Re7 | 4.00E-01 | 4.00E-01 | 0.80% |
| Re8 | 0.00E+00 | 0.00E+00 | 0.00% | Re8 | 0.00E+00 | 0.00E+00 | 0.00% |
| Re9 | 0.00E+00 | 0.00E+00 | 0.00% | Re9 | 0.00E+00 | 0.00E+00 | 0.00% |
| Re10 | 7.00E-02 | 7.00E-02 | 0.35%<br> | Re10<br> | 6.00E-01<br> | 6.00E-01<br> | 1.20% |

**Tabla 19: . Porcentaje de cumplimiento de limite D.S. N°12/2021 MMA.****

| Promedio anual | Col2 | Col3 | Col4 | Percentil 98, diario | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Valor<br>modelado<br>[μg/m3] | Norma<br>[μg/m3N] | % de norma | Receptor | Valor<br>modelado<br>[μg/m3] | Norma<br>[μg/m3N] | % de<br>norma |
| Re1 | 6.00E-02 | 50 | 0.12% | Re1 | 3.00E-01 | 130 | 0.23% |
| Re2 | 6.00E-02 | 6.00E-02 | 0.12% | Re2 | 3.00E-01 | 3.00E-01 | 0.23% |
| Re3 | 6.00E-03 | 6.00E-03 | 0.01% | Re3 | 3.00E-02 | 3.00E-02 | 0.02% |
| Re4 | 6.00E-02 | 6.00E-02 | 0.12% | Re4 | 1.00E-01 | 1.00E-01 | 0.08% |
| Re5 | 8.00E-02 | 8.00E-02 | 0.20% | Re5 | 2.00E-01 | 2.00E-01 | 0.38% |
| Re6 | 1.00E-01 | 1.00E-01 | 0.20% | Re6 | 1.00E-01 | 1.00E-01 | 0.08% |
| Re7 | 2.00E-02 | 2.00E-02 | 0.04% | Re7 | 1.00E-01 | 1.00E-01 | 0.08% |
| Re8 | 0.00E+00 | 0.00E+00 | 0.00% | Re8 | 0.00E+00 | 0.00E+00 | 0.00% |
| Re9 | 0.00E+00 | 0.00E+00 | 0.00% | Re9 | 0.00E+00 | 0.00E+00 | 0.00% |
| Re10 | 0.00E+00 | 0.00E+00 | 0.00% | Re10 | 0.00E+00 | 0.00E+00 | 0.00% |

**Tabla 20: . Porcentaje de cumplimiento de limite para MPS (Confederación Suiza).****

| Concentración diaria | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| Receptor | Valor modelado<br>[μg/m3] | Norma [μg/m3N]* | % de norma |
| Re1 | 1.00E+01 | 1.25E+05<br> | 0.01% |
| Re2 | 8.00E+00 | 8.00E+00 | 0.01% |
| Re3 | 1.51E+00 | 1.51E+00 | 0.00% |
| Re4 | 3.00E+01 | 3.00E+01 | 0.02% |
| Re5 | 1.00E+02 | 1.00E+02 | 0.08% |
| Re6 | 3.00E+01 | 3.00E+01 | 0.02% |
| Re7 | 1.00E+01 | 1.00E+01 | 0.01% |
| Re8 | 0.00E+00 | 0.00E+00 | 0.00% |
| Re9 | 0.00E+00 | 0.00E+00 | 0.00% |
| Re10 | 3.00E+01<br> | 3.00E+01<br> | 0.02% |
| *Considera una altura de receptor de 1.6m <br> | *Considera una altura de receptor de 1.6m <br> | *Considera una altura de receptor de 1.6m <br> | *Considera una altura de receptor de 1.6m <br> |

**Tabla 21: .Porcentaje de cumplimiento de limite D.S. N°115/2002 MINSEGPRES.****

| Percentil 99, horario | Col2 | Col3 | Col4 | Percentil 99, 8 horas | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Valor<br>modelado<br>[mg/m3] | Norma<br>[mg/m3N] | % de<br>norma | Receptor | Valor<br>modelado<br>[mg/m3] | Norma<br>[mg/m3N] | % de<br>norma |
| Re1 | 9.00E-05 | 30 | 0.00% | Re1 | 2.00E-04 | 10 | 0.00% |
| Re2 | 5.66E-05 | 5.66E-05 | 0.00% | Re2 | 1.00E-04 | 1.00E-04 | 0.00% |
| Re3 | 0.00E+00 | 0.00E+00 | 0.00% | Re3 | 0.00E+00 | 0.00E+00 | 0.00% |
| Re4 | 5.00E-04 | 5.00E-04 | 0.00% | Re4 | 1.00E-03 | 1.00E-03 | 0.01% |
| Re5 | 1.00E-03 | 1.00E-03 | 0.00% | Re5 | 5.00E-03 | 5.00E-03 | 0.05% |
| Re6 | 3.00E-04 | 3.00E-04 | 0.00% | Re6 | 7.00E-04 | 7.00E-04 | 0.01% |
| Re7 | 1.00E-04 | 1.00E-04 | 0.00% | Re7 | 5.00E-04 | 5.00E-04 | 0.01% |
| Re8 | 0.00E+00 | 0.00E+00 | 0.00% | Re8 | 0.00E+00 | 0.00E+00 | 0.00% |
| Re9 | 0.00E+00 | 0.00E+00 | 0.00% | Re9 | 0.00E+00 | 0.00E+00 | 0.00% |
| Re10 | 1.00E-03 | 1.00E-03 | 0.00% | Re10 | 1.00E-03 | 1.00E-03 | 0.01% |

**Tabla 22: . Porcentaje de cumplimiento de limite D.S. N°104/2018 MMA.****

| Promedio anual | Col2 | Col3 | Col4 | Percentil 99, diario | Col6 | Col7 | Col8 | Percentil 98,5 horario | Col10 | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Valor<br>modelado<br>[μg/m3] | Norma<br>[μg/m3N] | % de<br>norma | Receptor | Valor<br>modelado<br>[μg/m3] | Norma<br>[μg/m3N] | % de<br>norma | Receptor | Valor<br>modelado<br>[μg/m3] | Norma<br>[μg/m3N] | % de<br>norma |
| Re1 | 1.00E-04 | 60 | 0.000% | Re1 | 1.00E-03 | 150<br> | 0.001% | Re1 | 1.00E-03 | 350 | 0.001% |
| Re2 | 1.00E-04 | 1.00E-04 | 0.000% | Re2 | 1.00E-03 | 1.00E-03 | 0.001% | Re2 | 1.00E-03 | 1.00E-03 | 0.001% |
| Re3 | 1.21E-05 | 1.21E-05 | 0.000% | Re3 | 0.00E+00 | 0.00E+00 | 0.000% | Re3 | 0.00E+00 | 0.00E+00 | 0.000% |
| Re4 | 3.00E-04 | 3.00E-04 | 0.001% | Re4 | 5.00E-03 | 5.00E-03 | 0.003% | Re4 | 3.00E-03 | 3.00E-03 | 0.002% |
| Re5 | 8.00E-04 | 8.00E-04 | 0.001% | Re5 | 1.00E-02 | 1.00E-02 | 0.007% | Re5 | 5.00E-03 | 5.00E-03 | 0.003% |
| Re6 | 1.00E-04 | 1.00E-04 | 0.000% | Re6 | 6.00E-03 | 6.00E-03 | 0.004% | Re6 | 1.00E-03 | 1.00E-03 | 0.001% |
| Re7 | 1.00E-04 | 1.00E-04 | 0.000% | Re7 | 2.00E-03 | 2.00E-03 | 0.001% | Re7 | 1.00E-03 | 1.00E-03 | 0.001% |
| Re8 | 0.00E+00 | 0.00E+00 | 0.000% | Re8 | 0.00E+00 | 0.00E+00 | 0.000% | Re8 | 0.00E+00 | 0.00E+00 | 0.000% |
| Re9 | 0.00E+00 | 0.00E+00 | 0.000% | Re9 | 0.00E+00 | 0.00E+00 | 0.000% | Re9 | 0.00E+00 | 0.00E+00 | 0.000% |
| Re10 | 1.00E-04 | 1.00E-04 | 0.000% | Re10<br> | 2.00E-03<br> | 2.00E-03<br> | 0.001%<br> | Re10 | 1.00E-03 | 1.00E-03 | 0.001% |

**Tabla 23: . Porcentaje de cumplimiento de limite D.S. N°114/2002 MINSGPRES.****

| Promedio anual | Col2 | Col3 | Col4 | Percentil 99, horario | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Valor modelado<br>[μg/m3] | Norma [μg/m3N] | % de norma | Receptor | Valor modelado<br>[μg/m3] | Norma [μg/m3N] | % de norma |
| Re1 | 3.00E-02 | 100 | 0.05% | Re1 | 2.83E-01 | 400 | 0.19% |
| Re2 | 1.16E-02 | 1.16E-02 | 0.02% | Re2 | 2.83E-01 | 2.83E-01 | 0.19% |
| Re3 | 0.00E+00 | 0.00E+00 | 0.00% | Re3 | 0.00E+00 | 0.00E+00 | 0.00% |
| Re4 | 3.00E-01 | 3.00E-01 | 0.50% | Re4 | 2.00E+00 | 2.00E+00 | 1.33% |
| Re5 | 8.00E-01 | 8.00E-01 | 1.33% | Re5 | 1.00E+01 | 1.00E+01 | 6.67% |
| Re6 | 1.00E-01 | 1.00E-01 | 0.17% | Re6 | 1.00E+00 | 1.00E+00 | 0.67% |
| Re7 | 1.00E-01 | 1.00E-01 | 0.17% | Re7 | 1.00E+00 | 1.00E+00 | 0.67% |
| Re8 | 0.00E+00 | 0.00E+00 | 0.00% | Re8 | 0.00E+00 | 0.00E+00 | 0.00% |
| Re9 | 0.00E+00 | 0.00E+00 | 0.00% | Re9 | 0.00E+00 | 0.00E+00 | 0.00% |
| Re10 | 1.00E-01 | 1.00E-01 | 0.17%<br> | Re10<br> | 6.00E+00 | 6.00E+00 | 4.00% |

**Tabla 24.: MP2,5 [μg/m3] promedio anual.****

| Receptor | Valor<br>modelado<br>[μg/m3] | Línea<br>Base<br>[μg/m3N] | Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[μg/m3N] | Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Valor<br>modelado<br>[μg/m3] | Línea<br>Base<br>[μg/m3N] | Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[μg/m3N] | Este | Norte |
| Re1 | 1,00E-02 | 23,5 | 0,3015 | 23,80 | 20 | 344633 | 6225424 |
| Re2 | 1,00E-02 | 1,00E-02 | 1,00E-02 | 23,80 | 23,80 | 344253 | 6225476 |
| Re3 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 23,79 | 23,79 | 343363 | 6225175 |
| Re4 | 1,00E-01 | 1,00E-01 | 1,00E-01 | 23,89 | 23,89 | 345012 | 6225246 |
| Re5 - PMI | 3,00E-01 | 3,00E-01 | 3,00E-01 | 24,09 | 24,09 | 344909 | 6224852 |
| Re6 | 7,00E-02 | 7,00E-02 | 7,00E-02 | 23,86 | 23,86 | 344834 | 6224745 |
| Re7 | 3,00E-02 | 3,00E-02 | 3,00E-02 | 23,82 | 23,82 | 344768 | 6224653 |
| Re8 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 23,79 | 23,79 | 338517 | 6224401 |
| Re9 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 23,79 | 23,79 | 339495 | 6221288 |
| Re10 | 7,00E-02 | 7,00E-02 | 7,00E-02 | 23,86 | 23,86 | 342431 | 6219932 |

**Tabla 25.: MP2,5 [μg/m3] percentil 98, 24 horas.****

| Receptor | Valor<br>modelado<br>[μg/m3] | Línea<br>Base<br>[μg/m3N] | Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[μg/m3N] | Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Valor<br>modelado<br>[μg/m3] | Línea<br>Base<br>[μg/m3N] | Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[μg/m3N] | Este | Norte |
| Re1 | 1,00E-01 | 77,8 | 1,5 | 79,40 | 50 | 344633 | 6225424 |
| Re2 | 1,00E-01 | 1,00E-01 | 1,00E-01 | 79,40 | 79,40 | 344253 | 6225476 |
| Re3 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 79,30 | 79,30 | 343363 | 6225175 |
| Re4 | 1,00E+00 | 1,00E+00 | 1,00E+00 | 80,30 | 80,30 | 345012 | 6225246 |
| Re5 - PMI | 2,00E+00 | 2,00E+00 | 2,00E+00 | 81,30 | 81,30 | 344909 | 6224852 |
| Re6 | 5,00E-01 | 5,00E-01 | 5,00E-01 | 79,80 | 79,80 | 344834 | 6224745 |
| Re7 | 4,00E-01 | 4,00E-01 | 4,00E-01 | 79,70 | 79,70 | 344768 | 6224653 |
| Re8 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 79,30 | 79,30 | 338517 | 6224401 |
| Re9 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 79,30 | 79,30 | 339495 | 6221288 |
| Re10 | 6,00E-01 | 6,00E-01 | 6,00E-01 | 79,90 | 79,90 | 342431 | 6219932 |

**Tabla 26.: MP10[μg/m3] promedio anual.****

| Receptor | Valor<br>modelado<br>[μg/m3] | Línea Base<br>[μg/m3N] | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[μg/m3N] | Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Valor<br>modelado<br>[μg/m3] | Línea Base<br>[μg/m3N] | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[μg/m3N] | Este | Norte |
| Re1 | 0,06 | 58,60 | 0,45 | 59,1 | 50 | 344633 | 6225424 |
| Re2 | 0,06 | 0,06 | 0,06 | 59,1 | 59,1 | 344253 | 6225476 |
| Re3 | 0,01 | 0,01 | 0,01 | 59,1 | 59,1 | 343363 | 6225175 |
| Re4 | 0,06 | 0,06 | 0,06 | 59,1 | 59,1 | 345012 | 6225246 |
| Re5 - PMI | 0,10 | 0,10 | 0,10 | 59,1 | 59,1 | 344909 | 6224852 |
| Re6 - PMI | 0,10 | 0,10 | 0,10 | 59,1 | 59,1 | 344834 | 6224745 |
| Re7 | 0,02 | 0,02 | 0,02 | 59,1 | 59,1 | 344768 | 6224653 |
| Re8 | 0,00 | 0,00 | 0,00 | 59,0 | 59,0 | 338517 | 6224401 |
| Re9 | 0,00 | 0,00 | 0,00 | 59,0 | 59,0 | 339495 | 6221288 |
| Re10 | 0,00 | 0,00 | 0,00 | 59,0 | 59,0 | 342431 | 6219932 |

**Tabla 27.: MP10[μg/m3] percentil 98, 24 horas.****

| Receptor | Valor<br>modelado<br>[μg/m3] | Línea Base<br>[μg/m3N] | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[μg/m3N] | Coordenadas<br>[+N18:U18m]<br>UTM WGS-84,<br>Huso 19S | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Valor<br>modelado<br>[μg/m3] | Línea Base<br>[μg/m3N] | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[μg/m3N] | Este | Norte |
| Re1 | 0,3 | 131,99 | 2,23 | 134,5 | 130 | 344633 | 6225424 |
| Re2 | 0,3 | 0,3 | 0,3 | 134,5 | 134,5 | 344253 | 6225476 |
| Re3 | 0,0 | 0,0 | 0,0 | 134,2 | 134,2 | 343363 | 6225175 |
| Re4 | 0,1 | 0,1 | 0,1 | 134,3 | 134,3 | 345012 | 6225246 |
| Re5 - PMI | 0,5 | 0,5 | 0,5 | 134,7 | 134,7 | 344909 | 6224852 |
| Re6 | 0,1 | 0,1 | 0,1 | 134,3 | 134,3 | 344834 | 6224745 |
| Re7 | 0,1 | 0,1 | 0,1 | 134,3 | 134,3 | 344768 | 6224653 |
| Re8 | 0,0 | 0,0 | 0,0 | 134,2 | 134,2 | 338517 | 6224401 |
| Re9 | 0,0 | 0,0 | 0,0 | 134,2 | 134,2 | 339495 | 6221288 |
| Re10 | 0,0 | 0,0 | 0,0 | 134,2 | 134,2 | 342431 | 6219932 |

**Tabla 28.: Concentración diaria [μg/m3].****

| Receptor | Valor<br>modelado<br>[μg/ m3] | Línea Base<br>[μg/m 3N] | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final<br>[μg/m 3N] | *Norma<br>[μg/m 3N] | Coordenadas [m] UTM<br>WGS-84, Huso 19S | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Valor<br>modelado<br>[μg/m3]<br> | Línea Base<br>[μg/m3N]<br> | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final<br>[μg/m3N]<br> | *Norma<br>[μg/m3N]<br> | Este | Norte |
| Re1 | 10,0 | Sin<br>registros | Sin<br>registros | 10,0 | 1,25E+05 | 344633 | 6225424 |
| Re2 | 8,0 | 8,0 | 8,0 | 8,0 | 8,0 | 344253 | 6225476 |
| Re3 | 1,5 | 1,5 | 1,5 | 1,5 | 1,5 | 343363 | 6225175 |
| Re4 | 30,0 | 30,0 | 30,0 | 30,0 | 30,0 | 345012 | 6225246 |
| Re5 - PMI | 100,0 | 100,0 | 100,0 | 100,0 | 100,0 | 344909 | 6224852 |
| Re6 | 30,0 | 30,0 | 30,0 | 30,0 | 30,0 | 344834 | 6224745 |
| Re7 | 10,0 | 10,0 | 10,0 | 10,0 | 10,0 | 344768 | 6224653 |
| Re8 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 338517 | 6224401 |
| Re9 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 339495 | 6221288 |
| Re10 | 30,0 | 30,0 | 30,0 | 30,0 | 30,0 | 342431 | 6219932 |
| * Altura de 1.6m | * Altura de 1.6m | * Altura de 1.6m | * Altura de 1.6m | * Altura de 1.6m | * Altura de 1.6m | * Altura de 1.6m | * Altura de 1.6m |

**Tabla 29.: CO, Percentil 99, 1 hora.****

| Receptor | Valor<br>modelado<br>[μg/m3] | Línea Base<br>[μg/m3N] | Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[mg/m3N] | Coordenadas<br>[m] UTM WGS-<br>84, Huso 19S | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Valor<br>modelado<br>[μg/m3] | Línea Base<br>[μg/m3N] | Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[mg/m3N] | Este | Norte |
| Re1 | 0,09 | 1,97 | 22,57 | 24,63 | 30 | 344633 | 6E+06 |
| Re2 | 0,06 | 0,06 | 0,06 | 24,60 | 24,60 | 344253 | 6E+06 |
| Re3 | 0,00 | 0,00 | 0,00 | 24,54 | 24,54 | 343363 | 6E+06 |
| Re4 | 0,50 | 0,50 | 0,50 | 25,04 | 25,04 | 345012 | 6E+06 |
| Re5 - PMI | 1,00 | 1,00 | 1,00 | 25,54 | 25,54 | 344909 | 6E+06 |
| Re6 | 0,30 | 0,30 | 0,30 | 24,84 | 24,84 | 344834 | 6E+06 |
| Re7 | 0,10 | 0,10 | 0,10 | 24,64 | 24,64 | 344768 | 6E+06 |
| Re8 | 0,00 | 0,00 | 0,00 | 24,54 | 24,54 | 338517 | 6E+06 |
| Re9 | 0,00 | 0,00 | 0,00 | 24,54 | 24,54 | 339495 | 6E+06 |
| Re10 - PMI | 1,00 | 1,00 | 1,00 | 25,54 | 25,54 | 342431 | 6E+06 |

**Tabla 30.: CO, Percentil 99, 8 horas.****

| Receptor | Valor<br>modelado<br>[μg/m3] | Línea Base<br>[μg/m3N] | Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[mg/m3N] | Coordenadas<br>[m] UTM WGS-<br>84, Huso 19S | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Valor<br>modelado<br>[μg/m3] | Línea Base<br>[μg/m3N] | Aporte otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[mg/m3N] | Este | Norte |
| Re1 | 0,2 | 1,63 | 15,80 | 17,63 | 10 | 344633 | 6E+06 |
| Re2 | 0,1 | 0,1 | 0,1 | 17,53 | 17,53 | 344253 | 6E+06 |
| Re3 | 0 | 0 | 0 | 17,43 | 17,43 | 343363 | 6E+06 |
| Re4 | 1 | 1 | 1 | 18,43 | 18,43 | 345012 | 6E+06 |
| Re5 - PMI | 5 | 5 | 5 | 22,43 | 22,43 | 344909 | 6E+06 |
| Re6 | 0,7 | 0,7 | 0,7 | 18,13 | 18,13 | 344834 | 6E+06 |
| Re7 | 0,5 | 0,5 | 0,5 | 17,93 | 17,93 | 344768 | 6E+06 |
| Re8 | 0 | 0 | 0 | 17,43 | 17,43 | 338517 | 6E+06 |
| Re9 | 0 | 0 | 0 | 17,43 | 17,43 | 339495 | 6E+06 |
| Re10 | 1 | 1 | 1 | 18,43 | 18,43 | 342431 | 6E+06 |

**Tabla 31.: SO** **2** **, Promedio anual.****

| Receptor | Valor<br>modelado<br>[μg/m3] | Línea Base<br>[μg/m3N] | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[μg/m3N] | Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | Este | Norte |
| Re1 | 1,0E-04 | 1,02 | 0,12 | 1,14 | 60 | 344633 | 6225424 |
| Re2 | 1,0E-04 | 1,0E-04 | 1,0E-04 | 1,14 | 1,14 | 344253 | 6225476 |
| Re3 | 1,2E-05 | 1,2E-05 | 1,2E-05 | 1,14 | 1,14 | 343363 | 6225175 |
| Re4 | 3,0E-04 | 3,0E-04 | 3,0E-04 | 1,14 | 1,14 | 345012 | 6225246 |
| Re5 - PMI | 8,0E-04 | 8,0E-04 | 8,0E-04 | 1,14 | 1,14 | 344909 | 6224852 |
| Re6 | 1,0E-04 | 1,0E-04 | 1,0E-04 | 1,14 | 1,14 | 344834 | 6224745 |
| Re7 | 1,0E-04 | 1,0E-04 | 1,0E-04 | 1,14 | 1,14 | 344768 | 6224653 |
| Re8 | 0,0E+00 | 0,0E+00 | 0,0E+00 | 1,14 | 1,14 | 338517 | 6224401 |
| Re9 | 0,0E+00 | 0,0E+00 | 0,0E+00 | 1,14 | 1,14 | 339495 | 6221288 |
| Re10 | 1,0E-04 | 1,0E-04 | 1,0E-04 | 1,14 | 1,14 | 342431 | 6219932 |

**Tabla 32.: SO** **2** **, Percentil 99, 24 horas.****

| Receptor | Valor<br>modelado<br>[μg/m3] | Línea Base<br>[μg/m3N] | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[μg/m3N] | Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Valor<br>modelado<br>[μg/m3] | Línea Base<br>[μg/m3N] | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N] | Norma<br>[μg/m3N] | Este | Norte |
| Re1 | 1,0E-03 | 1,36 | 0,59 | 1,95 | 150 | 344633 | 6225424 |
| Re2 | 1,0E-03 | 1,0E-03 | 1,0E-03 | 1,95 | 1,95 | 344253 | 6225476 |
| Re3 | 0,0E+00 | 0,0E+00 | 0,0E+00 | 1,95 | 1,95 | 343363 | 6225175 |
| Re4 | 5,0E-03 | 5,0E-03 | 5,0E-03 | 1,95 | 1,95 | 345012 | 6225246 |
| Re5 - PMI | 1,0E-02 | 1,0E-02 | 1,0E-02 | 1,96 | 1,96 | 344909 | 6224852 |
| Re6 | 6,0E-03 | 6,0E-03 | 6,0E-03 | 1,95 | 1,95 | 344834 | 6224745 |
| Re7 | 2,0E-03 | 2,0E-03 | 2,0E-03 | 1,95 | 1,95 | 344768 | 6224653 |
| Re8 | 0,0E+00 | 0,0E+00 | 0,0E+00 | 1,95 | 1,95 | 338517 | 6224401 |
| Re9 | 0,0E+00 | 0,0E+00 | 0,0E+00 | 1,95 | 1,95 | 339495 | 6221288 |
| Re10 | 2,0E-03 | 2,0E-03 | 2,0E-03 | 1,95 | 1,95 | 342431 | 6219932 |

**Tabla 33.: SO** **2** **, Percentil 98,5 - 1 hora.****

| Rece ptor | Valor<br>modelado<br>[μg/ m3] | Línea Base<br>[μg/m 3N] | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg /m3N] | Norma<br>[μg/m 3N] | Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor<br> | Valor<br>modelado<br>[μg/m3]<br> | Línea Base<br>[μg/m3N]<br> | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N]<br> | Norma<br>[μg/m3N]<br> | Este | Norte |
| Re1 | 1,0E-03 | 1,02 | 0,00 | 1,948 | 350 | 344633 | 6225424 |
| Re2 | 1,0E-03 | 1,0E-03 | 1,0E-03 | 1,948 | 1,948 | 344253 | 6225476 |
| Re3 | 0,0E+00 | 0,0E+00 | 0,0E+00 | 1,947 | 1,947 | 343363 | 6225175 |
| Re4 | 3,0E-03 | 3,0E-03 | 3,0E-03 | 1,950 | 1,950 | 345012 | 6225246 |
| Re5 - PMI | 5,0E-03 | 5,0E-03 | 5,0E-03 | 1,952 | 1,952 | 344909 | 6224852 |
| Re6 | 1,0E-03 | 1,0E-03 | 1,0E-03 | 1,948 | 1,948 | 344834 | 6224745 |

**Tabla 34.: NO** **2** **, Promedio anual.****

| Rece ptor | Valor<br>modelado<br>[μg/ m3] | Línea Base<br>[μg/m 3N] | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg /m3N] | Norma<br>[μg/m 3N] | Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor<br> | Valor<br>modelado<br>[μg/m3]<br> | Línea Base<br>[μg/m3N]<br> | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N]<br> | Norma<br>[μg/m3N]<br> | Este | Norte |
| Re1 | 3E-02 | Sin<br>registros | 3,64 | 3,67 | 100 | 344633 | 6225424 |
| Re2 | 1E-02 | 1E-02 | 1E-02 | 3,65 | 3,65 | 344253 | 6225476 |
| Re3 | 0E+00 | 0E+00 | 0E+00 | 3,64 | 3,64 | 343363 | 6225175 |
| Re4 | 3E-01 | 3E-01 | 3E-01 | 3,94 | 3,94 | 345012 | 6225246 |
| Re5 - PMI | 8E-01 | 8E-01 | 8E-01 | 4,44 | 4,44 | 344909 | 6224852 |
| Re6 | 1E-01 | 1E-01 | 1E-01 | 3,74 | 3,74 | 344834 | 6224745 |
| Re7 | 1E-01 | 1E-01 | 1E-01 | 3,74 | 3,74 | 344768 | 6224653 |
| Re8 | 0E+00 | 0E+00 | 0E+00 | 3,64 | 3,64 | 338517 | 6224401 |
| Re9 | 0E+00 | 0E+00 | 0E+00 | 3,64 | 3,64 | 339495 | 6221288 |
| Re10 | 1E-01 | 1E-01 | 1E-01 | 3,74 | 3,74 | 342431 | 6219932 |

**Tabla 35.: NO** **2** **, Percentil 99, 1 hora.****

| Rece ptor | Valor<br>modelado<br>[μg/ m3] | Línea Base<br>[μg/m 3N] | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg /m3N] | Norma<br>[μg/m 3N] | Coordenadas [m]<br>UTM WGS-84,<br>Huso 19S | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor<br> | Valor<br>modelado<br>[μg/m3]<br> | Línea Base<br>[μg/m3N]<br> | Aporte<br>otro<br>proyecto<br>con RCA<br>[μg/m3N] | Concentración<br>final [μg/m3N]<br> | Norma<br>[μg/m3N]<br> | Este | Norte |
| Re1 | 3E-01 | Sin<br>registros | 18,19 | 18,47 | 400 | 344633 | 6225424 |
| Re2 | 3E-01 | 3E-01 | 3E-01 | 18,47 | 18,47 | 344253 | 6225476 |
| Re3 | 0E+00 | 0E+00 | 0E+00 | 18,19 | 18,19 | 343363 | 6225175 |
| Re4 | 2E+00 | 2E+00 | 2E+00 | 20,19 | 20,19 | 345012 | 6225246 |
| Re5 - PMI | 1E+01 | 1E+01 | 1E+01 | 28,19 | 28,19 | 344909 | 6224852 |
| Re6 | 1E+00 | 1E+00 | 1E+00 | 19,19 | 19,19 | 344834 | 6224745 |
| Re7 | 1E+00 | 1E+00 | 1E+00 | 19,19 | 19,19 | 344768 | 6224653 |
| Re8 | 0E+00 | 0E+00 | 0E+00 | 18,19 | 18,19 | 338517 | 6224401 |

**Tabla 36.: Análisis de significancia.****

| Contaminante | Periodo | Límite de<br>superación | Concentración<br>ambiental<br>2022<br>[μg/m3] | cumplimiento | Incremento<br>significativo<br>en la<br>concentración<br>[μg/m3]25 | Valor<br>modelado<br>[μg/m3]26 | Cumplimiento<br>bajo el<br>incremento<br>significativo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MP2,5 | 24 horas | 50 [μg/m3] | 77,8 | No | 1,7 | 0,105 | si |
| MP2,5 | anual | 20 [μg/m3] | 23,5 | No | 0,3 | 0,029 | si |
| MP10 | 24 horas | 130 [μg/m3] | 132 | No | 5 | 1,040 | si |
| MP10 | anual | 50 [μg/m3] | 58,6 | No | 1 | 0,240 | si |
| NO2 | 1 hora | 400 [μg/m3] | Sin registros | Si | 16 | 3,770 | si |
| NO2 | anual | 100 [μg/m3] | Sin registros | Si | 1 | 0,069 | si |
| CO | 1 hora | 26 ppm | 2,3 ppm | Si | 1500,0 | 0,006 | si |
| CO | anual | 9 ppm | 2,0 ppm | Si | 488,9 | 0,014 | si |
| SO2 | 24 horas | 150 [μg/m3] | 1,4 | Si | 2 | 0,008 | si |
| SO2 | anual | 60 [μg/m3] | 1,0 | Si | 1,2 | 0,001 | si |
