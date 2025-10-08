---
title: Sin título
author: Nicolas Pais
date: D:20240406072229-03'00'
language: es
type: report
pages: 26
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MEMORIA DE CÁLCULO HIDROLÓGICA CANAL DE CONTORNO BOSE
-->

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

## MANTOVERDE S.A. MODIFICACIÓN Y OPTIMIZACIÓN DE FAENA MINERA MANTOVERDE EN COMUNA DE CHAÑARAL Y TRANSPORTE DE CONCENTRADOS A PUERTOS DE ZONA DE MEJILLONES DOCUMENTO N° 1291-CAL-003

# MEMORIA DE CÁLCULO HIDROLÓGICA CANAL DE CONTORNO BOSE

_**Códice Ingeniería**_

Amapolas 1290, Oficina 808 APROB. CLIENTE: ____________

Providencia, Santiago FECHA: ____________

|REV.|FECHA|POR|REV.|APROB.|DESCRIPCION|
|---|---|---|---|---|---|
|A|Jun-2023|DCV|CPC|MPM|Coordinación Interna|
|B|Jun-2023|DCV|CPC|MPM|Para revisión del Cliente|
|0|Jun-2023|DCV|CPC|MPM|Incluye comentarios del Cliente|
|1|Abr-2024|DCV|MPM|MPM|Versión Final|

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

## MANTOVERDE S.A. MEMORIA DE CÁLCULO HIDROLÓGICA CANAL DE CONTORNO BOSE DOCUMENTO N° 1291-CAL-003 Contenido

1 INTRODUCCIÓN ........................................................................................................................ 4

2 OBJETIVO .................................................................................................................................. 5

3 ALCANCE ................................................................................................................................... 5

4 REFERENCIAS ............................................................................................................................ 6

5 ANTECEDENTES ......................................................................................................................... 7

5.1 CUENCAS APORTANTES .......................................................................................................... 7

5.2 PRECIPITACIONES MÁXIMAS .................................................................................................. 8

6 METODOLOGÍA DE TRABAJO .................................................................................................. 10

6.1 MÉTODOS DE CÁLCULO DE CAUDALES APORTANTES .......................................................... 10

6.1.1 Método Racional ......................................................................................................10

6.1.2 Método DGA-AC.......................................................................................................13

6.1.3 Método Verni y King Modificado .............................................................................14

6.2 FACTOR DE TRASPOSICIÓN .................................................................................................. 14

6.3 CAUDAL DETRÍTICO .............................................................................................................. 15

7 RESULTADOS ........................................................................................................................... 15

7.1 PRECIPITACIONES ZONA DE ESTUDIO .................................................................................. 15

7.1.1 Precipitaciones según periodo de retorno ..............................................................17

7.2 COEFICIENTES DE ESCORRENTÍA .......................................................................................... 17

7.3 CAUDALES POR SUBCUENCA ................................................................................................ 18

8 CONCLUSIONES Y COMENTARIOS .......................................................................................... 20

9 ANEXOS ................................................................................................................................... 21

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 2 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

## Tablas

Tabla 5-1 Datos de subcuencas canal de contorno BOSE (Ref. g) ............................................................ 8

Tabla 6-1 Coeficientes de amplificación de coeficientes de escorrentía (ver nota al final de Tabla 6-2)

................................................................................................................................................................ 10

Tabla 6-2 Factores del coeficiente de escorrentía (Ref. f) ..................................................................... 11

Tabla 6-3 Factor de transposición precipitaciones zona de estudio ...................................................... 14

Tabla 7-1 Parámetros utilizados distribución Gumbel para Estación Las Vegas .................................... 16

Tabla 7-2 Precipitaciones máximas anuales para periodos de retorno entre 2 y 200 años, Estación Las

Vegas y Zona de Estudio ......................................................................................................................... 17

Tabla 7-3 Coeficientes de escorrentía base ........................................................................................... 17

Tabla 7-4 Resumen resultados de caudales totales por periodo de retorno - Canal BOSE ................... 18

Tabla 7-5 Detalle de caudal de diseño detrítico por tramos de acuerdo con subcuencas .................... 19

Tabla 8-1 Caudales de diseño y verificación de descarga final - Canal de contorno BOSE ................... 20

Tabla 9-1 Precipitaciones máximas anuales de 24 horas de duración, Estación Las Vegas (Ref. l) y Zona

de Estudio (de acuerdo con factor de trasposición, ver Tabla 6-3) ....................................................... 21

Tabla 9-2 Coeficientes de Frecuencia (Ref. k) ........................................................................................ 22

Tabla 9-3 Coeficientes de Duración (Ref. k) ........................................................................................... 22

Tabla 9-4 Coeficientes empíricos - Método Verni y King Modificado (Ref. k) ....................................... 22

Tabla 9-5 Detalle de ajuste precipitaciones máximas Estación Las Vegas periodo 1990 a 2022 .......... 23

Tabla 9-6 Resultados caudales de diseño canal BOSE según distintos métodos ................................... 24

## Figuras

Figura 1-1 Emplazamiento proyectado anterior Canales de Contorno (Ref. c) ....................................... 4

Figura 1-2 Disposición actualizada botaderos BOMR, BONO y BOSE (Ref. d).......................................... 5

Figura 5-1 Subcuencas aportantes canal de contorno BOSE (Ref. g) ....................................................... 8

Figura 5-2 Ubicación Estación Las Vegas .................................................................................................. 9

Figura 5-3 Precipitaciones máximas anuales - Estación Las Vegas (Ref. l) ............................................... 9

Figura 6-1 Extrapolación de coeficientes de ampliación de coeficientes de escorrentía ...................... 11

Figura 7-1 Precipitaciones máximas anuales - Estación Las Vegas (Ref. l) y Mantoverde (según factor

trasposición) ........................................................................................................................................... 16

Figura 7-2 Distribución de probabilidades precipitaciones máximas anuales, 24 horas de duración ... 16

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 3 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

**1** **INTRODUCCIÓN**

Para darle continuidad al proceso de tratamiento de minerales de baja ley, _**Capstone Copper**_,
específicamente su faena Mantoverde, requiere realizar obras que permitan operar conforme a las
obligaciones establecidas para la ampliación de tres (3) botaderos de estéril, los cuales requieren contar
con obras de desvío y protección frente a escorrentías en los sectores donde se encuentran
emplazados, respectivamente.

Junto con lo anterior, se requiere ingresar a evaluación de impacto ambiental la DIA del proyecto
“Modificación y optimización de Faena Minera Mantoverde en comuna de Chañaral y transporte de
concentrados a puertos de zona de Mejillones”, dado el nuevo plan minero que incorpora nuevas fases
de operación, que obligan a la ampliación de los botaderos de estériles existentes (BOMR, BONO y
BOSE). Para efectos de impedir que las aguas que escurren por la cuenca entren en contacto con estas
obras, el proyecto considera la construcción de canales de contorno para desvío de aguas lluvias, los
que deben ser diseñados y sometidos a aprobación por parte de la Autoridad Ambiental.

_**Capstone Copper**_ solicita a Códice Ingeniería ( _**Códice**_ ) el desarrollo del diseño y la documentación
técnica necesaria para presentar los antecedentes requeridos por la legislación vigente para la
obtención de los Permisos Ambientales Sectoriales (PAS 155 y/o PAS 156) asociados a los canales de
contorno BOMR, BONO y BOSE, de acuerdo con la disposición actualizada de los botaderos del mismo

nombre.

Se consideran los tres (3) canales de contorno proyectados destacados en la Figura 1-1, los cuales se

denominan de la siguiente forma:

 - Canal BOMR, asociado al sector este de la ampliación del botadero Manto Ruso (BOMR).

 - Canal BONO, asociado al sector sureste de la ampliación del botadero Norte (BONO).

 - Canal BOSE, asociado al sector este de la ampliación del botadero Sur Este (BOSE).

_Figura 1-1 Emplazamiento proyectado anterior Canales de Contorno (Ref. c)_

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 4 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

En la Figura 1-1 se muestran los emplazamientos de los canales de contorno BOMR, BONO y BOSE, ya

aprobados, los que son ajustados mediante el diseño a desarrollar de acuerdo con la nueva disposición

de los botaderos. En la Figura 1-2, se presenta las envolventes finales de los botaderos considerados

en el proyecto “Modificación y optimización de Faena Minera Mantoverde en comuna de Chañaral y

transporte de concentrados a puertos de zona de Mejillones”.

_Figura 1-2 Disposición actualizada botaderos BOMR, BONO y BOSE (Ref. d)_

**2** **OBJETIVO**

Este documento tiene por objetivo presentar el detalle de los antecedentes, consideraciones, criterios

y cálculos hidrológicos para determinar los caudales de diseño y verificación asociados al canal de

contorno del botadero BOSE.

**3** **ALCANCE**

El alcance comprende determinar los flujos estimados para los canales a proyectar a partir de los

métodos planteados por la DGA, y siguiendo las indicaciones de las Guías Metodológicas para

Presentación y Revisión Técnica de Proyectos de Modificación de Cauces Naturales y Artificiales (Ref.

e), para lo cual se consideran los siguientes aspectos:

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 5 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

 - Delimitación de cuencas y subcuencas aportantes, junto con su caracterización.

 - Estimación de precipitaciones de diseño.

`o` Incluye la actualización de registro de precipitaciones máximas y trasposición desde la

estación meteorológica de la DGA cercana (Estación Las Vegas).

 - Estimación de los caudales aportantes según los métodos planteados en el Manual de

Carreteras (Ref. f).

**4** **REFERENCIAS**

a 1291-DWG-003. Planos Áreas a Intervenir (Planos Topográficos) - Canal de Contorno BOSE.
Códice Ingeniería, 2023.

b Manual de Carreteras Vol. 2 “Procedimientos de Estudios Viales”. Ministerio de Obras Públicas

(MOP), 2021.

c PLT-G-01-Rev0. Plano Planta General Obras Proyectadas. 3A Consultores, 2017.

d Archivo “int_botaderos_2023.dxf”. Disposición huellas actualizadas botaderos BOMR, BONO y

BOSE. Mantoverde, 2023.

e Guías Metodológicas para Presentación y Revisión Técnica de Proyectos de Modificación de
Cauces Naturales y Artificiales. DGA, 2016.

f Manual de carreteras. Volumen N°3. Instrucciones y criterios de diseño. Dirección de Vialidad,

Ministerio de Obras Públicas. Edición 2019.

g 1291-DWG-006. Plano áreas aportantes (plano subcuencas). Canal de Contorno BOSE - Planta.
Códice Ingeniería, 2023.

h Balance Hídrico de Chile. DGA, 1987.

i Actualización del Balance Hídrico Nacional. DGA, 2017.

j Precipitaciones máximas en 1, 2 y 3 días. Dirección General de Aguas. DGA, 1995.

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 6 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

k Manual de cálculo de crecidas y caudales mínimos en cuencas sin información fluviométrica.
Dirección General de Aguas, 1995.

l [Estadística hidrológica en línea, DGA. (https://snia.mop.gob.cl/BNAConsultas/reportes).](https://snia.mop.gob.cl/BNAConsultas/reportes)

m Synthetic Unit Hydrographs for Small Watersheds. D.M. Gray, 1961.

n Hidrología Aplicada. Ven Te Chow, 1994.

o Caracterización y levantamiento de información debido a las crecidas aluvionales en la cuenca
del Río Copiapó, Región de Atacama para el temporal del 25 y 26 de marzo de 2015. Informe
Final - Volumen 1 de 9. Dirección Obras Hidráulicas (DOH), 2015.

**5** **ANTECEDENTES**

**5.1** **CUENCAS APORTANTES**

Para definir las subcuencas aportantes a cada canal, se realizó un análisis de la topografía (Ref. a),

identificándose las líneas divisorias de aguas de cada cuenca con el fin de determinar la totalidad de las

áreas que aportan a cada obra de evacuación de aguas lluvias. Además, se obtuvieron otros parámetros

geomorfológicos de las cuencas, como las elevaciones máximas y mínimas, pendiente, largo del cauce

principal y los coeficientes de escorrentía para 10 años de periodo de retorno.

Notar que los canales de contorno a ser diseñados consideran la disposición final de los botaderos, por

lo que se debe disponer de un sistema de protección local para proteger las etapas iniciales hasta la

disposición del botadero en el área basal final. Es por lo anterior que las áreas aportantes consideradas

se asocian a las huellas finales de los botaderos.

El detalle de las subcuencas aportantes al canal BOSE se muestran en la Figura 5-1, mientras que los

datos de cada una de las subcuencas se muestran en la Tabla 5-1.

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 7 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

_Figura 5-1 Subcuencas aportantes canal de contorno BOSE (Ref. g)_

_Tabla 5-1 Datos de subcuencas canal de contorno BOSE (Ref. g)_

|Cuenca|1|2|3|4|5|6|7|8|9|
|---|---|---|---|---|---|---|---|---|---|
|Área (km2)|0,074|0,061|0,146|0,127|0,181|0,118|0,278|0,138|0,079|
|Cota máxima (msnm)|1.227|1.196|1.217|1.174|1.197|1.272|1.248|1.267|1.183|
|Cota mínima (msnm)|1.110|1.110|1.110|1.110|1.110|1.110|1.110|1.110|1.110|
|Dist. Cauce (m)|272|197|331|229|253|458|302|417|162|
|Pendiente (%)|43%|44%|32%|28%|34%|35%|46%|38%|45%|

**5.2** **PRECIPITACIONES MÁXIMAS**

Para la estimación de caudales de las subcuencas asociados a los distintos periodos de retorno se

utilizan los datos de la precipitación máxima anual de 24 horas de duración de la Estación Las Vegas de

la DGA (ver Figura 5-2) entre los años 1990 a 2022 (Ref. l), la cual es la estación más cercana que

presenta el registro de datos completo desde el año 1990.

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 8 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

Estos datos permitirán la extrapolación del registro de precipitaciones hacia el sector de interés en la

faena Mantoverde y posteriormente la determinación de los caudales asociados frente a la ocurrencia

de distintos eventos de precipitaciones, de acuerdo con la metodología presentada en la sección 6.2 y

6.1, respectivamente.

_Figura 5-2 Ubicación Estación Las Vegas_

En la Figura 5-3 se presentan las precipitaciones máximas anuales asociadas a la Estación Las Vegas

(Ref. l), cuyo detalle se presenta en la Tabla 9-1 (ver sección 9 Anexos).

_Figura 5-3 Precipitaciones máximas anuales - Estación Las Vegas (Ref. l)_

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 9 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

**6** **METODOLOGÍA DE TRABAJO**

**6.1** **MÉTODOS DE CÁLCULO DE CAUDALES APORTANTES**

Para el cálculo de los caudales aportantes a cada uno de los canales, se siguieron las indicaciones del

Manual de Carreteras Volumen 3 (Ref. f). Para determinar el caudal aportante se consideran los

métodos propuestos por la DGA (Ref. k): Método Racional, Método DGA-AC y Método Verni y King

Modificado.

Notar que no se considera en el análisis el Hidrograma Unitario Sintético (HUS) de Gray, el cual es

recomendado por el Manual de cálculo de crecidas de la DGA (Ref. k) para cuencas ubicadas entre la

III [a] y X [a] Región de Chile. Sin embargo, su campo de aplicación abarca cuencas entre 10 y 4.500 km [2], lo

cual no es el caso de las subcuencas analizadas.

**6.1.1** **Método Racional**

El método racional considera la siguiente ecuación:

Q= [C∙i∙A]

3,6

Donde:

Q : Caudal aportante (m [3] /s)
C : Coeficiente de escorrentía

i : Intensidad de precipitación (mm/hr)
A : Área subcuenca aportante (km [2] )

Para el cálculo del coeficiente de escorrentía, se consideran los valores asociados a relieve, infiltración,

cobertura natural y almacenamiento superficial presentados en la Tabla 6-2. Estos coeficientes se

suman y se multiplican por el factor de ajuste para los distintos periodos de retorno de acuerdo con lo

indicado en la Tabla 6-1.

_Tabla 6-1 Coeficientes de amplificación de coeficientes de escorrentía (ver nota al final de Tabla 6-2)_

|Periodo de retorno (T)|Años|2|5|10|25|50|100|200|
|---|---|---|---|---|---|---|---|---|
|**Coef. amplificación de coef. escorrentía**|**Adimensional**|1,0|1,0|1,0|1,1|1,2|1,25|1,3381|

1 Se determina el coeficiente de amplificación asociado a los 200 años de periodo de retorno de acuerdo con el ajuste logarítmico

de la función presentada en la Figura 6-1.

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 10 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

_Figura 6-1 Extrapolación de coeficientes de ampliación de coeficientes de escorrentía_

_Tabla 6-2 Factores del coeficiente de escorrentía (Ref. f)_

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 11 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

En cuanto a la intensidad, se determina mediante la siguiente ecuación:

T

[24] ∙CD Tc

i= K∙ [P] [24]

Tc

Donde:

i : Intensidad de precipitación en tiempo de concentración (mm/hr).
K : Coeficiente de corrección para la lluvia máxima medida entre 8 am y 8 am respecto a las

24 horas más lluviosas de la tormenta, para el que se adopta el valor de 1,1 (Ref. k).
P 24T : Precipitación máxima diaria (24 hrs) asociada a un periodo de retorno T (mm) (Ref. k).

CD Tc : Coeficiente de duración relativo al tiempo de concentración (Ref. k), ver Tabla 9-3. Se

extrapola el valor asociado a la duración de la lluvia de diseño según el tiempo de
concentración, para lo que se ajusta una curva a los datos presentados.
Tc : Tiempo de concentración de subcuenca aportante (hr).

Para el cálculo del tiempo de concentración se considera el mayor valor entre 10 minutos (mínimo

admitido para el diseño (Ref. k)) y los resultados de los dos (2) métodos siguientes:

 - Método California Culvers Practice, Kirpich (CCPK)

d [3]
Tc CCPK
= 0,95 ∙(z max −z min

0,385

)

Donde:

Tc CCPK : Tiempo de concentración según el método California Culvers Practice, Kirpich (hr).

d : Distancia que recorrer por el cauce (km).
z max : Cota máxima de la subcuenca (m.s.n.m.).
z min : Cota mínima de la subcuenca (m.s.n.m.).

 - Norma Española

Tc NE = 18 ∙ [d] i [0,19][0,76]

Donde:

Tc NE : Tiempo de concentración según el método de la Norma Española (min).

d : Distancia que recorrer por el cauce (km).
i : Pendiente media del cauce (m/m).

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 12 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

**6.1.2** **Método DGA-AC**

La relación para el cálculo del caudal medio diario máximo del período de retorno asociado a 10 años,

utilizada para adimensionalizar las curvas de frecuencia regionales del método DGA-AC, lo que depende

de la región donde se ubica la subcuenca analizada, se presenta a continuación:

10 [3,108]

24 ∙A p

Q 10 = 1,94 ∙10 [−7] ∙P 2410 ∙A p0,776

Donde:

Q 10 = 1,94 ∙10 [−7] ∙P 2410

Q 10 : Caudal máximo diario asociado al período de retorno 10 años (m [3] /s).
P 2410 : Precipitación diaria máxima asociada al período de retorno 10 años (mm).

A p : Área pluvial de la subcuenca aportante (km [2] ).

Para la transformación del caudal asociado a un período de retorno de 10 años al caudal de 100 años,

se utiliza el coeficiente de frecuencia presentado en la Tabla 9-2 (Ref. k). Para hacer esta transformación

se utiliza la siguiente ecuación:

Q 100 = CF [100] ∙Q 10

Donde:

Q 100 : Caudal máximo diario asociado al período de retorno 100 años (m [3] /s).
CF [100] : Coeficiente de frecuencia asociado a la zona de estudio para la conversión del caudal

máximo de 10 a 100 años de período de retorno.
Q 10 : Caudal máximo asociado al período de retorno 10 años (m [3] /s).

Finalmente, se obtiene el caudal máximo instantáneo mediante la siguiente ecuación:

Q= C [máx] ∙Q 100

Donde:

Q : Caudal máximo instantáneo asociado al período de retorno 100 años (m [3] /s).
C [máx] : Coeficiente de transformación a caudal instantáneo máximo.

Q 100 : Caudal diario asociado al período de retorno 100 años (m [3] /s).

Para el caso analizado, el valor adoptado para C [máx] = 3,07 (Ref. k).

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 13 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

**6.1.3** **Método Verni y King Modificado**

La fórmula de Verni y King Modificada tiene la siguiente forma:

Q= C(T) ∙0,00618 ∙P 241,24 ∙A p0,88

Donde:

Q= C(T) ∙0,00618 ∙P 24

1,24 ∙A
p

Q : Caudal máximo instantáneo asociado al período de retorno T años (m [3] /s).
C(T) : Coeficiente empírico de período de retorno T años (ver Tabla 9-4).

P 24 : Precipitación diaria máxima asociada al período de retorno T años (mm).
A p : Área pluvial de la subcuenca aportante (km [2] ).

**6.2** **FACTOR DE TRASPOSICIÓN**

Para la determinación de las precipitaciones esperadas en el sector de interés (faena Mantoverde) se

deben extrapolar los datos históricos desde la Estación Las Vegas mediante la trasposición de datos.

Para realizar la trasposición de precipitaciones máximas anuales se determina un factor de trasposición

que permite estimar la relación entre los datos medidos en la Estación Las Vegas y los esperados. Este

factor se determina de acuerdo con la media de los distintos modelos de precipitaciones según las

zonas estudiadas (ver Tabla 6-3), a partir de los cuales se considera un factor de transposición promedio

de 0,5767.

_Tabla 6-3 Factor de transposición precipitaciones zona de estudio_

|Método|Lugar|Precipitación<br>(mm)|Factor de<br>Trasposición|
|---|---|---|---|
|Balance Hídrico de Chile (Pp media anual)<br>(Ref. h)|Las Vegas|22,9|0,6|
|Balance Hídrico de Chile (Pp media anual)<br>(Ref. h)|Zona de Estudio|13,8|13,8|
|Actualización Balance Hídrico Nacional (Pp<br>media anual) (Ref. i)|Las Vegas|26,2|0,54|
|Actualización Balance Hídrico Nacional (Pp<br>media anual) (Ref. i)|Zona de Estudio|14,4|14,4|
|Precipitaciones máximas para 1, 2 y 3 días (Pp<br>máxima en 24 horas para T = 10 años) (Ref. j)|Las Vegas|34,1|0,59|
|Precipitaciones máximas para 1, 2 y 3 días (Pp<br>máxima en 24 horas para T = 10 años) (Ref. j)|Zona de Estudio|20,0|20,0|
|**Promedio**|**Promedio**|**Promedio**|**0,5767**|

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 14 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

**6.3** **CAUDAL DETRÍTICO**

Una vez realizados los cálculos del caudal líquido asociado a cada cuenca y cada periodo de retorno

analizados (2, 5, 10, 25, 50, 100 y 200 años), se realiza el cálculo del caudal detrítico. Según lo descrito

en el documento “Guías metodológicas para presentación y revisión de proyectos de modificación de

cauces naturales y artificiales” (Ref. e), se solicita incorporar el caudal de detritos que podría

presentarse en las diferentes cuencas aportantes. Se utiliza la siguiente expresión para obtener el flujo

de detritos:

Q detritos = [Q] (1 −C) [lí][q][uido]

Donde:

Q detritos : Caudal detrítico (suma del caudal sólido más caudal líquido) (m [3] /s)

Q líquido : Caudal líquido (m [3] /s)
C : Concentración en volumen de sólidos

En los eventos de marzo de 2015, de los mayores registrados en la zona, se ha estimado una
concentración volumétrica máxima del torrente de un 16% (Ref. o). Tomando en cuenta eso y basado
en la recomendación de DGA (Ref. e) se adopta un valor conservador de C = 30% para la concentración

en volumen de sólidos.

En base a los resultados, se escoge el caudal de mayor cuantía para definir el caudal de diseño para

cada uno de los canales, de tal manera de ser conservador en el diseño de los canales.

**7** **RESULTADOS**

**7.1** **PRECIPITACIONES ZONA DE ESTUDIO**

A partir de las precipitaciones máximas anuales registradas en la Estación Las Vegas, y utilizando el

factor de transposición determinado, de 0,5767 (ver Tabla 6-3), se obtiene un valor representativo de

precipitaciones para la zona de estudio, lo cual se muestra en la Figura 7-1 y se detalla en la Tabla 9-1

(ver sección 9 Anexos).

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 15 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

_Figura 7-1 Precipitaciones máximas anuales - Estación Las Vegas (Ref. l) y Mantoverde (según factor trasposición)_

Con los datos de precipitación máxima, se ordenaron los datos en orden decreciente para obtener una

distribución Weibull (ver anexo A.5 con detalles). Una vez realizado esto, se ajusta una distribución

Gumbel, la cual es la que mejor ajusta a los datos recopilados. En la Figura 7-2 se muestran ambas

distribuciones y en la Tabla 7-1 se muestran los parámetros utilizados para el cálculo de la distribución

Gumbel.

_Tabla 7-1 Parámetros utilizados distribución_

_Gumbel para Estación Las Vegas_

_Figura 7-2 Distribución de probabilidades precipitaciones máximas_

_anuales, 24 horas de duración_

|Desviación Estándar|12,902|
|---|---|
|**Sx (N=33)**|1,122|
||11,499|
|**Media**|14,658|
|**yn (N=33)**|0,539|
||8,464|
|**N° Datos**|33|

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 16 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

**7.1.1** **Precipitaciones según periodo de retorno**

En la Tabla 7-2 se muestran los resultados del ajuste de precipitaciones máximas anuales para periodos

de retorno entre 2 y 200 años, tanto para la estación Las Vegas, como para la zona de estudio que

corresponde a la zona de Mantoverde.

_Tabla 7-2 Precipitaciones máximas anuales para periodos de retorno entre 2 y 200 años, Estación Las Vegas y Zona de_

_Estudio_

|Periodo de Retorno|Precipitaciones|Col3|
|---|---|---|
|**T (años)**|**Las Vegas (mm)**|**Zona de Estudio (mm)**|
|200|69,4|40,0|
|100|61,4|35,4|
|50|53,3|30,8|
|25|45,2|26,1|
|10|34,3|19,8|
|5|25,7|14,8|
|2|12,7|7,3|

**7.2** **COEFICIENTES DE ESCORRENTÍA**

A partir del estudio de las consideraciones presentadas en el Manual de Carreteras (ver Tabla 6-2, Ref.

f) y las características del sector estudiado se determinan los coeficientes de escorrentía para cada

subcuenca.

Para lo anterior se consideran estas subcuencas como:

 Suelos arcillosos o limosos con baja capacidad de infiltración, mal drenados.

 Cobertura escasa, terreno sin vegetación o escasa cobertura.

 Almacenamiento superficial bajo, sistema de cauces superficiales pequeños bien definidos, sin

zonas húmedas.

Lo anterior, combinado con las pendientes del terreno asociadas a cada subcuenca permiten estimar

los siguientes coeficientes de escorrentía base, los que deben ser amplificados de acuerdo con lo

presentado en la Tabla 6-1.

_Tabla 7-3 Coeficientes de escorrentía base_

|Subcuenca|1|2|3|4|5|6|7|8|9|
|---|---|---|---|---|---|---|---|---|---|
|**Coef. Escorrentía Base**|0,59|0,59|0,56|0,55|0,56|0,57|0,59|0,58|0,59|

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 17 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

**7.3** **CAUDALES POR SUBCUENCA**

Considerando a que el área aportante al canal BOSE es menor a 20 km [2], se aceptan como válidos los

siguientes métodos: Racional, DGA-AC y Verni y King Modificado.

En la Tabla 7-4 se muestran los resultados de los caudales líquidos para cada método (Racional (ver

sección 6.1.1), DGA-AC (ver sección 6.1.2) y Verni y King Modificado (ver sección 6.1.3)). Asimismo, se

presenta el caudal liquido de diseño, que se considera el máximo entre los tres (3) métodos planteados

por la DGA (Ref. k), y, finalmente, se incorpora el componente detrítico, de acuerdo con lo indicado en

la sección 6.3, de tal manera de disponer de los caudales para el desarrollo de las modelaciones y

cálculos de hidráulica fluvial.

_Tabla 7-4 Resumen resultados de caudales totales por periodo de retorno - Canal BOSE_

|Periodo de<br>Retorno|Caudal según método|Col3|Col4|Caudal<br>Líquido de<br>Diseño|Caudal<br>Detrítico de<br>Diseño|
|---|---|---|---|---|---|
|**Periodo de**<br>**Retorno**|**Racional**|**DGA - AC**|**Verni y King**<br>**Modificado**|**Verni y King**<br>**Modificado**|**Verni y King**<br>**Modificado**|
|**Años**|**m3/s**|**m3/s**|**m3/s**|**m3/s**|**m3/s**|
|2|0,762|0,007|0,003|0,762|1,088|
|5|1,545|0,010|0,007|1,545|2,207|
|10|2,063|0,012|0,010|2,063|2,948|
|25|2,990|0,013|0,016|2,990|4,272|
|50|3,845|0,015|0,022|3,845|5,493|
|100|4,609|0,016|0,028|4,609|6,584|
|200|5,576|0,018|0,034|5,576|7,966|

Notar que los métodos DGA-AC y Verni-King Modificado no permiten estimar correctamente la
escorrentía esperada para el sector de análisis, debido a que no consideran las características
específicas del sector (sector árido de pendientes fuertes con mala infiltración).

Por otra parte, notar que lo indicado en la Tabla 7-4 considera los caudales totales asociados a la suma
de los caudales de las distintas subcuencas aportantes, con lo que se determina el método que permite
estimar el caudal de diseño (Método Racional).

A partir de lo anterior, se desglosan los caudales detríticos para cada tramo del canal a diseñar, de
acuerdo con la separación por subcuencas, lo cual se detalla en la Tabla 7-5, indicando los caudales
detríticos por subcuenca y el acumulado a medida que descarguen en el canal a ser proyectado.

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 18 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

_Tabla 7-5 Detalle de caudal de diseño detrítico por tramos de acuerdo con subcuencas_

|Periodo de<br>retorno|Caudal|Subcuencas|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Años**|**m3/s**|**1 **|**2 **|**3 **|**4 **|**5 **|**6 **|**7 **|**8 **|**9 **|
|**2 **|**Subcuenca**|0,070|0,058|0,132|0,112|0,163|0,094|0,265|0,119|0,075|
|**2 **|**Acumulado**|0,070|0,128|0,260|0,373|0,536|0,630|0,895|1,013|1,088|
|**5 **|**Subcuenca**|0,143|0,117|0,268|0,228|0,331|0,190|0,537|0,241|0,152|
|**5 **|**Acumulado**|0,143|0,260|0,528|0,756|1,087|1,278|1,814|2,055|2,207|
|**10**|**Subcuenca**|0,191|0,156|0,358|0,304|0,443|0,254|0,717|0,322|0,203|
|**10**|**Acumulado**|0,191|0,347|0,705|1,009|1,452|1,706|2,423|2,745|2,948|
|**25**|**Subcuenca**|0,277|0,227|0,518|0,441|0,642|0,369|1,039|0,466|0,294|
|**25**|**Acumulado**|0,277|0,503|1,022|1,463|2,104|2,473|3,512|3,978|4,272|
|**50**|**Subcuenca**|0,356|0,291|0,667|0,567|0,825|0,474|1,336|0,599|0,378|
|**50**|**Acumulado**|0,356|0,647|1,314|1,881|2,706|3,180|4,516|5,115|5,493|
|**100**|**Subcuenca**|0,426|0,349|0,799|0,680|0,989|0,568|1,601|0,718|0,453|
|**100**|**Acumulado**|0,426|0,776|1,575|2,254|3,243|3,811|5,412|6,130|6,584|
|**200**|**Subcuenca**|0,516|0,423|0,967|0,822|1,196|0,687|1,937|0,869|0,549|
|**200**|**Acumulado**|0,516|0,939|1,905|2,728|3,924|4,611|6,548|7,417|7,966|

En el Anexo A.6 se muestra el detalle de los cálculos para cada una de las subcuencas aportantes al

canal BOSE.

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 19 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

**8** **CONCLUSIONES Y COMENTARIOS**

Para la estimación de los caudales se utilizaron los datos de la precipitación máxima anual de 24 horas

de duración de la Estación Las Vegas (DGA) entre los años 1990 a 2022, los que fueron transpuestos al

área de estudio (ver Tabla 7-2).

Para determinar el caudal aportante se consideran los métodos propuestos por la DGA (Ref. e): Método

Racional, Método DGA-AC y Método Verni & King Modificado, según la aplicabilidad a cada una de las

cuencas.

Debido a que el área aportante a los canales BOMR, BONO y BOSE son menores a 20 km [2], se aceptan

como válidos y se utilizan los siguientes métodos: Racional, DGA-AC y Verni y King Modificado.

Sin embargo, los métodos DGA-AC y Verni-King Modificado no permiten estimar correctamente la

escorrentía esperada para el sector de análisis, debido a que las características específicas del sector

analizado no son capturadas por esos modelos. Es por lo anterior que se consideran los caudales

asociados al método Racional, el cual es el de uso más extendido para cuencas de menor tamaño.

En base a lo presentado en este documento, se determinaron los caudales de diseño y de verificación,

que corresponden al caudal detrítico total calculado para un periodo de retorno de 100 y 200 años,

respectivamente, los cuales se presentan en la Tabla 8-1.

_Tabla 8-1 Caudales de diseño y verificación de descarga final - Canal de contorno BOSE_

|Canal|Caudal de Diseño (m3/s)|Caudal de Verificación (m3/s)|
|---|---|---|
|**Canal**|**m3/s**|**m3/s**|
|BOSE|6,584|7,966|

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 20 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

**9** **ANEXOS**

A.1.Precipitaciones máximas anuales de 24 horas de duración

_Tabla 9-1 Precipitaciones máximas anuales de 24 horas de duración, Estación Las Vegas (Ref. l) y Zona de Estudio (de_

_acuerdo con factor de trasposición, ver Tabla 6-3)_

|Año|Fecha|Estación Las Vegas (mm)|Zona Estudio (mm)|
|---|---|---|---|
|1990|07/07|2,0|1,2|
|1991|17/06|44,0|25,4|
|1992|27/05|12,5|7,2|
|1993|11/08|11,5|6,6|
|1994|27/02|2,0|1,2|
|1995|18/05|22,0|12,7|
|1996|30/08|9,0|5,2|
|1997|17/08|40,0|23,1|
|1998|09/06|7,0|4,0|
|1999|27/06|17,0|9,8|
|2000|14/05|29,0|16,7|
|2001|21/03|0,5|0,3|
|2002|01/07|12,0|6,9|
|2003|01/01|0,0|0,0|
|2004|27/07|15,0|8,7|
|2005|15/07|9,0|5,2|
|2006|29/08|16,0|9,2|
|2007|01/01|0,0|0,0|
|2008|04/09|13,0|7,5|
|2009|20/07|17,0|9,8|
|2010|16/05|22,0|12,7|
|2011|07/07|21,0|12,1|
|2012|13/04|4,1|2,4|
|2013|13/06|8,2|4,7|
|2014|22/05|22,0|12,7|
|2015|24/03|33,4|19,3|
|2016|25/06|14,0|8,1|
|2017|11/05|41,0|23,6|
|2018|01/01|0,0|0,0|
|2019|09/09|0,3|0,2|
|2020|28/01|34,3|19,8|
|2021|15/06|1,5|0,9|
|2022|05/06|3,4|2,0|

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 21 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

A.2.Coeficientes de Frecuencia según período de retorno (CF [T] )

_Tabla 9-2 Coeficientes de Frecuencia (Ref. k)_

|Período de retorno (T) en años|Coeficiente de frecuencia (CFT)|
|---|---|
|2|0,584|
|5|0,854|
|10|1,000|
|20|1,124|
|50|1,266|
|100|1,363|

A.3.Coeficientes de duración según duración de la lluvia de diseño (CDt)

_Tabla 9-3 Coeficientes de Duración (Ref. k)_

|Duración de lluvia de diseño (t) en horas|Coeficiente de duración (CDt)|
|---|---|
|1|0,168|
|2|0,321|
|3|0,461|
|6|0,743|
|12|0,964|
|24|1,000|

A.4. Coeficientes empíricos según período de (C(T))

_Tabla 9-4 Coeficientes empíricos - Método Verni y King Modificado (Ref. k)_

|Período de retorno (T) en años|Coeficiente empírico (C(T))|
|---|---|
|2|0,0243|
|5|0,02565|
|10|0,027|
|20|0,0297|
|25|0,03078|
|50|0,03321|
|100|0,03564|

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 22 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

A.5.Ajuste distribución de probabilidades Estación Las Vegas

_Tabla 9-5 Detalle de ajuste precipitaciones máximas Estación Las Vegas periodo 1990 a 2022_

|Año|Fecha|DGA|Weibull|N°|P>x|F(x)|Gumbel|Test de Bondad|
|---|---|---|---|---|---|---|---|---|
|1990|07/07|2,0|44,0|1|0,029|0,971|48,84|0,48|
|1991|17/06|44,0|41,0|2|0,059|0,941|40,69|0,00|
|1992|27/05|12,5|40,0|3|0,088|0,912|35,85|0,48|
|1993|11/08|11,5|34,3|4|0,118|0,882|32,36|0,12|
|1994|27/02|2,0|33,4|5|0,147|0,853|29,60|0,49|
|1995|18/05|22,0|29,0|6|0,176|0,824|27,31|0,10|
|1996|30/08|9,0|22,0|7|0,206|0,794|25,34|0,44|
|1997|17/08|40,0|22,0|8|0,235|0,765|23,59|0,11|
|1998|09/06|7,0|22,0|9|0,265|0,735|22,02|0,00|
|1999|27/06|17,0|21,0|10|0,294|0,706|20,59|0,01|
|2000|14/05|29,0|17,0|11|0,324|0,676|19,27|0,27|
|2001|21/03|0,5|17,0|12|0,353|0,647|18,03|0,06|
|2002|01/07|12,0|16,0|13|0,382|0,618|16,86|0,04|
|2003|01/01|0,0|15,0|14|0,412|0,588|15,75|0,04|
|2004|27/07|15,0|14,0|15|0,441|0,559|14,69|0,03|
|2005|15/07|9,0|13,0|16|0,471|0,529|13,67|0,03|
|2006|29/08|16,0|12,5|17|0,500|0,500|12,68|0,00|
|2007|01/01|0,0|12,0|18|0,529|0,471|11,71|0,01|
|2008|04/09|13,0|11,5|19|0,559|0,441|10,77|0,05|
|2009|20/07|17,0|9,0|20|0,588|0,412|9,84|0,07|
|2010|16/05|22,0|9,0|21|0,618|0,382|8,92|0,00|
|2011|07/07|21,0|8,2|22|0,647|0,353|8,00|0,01|
|2012|13/04|4,1|7,0|23|0,676|0,324|7,07|0,00|
|2013|13/06|8,2|4,1|24|0,706|0,294|6,14|0,68|
|2014|22/05|22,0|3,4|25|0,735|0,265|5,19|0,62|
|2015|24/03|33,4|2,0|26|0,765|0,235|4,22|1,16|
|2016|25/06|14,0|2,0|27|0,794|0,206|3,20|0,45|
|2017|11/05|41,0|1,5|28|0,824|0,176|2,13|0,19|
|2018|01/01|0,0|0,5|29|0,853|0,147|0,98|0,24|
|2019|09/09|0,3|0,3|30|0,882|0,118|-0,28|-1,20|
|2020|28/01|34,3|0,0|31|0,912|0,088|-1,74|-1,74|
|2021|15/06|1,5|0,0|32|0,941|0,059|-3,51|-3,51|
|2022|05/06|3,4|0,0|33|0,971|0,029|-6,03|-6,03|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|Test Chi|0,999995377|

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 23 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

A.6.Resultado caudal de diseño canal BOSE.

_Tabla 9-6 Resultados caudales de diseño canal BOSE según distintos métodos_

|Cuenca|Col2|Canal|Canal BOSE|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Cuenca**|**Cuenca**|**Subcuenca**|**1 **|**2 **|**3 **|**4 **|**5 **|**6 **|**7 **|**8 **|**9 **|
|**Área**|**Área**|**m2**|74.000|60.610|146.079|126.519|180.786|117.508|277.798|137.526|78.675|
|**Área**|**Área**|**km2**|0,0740|0,0606|0,1461|0,1265|0,1808|0,1175|0,2778|0,1375|0,0787|
|**Cota Mínima**|**Cota Mínima**|**msnm**|1.110|1.110|1.110|1.110|1.110|1.110|1.110|1.110|1.110|
|**Cota Máxima**|**Cota Máxima**|**msnm**|1.227|1.196|1.217|1.174|1.197|1.272|1.248|1.267|1.183|
|**Distancia**|**Distancia**|**m **|272|197|331|229|253|458|302|417|162|
|**Distancia**|**Distancia**|**km**|0,272|0,197|0,331|0,229|0,253|0,458|0,302|0,417|0,162|
|**Factor conversión alfa**|**Factor conversión alfa**|**- **|3,07|3,07|3,07|3,07|3,07|3,07|3,07|3,07|3,07|
|**Coef, Escorrentía**|**Coef, Escorrentía**|**- **|0,59|0,59|0,56|0,55|0,56|0,57|0,59|0,58|0,59|
|**Pendiente**|**Cauce**|**m/m**|43%|44%|32%|28%|34%|35%|46%|38%|45%|
|**Tiempo de Concentración**|**CCPK**|**min**|2,030|1,567|2,636|2,095|2,097|3,259|2,147|2,964|1,334|
|**Tiempo de Concentración**|**CCPK**|**hr**|0,0338|0,0261|0,0439|0,0349|0,0349|0,0543|0,0358|0,0494|0,0222|
|**Tiempo de Concentración**|**Norma Española**|**min**|7,864|6,122|9,638|7,481|7,773|12,108|8,413|11,150|5,249|
|**Tiempo de Concentración**|**Norma Española**|**hr**|0,1311|0,1020|0,1606|0,1247|0,1295|0,2018|0,1402|0,1858|0,0875|
|**Tiempo de Concentración**|**Promedio**|**min**|4,947|3,844|6,137|4,788|4,935|7,684|5,280|7,057|3,291|
|**Tiempo de Concentración**|**Promedio**|**hr**|0,0825|0,0641|0,1023|0,0798|0,0822|0,1281|0,0880|0,1176|0,0549|
|**Tiempo de Concentración**|**Máximo**|**min**|7,864|6,122|9,638|7,481|7,773|12,108|8,413|11,150|5,249|
|**Tiempo de Concentración**|**Máximo**|**hr**|0,1311|0,1020|0,1606|0,1247|0,1295|0,2018|0,1402|0,1858|0,0875|
|**Tiempo de Concentración**|**Diseño**|**min**|10,000|10,000|10,000|10,000|10,000|12,108|10,000|11,150|10,000|
|**Tiempo de Concentración**|**Diseño**|**hr**|0,1667|0,1667|0,1667|0,1667|0,1667|0,2018|0,1667|0,1858|0,1667|
|**Método Racional**|**Coeficiente de corrección (K)**|**- **|1,1|1,1|1,1|1,1|1,1|1,1|1,1|1,1|1,1|
|**Método Racional**|**Coef, Duración**|**- **|0,084|0,084|0,084|0,084|0,084|0,089|0,084|0,087|0,084|
|**Método Racional**|**Intensidad - 2 años**|**mm/hr**|4,069|4,069|4,069|4,069|4,069|3,532|4,069|3,751|4,069|
|**Método Racional**|**Intensidad - 5 años**|**mm/hr**|8,251|8,251|8,251|8,251|8,251|7,163|8,251|7,607|8,251|
|**Método Racional**|**Intensidad - 10 años**|**mm/hr**|11,020|11,020|11,020|11,020|11,020|9,568|11,020|10,160|11,020|
|**Método Racional**|**Intensidad - 25 años**|**mm/hr**|14,519|14,519|14,519|14,519|14,519|12,605|14,519|13,385|14,519|
|**Método Racional**|**Intensidad - 50 años**|**mm/hr**|17,114|17,114|17,114|17,114|17,114|14,859|17,114|15,778|17,114|
|**Método Racional**|**Intensidad - 100 años**|**mm/hr**|19,691|19,691|19,691|19,691|19,691|17,096|19,691|18,153|19,691|
|**Método Racional**|**Intensidad - 200 años**|**mm/hr**|22,258|22,258|22,258|22,258|22,258|19,324|22,258|20,520|22,258|
|**Método Racional**|**Coef, Escorrentía - 2 años**|**- **|0,590|0,590|0,560|0,550|0,560|0,570|0,590|0,580|0,590|
|**Método Racional**|**Coef, Escorrentía - 5 años**|**- **|0,590|0,590|0,560|0,550|0,560|0,570|0,590|0,580|0,590|
|**Método Racional**|**Coef, Escorrentía - 10 años**|**- **|0,590|0,590|0,560|0,550|0,560|0,570|0,590|0,580|0,590|

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 24 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

|Cuenca<br>Coef, Escorrentía - 25 años<br>Coef, Escorrentía - 50 años<br>Coef, Escorrentía - 100 años<br>Coef, Escorrentía - 200 años<br>Caudal - 2 años<br>Caudal - 5 años<br>Caudal - 10 años<br>Caudal - 25 años<br>Caudal - 50 años<br>Caudal - 100 años<br>Caudal - 200 años|Col2|Canal|Canal BOSE|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Cuenca**<br>**Coef, Escorrentía - 25 años**<br>**Coef, Escorrentía - 50 años**<br>**Coef, Escorrentía - 100 años**<br>**Coef, Escorrentía - 200 años**<br>**Caudal - 2 años**<br>**Caudal - 5 años**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**|**Cuenca**<br>**Coef, Escorrentía - 25 años**<br>**Coef, Escorrentía - 50 años**<br>**Coef, Escorrentía - 100 años**<br>**Coef, Escorrentía - 200 años**<br>**Caudal - 2 años**<br>**Caudal - 5 años**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**|**Subcuenca**|**1 **|**2 **|**3 **|**4 **|**5 **|**6 **|**7 **|**8 **|**9 **|
|**Cuenca**<br>**Coef, Escorrentía - 25 años**<br>**Coef, Escorrentía - 50 años**<br>**Coef, Escorrentía - 100 años**<br>**Coef, Escorrentía - 200 años**<br>**Caudal - 2 años**<br>**Caudal - 5 años**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**|**Coef, Escorrentía - 25 años**|**- **|0,649|0,649|0,616|0,605|0,616|0,627|0,649|0,638|0,649|
|**Cuenca**<br>**Coef, Escorrentía - 25 años**<br>**Coef, Escorrentía - 50 años**<br>**Coef, Escorrentía - 100 años**<br>**Coef, Escorrentía - 200 años**<br>**Caudal - 2 años**<br>**Caudal - 5 años**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**|**Coef, Escorrentía - 50 años**|**- **|0,708|0,708|0,672|0,660|0,672|0,684|0,708|0,696|0,708|
|**Cuenca**<br>**Coef, Escorrentía - 25 años**<br>**Coef, Escorrentía - 50 años**<br>**Coef, Escorrentía - 100 años**<br>**Coef, Escorrentía - 200 años**<br>**Caudal - 2 años**<br>**Caudal - 5 años**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**|**Coef, Escorrentía - 100 años**|**- **|0,738|0,738|0,700|0,688|0,700|0,713|0,738|0,725|0,738|
|**Cuenca**<br>**Coef, Escorrentía - 25 años**<br>**Coef, Escorrentía - 50 años**<br>**Coef, Escorrentía - 100 años**<br>**Coef, Escorrentía - 200 años**<br>**Caudal - 2 años**<br>**Caudal - 5 años**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**|**Coef, Escorrentía - 200 años**|**- **|0,789|0,789|0,749|0,736|0,749|0,763|0,789|0,776|0,789|
|**Cuenca**<br>**Coef, Escorrentía - 25 años**<br>**Coef, Escorrentía - 50 años**<br>**Coef, Escorrentía - 100 años**<br>**Coef, Escorrentía - 200 años**<br>**Caudal - 2 años**<br>**Caudal - 5 años**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**|**Caudal - 2 años**|**m3/s**|0,0493|0,0404|0,0925|0,0786|0,1144|0,0657|0,1852|0,0831|0,0525|
|**Cuenca**<br>**Coef, Escorrentía - 25 años**<br>**Coef, Escorrentía - 50 años**<br>**Coef, Escorrentía - 100 años**<br>**Coef, Escorrentía - 200 años**<br>**Caudal - 2 años**<br>**Caudal - 5 años**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**|**Caudal - 5 años**|**m3/s**|0,1001|0,0820|0,1875|0,1595|0,2320|0,1333|0,3756|0,1685|0,1064|
|**Cuenca**<br>**Coef, Escorrentía - 25 años**<br>**Coef, Escorrentía - 50 años**<br>**Coef, Escorrentía - 100 años**<br>**Coef, Escorrentía - 200 años**<br>**Caudal - 2 años**<br>**Caudal - 5 años**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**|**Caudal - 10 años**|**m3/s**|0,1336|0,1095|0,2504|0,2130|0,3099|0,1780|0,5017|0,2251|0,1421|
|**Cuenca**<br>**Coef, Escorrentía - 25 años**<br>**Coef, Escorrentía - 50 años**<br>**Coef, Escorrentía - 100 años**<br>**Coef, Escorrentía - 200 años**<br>**Caudal - 2 años**<br>**Caudal - 5 años**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**|**Caudal - 25 años**|**m3/s**|0,1937|0,1586|0,3629|0,3087|0,4491|0,2580|0,7271|0,3262|0,2059|
|**Cuenca**<br>**Coef, Escorrentía - 25 años**<br>**Coef, Escorrentía - 50 años**<br>**Coef, Escorrentía - 100 años**<br>**Coef, Escorrentía - 200 años**<br>**Caudal - 2 años**<br>**Caudal - 5 años**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**|**Caudal - 50 años**|**m3/s**|0,2491|0,2040|0,4667|0,3970|0,5776|0,3317|0,9350|0,4195|0,2648|
|**Cuenca**<br>**Coef, Escorrentía - 25 años**<br>**Coef, Escorrentía - 50 años**<br>**Coef, Escorrentía - 100 años**<br>**Coef, Escorrentía - 200 años**<br>**Caudal - 2 años**<br>**Caudal - 5 años**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**|**Caudal - 100 años**|**m3/s**|0,2985|0,2445|0,5593|0,4758|0,6922|0,3976|1,1206|0,5028|0,3174|
|**Cuenca**<br>**Coef, Escorrentía - 25 años**<br>**Coef, Escorrentía - 50 años**<br>**Coef, Escorrentía - 100 años**<br>**Coef, Escorrentía - 200 años**<br>**Caudal - 2 años**<br>**Caudal - 5 años**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**|**Caudal - 200 años**|**m3/s**|0,3612|0,2958|0,6767|0,5756|0,8375|0,4811|1,3559|0,6083|0,3840|
|**Método DGA-AC**|**Caudal diario (24 hr) - 2 años**|**m3/s**|0,00016|0,00014|0,00027|0,00024|0,00032|0,00023|0,00045|0,00026|0,00017|
|**Método DGA-AC**|**Caudal diario (24 hr) - 5 años**|**m3/s**|0,00024|0,00020|0,00040|0,00036|0,00047|0,00034|0,00066|0,00038|0,00025|
|**Método DGA-AC**|**Caudal diario (24 hr) - 10 años**|**m3/s**|0,0003|0,0002|0,0005|0,0004|0,0006|0,0004|0,0008|0,0004|0,0003|
|**Método DGA-AC**|**Caudal diario (24 hr) - 25 años**|**m3/s**|0,00031|0,00027|0,00053|0,00047|0,00063|0,00045|0,00087|0,00051|0,00033|
|**Método DGA-AC**|**Caudal diario (24 hr) - 50 años**|**m3/s**|0,00035|0,00030|0,00059|0,00053|0,00070|0,00050|0,00097|0,00056|0,00037|
|**Método DGA-AC**|**Caudal diario (24 hr) - 100 años**|**m3/s**|0,00038|0,00032|0,00064|0,00057|0,00075|0,00054|0,00105|0,00061|0,00039|
|**Método DGA-AC**|**Caudal diario (24 hr) - 200 años**|**m3/s**|0,00042|0,00036|0,00072|0,00064|0,00085|0,00061|0,00118|0,00069|0,00044|
|**Método DGA-AC**|**Caudal Máximo - 2 años**|**m3/s**|0,00049|0,00042|0,00084|0,00075|0,00099|0,00071|0,00138|0,00080|0,00052|
|**Método DGA-AC**|**Caudal Máximo - 5 años**|**m3/s**|0,00072|0,00062|0,00123|0,00110|0,00145|0,00104|0,00202|0,00117|0,00076|
|**Método DGA-AC**|**Caudal Máximo - 10 años**|**m3/s**|0,00085|0,00073|0,00144|0,00128|0,00169|0,00121|0,00236|0,00137|0,00089|
|**Método DGA-AC**|**Caudal Máximo - 25 años**|**m3/s**|0,00096|0,00082|0,00163|0,00146|0,00192|0,00138|0,00268|0,00155|0,00101|
|**Método DGA-AC**|**Caudal Máximo - 50 años**|**m3/s**|0,00107|0,00092|0,00182|0,00163|0,00214|0,00153|0,00299|0,00173|0,00112|
|**Método DGA-AC**|**Caudal Máximo - 100 años**|**m3/s**|0,00115|0,00099|0,00196|0,00175|0,00231|0,00165|0,00322|0,00187|0,00121|
|**Método DGA-AC**|**Caudal Máximo - 200 años**|**m3/s**|0,00130|0,00112|0,00221|0,00197|0,00260|0,00186|0,00364|0,00211|0,00137|
|**Método Verni & King Modificada**|**Caudal - 2 años**|**m3/s**|0,00018|0,00015|0,00033|0,00029|0,00039|0,00027|0,00057|0,00031|0,00019|
|**Método Verni & King Modificada**|**Caudal - 5 años**|**m3/s**|0,00045|0,00038|0,00083|0,00073|0,00100|0,00068|0,00145|0,00078|0,00048|
|**Método Verni & King Modificada**|**Caudal - 10 años**|**m3/s**|0,00068|0,00057|0,00124|0,00110|0,00150|0,00103|0,00219|0,00118|0,00072|
|**Método Verni & King Modificada**|**Caudal - 25 años**|**m3/s**|0,00110|0,00092|0,00200|0,00176|0,00241|0,00165|0,00352|0,00189|0,00116|
|**Método Verni & King Modificada**|**Caudal - 50 años**|**m3/s**|0,00145|0,00122|0,00264|0,00233|0,00319|0,00218|0,00465|0,00251|0,00153|
|**Método Verni & King Modificada**|**Caudal - 100 años**|**m3/s**|0,00186|0,00156|0,00338|0,00297|0,00407|0,00279|0,00594|0,00320|0,00196|
|**Método Verni & King Modificada**|**Caudal - 200 años**|**m3/s**|0,00230|0,00193|0,00418|0,00368|0,00504|0,00345|0,00736|0,00396|0,00242|
|**Caudal de Diseño**|**Caudal - 2 años**|**m3/s**|0,04934|0,04041|0,09245|0,07864|0,11442|0,06572|0,18523|0,08311|0,05246|
|**Caudal de Diseño**|**Caudal - 5 años**|**m3/s**|0,10006|0,08196|0,18749|0,15948|0,23203|0,13328|0,37565|0,16854|0,10639|

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 25 de 26

Proyecto N° 1291 (Códice)
Contrato N° 4500061768 (Mantoverde)

|Cuenca<br>Caudal - 10 años<br>Caudal - 25 años<br>Caudal - 50 años<br>Caudal - 100 años<br>Caudal - 200 años<br>Caudal Detrítico - 2 años<br>Caudal Detrítico - 5 años<br>Caudal Detrítico - 10 años<br>Caudal Detrítico - 25 años<br>Caudal Detrítico - 50 años<br>Caudal Detrítico - 100 años<br>Caudal Detrítico - 200 años|Col2|Canal|Canal BOSE|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Cuenca**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**<br>**Caudal Detrítico - 2 años**<br>**Caudal Detrítico - 5 años**<br>**Caudal Detrítico - 10 años**<br>**Caudal Detrítico - 25 años**<br>**Caudal Detrítico - 50 años**<br>**Caudal Detrítico - 100 años**<br>**Caudal Detrítico - 200 años**|**Cuenca**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**<br>**Caudal Detrítico - 2 años**<br>**Caudal Detrítico - 5 años**<br>**Caudal Detrítico - 10 años**<br>**Caudal Detrítico - 25 años**<br>**Caudal Detrítico - 50 años**<br>**Caudal Detrítico - 100 años**<br>**Caudal Detrítico - 200 años**|**Subcuenca**|**1 **|**2 **|**3 **|**4 **|**5 **|**6 **|**7 **|**8 **|**9 **|
|**Cuenca**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**<br>**Caudal Detrítico - 2 años**<br>**Caudal Detrítico - 5 años**<br>**Caudal Detrítico - 10 años**<br>**Caudal Detrítico - 25 años**<br>**Caudal Detrítico - 50 años**<br>**Caudal Detrítico - 100 años**<br>**Caudal Detrítico - 200 años**|**Caudal - 10 años**|**m3/s**|0,13365|0,10946|0,25041|0,21301|0,30991|0,17801|0,50172|0,22511|0,14209|
|**Cuenca**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**<br>**Caudal Detrítico - 2 años**<br>**Caudal Detrítico - 5 años**<br>**Caudal Detrítico - 10 años**<br>**Caudal Detrítico - 25 años**<br>**Caudal Detrítico - 50 años**<br>**Caudal Detrítico - 100 años**<br>**Caudal Detrítico - 200 años**|**Caudal - 25 años**|**m3/s**|0,19369|0,15864|0,36291|0,30870|0,44913|0,25798|0,72711|0,32623|0,20592|
|**Cuenca**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**<br>**Caudal Detrítico - 2 años**<br>**Caudal Detrítico - 5 años**<br>**Caudal Detrítico - 10 años**<br>**Caudal Detrítico - 25 años**<br>**Caudal Detrítico - 50 años**<br>**Caudal Detrítico - 100 años**<br>**Caudal Detrítico - 200 años**|**Caudal - 50 años**|**m3/s**|0,24907|0,20400|0,46667|0,39697|0,57755|0,33174|0,93502|0,41951|0,26481|
|**Cuenca**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**<br>**Caudal Detrítico - 2 años**<br>**Caudal Detrítico - 5 años**<br>**Caudal Detrítico - 10 años**<br>**Caudal Detrítico - 25 años**<br>**Caudal Detrítico - 50 años**<br>**Caudal Detrítico - 100 años**<br>**Caudal Detrítico - 200 años**|**Caudal - 100 años**|**m3/s**|0,29851|0,24449|0,55930|0,47576|0,69218|0,39759|1,12060|0,50278|0,31736|
|**Cuenca**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**<br>**Caudal Detrítico - 2 años**<br>**Caudal Detrítico - 5 años**<br>**Caudal Detrítico - 10 años**<br>**Caudal Detrítico - 25 años**<br>**Caudal Detrítico - 50 años**<br>**Caudal Detrítico - 100 años**<br>**Caudal Detrítico - 200 años**|**Caudal - 200 años**|**m3/s**|0,36117|0,29582|0,67672|0,57564|0,83750|0,48106|1,35586|0,60833|0,38399|
|**Cuenca**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**<br>**Caudal Detrítico - 2 años**<br>**Caudal Detrítico - 5 años**<br>**Caudal Detrítico - 10 años**<br>**Caudal Detrítico - 25 años**<br>**Caudal Detrítico - 50 años**<br>**Caudal Detrítico - 100 años**<br>**Caudal Detrítico - 200 años**|**Caudal Detrítico - 2 años**|**m3/s**|0,07049|0,05773|0,13207|0,11235|0,16345|0,09389|0,26462|0,11873|0,07494|
|**Cuenca**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**<br>**Caudal Detrítico - 2 años**<br>**Caudal Detrítico - 5 años**<br>**Caudal Detrítico - 10 años**<br>**Caudal Detrítico - 25 años**<br>**Caudal Detrítico - 50 años**<br>**Caudal Detrítico - 100 años**<br>**Caudal Detrítico - 200 años**|**Caudal Detrítico - 5 años**|**m3/s**|0,14295|0,11708|0,26784|0,22783|0,33148|0,19040|0,53664|0,24077|0,15198|
|**Cuenca**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**<br>**Caudal Detrítico - 2 años**<br>**Caudal Detrítico - 5 años**<br>**Caudal Detrítico - 10 años**<br>**Caudal Detrítico - 25 años**<br>**Caudal Detrítico - 50 años**<br>**Caudal Detrítico - 100 años**<br>**Caudal Detrítico - 200 años**|**Caudal Detrítico - 10 años**|**m3/s**|0,19093|0,15638|0,35773|0,30430|0,44272|0,25430|0,71674|0,32158|0,20299|
|**Cuenca**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**<br>**Caudal Detrítico - 2 años**<br>**Caudal Detrítico - 5 años**<br>**Caudal Detrítico - 10 años**<br>**Caudal Detrítico - 25 años**<br>**Caudal Detrítico - 50 años**<br>**Caudal Detrítico - 100 años**<br>**Caudal Detrítico - 200 años**|**Caudal Detrítico - 25 años**|**m3/s**|0,27670|0,22663|0,51844|0,44100|0,64161|0,36854|1,03873|0,46605|0,29418|
|**Cuenca**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**<br>**Caudal Detrítico - 2 años**<br>**Caudal Detrítico - 5 años**<br>**Caudal Detrítico - 10 años**<br>**Caudal Detrítico - 25 años**<br>**Caudal Detrítico - 50 años**<br>**Caudal Detrítico - 100 años**<br>**Caudal Detrítico - 200 años**|**Caudal Detrítico - 50 años**|**m3/s**|0,35581|0,29143|0,66668|0,56710|0,82507|0,47392|1,33574|0,59931|0,37829|
|**Cuenca**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**<br>**Caudal Detrítico - 2 años**<br>**Caudal Detrítico - 5 años**<br>**Caudal Detrítico - 10 años**<br>**Caudal Detrítico - 25 años**<br>**Caudal Detrítico - 50 años**<br>**Caudal Detrítico - 100 años**<br>**Caudal Detrítico - 200 años**|**Caudal Detrítico - 100 años**|**m3/s**|0,42644|0,34927|0,79900|0,67966|0,98883|0,56798|1,60085|0,71826|0,45338|
|**Cuenca**<br>**Caudal - 10 años**<br>**Caudal - 25 años**<br>**Caudal - 50 años**<br>**Caudal - 100 años**<br>**Caudal - 200 años**<br>**Caudal Detrítico - 2 años**<br>**Caudal Detrítico - 5 años**<br>**Caudal Detrítico - 10 años**<br>**Caudal Detrítico - 25 años**<br>**Caudal Detrítico - 50 años**<br>**Caudal Detrítico - 100 años**<br>**Caudal Detrítico - 200 años**|**Caudal Detrítico - 200 años**|**m3/s**|0,51596|0,42260|0,96674|0,82235|1,19643|0,68723|1,93694|0,86905|0,54856|

1291-CAL-003 - MEMORIA DE CÁLCULO HIDROLÓGICA - CANALES DE CONTORNO BOSE_REV1 Página 26 de 26