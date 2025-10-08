---
title: Sin título
author: Asesorías del Favero y Meneses
date: D:20230414092108-04'00'
language: es
type: report
pages: 174
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”
-->

## Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

# Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”

### Marzo 2023

**PREPARADO PARA**

Golder Associates

|REVISIONES|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|No REV.|ELABORADO POR|REVISADO POR|FECHA|FIRMA RESPONSABLE|
|V0|Carlos Ross|María José Meneses V|16-03-23||
|V0|Ingeniero Ambiental<br>(UNAB), MSc.|Ingeniero Civil de Industrias<br>con Mención en Ingeniería<br>Química, PUC|Ingeniero Civil de Industrias<br>con Mención en Ingeniería<br>Química, PUC|Ingeniero Civil de Industrias<br>con Mención en Ingeniería<br>Química, PUC|
|V0|Ingeniero Ambiental<br>(UNAB), MSc.|Ingeniero Civil de Industrias<br>con Mención en Ingeniería<br>Química, PUC|Ingeniero Civil de Industrias<br>con Mención en Ingeniería<br>Química, PUC|María José Meneses V.|

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

ÍNDICE

1 INTRODUCCIÓN ............................................................................................................................. 1

2 OBJETIVOS ...................................................................................................................................... 3

2.1 Objetivo General ..................................................................................................................................................... 3

2.2 Objetivos Específicos ............................................................................................................................................. 3

3 INVENTARIO DE EMISIONES ATMOSFÉRICAS ........................................................................ 5

3.1 Descripción de Metodología Utilizada ................................................................................................................ 5

3.2 Fase de Cierre ......................................................................................................................................................... 8

3.2.1 Factores de Emisión ......................................................................................................... 8

3.2.2 Niveles de Actividad ....................................................................................................... 18

3.2.3 Emisiones ......................................................................................................................... 26

3.2.4 Resumen de Emisiones Fase de Cierre ...................................................................... 31

3.2.5 Resumen de Medidas de Control de Emisiones Fase de Cierre ............................. 31

3.3 Conclusiones ........................................................................................................................................................ 33

4 MODELO DE CALIDAD DEL AIRE ............................................................................................ 33

4.1 Tipo de Modelo de Calidad del Aire Seleccionado ........................................................................................ 33

4.2 Descripción del Modelo de Calidad del Aire Seleccionado - CALPUFF ..................................................... 33

4.3 Características del Modelo de Dispersión de Contaminantes ..................................................................... 35

4.3.1 Dominio de la Modelación ............................................................................................ 35

4.3.2 Topografía del Sector ..................................................................................................... 36

4.3.3 Uso de Suelos ................................................................................................................. 37

4.4 Descripción del Modelo Meteorológico Seleccionado - WRF .................................................................... 38

4.5 Caracterización Meteorológica del Área del Proyecto .................................................................................. 39

4.5.1 Meteorología de Superficie - Valores Observados ................................................... 40

4.5.2 Meteorología de Superficie - Valores Modelados ..................................................... 61

www.dfmconsultores.cl
i
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

4.6 Análisis de Incertidumbre ................................................................................................................................... 76

4.6.1 Estación JJ Latorre .......................................................................................................... 76

4.7 Normas de Calidad del Aire ............................................................................................................................... 83

4.8 Línea Base Medida de Calidad del Aire ........................................................................................................... 85

4.8.1 Estaciones ........................................................................................................................ 85

4.8.2 Estación JJ Latorre .......................................................................................................... 89

4.8.3 Estación Jardín Infantil .................................................................................................... 92

4.8.4 Estación Puerto Mejillones ............................................................................................ 96

4.8.5 Estación Ferrocarril ......................................................................................................... 98

4.8.6 Angamos 1 ................................................................................................................... 105

4.8.7 Estación MOLYB .......................................................................................................... 108

4.8.8 Estación MOLYNOR .................................................................................................... 113

4.8.9 Estación Subestación Eléctrica .................................................................................. 117

4.8.10 Resumen Línea de Base de Calidad del Aire........................................................... 121

4.9 Línea Base Proyectada .................................................................................................................................... 122

4.10 Receptores de Interés ..................................................................................................................................... 126

4.11 Escenario de Modelación ................................................................................................................................ 128

4.12 Resultados de la Modelación ......................................................................................................................... 131

4.12.1 Material Particulado Fino (MP2,5) ........................................................................... 132

4.12.2 Material Particulado Respirable (MP10) ................................................................. 136

4.12.3 Dióxido de Nitrógeno (NO 2 ) ..................................................................................... 140

4.12.4 Dióxido de Azufre (SO 2 ) ............................................................................................ 144

4.12.5 Monóxido de Carbono (CO) ...................................................................................... 154

4.12.6 Material Particulado Sedimentable (MPS) .............................................................. 157

4.13 Concentración Total Esperada ....................................................................................................................... 159

5 CONCLUSIONES ....................................................................................................................... 161

www.dfmconsultores.cl
ii
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

5.1 Inventario de Emisiones de Contaminantes Atmosféricos ........................................................................ 161

5.2 Caracterización Meteorológica del Área del Proyecto y Análisis de Incertidumbre del Modelo WRF161

5.3 Línea de Base de Calidad del Aire ................................................................................................................ 162

5.4 Modelación de Dispersión de Contaminantes Atmosféricos .................................................................... 162

6 ANEXO 1: ARCHIVOS DIGITALES MODELACIÓN ............................................................... 164

www.dfmconsultores.cl
iii
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

ÍNDICE TABLAS

**Tabla 3-1. Cronograma Fase de Cierre.** ............................................................................................ 7

**Tabla 3-2 - Factores de Emisión Movimientos de Tierra - Fase de cierre.** ............................ 9

**Tabla 3-3 - Factores de Emisión Maquinaria - Fase de Cierre.** ............................................... 11

**Tabla 3-4 - Factores de Emisión Grupos Electrógenos - Fase de Cierre.** .............................. 12

**Tabla 3-5 - Factores de Emisión Resuspensión de Polvo - Fase de Cierre.** .......................... 13

**Tabla 3-6 - Factores de Emisión Combustión por Tránsito Vehicular - Fase de Cierre.** ... 16

**Tabla 3-7. Niveles de actividad asociados a movimientos de tierra por Excavación. Fase**

**de Cierre.** ............................................................................................................................................... 19

**Tabla 3-8. Niveles de actividad asociados a movimientos de tierra por Compactado. Fase**

**de Cierre.** ............................................................................................................................................... 19

**Tabla 3-9. Niveles de actividad asociados a movimientos de tierra por Transferencia de**

**Material. Fase de Cierre.** ................................................................................................................... 19

**Tabla 3-10 - Maquinaria Utilizada - Fase de Cierre.** .................................................................. 20

**Tabla 3-11. Grupos Electrógenos Utilizados - Fase de Cierre.** ................................................. 20

**Tabla 3-12 - Tramos de los caminos del proyecto.** .................................................................... 21

**Tabla 3-13. Movimientos vehiculares para cada tramo. Fase de cierre.** .............................. 24

**Tabla 3-14. Distancias por recorrer en cada tramo - Fase de Cierre.** .................................... 25

**Tabla 3-15 - Emisiones por movimientos de tierra. Fase de Cierre.** ...................................... 26

**Tabla 3-16 - Emisiones Utilización de Maquinaria. Fase de Cierre.** ....................................... 27

**Tabla 3-17 - Emisiones Utilización de Grupos Electrógenos. Fase de Cierre.** ...................... 28

**Tabla 3-18 - Emisiones Producto de Resuspensión del Polvo. Fase de Cierre.** ................... 29

**Tabla 3-19 - Emisiones Producto de Combustión Vehicular. Fase de Cierre.** ...................... 30

**Tabla 3-20 - Resumen Emisiones. Fase de Cierre.** ...................................................................... 31

**Tabla 4-1. Configuración parámetros principales WRF** ............................................................. 39

www.dfmconsultores.cl
iv
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-2. Coordenadas de Ubicación, Estación de Monitoreo Meteorológico JJ Latorre.**

................................................................................................................................................................. 40

**Tabla 4-3. Resumen de Información Velocidad del Viento Observada en Estación JJ**

**Latorre.** .................................................................................................................................................. 42

**Tabla 4-4. Frecuencia de distribución Velocidad y Dirección del Viento. Periodo enero**

**2020 a diciembre 2020. Observado en Estación JJ Latorre.** ..................................................... 45

**Tabla 4-5. Resumen de Información Temperatura Observada en Estación JJ Latorre.** ..... 49

**Tabla 4-6. Resumen de Información Humedad Relativa Observada en Estación JJ Latorre.**

................................................................................................................................................................. 53

**Tabla 4-7. Resumen de Información Radiación Solar Observada en Estación JJ Latorre.** 57

**Tabla 4-8. Resumen de Información Velocidad del Viento Modelada en Estación JJ**

**Latorre, Año 2020.** .............................................................................................................................. 61

**Tabla 4-9. Frecuencia de distribución Velocidad y Dirección del Viento. Período enero a**

**diciembre 2020. Modelado en Estación JJ Latorre.** .................................................................... 64

**Tabla 4-10. Resumen de Información Temperatura Modelada en Estación JJ Latorre.** .... 68

**Tabla 4-11. Resumen de Información Altura de Capa de Mezcla Modelada en Estación JJ**

**Latorre.** .................................................................................................................................................. 72

**Tabla 4-12. Estadígrafos de Dispersión de Velocidad del Viento y Temperatura.** .............. 82

**Tabla 4-13. Normas primarias de calidad del aire.** ..................................................................... 83

**Tabla 4-14. Normas secundarias de calidad del aire.** ................................................................. 84

**Tabla 4-15. Caracterización de Estaciones de Monitoreo de Calidad del Aire Utilizadas**

**para Línea de Base de Calidad del Aire.** ........................................................................................ 85

**Tabla 4-16. Resultados Monitoreo MP10. Estación JJ Latorre.** ............................................... 90

**Tabla 4-17- Comparación de Monitoreo de MP10 con Normativa. Estación JJ Latorre.** .. 90

**Tabla 4-18. Resultados de Monitoreo de NO** **2** **. Estación JJ Latorre.** ....................................... 91

**Tabla 4-19. Comparación de Monitoreo de NO** **2** **con Normativa. Estación JJ Latorre.** ...... 91

www.dfmconsultores.cl
v
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-20. Resultados Monitoreo de MP10. Estación Jardín Infantil.** ................................. 93

**Tabla 4-21. Comparación de Monitoreo de MP10 con Normativa. Estación Jardín Infantil.**

................................................................................................................................................................. 94

**Tabla 4-22. Resultados Monitoreo de NO** **2** **. Estación Jardín Infantil.** ..................................... 95

**Tabla 4-23. Comparación de Monitoreo de NO** **2** **con Normativa. Estación Jardín Infantil.**

................................................................................................................................................................. 95

**Tabla 4-24. Resultados Monitoreo de MP10. Estación Puerto Mejillones.** .......................... 97

**Tabla 4-25. Comparación de Monitoreo de MP10 con Normativa. Estación Puerto**

**Mejillones.** ............................................................................................................................................ 97

**Tabla 4-26. Resultados Monitoreo MP2,5. Estación Ferrocarril.** ............................................ 98

**Tabla 4-27. Comparación de Monitoreo de MP2,5 con Normativa. Estación Ferrocarril.** 98

**Tabla 4-28 - Resultados Monitoreo de MP10. Estación Ferrocarril.** ...................................... 99

**Tabla 4-29 - Comparación de Monitoreo de MP10 con Normativa. Estación Ferrocarril.**

.............................................................................................................................................................. 100

**Tabla 4-30. Resultados Monitoreo de NO** **2** **. Estación Ferrocarril.** ........................................ 100

**Tabla 4-31. Comparación de Monitoreo de NO** **2** **con Normativa. Estación Ferrocarril.** . 101

**Tabla 4-32 - Resultados Monitoreo de SO** **2** **. Estación Ferrocarril** . ....................................... 101

**Tabla 4-33 - Comparación de Monitoreo de SO** **2** **con Normativa. Estación Ferrocarril.** 102

**Tabla 4-34. Resultados Monitoreo de CO. Estación Ferrocarril.** .......................................... 103

**Tabla 4-35. Comparación de Monitoreo de CO con Normativa. Estación Ferrocarril.** ... 103

**Tabla 4-36. Resultados Monitoreo de O3. Estación Ferrocarril.** .......................................... 104

**Tabla 4-37. Comparación de Monitoreo de O** **3** **con Normativa. Estación Ferrocarril.** .... 104

**Tabla 4-38. Resultados Monitoreo de MP10. Estación Angamos 1.** ................................... 105

**Tabla 4-39. Comparación de Monitoreo de MP10 con Normativa. Estación Angamos 1.**

.............................................................................................................................................................. 105

**Tabla 4-40. Resultados Monitoreo de NO** **2** **. Estación Angamos 1.** ....................................... 106

www.dfmconsultores.cl
vi
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-41. Comparación de Monitoreo de NO** **2** **con Normativa. Estación Angamos 1.** 107

**Tabla 4-42. Resultados Monitoreo de SO** **2** **. Estación Angamos 1.** ........................................ 107

**Tabla 4-43 - Comparación de Monitoreo de SO** **2** **con Normativa. Estación Angamos 1.** 108

**Tabla 4-44. Resultados Monitoreo MP2,5. Estación MOLYB.** ............................................... 109

**Tabla 4-45. Comparación de Monitoreo de MP2,5 con Normativa. Estación MOLYB.** .. 109

**Tabla 4-46. Resultados Monitoreo de MP10. Estación MOLYB.** .......................................... 110

**Tabla 4-47. Comparación de Monitoreo de MP10 con Normativa. Estación MOLYB.** .... 110

**Tabla 4-48. Resultados Monitoreo de NO** **2** **. Estación MOLYB.** .............................................. 111

**Tabla 4-49. Comparación de Monitoreo de NO** **2** **con Normativa. Estación MOLYB.** ....... 111

**Tabla 4-50. Resultados Monitoreo de SO** **2** **. Estación MOLYB.** ............................................... 112

**Tabla 4-51 - Comparación de Monitoreo de SO** **2** **con Normativa. Estación MOLYB** . ...... 113

**Tabla 4-52. Resultados Monitoreo de MP10. Estación MOLYNOR.** .................................... 113

**Tabla 4-53. Comparación de Monitoreo de MP10 con Normativa. Estación MOLYNOR.**

.............................................................................................................................................................. 114

**Tabla 4-54. Resultados Monitoreo de NO** **2** **. Estación MOLYNOR.** ........................................ 114

**Tabla 4-55. Comparación de Monitoreo de NO** **2** **con Normativa. Estación MOLYNOR.** . 115

**Tabla 4-56. Resultados Monitoreo de SO** **2** **. Estación MOLYNOR.** ......................................... 116

**Tabla 4-57 - Comparación de Monitoreo de SO** **2** **con Normativa. Estación MOLYNOR.** 116

**Tabla 4-58. Resultados Monitoreo de MP10. Estación Subestación Eléctrica.** ................ 117

**Tabla 4-59. Comparación de Monitoreo de MP10. Estación Subestación Eléctrica.** ...... 117

**Tabla 4-60. Resultados Monitoreo de NO** **2** **. Estación Subestación Eléctrica.** .................... 118

**Tabla 4-61. Comparación de Monitoreo de NO** **2** **con Normativa. Estación Subestación**

**Eléctrica.** ............................................................................................................................................. 118

**Tabla 4-62. Resultados Monitoreo de SO2. Estación Subestación Eléctrica.** .................... 119

www.dfmconsultores.cl
vii
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-63. Comparación de Monitoreo de SO** **2** **con Normativa. Estación Subestación**

**Eléctrica.** ............................................................................................................................................. 120

**Tabla 4-64. Resumen Línea de Base de Calidad del Aire.** ....................................................... 121

**Tabla 4-65. Proyectos aprobados en el Sector de Mejillones y Alrededores.** .................. 122

**Tabla 4-66. Aportes Declarados por Proyectos Aprobados, No Ejecutados.** .................... 124

**Tabla 4-67. Línea de Base Proyectada.** ....................................................................................... 125

**Tabla 4-68. Receptores Discretos en la Modelación.** .............................................................. 126

**Tabla 4-69. Fuentes Emisoras Fase de Cierre.** ........................................................................... 129

**Tabla 4-70. Resultados de modelo de dispersión de MP2.5. Fase de Cierre.** ................... 132

**Tabla 4-71. Resultados de modelo de dispersión de MP10. Fase de Cierre.** .................... 136

**Tabla 4-72. Resultados de modelo de dispersión de NO** **2** **. Fase de Cierre.** ........................ 140

**Tabla 4-73. Resultados de modelo de dispersión de SO** **2** **. Fase de Cierre.** ......................... 144

**Tabla 4-74. Resultados de modelo de dispersión de SO** **2** **. Fase de Cierre.** ......................... 149

**Tabla 4-75. Resultados de modelo de dispersión de CO. Fase de Cierre.** .......................... 154

**Tabla 4-76. Resultados de modelo de dispersión de MPS. Fase de Cierre.** ....................... 157

**Tabla 4-77 - Concentración Total Esperada. Fase de Cierre.** ................................................ 160

**Tabla 9-1. Archivos de modelación entregados.** ...................................................................... 164

www.dfmconsultores.cl
viii
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

#### 1 INTRODUCCIÓN

El presente informe contiene la estimación de emisiones atmosféricas y la modelación de

dispersión de contaminantes de la Fase de Cierre del proyecto “Terminal de Mantención

Mejillones”, en adelante “TMM” o el Proyecto. Este informe es solicitado por “Antofagasta

Railway Company PLC”, en adelante “FCAB” o el Titular, para dar cumplimiento a los

requerimientos de las Autoridades presentados en el ICSARA en contexto de la evaluación

ambiental del Proyecto en el SEIA.

El Proyecto que se somete a evaluación denominado Terminal de Mantención Mejillones

(en adelante “el Proyecto” o “TMM”) consiste principalmente en la implementación talleres

e instalaciones complementarias que permitan la ejecución de labores de mantención de

los carros y locomotoras de la flota actual de FCAB, que transportan diversas cargas

mediante vías férreas existentes que tienen como origen y destino los terminales

marítimos: Puerto Angamos; Interacid; Puerto Mejillones - Terminal Acido; y Puerto

Mejillones - Terminal Granelero.

El Terminal de Mantención Mejillones (TMM) se conformará por tres sectores, los que

ocupan en conjunto una superficie aproximada de 34 ha.

La Fase de Cierre del Proyecto contempla las actividades de habilitación e instalación de

faenas, desenergización de las instalaciones, la detención y desconexión de equipos y

maquinarias, el desmantelamiento y desmontaje de instalaciones y equipos y la

restauración de la geoforma en caso de ser requerido.

Para la determinación de los factores de emisión se han utilizado las fórmulas propuestas

en el Informe Final “Servicio de recopilación y sistematización de factores de emisión al aire

para el Servicio de Evaluación Ambiental”, desarrollado por BS Consultores para el Servicio

de Evaluación Ambiental y publicado en Julio de 2015, complementadas con la “Guía para

la Estimación de Emisiones Atmosféricas en la Región Metropolitana”, desarrollada por la

SEREMI de Medio Ambiente de la Región Metropolitana, 2020, y factores de emisión

incluidos en el documento AP-42 Compilation of Air Polluntant Emission Factors, Volumen

1: Stationary Point and Area Sources, Fifth Edition de la US EPA.

www.dfmconsultores.cl
1
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Mediante el uso de los factores de emisión y la determinación de los niveles de actividad,

según la información contenida en la descripción del proyecto, se procede al cálculo de la

estimación de emisión de contaminantes atmosféricos para cada fase del proyecto, de

acuerdo con la metodología establecida en la “Guía para la Estimación de Emisiones

Atmosféricas en la Región Metropolitana”.

Con respecto al modelo de dispersión, en primer lugar, se presenta, el resumen de

emisiones asociada a los escenarios modelados, la descripción del modelo de calidad del

aire utilizado (CALPUFF) y la caracterización meteorológica del área del proyecto a partir de

los datos registrados en la estación JJ Latorre, en donde se muestran los valores de variables

meteorológicas de velocidad del viento, dirección del viento, temperatura, humedad

relativa y radiación solar.

Luego, se presentan los resultados de la modelación meteorológica con el software

_Weather Research and Forecasting Model_ (WRF) para la misma estación, para las variables

velocidad del viento, dirección del viento y temperatura. A su vez, a partir de los resultados

del modelo meteorológico, se muestran los valores modelados de meteorología de altura,

en específico la variable meteorológica altura de capa de mezcla.

Posteriormente, se realiza un análisis de incertidumbre cualitativo y cuantitativo para

comparar los datos observados y modelados con el objetivo de validar dicho modelo,

siguiendo los lineamientos establecidos en la “Guía para el Uso de Modelos de Calidad del

Aire en el SEIA”, del Servicio de Evaluación Ambiental.

Por otro lado, para cuantificar el estado actual de la calidad del aire en la zona, se presenta

la línea de base de calidad del aire, en donde se muestran las series de tiempo, resultados

de monitoreo y comparación con normativas primarias de calidad del aire para MP2,5,

MP10, NO 2, SO 2, CO y O 3 para las estaciones JJ Latorre, Jardín Infantil, Puerto Mejillones,

Ferrocarril, Angamos 1, MOLYB, MOLYNOR y Subestación Eléctrica, a partir de información

obtenida de diversas fuentes detalladas más adelante en este documento.

Seguidamente, se presentan los receptores discretos de interés para la modelación, los

cuales corresponden a las estaciones de monitoreo de calidad del aire presentadas en la

línea de base mencionadas anteriormente.

www.dfmconsultores.cl
2
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Tras ello, se presentan los diferentes escenarios de modelación propuestos con el detalle

de las fuentes emisoras, su ubicación geográfica y las tasas de emisión ingresadas para los

contaminantes MP2,5, MP10, MPS, NO 2, SO 2 y CO.

Posteriormente, se presentan los resultados de la modelación de dispersión de

contaminantes con el aporte del Proyecto en cada receptor de interés para todos los

contaminantes en cada escenario. Además, se presentan las curvas de isoconcentración

para visualizar el aporte del proyecto dentro de todo el dominio de modelación.

Considerando la línea de base, se presenta un análisis de la concentración total esperada,

que resulta de sumar a la línea base proyectada el aporte del proyecto en sus distintas

etapas, para así verificar potenciales aumentos en concentraciones en cada uno de los

receptores discretos.

Finalmente, se presentan las conclusiones más relevantes de este estudio.

#### 2 OBJETIVOS

**2.1** **Objetivo General**

Estimar las emisiones atmosféricas resultantes de la ejecución de la fase de cierre del

proyecto y evaluar el efecto que tendrán dichas emisiones atmosféricas sobre la calidad del

aire en los receptores de interés mediante el uso de un dispersión de contaminantes para

así cumplir con los requerimientos indicados en la Ley N° 19.300 de Bases Generales de

Medio Ambiente, sus modificaciones a través de la Ley N° 20.417 y el Reglamento del SEIA

D.S. N° 40/2013 en relación con los requisitos mínimos y criterios para realizar una

Evaluación de Impacto Ambiental de Ingreso al Sistema de Evaluación de Impacto

Ambiental (SEIA).

**2.2** **Objetivos Específicos**

Los objetivos específicos del presente informe se listan a continuación:

 - Identificar las fuentes de emisión atmosférica en base a la descripción del proyecto.

www.dfmconsultores.cl
3
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

 - Determinar los factores de emisión de acuerdo con la descripción del proyecto y la

metodología descrita.

 - Estimar las emisiones de material particulado y de gases de las fuentes de emisión

atmosférica identificadas en base a la descripción del proyecto.

 - Definir un dominio de modelación acorde a la magnitud del proyecto y a la capacidad

potencial que tengan los contaminantes de dispersar en la atmósfera, que a su vez

incluya a los receptores discretos de interés.

 - Presentar la caracterización de la meteorología en la zona donde se emplaza el

Proyecto, a partir de monitoreos obtenidos a partir de alguna estación cercana al

Proyecto.

 - Establecer la incertidumbre del modelo meteorológico WRF y su correcta aplicación

para utilizarlo como dato de entrada para la modelación de dispersión de

contaminantes con CALPUFF.

 - Presentar la línea de base de calidad del aire, con el objetivo de identificar la

situación actual de la zona en términos de calidad del aire, a partir de monitoreos

de contaminantes atmosféricos registrados por estaciones en la zona donde se

emplaza el Proyecto.

 - Identificar las principales fuentes de emisión asociadas al proyecto y

georreferenciarlas dentro del dominio de modelación.

 - Modelar la dispersión de contaminantes atmosféricos con CALPUFF para la fase de

cierre.

 - Establecer el aporte total en concentración de contaminantes atmosféricos para

cada escenario en todos los receptores de interés y presentar la concentración

esperada dentro del dominio de modelación a partir de curvas de isoconcentración

para cada contaminante.

www.dfmconsultores.cl
4
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

#### 3 INVENTARIO DE EMISIONES ATMOSFÉRICAS

**3.1** **Descripción de Metodología Utilizada**

El método para determinar las emisiones generadas por el proyecto corresponde a un

método indirecto. Las emisiones son estimadas en base a la utilización de factores de

emisión, el cual corresponde a una relación entre el contaminante emitido a la atmósfera y

los niveles de actividad, de acuerdo con la siguiente ecuación:

E i = Fe i - NA · (1− P i )

Donde:

E i = Emisión de la sustancia i .

Fe i = Factor de Emisión de la sustancia i.

NA = Nivel de Actividad

(1 - P i ) = Factor de corrección, P = eficiencia de control.

Los factores de emisión utilizados para el cálculo presentado a continuación corresponden

a aquellos aceptados por la Autoridad. En específico se utilizarán los factores de emisión

indicados en los siguientes documentos:

 - Informe final servicio de recopilación y sistematización de factores de emisión al

aire para el Servicio de Evaluación Ambiental, desarrollado por BS Consultores para

el Servicio de Evaluación Ambiental, publicado en Julio de 2015.

 - Guía para la Estimación de Emisiones Atmosféricas en la Región Metropolitana,

desarrollada por la SEREMI de Medio Ambiente de la Región Metropolitana,

publicada en 2020.

 - AP-42 Compilation of Air Polluntant Emission Factors, Volumen 1: Stationary Point

and Area Sources, Fifth Edition de la US EPA, y en el Informe Final Servicio de

Recopilación y Sistematización de Factores de Emisión al Aire para el SEIA.

www.dfmconsultores.cl
5
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

 - Emission Standards Reference Guide for Heavy-Duty and Nonroad EnginesEPA420-F-97-014 - September 1997.

Es necesario mencionar que para la estimación de emisiones de material particulado

sedimentable se han considerado las partículas totales en suspensión (PTS). De acuerdo a

lo establecido en el AP-42 Compilation of Air Polluntant Emission Factors, Volumen 1:

Stationary Point and Area Sources, Fifth Edition de la US EPA, las partículas con diámetros

iguales o menores a 30 m (MP30), son consideradas a menudo como sustituto de las PTS,

es por ello, que para la estimación de emisiones se ha considerado las emisiones de PTS

equivalente del MP30.

En la Tabla 3-1 se presenta el cronograma de la fase de cierre del proyecto:

www.dfmconsultores.cl
6
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

**Tabla 3-1. Cronograma Fase de Cierre.**

|Actividad|Mes 1|Col3|Mes 2|Col5|Mes 3|Col7|Mes 4|Col9|
|---|---|---|---|---|---|---|---|---|
|Habilitación Instalación de faenas|||||||||
|Desenergización de las instalaciones|||||||||
|Detención y desconexión de equipos y<br>maquinarias|||||||||
|Desmantelamiento y desmontaje de algunas<br>instalaciones y equipos|||||||||
|Restaurar geoforma en caso de aplicar|||||||||

Fuente: Ingeniería del Proyecto.

www.dfmconsultores.cl
7
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**3.2** **Fase de Cierre**

A continuación, se presentan los factores de emisión a utilizar, para posteriormente

presentar los niveles de actividad utilizados y las emisiones estimadas para cada una de las

actividades consideradas durante la fase de cierre del proyecto.

**3.2.1** **Factores de Emisión**

3.2.1.1 Movimientos de Tierra

En la Tabla 3-2 se presentan los factores de emisión utilizados para la estimación de

emisiones relacionadas a los movimientos de tierra durante la fase de cierre del proyecto:

www.dfmconsultores.cl
8
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

**Tabla 3-2 - Factores de Emisión Movimientos de Tierra - Fase de cierre.**

|Actividad|Ecuación Factor<br>de Emisión|Unidad|Referencia<br>Ecuación Factor de<br>Emisión|Parámetros Factores de Emisión|Col6|Col7|Col8|Col9|Factor de Emisión|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Ecuación Factor**<br>**de Emisión**|**Unidad**|**Referencia**<br>**Ecuación Factor de**<br>**Emisión**|**Variables**|**Referencias**|**Valor**<br>**MP2,5**|**Valor**<br>**MP10**|**Valor**<br>**MPS**|**MP2,5**|**MP10**|**MPS**|
|Excavaciones /<br>Relleno|Para MP2,5|kg/h|Punto 4.6, Informe<br>Final Servicio de<br>Recopilación y<br>Sistematización de<br>Factores de<br>Emisión al Aire<br>para el SEIA.|k: factor de<br>tamaño de<br>partícula|Table 11.9-2, Capítulo 11,<br>Sección 11.9"Western Surface<br>Coal Mining", AP-42|0,105|n/a|n/a|0,189|n/a|n/a|
|Excavaciones /<br>Relleno|2,6 · k · (s1,2/M1,3)|2,6 · k · (s1,2/M1,3)|2,6 · k · (s1,2/M1,3)|s: contenido de<br>finos (%)|Valor por defecto, Punto 4.6,<br>Informe Final Servicio de<br>Recopilación y Sistematización<br>de Factores de Emisión al Aire<br>para el SEIA.|6,9|n/a|n/a|n/a|n/a|n/a|
|Excavaciones /<br>Relleno|2,6 · k · (s1,2/M1,3)|2,6 · k · (s1,2/M1,3)|2,6 · k · (s1,2/M1,3)|M: humedad del<br>material (%)|Valor por defecto, Punto 4.6,<br>Informe Final Servicio de<br>Recopilación y Sistematización<br>de Factores de Emisión al Aire<br>para el SEIA.|7,9|n/a|n/a|n/a|n/a|n/a|
|Excavaciones /<br>Relleno|Para MP 10|kg/h|Punto 4.6, Informe<br>Final Servicio de<br>Recopilación y<br>Sistematización de<br>Factores de<br>Emisión al Aire<br>para el SEIA.|k: factor de<br>tamaño de<br>partícula|Table 11.9-2, Capítulo 11,<br>Sección 11.9"Western Surface<br>Coal Mining", AP-42|n/a|0,75|n/a|n/a|0,339|n/a|
|Excavaciones /<br>Relleno|0,45 · k ·<br>(s1,5/M1,4)|0,45 · k ·<br>(s1,5/M1,4)|0,45 · k ·<br>(s1,5/M1,4)|s: contenido de<br>finos (%)|Valor por defecto, Punto 4.6,<br>Informe Final Servicio de<br>Recopilación y Sistematización<br>de Factores de Emisión al Aire<br>para el SEIA.|n/a|6,9|n/a|n/a|n/a|n/a|
|Excavaciones /<br>Relleno|0,45 · k ·<br>(s1,5/M1,4)|0,45 · k ·<br>(s1,5/M1,4)|0,45 · k ·<br>(s1,5/M1,4)|M: humedad del<br>material (%)|Valor por defecto, Punto 4.6,<br>Informe Final Servicio de<br>Recopilación y Sistematización<br>de Factores de Emisión al Aire<br>para el SEIA.|n/a|7,9|n/a|n/a|n/a|n/a|
|Excavaciones /<br>Relleno|Para MPS|kg/h|Punto 4.6, Informe<br>Final Servicio de<br>Recopilación y<br>Sistematización de<br>Factores de<br>Emisión al Aire<br>para el SEIA.|k: factor de<br>tamaño de<br>partícula|Table 11.9-2, Capítulo 11,<br>Sección 11.9"Western Surface<br>Coal Mining", AP-42|n/a|n/a|1,0|n/a|n/a|1,798|
|Excavaciones /<br>Relleno|2,6 · k · (s1,2/M1,3)|2,6 · k · (s1,2/M1,3)|2,6 · k · (s1,2/M1,3)|s: contenido de<br>finos (%)|Valor por defecto, Punto 4.6,<br>Informe Final Servicio de<br>Recopilación y Sistematización<br>de Factores de Emisión al Aire<br>para el SEIA.|n/a|n/a|6,9|6,9|6,9|6,9|

www.dfmconsultores.cl
9
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

|Actividad|Ecuación Factor<br>de Emisión|Unidad|Referencia<br>Ecuación Factor de<br>Emisión|Parámetros Factores de Emisión|Col6|Col7|Col8|Col9|Factor de Emisión|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Ecuación Factor**<br>**de Emisión**|**Unidad**|**Referencia**<br>**Ecuación Factor de**<br>**Emisión**|**Variables**|**Referencias**|**Valor**<br>**MP2,5**|**Valor**<br>**MP10**|**Valor**<br>**MPS**|**MP2,5**|**MP10**|**MPS**|
|**Actividad**|**Ecuación Factor**<br>**de Emisión**|**Unidad**|**Referencia**<br>**Ecuación Factor de**<br>**Emisión**|M: humedad del<br>material (%)|Valor por defecto, Punto 4.6,<br>Informe Final Servicio de<br>Recopilación y Sistematización<br>de Factores de Emisión al Aire<br>para el SEIA.|n/a|n/a|7,9||||
|Transferencia de<br>Material<br>(Carga/Descarga)|0,0016 · k ·<br>(U/2,2)1,3 /<br>(M/2)1,4|kg/t|Punto 3.4, Informe<br>Final Servicio de<br>Recopilación y<br>Sistematización de<br>Factores de<br>Emisión al Aire<br>para el SEIA.|k: Factor tamaño<br>de partícula|Punto 3.4, Informe Final Servicio<br>de Recopilación y<br>Sistematización de Factores de<br>Emisión al Aire para el SEIA.|0,053|0,35|0,74|1,39,E-05|9,16,E-05|1,94,E-04|
|Transferencia de<br>Material<br>(Carga/Descarga)|0,0016 · k ·<br>(U/2,2)1,3 /<br>(M/2)1,4|kg/t|Punto 3.4, Informe<br>Final Servicio de<br>Recopilación y<br>Sistematización de<br>Factores de<br>Emisión al Aire<br>para el SEIA.|U: Velocidad del<br>viento (m/s)|Valor promedio, trienio 2018-<br>2020, estación JJ Latorre|2,40|2,40|2,40|2,40|2,40|2,40|
|Transferencia de<br>Material<br>(Carga/Descarga)|0,0016 · k ·<br>(U/2,2)1,3 /<br>(M/2)1,4|kg/t|Punto 3.4, Informe<br>Final Servicio de<br>Recopilación y<br>Sistematización de<br>Factores de<br>Emisión al Aire<br>para el SEIA.|M: Humedad del<br>material (%)|Punto 3.4, Informe Final Servicio<br>de Recopilación y<br>Sistematización de Factores de<br>Emisión al Aire para el SEIA.|7,9|7,9|7,9|7,9|7,9|7,9|

Fuente: Elaboración propia, en base a ingeniería del Proyecto.

www.dfmconsultores.cl
10
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

3.2.1.2 Operación de Maquinaria

En la Tabla 3-3 se presentan los factores de emisión utilizados para estimar las emisiones de los contaminantes MP2.5, MP10, MPS,

CO, NO x y HC, asociadas a la utilización de maquinaria durante la fase de cierre del proyecto:

**Tabla 3-3 - Factores de Emisión Maquinaria - Fase de Cierre.**

|Maquinaria|C:% carga<br>del motor *|Potencia<br>Nominal [kW]<br>*|Factor según potencia [g/kW-h]|Col5|Col6|Col7|Col8|Col9|Col10|Factor de Emisión según Potencia [kg/h]|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Maquinaria**|**C:% carga**<br>**del motor ***|**Potencia**<br>**Nominal [kW]**<br>*** **|**MP2.5**|**MP10**|**MPS**|**CO**|**NOx**|**HC**|**Referencia**|**MP2.5**|**MP10**|**MPS**|**CO**|**NOx**|**HC**|
|Retroexcavadora|21%|66,00|1,51|1,51|1,51|5,06|14,36|2,33|Tabla 4.10 Guía para la estimación de emisiones<br>atmosféricas de proyectos Inmobiliarios para la<br>Región Metropolitana|0,021|0,021|0,021|0,070|0,199|0,032|
|Motoniveladora|59%|149,00|1,10|1,10|1,10|3,00|14,36|1,35|Tabla 4.10 Guía para la estimación de emisiones<br>atmosféricas de proyectos Inmobiliarios para la<br>Región Metropolitana|0,097|0,097|0,097|0,264|1,262|0,119|
|Rodillo<br>compactador|55%|206,00|1,10|1,10|1,10|3,00|14,36|1,35|Tabla 4.10 Guía para la estimación de emisiones<br>atmosféricas de proyectos Inmobiliarios para la<br>Región Metropolitana|0,125|0,125|0,125|0,340|1,627|0,153|
|Cargador Frontal|58%|151,00|1,10|1,10|1,10|3,00|14,36|1,35|Tabla 4.10 Guía para la estimación de emisiones<br>atmosféricas de proyectos Inmobiliarios para la<br>Región Metropolitana|0,096|0,096|0,096|0,263|1,258|0,118|
|Camión Tolva|47%|103,00|1,23|1,23|1,23|3,76|14,36|1,72|Tabla 4.10 Guía para la estimación de emisiones<br>atmosféricas de proyectos Inmobiliarios para la<br>Región Metropolitana|0,060|0,060|0,060|0,182|0,695|0,083|
|Camión Grúa|47%|164,12|1,10|1,10|1,10|3,00|14,36|1,35|Tabla 4.10 Guía para la estimación de emisiones<br>atmosféricas de proyectos Inmobiliarios para la<br>Región Metropolitana|0,085|0,085|0,085|0,231|1,108|0,104|

Fuente: Elaboración propia, en base a ingeniería del Proyecto.

www.dfmconsultores.cl
11
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

En la Tabla 3-4 se presentan los factores de emisión utilizados para estimar las emisiones asociadas a la utilización de grupos

electrógenos:

**Tabla 3-4 - Factores de Emisión Grupos Electrógenos - Fase de Cierre.**

|Tipo de<br>Maquinaria|Unidad|Referencia<br>Ecuación Factor<br>de Emisión|Factor de Emisión (kg/kg comb.)|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Tipo de**<br>**Maquinaria**|**Unidad**|**Referencia**<br>**Ecuación Factor**<br>**de Emisión**|**MP2.5**|**MP10**|**MPS**|**CO**|**NOx**|**SOx**|**COV**|
|Grupo<br>Electrógeno<br>(Diesel hasta 600<br>hp)|kg/kg comb.|Tabla 3.21.<br>Factores de<br>emisión grupos<br>electrógenos.<br>Guía para la<br>estimación de<br>emisiones<br>atmosféricas en<br>la RM 2019.|0,006|0,006|0,006|0,019|0,086|0,006|0,007|

Fuente: Elaboración propia, en base a ingeniería del Proyecto.

www.dfmconsultores.cl
12
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

3.2.1.3 Tránsito Vehicular

En la Tabla 3-5 se presentan los factores de emisión utilizados para estimar las emisiones asociadas a la resuspensión de polvo generada

por el tránsito vehicular asociado al proyecto en su fase de cierre para caminos pavimentados.

**Tabla 3-5 - Factores de Emisión Resuspensión de Polvo - Fase de Cierre.**

|Actividad|Ecuación Factor de<br>Emisión|Unidad|Referencia Ecuación<br>Factor de Emisión|Parámetros Factores de Emisión|Col6|Col7|Col8|Col9|Factor de Emisión|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Ecuación Factor de**<br>**Emisión**|**Unidad**|**Referencia Ecuación**<br>**Factor de Emisión**|**Variables**|**Referencias**|**MP2,5**|**MP10**|**MPS**|**MP2,5**|**MP10**|**MPS**|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 1)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|k: factor de tamaño<br>de partícula|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,15|0,62|3,23|0,42|1,73|9,01|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 1)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|sL: contenido de<br>finos (g/m2)|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,3|0,3|0,3|0,3|0,3|0,3|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 1)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|W: peso promedio<br>de la flota que<br>circula por la vía<br>(ton)|Valor por defecto, Guía para la<br>Estimación de Emisiones<br>Atmosféricas para la Región<br>Metropolitana.|8,00|8,00|8,00|8,00|8,00|8,00|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 2)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|k: factor de tamaño<br>de partícula|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,15|0,62|3,23|0,90<br> <br>|3,74<br> <br>|19,47<br> <br>|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 2)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|sL: contenido de<br>finos (g/m2)|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,7|0,7|0,7|0,7|0,7|0,7|

www.dfmconsultores.cl
13
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

|Actividad|Ecuación Factor de<br>Emisión|Unidad|Referencia Ecuación<br>Factor de Emisión|Parámetros Factores de Emisión|Col6|Col7|Col8|Col9|Factor de Emisión|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Ecuación Factor de**<br>**Emisión**|**Unidad**|**Referencia Ecuación**<br>**Factor de Emisión**|**Variables**|**Referencias**|**MP2,5**|**MP10**|**MPS**|**MP2,5**|**MP10**|**MPS**|
|**Actividad**|**Ecuación Factor de**<br>**Emisión**|**Unidad**|**Referencia Ecuación**<br>**Factor de Emisión**|W: peso promedio<br>de la flota que<br>circula por la vía<br>(ton)|Valor por defecto, Guía para la<br>Estimación de Emisiones<br>Atmosféricas para la Región<br>Metropolitana.|8,00|8,00|8,00||||
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 3)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|k: factor de tamaño<br>de partícula|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,15|0,62|3,23|0,90|3,74|19,47|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 3)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|sL: contenido de<br>finos (g/m2)|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,7|0,7|0,7|0,7|0,7|0,7|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 3)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|W: peso promedio<br>de la flota que<br>circula por la vía<br>(ton)|Valor por defecto, Guía para la<br>Estimación de Emisiones<br>Atmosféricas para la Región<br>Metropolitana.|8,00|8,00|8,00|8,00|8,00|8,00|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 4)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|k: factor de tamaño<br>de partícula|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,15|0,62|3,23|0,90|3,74|19,47|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 4)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|sL: contenido de<br>finos (g/m2)|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,7|0,7|0,7|0,7|0,7|0,7|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 4)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|W: peso promedio<br>de la flota que<br>circula por la vía<br>(ton)|Valor por defecto, Guía para la<br>Estimación de Emisiones<br>Atmosféricas para la Región<br>Metropolitana.|8,00|8,00|8,00|8,00|8,00|8,00|
|Tránsito Vehículos<br>camino pavimentado|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de|k: factor de tamaño<br>de partícula|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores|0,15|0,62|3,23|0,90|3,74|19,47|

www.dfmconsultores.cl
14
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

|Actividad|Ecuación Factor de<br>Emisión|Unidad|Referencia Ecuación<br>Factor de Emisión|Parámetros Factores de Emisión|Col6|Col7|Col8|Col9|Factor de Emisión|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Ecuación Factor de**<br>**Emisión**|**Unidad**|**Referencia Ecuación**<br>**Factor de Emisión**|**Variables**|**Referencias**|**MP2,5**|**MP10**|**MPS**|**MP2,5**|**MP10**|**MPS**|
|Vehículos Pesados<br>**(Tramo 5)**|||Factores de Emisión al<br>Aire para el SEIA.||de Emisión al Aire para el<br>SEIA.|||||||
|Vehículos Pesados<br>**(Tramo 5)**|||Factores de Emisión al<br>Aire para el SEIA.|sL: contenido de<br>finos (g/m2)|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,7|0,7|0,7|0,7|0,7|0,7|
|Vehículos Pesados<br>**(Tramo 5)**|||Factores de Emisión al<br>Aire para el SEIA.|W: peso promedio<br>de la flota que<br>circula por la vía<br>(ton)|Valor por defecto, Guía para la<br>Estimación de Emisiones<br>Atmosféricas para la Región<br>Metropolitana.|8,00|8,00|8,00|8,00|8,00|8,00|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 6)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|k: factor de tamaño<br>de partícula|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,15|0,62|3,23|0,90|3,74|19,47|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 6)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|sL: contenido de<br>finos (g/m2)|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,7|0,7|0,7|0,7|0,7|0,7|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 6)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|W: peso promedio<br>de la flota que<br>circula por la vía<br>(ton)|Valor por defecto, Guía para la<br>Estimación de Emisiones<br>Atmosféricas para la Región<br>Metropolitana.|8,00|8,00|8,00|8,00|8,00|8,00|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 7)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|k: factor de tamaño<br>de partícula|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,15|0,62|3,23|0,90|3,74|19,47|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 7)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|sL: contenido de<br>finos (g/m2)|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,7|0,7|0,7|0,7|0,7|0,7|

www.dfmconsultores.cl
15
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

|Actividad|Ecuación Factor de<br>Emisión|Unidad|Referencia Ecuación<br>Factor de Emisión|Parámetros Factores de Emisión|Col6|Col7|Col8|Col9|Factor de Emisión|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Ecuación Factor de**<br>**Emisión**|**Unidad**|**Referencia Ecuación**<br>**Factor de Emisión**|**Variables**|**Referencias**|**MP2,5**|**MP10**|**MPS**|**MP2,5**|**MP10**|**MPS**|
|**Actividad**|**Ecuación Factor de**<br>**Emisión**|**Unidad**|**Referencia Ecuación**<br>**Factor de Emisión**|W: peso promedio<br>de la flota que<br>circula por la vía<br>(ton)|Valor por defecto, Guía para la<br>Estimación de Emisiones<br>Atmosféricas para la Región<br>Metropolitana.|8,00|8,00|8,00||||
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 8)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|k: factor de tamaño<br>de partícula|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,15|0,62|3,23|0,90|3,74|19,47|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 8)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|sL: contenido de<br>finos (g/m2)|Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA.|0,7|0,7|0,7|0,7|0,7|0,7|
|Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 8)**|k x (sL)0,91 x (W)1,02|g/km|Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA.|W: peso promedio<br>de la flota que<br>circula por la vía<br>(ton)|Valor por defecto, Guía para la<br>Estimación de Emisiones<br>Atmosféricas para la Región<br>Metropolitana.|8,00|8,00|8,00|8,00|8,00|8,00|

Fuente: Elaboración propia, en base a ingeniería del Proyecto.

En la Tabla 3-6 se presentan los factores de emisión calculados para estimar las emisiones asociadas a la combustión por el tránsito

vehicular:

**Tabla 3-6 - Factores de Emisión Combustión por Tránsito Vehicular - Fase de Cierre.**

|Tipo de Vehículo|Tecnología|Referencia|MP2,5|MP10|MPS|CO|NOx|COV|SO2|NH3|CC|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo de Vehículo**|**Tecnología**|**Referencia**|**g/km**|**g/km**|**g/km**|**g/km**|**g/km**|**g/km**|**g/km**|**g/km**|**g/km**|
|Diesel 7.5-16t|Euro III|EMEP/EEA air pollutant<br>emission inventory guidebook<br>2019. Cap 1.A.3.b.I-IV.|0,088|0,088|0,088|0,972|4,300|0,189|0,005|0,003|155|
|Diesel 16-32t|Euro III|EMEP/EEA air pollutant<br>emission inventory guidebook<br>2019. Cap 1.A.3.b.I-IV.|0,130|0,130|0,130|1,490|6,270|0,278|0,006|0,003|210|

www.dfmconsultores.cl
16
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

|Tipo de Vehículo|Tecnología|Referencia|MP2,5|MP10|MPS|CO|NOx|COV|SO2|NH3|CC|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo de Vehículo**|**Tecnología**|**Referencia**|**g/km**|**g/km**|**g/km**|**g/km**|**g/km**|**g/km**|**g/km**|**g/km**|**g/km**|
|Diesel >32t|Euro III|EMEP/EEA air pollutant<br>emission inventory guidebook<br>2019. Cap 1.A.3.b.I-IV.|0,151|0,151|0,151|1,790|7,430|0,308|0,008|0,003|251|
|Urban Buses<br>Standard|Euro III - 2000|EMEP/EEA air pollutant<br>emission inventory guidebook<br>2019. Cap 1.A.3.b.I-IV.|0,207|0,207|0,207|2,670|9,380|0,409|0,009|0,003|301|
|Camioneta Diesel<br>Medium|Euro III|EMEP/EEA air pollutant<br>emission inventory guidebook<br>2019. Cap 1.A.3.b.I-IV.|0,039|0,039|0,039|0,089|0,773|0,020|0,000|0,001|55|

Fuente: Elaboración propia, en base a ingeniería del Proyecto.

www.dfmconsultores.cl
17
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**3.2.2** **Niveles de Actividad**

A continuación, se describen los niveles de actividad utilizados para la estimación de

emisiones de la fase de cierre del proyecto, para cada una de las actividades consideradas.

Para determinar los niveles de actividad asociados al proyecto se han utilizado las siguientes

consideraciones:

 - Para las actividades de compactado se utilizó como rendimiento el valor referencial

obtenido de la Guía para la Estimación de Emisiones de Proyectos Inmobiliarios RM,

Seremi de Medio Ambiente 2012, el cual indica que para 1 hectárea se recorre una

distancia de 3,57 km.

 - Para las actividades de excavación se ha considerado como rendimiento el valor

referencial obtenido de la Guía para la Estimación de Emisiones de Proyectos

Inmobiliarios RM, Seremi de Medio Ambiente 2012, el cual indica que una pala de 1

m [3] posee un rendimiento igual a 30 m [3] /hora.

 - Para las actividades de compactación se utilizó una velocidad de compactación de 3

km/h y 4 viajes por compactación.

 - La densidad considerada para el material es de 1,8 t/m [3 (1)] .

1 G. Baud (1994), “Tecnología de la Construcción”. Editorial Blume, Capítulo V - Los Movimientos de Tierra,
página 71.

www.dfmconsultores.cl
18
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

3.2.2.1 Movimientos de Tierra

En la Tabla 3-7 se presentan los niveles de actividad asociados a los movimientos de tierra
por excavación:

**Tabla 3-7. Niveles de actividad asociados a movimientos de tierra por Excavación. Fase de Cierre.**

|Actividad|Fuente|Volumen de excavación|Col4|Horas de excavación|Col6|
|---|---|---|---|---|---|
|**Actividad**|**Fuente**|**Valor Fase Cierre**|**Unidad**|**Fase Cierre**|**Unidad**|
|Excavaciones|Excavación de Corte/Escarpe|19.577|m3|653|h/año|

Fuente: Elaboración propia, en base a ingeniería del Proyecto.

En la Tabla 3-8 se presentan los niveles de actividad asociados a los movimientos de tierra
por compactado:

**Tabla 3-8. Niveles de actividad asociados a movimientos de tierra por Compactado. Fase de Cierre.**

|Actividad|Fuente|Volumen de excavación|Col4|Horas de compactación|Col6|
|---|---|---|---|---|---|
|**Actividad**|**Fuente**|**Valor Fase Cierre**|**Unidad**|**Fase Cierre**|**Unidad**|
|Compactación|Superficie Total de Proyecto|485,52|KVT|161,84|h/año|

Fuente: Elaboración propia, en base a ingeniería del Proyecto.

Finalmente, en la Tabla 3-9 se presentan los niveles de actividad asociados a los
movimientos de tierra por transferencia de material:

**Tabla 3-9. Niveles de actividad asociados a movimientos de tierra por Transferencia de Material. Fase de**

**Cierre.**

|Actividad|Fuente|Volumen de material a transferir|Col4|Peso de material a transferir|Col6|
|---|---|---|---|---|---|
|**Actividad**|**Fuente**|**Valor Fase Cierre**|**Unidad**|**Fase Cierre**|**Unidad**|
|Carga/Descarga de<br>material|Excavaciones|39.154|m3|70.477|t/año|

Fuente: Elaboración propia, en base a ingeniería del Proyecto.

www.dfmconsultores.cl
19
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

3.2.2.2 Operación de Maquinaria

En la Tabla 3-10 y la Tabla 3-11 se presentan las maquinarias y grupos electrógenos

respectivamente, asociados al proyecto en su fase de cierre:

**Tabla 3-10 - Maquinaria Utilizada - Fase de Cierre.**

|Maquinaria|Función|Cantidad|Potencia [kW]|Horas totales [h]|
|---|---|---|---|---|
|Retroexcavadora|Movimiento de Tierra|1|66,0|250|
|Motoniveladora|Restauración Geoforma|1|149,0|350|
|Rodillo compactador|Restauración Geoforma|2|206,0|650|
|Cargador Frontal|Movimiento de Tierra|1|151,0|100|
|Camión Tolva|Movimiento de Tierra|2|103,0|450|
|Camión Grúa|Desmantelación|1|164,1|336|
|**Total**|**Total**|**Total**|**Total**|**2.136**|

Fuente: Elaboración propia, en base a ingeniería del Proyecto.

**Tabla 3-11. Grupos Electrógenos Utilizados - Fase de Cierre.**

|Grupo electrógeno|Función|Cantidad|Potencia<br>aparente<br>[kVA]|Potencia<br>[kW]|Consumo<br>[kW-h]|Consumo [kg<br>comb/año]|
|---|---|---|---|---|---|---|
|Grupo electrógeno 20 kVA|Frente de trabajo|1|20,0|16,0|16.8962|4.227|

Fuente: Elaboración propia, en base a ingeniería del Proyecto.

2 Descripción del Proyecto: Se considera un régimen de operación de 4 meses por 12 horas al día, 22 días
hábiles por mes.

www.dfmconsultores.cl
20
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

3.2.2.3 Tránsito Vehicular

Para la definir niveles de actividad del tránsito vehicular del proyecto, se consideró la

cantidad de vehículos a utilizar para cada actividad. Adicionalmente, se estimó la cantidad

de kilómetros a recorrer para cada vehículo, la información detallada se presenta en las

siguientes tablas.

En la Tabla 3-12 se presentan los tramos considerados para estimar los niveles de actividad

del tránsito vehicular. Mientras que en la siguiente figura se presenta la localización de los

tramos mencionados.

**Tabla 3-12 - Tramos de los caminos del proyecto.**

|Tramo|Descripción|Desde|Hasta|Tipo|Longitud<br>(km)|
|---|---|---|---|---|---|
|Tramo 1|Acceso y Transito<br>Principal|Antofagasta|Empalme Ruta B-262|Pavimentado|63,40|
|Tramo 2|Ruta B-262 desde Ruta<br>1 a Quinta Industrial|Empalme Ruta B-262 (R-1)|Empalme Ruta B-262 Av.<br>Quinta Industrial (Km<br>7.4)|Pavimentado|5,10|
|Tramo 3|Acceso TMM|Empalme Av. Quinta<br>Industrial|Acceso TMM|Pavimentado|1,00|
|Tramo 4|Ruta B-262 hasta cruce<br>Compañía de<br>Fertilizantes|Empalme Ruta B-262 Av.<br>Quinta Industrial (Km 7.4)|Empalme Ruta B-262<br>Compañía de<br>Fertilizantes|Pavimentado|5,97|
|Tramo 5|Ruta B-262 cruce<br>Compañía de<br>Fertilizantes hasta<br>Centro Mejillones|Empalme Ruta B-262<br>Compañía de Fertilizantes|Centro Mejillones|Pavimentado|1,29|
|Tramo 6|Transporte Personal-<br>Insumos-Residuos|Empalme Ruta B-262<br>Compañía de Fertilizantes|Empalme Ruta B-272|Pavimentado|1,42|
|Tramo 7|Transporte Personal-<br>Insumos-Residuos|Ruta B-272|Empalme Acceso<br>Vertedero|Pavimentado|2,85|
|Tramo 8|Transporte Personal-<br>Insumos-Residuos|Empalme Acceso Vertedero|Vertedero|Pavimentado|2,16|

Fuente: Elaboración propia, en base a ingeniería del Proyecto.

www.dfmconsultores.cl
21
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 3-1. Tramos considerados para la Estimación de Emisiones de la Fase de Cierre.**

Fuente: Elaboración propia, en base a ingeniería del Proyecto.

www.dfmconsultores.cl
22
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 3-2. Tramos considerados para la Estimación de Emisiones de la Fase de Cierre. Zoom Sector**

**Proyecto.**

Fuente: Elaboración propia, en base a ingeniería del Proyecto.

www.dfmconsultores.cl
23
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes

Atmosféricos

Marzo 2023

La Tabla 3-13 muestra los tramos que se recorren para cada propósito asociado a la fase de cierre del proyecto:

**Tabla 3-13. Movimientos vehiculares para cada tramo. Fase de cierre.**

|Actividad|Tipo de vehículo Proyecto|Vehículo Standard|Cantidad de meses|Peso Promedio|Viajes Fase de<br>Cierre|Origen - destino|
|---|---|---|---|---|---|---|
|**Actividad**|**Tipo de vehículo Proyecto**|**Vehículo Standard**|**Cantidad de meses**|**(t)**|**(t)**|**(t)**|
|Transporte de Insumos|Camión Contenedor 20 pies|Diesel 16-32t|4|25,0|96|Antofagasta o Mejillones - TMM|
|Transporte de Combustible|Camión Cisterna|Diesel 16-32t|4|25,0|32|Antofagasta o Mejillones - TMM|
|Transporte de Residuos Domiciliarios|Camión Tolva 16t|Diesel 7.5-16t|4|10,0|32|TMM - Vertedero|
|Transporte de Residuos Industriales|Camión Tolva 16t|Diesel 7.5-16t|4|10,0|32|Antofagasta o Mejillones - TMM|
|Transporte de Residuos Peligrosos|Camión Tolva 16t|Diesel 7.5-16t|4|10,0|8,0|Antofagasta o Mejillones - TMM|
|Transporte Personal desde Mejillones|Bus para 30 personas|Urban Buses Standard|4|16,0|88|Mejillones - TMM|
|Transporte Personal desde Antofagasta|Bus para 30 personas|Urban Buses Standard|4|16,0|88|Antofagasta - TMM|

Fuente: Elaboración propia, en base a ingeniería del Proyecto.

www.dfmconsultores.cl
24
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes

Atmosféricos

Marzo 2023

En las siguientes tablas, se presentan los viajes totales para cada actividad de transporte asociada a la fase de cierre, los cuales fueron

calculados considerando la frecuencia de viajes de la tabla anterior y tomando en cuenta que cada tránsito vehicular es ida y vuelta,

con este valor y la distancia de cada tramo se calcula la distancia total a recorrer para cada tramo:

**Tabla 3-14. Distancias por recorrer en cada tramo - Fase de Cierre.**

|Actividad|Tramo 1|Tramo 2|Tramo 3|Tramo 4|Tramo 5|Tramo 6|Tramo 7|Tramo 8|Total<br>Pavimentado<br>(km)|Total|
|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**(km)**|**(km)**|**(km)**|**(km)**|**(km)**|**(km)**|**(km)**|**(km)**|**(km)**|**(km)**|
|Transporte de Insumos|12.173|979|192||||||13.344|13.344|
|Transporte de Combustible|4.058|326|64||||||4.448|4.448|
|Transporte de Residuos Domiciliarios|||64|382||91|182|138|858|858|
|Transporte de Residuos Industriales|4.058|326|64||||||4.448|4.448|
|Transporte de Residuos Peligrosos|1.014|82|16||||||1.112|1.112|
|Transporte Personal desde Mejillones|||176|1.051|227||||1.454|1.454|
|Transporte Personal desde<br>Antofagasta|11.158|898|176||||||12.232|12.232|
|**Total**|**32.461**|**2.611**|**752**|**1.433**|**227**|**91**|**182**|**138**|**37.895**|**37.895**|

Fuente: Elaboración Propia.

www.dfmconsultores.cl
25
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes

Atmosféricos

Marzo 2023

**3.2.3** **Emisiones**

A continuación, se presentan las emisiones de la fase de cierre del proyecto, para cada una de las actividades consideradas.

3.2.3.1 Movimientos de Tierra

En la Tabla 3-15 se presentan las emisiones asociadas a los movimientos de tierra por excavación, compactado y transferencia de

material, respectivamente, asociadas a la ejecución de la fase de cierre:

**Tabla 3-15 - Emisiones por movimientos de tierra. Fase de Cierre.**

|Identificación Fuente|Factor de Emisión|Col3|Col4|Col5|Nivel de Actividad|Col7|Emisión Cierre (t/año)|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Identificación Fuente**|**MP2.5**|**MP10**|**MPS**|**Unidad**|**Cantidad**|**Unidad**|**MP2.5**|**MP10**|**MPS**|
|Excavación|0,189|0,339|1,798|kg/h|652,57|h/año|0,123|0,221|1,173|
|Compactado|0,189|0,339|1,798|kg/h|161,84|h/año|0,031|0,055|0,291|
|Transferencia de material (carga/descarga)|1,39,E-05|9,16,E-05|1,94,E-04|kg/t|70.477,20|t/año|0,001|0,006|0,014|
|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**0,155**|**0,282**|**1,478**|

Fuente: Elaboración propia.

www.dfmconsultores.cl
26
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes

Atmosféricos

Marzo 2023

3.2.3.2 Operación de Maquinaria

En la Tabla 3-16 se presentan las emisiones estimadas para las actividades asociadas a utilización de maquinaria para la fase de cierre.

Para la estimación de emisiones se ha considerado el escenario más conservador que corresponde a que todo el material particulado

generado por el proceso de combustión es material particulado respirable fino.

**Tabla 3-16 - Emisiones Utilización de Maquinaria. Fase de Cierre.**

|Maquinaria|Cantidad|Factor de Emisión (kg/h maquinaria)|Col4|Col5|Col6|Col7|Col8|Nivel de Actividad|Emisión (t/año) (Año1)|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Maquinaria**|**Cantidad**|**MP2.5**|**MP10**|**MPS**|**CO**|**NOx**|**HC**|**Uso (h/año)**|**MP2.5**|**MP10**|**MPS**|**CO**|**NOx**|**HC**|
|Retroexcavadora|1|0,021|0,021|0,021|0,070|0,199|0,032|250|0,005|0,005|0,005|0,018|0,050|0,008|
|Motoniveladora|1|0,097|0,097|0,097|0,264|1,262|0,119|350|0,034|0,034|0,034|0,092|0,442|0,042|
|Rodillo compactador|2|0,125|0,125|0,125|0,340|1,627|0,153|650|0,081|0,081|0,081|0,221|1,058|0,099|
|Cargador Frontal|1|0,096|0,096|0,096|0,263|1,258|0,118|100|0,010|0,010|0,010|0,026|0,126|0,012|
|Camión Tolva|2|0,060|0,060|0,060|0,182|0,695|0,083|450|0,027|0,027|0,027|0,082|0,313|0,037|
|Camión Grúa|1|0,085|0,085|0,085|0,231|1,108|0,104|336|0,029|0,029|0,029|0,078|0,372|0,035|
|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**0,185**|**0,185**|**0,185**|**0,517**|**2,360**|**0,233**|

Fuente: Elaboración propia.

www.dfmconsultores.cl
27
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes

Atmosféricos

Marzo 2023

En la Tabla 3-17 se presentan las emisiones asociadas a la utilización de grupos electrógenos para la fase de cierre.

**Tabla 3-17 - Emisiones Utilización de Grupos Electrógenos. Fase de Cierre.**

|Grupo electrógeno|P: potencia<br>nominal<br>(kW)|Factor de Emisión (kg/kg comb.)|Col4|Col5|Col6|Col7|Col8|Col9|Nivel de Actividad|Emisión (t/año)|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Grupo electrógeno**|**P: potencia**<br>**nominal**<br>**(kW)**|**MP2.5**|**MP10**|**MPS**|**CO**|**NOx**|**SOx**|**COV**|**Uso (kg. comb./año)**|**MP2.5**|**MP10**|**MPS**|**CO**|**NOx**|**SOx**|**COV**|
|Grupo electrógeno 20 kVA|16|0,006|0,006|0,006|0,019|0,086|0,006|0,007|4.227|0,026|0,026|0,026|0,079|0,366|0,024|0,030|
|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**0,026**|**0,026**|**0,026**|**0,079**|**0,366**|**0,024**|**0,030**|

Fuente: Elaboración propia.

www.dfmconsultores.cl
28
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes

Atmosféricos

Marzo 2023

3.2.3.3 Tránsito Vehicular

En la siguiente tabla, se presentan las emisiones de material particulado estimadas por la resuspensión de polvo en caminos

pavimentados para la fase de cierre, asociadas al tránsito vehicular del proyecto:

**Tabla 3-18 - Emisiones Producto de Resuspensión del Polvo. Fase de Cierre.**

|Tramo|Factor de Emisión (g/KVT)|Col3|Col4|Distancia Total Recorrida (km/año)|Porcentaje de Control (%)|Emisión (t/año) - Cierre|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Tramo**|**MP2.5**|**MP10**|**MPS**|**MPS**|**MPS**|**MP2.5**|**MP10**|**MPS**|
|Tramo 1|0,42|1,73|9,01|32.461|0%|0,014|0,056|0,292|
|Tramo 2|0,90|3,74|19,47|2.611|0%|0,002|0,010|0,051|
|Tramo 3|0,90|3,74|19,47|752|0%|0,001|0,003|0,015|
|Tramo 4|0,90|3,74|19,47|1.433|0%|0,001|0,005|0,028|
|Tramo 5|0,90|3,74|19,47|227|0%|0,000|0,001|0,004|
|Tramo 6|0,90|3,74|19,47|91|0%|0,000|0,000|0,002|
|Tramo 7|0,90|3,74|19,47|182|0%|0,000|0,001|0,004|
|Tramo 8|0,90|3,74|19,47|138|0%|0,000|0,001|0,003|
|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**0,018**|**0,076**|**0,398**|

Fuente: Elaboración propia.

www.dfmconsultores.cl
29
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes

Atmosféricos

Marzo 2023

En la Tabla 3-19 se presentan las emisiones de gases estimadas por combustión producto del tránsito vehicular para la fase de cierre:

**Tabla 3-19 - Emisiones Producto de Combustión Vehicular. Fase de Cierre.**

|Tipo de vehículo|Factor de Emisión (g/KVT)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Distancia Total<br>Recorrida - Cierre<br>(km/año)|Emisión (t/año)|Col12|Col13|Col14|Col15|Col16|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo de vehículo**|**MP2.5**|**MP10**|**MPS**|**CO**|**NOx **|**HC**|**SO2 **|**NH3 **|**NH3 **|**MP2.5**|**MP10**|**MPS**|**CO**|**NOx**|**HC**|**SO2 **|**NH3 **|
|Diesel 7.5-16t|0,088|0,088|0,088|0,972|4,300|0,189|0,005|0,003|6.418|0,001|0,001|0,001|0,006|0,028|0,001|2,98,E-05|1,86,E-05|
|Diesel 16-32t|0,130|0,130|0,130|1,490|6,270|0,278|0,006|0,003|17.792|0,002|0,002|0,002|0,027|0,112|0,005|1,12,E-04|5,16,E-05|
|Urban Buses Standard|0,207|0,207|0,207|2,670|9,380|0,409|0,009|0,003|13.686|0,003|0,003|0,003|0,037|0,128|0,006|1,24,E-04|3,97,E-05|
|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**0,006**|**0,006**|**0,006**|**0,069**|**0,268**|**0,012**|**2,66,E-04**|**1,10,E-04**|

Fuente: Elaboración propia.

www.dfmconsultores.cl
30
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención**

**Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**3.2.4** **Resumen de Emisiones Fase de Cierre**

En la siguiente tabla, se presenta el resumen de emisiones estimadas para la fase de cierre

del proyecto:

**Tabla 3-20 - Resumen Emisiones. Fase de Cierre.**

|Actividad|Fase de Cierre (t/año)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Actividad**|**MP2.5**|**MP10**|**MPS**|**CO**<br>|**NOx**<br>|**SOx**<br>|**HC**<br>|**NH3 **<br>|
|Movimiento de Tierra|0,15|0,28|1,48|||<br>||<br>|
|Maquinaria|0,19|0,19|0,19|0,52|2,36||0,23||
|Tránsito Vehicular -<br>Resuspensión de Polvo|0,02|0,08|0,40||||||
|Tránsito Vehicular - Combustión|0,01|0,01|0,01|0,07|0,27|0,01|0,00|0,00<br>|
|Grupos Electrógenos|0,03|0,03|0,03|0,08|0,37|0,02|0,03||
|**Total**|**0,39**|**0,58**|**2,09**|**0,66**|**2,99**|**0,04**|**0,26**|**0,00**|

Fuente: Elaboración propia.

**3.2.5** **Resumen de Medidas de Control de Emisiones Fase de Cierre**

A continuación, se describen las medidas de control y abatimiento de emisiones

atmosféricas que serán implementadas durante la fase de cierre del proyecto:

 - Los camiones contarán con las mantenciones recomendadas por el fabricante y con

su revisión técnica al día; lo anterior se exigirá a las empresas contratistas a cargo

de las faenas de construcción. Se prohibirá la circulación de cualquier vehículo que

arroje humo visible a través del tubo de escape.

 - Sólo se utilizará maquinaria en buen estado, la que tendrá sus mantenciones

correspondientes al día.

 - Los vehículos utilizados en el transporte de material propenso a generar emisión de

material particulado y aquel que pudiera significar derrames en el camino, circularán

cubriendo total y eficazmente los materiales con lonas u otro sistema que impida la

dispersión de polvo a la atmósfera, lo cual será revisado periódicamente.

www.dfmconsultores.cl
31
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención**

**Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

www.dfmconsultores.cl
32
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**3.3** **Conclusiones**

#### 4 MODELO DE CALIDAD DEL AIRE

En la siguiente sección, se presenta la información relevante respecto del modelo de calidad

del aire utilizado.

**4.1** **Tipo de Modelo de Calidad del Aire Seleccionado**

Los principales factores por considerar para la selección de un modelo corresponden al tipo

de terreno presente en el área del proyecto, es decir, si es plano o complejo, y el tipo de

contaminante a emitir, si es primario o secundario. Conforme a ello, y de acuerdo con lo

recomendado en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, en el área

de emplazamiento del proyecto existen factores que podrían perturbar el carácter lineal de

los vientos, por lo que es necesario utilizar un modelo que permita simular meteorología

heterogénea. Debido a lo anterior, se ha seleccionado un modelo tipo _puff_ para la ejecución

de la modelación de calidad del aire.

A continuación, se presenta el detalle del modelo tipo _puff_ a utilizar.

**4.2** **Descripción del Modelo de Calidad del Aire Seleccionado - CALPUFF**

Tal como se indicó anteriormente, el entorno del área del proyecto presenta sectores de

topografía compleja, los cuales podrían interferir en el carácter lineal de los vientos. Es por

ello por lo que, en este estudio, se ha seleccionado el modelo de calidad del aire CALPUFF.

CALPUFF es un modelo de dispersión de contaminantes, no estacionario, multicapa, capaz

de modelar múltiples especies y simular los efectos del tiempo- y en el espacio- de las

diversas condiciones meteorológicas en el transporte de contaminantes. Además, es un

www.dfmconsultores.cl
33
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

modelo de libre disposición, desarrollado por Research Corporation, siendo la empresa

Exponent [3] su soporte técnico actual.

Cabe mencionar que CALLPUFF corresponde a un modelo Lagrangiano-Gaussiano de

transporte y dispersión de _puff_ emitidos por las fuentes emisoras consideradas, por lo que,

dentro de las capacidades del Modelo de Calidad del Aire, se puede destacar lo siguiente:

 - Simulación de procesos complejos: fumigación, estancamiento y recirculación.

 - Modelación de transporte de contaminantes de largo alcance.

 - Incorporación de efectos de terreno complejo en la dispersión de contaminantes.

 - Modelación de procesos de transformaciones químicas.

Además, el software posee un módulo para realizar el post-procesamiento de datos,

denominado CALPOST, el cual calcula las concentraciones en los receptores de interés,

permitiendo gestionar los datos para cada contaminante según el período de tiempo

requerido para el análisis.

Para evaluar el material particulado secundario se utilizará el mecanismo químico RIVAD

incorporado en el software CALPUFF.

3 [Sitio web: www.src.com/calpuff/calpuff1.htm](http://www.src.com/calpuff/calpuff1.htm)

www.dfmconsultores.cl
34
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.3** **Características del Modelo de Dispersión de Contaminantes**

**4.3.1** **Dominio de la Modelación**

En la siguiente figura se presenta el dominio de modelación, el cual corresponde a un área

de 26×30 kilómetros con 780 celdas de 1.000 × 1.000 m.

**Figura 4-1. Dominio de Modelación.**

Fuente: Elaboración propia.

www.dfmconsultores.cl
35
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.3.2** **Topografía del Sector**

La topografía del sector se ha extraído de Shuttle Radar Topography Mission, SRTM1, cuya

resolución es aproximadamente 30 m. Este archivo ha sido incorporado al modelo con el

objetivo de proporcionar la altura de los puntos de interés, por lo que en la Figura 4-2 se

presenta una imagen de la información utilizada.

**Figura 4-2. Topografía del Dominio de Modelación.**

Fuente: Elaboración propia.

www.dfmconsultores.cl
36
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.3.3** **Uso de Suelos**

De acuerdo en el dominio de modelación existen diversos usos de suelo, específicamente

del tipo Pastizal, de acuerdo con la clasificación presentada, en el sector de emplazamiento

del proyecto. con la información relacionada con el uso de suelo de la zona, obtenida a

través de los archivos Global Land Cover Characterization (GLCC) publicados por el U.S

Geological Survey (USGS), en la Figura 4-3 se presenta el uso de suelos para el dominio de

modelación.

**Figura 4-3. Uso de Suelos del Dominio de Modelación.**

Fuente: Elaboración propia.

www.dfmconsultores.cl
37
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.4** **Descripción del Modelo Meteorológico Seleccionado - WRF**

Weather Research and Forecasting Model o WRF por sus siglas en inglés, es un sistema de

modelación atmosférico de mesoescala ampliamente usado a nivel mundial en contextos

de investigación y de pronósticos operacionales. En Chile, es el modelo numérico

recomendado para la generación de datos meteorológicos en la Guía para el Uso de

Modelos de Calidad del Aire en el SEIA (SEA, 2023).

El modelo utiliza una grilla tridimensional para representar la atmósfera y sus procesos

(radiación atmosférica, capa superficial y capa límite y procesos de formación de nubes y

de precipitación, entre otros) en distintas escalas espaciales, las cuales pueden variar desde

las decenas de metros hasta miles de kilómetros. Utiliza información de topografía y uso de

suelo y de meteorología observada o modelada proveniente de modelos meteorológicos

globales para definir las condiciones iniciales y de borde para la simulación de pronósticos

meteorológicos.

A continuación, se describen las fuentes de la información suministrada y su tratamiento:

Topografía del dominio de modelación: Se ha utilizado información topográfica de alta

resolución proveniente del modelo Shuttle Radar Topography Mission, SRTM1, cuya

resolución es aproximadamente 30 m.

Uso de suelo: Se ha utilizado información de uso de suelos de alta resolución proveniente

del modelo Copernicus Global Land Service: Land Cover 100m con una resolución de 100

metros.

Meteorología proveniente de un modelo meteorológico global: Se han utilizado los

resultados del modelo ERA 5, año 2021. Este modelo corresponde a estimaciones horarias

de una gran cantidad de variables climáticas atmosféricas, terrestres y oceánicas. Los datos

cubren la Tierra en una grilla de aproximadamente 30 km de resolución y resuelven la

atmósfera hasta una altura de 80 km

Los principales parámetros utilizados para la configuración del modelo meteorológico se

presentan a continuación en la Tabla 4-1, estos fueron seleccionados por su capacidad de

adaptación a la topografía compleja y a modelos de alta resolución (< 3 km). La

www.dfmconsultores.cl
38
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

configuración del modelo se presenta en el Anexo 1. Archivos Digitales de Modelación

(Sección 6 del presente Informe).

**Tabla 4-1. Configuración parámetros principales WRF**

|Parámetro|Valor|
|---|---|
|**Dominio**|**Dominio**|
|Resolución horizontal|1 km|
|Proyección|Lambert|
|Dimensión|58x58x44|
|Número de niveles verticales|44|
|Niveles verticales (eta)|0.000000, 0.051578, 0.101822, 0.150735, 0.198315, 0.244562,<br>0.289477, 0.333059, 0.375309, 0.416226,<br>0.455810, 0.494062, 0.530982, 0.566569, 0.600823, 0.633745,<br>0.665334, 0.695591, 0.724515, 0.752107, 0.778366, 0.803292,<br>0.826886, 0.849148, 0.870076, 0.889673, 0.907937, 0.923302,<br>0.937101, 0.949333, 0.960000, 0.969101, 0.976635, 0.982603,<br>0.987005, 0.989841, 0.991111, 0.992381, 0.993651, 0.994921,<br>0.996190, 0.997460, 0.998730, 1.000000,|
|**Física**|**Física**|
|Esquema de radiación|RRTMG-fast (Onda corta y larga)|
|Modelo de suelo|Modelo Noah Land Surface|
|Tratamiento de capa superficial|Revised MM5 surface layer|
|Parametrización de capa límite|Yonsei University|
|Esquema de convección|Kain-Fritsch|
|Microfísica de nubes y precipitación|WSM 3-class|
|**Dinámica**|**Dinámica**|
|Parametrización de turbulencia|Smagorinsky|
|Núcleo dinámico|EM (Advanced Mass) y No hidroestático|
|Advección|positiva-definitiva|

Fuente: Elaboración propia.

**4.5** **Caracterización Meteorológica del Área del Proyecto**

En este inciso se presenta la caracterización de la meteorología observada y modelada para

el sector del “Proyecto Terminal de Mantención Mejillones”.

www.dfmconsultores.cl
39
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.5.1** **Meteorología de Superficie - Valores Observados**

La meteorología de superficie utilizada para caracterizar el área del Proyecto corresponde

a los registros horarios de velocidad y dirección del viento, temperatura, humedad relativa

y radiación solar pertenecientes a la Estación JJ Latorre. Dicha estación pertenece a la

empresa ENAEX S.A y es operada por la empresa Algoritmos, cuyos datos fueron obtenidos

mediante el sitio web “Monitoreo en Línea de Calidad del Aire Ambiental [4] ” de la Ilustre

Municipalidad de Mejillones.

Las coordenadas UTM de la estación mencionada se presentan en la Tabla 4-2 en conjunto

con las variables medidas y el periodo de monitoreo considerado para este estudio.

**Tabla 4-2. Coordenadas de Ubicación, Estación de Monitoreo Meteorológico JJ Latorre.**

|Estación de<br>Monitoreo|Variables Meteorológicas<br>Registradas|Periodo monitoreado<br>considerado para este<br>estudio|Coordenadas UTM (Datum<br>WGS84)|Col5|
|---|---|---|---|---|
|**Estación de**<br>**Monitoreo**|**Variables Meteorológicas**<br>**Registradas**|**Periodo monitoreado**<br>**considerado para este**<br>**estudio**|**Este (m)**|**Norte (m)**|
|JJ Latorre|Velocidad del Viento (m/s)|1 de enero 2020 al 31 de<br>diciembre 2020|352.346|7.444.100|
|JJ Latorre|Dirección del Viento (°)|Dirección del Viento (°)|Dirección del Viento (°)|Dirección del Viento (°)|
|JJ Latorre|Temperatura del Aire (°C)|Temperatura del Aire (°C)|Temperatura del Aire (°C)|Temperatura del Aire (°C)|
|JJ Latorre|Humedad Relativa (%)|Humedad Relativa (%)|Humedad Relativa (%)|Humedad Relativa (%)|
|JJ Latorre|Radiación Solar (W/m2)|Radiación Solar (W/m2)|Radiación Solar (W/m2)|Radiación Solar (W/m2)|

Fuente: Elaboración propia.

A continuación, en la Figura 4-4 se muestra la ubicación referencial de la estación de

monitoreo meteorológico presentada en la tabla anterior respecto a la zona de

emplazamiento del Proyecto.

**Figura 4-4. Ubicación Referencial Estación de Monitoreo Meteorológico.**

4 [Link web: https://www.mejillones.cl/2018/08/17/monitoreo-en-linea-calidad-del-aire-ambiental/](https://www.mejillones.cl/2018/08/17/monitoreo-en-linea-calidad-del-aire-ambiental/)

www.dfmconsultores.cl
40
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Fuente: Elaboración propia.

www.dfmconsultores.cl
41
info@dfmconsultores.cl

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

4.5.1.1 Estación JJ Latorre

a) Velocidad y Dirección del Viento

En la Tabla 4-3 se presenta el resumen de información para la variable velocidad viento,

especificando el valor promedio, máximo y mínimo, además del porcentaje de calmas,

registrados durante el periodo de estudio. Cabe mencionar que el porcentaje de calmas se

define como el porcentaje del tiempo en que la velocidad del viento es menor 0,5 m/s.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA”, las series de datos meteorológicos deben contener un 75% de datos válidos, lo cual

se cumple para el año 2020.

**Tabla 4-3. Resumen de Información Velocidad del Viento Observada en Estación JJ Latorre.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2020**|
|Velocidad de Viento (m/s)|Promedio|2,4|
|Velocidad de Viento (m/s)|Máximo|9,5|
|Velocidad de Viento (m/s)|Mínimo|0,0|
|Porcentaje de Calmas (%)|Porcentaje de Calmas (%)|1,6|
|Datos Válidos (%)|Datos Válidos (%)|100,0%|

Fuente: Elaboración propia.

A continuación, se presentan las series de tiempo, ciclos diarios y ciclo estacional

observados para las variables meteorológicas velocidad del viento y dirección del viento.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

42

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Series de Tiempo

A modo de verificación de la completitud de datos, se exhiben las series de tiempo de las

variables meteorológicas velocidad y dirección del viento en la Figura 4-5 y Figura 4-6

respectivamente.

**Figura 4-5. Serie de Tiempo de Velocidad del Viento. Periodo enero a diciembre 2020. Observado en**

**Estación JJ Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

43

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-6. Serie de Tiempo de Dirección del Viento. Periodo enero a diciembre 2020. Observado Estación**

**JJ Latorre.**

Fuente: Elaboración propia.

Por otro lado, con el fin de caracterizar la información anual registrada tanto para la

velocidad como para la dirección del viento, en la Tabla 4-4 se muestra la frecuencia de

distribución para la velocidad y dirección del viento observada en la Estación JJ Latorre.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

44

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-4. Frecuencia de distribución Velocidad y Dirección del Viento. Periodo enero 2020 a diciembre 2020. Observado en Estación JJ Latorre.**

|Dirección|Col2|Distribución Porcentual de Velocidad del Viento (m/s)|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Dirección**|**Dirección**|**0,50 - 2,10**|**2,10 - 3,60**|**3,60 - 5,70**|**5,70 - 8,80**|**8,80 - 11,10**|**>= 11,10**|**Total (%)**|
|348,75 - 11,25|N|7,1%|0,5%|0,0%|0,0%|0,0%|0,0%|7,6%|
|11,25 - 33,75|NNE|7,7%|1,0%|0,0%|0,0%|0,0%|0,0%|8,7%|
|33,75 - 56,25|NE|1,5%|0,3%|0,0%|0,0%|0,0%|0,0%|1,8%|
|56,25 - 78,75|ENE|0,4%|0,0%|0,0%|0,0%|0,0%|0,0%|0,4%|
|78,75 - 101,25|E|0,4%|0,0%|0,0%|0,0%|0,0%|0,0%|0,4%|
|101,25 - 123,75|ESE|1,1%|0,1%|0,0%|0,0%|0,0%|0,0%|1,2%|
|123,75 - 146,25|SE|1,8%|0,2%|0,0%|0,0%|0,0%|0,0%|2,1%|
|146,25 - 168,75|SSE|4,2%|1,6%|0,0%|0,0%|0,0%|0,0%|5,9%|
|168,75 - 191,25|S|8,1%|11,7%|10,6%|3,1%|0,0%|0,0%|33,5%|
|191,25 - 213,75|SSW|5,0%|5,2%|3,9%|0,2%|0,0%|0,0%|14,3%|
|213,75 - 236,25|SW|1,2%|0,9%|0,3%|0,0%|0,0%|0,0%|2,5%|
|236,25 - 258,75|WSW|0,7%|0,1%|0,0%|0,0%|0,0%|0,0%|0,9%|
|258,75 - 281,25|W|0,7%|0,0%|0,0%|0,0%|0,0%|0,0%|0,7%|
|281,25 - 303,75|WNW|1,3%|0,3%|0,0%|0,0%|0,0%|0,0%|1,6%|
|303,75 - 326,25|NW|3,1%|1,9%|0,4%|0,0%|0,0%|0,0%|5,3%|
|326,25 - 348,75|NNW|4,8%|6,3%|0,4%|0,0%|0,0%|0,0%|11,5%|
|Sub-Total|Sub-Total|49,1%|30,2%|15,7%|3,3%|0,0%|0,0%|98,4%|
|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|1,6%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

45

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Ciclos Diarios

En la Figura 4-7 se presenta el ciclo diario para la variable velocidad del viento, en donde es

posible observar que las menores intensidades ocurren en el período nocturno,

específicamente entre 00:00 y 9:00 horas con velocidades cercanas e inferiores a los 2 m/s.

Tras ello, a las 9:00 horas se observa un ascenso paulatino de la magnitud de esta variable,

la cual alcanza un máximo promedio de 3,9 m/s a las 19:00 horas, para luego descender

hasta alcanzar los valores nocturnos mencionados anteriormente, dando comienzo

nuevamente al ciclo descrito.

**Figura 4-7. Ciclo Diario de Velocidad del Viento. Periodo enero a diciembre 2020. Observado en Estación JJ**

**Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

46

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

En la Figura 4-8 se presenta el ciclo diario de dirección del viento, en donde se puede

identificar una predominancia de vientos sur (S) durante horas de la tarde hasta la

madrugada, con mayores frecuencias durante las 16:00 y 8:00 horas. Por otro lado, a partir

de las 10:00 horas se observan vientos nornoreste (NNE) y nornoroeste (NNO), los cuales

se mantienen hasta las 16:00 horas, para luego cambiar de dirección hacia vientos

provenientes del sur (S), dando inicio nuevamente al ciclo.

**Figura 4-8. Ciclo Diario dirección del Viento. Periodo enero 2020 a diciembre 2020. Observado en Estación**

**JJ Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

47

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Ciclo Estacional

En la Figura 4-9 se presenta el ciclo estacional de vientos observados, en donde se puede

apreciar que, en cuanto a la direccion del viento, existe una predomincancia de vientos sur

(S) durante la tarde hasta la madrugada, especificamente entre las 17:00 y 8:00 horas,

mientras que durante las 11:00 y 14:00 horas predominan vientos norte(N) y nornoroeste

(NNO). Ambos casos persisten a lo largo de todas las estaciones del año. Por otro lado, en

cuanto a la intensidad de la velocidad, se observan que los mayores valores se presentan

durante los meses de septiembre a abril, mientras que las menores intensidades se

registran mayoritariamente durante todo el año entre las 00:00 y 9:00 horas.

**Figura 4-9. Ciclo Estacional Vientos. Periodo enero a diciembre 2020. Observado en Estación JJ Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

48

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

b) Temperatura

En la Tabla 4-5 se presenta el resumen de información para la variable temperatura,

especificando el valor promedio, máximo y mínimo registrados durante el periodo en

estudio. De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del

Aire en el SEIA”, las series de datos meteorológicos deben contener un 75% de datos

válidos, lo que se cumple para el año 2020.

**Tabla 4-5. Resumen de Información Temperatura Observada en Estación JJ Latorre.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2020**|
|Temperatura (°C)|Promedio|18,6|
|Temperatura (°C)|Máximo|32,1|
|Temperatura (°C)|Mínimo|6,5|
|Datos Válidos (%)|Datos Válidos (%)|100,0%|

Fuente: Elaboración propia.

A continuación, se presenta la serie de tiempo, ciclo diario y ciclo estacional observados

para la variable meteorológica temperatura.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

49

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Serie de Tiempo

A modo de verificación de la completitud de los datos obtenidos mediante la estación de

monitoreo meteorológico JJ Latorre, en la Figura 4-10 se presenta la serie de tiempo para

la variable temperatura.

**Figura 4-10. Serie de Tiempo de Temperatura. Periodo enero a diciembre 2020. Observado en Estación JJ**

**Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

50

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Ciclo Diario

En la Figura 4-11 se presenta el ciclo diario para la variable temperatura, en donde se

aprecia que los valores más bajos se registran durante horas de la noche y madrugada,

específicamente entre las 20:00 y 6:00 horas, con un mínimo promedio aproximado de 16

°C. Tras ello, la temperatura comienza a aumentar rápidamente hasta alcanzar su máximo

promedio aproximado de 23 °C a las 15:00 horas, para luego descender hasta alcanzar el

valor descrito inicialmente para el periodo nocturno, dando inicio nuevamente al ciclo. En

cuanto a la dispersión de datos, se observa una amplitud de aproximadamente +/- 4 °C de

manera uniforme a lo largo de todo el ciclo diario.

**Figura 4-11. Ciclo Diario de Temperatura. Periodo enero a diciembre 2020. Observado en Estación JJ**

**Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

51

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Ciclo Estacional

En la Figura 4-12 se presenta el ciclo estacional para la variable temperatura, en donde se

puede apreciar que las mayores temperaturas se presentan durante los meses de diciembre

a marzo, especificamente entre las 12:00 y 17:00 horas, con valores superiores a los 25 °C.

Por el contrario, las menores temperaturas se registran durante el mes de julio en el periodo

nocturno y de madrugrada, especificamente entre las 21:00 y 7:00 horas, con valores de

aproximadamente 13 °C.

**Figura 4-12. Ciclo Estacional de Temperatura. Periodo enero a diciembre 2020. Observado en Estación JJ**

**Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

52

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

c) Humedad Relativa

En la Tabla 4-6 se presenta el resumen de información para la variable humedad relativa,

especificando el valor promedio, máximo y mínimo para el periodo en estudio. De acuerdo

con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, las

series de datos meteorológicos deben contener un 75% de datos válidos, lo cual se cumple

para el año 2020.

**Tabla 4-6. Resumen de Información Humedad Relativa Observada en Estación JJ Latorre.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2020**|
|Humedad Relativa (%)|Promedio|61,4|
|Humedad Relativa (%)|Máximo|84,8|
|Humedad Relativa (%)|Mínimo|23,6|
|% Datos Válidos|% Datos Válidos|100,0%|

Fuente: Elaboración propia.

A continuación, se presenta la serie de tiempo, ciclo diario y ciclo estacional observados

para la variable meteorológica humedad relativa.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

53

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Serie de Tiempo

A modo de verificación de la completitud de los datos obtenidos mediante la estación JJ

Latorre, en la Figura 4-13 se presenta la serie de tiempo para la variable meteorológica

humedad relativa.

**Figura 4-13. Serie de Tiempo de Humedad Relativa. Periodo enero a diciembre 2020. Observado en**

**Estación JJ Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

54

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Ciclo Diario

En la Figura 4-14 se presenta el ciclo diario para la variable humedad relativa, en donde se

puede identificar que los valores más altos se registran durante el periodo nocturno y de

madrugada, entre las 22:00 y 7:00 horas, alcanzando un valor máximo promedio

aproximado de 70% a las 6:00 horas. Tras este punto, la humedad comienza a descender a

lo largo del día, alcanzando un mínimo promedio aproximado de 48% a las 15:00 horas, para

luego comenzar a aumentar nuevamente hasta alcanzar los valores descritos de manera

inicial.

**Figura 4-14. Ciclo Diario de Humedad Relativa. Periodo enero a diciembre 2020. Observado en Estación JJ**

**Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

55

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Ciclo Estacional

En la Figura 4-15 se presenta el ciclo estacional para la variable humedad relativa, en donde

se puede apreciar que los mayores valores se presentan durante los meses de febrero a

julio durante horas de la madrugada, alcanzando los máximos valores entre las 03:00 y las

06:00 horas. Por el contrario, los valores más bajos se registran durante los meses de

noviembre a marzo durante el periodo diurno, específicamente entre las 13:00 y 16:00

horas, con valores cercanos al 40% de humedad.

**Figura 4-15. Ciclo Estacional de Humedad Relativa. Periodo enero a diciembre 2020. Observado en**

**Estación JJ Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

56

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

d) Radiación Solar

En la Tabla 4-7 se presenta el resumen de información para la variable radiación solar,

especificando el valor promedio, máximo y mínimo registrados durante el periodo en

estudio. De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del

Aire en el SEIA”, las series de datos meteorológicos deben contener un 75% de datos

válidos, lo cual se cumple para el año 2020.

**Tabla 4-7. Resumen de Información Radiación Solar Observada en Estación JJ Latorre.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2020**|
|Radiación Solar (W/m2)|Promedio|243,7|
|Radiación Solar (W/m2)|Máximo|1.121,8|
|Radiación Solar (W/m2)|Mínimo|0,0|
|% Datos Válidos|% Datos Válidos|100,0%|

Fuente: Elaboración propia.

A continuación, se presenta la serie de tiempo, ciclo diario y ciclo estacional observados

para la variable meteorológica radiación solar.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

57

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Serie de Tiempo

A modo de verificación de la completitud de los datos obtenidos mediante la estación de

monitoreo JJ Latorre, en la Figura 4-16 se presenta la serie de tiempo para la variable

meteorológica radiación solar.

**Figura 4-16. Serie de Tiempo de Radiación Solar. Periodo enero a diciembre 2020. Observado en Estación**

**JJ Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

58

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Ciclo Diario

En la Figura 4-17 se presenta el ciclo diario para la variable radiación solar, en donde se

puede apreciar que durante el periodo nocturno y de madrugada, es decir, entre las 20:00

y 5:00 horas, no se presentan radiaciones. Por el contrario, los registros de esta variable

aumentan rapidamente entre las 6:00 y 12:00 horas, alcanzando su máximo valor en esta

última hora, con un valor promedio aproximado de 830 W/m [2] . Tras este punto, los valores

comienzan a descender hasta alcanzar registros nulos, de tal forma de dar inicio

nuevamente al ciclo descrito. Cabe mencionar que la dispersión de datos presentada al

momento de máxima radiacion posee una diferencia entre los valores promedio mínimo y

máximo de aproximadamente 550 W/m [2] .

**Figura 4-17. Ciclo Diario de Radiación Solar. Periodo enero a diciembre 2020. Observado en Estación JJ**

**Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

59

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Ciclo Estacional

En la Figura 4-18 se presenta el ciclo estacional para la variable radiación solar, en donde se

puede apreciar que los máximos valores se registran durante los meses de noviembre a

febrero, entre las 11:00 y 13:00 horas, con valores cercanos a los 1.100 W/m [2] . Por el

contrario, los valores menores se presentan durante todo el año entre las 18:00 y 7:00

horas.

**Figura 4-18. Ciclo Estacional de Radiación Solar, periodo enero 2020 a diciembre 2020. Observado en**

**Estación JJ Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

60

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.5.2** **Meteorología de Superficie - Valores Modelados**

4.5.2.1 Estación JJ Latorre

a) Velocidad y Dirección del Viento

En la Tabla 4-8 se presenta el resumen de información para la variable velocidad viento,

detallando el valor promedio, máximo y mínimo, además del porcentaje de calmas,

registrados durante el periodo en estudio. Cabe mencionar que el periodo de calmas se

define como el porcentaje del tiempo en que la velocidad del viento es menor a 0,5 m/s.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA”, las series de datos meteorológicos deben contener un 75% de datos válidos, lo que

se cumple para el año 2020 debido a que se cuenta con la completitud de los datos a partir

del modelo WRF.

**Tabla 4-8. Resumen de Información Velocidad del Viento Modelada en Estación JJ Latorre, Año 2020.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2020**|
|Velocidad de Viento (m/s)|Promedio|3,3|
|Velocidad de Viento (m/s)|Máximo|9,7|
|Velocidad de Viento (m/s)|Mínimo|0,1|
|Porcentaje de Calmas (%)|Porcentaje de Calmas (%)|0,9|
|Datos Válidos (%)|Datos Válidos (%)|100,0%|

Fuente: Elaboración propia.

A continuación, se presentan las series de tiempo, ciclos diarios y ciclo estacional modelados

para las variables meteorológicas velocidad del viento y dirección del viento.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

61

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Series de Tiempo

A modo de verificación de la completitud de datos, en la Figura 4-19 y Figura 4-20 se

presentan las series de tiempos para las variables de velocidad y dirección del viento

respectivamente.

**Figura 4-19. Serie de Tiempo de Velocidad del Viento. Período enero a diciembre 2020. Modelado en**

**Estación JJ Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

62

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-20. Serie de Tiempo de Dirección del Viento. Período enero a diciembre 2020. Modelado en**

**Estación JJ Latorre.**

Fuente: Elaboración propia.

Por otro lado, con el fin de caracterizar la información anual registrada para las variables de

velocidad y dirección del viento, a continuación, en la Tabla 4-9 se presenta la frecuencia de

distribución de dichos parámetros de acuerdo con la modelación realizada.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

63

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-9. Frecuencia de distribución Velocidad y Dirección del Viento. Período enero a diciembre 2020. Modelado en Estación JJ Latorre.**

|Dirección|Col2|Distribución Porcentual de Velocidad del Viento (m/s)|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Dirección**|**Dirección**|**0,50 - 2,10**|**2,10 - 3,60**|**3,60 - 5,70**|**5,70 - 8,80**|**8,80 - 11,10**|**>= 11,10**|**Total (%)**|
|348,75 - 11,25|N|1,07%|3,81%|4,31%|0,16%|0,00%|0,00%|9,36%|
|11,25 - 33,75|NNE|0,77%|4,30%|2,19%|0,01%|0,00%|0,00%|7,27%|
|33,75 - 56,25|NE|1,09%|3,69%|0,99%|0,00%|0,00%|0,00%|5,77%|
|56,25 - 78,75|ENE|0,91%|0,68%|0,06%|0,00%|0,00%|0,00%|1,65%|
|78,75 - 101,25|E|0,60%|0,05%|0,00%|0,00%|0,00%|0,00%|0,65%|
|101,25 - 123,75|ESE|0,56%|0,01%|0,00%|0,00%|0,00%|0,00%|0,57%|
|123,75 - 146,25|SE|0,72%|0,11%|0,00%|0,00%|0,00%|0,00%|0,83%|
|146,25 - 168,75|SSE|2,08%|1,06%|0,01%|0,00%|0,00%|0,00%|3,15%|
|168,75 - 191,25|S|4,64%|19,43%|5,50%|0,47%|0,01%|0,00%|30,05%|
|191,25 - 213,75|SSW|2,38%|9,54%|15,63%|4,88%|0,00%|0,00%|32,43%|
|213,75 - 236,25|SW|0,56%|0,79%|1,56%|0,08%|0,00%|0,00%|2,98%|
|236,25 - 258,75|WSW|0,31%|0,15%|0,00%|0,00%|0,00%|0,00%|0,46%|
|258,75 - 281,25|W|0,31%|0,00%|0,00%|0,00%|0,00%|0,00%|0,31%|
|281,25 - 303,75|WNW|0,20%|0,00%|0,00%|0,00%|0,00%|0,00%|0,20%|
|303,75 - 326,25|NW|0,57%|0,11%|0,00%|0,00%|0,00%|0,00%|0,68%|
|326,25 - 348,75|NNW|0,67%|1,53%|0,55%|0,01%|0,00%|0,00%|2,76%|
|Sub-Total|Sub-Total|17.45%|45,26%|30,79%|5,61%|0,01%|0,00%|99,13%|
|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|0,87%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

64

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Ciclos Diarios

En la Figura 4-21 se presenta el ciclo diario para la variable velocidad del viento, en donde

se puede observar que el modelo calcula las menores intensidades para el periodo nocturno

y de madrugada, especificamente entre las 22:00 y 9:00 horas, con velocidades oscilantes

entre los 2,6 a 3 m/s. Así, a las 7:00 se aprecia una máxima local de velocidad de viento de

3 m/s, la cual desciende hasta alcanzar el mínimo global de 2,6 m/s a las 9:00 horas. Tras

ello, las velocidades comienzan a aumentar de manera paulatina hasta alcanzar un máximo

valor promedio de 4,5 m/s a las 18:00 horas, para luego descender nuevamente hasta

alcanzar los valores descritos inicialemente.

**Figura 4-21. Ciclo Diario de Velocidad del Viento. Período enero a diciembre 2020. Modelado en Estación**

**JJ Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

65

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

En la Figura 4-22 se presenta el ciclo diario de dirección del viento, en donde se puede

observar que, para el período nocturno, el modelo predice vientos mayoritariamente desde

el sur (S), con frecuencias aproximadas al 30%. Posteriormente, desde las 09:00 horas, el

modelo estima un cambio en el origen de los vientos, pasando a vientos desde el norte (N)

durante la mañana, con leves presencias de vientos provenientes desde el suroeste (SO).

Así, a partir del mediodía, el modelo predice un aumento en la frecuencia de vientos desde

el noreste (NE), lo cual se mantiene hasta las 17:00 horas aproximadamente, para luego

cambiar de dirección nuevamente y así comenzar con el ciclo descrito de manera inicial.

**Figura 4-22. Ciclo Diario Dirección del Viento. Periodo enero a diciembre 2020. Modelado en Estación JJ**

**Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

66

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Ciclo Estacional

En la Figura 4-23 se presenta el ciclo estacional de vientos modelados, en la que es posible

observar que la dirección del viento predominante durante el periodo nocturno es aquella

proveniente desde el sur (S), lo cual se mantiene desde las 18:00 hasta las 8:00 horas. Luego,

durante el periodo diurno, la direccion del viento proviene mayoritariamente desde el norte

con algunas variaciones durante los meses de invierno, en donde se aprecian algunos

vientos provenientes desde el noroeste. Por otra parte, el modelo predice mayores

velocidades de viento entre las 12:00 y 20:00 horas, especificamente entre los meses de

septiembre a noviembre, mientras que las menores velocidades se evidencian durante los

meses de diciembre y enero durante el periodo nocturno.

**Figura 4-23. Ciclo Estacional Vientos. Período enero a diciembre 2020. Modelado en Estación JJ Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

67

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

b) Temperatura

En la Tabla 4-10 se presenta el resumen de información para la variable temperatura,

detallando el valor promedio, máximo y mínimo registrados durante el periodo en estudio.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA”, las series de datos meteorológicos deben contener un 75% de datos válidos, lo cual

se cumple para el año 2020 debido a que se cuenta con la completitud de los datos a partir

del modelo WRF.

**Tabla 4-10. Resumen de Información Temperatura Modelada en Estación JJ Latorre.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2020**|
|Temperatura (°C)|Promedio|18,2|
|Temperatura (°C)|Máximo|27,8|
|Temperatura (°C)|Mínimo|9,1|
|Datos Válidos (%)|Datos Válidos (%)|100,0%|

Fuente: Elaboración propia.

A continuación, se presenta la serie de tiempo, ciclo diario y ciclo estacional modelados para

la variable meteorológica temperatura.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

68

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Serie de Tiempo

A modo de verificación de la completitud de los datos, en la Figura 4-24 se presenta la serie

de tiempo para la variable meteorológica temperatura.

**Figura 4-24. Serie de Tiempo de Temperatura. Período enero a diciembre 2020. Modelado en Estación JJ**

**Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

69

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Ciclo Diario

En la Figura 4-25 se presenta el ciclo diario para la variable temperatura calculada por el

modelo. Como se puede observar, la temperatura promedio mínima se predice para las

6:00 horas con un valor de 14,5 °C, momento a partir del cual la variable comienza a

incrementar gradualmente hasta alcanzar un promedio máximo cercano a los 22°C a las

14:00 horas. Luego, el modelo calcula un descenso sostenido de temperatura hasta alcanzar

el valor mínimo descrito inicialmente. Cabe mencionar que, es posible observar que la

dispersión de datos es relativamente constante a lo largo de todo el ciclo diario, con una

amplitud de +/- 4 °C.

**Figura 4-25. Ciclo Diario de Temperatura. Período enero a diciembre 2020. Modelado en Estación JJ**

**Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

70

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Ciclo Estacional

En la Figura 4-26 se observa el ciclo estacional de temperatura, en donde se puede apreciar

que el modelo calcula las mayores temperaturas para los meses de enero a marzo,

especificamente durante las 12:00 y 17:00 horas, con valores cercanos a los 25 °C. En

cambio, las menores temperaturas se estiman para el periodo invernal durante los meses

de julio a octubre, entre las 1:00 y 7:00 horas, con valores cercanos a los 11°C.

**Figura 4-26. Ciclo Estacional de Temperatura. Período enero a diciembre 2020. Modelado en Estación JJ**

**Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

71

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.5.3** **Meteorología de Altura - Valores Observados**

Con respecto a la meteorología de altura, no existen registros de mediciones disponibles en

la estación mencionada que puedan ser utilizadas en este estudio.

**4.5.4** **Meteorología de Altura - Valores Modelados**

De acuerdo con lo obtenido por el procesamiento de los resultados del modelo

meteorológico WRF, se ha caracterizado la variable altura de la capa de mezcla, la cual

corresponde a la altura medida desde la superficie en la que la inestabilidad favorece la

dispersión vertical de contaminantes. Para ello, se han utilizado los datos entregados por el

modelo meteorológico WRF en el sector de la Estación JJ Latorre, los cuales se muestran en

la siguiente sección.

4.5.4.1 Estación Meteorológica JJ Latorre

a) Altura de Capa de Mezcla

En la Tabla 4-11 se presenta el resumen de información para la variable altura de capa de

mezcla, detallando el valor promedio, máximo y mínimo para el periodo en estudio. De

acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA”, las series de datos meteorológicos deben contener un 75% de datos válidos, lo cual

se cumple para el año 2020 ya que se cuenta con la completitud de los datos a partir del

modelo WRF.

**Tabla 4-11. Resumen de Información Altura de Capa de Mezcla Modelada en Estación JJ Latorre.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2020**|
|Altura de Capa de Mezcla (m)|Promedio|282,01|
|Altura de Capa de Mezcla (m)|Máximo|1.622,46|
|Altura de Capa de Mezcla (m)|Mínimo|10,00|
|% Datos Válidos|% Datos Válidos|100,0%|

Fuente: Elaboración propia.

A continuación, se presenta la serie de tiempo, ciclo diario y ciclo estacional modelados para

la variable meteorológica altura de capa de mezcla.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

72

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Serie de tiempo

A modo de verificación de la completitud de datos, en la Figura 4-27 se presenta la serie de

tiempo para la variable altura de capa de mezcla.

**Figura 4-27. Serie de Tiempo de Altura de Capa de Mezcla. Período enero a diciembre 2020. Modelado en**

**Estación JJ Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

73

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Ciclo Diario

En la Figura 4-28 se presenta el ciclo diario para la variable altura de capa de mezcla

modelada, en donde se puede observar que durante el periodo nocturno y de madrugada

esta variable registra los menores valores de altura. En cambio, a partir de las 06:00 horas

comienza a aumentar sostenidamente hasta alcanzar un máximo promedio aproximado de

650 metros a las 14:00 horas, para luego descender hasta alcanzar los valores nocturnos

dando comienzo nuevamente al ciclo.

**Figura 4-28. Ciclo Diario de Altura de Capa de Mezcla. Período enero a diciembre 2020. Modelado en**

**Estación JJ Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

74

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Ciclo Estacional

En la Figura 4-29 se presenta el ciclo estacional para la variable altura de capa de mezcla,

en donde se puede observar que durante el periodo nocturno y de madrugada esta variable

tiene los menores valores a lo largo del año, mientras que los valores máximos se registran

en las estaciones de otoño y primavera entre las 12:00 y 17:00 horas.

**Figura 4-29. Ciclo Estacional de Altura de Capa de Mezcla. Período enero a diciembre 2020. Modelado en**

**Estación JJ Latorre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

75

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.6** **Análisis de Incertidumbre**

Con el fin de determinar la incertidumbre entre los resultados del modelo meteorológico y

los datos observados en las Estación JJ Latorre, en las siguientes secciones se presenta la

comparación cualitativa y cuantitativa entre la meteorología observada y modelada.

**4.6.1** **Estación JJ Latorre**

4.6.1.1 Comparación Cualitativa

Debido a que la meteorología de superficie es un factor relevante en la dispersión de los

contaminantes, en el presente inciso se busca validar el modelo WRF de manera cualitativa,

el cual será utilizado como información base de entrada al modelo de dispersión CALPUFF.

Para llevar a cabo lo anterior, se presenta una comparación de los datos observados en la

estación JJ Latorre para el periodo comprendido entre el 1 de enero y el 31 de diciembre

del año 2020, mismo periodo para el que se realizó el modelo meteorológico WRF. Así, se

comparan ciclos diarios y estacionales para las variables meteorológicas velocidad del

viento, dirección del viento y temperatura.

a) Velocidad y Dirección del Viento

A continuación, desde la Figura 4-30 a la Figura 4-32, se muestra una comparación entre los

resultados de los ciclos diarios y estacionales de la velocidad y dirección del viento

observados y modelados, además del histograma de frecuencias de direcciones de viento,

para así determinar la incertidumbre de dichas variables de manera cualitativa.

En la Figura 4-30 se puede observar que el modelo calcula de manera apropiada el

incremento de velocidad en el período diurno, así como la disminución de la magnitud de

esta variable durante la noche. Sin perjuicio de lo anterior, se observan diferencias entre

ambas figuras, describiendo una sobrestimación de la velocidad del viento por parte del

modelo, en particular en el periodo diurno. También se observa una menor dispersión de

las velocidades generadas por el modelo para el periodo de máximos valores, en

comparación a los valores observados.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

76

|Observado|Modelado|
|---|---|
|||

www.dfmconsultores.cl

**info@dfmconsultores.cl**

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

**Figura 4-30. Comparación de Ciclos Diarios de Velocidad del Viento. Estación JJ Latorre.**

Fuente: Elaboración propia.

77

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

En la Figura 4-31 se observa que el modelo realiza una aproximación razonable de la dirección de origen de los vientos a lo largo del

día, presentando sobreestimaciones en la frecuencia de los vientos durante el periodo nocturno y de madrugada, mientras que realiza

una subestimación de estos durante el periodo diurno.

**Figura 4-31. Comparación de Ciclos Diarios de Dirección del Viento. Estación JJ Latorre.**

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

78

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

En la Figura 4-32 se observa que el modelo tiende a sobreestimar la magnitud de la velocidad del viento para el periodo diurno,

especialmente para los meses de invierno, como también para el periodo de madrugada, en donde estos valores debiesen ser menores

durante la época comprendida entre abril y noviembre. En cuanto a la dirección del viento, se aprecia que el modelo tiene un buen

desempeño para representar los diversos cambios direccionales presentes con el transcurso de las horas en las distintas estaciones.

**Figura 4-32. Comparación de Ciclos Estacionales de Velocidad y Dirección del Viento. Estación JJ Latorre.**

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

79

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

b) Temperatura

A continuación, con el fin de comparar los resultados de la meteorología observada y modelada en las distintas horas del día y a lo

largo del año, en la Figura 4-33 y la Figura 4-34 se presenta una comparación de los ciclos diarios y estacionales, observados y

modelados, presentados en los incisos anteriores para la variable temperatura.

**Figura 4-33. Comparación de Ciclos Diarios de Temperatura. Estación JJ Latorre.**

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

80

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

**Figura 4-34. Comparación del Ciclo Estacional de Temperatura. Estación JJ Latorre.**

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia.

De acuerdo con las figuras anteriores, se puede apreciar que el modelo se aproxima bastante a las temperaturas observadas en la

estación de monitoreo, sin embargo, existe una subestimación de las temperaturas para el ciclo estacional, específicamente para el

periodo diurno durante los meses de verano. Por otro lado, en cuanto al ciclo diario, el modelo se asemeja a las variaciones de

temperatura presentadas a lo largo del día, calculando valores máximos y mínimos similares a lo real.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

81

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

4.6.1.2 Comparación Cuantitativa

Para realizar la comparación cuantitativa se han utilizado tres estadígrafos comúnmente

empleados para la evaluación del _performance_ de modelos: Sesgo, Error Cuadrático Medio

y el Coeficiente de Correlación (r).

A continuación, en la Tabla 4-12 se presentan los resultados de estadígrafos mencionados

para los ciclos diarios estudiados en el inciso anterior.

**Tabla 4-12. Estadígrafos de Dispersión de Velocidad del Viento y Temperatura.**

|Medida de Error|Velocidad del Viento|Temperatura|
|---|---|---|
|**Medida de Error**|**Ciclo Diario**|**Ciclo Diario**|
|Sesgo|0,84|-0,40|
|ECM|0,87|0,79|
|r|0,94|0,97|

Fuente: Elaboración propia.

Conforme con lo presentado en la tabla anterior, se pueden obtener conclusiones similares

a lo presentado en el análisis cualitativo, pues en cuanto a la variable velocidad del viento,

de acuerdo con el valor del sesgo obtenido, el modelo tiende a sobrestimar levemente los

valores, sin embargo, realiza una aproximación satisfactoria en cuanto a los valores

observados. Asimismo, el error cuadrático medio obtenido es relativamente alto, lo que

indica que el modelo posee una cierta diferencia entre los datos modelados y observados.

No obstante, al presentar un coeficiente de relación cercano a 1, es posible concluir que el

modelo posee una alta capacidad para representar las condiciones meteorológicas del

viento observadas.

Por otro lado, en cuanto a la variable temperatura, conforme al valor del sesgo obtenido, el

modelo tiende a subestimar los valores máximos presentados por la estación de monitoreo.

De igual forma, conforme con el resultado del error cuadrático medio, es posible establecer

que el modelo posee una leve diferencia entre los datos modelados y los observados. Sin

embargo, al presentar un coeficiente de relación cercano a 1, es posible concluir que el

modelo posee una alta capacidad para representar las condiciones meteorológicas

observadas.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

82

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.7** **Normas de Calidad del Aire**

En la Tabla 4-13 se presenta la normativa primaria de calidad del aire vigente a evaluar

respectivamente en el marco del Proyecto. Mientras que en la Tabla 4-14 se presentan las

normas secundarias a evaluar.

**Tabla 4-13. Normas primarias de calidad del aire.**

|Contaminante|Decreto<br>Aplicable|Norma|Col4|Periodo de Evaluación de Cumplimiento de Norma|
|---|---|---|---|---|
|**Contaminante**|**Decreto**<br>**Aplicable**|**Valor**|**Unidad**|**Unidad**|
|Material Particulado<br>Respirable Fino<br>(MP2,5)|Decreto<br>Supremo<br>N°12/2011|50|μg/m3|Percentil 98 de las concentraciones de 24 horas|
|Material Particulado<br>Respirable Fino<br>(MP2,5)|Decreto<br>Supremo<br>N°12/2011|20|20|Concentración anual|
|Material Particulado<br>Respirable (MP10)|Decreto<br>Supremo<br>N°12/2022|130|μg/m3N|Percentil 98 de las concentraciones de 24 horas|
|Material Particulado<br>Respirable (MP10)|Decreto<br>Supremo<br>N°12/2022|50|50|Concentración anual|
|Monóxido de<br>Carbono (CO)|Decreto<br>Supremo<br>N°115/2002|30|mg/m3N|Percentil 99 de los máximos diarios de concentración<br>de 1 hora|
|Monóxido de<br>Carbono (CO)|Decreto<br>Supremo<br>N°115/2002|10|10|Percentil 99 de los máximos diarios de concentración<br>de 8 horas|
|Dióxido de<br>Nitrógeno (NO2)|Decreto<br>Supremo<br>N°114/2002|400|μg/m3N|Percentil 99 de los máximos diarios de concentración<br>de 1 hora|
|Dióxido de<br>Nitrógeno (NO2)|Decreto<br>Supremo<br>N°114/2002|100|100|Concentración anual|
|Dióxido de Azufre<br>(SO2)|Decreto<br>Supremo<br>N°104/2019|350|μg/m3N|Percentil 98,5 de las concentraciones de 1 hora.|
|Dióxido de Azufre<br>(SO2)|Decreto<br>Supremo<br>N°104/2019|150|150|Percentil 99 de las concentraciones de 24 horas|
|Dióxido de Azufre<br>(SO2)|Decreto<br>Supremo<br>N°104/2019|60|60|Concentración anual|
|Ozono (O3)|Decreto<br>Supremo<br>N°112/02|120|μg/m3N|Percentil 99 de los máximos diarios de concentración<br>de 8 horas|

Fuente: Elaboración propia.

83

www.dfmconsultores.cl

**info@dfmconsultores.cl**

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-14. Normas secundarias de calidad del aire.**

|Contaminante|Decreto<br>Aplicable|Norma|Col4|Periodo de Evaluación de Cumplimiento de Norma|
|---|---|---|---|---|
|**Contaminante**|**Decreto**<br>**Aplicable**|**Valor**|**Unidad**|**Unidad**|
|Material Particulado<br>Sedimentable (MPS)|Norma de la<br>Confederación<br>Suiza|200|mg/m2/día|Promedio aritmético depositación anual|
|Dióxido de Azufre<br>(SO2)|Decreto<br>Supremo<br>N°22/2010|1.000|μg/m3N|Percentil 99,73 de las concentraciones de 1 hora.|
|Dióxido de Azufre<br>(SO2)|Decreto<br>Supremo<br>N°22/2010|365|365|Percentil 99,7 de las concentraciones de 24 horas|
|Dióxido de Azufre<br>(SO2)|Decreto<br>Supremo<br>N°22/2010|80|80|Concentración anual|

Fuente: Elaboración propia.

84

www.dfmconsultores.cl

**info@dfmconsultores.cl**

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

**4.8** **Línea Base Medida de Calidad del Aire**

**4.8.1** **Estaciones**

Con el fin de elaborar una línea de base de calidad del aire, se han seleccionado aquellas estaciones de monitoreo cercanas a la

localización del Proyecto, para luego utilizar los datos públicos de estas, específicamente los datos disponibles para los contaminantes

a evaluar de acuerdo con lo presentado en la Tabla 4-13.

La información utilizada para elaborar la línea de base de calidad del aire fue recolectada a partir de datos obtenidos del sitio web del

Sistema Nacional de Información de Fiscalización Ambiental, sección Seguimiento Ambiental, de la Superintendencia del Medio

Ambiente [5] y de la web de Monitoreo en Línea Calidad del Aire Ambiental, de la Ilustre Municipalidad de Mejillones [6], para el período

2019-2021.

De esta forma, en la Tabla 4-15 se presentan las coordenadas de ubicación para las estaciones seleccionadas, junto con los

contaminantes medidos, el periodo de medición, el propietario, el operador y la fuente de información de cada una de ellas.

**Tabla 4-15. Caracterización de Estaciones de Monitoreo de Calidad del Aire Utilizadas para Línea de Base de Calidad del Aire.**

|Estación de<br>Monitoreo|Coordenadas UTM<br>(Datum WGS84)|Col3|Contaminantes Medidos|Periodo de Datos Disponibles<br>por Contaminante|Propietario|Operador|Fuente de Información|
|---|---|---|---|---|---|---|---|
|**Estación de**<br>**Monitoreo**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|JJ Latorre|352.064|7.444.407|Material Particulado<br>Respirable (MP10)|1 de enero 2019 al 31 de<br>diciembre 2021|ENAEX|Algoritmos|https://snifa.sma.gob.cl/S<br>eguimientoAmbiental/Fic<br>ha/123141|
|JJ Latorre|352.064|7.444.407|Dióxido de Nitrógeno (NO2)|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|

5 https://snifa.sma.gob.cl/SeguimientoAmbiental
6 [Link web: https://www.mejillones.cl/2018/08/17/monitoreo-en-linea-calidad-del-aire-ambiental/](https://www.mejillones.cl/2018/08/17/monitoreo-en-linea-calidad-del-aire-ambiental/)

www.dfmconsultores.cl

**info@dfmconsultores.cl**

85

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

|Estación de<br>Monitoreo|Coordenadas UTM<br>(Datum WGS84)|Col3|Contaminantes Medidos|Periodo de Datos Disponibles<br>por Contaminante|Propietario|Operador|Fuente de Información|
|---|---|---|---|---|---|---|---|
|**Estación de**<br>**Monitoreo**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Jardín Infantil|352.064|7.444.407|Material Particulado<br>Respirable (MP10)|1 de enero 2019 al 31 de<br>diciembre 2021|ENAEX|Algoritmos|https://snifa.sma.gob.cl/S<br>eguimientoAmbiental/Fic<br>ha/123141|
|Jardín Infantil|352.064|7.444.407|Dióxido de Nitrógeno (NO2)|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|
|Puerto Mejillones|352.047|7.444.688|Material Particulado<br>Respirable (MP10)|1 de enero 2019 al 30 de<br>septiembre 2021|Puerto<br>Mejillones|Algoritmos|https://www.puertomejill<br>ones.cl/monitoreo-<br>ambiental/|
|Ferrocarril|350.017|7.444.552|Material Particulado<br>Respirable Fino (MP2.5)|1 de enero 2017 al 31 de<br>diciembre 2019|ENIGE|Algoritmos|https://snifa.sma.gob.cl/S<br>eguimientoAmbiental/Fic<br>ha/93163|
|Ferrocarril|350.017|7.444.552|Material Particulado<br>Respirable (MP10)|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|
|Ferrocarril|350.017|7.444.552|Monóxido de Carbono (CO)|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|
|Ferrocarril|350.017|7.444.552|Dióxido de Nitrógeno (NO2)|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|
|Ferrocarril|350.017|7.444.552|Dióxido de Azufre (SO2)|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|
|Ferrocarril|350.017|7.444.552|Ozono (O3)|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|1 de enero 2017 al 31 de<br>diciembre 2019|
|Angamos 1|357.839|7.446.453|Material Particulado<br>Respirable (MP10)|1 de enero 2019 al 31 de<br>diciembre 2021|AES GENER|CESMEC|https://snifa.sma.gob.cl/S<br>eguimientoAmbiental/Fic<br>ha/121792<br>|
|Angamos 1|357.839|7.446.453|Dióxido de Nitrógeno (NO2)|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|
|Angamos 1|357.839|7.446.453|Dióxido de Azufre (SO2)|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|
|Molyb|358.938|7.447.360|Material Particulado<br>Respirable Fino (MP2.5)|1 de enero 2019 al 31 de<br>diciembre 2021|MOLYB|Algoritmos||

www.dfmconsultores.cl

**info@dfmconsultores.cl**

86

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

|Estación de<br>Monitoreo|Coordenadas UTM<br>(Datum WGS84)|Col3|Contaminantes Medidos|Periodo de Datos Disponibles<br>por Contaminante|Propietario|Operador|Fuente de Información<br>https://snifa.sma.gob.cl/S<br>eguimientoAmbiental/Fic<br>ha/121242|
|---|---|---|---|---|---|---|---|
|**Estación de**<br>**Monitoreo**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|**Estación de**<br>**Monitoreo**|||Material Particulado<br>Respirable (MP10)|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|
|**Estación de**<br>**Monitoreo**|||Dióxido de Nitrógeno (NO2)|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|
|**Estación de**<br>**Monitoreo**|||Dióxido de Azufre (SO2)|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|
|Molynor|358.945|7.448.107|Material Particulado<br>Respirable (MP10)|1 de enero 2019 al 31 de<br>diciembre 2021|MOLYNOR|Algoritmos|https://snifa.sma.gob.cl/S<br>eguimientoAmbiental/Fic<br>ha/121452|
|Molynor|358.945|7.448.107|Dióxido de Nitrógeno (NO2)|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|
|Molynor|358.945|7.448.107|Dióxido de Azufre (SO2)|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|
|Subestación Eléctrica|354.703|7.445.227|Material Particulado<br>Respirable (MP10)|1 de enero 2019 al 31 de<br>diciembre 2021|ENGIE|Algoritmos|https://snifa.sma.gob.cl/S<br>eguimientoAmbiental/Fic<br>ha/122284<br>|
|Subestación Eléctrica|354.703|7.445.227|Dióxido de Nitrógeno (NO2)|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|
|Subestación Eléctrica|354.703|7.445.227|Dióxido de Azufre (SO2)|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|1 de enero 2019 al 31 de<br>diciembre 2021|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia

87

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

De manera complementaria, en la Figura 4-35 se presenta la ubicación de las estaciones de

monitoreo de calidad del aire respecto a la zona de emplazamiento del proyecto.

**Figura 4-35. Ubicación Referencial Estaciones de Monitoreo de Calidad del Aire.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

88

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.8.2** **Estación JJ Latorre**

4.8.2.1 Material Particulado Respirable (MP10)

a) Serie de Tiempo

En la Figura 4-36 se muestran las series de datos de material particulado respirable (MP10)

monitoreados por la Estación JJ Latorre durante el periodo en estudio.

**Figura 4-36. Serie de Tiempo Material Particulado Respirable (MP10). Estación JJ Latorre.**

Fuente: Elaboración propia.

De la figura anterior es posible concluir de manera cualitativa que la estación de monitoreo

JJ Latorre ha registrado concentraciones por debajo de la norma de percentil 98 de 24 horas

y para la norma de periodo anual para material particulado respirable (MP10).

www.dfmconsultores.cl

**info@dfmconsultores.cl**

89

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

b) Resultados Monitoreo

En la Tabla 4-16 se presentan los resultados del monitoreo de material particulado

respirable (MP10) en la Estación JJ Latorre durante el periodo en estudio.

**Tabla 4-16. Resultados Monitoreo MP10. Estación JJ Latorre.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|MP10 (μg/m3N)|Número de datos medidos|121|122|122|
|MP10 (μg/m3N)|Número de datos válidos|114|107|114|
|MP10 (μg/m3N)|Porcentaje de datos válidos|94,2|87,7|93,4|
|MP10 (μg/m3N)|Mínimo diario|9|6|7|
|MP10 (μg/m3N)|Máximo diario|57|34|55|
|MP10 (μg/m3N)|Percentil 98 diario|35|27|39|
|MP10 (μg/m3N)|Media anual|21,9|18,0|21,7|
|MP10 (μg/m3N)|Media trianual|20,5|20,5|20,5|

Fuente: Elaboración propia.

c) Comparación con Normativa

En la Tabla 4-17 se presenta la comparación de los resultados del monitoreo de material

particulado respirable (MP10) en la Estación JJ Latorre con la normativa primaria de calidad

del aire durante el periodo en estudio.

**Tabla 4-17- Comparación de Monitoreo de MP10 con Normativa. Estación JJ Latorre.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|MP10|1 de enero de 2019 -<br>31 de diciembre de 20197|Percentil 98 de<br>la concentración<br>media diaria|35,0|130|μg/m3N|23,3%|
|MP10|1 de enero de 2019 -<br>31 de diciembre de 2021|Concentración<br>media trianual|20,2|50|μg/m3N|40,4%|

Fuente: Elaboración propia.

7 De manera conservadora se ha considerado el máximo valor de percentil 98 para el trienio analizado.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

90

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

De la tabla anterior es posible concluir de manera cuantitativa que la estación de monitoreo

JJ Latorre ha registrado concentraciones por debajo de la norma de percentil 98 de 24 horas

y de periodo anual para material particulado respirable (MP10).

4.8.2.2 Dióxido de Nitrógeno (NO 2 )

a) Resultados Monitoreo

En la Tabla 4-18 se presentan los resultados de monitoreo de dióxido de nitrógeno (NO 2 ) en

la Estación JJ Latorre durante el periodo en estudio.

**Tabla 4-18. Resultados de Monitoreo de NO** **2** **. Estación JJ Latorre** **[8]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|NO2 (μg/m3N)|Percentil 99 de los máximos diarios de<br>concentración horaria|40,2|43,4|46,2|
|NO2 (μg/m3N)|Promedio trianual percentil 99 de los<br>máximos diarios de concentración<br>horaria|43,2|43,2|43,2|
|NO2 (μg/m3N)|Media anual|5,0|4,3|4,4|
|NO2 (μg/m3N)|Media trianual|4,6|4,6|4,6|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-19 se presenta la comparación de los resultados del monitoreo de dióxido de

nitrógeno (NO 2 ) en la Estación JJ Latorre con la normativa primaria de calidad del aire para

el periodo en estudio.

**Tabla 4-19. Comparación de Monitoreo de NO** **2** **con Normativa. Estación JJ Latorre.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de la<br>Norma|
|---|---|---|---|---|---|---|
|NO2|1 de enero de 2019 -<br>31 de diciembre de 2021|Percentil 99 de<br>los máximos<br>diarios de<br>concentración de<br>1 hora|43,2|400|μg/m3N|10,8%|

8 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

91

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de la<br>Norma|
|---|---|---|---|---|---|---|
||1 de enero de 2019 -<br>31 de diciembre de 2021|Concentración<br>media trianual|4,6|100|μg/m3N|4,6%|

Fuente: Elaboración propia.

De la tabla anterior es posible concluir de manera cualitativa que la estación de monitoreo

JJ Latorre ha registrado concentraciones por debajo de la norma de concentración horaria

y anual para el contaminante dióxido de nitrógeno (NO 2 ).

**4.8.3** **Estación Jardín Infantil**

4.8.3.1 Material Particulado Respirable (MP10)

a) Serie de Tiempo

En la siguiente figura se muestran las series de datos de material particulado respirable

(MP10) monitoreados por la Estación Jardín Infantil durante el periodo en estudio.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

92

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-37. Serie de Tiempo Material Particulado Respirable (MP10). Estación Jardín Infantil.**

Fuente: Elaboración propia.

De la figura anterior es posible establecer de manera cualitativa que la estación de

monitoreo Jardín Infantil ha registrado concentraciones por bajo la norma de percentil 98

de 24 horas y de periodo anual para material particulado respirable (MP10).

b) Resultados Monitoreo

En la Tabla 4-20 se presentan los resultados del monitoreo de material particulado

respirable (MP10) en la Estación Jardín Infantil durante el periodo en estudio.

**Tabla 4-20. Resultados Monitoreo de MP10. Estación Jardín Infantil.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|MP10 (μg/m3N)|Número de datos medidos|121|122|122|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

93

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|**Contaminante**|Número de datos válidos|116|105|118|
|**Contaminante**|Porcentaje de datos válidos|95,9|86,1|96,7|
|**Contaminante**|Mínimo diario|4|7|8|
|**Contaminante**|Máximo diario|106|53|54|
|**Contaminante**|Percentil 98 diario|32|29|32|
|**Contaminante**|Media anual|20,4|18,7|18,8|
|**Contaminante**|Media trianual|19,3|19,3|19,3|

Fuente: Elaboración propia.

c) Comparación con Normativa

En la Tabla 4-21 se presenta la comparación de los resultados del monitoreo de material

particulado respirable (MP10) en la Estación Jardín Infantil con la normativa primaria de

calidad del aire durante el periodo en estudio.

**Tabla 4-21. Comparación de Monitoreo de MP10 con Normativa. Estación Jardín Infantil.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|MP10|1 de enero de 2020-<br>31 de diciembre de 20219|Percentil 98 de la<br>concentración media diaria|32,0|130|μg/m3N|24,6%|
|MP10|1 de enero de 2019 -<br>31 de diciembre de 2021|Concentración media<br>trianual|20,4|50|μg/m3N|40,8%|

Fuente: Elaboración propia.

De la tabla anterior se puede establecer de manera cuantitativa que la estación de

monitoreo Jardín Infantil ha registrado concentraciones bajo la norma de percentil 98 de 24

horas y de periodo anual para el contaminante material particulado respirable (MP10)

durante el periodo de estudio.

9 De manera conservadora se ha considerado el máximo valor de percentil 98 para el trienio analizado.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

94

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

4.8.3.2 Dióxido de Nitrógeno (NO 2 )

a) Resultados Monitoreo

En la Tabla 4-22 se presentan los resultados de monitoreo de dióxido de nitrógeno (NO 2 ) en

la Estación Jardín Infantil durante el periodo en estudio.

**Tabla 4-22. Resultados Monitoreo de NO** **2** **. Estación Jardín Infantil** **[10]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|NO2 (μg/m3N)|Percentil 99 de los máximos diarios de<br>concentración horaria|44,7|58,5|55,8|
|NO2 (μg/m3N)|Promedio trianual percentil 99 de los<br>máximos diarios de concentración horaria|53,0|53,0|53,0|
|NO2 (μg/m3N)|Media anual|7,1|6,6|7,2|
|NO2 (μg/m3N)|Media trianual|7,0|7,0|7,0|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-23 se presenta la comparación de los resultados del monitoreo de dióxido de

nitrógeno (NO 2 ) en la Estación Jardín Infantil con la normativa primaria de calidad del aire

para el periodo en estudio.

**Tabla 4-23. Comparación de Monitoreo de NO** **2** **con Normativa. Estación Jardín Infantil.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|NO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora|53,0|400|μg/m3N|13,3%|
|NO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Concentración media<br>trianual|7,0|100|μg/m3N|7,0%|

Fuente: Elaboración propia.

10 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

95

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

De la tabla anterior es posible concluir de manera cuantitativa que la estación de monitoreo

Jardín Infantil ha registrado concentraciones por debajo de la norma de concentración

horaria y anual para el contaminante dióxido de nitrógeno (NO 2 ).

**4.8.4** **Estación Puerto Mejillones**

4.8.4.1 Material Particulado Respirable (MP10)

a) Serie de Tiempo

En la Figura 4-38 se muestran las series de datos de material particulado respirable (MP10)

monitoreados por la Estación Puerto Mejillones durante el periodo en estudio.

**Figura 4-38. Serie de Tiempo Material Particulado Respirable (MP10). Estación Puerto Mejillones.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

96

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

De la figura anterior es posible concluir de manera cualitativa que la estación de monitoreo

Puerto Mejillones ha registrado concentraciones por debajo de la norma de percentil 98 de

24 horas y para la norma de periodo anual de material particulado respirable (MP10).

b) Resultados Monitoreo

En la Tabla 4-24 se presentan los resultados del monitoreo de material particulado

respirable (MP10) en la Estación Puerto Mejillones durante el periodo en estudio.

**Tabla 4-24. Resultados Monitoreo de MP10. Estación Puerto Mejillones.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019 **|**2020 **|**2021 **|
|MP10 (μg/m3N)|Número de datos medidos|121|122|91|
|MP10 (μg/m3N)|Número de datos válidos|116|105|85|
|MP10 (μg/m3N)|Porcentaje de datos válidos|95,9|86,1|93,4|
|MP10 (μg/m3N)|Mínimo diario|6|8|5|
|MP10 (μg/m3N)|Máximo diario|108|36|50|
|MP10 (μg/m3N)|Percentil 98 diario|29|29|34|
|MP10 (μg/m3N)|Media anual|20,0|19,5|20,411|
|MP10 (μg/m3N)|Media trianual|20,0|20,0|20,0|

Fuente: Elaboración propia.

c) Comparación con Normativa

En la Tabla 4-25 se presenta la comparación de los resultados del monitoreo de material

particulado respirable (MP10) en la Estación Puerto Mejillones con la normativa primaria

de calidad del aire durante el periodo en estudio.

**Tabla 4-25. Comparación de Monitoreo de MP10 con Normativa. Estación Puerto Mejillones.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|MP10|1 de enero de 2021-<br>30 de septiembre de<br>202112|Percentil 98 de la<br>concentración media diaria|34,0|130|μg/m3N|26,2%|
|MP10|1 de enero de 2018 -<br>30 de septiembre de 2021|Concentración media<br>trianual|20,0|50|μg/m3N|40,0%|

11 De acuerdo a los D.S 59 se reemplazaron las medias mensuales de los 3 meses faltantes por el de máxima

media mensual de los 12 meses anteriores.
12 De manera conservadora se ha considerado el máximo valor de percentil 98 para el trienio analizado.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

97

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Fuente: Elaboración propia.

De la tabla anterior se puede concluir de manera cuantitativa que la estación de monitoreo

Puerto Mejillones ha registrado concentraciones bajo la norma de percentil 98 de 24 horas

y de periodo anual para el contaminante material particulado respirable (MP10) durante el

periodo de estudio.

**4.8.5** **Estación Ferrocarril**

4.8.5.1 Material Particulado Respirable Fino (MP2,5)

a) Resultados Monitoreo

En la Tabla 4-26 se presentan los resultados del monitoreo de material particulado

respirable fino (MP2,5) en la Estación Ferrocarril durante el periodo en estudio.

**Tabla 4-26. Resultados Monitoreo MP2,5. Estación Ferrocarril** **[13]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2017**|**2018**|**2019**|
|MP2,5 (μg/m3)|Percentil 98 diario|23,0|20,0|17,0|
|MP2,5 (μg/m3)|Media anual|10,0|10,0|7,0|
|MP2,5 (μg/m3)|Media trianual|9,0|9,0|9,0|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-27 se presenta la comparación de los resultados del monitoreo de material

particulado respirable fino (MP2,5) en la Estación Ferrocarril con la normativa primaria de

calidad del aire durante el periodo en estudio.

**Tabla 4-27. Comparación de Monitoreo de MP2,5 con Normativa. Estación Ferrocarril.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|MP2,5|1 de enero de 2017 -|Percentil 98 de la<br>concentración<br>media diaria|23,0|50|μg/m3|46,0%|

13 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

98

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
||31 de diciembre de 201714||||||
||1 de enero de 2017-<br>31 de diciembre de 2019|Concentración<br>media trianual|9,0|20|μg/m3|45,0%|

Fuente: Elaboración propia.

De la tabla anterior se puede concluir de manera cuantitativa que la estación de monitoreo

Ferrocarril ha registrado concentraciones bajo la norma de percentil 98 de 24 horas y de

periodo anual para el contaminante material particulado respirable fino (MP2,5) durante el

periodo en estudio.

4.8.5.2 Material Particulado Respirable (MP10)

a) Resultados Monitoreo

En la Tabla 4-28 se presentan los resultados del monitoreo de material particulado

respirable (MP10) en la Estación Ferrocarril durante el periodo en estudio.

**Tabla 4-28 - Resultados Monitoreo de MP10. Estación Ferrocarril** **[15]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2017**|**2018**|**2019**|
|MP10 (μg/m3N)|Percentil 98 diario|32,0|41,0|28,0|
|MP10 (μg/m3N)|Media anual|16,0|15,0|16,0|
|MP10 (μg/m3N)|Media trianual|15,7|15,7|15,7|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la siguiente tabla se presenta la comparación de los resultados del monitoreo de material

particulado respirable (MP10) en la Estación Ferrocarril con la normativa primaria de calidad

del aire durante el periodo de estudio.

14 De manera conservadora se ha considerado el máximo valor del percentil 98 para el trienio analizado.
15 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

99

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-29 - Comparación de Monitoreo de MP10 con Normativa. Estación Ferrocarril.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|MP10|1 de enero de 2018 -<br>31 de diciembre de 201816|Percentil 98 de la<br>concentración<br>media diaria|41,0|130|μg/m3N|31,5%|
|MP10|1 de enero de 2017 -<br>31 de diciembre de 2019|Concentración<br>media trianual|15,7|50|μg/m3N|31,3%|

Fuente: Elaboración propia.

De la tabla anterior se puede concluir de manera cuantitativa que la estación de monitoreo

Ferrocarril ha registrado concentraciones bajo la norma de percentil 98 de 24 horas y de

periodo anual para el contaminante material particulado respirable (MP10) durante el

periodo en estudio.

4.8.5.3 Dióxido de Nitrógeno (NO 2 )

a) Resultados Monitoreo

En la Tabla 4-30 se presentan los resultados de monitoreo de dióxido de nitrógeno (NO 2 ) en

la Estación Ferrocarril durante el periodo en estudio.

**Tabla 4-30. Resultados Monitoreo de NO** **2** **. Estación Ferrocarril** **[17]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2017**|**2018**|**2019**|
|NO2 (μg/m3N)|Percentil 99 de los máximos diarios de<br>concentración horaria|35,5|42,2|40,5|
|NO2 (μg/m3N)|Promedio trianual percentil 99 de los<br>máximos diarios de concentración horaria|39,4|39,4|39,4|
|NO2 (μg/m3N)|Media anual|2,7|2,5|2,3|
|NO2 (μg/m3N)|Media trianual|2,5|2,5|2,5|

Fuente: Elaboración propia.

16 De manera conservadora se ha considerado el máximo valor del percentil 98 para el trienio analizado.
17 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

100

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

b) Comparación con Normativa

En la Tabla 4-31 se presenta la comparación de los resultados del monitoreo de dióxido de

nitrógeno (NO 2 ) en la Estación Ferrocarril con la normativa primaria de calidad del aire para

el periodo en estudio.

**Tabla 4-31. Comparación de Monitoreo de NO** **2** **con Normativa. Estación Ferrocarril.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|NO2|1 de enero de 2017 -<br>31 de diciembre de 2019|Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora|39,4|400|μg/m3N|9,9%|
|NO2|1 de enero de 2017 -<br>31 de diciembre de 2019|Concentración media<br>trianual|2,5|100|μg/m3N|2,5%|

Fuente: Elaboración propia.

De la tabla anterior es posible concluir de manera cuantitativa que la estación de monitoreo

Ferrocarril ha registrado concentraciones por debajo de la norma de concentración horaria

y anual para el contaminante dióxido de nitrógeno (NO 2 ).

4.8.5.4 Dióxido de Azufre (SO 2 )

a) Resultados Monitoreo

En la Tabla 4-32 se presentan los resultados del monitoreo de dióxido de azufre (SO 2 ) en la

Estación Ferrocarril durante el periodo en estudio.

**Tabla 4-32 - Resultados Monitoreo de SO** **2** **. Estación Ferrocarril** **[18]** .

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2017**|**2018**|**2019**|
|SO2 (μg/m3N)|Percentil 98,5 de concentración horaria|-|-|8,4|
|SO2 (μg/m3N)|Promedio trianual percentil 98,5 de<br>concentración horaria|8,4|8,4|8,4|
|SO2 (μg/m3N)|Percentil 99 de concentración diaria|6,0|5,5|7,5|
|SO2 (μg/m3N)|Promedio trianual percentil 99 de<br>concentración diaria|6,3|6,3|6,3|

Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

101

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2017**|**2018**|**2019**|
|**Contaminante**|Media anual|1,8|1,7|2,0|
|**Contaminante**|Media trianual|1,8|1,8|1,8|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-33 se presenta la comparación de los resultados del monitoreo de dióxido de

azufre (SO 2 ) en la Estación Ferrocarril con la normativa primaria de calidad del aire durante

el periodo en estudio.

**Tabla 4-33 - Comparación de Monitoreo de SO** **2** **con Normativa. Estación Ferrocarril.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|SO2|1 de enero de 2017 -<br>31 de diciembre de 2019|Percentil 98,5 de<br>concentración<br>horaria|8,4|350|μg/m3N|2,4%|
|SO2|1 de enero de 2017 -<br>31 de diciembre de 2019|Percentil 98 de la<br>concentración<br>media diaria|6,3|150|μg/m3N|4,2%|
|SO2|1 de enero de 2017 -<br>31 de diciembre de 2019|Concentración<br>media trianual|1,8|60|μg/m3N|3,1%|

Fuente: Elaboración propia.

De la tabla anterior se puede concluir de manera cuantitativa que la estación de monitoreo

Ferrocarril ha registrado concentraciones por bajo la norma de concentración horaria, diaria

y anual para el contaminante dióxido de azufre (SO 2 ) durante el periodo de estudio.

4.8.5.5 Monóxido de Carbono (CO)

a) Resultados Monitoreo

En la Tabla 4-34 se presentan los resultados del monitoreo de monóxido de carbono (CO)

en la Estación Ferrocarril durante el periodo en estudio.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

102

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-34. Resultados Monitoreo de CO. Estación Ferrocarril** **[19]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2017**|**2018**|**2019**|
|CO (mg/m3N)|Percentil 99 de los máximos diarios de<br>concentración horaria|0,4|0,3|0,4|
|CO (mg/m3N)|Promedio trianual percentil 99 de los máximos<br>diarios de concentración horaria|0,4|0,4|0,4|
|CO (mg/m3N)|Percentil 99 de los máximos diarios de<br>concentración media móvil de 8 horas|0,3|0,3|0,3|
|CO (mg/m3N)|Promedio trianual percentil 99 de los máximos<br>diarios de concentración media móvil de 8 horas|0,3|0,3|0,3|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-35 se presenta la comparación de los resultados del monitoreo de monóxido

de carbono (CO) en la Estación Ferrocarril con la normativa primaria de calidad del aire

durante el periodo en estudio.

**Tabla 4-35. Comparación de Monitoreo de CO con Normativa. Estación Ferrocarril.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|CO|1 de enero de 2017 -<br>31 de diciembre de 2019|Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora|0,4|30|mg/m3N|1,2%|
|CO|1 de enero de 2017 -<br>31 de diciembre de 2019|Percentil 99 de los<br>máximos diarios de<br>concentración de 8 horas|0,3|10|mg/m3N|3,0%|

Fuente: Elaboración propia.

De la tabla anterior se puede concluir de manera cuantitativa que la estación de monitoreo

Ferrocarril ha registrado concentraciones por bajo la norma de percentil 99 de 1 hora y de

8 horas para el contaminante monóxido de carbono (CO).

19 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

103

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

4.8.5.6 Ozono (O 3 )

a) Resultados Monitoreo

En la Tabla 4-36 se presentan los resultados del monitoreo de ozono (O 3 ) en la Estación

Ferrocarril durante el periodo en estudio.

**Tabla 4-36. Resultados Monitoreo de O3. Estación Ferrocarril** **[20]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2017**|**2018**|**2019**|
|O3 (μg/m3N)|Percentil 99 de los máximos diarios de<br>concentración media móvil de 8 horas|57,0|55,0|58,0|
|O3 (μg/m3N)|Promedio trianual percentil 99 de los máximos<br>diarios de concentración media móvil de 8 horas|56,7|56,7|56,7|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-37 se presenta la comparación de los resultados del monitoreo de ozono (O 3 )

en la Estación Ferrocarril con la normativa primaria de calidad del aire durante el periodo

en estudio.

**Tabla 4-37. Comparación de Monitoreo de O** **3** **con Normativa. Estación Ferrocarril.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|O3|1 de enero de 2017 -<br>31 de diciembre de 2019|Percentil 99 de los<br>máximos diarios de<br>concentración de 8 horas|56,7|120|μg/m3N|47,2%|

Fuente: Elaboración propia.

De la tabla anterior se puede concluir de manera cuantitativa que la estación de monitoreo

Ferrocarril ha registrado concentraciones por bajo la norma de percentil 99 de 8 horas para

el contaminante ozono (O 3 ).

20 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

104

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.8.6** **Angamos 1**

4.8.6.1 Material Particulado Respirable (MP10)

a) Resultados Monitoreo

En la Tabla 4-38 se presentan los resultados del monitoreo de material particulado

respirable (MP10) en la Estación Angamos 1 durante el periodo en estudio.

**Tabla 4-38. Resultados Monitoreo de MP10. Estación Angamos 1** **[21]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|MP10 (μg/m3N)|Percentil 98 diario|23,7|29,2|39,6|
|MP10 (μg/m3N)|Media anual|13,0|15,0|23,8|
|MP10 (μg/m3N)|Media trianual|17,3|17,3|17,3|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-39 se exhibe la comparación de los resultados del monitoreo de material

particulado respirable (MP10) en la Estación Angamos 1 con la normativa primaria de

calidad del aire durante el periodo en estudio.

**Tabla 4-39. Comparación de Monitoreo de MP10 con Normativa. Estación Angamos 1.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|MP10|1 de enero de 2021-<br>31 de diciembre de 202122|Percentil 98 de la<br>concentración<br>media diaria|39,6|130|μg/m3N|30,5%|
|MP10|1 de enero de 2019 -<br>31 de diciembre de 2021|Concentración<br>media trianual|17,3|50|μg/m3N|34,5%|

Fuente: Elaboración propia.

21 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.
22 De manera conservadora se ha considerado el máximo valor de percentil 98 para el trienio analizado.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

105

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

De la tabla anterior se puede concluir de manera cuantitativa que la estación de monitoreo

Angamos 1 ha registrado concentraciones por bajo la norma de percentil 98 de 24 horas y

de periodo anual para material particulado respirable (MP10).

4.8.6.2 Dióxido de Nitrógeno (NO 2 )

a) Resultados Monitoreo

En la Tabla 4-40 se muestran los resultados del monitoreo de dióxido de nitrógeno (NO 2 ) en

la Estación Angamos 1 durante el periodo en estudio.

**Tabla 4-40. Resultados Monitoreo de NO** **2** **. Estación Angamos 1** **[23]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|NO2 (μg/m3N)|Percentil 99 de los máximos diarios de<br>concentración horaria|121,9|46,7|43,1|
|NO2 (μg/m3N)|Promedio trianual percentil 99 de los<br>máximos diarios de concentración horaria|70,6|70,6|70,6|
|NO2 (μg/m3N)|Media anual|12,2|8,4|6,7|
|NO2 (μg/m3N)|Media trianual|9,1|9,1|9,1|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-41 se presenta la comparación de los resultados del monitoreo de dióxido de

nitrógeno (NO 2 ) en la Estación Angamos 1 con la normativa primaria de calidad del aire

durante el periodo en estudio.

23 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

106

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-41. Comparación de Monitoreo de NO** **2** **con Normativa. Estación Angamos 1.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|NO2|1 de enero de 2019 -<br>31 de diciembre de 2021|Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora|70,6|400|μg/m3N|17,7%|
|NO2|1 de enero de 2019 -<br>31 de diciembre de 2021|Concentración media<br>trianual|9,1|100|μg/m3N|9,1%|

Fuente: Elaboración propia.

De la tabla anterior se puede establecer de manera cuantitativa que la estación de

monitoreo Angamos 1 ha registrado concentraciones por bajo la norma de concentración

horaria y de periodo anual para el contaminante dióxido de nitrógeno (NO 2 ).

4.8.6.3 Dióxido de Azufre (SO 2 )

a) Resultados Monitoreo

En la Tabla 4-42 se presentan los resultados del monitoreo de dióxido de azufre (SO 2 ) en la

Estación Angamos 1 durante el periodo en estudio.

**Tabla 4-42. Resultados Monitoreo de SO** **2** **. Estación Angamos 1** **[24]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|SO2 (μg/m3N)|Percentil 98,5 de concentración horaria|17,8|17,3|29,8|
|SO2 (μg/m3N)|Promedio trianual percentil 98,5 de<br>concentración horaria|21,6|21,6|21,6|
|SO2 (μg/m3N)|Percentil 99 de concentración diaria|12,8|16,0|22,5|
|SO2 (μg/m3N)|Promedio trianual percentil 99 de<br>concentración diaria|17,1|17,1|17,1|
|SO2 (μg/m3N)|Media anual|5,1|5,2|7,3|
|SO2 (μg/m3N)|Media trianual|5,9|5,9|5,9|

Fuente: Elaboración propia.

24 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

107

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

b) Comparación con Normativa

En la Tabla 4-43 se presenta la comparación de los resultados del monitoreo de dióxido de

azufre (SO 2 ) en la Estación Angamos 1 con la normativa primaria de calidad del aire durante

el periodo en estudio.

**Tabla 4-43 - Comparación de Monitoreo de SO** **2** **con Normativa. Estación Angamos 1.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|SO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Percentil 98,5 de<br>concentración<br>horaria|21,6|350|μg/m3N|6,2%|
|SO2|1 de enero de 2017 - 31<br>de diciembre de 2021|Percentil 98 de la<br>concentración<br>media diaria|17,1|150|μg/m3N|11,4%|
|SO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Concentración<br>media trianual|5,9|60|μg/m3N|9,8%|

Fuente: Elaboración propia.

De la tabla anterior se puede concluir de manera cuantitativa que la estación de monitoreo

Angamos 1 ha registrado concentraciones de dióxido de azufre (SO 2 ) por bajo la norma de

percentil 98,5 de 1 hora, percentil 99 de 24 horas y de periodo anual.

**4.8.7** **Estación MOLYB**

4.8.7.1 Material Particulado Respirable Fino (MP2,5)

a) Resultados Monitoreo

En la Tabla 4-44 se presentan los resultados del monitoreo de material particulado

respirable fino (MP2,5) en la Estación MOLYB durante el periodo en estudio.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

108

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-44. Resultados Monitoreo MP2,5. Estación MOLYB** **[25]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|MP2,5 (μg/m3)|Percentil 98 diario|24,0|18,0|23,0|
|MP2,5 (μg/m3)|Media anual|15,0|9,0|9,0|
|MP2,5 (μg/m3)|Media trianual|11,0|11,0|11,0|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-45 se presenta la comparación de los resultados del monitoreo de material

particulado respirable fino (MP2,5) en la Estación MOLYB con la normativa primaria de

calidad del aire durante el periodo en estudio.

**Tabla 4-45. Comparación de Monitoreo de MP2,5 con Normativa. Estación MOLYB.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|MP2,5|1 de enero de 2019-<br>31 de diciembre de 202126|Percentil 98 de la<br>concentración<br>media diaria|24,0|50|μg/m3|48,0%|
|MP2,5|1 de enero de 2019 -<br>31 de diciembre de 2021|Concentración<br>media trianual|11,0|20|μg/m3|55,0%|

Fuente: Elaboración propia.

De la tabla anterior se puede concluir de manera cuantitativa que la estación de monitoreo

MOLYB ha registrado concentraciones bajo la norma de percentil 98 de 24 horas y de

periodo anual para el contaminante material particulado respirable fino (MP2,5) durante el

periodo en estudio.

25 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.
26 De manera conservadora se ha considerado el máximo valor de percentil 98 para el trienio analizado.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

109

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

4.8.7.2 Material Particulado Respirable (MP10)

a) Resultados Monitoreo

En la Tabla 4-46 se presentan los resultados del monitoreo de material particulado

respirable (MP10) en la Estación MOLYB durante el periodo en estudio.

**Tabla 4-46. Resultados Monitoreo de MP10. Estación MOLYB** **[27]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|MP10 (μg/m3N)|Percentil 98 diario|52,0|35,0|39,0|
|MP10 (μg/m3N)|Media anual|24,0|18,0|22,0|
|MP10 (μg/m3N)|Media trianual|21,3|21,3|21,3|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-47 se presenta la comparación de los resultados del monitoreo de material

particulado respirable (MP10) en la Estación MOLYB con la normativa primaria de calidad

del aire durante el periodo en estudio.

**Tabla 4-47. Comparación de Monitoreo de MP10 con Normativa. Estación MOLYB.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|MP10|1 de enero de 2019-<br>31 de diciembre de 202128|Percentil 98 de la<br>concentración<br>media diaria|52,0|130|μg/m3N|40,0%|
|MP10|1 de enero de 2018 -<br>31 de diciembre de 2021|Concentración<br>media trianual|21,3|50|μg/m3N|42,6%|

Fuente: Elaboración propia.

De la tabla anterior, se puede concluir de manera cuantitativa que la estación de monitoreo

MOLYB ha registrado concentraciones bajo la norma de percentil 98 de 24 horas y de

27 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.
28 De manera conservadora se ha considerado el máximo valor de percentil 98 para el trienio analizado.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

110

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

periodo anual para el contaminante material particulado respirable (MP10) durante el

periodo en estudio.

4.8.7.3 Dióxido de Nitrógeno (NO 2 )

a) Resultados Monitoreo

En la Tabla 4-48 se exhiben los resultados del monitoreo de dióxido de nitrógeno (NO 2 ) en

la Estación MOLYB durante el periodo en estudio.

**Tabla 4-48. Resultados Monitoreo de NO** **2** **. Estación MOLYB** **[29]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|NO2 (μg/m3N)|Percentil 99 de los máximos diarios de<br>concentración horaria|50,3|52,0|56,3|
|NO2 (μg/m3N)|Promedio trianual percentil 99 de los<br>máximos diarios de concentración horaria|52,9|52,9|52,9|
|NO2 (μg/m3N)|Media anual|7,7|10,0|9,3|
|NO2 (μg/m3N)|Media trianual|9,0|9,0|9,0|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-49 se presenta la comparación de los resultados del monitoreo de dióxido de

nitrógeno (NO 2 ) en la Estación MOLYB con la normativa primaria de calidad del aire durante

el periodo en estudio.

**Tabla 4-49. Comparación de Monitoreo de NO** **2** **con Normativa. Estación MOLYB.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|NO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora|52,9|400|μg/m3N|13,2%|
|NO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Concentración media<br>trianual|9,0|100|μg/m3N|9,0%|

29 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

111

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Fuente: Elaboración propia.

De la tabla anterior se puede establecer de manera cuantitativa que la estación de

monitoreo MOLYB ha registrado concentraciones por bajo la norma de concentración

horaria y anual para el contaminante dióxido de nitrógeno (NO 2 ).

4.8.7.4 Dióxido de Azufre (SO 2 )

a) Resultados Monitoreo

En la Tabla 4-50 se presentan los resultados del monitoreo de dióxido de azufre (SO 2 ) en la

Estación MOLYB durante el periodo en estudio.

**Tabla 4-50. Resultados Monitoreo de SO** **2** **. Estación MOLYB** **[30]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2018**|**2019**|**2020**|
|SO2 (μg/m3N)|Percentil 98,5 de concentración<br>horaria|209,6|196,4|309,8|
|SO2 (μg/m3N)|Promedio trianual percentil 98,5 de<br>concentración horaria|238,6|238,6|238,6|
|SO2 (μg/m3N)|Percentil 99 de concentración diaria|96,9|100,8|310|
|SO2 (μg/m3N)|Promedio trianual percentil 99 de<br>concentración diaria|169,2|169,2|169,2|
|SO2 (μg/m3N)|Media anual|23,4|24,2|43,6|
|SO2 (μg/m3N)|Media trianual|30,4|30,4|30,4|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-51 se presenta la comparación de los resultados del monitoreo de dióxido de

azufre (SO 2 ) en la Estación MOLYB con la normativa primaria de calidad del aire durante el

periodo en estudio.

30 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

112

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-51 - Comparación de Monitoreo de SO** **2** **con Normativa. Estación MOLYB** .

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|SO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Percentil 98,5 de<br>concentración<br>horaria|238,6|350|μg/m3N|68,2%|
|SO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Percentil 98 de la<br>concentración media<br>diaria|169,2|150|μg/m3N|112,8%|
|SO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Concentración media<br>trianual|30,4|60|μg/m3N|50,6%|

Fuente: Elaboración propia.

De la tabla anterior se puede concluir de manera cuantitativa que la estación de monitoreo

MOLYB ha registrado concentraciones de dióxido de azufre (SO 2 ) por bajo la norma de

percentil 98,5 de 1 hora y de periodo anual; no obstante, se sobrepasa la norma de percentil

99 de 24 horas, donde la concentración obtenida es de 169,2 μg/m [3] N, equivalente a un

112,8% del valor normado.

**4.8.8** **Estación MOLYNOR**

4.8.8.1 Material Particulado Respirable (MP10)

a) Resultados Monitoreo

En la Tabla 4-52 se exhiben los resultados del monitoreo de material particulado respirable

(MP10) en la Estación MOLYNOR durante el periodo en estudio.

**Tabla 4-52. Resultados Monitoreo de MP10. Estación MOLYNOR** **[31]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2018**|**2019**|**2020**|
|MP10 (μg/m3N)|Percentil 98 diario|75,0|48,0|61,0|
|MP10 (μg/m3N)|Media trianual|30,0|30,0|30,0|

Fuente: Elaboración propia.

31 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

113

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

b) Comparación con Normativa

En la Tabla 4-53 se presenta la comparación de los resultados del monitoreo de material

particulado respirable (MP10) en la Estación MOLYNOR con la normativa primaria de

calidad del aire durante el periodo en estudio.

**Tabla 4-53. Comparación de Monitoreo de MP10 con Normativa. Estación MOLYNOR.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|MP10|1 de enero de 2019 -<br>31 de diciembre de 202132|Percentil 98 de la<br>concentración<br>media diaria|75,0|130|μg/m3N|57,8%|
|MP10|1 de enero de 2019 -<br>31 de diciembre de 2021|Concentración<br>media trianual|30,0|50|μg/m3N|60,0%|

Fuente: Elaboración propia.

De la tabla anterior es posible concluir de manera cuantitativa que la estación de monitoreo

MOLYNOR ha registrado concentraciones por bajo la norma de percentil 98 de 24 horas y

de periodo anual, por lo que no existe una condición de saturación de material particulado

respirable (MP10) para dichos periodos.

4.8.8.2 Dióxido de Nitrógeno (NO 2 )

a) Resultados Monitoreo

En la Tabla 4-54 se exhiben los resultados del monitoreo de dióxido de nitrógeno (NO 2 ) en

la Estación MOLYNOR durante el periodo en estudio.

**Tabla 4-54. Resultados Monitoreo de NO** **2** **. Estación MOLYNOR** **[33]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|NO2 (μg/m3N)|Percentil 99 de los máximos diarios de<br>concentración horaria|41,8|35,5|90,1|
|NO2 (μg/m3N)|Promedio trianual percentil 99 de los<br>máximos diarios de concentración horaria|39,3|39,3|39,3|

32 De manera conservadora se ha considerado el máximo valor del percentil 98 para el trienio analizado.
33 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

114

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|**Contaminante**|Media anual|6,2|5,7|7,7|
|**Contaminante**|Media trianual|6,5|6,5|6,5|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-55 se presenta la comparación de los resultados del monitoreo de dióxido de

nitrógeno (NO 2 ) en la Estación MOLYNOR con la normativa primaria de calidad del aire

durante el periodo de estudio.

**Tabla 4-55. Comparación de Monitoreo de NO** **2** **con Normativa. Estación MOLYNOR.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|NO2|1 de enero de 2019 -<br>31 de diciembre de 2021|Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora|39,3|400|μg/m3N|9,8%|
|NO2|1 de enero de 2019 -<br>31 de diciembre de 2021|Concentración media<br>trianual|6,5|100|μg/m3N|6,5%|

Fuente: Elaboración propia.

De la tabla anterior es posible concluir de manera cuantitativa que la estación de monitoreo

MOLYNOR ha registrado concentraciones por bajo la norma de concentración horaria y

anual para el contaminante dióxido de nitrógeno (NO 2 ).

4.8.8.3 Dióxido de Azufre (SO 2 )

a) Resultados Monitoreo

En la Tabla 4-56 se presentan los resultados del monitoreo de dióxido de azufre (SO 2 ) en la

Estación MOLYNOR durante el periodo en estudio.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

115

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-56. Resultados Monitoreo de SO** **2** **. Estación MOLYNOR** **[34]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|SO2 (μg/m3N)|Percentil 98,5 de concentración<br>horaria|64,1|47,4|44,8|
|SO2 (μg/m3N)|Promedio trianual percentil 98,5 de<br>concentración horaria|52,1|52,1|52,1|
|SO2 (μg/m3N)|Percentil 99 de concentración diaria|50,5|36,6|106,6|
|SO2 (μg/m3N)|Promedio trianual percentil 99 de<br>concentración diaria|64,6|64,6|64,6|
|SO2 (μg/m3N)|Media anual|6,7|7,5|12,1|
|SO2 (μg/m3N)|Media trianual|8,8|8,8|8,8|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-57 se presenta la comparación de los resultados del monitoreo de dióxido de

azufre (SO 2 ) en la Estación MOLYNOR con la normativa primaria de calidad del aire durante

el periodo en estudio.

**Tabla 4-57 - Comparación de Monitoreo de SO** **2** **con Normativa. Estación MOLYNOR.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|SO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Percentil 98,5 de<br>concentración<br>horaria|64,6|350|μg/m3N|18,5%|
|SO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Percentil 98 de la<br>concentración<br>media diaria|52,1|150|μg/m3N|34,7%|
|SO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Concentración<br>media trianual|8,8|60|μg/m3N|14,6%|

Fuente: Elaboración propia.

34 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

116

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

De la tabla anterior se puede concluir de manera cuantitativa que la estación de monitoreo

MOLYNOR ha registrado concentraciones bajo la norma de concentración horaria, diaria y

anual para el contaminante dióxido de azufre (SO 2 ) durante el periodo en estudio.

**4.8.9** **Estación Subestación Eléctrica**

4.8.9.1 Material Particulado Respirable (MP10)

a) Resultados Monitoreo

En la Tabla 4-58 se exhiben los resultados del monitoreo de material particulado respirable

(MP10) en la Estación Subestación Eléctrica durante el periodo en estudio.

**Tabla 4-58. Resultados Monitoreo de MP10. Estación Subestación Eléctrica** **[35]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|MP10 (μg/m3N)|Percentil 98 diario|35,0|81,0|35,0|
|MP10 (μg/m3N)|Media anual|19,0|27,0|17,0|
|MP10 (μg/m3N)|Media trianual|21,0|21,0|21,0|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-59 se presenta la comparación de los resultados del monitoreo de material

particulado respirable (MP10) en la Estación Subestación Eléctrica con la normativa

primaria de calidad del aire durante el periodo en estudio.

**Tabla 4-59. Comparación de Monitoreo de MP10. Estación Subestación Eléctrica.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|MP10|1 de enero de 2019-<br>31 de diciembre de 202136|Percentil 98 de la<br>concentración media diaria|81,0|130|μg/m3N|62,3%|
|MP10|1 de enero de 2019 -<br>31 de diciembre de 2021|Concentración media<br>trianual|21,0|50|μg/m3N|42,0%|

Fuente: Elaboración propia.

35 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.
36 De manera conservadora se ha considerado el máximo valor del percentil 98 para el trienio analizado.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

117

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

De la tabla anterior se puede concluir de manera cuantitativa que la estación de monitoreo

Subestación Eléctrica ha registrado concentraciones por bajo la norma de percentil 98 de

24 horas y de periodo anual para material particulado respirable (MP10).

4.8.9.2 Dióxido de Nitrógeno (NO 2 )

a) Resultados Monitoreo

En la Tabla 4-60 se exhiben los resultados del monitoreo de dióxido de nitrógeno (NO 2 ) en

la Estación Subestación Eléctrica durante el periodo en estudio.

**Tabla 4-60. Resultados Monitoreo de NO** **2** **. Estación Subestación Eléctrica** **[37]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|NO2 (μg/m3N)|Percentil 99 de los máximos diarios de<br>concentración horaria|51,8|57,0|57,0|
|NO2 (μg/m3N)|Promedio trianual percentil 99 de los<br>máximos diarios de concentración horaria|55,3|55,3|55,3|
|NO2 (μg/m3N)|Media anual|5,7|6,0|6,2|
|NO2 (μg/m3N)|Media trianual|6,0|6,0|6,0|

Fuente: Elaboración propia.

b) Comparación con Normativa

En la Tabla 4-61 se presenta la comparación de los resultados del monitoreo de dióxido de

nitrógeno (NO 2 ) en la Estación Subestación Eléctrica con la normativa primaria de calidad

del aire durante el periodo en estudio.

**Tabla 4-61. Comparación de Monitoreo de NO** **2** **con Normativa. Estación Subestación Eléctrica.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|NO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora|55,3|400|μg/m3N|13,8%|

37 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en la Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

118

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
||1 de enero de 2019 - 31<br>de diciembre de 2021|Concentración media<br>trianual|6,0|100|μg/m3N|6,0%|

Fuente: Elaboración propia.

De la tabla anterior es posible concluir de manera cuantitativa que la estación de monitoreo

Subestación Eléctrica ha registrado concentraciones por bajo la norma de concentración

horaria y anual para el contaminante dióxido de nitrógeno (NO 2 ).

4.8.9.3 Dióxido de Azufre (SO 2 )

a) Resultados Monitoreo

En la Tabla 4-62 se presentan los resultados del monitoreo de dióxido de azufre (SO 2 ) en la

Estación Subestación Eléctrica durante el periodo en estudio.

**Tabla 4-62. Resultados Monitoreo de SO2. Estación Subestación Eléctrica** **[38]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2019**|**2020**|**2021**|
|SO2 (μg/m3N)|Percentil 98,5 de concentración horaria|22,2|19,9|28,3|
|SO2 (μg/m3N)|Promedio trianual percentil 98,5 de<br>concentración horaria|23,5|23,5|23,5|
|SO2 (μg/m3N)|Percentil 99 de concentración diaria|14,3|14,4|18,9|
|SO2 (μg/m3N)|Promedio trianual percentil 99 de<br>concentración diaria|15,9|15,9|15,9|
|SO2 (μg/m3N)|Media anual|4,7|4,7|4,3|
|SO2 (μg/m3N)|Media trianual|4,6|4,6|4,6|

Fuente: Elaboración propia.

38 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado por el titular propietario de la estación según la referencia presentada

en Tabla 4-15.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

119

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

b) Comparación con Normativa

En la Tabla 4-63 se presenta la comparación de los resultados del monitoreo de dióxido de

azufre (SO 2 ) en la Estación Subestación Eléctrica con la normativa primaria de calidad del

aire durante el periodo en estudio.

**Tabla 4-63. Comparación de Monitoreo de SO** **2** **con Normativa. Estación Subestación Eléctrica.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|SO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Percentil 98,5 de<br>concentración<br>horaria|21,1|350|μg/m3N|6,0%|
|SO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Percentil 98 de la<br>concentración<br>media diaria|12,9|150|μg/m3N|8,6%|
|SO2|1 de enero de 2019 - 31<br>de diciembre de 2021|Concentración<br>media trianual|4,4|60|μg/m3N|7,4%|

Fuente: Elaboración propia.

De la tabla anterior se puede concluir de manera cuantitativa que la estación de monitoreo

Subestación Eléctrica ha registrado concentraciones de dióxido de azufre (SO 2 ) por bajo la

norma de percentil 98,5 de 1 hora, de percentil 99 de 24 horas y de periodo anual.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

120

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

**4.8.10** **Resumen Línea de Base de Calidad del Aire**

A continuación, en la Tabla 4-64 se presenta el resumen de la línea de base de calidad del aire correspondiente al periodo comprendido

entre enero de 2019 a diciembre de 2021, exceptuando la Estación Ferrocarril, la cual comprende un periodo entre enero de 2017 a

diciembre de 2019.

**Tabla 4-64. Resumen Línea de Base de Calidad del Aire.**

|Contaminante|Estadígrafo|Norma|Unidad|JJ Latorre|Col6|Jardín Infantil|Col8|Puerto Mejillones|Col10|Ferrocarril|Col12|Angamos 1|Col14|MOLYB|Col16|MOLYNOR|Col18|Subestación<br>Eléctrica|Col20|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Norma**|**Unidad**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|
|MP2,5|P98 24 hrs|50|μg/m3|||||||23,00|46,00%|||24,00|48,00%|||||
|MP2,5|Anual|20|μg/m3|||||||9,00|45,00%|||11,00|55,00%|||||
|MP10|P98 24 hrs|130|μg/m3N|35,00|26,92%|32,00|24,62%|34,00|26,15%|41,00|31,54%|39,60|30,46%|52,00|40,00%|75,00|57,69%|81,00|62,31%|
|MP10|Anual|50|μg/m3N|20,20|40,40%|20,40|40,80%|20,00|40,00%|15,70|31,40%|17,30|34,60%|21,30|42,60%|30,00|60,00%|21,00|42,00%|
|NO2|P99 1hr|400|μg/m3N|43,20|10,80%|53,00|13,25%|||39,40|9,85%|70,60|17,65%|52,90|13,23%|39,30|9,83%|55,30|13,83%|
|NO2|Anual|100|μg/m3N|4,60|4,60%|7,00|7,00%|||2,50|2,50%|9,10|9,10%|9,00|9,00%|6,50|6,50%|6,00|6,00%|
|SO2|P98,5 1hr|350|μg/m3N|||||||8,40|2,40%|21,60|6,17%|238,60|68,17%|64,60|18,46%|21,10|6,03%|
|SO2|P99 24 hrs|150|μg/m3N|||||||6,30|4,20%|17,10|11,40%|169,20|112,80<br>%|52,10|34,73%|12,90|8,60%|
|SO2|Anual|60|μg/m3N|||||||1,80|3,00%|5,90|9,83%|30,40|50,67%|8,80|14,67%|4,40|7,33%|
|CO|P99 1 hr|30|mg/m3N|||||||0,40|1,33%|||||||||
|CO|P99 8 hrs|10|mg/m3N|||||||0,30|3,00%|||||||||
|O3|P99|120|μg/m3N|||||||56,70|47,25%|||||||||

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

121

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.9** **Línea Base Proyectada**

Considerando que en la zona de emplazamiento del proyecto existen otros proyectos

sometidos a evaluación por parte del SEIA con RCA favorable que se encuentran sin ejecutar

dentro del área de influencia del proyecto durante el período de registro de calidad del aire

disponible, se realizó una revisión de los proyectos con dicha condición en los últimos años,

para verificar si estos pueden modificar la línea de base de este componente, en base a la

fase en la que se encuentran según la información disponible en el Sistema Nacional de

Información de Fiscalización Ambiental (SNIFA), lo cual se presenta a continuación:

**Tabla 4-65. Proyectos aprobados en el Sector de Mejillones y Alrededores.**

|Proyecto|RCA|Fase según SNIFA|
|---|---|---|
|Ampliación Plantas de Ácido Nítrico y Nitrato de Amonio|102/2016|En fase de operación|
|Planta Fotovoltaica AR Changos Solar|221/2021|No iniciada la fase de construcción|
|Centro de Almacenamiento de Peróxido de Hidrógeno<br>Mejillones|152/2021|No iniciada la fase de construcción|
|Central Termoeléctrica Ttanti|013/2018|No iniciada la fase de construcción|
|Planta desalinizadora y suministro de agua industrial|217/2017|Iniciada la fase de construcción|
|Ampliación Planta Mejillones|013/2017|No iniciada la fase de construcción|
|Modificación Sistema Eléctrico y trazado Tubería Proyecto<br>Algorta|454/2017|No iniciada la fase de construcción|
|Modificación del Transporte Terrestre de Sustancias Corrosivas<br>en Región de Atacama|661/2017|En fase de operación|
|Terminal de Graneles en Complejo Portuario Mejillones|369/2017|Sin información|
|Proyecto Terminar para Carga y Descarga de Combustibles<br>Mejillones|46/2018|No iniciada la fase de construcción|
|Línea de Alta Tensión 2x200 kV, Los Changos-Kimal|440/2017|En fase de operación|
|Ampliación Terminal Marítimo Mejillones|474/2017|En fase de operación|
|Autogeneración eléctrica Terminal GNL Mejillones|8/2018|En fase de operación|
|Conexión Unidades CTM-2 y CTM-3 a GIS en S/E Chacaya|27/2018|En fase de operación|
|Transporte de ácido sulfúrico hacia Minera Antucoya desde<br>puntos de despacho de la Región de Antofagasta|174/2018|Sin información|
|Transporte de ácido sulfúrico hacia Minera Spence desde<br>puntos de despacho de la Región de Antofagasta|170/2018|Sin información|
|Marimaca|129/2018|Sin información|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

122

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

|Proyecto|RCA|Fase según SNIFA|
|---|---|---|
|Disposición temporal de residuos de generación de la unidad<br>CTM 4 en Depósito CTM existente|118/2018|Iniciada la fase de cierre o abandono|
|Modificación proyecto Ampliación del tipo de Carga a<br>Embarcar y Desembarcar a través de las Instalaciones del<br>Terminal 1 Complejo Portuario Mejillones|100/2019|Iniciada la fase de construcción|
|Modificación Terminal para depósito y manejo de Graneles<br>Líquidos en la Bahía de Mejillones|113/2019|Iniciada la fase de construcción|
|Obra Complementaria a la RCA N°0217/2017: Subestación<br>Eléctrica Caitan|72/2019|Iniciada la fase de construcción|
|Transporte Terrestre Interregional de Sustancias Peligrosas|1061/2019|Sin información|
|Desarrollo Terminal Marítimo Puerto Andino|172/2019|No iniciada la fase de construcción|
|Plan de Cierre Vertedero de Mejillones|074/2020|Sin información|
|Planta Fotovoltaica Ckontor|89/2021|Sin información|
|Parque Lince Solar|124/2020|No iniciada la fase de construcción|
|Parque Fotovoltaico Angamos|237/2020|Sin información|
|Operación Unidades CTA/CTH con 100% de Biomasa|20220200198|No iniciada la construcción|

Fuente: elaboración propia.

De la tabla anterior se observa que existen veintisiete (28) proyectos aprobados en los

últimos años, de los cuales nueve proyectos se encuentran en el estado “No iniciada la fase

de construcción”.

De la información anteriormente descrita, los proyectos que consideran aportes en las

estaciones localizadas en el sector de Mejillones son [39] :

 - Central Termoeléctrica Ttanti.

 - Ampliación Planta Mejillones.

 - Modificación proyecto Ampliación del tipo de Carga a Embarcar y Desembarcar a

través de las Instalaciones del Terminal 1 Complejo Portuario Mejillones.

 - Desarrollo Terminal Marítimo Puerto Andino.

39 No se ha considerado los aportes indicados en el proyecto Operación Unidades CTA/CTH por ser
negativos, es decir, implican una disminución respecto al caso actual.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

123

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

En base a lo anteriormente expuesto, se presenta a continuación una tabla resumen con el

aporte de los proyectos aprobados y no ejecutados en la cual se ha considerado el escenario

con mayor aporte presentado en el respectivo proceso de evaluación.

**Tabla 4-66. Aportes Declarados por Proyectos Aprobados, No Ejecutados.**

|Contaminante|Estadígrafo|Norma|Unidad|JJ Latorre|Col6|Jardín Infantil|Col8|Ferrocarril|Col10|MOLYNOR|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Norma**|**Unidad**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|
|MP2,5|P98 24 hrs|50|μg/m3|0,19|0,38%|0,20|0,40%|0,12|0,24%|6,35|12,70%|
|MP2,5|Anual|20|μg/m3|0,03|0,15%|0,03|0,15%|0,02|0,10%|1,36|6,80%|
|MP10|P98 24 hrs|150|μg/m3N|1,41|0,94%|1,37|0,91%|0,27|0,18%|6,35|4,23%|
|MP10|Anual|50|μg/m3N|0,08|0,16%|0,07|0,14%|0,05|0,10%|1,36|2,72%|
|NO2|P99 1hr|400|μg/m3N|232,82|58,21%|179,09|44,77%|18,89|4,72%|||
|NO2|Anual|100|μg/m3N|3,34|3,34%|2,93|2,93%|0,10|0,10%|||
|SO2|P98,5 1hr|350|μg/m3N|0,00|0,00%|0,00|0,00%|0,00|0,00%|||
|SO2|P99 24 hrs|150|μg/m3N|0,18|0,12%|0,16|0,11%|0,72|0,48%|||
|SO2|Anual|60|μg/m3N|0,02|0,03%|0,02|0,03%|0,13|0,22%|||
|CO|P99 1 hr|30|mg/m3N|3,73|12,43%|3,60|12,00%|2,05|6,83%|||
|CO|P99 8 hrs|10|mg/m3N|1,61|16,10%|1,52|15,20%|1,39|13,90%|||

Fuente: elaboración propia.

Considerando los aportes declarados por proyectos aprobados y no ejecutados, y la línea

base medida, se ha elaborado la línea base proyectada, la cual se presenta en la siguiente

tabla.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

124

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-67. Línea de Base Proyectada.**

|Contaminante|Estadígrafo|Norma|Unidad|JJ Latorre|Col6|Jardín Infantil|Col8|Puerto Mejillones|Col10|Ferrocarril|Col12|Angamos 1|Col14|MOLYB|Col16|MOLYNOR|Col18|Subestación Eléctrica|Col20|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Norma**|**Unidad**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|
|MP2,5|P98 24 hrs|50|μg/m3|||||||23,12|46,24%|||24,00|48,00%|||||
|MP2,5|Anual|20|μg/m3|||||||9,02|45,10%|||11,00|55,00%|||||
|MP10|P98 24 hrs|150|μg/m3N|36,41|28,01%|33,37|25,67%|34,00|26,15%|41,27|31,75%|39,60|30,46%|52,00|40,00%|81,35|62,58%|81,00|62,31%|
|MP10|Anual|50|μg/m3N|20,28|40,56%|20,47|40,94%|20,00|40,00%|15,75|31,50%|17,30|34,60%|21,30|42,60%|31,36|62,72%|21,00|42,00%|
|NO2|P99 1hr|400|μg/m3N|276,02|69,01%|232,09|58,02%|||58,29|14,57%|70,60|17,65%|52,90|13,23%|38,70|9,68%|55,30|13,83%|
|NO2|Anual|100|μg/m3N|7,94|7,94%|9,93|9,93%|||2,60|2,60%|9,10|9,10%|9,00|9,00%|5,60|5,60%|6,00|6,00%|
|SO2|P98,5 1hr|350|μg/m3N|||||||8,40|2,40%|21,60|6,17%|238,60|68,17%|55,80|15,94%|21,10|6,03%|
|SO2|P99 24 hrs|150|μg/m3N|||||||7,02|4,68%|17,10|11,40%|169,20|112,80%|35,70|23,80%|12,90|8,60%|
|SO2|Anual|60|μg/m3N|||||||1,93|3,22%|5,90|9,83%|30,40|50,67%|6,80|11,33%|4,40|7,33%|
|CO|P99 1 hr|30|mg/m3N|||||||2,45|8,17%|||||||||
|CO|P99 8 hrs|10|mg/m3N|||||||1,69|16,90%|||||||||
|O3|P99|120|μg/m3N|||||||56,70|47,25%|||||||||

Fuente: elaboración propia.

De la tabla precedente se observa que la condición basal de la calidad del aire en el sector no presenta sobrepaso de valores normados,

encontrándose todos los valores proyectados fuera de condición de latencia [40] .

40 Condición de latencia: Equivale a concentraciones entre el 80% y el 100% del valor normado.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

125

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.10** **Receptores de Interés**

Considerando el dominio de modelación compuesto por una grilla de receptores de

resolución 1.000 x 1.000 m, se han analizado 12 receptores discretos, de los cuales 8

corresponden a las estaciones de monitoreo de calidad del aire presentadas en la línea de

base de la sección anterior, y cuatro (4) corresponden a puntos referenciales de receptores

de MPS, los primeros 2 puntos ubicados en las zonas P1 y P2 [41], respectivamente, mientras

que los segundos dos puntos se ubican en los puntos de anidación identificados. Sobre ellas

se han comparado los resultados de la modelación con las normativas primarias de calidad

del aire presentadas en la sección 4.7.

De esta manera, en la Tabla 4-68 se muestran las coordenadas geográficas y la elevación

sobre el nivel del mar de los receptores considerados para el modelo, de tal forma de

evaluar correctamente la normativa primaria de calidad de aire.

**Tabla 4-68. Receptores Discretos en la Modelación.**

|ID Receptor|Descripción|Coordenadas de Ubicación (Datum WGS84)|Col4|Elevación<br>(m.s.n.m)42|
|---|---|---|---|---|
|**ID Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|R1|JJ Latorre|352.346|7.444.100|22,99|
|R2|Jardín Infantil|352.064|7.444.407|15,73|
|R3|Puerto Mejillones|352.047|7.444.688|9,21|
|R4|Ferrocarril|350.017|7.444.552|15,30|
|R5|Angamos 1|357.839|7.446.453|36,89|
|R6|MOLYB|358.938|7.447.360|38,55|
|R7|MOLYNOR|358.945|7.448.107|19,94|
|R8|Subestación Eléctrica|354.703|7.445.227|20,58|
|R9|Zona P1 (MPS y SO2 secundario)|362.220|7.449.342|66,92|
|R10|Zona P2 (MPS y SO2 secundario)|363.600|7.454.270|26,24|
|R11|Nido 1 (MPS y SO2 secundario)|357.871|7.446.345|49,22|
|R12|Nido 2 (MPS y SO2 secundario)|358.161|7.445.819|55,48|

Fuente: Elaboración propia.

41 Zona P1 y P2 del Plan Regulador de Mejillones.
42 Obtenida a partir de Shuttle Radar Topography Mission, SRTM1 (ver sección 4.3.2)

www.dfmconsultores.cl

**info@dfmconsultores.cl**

126

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

Asimismo, en la Figura 4-39 se muestra una imagen referencial de la ubicación de los

receptores discretos, detallados en la tabla anterior, utilizados en la modelación de calidad

del aire.

**Figura 4-39. Ubicación de Receptores Discretos en la Modelación.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

127

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.11** **Escenario de Modelación**

En la siguiente sección, se presenta la descripción del escenario de modelación,

correspondiente a la Fase de Cierre del Proyecto, en conjunto con las fuentes de emisión,

mencionando las características de estas y las emisiones de cada contaminante

correspondientes a cada una, las cuales fueron ingresadas al modelo.

Para la modelación de este escenario se han considerado las actividades correspondientes

a la fase de cierre, la cual contempla un tiempo de ejecución de 4 meses.

De esta manera, a continuación, en la Tabla 4-69 se detallan las fuentes emisoras ingresadas

al modelo de dispersión de contaminantes, las cuales corresponden a caminos (emisiones

generadas por tránsito vehicular) y fuentes de área asociadas a los movimientos de tierra y

uso de maquinaria, mientras que en la siguiente figura se muestra la localización de dichas

fuentes

www.dfmconsultores.cl

**info@dfmconsultores.cl**

128

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-69. Fuentes Emisoras - Fase de Cierre.**

|Tipo|ID|Descripción|Tasa de Emisión|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo**|**ID**|**Descripción**|**SO2 **|**SO4 **|**NO**|**NO2 **|**HNO3 **|**NO3 **|**MP2.5**|**MP10**|**MPS**|**CO**|**Unidad**|
|Camino|SRC_2|Tramo 2|5,22,E-07|0,00,E+00|6,96,E-06|1,19,E-06|0,00,E+00|0,00,E+00|9,59,E-07|3,17,E-06|1,55,E-05|3,06,E-06|g/s/m|
|Camino|SRC_3|Tramo 3|2,04,E-07|0,00,E+00|2,73,E-06|4,65,E-07|0,00,E+00|0,00,E+00|6,97,E-07|2,57,E-06|1,30,E-05|1,20,E-06|g/s/m|
|Camino|SRC_4|Tramo 4|1,06,E-08|0,00,E+00|1,42,E-07|2,41,E-08|0,00,E+00|0,00,E+00|3,49,E-08|1,28,E-07|6,45,E-07|6,38,E-08|g/s/m|
|Camino|SRC_5|Tramo 5|1,08,E-07|0,00,E+00|1,45,E-06|2,47,E-07|0,00,E+00|0,00,E+00|3,32,E-07|1,20,E-06|6,04,E-06|6,82,E-07|g/s/m|
|Camino|SRC_6|Tramo 6|3,13,E-09|0,00,E+00|4,18,E-08|7,12,E-09|0,00,E+00|0,00,E+00|4,60,E-08|1,63,E-07|8,14,E-07|1,61,E-08|g/s/m|
|Camino|SRC_7|Tramo 7|4,73,E-09|0,00,E+00|6,31,E-08|1,08,E-08|0,00,E+00|0,00,E+00|1,24,E-08|4,77,E-08|2,44,E-07|2,43,E-08|g/s/m|
|Camino|SRC_8|Tramo 8|3,10,E-09|0,00,E+00|4,14,E-08|7,05,E-09|0,00,E+00|0,00,E+00|2,15,E-08|8,27,E-08|4,23,E-07|1,59,E-08|g/s/m|
|Área|SRC_1|Área instalación|1,92,E-07|0,00,E+00|1,20,E-06|2,04,E-07|0,00,E+00|0,00,E+00|2,73,E-07|3,69,E-07|1,26,E-06|4,45,E-07|g/s/m2|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

129

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-40. Ubicación de Tramos Fuentes Emisoras Modeladas. Fase de Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

130

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.12** **Resultados de la Modelación**

En este inciso se presentan los resultados de la modelación para la Fase de Cierre del

proyecto, descrita en el inciso anterior.

En primer lugar, se presentan tablas en donde se cuantifica el aporte de cada contaminante

evaluado del proyecto para cada receptor de interés. Luego, se realiza una comparación con

la normativa de calidad de aire respectiva, para así establecer el porcentaje del aporte del

proyecto, en su fase de cierre, respecto a la norma de cada contaminante.

Además del análisis cuantitativo, se presentan las curvas de isoconcentración o

isodepositación para el escenario de modelación, para todos los contaminantes, lo cual es

útil para cuantificar el impacto de las actividades del proyecto en todo el dominio de

modelación y estimar el aporte que tendrá el proyecto en otras zonas que no

necesariamente son las de los receptores discretos estudiados.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

131

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.12.1** **Material Particulado Fino (MP2,5)**

En la Tabla 4-70 se presentan las concentraciones de Material Particulado Fino (MP2,5)

aportadas por el proyecto en los receptores de interés para el escenario de modelación de

la Fase de Cierre del Proyecto, la cual considera el material particulado secundario.

**Tabla 4-70. Resultados de modelo de dispersión de MP2.5. Fase de Cierre.**

|Receptor|Descripción|Material Particulado Respirable Fino (MP2,5)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**|**Norma de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|
|R1|JJ Latorre|1,70,E-03|1,94,E-04|50|20|0,00%|0,00%|
|R2|Jardín Infantil|1,50,E-03|1,27,E-04|1,27,E-04|1,27,E-04|0,00%|0,00%|
|R3|Puerto Mejillones|1,43,E-03|1,28,E-04|1,28,E-04|1,28,E-04|0,00%|0,00%|
|R4|Ferrocarril|8,19,E-04|6,10,E-05|6,10,E-05|6,10,E-05|0,00%|0,00%|
|R5|Angamos 1|1,47,E-01|1,37,E-02|1,37,E-02|1,37,E-02|0,29%|0,07%|
|R6|MOLYB|1,19,E-01|1,79,E-02|1,79,E-02|1,79,E-02|0,24%|0,09%|
|R7|MOLYNOR|6,65,E-02|9,74,E-03|9,74,E-03|9,74,E-03|0,13%|0,05%|
|R8|Subestación Eléctrica|3,42,E-03|4,56,E-04|4,56,E-04|4,56,E-04|0,01%|0,00%|

Fuente: Elaboración propia.

Por otro lado, en la Figura 4-41 y la Figura 4-42 se presentan las curvas de isoconcentración

de Material Particulado Fino (MP2,5) para la norma de percentil 98 de 24 horas y la norma

periodo anual respectivamente.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

132

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-41. Curvas de Isoconcentración para Percentil 98 período 24 horas MP2,5 (μg/m** **[3]** **N). Fase de**

**Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

133

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-42. Curvas de Isoconcentración para período anual MP2,5 (μg/m** **[3]** **N). Fase de Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

134

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

De las tablas precedentes, es posible apreciar que en durante la Fase de Cierre no se

superan las normativas primarias de calidad del aire para MP2,5 en ninguno de los

receptores discretos evaluados. Además, los aportes en los receptores son de baja

magnitud, alcanzando como máximo un 0,29% en la norma diaria de MP2,5.

Respecto a la concentración media anual de MP2,5, el máximo aporte se presenta en

Estación MOLYB, alcanzando un valor inferior al 0,09% de la Norma Anual.

Por otro lado, a partir de las curvas de isoconcentración se aprecia que los mayores aportes

se concentran en el entorno del Terminal, cercano a las fuentes de emisión.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

135

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.12.2** **Material Particulado Respirable (MP10)**

En la Tabla 4-71 se presentan las concentraciones de Material Particulado Respirable

(MP10) aportadas por el proyecto en los receptores de interés para el escenario de

modelación de la Fase de Cierre, la cual considera el material particulado secundario.

**Tabla 4-71. Resultados de modelo de dispersión de MP10. Fase de Cierre.**

|Receptor|Descripción|Material Particulado Respirable (MP10)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**|**Norma de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|
|R1|JJ Latorre|2,94,E-03|4,26,E-04|130|50|0,00%|0,00%|
|R2|Jardín Infantil|1,98,E-03|2,09,E-04|2,09,E-04|2,09,E-04|0,00%|0,00%|
|R3|Puerto Mejillones|2,55,E-03|2,10,E-04|2,10,E-04|2,10,E-04|0,00%|0,00%|
|R4|Ferrocarril|1,12,E-03|8,82,E-05|8,82,E-05|8,82,E-05|0,00%|0,00%|
|R5|Angamos 1|1,97,E-01|1,83,E-02|1,83,E-02|1,83,E-02|0,15%|0,04%|
|R6|MOLYB|1,60,E-01|2,45,E-02|2,45,E-02|2,45,E-02|0,12%|0,05%|
|R7|MOLYNOR|8,74,E-02|1,33,E-02|1,33,E-02|1,33,E-02|0,07%|0,03%|
|R8|Subestación Eléctrica|4,65,E-03|6,48,E-04|6,48,E-04|6,48,E-04|0,00%|0,00%|

Fuente: Elaboración propia.

Por otro lado, en la Figura 4-43 y la Figura 4-44 se presentan las curvas de isoconcentración

de Material Particulado Respirable (MP10) para la norma de percentil 98 de 24 horas y la

norma periodo anual respectivamente para la Fase de Cierre.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

136

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-43. Curva de Isoconcentración para Percentil 98 periodo 24 horas MP10 (μg/m** **[3]** **N). Fase de Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

137

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-44. Curva de Isoconcentración para período anual MP10 (μg/m** **[3]** **N). Fase de Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

138

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

De las tablas precedentes, es posible apreciar que durante la Fase de Cierre no se superarán

las normativas primarias de calidad del aire para MP10 en ninguno de los receptores

discretos evaluados. Además, los aportes en los receptores son de baja magnitud,

alcanzando como máximo un valor inferior al 0,15% en la norma diaria de MP10 en la

Estación Angamos 1.

Respecto a la concentración media anual de MP10, el máximo aporte se presenta en

Estación MOLYB alcanzado un valor inferior a 0,05% de la Norma Anual.

Por otro lado, a partir de las curvas de isoconcentración se aprecia que los mayores aportes

se concentran en el entorno del Terminal, cercano a las fuentes de emisión.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

139

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.12.3** **Dióxido de Nitrógeno (NO** **2** **)**

En la Tabla 4-72 se presentan las concentraciones de Dióxido de Nitrógeno (NO 2 ) aportadas

por el proyecto en los receptores de interés para el escenario de modelación asociado a la

Fase de Cierre.

**Tabla 4-72. Resultados de modelo de dispersión de NO** **2** **. Fase de Cierre.**

|Receptor|Descripción|Dióxido de Nitrógeno (NO )<br>2|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Norma de Calidad**|**Norma de Calidad**|**Porcentaje de la**<br>**Norma de Calidad**|**Porcentaje de la**<br>**Norma de Calidad**|
|**Receptor**|**Descripción**|**Percentil 99**<br>**1 hora**|**Período**<br>**Anual**|**Percentil**<br>**99 1 hora**|**Período**<br>**Anual**|**Percentil**<br>**99 1 hora**|**Período**<br>**Anual**|
|R1|JJ Latorre|0,224|0,001|400|100|0,06%|0,00%|
|R2|Jardín Infantil|0,183|0,001|0,001|0,001|0,05%|0,00%|
|R3|Puerto Mejillones|0,185|0,001|0,001|0,001|0,05%|0,00%|
|R4|Ferrocarril|0,071|0,000|0,000|0,000|0,02%|0,00%|
|R5|Angamos 1|11,069|0,071|0,071|0,071|2,77%|0,07%|
|R6|MOLYB|5,077|0,104|0,104|0,104|1,27%|0,10%|
|R7|MOLYNOR|3,344|0,055|0,055|0,055|0,84%|0,06%|
|R8|Subestación Eléctrica|0,391|0,002|0,002|0,002|0,10%|0,00%|

Fuente: Elaboración propia.

Por otro lado, en las siguientes figuras se presentan las curvas de isoconcentración de

Dióxido de Nitrógeno (NO 2 ) para la norma de percentil 99 de 1 hora y la norma periodo

anual respectivamente para el escenario de modelación.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

140

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-45. Curvas de Isoconcentración para Percentil 99 período 1 hora NO** **2** **(μg/m** **[3]** **N). Fase de Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

141

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-46. Curvas de Isoconcentración para período anual NO** **2** **(μg/m** **[3]** **N). Fase de Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

142

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

De las tablas precedentes, es posible apreciar que en el escenario de modelación no se

superan las normativas primarias de calidad del aire para NO 2 en ninguno de los receptores

discretos evaluados. Además, los aportes en los receptores son de baja magnitud,

alcanzando como máximo un 2,77% en la norma horaria de NO 2, y un 0,10% de la norma

anual de NO 2 .

Por otro lado, a partir de las curvas de isoconcentración se aprecia que los mayores aportes

se concentran en el entorno del Terminal, cercano a las fuentes de emisión.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

143

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

**4.12.4** **Dióxido de Azufre (SO** **2** **)**

4.12.4.1 Norma Primaria

En la Tabla 4-73 se presentan las concentraciones de Dióxido de Azufre (SO 2 ) aportadas por el proyecto en los receptores de interés

para el escenario de modelación.

**Tabla 4-73. Resultados de modelo de dispersión de SO** **2** **. Fase de Cierre.**

|Receptor|Descripción|Dióxido de Azufre (SO )<br>2|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Norma de Calidad**|**Norma de Calidad**|**Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Percentil 98,5**<br>**1 hora**|**Percentil 99**<br>**24 horas**|**Período Anual**|**Percentil**<br>**98,5 1 hora**|**Percentil**<br>**99 24**<br>**horas**|**Período**<br>**Anual**|**Percentil**<br>**98,5 1 hora**|**Percentil**<br>**99 24**<br>**horas**|**Período**<br>**Anual**|
|R1|JJ Latorre|5,75,E-04|1,17,E-03|7,05,E-05|350|150|60|0,00%|0,00%|0,00%|
|R2|Jardín Infantil|4,13,E-04|1,02,E-03|4,62,E-05|4,62,E-05|4,62,E-05|4,62,E-05|0,00%|0,00%|0,00%|
|R3|Puerto Mejillones|4,06,E-04|1,03,E-03|4,52,E-05|4,52,E-05|4,52,E-05|4,52,E-05|0,00%|0,00%|0,00%|
|R4|Ferrocarril|1,77,E-04|4,25,E-04|1,90,E-05|1,90,E-05|1,90,E-05|1,90,E-05|0,00%|0,00%|0,00%|
|R5|Angamos 1|9,50,E-02|1,04,E-01|8,19,E-03|8,19,E-03|8,19,E-03|8,19,E-03|0,03%|0,07%|0,01%|
|R6|MOLYB|2,30,E-01|8,03,E-02|1,02,E-02|1,02,E-02|1,02,E-02|1,02,E-02|0,07%|0,05%|0,02%|
|R7|MOLYNOR|1,21,E-01|4,19,E-02|5,27,E-03|5,27,E-03|5,27,E-03|5,27,E-03|0,03%|0,03%|0,01%|
|R8|Subestación Eléctrica|1,26,E-03|3,04,E-03|1,81,E-04|1,81,E-04|1,81,E-04|1,81,E-04|0,00%|0,00%|0,00%|

Fuente: Elaboración propia.

De la Figura 4-47 a la Figura 4-49 se presentan las curvas de isoconcentración de Dióxido de Azufre (SO 2 ) para la norma de percentil

98,5 de una hora, la norma de percentil 99 de 24 horas y la norma de periodo anual respectivamente para la Fase de Cierre.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

144

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-47. Curvas de Isoconcentración para Percentil 98,5 periodo 1 hora SO** **2** **(μg/m** **[3]** **N). Fase de Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

145

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-48. Curvas de Isoconcentración para Percentil 99 periodo 24 horas SO** **2** **(μg/m** **[3]** **N). Fase de Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

146

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-49. Curvas de Isoconcentración para período anual SO2 (μg/m** **[3]** **N). Fase de Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

147

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

De las tablas precedentes, es posible apreciar que durante la Fase de Cierre no se superan

las normativas primarias de calidad del aire para SO 2 en ninguno de los receptores discretos

evaluados. Además, se aprecia que los aportes para los tres estadígrafos son menores al

0,1% del valor de la norma.

Por otro lado, a partir de las curvas de isoconcentración se aprecia que los mayores aportes

se concentran en el entorno del Terminal, cercano a las fuentes de emisión.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

148

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

4.12.4.2 Norma Secundaria

En la Tabla 4-74 se presentan las concentraciones de Dióxido de Azufre (SO 2 ) aportadas por el proyecto en los receptores de interés

para el escenario de modelación, para la norma secundaria.

**Tabla 4-74. Resultados de modelo de dispersión de SO** **2** **. Fase de Cierre.**

|Receptor|Descripción|Dióxido de Azufre (SO )<br>2|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Norma de Calidad**|**Norma de Calidad**|**Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Percentil**<br>**99,73 hora**|**Percentil 99,7**<br>**24 horas**|**Período Anual**|**Percentil**<br>**98,73 1**<br>**hora**|**Percentil**<br>**99,7 24**<br>**horas**|**Período**<br>**Anual**|**Percentil**<br>**99,73 hora**|**Percentil**<br>**99,7 24**<br>**horas**|**Período**<br>**Anual**|
|R9|MPS 1|1,39,E-02|2,87,E-03|3,93,E-04|1000|365|80|0,00%|0,00%|0,00%|
|R10|MPS 2|1,18,E-02|2,19,E-03|2,86,E-04|2,86,E-04|2,86,E-04|2,86,E-04|0,00%|0,00%|0,00%|
|R11|Nido 1|5,53,E+00|1,11,E+00|1,52,E-01|1,52,E-01|1,52,E-01|1,52,E-01|0,55%|0,30%|0,19%|
|R12|Nido 2|1,80,E+00|5,24,E-01|8,97,E-02|8,97,E-02|8,97,E-02|8,97,E-02|0,18%|0,14%|0,11%|

Fuente: Elaboración propia.

En las siguientes figuras se presentan las curvas de isoconcentración de Dióxido de Azufre (SO 2 ) para la norma de una hora, la norma

de 24 horas y la norma de periodo anual respectivamente para la Fase de Cierre.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

149

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-50. Curvas de Isoconcentración para Percentil 99,73 periodo 1 hora SO** **2** **(μg/m** **[3]** **N Fase de Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

150

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-51. Curvas de Isoconcentración para Percentil 99,7 periodo 24 horas SO** **2** **(μg/m** **[3]** **N). Fase de**

**Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

151

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-52. Curvas de Isoconcentración para período anual SO2 (μg/m** **[3]** **N). Fase de Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

152

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

De las tablas precedentes, es posible apreciar que durante la Fase de Cierre no se superan

las normativas secundarias de calidad del aire para SO 2 en ninguno de los receptores

discretos evaluados. Además, se aprecia que los aportes para los tres estadígrafos son

nulos.

Por otro lado, a partir de las curvas de isoconcentración se aprecia que los mayores aportes

se concentran en el entorno del Terminal, cercano a las fuentes de emisión.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

153

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

4.12.5 **Monóxido de Carbono (CO)**

En la Tabla 4-75 se presentan las concentraciones de Monóxido de Carbono (CO) aportadas

por el proyecto en los receptores de interés para el escenario de modelación de la fase de

cierre.

**Tabla 4-75. Resultados de modelo de dispersión de CO. Fase de Cierre.**

|Receptor|Descripción|Monóxido de Carbono (CO)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [mg/m3] **|**Concentración [mg/m3] **|**Norma de Calidad**|**Norma de Calidad**|**Porcentaje de la**<br>**Norma de Calidad**|**Porcentaje de la**<br>**Norma de Calidad**|
|**Receptor**|**Descripción**|**Percentil 99 1**<br>**hora**|**Percentil 99 8**<br>**horas**|**Percentil**<br>**99 1 hora**|**Percentil**<br>**99 8**<br>**horas**|**Percentil**<br>**99 1 hora**|**Percentil**<br>**99 8**<br>**horas**|
|R1|JJ Latorre|5,95E-05|9,41E-06|30|10|0,00%|0,00%|
|R2|Jardín Infantil|5,63E-05|8,39E-06|8,39E-06|8,39E-06|0,00%|0,00%|
|R3|Puerto Mejillones|5,12E-05|7,88E-06|7,88E-06|7,88E-06|0,00%|0,00%|
|R4|Ferrocarril|1,93E-05|2,88E-06|2,88E-06|2,88E-06|0,00%|0,00%|
|R5|Angamos 1|4,43E-03|5,93E-04|5,93E-04|5,93E-04|0,01%|0,01%|
|R6|MOLYB|1,32E-03|2,97E-04|2,97E-04|2,97E-04|0,00%|0,00%|
|R7|MOLYNOR|8,97E-04|1,54E-04|1,54E-04|1,54E-04|0,00%|0,00%|
|R8|Subestación Eléctrica|9,76E-05|1,59E-05|1,59E-05|1,59E-05|0,00%|0,00%|

Fuente: Elaboración propia.

Por otro lado, en las siguientes figuras se presentan las curvas de isoconcentración de

Monóxido de Carbono (CO) para la norma de percentil 99 de 1 hora y de 8 horas

respectivamente para el escenario de modelación.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

154

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-53. Curva de Isoconcentración para Percentil 99 período horario CO (mg/m** **[3]** **N). Fase de Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

155

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-54. Curva de Isoconcentración para Percentil 99 período 8 horas CO (μg/m** **[3]** **N). Fase de Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

156

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

4.12.6 **Material Particulado Sedimentable (MPS)**

En la Tabla 4-76 se presentan las depositaciones de Material Particulado Sedimentable

(MPS) aportadas por el proyecto en los receptores de interés para el escenario de

modelación de la Fase de Cierre.

**Tabla 4-76. Resultados de modelo de dispersión de MPS. Fase de Cierre.**

|Receptor|Descripción|Material Particulado Sedimentable (MPS)|Col4|Col5|
|---|---|---|---|---|
|**Receptor**|**Descripción**|**Tasa de**<br>**depositación**<br>**[mg/m2-día]**|**Norma Periodo**<br>**Anual**|**Porcentaje de la**<br>**Norma de**<br>**Referencia**|
|R9|MPS 1|8,79E-04|200|0,00%|
|R10|MPS 2|3,73E-04|3,73E-04|0,00%|
|R11|Nido 1|7,46E-01|7,46E-01|0,37%|
|R12|Nido 2|4,38E-01|4,38E-01|0,22%|

Fuente: Elaboración propia.

Por otro lado, en la siguiente figura se presenta la curva de isodepositación de Material

Particulado Sedimentable para la norma anual correspondiente a la fase de cierre.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

157

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**Figura 4-55. Curva de Isodepositación para período anual MPS (mg/m** **[2]** **/día). Fase de Cierre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

158

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

**4.13** **Concentración Total Esperada**

En este inciso se presenta el análisis de la concentración total esperada, la cual resulta de

sumar a la línea de base de calidad del aire proyectada el aporte del escenario modelado,

de acuerdo a la siguiente ecuación:

Concentración Total Esperada Fase de Cierre

= Línea de Base Proyectada + Aporte del Proyecto Fase de Cierre

A continuación, en la Tabla 4-77 se presenta el resultado la concentración total esperada

anteriormente explicada para la Fase de Cierre para MP2,5, MP10, NO 2, SO 2 y CO

respectivamente:

www.dfmconsultores.cl

**info@dfmconsultores.cl**

159

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de Contaminantes Atmosféricos

Marzo 2023

**Tabla 4-77 - Concentración Total Esperada. Fase de Cierre.**

|Contaminante|Estadígrafo|Norma|Unidad|JJ Latorre|Col6|Jardín Infantil|Col8|Puerto Mejillones|Col10|Ferrocarril|Col12|Angamos 1|Col14|MOLYB|Col16|MOLYNOR|Col18|Subestación Eléctrica|Col20|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Norma**|**Unidad**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|**Valor**|**Norma**|
|MP2,5|P98 24 hrs|50|μg/m3|||||||23,1|46,2%|||24,0|48,0%|||||
|MP2,5|Anual|20|μg/m3|||||||9,0|45,1%|||11,0|55,0%|||||
|MP10|P98 24 hrs|130|μg/m3N|36,4|28,0%|33,4|25,7%|34,0|26,2%|41,3|31,7%|39,8|30,6%|52,2|40,1%|81,4|62,6%|81,0|62,3%|
|MP10|Anual|50|μg/m3N|20,3|40,6%|20,5|40,9%|20,0|40,0%|15,8|31,5%|17,3|34,6%|21,3|42,6%|31,4|62,7%|21,0|42,0%|
|NO2|P99 1hr|400|μg/m3N|276,2|69,1%|232,3|58,1%|||58,4|14,6%|81,7|20,4%|58,0|14,5%|42,0|10,5%|55,7|13,9%|
|NO2|Anual|100|μg/m3N|7,9|7,9%|9,9|9,9%|||2,6|2,6%|9,2|9,2%|9,1|9,1%|5,7|5,7%|6,0|6,0%|
|SO2|P98,5 1hr|350|μg/m3N|||||||8,4|2,4%|21,7|6,2%|238,8|68,2%|55,9|16,0%|21,1|6,0%|
|SO2|P99 24 hrs|150|μg/m3N|||||||7,0|4,7%|17,2|11,5%|169,3|112,9%|35,7|23,8%|12,9|8,6%|
|SO2|Anual|60|μg/m3N|||||||1,9|3,2%|5,9|9,8%|30,4|50,7%|6,8|11,3%|4,4|7,3%|
|CO|P99 1 hr|30|mg/m3N|||||||2,5|8,2%|||||||||
|CO|P99 8 hrs|10|mg/m3N|||||||1,69|16,9%|||||||||

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

160

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

#### 5 CONCLUSIONES

**5.1** **Inventario de Emisiones de Contaminantes Atmosféricos**

En el presente informe se han calculado las emisiones atmosféricas asociadas a la fase de

cierre del Proyecto “Terminal de Mantención Mejillones”, para los contaminantes MP 2.5,

MP 10, MPS, CO, NO x, NH 3, COV y SO 2 de manera independiente.

Conforme a lo presentado anteriormente, es posible concluir lo siguiente:

- Las mayores emisiones de material particulado son generadas por los movimientos de

material, seguidas por las emisiones generadas por maquinaria. Para gases, las mayores

emisiones se encuentran asociadas a la utilización de maquinaria, seguidas por las

generadas por la utilización de grupos electrógenos.

- Las emisiones estimadas están acotadas a los 4 meses de duración de la Fase de Cierre,

de acuerdo con el cronograma del Proyecto.

**5.2** **Caracterización Meteorológica del Área del Proyecto y Análisis de Incertidumbre del**

**Modelo WRF**

A partir del análisis meteorológico realizado se concluye que de los datos registrados

durante el período comprendido entre el 01 de enero y el 31 de diciembre de 2020 en la

estación Meteorológica JJ Latorre, en la zona de emplazamiento del Proyecto existe una

velocidad del viento promedio de 2,4 m/s, una mínima de 0,0 m/s y una máxima de 9,5 m/s,

con un porcentaje de calmas de 1,6%. La dirección de viento predominante durante el

periodo nocturno es aquella proveniente desde el sur (S), lo cual se mantiene desde las

18:00 hasta las 8:00 horas. Luego, durante el periodo diurno, la dirección del viento

proviene mayoritariamente desde el norte con algunas variaciones durante los meses de

invierno, en donde se aprecian algunos vientos provenientes desde el noroeste. Respecto a

la temperatura ambiente, se registra un promedio de 18,6°C, un mínimo de 6,5°C y un

máximo de 32,1°C. En cuanto a la humedad relativa en la estación en términos promedio es

de 61,4%, con mínimo de 23,6% y máximo de 84,8%. La radiación solar alcanza valores

promedio de 243,7 W/m [2], mínimos de 0 W/m [2 ] y máximos de 1.121,8 W/m [2] .

www.dfmconsultores.cl

**info@dfmconsultores.cl**

161

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

En relación a la meteorología modelada obtenida a partir del modelo meteorológico WRF,

se concluye que el modelo tiende a representar de manera aceptable los ciclos diarios y

estacionales para las variables meteorológicas velocidad del viento, dirección del viento y

temperatura. Sin perjuicio de lo anterior, respecto a la velocidad del viento el modelo tiende

a sobreestimar la magnitud de ésta para el periodo diurno, especialmente para los meses

de invierno, como también para el periodo de madrugada, en donde estos valores debiesen

ser menores durante la época comprendida entre abril y noviembre. En cuanto a la

dirección del viento, se aprecia que el modelo tiene un buen desempeño para representar

los diversos cambios direccionales presentes con el transcurso de las horas en las distintas

estaciones

Considerando el análisis cuantitativo, la magnitud de los valores de coeficientes de

correlación para los ciclos diarios calculados para las variables velocidad del viento y

temperatura, sumado a los bajos valores de sesgo y error cuadrático medio justifican el

correcto ajuste del modelo a los datos meteorológicos observados en la estación

Meteorológica JJ Latorre.

**5.3** **Línea de Base de Calidad del Aire**

De los resultados de la línea de base de calidad del aire presentados, se concluye que

respecto a las concentraciones registradas de MP2,5, MP10, NO 2, SO 2 y CO para todas las

estaciones analizadas no existe excedencia de normativa primaria de calidad del aire, a

excepción de la estación MOLYB que presenta saturación para la norma diaria de SO 2 (P99

24 horas), donde la concentración obtenida es de 169,2 μg/m [3] N, equivalente a un 112,8%

del valor normado.

**5.4** **Modelación de Dispersión de Contaminantes Atmosféricos**

Respecto a los aportes específicos del proyecto en los receptores de interés evaluados, se

concluye que los aportes de la fase de cierre del proyecto, no superan las normativas

primarias de calidad del aire para ninguno de los contaminantes evaluados.

Por su parte, a partir del análisis de normativa secundaria de calidad del aire evaluada en el

sector de protección del gaviotín chico (zonas P1 y P2), así como en los puntos de anidación

www.dfmconsultores.cl

**info@dfmconsultores.cl**

162

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

identificado, se concluye que la fase de cierre del proyecto no genera un impacto

significativo para ninguno de los cuatro receptores de interés evaluados (R9, R10, R11 y

R12), tanto para MPS como SO 2 .

Finalmente, al evaluar la concentración total esperada, para la fase de cierre se concluye

que no hay aumentos significativos en los contaminantes evaluados, respecto a la línea base

proyectada. Así mismo no existe una superación de normativa primaria de calidad del aire

para ninguno de los contaminantes evaluados para la concentración total esperada

proyectada.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

163

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

#### 6 ANEXO 1: ARCHIVOS DIGITALES MODELACIÓN

En la siguiente tabla se detallan los archivos de entrada y salida de la modelación de calidad

del aire presentada en este estudio. Los archivos se listan según lo indicado en la “Guía para

el uso de modelos de calidad del aire en el SEIA”, considerando los archivos de entrada y

salida de los módulos CALMET, CALPUFF y CALPOST.

**Tabla 6-1. Archivos de modelación entregados.**

|Archivos|Entregado|Observación|
|---|---|---|
|**Archivos CALPUFF:**|**Archivos CALPUFF:**|**Archivos CALPUFF:**|
|- CALPUFF.DAT|NO|Corresponde al archivo CONC.DAT|
|- CALPUFF.LST|SI|-|
|- CALPUFF.INP|SI|-|
|- CONC.DAT|SI|-|
|- DFLX.DAT|SI|-|
|- WFLX.DAT|NO|-|
|**Archivos Meteorológicos:**|**Archivos Meteorológicos:**|**Archivos Meteorológicos:**|
|- CALMET.DAT|SI|- Corresponde al archivo:<br>calmetv6_Mejillones.dat|
|- GEO.DAT|SI|-|
|- SURF.DAT|NO|No fueron utilizados debido a que se usó, directamente<br>en CALPUFF, la meteorología proveniente del modelo<br>meteorológico WRF.|
|- UP.DAT|NO|NO|
|- CALMET.LST|NO|NO|
|- CALMET.INP|NO|NO|
|- namelist.wpl|SI|Archivo de configuración de preproceso de WRF (WPS)|
|- namelist.input|SI|Archivo de configuración de WRF|
|**Archivos CALPOST:**|**Archivos CALPOST:**|**Archivos CALPOST:**|
|- CALPOST.DAT|SI|Los archivos se presentan en forma separada según<br>contaminantes y periodo.|
|- CALPOST.LST|SI|SI|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

164

**Fase de Cierre - Proyecto “Terminal de Mantención Mejillones”**

Inventario de Emisiones y Modelación de Dispersión de

Contaminantes Atmosféricos

Marzo 2023

|Archivos|Entregado|Observación|
|---|---|---|
|**Archivos CALPUFF:**|**Archivos CALPUFF:**|**Archivos CALPUFF:**|
|- CALPOST.INP|SI||
|**Archivos Complementarios:**|**Archivos Complementarios:**|**Archivos Complementarios:**|
|- Coastline Data File, Dry Flux Data File, Wet Flux<br>Data File, Ozone Data File, Chem Data File.|NO|No se incluyen, debido a que corresponden a datos que<br>no fueron modelados.|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

165

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3-1.: Cronograma Fase de Cierre.****

| Actividad | Mes 1 | Col3 | Mes 2 | Col5 | Mes 3 | Col7 | Mes 4 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Habilitación Instalación de faenas |  |  |  |  |  |  |  |  |
| Desenergización de las instalaciones |  |  |  |  |  |  |  |  |
| Detención y desconexión de equipos y<br>maquinarias |  |  |  |  |  |  |  |  |
| Desmantelamiento y desmontaje de algunas<br>instalaciones y equipos |  |  |  |  |  |  |  |  |
| Restaurar geoforma en caso de aplicar |  |  |  |  |  |  |  |  |

**Tabla 3-2: - Factores de Emisión Movimientos de Tierra - Fase de cierre.****

| Actividad | Ecuación Factor<br>de Emisión | Unidad | Referencia<br>Ecuación Factor de<br>Emisión | Parámetros Factores de Emisión | Col6 | Col7 | Col8 | Col9 | Factor de Emisión | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Ecuación Factor**<br>**de Emisión** | **Unidad** | **Referencia**<br>**Ecuación Factor de**<br>**Emisión** | **Variables** | **Referencias** | **Valor**<br>**MP2,5** | **Valor**<br>**MP10** | **Valor**<br>**MPS** | **MP2,5** | **MP10** | **MPS** |
| Excavaciones /<br>Relleno | Para MP2,5 | kg/h | Punto 4.6, Informe<br>Final Servicio de<br>Recopilación y<br>Sistematización de<br>Factores de<br>Emisión al Aire<br>para el SEIA. | k: factor de<br>tamaño de<br>partícula | Table 11.9-2, Capítulo 11,<br>Sección 11.9"Western Surface<br>Coal Mining", AP-42 | 0,105 | n/a | n/a | 0,189 | n/a | n/a |
| Excavaciones /<br>Relleno | 2,6 · k · (s1,2/M1,3) | 2,6 · k · (s1,2/M1,3) | 2,6 · k · (s1,2/M1,3) | s: contenido de<br>finos (%) | Valor por defecto, Punto 4.6,<br>Informe Final Servicio de<br>Recopilación y Sistematización<br>de Factores de Emisión al Aire<br>para el SEIA. | 6,9 | n/a | n/a | n/a | n/a | n/a |
| Excavaciones /<br>Relleno | 2,6 · k · (s1,2/M1,3) | 2,6 · k · (s1,2/M1,3) | 2,6 · k · (s1,2/M1,3) | M: humedad del<br>material (%) | Valor por defecto, Punto 4.6,<br>Informe Final Servicio de<br>Recopilación y Sistematización<br>de Factores de Emisión al Aire<br>para el SEIA. | 7,9 | n/a | n/a | n/a | n/a | n/a |
| Excavaciones /<br>Relleno | Para MP 10 | kg/h | Punto 4.6, Informe<br>Final Servicio de<br>Recopilación y<br>Sistematización de<br>Factores de<br>Emisión al Aire<br>para el SEIA. | k: factor de<br>tamaño de<br>partícula | Table 11.9-2, Capítulo 11,<br>Sección 11.9"Western Surface<br>Coal Mining", AP-42 | n/a | 0,75 | n/a | n/a | 0,339 | n/a |
| Excavaciones /<br>Relleno | 0,45 · k ·<br>(s1,5/M1,4) | 0,45 · k ·<br>(s1,5/M1,4) | 0,45 · k ·<br>(s1,5/M1,4) | s: contenido de<br>finos (%) | Valor por defecto, Punto 4.6,<br>Informe Final Servicio de<br>Recopilación y Sistematización<br>de Factores de Emisión al Aire<br>para el SEIA. | n/a | 6,9 | n/a | n/a | n/a | n/a |
| Excavaciones /<br>Relleno | 0,45 · k ·<br>(s1,5/M1,4) | 0,45 · k ·<br>(s1,5/M1,4) | 0,45 · k ·<br>(s1,5/M1,4) | M: humedad del<br>material (%) | Valor por defecto, Punto 4.6,<br>Informe Final Servicio de<br>Recopilación y Sistematización<br>de Factores de Emisión al Aire<br>para el SEIA. | n/a | 7,9 | n/a | n/a | n/a | n/a |
| Excavaciones /<br>Relleno | Para MPS | kg/h | Punto 4.6, Informe<br>Final Servicio de<br>Recopilación y<br>Sistematización de<br>Factores de<br>Emisión al Aire<br>para el SEIA. | k: factor de<br>tamaño de<br>partícula | Table 11.9-2, Capítulo 11,<br>Sección 11.9"Western Surface<br>Coal Mining", AP-42 | n/a | n/a | 1,0 | n/a | n/a | 1,798 |
| Excavaciones /<br>Relleno | 2,6 · k · (s1,2/M1,3) | 2,6 · k · (s1,2/M1,3) | 2,6 · k · (s1,2/M1,3) | s: contenido de<br>finos (%) | Valor por defecto, Punto 4.6,<br>Informe Final Servicio de<br>Recopilación y Sistematización<br>de Factores de Emisión al Aire<br>para el SEIA. | n/a | n/a | 6,9 | 6,9 | 6,9 | 6,9 |

**Tabla 3-3: - Factores de Emisión Maquinaria - Fase de Cierre.****

| Maquinaria | C:% carga<br>del motor * | Potencia<br>Nominal [kW]<br>* | Factor según potencia [g/kW-h] | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Factor de Emisión según Potencia [kg/h] | Col12 | Col13 | Col14 | Col15 | Col16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Maquinaria** | **C:% carga**<br>**del motor *** | **Potencia**<br>**Nominal [kW]**<br>*** ** | **MP2.5** | **MP10** | **MPS** | **CO** | **NOx** | **HC** | **Referencia** | **MP2.5** | **MP10** | **MPS** | **CO** | **NOx** | **HC** |
| Retroexcavadora | 21% | 66,00 | 1,51 | 1,51 | 1,51 | 5,06 | 14,36 | 2,33 | Tabla 4.10 Guía para la estimación de emisiones<br>atmosféricas de proyectos Inmobiliarios para la<br>Región Metropolitana | 0,021 | 0,021 | 0,021 | 0,070 | 0,199 | 0,032 |
| Motoniveladora | 59% | 149,00 | 1,10 | 1,10 | 1,10 | 3,00 | 14,36 | 1,35 | Tabla 4.10 Guía para la estimación de emisiones<br>atmosféricas de proyectos Inmobiliarios para la<br>Región Metropolitana | 0,097 | 0,097 | 0,097 | 0,264 | 1,262 | 0,119 |
| Rodillo<br>compactador | 55% | 206,00 | 1,10 | 1,10 | 1,10 | 3,00 | 14,36 | 1,35 | Tabla 4.10 Guía para la estimación de emisiones<br>atmosféricas de proyectos Inmobiliarios para la<br>Región Metropolitana | 0,125 | 0,125 | 0,125 | 0,340 | 1,627 | 0,153 |
| Cargador Frontal | 58% | 151,00 | 1,10 | 1,10 | 1,10 | 3,00 | 14,36 | 1,35 | Tabla 4.10 Guía para la estimación de emisiones<br>atmosféricas de proyectos Inmobiliarios para la<br>Región Metropolitana | 0,096 | 0,096 | 0,096 | 0,263 | 1,258 | 0,118 |
| Camión Tolva | 47% | 103,00 | 1,23 | 1,23 | 1,23 | 3,76 | 14,36 | 1,72 | Tabla 4.10 Guía para la estimación de emisiones<br>atmosféricas de proyectos Inmobiliarios para la<br>Región Metropolitana | 0,060 | 0,060 | 0,060 | 0,182 | 0,695 | 0,083 |
| Camión Grúa | 47% | 164,12 | 1,10 | 1,10 | 1,10 | 3,00 | 14,36 | 1,35 | Tabla 4.10 Guía para la estimación de emisiones<br>atmosféricas de proyectos Inmobiliarios para la<br>Región Metropolitana | 0,085 | 0,085 | 0,085 | 0,231 | 1,108 | 0,104 |

**Tabla 3-4: - Factores de Emisión Grupos Electrógenos - Fase de Cierre.****

| Tipo de<br>Maquinaria | Unidad | Referencia<br>Ecuación Factor<br>de Emisión | Factor de Emisión (kg/kg comb.) | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo de**<br>**Maquinaria** | **Unidad** | **Referencia**<br>**Ecuación Factor**<br>**de Emisión** | **MP2.5** | **MP10** | **MPS** | **CO** | **NOx** | **SOx** | **COV** |
| Grupo<br>Electrógeno<br>(Diesel hasta 600<br>hp) | kg/kg comb. | Tabla 3.21.<br>Factores de<br>emisión grupos<br>electrógenos.<br>Guía para la<br>estimación de<br>emisiones<br>atmosféricas en<br>la RM 2019. | 0,006 | 0,006 | 0,006 | 0,019 | 0,086 | 0,006 | 0,007 |

**Tabla 3-5: - Factores de Emisión Resuspensión de Polvo - Fase de Cierre.****

| Actividad | Ecuación Factor de<br>Emisión | Unidad | Referencia Ecuación<br>Factor de Emisión | Parámetros Factores de Emisión | Col6 | Col7 | Col8 | Col9 | Factor de Emisión | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Ecuación Factor de**<br>**Emisión** | **Unidad** | **Referencia Ecuación**<br>**Factor de Emisión** | **Variables** | **Referencias** | **MP2,5** | **MP10** | **MPS** | **MP2,5** | **MP10** | **MPS** |
| Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 1)** | k x (sL)0,91 x (W)1,02 | g/km | Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA. | k: factor de tamaño<br>de partícula | Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA. | 0,15 | 0,62 | 3,23 | 0,42 | 1,73 | 9,01 |
| Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 1)** | k x (sL)0,91 x (W)1,02 | g/km | Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA. | sL: contenido de<br>finos (g/m2) | Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA. | 0,3 | 0,3 | 0,3 | 0,3 | 0,3 | 0,3 |
| Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 1)** | k x (sL)0,91 x (W)1,02 | g/km | Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA. | W: peso promedio<br>de la flota que<br>circula por la vía<br>(ton) | Valor por defecto, Guía para la<br>Estimación de Emisiones<br>Atmosféricas para la Región<br>Metropolitana. | 8,00 | 8,00 | 8,00 | 8,00 | 8,00 | 8,00 |
| Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 2)** | k x (sL)0,91 x (W)1,02 | g/km | Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA. | k: factor de tamaño<br>de partícula | Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA. | 0,15 | 0,62 | 3,23 | 0,90<br> <br> | 3,74<br> <br> | 19,47<br> <br> |
| Tránsito Vehículos<br>camino pavimentado<br>Vehículos Pesados<br>**(Tramo 2)** | k x (sL)0,91 x (W)1,02 | g/km | Punto 3.1, Informe Final<br>Servicio de Recopilación<br>y Sistematización de<br>Factores de Emisión al<br>Aire para el SEIA. | sL: contenido de<br>finos (g/m2) | Punto 3.1, Informe Final<br>Servicio de Recopilación y<br>Sistematización de Factores<br>de Emisión al Aire para el<br>SEIA. | 0,7 | 0,7 | 0,7 | 0,7 | 0,7 | 0,7 |

**Tabla 3-6: - Factores de Emisión Combustión por Tránsito Vehicular - Fase de Cierre.****

| Tipo de Vehículo | Tecnología | Referencia | MP2,5 | MP10 | MPS | CO | NOx | COV | SO2 | NH3 | CC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo de Vehículo** | **Tecnología** | **Referencia** | **g/km** | **g/km** | **g/km** | **g/km** | **g/km** | **g/km** | **g/km** | **g/km** | **g/km** |
| Diesel 7.5-16t | Euro III | EMEP/EEA air pollutant<br>emission inventory guidebook<br>2019. Cap 1.A.3.b.I-IV. | 0,088 | 0,088 | 0,088 | 0,972 | 4,300 | 0,189 | 0,005 | 0,003 | 155 |
| Diesel 16-32t | Euro III | EMEP/EEA air pollutant<br>emission inventory guidebook<br>2019. Cap 1.A.3.b.I-IV. | 0,130 | 0,130 | 0,130 | 1,490 | 6,270 | 0,278 | 0,006 | 0,003 | 210 |

**Tabla 3-7.: Niveles de actividad asociados a movimientos de tierra por Excavación. Fase de Cierre.****

| Actividad | Fuente | Volumen de excavación | Col4 | Horas de excavación | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Actividad** | **Fuente** | **Valor Fase Cierre** | **Unidad** | **Fase Cierre** | **Unidad** |
| Excavaciones | Excavación de Corte/Escarpe | 19.577 | m3 | 653 | h/año |

**Tabla 3-8.: Niveles de actividad asociados a movimientos de tierra por Compactado. Fase de Cierre.****

| Actividad | Fuente | Volumen de excavación | Col4 | Horas de compactación | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Actividad** | **Fuente** | **Valor Fase Cierre** | **Unidad** | **Fase Cierre** | **Unidad** |
| Compactación | Superficie Total de Proyecto | 485,52 | KVT | 161,84 | h/año |

**Tabla 3-9.: Niveles de actividad asociados a movimientos de tierra por Transferencia de Material. Fase de****

| Actividad | Fuente | Volumen de material a transferir | Col4 | Peso de material a transferir | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Actividad** | **Fuente** | **Valor Fase Cierre** | **Unidad** | **Fase Cierre** | **Unidad** |
| Carga/Descarga de<br>material | Excavaciones | 39.154 | m3 | 70.477 | t/año |

**Tabla 3-10: - Maquinaria Utilizada - Fase de Cierre.****

| Maquinaria | Función | Cantidad | Potencia [kW] | Horas totales [h] |
| --- | --- | --- | --- | --- |
| Retroexcavadora | Movimiento de Tierra | 1 | 66,0 | 250 |
| Motoniveladora | Restauración Geoforma | 1 | 149,0 | 350 |
| Rodillo compactador | Restauración Geoforma | 2 | 206,0 | 650 |
| Cargador Frontal | Movimiento de Tierra | 1 | 151,0 | 100 |
| Camión Tolva | Movimiento de Tierra | 2 | 103,0 | 450 |
| Camión Grúa | Desmantelación | 1 | 164,1 | 336 |
| **Total** | **Total** | **Total** | **Total** | **2.136** |

**Tabla 3-11.: Grupos Electrógenos Utilizados - Fase de Cierre.****

| Grupo electrógeno | Función | Cantidad | Potencia<br>aparente<br>[kVA] | Potencia<br>[kW] | Consumo<br>[kW-h] | Consumo [kg<br>comb/año] |
| --- | --- | --- | --- | --- | --- | --- |
| Grupo electrógeno 20 kVA | Frente de trabajo | 1 | 20,0 | 16,0 | 16.8962 | 4.227 |

**Tabla 3-12: - Tramos de los caminos del proyecto.****

| Tramo | Descripción | Desde | Hasta | Tipo | Longitud<br>(km) |
| --- | --- | --- | --- | --- | --- |
| Tramo 1 | Acceso y Transito<br>Principal | Antofagasta | Empalme Ruta B-262 | Pavimentado | 63,40 |
| Tramo 2 | Ruta B-262 desde Ruta<br>1 a Quinta Industrial | Empalme Ruta B-262 (R-1) | Empalme Ruta B-262 Av.<br>Quinta Industrial (Km<br>7.4) | Pavimentado | 5,10 |
| Tramo 3 | Acceso TMM | Empalme Av. Quinta<br>Industrial | Acceso TMM | Pavimentado | 1,00 |
| Tramo 4 | Ruta B-262 hasta cruce<br>Compañía de<br>Fertilizantes | Empalme Ruta B-262 Av.<br>Quinta Industrial (Km 7.4) | Empalme Ruta B-262<br>Compañía de<br>Fertilizantes | Pavimentado | 5,97 |
| Tramo 5 | Ruta B-262 cruce<br>Compañía de<br>Fertilizantes hasta<br>Centro Mejillones | Empalme Ruta B-262<br>Compañía de Fertilizantes | Centro Mejillones | Pavimentado | 1,29 |
| Tramo 6 | Transporte Personal-<br>Insumos-Residuos | Empalme Ruta B-262<br>Compañía de Fertilizantes | Empalme Ruta B-272 | Pavimentado | 1,42 |
| Tramo 7 | Transporte Personal-<br>Insumos-Residuos | Ruta B-272 | Empalme Acceso<br>Vertedero | Pavimentado | 2,85 |
| Tramo 8 | Transporte Personal-<br>Insumos-Residuos | Empalme Acceso Vertedero | Vertedero | Pavimentado | 2,16 |

**Tabla 3-13.: Movimientos vehiculares para cada tramo. Fase de cierre.****

| Actividad | Tipo de vehículo Proyecto | Vehículo Standard | Cantidad de meses | Peso Promedio | Viajes Fase de<br>Cierre | Origen - destino |
| --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Tipo de vehículo Proyecto** | **Vehículo Standard** | **Cantidad de meses** | **(t)** | **(t)** | **(t)** |
| Transporte de Insumos | Camión Contenedor 20 pies | Diesel 16-32t | 4 | 25,0 | 96 | Antofagasta o Mejillones - TMM |
| Transporte de Combustible | Camión Cisterna | Diesel 16-32t | 4 | 25,0 | 32 | Antofagasta o Mejillones - TMM |
| Transporte de Residuos Domiciliarios | Camión Tolva 16t | Diesel 7.5-16t | 4 | 10,0 | 32 | TMM - Vertedero |
| Transporte de Residuos Industriales | Camión Tolva 16t | Diesel 7.5-16t | 4 | 10,0 | 32 | Antofagasta o Mejillones - TMM |
| Transporte de Residuos Peligrosos | Camión Tolva 16t | Diesel 7.5-16t | 4 | 10,0 | 8,0 | Antofagasta o Mejillones - TMM |
| Transporte Personal desde Mejillones | Bus para 30 personas | Urban Buses Standard | 4 | 16,0 | 88 | Mejillones - TMM |
| Transporte Personal desde Antofagasta | Bus para 30 personas | Urban Buses Standard | 4 | 16,0 | 88 | Antofagasta - TMM |

**Tabla 3-14.: Distancias por recorrer en cada tramo - Fase de Cierre.****

| Actividad | Tramo 1 | Tramo 2 | Tramo 3 | Tramo 4 | Tramo 5 | Tramo 6 | Tramo 7 | Tramo 8 | Total<br>Pavimentado<br>(km) | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **(km)** | **(km)** | **(km)** | **(km)** | **(km)** | **(km)** | **(km)** | **(km)** | **(km)** | **(km)** |
| Transporte de Insumos | 12.173 | 979 | 192 |  |  |  |  |  | 13.344 | 13.344 |
| Transporte de Combustible | 4.058 | 326 | 64 |  |  |  |  |  | 4.448 | 4.448 |
| Transporte de Residuos Domiciliarios |  |  | 64 | 382 |  | 91 | 182 | 138 | 858 | 858 |
| Transporte de Residuos Industriales | 4.058 | 326 | 64 |  |  |  |  |  | 4.448 | 4.448 |
| Transporte de Residuos Peligrosos | 1.014 | 82 | 16 |  |  |  |  |  | 1.112 | 1.112 |
| Transporte Personal desde Mejillones |  |  | 176 | 1.051 | 227 |  |  |  | 1.454 | 1.454 |
| Transporte Personal desde<br>Antofagasta | 11.158 | 898 | 176 |  |  |  |  |  | 12.232 | 12.232 |
| **Total** | **32.461** | **2.611** | **752** | **1.433** | **227** | **91** | **182** | **138** | **37.895** | **37.895** |

**Tabla 3-15: - Emisiones por movimientos de tierra. Fase de Cierre.****

| Identificación Fuente | Factor de Emisión | Col3 | Col4 | Col5 | Nivel de Actividad | Col7 | Emisión Cierre (t/año) | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Identificación Fuente** | **MP2.5** | **MP10** | **MPS** | **Unidad** | **Cantidad** | **Unidad** | **MP2.5** | **MP10** | **MPS** |
| Excavación | 0,189 | 0,339 | 1,798 | kg/h | 652,57 | h/año | 0,123 | 0,221 | 1,173 |
| Compactado | 0,189 | 0,339 | 1,798 | kg/h | 161,84 | h/año | 0,031 | 0,055 | 0,291 |
| Transferencia de material (carga/descarga) | 1,39,E-05 | 9,16,E-05 | 1,94,E-04 | kg/t | 70.477,20 | t/año | 0,001 | 0,006 | 0,014 |
| **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **0,155** | **0,282** | **1,478** |

**Tabla 3-16: - Emisiones Utilización de Maquinaria. Fase de Cierre.****

| Maquinaria | Cantidad | Factor de Emisión (kg/h maquinaria) | Col4 | Col5 | Col6 | Col7 | Col8 | Nivel de Actividad | Emisión (t/año) (Año1) | Col11 | Col12 | Col13 | Col14 | Col15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Maquinaria** | **Cantidad** | **MP2.5** | **MP10** | **MPS** | **CO** | **NOx** | **HC** | **Uso (h/año)** | **MP2.5** | **MP10** | **MPS** | **CO** | **NOx** | **HC** |
| Retroexcavadora | 1 | 0,021 | 0,021 | 0,021 | 0,070 | 0,199 | 0,032 | 250 | 0,005 | 0,005 | 0,005 | 0,018 | 0,050 | 0,008 |
| Motoniveladora | 1 | 0,097 | 0,097 | 0,097 | 0,264 | 1,262 | 0,119 | 350 | 0,034 | 0,034 | 0,034 | 0,092 | 0,442 | 0,042 |
| Rodillo compactador | 2 | 0,125 | 0,125 | 0,125 | 0,340 | 1,627 | 0,153 | 650 | 0,081 | 0,081 | 0,081 | 0,221 | 1,058 | 0,099 |
| Cargador Frontal | 1 | 0,096 | 0,096 | 0,096 | 0,263 | 1,258 | 0,118 | 100 | 0,010 | 0,010 | 0,010 | 0,026 | 0,126 | 0,012 |
| Camión Tolva | 2 | 0,060 | 0,060 | 0,060 | 0,182 | 0,695 | 0,083 | 450 | 0,027 | 0,027 | 0,027 | 0,082 | 0,313 | 0,037 |
| Camión Grúa | 1 | 0,085 | 0,085 | 0,085 | 0,231 | 1,108 | 0,104 | 336 | 0,029 | 0,029 | 0,029 | 0,078 | 0,372 | 0,035 |
| **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **0,185** | **0,185** | **0,185** | **0,517** | **2,360** | **0,233** |

**Tabla 3-17: - Emisiones Utilización de Grupos Electrógenos. Fase de Cierre.****

| Grupo electrógeno | P: potencia<br>nominal<br>(kW) | Factor de Emisión (kg/kg comb.) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Nivel de Actividad | Emisión (t/año) | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo electrógeno** | **P: potencia**<br>**nominal**<br>**(kW)** | **MP2.5** | **MP10** | **MPS** | **CO** | **NOx** | **SOx** | **COV** | **Uso (kg. comb./año)** | **MP2.5** | **MP10** | **MPS** | **CO** | **NOx** | **SOx** | **COV** |
| Grupo electrógeno 20 kVA | 16 | 0,006 | 0,006 | 0,006 | 0,019 | 0,086 | 0,006 | 0,007 | 4.227 | 0,026 | 0,026 | 0,026 | 0,079 | 0,366 | 0,024 | 0,030 |
| **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **0,026** | **0,026** | **0,026** | **0,079** | **0,366** | **0,024** | **0,030** |

**Tabla 3-18: - Emisiones Producto de Resuspensión del Polvo. Fase de Cierre.****

| Tramo | Factor de Emisión (g/KVT) | Col3 | Col4 | Distancia Total Recorrida (km/año) | Porcentaje de Control (%) | Emisión (t/año) - Cierre | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tramo** | **MP2.5** | **MP10** | **MPS** | **MPS** | **MPS** | **MP2.5** | **MP10** | **MPS** |
| Tramo 1 | 0,42 | 1,73 | 9,01 | 32.461 | 0% | 0,014 | 0,056 | 0,292 |
| Tramo 2 | 0,90 | 3,74 | 19,47 | 2.611 | 0% | 0,002 | 0,010 | 0,051 |
| Tramo 3 | 0,90 | 3,74 | 19,47 | 752 | 0% | 0,001 | 0,003 | 0,015 |
| Tramo 4 | 0,90 | 3,74 | 19,47 | 1.433 | 0% | 0,001 | 0,005 | 0,028 |
| Tramo 5 | 0,90 | 3,74 | 19,47 | 227 | 0% | 0,000 | 0,001 | 0,004 |
| Tramo 6 | 0,90 | 3,74 | 19,47 | 91 | 0% | 0,000 | 0,000 | 0,002 |
| Tramo 7 | 0,90 | 3,74 | 19,47 | 182 | 0% | 0,000 | 0,001 | 0,004 |
| Tramo 8 | 0,90 | 3,74 | 19,47 | 138 | 0% | 0,000 | 0,001 | 0,003 |
| **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **0,018** | **0,076** | **0,398** |

**Tabla 3-19: - Emisiones Producto de Combustión Vehicular. Fase de Cierre.****

| Tipo de vehículo | Factor de Emisión (g/KVT) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Distancia Total<br>Recorrida - Cierre<br>(km/año) | Emisión (t/año) | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo de vehículo** | **MP2.5** | **MP10** | **MPS** | **CO** | **NOx ** | **HC** | **SO2 ** | **NH3 ** | **NH3 ** | **MP2.5** | **MP10** | **MPS** | **CO** | **NOx** | **HC** | **SO2 ** | **NH3 ** |
| Diesel 7.5-16t | 0,088 | 0,088 | 0,088 | 0,972 | 4,300 | 0,189 | 0,005 | 0,003 | 6.418 | 0,001 | 0,001 | 0,001 | 0,006 | 0,028 | 0,001 | 2,98,E-05 | 1,86,E-05 |
| Diesel 16-32t | 0,130 | 0,130 | 0,130 | 1,490 | 6,270 | 0,278 | 0,006 | 0,003 | 17.792 | 0,002 | 0,002 | 0,002 | 0,027 | 0,112 | 0,005 | 1,12,E-04 | 5,16,E-05 |
| Urban Buses Standard | 0,207 | 0,207 | 0,207 | 2,670 | 9,380 | 0,409 | 0,009 | 0,003 | 13.686 | 0,003 | 0,003 | 0,003 | 0,037 | 0,128 | 0,006 | 1,24,E-04 | 3,97,E-05 |
| **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **0,006** | **0,006** | **0,006** | **0,069** | **0,268** | **0,012** | **2,66,E-04** | **1,10,E-04** |

**Tabla 3-20: - Resumen Emisiones. Fase de Cierre.****

| Actividad | Fase de Cierre (t/año) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MP2.5** | **MP10** | **MPS** | **CO**<br> | **NOx**<br> | **SOx**<br> | **HC**<br> | **NH3 **<br> |
| Movimiento de Tierra | 0,15 | 0,28 | 1,48 |  |  | <br> |  | <br> |
| Maquinaria | 0,19 | 0,19 | 0,19 | 0,52 | 2,36 |  | 0,23 |  |
| Tránsito Vehicular -<br>Resuspensión de Polvo | 0,02 | 0,08 | 0,40 |  |  |  |  |  |
| Tránsito Vehicular - Combustión | 0,01 | 0,01 | 0,01 | 0,07 | 0,27 | 0,01 | 0,00 | 0,00<br> |
| Grupos Electrógenos | 0,03 | 0,03 | 0,03 | 0,08 | 0,37 | 0,02 | 0,03 |  |
| **Total** | **0,39** | **0,58** | **2,09** | **0,66** | **2,99** | **0,04** | **0,26** | **0,00** |

**Tabla 4-1.: Configuración parámetros principales WRF****

| Parámetro | Valor |
| --- | --- |
| **Dominio** | **Dominio** |
| Resolución horizontal | 1 km |
| Proyección | Lambert |
| Dimensión | 58x58x44 |
| Número de niveles verticales | 44 |
| Niveles verticales (eta) | 0.000000, 0.051578, 0.101822, 0.150735, 0.198315, 0.244562,<br>0.289477, 0.333059, 0.375309, 0.416226,<br>0.455810, 0.494062, 0.530982, 0.566569, 0.600823, 0.633745,<br>0.665334, 0.695591, 0.724515, 0.752107, 0.778366, 0.803292,<br>0.826886, 0.849148, 0.870076, 0.889673, 0.907937, 0.923302,<br>0.937101, 0.949333, 0.960000, 0.969101, 0.976635, 0.982603,<br>0.987005, 0.989841, 0.991111, 0.992381, 0.993651, 0.994921,<br>0.996190, 0.997460, 0.998730, 1.000000, |
| **Física** | **Física** |
| Esquema de radiación | RRTMG-fast (Onda corta y larga) |
| Modelo de suelo | Modelo Noah Land Surface |
| Tratamiento de capa superficial | Revised MM5 surface layer |
| Parametrización de capa límite | Yonsei University |
| Esquema de convección | Kain-Fritsch |
| Microfísica de nubes y precipitación | WSM 3-class |
| **Dinámica** | **Dinámica** |
| Parametrización de turbulencia | Smagorinsky |
| Núcleo dinámico | EM (Advanced Mass) y No hidroestático |
| Advección | positiva-definitiva |

**Tabla 4-2.: Coordenadas de Ubicación, Estación de Monitoreo Meteorológico JJ Latorre.****

| Estación de<br>Monitoreo | Variables Meteorológicas<br>Registradas | Periodo monitoreado<br>considerado para este<br>estudio | Coordenadas UTM (Datum<br>WGS84) | Col5 |
| --- | --- | --- | --- | --- |
| **Estación de**<br>**Monitoreo** | **Variables Meteorológicas**<br>**Registradas** | **Periodo monitoreado**<br>**considerado para este**<br>**estudio** | **Este (m)** | **Norte (m)** |
| JJ Latorre | Velocidad del Viento (m/s) | 1 de enero 2020 al 31 de<br>diciembre 2020 | 352.346 | 7.444.100 |
| JJ Latorre | Dirección del Viento (°) | Dirección del Viento (°) | Dirección del Viento (°) | Dirección del Viento (°) |
| JJ Latorre | Temperatura del Aire (°C) | Temperatura del Aire (°C) | Temperatura del Aire (°C) | Temperatura del Aire (°C) |
| JJ Latorre | Humedad Relativa (%) | Humedad Relativa (%) | Humedad Relativa (%) | Humedad Relativa (%) |
| JJ Latorre | Radiación Solar (W/m2) | Radiación Solar (W/m2) | Radiación Solar (W/m2) | Radiación Solar (W/m2) |

**Tabla 4-3.: Resumen de Información Velocidad del Viento Observada en Estación JJ Latorre.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2020** |
| Velocidad de Viento (m/s) | Promedio | 2,4 |
| Velocidad de Viento (m/s) | Máximo | 9,5 |
| Velocidad de Viento (m/s) | Mínimo | 0,0 |
| Porcentaje de Calmas (%) | Porcentaje de Calmas (%) | 1,6 |
| Datos Válidos (%) | Datos Válidos (%) | 100,0% |

**Tabla 4-4.: Frecuencia de distribución Velocidad y Dirección del Viento. Periodo enero 2020 a diciembre 2020. Observado en Estación JJ Latorre.****

| Dirección | Col2 | Distribución Porcentual de Velocidad del Viento (m/s) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección** | **Dirección** | **0,50 - 2,10** | **2,10 - 3,60** | **3,60 - 5,70** | **5,70 - 8,80** | **8,80 - 11,10** | **>= 11,10** | **Total (%)** |
| 348,75 - 11,25 | N | 7,1% | 0,5% | 0,0% | 0,0% | 0,0% | 0,0% | 7,6% |
| 11,25 - 33,75 | NNE | 7,7% | 1,0% | 0,0% | 0,0% | 0,0% | 0,0% | 8,7% |
| 33,75 - 56,25 | NE | 1,5% | 0,3% | 0,0% | 0,0% | 0,0% | 0,0% | 1,8% |
| 56,25 - 78,75 | ENE | 0,4% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,4% |
| 78,75 - 101,25 | E | 0,4% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,4% |
| 101,25 - 123,75 | ESE | 1,1% | 0,1% | 0,0% | 0,0% | 0,0% | 0,0% | 1,2% |
| 123,75 - 146,25 | SE | 1,8% | 0,2% | 0,0% | 0,0% | 0,0% | 0,0% | 2,1% |
| 146,25 - 168,75 | SSE | 4,2% | 1,6% | 0,0% | 0,0% | 0,0% | 0,0% | 5,9% |
| 168,75 - 191,25 | S | 8,1% | 11,7% | 10,6% | 3,1% | 0,0% | 0,0% | 33,5% |
| 191,25 - 213,75 | SSW | 5,0% | 5,2% | 3,9% | 0,2% | 0,0% | 0,0% | 14,3% |
| 213,75 - 236,25 | SW | 1,2% | 0,9% | 0,3% | 0,0% | 0,0% | 0,0% | 2,5% |
| 236,25 - 258,75 | WSW | 0,7% | 0,1% | 0,0% | 0,0% | 0,0% | 0,0% | 0,9% |
| 258,75 - 281,25 | W | 0,7% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,7% |
| 281,25 - 303,75 | WNW | 1,3% | 0,3% | 0,0% | 0,0% | 0,0% | 0,0% | 1,6% |
| 303,75 - 326,25 | NW | 3,1% | 1,9% | 0,4% | 0,0% | 0,0% | 0,0% | 5,3% |
| 326,25 - 348,75 | NNW | 4,8% | 6,3% | 0,4% | 0,0% | 0,0% | 0,0% | 11,5% |
| Sub-Total | Sub-Total | 49,1% | 30,2% | 15,7% | 3,3% | 0,0% | 0,0% | 98,4% |
| Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | 1,6% |

**Tabla 4-5.: Resumen de Información Temperatura Observada en Estación JJ Latorre.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2020** |
| Temperatura (°C) | Promedio | 18,6 |
| Temperatura (°C) | Máximo | 32,1 |
| Temperatura (°C) | Mínimo | 6,5 |
| Datos Válidos (%) | Datos Válidos (%) | 100,0% |

**Tabla 4-6.: Resumen de Información Humedad Relativa Observada en Estación JJ Latorre.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2020** |
| Humedad Relativa (%) | Promedio | 61,4 |
| Humedad Relativa (%) | Máximo | 84,8 |
| Humedad Relativa (%) | Mínimo | 23,6 |
| % Datos Válidos | % Datos Válidos | 100,0% |

**Tabla 4-7.: Resumen de Información Radiación Solar Observada en Estación JJ Latorre.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2020** |
| Radiación Solar (W/m2) | Promedio | 243,7 |
| Radiación Solar (W/m2) | Máximo | 1.121,8 |
| Radiación Solar (W/m2) | Mínimo | 0,0 |
| % Datos Válidos | % Datos Válidos | 100,0% |

**Tabla 4-8.: Resumen de Información Velocidad del Viento Modelada en Estación JJ Latorre, Año 2020.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2020** |
| Velocidad de Viento (m/s) | Promedio | 3,3 |
| Velocidad de Viento (m/s) | Máximo | 9,7 |
| Velocidad de Viento (m/s) | Mínimo | 0,1 |
| Porcentaje de Calmas (%) | Porcentaje de Calmas (%) | 0,9 |
| Datos Válidos (%) | Datos Válidos (%) | 100,0% |

**Tabla 4-9.: Frecuencia de distribución Velocidad y Dirección del Viento. Período enero a diciembre 2020. Modelado en Estación JJ Latorre.****

| Dirección | Col2 | Distribución Porcentual de Velocidad del Viento (m/s) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección** | **Dirección** | **0,50 - 2,10** | **2,10 - 3,60** | **3,60 - 5,70** | **5,70 - 8,80** | **8,80 - 11,10** | **>= 11,10** | **Total (%)** |
| 348,75 - 11,25 | N | 1,07% | 3,81% | 4,31% | 0,16% | 0,00% | 0,00% | 9,36% |
| 11,25 - 33,75 | NNE | 0,77% | 4,30% | 2,19% | 0,01% | 0,00% | 0,00% | 7,27% |
| 33,75 - 56,25 | NE | 1,09% | 3,69% | 0,99% | 0,00% | 0,00% | 0,00% | 5,77% |
| 56,25 - 78,75 | ENE | 0,91% | 0,68% | 0,06% | 0,00% | 0,00% | 0,00% | 1,65% |
| 78,75 - 101,25 | E | 0,60% | 0,05% | 0,00% | 0,00% | 0,00% | 0,00% | 0,65% |
| 101,25 - 123,75 | ESE | 0,56% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% | 0,57% |
| 123,75 - 146,25 | SE | 0,72% | 0,11% | 0,00% | 0,00% | 0,00% | 0,00% | 0,83% |
| 146,25 - 168,75 | SSE | 2,08% | 1,06% | 0,01% | 0,00% | 0,00% | 0,00% | 3,15% |
| 168,75 - 191,25 | S | 4,64% | 19,43% | 5,50% | 0,47% | 0,01% | 0,00% | 30,05% |
| 191,25 - 213,75 | SSW | 2,38% | 9,54% | 15,63% | 4,88% | 0,00% | 0,00% | 32,43% |
| 213,75 - 236,25 | SW | 0,56% | 0,79% | 1,56% | 0,08% | 0,00% | 0,00% | 2,98% |
| 236,25 - 258,75 | WSW | 0,31% | 0,15% | 0,00% | 0,00% | 0,00% | 0,00% | 0,46% |
| 258,75 - 281,25 | W | 0,31% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,31% |
| 281,25 - 303,75 | WNW | 0,20% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,20% |
| 303,75 - 326,25 | NW | 0,57% | 0,11% | 0,00% | 0,00% | 0,00% | 0,00% | 0,68% |
| 326,25 - 348,75 | NNW | 0,67% | 1,53% | 0,55% | 0,01% | 0,00% | 0,00% | 2,76% |
| Sub-Total | Sub-Total | 17.45% | 45,26% | 30,79% | 5,61% | 0,01% | 0,00% | 99,13% |
| Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | 0,87% |

**Tabla 4-10.: Resumen de Información Temperatura Modelada en Estación JJ Latorre.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2020** |
| Temperatura (°C) | Promedio | 18,2 |
| Temperatura (°C) | Máximo | 27,8 |
| Temperatura (°C) | Mínimo | 9,1 |
| Datos Válidos (%) | Datos Válidos (%) | 100,0% |

**Tabla 4-11.: Resumen de Información Altura de Capa de Mezcla Modelada en Estación JJ Latorre.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2020** |
| Altura de Capa de Mezcla (m) | Promedio | 282,01 |
| Altura de Capa de Mezcla (m) | Máximo | 1.622,46 |
| Altura de Capa de Mezcla (m) | Mínimo | 10,00 |
| % Datos Válidos | % Datos Válidos | 100,0% |

**Tabla 4-12.: Estadígrafos de Dispersión de Velocidad del Viento y Temperatura.****

| Medida de Error | Velocidad del Viento | Temperatura |
| --- | --- | --- |
| **Medida de Error** | **Ciclo Diario** | **Ciclo Diario** |
| Sesgo | 0,84 | -0,40 |
| ECM | 0,87 | 0,79 |
| r | 0,94 | 0,97 |

**Tabla 4-13.: Normas primarias de calidad del aire.****

| Contaminante | Decreto<br>Aplicable | Norma | Col4 | Periodo de Evaluación de Cumplimiento de Norma |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Decreto**<br>**Aplicable** | **Valor** | **Unidad** | **Unidad** |
| Material Particulado<br>Respirable Fino<br>(MP2,5) | Decreto<br>Supremo<br>N°12/2011 | 50 | μg/m3 | Percentil 98 de las concentraciones de 24 horas |
| Material Particulado<br>Respirable Fino<br>(MP2,5) | Decreto<br>Supremo<br>N°12/2011 | 20 | 20 | Concentración anual |
| Material Particulado<br>Respirable (MP10) | Decreto<br>Supremo<br>N°12/2022 | 130 | μg/m3N | Percentil 98 de las concentraciones de 24 horas |
| Material Particulado<br>Respirable (MP10) | Decreto<br>Supremo<br>N°12/2022 | 50 | 50 | Concentración anual |
| Monóxido de<br>Carbono (CO) | Decreto<br>Supremo<br>N°115/2002 | 30 | mg/m3N | Percentil 99 de los máximos diarios de concentración<br>de 1 hora |
| Monóxido de<br>Carbono (CO) | Decreto<br>Supremo<br>N°115/2002 | 10 | 10 | Percentil 99 de los máximos diarios de concentración<br>de 8 horas |
| Dióxido de<br>Nitrógeno (NO2) | Decreto<br>Supremo<br>N°114/2002 | 400 | μg/m3N | Percentil 99 de los máximos diarios de concentración<br>de 1 hora |
| Dióxido de<br>Nitrógeno (NO2) | Decreto<br>Supremo<br>N°114/2002 | 100 | 100 | Concentración anual |
| Dióxido de Azufre<br>(SO2) | Decreto<br>Supremo<br>N°104/2019 | 350 | μg/m3N | Percentil 98,5 de las concentraciones de 1 hora. |
| Dióxido de Azufre<br>(SO2) | Decreto<br>Supremo<br>N°104/2019 | 150 | 150 | Percentil 99 de las concentraciones de 24 horas |
| Dióxido de Azufre<br>(SO2) | Decreto<br>Supremo<br>N°104/2019 | 60 | 60 | Concentración anual |
| Ozono (O3) | Decreto<br>Supremo<br>N°112/02 | 120 | μg/m3N | Percentil 99 de los máximos diarios de concentración<br>de 8 horas |

**Tabla 4-14.: Normas secundarias de calidad del aire.****

| Contaminante | Decreto<br>Aplicable | Norma | Col4 | Periodo de Evaluación de Cumplimiento de Norma |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Decreto**<br>**Aplicable** | **Valor** | **Unidad** | **Unidad** |
| Material Particulado<br>Sedimentable (MPS) | Norma de la<br>Confederación<br>Suiza | 200 | mg/m2/día | Promedio aritmético depositación anual |
| Dióxido de Azufre<br>(SO2) | Decreto<br>Supremo<br>N°22/2010 | 1.000 | μg/m3N | Percentil 99,73 de las concentraciones de 1 hora. |
| Dióxido de Azufre<br>(SO2) | Decreto<br>Supremo<br>N°22/2010 | 365 | 365 | Percentil 99,7 de las concentraciones de 24 horas |
| Dióxido de Azufre<br>(SO2) | Decreto<br>Supremo<br>N°22/2010 | 80 | 80 | Concentración anual |

**Tabla 4-15.: Caracterización de Estaciones de Monitoreo de Calidad del Aire Utilizadas para Línea de Base de Calidad del Aire.****

| Estación de<br>Monitoreo | Coordenadas UTM<br>(Datum WGS84) | Col3 | Contaminantes Medidos | Periodo de Datos Disponibles<br>por Contaminante | Propietario | Operador | Fuente de Información |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Estación de**<br>**Monitoreo** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| JJ Latorre | 352.064 | 7.444.407 | Material Particulado<br>Respirable (MP10) | 1 de enero 2019 al 31 de<br>diciembre 2021 | ENAEX | Algoritmos | https://snifa.sma.gob.cl/S<br>eguimientoAmbiental/Fic<br>ha/123141 |
| JJ Latorre | 352.064 | 7.444.407 | Dióxido de Nitrógeno (NO2) | 1 de enero 2019 al 31 de<br>diciembre 2021 | 1 de enero 2019 al 31 de<br>diciembre 2021 | 1 de enero 2019 al 31 de<br>diciembre 2021 | 1 de enero 2019 al 31 de<br>diciembre 2021 |

**Tabla 4-16.: Resultados Monitoreo MP10. Estación JJ Latorre.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| MP10 (μg/m3N) | Número de datos medidos | 121 | 122 | 122 |
| MP10 (μg/m3N) | Número de datos válidos | 114 | 107 | 114 |
| MP10 (μg/m3N) | Porcentaje de datos válidos | 94,2 | 87,7 | 93,4 |
| MP10 (μg/m3N) | Mínimo diario | 9 | 6 | 7 |
| MP10 (μg/m3N) | Máximo diario | 57 | 34 | 55 |
| MP10 (μg/m3N) | Percentil 98 diario | 35 | 27 | 39 |
| MP10 (μg/m3N) | Media anual | 21,9 | 18,0 | 21,7 |
| MP10 (μg/m3N) | Media trianual | 20,5 | 20,5 | 20,5 |

**Tabla 4-17-: Comparación de Monitoreo de MP10 con Normativa. Estación JJ Latorre.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 1 de enero de 2019 -<br>31 de diciembre de 20197 | Percentil 98 de<br>la concentración<br>media diaria | 35,0 | 130 | μg/m3N | 23,3% |
| MP10 | 1 de enero de 2019 -<br>31 de diciembre de 2021 | Concentración<br>media trianual | 20,2 | 50 | μg/m3N | 40,4% |

**Tabla 4-18.: Resultados de Monitoreo de NO** **2** **. Estación JJ Latorre** **[8]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| NO2 (μg/m3N) | Percentil 99 de los máximos diarios de<br>concentración horaria | 40,2 | 43,4 | 46,2 |
| NO2 (μg/m3N) | Promedio trianual percentil 99 de los<br>máximos diarios de concentración<br>horaria | 43,2 | 43,2 | 43,2 |
| NO2 (μg/m3N) | Media anual | 5,0 | 4,3 | 4,4 |
| NO2 (μg/m3N) | Media trianual | 4,6 | 4,6 | 4,6 |

**Tabla 4-19.: Comparación de Monitoreo de NO** **2** **con Normativa. Estación JJ Latorre.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- |
| NO2 | 1 de enero de 2019 -<br>31 de diciembre de 2021 | Percentil 99 de<br>los máximos<br>diarios de<br>concentración de<br>1 hora | 43,2 | 400 | μg/m3N | 10,8% |

**Tabla 4-20.: Resultados Monitoreo de MP10. Estación Jardín Infantil.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| MP10 (μg/m3N) | Número de datos medidos | 121 | 122 | 122 |

**Tabla 4-21.: Comparación de Monitoreo de MP10 con Normativa. Estación Jardín Infantil.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 1 de enero de 2020-<br>31 de diciembre de 20219 | Percentil 98 de la<br>concentración media diaria | 32,0 | 130 | μg/m3N | 24,6% |
| MP10 | 1 de enero de 2019 -<br>31 de diciembre de 2021 | Concentración media<br>trianual | 20,4 | 50 | μg/m3N | 40,8% |

**Tabla 4-22.: Resultados Monitoreo de NO** **2** **. Estación Jardín Infantil** **[10]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| NO2 (μg/m3N) | Percentil 99 de los máximos diarios de<br>concentración horaria | 44,7 | 58,5 | 55,8 |
| NO2 (μg/m3N) | Promedio trianual percentil 99 de los<br>máximos diarios de concentración horaria | 53,0 | 53,0 | 53,0 |
| NO2 (μg/m3N) | Media anual | 7,1 | 6,6 | 7,2 |
| NO2 (μg/m3N) | Media trianual | 7,0 | 7,0 | 7,0 |

**Tabla 4-23.: Comparación de Monitoreo de NO** **2** **con Normativa. Estación Jardín Infantil.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| NO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora | 53,0 | 400 | μg/m3N | 13,3% |
| NO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Concentración media<br>trianual | 7,0 | 100 | μg/m3N | 7,0% |

**Tabla 4-24.: Resultados Monitoreo de MP10. Estación Puerto Mejillones.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019 ** | **2020 ** | **2021 ** |
| MP10 (μg/m3N) | Número de datos medidos | 121 | 122 | 91 |
| MP10 (μg/m3N) | Número de datos válidos | 116 | 105 | 85 |
| MP10 (μg/m3N) | Porcentaje de datos válidos | 95,9 | 86,1 | 93,4 |
| MP10 (μg/m3N) | Mínimo diario | 6 | 8 | 5 |
| MP10 (μg/m3N) | Máximo diario | 108 | 36 | 50 |
| MP10 (μg/m3N) | Percentil 98 diario | 29 | 29 | 34 |
| MP10 (μg/m3N) | Media anual | 20,0 | 19,5 | 20,411 |
| MP10 (μg/m3N) | Media trianual | 20,0 | 20,0 | 20,0 |

**Tabla 4-25.: Comparación de Monitoreo de MP10 con Normativa. Estación Puerto Mejillones.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 1 de enero de 2021-<br>30 de septiembre de<br>202112 | Percentil 98 de la<br>concentración media diaria | 34,0 | 130 | μg/m3N | 26,2% |
| MP10 | 1 de enero de 2018 -<br>30 de septiembre de 2021 | Concentración media<br>trianual | 20,0 | 50 | μg/m3N | 40,0% |

**Tabla 4-26.: Resultados Monitoreo MP2,5. Estación Ferrocarril** **[13]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2017** | **2018** | **2019** |
| MP2,5 (μg/m3) | Percentil 98 diario | 23,0 | 20,0 | 17,0 |
| MP2,5 (μg/m3) | Media anual | 10,0 | 10,0 | 7,0 |
| MP2,5 (μg/m3) | Media trianual | 9,0 | 9,0 | 9,0 |

**Tabla 4-27.: Comparación de Monitoreo de MP2,5 con Normativa. Estación Ferrocarril.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP2,5 | 1 de enero de 2017 - | Percentil 98 de la<br>concentración<br>media diaria | 23,0 | 50 | μg/m3 | 46,0% |

**Tabla 4-28: - Resultados Monitoreo de MP10. Estación Ferrocarril** **[15]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2017** | **2018** | **2019** |
| MP10 (μg/m3N) | Percentil 98 diario | 32,0 | 41,0 | 28,0 |
| MP10 (μg/m3N) | Media anual | 16,0 | 15,0 | 16,0 |
| MP10 (μg/m3N) | Media trianual | 15,7 | 15,7 | 15,7 |

**Tabla 4-29: - Comparación de Monitoreo de MP10 con Normativa. Estación Ferrocarril.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 1 de enero de 2018 -<br>31 de diciembre de 201816 | Percentil 98 de la<br>concentración<br>media diaria | 41,0 | 130 | μg/m3N | 31,5% |
| MP10 | 1 de enero de 2017 -<br>31 de diciembre de 2019 | Concentración<br>media trianual | 15,7 | 50 | μg/m3N | 31,3% |

**Tabla 4-30.: Resultados Monitoreo de NO** **2** **. Estación Ferrocarril** **[17]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2017** | **2018** | **2019** |
| NO2 (μg/m3N) | Percentil 99 de los máximos diarios de<br>concentración horaria | 35,5 | 42,2 | 40,5 |
| NO2 (μg/m3N) | Promedio trianual percentil 99 de los<br>máximos diarios de concentración horaria | 39,4 | 39,4 | 39,4 |
| NO2 (μg/m3N) | Media anual | 2,7 | 2,5 | 2,3 |
| NO2 (μg/m3N) | Media trianual | 2,5 | 2,5 | 2,5 |

**Tabla 4-31.: Comparación de Monitoreo de NO** **2** **con Normativa. Estación Ferrocarril.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| NO2 | 1 de enero de 2017 -<br>31 de diciembre de 2019 | Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora | 39,4 | 400 | μg/m3N | 9,9% |
| NO2 | 1 de enero de 2017 -<br>31 de diciembre de 2019 | Concentración media<br>trianual | 2,5 | 100 | μg/m3N | 2,5% |

**Tabla 4-32: - Resultados Monitoreo de SO** **2** **. Estación Ferrocarril** **[18]** .**

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2017** | **2018** | **2019** |
| SO2 (μg/m3N) | Percentil 98,5 de concentración horaria | - | - | 8,4 |
| SO2 (μg/m3N) | Promedio trianual percentil 98,5 de<br>concentración horaria | 8,4 | 8,4 | 8,4 |
| SO2 (μg/m3N) | Percentil 99 de concentración diaria | 6,0 | 5,5 | 7,5 |
| SO2 (μg/m3N) | Promedio trianual percentil 99 de<br>concentración diaria | 6,3 | 6,3 | 6,3 |

**Tabla 4-33: - Comparación de Monitoreo de SO** **2** **con Normativa. Estación Ferrocarril.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| SO2 | 1 de enero de 2017 -<br>31 de diciembre de 2019 | Percentil 98,5 de<br>concentración<br>horaria | 8,4 | 350 | μg/m3N | 2,4% |
| SO2 | 1 de enero de 2017 -<br>31 de diciembre de 2019 | Percentil 98 de la<br>concentración<br>media diaria | 6,3 | 150 | μg/m3N | 4,2% |
| SO2 | 1 de enero de 2017 -<br>31 de diciembre de 2019 | Concentración<br>media trianual | 1,8 | 60 | μg/m3N | 3,1% |

**Tabla 4-34.: Resultados Monitoreo de CO. Estación Ferrocarril** **[19]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2017** | **2018** | **2019** |
| CO (mg/m3N) | Percentil 99 de los máximos diarios de<br>concentración horaria | 0,4 | 0,3 | 0,4 |
| CO (mg/m3N) | Promedio trianual percentil 99 de los máximos<br>diarios de concentración horaria | 0,4 | 0,4 | 0,4 |
| CO (mg/m3N) | Percentil 99 de los máximos diarios de<br>concentración media móvil de 8 horas | 0,3 | 0,3 | 0,3 |
| CO (mg/m3N) | Promedio trianual percentil 99 de los máximos<br>diarios de concentración media móvil de 8 horas | 0,3 | 0,3 | 0,3 |

**Tabla 4-35.: Comparación de Monitoreo de CO con Normativa. Estación Ferrocarril.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| CO | 1 de enero de 2017 -<br>31 de diciembre de 2019 | Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora | 0,4 | 30 | mg/m3N | 1,2% |
| CO | 1 de enero de 2017 -<br>31 de diciembre de 2019 | Percentil 99 de los<br>máximos diarios de<br>concentración de 8 horas | 0,3 | 10 | mg/m3N | 3,0% |

**Tabla 4-36.: Resultados Monitoreo de O3. Estación Ferrocarril** **[20]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2017** | **2018** | **2019** |
| O3 (μg/m3N) | Percentil 99 de los máximos diarios de<br>concentración media móvil de 8 horas | 57,0 | 55,0 | 58,0 |
| O3 (μg/m3N) | Promedio trianual percentil 99 de los máximos<br>diarios de concentración media móvil de 8 horas | 56,7 | 56,7 | 56,7 |

**Tabla 4-37.: Comparación de Monitoreo de O** **3** **con Normativa. Estación Ferrocarril.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| O3 | 1 de enero de 2017 -<br>31 de diciembre de 2019 | Percentil 99 de los<br>máximos diarios de<br>concentración de 8 horas | 56,7 | 120 | μg/m3N | 47,2% |

**Tabla 4-38.: Resultados Monitoreo de MP10. Estación Angamos 1** **[21]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| MP10 (μg/m3N) | Percentil 98 diario | 23,7 | 29,2 | 39,6 |
| MP10 (μg/m3N) | Media anual | 13,0 | 15,0 | 23,8 |
| MP10 (μg/m3N) | Media trianual | 17,3 | 17,3 | 17,3 |

**Tabla 4-39.: Comparación de Monitoreo de MP10 con Normativa. Estación Angamos 1.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 1 de enero de 2021-<br>31 de diciembre de 202122 | Percentil 98 de la<br>concentración<br>media diaria | 39,6 | 130 | μg/m3N | 30,5% |
| MP10 | 1 de enero de 2019 -<br>31 de diciembre de 2021 | Concentración<br>media trianual | 17,3 | 50 | μg/m3N | 34,5% |

**Tabla 4-40.: Resultados Monitoreo de NO** **2** **. Estación Angamos 1** **[23]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| NO2 (μg/m3N) | Percentil 99 de los máximos diarios de<br>concentración horaria | 121,9 | 46,7 | 43,1 |
| NO2 (μg/m3N) | Promedio trianual percentil 99 de los<br>máximos diarios de concentración horaria | 70,6 | 70,6 | 70,6 |
| NO2 (μg/m3N) | Media anual | 12,2 | 8,4 | 6,7 |
| NO2 (μg/m3N) | Media trianual | 9,1 | 9,1 | 9,1 |

**Tabla 4-41.: Comparación de Monitoreo de NO** **2** **con Normativa. Estación Angamos 1.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| NO2 | 1 de enero de 2019 -<br>31 de diciembre de 2021 | Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora | 70,6 | 400 | μg/m3N | 17,7% |
| NO2 | 1 de enero de 2019 -<br>31 de diciembre de 2021 | Concentración media<br>trianual | 9,1 | 100 | μg/m3N | 9,1% |

**Tabla 4-42.: Resultados Monitoreo de SO** **2** **. Estación Angamos 1** **[24]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| SO2 (μg/m3N) | Percentil 98,5 de concentración horaria | 17,8 | 17,3 | 29,8 |
| SO2 (μg/m3N) | Promedio trianual percentil 98,5 de<br>concentración horaria | 21,6 | 21,6 | 21,6 |
| SO2 (μg/m3N) | Percentil 99 de concentración diaria | 12,8 | 16,0 | 22,5 |
| SO2 (μg/m3N) | Promedio trianual percentil 99 de<br>concentración diaria | 17,1 | 17,1 | 17,1 |
| SO2 (μg/m3N) | Media anual | 5,1 | 5,2 | 7,3 |
| SO2 (μg/m3N) | Media trianual | 5,9 | 5,9 | 5,9 |

**Tabla 4-43: - Comparación de Monitoreo de SO** **2** **con Normativa. Estación Angamos 1.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| SO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Percentil 98,5 de<br>concentración<br>horaria | 21,6 | 350 | μg/m3N | 6,2% |
| SO2 | 1 de enero de 2017 - 31<br>de diciembre de 2021 | Percentil 98 de la<br>concentración<br>media diaria | 17,1 | 150 | μg/m3N | 11,4% |
| SO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Concentración<br>media trianual | 5,9 | 60 | μg/m3N | 9,8% |

**Tabla 4-44.: Resultados Monitoreo MP2,5. Estación MOLYB** **[25]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| MP2,5 (μg/m3) | Percentil 98 diario | 24,0 | 18,0 | 23,0 |
| MP2,5 (μg/m3) | Media anual | 15,0 | 9,0 | 9,0 |
| MP2,5 (μg/m3) | Media trianual | 11,0 | 11,0 | 11,0 |

**Tabla 4-45.: Comparación de Monitoreo de MP2,5 con Normativa. Estación MOLYB.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP2,5 | 1 de enero de 2019-<br>31 de diciembre de 202126 | Percentil 98 de la<br>concentración<br>media diaria | 24,0 | 50 | μg/m3 | 48,0% |
| MP2,5 | 1 de enero de 2019 -<br>31 de diciembre de 2021 | Concentración<br>media trianual | 11,0 | 20 | μg/m3 | 55,0% |

**Tabla 4-46.: Resultados Monitoreo de MP10. Estación MOLYB** **[27]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| MP10 (μg/m3N) | Percentil 98 diario | 52,0 | 35,0 | 39,0 |
| MP10 (μg/m3N) | Media anual | 24,0 | 18,0 | 22,0 |
| MP10 (μg/m3N) | Media trianual | 21,3 | 21,3 | 21,3 |

**Tabla 4-47.: Comparación de Monitoreo de MP10 con Normativa. Estación MOLYB.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 1 de enero de 2019-<br>31 de diciembre de 202128 | Percentil 98 de la<br>concentración<br>media diaria | 52,0 | 130 | μg/m3N | 40,0% |
| MP10 | 1 de enero de 2018 -<br>31 de diciembre de 2021 | Concentración<br>media trianual | 21,3 | 50 | μg/m3N | 42,6% |

**Tabla 4-48.: Resultados Monitoreo de NO** **2** **. Estación MOLYB** **[29]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| NO2 (μg/m3N) | Percentil 99 de los máximos diarios de<br>concentración horaria | 50,3 | 52,0 | 56,3 |
| NO2 (μg/m3N) | Promedio trianual percentil 99 de los<br>máximos diarios de concentración horaria | 52,9 | 52,9 | 52,9 |
| NO2 (μg/m3N) | Media anual | 7,7 | 10,0 | 9,3 |
| NO2 (μg/m3N) | Media trianual | 9,0 | 9,0 | 9,0 |

**Tabla 4-49.: Comparación de Monitoreo de NO** **2** **con Normativa. Estación MOLYB.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| NO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora | 52,9 | 400 | μg/m3N | 13,2% |
| NO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Concentración media<br>trianual | 9,0 | 100 | μg/m3N | 9,0% |

**Tabla 4-50.: Resultados Monitoreo de SO** **2** **. Estación MOLYB** **[30]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2018** | **2019** | **2020** |
| SO2 (μg/m3N) | Percentil 98,5 de concentración<br>horaria | 209,6 | 196,4 | 309,8 |
| SO2 (μg/m3N) | Promedio trianual percentil 98,5 de<br>concentración horaria | 238,6 | 238,6 | 238,6 |
| SO2 (μg/m3N) | Percentil 99 de concentración diaria | 96,9 | 100,8 | 310 |
| SO2 (μg/m3N) | Promedio trianual percentil 99 de<br>concentración diaria | 169,2 | 169,2 | 169,2 |
| SO2 (μg/m3N) | Media anual | 23,4 | 24,2 | 43,6 |
| SO2 (μg/m3N) | Media trianual | 30,4 | 30,4 | 30,4 |

**Tabla 4-51: - Comparación de Monitoreo de SO** **2** **con Normativa. Estación MOLYB** .**

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| SO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Percentil 98,5 de<br>concentración<br>horaria | 238,6 | 350 | μg/m3N | 68,2% |
| SO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Percentil 98 de la<br>concentración media<br>diaria | 169,2 | 150 | μg/m3N | 112,8% |
| SO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Concentración media<br>trianual | 30,4 | 60 | μg/m3N | 50,6% |

**Tabla 4-52.: Resultados Monitoreo de MP10. Estación MOLYNOR** **[31]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2018** | **2019** | **2020** |
| MP10 (μg/m3N) | Percentil 98 diario | 75,0 | 48,0 | 61,0 |
| MP10 (μg/m3N) | Media trianual | 30,0 | 30,0 | 30,0 |

**Tabla 4-53.: Comparación de Monitoreo de MP10 con Normativa. Estación MOLYNOR.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 1 de enero de 2019 -<br>31 de diciembre de 202132 | Percentil 98 de la<br>concentración<br>media diaria | 75,0 | 130 | μg/m3N | 57,8% |
| MP10 | 1 de enero de 2019 -<br>31 de diciembre de 2021 | Concentración<br>media trianual | 30,0 | 50 | μg/m3N | 60,0% |

**Tabla 4-54.: Resultados Monitoreo de NO** **2** **. Estación MOLYNOR** **[33]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| NO2 (μg/m3N) | Percentil 99 de los máximos diarios de<br>concentración horaria | 41,8 | 35,5 | 90,1 |
| NO2 (μg/m3N) | Promedio trianual percentil 99 de los<br>máximos diarios de concentración horaria | 39,3 | 39,3 | 39,3 |

**Tabla 4-55.: Comparación de Monitoreo de NO** **2** **con Normativa. Estación MOLYNOR.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| NO2 | 1 de enero de 2019 -<br>31 de diciembre de 2021 | Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora | 39,3 | 400 | μg/m3N | 9,8% |
| NO2 | 1 de enero de 2019 -<br>31 de diciembre de 2021 | Concentración media<br>trianual | 6,5 | 100 | μg/m3N | 6,5% |

**Tabla 4-56.: Resultados Monitoreo de SO** **2** **. Estación MOLYNOR** **[34]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| SO2 (μg/m3N) | Percentil 98,5 de concentración<br>horaria | 64,1 | 47,4 | 44,8 |
| SO2 (μg/m3N) | Promedio trianual percentil 98,5 de<br>concentración horaria | 52,1 | 52,1 | 52,1 |
| SO2 (μg/m3N) | Percentil 99 de concentración diaria | 50,5 | 36,6 | 106,6 |
| SO2 (μg/m3N) | Promedio trianual percentil 99 de<br>concentración diaria | 64,6 | 64,6 | 64,6 |
| SO2 (μg/m3N) | Media anual | 6,7 | 7,5 | 12,1 |
| SO2 (μg/m3N) | Media trianual | 8,8 | 8,8 | 8,8 |

**Tabla 4-57: - Comparación de Monitoreo de SO** **2** **con Normativa. Estación MOLYNOR.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| SO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Percentil 98,5 de<br>concentración<br>horaria | 64,6 | 350 | μg/m3N | 18,5% |
| SO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Percentil 98 de la<br>concentración<br>media diaria | 52,1 | 150 | μg/m3N | 34,7% |
| SO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Concentración<br>media trianual | 8,8 | 60 | μg/m3N | 14,6% |

**Tabla 4-58.: Resultados Monitoreo de MP10. Estación Subestación Eléctrica** **[35]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| MP10 (μg/m3N) | Percentil 98 diario | 35,0 | 81,0 | 35,0 |
| MP10 (μg/m3N) | Media anual | 19,0 | 27,0 | 17,0 |
| MP10 (μg/m3N) | Media trianual | 21,0 | 21,0 | 21,0 |

**Tabla 4-59.: Comparación de Monitoreo de MP10. Estación Subestación Eléctrica.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 1 de enero de 2019-<br>31 de diciembre de 202136 | Percentil 98 de la<br>concentración media diaria | 81,0 | 130 | μg/m3N | 62,3% |
| MP10 | 1 de enero de 2019 -<br>31 de diciembre de 2021 | Concentración media<br>trianual | 21,0 | 50 | μg/m3N | 42,0% |

**Tabla 4-60.: Resultados Monitoreo de NO** **2** **. Estación Subestación Eléctrica** **[37]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| NO2 (μg/m3N) | Percentil 99 de los máximos diarios de<br>concentración horaria | 51,8 | 57,0 | 57,0 |
| NO2 (μg/m3N) | Promedio trianual percentil 99 de los<br>máximos diarios de concentración horaria | 55,3 | 55,3 | 55,3 |
| NO2 (μg/m3N) | Media anual | 5,7 | 6,0 | 6,2 |
| NO2 (μg/m3N) | Media trianual | 6,0 | 6,0 | 6,0 |

**Tabla 4-61.: Comparación de Monitoreo de NO** **2** **con Normativa. Estación Subestación Eléctrica.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| NO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora | 55,3 | 400 | μg/m3N | 13,8% |

**Tabla 4-62.: Resultados Monitoreo de SO2. Estación Subestación Eléctrica** **[38]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2019** | **2020** | **2021** |
| SO2 (μg/m3N) | Percentil 98,5 de concentración horaria | 22,2 | 19,9 | 28,3 |
| SO2 (μg/m3N) | Promedio trianual percentil 98,5 de<br>concentración horaria | 23,5 | 23,5 | 23,5 |
| SO2 (μg/m3N) | Percentil 99 de concentración diaria | 14,3 | 14,4 | 18,9 |
| SO2 (μg/m3N) | Promedio trianual percentil 99 de<br>concentración diaria | 15,9 | 15,9 | 15,9 |
| SO2 (μg/m3N) | Media anual | 4,7 | 4,7 | 4,3 |
| SO2 (μg/m3N) | Media trianual | 4,6 | 4,6 | 4,6 |

**Tabla 4-63.: Comparación de Monitoreo de SO** **2** **con Normativa. Estación Subestación Eléctrica.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| SO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Percentil 98,5 de<br>concentración<br>horaria | 21,1 | 350 | μg/m3N | 6,0% |
| SO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Percentil 98 de la<br>concentración<br>media diaria | 12,9 | 150 | μg/m3N | 8,6% |
| SO2 | 1 de enero de 2019 - 31<br>de diciembre de 2021 | Concentración<br>media trianual | 4,4 | 60 | μg/m3N | 7,4% |

**Tabla 4-64.: Resumen Línea de Base de Calidad del Aire.****

| Contaminante | Estadígrafo | Norma | Unidad | JJ Latorre | Col6 | Jardín Infantil | Col8 | Puerto Mejillones | Col10 | Ferrocarril | Col12 | Angamos 1 | Col14 | MOLYB | Col16 | MOLYNOR | Col18 | Subestación<br>Eléctrica | Col20 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadígrafo** | **Norma** | **Unidad** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** |
| MP2,5 | P98 24 hrs | 50 | μg/m3 |  |  |  |  |  |  | 23,00 | 46,00% |  |  | 24,00 | 48,00% |  |  |  |  |
| MP2,5 | Anual | 20 | μg/m3 |  |  |  |  |  |  | 9,00 | 45,00% |  |  | 11,00 | 55,00% |  |  |  |  |
| MP10 | P98 24 hrs | 130 | μg/m3N | 35,00 | 26,92% | 32,00 | 24,62% | 34,00 | 26,15% | 41,00 | 31,54% | 39,60 | 30,46% | 52,00 | 40,00% | 75,00 | 57,69% | 81,00 | 62,31% |
| MP10 | Anual | 50 | μg/m3N | 20,20 | 40,40% | 20,40 | 40,80% | 20,00 | 40,00% | 15,70 | 31,40% | 17,30 | 34,60% | 21,30 | 42,60% | 30,00 | 60,00% | 21,00 | 42,00% |
| NO2 | P99 1hr | 400 | μg/m3N | 43,20 | 10,80% | 53,00 | 13,25% |  |  | 39,40 | 9,85% | 70,60 | 17,65% | 52,90 | 13,23% | 39,30 | 9,83% | 55,30 | 13,83% |
| NO2 | Anual | 100 | μg/m3N | 4,60 | 4,60% | 7,00 | 7,00% |  |  | 2,50 | 2,50% | 9,10 | 9,10% | 9,00 | 9,00% | 6,50 | 6,50% | 6,00 | 6,00% |
| SO2 | P98,5 1hr | 350 | μg/m3N |  |  |  |  |  |  | 8,40 | 2,40% | 21,60 | 6,17% | 238,60 | 68,17% | 64,60 | 18,46% | 21,10 | 6,03% |
| SO2 | P99 24 hrs | 150 | μg/m3N |  |  |  |  |  |  | 6,30 | 4,20% | 17,10 | 11,40% | 169,20 | 112,80<br>% | 52,10 | 34,73% | 12,90 | 8,60% |
| SO2 | Anual | 60 | μg/m3N |  |  |  |  |  |  | 1,80 | 3,00% | 5,90 | 9,83% | 30,40 | 50,67% | 8,80 | 14,67% | 4,40 | 7,33% |
| CO | P99 1 hr | 30 | mg/m3N |  |  |  |  |  |  | 0,40 | 1,33% |  |  |  |  |  |  |  |  |
| CO | P99 8 hrs | 10 | mg/m3N |  |  |  |  |  |  | 0,30 | 3,00% |  |  |  |  |  |  |  |  |
| O3 | P99 | 120 | μg/m3N |  |  |  |  |  |  | 56,70 | 47,25% |  |  |  |  |  |  |  |  |

**Tabla 4-65.: Proyectos aprobados en el Sector de Mejillones y Alrededores.****

| Proyecto | RCA | Fase según SNIFA |
| --- | --- | --- |
| Ampliación Plantas de Ácido Nítrico y Nitrato de Amonio | 102/2016 | En fase de operación |
| Planta Fotovoltaica AR Changos Solar | 221/2021 | No iniciada la fase de construcción |
| Centro de Almacenamiento de Peróxido de Hidrógeno<br>Mejillones | 152/2021 | No iniciada la fase de construcción |
| Central Termoeléctrica Ttanti | 013/2018 | No iniciada la fase de construcción |
| Planta desalinizadora y suministro de agua industrial | 217/2017 | Iniciada la fase de construcción |
| Ampliación Planta Mejillones | 013/2017 | No iniciada la fase de construcción |
| Modificación Sistema Eléctrico y trazado Tubería Proyecto<br>Algorta | 454/2017 | No iniciada la fase de construcción |
| Modificación del Transporte Terrestre de Sustancias Corrosivas<br>en Región de Atacama | 661/2017 | En fase de operación |
| Terminal de Graneles en Complejo Portuario Mejillones | 369/2017 | Sin información |
| Proyecto Terminar para Carga y Descarga de Combustibles<br>Mejillones | 46/2018 | No iniciada la fase de construcción |
| Línea de Alta Tensión 2x200 kV, Los Changos-Kimal | 440/2017 | En fase de operación |
| Ampliación Terminal Marítimo Mejillones | 474/2017 | En fase de operación |
| Autogeneración eléctrica Terminal GNL Mejillones | 8/2018 | En fase de operación |
| Conexión Unidades CTM-2 y CTM-3 a GIS en S/E Chacaya | 27/2018 | En fase de operación |
| Transporte de ácido sulfúrico hacia Minera Antucoya desde<br>puntos de despacho de la Región de Antofagasta | 174/2018 | Sin información |
| Transporte de ácido sulfúrico hacia Minera Spence desde<br>puntos de despacho de la Región de Antofagasta | 170/2018 | Sin información |
| Marimaca | 129/2018 | Sin información |

**Tabla 4-66.: Aportes Declarados por Proyectos Aprobados, No Ejecutados.****

| Contaminante | Estadígrafo | Norma | Unidad | JJ Latorre | Col6 | Jardín Infantil | Col8 | Ferrocarril | Col10 | MOLYNOR | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadígrafo** | **Norma** | **Unidad** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** |
| MP2,5 | P98 24 hrs | 50 | μg/m3 | 0,19 | 0,38% | 0,20 | 0,40% | 0,12 | 0,24% | 6,35 | 12,70% |
| MP2,5 | Anual | 20 | μg/m3 | 0,03 | 0,15% | 0,03 | 0,15% | 0,02 | 0,10% | 1,36 | 6,80% |
| MP10 | P98 24 hrs | 150 | μg/m3N | 1,41 | 0,94% | 1,37 | 0,91% | 0,27 | 0,18% | 6,35 | 4,23% |
| MP10 | Anual | 50 | μg/m3N | 0,08 | 0,16% | 0,07 | 0,14% | 0,05 | 0,10% | 1,36 | 2,72% |
| NO2 | P99 1hr | 400 | μg/m3N | 232,82 | 58,21% | 179,09 | 44,77% | 18,89 | 4,72% |  |  |
| NO2 | Anual | 100 | μg/m3N | 3,34 | 3,34% | 2,93 | 2,93% | 0,10 | 0,10% |  |  |
| SO2 | P98,5 1hr | 350 | μg/m3N | 0,00 | 0,00% | 0,00 | 0,00% | 0,00 | 0,00% |  |  |
| SO2 | P99 24 hrs | 150 | μg/m3N | 0,18 | 0,12% | 0,16 | 0,11% | 0,72 | 0,48% |  |  |
| SO2 | Anual | 60 | μg/m3N | 0,02 | 0,03% | 0,02 | 0,03% | 0,13 | 0,22% |  |  |
| CO | P99 1 hr | 30 | mg/m3N | 3,73 | 12,43% | 3,60 | 12,00% | 2,05 | 6,83% |  |  |
| CO | P99 8 hrs | 10 | mg/m3N | 1,61 | 16,10% | 1,52 | 15,20% | 1,39 | 13,90% |  |  |

**Tabla 4-67.: Línea de Base Proyectada.****

| Contaminante | Estadígrafo | Norma | Unidad | JJ Latorre | Col6 | Jardín Infantil | Col8 | Puerto Mejillones | Col10 | Ferrocarril | Col12 | Angamos 1 | Col14 | MOLYB | Col16 | MOLYNOR | Col18 | Subestación Eléctrica | Col20 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadígrafo** | **Norma** | **Unidad** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** |
| MP2,5 | P98 24 hrs | 50 | μg/m3 |  |  |  |  |  |  | 23,12 | 46,24% |  |  | 24,00 | 48,00% |  |  |  |  |
| MP2,5 | Anual | 20 | μg/m3 |  |  |  |  |  |  | 9,02 | 45,10% |  |  | 11,00 | 55,00% |  |  |  |  |
| MP10 | P98 24 hrs | 150 | μg/m3N | 36,41 | 28,01% | 33,37 | 25,67% | 34,00 | 26,15% | 41,27 | 31,75% | 39,60 | 30,46% | 52,00 | 40,00% | 81,35 | 62,58% | 81,00 | 62,31% |
| MP10 | Anual | 50 | μg/m3N | 20,28 | 40,56% | 20,47 | 40,94% | 20,00 | 40,00% | 15,75 | 31,50% | 17,30 | 34,60% | 21,30 | 42,60% | 31,36 | 62,72% | 21,00 | 42,00% |
| NO2 | P99 1hr | 400 | μg/m3N | 276,02 | 69,01% | 232,09 | 58,02% |  |  | 58,29 | 14,57% | 70,60 | 17,65% | 52,90 | 13,23% | 38,70 | 9,68% | 55,30 | 13,83% |
| NO2 | Anual | 100 | μg/m3N | 7,94 | 7,94% | 9,93 | 9,93% |  |  | 2,60 | 2,60% | 9,10 | 9,10% | 9,00 | 9,00% | 5,60 | 5,60% | 6,00 | 6,00% |
| SO2 | P98,5 1hr | 350 | μg/m3N |  |  |  |  |  |  | 8,40 | 2,40% | 21,60 | 6,17% | 238,60 | 68,17% | 55,80 | 15,94% | 21,10 | 6,03% |
| SO2 | P99 24 hrs | 150 | μg/m3N |  |  |  |  |  |  | 7,02 | 4,68% | 17,10 | 11,40% | 169,20 | 112,80% | 35,70 | 23,80% | 12,90 | 8,60% |
| SO2 | Anual | 60 | μg/m3N |  |  |  |  |  |  | 1,93 | 3,22% | 5,90 | 9,83% | 30,40 | 50,67% | 6,80 | 11,33% | 4,40 | 7,33% |
| CO | P99 1 hr | 30 | mg/m3N |  |  |  |  |  |  | 2,45 | 8,17% |  |  |  |  |  |  |  |  |
| CO | P99 8 hrs | 10 | mg/m3N |  |  |  |  |  |  | 1,69 | 16,90% |  |  |  |  |  |  |  |  |
| O3 | P99 | 120 | μg/m3N |  |  |  |  |  |  | 56,70 | 47,25% |  |  |  |  |  |  |  |  |

**Tabla 4-68.: Receptores Discretos en la Modelación.****

| ID Receptor | Descripción | Coordenadas de Ubicación (Datum WGS84) | Col4 | Elevación<br>(m.s.n.m)42 |
| --- | --- | --- | --- | --- |
| **ID Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Norte (m)** |
| R1 | JJ Latorre | 352.346 | 7.444.100 | 22,99 |
| R2 | Jardín Infantil | 352.064 | 7.444.407 | 15,73 |
| R3 | Puerto Mejillones | 352.047 | 7.444.688 | 9,21 |
| R4 | Ferrocarril | 350.017 | 7.444.552 | 15,30 |
| R5 | Angamos 1 | 357.839 | 7.446.453 | 36,89 |
| R6 | MOLYB | 358.938 | 7.447.360 | 38,55 |
| R7 | MOLYNOR | 358.945 | 7.448.107 | 19,94 |
| R8 | Subestación Eléctrica | 354.703 | 7.445.227 | 20,58 |
| R9 | Zona P1 (MPS y SO2 secundario) | 362.220 | 7.449.342 | 66,92 |
| R10 | Zona P2 (MPS y SO2 secundario) | 363.600 | 7.454.270 | 26,24 |
| R11 | Nido 1 (MPS y SO2 secundario) | 357.871 | 7.446.345 | 49,22 |
| R12 | Nido 2 (MPS y SO2 secundario) | 358.161 | 7.445.819 | 55,48 |

**Tabla 4-69.: Fuentes Emisoras - Fase de Cierre.****

| Tipo | ID | Descripción | Tasa de Emisión | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo** | **ID** | **Descripción** | **SO2 ** | **SO4 ** | **NO** | **NO2 ** | **HNO3 ** | **NO3 ** | **MP2.5** | **MP10** | **MPS** | **CO** | **Unidad** |
| Camino | SRC_2 | Tramo 2 | 5,22,E-07 | 0,00,E+00 | 6,96,E-06 | 1,19,E-06 | 0,00,E+00 | 0,00,E+00 | 9,59,E-07 | 3,17,E-06 | 1,55,E-05 | 3,06,E-06 | g/s/m |
| Camino | SRC_3 | Tramo 3 | 2,04,E-07 | 0,00,E+00 | 2,73,E-06 | 4,65,E-07 | 0,00,E+00 | 0,00,E+00 | 6,97,E-07 | 2,57,E-06 | 1,30,E-05 | 1,20,E-06 | g/s/m |
| Camino | SRC_4 | Tramo 4 | 1,06,E-08 | 0,00,E+00 | 1,42,E-07 | 2,41,E-08 | 0,00,E+00 | 0,00,E+00 | 3,49,E-08 | 1,28,E-07 | 6,45,E-07 | 6,38,E-08 | g/s/m |
| Camino | SRC_5 | Tramo 5 | 1,08,E-07 | 0,00,E+00 | 1,45,E-06 | 2,47,E-07 | 0,00,E+00 | 0,00,E+00 | 3,32,E-07 | 1,20,E-06 | 6,04,E-06 | 6,82,E-07 | g/s/m |
| Camino | SRC_6 | Tramo 6 | 3,13,E-09 | 0,00,E+00 | 4,18,E-08 | 7,12,E-09 | 0,00,E+00 | 0,00,E+00 | 4,60,E-08 | 1,63,E-07 | 8,14,E-07 | 1,61,E-08 | g/s/m |
| Camino | SRC_7 | Tramo 7 | 4,73,E-09 | 0,00,E+00 | 6,31,E-08 | 1,08,E-08 | 0,00,E+00 | 0,00,E+00 | 1,24,E-08 | 4,77,E-08 | 2,44,E-07 | 2,43,E-08 | g/s/m |
| Camino | SRC_8 | Tramo 8 | 3,10,E-09 | 0,00,E+00 | 4,14,E-08 | 7,05,E-09 | 0,00,E+00 | 0,00,E+00 | 2,15,E-08 | 8,27,E-08 | 4,23,E-07 | 1,59,E-08 | g/s/m |
| Área | SRC_1 | Área instalación | 1,92,E-07 | 0,00,E+00 | 1,20,E-06 | 2,04,E-07 | 0,00,E+00 | 0,00,E+00 | 2,73,E-07 | 3,69,E-07 | 1,26,E-06 | 4,45,E-07 | g/s/m2 |

**Tabla 4-70.: Resultados de modelo de dispersión de MP2.5. Fase de Cierre.****

| Receptor | Descripción | Material Particulado Respirable Fino (MP2,5) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración**<br>**[μg/m3N]** | **Concentración**<br>**[μg/m3N]** | **Norma de Calidad** | **Norma de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** |
| R1 | JJ Latorre | 1,70,E-03 | 1,94,E-04 | 50 | 20 | 0,00% | 0,00% |
| R2 | Jardín Infantil | 1,50,E-03 | 1,27,E-04 | 1,27,E-04 | 1,27,E-04 | 0,00% | 0,00% |
| R3 | Puerto Mejillones | 1,43,E-03 | 1,28,E-04 | 1,28,E-04 | 1,28,E-04 | 0,00% | 0,00% |
| R4 | Ferrocarril | 8,19,E-04 | 6,10,E-05 | 6,10,E-05 | 6,10,E-05 | 0,00% | 0,00% |
| R5 | Angamos 1 | 1,47,E-01 | 1,37,E-02 | 1,37,E-02 | 1,37,E-02 | 0,29% | 0,07% |
| R6 | MOLYB | 1,19,E-01 | 1,79,E-02 | 1,79,E-02 | 1,79,E-02 | 0,24% | 0,09% |
| R7 | MOLYNOR | 6,65,E-02 | 9,74,E-03 | 9,74,E-03 | 9,74,E-03 | 0,13% | 0,05% |
| R8 | Subestación Eléctrica | 3,42,E-03 | 4,56,E-04 | 4,56,E-04 | 4,56,E-04 | 0,01% | 0,00% |

**Tabla 4-71.: Resultados de modelo de dispersión de MP10. Fase de Cierre.****

| Receptor | Descripción | Material Particulado Respirable (MP10) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración**<br>**[μg/m3N]** | **Concentración**<br>**[μg/m3N]** | **Norma de Calidad** | **Norma de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** |
| R1 | JJ Latorre | 2,94,E-03 | 4,26,E-04 | 130 | 50 | 0,00% | 0,00% |
| R2 | Jardín Infantil | 1,98,E-03 | 2,09,E-04 | 2,09,E-04 | 2,09,E-04 | 0,00% | 0,00% |
| R3 | Puerto Mejillones | 2,55,E-03 | 2,10,E-04 | 2,10,E-04 | 2,10,E-04 | 0,00% | 0,00% |
| R4 | Ferrocarril | 1,12,E-03 | 8,82,E-05 | 8,82,E-05 | 8,82,E-05 | 0,00% | 0,00% |
| R5 | Angamos 1 | 1,97,E-01 | 1,83,E-02 | 1,83,E-02 | 1,83,E-02 | 0,15% | 0,04% |
| R6 | MOLYB | 1,60,E-01 | 2,45,E-02 | 2,45,E-02 | 2,45,E-02 | 0,12% | 0,05% |
| R7 | MOLYNOR | 8,74,E-02 | 1,33,E-02 | 1,33,E-02 | 1,33,E-02 | 0,07% | 0,03% |
| R8 | Subestación Eléctrica | 4,65,E-03 | 6,48,E-04 | 6,48,E-04 | 6,48,E-04 | 0,00% | 0,00% |

**Tabla 4-72.: Resultados de modelo de dispersión de NO** **2** **. Fase de Cierre.****

| Receptor | Descripción | Dióxido de Nitrógeno (NO )<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Norma de Calidad** | **Norma de Calidad** | **Porcentaje de la**<br>**Norma de Calidad** | **Porcentaje de la**<br>**Norma de Calidad** |
| **Receptor** | **Descripción** | **Percentil 99**<br>**1 hora** | **Período**<br>**Anual** | **Percentil**<br>**99 1 hora** | **Período**<br>**Anual** | **Percentil**<br>**99 1 hora** | **Período**<br>**Anual** |
| R1 | JJ Latorre | 0,224 | 0,001 | 400 | 100 | 0,06% | 0,00% |
| R2 | Jardín Infantil | 0,183 | 0,001 | 0,001 | 0,001 | 0,05% | 0,00% |
| R3 | Puerto Mejillones | 0,185 | 0,001 | 0,001 | 0,001 | 0,05% | 0,00% |
| R4 | Ferrocarril | 0,071 | 0,000 | 0,000 | 0,000 | 0,02% | 0,00% |
| R5 | Angamos 1 | 11,069 | 0,071 | 0,071 | 0,071 | 2,77% | 0,07% |
| R6 | MOLYB | 5,077 | 0,104 | 0,104 | 0,104 | 1,27% | 0,10% |
| R7 | MOLYNOR | 3,344 | 0,055 | 0,055 | 0,055 | 0,84% | 0,06% |
| R8 | Subestación Eléctrica | 0,391 | 0,002 | 0,002 | 0,002 | 0,10% | 0,00% |

**Tabla 4-73.: Resultados de modelo de dispersión de SO** **2** **. Fase de Cierre.****

| Receptor | Descripción | Dióxido de Azufre (SO )<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Norma de Calidad** | **Norma de Calidad** | **Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Percentil 98,5**<br>**1 hora** | **Percentil 99**<br>**24 horas** | **Período Anual** | **Percentil**<br>**98,5 1 hora** | **Percentil**<br>**99 24**<br>**horas** | **Período**<br>**Anual** | **Percentil**<br>**98,5 1 hora** | **Percentil**<br>**99 24**<br>**horas** | **Período**<br>**Anual** |
| R1 | JJ Latorre | 5,75,E-04 | 1,17,E-03 | 7,05,E-05 | 350 | 150 | 60 | 0,00% | 0,00% | 0,00% |
| R2 | Jardín Infantil | 4,13,E-04 | 1,02,E-03 | 4,62,E-05 | 4,62,E-05 | 4,62,E-05 | 4,62,E-05 | 0,00% | 0,00% | 0,00% |
| R3 | Puerto Mejillones | 4,06,E-04 | 1,03,E-03 | 4,52,E-05 | 4,52,E-05 | 4,52,E-05 | 4,52,E-05 | 0,00% | 0,00% | 0,00% |
| R4 | Ferrocarril | 1,77,E-04 | 4,25,E-04 | 1,90,E-05 | 1,90,E-05 | 1,90,E-05 | 1,90,E-05 | 0,00% | 0,00% | 0,00% |
| R5 | Angamos 1 | 9,50,E-02 | 1,04,E-01 | 8,19,E-03 | 8,19,E-03 | 8,19,E-03 | 8,19,E-03 | 0,03% | 0,07% | 0,01% |
| R6 | MOLYB | 2,30,E-01 | 8,03,E-02 | 1,02,E-02 | 1,02,E-02 | 1,02,E-02 | 1,02,E-02 | 0,07% | 0,05% | 0,02% |
| R7 | MOLYNOR | 1,21,E-01 | 4,19,E-02 | 5,27,E-03 | 5,27,E-03 | 5,27,E-03 | 5,27,E-03 | 0,03% | 0,03% | 0,01% |
| R8 | Subestación Eléctrica | 1,26,E-03 | 3,04,E-03 | 1,81,E-04 | 1,81,E-04 | 1,81,E-04 | 1,81,E-04 | 0,00% | 0,00% | 0,00% |

**Tabla 4-74.: Resultados de modelo de dispersión de SO** **2** **. Fase de Cierre.****

| Receptor | Descripción | Dióxido de Azufre (SO )<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Norma de Calidad** | **Norma de Calidad** | **Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Percentil**<br>**99,73 hora** | **Percentil 99,7**<br>**24 horas** | **Período Anual** | **Percentil**<br>**98,73 1**<br>**hora** | **Percentil**<br>**99,7 24**<br>**horas** | **Período**<br>**Anual** | **Percentil**<br>**99,73 hora** | **Percentil**<br>**99,7 24**<br>**horas** | **Período**<br>**Anual** |
| R9 | MPS 1 | 1,39,E-02 | 2,87,E-03 | 3,93,E-04 | 1000 | 365 | 80 | 0,00% | 0,00% | 0,00% |
| R10 | MPS 2 | 1,18,E-02 | 2,19,E-03 | 2,86,E-04 | 2,86,E-04 | 2,86,E-04 | 2,86,E-04 | 0,00% | 0,00% | 0,00% |
| R11 | Nido 1 | 5,53,E+00 | 1,11,E+00 | 1,52,E-01 | 1,52,E-01 | 1,52,E-01 | 1,52,E-01 | 0,55% | 0,30% | 0,19% |
| R12 | Nido 2 | 1,80,E+00 | 5,24,E-01 | 8,97,E-02 | 8,97,E-02 | 8,97,E-02 | 8,97,E-02 | 0,18% | 0,14% | 0,11% |

**Tabla 4-75.: Resultados de modelo de dispersión de CO. Fase de Cierre.****

| Receptor | Descripción | Monóxido de Carbono (CO) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [mg/m3] ** | **Concentración [mg/m3] ** | **Norma de Calidad** | **Norma de Calidad** | **Porcentaje de la**<br>**Norma de Calidad** | **Porcentaje de la**<br>**Norma de Calidad** |
| **Receptor** | **Descripción** | **Percentil 99 1**<br>**hora** | **Percentil 99 8**<br>**horas** | **Percentil**<br>**99 1 hora** | **Percentil**<br>**99 8**<br>**horas** | **Percentil**<br>**99 1 hora** | **Percentil**<br>**99 8**<br>**horas** |
| R1 | JJ Latorre | 5,95E-05 | 9,41E-06 | 30 | 10 | 0,00% | 0,00% |
| R2 | Jardín Infantil | 5,63E-05 | 8,39E-06 | 8,39E-06 | 8,39E-06 | 0,00% | 0,00% |
| R3 | Puerto Mejillones | 5,12E-05 | 7,88E-06 | 7,88E-06 | 7,88E-06 | 0,00% | 0,00% |
| R4 | Ferrocarril | 1,93E-05 | 2,88E-06 | 2,88E-06 | 2,88E-06 | 0,00% | 0,00% |
| R5 | Angamos 1 | 4,43E-03 | 5,93E-04 | 5,93E-04 | 5,93E-04 | 0,01% | 0,01% |
| R6 | MOLYB | 1,32E-03 | 2,97E-04 | 2,97E-04 | 2,97E-04 | 0,00% | 0,00% |
| R7 | MOLYNOR | 8,97E-04 | 1,54E-04 | 1,54E-04 | 1,54E-04 | 0,00% | 0,00% |
| R8 | Subestación Eléctrica | 9,76E-05 | 1,59E-05 | 1,59E-05 | 1,59E-05 | 0,00% | 0,00% |

**Tabla 4-76.: Resultados de modelo de dispersión de MPS. Fase de Cierre.****

| Receptor | Descripción | Material Particulado Sedimentable (MPS) | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Tasa de**<br>**depositación**<br>**[mg/m2-día]** | **Norma Periodo**<br>**Anual** | **Porcentaje de la**<br>**Norma de**<br>**Referencia** |
| R9 | MPS 1 | 8,79E-04 | 200 | 0,00% |
| R10 | MPS 2 | 3,73E-04 | 3,73E-04 | 0,00% |
| R11 | Nido 1 | 7,46E-01 | 7,46E-01 | 0,37% |
| R12 | Nido 2 | 4,38E-01 | 4,38E-01 | 0,22% |

**Tabla 4-77: - Concentración Total Esperada. Fase de Cierre.****

| Contaminante | Estadígrafo | Norma | Unidad | JJ Latorre | Col6 | Jardín Infantil | Col8 | Puerto Mejillones | Col10 | Ferrocarril | Col12 | Angamos 1 | Col14 | MOLYB | Col16 | MOLYNOR | Col18 | Subestación Eléctrica | Col20 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadígrafo** | **Norma** | **Unidad** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** | **Valor** | **Norma** |
| MP2,5 | P98 24 hrs | 50 | μg/m3 |  |  |  |  |  |  | 23,1 | 46,2% |  |  | 24,0 | 48,0% |  |  |  |  |
| MP2,5 | Anual | 20 | μg/m3 |  |  |  |  |  |  | 9,0 | 45,1% |  |  | 11,0 | 55,0% |  |  |  |  |
| MP10 | P98 24 hrs | 130 | μg/m3N | 36,4 | 28,0% | 33,4 | 25,7% | 34,0 | 26,2% | 41,3 | 31,7% | 39,8 | 30,6% | 52,2 | 40,1% | 81,4 | 62,6% | 81,0 | 62,3% |
| MP10 | Anual | 50 | μg/m3N | 20,3 | 40,6% | 20,5 | 40,9% | 20,0 | 40,0% | 15,8 | 31,5% | 17,3 | 34,6% | 21,3 | 42,6% | 31,4 | 62,7% | 21,0 | 42,0% |
| NO2 | P99 1hr | 400 | μg/m3N | 276,2 | 69,1% | 232,3 | 58,1% |  |  | 58,4 | 14,6% | 81,7 | 20,4% | 58,0 | 14,5% | 42,0 | 10,5% | 55,7 | 13,9% |
| NO2 | Anual | 100 | μg/m3N | 7,9 | 7,9% | 9,9 | 9,9% |  |  | 2,6 | 2,6% | 9,2 | 9,2% | 9,1 | 9,1% | 5,7 | 5,7% | 6,0 | 6,0% |
| SO2 | P98,5 1hr | 350 | μg/m3N |  |  |  |  |  |  | 8,4 | 2,4% | 21,7 | 6,2% | 238,8 | 68,2% | 55,9 | 16,0% | 21,1 | 6,0% |
| SO2 | P99 24 hrs | 150 | μg/m3N |  |  |  |  |  |  | 7,0 | 4,7% | 17,2 | 11,5% | 169,3 | 112,9% | 35,7 | 23,8% | 12,9 | 8,6% |
| SO2 | Anual | 60 | μg/m3N |  |  |  |  |  |  | 1,9 | 3,2% | 5,9 | 9,8% | 30,4 | 50,7% | 6,8 | 11,3% | 4,4 | 7,3% |
| CO | P99 1 hr | 30 | mg/m3N |  |  |  |  |  |  | 2,5 | 8,2% |  |  |  |  |  |  |  |  |
| CO | P99 8 hrs | 10 | mg/m3N |  |  |  |  |  |  | 1,69 | 16,9% |  |  |  |  |  |  |  |  |

**Tabla 6-1.: Archivos de modelación entregados.****

| Archivos | Entregado | Observación |
| --- | --- | --- |
| **Archivos CALPUFF:** | **Archivos CALPUFF:** | **Archivos CALPUFF:** |
| - CALPUFF.DAT | NO | Corresponde al archivo CONC.DAT |
| - CALPUFF.LST | SI | - |
| - CALPUFF.INP | SI | - |
| - CONC.DAT | SI | - |
| - DFLX.DAT | SI | - |
| - WFLX.DAT | NO | - |
| **Archivos Meteorológicos:** | **Archivos Meteorológicos:** | **Archivos Meteorológicos:** |
| - CALMET.DAT | SI | - Corresponde al archivo:<br>calmetv6_Mejillones.dat |
| - GEO.DAT | SI | - |
| - SURF.DAT | NO | No fueron utilizados debido a que se usó, directamente<br>en CALPUFF, la meteorología proveniente del modelo<br>meteorológico WRF. |
| - UP.DAT | NO | NO |
| - CALMET.LST | NO | NO |
| - CALMET.INP | NO | NO |
| - namelist.wpl | SI | Archivo de configuración de preproceso de WRF (WPS) |
| - namelist.input | SI | Archivo de configuración de WRF |
| **Archivos CALPOST:** | **Archivos CALPOST:** | **Archivos CALPOST:** |
| - CALPOST.DAT | SI | Los archivos se presentan en forma separada según<br>contaminantes y periodo. |
| - CALPOST.LST | SI | SI |
