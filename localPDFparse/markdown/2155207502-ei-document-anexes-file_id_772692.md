---
title: Sin título
author: Antonio Santos
date: D:20220216131324-03'00'
language: es
type: report
pages: 62
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO I JUSTIFICACIÓN DE POTENCIAS ACÚSTICAS
  - ANEXO II CÁLCULO INSUL OSB 18 [mm]
-->

## ESTUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

### PROYECTO MAKROPLAZA COMUNA DE VIÑA DEL MAR - REGIÓN DE VALPARAÍSO

**P** **REPARADO PARA** **:**

|PROYECTO N°: 5362|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**VERSIÓN**|**FECHA**|**DESCRIPCIÓN**|**ELABORACIÓN**|**REVISIÓN**<br>|**APROBACIÓN**|
|**A **|09.02.2022|Elaboración Inicial|NHP - MDF|~~MGD~~||
|**B **|14.02.2022|Incorpora observaciones|MDF - JSC|CSC||

S ANTIAGO, FEBRERO DE 2022

G ERARD I NGENIERÍA A CÚSTICA S P A

SE ENCUENTRA CERTIFICADO POR :

**ÍNDICE DE CONTENIDOS**

1 Introducción ............................................................................................................................................4

2 Objetivos ................................................................................................................................................5

2.1 Objetivo general ..............................................................................................................................5

2.2 Objetivos específicos .......................................................................................................................5

3 Normativas y guía de referencia ...............................................................................................................6

3.1 Ruido de maquinaria e instalaciones .................................................................................................6

3.2 Ruido flujo vehicular ........................................................................................................................7

3.3 Vibraciones de maquinaria ............................................................................................................. 10

4 Área de estudio y puntos de medición ..................................................................................................... 11

4.1 Área de influencia (AI) ................................................................................................................... 11

4.2 Puntos de evaluación .................................................................................................................... 14

4.3 Máximos permisibles ..................................................................................................................... 17

4.3.1 Ruido - D.S. N° 38/2011 del MMA ............................................................................................ 17

4.3.2 Ruido - FTA Transit Noise and Vibration Impact Assessment Manual (Humanos) ......................... 17

4.3.3 Vibraciones - FTA ................................................................................................................... 18

5 Metodología .......................................................................................................................................... 18

5.1 Modelación de ruido ...................................................................................................................... 18

5.1.1 Maquinarias e instalaciones ..................................................................................................... 18

5.1.2 Flujo vehicular......................................................................................................................... 19

5.2 Proyección de vibraciones.............................................................................................................. 22

6 Datos de entrada al modelo predictivo de ruido ........................................................................................ 25

6.1 Fase de construcción..................................................................................................................... 25

6.1.1 Ruido de maquinaria e instalaciones ......................................................................................... 25

6.1.2 Flujo vehicular......................................................................................................................... 29

7 Resultados ........................................................................................................................................... 30

7.1 Modelación y evaluación preliminar................................................................................................. 30

7.1.1 Fase de construcción............................................................................................................... 30

7.1.1.1 Ruido de maquinaria e instalaciones ............................................................................... 30

7.1.1.2 Flujo vehicular............................................................................................................... 36

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

1

7.2 Proyección de vibraciones.............................................................................................................. 38

8 Medidas de control ................................................................................................................................ 39

8.1 Ruido ........................................................................................................................................... 39

8.1.1 Escenario 1: Barreras acústicas................................................................................................ 39

8.1.2 Escenario 2: Cierre de vanos.................................................................................................... 42

8.2 Vibraciones................................................................................................................................... 43

8.2.1 Buffer de seguridad ................................................................................................................. 43

9 Resultados y evaluación con medidas de control ..................................................................................... 44

9.1 Ruido ........................................................................................................................................... 44

9.2 Vibraciones................................................................................................................................... 50

10 Conclusiones ........................................................................................................................................ 51

11 Instrumental .......................................................................................................................................... 52

12 Bibliografía ........................................................................................................................................... 52

13 Profesionales participantes .................................................................................................................... 53

14 Glosario................................................................................................................................................ 53

ANEXO I....................................................................................................................................................... 55

ANEXO II...................................................................................................................................................... 60

**ÍNDICE DE ILUSTRACIONES**

Ilustración 1: Tipo de impacto según incremento de los niveles y ruido existente. .........................................................................................................7
Ilustración 2: Área de influencia. Vista general. ........................................................................................................................................................13
Ilustración 3: Ubicación de los puntos de evaluación. Vista general. ..........................................................................................................................14
Ilustración 4: Fotografías de los puntos de medición de ruido y vibraciones................................................................................................................15
Ilustración 5: Croquis que representa la propagación en infraestructura vial. ..............................................................................................................21
Ilustración 6: Esquema de propagación semi-cilíndrica. ............................................................................................................................................21
Ilustración 7: Ejemplo de situación más desfavorable de propagación de vibraciones según distancia entre maquinaria y recepto r.................................24
Ilustración 8: Esquema fase de construcción. Ruido de maquinaria e instalaciones. Escenario1. .................................................................................27
Ilustración 9: Esquema fase de construcción. Ruido de maquinaria e instalaciones. Escenario2. .................................................................................28
Ilustración 10: Esquema fase de construcción. Flujo vehicular...................................................................................................................................29
Ilustración 11: Mapa de propagación sonora según NPSeq en [dB(A)]. Fase de construcción. Escenario 1...................................................................30
Ilustración 12: Mapa de propagación sonora según NPSeq en [dB(A)]. Fase de construcción. Escenario 2...................................................................33
Ilustración 13: Mapa de propagación sonora según L DN en [dB(A)]. Fase de construcción. Flujo vehicular. ...................................................................36
Ilustración 14: Croquis implementación de barrera acústica. Fase de construcción. Escenario 1. .................................................................................41
Ilustración 15: Ejemplo de aplicación de medida de confinamiento. ...........................................................................................................................42
Ilustración 16: Croquis implementación de buffer de seguridad. Fase de construcción. Punto 1. ..................................................................................43
Ilustración 17: Mapa de propagación sonora según NPSeq en [dB(A)]. Fase de construcción con medidas de control. Escenario 1. ...............................44
Ilustración 18: Mapa de propagación sonora según NPSeq en [dB(A)]. Fase de construcción con medidas de control. Escenario 2. ...............................47
Ilustración 19: Ficha técnica allanadora de pavimento. .............................................................................................................................................57
Ilustración 20: Software ENC 4.1. Cálculo potencia acústica motor eléctrico 9 [HP].....................................................................................................59

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

2

**ÍNDICE DE TABLAS**

Tabla 1: Descripción de usos de suelo permitidos para cada tipo de zona según D.S. N° 38/2011 MMA. .......................................................................6

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- de inmisión de ruido generados por las fuentes emisoras de ruido definidas en su Artículo N° 6, punto 13. Los límites máximos permitidos por la normativa están asociados a la zonificación acorde con el Instrumento de Planificación Territorial (IPT) respectivo. Los tipos de zonas se definen como: -->

**Tabla 1: Descripción de usos de suelo permitidos para cada tipo de zona según D.S. N° 38/2011 MMA.****

| Tipo de Zona | Descripción |
| --- | --- |
| Zona I | Aquella zona definida en el IPT respectivo y ubicada dentro del límite urbano, que permite exclusivamente<br>uso de suelo Residencial o bien este uso de suelo y alguno de los siguientes usos de suelo: Espacio Público<br>y/o Área Verde. |
| Zona II | Aquella zona definida en el IPT respectivo y ubicada dentro del límite urbano, que permite además los usos<br>de la Zona I, Equipamiento a cualquier escala. |
| Zona III | Aquella zona definida en el IPT respectivo y ubicada dentro del límite urbano, que permite además de los<br>usos de suelo de la Zona II, Actividades Productivas y/o de Infraestructura.<br> |
| Zona IV | ~~Aquella zona definida en el IPT respectivo y ubicada dentro del límite urbano, que permite sólo usos de~~<br>suelo de Actividades Productivas y/o de Infraestructura. |
| Zona Rural | Aquella ubicada al exterior del límite urbano establecido en el Instrumento de Planificación Territorial<br>respectivo. |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: D.S. 38/2011 del MMA, artículo 6° numerales 28al 32. Los Niveles de Presión Sonora Corregidos (NPC) que se obtengan no podrán exceder los valores de la siguiente tabla: -->
<!-- FIN TABLA 1 -->

Tabla 2: Niveles máximos permisibles de NPC según D.S. N° 38/2011 del MMA..........................................................................................................6

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Fuente: D.S. 38/2011 del MMA, artículo 6° numerales 28al 32. Los Niveles de Presión Sonora Corregidos (NPC) que se obtengan no podrán exceder los valores de la siguiente tabla: -->

**Tabla 2: Niveles máximos permisibles de NPC según D.S. N° 38/2011 del MMA.****

| Tipo de Zona | Nivel de Presión Sonora Corregido (NPC) Máximo Permitido [dB(A)] | Col3 |
| --- | --- | --- |
| **Tipo de Zona** | **Periodo Diurno**<br>**7:00 a 21:00 horas** | **Periodo Nocturno**<br>**21:00 a 7:00 horas** |
| Zona I | 55 | 45 |
| Zona II | 60 | 45 |
| Zona III | 65 | 50 |
| Zona IV | 70 | 70 |
| Zona Rural | Menor nivel entre el Nivel de Ruido de Fondo +10 [dB], y el NPC máximo permitido para Zona III | Menor nivel entre el Nivel de Ruido de Fondo +10 [dB], y el NPC máximo permitido para Zona III |

<!-- Estadísticas: 6 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: D.S. 38/2011 del MMA, artículos 7° y 9°. El criterio para zona rural se aplicará en periodo diurno y nocturno de manera independiente. -->
<!-- FIN TABLA 2 -->

Tabla 3: Categoría de uso de suelo y descriptor para criterio de impacto de ruido de tránsito vehicular. .........................................................................8

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- de ruido exterior futuros generados por el Proyecto propuesto. Estos incorporan criterios absolutos, que consideran el aporte de la actividad generada solo por la operación del proyecto. La categoría del receptor y/o edificación evaluada se definen según el uso de suelo, como se detalla a continuación: -->

**Tabla 3: Categoría de uso de suelo y descriptor para criterio de impacto de ruido de tránsito vehicular.****

| Categoría según<br>uso de suelo | Unidad de<br>medida [dB(A)] | Descripción |
| --- | --- | --- |
| 1 | Leq [h]* | Sectores donde bajos niveles de ruido sean indispensables para las actividades a desarrollar.<br>(Teatros, salas de concierto, estudios de grabación, entre otros) |
| 2 | LDN | Sectores con construcciones que la gente utiliza normalmente para dormir. (Viviendas,<br>hospitales y hoteles) |
| 3 <br> | Leq [h]*<br> | Suelo institucional con uso principalmente diurno. Esta categoría incluye colegios, librerías,<br>teatros e iglesias, en donde es importante evitar interferencias con las actividades como el<br>habla, meditación y concentración en la lectura de material. Lugares para meditación o<br>asociados a estudio con cementerios, monumentos, museos, sector de camping y<br>recreacionales, pueden también ser considerados para estar en esta categoría. Sitios<br>históricos y parques pueden también ser considerados<br> |
| *Leq correspondiente a la hora más ruidosa relacionada a actividades de tránsito durante horas sensibles al ruido | *Leq correspondiente a la hora más ruidosa relacionada a actividades de tránsito durante horas sensibles al ruido | *Leq correspondiente a la hora más ruidosa relacionada a actividades de tránsito durante horas sensibles al ruido |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: _Federal Transit Administration_ . En la clasificación anterior se aprecia que las categorías presentan dos descriptores distintos, lo cual se debe a que las categorías 1 y 3 presentan un funcionamiento temporal acotado, poniendo énfasis al mayor nivel de presión -->
<!-- FIN TABLA 3 -->

Tabla 4: Definición de tipos de impacto según FTA. ...................................................................................................................................................8

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Respecto a la clasificación de impacto de ruido, la guía establece que el impacto severo amerita la implementación inmediata de alguna medida de control de ruido, mientras que el impacto moderado corresponde a una advertencia por la cual se señala que los niveles están próximos al límite del impacto severo. La siguiente tabla describe la clasificación de impacto de ruido dada por el estándar de la FTA. -->

**Tabla 4: Definición de tipos de impacto según FTA.****

| Clasificación del impacto | Definición |
| --- | --- |
| No existe impacto | La introducción del ruido del proyecto conlleva un incremento insignificante en el número de<br>personas altamente molestas. |
| Impacto moderado | El cambio en el nivel de ruido acumulado es notorio para la mayoría de las personas, pero no lo<br>suficientemente alto para producir una reacción adversa por parte de la comunidad. |
| Impacto severo | Un porcentaje significativo de personas estaría altamente molesto por el ruido introducido por el<br>proyecto. |

<!-- Estadísticas: 3 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: _Federal Transit Administration_ . E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO -->
<!-- FIN TABLA 4 -->

Tabla 5: Criterio de molestia a personas de vibraciones transmitidas por el suelo. ......................................................................................................10

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Los indicadores de evaluación para el criterio de molestia “General”, se presentan en la siguiente tabla y se establecen diferentes límites según tipos de usos de suelo, los cuales se clasifican en: altamente sensibles, residencial e institucional. -->

**Tabla 5: Criterio de molestia a personas de vibraciones transmitidas por el suelo.****

| Categoría uso de suelo | Nivel de impacto de vibraciones<br>([VdB] re 1 [μin/s]) | Col3 | Col4 |
| --- | --- | --- | --- |
| **Categoría uso de suelo** | **Eventos**<br>**frecuentes1 ** | **Eventos**<br>**ocasionales2 ** | **Eventos**<br>**infrecuentes3 ** |
| **Categoría 1:**<br>Edificios donde son esenciales bajos ambientes de vibración para operaciones<br>internas (Instrumental hospitalario, laboratorios de investigación, etc) | 654 | 654 | 654 |
| **Categoría 2:**<br>Residencias o edificaciones donde normalmente duerme gente. | 72 | 75 | 80 |
| **Categoría 3:**<br>Usos de suelo institucionales prioritariamente diurno (Escuelas, Iglesias, etc)<br> | 75 | 78 | 83 |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: FTA. Finalmente, la normativa no explicita límites admisibles para garantizar la no generación de daños sobre edificaciones como consecuencia de operaciones de transporte. No obstante, lo anterior sí establece un criterio de -->
<!-- FIN TABLA 5 -->

Tabla 6: Criterio de daño a estructuras para niveles generales de vibración. Extracto FTA. .........................................................................................11

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 10 máximos permitidos se indican en sistema norteamericano ([in/s]) y corresponden a los enunciados en la siguiente tabla: -->

**Tabla 6: Criterio de daño a estructuras para niveles generales de vibración. Extracto FTA.****

| Categoría de edificación | PPV [in/s] | Lv aproximado [VdB]a |
| --- | --- | --- |
| I. Concreto reforzado con madera o acero (sin enlucido) | 0.5 | 102 |
| II. Diseño de ingeniería de hormigón y mampostería | 0.3 | 98 |
| III. Madera y mampostería sin diseño de ingeniería | 0.2 | 94 |
| IV. Edificio muy susceptible al daño por vibraciones | 0.12 | 90 |
| a Velocidad RMS en decibeles [VdB] referencia 1 [μin/s.] | a Velocidad RMS en decibeles [VdB] referencia 1 [μin/s.] | a Velocidad RMS en decibeles [VdB] referencia 1 [μin/s.] |

<!-- Estadísticas: 5 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: FTA **4** **ÁREA DE ESTUDIO Y PUNTOS DE MEDICIÓN** -->
<!-- FIN TABLA 6 -->

Tabla 7: Ubicación y descripción de receptores........................................................................................................................................................15

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- M AKROPLAZA - R EV . B 14 -->

**Tabla 7: Ubicación y descripción de receptores.****

| Punto | Descripción | Altura del<br>receptor [m] | Uso efectivo | Coordenadas UTM | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Punto** | **Descripción** | **Altura del**<br>**receptor [m]** | **Uso efectivo** | **Datum WGS 84 Huso 19H** | **Datum WGS 84 Huso 19H** |
| **Punto** | **Descripción** | **Altura del**<br>**receptor [m]** | **Uso efectivo** | **Este** | **Norte** |
| 1 | Edificio Cumbre de 24 pisos, ubicado en Av. Edmundo Eluchans<br>1615. | 1,5 - 59 | Vivienda | 262.157 | 6.350.314 |
| 2 | Edificio Reñacamar II de 25 pisos, ubicado Av. Edmundo<br>Eluchans 1737.<br> | 1,5 - 61,5 | Vivienda | 262.155 | 6.350.381 |
| 3 | ~~Edificio Las Golondrinas de 26 pisos, ubicado en calle~~<br>Golondrinas 1731. | 1,5 - 64 | Vivienda | 262.298 | 6.350.417 |
| 4 | Portón de entrada a faena de construcción. | 1,5 | Construcción | 262.316 | 6.350.272 |
| 5 | Gasolinera Shell con strip center*. | 1,5 | Comercial | 262.209 | 6.350.423 |

<!-- Estadísticas: 7 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Nota: Coordenadas obtenidas en terreno. *Punto 5 se considera en particular, para evaluación de flujo vehicular en fases de construcción y operación del proyecto. A continuación, se presentan fotografías de los puntos de medición obtenidas en la campaña de línea de base. -->
<!-- FIN TABLA 7 -->

Tabla 8: Zonificación y máximos permitidos según el D.S. No 38/2011 del MMA. ........................................................................................................17

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- el D.S No38/2011 del MMA. En la Tabla 8 se presenta un resumen de las homologaciones y el máximo permitido según el D.S No 38/2011 del MMA: -->

**Tabla 8: Zonificación y máximos permitidos según el D.S. No 38/2011 del MMA.****

| Punto | Zona | Zonificación según<br>D.S. No38/2011 del MMA | NPC Máximo Permitido [dB(A)] | Col5 |
| --- | --- | --- | --- | --- |
| **Punto**<br> | **Zona**<br> | **Zonificación según**<br>**D.S. No38/2011 del MMA**<br> | ~~**Periodo diurno**~~<br> | ~~**Periodo nocturno**~~<br> |
| ~~1 y 2~~ | ~~E3~~ | ~~Zona II~~ | ~~60~~ | ~~45~~ |
| 3 y 4 | V4 | Zona II | 60 | 45 |

<!-- Estadísticas: 3 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **4.3.2** **Ruido - FTA Transit Noise and Vibration Impact Assessment Manual (Humanos)** De acuerdo con el procedimiento indicado por la FTA a partir de la medición horaria de _L_ _eq_ _[h]_ es posible obtener el _L_ _DN_, según las expresiones de cálculo descritas en el Capítulo 0, Ecuación 1 y 2. En la tabla siguiente se presentan -->
<!-- FIN TABLA 8 -->

Tabla 9: Estimación del nivel de ruido existente según descriptor L DN . .......................................................................................................................18

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- M AKROPLAZA - R EV . B 17 -->

**Tabla 9: Estimación del nivel de ruido existente según descriptor L** **DN** **.****

| Punto | Hora de medición<br>[hh:mm] | Nivel de ruido<br>existente<br>Leq [h] [dB(A)]* | Corrección, según<br>guía FTA [dB] | Nivel de ruido<br>existente LDN<br>[dB(A)] | Máximo “Sin<br>impacto” LDN<br>[dB(A)]** |
| --- | --- | --- | --- | --- | --- |
| **1 ** | 18:58 | 70 | +3 | 73 | 65 |
| **5 ** | 17:48 | 64 | -2 | 62 | 59 |

<!-- Estadísticas: 2 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- *Valor aproximado al entero más cercano. **Máximo de referencia para que el proyecto no genere impacto (No superación de la curva inferior Ilustración 1). En la Tabla 9, se observa que los valores de _L_ _DN_ para los puntos son 73 y 62 [dB(A)]. Estos resultados son la base -->
<!-- FIN TABLA 9 -->

Tabla 10: Niveles máximos de referencia según FTA. ..............................................................................................................................................18
Tabla 11: Resumen de entradas y salidas en el proceso de cálculo del modelo SoundPLAN. ......................................................................................19

<!-- INICIO TABLA 11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- por la baja atenuación de la propagación de la onda sonora debido a estos efectos meteorológicos. Además, la norma de cálculo utilizada considera siempre la velocidad del viento entre 1 y 5 [m/s] [4], en dirección desde las fuentes de ruido hacia los receptores, es decir, a favor de la propagación. De acuerdo con lo anterior, el escenario modelado representa una estacionalidad climática crítica. -->

**Tabla 11: Resumen de entradas y salidas en el proceso de cálculo del modelo SoundPLAN.****

| Col1 | Ítem | Col3 | Descripción |
| --- | --- | --- | --- |
| Entradas<br>(Input) | Topografía<br> | Topografía<br> | Cotas de terreno<br> |
| Entradas<br>(Input) | ~~Ubicación de fuentes de ruido~~<br> | ~~Ubicación de fuentes de ruido~~<br> | ~~Puntos, áreas o líneas de emisión~~<br> |
| Entradas<br>(Input) | ~~Ubicación de receptores~~<br> | ~~Ubicación de receptores~~<br> | ~~Puntos de evaluación~~<br> |
| Entradas<br>(Input) | Obstáculos | ~~Existentes~~<br> | ~~Cotas de Terreno~~<br> |
| Entradas<br>(Input) | Obstáculos | ~~Introducidos~~ | ~~- ~~ |
| Entradas<br>(Input) | Algoritmo de cálculo | Algoritmo de cálculo | ISO 9613, parte 1 y 2 |
| Salidas<br>(Output) | Niveles de Presión Sonora modelados | Niveles de Presión Sonora modelados | Mapas de propagación sonora |
| Salidas<br>(Output) | Niveles de Presión Sonora modelados | Niveles de Presión Sonora modelados | Niveles de Presión Sonora en puntos de inmisión (Receptores) |

<!-- Estadísticas: 8 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- La modelación incorporó la maquinaria de mayor emisión de ruido, con lo cual se garantiza que las emisiones sonoras provenientes de otras actividades (con maquinaria menor) quedarán enmascaradas por la emisión de las fuentes consideradas. -->
<!-- FIN TABLA 11 -->

Tabla 12: Resumen de entradas y salidas en el proceso de cálculo del modelo SoundPLAN. ......................................................................................19

<!-- INICIO TABLA 12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **5.1.2** **Flujo vehicular** El software de simulación computacional utilizado corresponde a SoundPLAN v8.2, el cual incorpora variables físicas del entorno y características acústicas de las fuentes sonoras. -->

**Tabla 12: Resumen de entradas y salidas en el proceso de cálculo del modelo SoundPLAN.****

| Col1 | Ítem | Descripción |
| --- | --- | --- |
| Entradas<br>(Input) | Topografía | Cotas de terreno |
| Entradas<br>(Input) | Ubicación de fuentes de ruido | Puntos, áreas o líneas de emisión |

<!-- Estadísticas: 2 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- 4 ISO 9613-2:1996, Meteorological conditions, page 3. E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO -->
<!-- FIN TABLA 12 -->

Tabla 13: Indicadores de vibración de distintas maquinarias, medidos a 25 [ft] de distancia.........................................................................................22
Tabla 14: Potencias acústicas de la maquinaria utilizada en fase de construcción. Fuentes a nivel de terreno. .............................................................25

<!-- INICIO TABLA 14 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Acústica SpA a maquinarias en proyectos similares. A continuación, en la siguiente tabla se detallan las potencias acústicas de las principales fuentes de ruido involucradas en las faenas de construcción: -->

**Tabla 14: Potencias acústicas de la maquinaria utilizada en fase de construcción. Fuentes a nivel de terreno.****

| Fuente | Cantidad | Lw en [dB(A)] en espectro de frecuencia [Hz] | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Lw [dB(A)]<br>c/u | Referencia |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | **Cantidad** | **63** | **125** | **250** | **500** | **1K** | **2k** | **4k** | **8k** | **8k** | **8k** |
| Torre Grúa | 4 | 84 | 89 | 99 | 101 | 94 | 95 | 85 | 77 | 104 | BS 5228 Tabla 4, N°48 |
| Camión Tolva | 8 | 82 | 88 | 92 | 95 | 97 | 95 | 92 | 85 | 102 | BS 5228 Tabla 2, N°33 |
| Camión Mixer | 5 | 82 | 83 | 84 | 97 | 99 | 101 | 97 | 83 | 105 | BS 5228 Tabla 4, N°21 |
| Bomba de hormigón | 2 | 86 | 88 | 89 | 96 | 101 | 102 | 95 | 85 | 106 | BS 5228 Tabla 3, N°25 |
| Minicargador | 1 | 73 | 83 | 85 | 84 | 87 | 87 | 83 | 75 | 93 | BS 5228 Tabla 4, N°68 |
| Excavadora | 2 | 79 | 97 | 89 | 98 | 98 | 97 | 92 | 84 | 104 | BS 5228 Tabla 2, N°15 |
| Montacargas | 1 | 87 | 91 | 88 | 92 | 92 | 91 | 85 | 74 | 99 | BS 5228 Tabla 2, N°35 |
| Rodillo Compactador | 1 | 82 | 87 | 96 | 97 | 95 | 91 | 83 | 73 | 102 | BS 5228 Tabla 2, N°38 |
| **TOTAL - FOCO DE RUIDO** | **TOTAL - FOCO DE RUIDO** | **97** | **104** | **107** | **111** | **111** | **112** | **107** | **97** | **117** |  |

<!-- Estadísticas: 10 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 15: Potencias acústicas de la maquinaria utilizada en fase de construcción. Fuentes en altura.** |Fuente|Cantidad|Lw en [dB(A)] en espectro de frecuencia [Hz]|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Lw [dB(A)]<br>c/u|Referencia| |---|---|---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 14 -->

Tabla 15: Potencias acústicas de la maquinaria utilizada en fase de construcción. Fuentes en altura. ..........................................................................25

<!-- INICIO TABLA 15 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Excavadora|2|79|97|89|98|98|97|92|84|104|BS 5228 Tabla 2, N°15| |Montacargas|1|87|91|88|92|92|91|85|74|99|BS 5228 Tabla 2, N°35| |Rodillo Compactador|1|82|87|96|97|95|91|83|73|102|BS 5228 Tabla 2, N°38| |**TOTAL - FOCO DE RUIDO**|**TOTAL - FOCO DE RUIDO**|**97**|**104**|**107**|**111**|**111**|**112**|**107**|**97**|**117**|| -->

**Tabla 15: Potencias acústicas de la maquinaria utilizada en fase de construcción. Fuentes en altura.****

| Fuente | Cantidad | Lw en [dB(A)] en espectro de frecuencia [Hz] | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Lw [dB(A)]<br>c/u | Referencia |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | **Cantidad** | **63** | **125** | **250** | **500** | **1K** | **2k** | **4k** | **8k** | **8k** | **8k** |
| Martillo demoledor | 1 | 85 | 95 | 100 | 99 | 101 | 105 | 107 | 104 | 111 | BS 5228 Tabla 1, No 6 |
| Allanadora de concreto | 1 | 71 | 84 | 94 | 102 | 105 | 106 | 100 | 90 | 110 | Ficha técnica* |
| **TOTAL - FOCO DE RUIDO** | **TOTAL - FOCO DE RUIDO** | **85** | **95** | **101** | **104** | **106** | **109** | **108** | **104** | **114** |  |

<!-- Estadísticas: 4 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- *Ver Anexo I. E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO -->
<!-- FIN TABLA 15 -->

Tabla 16: Evaluación preliminar de cumplimiento D.S. No38/2011 del MMA. Fase de construcción. Periodo diurno. Escenario 1. ...................................31

<!-- INICIO TABLA 16 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- M AKROPLAZA - R EV . B 30 -->

**Tabla 16: Evaluación preliminar de cumplimiento D.S. No38/2011 del MMA. Fase de construcción. Periodo diurno. Escenario 1.****

| Punto | Piso | NPSeq proyectado, en<br>[dB(A)]* | Máximo permitido<br>Periodo diurno [dB(A)] | Evaluación |
| --- | --- | --- | --- | --- |
| 1 | 1 | 70 | 60 | Supera en 10 [dB] |
| 1 | 2 | 70 | 60 | Supera en 10 [dB] |
| 1 | 3 | 70 | 60 | Supera en 10 [dB] |
| 1 | 4 | 70 | 60 | Supera en 10 [dB] |
| 1 | 5 | 70 | 60 | Supera en 10 [dB] |
| 1 | 6 | 70 | 60 | Supera en 10 [dB] |
| 1 | 7 | 70 | 60 | Supera en 10 [dB] |
| 1 | 8 | 70 | 60 | Supera en 10 [dB] |
| 1 | 9 | 69 | 60 | Supera en 9 [dB] |
| 1 | 10 | 69 | 60 | Supera en 9 [dB] |
| 1 | 11 | 69 | 60 | Supera en 9 [dB] |
| 1 | 12 | 69 | 60 | Supera en 9 [dB] |
| 1 | 13 | 69 | 60 | Supera en 9 [dB] |
| 1 | 14 | 68 | 60 | Supera en 8 [dB] |
| 1 | 15 | 68 | 60 | Supera en 8 [dB] |
| 1 | 16 | 68 | 60 | Supera en 8 [dB] |
| 1 | 17 | 68 | 60 | Supera en 8 [dB] |
| 1 | 18 | 67 | 60 | Supera en 7 [dB] |
| 1 <br> | 19<br> | 67<br> | 60<br> | Supera en 7 [dB]<br> |
| ~~1 ~~<br> | ~~20~~<br> | ~~67~~<br> | ~~60~~<br> | ~~Supera en 7 [dB]~~<br> |
| ~~1 ~~<br> | ~~21~~<br> | ~~67~~<br> | ~~60~~<br> | ~~Supera en 7 [dB]~~<br> |
| ~~1 ~~<br> | ~~22~~<br> | ~~67~~<br> | ~~60~~<br> | ~~Supera en 7 [dB]~~<br> |
| ~~1 ~~<br> | ~~23~~<br> | ~~66~~<br> | ~~60~~<br> | ~~Supera en 6 [dB]~~<br> |
| ~~1 ~~<br> | ~~24~~<br> | ~~66~~<br> | ~~60~~<br> | ~~Supera en 6 [dB]~~<br> |
| ~~2 ~~<br> | ~~1 ~~<br> | ~~66~~<br> | ~~60~~<br> | ~~Supera en 6 [dB]~~<br> |
| ~~2 ~~<br> | ~~2 ~~<br> | ~~67~~<br> | ~~60~~<br> | ~~Supera en 7 [dB]~~<br> |
| ~~2 ~~<br> | ~~3 ~~<br> | ~~67~~<br> | ~~60~~<br> | ~~Supera en 7 [dB]~~<br> |
| ~~2 ~~<br> | ~~4 ~~<br> | ~~68~~<br> | ~~60~~<br> | ~~Supera en 8 [dB]~~<br> |
| ~~2 ~~ | ~~5 ~~ | ~~68~~ | ~~60~~ | ~~Supera en 8 [dB]~~ |
| 2 | 6 | 68 | 60 | Supera en 8 [dB] |
| 2 | 7 | 68 | 60 | Supera en 8 [dB] |
| 2 | 8 | 68 | 60 | Supera en 8 [dB] |
| 2 | 9 | 68 | 60 | Supera en 8 [dB] |
| 2 | 10 | 68 | 60 | Supera en 8 [dB] |
| 2 | 11 | 68 | 60 | Supera en 8 [dB] |
| 2 | 12 | 67 | 60 | Supera en 7 [dB] |
| 2 | 13 | 67 | 60 | Supera en 7 [dB] |
| 2 | 14 | 67 | 60 | Supera en 7 [dB] |
| 2 | 15 | 67 | 60 | Supera en 7 [dB] |
| 2 | 16 | 67 | 60 | Supera en 7 [dB] |
| 2 | 17 | 67 | 60 | Supera en 7 [dB] |
| 2 | 18 | 67 | 60 | Supera en 7 [dB] |
| 2 | 19 | 66 | 60 | Supera en 6 [dB] |
| 2 | 20 | 66 | 60 | Supera en 6 [dB] |
| 2 | 21 | 66 | 60 | Supera en 6 [dB] |
| 2 | 22 | 66 | 60 | Supera en 6 [dB] |

<!-- Estadísticas: 46 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO M AKROPLAZA - R EV . B -->
<!-- FIN TABLA 16 -->

Tabla 17: Evaluación preliminar de cumplimiento D.S. No38/2011 del MMA. Fase de construcción. Periodo diurno. Escenario 2. ...................................33

<!-- INICIO TABLA 17 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Ilustración 12: Mapa de propagación sonora según NPSeq en [dB(A)]. Fase de construcción. Escenario 2.** Elaboración: Gerard Ingeniería Acústica SpA 2022. Nota: En mapa de ruido se presenta el piso del receptor con mayor nivel de inmisión de ruido. -->

**Tabla 17: Evaluación preliminar de cumplimiento D.S. No38/2011 del MMA. Fase de construcción. Periodo diurno. Escenario 2.****

| Punto | Piso | NPSeq proyectado, en<br>[dB(A)]* | Máximo permitido<br>Periodo diurno [dB(A)] | Evaluación |
| --- | --- | --- | --- | --- |
| 1 | 1 | 76 | 60 | Supera en 16 [dB] |
| 1 | 2 | 76 | 60 | Supera en 16 [dB] |
| 1 | 3 | 76 | 60 | Supera en 16 [dB] |
| 1 <br> | 4 <br> | 76<br> | 60<br> | Supera en 16 [dB]<br> |
| ~~1 ~~<br> | ~~5 ~~<br> | ~~76~~<br> | ~~60~~<br> | ~~Supera en 16 [dB]~~<br> |
| ~~1 ~~<br> | ~~6 ~~<br> | ~~76~~<br> | ~~60~~<br> | ~~Supera en 16 [dB]~~<br> |
| ~~1 ~~<br> | ~~7 ~~<br> | ~~76~~<br> | ~~60~~<br> | ~~Supera en 16 [dB]~~<br> |
| ~~1 ~~<br> | ~~8 ~~<br> | ~~76~~<br> | ~~60~~<br> | ~~Supera en 16 [dB]~~<br> |
| ~~1 ~~<br> | ~~9 ~~<br> | ~~76~~<br> | ~~60~~<br> | ~~Supera en 16 [dB]~~<br> |
| ~~1 ~~<br> | ~~10~~<br> | ~~76~~<br> | ~~60~~<br> | ~~Supera en 16 [dB]~~<br> |
| ~~1 ~~ | ~~11~~ | ~~76~~ | ~~60~~ | ~~Supera en 16 [dB]~~ |

<!-- Estadísticas: 11 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO M AKROPLAZA - R EV . B -->
<!-- FIN TABLA 17 -->

Tabla 18: Evaluación preliminar de cumplimiento. Fase de construcción. Periodo diurno. Flujo vehicular......................................................................37

<!-- INICIO TABLA 18 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- M AKROPLAZA - R EV . B 36 -->

**Tabla 18: Evaluación preliminar de cumplimiento. Fase de construcción. Periodo diurno. Flujo vehicular****

| Receptor | Piso | Nivel de Presión<br>Proyectado [dB(A)] | Valor límite de inmisión<br>Periodo diurno [dB(A)]* | Evaluación |
| --- | --- | --- | --- | --- |
| 1 | 1 | 52 | 65 | No supera |
| 1 | 2 | 53 | 65 | No supera |
| 1 | 3 | 54 | 65 | No supera |
| 1 | 4 | 53 | 65 | No supera |
| 1 | 5 | 53 | 65 | No supera |
| 1 | 6 | 53 | 65 | No supera |
| 1 | 7 | 53 | 65 | No supera |
| 1 | 8 | 52 | 65 | No supera |
| 1 | 9 | 52 | 65 | No supera |
| 1 | 10 | 52 | 65 | No supera |
| 1 | 11 | 51 | 65 | No supera |
| 1 | 12 | 51 | 65 | No supera |
| 1 | 13 | 51 | 65 | No supera |
| 1 | 14 | 51 | 65 | No supera |
| 1 | 15 | 50 | 65 | No supera |
| 1 | 16 | 50 | 65 | No supera |
| 1 | 17 | 50 | 65 | No supera |
| 1 | 18 | 49 | 65 | No supera |
| 1 | 19 | 49 | 65 | No supera |
| 1 | 20 | 49 | 65 | No supera |
| 1 | 21 | 49 | 65 | No supera |
| 1 | 22 | 48 | 65 | No supera |
| 1 | 23 | 48 | 65 | No supera |
| 1 | 24 | 48 | 65 | No supera |
| 5 | 1 | 56 | 59 | No supera |

<!-- Estadísticas: 25 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- *Valores aproximados al entero más cercano. De acuerdo con la evaluación presentada no se supera el estándar aplicado en todos los puntos de evaluación para el flujo vehicular en fase de construcción. -->
<!-- FIN TABLA 18 -->

Tabla 19: Proyección de L V y PPV en cada receptor. Vibraciones generadas por maquinaria pesada...........................................................................38

<!-- INICIO TABLA 19 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la siguiente tabla se presentan los resultados de las proyecciones vibratorias (PPV) realizadas para todos los puntos de evaluación de acuerdo con la metodología detallada en el capítulo 5.2. Posteriormente se indica la evaluación para el criterio de daño y molestia, cuyos niveles máximos permitidos se indicaron en el acápite 0. -->

**Tabla 19: Proyección de L** **V** **y PPV en cada receptor. Vibraciones generadas por maquinaria pesada.****

| Punto | Faena o maquinaria más cercana | Distancia<br>[m] | Distancia<br>[ft] | PPV proyectado<br>[in/s] | Lv proyectado<br>[VdB] |
| --- | --- | --- | --- | --- | --- |
| ~~1 ~~<br> | ~~Rodillo vibratorio~~<br> | ~~28~~<br> | ~~92~~<br> | ~~0,03~~<br> | ~~77~~<br> |
| ~~2 ~~<br> | ~~Rodillo vibratorio~~<br> | ~~50~~<br> | ~~164~~<br> | ~~0,01~~<br> | ~~69~~<br> |
| ~~3 ~~<br> | ~~Rodillo vibratorio~~<br> | ~~47~~<br> | ~~154~~<br> | ~~0,01~~<br> | ~~70~~<br> |
| ~~4 ~~ | ~~Rodillo vibratorio~~ | ~~61~~ | ~~200~~ | ~~ < 0,01~~ | ~~67~~ |

<!-- Estadísticas: 4 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- **Criterio de daño** **Tabla 20: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de daño.** -->
<!-- FIN TABLA 19 -->

Tabla 20: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de daño. ....................................................................38

<!-- INICIO TABLA 20 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |~~3 ~~<br>|~~Rodillo vibratorio~~<br>|~~47~~<br>|~~154~~<br>|~~0,01~~<br>|~~70~~<br>| |~~4 ~~|~~Rodillo vibratorio~~|~~61~~|~~200~~|~~ < 0,01~~|~~67~~| **Criterio de daño** -->

**Tabla 20: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de daño.****

| Punto | PPV proyectado [in/s] | PPV Máximo permitido [in/s] | Observación |
| --- | --- | --- | --- |
| 1 | 0,03 <br> | 0,2 | Cumple |
| 2 | 0,01 <br> | 0,2 | Cumple |
| 3 | 0,01 <br> | 0,2 | Cumple |
| 4 | < 0,01 | 0,2 | Cumple |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Criterio de molestia** **Tabla 21: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de molestia.** -->
<!-- FIN TABLA 20 -->

Tabla 21: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de molestia. ...............................................................38

<!-- INICIO TABLA 21 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |3|0,01 <br>|0,2|Cumple| |4|< 0,01|0,2|Cumple| **Criterio de molestia** -->

**Tabla 21: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de molestia.****

| Punto | LV proyectado [VdB] | LV Máximo permitido [VdB] | Observación |
| --- | --- | --- | --- |
| 1 | 77 | 72 | No Cumple |
| 2 | 69 | 72 | Cumple |
| 3 | 70 | 72 | Cumple |
| 4 | 67 | 72 | Cumple |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- En las tablas anteriores se puede apreciar que los valores proyectados para la construcción del Proyecto en PPV se encuentran por debajo de los máximos recomendados por la guía para el criterio de daño, pero para el criterio de molestia es posible apreciar que en el punto 1 preliminarmente se superan los límites establecidos. Por este motivo, en el capítulo 8 se presentan medidas de control a incorporar en el Proyecto. -->
<!-- FIN TABLA 21 -->

Tabla 22: Características barreras acústicas propuesta para la fase de construcción. .................................................................................................39
Tabla 23: Pérdida de transmisión del elemento divisorio. OSB e.: 18 [mm]. ................................................................................................................42
Tabla 24: Evaluación preliminar de cumplimiento D.S. No38/2011 del MMA. Fase de construcción. Periodo diurno. Escenario 1. ...................................45

<!-- INICIO TABLA 24 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- M AKROPLAZA - R EV . B 44 -->

**Tabla 24: Evaluación preliminar de cumplimiento D.S. No38/2011 del MMA. Fase de construcción. Periodo diurno. Escenario 1.****

| Punto | Piso | NPSeq proyectado, en<br>[dB(A)]* | Máximo permitido<br>Periodo diurno [dB(A)] | Evaluación |
| --- | --- | --- | --- | --- |
| 1 | 1 | 55 | 60 | Cumple |
| 1 | 2 | 56 | 60 | Cumple |
| 1 | 3 | 56 | 60 | Cumple |
| 1 | 4 | 57 | 60 | Cumple |
| 1 | 5 | 57 | 60 | Cumple |
| 1 | 6 | 57 | 60 | Cumple |
| 1 | 7 | 57 | 60 | Cumple |
| 1 | 8 | 57 | 60 | Cumple |
| 1 | 9 | 56 | 60 | Cumple |
| 1 | 10 | 56 | 60 | Cumple |
| 1 | 11 | 56 | 60 | Cumple |
| 1 | 12 | 56 | 60 | Cumple |
| 1 | 13 | 56 | 60 | Cumple |
| 1 | 14 | 56 | 60 | Cumple |
| 1 | 15 | 56 | 60 | Cumple |
| 1 | 16 | 55 | 60 | Cumple |
| 1 | 17 | 55 | 60 | Cumple |
| 1 | 18 | 55 | 60 | Cumple |
| 1 <br> | 19<br> | 55<br> | 60<br> | Cumple<br> |
| ~~1 ~~<br> | ~~20~~<br> | ~~55~~<br> | ~~60~~<br> | ~~Cumple~~<br> |
| ~~1 ~~<br> | ~~21~~<br> | ~~54~~<br> | ~~60~~<br> | ~~Cumple~~<br> |
| ~~1 ~~<br> | ~~22~~<br> | ~~54~~<br> | ~~60~~<br> | ~~Cumple~~<br> |
| ~~1 ~~<br> | ~~23~~<br> | ~~54~~<br> | ~~60~~<br> | ~~Cumple~~<br> |
| ~~1 ~~<br> | ~~24~~<br> | ~~54~~<br> | ~~60~~<br> | ~~Cumple~~<br> |
| ~~2 ~~<br> | ~~1 ~~<br> | ~~52~~<br> | ~~60~~<br> | ~~Cumple~~<br> |
| ~~2 ~~<br> | ~~2 ~~<br> | ~~53~~<br> | ~~60~~<br> | ~~Cumple~~<br> |
| ~~2 ~~<br> | ~~3 ~~<br> | ~~53~~<br> | ~~60~~<br> | ~~Cumple~~<br> |
| ~~2 ~~<br> | ~~4 ~~<br> | ~~53~~<br> | ~~60~~<br> | ~~Cumple~~<br> |
| ~~2 ~~ | ~~5 ~~ | ~~54~~ | ~~60~~ | ~~Cumple~~ |
| 2 | 6 | 54 | 60 | Cumple |
| 2 | 7 | 54 | 60 | Cumple |
| 2 | 8 | 54 | 60 | Cumple |
| 2 | 9 | 54 | 60 | Cumple |
| 2 | 10 | 54 | 60 | Cumple |
| 2 | 11 | 54 | 60 | Cumple |
| 2 | 12 | 54 | 60 | Cumple |
| 2 | 13 | 54 | 60 | Cumple |
| 2 | 14 | 54 | 60 | Cumple |
| 2 | 15 | 54 | 60 | Cumple |
| 2 | 16 | 54 | 60 | Cumple |
| 2 | 17 | 54 | 60 | Cumple |
| 2 | 18 | 54 | 60 | Cumple |
| 2 | 19 | 54 | 60 | Cumple |
| 2 | 20 | 54 | 60 | Cumple |
| 2 | 21 | 53 | 60 | Cumple |
| 2 | 22 | 53 | 60 | Cumple |

<!-- Estadísticas: 46 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO M AKROPLAZA - R EV . B -->
<!-- FIN TABLA 24 -->

Tabla 25: Evaluación preliminar de cumplimiento D.S. No38/2011 del MMA. Fase de construcción. Periodo diurno. Escenario 2. ...................................48

<!-- INICIO TABLA 25 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- M AKROPLAZA - R EV . B 47 -->

**Tabla 25: Evaluación preliminar de cumplimiento D.S. No38/2011 del MMA. Fase de construcción. Periodo diurno. Escenario 2.****

| Punto | Piso | NPSeq proyectado, en<br>[dB(A)]* | Máximo permitido<br>Periodo diurno [dB(A)] | Evaluación |
| --- | --- | --- | --- | --- |
| 1 | 1 | 55 | 60 | No supera |
| 1 | 2 | 56 | 60 | No supera |
| 1 | 3 | 56 | 60 | No supera |
| 1 | 4 | 57 | 60 | No supera |
| 1 | 5 | 57 | 60 | No supera |
| 1 | 6 | 57 | 60 | No supera |
| 1 | 7 | 57 | 60 | No supera |
| 1 | 8 | 57 | 60 | No supera |
| 1 | 9 | 56 | 60 | No supera |
| 1 | 10 | 56 | 60 | No supera |
| 1 | 11 | 56 | 60 | No supera |
| 1 | 12 | 56 | 60 | No supera |
| 1 | 13 | 56 | 60 | No supera |
| 1 | 14 | 56 | 60 | No supera |
| 1 | 15 | 56 | 60 | No supera |
| 1 | 16 | 55 | 60 | No supera |
| 1 | 17 | 55 | 60 | No supera |
| 1 | 18 | 55 | 60 | No supera |
| 1 <br> | 19<br> | 55<br> | 60<br> | No supera<br> |
| ~~1 ~~<br> | ~~20~~<br> | ~~55~~<br> | ~~60~~<br> | ~~No supera~~<br> |
| ~~1 ~~<br> | ~~21~~<br> | ~~54~~<br> | ~~60~~<br> | ~~No supera~~<br> |
| ~~1 ~~<br> | ~~22~~<br> | ~~54~~<br> | ~~60~~<br> | ~~No supera~~<br> |
| ~~1 ~~<br> | ~~23~~<br> | ~~54~~<br> | ~~60~~<br> | ~~No supera~~<br> |
| ~~1 ~~<br> | ~~24~~<br> | ~~54~~<br> | ~~60~~<br> | ~~No supera~~<br> |
| ~~2 ~~<br> | ~~1 ~~<br> | ~~52~~<br> | ~~60~~<br> | ~~No supera~~<br> |
| ~~2 ~~<br> | ~~2 ~~<br> | ~~53~~<br> | ~~60~~<br> | ~~No supera~~<br> |
| ~~2 ~~<br> | ~~3 ~~<br> | ~~53~~<br> | ~~60~~<br> | ~~No supera~~<br> |
| ~~2 ~~<br> | ~~4 ~~<br> | ~~53~~<br> | ~~60~~<br> | ~~No supera~~<br> |
| ~~2 ~~ | ~~5 ~~ | ~~54~~ | ~~60~~ | ~~No supera~~ |
| 2 | 6 | 54 | 60 | No supera |
| 2 | 7 | 54 | 60 | No supera |
| 2 | 8 | 54 | 60 | No supera |
| 2 | 9 | 54 | 60 | No supera |
| 2 | 10 | 54 | 60 | No supera |
| 2 | 11 | 54 | 60 | No supera |
| 2 | 12 | 54 | 60 | No supera |
| 2 | 13 | 54 | 60 | No supera |
| 2 | 14 | 54 | 60 | No supera |
| 2 | 15 | 54 | 60 | No supera |
| 2 | 16 | 54 | 60 | No supera |
| 2 | 17 | 54 | 60 | No supera |
| 2 | 18 | 54 | 60 | No supera |
| 2 | 19 | 54 | 60 | No supera |
| 2 | 20 | 54 | 60 | No supera |
| 2 | 21 | 53 | 60 | No supera |
| 2 | 22 | 53 | 60 | No supera |

<!-- Estadísticas: 46 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO M AKROPLAZA - R EV . B -->
<!-- FIN TABLA 25 -->

Tabla 26: Proyección de L V y PPV en cada receptor. Vibraciones generadas por maquinaria pesada...........................................................................50

<!-- INICIO TABLA 26 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **9.2** **Vibraciones** A continuación, se presenta la evaluación de vibraciones al implementar el buffer de seguridad señalado en el Capítulo 8.2.1 como medida de control. -->

**Tabla 26: Proyección de L** **V** **y PPV en cada receptor. Vibraciones generadas por maquinaria pesada.****

| Punto | Faena o maquinaria más cercana | Distancia<br>[m] | Distancia<br>[ft] | PPV proyectado<br>[in/s] | Lv proyectado<br>[VdB] |
| --- | --- | --- | --- | --- | --- |
| 1 | Rodillo vibratorio | 40 | 131 | 0,02 | 72 |
| 2 | Rodillo vibratorio | 50 | 164 | 0,01 | 69 |
| 3 | Rodillo vibratorio | 47 | 154 | 0,01 | 70 |
| 4 | Rodillo vibratorio | 61 | 200 | < 0,01 | 67 |

<!-- Estadísticas: 4 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- **Criterio de daño** **Tabla 27: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de daño.** -->
<!-- FIN TABLA 26 -->

Tabla 27: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de daño. ....................................................................50

<!-- INICIO TABLA 27 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |3|Rodillo vibratorio|47|154|0,01|70| |4|Rodillo vibratorio|61|200|< 0,01|67| **Criterio de daño** -->

**Tabla 27: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de daño.****

| Punto | PPV proyectado [in/s] | PPV Máximo permitido [in/s] | Observación |
| --- | --- | --- | --- |
| ~~1 ~~<br> | ~~0,02 ~~<br> | ~~0,2~~<br> | ~~Cumple~~<br> |
| ~~2 ~~<br> | ~~0,01 ~~<br> | ~~0,2~~<br> | ~~Cumple~~<br> |
| ~~3 ~~<br> | ~~0,01 ~~<br> | ~~0,2~~<br> | ~~Cumple~~<br> |
| ~~4 ~~ | ~~ < 0,01 ~~ | ~~0,2~~ | ~~Cumple~~ |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Criterio de molestia** **Tabla 28: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de molestia.** -->
<!-- FIN TABLA 27 -->

Tabla 28: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de molestia. ...............................................................50

<!-- INICIO TABLA 28 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |~~3 ~~<br>|~~0,01 ~~<br>|~~0,2~~<br>|~~Cumple~~<br>| |~~4 ~~|~~ < 0,01 ~~|~~0,2~~|~~Cumple~~| **Criterio de molestia** -->

**Tabla 28: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de molestia.****

| Punto | LV proyectado [VdB] | LV Máximo permitido [VdB] | Observación |
| --- | --- | --- | --- |
| 1 | 72 | 72 | Cumple |
| 2 | 69 | 72 | Cumple |
| 3 | 70 | 72 | Cumple |
| 4 | 67 | 72 | Cumple |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- En las tablas anteriores se puede apreciar que los valores proyectados para la construcción del proyecto se encuentran por debajo de los máximos recomendados por la normativa tanto para el criterio de daño como el de molestia para todos los puntos al incorporar la medida de control de vibraciones. -->
<!-- FIN TABLA 28 -->

Tabla 29: Nivel de potencia acústica motor eléctrico 9 [HP].......................................................................................................................................59

<!-- INICIO TABLA 29 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 58 El espectro de potencia del equipo se obtiene mediante cálculo en software ENC 4.1 (Tabla 29, Ilustración 20) considerando un motor eléctrico de 9 [HP] (6,7 [kW]) a 3.600 R.P.M. -->

**Tabla 29: Nivel de potencia acústica motor eléctrico 9 [HP].****

| Fuente | Lw [dB(A)] en bandas de octava de frecuencia [Hz] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Lw<br>[dB(A)] | Fuente |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | **63** | **125** | **250** | **500** | **1k** | **2k** | **4k** | **8K** | **8K** | **8K** |
| Motor Eléctrico 9 [HP] | 52,1 | 65,2 | 74,7 | 83,1 | 86,3 | 86,5 | 81,3 | 71,2 | **91,0** | Software ENC 4.1 |

<!-- Estadísticas: 2 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- 9 [HP] = 6,7 [kW] **Ilustración 20: Software ENC 4.1. Cálculo potencia acústica motor eléctrico 9 [HP]** -->
<!-- FIN TABLA 29 -->

Tabla 30: Nivel de potencia acústica allanadora de pavimento. .................................................................................................................................59

<!-- INICIO TABLA 30 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Se puede observar que la diferencia entre el Lw de la Tabla 29 y el valor en ficha técnica (Ilustración 19) es de 19 [dB(A)], el cual es sumado a cada banda de frecuencia, con el fin de ajustar la curva al Lw esperado (110 [dB(A)]). De esta forma, el nivel de potencia acústica de la allanadora de pavimento se presenta en la Tabla 30. -->

**Tabla 30: Nivel de potencia acústica allanadora de pavimento.****

| Fuente | Lw [dB(A)] en bandas de octava de frecuencia [Hz] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Lw<br>[dB(A)] | Fuente |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | **63** | **125** | **250** | **500** | **1k** | **2k** | **4k** | **8K** | **8K** | **8K** |
| Allanadora de pavimento | 71,1 | 84,2 | 93,7 | 102,1 | 105,3 | 105,5 | 100,3 | 90,2 | **110** | Ficha técnica |

<!-- Estadísticas: 2 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO M AKROPLAZA - R EV . B -->
<!-- FIN TABLA 30 -->


E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

3

**1** **INTRODUCCIÓN**

El presente documento, elaborado por Gerard Ingeniería Acústica SpA contiene la proyección y evaluación de ruido
y vibraciones del proyecto _“Makroplaza”_, (en adelante “Proyecto”), el cual se ubicará en la comuna de Viña del Mar,
Región de Valparaíso. Este tiene por finalidad evaluar los niveles de ruido y vibraciones del proyecto en los sectores
que pueden verse afectados.

Las actividades involucradas en la fase de construcción del proyecto pueden generar un aumento del nivel de ruido
y vibración en los sectores aledaños. En este contexto, la definición del área de estudio se efectúa en base a la
existencia de lugares habitados, identificándose cinco (5) puntos representativos. Dos (2) de los puntos, además,
corresponden a eventual afectación por flujo vehicular.

Por otro lado, se efectuó la predicción de los niveles de ruido mediante un modelo asistido por software y, en el caso
de vibraciones, proyecciones a través de métodos de cálculo específicos, con lo que se obtiene la magnitud de las
emisiones acústicas y vibratorias en los puntos de evaluación definidos considerando las características del proyecto.

Los valores estimados son comparados con los máximos permitidos que establece la normativa nacional vigente o,
en caso de ausencia de ésta, estándares internacionales aplicables seleccionados para tal efecto, con la finalidad
de verificar su cumplimiento.

Finalmente, la evaluación se realizó bajo los lineamientos que indica la “Guía para la predicción y evaluación de
impactos por ruido y vibración en el SEIA, del Servicio de Evaluación Ambiental (SEA, 2019).

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

4

**2** **OBJETIVOS**

**2.1** **Objetivo general**

Evaluar el impacto acústico y vibratorio que podría generar el proyecto _,_ de acuerdo con los criterios de evaluación
establecidos en la normativa nacional vigente o, en caso de ausencia de ésta, estándares extranjeros aplicables.

**2.2** **Objetivos específicos**

 - Identificar receptores que pudiesen ser afectados producto de la emisión acústica y vibratoria del proyecto

en las fases de construcción.

 - Predecir el nivel de ruido que generarán las distintas actividades que contempla el proyecto, mediante un

modelo acústico asistido por software.

 - Efectuar proyecciones de velocidad vibratoria para las fases construcción del proyecto, mediante planillas

de cálculo.

 - Verificar el cumplimiento de los límites establecidos en la normativa nacional y en estándares internacionales

aplicables para las componentes ruido y vibraciones.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

5

**3** **NORMATIVAS Y GUÍA DE REFERENCIA**

**3.1** **Ruido de maquinaria e instalaciones**

**Decreto Supremo N°38/2011 del Ministerio del Medio Ambiente (D.S. N° 38/2011 del MMA)**

El objetivo de esta normativa es proteger la salud de la comunidad mediante el establecimiento de niveles máximos
de inmisión de ruido generados por las fuentes emisoras de ruido definidas en su Artículo N° 6, punto 13.

Los límites máximos permitidos por la normativa están asociados a la zonificación acorde con el Instrumento de
Planificación Territorial (IPT) respectivo. Los tipos de zonas se definen como:

**Tabla 1: Descripción de usos de suelo permitidos para cada tipo de zona según D.S. N° 38/2011 MMA.**

|Tipo de Zona|Descripción|
|---|---|
|Zona I|Aquella zona definida en el IPT respectivo y ubicada dentro del límite urbano, que permite exclusivamente<br>uso de suelo Residencial o bien este uso de suelo y alguno de los siguientes usos de suelo: Espacio Público<br>y/o Área Verde.|
|Zona II|Aquella zona definida en el IPT respectivo y ubicada dentro del límite urbano, que permite además los usos<br>de la Zona I, Equipamiento a cualquier escala.|
|Zona III|Aquella zona definida en el IPT respectivo y ubicada dentro del límite urbano, que permite además de los<br>usos de suelo de la Zona II, Actividades Productivas y/o de Infraestructura.<br>|
|Zona IV|~~Aquella zona definida en el IPT respectivo y ubicada dentro del límite urbano, que permite sólo usos de~~<br>suelo de Actividades Productivas y/o de Infraestructura.|
|Zona Rural|Aquella ubicada al exterior del límite urbano establecido en el Instrumento de Planificación Territorial<br>respectivo.|

Fuente: D.S. 38/2011 del MMA, artículo 6° numerales 28al 32.

Los Niveles de Presión Sonora Corregidos (NPC) que se obtengan no podrán exceder los valores de la siguiente
tabla:

**Tabla 2: Niveles máximos permisibles de NPC según D.S. N° 38/2011 del MMA.**

|Tipo de Zona|Nivel de Presión Sonora Corregido (NPC) Máximo Permitido [dB(A)]|Col3|
|---|---|---|
|**Tipo de Zona**|**Periodo Diurno**<br>**7:00 a 21:00 horas**|**Periodo Nocturno**<br>**21:00 a 7:00 horas**|
|Zona I|55|45|
|Zona II|60|45|
|Zona III|65|50|
|Zona IV|70|70|
|Zona Rural|Menor nivel entre el Nivel de Ruido de Fondo +10 [dB], y el NPC máximo permitido para Zona III|Menor nivel entre el Nivel de Ruido de Fondo +10 [dB], y el NPC máximo permitido para Zona III|

Fuente: D.S. 38/2011 del MMA, artículos 7° y 9°.

El criterio para zona rural se aplicará en periodo diurno y nocturno de manera independiente.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

6

**3.2** **Ruido flujo vehicular**

**FTA-VA--90-1003-06** **“Transit Noise and Vibration Assessment”**

Este manual de evaluación, de la Federal Transit Administration (FTA) de los Estados Unidos, regula los niveles de
ruido y vibración generados por los sistemas de transporte público y funcionamiento de maquinaria, estableciendo
criterios de daño para evaluar los niveles de ruido y vibración asociados al tránsito vehicular y ferroviario superficial
o subterráneo, y para evaluar los niveles de vibración asociados al funcionamiento de maquinaria durante actividades
constructivas.

Ante la ausencia de una normativa nacional que regule la emisión de ruido de fuentes móviles, se utilizará la guía de
referencia de la Administración Federal de Tránsito (FTA) de los Estados Unidos, que establece regulaciones y
políticas para el cuidado del medioambiente, de los posibles impactos que pudiesen causar los sistemas de
transporte. Entre dichas regulaciones se encuentran los niveles máximos de ruido para distintos medios de
transporte, tales como ferrocarriles, buses y automóviles.

_**Criterio de evaluación de ruido**_

En la siguiente ilustración se muestra el criterio de impacto de ruido ( _Noise Impact Criteria_ ) establecido por la FTA,
para las categorías de usos de suelo y para dos tipos de impactos del proyecto de transportes (moderado y severo),
considerando el nivel de ruido existente en las viviendas evaluadas y el incremento en los niveles de ruido por la
operación del proyecto.

**Ilustración 1: Tipo de impacto según incremento de los niveles y ruido existente.**

Fuente: _Federal Transit Administration_ .

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

7

Los criterios de impacto de ruido se basan en la comparación de los niveles de ruido exterior existentes y los niveles
de ruido exterior futuros generados por el Proyecto propuesto. Estos incorporan criterios absolutos, que consideran
el aporte de la actividad generada solo por la operación del proyecto.

La categoría del receptor y/o edificación evaluada se definen según el uso de suelo, como se detalla a continuación:

**Tabla 3: Categoría de uso de suelo y descriptor para criterio de impacto de ruido de tránsito vehicular.**

|Categoría según<br>uso de suelo|Unidad de<br>medida [dB(A)]|Descripción|
|---|---|---|
|1|Leq [h]*|Sectores donde bajos niveles de ruido sean indispensables para las actividades a desarrollar.<br>(Teatros, salas de concierto, estudios de grabación, entre otros)|
|2|LDN|Sectores con construcciones que la gente utiliza normalmente para dormir. (Viviendas,<br>hospitales y hoteles)|
|3 <br>|Leq [h]*<br>|Suelo institucional con uso principalmente diurno. Esta categoría incluye colegios, librerías,<br>teatros e iglesias, en donde es importante evitar interferencias con las actividades como el<br>habla, meditación y concentración en la lectura de material. Lugares para meditación o<br>asociados a estudio con cementerios, monumentos, museos, sector de camping y<br>recreacionales, pueden también ser considerados para estar en esta categoría. Sitios<br>históricos y parques pueden también ser considerados<br>|
|*Leq correspondiente a la hora más ruidosa relacionada a actividades de tránsito durante horas sensibles al ruido|*Leq correspondiente a la hora más ruidosa relacionada a actividades de tránsito durante horas sensibles al ruido|*Leq correspondiente a la hora más ruidosa relacionada a actividades de tránsito durante horas sensibles al ruido|

Fuente: _Federal Transit Administration_ .

En la clasificación anterior se aprecia que las categorías presentan dos descriptores distintos, lo cual se debe a que
las categorías 1 y 3 presentan un funcionamiento temporal acotado, poniendo énfasis al mayor nivel de presión
sonora obtenido por hora durante este periodo (en _L_ _eq_ _[h]_ ). En cambio, para la categoría 2, relacionada al uso
habitacional, se evalúa con relación al nivel día-noche ( _L_ _DN_ ), ya que este descriptor es tomado en consideración para
zonas donde el periodo nocturno en un factor sensible.

Respecto a la clasificación de impacto de ruido, la guía establece que el impacto severo amerita la implementación
inmediata de alguna medida de control de ruido, mientras que el impacto moderado corresponde a una advertencia
por la cual se señala que los niveles están próximos al límite del impacto severo. La siguiente tabla describe la
clasificación de impacto de ruido dada por el estándar de la FTA.

**Tabla 4: Definición de tipos de impacto según FTA.**

|Clasificación del impacto|Definición|
|---|---|
|No existe impacto|La introducción del ruido del proyecto conlleva un incremento insignificante en el número de<br>personas altamente molestas.|
|Impacto moderado|El cambio en el nivel de ruido acumulado es notorio para la mayoría de las personas, pero no lo<br>suficientemente alto para producir una reacción adversa por parte de la comunidad.|
|Impacto severo|Un porcentaje significativo de personas estaría altamente molesto por el ruido introducido por el<br>proyecto.|

Fuente: _Federal Transit Administration_ .

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

8

En particular, para la evaluación de ruido del presente Proyecto se considera los métodos expuestos por la versión
2018 de esta guía en cuanto a la evaluación del descriptor Nivel Día Noche ( _L_ _DN_ ) a partir de mediciones de Nivel
Continuo Equivalente ( _L_ _eq_ ).

De esta forma, el descriptor _L_ _DN_ puede determinarse a partir de la medición de _L_ _eq_ durante una hora del día y posterior
cálculo mediante las ecuaciones presentadas a continuación. Cabe señalar que este método presenta menor
precisión que el cálculo de _L_ _DN_ a partir de 3 mediciones de _L_ _eq_ durante el día, sin embargo, es útil para proyectos
que consideran varios puntos de medición para Evaluación General de Ruido. El método también puede ser
apropiado al determinar si un receptor de interés en particular representa a un grupo en un Análisis Detallado de
Ruido. Los siguientes procedimientos se aplican a esta opción de medición de duración parcial para _L_ _DN_ :

 - Medir el _L_ _eq_ _[h]_ para la hora más ruidosa de actividad relacionada con el proyecto, durante un periodo de

sensibilidad al ruido. Si no se selecciona esta hora, se pueden usar otras horas entendiendo que la
estimación es menos precisa.

 Posicionar el micrófono de medición en todos los sitios con orientación relativa al proyecto y las fuentes

ambientales. Colocar el micrófono en una ubicación que esté algo protegida de la fuente ambiental, para así
medir dicho ruido en el área más silenciosa de la propiedad.

 Realizar todas las mediciones de acuerdo con las buenas prácticas de ingeniería.

 - Convertir el _L_ _eq_ _[h]_ medido por hora a _L_ _DN_ con las siguientes ecuaciones según corresponda.

Para mediciones entre las 7 a.m. y las 7 p.m.:

L DN ≈ L eq −2 **Ecuación 1**

Para mediciones entre las 7 p.m. y las 10 p.m.:

L DN ≈ L eq + 3 **Ecuación 2**

Para mediciones entre las 10 p.m. y las 7 a.m.:

L DN ≈ L eq + 8 **Ecuación 3**

El valor del _L_ _DN_ resultante se subestimará moderadamente debido al uso de las constantes de ajuste en estas
ecuaciones. Esta subestimación está destinada a compensar la precisión reducida del _L_ _DN_ calculado. Si se usa este
método, se debe usar una duración de tiempo mínima de una hora para cada período de medición en el cálculo de
un _L_ _DN_ .

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

9

**3.3** **Vibraciones de maquinaria**

**FTA “Transit Noise and Vibration Assessment Manual”**

La Administración Federal de Tránsito (FTA) de los Estados Unidos, establece las regulaciones y políticas para el
cuidado del medioambiente, de los posibles impactos que pudiesen causar los sistemas de transporte. Entre dichas
regulaciones se encuentran los niveles máximos de ruido para distintos medios de transportes, tales como
ferrocarriles, buses y automóviles.

Para el caso de las vibraciones, esta norma identifica dos (2) tipos de impacto por vibraciones, el primero hace
referencia al criterio de molestia a personas, mientras que el segundo al criterio de daño a estructuras. El criterio de
“molestia”, está relacionado con los niveles de vibración transmitidos por suelo cuya influencia y percepción puedan
generar “molestia” en los humanos influenciados. Los indicadores de evaluación se basan en la velocidad de
vibración RMS, la cual ha mostrado una mejor correlación respecto a la sensibilidad de la vibración en el cuerpo
humano. Los niveles de velocidad de vibración (L v ) son expresados en unidades de decibeles [dB] referenciados a
1 [μin/s] o con una V antepuesta a dB [VdB]. En general, el umbral de perceptibilidad humana es 65 [VdB]. El criterio
de molestia a su vez se subdivide en un criterio “General” y un “Análisis detallado”. El criterio general de FTA,
considera la cantidad de eventos vibratorios diarios y los clasifica en eventos frecuentes, ocasionales e infrecuentes.

 - Se define “Eventos frecuentes”, cuando ocurren más de 70 eventos por día.

 - Se define “Eventos ocasionales”, cuando ocurren entre 30 y 70 eventos por día.

 - Se define “Eventos infrecuentes”, cuando ocurren menos de 30 eventos por día.

Los indicadores de evaluación para el criterio de molestia “General”, se presentan en la siguiente tabla y se
establecen diferentes límites según tipos de usos de suelo, los cuales se clasifican en: altamente sensibles,
residencial e institucional.

**Tabla 5: Criterio de molestia a personas de vibraciones transmitidas por el suelo.**

|Categoría uso de suelo|Nivel de impacto de vibraciones<br>([VdB] re 1 [μin/s])|Col3|Col4|
|---|---|---|---|
|**Categoría uso de suelo**|**Eventos**<br>**frecuentes1 **|**Eventos**<br>**ocasionales2 **|**Eventos**<br>**infrecuentes3 **|
|**Categoría 1:**<br>Edificios donde son esenciales bajos ambientes de vibración para operaciones<br>internas (Instrumental hospitalario, laboratorios de investigación, etc)|654|654|654|
|**Categoría 2:**<br>Residencias o edificaciones donde normalmente duerme gente.|72|75|80|
|**Categoría 3:**<br>Usos de suelo institucionales prioritariamente diurno (Escuelas, Iglesias, etc)<br>|75|78|83|

Fuente: FTA.

Finalmente, la normativa no explicita límites admisibles para garantizar la no generación de daños sobre
edificaciones como consecuencia de operaciones de transporte. No obstante, lo anterior sí establece un criterio de
evaluación para actividades de construcción asociadas a proyectos de infraestructura de transporte. Los valores

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

10

máximos permitidos se indican en sistema norteamericano ([in/s]) y corresponden a los enunciados en la siguiente
tabla:

**Tabla 6: Criterio de daño a estructuras para niveles generales de vibración. Extracto FTA.**

|Categoría de edificación|PPV [in/s]|Lv aproximado [VdB]a|
|---|---|---|
|I. Concreto reforzado con madera o acero (sin enlucido)|0.5|102|
|II. Diseño de ingeniería de hormigón y mampostería|0.3|98|
|III. Madera y mampostería sin diseño de ingeniería|0.2|94|
|IV. Edificio muy susceptible al daño por vibraciones|0.12|90|
|a Velocidad RMS en decibeles [VdB] referencia 1 [μin/s.]|a Velocidad RMS en decibeles [VdB] referencia 1 [μin/s.]|a Velocidad RMS en decibeles [VdB] referencia 1 [μin/s.]|

Fuente: FTA

**4** **ÁREA DE ESTUDIO Y PUNTOS DE MEDICIÓN**

**4.1** **Área de influencia (AI)**

**Ruido**

El área de influencia se establece en función de la existencia de asentamientos humanos que potencialmente pueden
ser afectados por un aumento en los niveles de presión sonora, de acuerdo con los máximos permitidos establecidos
por el D.S N°38/2011 del MMA.

El área considerada se determina realizando un cálculo simple de atenuación sonora debido a divergencia
geométrica (propagación por distancia), a partir de un nivel de emisión acústica máximo posible de las actividades
con maquinaria pesada que se desarrollará en el proyecto, representativas de la condición más crítica (mayor
emisión de ruido).

Por otro lado, y según lo indicado en la _“Guía para la predicción y evaluación de impactos de ruido y vibraciones en_
_el SEIA”_, para determinar el área de influencia del Proyecto y su entorno cercano, al emplazarse fuera de los límites
urbanos de acuerdo a los instrumentos de planificación territorial (IPT) aplicables, se consideró el menor ruido de
fondo registrado para periodo diurno, puesto que solo se contemplan obras de construcción para dicho periodo, el
nivel correspondiente es de 46 [dB(A)], perteneciente al punto 4.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

11

La fórmula de cálculo utilizada viene dada de la siguiente expresión:

Fuente puntual
NPS= NWS−20Log(r) −8 [dB(A)]

Dónde:

**(Ecuación 1)** **[1]**

NPS : Nivel de presión sonora en dB(A),
NWS : Nivel de potencia sonora en dB(A) y
r : Distancia entre la fuente y el receptor.

Tomando como referencia el nivel NWS (o L w ) del frente a nivel de terreno, con un nivel de potencia de 117 [dB(A)],
el nivel de 46 [dB(A)] se obtiene como resultado un área de extensión para una distancia fuente-receptor de 1.413

[m] desde el área del Proyecto.

Es importante destacar que todos los cálculos determinan la condición más crítica de propagación, no considerando
atenuación acústica debido a obstáculos topográficos, ni tampoco absorción de aire y suelo, como también considera
la totalidad de la potencia acústica en un punto, lo cual no ocurrirá en la realidad.

**Vibraciones**

En forma análoga, para la componente vibración se determinó que el área de influencia corresponde a la cual los
niveles proyectados se igualan a los niveles que caracterizan la situación previa al proyecto. Para el presente caso,
se considera el menor nivel obtenido en las mediciones de línea de base, el cual fue en el punto 4 para el periodo
nocturno, con un nivel Lv de 54,6 [VdB]. Para efectos de proyección se utilizó la expresión matemática que describe
la (Ecuación 2), definida por la normativa de referencia antes señalada.

L v ( D ) = L v ( 25 ft ) −30 ∙log 10
(

D

(Ecuación 2)
25 ~~[)]~~

Donde:

L v ( D ) : Es el nivel de velocidad en [VdB] proyectado en el receptor.
L v ( 25 ft ) : Es el nivel de velocidad de referencia en [VdB] medido a 25 [pies].
D : Distancia (en pies) entre el receptor y la fuente.

De esta forma, considerando el “Rodillo vibratorio” (94 [VdB] a 25 [ft] [2] de distancia), maquina utilizada para los
cálculos de impacto vibratorio del presente proyecto para faenas asociadas a la construcción; el AI asociada a la
componente vibración abarca una extensión de 157 [m] (cerca de 515 [ft]) alrededor de las actividades de Proyecto.

1 Samir N.Y Gerges. “Ruido, Fundamentos y Control”
2 Pie (del inglés _foot_ ).

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

12

A partir de lo anterior, el AI definido para los componentes ruido y vibración queda definida por el mayor de los
contornos anteriormente definidos, el cual está dado para ruido, y abarca un radio de 1.413 [m] alrededor de las
actividades de proyecto.

La siguiente ilustración presenta una gráfica de la extensión del AI antes definida, según los criterios presentados
anteriormente:

**Ilustración 2: Área de influencia. Vista general.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

13

**4.2** **Puntos de evaluación**

A continuación, en la Tabla 7 se presenta la ubicación y descripción de los puntos de medición de ruido y vibraciones,
los cuales fueron seleccionados de acuerdo con su cercanía con las futuras fuentes generadoras de ruido del
proyecto. Por su parte, en la Ilustración 3 se muestra la ubicación de los receptores en torno al emplazamiento del
proyecto.

**Ilustración 3: Ubicación de los puntos de evaluación. Vista general.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

14

**Tabla 7: Ubicación y descripción de receptores.**

|Punto|Descripción|Altura del<br>receptor [m]|Uso efectivo|Coordenadas UTM|Col6|
|---|---|---|---|---|---|
|**Punto**|**Descripción**|**Altura del**<br>**receptor [m]**|**Uso efectivo**|**Datum WGS 84 Huso 19H**|**Datum WGS 84 Huso 19H**|
|**Punto**|**Descripción**|**Altura del**<br>**receptor [m]**|**Uso efectivo**|**Este**|**Norte**|
|1|Edificio Cumbre de 24 pisos, ubicado en Av. Edmundo Eluchans<br>1615.|1,5 - 59|Vivienda|262.157|6.350.314|
|2|Edificio Reñacamar II de 25 pisos, ubicado Av. Edmundo<br>Eluchans 1737.<br>|1,5 - 61,5|Vivienda|262.155|6.350.381|
|3|~~Edificio Las Golondrinas de 26 pisos, ubicado en calle~~<br>Golondrinas 1731.|1,5 - 64|Vivienda|262.298|6.350.417|
|4|Portón de entrada a faena de construcción.|1,5|Construcción|262.316|6.350.272|
|5|Gasolinera Shell con strip center*.|1,5|Comercial|262.209|6.350.423|

Nota: Coordenadas obtenidas en terreno.
*Punto 5 se considera en particular, para evaluación de flujo vehicular en fases de construcción y operación del proyecto.

A continuación, se presentan fotografías de los puntos de medición obtenidas en la campaña de línea de base.

**Ilustración 4: Fotografías de los puntos de medición de ruido y vibraciones.**

|Punto 1 - Ruido|Punto 1 - Vibraciones|
|---|---|
|<br>**Punto 2 - Ruido**|<br>**Punto 2 - Vibraciones**|

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

15

|Punto 3 - Ruido|Punto 3 - Vibraciones|
|---|---|
|<br>**Punto 4 - Ruido**|<br>**Punto 4 - Vibraciones**|
|<br>**Punto 5 - Ruido FTA**|<br>**Punto 5 - Ruido FTA**|

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

16

**4.3** **Máximos permisibles**

**4.3.1** **Ruido - D.S. N° 38/2011 del MMA**

En el presente acápite se muestra la zonificación según el D.S No38/2011 del MMA asociada a los puntos
catalogados como receptores sensibles, junto con sus respectivos niveles máximos permitidos.

De acuerdo con lo anterior:

 Los puntos 1 y 2 se encuentran en la zona “E3”, según lo indicado en el PRC de Viña del Mar, el cual permite

el uso residencial, equipamiento, espacio público y áreas verdes, por lo que se homologan a Zona II según
el D.S No38/2011 del MMA.

 Los puntos 3 y 4 se encuentran en la zona “V4”, según lo indicado en el PRC de Viña del Mar, el cual permite

el uso residencial, equipamiento, espacio público y áreas verdes, por lo que se homologan a Zona II según
el D.S No38/2011 del MMA.

En la Tabla 8 se presenta un resumen de las homologaciones y el máximo permitido según el D.S No 38/2011 del
MMA:

**Tabla 8: Zonificación y máximos permitidos según el D.S. No 38/2011 del MMA.**

|Punto|Zona|Zonificación según<br>D.S. No38/2011 del MMA|NPC Máximo Permitido [dB(A)]|Col5|
|---|---|---|---|---|
|**Punto**<br>|**Zona**<br>|**Zonificación según**<br>**D.S. No38/2011 del MMA**<br>|~~**Periodo diurno**~~<br>|~~**Periodo nocturno**~~<br>|
|~~1 y 2~~|~~E3~~|~~Zona II~~|~~60~~|~~45~~|
|3 y 4|V4|Zona II|60|45|

**4.3.2** **Ruido - FTA Transit Noise and Vibration Impact Assessment Manual (Humanos)**

De acuerdo con el procedimiento indicado por la FTA a partir de la medición horaria de _L_ _eq_ _[h]_ es posible obtener el
_L_ _DN_, según las expresiones de cálculo descritas en el Capítulo 0, Ecuación 1 y 2. En la tabla siguiente se presentan
los resultados de este cálculo.
Para los puntos 1 y 5 se aplicará el criterio “Sin impacto” definido por el estándar de la FTA, para fines de descartar
cualquier reacción adversa en la comunidad. De este modo, se determinó el nivel de ruido existente según el
descriptor nivel día-noche _L_ _DN_ para receptores residenciales (Categoría 2). En función de dicho valor se calculó el
máximo permitido a partir de las ecuaciones dadas por el estándar de referencia [3] .

3 Apéndice C.3 de la guía FTA.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

17

**Tabla 9: Estimación del nivel de ruido existente según descriptor L** **DN** **.**

|Punto|Hora de medición<br>[hh:mm]|Nivel de ruido<br>existente<br>Leq [h] [dB(A)]*|Corrección, según<br>guía FTA [dB]|Nivel de ruido<br>existente LDN<br>[dB(A)]|Máximo “Sin<br>impacto” LDN<br>[dB(A)]**|
|---|---|---|---|---|---|
|**1 **|18:58|70|+3|73|65|
|**5 **|17:48|64|-2|62|59|

*Valor aproximado al entero más cercano.
**Máximo de referencia para que el proyecto no genere impacto (No superación de la curva inferior Ilustración 1).

En la Tabla 9, se observa que los valores de _L_ _DN_ para los puntos son 73 y 62 [dB(A)]. Estos resultados son la base
para establecer los niveles máximos permitidos para el Proyecto para flujo vehicular.

De acuerdo con la tabla anterior se tiene que los niveles máximos de ruido, para que el Proyecto se considere sin
impacto, son 65 y 59 [dB(A)], para el aporte exclusivo del Proyecto, como se observa en la última columna de la
Tabla 9.

**4.3.3** **Vibraciones - FTA**

A continuación, en la Tabla 10, se proporcionan los niveles máximos de referencia de acuerdo con la normativa FTA.

**Tabla 10: Niveles máximos de referencia según FTA.**

|Punto de medición|Máximo de referencia para<br>Criterio de Molestia según FTA,<br>en [VdB]|Máximo de referencia para Criterio de Daño según FTA|Col4|
|---|---|---|---|
|**Punto de medición**|**Máximo de referencia para**<br>**Criterio de Molestia según FTA,**<br>**en [VdB]**|**PPV [in/s]**|**Lv aproximado [VdB]**|
|1 al 4|72|0,2|94|

Para los puntos, el criterio de Molestia se definirá con un máximo de referencia de 72 [VdB], el que corresponde a la
Categoría 2 con eventos frecuentes. Para el Criterio de Daño este valor se establecerá en 0,2 [in/s] o 94 [VdB], el
que corresponde a la categoría de edificación III.

**5** **METODOLOGÍA**

**5.1** **Modelación de ruido**

**5.1.1** **Maquinarias e instalaciones**

La modelación de ruido fue empleada para estimar el nivel de presión acústica que generará el proyecto en su fase
de construcción.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

18

La metodología se basa en la normativa ISO 9613, que utiliza los principios de atenuación divergente junto a
atenuación extra introducida por obstáculos y propagación a través del aire. Las variables de entrada al modelo de
ruido son las potencias sonoras de las fuentes de ruido que contempla el proyecto.

El software de simulación computacional utilizado corresponde a SoundPLAN v8.2, el cual permite incorporar una
serie de variables físicas del medio y características acústicas de las fuentes sonoras.

La temperatura se fijó en 10 [oC] y la humedad relativa del aire en 70[%], constituyendo un escenario desfavorable
por la baja atenuación de la propagación de la onda sonora debido a estos efectos meteorológicos. Además, la
norma de cálculo utilizada considera siempre la velocidad del viento entre 1 y 5 [m/s] [4], en dirección desde las fuentes
de ruido hacia los receptores, es decir, a favor de la propagación. De acuerdo con lo anterior, el escenario modelado
representa una estacionalidad climática crítica.

**Tabla 11: Resumen de entradas y salidas en el proceso de cálculo del modelo SoundPLAN.**

|Col1|Ítem|Col3|Descripción|
|---|---|---|---|
|Entradas<br>(Input)|Topografía<br>|Topografía<br>|Cotas de terreno<br>|
|Entradas<br>(Input)|~~Ubicación de fuentes de ruido~~<br>|~~Ubicación de fuentes de ruido~~<br>|~~Puntos, áreas o líneas de emisión~~<br>|
|Entradas<br>(Input)|~~Ubicación de receptores~~<br>|~~Ubicación de receptores~~<br>|~~Puntos de evaluación~~<br>|
|Entradas<br>(Input)|Obstáculos|~~Existentes~~<br>|~~Cotas de Terreno~~<br>|
|Entradas<br>(Input)|Obstáculos|~~Introducidos~~|~~- ~~|
|Entradas<br>(Input)|Algoritmo de cálculo|Algoritmo de cálculo|ISO 9613, parte 1 y 2|
|Salidas<br>(Output)|Niveles de Presión Sonora modelados|Niveles de Presión Sonora modelados|Mapas de propagación sonora|
|Salidas<br>(Output)|Niveles de Presión Sonora modelados|Niveles de Presión Sonora modelados|Niveles de Presión Sonora en puntos de inmisión (Receptores)|

La modelación incorporó la maquinaria de mayor emisión de ruido, con lo cual se garantiza que las emisiones sonoras
provenientes de otras actividades (con maquinaria menor) quedarán enmascaradas por la emisión de las fuentes
consideradas.

El plano del proyecto (otorgado por el mandante) fue ingresado en el modelo acústico, el cual trabaja sobre un
entorno escalado y georreferenciado, de manera que permite mayor exactitud en lo que respecta a distancia y
orientación entre las fuentes de ruido y los receptores en estudio.

**5.1.2** **Flujo vehicular**

El software de simulación computacional utilizado corresponde a SoundPLAN v8.2, el cual incorpora variables físicas
del entorno y características acústicas de las fuentes sonoras.

**Tabla 12: Resumen de entradas y salidas en el proceso de cálculo del modelo SoundPLAN.**

|Col1|Ítem|Descripción|
|---|---|---|
|Entradas<br>(Input)|Topografía|Cotas de terreno|
|Entradas<br>(Input)|Ubicación de fuentes de ruido|Puntos, áreas o líneas de emisión|

4 ISO 9613-2:1996, Meteorological conditions, page 3.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

19

|Col1|Ítem|Col3|Descripción|
|---|---|---|---|
||Ubicación de receptores|Ubicación de receptores|Puntos de inmisión|
||Obstáculos|Existentes|Cotas de Terreno / Viviendas|
||Obstáculos|Introducidos|-|
||Algoritmo de cálculo|Algoritmo de cálculo|RLS - 90|
|Salidas<br>(Output)|Niveles de Presión Sonora modelados|Niveles de Presión Sonora modelados|Mapas de propagación sonora|
|Salidas<br>(Output)|Niveles de Presión Sonora modelados|Niveles de Presión Sonora modelados|Niveles de Presión Sonora en puntos de inmisión<br>elegidos (Receptores)|

Para la modelación del flujo vehicular (fuentes móviles), el cálculo se efectúa de acuerdo con la normativa alemana
RLS-90, que se divide en dos partes. La primera de ellas se refiere al descriptor principal de la línea de emisión de
una carretera, llamado LME25, y que corresponde al nivel de inmisión producido por una carretera en un punto
situado a 25 [m] del eje central y a 4 [m] sobre el nivel del suelo.

La predicción de este descriptor (LME25) utiliza las variables de:

✓ Flujo vehículos livianos.
✓ Flujo vehículos pesados.
✓ Velocidad media vehículos livianos.
✓ Velocidad media vehículos pesados.
✓ Tipo de superficie (asfalto o ripio)
✓ Reflexión múltiple (causada por eventuales edificios altos en ambos lados de la carretera).

La segunda parte de la norma se refiere al cálculo de propagación sonora desde la línea de emisión, utilizando el
LME25 como dato de entrada.

La RLS 90 fragmenta la línea de emisión como pequeños segmentos diferenciales, tomando cada uno de ellos como
una fuente puntual. La propagación la realiza considerando divergencia puntual de cada segmento, integrando la
totalidad de la carretera y calculando las atenuaciones para la banda de 500 [Hz].

La configuración física se obtiene de planos geo-referenciados con curvas de nivel elevadas y viviendas. Este
proceso de cálculo fue asistido por un modelo computacional implementado a través del software SoundPLAN®, el
cual permitió caracterizar el entorno físico del Proyecto y efectuar la estimación de acuerdo con el método antes
referido.

Finalmente, el mapa resultante representa la emisión de la vía e intenta interpretar dicha emisión en función de los
flujos vehiculares. La línea de emisión sonora se compone de fuentes puntuales incoherentes e iguales entre sí que
irradian energía acústica de propagación cilíndrica.

Las siguientes ilustraciones contienen croquis que ejemplifican la propagación de una línea de emisión en conjunto
con las atenuaciones en [dB] que se generan al incrementar la distancia entre fuente - receptor.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

20

**Ilustración 5: Croquis que representa la propagación en infraestructura vial.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.

**Ilustración 6: Esquema de propagación semi-cilíndrica.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

21

**5.2** **Proyección de vibraciones**

Las actividades de construcción pueden generar variados grados de vibración, dependiendo de la maquinaria
utilizada y de los métodos constructivos empleados, considerando además que la operación de las maquinarias
genera ondas vibratorias que disminuyen en intensidad con la distancia.

Las edificaciones cercanas a estas actividades pueden verse afectadas a las vibraciones, cuyos efectos varían desde
niveles casi imperceptibles, como ruido de baja frecuencia con percepción moderada, hasta daños en las estructuras
o en alguna parte de éstas.

Generalmente, las vibraciones generadas por actividades constructivas no suelen causar daño en las estructuras,
sin embargo, pueden alcanzar rangos audibles y sensitivos en sectores con edificaciones cercanas al sitio de faena.
Una excepción a lo anterior puede darse en edificaciones frágiles, en donde se debe tener mucho cuidado para no
generar daños.

Con el fin de predecir y evaluar el impacto producido por las vibraciones que se generarán durante la construcción
del proyecto, se utilizará la metodología de predicción y evaluación dispuesta en la norma norteamericana “ _Transit_
_Noise and Vibration Impact Assessment Manual_ ”, elaborada por la FTA, la cual establece valores de daño sobre
estructuras a partir del descriptor PPV en [in/s].

En dicha normativa, se especifican niveles de vibración referenciales para diferentes tipos de maquinaria, los cuales
fueron medidos a 25 [ft] [5] de distancia (8 [m] aproximadamente). Los valores especificados en la norma se detallan
en la siguiente tabla:

|Tabla 13: Indicadores de vibración de distintas maquinarias, medidos a 25 [ft] de distancia. Velocidad peak de partícula y niveles de vibración|Col2|Col3|
|---|---|---|
|~~**Velocidad peak de partícula y niveles de vibración**~~<br><br><br>|~~**Velocidad peak de partícula y niveles de vibración**~~<br><br><br>|~~**Velocidad peak de partícula y niveles de vibración**~~<br><br><br>|
|~~**Maquinaria**~~<br>|~~**PPV [in/s] a 25 [ft]**~~<br>|~~**L**~~**v**~~** [VdB] a 25 [ft]**~~<br>|
|~~Hincado de pilotes~~<br>|~~1,518~~<br>|~~112~~<br>|
|~~Rodillo vibratorio~~<br>|~~0,210~~<br>|~~94~~<br>|
|~~Martillo percutor en excavadora~~<br>|~~0,089~~<br>|~~87~~<br>|
|~~Bulldozer grande~~<br>|~~0,089~~<br>|~~87~~<br>|
|~~Perforadora~~<br>|~~0,089~~<br>|~~87~~<br>|
|~~Camión pesado~~<br>|~~0,076~~<br>|~~86~~<br>|
|~~Kango~~<br>|~~0,035~~<br>|~~79~~<br>|

Fuente: Federal Transit Administration (FTA) - “ _Transit Noise and Vibration Impact Assessment Manual”._

5 Pie (del inglés _foot_ ).

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

22

**Velocidad Peak de Partícula VPP o PPV**

Para la estimación del impacto producido por las actividades de construcción, se define la siguiente ecuación para
el criterio de daño:

PPV = PPV
equip ref
-( [25] D ~~[)]~~

1.5

(Ecuación 3)

Dónde:

PPV equip : Es la velocidad peak de partícula proyectada en el receptor.
PPV ref : Es la vibración de referencia en [in/s] medida a 25 [ft].
D : Distancia (en pies) entre el receptor y la fuente.

**Nivel de velocidad Lv**

Para la estimación del impacto producido por las actividades de construcción, se define la siguiente ecuación para
el criterio de molestia:

L v (D) = L v (25 ft) −30 ∙log 10 [D] (Ecuación 4)
(25 ~~[)]~~

Donde:

L v (D) : Es el nivel de velocidad en [VdB] proyectado en el receptor.
L v (25 ft) : Es el nivel de velocidad de referencia en [VdB] medido a 25 [ft].
D : Distancia (en pies) entre el receptor y la fuente.

En virtud de la ecuación anteriormente definida, se realizan proyecciones de las vibraciones en todos los receptores
evaluados.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

23

**Fase de construcción**

El análisis consideró la maquinaria de mayor emisión con la finalidad de representar y evaluar el cumplimiento
normativo para un escenario crítico. Además, la distancia Fuente - Receptor ( D ) correspondió a la separación
mínima entre la ubicación del punto de evaluación y el punto más cercano posible a la extensión de las faenas
constructivas.

**Ilustración 7: Ejemplo de situación más desfavorable de propagación de vibraciones según distancia entre maquinaria y receptor.**

Elaboración: Gerard Ingeniería Acústica SpA 2021.

Considerando la maquinaria proyectada para esta fase, y según los niveles de emisión L v que indica la Tabla 13, la
proyección de vibraciones consideró para los puntos la ejecución de la maquinaria “Rodillo vibratorio” (94 [VdB]),
homologando a un “Rodillo compactador”.

**Fase de operación**

Dada la naturaleza de las actividades que serán ejecutadas durante esta fase, se asume que éstas no generarán
emisiones vibratorias mayores a las evaluadas, por lo tanto, cumplirán con lo exigido por la normativa.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

24

**6** **DATOS DE ENTRADA AL MODELO PREDICTIVO DE RUIDO**

**6.1** **Fase de construcción**

**6.1.1** **Ruido de maquinaria e instalaciones**

La modelación contempla todas las obras que están asociadas a la construcción del proyecto, por lo cual, para su
ejecución se tiene en consideración diversa maquinaria pesada.

Las potencias acústicas asignadas a las fuentes de ruido se obtuvieron principalmente a partir de los valores
contenidos en el anexo C de la norma británica BS 5228-1:2009, “ _Code of practice for noise and vibration control on_
_construction and open sites_ ”, los cuales son comparables en magnitud a mediciones realizadas por Gerard Ingeniería
Acústica SpA a maquinarias en proyectos similares.

A continuación, en la siguiente tabla se detallan las potencias acústicas de las principales fuentes de ruido
involucradas en las faenas de construcción:

**Tabla 14: Potencias acústicas de la maquinaria utilizada en fase de construcción. Fuentes a nivel de terreno.**

|Fuente|Cantidad|Lw en [dB(A)] en espectro de frecuencia [Hz]|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Lw [dB(A)]<br>c/u|Referencia|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fuente**|**Cantidad**|**63**|**125**|**250**|**500**|**1K**|**2k**|**4k**|**8k**|**8k**|**8k**|
|Torre Grúa|4|84|89|99|101|94|95|85|77|104|BS 5228 Tabla 4, N°48|
|Camión Tolva|8|82|88|92|95|97|95|92|85|102|BS 5228 Tabla 2, N°33|
|Camión Mixer|5|82|83|84|97|99|101|97|83|105|BS 5228 Tabla 4, N°21|
|Bomba de hormigón|2|86|88|89|96|101|102|95|85|106|BS 5228 Tabla 3, N°25|
|Minicargador|1|73|83|85|84|87|87|83|75|93|BS 5228 Tabla 4, N°68|
|Excavadora|2|79|97|89|98|98|97|92|84|104|BS 5228 Tabla 2, N°15|
|Montacargas|1|87|91|88|92|92|91|85|74|99|BS 5228 Tabla 2, N°35|
|Rodillo Compactador|1|82|87|96|97|95|91|83|73|102|BS 5228 Tabla 2, N°38|
|**TOTAL - FOCO DE RUIDO**|**TOTAL - FOCO DE RUIDO**|**97**|**104**|**107**|**111**|**111**|**112**|**107**|**97**|**117**||

**Tabla 15: Potencias acústicas de la maquinaria utilizada en fase de construcción. Fuentes en altura.**

|Fuente|Cantidad|Lw en [dB(A)] en espectro de frecuencia [Hz]|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Lw [dB(A)]<br>c/u|Referencia|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fuente**|**Cantidad**|**63**|**125**|**250**|**500**|**1K**|**2k**|**4k**|**8k**|**8k**|**8k**|
|Martillo demoledor|1|85|95|100|99|101|105|107|104|111|BS 5228 Tabla 1, No 6|
|Allanadora de concreto|1|71|84|94|102|105|106|100|90|110|Ficha técnica*|
|**TOTAL - FOCO DE RUIDO**|**TOTAL - FOCO DE RUIDO**|**85**|**95**|**101**|**104**|**106**|**109**|**108**|**104**|**114**||

*Ver Anexo I.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

25

**Escenarios de modelación**

La maquinaria no funciona de forma simultánea, sino que lo realiza secuencialmente o en pequeños grupos de
trabajo. En el modelo predictivo, se configuraron dos (2) escenarios los cuales representan dos condiciones críticas
del proceso constructivo. Los focos de ruido se distribuyeron en el área donde se realizarán los trabajos considerando
la distancia más crítica entre la fuente y el receptor.

 - **Escenario 1:**

Con la finalidad de representar un escenario conservador, en el área del proyecto se simuló el funcionamiento de
todo el equipamiento asociado al frente de trabajo a nivel de terreno (Lw = 117 [dB(A)]). Dicho frente de trabajo se
distribuyó sobre el layout del Proyecto en la posición más cercana posible a los receptores.

 - **Escenario 2:**

Este escenario corresponde a evaluación de fuentes de ruido en altura, para las actividades y/o maquinarias que
produzcan altos niveles de ruido ubicadas en pisos con obra gruesa terminada en los edificios. Se considera el total
de este frente (Lw = 114 [dB(A)] a la mitad de la altura proyectada para las torres del Proyecto, duplicado para cada
receptor en la posición más cercana posible y en cada edificio. Esto es a una altura de 43 [m] para el edificio
residencial, 13 [m] para el edificio de oficina y 8,35 [m] para la placa comercial.

En las siguientes ilustraciones se indica la distribución de las fuentes para cada escenario de modelación.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

26

**Ilustración 8: Esquema fase de construcción. Ruido de maquinaria e instalaciones. Escenario1.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

27

**Ilustración 9: Esquema fase de construcción. Ruido de maquinaria e instalaciones. Escenario2.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

28

**6.1.2** **Flujo vehicular**

De acuerdo con lo informado por el mandante, el flujo vehicular para la fase de construcción corresponde
aproximadamente a 22 camiones diarios durante la jornada laboral diurna. Se consideró un flujo homogéneo cercano
a 1,5 camiones por hora, tomando en cuenta una jornada de 15 horas. La velocidad de circulación que se considera
en todas las rutas corresponde a 80 [km/h]. Por otra parte, se incluyen los edificios construidos como parte del
modelo. Esto es para considerar el impacto por parte de las reflexiones que estos podrían efectuar en las
inmediaciones del proyecto.

En la siguiente ilustración (Ilustración 10) se indican las rutas consideradas en el modelo para ruido de flujo vehicular.

**Ilustración 10: Esquema fase de construcción. Flujo vehicular.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

29

**7** **RESULTADOS**

**7.1** **Modelación y evaluación preliminar**

**7.1.1** **Fase de construcción**

**7.1.1.1** **Ruido de maquinaria e instalaciones**

A continuación, se presenta el nivel de inmisión acústica estimado para la fase de construcción en cada punto de
evaluación. Los valores se presentan en formato de tabla y mapas de propagación sonora, cuya altura de coloración
está referida a 1,5 [m] del suelo. La evaluación de cumplimiento se presenta únicamente para el periodo diurno, ya
que no se proyectan faenas durante el horario nocturno.

**Escenario 1:**

**Ilustración 11: Mapa de propagación sonora según NPSeq en [dB(A)]. Fase de construcción. Escenario 1.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.
Nota: En mapa de ruido se presenta el piso del receptor con mayor nivel de inmisión de ruido.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

30

**Tabla 16: Evaluación preliminar de cumplimiento D.S. No38/2011 del MMA. Fase de construcción. Periodo diurno. Escenario 1.**

|Punto|Piso|NPSeq proyectado, en<br>[dB(A)]*|Máximo permitido<br>Periodo diurno [dB(A)]|Evaluación|
|---|---|---|---|---|
|1|1|70|60|Supera en 10 [dB]|
|1|2|70|60|Supera en 10 [dB]|
|1|3|70|60|Supera en 10 [dB]|
|1|4|70|60|Supera en 10 [dB]|
|1|5|70|60|Supera en 10 [dB]|
|1|6|70|60|Supera en 10 [dB]|
|1|7|70|60|Supera en 10 [dB]|
|1|8|70|60|Supera en 10 [dB]|
|1|9|69|60|Supera en 9 [dB]|
|1|10|69|60|Supera en 9 [dB]|
|1|11|69|60|Supera en 9 [dB]|
|1|12|69|60|Supera en 9 [dB]|
|1|13|69|60|Supera en 9 [dB]|
|1|14|68|60|Supera en 8 [dB]|
|1|15|68|60|Supera en 8 [dB]|
|1|16|68|60|Supera en 8 [dB]|
|1|17|68|60|Supera en 8 [dB]|
|1|18|67|60|Supera en 7 [dB]|
|1 <br>|19<br>|67<br>|60<br>|Supera en 7 [dB]<br>|
|~~1 ~~<br>|~~20~~<br>|~~67~~<br>|~~60~~<br>|~~Supera en 7 [dB]~~<br>|
|~~1 ~~<br>|~~21~~<br>|~~67~~<br>|~~60~~<br>|~~Supera en 7 [dB]~~<br>|
|~~1 ~~<br>|~~22~~<br>|~~67~~<br>|~~60~~<br>|~~Supera en 7 [dB]~~<br>|
|~~1 ~~<br>|~~23~~<br>|~~66~~<br>|~~60~~<br>|~~Supera en 6 [dB]~~<br>|
|~~1 ~~<br>|~~24~~<br>|~~66~~<br>|~~60~~<br>|~~Supera en 6 [dB]~~<br>|
|~~2 ~~<br>|~~1 ~~<br>|~~66~~<br>|~~60~~<br>|~~Supera en 6 [dB]~~<br>|
|~~2 ~~<br>|~~2 ~~<br>|~~67~~<br>|~~60~~<br>|~~Supera en 7 [dB]~~<br>|
|~~2 ~~<br>|~~3 ~~<br>|~~67~~<br>|~~60~~<br>|~~Supera en 7 [dB]~~<br>|
|~~2 ~~<br>|~~4 ~~<br>|~~68~~<br>|~~60~~<br>|~~Supera en 8 [dB]~~<br>|
|~~2 ~~|~~5 ~~|~~68~~|~~60~~|~~Supera en 8 [dB]~~|
|2|6|68|60|Supera en 8 [dB]|
|2|7|68|60|Supera en 8 [dB]|
|2|8|68|60|Supera en 8 [dB]|
|2|9|68|60|Supera en 8 [dB]|
|2|10|68|60|Supera en 8 [dB]|
|2|11|68|60|Supera en 8 [dB]|
|2|12|67|60|Supera en 7 [dB]|
|2|13|67|60|Supera en 7 [dB]|
|2|14|67|60|Supera en 7 [dB]|
|2|15|67|60|Supera en 7 [dB]|
|2|16|67|60|Supera en 7 [dB]|
|2|17|67|60|Supera en 7 [dB]|
|2|18|67|60|Supera en 7 [dB]|
|2|19|66|60|Supera en 6 [dB]|
|2|20|66|60|Supera en 6 [dB]|
|2|21|66|60|Supera en 6 [dB]|
|2|22|66|60|Supera en 6 [dB]|

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

31

|Punto|Piso|NPSeq proyectado, en<br>[dB(A)]*|Máximo permitido<br>Periodo diurno [dB(A)]|Evaluación|
|---|---|---|---|---|
|~~2 ~~<br>|~~23~~<br>|~~66~~<br>|~~60~~<br>|~~Supera en 6 [dB]~~<br>|
|~~2 ~~<br>|~~24~~<br>|~~66~~<br>|~~60~~<br>|~~Supera en 6 [dB]~~<br>|
|~~2 ~~<br>|~~25~~<br>|~~66~~<br>|~~60~~<br>|~~Supera en 6 [dB]~~<br>|
|~~3 ~~<br>|~~1 ~~<br>|~~67~~<br>|~~60~~<br>|~~Supera en 7 [dB]~~<br>|
|~~3 ~~<br>|~~2 ~~<br>|~~67~~<br>|~~60~~<br>|~~Supera en 7 [dB]~~<br>|
|~~3 ~~|~~3 ~~|~~67~~|~~60~~|~~Supera en 7 [dB]~~|
|3|4|67|60|Supera en 7 [dB]|
|3|5|67|60|Supera en 7 [dB]|
|3|6|67|60|Supera en 7 [dB]|
|3|7|67|60|Supera en 7 [dB]|
|3|8|67|60|Supera en 7 [dB]|
|3|9|67|60|Supera en 7 [dB]|
|3|10|67|60|Supera en 7 [dB]|
|3|11|66|60|Supera en 6 [dB]|
|3|12|66|60|Supera en 6 [dB]|
|3|13|66|60|Supera en 6 [dB]|
|3|14|66|60|Supera en 6 [dB]|
|3|15|66|60|Supera en 6 [dB]|
|3|16|66|60|Supera en 6 [dB]|
|3|17|66|60|Supera en 6 [dB]|
|3|18|66|60|Supera en 6 [dB]|
|3|19|66|60|Supera en 6 [dB]|
|3|20|65|60|Supera en 5 [dB]|
|3|21|65|60|Supera en 5 [dB]|
|3|22|65|60|Supera en 5 [dB]|
|3 <br>|23<br>|65<br>|60<br>|Supera en 5 [dB]<br>|
|~~3 ~~<br>|~~24~~<br>|~~65~~<br>|~~60~~<br>|~~Supera en 5 [dB]~~<br>|
|~~3 ~~<br>|~~25~~<br>|~~65~~<br>|~~60~~<br>|~~Supera en 5 [dB]~~<br>|
|~~3 ~~<br>|~~26~~<br>|~~65~~<br>|~~60~~<br>|~~Supera en 5 [dB]~~<br>|
|~~4 ~~|~~1 ~~|~~65~~|~~60~~|~~Supera en 5 [dB]~~|

*Valores aproximados al entero más cercano.

Se aprecia en la evaluación anterior que las emisiones esperadas para la fase de construcción superan los máximos
que establece D.S. No 38/11 del MMA en la totalidad de los receptores sensibles. Sin embargo, se implementarán
medidas de control de ruido con tal de alcanzar el cumplimiento normativo. En el capítulo 8.1 se presentan las
medidas de control asociadas.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

32

**Escenario 2:**

**Ilustración 12: Mapa de propagación sonora según NPSeq en [dB(A)]. Fase de construcción. Escenario 2.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.
Nota: En mapa de ruido se presenta el piso del receptor con mayor nivel de inmisión de ruido.

**Tabla 17: Evaluación preliminar de cumplimiento D.S. No38/2011 del MMA. Fase de construcción. Periodo diurno. Escenario 2.**

|Punto|Piso|NPSeq proyectado, en<br>[dB(A)]*|Máximo permitido<br>Periodo diurno [dB(A)]|Evaluación|
|---|---|---|---|---|
|1|1|76|60|Supera en 16 [dB]|
|1|2|76|60|Supera en 16 [dB]|
|1|3|76|60|Supera en 16 [dB]|
|1 <br>|4 <br>|76<br>|60<br>|Supera en 16 [dB]<br>|
|~~1 ~~<br>|~~5 ~~<br>|~~76~~<br>|~~60~~<br>|~~Supera en 16 [dB]~~<br>|
|~~1 ~~<br>|~~6 ~~<br>|~~76~~<br>|~~60~~<br>|~~Supera en 16 [dB]~~<br>|
|~~1 ~~<br>|~~7 ~~<br>|~~76~~<br>|~~60~~<br>|~~Supera en 16 [dB]~~<br>|
|~~1 ~~<br>|~~8 ~~<br>|~~76~~<br>|~~60~~<br>|~~Supera en 16 [dB]~~<br>|
|~~1 ~~<br>|~~9 ~~<br>|~~76~~<br>|~~60~~<br>|~~Supera en 16 [dB]~~<br>|
|~~1 ~~<br>|~~10~~<br>|~~76~~<br>|~~60~~<br>|~~Supera en 16 [dB]~~<br>|
|~~1 ~~|~~11~~|~~76~~|~~60~~|~~Supera en 16 [dB]~~|

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

33

|Punto|Piso|NPSeq proyectado, en<br>[dB(A)]*|Máximo permitido<br>Periodo diurno [dB(A)]|Evaluación|
|---|---|---|---|---|
|~~1 ~~<br>|~~12~~<br>|~~76~~<br>|~~60~~<br>|~~Supera en 16 [dB]~~<br>|
|~~1 ~~<br>|~~13~~<br>|~~76~~<br>|~~60~~<br>|~~Supera en 16 [dB]~~<br>|
|~~1 ~~<br>|~~14~~<br>|~~76~~<br>|~~60~~<br>|~~Supera en 16 [dB]~~<br>|
|~~1 ~~<br>|~~15~~<br>|~~75~~<br>|~~60~~<br>|~~Supera en 15 [dB]~~<br>|
|~~1 ~~<br>|~~16~~<br>|~~75~~<br>|~~60~~<br>|~~Supera en 15 [dB]~~<br>|
|~~1 ~~|~~17~~|~~75~~|~~60~~|~~Supera en 15 [dB]~~|
|1|18|75|60|Supera en 15 [dB]|
|1|19|74|60|Supera en 14 [dB]|
|1|20|74|60|Supera en 14 [dB]|
|1|21|74|60|Supera en 14 [dB]|
|1|22|74|60|Supera en 14 [dB]|
|1|23|74|60|Supera en 14 [dB]|
|1|24|73|60|Supera en 13 [dB]|
|2|1|72|60|Supera en 12 [dB]|
|2|2|73|60|Supera en 13 [dB]|
|2|3|73|60|Supera en 13 [dB]|
|2|4|73|60|Supera en 13 [dB]|
|2|5|73|60|Supera en 13 [dB]|
|2|6|73|60|Supera en 13 [dB]|
|2|7|73|60|Supera en 13 [dB]|
|2|8|74|60|Supera en 14 [dB]|
|2|9|74|60|Supera en 14 [dB]|
|2|10|74|60|Supera en 14 [dB]|
|2|11|74|60|Supera en 14 [dB]|
|2|12|74|60|Supera en 14 [dB]|
|2 <br>|13<br>|74<br>|60<br>|Supera en 14 [dB]<br>|
|~~2 ~~<br>|~~14~~<br>|~~74~~<br>|~~60~~<br>|~~Supera en 14 [dB]~~<br>|
|~~2 ~~<br>|~~15~~<br>|~~74~~<br>|~~60~~<br>|~~Supera en 14 [dB]~~<br>|
|~~2 ~~<br>|~~16~~<br>|~~74~~<br>|~~60~~<br>|~~Supera en 14 [dB]~~<br>|
|~~2 ~~<br>|~~17~~<br>|~~74~~<br>|~~60~~<br>|~~Supera en 14 [dB]~~<br>|
|~~2 ~~<br>|~~18~~<br>|~~74~~<br>|~~60~~<br>|~~Supera en 14 [dB]~~<br>|
|~~2 ~~<br>|~~19~~<br>|~~74~~<br>|~~60~~<br>|~~Supera en 14 [dB]~~<br>|
|~~2 ~~<br>|~~20~~<br>|~~73~~<br>|~~60~~<br>|~~Supera en 13 [dB]~~<br>|
|~~2 ~~<br>|~~21~~<br>|~~73~~<br>|~~60~~<br>|~~Supera en 13 [dB]~~<br>|
|~~2 ~~<br>|~~22~~<br>|~~73~~<br>|~~60~~<br>|~~Supera en 13 [dB]~~<br>|
|~~2 ~~|~~23~~|~~73~~|~~60~~|~~Supera en 13 [dB]~~|
|2|24|73|60|Supera en 13 [dB]|
|2|25|73|60|Supera en 13 [dB]|
|3|1|72|60|Supera en 12 [dB]|
|3|2|73|60|Supera en 13 [dB]|
|3|3|73|60|Supera en 13 [dB]|
|3|4|73|60|Supera en 13 [dB]|
|3|5|73|60|Supera en 13 [dB]|
|3|6|73|60|Supera en 13 [dB]|
|3|7|73|60|Supera en 13 [dB]|
|3|8|73|60|Supera en 13 [dB]|

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

34

|Punto|Piso|NPSeq proyectado, en<br>[dB(A)]*|Máximo permitido<br>Periodo diurno [dB(A)]|Evaluación|
|---|---|---|---|---|
|~~3 ~~<br>|~~9 ~~<br>|~~73~~<br>|~~60~~<br>|~~Supera en 13 [dB]~~<br>|
|~~3 ~~<br>|~~10~~<br>|~~73~~<br>|~~60~~<br>|~~Supera en 13 [dB]~~<br>|
|~~3 ~~<br>|~~11~~<br>|~~73~~<br>|~~60~~<br>|~~Supera en 13 [dB]~~<br>|
|~~3 ~~<br>|~~12~~<br>|~~73~~<br>|~~60~~<br>|~~Supera en 13 [dB]~~<br>|
|~~3 ~~<br>|~~13~~<br>|~~73~~<br>|~~60~~<br>|~~Supera en 13 [dB]~~<br>|
|~~3 ~~|~~14~~|~~73~~|~~60~~|~~Supera en 13 [dB]~~|
|3|15|73|60|Supera en 13 [dB]|
|3|16|73|60|Supera en 13 [dB]|
|3|17|73|60|Supera en 13 [dB]|
|3|18|73|60|Supera en 13 [dB]|
|3|19|73|60|Supera en 13 [dB]|
|3|20|73|60|Supera en 13 [dB]|
|3|21|73|60|Supera en 13 [dB]|
|3|22|73|60|Supera en 13 [dB]|
|3|23|72|60|Supera en 12 [dB]|
|3|24|72|60|Supera en 12 [dB]|
|3|25|72|60|Supera en 12 [dB]|
|3|26|72|60|Supera en 12 [dB]|
|4 <br>|1 <br>|73|60|Supera en 13 [dB]|

*Valores aproximados al entero más cercano.

Se aprecia en la evaluación anterior que las emisiones esperadas para la fase de construcción superan los máximos
que establece D.S. No 38/11 del MMA en la totalidad de los receptores sensibles. Sin embargo, se implementarán
medidas de control de ruido con tal de alcanzar el cumplimiento normativo. En el capítulo 8.1 se presentan las
medidas de control asociadas.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

35

**7.1.1.2** **Flujo vehicular**

Se presentan a continuación, los resultados obtenidos a partir del modelo predictivo representativo del flujo vehicular
de la fase de construcción del Proyecto, juntamente con la evaluación de cumplimiento normativo. Los resultados se
entregan mediante mapas de propagación sonora cuya coloración está referida a una altura de 1,5 [m] del suelo y
valores tabulados.

**Ilustración 13: Mapa de propagación sonora según L** **DN** **en [dB(A)]. Fase de construcción. Flujo vehicular.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.
Nota: En mapa de ruido se indica el piso con mayor nivel de inmisión en cada receptor.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

36

**Tabla 18: Evaluación preliminar de cumplimiento. Fase de construcción. Periodo diurno. Flujo vehicular**

|Receptor|Piso|Nivel de Presión<br>Proyectado [dB(A)]|Valor límite de inmisión<br>Periodo diurno [dB(A)]*|Evaluación|
|---|---|---|---|---|
|1|1|52|65|No supera|
|1|2|53|65|No supera|
|1|3|54|65|No supera|
|1|4|53|65|No supera|
|1|5|53|65|No supera|
|1|6|53|65|No supera|
|1|7|53|65|No supera|
|1|8|52|65|No supera|
|1|9|52|65|No supera|
|1|10|52|65|No supera|
|1|11|51|65|No supera|
|1|12|51|65|No supera|
|1|13|51|65|No supera|
|1|14|51|65|No supera|
|1|15|50|65|No supera|
|1|16|50|65|No supera|
|1|17|50|65|No supera|
|1|18|49|65|No supera|
|1|19|49|65|No supera|
|1|20|49|65|No supera|
|1|21|49|65|No supera|
|1|22|48|65|No supera|
|1|23|48|65|No supera|
|1|24|48|65|No supera|
|5|1|56|59|No supera|

*Valores aproximados al entero más cercano.

De acuerdo con la evaluación presentada no se supera el estándar aplicado en todos los puntos de evaluación para
el flujo vehicular en fase de construcción.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

37

**7.2** **Proyección de vibraciones**

En la siguiente tabla se presentan los resultados de las proyecciones vibratorias (PPV) realizadas para todos los
puntos de evaluación de acuerdo con la metodología detallada en el capítulo 5.2. Posteriormente se indica la
evaluación para el criterio de daño y molestia, cuyos niveles máximos permitidos se indicaron en el acápite 0.

**Tabla 19: Proyección de L** **V** **y PPV en cada receptor. Vibraciones generadas por maquinaria pesada.**

|Punto|Faena o maquinaria más cercana|Distancia<br>[m]|Distancia<br>[ft]|PPV proyectado<br>[in/s]|Lv proyectado<br>[VdB]|
|---|---|---|---|---|---|
|~~1 ~~<br>|~~Rodillo vibratorio~~<br>|~~28~~<br>|~~92~~<br>|~~0,03~~<br>|~~77~~<br>|
|~~2 ~~<br>|~~Rodillo vibratorio~~<br>|~~50~~<br>|~~164~~<br>|~~0,01~~<br>|~~69~~<br>|
|~~3 ~~<br>|~~Rodillo vibratorio~~<br>|~~47~~<br>|~~154~~<br>|~~0,01~~<br>|~~70~~<br>|
|~~4 ~~|~~Rodillo vibratorio~~|~~61~~|~~200~~|~~ < 0,01~~|~~67~~|

**Criterio de daño**

**Tabla 20: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de daño.**

|Punto|PPV proyectado [in/s]|PPV Máximo permitido [in/s]|Observación|
|---|---|---|---|
|1|0,03 <br>|0,2|Cumple|
|2|0,01 <br>|0,2|Cumple|
|3|0,01 <br>|0,2|Cumple|
|4|< 0,01|0,2|Cumple|

**Criterio de molestia**

**Tabla 21: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de molestia.**

|Punto|LV proyectado [VdB]|LV Máximo permitido [VdB]|Observación|
|---|---|---|---|
|1|77|72|No Cumple|
|2|69|72|Cumple|
|3|70|72|Cumple|
|4|67|72|Cumple|

En las tablas anteriores se puede apreciar que los valores proyectados para la construcción del Proyecto en PPV se
encuentran por debajo de los máximos recomendados por la guía para el criterio de daño, pero para el criterio de
molestia es posible apreciar que en el punto 1 preliminarmente se superan los límites establecidos. Por este motivo,
en el capítulo 8 se presentan medidas de control a incorporar en el Proyecto.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

38

**8** **MEDIDAS DE CONTROL**

Debido a las superaciones preliminares del capítulo anterior, a continuación, se describen aquellas medidas de
control que permitirán enmarcar la fase de construcción bajo los umbrales que define las normativas aplicadas.

**8.1** **Ruido**

**8.1.1** **Escenario 1: Barreras acústicas**

Esta solución consiste en la implementación de una barrera perimetral ubicada en el deslinde del proyecto y en
barreras modulares cercanas a la maquinaria. Estas barreras acústicas deberán fabricarse en base a las
características detalladas en la siguiente ficha técnica.

**Tabla 22: Características barreras acústicas propuesta para la fase de construcción.**

6 Coeficiente de reducción sonora o NRC de sus siglas en inglés. Corresponde un descriptor global para indicar la absorción sonora de un producto.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

39

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

40

En la siguiente ilustración se presenta croquis con la ubicación de esta medida de control de ruido.

**Ilustración 14: Croquis implementación de barrera acústica. Fase de construcción. Escenario 1.**

Fuente: Gerard Ingeniería Acústica SpA 2022.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

41

**8.1.2** **Escenario 2: Cierre de vanos**

Para las actividades y/o maquinarias que produzcan altos niveles de ruido ubicadas en pisos con obra gruesa
terminada, se pueden instalar planchas de OSB de 18 [mm] en los vanos laterales existentes en la obra gruesa.
Dichas planchas deberán cubrir toda la superficie de los vanos, de modo de sellar todas las aberturas que puedan
servir como vía de transmisión del sonido. Dicha medida deberá ser aplicada específicamente en el piso en el cual
se estén desarrollando las actividades.

**Ilustración 15: Ejemplo de aplicación de medida de confinamiento.**

La pérdida por transmisión TL (de sus siglas en inglés: Transmission Loss), del panel OSB utilizado es:

|Col1|Tabla 23: Pérdida de transmisión del elemento divisorio. OSB e.: 18 [mm].|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Elemento divisorio**|**TL [dB] en bandas de octava de frecuencia [Hz]**|**TL [dB] en bandas de octava de frecuencia [Hz]**|**TL [dB] en bandas de octava de frecuencia [Hz]**|**TL [dB] en bandas de octava de frecuencia [Hz]**|**TL [dB] en bandas de octava de frecuencia [Hz]**|**TL [dB] en bandas de octava de frecuencia [Hz]**|**TL [dB] en bandas de octava de frecuencia [Hz]**|**Rw **<br>**[dB]**|**Fuente**|
|**Elemento divisorio**|**63**|**125**|**250**|**500**|**1k**|**2k**|**4k**|**4k**|**4k**|
|OSB e.: 18 [mm]|13|16|20|24|26|28|37|**27 **|INSUL v7.0.6*|

*Ver Anexo II.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

42

**8.2** **Vibraciones**

**8.2.1** **Buffer de seguridad**

Esta medida de control de vibraciones está enfocada en reducir el exceso evidenciado en fase de construcción (ver
capítulo 7.2) y cumplir con los valores recomendados por la normativa para el criterio de molestia a personas.
Consiste en restringir la distancia mínima entre el lugar de ejecución de faenas con maquinaria pesada y los
receptores afectados, en este caso, el punto 1.

Dicho buffer de seguridad deberá ser de al menos 40 [m] entre la fuente y el receptor, con tal de asegurar que no
exista un impacto. En la siguiente figura se presenta un croquis con la ubicación de esta medida de control de
vibraciones en torno al punto 1. Por ende, y sólo para el punto 1, se debe realizar la maniobra sin el uso de maquinaria
pesada que emita vibraciones importantes dentro de este buffer. Es decir, se tendrán que utilizar tecnologías
alternativas: faenas manuales (mano de obra) o similar.

**Ilustración 16: Croquis implementación de buffer de seguridad. Fase de construcción. Punto 1.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

43

**9** **RESULTADOS Y EVALUACIÓN CON MEDIDAS DE CONTROL**

**9.1** **Ruido**

En el presente capítulo se detallan los niveles de ruido generados durante la fase de construcción considerando la
implementación de medidas de control de ruido indicadas en el capítulo anterior (capítulo 8.1). Los valores se
presentan en formato de tabla y mapas de propagación sonora, cuya altura de coloración está referida a 1,5 [m] del
suelo.

**Escenario 1:**

**Ilustración 17: Mapa de propagación sonora según NPSeq en [dB(A)]. Fase de construcción con medidas de control. Escenario 1.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.
Nota: En mapa de ruido se presenta el piso del receptor con mayor nivel de inmisión de ruido.

La evaluación de cumplimiento se presenta únicamente para el periodo diurno, ya que no se proyectan faenas
durante el horario nocturno.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

44

**Tabla 24: Evaluación preliminar de cumplimiento D.S. No38/2011 del MMA. Fase de construcción. Periodo diurno. Escenario 1.**

|Punto|Piso|NPSeq proyectado, en<br>[dB(A)]*|Máximo permitido<br>Periodo diurno [dB(A)]|Evaluación|
|---|---|---|---|---|
|1|1|55|60|Cumple|
|1|2|56|60|Cumple|
|1|3|56|60|Cumple|
|1|4|57|60|Cumple|
|1|5|57|60|Cumple|
|1|6|57|60|Cumple|
|1|7|57|60|Cumple|
|1|8|57|60|Cumple|
|1|9|56|60|Cumple|
|1|10|56|60|Cumple|
|1|11|56|60|Cumple|
|1|12|56|60|Cumple|
|1|13|56|60|Cumple|
|1|14|56|60|Cumple|
|1|15|56|60|Cumple|
|1|16|55|60|Cumple|
|1|17|55|60|Cumple|
|1|18|55|60|Cumple|
|1 <br>|19<br>|55<br>|60<br>|Cumple<br>|
|~~1 ~~<br>|~~20~~<br>|~~55~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~1 ~~<br>|~~21~~<br>|~~54~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~1 ~~<br>|~~22~~<br>|~~54~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~1 ~~<br>|~~23~~<br>|~~54~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~1 ~~<br>|~~24~~<br>|~~54~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~2 ~~<br>|~~1 ~~<br>|~~52~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~2 ~~<br>|~~2 ~~<br>|~~53~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~2 ~~<br>|~~3 ~~<br>|~~53~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~2 ~~<br>|~~4 ~~<br>|~~53~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~2 ~~|~~5 ~~|~~54~~|~~60~~|~~Cumple~~|
|2|6|54|60|Cumple|
|2|7|54|60|Cumple|
|2|8|54|60|Cumple|
|2|9|54|60|Cumple|
|2|10|54|60|Cumple|
|2|11|54|60|Cumple|
|2|12|54|60|Cumple|
|2|13|54|60|Cumple|
|2|14|54|60|Cumple|
|2|15|54|60|Cumple|
|2|16|54|60|Cumple|
|2|17|54|60|Cumple|
|2|18|54|60|Cumple|
|2|19|54|60|Cumple|
|2|20|54|60|Cumple|
|2|21|53|60|Cumple|
|2|22|53|60|Cumple|

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

45

|Punto|Piso|NPSeq proyectado, en<br>[dB(A)]*|Máximo permitido<br>Periodo diurno [dB(A)]|Evaluación|
|---|---|---|---|---|
|~~2 ~~<br>|~~23~~<br>|~~53~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~2 ~~<br>|~~24~~<br>|~~53~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~2 ~~<br>|~~25~~<br>|~~53~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~3 ~~<br>|~~1 ~~<br>|~~51~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~3 ~~<br>|~~2 ~~<br>|~~53~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~3 ~~|~~3 ~~|~~53~~|~~60~~|~~Cumple~~|
|3|4|53|60|Cumple|
|3|5|53|60|Cumple|
|3|6|53|60|Cumple|
|3|7|53|60|Cumple|
|3|8|53|60|Cumple|
|3|9|53|60|Cumple|
|3|10|53|60|Cumple|
|3|11|53|60|Cumple|
|3|12|53|60|Cumple|
|3|13|53|60|Cumple|
|3|14|53|60|Cumple|
|3|15|53|60|Cumple|
|3|16|53|60|Cumple|
|3|17|53|60|Cumple|
|3|18|53|60|Cumple|
|3|19|53|60|Cumple|
|3|20|53|60|Cumple|
|3|21|53|60|Cumple|
|3|22|53|60|Cumple|
|3 <br>|23<br>|53<br>|60<br>|Cumple<br>|
|~~3 ~~<br>|~~24~~<br>|~~53~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~3 ~~<br>|~~25~~<br>|~~53~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~3 ~~<br>|~~26~~<br>|~~53~~<br>|~~60~~<br>|~~Cumple~~<br>|
|~~4 ~~|~~1 ~~|~~52~~|~~60~~|~~Cumple~~|

*Valores aproximados al entero más cercano.

Se aprecia en la evaluación anterior que las emisiones esperadas para la fase de construcción no superan los
máximos que establece D.S. No 38/11 del MMA al incorporar las medidas de control de ruido propuestas.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

46

**Escenario 2:**

**Ilustración 18: Mapa de propagación sonora según NPSeq en [dB(A)]. Fase de construcción con medidas de control. Escenario 2.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.
Nota: En mapa de ruido se presenta el piso del receptor con mayor nivel de inmisión de ruido.

La evaluación de cumplimiento se presenta únicamente para el periodo diurno, ya que no se proyectan faenas
durante el horario nocturno.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

47

**Tabla 25: Evaluación preliminar de cumplimiento D.S. No38/2011 del MMA. Fase de construcción. Periodo diurno. Escenario 2.**

|Punto|Piso|NPSeq proyectado, en<br>[dB(A)]*|Máximo permitido<br>Periodo diurno [dB(A)]|Evaluación|
|---|---|---|---|---|
|1|1|55|60|No supera|
|1|2|56|60|No supera|
|1|3|56|60|No supera|
|1|4|57|60|No supera|
|1|5|57|60|No supera|
|1|6|57|60|No supera|
|1|7|57|60|No supera|
|1|8|57|60|No supera|
|1|9|56|60|No supera|
|1|10|56|60|No supera|
|1|11|56|60|No supera|
|1|12|56|60|No supera|
|1|13|56|60|No supera|
|1|14|56|60|No supera|
|1|15|56|60|No supera|
|1|16|55|60|No supera|
|1|17|55|60|No supera|
|1|18|55|60|No supera|
|1 <br>|19<br>|55<br>|60<br>|No supera<br>|
|~~1 ~~<br>|~~20~~<br>|~~55~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~1 ~~<br>|~~21~~<br>|~~54~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~1 ~~<br>|~~22~~<br>|~~54~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~1 ~~<br>|~~23~~<br>|~~54~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~1 ~~<br>|~~24~~<br>|~~54~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~2 ~~<br>|~~1 ~~<br>|~~52~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~2 ~~<br>|~~2 ~~<br>|~~53~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~2 ~~<br>|~~3 ~~<br>|~~53~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~2 ~~<br>|~~4 ~~<br>|~~53~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~2 ~~|~~5 ~~|~~54~~|~~60~~|~~No supera~~|
|2|6|54|60|No supera|
|2|7|54|60|No supera|
|2|8|54|60|No supera|
|2|9|54|60|No supera|
|2|10|54|60|No supera|
|2|11|54|60|No supera|
|2|12|54|60|No supera|
|2|13|54|60|No supera|
|2|14|54|60|No supera|
|2|15|54|60|No supera|
|2|16|54|60|No supera|
|2|17|54|60|No supera|
|2|18|54|60|No supera|
|2|19|54|60|No supera|
|2|20|54|60|No supera|
|2|21|53|60|No supera|
|2|22|53|60|No supera|

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

48

|Punto|Piso|NPSeq proyectado, en<br>[dB(A)]*|Máximo permitido<br>Periodo diurno [dB(A)]|Evaluación|
|---|---|---|---|---|
|~~2 ~~<br>|~~23~~<br>|~~53~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~2 ~~<br>|~~24~~<br>|~~53~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~2 ~~<br>|~~25~~<br>|~~53~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~3 ~~<br>|~~1 ~~<br>|~~51~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~3 ~~<br>|~~2 ~~<br>|~~53~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~3 ~~|~~3 ~~|~~53~~|~~60~~|~~No supera~~|
|3|4|53|60|No supera|
|3|5|53|60|No supera|
|3|6|53|60|No supera|
|3|7|53|60|No supera|
|3|8|53|60|No supera|
|3|9|53|60|No supera|
|3|10|53|60|No supera|
|3|11|53|60|No supera|
|3|12|53|60|No supera|
|3|13|53|60|No supera|
|3|14|53|60|No supera|
|3|15|53|60|No supera|
|3|16|53|60|No supera|
|3|17|53|60|No supera|
|3|18|53|60|No supera|
|3|19|53|60|No supera|
|3|20|53|60|No supera|
|3|21|53|60|No supera|
|3|22|53|60|No supera|
|3 <br>|23<br>|53<br>|60<br>|No supera<br>|
|~~3 ~~<br>|~~24~~<br>|~~53~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~3 ~~<br>|~~25~~<br>|~~53~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~3 ~~<br>|~~26~~<br>|~~53~~<br>|~~60~~<br>|~~No supera~~<br>|
|~~4 ~~|~~1 ~~|~~52~~|~~60~~|~~No supera~~|

*Valores aproximados al entero más cercano.

Se aprecia en la evaluación anterior que las emisiones esperadas para la fase de construcción no superan los
máximos que establece D.S. No 38/11 del MMA al incorporar las medidas de control de ruido propuestas. Notar que
el cumplimiento normativo se alcanza con una holgura de 3 [dB].

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

49

**9.2** **Vibraciones**

A continuación, se presenta la evaluación de vibraciones al implementar el buffer de seguridad señalado en el
Capítulo 8.2.1 como medida de control.

**Tabla 26: Proyección de L** **V** **y PPV en cada receptor. Vibraciones generadas por maquinaria pesada.**

|Punto|Faena o maquinaria más cercana|Distancia<br>[m]|Distancia<br>[ft]|PPV proyectado<br>[in/s]|Lv proyectado<br>[VdB]|
|---|---|---|---|---|---|
|1|Rodillo vibratorio|40|131|0,02|72|
|2|Rodillo vibratorio|50|164|0,01|69|
|3|Rodillo vibratorio|47|154|0,01|70|
|4|Rodillo vibratorio|61|200|< 0,01|67|

**Criterio de daño**

**Tabla 27: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de daño.**

|Punto|PPV proyectado [in/s]|PPV Máximo permitido [in/s]|Observación|
|---|---|---|---|
|~~1 ~~<br>|~~0,02 ~~<br>|~~0,2~~<br>|~~Cumple~~<br>|
|~~2 ~~<br>|~~0,01 ~~<br>|~~0,2~~<br>|~~Cumple~~<br>|
|~~3 ~~<br>|~~0,01 ~~<br>|~~0,2~~<br>|~~Cumple~~<br>|
|~~4 ~~|~~ < 0,01 ~~|~~0,2~~|~~Cumple~~|

**Criterio de molestia**

**Tabla 28: Evaluación de cumplimiento. Vibraciones generadas por maquinaria pesada. Criterio de molestia.**

|Punto|LV proyectado [VdB]|LV Máximo permitido [VdB]|Observación|
|---|---|---|---|
|1|72|72|Cumple|
|2|69|72|Cumple|
|3|70|72|Cumple|
|4|67|72|Cumple|

En las tablas anteriores se puede apreciar que los valores proyectados para la construcción del proyecto se
encuentran por debajo de los máximos recomendados por la normativa tanto para el criterio de daño como el de
molestia para todos los puntos al incorporar la medida de control de vibraciones.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

50

**10** **CONCLUSIONES**

Se realizaron mediciones de ruido y vibraciones en sectores sensibles cercanos al futuro emplazamiento del Proyecto
“ _Makroplaza_ ”, ubicado en la comuna de Viña del Mar, Región de Valparaíso, obteniéndose cinco (5) puntos de
muestreo de ruido y vibraciones que caracterizan cabalmente dichos sectores.

Para el análisis acústico del proyecto se utilizó un modelo de ruido asistido por el software SoundPLAN v8.2, el cual
permitió estimar el nivel de ruido generado por la maquinaria involucrada en la fase de construcción del proyecto.
Los niveles de presión acústica obtenidos fueron evaluados de acuerdo con el máximo permitido por el D.S. N° 38/11
del MMA, presentando superaciones preliminares de los valores establecidos por dicha normativa para todos los
receptores en fase de construcción para el periodo diurno. Cabe señalar que durante la fase de construcción se
considera la implementación de barreras acústicas sobre maquinaria a nivel del terreno, como así también, cierre de
vanos en pisos superiores de edificios durante las obras de terminaciones sobre obra gruesa.

Respecto de la evaluación del flujo vehicular realizada mediante la guía americana de la FTA para la fase de
construcción, se evaluó exclusivamente para los puntos 1 y 5 un caso el cual corresponde a la circulación diaria de
22 vehículos pesados por la ruta inmediata de acceso al proyecto. A partir de los valores obtenidos, se espera que
el Proyecto no genere impacto acústico perjudicial en los receptores ubicados en el entorno de dichas rutas.

Los niveles vibratorios proyectados para maquinaria pesada fueron evaluados mediante la guía americana de la
FTA, tanto para el criterio de molestia como el criterio de daño, donde para este último, los valores cumplen con los
máximos recomendados por dicha guía en todos los puntos. En cuanto a la evaluación por criterio de molestia, se
registran superaciones en el receptor del punto 1, estableciendo en consecuencia, la generación de un buffer de
seguridad de 40 [m] donde no podrá operar maquinaria pesada.

En virtud de todo lo anteriormente señalado, se asume que el proyecto no generará un impacto acústico y/o vibratorio
negativo en los receptores cercano al emplazamiento de este.

**M** **ATÍAS** **D** **URÁN** **F** **ARÍAS**

I NGENIERO C IVIL A CÚSTICO

J EFE DE P ROYECTOS

**G** **ERARD** **I** **NGENIERÍA** **A** **CÚSTICA** **S** **P** **A.**

**M** **AX** **G** **LISSER** **D** **ONOSO**

I NGENIERO C IVIL EN S ONIDO Y A CÚSTICA

G ERENTE T ÉCNICO

**G** **ERARD** **I** **NGENIERÍA** **A** **CÚSTICA** **S** **P** **A.**

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

51

**11** **INSTRUMENTAL**

 - 01 Sonómetro marca Rion, modelo NL-22, Clase 2 según IEC 61672-1:2002.

 - 01 Calibrador de niveles sonoros marca RION, modelo NC-74 Clase 1 según IEC 60942:2003.

 - 01 Analizador en tiempo real marca Svantek modelo SVAN 958A, con acelerómetro triaxial PCB.

 - 01 Calibrador de analizador en tiempo real marca Svantek modelo SV33.

 - 01 Cámara fotográfica digital marca Canon, modelo Powershot Elph 160.

 - 01 Termo anemómetro marca Extech modelo 41158.

 - 01 GPS (Global Positioning System) marca Garmin, modelo Legend H.

**12** **BIBLIOGRAFÍA**

 - IEC 61672-1:2002, _Electroacoustic - Sound Level Meters - Part 1: Specifications_ .

 - Decreto No 38/2011 del MMA: _Establece Norma de Ruido generados para fuentes que indica_, elaborada a

partir de la revisión del Decreto No 146, de 1997, Ministerio Secretaría General de la República.

 - Resolución Exenta No 491/2016 del SMA “Instrucción de carácter general sobre criterios para homologación de

zonas del decreto supremo N° 38 de 2011 del Ministerio del Medio Ambiente”

 - ISO 9613-2:1996, _Attenuation of sound during propagation outdoors_ .

 - Software Designers & Consulting Engineers for Noise Control & Environmental Protection _SoundPLAN_ - User
Manual.

 - U.S. Federal Transit Administration Report, _Transit Noise and Vibration Impact Assessment Manual_, Edición

Septiembre de 2018.

 - Samir N. Y. Gerges, Ruido, Fundamentes y control, Primera edición en español, 1998.

 - BS 5228-1:2009, “ _Code of practice for noise and vibration control on construction and open sites_ ”.

 Guía para la predicción y evaluación de impactos por ruido y vibración en el SEIA, del Servicio de Evaluación
Ambiental (SEA), 2019.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

52

**13** **PROFESIONALES PARTICIPANTES**

|LISTADO DE PROFESIONALES|Col2|
|---|---|
|**Jefe de Proyecto**|Matías Durán Farías|
|**Gerente de proyectos**|Claudio Salas Castro|
|**Gerente Técnico**|Max Glisser Donoso|
|**Gerente General**|Christian Gerard Büchi|
|**Asistente de Proyecto**|Juan Pablo Cuevas Fuentealba|
|**Ingeniero de Proyecto**<br>|Nicolás Hrdina Pavez|

**14** **GLOSARIO**

a) **Decibel [dB]:** Unidad adimensional usada para expresar 10 veces el logaritmo de la razón entre una
cantidad medida y una cantidad de referencia.

b) **Decibel A [dB(A)]:** Es la unidad adimensional usada para expresar el nivel de presión sonora, medido con
el filtro de ponderación de frecuencias A.

c) **Fuente emisora de ruido:** Toda actividad, proceso, operación o dispositivo que genere, o pueda generar,
emisiones de ruido hacia la comunidad.

d) **Ruido de fondo:** es aquel ruido que está presente en el mismo lugar y momento de medición de la fuente
que se desea evaluar, en ausencia de ésta.

e) **Nivel de Presión Sonora (NPS ó L** **p** **):** Se expresa en decibeles [dB] y se define por la siguiente relación
matemática:

NPS= 20 ∙log 10
( [P] P [1] [)]

Donde:
P 1 : Valor efectivo de la presión medida
P : Valor efectivo de la presión sonora de referencia, fijada en 2×10 [-5] [N/m [2] ]

f) **Nivel de Presión Sonora Continuo Equivalente (NPSeq):** Es aquel nivel de presión sonora constante,
expresado en decibeles A, que, en el mismo intervalo de tiempo, contiene la misma energía total (o dosis)
que el ruido medido.

g) **Nivel de Presión Sonora Máximo (NPS** **máx** **):** Es el NPS más alto registrado durante el periodo de medición,
con respuesta lenta.

h) **Nivel de Presión Sonora Mínimo (NPS** **mín** **):** Es el NPS más bajo registrado durante el periodo de medición,
con respuesta lenta.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

53

i) **Nivel de Presión Sonora Corregido (NPC):** Es aquel nivel de presión sonora continuo equivalente, que
resulte de aplicar el procedimiento de medición y las correcciones definidas en el D.S. N° 38/2011 del MMA.

j) **Receptor:** Toda persona que habite, resida o permanezca en un recinto, ya sea un domicilio particular o en
un lugar de trabajo, que esté o pueda estar expuesta al ruido generado por una fuente emisora de ruido
externa.

k) **Respuesta Lenta:** Es la respuesta temporal del instrumento de medición que evalúa la energía media en
un intervalo de 1 segundo. Cuando el instrumento mide el nivel de presión sonora con respuesta lenta, dicho
nivel se denomina NPS Lento. Si además se emplea el filtro de ponderación A, el nivel obtenido se expresa
en [dB(A)] Lento.

l) **Vibraciones:** Perturbación que provoca la oscilación de los cuerpos sobre su posición de equilibrio.

m) **Acelerómetro:** Dispositivo que convierte los efectos del movimiento mecánico en una señal eléctrica, la cual
es proporcional al valor de aceleración del movimiento .

n) **Analizador de Frecuencia:** Equipo de medición acústica que permite analizar los componentes en
frecuencia de un sonido.

o) **Velocidad eficaz o RMS:** Valor cuadrático medio (RMS) de velocidad de la onda de vibración.

p) **Velocidad de referencia:** Velocidad utilizada para transformar la velocidad vibratoria en nivel de velocidad

in

vibratoria, como 10-6 [ ~~[]]~~ [, definida en normativas internacionales. ]

in

vibratoria, como 10-6 [ s ~~[]]~~ [, definida en normativas internacionales. ]

q) **Bandas de tercio de Octava:** Intervalo entre dos tonos cuya relación es de un tercio de la octava, (21/3 ó
1,259).

r) **Nivel de Velocidad (Lv):** Se expresa en decibeles [dB] y se define por la siguiente relación matemática:

L v = 20 ∙log 10 [v]
(v ref

)

Donde:

v : Valor de Velocidad medida, en unidades [

in

s [] ]

v ref : Valor de Velocidad de referencia, fijada en 1×10-6 [

in

v ref : Valor de Velocidad de referencia, fijada en 1×10-6 [ s ~~[]]~~

s) **Direcciones de medición:** Sistema de coordenadas que se origina en el punto desde el cual se considera
que ingresa la vibración al cuerpo humano.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

54

# ANEXO I JUSTIFICACIÓN DE POTENCIAS ACÚSTICAS

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

55

**Cálculo de potencias acústicas**

El nivel de potencia acústica Lw (o NWS) se obtuvo a partir de mediciones de nivel de presión sonora a una distancia
conocida desde la fuente de ruido y aplicando la expresión matemática que indica la Ecuación 5. Esta relación asume
que la propagación de la onda diverge en forma de semi-esfera, simulando la ubicación de una fuente puntual sobre
un plano reflectante donde la sección de propagación equivale a 2πr [2] :

**Ecuación 5**
NWS= NPS medido + 20 ∙log 10 (r) + 8 [7]

Dónde:

NWS : Nivel de Potencia Acústica (L w o NWS).
NPS medido : Nivel de Presión Sonora (NPS) medido en [dB(A)] a una distancia r .
r : Distancia en [m] a la cual se registró el NPS medido .

7 Samir, Gerges. Fundamentos y Control de Ruido y Vibraciones.

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

56

**Allanadora de pavimento**

**Ilustración 19: Ficha técnica allanadora de pavimento.**

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

57

Nota: Se asume Lw = 110 [dB(A)] como potencia acústica del equipo producto de la corta distancia entre operador y motor (< 0,5 [m]).

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

58

El espectro de potencia del equipo se obtiene mediante cálculo en software ENC 4.1 (Tabla 29, Ilustración 20)
considerando un motor eléctrico de 9 [HP] (6,7 [kW]) a 3.600 R.P.M.

**Tabla 29: Nivel de potencia acústica motor eléctrico 9 [HP].**

|Fuente|Lw [dB(A)] en bandas de octava de frecuencia [Hz]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Lw<br>[dB(A)]|Fuente|
|---|---|---|---|---|---|---|---|---|---|---|
|**Fuente**|**63**|**125**|**250**|**500**|**1k**|**2k**|**4k**|**8K**|**8K**|**8K**|
|Motor Eléctrico 9 [HP]|52,1|65,2|74,7|83,1|86,3|86,5|81,3|71,2|**91,0**|Software ENC 4.1|

9 [HP] = 6,7 [kW]

**Ilustración 20: Software ENC 4.1. Cálculo potencia acústica motor eléctrico 9 [HP]**

Nota: Se obtiene Lw = 91 [dB(A)] según cálculo por Ecuación 5 para SPL@1m = 83 [dB(A)].

Se puede observar que la diferencia entre el Lw de la Tabla 29 y el valor en ficha técnica (Ilustración 19) es de 19

[dB(A)], el cual es sumado a cada banda de frecuencia, con el fin de ajustar la curva al Lw esperado (110 [dB(A)]).
De esta forma, el nivel de potencia acústica de la allanadora de pavimento se presenta en la Tabla 30.

**Tabla 30: Nivel de potencia acústica allanadora de pavimento.**

|Fuente|Lw [dB(A)] en bandas de octava de frecuencia [Hz]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Lw<br>[dB(A)]|Fuente|
|---|---|---|---|---|---|---|---|---|---|---|
|**Fuente**|**63**|**125**|**250**|**500**|**1k**|**2k**|**4k**|**8K**|**8K**|**8K**|
|Allanadora de pavimento|71,1|84,2|93,7|102,1|105,3|105,5|100,3|90,2|**110**|Ficha técnica|

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

59

# ANEXO II CÁLCULO INSUL OSB 18 [mm]

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

60

E STUDIO DE IMPACTO ACÚSTICO Y VIBRATORIO

M AKROPLAZA - R EV . B

61

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 9.**

| Punto de medición | Máximo de referencia para<br>Criterio de Molestia según FTA,<br>en [VdB] | Máximo de referencia para Criterio de Daño según FTA | Col4 |
| --- | --- | --- | --- |
| **Punto de medición** | **Máximo de referencia para**<br>**Criterio de Molestia según FTA,**<br>**en [VdB]** | **PPV [in/s]** | **Lv aproximado [VdB]** |
| 1 al 4 | 72 | 0,2 | 94 |
