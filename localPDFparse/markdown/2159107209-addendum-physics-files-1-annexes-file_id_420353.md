---
title: Santiago, 14 de Marzo de 2003
author: Santander, Eugenio (Pascua)
date: D:20231123152454-03'00'
language: es
type: report
pages: 40
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Contenido
  - ANEXO: IDENTIFICACION DE LOS PEAKS DE VIBRACIÓN
-->

**GS3 CONSULTORES**

**LEVANTAMIENTO LÍNEA BASE OPTIMIZACIÓN RAJO SUR**

**“EVALUACIÓN DEL IMPACTO DE LAS VIBRACIONES POR VOLADURA SOBRE**

**LOS GLACIARES DE ROCA”**

**INFORME ACTUALIZADO**

**Hoja de Control**

|RESPONSABLES:|Col2|Col3|Col4|
|---|---|---|---|
|**Versión**|**fecha**|**CLIENTE**|**EPC**|
|**A **|**02/10/2023**||**Frederic Vanbrabant**|
|**B **|**10/10/2023**||**Frederic Vanbrabant**|
|**C **|**23/10/2023**||**Frederic Vanbrabant**|
|**D **|**16/11/2023**||**Frederic Vanbrabant**|
|**E **|**23/11/2023**||**Frederic Vanbrabant**|

|APROBACIONES:|Col2|Col3|Col4|
|---|---|---|---|
|**Versión**|**Preparado por:**|**Revisado por:**|**Aprobado por:**|
|**E **|**Frederic Vanbrabant**|**Juan Daniel Silva**|**Frederic Vanbrabant**|
|**Firmas**||||
|**Fecha**|**23/11/2023**|**23/11/2023**|**23/11/2023**|

**Este documento fue confeccionado para GS3 Consultores por EPC ANDES CHILE**

**SPA. Tiene carácter de reservado y confidencial.**

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

**RESUMEN EJECUTIVO**

El objetivo de este estudio es evaluar la amplitud de las vibraciones (PPV) generadas por las
voladuras del Rajo Sur de la División El Teniente, y en particular en el borde del glaciar de
roca más cercano (CL106007013), y compararla con el valor máximo admisible calculado para
este glaciar específico (PPV crítico).

Para eso, se dispuso del monitoreo de vibraciones de una voladura específicamente realizado
para este propósito con dos geófonos triaxiales alineados entre la voladura y el glaciar de roca
(monitoreo especial). También se entregaron 10 registros de monitoreos de voladuras,
realizadas los últimos años, con los diagramas de perforación, carguío y secuencia
correspondientes.

Con esta información, se pudieron extraer 98 peaks de vibraciones para distancias entre 73 y
368 m, y calibrar un modelo de atenuación geométrica simple.

El monitoreo especial validó este modelo para distancias de hasta 616 m.

El PPV crítico fue calculado con dos métodos (observaciones regionales durante sismos de
gran amplitud, y método de equilibrio límite simulado numéricamente). El valor obtenido
con ambos métodos es del orden de 70 mm/s.

Para el glaciar de roca ubicado a 516 m del límite actual del rajo, existe 90% de probabilidad
para que las amplitudes de las vibraciones (PPV) sean inferiores a 3,0 mm/s, o sea muy por
debajo del PPV crítico calculado.

Por lo tanto, se puede descartar cualquier impacto significativo de las vibraciones inducidas
por las voladuras del Rajo Sur sobre los glaciares de roca en el entorno.

Esta conclusión aplica incluso si se modifican los diagramas de perforación, pasando de
banco de 10 m a 15 m, y aumentando el diámetro de perforación de 9” a 10”5/8.

Con los diseños actuales, las voladuras pueden acercarse por lo menos hasta 84 m del glaciar
de roca, sin que sea necesario modificar los diagramas de perforación y carguío de explosivo.

www.epc-groupe.com

2

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

# Contenido

**TABLA DE CONTENIDO**

1 INTRODUCCION ..................................................................................................................... 4

2 CONTEXTO ............................................................................................................................... 6

3 BASE DE DATOS Y MODELO PREDICTIVO ...................................................................... 7

4 MONITOREO ESPECIAL E IMPACTO SOBRE EL GLACIAR DE ROCA ..................... 15

5 IMPACTO SOBRE EL GLACIAR DE ROCA ...................................................................... 18

5.1 Metodología del PPV crítico fijo ................................................................................... 18

5.2 Metodología del equilibrio límite ................................................................................. 19

5.2.1 Aceleración crítica (K y ) ............................................................................................... 21

5.2.2 Velocidad crítica (PPV crítico) .................................................................................. 26

5.3 Distancia crítica ............................................................................................................... 27

5.4 Estudio paramétrico para otro tipo de diseño de P&T ............................................. 28

6 CONCLUSIONES .................................................................................................................... 31

ANEXO: IDENTIFICACION DE LOS PEAKS DE VIBRACIÓN ............................................. 33

www.epc-groupe.com

3

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

**1** **INTRODUCCION**

El objetivo de este estudio es evaluar la amplitud de las vibraciones generadas por las
voladuras del Rajo Sur de la División El Teniente, y en particular en el borde del glaciar de
roca más cercano.

Para eso, se dispuso del monitoreo de vibraciones de una voladura, específicamente realizado
para este propósito, con dos geófonos triaxiales alineados entre la voladura y el glaciar de
roca (nombrado a continuación “monitoreo especial”).

También se entregaron 10 registros de monitoreos de voladura, realizados los últimos años,
con los diagramas de perforación, carguío y secuencia correspondientes.

Con esta información, se propone realizar las siguientes actividades:

 Identificar las características principales de las voladuras realizadas en el Rajo Sur
(tamaño, diámetro de perforación, cantidad de explosivo por pozo, retardos entre
cargas, etc)

 Identificar las voladuras con mayor impacto vibracional

 Elaborar un modelo de predicción de vibraciones superficiales (PPV) en función de la
distancia para esas voladuras

 Estimar el nivel de vibración que se puede llegar al borde del glaciar de roca más

cercano

 Calcular la velocidad de partículas (PPV) crítica que puede soportar el glaciar, es decir
sin afectar su estabilidad.

 Generar ábacos de vibraciones que permitan manejar de manera rápida y sencilla
posibles configuraciones de voladuras para que no impacten la estabilidad de los
glaciares

Para realizar este estudio, se dispuso de la siguiente información:

Planos

 Topografía mina al 1 de agosto de 2022 (en coordenadas UTM y mina) en formato
.dxf, sin n°referencia (“Topo Rajo Sur 01 Ago.dxf “ y “Topo Rajo_UTM.dxf”)

 Inventario de los glaciares en Chile en formato kmz (“IPG2022.kmz”) e identificación
del glaciar de roca más cercanos del Rajo Sur (“Glaciar_Rajo.kmz”)

Monitoreo especial

 Coordenadas de los 2 geófonos del monitoreo especial (en coordenadas UTM y mina)
en formato .dxf, sin n°referencia (“Vibraciones_P1P2_CoordMina.dxf “ y
“Vibraciones_P1P2_UTM.dxf”)

 Coordenadas de los pozos de la voladura del monitoreo especial (en coordenadas
UTM y mina) en formato .dxf, sin n°referencia (“Malla Pol15N - 2910.dxf “ y “Malla
Voladura_UTM.dxf”)

 Presentación PowerPoint con la instalación de los geófonos “Montaje terreno
vibraciones P1-P2.pptx”

www.epc-groupe.com

4

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

 2 archivos ASCII con los datos del monitoreo “CampolejanoP1.txt” y
“CampolejanoP2.txt”

 1 protocolo de pre voladura en formato pdf “Protocolo Voladura F3 2910_15 N.pdf”

 1 reporte post voladura en formato pdf « Post Voladura Sive Teniente 2910_015
N.pdf »

Base de datos de vibraciones

10 carpetas completas, con la siguiente información:

 Reporte automático del sistema de monitoreo Micromate en pdf

 Registro del monitoreo en formato ASCII

 Protocolo de pre voladura en formato pdf

 Reporte post voladura en formato pdf

 Coordenadas de los pozos volados en formato ASCII

 Coordenadas del geófono en formato ASCII

www.epc-groupe.com

5

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

**2** **CONTEXTO**

El Proyecto Rajo Sur de la División El Teniente explota reservas de minerales ubicados en el
borde del cráter de la mina subterránea, entre 2.730 y 3.240 metros sobre el nivel del mar.

En las cumbres más altas del sector se encuentran glaciares de roca. El más cercano se ubica
a unos 516 m del borde de la explotación (Ilustración 1). Ya que las vibraciones se atenúan
con la distancia, éste será tomado como referencia en este estudio (glaciar CL106007013).

Ilustración 1: Proyecto Rajo Sur (arriba) y distancia a los glaciares de roca más cercano (abajo).

www.epc-groupe.com

6

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

**3** **BASE DE DATOS Y MODELO PREDICTIVO**

Las 11 voladuras para las cuales se dispone de registros de vibraciones son detalladas en la
Tabla 1. La voladura n°11 corresponde al monitoreo especial.

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |8|3000_07|03-07-2019|Contorno + precorte|38|8481|224|5X250|10|9|348| |9|2960_04|16-03-2020|Contorno + precorte|41|9490|231|5X200|10|9|345| |10|2960_05|25-03-2020|Contorno + precorte|55|13234|241|5X200|10|9|345| |11|2910_15|27-05-2022|Contorno+Rampa|60|8856|147|5X200|variable|9|298| -->

**Tabla 1: parámetros característicos de las voladuras de la base de datos.**

| Col1 | Voladura | Nombre | Coordenadas UTM WGS 84 Datum 19 Huso S | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Voladura | Nombre | Latitud | Longitud | Cota | Este | Norte | Zona |
| 1<br>2 | 1<br>2 | 3020_06 A<br>2760_05 | 34°05'51"S<br>34°05'39"S | 70°20'52"W<br>70°20'58"W | 3020<br>2760 | 375673.732<br>375515.098 | 6226213.48<br> 6226581.09 | 19<br>19 |
| 3 | 3 | 3010_06 | 34°05'51"S | 70°20'52"W | 3010 | 375673.732 | 6226213.48 | 19 |
| 4 | 4 | 2760_06 | 34°05'40"S | 70°20'58"W | 2760 | 375515.505 | 6226550.29 | 19 |
| 5 | 5<br> | 2760_06B_07 | 34°05'40"S | 70°20'58"W | 2760 | 375515.505 | 6226550.29 | 19 |
| 6 | 6 | 2760_08 | 34°05'41"S | 70°20'58"W | 2760 | 375515.912 | 6226519.49 | 19 |
| 7 | 7 | 2750_01A | 34°05'35"S | 70°21'01"W | 2750 | 375436.591 | 6226703.29 | 19 |
| 8 | 8 | 3000_07 | 34°05'50"S | 70°20'51"W | 3000 | 375698.952 | 6226244.63 | 19 |
| 9 | 9 | 2960_04 | 34°05'45"S | 70°20'47"W | 2960 | 375799.425 | 6226399.99 | 19 |
| 10 | 10 | 2960_05 | 34°05'47"S | 70°20'48"W | 2960 | 375774.61 | 6226338.05 | 19 |
| 11 | 11 | 2910_15 | 34°05'40"S | 70°20'59"W | 2910 | 375489.878 | 6226549.95 | 19 |

<!-- Estadísticas: 11 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 2: coordenadas UTM WGS 84 de las voladuras. www.epc-groupe.com -->
<!-- FIN TABLA 1 -->


|Voladura|Nombre|Fecha|Tipo|Tamaño|Q explo eq.<br>ANFO|FC eq. ANFO|Secuencia|Altura banco|diámetro|Q<br>explo/pozo|
|---|---|---|---|---|---|---|---|---|---|---|
|Voladura|Nombre|Fecha|Tipo|kt|kg|gr/t|pozo[ms]X<br>fila[ms]|m|"|kg|
|1|3020_06 A|07-02-2019|Contorno + precorte|50|8398|168|5X200|10|9|348|
|2|2760_05|08-03-2019|Contorno|59,8|12862|215|3X150|10|9|348|
|3|3010_06|19-03-2019|Contorno|102|17740|174|5X250|10|9|348|
|4|2760_06|22-03-2019|Contorno|24|12768|532|3X150|10|9|348|
|5|2760_06B_07|27-03-2019|Contorno|74,4|22175|298|3X150|10|9|348|
|6|2760_08|08-04-2019|Rampa|36,5|5455|150|3X150|variable|9|298|
|7|2750_01A|15-04-2019|Producción + Precorte|67|11426|171|5X250|10|9|348|
|8|3000_07|03-07-2019|Contorno + precorte|38|8481|224|5X250|10|9|348|
|9|2960_04|16-03-2020|Contorno + precorte|41|9490|231|5X200|10|9|345|
|10|2960_05|25-03-2020|Contorno + precorte|55|13234|241|5X200|10|9|345|
|11|2910_15|27-05-2022|Contorno+Rampa|60|8856|147|5X200|variable|9|298|

Tabla 1: parámetros característicos de las voladuras de la base de datos.

A continuación, se indican las coordenadas UTM WGS 84 Datum 19 Huso S, de cada una de
las voladuras (Tabla 2) y una vista topográfica (Ilustración 2).

|Col1|Voladura|Nombre|Coordenadas UTM WGS 84 Datum 19 Huso S|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||Voladura|Nombre|Latitud|Longitud|Cota|Este|Norte|Zona|
|1<br>2|1<br>2|3020_06 A<br>2760_05|34°05'51"S<br>34°05'39"S|70°20'52"W<br>70°20'58"W|3020<br>2760|375673.732<br>375515.098|6226213.48<br> 6226581.09|19<br>19|
|3|3|3010_06|34°05'51"S|70°20'52"W|3010|375673.732|6226213.48|19|
|4|4|2760_06|34°05'40"S|70°20'58"W|2760|375515.505|6226550.29|19|
|5|5<br>|2760_06B_07|34°05'40"S|70°20'58"W|2760|375515.505|6226550.29|19|
|6|6|2760_08|34°05'41"S|70°20'58"W|2760|375515.912|6226519.49|19|
|7|7|2750_01A|34°05'35"S|70°21'01"W|2750|375436.591|6226703.29|19|
|8|8|3000_07|34°05'50"S|70°20'51"W|3000|375698.952|6226244.63|19|
|9|9|2960_04|34°05'45"S|70°20'47"W|2960|375799.425|6226399.99|19|
|10|10|2960_05|34°05'47"S|70°20'48"W|2960|375774.61|6226338.05|19|
|11|11|2910_15|34°05'40"S|70°20'59"W|2910|375489.878|6226549.95|19|

Tabla 2: coordenadas UTM WGS 84 de las voladuras.

www.epc-groupe.com

7

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Ilustración 2: ubicación de las voladuras monitoreadas

Se observa que la mayoría corresponde a voladuras de contorno, es decir voladuras con filas
de pozos amortiguadas. Las otras variables características son:

 Tamaño de las voladuras: entre 24 y 102 kt

 Cantidad total de explosivo: entre 5,4 y 22,2 t

 Factor de carga (equivalente Anfo): entre 147 y 532 gr/t

 Los retardos entre cargas (desde 3msX150ms hasta 5msX250ms)

 La cantidad máxima de explosivo por pozo (carga “operante”): entre 298 y 348 kg

Todos los pozos son de 9” y los bancos son de 10 m.

Respecto a las vibraciones, un examen rápido de los registros permite extraer los valores de
la amplitud máxima del movimiento (PPV) en mm/s (Tabla 3).

www.epc-groupe.com

8

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Tabla 3: PPV máximo y distancia entre la voladura y los geófonos

Se observa una buena correlación entre PPV máximo y distancia (85,6%), con un PPV menor
para las rampas, y mayor para la voladura de producción. Los precortes producen un PPV
similar a las voladuras de contorno (Figura 1).

Figura 1: PPV máximo de las voladuras en función de la distancia.

www.epc-groupe.com

9

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Luego, se realizó un análisis más detallado, donde se identifica cada peak intermedio en los
registros de vibración, relacionándolo con el o los pozos responsables, y se calcula la distancia
al geófono (distancia mínima en caso de grupo de pozos). Este estudio se puede realizar por
la separación clara de los peaks entre filas de pozos, debido al uso de retardos largos (150 a
250 ms). El uso de retardos cortos entre pozo (3 a 5ms) no permite identificar cada carga. Sin
embargo, el número reducido de pozos por filas (entre 1 y 4) no debería alterar
fundamentalmente el modelo. En anexo se encuentra el análisis de cada voladura.

Figura 2: ejemplo de análisis detallado de los peaks intermedios de vibración y cálculo de las
distancias asociadas (voladura n°1). El registro de vibración corresponde a la suma vectorial
de la velocidad de partícula.

Este método permite obtener muchos más valores que el anterior (98 vs 12), sin debilitar la
correlación del modelo (correlación de 87,6%).

Con esta población de datos, se puede calibrar un modelo predictivo de PPV en función de la
distancia (modelo de atenuación geométrica simple) de tipo:

PPV=

K
Ecuación 1
d [λ]

Donde el _PPV_ la velocidad de partícula en mm/s, _d_ la distancia en m, _K_ y  parámetros de
ajuste.

www.epc-groupe.com

10

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

También se puede establecer una probabilidad de PPV, definida por un límite superior de
confianza de 90%. Se utiliza un 90% de confianza, que representa un criterio habitualmente
utilizado en la minería y para límites de aceptabilidad para normas que rigen eventos
puntuales (ver por ejemplo la norma de ruido establecido por la norma australiana AS-21872-2006).

Por lo tanto, se utiliza un límite superior de confianza de 90% definido por K max, lo que en
práctica significa que existe 90% de probabilidad que los PPV sean inferiores a:

11

PPV<

K max

d [λ] [=]

El valor medio es:

158800

Ecuación 2
d [1,74]

96990

Ecuación 3
d [1,74]

www.epc-groupe.com

PPV 50 =

K 50

d [λ] [=]

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Figura 3: modelo de atenuación geométrica de predicción de PPV. Arriba: escala lineal.

Abajo: escala logarítmica.

También se puede ajustar un modelo de tipo Devine, que relaciona el PPV y la distancia
escalar: Es decir, la distancia dividida por la raíz cuadrada de los kg de explosivo de la carga:

PPV= K(

d

√Q [)]

d

−α

Ecuación 4

Donde el _PPV_ la velocidad de partícula en mm/s, _d_ la distancia en m, _Q_ la cantidad de kg de
explosivo de la carga operante, _K_ y  parámetros de ajuste (Figura 4).

www.epc-groupe.com

12

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Figura 4: modelo de Devine de predicción de PPV. Arriba: escala lineal. Abajo: escala

logarítmica.

Este modelo tiene una correlación satisfactoria del 84,3%, y permite comparar PPV del Rajo
Sur con otras prácticas de voladura (por ejemplo, voladura de banco más altos o de pozos de
mayor diámetro), que no son propias del proyecto pero permiten descartar el impacto bajo
cualquier escenario más desfavorable.

www.epc-groupe.com

13

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Se resume este modelo con las ecuaciones siguientes:

PPV 50
= 334 (

d

√Q [)]

d

−1,41

14

Ecuación 5

Ecuación 6

www.epc-groupe.com

= 566 (

d

PPV< PPV max = K max
(

d

√Q [)]

d

√Q ~~[)]~~

d

−α

−1,41

con _PPV_ _max_ el límite superior de confianza de 90%.

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

**4** **MONITOREO ESPECIAL E IMPACTO SOBRE EL GLACIAR DE ROCA**

La voladura del 27 de mayo de 2022 fue monitoreada por 2 geófonos, alineados con el glaciar
de roca más cercano, y ubicados a una distancia de 274 m (P1) y 619 m (P2) respectivamente
de una voladura mixta, parte de contorno y parte de rampa (Ilustración 3 y Ilustración 4).

Ilustración 3: instalación de los geófonos P1 y P2 utilizados para el monitoreo especial de la
voladura del 27/05/2022

www.epc-groupe.com

15

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Ilustración 4: posición relativa de la voladura, de los geófonos y del glaciar de roca.

El registro de geófono P1 pudo ser analizado completamente (ya incluido en el modelo),
mientras que solamente se pudo considerar el peak máximo del geófono P2, por falta de la
captura del inicio de la vibración. Se observa que el peak del geófono P2 está alineado con el
modelo de predicción ya calibrado, lo que permitiría extrapolar el modelo a distancias

mayores.

www.epc-groupe.com

16

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Figura 5: PPV extraídos del monitoreo especial.

www.epc-groupe.com

17

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

**5** **IMPACTO SOBRE EL GLACIAR DE ROCA**

Después de revisión de otras tramitaciones ambientales con estudios de impacto de las
voladuras sobre glaciares de roca, aparece dos metodologías distintas: una que define un PPV
crítico fijo (70 mm/s) en base a la observación en terreno de ausencia de daño realizada
durante sismos de gran magnitud, y otra en base a un cálculo de estabilidad con método del
equilibrio límite.

**5.1** **Metodología del PPV crítico fijo**

La División Andina de Codelco propuso, en el EIA “Adecuación Obras Mineras de Andina
para Continuidad Operacional” (anexo 4.11), un valor límite de 70 mm/s a aplicar en el borde
del glaciar. Esta metodología se basa en la ausencia de daño observado en los glaciares de
roca en el entorno del rajo Don Luis, durante los terremotos de 1985 (Valparaíso, Mw 8,0) y
2010 (Maule, Mw 8,8). Luego de un estudio estadístico realizado con el análisis de los PPV
monitoreados durante 8 sismos con magnitud sobre 6,9, se establece una relación MagnitudDistancia-PPV, y se calcula un PPV mínimo al cual fueron probablemente sometidos los
glaciares de roca en 1985 y 2010, para llegar a este valor conservador de 70 mm/s.

Para una distancia actual entre el glaciar de roca y el límite del rajo (516 m aproximadamente,
ver Ilustración 5), y aplicando el formulismo de la ecuación 1, existe 90% de probabilidad
para que el PPV máximo sea inferior a 3,0 mm/s, o sea muy por debajo de los 70 mm/s (Figura
6).

www.epc-groupe.com

18

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Ilustración 5: distancia entre el límite actual del rajo y el glaciar de roca más cercano.

Figura 6: estimación del PPV máximo esperable con un límite de confianza de 90%, para una
distancia de 516 m.

Para un criterio de 70 mm/s, la distancia límite entre el borde del glaciar y las voladuras del
rajo, asumiendo que no haya modificación de los parámetros de diseño de las voladuras
(tamaño, altura de banco, diámetro de perforación, cantidad de explosivo por pozo y
retardos) sería de 84 m, con una probabilidad de 90% que esta distancia sea menor.

**5.2** **Metodología del equilibrio límite**

El impacto de las voladuras sobre la estabilidad de glaciares con el método del equilibrio
límite fue propuesto por Anglo American Sur S.A., EIA "Proyecto Los Bronces Integrado",
anexo C4-6.

El modelo calcula el factor de seguridad de una masa potencialmente inestable, agregando
una fuerza de inercia (horizontal) producto del movimiento de la masa por la vibración, y
cuya expresión está dado por:

19

C+mg(cosα−K h sinα)tanφ Ecuación 7

mg(K h cosα+sinα)

www.epc-groupe.com

FS =
ps

∑ esfuerzos resistantes

=
∑esfuerzos motores

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

con _C_ la cohesión de la base del bloque,  su fricción, _m_ su masa y  el ángulo del plano
inclinado. _K_ _h_ es la aceleración horizontal expresada en g.

Figura 7: Equilibrio de fuerzas en condición pseudo-estática

_K_ _h_
Por lo tanto, la solución del problema consiste en determinar la aceleración crítica para la
cual el factor de seguridad es igual a 1,0.

Luego, el PPV crítico se calcula suponiendo una onda sinusoidal:

ü = gK h = 2πf∗PPV
Ecuación 8

Donde ü es la aceleración horizontal y _f_ la frecuencia principal.

Es decir, para un factor de seguridad de 1, el PPV “crítico” actuando al centro de gravedad
del cuerpo glaciar sería dado por:

PPV crítico =

1
Ecuación 9
2πf [K] [y] [g ]

Donde _K_ _y_ la aceleración crítica (en g).

La Figura 8 presenta el PPV crítico (o velocidad crítica) en función de la frecuencia, para
distintos valores de aceleraciones críticas _K_ _y_ .

www.epc-groupe.com

20

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Figura 8: velocidad crítica en función de la frecuencia de una onda sinusoidal y de la
aceleración crítica.

_**5.2.1**_ _**Aceleración crítica (K**_ _**y**_ _**)**_

En su estudio, Los Bronces consideró que el glaciar podía ser asimilado a un bloque
deslizante, sin en la base del bloque (C=0). En este caso, el factor de seguridad es
independiente de la geometría (masa) del bloque, y el factor de seguridad pseudo-estático se
simplifica a:

(1−K h tanα)tanφ Ecuación 10

K h +tanα

FS =
ps

(cosα−K h sinα)tanφ

=
(K h cosα+sinα)

Es decir, la aceleración crítica _Kh_ se obtiene para un factor de seguridad de 1, y se expresa

como:

K =
y

tanφ−tanα Ecuación 11
1+tanφtanα

Sin embargo, en el caso de El Teniente, se dispone de la geometría de la base el glaciar, y se
observa que en el sector más vulnerable del glaciar, es decir más cercano a las voladuras (zona
de ablación), el cuerpo no puede ser asimilado a un bloque deslizante, ya que se apoya en
una superficie horizontal (Figura 9).

www.epc-groupe.com

21

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Figura 9: topografía del glaciar (datos comunicados por El Teniente), y sector analizado (zona
de ablación). Cuerpo I: bloque potencialmente inestable. Cuerpo II: bloque soportante.

Por eso se decidió determinar la aceleración crítica mediante simulaciones numéricas, con el
modelo numérico por diferencias finitas FLAC de Itasca. Este modelo permite simular los 4
tipos de materiales de la Figura 9 (Figura 10), con las propiedades geomecánicas de la Tabla

4.

www.epc-groupe.com

22

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Figura 10: simulación de la zona de ablación del glaciar

Tabla 4: valores de propiedades geotécnicas para los distintos elementos constitutivos del
glaciar (datos comunicados por El Teniente)

Se aplica una aceleración horizontal, y se calcula el factor de seguridad. La aceleración crítica
corresponde a un factor de seguridad de 1,0.

El modelo reológico utilizado es de Mohr-Coulomb.

Sin aceleración horizontal (condición estática, el factor de seguridad (FS) es de 5,2 (Figura 11),
o sea el pie del glaciar es muy estable.

www.epc-groupe.com

23

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Figura 11: simulación de la deformación de cizalle y del factor de seguridad para la zona de
ablación del glaciar en condiciones estáticas.

Para una aceleración sísmica de 0,2 g (Norma Sísmica Chilena NCh 433), el factor de
seguridad (FS) baja a 3 (Figura 12), pero el glaciar sigue estable (FS>1).

Figura 12: simulación de la deformación de cizalle y del factor de seguridad para la zona de
ablación del glaciar con una solicitación sísmica de 0,2g.

La ruptura del pie del glaciar se calcula para una aceleración de 0,8g (Figura 13).

www.epc-groupe.com

24

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Figura 13: simulación de la deformación de cizalle y del factor de seguridad para la zona de
ablación del glaciar con una solicitación sísmica de 0,8g.

En la Tabla 5 se presentan los valores del factor de seguridad en función de la aceleración
sísmica (en g).

|Kh FS|Col2|
|---|---|
|**0 **|5.18|
|**0.1**|3.87|
|**0.2**|3.03|
|**0.3**|2.44|
|**0.4**|2.0|
|**0.5**|1.65|
|**0.6**|1.4|
|**0.7**|1.16|
|**0.8**|1.01|
|**0.9**|0.86|
|**1 **|0.74|

Tabla 5: valores del factor de seguridad en función de la aceleración sísmica (en g)

Por lo tanto, la aceleración crítica que conduce a un factor de seguridad de 1,0 es de:

K h(FS=1) = K y = 0,8 Ecuación 12

www.epc-groupe.com

25

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

_**5.2.2**_ _**Velocidad crítica (PPV crítico)**_

Para calcular el PPV crítico con la ecuación 9, se requiere conocer las frecuencias que pueden
llegar al borde del glaciar.

Esas frecuencias se obtienen de los 11 monitoreos de vibraciones, cada uno entregando una
frecuencia principal por canal de medición horizontal (2 por geófono) calculado desde el
espectro completo de frecuencia obtenido con una transformada de Fourier. La distribución
de frecuencia está bien representada por una distribución normal (Figura 14):

Figura 14: distribución de frecuencias para los monitoreos (canales horizontales) de la Tabla
1 y ajuste con una distribución normal (en rojo)

Para esta función, existe 90% de probabilidad que la frecuencia sea inferior a 17,5 Hz.

Por lo tanto, existe 90% de probabilidad para que la velocidad crítica sea superior a 71 mm/s.

1
2π∗17,5 [0,8g= 71 mm/s ] Ecuación 13

www.epc-groupe.com

26

PPV crítico (P 90 ) =

1
2πf [K] [h] [g=]

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

**5.3** **Distancia crítica**

La distancia crítica corresponde a la distancia mínima a la cual se puede acerca la voladura
del glaciar, sin que sea necesario de realizar cambios de diseño del diagrama de perforación
y carguío.

Se obtiene de manera probabilística, utilizando las ecuaciones 1 y 9:

Ecuación 14

= (

2πfK

2πfK

k y g ~~[)]~~

d crit =
~~(~~

K
PPV crit [)]

1 λ⁄

1 λ⁄

El valor de K se obtiene ajustando una distribución normal a la ecuación 1, con los valores de
PPV y distancia de la Figura 3, y un factor de atenuación geométrica  de la ecuación 2, es
decir 1,74 (Figura 15).

Figura 15: ajuste de una distribución normal al parámetro _K_

La frecuencia _f_ se obtiene con la distribución normal de la Figura 14.

La distancia crítica se calcula con una simulación de Monte Carlo (Figura 16).

www.epc-groupe.com

27

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Figura 16: distancia crítica calculada con el método de Monte Carlo, haciendo variar la
frecuencia y el PPV esperado.

Esta simulación indica que existe 90% de probabilidad que esta distancia crítica sea inferior a
72,4 m o sea, que mientras las voladuras, con su diseño actual, se ubiquen a más de 72,4, el
PPV debería mantenerse debajo del PPV crítico.

Para un PPV crítico “fijo” de 70 mm/s establecido con observaciones durante los sismos, este
valor es de 84 m. Este valor es mayor, a pesar de considerar un PPV crítico mayor, porque no
considera el efecto de la frecuencia.

**5.4** **Estudio paramétrico para otro tipo de diseño de P&T**

Finalmente, se propone aplicar el modelo de Devine de la Figura 4 para otro tipo de diseño.

Se eligen 2 casos.

Caso A:

 - Banco de 10m

 - Diámetro de 9”

 - Explosivo no gasificado (densidad 1,3)

 - Longitud de columna de 6,5m

Caso B:

 - Banco de 15m

 - Diámetro de 10”5/8

www.epc-groupe.com

28

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

 - Explosivo no gasificado (densidad 1,3)

 - Longitud de columna de 11,5m

El primer caso corresponde a una práctica habitual para banco de 10 m, y el segundo para
banco de 15m.

Los resultados se presentan en la Tabla 6.

|Col1|Col2|Col3|Col4|Col5|Col6|K50|K90|K99|
|---|---|---|---|---|---|---|---|---|
|||||||334|566|723|
|**A**|**H**<br>m<br>10|**DIAM**<br>"<br>9|**L carga**<br>m<br>6.5|**Dens explo**<br>1.3|**Q**<br>kg<br>347|**PPV**<br>mm/s<br>3.1|**PPV**<br>mm/s<br>5.2|**PPV**<br>mm/s<br>**6.7**|
|**B**|15|10.625|11.5|1.3|855|5.8|9.9|**12.6**|

|alfa|1.41|
|---|---|
|**D**|516|

Tabla 6: PPV máximo esperable para los dos casos considerados (A y B).

Se observa que, para esos dos casos, los PPV máximos tienen 97,5% de probabilidad de estar
inferior a 6,7mm/s en el caso del banco de 10m, y de 12,6 mm/s para el banco de 15m (Figura
17), o sea muy inferior al PPV crítico definido en los párrafos anteriores.

www.epc-groupe.com

29

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Figura 17: simulación del PPV máximo (con 97,5% de probabilidad que el PPV real sea
inferior al valor indicado) para dos casos extremos. A: banco de 10m, diámetro de perforación
de 9”. B: banco de 15m, diámetro de perforación de 10”5/8.

www.epc-groupe.com

30

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

**6** **CONCLUSIONES**

El PPV máximo que podría llegar a la frente del glaciar rocoso más cercano a la mina Rajo
Sur (ubicado a una distancia de 516 m aproximadamente) tiene una probabilidad de 90% de
ser inferior a 3,0 mm/s, con las prácticas actuales de voladura.

El modelo utilizado fue calibrado con 98 datos de peak de vibraciones provenientes del
monitoreo de 11 voladuras realizadas entre 2019 y 2022, y para distancias entre 73 y 368 m.

Un monitoreo especial realizado con un geófono ubicado a 619 m demostró la robustez del
modelo y su utilidad para predecir vibraciones extrapoladas a mayor distancia.

Para definir el valor del PPV límite en la frente del glaciar rocoso, se utilizaron 2 métodos:

 un valor “sismológico”, es decir independiente de la forma del glaciar, basado en las
observaciones del impacto de los sismos de gran magnitud sobre la estabilidad de
glaciares en la zona central (tal como lo propuso la División Andina)

 un valor obtenido con un cálculo del equilibrio límite de la zona de ablación del glaciar
de roca, obtenido con simulaciones numéricas (diferencias finitas) y un
comportamiento reológico de Mohr-Coulomb.

Los valores son resumidos en la tabla siguiente (Tabla 7). Además, se presenta la distancia
mínima a la cual debería acercarse las voladuras del glaciar para potencialmente afectar su
estabilidad.

90% de confianza del límite superior:

|Col1|PPV fijo|equilibrio límite<br>(simulaciones numéricas)|
|---|---|---|
|**PPV crítico**|70 mm/s|71 mm/s|
|**distancia límite**|84 m|72 m|

Tabla 7: resumen de los PPV críticos calculados y distancias límites para las voladuras con
diseño actual

Se observa que sea cual sea el método empleado, se determinan PPVs críticos que establecen
distancias muy por bajo los 516 m que separan el glaciar del área del proyecto.

Finalmente, se ha realizado un estudio paramétrico que evalúa el impacto de las voladuras si
se cambia el diseño del diagrama de P&T o la geometría de la explotación, es decir si se decide
explotar bancos de 15 m en vez de 10 m, y cambiar el diámetro de perforación de 9” a 10”5/8.
Este cambio tampoco puede afectar el glaciar de roca, para la geometría del rajo proyectada.

www.epc-groupe.com

31

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

Cabe mencionar que el método de evaluación con equilibrio límite es muy conservador
porque supone que la aceleración sísmica inducida por la voladura se aplica de manera
permanente al glaciar, y no transitoria. Sin embargo, existe una literatura abundante que
compara la estabilidad de taludes bajo ambas condiciones, y concluye en el carácter muy
conservador del primer caso, o del desplazamiento insignificante (es decir no detectable por
la instrumentación) en el caso de alcanzar factores de seguridad inferiores a 1 en el caso del
segundo (ver por ejemplo Alberto Bolla and Paolo Paronuzzi 2021, IOP Conf. Ser.: Earth
Environ. Sci. 906 012093).

www.epc-groupe.com

32

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

# ANEXO: IDENTIFICACION DE LOS PEAKS DE VIBRACIÓN

www.epc-groupe.com

33

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

TABLA DE RESUMEN DE LOS PEAKS DE PPV

DISTANCIA PPV Q Tronadura ID pozo DISTANCIA PPV Q Tronadura ID pozo

257.0 9.9 348 1 1 322.0 2.7 348 8 1

263.0 11.0 348 1 2 316.0 2.4 348 8 2

250.0 20.2 348 1 3 310.0 4.8 348 8 3

254.0 10.8 348 1 4 303.0 5.5 348 8 4

260.0 13.8 348 1 5 252.0 5.3 246 9 1

270.0 9.7 348 1 6 248.0 4.4 345 9 2

260.0 14.9 348 1 7 246.0 6.8 246 9 3

266.0 7.5 348 1 8 236.0 8.2 345 9 4

243.0 10.8 348 1 9 230.0 9.8 345 9 5

247.0 5.2 149 1 10 221.0 4.2 345 10 1

253.0 5.3 149 1 11 229.0 5.2 345 10 2

266.0 4.3 149 1 12 217.0 6.2 345 10 3

139.0 14.8 348 2 1 212.0 6.6 345 10 4

123.0 41.7 348 2 2 224.0 8.8 345 10 5

117.0 54.3 348 2 3 182.0 8.0 148 10 6

131.0 35.4 348 2 4 184.0 10.9 148 10 7

98.0 35.0 348 2 5 204.0 9.7 345 10 8

115.0 37.6 348 2 6 187.0 13.0 148 10 9

128.0 23.3 348 2 7 273.9 3.9 202 11 1

91.0 49.3 248 4 1 277.1 4.1 202 11 2

88.0 31.3 248 4 2 280.3 7.5 202 11 3

85.0 35.3 248 4 3 289.2 5.1 252 11 4

84.0 42.2 149 4 4 286.9 8.1 202 11 5

81.0 42.5 149 4 5 290.3 5.5 202 11 6

98.0 32.0 373 4 6 293.7 7.9 202 11 7

103.0 27.6 373 4 7 297.4 4.7 202 11 8

107.0 28.6 373 4 8 301.2 5.1 202 11 9

95.0 27.0 373 4 9 305.0 3.0 202 11 10

92.0 22.9 373 4 10 308.8 2.9 202 11 11

89.0 32.7 373 4 11 291.1 3.3 164 11 13

115.0 22.3 373 4 12 295.0 3.0 164 11 14

119.0 24.7 373 4 13 299.2 3.8 164 11 15

124.0 18.8 373 4 14 303.5 4.5 164 11 16

105.0 37.8 373 5 1 307.8 3.9 164 11 17

108.0 22.9 298 5 2 312.1 4.4 164 11 18

110.0 18.8 373 5 3 316.5 5.0 164 11 19

108.0 22.9 224 5 4 320.9 5.4 164 11 20

117.0 13.5 224 5 5 325.3 4.0 164 11 21

122.0 22.5 224 5 6 329.7 3.6 164 11 22

127.0 16.2 224 5 7 334.2 4.6 164 11 23

136.0 27.6 373 5 8 338.7 3.5 164 11 24

142.0 14.1 373 5 9 342.9 3.8 164 11 25

150.0 17.5 373 5 10 347.1 2.9 164 11 26

154.0 12.5 373 5 11 351.3 3.0 164 11 27

158.0 12.9 373 5 12 355.6 2.5 164 11 28

162.0 8.8 373 5 13 359.0 2.9 164 11 29

167.0 6.5 373 5 14 364.2 1.8 164 11 30

171.0 17.5 348 5 15 368.5 2.6 164 11 31

|DISTANCIA|PPV|Q|Tronadura|ID pozo|
|---|---|---|---|---|
|322.0|2.7|348|8|1|
|316.0|2.4|348|8|2|
|310.0|4.8|348|8|3|
|303.0|5.5|348|8|4|
|252.0|5.3|246|9|1|
|248.0|4.4|345|9|2|
|246.0|6.8|246|9|3|
|236.0|8.2|345|9|4|
|230.0|9.8|345|9|5|
|221.0|4.2|345|10|1|
|229.0|5.2|345|10|2|
|217.0|6.2|345|10|3|
|212.0|6.6|345|10|4|
|224.0|8.8|345|10|5|
|182.0|8.0|148|10|6|
|184.0|10.9|148|10|7|
|204.0|9.7|345|10|8|
|187.0|13.0|148|10|9|
|273.9|3.9|202|11|1|
|277.1|4.1|202|11|2|
|280.3|7.5|202|11|3|
|289.2|5.1|252|11|4|
|286.9|8.1|202|11|5|
|290.3|5.5|202|11|6|
|293.7|7.9|202|11|7|
|297.4|4.7|202|11|8|
|301.2|5.1|202|11|9|
|305.0|3.0|202|11|10|
|308.8|2.9|202|11|11|
|291.1|3.3|164|11|13|
|295.0|3.0|164|11|14|
|299.2|3.8|164|11|15|
|303.5|4.5|164|11|16|
|307.8|3.9|164|11|17|
|312.1|4.4|164|11|18|
|316.5|5.0|164|11|19|
|320.9|5.4|164|11|20|
|325.3|4.0|164|11|21|
|329.7|3.6|164|11|22|
|334.2|4.6|164|11|23|
|338.7|3.5|164|11|24|
|342.9|3.8|164|11|25|
|347.1|2.9|164|11|26|
|351.3|3.0|164|11|27|
|355.6|2.5|164|11|28|
|359.0|2.9|164|11|29|
|364.2|1.8|164|11|30|
|368.5|2.6|164|11|31|

www.epc-groupe.com

|DISTANCIA|PPV|Q|Tronadura|ID pozo|
|---|---|---|---|---|
|257.0|9.9|348|1|1|
|263.0|11.0|348|1|2|
|250.0|20.2|348|1|3|
|254.0|10.8|348|1|4|
|260.0|13.8|348|1|5|
|270.0|9.7|348|1|6|
|260.0|14.9|348|1|7|
|266.0|7.5|348|1|8|
|243.0|10.8|348|1|9|
|247.0|5.2|149|1|10|
|253.0|5.3|149|1|11|
|266.0|4.3|149|1|12|
|139.0|14.8|348|2|1|
|123.0|41.7|348|2|2|
|117.0|54.3|348|2|3|
|131.0|35.4|348|2|4|
|98.0|35.0|348|2|5|
|115.0|37.6|348|2|6|
|128.0|23.3|348|2|7|
|91.0|49.3|248|4|1|
|88.0|31.3|248|4|2|
|85.0|35.3|248|4|3|
|84.0|42.2|149|4|4|
|81.0|42.5|149|4|5|
|98.0|32.0|373|4|6|
|103.0|27.6|373|4|7|
|107.0|28.6|373|4|8|
|95.0|27.0|373|4|9|
|92.0|22.9|373|4|10|
|89.0|32.7|373|4|11|
|115.0|22.3|373|4|12|
|119.0|24.7|373|4|13|
|124.0|18.8|373|4|14|
|105.0|37.8|373|5|1|
|108.0|22.9|298|5|2|
|110.0|18.8|373|5|3|
|108.0|22.9|224|5|4|
|117.0|13.5|224|5|5|
|122.0|22.5|224|5|6|
|127.0|16.2|224|5|7|
|136.0|27.6|373|5|8|
|142.0|14.1|373|5|9|
|150.0|17.5|373|5|10|
|154.0|12.5|373|5|11|
|158.0|12.9|373|5|12|
|162.0|8.8|373|5|13|
|167.0|6.5|373|5|14|
|171.0|17.5|348|5|15|
|177.0|21.3|248|5|16|
|178.0|16.6|149|5|17|

34

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

www.epc-groupe.com

35

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

www.epc-groupe.com

36

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

www.epc-groupe.com

37

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

www.epc-groupe.com

38

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

www.epc-groupe.com

39

Proyecto “Levantamiento Línea

Base Optimización Rajo Sur”

www.epc-groupe.com

40

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: La voladura n°11 corresponde al monitoreo especial.**

| Voladura | Nombre | Fecha | Tipo | Tamaño | Q explo eq.<br>ANFO | FC eq. ANFO | Secuencia | Altura banco | diámetro | Q<br>explo/pozo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Voladura | Nombre | Fecha | Tipo | kt | kg | gr/t | pozo[ms]X<br>fila[ms] | m | " | kg |
| 1 | 3020_06 A | 07-02-2019 | Contorno + precorte | 50 | 8398 | 168 | 5X200 | 10 | 9 | 348 |
| 2 | 2760_05 | 08-03-2019 | Contorno | 59,8 | 12862 | 215 | 3X150 | 10 | 9 | 348 |
| 3 | 3010_06 | 19-03-2019 | Contorno | 102 | 17740 | 174 | 5X250 | 10 | 9 | 348 |
| 4 | 2760_06 | 22-03-2019 | Contorno | 24 | 12768 | 532 | 3X150 | 10 | 9 | 348 |
| 5 | 2760_06B_07 | 27-03-2019 | Contorno | 74,4 | 22175 | 298 | 3X150 | 10 | 9 | 348 |
| 6 | 2760_08 | 08-04-2019 | Rampa | 36,5 | 5455 | 150 | 3X150 | variable | 9 | 298 |
| 7 | 2750_01A | 15-04-2019 | Producción + Precorte | 67 | 11426 | 171 | 5X250 | 10 | 9 | 348 |
| 8 | 3000_07 | 03-07-2019 | Contorno + precorte | 38 | 8481 | 224 | 5X250 | 10 | 9 | 348 |
| 9 | 2960_04 | 16-03-2020 | Contorno + precorte | 41 | 9490 | 231 | 5X200 | 10 | 9 | 345 |
| 10 | 2960_05 | 25-03-2020 | Contorno + precorte | 55 | 13234 | 241 | 5X200 | 10 | 9 | 345 |
| 11 | 2910_15 | 27-05-2022 | Contorno+Rampa | 60 | 8856 | 147 | 5X200 | variable | 9 | 298 |
