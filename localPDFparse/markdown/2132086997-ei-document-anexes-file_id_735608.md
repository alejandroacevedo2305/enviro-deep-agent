---
title: Sin título
author: HP Pavilion
date: D:20170113164317-03'00'
language: es
type: report
pages: 100
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Modelación de Dispersión Atmosférica
-->

Planta de Reciclaje de Aceites, Caucho y Plásticos Fuera

de Uso

Declaración de Impacto Ambiental

## Anexo 21: Modelación de Emisiones

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

### Planta de Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

# Modelación de Dispersión Atmosférica

Haga clic aquí para escribir texto.

Sebastián Marín Obreque

Ingeniero Ambiental

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**INDICE DE CONTENIDOS**

1 Antecedentes Generales ............................................................................................................. 1

2 Modelo Utilizado para Realizar Simulación de Dispersión Atmosférica de Contaminantes ....... 2

3 Caracterización del Área de Modelación .................................................................................... 7

3.1 Antecedentes Generales ..................................................................................................... 7

3.2 Variables de Superficie Consideradas ................................................................................. 8

3.2.1 Topografía ................................................................................................................... 8

3.2.2 Uso de Suelo .............................................................................................................. 10

3.3 Variables Meteorológicas .................................................................................................. 11

3.3.1 Meteorología de Superficie de Altura ....................................................................... 11

3.3.2 Dirección y Velocidad del Viento............................................................................... 13

3.3.3 Mapas Campos de vientos dentro del dominio de la modelación ............................ 17

3.3.4 Mapas de altura de mezclado dentro del dominio de modelación .......................... 21

3.3.5 Temperatura del aire superficial ............................................................................... 25

3.3.6 Humedad Relativa ..................................................................................................... 29

3.3.7 Precipitaciones .......................................................................................................... 33

3.3.8 Radiaciones ............................................................................................................... 34

3.3.9 Análisis de incertidumbre del periodo modelado ..................................................... 36

3.3.10 Evaluación Cualitativa ............................................................................................... 36

3.3.11 Evaluación Cuantitativa ............................................................................................. 37

3.4 Receptores Contemplados en la Modelación ................................................................... 38

3.4.1 Estación de Monitoreo .............................................................................................. 38

3.4.2 Receptores Sensibles ................................................................................................. 39

Cerro El Plomo 5630 Oficina 1501 Marco Polo 8939

Las Condes, Santiago Hualpén, Concepción
(56) 227144000 (56) 412908700

b

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

4 Marco Legal ............................................................................................................................... 41

4.4 Aspectos Generales ........................................................................................................... 41

4.4.1 Normas de Calidad Ambiental ................................................................................... 41

4.4.2 Normas de Emisión ................................................................................................... 42

**4.5** **Normas de calidad del Aire Aplicables** ............................................................................ 43

**4.6** **Normas de Emisión Aplicables** ......................................................................................... 44

5 Línea de Base de Calidad del Aire ............................................................................................. 45

6 Descripción de la Fuente Emisora ............................................................................................. 46

6.4 Ubicación de la Fuente ...................................................................................................... 46

6.5 Variables Físicas y Operacionales Consideradas en la Modelación .................................. 47

6.5.1 Chimeneas de Hornos de Pirólisis ................................................................................. 48

6.5.2 Grupo Electrógeno de Emergencia ............................................................................... 49

6.5.3 Material Particulado Secundario ................................................................................... 49

7 Resultados de Modelación en los Receptores Discretos .......................................................... 50

8. Aporte del Proyecto a la Línea de Base de Calidad del Aire...................................................... 61

8.1 . Análisis de Cumplimiento Normativo en Estación de Monitoreo ................................... 61

8.2 . Análisis de Cumplimiento Normativo en Punto de Máximo Impacto ............................. 62

8 Conclusiones.............................................................................................................................. 63

Cerro El Plomo 5630 Oficina 1501 Marco Polo 8939

Las Condes, Santiago Hualpén, Concepción
(56) 227144000 (56) 412908700

c

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**INDICE DE FIGURAS**

F IGURA N° 1: R EPRESENTACIÓN G RÁFICA DEL M ODELO T IPO P UFF Y DE P LUMA . ............................................... 3

F IGURA N° 2: V ISTA G ENERAL DEL D OMINIO DE M ODELACIÓN . ....................................................................... 7

F IGURA N° 3: T OPOGRAFÍA C ONSIDERADA EN LA M ODELACIÓN . ..................................................................... 9

F IGURA N° 4: U SOS DE SUELO CONSIDERADO EN LA MODELACIÓN . ................................................................ 10

F IGURA N° 5. G RILLA METEOROLÓGICA WRF UTILIZADA PARA LA MODELACIÓN EN C ALPUFF . ............................ 12

F IGURA N° 6: R OSA DE V IENTOS OBTENIDA CON WRF PARA EL A ÑO 2012. .................................................... 13

F IGURA N° 7: R OSA DE VIENTOS EN CONTEXTO ESPACIAL PARA AÑO 2012. ..................................................... 14

F IGURA N° 8: G RÁFICO DE DISTRIBUCIÓN DE FRECUENCIA DE VIENTOS . ........................................................... 14

F IGURA N° 9: R OSAS DE VIENTO, P ERIODO P RIMAVERA -V ERANO, 2012. ........................................................ 15

F IGURA N° 10: R OSAS DE VIENTO, P ERIODO O TOÑO -I NVIERNO, 2012. .......................................................... 15

F IGURA N° 11: G RÁFICOS DE DISTRIBUCIÓN DE FRECUENCIA, P ERIODO P RIMAVERA -V ERANO, 2012. .................. 16

F IGURA N° 12: G RÁFICOS DE DISTRIBUCIÓN DE FRECUENCIA, P ERIODO O TOÑO -I NVIERNO, 2012. ...................... 16

F IGURA N° 13. M APA DE VIENTO DE ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN NOCTURNO, VERANO, 2012,

MODELADO CON WRF (01-01-2012 03:00 AM ). ...................................................................................... 17

F IGURA N° 14. M APA DE VIENTO ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN DIURNO, VERANO, 2012, MODELADO

CON WRF (01-01-2012 03:00 PM ). ....................................................................................................... 18

F IGURA N° 15. M APA DE VIENTO ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN NOCTURNO, INVIERNO, 2012,

MODELADO CON WRF (07-07-2012 03:00 AM ). ...................................................................................... 19

F IGURA N° 16. M APA DE VIENTO ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN DIURNO, INVIERNO, 2012, MODELADO

CON WRF (07-07-2012 03:00 PM ). ....................................................................................................... 20

F IGURA N° 17. M APA DE ALTURA DE MEZCLA, ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN NOCTURNO, PERIODO

PRIMAVERA - VERANO, 2012. ................................................................................................................... 21

F IGURA N° 18. M APA DE ALTURA DE MEZCLA, ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN DIURNO, PERIODO

PRIMAVERA - VERANO 2012. .................................................................................................................... 22

F IGURA N° 19. M APA DE ALTURA DE MEZCLA, ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN NOCTURNO, PERIODO

OTOÑO - INVIERNO 2012. ........................................................................................................................ 23

Cerro El Plomo 5630 Oficina 1501 Marco Polo 8939

Las Condes, Santiago Hualpén, Concepción
(56) 227144000 (56) 412908700

d

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

F IGURA N° 20. M APA DE ALTURA DE MEZCLA, ÁREA MODELACIÓN 62 X 62 KM, RÉGIMEN DIURNO, PERIODO OTOÑO

INVIERNO, 2012. ................................................................................................................................... 24

F IGURA N° 21. T EMPERATURA EN ALTURA, ÁREA MODELACIÓN 62 X 62 KM AÑO 2012, PERIODO PRIMAVERA

VERANO, RÉGIMEN NOCTURNO . ............................................................................................................... 25

F IGURA N° 22. T EMPERATURA EN ALTURA, ÁREA MODELACIÓN 62 X 62 KM AÑO 2012, PERIODO PRIMAVERA

VERANO, RÉGIMEN DIURNO . .................................................................................................................... 26

F IGURA N° 23. T EMPERATURA EN ALTURA, ÁREA MODELACIÓN 62 X 62 KM AÑO 2012, PERIODO OTOÑO - INVIERNO,

RÉGIMEN NOCTURNO .............................................................................................................................. 27

F IGURA N° 24. T EMPERATURA EN ALTURA, ÁREA MODELACIÓN 62 X 62 KM AÑO 2012, PERIODO OTOÑO - INVIERNO,

RÉGIMEN DIURNO . ................................................................................................................................. 28

F IGURA N° 25. H UMEDAD RELATIVA, ÁREA MODELACIÓN 62 X 62 KM AÑO 2012, PERIODO DE VERANO, RÉGIMEN

DIURNO . ............................................................................................................................................... 29

F IGURA N° 26. H UMEDAD RELATIVA, ÁREA MODELACIÓN 62 X 62 KM AÑO 2012, PERIODO DE VERANO, RÉGIMEN

NOCTURNO . .......................................................................................................................................... 30

F IGURA N° 27. H UMEDAD RELATIVA, ÁREA MODELACIÓN 62 X 62 KM AÑO 2012, PERIODO DE INVIERNO, RÉGIMEN

DIURNO . ............................................................................................................................................... 31

F IGURA N° 28. H UMEDAD RELATIVA, ÁREA MODELACIÓN 62 X 62 KM AÑO 2012, PERIODO DE INVIERNO, RÉGIMEN

NOCTURNO . .......................................................................................................................................... 32

F IGURA N° 29. P RECIPITACIONES, ÁREA MODELACIÓN 62 X 62 KM AÑO 2012, PERIODO DE INVIERNO ( MM / HR ). . 33

F IGURA N° 30. R ADIACIÓN SOLAR, ÁREA MODELACIÓN 62 X 62 KM AÑO 2012, PERIODO DE VERANO . ................ 34

F IGURA N° 31. R ADIACIÓN SOLAR, ÁREA MODELACIÓN 62 X 62 KM AÑO 2012, PERIODO DE I NVIERNO . .............. 35

F IGURA N° 32. U BICACIÓN DE E STACIÓN DE M ONITOREO N OGALES . ............................................................. 38

F IGURA N° 33. R ECEPTORES SENSIBLES CERCANOS AL PROYECTO . .................................................................. 39

F IGURA N° 34. F UENTES DE EMISIÓN CONSIDERADAS EN LA MODELACIÓN ATMOSFÉRICA . .................................. 47

F IGURA N° 35. P UNTO DE M ÁXIMO I MPACTO DEL P ROYECTO . ...................................................................... 60

Cerro El Plomo 5630 Oficina 1501 Marco Polo 8939

Las Condes, Santiago Hualpén, Concepción
(56) 227144000 (56) 412908700

e

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**INDICE DE TABLAS**

T ABLA N° 1: V ÉRTICES DEL Á REA DE M ODELACIÓN DEL P ROYECTO . .................................................................. 8

T ABLA N° 2. D IFERENCIA PORCENTUAL METEOROLOGÍA OBSERVADA VS METEOROLOGÍA MODELADA . .................. 37

T ABLA N° 3. C OORDENADAS DE E STACIÓN DE M ONITOREO . ......................................................................... 38

T ABLA N° 4. U BICACIÓN DE R ECEPTORES SENSIBLES RESPECTO AL PROYECTO . .................................................. 40

T ABLA N° 5: N ORMAS DE C ALIDAD DEL A IRE C ONSIDERADAS EN LA M ODELACIÓN . ........................................... 43

T ABLA N° 6: M ÁXIMAS CONCENTRACIONES DE EMISIÓN DE CONTAMINANTES RESPECTO AL D.S. N°29/2013. ..... 44

T ABLA N° 7: C ONCENTRACIONES OBSERVADAS EN E STACIÓN N OGALES, ENERO - AGOSTO DE 2015. .................. 45

T ABLA N° 8: U BICACIÓN DE F UENTES E MISORAS . ........................................................................................ 46

T ABLA N° 9: C ARACTERÍSTICAS FÍSICAS - OPERACIONALES DE LAS CHIMENEAS DEL PROYECTO . ............................. 48

T ABLA N° 10: C ONCENTRACIÓN Y TASAS MÁXIMAS DE EMISIÓN DE CHIMENEAS DEL PROYECTO . .......................... 48

T ABLA N° 11: C ARACTERÍSTICAS F ÍSICAS - O PERACIONALES Y TASA DE EMISIÓN ( G / S ) DE G RUPO E LECTRÓGENO DE

E MERGENCIA . ....................................................................................................................................... 49

T ABLA N° 12: C ONCENTRACIONES APORTADAS SOBRE E STACIÓN N OGALES ( μG / M [3] N). ..................................... 50

T ABLA N° 13: C ONCENTRACIONES APORTADAS DE MP10 SOBRE RECEPTORES SENSIBLES ( G / M [3] N). .................. 51

T ABLA N° 14: C ONCENTRACIONES APORTADAS DE MP2,5 SOBRE RECEPTORES SENSIBLES ( G / M [3] N). ................. 52

T ABLA N° 15: C ONCENTRACIONES APORTADAS DE NO 2 SOBRE RECEPTORES SENSIBLES ( G / M [3] N). ..................... 53

T ABLA N° 16: C ONCENTRACIONES APORTADAS DE SO 2 SOBRE RECEPTORES SENSIBLES ( G / M [3] N). ..................... 54

T ABLA N° 17. C ONCENTRACIONES APORTADAS DE CO SOBRE RECEPTORES SENSIBLES ( G / M [3] N)........................ 55

T ABLA N° 18. C ONCENTRACIONES APORTADAS DE P B SOBRE RECEPTORES SENSIBLES ( G / M [3] N). ....................... 56

T ABLA N° 19. C ONCENTRACIONES APORTADAS DE GASES Y METALES NO NORMADOS SOBRE RECEPTORES SENSIBLES

( G / M [3] N). ........................................................................................................................................... 57

T ABLA N° 20: C ONCENTRACIONES DETERMINADAS EN LOS P UNTOS DE M ÁXIMO I MPACTO ( G / M [3] N). ............... 58

T ABLA N° 21: C ONCENTRACIONES DE GASES Y METALES SIN NORMA DE CALIDAD EN LOS P UNTOS DE M ÁXIMO

I MPACTO ( G / M [3] N). ............................................................................................................................. 59

T ABLA N° 22: C ONCENTRACIÓN FINAL MODELADA EN E STACIÓN N OGALES ( G / M [3] N). ..................................... 61

T ABLA N° 23: C ONCENTRACIÓN FINAL MODELADA EN PMI ( G / M [3] N) RESPECTO A LB DE E STACIÓN N OGALES ..... 62

Cerro El Plomo 5630 Oficina 1501 Marco Polo 8939

Las Condes, Santiago Hualpén, Concepción
(56) 227144000 (56) 412908700

f

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

#### 1 Antecedentes Generales

El proyecto consiste en la revalorización de productos de desecho, específicamente neumáticos,

plásticos y aceite. Esta revalorización pretende someter los desechos a diferentes procesos físicos para

obtener como productos finales: Negro de Humo, producto que es utilizado como pigmento y como

refuerzo en productos de goma y plástico; y un aceite con las características de un Diesel. De esta forma

se busca dar un valor a los desechos ya mencionados al obtener un subproducto y al disminuir la

cantidad de residuos que se debieran eliminar finalmente en un relleno autorizado.

Para esta revalorización se someten los residuos a un proceso de pirolisis, a partir del cual se obtienen

diferentes corrientes, las que son tratadas por separado, para la obtención de los productos finales

deseados en este proyecto.

En el proceso de pirólisis se calientan los residuos a temperatura entre los 1102 - 1121 °C, en ausencia

de oxígeno o con una cantidad limitada del mismo. La degradación térmica del material produce una

descomposición de estas sustancias, en donde los elementos orgánicos volatilizables (principalmente

cadenas de caucho) se descomponen en gases y líquidos, y los elementos inorgánicos (principalmente

acero y negro de humo no volátil) permanecen como residuo sólido.

A partir de las tres corrientes obtenidas de la pirólisis se obtienen los diferentes productos en la planta.

De la corriente de sólidos, a través de una línea de proceso, se obtiene el negro de Humo; de la corriente

de aceites pesados se obtiene el Diesel; y de la corriente gaseosa, un gas de pirólisis que sirve como

combustible para el proceso de pirólisis con el que cuenta la planta.

Las principales emisiones a la atmósfera asociadas a la operación del Proyecto corresponden a material

particulado total (expresado como MP10 y MP2,5, para efectos de contrastar con la normativa legal);

Dióxido de Nitrógeno (NO 2 ) y Monóxido de Carbono (CO), contenidas en el flujo de gases del proceso de

pirólisis.

Con el propósito de conocer los aportes al aire de las emisiones originadas por esta fuente, se realizó

una modelación de dispersión atmosférica de contaminantes, la que considera las emisiones calculadas

para la operación del Proyecto, bajo la condición de funcionamiento durante 24 horas. Para ello se ha

utilizado como base lo establecido en la _“Guía para el Uso de Modelos de Calidad del Aire en el SEIA”._

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

1

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

#### 2 Modelo Utilizado para Realizar Simulación de Dispersión Atmosférica de Contaminantes

Para realizar la modelación de emisiones atmosféricas se utilizó el programa para modelación de

dispersión atmosférica de contaminantes denominado Calpuff View V.7.1. Este modelo es recomendado

por la EPA de Estados Unidos para estimar el transporte de largo alcance de contaminantes, y su impacto

en áreas con terreno complejo; y reconocido por el SEA (Servicio de Evaluación Ambiental), como

modelo regulatorio, es decir, puede ser aplicado durante procesos de Evaluación Ambiental que

involucren Estudios de Impacto Ambiental o Declaraciones de Impacto Ambiental.

Los modelos de ‘paquetes de emisiones’ o de ‘puffs’ o ‘de trayectorias’ representan la emisión de cada

fuente puntual, como un conjunto de paquetes de contaminantes (‘puffs’), los cuales son transportados

por el campo de vientos, se expanden al mezclarse con el aire que los rodea, y en su interior se considera

también las reacciones químicas más importantes.

Los modelos de “puff”, a diferencia de los modelos Gaussianos, permiten manejar situaciones

transientes como desarrollo de brisa valle-cordillera y los casos de calmas del viento, donde los modelos

Gaussianos predicen concentraciones infinitas (o irrazonablemente altas), ya que en tal caso los

paquetes de contaminación siguen creciendo en tamaño, aunque la velocidad del viento sea

prácticamente cero.

Por esta misma razón los modelos de puff son particularmente útiles para simular situaciones de

acumulación de contaminantes bajo condiciones de muy mala dispersión (alta estabilidad atmosférica,

bajos vientos superficiales), donde fallan los modelos Gaussianos (que tienden a estimar muy altas

condiciones en las horas previas al amanecer, pese a que en esas condiciones las emisiones suelen ser

mínimas).

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

2

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 1: Representación Gráfica del Modelo Tipo Puff y de Pluma.**

Fuente: Lakes Environmental.

En la Ecuación N° 1 se presenta la fórmula que utiliza el modelo Calpuff View para el cálculo de

concentración en el aire de algún contaminante determinado, que haya sido emitido a la atmósfera por

una fuente fija y móvil.

**Ecuación N° 1: Ecuación que domina el modelo utilizado.**

2
σ x [e][2] [) ; g= ] ~~√~~

2

2

~~√~~ 2πσ z

Q
C=
2πσ x σ y

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

g∙exp(− [d] σ x [a]

[d] σ x [a][2] ~~[)]~~ [ ∙exp(−d] σ x [e]

∞

∑exp[− [(H] [e] 2σ [+ 2nh)] z [2] ]

n=−∞

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

3

Donde:

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

c : Concentración del contaminante a nivel de suelo

Q : Masa de contaminante contenida en el puff

σ x : Desviación estándar de la distribución gaussiana de concentración, en la dirección del viento

σ y : Desviación estándar de la distribución gaussiana de concentración, en la dirección

perpendicular a la del viento

σ z : Desviación estándar de la distribución gaussiana de la concentración, en la dirección vertical

d a : Distancia desde el centro geométrico del puff al receptor en la dirección del viento

d c : Distancia desde el centro geométrico del puff al receptor en la dirección perpendicular a la

del viento

g Término vertical de la ecuación gaussiana, que considera las interacciones del puff con el suelo

y con la altura de mezclado

H e : Altura efectiva desde el suelo hasta el centro geométrico del puff

h: Altura de capa de mezclado

En términos generales, el modelo Calpuff View trabaja utilizando datos de superficie terrestre (variables

de superficie) y datos meteorológicos de altura y superficie. Con dichos datos el programa es capaz de

predecir el movimiento del puff y el posterior arrastre de contaminantes atmosféricos dentro de un área

geográfica determinada (área de modelación). Resultado de lo anterior, se puede evaluar la magnitud

de los impactos ambientales sobre la calidad del aire producto de la contaminación atmosférica

originada desde fuentes fijas y móviles.

Las variables de superficie consideradas para la modelación fueron:

 Topografía del Área de Modelación

 - Albedo

 - Radio de Bowen

 - Rugosidad de superficie

 - Leaf Area Index (LAI)

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

4

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

La incidencia de las variables de superficie sobre el modelo se relaciona principalmente con la formación

y/o modificación del viento en el área de modelación.

Dependiendo de las características que presente el suelo en la superficie (tipo de suelo, especies

vegetales y porcentaje de cobertura vegetal), este tiene la capacidad de irradiar calor, el cual por medio

de convección asciende hacia la atmósfera, alterando el gradiente térmico del área de modelación,

relacionando el comportamiento de las masas de aire con las características de superficie del terreno.

Por otro lado, las variables meteorológicas que utiliza el modelo Calpuff View, son:

 - Dirección del viento (Grados)

 - Velocidad del Viento (m/s)

 - Mapa de altura de mezclado (m)

 - Temperatura (°C)

 - Humedad relativa (%)

 - Precipitaciones (mm)

 - Radiación (Wm [2] /h)

Las variaciones en la concentración de los contaminantes están directamente relacionadas con dichas

variables meteorológicas, debido a que las variaciones en la temperatura y los porcentajes de radiación

solar que el suelo recibe son los principales causantes de los fenómenos atmosféricos como las

inversiones térmicas, fenómeno por el cual se genera una alta estabilidad en la atmósfera disminuyendo

la convección térmica y los fenómenos de transporte y difusión de gases, generando finalmente

aumentos en la concentración de contaminantes debido a una mayor estabilidad atmosférica.

En cuanto a la dirección del viento, ésta tiene como resultado el transporte de contaminantes hacia un

área determinada, factor que se ve relacionado a su vez directamente con la topografía del lugar en

conjunto con las demás variables mencionadas en los puntos anteriores.

A su vez, los tipos de fuentes de emisión que el software es capaz de modelar son:

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

5

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

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

incide en la dispersión final de los contaminantes, ya que su dispersión depende igualmente de la altura

de la fuente y de la temperatura de salida del flujo de gases, lo que en conjunto con las variables

atmosféricas definen el transporte y difusión de gases y los respectivos contaminantes dentro del área

de modelación considerada.

Para el Proyecto en estudio, el tipo de fuente seleccionado para considerar en la modelación

correspondió a fuentes del tipo puntual.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

6

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

#### 3 Caracterización del Área de Modelación

**3.1** **Antecedentes Generales**

En la Figura N° 2 se presenta una vista general del dominio de modelación, cuya superficie total

corresponde a 3.844 km [2] (62 x 62 km), en ella se pueden identificar principalmente 5 sectores poblados,

correspondientes a las capitales comunales de: Llay Llay, San Felipe, Los Andes, Til Til y Colina. El dominio

contó con una resolución horizontal de 1 km y una resolución vertical de 10 niveles con límites de 0, 20,

40, 80, 160, 320, 640, 1200, 2000, 3000 y 4000 metros de altura respecto al suelo.

**Figura N° 2: Vista General del Dominio de Modelación.**

|Col1|Proyecto:<br>“Planta de Reciclaje de<br>Aceites, Caucho y Plásticos<br>Fuera de Uso”<br>Comuna de Til Til<br>Provincia de Chacabuco<br>Región Metropolitana de<br>Santiago|
|---|---|
||Situación Nacional y Regional<br> <br>**Proyecto**|
||Referencia Geodésica<br>Proyección: LCC<br>Datum: NWS-84|
||<br>|

Fuente: Elaboración propia mediante Google Earth.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

7

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

En la Tabla N° 1 se dan a conocer las coordenadas, en proyección UTM y Datum WGS - 84, que definen

la superficie de modelación considerada en el modelo Calpuff View.

**Tabla N° 1: Vértices del Área de Modelación del Proyecto.**

|Vértice|Coordenadas UTM, Huso 19 Sur, Datum WGS-84|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|Suroeste|300.087|6.321.563|
|Sureste|362.216|6.322.640|
|Noroeste|299.023|6.383.407|
|Noreste|361.151|6.384.468|
|**Resolución de Dominio**|**Resolución de Dominio**|**Resolución de Dominio**|
|Horizontal|1 km|1 km|
|Vertical|0, 20, 40, 80, 160, 320, 1200, 2000, 3000, 4000 metros|0, 20, 40, 80, 160, 320, 1200, 2000, 3000, 4000 metros|

Fuente: Elaboración propia.

**3.2** **Variables de Superficie Consideradas**

**3.2.1** **Topografía**

Desde el punto de vista geofísico, el Proyecto se ubica a unos 805 metros sobre el nivel del mar

(m s. n. m.) aproximadamente, en la Depresión Intermedia de la Región Metropolitana de Santiago de

Chile, entre la Cordillera de la Costa al poniente y la Cordillera de los Andes al oriente.

Para efectos de considerar la topografía dentro de la modelación de emisiones atmosféricas, es que las

diferencias de altura serán consideradas tanto por el modelo Calpuff view como por el procesador de

terreno GEO del software Calpuff View de Lakes Environmetal mediante la utilización de topografía

digital del área considerada. La topografía utilizada corresponde a un modelo de elevación digital

SRTM3, cuyo formato es admitido por el procesador topográfico GEO de Calpuff View, el cual tiene la

capacidad de incluir dentro de la modelación las diferencias de cotas del terreno a medida que se avanza

hacia la costa y para toda el área de modelación considerada. Con lo anterior, se logra incorporar la

topografía al modelo Calpuff View, según el área de modelación de interés y las coordenadas que

demarcan el límite del área de modelación.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

8

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

A continuación se presenta un modelo digital de la topografía considerada en la modelación, en él se

observa que el Proyecto se ubica en un valle, con altitudes entre los 800 y 900 m s. n. m., específicamente

a unos 805 m s. n. m. aproximadamente. Se observa que las características topográficas del área de

emplazamiento del Proyecto dificultarían una correcta dispersión y dilución de contaminantes, dado que

al estar rodeando de cerros y montañas se produce un encajonamiento del aire, dificultando el paso el

viento que por lo demás, al estar tan aislado y alejado de la costa, se espera que sean vientos de bajas

velocidades.

**Figura N° 3: Topografía Considerada en la Modelación.**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

9

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**3.2.2** **Uso de Suelo**

El dominio de modelación (62 km x 62 km) abarca diversas comunas de las Regiones de Valparaíso y

Metropolitana de Santiago, tales como: Quilpué, Olmué, Hijuelas, Catemu, Llay Llay, Panquehue, San

Felipe, Santa María, Rinconada, San Esteban, Los Andes, Calle Larga, Til Til, Colina y Lampa. Por otra

parte, el Proyecto se emplaza en la comuna de Til Til, la cual abarca una superficie total de 653,0 km2,

equivalentes al 4,2% de la superficie total regional (PLADECO Til Til 2015 - 2019). La predominancia en

el uso del suelo alrededor del Proyecto es del tipo pastizales (sector 30, Figura N° 4) y agrícola (sector

20, Figura N° 4), de acuerdo a lo generado por la herramienta GEO de Calpuff View. También se pueden

observar pequeñas porciones de suelo Urbano (Sector 10, Figura N° 4) correspondientes a San Felipe y

Los Andes, tal como se presenta a continuación:

**Figura N° 4: Usos de suelo considerado en la modelación.**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

10

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

##### 3.3 Variables Meteorológicas

**3.3.1** **Meteorología de Superficie de Altura**

Dada la falta de información meteorológica observacional completa y representativa en el dominio de

modelación, las variables meteorológicas de superficie y de altura necesarias para realizar la modelación

de dispersión de contaminantes atmosféricos fueron obtenidas mediante el modelo numérico Weather

Research and Forecasting Model (WRF), recomendado en la “Guía para el Uso de Modelos de Calidad

del Aire en el SEIA”, siendo uno de los modelos meteorológicos de pronóstico más avanzados y

completos, mantenido por NCAR/NOAA de Estados Unidos. Además, se ha ocupado en la mayoría de los

proyectos relacionados con modelación atmosférica a cargo de organismos estatales, como la ex

CONAMA y la Comisión Nacional de Energía (CNE) en los últimos cinco años.

Se utilizó una grilla meteorológica de 62 km X 62 km generada a partir del modelo WRF para el periodo

1 de Enero a 31 de Diciembre de 2012, la cual fue generada por la empresa especialista Meteodata, una

empresa spin-off del Departamento de Geofísica de la Universidad de Chile. Las variables meteorológicas

procesadas por el modelo fueron las siguientes:

 - Dirección del viento (Grados)

 - Velocidad del Viento (m/s)

 - Mapa de altura de mezclado (m)

 - Temperatura (°C)

 - Humedad relativa (%)

 - Precipitaciones (mm)

 - Radiación (Wm [2] /h)

A continuación, en la Figura N° 5 se presenta el dominio de la grilla meteorológica WRF, cuya resolución

es de 1 km.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

11

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 5. Grilla meteorológica WRF utilizada para la modelación en Calpuff** .

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

12

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**3.3.2** **Dirección y Velocidad del Viento**

A continuación, en la Figura N° 6 y Figura N° 7, se presenta la Rosa de Vientos para el periodo EneroDiciembre de 2012, según lo obtenido por el modelo Weather Research and Forecasting (WRF) en el

área de emplazamiento del Proyecto a 10 metros de altura sobre del suelo.

**Figura N° 6: Rosa de Vientos obtenida con WRF para el Año 2012.**

Fuente: Elaboración propia mediante Calpuff View en base a WRF de la zona para año 2012.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

13

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 7: Rosa de vientos en contexto espacial para año 2012.**

Fuente: Elaboración propia con WR Plot y Google Earth, en base a WRF, año 2012.

A continuación se presentan las frecuencias de velocidades de vientos del área de emplazamiento del

proyecto a 10 metros de altura sobre el suelo, según lo obtenido con el modelo WRF.

**Figura N° 8: Gráfico de distribución de frecuencia de vientos.**

Fuente: Elaboración propia con WR Plot, en base a WRF, año 2012.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

14

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

En las figuras anteriores se puede observar que la dirección del viento predominante anual en el área

del Proyecto, de acuerdo al vector resultante, es principalmente Nor-noreste (NNE), mientras que la

velocidad del viento predominante anual fluctúa entre los 2,1 y 3,6 m/s (30,5%), seguido de las

velocidades entre 0,5 y 2,1 m/s (30,3%), y de las velocidades entre 3,6 y 5,7 m/s (28,5%).

A continuación se presenta el análisis estacional y diario para la velocidad y dirección del viento con sus

respectivos gráficos de frecuencia.

**Figura N° 9: Rosas de viento, Periodo Primavera-Verano, 2012.**

Fuente: Elaboración propia con WR Plot, en base a WRF, año 2012

**Figura N° 10: Rosas de viento, Periodo Otoño-Invierno, 2012.**

Fuente: Elaboración propia con WR Plot, en base a WRF, año 2012.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

15

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 11: Gráficos de distribución de frecuencia, Periodo Primavera-Verano, 2012.**

Fuente: Elaboración propia con WR Plot, en base a WRF, año 2012.

**Figura N° 12: Gráficos de distribución de frecuencia, Periodo Otoño-Invierno, 2012.**

Fuente: Elaboración propia con WR Plot, en base a WRF, año 2012.

En las figuras anteriores se puede observar que no existe una gran diferencia estacional en las

direcciones de viento, observándose que prácticamente todo el año predominan vientos desde el norte

durante el día y desde el sureste durante la noche, asociados principalmente a brisas Valle - Montaña.

Respecto a las velocidades, se observan mayores velocidades de viento durante el día y menores

velocidades con mayores periodos de calma durante la noche. Por otro lado, estacionalmente se observa

que los meses de otoño - invierno presentan menores velocidades y mayores periodos de calmas que

los meses de primavera - verano.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

16

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**3.3.3** **Mapas Campos de vientos dentro del dominio de la modelación**

A continuación, en las siguientes figuras, se presenta el campo de vientos superficiales simulados a partir

del modelo de pronóstico meteorológico WRF correspondiente al año 2012, haciéndose el análisis

estacional y diario.

**Figura N° 13. Mapa de viento de área modelación 62 x 62 km, régimen nocturno, verano, 2012,**

**modelado con WRF (01-01-2012 03:00 am).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

17

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 14. Mapa de viento área modelación 62 x 62 km, régimen diurno, verano, 2012, modelado con WRF**

**(01-01-2012 03:00 pm).**

Fuente: Elaboración propia mediante Calpuff View.

En la Figura N° 13 y Figura N° 14 se observan mapas de viento en verano para régimen nocturno y diurno

respectivamente, se puede apreciar que debido a la compleja topografía de la zona, no existe un patrón

definido de dirección del viento para toda el área, no obstante, se puede apreciar un claro efecto Brisa

Valle - Montaña, dado que en el régimen diurno se observan vientos que van desde los valles hacia las

zonas altas, mientras que en el régimen nocturno los vientos bajan hacia los valles.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

18

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

Paralelamente, se puede apreciar que el viento presenta una mayor intensidad durante el día

(Figura N° 14), alcanzándose velocidades de 10,4 m/s, mientras que de noche (Figura N° 13) predominan

las velocidades más bajas y se alcanzan máximos de 9,1 m/s.

**Figura N° 15. Mapa de viento área modelación 62 x 62 km, régimen nocturno, invierno, 2012,**

**modelado con WRF (07-07-2012 03:00 am).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

19

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 16. Mapa de viento área modelación 62 x 62 km, régimen diurno, invierno, 2012, modelado con WRF**

**(07-07-2012 03:00 pm).**

Fuente: Elaboración propia mediante Calpuff View.

Para el caso de los vientos de invierno presentados en régimen nocturno y diurno en la Figura N° 15 y

Figura N° 16 respectivamente, es posible observar velocidades más bajas que en verano, las cuales

aumentan levemente durante el día alcanzando 8,3 m/s. Respecto a las direcciones, no se observa una

gran diferencia con los vientos de verano, apreciándose también el efecto Brisa Valle - Montaña, con

vientos que bajan por las laderas de los cerros hacia los valles durante la noche y vientos que suben

desde los valles hacia los cerros durante el día.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

20

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**3.3.4** **Mapas de altura de mezclado dentro del dominio de modelación**

A continuación, en las siguientes figuras, se presentan las capas de altura de mezclado, tanto para un

régimen diurno (Figura N° 18 y Figura N° 20) como nocturno (Figura N° 17 y Figura N° 19), para verano

(01 de enero de 2012) e invierno (07 de julio de 2012). En estas, se puede observar que en horas de la

noche se presentan alturas de capa de mezclado más bajas, que pueden llegar a los 234 metros sobre el

nivel del terreno en verano y 238 metros en invierno, en tanto, durante el día se alcanzan mayores

alturas de mezclado que pueden llegar a 2115 metros sobre el nivel del terreno en verano y 829 metros

en invierno.

**Figura N° 17. Mapa de altura de mezcla, área modelación 62 x 62 km, régimen nocturno, verano,**

**2012 (01-01-2012 03:00 am).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

21

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 18. Mapa de altura de mezcla, área modelación 62 x 62 km, régimen diurno, verano 2012**

**(01-01-2012 03:00 pm).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

22

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 19. Mapa de altura de mezcla, área modelación 62 x 62 km, régimen nocturno, invierno**

**2012 (07-07-2012 03:00 am).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

23

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 20. Mapa de altura de mezcla, área modelación 62 x 62 km, régimen diurno, invierno, 2012**

**(07-07-2012 03:00 pm).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

24

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**3.3.5** **Temperatura del aire superficial**

A continuación, en las siguientes figuras, se presenta la temperatura del aire modelado con WRF, en

periodo nocturno y diurno para verano (Figura N° 21 y Figura N° 22) e invierno (Figura N° 23 y Figura N°

24) del 2012. Se observa una clara diferencia entre temperaturas diurnas y nocturnas, con amplitudes

térmicas diarias que alcanzan 10,8 °C en verano y 6,1 °C en invierno, por otro lado, se observan menores

temperaturas a medida que aumenta la altitud y mayores temperaturas en las zonas más bajas y

encajonadas [1] . Adicionalmente, debido a las características topográficas de la zona, aislada de influencia

oceánica, se generan temperaturas extremas que llegan fácilmente a los 32 °C en verano y a los -0,6 ° C

en invierno (Figura N° 22 y Figura N° 23, respectivamente).

**Figura N° 21. Temperatura del aire superficial, área modelación 62 x 62 km año 2012, verano,**

**régimen nocturno (01-01-2012 03:00 am).**

Fuente: Elaboración propia mediante Calpuff View.

1 Ver Topografía del área de modelación en Figura N° 3.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

25

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 22. Temperatura del aire superficial, área modelación 62 x 62 km año 2012, verano,**

**régimen diurno (01-01-2012 03:00 pm).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

26

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 23. Temperatura del aire superficial, área modelación 62 x 62 km año 2012, invierno,**

**régimen nocturno (07-07-2012 03:00 am)** .

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

27

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 24. Temperatura del aire superficial, área modelación 62 x 62 km año 2012, invierno,**

**régimen diurno (07-07-2012 03:00 pm).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

28

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**3.3.6** **Humedad Relativa**

A continuación en la Figura N° 25, Figura N° 26, Figura N° 27 y Figura N° 28 se observa que las humedades

relativas aumentan en periodo de invierno alcanzando valores de 100% (tanto en régimen nocturno

como diurno); por su parte, en periodo estival estas no superan un 92% en régimen nocturno y un 67%

en régimen diurno.

**Figura N° 25. Humedad relativa, área modelación 62 x 62 km año 2012, verano, régimen diurno**

**(01-01-2012 03:00 pm).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

29

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 26. Humedad relativa, área modelación 62 x 62 km año 2012, verano, régimen nocturno**

**(01-01-2012 03:00 am).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

30

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 27. Humedad relativa, área modelación 62 x 62 km año 2012, invierno, régimen diurno**

**(07-07-2012 03:00 pm).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

31

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 28. Humedad relativa, área modelación 62 x 62 km año 2012, invierno, régimen nocturno**

**(07-07-2012 03:00 am).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

32

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**3.3.7** **Precipitaciones**

Las precipitaciones son prácticamente nulas alcanzándose máximos de 0,1 mm/hr en periodo de

invierno, tal como se presenta en la Figura N° 29.

**Figura N° 29. Precipitaciones, área modelación 62 x 62 km año 2012, periodo de invierno (mm/hr).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

33

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**3.3.8** **Radiaciones**

A continuación, en la Figura N° 30 y Figura N° 31 _,_ se observa que la radiación solar en periodo de verano

puede alcanzar valores de 1002 w/m [2], disminuyendo de manera importante en periodo de invierno,

donde la radiación sólo alcanza valores máximos de 470 W/m [2] .

**Figura N° 30. Radiación solar, área modelación 62 x 62 km año 2012, periodo de verano**

**(01-01-2012 03:00 pm).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

34

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura N° 31. Radiación solar, área modelación 62 x 62 km año 2012, periodo de invierno**

**(07-07-2012 03:00 pm).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

35

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**3.3.9** **Análisis de incertidumbre del periodo modelado**

De acuerdo al análisis antes expuesto, a continuación se presenta un resumen del análisis cualitativo y

cuantitativo de la capacidad predictiva del modelo meteorológico WRF, donde se realiza una

comparación entre la meteorología observada en el año 2015 por la Estación de Monitoreo Romeral,

ubicada en la comuna de Hijuelas, y la meteorología modelada por WRF para el año 2012.

Es importante destacar que no se contó con información meteorológica observada para el mismo año

del modelo WRF (Año 2012), los datos observados fueron descargados del Sistema Nacional de Calidad

del Aire (SINCA). Las estaciones de monitoreo del SINCA ubicadas al interior de la grilla meteorológica

WRF utilizada en la presente modelación correspondieron a: Estación Catemu, Estación Santa Margarita,

Estación Lo Campo y Estación Romeral, todas ubicadas en Región de Valparaíso, se eligió el año 2015 de

Estación Romeral por presentar la mayor disponibilidad de datos horarios (97% del año).

**3.3.10** **Evaluación Cualitativa**

Las gráficas siguientes presentan la comparación entre los valores observados y modelados para la

variable de velocidad de viento en el mismo punto geográfico (ubicación de Estación Romeral [2] ).

**Gráfico N° 1. Ciclos diarios de velocidad del viento (m/s) observados vs modelados.**

Fuente: Elaboración propia en base a registros de estación Romeral, 2015 y datos modelados con WRF, 2012.

2 Coordenadas UTM, Huso 19 Sur, Datum WGS-84: 312.181 metros Este; 6.366.428 metros Norte.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

36

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

En el Gráfico N° 1 se aprecia que al comparar el ciclo diario observado y de pronóstico, el modelo

reproduce correctamente la trayectoria de las curvas de velocidad del viento, sin embargo se observa

que el modelo sobrestima levemente la intensidad del viento, principalmente en la tarde. Lo anterior,

generaría que el modelo de dispersión subestime concentraciones de contaminantes principalmente en

las horas de la tarde (Entre las 14:00 y 18:00 horas, principalmente).

**3.3.11** **Evaluación Cuantitativa**

A continuación en la Tabla N° 2 se presenta la diferencia entre la meteorología observada y modelada

para los promedios de los ciclos diarios.

**Tabla N° 2. Diferencia porcentual meteorología observada vs meteorología modelada.**

|Parámetro|Media Anual<br>Modelada|Media Anual<br>Observada|Diferencia porcentual<br>(Modelada - Observada)|
|---|---|---|---|
|Velocidad del viento (m/s)|4,42|3,81|13,7%|

Fuente: Elaboración propia en base a registros de estación Romeral, 2015 y datos modelados con WRF, 2012.

De la Tabla N° 2 se puede observar que no se presenta una gran diferencia entre la meteorología

observada y simulada por el modelo de pronóstico WRF, cuya diferencia porcentual es de un 13,7%. Lo

anterior puede desencadenar en una subestimación de las concentraciones atmosféricas,

principalmente en las horas de la tarde, donde se presenta la mayor diferencia, según el ciclo diario.

Adicionalmente, cabe destacar que el modelo WRF entrega el promedio horario de las variables

meteorológicas de una celda completa (1 x 1 km) y de la primera capa vertical de la atmósfera (0 a 10

metros de altura respecto al suelo), a diferencia de la meteorología observada que mide en un punto y

altura específica del territorio, por lo que las diferencias entre ambas son esperables. No obstante, de

manera de no arriesgar una posible subestimación de las concentraciones de contaminantes a modelar,

se procedió a simular las máximas tasas de emisión posibles a emitir por el Proyecto durante todo el

periodo anual del modelo WRF (01/01/2012 00:00 a 30/12/2012 23:00), de manera constante [3], con el

fin de evaluar el peor escenario posible.

3 La modelación de dispersión consideró que los hornos del Proyecto estarán operando todas las horas del año de manera constante,

sin ningún periodo de pausa, emitiendo constantemente las máximas tasas de emisión garantizadas por el proveedor.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

37

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**3.4** **Receptores Contemplados en la Modelación**

**3.4.1** **Estación de Monitoreo**

Se ha contemplado el uso de una estación de monitoreo, siendo las más cercana a la ubicación del

proyecto con datos de calidad del aire disponibles, correspondiente a Estación Nogales, propiedad de

Cemento Polpaico S.A., operada por Cesmec S.A. y cuyos parámetros de medición correspondieron a

MP10, NO 2, SO 2, CO, Pb y otros metales pesados. A continuación se presentan las coordenadas y

ubicación de la estación de monitoreo.

**Tabla N° 3. Coordenadas de Estación de Monitoreo.**

|Receptor|Coordenadas UTM, HUSO 19 Sur, Datum: WGS - 84|Col3|
|---|---|---|
|**Receptor**|**Este (m)**|**Norte (m)**|
|Estación Nogales|323.808|6.327.899|

Fuente: Elaboración propia mediante Calpuff View.

**Figura N° 32. Ubicación de Estación de Monitoreo Nogales.**

Fuente: Elaboración propia en base a informe de calidad del aire de Cesmec.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

38

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**3.4.2** **Receptores Sensibles**

Los receptores sensibles identificados y contemplados dentro de la modelación se presentan en la
siguiente Figura N° 33 y Tabla N° 4.
Estos corresponden a establecimientos educaciones y establecimientos de salud de los principales

sectores habitados de la zona.

**Figura N° 33. Receptores sensibles cercanos al proyecto.**

Fuente: Elaboración propia en base a Geoportal.cl.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

39

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Tabla N° 4. Ubicación de Receptores sensibles respecto al proyecto.**

|N°|Receptores Sensibles|Coordenadas UTM, HUSO 19, Datum WGS - 84|Col4|Distancia al Proyecto<br>(km)|
|---|---|---|---|---|
|**N°**|**Receptores Sensibles**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|1|Posta de Salud Rural Rungue|323.538|6.346.058|19,50|
|2|La Cumbre|330.393|6.354.387|1,39|
|3|Escuela Rungue|323.160|6.346.139|19,96|
|4|Escuela Santa Matilde|323.115|6.345.117|21,45|
|5|Escuela Capilla de Caleu|313.911|6.346.544|35,61|
|6|Jardín Infantil La Sonrisa|315.363|6.344.463|34,70|
|7|Escuela Básica Manchester College|319.950|6.339.249|34,48|
|8|Escuela San Pio De Pietrelcina|319.968|6.338.228|36,10|
|9|Cosam Til-Til|320.296|6.337.851|36,33|
|10|Jardín Infantil Los Angelitos|320.949|6.337.225|36,67|
|11|Escuela Plazuela de Polpaico|323.832|6.330.197|47,24|
|12|Posta de Salud Rural Polpaico|323.619|6.327.834|51,90|
|13|Escuela Básica Montenegro|328.402|6.350.960|5,75|
|14|Posta de Salud Rural Montenegro|328.404|6.350.963|5,74|
|15|Jardín Infantil Huechún|334.576|6.338.933|28,96|
|16|Consultorio Huertos Familiares|332.255|6.332.195|41,44|
|17|Escuela Especial La Huerta|332.205|6.331.365|43,09|
|18|Colegio Saint Louis School|332.958|6.328.572|48,79|
|19|Jardín Infantil mi Campito|339.572|6.339.271|32,58|
|20|Posta de Salud Rural Chacabuco|342.017|6.342.694|30,60|
|21|Posta de Salud Rural San Vicente|348.763|6.358.644|38,19|

Fuente: Elaboración propia.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

40

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

#### 4 Marco Legal

**4.4** **Aspectos Generales**

Para controlar y evitar la contaminación en Chile existen normas primarias de calidad, normas

secundarias de calidad y normas de emisión.

**4.4.1** **Normas de Calidad Ambiental**

La Norma Primaria de Calidad Ambiental es “ _aquélla que establece los valores de las concentraciones y_

_períodos, máximos o mínimos permisibles de elementos, compuestos, sustancias, derivados químicos o_

_biológicos, energías, radiaciones, vibraciones, ruidos o combinación de ellos, cuya presencia o carencia_

_en el ambiente pueda constituir un riesgo para la vida o la salud de la población_ ” (Art 2 LBGMA [4] ).

La Norma Secundaria de Calidad Ambiental es “ _aquélla que establece los valores de las concentraciones_

_y períodos, máximos o mínimos permisibles de sustancias, elementos, energía o combinación de ellos,_

_cuya presencia o carencia en el ambiente pueda constituir un riesgo para la protección o la conservación_

_del medio ambiente, o la preservación de la naturaleza_ ” (Art 2 LBGMA).

Las normas de calidad, tienen como objetivo servir para definir si existe riesgo sobre la población

(normas primarias) y/o efectos adversos significativos sobre los recursos naturales renovables incluidos

suelo, agua y aire (normas secundarias). De esta manera, en base a las normas primarias y secundarias

se puede:

1. Declarar zonas latentes (cuando la concentración ambiental supere el 80% del límite establecido en

una norma de calidad) y zonas saturadas (cuando la concentración ambiental supere el límite

establecido en una norma de calidad). Declarada una zona latente o saturada, mediante Decreto

Supremo, se deberá generar un Plan de Prevención y/o Descontaminación que regulará las

actividades que se encuentran al interior de la zona declarada latente o saturada.

2. Indicar cuándo un Proyecto debe mitigar, reparar y/o compensar sus impactos por ser significativos.

_4_ _Ley 19.300 sobre Bases Generales del Medio Ambiente._

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

41

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

Por otra parte las normas primarias de calidad indican cuándo se genera riesgo para la salud de la

población, lo que se puede generar en dos hipótesis:

1. Cuando un Proyecto se emplaza en una zona en estado de saturación o con declaración de zona

saturada y _**genera emisiones importantes del mismo contaminante responsable de la**_

_**saturación**_ [5] .

2. Cuando un Proyecto no se emplaza en una zona de estado de saturación, pero producto de las

emisiones, efluentes o residuos, la población se verá expuesta a concentraciones de saturación

(de norma nacional o de referencia).

**4.4.2** **Normas de Emisión**

Las normas de emisión son “las que establecen la cantidad máxima permitida para un contaminante

medida en el efluente de la fuente emisora” (Art 2 LBGMA). Las normas de emisión son normativas que

deben ser cumplidas por todos los Proyectos, actividades, personas jurídicas y naturales que se

encuentren regulados por alguna norma de emisión.

En relación a la evaluación ambiental, las normas de emisión vigentes “serán consideradas para efectos

de predecir los impactos sobre los recursos naturales renovables, incluidos el suelo, agua y aire de

acuerdo a los límites establecidos en ellas.” (Art 5 DS 40/2013, MMA. RSEIA).

_5_ _Guía de Evaluación Ambiental “Riesgo para la Salud de la Población” (SEA, 2012)_

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

42

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**4.5** **Normas de calidad del Aire Aplicables**

Con el fin de determinar si el Proyecto afecta de manera significativa la calidad del aire en los potenciales

receptores, es necesario considerar el cumplimiento de la normativa ambiental aplicable, para lo cual

se consideraron las normas de calidad para los contaminantes asociados al Proyecto. A continuación se

presentan los límites establecidos por las normas de calidad del aire existentes en Chile.

**Tabla N° 5: Normas de Calidad del Aire Consideradas en la Modelación.**

|Contaminante|Tipo de norma|Estadístico y periodo normado|Valor límite|Decreto y Organismo|
|---|---|---|---|---|
|MP10|Primaria|Percentil 98 de 24 horas|150 μg/m3N|D.S. N°59/1998,<br>MISEGPRES6|
|MP10|Primaria|Promedio Anual|50 μg/m3N|50 μg/m3N|
|MP2,5|Primaria|Promedio Anual|20 μg/m3N|D.S. N°12/2011, MMA|
|MP2,5|Primaria|Percentil 98 de 24 horas|50 μg/m3N|50 μg/m3N|
|SO2|Primaria|Promedio Anual|80 μg /m3N|D.S. N°113/2002,<br>MINSEGPRES|
|SO2|Primaria|Percentil 99 de 24 horas|250 μg/m3N|250 μg/m3N|
|SO2|Secundaria|Promedio Anual|80 μg /m3N|D.S. N°22/2010,<br>MINSEGPRES|
|SO2|Secundaria|Percentil 99,7 de 24 horas|365 μg/m3N|365 μg/m3N|
|SO2|Secundaria|Percentil 99,73 de 1 hora|1.000 μg/m3N|1.000 μg/m3N|
|NO2|Primaria|Promedio Anual|100 μg/m3N|D.S. N°114/2002,<br>MINSEGPRES|
|NO2|Primaria|Percentil 99 de 1 hora|400 μg/m3N|400 μg/m3N|
|CO|Primaria|Percentil 99 de 1 hora|30.000 μg/m3N|D.S. N°115/2002,<br>MINSEGPRES|
|CO|Primaria|Percentil 99 de 8 hora|10.000 μg/m3N|10.000 μg/m3N|
|Pb|Primaria|Promedio anual|0,5 μg/m3N|D.S. N° 136/2001, <br>MINSEGPRES|

Fuente: Elaboración propia en base a las respectivas normas de calidad del aire de Chile.

6 Si bien, el D.S. N°20/13 derogaba el D.S. N°59/98, eliminando el límite anual, el Tribunal Ambiental de Santiago decidió

anular el nuevo decreto, manteniendo vigente el original.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

43

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**4.6** **Normas de Emisión Aplicables**

El proyecto que se evalúa en este informe corresponde a una planta que considera un proceso de

pirólisis, el que incluye la incineración de gases generados en procesos de pirólisis o gasificación, por lo

cual aplica el D.S. N° 29/2013, del Ministerio del Medio Ambiente, que establece la Norma de Emisión

para Incineración, Coincineración y Coprocesamiento.

En la siguiente tabla se presentan las concentraciones máximas, garantizadas por el fabricante de los

hornos, en los gases de salida de las chimeneas del proyecto, junto con los límites establecidos en el D.S.

N° 29/2013, detallando el cumplimiento del límite de emisión.

**Tabla N° 6: Máximas concentraciones de emisión de contaminantes respecto al D.S. N°29/2013.**

|Fuente|Contaminante|(*) Máximas concentraciones en gases de salida (mg/m3N)|Col4|Col5|(*) Límite de<br>norma (mg/m3N)|Cumplimiento<br>de Norma|
|---|---|---|---|---|---|---|
|**Fuente**|**Contaminante**|**Neumáticos**|**Plásticos**|**Aceites**|**Aceites**|**Aceites**|
|Chimeneas<br>Hornos de<br>Pirólisis|MP|10|18|15|30|Si cumple|
|Chimeneas<br>Hornos de<br>Pirólisis|SO2|35|27|24|50|Si cumple|
|Chimeneas<br>Hornos de<br>Pirólisis|NOx|62,6|53,6|31,3|300|Si cumple|
|Chimeneas<br>Hornos de<br>Pirólisis|CO|39,4|31,8|26,3|50|Si cumple|
|Chimeneas<br>Hornos de<br>Pirólisis|COT|12|14|17|20|Si cumple|
|Chimeneas<br>Hornos de<br>Pirólisis|Cd|0,008|0,008|0,008|0,1|Si cumple|
|Chimeneas<br>Hornos de<br>Pirólisis|Be|0,01|0,01|0,01|0,1|Si cumple|
|Chimeneas<br>Hornos de<br>Pirólisis|Pb/Zn|0,2|0,116|0,4|1|Si cumple|
|Chimeneas<br>Hornos de<br>Pirólisis|HCl|8|7|12|20|Si cumple|
|Chimeneas<br>Hornos de<br>Pirólisis|Benceno|2|2|3|5|Si cumple|
|Chimeneas<br>Hornos de<br>Pirólisis|As/Co/Ni/Se/Te|0,8|0,8|0,9|1|Si cumple|
|Chimeneas<br>Hornos de<br>Pirólisis|Sb/Cr/Mn/V|2|1|1|5|Si cumple|
|Chimeneas<br>Hornos de<br>Pirólisis|Hf|0,8|1,1|1,3|2|Si cumple|
|Chimeneas<br>Hornos de<br>Pirólisis|Hg|0,01|0,01|0,01|0,1|Si cumple|
|Chimeneas<br>Hornos de<br>Pirólisis|Dioxin/Furans|3,00E-08|5,00E-08|1,40E-07|2,00E-07|Si cumple|

(*) Concentraciones en base seca normalizadas a 25°C y 101 kPa, corregidas a 3% de oxígeno de acuerdo al D. S. N°29/13.

Fuente: Certificado del fabricante de equipos del proyecto y D.S. N°29/13 Norma de Emisión para Incineración,

Coincineración y Coprocesamiento.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

44

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

#### 5 Línea de Base de Calidad del Aire

Para determinar la línea de base se utilizaron los resultados de monitoreos de calidad del aire

realizados por Cesmec S.A., cuyos registros fueron obtenidos desde las Estación Nogales, propiedad

de Cemento Polpaico S.A., analizándose los siguientes contaminantes atmosféricos: MP 10, SO 2, NO 2,

CO y Pb. La ubicación geográfica de la estación fue presentada en la Tabla N° 3 y Figura N° 32, los

gráficos con las series de tiempo de cada contaminante se presentan en el Apéndice 2 del presente

informe.

En la Tabla N° 7 se entrega un análisis de los estadísticos y periodos normados a partir de los datos

medidos por Estación Nogales para el periodo enero - agosto de 2015. Cabe destacar, que si bien el

MP2,5 no fue monitoreado, los estadísticos de este contaminante fueron estimados en base a las

mediciones de Estación Quilicura _[7]_, la más cercana a Estación Nogales, para el mismo periodo (enero

- agosto de 2015), en la que se observó que aproximadamente un 37% del MP10 corresponde a

MP2,5.

**Tabla N° 7: Concentraciones observadas en Estación Nogales, enero - agosto de 2015.**

|Contaminante|Estadístico y Periodo|Línea Base|Límite Norma<br>Primaria|Límite Norma<br>Secundaria|Unidad|% Norma|Cumplimiento|
|---|---|---|---|---|---|---|---|
|MP10|Promedio anual|77,8|50|-|μg/m3N|155,6%|**No cumple**|
|MP10|Percentil 98 de 24 horas|144,1|150|-|μg/m3N|96,1%|Si cumple|
|MP2,5|Promedio anual|28,8|20|-|μg/m3N|143,9%|**No cumple**|
|MP2,5|Percentil 98 de 24 horas|53,3|50|-|μg/m3N|106,6%|**No cumple**|
|NO2|Promedio Anual|24,5|100|-|μg/m3N|24,5%|Si cumple|
|NO2|Percentil 99 de máximos horarios|89,2|400|-|μg/m3N|22,3%|Si cumple|
|SO2|Promedio Anual|8,9|80|80|μg/m3N|11,1%|Si cumple|
|SO2|Percentil 99 de 24 horas|16,8|250||μg/m3N|6,7%|Si cumple|
|SO2|Percentil 99,7 de 24 horas|17,6|-|365|μg/m3N|4,8%|Si cumple|
|SO2|Percentil 99,73 de 1 hora|21,7|-|1.000|μg/m3N|2,2%|Si cumple|
|CO|Percentil 99 de máximos horarios|3,7|30|-|mg/m3N|12,3%|Si cumple|
|CO|Percentil 99 de máximos 8 horas|2,4|10|-|mg/m3N|24,1%|Si cumple|
|Pb|Promedio Anual|0,0018|0,5|-|μg/m3N|0,4%|Si cumple|

Fuente: Elaboración propia.

7 Los datos de Estación Quilicura fueron descargados del Sistema Nacional de Calidad del Aire (SINCA).

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

45

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

De acuerdo a los resultados, se tiene que la mayoría de los contaminantes monitoreados en Estación

Nogales cumplen con las normas calidad del aire vigente en Chile, con excepción del MP10 y MP2,5,

los cuales muestran una tendencia [8] a la saturación, como promedio anual para MP10 y como

promedio anual y 24 horas para MP2,5.

Los valores monitoreados representan un 155,6% y 96,1% de los límites al promedio anual y 24

horas de MP10; un 143,9% y 106,6% para el promedio anual y 24 horas de MP2,5; un 24,5% y 22,3%

para el promedio anual y percentil 99 de 1 hora de NO 2 ; 11,1% y 6,7% para el promedio anual y

percentil 99 de 24 horas de SO 2 (norma primaria); 11,1%, 4,8% y 2,2% para el promedio anual,

percentil 99,7 de 24 horas y percentil 99,73 de 1 hora de SO 2 (norma secundaria); 12,3% y 24,1%

para el percentil 99 de 1 hora y de percentil 99 de 8 horas de CO y 0,4% para el promedio anual de

Pb. Adicionalmente, se observa que el promedio anual de MP10 muestra una tendencia a estado de

latencia (>80%).

#### 6 Descripción de la Fuente Emisora

**6.4** **Ubicación de la Fuente**

En la Tabla N° 6 se presentan las coordenadas UTM que indican la localización de las fuentes de

emisión consideradas en la modelación de dispersión atmosférica de contaminantes.

**Tabla N° 8: Ubicación de Fuentes Emisoras.**

|No|Fuentes Emisoras a Modelar|Coordenadas UTM, Huso 19 Sur, Datum WGS - 84|Col4|
|---|---|---|---|
|**No**|**Fuentes Emisoras a Modelar**|**Este (m)**|**Norte (m)**|
|1|Chimenea N°1, primer horno de Pirólisis|330.651|6.353.023|
|2|Chimenea N°2, segundo horno de Pirólisis|330.655|6.3530.21|
|3|Grupo Electrógeno de emergencia|330.644|6.353.011|

Fuente: Elaboración propia.

8 Se debe destacar que se habla de una “tendencia” a la saturación, dado que los registros analizados abarcan sólo una
parte del periodo anual 2015 (Enero - Agosto), faltando cerca de un 33% del año.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

46

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

La ubicación de las fuentes de emisión al interior de la planta se presenta en la siguiente figura.

**Figura N° 34. Fuentes de emisión consideradas en la modelación atmosférica.**

Fuente: Elaboración propia en base a layout del Proyecto y Google Earth Pro.

##### 6.5 Variables Físicas y Operacionales Consideradas en la Modelación

Tomando en consideración las concentraciones máximas de gases de salida y las especificaciones

técnicas entregadas por el proveedor de los hornos de pirólisis, se determinaron las siguientes

variables necesarias para la modelación de dispersión atmosférica:

 - Tasa de emisión del contaminante (g/s, kg/h, ton/año, etc.).

 - Temperatura de salida de los gases (K).

 - Altura de la fuente emisora (m).

 - Diámetro interno del ducto de salida (m).

 - Velocidad de salida de los gases (m/s).

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

47

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**6.5.1** **Chimeneas de Hornos de Pirólisis**

En la siguiente tabla se presentan las características físicas - operacionales de las chimeneas de los

hornos de pirólisis del proyecto:

**Tabla N° 9: Características físicas - operacionales de las chimeneas del proyecto.**

|Fuente|Altura de<br>emisión (m)|Temperatura gases<br>de salida (K)|Diámetro<br>interno (m)|Velocidad gases<br>de salida (m/s)|(*) Flujo de<br>salida (m3/h)|(**) Flujo de salida<br>Normal (m3N/h)|
|---|---|---|---|---|---|---|
|Chimenea N°1|17,00|553,15|0,40|12,47|5.641|2.937|
|Chimenea N°2|17,00|553,15|0,40|3,40|1.538|801|

(*) Flujo actual de gases de salida húmedos. (**)Flujo normal de gases secos a 25°C y 101 kPa.

Fuente: Elaboración propia en base a especificaciones técnicas de caldera.

Luego, para determinar las tasas de emisión se evaluó el peor escenario, considerando la máxima

concentración de las tres alternativas de insumos para cada uno de los contaminantes a modelar

(Ver Tabla N° 6). De esta forma se modeló la máxima tasa de emisión posible para cada uno de los

contaminantes, considerando una operación constante durante todo el año, sin pausas.

La siguiente tabla resume las máximas concentraciones y tasas de emisión por contaminante que

fueron consideradas en la modelación atmosférica. Las concentraciones, corregidas al porcentaje

de oxígeno real que salen los gases de las chimeneas, fueron multiplicadas por el correspondiente

flujo normal de gases secos presentado en la Tabla N° 9.

**Tabla N° 10: Concentración y tasas máximas de emisión de chimeneas del proyecto.**

|Contaminante|(*) Concentración (mg/m3N)|(**) Concentración (mg/m3N)|Emisión Chimenea N°1 (g/s)|Emisión Chimenea N°2 (g/s)|
|---|---|---|---|---|
|MP10|18|16,52|0,01348|0,00368|
|MP2,5|18|16,52|0,01348|0,00368|
|SO2|35|31,05|0,02534|0,00691|
|NOx|62,6|55,54|0,04532|0,01236|
|CO|39,4|34,96|0,02852|0,00778|
|COT|17|17,20|0,01403|0,00383|
|Cd|0,008|0,01|0,00001|0,000002|
|Be|0,01|0,01|0,00001|0,000002|
|Pb/Zn|0,4|0,40|0,00033|0,00009|
|HCl|12|12,14|0,00991|0,00270|
|Benceno|3|3,04|0,00248|0,00068|
|As/Co/Ni/Se/Te|0,9|0,91|0,00074|0,00020|
|Sb/Cr/Mn/V|2|1,77|0,00145|0,00039|
|Hf|1,3|1,32|0,00107|0,00029|
|Hg|0,01|0,01|0,00001|0,000002|
|Dioxin/Furans|1,40E-07|1,42E-07|1,156E-10|3,151E-11|

(*) En base seca, corregidas a 3% de oxígeno de acuerdo al D. S. N°29/13. (**) En base seca, corregidas al % oxígeno real de salida de los
gases: 5,03% Neumáticos, 4,48% Plásticos y 2,79% Aceites.

Fuente: Elaboración propia.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

48

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

Cabe destacar que para el MP10 y MP2,5 se utilizó como referencia la “Tabla 4: Factores de emisión

empleados por calderas GLP” de la “Guía Metodológica para la Estimación de Emisiones

Atmosféricas de Fuentes Fijas y Móviles en el RETC” de la CONAMA, que se su vez se basa en la “AP

42 de la EPA, LPG Combustion, Industrial Boilers, Quinta Edición/1998.”, en esta se observa que el

100% de Material Particulado emitido corresponde a MP10 y MP2,5, recordando que la combustión

de Gas Licuado de Petróleo es muy similar a la combustión del gas generado en la pirolisis de

neumáticos, plásticos y aceites.

**6.5.2** **Grupo Electrógeno de Emergencia**

Adicionalmente, se considerará el funcionamiento de un Grupo Electrógeno de Emergencia de 60

kVA (48 kW) de potencia, el cual se consideró que opera 0,5 horas a la semana. En la Tabla N° 11, se

resume la tasa de emisión de los contaminantes y las características físicas y operacionales del

Grupo Electrógeno de Emergencia.

**Tabla N° 11: Características Físicas - Operacionales y tasa de emisión (g/s) de Grupo Electrógeno de Emergencia.**

|Fuente|Altura<br>emisión (m)|Diámetro<br>interno (mm)|Velocidad Salida<br>Gases (m/s)|Temperatura<br>Salida Gases (K)|Contaminante|Factor de Emisión<br>(g/kW-h)|Tasa de<br>Emisión (g/s)|
|---|---|---|---|---|---|---|---|
|Grupo<br>Electrógeno de<br>Emergencia<br>(48 kW)|1,5|140|99,74|718,15|MP10|1,34|0,018|
|Grupo<br>Electrógeno de<br>Emergencia<br>(48 kW)|1,5|140|99,74|718,15|MP2,59|1,26|0,017|
|Grupo<br>Electrógeno de<br>Emergencia<br>(48 kW)|1,5|140|99,74|718,15|NOx|18,80|0,251|
|Grupo<br>Electrógeno de<br>Emergencia<br>(48 kW)|1,5|140|99,74|718,15|SO2|1,25|0,017|
|Grupo<br>Electrógeno de<br>Emergencia<br>(48 kW)|1,5|140|99,74|718,15|CO|4,06|0,054|

Fuente: Elaboración propia en base a especificaciones técnicas del Grupo Electrógeno y Factores de Emisión

de la “AP 42: Chapter 3, Section 3.4 “Large Stationary Diesel and All Stationary Dual-fuel Engines”.

**6.5.3** **Material Particulado Secundario**

Respecto al aporte secundario de material particulado, este se calculó usando el modelo

fotoquímico de Calpuff View: “MESOPUFF II”, el cual estima la formación de sulfatos (SO 4 ) y nitratos

(NO 3 ) a partir de los óxidos de nitrógeno (NOx) y dióxido de azufre (SO 2 ).

9 De acuerdo al “Appendix B.2: Generalized Particle Size Distributions” se encontraron porcentajes másicos para

“Stationary Internal Combustion Engines, Gasoline and Diesel Fuel”, donde se afirma que el MP2,5 corresponde a un 94%

del MP10.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

49

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

#### 7 Resultados de Modelación en los Receptores Discretos

Se procedió a estimar el aporte del Proyecto a la calidad del aire a través del modelo Calpuff. Esto

se hizo incluyendo la Estación de Monitoreo de Calidad del Aire Nogales, así como los receptores

sensibles identificados. Las plumas de dispersión son presentadas en el Apéndice 1 del presente

informe. En la Tabla N° 12 se presenta el resultado de los aportes del Proyecto sobre la Estación

Nogales para los contaminantes MP10, MP2,5, NO 2, SO 2, CO y Pb.

**Tabla N° 12: Concentraciones aportadas sobre Estación Nogales (μg/m** **[3]** **N).**

|Contaminante|Estadístico|Aporte<br>Primario|Aporte<br>Secundario|Aporte<br>Total|% Norma<br>Primaria|% Norma<br>Secundaria|Límites de<br>Normas|
|---|---|---|---|---|---|---|---|
|MP10|Promedio Anual|0,0002|0,0001|0,0003|0,0006%|-|50|
|MP10|Percentil 98 de 24 horas|0,0013|0,0011|0,0025|0,0016%|-|150|
|MP2,5|Promedio Anual|0,0002|0,0001|0,0003|0,0016%|-|20|
|MP2,5|Percentil 98 de 24 horas|0,0013|0,0011|0,0025|0,0049%|-|50|
|NO2|Promedio Anual|0,0003|-|0,0003|0,0003%|-|100|
|NO2|Percentil 99 Máx. 1 hora|0,0175|-|0,0175|0,0044%|-|400|
|SO2|Promedio Anual|0,0003|-|0,0003|0,0004%|0,0004%|80|
|SO2|Percentil 99 de 24 horas|0,0031|-|0,0031|0,0012%|-|250|
|SO2|Percentil 99,7 de 24 horas|0,0034|-|0,0034|-|0,0009%|365|
|SO2|Percentil 99,73 de 1 hora|0,0091|-|0,0091|-|0,0009%|1.000|
|CO|Percentil 99 Máx. 1 hora|0,0133|-|0,0133|0,00004%|-|30.000|
|CO|Percentil 99 Máx. 8 horas|0,0093|-|0,0093|0,00009%|-|10.000|
|Pb|Promedio Anual|3,32E-06|-|3,32E-06|0,0007%|-|0,5|

Fuente: Elaboración Propia.

Los resultados evidencian un muy bajo aporte del Proyecto sobre Estación Nogales, dado que

representa un aporte máximo, respecto a la norma, de MP10 de 0,0016% (Percentil 98 de 24 hrs),

0,0049% de MP2,5 (Percentil 98 de 24 hrs), 0,0044% de NO 2 (Percentil 99 de 1 hora), 0,0012% de

SO 2 (Percentil 99 de 24 hrs), 0,00009% de CO (Percentil 99 de 8 hrs) y 0,0007% de Pb (Promedio

anual).

A continuación se presentan los resultados de los aportes del Proyecto sobre los receptores

sensibles, para los contaminantes MP10, MP2,5, NO 2, SO 2, CO y Pb. La ubicación de los receptores

sensibles fue presentada en la Tabla N° 4y Figura N° 33.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

50

Modelación de Dispersión Atmosférica / Planta de Reciclaje de Aceites, Caucho y

Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Tabla N° 13: Concentraciones aportadas de MP10 sobre receptores sensibles (**  **g/m** **[3]** **N).**

|Receptor|Aporte Primario<br>Promedio anual|Aporte<br>Secundario<br>Promedio anual|Aporte Total<br>Promedio Anual|Norma<br>promedio<br>Anual|% Norma<br>promedio<br>anual|Percentil 98<br>de 24 horas<br>Primario|Percentil 98<br>de 24 horas<br>Secundario|Aporte<br>Total 24<br>horas|Norma 24<br>horas|% Norma<br>promedio 24<br>horas|
|---|---|---|---|---|---|---|---|---|---|---|
|Posta de Salud Rural Rungue|0,0018|0,0008|0,0026|50|0,0052%|0,0125|0,0052|0,0177|150|0,0118%|
|La Cumbre|0,0157|0,0019|0,0176|50|0,0352%|0,0831|0,0112|0,0943|150|0,0629%|
|Escuela Rungue|0,0019|0,0009|0,0029|50|0,0057%|0,0141|0,0063|0,0204|150|0,0136%|
|Escuela Santa Matilde|0,0016|0,0008|0,0024|50|0,0048%|0,0116|0,0061|0,0176|150|0,0118%|
|Escuela Capilla de Caleu|0,0002|0,0002|0,0004|50|0,0008%|0,0010|0,0009|0,0019|150|0,0013%|
|Jardín Infantil La Sonrisa|0,0003|0,0002|0,0005|50|0,0009%|0,0014|0,0012|0,0026|150|0,0017%|
|Escuela Básica Manchester College|0,0004|0,0003|0,0007|50|0,0014%|0,0028|0,0020|0,0049|150|0,0032%|
|Escuela San Pio De Pietrelcina|0,0004|0,0003|0,0007|50|0,0013%|0,0025|0,0018|0,0043|150|0,0029%|
|Cosam Til-Til|0,0004|0,0003|0,0007|50|0,0013%|0,0025|0,0018|0,0043|150|0,0028%|
|Jardín Infantil Los Angelitos|0,0004|0,0003|0,0007|50|0,0013%|0,0024|0,0019|0,0043|150|0,0029%|
|Escuela Plazuela de Polpaico|0,0002|0,0002|0,0004|50|0,0008%|0,0017|0,0013|0,0030|150|0,0020%|
|Posta de Salud Rural Polpaico|0,0002|0,0001|0,0003|50|0,0006%|0,0013|0,0011|0,0024|150|0,0016%|
|Escuela Básica Montenegro|0,0038|0,0013|0,0051|50|0,0101%|0,0253|0,0091|0,0345|150|0,0230%|
|Posta de Salud Rural Montenegro|0,0038|0,0013|0,0050|50|0,0101%|0,0252|0,0091|0,0344|150|0,0229%|
|Jardín Infantil Huechún|0,0004|0,0002|0,0006|50|0,0012%|0,0020|0,0013|0,0033|150|0,0022%|
|Consultorio Huertos Familiares|0,0003|0,0002|0,0005|50|0,0010%|0,0021|0,0013|0,0034|150|0,0022%|
|Escuela Especial La Huerta|0,0003|0,0002|0,0005|50|0,0009%|0,0019|0,0012|0,0032|150|0,0021%|
|Colegio Saint Louis School|0,0002|0,0002|0,0003|50|0,0007%|0,0014|0,0011|0,0025|150|0,0017%|
|Jardín Infantil mi Campito|0,0002|0,0002|0,0004|50|0,0007%|0,0009|0,0008|0,0017|150|0,0011%|
|Posta de Salud Rural Chacabuco|0,0002|0,0001|0,0003|50|0,0006%|0,0007|0,0007|0,0013|150|0,0009%|
|Posta de Salud Rural San Vicente|0,0001|0,0001|0,0001|50|0,0003%|0,0003|0,0004|0,0007|150|0,0004%|

Fuente: Elaboración propia.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

51

Modelación de Dispersión Atmosférica / Planta de Reciclaje de Aceites, Caucho y

Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Tabla N° 14: Concentraciones aportadas de MP2,5 sobre receptores sensibles (**  **g/m** **[3]** **N).**

|Receptor|Aporte Primario<br>Promedio anual|Aporte<br>Secundario<br>Promedio anual|Aporte Total<br>Promedio<br>Anual|Norma<br>promedio<br>Anual|% Norma<br>promedio<br>anual|Percentil 98 de<br>24 horas<br>Primario|Percentil 98<br>de 24 horas<br>Secundario|Aporte<br>Total 24<br>horas|Norma<br>24 horas|% Norma<br>promedio<br>24 horas|
|---|---|---|---|---|---|---|---|---|---|---|
|Posta de Salud Rural Rungue|0,0018|0,0008|0,0026|20|0,013%|0,0125|0,0052|0,0177|50|0,035%|
|La Cumbre|0,0157|0,0019|0,0176|20|0,088%|0,0831|0,0112|0,0943|50|0,189%|
|Escuela Rungue|0,0019|0,0009|0,0029|20|0,014%|0,0141|0,0063|0,0204|50|0,041%|
|Escuela Santa Matilde|0,0016|0,0008|0,0024|20|0,012%|0,0116|0,0061|0,0176|50|0,035%|
|Escuela Capilla de Caleu|0,0002|0,0002|0,0004|20|0,002%|0,0010|0,0009|0,0019|50|0,004%|
|Jardín Infantil La Sonrisa|0,0003|0,0002|0,0005|20|0,002%|0,0014|0,0012|0,0026|50|0,005%|
|Escuela Básica Manchester College|0,0004|0,0003|0,0007|20|0,004%|0,0028|0,0020|0,0049|50|0,010%|
|Escuela San Pio De Pietrelcina|0,0004|0,0003|0,0007|20|0,003%|0,0025|0,0018|0,0043|50|0,009%|
|Cosam Til-Til|0,0004|0,0003|0,0007|20|0,003%|0,0025|0,0018|0,0043|50|0,009%|
|Jardín Infantil Los Angelitos|0,0004|0,0003|0,0007|20|0,003%|0,0024|0,0019|0,0043|50|0,009%|
|Escuela Plazuela de Polpaico|0,0002|0,0002|0,0004|20|0,002%|0,0017|0,0013|0,0030|50|0,006%|
|Posta de Salud Rural Polpaico|0,0002|0,0001|0,0003|20|0,002%|0,0013|0,0011|0,0024|50|0,005%|
|Escuela Básica Montenegro|0,0038|0,0013|0,0051|20|0,025%|0,0253|0,0091|0,0344|50|0,069%|
|Posta de Salud Rural Montenegro|0,0038|0,0013|0,0050|20|0,025%|0,0252|0,0091|0,0344|50|0,069%|
|Jardín Infantil Huechún|0,0004|0,0002|0,0006|20|0,003%|0,0020|0,0013|0,0033|50|0,007%|
|Consultorio Huertos Familiares|0,0003|0,0002|0,0005|20|0,002%|0,0021|0,0013|0,0034|50|0,007%|
|Escuela Especial La Huerta|0,0003|0,0002|0,0005|20|0,002%|0,0019|0,0012|0,0032|50|0,006%|
|Colegio Saint Louis School|0,0002|0,0002|0,0003|20|0,002%|0,0014|0,0011|0,0025|50|0,005%|
|Jardín Infantil mi Campito|0,0002|0,0002|0,0004|20|0,002%|0,0009|0,0008|0,0017|50|0,003%|
|Posta de Salud Rural Chacabuco|0,0002|0,0001|0,0003|20|0,001%|0,0007|0,0007|0,0013|50|0,003%|
|Posta de Salud Rural San Vicente|0,0001|0,0001|0,0001|20|0,001%|0,0003|0,0004|0,0007|50|0,001%|

Fuente: Elaboración propia.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

52

Modelación de Dispersión Atmosférica / Planta de Reciclaje de Aceites, Caucho y

Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Tabla N° 15: Concentraciones aportadas de NO** **2** **sobre receptores sensibles (**  **g/m** **[3]** **N).**

|Receptor|Promedio<br>anual|% Norma<br>promedio anual|Percentil 99 Máx.<br>1 hora|% Norma percentil<br>99 Máx. 1 hora|Norma Promedio<br>anual|Norma Percentil 99<br>Máx. 1 hr|
|---|---|---|---|---|---|---|
|Posta de Salud Rural Rungue|0,0041|0,0041%|0,294|0,0736%|100|400|
|La Cumbre|0,0487|0,0487%|1,9821|0,4955%|100|400|
|Escuela Rungue|0,0046|0,0046%|0,323|0,0807%|100|400|
|Escuela Santa Matilde|0,0036|0,0036%|0,263|0,0658%|100|400|
|Escuela Capilla de Caleu|0,0004|0,0004%|0,010|0,0025%|100|400|
|Jardín Infantil La Sonrisa|0,0004|0,0004%|0,015|0,0038%|100|400|
|Escuela Básica Manchester College|0,0007|0,0007%|0,043|0,0107%|100|400|
|Escuela San Pio De Pietrelcina|0,0007|0,0007%|0,038|0,0095%|100|400|
|Cosam Til-Til|0,0007|0,0007%|0,038|0,0095%|100|400|
|Jardín Infantil Los Angelitos|0,0007|0,0007%|0,038|0,0094%|100|400|
|Escuela Plazuela de Polpaico|0,0004|0,0004%|0,022|0,0055%|100|400|
|Posta de Salud Rural Polpaico|0,0003|0,0003%|0,017|0,0042%|100|400|
|Escuela Básica Montenegro|0,0100|0,0100%|0,840|0,2101%|100|400|
|Posta de Salud Rural Montenegro|0,0100|0,0100%|0,841|0,2102%|100|400|
|Jardín Infantil Huechún|0,0006|0,0006%|0,030|0,0074%|100|400|
|Consultorio Huertos Familiares|0,0005|0,0005%|0,028|0,0070%|100|400|
|Escuela Especial La Huerta|0,0005|0,0005%|0,025|0,0062%|100|400|
|Colegio Saint Louis School|0,0003|0,0003%|0,016|0,0039%|100|400|
|Jardín Infantil mi Campito|0,0002|0,0002%|0,010|0,0025%|100|400|
|Posta de Salud Rural Chacabuco|0,0002|0,0002%|0,007|0,0017%|100|400|
|Posta de Salud Rural San Vicente|0,0001|0,0001%|0,002|0,0004%|100|400|

Fuente: Elaboración propia.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

53

Modelación de Dispersión Atmosférica / Planta de Reciclaje de Aceites, Caucho y

Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Tabla N° 16: Concentraciones aportadas de SO** **2** **sobre receptores sensibles (**  **g/m** **[3]** **N).**

|Receptor|Promedio<br>anual|% Norma<br>Primaria<br>promedio<br>anual|% Norma<br>Secundaria<br>promedio<br>anual|Percentil<br>99 de 24<br>horas|Percentil<br>99,7 de<br>24 horas|% Norma<br>percentil<br>99 de 24<br>horas|% Norma<br>percentil<br>99,7 de<br>24 horas|Percentil<br>99,73 de<br>1 hora|% Norma<br>percentil<br>99,73 de<br>1 hora|Normas<br>Anuales10|Normas<br>Percentil<br>99/99,7 de<br>24 horas11|Norma<br>percentil<br>99,73 de 1<br>hora12|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Posta de Salud Rural Rungue|0,0033|0,0041%|0,0041%|0,0249|0,0319|0,0100%|0,0087%|0,123|0,0123%|80/80|250/365|1.000|
|La Cumbre|0,0294|0,0367%|0,0367%|0,1718|0,1917|0,0687%|0,0525%|0,976|0,0976%|80/80|250/365|1.000|
|Escuela Rungue|0,0036|0,0045%|0,0045%|0,0323|0,0393|0,0129%|0,0108%|0,147|0,0147%|80/80|250/365|1.000|
|Escuela Santa Matilde|0,0029|0,0037%|0,0037%|0,0281|0,0319|0,0113%|0,0087%|0,110|0,0110%|80/80|250/365|1.000|
|Escuela Capilla de Caleu|0,0004|0,0005%|0,0005%|0,0021|0,0024|0,0009%|0,0007%|0,006|0,0006%|80/80|250/365|1.000|
|Jardín Infantil La Sonrisa|0,0005|0,0006%|0,0006%|0,0032|0,0037|0,0013%|0,0010%|0,009|0,0009%|80/80|250/365|1.000|
|Escuela Básica Manchester College|0,0008|0,0010%|0,0010%|0,0062|0,0078|0,0025%|0,0021%|0,022|0,0022%|80/80|250/365|1.000|
|Escuela San Pio De Pietrelcina|0,0007|0,0009%|0,0009%|0,0058|0,0069|0,0023%|0,0019%|0,019|0,0019%|80/80|250/365|1.000|
|Cosam Til-Til|0,0007|0,0009%|0,0009%|0,0058|0,0069|0,0023%|0,0019%|0,019|0,0019%|80/80|250/365|1.000|
|Jardín Infantil Los Angelitos|0,0007|0,0009%|0,0009%|0,0058|0,0069|0,0023%|0,0019%|0,019|0,0019%|80/80|250/365|1.000|
|Escuela Plazuela de Polpaico|0,0004|0,0005%|0,0005%|0,0038|0,0043|0,0015%|0,0012%|0,011|0,0011%|80/80|250/365|1.000|
|Posta de Salud Rural Polpaico|0,0003|0,0004%|0,0004%|0,0030|0,0034|0,0012%|0,0009%|0,009|0,0009%|80/80|250/365|1.000|
|Escuela Básica Montenegro|0,0071|0,0088%|0,0088%|0,0637|0,0777|0,0255%|0,0213%|0,359|0,0359%|80/80|250/365|1.000|
|Posta de Salud Rural Montenegro|0,0071|0,0088%|0,0088%|0,0636|0,0779|0,0255%|0,0213%|0,360|0,0360%|80/80|250/365|1.000|
|Jardín Infantil Huechún|0,0007|0,0008%|0,0008%|0,0040|0,0047|0,0016%|0,0013%|0,012|0,0012%|80/80|250/365|1.000|
|Consultorio Huertos Familiares|0,0005|0,0007%|0,0007%|0,0042|0,0049|0,0017%|0,0013%|0,013|0,0013%|80/80|250/365|1.000|
|Escuela Especial La Huerta|0,0005|0,0006%|0,0006%|0,0039|0,0042|0,0016%|0,0012%|0,012|0,0012%|80/80|250/365|1.000|
|Colegio Saint Louis School|0,0004|0,0004%|0,0004%|0,0031|0,0033|0,0012%|0,0009%|0,008|0,0008%|80/80|250/365|1.000|
|Jardín Infantil mi Campito|0,0004|0,0005%|0,0005%|0,0020|0,0023|0,0008%|0,0006%|0,005|0,0005%|80/80|250/365|1.000|
|Posta de Salud Rural Chacabuco|0,0003|0,0003%|0,0003%|0,0016|0,0021|0,0006%|0,0006%|0,004|0,0004%|80/80|250/365|1.000|
|Posta de Salud Rural San Vicente|0,0001|0,0001%|0,0001%|0,0006|0,0007|0,0003%|0,0002%|0,001|0,0001%|80/80|250/365|1.000|

Fuente: Elaboración propia.

10 Valor Límite de Norma Primaria / Valor Límite de Norma Secundaria
11 Valor Límite de Norma Primaria / Valor Límite de Norma Secundaria

12 Valor Límite de Norma Secundaria

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

54

Modelación de Dispersión Atmosférica / Planta de Reciclaje de Aceites, Caucho y

Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Tabla N° 17. Concentraciones aportadas de CO sobre receptores sensibles (**  **g/m** **[3]** **N).**

|Receptor|Percentil 99 Máx.<br>de 8 horas|% Norma Percentil<br>99 Máx. de 8 horas|Percentil 99<br>Máx. de 1 hora|% Norma percentil<br>99 de 1 hora|Norma Percentil<br>99 Máx. de 8hrs|Norma percentil 99<br>Máx. de 1hr|
|---|---|---|---|---|---|---|
|Posta de Salud Rural Rungue|0,078|0,00078%|0,226|0,00075%|10.000|30.000|
|La Cumbre|0,550|0,00550%|1,2491|0,00416%|10.000|30.000|
|Escuela Rungue|0,099|0,00099%|0,264|0,00088%|10.000|30.000|
|Escuela Santa Matilde|0,088|0,00088%|0,233|0,00078%|10.000|30.000|
|Escuela Capilla de Caleu|0,005|0,00005%|0,008|0,00003%|10.000|30.000|
|Jardín Infantil La Sonrisa|0,008|0,00008%|0,015|0,00005%|10.000|30.000|
|Escuela Básica Manchester College|0,019|0,00019%|0,031|0,00010%|10.000|30.000|
|Escuela San Pio De Pietrelcina|0,018|0,00018%|0,032|0,00011%|10.000|30.000|
|Cosam Til-Til|0,017|0,00017%|0,033|0,00011%|10.000|30.000|
|Jardín Infantil Los Angelitos|0,017|0,00017%|0,038|0,00013%|10.000|30.000|
|Escuela Plazuela de Polpaico|0,011|0,00011%|0,017|0,00006%|10.000|30.000|
|Posta de Salud Rural Polpaico|0,009|0,00009%|0,013|0,00004%|10.000|30.000|
|Escuela Básica Montenegro|0,200|0,00200%|0,651|0,00217%|10.000|30.000|
|Posta de Salud Rural Montenegro|0,199|0,00199%|0,651|0,00217%|10.000|30.000|
|Jardín Infantil Huechún|0,009|0,00009%|0,020|0,00007%|10.000|30.000|
|Consultorio Huertos Familiares|0,012|0,00012%|0,022|0,00007%|10.000|30.000|
|Escuela Especial La Huerta|0,011|0,00011%|0,021|0,00007%|10.000|30.000|
|Colegio Saint Louis School|0,008|0,00008%|0,015|0,00005%|10.000|30.000|
|Jardín Infantil mi Campito|0,005|0,00005%|0,009|0,00003%|10.000|30.000|
|Posta de Salud Rural Chacabuco|0,004|0,00004%|0,005|0,00002%|10.000|30.000|
|Posta de Salud Rural San Vicente|0,002|0,00002%|0,002|0,00001%|10.000|30.000|

Fuente: Elaboración propia.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

55

Modelación de Dispersión Atmosférica / Planta de Reciclaje de Aceites, Caucho y

Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Tabla N° 18. Concentraciones aportadas de Pb sobre receptores sensibles (**  **g/m** **[3]** **N).**

|Receptor|Promedio Anual|% Norma|Norma Promedio Anual|
|---|---|---|---|
|Posta de Salud Rural Rungue|0,000034|0,0069%|0,5|
|La Cumbre|0,000280|0,0560%|0,5|
|Escuela Rungue|0,000038|0,0077%|0,5|
|Escuela Santa Matilde|0,000031|0,0062%|0,5|
|Escuela Capilla de Caleu|0,000004|0,0009%|0,5|
|Jardín Infantil La Sonrisa|0,000005|0,0010%|0,5|
|Escuela Básica Manchester College|0,000008|0,0016%|0,5|
|Escuela San Pio De Pietrelcina|0,000007|0,0015%|0,5|
|Cosam Til-Til|0,000007|0,0015%|0,5|
|Jardín Infantil Los Angelitos|0,000007|0,0015%|0,5|
|Escuela Plazuela de Polpaico|0,000004|0,0009%|0,5|
|Posta de Salud Rural Polpaico|0,000003|0,0007%|0,5|
|Escuela Básica Montenegro|0,000072|0,0143%|0,5|
|Posta de Salud Rural Montenegro|0,000071|0,0143%|0,5|
|Jardín Infantil Huechún|0,000007|0,0014%|0,5|
|Consultorio Huertos Familiares|0,000006|0,0011%|0,5|
|Escuela Especial La Huerta|0,000005|0,0010%|0,5|
|Colegio Saint Louis School|0,000004|0,0008%|0,5|
|Jardín Infantil mi Campito|0,000004|0,0008%|0,5|
|Posta de Salud Rural Chacabuco|0,000003|0,0006%|0,5|
|Posta de Salud Rural San Vicente|0,000001|0,0002%|0,5|

Fuente: Elaboración propia.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

56

Modelación de Dispersión Atmosférica / Planta de Reciclaje de Aceites, Caucho y

Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Tabla N° 19. Concentraciones aportadas de gases y metales no normados sobre receptores sensibles (**  **g/m** **[3]** **N).**

|Receptor|Promedio<br>Anual COT|Promedio<br>Anual Cd|Promedio<br>Anual Be|Promedio<br>Anual HCl|Promedio Anual<br>Benceno|Promedio Anual<br>As/Co/Ni/Se/Te|Promedio Anual<br>Sb/Cr/Mn/V|Promedio<br>Anual HF|Promedio<br>Anual Hg|Promedio Anual<br>Dioxinas/Furanos|
|---|---|---|---|---|---|---|---|---|---|---|
|Estación Nogales|1,76E-04|1,18E-08|1,18E-08|1,24E-04|3,12E-05|9,27E-06|1,81E-05|1,34E-05|1,18E-08|1,45E-12|
|Posta de Salud Rural Rungue|1,83E-03|1,23E-07|1,23E-07|1,29E-03|3,23E-04|9,61E-05|1,88E-04|1,39E-04|1,23E-07|1,50E-11|
|La Cumbre|1,63E-02|1,07E-06|1,07E-06|1,15E-02|2,88E-03|8,55E-04|1,67E-03|1,24E-03|1,07E-06|1,34E-10|
|Escuela Rungue|2,02E-03|1,36E-07|1,36E-07|1,43E-03|3,58E-04|1,06E-04|2,08E-04|1,54E-04|1,36E-07|1,67E-11|
|Escuela Santa Matilde|1,65E-03|1,11E-07|1,11E-07|1,16E-03|2,92E-04|8,68E-05|1,70E-04|1,26E-04|1,11E-07|1,36E-11|
|Escuela Capilla de Caleu|2,28E-04|1,53E-08|1,53E-08|1,61E-04|4,04E-05|1,20E-05|2,35E-05|1,74E-05|1,53E-08|1,88E-12|
|Jardín Infantil La Sonrisa|2,68E-04|1,79E-08|1,79E-08|1,89E-04|4,74E-05|1,41E-05|2,76E-05|2,04E-05|1,79E-08|2,20E-12|
|Escuela Básica Manchester College|4,33E-04|2,91E-08|2,91E-08|3,06E-04|7,66E-05|2,28E-05|4,46E-05|3,30E-05|2,91E-08|3,57E-12|
|Escuela San Pio De Pietrelcina|3,90E-04|2,62E-08|2,62E-08|2,76E-04|6,91E-05|2,05E-05|4,02E-05|2,97E-05|2,62E-08|3,22E-12|
|Cosam Til-Til|3,92E-04|2,63E-08|2,63E-08|2,76E-04|6,93E-05|2,06E-05|4,03E-05|2,98E-05|2,63E-08|3,23E-12|
|Jardín Infantil Los Angelitos|3,96E-04|2,65E-08|2,65E-08|2,79E-04|7,00E-05|2,08E-05|4,07E-05|3,01E-05|2,65E-08|3,26E-12|
|Escuela Plazuela de Polpaico|2,30E-04|1,54E-08|1,54E-08|1,62E-04|4,07E-05|1,21E-05|2,37E-05|1,75E-05|1,54E-08|1,89E-12|
|Posta de Salud Rural Polpaico|1,73E-04|1,16E-08|1,16E-08|1,22E-04|3,06E-05|9,10E-06|1,78E-05|1,32E-05|1,16E-08|1,42E-12|
|Escuela Básica Montenegro|3,94E-03|2,62E-07|2,62E-07|2,78E-03|6,97E-04|2,07E-04|4,05E-04|3,00E-04|2,62E-07|3,24E-11|
|Posta de Salud Rural Montenegro|3,93E-03|2,61E-07|2,61E-07|2,77E-03|6,95E-04|2,07E-04|4,05E-04|2,99E-04|2,61E-07|3,24E-11|
|Jardín Infantil Huechún|3,81E-04|2,56E-08|2,56E-08|2,69E-04|6,74E-05|2,01E-05|3,92E-05|2,90E-05|2,56E-08|3,14E-12|
|Consultorio Huertos Familiares|2,98E-04|2,00E-08|2,00E-08|2,11E-04|5,28E-05|1,57E-05|3,07E-05|2,27E-05|2,00E-08|2,46E-12|
|Escuela Especial La Huerta|2,74E-04|1,84E-08|1,84E-08|1,94E-04|4,86E-05|1,44E-05|2,83E-05|2,09E-05|1,84E-08|2,26E-12|
|Colegio Saint Louis School|2,01E-04|1,35E-08|1,35E-08|1,42E-04|3,55E-05|1,06E-05|2,07E-05|1,53E-05|1,35E-08|1,65E-12|
|Jardín Infantil mi Campito|2,09E-04|1,40E-08|1,40E-08|1,47E-04|3,69E-05|1,10E-05|2,15E-05|1,59E-05|1,40E-08|1,72E-12|
|Posta de Salud Rural Chacabuco|1,61E-04|1,08E-08|1,08E-08|1,14E-04|2,85E-05|8,46E-06|1,66E-05|1,22E-05|1,08E-08|1,32E-12|
|Posta de Salud Rural San Vicente|6,46E-05|4,33E-09|4,33E-09|4,56E-05|1,14E-05|3,40E-06|6,66E-06|4,92E-06|4,33E-09|5,33E-13|

Fuente: Elaboración propia.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

57

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

En las tablas anteriores se puede apreciar que el aporte del Proyecto sobre los receptores sensibles es

relativamente bajo, si se compara con la normativa primaria y secundaria de calidad del aire, por lo cual,

no se evidencia un riesgo a la salud de la población o al estado de los recursos naturales.

Lo anterior, dado que el máximo aporte, respecto a la norma, para MP10 fue de 0,063% (Percentil 98 de

24 hrs), 0,189% de MP2,5 (Percentil 98 de 24 hrs), 0,50% de NO 2 (Percentil 99 de 1 hora), 0,098% de SO 2

(Percentil 99,73 de 1 hora), 0,0055% de CO (Percentil 99 de 8 horas) y 0,056% de Pb (Promedio anual).

En la siguiente tabla se identifican los puntos de máximo impacto (PMI) determinados a través de la

modelación con Calpuff View para los contaminantes MP10, MP2,5, NO 2, SO 2, CO y Pb.

**Tabla N° 20: Concentraciones determinadas en los Puntos de Máximo Impacto (**  **g/m** **[3]** **N).**

|Contaminante|Estadístico|Aporte<br>Primario|Aporte<br>Secundario|Aporte<br>Total en<br>PMI|Normas<br>de<br>calidad|% Norma<br>Primaria|% Norma<br>Secundaria|Coordenadas UTM<br>(m), Huso 18 sur|Distancia del<br>Proyecto|
|---|---|---|---|---|---|---|---|---|---|
|MP10|Promedio Anual|0,033|0,002|0,035|50|0,07%|-|X = 331.112|0,70 km al NE|
|MP10|Promedio Anual|0,033|0,002|0,035|50|0,07%|-|Y = 6.353.528|Y = 6.353.528|
|MP10|Percentil 98 de 24<br>horas|0,121|0,015|0,136|150|0,09%|-|X = 331.112|0,70 km al NE|
|MP10|Percentil 98 de 24<br>horas|0,121|0,015|0,136|150|0,09%|-|Y = 6.353.528|Y = 6.353.528|
|MP2.5|Promedio Anual|0,033|0,002|0,035|20|0,17%|-|X = 331.112|0,70 km al NE|
|MP2.5|Promedio Anual|0,033|0,002|0,035|20|0,17%|-|Y = 6.353.528|Y = 6.353.528|
|MP2.5|Percentil 98 de 24<br>horas|0,121|0,015|0,136|50|0,27%|-|X = 331.112|0,70 km al NE|
|MP2.5|Percentil 98 de 24<br>horas|0,121|0,015|0,136|50|0,27%|-|Y = 6.353.528|Y = 6.353.528|
|NO2|Promedio Anual|0,102|-|0,102|100|0,10%|-|X = 331.112|0,70 km al NE|
|NO2|Promedio Anual|0,102|-|0,102|100|0,10%|-|Y = 6.353.528|Y = 6.353.528|
|NO2|Percentil 99 Máx. 1<br>hora|2,881|-|2,881|400|0,72%|-|X = 331.112|0,70 km al NE|
|NO2|Percentil 99 Máx. 1<br>hora|2,881|-|2,881|400|0,72%|-|Y = 6.353.528|Y = 6.353.528|
|SO2|Promedio Anual|0,061|-|0,061|80|0,08%|0,08%|X = 331.112|0,70 km al NE|
|SO2|Promedio Anual|0,061|-|0,061|80|0,08%|0,08%|Y = 6.353.528|Y = 6.353.528|
|SO2|Percentil 99 de 24<br>horas|0,281|-|0,281|250|0,11%|-|X = 331.112|0,70 km al NE|
|SO2|Percentil 99 de 24<br>horas|0,281|-|0,281|250|0,11%|-|Y = 6.353.528|Y = 6.353.528|
|SO2|Percentil 99,7 de<br>24 horas|0,332|-|0,332|365|-|0,09%|X = 331.112|0,70 km al NE|
|SO2|Percentil 99,7 de<br>24 horas|0,332|-|0,332|365|-|0,09%|Y = 6.353.528|Y = 6.353.528|
|SO2|Percentil 99,73 de<br>1 hora|1,380|-|1,380|1.000|-|0,14%|X = 331.112|0,70 km al NE|
|SO2|Percentil 99,73 de<br>1 hora|1,380|-|1,380|1.000|-|0,14%|Y = 6.353.528|Y = 6.353.528|
|CO|Percentil 99 Máx. 1<br>hora|1,873|-|1,873|30.000|0,006%|-|X = 331.112|0,70 km al NE|
|CO|Percentil 99 Máx. 1<br>hora|1,873|-|1,873|30.000|0,006%|-|Y = 6.353.528|Y = 6.353.528|
|CO|Percentil 99 Máx. 8<br>horas|0,801|-|0,801|10.000|0,008%|-|X = 331.112|0,70 km al NE|
|CO|Percentil 99 Máx. 8<br>horas|0,801|-|0,801|10.000|0,008%|-|Y = 6.353.528|Y = 6.353.528|
|Pb|Promedio Anual|6,00E-04|-|0,0006|0,5|0,12%|-|X = 331.112|0,70 km al NE|
|Pb|Promedio Anual|6,00E-04|-|0,0006|0,5|0,12%|-|Y = 6.353.528|Y = 6.353.528|

Fuente: Elaboración propia.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

58

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

Luego del análisis de los datos presentados en la tabla anterior, es posible indicar que los máximos

aportes del Proyecto en el Punto de Máximo Impacto representan para el MP10 un aporte máximo de

0,09 % de la norma (Percentil 98 de 24 horas); para el caso del MP2,5 el aporte máximo corresponde a

0,27% de la norma (Percentil 98 de 24 horas), para el caso del NO 2 el aporte máximo corresponde a un

0,72% de la norma (Percentil 99 de 1 hora), para el SO 2 el aporte máximo corresponde a un 0,14% de la

norma secundaria (Percentil 99,73 de 1 hora), para el CO el aporte máximo corresponde a un 0,008% de

la norma (Percentil 99 de 8 horas) y para el Pb el aporte máximo es de 0,12% de la norma (Promedio

anual). Por otro lado, se observa que las coordenadas geográficas de los PMI corresponden siempre al

mismo punto para todos los contaminantes y periodos evaluados.

Adicionalmente, a continuación se presentan las máximas concentraciones modeladas, para el resto de

gases y metales pesados no normados en los Puntos de Máximo Impacto (PMI).

**Tabla N° 21: Concentraciones de gases y metales sin norma de calidad en los Puntos de Máximo**

**Impacto (**  **g/m** **[3]** **N).**

|Contaminante|Estadístico|Aporte Total en<br>PMI|Coordenadas UTM (m),<br>Huso 18 sur|Distancia del<br>Proyecto|
|---|---|---|---|---|
|COT|Promedio Anual|0,034|X = 331.112|0,70 km al NE|
|COT|Promedio Anual|0,034|Y = 6.353.528|Y = 6.353.528|
|Cd|Promedio Anual|2,20E-06|X = 331.112|0,70 km al NE|
|Cd|Promedio Anual|2,20E-06|Y = 6.353.528|Y = 6.353.528|
|Be|Promedio Anual|2,20E-06|X = 331.112|0,70 km al NE|
|Be|Promedio Anual|2,20E-06|Y = 6.353.528|Y = 6.353.528|
|HCl|Promedio Anual|0,024|X = 331.112|0,70 km al NE|
|HCl|Promedio Anual|0,024|Y = 6.353.528|Y = 6.353.528|
|Benceno|Promedio Anual|0,006|X = 331.112|0,70 km al NE|
|Benceno|Promedio Anual|0,006|Y = 6.353.528|Y = 6.353.528|
|As/Co/Ni/Se/Te|Promedio Anual|0,002|X = 331.112|0,70 km al NE|
|As/Co/Ni/Se/Te|Promedio Anual|0,002|Y = 6.353.528|Y = 6.353.528|
|Sb/Cr/Mn/V|Promedio Anual|0,004|X = 331.112|0,70 km al NE|
|Sb/Cr/Mn/V|Promedio Anual|0,004|Y = 6.353.528|Y = 6.353.528|
|HF|Promedio Anual|0,003|X = 331.112|0,70 km al NE|
|HF|Promedio Anual|0,003|Y = 6.353.528|Y = 6.353.528|
|Hg|Promedio Anual|2,20E-06|X = 331.112|0,70 km al NE|
|Hg|Promedio Anual|2,20E-06|Y = 6.353.528|Y = 6.353.528|
|Dioxinas/Furanos|Promedio Anual|2,79E-10|X = 331.112|0,70 km al NE|
|Dioxinas/Furanos|Promedio Anual|2,79E-10|Y = 6.353.528|Y = 6.353.528|

Fuente: Elaboración propia.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

59

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

En la tabla anterior, se observa que las coordenadas geográficas de los PMI corresponden al mismo

punto para todos los contaminantes y periodos evaluados, siendo el mismo punto que los

contaminantes normados.

La siguiente figura muestra la ubicación del Punto de Máximo Impacto del Proyecto, evidenciándose que

este se localiza en un sector deshabitado con escasa vegetación, a aproximadamente 700 metros al

noreste del proyecto.

**Figura N° 35. Punto de Máximo Impacto del Proyecto.**

Fuente: Elaboración propia en base a modelación Calpuff View y Google Earth Pro.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

60

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

#### 8. Aporte del Proyecto a la Línea de Base de Calidad del Aire

Para evaluar la calidad del aire resultante en los receptores considerados en la modelación, se utilizó

como referencia la línea de base (LB) medida en la Estación Nogales, a las cuales se les sumó los aportes

del Proyecto presentados en la sección anterior, para finalmente evaluar el cumplimiento legal de las

respectivas normas de calidad del aire.

**8.1** **. Análisis de Cumplimiento Normativo en Estación de Monitoreo**

En la Tabla N° 22 se analiza el cumplimiento normativo en relación a la concentración de los distintos

contaminantes observados en Estación Nogales.

**Tabla N° 22: Concentración final modelada en Estación Nogales (**  **g/m** **[3]** **N).**

|Contaminante|Estadístico|Aporte Total<br>Modelado|LB|Aporte +<br>LB|Límites de<br>Normas|% Norma<br>Primaria|% Norma<br>Secundaria|
|---|---|---|---|---|---|---|---|
|MP10|Promedio Anual|0,0003|77,793|77,793|50|**155,59%**|-|
|MP10|Percentil 98 de 24 horas|0,0025|144,100|144,102|150|96,07%|-|
|MP2,5|Promedio Anual|0,0003|28,783|28,784|20|**143,92%**|-|
|MP2,5|Percentil 98 de 24 horas|0,0025|53,317|53,319|50|**106,64%**|-|
|NO2|Promedio Anual|0,0003|24,471|24,471|100|24,47%|-|
|NO2|Percentil 99 Máx. 1 hora|0,0175|89,200|89,218|400|22,30%|-|
|SO2|Promedio Anual|0,0003|8,887|8,887|80/8013|11,11%|11,11%|
|SO2|Percentil 99 de 24 horas|0,0031|16,800|16,803|250|6,72%|-|
|SO2|Percentil 99,7 de 24 horas|0,0034|17,600|17,603|36514|-|4,82%|
|SO2|Percentil 99,73 de 1 hora|0,0091|21,700|21,709|1.00015|-|2,17%|
|CO|Percentil 99 Máx. 1 hora|0,0133|3.690,00|3.690,01|30.000|12,30%|-|
|CO|Percentil 99 Máx. 8 horas|0,0093|2.410,00|2.410,01|10.000|24,10%|-|
|Pb|Promedio Anual|3,32E-06|0,0018|0,0018|0,5|0,36%|-|

Fuente: Elaboración propia.

De acuerdo a los resultados presentados, es posible indicar que los aportes del Proyecto sobre la línea

de base de Estación Nogales, generan un incremento mínimo de las concentraciones de contaminantes

basales. Por otra parte, no se provoca ningún estado de saturación ni latencia extra, recordando que la

13 Valor límite de Norma Primaria / Valor Límite de Norma Secundaria.

14 Valor Límite de Norma Secundaria.

15 Valor Límite de Norma Secundaria.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

61

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

línea de base actual de Estación Nogales (sin Proyecto), evidenció niveles que tienden a la saturación

para MP2,5, como promedio anual y diario, y una tendencia a estado de saturación para MP10,

específicamente como promedio anual (Ver Tabla N° 7), en otras palabras, el Proyecto no modifica de

manera significativa la tendencia a saturación que presenta la Línea de Base de Estación Nogales para

MP2,5 y MP10, ni provoca que otros contaminantes entren a esta tendencia.

**8.2** **. Análisis de Cumplimiento Normativo en Punto de Máximo Impacto**

A continuación se analiza el cumplimiento normativo en relación a la concentración de los distintos

contaminantes en el Punto de Máximo Impacto o PMI (μg/m [3] N) considerando que la línea base (LB)

podría ser similar a lo medido en la Estación Nogales.

**Tabla N° 23: Concentración final modelada en PMI (**  **g/m** **[3]** **N) respecto a LB de Estación Nogales.**

|Contaminante|Estadístico|Aporte Total<br>en PMI|LB E. Nogales|Aporte + LB|Normas de<br>calidad|% Norma<br>Primaria|% Norma<br>Secundaria|
|---|---|---|---|---|---|---|---|
|MP10|Promedio Anual|0,035|77,793|77,827|50|**155,65%**|-|
|MP10|Percentil 98 de 24 horas|0,136|144,100|144,236|150|96,16%|-|
|MP2.5|Promedio Anual|0,035|28,783|28,818|20|**144,09%**|-|
|MP2.5|Percentil 98 de 24 horas|0,136|53,317|53,453|50|**106,91%**|-|
|NO2|Promedio Anual|0,102|24,471|24,573|100|24,57%|-|
|NO2|Percentil 99 Máx. 1 hora|2,881|89,200|92,081|400|23,02%|-|
|SO2|Promedio Anual|0,061|8,887|8,948|80|11,19%|11,19%|
|SO2|Percentil 99 de 24 horas|0,281|16,800|17,081|250|6,83%|-|
|SO2|Percentil 99,7 de 24 horas|0,332|17,600|17,932|365|-|4,91%|
|SO2|Percentil 99,73 de 1 hora|1,380|21,700|23,080|1.000|-|2,31%|
|CO|Percentil 99 Máx. 1 hora|1,873|3.690|3.692|30.000|12,31%|-|
|CO|Percentil 99 Máx. 8 horas|0,801|2.410|2.411|10.000|24,11%|-|
|Pb|Promedio Anual|0,0006|0,0018|0,0024|0,5|0,48%|-|

Fuente: Elaboración propia.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

62

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

Luego del análisis de los datos presentados en la tabla anterior, es posible indicar que la suma de los

aportes en el PMI calculados no modifica de manera relevante la línea de base referencial establecida

para todos los estadísticos. Por otra parte, no se provoca ningún estado de saturación ni latencia extra,

recordando que la línea de base actual de Estación Nogales (sin Proyecto), evidenció niveles que tienden

a la saturación para MP2,5, como promedio anual y diario, y una tendencia a estado de saturación para

MP10, específicamente como promedio anual (Ver Tabla N° 7).

#### 8 Conclusiones

Se realizó una modelación meteorológica para el lugar en el que se encuentra el Proyecto con el modelo

numérico Weather Research and Forecasting Model (WRF) y se realizó un análisis de la calidad de la

modelación comparando los valores modelados con los observados en la Estación Nogales. Entre las

principales conclusiones se encuentran:

 - El modelo predice bien el ciclo de las velocidades del viento aunque sobrestima levemente las

magnitudes principalmente en las horas de la tarde (entre las 14:00 y 18:00 horas).

 - Los vientos predominantes en el área poseen principalmente una componente Norte (N) y Sur

Nor-noreste (NNE), con predominancia de vientos que fluctúan entre los 0,5-3,6 m/s (60,8%).

Junto a lo anterior, y utilizando la información meteorológica modelada, se efectuó una modelación de

dispersión de contaminantes utilizando el software de modelación Calpuff View que es el modelo

recomendado de acuerdo a la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA” (SEA, 2013).

Entre las conclusiones de dicho modelo destacan las siguientes:

 - El aporte de MP10, MP2,5, NO 2, SO 2, CO y Pb tanto en la Estación de Monitoreo de Calidad del

Aire Nogales, como en el punto de máximo impacto (PMI) representa un aporte relativamente

bajo respecto a la línea de base (LB) actual en la comuna de Til Til y los límites normativos.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

63

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

 - Los máximos aportes del Proyecto en el Punto de Máximo Impacto sumado a la línea de base

registrada por la estación de calidad del aire más cercana al proyecto, Estación Nogales, no

modifican de manera relevante los niveles observados. Por otra parte, no se provoca ningún

estado de saturación ni latencia extra, recordando que la línea de base actual de Estación

Nogales (sin Proyecto), evidenció niveles que tienden a la saturación para MP2,5, como

promedio anual y diario, y una tendencia a estado de saturación para MP10, específicamente

como promedio anual (Ver Tabla N° 23).

Con los resultados obtenidos es posible afirmar que ninguno de estos aportes generados por el Proyecto

constituye un verdadero riesgo a la salud de las personas o a los recursos naturales, ni una modificación

significativa en los valores de línea de base registrados en Estación Nogales.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

64

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Apéndice 1**

#### GRÁFICAS DE SALIDA DE SOFTWARE CALPUFF VIEW

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

65

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1. 1. Concentración MP10 promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

66

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1. 2. Concentración MP10 percentil 98 de 24 horas (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

67

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.3. Concentración MP2,5 promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

68

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.4. Concentración MP2,5 percentil 98 de 24 horas (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

69

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.5. Concentración NOx promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

70

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.6. Concentraciones Máximas NOx de 1 hora (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

71

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.7. Concentración SO** **2** **promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

72

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.8. Concentración SO** **2** **Percentil 99 de 24 horas (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

73

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.9. Concentración SO** **2** **Percentil 99,7 de 24 horas (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

74

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.10. Concentraciones Máximas SO** **2** **de 1 hora (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

75

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.11. Concentraciones Máximas CO de 8 horas (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

76

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.12. Concentraciones Máximas CO de 1 hora (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

77

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.13. Concentración As/Co/Ni/Se/Te promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

78

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.14. Concentración Benceno promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

79

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.15. Concentración Berilio (Be) promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

80

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.16. Concentración Cadmio (Cd) promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

81

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.17. Concentración COT promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

82

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.18. Concentración Dioxinas/Furanos promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

83

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.19. Concentración HCl promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

84

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.20. Concentración HF promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

85

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.21. Concentración Mercurio (Hg) promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

86

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.22. Concentración Plomo (Pb)/Zinc (Zn) promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

87

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Figura 1.23. Concentración Sb/Cr/Mn/V promedio anual (μg/m** **[3]** **N).**

Fuente: Elaboración propia mediante Calpuff View.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

88

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Apéndice 2**

#### Series de Tiempo de Calidad del Aire observada por Estación Nogales Periodo: enero - agosto de 2015

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

89

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Gráfico N° 2. Serie de tiempo de MP10 observado en Estación Nogales.**

Fuente: Elaboración propia en base a registros de estación Nogales.

**Gráfico N° 3. Serie de tiempo de concentraciones diarias (*) de SO** **2** **observadas en Estación Nogales.**

(*) Norma primaria: 250 μg/m [3] N. Norma secundaria: 365 μg/m [3] N.

Fuente: Elaboración propia en base a registros de estación Nogales.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

90

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Gráfico N° 4. Serie de tiempo concentraciones horarias (*) de SO** **2** **observadas en Estación Nogales.**

(*) Norma secundaria: 1000 μg/m [3] N.

Fuente: Elaboración propia en base a registros de estación Nogales.

**Gráfico N° 5. Serie de tiempo de NO** **2** **observado en Estación Nogales.**

Fuente: Elaboración propia en base a registros de estación Nogales.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

91

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Gráfico N° 6. Serie de tiempo de concentraciones 1 hora de CO observado en Estación Nogales.**

Fuente: Elaboración propia en base a registros de estación Nogales.

**Gráfico N° 7. Serie de tiempo de concentraciones 8 horas de CO observado en Estación Nogales.**

Fuente: Elaboración propia en base a registros de estación Nogales.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

92

Modelación de Dispersión Atmosférica / Planta de

Reciclaje de Aceites, Caucho y Plásticos Fuera de Uso

Declaración de Impacto Ambiental

**Gráfico N° 8. Concentraciones de Pb observado en Estación Nogales.**

Fuente: Elaboración propia en base a registros de estación Nogales.

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

93