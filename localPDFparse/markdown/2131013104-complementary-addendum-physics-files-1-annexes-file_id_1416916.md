---
title: Sin título
author: Javier Peña
date: D:20160317111644-03'00'
language: es
type: report
pages: 75
has_toc: False
has_tables: True
extraction_quality: high
---

|Col1|Col2|Col3|
|---|---|---|
||<br> <br>ANEXO B<br>Modelación de Dispersión<br>Atmosférica de<br>Contaminantes||

## MODELACIÓN DE DISPERSIÓN ATMOSFÉRICA DE CONTAMINANTES

### “SISTEMA DE TRATAMIENTO DE AGUA POTABLE EL CARMELO”

PARA

**DOCUMENTO P&A**

**2948-AT-003**

|REV|FECHA|DESCRIPCIÓN|POR|REV|APR.|
|---|---|---|---|---|---|
|0|16.03.2016|Para Revisión y Comentarios del Cliente|SMO|MSA|CMM|
|||||||
|||||||
|||||||

#### ÍNDICE DE CONTENIDOS

1. ANTECEDENTES GENERALES ................................................................................................................. 1

2. MODELO UTILIZADO PARA REALIZAR SIMULACIÓN DE DISPERSIÓN ATMOSFÉRICA DE CONTAMINANTES

1

3. CARACTERIZACIÓN DEL AREA DE MODELACIÓN .................................................................................... 6

3.1 ANTECEDENTES GENERALES ........................................................................................... 6

3.2 VARIABLES DE SUPERFICIE CONSIDERADAS ..................................................................... 7

3.2.1 Topografía .............................................................................................................. 7

3.2.2 Usos de Suelo ......................................................................................................... 9

3.3 VARIABLES METEOROLÓGICAS...................................................................................... 10

3.3.1 Meteorología de superficie y de altura .................................................................. 10

3.3.3 Dirección y velocidad del viento ............................................................................ 12

3.3.4 Mapas campos de vientos dentro del dominio de la modelación ........................... 16

3.3.5 Mapas de altura de mezclado dentro del dominio de modelación ......................... 20

3.3.6 Temperatura del aire superficial............................................................................ 24

3.3.7 Humedad Relativa (HR) ......................................................................................... 28

3.3.10 Radiaciones ........................................................................................................... 32

3.4 RECEPTORES CONTEMPLADOS EN LA MODELACIÓN. .................................................... 34

3.4.1 Receptores Discretos (Estaciones de Monitoreo)................................................... 34

3.4.2 Receptores Sensibles ............................................................................................ 34

4 MARCO LEGAL.................................................................................................................................... 36

4.1 ASPECTOS GENERALES .................................................................................................. 36

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

a

4.2 NORMAS DE CALIDAD DEL AIRE .................................................................................... 37

5 LINEA DE BASE DE CALIDAD DEL AIRE ................................................................................................. 38

5.1 CONCENTRACIONES DE ESTACIÓN DE MONITOREO DE CALIDAD DEL AIRE .................... 38

5.2 ANÁLISIS ANUAL Y ESTACIONAL .................................................................................... 39

5.2.1 Material Particulado Respirable (MP 10 ) ................................................................. 39

5.1.2 Material Particulado Fino (MP 2,5 ) .......................................................................... 40

5.2.2 Dióxido de Azufre (SO 2 ) ......................................................................................... 41

6 DESCRIPCIÓN DE LAS FUENTES EMISORAS .......................................................................................... 43

6.1 UBICACIÓN DE FUENTES DE EMISIÓN ........................................................................... 43

6.2 TASAS DE EMISIÓN ....................................................................................................... 45

7 APORTES DEL PROYECTO A LAS CONCENTRACIONES ATMOSFÉRICAS .................................................. 48

8. RESULTADOS DE MODELACIÓN EN ESTACIÓN DE MONITOREO ........................................................... 53

9. CONCLUSIONES .................................................................................................................................. 55

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

b

#### ÍNDICE DE FIGURAS

F IGURA N° 1: R EPRESENTACIÓN G RÁFICA DEL M ODELO T IPO P UFF Y DE P LUMA . .............................................................. 2

F IGURA N° 2: V ISTA G ENERAL DE LA S UPERFICIE C ONSIDERADA EN LA M ODELACIÓN . ........................................................ 6

F IGURA N° 3: T OPOGRAFÍA C ONSIDERADA EN LA M ODELACIÓN . ................................................................................... 8

F IGURA N° 4: U SOS DE SUELO CONSIDERADO EN LA MODELACIÓN . ................................................................................ 9

F IGURA N° 5. G RILLA METEOROLÓGICA WRF UTILIZADA PARA LA MODELACIÓN EN C ALPUFF . ............................................ 11

F IGURA N° 6: R OSA DE VIENTO A NUAL EN P OZO A LMONTE 2014. .............................................................................. 12

F IGURA N° 7: G RÁFICO DE DISTRIBUCIÓN DE FRECUENCIA DE VIENTOS . ......................................................................... 13

F IGURA N° 8: R OSAS DE VIENTO, P ERIODO P RIMAVERA -V ERANO, 2014. ..................................................................... 14

F IGURA N° 9: R OSAS DE VIENTO, P ERIODO O TOÑO -I NVIERNO, 2014. ......................................................................... 14

F IGURA N° 10: G RÁFICOS DE DISTRIBUCIÓN DE FRECUENCIA, P ERIODO P RIMAVERA -V ERANO, 2014. .................................. 15

F IGURA N° 11: G RÁFICOS DE DISTRIBUCIÓN DE FRECUENCIA, P ERIODO O TOÑO -I NVIERNO, 2014. ...................................... 15

F IGURA N° 12. M APA DE VIENTO DE ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN NOCTURNO, PERIODO PRIMAVERA - VERANO,

2014. ................................................................................................................................................. 16

F IGURA N° 13. M APA DE VIENTO ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN DIURNO, PERIODO PRIMAVERA - VERANO, 2014. ... 17

F IGURA N° 14. M APA DE VIENTO ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN NOCTURNO, PERIODO OTOÑO - INVIERNO, 2014. ... 18

F IGURA N° 15. M APA DE VIENTO ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN DIURNO, PERIODO OTOÑO - INVIERNO, 2014. ....... 19

F IGURA N° 16. M APA DE ALTURA DE MEZCLA, ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN NOCTURNO, PERIODO PRIMAVERA

VERANO, 2014. ..................................................................................................................................... 20

F IGURA N° 17. M APA DE ALTURA DE MEZCLA, ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN DIURNO, PERIODO PRIMAVERA - VERANO,

2014. ................................................................................................................................................. 21

F IGURA N° 18. M APA DE ALTURA DE MEZCLA, ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN NOCTURNO, PERIODO OTOÑO - INVIERNO

2014. ................................................................................................................................................. 22

F IGURA N° 19. M APA DE ALTURA DE MEZCLA, ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN DIURNO, PERIODO OTOÑO - INVIERNO,

2014. ................................................................................................................................................. 23

F IGURA N° 20. T EMPERATURA DEL AIRE SUPERFICIAL, ÁREA MODELACIÓN 62 X 62 KM AÑO 2014, PERIODO PRIMAVERAVERANO, RÉGIMEN NOCTURNO . .................................................................................................................. 24

F IGURA N° 21. T EMPERATURA DEL AIRE SUPERFICIAL, ÁREA MODELACIÓN 62 X 62 KM AÑO 2014, PERIODO PRIMAVERA - VERANO,

RÉGIMEN DIURNO . .................................................................................................................................. 25

F IGURA N° 22. T EMPERATURA DEL AIRE SUPERFICIAL, ÁREA MODELACIÓN 62 X 62 KM AÑO 2014, PERIODO OTOÑO - INVIERNO,

RÉGIMEN NOCTURNO . .............................................................................................................................. 26

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

c

F IGURA N° 23. T EMPERATURA DEL AIRE SUPERFICIAL, ÁREA MODELACIÓN 62 X 62 KM AÑO 2014, PERIODO OTOÑO - INVIERNO,

RÉGIMEN DIURNO . .................................................................................................................................. 27

F IGURA N° 24. H UMEDAD RELATIVA, ÁREA MODELACIÓN 62 X 62 KM AÑO 2014, PERIODO DE VERANO, RÉGIMEN DIURNO . ..... 28

F IGURA N° 25. H UMEDAD RELATIVA, ÁREA MODELACIÓN 62 X 62 KM AÑO 2014, PERIODO DE VERANO, RÉGIMEN NOCTURNO .. 29

F IGURA N° 26. H UMEDAD RELATIVA, ÁREA MODELACIÓN 62 X 62 KM AÑO 2014, PERIODO DE INVIERNO, RÉGIMEN DIURNO . ... 30

F IGURA N° 27. H UMEDAD RELATIVA, ÁREA MODELACIÓN 62 X 62 KM AÑO 2014, PERIODO DE INVIERNO, RÉGIMEN NOCTURNO .

.......................................................................................................................................................... 31

F IGURA N° 28. R ADIACIÓN SOLAR, ÁREA MODELACIÓN 62 X 62 KM AÑO 2014, PERIODO DE VERANO . ................................ 32

F IGURA N° 29. R ADIACIÓN SOLAR, ÁREA MODELACIÓN 62 X 62 KM AÑO 2014, PERIODO DE INVIERNO . ............................... 33

F IGURA N° 30. R ECEPTORES SENSIBLES CERCANOS AL PROYECTO . ................................................................................ 35

#### ÍNDICE DE TABLAS

T ABLA N° 1: V ÉRTICES DEL Á REA DE M ODELACIÓN DEL P ROYECTO . ............................................................................... 7

T ABLA N° 2. C OORDENADAS UTM DE ESTACIÓN P OZO A LMONTE COSAYACH. ............................................................ 34

T ABLA N° 3. U BICACIÓN DE R ECEPTORES SENSIBLES RESPECTO AL PROYECTO .................................................................. 35

T ABLA N° 4: N ORMAS DE C ALIDAD DEL A IRE C ONSIDERADAS EN LA M ODELACIÓN ........................................................... 37

T ABLA N° 5: C ONCENTRACIONES ESTABLECIDAS A PARTIR DE LOS DATOS DE LA E STACIÓN P OZO A LMONTE PARA EL PERIODO ENERO

2013 - JULIO 2013................................................................................................................................. 38

T ABLA N° 6: U BICACIÓN DE F UENTES E MISORAS P UNTUALES . .................................................................................... 43

T ABLA N° 7: U BICACIÓN DE F UENTES E MISORAS A REALES . ........................................................................................ 44

T ABLA N° 8: C ARACTERÍSTICAS Y TASAS DE EMISIÓN DE CONTAMINANTES DE FUENTES PUNTUALES . ..................................... 45

T ABLA N° 9: T ASAS DE EMISIÓN DE CONTAMINANTES DE FUENTES EMISORAS AREALES . ..................................................... 47

T ABLA N° 10: A PORTE DEL PROYECTO A LA CONCENTRACIÓN AMBIENTAL EN EL PMI ( μG / M [3] N). ........................................ 48

T ABLA N° 11: A PORTE DEL PROYECTO A LA CONCENTRACIÓN AMBIENTAL DE MP 10 SOBRE RECEPTORES SENSIBLES ( G / M [3] N). ... 49

T ABLA N° 12: A PORTE DEL PROYECTO A LA CONCENTRACIÓN AMBIENTAL DE MP 2,5 SOBRE RECEPTORES SENSIBLES ( G / M [3] N). .. 50

T ABLA N° 13: A PORTE DEL PROYECTO A LA CONCENTRACIÓN AMBIENTAL DE NO 2 SOBRE RECEPTORES SENSIBLES ( G / M [3] N). .... 50

T ABLA N° 14. A PORTE DEL PROYECTO A LA CONCENTRACIÓN AMBIENTAL DE CO SOBRE RECEPTORES SENSIBLES ( G / M [3] N). ...... 51

T ABLA N° 15. A PORTE DEL PROYECTO A LA CONCENTRACIÓN AMBIENTAL DE SO 2 SOBRE RECEPTORES SENSIBLES ( G / M [3] N). ..... 51

T ABLA N° 16: C ONCENTRACIÓN FINAL ESPERADA PARA C ONTAMINANTES EN E STACIÓN P OZO A LMONTE COSAYACH ( G / M [3] N).

.......................................................................................................................................................... 54

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

d

#### ÍNDICE DE APÉNDICES

APÉNDICE 1 Plumas De Dispersión De Contaminantes Modelados En Calpuff View

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

e

#### 1. ANTECEDENTES GENERALES

El proyecto “Sistema de Tratamiento de Agua Potable El Carmelo” ubicado en la comuna de Pozo

Almonte, I Región de Tarapacá, consiste en la construcción y operación de una Planta de Tratamiento

de Agua Potable para el abatimiento de arsénico mediante un sistema de Sistema de coagulación

filtración para un caudal total de 750 L/s, con el fin de dar cumplimiento con las concentraciones

inferiores a 0,01 mg/L de arsénico definidas en la norma NCh 409/2005, la cual debe ser efectiva a

partir del año 2017, tal como lo especifica la Ord. 1582/2007 de la Superintendencia de Servicios

Sanitarios.

Las principales emisiones a la atmósfera asociadas a la construcción y operación del proyecto

corresponderán a material particulado total (expresado como MP 10 y MP 2,5 para efectos de contrastar

con la normativa legal), Óxidos de Nitrógeno (NO 2 ), Óxidos de Azufre (SO 2 ) y Monóxido de Carbono

(CO).

Con el propósito de conocer los aportes al ambiente de las emisiones generadas por las fuentes del

proyecto se realizó una modelación de dispersión atmosférica de contaminantes, la que considera las

emisiones calculadas para la construcción y operación del proyecto, bajo la condición de

funcionamiento normal. Para ello se ha utilizado como base lo establecido en la _“Guía para el Uso de_

_Modelos de Calidad del Aire en el SEIA”._

#### 2. MODELO UTILIZADO PARA REALIZAR SIMULACIÓN DE DISPERSIÓN ATMOSFÉRICA DE CONTAMINANTES

Para realizar la modelación de emisiones atmosféricas se utilizó el programa de dispersión atmosférica

de contaminantes denominado Calpuff View V.7.1. Este modelo es recomendado por la EPA de

E.E.U.U. para estimar el transporte de largo alcance de contaminantes e impacto en áreas con terreno

complejo, y es reconocido por el Servicio de Evaluación Ambiental (SEA), como modelo regulatorio; es

decir, puede ser aplicado durante procesos de Evaluación Ambiental que involucren Estudios de

Impacto Ambiental y Declaraciones de Impacto Ambiental.

Los modelos de ‘paquetes de emisiones’ o de ‘puffs’ o ‘de trayectorias’ representan la emisión de cada

fuente puntual como un conjunto de paquetes de contaminantes (‘puffs’), los cuales son

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

1

transportados por el campo de vientos, se expanden al mezclarse con el aire que los rodea y en su

interior se considera también las reacciones químicas más importantes.

Los modelos de “puff”, a diferencia de los modelos Gaussianos, permiten manejar situaciones

transientes como desarrollo de brisa valle-cordillera y los casos de calmas del viento, donde los

modelos Gaussianos predicen concentraciones infinitas (o irrazonablemente altas), ya que en tal caso

los paquetes de contaminación siguen creciendo en tamaño, aunque la velocidad de viento sea

prácticamente cero.

Por esta misma razón los modelos de puff son particularmente útiles para simular situaciones de

acumulación de contaminantes bajo condiciones de muy mala dispersión (alta estabilidad atmosférica,

bajos vientos superficiales), donde fallan los modelos Gaussianos (que tienden a estimar muy altas

condiciones en las horas previas al amanecer, pese a que en esas condiciones las emisiones suelen ser

mínimas).

**Figura N° 1: Representación Gráfica del Modelo Tipo Puff y de Pluma.**

Fuente: Lakes Environmental

En la Ecuación N° 1 se presenta la fórmula que utiliza el modelo Calpuff View para el cálculo de

concentración en el aire de algún contaminante determinado que haya sido emitido a la atmósfera por

una fuente fija y móvil.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

2

**Ecuación N° 1: Ecuación que domina el modelo utilizado** .

2
  [][] [;
 = ] ~~~~

~~~~ 2 


 =
2  


-

 − []   [][]

 

[]   [][] [ ∙

 −]   [][]

"



 − [(][
] [] 2 [ + 2]  [] [
h][)] !

#$%"

Donde:

C : Concentración del contaminante a nivel de suelo

Q : Masa de contaminante contenida en el puff

σ x : Desviación estándar de la distribución gaussiana de concentración, en la dirección del viento

σ y : Desviación estándar de la distribución gaussiana de concentración, en la dirección perpendicular a

la del viento

σ z : Desviación estándar de la distribución gaussiana de la concentración, en la dirección vertical

d a : Distancia desde el centro geométrico del puff al receptor en la dirección del viento

d c : Distancia desde el centro geométrico del puff al receptor en la dirección perpendicular a la del

viento

g Término vertical de la ecuación gaussiana, que considera las interacciones del puff con el suelo y con

la altura de mezclado

H e : Altura efectiva desde el suelo hasta el centro geométrico del puff

h: Altura de capa de mezclado

En términos generales, el modelo Calpuff View trabaja utilizando datos de superficie terrestre

(variables de superficie) y datos meteorológicos de altura y superficie. Con dichos datos el programa es

capaz de predecir el movimiento del puff y el posterior arrastre de contaminantes atmosféricos dentro

de un área geográfica determinada (área de modelación). Resultado de lo anterior, se puede evaluar la

magnitud de los impactos ambientales sobre la calidad del aire producto de la contaminación

atmosférica originada desde fuentes fijas y móviles.

Las variables de superficie consideradas para la modelación fueron:

 Topografía del Área de Modelación

 - Albedo

 - Radio de Bowen

 - Rugosidad de superficie

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

3

 - Leaf Area Index (LAI)

La incidencia de las variables de superficie sobre el modelo se relaciona principalmente con la

formación y o modificación del viento en el área de modelación.

Dependiendo de las características que presente el suelo en la superficie (tipo de suelo, especies

vegetales y porcentaje de cobertura vegetal), éste tiene la capacidad de irradiar calor, el cual por

medio de convección asciende hacia la atmósfera, alterando el gradiente térmico del área de

modelación, relacionando el comportamiento de las masas de aire con las características de superficie

del terreno.

Por otro lado, las variables meteorológicas que utiliza el modelo Calpuff View, son:

 - Dirección del viento (Grados)

 - Velocidad del Viento (m/s)

 - Mapa de altura de mezclado (m)

 - Temperatura (oC)

 - Humedad relativa (%)

 - Precipitaciones (mm)

 - Radiación (Wm [2] /hr)

Las variaciones en la concentración de los contaminantes están directamente relacionadas con dichas

variables meteorológicas, debido a que las variaciones en la temperatura y los porcentajes de

radiación solar que el suelo recibe son los principales causantes de los fenómenos atmosféricos como

las inversiones térmicas, fenómeno por el cual se genera una alta estabilidad en la atmósfera

disminuyendo la convección térmica y los fenómenos de transporte y difusión de gases, generando

finalmente aumentos en la concentración de contaminantes debido a una mayor estabilidad

atmosférica.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

4

En cuanto a la dirección del viento, ésta tiene como resultado el transporte de contaminantes hacia un

área determinada, factor que se ve relacionado a su vez directamente con la topografía del lugar en

conjunto con las demás variables mencionadas en los puntos anteriores.

A su vez, los tipos de fuentes de emisión que el software es capaz de modelar son:

 - Fuentes Puntuales

 - Fuentes por Volumen

 - Fuentes de Área

 - Fuentes Lineales

 - Fuentes de Antorcha o Torre de Incineración

 - A Cielo abierto (Open Pit)

En cuanto al tipo de fuente a considerar dentro de la modelación, se deben tomar en cuenta las

características físicas y operacionales que dichas fuentes poseen, lo que incide en la concentración de

los parámetros asociados a la salida del punto de emisión.

Por otro lado, las características del tipo de fuente que es utilizada dentro de la modelación también

incide en la dispersión final de los contaminantes, ya que su dispersión depende igualmente de la

altura de la fuente y de la temperatura de salida del flujo de gases, lo que en conjunto con las variables

atmosféricas definen el transporte y difusión de gases y los respectivos contaminantes dentro del área

de modelación considerada. Para el Proyecto en estudio, el tipo de fuente seleccionado para

considerar en la modelación correspondió a fuentes de tipo puntual y de tipo areal.

Dentro de lo presentado en el informe no se considera Análisis de Incertidumbre para meteorología y

para los resultados de la modelación debido a que no se cuenta con datos de estaciones de calidad del

aire cercanas que superen un periodo anual de datos para el caso de meteorología y 3 años para el

análisis de los resultados de la modelación, según se detalla en Acápite 5.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

5

#### 3. CARACTERIZACIÓN DEL AREA DE MODELACIÓN

**3.1** **ANTECEDENTES GENERALES**

En la Figura N° 2 se presenta una vista general de la zona de modelación, y en color blanco se presenta

el área de modelación considerada para la confección del presente informe, cuya superficie

corresponde a 3.844 km [2] (62 km x 62 km).

**Figura N° 2: Vista General de la Superficie Considerada en la Modelación.**

Fuente: Elaboración propia en base a Google Earth.

En la Tabla N° 1 se dan a conocer las coordenadas que definen la superficie de modelación considerada

en el modelo Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail: info@pyaing.cl**

6

**Tabla N° 1: Vértices del Área de Modelación del Proyecto.**

|Vértice|Coordenadas UTM, Huso 19 Sur, Datum WGS -84|Col3|
|---|---|---|
|**Vértice**|**Norte (m)**|**Este (m)**|
|Noreste|7.790.562|452.156|
|Noroeste|7.790.286|390.074|
|Suroeste|7.728.563|390.355|
|Sureste|7.728.850|452.438|

**3.2** **VARIABLES DE SUPERFICIE CONSIDERADAS**

**3.2.1** **Topografía**

El proyecto se ubica en la comuna de Pozo Almonte, a unos 3 kilómetros al oriente de la ciudad. Del

punto de vista físico, la zona se emplaza en la depresión intermedia de Chile en una faja de tierra de

baja pendiente que baja hacia el poniente, instalada entre la Cordillera de la Costa y la Cordillera de los

Andes. Esta se generó a partir del hundimiento de la corteza y posterior relleno producto de la erosión

de los Andes hasta formar la Pampa.

Para efectos de considerar dentro de la modelación de emisiones atmosféricas los efectos de la

topografía sobre la dispersión de contaminantes, es que las diferencias de altura serán consideradas

tanto por el modelo Calpuff View como por el procesador de terreno GEO del software Calpuff View de

Lakes Environmetal mediante la utilización de topografía digital del área considerada.

La topografía utilizada corresponde a un modelo de elevación digital SRTM3, cuyo formato es admitido

por el procesador topográfico GEO de Calpuff View, el cual tiene la capacidad de incluir dentro de la

modelación las diferencias de cotas del terreno a medida que se avanza hacia la costa y para toda el

área de modelación considerada. Con lo anterior, se logra incorporar la topografía al modelo Calpuff

View, según el área de modelación de interés y las coordenadas que demarcan el límite del área de

modelación.

A continuación en la Figura N° 3 se presenta un modelo digital de la topografía considerada dentro de

la modelación, cuyas elevaciones máximas alcanzan los 1.894 msnm.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

7

**Figura N° 3: Topografía Considerada en la Modelación.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

8

**3.2.2** **Usos de Suelo**

La comuna de Pozo Almonte tiene una superficie de 13.765,8 km [2] y tiene una población total de

14.366 habitantes (INE, 2006), esta se encuentra ubicada en pleno centro de la Pampa del Tamarugal y

sus principales actividades económicas corresponden al comercio, la minería, la agricultura, la

ganadería y el turismo.

La predominancia en el uso del suelo de la zona que rodea el proyecto es del tipo tierra estéril o árida

(sector 70), luego en un porcentaje menor se encuentran los pastizales (sector 30). Lo anterior se

puede observar a continuación en la Figura N° 4.

**Figura N° 4: Usos de suelo considerado en la modelación.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

9

**3.3** **VARIABLES METEOROLÓGICAS**

**3.3.1** **Meteorología de superficie y de altura**

Las variables meteorológicas procesadas por el modelo fueron las siguientes:

 - Dirección del viento (Grados)

 - Velocidad del Viento (m/s)

 - Mapa de altura de mezclado (m)

 - Temperatura (oC)

 - Humedad relativa (%)

 - Precipitaciones (mm)

 - Radiación (Wm [2] /hr)

Se utilizó el modelo numérico Weather Research and Forecasting Model (WRF), dada la falta de

información meteorológica en altura observacional representativa en el dominio de modelación

considerado, este modelo es recomendado por la “Guía para el Uso de Modelos de Calidad del Aire en

el SEIA”, siendo uno de los modelos meteorológicos de pronóstico más avanzados y completos, el que

es mantenido por NCAR/NOAA de Estados Unidos. Además, se ha ocupado en la mayoría de los

proyectos relacionados con modelación atmosférica cargados por organismos estatales, como la ex

CONAMA y la Comisión Nacional de Energía (CNE) en los últimos cinco años.

Se utilizó una grilla meteorológica de 62 X 62 km, generada a partir del modelo de pronóstico

meteorológico WRF, para el periodo 1 de Enero a 30 de Diciembre de 2014, la cual cumple todos los

lineamientos de la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”.

A continuación en la Figura N° 5 se presenta el dominio de la grilla meteorológica WRF, cuya resolución

es de 1 km.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

10

**Figura N° 5. Grilla meteorológica WRF utilizada para la modelación en Calpuff.**

Fuente: Elaboración propia mediante Google Earth y Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

11

**3.3.3** **Dirección y velocidad del viento**

En la Figura N° 6 se presenta la Rosa de Vientos para el periodo Enero - Diciembre 2014, según lo

obtenido por el modelo Weather Research and Forecasting.

**Figura N° 6: Rosa de viento Anual en Pozo Almonte 2014.**

Fuente: Elaboración propia mediante WR Plot, Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

12

**Figura N° 7: Gráfico de distribución de frecuencia de vientos.**

Fuente: Elaboración propia mediante WR Plot, Calpuff View.

En la Figura N° 6 se puede observar que el viento predominante en el área del Proyecto, de acuerdo al

vector resultante, corresponde principalmente a componente Oeste-Noroeste (ONO) y Oeste (O),

mientras que en la Figura N° 7 se puede apreciar que la velocidad del viento predominante fluctúa

entre los 0,5 y 2,1 m/s con una frecuencia de 37,7%.

A continuación se presenta el análisis estacional y diario para la dirección y velocidad del viento con

sus respectivos gráficos de frecuencia.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

13

**Figura N° 8: Rosas de viento, Periodo Primavera-Verano, 2014.**

**Régimen Nocturno** **Régimen Diario**

Fuente: Elaboración propia mediante WR Plot, Calpuff View.

**Figura N° 9: Rosas de viento, Periodo Otoño-Invierno, 2014.**

**Régimen Nocturno** **Régimen Diurno**

Fuente: Elaboración propia mediante WR Plot, Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

14

**Figura N° 10: Gráficos de distribución de frecuencia, Periodo Primavera-Verano, 2014.**

**Régimen Nocturno** **Régimen Diurno**

Fuente: Elaboración propia mediante WR Plot, Calpuff View.

**Figura N° 11: Gráficos de distribución de frecuencia, Periodo Otoño-Invierno, 2014.**

**Régimen Nocturno** **Régimen Diurno**

Fuente: Elaboración propia mediante WR Plot, Calpuff View.

De las figuras anteriores se pueden apreciar mayores velocidades de viento durante el día,

presentándose abundantes periodos de calma durante la noche. Estacionalmente, se observa que el

periodo primavera - verano presenta mayores velocidades de viento y que el periodo otoño - invierno,

alcanza un mayor porcentaje de calmas.

Por otro lado, en los meses de primavera - verano predominan vientos desde la dirección oeste

noroeste (ONO) y noroeste (NO) durante la noche y principalmente oeste (O) durante el día. Con

respecto a los meses de otoño - invierno, las direcciones que predominante vienen desde el nor

noroeste (NNO) durante la noche y oeste (O) durante el día.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

15

**3.3.4** **Mapas campos de vientos dentro del dominio de la modelación**

A continuación se presenta el campo de vientos superficiales simulados a partir del modelo de

pronóstico meteorológico WRF correspondiente al año 2014, haciéndose el análisis estacional y diario.

En la Figura N° 12 y Figura N° 13 se observa para los meses de primavera - verano la predominancia de

vientos provenientes del noroeste (NO) durante la noche y vientos desde el oeste (O) durante el día.

**Figura N° 12. Mapa de viento de área modelación 62 x 62 km, régimen nocturno, periodo primavera-**

**verano, 2014.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

16

En la Figura N° 13 se puede apreciar que el viento presenta una mayor intensidad durante el día

alcanzándose velocidades superiores a 5,5 m/s, a diferencia de horas de la noche (Figura N° 12), donde

las velocidades se encuentran, en su mayoría, bajo los 2,4 m/s.

**Figura N° 13. Mapa de viento área modelación 62 x 62 km, régimen diurno, periodo primavera-**

**verano, 2014.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

17

En la Figura N° 14 es posible distinguir componentes norte (N) del viento de manera predominante, lo

que es habitual en los meses de otoño - invierno, por su parte en el día ( Figura N° 15 ) se observa una

predominancia de vientos provenientes del oeste (O).

**Figura N° 14. Mapa de viento área modelación 62 x 62 km, régimen nocturno, periodo otoño-**

**invierno, 2014.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

18

**Figura N° 15. Mapa de viento área modelación 62 x 62 km, régimen diurno, periodo otoño-invierno,**

**2014.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

19

**3.3.5** **Mapas de altura de mezclado dentro del dominio de modelación**

A continuación se presentan las capas de altura de mezclado, tanto para un régimen diurno como

nocturno, para las estaciones de otoño - invierno y primavera - verano. Se puede observar que en

horas de la noche se presentan bajas alturas en la capa de mezclado que llegan a los 225 m sobre el

nivel del terreno en los meses de primavera - verano y 179 m en los meses de otoño - invierno. Por

otro lado, durante el día se alcanzan alturas de mezclado más elevadas que superan los 2.457 metros

sobre el nivel del terreno en primavera - verano, mientras que en otoño - invierno las alturas de

mezcla no alcanzan los 1.900 metros.

**Figura N° 16. Mapa de altura de mezcla, área modelación 62 x 62 km, régimen nocturno, periodo**

**primavera-verano, 2014.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

20

**Figura N° 17. Mapa de altura de mezcla, área modelación 62 x 62 km, régimen diurno, periodo**

**primavera-verano, 2014.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

21

**Figura N° 18. Mapa de altura de mezcla, área modelación 62 x 62 km, régimen nocturno, periodo**

**otoño-invierno 2014.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

22

**Figura N° 19. Mapa de altura de mezcla, área modelación 62 x 62 km, régimen diurno, periodo**

**otoño- invierno, 2014.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

23

**3.3.6** **Temperatura del aire superficial**

A continuación en la Figura N° 20 y Figura N° 21 se presentan las temperaturas del aire para los meses

de primavera - verano, donde se puede observar una diferencia tanto en los valores como en las

superficies, dado que evidentemente el periodo nocturno posee menores temperaturas que el diurno

y adicionalmente se observa que durante el periodo diurno las mayores temperaturas abarcan una

superficie mucho mayor que en la noche.

**Figura N° 20. Temperatura del aire superficial, área modelación 62 x 62 km año 2014, periodo**

**primavera - verano, régimen nocturno.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

24

**Figura N° 21. Temperatura del aire superficial, área modelación 62 x 62 km año 2014, periodo**

**primavera-verano, régimen diurno.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

25

Para el caso de los meses de otoño - invierno se observan menores temperaturas que en primaveraverano, observándose que las mayores temperaturas en el periodo nocturno son 6,83 K más bajas y en

el periodo diurno son 1,2 K más que en primavera - verano. Adicionalmente, las superificies de las

mayores temperaturas son considerablemente más pequeñas que en los meses de primaveraverano.

**Figura N° 22. Temperatura del aire superficial, área modelación 62 x 62 km año 2014, periodo otoño-**

**invierno, régimen nocturno.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

26

**Figura N° 23. Temperatura del aire superficial, área modelación 62 x 62 km año 2014, periodo otoño-**

**invierno, régimen diurno.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

27

**3.3.7** **Humedad Relativa (HR)**

A continuación en la Figura N° 24, Figura N° 25, Figura N° 26 y Figura N° 27, se observa que las

humedades relativas aumentan en periodo de invierno alcanzando hasta valores de 100% de HR

durante las noches, por otro lado en el periodo estival estas apenas superan un 97% en hora nocturna

en área muy acotadas. Para el caso diurno se observan valores que superan el 51% de humedad tanto

para invierno como verano; sin embargo, en invierno se observan que las mayores humedades

abarcan superficies más grandes del área de estudio.

**Figura N° 24. Humedad relativa, área modelación 62 x 62 km año 2014, periodo de verano, régimen**

**diurno.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

28

**Figura N° 25. Humedad relativa, área modelación 62 x 62 km año 2014, periodo de verano, régimen**

**nocturno.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

29

**Figura N° 26. Humedad relativa, área modelación 62 x 62 km año 2014, periodo de invierno, régimen**

**diurno.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

30

**Figura N° 27. Humedad relativa, área modelación 62 x 62 km año 2014, periodo de invierno, régimen**

**nocturno.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

31

**3.3.10 Radiaciones**

A continuación, en la Figura N° 28 y Figura N° 29, se observa que la radiación solar es mayor en

periodo de verano alcanzando una radiación superior a 777,8 W/m [2], la cual disminuye de manera

importante en periodo de invierno, donde la radiación apenas supera los 451,9 W/m [2] .

**Figura N° 28. Radiación solar, área modelación 62 x 62 km año 2014, periodo de verano.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

32

**Figura N° 29. Radiación solar, área modelación 62 x 62 km año 2014, periodo de invierno.**

Fuente: Elaboración propia mediante Calpuff View.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

33

**3.4** **RECEPTORES CONTEMPLADOS EN LA MODELACIÓN.**

**3.4.1** **Receptores Discretos (Estaciones de Monitoreo)**

Luego de revisar en el Sistema Nacional de Calidad del Aire (SINCA) del Ministerio del Medio Ambiente,

se observó que la estación de monitoreo de calidad del aire más cercana al proyecto se encuentra

ubicada en la comuna de Alto Hospicio a más de 36 kilómetros del proyecto y corresponde a la única

estación con información pública en la Región de Tarapacá.

Debido a lo anterior, se realizó una revisión en el Sistema de Evaluación de Impacto Ambiental (SEIA),

encontrándose datos de MP10, MP2,5 y SO 2 correspondientes a la estación "Pozo Almonte

COSAYACH", perteneciente a COSAYACH S.A., la cual fue instalada durante el periodo 23 de enero al 30

de julio del 2013 para la Declaración de Impacto Ambiental del Proyecto "Aumento Producción Cala

Cala, SCM COSAYACH" aprobado mediante RCA N°91/2013. En virtud a lo anterior se utilizó la

información de la estación "Pozo Almonte COSAYACH" entregada en dicha DIA, ya que es la más

cercana al proyecto, a unos 3,7 kilómetros aproximadamente. La siguiente tabla presenta las

coordenadas UTM de la estación.

**Tabla N° 2. Coordenadas UTM de estación Pozo Almonte COSAYACH.**

|Estación de Monitoreo|Coordenadas UTM, Huso 19 Sur, Datum WGS-84|Col3|
|---|---|---|
|**Estación de Monitoreo**|**Este (m)**|**Norte (m)**|
|Pozo Almonte COSAYACH|417.709 m E|7.760.605 m N|

Fuente: Elaboración propia en base a DIA "Aumento Producción Cala-Cala, SCM COSAYACH", 2013.

##### 3.4.2 Receptores Sensibles

Los receptores contemplados dentro de la modelación corresponde a receptores sensibles desde el

punto de vista de la población circundante y recursos naturales, lo cuales se presentan en la Figura N°

30.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

34

**Figura N° 30. Receptores sensibles cercanos al proyecto.**

Fuente: Elaboración propia, Google Earh Pro.

En la Tabla N° 3 se presentan las coordenadas UTM donde se encuentran ubicados los receptores

sensibles al proyecto:

**Tabla N° 3. Ubicación de Receptores sensibles respecto al proyecto.**

|N°|Receptores|Coordenadas UTM, Huso 19 Sur, Datum WGS-84|Col4|Distancia al<br>Proyecto (m)|
|---|---|---|---|---|
|**N°**|**Receptores**|**Norte (m)**|**Este (m)**|**Este (m)**|
|1|Vegetación y cultivos agrícolas|419.864|7.760.359|1600|
|2|Población cercana|419.114|7.759.440|2112|
|3|Plaza de Pozo Almonte|418.282|7.759.714|2957|
|4|Centro de Salud|418.007|7.759.732|3229|
|5|Establecimiento Educacional|417.994|7.759.434|3242|
|6|Cultivos Agrícolas|419.090|7.757.804|2748|
|7|Cultivos Agrícolas|419.385|7.757.023|3125|

Fuente: Elaboración propia mediante Google Earh Pro.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

35

#### 4 MARCO LEGAL

##### 4.1 ASPECTOS GENERALES

En Chile existen normas primarias de calidad y normas secundarias de calidad.

La Norma Primaria de Calidad Ambiental es “ _aquella que establece los valores de las concentraciones y_

_períodos, máximos o mínimos permisibles de elementos, compuestos, sustancias, derivados químicos o_

_biológicos, energías, radiaciones, vibraciones, ruidos o combinación de ellos, cuya presencia o carencia_

_en el ambiente pueda constituir un riesgo para la vida o la salud de la población_ ” (Art 2 LBGMA [1] ).

La Norma Secundaria de Calidad Ambiental es “ _aquella que establece los valores de las_

_concentraciones y períodos, máximos o mínimos permisibles de sustancias, elementos, energía o_

_combinación de ellos, cuya presencia o carencia en el ambiente pueda constituir un riesgo para la_

_protección o la conservación del medio ambiente, o la preservación de la naturaleza_ ” (Art 2 LBGMA).

Las normas de calidad, tienen como objetivo servir para definir si existe riesgo sobre la población

(normas primarias) y/o efectos adversos significativos sobre los recursos naturales renovables

incluidos suelo, agua y aire (normas secundarias). De esta manera, las normas primarias y secundarias

tienen como objetivo:

1. Declarar zonas latentes (cuando la concentración ambiental supere el 80% del límite

establecido en una norma de calidad) y zonas saturadas (cuando la concentración ambiental

supere el límite establecido en una norma de calidad). Declarada una zona latente o saturada,

mediante Decreto Supremo, se deberá generar un Plan de Prevención y/o Descontaminación

que regulará las actividades que se encuentran al interior de la zona declarada latente o

saturada.

2. Indicar cuándo un proyecto debe mitigar, reparar y/o compensar sus impactos por ser

significativos.

_1_ _Ley 19.300 sobre Bases Generales del Medio Ambiente_

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

36

##### 4.2 NORMAS DE CALIDAD DEL AIRE

La siguiente tabla muestra los límites establecidos por las normas de calidad aplicables en la

localización del proyecto.

**Tabla N° 4: Normas de Calidad del Aire Consideradas en la Modelación.**

|Parámetro|Norma|Estadístico|Valor|Normativa<br>aplicable|
|---|---|---|---|---|
|MP10|Primaria|Promedio Anual|50 μg/m3N|D.S. N°59/98<br>MINSEGPRES|
|MP10|Primaria|Percentil 98 de 24 horas|150 μg/m3N|150 μg/m3N|
|MP2.5|Primaria|Promedio Anual|20 μg/m3N|D.S. N°12/11<br>MMA|
|MP2.5|Primaria|Percentil 98 de 24 horas|50 μg/m3N|50 μg/m3N|
|SO2|Primaria|Promedio Anual|80 μg /m3N|D.S. N°113/02<br>MINSEGPRES|
|SO2|Primaria|Percentil 99 de 24 horas|250 μg/m3N|250 μg/m3N|
|SO2|Secundaria|Promedio Anual|80 μg /m3N|D.S. N° 22/10<br>MINSEGPRES|
|SO2|Secundaria|Percentil 99,7 de 24<br>horas|365 μg/m3N|365 μg/m3N|
|SO2|Secundaria|Percentil 99,73 de 24<br>horas|1000 μg/m3N|1000 μg/m3N|
|CO|Primaria|Percentil 99 de 1 hora|30.000 μg/m3N|D.S. N° 115/02<br>MINSEGPRES|
|CO|Primaria|Percentil 99 de 8 horas|10.000 μg/m3N|10.000 μg/m3N|
|NO2|Primaria|Promedio Anual|100 μg/m3N|D.S. N°114/02<br>MINSEGPRES|
|NO2|Primaria|Percentil 99 de 1 hora|400 μg/m3N|400 μg/m3N|

Fuente: Elaboración Propia

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

37

#### 5 LINEA DE BASE DE CALIDAD DEL AIRE

##### 5.1 CONCENTRACIONES DE ESTACIÓN DE MONITOREO DE CALIDAD DEL AIRE

Para determinar la línea de base con la cual verificar el cumplimiento de la normativa legal aplicable,

se utilizaron los resultados de los monitoreos de calidad del aire realizados por COSAYACH S.A., cuyos

registros fueron obtenidos por la estación "Pozo Almonte COSAYACH".

En la Tabla N° 5 se entrega un análisis de los estadísticos a partir de los datos medidos por la estación

Pozo Almonte COSAYACH para el periodo enero 2013 - julio 2013, para los parámetros MP 10, MP 2.5 y

SO 2 .

Según los resultados obtenidos se tiene que los parámetros analizados en la estación de monitoreo

cumplen con la normativa ambiental asociada a cada uno de ellos.

**Tabla N° 5: Concentraciones establecidas a partir de los datos de la Estación Pozo Almonte para el**

**periodo enero 2013 - julio 2013.**

|Parámetro|Estadístico|Línea Base|Norma|Unidad|% Norma|Cumple Normativa|
|---|---|---|---|---|---|---|
|MP10|Promedio<br>anual|65,0|50|μg/m3N|130,0%|No|
|MP10|Percentil 98<br>de 24 horas|108,0|150|μg/m3N|72,0%|Si|
|MP2,5|Promedio<br>anual|22,8|20|μg/m3N|114,0%|No|
|MP2,5|Percentil 98<br>de 24 horas|47,0|50|μg/m3N|94,0%|Si|
|SO2|Percentil 99<br>de 24 horas|16,0|250|μg/m3N|6,4%|Si|
|SO2|Percentil 99,7<br>de 24 horas|17,0|365|μg/m3N|4,7%|Si|
|SO2|Percentil<br>99,73 horario|103|1000|μg/m3N|10,3%|Si|
|SO2|Promedio<br>anual2|-|80|μg/m3N|-|-|

Fuente: DIA "Aumento Producción Cala-Cala, SCM COSAYACH", 2013.

_2_ _Estadístico no posible de calcular, debido a la baja cantidad de registros de la estación._

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

38

##### 5.2 ANÁLISIS ANUAL Y ESTACIONAL

**5.2.1** **Material Particulado Respirable (MP** **10** **)**

A continuación se presentan en el Gráfico N° 1 las concentraciones medias diarias para MP 10, de la

estación de monitoreo de calidad del aire "Pozo Almonte COSAYACH".

El límite de la norma primaria de calidad del aire (D.S. N° 59/98), para el contaminante Material

Particulado Respirable MP 10, es 150 μg/m [3] N para el Percentil 98 de las concentraciones de 24 horas

registradas durante un período anual en cualquier estación monitora clasificada como EMRP [3] . Por otra

parte, se establece para el promedio anual un límite máximo de 50 μg/m [3] N, declarándose saturación

cuando el promedio de 3 años continuos supere dicho valor.

Al observar las concentraciones diarias de la estación de monitoreo Pozo Almonte COSAYACH y según

el análisis realizado anteriormente se tiene que la calidad del aire en dicha estación se encontraría en

condiciones de saturación, según el promedio anual de 65 μg/m [3] N, el cual sobrepasa el máximo

permitido de 50 μg/m [3] N como periodo anual, no obstante se aclara que la estación no registró el año

completo ni por los tres años indicados en la norma, por lo que esta información es sólo referencial y

no se puede evaluar correctamente la normativa.

**Gráfico N° 1: Concentraciones diarias (μg/m** **[3]** **) de MP** **10,** **Estación Pozo Almonte COSAYACH.**

Fuente: DIA "Aumento Producción Cala-Cala, SCM COSAYACH", 2013.

_3_ _Estación de Monitoreo con Representatividad Poblacional._

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

39

Como se puede observar del Gráfico N° 1, las mayores concentraciones ocurren en los meses de

verano y comienzos de otoño (enero - abril), coincidente con el periodo de mayores velocidades de

viento en la zona (ver Figura N° 11), con una concentración máxima de 101 μg/m [3] N en abril, por otro

lado, el percentil 98 para este periodo es de 108 μg/m3N, el cual se encuentra bajo el límite de 150

μg/m [3] N que establece la norma respectiva.

**5.1.2** **Material Particulado Fino (MP** **2,5** **)**

A continuación se presenta en el Gráfico N° 2 las concentraciones medias diarias para MP 2,5, de la

estación de monitoreo de calidad del aire Pozo Almonte COSAYACH. La norma primaria de calidad del

aire (D.S. N° 11/12 del MMA), para el contaminante Material Particulado Fino MP 2,5, es 50 μg/m [3] N

para el Percentil 98 de las concentraciones de 24 horas registradas durante un período anual en

cualquier estación monitora clasificada como EMRP, se tendrá una condición de saturación cuando se

supere dicho límite, o cuando se supere el promedio anual de 3 años que es 20 μg/m [3] N.

Al observar las concentraciones de la estación Pozo Almonte COSAYACH y según el análisis realizado

anteriormente se tiene que la calidad del aire en dicha estación se encontraría en condiciones de

saturación, según el promedio anual de 22,8 μg/m [3] N, el cual sobrepasa el máximo permitido de 20

μg/m [3] N como periodo anual, no obstante se aclara que la estación no registró el año completo ni 3

años consecutivos, por lo que esta información es solo referencial y no se puede evaluar

correctamente la normativa.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

40

**Gráfico N° 2: Concentraciones diarias (μg/m** **[3]** **N) de MP** **2,5,** **Estación Pozo Almonte COSAYACH.**

Fuente: DIA "Aumento Producción Cala-Cala, SCM COSAYACH", 2013.

Como se puede observar en el Gráfico N° 2, las mayores concentraciones ocurren en los meses de

verano, coincidente con el periodo de mayores velocidades de viento en la zona (ver Figura N° 11), con

una concentración máxima de 59 μg/m [3] N en marzo, por otro lado, el percentil 98 para este periodo es

de 47 μg/m [3] N, el cual se encuentra bajo el límite de 50 μg/m [3] N que establece la norma respectiva.

**5.2.2** **Dióxido de Azufre (SO** **2** **)**

Las concentraciones diarias de SO 2 medidas por la Estación Pozo Almonte COSAYACH durante el

periodo enero - julio del 2013, dieron como resultado un percentil 99 de 16 μg/m [3] N, estando en

conformidad con el límite de 250 μg/m [3] N establecido por la norma primaria (D.S. N°113/2002

MINSEGPRES).

Luego para el caso de la norma secundaria, el percentil 99,7 de 24 horas correspondió a 17 μg/m [3] N,

valor que se encuentra en conformidad con el límite de 365 μg/m [3] N establecido por el D.S. N°22/2010

del MINSEGPRES. De igual forma, el percentil 99,73 de las concentraciones horarias correspondió a

103 μg/m [3] N, valor que se encuentra bastante bajo los 1.000 μg/m [3] N que establece la norma

secundaria.

Para el caso del promedio anual, debido a la cantidad de datos registrados por la estación, no fue

posible calcular este valor. No obstante, se debe recordar que debido a que la estación solo midió de

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

41

enero a julio de 2013, el análisis realizado es sólo referencial y no se puede evaluar de manera formal

el cumplimiento de las normas de calidad.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

42

#### 6 DESCRIPCIÓN DE LAS FUENTES EMISORAS

Las fuentes consideradas en la modelación son las presentes en la etapa de construcción del proyecto.

Cabe destacar que se decidió modelar la construcción por ser la etapa del proyecto donde se genera

mayor emisión de contaminantes.

**6.1** **UBICACIÓN DE FUENTES DE EMISIÓN**

En la Tabla N° 6 y Tabla N° 7 se presentan las coordenadas UTM que indican la localización de las

fuentes del proyecto consideradas en la modelación de dispersión atmosférica de contaminantes. Para

el caso de las fuentes móviles, se ha asignado una ubicación representativa del área en la que se

encontrará, mientras que las fuentes areales (Tabla N° 7) fueron definidas según las zonas en que se

ejecutarán trabajos de excavación y movimientos de tierra.

**Tabla N° 6: Ubicación de Fuentes Emisoras Puntuales.**

|No|Fuente Puntuales|Coordenadas UTM, Huso 19 Sur, Datum WGS- 84|Col4|
|---|---|---|---|
|**No**|**Fuente Puntuales**|**Norte (m)**|**Este (m)**|
|1|Equipo Electrógeno Diesel|421.228|7.759.504|
|2|Vehículo N°1|421.239|7.759.520|
|3|Vehículo N°2|421.238|7.759.501|
|4|Vehículo N°3|421.238|7.759.480|
|5|Vehículo N°4|421.237|7.759.459|
|6|Vehículo N°5|421.236|7.759.437|
|7|Bulldozer|421.268|7.759.416|
|8|Retroexcavadora|421.281|7.759.427|
|9|Excavadora|421.273|7.759.456|
|10|Motoniveladora|421.266|7.759.519|
|11|Grúa|421.289|7.759.517|
|12|Camión Pluma|421.250|7.759.426|
|13|Rodillo Compactador|421.307|7.759.517|

Fuente: Elaboración Propia

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

43

**Tabla N° 7: Ubicación de Fuentes Emisoras Areales.**

|No|Fuente Areal|Vértice|Coordenadas UTM, Huso 19 Sur, Datum WGS- 84|Col5|
|---|---|---|---|---|
|**No**|**Fuente Areal**|**Vértice**|**Norte (m)**|**Este (m)**|
|1|Escarpe|a|421.242|7.759.392|
|1|Escarpe|b|421.316|7.759.388|
|1|Escarpe|c|421.245|7.759.526|
|1|Escarpe|d|421.320|7.759.523|
|2|Excavación y<br>transferencia de<br>material|a|421.251|7.759.437|
|2|Excavación y<br>transferencia de<br>material|b|421.313|7.759.435|
|2|Excavación y<br>transferencia de<br>material|c|421.253|7.759.512|
|2|Excavación y<br>transferencia de<br>material|d|421.316|7.759.509|
|3|Erosión de material en<br>pilas|a|421.202|7.759.459|
|3|Erosión de material en<br>pilas|b|421.220|7.759.459|
|3|Erosión de material en<br>pilas|c|421.202|7.759.476|
|3|Erosión de material en<br>pilas|d|421.219|7.759.476|
|4|Circulación en<br>vehículos en vías no<br>pavimentadas|a|421.235|7.759.428|
|4|Circulación en<br>vehículos en vías no<br>pavimentadas|b|421.238|7.759.428|
|4|Circulación en<br>vehículos en vías no<br>pavimentadas|c|421.238|7.759.525|
|4|Circulación en<br>vehículos en vías no<br>pavimentadas|d|421.242|7.759.525|

Fuente: Elaboración Propia

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

44

**6.2** **TASAS DE EMISIÓN**

En la Tabla N° 8 y Tabla N° 9, se resume la tasa de emisión de los contaminantes y las características

físicas y operacionales de cada fuente emisora.

**Tabla N° 8: Características y tasas de emisión de contaminantes de fuentes puntuales.**

|Fuente Puntual|Altura<br>emisión (m)|Diámetro interno<br>Ducto (m)|Vel. Salida<br>Gases (m/s)|Temperatura Salida<br>Gases (K)|Contaminante|Emisiones (kg/h)|
|---|---|---|---|---|---|---|
|Equipo<br>Electrógeno (110<br>kW)|2,0|0,15|72,58|796,8|CO|0,260|
|Equipo<br>Electrógeno (110<br>kW)|2,0|0,15|72,58|796,8|NOx|1,202|
|Equipo<br>Electrógeno (110<br>kW)|2,0|0,15|72,58|796,8|MP10|0,042|
|Equipo<br>Electrógeno (110<br>kW)|2,0|0,15|72,58|796,8|MP2,5|0,010|
|Equipo<br>Electrógeno (110<br>kW)|2,0|0,15|72,58|796,8|SOx|0,064|
|Vehículo N°1|1,5|0,14|99,74|718,15|CO|0,00334|
|Vehículo N°1|1,5|0,14|99,74|718,15|NOx|0,01825|
|Vehículo N°1|1,5|0,14|99,74|718,15|MP10|0,00035|
|Vehículo N°1|1,5|0,14|99,74|718,15|MP2,5|0,00034|
|Vehículo N°1|1,5|0,14|99,74|718,15|SOx|0,000003|
|Vehículo N°2|1,5|0,14|99,74|718,15|CO|0,00334|
|Vehículo N°2|1,5|0,14|99,74|718,15|NOx|0,01825|
|Vehículo N°2|1,5|0,14|99,74|718,15|MP10|0,00035|
|Vehículo N°2|1,5|0,14|99,74|718,15|MP2,5|0,00034|
|Vehículo N°2|1,5|0,14|99,74|718,15|SOx|0,000003|
|Vehículo N°3|1,5|0,14|99,74|718,15|CO|0,00334|
|Vehículo N°3|1,5|0,14|99,74|718,15|NOx|0,01825|
|Vehículo N°3|1,5|0,14|99,74|718,15|MP10|0,00035|
|Vehículo N°3|1,5|0,14|99,74|718,15|MP2,5|0,00034|
|Vehículo N°3|1,5|0,14|99,74|718,15|SOx|0,000003|
|Vehículo N°4|1,5|0,14|99,74|718,15|CO|0,00334|
|Vehículo N°4|1,5|0,14|99,74|718,15|NOx|0,01825|
|Vehículo N°4|1,5|0,14|99,74|718,15|MP10|0,00035|
|Vehículo N°4|1,5|0,14|99,74|718,15|MP2,5|0,00034|
|Vehículo N°4|1,5|0,14|99,74|718,15|SOx|0,000003|
|Vehículo N°5|1,5|0,14|99,74|718,15|CO|0,00334|
|Vehículo N°5|1,5|0,14|99,74|718,15|NOx|0,01825|
|Vehículo N°5|1,5|0,14|99,74|718,15|MP10|0,00035|
|Vehículo N°5|1,5|0,14|99,74|718,15|MP2,5|0,00034|
|Vehículo N°5|1,5|0,14|99,74|718,15|SOx|0,000003|
|Bulldozer|3,0|0,14|99,74|718,15|CO|0,0210|
|Bulldozer|3,0|0,14|99,74|718,15|NOx|0,2777|
|Bulldozer|3,0|0,14|99,74|718,15|MP10|0,03442|
|Bulldozer|3,0|0,14|99,74|718,15|MP2,5|0,03338|
|Bulldozer|3,0|0,14|99,74|718,15|SOx|0,0007|

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

45

|Fuente Puntual|Altura<br>emisión (m)|Diámetro interno<br>Ducto (m)|Vel. Salida<br>Gases (m/s)|Temperatura Salida<br>Gases (K)|Contaminante|Emisiones (kg/h)|
|---|---|---|---|---|---|---|
|Retroexcavadora|3,0|0,14|99,74|718,15|CO|0,0210|
|Retroexcavadora|3,0|0,14|99,74|718,15|NOx|0,2777|
|Retroexcavadora|3,0|0,14|99,74|718,15|MP10|0,03442|
|Retroexcavadora|3,0|0,14|99,74|718,15|MP2,5|0,03338|
|Retroexcavadora|3,0|0,14|99,74|718,15|SOx|0,0007|
|Excavadora|3,0|0,14|99,74|718,15|CO|0,0174|
|Excavadora|3,0|0,14|99,74|718,15|NOx|0,2301|
|Excavadora|3,0|0,14|99,74|718,15|MP10|0,04182|
|Excavadora|3,0|0,14|99,74|718,15|MP2,5|0,04057|
|Excavadora|3,0|0,14|99,74|718,15|SOx|0,0007|
|Motoniveladora|3,0|0,14|99,74|718,15|CO|0,0239|
|Motoniveladora|3,0|0,14|99,74|718,15|NOx|0,3189|
|Motoniveladora|3,0|0,14|99,74|718,15|MP10|0,02796|
|Motoniveladora|3,0|0,14|99,74|718,15|MP2,5|0,02712|
|Motoniveladora|3,0|0,14|99,74|718,15|SOx|0,0007|
|Grúa|4,0|0,14|99,74|718,15|CO|0,0054|
|Grúa|4,0|0,14|99,74|718,15|NOx|0,0530|
|Grúa|4,0|0,14|99,74|718,15|MP10|0,00690|
|Grúa|4,0|0,14|99,74|718,15|MP2,5|0,00670|
|Grúa|4,0|0,14|99,74|718,15|SOx|0,0007|
|Camión Pluma|3,0|0,14|99,74|718,15|CO|0,0350|
|Camión Pluma|3,0|0,14|99,74|718,15|NOx|0,4639|
|Camión Pluma|3,0|0,14|99,74|718,15|MP10|0,05749|
|Camión Pluma|3,0|0,14|99,74|718,15|MP2,5|0,05576|
|Camión Pluma|3,0|0,14|99,74|718,15|SOx|0,0007|
|Rodillo<br>Compactador|2,5|0,14|99,74|718,15|CO|0,0210|
|Rodillo<br>Compactador|2,5|0,14|99,74|718,15|NOx|0,2777|
|Rodillo<br>Compactador|2,5|0,14|99,74|718,15|MP10|0,03442|
|Rodillo<br>Compactador|2,5|0,14|99,74|718,15|MP2,5|0,03338|
|Rodillo<br>Compactador|2,5|0,14|99,74|718,15|SOx|0,0007|

Fuente: Informe de Cálculo de Emisiones DIA Sistema de Tratamiento de Agua Potable El Carmelo

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

46

**Tabla N° 9: Tasas de emisión de contaminantes de fuentes emisoras areales.**

|Fuente Areal|Contaminante|Emisiones (kg/h/m2)|
|---|---|---|
|Escarpe|MP10|1,05E-05|
|Excavación y transferencia de material|MP10|4,11E-05|
|Excavación y transferencia de material|MP2.5|2,03E-05|
|Erosión de Pilas de Acopio|MP10|5,83E-05|
|Erosión de Pilas de Acopio|MP2.5|8,60E-06|
|Circulación en vehículos en vías no<br>pavimentadas|MP10|1,63E-05|
|Circulación en vehículos en vías no<br>pavimentadas|MP2.5|1,63E-04|

Fuente: Informe de Cálculo de Emisiones DIA Sistema de Tratamiento de Agua Potable El Carmelo

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

47

#### 7 APORTES DEL PROYECTO A LAS CONCENTRACIONES ATMOSFÉRICAS

Con la información ingresada en el modelo Calpuff, se procedió a establecer los aportes al aire de los

contaminantes considerados sobre la estación de monitoreo, los receptores discretos sensibles, tales

como viviendas, escuelas, plazas, centros de salud, etc., y en el punto de mayor concentración o punto

de máximo impacto (PMI).

En la Tabla N° 10 se muestra el aporte a las concentraciones ambientales en los puntos de máximo

impacto (PMI) determinados a través de la modelación de calidad del aire para los parámetros MP 10,

MP 2,5, SO 2, NO x y CO con el software Calpuff View.

**Tabla N° 10: Aporte del proyecto a la concentración ambiental en el PMI (μg/m** **[3]** **N).**

|Contaminante|Estadístico|Aporte<br>(μg/m3N)|Norma<br>(μg/m3N)|% Norma|Distancia del Proyecto (km)|
|---|---|---|---|---|---|
|MP10|Promedio Anual|0,273|50|0,55%|0,6 km al SE|
|MP10|Percentil 98 de<br>24 horas|2,645|150|1,76%|0,6 km al SE|
|MP2.5|Promedio Anual|0,048|20|0,24%|0,6 km al SE|
|MP2.5|Percentil 98 de<br>24 horas|0,225|50|0,45%|0,6 km al SE|
|NO2|Promedio<br>Anual|0,295|100|0,30%|0,6 km al SE|
|NO2|Percentil 99 de<br>1 hora|17,792|400|4,45%|0,8 km al NO|
|SO2|Promedio<br>Anual|0,008|80|0,01%|0,6 km al SE|
|SO2|Percentil 99 de<br>24 horas|0,054|250|0,22%|0,6 km al SE|
|SO2|Percentil 99,7<br>de 24 horas|0,084|365|0,02%|0,8 km al NO|
|SO2|Percentil 99,73<br>horario|0,364|1000|0,04%|0,8 km al NO|
|CO|Percentil 99 de<br>1 hora|3,150|10000|0,03%|0,8 km al NO|
|CO|Percentil 99 de<br>8 horas|0,549|30000|0,002%|0,8 km al NO|

Fuente: Elaboración Propia

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

48

Luego del análisis de los datos presentados en la tabla anterior, es posible indicar que las emisiones del

Proyecto que han sido proyectadas en los PMI representan un porcentaje muy bajo de los valores

máximos establecidos en las normas de calidad respectivas, ya que para el caso del MP 10 el aporte

máximo corresponde a 1,76 % de la norma (Percentil 98 de 24 horas), para el caso del MP 2,5 el aporte

máximo corresponde a 0,45 % de la norma (Percentil 98 de 24 horas), para el caso del NO 2 el aporte

máximo corresponde a un 4,45 % de la norma (Percentil 99 de 1 hora), para el CO el aporte máximo

corresponde a un 0,03 % de la norma (Percentil 99 de 1 hora) y para el SO 2 el aporte máximo

corresponde a un 0,22 % de la norma (Percentil 99 de 24 horas).

En las Tabla N° 11, Tabla N° 12, Tabla N° 13, Tabla N° 14 y Tabla N° 15, se presentan los resultados de

los aportes del Proyecto sobre los receptores sensibles desde el punto de vista de la población

circundante y recursos naturales, para MP 10, MP 2,5, SO 2, NO 2 y CO. Estos receptores se encuentran

dentro de un radio de 4 km desde las fuentes de emisión.

**Tabla N° 11: Aporte del proyecto a la concentración ambiental de MP** **10** **sobre receptores sensibles**
**(**  **g/m** **[3]** **N).**

|N°|Receptor|Promedio Anual<br>(g/m3N)|% Norma Anual|Percentil 98 de 24<br>horas (g/m3N)|% Norma<br>Diaria|Normativa<br>Anual / Diaria<br>(g/m3N)|
|---|---|---|---|---|---|---|
|1|Vegetación y<br>cultivos agrícolas|0,0081|0,016%|0,064|0,043%|50/150|
|2|Población cercana|0,0048|0,010%|0,044|0,029%|50/150|
|3|Plaza de Pozo<br>Almonte|0,0025|0,005%|0,022|0,015%|50/150|
|4|Centro de Salud|0,0021|0,004%|0,017|0,011%|50/150|
|5|Establecimiento<br>Educacional|0,0021|0,004%|0,016|0,011%|50/150|
|6|Cultivos Agrícolas|0,0034|0,007%|0,025|0,017%|50/150|
|7|Cultivos Agrícolas|0,0031|0,006%|0,018|0,012%|50/150|

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

49

**Tabla N° 12: Aporte del proyecto a la concentración ambiental de MP** **2,5** **sobre receptores sensibles**
**(**  **g/m** **[3]** **N).**

|N°|Receptor|Promedio Anual<br>(g/m3N)|% Norma<br>Anual|Percentil 98 de 24<br>horas (g/m3N)|% Norma<br>Diaria|Normativa<br>Anual / Diaria<br>(g/m3N)|
|---|---|---|---|---|---|---|
|1|Vegetación y<br>cultivos agrícolas|0,0023|0,012%|0,0170|0,034%|20/50|
|2|Población cercana|0,0013|0,007%|0,0102|0,020%|20/50|
|3|Plaza de Pozo<br>Almonte|0,0008|0,004%|0,0063|0,013%|20/50|
|4|Centro de Salud|0,0007|0,004%|0,0055|0,011%|20/50|
|5|Establecimiento<br>Educacional|0,0007|0,004%|0,0057|0,011%|20/50|
|6|Cultivos Agrícolas|0,0011|0,006%|0,0071|0,014%|20/50|
|7|Cultivos Agrícolas|0,0011|0,006%|0,0067|0,013%|20/50|

**Tabla N° 13: Aporte del proyecto a la concentración ambiental de NO** **2** **sobre receptores sensibles**
**(**  **g/m** **[3]** **N).**

|N°|Receptor|Promedio Anual<br>(g/m3N)|% Norma<br>Anual|Percentil 99<br>horario (g/m3N)|% Norma<br>Horaria|Normativa<br>Anual / Horaria<br>(g/m3N)|
|---|---|---|---|---|---|---|
|1|Vegetación y<br>cultivos agrícolas|0,026|0,026%|2,531|0,63%|100/400|
|2|Población cercana|0,015|0,015%|1,404|0,35%|100/400|
|3|Plaza de Pozo<br>Almonte|0,008|0,008%|0,698|0,17%|100/400|
|4|Centro de Salud|0,007|0,007%|0,703|0,18%|100/400|
|5|Establecimiento<br>Educacional|0,007|0,007%|0,639|0,16%|100/400|
|6|Cultivos Agrícolas|0,012|0,012%|1,131|0,28%|100/400|
|7|Cultivos Agrícolas|0,011|0,011%|0,774|0,19%|100/400|

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

50

**Tabla N° 14. Aporte del proyecto a la concentración ambiental de CO sobre receptores sensibles**
**(**  **g/m** **[3]** **N).**

|N°|Receptor|Percentil 99 de 8<br>horas (g/m3N)|% Norma 8<br>horas|Percentil 99 de 1<br>hora (g/m3N)|% Norma 1<br>hora|Normativa 8<br>horas / 1 hora<br>(g/m3N)|
|---|---|---|---|---|---|---|
|1|Vegetación y cultivos agrícolas|0,102|0,0010%|0,526|0,0018%|10000/30000|
|2|Población cercana|0,049|0,0005%|0,278|0,0009%|10000/30000|
|3|Plaza de Pozo Almonte|0,025|0,0003%|0,107|0,0004%|10000/30000|
|4|Centro de Salud|0,021|0,0002%|0,082|0,0003%|10000/30000|
|5|Establecimiento Educacional|0,020|0,0002%|0,077|0,0003%|10000/30000|
|6|Cultivos Agrícolas|0,035|0,0004%|0,162|0,0005%|10000/30000|
|7|Cultivos Agrícolas|0,029|0,0003%|0,135|0,0005%|10000/30000|

**Tabla N° 15. Aporte del proyecto a la concentración ambiental de SO** **2** **sobre receptores sensibles**
**(**  **g/m** **[3]** **N).**

|N°|Receptor|Per. 99,<br>24 h<br>(g/m3N)|%<br>Norma<br>primaria<br>24 h|Per. 99,7,<br>24h<br>(g/m3N)|% Norma<br>Secundaria<br>24 h|Per.<br>99,73, 1h<br>(g/m3N)|% Norma<br>secundaria<br>1 h|Promedio<br>anual<br>(g/m3N)|%<br>Norma<br>anual|Norma<br>Primaria<br>Anual / 24h<br>(g/m3N)|Norma<br>Secundaria<br>Anual / 24h /<br>1h (g/m3N)|
|---|---|---|---|---|---|---|---|---|---|---|---|
|1|Vegetación y<br>cultivos<br>agrícolas|0,0077|0,0031%|0,0115|0,0032%|0,050|0,0050%|0,00076|0,0010%|80/250|80/365/1000|
|2|Población<br>cercana|0,0038|0,0015%|0,0098|0,0027%|0,023|0,0023%|0,00039|0,0005%|80/250|80/365/1000|
|3|Plaza de Pozo<br>Almonte|0,0019|0,0008%|0,0034|0,0009%|0,012|0,0012%|0,00019|0,0002%|80/250|80/365/1000|
|4|Centro de Salud|0,0016|0,0006%|0,0021|0,0006%|0,009|0,0009%|0,00015|0,0002%|80/250|80/365/1000|
|5|Establecimiento<br>Educacional|0,0012|0,0005%|0,0022|0,0006%|0,010|0,0010%|0,00015|0,0002%|80/250|80/365/1000|
|6|Cultivos<br>Agrícolas|0,0027|0,0011%|0,0053|0,0015%|0,018|0,0018%|0,00028|0,0004%|80/250|80/365/1000|
|7|Cultivos<br>Agrícolas|0,0022|0,0009%|0,0030|0,0008%|0,015|0,0015%|0,00025|0,0003%|80/250|80/365/1000|

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

51

En la Tabla N° 11, Tabla N° 12, Tabla N° 13, Tabla N° 14 y Tabla N° 15, se puede apreciar que el aporte

del Proyecto sobre los receptores sensibles, desde el punto de vista de la población circundante y

recursos naturales, para los contaminantes MP 10, MP 2,5, NO 2, CO y SO 2, no es significativo, dado los

muy bajos aportes si se comparan a la normativa primaria y secundaria de calidad del aire, por lo cual

no provocará un aumento relativamente grande en las concentraciones ambientales de los

contaminantes normados.

En el Apéndice 1 se presentan las plumas de dispersión de la modelación del software Calpuff View,

donde es posible apreciar la concentración final para cada estadístico considerado en la modelación

para los contaminantes MP 10, MP 2,5, NO 2, CO y SO 2 .

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

52

#### 8. RESULTADOS DE MODELACIÓN EN ESTACIÓN DE MONITOREO

Para evaluar la calidad del aire resultante en la modelación, se utilizó como referencia la línea de base

(LB) de calidad del aire establecida para la estación Pozo Almonte COSAYACH.

A su vez, para conocer la incidencia del Proyecto sobre la línea de base de calidad del aire se sumaron

los aportes en concentración para los parámetros contaminantes considerados calculados por el

software Calpuff View.

En la Tabla N° 16 se analiza el cumplimiento normativo en relación a la concentración de los distintos

contaminantes en la estación de monitoreo Pozo Almonte COSAYACH, tomando como línea de base las

mediciones realizadas en dicha estación.

Cabe destacar que la estación solo midió MP 10, MP 2,5 y SO 2, sin embargo, para el caso del SO 2 no se

pudo calcular el promedio anual debido a la baja cantidad de registros.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

53

**Tabla N° 16: Concentración final esperada para Contaminantes en**
**Estación Pozo Almonte COSAYACH (**  **g/m** **[3]** **N).**

|Parámetro|Estadístico|Aporte<br>(g/m3N)|% Norma|Línea Base<br>(g/m3N)|Aporte +<br>Línea Base<br>(g/m3N)|Norma<br>(g/m3N)|% Norma<br>Final|
|---|---|---|---|---|---|---|---|
|MP10|Promedio Anual|0,0016|0,0032%|65,00|65,00|50|130,0%|
|MP10|Percentil 98 de<br>24 horas|0,0126|0,0084%|108,00|108,01|150|72,0%|
|MP2,5|Promedio Anual|0,0005|0,0025%|22,80|22,80|20|114,0%|
|MP2,5|Percentil 98 de<br>24 horas|0,0047|0,0094%|47,00|47,00|50|94,0%|
|NO2|Promedio<br>Anual|0,0054|0,0054%|-|-|100|-|
|NO2|Percentil 99 de<br>1 hora|0,515|0,1288%|-|-|400|-|
|SO2|Promedio Anual|0,00013|0,0002%|-|-|80|-|
|SO2|Percentil 99 de<br>24 horas|0,00134|0,0005%|16,00|16,00|250|6,4%|
|SO2|Percentil 99,7<br>de 24 horas|0,00236|0,0006%|17,00|17,00|365|4,7%|
|SO2|Percentil 99,73<br>de 1 hora|0,0116|0,0012%|103,00|103,01|1000|10,3%|
|CO|Percentil 99 de<br>1 hora (μg/m3)|0,071|0,0002%|-|-|30000|-|
|CO|Percentil 99 de<br>8 horas (μg/m3)|0,017|0,0002%|-|-|10000|-|

Luego del análisis de los datos presentados en la tabla anterior, es posible indicar que la suma de los

aportes en la estación Pozo Almonte calculados no modifica de manera considerable la línea de base

referencial establecida para los estadísticos, por lo que ninguno de estos aportes indica un riesgo para

la población y recursos naturales, ni una modificación significativa en los valores de línea base

registrados en la estación cercana al proyecto.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

54

#### 9. CONCLUSIONES

- Se realizó una modelación meteorológica para el lugar en el que se encuentra en proyecto con el

modelo numérico Weather Research and Forecasting Model (WRF)4. Entre las principales

conclusiones se tiene que los vientos predominantes en el área de estudio poseen principalmente

un componente Oeste - Noroeste (ONO) y Oeste (O), con predominancia de vientos que fluctúan

entre los 0,5 - 2,1 m/s.

- Junto a lo anterior, y utilizando la información meteorológica modelada, se efectuó una

modelación de la dispersión de contaminantes utilizando el software de modelación Calpuff View

que es el modelo recomendado de acuerdo a la “Guía para el Uso de Modelos de Calidad del Aire

en el SEIA” (SEA, 2013). Entre las conclusiones de dicho modelo destacan las siguientes:

 - El aporte de MP 10, MP 2.5, NO 2, SO 2 y CO en la estación de monitoreo, receptores sensibles

y en el punto de máximo impacto representa un aporte mínimo respecto a la normativa

vigente para cada contaminante.

 - Para el caso del MP 10 el aporte máximo corresponde a 1,76 % de la norma (Percentil 98 de

24 horas), para el caso del MP 2,5 el aporte máximo corresponde a 0,45 % de la norma

(Percentil 98 de 24 horas), para el caso del NO 2 el aporte máximo corresponde a un 4,45 %

de la norma (Percentil 99 de 1 hora), para el CO el aporte máximo corresponde a un 0,03

% de la norma (Percentil 99 de 1 hora) y para el SO 2 el aporte máximo corresponde a un

0,22 % de la norma (Percentil 99 de 24 horas).

Con los resultados obtenidos es posible afirmar que ninguno de estos aportes generados por el

proyecto constituye un riesgo a la salud de las personas o al estado de los recursos naturales, ni

tampoco una modificación significativa en los valores de línea de base registrados en la estación de

monitoreo tomada como referencia. Por otro lado, se debe destacar que adicionalmente se contará

con medidas de control y de abatimiento que se implementarán durante la construcción del proyecto

tales como la humectación de vías no pavimentadas, reduciendo en un 75% las emisiones de MP.

_4_ Modelo recomendado para la generación de datos meteorológicos. Es uno de los modelos meteorológicos de pronóstico más avanzados y

completos, el que es mantenido por NCAR/ NOAA de Estados Unidos.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

55

#### APÉNDICE 1 PLUMAS DE DISPERSIÓN DE CONTAMINANTES MODELADOS EN CALPUFF VIEW

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

56

**Figura 1. 1. Concentración MP10 promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View y Google Earth.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

**Figura 1. 2. Concentración MP10 percentil 98 diario (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View y Google Earth.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

**Figura 1.3. Concentración MP2,5 promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View y Google Earth.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

**Figura 1.4. Concentración MP2,5 percentil 98 de 24 horas (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View y Google Earth.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

**Figura 1.5. Concentración NO** **2** **promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View y Google Earth.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

**Figura 1.6. NO** **2** **máxima concentración horaria (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View y Google Earth.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

**Figura 1.7. CO máxima concentración de 8 horas (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View y Google Earth.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

**Figura 1.8. CO máxima concentración de 1 hora (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View y Google Earth.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

**Figura 1.9. Concentración SO** **2** **promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View y Google Earth.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

**Figura 1.10. Concentración SO** **2** **percentil 99 de 24 horas (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View y Google Earth.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

**Figura 1.11. Concentración SO** **2** **percentil 99,7 de 24 horas (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View y Google Earth.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**

**Figura 1.12. SO** **2** **máxima concentración de 1 hora (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View y Google Earth.

**Marco Polo 8939 Hualpén-Concepción**
**Fono (56-41) 2908700**
**Fax (56-41) 2908701**
**E mail:** **info@pyaing.cl**