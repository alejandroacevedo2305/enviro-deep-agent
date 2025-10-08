---
title: Sin título
author: Nelson MO
date: D:20210311194443-03'00'
language: es
type: report
pages: 19
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 1-6 ESTUDIO DE CAMPOS ELECTROMAGNÉTICOS
  - APÉNDICE 1. CÁLCULO DE GRADIENTE SUPERFICIAL Y RADIO INTERFERENCIA
-->

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

# ANEXO 1-6 ESTUDIO DE CAMPOS ELECTROMAGNÉTICOS

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

**ÍNDICE DE CONTENIDO**

**1** **OBJETIVO Y ALCANCE DEL ESTUDIO .................................................................................... 1**
**2** **DESCRIPCIÓN DEL PROYECTO ............................................................................................. 1**
**3** **CAMPO ELECTROMAGNÉTICO EN ALTA TENSIÓN ................................................................ 4**
**4** **INFORMACIÓN RECOPILADA DE LA LITERATURA TÉCNICA ................................................... 4**

4.1 Campo magnético de transformador de 220/66kV ........................................................ 4

**5** **MODELACIÓN DEL PATIO 220/66KV DE SUBESTACIÓN ........................................................ 5**
**6** **RADIO INTERFERENCIA GENERADA POR SUBESTACIÓN ..................................................... 10**
**7** **LÍMITES DE RADIO INTERFERENCIA PROVOCADA POR INSTALACIONES DE ALTA TENSIÓN . 11**
**8** **NORMAS APLICABLES EN CHILE PARA EXPOSICIÓN HUMANA A CAMPOS EM DE 50 HZ ...... 11**

**9** **CONCLUSIONES ............................................................................................................... 12**
**10** **REFERENCIAS BIBLIOGRÁFICAS..................................................................................... 13**

**ÍNDICE DE TABLAS**

Tabla 1. Campo magnético según distancia para un transformador de 60MVA ................................ 5
Tabla 2. Valores de Campo en borde subestación .............................................................................. 8
Tabla 3. Valores de Campo en borde subestación ............................................................................ 10
Tabla 4. Radio interferencia generada por barras de 66kV .............................................................. 11
Tabla 5. Límite de Interferencias de Radio, recomendados por Asociación de Normas Canadienses

........................................................................................................................................................... 11

Tabla 6. Valores de campo electromagnético y confrontación con límites de norma ..................... 12
Tabla 7. Radio interferencia emitida por nuevos equipos ................................................................ 13

**INDICE DE FIGURAS**

Figura 1. Nuevas instalaciones para subestación Nueva Valdivia ....................................................... 2
Figura 2. Perfil barras AIS 66kV ........................................................................................................... 3
Figura 3. Perfil corte transversal subestación ..................................................................................... 3
Figura 5 Trayectorias para estudio de campos en patio de 66kV ..................................................... 6
Figura 6. Campo eléctrico a 1m sobre el suelo en trayectoria A1-A2 ................................................. 7
Figura 7. Inducción magnética a 1m sobre el suelo en trayectoria A1-A2 .......................................... 7
Figura 8 Trayectoria para estudio de campos en barra de 23kV ....................................................... 8
Figura 9. Campo eléctrico a 1m sobre el suelo bajo barras de 23kV .................................................. 9
Figura 10. Inducción magnética a 1m sobre el suelo bajo barras de 23kV ......................................... 9
Figura 11. Radio interferencia de barras de 66kV ............................................................................. 10

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **i**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

**1** **OBJETIVO Y ALCANCE DEL ESTUDIO**

El Proyecto corresponde a la ampliación de la subestación actualmente conocida como “Subestación
Seccionadora Nueva Valdivia”, que se encuentra en operación normal y cuya implementación fue
aprobada mediante la Resolución Exenta N° 005/2018, del SEA de la Región de Los Ríos.

En este Informe se desarrolla una estimación de los campos electromagnéticos de baja y alta
frecuencia que pueden presentarse en operación debido a la ampliación de la Subestación Nueva
Valdivia, que comprende la construcción de un patio de 66kV en configuración barra principal más
barra de transferencia, con espacio para al menos 5 paños adicionales, la instalación de un
transformador 220/66kV, 60 MVA con sus respectivos paños de conexión en ambos niveles de
tensión y, la canalización para salida subterránea de una línea en 66kV. Además, se deberá ampliar
la barra principal del Patio de 23kV existente en 4 paños y se dejará lugar para la construcción futura
de una barra de iguales características. El Proyecto incluye todas las obras y labores necesarias para
la ejecución y puesta en servicio, tales como adecuaciones en el patio de media tensión, adecuación
de las protecciones, SCADA, obras civiles, montaje, malla de puesta a tierra y pruebas de los nuevos
equipos, entre otras.

Luego de presentar las características del Proyecto de ampliación de la Subestación Nueva Valdivia,
se revisa la información bibliográfica respecto de valores medidos o calculados de campo
electromagnético de frecuencia industrial en equipos similares a los incorporados en la subestación.
Se realiza para los nuevos patios de la subestación un modelamiento de conductores de barras y
líneas mediante el software utilitario QuickField [1], que aplica el método de elementos finitos para
obtener campo eléctrico y campo magnético en torno al equipo analizado.

Posteriormente, se realiza una estimación del nivel perturbador a frecuencias de radio generado
por dichos patios debido al fenómeno corona, empleando expresiones aproximadas de uso habitual
aplicadas a líneas de alta tensión.

Se entrega los valores límites recomendados de radio interferencia provocada por instalaciones de
alta tensión y las normas de referencia aplicables en Chile respecto de la exposición humana a
campos electromagnéticos de 50 Hz.

Finalmente, estos valores se confrontan con los respectivos valores obtenidos en la recopilación de
información bibliográfica y las modelaciones, con el objeto de establecer una conclusión respecto
al impacto ambiental de las nuevas instalaciones del proyecto, desde el punto de vista técnico de la
emisión electromagnética de baja y alta frecuencia.

**2** **DESCRIPCIÓN DEL PROYECTO**

La subestación Seccionadora Nueva Valdivia 220 kV se encuentra en servicio desde junio de 2019,
bajo el nombre de SE El Laurel. La subestación cuenta con un patio de 220 kV en tecnología GIS para

seccionar la Línea 2x220 kV Valdivia-Rahue 220 kV.

La ampliación de la Subestación Nueva Valdivia comprende la construcción de un patio de 66kV en
configuración barra principal más barra de transferencia, con espacio para al menos 5 paños
adicionales, la instalación de un transformador 220/66kV, 60 MVA con sus respectivos paños de

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **1**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

conexión en ambos niveles de tensión y, la canalización para salida subterránea de una línea en

66kV.

Además, se deberá ampliar la barra principal del Patio de 23kV existente en 4 paños y se dejará lugar
para la construcción futura de una barra de iguales características.

**Figura 1. Nuevas instalaciones para subestación Nueva Valdivia**

_Fuente: Ingeniería del Proyecto_

La Subestación contará una vez terminada la ampliación, con tres niveles de voltaje 220kV, 66kV y
23 kV. Para 220 kV la SE contará con una configuración interruptor y medio en tecnología GIS. Para
66 kV la configuración será barra principal más barra de transferencia en tecnología AIS.

La barra principal 66kV deberá dimensionarse para soportar una potencia igual o superior a 200
MVA a una temperatura ambiente de 35°C y una corriente de corto circuito de 40 kA.

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **2**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

Se incluye a continuación unos perfiles que permiten clarificar distancias y alturas de conductores,
para el modelamiento.

**Figura 2. Perfil barras AIS 66kV**

**Figura 3. Perfil corte transversal subestación**

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **3**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

**3** **CAMPO ELECTROMAGNÉTICO EN ALTA TENSIÓN**

La unidad del campo eléctrico es el Volt por metro [V/m] o Kilo Volt por metro [KV/m] en alta tensión
y es dependiente del voltaje de los conductores.

El campo magnético se debe a la corriente que circula por los conductores. La magnitud
representativa del campo magnético es la “Inducción Magnética” o “Densidad de Flujo Magnético”
B **,** que tiene como unidad de medida práctica la mili Gauss (1 mG = 10 [-3] Gauss) o el micro Tesla (1T
= 10 [-6] Tesla) y se relacionan por: 1 T = 10 mG.

Para investigar los efectos ambientales de los campos electromagnéticos, se acostumbra a
caracterizar al campo eléctrico y el campo magnético cerca de una instalación de alta tensión por el
concepto “Campo a nivel del suelo”, que corresponde al campo eléctrico o magnético medido o
calculado a 1 metro de altura sobre el suelo, en ausencia de otros objetos.

**4** **INFORMACIÓN RECOPILADA DE LA LITERATURA TÉCNICA**

Se incluye a continuación información recopilada de investigación bibliográfica de la literatura
técnica, respecto de valores de campo medidos o calculados en equipos similares a los del proyecto.

**4.1** **Campo magnético de transformador de 220/66kV**

En la referencia [2] se ilustra el comportamiento del campo magnético, medido y extrapolado, desde
la pared de un transformador de 220/66 kV, Figura que se reproduce a continuación.

**Figura 4. Campo magnético desde la pared de un transformador 220/66 kV**

_Fuente: Referencia [2]_

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **4**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

Se aprecia un decaimiento en proporción inversa al logaritmo de la distancia, lo cual determina que,
a 16 m desde la pared del transformador, la inducción magnética es inferior a 1 [micro Tesla]. Por
lo tanto, de acuerdo con esta información, para el caso particular de la subestación Nueva Valdivia,
el efecto del transformador es muy localizado, no alcanzando a manifestarse fuera de los límites de

la subestación.

En base a una serie de experiencias y resultados obtenidos en una amplia gama de potencias,
comparables a las de los nuevos transformadores de la subestación, en la referencia [7] se sugiere
una relación simple para estimar el valor efectivo de la inducción magnética en la vecindad de un

transformador:

B rms (r) = k Tr P N /r [3] [micro Tesla]

P N : Potencia Nominal del equipo [kVA]
r: Distancia desde el centro del equipo [m]
k Tr : Coeficiente de Campo [ms/A], [Tm [3] /VA]
Un valor establecido de k Tr en la misma referencia es: 0,04 Tm [3] /kVA.

Esta relación demuestra que el campo magnético de equipos concentrados decrece rápidamente al
alejarse del equipo (relación inversa con la tercera potencia de la distancia). Aplicando la relación
anterior a un transformador de 60MVA, se obtiene la siguiente Tabla de variación de la inducción
magnética con la distancia:

**Tabla 1. Campo magnético según distancia para un transformador de 60MVA**

|Distancia [m]|5|7,5|10|12,5|15|
|---|---|---|---|---|---|
|**Inducción magnética [micro Tesla]**|19|5,69|2,40|1,23|0,71|

_Fuente: Elaboración propia_

El resultado que muestra la Tabla anterior, consistente con lo mostrado en la Figura 4, confirma que
el campo magnético generado por los nuevos transformadores que se incorporan en la ampliación
de la subestación Nueva Valdivia resulta inferior a 1 [micro Tesla] en el borde de la subestación.

**5** **MODELACIÓN DEL PATIO 220/66KV DE SUBESTACIÓN**

La metodología utilizada consiste en una modelación de los conductores de las barras y líneas del
patio de 66kV de la subestación, utilizando elementos finitos y el software utilitario QuickField [1]
para la solución del campo eléctrico y magnético.

El resultado del estudio se presenta en la forma de perfiles de campo evaluados a una altura de 1,0
m sobre el suelo, a través de la trayectoria A1-A2 que cruza las barras en 66 kV mostrada en la Figura
siguiente.

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **5**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

**Figura 4 Trayectorias para estudio de campos en patio de 66kV**

_Fuente: Elaboración propia._

En los gráficos de campo, las líneas rojas indican el borde del patio o de la subestación y los círculos
rojos, la ubicación aproximada de los conductores.

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **6**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

**Figura 5. Campo eléctrico a 1m sobre el suelo en trayectoria A1-A2**

_Fuente: Elaboración propia._

Para evaluar el campo magnético se consideró una potencia de 60MVA, lo que entrega una corriente
de 525 Amperes.

**Figura 6. Inducción magnética a 1m sobre el suelo en trayectoria A1-A2**

_Fuente: Elaboración propia._

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **7**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

En el borde del patio de 66kV los valores resultantes son:

**Tabla 2. Valores de Campo en borde subestación**

|Col1|Campo eléctrico<br>[V/m]|Inducción magnética<br>[micro Tesla]|
|---|---|---|
|Barras 66kV|365|2,61|

_Fuente: Elaboración propia._

Para el estudio de campos en el Patio de 23kV, se consideró una trayectoria C1-C2 cruzando las

barras de 23kV.

Figura 7 Trayectoria para estudio de campos en barra de 23kV

_Fuente: Elaboración propia a partir de información entregada por Traselec._

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **8**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

**Figura 8. Campo eléctrico a 1m sobre el suelo bajo barras de 23kV**

_Fuente: Elaboración propia._

**Figura 9. Inducción magnética a 1m sobre el suelo bajo barras de 23kV**

_Fuente: Elaboración propia._

En el borde del patio de 23kV los valores resultantes son:

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **9**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

**Tabla 3. Valores de Campo en borde subestación**

|Campo eléctrico<br>[V/m]|Inducción magnética<br>[micro Tesla]|
|---|---|
|203|1,06|

_Fuente: Elaboración propia._

**6** **RADIO INTERFERENCIA GENERADA POR SUBESTACIÓN**

La radio interferencia es generada por el fenómeno corona, que corresponde a la ionización del aire
en torno al conductor por efecto de un alto campo eléctrico; este a su vez es generado por el voltaje

de los conductores.

La mayor fuente de radio interferencia en el caso de los equipos que se incorporan, la constituyen

las barras de 66kV.

En la Figura siguiente se presenta el resultado de la evaluación de radio interferencia provocada por
los conductores de barras de 66kV, en un perfil transversal a las barras, simétrico con respecto a la
ubicación de cada juego de barras, en función de la distancia hacia solo un costado. En el Apéndice
1 se presenta el detalle del cálculo.

**Figura 10. Radio interferencia de barras de 66kV**

_Fuente: Elaboración propia._

El borde más cercano de la subestación se encuentra a 10m del conductor (línea azul, 16m desde el
eje del gráfico) y la distancia de norma es 15m desde el borde (línea verde); los respectivos valores

son:

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **10**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

**Tabla 4. Radio interferencia generada por barras de 66kV**

|Col1|Radio interferencia<br>[dB/uV/m]|
|---|---|
|Borde subestación|18,25|
|A 15m desde el borde|7,46|

_Fuente: Elaboración propia._

**7** **LÍMITES DE RADIO INTERFERENCIA PROVOCADA POR INSTALACIONES DE ALTA TENSIÓN**

En la referencia [4], se propone la siguiente recomendación para el límite de campo electromagnético

perturbador de alta frecuencia (radio interferencia) emitida por líneas de transmisión y subestaciones, según

su nivel de tensión:

**Tabla 5. Límite de Interferencias de Radio, recomendados por Asociación de Normas**

**Canadienses**

|Voltaje nominal entre fases<br>(kV)|Nivel de Radio Interferencia<br>(dB/1μV/m)|
|---|---|
|Menos de 70|43|
|70 - 200|49|
|200 - 300|53|
|400 - 600|60|
|Sobre 600|63|
|Para líneas de transmisión, valores indicados a 15 m de la fase externa y a 0,5 MHz<br>Para subestaciones, valores medidos a 15 m del cerco del recinto de la subestación|Para líneas de transmisión, valores indicados a 15 m de la fase externa y a 0,5 MHz<br>Para subestaciones, valores medidos a 15 m del cerco del recinto de la subestación|

_Fuente: Referencia [4]_

Para una línea de transmisión o subestación de 66kV, el valor límite corresponde a 43 [dB/1μV/m].

**8** **NORMAS APLICABLES EN CHILE PARA EXPOSICIÓN HUMANA A CAMPOS EM DE 50 HZ**

En nuestro país no existe reglamentación relativa a los valores límites permitidos de exposición de
las personas a los campos electromagnéticos de frecuencia industrial. No obstante, la regulación
ambiental que rige el tema de emisiones señala que, de no existir una regulación nacional, debe
aplicarse como norma de referencia aquella que se encuentre vigente en estados específicos.

El Decreto No 40 del Ministerio del Medio Ambiente, “Aprueba Reglamento del Sistema de
Evaluación de Impacto Ambiental”, publicado el 12-08-2013, y que entró en vigencia el 24-12-2013,

indica en su Artículo 11:

_Artículo 11.- Normas de referencia._

Las normas de calidad ambiental y de emisión que se utilizarán como referencia para los efectos de
evaluar si se genera o presenta el riesgo indicado en la letra a) y los efectos adversos señalados en
la letra b), ambas del artículo 11 de la Ley, serán aquellas vigentes en los siguientes Estados:
República Federal de Alemania, República Argentina, Australia, República Federativa del Brasil,

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **11**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

Canadá, Reino de España, Estados Unidos Mexicanos, Estados Unidos de América, Nueva Zelandia,
Reino de los Países Bajos, República Italiana, Japón, Reino de Suecia y Confederación Suiza. Para la
utilización de las normas de referencia, se priorizará aquel Estado que posea similitud en sus
componentes ambientales, con la situación nacional y/o local, lo que será justificado
razonablemente por el proponente.

La recomendación de uso más frecuente para público general y exposición permanente es la
publicada por la ICNIRP [3], organismo no gubernamental reconocido por la Organización Mundial
de la Salud como referente en el tema, que establece 5.000 [V/m] para el campo eléctrico y 200

[micro Tesla] para la inducción magnética.

Recientemente se ha publicado el PLIEGO TÉCNICO NORMATIVO RPTDN°07, dictado por Resolución
Exenta No 33.277, de fecha 10/09/2020, de la Superintendencia de Electricidad y Combustibles, que
en su Artículo 4.7 establece:

_“Los límites máximos permisibles para la seguridad de las personas, en cuanto a la emisión de campo_
_electromagnético para el diseño de líneas aéreas de corriente alterna de 50 Hz de frecuencia, y que_
_será evaluado en el exterior de la franja de seguridad, a 1 metro sobre el nivel del suelo, en_
_condiciones normales de operación de la línea, con los conductores en reposo, serán los que_
_determinen las normas respectivas. En ausencia de regulación técnica nacional, se debe cumplir con_
_lo siguiente:_

 - _5 kV/m para campo eléctrico (valor RMS);_

 - _100 μT para campo magnético (valor RMS).”_

**9** **CONCLUSIONES**

De los resultados obtenidos en la investigación bibliográfica referente a efectos provocados por
equipos de subestaciones de los niveles de voltaje y potencia similares a los incorporados en la
subestación Nueva Valdivia, y en el respectivo modelamiento, se obtiene los valores indicados en la
Tabla que sigue:

**Tabla 6. Valores de campo electromagnético y confrontación con límites de norma**

|Instalación|Campo eléctrico<br>[V/m]|Inducción magnética<br>[micro Tesla]|Ubicación|
|---|---|---|---|
|**Referencias**||||
|Transformador 220/66|0|<1,0|A 10 m|
|Transformador 60MVA|0|<1,0|Borde S/E|
|**Modelaciones**||||
|Barras 66 kV|365|5,1|Borde S/E|
|Barras 23 kV|203|1,06|Borde S/E|
|Límite RPTDN°07|5.000|100|Borde S/E|
|CUMPLE|SI|SI||

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **12**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

Todos los valores resultan inferiores a los valores límites recomendados por la ICNIRP [3] y por la
RPTDN°07 . Los valores de radio interferencia generados por las nuevas instalaciones,
específicamente las barras del patio de 66kV, son:

**Tabla 7. Radio interferencia emitida por nuevos equipos**

|Col1|Radio interferencia<br>[dB/uV/m]|
|---|---|
|Borde Subestación|18,25|
|A 15m del borde Subestación|7,46|
|Límite norma canadiense<br>(a 15m del borde subestación)|43|
|CUMPLE|SI|

A su vez, estos valores son inferiores al límite de 43 [dB/ 1uV/m] establecido por la normativa
canadiense [3] bajo idénticas condiciones.

En consecuencia, se comprueba que las nuevas instalaciones correspondientes a la ampliación de la
Subestación Nueva Valdivia cumplen la normativa vigente para campo electromagnético de baja y

alta frecuencia.

**10** **REFERENCIAS BIBLIOGRÁFICAS**

[[1] Students' QuickField (TM) Finite Element Analysis System <www.quickfield.com>](http://www.quickfield.com/)

[2] Patricia Arnera, Pedro Issouribehere, _et all_ .

“Evaluación de campos eléctricos y magnéticos en instalaciones de la Administración Nacional de
Electricidad - ANDE, Asunción, Paraguay. Trabajo presentado al Comité de estudio 36 en el X Encuentro
Regional Latinoamericano de la CIGRE, mayo 2003, Puerto Iguazú, Argentina.

[3] Informe de ICNIRP (Comisión Internacional para la Protección contra la radiación No Ionizante) “Interim

guidelines on limits of exposure to 50/60 Hz Electric and Magnetic Fields” 1998, Health Physics, 74,4,494
522

[4] Association canadienne de normalisation, Valeurs limites et methods de mesure du bruit

électromagnétique (0,15 à 30 MHz) produit par les reseaux de courant alternatif. CAN3- C108.3.1M84. Octobre 1984.

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **13**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

# APÉNDICE 1. CÁLCULO DE GRADIENTE SUPERFICIAL Y RADIO INTERFERENCIA

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **1**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

A continuación, se incluye el listado de salida del programa LINEAS, de elaboración propia, que
ocupa el método de simulación de cargas para evaluar el campo eléctrico superficial de los
conductores y la radio interferencia, aplicado a las barras de 66kV.

CAMPO ELECTRICO Y POTENCIAL INDUCIDO EN TORNO A LINEAS DE TRANSMISIÓN

Número total de conductores: 6

Número de conductores activos: 6

Numero de cables de guardia: 0

|Fase|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|**Numero de subconductores **|1|1|1|1|1|1|
|**Radio del subconductor (cm) **|2.000|2.000|2.000|2.000|2.000|2.000|
|**ubicación lateral conductor (m) **|-6.00|-4.00|-2.00|2.00|4.00|6.00|
|**Altura conductor sobre suelo (m) **|6.00|6.00|6.00|6.00|6.00|6.00|

## Matriz de coeficientes (amplif. por (2 ¶ ε 0 ))

6.3969 1.8055 1.1513 .5893 .4460 .3466

1.8055 6.3969 1.8055 .8047 .5893 .4460

1.1513 1.8055 6.3969 1.1513 .8047 .5893

.5893 .8047 1.1513 6.3969 1.8055 1.1513

.4460 .5893 .8047 1.8055 6.3969 1.8055

.3466 .4460 .5893 1.1513 1.8055 6.3969

## Matriz de capacitancias (amplif. por 1/(2 ¶ ε 0 ))

.1724 -.0425 -.0173 -.0060 -.0035 -.0027

-.0425 .1818 -.0410 -.0096 -.0049 -.0035

-.0173 -.0410 .1766 -.0213 -.0096 -.0060

-.0060 -.0096 -.0213 .1766 -.0410 -.0173

-.0035 -.0049 -.0096 -.0410 .1818 -.0425

-.0027 -.0035 -.0060 -.0173 -.0425 .1724

Potenciales de conductores ( KVolts)

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **1**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

( 38.1050, 0.0000 ) 38.1050

( -19.0525, -32.9999 ) 38.1050

( -19.0525, 32.9999 ) 38.1050

( 38.1050, 0.0000 ) 38.1050

( -19.0525, -32.9999 ) 38.1050

( -19.0525, 32.9999 ) 38.1050

## Cargas en conductores (Cb)/(2 ¶ ε 0 )

( 7.5987, 0.8581 ) 7.6470

( -4.5061, -7.3036 ) 8.5818

( -3.7560, 7.2988 ) 8.2085

( 8.1989, 0.3966 ) 8.2085

( -4.0720, -7.5542 ) 8.5818

( -3.0562, 7.0097 ) 7.6470

Gradientes superficiales (kVef./cm)

( 3.7993, 0.4291 ) 3.8235

( -2.2531, -3.6518 ) 4.2909

( -1.8780, 3.6494 ) 4.1042

( 4.0994, 0.1983 ) 4.1042

( -2.0360, -3.7771 ) 4.2909

( -1.5281, 3.5049 ) 3.8235

Radio interferencia [dB/uV/m]

|RI1|RI2|RI3|Col4|RI|
|---|---|---|---|---|
|4,24|6,12|5,79||7,46|

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **2**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|AMPLIACIÓN SUBESTACIÓN NUEVA VALDIVIA|

**Anexo 1-6 - Estudio de Campos Electromagnéticos** **3**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Campo magnético según distancia para un transformador de 60MVA****

| Distancia [m] | 5 | 7,5 | 10 | 12,5 | 15 |
| --- | --- | --- | --- | --- | --- |
| **Inducción magnética [micro Tesla]** | 19 | 5,69 | 2,40 | 1,23 | 0,71 |

**Tabla 2.: Valores de Campo en borde subestación****

| Col1 | Campo eléctrico<br>[V/m] | Inducción magnética<br>[micro Tesla] |
| --- | --- | --- |
| Barras 66kV | 365 | 2,61 |

**Tabla 3.: Valores de Campo en borde subestación****

| Campo eléctrico<br>[V/m] | Inducción magnética<br>[micro Tesla] |
| --- | --- |
| 203 | 1,06 |

**Tabla 4.: Radio interferencia generada por barras de 66kV****

| Col1 | Radio interferencia<br>[dB/uV/m] |
| --- | --- |
| Borde subestación | 18,25 |
| A 15m desde el borde | 7,46 |

**Tabla 5.: Límite de Interferencias de Radio, recomendados por Asociación de Normas****

| Voltaje nominal entre fases<br>(kV) | Nivel de Radio Interferencia<br>(dB/1μV/m) |
| --- | --- |
| Menos de 70 | 43 |
| 70 - 200 | 49 |
| 200 - 300 | 53 |
| 400 - 600 | 60 |
| Sobre 600 | 63 |
| Para líneas de transmisión, valores indicados a 15 m de la fase externa y a 0,5 MHz<br>Para subestaciones, valores medidos a 15 m del cerco del recinto de la subestación | Para líneas de transmisión, valores indicados a 15 m de la fase externa y a 0,5 MHz<br>Para subestaciones, valores medidos a 15 m del cerco del recinto de la subestación |

**Tabla 6.: Valores de campo electromagnético y confrontación con límites de norma****

| Instalación | Campo eléctrico<br>[V/m] | Inducción magnética<br>[micro Tesla] | Ubicación |
| --- | --- | --- | --- |
| **Referencias** |  |  |  |
| Transformador 220/66 | 0 | <1,0 | A 10 m |
| Transformador 60MVA | 0 | <1,0 | Borde S/E |
| **Modelaciones** |  |  |  |
| Barras 66 kV | 365 | 5,1 | Borde S/E |
| Barras 23 kV | 203 | 1,06 | Borde S/E |
| Límite RPTDN°07 | 5.000 | 100 | Borde S/E |
| CUMPLE | SI | SI |  |

**Tabla 7.: Radio interferencia emitida por nuevos equipos****

| Col1 | Radio interferencia<br>[dB/uV/m] |
| --- | --- |
| Borde Subestación | 18,25 |
| A 15m del borde Subestación | 7,46 |
| Límite norma canadiense<br>(a 15m del borde subestación) | 43 |
| CUMPLE | SI |
