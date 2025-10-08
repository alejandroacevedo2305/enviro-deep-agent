---
title: Sin título
author: Desconocido
date: D:20220418200805-04'00'
language: es
type: manual
pages: 22
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO I REFERENCIAS POTENCIA ACÚSTICA
-->

## ESTUDIO ACÚSTICO EN FAUNA

### PROYECTO SUBESTACIÓN SECCIONADORA 220/33 KV ORCOMA COMUNA DE HUARA - REGIÓN DE TARAPACÁ

**P** **REPARADO PARA** **:**

S ANTIAGO, ABRIL DE 2022

G ERARD I NGENIERÍA A CÚSTICA S P A

SE ENCUENTRA CERTIFICADO POR :

**ÍNDICE DE CONTENIDOS**

1 Introducción .............................................................................................................................................................. 3

2 Objetivos ................................................................................................................................................................... 3

2.1 Objetivo general .............................................................................................................................................. 3

2.2 Objetivos específicos ...................................................................................................................................... 3

3 Normativas o guías de referencia ............................................................................................................................ 4

3.1 Ruido en fauna silvestre.................................................................................................................................. 4

4 Área de influencia (AI) .............................................................................................................................................. 5

5 Puntos de evaluación ............................................................................................................................................... 7

6 Metodología .............................................................................................................................................................. 8

6.1 Modelación de ruido ........................................................................................................................................ 8

7 Datos de entrada al modelo predictivo de ruido ..................................................................................................... 9

7.1 Fase de construcción ...................................................................................................................................... 9

7.2 Fase de operación ......................................................................................................................................... 10

7.3 Fase de cierre ................................................................................................................................................ 11

8 Resultados .............................................................................................................................................................. 12

8.1 Modelación y evaluación de ruido ................................................................................................................ 12

8.1.1 Fase de construcción ............................................................................................................................. 12

8.1.2 Fase de operación .................................................................................................................................. 13

9 Conclusiones .......................................................................................................................................................... 15

10 Bibliografía utilizada ............................................................................................................................................... 16

11 Profesionales participantes .................................................................................................................................... 17

12 Glosario ................................................................................................................................................................... 17

ANEXO I ........................................................................................................................................................................... 18

**ÍNDICE DE ILUSTRACIONES**

Ilustración 1: Extracto de revisión bibliográfica acerca de umbrales de evaluación de ruido en fauna ................................................................................ 4
Ilustración 2: Área de influencia. Vista general. ................................................................................................................................................................ 6
Ilustración 3: Ubicación de los puntos de evaluación. Vista general. ................................................................................................................................. 7
Ilustración 4: Mapa de propagación sonora según NPSeq en [dB(A)]. Fase de construcción. .......................................................................................... 12
Ilustración 5: Mapa de propagación sonora según NPSeq en [dB(A)]. Fase de operación. .............................................................................................. 14

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

1

**ÍNDICE DE TABLAS**

Tabla 1: Resumen de revisión bibliográfica de umbrales para la evaluación de impacto de ruido en avifauna. ................................................................... 5

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 4 En la Tabla 1 se resume el detalle de la información dispuesta en la bibliografía revisada por el documento en cuestión: -->

**Tabla 1: Resumen de revisión bibliográfica de umbrales para la evaluación de impacto de ruido en avifauna.****

| Autor | Año | Ref. | Componente<br>biótico | Descripción umbral | Valor umbral<br>[dB(A)] | Tipo de efecto sobre<br>el umbral |
| --- | --- | --- | --- | --- | --- | --- |
| Brown et al. | 1990 | 1 | Thallaseus bergii<br>(emparentado con<br>gaviotín) | Magnitud de ruido registrada en<br>colonias reproductivas control y<br>tratamientos | 60 | Se incrementan<br>conductas de alerta.<br>Luego miedo y escape. |
| Dooling et al. | 2007 | 2 | Aves | Nivel de ruido emitido en<br>carretera equivalente a espectro<br>que un ave experimenta en área<br>suburbana silenciosa (3 kHz).<br>Umbral es considerado informal<br>pero bien conocido. | 60 | Se enmascara la<br>vocalización, por<br>encima de<br>enmascaramiento<br>natural. |
| McGregor et al. | 2013 | 3 | Animales<br>(excluidos<br>humanos) | Ante ausencia de normativa de<br>referencia (USA y Canadá), se<br>propone usar umbral para<br>humanos<br>zonas<br>urbanas<br>residenciales como efectivo<br>para fauna | 60 | Umbral diseñado para<br>humanos en zonas<br>urbanas residenciales,<br>componentes fauna<br>afectados<br>negativamente. |
| California<br>Department<br>of<br>Trasportation | 2016 | 4 | Aves | Umbral de enmascaramiento<br>promedio de aves en zonas<br>adyacentes a carreteras | 60 | Comunicación cómoda<br>entre aves ubicadas a<br>60 metros o más de la<br>carretera. A menor<br>distancia el umbral de<br>enmascaramiento<br>crece. |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- En virtud de lo anterior, para este estudio se utiliza el valor de 60 [dB(A)] como criterio de evaluación para todos los puntos. **4** **ÁREA DE ESTUDIO** -->
<!-- FIN TABLA 1 -->

Tabla 2: Ubicación y descripción de receptores. .............................................................................................................................................................. 7

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Ilustración 3: Ubicación de los puntos de evaluación. Vista general.** Elaboración: Gerard Ingeniería Acústica SpA 2022. -->

**Tabla 2: Ubicación y descripción de receptores.****

| Punto | Nombre común | Evidencia | N° de<br>individuos | Coordenadas UTM | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Punto** | **Nombre común** | **Evidencia** | **N° de**<br>**individuos** | **Datum WGS 84**<br>**Huso 19K Sur** | **Datum WGS 84**<br>**Huso 19K Sur** |
| **Punto** | **Nombre común** | **Evidencia** | **N° de**<br>**individuos** | **Este** | **Norte** |
| D1 | Dragón de Stolzmann | Avistamiento | 1 | 387083 | 7795032 |
| S1 | Salamanqueja del norte grande | Avistamiento | 1 | 387034 | 7795261 |
| S2 | Salamanqueja del norte grande | Avistamiento | 1 | 387000 | 7795163 |
| S3 | Salamanqueja del norte grande | Avistamiento | 1 | 387177 | 7795187 |
| S4 | Salamanqueja del norte grande | Avistamiento | 1 | 387178 | 7795155 |
| S5 | Salamanqueja del norte grande | Avistamiento | 1 | 387188 | 7795157 |

<!-- Estadísticas: 8 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Nota: Coordenadas obtenidas en terreno. E STUDIO A CÚSTICO EN F AUNA S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D -->
<!-- FIN TABLA 2 -->

Tabla 3: Resumen de entradas y salidas en el proceso de cálculo del modelo SoundPLAN. ............................................................................................. 8

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- por la baja atenuación de la propagación de la onda sonora debido a estos efectos meteorológicos. Además, la norma de cálculo utilizada considera siempre la velocidad del viento entre 1 y 5 [m/s] [3], en dirección desde las fuentes de ruido hacia los receptores, es decir, a favor de la propagación. De acuerdo con lo anterior, el escenario modelado representa una estacionalidad climática crítica. -->

**Tabla 3: Resumen de entradas y salidas en el proceso de cálculo del modelo SoundPLAN.****

| Col1 | Ítem | Col3 | Descripción |
| --- | --- | --- | --- |
| Entradas<br>(Input) | Topografía | Topografía | Cotas de terreno |
| Entradas<br>(Input) | Ubicación de fuentes de ruido | Ubicación de fuentes de ruido | Puntos, áreas o líneas de emisión |
| Entradas<br>(Input) | Ubicación de receptores | Ubicación de receptores | Puntos de evaluación |
| Entradas<br>(Input) | Obstáculos | Existentes | Cotas de Terreno |
| Entradas<br>(Input) | Obstáculos | Introducidos | - |
| Entradas<br>(Input) | Algoritmo de cálculo | Algoritmo de cálculo | ISO 9613, parte 1 y 2 |
| Salidas<br>(Output) | Niveles de Presión Sonora modelados | Niveles de Presión Sonora modelados | Mapas de propagación sonora |
| Salidas<br>(Output) | Niveles de Presión Sonora modelados | Niveles de Presión Sonora modelados | Niveles de Presión Sonora en puntos de inmisión (Receptores) |

<!-- Estadísticas: 8 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- La modelación incorporó la maquinaria de mayor emisión de ruido, con lo cual se garantiza que las emisiones sonoras provenientes de otras actividades (con maquinaria menor) quedarán enmascaradas por la emisión de las fuentes consideradas. -->
<!-- FIN TABLA 3 -->

Tabla 4: Niveles de potencia acústica. Maquinaria fase de construcción. Movimiento, nivelación y comptactación de terreno. .......................................... 9

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- - **Subestación seccionadora** Movimiento, nivelación y compactación del terreno -->

**Tabla 4: Niveles de potencia acústica. Maquinaria fase de construcción.****

| Col1 | Tabla | a 4: Niveles de potencia acústica. Maquinaria fase de construcció Movimiento, nivelación y comptactación de terreno. | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | ón. | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente de ruido** | **Cantidad** | **Lw en dB(A) en bandas de octava de frecuencia** | **Lw en dB(A) en bandas de octava de frecuencia** | **Lw en dB(A) en bandas de octava de frecuencia** | **Lw en dB(A) en bandas de octava de frecuencia** | **Lw en dB(A) en bandas de octava de frecuencia** | **Lw en dB(A) en bandas de octava de frecuencia** | **Lw en dB(A) en bandas de octava de frecuencia** | **Lw en dB(A) en bandas de octava de frecuencia** | **Lw**<br>**dB(A)** | **Referencia** |
| **Fuente de ruido** | **Cantidad** | **63** | **125** | **250** | **500** | **1k** | **2k** | **4k** | **8k** | **8k** | **8k** |
| Motoniveladora | 1 | 92.5 | 95.5 | 99.5 | 99.5 | 97.5 | 94.5 | 91.5 | 86.5 | 105.2 | Ficha técnica* |
| Camión tolva | 1 | 81.8 | 87.9 | 92.4 | 94.8 | 97.0 | 95.2 | 92.0 | 84.9 | 102.0 | BS 5228 Tabla 02, No 33 |
| Excavadora | 1 | 78.8 | 85.9 | 90.4 | 94.8 | 96.0 | 95.2 | 89.0 | 80.9 | 101.1 | BS 5228 Tabla 02, No 24 |
| Cargador frontal | 1 | 84.8 | 88.9 | 89.4 | 94.8 | 98.0 | 97.2 | 93.0 | 84.9 | 102.7 | BS 5228 Tabla 06, No32 |
| Camión aljibe | 1 | 73.0 | 84.0 | 86.0 | 95.0 | 92.0 | 95.0 | 90.0 | 83.0 | 99.9 | Environmental Noise<br>Monitoring* |
| Rodillo | 1 | 83.8 | 89.9 | 86.4 | 95.8 | 95.0 | 93.2 | 89.0 | 83.9 | 100.7 | BS 5228 Tabla 02, No 40 |
| **Total Foco de Ruido** | **Total Foco de Ruido** | **94** | **98** | **101** | **104** | **104** | **103** | **99** | **92** | **110** |  |

<!-- Estadísticas: 9 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- - Ver Anexo I Montaje -->
<!-- FIN TABLA 4 -->

Tabla 5: Niveles de potencia acústica. Maquinaria fase de construcción. Montaje. .......................................................................................................... 10

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- E STUDIO A CÚSTICO EN F AUNA S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D 9 -->

**Tabla 5: Niveles de potencia acústica. Maquinaria fase de construcción. Montaje.****

| Fuente de ruido | Cantidad | Lw en dB(A) en bandas de octava de frecuencia | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Lw<br>dB(A) | Referencia |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente de ruido** | **Cantidad** | **63** | **125** | **250** | **500** | **1k** | **2k** | **4k** | **8k** | **8k** | **8k** |
| Camión Grúa | 2 | 79.8 | 80.9 | 86.4 | 88.8 | 90.0 | 86.2 | 78.0 | 66.9 | 94.6 | BS 5228 Tabla 04, No 46 |
| Camión tolva | 1 | 81.8 | 87.9 | 92.4 | 94.8 | 97.0 | 95.2 | 92.0 | 84.9 | 102.0 | BS 5228 Tabla 02, No 33 |
| **Total Foco de Ruido** | **Total Foco de Ruido** | **85** | **89** | **94** | **97** | **99** | **96** | **92** | **85** | **103** |  |

<!-- Estadísticas: 4 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- - **Instalación de faenas** La instalación de faena considerada para este proyecto contempla la misma cantidad y tipo de maquinaria que la ya declarada y aprobada en el EIA del proyecto “Orcoma” cuyo detalle forma parte del Anexo 49 de la Adenda [4] . En la -->
<!-- FIN TABLA 5 -->

Tabla 6: Niveles de potencia acústica. Maquinaria fase de construcción. Instalación de faenas. ..................................................................................... 10

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La instalación de faena considerada para este proyecto contempla la misma cantidad y tipo de maquinaria que la ya declarada y aprobada en el EIA del proyecto “Orcoma” cuyo detalle forma parte del Anexo 49 de la Adenda [4] . En la siguiente tabla se indica el nivel de potencia acústica para dicha instalación de faenas. -->

**Tabla 6: Niveles de potencia acústica. Maquinaria fase de construcción. Instalación de faenas.****

| Fuente de ruido | Lw en bandas de octava de frecuencia | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Lw | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente de ruido** | **63** | **125** | **250** | **500** | **1k** | **2k** | **4k** | **8k** | **8k** | **8k** |
| Instalación de faenas | 90 | 91 | 91 | 91 | 89 | 87 | 84 | 79 | **98** | **dB(A)** |

<!-- Estadísticas: 2 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- La maquinaria indicada en las tablas anteriores no opera de forma simultánea, sino que de manera secuencial o en pequeños grupos de trabajo. De todos modos, con la finalidad de representar un escenario conservador, se simuló el funcionamiento del equipamiento asociado a uno de los frentes de mayor emisión sonora para cada obra y/o sector, correspondiente a: 1) “Movimiento, nivelación y compactación de terreno” para la subestación seccionadora, -->
<!-- FIN TABLA 6 -->

Tabla 7: Factor de corrección C para ecuación de cálculo para ruido de transformadores en [dB(Z)] ............................................................................... 11
Tabla 8: Nivel de potencia acústica del transformador a utilizar durante la fase de operación. ......................................................................................... 11

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La siguiente tabla indica el L w correspondiente a los parámetros utilizados en los cálculos (W e =50 [MVA] con N R =75.4 [dB(A)]). -->

**Tabla 8: Nivel de potencia acústica del transformador a utilizar durante la fase de operación.****

| Fuente | Cantidad | Lw [dB(A)] en bandas de octava de frecuencia [Hz] | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Lw<br>[dB(A)]<br>c/u | Fuente |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | **Cantidad** | **63** | **125** | **250** | **500** | **1k** | **2k** | **4k** | **8K** | **8K** | **8K** |
| Transformador<br>50 [MVA] | 1 | 70.4 | 82.5 | 85.0 | 90.4 | 87.6 | 83.8 | 78.6 | 69.5 | 94.0 | Crocker, Malcolm J. - Handbook of<br>Noise and Vibration Control, 2007 |

<!-- Estadísticas: 2 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- Finalmente, para el caso del generador eléctrico y las camionetas se tienen los siguientes niveles de potencia acústica: **Tabla 9: Nivel de potencia acústica del transformador a utilizar durante la fase de operación.** -->
<!-- FIN TABLA 8 -->

Tabla 9: Nivel de potencia acústica del transformador a utilizar durante la fase de operación. ......................................................................................... 11

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Transformador<br>50 [MVA]|1|70.4|82.5|85.0|90.4|87.6|83.8|78.6|69.5|94.0|Crocker, Malcolm J. - Handbook of<br>Noise and Vibration Control, 2007| Finalmente, para el caso del generador eléctrico y las camionetas se tienen los siguientes niveles de potencia acústica: -->

**Tabla 9: Nivel de potencia acústica del transformador a utilizar durante la fase de operación.****

| Fuente | Cantidad | Lw [dB(A)] en bandas de octava de frecuencia [Hz] | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Lw<br>[dB(A)] c/u | Fuente |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | **Cantidad** | **63** | **125** | **250** | **500** | **1k** | **2k** | **4k** | **8K** | **8K** | **8K** |
| Camionetas | 2 | 69.1 | 77.7 | 77.3 | 83.5 | 93.0 | 94.0 | 92.1 | 85.6 | 98.3 | SoundPLAN 8.2 database* |
| GE 150 kW | 1 | 62.5 | 73.6 | 81.1 | 86.5 | 87.7 | 86.9 | 83.7 | 76.6 | 92.9 | Bies, Hansen |

<!-- Estadísticas: 3 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- *Ver Anexo I **7.3** **Fase de cierre** -->
<!-- FIN TABLA 9 -->

Tabla 10: Evaluación de cumplimiento fase de construcción. ......................................................................................................................................... 13

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- E STUDIO A CÚSTICO EN F AUNA S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D 12 -->

**Tabla 10: Evaluación de cumplimiento fase de construcción.****

| Punto | NPS proyectado [dB(A)]*<br>eq | Máximo permitido [dB(A)] | Evaluación |
| --- | --- | --- | --- |
| ~~D1~~ | ~~48~~ | 60 | ~~No supera~~ |
| S1 | 48 | 48 | No supera |
| S2 | 44 | 44 | No supera |
| S3 | 51 | 51 | No supera |
| S4 | 51 | 51 | No supera |
| S5 | 51 | 51 | No supera |

<!-- Estadísticas: 6 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- *Valores aproximados al entero más cercano. En la evaluación anterior se aprecia que en todos los puntos de evaluación no se supera el umbral seleccionado de 60 [dB(A)]. -->
<!-- FIN TABLA 10 -->

Tabla 11: Evaluación de cumplimiento fase de operación............................................................................................................................................... 14

<!-- INICIO TABLA 11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Ilustración 5: Mapa** **de** **propagación sonora** **según NPSeq** **en [dB(A)]. Fase** **de** **operación.** Elaboración: Gerard Ingeniería Acústica SpA 2022. -->

**Tabla 11: Evaluación de cumplimiento fase de operación.****

| Punto | NPS proyectado [dB(A)]*<br>eq | Máximo permitido [dB(A)] | Evaluación |
| --- | --- | --- | --- |
| D1 | 41 | 60 | No Supera |
| S1 | 44 | 44 | No Supera |
| S2<br> | 57<br> | 57<br> | No Supera<br> |
| ~~S3~~ | ~~39~~ | ~~39~~ | ~~No Supera~~ |
| S4 | 38 | 38 | No Supera |
| S5 | 38 | 38 | No Supera |

<!-- Estadísticas: 6 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- *Valores aproximados al entero más cercano. En la evaluación anterior se aprecia que los niveles de ruido proyectados para la fase de operación no superan el umbral de evaluación seleccionado en todos los puntos de evaluación. -->
<!-- FIN TABLA 11 -->


E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

2

**1** **INTRODUCCIÓN**

El presente documento, elaborado por Gerard Ingeniería Acústica SpA, contiene la proyección y evaluación de ruido
del proyecto “ _Subestación Seccionadora 220/33 kV Orcoma”_ (en adelante “Proyecto”), el cual se ubicará en la
comuna de Huara, Región de Tarapacá, con la finalidad principal de evaluar los niveles de ruido del Proyecto en los
sectores cercanos cuya fauna silvestre pueda verse afectada. Cabe señalar que se descarta la evaluación en
receptores humanos, considerando que la localidad más próxima se encuentra a aproximadamente a 32 [km] del
área en la cual se construirán y operarán las obras físicas del Proyecto.

Las actividades involucradas en las fases de construcción, operación y cierre del Proyecto pueden generar un
aumento del nivel de ruido en los sectores aledaños. En este contexto, la definición del área de estudio se efectuó
en base a la existencia de especies de fauna silvestre, identificándose seis (6) puntos de evaluación.

Se llevó a cabo la predicción de los niveles de ruido mediante un modelo asistido por software, con lo que se obtiene
la magnitud de las inmisiones acústicas en los puntos de evaluación definidos considerando las características del
Proyecto.

Finalmente, los valores estimados fueron comparados con el umbral máximo referencial aceptado como seguro para
la avifauna por el “California Department of Transportation” de EE. UU. (60 [dB(A)]), indicando medidas de control
para los puntos donde fue necesario.

**2** **OBJETIVOS**

**2.1** **Objetivo general**

 - Evaluar la potencial afectación acústica que podría generar el Proyecto _,_ de acuerdo con los criterios de
evaluación establecidos.

**2.2** **Objetivos específicos**

 Identificar puntos de evaluación asociados a la fauna silvestre que pueda verse afectada producto de la
emisión acústica del Proyecto en sus distintas fases.

 Predecir el nivel de ruido que generarán las distintas actividades que contempla el Proyecto mediante un
modelo acústico asistido por software.

 Verificar el cumplimiento del umbral límite de 60 [dB(A)] recomendado por el “California Department of
Transportation” de EEUU y proponer medidas de control en caso de ser necesarias.

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

3

**3** **NORMATIVAS O GUÍAS DE REFERENCIA**

**3.1** **Ruido en fauna silvestre**

Si bien en la Guía de Evaluación Ambiental: Componente Fauna Silvestre D-RNN-EIA-PR-001 publicada por el SAG
del Ministerio de Agricultura en 2019, en su punto 6.1, letra (g) se recomienda utilizar como referencia el documento
de la EPA que establece como referencia un máximo de 85 [dB(Z)] como umbral de ruido para no generar efectos
sobre fauna silvestre, revisiones bibliográficas posteriores indican que existen umbrales de ruido más restrictivos
que buscan una mayor protección de la fauna.

A continuación, se presenta un extracto del documento “Revisión bibliográfica, síntesis y propuesta. Umbrales de
ruido y respuestas biológicas en fauna, con énfasis en aves” presentado por Geobiota como parte de la segunda
Adenda complementaria en el EIA del proyecto “Tente en el Aire” en su Anexo 11 [1], en el cual se sugiere un umbral
máximo de 60 [dB(A)] como valor seguro para la avifauna y fauna en general:

**Ilustración 1: Extracto de revisión bibliográfica acerca de umbrales de evaluación de ruido en fauna**

1 https://infofirma.sea.gob.cl/DocumentosSEA/MostrarDocumento?docId=c3/27/e022351648747bcd6afead578413da8ecf9e

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

4

En la Tabla 1 se resume el detalle de la información dispuesta en la bibliografía revisada por el documento en
cuestión:

**Tabla 1: Resumen de revisión bibliográfica de umbrales para la evaluación de impacto de ruido en avifauna.**

|Autor|Año|Ref.|Componente<br>biótico|Descripción umbral|Valor umbral<br>[dB(A)]|Tipo de efecto sobre<br>el umbral|
|---|---|---|---|---|---|---|
|Brown et al.|1990|1|Thallaseus bergii<br>(emparentado con<br>gaviotín)|Magnitud de ruido registrada en<br>colonias reproductivas control y<br>tratamientos|60|Se incrementan<br>conductas de alerta.<br>Luego miedo y escape.|
|Dooling et al.|2007|2|Aves|Nivel de ruido emitido en<br>carretera equivalente a espectro<br>que un ave experimenta en área<br>suburbana silenciosa (3 kHz).<br>Umbral es considerado informal<br>pero bien conocido.|60|Se enmascara la<br>vocalización, por<br>encima de<br>enmascaramiento<br>natural.|
|McGregor et al.|2013|3|Animales<br>(excluidos<br>humanos)|Ante ausencia de normativa de<br>referencia (USA y Canadá), se<br>propone usar umbral para<br>humanos<br>zonas<br>urbanas<br>residenciales como efectivo<br>para fauna|60|Umbral diseñado para<br>humanos en zonas<br>urbanas residenciales,<br>componentes fauna<br>afectados<br>negativamente.|
|California<br>Department<br>of<br>Trasportation|2016|4|Aves|Umbral de enmascaramiento<br>promedio de aves en zonas<br>adyacentes a carreteras|60|Comunicación cómoda<br>entre aves ubicadas a<br>60 metros o más de la<br>carretera. A menor<br>distancia el umbral de<br>enmascaramiento<br>crece.|

En virtud de lo anterior, para este estudio se utiliza el valor de 60 [dB(A)] como criterio de evaluación para todos los
puntos.

**4** **ÁREA DE ESTUDIO**

El área de estudio se establece en función de la existencia de individuos de fauna silvestre que potencialmente
pueden ser afectados por un aumento en los niveles de presión sonora.

De este modo, para determinar el área se considera un cálculo simple de atenuación sonora debido a divergencia
geométrica (propagación por distancia), a partir de un nivel de emisión acústica máximo posible de las actividades
con maquinaria pesada que se desarrollará en el Proyecto, representativas de la condición más crítica (mayor
emisión de ruido), junto con el umbral de evaluación considerado (60 [dB(A)])

La fórmula de cálculo utilizada viene dada de la siguiente expresión para una fuente de ruido puntual:

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

5

NPS = NWS− 20 Log ( r ) − 8 [ dB ( A )] **(Ecuación 1)** **[2]**
Dónde:
NPS : Nivel de presión sonora en dB(A),
NWS : Nivel de potencia sonora en dB(A) y
r : Distancia entre la fuente y el receptor.

Tomando como referencia el mayor nivel NWS (o L w ) del Proyecto con un nivel de potencia acústica de 110 [dB(A)]
asociado al frente de trabajo “Movimiento, nivelación y compactación de terreno” de la subestación seccionadora
(detalle acápite 7.1 del presente documento), el nivel de 60 [dB(A)] se alcanza a una distancia fuente-receptor de
aproximadamente 126 [m] desde el área del Proyecto, equivalente a un área total aproximada de 19.1 [ha].

Es importante destacar que todos los cálculos determinan la condición más crítica de propagación, no considerando
atenuación acústica debido a obstáculos topográficos, ni tampoco absorción de aire y suelo, como también considera
la totalidad de la potencia acústica en un punto, lo cual no ocurrirá en la realidad.

**Ilustración 2: Área** **de Estudio. Vista** **general.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.

2 Samir N.Y Gerges. “Ruido, Fundamentos y Control”

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

6

**5** **PUNTOS DE EVALUACIÓN**

A continuación, en la Tabla 2 y en la Ilustración 3 se presenta la ubicación y descripción de los puntos de evaluación
de ruido, los cuales fueron seleccionados de acuerdo con la evidencia de fauna silvestre presente en las cercanías
de las futuras fuentes generadoras de ruido del Proyecto.

**Ilustración 3: Ubicación de los puntos de evaluación. Vista general.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.

**Tabla 2: Ubicación y descripción de receptores.**

|Punto|Nombre común|Evidencia|N° de<br>individuos|Coordenadas UTM|Col6|
|---|---|---|---|---|---|
|**Punto**|**Nombre común**|**Evidencia**|**N° de**<br>**individuos**|**Datum WGS 84**<br>**Huso 19K Sur**|**Datum WGS 84**<br>**Huso 19K Sur**|
|**Punto**|**Nombre común**|**Evidencia**|**N° de**<br>**individuos**|**Este**|**Norte**|
|D1|Dragón de Stolzmann|Avistamiento|1|387083|7795032|
|S1|Salamanqueja del norte grande|Avistamiento|1|387034|7795261|
|S2|Salamanqueja del norte grande|Avistamiento|1|387000|7795163|
|S3|Salamanqueja del norte grande|Avistamiento|1|387177|7795187|
|S4|Salamanqueja del norte grande|Avistamiento|1|387178|7795155|
|S5|Salamanqueja del norte grande|Avistamiento|1|387188|7795157|

Nota: Coordenadas obtenidas en terreno.

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

7

**6** **METODOLOGÍA**

**6.1** **Modelación de ruido**

La modelación de ruido fue empleada para estimar el nivel de presión acústica que generará el Proyecto en sus
distintas fases.

La metodología se basa en la normativa ISO 9613, que utiliza los principios de atenuación divergente junto a
atenuación extra introducida por obstáculos y propagación a través del aire. Las variables de entrada al modelo de
ruido son las potencias sonoras de las fuentes de ruido que contempla el Proyecto.

El software de simulación computacional utilizado corresponde a SoundPLAN v8.2, el cual permite incorporar una
serie de variables físicas del medio y características acústicas de las fuentes sonoras.

La temperatura se fijó en 10 [oC] y la humedad relativa del aire en 70 [%], constituyendo un escenario desfavorable
por la baja atenuación de la propagación de la onda sonora debido a estos efectos meteorológicos. Además, la
norma de cálculo utilizada considera siempre la velocidad del viento entre 1 y 5 [m/s] [3], en dirección desde las fuentes
de ruido hacia los receptores, es decir, a favor de la propagación. De acuerdo con lo anterior, el escenario modelado
representa una estacionalidad climática crítica.

**Tabla 3: Resumen de entradas y salidas en el proceso de cálculo del modelo SoundPLAN.**

|Col1|Ítem|Col3|Descripción|
|---|---|---|---|
|Entradas<br>(Input)|Topografía|Topografía|Cotas de terreno|
|Entradas<br>(Input)|Ubicación de fuentes de ruido|Ubicación de fuentes de ruido|Puntos, áreas o líneas de emisión|
|Entradas<br>(Input)|Ubicación de receptores|Ubicación de receptores|Puntos de evaluación|
|Entradas<br>(Input)|Obstáculos|Existentes|Cotas de Terreno|
|Entradas<br>(Input)|Obstáculos|Introducidos|-|
|Entradas<br>(Input)|Algoritmo de cálculo|Algoritmo de cálculo|ISO 9613, parte 1 y 2|
|Salidas<br>(Output)|Niveles de Presión Sonora modelados|Niveles de Presión Sonora modelados|Mapas de propagación sonora|
|Salidas<br>(Output)|Niveles de Presión Sonora modelados|Niveles de Presión Sonora modelados|Niveles de Presión Sonora en puntos de inmisión (Receptores)|

La modelación incorporó la maquinaria de mayor emisión de ruido, con lo cual se garantiza que las emisiones sonoras
provenientes de otras actividades (con maquinaria menor) quedarán enmascaradas por la emisión de las fuentes
consideradas.

El plano del Proyecto (otorgado por el mandante) fue ingresado en el modelo acústico, el cual trabaja sobre un
entorno escalado y georreferenciado, de manera que permite mayor exactitud en lo que respecta a distancia y
orientación entre las fuentes de ruido y los receptores en estudio.

3 ISO 9613-2:1996, Meteorological conditions, page 3.

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

8

**7** **DATOS DE ENTRADA AL MODELO PREDICTIVO DE RUIDO**

**7.1** **Fase de construcción**

En primer lugar, como acción inicial para las fases de construcción y cierre, se considera una perturbación controlada
enfocada en las especies de fauna silvestre identificadas con el fin de disminuir la cantidad de individuos en el área
afectada por las actividades del Proyecto, logrando de este modo que ninguno de dichos individuos se encuentre a
menos de 126 metros desde alguna faena, de acuerdo con el AI definida en el acápite 4 bajo un criterio conservador.

Por otro lado, la modelación contempla todas las obras que están asociadas a la construcción de la subestación
seccionadora junto con la instalación de faena asociada a esta fase. Para la ejecución de dichas obras se tiene en
consideración diversa maquinaria pesada.

Las potencias acústicas asignadas a las fuentes de ruido se obtuvieron principalmente a partir de los valores
contenidos en el anexo C de la norma británica BS 5228-1:2009, “ _Code of practice for noise and vibration control on_
_construction and open sites_ ”, los cuales son comparables en magnitud a mediciones realizadas por Gerard Ingeniería
Acústica SpA a maquinarias en proyectos similares.

A continuación, se indica el nivel de emisión acústica asignado a las maquinarias en los distintos frentes de trabajos
a ejecutar para las distintas obras del Proyecto.

 - **Subestación seccionadora**

Movimiento, nivelación y compactación del terreno

**Tabla 4: Niveles de potencia acústica. Maquinaria fase de construcción.**

|Col1|Tabla|a 4: Niveles de potencia acústica. Maquinaria fase de construcció Movimiento, nivelación y comptactación de terreno.|Col4|Col5|Col6|Col7|Col8|Col9|Col10|ón.|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fuente de ruido**|**Cantidad**|**Lw en dB(A) en bandas de octava de frecuencia**|**Lw en dB(A) en bandas de octava de frecuencia**|**Lw en dB(A) en bandas de octava de frecuencia**|**Lw en dB(A) en bandas de octava de frecuencia**|**Lw en dB(A) en bandas de octava de frecuencia**|**Lw en dB(A) en bandas de octava de frecuencia**|**Lw en dB(A) en bandas de octava de frecuencia**|**Lw en dB(A) en bandas de octava de frecuencia**|**Lw**<br>**dB(A)**|**Referencia**|
|**Fuente de ruido**|**Cantidad**|**63**|**125**|**250**|**500**|**1k**|**2k**|**4k**|**8k**|**8k**|**8k**|
|Motoniveladora|1|92.5|95.5|99.5|99.5|97.5|94.5|91.5|86.5|105.2|Ficha técnica*|
|Camión tolva|1|81.8|87.9|92.4|94.8|97.0|95.2|92.0|84.9|102.0|BS 5228 Tabla 02, No 33|
|Excavadora|1|78.8|85.9|90.4|94.8|96.0|95.2|89.0|80.9|101.1|BS 5228 Tabla 02, No 24|
|Cargador frontal|1|84.8|88.9|89.4|94.8|98.0|97.2|93.0|84.9|102.7|BS 5228 Tabla 06, No32|
|Camión aljibe|1|73.0|84.0|86.0|95.0|92.0|95.0|90.0|83.0|99.9|Environmental Noise<br>Monitoring*|
|Rodillo|1|83.8|89.9|86.4|95.8|95.0|93.2|89.0|83.9|100.7|BS 5228 Tabla 02, No 40|
|**Total Foco de Ruido**|**Total Foco de Ruido**|**94**|**98**|**101**|**104**|**104**|**103**|**99**|**92**|**110**||

- Ver Anexo I

Montaje

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

9

**Tabla 5: Niveles de potencia acústica. Maquinaria fase de construcción. Montaje.**

|Fuente de ruido|Cantidad|Lw en dB(A) en bandas de octava de frecuencia|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Lw<br>dB(A)|Referencia|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fuente de ruido**|**Cantidad**|**63**|**125**|**250**|**500**|**1k**|**2k**|**4k**|**8k**|**8k**|**8k**|
|Camión Grúa|2|79.8|80.9|86.4|88.8|90.0|86.2|78.0|66.9|94.6|BS 5228 Tabla 04, No 46|
|Camión tolva|1|81.8|87.9|92.4|94.8|97.0|95.2|92.0|84.9|102.0|BS 5228 Tabla 02, No 33|
|**Total Foco de Ruido**|**Total Foco de Ruido**|**85**|**89**|**94**|**97**|**99**|**96**|**92**|**85**|**103**||

 - **Instalación de faenas**

La instalación de faena considerada para este proyecto contempla la misma cantidad y tipo de maquinaria que la ya
declarada y aprobada en el EIA del proyecto “Orcoma” cuyo detalle forma parte del Anexo 49 de la Adenda [4] . En la
siguiente tabla se indica el nivel de potencia acústica para dicha instalación de faenas.

**Tabla 6: Niveles de potencia acústica. Maquinaria fase de construcción. Instalación de faenas.**

|Fuente de ruido|Lw en bandas de octava de frecuencia|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Lw|Unidad|
|---|---|---|---|---|---|---|---|---|---|---|
|**Fuente de ruido**|**63**|**125**|**250**|**500**|**1k**|**2k**|**4k**|**8k**|**8k**|**8k**|
|Instalación de faenas|90|91|91|91|89|87|84|79|**98**|**dB(A)**|

La maquinaria indicada en las tablas anteriores no opera de forma simultánea, sino que de manera secuencial o en
pequeños grupos de trabajo. De todos modos, con la finalidad de representar un escenario conservador, se simuló
el funcionamiento del equipamiento asociado a uno de los frentes de mayor emisión sonora para cada obra y/o
sector, correspondiente a: 1) “Movimiento, nivelación y compactación de terreno” para la subestación seccionadora,
con un nivel de potencia acústica de 110 [dB(A)] y 2) toda la maquinaria asociada al sector de la instalación de
faenas, con un nivel de potencia acústica de 98 [dB(A)].

Para la fase de cierre se considera que la maquinaria será de igual o menor magnitud, por tanto, el análisis aquí
contenido es representativo también de dicha fase.

**7.2** **Fase de operación**

Las principales fuentes de ruido para efectos del análisis acústico de la fase de operación del proyecto están
asociadas al funcionamiento de un transformador de 50 [MVA], un generador eléctrico de respaldo de 150 [kW] y a
la presencia de 2 camionetas (únicamente cuando se realicen labores de mantención).

Para calcular el nivel de emisión del transformador, se utilizaron las siguientes expresiones matemáticas [5]

L w = N R + 10 log 10 ( S ) + C ( dBre 10 [−12] W ) **Ecuación 2**

4 Adenda EIA Orcoma - Anexo 49: Estimación de emisiones de ruido y vibraciones
5 Crocker, Malcolm J. - Handbook of Noise and Vibration Control, 2007.

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

10

10 log 10 ( S ) = 14 + 2.5 log 10 ( W e ) **Ecuación 3**

N R = 55 + 12 log 10 ( W e )
para un transformador estándar (sin silenciador)

**Ecuación 5**

Donde:

L w : Nivel de Potencia Acústica estimado [dB(A)],
N R : Rangos de nivel de ruido ( _Sound Level Rating_ s)
W e : Potencia Eléctrica [MVA] [6], y
C : Factor de corrección para cálculo de espectro de frecuencia (Tabla 7).

|Tabla 7: Factor de corrección C para ecuación de cálculo para ruido de transformadores en [dB(Z)] 7|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Correcciones en bandas de octava de frecuencia [Hz]**|**Correcciones en bandas de octava de frecuencia [Hz]**|**Correcciones en bandas de octava de frecuencia [Hz]**|**Correcciones en bandas de octava de frecuencia [Hz]**|**Correcciones en bandas de octava de frecuencia [Hz]**|**Correcciones en bandas de octava de frecuencia [Hz]**|**Correcciones en bandas de octava de frecuencia [Hz]**|**Correcciones en bandas de octava de frecuencia [Hz]**|
|**63**|**125**|**250**|**500**|**1k**|**2k**|**4k**|**8K**|
|-3|-5|0|0|6|11|16|23|

La siguiente tabla indica el L w correspondiente a los parámetros utilizados en los cálculos (W e =50 [MVA] con N R =75.4

[dB(A)]).

**Tabla 8: Nivel de potencia acústica del transformador a utilizar durante la fase de operación.**

|Fuente|Cantidad|Lw [dB(A)] en bandas de octava de frecuencia [Hz]|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Lw<br>[dB(A)]<br>c/u|Fuente|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fuente**|**Cantidad**|**63**|**125**|**250**|**500**|**1k**|**2k**|**4k**|**8K**|**8K**|**8K**|
|Transformador<br>50 [MVA]|1|70.4|82.5|85.0|90.4|87.6|83.8|78.6|69.5|94.0|Crocker, Malcolm J. - Handbook of<br>Noise and Vibration Control, 2007|

Finalmente, para el caso del generador eléctrico y las camionetas se tienen los siguientes niveles de potencia
acústica:

**Tabla 9: Nivel de potencia acústica del transformador a utilizar durante la fase de operación.**

|Fuente|Cantidad|Lw [dB(A)] en bandas de octava de frecuencia [Hz]|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Lw<br>[dB(A)] c/u|Fuente|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fuente**|**Cantidad**|**63**|**125**|**250**|**500**|**1k**|**2k**|**4k**|**8K**|**8K**|**8K**|
|Camionetas|2|69.1|77.7|77.3|83.5|93.0|94.0|92.1|85.6|98.3|SoundPLAN 8.2 database*|
|GE 150 kW|1|62.5|73.6|81.1|86.5|87.7|86.9|83.7|76.6|92.9|Bies, Hansen|

*Ver Anexo I

**7.3** **Fase de cierre**

Tal como se mencionó anteriormente, para la fase de cierre se utilizará, en igual o menor cantidad, maquinaria similar
a la utilizada en la fase de construcción, por lo que no existirá una mayor emisión de ruido. Así mismo, se consideran
las mismas acciones de perturbación controlada para la fauna silvestre indicadas en la fase de construcción.

6 MVA: Abreviatura de Megavoltampere, unidad de potencia eléctrica.
7 Crocker, Malcolm J. - Handbook of Noise and Vibration Control, 2007.

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

11

Producto de lo anterior, sólo será necesario evaluar el caso más desfavorable el cual estará dado por la fase de
construcción.

**8** **RESULTADOS**

**8.1** **Modelación y evaluación de ruido**

**8.1.1** **Fase de construcción**

A continuación, se presenta el nivel de inmisión acústica preliminar estimado para la fase de construcción en cada
punto de evaluación. Los valores se presentan en formato de tabla y mapas de propagación sonora, cuya altura de
coloración está referida a 10 [cm] del suelo.

**Ilustración 4: Mapa** **de** **propagación sonora** **según NPSeq** **en [dB(A)]. Fase** **de** **construcción.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

12

**Tabla 10: Evaluación de cumplimiento fase de construcción.**

|Punto|NPS proyectado [dB(A)]*<br>eq|Máximo permitido [dB(A)]|Evaluación|
|---|---|---|---|
|~~D1~~|~~48~~|60|~~No supera~~|
|S1|48|48|No supera|
|S2|44|44|No supera|
|S3|51|51|No supera|
|S4|51|51|No supera|
|S5|51|51|No supera|

*Valores aproximados al entero más cercano.

En la evaluación anterior se aprecia que en todos los puntos de evaluación no se supera el umbral seleccionado de
60 [dB(A)].

**8.1.2** **Fase de operación**

Se presentan a continuación los niveles de presión acústica modelados para la fase de operación. Los valores se
presentan en formato de tabla y mapas de propagación sonora, cuya altura de coloración está referida a 10 [cm] del
suelo.

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

13

**Ilustración 5: Mapa** **de** **propagación sonora** **según NPSeq** **en [dB(A)]. Fase** **de** **operación.**

Elaboración: Gerard Ingeniería Acústica SpA 2022.

**Tabla 11: Evaluación de cumplimiento fase de operación.**

|Punto|NPS proyectado [dB(A)]*<br>eq|Máximo permitido [dB(A)]|Evaluación|
|---|---|---|---|
|D1|41|60|No Supera|
|S1|44|44|No Supera|
|S2<br>|57<br>|57<br>|No Supera<br>|
|~~S3~~|~~39~~|~~39~~|~~No Supera~~|
|S4|38|38|No Supera|
|S5|38|38|No Supera|

*Valores aproximados al entero más cercano.

En la evaluación anterior se aprecia que los niveles de ruido proyectados para la fase de operación no superan el
umbral de evaluación seleccionado en todos los puntos de evaluación.

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

14

**9** **CONCLUSIONES**

Se realizaron modelaciones de ruido en los sectores cercanos al futuro emplazamiento del proyecto “ _Subestación_
_Seccionadora 220/33 kV Orcoma_ ”, ubicado en la comuna de Huara, Región de Tarapacá, para los seis (6) puntos en
los cuales se identificó fauna silvestre que pudiese verse afectada por los niveles de ruido que generará el mismo.

El análisis acústico del proyecto utilizó un modelo de ruido asistido por el software SoundPLAN v8.2, el cual permitió
estimar el nivel de ruido generado por la maquinaria involucrada en las fases de construcción, operación y cierre del
Proyecto. En particular para las fases de construcción y cierre se contemplaron desde un inicio acciones de
perturbación controlada para el ahuyentamiento de las especies con tal de que estas no se encuentren a una
distancia menor a 126 metros desde alguna faena.

Los niveles ruido obtenidos fueron evaluados de acuerdo con el umbral de 60 [dB(A)] sugerido por el “California
Department of Transportation” de EE. UU., verificándose que no existen superaciones al umbral sugerido tanto en la
fase de construcción, así como en las fases de operación y cierre.

En virtud de todo lo anteriormente señalado, se asume que el proyecto no generará una afectación acústica
significativa en la fauna silvestre cercana al emplazamiento de este.

**C** **LAUDIO** **S** **ALAS** **C** **ASTRO**
I NGENIERO C IVIL EN S ONIDO Y A CÚSTICA
G ERENTE DE P ROYECTOS

**G** **ERARD** **I** **NGENIERÍA** **A** **CÚSTICA** **S** **P** **A.**

**M** **AX** **G** **LISSER** **D** **ONOSO**
I NGENIERO C IVIL EN S ONIDO Y A CÚSTICA
G ERENTE T ÉCNICO

**G** **ERARD** **I** **NGENIERÍA** **A** **CÚSTICA** **S** **P** **A.**

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

15

**10** **BIBLIOGRAFÍA UTILIZADA**

 - ISO 9613-2:1996, _Attenuation of sound during propagation outdoors_ .

 - Software Designers & Consulting Engineers for Noise Control & Environmental Protection _SoundPLAN_ - User
Manual.

 - Samir N. Y. Gerges, Ruido, Fundamentes y control, Primera edición en español, 1998.

 - BS 5228-1:2009, “ _Code of practice for noise and vibration control on construction and open sites_ ”.

 Guía para la predicción y evaluación de impactos por ruido y vibración en el SEIA, del Servicio de Evaluación
Ambiental (SEA), 2019.

 Guía de Evaluación Ambiental: Componente Fauna Silvestre D-RNN-EIA-PR-001 publicada por el SAG del
Ministerio de Agricultura en 2019.

 Revisión bibliográfica, síntesis y propuesta. Umbrales de ruido y respuestas biológicas en fauna, con énfasis
en aves. Geobiota, segunda Adenda complementaria en el EIA del proyecto “Tente en el Aire” en su Anexo

11.

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

16

|11 PROFESIONALES PARTICIPANTES|Col2|
|---|---|
|**LISTADO DE PROFESIONALES**|**LISTADO DE PROFESIONALES**|
|**Jefe de Proyecto**|Ismael Gómez Schmidt|
|**Gerente de proyectos**|Claudio Salas Castro|
|**Gerente Técnico**|Max Glisser Donoso|
|**Gerente General**|Christian Gerard Büchi|
|**Asistente(s) de Proyecto**|--|
|||

**12** **GLOSARIO**

a) **Decibel [dB]:** Unidad adimensional usada para expresar 10 veces el logaritmo de la razón entre una
cantidad medida y una cantidad de referencia.

b) **Decibel A [dB(A)]:** Es la unidad adimensional usada para expresar el nivel de presión sonora, medido con
el filtro de ponderación de frecuencias A.

c) **Fuente emisora de ruido:** Toda actividad, proceso, operación o dispositivo que genere, o pueda generar,
emisiones de ruido hacia la comunidad.

d) **Nivel de Presión Sonora (NPS ó L** **p** **):** Se expresa en decibeles [dB] y se define por la siguiente relación
matemática:

NPS = 20 ∙ log 10
൬ [P] P [1] ~~[൰]~~

Donde:
P 1 : Valor efectivo de la presión medida
P : Valor efectivo de la presión sonora de referencia, fijada en 2×10 [-5] [N/m [2] ]

e) **Nivel de Presión Sonora Continuo Equivalente (NPSeq):** Es aquel nivel de presión sonora constante,
expresado en decibeles A, que en el mismo intervalo de tiempo, contiene la misma energía total (o dosis)
que el ruido medido.

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

17

# ANEXO I REFERENCIAS POTENCIA ACÚSTICA

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

18

- **Motoniveladora:**

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

19

- **Camionetas**

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

20

 **Camión aljibe**

El nivel de potencia acústica se obtuvo del estudio “Environmental Noise Monitoring” [8] realizado por Umwelt
(Australia) Pty Limited para Mackas Sand. El nivel de potencia acústica se puede apreciar a continuación destacado
con rojo.

8 http://www.mackassand.com.au/compliance/files/R28_January2011_%20NoiseMonitoring_V1.pdf

E STUDIO A CÚSTICO EN F AUNA
S UBESTACIÓN S ECCIONADORA 220/33 K V O RCOMA - R EV . D

21