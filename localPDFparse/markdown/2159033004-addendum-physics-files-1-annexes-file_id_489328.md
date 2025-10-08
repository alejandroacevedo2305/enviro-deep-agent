---
title: Sin título
author: Envirometrika
date: D:20231129141739-03'00'
language: es
type: report
pages: 77
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - PROYECTO: P7056 - Modelación de Impacto Odorante
  - Fecha: Noviembre 2023
  - SOLICITANTE: Volta Servicios SpA
  - At: Sra. Deyanira Henríquez
-->

# PROYECTO: P7056 - Modelación de Impacto Odorante

# Fecha: Noviembre 2023

# SOLICITANTE: Volta Servicios SpA

# At: Sra. Deyanira Henríquez

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 2 de 77

Modelación de Impacto Odorante
Nombre Ficha:
Plataforma de Economía Circular Volta Los Lagos

Reporte no: Versión Final 2.0

Código de proyecto: P 7056

Palabras claves

Área de influencia, concentración de olor, dispersión, emisión,
frecuencia de percepción, dispersión, modelación odorante, tasa
de emisión odorante.

Preparado a petición de: Volta Servicios SpA

Contacto: Sra. Deyanira Henríquez - Jefe de Proyecto

Preparado por:

Autores:

Envirometrika
Cordillera 331, Bodega C9, Quilicura, Santiago
Arturo Prat 199 -Torre A of 1401 Concepción  56 41 383 3978
[e-mail: info@envirometrika.com](mailto:info@envirometrika.com)
[www.envirometrika.com](http://www.envirometrika.com/)

Benjamín Rosenblitt

Firmado y aprobado por: Envirometrika por Héctor Vergara

Fecha:

Noviembre 2023 (emisión reporte borrador 0.1)
Noviembre 2023 (emisión reporte final 1.0)
Noviembre 2023 (emisión reporte final 2.0)

CONTROL DE CAMBIOS www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 3 de 77

**CONTROL DE CAMBIOS**

|DESARROLLADO POR:|FIRMA|ÁREA|
|---|---|---|
|Benjamín Rosenblitt||Modelación y Simulación|

|REVISADO POR:|FIRMA|ÁREA|
|---|---|---|
|Ricardo Guerra||Modelación y Simulación|

|APROBADO POR:|FIRMA|ÁREA|
|---|---|---|
|Héctor Vergara||Gerencia|

**REVISIONES**

|REVISIÓN|TIPO DE CAMBIO|FECHA|
|---|---|---|
|V 0.1|1a revisión reporte borrador para<br>entrega al cliente|10 de noviembre de 2023|
|V 1.0|Envío reporte final a cliente|27 de noviembre de 2023|
|V 2.0|Envío reporte final a cliente|29 de noviembre de 2023|

CONTROL DE CAMBIOS www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 4 de 77

**GLOSARIO**

GLOSARIO www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 5 de 77

GLOSARIO www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 6 de 77

Fuentes:

[1] Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA, 2017.

[2] Guía para el Uso de Modelos de Calidad del Aire en el SEIA, 2023.

[3] Air Quality Dispersion Modeling - Related Model Support Programs, EPA.

GLOSARIO www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 7 de 77

**RESUMEN EJECUTIVO**

El presente reporte, corresponde a los resultados de la
Modelación de Impacto Odorante solicitado por Volta
Servicios SpA, para el proyecto “Plataforma de Economía
Circular Volta Los Lagos”. Esto bajo el marco de la
Declaración de Impacto Ambiental (DIA) sometida al
Sistema de Evaluación de Impacto Ambiental (SEIA).

El proyecto contempla la futura instalación de un centro
de tratamiento de residuos sólidos domésticos y
orgánicos, proporcionando un servicio integral en cuanto
al manejo y tratamiento de residuos, adoptando
estándares actualizados, tecnologías de alto nivel y
acciones que permitan una gestión eficiente, priorizando
por la valorización de los residuos.

La instalación se localizará fuera del límite urbano de la
comuna de Maullín, provincia de Llanquihue, Región de
Los Lagos, específicamente centrada en las coordenadas
UTM (WGS-84, Huso 18 Sur) 644.590 [m] Este y
5.393.748 [m] Sur.

Figura 1 - Localización del Proyecto

Fuente: Elaboración propia, a partir de Google Earth 2023.

El objetivo fue determinar el alcance odorante de la futura
Plataforma de Economía Circular, basado en las
condiciones operacionales definidas por el Titular.

El plan de trabajo consideró el desarrollo de las siguientes
etapas:

1. Recopilación de antecedentes.
2. Identificación y caracterización de fuentes emisoras.
3. Revisión de emisiones de referencia aplicables.

4. Preparación de datos de entrada al software de

modelación.
5. Estimación del área de influencia para la componente

olor.
6. Cuantificar y evaluar impacto en receptores.
7. Informe de resultados.

Basado en las partes, obras y acciones declaradas por el
solicitante para el proyecto, se identificaron 16 fuentes
con emisión de olor al aire ambiente durante la fase de
operación, de acuerdo con la siguiente tabla:

Tabla 1 - Fuentes de emisión

|ID|Nombre fuente|EO<br>[ou/m2s]<br>E|TEO<br>[ou/s]<br>E|
|---|---|---|---|
|1|Sist. de abatimiento de olores<br>galpón de compostaje - Biofiltro|12,5\a|352,80|
|2|Trincheras|0,83\b|5.736,96|
|3|Patio de maduración|0,40\c|1.200,00|
|4|Chimenea scrubber (calcinación)|31.100,91\d|24.426,60|
|5|Sist. de abatimiento de olores<br>planta de carbonato - Biofiltro|96,38\a|2.822,02|
|6|Sist. de abatimiento de olores<br>planta de biogás - Biofiltro|20,87\a|611,01|
|7|Deshidratador|0,32\d|1,20|
|8|Laguna de digestato|0,32\d|2.592,00|
|9|Estanque ecualizador 1|3,80\d|41,75|
|10|Estanque ecualizador 2|3,80\d|41,75|
|11|Estanque ecualizador 3|3,80\d|41,75|
|12|Reactor de trat. aerobio SBR 1-1|19,08\d|1.431,00|
|13|Reactor de trat. aerobio SBR 1-2|19,08\d|1.431,00|
|14|Reactor de trat. aerobio SBR 2-1|19,08\d|1.431,00|
|15|Reactor de trat. aerobio SBR 2-2|19,08\d|1.431,00|
|16|Camiones de transporte|0,05|1.790,40|

\a Implementación de biofiltro de eficiencia -90%TEO.
\b Implementación de lámina cobertora con eficiencia de remoción de

olores -90%TEO.
\c Implementación de lámina cobertora con eficiencia de remoción de

olores -75%TEO.
\d Emisión de olor directa al ambiente (sin tratamiento).

La representación operacional y estructural de las fuentes,
siguió los lineamientos y recomendaciones descritos en la
Guía Para el Uso de Modelos de Calidad del Aire en el

RESUMEN EJECUTIVO www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 8 de 77

SEIA [1] y la Guía para la Predicción y Evaluación de
Impactos por Olor en el SEIA [2] .

Debido a que la Plataforma de Economía Circular
corresponde a un proyecto inexistente, es aplicable el uso
de emisiones de referencia provenientes de instalaciones
y/o unidades de procesos asimilables a la futura planta.
Las emisiones de referencia utilizadas fueron obtenidas a
partir de una recopilación de estudios publicados en la
plataforma del SEIA, seleccionando aquellos estudios
realizados en cumplimiento a la normativa vigente de
muestreo NCh3386:2015 [3] y de análisis olfatométrico
NCh3190:2010 [4] . En una segunda etapa, se evaluó la
similitud las fuentes de referencia respecto a las del
proyecto, considerando como criterio: tipo de fuente,
características estructurales y operacionales, entre otras.

Finalmente, fueron seleccionadas aquellas emisiones de
referencia con el mayor grado de ajuste al proceso
descrito para las fuentes odorantes identificadas en el
Proyecto.
Para aquellas unidades de proceso donde no fue posible la
caracterización de emisiones en base a estudios
olfatométricos públicos nacionales, se consultaron
referencias internacionales en cumplimiento a los criterios
normativos tanto de muestreo como de análisis
olfatométrico.

La evaluación del proyecto, consideró lo señalado en la
Guía para la Predicción y Evaluación de Impactos por Olor
en el SEIA, que de acuerdo al artículo 11 de la Ley N°
19.300 [5], para efectos de evaluar si el proyecto genera o
presenta riesgo para la salud, se debe considerar lo
establecido en las normas de calidad ambiental y de
emisión vigentes utilizando como referencia las vigentes
en los Estados que señala el artículo 11 del Reglamento
del SEIA, y de no utilizarlas, se debe priorizar la normativa
de aquel Estado que posea similitud en sus componentes
ambientales, con la situación nacional o local.

De acuerdo con lo anterior, se utilizó como referencia la
normativa del Estado de Italia, correspondiente a la Junta

1 Servicio de Evaluación Ambiental. (2012). Guía para el uso de

modelos de calidad del aire en el SEIA. Chile.
2 Servicio de Evaluación Ambiental. (2017). Guía para la

Predicción y Evaluación de Impactos por Olor en el SEIA.
Ministerio del Medio Ambiente. Chile.
3 Instituto Nacional de Normalización. (2015). NCh 3386:2015

Calidad del aire - Muestreo Estático para Olfatometría. Chile.
4 Instituto Nacional de Normalización. (2010). NCh 3190:2010

Calidad del aire - Determinación de la Concentración de Olor
por Olfatometría Dinámica. Chile.
5 Ministerio Secretaría General de la Presidencia. (2016). Ley

19.300 Aprueba Ley Sobre Bases Generales del Medio
Ambiente. Ministerio Secretaría General de la Presidencia. Chile.

Provincial de Trento [6] (2016), la cual establece los límites
permisibles en función de la planificación territorial y
proximidad de los receptores. Dado que el lugar de
emplazamiento del proyecto se encuentra en una zona no
regulada por los Instrumentos de Planificación Territorial
(IPT), es aplicable el uso de criterios para receptores fuera
de una zonificación residencial. Por lo tanto, los límites
normativos aplicables, bajo percentil 98, según la distancia
de los receptores desde el perímetro del predio
corresponderían a:

- 2 [ou E /m [3] ], para receptores situados a una distancia
>500 [m] del perímetro del predio.

- 3 [ou E /m [3] ], para receptores situados a una distancia
entre 200 y 500 [m] desde el perímetro del predio.

- 4 [ou E /m [3] ], para receptores situados a una distancia
<200 [m] desde el perímetro del predio.

Por lo tanto, para evaluación de impacto odorante en los
puntos receptores cercanos al perímetro predial del
proyecto, serían aplicables los siguientes niveles límites de
concentración:

6 Giunta Provinciale di Trento. (2016). Linee guida per la

caratterizzazione, l’analisi e la definizione dei criteri tecnici e
gestionali per la mitigazione delle emissioni delle attività ad
impatto odorigeno. Italia.

RESUMEN EJECUTIVO www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 9 de 77

Tabla 2 - Límites de concentración de olor en receptores
según normativa de Trento

|ID|Nombre|Distancia\a<br>[m]|Límite de<br>concentración<br>de olor según<br>Normativa de<br>Trento<br>[ou/m3]<br>E|
|---|---|---|---|
|R1|Vivienda ubicada fuera del<br>límite urbano de Maullín|636|2|
|R2|Vivienda ubicada fuera del<br>límite urbano de Maullín|472|3|
|R3|Vivienda ubicada fuera del<br>límite urbano de Maullín|493|3|
|R4|Vivienda ubicada fuera del<br>límite urbano de Maullín|580|2|
|R5|Vivienda ubicada fuera del<br>límite urbano de Maullín|858|2|
|R6|Vivienda ubicada fuera del<br>límite urbano de Maullín|649|2|
|R7|Vivienda ubicada fuera del<br>límite urbano de Maullín|502|2|
|R8|Vivienda ubicada fuera del<br>límite urbano de Maullín|439|3|
|R9<br>|Vivienda ubicada fuera del<br>límite urbano de Maullín<br>|584|2|
|R10|Vivienda ubicada fuera del<br>límite urbano de Maullín|623|2|
|R11|Vivienda ubicada fuera del<br>límite urbano de Maullín|474|3|
|R12|Vivienda ubicada fuera del<br>límite urbano de Maullín|79|4|
|R13|Vivienda ubicada fuera del<br>límite urbano de Maullín|63|4|
|R14|Vivienda ubicada fuera del<br>límite urbano de Maullín|255|3|
|R15|Vivienda ubicada fuera del<br>límite urbano de Maullín|33|4|
|R16|Vivienda ubicada fuera del<br>límite urbano de Maullín|760|2|
|R17|Vivienda ubicada fuera del<br>límite urbano de Maullín|471|3|
|R18|Vivienda ubicada fuera del<br>límite urbano de Maullín|675|2|

\a Distancia medida desde el perímetro predial al punto receptor.

Tabla 3 - Escenario operacional para modelación

variables meteorológicas e información topográfica y de
uso de suelo.

La base meteorológica fue procesada mediante MMIF,
integrando datos de pronóstico WRF [7] 2021 con resolución
de 1 [km] (espaciado de la cuadrícula). Se aplicó una grilla
anidada con un espaciado en receptor desde 10 [m], para
alcanzar mayor resolución de las isolíneas de
concentración resultantes del modelo, basado en la
parametrización definida en la “Guía para el Uso de
Modelos de Calidad del Aire en el SEIA” (SEA, 2017).
El dominio meteorológico WRF cubrió un área de
aproximadamente 50 x 50 [km].

La distribución espacial de los puntos receptores de
interés se describe en la siguiente tabla.

Tabla 4 - Puntos receptores de interés

|ID|Coordenadas UTM [m] (WGS84-<br>18G)|Col3|Distancia\a<br>[m]|Orientación|
|---|---|---|---|---|
|ID|X: Este|Y: Sur|Y: Sur|Y: Sur|
|R1|643.642|5.393.170|636|OSO|
|R2|643.846|5.393.126|472|SO|
|R3|643.905|5.392.985|493|SO|
|R4|643.884|5.392.862|580|SO|
|R5|644.596|5.392.490|858|S|
|R6|645.279|5.393.031|649|SE|
|R7|645.426|5.393.416|502|ESE|
|R8|645.430|5.393.521|439|ESE|
|R9|645.728|5.393.863|584|E|
|R10|645.681|5.394.079|623|ENE|
|R11|645.430|5.394.234|474|ENE|
|R12|644.968|5.394.229|79|NE|
|R13|644.950|5.394.281|63|NE|
|R14|645.051|5.394.456|255|NNE|
|R15|645.162|5.393.860|33|E|
|R16|645.603|5.393.258|760|ESE|
|R17|645.395|5.393.441|471|ESE|
|R18|645.335|5.393.068|675|SE|

\a Distancia medida desde el perímetro predial al punto receptor.

7 Weather Research and Forecasting Model, WRF

|Escenario|Col2|Modelos|Percentil|
|---|---|---|---|
|E1|Sit.<br>futura|M1: Isolíneas de olor.<br>M2: Frec. de percepción de olor horaria<br>M3: Frec. de percepción de olor mensual<br>M4: Concentración máxima horaria.|98|

El software empleado para la modelación de la dispersión
atmosférica de olores corresponde a Calpuff View, versión
8.6.0, el cual requiere de datos de entrada, tales como, de
características físicas de las fuentes, valores de emisión,

RESUMEN EJECUTIVO www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 10 de 77

Figura 2 - Puntos receptores de interés

Fuente: Elaboración propia, a partir de Google Earth 2023.

Tanto para la determinación del área de influencia de olor
como para la cuantificación del impacto por olores, se
siguieron los lineamientos de la Guía para la Predicción y
Evaluación de Impactos por Olor (SEIA, 2017).
Considerando como herramienta de predicción del
impacto, un modelo complejo de dispersión: Calpuff.

La estimación consideró como criterio el área proyectada
con 1 [ou E /m [3] ], que corresponde al umbral de detección
del olor.

La cuantificación del impacto se realizó a través de la
excedencia del criterio de calidad según distancia entre el
perímetro predial y el receptor. Considerando además la
cantidad de horas al año con probabilidad de percepción
de olor en los puntos receptores evaluados.

**Resultados**

Basado en la futura condición operacional de Plataforma
de Economía Circular Volta Los Lagos, se estimó una Tasa
de Emisión de Olor (TEO) de 46.638 [ou E /s].

Figura 3 - Estimación del área de influencia según nivel
umbral del C P98-1hr = 1 [ou E /m [3] ]

Fuente: Elaboración propia, a partir de Google Earth 2023.

La proyección de las emisiones de la futura Plataforma
arrojó un área de influencia para la componente olor de
aproximadamente 77 [ha]. De los 18 receptores
evaluados, 15 de ellos se encontrarían fuera del nivel de
umbral de 1 [ou E /m [3] ].

Figura 4 - Curvas isodoras a C P98-1hr = 2 [ou E /m [3] ] -
distancia >500 [m]

Fuente: Elaboración propia, a partir de Google Earth 2023.

RESUMEN EJECUTIVO www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 11 de 77

El alcance odorante de la situación futura para isocurvas
desde 2 [ou E /m [3] ] arrojaron un área de 5,37 [ha]. De los
receptores situados a más de 500 [m], ninguno de ellos
acusaría excedencia de este nivel de concentración de

olor.

Figura 5 - Curvas isodoras a C P98-1hr = 3 [ou E /m [3] ] -
distancia 200 - 500 [m]

Fuente: Elaboración propia, a partir de Google Earth 2023.

La modelación de la situación futura para
isoconcentraciones desde 3 [ou E /m [3] ] arrojó un alcance de
0,17 [ha]. De los 6 receptores situados entre 200 [m] y
500 [m] del perímetro predial del proyecto ninguno
acusaría superación de este nivel de concentración.

Figura 6 - Curvas isodoras a C P98-1hr = 4 [ou E /m [3] ] -
distancia <200 [m]

Fuente: Elaboración propia, a partir de Google Earth 2023.

El alcance odorante para isocurvas de concentración
desde 4 [ou E /m [3] ] no arrojaron niveles fuera del límite
predial. De los receptores situados a menos de 200 [m],
ninguno de ellos acusaría excedencia de este nivel de
concentración de olor.

Tabla 5 - Concentración máxima en receptores

|Concentración máxima en receptores<br>C = 3 [ou/m3]<br>P98-1hr E|Col2|Col3|
|---|---|---|
|ID|E1: Situación futura|E1: Situación futura|
|ID|Percentil 99,5|Percentil 98|
|R1|1|<1|
|R2|2|<1|
|R3|2|<1|
|R4|1|<1|
|R5|<1|<1|
|R6|<1|<1|
|R7|1|<1|
|R8|1|<1|
|R9|1|<1|
|R10|1|<1|
|R11|1|<1|
|R12|2|1|
|R13|2|1|
|R14|1|<1|
|R15|3|1|
|R16|<1|<1|
|R17|1|<1|
|R18|<1|<1|

Tabla 6 - Evaluación de cumplimiento de límite de
aceptabilidad en receptores - Situación futura

|ID|Concentración<br>máxima<br>[ou/m3]<br>E<br>Percentil 98|Límite de<br>concentración<br>Normativa de<br>Trento8<br>[ou/m3]<br>E|Cumplimiento|Superación<br>valor límite<br>normado|
|---|---|---|---|---|
|R1|<1|2|Sí|No|
|R2|<1|3|Sí|No|
|R3|<1|3|Sí|No|
|R4|<1|2|Sí|No|
|R5|<1|2|Sí|No|
|R6|<1|2|Sí|No|
|R7|<1|2|Sí|No|
|R8|<1|3|Sí|No|
|R9|<1|2|Sí|No|
|R10|<1|2|Sí|No|
|R11|<1|3|Sí|No|
|R12|1|4|Sí|No|
|R13|1|4|Sí|No|
|R14|<1|3|Sí|No|
|R15|1|4|Sí|No|
|R16|<1|2|Sí|No|
|R17|<1|3|Sí|No|
|R18|<1|2|Sí|No|

8 Giunta Provinciale di Trento. (2016). Linee guida per la

caratterizzazione, l’analisi e la definizione dei criteri tecnici e
gestionali per la mitigazione delle emissioni delle attività ad
impatto odorigeno. Italia.

RESUMEN EJECUTIVO www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 12 de 77

**Conclusión**

De la caracterización de emisiones de la futura Plataforma
de Economía Circular Volta Los Lagos, se estimó una Tasa
de Emisión de Olor de 46.638 [ou E /s], basado en las
condiciones operacionales descritas por el Titular.

La estimación del Área de Influencia del Proyecto arrojó
alcance sobre el nivel umbral de C P98-1h =1 [ou E /m [3] ], en 3
receptores de los 18 evaluados situados al norte del límite
predial.

De la cuantificación de impacto, el modelo acusaría que
los 18 receptores considerados en la evaluación se
encuentran en cumplimiento con el límite de aceptabilidad
de la normativa de Trento, correspondiente a 2 [ou E /m [3] ]
para receptores que se encuentren a más de 500 [m] del
límite predial, 3 [ou E /m [3] ] para receptores entre 200 y 500

[m] del límite predial y 4 [ou E /m [3] ] para aquellos
receptores que se encuentren a menos de 200 [m] del
límite predial.

En virtud de la proyección del alcance odorante de las
emisiones del proyecto en evaluación, para la componente
olor, no se generaría o presentaría algún efecto,
características o circunstancias contempladas en el artículo
11 de la Ley N° 19.300, siendo aplicable su ingreso como
Declaración de Impacto Ambiental.

RESUMEN EJECUTIVO www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 13 de 77

**ÍNDICE**

1 ANTECEDENTES ................................................................................................................................... 16
1.1 Antecedentes generales ................................................................................................................ 16
1.2 Antecedentes específicos .............................................................................................................. 17
1.2.1 Aprovechamiento energético de los residuos orgánicos a través de la digestión anaeróbica ........... 17
1.2.2 Elaboración de compost y sustratos agrícolas a través del proceso de compostaje ........................ 19
1.2.3 Tratamiento aeróbico de residuos líquidos industriales orgánicos mediante planta de tratamiento de
RILes ............................................................................................................................................................. 20
1.2.4 Producción de Carbonato de Calcio a partir de conchas de moluscos ............................................ 21
1.2.5 Segregación y Valorización de residuos sólidos recuperables ....................................................... 22
1.2.6 Transferencia y valorización de residuos peligrosos ..................................................................... 24
1.2.7 Transferencia y valorización de residuos no peligrosos ................................................................ 26
1.3 Identificación de fuentes de emisión .............................................................................................. 28
1.4 Descripción de las fuentes de emisión ............................................................................................ 29
2 OBJETIVOS .......................................................................................................................................... 31
2.1 Objetivo general ........................................................................................................................... 31
2.2 Objetivos específicos .................................................................................................................... 31
3 ESTIMACIÓN DE EMISIONES ................................................................................................................ 32

3.1 Emisiones de referencia ................................................................................................................ 32
3.2 Emisiones según olor simple o compuesto...................................................................................... 34
3.3 Descripción de fuentes emisoras de olor ........................................................................................ 36
3.4 Ranking de emisiones ................................................................................................................... 38
4 PREDICCIÓN DE IMPACTOS POR OLOR ................................................................................................. 40
4.1 Metodologías para la predicción de impactos por olor ..................................................................... 40
4.2 Antecedentes para el área de influencia ......................................................................................... 41
4.2.1 Descripción del área de influencia según elementos del medio ambiente ...................................... 42
4.2.2 Identificación de receptores de olor ........................................................................................... 42
4.2.3 Olor base en situación sin proyecto ............................................................................................ 44
5 ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR ................................................................... 47
5.1 Estimación concentración límite de exposición ................................................................................ 47
5.2 Estimación de los impactos por emisiones de olor ........................................................................... 49
5.3 Predicción de Área de Influencia del Proyecto ................................................................................ 50
5.4 Cuantificación según curva de isoconcentración de olor .................................................................. 51
5.5 Cuantificación de la frecuencia de percepción de olor ..................................................................... 54
5.6 Concentración máxima .................................................................................................................. 56
6 CONCLUSIÓN ....................................................................................................................................... 57
7 BIBLIOGRAFÍA ..................................................................................................................................... 58
8 ANEXO 1 - CARACTERIZACIÓN DE FUENTES ODORANTES ..................................................................... 60
9 ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES ............................................................. 62
9.1 Aprovechamiento energético de los residuos orgánicos a través de la digestión anaeróbica ............... 62
9.2 Elaboración de compost agrícolas a través del proceso de compostaje ............................................. 63
9.3 Elaboración de carbonato de calcio a partir de conchas de moluscos ............................................... 66
10 ANEXO 3 - PLAN DE TRABAJO Y METODOLOGÍA ............................................................................... 69
10.1 Plan de trabajo ............................................................................................................................. 69
10.1.1 Rueda de olor ....................................................................................................................... 70
11 ANEXO 4 - MODELO DE DISPERSIÓN ............................................................................................... 72

11.1 Alcances del modelo ..................................................................................................................... 72
11.2 Descripción del modelo ................................................................................................................. 72
11.3 Dominio de modelación................................................................................................................. 73

11.4 Elevaciones de terreno .................................................................................................................. 74

ÍNDICE www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 14 de 77

11.5 Uso de suelo ................................................................................................................................ 75
12 ANEXO 5 - ANÁLISIS METEOROLÓGICO ........................................................................................... 76
12.1 Comportamiento meteorológico anual ............................................................................................ 76
12.2 Caracterización meteorológica anual horaria ................................................................................... 77

**ÍNDICE DE TABLAS**
Tabla 1 - Fuentes de emisión ........................................................................................................................ 7
Tabla 2 - Límites de concentración de olor en receptores según normativa de Trento ....................................... 9
Tabla 3 - Escenario operacional para modelación ............................................................................................ 9
Tabla 4 - Puntos receptores de interés ........................................................................................................... 9
Tabla 5 - Concentración máxima en receptores ............................................................................................ 11
Tabla 6 - Evaluación de cumplimiento de límite de aceptabilidad en receptores - Situación futura ................... 11
Tabla 7 - Coordenadas referenciales de localización del Proyecto ................................................................... 16
Tabla 8 - Identificación de unidades con emisión de olor al ambiente ............................................................ 28
Tabla 9 - Fuentes odorantes - Situación futura ............................................................................................ 29
Tabla 10 - Proyectos de referencia asimilables al proyecto ............................................................................ 33
Tabla 11 - Emisiones de referencia aplicados en la situación futura ............................................................... 33
Tabla 12 - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 1 ...................................... 36
Tabla 13 - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 2 ...................................... 37
Tabla 14 - Ranking TEO [ou E /s] por fuente modelada - Situación futura ........................................................ 39
Tabla 15 - Puntos receptores de interés ....................................................................................................... 43
Tabla 16 - Proyectos aprobados por el SEA .................................................................................................. 45
Tabla 17 - Concentraciones máximas en receptores según normativa de Trento. ............................................ 48
Tabla 18 - Valores de aceptabilidad de concentración de olor en receptores según distancia ........................... 48
Tabla 19 - Descripción escenarios simulados ................................................................................................ 49
Tabla 20 - E1/M2: Frecuencia de percepción de olor horaria - C P98-1hr =2, 3 y 4 [ou E /m [3] ] ................................. 54
Tabla 21 - E1/M3: Frecuencia de percepción de olor mensual - C P98-1hr =2, 3 y 4 [ou E /m [3] ] ............................... 55
Tabla 22 - Concentración máxima - Percentil 98 y 99,5 - Situación futura ..................................................... 56
Tabla 23 - Situación futura: Caracterización de fuentes de olor ..................................................................... 60
Tabla 24 - Situación futura: Características operacionales de fuentes emisoras ............................................... 61
Tabla 25 - Base de cálculo: emisiones de entrada biofiltro de planta de biogás ............................................... 62
Tabla 26 - Base de cálculo: emisión proyectada en biofiltro de planta de biogás ............................................. 63
Tabla 27 - Base de cálculo: emisiones de entrada biofiltro de galpón de compostaje ...................................... 63
Tabla 28 - Base de cálculo: emisión proyectada en biofiltro de galpón de compostaje ..................................... 63
Tabla 29 - Base de cálculo: emisiones compostaje en trincheras .................................................................... 64
Tabla 30 - Base de cálculo: emisiones proyectadas de trincheras según condición .......................................... 65
Tabla 31 - Base de cálculo: emisiones proyectadas de trincheras en condición de carga/descarga ................... 65
Tabla 32 - Base de cálculo: emisiones de patio de maduración ...................................................................... 66
Tabla 33 - Base de cálculo: emisiones proyectadas de patio de maduración según condición .......................... 66
Tabla 34 - Base de cálculo: emisiones proyectadas de patio de maduración en condición de carga/descarga ... 66
Tabla 35 - Base de cálculo: emisiones de entrada biofiltro de planta de carbonato de calcio ............................ 67
Tabla 36 - Base de cálculo: emisión proyectada en biofiltro de planta de carbonato de calcio .......................... 67
Tabla 37 - Base de cálculo: emisiones de salida chimenea scrubber de planta de carbonato de calcio .............. 68
Tabla 38 - Base de cálculo: emisiones de camiones en tránsito por camiones de transporte ............................ 68
Tabla 39 - Base de cálculo: emisiones de tránsito por camiones de transporte ............................................... 68
Tabla 40 - Descripción de grilla anidada ....................................................................................................... 72
Tabla 41 - Coordenada central Plataforma Economía Circular Volta Los Lagos ................................................ 76
Tabla 42 - Rosas y campos de viento pronóstico anual.................................................................................. 77

ÍNDICE www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 15 de 77

**ÍNDICE DE FIGURAS**
Figura 1 - Localización del Proyecto ............................................................................................................... 7
Figura 2 - Puntos receptores de interés ........................................................................................................ 10
Figura 3 - Estimación del área de influencia según nivel umbral del C P98-1hr = 1 [ou E /m [3] ] ................................. 10
Figura 4 - Curvas isodoras a C P98-1hr = 2 [ou E /m [3] ] - distancia >500 [m] .......................................................... 10
Figura 5 - Curvas isodoras a C P98-1hr = 3 [ou E /m [3] ] - distancia 200 - 500 [m] .................................................... 11
Figura 6 - Curvas isodoras a C P98-1hr = 4 [ou E /m [3] ] - distancia <200 [m] .......................................................... 11
Figura 7 - Localización del Proyecto ............................................................................................................. 16
Figura 8 - Diagrama de proceso Planta de Biogás ......................................................................................... 18
Figura 9 - Diagrama de proceso Planta de Compostaje ................................................................................. 20
Figura 10 - Diagrama de proceso Planta de Tratamiento de RILes ................................................................. 21
Figura 11 - Diagrama de proceso Planta de Carbonato de Calcio ................................................................... 22
Figura 12 - Diagrama de proceso Planta de Segregación y Valorización .......................................................... 23
Figura 13 - Diagrama de flujo del proceso de la Transferencia y Valorización de residuos peligrosos ................ 25
Figura 14 - Diagrama de flujo del proceso de la Transferencia y Valorización de residuos no peligrosos ........... 26
Figura 15 - Distribución espacial de fuentes odorantes del Proyecto ............................................................... 30
Figura 16 - Distribución espacial de fuentes odorantes (zoom) ...................................................................... 30
Figura 17 - Método para la predicción de impactos por olor ........................................................................... 40
Figura 18 - Emplazamiento del proyecto según planificación territorial vigente ............................................... 41
Figura 19 - Distribución de receptores de interés .......................................................................................... 44
Figura 20 - Proyectos aprobados por el Servicio de Evaluación Ambiental ...................................................... 45
Figura 21 - AI: Área de influencia del Proyecto, C P98-1hr = 1 [ou E /m [3] ] .............................................................. 50
Figura 22 - E1: Curvas isodoras, Sit. futura, receptores a una distancia >500 [m], C P98-1hr = 2 [ou E /m [3] ]............ 51
Figura 23 - E1: Curvas isodoras, Sit. futura, receptores a una distancia entre 200 [m] y 500 [m], C P98-1hr = 3

[ou E /m [3] ] ..................................................................................................................................................... 52
Figura 24 - E1: Curvas isodoras, Sit. futura, receptores a una distancia <200 [m], C P98-1hr = 4 [ou E /m [3] ]............ 53
Figura 25 - Esquema de plan de trabajo y metodología aplicada .................................................................... 69
Figura 26 - Rueda de olor compostaje ......................................................................................................... 70
Figura 27 - Rueda de descriptores de plantas de tratamiento de aguas residuales .......................................... 71
Figura 28 - Dominio de modelación ............................................................................................................. 73
Figura 29 - Elevación de terreno del dominio ................................................................................................ 74
Figura 30 - Uso de suelo del dominio ........................................................................................................... 75
Figura 31 - Distribución de rosa de viento anual ........................................................................................... 76

ÍNDICE www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 16 de 77

**1** **ANTECEDENTES**

En el marco de la Declaración de Impacto Ambiental (DIA) sometida al Sistema de Evaluación de Impacto
Ambiental (SEIA), Volta Servicios SpA, ha solicitado a TSG Environmental SpA., área Envirometrika, realizar
una Modelación de Impacto Odorante del proyecto “Plataforma de Economía Circular Volta Los Lagos”.

**1.1** **Antecedentes generales**

El proyecto se ubicará en la comuna de Maullín, provincia de Llanquihue, Región de Los Lagos. Se
inserta dentro del predio del mismo Titular, cuya superficie total es de 87 [ha], de las cuales 24 [ha]
corresponden a la Plataforma de Economía Circular Volta Los Lagos.

Tabla 7 - Coordenadas referenciales de localización del Proyecto

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|X: Este|Y: Sur|Huso|Datum|
|644.590|5.393.748|18 G|WGS 84|

Figura 7 - Localización del Proyecto

Fuente: Envirometrika - Google Earth, 2023.

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 17 de 77

El proyecto tiene por objetivo la habilitación de una planta de economía circular para el manejo de los
residuos, garantizando una operación sustentable en el tiempo, adoptando estándares actualizados y
tecnologías de alto nivel que permiten el reciclaje, la reutilización y valorización de los residuos generados
en la Región de Los Lagos. Entre las áreas de proceso contempladas en el futuro proyecto se encuentran:

1. Aprovechamiento energético de los residuos orgánicos a través de la digestión anaeróbica.
2. Elaboración de compost y sustratos agrícolas a través del proceso de compostaje.
3. Tratamiento aeróbico de residuos líquidos industriales orgánicos mediante Planta de Tratamiento de

RILes.
4. Producción de carbonato de calcio a partir de conchas de moluscos.
5. Segregación y valorización de residuos sólidos recuperables.
6. Transferencia y valorización de residuos peligrosos y no peligrosos.

**1.2** **Antecedentes específicos**

**1.2.1** **Aprovechamiento energético de los residuos orgánicos a través de la digestión**

**anaeróbica**

La operación de esta área contempla el aprovechamiento energético de los residuos mediante
digestión anaerobia, mediante la recepción de residuos orgánicos, tales como lodos sanitarios y
residuos provenientes de la industria agrícola, alimentaria y otros procesos que generen
residuos de origen orgánico en concordancia con la Norma Chilena de digestato (NCh
3375:2015 [9] ).

La digestión anaeróbica es una tecnología eficiente y ambientalmente sostenible, en la cual
microorganismos descomponen material biodegradable en ausencia de oxígeno. Este proceso
genera la estabilización de los residuos orgánicos y la desinfección de residuos de origen animal
(higienización), eliminando microorganismos patógenos y reduciendo el riesgo de transmisión de
enfermedades. Adicionalmente, el proceso produce biogás, el cual se puede aprovechar para
generar energía eléctrica y/o térmica de manera sustentable, reduciendo considerablemente los
gases de efecto invernadero, otorgando un valor agregado a los residuos recibidos por la

empresa.

De la digestión anaeróbica se obtiene también digestato (material estabilizado), este pasa a un
estanque de acumulación cerrado (sin emisión al ambiente) para su posterior ingreso al
deshidratador mecánico. En esta unidad, se obtiene una fracción líquida que se conduce a la
laguna de digestato clarificado. Por otro lado, la fracción sólida, que corresponde al lodo
digestato, es almacenado en un estanque cerrado para su despacho para su uso como insumo
para la mejora del suelo, como aporte nutricional en el proceso de compostaje, o bien ser
comercializado como digestato, en cumplimiento con la normativa NCh 3375:2015 [10] .

9 Instituto Nacional de Normalización. (2015). NCh 3375/15: Digestato - Requisitos de Calidad. Chile.
10 Ibid.

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 18 de 77

Figura 8 - Diagrama de proceso Planta de Biogás

Fuente: Envirometrika basado en diagrama de Volta Servicios, 2023

La planta de biogás cuenta con un galpón de recepción, dispuesto con un estanque de recepción
donde descargan los camiones con residuos orgánicos, esté contará con un sistema de filtrado
para evitar partículas de gran tamaño que puedan afectar a los sistemas mecánicos que entren
al proceso.

El galpón además considera dos estanques de higienización para el procesamiento de residuos
de origen animal, logrando de esta forma esterilizar los residuos. Del mismo modo, se dispone
de un estanque de mezcla donde se recibirán los lodos sanitarios y lodos orgánicos de forma
directa, como también los residuos provenientes del proceso de higienización. En este estanque
habrá una pre-acidificación del residuo sólido, el que contará con una cubierta para evitar
emanaciones de biogás a la atmósfera y malos olores. Las unidades descritas al interior del
galpón contarán con un sistema de extracción forzada para el posterior envió a un sistema de
abatimiento de olores correspondiente a un biofiltro con capacidad de tratamiento de 33 [m [3] ] y
con una eficiencia de remoción superior al 95% [11], garantizando la no generación de impactos
por olores al ambiente.

La planta de biogás contempla digestor anaeróbico, correspondiente a un estanque cerrado,
hermético e impermeable, en el cual se metaboliza la materia orgánica en ausencia de oxígeno
(ambiente anóxico) siendo necesario que este opere de forma continua en condiciones
mesofílicas (35[°C]) y que la mezcla esté en agitación constante. De la degradación de materia
orgánica se produce biogás, el cual será almacenado en un gasómetro de doble membrana. Este
biogás puede ser utilizado como combustible de un equipo de cogeneración de energía eléctrica
y térmica, como también ser usado en el quemador de la planta de carbonato de calcio.

11 Para la representación del escenario más desfavorable se aplicó un valor de eficiencia más conservador correspondiente al 90%.

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 19 de 77

Posterior a la digestión, el digestato producido se almacenará en un estanque cerrado (postdigestor), donde se generará la estabilización final del sustrato, para luego conducirlo a la
unidad de almacenamiento de digestato o hacia el deshidratado mecánico. A continuación, el
digestato crudo (sin deshidratar) será almacenado en un estanque cónico y cerrado, el cual
podrá ser utilizado posteriormente en el proceso de deshidratado mecánico, como también en el
proceso de compostaje como fuente de nutrientes, riego de digestato y venta a terceros.

La unidad de deshidratación considera la reducción del contenido de humedad del digestato de
forma mecánica. Como resultado del proceso de deshidratación se obtendrá clarificado
(digestato liquido), el cual será bombeado a la laguna de digestato clarificado o será conducido
para humectar los residuos del estanque de mezcla según el porcentaje de humedad que tenga
la mezcla. Por su parte, el digestato deshidratado se almacenará en batea para su posterior
utilización como abono dentro del mismo predio, en el proceso de compostaje o comercializado
para uso agrícola, cumpliendo la Norma Chilena NCh 3375:2015 [12] de “Requisitos de calidad de
digestato”.

El digestato líquido (clarificado) será almacenado en una laguna de digestato clarificado, el cual
será utilizado primordialmente en el suelo como fertirriego o infiltrado en el predio de Volta.

Las unidades gasholder y cogenerador corresponden a unidades cerradas sin emisión directa al
ambiente, condición que forma parte del diseño y operación de estas, para el aprovechamiento
del biogás tanto para el aprovechamiento de energía eléctrica (planta de carbonato) como
energía térmica (higienización).

**1.2.2** **Elaboración de compost y sustratos agrícolas a través del proceso de compostaje**

El proyecto contempla el diseño de una planta de compostaje para el desarrollo del proceso de
descomposición biológica de materia orgánica y posterior estabilización mediante la aplicación
de condiciones aeróbicas. Las etapas iniciales del proceso se realizarán en un galpón de
recepción de lodos y mezcla, donde se realiza el proceso de mezclado de los residuos orgánicos
y el material estructurante. Mediante un mixer, se incorporarán, homogenizarán y oxigenarán
las materias primas (residuos orgánicos y material estructurante) para disminuir su potencial
carga anóxica y lograr una buena porosidad de la mezcla. La mezcla obtenida al interior del
galpón será trasladada hacia el área de trincheras donde se realizará el proceso de compostaje.

Los gases odorantes generados al interior del galpón serán conducidos a un biofiltro de olor
mediante un sistema de aireación forzada negativa (extractor de aire), con una eficiencia de
remoción de olores mayor a 95%.

Una vez trasladado el material de mezcla, se dispondrá al interior de cada trinchera
considerando una altura máxima de 2,4 [m], pudiendo formar hasta 32 trincheras dentro de
esta área. Las trincheras contarán con sistemas de aireación forzada positiva (inyección de aire),
permitiendo oxigenar las pilas de forma homogénea, acelerando la descomposición y evitando la
generación de malos olores. A medida que se complete la capacidad de cada trinchera, se
cubrirá con cobertores especiales que protegen las pilas de las lluvias, mantienen el oxígeno
dentro de ellas y retienen los gases odorantes que se puedan generar en el proceso. La acción
combinada de la aireación forzada y los cobertores permiten acelerar el compostaje y hacerlo
más eficiente y sostenible.

12 Instituto Nacional de Normalización. (2015). NCh 3375/15: Digestato - Requisitos de Calidad. Chile.

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 20 de 77

Finalizado el proceso en trincheras, el material será conducido a un patio de compost, donde se
desarrollará la fase de maduración y término del proceso de compostaje. El producto final
(compost terminado) será tamizado, analizado en laboratorio externo y almacenado en pilas
para su posterior distribución y venta a granel. Para que no se humedezca por efecto de las
lluvias, será protegido con una cubierta impermeable.

Figura 9 - Diagrama de proceso Planta de Compostaje

Unidad sin emisión de olor al ambiente

Unidad canalizada a sistema de abatimiento

Unidad con emisión de olor al ambiente

Retiro de

Fuente: Envirometrika basado en diagrama de Volta Servicios, 2023

**1.2.3** **Tratamiento aeróbico de residuos líquidos industriales orgánicos mediante planta de**

**tratamiento de RILes**

El proyecto contempla una planta de tratamiento de RILes, cuya operación considera tratar los
RILes generados por la actividad de lavado de ruedas de camiones, de conchas de moluscos, de
sólidos recuperables los cuales serán recepcionados en estanques de ecualización, y RILes
externos.

Posteriormente, los RILes serán tratados en reactores de aerobios de tipo SBR mediante la
inyección de oxígeno disuelto. Las aguas tratadas en la Planta de tratamiento de RILes serán
prioritariamente reutilizadas como agua industrial en el proceso de aprovechamiento energético
de materia orgánica a través de la digestión anaeróbica, como agua de proceso para elaboración
de carbonato de calcio, para humectación de caminos, además, será reutilizado para el riego de
áreas verdes internas, dando cumplimiento a la NCh 1333 of 87, y como última alternativa, las
aguas tratadas serán infiltradas dando cumplimiento al artículo N°9 del D.S N° 46/2002
“Establece Norma de Emisión de residuos líquidos a aguas subterráneas debiendo estas tener
igual o mejor calidad que las contenidos en el acuífero presentes en el sector, y que presenta
condiciones de vulnerabilidad alta, de acuerdo al Estudio de Vulnerabilidad del Acuífero, adjunto
en el Anexo 3-4 de la Adenda

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 21 de 77

Respecto a los lodos generados durante el proceso de tratamiento de lixiviados, estos serán
tratados en la planta de Digestión Anaeróbica, con la finalidad de lograr la estabilización de los
lodos biológicos.

Figura 10 - Diagrama de proceso Planta de Tratamiento de RILes

|Descarga de<br>RILes|Col2|
|---|---|
|||

lodos

|Filtro<br>rotatorio|Col2|
|---|---|
|||

recepción SBR

|Cámara de<br>recepción|Col2|
|---|---|
|||

|Almacenamiento<br>de grasas|Col2|
|---|---|
|Almacenamiento<br>de grasas||

|Sedimentadores|Col2|Ecualizadores|
|---|---|---|
||||

Unidad sin emisión de olor al ambiente

Unidad canalizada a sistema de abatimiento

Unidad con emisión de olor al ambiente

Fuente: Envirometrika basado en diagrama de Volta Servicios, 2023

**1.2.4** **Producción de Carbonato de Calcio a partir de conchas de moluscos**

Esta área de proceso contempla la elaboración de carbonato de calcio a partir de conchas de
moluscos el cual será utilizado para la alimentación de animales, mejoramiento de suelos y/o
otros usos.

El proceso productivo comienza al interior del galpón de la planta con la recepción ordenada de
camiones de conchillas de moluscos, donde se contará con una losa impermeable, con pretiles
en su perímetro y canaletas, que permitirán captar los lixiviados generados en esta instalación y
conducirlos a la planta de tratamiento de RILes.

Las conchillas recepcionadas serán sometidas a un proceso de lavado mediante un equipo
rotatorio para la separación de arena y lavado de sales. Se utilizarán las aguas tratadas por la
Planta de Tratamiento de RILes, el digestato líquido y el agua extraída del pozo para el proceso
de lavado de conchillas. Las arenas de lavado serán acumuladas, para posteriormente ser
enviadas a disposición final a un sitio autorizado por la SEREMI de Salud de la Región. En
cuanto a las aguas de lavado, estas serán conducidas a la Planta de Tratamiento de RILes para
su tratamiento y reutilización en el proceso de lavado de conchillas.

Posteriormente, las conchillas lavadas se trasladan hacia silos cerrados para su almacenamiento
por un periodo máximo de 3 días, donde por gravedad se remueve el contenido remanente de
agua, el que es captado y dirigido hacia la Planta de Tratamiento de RILes.

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 22 de 77

Desde los silos de almacenamiento, las conchillas serán conducidas mediante una cinta
transportadora hacia el dosificador del proceso de calcinación mediante un horno rotatorio que
utilizará como fuente de energía para su funcionamiento el biogás producido por el proceso de
Digestión Anaerobia. El proceso de calcinación contará con un sistema depurador húmedo, tipo
Scrubber que eliminan los contaminantes gaseosos del flujo del aire.

Luego que el material es calcinado, se deriva al proceso de enfriamiento mediante la inyección
de agua para bajar la temperatura. Para el desarrollo del proceso de enfriamiento se utilizarán
las aguas tratadas por la Planta de Tratamiento de RILes, el digestato líquido y el agua extraída
del pozo para el proceso de enfriamiento.

Una vez que la materia prima es enfriada se realiza el proceso de trituración y molienda con el
objetivo de lograr un producto con una granulometría adecuada para uso y comercialización. De
esta manera se obtendrán diversos productos a una pureza del carbonato de calcio del 95%.

Posteriormente el material es conducido a un tamizador ultrasónico, que permitirá segregar en
diversos tamaños dependiendo de la fineza de la partícula, para luego ser almacenados en
distintos silos antes de ser envasados para su uso final.

Figura 11 - Diagrama de proceso Planta de Carbonato de Calcio

Fuente: Envirometrika basado en diagrama de Volta Servicios, 2023

**1.2.5** **Segregación y Valorización de residuos sólidos recuperables**

El proyecto contempla la operación de una planta para la segregación y valorización de solidos
recuperables previamente preseleccionados. En ella, se realizarán los procesos de recepción,
segregación, consolidación y comercialización principalmente de papel, plástico, aluminio, vidrio
y madera entre otros materiales con valor comercial, así como productos prioritarios de la ley
REP, para su posterior aprovechamiento como materia prima o fuente energética no tradicional.

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 23 de 77

Se considera la recepción de residuos sólidos industriales asimilables a domiciliarios que se
puedan separar en:

a) Valorizables: Corresponden a residuos que serán sometidos a un proceso de trituración y/o
compactación, para posteriormente ser valorizados, vendidos y/o utilizados en otros procesos
que los requieran como materia prima.
b) No valorizables: Del proceso de valorización y reciclaje, se estima que un porcentaje de los
residuos no podrán ser recuperados ni reciclados en las instalaciones del proyecto por lo que
serán almacenados temporalmente, y luego serán enviados a un Relleno Sanitario Autorizado.

La Planta de valorización, corresponderá a un galpón en el cual se albergarán equipos tales
como: equipos compactadores, grúa horquilla y cintas transportadoras. Los residuos serán
descargados para su clasificación manual en papel, cartón, vidrios, plástico, metal y madera,
siendo conducidos mediante correas transportadoras a contenedores de plástico cerrados,
donde se segregará cada tipo de residuos para ser compactados y almacenados provisoriamente
en la zona de bloques compactados y posteriormente ser despachados a plantas de reciclaje y/o
revalorización. Se estima la recuperación del 90% de los residuos recibidos en las instalaciones.

Aquellos residuos que sean clasificados como no recuperables, donde se estima que sean un
40% de los recibidos en las instalaciones, serán almacenados en un contenedor metálico
cerrado, el cual una vez llegue a una carga superior al 80%, será enviado a un sitio de
disposición final autorizado.

Dadas las características de las materias primas procesadas en esta área, no se identifican
componentes de origen orgánico que pudieran ser considerados como fuente potencial de olores
molestos.

Figura 12 - Diagrama de proceso Planta de Segregación y Valorización

Salida del

recinto

|Inspección<br>de camión|Rechazada|
|---|---|
|||

|Descarga|Col2|
|---|---|
|Descarga||

|Residuos no<br>valorizables|Col2|
|---|---|
|Residuos no<br>valorizables||

|Compactador|Col2|
|---|---|
|Compactador||

|Almacenaje<br>de bloques<br>compactados|Col2|
|---|---|
|Almacenaje<br>de bloques<br>compactados||

|Clasificación|Col2|
|---|---|
|||

|Residuos<br>valorizables|Col2|
|---|---|
|Residuos<br>valorizables||

Unidad sin emisión de olor al ambiente

|Compactador|Col2|
|---|---|
|Compactador||

|Almacenaje<br>de bloques<br>compactados|Col2|
|---|---|
|Almacenaje<br>de bloques<br>compactados||

Unidad canalizada a sistema de abatimiento

Unidad con emisión de olor al ambiente

Fuente: Envirometrika basado en diagrama de Volta Servicios, 2023

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 24 de 77

**1.2.6** **Transferencia y valorización de residuos peligrosos**

Esta área tiene por objeto valorizar los residuos peligrosos que ingresen a la planta, así como,
acondicionarlos para disminuir su densidad volumétrica a fin de optimizar la gestión de
transporte de estos al momento de ser enviados a destinatario final o valorizador autorizado.
Para valorizar y/o reducir su densidad volumétrica, los residuos peligrosos serán sometidos a
segregación, trituración, destrucción de productos fuera de especificación y compactación de
aerosoles. Lo anterior permitirá valorizar los residuos peligrosos y/o disminuir su densidad
volumétrica a fin de optimizar la gestión de transporte de estos al momento de ser enviados a
destinatario final o valorizador autorizado.

La bodega de segregación y acondicionamiento de RESPEL se dividirá en 4 zonas de operación:

 - Segregación: Sector donde se recepcionarán residuos peligrosos en formato granel y
paletizado.

 - Trituración de residuos peligrosos: Sector de acondicionamiento de residuos peligrosos
sólidos mediante trituración.

 - Destrucción de productos fuera de especificación: Sector de acondicionamiento de residuos
sólidos de productos fuera de especificación o descarte de marca mediante trituración.

 - Compactación de aerosoles: Sector de acondicionamiento de residuos tipo aerosol mediante
compactación y separación.

La bodega de almacenamiento temporal de residuos peligrosos (RESPEL) estará destinada para
el almacenamiento de residuos peligrosos y contará con áreas ambientalmente identificadas y
segregadas unas de otras, para residuos corrosivos, tóxicos, comburentes y misceláneos. Los
residuos peligrosos consolidados serán transportados a sitios de disposición final autorizados
para tales efectos.

La bodega de almacenamiento temporal de residuos peligrosos (RESPEL) inflamables estará
destinada para el almacenamiento de residuos peligrosos inflamables, los cuales una vez
consolidados serán transportados a sitios de disposición final autorizados para tales efectos.

Debido a las condiciones de manejo y almacenamiento de los residuos al interior de cada
bodega (contenedores cerrados), no se identificarían unidades con una contribución significativa
de emisiones odorantes.

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 25 de 77

Figura 13 - Diagrama de flujo del proceso de la Transferencia y Valorización de residuos peligrosos

Fuente: Volta Servicios, 2023.

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 26 de 77

**1.2.7** **Transferencia y valorización de residuos no peligrosos**

El diseño del proceso de Transferencia y Valorización de residuos no peligrosos contará con el desarrollo de las siguientes instalaciones:

 - Sector de carga y descarga de camiones

 - Área de clasificación y valorización

 - Bodega de residuos industriales no peligrosos valorizados

 - Despacho de residuos valorizados

En la siguiente Figura se presenta el diagrama de flujo del proceso de Transferencia y Valorización de residuos peligrosos y no
peligrosos, respectivamente.

Figura 14 - Diagrama de flujo del proceso de la Transferencia y Valorización de residuos no peligrosos

Fuente: Volta Servicios, 2023.

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 27 de 77

Previo a la descarga de los residuos sólidos industriales no peligrosos se realizará el control de
reserva y documentos del ingreso, el control de pesaje del camión y la inspección visual de la
carga, a fin de determinar el cumplimiento de las condiciones de carga, así como, determinar su
naturaleza no peligrosa. El proceso de operación se ejecutará en un plazo menor a 24 horas,
desde la recepción del residuo.

Luego de la inspección documental y visual de los residuos industriales no peligrosos, se
realizará la descarga en el sector de carga y descarga de camiones, donde se recepcionarán
residuos no peligrosos correspondientes a neumáticos en desuso, maderas descartadas, materia
prima descartada, alimentos descartados y asbesto no friable, entre otros.

Una vez finalizada la recepción adecuada de los residuos, el camión que transportaba los
residuos se retirará de las instalaciones obteniéndose la tara de su ingreso, finalizando así la
etapa Control Documental y Pesaje, y cerrando el proceso del número de ticket de ingreso.

Para el caso de residuos paletizados, los residuos son etiquetados según su número de ticket y
almacenados temporalmente en la zona de clasificación, para ser posteriormente ubicado en su
sector de almacenamiento correspondiente. En el caso de que la carga no cumpla con las
condiciones de embalaje y rotulación, se podrá ejecutar el rechazo parcial o total de la carga,
comunicando al cliente los motivos por los cuales no se puede aceptar la carga y, cuando
corresponda, se enviará notificación al SEREMI de Salud. El protocolo de rechazo de ingresos se
activará en el momento de la detección de algún incumplimiento de ingreso, ya sea durante la
descarga de los residuos como durante la etapa de validación, contando en este último caso con
no más de 24 horas para ejecutar el retiro de los residuos de planta.

Los residuos detectados y separados en cada ingreso serán almacenados en contenedores
ubicados en la zona de segregación, con su respectiva rotulación por tipo de residuo. El personal
que realice estas actividades contará con las herramientas y EPP adecuados para poder realizar
una separación de residuos de forma segura, eficiente y efectiva.

Los residuos sólidos industriales no peligrosos que serán valorizados en el proceso de
Transferencia y valorización de residuos no peligrosos ingresarán para su almacenamiento
previamente segregados y clasificados por el mencionado proceso, donde se realizará la
recuperación de neumáticos en desuso, maderas descartadas, materia prima descartada,
alimentos descartados y asbesto no friable, entre otros.

Una vez clasificados, los materiales serán consolidades para posteriormente ser derivados a su
almacenamiento temporal en la Bodega de almacenamiento de residuos no que se habilitará en
el proceso de Transferencia y valorización de residuos no peligrosos permitirá almacenar los
residuos no peligrosos valorizados por dicho proceso, los cuales corresponderán a neumáticos
en desuso, maderas descartadas, materia prima descartada, alimentos descartados y asbesto no
friable, entre otros. Esta bodega contará con superficie de 180 [m [2] ].

Finalmente, una vez que los residuos son clasificados y almacenados temporalmente hasta
lograr consolidación de carga y acondicionados dentro de las posibilidades de las líneas de
proceso, serán enviados al destinatario final o valorizador autorizado que corresponda.

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 28 de 77

**1.3** **Identificación de fuentes de emisión**

Tabla 8 - Identificación de unidades con emisión de olor al ambiente

|Área|Unidad|Emite<br>olores<br>molestos al<br>ambiente<br>(Si/No)|Contribución de olor al ambiente|
|---|---|---|---|
|Compostaje|Patio de acopio de material estructurante|No|Acopio de material sin olores ofensivos|
|Compostaje|Galpón de compostaje|No|Emisiones canalizadas a sist. de abatimiento (biofiltro)|
|Compostaje|Sistema de abatimiento de olores/a|Sí|Biofiltro con eficiencia de remoción de olor de 95%|
|Compostaje|Trincheras/b|Sí|Trincheras con cobertor de 98% de retención de olor|
|Compostaje|Patio de maduración/c|Sí|Acopio con cobertura de 75% de retención de olor|
|Planta de<br>Carbonato|Almacenamiento|No|Emisiones canalizadas a sist. de abatimiento (biofiltro)|
|Planta de<br>Carbonato|Lavado de conchillas|No|Emisiones canalizadas a sist. de abatimiento (biofiltro)|
|Planta de<br>Carbonato|Cinta elevadora|No|Emisiones canalizadas a sist. de abatimiento (biofiltro)|
|Planta de<br>Carbonato|Horno|No|Emisiones canalizadas a sist. de abatimiento (biofiltro)|
|Planta de<br>Carbonato|Enfriador|No|Emisiones canalizadas a sist. de abatimiento (biofiltro)|
|Planta de<br>Carbonato|Triturado|No|Emisiones canalizadas a sist. de abatimiento (biofiltro)|
|Planta de<br>Carbonato|Molino|No|Emisiones canalizadas a sist. de abatimiento (biofiltro)|
|Planta de<br>Carbonato|Micromolienda|No|Emisiones canalizadas a sist. de abatimiento (biofiltro)|
|Planta de<br>Carbonato|Tamizado|No|Emisiones canalizadas a sist. de abatimiento (biofiltro)|
|Planta de<br>Carbonato|Empacado|No|Emisiones canalizadas a sist. de abatimiento (biofiltro)|
|Planta de<br>Carbonato|Chimenea scrubber (Calcinación)|Sí|Gases odorantes residuales de la torre de purificación|
|Planta de<br>Carbonato|Sistema de abatimiento de olores/a|Sí|Biofiltro con eficiencia de remoción de olor de 95%|
|Planta de<br>biogás|Estanque de recepción|No|Emisiones canalizadas a sist. de abatimiento (biofiltro)|
|Planta de<br>biogás|Estanque de higienización|No|Emisiones canalizadas a sist. de abatimiento (biofiltro)|
|Planta de<br>biogás|Sistema de abatimiento de olores/a|Sí|Biofiltro con eficiencia de remoción de olor de 95%|
|Planta de<br>biogás|Digestor anaeróbico|No|Unidad cerrada sin emisión de olores al ambiente|
|Planta de<br>biogás|Gasómetro|No|Unidad cerrada sin emisión de olores al ambiente|
|Planta de<br>biogás|Almacenamiento de digestato crudo|No|Unidad cerrada sin emisión de olores al ambiente|
|Planta de<br>biogás|Deshidratador|Sí|Unidad con emisión de olores al ambiente|
|Planta de<br>biogás|Laguna de digestato|Sí|Unidad con emisión de olores al ambiente|
|Planta de<br>biogás|Antorcha|No|Proceso de combustión de comp. orgánicos volátiles|
|Planta de trat.<br>de RILes|Estanque ecualizador|Sí|Estanques cerrados con ventilación|
|Planta de trat.<br>de RILes|Reactor de tratamiento aerobio SBR|Sí|Unidad con emisión de olores al ambiente|
|Segreg. y valor.<br>de res. sólidos<br>recuperables|Contenedor de descarte (no valorizables)|No|Unidad con materia prima sin aporte de olores|
|Segreg. y valor.<br>de res. sólidos<br>recuperables|Galpón de almacenamiento|No|Unidad con materia prima sin aporte de olores|
|Segreg. y valor.<br>de res. sólidos<br>recuperables|Zona despacho|No|Unidad con materia prima sin aporte de olores|
|Transferencia y<br>valorización de<br>residuos<br>peligrosos y no<br>peligrosos|Sector de segregación|No|Unidad sin aporte de olores al ambiente|
|Transferencia y<br>valorización de<br>residuos<br>peligrosos y no<br>peligrosos|Sector de almac. de res. peligrosos sólidos|No|Unidad sin aporte de olores al ambiente|
|Transferencia y<br>valorización de<br>residuos<br>peligrosos y no<br>peligrosos|Sector de descarte de marca|No|Unidad sin aporte de olores al ambiente|
|Transferencia y<br>valorización de<br>residuos<br>peligrosos y no<br>peligrosos|Bodega RESPEL|No|Unidad sin aporte de olores al ambiente|
|Caminos<br>interiores|Camiones de transporte/d|Sí|Unidad con emisiones fugitivas de los camiones de<br>traslado de material con eficiencia de remoción de 50%|

/a Para representar la condición más desfavorable, se proyectó el biofiltro con un valor conservador de eficiencia de remoción de

olor de 90%.
/b Para representar la condición más desfavorable, se proyectó la lámina cobertora con un valor conservador de retención de gases

odorantes de 90%.
/c Para representar la condición más desfavorable, se proyectó la lámina cobertora con un valor conservador de retención de gases

odorantes de 75%.
/d Para representar la condición más desfavorable, se proyectó la lámina cobertora con un valor conservador de retención de gases

odorantes de 50%.

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 29 de 77

**1.4** **Descripción de las fuentes de emisión**

En la siguiente tabla se muestran las fuentes odorantes identificadas en la operación futura de la planta.

Tabla 9 - Fuentes odorantes - Situación futura

|ID|Nombre fuente|Tipo de<br>fuente|Coordenadas UTM [m]<br>WGS84 18 G|Col5|
|---|---|---|---|---|
|ID|Nombre fuente|Tipo de<br>fuente|Este|Norte|
|1|Sistema de abatimiento de olores Compostaje - Biofiltro|Difusa|644.351|5.393.842|
|2|Trincheras|Difusa|644.295|5.393.676|
|3|Patio de maduración|Difusa|644.313|5.393.638|
|4|Chimenea Scrubber (Calcinación)|Puntual|644.533|5.393.734|
|5|Sistema de abatimiento de olores Carbonato- Biofiltro|Difusa|644.552|5.393.741|
|6|Sistema de abatimiento de olores Biogás - Biofiltro|Difusa|644.547|5.393.560|
|7|Deshidratador|Difusa|644.491|5.393.673|
|8|Laguna de digestato|Difusa|644.696|5.393.668|
|9|Estanque ecualizador 1|Difusa|644.393|5.393.614|
|10|Estanque ecualizador 2|Difusa|644.395|5.393.608|
|11|Estanque ecualizador 3|Difusa|644.398|5.393.604|
|12|Reactor de tratamiento aerobio SBR 1-1|Difusa|644.372|5.393.601|
|13|Reactor de tratamiento aerobio SBR 1-2|Difusa|644.376|5.393.596|
|14|Reactor de tratamiento aerobio SBR 2-1|Difusa|644.379|5.393.591|
|15|Reactor de tratamiento aerobio SBR 2-2|Difusa|644.382|5.393.586|
|16|Camiones de transporte|Fugitiva|645.423|5.393.115|

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 30 de 77

Figura 15 - Distribución espacial de fuentes odorantes del Proyecto

Fuente: Envirometrika, basado en layout de obras proyectadas, 2023.

Figura 16 - Distribución espacial de fuentes odorantes (zoom)

Fuente: Envirometrika, basado en layout de obras proyectadas, 2023.

ANTECEDENTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 31 de 77

**2** **OBJETIVOS**

**2.1** **Objetivo general**

Proyectar el alcance odorante de la futura Plataforma de Economía Circular Volta Los Lagos, bajo
condición operacional definida por el Titular.

**2.2** **Objetivos específicos**

 Recopilación de antecedentes operacionales asociadas al proyecto.

 - Identificación de fuentes odorantes con emisión directa al aire ambiente.

 Recopilación de emisiones de referencia aplicables al proyecto.

 Caracterización estructural, espacial y operacional de fuentes de emisión de olor.

 Proyectar vía modelación de dispersión odorante las emisiones asociadas a la condición operacional

futura del proyecto.

 Determinar el área de influencia del proyecto para la componente olor.

 - Evaluar el alcance odorante de las emisiones del proyecto según niveles de concentración C P98-1hr = 2,

3 y 4 [ou E /m [3] ], definidos por la normativa italiana de referencia, Provincia de Trento.

 Cuantificar niveles de concentración de olor generados por el proyecto en receptores.

OBJETIVOS www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 32 de 77

**3** **ESTIMACIÓN DE EMISIONES**

De acuerdo con lo señalado en la “Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA” [13],
las emisiones de referencia son aquellas que han sido estimadas a partir de la toma de muestras de olor en
la fuente y su respectiva caracterización. La selección y aplicación de emisiones de referencia, se realiza
sobre la base de proyectos o actividades similares al proyecto que se somete a evaluación ambiental. Es
importante considerar que las condiciones de operación o funcionamiento de las fuentes existentes o de
referencia también sean análogas al proyecto.

Respecto al uso de factores de emisión de olor, se define como la relación entre la cantidad de contaminante
emitido a la atmósfera y una unidad de actividad. La unidad de actividad puede consistir en datos de
producción, horas de operación de la fuente, área superficial involucrada u otros.
El uso de factores de emisión es aconsejable sólo en proyectos nuevos, y siempre que no se cuente con
emisiones de referencia, en este caso, se deben utilizar preferentemente factores publicados por agencias
estatales de protección del medio ambiente, normas o guías técnicas relacionadas [14] .

En relación con lo anterior, se consultaron en una primera instancia fuentes públicas de información
ambiental correspondientes al Sistema de Evaluación de Impacto Ambiental (SEIA) y Sistema de Nacional de
Información de Fiscalización Ambiental (SNIFA). De los proyectos aprobados cuyas actividades fueran
asimilables al proyecto en evaluación, se seleccionaron aquellos Estudios de Impacto odorante (EIO) cuya
caracterización de emisiones fuera realizada bajo los requerimientos normativos vigentes, NCh 3190:2010 [15] y
NCh 3386:2015 [16] .

Para las áreas de proceso donde no se dispone de suficiente información, a nivel nacional, para la
caracterización de emisiones, fue necesario aplicar factores de emisión de olor provenientes de estudios
internacionales para su representación en el modelo de dispersión.

**3.1** **Emisiones de referencia**

Los valores de emisión utilizados para caracterizar el ciclo de emisión de olor de las fuentes asociadas a
la futura operación de la Plataforma de Economía Circular Volta Los Lagos, provienen de lo muestreado
en Estudios de Impacto Odorante (EIO) desarrollados en los siguientes proyectos de referencia:

13 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA. Ministerio del Medio

Ambiente. Chile.
14 Ibid.
15 Instituto Nacional de Normalización. (2010). NCh 3190:2010 Calidad del aire - Determinación de la concentración de olor por olfatometría

dinámica. Chile.
16 Instituto Nacional de Normalización. (2015). NCh 3386:2015 Calidad del aire - Muestreo estático para olfatometría. Chile.

ESTIMACIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 33 de 77

Tabla 10 - Proyectos de referencia asimilables al proyecto

|Proyecto de referencia|Titular|Fuente de información|Link de expediente SEIA|
|---|---|---|---|
|Mejoramiento y Transformación<br>Ecomaule:<br>Plataforma<br>de<br>Reciclaje y Valorización|Ecomaule S.A17.|Servicio de Evaluación de<br>Impacto Ambiental|https://seia.sea.gob.cl/expediente/expedien<br>tesEvaluacion.php?modo=ficha&id_expedie<br>nte=2149076836|
|Planta de Carbonato de Calcio<br>CALAGRO|Inversiones Las<br>Garzas S.A. 18,19|Servicio de Evaluación de<br>Impacto Ambiental/ Sistema<br>Nacional de Información de<br>Fiscalización Ambiental|https://seia.sea.gob.cl/expediente/expedien<br>tesEvaluacion.php?modo=ficha&id_expedie<br>nte=7226669<br>https://snifa.sma.gob.cl/Fiscalizacion/Ficha/<br>1045139|
|Odours Prevention and Control<br>in the Shell Waste Valorisation|Barros, C. et<br>al20|Universidad de Santiago de<br>Compostela / Calizas Marinas S.A.|https://www.researchgate.net/publication/2<br>64876859_Odours_Prevention_and_Control<br>_in_the_Shell_Waste_Valorisation#pf4|

Tabla 11 - Emisiones de referencia aplicados en la situación futura

|ID|Fuente|Tipo de<br>fuente|EO por sup.<br>[ou/m2s]<br>E|Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E|Estudio de<br>referencia|
|---|---|---|---|---|---|
|1|Sistema de abatimiento de olores Compostaje - Biofiltro|Difusa|12,05|352,80|A|
|2|Trincheras|Difusa|0,83|5.736,96|A|
|3|Patio de Maduración|Difusa|0,40|1.200,00|A|
|4|Chimenea Scrubber (Calcinación)|Puntual|31.100,91|24.426,60|B|
|5|Sistema de abatimiento de olores Carbonato- Biofiltro|Difusa|96,38|2.822,02|C|
|6|Sistema de abatimiento de olores Biogás - Biofiltro|Difusa|20,87|611,01|B|
|7|Deshidratador|Difusa|0,32|1,20|A|
|8|Laguna de digestato|Difusa|0,32|2.592,00|A|
|9|Estanque ecualizador 1|Difusa|3,80|41,75|A|
|10|Estanque ecualizador 2|Difusa|3,80|41,75|A|
|11|Estanque ecualizador 3|Difusa|3,80|41,75|A|
|12|Reactor de tratamiento aerobio SBR 1-1|Difusa|19,08|1.431,00|A|
|13|Reactor de tratamiento aerobio SBR 1-2|Difusa|19,08|1.431,00|A|
|14|Reactor de tratamiento aerobio SBR 2-1|Difusa|19,08|1.431,00|A|
|15|Reactor de tratamiento aerobio SBR 2-2|Difusa|19,08|1.431,00|A|
|16|Camiones de transporte|Difusa|0,05|1.790,40|A, B, C|

A: Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y Valorización [21] .
B: Planta de Carbonato de Calcio CALAGRO. [22], [23]
C: Odours Prevention and Control in the Shell Waste Valorisation. [24]

17 Ecomaule S.A. (2020). P6168 Estudio de Impacto Odorante: Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y

Valorización. SEIA, Chile.
18 Inversiones Las Garzas S.A. (2013). Planta de Carbonato de Calcio CALAGRO. SEIA, Chile.
19 Inversiones Las Garzas S.A. (2020). Planta de Carbonato de Calcio CALAGRO. SNIFA, Chile.
20 Barros, C. et. al. (2007). Odours Prevention and Control in the Shell Waste Valorisation. España.
21 Ecomaule S.A. (2020). P6168 Estudio de Impacto Odorante: Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y

Valorización. SEIA, Chile.
22 Inversiones Las Garzas S.A. (2013). Planta de Carbonato de Calcio CALAGRO. SEIA, Chile.
23 Inversiones Las Garzas S.A. (2020). Planta de Carbonato de Calcio CALAGRO. SNIFA, Chile.
24 Barros, C. et. al. (2007). Odours Prevention and Control in the Shell Waste Valorisation. España.

ESTIMACIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 34 de 77

Para representar la condición más desfavorable de emisión, en la proyección operacional de la
instalación tanto para la estimación de emisiones como para su ingreso al modelo, se aplicaron los
siguientes criterios:

Adicionalmente, para representar las condiciones más desfavorables de emisión asociadas a la
elaboración de compost agrícolas a través del proceso de compostaje se incluyeron las actividades de
carga y descarga de material, tanto en el manejo de trincheras como del patio de maduración donde se
tendría emisión directa de olores por ciertos periodos acotados de tiempo. Siendo proyectados los
incrementos de emisión asociados al retiro parcial de la lámina cobertora en trincheras durante el
ingreso y retiro de material, basado en el nivel de actividad y frecuencia de carga/descarga declarada
por el Titular.

En el manejo de las pilas del patio de maduración se integraron incrementos en la emisión desde el
desarme de trinchera hasta que el material es dispuesto en el patio de maduración, incluyendo
actividades de volteos realizados durante el proceso de estabilización, donde se tendría emisión directa
al ambiente producto del retiro temporal de la lámina impermeable.

Del mismo modo, se incluyó la contribución de olor asociadas al transporte de insumos, productos y
residuos considerando la frecuencia de ingreso y retiro diario de camiones, así como la caracterización
de emisiones según tipo de material y características del transporte.

El detalle de la estimación de emisión de olor para cada una de estas unidades se describe en Anexo 2.

**3.2** **Emisiones según olor simple o compuesto**

De la Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA (2017, página 18), se tiene
que: El olor simple es el que percibe el olfato como consecuencia de la emisión de un compuesto
químico o sustancia olorosa determinada. Los olores de tipo simple suelen ser fácilmente identificables
(Díaz et al., 2013), por ejemplo, el ácido sulfhídrico (H 2 S) siendo una sustancia olorosa que se identifica
fácilmente con el descriptor de huevos podridos. En cambio, el olor compuesto es el que se percibe
como consecuencia de la mezcla de más de un olor simple, pudiendo producirse fenómenos de
sinergias, interferencias e inhibiciones, y por lo mismo, en la percepción del olor compuesto no siempre
es fácil definir y atribuir las moléculas que lo causan, no pudiendo identificarlo con un único descriptor
de olor.

El presente proyecto considera una serie de operaciones potencialmente generadoras de olor atribuibles
a olores compuestos ya que no es una actividad que genera sólo un olor simple o una única sustancia o
compuesto gaseoso.

ESTIMACIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 35 de 77

Existe una forma de acceder al menos a la familia de compuestos e idealmente al gas precursor del olor
analizando los descriptores o notas de olor con la rueda de olor, en este caso se utilizó la rueda de olor
de Plantas de Tratamiento de Residuos Líquidos, la cual nos acerca a los compuestos que pudieran estar
relacionados. A continuación, se indican las notas de olor consideradas como ofensivas, asimilables al
proyecto:

 Sulfuroso.

 Descomposición.

 - Agrio.

 Ácido.

 Percolado.

 - Terroso.

ESTIMACIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 36 de 77

**3.3** **Descripción de fuentes emisoras de olor**

Tabla 12 - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 1

|Requisito|Col2|Sistema de<br>abatimiento de<br>olores<br>Compostaje -<br>Biofiltro|Trinch eras|Patio de<br>madur ación|Chimenea<br>scrub ber|Sistema de<br>abatimiento de<br>olores<br>Carbonato-<br>Biofiltro|Sistema de<br>abatimiento de<br>olores Biogás -<br>Biofiltro|Deshidratador|Laguna de<br>digestato|
|---|---|---|---|---|---|---|---|---|---|
|Fase del proyecto que<br>genera olor|Fase del proyecto que<br>genera olor|Operación|Operación|Operación|Operación|Operación|Operación|Operación|Operación|
|Actividad que genera<br>emisiones de olor|Actividad que genera<br>emisiones de olor|Tratamiento<br>(sistema de<br>abatimiento)|Estabilización<br>de compost|Estabilización<br>de compost|Calcinación|Tratamiento<br>(sistema de<br>abatimiento)|Tratamiento<br>(sistema de<br>abatimiento)|Deshidratación<br>de digestato|Digestión<br>anaeróbica|
|Identificación del material<br>o sustancia olorosa|Identificación del material<br>o sustancia olorosa|Compost|Compost|Compost|Gases de<br>calcinación de<br>conchillas|Recepción y<br>almacenamiento<br>de conchillas|Recepción de<br>lodos|Digestato|Digestato|
|Tipo de fuente|Tipo de fuente|Difusa|Difusa|Difusa|Puntual|Difusa|Difusa|Difusa|Difusa|
|Régimen<br>de<br>emisión<br>de olor|Ciclo<br>operacional|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|
|Régimen<br>de<br>emisión<br>de olor|Horario de<br>operación|24 [h]|24 [h]|8:00 - 20:59<br>[h]/a|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|
|Régimen<br>de<br>emisión<br>de olor|Frecuencia<br>mensual|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|
|Emisión de olor<br>[ouE/m2*s]|Emisión de olor<br>[ouE/m2*s]|12,05|0,83|0,40|31.100,91|96,38|20,87|0,32|0,32|
|Tasa de emisión de olor<br>[ouE/s]|Tasa de emisión de olor<br>[ouE/s]|352,80|5.736,96|1.200,00|24.426,60|2.822,02|611,01|1,20|2.592,00|
|Tono Hedónico|Tono Hedónico|S/I/b|S/I/b|S/I/b|-3|S/I/d|S/I/b|S/I/b|S/I/a|
|Intensidad|Intensidad|S/I/b|S/I/b|S/I/b|3|S/I/d|S/I/b|S/I/b|S/I/a|
|Ofensividad|Ofensividad|S/I/b|S/I/b|S/I/b|3|S/I/d|S/I/b|S/I/b|S/I/a|
|Calidad|Calidad|Humedad,<br>percolado,<br>agrio/b|Basura,<br>descomposición,<br>agrio/b|Tierra,<br>humedad,<br>basura/b|Marino,<br>rancio,<br>amoniaco/c|S/I/d|S/I/b|S/I/b|S/I/a|

S/I: Sin información
/a Para representar la condición operacional más desfavorable se consideró en el modelo un funcionamiento continuo (00:00-23:59 [h], todos los días del año).
/b P6168 Estudio de Impacto Odorante: Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y Valorización.
/c Planta de Carbonato de Calcio CALAGRO.

/d Odours Prevention and Control in the Shell Waste Valorisation

ESTIMACIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 37 de 77

Tabla 13 - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 2

|Requisito|Col2|Estanque<br>ecualizador 1|Estanque<br>ecualizador 2|Estanque<br>ecualizador 3|Reactor de<br>tratamiento<br>aerobio SBR<br>1-1|Reactor de<br>tratamiento<br>aerobio SBR<br>1-2|Reactor de<br>tratamiento<br>aerobio SBR<br>2-1|Reactor de<br>tratamiento<br>aerobio SBR<br>2-2|Camiones de<br>transporte|
|---|---|---|---|---|---|---|---|---|---|
|Fase del proyecto que<br>genera olor|Fase del proyecto que<br>genera olor|Operación|Operación|Operación|Operación|Operación|Operación|Operación|Operación|
|Actividad que genera<br>emisiones de olor|Actividad que genera<br>emisiones de olor|Tratamiento<br>de RILes|Tratamiento<br>de RILes|Tratamiento<br>de RILes|Tratamiento<br>de RILes|Tratamiento<br>de RILes|Tratamiento<br>de RILes|Tratamiento<br>de RILes|Transporte de<br>materiales|
|Identificación del<br>material o sustancia<br>olorosa|Identificación del<br>material o sustancia<br>olorosa|Digestato|Digestato|Digestato|Digestato|Digestato|Digestato|Digestato|Recepción y<br>almacenamiento<br>de conchillas,<br>Digestato y<br>Compost|
|Tipo de fuente|Tipo de fuente|Difusa|Difusa|Difusa|Difusa|Difusa|Difusa|Difusa|Fugitiva|
|Régimen de<br>emisión de<br>olor|Ciclo<br>operacional|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|
|Régimen de<br>emisión de<br>olor|Horario de<br>operación|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|12 [h]|
|Régimen de<br>emisión de<br>olor|Frecuencia<br>mensual|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|
|Emisión de olor<br>[ouE/m2*s]|Emisión de olor<br>[ouE/m2*s]|3,80|3,80|3,80|19,08|19,08|19,08|19,08|0,05|
|Tasa de emisión de olor<br>[ouE/s]|Tasa de emisión de olor<br>[ouE/s]|41,75|41,75|41,75|1.431,00|1.431,00|1.431,00|1.431,00|1.790,80|
|Tono hedónico|Tono hedónico|S/I/a|S/I/a|S/I/a|S/I/a|S/I/a|S/I/a|S/I/a|S/I/a|
|Intensidad|Intensidad|S/I/a|S/I/a|S/I/a|S/I/a|S/I/a|S/I/a|S/I/a|S/I/a|
|Ofensividad|Ofensividad|S/I/a|S/I/a|S/I/a|S/I/a|S/I/a|S/I/a|S/I/a|S/I/a|
|Calidad|Calidad|S/I/a|S/I/a|S/I/a|Detergente,<br>humedad,<br>ácido/a|Detergente,<br>humedad,<br>ácido/a|Detergente,<br>humedad,<br>ácido/a|Detergente,<br>humedad,<br>ácido/a|S/I/a|

S/I: Sin información
/a P6168 Estudio de Impacto Odorante: Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y Valorización.

ESTIMACIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 38 de 77

Tal como señala la sección 2.3.1 de la Guía para la Predicción y Evaluación de Impactos por Olor en el
SEIA (SEA, 2017), para caracterizar las emisiones de una fuente odorante en sus cuatro dimensiones
(concentración, intensidad, calidad y tono hedónico), es necesaria la toma de muestra y posterior
análisis en cumplimiento a los requerimientos descritos en las norma NCh3386:2015 [25] Muestreo Estático
para Olfatometría y NCh3190:2010 [26] Determinación de la Concentración de Olor por Olfatometría
Dinámica. En lo que respecta a este criterio, dado que el proyecto corresponde a una instalación futura
cuyas unidades de proceso y tratamiento aún no han sido construidas, no sería aplicable su
caracterización hasta que lleve a cabo su construcción y que se encuentren en régimen de operación
normal para su muestreo, análisis y caracterización olfatométrica de estas dimensiones.

A modo de referencia, se complementaron las características del olor en base a los antecedentes
disponibles en los estudios de referencia, para aquellas fuentes odorantes asimilables al proyecto. Es
importante destacar que las particularidades (Ej. parámetros operacionales) de cada fuente odorífera
determinan las características del olor, por lo que esta información debe ser interpretada únicamente
como una referencia en el contexto de este estudio.

**3.4** **Ranking de emisiones**

Una fuente con la mayor concentración no necesariamente se relaciona con una mayor emisión, ya que
esta última dependerá de sus características operacionales y estructurales. A su vez, una fuente con la
mayor emisión no siempre genera mayor exposición en las zonas de percepción de olor, ya que éste
último dependerá de diversos factores como: variables meteorológicas, geográficas y topográficas de la
zona en estudio, las características particulares del terreno, de emplazamiento de las fuentes, de la zona
de inmisión, las características estructurales de las fuentes, como la altura y el área de exposición.
También influye el tipo de fuente ya sea puntual, difusa o fugitiva.

Todo lo anterior deriva en que un mismo valor de emisión puede generar un mayor o menor nivel de
exposición dependiendo de las características antes mencionadas. Por lo tanto, mediante la modelación
de esta emisión, se pueden determinar las fuentes que generen mayores niveles de exposición, y en
cuál de éstas es recomendable realizar modificaciones estructurales u operacionales para poder obtener
una reducción relevante en el área de percepción.

A continuación, se indican las TEO [ou E /s] para cada fuente emisora, considerados en el futuro
escenario operacional. Las fuentes emisoras están ordenadas en forma descendente en función de su
valor de TEO.

25 Instituto Nacional de Normalización. (2015). NCh 3386:2015 Calidad del aire - Muestreo estático para olfatometría. Chile.
26 Instituto Nacional de Normalización. (2010). NCh 3190:2010 Calidad del aire - Determinación de la Concentración de Olor por

Olfatometría Dinámica. Chile.

ESTIMACIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 39 de 77

Tabla 14 - Ranking TEO [ou E /s] por fuente modelada - Situación futura

|ID|Unidad|EO<br>[ou /m2s]<br>E|TEO<br>[ou /s]<br>E|% TEO|% TEO<br>acum.|
|---|---|---|---|---|---|
|4|Chimenea Scrubber (Calcinación)|31.100,91|24.426,60|52,37%|52,37%|
|2|Trincheras|0,88|6.093,43|13,07%|65,44%|
|5|Sistema de abatimiento de olores Carbonato- Biofiltro|96,38|2.822,02|6,05%|71,49%|
|8|Laguna de digestato|0,32|2.592,00|5,56%|77,05%|
|3|Patio de maduración|0,70|2.099,61|4,50%|81,55%|
|16|Camiones de transporte|0,05|1.790,40|3,84%|85,39%|
|12|Reactor de tratamiento aerobio SBR 1-1|19,08|1.431,00|3,07%|88,46%|
|13|Reactor de tratamiento aerobio SBR 1-2|19,08|1.431,00|3,07%|91,53%|
|14|Reactor de tratamiento aerobio SBR 2-1|19,08|1.431,00|3,07%|94,59%|
|15|Reactor de tratamiento aerobio SBR 2-2|19,08|1.431,00|3,07%|97,66%|
|6|Sistema de abatimiento de olores Biogás - Biofiltro|20,87|611,01|1,31%|98,97%|
|1|Sistema de abatimiento de olores Compostaje - Biofiltro|12,05|352,80|0,76%|99,73%|
|9|Estanque ecualizador 1|3,80|41,75|0,09%|99,82%|
|10|Estanque ecualizador 2|3,80|41,75|0,09%|99,91%|
|11|Estanque ecualizador 3|3,80|41,75|0,09%|100,00%|
|7 <br>|Deshidratador|0,32|1,20|0,00%<br>|100,00%<br>|

**TEO Total [ou** **E** **/s] 46.638,32**

EO: Emisión Odorante; TEO: Tasa de Emisión de Olor.

ESTIMACIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 40 de 77

**4** **PREDICCIÓN DE IMPACTOS POR OLOR**

**4.1** **Metodologías para la predicción de impactos por olor**

La metodología para realizar la predicción de impactos por olor del presente estudio sigue los
lineamientos de la “Guía para la predicción y evaluación de impactos por olor en el SEIA” [27], en la cual se
presentan los métodos que se utilizan para la predicción de impactos por olor, donde se desarrollan las
obras o acciones contenidas en un proyecto o actividad tendientes a materializar una o más de sus fases
de operación, como se observa en la siguiente figura:

Figura 17 - Método para la predicción de impactos por olor

Fuente: Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA [28]

27 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA. Ministerio del Medio

Ambiente. Chile.
28 Ibid.

PREDICCIÓN DE IMPACTOS POR OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 41 de 77

**4.2** **Antecedentes para el área de influencia**

El presente estudio se basó en los lineamientos establecidos en la “Guía para la Descripción del Área de
Influencia” [29] y la “Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA” [30] del Servicio
de Evaluación Ambiental, para proyectos sometidos al Sistema de Evaluación de Impacto Ambiental
(SEIA). Lo anterior, abordando y justificando las letras a), c), d) y e) del artículo 11 de la Ley No
19.300 [31], aplicables para la componente olor del proyecto en evaluación.

Con relación a la predicción de impactos por olor, la Guía de Olores [32], (SEA, 2017), señala que “Para
predecir los impactos por emisiones de olor es necesario levantar información sobre estos elementos en
el AI (Área de Influencia)”. En el contexto del SEIA el AI se considera como el área o espacio geográfico
cuyos atributos y elementos deben ser considerados con la finalidad de definir si el proyecto o actividad
genera impactos significativos o bien para justificar su inexistencia.

La determinación del Área de Influencia se define a partir de la pluma odorante obtenida desde el
modelo de dispersión, cuyo espacio se circunscribe usualmente a la isocurva de concentración de 1

[ou E /m [3] ], correspondiente al umbral de detección de olor compuesto.

Basado en los instrumentos de planificación territorial vigentes, el proyecto se emplaza en una zona
fuera del límite urbano del Plan Regulador Comunal de Maullín [33], a una distancia aproximada de 28

[km].

Figura 18 - Emplazamiento del proyecto según planificación territorial vigente

Fuente: Elaboración propia, a partir de Instrumentos de Planificación Territorial MINVU [34], 2023.

29 Servicio de Evaluación Ambiental. (2017). Guía para la Descripción de la Calidad del Aire en el Área de Influencia de Proyectos que

Ingresan al SEIA. Departamento de Estudios y Desarrollo - División de Evaluación y Participación Ciudadana. Chile.
30 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA. Ministerio del Medio

Ambiente. Chile.
31 Ministerio del Medio Ambiente. (2011). Ley No 19.300, sobre Bases Generales del Medio Ambiente - Ley Orgánica de la Superintendencia

del Medio Ambiente. División Jurídica del Medio Ambiente. Chile.
32 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA. Ministerio del Medio

Ambiente. Chile.
33 Municipalidad de Maullín. (2022). Promulga Plan Regulador Comunal de Maullín. Gobierno Regional de Los Lagos. Chile.

PREDICCIÓN DE IMPACTOS POR OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 42 de 77

**4.2.1** **Descripción del área de influencia según elementos del medio ambiente**

Tal como señala la Guía de Olores [35] (SEA, 2017), las personas son las que perciben el olor y, por
lo tanto, son las receptoras de impactos por este tipo de emisiones. En coherencia a lo anterior,
se adapta al ámbito de olores el concepto de la norma de emisión de ruido [36], la cual define
como receptor toda persona que habite, resida o permanezca en un recinto, ya sea en un
domicilio particular o en un lugar de trabajo, que esté o pueda estar expuesta a olores
generados por una fuente emisora de olor externa. De acuerdo con lo establecido en el artículo
11 de la Ley N° 19.300 [37], las personas receptoras de impactos por olor se asocian con los
siguientes elementos del medio ambiente:

 Población, en cuanto a salud de la población (letra a).

 - Grupos humanos, en cuanto a sus sistemas de vida y costumbres (letra c).

 Población protegida (letra d).

 Visitantes o turistas, en cuanto componen el valor turístico de una zona (letra e).

**4.2.2** **Identificación de receptores de olor**

Los receptores de olor corresponden a las personas que perciben el olor y, por lo tanto, los
posibles impactos por emisiones de esta componente. Además de la presencia de personas,
también se debe considerar como receptores, los sitios donde los grupos humanos realizan sus
actividades, incluyendo actividades que desarrollan los visitantes o turista, por ejemplo:
viviendas; instalaciones asociadas al asentamiento de los grupos humanos en el territorio, como
bodegas de granos y talleres, hospitales, establecimientos educacionales y de recreación.

De acuerdo con lo anterior, los puntos receptores de interés considerados en el estudio se
georreferencian a continuación:

34 Geoportal MINVU. (2022). Plan Regulador Comunal de Maullín. Ministerio de Vivienda y Urbanismo. Chile.
35 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA. Ministerio del Medio

Ambiente. Chile.
36 Ministerio del Medio Ambiente. (2012). Decreto Supremo N°38/11 del Ministerio del Medio Ambiente - Norma de Emisión de Ruidos

Generados por Fuentes que Indica. Publicado en el Diario Oficial el 12 de junio de 2012.
37 Ministerio Secretaría General de la Presidencia. (2016). Ley 19.300 Aprueba Ley Sobre Bases Generales del Medio Ambiente. Ministerio

Secretaría General de la Presidencia. Chile.

PREDICCIÓN DE IMPACTOS POR OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 43 de 77

Tabla 15 - Puntos receptores de interés

|ID|Descripción|Coordenadas UTM [m]<br>(WGS84-18 G)|Col4|Distancia de<br>receptor desde<br>perímetro<br>predial<br>[m]|Orientación|
|---|---|---|---|---|---|
|ID|Descripción|X: Este|Y: Sur|Y: Sur|Y: Sur|
|R1|Vivienda ubicada fuera del límite urbano<br>de Maullín|643.642|5.393.170|636|OSO|
|R2|Vivienda ubicada fuera del límite urbano<br>de Maullín|643.846|5.393.126|472|SO|
|R3|Vivienda ubicada fuera del límite urbano<br>de Maullín|643.905|5.392.985|493|SO|
|R4|Vivienda ubicada fuera del límite urbano<br>de Maullín|643.884|5.392.862|580|SO|
|R5|Vivienda ubicada fuera del límite urbano<br>de Maullín|644.596|5.392.490|858|S|
|R6|Vivienda ubicada fuera del límite urbano<br>de Maullín|645.279|5.393.031|649|SE|
|R7|Vivienda ubicada fuera del límite urbano<br>de Maullín|645.426|5.393.416|502|ESE|
|R8|Vivienda ubicada fuera del límite urbano<br>de Maullín|645.430|5.393.521|439|ESE|
|R9|Vivienda ubicada fuera del límite urbano<br>de Maullín|645.728|5.393.863|584|E|
|R10|Vivienda ubicada fuera del límite urbano<br>de Maullín|645.681|5.394.079|623|ENE|
|R11|Vivienda ubicada fuera del límite urbano<br>de Maullín|645.430|5.394.234|474|ENE|
|R12|Vivienda ubicada fuera del límite urbano<br>de Maullín|644.968|5.394.229|79|NE|
|R13|Vivienda ubicada fuera del límite urbano<br>de Maullín|644.950|5.394.281|63|NE|
|R14|Vivienda ubicada fuera del límite urbano<br>de Maullín|645.051|5.394.456|255|NNE|
|R15|Vivienda ubicada fuera del límite urbano<br>de Maullín|645.162|5.393.860|33|E|
|R16|Vivienda ubicada fuera del límite urbano<br>de Maullín|645.603|5.393.258|760|ESE|
|R17|Vivienda ubicada fuera del límite urbano<br>de Maullín|645.395|5.393.441|471|ESE|
|R18|Vivienda ubicada fuera del límite urbano<br>de Maullín|645.335|5.393.068|675|SE|

PREDICCIÓN DE IMPACTOS POR OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 44 de 77

Figura 19 - Distribución de receptores de interés

Fuente: Envirometrika - Google Earth, 2023.

**4.2.3** **Olor base en situación sin proyecto**

La Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA [38], señala: “es necesario
considerar el olor al que están expuestos los receptores en el AI de la situación sin proyecto”.
Para caracterizar la zona de emplazamiento con respecto a otras actividades que puedan ser
potenciales generadores de olor en la situación proyecto inexistente, se utilizó la plataforma de
Mapa de Proyectos del Servicio de Evaluación Ambiental (SEA) [39] . Esta herramienta permite
visualizar todos los proyectos de la zona de interés, y así caracterizar el tipo de industria o
emisión de olor base.

En relación con lo anterior, describen los proyectos potencialmente generadores de olor,
cercanos al lugar de emplazamiento del proyecto, basado en información pública disponible en
las plataformas del Sistema de Evaluación de Impacto Ambiental (SEIA). Los establecimientos
considerados se describen a continuación:

38 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA. Ministerio del Medio

Ambiente. Chile.
39 [Servicio de Evaluación Ambiental (2019). Mapa de proyectos http://sig.sea.gob.cl/mapadeproyectos/. Chile.](http://sig.sea.gob.cl/mapadeproyectos/)

PREDICCIÓN DE IMPACTOS POR OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 45 de 77

Tabla 16 - Proyectos aprobados por el SEA

|Nombre del proyecto|Titular del proyecto|N.o RCA|Distancia del<br>proyecto<br>desde el<br>perímetro<br>predial [m]|Coordenadas UTM<br>[m]|Col6|
|---|---|---|---|---|---|
|Nombre del proyecto|Titular del proyecto|N.o RCA|Distancia del<br>proyecto<br>desde el<br>perímetro<br>predial [m]|X: Este|Y: Norte|
|Planta procesadora de<br>recursos hidrobiológicos-<br>pesquera La Portada (PPRH-<br>PP)|Pesquera La Portada<br>S.A.|429/05|2.370|644.942|5.396.639|
|Sistema de neutralización y<br>depuración de Residuos<br>Industriales Líquidos<br>(Gelymar S.A.)|Extractos Naturales<br>Gelymar S.A.|176/00|6.191|650.820|5.396.173|
|Planta de Carbonato de<br>Calcio CALAGRO|Inversiones Las<br>Garzas S.A.|105/13|8.738|653.180|5.397.182|
|Modificación proyecto retiro,<br>transporte y almacenamiento<br>prolongado de Respel Rexin|Rexin SpA.|273/08|1.988|646.800|5.395.140|
|Sistema de adecuación de<br>lodos orgánicos Rexin|Rexin SpA.|157/08|1.988|646.800|5.395.140|

Figura 20 - Proyectos aprobados por el Servicio de Evaluación Ambiental

Fuente: Envirometrika - Google Earth, 2023.

Respecto a la contribución de olor de otros proyectos en el área de influencia, la Guía para el
Uso de Modelos de Calidad del Aire en el SEIA (SEA, 2023), en la sección 8.1 “Caracterización
de Calidad del Aire” señala que “El análisis de la acumulación de los impactos en el área de
influencia del proyecto debe evaluarse caso a caso, distinguiéndose entre la concentración
“medida” y la concentración proveniente del aporte de “otros proyectos’”. Lo anterior, haciendo
referencia a la medición de la calidad del aire en estaciones monitoras emplazadas en zonas que
representen la calidad del aire de los receptores de interés del área de influencia respectiva del

PREDICCIÓN DE IMPACTOS POR OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 46 de 77

proyecto en evaluación. Cabe señalar, que en el caso de la componente olor, a nivel global, no
se ha desarrollado algún tipo de tecnología que permita tanto la medición continua de
concentración de olor como su caracterización sensorial (Ej. tono hedónico, intensidad,
descriptores, entre otros). Por lo cual no sería posible evaluar la acumulación de impactos a
través de esta metodología.

Complementariamente, la Guía señala que ...” siempre que sea posible, se debe considerar en el
aporte de “otros proyectos” aquellos que coincidan en el área de influencia de calidad del aire y
temporalidad del proyecto en evaluación, además que presenten los antecedentes de
modelación de calidad del aire para estos análisis, siendo requisito que sus procesos de
calificación ambiental hayan sido considerados favorables”. En relación con este criterio, se
realizó un levantamiento en el Sistema de Evaluación de Impacto Ambiental de otros proyectos
cercanos con RCA favorable y no se encontró ninguno que presentara coincidencia en su área
de influencia de olor, correspondiente a la isocurva de concentración de 1 [ou E /m [3] ], respecto a
la de Plataforma de Economía Circular. Dado lo anterior, no sería aplicable realizar una
evaluación del efecto sinérgico o contribución de olor de otros proyectos, simulando una
incidencia ambiental mayor a la declarada en este estudio de impacto odorante.

Cabe señalar que, si bien la modelación de olores utiliza los mismos principios aplicados en la
emisión al ambiente de cualquier otro contaminante, presenta algunas características propias
que deben ser consideradas al momento de realizar este tipo de análisis. En este contexto, la
Agencia de Protección Ambiental de Irlanda [40] (EPA) señala que la incorporación de los niveles
ambientales de línea base de olor a los resultados del modelo de un proyecto no es considerado
como un enfoque válido. Debido a que los olores generalmente no son aditivos debido a la
sinergia y efecto no lineal de la mezcla de compuestos odorantes en el ambiente.

Del mismo modo, diversos expertos internacionales exponen en el Manual de Modelación de
Olores [41], algunos fundamentos y enfoques que van desde su inaplicabilidad debido al carácter
multidimensional de los olores, el desconocimiento de la sinergia de la mezcla de compuestos
odorantes en el ambiente y de la limitada información disponible para la caracterización de las
condiciones de emisión de otras instalaciones aledañas (Ej. cantidad de fuentes, tipos de
fuentes, régimen de emisión, tasa de emisión, entre otras). Por lo cual, de aplicar este tipo de
metodología, los resultados obtenidos en el análisis de los impactos acumulativos de olor
estarían sujetos a un gran número de supuestos e incertidumbre que afectaría de alguna forma
la representatividad del análisis.

40 Environmental Protection Agency. (2020). Air Dispersion Modelling from Industrial Installations Guidance Note (AG4). Office of

Environmental Enforcement (OEE), Ireland.
41 Olores.org & Asociación Medioambiental Internacional de Gestores del Olor (AMIGO). (Draft, 2023). Handbook Odour Exposure Modelling

- International Handbook on the Assessment of Odour Exposure by using Dispersion Modelling.

PREDICCIÓN DE IMPACTOS POR OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 47 de 77

**5** **ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR**

**5.1** **Estimación concentración límite de exposición**

Los modelos de dispersión odorante normalmente utilizan un criterio horario (1 hora), basado en la
evaluación odorante alemana. Por lo tanto, la evaluación de olor está basada en la frecuencia de
ocurrencia de las horas de olor en el año [42] . La mayoría de las guías de modelación de olor toman en
cuenta al menos un 98% de las horas del año para evaluar el impacto de las emisiones generadas por
las fuentes representadas. En relación con lo anterior, se recomienda el uso de percentil 98 para
propósitos comparativos. [43-44]
Environment Agency (UK) recomienda el percentil 98, como el adecuado para estimar concentraciones
de olor, a través de modelación de dispersión atmosférica, debido a que este percentil tiene una relación
directa con la molestia producida por olor [45] .

En la actualidad, en Chile sólo se han definido criterios de calidad o normas de emisión específicas para
la evaluación de impactos por olor en el sector porcino, aplicando la Norma de Emisión de
Contaminantes en Planteles Porcinos que, en función de sus olores, generan Molestia y Constituyen un
Riesgo a la Calidad de Vida de la Población (Ministerio del Medio Ambiente), único referente a nivel
nacional relativo al tema de olores. Esta norma no guarda relación con el proyecto en referencia.

En base a lo anteriormente descrito, se consultaron las **normativas vigentes** de olor de los Estados de
referencia descritos en el art. 11 del Reglamento del SEIA, considerando que para su aplicabilidad se
priorizará aquel Estado que posea similitud en sus componentes ambientales, con la situación nacional
y/o local. De la revisión del listado se tiene que sólo los Estados de **Alemania, Australia, Canadá,**
**Nueva Zelandia, Reino de los Países Bajos e Italia** cuentan con normativa, guía o lineamientos
regulatorios que podrían ser ajustarse a nuestro territorio. Posteriormente se analizó su aplicabilidad
según normativa, percentil, descripción de actividad regulada y planificación territorial, de acuerdo con
lo señalado en la Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA (SEA, 2017).

De acuerdo con el análisis anterior y sumado a los antecedentes de normativa internacional descrito por
el Ministerio del Medio Ambiente [46], se desprende lo siguiente:

 Normativa vigente: Se descarta Australia, España, Irlanda, Nueva Zelandia, Panamá y Reino Unido.

Debido a que sólo disponen de guías/estándares regulatorios y no de normativas. Del mismo modo,
se excluye la normativa de Colombia, dado que no forma parte del listado de Estados descritos en el
artículo 11 del Reglamento del SEIA.

 Unidades comparables para niveles límites: Se descarta Bélgica, Brasil, Corea del Sur y Estados

Unidos de América, dado que utilizan unidades de medición distintas a las descritas en la Guía de
Olores del SEA.

 Percentil: Se descarta normas de Alemania, Australia, Canadá, Dinamarca, Hong Kong, Israel y

Noruega, dado que no son compatibles con el criterio de percentil 98 descrito en la Guía de Olores
del SEA.

 Actividad aplicable: Se descarta las normas de Francia, Puglia (Italia) y Países Bajos, dado que no

abordan la actividad a evaluar en el presente proyecto.

42 Environment Agency. (2007). Review of Dispersion Modelling for Odour Predictions. Environment Agency.
43 Environment Agency. (2009). Horizontal Guidance: Technical Guidance Note - H4 Odour Management. Environment Agency.
44 Ibid.
45 Environment Agency. (2007). Review of Dispersion Modelling for Odour Predictions. Environment Agency.
46 [Regulaciones a nivel internacional: Antecedentes Normativa Internacional. Link: https://olores.mma.gob.cl/estudios-y-](https://olores.mma.gob.cl/estudios-y-publicaciones/#estudios-internacionales)

[publicaciones/#estudios-internacionales](https://olores.mma.gob.cl/estudios-y-publicaciones/#estudios-internacionales)

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 48 de 77

En coherencia al análisis descrito anteriormente, se define la normativa del Estado de Italia (provincia de
Trento [47] ) como aplicable al proyecto en función de lo establecido en el Reglamento del SEIA y la Guía de
Olores del SEA, basado en criterios de normativa vigente, unidad del nivel límite, percentil y actividad
regulada.

Los límites establecidos en esta norma están en función de la distancia de los receptores al perímetro
del predio o instalación y según el uso del territorio, definidos como zona residencial y no residencial.
Por lo tanto, los valores de aceptabilidad de la alteración olfativa en los receptores, expresados como
concentraciones máximas horarias de olor al percentil 98, calculados sobre la base anual, que deben ser
cumplidos en los receptores situados en zonas no residenciales según los Instrumentos de Planificación
Territorial vigentes se describen en la siguiente tabla:

Tabla 17 - Concentraciones máximas en receptores según normativa de Trento.

|Receptores|Percentil|Valores [ou /m3]<br>E|
|---|---|---|
|Receptores a una distancia >500 [m] desde el deslinde del predio|98|2|
|Receptores a una distancia entre 200 [m] y 500 [m] desde el deslinde del predio|Receptores a una distancia entre 200 [m] y 500 [m] desde el deslinde del predio|3|
|Receptores a una distancia <200 [m] desde el deslinde del predio|Receptores a una distancia <200 [m] desde el deslinde del predio|4|

Tabla 18 - Valores de aceptabilidad de concentración de olor en receptores según distancia

|ID|Descripción|Distancia al<br>perímetro de<br>la planta<br>[m]|Rango<br>distancia<br>[m]|Valor límite norma<br>Trento<br>CO<br>[ou /m3]<br>E|
|---|---|---|---|---|
|R1|Vivienda ubicada fuera del límite urbano de Maullín|636|>500|2|
|R2|Vivienda ubicada fuera del límite urbano de Maullín|472|200 - 500|3|
|R3|Vivienda ubicada fuera del límite urbano de Maullín|493|200 - 500|3|
|R4|Vivienda ubicada fuera del límite urbano de Maullín|580|>500|2|
|R5|Vivienda ubicada fuera del límite urbano de Maullín|858|>500|2|
|R6|Vivienda ubicada fuera del límite urbano de Maullín|649|>500|2|
|R7|Vivienda ubicada fuera del límite urbano de Maullín|502|>500|2|
|R8|Vivienda ubicada fuera del límite urbano de Maullín|439|200 - 500|3|
|R9|Vivienda ubicada fuera del límite urbano de Maullín|584|>500|2|
|R10|Vivienda ubicada fuera del límite urbano de Maullín|623|>500|2|
|R11|Vivienda ubicada fuera del límite urbano de Maullín|474|200 - 500|3|
|R12|Vivienda ubicada fuera del límite urbano de Maullín|79|<200|4|
|R13|Vivienda ubicada fuera del límite urbano de Maullín|63|<200|4|
|R14|Vivienda ubicada fuera del límite urbano de Maullín|255|200 - 500|3|
|R15|Vivienda ubicada fuera del límite urbano de Maullín|33|<200|4|
|R16|Vivienda ubicada fuera del límite urbano de Maullín|760|>500|2|
|R17|Vivienda ubicada fuera del límite urbano de Maullín|471|200 - 500|3|
|R18|Vivienda ubicada fuera del límite urbano de Maullín|675|>500|2|

Los resultados son evaluados en términos de área y alcance odorante bajo el criterio de calidad definido,
en función de los objetivos del estudio. Se presentan los resultados de los valores límites de exposición:

`o` Concentración límite = 2, 3 y 4 [ou E /m [3] ].
`o` Criterio de cumplimiento = P98.

`o` Tiempo de evaluación = 1 hora.

`o` Tasa de Emisión de Olor - E1: Situación futura = 46.638 [ou E /s].

47 Giunta Provinciale di Trento. (2016). Linee guida per la caratterizzazione, l’analisi e la definizione dei criteri tecnici e gestionali per la

mitigazione delle emissioni delle attività ad impatto odorigeno. Italia.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 49 de 77

**5.2** **Estimación de los impactos por emisiones de olor**

Para la estimación cuantitativa y cualitativa de los impactos por olor, producto de la operación del
proyecto se evaluó el siguiente escenario:

Tabla 19 - Descripción escenarios simulados

|Escenario|Modelo|Percentil|Criterio de<br>calidad|
|---|---|---|---|
|E1: Situación futura|M1: Curvas de isoconcentración de olor<br>M2: Frecuencia de percepción de olor (horaria)<br>M3: Frecuencia de percepción de olor (mensual)<br>M4: Concentración máxima horaria|98|2, 3 y 4<br>[ouE/m3]|

A partir de lo obtenido en el modelo anual (WRF-MMIF, 2021), se evaluaron los siguientes resultados:

 - Área de influencia

Corresponde al área en la cual se libera olor por un emisor observado [48] y que se define por la isolínea
de olor resultante de la proyección, bajo un criterio de calidad de 1 [ou E /m [3] ] considerado como
umbral de percepción (olor no reconocible). Se consideró el escenario de emisión de olor más
desfavorable correspondiente a la situación operacional futura, dado que es la que presenta mayor
Tasa de Emisión de Olor.

 Cuantificación según curvas de isoconcentraciones de olor (M1)

Corresponde al percentil 98 anual de los promedios horarios de las concentraciones de olor (175
horas al año), utilizando meteorología de pronóstico, bajo un criterio de calidad de 2, 3 y 4 [ou E /m [3] ]
según valores de aceptabilidad de la alteración olfativa para actividades generadoras de olores. Se
presentan como isolíneas de olor (alcance o nivel de exposición de olor) desde el criterio definido.

 - Cuantificación de la frecuencia de percepción de olor (M2 M3)

Corresponde a la frecuencia de ocurrencia de concentraciones horarias medias por encima del valor
de aceptabilidad definido según la distancia del receptor al deslinde del predio, describiéndose como
la sumatoria de horas anuales de excedencia, distribuidas en horas del día y del mes. Debido a
variaciones meteorológicas de carácter estacional, se recomienda el uso del criterio de percentil 98 el
cual permite visualizar los porcentajes de horas en que se supera el valor definido para las 8.760
horas del año [49] .

 Estimación de Concentración máxima horaria (M4)

Corresponde al límite superior de los promedios horarios de concentración de olor registrados en un
punto receptor, bajo percentil 98 para la totalidad del periodo anual y es expresada en [ou E /m [3] ].

El percentil 98 (P98) de los promedios horarios de concentración de olor en un periodo anual, excluye el
2% de las horas que agrupan los valores más altos (175 horas). Por lo tanto, para un punto receptor, el
valor de Concentración Máxima bajo P98, significa que el 98% de las horas de un año registran valores
de concentración que no exceden el límite superior de concentración de olor determinado.

48 Ministerio del Medio Ambiente. (2013). Estudio: Antecedentes para la Regulación de Olores en Chile. Subsecretaría del Medio Ambiente,

Chile.
49 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA. Chile.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 50 de 77

**5.3** **Predicción de Área de Influencia del Proyecto**

Figura 21 - AI: Área de influencia del Proyecto, C P98-1hr = 1 [ou E /m [3] ]

|Alcance|Orientación|Distancia<br>[m]|
|---|---|---|
|**Alcance**|N <br>NE<br>E <br>SE<br>S <br>SO<br>O <br>NO|290<br>297<br>35<br>220<br>310<br>363<br>0 <br>97|

Fuente: Envirometrika. “Situación futura: Área de Influencia, C P98-1hr = 1 [ou E /m [3] ].” [Cartografía]. 1:11.000. Noviembre 2023.
Software: ArcGIS [software GIS]. Version 10.2 Redlands, CA: Environmental Systems Research Institute, Inc., 2023.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 51 de 77

**5.4** **Cuantificación según curva de isoconcentración de olor**

Figura 22 - E1: Curvas isodoras, Sit. futura, receptores a una distancia >500 [m], C P98-1hr = 2 [ou E /m [3] ]

|Alcance|Orientación|Distancia<br>[m]|
|---|---|---|
|**Alcance**|N <br>NE<br>E <br>SE<br>S <br>SO<br>O <br>NO|0 <br>0 <br>0 <br>0 <br>0 <br>16<br>0 <br>0|

Fuente: Envirometrika. Isolíneas de olor, C P98-1hr = 2 [ou E /m [3] ].” [Cartografía]. 1:11.000. Noviembre 2023.
Software: ArcGIS [software GIS]. Versión 10.2 Redlands, CA: Environmental Systems Research Institute, Inc., 2023.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 52 de 77

Figura 23 - E1: Curvas isodoras, Sit. futura, receptores a una distancia entre 200 [m] y 500 [m], C P98-1hr = 3 [ou E /m [3] ]

|Alcance|Orientación|Distancia<br>[m]|
|---|---|---|
|**Alcance**|N <br>NE<br>E <br>SE<br>S <br>SO<br>O <br>NO|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|

Fuente: Envirometrika. Isolíneas de olor, C P98-1hr = 3 [ou E /m [3] ].” [Cartografía]. 1:11.000. Noviembre 2023.
Software: ArcGIS [software GIS]. Versión 10.2 Redlands, CA: Environmental Systems Research Institute, Inc., 2023.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 53 de 77

Figura 24 - E1: Curvas isodoras, Sit. futura, receptores a una distancia <200 [m], C P98-1hr = 4 [ou E /m [3] ]

|Alcance|Orientación|Distancia<br>[m]|
|---|---|---|
|**Alcance**|N <br>NE<br>E <br>SE<br>S <br>SO<br>O <br>NO|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|

Fuente: Envirometrika. Isolíneas de olor, C P98-1hr = 4 [ou E /m [3] ].” [Cartografía]. 1:11.000. Noviembre 2023.
Software: ArcGIS [software GIS]. Versión 10.2 Redlands, CA: Environmental Systems Research Institute, Inc., 2023.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 54 de 77

**5.5** **Cuantificación de la frecuencia de percepción de olor**

La frecuencia de ocurrencia de concentración de olor para 2, 3 y 4 [ou E /m [3] ], se presenta como tablas y gráficos que muestran la sumatoria de
horas anuales, distribuidas en horas del día y meses del año. Estos resultados indicarían la probabilidad de superar concentraciones de olor en
los niveles de aceptabilidad de concentración de olor en los puntos evaluados. La nomenclatura para este análisis corresponderá a:

✓ **Frecuencia horaria** = Cantidad de horas con olor del año, distribuidas en horas del día, en que existe la probabilidad de superar 2 [ou E /m [3] ]

(en receptores sobre 500 [m] de distancia del deslinde); 3[ou E /m [3] ] (en receptores entre 200 [m] y 500 [m] de distancia del deslinde); 4

[ou E /m [3] ] (en receptores con menos de 200 [m] de distancia del deslinde).

✓ **Frecuencia mensual** = Cantidad de horas con olor del año, distribuidas en meses del año, en que existe la probabilidad de 2 [ou E /m [3] ] (en

receptores sobre 500 [m] de distancia del deslinde); 3[ou E /m [3] ] (en receptores entre 200 [m] y 500 [m] de distancia del deslinde); 4 [ou E /m [3] ]
(en receptores con menos de 200 [m] de distancia del deslinde).

Tabla 20 - E1/M2: Frecuencia de percepción de olor horaria - C P98-1hr =2, 3 y 4 [ou E /m [3] ]

|Valor límite<br>CP98|2 [ou /m3]<br>E|3 [ou /m3]<br>E|4 [ou /m3]<br>E|
|---|---|---|---|
|Hora del día|**R1**<br>**R4**<br>**R5**<br>**R6**<br>**R7**<br>**R9**<br>**R10**<br>**R16**<br>**R18**|**R2**<br>**R3**<br>**R8**<br>**R11**<br>**R14**<br>**R17**|**R12**<br>**R13**<br>**R15**|
|0 <br>1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|
|Total|**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **|**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **|**0 **<br>**0 **<br>**0 **|

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 55 de 77

Tabla 21 - E1/M3: Frecuencia de percepción de olor mensual - C P98-1hr =2, 3 y 4 [ou E /m [3] ]

|Valor límite<br>CP98|2 [ou /m3]<br>E|3 [ou /m3]<br>E|4 [ou /m3]<br>E|
|---|---|---|---|
|Hora del día|**R1**<br>**R4**<br>**R5**<br>**R6**<br>**R7**<br>**R9**<br>**R10**<br>**R16**<br>**R18**|**R2**<br>**R3**<br>**R8**<br>**R11**<br>**R14**<br>**R17**|**R12**<br>**R13**<br>**R15**|
|Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|
|Total|**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **|**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **|**0 **<br>**0 **<br>**0 **|

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 56 de 77

**5.6** **Concentración máxima**

En la siguiente tabla se informa el valor máximo de concentración odorante que percibirían los
receptores analizados para la situacion futura:

Tabla 22 - Concentración máxima - Percentil 98 y 99,5 - Situación futura

|ID|Concentración máxima [ou /m3]<br>E|Col3|Limite aceptabilidad<br>Normativa de Trento<br>CO [ou /m3]<br>E|Cumplimiento|Superación valor<br>límite normado|
|---|---|---|---|---|---|
|ID|Percentil 99,5|Percentil 98|Percentil 98|Percentil 98|Percentil 98|
|R1|1|<1|2|Sí|No|
|R2|2|<1|3|Sí|No|
|R3|1|<1|3|Sí|No|
|R4|1|<1|2|Sí|No|
|R5|<1|<1|2|Sí|No|
|R6|1|<1|2|Sí|No|
|R7|1|<1|2|Sí|No|
|R8|1|<1|3|Sí|No|
|R9|1|<1|2|Sí|No|
|R10|1|<1|2|Sí|No|
|R11|1|<1|3|Sí|No|
|R12|2|1|4|Sí|No|
|R13|2|1|4|Sí|No|
|R14|1|<1|3|Sí|No|
|R15|3|1|4|Sí|No|
|R16|<1|<1|2|Sí|No|
|R17|1|<1|3|Sí|No|
|R18|<1|<1|2|Sí|No|

La modelación a percentil C p98 de la situación operacional futura, no acusaría concentraciones de olor
sobre los criterios de calidad de 2, 3 o 4 [ou E /m [3] ] aplicables según la distancia al límite predial del
proyecto en ninguno de los 18 receptores evaluados.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 57 de 77

**6** **CONCLUSIÓN**

De la caracterización de emisiones de la futura Plataforma de Economía Circular Volta Los Lagos, se estimó
una Tasa de Emisión de Olor de 46.638 [ou E /s], basado en las condiciones operacionales descritas por el
Titular.

La estimación del Área de Influencia del Proyecto arrojó alcance sobre el nivel umbral de C P98-1h =1 [ou E /m [3] ],
en 3 receptores de los 18 evaluados situados al norte del límite predial.

De la cuantificación de impacto, el modelo acusaría que los 18 receptores considerados en la evaluación se
encuentran en cumplimiento con el límite de aceptabilidad de la normativa de Trento, correspondiente a 2

[ou E /m [3] ] para receptores que se encuentren a más de 500 [m] del límite predial, 3 [ou E /m [3] ] para receptores
entre 200 y 500 [m] del límite predial y 4 [ou E /m [3] ] para aquellos receptores que se encuentren a menos de
200 [m] del límite predial.

En virtud de la proyección del alcance odorante de las emisiones del proyecto en evaluación, para la
componente olor, no se generaría o presentaría algún efecto, características o circunstancias contempladas
en el artículo 11 de la Ley N° 19.300, siendo aplicable su ingreso como Declaración de Impacto Ambiental.

CONCLUSIÓN www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 58 de 77

**7** **BIBLIOGRAFÍA**

 Barros, C., Bello, P., Valiño, S., Bao, M., Arias, J. (2007). Odours Prevention and Control in the Shell

Waste Valorisation. Universidad de Santiago de Compostela. España.

 Brashers, B., Emery, C. (2014). Draft User’s Manual: The Mesoscale Model Interface Program (MMIF),

Version 3.1. U.S. Environmental Protection Agency.

 Department for Environment, Food & Rural Affairs. (2009). Good Practice and Regulatory Guidance on

Composting and Odour Control for Local Authorities. Environmental Health Practitioners - Local
Environment Protection. United Kingdom.

 Department of Water and Environmental Regulation. (2019). Guideline: Odour Emissions. Government

of Western Australia. Australia.

 Ecomaule S.A., (2020). P6168 Estudio de Impacto Odorante: Mejoramiento y Transformación Ecomaule:

Plataforma de Reciclaje y Valorización. SEIA, Chile.

 Environment Agency. (2007). Review of Dispersion Modelling for Odour Predictions. Environment

Agency.

 - Environment Agency. (2009). Horizontal Guidance: Technical Guidance Note - H4 Odour Management.

Environment Agency.

 Environmental Protection Agency. (2020). Air Dispersion Modelling from Industrial Installations Guidance

Note (AG4). Office of Environmental Enforcement (OEE), Ireland.

 - Envirometrika. (2019). P6015 Estudio de Impacto Odorante: Planta Calagro. Inversiones Las Garzas S.A.

Chile

 European Commitee for Standarization. (2003). Air quality - Determination of odour concentration by

Dynamic olfactometry. Unión Europea.

 Geoportal MINVU. (2022). Plan Regulador Comunal de Maullín. Ministerio de Vivienda y Urbanismo.

Chile.

 Giunta Provinciale di Trento. (2016). Linee guida per la caratterizzazione, l’analisi e la definizione dei

criteri tecnici e gestionali per la mitigazione delle emissioni delle attività ad impatto odorigeno. Italia.

 Instituto Nacional de Normalización. (2010). NCh 3190:2010 Calidad del aire - Determinación de la

Concentración de Olor por Olfatometría Dinámica. Chile.

 Instituto Nacional de Normalización. (2015). NCh 3386:2015 Calidad del aire - Muestreo estático para

olfatometría. Chile.

 Instituto Nacional de Normalización. (2015). NCh 3375/15: Digestato - Requisitos de Calidad. Chile.

 - Inversiones Las Garzas S.A. (2013). Planta de Carbonato de Calcio CALAGRO. SEIA, Chile.

 - Inversiones Las Garzas S.A. (2020). Planta de Carbonato de Calcio CALAGRO. SNIFA, Chile.

BIBLIOGRAFÍA www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 59 de 77

 - Ministerio del Medio Ambiente. (2012). Decreto Supremo N°38/11 del Ministerio del Medio Ambiente
Norma de Emisión de Ruidos Generados por Fuentes que Indica. Publicado en el Diario Oficial el 12 de
junio de 2012.

 Ministerio del Medio Ambiente. (2013). Estudio: Antecedentes para la Regulación de Olores en Chile.

Subsecretaría del Medio Ambiente, Chile.

 Municipalidad de Maullín. (2022). Promulga Plan Regulador Comunal de Maullín. Gobierno Regional de

Los Lagos. Chile.

 Ministerio Secretaría General de la Presidencia. (2016). Ley 19.300 Aprueba Ley Sobre Bases Generales

del Medio Ambiente. Ministerio Secretaría General de la Presidencia. Chile.

 Olores.org & Asociación Medioambiental Internacional de Gestores del Olor (AMIGO). (Draft, 2023).

Handbook Odour Exposure Modelling - International Handbook on the Assessment of Odour Exposure
by using Dispersion Modelling.

 Organización Meteorológica Mundial (2010). Manual de Claves, Claves Internacional, Volumen I.1 Parte

A - Claves alfanuméricas - Escala Beaufort de Viento. OMM-N°306, Suiza: OMM.

 Scire, J., Strimaitis, D., Yamartino, R. (2000). A User's Guide for the Calpuff Dispersion Model. Earth

Tech, Inc.

 Servicio de Evaluación Ambiental. (2023). Guía para el Uso de Modelos de Calidad del Aire en el SEIA.

Servicio de Evaluación Ambiental, Chile.

 Servicio de Evaluación Ambiental. (2017). Guía para la Descripción de la Calidad del Aire en el Área de

Influencia de Proyectos que Ingresan al SEIA. Departamento de Estudios y Desarrollo - División de
Evaluación y Participación Ciudadana. Chile.

 - Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en
el SEIA. Ministerio del Medio Ambiente. Chile.

 Suffet, I., H., et al., (2009). Sensory Assessment and Characterization of Odor Nuisance Emissions

during the Composting of Wastewater Biosolids. Water Environment Research, Vol. 81, No. 7.

 Suffet, I. H., et al. (2004). The Value of an Odor-Quality-Wheel Classification Scheme for Wastewater

Treatment Plants. Water Science and Technology, Vol 50, N° 4.

BIBLIOGRAFÍA www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 60 de 77

**8** **ANEXO 1 - CARACTERIZACIÓN DE FUENTES ODORANTES**

Tabla 23 - Situación futura: Caracterización de fuentes de olor

|ID|Fuente|Coordenadas UTM [m]|Col4|Altura<br>desde<br>suelo [m]|Vel.<br>salida<br>[m/s]|Temp.<br>salida<br>[oK]|Diám.<br>ducto<br>[m]|Largo<br>[m]|Ancho<br>[m]|Radio<br>[m]|Área<br>[m2]|
|---|---|---|---|---|---|---|---|---|---|---|---|
|ID|Fuente|X: Este|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|
|1|Sist. de abatimiento de olores Compostaje - Biofiltro|644.351|5.393.842|4,00|-|-|-|12,00|2,44|-|29,28|
|2|Trincheras|644.295|5.393.676|2,40|-|-|-|24,00|288,00|-|6.912,00|
|3|Patio de maduración|644.313|5.393.638|4,00|-|-|-|150,00|20,00|-|3.000,00|
|4|Chimenea Scrubber (Calcinación)|644.533|5.393.734|12,00|2,98|366,25|1,00|-|-|-|0,79|
|5|Sist. de abatimiento de olores Carbonato - Biofiltro|644.552|5.393.741|4,00|-|-|-|12,00|2,44|-|29,28|
|6|Sist. de abatimiento de olores Biogás - Biofiltro|644.547|5.393.560|3,00|-|-|-|12,00|2,44|-|29,28|
|7|Deshidratador|644.491|5.393.673|2,00|-|-|-|4,45|0,84|-|3,74|
|8|Laguna de digestato|644.696|5.393.668|0,00|-|-|-|90,00|90,00|-|8.100,00|
|9|Estanque ecualizador 1|644.393|5.393.614|3,00|-|-|-|-|-|1,87|10,99|
|10|Estanque ecualizador 2|644.395|5.393.608|3,00|-|-|-|-|-|1,87|10,99|
|11|Estanque ecualizador 3|644.398|5.393.604|3,00|-|-|-|-|-|1,87|10,99|
|12|Reactor de tratamiento aerobio SBR 1-1|644.372|5.393.601|6,00|-|-|-|15,00|5,00|-|75,00|
|13|Reactor de tratamiento aerobio SBR 1-2|644.376|5.393.596|6,00|-|-|-|15,00|5,00|-|75,00|
|14|Reactor de tratamiento aerobio SBR 2-1|644.379|5.393.591|6,00|-|-|-|15,00|5,00|-|75,00|
|15|Reactor de tratamiento aerobio SBR 2-2|644.382|5.393.586|6,00|-|-|-|15,00|5,00|-|75,00|
|16|Camiones de transporte|645.423|5.393.115|2,00|-|-|-|4.345,80|8,62|-|37.460,80|

ANEXO 1 - CARACTERIZACIÓN DE FUENTES ODORANTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 61 de 77

Tabla 24 - Situación futura: Características operacionales de fuentes emisoras

|ID|Fuente|Tipo de<br>fuente|Área [m2]|EO por sup.<br>[ou/m2s]<br>E|TEO<br>[ou/s]<br>E|Ciclo de<br>operación|Horas de operación|Días de<br>operación|Meses de<br>operación|
|---|---|---|---|---|---|---|---|---|---|
|1|Sist. de abat. de olores Compostaje - Biofiltro|Difusa|29,28|12,05|352,80|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|2|Trincheras|Difusa|6.912,00|0,83|5.736,96|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|3|Patio de Maduración|Difusa|3.000,00|0,40|1.200,00|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|4|Chimenea Scrubber (Calcinación)|Puntual|0,79|31.100,91|24.426,60|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|5|Sist. de abat. de olores Carbonato- Biofiltro|Difusa|29,28|96,38|2.822,02|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|6|Sist. de abat. de olores Biogás - Biofiltro|Difusa|29,28|20,87|611,01|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|7|Deshidratador|Difusa|3,74|0,32|1,20|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|8|Laguna de digestato|Difusa|8.100,00|0,32|2.592,00|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|9|Estanque ecualizador 1|Difusa|10,99|3,80|41,75|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|10|Estanque ecualizador 2|Difusa|10,99|3,80|41,75|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|11|Estanque ecualizador 3|Difusa|10,99|3,80|41,75|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|12|Reactor de tratamiento aerobio SBR 1-1|Difusa|75,00|19,08|1.431,00|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|13|Reactor de tratamiento aerobio SBR 1-2|Difusa|75,00|19,08|1.431,00|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|14|Reactor de tratamiento aerobio SBR 2-1|Difusa|75,00|19,08|1.431,00|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|15|Reactor de tratamiento aerobio SBR 2-2|Difusa|75,00|19,08|1.431,00|Continuo|24 horas (00:00-23:59)|Lu - Do|Ene -Dic|
|16|Camiones de transporte|Fugitiva|37.461|0,05|1.790,40|Continuo|12 horas (08:00-19:59)|Lu - Do|Ene -Dic|

ANEXO 1 - CARACTERIZACIÓN DE FUENTES ODORANTES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 62 de 77

**9** **ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES**

La Emisión de Olor (EO) es definida como la cantidad de olor emitida por una superficie o área respecto a
una unidad de tiempo, representada por la unidad [ou E /m [2] s], la cual es calculada a partir del muestreo de
una fuente odorante. Para calcular la Tasa de Emisión de Olor (TEO) de la fuente muestreada se multiplica la
Emisión de Olor (EO) por el área de emisión de esta fuente, como se describe en la siguiente ecuación [50] :

TEO= EO ~~[~~ [ou] [E]

m [2] s ~~[]]~~ [ ∗Área[m] [2] []]

A continuación, se describe la base cálculo de las emisiones de olor proyectadas, basado en emisiones de
referencia, cuyo enfoque se centra en representar la condición más desfavorable en términos de emisiones
para cada operación.

**9.1** **Aprovechamiento energético de los residuos orgánicos a través de la digestión anaeróbica**

**Galpón de recepción** : Tasa de emisión de olor proyectada en base a la operación de las unidades de
estanque de recepción, higienización y estanque de mezcla, cuyas emisiones son canalizadas a un
sistema de abatimiento correspondiente a un biofiltro de lecho con una eficiencia de remoción de olor
teórica de 95%. Para representar la condición de emisión más desfavorable se consideró el nivel
máximo de operación y una eficiencia conservadora del 90% de remoción de olor.
Las emisiones de referencia asimiladas fueron obtenidas del proyecto aprobado en el SEIA
“Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y Valorización [51] ”, cuyos valores
provienen de lo muestreado y analizado bajo los estándares definidos por las normativas
NCh3386:2015 [52] y NCh3190:2010 [53] .

Tabla 25 - Base de cálculo: emisiones de entrada biofiltro de planta de biogás

|Fuente|N°<br>Unidades|Área<br>[m2]|Emisión de<br>Referencia<br>[ou/m2s]<br>E|Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E|
|---|---|---|---|---|
|Higienizado|2|19,63|3,80/a|149,23|
|Estanque de recepción|1|144,00|41,10/b|5.918,40|
|Estanque de mezcla|1|132,73|0,32/c|42,47|

/a Emisión de referencia de unidad de higienizado.
/b Emisión de referencia de unidad de piscina de acumulación.
/c Emisión de referencia de unidad de estanque de acumulación.

50 Department of Water and Environmental Regulation. (2019). Guideline: Odour Emissions. Government of Western Australia. Australia.
51 Ecomaule S.A., (2020). P6168 Estudio de Impacto Odorante: Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y

Valorización. Centro de Manejo de Residuos Ecomaule. Chile.
52 Instituto Nacional de Normalización. (2015). NCh 3386:2015 Calidad del aire - Muestreo estático para olfatometría. Chile.
53 Instituto Nacional de Normalización. (2010). NCh 3190:2010 Calidad del aire - Determinación de la concentración de olor por olfatometría

dinámica. Chile.

ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 63 de 77

Tabla 26 - Base de cálculo: emisión proyectada en biofiltro de planta de biogás

|Fuente|N°<br>Unidades|Área<br>[m2]|Eficiencia de<br>remoción de<br>olor [%]|Emisión de<br>Referencia<br>[ou/m2s]<br>E|Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E|
|---|---|---|---|---|---|
|Sistema de abatimiento de olores- biofiltro|1|29,28|90%/a|20,87|611,01|

/a Valor conservador de eficiencia de remoción de olor.

**9.2** **Elaboración de compost agrícolas a través del proceso de compostaje**

**Galpón de compostaje** : Tasa de Emisión de Olor proyectada en base a la superficie efectiva de
compostaje al interior del galpón. Basado en las características de diseño se consideró un 40% de
superficie efectiva de emisión de olor, dado que el resto de la superficie corresponde a zonas de
tránsito, zonas de manejo de material y zona de material estructurante. La emisión asociada a la
superficie efectiva de generación de olores es canalizada a un sistema de abatimiento de olores
correspondiente a un biofiltro de lecho de 95% de eficiencia de remoción de olor. Para representar la
condición de emisión más desfavorable se consideró el nivel máximo de operación y una eficiencia
conservadora del 90% de remoción de olor.

Las emisiones de referencia asimiladas fueron obtenidas del proyecto aprobado en el SEIA
“Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y Valorización [54] ”, cuyos valores
provienen de lo muestreado y analizado bajo los estándares definidos por las normativas
NCh3386:2015 [55] y NCh3190:2010 [56] . Las emisiones referencia utilizadas correspondieron a pilas
agroindustriales en su estado inicial (edad 1), cuyos valores son los de mayor emisión entre los residuos
orgánicos a compostar, basado en lo muestreado en el estudio de referencia.

Tabla 27 - Base de cálculo: emisiones de entrada biofiltro de galpón de compostaje

|Fuente|N°<br>Unidades|Área total del<br>galpón<br>[m2]|Área efectiva<br>de emisión<br>de olor/a<br>[m2]|Emisión de<br>Referencia/b<br>[ou/m2s]<br>E|Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E|
|---|---|---|---|---|---|
|Galpón de compostaje|1|600,00|240,00|14,70|3.528,00|

/a Superficie al interior del galpón asociada al manejo de pilas de compostaje.
/b Emisión de referencia de pilas agroindustrial en etapa inicial (edad 1, materia prima fresca).

Tabla 28 - Base de cálculo: emisión proyectada en biofiltro de galpón de compostaje

|Fuente|N°<br>Unidades|Área<br>[m2]|Eficiencia de<br>remoción de<br>olor [%]|Emisión de<br>Olor<br>[ou/m2s]]<br>E|Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E|
|---|---|---|---|---|---|
|Sistema de abatimiento de olores- biofiltro|1|29,28|90%/a|12,05|352,80|

/a Valor conservador de eficiencia de remoción de olor.

54 Ecomaule S.A., (2020). P6168 Estudio de Impacto Odorante: Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y

Valorización. Centro de Manejo de Residuos Ecomaule. Chile.
55 Instituto Nacional de Normalización. (2015). NCh 3386:2015 Calidad del aire - Muestreo estático para olfatometría. Chile.
56 Instituto Nacional de Normalización. (2010). NCh 3190:2010 Calidad del aire - Determinación de la concentración de olor por olfatometría

dinámica. Chile.

ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 64 de 77

**Trincheras** : Tasa de Emisión de Olor proyectada en base la mezcla de material proveniente del galpón
de compostaje para su estabilización mediante la inyección de aire en trincheras, que permitirán
confinar el compostaje en las primeras semanas de tratamiento y operar de manera continua. Una vez
conformada la trinchera se cubrirá con una lámina hasta el término del proceso, cuyas propiedades
permiten proteger las pilas de las lluvias, mantener el oxígeno dentro de ellas y retener los gases
odorantes que se puedan generar en el proceso con una eficiencia del 98%. Para representar la
condición de emisión más desfavorable se consideró una eficiencia conservadora del 90% de retención

de olor.

Del mismo modo, para representar el nivel de máximo de operación se consideró un total de 32
trincheras, las cuales fueron caracterizadas con cobertura y en condición de carga/descarga parcial. La
operación de carga contempla la preparación de trinchera para la recepción de material durante un
periodo de 30 [min], tiempo en la cual permanecería descubierta hasta recibir la carga. Luego el
material es descargado y acondicionado al interior de la trinchera para posterior ser cubierto
nuevamente a medida que ingresa el material, esta actividad tendría una duración aproximada de 30

[min]. El manejo de estas unidades, consideraría en el peak de la operación una carga de máxima de 1
trinchera por día. Esta misma condición se presentaría para actividad de descarga de material, una vez
finalizada esta etapa, para su traslado al patio de maduración. Por lo tanto, a modo general se tendría
en la condición más desfavorable, 2 de las 32 trincheras en operación de carga y descarga, durante un
rango horario de 08:00 a 20:00 horas (jornada laboral), lo que equivaldría al 6,25% del total de la
unidades asociadas a esta etapa del proceso.

Las emisiones de referencia asimiladas fueron obtenidas del proyecto aprobado en el SEIA
“Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y Valorización [57] ”, cuyos valores
provienen de lo muestreado y analizado bajo los estándares definidos por las normativas
NCh3386:2015 [58] y NCh3190:2010 [59] . Siendo utilizadas para la proyección de trincheras cubiertas y en la
carga de material, valores de emisión correspondieron a pilas agroindustriales en edad 2, cuyos valores
corresponden a la segunda etapa de estabilización. Para la operación de descarga de trincheras se
aplicaron valores correspondieron a las pilas agroindustriales en edad 3.

Dado que las actividades de carga y descarga presentan una duración acotada (subhoraria) se aplicaron
valores ponderados para representar la operación en un régimen horario de emisión en el modelo de
dispersión.

Tabla 29 - Base de cálculo: emisiones compostaje en trincheras

|Fuente|N°<br>Unidades|Área unitaria<br>trinchera [m2]|Área total de<br>trincheras/a|Emisión de<br>Olor/a<br>[ou/m2s]<br>E|Tasa de<br>Emisión de Olor<br>[ou/s]<br>E|
|---|---|---|---|---|---|
|Trincheras en operación|32|216|6.912|0,88|6.093,43|

**TEO Total de trincheras en operación [ou** **E** **/s]** **6.093,43**
/a Emisión ponderada de trincheras en condición de carga y descarga.

57 Ecomaule S.A., (2020). P6168 Estudio de Impacto Odorante: Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y

Valorización. Centro de Manejo de Residuos Ecomaule. Chile.
58 Instituto Nacional de Normalización. (2015). NCh 3386:2015 Calidad del aire - Muestreo estático para olfatometría. Chile.
59 Instituto Nacional de Normalización. (2010). NCh 3190:2010 Calidad del aire - Determinación de la concentración de olor por olfatometría

dinámica. Chile.

ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 65 de 77

Tabla 30 - Base de cálculo: emisiones proyectadas de trincheras según condición

|Fuente|Unidades|%Un|Emisión de Olor<br>[ou/m2s]<br>E|Tasa de<br>Emisión de Olor<br>[ou/s]<br>E|
|---|---|---|---|---|
|Trincheras cubiertas/a|30|93,75%|0,83|5.378,40|
|Trincheras carga/descarga/b|2|6,25%|1,66|715,03|

/a Emisiones de referencia de Pila Agroindustrial Edad 2 con eficiencia de remoción de olor de un 90% de la lámina cobertora.
/b Emisión de referencia resultante de la ponderación de las condiciones con carga y con descarga.

Tabla 31 - Base de cálculo: emisiones proyectadas de trincheras en condición de carga/descarga

|Condición|Unidades|% total de<br>unidades según<br>condición|EO Prom<br>[ou/m2s]<br>E|
|---|---|---|---|
|Con carga/a|1|3,13%|2,78|
|Con descarga/b|1|3,13%|0,54|
|Cubierta|32|93,75%|0,83|

/a Considera emisiones de trinchera cubierta de Pila Agroindustrial Edad 2 con eficiencia de remoción de olor de un 90% de la
lámina cobertora. Carga parcial considera emisiones de referencia de Pila Agroindustrial Edad 2 sin cobertura.
/b Considera emisiones de trinchera cubierta de Pila Agroindustrial Edad 3 con eficiencia de remoción de olor de un 90% de la
lámina cobertora. Descarga parcial considera emisiones de material estabilizado de Pila Agroindustrial Edad 3 sin cobertura.

**Patio de maduración:** Tasa de Emisión de Olor proyectada a partir del material resultante del proceso
de compostaje en trinchera, el cual es depositado en un patio de maduración/almacenaje por un periodo
máximo de 20 días hasta finalizar el proceso de estabilización. Una vez depositado el material en el
patio, este es cubierto con una lámina impermeable, cuya capacidad de retención de gases odorantes es
del 95%. Para representar la condición de emisión más desfavorable se consideró nivel operacional
máximo (100% de ocupación) y una eficiencia conservadora del 75% de retención de olor.

Las emisiones de referencia asimiladas fueron obtenidas del proyecto aprobado en el SEIA
“Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y Valorización [60] ”, cuyos valores
provienen de lo muestreado y analizado bajo los estándares definidos por las normativas
NCh3386:2015 [61] y NCh3190:2010 [62] . Dadas las características del material que ingresa al patio de
maduración, en esta etapa del proceso de compostaje, se aplicaron emisiones correspondientes a pilas
agroindustriales en edad 3.

La operación de carga del patio de maduración considera el traslado del material de 1 trinchera al día
como máximo, el cual se realizaría dentro de una jornada laboral de 8 horas (08:00-17:00[h]). Esta
operación contempla la descarga de material parcial, armado de pila y posterior cobertura. Dado que el
proceso requiere de volteos periódicos del material con una frecuencia de 1 vez por semana durante los
20 días que permanece en el patio de maduración, se consideró que, del total de material dispuesto en
el patio de maduración, el 5% permanecería descubierta por condición de carga, volteo y descarga de
material.

60 Ecomaule S.A., (2020). P6168 Estudio de Impacto Odorante: Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y

Valorización. Centro de Manejo de Residuos Ecomaule. Chile.
61 Instituto Nacional de Normalización. (2015). NCh 3386:2015 Calidad del aire - Muestreo estático para olfatometría. Chile.
62 Instituto Nacional de Normalización. (2010). NCh 3190:2010 Calidad del aire - Determinación de la concentración de olor por olfatometría

dinámica. Chile.

ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 66 de 77

Con relación a la operación de volteo, su ejecución consideró actividades de retiro de cobertura, volteo
mecánico y cobertura (post-volteo), cada una de ellas con una duración aproximada de 20 [min]. Por lo
tanto, para representar esta operación en el modelo de forma horaria, se estimó un valor ponderado de
emisión a partir de la contribución subhoraria de cada una de las actividades ejecutadas. Para
representar el comportamiento del olor durante el volteo, se aplicó un incremento de 4 veces la emisión
correspondiente a pilas agroindustriales en edad 3. Del mismo modo, una vez ejecutado el volteo, la
emisión de olor presentaría una curva de disminución gradual, a medida que transcurren las horas post
volteo, cuyo comportamiento es descrito por la función Y= 27,389*X [-0.478] [63], reestableciéndose la
condición de reposo luego de 6 horas de realizado el volteo, lo cual fue representado en el modelo de
dispersión de olor.

Tabla 32 - Base de cálculo: emisiones de patio de maduración

|Fuente|Área de emisión/a<br>[m2]|Emisión de Olor/b<br>[ou/m2s]<br>E|Tasa de Emisión de<br>Olor<br>[ou/s]<br>E|
|---|---|---|---|
|Patio de maduración total|3.000|0,70|2.099,61|

**TEO Total de patio de maduración [ou** **E** **/s]** **2.099,61**
/a Considera ocupación del 100% de capacidad y operación continua durante todo el periodo anual.
/b Emisión de referencia de la ponderación de emisión según condición.

Tabla 33 - Base de cálculo: emisiones proyectadas de patio de maduración según condición

|TEO|Área unitaria<br>[m2]|% total de<br>superficie según<br>condición|EO<br>[ou/m2s]<br>E|TEO Pond<br>[ou/s]<br>E|
|---|---|---|---|---|
|Patio de maduración cubierto (con volteo)/a|2.850|95,00%|0,71|2.014,65|
|Patio de maduración carga/descarga/b <br>|150<br>|5,00%<br>|0,57<br>|84,96<br>|

/a Emisión ponderada del ciclo de maduración, Pila Agroindustrial Edad 3, con cobertura con eficiencia de olor de un 75%,
integrando volteos 1 vez por semana en horario de 08:00 y 17:00 horas.
/b Emisión de referencia resultante de la ponderación de las condiciones con carga y con descarga.

Tabla 34 - Base de cálculo: emisiones proyectadas de patio de maduración en condición de carga/descarga

|Condición|Área unitaria<br>[m2]|% total de<br>superficie según<br>condición|EO<br>[ou/m2s]<br>E|
|---|---|---|---|
|Con carga/a|75|2,50%|0,63|
|Con descarga/b|75|2,50%|0,51|

/a Considera emisiones de trinchera cubierta de Pila Agroindustrial Edad 2 con eficiencia de remoción de olor de un 90% de la

lámina cobertora. y zona activa de carga con un ciclo de emisión de 08:00 a 17:00 horas con emisiones de referencia de Pila
Agroindustrial Edad 2.
/b Considera emisiones de trinchera cubierta de Pila Agroindustrial Edad 3 con eficiencia de remoción de olor de un 75% de la

lámina cobertora. y zona activa de descarga con un ciclo de emisión de 08:00 a 17:00 horas con emisiones de referencia de Pila
Agroindustrial Edad 3.

**9.3** **Elaboración de carbonato de calcio a partir de conchas de moluscos**

**Planta de carbonato de calcio** : Tasa de Emisión de Olor proyectada en base al confinamiento de las
unidades de procesamiento de conchas de moluscos, al interior de la planta de carbonato de calcio. Las
emisiones odorantes generadas en los distintos procesos (desde la descarga de materia prima hasta el

63 Department for Environment, Food & Rural Affairs. (2009). Good Practice and Regulatory Guidance on Composting and Odour Control for

Local Authorities. Environmental Health Practitioners - Local Environment Protection. United Kingdom.

ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 67 de 77

envasado) son canalizadas a un sistema de abatimiento de olores correspondiente a un biofiltro de lecho
con una eficiencia de remoción de olor del 95%. Para representar la condición de emisión más
desfavorable se consideró el nivel máximo de operación y una eficiencia conservadora del 90% de
remoción de olor.

Las emisiones de referencia asimiladas fueron obtenidas de un estudio olfatométrico realizado en una
planta de procesamiento de conchas en la costa norponiente de España, Calizas Marinas S.A. [64] ., cuyos
valores provienen de lo muestreado y analizado bajo los estándares definidos por la normativa técnica
europea EN 13725: 2003 [65], equivalente a la NCh3190:2010 [66] . Las emisiones referencia utilizadas fueron
interpoladas en base a la capacidad de procesamiento de la planta de referencia, cuyos procesos son
equivalente y asimilables al proyecto.

Tabla 35 - Base de cálculo: emisiones de entrada biofiltro de planta de carbonato de calcio

|Fuente|Volumen de<br>procesamiento<br>[ton/año]|Caudal<br>[m3/s]|Concentración<br>de olor<br>[ou/m3]<br>E|Tasa de Emisión<br>de Olor<br>[ou/s]<br>E|
|---|---|---|---|---|
|Planta de referencia Calizas Marinas S.A.|200.000,00|3,89|96.755,00|376.269,44|
|Planta de carbonato proyectada|15.000,00|3,90|-|28.220,21|

/a Emisión de olor proyectada en base a un volumen de procesamiento de 15.000 [ton/año].
/b Representa la emisión en una condición de nivel operacional máximo con funcionamiento continuo. Considera operaciones
preliminares (recepción de conchillas y lavado), procesamiento (calcinación y enfriado) y operaciones auxiliares (molienda,
tamizado, envasado y almacenamiento).

Tabla 36 - Base de cálculo: emisión proyectada en biofiltro de planta de carbonato de calcio

|Fuente|N°<br>Unidades|Área<br>[m2]|Eficiencia de<br>remoción de<br>olor [%]|Emisión de<br>Referencia<br>[ou/m2s]<br>E|Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E|
|---|---|---|---|---|---|
|Sistema de abatimiento de olores- biofiltro|1|29,28|90%/a|96,38|2.822,02|

/a Valor conservador de eficiencia de remoción de olor.

**Chimenea scrubber (calcinación):** Tasa de Emisión de Olor proyectada a partir de las emisiones
odorantes generadas en la planta de referencia “Planta de Carbonato de Calcio Calagro” [67], las cuales
fueron interpoladas según volumen de procesamiento. La Tasa de Emisión de Olor de la planta de
referencia considera el procesamiento de conchillas de moluscos para la obtención de carbonato de
calcio, cuyas unidades de proceso son asimilables al proyecto. En la planta de referencia las emisiones
de gases odorantes generadas por las unidades de proceso son canalizadas a la chimenea extractor
vapores de secadores. Por lo tanto, su aplicación representaría una condición más desfavorable respecto
a la planta de carbonato de calcio proyectada, dado que esta considera sistema de abatimiento de
olores (biofiltro) y torre de purificación de gases odorantes.

Los valores de emisión provienen de la última campaña olfatométrica declarada en el marco del Sistema
Nacional de Información de Fiscalización Ambiental, correspondiente al año 2019, la cual fue ejecutada
bajo los estándares definidos por las normativas NCh3386:2015 [68] y NCh3190:2010 [69] .

64 Barros, C. et al (2007). Odours Prevention and Control in the Shell Waste Valorisation. Universidad de Santiago de Compostela. España.
65 European Commitee for Standarization. (2003). Air quality - Determination of odour concentration by Dynamic olfactometry. Unión

Europea.
66 Instituto Nacional de Normalización. (2010). NCh 3190:2010 Calidad del aire - Determinación de la concentración de olor por olfatometría

dinámica. Chile.
67 Envirometrika. (2019). P6015 Estudio de Impacto Odorante: Planta Calagro. Inversiones Las Garzas S.A. Chile
68 Instituto Nacional de Normalización. (2015). NCh 3386:2015 Calidad del aire - Muestreo estático para olfatometría. Chile.

ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 68 de 77

Tabla 37 - Base de cálculo: emisiones de salida chimenea scrubber de planta de carbonato de calcio

|Fuente|Volumen de<br>procesamiento<br>[ton/año]|Caudal<br>[m3/s]|Concentración<br>de olor<br>[ou/m3]<br>E|Tasa de Emisión<br>de Olor<br>[ou/s]<br>E|
|---|---|---|---|---|
|Chimenea de Planta de carbonato de calcio<br>CALAGRO|25.000,00|3,89|10.468,54|40.711,00|
|Chimenea scrubber de Planta de carbonato<br>proyectada|15.000,00|2,34|-|24.426,60|

/a Emisión de olor proyectada en base a un volumen de procesamiento de 15.000 [ton/año].
/b Representa la emisión en una condición de nivel operacional máximo con funcionamiento continuo.

**Camiones de transporte:** Tasa de Emisión de Olor proyectada a partir de las emisiones odorantes
generadas por el tránsito vehicular por los caminos interiores del límite predial de camiones que
transportan distintos tipos de materia. Las emisiones de cada camión corresponderán a la materia prima
que este transporte. En adición, se considera una retención de olores por la cobertura de la lona de los
camiones correspondiente a un 50%. En el tránsito de salida, sin material, se considera una emisión
residual de olor de un 10% de la emisión de referencia.

El horario de tránsito de los camiones dentro del límite predial es considerado entre 08:00 a 20:00 horas
con una velocidad media de 10 [km/h] dentro del predio y una distancia total a recorrer de 4.346 [m] se
estima un tiempo del recorrido de 25 minutos aproximadamente. En base a un máximo de camiones
diarios para cada tipo de material a transportar, su emisión de referencia de entrada o salida, y el
tiempo de recorrido se establece un ciclo operacional para cada camión, obteniendo así la tasa de
emisión odorante ponderada de los camiones.

Tabla 38 - Base de cálculo: emisiones de camiones en tránsito por camiones de transporte

|ID|Tránsito vehicular de<br>camiones con cobertura<br>según tipo|Máximo<br>camiones<br>diarios<br>[camiones x<br>día]|Área de<br>emisión<br>[m2]|EO<br>[ou/m2s]<br>E|Retención<br>de olores<br>por<br>cobertura|EO con<br>cobertura<br>[ou/m2s]<br>E|TEO<br>Camión<br>[ou/s]<br>E|TEO Total<br>[ou/s]<br>E|
|---|---|---|---|---|---|---|---|---|
|1|Recepción MMPP<br>(Residuos Orgánicos)|8|24|14,70|50%|7,35|176,40|1.411,20|
|2|Despacho compost|5|5|1,60|1,60|0,80|19,20|96,00|
|3|Despacho digestato sólido|4|4|0,32|0,32|0,16|3,84|15,36|
|4|Conchas Moluscos planta<br>carbonato|3|3|7,44|7,44|3,72|89,28|267,84|

**TEO Total de camiones de transporte [ou** **E** **/s]** **1.790,40**

Tabla 39 - Base de cálculo: emisiones de tránsito por camiones de transporte

|Nombre fuente|Altura desde<br>el suelo [m]<br>(desde dónde<br>emite)|Largo<br>[m]|Ancho<br>[m]|Área de<br>emisión<br>[m2]|EO<br>[ou/m2s]<br>E|TEO Ruta<br>[ou/s]<br>E|
|---|---|---|---|---|---|---|
|Tránsito por Ruta interna - Sección 1|3|2.988|9|25.760|0,05|1.231|
|Tránsito por Ruta interna - Sección 2|3|776|9|6.693|6.693|320|
|Tránsito por Ruta interna - Sección 3|3|581|9|5.008|5.008|239|

69 Instituto Nacional de Normalización. (2010). NCh 3190:2010 Calidad del aire - Determinación de la concentración de olor por olfatometría

dinámica. Chile.

ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 69 de 77

**10** **ANEXO 3 - PLAN DE TRABAJO Y METODOLOGÍA**

**10.1** **Plan de trabajo**

La metodología aplicada en el desarrollo del servicio de Modelación de Impacto Odorante para el proyecto futuro se detalla en la siguiente figura:

Figura 25 - Esquema de plan de trabajo y metodología aplicada

Fuente: Envirometrika, 2023.

ANEXO 3 - PLAN DE TRABAJO Y METODOLOGÍA www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 70 de 77

**10.1.1** **Rueda de olor**

En la siguiente figura se muestra la rueda de olor aplicable al Proyecto, asociada a actividades
de disposición y tratamiento de residuos, planta de compostaje y tratamiento de lodos
sanitarios, para la identificación de las notas de olor características de este tipo de operación.

Figura 26 - Rueda de olor compostaje

Fuente: Suffet, I., H., et al., (2009) [70] .

70 Suffet, I., H., et al., (2009). Sensory Assessment and Characterization of Odor Nuisance Emissions during the Composting of Wastewater

Biosolids. Water Environment Research, Vol. 81, No. 7.

ANEXO 3 - PLAN DE TRABAJO Y METODOLOGÍA www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 71 de 77

Figura 27 - Rueda de descriptores de plantas de tratamiento de aguas residuales

Fuente: Water Science and Technology, Vol 50, N° 4 (2010) [71] .

71 Suffet, I. H., et al. (2004). The Value of an Odor-Quality-Wheel Classification Scheme for Wastewater Treatment Plants. Water Science

and Technology, Vol 50, N° 4.

ANEXO 3 - PLAN DE TRABAJO Y METODOLOGÍA www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 72 de 77

**11** **ANEXO 4 - MODELO DE DISPERSIÓN**

**11.1** **Alcances del modelo**

La modelación contempló los siguientes criterios:

 Base meteorológica de pronóstico preprocesada mediante MMIF, para generar archivo de campos de

viento tridimensionales y otras variables meteorológicas de ingreso al software de modelación, en
cumplimiento a los criterios señalados en la Guía para el uso de modelos de calidad del aire en el
SEIA [72] .

 Meteorología de pronóstico WRF año 2021 (enero 01 00:00 a diciembre 31 23:00) con un dominio de

50 x 50 [km], cuya configuración y modelación se basó en lo dispuesto por el Servicio de Evaluación
Ambiental.

 Los datos de pronóstico consideraron 11 niveles verticales, siendo el nivel más bajo de

aproximadamente 0 [m] a nivel del suelo, centrado en las coordenadas: Latitud 41,504° S, Longitud
73,169° O.

 - Resolución de 1 [km] (espaciado de la cuadrícula), aplicando una grilla anidada con un espaciado en

receptor desde 10 [m], con el fin de obtener isolíneas más definidas en los puntos de evaluación.

 Período de emisión anual, basado en recomendaciones descritas en la “Guía para el uso de modelos

de calidad del aire en el SEIA” [73] .

Tabla 40 - Descripción de grilla anidada

|Coordenada centro<br>UTM 18 G|UTM N[m]|UTM E [m]|
|---|---|---|
|Coordenada centro<br>UTM 18 G|644.354|5.393.838|
|Grilla|Distancia desde el<br>centro [m]|Espaciado entre<br>receptores [m]|
|1|100|10|
|2|500|50|
|3|1.000|100|
|4|2.000|200|
|5|4.000|500|

**11.2** **Descripción del modelo**

La proyección de dispersión odorante considera la aplicación del software de modelación atmosférica
“CALPUFF VIEW” versión 8.6.0, modelo alternativo indicado por EPA [74] (USA). El software contempla 3
módulos de análisis numérico: CALMET, CALPUFF (v7.2.1) y CALPOST.

CALMET es un modelo que simula campos de viento, temperaturas y otras variables meteorológicas, en
un dominio de modelación tridimensional. Sin embargo, en la Guía para el uso de modelos de calidad del
aire en el SEIA se menciona que “En el caso de CALPUFF, se recomienda usar la información del modelo
de pronóstico directamente, sin usar el preprocesador CALMET” [75] .

72 Servicio de Evaluación Ambiental. (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Chile. Servicio de Evaluación

Ambiental, Chile.
73 Ibid.
74 Environmental Protection Agency, U.S.
75 Servicio de Evaluación Ambiental. (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Chile. Servicio de Evaluación

Ambiental, Chile.

ANEXO 4 - MODELO DE DISPERSIÓN www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 73 de 77

De acuerdo con lo anterior, se utilizó como preprocesador meteorológico el modelo MMIF [76] recomendado
por EPA (USA), siendo una alternativa a CALMET en la generación de los campos tridimensionales para
la evaluación en el análisis de impacto en la calidad del aire [77] .

CALPUFF es un modelo tipo “puff” Lagrangiano Gaussiano no estacionario, capaz de modelar el
transporte y dispersión de contaminantes sobre un campo de viento tridimensional. Este tipo de modelo
permite la representación de una pluma de emisión continua como un número discreto de paquetes de
material correspondiente a la especie de interés.

El modelo evalúa la contribución de un “puff” en la concentración atmosférica de un receptor en un
instante determinado. Luego, la concentración total en un receptor resultará de la sumatoria de las
contribuciones de todos los “puff” [78] . Finalmente, el modelo CALPOST procesa las salidas de CALPUFF
creando así, los archivos con las tabulaciones necesarias para la evaluación de los resultados según los
percentiles definidos en el modelo.

**11.3** **Dominio de modelación**

El dominio o área de modelación se determinó en función de la magnitud del proyecto y sus emisiones,
así como la presencia de receptores [79] . El área de modelación meteorológica cubrió un dominio de
aproximadamente 50 x 50 [km], abarcando una superficie de 2.500 [km [2] ].

Figura 28 - Dominio de modelación

Fuente: Envirometrika - Google Earth, 2023.

76 Mesoscale Model Interface Program, MMIF.
77 Brashers, B., Emery, C. (2014). Draft User’s Manual: The Mesoscale Model Interface Program (MMIF), Version 3.1. U.S. Environmental

Protection Agency.
78 Scire, J., Strimaitis, D., Yamartino, R. (2000). A User's Guide for the Calpuff Dispersion Model. Earth Tech, Inc.
79 Servicio de Evaluación Ambiental. (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Chile. Servicio de Evaluación

Ambiental, Chile.

ANEXO 4 - MODELO DE DISPERSIÓN www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 74 de 77

**11.4** **Elevaciones de terreno**

Los componentes geofísicos del dominio de modelación fueron adquiridos desde la base de “U.S.
Geological Survey (USGS) - Global Multi-resolution Terrain Elevation Data 2010 (GMTED2010)” con
curvas de nivel de resolución 30 [arc-second], equivalente a 1 [km] aproximadamente.

Figura 29 - Elevación de terreno del dominio

Fuente: Envirometrika. “Elevaciones de terreno - Dominio de modelación” [Ortofoto]. Noviembre 2023. Software: Calpuff View.
Versión 8.6.0 Toronto, ON: Lakes Environmental Software, 1995-2023.

ANEXO 4 - MODELO DE DISPERSIÓN www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 75 de 77

**11.5** **Uso de suelo**

El uso de suelo fue provisto desde la base de datos “Moderate Resolution Imaging Spectroradiometer
(MODIS)” para Sudamérica con una resolución 15 [arc-second], cercano a 500 [m] aproximadamente.

Figura 30 - Uso de suelo del dominio

Fuente: Envirometrika. “Uso de suelo - Dominio de modelación” [Ortofoto]. Noviembre 2023. Software: Calpuff View. Versión
8.6.0 Toronto, ON: Lakes Environmental Software, 1995-2023.

ANEXO 4 - MODELO DE DISPERSIÓN www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 76 de 77

**12** **ANEXO 5 - ANÁLISIS METEOROLÓGICO**

**12.1** **Comportamiento meteorológico anual**

La evaluación del comportamiento de los parámetros meteorológicos de velocidad y dirección del viento;
y su interacción a nivel local, se obtuvo a partir de la serie de datos de la grilla meteorológica de
pronóstico WRF-MMIF’21, en base a coordenadas representativas de Plataforma de Economía Circular
Volta Los Lagos, donde se encuentran localizadas las fuentes de emisión consideradas en el estudio. Los
datos horarios comprenden el periodo anual entre 00:00 01ene’21 y 23:00 de 31dic’21.

Tabla 41 - Coordenada central Plataforma Economía Circular Volta Los Lagos

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|X: Este|Y: Sur|Huso|Datum|
|644.590|5.393.748|18 G|WGS 84|

Figura 31 - Distribución de rosa de viento anual

Fuente: Envirometrika - Google Earth, 2023.

ANEXO 5 - ANÁLISIS METEOROLÓGICO www.tsgenvironmental.com

P7056 - Modelación de Impacto Odorante Noviembre 2023
Volta Servicios SpA - Plataforma de Economía Circular Volta Los Lagos Página 77 de 77

**12.2** **Caracterización meteorológica anual horaria**

Los campos de viento están determinados por la velocidad del viento y las componentes vectoriales de
dirección, producto del comportamiento dinámico de las masas de aire. La interacción de estas
componentes caracteriza el comportamiento del viento y el cómo intervienen en la dispersión de
contaminantes en el área de interés.

Tabla 42 - Rosas y campos de viento pronóstico anual

|Col1|Rosa de vientos|Col3|Distribución de velocidad del viento|Características|
|---|---|---|---|---|
|Anual Nocturno<br>(00:00 a 6:59 horas)|||<br>6.95<br>13.12<br>31.10<br>22.50<br>14.42<br>6.88<br>3.08<br>1.34<br>0.38<br>0.24<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Los<br>campos<br>de<br>vientos<br>predominaron<br>principalmente desde las componentes NNE<br>(17%) y N (16%) a lo largo del horario<br>nocturno.<br>La<br>distribución<br>del<br>viento<br>tuvo<br>un<br>comportamiento<br>asimétrico<br>positivo.<br>La<br>velocidad se caracterizó como brisa muy débil80. <br> <br>Velocidad promedio de viento: 2,22 [m/s].<br> <br>Frecuencia de vientos calmos: 6,95%.|
|Anual AM<br>(7:00 a 14:59 horas)|||<br>3.32<br>7.60<br>19.14<br>23.15<br>25.07<br>14.42<br>4.55<br>1.47<br>0.96<br>0.31<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|En el horario AM, las masas de aire provinieron<br>en mayor frecuencia desde dirección S con un<br>21%, y consecutivamente desde la componente<br>N (14%). En general, la intensidad del viento<br>varió de brisa muy débil a débil81.<br>Respecto a la distribución de los vientos, éstos<br>tuvieron una tendencia mesocúrtica.<br> <br>Velocidad promedio de viento: 2,87 [m/s].<br> <br>Frecuencia de vientos calmos: 3,32%.|
|Anual PM<br>(15:00 a 23:59 horas)|||<br>2.43<br>6.99<br>32.60<br>27.19<br>16.54<br>8.46<br>3.29<br>1.44<br>0.75<br>0.31<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Durante el horario PM, se observó predominio<br>de los vientos desde la dirección S con una<br>frecuencia del 17%. La velocidad de los vientos<br>se caracterizó como una brisa muy débil82.<br>La distribución de los vientos se observó con<br>una curva asimétrica positivo.<br> <br>Velocidad promedio de viento: 2,52 [m/s]<br> <br>Frecuencia de vientos calmos: 2,43%|

80 Organización Meteorológica Mundial (2010). Manual de claves, Claves internacional, Volumen I.1 Parte A - Claves alfanuméricas - Escala

Beaufort de Viento. OMM-N°306, Suiza: OMM.
81 Ibid.
82 Ibid.

ANEXO 5 - ANÁLISIS METEOROLÓGICO www.tsgenvironmental.com

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: - Fuentes de emisión**

| ID | Nombre fuente | EO<br>[ou/m2s]<br>E | TEO<br>[ou/s]<br>E |
| --- | --- | --- | --- |
| 1 | Sist. de abatimiento de olores<br>galpón de compostaje - Biofiltro | 12,5\a | 352,80 |
| 2 | Trincheras | 0,83\b | 5.736,96 |
| 3 | Patio de maduración | 0,40\c | 1.200,00 |
| 4 | Chimenea scrubber (calcinación) | 31.100,91\d | 24.426,60 |
| 5 | Sist. de abatimiento de olores<br>planta de carbonato - Biofiltro | 96,38\a | 2.822,02 |
| 6 | Sist. de abatimiento de olores<br>planta de biogás - Biofiltro | 20,87\a | 611,01 |
| 7 | Deshidratador | 0,32\d | 1,20 |
| 8 | Laguna de digestato | 0,32\d | 2.592,00 |
| 9 | Estanque ecualizador 1 | 3,80\d | 41,75 |
| 10 | Estanque ecualizador 2 | 3,80\d | 41,75 |
| 11 | Estanque ecualizador 3 | 3,80\d | 41,75 |
| 12 | Reactor de trat. aerobio SBR 1-1 | 19,08\d | 1.431,00 |
| 13 | Reactor de trat. aerobio SBR 1-2 | 19,08\d | 1.431,00 |
| 14 | Reactor de trat. aerobio SBR 2-1 | 19,08\d | 1.431,00 |
| 15 | Reactor de trat. aerobio SBR 2-2 | 19,08\d | 1.431,00 |
| 16 | Camiones de transporte | 0,05 | 1.790,40 |

**Tabla 2: - Límites de concentración de olor en receptores**

| ID | Nombre | Distancia\a<br>[m] | Límite de<br>concentración<br>de olor según<br>Normativa de<br>Trento<br>[ou/m3]<br>E |
| --- | --- | --- | --- |
| R1 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 636 | 2 |
| R2 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 472 | 3 |
| R3 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 493 | 3 |
| R4 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 580 | 2 |
| R5 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 858 | 2 |
| R6 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 649 | 2 |
| R7 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 502 | 2 |
| R8 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 439 | 3 |
| R9<br> | Vivienda ubicada fuera del<br>límite urbano de Maullín<br> | 584 | 2 |
| R10 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 623 | 2 |
| R11 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 474 | 3 |
| R12 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 79 | 4 |
| R13 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 63 | 4 |
| R14 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 255 | 3 |
| R15 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 33 | 4 |
| R16 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 760 | 2 |
| R17 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 471 | 3 |
| R18 | Vivienda ubicada fuera del<br>límite urbano de Maullín | 675 | 2 |

**Tabla 4: - Puntos receptores de interés**

| ID | Coordenadas UTM [m] (WGS84-<br>18G) | Col3 | Distancia\a<br>[m] | Orientación |
| --- | --- | --- | --- | --- |
| ID | X: Este | Y: Sur | Y: Sur | Y: Sur |
| R1 | 643.642 | 5.393.170 | 636 | OSO |
| R2 | 643.846 | 5.393.126 | 472 | SO |
| R3 | 643.905 | 5.392.985 | 493 | SO |
| R4 | 643.884 | 5.392.862 | 580 | SO |
| R5 | 644.596 | 5.392.490 | 858 | S |
| R6 | 645.279 | 5.393.031 | 649 | SE |
| R7 | 645.426 | 5.393.416 | 502 | ESE |
| R8 | 645.430 | 5.393.521 | 439 | ESE |
| R9 | 645.728 | 5.393.863 | 584 | E |
| R10 | 645.681 | 5.394.079 | 623 | ENE |
| R11 | 645.430 | 5.394.234 | 474 | ENE |
| R12 | 644.968 | 5.394.229 | 79 | NE |
| R13 | 644.950 | 5.394.281 | 63 | NE |
| R14 | 645.051 | 5.394.456 | 255 | NNE |
| R15 | 645.162 | 5.393.860 | 33 | E |
| R16 | 645.603 | 5.393.258 | 760 | ESE |
| R17 | 645.395 | 5.393.441 | 471 | ESE |
| R18 | 645.335 | 5.393.068 | 675 | SE |

**Tabla 5: - Concentración máxima en receptores**

| Concentración máxima en receptores<br>C = 3 [ou/m3]<br>P98-1hr E | Col2 | Col3 |
| --- | --- | --- |
| ID | E1: Situación futura | E1: Situación futura |
| ID | Percentil 99,5 | Percentil 98 |
| R1 | 1 | <1 |
| R2 | 2 | <1 |
| R3 | 2 | <1 |
| R4 | 1 | <1 |
| R5 | <1 | <1 |
| R6 | <1 | <1 |
| R7 | 1 | <1 |
| R8 | 1 | <1 |
| R9 | 1 | <1 |
| R10 | 1 | <1 |
| R11 | 1 | <1 |
| R12 | 2 | 1 |
| R13 | 2 | 1 |
| R14 | 1 | <1 |
| R15 | 3 | 1 |
| R16 | <1 | <1 |
| R17 | 1 | <1 |
| R18 | <1 | <1 |

**Tabla 6: - Evaluación de cumplimiento de límite de**

| ID | Concentración<br>máxima<br>[ou/m3]<br>E<br>Percentil 98 | Límite de<br>concentración<br>Normativa de<br>Trento8<br>[ou/m3]<br>E | Cumplimiento | Superación<br>valor límite<br>normado |
| --- | --- | --- | --- | --- |
| R1 | <1 | 2 | Sí | No |
| R2 | <1 | 3 | Sí | No |
| R3 | <1 | 3 | Sí | No |
| R4 | <1 | 2 | Sí | No |
| R5 | <1 | 2 | Sí | No |
| R6 | <1 | 2 | Sí | No |
| R7 | <1 | 2 | Sí | No |
| R8 | <1 | 3 | Sí | No |
| R9 | <1 | 2 | Sí | No |
| R10 | <1 | 2 | Sí | No |
| R11 | <1 | 3 | Sí | No |
| R12 | 1 | 4 | Sí | No |
| R13 | 1 | 4 | Sí | No |
| R14 | <1 | 3 | Sí | No |
| R15 | 1 | 4 | Sí | No |
| R16 | <1 | 2 | Sí | No |
| R17 | <1 | 3 | Sí | No |
| R18 | <1 | 2 | Sí | No |

**Tabla 7: - Coordenadas referenciales de localización del Proyecto**

| Coordenadas UTM [m] | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| X: Este | Y: Sur | Huso | Datum |
| 644.590 | 5.393.748 | 18 G | WGS 84 |

**Tabla 8: - Identificación de unidades con emisión de olor al ambiente**

| Área | Unidad | Emite<br>olores<br>molestos al<br>ambiente<br>(Si/No) | Contribución de olor al ambiente |
| --- | --- | --- | --- |
| Compostaje | Patio de acopio de material estructurante | No | Acopio de material sin olores ofensivos |
| Compostaje | Galpón de compostaje | No | Emisiones canalizadas a sist. de abatimiento (biofiltro) |
| Compostaje | Sistema de abatimiento de olores/a | Sí | Biofiltro con eficiencia de remoción de olor de 95% |
| Compostaje | Trincheras/b | Sí | Trincheras con cobertor de 98% de retención de olor |
| Compostaje | Patio de maduración/c | Sí | Acopio con cobertura de 75% de retención de olor |
| Planta de<br>Carbonato | Almacenamiento | No | Emisiones canalizadas a sist. de abatimiento (biofiltro) |
| Planta de<br>Carbonato | Lavado de conchillas | No | Emisiones canalizadas a sist. de abatimiento (biofiltro) |
| Planta de<br>Carbonato | Cinta elevadora | No | Emisiones canalizadas a sist. de abatimiento (biofiltro) |
| Planta de<br>Carbonato | Horno | No | Emisiones canalizadas a sist. de abatimiento (biofiltro) |
| Planta de<br>Carbonato | Enfriador | No | Emisiones canalizadas a sist. de abatimiento (biofiltro) |
| Planta de<br>Carbonato | Triturado | No | Emisiones canalizadas a sist. de abatimiento (biofiltro) |
| Planta de<br>Carbonato | Molino | No | Emisiones canalizadas a sist. de abatimiento (biofiltro) |
| Planta de<br>Carbonato | Micromolienda | No | Emisiones canalizadas a sist. de abatimiento (biofiltro) |
| Planta de<br>Carbonato | Tamizado | No | Emisiones canalizadas a sist. de abatimiento (biofiltro) |
| Planta de<br>Carbonato | Empacado | No | Emisiones canalizadas a sist. de abatimiento (biofiltro) |
| Planta de<br>Carbonato | Chimenea scrubber (Calcinación) | Sí | Gases odorantes residuales de la torre de purificación |
| Planta de<br>Carbonato | Sistema de abatimiento de olores/a | Sí | Biofiltro con eficiencia de remoción de olor de 95% |
| Planta de<br>biogás | Estanque de recepción | No | Emisiones canalizadas a sist. de abatimiento (biofiltro) |
| Planta de<br>biogás | Estanque de higienización | No | Emisiones canalizadas a sist. de abatimiento (biofiltro) |
| Planta de<br>biogás | Sistema de abatimiento de olores/a | Sí | Biofiltro con eficiencia de remoción de olor de 95% |
| Planta de<br>biogás | Digestor anaeróbico | No | Unidad cerrada sin emisión de olores al ambiente |
| Planta de<br>biogás | Gasómetro | No | Unidad cerrada sin emisión de olores al ambiente |
| Planta de<br>biogás | Almacenamiento de digestato crudo | No | Unidad cerrada sin emisión de olores al ambiente |
| Planta de<br>biogás | Deshidratador | Sí | Unidad con emisión de olores al ambiente |
| Planta de<br>biogás | Laguna de digestato | Sí | Unidad con emisión de olores al ambiente |
| Planta de<br>biogás | Antorcha | No | Proceso de combustión de comp. orgánicos volátiles |
| Planta de trat.<br>de RILes | Estanque ecualizador | Sí | Estanques cerrados con ventilación |
| Planta de trat.<br>de RILes | Reactor de tratamiento aerobio SBR | Sí | Unidad con emisión de olores al ambiente |
| Segreg. y valor.<br>de res. sólidos<br>recuperables | Contenedor de descarte (no valorizables) | No | Unidad con materia prima sin aporte de olores |
| Segreg. y valor.<br>de res. sólidos<br>recuperables | Galpón de almacenamiento | No | Unidad con materia prima sin aporte de olores |
| Segreg. y valor.<br>de res. sólidos<br>recuperables | Zona despacho | No | Unidad con materia prima sin aporte de olores |
| Transferencia y<br>valorización de<br>residuos<br>peligrosos y no<br>peligrosos | Sector de segregación | No | Unidad sin aporte de olores al ambiente |
| Transferencia y<br>valorización de<br>residuos<br>peligrosos y no<br>peligrosos | Sector de almac. de res. peligrosos sólidos | No | Unidad sin aporte de olores al ambiente |
| Transferencia y<br>valorización de<br>residuos<br>peligrosos y no<br>peligrosos | Sector de descarte de marca | No | Unidad sin aporte de olores al ambiente |
| Transferencia y<br>valorización de<br>residuos<br>peligrosos y no<br>peligrosos | Bodega RESPEL | No | Unidad sin aporte de olores al ambiente |
| Caminos<br>interiores | Camiones de transporte/d | Sí | Unidad con emisiones fugitivas de los camiones de<br>traslado de material con eficiencia de remoción de 50% |

**Tabla 9: - Fuentes odorantes - Situación futura**

| ID | Nombre fuente | Tipo de<br>fuente | Coordenadas UTM [m]<br>WGS84 18 G | Col5 |
| --- | --- | --- | --- | --- |
| ID | Nombre fuente | Tipo de<br>fuente | Este | Norte |
| 1 | Sistema de abatimiento de olores Compostaje - Biofiltro | Difusa | 644.351 | 5.393.842 |
| 2 | Trincheras | Difusa | 644.295 | 5.393.676 |
| 3 | Patio de maduración | Difusa | 644.313 | 5.393.638 |
| 4 | Chimenea Scrubber (Calcinación) | Puntual | 644.533 | 5.393.734 |
| 5 | Sistema de abatimiento de olores Carbonato- Biofiltro | Difusa | 644.552 | 5.393.741 |
| 6 | Sistema de abatimiento de olores Biogás - Biofiltro | Difusa | 644.547 | 5.393.560 |
| 7 | Deshidratador | Difusa | 644.491 | 5.393.673 |
| 8 | Laguna de digestato | Difusa | 644.696 | 5.393.668 |
| 9 | Estanque ecualizador 1 | Difusa | 644.393 | 5.393.614 |
| 10 | Estanque ecualizador 2 | Difusa | 644.395 | 5.393.608 |
| 11 | Estanque ecualizador 3 | Difusa | 644.398 | 5.393.604 |
| 12 | Reactor de tratamiento aerobio SBR 1-1 | Difusa | 644.372 | 5.393.601 |
| 13 | Reactor de tratamiento aerobio SBR 1-2 | Difusa | 644.376 | 5.393.596 |
| 14 | Reactor de tratamiento aerobio SBR 2-1 | Difusa | 644.379 | 5.393.591 |
| 15 | Reactor de tratamiento aerobio SBR 2-2 | Difusa | 644.382 | 5.393.586 |
| 16 | Camiones de transporte | Fugitiva | 645.423 | 5.393.115 |

**Tabla 10: - Proyectos de referencia asimilables al proyecto**

| Proyecto de referencia | Titular | Fuente de información | Link de expediente SEIA |
| --- | --- | --- | --- |
| Mejoramiento y Transformación<br>Ecomaule:<br>Plataforma<br>de<br>Reciclaje y Valorización | Ecomaule S.A17. | Servicio de Evaluación de<br>Impacto Ambiental | https://seia.sea.gob.cl/expediente/expedien<br>tesEvaluacion.php?modo=ficha&id_expedie<br>nte=2149076836 |
| Planta de Carbonato de Calcio<br>CALAGRO | Inversiones Las<br>Garzas S.A. 18,19 | Servicio de Evaluación de<br>Impacto Ambiental/ Sistema<br>Nacional de Información de<br>Fiscalización Ambiental | https://seia.sea.gob.cl/expediente/expedien<br>tesEvaluacion.php?modo=ficha&id_expedie<br>nte=7226669<br>https://snifa.sma.gob.cl/Fiscalizacion/Ficha/<br>1045139 |
| Odours Prevention and Control<br>in the Shell Waste Valorisation | Barros, C. et<br>al20 | Universidad de Santiago de<br>Compostela / Calizas Marinas S.A. | https://www.researchgate.net/publication/2<br>64876859_Odours_Prevention_and_Control<br>_in_the_Shell_Waste_Valorisation#pf4 |

**Tabla 11: - Emisiones de referencia aplicados en la situación futura**

| ID | Fuente | Tipo de<br>fuente | EO por sup.<br>[ou/m2s]<br>E | Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E | Estudio de<br>referencia |
| --- | --- | --- | --- | --- | --- |
| 1 | Sistema de abatimiento de olores Compostaje - Biofiltro | Difusa | 12,05 | 352,80 | A |
| 2 | Trincheras | Difusa | 0,83 | 5.736,96 | A |
| 3 | Patio de Maduración | Difusa | 0,40 | 1.200,00 | A |
| 4 | Chimenea Scrubber (Calcinación) | Puntual | 31.100,91 | 24.426,60 | B |
| 5 | Sistema de abatimiento de olores Carbonato- Biofiltro | Difusa | 96,38 | 2.822,02 | C |
| 6 | Sistema de abatimiento de olores Biogás - Biofiltro | Difusa | 20,87 | 611,01 | B |
| 7 | Deshidratador | Difusa | 0,32 | 1,20 | A |
| 8 | Laguna de digestato | Difusa | 0,32 | 2.592,00 | A |
| 9 | Estanque ecualizador 1 | Difusa | 3,80 | 41,75 | A |
| 10 | Estanque ecualizador 2 | Difusa | 3,80 | 41,75 | A |
| 11 | Estanque ecualizador 3 | Difusa | 3,80 | 41,75 | A |
| 12 | Reactor de tratamiento aerobio SBR 1-1 | Difusa | 19,08 | 1.431,00 | A |
| 13 | Reactor de tratamiento aerobio SBR 1-2 | Difusa | 19,08 | 1.431,00 | A |
| 14 | Reactor de tratamiento aerobio SBR 2-1 | Difusa | 19,08 | 1.431,00 | A |
| 15 | Reactor de tratamiento aerobio SBR 2-2 | Difusa | 19,08 | 1.431,00 | A |
| 16 | Camiones de transporte | Difusa | 0,05 | 1.790,40 | A, B, C |

**Tabla 12: - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 1**

| Requisito | Col2 | Sistema de<br>abatimiento de<br>olores<br>Compostaje -<br>Biofiltro | Trinch eras | Patio de<br>madur ación | Chimenea<br>scrub ber | Sistema de<br>abatimiento de<br>olores<br>Carbonato-<br>Biofiltro | Sistema de<br>abatimiento de<br>olores Biogás -<br>Biofiltro | Deshidratador | Laguna de<br>digestato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fase del proyecto que<br>genera olor | Fase del proyecto que<br>genera olor | Operación | Operación | Operación | Operación | Operación | Operación | Operación | Operación |
| Actividad que genera<br>emisiones de olor | Actividad que genera<br>emisiones de olor | Tratamiento<br>(sistema de<br>abatimiento) | Estabilización<br>de compost | Estabilización<br>de compost | Calcinación | Tratamiento<br>(sistema de<br>abatimiento) | Tratamiento<br>(sistema de<br>abatimiento) | Deshidratación<br>de digestato | Digestión<br>anaeróbica |
| Identificación del material<br>o sustancia olorosa | Identificación del material<br>o sustancia olorosa | Compost | Compost | Compost | Gases de<br>calcinación de<br>conchillas | Recepción y<br>almacenamiento<br>de conchillas | Recepción de<br>lodos | Digestato | Digestato |
| Tipo de fuente | Tipo de fuente | Difusa | Difusa | Difusa | Puntual | Difusa | Difusa | Difusa | Difusa |
| Régimen<br>de<br>emisión<br>de olor | Ciclo<br>operacional | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo |
| Régimen<br>de<br>emisión<br>de olor | Horario de<br>operación | 24 [h] | 24 [h] | 8:00 - 20:59<br>[h]/a | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] |
| Régimen<br>de<br>emisión<br>de olor | Frecuencia<br>mensual | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses |
| Emisión de olor<br>[ouE/m2*s] | Emisión de olor<br>[ouE/m2*s] | 12,05 | 0,83 | 0,40 | 31.100,91 | 96,38 | 20,87 | 0,32 | 0,32 |
| Tasa de emisión de olor<br>[ouE/s] | Tasa de emisión de olor<br>[ouE/s] | 352,80 | 5.736,96 | 1.200,00 | 24.426,60 | 2.822,02 | 611,01 | 1,20 | 2.592,00 |
| Tono Hedónico | Tono Hedónico | S/I/b | S/I/b | S/I/b | -3 | S/I/d | S/I/b | S/I/b | S/I/a |
| Intensidad | Intensidad | S/I/b | S/I/b | S/I/b | 3 | S/I/d | S/I/b | S/I/b | S/I/a |
| Ofensividad | Ofensividad | S/I/b | S/I/b | S/I/b | 3 | S/I/d | S/I/b | S/I/b | S/I/a |
| Calidad | Calidad | Humedad,<br>percolado,<br>agrio/b | Basura,<br>descomposición,<br>agrio/b | Tierra,<br>humedad,<br>basura/b | Marino,<br>rancio,<br>amoniaco/c | S/I/d | S/I/b | S/I/b | S/I/a |

**Tabla 13: - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 2**

| Requisito | Col2 | Estanque<br>ecualizador 1 | Estanque<br>ecualizador 2 | Estanque<br>ecualizador 3 | Reactor de<br>tratamiento<br>aerobio SBR<br>1-1 | Reactor de<br>tratamiento<br>aerobio SBR<br>1-2 | Reactor de<br>tratamiento<br>aerobio SBR<br>2-1 | Reactor de<br>tratamiento<br>aerobio SBR<br>2-2 | Camiones de<br>transporte |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fase del proyecto que<br>genera olor | Fase del proyecto que<br>genera olor | Operación | Operación | Operación | Operación | Operación | Operación | Operación | Operación |
| Actividad que genera<br>emisiones de olor | Actividad que genera<br>emisiones de olor | Tratamiento<br>de RILes | Tratamiento<br>de RILes | Tratamiento<br>de RILes | Tratamiento<br>de RILes | Tratamiento<br>de RILes | Tratamiento<br>de RILes | Tratamiento<br>de RILes | Transporte de<br>materiales |
| Identificación del<br>material o sustancia<br>olorosa | Identificación del<br>material o sustancia<br>olorosa | Digestato | Digestato | Digestato | Digestato | Digestato | Digestato | Digestato | Recepción y<br>almacenamiento<br>de conchillas,<br>Digestato y<br>Compost |
| Tipo de fuente | Tipo de fuente | Difusa | Difusa | Difusa | Difusa | Difusa | Difusa | Difusa | Fugitiva |
| Régimen de<br>emisión de<br>olor | Ciclo<br>operacional | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo |
| Régimen de<br>emisión de<br>olor | Horario de<br>operación | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 12 [h] |
| Régimen de<br>emisión de<br>olor | Frecuencia<br>mensual | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses |
| Emisión de olor<br>[ouE/m2*s] | Emisión de olor<br>[ouE/m2*s] | 3,80 | 3,80 | 3,80 | 19,08 | 19,08 | 19,08 | 19,08 | 0,05 |
| Tasa de emisión de olor<br>[ouE/s] | Tasa de emisión de olor<br>[ouE/s] | 41,75 | 41,75 | 41,75 | 1.431,00 | 1.431,00 | 1.431,00 | 1.431,00 | 1.790,80 |
| Tono hedónico | Tono hedónico | S/I/a | S/I/a | S/I/a | S/I/a | S/I/a | S/I/a | S/I/a | S/I/a |
| Intensidad | Intensidad | S/I/a | S/I/a | S/I/a | S/I/a | S/I/a | S/I/a | S/I/a | S/I/a |
| Ofensividad | Ofensividad | S/I/a | S/I/a | S/I/a | S/I/a | S/I/a | S/I/a | S/I/a | S/I/a |
| Calidad | Calidad | S/I/a | S/I/a | S/I/a | Detergente,<br>humedad,<br>ácido/a | Detergente,<br>humedad,<br>ácido/a | Detergente,<br>humedad,<br>ácido/a | Detergente,<br>humedad,<br>ácido/a | S/I/a |

**Tabla 14: - Ranking TEO [ou E /s] por fuente modelada - Situación futura**

| ID | Unidad | EO<br>[ou /m2s]<br>E | TEO<br>[ou /s]<br>E | % TEO | % TEO<br>acum. |
| --- | --- | --- | --- | --- | --- |
| 4 | Chimenea Scrubber (Calcinación) | 31.100,91 | 24.426,60 | 52,37% | 52,37% |
| 2 | Trincheras | 0,88 | 6.093,43 | 13,07% | 65,44% |
| 5 | Sistema de abatimiento de olores Carbonato- Biofiltro | 96,38 | 2.822,02 | 6,05% | 71,49% |
| 8 | Laguna de digestato | 0,32 | 2.592,00 | 5,56% | 77,05% |
| 3 | Patio de maduración | 0,70 | 2.099,61 | 4,50% | 81,55% |
| 16 | Camiones de transporte | 0,05 | 1.790,40 | 3,84% | 85,39% |
| 12 | Reactor de tratamiento aerobio SBR 1-1 | 19,08 | 1.431,00 | 3,07% | 88,46% |
| 13 | Reactor de tratamiento aerobio SBR 1-2 | 19,08 | 1.431,00 | 3,07% | 91,53% |
| 14 | Reactor de tratamiento aerobio SBR 2-1 | 19,08 | 1.431,00 | 3,07% | 94,59% |
| 15 | Reactor de tratamiento aerobio SBR 2-2 | 19,08 | 1.431,00 | 3,07% | 97,66% |
| 6 | Sistema de abatimiento de olores Biogás - Biofiltro | 20,87 | 611,01 | 1,31% | 98,97% |
| 1 | Sistema de abatimiento de olores Compostaje - Biofiltro | 12,05 | 352,80 | 0,76% | 99,73% |
| 9 | Estanque ecualizador 1 | 3,80 | 41,75 | 0,09% | 99,82% |
| 10 | Estanque ecualizador 2 | 3,80 | 41,75 | 0,09% | 99,91% |
| 11 | Estanque ecualizador 3 | 3,80 | 41,75 | 0,09% | 100,00% |
| 7 <br> | Deshidratador | 0,32 | 1,20 | 0,00%<br> | 100,00%<br> |

**Tabla 15: - Puntos receptores de interés**

| ID | Descripción | Coordenadas UTM [m]<br>(WGS84-18 G) | Col4 | Distancia de<br>receptor desde<br>perímetro<br>predial<br>[m] | Orientación |
| --- | --- | --- | --- | --- | --- |
| ID | Descripción | X: Este | Y: Sur | Y: Sur | Y: Sur |
| R1 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 643.642 | 5.393.170 | 636 | OSO |
| R2 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 643.846 | 5.393.126 | 472 | SO |
| R3 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 643.905 | 5.392.985 | 493 | SO |
| R4 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 643.884 | 5.392.862 | 580 | SO |
| R5 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 644.596 | 5.392.490 | 858 | S |
| R6 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 645.279 | 5.393.031 | 649 | SE |
| R7 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 645.426 | 5.393.416 | 502 | ESE |
| R8 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 645.430 | 5.393.521 | 439 | ESE |
| R9 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 645.728 | 5.393.863 | 584 | E |
| R10 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 645.681 | 5.394.079 | 623 | ENE |
| R11 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 645.430 | 5.394.234 | 474 | ENE |
| R12 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 644.968 | 5.394.229 | 79 | NE |
| R13 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 644.950 | 5.394.281 | 63 | NE |
| R14 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 645.051 | 5.394.456 | 255 | NNE |
| R15 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 645.162 | 5.393.860 | 33 | E |
| R16 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 645.603 | 5.393.258 | 760 | ESE |
| R17 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 645.395 | 5.393.441 | 471 | ESE |
| R18 | Vivienda ubicada fuera del límite urbano<br>de Maullín | 645.335 | 5.393.068 | 675 | SE |

**Tabla 16: - Proyectos aprobados por el SEA**

| Nombre del proyecto | Titular del proyecto | N.o RCA | Distancia del<br>proyecto<br>desde el<br>perímetro<br>predial [m] | Coordenadas UTM<br>[m] | Col6 |
| --- | --- | --- | --- | --- | --- |
| Nombre del proyecto | Titular del proyecto | N.o RCA | Distancia del<br>proyecto<br>desde el<br>perímetro<br>predial [m] | X: Este | Y: Norte |
| Planta procesadora de<br>recursos hidrobiológicos-<br>pesquera La Portada (PPRH-<br>PP) | Pesquera La Portada<br>S.A. | 429/05 | 2.370 | 644.942 | 5.396.639 |
| Sistema de neutralización y<br>depuración de Residuos<br>Industriales Líquidos<br>(Gelymar S.A.) | Extractos Naturales<br>Gelymar S.A. | 176/00 | 6.191 | 650.820 | 5.396.173 |
| Planta de Carbonato de<br>Calcio CALAGRO | Inversiones Las<br>Garzas S.A. | 105/13 | 8.738 | 653.180 | 5.397.182 |
| Modificación proyecto retiro,<br>transporte y almacenamiento<br>prolongado de Respel Rexin | Rexin SpA. | 273/08 | 1.988 | 646.800 | 5.395.140 |
| Sistema de adecuación de<br>lodos orgánicos Rexin | Rexin SpA. | 157/08 | 1.988 | 646.800 | 5.395.140 |

**Tabla 17: - Concentraciones máximas en receptores según normativa de Trento.**

| Receptores | Percentil | Valores [ou /m3]<br>E |
| --- | --- | --- |
| Receptores a una distancia >500 [m] desde el deslinde del predio | 98 | 2 |
| Receptores a una distancia entre 200 [m] y 500 [m] desde el deslinde del predio | Receptores a una distancia entre 200 [m] y 500 [m] desde el deslinde del predio | 3 |
| Receptores a una distancia <200 [m] desde el deslinde del predio | Receptores a una distancia <200 [m] desde el deslinde del predio | 4 |

**Tabla 18: - Valores de aceptabilidad de concentración de olor en receptores según distancia**

| ID | Descripción | Distancia al<br>perímetro de<br>la planta<br>[m] | Rango<br>distancia<br>[m] | Valor límite norma<br>Trento<br>CO<br>[ou /m3]<br>E |
| --- | --- | --- | --- | --- |
| R1 | Vivienda ubicada fuera del límite urbano de Maullín | 636 | >500 | 2 |
| R2 | Vivienda ubicada fuera del límite urbano de Maullín | 472 | 200 - 500 | 3 |
| R3 | Vivienda ubicada fuera del límite urbano de Maullín | 493 | 200 - 500 | 3 |
| R4 | Vivienda ubicada fuera del límite urbano de Maullín | 580 | >500 | 2 |
| R5 | Vivienda ubicada fuera del límite urbano de Maullín | 858 | >500 | 2 |
| R6 | Vivienda ubicada fuera del límite urbano de Maullín | 649 | >500 | 2 |
| R7 | Vivienda ubicada fuera del límite urbano de Maullín | 502 | >500 | 2 |
| R8 | Vivienda ubicada fuera del límite urbano de Maullín | 439 | 200 - 500 | 3 |
| R9 | Vivienda ubicada fuera del límite urbano de Maullín | 584 | >500 | 2 |
| R10 | Vivienda ubicada fuera del límite urbano de Maullín | 623 | >500 | 2 |
| R11 | Vivienda ubicada fuera del límite urbano de Maullín | 474 | 200 - 500 | 3 |
| R12 | Vivienda ubicada fuera del límite urbano de Maullín | 79 | <200 | 4 |
| R13 | Vivienda ubicada fuera del límite urbano de Maullín | 63 | <200 | 4 |
| R14 | Vivienda ubicada fuera del límite urbano de Maullín | 255 | 200 - 500 | 3 |
| R15 | Vivienda ubicada fuera del límite urbano de Maullín | 33 | <200 | 4 |
| R16 | Vivienda ubicada fuera del límite urbano de Maullín | 760 | >500 | 2 |
| R17 | Vivienda ubicada fuera del límite urbano de Maullín | 471 | 200 - 500 | 3 |
| R18 | Vivienda ubicada fuera del límite urbano de Maullín | 675 | >500 | 2 |

**Tabla 19: - Descripción escenarios simulados**

| Escenario | Modelo | Percentil | Criterio de<br>calidad |
| --- | --- | --- | --- |
| E1: Situación futura | M1: Curvas de isoconcentración de olor<br>M2: Frecuencia de percepción de olor (horaria)<br>M3: Frecuencia de percepción de olor (mensual)<br>M4: Concentración máxima horaria | 98 | 2, 3 y 4<br>[ouE/m3] |

**Tabla 20: - E1/M2: Frecuencia de percepción de olor horaria - C P98-1hr =2, 3 y 4 [ou E /m [3] ]**

| Valor límite<br>CP98 | 2 [ou /m3]<br>E | 3 [ou /m3]<br>E | 4 [ou /m3]<br>E |
| --- | --- | --- | --- |
| Hora del día | **R1**<br>**R4**<br>**R5**<br>**R6**<br>**R7**<br>**R9**<br>**R10**<br>**R16**<br>**R18** | **R2**<br>**R3**<br>**R8**<br>**R11**<br>**R14**<br>**R17** | **R12**<br>**R13**<br>**R15** |
| 0 <br>1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23 | 0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 | 0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 | 0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 |
| Total | **0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 ** | **0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 ** | **0 **<br>**0 **<br>**0 ** |

**Tabla 21: - E1/M3: Frecuencia de percepción de olor mensual - C P98-1hr =2, 3 y 4 [ou E /m [3] ]**

| Valor límite<br>CP98 | 2 [ou /m3]<br>E | 3 [ou /m3]<br>E | 4 [ou /m3]<br>E |
| --- | --- | --- | --- |
| Hora del día | **R1**<br>**R4**<br>**R5**<br>**R6**<br>**R7**<br>**R9**<br>**R10**<br>**R16**<br>**R18** | **R2**<br>**R3**<br>**R8**<br>**R11**<br>**R14**<br>**R17** | **R12**<br>**R13**<br>**R15** |
| Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre | 0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 | 0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 | 0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 |
| Total | **0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 ** | **0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 ** | **0 **<br>**0 **<br>**0 ** |

**Tabla 22: - Concentración máxima - Percentil 98 y 99,5 - Situación futura**

| ID | Concentración máxima [ou /m3]<br>E | Col3 | Limite aceptabilidad<br>Normativa de Trento<br>CO [ou /m3]<br>E | Cumplimiento | Superación valor<br>límite normado |
| --- | --- | --- | --- | --- | --- |
| ID | Percentil 99,5 | Percentil 98 | Percentil 98 | Percentil 98 | Percentil 98 |
| R1 | 1 | <1 | 2 | Sí | No |
| R2 | 2 | <1 | 3 | Sí | No |
| R3 | 1 | <1 | 3 | Sí | No |
| R4 | 1 | <1 | 2 | Sí | No |
| R5 | <1 | <1 | 2 | Sí | No |
| R6 | 1 | <1 | 2 | Sí | No |
| R7 | 1 | <1 | 2 | Sí | No |
| R8 | 1 | <1 | 3 | Sí | No |
| R9 | 1 | <1 | 2 | Sí | No |
| R10 | 1 | <1 | 2 | Sí | No |
| R11 | 1 | <1 | 3 | Sí | No |
| R12 | 2 | 1 | 4 | Sí | No |
| R13 | 2 | 1 | 4 | Sí | No |
| R14 | 1 | <1 | 3 | Sí | No |
| R15 | 3 | 1 | 4 | Sí | No |
| R16 | <1 | <1 | 2 | Sí | No |
| R17 | 1 | <1 | 3 | Sí | No |
| R18 | <1 | <1 | 2 | Sí | No |

**Tabla 23: - Situación futura: Caracterización de fuentes de olor**

| ID | Fuente | Coordenadas UTM [m] | Col4 | Altura<br>desde<br>suelo [m] | Vel.<br>salida<br>[m/s] | Temp.<br>salida<br>[oK] | Diám.<br>ducto<br>[m] | Largo<br>[m] | Ancho<br>[m] | Radio<br>[m] | Área<br>[m2] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ID | Fuente | X: Este | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte |
| 1 | Sist. de abatimiento de olores Compostaje - Biofiltro | 644.351 | 5.393.842 | 4,00 | - | - | - | 12,00 | 2,44 | - | 29,28 |
| 2 | Trincheras | 644.295 | 5.393.676 | 2,40 | - | - | - | 24,00 | 288,00 | - | 6.912,00 |
| 3 | Patio de maduración | 644.313 | 5.393.638 | 4,00 | - | - | - | 150,00 | 20,00 | - | 3.000,00 |
| 4 | Chimenea Scrubber (Calcinación) | 644.533 | 5.393.734 | 12,00 | 2,98 | 366,25 | 1,00 | - | - | - | 0,79 |
| 5 | Sist. de abatimiento de olores Carbonato - Biofiltro | 644.552 | 5.393.741 | 4,00 | - | - | - | 12,00 | 2,44 | - | 29,28 |
| 6 | Sist. de abatimiento de olores Biogás - Biofiltro | 644.547 | 5.393.560 | 3,00 | - | - | - | 12,00 | 2,44 | - | 29,28 |
| 7 | Deshidratador | 644.491 | 5.393.673 | 2,00 | - | - | - | 4,45 | 0,84 | - | 3,74 |
| 8 | Laguna de digestato | 644.696 | 5.393.668 | 0,00 | - | - | - | 90,00 | 90,00 | - | 8.100,00 |
| 9 | Estanque ecualizador 1 | 644.393 | 5.393.614 | 3,00 | - | - | - | - | - | 1,87 | 10,99 |
| 10 | Estanque ecualizador 2 | 644.395 | 5.393.608 | 3,00 | - | - | - | - | - | 1,87 | 10,99 |
| 11 | Estanque ecualizador 3 | 644.398 | 5.393.604 | 3,00 | - | - | - | - | - | 1,87 | 10,99 |
| 12 | Reactor de tratamiento aerobio SBR 1-1 | 644.372 | 5.393.601 | 6,00 | - | - | - | 15,00 | 5,00 | - | 75,00 |
| 13 | Reactor de tratamiento aerobio SBR 1-2 | 644.376 | 5.393.596 | 6,00 | - | - | - | 15,00 | 5,00 | - | 75,00 |
| 14 | Reactor de tratamiento aerobio SBR 2-1 | 644.379 | 5.393.591 | 6,00 | - | - | - | 15,00 | 5,00 | - | 75,00 |
| 15 | Reactor de tratamiento aerobio SBR 2-2 | 644.382 | 5.393.586 | 6,00 | - | - | - | 15,00 | 5,00 | - | 75,00 |
| 16 | Camiones de transporte | 645.423 | 5.393.115 | 2,00 | - | - | - | 4.345,80 | 8,62 | - | 37.460,80 |

**Tabla 24: - Situación futura: Características operacionales de fuentes emisoras**

| ID | Fuente | Tipo de<br>fuente | Área [m2] | EO por sup.<br>[ou/m2s]<br>E | TEO<br>[ou/s]<br>E | Ciclo de<br>operación | Horas de operación | Días de<br>operación | Meses de<br>operación |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Sist. de abat. de olores Compostaje - Biofiltro | Difusa | 29,28 | 12,05 | 352,80 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 2 | Trincheras | Difusa | 6.912,00 | 0,83 | 5.736,96 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 3 | Patio de Maduración | Difusa | 3.000,00 | 0,40 | 1.200,00 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 4 | Chimenea Scrubber (Calcinación) | Puntual | 0,79 | 31.100,91 | 24.426,60 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 5 | Sist. de abat. de olores Carbonato- Biofiltro | Difusa | 29,28 | 96,38 | 2.822,02 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 6 | Sist. de abat. de olores Biogás - Biofiltro | Difusa | 29,28 | 20,87 | 611,01 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 7 | Deshidratador | Difusa | 3,74 | 0,32 | 1,20 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 8 | Laguna de digestato | Difusa | 8.100,00 | 0,32 | 2.592,00 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 9 | Estanque ecualizador 1 | Difusa | 10,99 | 3,80 | 41,75 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 10 | Estanque ecualizador 2 | Difusa | 10,99 | 3,80 | 41,75 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 11 | Estanque ecualizador 3 | Difusa | 10,99 | 3,80 | 41,75 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 12 | Reactor de tratamiento aerobio SBR 1-1 | Difusa | 75,00 | 19,08 | 1.431,00 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 13 | Reactor de tratamiento aerobio SBR 1-2 | Difusa | 75,00 | 19,08 | 1.431,00 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 14 | Reactor de tratamiento aerobio SBR 2-1 | Difusa | 75,00 | 19,08 | 1.431,00 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 15 | Reactor de tratamiento aerobio SBR 2-2 | Difusa | 75,00 | 19,08 | 1.431,00 | Continuo | 24 horas (00:00-23:59) | Lu - Do | Ene -Dic |
| 16 | Camiones de transporte | Fugitiva | 37.461 | 0,05 | 1.790,40 | Continuo | 12 horas (08:00-19:59) | Lu - Do | Ene -Dic |

**Tabla 25: - Base de cálculo: emisiones de entrada biofiltro de planta de biogás**

| Fuente | N°<br>Unidades | Área<br>[m2] | Emisión de<br>Referencia<br>[ou/m2s]<br>E | Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E |
| --- | --- | --- | --- | --- |
| Higienizado | 2 | 19,63 | 3,80/a | 149,23 |
| Estanque de recepción | 1 | 144,00 | 41,10/b | 5.918,40 |
| Estanque de mezcla | 1 | 132,73 | 0,32/c | 42,47 |

**Tabla 26: - Base de cálculo: emisión proyectada en biofiltro de planta de biogás**

| Fuente | N°<br>Unidades | Área<br>[m2] | Eficiencia de<br>remoción de<br>olor [%] | Emisión de<br>Referencia<br>[ou/m2s]<br>E | Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E |
| --- | --- | --- | --- | --- | --- |
| Sistema de abatimiento de olores- biofiltro | 1 | 29,28 | 90%/a | 20,87 | 611,01 |

**Tabla 27: - Base de cálculo: emisiones de entrada biofiltro de galpón de compostaje**

| Fuente | N°<br>Unidades | Área total del<br>galpón<br>[m2] | Área efectiva<br>de emisión<br>de olor/a<br>[m2] | Emisión de<br>Referencia/b<br>[ou/m2s]<br>E | Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E |
| --- | --- | --- | --- | --- | --- |
| Galpón de compostaje | 1 | 600,00 | 240,00 | 14,70 | 3.528,00 |

**Tabla 28: - Base de cálculo: emisión proyectada en biofiltro de galpón de compostaje**

| Fuente | N°<br>Unidades | Área<br>[m2] | Eficiencia de<br>remoción de<br>olor [%] | Emisión de<br>Olor<br>[ou/m2s]]<br>E | Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E |
| --- | --- | --- | --- | --- | --- |
| Sistema de abatimiento de olores- biofiltro | 1 | 29,28 | 90%/a | 12,05 | 352,80 |

**Tabla 29: - Base de cálculo: emisiones compostaje en trincheras**

| Fuente | N°<br>Unidades | Área unitaria<br>trinchera [m2] | Área total de<br>trincheras/a | Emisión de<br>Olor/a<br>[ou/m2s]<br>E | Tasa de<br>Emisión de Olor<br>[ou/s]<br>E |
| --- | --- | --- | --- | --- | --- |
| Trincheras en operación | 32 | 216 | 6.912 | 0,88 | 6.093,43 |

**Tabla 30: - Base de cálculo: emisiones proyectadas de trincheras según condición**

| Fuente | Unidades | %Un | Emisión de Olor<br>[ou/m2s]<br>E | Tasa de<br>Emisión de Olor<br>[ou/s]<br>E |
| --- | --- | --- | --- | --- |
| Trincheras cubiertas/a | 30 | 93,75% | 0,83 | 5.378,40 |
| Trincheras carga/descarga/b | 2 | 6,25% | 1,66 | 715,03 |

**Tabla 31: - Base de cálculo: emisiones proyectadas de trincheras en condición de carga/descarga**

| Condición | Unidades | % total de<br>unidades según<br>condición | EO Prom<br>[ou/m2s]<br>E |
| --- | --- | --- | --- |
| Con carga/a | 1 | 3,13% | 2,78 |
| Con descarga/b | 1 | 3,13% | 0,54 |
| Cubierta | 32 | 93,75% | 0,83 |

**Tabla 32: - Base de cálculo: emisiones de patio de maduración**

| Fuente | Área de emisión/a<br>[m2] | Emisión de Olor/b<br>[ou/m2s]<br>E | Tasa de Emisión de<br>Olor<br>[ou/s]<br>E |
| --- | --- | --- | --- |
| Patio de maduración total | 3.000 | 0,70 | 2.099,61 |

**Tabla 33: - Base de cálculo: emisiones proyectadas de patio de maduración según condición**

| TEO | Área unitaria<br>[m2] | % total de<br>superficie según<br>condición | EO<br>[ou/m2s]<br>E | TEO Pond<br>[ou/s]<br>E |
| --- | --- | --- | --- | --- |
| Patio de maduración cubierto (con volteo)/a | 2.850 | 95,00% | 0,71 | 2.014,65 |
| Patio de maduración carga/descarga/b <br> | 150<br> | 5,00%<br> | 0,57<br> | 84,96<br> |

**Tabla 34: - Base de cálculo: emisiones proyectadas de patio de maduración en condición de carga/descarga**

| Condición | Área unitaria<br>[m2] | % total de<br>superficie según<br>condición | EO<br>[ou/m2s]<br>E |
| --- | --- | --- | --- |
| Con carga/a | 75 | 2,50% | 0,63 |
| Con descarga/b | 75 | 2,50% | 0,51 |

**Tabla 35: - Base de cálculo: emisiones de entrada biofiltro de planta de carbonato de calcio**

| Fuente | Volumen de<br>procesamiento<br>[ton/año] | Caudal<br>[m3/s] | Concentración<br>de olor<br>[ou/m3]<br>E | Tasa de Emisión<br>de Olor<br>[ou/s]<br>E |
| --- | --- | --- | --- | --- |
| Planta de referencia Calizas Marinas S.A. | 200.000,00 | 3,89 | 96.755,00 | 376.269,44 |
| Planta de carbonato proyectada | 15.000,00 | 3,90 | - | 28.220,21 |

**Tabla 36: - Base de cálculo: emisión proyectada en biofiltro de planta de carbonato de calcio**

| Fuente | N°<br>Unidades | Área<br>[m2] | Eficiencia de<br>remoción de<br>olor [%] | Emisión de<br>Referencia<br>[ou/m2s]<br>E | Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E |
| --- | --- | --- | --- | --- | --- |
| Sistema de abatimiento de olores- biofiltro | 1 | 29,28 | 90%/a | 96,38 | 2.822,02 |

**Tabla 37: - Base de cálculo: emisiones de salida chimenea scrubber de planta de carbonato de calcio**

| Fuente | Volumen de<br>procesamiento<br>[ton/año] | Caudal<br>[m3/s] | Concentración<br>de olor<br>[ou/m3]<br>E | Tasa de Emisión<br>de Olor<br>[ou/s]<br>E |
| --- | --- | --- | --- | --- |
| Chimenea de Planta de carbonato de calcio<br>CALAGRO | 25.000,00 | 3,89 | 10.468,54 | 40.711,00 |
| Chimenea scrubber de Planta de carbonato<br>proyectada | 15.000,00 | 2,34 | - | 24.426,60 |

**Tabla 38: - Base de cálculo: emisiones de camiones en tránsito por camiones de transporte**

| ID | Tránsito vehicular de<br>camiones con cobertura<br>según tipo | Máximo<br>camiones<br>diarios<br>[camiones x<br>día] | Área de<br>emisión<br>[m2] | EO<br>[ou/m2s]<br>E | Retención<br>de olores<br>por<br>cobertura | EO con<br>cobertura<br>[ou/m2s]<br>E | TEO<br>Camión<br>[ou/s]<br>E | TEO Total<br>[ou/s]<br>E |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Recepción MMPP<br>(Residuos Orgánicos) | 8 | 24 | 14,70 | 50% | 7,35 | 176,40 | 1.411,20 |
| 2 | Despacho compost | 5 | 5 | 1,60 | 1,60 | 0,80 | 19,20 | 96,00 |
| 3 | Despacho digestato sólido | 4 | 4 | 0,32 | 0,32 | 0,16 | 3,84 | 15,36 |
| 4 | Conchas Moluscos planta<br>carbonato | 3 | 3 | 7,44 | 7,44 | 3,72 | 89,28 | 267,84 |

**Tabla 39: - Base de cálculo: emisiones de tránsito por camiones de transporte**

| Nombre fuente | Altura desde<br>el suelo [m]<br>(desde dónde<br>emite) | Largo<br>[m] | Ancho<br>[m] | Área de<br>emisión<br>[m2] | EO<br>[ou/m2s]<br>E | TEO Ruta<br>[ou/s]<br>E |
| --- | --- | --- | --- | --- | --- | --- |
| Tránsito por Ruta interna - Sección 1 | 3 | 2.988 | 9 | 25.760 | 0,05 | 1.231 |
| Tránsito por Ruta interna - Sección 2 | 3 | 776 | 9 | 6.693 | 6.693 | 320 |
| Tránsito por Ruta interna - Sección 3 | 3 | 581 | 9 | 5.008 | 5.008 | 239 |

**Tabla 40: - Descripción de grilla anidada**

| Coordenada centro<br>UTM 18 G | UTM N[m] | UTM E [m] |
| --- | --- | --- |
| Coordenada centro<br>UTM 18 G | 644.354 | 5.393.838 |
| Grilla | Distancia desde el<br>centro [m] | Espaciado entre<br>receptores [m] |
| 1 | 100 | 10 |
| 2 | 500 | 50 |
| 3 | 1.000 | 100 |
| 4 | 2.000 | 200 |
| 5 | 4.000 | 500 |

**Tabla 41: - Coordenada central Plataforma Economía Circular Volta Los Lagos**

| Coordenadas UTM [m] | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| X: Este | Y: Sur | Huso | Datum |
| 644.590 | 5.393.748 | 18 G | WGS 84 |

**Tabla 42: - Rosas y campos de viento pronóstico anual**

| Col1 | Rosa de vientos | Col3 | Distribución de velocidad del viento | Características |
| --- | --- | --- | --- | --- |
| Anual Nocturno<br>(00:00 a 6:59 horas) |  |  | <br>6.95<br>13.12<br>31.10<br>22.50<br>14.42<br>6.88<br>3.08<br>1.34<br>0.38<br>0.24<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Los<br>campos<br>de<br>vientos<br>predominaron<br>principalmente desde las componentes NNE<br>(17%) y N (16%) a lo largo del horario<br>nocturno.<br>La<br>distribución<br>del<br>viento<br>tuvo<br>un<br>comportamiento<br>asimétrico<br>positivo.<br>La<br>velocidad se caracterizó como brisa muy débil80. <br> <br>Velocidad promedio de viento: 2,22 [m/s].<br> <br>Frecuencia de vientos calmos: 6,95%. |
| Anual AM<br>(7:00 a 14:59 horas) |  |  | <br>3.32<br>7.60<br>19.14<br>23.15<br>25.07<br>14.42<br>4.55<br>1.47<br>0.96<br>0.31<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | En el horario AM, las masas de aire provinieron<br>en mayor frecuencia desde dirección S con un<br>21%, y consecutivamente desde la componente<br>N (14%). En general, la intensidad del viento<br>varió de brisa muy débil a débil81.<br>Respecto a la distribución de los vientos, éstos<br>tuvieron una tendencia mesocúrtica.<br> <br>Velocidad promedio de viento: 2,87 [m/s].<br> <br>Frecuencia de vientos calmos: 3,32%. |
| Anual PM<br>(15:00 a 23:59 horas) |  |  | <br>2.43<br>6.99<br>32.60<br>27.19<br>16.54<br>8.46<br>3.29<br>1.44<br>0.75<br>0.31<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Durante el horario PM, se observó predominio<br>de los vientos desde la dirección S con una<br>frecuencia del 17%. La velocidad de los vientos<br>se caracterizó como una brisa muy débil82.<br>La distribución de los vientos se observó con<br>una curva asimétrica positivo.<br> <br>Velocidad promedio de viento: 2,52 [m/s]<br> <br>Frecuencia de vientos calmos: 2,43% |
