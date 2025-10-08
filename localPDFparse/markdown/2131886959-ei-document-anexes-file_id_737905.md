---
title: 1. Els títols s'han de fer emprant l'estil "Título 1", amb més d'una línia queda així.
author: QS-user (ORD-99-2)
date: D:20160525155017-04'00'
language: es
type: report
pages: 31
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1. Introducción
  - 1
  - 2. Diseño Geométrico
  - 3. Análisis de Socavación y Sedimentación
  - 4. Modelación Hidráulica
  - 5. Conclusiones y Recomendaciones
  - 6. Referencias
-->

A21_2016_575_ENAMI_Anexo_C_MC_Hidráulica_vC

**Anexo C1**
**Diseño Hidráulico de**
**Canalización Perimetral**

**para el Nuevo Depósito**
**de Ripios de Lixiviación,**

**Planta Matta**

Informe Avance N°1

Versión C

Cliente: ENAMI, Sr. Víctor Rivera

Contacto Amphos 21:
reynaldo.payano@amphos21.com

Mayo, 2016

|Elaborado:|Revisado:|Verificado:|Validado:|
|---|---|---|---|
|<br>Nicolás Jiménez<br>Reynaldo Payano|<br>Nicolás Jiménez|<br>Pierina Mirone|<br>Juan Castaño|

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

**Índice**

**1.** **INTRODUCCIÓN ................................................................................................................................... 1**

1.1 O BJETIVOS ......................................................................................................................................... 1

1.2 A NTECEDENTES ................................................................................................................................. 1

1.3 C ONTENIDO ........................................................................................................................................ 2

**2.** **DISEÑO GEOMÉTRICO ....................................................................................................................... 3**

2.1 D ESCRIPCIÓN G ENERAL DE LAS O BRAS P ROYECTADAS ..................................................................... 3

2.2 C AUDAL DE D ISEÑO ........................................................................................................................... 3

2.3 D IMENSIONAMIENTO H IDRÁULICO ..................................................................................................... 4

**3.** **ANÁLISIS DE SOCAVACIÓN Y SEDIMENTACIÓN ....................................................................... 9**

**4.** **MODELACIÓN HIDRÁULICA .......................................................................................................... 15**

4.1 M ETODOLOGÍA DE CÁLCULO DE HEC-RAS ..................................................................................... 15

4.2 R ESULTADOS DE LA MODELACIÓN HIDRÁULICA ............................................................................... 20

**5.** **CONCLUSIONES Y RECOMENDACIONES ................................................................................... 27**

**6.** **REFERENCIAS ..................................................................................................................................... 28**

**Anexos Asociados:**

Anexo C2 - Secciones Transversales para Q=0,19 m [3] /s

Anexo C3 - Secciones Transversales para Q=1,46 m [3] /s

Anexo C4 - Archivos Digitales del Modelo Hidráulico HEC-RAS

i

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

# 1. Introducción

A partir de los análisis hidrológicos desarrollados en el Anexo B, se ha determinado que el

Nuevo Depósito de Ripios de Lixiviación requiere considerar obras de manejo hidráulico,

con el fin de permitir un manejo apropiado de las escorrentías provenientes de una sub

cuenca pluvial al oriente del área del Proyecto. En dicho anexo se presentó la delimitación

geográfica de la cuenca pluvial y los cálculos hidrológicos necesarios para la estimación

de caudales máximos para diseño de infraestructura hidráulica.

En el presente documento se presentan los cálculos asociados al diseño hidráulico de

canalizaciones perimetrales, así como las verificaciones de condiciones de interés

particular de esta especialidad.

## 1.1 Objetivos

El objetivo general de este anexo es documentar el diseño de la infraestructura de

saneamiento perimetral que requiere el Proyecto del Nuevo Depósito de Ripios de

Lixiviación de la Planta Matta de ENAMI.

De forma complementaria, se establecen los siguientes objetivos específicos:

 - Dimensionar canalizaciones perimetrales para periodos de retorno de 100 años

 Verificar secciones transversales para periodos de retorno de 200 años

 Verificar velocidad de escurrimiento y requerimientos de revestimiento

 - Evaluar potencial erosivo y de arrastre de sedimentos

## 1.2 Antecedentes

Dentro de los antecedentes consultados para el desarrollo del presente documento, se

destacan los siguientes:

 Levantamiento topográfico del sitio. ENAMI. Marzo 2016.

# 1

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

 Anexo B Memoria de Cálculo Hidrología, Planta Matta, ENAMI. Amphos21. Mayo

2016.

 Diseño Geotécnico Nuevo Depósito de Ripios de Lixiviación. Geotecnia Ambiental.

Septiembre 2011.

## 1.3 Contenido

El contenido del documento se organiza de acuerdo a la siguiente estructura:

 Capítulo 1 - Introducción: Presentación del contexto general que justifica el

desarrollo del documento, así como objetivos y antecedentes de relevancia

mayor.

 Capítulo 2 - Diseño Geométrico: Desarrollo del cálculo que determina la

geometría de la sección transversal de las canalizaciones proyectadas.

 Capítulo 3 - Análisis de Socavación y Sedimentación: Contiene la verificación

de las condiciones críticas de velocidad de escurrimiento, que permiten evaluar

la necesidad de revestimiento y/o adopción de medidas para el control de

arrastre de sedimentos.

 Capítulo 4 - Modelación Hidráulica: Contiene el cálculo del eje hidráulico, tales

como condiciones de borde, coeficientes de rugosidad, coeficientes de

contracción y expansión, entre otros.

 Capítulo 5 - Conclusiones y Recomendaciones: Contiene las conclusiones y

recomendaciones finales para la construcción y mantenimiento de las obras

proyectadas.

 Capítulo 6 - Referencias: Listado de referencias técnicas utilizadas en el

desarrollo de este documento.

2

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

# 2. Diseño Geométrico

## 2.1 Descripción General de las Obras Proyectadas

Utilizando como base el diseño geométrico y el emplazamiento proyectado para el nuevo

depósito de ripios, se ha identificado que existe la necesidad de prevenir el ingreso de

escurrimientos pluviales desde sectores altos de la cuenca hacia el área en la cual dicha

instalación se emplazará. Para ello se propone la ejecución **de una obra de**

**regularización del cauce natural**, con objeto de mejorar las condiciones hidráulicas

actuales de la quebrada intermitente y rectificar la dirección de los flujos laterales hacia el

eje de la misma; previniendo así posibles afecciones de las obras proyectadas. De forma

complementaria se contempla excavar una zanja de desvío junto al sector nor-oriente del

depósito, que si bien cumple un rol menor dentro de las obras de manejo hidráulico

proyectadas, se recomienda su ejecución para desviar hacia el eje de la quebrada

principal la escorrentía que pudiese generarse en una micro-cuenca lateral.

La totalidad de las obras proyectadas tienen el propósito de favorecer el escurrimiento

pluvial hacia la red de drenaje natural. La regularización del cauce contempla conducir la

escorrentía hacia una canalización existente en el extremo sur del sitio del proyecto, cuyo

diseño no forma parte del alcance de este documento, sin embargo se procede a verificar

su capacidad de porteo con el fin de garantizar el correcto funcionamiento del sistema.

## 2.2 Caudal de Diseño

El análisis de las condiciones hidrológicas de la cuenca pluvial aportante ha permitido

determinar, en base a distintas metodologías de cálculo, los caudales máximos esperados

para distintos periodos de retorno seleccionados, los cuales se resumen a continuación.

El cálculo hidrológico detallado se presenta en el Anexo B.

3

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

|Col1|Tabla 1 - Caudal Instantáneo Máximo [m3/s]|Col3|Col4|
|---|---|---|---|
||**Método de Cálculo**|**Método de Cálculo**|**Método de Cálculo**|
|**T [años]**|**DGA-AC**|**Verni-King Modif.**|**Racional**|
|2|**0,04**|0,02|0,06|
|5|**0,07**|0,08|0,19|
|10|**0,10**|0,16|0,35|
|20|**0,12**|0,29|0,56|
|25|**0,13**|0,36|0,67|
|50|**0,16**|0,59|1,02|
|100<br>|**0,19**|0,91|1,46|

El caudal de diseño adoptado corresponde al calculado mediante el método DGA-AC,

aunque se incluyen verificaciones y comentarios de los resultados obtenidos con los otros

dos métodos.

## 2.3 Dimensionamiento Hidráulico

La obra proyectada de regularización del cauce natural contempla el mejoramiento de las

condiciones de porteo de la quebrada intermitente, mediante la excavación de una

sección transversal con capacidad para conducir al menos el caudal asociado a 100 años

de periodo de retorno.

Las pendientes longitudinales medias que actualmente existen en la quebrada NO se

modificarán. El diseño del perfil longitudinal se define de modo que la pendiente media se

ajuste a la del terreno.

Para el diseño hidráulico de la sección transversal típica se considera escurrimiento en

régimen uniforme, lo cual permite utilizar la ecuación de Manning:

_A_

=

_Q_

5
3

= ⋅

_m_

η

Donde:

4

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

A Área de la sección transversal al flujo de agua.

P m Perímetro mojado por el flujo de agua.

i Pendiente longitudinal del canal.

η Coeficiente de Manning.

Q Caudal que pasa a través de la sección transversal.

La selección de parámetros de diseño para el cálculo de la sección transversal se realiza

con criterio conservador, privilegiando la seguridad de la obra. Para el coeficiente de

Manning se considera que el escurrimiento ocurrirá en condiciones equivalentes a un

canal de tierra excavado mecánicamente, sin vegetación. Se adopta el valor medio, según

se destaca en la siguiente Figura.

**Figura 1 - Coeficientes de Manning Recomendados para Canales de Tierra.**

**Fuente: Manual de Carreteras, Vol II. MOP (2002).**

A continuación se resumen los parámetros de diseño adoptados para el cálculo hidráulico,

tanto para condición de pendiente longitudinal máxima como mínima, la cual controla la

velocidad de escurrimiento y la altura normal del escurrimiento.

5

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

**Tabla 2 - Parámetros de Diseño Regularización de Quebrada Intermitente**

|Parámetro|Valor|Comentario|
|---|---|---|
|Qn [m3/s]|0,04|Caudal normal, método DGA-AC, T=2 años.|
|Qd [m3/s]|0,19|Caudal máximo probable, método DGA-AC, T=100 años.|
|Qv [m3/s]|1,46|Caudal de verificación, método Racional, T=100 años.|
|i máx [m/m]|0,075|Pendiente máxima|
|i mín [m/m]|0,009|Pendiente mínima|
|Geometría|Trapecial|Sección transversal regularización proyectada|
|b [m]|1,0|Ancho basal en el fondo del trapecio|
|H / V|2 / 1|Talud recomendado para canal de tierra en suelo arenoso1 <br>|
|η <br>|0,028|~~Coeficiente de Manning para excavación mecánica, sin~~<br>vegetación2.|

La solución de la ecuación de Manning permite determinar la altura mínima requerida para

la sección típica de la regularización y verificar las condiciones de escurrimiento. En la

siguiente tabla se resumen los resultados obtenidos.

1 Según Tabla 3.705.2.A. Manual de Carreteras, Ver.2002, Ministerio de Obras Públicas, Chile.
2 Según Tabla 3.705.1.A. Manual de Carreteras, Ver.2002, Ministerio de Obras Públicas, Chile.

6

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

**Tabla 3 - Resultados Obtenidos para Diversos Escenarios de Escurrimiento**

|Escenario|Altura Normal<br>[m]|Velocidad<br>[m/s]|
|---|---|---|
|~~Caudal normal, pendiente~~<br>mínima<br>|0,07|0,5|
|~~Caudal normal, pendiente~~<br>máxima<br>|0,04|1,0|
|~~Caudal máximo probable,~~<br>pendiente mínima<br>|0,17|0,9|
|~~Caudal máximo probable,~~<br>pendiente máxima<br>|0,09|1,8|
|~~Caudal de verificación,~~<br>pendiente mínima<br>|0,49|1,5|
|~~Caudal de verificación,~~<br>pendiente máxima<br>|0,28|3,3|

A partir de la tabla anterior se identifica que para el escenario de **caudal máximo**

**probable** se genera una altura normal de escurrimiento no mayor a 20 cm y velocidades

máximas de 1,8 m/s. Para condición de caudal normal se observa que la velocidad de

escurrimiento no supera 1 m/s para la condición más crítica.

Dado lo anterior, además de las características esporádicas que caracterizan las

precipitaciones en el área de estudio, se acepta el diseño por velocidad, estableciendo

que el Titular del Proyecto debe efectuar inspección periódica y limpieza de las obras de

arte que corresponda en caso de detectarse pérdida de sección por sedimentación de

material fino.

Para brindar un grado de seguridad adecuado al proyecto se define una revancha mínima

de 20 cm sobre la altura normal máxima en condición de pendiente mínima y caudal de

verificación, esto es una altura útil mínima de 70 cm. Finalmente, considerando

requerimientos hidráulicos y criterios constructivos, se define la siguiente sección

transversal típica para la obra de regularización proyectada:

7

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

**Tabla 4 - Parámetros Constructivos Regularización Proyectada**

|Parámetro|Valor / Descripción|
|---|---|
|Geometría|Trapecial|
|Ancho Basal|1,0 [m]|
|Altura Mínima|1,0 [m]|
|Talud|2H/1V|
|Revestimiento|No|

La verificación de la sección transversal de diseño, considerando transporte de

sedimentos se aborda en la siguiente sección del documento.

8

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

# 3. Análisis de Socavación y Sedimentación

El objetivo principal de esta sección consiste analizar la potencialidad anual de arrastre de

sólidos para una seguridad de 95%, 80% y 60% en condiciones con y sin proyectos.

En este contexto, el transporte de sedimentos en las quebradas del norte de Chile,

principalmente en la III Región de Atacama, es un tema de gran relevancia dadas las

crecidas aluvionales registradas el año 2015. Por este motivo es importante realizar un

estudioso cuidadoso teniendo en cuenta el aporte de sedimentos o arrastre de sólidos

(Qs) que pueden causar los caudales líquidos (Ql) de precipitaciones máximas para

distintos periodo de retorno.

En este sentido, según López (2003), resulta complejo establecer una ecuación dinámica

general del transporte de sedimentos en un flujo de agua y sólidos, por lo que se han

desarrollado un gran número de ecuaciones de carácter empírico o semiempírico, válidas

de forma aproximada para las condiciones experimentales bajo las que fueron calibradas.

Sin embargo, es posible derivar ecuaciones para determinar el orden de magnitud de la

capacidad de transporte sólido (Qs) dado un caudal líquido (Ql) a partir de ecuaciones del

tipo:

Q **Q** = kkSS [mm] Q **Q**

Donde k y m son coeficientes que han sido previamente estimados por los autores

señalados en la Tabla 5.

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 9 Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta -->

**Tabla 5: - Fórmulas Empíricas Usadas en la Literatura para Determinar el Caudal de Sedimentos****

| Autor | Mizuyama<br>(1981) | Smart y<br>Jaeggi (1983) | Mizuyama y<br>shimohigashi<br>(1985) | Bathurst et al.<br>(1987) | Meunier (1989) | Rickenmann 1<br>(1990) | Rickenmann 2<br>(1990) | Rickenmann 3<br>(1990) | Rickenmann 4<br>(1991) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fórmula | Qs=5,5S2Ql | Qs= 2,5S1,6Ql<br> | Qs=7,35S2Ql | Qs=0,94S1,5Ql | Qs=6,3S2,02Ql | Qs=7,0S2,1Ql | Qs=9,26S2,3Ql<br> | Qs=6,35S2,1Ql | Qs=1,5S1,5Ql<br> |
| Observación | Se basa en el<br>uso de datos<br>de un canal<br>de laboratorio<br>de fuerte<br>pendiente<br>(entre el 5 y<br>25%) en<br>condiciones<br>de tensión de<br>corte muy<br>superior a la<br>tensión crítica<br>de las<br>partículas del<br>lecho | ~~Utilizan un~~<br>total de 77<br>datos propios<br>de laboratorio<br>y de 137 de<br>Meyer-Peter<br>y Müller<br>(1948)<br>obtienen la<br>expresión,<br>recomendada<br>para<br>pendientes<br>entre el 0,2 y<br>20%. | Obtienen la<br>expresión a<br>partir de las<br>experiencias<br>en cauces de<br>fuerte<br>pendiente<br>para fluido sin<br>concentración<br>significativa<br>de finos en<br>suspensión: | Proponen una<br>ecuación<br>modificada de<br>Schoklitsch: | Propone una<br>ecuación<br>producto de<br>una regresión <br>con 71 datos<br>de Smart y<br>Jaeggi (1983),<br>pero Meunier<br>limita el uso de<br>esta ecuación<br>a un rango de<br>pendientes<br>entre el 3 y el<br>5%. | Propone la<br>ecuación<br>basándose en<br>los 77 datos<br>de Smart y<br>Jaeggi (1983). | ~~Propone una~~<br>nueva<br>ecuación<br>basándose en<br>50 datos<br>propios<br>utilizando como<br>fluido una<br>suspensión de<br>arcilla de<br>densidad<br>variable con<br>pendientes<br>entre el 5 y el<br>25%. | <br>Desarrolla una<br>nueva<br>ecuación<br>integrando la<br>base de 77<br>datos de Smart<br>y Jaeggi (1983)<br>y los 50<br>propios. | ~~Integrando~~<br>datos propios<br>(Rickenmann,<br>1990) de<br>Smart y Jaeggi<br>(1983) y de<br>Meyer-Peter y<br>Müller (1948),<br>ascendiendo<br>en total a 252<br>recomienda la<br>ecuación, para<br>pendientes<br>entre 0,1 y<br>20%. |

<!-- Estadísticas: 2 filas, 10 columnas -->
<!-- Contexto posterior: -->
<!-- 10 Nota: Qs=Caudal de sedimento (m ~~[3]~~ /s); Ql=Caudal líquido (m ~~[3]~~ /s); S=Pendiente media del cauce principal (m/m) -->
<!-- FIN TABLA 5 -->


9

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

**Tabla 5 - Fórmulas Empíricas Usadas en la Literatura para Determinar el Caudal de Sedimentos**

|Autor|Mizuyama<br>(1981)|Smart y<br>Jaeggi (1983)|Mizuyama y<br>shimohigashi<br>(1985)|Bathurst et al.<br>(1987)|Meunier (1989)|Rickenmann 1<br>(1990)|Rickenmann 2<br>(1990)|Rickenmann 3<br>(1990)|Rickenmann 4<br>(1991)|
|---|---|---|---|---|---|---|---|---|---|
|Fórmula|Qs=5,5S2Ql|Qs= 2,5S1,6Ql<br>|Qs=7,35S2Ql|Qs=0,94S1,5Ql|Qs=6,3S2,02Ql|Qs=7,0S2,1Ql|Qs=9,26S2,3Ql<br>|Qs=6,35S2,1Ql|Qs=1,5S1,5Ql<br>|
|Observación|Se basa en el<br>uso de datos<br>de un canal<br>de laboratorio<br>de fuerte<br>pendiente<br>(entre el 5 y<br>25%) en<br>condiciones<br>de tensión de<br>corte muy<br>superior a la<br>tensión crítica<br>de las<br>partículas del<br>lecho|~~Utilizan un~~<br>total de 77<br>datos propios<br>de laboratorio<br>y de 137 de<br>Meyer-Peter<br>y Müller<br>(1948)<br>obtienen la<br>expresión,<br>recomendada<br>para<br>pendientes<br>entre el 0,2 y<br>20%.|Obtienen la<br>expresión a<br>partir de las<br>experiencias<br>en cauces de<br>fuerte<br>pendiente<br>para fluido sin<br>concentración<br>significativa<br>de finos en<br>suspensión:|Proponen una<br>ecuación<br>modificada de<br>Schoklitsch:|Propone una<br>ecuación<br>producto de<br>una regresión <br>con 71 datos<br>de Smart y<br>Jaeggi (1983),<br>pero Meunier<br>limita el uso de<br>esta ecuación<br>a un rango de<br>pendientes<br>entre el 3 y el<br>5%.|Propone la<br>ecuación<br>basándose en<br>los 77 datos<br>de Smart y<br>Jaeggi (1983).|~~Propone una~~<br>nueva<br>ecuación<br>basándose en<br>50 datos<br>propios<br>utilizando como<br>fluido una<br>suspensión de<br>arcilla de<br>densidad<br>variable con<br>pendientes<br>entre el 5 y el<br>25%.|<br>Desarrolla una<br>nueva<br>ecuación<br>integrando la<br>base de 77<br>datos de Smart<br>y Jaeggi (1983)<br>y los 50<br>propios.|~~Integrando~~<br>datos propios<br>(Rickenmann,<br>1990) de<br>Smart y Jaeggi<br>(1983) y de<br>Meyer-Peter y<br>Müller (1948),<br>ascendiendo<br>en total a 252<br>recomienda la<br>ecuación, para<br>pendientes<br>entre 0,1 y<br>20%.|

10

Nota: Qs=Caudal de sedimento (m ~~[3]~~ /s); Ql=Caudal líquido (m ~~[3]~~ /s); S=Pendiente media del cauce principal (m/m)

**Fuente: elaboración propia a partir de López (2003).**

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

Tal como se muestra en la tabla anterior, el caudal sólido está en función del caudal

líquido y es directamente proporcional a la pendiente media del cauce principal. Por lo

tanto, para el cálculo del caudal sólido se tomarán en cuenta las fórmulas presentadas

anteriormente, cuyos datos de entrada serán: la pendiente media del cauce estimada en

un 9% (Anexo B. Estudio Hidrológico) y los datos de caudal instantáneo máximo (caudal

líquido) para distintos periodos de retorno que ya fueron estimados en el Anexo B. Estudio

Hidrológico.

**Tabla 6 - Caudal Instantáneo Máximo o Caudal Líquido estimado para distintos periodo de**

|Col1|retorno [m3/s]|Col3|Col4|
|---|---|---|---|
||**Método de Cálculo**<br>|**Método de Cálculo**<br>|**Método de Cálculo**<br>|
|**T [años]**|**DGA-AC**|~~**Verni-King**~~<br>**Modificado**|**Racional**|
|2|**0,04**|0,02|0,06|
|5|**0,07**|0,08|0,19|
|10|**0,10**|0,16|0,35|
|20|**0,12**|0,29|0,56|
|25|**0,13**|0,36|0,67|
|50|**0,16**|0,59|1,02|
|100|**0,19**|0,91|1,46|

Según la tabla anterior, el caudal instantáneo máximo más alto o desfavorable

corresponde al estimado por el Método Racional. Por lo tanto, se adoptarán dichos

valores como caudal líquido para estimar el caudal de sedimentos para distintos periodo

de retorno. En la Tabla 7 se presentan los resultados del caudal de sedimento estimado.

11

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

**Tabla 7 - Caudal de Sedimentos [m3/s] Estimado Mediante Distintas Fórmulas Empíricas**

|T<br>[años]|Racional<br>adoptado<br>(Ql)|Mizuyama<br>(1981)|Smart y<br>Jaeggi<br>(1983)|Mizuyama y<br>shimohigashi<br>(1985)|Bathurst et al.<br>(1987)|Meunier<br>(1989)|Rickenmann<br>1 (1990)|Rickenmann<br>2 (1990)|Rickenmann<br>3 (1990)|Rickenmann<br>4 (1991)|Promedio<br>(Qtotal)<br>(m3/s)|
|---|---|---|---|---|---|---|---|---|---|---|---|
|2|**0,06**|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|**0,00**|
|5|**0,19**|0,01|0,01|0,01|0,00|0,01|0,01|0,01|0,01|0,01|**0,01**|
|10|**0,35**|0,02|0,02|0,02|0,01|0,02|0,02|0,01|0,01|0,01|**0,02**|
|20|**0,56**|0,02|0,03|0,03|0,01|0,03|0,02|0,02|0,02|0,02|**0,02**|
|25|**0,67**|0,03|0,03|0,04|0,02|0,03|0,03|0,02|0,03|0,03|**0,03**|
|50|**1,02**|0,05|0,05|0,06|0,03|0,05|0,05|0,04|0,04|0,04|**0,04**|
|100|**1,46**|0,07|0,08|0,09|0,04|0,07|0,07|0,05|0,06|0,06|**0,06**|

12

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

Considerando los datos anteriores, se ha estimado la potencialidad de arrastre de

sólidos para distintos periodo de retorno y para una seguridad de 95%, 80% y 60%.

Estos resultados se presentan resumidos en la Tabla 8. En dicha tabla se puede

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- de 0,03 m3/s (30 l/s aprox.) hasta 0,12 m3/s (120 l/s aprox.) para un periodo de retorno de 10 y 100 años respectivamente considerando un factor de seguridad del 95%. -->

**Tabla 8: - Caudal de Diseño de Sedimentos [m** **[3]** **/s] para Distintos Factores de Seguridad****

| T [años] | Factor de seguridad | Col3 | Col4 |
| --- | --- | --- | --- |
| **T [años**] | **95%** | **80%** | **60%** |
| 2 | 0,01 | 0,00 | 0,00 |
| 5 | 0,02 | 0,01 | 0,01 |
| 10 | 0,03 | 0,03 | 0,02 |
| 20 | 0,05 | 0,04 | 0,04 |
| 25 | 0,05 | 0,05 | 0,04 |
| 50 | 0,09 | 0,08 | 0,07 |
| 100 | **0,12** | 0,11 | 0,10 |

<!-- Estadísticas: 8 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Para verificación de la sección crítica de la obra de regularización proyectada, se determina por lo tanto un volumen total de escurrimiento sumando el caudal líquido y el -->
<!-- FIN TABLA 8 -->


apreciar que el caudal de sólidos generados por los caudales líquidos son de

relevancia menor en términos de diseño de obras hidráulicas en el Proyecto, variando

de 0,03 m3/s (30 l/s aprox.) hasta 0,12 m3/s (120 l/s aprox.) para un periodo de retorno

de 10 y 100 años respectivamente considerando un factor de seguridad del 95%.

**Tabla 8 - Caudal de Diseño de Sedimentos [m** **[3]** **/s] para Distintos Factores de Seguridad**

|T [años]|Factor de seguridad|Col3|Col4|
|---|---|---|---|
|**T [años**]|**95%**|**80%**|**60%**|
|2|0,01|0,00|0,00|
|5|0,02|0,01|0,01|
|10|0,03|0,03|0,02|
|20|0,05|0,04|0,04|
|25|0,05|0,05|0,04|
|50|0,09|0,08|0,07|
|100|**0,12**|0,11|0,10|

Para verificación de la sección crítica de la obra de regularización proyectada, se

determina por lo tanto un volumen total de escurrimiento sumando el caudal líquido y el

caudal de sólidos en suspensión, lo cual para un periodo de retorno de 100 años y el

método más conservador (racional), queda representado por el siguiente caudal

máximo probable:

QQ ll+ss = 1,46 + 0,12 = 1,58 [m [3] /s]

13

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

La sección transversal se verifica mediante la determinación de la altura de

escurrimiento para la sección más crítica, esto es para máximo caudal y pendiente

longitudinal mínima:

**Tabla 9 - Verificación Final Sección Transversal Típica**

|Escenario|Altura Escurrimiento<br>Normal [m]|Altura Canal<br>Según Diseño [m]|
|---|---|---|
|~~Método racional, T=100 años,~~<br>pendiente mínima, caudal<br>líquido + sedimentos<br>|0,50|1,00|

Dado que la altura normal calculada es menor a la altura de diseño, se verifica la

sección.

14

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

# 4. Modelación Hidráulica

El cálculo del eje hidráulico de la quebrada intermitente en el tramo de interés donde se

emplaza el proyecto (ver Anexo B. Memoria de Cálculo Hidrología) se determinó

mediante la utilización del software HEC-RAS 5.0 del U.S. Army Corps of Engineers

Hydrologic Engineering Center.

Los fundamentos teóricos aplicados en este programa ya han sido bien explicados por

DGA (2010) y USACE (2016), los cuales mencionan que el código trabaja con el

método de etapas fijas para pronosticar la dinámica de los niveles de aguas producidos

por eventos hidrometeorológicos extremos como las grandes crecidas o aluviones.

## 4.1 Metodología de cálculo de HEC-RAS

De acuerdo a varios autores (Bladé _et al._, 2009; DGA, 2010; Torres y González, 2011)

la estructura de simulación hidráulica del HEC-RAS permite estimar el comportamiento

de la dinámica del recurso hídrico y los efectos hidráulicos que pudieran generarse

tanto en el cauce como en proyectos próximos a este. Por lo tanto, conocida la

geometría del cauce en términos de perfiles transversales y de planta del sector, su

caracterización rugosa (coeficiente de rugosidad), el caudal y la altura de escurrimiento

en una sección inicial 1, se determina por iteraciones la altura en una sección 2,

ubicada a una distancia fija conocida, mediante el balance de Bernoulli o energía

específica. Dicho balance puede representarse como:

2
h 2 + αα 2 ∗ [vv] [2]

2
gg

2
= h 1 + αα 1 ∗ [vv] [1]

2
gg

+ HH ee

Donde:

2
HH ee = LL∗SS [ഥ] ff + CC∗ 2 ∗ [vv] [2]

2

ቤαα gg

2
−αα 1 ∗ [vv] [1]

2
gg

ቤ

15

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

Siendo:

_**H**_ _**e**_ la pérdida total de energía entre las secciones transversales.

_**h**_ _**1**_ _**y h**_ _**2**_ la cota superficial en las secciones transversales 1 y 2.

_**V**_ _**1**_ _**y V**_ _**2**_ la velocidades media en las secciones transversales 1 y 2.

**α** **1** **y α** **2** corresponden a los coeficientes que afectan las alturas de velocidad,

para compensar la incerteza de suponer una distribución uniforme de la

velocidad media a su correspondiente sección.

_**L**_ es la distancia entre las secciones.

_**S**_ _**f**_ es la pendiente de la línea de energía entre secciones. HEC-RAS presenta

diversas ecuaciones para estimar este valor. En este caso, lo recomendable

para un régimen fluvial es la ecuación que promedia la pendiente evaluada en

cada sección por separado, suponiendo flujo normal en cada una de ellas.

(Otras alternativas son la media geométrica, la media armónica y la de

conductancia promedio).

_**C**_ es el coeficiente de expansión o contracción del flujo. Se considera valores de

0,3 y 0,1 respectivamente, para cambios de sección natural, que son

detectados por el programa según la variación de la velocidad media de una

sección a otra, y valores de 0,5 y 0,3 para expansión y contracción asociados a

la presencia de la Obra de Arte.

Para lograr el balance anterior, es necesario tener bien definido factores tales como: el

coeficiente de rugosidad de Manning, el coeficiente de expansión y contracción, las

secciones transversales, las condiciones de borde y datos de terreno para calibrar el

modelo.

 **Coeficiente de rugosidad**

Un factor importante para el programa es el valor del coeficiente de rugosidad, el cual

ya ha sido previamente presentado en el apartado 2.3 de este documento. Los valores

adoptados para las condiciones de un canal excavado mecánicamente o dragado

oscilan entre 0,025 ( _n_ minímo), 0,028 ( _n_ medio) y 0,033 ( _n_ máximo) respectivamente.

16

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

A continuación se presentan algunas fotografías del sitio que, junto con el trabajo de

terreno efectuado, justifican el coeficiente de rugosidad adoptado para la modelación

hidráulica.

**Figura 2 - Fotografías del cauce intermitente a modelar.**

17

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

 **Coeficiente de expansión y contracción**

En el tramo de estudio, se han determinado los valores más apropiados para la

contracción y expansión necesarios para modelar las pérdidas de energía del flujo.

Para la expansión se considera un coeficiente de 0,3; por su parte el coeficiente de

contracción se ha considerado 0,1; debido a que en el cauce se producen

principalmente cambios de sección natural.

 - **Secciones transversales**

Las secciones transversales se han obtenido mediante el uso del software AutoCAD y

el levantamiento topográfico realizado en la zona del proyecto. En total se han extraído

22 perfiles cada 50 m en una longitud de 1,04 km. En la figura a continuación se

presenta un esquema en planta de la ubicación y distancia de cada sección

transversal, según el modelo HEC-RAS. El detalle de cada una de las secciones

transversales se presenta en los Anexo 7.1 y 7.2.

**Figura 3 - Esquema en planta del modelo HEC-RAS: secciones transversales y tramo de**

**interés.**

18

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

 - **Condiciones de borde**

Con el fin de establecer las condiciones de borde del eje hidráulico y su

correspondiente determinación de la lámina libre de agua, se ha considerado un

régimen subcrítico. Esta condición de contorno se ha establecido de acuerdo a los

resultados obtenidos en el dimensionamiento hidráulico del apartado 2.3 y los datos de

terreno. La condición inicial de cálculo corresponde a la altura normal tanto al principio

como el fin del tramo. Como se aprecia en la figura a continuación, la pendiente (i) es

relativamente uniforme y oscila entre 0,009 m/m (i mín) y 0,075 m/m (i máx). No

obstante lo anterior, con objeto de optimizar el modelo se considerará la pendiente

calculada automáticamente por HEC-RAS en las distintas secciones elegidas a través

del calado crítico (o _critical depth_ ).

**Figura 4 - Perfil Longitudinal Modelo HEC-RAS**

 - **Calibración del modelo**

Considerando que la zona de estudio corresponde a una **cuenca sin información**

**fluviométrica** (sin registro de caudales), donde se producen escurrimientos

superficiales intermitentes sólo en épocas de lluvias intensas, el modelo será calibrado

19

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

considerando la información obtenida de la campaña de terreno a la zona de estudio,

específicamente en lo relacionado a niveles máximos alcanzados por las crecidas

aluvionales.

## 4.2 Resultados de la modelación hidráulica

De acuerdo a los resultados del estudio hidrológico (Anexo B) y los cálculos efectuados

en el diseño geométrico de las estructuras hidráulicas (Capítulo 2 de este documento),

se generó un modelo de eje hidráulico para caudales de 0,19 m [3] /s (caudal de diseño

adoptado para T=100 años) y 1,46 m [3] /s (caudal de verificación).

La modelización hidráulica efectuada en el software HEC-RAS permitió evaluar las

condiciones de flujo para las diferentes configuraciones de caudales y secciones

transversales a lo largo del tramo, estudiando los valores simulados para niveles de

agua, profundidades de flujo y velocidades de escurrimiento, entre otras variables.

La simulación se realizó considerando un régimen subcrítico en todo el tramo de

interés y un calado crítico (critical depth) como condición de borde para los diferentes

escenarios. Los resultados obtenidos se presentan en los Anexos B2, B3 y B4

(Archivos digitales). Adicionalmente, en las Figuras 5, 6, 7 y 8; se muestran ejemplos

de los resultados que ofrece el programa.

20

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

**Figura 5 - Ejemplo de las Secciones Transversales Modeladas**

21

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

**Figura 6 - Ejemplo del Perfil Longitudinal Resultante de la Modelación en HEC-RAS**

22

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

**Figura 7 - Resumen de Resultados de Todas las Variables Calculadas por HEC-RAS**

**(Caudal Q=0,19 m** **[3]** **/s)**

De acuerdo a la figura anterior, la simulación es aceptable en términos de los

resultados esperados para el tramo analizado. A saber la pendiente resultante oscila

entre 0,009 (i min) y 0, 075 (i máx), que fueron las elegidas para el dimensionamiento

hidráulico del apartado 2.3. Para condición del caudal simulado se observa que la

velocidad de escurrimiento oscila entre 0,56 y 1,04 m/s para la condición más crítica y

el número de Froude resultante es menor o igual a 1 en todas secciones analizadas.

Esto es coherente con lo señalado anteriormente en la Tabla 3. Asimismo, se identifica

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 6 Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta -->

**Tabla 3: - Resultados Obtenidos para Diversos Escenarios de Escurrimiento****

| Escenario | Altura Normal<br>[m] | Velocidad<br>[m/s] |
| --- | --- | --- |
| ~~Caudal normal, pendiente~~<br>mínima<br> | 0,07 | 0,5 |
| ~~Caudal normal, pendiente~~<br>máxima<br> | 0,04 | 1,0 |
| ~~Caudal máximo probable,~~<br>pendiente mínima<br> | 0,17 | 0,9 |
| ~~Caudal máximo probable,~~<br>pendiente máxima<br> | 0,09 | 1,8 |
| ~~Caudal de verificación,~~<br>pendiente mínima<br> | 0,49 | 1,5 |
| ~~Caudal de verificación,~~<br>pendiente máxima<br> | 0,28 | 3,3 |

<!-- Estadísticas: 6 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- A partir de la tabla anterior se identifica que para el escenario de **caudal máximo** **probable** se genera una altura normal de escurrimiento no mayor a 20 cm y velocidades -->
<!-- FIN TABLA 3 -->


que para el escenario de **caudal máximo probable** (Q=0,19 m [3] /s) se genera una

altura de la lámina de agua que no supera los 20 cm (la altura de agua máxima de 12

cm se registró en sección 350).

23

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

**Figura 8 - Resumen de resultados de todas las variables calculadas por HEC-RAS**

**(Caudal Q=1,46 m** **[3]** **/s)**

De acuerdo a los datos mostrados en la figura anterior, la simulación es aceptable en

términos de los resultados esperados para el tramo analizado. A saber la pendiente

resultante oscila entre 0,009 (i min) y 0, 075 (i máx) que fueron las elegidas para el

dimensionamiento hidráulico del apartado 2.3. Para condición del caudal simulado se

observa que la velocidad de escurrimiento alcanza 1,38 m/s para la condición más

crítica y el número de Froude resultante oscila entre 0,20 y 1,02 en las secciones

analizadas. Asimismo, se identifica que para el escenario de **caudal máximo probable**

(Q=1,46 m [3] /s) se genera una altura de la lámina de agua de 19 cm, la cual fue

registrada en sección 250.

 - **Calibración del modelo**

Tal como se mencionó anteriormente, el tramo de interés pertenece a una cuenca sin

información fluviométrica, por lo que el modelo se ha calibrado considerando la

información obtenida de la campaña de terreno efectuada entre los meses de marzo y

abril del año 2016. En dicha campaña se reconocieron distintas alturas de aguas

24

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

(huellas hídricas de aluviones) que oscilaron entre 20 y 40 cm. Para efectos

conservadores el modelo será calibrado considerando la altura máxima de agua

registrada, es decir, hasta un límite de 40 cm y un periodo de retorno de 100 años. En

las figuras siguientes se presentan los resultados de la calibración, donde se muestra

que el nivel máximo modelado para caudales de 0,19 y 1,46 m [3] /s fue de 12 y 19 cm,

respectivamente.

**Figura 9 - Resultados de Calibración para Simulación con Q=0,19 m** **[3]** **/s**

**Figura 10 - Resultados de Calibración para Simulación con Q=1,46 m** **[3]** **/s**

25

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

A continuación se presenta un set de fotografías utilizadas como referencia para la

estimación de niveles máximos registrados.

**Figura 11 - Registro Fotográfico de los Niveles Máximos Alcanzados por el Agua en los**

**Puntos Aguas Abajo del Tramo de Interés.**

26

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

# 5. Conclusiones y Recomendaciones

 Para el manejo apropiado de la escorrentía pluvial afluente al área del proyecto

se proyectan obras de regularización en cauce natural, consistente en una

excavación de sección trapecial de 1 metro de base, 1 m de profundidad

mínima y taludes 2H:1V, sin revestimiento.

 La regularización proyectada permitirá conducir de forma eficiente y segura las

escorrentías pluviales generadas para todos los escenarios verificados,

incluyendo el volumen aportado por arrastre de sedimentos.

 Lo anterior se confirmó mediante modelación del eje hidráulico del cauce en

software HEC-RAS, con el cual se evaluó la respuesta del tramo analizado ante

un evento de precipitación extrema. Mediante dicho modelo hidráulico se

determinó que la altura máxima de agua en la sección crítica del cauce, para un

caudal de 0,19 m [3] /s (obtenido por el Método DGA-AC para T=100 años), es de

12 cm; mientras que para un caudal de verificación de 1.46 m [3] /s es de 19 cm.

 Debido a lo anterior se verifican las secciones de diseño proyectadas.

 Como medida de prevención se indica que, previo y posterior a eventos de

precipitación intensa, el Titular verificará las condiciones de las canalizaciones

existentes y proyectadas, con el fin de evitar pérdida de capacidad de porteo

por sedimentación de material fino.

27

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

# 6. Referencias

 - Ministerio de Obras Públicas (2002). _Manual de Carreteras_ . Volumen II. MOP.

 DGA (2010). _Análisis de metodología y determinación de caudales de reserva_

_turísticos_ . Realizado por Aquaterra Ingenieros Limitada. SIT N°206. MOP.

 - Chow V. T., Maidment D. & Mays L. (1994). _Hidrología Aplicada_ . McGraw-Hill.

Cap. 11-12.

 BATHURST, J.C.; GRAF, W.H. y CAO, H.H. (1987). _Bed load discharge_

_equations for steep mountains rivers_, en Thorne, C.R.; Bathurst, J.C. y Hey,

R.D. (Ed.): Sediment transport in gravel-bed rivers. Wiley, pp. 453-491.

 Bladé E.; Sánchez-Juny M.; Sánchez H.P.; Niñerola D. y Gómez M. (2009).

_Modelación numérica en ríos en régimen permanente y variable. Una visión a_

_partir del modelo HEC-RAS_ . Colección Politext 190, 216 pp.

 EINSTEIN, H.A. (1950). _The Bed-Load Function for Sediment Transportation in_

_Open Channel Flow_, en Technical Bulletin No. 1026. U. S. Department of

Agriculture, Washington D. C.

 - GRAF, W.H. (1971). _Hydraulics of sediment transport_ . Mc Graw-Hill, New York.

 LÓPEZ ALONSO, R. (2003). Fórmulas para el cálculo aproximado de la

capacidad de transporte de sedimentos en ríos de montaña. Revista Cimbra,

Artículos de opinión.

 - MEUNIER, M. (1989). _Essai de synthèse des connaissances en érosion et_

_hydraulique torrentielle_, en La Houille Blanche. 5: 361-375.

 MEYER-PETER, E. y MÜLLER, R. (1948): “Formulas for bed-load transport”, en

Proc.of the second meeting of the IAHSR. Estocolmo, pp. 39-64.

 - MIZUYAMA, T. (1981). _An intermediate phenomenon between debris flow and_

_bed load transport_ . AIHS, 132.

 - MIZUYAMA, T. y SHIMOHIGASHI, H (1985). _Influence of fine sediment_

_concentracion on sediment transport rates_, en Jap. Civil Eng. Journal. 27-1.

 RICKENMANN, D. (1990): Bedload transport capacity of slurry flows at steep

slopes. Mitteilung VAW 103. Zürich.

28

Anexo C -Diseño Hidráulico de Canalización Perimetral para el Nuevo Depósito de Ripios de Lixiviación, Planta Matta

 RICKENMANN, D. (1991) "Hyperconcentrated flow and sediment at steep

slopes", en J. of Hydr. Eng., Vol.117 (11): 1419-1439.

 SMART G.M. y JAEGGI M. (1983): Sediment transport on steep slopes.

Mitteilung VAW. 64. Zürich.

 Torres E. y González E. (2011). _Aplicación del modelo de simulación hidráulica_

_HEC-RAS para la emisión de pronósticos hidrológicos de inundaciones en_

_tiempo real, en la cuenca media del río Bogotá - sector Alicachin_ . Revista

Ingeniero Libre N°10.

 U.S. Army Corps of Engineers, USACE (2016). _HEC-RAS River Analysis_

_System: Hydraulic Reference Manual_ . Version 5.0. Hydrologic Engineering

Center.

29

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2: - Parámetros de Diseño Regularización de Quebrada Intermitente****

| Parámetro | Valor | Comentario |
| --- | --- | --- |
| Qn [m3/s] | 0,04 | Caudal normal, método DGA-AC, T=2 años. |
| Qd [m3/s] | 0,19 | Caudal máximo probable, método DGA-AC, T=100 años. |
| Qv [m3/s] | 1,46 | Caudal de verificación, método Racional, T=100 años. |
| i máx [m/m] | 0,075 | Pendiente máxima |
| i mín [m/m] | 0,009 | Pendiente mínima |
| Geometría | Trapecial | Sección transversal regularización proyectada |
| b [m] | 1,0 | Ancho basal en el fondo del trapecio |
| H / V | 2 / 1 | Talud recomendado para canal de tierra en suelo arenoso1 <br> |
| η <br> | 0,028 | ~~Coeficiente de Manning para excavación mecánica, sin~~<br>vegetación2. |

**Tabla 4: - Parámetros Constructivos Regularización Proyectada****

| Parámetro | Valor / Descripción |
| --- | --- |
| Geometría | Trapecial |
| Ancho Basal | 1,0 [m] |
| Altura Mínima | 1,0 [m] |
| Talud | 2H/1V |
| Revestimiento | No |

**Tabla 6: - Caudal Instantáneo Máximo o Caudal Líquido estimado para distintos periodo de****

| Col1 | retorno [m3/s] | Col3 | Col4 |
| --- | --- | --- | --- |
|  | **Método de Cálculo**<br> | **Método de Cálculo**<br> | **Método de Cálculo**<br> |
| **T [años]** | **DGA-AC** | ~~**Verni-King**~~<br>**Modificado** | **Racional** |
| 2 | **0,04** | 0,02 | 0,06 |
| 5 | **0,07** | 0,08 | 0,19 |
| 10 | **0,10** | 0,16 | 0,35 |
| 20 | **0,12** | 0,29 | 0,56 |
| 25 | **0,13** | 0,36 | 0,67 |
| 50 | **0,16** | 0,59 | 1,02 |
| 100 | **0,19** | 0,91 | 1,46 |

**Tabla 7: - Caudal de Sedimentos [m3/s] Estimado Mediante Distintas Fórmulas Empíricas****

| T<br>[años] | Racional<br>adoptado<br>(Ql) | Mizuyama<br>(1981) | Smart y<br>Jaeggi<br>(1983) | Mizuyama y<br>shimohigashi<br>(1985) | Bathurst et al.<br>(1987) | Meunier<br>(1989) | Rickenmann<br>1 (1990) | Rickenmann<br>2 (1990) | Rickenmann<br>3 (1990) | Rickenmann<br>4 (1991) | Promedio<br>(Qtotal)<br>(m3/s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | **0,06** | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | **0,00** |
| 5 | **0,19** | 0,01 | 0,01 | 0,01 | 0,00 | 0,01 | 0,01 | 0,01 | 0,01 | 0,01 | **0,01** |
| 10 | **0,35** | 0,02 | 0,02 | 0,02 | 0,01 | 0,02 | 0,02 | 0,01 | 0,01 | 0,01 | **0,02** |
| 20 | **0,56** | 0,02 | 0,03 | 0,03 | 0,01 | 0,03 | 0,02 | 0,02 | 0,02 | 0,02 | **0,02** |
| 25 | **0,67** | 0,03 | 0,03 | 0,04 | 0,02 | 0,03 | 0,03 | 0,02 | 0,03 | 0,03 | **0,03** |
| 50 | **1,02** | 0,05 | 0,05 | 0,06 | 0,03 | 0,05 | 0,05 | 0,04 | 0,04 | 0,04 | **0,04** |
| 100 | **1,46** | 0,07 | 0,08 | 0,09 | 0,04 | 0,07 | 0,07 | 0,05 | 0,06 | 0,06 | **0,06** |

**Tabla 9: - Verificación Final Sección Transversal Típica****

| Escenario | Altura Escurrimiento<br>Normal [m] | Altura Canal<br>Según Diseño [m] |
| --- | --- | --- |
| ~~Método racional, T=100 años,~~<br>pendiente mínima, caudal<br>líquido + sedimentos<br> | 0,50 | 1,00 |
