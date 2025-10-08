---
title: “TITULO DEL PROYECTO”
author: Daniela Carvajal
date: D:20190617225719-04'00'
language: es
type: report
pages: 147
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO: APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB PLANTA TENO REGIÓN DEL MAULE
-->

# MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO: APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB PLANTA TENO REGIÓN DEL MAULE

## Para: APLE CONSULTORES SPA Y

**Santiago, junio de 2019**

**Título del Proyecto**
MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES
ATMOSFÉRICAS DEL PROYECTO: APLICACIÓN DE ECONOMÍA

CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB PLANTA
TENO, VII REGIÓN

**Autores:**

Héctor Jorquera González, modelación de las emisiones,

Dictuc S.A. Vicuña Mackenna No 4860, Macul - Santiago

Alejandro Cofré, determinación de emisiones

INGEA, San Pio X 2390 OF 506, providencia, fono 22339552,

998834300

Ana María Villalobos, ayudante de proyecto, DICTUC S.A.

**Datos Mandante**

Nombre: Aple Consultores Spa

Dirección: Apoquindo 3401 - oficina 22 - Las Condes

RUT: 78.710.340-5

Teléfono:

Email: [jlehuede@aple.cl](mailto:jlehuede@aple.cl)

**Datos Cliente** (si es distinto al Mandante)

Razón Social: Bío Bío Cementos S.A., Planta Teno

RUT : 96.718.010-6

**Cuerpo del informe**

147 hojas (incluye portada)

**Fecha del informe**

14/06/2019

**Información Contractual**

Orden de servicio

**Contraparte técnica:**

José Miguel Lehuedé, APLE

**Resumen**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 2 de 147

Código V01: FI-A.03-DSA

**INDICE**

1. Resumen ejecutivo .................................................................................................................... 12

2. Introducción y objetivos ............................................................................................................ 19

3. Línea base de calidad del aire y meteorología. ......................................................................... 19

1.1 Características de la meteorología en la zona de Teno .................................................... 21

1.2 Modelación de la meteorología en la zona. ...................................................................... 25

3.2.1 Desempeño del modelo WRF con respecto a la meteorología superficial en Teno ...... 26

3.2.2 Desempeño de la modelación de WRF para meteorología en altura. ............................. 33

3.2.3 Desempeño de la modelación de WRF para la altura de mezclado. ................................ 37

4. Descripción de las emisiones consideradas según escenarios .................................................. 41

5. Determinación de los niveles de calidad del aire según escenarios y aplicación del modelo de
dispersión CALPUFF ........................................................................................................................... 49

5.1 Metodología de análisis ......................................................................................................... 49

5.2.1 Determinación de los puntos de interés. ........................................................................ 49

1.3 Análisis en Puntos de máximo impacto (PMI) ................................................................... 52

1.4 Análisis en Estación ENLASA .............................................................................................. 55

1.5 MP 10 ................................................................................................................................... 57

1.6 MP 2.5 .................................................................................................................................. 69

1.7 NO 2 .................................................................................................................................... 81

1.8 SO 2 ..................................................................................................................................... 94

1.9 CO .................................................................................................................................... 116

1.10 Plomo .............................................................................................................................. 128

1.11 Depositación total de azufre y nitrógeno en la zona. ..................................................... 130

6. Análisis de incertidumbre de la modelación. .......................................................................... 140

7. Conclusiones............................................................................................................................ 143

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 3 de 147

Código V01: FI-A.03-DSA

**INDICE TABLAS**

Tabla 1-1 Concentraciones ambientales de MP 10, MP 2.5, NO 2, SO 2, CO y Pb en PMI y porcentajes
según niveles de calidad del aire normados ..................................................................................... 14

Tabla 1-2. Ubicación receptores discretos (UTM, huso 19 H, WGS84) ............................................. 15

Tabla 1-3 Concentraciones ambientales de MP 10, MP 2.5, NO 2, SO 2, CO y Pb en Estación de Calidad del
Aire ENLASA y porcentajes según niveles de calidad del aire normados ......................................... 16

Tabla 3-1 Línea base de calidad del aire en estación ENLASA .......................................................... 20

Tabla 3-2. Estadísticas de desempeño del modelo WRF para el viento año 2018. .......................... 31

Tabla 3-3. Estadísticas de desempeño del modelo WRF para temperatura año 2018. .................... 32

Tabla 4-1. Emisiones de Fuente 1: Chimenea N° 1 Horno Clinker condición actual y la más
desfavorable con proyecto ................................................................................................................ 42

Tabla 4-2. Parámetros de las emisiones de la chimenea N°1 del horno Clinker. .............................. 43

Tabla 4-3. Características de las emisiones de las demás fuentes oficiales de Planta CBB que
mantienen sus emisiones en situación actual y con proyecto. ......................................................... 44

Tabla 4-4. Emisiones Base de la Central Térmica ENLASA y de Planta de Paneles MDP Arauco ...... 45

Tabla 4-5. Emisiones del proyecto Central Térmica ENLASA, 6 turbinas adicionales. ...................... 46

Tabla 4-6. Emisiones del proyecto planta de alimentos de mascotas de Nestlé S.A. ....................... 47

Tabla 5-1. Ubicación receptores discretos (UTM, Huso 19 H, WGS84) ............................................ 50

Tabla 5-2 Localización del PMI (UTM, WGS 84) y sus aportes en escenarios 1 a 4 para cada

contaminante en análisis. ................................................................................................................. 52

Tabla 5-3 Concentraciones ambientales de MP 10, MP 2.5, NO 2, SO 2, CO y Pb en PMI y porcentajes
según niveles de calidad del aire normados ..................................................................................... 54

Tabla 5-4 Aportes en estación ENLASA para escenarios 1 a 4 para cada contaminante en análisis. 55

Tabla 5-5 Concentraciones ambientales de MP 10, MP 2.5, NO 2, SO 2, CO y Pb en Estación ENLASA ... 56

Tabla 5-6 Resultados MP 10 Anual en PMI y los seis receptores de interés ....................................... 57

Tabla 5-7 Resultados Niveles de calidad del aire de MP 10 Anual en PMI y los seis receptores de interés

........................................................................................................................................................... 57

Tabla 5-8 Resultados MP 10 Percentil 98 diario en los seis receptores discretos y punto de máximo
impacto ............................................................................................................................................. 63

Tabla 5-9. Resultados Niveles de calidad del aire de MP 10 Diario en PMI y en los seis receptores de

interés ............................................................................................................................................... 64

Tabla 5-10 MP 2.5 Anual en PMI y los seis receptores de interés ....................................................... 69

Tabla 5-11 Resultados Niveles de calidad del aire de MP 2,5 Anual en PMI y en los seis receptores de

interés ............................................................................................................................................... 70

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 4 de 147

Código V01: FI-A.03-DSA

Tabla 5-12 Resultados MP 2,5 Percentil 98 diario en los seis receptores discretos y en el punto de
máximo impacto ................................................................................................................................ 75

Tabla 5-13 Resultados Niveles de calidad del aire de MP 2,5 P98 diario en PMI y en los seis receptores

de interés .......................................................................................................................................... 76

Tabla 5-14 Resultados NO 2 Anual en PMI y en los seis receptores de interés.................................. 82

Tabla 5-15 Resultados Niveles de calidad del aire de NO 2 Anual en PMI y en los seis receptores de

interés ............................................................................................................................................... 83

Tabla 5-16 Resultados NO 2 horario Percentil 99 en los seis receptores discretos y en el punto de
máximo impacto ................................................................................................................................ 88

Tabla 5-17 Resultados Niveles de calidad del aire de NO 2 horario P 99 en PMI y en los seis receptores

de interés .......................................................................................................................................... 89

Tabla 5-18 Resultados SO 2 Anual en PMI y los seis receptores de interés ....................................... 94

Tabla 5-19 Resultados Niveles de calidad del aire de SO 2 Anual en PMI y los seis receptores de interés

........................................................................................................................................................... 95

Tabla 5-20 Resultados SO 2 Percentil 99 diario en los seis receptores discretos y punto de máximo
impacto ........................................................................................................................................... 100

Tabla 5-21 Resultados Niveles de calidad del aire de SO 2 P99 diario en PMI y en los seis receptores

de interés ........................................................................................................................................ 101

Tabla 5-22 Resultados SO 2 horario P99 (g/m [3] ) en los seis receptores discretos y punto de máximo
impacto ........................................................................................................................................... 106

Tabla 5-23 Resultados Niveles de calidad del aire de SO 2 P99 Horario en PMI y los seis receptores de

interés ............................................................................................................................................. 107

Tabla 5-24 Resultados CO Percentil 99 horario en los seis receptores discretos y punto de máximo
impacto ........................................................................................................................................... 116

Tabla 5-25 Resultados Niveles de calidad del aire de CO P99 horario en PMI y los seis receptores de

interés ............................................................................................................................................. 117

Tabla 5-26 Resultados CO Percentil 99 8 horas en los seis receptores discretos y punto de máximo
impacto ........................................................................................................................................... 122

Tabla 5-27 Resultados Niveles de calidad del aire de CO P99 8 horas en PMI y los seis receptores de

interés ............................................................................................................................................. 123

Tabla 5-28 Resultados Plomo en PMI y los seis receptores de interés y comparación con norma de

calidad ............................................................................................................................................. 128

Tabla 5-29 Nivel de Azufre y Nitrógeno depositado en suelo considerando PMI y a 2 km del sitio,

Escenarios 1 a 4. .............................................................................................................................. 131

Tabla 6-1. Análisis de sensibilidad comparando los resultados de la modelación CALPUFF-WRF con
los valores medidos en estación ENLASA (g/m [3] ) .......................................................................... 140

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 5 de 147

Código V01: FI-A.03-DSA

Tabla 6-2. Comparación de los resultados de la modelación CALPUFF-WRF (usando un factor de
corrección) con los valores medidos en estación ENLASA (g/m [3] ) ................................................ 142

Tabla 7-1 Concentraciones ambientales de MP 10, MP 2.5, NO 2, SO 2, CO y Pb g/m3 en PMI y
porcentajes según las normas de calidad del aire .......................................................................... 144

Tabla 7-2 Concentraciones ambientales de MP 10, MP 2.5, NO 2, SO 2, CO y Pb en Estación de Calidad del
Aire ENLASA y porcentajes según niveles de calidad del aire normados ....................................... 145

**INDICE FIGURAS**

Figura 1-1. Ubicación de los Receptores R_1 a R_6 considerados en el análisis .............................. 15

Figura 3-1. Estaciones de monitoreo meteorológica de CBB y de estación de calidad del aire ENLASA.

........................................................................................................................................................... 20

Figura 3-2 Serie cronológica de datos estación de monitoreo Planta Teno ..................................... 21

Figura 3-3 Perfiles diarios de la velocidad del viento, Planta Teno. .................................................. 22

Figura 3-4. Rosas del viento anuales : a) todas las horas, b) de 8 a 19 horas, c) de 20 a 23 horas, d)

de 0 a 7 am. ....................................................................................................................................... 23

Figura 3-5. Serie cronológica de temperaturas medidas en Planta Teno CBB. Temperatura, °C. .... 24

Figura 3-6. Perfiles diarios de la temperatura a lo largo del año en Planta Teno. Temperatura, °C. 24

Figura 3-7: Dominios D2, D3 y D4 de la modelación meteorológica de WRF. .................................. 25

Figura 3-8. Variabilidad temporal de los vientos año 2018, estación Planta Teno CBB. .................. 27

Figura 3-9. Comparación de rosas de viento observada y modelada año 2018, Planta Teno CBB... 28

Figura 3-10. Variabilidad temporal de la temperatura año 2018, Planta Teno CBB. ........................ 29

Figura 3-11. Comparación de la temperatura observada (panel izquierdo) y modelada (panel
derecho) para el año completo modelado con WRF, sitio del radiosondeo de Santo Domingo, a las

12 UTC. .............................................................................................................................................. 33

Figura 3-12. Comparación de la temperatura observada (panel izquierdo) y modelada (panel
derecho) para el año completo modelado con WRF, sitio del radiosondeo de Santo Domingo, a las

00 UTC. .............................................................................................................................................. 34

Figura 3-13. Diferencia entre temperatura observada y modelada para el año completo modelado
con WRF, sitio del radiosondeo de Santo Domingo, a las 00 UTC (panel superior) y a las 12 UTC (panel
inferior). ............................................................................................................................................ 35

Figura 3-14 Comparación de la velocidad observada (panel izquierdo) y modelada con WRF (panel
derecho) para el año completo, sitio del radiosondeo de Santo Domingo, a las 12 UTC. ................ 36

Figura 3-15 Comparación de la velocidad observada (panel izquierdo) y modelada con WRF (panel
derecho) para el año completo, sitio del radiosondeo de Santo Domingo, a las 00 UTC. ................ 36

Figura 3-16. Perfiles diarios de la altura de mezclado modelada mediante WRF. ........................... 38

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 6 de 147

Código V01: FI-A.03-DSA

Figura 3-17. Comparación de alturas de mezclado medidas al mediodía en Santiago (panel superior,
Muñoz y Undurraga, 2010) y modeladas por WRF al mediodía en Teno (panel inferior). ............... 39

**Figura 3-18. Comparación del crecimiento de la altura de mezclado en meses fríos y cálidos. Panel**
**superior: estimaciones experimentales en Santiago (Muñoz y Undurraga, 2010); panel inferior:**
**modelación de WRF para Teno.** ....................................................................................................... 40

Figura 5-1. Dominio de modelación de calidad del aire, en coordenadas LCC (km). ........................ 50

Figura 5-2. Ubicación de los Receptores R_1 a R_6 considerados en el análisis .............................. 51

**Figura 5-3. Puntos de máximo impacto asociados a la Planta Teno. El polígono azul es el borde de**
**la planta Teno CBB, y el polígono negro es el borde urbano de Teno.** ........................................... 53

Figura 5-4 Mapa de concentraciones del MP 10 anual (g/m [3] ) para el escenario 1. La ciudad de Teno
está delimitada por el polígono negro. ............................................................................................. 59

Figura 5-5 Mapa de concentraciones del MP 10 anual (g/m [3] ) para el escenario 2. La ciudad de Teno
está delimitada por el polígono negro. ............................................................................................. 60

Figura 5-6 Mapa de concentraciones del MP 10 anual (g/m [3] ) para el escenario 3. La ciudad de Teno
está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................... 61

Figura 5-7 Mapa de concentraciones del MP 10 anual (g/m [3] ) para el escenario 4. La ciudad de Teno
está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................... 62

Figura 5-8 Mapa del percentil 98 de las concentraciones diarias de MP 10 (g/m [3] ) para el escenario
1. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ............................................................................................................. 65

Figura 5-9 Mapa del percentil 98 de las concentraciones diarias de MP 10 (g/m [3] ) para el escenario
2. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ............................................................................................................. 66

Figura 5-10 Mapa del percentil 98 de las concentraciones diarias de MP 10 (g/m [3] ) para el escenario
3. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ............................................................................................................. 67

Figura 5-11 Mapa del percentil 98 de las concentraciones diarias de MP 10 (g/m [3] ) para el escenario
4. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ............................................................................................................. 68

Figura 5-12 Mapa de concentraciones del MP2,5 anual (g/m3) para el escenario 1. La ciudad de
Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................... 71

Figura 5-13 Mapa de concentraciones del MP2,5 anual (g/m3) para el escenario 2. La ciudad de
Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................... 72

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 7 de 147

Código V01: FI-A.03-DSA

Figura 5-14 Mapa de concentraciones del MP2,5 anual (g/m3) para el escenario 3. La ciudad de
Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................... 73

Figura 5-15 Mapa de concentraciones del MP2,5 anual (g/m3) para el escenario 4. La ciudad de
Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................... 74

Figura 5-16 Mapa del percentil 98 de las concentraciones diarias de MP 2,5 (g/m [3] ) para el escenario
1 . La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ............................................................................................................. 77

Figura 5-17 Mapa del percentil 98 de las concentraciones diarias de MP 2,5 (g/m [3] ) para el escenario
2. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ............................................................................................................. 78

Figura 5-18 Mapa del percentil 98 de las concentraciones diarias de MP 2,5 (g/m [3] ) para el escenario
3 . La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ............................................................................................................. 79

Figura 5-19 Mapa del percentil 98 de las concentraciones diarias de MP 2,5 (g/m [3] ) para el escenario
4 . La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ............................................................................................................. 80

Figura 5-20. Relación entre concentraciones horarias de NOx y de NO 2 en la estación de monitoreo
La Florida, Talca, años 2017-2018. Fuente: http://sinca.mma.gob.cl ............................................... 81

Figura 5-21 Mapa de concentraciones del NO 2 anual (g/m [3] ) para el escenario 1. La ciudad de Teno
está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................... 84

Figura 5-22 Mapa de concentraciones del NO 2 anual (g/m [3] ) para el escenario 2. La ciudad de Teno
está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................... 85

Figura 5-23 Mapa de concentraciones del NO 2 anual (g/m [3] ) para el escenario 3. La ciudad de Teno
está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................... 86

Figura 5-24 Mapa de concentraciones del NO 2 anual (g/m [3] ) para el escenario 4. La ciudad de Teno
está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................... 87

Figura 5-25 Mapa de concentraciones horarias máximas del NO 2 (g/m [3] ) para el escenario 1. La
ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con
una línea poligonal azul. .................................................................................................................... 90

Figura 5-26 Mapa de concentraciones horarias máximas del NO 2 (g/m [3] ) para el escenario 2. La
ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con
una línea poligonal azul. .................................................................................................................... 91

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 8 de 147

Código V01: FI-A.03-DSA

Figura 5-27 Mapa de concentraciones horarias máximas del NO 2 (g/m [3] ) para el escenario 3. La
ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con
una línea poligonal azul. .................................................................................................................... 92

Figura 5-28 Mapa de concentraciones horarias máximas del NO 2 (g/m [3] ) para el escenario 4. La
ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con
una línea poligonal azul. .................................................................................................................... 93

Figura 5-29 Mapa de concentraciones del SO 2 anual (g/m [3] ) para el escenario 1. La ciudad de Teno
está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................... 96

Figura 5-30 Mapa de concentraciones del SO 2 anual (g/m [3] ) para el escenario 2. La ciudad de Teno
está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................... 97

Figura 5-31 Mapa de concentraciones del SO 2 anual (g/m [3] ) para el escenario 3. La ciudad de Teno
está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................... 98

Figura 5-32 Mapa de concentraciones del SO 2 anual (g/m [3] ) para el escenario 4. La ciudad de Teno
está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................... 99

Figura 5-33 Mapa del percentil 99 de las concentraciones diarias de SO 2 (g/m [3] ) para el escenario 1.
La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ........................................................................................................... 102

Figura 5-34 Mapa del percentil 99 de las concentraciones diarias de SO 2 (g/m [3] ) para el escenario 2.
La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ........................................................................................................... 103

Figura 5-35 Mapa del percentil 99 de las concentraciones diarias de SO 2 (g/m [3] ) para el escenario 3.
La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ........................................................................................................... 104

Figura 5-36 Mapa del percentil 99 de las concentraciones diarias de SO 2 (g/m [3] ) para el escenario 4.
La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ........................................................................................................... 105

Figura 5-37 Mapa de percentil 99 de las concentraciones horarias del SO 2 (g/m [3] ) para el escenario
1. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ........................................................................................................... 108

Figura 5-38 Mapa de percentil 99 de las concentraciones horarias del SO 2 (g/m [3] ) para el escenario
2. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ........................................................................................................... 109

Figura 5-39 Mapa de percentil 99 de las concentraciones horarias del SO 2 (g/m [3] ) para el escenario
3. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ........................................................................................................... 110

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 9 de 147

Código V01: FI-A.03-DSA

Figura 5-40 Mapa de percentil 99 de las concentraciones horarias del SO 2 (g/m [3] ) para el escenario
4. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado
con una línea poligonal azul. ........................................................................................................... 111

Figura 5-41 Mapa de percentil 99,73 de las concentraciones horarias del SO 2 (g/m [3] ) para el
escenario 1. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está
marcado con una línea poligonal azul. ............................................................................................ 112

Figura 5-42 Mapa de percentil 99,73 de las concentraciones horarias del SO 2 (g/m [3] ) para el
escenario 2. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está
marcado con una línea poligonal azul. ............................................................................................ 113

Figura 5-43 Mapa de percentil 99,73 de las concentraciones horarias del SO 2 (g/m [3] ) para el
escenario 3. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está
marcado con una línea poligonal azul. ............................................................................................ 114

Figura 5-44 Mapa de percentil 99,73 de las concentraciones horarias del SO 2 (g/m [3] ) para el
escenario 4. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está
marcado con una línea poligonal azul. ............................................................................................ 115

Figura 5-41 Mapa de concentraciones horarias máximas de CO (g/m [3] ) para el escenario 1. La ciudad
de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una
línea poligonal azul. ......................................................................................................................... 118

Figura 5-42 Mapa de concentraciones horarias máximas de CO (g/m [3] ) para el escenario 2. La ciudad
de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una
línea poligonal azul. ......................................................................................................................... 119

Figura 5-43 Mapa de concentraciones horarias máximas de CO (g/m [3] ) para el escenario 3. La ciudad
de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una
línea poligonal azul. ......................................................................................................................... 120

Figura 5-44 Mapa de concentraciones horarias máximas de CO (g/m [3] ) para el escenario 4. La ciudad
de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una
línea poligonal azul. ......................................................................................................................... 121

Figura 5-45 Mapa de concentraciones máximas de CO (g/m [3] ) promedio de 8 horas, para el
escenario 1. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está
marcado con una línea poligonal azul. ............................................................................................ 124

Figura 5-46 Mapa de concentraciones máximas de CO (g/m [3] ) promedio de 8 horas, para el
escenario 2. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está
marcado con una línea poligonal azul. ............................................................................................ 125

Figura 5-47 Mapa de concentraciones máximas de CO (g/m [3] ) promedio de 8 horas, para el
escenario 3. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está
marcado con una línea poligonal azul. ............................................................................................ 126

Figura 5-48 Mapa de concentraciones máximas de CO (g/m [3] ) promedio de 8 horas, para el
escenario 4. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está
marcado con una línea poligonal azul. ............................................................................................ 127

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 10 de 147

Código V01: FI-A.03-DSA

Figura 5-49. Mapa de concentraciones anuales de plomo (g/m [3] ), para los escenarios 1 (panel
superior), y 2 (panel inferior). La ciudad de Teno está delimitada por el polígono negro. El perímetro
del proyecto está marcado con una línea poligonal azul. ............................................................... 129

Figura 5-50 Mapa de depositación anual de azufre (eq/[ha año]) para el escenario 1. La ciudad de
Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................. 132

Figura 5-51 Mapa de depositación anual de azufre (eq/[ha año]), para el escenario 2. La ciudad de
Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................. 133

Figura 5-52 Mapa de depositación anual de azufre (eq/[ha año]), para el escenario 3. La ciudad de
Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................. 134

Figura 5-53 Mapa de depositación anual de azufre (eq/[ha año]), para el escenario 4. La ciudad de
Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una línea
poligonal azul. ................................................................................................................................. 135

Figura 5-54 Mapa de depositación anual de nitrógeno (eq/[ha año]), para el escenario 1. La ciudad
de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una
línea poligonal azul. ......................................................................................................................... 136

Figura 5-55 Mapa de depositación anual de nitrógeno (eq/[ha año]), para el escenario 2. La ciudad
de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una
línea poligonal azul. ......................................................................................................................... 137

Figura 5-56 Mapa de depositación anual de nitrógeno (eq/[ha año]), para el escenario 3. La ciudad
de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una
línea poligonal azul. ......................................................................................................................... 138

Figura 5-57 Mapa de depositación anual de nitrógeno (eq/[ha año]), para el escenario 4. La ciudad
de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una
línea poligonal azul. ......................................................................................................................... 139

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 11 de 147

Código V01: FI-A.03-DSA

**1.** **RESUMEN EJECUTIVO**

Se ha realizado una modelación de las emisiones atmosféricas de la Planta Teno de Cementos Bío

Bío S.A. en adelante Planta Teno Cbb, tanto para sus emisiones actuales como para la fase de
operación del proyecto “APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN
CBB PLANTA TENO”, Región del Maule, considerando también otras fuentes de emisión del sector,
analizando los siguientes cuatro escenarios:

Emisiones actuales de la Planta Teno CBB. Se consideran 7 fuentes de emisión
**Escenario 1:**
según emisiones especificadas en Tabla 4-1 y Tabla 4-3.

Emisiones de la Planta Teno CBB con la implementación del Proyecto
**Escenario 2:**
“APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB

PLANTA TENO”. En este caso, sólo se afecta la fuente 1, que corresponde al horno
clínker, para la cual se consideran las emisiones con proyecto indicadas en Tabla
4-1. Las demás fuentes de la planta Teno Cbb mantienen invariables sus niveles
operacionales y emisiones con la implementación del proyecto, las que se indican

en

Tabla 4-3. Los escenarios 1 y 2 permiten estimar los efectos solamente atribuibles
a las emisiones de la planta Teno CBB en la implementación del Proyecto.

Emisiones actuales de la Planta Teno de CBB (Escenario 1, según emisiones
**Escenario 3:**
especificadas en Tabla 4-1 y
Tabla 4-3) más las emisiones actuales de la central térmica Energía Latina (según
RCA N°43/2008, 36 turbinas de generación eléctrica), según su despacho eléctrico
2018 (informado por CDEC), las de la planta de paneles MDP de Arauco (Fuente:
Anexo de Informe de Modelación de Dispersión Atmosférica de Contaminantes
Planta de MDP Teno de Paneles Arauco, abril 2010 del proyecto “Planta de
Paneles MDP Teno”, aprobado mediante RCA N°191, del 01/Octubre/2010,
especificadas en Tabla 4-4 y las de la Planta de Elaboración de Alimento para
Mascotas de Nestlé Chile S.A. (etapa 1). Este escenario, permite contrastar los
resultados de la modelación con los niveles de calidad del aire medidos y así
realizar un análisis de sensibilidad del modelo de dispersión, reduciendo la

incertidumbre en la modelación.

Emisiones de la Planta Teno de Cbb con la implementación del Proyecto
**Escenario 4:**
“APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB

PLANTA TENO”, (Escenario 2) detalladas en Tabla 4-1 y Tabla 4-3 más las
emisiones de la central térmica Energía Latina y las de la planta de paneles MDP
de Arauco (mismas del escenario 3) y las de la planta de alimentos de mascotas
de Nestlé S.A. (etapa 2) indicadas en
Tabla 4-3 Además, se incluye la operación de 6 turbinas adicionales en la central
Teno de Energía Latina, según lo declarado en el Anexo F, Informe de Modelación
de Calidad del Aire presentado por Energía Latina S.A. en diciembre de 2016, como
parte de la Adenda al Proyecto “Central de Generación Eléctrica a Gas Teno”, el
cual fue aprobado según RCA N° 29 del 6 de abril de 2017, señaladas en

Tabla 4-3

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 12 de 147

Código V01: FI-A.03-DSA

En primer lugar, se modeló la meteorología en la zona usando el modelo numérico de pronóstico
WRF [1] . Posteriormente, se aplicó el modelo CALPUFF para la modelación de las emisiones de los
cuatro escenarios arriba mencionados. Se considera como año base de los cálculos y modelaciones
el año 2018. Se encontró que el modelo WRF tiende a sobrestimar la velocidad del viento medido
en la estación meteorológica ubicada en la planta Teno CBB; además el modelo WRF estima muy
bien el predominio de la dirección S y SW del viento en la zona durante todo el año; para la altura
de mezclado en la zona, el modelo estima bien el comportamiento en los meses fríos (Abril a
Agosto), pero sobrestima la altura de mezclado en primavera y verano. Para estimar un factor de
corrección para el modelo de dispersión, se comparó la modelación del año 2018 (con escenario 3
de emisiones) con los datos de calidad del aire 2018 disponibles en la estación ENLASA. De esta
forma se consigue reducir la incertidumbre en las predicciones del modelo de dispersión.

Para el análisis de resultados de las modelaciones de los cuatro escenarios arriba descritos, se
considera que el nivel actual de calidad del aire representa el aporte de todas las fuentes emisoras
en su situación normal de funcionamiento el año 2018. El aporte por el proyecto de CBB considera
el aumento de emisiones de CBB en la condición con Proyecto. El aporte por todos los proyectos
considera el aumento de emisiones respecto de la situación normal, considerando los otros
proyectos en desarrollo en la zona. El nivel actual calidad del aire más proyectos corresponden al
nuevo nivel de calidad del aire de implementarse plenamente todos los proyectos ambientalmente
aprobados.

El primer punto de interés modelado corresponde al punto de máximo impacto asociado a la Planta
CBB Teno, puesto que en este punto los efectos del proyecto en la calidad del aire serían los más
altos. La Tabla 1-1 resume los principales resultados obtenidos a partir de la modelación en el punto
de máximo impacto (PMI) para la planta Teno CBB. Se aprecia que para todos los contaminantes
regulados se cumple ampliamente con sus respectivas normas de calidad del aire en la situación
actual, ya que todos los parámetros se encuentran bajo su respectivo nivel de latencia. La
implementación del Proyecto no va a cambiar de manera significativa ninguno de los parámetros de
calidad del aire, debido a que los cambios en emisiones atmosféricas del Proyecto son marginales.
Por ejemplo, a excepción del MP 10 anual (bajo el 70% de la norma), todos los demás contaminantes
van a estar a concentraciones menores o iguales al 50% de la respectiva norma. Además, la
implementación plena de los proyectos ambientalmente aprobados tampoco va a modificar de
manera significativa la actual situación de calidad del aire en dicho punto de interés, ya que todos
los contaminantes se mantendrán bajo la condición de latencia. En este escenario sinérgico, el MP 10
anual se mantiene bajo el 70% de la norma y los demás contaminantes bajo el 50% de la norma
respectiva, excepto el MP 2,5 diario que alcanza el 52% de la norma.

El segundo punto de interés corresponde a la ubicación de la Estación de Monitoreo de calidad del
aire ENLASA, ya que en este lugar se conocen los respectivos niveles de calidad del aire (línea base,
situación sin proyecto). Finalmente, siendo la localidad de Teno la más cercana al proyecto, se
analizan 5 receptores discretos, que cubren todo el contorno de esta localidad. Las coordenadas de
los seis receptores discretos, se identifican en coordenadas UTM en la siguiente Figura 1-1 y Tabla

1-2.

1 [Weather Research and Forecasting Model, disponible en “http://www.wrf-model.org”](http://www.wrf-model.org/)

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 13 de 147

Código V01: FI-A.03-DSA

**Tabla 1-1 Concentraciones ambientales de MP** **10** **, MP** **2.5** **, NO** **2** **, SO** **2** **, CO y Pb en PMI y porcentajes según niveles de**

**calidad del aire normados**

|Parámetro|Norma de<br>calidad del<br>aire<br>g/m3N (1)|Nivel<br>actual<br>Calidad del<br>aire<br>g/m3N (2)|Porcentaje<br>c. aire<br>actual<br>c/r a<br>norma de<br>calidad|Aporte por<br>proyecto<br>CBB<br>g/m3N<br>(3)|Aporte por<br>todos los<br>proyectos<br>g/m3N<br>(4)|Nivel c.<br>aire con<br>proyectos<br>g/m3N<br>(5)|Porcentaje<br>calidad<br>aire por<br>proyecto<br>CBB c/r a<br>norma<br>calidad<br>aire|Porcentaje<br>c. aire con<br>proyectos<br>c/r a<br>norma de<br>calidad|
|---|---|---|---|---|---|---|---|---|
|MP10 Anual|50|33,8|68%|0,4|0,7|34,5|68%|69%|
|MP10 P98 Diario|150|69,7|46%|0,5|3,0|72,7|47%|48%|
|MP2.5 Anual|20|7,5|38%|0,2|0,5|8,0|39%|40%|
|MP2.5 P98 Diario|50|24|48%|0,3|2,0|26,0|49%|52%|
|SO2 Anual|60|6,3|11%|-0,2|-0,2|6,1|10%|10%|
|SO2 P99 Diario (6)|150|38,3|26%|-0,8|-0,3|38,0|25%|25%|
|SO2 P99 Horario|350|64,1|18%|-1,8|-1,5|62,6|18%|18%|
|SO2 P99,73<br>Horario (7)|700|105,1|15%|-2,4|-0,7|104,5|15%|15%|
|NO2 Anual|100|18,7|19%|0,5|3,1|21,8|19%|22%|
|NO2 P.99 Horario|400|67|17%|3,2|7,1|74,1|18%|19%|
|CO P99 Horario|30,000|1000|3%|5,4|0,2|1000,2|3%|3%|
|CO P99 8 horas|10,000|700|7%|2,4|1,0|701,0|7%|7%|
|Pb Anual|0,5|S/i||0,003|0,003|||S/i|

(1) Las normativas primarias de calidad del aire utilizadas son D.S N°12/2010 para MP2,5, D.S N°59/1998 para

MP10, D.S N°104/2018 para SO 2, D.S N°114/2002 para NO 2, D.S N°115/2002 para CO, D.S N°136/2000 para
Pb y D.S N°22/2009 para norma secundaria horario de SO 2 .
(2) Valor medido en estación de monitoreo de calidad del aire ENLASA
(3) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual: Escenario 2

- Escenario 1.

(4) Corresponde a la resta de Escenario 4 - Escenario 3. En este caso, se consideran los efectos del proyecto

más los otros proyectos no materializados.
(5) Al nivel actual se suma el aporte de todos los proyectos, que es el máximo entre (3) y (4).
(6) No se evalúa norma secundaria SO 2 P99,7 Diario de 260 ug/m3N, ya que es menos estricta que la norma

primaria.
(7) SO 2 P99,73 Horario, corresponde a la norma secundaria.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 14 de 147

Código V01: FI-A.03-DSA

**Figura 1-1. Ubicación de los Receptores R_1 a R_6 considerados en el análisis**

La Tabla 1-2 presenta las coordenadas de los receptores discretos de interés.

**Tabla 1-2. Ubicación receptores discretos (UTM, huso 19 H, WGS84)**

|Código|Receptor|UTM E [m]|UTM N [m]|
|---|---|---|---|
|R_1|Estación ENLASA(1)|305.205|6.140.221|
|R_2|Teno Norte|302.574|6.139.767|
|R_3|Estación FFCC Teno|302.668|6.139.114|
|R_4|Teno SE|302.714|6.138.326|
|R_5|Teno Sur|302.094|6.138.431|
|R_6|Teno Oeste|301.377|6.139.114|

(1) Corresponde a la estación de monitoreo de calidad del aire.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 15 de 147

Código V01: FI-A.03-DSA

La Tabla 1-3 presenta el cambio de las concentraciones ambientales en la estación de monitoreo de
calidad del aire ENLASA. También se aprecia que los parámetros de calidad del aire no se van a
modificar significativamente, ya que los impactos en calidad del aire son muy bajos e incluso
negativos en el caso del SO 2, ya que sus emisiones se reducen de 15,5 g/s a 15 g/s en el escenario
de implementación del Proyecto. En este caso, tanto para la implementación del proyecto CBB como
cuando los demás proyectos también se implementan en la zona, todos los contaminantes se
mantendrán bajo el 50% de su respectiva norma de calidad del aire, excepto el MP 10 anual que se
mantendrá bajor el 70%.

**Tabla 1-3 Concentraciones ambientales de MP** **10** **, MP** **2.5** **, NO** **2** **, SO** **2** **, CO y Pb en Estación de Calidad del Aire ENLASA y**

**porcentajes según niveles de calidad del aire normados**

|Parámetro|Norma de<br>calidad del<br>aire<br>g/m3N (1)|Nivel<br>actual<br>Calidad del<br>aire<br>g/m3N (2)|Aporte<br>por<br>proyecto<br>CBB (3)|Aporte<br>por todos<br>los<br>proyectos<br>(4)|Nivel<br>actual<br>mas<br>proyectos<br>(5)|Porcentaj<br>e c. aire<br>actual<br>c/r a<br>norma de<br>calidad|Porcentaj<br>e<br>respecto<br>a norma<br>de<br>calidad|
|---|---|---|---|---|---|---|---|
|MP10 Anual|50|33,8|0,2|0,3|34,1|68%|68%|
|MP10 P98 Diario|150|69,7|0,7|1,2|70,9|46%|47%|
|MP2.5 Anual|20|7,5|0,1|0,2|7,7|38%|39%|
|MP2.5 P98 Diario|50|24|0,3|0,9|24,9|48%|50%|
|SO2 Anual|60|6,3|-0,1|-0,1|6,2|11%|10%|
|SO2 P99 Diario (6)|150|38,3|-0,6|-0,6|37,7|26%|25%|
|SO2 P99 Horario|350|64,1|-1,1|-1,1|63,0|18%|18%|
|SO2 P99,73<br>Horario (7)|700|105,1|-1,3|-1,6|103,5|15%|15%|
|NO2 Anual|100|18,7|0,3|0,8|19,5|19%|19%|
|NO2 P.99 Horario|400|67|2,9|5,5|72,5|17%|18%|
|CO P99 Horario|30,000|1000|4,3|36,3|1036,3|3%|3%|
|CO P99 8 horas|10,000|700|1,7|25,8|725,8|7%|7%|
|Pb Anual|0,5|S/i|0,0014|0,0014||||

En el caso de la **zona urbana de Teno**, las Tablas de resultados para los receptores discretos y los
gráficos que muestran toda la distribución espacial de los contaminantes modelados indican que la
implementación del Proyecto aportará:

a) Menos de 1 g/m [3] y de 4 g/m [3] para el MP 10 anual y percentil 98 diario, respectivamente

b) Menos de 1 g/m [3] y de 4 g/m [3] para el MP 2,5 anual y percentil 98 diario, respectivamente

c) Menos de 0,5 g/m [3], 3,5 g/m [3] y 6 g/m [3] para el SO 2 anual, percentil 99 diario y horario,

respectivamente

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 16 de 147

Código V01: FI-A.03-DSA

d) Menos de 1 g/m [3] y 60 g/m [3] para el NO 2 anual y percentil 99 horario, respectivamente

e) Menos de 20 g/m [3] y 4 g/m [3] para el CO percentil 99 de 1h y 8h, respectivamente

En la condición más pesimista (caso del PMI Planta Teno CBB), se encuentra que:

`o` Respecto del **MP** **10**, la concentración anual subiría 0,75 g/m [3] (de los cuales solo 0,38 g/m [3] son

atribuibles a la implementación del Proyecto CBB), llegando a un 69% de la norma anual. Para la

norma diaria, la concentración subiría 3 g/m [3] (de los cuales solo 0,5 g/m [3] son atribuibles a la

implementación del Proyecto CBB), llegando a un 48% de la norma.

`o` Respecto del **MP** **2,5**, la concentración anual subiría 0,5 g/m [3] (de los cuales solo 0,2 g/m [3] son

atribuibles a la implementación del Proyecto CBB), llegando a un 40% de la norma anual. Para la

norma diaria, la concentración subiría 2 g/m [3] (de los cuales solo 0,3 g/m [3] son atribuibles a la

implementación del Proyecto CBB), llegando a un 52% de la norma.

`o` Respecto de **NO** **2**, la concentración anual subiría 3,14 g/m [3] (de los cuales solo 0,5 g/m [3] son

atribuibles a la implementación del Proyecto CBB), llegando a un 22% de la norma anual. Para la

norma horaria (percentil 99), la concentración subiría 7,1 g/m [3] (de los cuales solo 3,2 g/m [3] son

atribuibles a la implementación del Proyecto CBB), llegando a un 19% de la norma.

`o` Respecto del **SO** **2**, la concentración anual se reduciría en 0,22 g/m [3] (reducción de 0,2 g/m [3]

atribuibles a la implementación del Proyecto CBB), llegando a un 10% de la norma anual. Para la

norma diaria (percentil 99), la concentración se reduciría en 0,3 g/m [3] (reducción de 0,8 g/m [3]

atribuibles a la implementación del Proyecto CBB), llegando a un 25% de la norma. Para la norma

horaria (percentil 99), la concentración se reduciría en 1,5 g/m [3] (reducción de 1,8 g/m [3]

atribuibles a la implementación del Proyecto CBB), llegando a un 18% de la norma.

`o` Respecto del **CO**, la concentración de 1h (percentil 99) subiría 5 g/m [3] (todos atribuibles a la

implementación del Proyecto CBB), llegando a un 3% de la norma anual. Para la concentración

de 8h (percentil 99), la concentración subiría 2 g/m [3] (de los cuales 1 g/m [3] son atribuibles a la

implementación del Proyecto CBB), llegando a un 7% de la norma.

`o` Respecto del **Plomo**, único metal pesado con norma de calidad del aire, no se dispone de

mediciones de calidad del aire, sin embargo, en el PMI se puede señalar que los niveles de

emisión del proyecto estarían en el orden del 0,5 % de la norma de calidad del aire para este

contaminante. El PMI es distinto al caso de MP y gases, ubicándose en el punto de coordenadas

305.431 m E y 6.141.387 m N (a 3,7 km al NE de Teno, ver Figura 5-3).

`o` Respecto del **Azufre** depositado en el suelo, se determinó que en el punto de máximo impacto

la depositación estaba por debajo del 20 % del nivel de referencia y a 1 km del PMI, los valores

de depositación se reducen al 8 % del nivel de referencia o menos. A más de 1 km del PMI, los

aportes son marginales. El PMI es el mismo que en el caso de MP y gases (UTM 304.470 m E y

6.140.362 m N).

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 17 de 147

Código V01: FI-A.03-DSA

En resumen, la implementación del Proyecto “APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE COPROCESAMIENTO EN CBB PLANTA TENO”, Región del Maule, no va a modificar el estado de la calidad
del aire en la zona de Teno, ya que todos los contaminantes normados se mantendrán bajo la
condición de latencia (la mayoría bajo el 50% del valor de la respectiva norma de calidad del aire),
tanto con la implementación del Proyecto como en el caso que los otros proyectos ambientalmente
aprobados se implementen en la zona.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
**"APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO", VII REGIÓN**

**Informe Final**

Página 18 de 147

Código V01: FI-A.03-DSA

**2.** **INTRODUCCIÓN Y OBJETIVOS**

El presente estudio desarrolla una modelación de la dispersión de las emisiones atmosféricas de
MP 10, MP 2.5, SO 2, NO x y Plomo, asociadas a la operación del Proyecto: “APLICACIÓN DE ECONOMÍA
CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB PLANTA TENO”, Región del Maule,
determinando los niveles de calidad del aire resultantes de la implementación del Proyecto.

**Objetivos**

✓ Modelar el aporte a las concentraciones ambientales de MP 10, MP 2.5, SO 2, NO x, CO y Plomo

asociadas a la operación del Proyecto: “APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE COPROCESAMIENTO EN CBB PLANTA TENO”, Región del Maule.
✓ Determinar los niveles de calidad del aire a obtener con la implementación del proyecto,

considerando también otros proyectos vigentes en la zona y en vías de implementación.

**3.** **LÍNEA BASE DE CALIDAD DEL AIRE Y METEOROLOGÍA.**

La línea base de calidad del aire está disponible para el año 2018 en la estación de monitoreo de
calidad del aire perteneciente a Energía Latina (estación ENLASA), ubicada en el punto de
coordenadas UTM (DATUM WGS84 - 19H) 305.205 m E y 6.140.221 m N, como se aprecia en la
Figura 3-1. La información de meteorología corresponde a la estación de monitoreo ubicada en la
Planta Teno de CBB y con coordenadas UTM (DATUM WGS84 - 19H) 304.682 m y 6.139.515 m N
(ver Figura 3-1). Se observa que la distancia entre ambas estaciones de monitoreo es de 876 metros.

La Tabla 3-1 resume la calidad del aire en la zona del Proyecto, medida en la estación ENLASA. En
ella se puede apreciar que todos los contaminantes presentan niveles por debajo de la saturación y
la latencia (80% de la norma), respecto de sus normas de calidad del aire, siendo el MP 10 el
contaminante más cercano al nivel de la norma con un 67,6 % del período diario y 46,5 % del período
anual. Los valores de MP 2,5 están por debajo del 40 % de la norma anual y del 48 % de la norma
diaria. Respecto de NO 2, se tiene un valor horario en 16,8 % y un valor anual en 18,7 % del valor
normado, respectivamente. El SO 2 horario percentil 99 está en un 25,2 %, el SO 2 diario percentil 99
en 25,5 % y el SO 2 anual en 10,5 % de la norma, respectivamente. Con relación al CO, éste presenta
niveles por debajo del 10%. Respecto del plomo, no se dispone de mediciones en la zona. Para la
norma secundaria de SO 2, el percentil 99,73 del SO 2 horario está en un 11,6 % del valor regulado.

En resumen, los actuales niveles de calidad del aire en la zona de Teno son buenos, y ellos consideran
la operación de las actuales fuentes de emisión de la zona. A continuación, se presenta la descripción
de la meteorología en la zona del proyecto.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO"., VII REGIÓN**

**Informe Final**

Página 19 de 147

Código V01: FI-A.03-DSA

**Figura 3-1. Estaciones de monitoreo meteorológica de CBB y de estación de calidad del aire ENLASA.**

**Tabla 3-1 Línea base de calidad del aire en estación ENLASA**

|Parámetro|Norma de<br>calidad del aire<br>g/m3N|Nivel actual<br>Calidad del aire<br>2016<br>g/m3N|Nivel actual<br>Calidad del aire<br>2017<br>g/m3N|Nivel actual<br>Calidad del aire<br>2018<br>g/m3N|Promedio Trianual<br>2016-2018<br>Calidad del aire<br>2018<br>g/m3N|
|---|---|---|---|---|---|
|MP10 Anual|50|38,0|33,4|30,0|33,8|
|MP10 P98 Diario|150|74|73|62|69,7|
|MP2.5 Anual|20|6,1|5,8|10,5|7,5|
|MP2.5 P98 Diario|50|12,1|13,7|46,1|24,0|
|SO2 Anual|60|9,7|5,1|4,2|6,3|
|SO2 P99 Diario|150|60,4|32,5|21,9|38,3|
|SO2 P99 Horario|350|169,7|60,5|34,7|88,3|
|SO2 P99,73 Horario|700|97,1|91,7|53,9|80,9|
|NO2 Anual|100|19,9|19,4|16,7|18,7|
|NO2 P.99 Horario|400|70,3|67,0|63,7|67,0|
|CO P99 Horario|30.000|600|600|700|667|
|CO P99 8 horas|10.000|500|588|588|559|

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO"., VII REGIÓN**

**Informe Final**

Página 20 de 147

Código V01: FI-A.03-DSA

**1.1** **CARACTERÍSTICAS DE LA METEOROLOGÍA EN LA ZONA DE TENO**

Las figuras que se presentan en esta sección, muestran las variables de velocidad del viento,
dirección del viento y temperatura medidas en la zona de Teno, específicamente en la estación de
monitoreo meteorológico de CBB, ubicada en las coordenadas UTM (WGS84, huso 19S) 302.013 m
E y 6.139.056 m N.

La Figura 3-2 muestra la serie cronológica de la velocidad del viento medida en el año 2018
completo. Los datos horarios disponibles son del 99,9%. Para apreciar mejor la estacionalidad del
viento horario, la Figura 3-3 muestra el perfil promedio del viento durante todo el año. Se aprecia
que el viento se intensifica en los meses de primavera y verano y se debilita en los meses de invierno.
Esto se debe al clima mediterráneo con estación seca prolongada de la zona, lo cual favorece el
desarrollo de circulación del viento valle-montaña durante el día, y menores velocidades del viento
de noche, con un perfil claro de máximas velocidades por las tardes.

**Figura 3-2 Serie cronológica de datos estación de monitoreo Planta Teno**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO"., VII REGIÓN**

**Informe Final**

Página 21 de 147

Código V01: FI-A.03-DSA

**Figura 3-3 Perfiles diarios de la velocidad del viento, Planta Teno.**

La Figura 3-4 muestra las rosas del viento para todo el año y para diferentes horas del día. Se aprecia
que durante todo el año los vientos predominantes en frecuencia son de dirección S y SW, asociados
al forzamiento causado por el calentamiento de la superficie en condiciones diurnas y a la presencia
cuasi-permanente del anticiclón del Pacífico subtropical; solamente en las madrugadas hay una
componente de viento predominante de dirección E, asociada al enfriamiento nocturno del suelo y
a vientos montaña-valle inducidos por las diferencias de la elevación de terreno.

En resumen, la meteorología superficial indica que la mayor parte del tiempo el viento no va a
transportar las emisiones de la Planta Teno CBB hacia la ciudad de Teno.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO"., VII REGIÓN**

**Informe Final**

Página 22 de 147

Código V01: FI-A.03-DSA

|Col1|Col2|
|---|---|
|a) Todas las horas|b) De 8:00 a 19:00 h|
||<br>|
|c) De 20:00 a 23:00 h|d) De 0:00 a 7:00 h|

**Figura 3-4. Rosas del viento anuales : a) todas las horas, b) de 8 a 19 horas, c) de 20 a 23 horas, d) de 0 a 7 am.**

La Figura 3-5 muestra una serie cronológica de datos de temperatura medidos en Planta Teno CBB.
El porcentaje de datos disponibles en el año es del 99,9%.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO"., VII REGIÓN**

**Informe Final**

Página 23 de 147

Código V01: FI-A.03-DSA

**Figura 3-5. Serie cronológica de temperaturas medidas en Planta Teno CBB. Temperatura, °C.**

**Figura 3-6. Perfiles diarios de la temperatura a lo largo del año en Planta Teno. Temperatura, °C.**

En la Figura 3-6 se aprecia que la temperatura tiene una clara estacionalidad asociada al clima
mediterráneo de la zona, con mínimas temperaturas en invierno, y donde diariamente las máximas
temperaturas se presentan entre las 17 y 19 hora local.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO"., VII REGIÓN**

**Informe Final**

Página 24 de 147

Código V01: FI-A.03-DSA

**1.2** **MODELACIÓN DE LA METEOROLOGÍA EN LA ZONA.**

El modelo numérico de pronóstico WRF [2] fue corrido con la configuración recomendada por la Guía
del SEA, y consistió en usar cuatro dominios anidados de modelación del tiempo, tres de los cuales
(D2 a D4) se muestran en la Figura 3-7. El dominio más pequeño modelado D4, es de 63 x 63 km de
extensión, fue simulado con una resolución horizontal de 1 km.

El desempeño del modelo WRF fue evaluado de la siguiente forma:

a) La meteorología superficial modelada por WRF fue comparada con la información de

meteorología superficial de la Planta Teno, la cual se resumió en la sección anterior.
b) La meteorología modelada por WRF en altura fue comparada con las mediciones del

radiosondeo de Santo Domingo, el cual cae dentro del dominio D2 de WRF, lo que se
muestra en la Figura 3-7.

**Figura 3-7: Dominios D2, D3 y D4 de la modelación meteorológica de WRF.**

2 [The Weather Research and Forecasting Model, disponible en “http://www.wrf-model.org”](http://www.wrf-model.org/)

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO"., VII REGIÓN**

**Informe Final**

Página 25 de 147

Código V01: FI-A.03-DSA

**3.2.1 Desempeño del modelo WRF con respecto a la meteorología superficial en Teno**

El modelo WRF es evaluado en forma cualitativa utilizando gráficos, y en forma cuantitativa
utilizando indicadores estadísticos. En ambos análisis se utilizó el software de dominio público R, e
incluyendo el paquete de análisis de calidad del aire `openair` `[3]` .

**3.2.1.1 Evaluación gráfica del modelo WRF**

Con respecto a la velocidad del viento, el modelo tiende a sobrestimar las velocidades,
particularmente entre el mediodía y la puesta del sol (Figura 3-8). Este problema es típico de las
modelaciones de WRF realizadas con la configuración de WRF recomendada por el SEA, que
corresponde a la que se aplicó también en este caso.

En segundo lugar, el modelo WRF reproduce muy bien la dirección del viento, en toda época del
año, especialmente el citado predominio de direcciones S y SW todo el año (Figura 3-9). Solo en las
noches el modelo no captura el viento E predominante en condiciones de madrugada.

En tercer lugar, el desempeño del modelo es muy bueno para las temperaturas, con una leve
sobrestimación entre las 6 am y 6 pm (Figura 3-10). Esta sobrestimación está correlacionada con la
sobrestimación de la velocidad del viento, ya que en condiciones diurnas el forzamiento térmico del
viento es causado por el calentamiento de la superficie, el que a su vez controla el ascenso diurno
de la temperatura del aire.

En resumen, la evaluación gráfica indica que la temperatura y velocidad del viento modeladas por
WRF están muy correlacionadas con las observaciones en la planta Teno CBB. En la siguiente sección
vamos a evaluar cuantitativamente el desempeño del modelo WRF.

3 [Disponible en: http://www.openair](http://www.openair-project.org/) project.org/

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO"., VII REGIÓN**

**Informe Final**

Página 26 de 147

Código V01: FI-A.03-DSA

**Figura 3-8. Variabilidad temporal de los vientos año 2018, estación Planta Teno CBB.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO"., VII REGIÓN**

**Informe Final**

Página 27 de 147

Código V01: FI-A.03-DSA

**Figura 3-9. Comparación de rosas de viento observada y modelada año 2018, Planta Teno CBB.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO"., VII REGIÓN**

**Informe Final**

Página 28 de 147

Código V01: FI-A.03-DSA

**Figura 3-10. Variabilidad temporal de la temperatura año 2018, Planta Teno CBB.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO"., VII REGIÓN**

**Informe Final**

Página 29 de 147

Código V01: FI-A.03-DSA

**3.2.1.2 Evaluación estadística del modelo WRF**

Para poder comparar los valores modelados con los observados, se calculan los siguientes
indicadores estadísticos. En las siguientes definiciones, O i representa el i-ésimo valor observado y
M i representa el i-ésimo valor modelado de un total de n observaciones.

**Fracción de predicciones dentro de uno o dos factores (FAC2)**

La fracción de valores modelados dentro de un factor de dos de los valores observados son las

fracciones de las predicciones del modelo que satisfacen:

0.5 ≤ [M] [i]

O i

≤2.0

**Sesgo de la media (MB)**

El sesgo de la media proporciona una buena indicación si la media modelada sobre- o sub- estima

las observaciones:

N

MB = [1]

n [∑M] [i] [ −O] [i]

i=1

**Error bruto de la media (MGE)**

Este error proporciona una buena indicación de la media del error, sin importar si este está sobre o

sub estimado:

N

MGE = [1]

n [∑|M] [i] [ −O] [i]

i=1

**Sesgo de la media normalizado (NMB)**

|

El sesgo de la media normalizado es útil para comparar contaminantes que poseen diferentes
escalas de concentración. El sesgo de la media es normalizado dividiendo por el valor observado:

NMB = [∑] ni=1 (M i −O i )
∑ ni=1 O i

**Error bruto de la media normalizado (NMGE)**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO"., VII REGIÓN**

**Informe Final**

Página 30 de 147

Código V01: FI-A.03-DSA

**wwwdictuccl**

Este error ignora si la predicción está sobre o sub estimada, solo le interesan las desviaciones

absolutas.

NMGB = [∑] ni=1 |M i −O i |
∑ ni=1 O i

**Raíz cuadrática del error cuadrático medio (RMSE)**

∑ ni=1 (M i −O i ) [2]

1/2

RMSE = (

i −O i ) [2]

n
)

**Coeficiente de correlación (r)**

El coeficiente de correlación de Pearson es una medida de la relación lineal entre dos variables.

n

1

r =
(n−1) [∑(M] [i] σ [−M] M

~~)~~ ( [O] [i] σ [−O] O

~~)~~

i=1

σ M

**3.2.1.3 Indicadores estadísticos para la velocidad del viento**

A continuación se presentan los indicadores anuales y estacionales que se obtienen para la

velocidad del viento.

**Tabla 3-2. Estadísticas de desempeño del modelo WRF para el viento año 2018.**

|Indicador|año|verano|otoño|invierno|primavera|
|---|---|---|---|---|---|
|n|8750|2159|2208|2199|2184|
|FAC2|0,74|0,74|0,73|0,73|0,76|
|MB|0,43|0,44|0,43|0,36|0,50|
|MGE|0,73|0,75|0,72|0,70|0,73|
|NMB|0,30|0,29|0,31|0,27|0,34|
|NMGE|0,51|0,50|0,52|0,53|0,49|
|RMSE|0,97|0,96|0,96|1,00|0,95|
|r|0,51|0,56|0,50|0,48|0,49|

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO"., VII REGIÓN**

**Informe Final**

Página 31 de 147

Código V01: FI-A.03-DSA

**wwwdictuccl**

Esta Tabla nos indica que hay poca estacionalidad en los indicadores de desempeño del modelo.
Además, el sesgo medio está por debajo de 0,5 m/s y el RMSE está por debajo de 1 m/s, lo que se
considera un desempeño aceptable para un modelo numérico de pronóstico [4] .

**3.2.1.4 Indicadores estadísticos para la temperatura**

A continuación se presentan los indicadores anuales y estacionales de la temperatura.

**Tabla 3-3. Estadísticas de desempeño del modelo WRF para temperatura año 2018.**

|Indicador|año|verano|otoño|invierno|primavera|
|---|---|---|---|---|---|
|n|8750|2184|2159|2208|2199|
|FAC2|0,91|0,97|1,00|0,93|0,74|
|MB|2,58|1,67|2,42|2,96|3,27|
|MGE|3,32|2,60|3,59|3,44|3,64|
|NMB|0,19|0,12|0,12|0,22|0,45|
|NMGE|0,24|0,19|0,18|0,26|0,50|
|RMSE|4,33|3,47|4,61|4,51|4,62|
|r|0,87|0,84|0,79|0,81|0,69|

En este caso se aprecia una alta correlación (r alto) entre las temperaturas modeladas y observadas,

aunque hay un sesgo positivo de las temperaturas modeladas, como ya se ha mostrado en la Figura

3-10.

4 Fuente: The MMIFstat Statistical Analysis Package, Version 1.0. Alpine Geophysics LLC, Febrero 2010.
Disponible en: [https://www.epa.gov/scram/air-quality-dispersion-modeling-related-model-support-](https://www.epa.gov/scram/air-quality-dispersion-modeling-related-model-support-programs)

[programs](https://www.epa.gov/scram/air-quality-dispersion-modeling-related-model-support-programs)

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO"., VII REGIÓN**

**Informe Final**

Página 32 de 147

Código V01: FI-A.03-DSA

**wwwdictuccl**

**3.2.2 Desempeño de la modelación de WRF para meteorología en altura.**

Se realizó una comparación de las observaciones de magnitud del viento y temperatura realizadas
el año 2018 en la estación de radiosondeo de Santo Domingo (coordenadas UTM: 257.028 m S,
6.273.571 m N, datum WGS84, zona 19 S), por ser la más cercana al sitio del proyecto. Los datos
incluyen mediciones realizadas a las 12 UTC y 00 UTC, que corresponden a las 8 am y 8 pm,
respectivamente, en horario de invierno y a las 9 am y 9 pm en horario de verano, respectivamente.

Los siguientes gráficos permiten comparar el estado de la atmósfera en altura observado en Santo
Domingo con las simulaciones realizadas por el modelo WRF en ese mismo sitio. Para estos fines se
extrajo de la grilla del dominio 2 de WRF el punto más cercano al radiosondeo de Santo Domingo.
Las siguientes figuras muestran las comparaciones de las temperaturas, en la mañana (12 UTC) y en
la noche (00 UTC), respectivamente.

Se aprecia en primer lugar en la Figura 3-11 que en la mañana (12 UTC) WRF predice perfiles de la
temperatura en altura muy similares a los observados, incluyendo la inversión térmica a 1000 m
sobre el suelo, en los meses de enero a marzo y noviembre a diciembre, causada por la condición
de subsidencia inducida por el predominio de la alta presión del Pacífico subtropical.

**Figura 3-11. Comparación de la temperatura observada (panel izquierdo) y modelada (panel derecho) para el año**

**completo modelado con WRF, sitio del radiosondeo de Santo Domingo, a las 12 UTC.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 33 de 147

Código V01: FI-A.03-DSA

La Figura 3-122 muestra que, en condiciones de anochecer (00 UTC) nuevamente el modelo WRF
reproduce bien los perfiles verticales de la temperatura, incluyendo la máxima de temperatura en
altura (alrededor de 1000 m sobre el suelo) característica de la presencia de subsidencia en los
meses de primavera y verano. En los meses fríos los perfiles observados y modelados también están

en buena concordancia.

**Figura 3-12. Comparación de la temperatura observada (panel izquierdo) y modelada (panel derecho) para el año**

**completo modelado con WRF, sitio del radiosondeo de Santo Domingo, a las 00 UTC.**

La Figura 3-13 muestra las diferencias entre los datos del radiosondeo y los modelados por WRF en
la mañana (12 UTC) y al anochecer (00 UTC). Se aprecia que WRF simula mayores temperaturas que
las observadas en superficie, mientras que sobre los 1000 m de altura la tendencia es la opuesta:
menores temperaturas que las observadas. Esto implica que la distribución vertical de las
temperaturas modeladas por WRF produce más inestabilidad que lo observado, llevando a
condiciones de ventilación de contaminantes mejores que las observadas.

La Figura 3-14 muestra que, en las mañanas, el modelo WRF simula una distribución con
estacionalidad muy similar a la observada, pero con sobrestimación de las velocidades a nivel del
suelo, como ya se ha mostrado en el caso de la meteorología superficial. La Figura 3-155 muestra
que, al anochecer, el modelo WRF nuevamente reproduce la variabilidad estacional del viento en
altura, pero a nivel de superficie se sobrestima la magnitud de la velocidad del viento nuevamente.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 34 de 147

Código V01: FI-A.03-DSA

**Figura 3-13. Diferencia entre temperatura observada y modelada para el año completo modelado con WRF, sitio del**

**radiosondeo de Santo Domingo, a las 00 UTC (panel superior) y a las 12 UTC (panel inferior).**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 35 de 147

Código V01: FI-A.03-DSA

**Figura 3-14 Comparación de la velocidad observada (panel izquierdo) y modelada con WRF (panel derecho) para el**

**año completo, sitio del radiosondeo de Santo Domingo, a las 12 UTC.**

**Figura 3-15 Comparación de la velocidad observada (panel izquierdo) y modelada con WRF (panel derecho) para el**

**año completo, sitio del radiosondeo de Santo Domingo, a las 00 UTC.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 36 de 147

Código V01: FI-A.03-DSA

De los resultados para los perfiles verticales de la temperatura y la velocidad del viento, se aprecia
que se presentan dos tendencias en la representación meteorológica generada por el modelo WRF:

✓ Una tendencia a que la atmósfera sea más inestable (especialmente en las mañanas), lo que

tiende a subestimar las concentraciones modeladas.

✓ Una tendencia a sobrestimar el viento a nivel de superficie, lo que hace subestimar las

concentraciones modeladas nuevamente.

Una manera de estimar este efecto de la meterología en el modelo de dispersión consiste en
modelar la mayoría de las fuentes emisoras en la zona y comparar las concentraciones modeladas
con las observadas. Este punto se va a analizar en mayor profundidad en la sección de análisis de
incertidumbre del modelo de dispersión (sección 6 de este Informe), donde se calcula un factor de
corrección para reducir el sesgo meteorológico en la modelación de WRF, y así conseguir que el
modelo de dispersión entregue resultados confiables.

**3.2.3 Desempeño de la modelación de WRF para la altura de mezclado.**

La altura de mezclado es un parámetro que controla hasta qué altura se mezclan los contaminantes
en la columna de aire. La altura de mezclado es mayor en los meses de primavera y verano, ya que
la radiación solar es mayor y por ende la columna de aire se calienta más que en condiciones de
invierno. En otoño e invierno el enfriamiento nocturno del aire superficial (noches más largas) lleva
a condiciones de inversión térmica intensa a nivel del suelo, lo que reduce la altura de mezclado en
estos meses con respecto a primavera y verano.

En el caso particular de este proyecto, donde se modelan solo emisiones de chimeneas, la altura de
mezclado va a controlar hasta qué altura pueden ascender los contaminantes emitidos (inicialmente
a mayor temperatura que la ambiental).

Si la altura de mezclado es baja (menor a 200 m), la pluma de las chimeneas se va a bloquear al
topar con la altura de mezclado, y posteriormente, la pluma de cada chimenea se va a ir dispersando
hacia abajo, hasta alcanzar el nivel del suelo; esto es típico de condiciones nocturnas o al amanecer,

con vientos débiles.

Si la altura de mezclado es alta (sobre 500 m sobre el suelo, por ejemplo), la pluma de cada chimenea
va a alcanzar el suelo solo por su crecimiento viento abajo, sin interactuar con la altura de mezclado,
con impactos que van a depender solamente de la estabilidad atmosférica que predice el modelo.
Esta situación es característica de condiciones al mediodía y al comienzo de la tarde, especialmente
en primavera y verano con alta insolación y temperatura ambiental y condiciones de alta convección
natural, con vientos más intensos.

Las alturas de mezclado modeladas con WRF se presentan en la Figura 3-16. Se aprecia una alta
estacionalidad, con mayores valores en verano y menores en invierno. El crecimiento a lo largo del
día sigue la forma del perfil de la temperatura ambiental. Durante la noche la altura de mezclado
baja a valores cercanos a 100 m sobre el suelo, durante todo el año.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 37 de 147

Código V01: FI-A.03-DSA

**Figura 3-16. Perfiles diarios de la altura de mezclado modelada mediante WRF.**

Para poder comparar los valores de alturas de mezclado modeladas con WRF respecto de los datos
observados, tendríamos que tener, por ejemplo, radiosondeos realizados en Curicó o Teno. Pero
esta información no está disponible. Lo más cercano disponible (Santiago) son estimaciones
experimentales de alturas de mezclado tomadas con un instrumento originalmente empleado para
medir la altura de la base de las nubes, pero que cuando no hay nubosidad permite calcular la altura
de mezclado [5] . Las siguientes figuras emplean dicha información, comparando las predicciones de
WRF con las observaciones realizadas en Santiago.

La Figura 3-17 muestra que las predicciones de WRF para la altura de mezclado al mediodía son
similares a las medidas en Santiago en los meses de Abril a Agosto, aunque en los meses de
primavera y verano las alturas de mezclado que predice WRF tienden a sobrestimar las mediciones
de Santiago. Esto se debe a que WRF tiene una tendencia a aumentar la temperatura superficial
más rápido que las observaciones (Figura 3-6), y este calentamiento de la columna de aire se refleja
en un crecimiento más rápido de la altura de mezclado en esas condiciones.

5 Fuente: Muñoz, R.C., Undurraga, A., 2010. Daytime mixed layer over the Santiago Basin: Description of two

years of observations with a lidar ceilometer. J. Appl. Meteorol. Climatol. 49, 1728-1741.
doi:10.1175/2010JAMC2347.1

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 38 de 147

Código V01: FI-A.03-DSA

**Figura 3-17. Comparación de alturas de mezclado medidas al mediodía en Santiago (panel superior, Muñoz y**

**Undurraga, 2010) y modeladas por WRF al mediodía en Teno (panel inferior).**

Por lo tanto, se puede concluir que, para las condiciones de los meses de Abril a Agosto, el modelo
de dispersión va a representar bien eventos horarios de altas concentraciones de contaminantes
que ocurran en horas de la noche o antes del mediodía, ya que las emisiones modeladas van a ser
restringidas verticalmente por las alturas de mezclado que predice WRF, las que están en
concordancia con las mediciones realizadas en Santiago.

Por otra parte, la Figura 3-18 muestra la evolución matinal de la altura de mezclado en meses fríos
y durante el resto del año, respectivamente. Se aprecia que el modelo WRF tiende a sobrestimar la
velocidad de crecimiento de la altura de mezclado en los meses cálidos, porque WRF sobrestima la
tasa de aumento de las temperaturas superficiales en la zona. En contraste, en los meses de mayo
a agosto el modelo representa mejor el aumento de la altura de mezclado desde la mañana hasta

la tarde.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 39 de 147

Código V01: FI-A.03-DSA

**Figura 3-18. Comparación del crecimiento de la altura de mezclado en meses fríos y cálidos. Panel superior:**
**estimaciones experimentales en Santiago (Muñoz y Undurraga, 2010); panel inferior: modelación de WRF para Teno.**

Luego, se puede concluir que en la zona de Teno el modelo WRF estima adecuadamente las alturas
de mezclado entre abril y agosto, pero tiende a sobrestimarlas el resto del año. Este efecto tiende a
subestimar las concentraciones modeladas. Este aspecto se va a detallar más en la sección 6 análisis
de incertidumbre de la modelación, donde se va a estimar un factor de corrección para el modelo
de dispersión.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 40 de 147

Código V01: FI-A.03-DSA

**4.** **DESCRIPCIÓN DE LAS EMISIONES CONSIDERADAS SEGÚN ESCENARIOS**

Se consideran los siguientes escenarios de emisiones, para el desarrollo de la respectiva modelación

de calidad del aire.

Emisiones actuales de la Planta Teno CBB. Se consideran 7 fuentes de emisión
**Escenario 1:**
según emisiones especificadas en Tabla 4-1 y

Tabla 4-3.

Emisiones de la Planta Teno CBB con la implementación del Proyecto
**Escenario 2:**
“APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB

PLANTA TENO”. En este caso, sólo se afecta la fuente 1, que corresponde al horno
clínker, para la cual se consideran las emisiones con proyecto indicadas en Tabla
4-1. Las demás fuentes de la planta Teno CBB mantienen invariables sus niveles
operacionales y emisiones con la implementación del proyecto, las que se indican

en

Tabla 4-3. Los escenarios 1 y 2 permiten estimar los efectos solamente atribuibles
a las emisiones de la planta Teno CBB en la implementación del Proyecto.

Emisiones actuales de la Planta Teno de CBB (Escenario 1, según emisiones
**Escenario 3:**
especificadas en Tabla 4-1 y
Tabla 4-3) más las emisiones de la central térmica Energía Latina (según RCA
N°43/2008, 36 turbinas de generación eléctrica), según su despacho eléctrico
2018 (informado por CDEC), las de la planta de paneles MDP de Arauco (Fuente:
Anexo de Informe de Modelación de Dispersión Atmosférica de Contaminantes
Planta de MDP Teno de Paneles Arauco, abril 2010 del proyecto “Planta de
Paneles MDP Teno”, aprobado mediante RCA N°191, del 01/Octubre/2010,
especificadas en Tabla 4-4 y las de la Planta de Elaboración de Alimento para
Mascotas de Nestlé Chile S.A. (etapa 1). Este escenario, permite contrastar los
resultados de la modelación con los niveles de calidad del aire medidos y así
realizar un análisis de sensibilidad del modelo de dispersión, reduciendo así la

incertidumbre en la modelación.

Emisiones de la Planta Teno de CBB con la implementación del Proyecto
**Escenario 4:**
“APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB

PLANTA TENO”, (Escenario 2) detalladas en Tabla 4-1 y
Tabla 4-3 más las emisiones de la central térmica Energía Latina y las de la planta
de paneles MDP de Arauco (mismas del escenario 3) y las de la planta de alimentos
de mascotas de Nestlé S.A. (etapa 2) indicadas en
Tabla 4-3. Además, se incluye la operación de 6 turbinas adicionales en la central
Teno de Energía Latina, según lo declarado en el Anexo F, Informe de Modelación
de Calidad del Aire presentado por Energía Latina S.A. en diciembre de 2016, como
parte de la Adenda al Proyecto “Central de Generación Eléctrica a Gas Teno”, el
cual fue aprobado según RCA N° 29 del 6 de abril de 2017, señaladas en

Tabla 4-3

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 41 de 147

Código V01: FI-A.03-DSA

La Tabla 4-1 presenta las emisiones en la condición de operación actual, y las emisiones con
proyecto, en el Horno de clinker, que corresponde a la chimenea N°1 de la planta Teno de CBB.

**Tabla 4-1. Emisiones de Fuente 1: Chimenea N° 1 Horno Clinker condición actual y la más desfavorable con proyecto**

|Parámetro|Condición de<br>operación<br>actual (1)|Condición de<br>mayor emisión<br>posible con<br>proyecto (2)|Consideraciones|
|---|---|---|---|
|Caudal Nm3/h|216.201|240.000|El caudal de valor actual se determina según medición de<br>gases del 09 de octubre 2013.<br>El caudal de valor con proyecto, considera un aumento del<br>11% por uso de CAS, lo que implica un consumo mayor por<br>menor PCI.|
|MP2,5<br>mg/Nm3|5,84|12,0|Se considera que el 40% de MP corresponde a la parte<br>filtrable del MP 2,5, y el 76% de MP corresponde a MP10, de<br>acuerdo a referencia Factores de emisión USEPA AP 42,<br>capítulo 11.6, tabla 11.6-6, distribución de tamaño de<br>partícula en horno de clinker de cemento portland.<br>Para el nivel de emisión actual de MP, se consideró medición<br>del 2 de marzo de 2017.<br>Para la emisión con proyecto, se consideró nivel de emisión<br>de MP de 30 mg/m3N, inferior a nivel norma de 50 mg/m3N,<br>considerando para los niveles de MP2,5 y MP10 los mismos<br>porcentajes ya indicados (40% para MP2,5 y 76% para MP10<br>respecto del MP).|
|MP2,5 g/s|0,35|0,80|0,80|
|MP2,5 t/año|11,1|25,2|25,2|
|MP10 mg/Nm3|11,1|22,8|22,8|
|MP10 g/s|0,67|1,52|1,52|
|MP10 t/año|21,0|47,9|47,9|
|SO2 mg/Nm3|232,5|225|La concentración del valor actual se determina según<br>medición de gases del 09 de octubre 2013.<br>Valor con proyecto de 15 g/s, se determina como condición<br>máxima de operación del Proyecto. Cabe señalar que este<br>valos es un 32% del valor máximo del SO2, de 48 g/s<br>establecido en la RCA 239/2002.|
|SO2 g/s|15,5|15,0|15,0|
|SO2 t/año|488,8|473,0|473,0|
|NOx mg/Nm3|1.320|1.250|La concentración del valor actual se determina según<br>medición de gases del 09 de octubre 2013.<br>Valor con proyecto considera mantener valor indicado en<br>RCA 239/2002, el cual es de 300 kg/h de NOx.|
|NOx g/s|79,3|83,3|83,3|
|NOx kg/h|285,4|300|300|
|NOx t/año|2500|2628|2628|
|CO mg/Nm3|231,61|231,61|La concentración del valor actual se determina según<br>medición de CO del 29 enero 2016.<br>Para valor con proyecto se asume la misma concentración.|
|CO g/s|13,9|15,4|15,4|
|CO t/año|438,7|486,9|486,9|
|Plomo<br>mg/Nm3|0,0115|0,1|Valor actual corresponde a medición más alta del 10 y 12 de<br>febrero 2016.<br>El valor con proyecto corresponde al 10% del nivel de la<br>norma, establecida en DS 29/2013 - norma de emisión para|
|Plomo g/s|0,001|0,007|0,007|
|Plomo t/año|0,022|0,21|0,21|

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 42 de 147

Código V01: FI-A.03-DSA

(1) Fuente: Elaboración propia, en base a mediciones oficiales en chimenea del Horno.
(2) De acuerdo a consideraciones indicadas en esta tabla.

La chimenea N°1 del horno Clinker es la única fuente emisora que cambia sus emisiones debido a la
implementación del Proyecto, dado que en esta fuente se modificará su actual matriz de

combustibles a utilizar.

La Tabla 4-2 presenta los otros parámetros necesarios para la modelación de las emisiones del horno
de clinker - chimenea N°1 de la planta Teno de CBB.

**Tabla 4-2. Parámetros de las emisiones de la chimenea N°1 del horno Clinker.**

|Parámetro|Unidad|Valor|
|---|---|---|
|Coordenadas chimenea WGS84 H19|m|E: 304323<br>N: 6139736|
|Altura chimenea|m|80|
|Diámetro chimenea|m|2,5|
|Velocidad salida de los gases|m/s|16|
|Temperatura aprox. de salida de los gases|°C|115|

A continuación, se presentan las emisiones de las demás fuentes oficiales de CBB, las cuales no
varían con el proyecto. Para efectos de la modelación, se consideran las mediciones entre 2016 y
2018, según se detalla en la Tabla 4-3

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 43 de 147

Código V01: FI-A.03-DSA

**Tabla 4-3. Características de las emisiones de las demás fuentes oficiales de Planta CBB que mantienen sus emisiones**

**en situación actual y con proyecto.**

|Parámetro / Unidad|Chimenea<br>N°2,<br>Enfriador<br>Clinker.|Chimenea<br>N°3, molino<br>cemento 1.|Chimenea<br>N°4,<br>enfriador de<br>molino<br>cemento 1.|Chimenea<br>N°5, molino<br>de cemento<br>2.|Chimenea<br>N°6,<br>Generador<br>N°1|Chimenea<br>N°7,<br>Generador<br>N°2|
|---|---|---|---|---|---|---|
|Altura chimenea (m)|52|28|37,7|35|18|18|
|Diámetro interno de<br>la chimenea (m)|2,6|2,0|1,6|2,0|2,0|2,0|
|Velocidad de salida<br>de gases(m/s)|12|12|17|7|7|7|
|Temperatura de<br>salida de gases(°K)|468,15|356,15|349,15|365,55|365,55|365,55|
|Temperatura<br>Ambiente<br>Promedio(°K)|298,15|298,15|298,15|298,15|298,15|298,15|
|Caudal Volumétrico<br>Real Gases Chimenea<br>(m3N/h)|78.840|100.255|59.633|79.372|41.797|43.841|
|Ubicación (UTM,<br>Datum WGS 84) m|304350 E<br>6139753 N|304427 E<br>6139668 N|304421 E<br>6139666 N|304388 E<br>6139554 N|304091 E<br>6139621 N|304110 E<br>6139627 N|
|Fecha medición<br>caudal y MP|4 sept 2018|17 mayo<br>2017|12 de sept<br>2018|18 abril<br>2017|21 dic 2016|26 abril<br>2016|
|MP10 (mg/m3N)|8,9|17,7|9,56|9,54|89,31|108,24|
|MP10 (g/s)|0,195|0,49|0,16|0,21|1,04|1,32|
|Fecha medición NOx<br>y SO2|14 sept<br>2016|13 sept<br>2016|-|1 julio 2016|28 feb<br>2018|28 abril<br>2016|
|NOx (mg/m3N)|0,95|8,25|-|2,53|1.228,4|1.238,3|
|NOx (g/s)|0,021|0,23|-|0,06|14,3|15,08|
|SOx (mg/m3N)|1,46|2,14|-|0,89|70,2|35,7|
|SOx (g/s)|0,032|0,06|-|0,02|0,82|0,43|

Fuente: Elaboración propia, en base a mediciones oficiales en chimenea Horno.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 44 de 147

Código V01: FI-A.03-DSA

La Tabla 4-4 presenta las emisiones de la Central Térmica ENLASA y de la planta de Paneles de MDP

Arauco.

**Tabla 4-4. Emisiones Base de la Central Térmica ENLASA y de Planta de Paneles MDP Arauco**

|Parámetro /<br>Unidad|ENLASA<br>(1)<br>Chimenea<br>s D-1 a D-<br>36|MDP (2)<br>Aspira-<br>ción<br>Viruta<br>C900|MDP (2)<br>Aspira-<br>ción<br>Lamina<br>do|MDP (2)<br>Aspira-<br>ción<br>impreg-<br>nación|MDP (2)<br>Transp.<br>N. Q600|MDP (2)<br>Transp.<br>N. Q500|MDP (2)<br>WESP<br>E300|MDP (2)<br>Batería<br>Filtros|MDP (2)<br>Transp.<br>N. F900|MDP (2)<br>Transp.<br>N. J800|
|---|---|---|---|---|---|---|---|---|---|---|
|Altura de<br>chimenea (m)|6,9|8|8|8|8|8|25|10|8|8|
|Diámetro<br>interno de la<br>chimenea (m)|2,0|0,75|0,9|0,7|0,35|0,65|2,5|1,8|0,7|0,7|
|Velocidad de<br>salida de<br>gases(m/s)|13,2|20,82|23,41|20,0|15,59|18,68|13,81|24,24|20,0|20,0|
|Temperatura<br>de salida de<br>gases(°K)|358|293|293|303|303|303|333|303|303|303|
|Ubicación<br>(UTM, Datum<br>WGS 84, Huso<br>19)|315962 E<br>6139787<br>N|309242<br>E <br>614059<br>N|309175<br>E <br>614068<br>N|309160<br>E <br>614076<br>N|309254<br>E <br>614065<br>N|309254<br>E <br>614066<br>N|309254<br>E <br>614065<br>N|309164<br>E <br>614065<br>N|309210<br>E <br>614060<br>N|309190<br>E <br>614061<br>N|
|MP10 (g/s)|0,28|0,86|0,28|0,03|0,03|0,11|2,78|1,11|0,14|0,14|
|MP2,5 (g/s)|0,28|0,86|0,28|0,03|0,03|0,11|2,78|1,11|0,14|0,14|
|NOx (g/s)|1,33|-|-|-|-|-|13,89|-|-|-|
|SOx (g/s)|1,22|-|-|-|-|-|0,56|-|-|-|
|CO (g/s)|2,33|-|-|-|-|-|-|-|-|-|

(1) Fuente: Anexo F Informe de modelación Central de Generación Eléctrica a gas Teno, Energía Latina, diciembre

2016, tabla 4-1 Proyecto con Central a Gas Teno Utilizando GLP. Adenda al proyecto “Central de Generación

Eléctrica a Gas Teno”. Cada chimenea tiene las mismas emisiones, así la emisión total de cada contaminante es
36 veces el valor indicado en la tabla. Ejemplo MP10 es 0,28 x 36 = 10,08 g/s.
(2) Fuente: Anexo H Informe de Modelación de Dispersión Atmosférica DIA Planta de Paneles MDP Teno, abril de

2010.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 45 de 147

Código V01: FI-A.03-DSA

La Tabla 4-5 presenta la operación de 6 turbinas adicionales en la central Teno de Energía Latina,
según lo declarado en el Anexo F, Informe de Modelación de Calidad del Aire presentado por Energía
Latina S.A. con fecha 5 de diciembre de 2016, como parte del Adenda al proyecto ‘Central de

Generación Eléctrica a Gas Teno.

**Tabla 4-5. Emisiones del proyecto Central Térmica ENLASA, 6 turbinas adicionales.**

|Parámetro / Unidad|ENLASA<br>Turbina<br>GNL-1|ENLASA<br>Turbina<br>GNL-2|ENLASA<br>Turbina<br>GNL-3|ENLASA<br>Turbina<br>GNL-4|ENLASA<br>Turbina<br>GNL-5|ENLASA<br>Turbina<br>GNL-6|
|---|---|---|---|---|---|---|
|Altura de chimenea<br>(m)|27,5|27,5|27,5|27,5|27,5|27,5|
|Diámetro interno de<br>la chimenea (m)|1,2|1,2|1,2|1,2|1,2|1,2|
|Velocidad de salida<br>de gases(m/s)|28,12|28,12|28,12|28,12|28,12|28,12|
|Temperatura de<br>salida de gases(°K)|673|673|673|673|673|673|
|Ubicación (UTM,<br>Datum WGS 84,<br>Huso 19)|304027 E<br>6139549 N|304025 E<br>6139547 N|304023 E<br>6139545 N|304029 E<br>6139547 N|304027 E<br>6139545 N|304026 E<br>6139543 N|
|MP10 (g/s)|0,18|0,18|0,18|0,18|0,18|0,18|
|MP2,5 (g/s)|0,18|0,18|0,18|0,18|0,18|0,18|
|NOx (g/s)|3,4|3,4|3,4|3,4|3,4|3,4|
|CO (g/s)|5,75|5,75|5,75|5,75|5,75|5,75|

(1) Fuente: Anexo F Informe de modelación Central de Generación Eléctrica a gas Teno, Energía Latina, diciembre

2016, tabla 4-1 Proyecto con Central a Gas Teno Utilizando GLP. Adenda al proyecto “Central de Generación

Eléctrica a Gas Teno”.

La Tabla 4-6 [6] presenta las emisiones de la Planta de Alimentos de Mascotas de Nestlé S.A., localizada
al norte de la Ruta J-310 y al oriente de la línea férrea, sector Aurora, Comuna de Teno,
aproximadamente a la altura del kilómetro 166 ruta 5 sur.

Se presentan las emisiones asociadas a las dos etapas de operación de la planta. La etapa 1
(actualmente en operación para el año base 2018) consiste en una línea de producción, con una
capacidad máxima de 77.000 ton/año de producto terminado; la etapa 2 contempla la
instalación de una segunda línea de producción, de las mismas características de la primera,
aumentando la capacidad de producción a 154.000 ton/año (esta etapa todavía no se
materializa). La producción será destinada a consumo en el país y exportaciones.

Por lo tanto, las emisiones de la etapa 1 están incluidas en la línea base de emisiones
atmosféricas correspondientes al año 2018 (escenario 3 de emisiones). Las emisiones de la
etapa 2 (por construirse) se van a considerar en el citado escenario 4 de emisiones.

6 Fuente: Ambiosis S.A. INFORME DE ESTIMACIONES DE EMISIONES ATMOSFERICAS. Evaluación de impacto
en la calidad del aire del proyecto “Elaboración de Alimento para Mascotas de Nestlé Chile S.A.” Octubre 2014.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 46 de 147

Código V01: FI-A.03-DSA

**Tabla 4-6** **.** **Emisiones del proyecto planta de alimentos de mascotas de Nestlé S.A.**

**a) Etapa 1 de operación**

**b) Etapa 2 de operación**

Con respecto a las emisiones de la planta termoeléctrica Teno de Energía Latina S.A., el año 2018
esas central entró en operación solamente una fracción del año (229 horas o 2,6 % del tiempo),
como se indica en la siguiente Figura.

**Figura 4-1 Generación horaria central Teno, año 2018 (MW). Fuente:**
**[https://www.coordinador.cl/operacion/graficos/operacion-real/generacion-real-del-sistema/](https://www.coordinador.cl/operacion/graficos/operacion-real/generacion-real-del-sistema/)**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 47 de 147

Código V01: FI-A.03-DSA

Usando la información horaria de generación eléctrica, es posible estimar las emisiones horarias de
la central diésel Teno, combinando las emisiones de la Tabla 4-4 con la generación horaria entregada
por la autoridad de coordinación del sistema eléctrico chileno. Con esta información se construye el

escenario 3 de emisiones.

Para construir el escenario 4 de emisiones, se asume que la central diésel va a despachar energía en
las mismas condiciones que el año 2018, y que además las seis turbinas GLP (Tabla 4-5) van a estar
en operación de despacho de energía. Es decir, el escenario 4 incluye las emisiones base de la central
Teno y considera esas seis turbinas con emisiones adicionales.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 48 de 147

Código V01: FI-A.03-DSA

**5.** **DETERMINACIÓN DE LOS NIVELES DE CALIDAD DEL AIRE SEGÚN ESCENARIOS Y**

**APLICACIÓN DEL MODELO DE DISPERSIÓN CALPUFF**

**5.1 METODOLOGÍA DE ANÁLISIS**

La metodología considerada para la determinación de los niveles de calidad del aire, para la
condición con Proyecto, se desarrolla mediante la modelación de las emisiones atmosféricas, de
acuerdo con la Guía de Uso de Modelos de Calidad del Aire en el SEIA, publicada por el SEA. Esta
metodología considera las siguientes actividades:

a. Obtención de datos meteorológicos para CALPUFF a partir de la modelación meteorológica

en altura en la zona del proyecto para el año 2018 completo, usando el modelo de

pronóstico numérico del tiempo WRF.

b. Configuración de la modelación de CALPUFF para las emisiones de MP 10, MP 2.5, SO 2, NO x, CO

y Plomo, estimadas por el Consultor en base a la información proporcionada por el

Mandante, las que se detallan en la sección 4 de este Informe.

c. Definición de una grilla de 63 x 63 km de superficie, la que cubre la zona modelada de las

emisiones de la planta Teno de CBB, como se puede apreciar en la siguiente figura 5-1; en

la Tabla 5-1 se especifica la ubicación geográfica de los receptores discretos. Las
coordenadas de la figura corresponden a coordenadas LCC [7] (que provienen de la simulación

numérica con WRF), las que tienen como origen suroeste el punto de coordenadas UTM:

271.560 m E y 6.105.055 m N (datum: WGS 84 19-H).

d. Uso de un factor de corrección para corregir las concentraciones modeladas, considerando

la evaluación del desempeño del modelo del tiempo WRF y la situación de la línea base 2018

de calidad del aire. La derivación de este factor se presenta en la sección 6 de este Informe

(Análisis de sensibilidad de la modelación de calidad del aire).

**5.2.1 Determinación de los puntos de interés.**

El primer punto de interés corresponde al punto de máximo impacto asociado a la Planta CBB Teno,
puesto que en este punto los efectos del proyecto en la calidad del aire serán los más altos.

El segundo punto de interés corresponde a la ubicación de la Estación de monitoreo de calidad del
aire Teno ENLASA, ya que en este lugar se conocen los respectivos niveles de calidad del aire.

Finalmente, siendo la localidad de Teno la más cercana al proyecto, se analizan 5 receptores
discretos, que cuben todo el contorno de esta localidad.

El punto de máximo impacto se detalla en el siguiente sub capítulo. Las coordenadas de los seis
receptores discretos, se identifican en coordenadas UTM en la Tabla 5-1.

7 LCC es una abreviatura para Lambert-Conformal Coordinates, coordenadas geográficas usadas por WRF para

zonas en latitudes medias.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 49 de 147

Código V01: FI-A.03-DSA

**Figura 5-1. Dominio de modelación de calidad del aire, en coordenadas LCC (km).**

**Tabla 5-1. Ubicación receptores discretos (UTM, Huso 19 H, WGS84)**

|Código|Receptor|UTM E [m]|UTM N [m]|
|---|---|---|---|
|R_1|Estación ENLASA(1)|305.205|6.140.221|
|R_2|Teno Norte|302.574|6.139.767|
|R_3|Estación FFCC Teno|302.668|6.139.114|
|R_4|Teno SE|302.714|6.138.326|
|R_5|Teno Sur|302.094|6.138.431|
|R_6|Teno Oeste|301.377|6.139.114|

(1) Corresponde a la estación de monitoreo de calidad del aire.

Cada uno de los receptores R_1 a R_6 se pueden apreciar en la Figura 5-2.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 50 de 147

Código V01: FI-A.03-DSA

**Figura 5-2. Ubicación de los Receptores R_1 a R_6 considerados en el análisis**

Además de los seis receptores ya descritos, se definió una grilla Cartesiana de receptores,
espaciados cada 1000 m, con el fin de poder representar adecuadamente la distribución espacial de
los potenciales impactos en calidad del aire atribuibles a la operación del Proyecto.

A continuación, se muestran resultados de las simulaciones generadas para los cuatro escenarios [8] .
En primer lugar, se determina el punto de máximo impacto asociado exclusivamente a las fuentes
de Planta Teno de CBB, considerando que en ese punto se tendrían las mayores variaciones en
términos de calidad del aire asociadas con la implementación del proyecto. Además, es un punto
necesario de analizar en cuanto a cumplimiento de normas secundarias, ya que en ese punto no hay
población. En segundo lugar, para cada contaminante, se presentan las concentraciones
ambientales en el punto de máximo impacto de la Planta CBB y en los seis receptores discretos
considerados (incluyendo la estación ENLASA donde está disponible la línea base de calidad del aire),
presentando la información en forma de tablas, para cada uno de los cuatro escenarios de análisis.
Paralelamente, se presentan la distribución espacial de las concentraciones en forma de gráficos
con curvas de contorno; para cada contaminante, los niveles de las curvas son los mismos en los
cuatro escenarios modelados, para facilitar una comparación visual.

8 En todos los escenarios se consideran los mismos factores de corrección para las concentraciones modeladas
(ver Sección 6).

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 51 de 147

Código V01: FI-A.03-DSA

**1.3** **ANÁLISIS EN PUNTOS DE MÁXIMO IMPACTO (PMI)**

La Tabla 5-2 muestra la ubicación de los puntos de máximos impactos (PMI) para MP 10, MP 2.5, NO 2,
SO 2, CO y Pb, obtenidos a partir de los escenarios 1 y 2, que reflejan solamente el impacto de la
Planta Teno de CBB. En estos puntos, se obtienen los máximos valores considerando la operación
actual y con proyecto. Dado que solo cambian las emisiones y no la cantidad ni las dimensiones de
las chimeneas, los PMI de ambos escenarios son coincidentes.

Para estos mismos puntos, se considera también los resultados con otros proyectos, los cuales
representan los escenarios 3 (proyectos actuales) y escenario 4 (proyecto en evaluación más
proyectos no materializados).

**Tabla 5-2 Localización del PMI (UTM, WGS 84)** **y sus aportes en escenarios 1 a 4 para cada contaminante en análisis.**

|Parámetr<br>o|E [m]|N [m]|Escenario 1<br>g/m3N|Escenario 2<br>g/m3N|Escenario 3<br>g/m3N|Escenario 4<br>g/m3N|
|---|---|---|---|---|---|---|
|MP10 <br>Anual|304.470|6.140.362|10,9|11,3|11,5|12,25|
|MP10 P98<br>Diario|304.470|6.140.362|24,7|25,1|26,8|29,7|
|MP2.5 <br>Anual|304.470|6.140.362|9,79|10,0|10,35|10,9|
|MP2.5 P98<br>Diario|304.470|6.140.362|22,2|22,4|25,1|27,1|
|NO2 Anual|304.470|6.140.362|10,1|9,91|11,87|11,67|
|NO2 P.99<br>1h|304.470|6.140.362|28,8|28,0|58,0|58|
|SO2 Anual|304.470|6.140.362|56,6|54,8|74,6|73,1|
|SO2 P99<br>Diario|304.470|6.140.362|78,1|75,7|140,9|140,3|
|SO2 P99<br>1h|304.470|6.140.362|44,7|45,2|45,3|48,5|
|SO2 <br>P99,73 1h<br>(1)|304.470|6.140.362|121|124|132|139|
|CO P99 1h|304.470|6.140.362|50|56|195|195|
|CO P99 8h|304.470|6.140.362|22|25|95|96|
|Pb Anual|305.431|6.142.387|0,00045|0,00313|0,00045|0,00313|

_(1)_ _La norma secundaria diaria corresponde a 260 ug/m3N, el cual no se evalúa ya que es menos estricto_

_que el nivel diaria de la norma primaria._
_(2)_ _Corresponde a norma secundaria_

Todos los PMI para MP y gases coinciden en el punto de coordenadas UTM 304.470 m E y 6.140.362
m N (a 1,62 km al NE de Teno). La excepción es el PMI del Pb anual (solamente emitido por la
Chimenea 1 de CBB), el que se encuentra en el punto de coordenadas 305.431 m E y 6.141.387 m N

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 52 de 147

Código V01: FI-A.03-DSA

(a 3,7 km al NE de Teno). Esto se debe a que la meteorología y la geometría de las fuentes es la
misma, solo cambia la magnitud de las emisiones de cada contaminante en una de las fuentes
asociadas al desarrollo del proyecto, que es la chimenea del horno. La ubicación de los PMI se
muestra en la siguiente Figura. Ambos están ubicados en zonas rurales.

**Figura 5-3. Puntos de máximo impacto asociados a la Planta Teno. El polígono azul es el borde de la planta Teno CBB,**

**y el polígono negro es el borde urbano de Teno.**

La siguiente tabla muestra los efectos en la calidad del aire debido a la implementación del proyecto
más los otros no materializados, en el PMI. De este modo, se presenta, por una parte, los efectos
atribuibles exclusivamente al proyecto, el cual se determina como la diferencia entre el Escenario 2
y el Escenario 1, y se denomina “Aumento por Proyecto CBB”.

Además, se determina el efecto del aumento en la calidad del aire al considerar adicionalmente los
proyectos aún no implementados completamente, lo cual se determina mediante la diferencia entre
el Escenario 4 y el Escenario 3; y se denomina “Aumento por todos los Proyectos”.

Conocido el nivel de calidad del aire actual (se asume el mismo nivel medido en la estación ENLASA),
se determina el nuevo nivel de calidad del aire bajo la condición más desfavorable, teniendo en
consideración el aumento asociado a la materialización de todos los proyectos, y finalmente se
determina el porcentaje de aumento respecto a la norma.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 53 de 147

Código V01: FI-A.03-DSA

**Tabla 5-3 Concentraciones ambientales de MP** **10** **, MP** **2.5** **, NO** **2** **, SO** **2** **, CO y Pb en PMI y porcentajes según niveles de**

**calidad del aire normados**

|Parámetro|Norma de<br>calidad del<br>aire<br>g/m3N (1)|Nivel<br>actual<br>Calidad del<br>aire<br>g/m3N (2)|Porcentaje<br>c. aire<br>actual<br>c/r a<br>norma de<br>calidad|Aporte por<br>proyecto<br>CBB<br>g/m3N<br>(3)|Aporte por<br>todos los<br>proyectos<br>g/m3N<br>(4)|Nivel c.<br>aire con<br>proyectos<br>g/m3N<br>(5)|Porcentaje<br>calidad<br>aire por<br>proyecto<br>CBB c/r a<br>norma<br>calidad<br>aire|Porcentaje<br>c. aire con<br>proyectos<br>c/r a<br>norma de<br>calidad|
|---|---|---|---|---|---|---|---|---|
|MP10 Anual|50|33,8|68%|0,4|0,7|34,5|68%|69%|
|MP10 P98 Diario|150|69,7|46%|0,5|3,0|72,7|47%|48%|
|MP2.5 Anual|20|7,5|38%|0,2|0,5|8,0|39%|40%|
|MP2.5 P98 Diario|50|24|48%|0,3|2,0|26,0|49%|52%|
|SO2 Anual|60|6,3|11%|-0,2|-0,2|6,1|10%|10%|
|SO2 P99 Diario (6)|150|38,3|26%|-0,8|-0,3|38,0|25%|25%|
|SO2 P99 Horario|350|64,1|18%|-1,8|-1,5|62,6|18%|18%|
|SO2 P99,73<br>Horario (7)|700|105,1|15%|-2,4|-0,7|104,5|15%|15%|
|NO2 Anual|100|18,7|19%|0,5|3,1|21,8|19%|22%|
|NO2 P.99 Horario|400|67|17%|3,2|7,1|74,1|18%|19%|
|CO P99 Horario|30,000|1000|3%|5,4|0,2|1000,2|3%|3%|
|CO P99 8 horas|10,000|700|7%|2,4|1,0|701,0|7%|7%|
|Pb Anual|0,5|S/i||0,003|0,003|||S/i|

_(1)_ _Las normativas primarias de calidad del aire utilizadas son D.S N°12/2010 para MP2,5, D.S N°59/1998 para_

_MP10, D.S N°104/2018 para SO_ _2_ _, D.S N°114/2002 para NO_ _2_ _, D.S N°115/2002 para CO_ _,_ _D.S N°136/2000 para_
_Pb y D.S N°22/2009 para norma secundaria horario de SO_ _2_ _._
_(2)_ _Valor medido en estación ENLASA_
_(3)_ _Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual: Escenario 2 -_

_Escenario 1._

_(4)_ _Corresponde a la resta de Escenario 4 - Escenario 3. En este caso, se consideran los efectos del proyecto más_

_los otros proyectos no materializados._
_(5)_ _Al nivel actual se suma el aporte de todos los proyectos, que es el máximo entre (3) y (4)._
_(6)_ _No se evalúa norma secundaria SO_ _2_ _P99,7 Diario de 260 ug/m3N, ya que es menos estricta que la norma_

_primaria._
_(7)_ _SO_ _2_ _P99,73 Horario, corresponde a la norma secundaria._

Cabe hacer notar que las estimaciones de niveles de concentraciones con proyectos son
conservadoras en el caso de las normas que consideran percentiles, puesto que en general, los
percentiles no son aditivos.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 54 de 147

Código V01: FI-A.03-DSA

Se aprecia en la Tabla anterior que en todos los casos se cumple ampliamente con la respectiva
norma de calidad del aire primaria (o secundaria en el caso del SO 2 horario), ya que todos los
contaminantes están bajo la condición de latencia en la situación con Proyecto CBB y también en
caso que otros proyectos se implementen en la zona. En el caso del material particulado fino MP 2,5,
los niveles proyectados alcanzan al 40% y 52% de las normas primarias anual y diaria,
respectivamente. Para el MP10, los niveles proyectados llegan al 69% y 48% de las normas primarias
anual y diaria, respectivamente. Para los demás contaminantes, las concentraciones proyectadas
están por debajo del 50% de la respectiva norma de calidad del aire.

**1.4** **ANÁLISIS EN ESTACIÓN ENLASA**

La Tabla 5-4 muestra para MP 10, MP 2.5, NO 2, SO 2, CO y Pb, los resultados obtenidos a partir de los
escenarios 1 y 2, siendo estos puntos donde se obtienen los máximos valores considerando la
operación actual y con proyecto solamente de la planta Teno. Los escenarios 1 y 2 reflejan
solamente el impacto de la Planta Teno de CBB. Se presenta también los resultados con otros
proyectos vigentes y proyectados, los cuales representan los escenarios 3 y 4, respectivamente.

**Tabla 5-4 Aportes en estación ENLASA para escenarios 1 a 4 para cada contaminante en análisis.**

|Parámetro|Escenario 1<br>g/m3N|Escenario 2<br>g/m3N|Escenario 3<br>g/m3N|Escenario 4<br>g/m3N|
|---|---|---|---|---|
|MP10 Anual|1,9|2,1|2,1|2,48|
|MP10 P98 Diario|6,7|7,4|7,5|8,7|
|MP2.5 Anual|1,6|1,8|1,9|2,1|
|MP2.5 P98 Diario|5,9|6,2|6,5|7,4|
|NO2 Anual|4,0|3,9|4,2|4,1|
|NO2 P.99 Horario|19,4|18,9|19,9|19,3|
|SO2 Anual|35,2|34,1|35,7|34,7|
|SO2 P99 Diario|43,7|42,4|50,8|49,1|
|SO2 P99 Horario (1)|9,0|9,2|9,1|9,9|
|SO2 P99,73 Horario (2)|81,7|84,5|81,7|87,3|
|CO P99 horario|39,4|43,7|46,7|83,0|
|CO P99 8 horas|15,8|17,5|18,5|44,3|
|Pb anual|0,0002|0,0016|0,0002|0,0016|

(1) Valos horario norma primaria de SO 2, percentil 99.
(2) Valor horario para la norma secundaria de SO 2 .

La Tabla 5-5 muestra los efectos en la calidad del aire debido a la implementación del proyecto más
los otros no materializados, en PMI. De este modo, se presenta, por una parte, los efectos atribuibles
exclusivamente al proyecto, el cual se determina como la diferencia entre el Escenario 2 y el

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 55 de 147

Código V01: FI-A.03-DSA

Escenario 1, y se denomina “Aumento por Proyecto CBB”. Además, se determina el efecto del
aumento en la calidad del aire al considerar adicionalmente los proyectos no materializados, lo cual
se determina mediante la diferencia entre el Escenario 4 y el Escenario 3; y se denomina “Aumento
por todos los Proyectos”.

Se aprecia en la Tabla que se cumplen ampliamente todas las normas de calidad del aire en la
estación de monitoreo ENLASA, ya que todos ellos están claramente bajo el respectivo nivel de

latencia de la norma.

**Tabla 5-5 Concentraciones ambientales de MP** **10** **, MP** **2.5** **, NO** **2** **, SO** **2** **, CO y Pb en Estación ENLASA**

|Parámetro|Norma de<br>calidad del<br>aire<br>g/m3N|Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1)|Aporte por<br>Proyecto<br>CBB<br>g/m3N<br>(2)|Aporte por<br>todos los<br>Proyectos<br>g/m3N<br>(3)|Nivel<br>actual más<br>Proyectos<br>g/m3N<br>(4)|Porcentaje<br>actual<br>respecto a<br>norma de<br>calidad|Porcentaje<br>con<br>Proyectos<br>respecto a<br>norma de<br>calidad|
|---|---|---|---|---|---|---|---|
|MP10 Anual|50|33,8|0,2|0,3|34,1|68%|68%|
|MP10 P98 Diario|150|69,7|0,7|1,2|70,9|46%|47%|
|MP2.5 Anual|20|7,5|0,1|0,2|7,7|38%|39%|
|MP2.5 P98 Diario|50|24|0,3|0,9|24,9|48%|50%|
|SO2 anual|60|6,3|-0,1|-0,1|6,2|11%|10%|
|SO2 P99 Diario|150|38,3|-0,6|-0,6|37,7|26%|25%|
|SO2 P99 Horario (5)|350|64,1|-1,1|-1,1|63,0|18%|18%|
|SO2 P99,73 Horario (6)|700|105,1|-1,3|-1,6|103,5|15%|15%|
|NO2 anual|100|18,7|0,3|0,8|19,5|19%|19%|
|NO2 P.99 Horario|400|67|2,9|5,5|72,5|17%|18%|
|CO P99 horario|30.000|1000|4,3|36,3|1036,3|3%|3%|
|CO P99 8 horas|10.000|700|1,7|25,8|725,8|7%|7%|
|Pb anual|0,5|S/i|0,0014|0,0014||||

(1) Valor medido en estación ENLASA
(2) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual.
(3) Corresponde a la resta de Escenario 4 - Escenario 3. En este caso, se consideran los otros proyectos

no materializados.

(4) Al nivel actual se suma el aporte de todos los proyectos.
(5) Valor horario norma primaria de SO 2, percentil 99.
(6) Valor horario para la norma secundaria de SO 2, percentil 99,73

A continuación se presenta el mismo análisis hecho para el PMI, pero para los receptores discretos
en Teno, para cada contaminante por separado.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 56 de 147

Código V01: FI-A.03-DSA

**1.5** **MP** **10**

La Tabla 5-6 presenta para MP 10 anual, los aportes a la calidad del aire para los cuatro escenarios
considerados en los 6 receptores sensibles modelados.

**Tabla 5-6 Resultados MP** **10** **Anual en PMI y los seis receptores de interés**

|Receptor|MP Anual<br>10<br>Escenario 1<br>g/m3N|MP Anual<br>10<br>Escenario 2<br>g/m3N|MP Anual<br>10<br>Escenario 3<br>g/m3N|MP Anual<br>10<br>Escenario 4<br>g/m3N|
|---|---|---|---|---|
|PMI Teno CBB|10,93|11,31|11,51|12,25|
|R-1 Estación Teno ENLASA|1,89|2,09|2,15|2,48|
|R-2 Teno Norte|0,21|0,23|0,31|0,34|
|R-3 Estación FFCC Teno|0,26|0,28|0,35|0,38|
|R-4 Teno SE|0,32|0,33|0,40|0,43|
|R-5 Teno Sur|0,22|0,23|0,30|0,32|
|R-6 Teno Oeste|0,16|0,16|0,21|0,23|

En la Tabla 5-7 se aprecia que los niveles del MP 10 anual se mantienen en todos los casos por debajo

del 70% de la norma.

**Tabla 5-7 Resultados Niveles de calidad del aire de MP** **10** **Anual en PMI y los seis receptores de interés**

|Receptor|Norma de<br>calidad<br>del aire<br>g/m3N|Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1)|Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2)|Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3)|Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4)|Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma|Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad|
|---|---|---|---|---|---|---|---|
|PMI Teno CBB|50|33,8|0,38|0,75|34,55|68%|69%|
|R-1 Estación<br>Teno ENLASA|50|33,8|0,20|0,33|34,13|68%|68%|
|R-2 Teno Norte|50|33,8|0,01|0,03|33,83|68%|68%|
|R-3 Estación<br>FFCC Teno|50|33,8|0,01|0,03|33,83|68%|68%|
|R-4 Teno SE|50|33,8|0,02|0,03|33,83|68%|68%|
|R-5 Teno Sur|50|33,8|0,01|0,02|33,82|68%|68%|
|R-6 Teno Oeste|50|33,8|0,01|0,02|33,82|68%|68%|

(1) Valor medido en estación ENLASA
(2) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual.
(3) Corresponde a la resta de Escenario 4 - Escenario 3. En este caso se consideran los otros proyectos no

materializados.

(4) Al nivel actual se suma el aporte de todos los proyectos.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 57 de 147

Código V01: FI-A.03-DSA

En las figuras 5-4 a 5-7 se muestra las curvas de niveles de concentraciones promedio anual de MP 10,

para los escenarios 1 a 4, respectivamente. Se puede apreciar en ellas, que los aportes de planta

Teno de CBB a las concentraciones de MP 10 promedio anual disminuyen fuertemente con la

distancia a la Planta Teno (escenarios 1 y 2). En la ciudad de Teno los aportes son menores a 1 g/m [3]

para todos los escenarios, tal como ya se ha presentado en la Tabla anterior, en particular los valores

presentados en los receptores R-2 a R-6.

Al considerarse todos los proyectos en la zona (vigentes y por concretarse), aparecen otras zonas

con aportes relevantes a las concentraciones ambientales, pero que corresponden a los otros

proyectos considerados en los escenarios 3 y 4. No se modifica la condición de que todos los aportes

modelados en la ciudad de Teno son menores a 1 g/m [3], lo que se explica porque el viento

predominante en la zona es S y SSW así que las fuentes modeladas están viento abajo de Teno la

mayor parte del tiempo.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 58 de 147

Código V01: FI-A.03-DSA

**Figura 5-4 Mapa de concentraciones del MP** **10** **anual (**  **g/m** **[3]** **) para el escenario 1. La ciudad de Teno está delimitada por el polígono negro.**

**El perímetro del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 59 de 147

Código V01: FI-A.03-DSA

**Figura 5-5 Mapa de concentraciones del MP** **10** **anual (**  **g/m** **[3]** **) para el escenario 2. La ciudad de Teno está delimitada por el polígono negro.**

**El perímetro del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 60 de 147

Código V01: FI-A.03-DSA

**Figura 5-6 Mapa de concentraciones del MP** **10** **anual (**  **g/m** **[3]** **) para el escenario 3. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 61 de 147

Código V01: FI-A.03-DSA

**Figura 5-7 Mapa de concentraciones del MP** **10** **anual (**  **g/m** **[3]** **) para el escenario 4. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 62 de 147

Código V01: FI-A.03-DSA

En la Tabla 5-8 se presenta para MP 10 diario Percentil 98, los aportes a la calidad del aire para los
cuatro escenarios considerados en los 6 receptores sensibles modelados.

**Tabla 5-8 Resultados MP** **10** **Percentil 98 diario en los seis receptores discretos y** **punto de máximo impacto**

|Receptor|P. 98 MP<br>10<br>Diario<br>Escenario 1<br>g/m3N|P. 98 MP<br>10<br>Diario<br>Escenario 2<br>g/m3N|P. 98 MP<br>10<br>Diario<br>Escenario 3<br>g/m3N|P. 98 MP<br>10<br>Diario<br>Escenario 4<br>g/m3N|
|---|---|---|---|---|
|PMI Teno CBB|24,7|25,1|26,8|29,7|
|R-1 Estación Teno ENLASA|6,7|7,4|7,5|8,7|
|R-2 Teno Norte|1,9|1,9|2,7|2,8|
|R-3 Estación FFCC Teno|2,6|2,7|3,0|3,1|
|R-4 Teno SE|2,7|2,7|3,2|3,3|
|R-5 Teno Sur|2,3|2,3|2,7|2,9|
|R-6 Teno Oeste|1,3|1,4|1,7|1,8|

La Tabla 5-9 muestra los efectos en la calidad del aire debido a la implementación del proyecto más
los otros no materializados. En todos los casos las concentraciones proyectadas se mantienen por
debajo del 50% de la norma diaria.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 63 de 147

Código V01: FI-A.03-DSA

**Tabla 5-9. Resultados Niveles de calidad del aire de MP** **10** **Diario en PMI y en los seis receptores de interés**

|Receptor|Norma de<br>calidad<br>del aire<br>g/m3N|Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1)|Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2)|Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3)|Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4)|Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma|Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad|
|---|---|---|---|---|---|---|---|
|PMI Teno CBB|150|69,7|0,5|3,0|72,7|46%|48%|
|R-1 Estación<br>Teno ENLASA|150|69,7|0,7|1,2|70,9|46%|47%|
|R-2 Teno Norte|150|69,7|0,0|0,1|69,8|46%|47%|
|R-3 Estación<br>FFCC Teno|150|69,7|0,1|0,1|69,8|46%|47%|
|R-4 Teno SE|150|69,7|0,0|0,1|69,8|46%|47%|
|R-5 Teno Sur|150|69,7|0,1|0,1|69,8|46%|47%|
|R-6 Teno Oeste|150|69,7|0,1|0,1|69,8|46%|47%|

(1) Valor medido en estación ENLASA
(2) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual.
(3) orresponde a la resta de Escenario 4 - Escenario 3. En este caso se consideran los otros proyectos

no materializados.

(4) Al nivel actual se suma el aporte de todos los proyectos.

En las figuras 5-8 a 5-11 se presentan las curvas de niveles de los percentiles 98 de las

concentraciones promedio diario de MP 10, para los escenarios 1 a 4, respectivamente. Nuevamente

se puede apreciar en la figura que los aportes de planta Teno de CBB a los precentiles 98 de las

concentraciones diarias de MP 10 disminuyen fuertemente con la distancia a la Planta Teno

(escenarios 1 y 2). Al considerarse los demás proyectos vigentes en la zona, aparecen otras zonas

con aportes relevantes, los que corresponden a otros proyectos en la zona. En todos los casos los

aportes en la ciudad de Teno se mantienen por debajo de 4 g/m [3] .

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 64 de 147

Código V01: FI-A.03-DSA

**Figura 5-8 Mapa del percentil 98 de las concentraciones diarias de MP** **10** **(**  **g/m** **[3]** **) para el escenario 1. La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 65 de 147

Código V01: FI-A.03-DSA

**Figura 5-9 Mapa del percentil 98 de las concentraciones diarias de MP** **10** **(**  **g/m** **[3]** **) para el escenario 2. La ciudad de Teno está delimitada por el polígono negro. El perímetro del**

**proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 66 de 147

Código V01: FI-A.03-DSA

**Figura 5-10 Mapa del percentil 98 de las concentraciones diarias de MP** **10** **(**  **g/m** **[3]** **) para el escenario 3. La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 67 de 147

Código V01: FI-A.03-DSA

**Figura 5-11 Mapa del percentil 98 de las concentraciones diarias de MP** **10** **(**  **g/m** **[3]** **) para el escenario 4. La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 68 de 147

Código V01: FI-A.03-DSA

**1.6** **MP** **2.5**

En la Tabla 5-10 se presenta para MP 2,5 anual, los aportes a la calidad del aire para los cuatro
escenarios considerados en los 6 receptores sensibles modelados.

**Tabla 5-10 MP** **2.5** **Anual en PMI y los seis receptores de interés**

|Receptor|MP Anual<br>2,5<br>Escenario 1<br>g/m3N|MP Anual<br>2,5<br>Escenario 2<br>g/m3N|MP Anual<br>2,5<br>Escenario 3<br>g/m3N|MP Anual<br>2,5<br>Escenario 4<br>g/m3N|
|---|---|---|---|---|
|PMI Teno CBB|9,8|10,0|10,4|10,9|
|R-1 Estación Teno ENLASA|1,6|1,8|1,9|2,1|
|R-2 Teno Norte|0,2|0,2|0,3|0,3|
|R-3 Estación FFCC Teno|0,2|0,3|0,3|0,3|
|R-4 Teno SE|0,3|0,3|0,4|0,4|
|R-5 Teno Sur|0,2|0,2|0,3|0,3|
|R-6 Teno Oeste|0,1|0,2|0,2|0,2|

La Tabla 5-11 muestra que en todos los casos analizados las concentraciones proyectadas están por
debajo del 40% del valor de la norma anual.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 69 de 147

Código V01: FI-A.03-DSA

**Tabla 5-11 Resultados Niveles de calidad del aire de MP** **2,5** **Anual en PMI y en los seis receptores de interés**

|Receptor|Norma de<br>calidad<br>del aire<br>g/m3N|Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1)|Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2)|Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3)|Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4)|Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma|Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad|
|---|---|---|---|---|---|---|---|
|PMI Teno CBB|20|7,5|0,20|0,5|8,0|38%|40%|
|R-1 Estación<br>Teno ENLASA|20|7,5|0,11|0,2|7,7|38%|39%|
|R-2 Teno Norte|20|7,5|0,01|0,0|7,5|38%|38%|
|R-3 Estación<br>FFCC Teno|20|7,5|0,01|0,0|7,5|38%|38%|
|R-4 Teno SE|20|7,5|0,01|0,0|7,5|38%|38%|
|R-5 Teno Sur|20|7,5|0,01|0,0|7,5|38%|38%|
|R-6 Teno Oeste|20|7,5|0,01|0,0|7,5|38%|38%|

(1) Valor medido en estación ENLASA
(2) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual.
(3) Corresponde a la resta de Escenario 4 - Escenario 3. En este caso se consideran los otros proyectos

no materializados.

(4) Al nivel actual se suma el aporte de todos los proyectos.

En las figuras 5-12 a 5-14, se muestran las concentraciones anuales de MP 2,5 para los escenarios 1 a

4. Se puede apreciar en la figura que los aportes de planta Teno de CBB a las concentraciones de

MP 10 promedio anual disminuyen fuertemente con la distancia a la Planta misma. Luego, en los

sectores poblados de Teno los aportes son bajos en magnitud, tal como ya se ha presentado en la

Tabla anterior, en particular, los valores presentados en los receptores R-2 a R-6.

Cuando se consideran todos los proyectos en operación en la zona, aparecen otras zonas con

aportes relevantes, pero que no corresponden a la operación de Planta Teno de CBB. Los aportes al

promedio anual de MP2,5 se mantienen en todos los casos por debajo de 1 g/m [3] ; la explicación es

la ubicación de las fuentes emisoras con respecto a Teno y el viento predominante en la zona (S y

SW).

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 70 de 147

Código V01: FI-A.03-DSA

**Figura 5-12 Mapa de concentraciones del MP2,5 anual (**  **g/m3) para el escenario 1. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 71 de 147

Código V01: FI-A.03-DSA

**Figura 5-13 Mapa de concentraciones del MP2,5 anual (**  **g/m3) para el escenario 2. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 72 de 147

Código V01: FI-A.03-DSA

**Figura 5-14 Mapa de concentraciones del MP2,5 anual (**  **g/m3) para el escenario 3. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 73 de 147

Código V01: FI-A.03-DSA

**Figura 5-15 Mapa de concentraciones del MP2,5 anual (**  **g/m3) para el escenario 4. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 74 de 147

Código V01: FI-A.03-DSA

En la Tabla 5-12 se presenta para MP 2,5 diario Percentil 98, los aportes a la calidad del aire para los
cuatro escenarios considerados en los 6 receptores sensibles modelados.

**Tabla 5-12 Resultados MP** **2,5** **Percentil 98 diario en los seis receptores discretos y en el punto de máximo impacto**

|Receptor|P. 98 MP<br>2,5<br>Diario<br>Escenario 1<br>g/m3N|P. 98 MP<br>2,5<br>Diario<br>Escenario 2<br>g/m3N|P. 98 MP<br>2,5<br>Diario<br>Escenario 3<br>g/m3N|P. 98 MP<br>2,5<br>Diario<br>Escenario 4<br>g/m3N|
|---|---|---|---|---|
|PMI Teno CBB|22,2|22,4|25,1|27,1|
|R-1 Estación Teno ENLASA|5,9|6,2|6,5|7,4|
|R-2 Teno Norte|1,7|1,7|2,6|2,6|
|R-3 Estación FFCC Teno|2,4|2,5|2,8|2,9|
|R-4 Teno SE|2,4|2,4|3,0|3,0|
|R-5 Teno Sur|2,1|2,1|2,6|2,7|
|R-6 Teno Oeste|1,3|1,3|1,6|1,7|

La Tabla 5-13 muestra que en la ciudad de Teno los niveles diarios proyectados para el MP2,5 están
por debajo del 50% de la norma de calidad.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 75 de 147

Código V01: FI-A.03-DSA

**Tabla 5-13 Resultados Niveles de calidad del aire de MP** **2,5** **P98 diario en PMI y en los seis receptores de interés**

|Receptor|Norma<br>de<br>calidad<br>del aire<br>g/m3N|Nivel actual<br>Calidad del<br>aire<br>g/m3N<br>(1)|Aporte por<br>proyecto<br>CBB<br>g/m3N<br>(2)|Aporte por<br>todos los<br>proyectos<br>g/m3N<br>(3)|Nivel actual<br>mas<br>proyectos<br>g/m3N<br>(4)|Porcentaje<br>Calidad del<br>aire actual<br>respecto de<br>norma|Porcentaje<br>Con<br>proyectos<br>respecto de<br>norma de<br>calidad|
|---|---|---|---|---|---|---|---|
|PMI Teno CBB|50|24|0,3|2,0|26,0|48%|52%|
|R-1 Estación<br>Teno ENLASA|50|24|0,3|0,9|24,9|48%|50%|
|R-2 Teno Norte|50|24|0,0|0,1|24,1|48%|48%|
|R-3 Estación<br>FFCC Teno|50|24|0,1|0,1|24,1|48%|48%|
|R-4 Teno SE|50|24|0,0|0,1|24,1|48%|48%|
|R-5 Teno Sur|50|24|0,1|0,1|24,1|48%|48%|
|R-6 Teno Oeste|50|24|0,0|0,1|24,1|48%|48%|

(1) Valor medido en estación ENLASA
(2) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual. Se

considera mayor diferencia entre Escenario 2-Escenario 1 y escenario 4-escenario 3.
(3) Corresponde a la resta de Escenario 4 - Escenario 3. En este caso se consideran los otros proyectos

no materializados.

(4) Al nivel actual se suma el aporte de todos los proyectos.

En las figuras 5-16 a 5-19 se presentan los resultados para el percentil 98 de las concentraciones

diarias de MP2,5. Nuevamente, los aportes de la planta CBB de Teno disminuyen rápidamente con

la distancia a ella (escenarios 1 y 2). En los escenarios 3 y 4 aparecen otros impactos, asociados a

otros proyectos presentes (o por implementarse) en la zona. En todos los casos los aportes en la

ciudad de Teno se mantienen por debajo de 4 g/m [3] .

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 76 de 147

Código V01: FI-A.03-DSA

**Figura 5-16 Mapa del percentil 98 de las concentraciones diarias de MP** **2,5** **(**  **g/m** **[3]** **) para el escenario 1 . La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 77 de 147

Código V01: FI-A.03-DSA

**Figura 5-17 Mapa del percentil 98 de las concentraciones diarias de MP** **2,5** **(**  **g/m** **[3]** **) para el escenario 2. La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 78 de 147

Código V01: FI-A.03-DSA

**Figura 5-18 Mapa del percentil 98 de las concentraciones diarias de MP** **2,5** **(**  **g/m** **[3]** **) para el escenario 3 . La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 79 de 147

Código V01: FI-A.03-DSA

**Figura 5-19 Mapa del percentil 98 de las concentraciones diarias de MP** **2,5** **(**  **g/m** **[3]** **) para el escenario 4 . La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 80 de 147

Código V01: FI-A.03-DSA

**1.7** **NO** **2**

En el caso del dióxido de nitrógeno (NO 2 ), este contaminante se produce directamente en emisiones
de procesos de combustión, y está incluido en los llamados óxidos de nitrógeno (NO x ) que
corresponden a la suma de NO y NO 2 . El modelo CALPUFF simula la dispersión de los NO x, por lo que
es necesario estimar qué fracción en masa de los NO x corresponde a NO 2 . Esta razón es muy
específica a cada zona urbana, ya que depende de la capacidad oxidativa de las emisiones de NO x y
COV en la cuenca a escala regional. Para poder estimar esa relación, usamos las concentraciones
ambientales de NO 2 y NO x medidas en la estación La Florida en Talca, ya que no disponemos de
datos de la estación de monitoreo ENLASA, donde solo se reporta el NO 2 . La siguiente figura muestra
el análisis de regresión lineal para los datos 2017-2018 de la estación La Florida - Talca. Se aprecia
que el NO 2 se puede estimar como el 28% de los NO x medidos en ese monitor. Además, los datos
horarios del ozono en La Florida son similares a los medidos en la estación ENLASA Teno [9] . Esto

justifica la elección de esa estación para estimar ese factor de conversión de NO x a NO 2 .

**Figura 5-20. Relación entre concentraciones horarias de NOx y de NO** **2** **en la estación de monitoreo La Florida, Talca,**

**[años 2017-2018. Fuente: http://sinca.mma.gob.cl](http://sinca.mma.gob.cl/)**

9 Fuente: Anexo F Informe de Modelación de Energía Latina, de fecha 5 diciembre 2016 de Adenda del
proyecto Central de Generación Eléctrica a Gas Teno.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 81 de 147

Código V01: FI-A.03-DSA

La Tabla 5-14 presenta para el NO 2 anual, los aportes a la calidad del aire para los cuatro escenarios
considerados en los 6 receptores sensibles modelados.

**Tabla 5-14 Resultados NO** **2** **Anual en PMI y en los seis receptores de interés**

|Receptor|NO Anual<br>2<br>Escenario 1<br>g/m3N|NO Anual<br>2<br>Escenario 2<br>g/m3N|NO Anual<br>2<br>Escenario 3<br>g/m3N|NO Anual<br>2<br>Escenario 4<br>g/m3N|
|---|---|---|---|---|
|PMI Teno CBB|44,7|45,2|45,3|48,5|
|R-1 Estación Teno ENLASA|9,0|9,2|9,1|9,9|
|R-2 Teno Norte|0,6|0,6|0,6|0,6|
|R-3 Estación FFCC Teno|0,7|0,7|0,8|0,8|
|R-4 Teno SE|0,9|0,9|1,0|1,0|
|R-5 Teno Sur|0,6|0,6|0,6|0,6|
|R-6 Teno Oeste|0,3|0,4|0,4|0,4|

La Tabla 5-15 muestra que en la ciudad de Tenos los aportes proyectados están por debajo del 20%

de la norma anual.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 82 de 147

Código V01: FI-A.03-DSA

**Tabla 5-15 Resultados Niveles de calidad del aire de NO** **2** **Anual en PMI y en los seis receptores de interés**

|Receptor|Norma de<br>calidad<br>del aire<br>g/m3N|Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1)|Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2)|Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3)|Nivel<br>actual<br>mas<br>proyectos<br>g/m3N<br>(4)|Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma|Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad|
|---|---|---|---|---|---|---|---|
|PMI Teno CBB|100|18,7|0,50|3,14|21,84|19%|22%|
|R-1 Estación<br>Teno ENLASA|100|18,7|0,26|0,78|19,48|19%|19%|
|R-2 Teno Norte|100|18,7|0,01|0,02|18,72|19%|19%|
|R-3 Estación<br>FFCC Teno|100|18,7|0,01|0,02|18,72|19%|19%|
|R-4 Teno SE|100|18,7|0,02|0,02|18,72|19%|19%|
|R-5 Teno Sur|100|18,7|0,01|0,02|18,72|19%|19%|
|R-6 Teno Oeste|100|18,7|0,01|0,01|18,71|19%|19%|

(1) Valor medido en estación ENLASA
(2) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual. Se

considera mayor diferencia entre Escenario 2-Escenario 1 y escenario 4-escenario 3.
(3) Corresponde a la resta de Escenario 4 - Escenario 3. En este caso se consideran los otros proyectos

no materializados.

(4) Al nivel actual se suma el aporte de todos los proyectos.

En las figuras 5-21 a 5-24 se muestra las curvas de contorno de concentraciones promedio anual de

NO 2 para los escenarios 1 a 4, respectivamente. En todos los casos los PMI se encuentran al NW de

la estación de monitoreo de calidad del aire (Receptor R_1), cerca de dicha estación. Se puede

apreciar en la figura que los aportes de la Planta Teno de CBB a las concentraciones de NO 2 promedio

anual disminuyen fuertemente con la distancia a la Planta (escenarios 1 y 2). Luego, en la ciudad de

Teno los aportes son bajos en magnitud (por debajo de 2 g/m [3] ), tal como ya se ha presentado en

la Tabla 5-15.

<!-- INICIO TABLA 5-15 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Página 82 de 147 Código V01: FI-A.03-DSA -->

**Tabla 5-15: Resultados Niveles de calidad del aire de NO** **2** **Anual en PMI y en los seis receptores de interés****

| Receptor | Norma de<br>calidad<br>del aire<br>g/m3N | Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1) | Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2) | Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3) | Nivel<br>actual<br>mas<br>proyectos<br>g/m3N<br>(4) | Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma | Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PMI Teno CBB | 100 | 18,7 | 0,50 | 3,14 | 21,84 | 19% | 22% |
| R-1 Estación<br>Teno ENLASA | 100 | 18,7 | 0,26 | 0,78 | 19,48 | 19% | 19% |
| R-2 Teno Norte | 100 | 18,7 | 0,01 | 0,02 | 18,72 | 19% | 19% |
| R-3 Estación<br>FFCC Teno | 100 | 18,7 | 0,01 | 0,02 | 18,72 | 19% | 19% |
| R-4 Teno SE | 100 | 18,7 | 0,02 | 0,02 | 18,72 | 19% | 19% |
| R-5 Teno Sur | 100 | 18,7 | 0,01 | 0,02 | 18,72 | 19% | 19% |
| R-6 Teno Oeste | 100 | 18,7 | 0,01 | 0,01 | 18,71 | 19% | 19% |

<!-- Estadísticas: 7 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- (1) Valor medido en estación ENLASA (2) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual. Se considera mayor diferencia entre Escenario 2-Escenario 1 y escenario 4-escenario 3. -->
<!-- FIN TABLA 5-15 -->


Al considerarse los demás proyectos en operación en la zona, aumentan los aportes antropogénicos

a las concentraciones anuales de NO 2, pero esos aportes no están asociados a la operación de la

Planta Teno de CBB, sino que provienen de otros proyectos. Se apreciar gráficamente la condición

de que los aportes en la ciudad de Teno se mantienen por debajo de 2 g/m [3] .

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 83 de 147

Código V01: FI-A.03-DSA

**Figura 5-21 Mapa de concentraciones del NO** **2** **anual (**  **g/m** **[3]** **) para el escenario 1. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 84 de 147

Código V01: FI-A.03-DSA

**Figura 5-22 Mapa de concentraciones del NO** **2** **anual (**  **g/m** **[3]** **) para el escenario 2. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 85 de 147

Código V01: FI-A.03-DSA

**Figura 5-23 Mapa de concentraciones del NO** **2** **anual (**  **g/m** **[3]** **) para el escenario 3. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 86 de 147

Código V01: FI-A.03-DSA

**Figura 5-24 Mapa de concentraciones del NO** **2** **anual (**  **g/m** **[3]** **) para el escenario 4. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 87 de 147

Código V01: FI-A.03-DSA

En la Tabla 5-16 se presenta para el NO 2 horario Percentil 99, los aportes a la calidad del aire para

los cuatro escenarios considerados en los 6 receptores sensibles modelados.

**Tabla 5-16 Resultados NO** **2** **horario Percentil 99 en los seis receptores discretos y en el punto de máximo impacto**

|Receptor|P. 99<br>NO Horario<br>2<br>Escenario 1<br>g/m3N|P. 99<br>NO Horario<br>2<br>Escenario 2<br>g/m3N|P. 99<br>NO Horario<br>2<br>Escenario 3<br>g/m3N|P. 99<br>NO Horario<br>2<br>Escenario 4<br>g/m3N|
|---|---|---|---|---|
|PMI Teno CBB|121|124|132|139|
|R-1 Estación Teno ENLASA|82|85|82|87|
|R-2 Teno Norte|51|52|55|57|
|R-3 Estación FFCC Teno|48|50|49|50|
|R-4 Teno SE|56|56|56|56|
|R-5 Teno Sur|31|31|32|32|
|R-6 Teno Oeste|24|24|24|24|

La Tabla 5-17 muestra que las concentraciones proyectadas en la ciudad de Teno se mantienen por

debajo del 20% de la norma de corto plazo del NO 2 .

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 88 de 147

Código V01: FI-A.03-DSA

**Tabla 5-17 Resultados Niveles de calidad del aire de NO** **2** **horario P 99 en PMI y en los seis receptores de interés**

|Receptor|Norma de<br>calidad<br>del aire<br>g/m3N|Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1)|Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2)|Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3)|Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4)|Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma|Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad|
|---|---|---|---|---|---|---|---|
|PMI Teno CBB|400|67|3,2|7,1|74,1|17%|19%|
|R-1 Estación<br>Teno ENLASA|400|67|2,9|5,5|72,5|17%|18%|
|R-2 Teno Norte|400|67|1,0|1,2|68,2|17%|17%|
|R-3 Estación<br>FFCC Teno|400|67|1,4|1,4|68,4|17%|17%|
|R-4 Teno SE|400|67|0,1|0,1|67,1|17%|17%|
|R-5 Teno Sur|400|67|0,0|0,0|67,0|17%|17%|
|R-6 Teno Oeste|400|67|0,1|0,1|67,1|17%|17%|

(1) Valor medido en estación ENLASA
(2) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual. Se

considera mayor diferencia entre Escenario 2-Escenario 1 y escenario 4-escenario 3.
(3) Corresponde a la resta de Escenario 5 - Escenario 3. En este caso se consideran los otros proyectos

no materializados.

(4) Al nivel actual se suma el aporte de todos los proyectos.

Con respecto a los percentiles 99 de las máximas concentraciones horarias de NO 2, las diferencias

entre el escenario 1 y 2 son mínimas, menores al 1% de la norma horaria respectiva, lo que indica

que la implementación del Proyecto no va a modificar la distribución del NO 2 horario en forma

significativa en la zona poblada de Teno.

En las figuras 5-25 a 5-28 se muestra las curvas de nivel de las concentraciones horarias máximas

de NO 2, para los escenarios 1 a 4, respectivamente (no es posible procesar los datos para obtener

los percentiles 99 dentro del ambiente computacional que realiza las modelaciones de calidad del

aire). Hay que tener presente que al aplicarse el procesamiento de percentiles de acuerdo a la norma

de calidad del NO 2, los valores se reducen bastante, como se puede apreciar al comparar los

impactos horarios máximos en los PMI con respecto a los percentiles 99 procesados y mostrados en

la. En otras palabras, las figuras 5-25 a 5-29 muestran sobreestimaciones de las concentraciones

consideradas en la norma horaria del NO 2 .

En todo caso, nuevamente se aprecia que los aportes de la Planta Teno de CBB a las concentraciones

horarias de NO 2 disminuyen rápidamente con la distancia a la Planta Teno (escenarios 1 y 2), y que

los incrementos de los percentiles 99 de las concentraciones horarias de NO 2 son menores del 20%

de los niveles actuales medidos en la zona.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 89 de 147

Código V01: FI-A.03-DSA

**Figura 5-25 Mapa de concentraciones horarias máximas del NO** **2** **(**  **g/m** **[3]** **) para el escenario 1. La ciudad de Teno está delimitada por el polígono negro. El perímetro del**

**proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 90 de 147

Código V01: FI-A.03-DSA

**Figura 5-26 Mapa de concentraciones horarias máximas del NO** **2** **(**  **g/m** **[3]** **) para el escenario 2. La ciudad de Teno está delimitada por el polígono negro. El perímetro del**

**proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 91 de 147

Código V01: FI-A.03-DSA

**Figura 5-27 Mapa de concentraciones horarias máximas del NO** **2** **(**  **g/m** **[3]** **) para el escenario 3. La ciudad de Teno está delimitada por el polígono negro. El perímetro del**

**proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 92 de 147

Código V01: FI-A.03-DSA

**Figura 5-28 Mapa de concentraciones horarias máximas del NO** **2** **(**  **g/m** **[3]** **) para el escenario 4. La ciudad de Teno está delimitada por el polígono negro. El perímetro del**

**proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 93 de 147

Código V01: FI-A.03-DSA

**1.8** **SO** **2**

La Tabla 5-18 presenta para SO 2 anual, los aportes a la calidad del aire para los cuatro escenarios
considerados en los 6 receptores sensibles modelados.

**Tabla 5-18 Resultados SO** **2** **Anual en PMI y los seis receptores de interés**

|Receptor|SO Anual<br>2<br>Escenario 1<br>g/m3N|SO Anual<br>2<br>Escenario 2<br>g/m3N|SO Anual<br>2<br>Escenario 3<br>g/m3N|SO Anual<br>2<br>Escenario 4<br>g/m3N|
|---|---|---|---|---|
|PMI Teno CBB|10,1|9,9|11,9|11,7|
|R-1 Estación Teno ENLASA|4,0|3,9|4,2|4,1|
|R-2 Teno Norte|0,2|0,2|0,3|0,3|
|R-3 Estación FFCC Teno|0,2|0,2|0,2|0,2|
|R-4 Teno SE|0,3|0,3|0,3|0,3|
|R-5 Teno Sur|0,2|0,2|0,2|0,2|
|R-6 Teno Oeste|0,1|0,1|0,2|0,2|

La Tabla 5-19 muestra que las concentraciones proyectadas se van a mantener por debajo del 10%
de la norma anual del SO 2 .

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 94 de 147

Código V01: FI-A.03-DSA

**Tabla 5-19 Resultados Niveles de calidad del aire de SO** **2** **Anual en PMI y los seis receptores de interés**

|Receptor|Norma de<br>calidad<br>del aire<br>g/m3N|Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1)|Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2)|Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3)|Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4)|Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma|Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad|
|---|---|---|---|---|---|---|---|
|PMI Teno CBB|60|6,3|-0,22|-0,20|6,10|11%|10%|
|R-1 Estación<br>Teno ENLASA|60|6,3|-0,12|-0,11|6,19|11%|10%|
|R-2 Teno Norte|60|6,3|-0,01|0,00|6,30|11%|10%|
|R-3 Estación<br>FFCC Teno|60|6,3|-0,01|-0,01|6,29|11%|10%|
|R-4 Teno SE|60|6,3|-0,01|-0,01|6,29|11%|10%|
|R-5 Teno Sur|60|6,3|-0,01|0,00|6,30|11%|10%|
|R-6 Teno Oeste|60|6,3|0,00|0,00|6,30|11%|10%|

(1) Valor medido en estación ENLASA
(2) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual.
(3) Corresponde a la resta de Escenario 4 - Escenario 3. En este caso se consideran los otros proyectos

no materializados.

(4) Al nivel actual se suma el aporte de todos los proyectos.

En las figuras 5-29 a 5-32, se muestran las curvas de contorno de las concentraciones promedio

anual de SO 2 para los escenarios 1 a 4, respectivamente. En todos los casos los PMI se encuentran

al NW de Teno. Los aportes de Planta Teno de CBB a las concentraciones de SO 2 promedio anual

disminuyen fuertemente con la distancia a ella (escenarios 1 y 2). Luego, en los sectores poblados

de Teno los aportes son bajos en magnitud, tal como ya se ha presentado en la Tabla anterior, en

particular los valores presentados en los receptores R-2 a R-6. En todos los casos los aportes se

mantienen por debajo de 1 g/m [3] .

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 95 de 147

Código V01: FI-A.03-DSA

**Figura 5-29 Mapa de concentraciones del SO** **2** **anual (**  **g/m** **[3]** **) para el escenario 1. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 96 de 147

Código V01: FI-A.03-DSA

**Figura 5-30 Mapa de concentraciones del SO** **2** **anual (**  **g/m** **[3]** **) para el escenario 2. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 97 de 147

Código V01: FI-A.03-DSA

**Figura 5-31 Mapa de concentraciones del SO** **2** **anual (**  **g/m** **[3]** **) para el escenario 3. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 98 de 147

Código V01: FI-A.03-DSA

**Figura 5-32 Mapa de concentraciones del SO** **2** **anual (**  **g/m** **[3]** **) para el escenario 4. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 99 de 147

Código V01: FI-A.03-DSA

La Tabla 5-20 presenta para SO 2 diario Percentil 99, los aportes a la calidad del aire para los cuatro

escenarios considerados en los 6 receptores sensibles modelados.

**Tabla 5-20 Resultados SO** **2** **Percentil 99 diario en los seis receptores discretos y** **punto de máximo impacto**

|Receptor|P. 99<br>SO Diario<br>2<br>Escenario 1<br>g/m3N|P. 99<br>SO Diario<br>2<br>Escenario 2<br>g/m3N|P. 99<br>SO Diario<br>2<br>Escenario 3<br>g/m3N|P. 99<br>SO Diario<br>2<br>Escenario 4<br>g/m3N|
|---|---|---|---|---|
|PMI Teno CBB|28,8|28,0|58,0|57,7|
|R-1 Estación Teno ENLASA|19,4|18,9|19,9|19,3|
|R-2 Teno Norte|2,7|2,6|3,0|2,9|
|R-3 Estación FFCC Teno|3,1|3,0|3,1|3,1|
|R-4 Teno SE|3,1|3,0|3,1|3,0|
|R-5 Teno Sur|2,7|2,6|2,8|2,7|
|R-6 Teno Oeste|1,8|1,8|1,9|1,9|

La Tabla 5-21 muestra que las concentraciones diarias proyectadas se mantienen por debajo del
30% de la norma del SO 2 .

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 100 de 147

Código V01: FI-A.03-DSA

**Tabla 5-21 Resultados Niveles de calidad del aire de SO** **2** **P99 diario en PMI y en los seis receptores de interés**

|Receptor|Norma de<br>calidad<br>del aire<br>g/m3N|Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1)|Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2)|Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3)|Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4)|Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma|Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad|
|---|---|---|---|---|---|---|---|
|PMI Teno CBB|150|38,3|-0,8|-0,3|38,0|26%|25%|
|R-1 Estación<br>Teno ENLASA|150|38,3|-0,6|-0,6|37,7|26%|25%|
|R-2 Teno Norte|150|38,3|-0,1|-0,1|38,2|26%|25%|
|R-3 Estación<br>FFCC Teno|150|38,3|-0,1|-0,1|38,2|26%|25%|
|R-4 Teno SE|150|38,3|-0,1|-0,1|38,2|26%|25%|
|R-5 Teno Sur|150|38,3|-0,1|-0,1|38,2|26%|25%|
|R-6 Teno Oeste|150|38,3|-0,1|0,0|38,3|26%|26%|

(1) Valor medido en estación ENLASA
(2) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual.
(3) Corresponde a la resta de Escenario 4 - Escenario 3. En este caso se consideran los otros proyectos

no materializados.

(4) Al nivel actual se suma el aporte de todos los proyectos.

Las figuras 5-33 a 5-36, muestra las curvas de contorno para el percentil 99 de las concentraciones

diarias de SO 2, para los cuatro escenarios analizados, respectivamente. Nuevamente se aprecia que

los aportes de Planta Teno de CBB a las concentraciones de SO 2 disminuyen rápidamente con la

distancia a la Planta (escenarios 1 y 2, Figura 5-33). Al considerarse la operación de los restantes

proyectos en la zona, se aprecia que las máximas concentraciones ahora están al ESE de Teno,

debido a la presencia de esos otros proyectos. Además, en la zona de Teno, las concentraciones son

bajas, como ya se ha comentado en las Tablas anteriores. En todos los casos los aportes de las

fuentes modeladas se mantienen por debajo de 5 g/m [3] .

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 101 de 147

Código V01: FI-A.03-DSA

**Figura 5-33 Mapa del percentil 99 de las concentraciones diarias de SO** **2** **(**  **g/m** **[3]** **) para el escenario 1. La ciudad de Teno está delimitada por el polígono negro. El perímetro del**

**proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 102 de 147

Código V01: FI-A.03-DSA

**Figura 5-34 Mapa del percentil 99 de las concentraciones diarias de SO** **2** **(**  **g/m** **[3]** **) para el escenario 2. La ciudad de Teno está delimitada por el polígono negro. El perímetro del**

**proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 103 de 147

Código V01: FI-A.03-DSA

**Figura 5-35 Mapa del percentil 99 de las concentraciones diarias de SO** **2** **(**  **g/m** **[3]** **) para el escenario 3. La ciudad de Teno está delimitada por el polígono negro. El perímetro del**

**proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 104 de 147

Código V01: FI-A.03-DSA

**Figura 5-36 Mapa del percentil 99 de las concentraciones diarias de SO** **2** **(**  **g/m** **[3]** **) para el escenario 4. La ciudad de Teno está delimitada por el polígono negro. El perímetro del**

**proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 105 de 147

Código V01: FI-A.03-DSA

En la Tabla 5-22 se presenta para las concentraciones de SO 2 horario, norma primaria y secundaria,

los aportes a la calidad del aire para los cuatro escenarios considerados en los 6 receptores sensibles

modelados.

**Tabla 5-22 Resultados SO** **2** **horario P99 (**  **g/m** **[3]** **) en los seis receptores discretos y** **punto de máximo impacto**

|Receptor|SO Horario<br>2<br>Escenario 1<br>g/m3N|SO Horario<br>2<br>Escenario 2<br>g/m3N|SO Horario<br>2<br>Escenario 3<br>g/m3N|SO Horario<br>2<br>Escenario 4<br>g/m3N|
|---|---|---|---|---|
|Análisis P99|Análisis P99|Análisis P99|Análisis P99|Análisis P99|
|PMI Teno CBB|57|55|75|73|
|R-1 Estación Teno ENLASA|35|34|36|35|
|R-2 Teno Norte|3|3|3|3|
|R-3 Estación FFCC Teno|4|4|4|4|
|R-4 Teno SE|5|5|5|5|
|R-5 Teno Sur|3|3|3|3|
|R-6 Teno Oeste|2|2|2|2|
|Análisis P99,73|Análisis P99,73|Análisis P99,73|Análisis P99,73|Análisis P99,73|
|PMI Teno CBB|78|76|141|140|
|R-1 Estación Teno ENLASA|44|42|51|49|
|R-2 Teno Norte|9|8|10|10|
|R-3 Estación FFCC Teno|12|12|12|12|
|R-4 Teno SE|13|13|13|13|
|R-5 Teno Sur|10|10|11|11|
|R-6 Teno Oeste|6|6|7|6|

La Tabla 5-23 muestra las concentraciones horarias proyectadas, y se constata que ellas vana a estar
por debajo del 20% de la norma de calidad primaria y por debajo del 15% de la norma de calidad
secundaria para SO2.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 106 de 147

Código V01: FI-A.03-DSA

**Tabla 5-23 Resultados Niveles de calidad del aire de SO** **2** **P99 Horario en PMI y los seis receptores de interés**

|Receptor|Norma de<br>calidad<br>del aire<br>g/m3N|Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1)|Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2)|Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3)|Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4)|Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma|Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad|
|---|---|---|---|---|---|---|---|
|Análisis P99|Análisis P99|Análisis P99|Análisis P99|Análisis P99|Análisis P99|Análisis P99|Análisis P99|
|PMI Teno CBB|350|64,1|-1,8|-1,5|62,6|18%|18%|
|R-1 Estación<br>Teno ENLASA|350|64,1|-1,1|-1,1|63,0|18%|18%|
|R-2 Teno Norte|350|64,1|-0,1|0,0|64,1|18%|18%|
|R-3 Estación<br>FFCC Teno|350|64,1|-0,1|-0,1|64,0|18%|18%|
|R-4 Teno SE|350|64,1|-0,1|-0,1|64,0|18%|18%|
|R-5 Teno Sur|350|64,1|-0,1|-0,1|64,0|18%|18%|
|R-6 Teno Oeste|350|64,1|-0,1|-0,1|64,0|18%|18%|
|Análisis P99,73|Análisis P99,73|Análisis P99,73|Análisis P99,73|Análisis P99,73|Análisis P99,73|Análisis P99,73|Análisis P99,73|
|PMI Teno CBB|700|105,1|-2,4|-0,7|104,5|15%|15%|
|R-1 Estación<br>Teno ENLASA|700|105,1|-1,3|-1,6|103,5|15%|15%|
|R-2 Teno Norte|700|105,1|-0,3|-0,3|104,8|15%|15%|
|R-3 Estación<br>FFCC Teno|700|105,1|-0,3|-0,1|105,0|15%|15%|
|R-4 Teno SE|700|105,1|-0,4|-0,4|104,7|15%|15%|
|R-5 Teno Sur|700|105,1|-0,3|-0,2|104,9|15%|15%|
|R-6 Teno Oeste|700|105,1|-0,2|-0,2|104,9|15%|15%|

(1) Valor medido en estación ENLASA
(2) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual.
(3) Corresponde a la resta de Escenario 4 - Escenario 3. En este caso se consideran los otros proyectos

no materializados.

(4) Al nivel actual se suma el aporte de todos los proyectos.

En las figuras 5-37 a 5-40, se muestran las curvas de contorno de las concentraciones horarias de

SO 2 (percentil 99) para los cuatro escenarios modelados, respectivamente. Se aprecia que los

aportes de Planta Teno de CBB a las concentraciones horarias de SO 2 disminuyen rápidamente con

la distancia a la Planta Teno (escenarios 1 y 2). Al considerarse todos los proyectos en la zona,

aparece un área de mayores aportes hacia el este de Teno, con una extensión de 2 km O-E y 3 km

S-N aproximadamente, es decir, un área acotada. En todos los casos los aportes en Teno se

mantienen por debajo de 10 g/m [3] .

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 107 de 147

Código V01: FI-A.03-DSA

**Figura 5-37 Mapa de percentil 99 de las concentraciones horarias del SO** **2** **(**  **g/m** **[3]** **) para el escenario 1. La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 108 de 147

Código V01: FI-A.03-DSA

**Figura 5-38 Mapa de percentil 99 de las concentraciones horarias del SO** **2** **(**  **g/m** **[3]** **) para el escenario 2. La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 109 de 147

Código V01: FI-A.03-DSA

**Figura 5-39 Mapa de percentil 99 de las concentraciones horarias del SO** **2** **(**  **g/m** **[3]** **) para el escenario 3. La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 110 de 147

Código V01: FI-A.03-DSA

**Figura 5-40 Mapa de percentil 99 de las concentraciones horarias del SO** **2** **(**  **g/m** **[3]** **) para el escenario 4. La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 111 de 147

Código V01: FI-A.03-DSA

**Figura 5-41 Mapa de percentil 99,73 de las concentraciones horarias del SO** **2** **(**  **g/m** **[3]** **) para el escenario 1. La ciudad de Teno está delimitada por el polígono negro. El**

**perímetro del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 112 de 147

Código V01: FI-A.03-DSA

**Figura 5-42 Mapa de percentil 99,73 de las concentraciones horarias del SO** **2** **(**  **g/m** **[3]** **) para el escenario 2. La ciudad de Teno está delimitada por el polígono negro. El**

**perímetro del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 113 de 147

Código V01: FI-A.03-DSA

**Figura 5-43 Mapa de percentil 99,73 de las concentraciones horarias del SO** **2** **(**  **g/m** **[3]** **) para el escenario 3. La ciudad de Teno está delimitada por el polígono negro. El**

**perímetro del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 114 de 147

Código V01: FI-A.03-DSA

**Figura 5-44 Mapa de percentil 99,73 de las concentraciones horarias del SO** **2** **(**  **g/m** **[3]** **) para el escenario 4. La ciudad de Teno está delimitada por el polígono negro. El**

**perímetro del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 115 de 147

Código V01: FI-A.03-DSA

**1.9** **CO**

La Tabla 5-24 presenta para CO horario percentil 99, los aportes a la calidad del aire para los cuatro
escenarios considerados en los 6 receptores sensibles modelados.

**Tabla 5-24 Resultados CO Percentil 99 horario en los seis receptores discretos y** **punto de máximo impacto**

|Receptor|P. 99<br>CO<br>Horario<br>Escenario 1<br>g/m3N|P. 99<br>CO<br>Horario<br>Escenario 2<br>g/m3N|P. 99<br>CO<br>Horario<br>Escenario 3<br>g/m3N|P. 99<br>CO<br>Horario<br>Escenario 4<br>g/m3N|
|---|---|---|---|---|
|PMI Teno CBB|50|56|195|195|
|R-1 Estación Teno ENLASA|39|44|47|83|
|R-2 Teno Norte|16|17|17|19|
|R-3 Estación FFCC Teno|13|15|14|16|
|R-4 Teno SE|14|15|14|16|
|R-5 Teno Sur|10|11|11|13|
|R-6 Teno Oeste|10|11|10|11|

La Tabla 5-25 muestra que en todos los casos las concentraciones proyectadas en la ciudad de Teno
no superan el 3% del valor de la norma horaria.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 116 de 147

Código V01: FI-A.03-DSA

**Tabla 5-25 Resultados Niveles de calidad del aire de CO P99 horario en PMI y los seis receptores de interés**

|Receptor|Norma de<br>calidad<br>del aire<br>g/m3N|Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1)|Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2)|Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3)|Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4)|Porcentaje<br>de<br>aumento<br>nivel actual|Porcentaje<br>respecto a<br>norma de<br>calidad|
|---|---|---|---|---|---|---|---|
|PMI Teno CBB|30.000|1.000|5|0|1000|3%|3%|
|R-1 Estación<br>Teno ENLASA|30.000|1.000|4|36|1036|3%|3%|
|R-2 Teno Norte|30.000|1.000|2|2|1002|3%|3%|
|R-3 Estación<br>FFCC Teno|30.000|1.000|1|2|1002|3%|3%|
|R-4 Teno SE|30.000|1.000|1|2|1002|3%|3%|
|R-5 Teno Sur|30.000|1.000|1|1|1001|3%|3%|
|R-6 Teno Oeste|30.000|1.000|1|1|1001|3%|3%|

(1) Valor medido en estación ENLASA
(2) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual.
(3) Corresponde a la resta de Escenario 4 - Escenario 3. En este caso se consideran los otros proyectos

no materializados.

(4) Al nivel actual se suma el aporte de todos los proyectos.

Las figuras 5-41 a 5-44 muestran las máximas concentraciones horarias de CO para los escenarios 1

a 4, respectivamente. Se aprecia que se trata de valores muy bajos con respecto a la norma horaria

que es de 30.000 g/m [3] . Lo mismo pasa al considerarse todos los proyectos operando en la zona.

En todos los casos los aportes se mantienen por debajo de 200 g/m [3] .

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 117 de 147

Código V01: FI-A.03-DSA

**Figura 5-45 Mapa de concentraciones horarias máximas de CO (**  **g/m** **[3]** **) para el escenario 1. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto**

**está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 118 de 147

Código V01: FI-A.03-DSA

**Figura 5-46 Mapa de concentraciones horarias máximas de CO (**  **g/m** **[3]** **) para el escenario 2. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto**

**está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 119 de 147

Código V01: FI-A.03-DSA

**Figura 5-47 Mapa de concentraciones horarias máximas de CO (**  **g/m** **[3]** **) para el escenario 3. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto**

**está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 120 de 147

Código V01: FI-A.03-DSA

**Figura 5-48 Mapa de concentraciones horarias máximas de CO (**  **g/m** **[3]** **) para el escenario 4. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto**

**está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 121 de 147

Código V01: FI-A.03-DSA

En la Tabla 5-26 se presenta para el promedio móvil de 8 horas de CO, Percentil 99, los aportes a la

calidad del aire para los cuatro escenarios considerados en los 6 receptores sensibles modelados.

**Tabla 5-26 Resultados CO Percentil 99 8 horas en los seis receptores discretos y** **punto de máximo impacto**

|Receptor|P. 99<br>CO<br>8 horas<br>Escenario 1<br>g/m3N|P. 99<br>CO<br>8 horas<br>Escenario 2<br>g/m3N|P. 99<br>CO<br>8 horas<br>Escenario 3<br>g/m3N|P. 99<br>CO<br>8 horas<br>Escenario 4<br>g/m3N|
|---|---|---|---|---|
|PMI Teno CBB|22|25|95|96|
|R-1 Estación Teno ENLASA|16|18|19|44|
|R-2 Teno Norte|2|3|3|3|
|R-3 Estación FFCC Teno|2|3|3|3|
|R-4 Teno SE|3|3|3|3|
|R-5 Teno Sur|2|2|2|2|
|R-6 Teno Oeste|2|2|2|2|

La Tabla 5-27 muestra que las concentraciones proyectadas para el CO para promedios móviles de
8 horas van a mantenerse por debajo del 7% del valor de la norma.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 122 de 147

Código V01: FI-A.03-DSA

**Tabla 5-27 Resultados Niveles de calidad del aire de CO P99 8 horas en PMI y los seis receptores de interés**

|Receptor|Norma de<br>calidad<br>del aire<br>g/m3N|Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1)|Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2)|Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3)|Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4)|Porcentaje<br>de<br>aumento<br>nivel actual|Porcentaje<br>respecto a<br>norma de<br>calidad|
|---|---|---|---|---|---|---|---|
|PMI Teno CBB|10.000|700|2|1|701|7%|7%|
|R-1 Estación<br>Teno ENLASA|10.000|700|2|26|726|7%|7%|
|R-2 Teno Norte|10.000|700|0|1|701|7%|7%|
|R-3 Estación<br>FFCC Teno|10.000|700|0|0|700|7%|7%|
|R-4 Teno SE|10.000|700|0|0|700|7%|7%|
|R-5 Teno Sur|10.000|700|0|0|700|7%|7%|
|R-6 Teno Oeste|10.000|700|0|0|700|7%|7%|

(1) Valor medido en estación ENLASA
(2) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual. Se

considera mayor diferencia entre Escenario 2-Escenario 1 y escenario 4-escenario 3.
(3) Corresponde a la resta de Escenario 5 - Escenario 3. En este caso se consideran los otros proyectos

no materializados.

(4) Al nivel actual se suma el aporte de todos los proyectos

Las figuras 5-45 a 5-48 muestran las curvas de contorno de las concentraciones de 8 horas percentil

99 de CO para los esceanarios 1 a 4, respectivamente. El comportamiento espacial de estos

promedios móviles de 8 horas es similar al caso de las concentraciones horarias. En la ciudad de

Teno los aportes no superan los 25 g/m [3] .

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 123 de 147

Código V01: FI-A.03-DSA

**Figura 5-49 Mapa de concentraciones máximas de CO (**  **g/m** **[3]** **) promedio de 8 horas, para el escenario 1. La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 124 de 147

Código V01: FI-A.03-DSA

**Figura 5-50 Mapa de concentraciones máximas de CO (**  **g/m** **[3]** **) promedio de 8 horas, para el escenario 2. La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 125 de 147

Código V01: FI-A.03-DSA

**Figura 5-51 Mapa de concentraciones máximas de CO (**  **g/m** **[3]** **) promedio de 8 horas, para el escenario 3. La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 126 de 147

Código V01: FI-A.03-DSA

**Figura 5-52 Mapa de concentraciones máximas de CO (**  **g/m** **[3]** **) promedio de 8 horas, para el escenario 4. La ciudad de Teno está delimitada por el polígono negro. El perímetro**

**del proyecto está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 127 de 147

Código V01: FI-A.03-DSA

**1.10** **PLOMO**

El plomo es el único metal pesado con una norma de calidad primaria del aire. El valor de la norma
se expresa para el promedio anual y es de 0,5 g/m [3] .

La siguiente Tabla presenta para plomo anual, los aportes a la calidad del aire para los cuatro
escenarios considerados en los 6 receptores sensibles modelados.

**Tabla 5-28 Resultados Plomo en PMI y los seis receptores de interés y comparación con norma de calidad**

|Receptor|Pb Anual<br>Escenario 1<br>g/m3N|Pb Anual<br>Escenario 2<br>g/m3N|Aumento por<br>Proyecto CBB<br>g/m3N|Norma<br>Calidad de<br>aire<br>g/m3N|Aumento<br>respecto de<br>norma<br>calidad %|
|---|---|---|---|---|---|
|PMI Teno CBB|0,00045|0,00313|0,0027|0,5|0,54%|
|R-1 Estación Teno ENLASA|0,00024|0,00165|0,0014|0,5|0,28%|
|R-2 Teno Norte|0,00001|0,00008|0,0001|0,5|0,01%|
|R-3 Estación FFCC Teno|0,00001|0,00009|0,0001|0,5|0,02%|
|R-4 Teno SE|0,00001|0,00010|0,0001|0,5|0,02%|
|R-5 Teno Sur|0,00001|0,00008|0,0001|0,5|0,01%|
|R-6 Teno Oeste|0,00001|0,00006|0,0001|0,5|0,01%|

No hay mediciones de plomo en calidad del aire, por lo tanto, sólo se compara respecto de la norma

de calidad, observando que en el punto de máximo impacto el aumento sería respecto de la norma

de un 0,54%, en estación ENLASA de un 0,28%, y en los receptores de Teno, por debajo del 0,03%.

Por lo tanto, el aumento no sería significativo.

En la Figura 5-53, se muestra para los escenarios 1 y 2, las curvas de nivel de las concentraciones

promedio anual de Plomo. Se aprecia que los promedios anuales de plomo modelados son muy

bajos, ya que los máximos promedios anuales son de a 0,00067 y 0,0047 g/m [3], respectivamente,

muy por debajo de la norma de 0,5 g/m [3] .

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 128 de 147

Código V01: FI-A.03-DSA

**Figura 5-53. Mapa de concentraciones anuales de plomo (**  **g/m** **[3]** **), para los escenarios 1 (panel superior), y 2 (panel**
**inferior). La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está marcado con una**

**línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 129 de 147

Código V01: FI-A.03-DSA

**1.11** **DEPOSITACIÓN TOTAL DE AZUFRE Y NITRÓGENO EN LA ZONA.**

Un parámetro que interesa evaluar también en la zona es la depositación total de acidez, medida

como azufre (S) y nitrógeno (N) total depositados en la zona modelada, asociados con la operación

actual y futura de los proyectos industriales vigentes.

El modelo CALPUFF permite estimar esa depósitacion, expresada en equivalentes [10] por hectárea al

año (eq/ha/año). Las siguientes figuras 5-50 a 5-57 entregan los resultados para S y N,

respectivamente. El PMI para el S y el N es el mismo PMI asociado a la operación de la planta Teno

de Cbb, con coordenadas UTM (WGS84, zona 19) 304.470 m E y 6.140.362 m N. Los impactos

disminuyen rápidamente con la distancia a ese PMI, como se puede apreciar en las figuras 5-50 a 5
57.

Para poner estos resultados en términos de impactos, habría que calcular cual es la capacidad

máxima de carga ácida en la cuenca, lo que implica un esfuerzo de modelación que queda fuera del

alcance del presente análisis. Recurriendo a referencias bibliográficas [11], encontramos que para el

caso del estado de California en EEUU (con clima y precipitaciones similares a la zona modelada), las


cargas críticas de acidez en ecosistemas están sobre los 1000 eq/(ha año), por lo que se puede

concluir que el proyecto no va a presentar impactos significativos por acidificación de los suelos, ya

que el ecosistema es capaz de soportar las cargas ácidas aquí estimadas.

En efecto, excepto por una pequeña zona alrededor del PMI asociado a la Planta Teno de Cbb, los


valores de la depositación de S y N se reducen a menos de 100 y 200 eq/(ha año), respectivamente,

para distancias mayores a 1 km de ese PMI.

Los resultados se presentan en la Tabla 5-29, donde se comparan con respecto a un valor de


referencia de 1000 eq/(ha año).

10 Equivalente es la cantidad de masa de una especie química que reacciona con 1 g de hidrógeno en fase
acuosa. Por ejemplo, el peso molecular del sulfato es 96, y como el sulfato podría reaccionar en fase acuosa
con dos protones para generar ácido sulfúrico, su equivalente es 96/2=48 g.

11 Fuente: Steven G. McNulty, Erika C. Cohen, Jennifer A. Moore Myers, Timothy J. Sullivan y Harbin Li.

Estimates of critical acid loads and exceedances for forest soils across the conterminous United States

Environmental Pollution 149 (2007) 281-292

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 130 de 147

Código V01: FI-A.03-DSA

**Tabla 5-29 Nivel de Azufre y Nitrógeno depositado en suelo considerando PMI y a 2 km del sitio, Escenarios 1 a 4.**

|Col1|Col2|Azufre (S)<br>depositado en<br>suelo en PMI|Azufre (S)<br>depositado en<br>suelo a 1 km de<br>PMI|Nitrógeno (N)<br>depositado en<br>suelo en PMI|Nitrógeno (N)<br>depositado en<br>suelo a 1 km de<br>PMI|
|---|---|---|---|---|---|
|**Escenario 1**|**Depósito anual**<br>**Eq/(ha-año)**|179|50|879|100|
|**Escenario 1**|**Porcentaje respecto de nivel de**<br>**referencia %**|17,9%|5%|88%|10%|
|**Escenario 2**|**Depósito anual**<br>**Eq/(ha-año)**|174|50|892|100|
|**Escenario 2**|**Porcentaje respecto de nivel de**<br>**referencia %**|17,4%|5%|89%|10%|
|**Escenario 3**|**Depósito anual**<br>**Eq/(ha-año)**|200|75|889|200|
|**Escenario 3**|**Porcentaje respecto de nivel de**<br>**referencia %**|20%|7,5%|89%|20%|
|**Escenario 4**|**Depósito anual**<br>**Eq/(ha-año)**|196|75|953|200|
|**Escenario 4**|**Porcentaje respecto de nivel de**<br>**referencia %**|20%|7,5%|95%|20%|

Se aprecia que los niveles de depositación ácida en los PMI están por debajo de las normas de
referencia, aún en el escenario 4 con mayores emisiones totales de todos los proyectos operativos

en la zona.

En las figuras 5-50 a 5-53 se muestran las curvas de nivel de las depositaciones anuales de azufre
para los escenarios 1 a 4, respectivamente. Los aportes están muy localizados y disminuyen
rápidamente con la distancia al respectivo PMI. A 1 km de cada PMI, el aporte se reduce
aproximadamente 3 veces, lo que en términos porcentuales son aportes menores al 8% del nivel
estimado de capacidad de neutralización del suelo.

En las figuras 5-54 a 5-57 se muestran los resultados para el caso de la depositación de nitrógeno
para los escenarios 1 al 4, respectivamente. El comportamiento espacial es similar al caso del azufre,
excepto que los valores cambian pero se mantienen aportes que son inferiores a la capacidad de
neutralización estimada para el suelo. A distancias mayores a 1 km del PMI, los aportes son menores

al 20% del valor de referencia considerado en el análisis.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 131 de 147

Código V01: FI-A.03-DSA

**Figura 5-54 Mapa de depositación anual de azufre (eq/[ha año]) para el escenario 1. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 132 de 147

Código V01: FI-A.03-DSA

**Figura 5-55 Mapa de depositación anual de azufre (eq/[ha año]), para el escenario 2. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 133 de 147

Código V01: FI-A.03-DSA

**Figura 5-56 Mapa de depositación anual de azufre (eq/[ha año]), para el escenario 3. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 134 de 147

Código V01: FI-A.03-DSA

**Figura 5-57 Mapa de depositación anual de azufre (eq/[ha año]), para el escenario 4. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto está**

**marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 135 de 147

Código V01: FI-A.03-DSA

**Figura 5-58 Mapa de depositación anual de nitrógeno (eq/[ha año]), para el escenario 1. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto**

**está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 136 de 147

Código V01: FI-A.03-DSA

**Figura 5-59 Mapa de depositación anual de nitrógeno (eq/[ha año]), para el escenario 2. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto**

**está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 137 de 147

Código V01: FI-A.03-DSA

**Figura 5-60 Mapa de depositación anual de nitrógeno (eq/[ha año]), para el escenario 3. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto**

**está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 138 de 147

Código V01: FI-A.03-DSA

**Figura 5-61 Mapa de depositación anual de nitrógeno (eq/[ha año]), para el escenario 4. La ciudad de Teno está delimitada por el polígono negro. El perímetro del proyecto**

**está marcado con una línea poligonal azul.**

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:** " **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-**
**PROCESAMIENTO EN CBB - PLANTA TENO** ". **, VII REGIÓN**

**Informe Final**

Página 139 de 147

Código V01: FI-A.03-DSA

**6.** **ANÁLISIS DE INCERTIDUMBRE DE LA MODELACIÓN.**

En esta sección presentamos una estimación de la incertidumbre de las estimaciones de impactos

en calidad del aire realizadas con el modelo CALPUFF, cuando se emplea la meteorología generada

con el modelo numérico de pronóstico WRF.

Para poder estimar que tan cercana está la modelación de la observación, analizamos el escenario

3, modelando todas las fuentes industriales actuales y comparándolas con el monitoreo ambiental

de la estación ENLASA, para el año 2018. Si las concentraciones simuladas por el modelo

subestimaran las concentraciones medidas, se concluiría que el modelo subestima y hay que

corregir los resultados de la modelación por un factor mayor a 1. Asimismo, si el modelo

sobrestimase las concentraciones observadas, habría que corregir esas concentraciones por un

factor menor a 1. La siguiente Tabla resume esas comparaciones.

**Tabla 6-1. Análisis de sensibilidad comparando los resultados de la modelación CALPUFF-WRF con los valores medidos**

**en estación ENLASA (**  **g/m** **[3]** **)**

|Parámetro|Norma de<br>calidad del aire<br>g/m3N|Nivel calidad del<br>aire<br>Medido 2018<br>g/m3N|Nivel calidad del<br>aire modelación<br>g/m3N|Factor Modelo /<br>Medición|
|---|---|---|---|---|
|**MP10 Anual**|50|30,0|1,1|27,9|
|**P. 98 MP10 24 h**|150|62|3,7|16,6|
|**MP2.5 Anual**|20|10,4|0,94|11,1|
|**P. 98 MP2.5 Diario**|50|46,1|3,2|14,4|
|**NO2 anual**|100|16,5|4,6|3,6|
|**P. 99 NO2 1h**|400|63,7|81,0|0,79|
|**NO2 1h máximo**|-|110,5|136|0,8|
|**SO2 anual**|80|4,2|2,11|2,0|
|**P. 99 SO2 24 h**|250|21,9|9,9|2,2|
|**P. 99 SO2 1h**|350|34,7|25,5|1,4|
|**P. 99,73 SO2 1h**|700|53,9|36,3|1,5|
|**SO2 1h máximo**|-|106|138|0,77|
|**P. 99 Máximo CO 1 h**|30000|700|152|4,61|
|**P.99 Máximo CO 8 h**|10000|588|60|9,8|
|**Máximo CO 1h**|-|1400|261|5,4|

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 140 de 147

Código V01: FI-A.03-DSA

De la tabla anterior, se observa que en el caso del MP 10 y MP 2,5 lo modelado es muy bajo respecto

de la medición. Esta situación es consistente, ya que las emisiones industriales provienen de

chimeneas, donde esas emisiones se dispersan bastante antes de llegar a nivel del suelo. Por otra

parte, se espera que el MP 10 tenga aportes provenientes de emisiones fugitivas tales como

suspensión de polvo del tráfico de la ruta J-25, erosión eólica, manejo de suelos agrícolas, además

de las fuentes en la zona Poblada de Teno, que están ubicadas viento arriba del monitor de calidad

del aire. Finalmente, hay una contribución basal regional que corresponde al mismo tipo de fuentes

recién listadas, solo que distribuidas en toda la cuenca de la zona Teno-Curicó-Molina.

Para el caso del CO, los valores modelados también están muy bajos respecto de la medición, lo

cual es coherente considerando otras fuentes de emisión como el tráfico por la ruta 5 Sur.

Para NO 2 se constata un valor modelado bajo respecto de la medición anual, lo cual es coherente

considerando otras fuentes de emisión, particularmente el tráfico en ruta 5 sur más fuentes viento

arriba a escala regional, ya que el NO 2 requiere tiempo para generarse por oxidación de las

emisiones de NO. Con respecto del nivel horario, el modelo simula el 125 % respecto del nivel

horario medido, tanto para el máximo horario como para el percentil 99 de máximas diarias.

Para el SO 2 se observa un valor modelado de 50 % respecto de la medición anual, lo cual refleja que

el modelo está subestimando, ya que no hay otras fuentes relevantes de SO 2 en la zona, no hay

megafuentes de SO 2 en la región del Maule y las emisiones no modeladas no son relevantes, debido

al bajísimo contenido de azufre en los combustibles del transporte, comercio y residencia

(incluyendo consumo de leña en invierno). El valor modelado del nivel diario percentil 99 es de un

45% respecto de lo observado, es decir, subestimación. Con respecto del nivel horario, el modelo

subestima respecto del nivel horario observado, tanto para el percentil 99 como para el percentil

99,73. La excepción es el máximo de 1h, donde el modelo sobrestima la observación en un 25%.

Los resultados de esta comparación se pueden aplicar con mayor confianza en el caso del SO 2, ya

que los otros contaminantes tienen más fuentes emisoras que contribuyen a las concentraciones

observadas. De esta manera, se va a usar un factor de 2 para corregir las concentraciones modeladas

anuales y diarias. Para los casos del percentil 99 y 99,73 de los valores horarios del SO 2, que son

eventos cuyo origen se puede atribuir exclusivamente a fuentes de chimenea como las que se han

modelado, se toma un factor de corrección de 1,4. Por otra parte, para simular de manera adecuada

las concentraciones horarias de CO, NO 2 y SO 2, el factor de 0,8 aplicado a las concentraciones

modeladas se desprende de la tabla anterior.

El resultado de esta corrección para el escenario 3 se presenta en la siguiente Tabla. Se aprecia que

las concentraciones modeladas corregidas se acercan bastante a las concentraciones observadas,

para el caso de corto plazo (valores horarios) y de aquellos contaminantes que tienen como fuentes

dominantes las fuentes puntuales modeladas, como es el caso del SO 2 y del NO 2 .

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 141 de 147

Código V01: FI-A.03-DSA

Para el caso de otros contaminantes donde hay otras fuentes dominantes, como el caso del CO y las

emisiones del transporte, el ratio observado/modelado es bastante mayor a 1.

**Tabla 6-2. Comparación de los resultados de la modelación CALPUFF-WRF (usando un factor de corrección) con los**

**valores medidos en estación ENLASA (**  **g/m** **[3]** **)**

|Parámetro|Norma de<br>calidad del aire<br>g/m3N|Nivel calidad del<br>aire<br>Medido<br>g/m3N|Nivel calidad del<br>aire modelación<br>g/m3N|Factor Modelo /<br>Medición|
|---|---|---|---|---|
|**MP10 Anual**|50|30|2,15|14,0|
|**P. 98 MP10 24 h**|150|62|7,5|8,3|
|**MP2.5 Anual**|20|10,5|1,89|5,6|
|**P. 98 MP2.5 Diario**|50|46,1|6,5|7,1|
|**NO2 anual**|100|16,7|9,1|1,8|
|**P. 99 NO2 1h**|400|89,5|82|1,1|
|**NO2 1h máximo**|-|110,5|110|1,0|
|**SO2 anual**|80|4,2|4,23|1,0|
|**P. 99 SO2 24 h**|250|21,9|19,9|1,1|
|**P. 99 SO2 1h**|350|34,7|35,7|1,0|
|**P. 99,73 SO2 1h**|700|53,9|50,8|1,1|
|**SO2 1h máximo**|-|106|106|1,0|
|**P. 99 Máximo CO 1 h**|30000|700|47|15,0|
|**P.99 Máximo CO 8 h**|10000|588|19|31,7|

En resumen, el resultado de este análisis nos indica que las concentraciones modeladas se deben

multiplicar por un factor que depende del periodo promedio de las concentraciones: 0,8, 1,4 y 2

para los casos horarios, percentiles horarios y diarios/anuales, respectivamente. Con esta corrección

se minimiza la incertidumbre del modelo de dispersión. Estas correcciones se han aplicado a todos

los escenarios modelados y ya presentados en la sección 5 de este Informe.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 142 de 147

Código V01: FI-A.03-DSA

**7.** **CONCLUSIONES**

Se ha realizado una modelación de las emisiones atmosféricas de la Planta Teno de Cementos Bío

Bío S.A. en adelante Planta Teno Cbb, tanto para sus emisiones actuales como para la fase de
operación del proyecto “APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN
Cbb PLANTA TENO”, Región del Maule, considerando también otras fuentes de emisión del sector,

analizando cuatro escenarios de emisiones:

|Escenario 1:|Emisiones actuales de la Planta Teno CBB. Se consideran 7 fuentes de emisión<br>según emisiones especificadas en Tabla 4-1 y<br>Tabla 4-3.|
|---|---|
|**Escenario 2:**|Emisiones de la Planta Teno CBB con la implementación del Proyecto<br>“APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB<br>PLANTA TENO”. En este caso, sólo se afecta la fuente 1, que corresponde al horno<br>clínker, para la cual se consideran las emisiones con proyecto indicadas en Tabla<br>4-1. Las demás fuentes de la planta Teno Cbb mantienen invariables sus niveles<br>operacionales y emisiones con la implementación del proyecto, las que se indican<br>en <br>Tabla 4-3Tabla 4-3. Los escenarios 1 y 2 permiten estimar los efectos solamente<br>atribuibles a las emisiones de la planta Teno CBB en la implementación del<br>Proyecto.|
|**Escenario 3:**|Emisiones actuales de la Planta Teno de CBB (Escenario 1, según emisiones<br>especificadas en Tabla 4-1 y Tabla 4-3) más las emisiones de la central térmica<br>Energía Latina (según RCA N°43/2008, 36 turbinas de generación eléctrica), según<br>su despacho eléctrico 2018 (informado por CDEC), las de la planta de paneles MDP<br>de Arauco (Fuente: Anexo de Informe de Modelación de Dispersión Atmosférica<br>de Contaminantes Planta de MDP Teno de Paneles Arauco, abril 2010 del proyecto<br>“Planta de Paneles MDP Teno”, aprobado mediante RCA N°191, del<br>01/Octubre/2010, especificadas en Tabla 4-4 y las de la Planta de Elaboración de<br>Alimento para Mascotas de Nestlé Chile S.A. (etapa 1). Este escenario, permite<br>contrastar los resultados de la modelación con los niveles de calidad del aire<br>medidos y así realizar un análisis de sensibilidad del modelo de dispersión,<br>reduciendo la incertidumbre en la modelación.|
|**Escenario 4:**|Emisiones de la Planta Teno de CBB con la implementación del Proyecto<br>“APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB<br>PLANTA TENO”, (Escenario 2) detalladas en Tabla 4-1 y Tabla 4-3 más las<br>emisiones de la central térmica Energía Latina y las de la planta de paneles MDP<br>de Arauco (mismas del escenario 3) y las de la planta de alimentos de mascotas<br>de Nestlé S.A. (etapa 2) indicadas en<br>Tabla 4-3 4-3. Además, se incluye la operación de 6 turbinas adicionales en la<br>central Teno de Energía Latina, según lo declarado en el Anexo F, Informe de<br>Modelación de Calidad del Aire presentado por Energía Latina S.A. en diciembre<br>de 2016, como parte de la Adenda al Proyecto “Central de Generación Eléctrica a<br>Gas Teno”, el cual fue aprobado según RCA N° 29 del 6 de abril de 2017, señaladas<br>en Tabla 4-3.|

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 143 de 147

Código V01: FI-A.03-DSA

Para cada uno de los escenarios arriba descritos, se modeló el aporte a las concentraciones
ambientales de MP 10, MP 2.5, SO 2, NO x, CO y Plomo, determinando los niveles de calidad del aire a
obtener. En primer lugar, se modeló la meteorología en la zona usando el modelo numérico de
pronóstico WRF. Posteriormente se aplicó CALPUFF para la modelación de las emisiones de los cinco

escenarios arriba mencionados.

La Tabla 7-1 resume los principales resultados obtenidos a partir de la modelación para el punto de
máximo impacto para la planta Teno de Cbb. Todos los PMI para MP y gases coinciden en el punto
de coordenadas UTM 304.470 m E y 6.140.362 m N (a 1,62 km al NE de Teno).

**Tabla 7-1 Concentraciones ambientales de MP** **10** **, MP** **2.5** **, NO** **2** **, SO** **2** **, CO y Pb**  **g/m3 en PMI y porcentajes según las**

**normas de calidad del aire**

|Parámetro|Norma de<br>calidad del<br>aire<br>g/m3N (1)|Nivel<br>actual<br>Calidad del<br>aire<br>g/m3N (2)|Porcentaje<br>c. aire<br>actual<br>c/r a<br>norma de<br>calidad|Aporte por<br>proyecto<br>Cbb<br>g/m3N<br>(3)|Aporte por<br>todos los<br>proyectos<br>g/m3N<br>(4)|Nivel c.<br>aire con<br>proyectos<br>g/m3N<br>(5)|Porcentaje<br>calidad<br>aire por<br>proyecto<br>CBB c/r a<br>norma<br>calidad<br>aire|Porcentaje<br>c. aire con<br>proyectos<br>c/r a<br>norma de<br>calidad|
|---|---|---|---|---|---|---|---|---|
|MP10 Anual|50|33,8|68%|0,4|0,7|34,5|68%|69%|
|MP10 P98 Diario|150|69,7|46%|0,5|3,0|72,7|47%|48%|
|MP2.5 Anual|20|7,5|38%|0,2|0,5|8,0|39%|40%|
|MP2.5 P98 Diario|50|24|48%|0,3|2,0|26,0|49%|52%|
|SO2 Anual|60|6,3|11%|-0,2|-0,2|6,1|10%|10%|
|SO2 P99 Diario (6)|150|38,3|26%|-0,8|-0,3|38,0|25%|25%|
|SO2 P99 Horario|350|64,1|18%|-1,8|-1,5|62,6|18%|18%|
|SO2 P99,73<br>Horario (7)|700|105,1|15%|-2,4|-0,7|104,5|15%|15%|
|NO2 Anual|100|18,7|19%|0,5|3,1|21,8|19%|22%|
|NO2 P.99 Horario|400|67|17%|3,2|7,1|74,1|18%|19%|
|CO P99 Horario|30,000|1000|3%|5,4|0,2|1000,2|3%|3%|
|CO P99 8 horas|10,000|700|7%|2,4|1,0|701,0|7%|7%|
|Pb Anual|0,5|S/i||0,003|0,003|||S/i|

(1) Las normativas primarias de calidad del aire utilizadas son D.S N°12/2010 para MP2,5, D.S

N°59/1998 para MP10, D.S N°104/2018 para SO 2, D.S N°114/2002 para NO 2, D.S N°115/2002 para
CO, D.S N°136/2000 para Pb y D.S N°22/2009 para norma secundaria horario de SO 2 .
(2) Valor medido en estación de monitoreo de calidad del aire ENLASA
(3) Corresponde a la resta: del valor modelado con Proyecto al valor modelado en situación actual:

Escenario 2 - Escenario 1.

(4) Corresponde a la resta de Escenario 4 - Escenario 3. En este caso, se consideran los efectos del

proyecto más los otros proyectos no materializados.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 144 de 147

Código V01: FI-A.03-DSA

(5) Al nivel actual se suma el aporte de todos los proyectos, que es el máximo entre (3) y (4).
(6) No se evalúa norma secundaria SO 2 P99,7 Diario de 260 ug/m3N, ya que es menos estricta que la

norma primaria.
(7) SO 2 P99,73 Horario, corresponde a la norma secundaria.

El análisis también se realizó en la estación ENLASA y en cinco receptores en la ciudad de Teno. En
estos receptores se verificó que las concentraciones proyectadas son siempre menores a las del
punto de máximo impacto. Para el caso de ENLASA, también los resultados son más altos que en los
receptores de la ciudad de Teno y más bajos que en el PMI. La Tabla 7-2 presenta resultados de la
modelación para la estación ENLASA.

**Tabla 7-2 Concentraciones ambientales de MP** **10** **, MP** **2.5** **, NO** **2** **, SO** **2** **, CO y Pb en Estación de Calidad del Aire ENLASA y**

**porcentajes según niveles de calidad del aire normados**

|Parámetro|Norma de<br>calidad del<br>aire<br>g/m3N (1)|Nivel<br>actual<br>Calidad del<br>aire<br>g/m3N (2)|Aporte<br>por<br>proyecto<br>Cbb (3)|Aporte<br>por todos<br>los<br>proyectos<br>(4)|Nivel<br>actual<br>mas<br>proyectos<br>(5)|Porcentaj<br>e c. aire<br>actual<br>c/r a<br>norma de<br>calidad|Porcentaj<br>e<br>respecto<br>a norma<br>de<br>calidad|
|---|---|---|---|---|---|---|---|
|MP10 Anual|50|33,8|0,2|0,3|34,1|68%|68%|
|MP10 P98 Diario|150|69,7|0,7|1,2|70,9|46%|47%|
|MP2.5 Anual|20|7,5|0,1|0,2|7,7|38%|39%|
|MP2.5 P98 Diario|50|24|0,3|0,9|24,9|48%|50%|
|SO2 Anual|60|6,3|-0,1|-0,1|6,2|11%|10%|
|SO2 P99 Diario (6)|150|38,3|-0,6|-0,6|37,7|26%|25%|
|SO2 P99 Horario|350|64,1|-1,1|-1,1|63,0|18%|18%|
|SO2 P99,73<br>Horario (7)|700|105,1|-1,3|-1,6|103,5|15%|15%|
|NO2 Anual|100|18,7|0,3|0,8|19,5|19%|19%|
|NO2 P.99 Horario|400|67|2,9|5,5|72,5|17%|18%|
|CO P99 Horario|30,000|1000|4,3|36,3|1036,3|3%|3%|
|CO P99 8 horas|10,000|700|1,7|25,8|725,8|7%|7%|
|Pb Anual|0,5|S/i|0,0014|0,0014||||

Ambas Tablas indican que la implementación del Proyecto no va a alterar la calidad del aire en la
zona de Teno, ya que todos los contaminantes se van a mantener por debajo de la condición de
latencia. Por ejemplo, el MP 10 se va a mantener bajo el 70% y 50% de la norma anual y diaria,
respectivamente, en los escenarios 2 y 4 con proyecto Cbb operativo. Para el MP 2,5 los respectivos

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 145 de 147

Código V01: FI-A.03-DSA

porcentajes son 40% y 50%, respectivamente. Para el resto de los contaminantes, las
concentraciones proyectadas están bajo el 50% de las respectivas normas de calidad.

En el caso de la **zona urbana de Teno**, las Tablas de resultados para los receptores discretos y los
gráficos que muestran toda la distribución espacial de los contaminantes modelados indican que la
implementación del Proyecto aportará:

a) Menos de 1 g/m [3] y de 4 g/m [3] para el MP 10 anual y percentil 98 diario, respectivamente

b) Menos de 1 g/m [3] y de 4 g/m [3] para el MP 2,5 anual y percentil 98 diario, respectivamente

c) Menos de 0,5 g/m [3], 3,5 g/m [3] y 6 g/m [3] para el SO 2 anual, percentil 99 diario y horario,

respectivamente

d) Menos de 1 g/m [3] y 60 g/m [3] para el NO 2 anual y percentil 99 horario, respectivamente

e) Menos de 20 g/m [3] y 4 g/m [3] para el CO percentil 99 de 1h y 8h, respectivamente

En la condición más pesimista (caso del **PMI** Planta Teno de Cbb), se encuentra que:

`o` Respecto del **MP** **10**, la concentración anual subiría 0,75 g/m [3] (de los cuales solo 0,38 g/m [3] son

atribuibles a la implementación del Proyecto Cbb), llegando a un 69% de la norma anual. Para

la norma diaria, la concentración subiría 3 g/m [3] (de los cuales solo 0,5 g/m [3] son atribuibles a

la implementación del Proyecto Cbb), llegando a un 48% de la norma.

`o` Respecto del **MP** **2,5**, la concentración anual subiría 0,5 g/m [3] (de los cuales solo 0,2 g/m [3] son

atribuibles a la implementación del Proyecto Cbb), llegando a un 40% de la norma anual. Para

la norma diaria, la concentración subiría 2 g/m [3] (de los cuales solo 0,3 g/m [3] son atribuibles a

la implementación del Proyecto Cbb), llegando a un 52% de la norma.

`o` Respecto de **NO** **2**, la concentración anual subiría 3,14 g/m [3] (de los cuales solo 0,5 g/m [3] son

atribuibles a la implementación del Proyecto Cbb), llegando a un 22% de la norma anual. Para

la norma horaria (percentil 99), la concentración subiría 7,1 g/m [3] (de los cuales solo 3,2 g/m [3]

son atribuibles a la implementación del Proyecto Cbb), llegando a un 19% de la norma.

`o` Respecto del **SO** **2**, la concentración anual se reduciría en 0,22 g/m [3] (reducción de 0,2 g/m [3]

atribuibles a la implementación del Proyecto Cbb), llegando a un 10% de la norma anual. Para

la norma diaria (percentil 99), la concentración se reduciría en 0,3 g/m [3] (reducción de 0,8
g/m [3] atribuibles a la implementación del Proyecto Cbb), llegando a un 25% de la norma. Para
la norma horaria (percentil 99), la concentración se reduciría en 1,5 g/m [3] (reducción de 1,8
g/m [3] atribuibles a la implementación del Proyecto Cbb), llegando a un 18% de la norma.
`o` Respecto del **CO**, la concentración de 1h (percentil 99) subiría 5 g/m [3] (todos atribuibles a la

implementación del Proyecto Cbb), llegando a un 3% de la norma anual. Para la concentración

de 8h (percentil 99), la concentración subiría 2 g/m [3] (de los cuales 1 g/m [3] son atribuibles a

la implementación del Proyecto de Cbb), llegando a un 7% de la norma.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 146 de 147

Código V01: FI-A.03-DSA

`o` Respecto del **Plomo**, único metal pesado con norma de calidad del aire, no se dispone de

mediciones de calidad del aire, sin embargo, en el PMI se puede señalar que los niveles de

emisión del proyecto estarían en el orden del 0,5 % de la norma de calidad del aire para este

contaminante. El PMI es distinto al caso de MP y gases, ubicándose en el punto de coordenadas

305.431 m E y 6.141.387 m N (a 3,7 km al NE de Teno, ver Figura 5-3).

`o` Respecto del **Azufre** depositado en el suelo, se determinó que en el punto de máximo impacto

la depositación estaba por debajo del 20 % del nivel de referencia y a 1 km del PMI, los valores

de depositación se reducen al 8 % del nivel de referencia o menos. A más de 1 km del PMI, los

aportes son marginales. El PMI es el mismo que en el caso de MP y gases (UTM 304.470 m E y

6.140.362 m N).

En resumen, la implementación del Proyecto “APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE COPROCESAMIENTO EN Cbb PLANTA TENO”, Región del Maule, no va a modificar el estado de la calidad
del aire en la zona de Teno, ya que todos los contaminantes normados se mantendrán bajo la
condición de latencia (la mayoría bajo el 50% del valor de la respectiva norma de calidad del aire),
tanto con la implementación del Proyecto como en el caso que los otros proyectos ambientalmente
aprobados se implementen en la zona.

**MODELACIÓN DE DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS DEL PROYECTO:**
" **APLICACIÓN DE ECONOMÍA CIRCULAR MEDIANTE CO-PROCESAMIENTO EN CBB - PLANTA**
**TENO** ". **, VII REGIÓN**

**Informe Final**

Página 147 de 147

Código V01: FI-A.03-DSA

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1-1: Concentraciones ambientales de MP** **10** **, MP** **2.5** **, NO** **2** **, SO** **2** **, CO y Pb en PMI y porcentajes según niveles de****

| Parámetro | Norma de<br>calidad del<br>aire<br>g/m3N (1) | Nivel<br>actual<br>Calidad del<br>aire<br>g/m3N (2) | Porcentaje<br>c. aire<br>actual<br>c/r a<br>norma de<br>calidad | Aporte por<br>proyecto<br>CBB<br>g/m3N<br>(3) | Aporte por<br>todos los<br>proyectos<br>g/m3N<br>(4) | Nivel c.<br>aire con<br>proyectos<br>g/m3N<br>(5) | Porcentaje<br>calidad<br>aire por<br>proyecto<br>CBB c/r a<br>norma<br>calidad<br>aire | Porcentaje<br>c. aire con<br>proyectos<br>c/r a<br>norma de<br>calidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 Anual | 50 | 33,8 | 68% | 0,4 | 0,7 | 34,5 | 68% | 69% |
| MP10 P98 Diario | 150 | 69,7 | 46% | 0,5 | 3,0 | 72,7 | 47% | 48% |
| MP2.5 Anual | 20 | 7,5 | 38% | 0,2 | 0,5 | 8,0 | 39% | 40% |
| MP2.5 P98 Diario | 50 | 24 | 48% | 0,3 | 2,0 | 26,0 | 49% | 52% |
| SO2 Anual | 60 | 6,3 | 11% | -0,2 | -0,2 | 6,1 | 10% | 10% |
| SO2 P99 Diario (6) | 150 | 38,3 | 26% | -0,8 | -0,3 | 38,0 | 25% | 25% |
| SO2 P99 Horario | 350 | 64,1 | 18% | -1,8 | -1,5 | 62,6 | 18% | 18% |
| SO2 P99,73<br>Horario (7) | 700 | 105,1 | 15% | -2,4 | -0,7 | 104,5 | 15% | 15% |
| NO2 Anual | 100 | 18,7 | 19% | 0,5 | 3,1 | 21,8 | 19% | 22% |
| NO2 P.99 Horario | 400 | 67 | 17% | 3,2 | 7,1 | 74,1 | 18% | 19% |
| CO P99 Horario | 30,000 | 1000 | 3% | 5,4 | 0,2 | 1000,2 | 3% | 3% |
| CO P99 8 horas | 10,000 | 700 | 7% | 2,4 | 1,0 | 701,0 | 7% | 7% |
| Pb Anual | 0,5 | S/i |  | 0,003 | 0,003 |  |  | S/i |

**Tabla 1-2.: Ubicación receptores discretos (UTM, huso 19 H, WGS84)****

| Código | Receptor | UTM E [m] | UTM N [m] |
| --- | --- | --- | --- |
| R_1 | Estación ENLASA(1) | 305.205 | 6.140.221 |
| R_2 | Teno Norte | 302.574 | 6.139.767 |
| R_3 | Estación FFCC Teno | 302.668 | 6.139.114 |
| R_4 | Teno SE | 302.714 | 6.138.326 |
| R_5 | Teno Sur | 302.094 | 6.138.431 |
| R_6 | Teno Oeste | 301.377 | 6.139.114 |

**Tabla 1-3: Concentraciones ambientales de MP** **10** **, MP** **2.5** **, NO** **2** **, SO** **2** **, CO y Pb en Estación de Calidad del Aire ENLASA y****

| Parámetro | Norma de<br>calidad del<br>aire<br>g/m3N (1) | Nivel<br>actual<br>Calidad del<br>aire<br>g/m3N (2) | Aporte<br>por<br>proyecto<br>CBB (3) | Aporte<br>por todos<br>los<br>proyectos<br>(4) | Nivel<br>actual<br>mas<br>proyectos<br>(5) | Porcentaj<br>e c. aire<br>actual<br>c/r a<br>norma de<br>calidad | Porcentaj<br>e<br>respecto<br>a norma<br>de<br>calidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 Anual | 50 | 33,8 | 0,2 | 0,3 | 34,1 | 68% | 68% |
| MP10 P98 Diario | 150 | 69,7 | 0,7 | 1,2 | 70,9 | 46% | 47% |
| MP2.5 Anual | 20 | 7,5 | 0,1 | 0,2 | 7,7 | 38% | 39% |
| MP2.5 P98 Diario | 50 | 24 | 0,3 | 0,9 | 24,9 | 48% | 50% |
| SO2 Anual | 60 | 6,3 | -0,1 | -0,1 | 6,2 | 11% | 10% |
| SO2 P99 Diario (6) | 150 | 38,3 | -0,6 | -0,6 | 37,7 | 26% | 25% |
| SO2 P99 Horario | 350 | 64,1 | -1,1 | -1,1 | 63,0 | 18% | 18% |
| SO2 P99,73<br>Horario (7) | 700 | 105,1 | -1,3 | -1,6 | 103,5 | 15% | 15% |
| NO2 Anual | 100 | 18,7 | 0,3 | 0,8 | 19,5 | 19% | 19% |
| NO2 P.99 Horario | 400 | 67 | 2,9 | 5,5 | 72,5 | 17% | 18% |
| CO P99 Horario | 30,000 | 1000 | 4,3 | 36,3 | 1036,3 | 3% | 3% |
| CO P99 8 horas | 10,000 | 700 | 1,7 | 25,8 | 725,8 | 7% | 7% |
| Pb Anual | 0,5 | S/i | 0,0014 | 0,0014 |  |  |  |

**Tabla 3-1: Línea base de calidad del aire en estación ENLASA****

| Parámetro | Norma de<br>calidad del aire<br>g/m3N | Nivel actual<br>Calidad del aire<br>2016<br>g/m3N | Nivel actual<br>Calidad del aire<br>2017<br>g/m3N | Nivel actual<br>Calidad del aire<br>2018<br>g/m3N | Promedio Trianual<br>2016-2018<br>Calidad del aire<br>2018<br>g/m3N |
| --- | --- | --- | --- | --- | --- |
| MP10 Anual | 50 | 38,0 | 33,4 | 30,0 | 33,8 |
| MP10 P98 Diario | 150 | 74 | 73 | 62 | 69,7 |
| MP2.5 Anual | 20 | 6,1 | 5,8 | 10,5 | 7,5 |
| MP2.5 P98 Diario | 50 | 12,1 | 13,7 | 46,1 | 24,0 |
| SO2 Anual | 60 | 9,7 | 5,1 | 4,2 | 6,3 |
| SO2 P99 Diario | 150 | 60,4 | 32,5 | 21,9 | 38,3 |
| SO2 P99 Horario | 350 | 169,7 | 60,5 | 34,7 | 88,3 |
| SO2 P99,73 Horario | 700 | 97,1 | 91,7 | 53,9 | 80,9 |
| NO2 Anual | 100 | 19,9 | 19,4 | 16,7 | 18,7 |
| NO2 P.99 Horario | 400 | 70,3 | 67,0 | 63,7 | 67,0 |
| CO P99 Horario | 30.000 | 600 | 600 | 700 | 667 |
| CO P99 8 horas | 10.000 | 500 | 588 | 588 | 559 |

**Tabla 3-2.: Estadísticas de desempeño del modelo WRF para el viento año 2018.****

| Indicador | año | verano | otoño | invierno | primavera |
| --- | --- | --- | --- | --- | --- |
| n | 8750 | 2159 | 2208 | 2199 | 2184 |
| FAC2 | 0,74 | 0,74 | 0,73 | 0,73 | 0,76 |
| MB | 0,43 | 0,44 | 0,43 | 0,36 | 0,50 |
| MGE | 0,73 | 0,75 | 0,72 | 0,70 | 0,73 |
| NMB | 0,30 | 0,29 | 0,31 | 0,27 | 0,34 |
| NMGE | 0,51 | 0,50 | 0,52 | 0,53 | 0,49 |
| RMSE | 0,97 | 0,96 | 0,96 | 1,00 | 0,95 |
| r | 0,51 | 0,56 | 0,50 | 0,48 | 0,49 |

**Tabla 3-3.: Estadísticas de desempeño del modelo WRF para temperatura año 2018.****

| Indicador | año | verano | otoño | invierno | primavera |
| --- | --- | --- | --- | --- | --- |
| n | 8750 | 2184 | 2159 | 2208 | 2199 |
| FAC2 | 0,91 | 0,97 | 1,00 | 0,93 | 0,74 |
| MB | 2,58 | 1,67 | 2,42 | 2,96 | 3,27 |
| MGE | 3,32 | 2,60 | 3,59 | 3,44 | 3,64 |
| NMB | 0,19 | 0,12 | 0,12 | 0,22 | 0,45 |
| NMGE | 0,24 | 0,19 | 0,18 | 0,26 | 0,50 |
| RMSE | 4,33 | 3,47 | 4,61 | 4,51 | 4,62 |
| r | 0,87 | 0,84 | 0,79 | 0,81 | 0,69 |

**Tabla 4-1.: Emisiones de Fuente 1: Chimenea N° 1 Horno Clinker condición actual y la más desfavorable con proyecto****

| Parámetro | Condición de<br>operación<br>actual (1) | Condición de<br>mayor emisión<br>posible con<br>proyecto (2) | Consideraciones |
| --- | --- | --- | --- |
| Caudal Nm3/h | 216.201 | 240.000 | El caudal de valor actual se determina según medición de<br>gases del 09 de octubre 2013.<br>El caudal de valor con proyecto, considera un aumento del<br>11% por uso de CAS, lo que implica un consumo mayor por<br>menor PCI. |
| MP2,5<br>mg/Nm3 | 5,84 | 12,0 | Se considera que el 40% de MP corresponde a la parte<br>filtrable del MP 2,5, y el 76% de MP corresponde a MP10, de<br>acuerdo a referencia Factores de emisión USEPA AP 42,<br>capítulo 11.6, tabla 11.6-6, distribución de tamaño de<br>partícula en horno de clinker de cemento portland.<br>Para el nivel de emisión actual de MP, se consideró medición<br>del 2 de marzo de 2017.<br>Para la emisión con proyecto, se consideró nivel de emisión<br>de MP de 30 mg/m3N, inferior a nivel norma de 50 mg/m3N,<br>considerando para los niveles de MP2,5 y MP10 los mismos<br>porcentajes ya indicados (40% para MP2,5 y 76% para MP10<br>respecto del MP). |
| MP2,5 g/s | 0,35 | 0,80 | 0,80 |
| MP2,5 t/año | 11,1 | 25,2 | 25,2 |
| MP10 mg/Nm3 | 11,1 | 22,8 | 22,8 |
| MP10 g/s | 0,67 | 1,52 | 1,52 |
| MP10 t/año | 21,0 | 47,9 | 47,9 |
| SO2 mg/Nm3 | 232,5 | 225 | La concentración del valor actual se determina según<br>medición de gases del 09 de octubre 2013.<br>Valor con proyecto de 15 g/s, se determina como condición<br>máxima de operación del Proyecto. Cabe señalar que este<br>valos es un 32% del valor máximo del SO2, de 48 g/s<br>establecido en la RCA 239/2002. |
| SO2 g/s | 15,5 | 15,0 | 15,0 |
| SO2 t/año | 488,8 | 473,0 | 473,0 |
| NOx mg/Nm3 | 1.320 | 1.250 | La concentración del valor actual se determina según<br>medición de gases del 09 de octubre 2013.<br>Valor con proyecto considera mantener valor indicado en<br>RCA 239/2002, el cual es de 300 kg/h de NOx. |
| NOx g/s | 79,3 | 83,3 | 83,3 |
| NOx kg/h | 285,4 | 300 | 300 |
| NOx t/año | 2500 | 2628 | 2628 |
| CO mg/Nm3 | 231,61 | 231,61 | La concentración del valor actual se determina según<br>medición de CO del 29 enero 2016.<br>Para valor con proyecto se asume la misma concentración. |
| CO g/s | 13,9 | 15,4 | 15,4 |
| CO t/año | 438,7 | 486,9 | 486,9 |
| Plomo<br>mg/Nm3 | 0,0115 | 0,1 | Valor actual corresponde a medición más alta del 10 y 12 de<br>febrero 2016.<br>El valor con proyecto corresponde al 10% del nivel de la<br>norma, establecida en DS 29/2013 - norma de emisión para |
| Plomo g/s | 0,001 | 0,007 | 0,007 |
| Plomo t/año | 0,022 | 0,21 | 0,21 |

**Tabla 4-2.: Parámetros de las emisiones de la chimenea N°1 del horno Clinker.****

| Parámetro | Unidad | Valor |
| --- | --- | --- |
| Coordenadas chimenea WGS84 H19 | m | E: 304323<br>N: 6139736 |
| Altura chimenea | m | 80 |
| Diámetro chimenea | m | 2,5 |
| Velocidad salida de los gases | m/s | 16 |
| Temperatura aprox. de salida de los gases | °C | 115 |

**Tabla 4-3.: Características de las emisiones de las demás fuentes oficiales de Planta CBB que mantienen sus emisiones****

| Parámetro / Unidad | Chimenea<br>N°2,<br>Enfriador<br>Clinker. | Chimenea<br>N°3, molino<br>cemento 1. | Chimenea<br>N°4,<br>enfriador de<br>molino<br>cemento 1. | Chimenea<br>N°5, molino<br>de cemento<br>2. | Chimenea<br>N°6,<br>Generador<br>N°1 | Chimenea<br>N°7,<br>Generador<br>N°2 |
| --- | --- | --- | --- | --- | --- | --- |
| Altura chimenea (m) | 52 | 28 | 37,7 | 35 | 18 | 18 |
| Diámetro interno de<br>la chimenea (m) | 2,6 | 2,0 | 1,6 | 2,0 | 2,0 | 2,0 |
| Velocidad de salida<br>de gases(m/s) | 12 | 12 | 17 | 7 | 7 | 7 |
| Temperatura de<br>salida de gases(°K) | 468,15 | 356,15 | 349,15 | 365,55 | 365,55 | 365,55 |
| Temperatura<br>Ambiente<br>Promedio(°K) | 298,15 | 298,15 | 298,15 | 298,15 | 298,15 | 298,15 |
| Caudal Volumétrico<br>Real Gases Chimenea<br>(m3N/h) | 78.840 | 100.255 | 59.633 | 79.372 | 41.797 | 43.841 |
| Ubicación (UTM,<br>Datum WGS 84) m | 304350 E<br>6139753 N | 304427 E<br>6139668 N | 304421 E<br>6139666 N | 304388 E<br>6139554 N | 304091 E<br>6139621 N | 304110 E<br>6139627 N |
| Fecha medición<br>caudal y MP | 4 sept 2018 | 17 mayo<br>2017 | 12 de sept<br>2018 | 18 abril<br>2017 | 21 dic 2016 | 26 abril<br>2016 |
| MP10 (mg/m3N) | 8,9 | 17,7 | 9,56 | 9,54 | 89,31 | 108,24 |
| MP10 (g/s) | 0,195 | 0,49 | 0,16 | 0,21 | 1,04 | 1,32 |
| Fecha medición NOx<br>y SO2 | 14 sept<br>2016 | 13 sept<br>2016 | - | 1 julio 2016 | 28 feb<br>2018 | 28 abril<br>2016 |
| NOx (mg/m3N) | 0,95 | 8,25 | - | 2,53 | 1.228,4 | 1.238,3 |
| NOx (g/s) | 0,021 | 0,23 | - | 0,06 | 14,3 | 15,08 |
| SOx (mg/m3N) | 1,46 | 2,14 | - | 0,89 | 70,2 | 35,7 |
| SOx (g/s) | 0,032 | 0,06 | - | 0,02 | 0,82 | 0,43 |

**Tabla 4-4.: Emisiones Base de la Central Térmica ENLASA y de Planta de Paneles MDP Arauco****

| Parámetro /<br>Unidad | ENLASA<br>(1)<br>Chimenea<br>s D-1 a D-<br>36 | MDP (2)<br>Aspira-<br>ción<br>Viruta<br>C900 | MDP (2)<br>Aspira-<br>ción<br>Lamina<br>do | MDP (2)<br>Aspira-<br>ción<br>impreg-<br>nación | MDP (2)<br>Transp.<br>N. Q600 | MDP (2)<br>Transp.<br>N. Q500 | MDP (2)<br>WESP<br>E300 | MDP (2)<br>Batería<br>Filtros | MDP (2)<br>Transp.<br>N. F900 | MDP (2)<br>Transp.<br>N. J800 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Altura de<br>chimenea (m) | 6,9 | 8 | 8 | 8 | 8 | 8 | 25 | 10 | 8 | 8 |
| Diámetro<br>interno de la<br>chimenea (m) | 2,0 | 0,75 | 0,9 | 0,7 | 0,35 | 0,65 | 2,5 | 1,8 | 0,7 | 0,7 |
| Velocidad de<br>salida de<br>gases(m/s) | 13,2 | 20,82 | 23,41 | 20,0 | 15,59 | 18,68 | 13,81 | 24,24 | 20,0 | 20,0 |
| Temperatura<br>de salida de<br>gases(°K) | 358 | 293 | 293 | 303 | 303 | 303 | 333 | 303 | 303 | 303 |
| Ubicación<br>(UTM, Datum<br>WGS 84, Huso<br>19) | 315962 E<br>6139787<br>N | 309242<br>E <br>614059<br>N | 309175<br>E <br>614068<br>N | 309160<br>E <br>614076<br>N | 309254<br>E <br>614065<br>N | 309254<br>E <br>614066<br>N | 309254<br>E <br>614065<br>N | 309164<br>E <br>614065<br>N | 309210<br>E <br>614060<br>N | 309190<br>E <br>614061<br>N |
| MP10 (g/s) | 0,28 | 0,86 | 0,28 | 0,03 | 0,03 | 0,11 | 2,78 | 1,11 | 0,14 | 0,14 |
| MP2,5 (g/s) | 0,28 | 0,86 | 0,28 | 0,03 | 0,03 | 0,11 | 2,78 | 1,11 | 0,14 | 0,14 |
| NOx (g/s) | 1,33 | - | - | - | - | - | 13,89 | - | - | - |
| SOx (g/s) | 1,22 | - | - | - | - | - | 0,56 | - | - | - |
| CO (g/s) | 2,33 | - | - | - | - | - | - | - | - | - |

**Tabla 4-5.: Emisiones del proyecto Central Térmica ENLASA, 6 turbinas adicionales.****

| Parámetro / Unidad | ENLASA<br>Turbina<br>GNL-1 | ENLASA<br>Turbina<br>GNL-2 | ENLASA<br>Turbina<br>GNL-3 | ENLASA<br>Turbina<br>GNL-4 | ENLASA<br>Turbina<br>GNL-5 | ENLASA<br>Turbina<br>GNL-6 |
| --- | --- | --- | --- | --- | --- | --- |
| Altura de chimenea<br>(m) | 27,5 | 27,5 | 27,5 | 27,5 | 27,5 | 27,5 |
| Diámetro interno de<br>la chimenea (m) | 1,2 | 1,2 | 1,2 | 1,2 | 1,2 | 1,2 |
| Velocidad de salida<br>de gases(m/s) | 28,12 | 28,12 | 28,12 | 28,12 | 28,12 | 28,12 |
| Temperatura de<br>salida de gases(°K) | 673 | 673 | 673 | 673 | 673 | 673 |
| Ubicación (UTM,<br>Datum WGS 84,<br>Huso 19) | 304027 E<br>6139549 N | 304025 E<br>6139547 N | 304023 E<br>6139545 N | 304029 E<br>6139547 N | 304027 E<br>6139545 N | 304026 E<br>6139543 N |
| MP10 (g/s) | 0,18 | 0,18 | 0,18 | 0,18 | 0,18 | 0,18 |
| MP2,5 (g/s) | 0,18 | 0,18 | 0,18 | 0,18 | 0,18 | 0,18 |
| NOx (g/s) | 3,4 | 3,4 | 3,4 | 3,4 | 3,4 | 3,4 |
| CO (g/s) | 5,75 | 5,75 | 5,75 | 5,75 | 5,75 | 5,75 |

**Tabla 5-1.: Ubicación receptores discretos (UTM, Huso 19 H, WGS84)****

| Código | Receptor | UTM E [m] | UTM N [m] |
| --- | --- | --- | --- |
| R_1 | Estación ENLASA(1) | 305.205 | 6.140.221 |
| R_2 | Teno Norte | 302.574 | 6.139.767 |
| R_3 | Estación FFCC Teno | 302.668 | 6.139.114 |
| R_4 | Teno SE | 302.714 | 6.138.326 |
| R_5 | Teno Sur | 302.094 | 6.138.431 |
| R_6 | Teno Oeste | 301.377 | 6.139.114 |

**Tabla 5-2: Localización del PMI (UTM, WGS 84)** **y sus aportes en escenarios 1 a 4 para cada contaminante en análisis.****

| Parámetr<br>o | E [m] | N [m] | Escenario 1<br>g/m3N | Escenario 2<br>g/m3N | Escenario 3<br>g/m3N | Escenario 4<br>g/m3N |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 <br>Anual | 304.470 | 6.140.362 | 10,9 | 11,3 | 11,5 | 12,25 |
| MP10 P98<br>Diario | 304.470 | 6.140.362 | 24,7 | 25,1 | 26,8 | 29,7 |
| MP2.5 <br>Anual | 304.470 | 6.140.362 | 9,79 | 10,0 | 10,35 | 10,9 |
| MP2.5 P98<br>Diario | 304.470 | 6.140.362 | 22,2 | 22,4 | 25,1 | 27,1 |
| NO2 Anual | 304.470 | 6.140.362 | 10,1 | 9,91 | 11,87 | 11,67 |
| NO2 P.99<br>1h | 304.470 | 6.140.362 | 28,8 | 28,0 | 58,0 | 58 |
| SO2 Anual | 304.470 | 6.140.362 | 56,6 | 54,8 | 74,6 | 73,1 |
| SO2 P99<br>Diario | 304.470 | 6.140.362 | 78,1 | 75,7 | 140,9 | 140,3 |
| SO2 P99<br>1h | 304.470 | 6.140.362 | 44,7 | 45,2 | 45,3 | 48,5 |
| SO2 <br>P99,73 1h<br>(1) | 304.470 | 6.140.362 | 121 | 124 | 132 | 139 |
| CO P99 1h | 304.470 | 6.140.362 | 50 | 56 | 195 | 195 |
| CO P99 8h | 304.470 | 6.140.362 | 22 | 25 | 95 | 96 |
| Pb Anual | 305.431 | 6.142.387 | 0,00045 | 0,00313 | 0,00045 | 0,00313 |

**Tabla 5-3: Concentraciones ambientales de MP** **10** **, MP** **2.5** **, NO** **2** **, SO** **2** **, CO y Pb en PMI y porcentajes según niveles de****

| Parámetro | Norma de<br>calidad del<br>aire<br>g/m3N (1) | Nivel<br>actual<br>Calidad del<br>aire<br>g/m3N (2) | Porcentaje<br>c. aire<br>actual<br>c/r a<br>norma de<br>calidad | Aporte por<br>proyecto<br>CBB<br>g/m3N<br>(3) | Aporte por<br>todos los<br>proyectos<br>g/m3N<br>(4) | Nivel c.<br>aire con<br>proyectos<br>g/m3N<br>(5) | Porcentaje<br>calidad<br>aire por<br>proyecto<br>CBB c/r a<br>norma<br>calidad<br>aire | Porcentaje<br>c. aire con<br>proyectos<br>c/r a<br>norma de<br>calidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 Anual | 50 | 33,8 | 68% | 0,4 | 0,7 | 34,5 | 68% | 69% |
| MP10 P98 Diario | 150 | 69,7 | 46% | 0,5 | 3,0 | 72,7 | 47% | 48% |
| MP2.5 Anual | 20 | 7,5 | 38% | 0,2 | 0,5 | 8,0 | 39% | 40% |
| MP2.5 P98 Diario | 50 | 24 | 48% | 0,3 | 2,0 | 26,0 | 49% | 52% |
| SO2 Anual | 60 | 6,3 | 11% | -0,2 | -0,2 | 6,1 | 10% | 10% |
| SO2 P99 Diario (6) | 150 | 38,3 | 26% | -0,8 | -0,3 | 38,0 | 25% | 25% |
| SO2 P99 Horario | 350 | 64,1 | 18% | -1,8 | -1,5 | 62,6 | 18% | 18% |
| SO2 P99,73<br>Horario (7) | 700 | 105,1 | 15% | -2,4 | -0,7 | 104,5 | 15% | 15% |
| NO2 Anual | 100 | 18,7 | 19% | 0,5 | 3,1 | 21,8 | 19% | 22% |
| NO2 P.99 Horario | 400 | 67 | 17% | 3,2 | 7,1 | 74,1 | 18% | 19% |
| CO P99 Horario | 30,000 | 1000 | 3% | 5,4 | 0,2 | 1000,2 | 3% | 3% |
| CO P99 8 horas | 10,000 | 700 | 7% | 2,4 | 1,0 | 701,0 | 7% | 7% |
| Pb Anual | 0,5 | S/i |  | 0,003 | 0,003 |  |  | S/i |

**Tabla 5-4: Aportes en estación ENLASA para escenarios 1 a 4 para cada contaminante en análisis.****

| Parámetro | Escenario 1<br>g/m3N | Escenario 2<br>g/m3N | Escenario 3<br>g/m3N | Escenario 4<br>g/m3N |
| --- | --- | --- | --- | --- |
| MP10 Anual | 1,9 | 2,1 | 2,1 | 2,48 |
| MP10 P98 Diario | 6,7 | 7,4 | 7,5 | 8,7 |
| MP2.5 Anual | 1,6 | 1,8 | 1,9 | 2,1 |
| MP2.5 P98 Diario | 5,9 | 6,2 | 6,5 | 7,4 |
| NO2 Anual | 4,0 | 3,9 | 4,2 | 4,1 |
| NO2 P.99 Horario | 19,4 | 18,9 | 19,9 | 19,3 |
| SO2 Anual | 35,2 | 34,1 | 35,7 | 34,7 |
| SO2 P99 Diario | 43,7 | 42,4 | 50,8 | 49,1 |
| SO2 P99 Horario (1) | 9,0 | 9,2 | 9,1 | 9,9 |
| SO2 P99,73 Horario (2) | 81,7 | 84,5 | 81,7 | 87,3 |
| CO P99 horario | 39,4 | 43,7 | 46,7 | 83,0 |
| CO P99 8 horas | 15,8 | 17,5 | 18,5 | 44,3 |
| Pb anual | 0,0002 | 0,0016 | 0,0002 | 0,0016 |

**Tabla 5-5: Concentraciones ambientales de MP** **10** **, MP** **2.5** **, NO** **2** **, SO** **2** **, CO y Pb en Estación ENLASA****

| Parámetro | Norma de<br>calidad del<br>aire<br>g/m3N | Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1) | Aporte por<br>Proyecto<br>CBB<br>g/m3N<br>(2) | Aporte por<br>todos los<br>Proyectos<br>g/m3N<br>(3) | Nivel<br>actual más<br>Proyectos<br>g/m3N<br>(4) | Porcentaje<br>actual<br>respecto a<br>norma de<br>calidad | Porcentaje<br>con<br>Proyectos<br>respecto a<br>norma de<br>calidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 Anual | 50 | 33,8 | 0,2 | 0,3 | 34,1 | 68% | 68% |
| MP10 P98 Diario | 150 | 69,7 | 0,7 | 1,2 | 70,9 | 46% | 47% |
| MP2.5 Anual | 20 | 7,5 | 0,1 | 0,2 | 7,7 | 38% | 39% |
| MP2.5 P98 Diario | 50 | 24 | 0,3 | 0,9 | 24,9 | 48% | 50% |
| SO2 anual | 60 | 6,3 | -0,1 | -0,1 | 6,2 | 11% | 10% |
| SO2 P99 Diario | 150 | 38,3 | -0,6 | -0,6 | 37,7 | 26% | 25% |
| SO2 P99 Horario (5) | 350 | 64,1 | -1,1 | -1,1 | 63,0 | 18% | 18% |
| SO2 P99,73 Horario (6) | 700 | 105,1 | -1,3 | -1,6 | 103,5 | 15% | 15% |
| NO2 anual | 100 | 18,7 | 0,3 | 0,8 | 19,5 | 19% | 19% |
| NO2 P.99 Horario | 400 | 67 | 2,9 | 5,5 | 72,5 | 17% | 18% |
| CO P99 horario | 30.000 | 1000 | 4,3 | 36,3 | 1036,3 | 3% | 3% |
| CO P99 8 horas | 10.000 | 700 | 1,7 | 25,8 | 725,8 | 7% | 7% |
| Pb anual | 0,5 | S/i | 0,0014 | 0,0014 |  |  |  |

**Tabla 5-6: Resultados MP** **10** **Anual en PMI y los seis receptores de interés****

| Receptor | MP Anual<br>10<br>Escenario 1<br>g/m3N | MP Anual<br>10<br>Escenario 2<br>g/m3N | MP Anual<br>10<br>Escenario 3<br>g/m3N | MP Anual<br>10<br>Escenario 4<br>g/m3N |
| --- | --- | --- | --- | --- |
| PMI Teno CBB | 10,93 | 11,31 | 11,51 | 12,25 |
| R-1 Estación Teno ENLASA | 1,89 | 2,09 | 2,15 | 2,48 |
| R-2 Teno Norte | 0,21 | 0,23 | 0,31 | 0,34 |
| R-3 Estación FFCC Teno | 0,26 | 0,28 | 0,35 | 0,38 |
| R-4 Teno SE | 0,32 | 0,33 | 0,40 | 0,43 |
| R-5 Teno Sur | 0,22 | 0,23 | 0,30 | 0,32 |
| R-6 Teno Oeste | 0,16 | 0,16 | 0,21 | 0,23 |

**Tabla 5-7: Resultados Niveles de calidad del aire de MP** **10** **Anual en PMI y los seis receptores de interés****

| Receptor | Norma de<br>calidad<br>del aire<br>g/m3N | Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1) | Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2) | Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3) | Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4) | Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma | Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PMI Teno CBB | 50 | 33,8 | 0,38 | 0,75 | 34,55 | 68% | 69% |
| R-1 Estación<br>Teno ENLASA | 50 | 33,8 | 0,20 | 0,33 | 34,13 | 68% | 68% |
| R-2 Teno Norte | 50 | 33,8 | 0,01 | 0,03 | 33,83 | 68% | 68% |
| R-3 Estación<br>FFCC Teno | 50 | 33,8 | 0,01 | 0,03 | 33,83 | 68% | 68% |
| R-4 Teno SE | 50 | 33,8 | 0,02 | 0,03 | 33,83 | 68% | 68% |
| R-5 Teno Sur | 50 | 33,8 | 0,01 | 0,02 | 33,82 | 68% | 68% |
| R-6 Teno Oeste | 50 | 33,8 | 0,01 | 0,02 | 33,82 | 68% | 68% |

**Tabla 5-8: Resultados MP** **10** **Percentil 98 diario en los seis receptores discretos y** **punto de máximo impacto****

| Receptor | P. 98 MP<br>10<br>Diario<br>Escenario 1<br>g/m3N | P. 98 MP<br>10<br>Diario<br>Escenario 2<br>g/m3N | P. 98 MP<br>10<br>Diario<br>Escenario 3<br>g/m3N | P. 98 MP<br>10<br>Diario<br>Escenario 4<br>g/m3N |
| --- | --- | --- | --- | --- |
| PMI Teno CBB | 24,7 | 25,1 | 26,8 | 29,7 |
| R-1 Estación Teno ENLASA | 6,7 | 7,4 | 7,5 | 8,7 |
| R-2 Teno Norte | 1,9 | 1,9 | 2,7 | 2,8 |
| R-3 Estación FFCC Teno | 2,6 | 2,7 | 3,0 | 3,1 |
| R-4 Teno SE | 2,7 | 2,7 | 3,2 | 3,3 |
| R-5 Teno Sur | 2,3 | 2,3 | 2,7 | 2,9 |
| R-6 Teno Oeste | 1,3 | 1,4 | 1,7 | 1,8 |

**Tabla 5-9.: Resultados Niveles de calidad del aire de MP** **10** **Diario en PMI y en los seis receptores de interés****

| Receptor | Norma de<br>calidad<br>del aire<br>g/m3N | Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1) | Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2) | Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3) | Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4) | Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma | Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PMI Teno CBB | 150 | 69,7 | 0,5 | 3,0 | 72,7 | 46% | 48% |
| R-1 Estación<br>Teno ENLASA | 150 | 69,7 | 0,7 | 1,2 | 70,9 | 46% | 47% |
| R-2 Teno Norte | 150 | 69,7 | 0,0 | 0,1 | 69,8 | 46% | 47% |
| R-3 Estación<br>FFCC Teno | 150 | 69,7 | 0,1 | 0,1 | 69,8 | 46% | 47% |
| R-4 Teno SE | 150 | 69,7 | 0,0 | 0,1 | 69,8 | 46% | 47% |
| R-5 Teno Sur | 150 | 69,7 | 0,1 | 0,1 | 69,8 | 46% | 47% |
| R-6 Teno Oeste | 150 | 69,7 | 0,1 | 0,1 | 69,8 | 46% | 47% |

**Tabla 5-10: MP** **2.5** **Anual en PMI y los seis receptores de interés****

| Receptor | MP Anual<br>2,5<br>Escenario 1<br>g/m3N | MP Anual<br>2,5<br>Escenario 2<br>g/m3N | MP Anual<br>2,5<br>Escenario 3<br>g/m3N | MP Anual<br>2,5<br>Escenario 4<br>g/m3N |
| --- | --- | --- | --- | --- |
| PMI Teno CBB | 9,8 | 10,0 | 10,4 | 10,9 |
| R-1 Estación Teno ENLASA | 1,6 | 1,8 | 1,9 | 2,1 |
| R-2 Teno Norte | 0,2 | 0,2 | 0,3 | 0,3 |
| R-3 Estación FFCC Teno | 0,2 | 0,3 | 0,3 | 0,3 |
| R-4 Teno SE | 0,3 | 0,3 | 0,4 | 0,4 |
| R-5 Teno Sur | 0,2 | 0,2 | 0,3 | 0,3 |
| R-6 Teno Oeste | 0,1 | 0,2 | 0,2 | 0,2 |

**Tabla 5-11: Resultados Niveles de calidad del aire de MP** **2,5** **Anual en PMI y en los seis receptores de interés****

| Receptor | Norma de<br>calidad<br>del aire<br>g/m3N | Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1) | Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2) | Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3) | Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4) | Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma | Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PMI Teno CBB | 20 | 7,5 | 0,20 | 0,5 | 8,0 | 38% | 40% |
| R-1 Estación<br>Teno ENLASA | 20 | 7,5 | 0,11 | 0,2 | 7,7 | 38% | 39% |
| R-2 Teno Norte | 20 | 7,5 | 0,01 | 0,0 | 7,5 | 38% | 38% |
| R-3 Estación<br>FFCC Teno | 20 | 7,5 | 0,01 | 0,0 | 7,5 | 38% | 38% |
| R-4 Teno SE | 20 | 7,5 | 0,01 | 0,0 | 7,5 | 38% | 38% |
| R-5 Teno Sur | 20 | 7,5 | 0,01 | 0,0 | 7,5 | 38% | 38% |
| R-6 Teno Oeste | 20 | 7,5 | 0,01 | 0,0 | 7,5 | 38% | 38% |

**Tabla 5-12: Resultados MP** **2,5** **Percentil 98 diario en los seis receptores discretos y en el punto de máximo impacto****

| Receptor | P. 98 MP<br>2,5<br>Diario<br>Escenario 1<br>g/m3N | P. 98 MP<br>2,5<br>Diario<br>Escenario 2<br>g/m3N | P. 98 MP<br>2,5<br>Diario<br>Escenario 3<br>g/m3N | P. 98 MP<br>2,5<br>Diario<br>Escenario 4<br>g/m3N |
| --- | --- | --- | --- | --- |
| PMI Teno CBB | 22,2 | 22,4 | 25,1 | 27,1 |
| R-1 Estación Teno ENLASA | 5,9 | 6,2 | 6,5 | 7,4 |
| R-2 Teno Norte | 1,7 | 1,7 | 2,6 | 2,6 |
| R-3 Estación FFCC Teno | 2,4 | 2,5 | 2,8 | 2,9 |
| R-4 Teno SE | 2,4 | 2,4 | 3,0 | 3,0 |
| R-5 Teno Sur | 2,1 | 2,1 | 2,6 | 2,7 |
| R-6 Teno Oeste | 1,3 | 1,3 | 1,6 | 1,7 |

**Tabla 5-13: Resultados Niveles de calidad del aire de MP** **2,5** **P98 diario en PMI y en los seis receptores de interés****

| Receptor | Norma<br>de<br>calidad<br>del aire<br>g/m3N | Nivel actual<br>Calidad del<br>aire<br>g/m3N<br>(1) | Aporte por<br>proyecto<br>CBB<br>g/m3N<br>(2) | Aporte por<br>todos los<br>proyectos<br>g/m3N<br>(3) | Nivel actual<br>mas<br>proyectos<br>g/m3N<br>(4) | Porcentaje<br>Calidad del<br>aire actual<br>respecto de<br>norma | Porcentaje<br>Con<br>proyectos<br>respecto de<br>norma de<br>calidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PMI Teno CBB | 50 | 24 | 0,3 | 2,0 | 26,0 | 48% | 52% |
| R-1 Estación<br>Teno ENLASA | 50 | 24 | 0,3 | 0,9 | 24,9 | 48% | 50% |
| R-2 Teno Norte | 50 | 24 | 0,0 | 0,1 | 24,1 | 48% | 48% |
| R-3 Estación<br>FFCC Teno | 50 | 24 | 0,1 | 0,1 | 24,1 | 48% | 48% |
| R-4 Teno SE | 50 | 24 | 0,0 | 0,1 | 24,1 | 48% | 48% |
| R-5 Teno Sur | 50 | 24 | 0,1 | 0,1 | 24,1 | 48% | 48% |
| R-6 Teno Oeste | 50 | 24 | 0,0 | 0,1 | 24,1 | 48% | 48% |

**Tabla 5-14: Resultados NO** **2** **Anual en PMI y en los seis receptores de interés****

| Receptor | NO Anual<br>2<br>Escenario 1<br>g/m3N | NO Anual<br>2<br>Escenario 2<br>g/m3N | NO Anual<br>2<br>Escenario 3<br>g/m3N | NO Anual<br>2<br>Escenario 4<br>g/m3N |
| --- | --- | --- | --- | --- |
| PMI Teno CBB | 44,7 | 45,2 | 45,3 | 48,5 |
| R-1 Estación Teno ENLASA | 9,0 | 9,2 | 9,1 | 9,9 |
| R-2 Teno Norte | 0,6 | 0,6 | 0,6 | 0,6 |
| R-3 Estación FFCC Teno | 0,7 | 0,7 | 0,8 | 0,8 |
| R-4 Teno SE | 0,9 | 0,9 | 1,0 | 1,0 |
| R-5 Teno Sur | 0,6 | 0,6 | 0,6 | 0,6 |
| R-6 Teno Oeste | 0,3 | 0,4 | 0,4 | 0,4 |

**Tabla 5-16: Resultados NO** **2** **horario Percentil 99 en los seis receptores discretos y en el punto de máximo impacto****

| Receptor | P. 99<br>NO Horario<br>2<br>Escenario 1<br>g/m3N | P. 99<br>NO Horario<br>2<br>Escenario 2<br>g/m3N | P. 99<br>NO Horario<br>2<br>Escenario 3<br>g/m3N | P. 99<br>NO Horario<br>2<br>Escenario 4<br>g/m3N |
| --- | --- | --- | --- | --- |
| PMI Teno CBB | 121 | 124 | 132 | 139 |
| R-1 Estación Teno ENLASA | 82 | 85 | 82 | 87 |
| R-2 Teno Norte | 51 | 52 | 55 | 57 |
| R-3 Estación FFCC Teno | 48 | 50 | 49 | 50 |
| R-4 Teno SE | 56 | 56 | 56 | 56 |
| R-5 Teno Sur | 31 | 31 | 32 | 32 |
| R-6 Teno Oeste | 24 | 24 | 24 | 24 |

**Tabla 5-17: Resultados Niveles de calidad del aire de NO** **2** **horario P 99 en PMI y en los seis receptores de interés****

| Receptor | Norma de<br>calidad<br>del aire<br>g/m3N | Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1) | Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2) | Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3) | Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4) | Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma | Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PMI Teno CBB | 400 | 67 | 3,2 | 7,1 | 74,1 | 17% | 19% |
| R-1 Estación<br>Teno ENLASA | 400 | 67 | 2,9 | 5,5 | 72,5 | 17% | 18% |
| R-2 Teno Norte | 400 | 67 | 1,0 | 1,2 | 68,2 | 17% | 17% |
| R-3 Estación<br>FFCC Teno | 400 | 67 | 1,4 | 1,4 | 68,4 | 17% | 17% |
| R-4 Teno SE | 400 | 67 | 0,1 | 0,1 | 67,1 | 17% | 17% |
| R-5 Teno Sur | 400 | 67 | 0,0 | 0,0 | 67,0 | 17% | 17% |
| R-6 Teno Oeste | 400 | 67 | 0,1 | 0,1 | 67,1 | 17% | 17% |

**Tabla 5-18: Resultados SO** **2** **Anual en PMI y los seis receptores de interés****

| Receptor | SO Anual<br>2<br>Escenario 1<br>g/m3N | SO Anual<br>2<br>Escenario 2<br>g/m3N | SO Anual<br>2<br>Escenario 3<br>g/m3N | SO Anual<br>2<br>Escenario 4<br>g/m3N |
| --- | --- | --- | --- | --- |
| PMI Teno CBB | 10,1 | 9,9 | 11,9 | 11,7 |
| R-1 Estación Teno ENLASA | 4,0 | 3,9 | 4,2 | 4,1 |
| R-2 Teno Norte | 0,2 | 0,2 | 0,3 | 0,3 |
| R-3 Estación FFCC Teno | 0,2 | 0,2 | 0,2 | 0,2 |
| R-4 Teno SE | 0,3 | 0,3 | 0,3 | 0,3 |
| R-5 Teno Sur | 0,2 | 0,2 | 0,2 | 0,2 |
| R-6 Teno Oeste | 0,1 | 0,1 | 0,2 | 0,2 |

**Tabla 5-19: Resultados Niveles de calidad del aire de SO** **2** **Anual en PMI y los seis receptores de interés****

| Receptor | Norma de<br>calidad<br>del aire<br>g/m3N | Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1) | Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2) | Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3) | Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4) | Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma | Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PMI Teno CBB | 60 | 6,3 | -0,22 | -0,20 | 6,10 | 11% | 10% |
| R-1 Estación<br>Teno ENLASA | 60 | 6,3 | -0,12 | -0,11 | 6,19 | 11% | 10% |
| R-2 Teno Norte | 60 | 6,3 | -0,01 | 0,00 | 6,30 | 11% | 10% |
| R-3 Estación<br>FFCC Teno | 60 | 6,3 | -0,01 | -0,01 | 6,29 | 11% | 10% |
| R-4 Teno SE | 60 | 6,3 | -0,01 | -0,01 | 6,29 | 11% | 10% |
| R-5 Teno Sur | 60 | 6,3 | -0,01 | 0,00 | 6,30 | 11% | 10% |
| R-6 Teno Oeste | 60 | 6,3 | 0,00 | 0,00 | 6,30 | 11% | 10% |

**Tabla 5-20: Resultados SO** **2** **Percentil 99 diario en los seis receptores discretos y** **punto de máximo impacto****

| Receptor | P. 99<br>SO Diario<br>2<br>Escenario 1<br>g/m3N | P. 99<br>SO Diario<br>2<br>Escenario 2<br>g/m3N | P. 99<br>SO Diario<br>2<br>Escenario 3<br>g/m3N | P. 99<br>SO Diario<br>2<br>Escenario 4<br>g/m3N |
| --- | --- | --- | --- | --- |
| PMI Teno CBB | 28,8 | 28,0 | 58,0 | 57,7 |
| R-1 Estación Teno ENLASA | 19,4 | 18,9 | 19,9 | 19,3 |
| R-2 Teno Norte | 2,7 | 2,6 | 3,0 | 2,9 |
| R-3 Estación FFCC Teno | 3,1 | 3,0 | 3,1 | 3,1 |
| R-4 Teno SE | 3,1 | 3,0 | 3,1 | 3,0 |
| R-5 Teno Sur | 2,7 | 2,6 | 2,8 | 2,7 |
| R-6 Teno Oeste | 1,8 | 1,8 | 1,9 | 1,9 |

**Tabla 5-21: Resultados Niveles de calidad del aire de SO** **2** **P99 diario en PMI y en los seis receptores de interés****

| Receptor | Norma de<br>calidad<br>del aire<br>g/m3N | Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1) | Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2) | Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3) | Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4) | Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma | Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PMI Teno CBB | 150 | 38,3 | -0,8 | -0,3 | 38,0 | 26% | 25% |
| R-1 Estación<br>Teno ENLASA | 150 | 38,3 | -0,6 | -0,6 | 37,7 | 26% | 25% |
| R-2 Teno Norte | 150 | 38,3 | -0,1 | -0,1 | 38,2 | 26% | 25% |
| R-3 Estación<br>FFCC Teno | 150 | 38,3 | -0,1 | -0,1 | 38,2 | 26% | 25% |
| R-4 Teno SE | 150 | 38,3 | -0,1 | -0,1 | 38,2 | 26% | 25% |
| R-5 Teno Sur | 150 | 38,3 | -0,1 | -0,1 | 38,2 | 26% | 25% |
| R-6 Teno Oeste | 150 | 38,3 | -0,1 | 0,0 | 38,3 | 26% | 26% |

**Tabla 5-22: Resultados SO** **2** **horario P99 (**  **g/m** **[3]** **) en los seis receptores discretos y** **punto de máximo impacto****

| Receptor | SO Horario<br>2<br>Escenario 1<br>g/m3N | SO Horario<br>2<br>Escenario 2<br>g/m3N | SO Horario<br>2<br>Escenario 3<br>g/m3N | SO Horario<br>2<br>Escenario 4<br>g/m3N |
| --- | --- | --- | --- | --- |
| Análisis P99 | Análisis P99 | Análisis P99 | Análisis P99 | Análisis P99 |
| PMI Teno CBB | 57 | 55 | 75 | 73 |
| R-1 Estación Teno ENLASA | 35 | 34 | 36 | 35 |
| R-2 Teno Norte | 3 | 3 | 3 | 3 |
| R-3 Estación FFCC Teno | 4 | 4 | 4 | 4 |
| R-4 Teno SE | 5 | 5 | 5 | 5 |
| R-5 Teno Sur | 3 | 3 | 3 | 3 |
| R-6 Teno Oeste | 2 | 2 | 2 | 2 |
| Análisis P99,73 | Análisis P99,73 | Análisis P99,73 | Análisis P99,73 | Análisis P99,73 |
| PMI Teno CBB | 78 | 76 | 141 | 140 |
| R-1 Estación Teno ENLASA | 44 | 42 | 51 | 49 |
| R-2 Teno Norte | 9 | 8 | 10 | 10 |
| R-3 Estación FFCC Teno | 12 | 12 | 12 | 12 |
| R-4 Teno SE | 13 | 13 | 13 | 13 |
| R-5 Teno Sur | 10 | 10 | 11 | 11 |
| R-6 Teno Oeste | 6 | 6 | 7 | 6 |

**Tabla 5-23: Resultados Niveles de calidad del aire de SO** **2** **P99 Horario en PMI y los seis receptores de interés****

| Receptor | Norma de<br>calidad<br>del aire<br>g/m3N | Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1) | Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2) | Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3) | Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4) | Porcentaje<br>Calidad del<br>aire actual<br>respecto<br>de norma | Porcentaje<br>Con<br>proyectos<br>respecto<br>de norma<br>de calidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Análisis P99 | Análisis P99 | Análisis P99 | Análisis P99 | Análisis P99 | Análisis P99 | Análisis P99 | Análisis P99 |
| PMI Teno CBB | 350 | 64,1 | -1,8 | -1,5 | 62,6 | 18% | 18% |
| R-1 Estación<br>Teno ENLASA | 350 | 64,1 | -1,1 | -1,1 | 63,0 | 18% | 18% |
| R-2 Teno Norte | 350 | 64,1 | -0,1 | 0,0 | 64,1 | 18% | 18% |
| R-3 Estación<br>FFCC Teno | 350 | 64,1 | -0,1 | -0,1 | 64,0 | 18% | 18% |
| R-4 Teno SE | 350 | 64,1 | -0,1 | -0,1 | 64,0 | 18% | 18% |
| R-5 Teno Sur | 350 | 64,1 | -0,1 | -0,1 | 64,0 | 18% | 18% |
| R-6 Teno Oeste | 350 | 64,1 | -0,1 | -0,1 | 64,0 | 18% | 18% |
| Análisis P99,73 | Análisis P99,73 | Análisis P99,73 | Análisis P99,73 | Análisis P99,73 | Análisis P99,73 | Análisis P99,73 | Análisis P99,73 |
| PMI Teno CBB | 700 | 105,1 | -2,4 | -0,7 | 104,5 | 15% | 15% |
| R-1 Estación<br>Teno ENLASA | 700 | 105,1 | -1,3 | -1,6 | 103,5 | 15% | 15% |
| R-2 Teno Norte | 700 | 105,1 | -0,3 | -0,3 | 104,8 | 15% | 15% |
| R-3 Estación<br>FFCC Teno | 700 | 105,1 | -0,3 | -0,1 | 105,0 | 15% | 15% |
| R-4 Teno SE | 700 | 105,1 | -0,4 | -0,4 | 104,7 | 15% | 15% |
| R-5 Teno Sur | 700 | 105,1 | -0,3 | -0,2 | 104,9 | 15% | 15% |
| R-6 Teno Oeste | 700 | 105,1 | -0,2 | -0,2 | 104,9 | 15% | 15% |

**Tabla 5-24: Resultados CO Percentil 99 horario en los seis receptores discretos y** **punto de máximo impacto****

| Receptor | P. 99<br>CO<br>Horario<br>Escenario 1<br>g/m3N | P. 99<br>CO<br>Horario<br>Escenario 2<br>g/m3N | P. 99<br>CO<br>Horario<br>Escenario 3<br>g/m3N | P. 99<br>CO<br>Horario<br>Escenario 4<br>g/m3N |
| --- | --- | --- | --- | --- |
| PMI Teno CBB | 50 | 56 | 195 | 195 |
| R-1 Estación Teno ENLASA | 39 | 44 | 47 | 83 |
| R-2 Teno Norte | 16 | 17 | 17 | 19 |
| R-3 Estación FFCC Teno | 13 | 15 | 14 | 16 |
| R-4 Teno SE | 14 | 15 | 14 | 16 |
| R-5 Teno Sur | 10 | 11 | 11 | 13 |
| R-6 Teno Oeste | 10 | 11 | 10 | 11 |

**Tabla 5-25: Resultados Niveles de calidad del aire de CO P99 horario en PMI y los seis receptores de interés****

| Receptor | Norma de<br>calidad<br>del aire<br>g/m3N | Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1) | Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2) | Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3) | Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4) | Porcentaje<br>de<br>aumento<br>nivel actual | Porcentaje<br>respecto a<br>norma de<br>calidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PMI Teno CBB | 30.000 | 1.000 | 5 | 0 | 1000 | 3% | 3% |
| R-1 Estación<br>Teno ENLASA | 30.000 | 1.000 | 4 | 36 | 1036 | 3% | 3% |
| R-2 Teno Norte | 30.000 | 1.000 | 2 | 2 | 1002 | 3% | 3% |
| R-3 Estación<br>FFCC Teno | 30.000 | 1.000 | 1 | 2 | 1002 | 3% | 3% |
| R-4 Teno SE | 30.000 | 1.000 | 1 | 2 | 1002 | 3% | 3% |
| R-5 Teno Sur | 30.000 | 1.000 | 1 | 1 | 1001 | 3% | 3% |
| R-6 Teno Oeste | 30.000 | 1.000 | 1 | 1 | 1001 | 3% | 3% |

**Tabla 5-26: Resultados CO Percentil 99 8 horas en los seis receptores discretos y** **punto de máximo impacto****

| Receptor | P. 99<br>CO<br>8 horas<br>Escenario 1<br>g/m3N | P. 99<br>CO<br>8 horas<br>Escenario 2<br>g/m3N | P. 99<br>CO<br>8 horas<br>Escenario 3<br>g/m3N | P. 99<br>CO<br>8 horas<br>Escenario 4<br>g/m3N |
| --- | --- | --- | --- | --- |
| PMI Teno CBB | 22 | 25 | 95 | 96 |
| R-1 Estación Teno ENLASA | 16 | 18 | 19 | 44 |
| R-2 Teno Norte | 2 | 3 | 3 | 3 |
| R-3 Estación FFCC Teno | 2 | 3 | 3 | 3 |
| R-4 Teno SE | 3 | 3 | 3 | 3 |
| R-5 Teno Sur | 2 | 2 | 2 | 2 |
| R-6 Teno Oeste | 2 | 2 | 2 | 2 |

**Tabla 5-27: Resultados Niveles de calidad del aire de CO P99 8 horas en PMI y los seis receptores de interés****

| Receptor | Norma de<br>calidad<br>del aire<br>g/m3N | Nivel<br>actual<br>Calidad<br>del aire<br>g/m3N<br>(1) | Aporte<br>por<br>proyecto<br>CBB<br>g/m3N<br>(2) | Aporte<br>por todos<br>los<br>proyectos<br>g/m3N<br>(3) | Nivel<br>actual mas<br>proyectos<br>g/m3N<br>(4) | Porcentaje<br>de<br>aumento<br>nivel actual | Porcentaje<br>respecto a<br>norma de<br>calidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PMI Teno CBB | 10.000 | 700 | 2 | 1 | 701 | 7% | 7% |
| R-1 Estación<br>Teno ENLASA | 10.000 | 700 | 2 | 26 | 726 | 7% | 7% |
| R-2 Teno Norte | 10.000 | 700 | 0 | 1 | 701 | 7% | 7% |
| R-3 Estación<br>FFCC Teno | 10.000 | 700 | 0 | 0 | 700 | 7% | 7% |
| R-4 Teno SE | 10.000 | 700 | 0 | 0 | 700 | 7% | 7% |
| R-5 Teno Sur | 10.000 | 700 | 0 | 0 | 700 | 7% | 7% |
| R-6 Teno Oeste | 10.000 | 700 | 0 | 0 | 700 | 7% | 7% |

**Tabla 5-28: Resultados Plomo en PMI y los seis receptores de interés y comparación con norma de calidad****

| Receptor | Pb Anual<br>Escenario 1<br>g/m3N | Pb Anual<br>Escenario 2<br>g/m3N | Aumento por<br>Proyecto CBB<br>g/m3N | Norma<br>Calidad de<br>aire<br>g/m3N | Aumento<br>respecto de<br>norma<br>calidad % |
| --- | --- | --- | --- | --- | --- |
| PMI Teno CBB | 0,00045 | 0,00313 | 0,0027 | 0,5 | 0,54% |
| R-1 Estación Teno ENLASA | 0,00024 | 0,00165 | 0,0014 | 0,5 | 0,28% |
| R-2 Teno Norte | 0,00001 | 0,00008 | 0,0001 | 0,5 | 0,01% |
| R-3 Estación FFCC Teno | 0,00001 | 0,00009 | 0,0001 | 0,5 | 0,02% |
| R-4 Teno SE | 0,00001 | 0,00010 | 0,0001 | 0,5 | 0,02% |
| R-5 Teno Sur | 0,00001 | 0,00008 | 0,0001 | 0,5 | 0,01% |
| R-6 Teno Oeste | 0,00001 | 0,00006 | 0,0001 | 0,5 | 0,01% |

**Tabla 5-29: Nivel de Azufre y Nitrógeno depositado en suelo considerando PMI y a 2 km del sitio, Escenarios 1 a 4.****

| Col1 | Col2 | Azufre (S)<br>depositado en<br>suelo en PMI | Azufre (S)<br>depositado en<br>suelo a 1 km de<br>PMI | Nitrógeno (N)<br>depositado en<br>suelo en PMI | Nitrógeno (N)<br>depositado en<br>suelo a 1 km de<br>PMI |
| --- | --- | --- | --- | --- | --- |
| **Escenario 1** | **Depósito anual**<br>**Eq/(ha-año)** | 179 | 50 | 879 | 100 |
| **Escenario 1** | **Porcentaje respecto de nivel de**<br>**referencia %** | 17,9% | 5% | 88% | 10% |
| **Escenario 2** | **Depósito anual**<br>**Eq/(ha-año)** | 174 | 50 | 892 | 100 |
| **Escenario 2** | **Porcentaje respecto de nivel de**<br>**referencia %** | 17,4% | 5% | 89% | 10% |
| **Escenario 3** | **Depósito anual**<br>**Eq/(ha-año)** | 200 | 75 | 889 | 200 |
| **Escenario 3** | **Porcentaje respecto de nivel de**<br>**referencia %** | 20% | 7,5% | 89% | 20% |
| **Escenario 4** | **Depósito anual**<br>**Eq/(ha-año)** | 196 | 75 | 953 | 200 |
| **Escenario 4** | **Porcentaje respecto de nivel de**<br>**referencia %** | 20% | 7,5% | 95% | 20% |

**Tabla 6-1.: Análisis de sensibilidad comparando los resultados de la modelación CALPUFF-WRF con los valores medidos****

| Parámetro | Norma de<br>calidad del aire<br>g/m3N | Nivel calidad del<br>aire<br>Medido 2018<br>g/m3N | Nivel calidad del<br>aire modelación<br>g/m3N | Factor Modelo /<br>Medición |
| --- | --- | --- | --- | --- |
| **MP10 Anual** | 50 | 30,0 | 1,1 | 27,9 |
| **P. 98 MP10 24 h** | 150 | 62 | 3,7 | 16,6 |
| **MP2.5 Anual** | 20 | 10,4 | 0,94 | 11,1 |
| **P. 98 MP2.5 Diario** | 50 | 46,1 | 3,2 | 14,4 |
| **NO2 anual** | 100 | 16,5 | 4,6 | 3,6 |
| **P. 99 NO2 1h** | 400 | 63,7 | 81,0 | 0,79 |
| **NO2 1h máximo** | - | 110,5 | 136 | 0,8 |
| **SO2 anual** | 80 | 4,2 | 2,11 | 2,0 |
| **P. 99 SO2 24 h** | 250 | 21,9 | 9,9 | 2,2 |
| **P. 99 SO2 1h** | 350 | 34,7 | 25,5 | 1,4 |
| **P. 99,73 SO2 1h** | 700 | 53,9 | 36,3 | 1,5 |
| **SO2 1h máximo** | - | 106 | 138 | 0,77 |
| **P. 99 Máximo CO 1 h** | 30000 | 700 | 152 | 4,61 |
| **P.99 Máximo CO 8 h** | 10000 | 588 | 60 | 9,8 |
| **Máximo CO 1h** | - | 1400 | 261 | 5,4 |

**Tabla 6-2.: Comparación de los resultados de la modelación CALPUFF-WRF (usando un factor de corrección) con los****

| Parámetro | Norma de<br>calidad del aire<br>g/m3N | Nivel calidad del<br>aire<br>Medido<br>g/m3N | Nivel calidad del<br>aire modelación<br>g/m3N | Factor Modelo /<br>Medición |
| --- | --- | --- | --- | --- |
| **MP10 Anual** | 50 | 30 | 2,15 | 14,0 |
| **P. 98 MP10 24 h** | 150 | 62 | 7,5 | 8,3 |
| **MP2.5 Anual** | 20 | 10,5 | 1,89 | 5,6 |
| **P. 98 MP2.5 Diario** | 50 | 46,1 | 6,5 | 7,1 |
| **NO2 anual** | 100 | 16,7 | 9,1 | 1,8 |
| **P. 99 NO2 1h** | 400 | 89,5 | 82 | 1,1 |
| **NO2 1h máximo** | - | 110,5 | 110 | 1,0 |
| **SO2 anual** | 80 | 4,2 | 4,23 | 1,0 |
| **P. 99 SO2 24 h** | 250 | 21,9 | 19,9 | 1,1 |
| **P. 99 SO2 1h** | 350 | 34,7 | 35,7 | 1,0 |
| **P. 99,73 SO2 1h** | 700 | 53,9 | 50,8 | 1,1 |
| **SO2 1h máximo** | - | 106 | 106 | 1,0 |
| **P. 99 Máximo CO 1 h** | 30000 | 700 | 47 | 15,0 |
| **P.99 Máximo CO 8 h** | 10000 | 588 | 19 | 31,7 |

**Tabla 7-1: Concentraciones ambientales de MP** **10** **, MP** **2.5** **, NO** **2** **, SO** **2** **, CO y Pb**  **g/m3 en PMI y porcentajes según las****

| Parámetro | Norma de<br>calidad del<br>aire<br>g/m3N (1) | Nivel<br>actual<br>Calidad del<br>aire<br>g/m3N (2) | Porcentaje<br>c. aire<br>actual<br>c/r a<br>norma de<br>calidad | Aporte por<br>proyecto<br>Cbb<br>g/m3N<br>(3) | Aporte por<br>todos los<br>proyectos<br>g/m3N<br>(4) | Nivel c.<br>aire con<br>proyectos<br>g/m3N<br>(5) | Porcentaje<br>calidad<br>aire por<br>proyecto<br>CBB c/r a<br>norma<br>calidad<br>aire | Porcentaje<br>c. aire con<br>proyectos<br>c/r a<br>norma de<br>calidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 Anual | 50 | 33,8 | 68% | 0,4 | 0,7 | 34,5 | 68% | 69% |
| MP10 P98 Diario | 150 | 69,7 | 46% | 0,5 | 3,0 | 72,7 | 47% | 48% |
| MP2.5 Anual | 20 | 7,5 | 38% | 0,2 | 0,5 | 8,0 | 39% | 40% |
| MP2.5 P98 Diario | 50 | 24 | 48% | 0,3 | 2,0 | 26,0 | 49% | 52% |
| SO2 Anual | 60 | 6,3 | 11% | -0,2 | -0,2 | 6,1 | 10% | 10% |
| SO2 P99 Diario (6) | 150 | 38,3 | 26% | -0,8 | -0,3 | 38,0 | 25% | 25% |
| SO2 P99 Horario | 350 | 64,1 | 18% | -1,8 | -1,5 | 62,6 | 18% | 18% |
| SO2 P99,73<br>Horario (7) | 700 | 105,1 | 15% | -2,4 | -0,7 | 104,5 | 15% | 15% |
| NO2 Anual | 100 | 18,7 | 19% | 0,5 | 3,1 | 21,8 | 19% | 22% |
| NO2 P.99 Horario | 400 | 67 | 17% | 3,2 | 7,1 | 74,1 | 18% | 19% |
| CO P99 Horario | 30,000 | 1000 | 3% | 5,4 | 0,2 | 1000,2 | 3% | 3% |
| CO P99 8 horas | 10,000 | 700 | 7% | 2,4 | 1,0 | 701,0 | 7% | 7% |
| Pb Anual | 0,5 | S/i |  | 0,003 | 0,003 |  |  | S/i |

**Tabla 7-2: Concentraciones ambientales de MP** **10** **, MP** **2.5** **, NO** **2** **, SO** **2** **, CO y Pb en Estación de Calidad del Aire ENLASA y****

| Parámetro | Norma de<br>calidad del<br>aire<br>g/m3N (1) | Nivel<br>actual<br>Calidad del<br>aire<br>g/m3N (2) | Aporte<br>por<br>proyecto<br>Cbb (3) | Aporte<br>por todos<br>los<br>proyectos<br>(4) | Nivel<br>actual<br>mas<br>proyectos<br>(5) | Porcentaj<br>e c. aire<br>actual<br>c/r a<br>norma de<br>calidad | Porcentaj<br>e<br>respecto<br>a norma<br>de<br>calidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 Anual | 50 | 33,8 | 0,2 | 0,3 | 34,1 | 68% | 68% |
| MP10 P98 Diario | 150 | 69,7 | 0,7 | 1,2 | 70,9 | 46% | 47% |
| MP2.5 Anual | 20 | 7,5 | 0,1 | 0,2 | 7,7 | 38% | 39% |
| MP2.5 P98 Diario | 50 | 24 | 0,3 | 0,9 | 24,9 | 48% | 50% |
| SO2 Anual | 60 | 6,3 | -0,1 | -0,1 | 6,2 | 11% | 10% |
| SO2 P99 Diario (6) | 150 | 38,3 | -0,6 | -0,6 | 37,7 | 26% | 25% |
| SO2 P99 Horario | 350 | 64,1 | -1,1 | -1,1 | 63,0 | 18% | 18% |
| SO2 P99,73<br>Horario (7) | 700 | 105,1 | -1,3 | -1,6 | 103,5 | 15% | 15% |
| NO2 Anual | 100 | 18,7 | 0,3 | 0,8 | 19,5 | 19% | 19% |
| NO2 P.99 Horario | 400 | 67 | 2,9 | 5,5 | 72,5 | 17% | 18% |
| CO P99 Horario | 30,000 | 1000 | 4,3 | 36,3 | 1036,3 | 3% | 3% |
| CO P99 8 horas | 10,000 | 700 | 1,7 | 25,8 | 725,8 | 7% | 7% |
| Pb Anual | 0,5 | S/i | 0,0014 | 0,0014 |  |  |  |
