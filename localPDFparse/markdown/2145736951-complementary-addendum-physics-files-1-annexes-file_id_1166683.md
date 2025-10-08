---
title: PERFIL DE PROYECTO 
“DISEÑO DE UNA MICROCENTRAL HIDROELÉCTRICA Y REDES DE DISTRIBUCIÓN PARA LA LOCALIDAD DE PIREHUEICO”
author: hfgodoy@outlook.com
date: D:20200710165108-04'00'
language: es
type: report
pages: 44
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MEMORIA DE CÁLCULO HIDROLÓGICO
-->

# MEMORIA DE CÁLCULO HIDROLÓGICO

## PROYECTO “PLANTA FOTOVOLTAICA NORTH WEST”

**REGIÓN DE ATACAMA**

JUNIO - 2020

CURICÓ - CHILE

**CONTENIDO**

1. INTRODUCCIÓN .................................................................................................................................................................................. 3

1.1. Objetivo ...................................................................................................................................................................................... 4

2. ESTUDIO HIDROLÓGICO DE CAUDALES ......................................................................................................................................... 5

2.1. Metodología de cálculo .............................................................................................................................................................. 5

2.2. Definición de Microcuencas ....................................................................................................................................................... 8

2.3. Análisis de precipitaciones máximas ....................................................................................................................................... 10

2.4. Caudales Microcuencas ........................................................................................................................................................... 15

2.5. SIMULACIÓN HIDRÁULICO QUEBRADAS ............................................................................................................................ 16

2.5.1. MARCO TEÓRICO SIMULACIÓN HIDRÁULICA ............................................................................................................... 16

2.5.2. Coeficiente de Manning ....................................................................................................................................................... 17

2.5.3. Resultados .......................................................................................................................................................................... 19

3. CONCLUSIONES Y/O COMENTARIOS .............................................................................................................................. 23

4. ANEXOS ............................................................................................................................................................................................. 24

4.1. PERFILES TRANSVERSALES Mc-1 ....................................................................................................................................... 24

4.2. PERFILES TRANSVERSALES Mc-2 ....................................................................................................................................... 32

4.3. PERFILES TRANSVERSALES Mc-3 ....................................................................................................................................... 36

4.4. RESUMEN SIMULACIÓN HIDRÁULICA QUEBRADA Mc-1 ................................................................................................... 39

4.5. RESUMEN SIMULACIÓN HIDRÁULICA QUEBRADA Mc-2 ................................................................................................... 41

4.6. RESUMEN SIMULACIÓN HIDRÁULICA QUEBRADA Mc-3 ................................................................................................... 43

Contacto : contacto@emergeingenieria.cl
**1**
Teléfono : 752313453

**ÍNDICE DE FIGURAS**

F IGURA 1.1 U BICACIÓN G ENERAL DEL P ROYECTO ................................................................................................................................3

F IGURA 1.2 U BICACIÓN L OCAL DEL P ROYECTO ....................................................................................................................................4

F IGURA 2.1 P RINCIPALES M ICROCUENCAS INFLUYENTES AL Á REA DEL P ROYECTO .......................................................................................8

F IGURA 2.2 E STACIONES M ETEOROLÓGICAS S ELECCIONADAS ...............................................................................................................10

F IGURA 2.3 A NÁLISIS DE F RECUENCIA E STACIÓN E L T RAPICHE ..............................................................................................................13

F IGURA 2.4 A NÁLISIS DE F RECUENCIA E STACIÓN D OMEIKO ..................................................................................................................14

F IGURA 2 **.** 5. D ISTRIBUCIÓN P ERFILES EN QUEBRADAS PARA LAS TRES MICROCUENCAS ESTUDIADAS ..............................................................19

F IGURA 2.6. P ERFIL L ONGITUDINAL Q UEBRADA S IN NOMBRE ...............................................................................................................20

F IGURA 2.7. P ERFIL L ONGITUDINAL Q UEBRADA DE L OS N EGROS ..........................................................................................................21

F IGURA 2 **.** 8. P ERFIL L ONGITUDINAL Q UEBRADA DE L OS N EGROS ..........................................................................................................22

**ÍNDICE DE TABLAS**

T ABLA 2.1 C OEFICIENTES DE E SCORRENTÍA .........................................................................................................................................7

T ABLA 2.2 P ARÁMETROS M ICROCUENCAS ..........................................................................................................................................9

T ABLA 2.3 T IEMPO DE C ONCENTRACIÓN ............................................................................................................................................9

T ABLA 2.4 R ESUMEN E STACIONES M ETEOROLÓGICAS U TILIZADAS ........................................................................................................10

T ABLA 2.5 R EGISTRO DE PRECIPITACIONES MÁXIMAS ANUALES EN 24 HORAS ..........................................................................................11

T ABLA 2.6 T EST K OLMOGOROV S MIRNOV E L T RAPICHE ......................................................................................................................12

T ABLA 2.7 T EST K OLMOGOROV S MIRNOV E STACIÓN D OMEIKO ............................................................................................................13

T ABLA 2.8 R ESUMEN DE P RECIPITACIONES M ÁXIMAS EN 24 HORAS ......................................................................................................14

T ABLA 2.9 R ESUMEN M ÉTODO R ACIONAL, C AUDALES M C -1, M C -2 Y M C -3 .........................................................................................15

T ABLA 2.10. C OEFICIENTES DE M ANNING SEGÚN M ÉTODO DE C OWAN .................................................................................................18

T ABLA 2.11 V ALORES PARA LA OBTENCIÓN DE RUGOSIDAD SEGÚN C OWAN .............................................................................................18

T ABLA 4.1. S IMULACIÓN H IDRÁULICA M C -1 .....................................................................................................................................39

T ABLA 4.2. S IMULACIÓN H IDRÁULICA M C -2 .....................................................................................................................................41

T ABLA 4.3. S IMULACIÓN H IDRÁULICA M C -3 .....................................................................................................................................43

Contacto : contacto@emergeingenieria.cl
**2**
Teléfono : 752313453

**1.** **INTRODUCCIÓN**

El proyecto “Planta Fotovoltaica North West”, en adelante el Proyecto, Corresponde a un nuevo proyecto de pequeños medios de

generación distribuida (PMGD), que producirá energía eléctrica a través de energías renovables no convencionales (ERNC), mediante la

construcción de una central de módulos fotovoltaicos, que captarán la radiación solar, inyectando hasta 9 MW al Sistema Eléctrico

Nacional (SEN). El Proyecto estará ubicado en la Región de Atacama, en la Provincia de Huasco, Comuna de Vallenar, accediendo al

mismo por la Ruta 5 Norte en dirección “Este” por un camino privado existente a la altura del km 620 de la ruta 5 norte, bifurcación a

1.600m pasado cruce con Ruta C-541 camino de acceso al observatorio La Silla. (Figura 1.1).

_Figura 1.1 Ubicación General del Proyecto_

Contacto : contacto@emergeingenieria.cl
**3**
Teléfono : 752313453

En este informe se estudiará la hidrología de la zona, detectando las quebradas ubicadas en las inmediaciones del proyecto y que

pudiesen afectar su funcionamiento normal bajo condiciones meteorológicas relevantes.

**1.1.** **Objetivo**

El objetivo de este informe, es definir las principales quebradas que pudiesen afectar al proyecto, y mediante un estudio hidrológico,

obtener caudales de escorrentía para periodos de retorno de hasta 200 años y menores, con el fin de estimar las inundaciones que

podrían afectar al proyecto y así dar respuesta a las consulta de la Adenda del proyecto . En la Figura 1.2, se presenta la ubicación del

proyecto de forma local con su entorno.

_Figura 1.2 Ubicación Local del Proyecto_

Contacto : contacto@emergeingenieria.cl
**4**
Teléfono : 752313453

**2.** **ESTUDIO HIDROLÓGICO DE CAUDALES**

En el presente informe se definen las quebradas y área aportante, obteniendo un caudal para condiciones de escorrentía superficial de

eventos meteorológicos significativos.

**2.1.** **Metodología de cálculo**

La metodología aplicada consistió en la recopilación y revisión de distintas fuentes de información existentes. Esta actividad fue apoyada

mediante el uso de Sistemas de Información Geográfica (SIG).

Inicialmente se realizó una caracterización hidrográfica regional del área de estudio, donde se identificaron las cuencas y principales

cauces en donde se emplaza el proyecto.

A continuación, se realizó una caracterización hidrográfica local, con el fin de identificar los principales cursos de agua y quebradas en el

área de interés.

Seguidamente, se calculó los parámetros morfométricos de quebradas sobre las que se ubica el proyecto, para luego determinar los

caudales de crecida para distintos periodos de retorno

Para la elaboración del presente informe, se consideraron las siguientes actividades.

 - Revisión de información secundaria

Para recabar los antecedentes necesarios para el presente informe, se consultó la base de datos de la Dirección General de Aguas

(DGA), de modo de caracterizar la climatología del sector.

 Trabajo de gabinete

El trabajo de gabinete consiste en las actividades que se presentan a continuación:

a) Fotointerpretación: Se revisan las imágenes satelitales disponibles, de modo de identificar posibles redes de escurrimiento y/o

quebradas naturales.

b) Análisis geomorfológico: Considerando los resultados de la fotointerpretación, se delimitaron las cuencas aportantes y se obtuvieron

los parámetros necesarios para la correcta estimación de caudales. Los parámetros que interesa describir son los siguientes:

Ap: Área aportante pluvial (km2)

L: Longitud del cauce principal (km)

H: Desnivel máximo de la cuenca (m), se obtiene de la diferencia entra la cota máxima (Hmax) y cota mínima (Hmin) de
la cuenca en estudio.

tc: Tiempo de concentración (hr), se estima según las expresiones de; Normas Españolas, California Culverts Practive
(1942) y Giandotti.

Contacto : contacto@emergeingenieria.cl
**5**
Teléfono : 752313453

c) Estimación de caudales: Para la estimación de caudales, se utilizó el Método Racional para cuencas menores a 20km [2], el cual se

presentan a continuación:

I. Método Racional

La Fórmula Racional, es una expresión que permite determinar el caudal instantáneo máximo de periodo de retorno T años es:

s
⁄ )

Q=

C(T) ∙i t c

tT c ∙A

3,6 ( [m] [3]

T

T = [P] [tc]

i t c

t c

-60 ( [mm] ⁄hr)

Donde:

Q : Caudal instantáneo máximo de periodo de retorno T, expresado en m3/s.

C : Coeficiente de escorrentía asociado al periodo de retorno T.

i tT c : Intensidad media de lluvia asociada al periodo de retorno T y a una duración igual al tiempo de concentración ( t c, en

minutos) de la cuenca pluvial, expresada en mm/hr.

A p : Área pluvial aportante, expresada en km2.

P tcT : Precipitación de periodo de retorno T, asociada a una duración de t c horas, en mm.

t c : Tiempo de concentración de la cuenca, en minutos.

Para transformar la precipitación máxima asociada a una duración en 24 horas a una duración igual al tiempo de concentración.

Para tiempo de concentración menor a 1 hora, se utilizara la fórmula de Bell:

T = (0,54 ∗t 0,25 −0,50) ∗P 1

P t

10

Dónde:

P tT : Precipitación con periodo de retorno T años y duración t minutos, en mm

P 110 : Precipitación con T = 10 años y duración de 1 hora, en mm.

Finalmente el coeficiente de escorrentía se obtendrá según lo propuesto en el Manual de Carretera Vol. 3, Tabla 3.702.503 (B)

Contacto : contacto@emergeingenieria.cl
**6**
Teléfono : 752313453

_Tabla 2.1 Coeficientes de Escorrentía_

Contacto : contacto@emergeingenieria.cl
**7**
Teléfono : 752313453

**2.2.** **Definición de Microcuencas**

A continuación se presenta el trazado de las principales Microcuencas que interfiere dentro del área del proyecto, cabe destacar que la

definición de las microcuencas se realizó en función de los postes de línea eléctrica.

_Figura 2.1 Principales Microcuencas influyentes al Área del Proyecto_

A nivel local se observan 3 microcuencas cercanas al proyecto, de estas se observan cauces que podrían causar daño en las obras del

proyecto producto de inundaciones, por lo tanto se han estimado cuencas con puntos de control pasadas las obras, con el fin de

sobrestimar el caudal asociado a cada microcuenca y tener magnitudes de caudal más conservadores.

Contacto : contacto@emergeingenieria.cl
**8**
Teléfono : 752313453

Los diferentes parámetros geomorfométricos de las microcuencas son presentados en las tablas 2.2 y 2.3.

_Tabla 2.2 Parámetros Microcuencas_

Microcuenca 1 5,22 4,16 1219 1100

Microcuenca 2 0,98 1,57 1161 1109

Microcuenca 5 0,36 1,15 1145 1109

_Tabla 2.3 Tiempo de Concentración_

**Microcuenca 1** 0,780 0,781 - 0,78

**Microcuenca 2** 0,348 0,349 - 0,35

**Microcuenca 5** 0,280 0,280 - 0,28

Contacto : contacto@emergeingenieria.cl
**9**
Teléfono : 752313453

**2.3.** **Análisis de precipitaciones máximas**

Para el cálculo de P 2410, se utilizo como referencia las estaciones Meteorológicas El Trapiche y Domeiko, las cuales se presentan en la

siguiente figura, mientras que sus principales datos se observan en la Tabla 2.4.

_Figura 2.2 Estaciones Meteorológicas Seleccionadas_

_Tabla 2.4 Resumen Estaciones Meteorológicas Utilizadas_

**Estación** **Código BNA** **Coordenada Norte [m]** **Coordenada Este [m]** **Altitud [m.s.n.m.]** **Año Registros**

**Domeiko** 03940001-4 6795593 315393 780 1994-2019

**El Trapiche** 04120001-4 6748816 294474 300 1979-2019

Contacto : contacto@emergeingenieria.cl
**10**
Teléfono : 752313453

_Tabla 2.5 Registro de precipitaciones máximas anuales en 24 horas_

**1980** 15.50 -

**1982** 13.00 -

**1984** 24.10 -

**1986** 9.50 -

**1988** 3.00 -

**1990** 13.50 -

**1992** 25.50 -

**1994** 2.50 1.00

**1996** 11.00 3.50

**1998** 0.00 4.50

**2000** 35.00 38.00

**2002** 28.00 28.00

**2004** 38.50 33.00

**2006** 10.50 2.50

**2008** 25.00 21.00

**2010** 16.50 18.00

**2012** 0.00 2.00

**2014** 32.50 17.00

**2016** 1.00 6.50

Contacto : contacto@emergeingenieria.cl
**11**
Teléfono : 752313453

**2018** 0.00 16.50

Para el estudio estadístico, se utilizó el software Hydrognomon diseñado para el análisis y procesamiento de datos hidrológicos,

principalmente bajo la forma de serie de tiempo, los resultados fueron validados con el programa HidroEsta.

En las siguientes Tablas se presentan los resultados del análisis de frecuencia para cada estación estudiada.

_Tabla 2.6 Test Kolmogorov Smirnov El Trapiche_

**Test Kolmogorov-Smirnov** **a=1%** **a=5%** **a=10%** **Porcentaje** **DMax**

Normal ACCEPT ACCEPT ACCEPT 48,63% 0,12781

Normal (L-Moments) ACCEPT ACCEPT ACCEPT 48,16% 0,12828

LogNormal ACCEPT ACCEPT REJECT 8,55% 0,19328

Galton ACCEPT ACCEPT ACCEPT 97,86% 0,07106

Exponential ACCEPT ACCEPT REJECT 9,93% 0,18855

Exponential (L-Moments) ACCEPT ACCEPT ACCEPT 39,47% 0,13752

Gamma ACCEPT ACCEPT ACCEPT 57,11% 0,11956

Pearson III ACCEPT ACCEPT ACCEPT 98,59% 0,0682

Log Pearson III ACCEPT ACCEPT REJECT 7,34% 0,19793

EV1-Max (Gumbel) ACCEPT ACCEPT ACCEPT 97,25% 0,07301

EV3-Min (Weibull) ACCEPT ACCEPT ACCEPT 65,84% 0,11143

De la tabla 2.6 se observa que la distribución Pearson III tiene un mayor ajuste a los datos de precipitación máxima en relación con las
otras distribuciones utilizadas.

Contacto : contacto@emergeingenieria.cl
**12**
Teléfono : 752313453

Exceedance probability (%) - scale: Normal distribution

70

65

60

55

50

45

40

35

30

25

20

15

10

5

0

-3 -2 -1 0 1 2 3

_Figura 2.3 Análisis de Frecuencia Estación El Trapiche_

_Tabla 2.7 Test Kolmogorov Smirnov Estación Domeiko_

**Test Kolmogorov-Smirnov** **a=1%** **a=5%** **a=10%** **Porcentaje** **DMax**

Normal ACCEPT ACCEPT ACCEPT 19,98% 0,20102

Normal (L-Moments) ACCEPT ACCEPT ACCEPT 20,18% 0,20057

LogNormal ACCEPT ACCEPT ACCEPT 33,69% 0,17541

Galton ACCEPT ACCEPT ACCEPT 57,84% 0,14339

Exponential ACCEPT ACCEPT ACCEPT 54,69% 0,14714

Gamma ACCEPT ACCEPT ACCEPT 94,24% 0,09432

Pearson III ACCEPT ACCEPT ACCEPT 69,03% 0,13032

Log Pearson III ACCEPT ACCEPT ACCEPT 60,13% 0,14069

EV1-Max (Gumbel) ACCEPT ACCEPT ACCEPT 35,01% 0,17337

EV3-Min (Weibull) ACCEPT ACCEPT ACCEPT 93,28% 0,09644

Dado el Test de bondad y ajuste Kolmogorov-Smirnov (Tabla 2.7) para la estación Domeiko se observa que la distribución Gamma tiene

un mayor ajuste a los datos de precipitación máxima en relación con las otras distribuciones utilizadas.

Contacto : contacto@emergeingenieria.cl
**13**
Teléfono : 752313453

Return period (T) f or Maximum v alues in y ears - scale: Normal distribution

110

100

90

80

70

60

50

40

30

20

10

0

-3 -2 -1 0 1 2 3

_Figura 2.4 Análisis de Frecuencia Estación Domeiko_

El resumen de las precipitaciones máximas en 24 horas para diferentes periodos de retorno se presenta en la siguiente tabla.

_Tabla 2.8 Resumen de Precipitaciones Máximas en 24 horas_

**El Trapiche** 15,46 29,35 37,99 48,34 55,64 62,64 69,64

**Domeiko** 10,50 29,34 44,65 65,56 80,69 98,00 114,45

Dado los resultados presentados en la Tabla 2.8, se opta por usar las precipitaciones entregadas por la estación Domeiko siguiendo un
resultado conservador.

Contacto : contacto@emergeingenieria.cl
**14**
Teléfono : 752313453

**2.4.** **Caudales Microcuencas**

A partir de los valores anteriormente obtenidos, se calculan los caudales máximos asociados a diversos periodos de retorno. Los

resultados se presentan en las siguientes tablas.

_Tabla 2.9 Resumen Método Racional, Caudales Mc-1, Mc-2 y Mc-3_

**T = 2 años** 3,490 1,053 0,436

**T = 10 años** 5,263 1,588 0,658

**T = 50 años** 8,443 2,547 1,055

Contacto : contacto@emergeingenieria.cl
**15**
Teléfono : 752313453

**2.5.** **SIMULACIÓN HIDRÁULICO QUEBRADAS**

A partir de la información proporcionada por el levantamiento topográfico el cual abarca el área necesaria para poder definir los tramos

de las quebradas asociados al Proyecto, se puede determinar el comportamiento de las quebradas de acuerdo al caudal al que será

sometido.

Se generaron secciones transversales espaciadas cada 40 metros en los casos de más separación.

**2.5.1.** **MARCO TEÓRICO SIMULACIÓN HIDRÁULICA**

En función de las condiciones existentes es que se utilizó el software Hec-Ras para realizar las simulaciones.

HEC-RAS 5.0.3 ( _Hydraulic Engineering Center - River Analysis System_ ) es un software de libre acceso desarrollado por el cuerpo de

ingenieros de los Estados Unidos ( _US Corp. of Engineers_ ). Este Software al incluir el cálculo de pérdidas de carga singulares derivadas

de las contracciones y expansiones del cauce, permite considerar las modificaciones locales generadas al escurrimiento a lo largo de

todo el tramo en estudio.

El cálculo del flujo permanente se realiza a partir de la siguiente ecuación:

2

2

Y 2 + Z 2 + [a] [2] [ ∙V] [2]

[ ∙V] [2]

= Y 1 + Z 1 + [a] [1] [ ∙V] [1]
2g 2g

2g + h e

Dónde:

Y1, Y2: Profundidad del agua en la sección.

Z1, Z2: Elevación de la sección principal del cauce.

V1, V2: Velocidad media.

a1, a2: Coeficiente de carga de la velocidad.

g: Aceleración de gravedad.

H e : Pérdida principal de energía

La pérdida de energía (H e ) entre dos secciones transversales se atribuye a las pérdidas por fricción y a las pérdidas debido a contracciones

y/o expansiones. La ecuación utilizada para el cálculo de pérdidas es:

2

[ ∙V] [1] 2

2g ]

2

2

h e = L∙S [̅ ] f
+ C∙[ [a] [2] 2g [ ∙V] [2]

[ ∙V] [2] + [a] [1] [ ∙V] [1]

2g 2g

Dónde:

L: Longitud de alcance de descarga;

S [̅] f : Pendiente representativa de la fricción entre dos secciones;

C: Coeficiente de contracción o expansión.

Contacto : contacto@emergeingenieria.cl
**16**
Teléfono : 752313453

La pérdida de fricción se calculó para cada sección de la siguiente forma:

S f =
~~(~~ K [Q]

2

K [Q] ~~[)]~~

Dónde:

Q: Transporte para la sección.

K: Transporte para la subdivisión.

La determinación del transporte total y del coeficiente de velocidad para una sección transversal requiere que el flujo esté subdividido en

las unidades para las cuales la velocidad se distribuye uniformemente. El software HEC-RAS subdivide el flujo, separando las planicies

de inundación del cauce principal a partir de los puntos medidos. El flujo es calculado para cada sub-sección con la siguiente ecuación:

1/2

Q= K∙S
f

K= [1]

2/3

n [∙A∙R] [H]

El programa requiere como datos de entrada la topografía de los cauces, vale decir, las secciones transversales del cauce en el tramo

de interés, rugosidad del material del lecho y características del flujo (condición inicial y de borde). Como resultados HEC-RAS 5.0.3

entrega parámetros como la profundidad y velocidad media del flujo, sección de escurrimiento, perímetro mojado, profundidad crítica y

número de Froude, entre otros.

**2.5.2.** **Coeficiente de Manning**

Los valores de coeficientes de Manning para las Quebradas se obtuvieron a través de la formulación de Cowan según la siguiente

expresión.

n= m (n 0 + n 1 + n 2 + n 3 + n 4 )

Donde:

n 0 : Rugosidad base para un canal,

n 1 : Rugosidad adicional debido a irregularidades superficiales del perímetro mojado a lo largo del tramo en estudio.

n 2 : Rugosidad adicional equivalente debida a variación de forma y de dimensiones de la secciones a lo largo del tramo en estudio.

n 3 : Rugosidad adicional equivalente debido a obstrucciones existentes en el cauce.

n 4 : Rugosidad adicional equivalente debida a la presencia de vegetación.

m : Factor de corrección para incorporar efecto de sinuosidad del cauce.

Contacto : contacto@emergeingenieria.cl
**17**
Teléfono : 752313453

En la siguiente tabla se incluyen los valores de los parámetros que intervienen en la fórmula de Cowan.

_Tabla 2.10. Coeficientes de Manning según Método de Cowan_

Fuente: Tabla 3.707.104.B, Manual de Carreteras Volumen No3, MOP, 2014

Los valores se presentan en la Tabla 2.11.

_Tabla 2.11 Valores para la obtención de rugosidad según Cowan_

n 0 0,020

n 2 0,000

n 3 0,000

n 4 0,005

n 0,047

Se consideró el mismo valor de rugosidad para las tres micro cuencas.

Contacto : contacto@emergeingenieria.cl
**18**
Teléfono : 752313453

**2.5.3.** **Resultados**

La simulación se llevó a cabo en régimen supercrítico, por ende, se definió como condición de contorno
la pendiente normal aguas arriba de las tres quebradas de las cuencas mencionadas Mc-1, Mc-2 y Mc3. Por otro lado, para la simulación hidráulica se utilizaron los caudales entregados por el Método
Racional del Manual de Carreteras, pese a que estos valores sobre-estiman los caudales, se optó por
obtener resultados conservadores.

En lo sucesivo se mostrarán figuras con los resultados más relevantes de la simulación y un análisis
para cada situación.

_Figura 2_ _**.**_ _5. Distribución Perfiles en quebradas para las tres microcuencas estudiadas_

Contacto : contacto@emergeingenieria.cl
**19**
Teléfono : 752313453

En las Figuras 2.5, se observa la distribución de los perfiles transversales en las tres quebradas, lo cual se definió en su extensión por

sobre el emplazamiento del proyecto. Por otro lado, en las Figuras 2.6, 2.7 y 2.8, se presenta el perfil longitudinal de cada tramo de las

Quebradas Simuladas, cabe destacar que claramente se aprecia una pendiente pronunciada lo que se asociada con un flujo supercrítico.

_Figura 2.6. Perfil Longitudinal Quebrada Sin nombre_

Contacto : contacto@emergeingenieria.cl
**20**
Teléfono : 752313453

_Figura 2.7. Perfil Longitudinal Quebrada de Los Negros_

Contacto : contacto@emergeingenieria.cl
**21**
Teléfono : 752313453

_Figura 2_ _**.**_ _8. Perfil Longitudinal Quebrada de Los Negros_

Finalmente en las láminas anexas se muestran las áreas de inundación asociadas a una crecida de un periodo de retorno de 50 años,

100 años y 200 años, por otro lado los perfiles transversales se presentan en el Anexo-A.

En las láminas LAM 02_AREAS DE INUNDACION Q1_Mc-1 y LAM 03_AREAS DE INUNDACION Q2_Mc-2 y Q3_Mc-3 se observa el

área de inundación de las Quebradas denominadas Q1_Mc-1, Q2_Mc-3 y Q1_Mc-3, asociadas al Layout del Proyecto, se observa que

el emplazamiento del proyecto en ningún caso interfiere con el área de inundación para una crecida de 100 años de periodo de retorno,

en detalle se observa que el sector más crítico del emplazamiento de los postes se encuentra distanciado a 3 metros del área de

inundación, para el caso del Poste 3.

Contacto : contacto@emergeingenieria.cl
**22**
Teléfono : 752313453

**3. CONCLUSIONES Y/O COMENTARIOS**

Para el cálculo de caudales se ha escogido las precipitaciones máximas en 24 horas de la estación meteorológica Domeiko por sobre

estación meteorológica El trapiche, dado que sus datos de precipitación son mayores por ende se ha optado por ser más conservador.

**El Trapiche** 15,46 29,35 37,99 48,34 55,64 62,64 69,64

**Domeiko** 10,50 29,34 44,65 65,56 80,69 98,00 114,45

El Área de Influencia para la componente Hidrológica corresponde a la zona donde se emplazará la Planta Fotovoltaica North West

incluyendo todas las zonas de intervención directa del proyecto. Considerando esta área se observó la influencia de tres microcuencas

que podrían afectar al proyecto denominadas Mc-1, Mc-2 y Mc-3. Dadas estas microcuencas se ha estudiado una sección de cada una

en las zonas de intervención del proyecto para estimar las áreas de inundación como se puede observar en las láminas adjuntas.

Los resultados de la simulación Hidráulico de las quebradas, muestran que el emplazamiento del proyecto no interfiere con el área de

inundación para una crecida de 100 años de periodo de retorno bajo los caudales máximos obtenidos por el Método Racional (Manual de

Carreteras). En detalle se observa que el poste 3, correspondiente a la situación más desfavorable observada, este se encuentra a 3

metros de distancia del área de inundación, correspondiente al área de inundación de (T=100años). El siguiente poste más cercano al

área de inundación corresponde al poste 6, que se ubica a más de 8 m de la inundación centenaria.

De lo mostrado en el presente informe se concluye que las áreas de inundación obtenidas con la metodología expuesta, han sido

calculadas siendo conservador en todas las etapas de cálculo desde la elección del ara aportante de las microcuencas hasta la elección

del Método Racional (Manual de carreteras). Por lo tanto los postes del proyecto no interfieren en el área de inundación de las quebradas.

Contacto : contacto@emergeingenieria.cl
**23**
Teléfono : 752313453

**4.** **ANEXOS**

**4.1.** **PERFILES TRANSVERSALES Mc-1**

Contacto : contacto@emergeingenieria.cl
**24**
Teléfono : 752313453

Contacto : contacto@emergeingenieria.cl
**25**
Teléfono : 752313453

Contacto : contacto@emergeingenieria.cl
**26**
Teléfono : 752313453

Contacto : contacto@emergeingenieria.cl
**27**
Teléfono : 752313453

Contacto : contacto@emergeingenieria.cl
**28**
Teléfono : 752313453

Contacto : contacto@emergeingenieria.cl
**29**
Teléfono : 752313453

Contacto : contacto@emergeingenieria.cl
**30**
Teléfono : 752313453

Contacto : contacto@emergeingenieria.cl
**31**
Teléfono : 752313453

**4.2.** **PERFILES TRANSVERSALES Mc-2**

Contacto : contacto@emergeingenieria.cl
**32**
Teléfono : 752313453

Contacto : contacto@emergeingenieria.cl
**33**
Teléfono : 752313453

Contacto : contacto@emergeingenieria.cl
**34**
Teléfono : 752313453

Contacto : contacto@emergeingenieria.cl
**35**
Teléfono : 752313453

**4.3.** **PERFILES TRANSVERSALES Mc-3**

Contacto : contacto@emergeingenieria.cl
**36**
Teléfono : 752313453

Contacto : contacto@emergeingenieria.cl
**37**
Teléfono : 752313453

Contacto : contacto@emergeingenieria.cl
**38**
Teléfono : 752313453

**4.4.** **RESUMEN SIMULACIÓN HIDRÁULICA QUEBRADA Mc-1**

Tabla 4.1. Simulación Hidráulica Mc-1

**1422.85** Q(T=100años) 9.75 1134.94 1135.09 1.12 8.71 1.02 0.15
**1422.85** Q(T=200años) 10.7 1134.94 1135.10 1.14 9.37 1.00 0.16
**1400** Q(T=50años) 8.44 1134.90 1135.06 1.03 8.22 1.00 0.16
**1400** Q(T=100años) 9.75 1134.90 1135.07 1.09 8.96 1.02 0.17
**1400** Q(T=200años) 10.7 1134.90 1135.08 1.11 9.69 1.00 0.18
**1350** Q(T=50años) 8.44 1133.86 1134.04 1.09 7.76 1.01 0.18
**1350** Q(T=100años) 9.75 1133.86 1134.06 1.14 8.57 1.01 0.20
**1350** Q(T=200años) 10.7 1133.86 1134.06 1.17 9.12 1.02 0.20
**1300** Q(T=50años) 8.44 1131.65 1131.84 1.18 7.19 1.03 0.19
**1300** Q(T=100años) 9.75 1131.65 1131.85 1.23 7.96 1.03 0.20
**1300** Q(T=200años) 10.7 1131.65 1131.86 1.27 8.46 1.04 0.21
**1250** Q(T=50años) 8.44 1129.86 1130.01 0.96 8.76 1.01 0.15
**1250** Q(T=100años) 9.75 1129.86 1130.02 1.00 9.76 1.00 0.16
**1250** Q(T=200años) 10.7 1129.86 1130.03 1.04 10.27 1.01 0.17
**1200** Q(T=50años) 8.44 1129.16 1129.32 1.01 8.33 1.02 0.16
**1200** Q(T=100años) 9.75 1129.16 1129.33 1.04 9.34 1.00 0.17
**1200** Q(T=200años) 10.7 1129.16 1129.34 1.07 10.00 1.00 0.18
**1150** Q(T=50años) 8.44 1127.59 1127.83 1.10 7.69 1.01 0.24
**1150** Q(T=100años) 9.75 1127.59 1127.85 1.14 8.58 1.02 0.26
**1150** Q(T=200años) 10.7 1127.59 1127.86 1.16 9.19 1.02 0.27
**1100** Q(T=50años) 8.44 1125.86 1126.11 1.20 7.01 1.01 0.25
**1100** Q(T=100años) 9.75 1125.86 1126.13 1.25 7.80 1.01 0.27
**1100** Q(T=200años) 10.7 1125.86 1126.10 1.59 6.73 1.36 0.24
**1050** Q(T=50años) 8.44 1124.98 1125.10 1.03 8.23 1.01 0.12
**1050** Q(T=100años) 9.75 1124.98 1125.11 1.07 9.10 1.01 0.13
**1050** Q(T=200años) 10.7 1124.98 1125.12 1.10 9.77 1.00 0.14
**1000** Q(T=50años) 8.44 1124.94 1125.04 0.85 9.91 1.00 0.10
**1000** Q(T=100años) 9.75 1124.94 1125.05 0.89 10.95 1.00 0.11
**1000** Q(T=200años) 10.7 1124.94 1125.05 0.92 11.57 1.01 0.11
**950** Q(T=50años) 8.44 1124.90 1125.03 0.87 9.68 1.00 0.13
**950** Q(T=100años) 9.75 1124.90 1125.04 0.92 10.54 1.02 0.14
**950** Q(T=200años) 10.7 1124.90 1125.04 0.95 11.31 1.00 0.14
**900** Q(T=50años) 8.44 1124.84 1125.02 0.98 8.59 1.02 0.18
**900** Q(T=100años) 9.75 1124.84 1125.03 1.01 9.64 1.00 0.19
**900** Q(T=200años) 10.7 1124.84 1125.04 1.05 10.21 1.01 0.20
**850** Q(T=50años) 8.44 1123.78 1123.94 1.07 7.91 1.00 0.16
**850** Q(T=100años) 9.75 1123.78 1123.96 1.11 8.79 1.00 0.18
**850** Q(T=200años) 10.7 1123.78 1123.96 1.14 9.42 1.01 0.18
**800** Q(T=50años) 8.44 1121.96 1122.18 1.23 6.88 1.01 0.22
**800** Q(T=100años) 9.75 1121.96 1122.20 1.27 7.67 1.00 0.24
**800** Q(T=200años) 10.7 1121.96 1122.19 1.51 7.07 1.23 0.23
**750** Q(T=50años) 8.44 1120.27 1120.63 1.40 6.05 1.01 0.36
**750** Q(T=100años) 9.75 1120.27 1120.65 1.44 6.79 1.01 0.38
**750** Q(T=200años) 10.7 1120.27 1120.65 1.60 6.70 1.12 0.38
**700** Q(T=50años) 8.44 1119.89 1120.04 1.02 8.30 1.01 0.15

Contacto : contacto@emergeingenieria.cl
**39**
Teléfono : 752313453

**700** Q(T=100años) 9.75 1119.89 1120.06 1.06 9.22 1.00 0.17
**700** Q(T=200años) 10.7 1119.89 1120.06 1.10 9.77 1.01 0.17
**650** Q(T=50años) 8.44 1119.76 1119.95 1.01 8.34 1.01 0.19
**650** Q(T=100años) 9.75 1119.76 1119.96 1.03 9.45 1.00 0.20
**650** Q(T=200años) 10.7 1119.76 1119.97 1.06 10.10 1.01 0.21
**600** Q(T=50años) 8.44 1119.64 1119.87 1.11 7.63 1.02 0.23
**600** Q(T=100años) 9.75 1119.64 1119.89 1.14 8.56 1.02 0.25
**600** Q(T=200años) 10.7 1119.64 1119.90 1.16 9.25 1.01 0.26
**550** Q(T=50años) 8.44 1119.52 1119.79 1.15 7.33 1.01 0.27
**550** Q(T=100años) 9.75 1119.52 1119.80 1.19 8.19 1.01 0.28
**550** Q(T=200años) 10.7 1119.52 1119.81 1.21 8.84 1.01 0.29
**500** Q(T=50años) 8.44 1118.46 1118.70 1.15 7.33 1.02 0.24
**500** Q(T=100años) 9.75 1118.46 1118.71 1.20 8.15 1.01 0.25
**500** Q(T=200años) 10.7 1118.46 1118.72 1.23 8.72 1.01 0.26
**450** Q(T=50años) 8.44 1116.71 1116.97 1.30 6.47 1.01 0.26
**450** Q(T=100años) 9.75 1116.71 1116.97 1.57 6.22 1.23 0.26
**450** Q(T=200años) 10.7 1116.71 1117.01 1.38 7.73 1.01 0.30
**400** Q(T=50años) 8.44 1115.00 1115.31 1.58 5.35 1.24 0.31
**400** Q(T=100años) 9.75 1115.00 1115.36 1.38 7.05 1.01 0.36
**400** Q(T=200años) 10.7 1115.00 1115.38 1.41 7.59 1.01 0.38
**350** Q(T=50años) 8.44 1114.77 1114.95 1.03 8.17 1.01 0.18
**350** Q(T=100años) 9.75 1114.77 1114.96 1.07 9.12 1.01 0.19
**350** Q(T=200años) 10.7 1114.77 1114.97 1.10 9.76 1.02 0.20
**300** Q(T=50años) 8.44 1114.14 1114.31 1.09 7.77 1.01 0.17
**300** Q(T=100años) 9.75 1114.14 1114.33 1.13 8.62 1.01 0.19
**300** Q(T=200años) 10.7 1114.14 1114.34 1.15 9.29 1.00 0.20
**250** Q(T=50años) 8.44 1112.42 1112.64 1.20 7.04 1.00 0.22
**250** Q(T=100años) 9.75 1112.42 1112.66 1.26 7.76 1.01 0.24
**250** Q(T=200años) 10.7 1112.42 1112.67 1.28 8.35 1.01 0.25
**200** Q(T=50años) 8.44 1110.75 1111.04 1.37 6.16 1.02 0.29
**200** Q(T=100años) 9.75 1110.75 1111.06 1.41 6.90 1.01 0.31
**200** Q(T=200años) 10.7 1110.75 1111.05 1.64 6.52 1.19 0.30
**150** Q(T=50años) 8.44 1108.94 1109.29 1.32 6.38 1.01 0.35
**150** Q(T=100años) 9.75 1108.94 1109.31 1.36 7.14 1.01 0.37
**150** Q(T=200años) 10.7 1108.94 1109.32 1.39 7.72 1.01 0.38
**100** Q(T=50años) 8.44 1107.00 1107.33 1.51 5.59 1.16 0.33
**100** Q(T=100años) 9.75 1107.00 1107.37 1.42 6.89 1.03 0.37
**100** Q(T=200años) 10.7 1107.00 1107.38 1.45 7.36 1.04 0.38
**50** Q(T=50años) 8.44 1105.00 1105.18 1.18 7.18 1.02 0.18
**50** Q(T=100años) 9.75 1105.00 1105.20 1.21 8.05 1.00 0.20
**50** Q(T=200años) 10.7 1105.00 1105.21 1.25 8.58 1.01 0.21
**0** Q(T=50años) 8.44 1104.77 1104.95 0.96 8.81 1.02 0.18
**0** Q(T=100años) 9.75 1104.77 1104.96 0.98 9.96 1.01 0.19
**0** Q(T=200años) 10.7 1104.77 1104.97 0.99 10.84 1.00 0.20

Contacto : contacto@emergeingenieria.cl
**40**
Teléfono : 752313453

**4.5.** **RESUMEN SIMULACIÓN HIDRÁULICA QUEBRADA Mc-2**

Tabla 4.2. Simulación Hidráulica Mc-2

|Perfil|Periodo de<br>Retorno<br>(T años)|Caudal<br>(m3/s)|Cota de<br>Fondo<br>(m.s.n.m.)|Nivel de<br>Agua<br>(m.s.n.m.)|Velocidad<br>(m/s)|Área del<br>Flujo<br>(m2)|Froude|Altura<br>Normal<br>(m)|
|---|---|---|---|---|---|---|---|---|
|**598.48**|Q(T=50años)|2.55|1171.69|1171.82|0.86|2.95|1.00|0.13|
|**598.48**|Q(T=100años)|2.94|1171.69|1171.83|0.91|3.25|1.01|0.14|
|**598.48**|Q(T=200años)|3.23|1171.69|1171.83|0.93|3.48|1.02|0.14|
|**560**|Q(T=50años)|2.55|1170.77|1170.88|0.82|3.10|1.00|0.11|
|**560**|Q(T=100años)|2.94|1170.77|1170.89|0.84|3.50|0.99|0.12|
|**560**|Q(T=200años)|3.23|1170.77|1170.89|0.87|3.72|1.02|0.12|
|**520**|Q(T=50años)|2.55|1169.87|1169.96|0.77|3.32|1.00|0.09|
|**520**|Q(T=100años)|2.94|1169.87|1169.97|0.79|3.71|1.00|0.10|
|**520**|Q(T=200años)|3.23|1169.87|1169.97|0.78|4.15|0.94|0.10|
|**480**|Q(T=50años)|2.55|1169.04|1169.15|0.82|3.12|1.01|0.11|
|**480**|Q(T=100años)|2.94|1169.04|1169.16|0.86|3.42|1.03|0.12|
|**480**|Q(T=200años)|3.23|1169.04|1169.16|0.86|3.75|1.00|0.12|
|**440**|Q(T=50años)|2.55|1168.28|1168.41|0.90|2.84|1.01|0.13|
|**440**|Q(T=100años)|2.94|1168.28|1168.42|0.93|3.17|1.01|0.14|
|**440**|Q(T=200años)|3.23|1168.28|1168.42|0.96|3.37|1.02|0.14|
|**400**|Q(T=50años)|2.55|1167.15|1167.33|1.07|2.38|1.00|0.18|
|**400**|Q(T=100años)|2.94|1167.15|1167.34|1.11|2.65|1.01|0.19|
|**400**|Q(T=200años)|3.23|1167.15|1167.35|1.13|2.85|1.00|0.20|
|**360**|Q(T=50años)|2.55|1165.96|1166.11|1.06|2.41|1.00|0.15|
|**360**|Q(T=100años)|2.94|1165.96|1166.12|1.10|2.68|1.00|0.16|
|**360**|Q(T=200años)|3.23|1165.96|1166.13|1.13|2.86|1.01|0.17|
|**320**|Q(T=50años)|2.55|1164.95|1165.10|1.06|2.40|1.00|0.15|
|**320**|Q(T=100años)|2.94|1164.95|1165.12|1.10|2.67|1.00|0.17|
|**320**|Q(T=200años)|3.23|1164.95|1165.12|1.13|2.87|1.00|0.17|
|**280**|Q(T=50años)|2.55|1163.95|1164.11|1.10|2.33|1.00|0.16|
|**280**|Q(T=100años)|2.94|1163.95|1164.13|1.13|2.60|1.00|0.18|
|**280**|Q(T=200años)|3.23|1163.95|1164.14|1.16|2.78|1.01|0.19|
|**240**|Q(T=50años)|2.55|1163.01|1163.22|1.10|2.32|1.01|0.21|
|**240**|Q(T=100años)|2.94|1163.01|1163.23|1.13|2.60|1.01|0.22|
|**240**|Q(T=200años)|3.23|1163.01|1163.24|1.15|2.82|1.01|0.23|
|**200**|Q(T=50años)|2.55|1162.35|1162.51|0.95|2.69|1.00|0.16|
|**200**|Q(T=100años)|2.94|1162.35|1162.52|0.98|2.99|1.00|0.17|
|**200**|Q(T=200años)|3.23|1162.35|1162.52|1.01|3.20|1.01|0.17|
|**160**|Q(T=50años)|2.55|1161.36|1161.52|0.97|2.64|1.00|0.16|
|**160**|Q(T=100años)|2.94|1161.36|1161.53|1.00|2.95|1.00|0.17|
|**160**|Q(T=200años)|3.23|1161.36|1161.53|1.03|3.13|1.01|0.17|
|**120**|Q(T=50años)|2.55|1160.33|1160.49|0.99|2.57|1.03|0.16|
|**120**|Q(T=100años)|2.94|1160.33|1160.51|1.01|2.92|1.01|0.18|
|**120**|Q(T=200años)|3.23|1160.33|1160.51|1.03|3.13|1.01|0.18|
|**80**|Q(T=50años)|2.55|1159.42|1159.56|0.93|2.74|1.00|0.14|
|**80**|Q(T=100años)|2.94|1159.42|1159.57|0.98|3.01|1.02|0.15|
|**80**|Q(T=200años)|3.23|1159.42|1159.58|0.99|3.26|1.00|0.16|
|**40**|Q(T=50años)|2.55|1158.45|1158.56|0.88|2.90|1.00|0.11|
|**40**|Q(T=100años)|2.94|1158.45|1158.57|0.91|3.23|1.00|0.12|
|**40**|Q(T=200años)|3.23|1158.45|1158.58|0.94|3.45|1.00|0.13|
|**0 **|Q(T=50años)|2.55|1157.50|1157.59|0.74|3.42|1.00|0.09|

Contacto : contacto@emergeingenieria.cl
**41**
Teléfono : 752313453

|0|Q(T=100años)|2.94|1157.50|1157.60|0.78|3.79|1.00|0.10|
|---|---|---|---|---|---|---|---|---|
|**0 **|Q(T=200años)|3.23|1157.50|1157.60|0.79|4.10|0.99|0.10|

Contacto : contacto@emergeingenieria.cl
**42**
Teléfono : 752313453

**4.6.** **RESUMEN SIMULACIÓN HIDRÁULICA QUEBRADA Mc-3**

Tabla 4.3. Simulación Hidráulica Mc-3

|Perfil|Periodo de<br>Retorno<br>(T años)|Caudal<br>(m3/s)|Cota de<br>Fondo<br>(m.s.n.m.)|Nivel de<br>Agua<br>(m.s.n.m.)|Velocidad<br>(m/s)|Área del<br>Flujo<br>(m2)|Froude|Altura<br>Normal<br>(m)|
|---|---|---|---|---|---|---|---|---|
|**373.65**|Q(T=50años)|1.06|1177.00|1177.08|0.68|1.56|1.00|0.08|
|**373.65**|Q(T=100años)|1.22|1177.00|1177.08|0.70|1.75|1.00|0.08|
|**373.65**|Q(T=200años)|1.34|1177.00|1177.09|0.68|1.95|0.95|0.09|
|**320**|Q(T=50años)|1.06|1175.47|1175.54|0.63|1.67|1.00|0.07|
|**320**|Q(T=100años)|1.22|1175.47|1175.54|0.65|1.87|0.99|0.07|
|**320**|Q(T=200años)|1.34|1175.47|1175.55|0.67|2.00|1.00|0.08|
|**280**|Q(T=50años)|1.06|1174.38|1174.45|0.70|1.51|1.03|0.07|
|**280**|Q(T=100años)|1.22|1174.38|1174.46|0.71|1.72|1.00|0.08|
|**280**|Q(T=200años)|1.34|1174.38|1174.46|0.72|1.84|1.00|0.08|
|**250**|Q(T=50años)|1.06|1173.76|1173.84|0.66|1.59|1.01|0.08|
|**250**|Q(T=100años)|1.22|1173.76|1173.84|0.70|1.73|1.04|0.08|
|**250**|Q(T=200años)|1.34|1173.76|1173.85|0.69|1.93|1.00|0.09|
|**220**|Q(T=50años)|1.06|1173.30|1173.39|0.69|1.53|1.00|0.09|
|**220**|Q(T=100años)|1.22|1173.30|1173.39|0.70|1.73|0.99|0.09|
|**220**|Q(T=200años)|1.34|1173.30|1173.40|0.71|1.87|0.98|0.10|
|**170**|Q(T=50años)|1.06|1172.59|1172.69|0.79|1.34|1.00|0.10|
|**170**|Q(T=100años)|1.22|1172.59|1172.70|0.83|1.47|1.02|0.11|
|**170**|Q(T=200años)|1.34|1172.59|1172.71|0.83|1.61|1.00|0.12|
|**138.57**|Q(T=50años)|1.06|1171.98|1172.04|0.68|1.55|1.01|0.06|
|**138.57**|Q(T=100años)|1.22|1171.98|1172.05|0.70|1.73|1.00|0.07|
|**138.57**|Q(T=200años)|1.34|1171.98|1172.05|0.72|1.85|1.00|0.07|
|**100**|Q(T=50años)|1.06|1169.85|1169.95|0.84|1.25|1.02|0.10|
|**100**|Q(T=100años)|1.22|1169.85|1169.96|0.89|1.37|1.03|0.11|
|**100**|Q(T=200años)|1.34|1169.85|1169.97|0.91|1.46|1.04|0.12|
|**80**|Q(T=50años)|1.06|1168.82|1168.94|0.82|1.29|1.02|0.12|
|**80**|Q(T=100años)|1.22|1168.82|1168.94|0.84|1.45|1.00|0.12|
|**80**|Q(T=200años)|1.34|1168.82|1168.95|0.86|1.56|1.00|0.13|
|**40**|Q(T=50años)|1.06|1167.30|1167.42|0.82|1.29|0.99|0.12|
|**40**|Q(T=100años)|1.22|1167.30|1167.43|0.85|1.44|0.99|0.13|
|**40**|Q(T=200años)|1.34|1167.30|1167.44|0.88|1.51|1.02|0.14|
|**0 **|Q(T=50años)|1.06|1165.96|1166.07|0.79|1.33|1.00|0.11|
|**0 **|Q(T=100años)|1.22|1165.96|1166.07|0.82|1.48|1.01|0.11|
|**0 **|Q(T=200años)|1.34|1165.96|1166.08|0.83|1.60|1.00|0.12|

Contacto : contacto@emergeingenieria.cl
**43**
Teléfono : 752313453

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4.2.: Simulación Hidráulica Mc-2**

| Perfil | Periodo de<br>Retorno<br>(T años) | Caudal<br>(m3/s) | Cota de<br>Fondo<br>(m.s.n.m.) | Nivel de<br>Agua<br>(m.s.n.m.) | Velocidad<br>(m/s) | Área del<br>Flujo<br>(m2) | Froude | Altura<br>Normal<br>(m) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **598.48** | Q(T=50años) | 2.55 | 1171.69 | 1171.82 | 0.86 | 2.95 | 1.00 | 0.13 |
| **598.48** | Q(T=100años) | 2.94 | 1171.69 | 1171.83 | 0.91 | 3.25 | 1.01 | 0.14 |
| **598.48** | Q(T=200años) | 3.23 | 1171.69 | 1171.83 | 0.93 | 3.48 | 1.02 | 0.14 |
| **560** | Q(T=50años) | 2.55 | 1170.77 | 1170.88 | 0.82 | 3.10 | 1.00 | 0.11 |
| **560** | Q(T=100años) | 2.94 | 1170.77 | 1170.89 | 0.84 | 3.50 | 0.99 | 0.12 |
| **560** | Q(T=200años) | 3.23 | 1170.77 | 1170.89 | 0.87 | 3.72 | 1.02 | 0.12 |
| **520** | Q(T=50años) | 2.55 | 1169.87 | 1169.96 | 0.77 | 3.32 | 1.00 | 0.09 |
| **520** | Q(T=100años) | 2.94 | 1169.87 | 1169.97 | 0.79 | 3.71 | 1.00 | 0.10 |
| **520** | Q(T=200años) | 3.23 | 1169.87 | 1169.97 | 0.78 | 4.15 | 0.94 | 0.10 |
| **480** | Q(T=50años) | 2.55 | 1169.04 | 1169.15 | 0.82 | 3.12 | 1.01 | 0.11 |
| **480** | Q(T=100años) | 2.94 | 1169.04 | 1169.16 | 0.86 | 3.42 | 1.03 | 0.12 |
| **480** | Q(T=200años) | 3.23 | 1169.04 | 1169.16 | 0.86 | 3.75 | 1.00 | 0.12 |
| **440** | Q(T=50años) | 2.55 | 1168.28 | 1168.41 | 0.90 | 2.84 | 1.01 | 0.13 |
| **440** | Q(T=100años) | 2.94 | 1168.28 | 1168.42 | 0.93 | 3.17 | 1.01 | 0.14 |
| **440** | Q(T=200años) | 3.23 | 1168.28 | 1168.42 | 0.96 | 3.37 | 1.02 | 0.14 |
| **400** | Q(T=50años) | 2.55 | 1167.15 | 1167.33 | 1.07 | 2.38 | 1.00 | 0.18 |
| **400** | Q(T=100años) | 2.94 | 1167.15 | 1167.34 | 1.11 | 2.65 | 1.01 | 0.19 |
| **400** | Q(T=200años) | 3.23 | 1167.15 | 1167.35 | 1.13 | 2.85 | 1.00 | 0.20 |
| **360** | Q(T=50años) | 2.55 | 1165.96 | 1166.11 | 1.06 | 2.41 | 1.00 | 0.15 |
| **360** | Q(T=100años) | 2.94 | 1165.96 | 1166.12 | 1.10 | 2.68 | 1.00 | 0.16 |
| **360** | Q(T=200años) | 3.23 | 1165.96 | 1166.13 | 1.13 | 2.86 | 1.01 | 0.17 |
| **320** | Q(T=50años) | 2.55 | 1164.95 | 1165.10 | 1.06 | 2.40 | 1.00 | 0.15 |
| **320** | Q(T=100años) | 2.94 | 1164.95 | 1165.12 | 1.10 | 2.67 | 1.00 | 0.17 |
| **320** | Q(T=200años) | 3.23 | 1164.95 | 1165.12 | 1.13 | 2.87 | 1.00 | 0.17 |
| **280** | Q(T=50años) | 2.55 | 1163.95 | 1164.11 | 1.10 | 2.33 | 1.00 | 0.16 |
| **280** | Q(T=100años) | 2.94 | 1163.95 | 1164.13 | 1.13 | 2.60 | 1.00 | 0.18 |
| **280** | Q(T=200años) | 3.23 | 1163.95 | 1164.14 | 1.16 | 2.78 | 1.01 | 0.19 |
| **240** | Q(T=50años) | 2.55 | 1163.01 | 1163.22 | 1.10 | 2.32 | 1.01 | 0.21 |
| **240** | Q(T=100años) | 2.94 | 1163.01 | 1163.23 | 1.13 | 2.60 | 1.01 | 0.22 |
| **240** | Q(T=200años) | 3.23 | 1163.01 | 1163.24 | 1.15 | 2.82 | 1.01 | 0.23 |
| **200** | Q(T=50años) | 2.55 | 1162.35 | 1162.51 | 0.95 | 2.69 | 1.00 | 0.16 |
| **200** | Q(T=100años) | 2.94 | 1162.35 | 1162.52 | 0.98 | 2.99 | 1.00 | 0.17 |
| **200** | Q(T=200años) | 3.23 | 1162.35 | 1162.52 | 1.01 | 3.20 | 1.01 | 0.17 |
| **160** | Q(T=50años) | 2.55 | 1161.36 | 1161.52 | 0.97 | 2.64 | 1.00 | 0.16 |
| **160** | Q(T=100años) | 2.94 | 1161.36 | 1161.53 | 1.00 | 2.95 | 1.00 | 0.17 |
| **160** | Q(T=200años) | 3.23 | 1161.36 | 1161.53 | 1.03 | 3.13 | 1.01 | 0.17 |
| **120** | Q(T=50años) | 2.55 | 1160.33 | 1160.49 | 0.99 | 2.57 | 1.03 | 0.16 |
| **120** | Q(T=100años) | 2.94 | 1160.33 | 1160.51 | 1.01 | 2.92 | 1.01 | 0.18 |
| **120** | Q(T=200años) | 3.23 | 1160.33 | 1160.51 | 1.03 | 3.13 | 1.01 | 0.18 |
| **80** | Q(T=50años) | 2.55 | 1159.42 | 1159.56 | 0.93 | 2.74 | 1.00 | 0.14 |
| **80** | Q(T=100años) | 2.94 | 1159.42 | 1159.57 | 0.98 | 3.01 | 1.02 | 0.15 |
| **80** | Q(T=200años) | 3.23 | 1159.42 | 1159.58 | 0.99 | 3.26 | 1.00 | 0.16 |
| **40** | Q(T=50años) | 2.55 | 1158.45 | 1158.56 | 0.88 | 2.90 | 1.00 | 0.11 |
| **40** | Q(T=100años) | 2.94 | 1158.45 | 1158.57 | 0.91 | 3.23 | 1.00 | 0.12 |
| **40** | Q(T=200años) | 3.23 | 1158.45 | 1158.58 | 0.94 | 3.45 | 1.00 | 0.13 |
| **0 ** | Q(T=50años) | 2.55 | 1157.50 | 1157.59 | 0.74 | 3.42 | 1.00 | 0.09 |

**Tabla 4.3.: Simulación Hidráulica Mc-3**

| Perfil | Periodo de<br>Retorno<br>(T años) | Caudal<br>(m3/s) | Cota de<br>Fondo<br>(m.s.n.m.) | Nivel de<br>Agua<br>(m.s.n.m.) | Velocidad<br>(m/s) | Área del<br>Flujo<br>(m2) | Froude | Altura<br>Normal<br>(m) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **373.65** | Q(T=50años) | 1.06 | 1177.00 | 1177.08 | 0.68 | 1.56 | 1.00 | 0.08 |
| **373.65** | Q(T=100años) | 1.22 | 1177.00 | 1177.08 | 0.70 | 1.75 | 1.00 | 0.08 |
| **373.65** | Q(T=200años) | 1.34 | 1177.00 | 1177.09 | 0.68 | 1.95 | 0.95 | 0.09 |
| **320** | Q(T=50años) | 1.06 | 1175.47 | 1175.54 | 0.63 | 1.67 | 1.00 | 0.07 |
| **320** | Q(T=100años) | 1.22 | 1175.47 | 1175.54 | 0.65 | 1.87 | 0.99 | 0.07 |
| **320** | Q(T=200años) | 1.34 | 1175.47 | 1175.55 | 0.67 | 2.00 | 1.00 | 0.08 |
| **280** | Q(T=50años) | 1.06 | 1174.38 | 1174.45 | 0.70 | 1.51 | 1.03 | 0.07 |
| **280** | Q(T=100años) | 1.22 | 1174.38 | 1174.46 | 0.71 | 1.72 | 1.00 | 0.08 |
| **280** | Q(T=200años) | 1.34 | 1174.38 | 1174.46 | 0.72 | 1.84 | 1.00 | 0.08 |
| **250** | Q(T=50años) | 1.06 | 1173.76 | 1173.84 | 0.66 | 1.59 | 1.01 | 0.08 |
| **250** | Q(T=100años) | 1.22 | 1173.76 | 1173.84 | 0.70 | 1.73 | 1.04 | 0.08 |
| **250** | Q(T=200años) | 1.34 | 1173.76 | 1173.85 | 0.69 | 1.93 | 1.00 | 0.09 |
| **220** | Q(T=50años) | 1.06 | 1173.30 | 1173.39 | 0.69 | 1.53 | 1.00 | 0.09 |
| **220** | Q(T=100años) | 1.22 | 1173.30 | 1173.39 | 0.70 | 1.73 | 0.99 | 0.09 |
| **220** | Q(T=200años) | 1.34 | 1173.30 | 1173.40 | 0.71 | 1.87 | 0.98 | 0.10 |
| **170** | Q(T=50años) | 1.06 | 1172.59 | 1172.69 | 0.79 | 1.34 | 1.00 | 0.10 |
| **170** | Q(T=100años) | 1.22 | 1172.59 | 1172.70 | 0.83 | 1.47 | 1.02 | 0.11 |
| **170** | Q(T=200años) | 1.34 | 1172.59 | 1172.71 | 0.83 | 1.61 | 1.00 | 0.12 |
| **138.57** | Q(T=50años) | 1.06 | 1171.98 | 1172.04 | 0.68 | 1.55 | 1.01 | 0.06 |
| **138.57** | Q(T=100años) | 1.22 | 1171.98 | 1172.05 | 0.70 | 1.73 | 1.00 | 0.07 |
| **138.57** | Q(T=200años) | 1.34 | 1171.98 | 1172.05 | 0.72 | 1.85 | 1.00 | 0.07 |
| **100** | Q(T=50años) | 1.06 | 1169.85 | 1169.95 | 0.84 | 1.25 | 1.02 | 0.10 |
| **100** | Q(T=100años) | 1.22 | 1169.85 | 1169.96 | 0.89 | 1.37 | 1.03 | 0.11 |
| **100** | Q(T=200años) | 1.34 | 1169.85 | 1169.97 | 0.91 | 1.46 | 1.04 | 0.12 |
| **80** | Q(T=50años) | 1.06 | 1168.82 | 1168.94 | 0.82 | 1.29 | 1.02 | 0.12 |
| **80** | Q(T=100años) | 1.22 | 1168.82 | 1168.94 | 0.84 | 1.45 | 1.00 | 0.12 |
| **80** | Q(T=200años) | 1.34 | 1168.82 | 1168.95 | 0.86 | 1.56 | 1.00 | 0.13 |
| **40** | Q(T=50años) | 1.06 | 1167.30 | 1167.42 | 0.82 | 1.29 | 0.99 | 0.12 |
| **40** | Q(T=100años) | 1.22 | 1167.30 | 1167.43 | 0.85 | 1.44 | 0.99 | 0.13 |
| **40** | Q(T=200años) | 1.34 | 1167.30 | 1167.44 | 0.88 | 1.51 | 1.02 | 0.14 |
| **0 ** | Q(T=50años) | 1.06 | 1165.96 | 1166.07 | 0.79 | 1.33 | 1.00 | 0.11 |
| **0 ** | Q(T=100años) | 1.22 | 1165.96 | 1166.07 | 0.82 | 1.48 | 1.01 | 0.11 |
| **0 ** | Q(T=200años) | 1.34 | 1165.96 | 1166.08 | 0.83 | 1.60 | 1.00 | 0.12 |
