---
title: Sin título
author: Ambiental2
date: D:20171115193012-03'00'
language: es
type: report
pages: 48
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO N°1.4 ESTUDIO DE RUIDO Y ESTUDIO DE RUIDO Y VIBRACIONES VIBRACIONES
-->

ANEXO N°1.4

# ANEXO N°1.4 ESTUDIO DE RUIDO Y ESTUDIO DE RUIDO Y VIBRACIONES VIBRACIONES

#### PROYECTO SUBESTACIÓN SECCIONADORA NUEVA POZO ALMONTE 220 KV

## RED ELÉCTRICA DEL NORTE S.A.

Elaborado por:

**Noviembre, 2017**

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

##### ANEXO N°1.4 ESTUDIO DE RUIDO Y VIBRACIONES

**DIA PROYECTO SUBESTACIÓN SECCIONADORA**

**NUEVA POZO ALMONTE 220 KV**

**ÍNDICE**

1. INTRODUCCIÓN ....................................................................................................... 5

2. OBJETIVOS ............................................................................................................... 6

3. MARCO REGULATORIO ........................................................................................... 6

3.1. Ruido .................................................................................................................. 6

3.2. Vibraciones ......................................................................................................... 7

4. IDENTIFICACIÓN DE RECEPTORES ....................................................................... 8

4.1. Descripción ......................................................................................................... 8

4.2. Medición de Niveles Basales de Ruido ............................................................. 14

4.2.1. Metodología ............................................................................................... 14

4.2.2. Instrumentos de Medición .......................................................................... 15

4.2.3. Resultados ................................................................................................. 15

5. MODELACIÓN EMISIONES DE RUIDO .................................................................. 17

5.1. Descripción del Proyecto .................................................................................. 17

5.2. Fuentes de Ruido.............................................................................................. 19

5.2.1. Fase de Construcción ................................................................................ 19

5.2.2. Fase de Operación .................................................................................... 20

5.2.3. Fase de Cierre ........................................................................................... 20

5.3. Software de Simulación de Ruido ..................................................................... 20

5.4. Resultados ........................................................................................................ 20

5.4.1. Fase de Construcción ................................................................................ 20

5.4.2. Fase de Operación .................................................................................... 23

6. ESTIMACIÓN DE VIBRACIONES............................................................................ 25

6.1. Vibraciones en Fase de Construcción ............................................................... 25

6.2. Vibraciones Fase de Operación ........................................................................ 25

6.3. Metodología ...................................................................................................... 25

6.4. Resultados ........................................................................................................ 26

_**2**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

7. EVALUACIÓN DE RESULTADOS ............................................................................ 27

7.1. Ruido ................................................................................................................. 27

7.1.1. Fase de Construcción ................................................................................. 27

7.1.2. Fase de Operación ..................................................................................... 28

7.2. Vibraciones ........................................................................................................ 28

7.2.1. Fase de Construcción ................................................................................. 28

7.2.2. Operación ................................................................................................... 29

8. Medidas de Control ................................................................................................... 29

9. RESUMEN EJECUTIVO ........................................................................................... 30

10. CONCLUSIONES ................................................................................................. 31

**ÍNDICE DE FIGURAS**

Figura 1: Área del Proyecto y Puntos receptores ...............................................................9

Figura 2: Comparación Niveles Basales de Ruido, Diurno / Nocturno .............................. 16

Figura 3: Layout del Proyecto .......................................................................................... 17

Figura 4: Mapa de ruido - Fase Construcción ................................................................. 21

Figura 5: Mapa de ruido sobre imagen satelital - Fase Construcción .............................. 22

Figura 6: Mapa de Ruido- Fase de Operación................................................................. 24

_**3**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**ÍNDICE DE TABLAS**

Tabla 1: Límite Normativo D.S. N° 38/11 del MMA ............................................................ 7

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Los niveles de presión sonora corregidos que se obtengan de la emisión de una fuente emisora de ruido, medidos en el lugar donde se encuentre el receptor, no podrán exceder los valores que se fijan a continuación: -->

**Tabla 1: Límite Normativo D.S. N° 38/11 del MMA****

| Niveles Máximos Permisibles de Presión<br>Sonora Corregidos (NPC) en dB(A) Lento | Col2 | Col3 |
| --- | --- | --- |
|  | de 7 a 21 Hrs. | de 21 a 7 Hrs. |
| Zona I | 55 | 45 |
| Zona II | 60 | 45 |
| Zona III | 65 | 50 |
| Zona IV | 70 | 70 |

<!-- Estadísticas: 5 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- En las áreas rurales, los niveles de presión sonora corregidos que se obtengan de la emisión de una fuente emisora de ruido, medidos en el lugar donde se encuentre el receptor, no podrán superar el menor valor entre el Nivel de ruido de fondo + 10 dB(A) y el NPC para zona III de la Tabla 1 (65 dB(A) diurno y 50 dB(A) nocturno). -->
<!-- FIN TABLA 1 -->


Tabla 2: Criterio FTA para evaluación daño estructural por vibraciones ............................ 8

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Nueva Pozo Almonte 220 KV de partículas para daño estructural para construcciones livianas de madera y edificios de mampostería, por corresponder a un escenario desfavorable para el Proyecto. -->

**Tabla 2: Criterio FTA para evaluación daño estructural por vibraciones****

| Col1 | Categoría de edificación | PPV<br>(pulgadas/segundo) |
| --- | --- | --- |
| 1 | Hormigón armado, acero o madera (sin yeso) | 0,5 |
| 2 | Ingeniería de hormigón y albañilería (sin yeso) | 0,3 |
| 3 | Construcciones livianas de madera y edificios<br>de mampostería | 0,2 |
| 4 | Edificios extremadamente susceptibles a daño<br>por vibración | 0,12 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: “Transit Noise and Vibration - Impact Assesment” de la Federal Transit Administration (FTA) de Estados Unidos (2006). -->
<!-- FIN TABLA 2 -->


Tabla 3: Puntos de Evaluación de Ruido y Vibraciones .................................................. 10

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Subestación Seccionadora Nueva Pozo Almonte 220 KV -->

**Tabla 3: Puntos de Evaluación de Ruido y Vibraciones****

| PUNTO: | SE-01 | UTM E: | 421.207 | UTM N: | 7.752.702 | Distancia<br>a SE:: | 1.092 m |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665. | **DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665. | **DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665. | **DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665. | **DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665. | **DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665. | **DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665. | **DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665. |

<!-- Estadísticas: 3 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- _**10**_ Subestación Seccionadora -->
<!-- FIN TABLA 3 -->


Tabla 4: Descripción Puntos complementarios (Sitios Arqueológicos) ............................ 14

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Subestación Seccionadora Nueva Pozo Almonte 220 KV -->

**Tabla 4: Descripción Puntos complementarios (Sitios Arqueológicos)****

| PUNTO: | P-05 | UTM E: | 421.898 | UTM N: | 7.752.458 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
| **PUNTO:** | P-07 | **UTM E**: | 4242.20 | **UTM N**: | 7.754.900 |
|  |  |  |  |  |  |

<!-- Estadísticas: 3 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- **4.2. Medición de Niveles Basales de Ruido** **4.2.1. Metodología** -->
<!-- FIN TABLA 4 -->


Tabla 5: Niveles Basales de Ruido, Período Diurno ........................................................ 15

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la siguiente tabla se muestran los Niveles de Presión Sonora Equivalentes (NPSeq) y los NPS mínimos y máximos obtenidos en dichas mediciones, y además, se indican las fuentes de ruido presentes en cada punto receptor: -->

**Tabla 5: Niveles Basales de Ruido, Período Diurno****

| Receptor | NPSeq<br>[dB(A)] | NPSmín<br>[dB(A)] | NPSmáx<br>[dB(A)] | Fuentes de ruido |
| --- | --- | --- | --- | --- |
| SE -01 | **60** | 28,0 | 76,5 | Tránsito vehicular lejano, aves,<br>ladrido de perros lejanos. |
| SE - 02 | **45** | 29,1 | 55,4 | Tránsito vehicular lejano, aves. |
| SE - 03 | **40** | 27,8 | 50,4 | Viento, ladrido de perros lejano,<br>tránsito vehicular lejano. |
| RA - 06 | **46** | 39,6 | 59,2 | Viento, tránsito lejano, actividades<br>en receptores. |

<!-- Estadísticas: 4 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Como se observa, los niveles de ruido en período diurno fluctúan entre 40 y 60 dB(A), con mínimos entre 28 y 29 dB(A) y máximos entre 50 y 77 dB(A), donde la principal fuente de ruido es el tránsito vehicular lejano por Ruta 5 Norte. -->
<!-- FIN TABLA 5 -->


Tabla 6: Niveles Basales de Ruido, Período Nocturno .................................................... 16

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Subestación Seccionadora Nueva Pozo Almonte 220 KV -->

**Tabla 6: Niveles Basales de Ruido, Período Nocturno****

| Receptor | NPSeq<br>[dB(A)] | NPSmín<br>[dB(A)] | NPSmáx<br>[dB(A)] | Fuentes de ruido |
| --- | --- | --- | --- | --- |
| SE - 01 | **53** | 23,7 | 70,5 | Tránsito vehicular lejano, ladrido de<br>perros lejanos. |
| SE - 02 | **35** | 23,0 | 58,5 | Tránsito vehicular lejano. |
| SE - 03 | **29** | 21,4 | 35,2 | Tránsito vehicular lejano. |
| RA - 06 | **43** | 32,3 | 71,3 | Tránsito vehicular lejano. |

<!-- Estadísticas: 4 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Como se observa, los niveles de ruido en período diurno fluctúan entre 29 y 53 dB(A), con mínimos entre 21 y 24 dB(A) y máximos entre 35 y 71 dB(A), donde la principal fuente de ruido es el tránsito vehicular lejano por Ruta 5 Norte. -->
<!-- FIN TABLA 6 -->


Tabla 7: Cronograma del Proyecto .................................................................................. 18

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Subestación Seccionadora Nueva Pozo Almonte 220 KV -->

**Tabla 7: Cronograma del Proyecto****

| Actividades | Meses | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividades** | **1 ** | **2 ** | **3 ** | **4 ** | **5 ** | **6 ** | **7 ** | **8 ** | **9** | **10** | **11** | **12** |
| Habilitación camino de acceso |  |  |  |  |  |  |  |  |  |  |  |  |
| Implementación instalación de faenas |  |  |  |  |  |  |  |  |  |  |  |  |
| **_Sector Subestación y Ampliación (Patio 220 kV)_** | **_Sector Subestación y Ampliación (Patio 220 kV)_** | **_Sector Subestación y Ampliación (Patio 220 kV)_** | **_Sector Subestación y Ampliación (Patio 220 kV)_** | **_Sector Subestación y Ampliación (Patio 220 kV)_** | **_Sector Subestación y Ampliación (Patio 220 kV)_** | **_Sector Subestación y Ampliación (Patio 220 kV)_** | **_Sector Subestación y Ampliación (Patio 220 kV)_** | **_Sector Subestación y Ampliación (Patio 220 kV)_** | **_Sector Subestación y Ampliación (Patio 220 kV)_** | **_Sector Subestación y Ampliación (Patio 220 kV)_** | **_Sector Subestación y Ampliación (Patio 220 kV)_** | **_Sector Subestación y Ampliación (Patio 220 kV)_** |
| Instalación cercos perimetrales |  |  |  |  |  |  |  |  |  |  |  |  |
| Preparación de la superficie (escarpe) |  |  |  |  |  |  |  |  |  |  |  |  |
| Preparación de la superficie (excavaciones) |  |  |  |  |  |  |  |  |  |  |  |  |
| Fundaciones |  |  |  |  |  |  |  |  |  |  |  |  |
| Construcción camino interior |  |  |  |  |  |  |  |  |  |  |  |  |
| Construcción edificio de control |  |  |  |  |  |  |  |  |  |  |  |  |
| Montaje de estructuras de equipos |  |  |  |  |  |  |  |  |  |  |  |  |
| Instalaciones eléctricas |  |  |  |  |  |  |  |  |  |  |  |  |
| Limpieza y compactación Área de Ampliación |  |  |  |  |  |  |  |  |  |  |  |  |
| **_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_** | **_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_** | **_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_** | **_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_** | **_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_** | **_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_** | **_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_** | **_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_** | **_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_** | **_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_** | **_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_** | **_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_** | **_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_** |
| Preparación de la superficie |  |  |  |  |  |  |  |  |  |  |  |  |
| Fundaciones |  |  |  |  |  |  |  |  |  |  |  |  |
| Montaje de Estructuras |  |  |  |  |  |  |  |  |  |  |  |  |
| Tendido y templado de Conductor |  |  |  |  |  |  |  |  |  |  |  |  |
| Puesta en Servicio |  |  |  |  |  |  |  |  |  |  |  |  |

<!-- Estadísticas: 19 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Descripción del Proyecto (DIA). Durante la Fase de Construcción el horario de trabajo en el área de la Subestación será -->
<!-- FIN TABLA 7 -->


Tabla 8: Niveles de Presión Sonora de maquinaria - Fase Construcción ....................... 19

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la siguiente tabla, se indica la maquinaria que se utilizará durante la Fase de Construcción y se detallan los Niveles de Presión Sonora (NPS) de emisión de cada fuente, a 10 metros, y sus niveles en bandas de octava de frecuencia. -->

**Tabla 8: Niveles de Presión Sonora de maquinaria - Fase Construcción****

| Referencia<br>BS5228 | Col2 | Fuente de ruido | Frecuencia en Hz, niveles en dB | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | dB(A)<br>a 10 m |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tabla** | **N°** | **N°** | **63** | **125** | **250** | **500** | **1k** | **2k** | **4k** | **8k** | **8k** |
| _C2_ | _2 _ | Excavadora | 75 | 84 | 78 | 74 | 70 | 68 | 64 | 61 | **77** |
| C2 | 8 | Retroexcavadora | 76 | 66 | 64 | 64 | 63 | 60 | 59 | 50 | **68** |
| _Medición del_<br>_Consultor_ | _Medición del_<br>_Consultor_ | Motoniveladora | 72 | 68 | 63 | 55 | 55 | 52 | 48 | -- | **61** |
| _C4_ | _16_ | Camión Pluma | 75 | 70 | 67 | 67 | 69 | 66 | 60 | 53 | **72** |
| _Medición del_<br>_Consultor_ | _Medición del_<br>_Consultor_ | Placa compactadora | 67 | 62 | 59 | 59 | 61 | 58 | 52 | 45 | **64** |
| _C4_ | _26_ | Camión mixer+ Bomba<br>hormigón | 75 | 76 | 71 | 70 | 71 | 68 | 64 | 60 | **75** |
| _C4_ | _16_ | Camión estanque | 75 | 70 | 67 | 67 | 69 | 66 | 60 | 53 | **72** |
| _Medición del_<br>_consultor_ | _Medición del_<br>_consultor_ | Camioneta | 62 | 49 | 42 | 44 | 47 | 43 | 40 | -- | **50** |
| _C4_ | _3 _ | Camión Tolva | 84 | 81 | 74 | 73 | 72 | 68 | 61 | 53 | **76** |
| _C4_ | _16_ | Camión Rampla | 75 | 70 | 67 | 67 | 69 | 66 | 60 | 53 | **72** |
| _C2_ | _38_ | Rodillo Compactador | 80 | 75 | 77 | 72 | 67 | 62 | 54 | 46 | **73** |
| **Total** | **Total** | **Total** | **88** | **87** | **82** | **80** | **79** | **75** | **70** | **65** | **83** |

<!-- Estadísticas: 13 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Norma Británica BS 5228-1:2009: “ _Code of practice for noise and vibration control on construction and open_ _sites - Part 1: Noise_ ” o mediciones de Consultor cuando se indica cuyo detalle se presenta en Anexo 2 -->
<!-- FIN TABLA 8 -->


Tabla 9: Nivel de Potencia Sonora Fuentes de ruido - Etapa de Operación ................... 20

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **5.2.2. Fase de Operación** Las fuentes de ruido consideradas en la modelación y su nivel de emisión en términos del nivel de Potencia Sonora en dB(A) se presentan en la siguiente tabla: -->

**Tabla 9: Nivel de Potencia Sonora Fuentes de ruido - Etapa de Operación****

| Fuente | Frecuencia en Hz, NWS en dB(A) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | NWS<br>[dB(A)] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | _63_ | _125_ | _250_ | _500_ | _1K_ | _2K_ | _4K_ | _8K_ | _8K_ |
| Subestación Eléctrica de<br>Referencia | 96 | 103 | 95 | 85 | 77 | 75 | 73 | 64 | **104** |
| Efecto Corona Líneas<br>eléctricas de Alta tensión | -- | 83 | 80 | 78 | 80 | 81 | 81 | -- | 88 |

<!-- Estadísticas: 3 filas, 10 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Mediciones del Consultor en proyectos similares. Ver detalles en Anexo 2. **5.2.3. Fase de Cierre** -->
<!-- FIN TABLA 9 -->


Tabla 10: Niveles de Ruido Modelados - Fase Construcción .......................................... 22

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 5: Mapa de ruido sobre imagen satelital - Fase Construcción** La tabla siguiente resume los niveles de ruido estimados en los puntos receptores para la Fase de Construcción del Proyecto: -->

**Tabla 10: Niveles de Ruido Modelados - Fase Construcción****

| Punto | NPS Modelado [dB(A)] |
| --- | --- |
| SE-01 | 42 |
| SE-02 | 51 |
| SE-03 | 36 |
| RA-06 | 42 |

<!-- Estadísticas: 4 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Modelación con Software Predictor Lima V11.21 Es posible establecer que los niveles obtenidos para el escenario de modelación que simula la construcción del Proyecto fluctúan entre 36 y 51 dB(A). -->
<!-- FIN TABLA 10 -->


Tabla 11: Niveles de ruido - Fase de Operación ............................................................. 23

<!-- INICIO TABLA 11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- niveles de emisión indicados en la Tabla 9. En la siguiente tabla se resumen los niveles estimados mediante el software de modelación en los puntos receptores para la Fase de Operación: -->

**Tabla 11: Niveles de ruido - Fase de Operación****

| Punto | NPS Modelado [dB(A)] |
| --- | --- |
| SE-01 | **24** |
| SE-02 | **23** |
| SE-03 | **19** |
| RA-06 | **8 ** |

<!-- Estadísticas: 4 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Modelación con Software Predictor Lima V11.21 Es posible establecer que los niveles obtenidos en los puntos receptores asociados a la operación del Proyecto fluctúan entre 8 y 24 dB(A). -->
<!-- FIN TABLA 11 -->


Tabla 12: Fuentes de Vibración - Fase de Construcción ................................................. 25

<!-- INICIO TABLA 12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Peak de Partícula (PPV) para las maquinarias que contempla la construcción del Proyecto. Dichos niveles son extraídos del documento de la FTA señalado en el punto 3.2 y corresponden a mediciones efectuadas a 25 pies de distancia (7,6 m aprox.). -->

**Tabla 12: Fuentes de Vibración - Fase de Construcción****

| Maquinaria | PPV a 25 pies (7,62m) | VdB |
| --- | --- | --- |
| **Maquinaria** | **pulgadas/seg.** | **(ref. 10^-6 pulg./seg.)** |
| Excavadora | 0,089 | 87 |
| Retroexcavadora | 0,089 | 87 |
| Motoniveladora | 0,089 | 87 |
| Camión Pluma | 0,076 | 86 |
| Placa compactadora | 0,089 | 87 |
| Camión mixer+ Bomba<br>hormigón | 0,76 | 106 |
| Camión estanque | 0,076 | 86 |
| Camión Tolva | 0,076 | 86 |
| Camión Rampla | 0,076 | 86 |
| Rodillo Compactador | 0,21 | 94 |
| **TOTAL PPV a 25 pies (7,6m)** | **0,324** | **98,2** |

<!-- Estadísticas: 12 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **6.2. Vibraciones Fase de Operación** Para la Fase de Operación, dadas las características del Proyecto, no se esperan impactos relacionados con la operación de la Subestación ni líneas eléctricas. -->
<!-- FIN TABLA 12 -->


Tabla 13: Resultados Estimación de Vibraciones - Fase de Construcción ..................... 26

<!-- INICIO TABLA 13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **6.4. Resultados** En la siguiente tabla se presentan los resultados obtenidos de la estimación de Vibraciones. -->

**Tabla 13: Resultados Estimación de Vibraciones - Fase de Construcción****

| Receptor | Distancia a frente trabajo [m] | PPV Proyectado [pulgadas/s] |
| --- | --- | --- |
| SE-01 | 980 | **0,00022** |
| SE-02 | 140 | **0,11714** |
| SE-03 | 1.679 | **0,00010** |
| RA-06 | 294 | **0,00135** |
| P-05 | 768 | **0,00032** |
| P-07 | 2.642 | **0,00005** |

<!-- Estadísticas: 6 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia Como se aprecia, el unico punto cercano a las obras es el SE-02 que en particular se -->
<!-- FIN TABLA 13 -->


Tabla 14: Límites Máximos Permisibles .......................................................................... 27

<!-- INICIO TABLA 14 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- los ambientes sonoros en los que se emplazan los receptores, para efectos de evaluación se establecen los límites máximos permisibles que se detallan en la siguiente tabla en base a los resultados del levantamiento basal como representativos del ruido de fondo. -->

**Tabla 14: Límites Máximos Permisibles****

| Receptor | Ruido de Fondo<br>NPSeq [dB(A)] | Col3 | RF+10 dB | Col5 | Límites Zona III | Col7 | Límite Máximo<br>Permisible | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Diurno** | **Nocturno** | **Diurno** | **Nocturno** | **Diurno** | **Nocturno** | **Diurno** | **Nocturno** |
| **SE -01** | 60 | 53 | 70 | 63 | 65 | 50 | **65** | **50** |
| **SE - 02** | 45 | 35 | 55 | 45 | 45 | 45 | **55** | **45** |
| **SE - 03** | 40 | 29 | 50 | 39 | 39 | 39 | **50** | **39** |
| **RA - 06** | 46 | 43 | 56 | 53 | 53 | 53 | **56** | **50** |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **7.1.1. Fase de Construcción** Para efectos de evaluación de esta Fase, se consideran los Niveles de Presión Sonora -->
<!-- FIN TABLA 14 -->


Tabla 15: Evaluación normativa - Fase de Construcción ................................................. 28

<!-- INICIO TABLA 15 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Subestación Seccionadora Nueva Pozo Almonte 220 KV -->

**Tabla 15: Evaluación normativa - Fase de Construcción****

| Receptor | Altura [m] | Nivel Modelado<br>Fase de<br>Construcción | Limite | Exceso de<br>nivel [dB] | ¿Cumple<br>Norma? |
| --- | --- | --- | --- | --- | --- |
| SE-01_A | 1,5 | 42 | 65 | 0 | **SI** |
| SE-02_A | 1,5 | 51 | _No aplica (deshabitado)_ | _No aplica (deshabitado)_ | _No aplica (deshabitado)_ |
| SE-03_A | 1,5 | 36 | 50 | 0 | **SI** |
| RA-06_A | 1,5 | 42 | 56 | 0 | **SI** |

<!-- Estadísticas: 4 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Se puede observar que en esta Fase se cumple con los niveles máximos dispuestos en el D.S. N° 38/11 del MMA en los todos los puntos receptores. -->
<!-- FIN TABLA 15 -->


Tabla 16: Evaluación normativa - Fase de Operación ..................................................... 28

<!-- INICIO TABLA 16 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la siguiente tabla se evalúan los niveles estimados para la Fase de Operación del Proyecto considerando el horario nocturno de modo de garantizar el cumplimiento de los límites más restrictivos. -->

**Tabla 16: Evaluación normativa - Fase de Operación****

| Receptor | Altura<br>[m] | Nivel Modelado<br>Fase Operación<br>[dB(A)] | Límite normativo<br>(horario nocturno)<br>[dB(A)] | Exceso de<br>nivel [dB] | ¿Cumple<br>Norma? |
| --- | --- | --- | --- | --- | --- |
| SE-01_A | 1,5 | **24** | 50 | 0 | **SÍ** |
| SE-02_A | 1,5 | _23_ | _No aplica (deshabitado)_ | _No aplica (deshabitado)_ | _No aplica (deshabitado)_ |
| SE-03_A | 1,5 | **19** | 39 | 0 | **SÍ** |
| RA-06_A | 1,5 | **8 ** | 50 | 0 | **SÍ** |

<!-- Estadísticas: 4 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Se puede observar que los puntos evaluados cumplen con el límite máximo establecido por el D.S.38/11 del Ministerio del Medio Ambiente. -->
<!-- FIN TABLA 16 -->


Tabla 17: Evaluación Criterio FTA Vibraciones - Fase de Construcción ......................... 29

<!-- INICIO TABLA 17 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Nueva Pozo Almonte 220 KV De acuerdo con lo anterior, en la siguiente tabla se presenta la evaluación para todos los receptores considerando la menor distancia a los frentes de potencial emisión de vibraciones. -->

**Tabla 17: Evaluación Criterio FTA Vibraciones - Fase de Construcción****

| Receptor | Distancia a frente<br>trabajo [m] | PPV Proyectado<br>[pulgadas/s] | Límite PPV<br>[pulgadas/s] | ¿Cumple? |
| --- | --- | --- | --- | --- |
| SE-01 | 980 | **0,00022** | 0,2 | **Sí** |
| SE-02 | 140 | **0,11714** | 0,2 | **Sí** |
| SE-03 | 1679 | **0,00010** | 0,2 | **Sí** |
| RA-06 | 294 | **0,00135** | 0,2 | **Sí** |
| P-05 | 768 | **0,00032** | 0,2 | **Sí** |
| P-07 | 2642 | **0,00005** | 0,2 | **Sí** |

<!-- Estadísticas: 6 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Como se puede apreciar, para todos los receptores se demuestra el cumplimiento del criterio de evaluación adoptado, inclusive sobre el punto SE-02 que se ubica a la menor distancia. **7.2.2. Operación** -->
<!-- FIN TABLA 17 -->


**ÍNDICE DE ANEXOS**

ANEXO 1 CERTIFICADOS DE CALIBRACIÓN INSTRUMENTOS DE MEDICIÓN......... 32

ANEXO 2 REPORTES DE MEDICIÓN FUENTES DE RUIDO USADAS COMO
REFERENCIA ................................................................................................................. 42

_**4**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**1. INTRODUCCIÓN**

El presente estudio corresponde a la estimación y evaluación de los niveles de ruido y
vibración asociados a la ejecución del Proyecto _“_ _**Subestación Seccionadora Nueva**_
_**Pozo Almonte 220 kV**_ _”_, ubicado en la comuna de Pozo Almonte, región de Tarapacá.

En términos resumidos, el Proyecto corresponderá a una nueva obra del Sistema
Interconectado del Norte Grande (SING), que nace a partir de la necesidad de expandir el
Sistema de Transmisión Troncal, y por tanto ampliar las obras referidas tanto al Sistema

Interconectado Central como al del Norte Grande.

La nueva Subestación contendrá los espacios suficientes para recibir los paños relativos
al seccionamiento de la línea existente entre Lagunas - Pozo Almonte y de las nuevas
líneas hacia Cóndores y Parinacota, así como el enlace hacia la actual Subestación Pozo

Almonte. Por consiguiente, el Proyecto considera un patio inicial con capacidad para 4
diagonales y 5 paños habilitados. Junto con esto, se habilitarán los terrenos para generar
los espacios suficientes para 4 diagonales adicionales de igual configuración, para futuros

proyectos.

Teniendo en cuenta que la ejecución del Proyecto tendrá asociada la emisión de ruido y

vibraciones, en el marco de la tramitación ambientales es necesario cuantificar dichas

emisiones y estimar los niveles que potencialmente podrían registrarse sobre la

comunidad emplazada en el entorno. Para ello, el presente estudio identifica mediante el
análisis de imágenes satelitales y un reconocimiento en terreno, potenciales receptores

de ruido y vibraciones, incluyendo mediciones de ruido ambiente representativas de la
situación actual (antes del Proyecto).

Junto a ello, el presente estudio contempla modelaciones y cálculos teóricos de las
emisiones de ruido y vibraciones en los escenarios más desfavorable asociados a la
construcción y operación de la Subestación eléctrica. El resultado de lo anterior se
compara con los límites máximos permitidos por la normativa vigente o criterios

extranjeros de referencia cuando corresponda, estableciendo, en caso de ser necesario,
las medidas de control de ruido para asegurar el cumplimiento de los límites.

_**5**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**2. OBJETIVOS**

Los objetivos del estudio son:

 Identificar receptores sensibles cercanos al Proyecto, que pudieran verse afectados
por la ejecución de éste.

 Obtener los niveles basales de ruido en los puntos receptores previamente

identificados.

 Estimar los niveles de ruido y vibración sobre los puntos receptores previamente

identificados durante las diferentes Fases del Proyecto considerando los escenarios

más desfavorables.

 - Evaluar los niveles de ruido estimados para cada una de las Fases del Proyecto con

respecto a la normativa ambiental nacional y los niveles de vibraciones con respecto

al criterio de Referencia especificado.

 Establecer las medidas de control que incorporará el Proyecto en caso de estimarse
superaciones de los límites correspondientes.

**3. MARCO REGULATORIO**

**3.1. Ruido**

Para evaluar los niveles de ruido sobre la comunidad se aplica el Decreto Supremo

No38/11 del Ministerio del Medio Ambiente: “Norma de Emisión de Ruidos Generados por

Fuentes que Indica”, el cual establece los niveles máximos de emisión de ruido

generados por las fuentes emisoras de ruido que la norma regula. La evaluación de los
Niveles de ruido se efectúa con respecto a la zona donde se sitúe el receptor:

_Zona I:_ Aquella zona definida en el Instrumento de Planificación Territorial respectivo y
ubicada dentro del límite urbano, que permite exclusivamente uso de suelo Residencial o
bien este uso de suelo y alguno de los siguientes usos de suelo: Espacio Público y/o Área

Verde.

_Zona II:_ Aquella zona definida en el Instrumento de Planificación Territorial respectivo y

ubicada dentro del límite urbano, que permite además de los usos de suelo de la Zona I,

Equipamiento de cualquier escala.

_Zona III:_ Aquella zona definida en el Instrumento de Planificación Territorial respectivo y
ubicada dentro del límite urbano, que permite además de los usos de suelo de la Zona II,

Actividades Productivas y/o de Infraestructura.

_**6**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_Zona IV:_ Aquella zona definida en el Instrumento de Planificación Territorial respectivo y
ubicada dentro del límite urbano, que permite sólo usos de suelo de Actividades

Productivas y/o Infraestructura.

_Zona Rural:_ Aquella ubicada al exterior del límite urbano establecido en el Instrumento de
Planificación Territorial respectivo.

Los niveles de presión sonora corregidos que se obtengan de la emisión de una fuente
emisora de ruido, medidos en el lugar donde se encuentre el receptor, no podrán exceder
los valores que se fijan a continuación:

**Tabla 1: Límite Normativo D.S. N° 38/11 del MMA**

|Niveles Máximos Permisibles de Presión<br>Sonora Corregidos (NPC) en dB(A) Lento|Col2|Col3|
|---|---|---|
||de 7 a 21 Hrs.|de 21 a 7 Hrs.|
|Zona I|55|45|
|Zona II|60|45|
|Zona III|65|50|
|Zona IV|70|70|

En las áreas rurales, los niveles de presión sonora corregidos que se obtengan de la
emisión de una fuente emisora de ruido, medidos en el lugar donde se encuentre el
receptor, no podrán superar el menor valor entre el Nivel de ruido de fondo + 10 dB(A) y
el NPC para zona III de la Tabla 1 (65 dB(A) diurno y 50 dB(A) nocturno).

**3.2. Vibraciones**

Considerando la ausencia de una norma chilena que permita regular las vibraciones de
índole ambiental, en cumplimiento a lo establecido en el literal b) del Art. N° 5 del
Reglamento del SEIA, se utiliza referencialmente para estos fines el criterio establecido

en el documento “Transit Noise and Vibration - Impact Assesment” de la Federal Transit

Administration (FTA) de Estados Unidos (2006), la cual establece valores para estimación
y evaluación de daño a partir de Velocidad Peak de Partícula (PPV) en pulgadas/segundo

(in/sec).

Para el criterio de daño se utilizarán los establecidos por la norma FTA [Tabla 12-3] para
Categoría III, con un nivel máximo permitido de 0,2 pulgadas/s como velocidad máxima

_**7**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

de partículas para daño estructural para construcciones livianas de madera y edificios de
mampostería, por corresponder a un escenario desfavorable para el Proyecto.

**Tabla 2: Criterio FTA para evaluación daño estructural por vibraciones**

|Col1|Categoría de edificación|PPV<br>(pulgadas/segundo)|
|---|---|---|
|1|Hormigón armado, acero o madera (sin yeso)|0,5|
|2|Ingeniería de hormigón y albañilería (sin yeso)|0,3|
|3|Construcciones livianas de madera y edificios<br>de mampostería|0,2|
|4|Edificios extremadamente susceptibles a daño<br>por vibración|0,12|

Fuente: “Transit Noise and Vibration - Impact Assesment” de la Federal Transit Administration

(FTA) de Estados Unidos (2006).

**4. IDENTIFICACIÓN DE RECEPTORES**

Para la determinación de los puntos sensibles se efectuó una inspección inicial de
imágenes satelitales identificando potenciales receptores, los que luego fueron
corroborados en una visita inspectiva de terreno bajo el concepto descrito por el D.S.

N°38/11 del MMA como receptor a “ _toda persona que habite, resida o permanezca en un_

_recinto, ya sea un domicilio particular o en un lugar de trabajo, que esté o pueda estar_

_expuesta al ruido generado por una fuente emisora de ruido externa_ ”.

**4.1. Descripción**

En la siguiente imagen se muestran las áreas y trazados asociados al Proyecto y los

puntos potencialmente sensibles representativos de su entorno, considerados para

evaluación.

Posteriormente, se muestra cada receptor identificado con sus coordenadas UTM
(WGS84, uso 19H), la distancia aproximada al Proyecto, fotografías y una breve
descripción.

Cabe tener en cuenta que, para la evaluación de ruido, se consideran exclusivamente
aquellos puntos donde se evidencia presencia humana, conforme a la citada definición de
receptor del D.S. N° 38/11 del MMA, mientras que para vibraciones, también se incluyen
sitios arqueológicos o monumentos dado que el criterio de evaluación más restrictivo está

asociado a potenciales daños sobre las estructuras.

_**8**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**Figura 1: Área del Proyecto y Puntos receptores**

Fuente: Descripción del Proyecto - Imagen Satelital Google Earth.

_**9**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**Tabla 3: Puntos de Evaluación de Ruido y Vibraciones**

|PUNTO:|SE-01|UTM E:|421.207|UTM N:|7.752.702|Distancia<br>a SE::|1.092 m|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|**DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665.|**DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665.|**DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665.|**DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665.|**DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665.|**DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665.|**DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665.|**DESCRIPCIÓN**<br>Vivienda de un piso, de construcción ligera ubicada al poniente de la Ruta 5 Norte, cercano al<br>cruce con ruta A-665.|

_**10**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

|PUNTO:|SE-02|UTM E:|422.453|UTM N:|7.752.410|Distancia<br>a SE:|1.212 m|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|**DESCRIPCIÓN**<br>Sector no habitado ubicado en ruta A-665 a 1 Km al oriente de cruce con Ruta 5 Norte. Se<br>identifica estatua religiosa en memoria a “Comunidad Custodia”.|**DESCRIPCIÓN**<br>Sector no habitado ubicado en ruta A-665 a 1 Km al oriente de cruce con Ruta 5 Norte. Se<br>identifica estatua religiosa en memoria a “Comunidad Custodia”.|**DESCRIPCIÓN**<br>Sector no habitado ubicado en ruta A-665 a 1 Km al oriente de cruce con Ruta 5 Norte. Se<br>identifica estatua religiosa en memoria a “Comunidad Custodia”.|**DESCRIPCIÓN**<br>Sector no habitado ubicado en ruta A-665 a 1 Km al oriente de cruce con Ruta 5 Norte. Se<br>identifica estatua religiosa en memoria a “Comunidad Custodia”.|**DESCRIPCIÓN**<br>Sector no habitado ubicado en ruta A-665 a 1 Km al oriente de cruce con Ruta 5 Norte. Se<br>identifica estatua religiosa en memoria a “Comunidad Custodia”.|**DESCRIPCIÓN**<br>Sector no habitado ubicado en ruta A-665 a 1 Km al oriente de cruce con Ruta 5 Norte. Se<br>identifica estatua religiosa en memoria a “Comunidad Custodia”.|**DESCRIPCIÓN**<br>Sector no habitado ubicado en ruta A-665 a 1 Km al oriente de cruce con Ruta 5 Norte. Se<br>identifica estatua religiosa en memoria a “Comunidad Custodia”.|**DESCRIPCIÓN**<br>Sector no habitado ubicado en ruta A-665 a 1 Km al oriente de cruce con Ruta 5 Norte. Se<br>identifica estatua religiosa en memoria a “Comunidad Custodia”.|

_**11**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

|PUNTO:|SE-03|UTM E:|423.827|UTM N:|7.752.671|Distancia<br>a SE:|1.929 m|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|**DESCRIPCIÓN**<br>Viviendas de un piso de material ligero ubicadas en Ruta A-665.|**DESCRIPCIÓN**<br>Viviendas de un piso de material ligero ubicadas en Ruta A-665.|**DESCRIPCIÓN**<br>Viviendas de un piso de material ligero ubicadas en Ruta A-665.|**DESCRIPCIÓN**<br>Viviendas de un piso de material ligero ubicadas en Ruta A-665.|**DESCRIPCIÓN**<br>Viviendas de un piso de material ligero ubicadas en Ruta A-665.|**DESCRIPCIÓN**<br>Viviendas de un piso de material ligero ubicadas en Ruta A-665.|**DESCRIPCIÓN**<br>Viviendas de un piso de material ligero ubicadas en Ruta A-665.|**DESCRIPCIÓN**<br>Viviendas de un piso de material ligero ubicadas en Ruta A-665.|

_**12**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

|PUNTO:|RA-06|UTM E:|419.334|UTM N:|7.752.671|Distancia<br>a SE:|3.986 m|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|**DESCRIPCIÓN**<br>Sector con viviendas y actividades productivas ubicado en Ruta 5 Norte con Ruta A-65.|**DESCRIPCIÓN**<br>Sector con viviendas y actividades productivas ubicado en Ruta 5 Norte con Ruta A-65.|**DESCRIPCIÓN**<br>Sector con viviendas y actividades productivas ubicado en Ruta 5 Norte con Ruta A-65.|**DESCRIPCIÓN**<br>Sector con viviendas y actividades productivas ubicado en Ruta 5 Norte con Ruta A-65.|**DESCRIPCIÓN**<br>Sector con viviendas y actividades productivas ubicado en Ruta 5 Norte con Ruta A-65.|**DESCRIPCIÓN**<br>Sector con viviendas y actividades productivas ubicado en Ruta 5 Norte con Ruta A-65.|**DESCRIPCIÓN**<br>Sector con viviendas y actividades productivas ubicado en Ruta 5 Norte con Ruta A-65.|**DESCRIPCIÓN**<br>Sector con viviendas y actividades productivas ubicado en Ruta 5 Norte con Ruta A-65.|

Como se puede apreciar, los sitios habitados se encuentran a distancias mayores a 1 Km del
emplazamiento de la nueva SE.

Adicionalmente, de manera referencial se visitaron los puntos P05 y P07 señalados en la

Figura 1, identificados como “Sitios Arqueológicos” por los especialistas correspondientes, que,
a pesar de no corresponder a sectores habitados, serán considerados dentro de los puntos de

evaluación.

_**13**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**Tabla 4: Descripción Puntos complementarios (Sitios Arqueológicos)**

|PUNTO:|P-05|UTM E:|421.898|UTM N:|7.752.458|
|---|---|---|---|---|---|
|||||||
|**PUNTO:**|P-07|**UTM E**:|4242.20|**UTM N**:|7.754.900|
|||||||

**4.2. Medición de Niveles Basales de Ruido**

**4.2.1. Metodología**

Los niveles basales de ruido, en los puntos de evaluación señalados en el apartado anterior, se
obtuvieron mediante la medición del NPSeq en forma continua, descartando los ruidos

ocasionales, registrando su valor cada cinco minutos hasta que se estabilice la lectura, es
decir, hasta cuando la diferencia aritmética entre dos registros consecutivos sea menor o igual
a 2 dB. El nivel a considerar será el último de los niveles registrados.

_**14**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

Las mediciones de los niveles basales de ruido se realizaron el día 17 de octubre de 2017, en

periodo diurno y nocturno.

**4.2.2. Instrumentos de Medición**

Los instrumentos utilizados para caracterizar la línea base de ruido son:

 Sonómetro Integrador Tipo 2, marca Larson Davis Modelo LxT2 Sound Track.

 - Calibrador acústico, marca Larson Davis, modelo CAL 150.

 - Pantalla anti-viento.

 Trípode 1,5 m.

 - GPS Garmin.

 Cámara fotográfica digital.

Los equipos de medición cumplen con los requisitos establecidos en la normativa y sus
certificados de calibración se presentan en el Anexo 1 del presente estudio.

**4.2.3. Resultados**

En la siguiente tabla se muestran los Niveles de Presión Sonora Equivalentes (NPSeq) y los
NPS mínimos y máximos obtenidos en dichas mediciones, y además, se indican las fuentes de

ruido presentes en cada punto receptor:

**Tabla 5: Niveles Basales de Ruido, Período Diurno**

|Receptor|NPSeq<br>[dB(A)]|NPSmín<br>[dB(A)]|NPSmáx<br>[dB(A)]|Fuentes de ruido|
|---|---|---|---|---|
|SE -01|**60**|28,0|76,5|Tránsito vehicular lejano, aves,<br>ladrido de perros lejanos.|
|SE - 02|**45**|29,1|55,4|Tránsito vehicular lejano, aves.|
|SE - 03|**40**|27,8|50,4|Viento, ladrido de perros lejano,<br>tránsito vehicular lejano.|
|RA - 06|**46**|39,6|59,2|Viento, tránsito lejano, actividades<br>en receptores.|

Como se observa, los niveles de ruido en período diurno fluctúan entre 40 y 60 dB(A), con
mínimos entre 28 y 29 dB(A) y máximos entre 50 y 77 dB(A), donde la principal fuente de ruido
es el tránsito vehicular lejano por Ruta 5 Norte.

_**15**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**Tabla 6: Niveles Basales de Ruido, Período Nocturno**

|Receptor|NPSeq<br>[dB(A)]|NPSmín<br>[dB(A)]|NPSmáx<br>[dB(A)]|Fuentes de ruido|
|---|---|---|---|---|
|SE - 01|**53**|23,7|70,5|Tránsito vehicular lejano, ladrido de<br>perros lejanos.|
|SE - 02|**35**|23,0|58,5|Tránsito vehicular lejano.|
|SE - 03|**29**|21,4|35,2|Tránsito vehicular lejano.|
|RA - 06|**43**|32,3|71,3|Tránsito vehicular lejano.|

Como se observa, los niveles de ruido en período diurno fluctúan entre 29 y 53 dB(A), con
mínimos entre 21 y 24 dB(A) y máximos entre 35 y 71 dB(A), donde la principal fuente de ruido
es el tránsito vehicular lejano por Ruta 5 Norte.

**Figura 2: Comparación Niveles Basales de Ruido, Diurno / Nocturno**

65

60

55

50

45

40

35

30

25

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

SE -01 SE - 02 SE - 03 RA - 06

**Receptores**

_**16**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**5. MODELACIÓN EMISIONES DE RUIDO**

**5.1. Descripción del Proyecto**

La nueva Subestación contendrá los espacios suficientes para recibir los paños relativos al
seccionamiento de la línea existente entre Lagunas - Pozo Almonte y de las nuevas líneas
hacia Cóndores y Parinacota, así como el enlace hacia la actual Subestación Pozo Almonte.

Por consiguiente, el Proyecto considera un patio inicial con capacidad para 4 diagonales y 5
paños habilitados. Junto con esto, se habilitarán los terrenos para generar los espacios
suficientes para 4 diagonales adicionales de igual configuración, para futuros proyectos. La
siguiente figura muestra un Layout de la Subestación.

**Figura 3: Layout del Proyecto**

_**17**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**Tabla 7: Cronograma del Proyecto**

|Actividades|Meses|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividades**|**1 **|**2 **|**3 **|**4 **|**5 **|**6 **|**7 **|**8 **|**9**|**10**|**11**|**12**|
|Habilitación camino de acceso|||||||||||||
|Implementación instalación de faenas|||||||||||||
|**_Sector Subestación y Ampliación (Patio 220 kV)_**|**_Sector Subestación y Ampliación (Patio 220 kV)_**|**_Sector Subestación y Ampliación (Patio 220 kV)_**|**_Sector Subestación y Ampliación (Patio 220 kV)_**|**_Sector Subestación y Ampliación (Patio 220 kV)_**|**_Sector Subestación y Ampliación (Patio 220 kV)_**|**_Sector Subestación y Ampliación (Patio 220 kV)_**|**_Sector Subestación y Ampliación (Patio 220 kV)_**|**_Sector Subestación y Ampliación (Patio 220 kV)_**|**_Sector Subestación y Ampliación (Patio 220 kV)_**|**_Sector Subestación y Ampliación (Patio 220 kV)_**|**_Sector Subestación y Ampliación (Patio 220 kV)_**|**_Sector Subestación y Ampliación (Patio 220 kV)_**|
|Instalación cercos perimetrales|||||||||||||
|Preparación de la superficie (escarpe)|||||||||||||
|Preparación de la superficie (excavaciones)|||||||||||||
|Fundaciones|||||||||||||
|Construcción camino interior|||||||||||||
|Construcción edificio de control|||||||||||||
|Montaje de estructuras de equipos|||||||||||||
|Instalaciones eléctricas|||||||||||||
|Limpieza y compactación Área de Ampliación|||||||||||||
|**_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_**|**_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_**|**_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_**|**_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_**|**_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_**|**_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_**|**_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_**|**_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_**|**_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_**|**_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_**|**_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_**|**_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_**|**_Seccionamiento Línea 1x220 kV Lagunas - Pozo Almonte_**|
|Preparación de la superficie|||||||||||||
|Fundaciones|||||||||||||
|Montaje de Estructuras|||||||||||||
|Tendido y templado de Conductor|||||||||||||
|Puesta en Servicio|||||||||||||

Fuente: Descripción del Proyecto (DIA).

Durante la Fase de Construcción el horario de trabajo en el área de la Subestación será

exclusivamente diurno considerando 10 horas diarias de lunes a viernes. Para efectos de

modelación se considerará un frente de trabajo asociado a la habilitación de los caminos, otro
asociado a la Subestación Seccionadora y uno ubicado en los límites del área de la
Subestación (menor distancia hacia los receptores). Cada frente de trabajo contempla una
unidad de cada tipo de maquinaria de las especificadas en la Tabla 8.

_**18**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**5.2. Fuentes de Ruido**

**5.2.1. Fase de Construcción**

En la siguiente tabla, se indica la maquinaria que se utilizará durante la Fase de Construcción y
se detallan los Niveles de Presión Sonora (NPS) de emisión de cada fuente, a 10 metros, y sus

niveles en bandas de octava de frecuencia.

**Tabla 8: Niveles de Presión Sonora de maquinaria - Fase Construcción**

|Referencia<br>BS5228|Col2|Fuente de ruido|Frecuencia en Hz, niveles en dB|Col5|Col6|Col7|Col8|Col9|Col10|Col11|dB(A)<br>a 10 m|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tabla**|**N°**|**N°**|**63**|**125**|**250**|**500**|**1k**|**2k**|**4k**|**8k**|**8k**|
|_C2_|_2 _|Excavadora|75|84|78|74|70|68|64|61|**77**|
|C2|8|Retroexcavadora|76|66|64|64|63|60|59|50|**68**|
|_Medición del_<br>_Consultor_|_Medición del_<br>_Consultor_|Motoniveladora|72|68|63|55|55|52|48|--|**61**|
|_C4_|_16_|Camión Pluma|75|70|67|67|69|66|60|53|**72**|
|_Medición del_<br>_Consultor_|_Medición del_<br>_Consultor_|Placa compactadora|67|62|59|59|61|58|52|45|**64**|
|_C4_|_26_|Camión mixer+ Bomba<br>hormigón|75|76|71|70|71|68|64|60|**75**|
|_C4_|_16_|Camión estanque|75|70|67|67|69|66|60|53|**72**|
|_Medición del_<br>_consultor_|_Medición del_<br>_consultor_|Camioneta|62|49|42|44|47|43|40|--|**50**|
|_C4_|_3 _|Camión Tolva|84|81|74|73|72|68|61|53|**76**|
|_C4_|_16_|Camión Rampla|75|70|67|67|69|66|60|53|**72**|
|_C2_|_38_|Rodillo Compactador|80|75|77|72|67|62|54|46|**73**|
|**Total**|**Total**|**Total**|**88**|**87**|**82**|**80**|**79**|**75**|**70**|**65**|**83**|

Fuente: Norma Británica BS 5228-1:2009: “ _Code of practice for noise and vibration control on construction and open_

_sites - Part 1: Noise_ ” o mediciones de Consultor cuando se indica cuyo detalle se presenta en Anexo 2

El Nivel de Presión Sonora del Frente Total considera la operación de manera simultánea de

una unidad de cada una de las fuentes, distribuidas en el área definida en cada frente de

trabajo.

_**19**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**5.2.2. Fase de Operación**

Las fuentes de ruido consideradas en la modelación y su nivel de emisión en términos del nivel
de Potencia Sonora en dB(A) se presentan en la siguiente tabla:

**Tabla 9: Nivel de Potencia Sonora Fuentes de ruido - Etapa de Operación**

|Fuente|Frecuencia en Hz, NWS en dB(A)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|NWS<br>[dB(A)]|
|---|---|---|---|---|---|---|---|---|---|
|**Fuente**|_63_|_125_|_250_|_500_|_1K_|_2K_|_4K_|_8K_|_8K_|
|Subestación Eléctrica de<br>Referencia|96|103|95|85|77|75|73|64|**104**|
|Efecto Corona Líneas<br>eléctricas de Alta tensión|--|83|80|78|80|81|81|--|88|

Fuente: Mediciones del Consultor en proyectos similares. Ver detalles en Anexo 2.

**5.2.3. Fase de Cierre**

De acuerdo con la descripción del Proyecto, no se contemplan obras significativas asociadas al
cierre del Proyecto. No obstante, de requerirse éstas serán en el escenario más desfavorable,

asimilables a las actividades de construcción.

**5.3. Software de Simulación de Ruido**

Para evaluar los impactos esperados en esta componente ambiental, se estiman y proyectan
los niveles de ruido hacia los receptores sensibles, mediante el software de modelación
PREDICTOR - LIMA V11.21, de Bruel & Kjaer, Alemania. Este programa basa su algoritmo de
predicción en la Norma ISO 9613 " _Acoustics - Attenuation of sound during propagation outdoors_

_- Part 1: Calculation of the absorption of sound by the atmosphere; Part 2: General method of_
_calculation_ ". Cabe mencionar que este software se encuentra validado, en cuanto a sus
cálculos, por medio de la ISO 17534-1: 2015 - _“Acoustics - Software for the calculation of_

_sound outdoors - Part 1: “Quality requirements and quality assurance”_ .

**5.4. Resultados**

**5.4.1. Fase de Construcción**

En las siguientes figuras y tablas se presentan los resultados de la modelación mediante
mapas de ruido tanto en planta como en 3D considerando un código de colores representativo

de los rangos de niveles en dB(A).

_**20**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**Figura 4: Mapa de ruido - Fase Construcción**

Fuente: Modelación Software Predictor Lima V11.21

_**21**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**Figura 5: Mapa de ruido sobre imagen satelital - Fase Construcción**

La tabla siguiente resume los niveles de ruido estimados en los puntos receptores para la Fase
de Construcción del Proyecto:

**Tabla 10: Niveles de Ruido Modelados - Fase Construcción**

|Punto|NPS Modelado [dB(A)]|
|---|---|
|SE-01|42|
|SE-02|51|
|SE-03|36|
|RA-06|42|

Fuente: Modelación con Software Predictor Lima V11.21

Es posible establecer que los niveles obtenidos para el escenario de modelación que simula la
construcción del Proyecto fluctúan entre 36 y 51 dB(A).

_**22**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**5.4.2. Fase de Operación**

Por su parte, para la modelación de la Fase de Operación, se consideran el ruido generado por
los equipos instalados dentro de la Subestación y bajo ciertas condiciones climáticas el ruido
leve que podría producirse en los conductores eléctricos de la línea de seccionamiento, con los

niveles de emisión indicados en la Tabla 9.

En la siguiente tabla se resumen los niveles estimados mediante el software de modelación en
los puntos receptores para la Fase de Operación:

**Tabla 11: Niveles de ruido - Fase de Operación**

|Punto|NPS Modelado [dB(A)]|
|---|---|
|SE-01|**24**|
|SE-02|**23**|
|SE-03|**19**|
|RA-06|**8 **|

Fuente: Modelación con Software Predictor Lima V11.21

Es posible establecer que los niveles obtenidos en los puntos receptores asociados a la
operación del Proyecto fluctúan entre 8 y 24 dB(A).

Como se puede apreciar, para el aporte exclusivo del Proyecto sobre los receptores de manera
teórica, el software entrega resultados menores a 25 dB, lo que, al encontrarse bajo el rango
auditivo del ser humano, en la práctica significa que será imperceptible en dichos lugares.

En la siguiente figura se presentan los resultados de la modelación mediante mapas de ruido
considerando un código de colores representativo de los rangos de niveles en dB(A).

_**23**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**Figura 6: Mapa de Ruido- Fase de Operación**

Fuente: Modelación Software Predictor Lima V11.21.

_**24**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**6. ESTIMACIÓN DE VIBRACIONES**

**6.1. Vibraciones en Fase de Construcción**

La siguiente tabla, presenta los niveles de emisión de vibraciones en términos de la Velocidad
Peak de Partícula (PPV) para las maquinarias que contempla la construcción del Proyecto.
Dichos niveles son extraídos del documento de la FTA señalado en el punto 3.2 y

corresponden a mediciones efectuadas a 25 pies de distancia (7,6 m aprox.).

**Tabla 12: Fuentes de Vibración - Fase de Construcción**

|Maquinaria|PPV a 25 pies (7,62m)|VdB|
|---|---|---|
|**Maquinaria**|**pulgadas/seg.**|**(ref. 10^-6 pulg./seg.)**|
|Excavadora|0,089|87|
|Retroexcavadora|0,089|87|
|Motoniveladora|0,089|87|
|Camión Pluma|0,076|86|
|Placa compactadora|0,089|87|
|Camión mixer+ Bomba<br>hormigón|0,76|106|
|Camión estanque|0,076|86|
|Camión Tolva|0,076|86|
|Camión Rampla|0,076|86|
|Rodillo Compactador|0,21|94|
|**TOTAL PPV a 25 pies (7,6m)**|**0,324**|**98,2**|

**6.2. Vibraciones Fase de Operación**

Para la Fase de Operación, dadas las características del Proyecto, no se esperan impactos
relacionados con la operación de la Subestación ni líneas eléctricas.

**6.3. Metodología**

Para estimar los niveles de vibración producto de la ejecución del Proyecto, se utiliza el

algoritmo establecido por la FTA “Transit Noise and Vibration- Impact Assesment”. Para
efectos de modelación se consideran las distintas distancias de los receptores al área de

_**25**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

Proyecto para cada una de las actividades constructivas. La estimación de la vibración sobre
cada punto de evaluación se determina utilizando la siguiente relación:

PPV Proyectado = PPV Ref x (25/D) [ 1,5 ]

Dónde:

PPV Proyectado es la velocidad peak de partícula a determinar a la distancia D, utilizando como

referencia las velocidades (PPV a 25 ft) señaladas en la Tabla 12.

La distancia a considerar para los cálculos es la menor existente entre cada receptor y las
obras que contempla el Proyecto dónde se usará maquinaria pesada, ya sea referida a la

ubicación de la SE o de los caminos de acceso a habilitar.

**6.4. Resultados**

En la siguiente tabla se presentan los resultados obtenidos de la estimación de Vibraciones.

**Tabla 13: Resultados Estimación de Vibraciones - Fase de Construcción**

|Receptor|Distancia a frente trabajo [m]|PPV Proyectado [pulgadas/s]|
|---|---|---|
|SE-01|980|**0,00022**|
|SE-02|140|**0,11714**|
|SE-03|1.679|**0,00010**|
|RA-06|294|**0,00135**|
|P-05|768|**0,00032**|
|P-07|2.642|**0,00005**|

Fuente: Elaboración Propia

Como se aprecia, el unico punto cercano a las obras es el SE-02 que en particular se

encuantra a 140 m del trazado de uno de las rutas de acceso a la SE a habilitar durante la

construcción.

_**26**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**7. EVALUACIÓN DE RESULTADOS**

**7.1. Ruido**

La evaluación de los niveles de ruido se realiza con respecto a los límites establecidos en el
D.S. No38/11 del Ministerio del Medio Ambiente, aplicables sobre cada receptor identificado.
Para lo cual se efectúa una homologación entre lo definido por los Instrumentos de
Planificación Territorial Vigente (IPT) para los receptores y las definiciones de Zonificación de

la citada norma de ruido, especificada en el punto 3.1 del presente Estudio.

Al respecto, analizando los IPT vigentes en Pozo Almonte se pudo determinar que la totalidad

de los receptores considerados en el presente estudio se ubican fuera del límite urbano

correspondiente.

Dado lo anterior, corresponde la asimilación de los Receptores a la “Zona Rural” definida en la
citada normativa de ruido, estando los límites máximos permisibles determinados por el menor
valor entre el nivel de ruido de fondo + 10 dB o el límite para Zona III (65 diurno y 50 nocturno).

Considerando que las mediciones de ruido basal se efectuaron en ausencia del Proyecto,
mediante metodología que garantiza la obtención de los menores niveles representativos de
los ambientes sonoros en los que se emplazan los receptores, para efectos de evaluación se
establecen los límites máximos permisibles que se detallan en la siguiente tabla en base a los

resultados del levantamiento basal como representativos del ruido de fondo.

**Tabla 14: Límites Máximos Permisibles**

|Receptor|Ruido de Fondo<br>NPSeq [dB(A)]|Col3|RF+10 dB|Col5|Límites Zona III|Col7|Límite Máximo<br>Permisible|Col9|
|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Diurno**|**Nocturno**|**Diurno**|**Nocturno**|**Diurno**|**Nocturno**|**Diurno**|**Nocturno**|
|**SE -01**|60|53|70|63|65|50|**65**|**50**|
|**SE - 02**|45|35|55|45|45|45|**55**|**45**|
|**SE - 03**|40|29|50|39|39|39|**50**|**39**|
|**RA - 06**|46|43|56|53|53|53|**56**|**50**|

**7.1.1. Fase de Construcción**

Para efectos de evaluación de esta Fase, se consideran los Niveles de Presión Sonora

estimados hacia los receptores. La construcción, no contempla obras en horario nocturno.

_**27**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**Tabla 15: Evaluación normativa - Fase de Construcción**

|Receptor|Altura [m]|Nivel Modelado<br>Fase de<br>Construcción|Limite|Exceso de<br>nivel [dB]|¿Cumple<br>Norma?|
|---|---|---|---|---|---|
|SE-01_A|1,5|42|65|0|**SI**|
|SE-02_A|1,5|51|_No aplica (deshabitado)_|_No aplica (deshabitado)_|_No aplica (deshabitado)_|
|SE-03_A|1,5|36|50|0|**SI**|
|RA-06_A|1,5|42|56|0|**SI**|

Se puede observar que en esta Fase se cumple con los niveles máximos dispuestos en el D.S.

N° 38/11 del MMA en los todos los puntos receptores.

**7.1.2. Fase de Operación**

En la siguiente tabla se evalúan los niveles estimados para la Fase de Operación del Proyecto
considerando el horario nocturno de modo de garantizar el cumplimiento de los límites más

restrictivos.

**Tabla 16: Evaluación normativa - Fase de Operación**

|Receptor|Altura<br>[m]|Nivel Modelado<br>Fase Operación<br>[dB(A)]|Límite normativo<br>(horario nocturno)<br>[dB(A)]|Exceso de<br>nivel [dB]|¿Cumple<br>Norma?|
|---|---|---|---|---|---|
|SE-01_A|1,5|**24**|50|0|**SÍ**|
|SE-02_A|1,5|_23_|_No aplica (deshabitado)_|_No aplica (deshabitado)_|_No aplica (deshabitado)_|
|SE-03_A|1,5|**19**|39|0|**SÍ**|
|RA-06_A|1,5|**8 **|50|0|**SÍ**|

Se puede observar que los puntos evaluados cumplen con el límite máximo establecido por el

D.S.38/11 del Ministerio del Medio Ambiente.

**7.2. Vibraciones**

**7.2.1. Fase de Construcción**

Como se señaló en el punto 3.2 del presente estudio, se adoptó como criterio para la
evaluación de vibraciones, lo señalado por la FTA respecto del riego de daño estructural para
construcciones livianas de madera y edificios de mampostería, por corresponder a un

escenario desfavorable para el Proyecto.

_**28**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

De acuerdo con lo anterior, en la siguiente tabla se presenta la evaluación para todos los
receptores considerando la menor distancia a los frentes de potencial emisión de vibraciones.

**Tabla 17: Evaluación Criterio FTA Vibraciones - Fase de Construcción**

|Receptor|Distancia a frente<br>trabajo [m]|PPV Proyectado<br>[pulgadas/s]|Límite PPV<br>[pulgadas/s]|¿Cumple?|
|---|---|---|---|---|
|SE-01|980|**0,00022**|0,2|**Sí**|
|SE-02|140|**0,11714**|0,2|**Sí**|
|SE-03|1679|**0,00010**|0,2|**Sí**|
|RA-06|294|**0,00135**|0,2|**Sí**|
|P-05|768|**0,00032**|0,2|**Sí**|
|P-07|2642|**0,00005**|0,2|**Sí**|

Como se puede apreciar, para todos los receptores se demuestra el cumplimiento del criterio
de evaluación adoptado, inclusive sobre el punto SE-02 que se ubica a la menor distancia.

**7.2.2. Operación**

Para la Fase de Operación, dadas las características del Proyecto, no se esperan impactos
relacionados con la operación de la Subestación eléctrica ni de la línea de Seccionamiento.

**8. Medidas de Control**

Teniendo en cuenta que se ha demostrado el cumplimiento normativo para todos los

componentes evaluados, el Proyecto no contempla medidas de control.

_**29**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**9. RESUMEN EJECUTIVO**

El Proyecto “SUBESTACIÓN SECCIONADORA NUEVA POZO ALMONTE 220 KV” se
ejecutará en la comuna de Pozo Almonte en un sector ubicado al exterior de los límites

urbanos de dicha comuna. En el entorno se identificaron potenciales receptores de ruido

asociados a viviendas aisladas de material ligero cercanos al cruce de Ruta 5 Norte con las
Rutas A-665 y A-65. Se identificaron también sitios arqueológicos o monumentos,
incorporados principalmente en el análisis de vibraciones del presente estudio.

Los niveles de ruido ambiente actuales (antes de la ejecución del Proyecto) en dichos lugares
se ve influenciado por el ruido del tráfico lejano por las rutas mencionadas, ladridos de perros,

viento y eventualmente actividades propias de los receptores. La técnica de medición de ruido
descartó aquellos instantes en que circularon vehículos cercanos al punto de medición por la

Ruta 5, por lo tanto es representativa de las condiciones de menor ruido ambiente tanto en

horario diurno como nocturno. Bajo estas condiciones, los niveles obtenidos en horario diurno

oscilan entre 40 y 60 dB(A), mientras que en horario nocturno lo hacen entre 29 y 53 dB(A).

Para la evaluación de las emisiones de ruido y vibraciones asociadas a la Fase de
Construcción del Proyecto, se consideró la operación simultánea de todas las maquinarias
contempladas para dicha actividad, distribuidas en el área y/o trazados definidos para el
Proyecto. Por su parte, para la simulación de la Operación, se consideraron la emisión de los
equipos que contemplará la Subestación y el eventual ruido generado por los conductores

eléctricos. Los niveles de ruido se obtienen mediante modelaciones con Software

especializado (predictor Lima V11.21) y los cálculos de Vibraciones se efectuaron conforme a

lo indicado en el Documento “Transit Noise and Vibration- Impact Assesment” de la FTA de

Estados Unidos.

Los niveles de **ruido** modelados asociados a la Fase de Construcción del Proyecto, se

encuentran entre 36 y 42 dB(A) en los distintos puntos receptores con presencia humana. Por
su parte, la modelación de la Fase de Operación arrojó valores sobre los puntos receptores
imperceptibles para el oído humano (entre 8 y 24 dB(A)).

Para la componente **vibraciones**, dada las características del Proyecto y sus actividades

asociadas, sólo se estimaron posibles emisiones durante la construcción, las cuales fueron
calculadas bajo el escenario más desfavorable, a la menor distancia entre los frentes de
trabajo y los puntos de evaluación. Los niveles resultantes indican valores de velocidad peak
de partícula (PPV) de hasta 0,011 pug/seg. Dichos niveles podrían esperarse sobre el punto
SE-02 que se encontraría a 140 m del trazado de una de las rutas de acceso a la nueva

Subestación.

_**30**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

**10. CONCLUSIONES**

Si bien la ejecución del Proyecto tiene asociada la emisión de Ruido y Vibraciones, de acuerdo
con los antecedentes presentados en este estudio y la evaluación de sus resultados

presentada para Ruido en el punto 7.1 y para Vibraciones en el punto 7.2, es posible concluir
que dichas emisiones, bajo las condiciones más desfavorables, no superarán los valores
establecidos por la normativa vigente o normativas de referencia según corresponda.

**Por lo tanto, en materia de Ruido y Vibraciones las emisiones del Proyecto no generan**
**riesgo para la salud de la población en virtud de lo definido en el Artículo 5 del**
**Reglamento del SEIA (D.S N° 40/2012 del MMA), ni para el patrimonio cultural en virtud**
**de lo señalado en el Artículo 10 del citado reglamento.**

Elaborado por:

**CAMILO ROCHA GANA**

**Ingeniero de Proyectos**

**Ruido Ambiental SpA.**

Ingeniero Civil en Sonido y Acústica

Diplomado en Gestión Ambiental

_**31**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

### ANEXO 1 CERTIFICADOS DE CALIBRACIÓN INSTRUMENTOS DE MEDICIÓN

_**32**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_**33**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_**34**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_**35**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_**36**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_**37**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_**38**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_**39**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_**40**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_**41**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

### ANEXO 2 REPORTES DE MEDICIÓN FUENTES DE RUIDO USADAS COMO REFERENCIA

_**42**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_**43**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_**44**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_**45**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

|Mediciones Operación Subestación Eléctrica|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|
|**RESULTADO:**<br>|**RESULTADO:**<br>|**RESULTADO:**<br>|**RESULTADO:**<br>|**RESULTADO:**<br>|**RESULTADO:**<br>|**RESULTADO:**<br>|**RESULTADO:**<br>|**RESULTADO:**<br>|**RESULTADO:**<br>|
|**Distancia**|**63 Hz**|**125**<br>**Hz**|**250**<br>**Hz**|**500Hz**|**1KHz**|**2KHz**|**4KHz**|**8KHz**|**NPS**<br>**[dB(A)]**|
|**15 m**|64|71|63|53|45|43|41|32|**57,3**|
|||||||||||

_**46**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_**47**_

Subestación Seccionadora

Nueva Pozo Almonte 220 KV

_Este informe ha sido elaborado bajo los controles establecidos por el Sistema de Gestión de_

_Calidad de Ruido Ambiental SpA., certificado por Bureau Veritas Certification conforme con la_

_norma ISO9001: 2008. Numero de Certificado Serie: BVCSG5451_

_**48**_