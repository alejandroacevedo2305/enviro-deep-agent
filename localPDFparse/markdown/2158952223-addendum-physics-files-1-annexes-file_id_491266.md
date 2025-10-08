---
title: Sin título
author: Francisca Valenzuela
date: D:20231031161343+00'00'
language: es
type: report
pages: 20
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1 INTRODUCCIÓN
  - 2 OBJETIVO
  - 1
  - 3 ANTECEDENTES DEL PROYECTO
  - 4 METODOLOGÍA MODELACIÓN DE EMISIONES
  - 5 RESULTADOS DE LA MODELACIÓN
  - 6 CONCLUSIÓN Y ANÁLISIS DE RESULTADOS DE MODELACIÓN
  - 7 APÉNDICES
-->

**ANEXO 4**
**MODELACIÓN DE EMISIONES**

**Calidad del aire**

**PROYECTO**

**“MEJORAS AL SISTEMA DE TRATAMIENTO DE RILES**

**BODEGA CLOS APALTA”**

**Octubre 2023**

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

**INDICE**

1 Introducción 1

2 Objetivo 1

3 Antecedentes del proyecto 2

3.1 Localización 2

3.2 Cronograma general 2

3.3 Emisiones a modelar 2

4 Metodología modelación de emisiones 3

4.1 Identificación de normativa asociada 4

4.2 Identificación situación base de calidad del aire 4

4.3 Descripción y justificación del modelo 5

4.4 Identificación de fuentes emisoras 6

4.5 Identificación de receptores sensibles 6

4.6 Caracterización del viento 8

4.7 Modelación MP10 8

5 Resultados de la modelación 10

5.1 Resultados obtenidos en Screen View 10

6 Análisis de resultados de modelación 14

7 Apéndices 16

7.1 Resultado modelación MP10 16

7.2 Resultados modelación MP2,5 17

**INDICE TABLAS**

Tabla 3-1 Cronograma de actividades del Proyecto ........................................................... 2
Tabla 3-2 Emisiones atmosféricas para el año 1 del proyecto ........................................... 2
Tabla 3-3 Año y emisiones a modelar por contaminante .................................................... 3
Tabla 3-4 Emisiones a modelar.......................................................................................... 3
Tabla 4-1 Normas primaria de calidad del aire ................................................................... 4
Tabla 4-2 coordenadas y contaminantes medidos en estación San Fernando ................... 5
Tabla 4-3 cumplimiento normativo Estación San Fernando para el periodo 2020-2022 ..... 5
Tabla 4-4 Ubicación y distancia de receptores sensibles ................................................... 8
Tabla 4-5 Caracterización del viento .................................................................................. 8
Tabla 4-6 Parámetros de modelación ................................................................................ 9
Tabla 5-1 Resultados de modelación de MP10 y MP2,5 .................................................. 10
Tabla 5-2 Concentración diaria y anual de MP10 ............................................................. 12

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

Tabla 5-3 Concentración diaria y anual de MP2,5 ............................................................ 13
Tabla 6-1 Aporte del proyecto a la calidad de aire ........................................................... 14

**INDICE FIGURAS**

Figura 4-1 Receptores sensibles........................................................................................ 7
Figura 4-2 Datos de entrada para la modelación ............................................................... 8
Figura 4-3 Parámetros ingresados en software de modelación Screen View ..................... 9

**INDICE GRÁFICOS**

Gráfico 5-1 Modelación de contaminante MP10 ............................................................... 11
Gráfico 5-2 Modelación de contaminante MP2,5 .............................................................. 11

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

# 1 INTRODUCCIÓN

El presente Anexo entrega el detalle y resultados obtenidos de la modelación de
dispersión de MP10 y MP2,5 generados durante el año 1 del proyecto **“Mejoras al**
**Sistema de Tratamiento de RILes de Bodega Clos Apalta”** en adelante el Proyecto, los
cuales son regulados a través de las normas primarias y secundarias de calidad del
aire.

El Proyecto consiste en la construcción y operación de dos nuevas unidades: Estanque
Reactor (SBR), cuyo sistema es el más eficiente en la modalidad de lodos activados y un
Sistema Terraplanta, que consiste en una modalidad de lechos de secado de lodos, que
utiliza plantas para la deshidratación y estabilización de éstos. Asimismo, dichas mejoras,
contemplan eficiencia del abatimiento, lo cual permitirá producir mayor cantidad de litros de
vino (con un máximo de 260.000 litros/año) y facultará acondicionar un aumento en el
caudal de RILes que se genera en vendimia, con un máximo de 25 m [3] /día.

El proyecto se localiza dentro de 522 ha del fundo y presenta una superficie de construcción
de 700 m2

Para la modelación se utiliza los resultados obtenidos en la Estimación de emisiones
atmosféricas en el año 1 del Proyecto. Las emisiones a considerar por el Proyecto se deben

a:

 - Emisiones de material particulado de resuspensión producto del movimiento de
tierra para las obras de construcción.

 - Emisiones de material particulado de resuspensión por la circulación de vehículos
por caminos pavimentados y no pavimentados.

 - Emisiones de material particulado y gases de combustión de los motores de la flota
vehicular.

 - Emisión Maquinaria utilizada por el Proyecto.

Cabe destacar que, se consideran como receptores sensibles a las viviendas identificadas
en el estudio de Ruido y vibraciones, cercanas al Proyecto.

Con el fin de analizar y descartar el impacto sobre aquellos receptores sensibles
identificados, se ha utilizado como normativas de referencia las Normas Primarias de
calidad del aire para los contaminantes de MP10 y MP2,5

# 2 OBJETIVO

El objetivo del presente informe corresponde a la modelación de la dispersión de los
contaminantes regulados a través de las normas primarias de calidad del Aire, que se
emitirán durante la ejecución del Proyecto sobre los receptores de interés, y así
determinar los efectos en la calidad del aire del sector, utilizando un modelo básico del
tipo gaussiano (Screen View).

# 1

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

# 3 ANTECEDENTES DEL PROYECTO

## 3.1 Localización

El proyecto se localiza en el Fundo El Cóndor de Apalta, Hijuela Villa Eloísa, Comuna de
Santa Cruz, Provincia de Colchagua, Región Libertador Bernardo O ́Higgins, Chile.

## 3.2 Cronograma general

El Proyecto contó con una fase de construcción de una duración de 4 meses y una fase de
operación con una duración indefinida. En la siguiente tabla se señala el cronograma de las
etapas de Construcción y Operación, detallando las principales tareas efectuadas en la
tabla siguiente:

**Tabla** **3-1 Cronograma** **de** **actividades** **del Proyecto**

|Actividad|Mes 1|Col3|Col4|Col5|Mes 2|Col7|Col8|Mes 3|Col10|Col11|Col12|Col13|Mes 4|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Etapa de Construcción**|**S1 **|**S2**|**S3**|**S4**|**S5**|**S6**|**S7**|**S8**|**S9**|**S10**|**S11**|**S12**|**S1**<br>**3**|**S14**|**S15**|**S16**|
|Construcción y<br>habilitación SBR|||||||||||||||||
|Construcción y<br>habilitación Terraplanta|||||||||||||||||
|Instalación y conexión de<br>sistema de control|||||||||||||||||
|**Etapa de operación**|**S1 **|**S2**|**S3**|**S4**|**S5**|**S6**|**S7**|**S8**|**S9**|**S10**|**S11**|**S12**|**S1**<br>**3**|**S14**|**S15**|**S16**|
|Puesta en marcha<br>(Prueba y correcciones)|||||||||||||||||
|Operación Sistema de<br>Tratamiento|||||||||||||||||

Fuente: DIA

## 3.3 Emisiones a modelar

En la siguiente tabla, se presentan los resultados obtenidos en la Estimación de emisiones
atmosféricas para el año 1 del Proyecto. Para las cuales, se debe sumar las emisiones
correspondientes a la fase de construcción que dura solamente 4 meses, y del año 1 de la
fase de operación. En la siguiente tabla se señala las emisiones para el año 1 del Proyecto

**Tabla 3-2 Emisiones** **atmosféricas** **para** **el año 1 del proyecto**

|Emisión total|Emisión [t/año]|Col3|Col4|
|---|---|---|---|
|**Emisión total**|**Fase de**<br>**construcción**|**Año 1 Fase de**<br>**operación**|**Total**<br>**año 1**|
|MP10 Resuspensión|0,16|0,22|0,38|
|MP10 Combustión|0,002|0,0001|0,002|
|MP10 total|0,17|0,22|0,39|
|MP2,5 Resuspensión|0,02|0,02|0,04|
|MP2,5 Combustión|0,002|0,0001|0,002|
|MP2,5 total|0,02|0,02|0,04|
|CO|0,02|0,001|0,02|

2

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

|COV|0,002|0,00005|0,002|
|---|---|---|---|
|NOx|0,04|0,01|0,05|
|NH3|0,00003|0,0001|0,0001|
|SO2|0,00002|0,00003|0,0001|

Fuente: Anexo de estimación de emisiones atmosféricas

En base a las emisiones de la tabla anteriores, se va a modelar las emisiones
correspondientes al total de MP10 y MP2,5. En la siguiente tabla, se detalla el año y la
concentración a modelar de cada contaminante.

**Tabla 3-3 Año** **y** **emisiones** **a modelar por contaminante**

|Contaminante|Año a modelar|Emisión<br>[t/año]|
|---|---|---|
|MP10 total|Año 1|0,39|
|MP 2,5 total|Año 1|0,04|

Fuente: elaboración propia

Para efectos de la modelación de contaminantes en el software Screen View, se debe
realizar una conversión de unidades pasando de ton/año a g/s/m2. Para ello se consideró
que 1 tonelada de MP10 equivale a 1.000.000 gramos, que 12 meses equivalen a 30 días,
que un día tiene 86.400 segundos. Respecto a la superficie, se considera una superficie de
5.220.000 m2 (522 ha). Por lo tanto, utilizando la siguiente ecuación, se obtienen las
emisiones a modelar.

seg ~~[)]~~

días [año] ~~[)]~~ [x1]

[día] 1 [h]

hora [)] [x] 3.600 [(] se

[día]
24 [(] hora

t ~~[)]~~ [x1]

365 [(] días [año]

Emisión a modelar(gsm2⁄ ⁄ ) =

emisión [t]
(

[t]

año ~~[)]~~ [x1.000.000 ] [(g] t

5.220.000 (m2)

En la siguiente tabla se señala los resultados obtenidos de las emisiones a modelar

**Tabla** **3-4 Emisiones** **a modelar**

|Contaminante|Año a modelar|Emisión<br>[t/año]|Emisión a modelar<br>[g/s/m2]|
|---|---|---|---|
|MP10 total|Año 1|0,39|2,37E-09|
|MP 2,5 total|Año 1|0,04|2,43E-10|

Fuente: elaboración propia

# 4 METODOLOGÍA MODELACIÓN DE EMISIONES

En el presente apartado se presenta la metodología utilizada para modelar las emisiones
generadas por la construcción del Proyecto.

i. Identificación de normativa de contaminantes regulados;
ii. Identificación de la situación base de calidad del aire de la zona donde se emplaza
el Proyecto;
iii. Descripción y justificación del modelo a utilizar;
iv. Identificación de fuentes emisoras;
v. Identificación de receptores sensibles

3

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

vi. Identificación de características del viento;
vii. Modelación de MP10 y MP2,5

## 4.1 Identificación de normativa asociada

En la siguiente tabla se presenta las normas de calidad de aire para MP10 y MP2,5

**Tabla 4-1 Normas** **primaria** **de** **calidad** **del aire**

|Contaminante|Concentración<br>máxima permitida<br>[μg/m3N]|Limite estadístico|fuente|
|---|---|---|---|
|MP10|130|Percentil 98 de la media<br>aritmética diaria durante 1 año|D.S. N°12/2022 del<br>MMA|
|MP10|50|Media aritmética trianual|Media aritmética trianual|
|MP 2,5|50|Percentil 98 de la media<br>aritmética diaria durante 1 año|D.S. N°12/2011 del<br>MMA|
|MP 2,5|20|Media aritmética trianual|Media aritmética trianual|

Fuente: elaboración propia

## 4.2 Emisiones e Identificación situación base de calidad del aire

En la siguiente tabla, se presenta el porcentaje de aporte de las emisiones generadas por
el proyecto en relación al inventario de emisiones presentado en la tabla 6 del D.S. N°1/2021
del MMA que establece Plan de Descontaminación Atmosférica para el Valle Central de la
Región del Libertador General Bernardo O’Higgins. Se consideran las emisiones de las
fuentes fijas del inventario ya que es el origen más representativo con el proyecto.

**Tabla 4-2 Emisiones** **proyecto** **con respecto** **al inventario** **de** **emisiones** **en fuentes fijas**

|Contaminante|Inventario de emisiones<br>en fuentes fijas<br>(D.S. N°1/2021)<br>[t/año]|Proyecto<br>[t/año]|% respecto inventario|
|---|---|---|---|
|MP10|547|0,39|0,07%|
|MP2,5|360|0,04|0,01%|
|SO2|1338|0,0001|0,00001%|
|NOX|1883|0,05|0,003%|
|CO|931|0,02|0,002%|
|COV|142|0,002|0,001%|
|NH3|219|0,0001|0,00005%|

Fuente: elaboración propia

Como se observa en la tabla anterior, el aporte de las emisiones generadas por el proyecto
es menor al 0,002% en NOx, CO y SO2, por lo tanto, sus aportes en calidad del aire serán
aún menores por lo cual no es necesario hacer modelación para estos contaminantes. De
todas maneras se realiza modelación de la calidad del aire para MP10 y MP2,5 ya que la
zona está declarada como saturada en MP10 y MP2,5, según los decretos D.S. N°7/2009
del MINSEGPRES y D.S. N°42/2017 del MMA, y sus aportes respecto del inventario son
algo mayores siendo 0,01% en MP2,5 y 0,07% en MP10.

## 4

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

Para el análisis de este componente en el área donde se ubicará el Proyecto, se entregan
antecedentes sobre la situación base en la zona. Para ello se observó en el portal del
Sistema de Información Nacional de Calidad del Aire (SINCA), que en la región del
Libertador General Bernardo O’Higgins existen 7 estaciones de monitoreo, de las cuales 3
pertenecen a la Red CODELCO El Teniente, Rancagua y 4 a la Red del Ministerio del Medio
Ambiente (MMA). Éstas presentan información de diferentes parámetros para monitorear la
calidad del aire.

Se identificó que la estación de monitoreo más cercana corresponde a la “San Fernando”,
perteneciente a la Red MMA y se ubica a 27 km de distancia hacia el este del del Proyecto.
Sus coordenadas y parámetros medidas se presentan en la siguiente tabla

**Tabla 4-3** **coordenadas** **y** **contaminantes medidos** **en estación San Fernando**

|Estación|Coordenadas<br>(WGS84, UTM HUSO 19S)|Col3|Contaminante<br>medido|Año de registro<br>disponibles|
|---|---|---|---|---|
|**Estación**|**Este**|**Norte**|**Norte**|**Norte**|
|San<br>Fernando|317.503|6.171.746|MP10|2007-2023|
|San<br>Fernando|317.503|6.171.746|MP2,5|2007-2023|

Fuente: elaboración propia

Para analizar el cumplimiento normativo de cada contaminante medido en la estación, se
tomaron en cuenta los registros validados de los años más recientes, es decir, desde el
2020 en adelante. En la siguiente tabla, se presenta el cumplimiento normativo de la
situación base.

**Tabla 4-4 cumplimiento normativo Estación San Fernando** **para** **el periodo 2020-2022**

|Contaminante|Concentración<br>máxima permitida<br>[μg/m3N]|periodo|Registro<br>Estación San<br>Fernando|Cumple<br>la norma|%<br>respecto<br>a la<br>norma|
|---|---|---|---|---|---|
|MP10|130|2022|93|Sí|72|
|MP10|50|2020 al 2022|42,6|Sí|85|
|MP 2,5|50|2022|79|No|158|
|MP 2,5|20|2020 a l2022|21,6|No|108|

Fuente: elaboración propia

Como se observa en la tabla anterior los registros obtenidos para MP10 se encuentran
dentro de los límites permitidos por la norma de calidad ambiental, mientras que para el
MP2,5 se encuentra sobre la concentración máxima establecido en la norma de calidad
primaria.

## 4.3 Descripción y justificación del modelo

El modelo corresponde al SCREEN 3 de la United States Environmental Protection Agency
(USEPA), el modelo genera de forma interna la condición meteorológica más desfavorable,
por lo que entrega un resultado de concentraciones sobreestimadas. Esto se debe a que el
diseño ubica al receptor recibiendo el viento directo de las fuentes y no considera la
topografía del sector, además, se modela la concentración más alta de cada contaminante.
Debido a lo anterior, la modelación establece un valor máximo de peor escenario, por lo
que las concentraciones que llegarán a los receptores siempre son menores a las
estimadas por el modelo.

5

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

## 4.4 Identificación de fuentes emisoras

En la siguiente tabla, se señala se señala las actividades susceptibles de generar emisiones
durante la fase de construcción y operación del Proyecto.

**Tabla** **3.2-1** Actividades susceptibles de generar emisiones

|Fase de<br>Generación|Actividad|Tipo de Emisión|Contaminantes|
|---|---|---|---|
|Construcción|Excavación|Directa|MP10 - MP2,5|
|Construcción|Carguío y volteo de material|Directa|MP10 - MP2,5|
|Construcción|Tránsito de vehículos por<br>caminos pavimentados|Indirecta|MP10 - MP2,5|
|Construcción|Tránsito de vehículos por<br>caminos no pavimentados|Indirecta|MP10 - MP2,5|
|Construcción|Combustión de vehículos|Directa|MP10 - MP2,5 - NOx -<br>SO2 - NH3- CO - COV|
|Construcción|Combustión maquinaria<br>fuera de ruta|Directa|MP10 - MP2,5 - NOx -<br>CO - COV|
|Construcción|Combustión grupos<br>electrógenos|Directa|MP10 - MP2,5 - NOx -<br>SOx - CO - COV|
|Operación|Tránsito de vehículos por<br>caminos pavimentados|Indirecta|MP10 - MP2,5|
|Operación|Tránsito de vehículos por<br>caminos no pavimentados|Indirecta|MP10 - MP2,5|
|Operación|Combustión de vehículos|Directa|MP10 - MP2,5 - NOx -<br>SO2 - NH3- CO - COV|
|Operación|Combustión maquinaria<br>fuera de ruta|Directa|MP10 - MP2,5 - NOx -<br>CO - COV|
|Operación|Combustión grupos<br>electrógenos|Directa|MP10 - MP2,5 - NOx -<br>SOx - CO - COV|

Fuente: elaboración propia

## 4.5 Identificación de receptores sensibles

Para la modelación de la calidad del aire, se consideraron 4 receptores sensibles que fueron
consideradores para el estudio acústico del proyecto. En la siguiente figura se presenta la
ubicación de los receptores y en la siguiente tabla se presenta la coordenada y distancia al
proyecto.

6

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

**Figura 4-1 Receptores sensibles**

Planta de RILes

Planta de Compostaje

Fuente: elaboración propia

En la siguiente figura se señala, la ubicación de la estación San Fernando y el Proyecto que es
considerado un receptor sensible

**Figura 4-2 ubicación estación San Fernando y Proyecto**

Fuente: elaboración propia

7

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

**Tabla 4-5** **Ubicación y** **distancia** **de receptores** **sensibles**

|Clasificación|Receptor|Coordenadas<br>(WGS84, UTM HUSO 19S)|Col4|Distancia al<br>proyecto<br>[km]|
|---|---|---|---|---|
|**Clasificación**|**Receptor**|**Este**|**Norte**|**Norte**|
|Instalaciones al interior del fundo|R1|289.808|6.169.727|0,24|
|Instalación agrícola en predio<br>colindante|R2|290.308|6.169.296|0,48|
|Instalaciones al interior del fundo|R3|289.133|6.169.436|0,95|
|Viviendas|R4|289.924|6.168.306|1,4|
|Estación San Fernando|ESF|317.503|6.171.746|27|

Fuente: elaboración propia

## 4.6 Caracterización del viento

Se requieren los datos meteorológicos de la zona donde se ubicará el Proyecto, por lo que
se utilizó el Explorador Eólico del Ministerio de Energía para obtener las características del
viento en el punto central del predio del Proyecto. Las coordenadas y características de la
zona se presentan en la siguiente tabla

**Tabla 4-6 Caracterización del viento**

|Coordenadas<br>(WGS84, UTM HUSO 19S)|Col2|Viento<br>promedio<br>[m/s]|Dirección<br>predominante|
|---|---|---|---|
|**Este**|**Norte**|**Norte**|**Norte**|
|290.046|6.169.696|4,8|Suroeste (200<br>grados)|

Fuente: elaboración propia

## 4.7 Modelación MP10

Luego de determinar las características del predio y comenzar a realizar la modelación, se
procede a ingresar los datos al software. En primer lugar, se especifican los parámetros de
entrada correspondientes al Proyecto y su entorno, es decir, se determina el tipo de fuente
(puntual, área, volumen o llama), zona en que se ubicará el Proyecto (urbana o rural) y
altura del receptor en metros.

De acuerdo a las características del Proyecto presentada en la figura anterior, se considera
que corresponde a una fuente de “área”, se ubica en una zona rural y altura del receptor se
considera a los 0 metros.

**Figura 4-3 Datos de entrada para la modelación**

Fuente: Software de modelación Screen View

Posteriormente se ingresan los parámetros solicitados para la modelación

8

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

**Tabla 4-7 Parámetros** **de modelación**

|Contaminante|Razón de<br>emisión<br>[g/s/m]|Altura de la<br>fuente|Lado más<br>largo del<br>polígono<br>[m]|Lado más<br>corto del<br>polígono<br>[m]|Dirección<br>del viento<br>(grados)|
|---|---|---|---|---|---|
|MP 10|2,37E-09|0|190|90|200|
|MP 2,5|2,43E-10|2,43E-10|2,43E-10|2,43E-10|2,43E-10|

Fuente: elaboración propia

Luego, se ingresan los datos meteorológicos seleccionando la opción “Single Stability Class
and Wind Speed” incorporando los datos de velocidad promedio del viento y su estabilidad.
Para aquello, se considera la velocidad de viento promedio presentada anteriormente en la
celda que indica “10-Meters Wind Speed”, además se selecciona la opción inestable (opción
B) para los casos que la velocidad del viento se encuentre entre 1 a 5 m/s.

**Figura 4-4 Parámetros ingresados en software de modelación Screen View**

Fuente: Software de modelación Screen View

Finalmente, en opciones de terreno se selecciona la opción “Discrete Distances” ya que
esta permite ingresar las distancias en las cuales se quiere conocer la concentración que
alcanza el contaminante. Para efectos de la presente modelación, se consideraron tramos
de 50 metros iniciando desde 1 hasta los 1.000 metros.

9

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

# 5 RESULTADOS DE LA MODELACIÓN

## 5.1 Resultados obtenidos en Screen View

A continuación, se presentan los resultados de la modelación para cada contaminante.

**Tabla** **5-1 Resultados** **de modelación de MP10** **y MP2,5**

|Distancia<br>[m]|Concentración del contaminante<br>[μg/m3N]|Col3|
|---|---|---|
|**Distancia**<br>**[m]**|**MP10**|**MP2,5**|
|1|0,0145|0,00148|
|50|0,0158|0,00162|
|100|0,0168|0,00173|
|150|0,0052|0,00053|
|200|0,0031|0,00032|
|250|0,0021|0,00022|
|300|0,0016|0,00016|
|350|0,0012|0,00012|
|400|0,0009|0,00010|
|450|0,0007|0,00008|
|500|0,0006|0,00006|
|550|0,0005|0,00005|
|600|0,0004|0,00004|
|650|0,0004|0,00004|
|700|0,0003|0,00003|
|750|0,0003|0,00003|
|800|0,0002|0,00003|
|850|0,0002|0,00002|
|900|0,0002|0,00002|
|950|0,0002|0,00002|
|1.000|0,0002|0,00002|
|**Máx. concentración**<br>**[μg/m3N]**|**0,0168**|**0,00173**|

Fuente: elaboración propia

A continuación se presentan los gráficos de la modelación de MP10 y MP2.5

10

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

**Gráfico 5-1 Modelación de contaminante MP10**

Discrete Distance Vs. Concentration

Terrain Height = 0,00 m.

0,018

0,016

0,014

0,012

0,01

0,008

0,006

0,004

0,002

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||

0 100 200 300 400 500 600 700 800 900 1000 1100

Distance (m)

Fuente: elaboración propia

**Gráfico 5-2 Modelación de contaminante MP2,5**

Discrete Distance Vs. Concentration

Terrain Height = 0,00 m.

0,0018

0,0016

0,0014

0,0012

0,001

0,0008

0,0006

0,0004

0,0002

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||

0 100 200 300 400 500 600 700 800 900 1000 1100

Distance (m)

Fuente: elaboración propia

11

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

Las concentraciones de los contaminantes modelados deben ser convertidas a
concentraciones diarias y anuales para poder analizarlas con la normativa aplicable. Se
utiliza el factor de corrección anual y diario establecido por la EPA para material particulado.

**Tabla** **5-2 Concentración diaria** **y** **anual de MP10**

|Distancia<br>[m]|MP10<br>Concentración<br>del contaminante<br>[μg/m3N]|Factor de conversión|Col4|MP10<br>Concentración<br>anual<br>[μg/m3N]|MP10<br>Concentración<br>diaria<br>[μg/m3N]|
|---|---|---|---|---|---|
|**Distancia**<br>**[m]**|**MP10**<br>**Concentración**<br>**del contaminante**<br>**[μg/m3N]**|**Anual**|**diario**|**diario**|**diario**|
|1|0,0145|0,08|0,4|0,00116|0,00578|
|50|0,0158|0,0158|0,0158|0,00126|0,00632|
|100|0,0168|0,0168|0,0168|0,00135|0,00674|
|150|0,0052|0,0052|0,0052|0,00041|0,00207|
|200|0,0031|0,0031|0,0031|0,00025|0,00125|
|250|0,0021|0,0021|0,0021|0,00017|0,00086|
|300|0,0016|0,0016|0,0016|0,00012|0,00062|
|350|0,0012|0,0012|0,0012|0,00010|0,00048|
|400|0,0009|0,0009|0,0009|0,00007|0,00037|
|450|0,0007|0,0007|0,0007|0,00006|0,00030|
|500|0,0006|0,0006|0,0006|0,00005|0,00025|
|550|0,0005|0,0005|0,0005|0,00004|0,00020|
|600|0,0004|0,0004|0,0004|0,00003|0,00017|
|650|0,0004|0,0004|0,0004|0,00003|0,00015|
|700|0,0003|0,0003|0,0003|0,00003|0,00013|
|750|0,0003|0,0003|0,0003|0,00002|0,00011|
|800|0,0002|0,0002|0,0002|0,00002|0,00010|
|850|0,0002|0,0002|0,0002|0,00002|0,00009|
|900|0,0002|0,0002|0,0002|0,00002|0,00008|
|950|0,0002|0,0002|0,0002|0,00001|0,00007|
|1.000|0,0002|0,0002|0,0002|0,00001|0,00006|
|**Máx. concentración [μg/m3N]**|**Máx. concentración [μg/m3N]**|**Máx. concentración [μg/m3N]**|**Máx. concentración [μg/m3N]**|**0,00135**|**0,00674**|

Fuente: elaboración propia

12

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

**Tabla** **5-3** **Concentración diaria** **y** **anual de MP2,5**

|Distancia<br>[m]|MP2,5<br>Concentración<br>del contaminante<br>[μg/m3N]|Factor de conversión|Col4|MP2,5<br>Concentración<br>anual<br>[μg/m3N]|MP2,5<br>Concentración<br>diaria<br>[μg/m3N]|
|---|---|---|---|---|---|
|**Distancia**<br>**[m]**|**MP2,5**<br>**Concentración**<br>**del contaminante**<br>**[μg/m3N]**|**Anual**|**diario**|**diario**|**diario**|
|1|0,00148|0,08|0,4|0,00012|0,00059|
|50|0,00162|0,00162|0,00162|0,00013|0,00065|
|100|0,00173|0,00173|0,00173|0,00014|0,00069|
|150|0,00053|0,00053|0,00053|0,00004|0,00021|
|200|0,00032|0,00032|0,00032|0,00003|0,00013|
|250|0,00022|0,00022|0,00022|0,00002|0,00009|
|300|0,00016|0,00016|0,00016|0,00001|0,00006|
|350|0,00012|0,00012|0,00012|0,00001|0,00005|
|400|0,00010|0,00010|0,00010|0,00001|0,00004|
|450|0,00008|0,00008|0,00008|0,00001|0,00003|
|500|0,00006|0,00006|0,00006|0,00001|0,00003|
|550|0,00005|0,00005|0,00005|0,00000|0,00002|
|600|0,00004|0,00004|0,00004|0,00000|0,00002|
|650|0,00004|0,00004|0,00004|0,00000|0,00002|
|700|0,00003|0,00003|0,00003|0,00000|0,00001|
|750|0,00003|0,00003|0,00003|0,00000|0,00001|
|800|0,00003|0,00003|0,00003|0,00000|0,00001|
|850|0,00002|0,00002|0,00002|0,00000|0,00001|
|900|0,00002|0,00002|0,00002|0,00000|0,00001|
|950|0,00002|0,00002|0,00002|0,00000|0,00001|
|1.000|0,00002|0,00002|0,00002|0,00000|0,00001|
|**Máx. concentración [μg/m3N]**|**Máx. concentración [μg/m3N]**|**Máx. concentración [μg/m3N]**|**Máx. concentración [μg/m3N]**|**0,00014**|**0,00069**|

Fuente: elaboración propia

13

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

# 6 CONCLUSIÓN Y ANÁLISIS DE RESULTADOS DE MODELACIÓN

El porcentaje de aporte de las emisiones generadas por el proyecto en relación al inventario
de emisiones del D.S. N°1/2021 del MMA es menor, por lo tanto, no es necesario hacer
modelación para los contaminantes NOX, SO2 y CO. De todas maneras se realiza
modelación de la calidad del aire para MP10 y MP2,5 ya que la zona está declarada como
saturada en MP10 y MP2,5, según los decretos D.S. N°7/2009 del MINSEGPRES y D.S.
N°42/2017 del MMA.

De acuerdo a lo observado en los resultados obtenidos de la modelación, es posible
determinar que el peak de concentraciones para todos los contaminantes se genera a 100
metros del centro del polígono del Proyecto en dirección hacia el suroeste (200 grados).
Esto se debe a las condiciones del terreno donde se ubica el Proyecto.

De acuerdo a los gráficos de MP10 y MP2,5 se observa que la concentración horaria
obtenida alcanza el peak en los 100 metros y tiende a cero de forma gradual cerca de los
500 metros de distancia.

En la siguiente tabla, se presenta el aporte de las concentraciones diarias y anuales más
altas de MP10 y MP2,5.

**Tabla 6-1 Aporte del proyecto a la calidad de** **aire**

|Norma|Valor Norma<br>(μg/Nmɜ)|Aporte proyecto<br>(μg/Nmɜ)|Línea de<br>Base<br>(μg/Nmɜ)|Total<br>(μg/Nmɜ)|%aporte de<br>emisiones a<br>la norma|% total con<br>respecto a<br>norma|
|---|---|---|---|---|---|---|
|MP10 24 horas<br>Percentil 98|130|0,0067|93|93,007|0,005%|72%|
|MP10 Anual|50|0,0013|42,6|42,601|0,003%|85%|
|MP2,5 24 horas<br>Percentil 98|50|0,0007|79|79,001|0,001%|158%|
|MP2,5 Anual|20|0,0001<br>|21,6<br>|21,600<br>|0,001%|108%|

Fuente: elaboración propia

Como se observa en la tabla anterior las emisiones generadas por el proyecto cumplen con
los límites establecidos por las normativas identificadas, ya que se encuentran muy por
debajo de los valores limitantes, el porcentaje de aporte es menor al 0,005% y por lo tanto,
no es significativo.

De acuerdo con las mediciones de MP10 registradas en la estación en estación en el año
2022, la concentración de 24 horas de MP10 alcanza un valor de 93 μg/Nmɜ
correspondiente al 72% de la norma diaria. En caso de la concentración anual considerando
el periodo de 2020 al 2022, alcanza un calor de 42,6 μg/Nmɜ equivalentes al 85% de la
norma para dicho periodo.

En cuanto al MP 2,5 registradas en la estación en estación en el año 2022, la concentración
de 24 horas de MP 2,5 alcanza un valor de 79 μg/Nmɜ correspondiente al 158% de la norma
diaria. En caso de la concentración anual considerando el periodo de 2020 al 2022, alcanza
un calor de 21,6 μg/Nmɜ equivalentes al 108% de la norma para dicho periodo.

14

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

A pesar de que el aporte de material particulado del proyecto esta muy por debajo de los
limites establecidos en la norma, la concentración de MP2,5 esta por sobre los limites
establecidos en la norma, lo que se encuentra en consonancia con el hecho que la zona
está declarada como saturada en MP10 y MP2,5, según los decretos D.S. N°7/2009 del
MINSEGPRES y D.S. N°42/2017 del MMA.

15

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

# 7 APÉNDICES

## 7.1 Resultado modelación MP10

16

Modelación de Emisiones Atmosféricas
“Mejoras al Sistema de Tratamiento de RILes Bodega

Clos Apalta”

## 7.2 Resultados modelación MP2,5

17

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3-2: Emisiones** **atmosféricas** **para** **el año 1 del proyecto****

| Emisión total | Emisión [t/año] | Col3 | Col4 |
| --- | --- | --- | --- |
| **Emisión total** | **Fase de**<br>**construcción** | **Año 1 Fase de**<br>**operación** | **Total**<br>**año 1** |
| MP10 Resuspensión | 0,16 | 0,22 | 0,38 |
| MP10 Combustión | 0,002 | 0,0001 | 0,002 |
| MP10 total | 0,17 | 0,22 | 0,39 |
| MP2,5 Resuspensión | 0,02 | 0,02 | 0,04 |
| MP2,5 Combustión | 0,002 | 0,0001 | 0,002 |
| MP2,5 total | 0,02 | 0,02 | 0,04 |
| CO | 0,02 | 0,001 | 0,02 |

**Tabla 3-3: Año** **y** **emisiones** **a modelar por contaminante****

| Contaminante | Año a modelar | Emisión<br>[t/año] |
| --- | --- | --- |
| MP10 total | Año 1 | 0,39 |
| MP 2,5 total | Año 1 | 0,04 |

**Tabla 4-1: Normas** **primaria** **de** **calidad** **del aire****

| Contaminante | Concentración<br>máxima permitida<br>[μg/m3N] | Limite estadístico | fuente |
| --- | --- | --- | --- |
| MP10 | 130 | Percentil 98 de la media<br>aritmética diaria durante 1 año | D.S. N°12/2022 del<br>MMA |
| MP10 | 50 | Media aritmética trianual | Media aritmética trianual |
| MP 2,5 | 50 | Percentil 98 de la media<br>aritmética diaria durante 1 año | D.S. N°12/2011 del<br>MMA |
| MP 2,5 | 20 | Media aritmética trianual | Media aritmética trianual |

**Tabla 4-2: Emisiones** **proyecto** **con respecto** **al inventario** **de** **emisiones** **en fuentes fijas****

| Contaminante | Inventario de emisiones<br>en fuentes fijas<br>(D.S. N°1/2021)<br>[t/año] | Proyecto<br>[t/año] | % respecto inventario |
| --- | --- | --- | --- |
| MP10 | 547 | 0,39 | 0,07% |
| MP2,5 | 360 | 0,04 | 0,01% |
| SO2 | 1338 | 0,0001 | 0,00001% |
| NOX | 1883 | 0,05 | 0,003% |
| CO | 931 | 0,02 | 0,002% |
| COV | 142 | 0,002 | 0,001% |
| NH3 | 219 | 0,0001 | 0,00005% |

**Tabla 4-3: ** **coordenadas** **y** **contaminantes medidos** **en estación San Fernando****

| Estación | Coordenadas<br>(WGS84, UTM HUSO 19S) | Col3 | Contaminante<br>medido | Año de registro<br>disponibles |
| --- | --- | --- | --- | --- |
| **Estación** | **Este** | **Norte** | **Norte** | **Norte** |
| San<br>Fernando | 317.503 | 6.171.746 | MP10 | 2007-2023 |
| San<br>Fernando | 317.503 | 6.171.746 | MP2,5 | 2007-2023 |

**Tabla 4-4: cumplimiento normativo Estación San Fernando** **para** **el periodo 2020-2022****

| Contaminante | Concentración<br>máxima permitida<br>[μg/m3N] | periodo | Registro<br>Estación San<br>Fernando | Cumple<br>la norma | %<br>respecto<br>a la<br>norma |
| --- | --- | --- | --- | --- | --- |
| MP10 | 130 | 2022 | 93 | Sí | 72 |
| MP10 | 50 | 2020 al 2022 | 42,6 | Sí | 85 |
| MP 2,5 | 50 | 2022 | 79 | No | 158 |
| MP 2,5 | 20 | 2020 a l2022 | 21,6 | No | 108 |

**Tabla 4-5: ** **Ubicación y** **distancia** **de receptores** **sensibles****

| Clasificación | Receptor | Coordenadas<br>(WGS84, UTM HUSO 19S) | Col4 | Distancia al<br>proyecto<br>[km] |
| --- | --- | --- | --- | --- |
| **Clasificación** | **Receptor** | **Este** | **Norte** | **Norte** |
| Instalaciones al interior del fundo | R1 | 289.808 | 6.169.727 | 0,24 |
| Instalación agrícola en predio<br>colindante | R2 | 290.308 | 6.169.296 | 0,48 |
| Instalaciones al interior del fundo | R3 | 289.133 | 6.169.436 | 0,95 |
| Viviendas | R4 | 289.924 | 6.168.306 | 1,4 |
| Estación San Fernando | ESF | 317.503 | 6.171.746 | 27 |

**Tabla 4-6: Caracterización del viento****

| Coordenadas<br>(WGS84, UTM HUSO 19S) | Col2 | Viento<br>promedio<br>[m/s] | Dirección<br>predominante |
| --- | --- | --- | --- |
| **Este** | **Norte** | **Norte** | **Norte** |
| 290.046 | 6.169.696 | 4,8 | Suroeste (200<br>grados) |

**Tabla 4-7: Parámetros** **de modelación****

| Contaminante | Razón de<br>emisión<br>[g/s/m] | Altura de la<br>fuente | Lado más<br>largo del<br>polígono<br>[m] | Lado más<br>corto del<br>polígono<br>[m] | Dirección<br>del viento<br>(grados) |
| --- | --- | --- | --- | --- | --- |
| MP 10 | 2,37E-09 | 0 | 190 | 90 | 200 |
| MP 2,5 | 2,43E-10 | 2,43E-10 | 2,43E-10 | 2,43E-10 | 2,43E-10 |

**Tabla 6-1: Aporte del proyecto a la calidad de** **aire****

| Norma | Valor Norma<br>(μg/Nmɜ) | Aporte proyecto<br>(μg/Nmɜ) | Línea de<br>Base<br>(μg/Nmɜ) | Total<br>(μg/Nmɜ) | %aporte de<br>emisiones a<br>la norma | % total con<br>respecto a<br>norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 24 horas<br>Percentil 98 | 130 | 0,0067 | 93 | 93,007 | 0,005% | 72% |
| MP10 Anual | 50 | 0,0013 | 42,6 | 42,601 | 0,003% | 85% |
| MP2,5 24 horas<br>Percentil 98 | 50 | 0,0007 | 79 | 79,001 | 0,001% | 158% |
| MP2,5 Anual | 20 | 0,0001<br> | 21,6<br> | 21,600<br> | 0,001% | 108% |
