---
title: Sin título
author: Antonia Barrientos
date: D:20250227111001-03'00'
language: es
type: report
pages: 73
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO Modelación atmosférica ADENDA PROYECTO “ Parque Las Alamedas I, II y III ”
  - ÍNDICE DE CONTENIDOS
  - ÍNDICE DE TABLAS
  - ÍNDICE DE FIGURAS
  - 1. Introducción
  - 2. Antecedentes generales del proyecto
  - 3. Objetivos
  - 4. Normativa Calidad de Aire
  - 5. Justificación de los modelos utilizados
  - 6. Metodología
  ... y 3 secciones más
-->

# ANEXO Modelación atmosférica ADENDA PROYECTO “ Parque Las Alamedas I, II y III ”

FEBERO, 2025

# ÍNDICE DE CONTENIDOS

**1. INTRODUCCIÓN ...................................................................................................................................... 5**

**2. ANTECEDENTES GENERALES DEL PROYECTO .......................................................................................... 5**
**2.1.1.** **DESCRIPCIÓN ................................................................................................................................. 5**
**2.1.2.** **LOCALIZACIÓN ................................................................................................................................ 6**

**3. OBJETIVOS .............................................................................................................................................. 7**

**3.1.** **OBJETIVO GENERAL ......................................................................................................................... 7**
**3.2.** **OBJETIVOS ESPECÍFICOS ................................................................................................................. 7**

**4. NORMATIVA CALIDAD DE AIRE ................................................................................................................. 8**

**4.1.** **MATERIAL PARTICULADO (MP10 Y MP2,5) ......................................................................................... 8**
**4.2.** **DIÓXIDO DE AZUFRE (SO2) ............................................................................................................... 9**
**4.3.** **DIÓXIDO DE NITRÓGENO (NO2) ..................................................................................................... 10**
**4.4.** **MONÓXIDO DE CARBONO (CO) ...................................................................................................... 11**
**5. JUSTIFICACIÓN DE LOS MODELOS UTILIZADOS ..................................................................................... 13**

**5.1.** **USO DEL MODELO CALPUFF ........................................................................................................... 13**
**5.2.** **ECUACIÓN DEL MODELO CALPUFF ................................................................................................. 13**

**5.3.** **USO DEL MODELO WRF .................................................................................................................. 14**
**6. METODOLOGÍA ..................................................................................................................................... 14**
**6.1.** **MODELACIÓN METEOROLÓGICA .................................................................................................... 14**
**6.2.** **MODELACIÓN CALPUFF ................................................................................................................. 15**

**6.3.** **RECEPTORES DISCRETOS .............................................................................................................. 15**
**6.4.** **FUENTES DE EMISIÓN .................................................................................................................... 18**
**6.5.** **ANÁLISIS DE INCERTIDUMBRE ....................................................................................................... 20**
**6.5.1.** **MODELO METEOROLÓGICO ........................................................................................................... 20**
**6.5.2.** **ANÁLISIS CUALITATIVO .................................................................................................................. 21**
**6.5.3.** **ANÁLISIS CUANTITATIVO ................................................................................................................ 51**
**6.6.** **TOPOGRAFÍA.................................................................................................................................. 53**
**6.7.** **CARACTERIZACIÓN AMBIENTAL DEL PROYECTO ............................................................................. 54**

**6.7.1.** **MATERIAL PARTICULADO RESPIRABLE (MP10) ................................................................................ 54**
**6.7.2.** **MATERIAL PARTICULADO RESPIRABLE FINO (MP2,5) ...................................................................... 56**
**6.7.3.** **DIÓXIDO DE AZUFRE (SO2) ............................................................................................................. 57**
**6.7.4.** **ÓXIDOS DE NITRÓGENO (NOX) ....................................................................................................... 57**
**6.7.5.** **MONÓXIDO DE CARBONO (CO) ...................................................................................................... 57**

**7. RESULTADOS ........................................................................................................................................ 58**
**7.1.** **ISOCONCENTRACIÓN .................................................................................................................... 58**

**7.2.** **APORTE DEL PROYECTO ................................................................................................................. 64**
**7.3.** **EVALUACIÓN DEL IMPACTO DE LAS EMISIONES ATMOSFÉRICAS DEL MATERIAL PARTICULADO MP10**

**Y MP2,5 EN ZONAS SATURADAS ............................................................................................................ 65**
**7.4.** **EVALUACIÓN DEL EFECTO SINÉRGICO ........................................................................................... 67**
**7.5.** **EVALUACIÓN DE LOS NIVELES DE CONCENTRACIÓN ..................................................................... 68**
**7.6.** **ÁREA DE INFLUENCIA ..................................................................................................................... 71**

**8. CONSIDERACIONES .............................................................................................................................. 71**

**9. CONCLUSIONES ................................................................................................................................... 72**

# ÍNDICE DE TABLAS

**T** **ABLA** **1.** **L** **ÍMITES ANUAL Y DIARIO** **MP** **10** **Y** **MP** **2,5** ...................................................................................................................... 8
**T** **ABLA** **2.** **L** **ÍMITES ANUAL Y DIARIO** **SO** **2** .................................................................................................................................... 9
**T** **ABLA** **3.** **L** **ÍMITES ANUAL Y DIARIO DE** **NO** **2** ............................................................................................................................. 10

**T** **ABLA** **4.** **L** **ÍMITES ANUAL Y DIARIO DE** **CO** .............................................................................................................................. 11

**T** **ABLA** **5.** **R** **ECEPTORES DISCRETOS EN EL ÁREA DEL** **P** **ROYECTO** ............................................................................................. 16

**T** **ABLA** **6.** **FOTOGRAFÍAS REFERENCIALES DE RECEPTORES** ...................................................................................................... 16

**T** **ABLA** **7.** **F** **UENTES DE EMISIÓN DEL** **P** **ROYECTO** ...................................................................................................................... 18

Página **2** de **73**

**T** **ABLA** **8.** **P** **ARÁMETROS DE ENTRADA AL MODELO** ................................................................................................................... 19

**T** **ABLA** **9.** **E** **STACIÓN UTILIZADA PARA LA VALIDACIÓN DEL MODELO** **WRF** ................................................................................. 20
**T** **ABLA** **10.** **E** **STADÍSTICOS DE SESGO** **,** **ERROR ABSOLUTO MEDIO Y ERROR CUADRÁTICO MEDIO** .................................................. 52
**T** **ABLA** **11.** **C** **ONCENTRACIÓN** **M** **EDIA** **A** **NUAL DE** **MP** **10** **(** **UG** **/** **M** **[3]** **N)** ............................................................................................... 55
**T** **ABLA** **12.** **P** **ERCENTIL** **98** **CONCENTRACIÓN** **24** **HORAS DE** **MP** **10** **(** **UG** **/** **M** **[3]** **N)** ............................................................................... 55
**T** **ABLA** **13.** **C** **ONCENTRACIÓN** **M** **EDIA** **A** **NUAL DE** **MP** **2,5** **(** **UG** **/** **M** **[3]** **N)** .............................................................................................. 57
**T** **ABLA** **14.** **P** **ERCENTIL** **98** **CONCENTRACIÓN** **24** **HORAS DE** **MP** **2,5** **(** **UG** **/** **M** **[3]** **N)** .............................................................................. 57
**T** **ABLA** **15.** **N** **ORMAS DE CALIDAD PRIMARIA** ............................................................................................................................. 58

**T** **ABLA** **16.** **A** **PORTES DEL** **P** **ROYECTO** **-** **CONCENTRACIONES MÁXIMAS REGISTRADAS DE** **MP** **10** .................................................. 64
**T** **ABLA** **17.** **A** **PORTES DEL** **P** **ROYECTO** **-** **CONCENTRACIONES MÁXIMAS REGISTRADAS DE** **MP** **2,5** .................................................. 64
**T** **ABLA** **18.** **A** **PORTES DEL** **P** **ROYECTO** **-** **CONCENTRACIONES MÁXIMAS REGISTRADAS DE** **NO** **X** ................................................... 65

**T** **ABLA** **19.** **A** **PORTES DEL** **P** **ROYECTO** **-** **CONCENTRACIONES MÁXIMAS REGISTRADAS DE** **CO** ..................................................... 65

**T** **ABLA** **20.** **A** **PORTES DEL** **P** **ROYECTO** **-** **CONCENTRACIONES MÁXIMAS REGISTRADAS DE** **SO** **2** .................................................... 65

**T** **ABLA** **21.** **R** **ESUMEN DE** **E** **MISIONES DEL** **P** **ROYECTO** .............................................................................................................. 66

**T** **ABLA** **22.** **C** **OMPARACIÓN DE LOS RESULTADOS DE LA MODELACIÓN EN RECEPTORES HUMANOS Y VALORES DE SIGNIFICANCIA DE**

**LA** **T** **ABLA** **2** **DE LA** **G** **UÍA** **,** **PARA EL PRIMER AÑO DEL** **P** **ROYECTO** ..................................................................................... 66
**T** **ABLA** **23.** **P** **ROYECTOS** **A** **PROBADOS O EN** **C** **ALIFICACIÓN** **A** **MBIENTAL EN LAS CERCANÍAS AL** **P** **ROYECTO** **P** **LANTA** **S** **OLAR** **E** **L**

**C** **ARDONAL** .................................................................................................................................................................. 67

**T** **ABLA** **24.** **E** **VALUACIÓN DE SOLAPAMIENTO FASE DE CONSTRUCCIÓN** ...................................................................................... 67

**T** **ABLA** **25.** **T** **ASAS DE EMISIÓN A CONSIDERAR PARA LA EVALUACIÓN DEL EFECTO SINÉRGICO** ................................................... 67

**T** **ABLA** **26.** **R** **ESULTADOS APORTE PROYECTOS CERCANOS EN RECEPTORES** ............................................................................. 68

**T** **ABLA** **27.** **C** **ONCENTRACIONES TOTALES DE** **MP** **10** .................................................................................................................. 69
**T** **ABLA** **28.** **C** **ONCENTRACIONES TOTALES DE** **MP** **2,5** ................................................................................................................. 69
**T** **ABLA** **29.** **C** **ONCENTRACIONES TOTALES DE** **NO** **X** ................................................................................................................... 69

**T** **ABLA** **30.** **C** **ONCENTRACIONES TOTALES DE** **CO** .................................................................................................................... 69

**T** **ABLA** **31.** **C** **ONCENTRACIONES TOTALES DE** **SO** **2** ................................................................................................................... 70

# ÍNDICE DE FIGURAS

**F** **IGURA** **1.** **U** **BICACIÓN Y VÉRTICES DEL** **P** **ROYECTO** **................................................................................................................... 7**

**F** **IGURA** **2.** **D** **OMINIO DE LA MODELACIÓN** **................................................................................................................................. 15**

**F** **IGURA** **3.** **U** **BICACIÓN DE RECEPTORES DISCRETOS** **................................................................................................................ 18**

**F** **IGURA** **4.** **F** **UENTES DE EMISIÓN DEL** **P** **ROYECTO** **..................................................................................................................... 19**

**F** **IGURA** **5.** **D** **ATOS VELOCIDAD DEL VIENTO** **WRF** **R** **ANCAGUA** **I ................................................................................................. 21**

**F** **IGURA** **6.** **D** **ATOS VELOCIDAD DEL VIENTO ESTACIÓN** **R** **ANCAGUA** **I .......................................................................................... 22**

**F** **IGURA** **7.** **D** **ATOS VELOCIDAD DEL VIENTO** **WRF** **R** **ANCAGUA** **II ................................................................................................ 22**

**F** **IGURA** **8.** **D** **ATOS VELOCIDAD DE VIENTO OBSERVADA EN ESTACIÓN** **R** **ANCAGUA** **II ................................................................... 23**
**F** **IGURA** **9.** **P** **ROMEDIO HORARIO VELOCIDAD DEL VIENTO** **(** **M** **/** **S** **)** **WRF** **R** **ANCAGUA** **I .................................................................... 23**
**F** **IGURA** **10.** **P** **ROMEDIO HORARIO VELOCIDAD DEL VIENTO** **(** **M** **/** **S** **)** **ESTACIÓN** **R** **ANCAGUA** **I ............................................................ 24**
**F** **IGURA** **11.** **P** **ROMEDIO HORARIO VELOCIDAD DEL VIENTO** **(** **M** **/** **S** **)** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II .................................................. 24**
**F** **IGURA** **12.** **P** **ROMEDIO HORARIO VELOCIDAD DEL VIENTO** **(** **M** **/** **S** **)** **ESTACIÓN** **R** **ANCAGUA** **II ........................................................... 25**
**F** **IGURA** **13.** **D** **IRECCIÓN DEL VIENTO** **(°)** **ESTACIÓN** **R** **ANCAGUA** **I ............................................................................................... 25**
**F** **IGURA** **14.** **D** **IRECCIÓN DEL VIENTO** **(°)** **WRF** **R** **ANCAGUA** **I ...................................................................................................... 26**
**F** **IGURA** **15.** **D** **IRECCIÓN DEL VIENTO** **(°)** **ESTACIÓN** **R** **ANCAGUA** **II .............................................................................................. 26**
**F** **IGURA** **16.** **D** **IRECCIÓN DEL VIENTO** **(°)** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ..................................................................................... 27**
**F** **IGURA** **17.** **P** **ROMEDIO HORARIO DIRECCIÓN DEL VIENTO** **WRF** **R** **ANCAGUA** **I ............................................................................ 27**

**F** **IGURA** **18.** **P** **ROMEDIO HORARIO DIRECCIÓN DEL VIENTO ESTACIÓN** **R** **ANCAGUA** **I. .................................................................... 28**

**F** **IGURA** **19.** **P** **ROMEDIO HORARIO DIRECCIÓN DEL VIENTO** **WRF** **R** **ANCAGUA** **II ........................................................................... 28**

**F** **IGURA** **20.** **P** **ROMEDIO HORARIO DIRECCIÓN DEL VIENTO ESTACIÓN** **R** **ANCAGUA** **II .................................................................... 29**

**F** **IGURA** **21.** **C** **ICLO HORARIO Y MENSUAL DIRECCIÓN Y VELOCIDAD DEL VIENTO ESTACIÓN** **R** **ANCAGUA** **I...................................... 29**

**F** **IGURA** **22.** **C** **ICLO HORARIO Y MENSUAL DIRECCIÓN Y VELOCIDAD DEL VIENTO** **WRF** **R** **ANCAGUA** **I ............................................ 30**

**F** **IGURA** **23.C** **ICLO HORARIO Y MENSUAL DIRECCIÓN Y VELOCIDAD DEL VIENTO** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ............................ 30**

**F** **IGURA** **24.C** **ICLO HORARIO Y MENSUAL DIRECCIÓN Y VELOCIDAD DEL VIENTO ESTACIÓN** **R** **ANCAGUA** **II ..................................... 31**

**F** **IGURA** **25.** **%** **HUMEDAD MODELO** **WRF** **R** **ANCAGUA** **I ............................................................................................................. 31**
**F** **IGURA** **26.** **%** **HUMEDAD ESTACIÓN** **R** **ANCAGUA** **I .................................................................................................................... 32**

**F** **IGURA** **27.%** **HUMEDAD MODELO** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ............................................................................................. 32**

**F** **IGURA** **28.** **%** **HUMEDAD ESTACIÓN** **R** **ANCAGUA** **II ................................................................................................................... 33**

Página **3** de **73**

**F** **IGURA** **29.** **P** **ROMEDIO HORARIO** **%** **HUMEDAD ESTACIÓN** **R** **ANCAGUA** **I..................................................................................... 33**

**F** **IGURA** **30.** **P** **ROMEDIO HORARIO** **%** **HUMEDAD MODELO** **WRF** **R** **ANCAGUA** **I .............................................................................. 34**
**F** **IGURA** **31.P** **ROMEDIO HORARIO** **%** **HUMEDAD ESTACIÓN** **R** **ANCAGUA** **II .................................................................................... 34**

**F** **IGURA** **32.P** **ROMEDIO HORARIO** **%** **HUMEDAD MODELO** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II .............................................................. 35**

**F** **IGURA** **33.** **P** **ROMEDIO HORARIO Y MENSUAL** **%** **DE HUMEDAD MODELO** **WRF** **R** **ANCAGUA** **I ....................................................... 35**
**F** **IGURA** **34.** **P** **ROMEDIO HORARIO Y MENSUAL** **%** **DE HUMEDAD ESTACIÓN** **R** **ANCAGUA** **I .............................................................. 36**

**F** **IGURA** **35.** **P** **ROMEDIO HORARIO Y MENSUAL** **%** **DE HUMEDAD MODELO** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ....................................... 36**
**F** **IGURA** **36.** **P** **ROMEDIO HORARIO Y MENSUAL** **%** **DE HUMEDAD ESTACIÓN** **R** **ANCAGUA** **II ............................................................. 37**
**F** **IGURA** **37.** **T** **EMPERATURA** **(°C)** **MODELO** **WRF** **R** **ANCAGUA** **I .................................................................................................. 37**
**F** **IGURA** **38.** **T** **EMPERATURA** **(°C)** **ESTACIÓN** **R** **ANCAGUA** **I......................................................................................................... 38**
**F** **IGURA** **39.** **T** **EMPERATURA** **(°C)** **MODELO** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ................................................................................. 38**
**F** **IGURA** **40.** **T** **EMPERATURA** **(°C)** **ESTACIÓN** **R** **ANCAGUA** **II........................................................................................................ 39**
**F** **IGURA** **41.** **P** **ROMEDIO HORARIO DE TEMPERATURA** **(°C)** **MODELO** **WRF** **R** **ANCAGUA** **I .............................................................. 39**
**F** **IGURA** **42.** **P** **ROMEDIO HORARIO DE TEMPERATURA** **(°C)** **ESTACIÓN** **R** **ANCAGUA** **I ..................................................................... 40**
**F** **IGURA** **43.** **P** **ROMEDIO HORARIO DE TEMPERATURA** **(°C)** **MODELO** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ............................................. 40**
**F** **IGURA** **44.** **P** **ROMEDIO HORARIO DE TEMPERATURA** **(°C)** **ESTACIÓN** **R** **ANCAGUA** **II .................................................................... 41**
**F** **IGURA** **45.** **P** **ROMEDIO HORARIO Y MENSUAL DE TEMPERATURA** **(°C)** **MODELO** **WRF** **R** **ANCAGUA** **I ............................................ 41**
**F** **IGURA** **46.** **P** **ROMEDIO HORARIO Y MENSUAL DE TEMPERATURA** **(°C)** **ESTACIÓN** **R** **ANCAGUA** **I ................................................... 42**
**F** **IGURA** **47.** **P** **ROMEDIO HORARIO Y MENSUAL TEMPERATURA** **(°C)** **MODELO** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ................................ 42**
**F** **IGURA** **48.** **P** **ROMEDIO HORARIO Y MENSUAL DE TEMPERATURA** **(°C)** **ESTACIÓN** **R** **ANCAGUA** **II .................................................. 43**
**F** **IGURA** **49.** **R** **OSA DE LOS VIENTOS NOCHE MODELO** **WRF** **R** **ANCAGUA** **I ................................................................................... 43**

**F** **IGURA** **50.** **R** **OSA DE LOS VIENTOS NOCHE ESTACIÓN** **R** **ANCAGUA** **I .......................................................................................... 44**
**F** **IGURA** **51.** **R** **OSA DE LOS VIENTOS MAÑANA** **,** **MODELO** **WRF** **R** **ANCAGUA** **I ............................................................................... 44**
**F** **IGURA** **52.** **R** **OSA DE LOS VIENTOS MAÑANA** **,** **ESTACIÓN** **R** **ANCAGUA** **I ...................................................................................... 45**
**F** **IGURA** **53.** **R** **OSA DE LOS VIENTOS TARDE** **,** **MODELO** **WRF** **R** **ANCAGUA** **I .................................................................................. 45**
**F** **IGURA** **54.** **R** **OSA DE LOS VIENTOS TARDE** **,** **ESTACIÓN** **R** **ANCAGUA** **I ......................................................................................... 46**
**F** **IGURA** **55.** **R** **OSA DE LOS VIENTOS DIARIA** **,** **MODELO** **WRF** **R** **ANCAGUA** **I .................................................................................. 46**
**F** **IGURA** **56.** **R** **OSA DE LOS VIENTOS DIARIA** **,** **ESTACIÓN** **R** **ANCAGUA** **I ......................................................................................... 47**
**F** **IGURA** **57.** **R** **OSA DE LOS VIENTOS NOCHE** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ................................................................................ 47**

**F** **IGURA** **58.** **R** **OSA DE LOS VIENTOS NOCHE ESTACIÓN** **R** **ANCAGUA** **II ......................................................................................... 48**

**F** **IGURA** **59.** **R** **OSA DE LOS VIENTOS MAÑANA** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ............................................................................. 48**

**F** **IGURA** **60.** **R** **OSA DE LOS VIENTOS MAÑANA ESTACIÓN** **R** **ANCAGUA** **II ...................................................................................... 49**

**F** **IGURA** **61.R** **OSA DE LOS VIENTOS TARDE** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ................................................................................. 49**

**F** **IGURA** **62.R** **OSA DE LOS VIENTOS TARDE ESTACIÓN** **R** **ANCAGUA** **II .......................................................................................... 50**

**F** **IGURA** **63.** **R** **OSA DE LOS VIENTOS DIARIA** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ................................................................................ 50**

**F** **IGURA** **64.** **R** **OSA DE LOS VIENTOS DIARIA** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ................................................................................ 51**

**F** **IGURA** **65.** **I** **NFORMACIÓN TOPOGRÁFICA** **............................................................................................................................... 53**

**F** **IGURA** **66.** **E** **LEVACIÓN DE LA ZONA DE MODELACIÓN** **-** **CALPUFF** **3D ................................................................................... 53**

**F** **IGURA** **67.** **R** **EGISTRO DIARIO** **.** **P** **ROMEDIO ANUAL** **MP** **10** **E** **STACIÓN** **R** **ANCAGUA** **II ..................................................................... 54**
**F** **IGURA** **68.** **C** **ONCENTRACIÓN DIARIA** **MP** **10** **E** **STACIÓN** **R** **ANCAGUA** **II........................................................................................ 55**
**F** **IGURA** **69.** **R** **EGISTRO DIARIO** **.** **P** **ROMEDIO ANUAL** **MP** **2,5** **E** **STACIÓN** **R** **ANCAGUA** **II .................................................................... 56**
**F** **IGURA** **70.** **C** **ONCENTRACIÓN DIARIA DE** **MP** **2,5** **E** **STACIÓN** **R** **ANCAGUA** **II .................................................................................. 56**
**F** **IGURA** **71.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **MP** **10** **CONCENTRACIÓN PROMEDIO ANUAL** **.............................................................. 59**
**F** **IGURA** **72.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **MP** **10** **P98** **24H ..................................................................................................... 59**
**F** **IGURA** **73.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **MP** **2,5** **CONCENTRACIÓN PROMEDIO ANUAL** **.............................................................. 60**
**F** **IGURA** **74.** **M** **APA** **I** **SOCONCENTRACIÓN** **MP** **2,5** **P98** **24H.......................................................................................................... 60**
**F** **IGURA** **75.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **SO** **2** **CONCENTRACIÓN PROMEDIO ANUAL** **................................................................ 61**
**F** **IGURA** **76.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **SO** **2** **,** **CONCENTRACIÓN PROMEDIO** **24H .................................................................. 61**
**F** **IGURA** **77.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **SO** **2** **CONCENTRACIÓN** **P98,5** **H** **ORARIO** **.................................................................. 62**
**F** **IGURA** **78.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **NO** **X** **CONCENTRACIÓN PROMEDIO ANUAL** **............................................................... 62**
**F** **IGURA** **79.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **NO** **X** **,** **CONCENTRACIÓN** **P99** **1H ............................................................................. 63**
**F** **IGURA** **80.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **CO,** **CONCENTRACIÓN** **P99** **1** **HORA** **........................................................................ 63**
**F** **IGURA** **81.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **CO,** **CONCENTRACIÓN** **P99** **8H ............................................................................... 64**
**F** **IGURA** **82.** **U** **BICACIÓN DEL** **P** **ROYECTO EN RELACIÓN CON LA ZONA SATURADA O LATENTE** **...................................................... 66**
**F** **IGURA** **83.** **Á** **REA DE INFLUENCIA DEL** **P** **ROYECTO** **,** **COMPONENTE AIRE** **(** **EMISIONES ATMOSFÉRICAS** **) ......................................... 71**

Página **4** de **73**

# 1. Introducción

El Proyecto “Parque Las Alamedas I, II y III”, se ubica en la comuna de Rancagua, provincia de Cachapoal de
la Región del Libertador General Bernardo O'Higgins.

El presente documento corresponde a la evaluación de la dispersión y concentración ambiental de los
contaminantes emitidos a la atmósfera producto de las actividades del Proyecto, dentro del área de estudio,
mediante las herramientas de modelación sugeridas por el Servicio de Evaluación Ambiental, en base a los
lineamientos establecidos en la Guía “Uso de Modelos de Calidad del Aire en el SEIA”, 2023.

En esta modelación, se estimarán las concentraciones horarias utilizando el modelo tipo “Puff” (Utilizando el
programa Calpuff View versión 7.0) de MP 10, MP 2,5, CO, NO X y SO 2 para evaluar el cumplimiento de las normas
de calidad de aire durante el escenario más desfavorable del Proyecto.

# 2. Antecedentes generales del proyecto

**2.1.1.** **Descripción**

Parque Las Alamedas I, II y III está ubicado en la Av. Libertador Bernardo O’Higgins Lote 2B, Comuna de
Rancagua, Región del Libertador General Bernardo O’Higgins, la cual contempla la construcción y operación
de una solución habitacional de tres edificios de 9 pisos, el cual contempla un total de 633 departamentos, 3
locales comerciales y 648 estacionamientos vehiculares y 30 estacionamientos para bicicletas. El proyecto
presenta una superficie de construcción de 42.388,65 m [2] y una superficie predial de 26.340 m [2], donde se
incorporarán 3.123 m [2] de áreas verdes con el objeto de brindar un entorno más amigable a los futuros
propietarios.

El proyecto considera tres etapas constructivas, la cual tendrá una duración de 24 meses cada una y que se
evaluarán íntegramente en la presente DIA.

A continuación, se presentan la descripción de cada etapa.

Etapa N°1: Consiste en la construcción y operación de un edificio de 9 pisos de 211 departamentos, 1 local
comercial, 216 estacionamientos vehiculares y 10 estacionamientos para bicicletas. Posee una superficie de
construcción es de 14.129,55 m [2] en un predio de 8.527,2 m [2] .

Etapa N°2: Consiste en la construcción y operación de un edificio de 9 pisos de 211 departamentos, 1 local
comercial, 216 estacionamientos vehiculares y 10 estacionamientos para bicicletas. Posee una superficie de
construcción es de 14.129,55 m [2] en un predio de 8.527,2 m [2] .

Etapa N°3: Consiste en la construcción y operación de un edificio de 9 pisos de 211 departamentos, 1 local
comercial, 216 estacionamientos vehiculares y 10 estacionamientos para bicicletas. Posee una superficie de
construcción es de 14.129,55 m [2] en un predio de 9.285,6 m [2] .

Adicionalmente, El proyecto forma parte del Plan de Emergencia Habitacional, de acuerdo con lo dispuesto en
el D.S. N°19/2016 del Ministerio de Vivienda y Urbanismo “Programa de Integración Social y Territorial”.

Página **5** de **73**

De acuerdo con el artículo 8° de la Ley N° 19.300, "Los Proyectos o actividades señaladas en el artículo 10
sólo podrán ejecutarse o modificarse previa evaluación de su impacto ambiental, de acuerdo con lo establecido
en la presente Ley".

A su vez, el artículo 10 de la citada Ley enumera la lista de “los Proyectos o actividades susceptibles de causar
impacto ambiental, en cualesquiera de sus fases, que deberán someterse al sistema de evaluación de impacto
ambiental”, los cuales son precisados, en cuanto a sus características y dimensiones, en el artículo 3° del
Reglamento del SEIA (“RSEIA”).

De conformidad con las disposiciones legales y reglamentarias citadas y, específicamente, el artículo 3° del
RSEIA, las siguientes tipologías resultan aplicables al Proyecto:

h) Proyectos industriales o inmobiliarios que se ejecuten en zonas declaradas latentes o saturadas.

h.1. Se entenderá por proyectos inmobiliarios aquellos loteos o conjuntos de viviendas que contemplen obras
de edificación y/o urbanización, así como los proyectos destinados a equipamiento, y que presenten alguna de
las siguientes características:

h.1.3. Que se emplacen en una superficie igual o superior a siete hectáreas (7 ha) o consulten la construcción
de trescientas (300) o más viviendas.

Debido a que el Proyecto se ubica en la Región del Libertador General Bernardo O’Higgins, la cual se encuentra
declarada como saturada por MP 10, como concentración anual y de 24 horas según D.S N°7/2009 y saturada
por MP 2,5 como concentración anual y de 24 horas según D.S. N°42/2017, además de contemplar la
construcción de 633 viviendas, es posible concluir que el proyecto debe ingresar al SEIA por el literal h.1.3.

**2.1.2.** **Localización**

La ubicación político-administrativa a nivel Regional, Provincial y Comunal del Proyecto es la siguiente:

**Región:** del Libertador General Bernardo O'Higgins

**Provincia:** Cachapoal

**Comuna:** Rancagua

El Proyecto se encuentra ubicado en Av. Libertador Bernardo O’Higgins, Lote 2B.

Página **6** de **73**

**Figura 1. Ubicación y vértices del Proyecto**

Fuente: Cartografía 6 Capítulo 1 “Descripción de Proyecto”, 2025.

# 3. Objetivos

**3.1.** **Objetivo General**

El objetivo principal de este estudio atmosférico es evaluar el efecto de las emisiones de contaminantes del
Proyecto “Parque Las Alamedas I, II y III” en la atmósfera.

El propósito es determinar si existe alguna afectación potencial a la salud y calidad de vida de las personas que
realicen actividades en las proximidades del área del Proyecto, en conformidad al artículo 5° del D.S. N° 40/12.

**3.2.** **Objetivos Específicos**

1. Determinar y evaluar la extensión de la dispersión de los contaminantes MP 10, MP 2,5, óxidos de azufre
(SOx), óxidos de nitrógeno (NOx) y monóxido de carbono (CO) con el objetivo de predecir las áreas
de impacto máximo y mínimo.

2. Determinar y evaluar la extensión de la dispersión de los contaminantes MP 10, MP 2,5, óxidos de azufre
(SOx), óxidos de nitrógeno (NOx) y monóxido de carbono (CO), en los receptores detectados en las
cercanías del proyecto.

3. Determinar y evaluar la extensión de la dispersión de los contaminantes MP 10, MP 2,5, SOx, CO y NOx
en las Estaciones de Monitoreo con Representatividad Poblacional (EMRP) cercanas al Proyecto.

4. Realizar un análisis de la línea de base de calidad del aire, en el cual se busca conocer la concentración
de material particulado característico del área del Proyecto.

Página **7** de **73**

# 4. Normativa Calidad de Aire

**4.1.** **Material particulado (MP** **10** **y MP** **2,5** **)**

Para llevar a cabo la evaluación de los aportes y la exposición a las concentraciones de estos contaminantes,
los cuales están regulados bajo normas de calidad primaria. Estas regulaciones tienen como objetivo principal
proteger la salud de las personas frente a los efectos agudos y crónicos, por lo tanto, su aplicación es
fundamental para salvaguardar la calidad del aire en el país.

A continuación, en la siguiente Tabla, se detalla la normativa ambiental relacionada con los contaminantes MP 10
y MP 2,5 .

**Tabla 1. Límites anual y diario MP** **10** **y MP** **2,5**

|Nivel|MP (μg/m3)<br>10|MP (μg/m3)<br>2,5|
|---|---|---|
|Límite anual|50|20|
|Límite diario|130|50|
|Normativa|D.S. N° 12/2022|D.S. N° 12/2011 del MMA|

Fuente: Elaboración propia en base a D.S. N° 12/2022 y D.S. N° 12/2011 del MMA, 2025.

La superación del límite normativa no es motivo de condiciones de superación de la norma, sino que se
considera que la norma es incumplida bajos las siguientes condiciones:

Artículo 4° D.S. N° 12/2022 del MMA, _“Se considerará sobrepasada la norma primaria de calidad ambiental_
_para material particulado respirable MP10 como concentración anual, cuando el promedio aritmético de tres_
_años calendarios consecutivos, en cualquier estación monitora calificada como EMRP, sea mayor o igual a 50_
_μg/m_ _[3]_ _N”_

Artículo 5° D.S. N° 12/2022 del MMA, _“Se considerará sobrepasada la norma primaria de calidad ambiental_
_para material particulado respirable MP10, como concentración de 24 horas, cuando ocurra, en cualquier_
_estación monitora calificada como EMRP, una de las siguientes condiciones:_

_a. En un año calendario, el valor correspondiente al percentil 98 de las concentraciones de 24 horas_
_registradas, sea mayor o igual a 130 μg/m3N_

_b. Si antes que concluya un año calendario, el número de días con mediciones sobre el valor de 130 μg/m3N,_
_sea mayor que siete”_

Artículo 4° D.S. N° 12/2011 del MMA, _“Se considerará sobrepasada la norma primaria de calidad del aire para_
_material particulado fino respirable MP2,5, en los siguientes casos:_

_a) Cuando el percentil 98 de los promedios diarios registrados durante un año, sea mayor a 50(μg/m3), en_
_cualquier estación monitora calificada como EMRP; o_

_b) Cuando el promedio tri-anual de las concentraciones anuales sea mayor a 20(μg/m3), en cualquier estación_

_monitora calificada como EMRP.”_

Página **8** de **73**

**4.2.** **Dióxido de azufre (SO** **2** **)**

En relación con los contaminantes de dióxido de azufre (SO 2 ), éstos están sujetos a regulación de acuerdo con

el D.S. N° 104/2019 del Ministerio del Medio Ambiente. Esta normativa establece los límites máximos

permisibles de concentración de SO 2 en el aire, así como los estándares de calidad del aire aplicables. Este
decreto corresponde a una norma de calidad primaria, cuyo propósito es proteger la salud de las personas de
los efectos agudos y crónicos derivados de la exposición a estos contaminantes, manteniendo un nivel de riesgo
aceptable. Para lograr esto, se establecen límites de concentración permitidos, así como condiciones que
definen la superación de la norma.

**Tabla 2. Límites anual y diario SO** **2**

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Fuente: Elaboración propia, 2025. Como se puede apreciar, el escenario más desfavorable en cuanto a la generación de emisiones atmosféricas corresponde al año 5, y dada la duración del impacto de 12 meses, corresponde evaluar la significancia con la -->

**Tabla 2: de la Guía.**

| Receptores | MP (ug/m3)<br>10 | Col3 | MP 2,5(ug/m3) | Col5 |
| --- | --- | --- | --- | --- |
| **Receptores** | **24 H P98** | **Anual** | **24 H P98** | **Anual** |
| 1 | 5,53E-1 | 1,24E-1 | 3,00E-1 | 7,78E-2 |
| 2 | 5,38E-1 | 1,01E-1 | 2,47E-1 | 5,85E-2 |
| 3 | 4,94E-1 | 5,54E-2 | 2,00E-1 | 2,42E-2 |
| 4 | 6,19E-1 | 1,13E-1 | 2,34E-1 | 5,42E-2 |
| **Valor significancia (Tabla-2, 12 meses)** | **10,00** | **3,00** | **5,13** | **0,99** |

<!-- Estadísticas: 6 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia, 2025. De acuerdo con la Tabla anterior, la concentración de material particulado de MP 10 y MP 2,5 en los receptores humanos, se encuentra **por debajo de los valores de significancia establecidos para la Tabla 2, para 12** -->
<!-- FIN TABLA 2 -->


|Nivel|SO (μg/m3)<br>2|
|---|---|
|Límite anual|60|
|Límite diario|150|
|Límite horario|350|
|Normativa|D.S. N° 104/2019 del MMA|

Fuente: Elaboración propia en base al D.S. N° 104/2019 del MMA, 2025.

De acuerdo con lo indicado en el D.S. N° 104/2019 del MMA, se tiene lo siguiente:

**Artículo 3°**

_“La norma primaria de calidad de aire para dióxido de azufre como concentración anual será de 60 μg/m3N,_
_equivalente a 23 ppbv._

_Se considerará sobrepasada la norma primaria de calidad de aire para dióxido de azufre como concentración_
_anual, cuando ocurra al menos, una de las siguientes condiciones:_

_a) El promedio aritmético de tres años calendario sucesivos de los valores de concentración anual, fuere mayor_
_o igual al valor de la norma que se establece._

_b) Si en un año calendario, el valor de la concentración anual, fuere mayor o igual al doble del valor de la norma_
_que se establece.”_

**Artículo 4°**

_“La norma primaria de calidad de aire para dióxido de azufre como concentración de 24 horas será de 150_
_μg/m3N, equivalente a 57 ppbv._

_Se considerará sobrepasada la norma primaria de calidad de aire para dióxido de azufre como concentración_
_de 24 horas, cuando ocurra al menos, una de las siguientes condiciones:_

_a) El promedio aritmético de tres años calendario sucesivos de los valores del percentil 99 de las_
_concentraciones de 24 horas registradas cada año, fuere mayor o igual al valor de la norma que se establece._

_b) Si en un año calendario, el valor correspondiente al percentil 99 de las concentraciones de 24 horas_
_registradas, fuere mayor o igual al doble del valor de la norma que se establece.”_

Página **9** de **73**

**Artículo 5°**

_“La norma primaria de calidad de aire para dióxido de azufre como concentración de 1 hora será de 350 μg/m3N,_
_equivalente a 134 ppbv._

_Se considerará sobrepasada la norma primaria de calidad de aire para dióxido de azufre como concentración_
_de 1 hora, cuando ocurra al menos, una de las siguientes condiciones:_

_a) El promedio aritmético de tres años calendario sucesivos de los valores del percentil 98,5 de las_
_concentraciones de 1 hora registradas cada año, fuere mayor o igual al valor de la norma que se establece. A_
_partir del cuarto año calendario de publicada la norma en el Diario Oficial, se considera un percentil 99 para_

_evaluar esta condición._

_b) Si en un año calendario, el valor correspondiente al percentil 98,5 de las concentraciones de 1 hora_
_registradas, fuere mayor o igual al doble del valor de la norma que se establece. A partir del cuarto año_
_calendario de publicada la norma en el Diario Oficial, se considera un percentil 99 para evaluar esta condición”._

**4.3.** **Dióxido de nitrógeno (NO** **2** **)**

El dióxido de nitrógeno (NO 2 ) se encuentra sujeto a regulación normativa mediante una norma de calidad
primaria, la cual tiene como objetivo proteger la salud de las personas frente a los efectos agudos y crónicos
derivados de la exposición al NO 2 en el aire. Con este objetivo, se establecen límites de concentración
permitidos y condiciones para la superación de la norma. La regulación del NO 2 se encuentra establecida en el
D.S. N° 114/2002 del Ministerio Secretaría General de la República.

Este decreto establece los límites máximos permisibles de concentración de NO 2 en el aire, así como los
estándares de calidad del aire correspondientes, los cuales se presentan en la siguiente tabla.

**Tabla 3. Límites anual y diario de NO** **2**

|Nivel|NO (μg/m3)<br>2|
|---|---|
|Límite anual|100|
|Límite horario|400|
|Normativa|D.S. N° 114/2002 del MINSEGPRES|

Fuente: Elaboración propia en base a D.S. N° 114/2002 del MINSEGPRES, 2025.

De acuerdo con lo indicado en el D.S. N° 114/2002 del MINSEGPRES, se tiene lo siguiente:

**Artículo 3°**

_“La norma primaria de calidad de aire para dióxido de nitrógeno como concentración anual será de 53 ppbv_
_(100 ug/m_ _[3]_ _N)._

_Se considerará sobrepasada la norma primaria de calidad de aire para dióxido de nitrógeno como concentración_
_anual, cuando el promedio aritmético de los valores de concentración anual de tres años calendarios sucesivos,_
_en cualquier estación monitora EMRPG, fuere mayor o igual al nivel indicado en el inciso precedente._

Página **10** de **73**

_Si el periodo de medición en una estación monitora EMRPG no comenzare el 1o de enero, se considerarán los_
_tres primeros periodos de 12 meses a partir del mes de inicio de las mediciones hasta disponer de tres años_

_calendarios sucesivos de mediciones._

_Se considerará sobrepasada la norma primaria de calidad de aire para dióxido de nitrógeno como concentración_
_anual, si en el primer o segundo periodo de 12 meses a partir del mes de inicio de las mediciones y, al_
_reemplazar la concentración anual para los periodos faltantes por cero, el promedio aritmético de los tres_
_periodos resultare mayor o igual al nivel de la norma.”_

**Artículo 4°**

_“La norma primaria de calidad de aire para dióxido de nitrógeno como concentración de 1 hora será de 213_
_ppbv (400 ug/m_ _[3]_ _N)._

_Se considerará sobrepasada la norma primaria de calidad de aire para dióxido de nitrógeno como concentración_
_de 1 hora, cuando el promedio aritmético de tres años sucesivos del percentil 99 de los máximos diarios de_
_concentración de 1 hora registrados durante un año calendario, en cualquier estación monitora EMRPG, fuere_
_mayor o igual al nivel indicado en el inciso precedente._

_Si el periodo de medición en una estación monitora EMPRG no comenzare el 1 de enero, se considerarán los_
_tres primeros periodos de 12 meses a partir del mes de inicio de las mediciones hasta disponer de tres años_

_calendarios consecutivos de mediciones._

_Se considerará sobrepasada la norma primaria de calidad de aire para dióxido de nitrógeno como concentración_
_de 1 hora, si en el primer o segundo periodo de 12 meses a partir del mes de inicio de las mediciones y, al_
_reemplazar el percentil 99 de los máximos diarios de concentración de 1 hora para los periodos faltantes por_
_cero, el promedio aritmético de los tres periodos resultare mayor o igual al nivel de la norma”._

**4.4.** **Monóxido de carbono (CO)**

El monóxido de carbono (CO) se encuentra sujeto a regulación normativa mediante una norma de calidad
primaria, la cual tiene como objetivo proteger la salud de las personas frente a los efectos agudos y crónicos
derivados de la exposición al CO en el aire. Con este objetivo, se establecen límites de concentración permitidos
y condiciones para la superación de la norma. La regulación del CO se encuentra establecida en el D.S. N°

115/2002 del MINSEGPRES.

Este decreto establece los límites máximos permisibles de concentración de CO en el aire, así como los
estándares de calidad del aire correspondientes, los cuales se presentan en la siguiente tabla.

**Tabla 4. Límites anual y diario de CO**

|Nivel|CO (mg/m3N)|
|---|---|
|Límite horario|30|
|Límite 8 horas|10|
|Normativa|D.S. N° 115/2002 del MINSEGPRES|

Fuente: Elaboración propia en base a D.S. N° 115/2002 del MINSEGPRES, 2025.

De acuerdo con lo indicado en el D.S. N° 115/2002 del MINSEGPRES, se tiene lo siguiente:

Página **11** de **73**

**Artículo 3°**

_“La norma primaria de calidad de aire para monóxido de carbono como concentración de 8 horas será de 9_
_ppmv (10mg/m_ _[3]_ _N)._

_Se considerará sobrepasada la norma primaria de calidad de aire para monóxido de carbono como_
_concentración de 8 horas, cuando el promedio aritmético de tres años sucesivos, del percentil 99 de los_
_máximos diarios de concentración de 8 horas registrados durante un año calendario, en cualquier estación_
_monitora EMRPG fuere mayor o igual al nivel indicado en el inciso precedente._

_Si el período de medición en una estación monitora EMPRG no comenzare el 1o de enero, se considerarán los_
_tres primeros períodos de 12 meses a partir del mes de inicio de las mediciones hasta disponer de tres años_

_calendarios sucesivos de mediciones._

_Se considerará sobrepasada la norma primaria de calidad de aire para monóxido de carbono como_
_concentración de 8 horas, si en el primer o segundo período de 12 meses a partir del mes de inicio de las_
_mediciones y, al reemplazar el percentil 99 de los máximos diarios de concentración de 8 horas para los_
_períodos faltantes por cero, el promedio aritmético de los tres períodos resultare mayor o igual al nivel de la_

_norma.”_

**Artículo 4°**

_“La norma primaria de calidad de aire para monóxido de carbono como concentración de 1 hora será de 26_
_ppmv (30 mg/m_ _[3]_ _N)._

_Se considerará sobrepasada la norma primaria de calidad de aire para monóxido de carbono como_
_concentración de 1 hora, cuando el promedio aritmético de tres años sucesivos, del percentil 99 de los máximos_
_diarios de concentración de 1 hora registrados durante un año calendario, en cualquier estación monitora_
_EMRPG, fuere mayor o igual al nivel indicado en el inciso precedente._

_Si el período de medición en una estación monitora EMPRG no comenzare el 1o de enero, se considerarán los_
_tres primeros períodos de 12 meses a partir del mes de inicio de las mediciones hasta disponer de tres años_

_calendarios sucesivos de mediciones._

_Se considerará sobrepasada la norma primaria de calidad de aire para monóxido de carbono como_
_concentración de 1 hora, si en el primer o segundo período de 12 meses a partir del mes de inicio de las_
_mediciones y, al reemplazar el percentil 99 de los máximos diarios de concentración de 1 hora para los períodos_
_faltantes por cero, el promedio aritmético de los tres períodos resultare mayor o igual al nivel de la norma.”_

Página **12** de **73**

# 5. Justificación de los modelos utilizados

**5.1.** **Uso del Modelo CALPUFF**

Los modelos de calidad del aire disponibles se clasifican principalmente en cuatro categorías: modelos
Gaussianos, modelos Eulerianos, modelos Lagrangeanos y modelos tipo puff.

Para efectos de esta modelación de dispersión de contaminantes atmosféricos provenientes del Proyecto, se
realizó con un modelo tipo “Puff”, específicamente el modelo CALPUFF, modelo recomendado en el punto 3.2
a) de la “Guía para el uso de modelos de calidad del aire en el SEIA”, 2023, para contaminantes primarios en

un radio de 5 km desde la fuente de emisión.

De acuerdo con lo indicado por la “Guía para el uso de modelos de calidad del aire en el SEIA”, 2023, “los
modelos tipo puff son una combinación entre los modelos Gaussianos y los modelos Lagrangeanos, en el
sentido de que esencialmente calculan la dispersión de contaminantes provenientes de una emisión
instantánea, llamada puff, a lo largo de una trayectoria. Su aproximación matemática consiste en estimar la
dispersión en forma Gaussiana en cada punto de una trayectoria; es decir, a diferencia de los modelos
Lagrangeanos que necesitan el cálculo de un gran número de trayectorias para una fuente, los modelos tipo
puff solo requieren una trayectoria por puff, lo que hace su cálculo mucho más rápido. En el caso de emisiones
continuas, se simulan las trayectorias y la dispersión Gaussiana de muchos puff”.

CALPUFF se compone de tres módulos: CALMET, CALPUFF y CALPOST.

El módulo CALMET es un modelo meteorológico que genera campos horarios de viento y temperatura en una
grilla tridimensional. También asigna campos en dos dimensiones de altura y usos del suelo. Es importante
destacar que este módulo puede ser reemplazado por el modelo WRF.

El módulo CALPUFF, por su parte, es un modelo de transporte y dispersión que simula los procesos de
dispersión y transformación de contaminantes emitidos desde fuentes modeladas. CALPUFF utiliza los datos
generados por CALMET como entrada y genera archivos de salida que contienen las concentraciones horarias
o la deposición por hora de los flujos evaluados en receptores seleccionados.

Además, el módulo CALPOST se utiliza para procesar los archivos generados por CALMET y CALPUFF,
produciendo tabulaciones que resumen los resultados de la simulación.

Por último, se destaca que la modelación CALPUFF es la más recomendable para este caso, debido a que, es
especialmente útil para modelar la dispersión de contaminantes a largas distancias (mayores a 50 km). Además,
este tiene la capacidad de manejar condiciones meteorológicas no estacionarias y complejas, como vientos
variables en el tiempo, espacio y terrenos irregulares, al considerar la topografía y meteorología del
emplazamiento del Proyecto, brindando así una mayor precisión en el resultado.

**5.2.** **Ecuación del modelo CALPUFF**

La ecuación básica que utiliza el modelo para realizar la modelación es la siguiente:

Página **13** de **73**

[−d] 2σ y [2][c2] []]

Q
C=
2πQ x Q y

g exp

~~[~~ [−d] 2σ x [2][a2]

[−d] 2σ x [2][a2] [] exp] ~~[[]~~ [−d] 2σ y [2][c2]

∞

2
g=
(2π) [1/2] σ z

2

∑ ~~[~~ [−(H] [e] 2σ [+ 2nh)] Z [2]

n=−∞

2σ Z

[2]

2
]

Dónde:

 - C, es concentración a nivel del suelo (g/m3),

 - Q, es masa de contaminantes (g) en la nube.

 - σ x, es desviación estándar (m) de la distribución de Gauss en el viento a lo largo de la dirección.

 - σ y, es desviación estándar (m) de la distribución de Gauss en el viento de costado

 - σ z, es desviación estándar (m) de la distribución de Gauss en la dirección vertical.

 - da, es distancia (m) del centro de la nube al receptor en la dirección del viento a lo largo.

 - dc, es distancia (m) del centro de la nube al receptor en la dirección de viento cruzado.

 - g, es el término vertical (m) de la ecuación Gaussiana.

 - H, es la altura afectiva (m) desde el nivel del suelo del hojaldre.

 - h, es la altura de la capa de mezcla.

**5.3.** **Uso del Modelo WRF**

Modelo numérico recomendado para la generación de datos meteorológicos corresponde al modelo WRF,
Weather Research and Forecasting Model por sus siglas en inglés, es uno de los simuladores meteorológicos
de pronóstico más avanzados y completos que se encuentra en constante mejora por el National Center for
Atmospheric Research (NCAR) y la National Oceanic and Atmospheric Administration (NOAA) (además de otras
instituciones como el NCEP, ESRL, AFWA, etc.).

El modelo WRF es una herramienta de predicción numérica del tiempo desarrollada tanto para fines de
investigación como para aplicaciones operativas.

# 6. Metodología

La metodología utilizada para llevar a cabo la modelación de la dispersión de material particulado y gases de
combustión se describe, a continuación.

**6.1.** **Modelación meteorológica**

El modelo WRF es un modelo matemático que realiza la simulación de las condiciones meteorológicas en un
dominio de modelación, utilizando las variables que influyen en la meteorología. Para el caso de la presente
modelación de emisiones, se utilizó para el año 2024.

Página **14** de **73**

**6.2.** **Modelación CALPUFF**

Para la modelación meteorológica, se adoptaron los siguientes criterios. La modelación CALPUFF se realizó en
un dominio de 50 km x 50 km, que abarca toda el área del Proyecto, como se muestra en la siguiente Figura.

**Figura 2. Dominio de la modelación**

Fuente: Elaborado propia, 2025.

En cuanto a los escenarios de modelación, se generó un mapa de iso-concentración para analizar los resultados
de la dispersión de MP 2,5, MP 10, SO x, CO y NO x, los cuales corresponden a las emisiones generadas por las
actividades del Proyecto. Este mapa permitió evaluar los niveles de concentración en toda el área de estudio.

El mapa se obtuvo mediante la modelación del dominio, el cual se representó mediante una grilla con una
resolución de 1 km. Esta grilla proporciona datos de concentración en cada vértice. Los mapas resultantes son
el producto de la interpolación entre los datos de modelación en cada vértice. Además, los datos de
concentración generados por el modelo corresponden a la concentración promedio de la primera capa de

modelación.

Dado lo anterior, es necesario considerar que el mapa de iso-concentración es una representación espacial de
la dispersión y no debe tomarse como una referencia precisa de la concentración, ya que tiende a sobreestimar
los valores. Por el contrario, la evaluación de la concentración en puntos discretos ofrece una estimación más
precisa y libre de distorsiones de la magnitud del impacto en la calidad del aire. Por esta razón, se realizó una
modelación discreta en receptores específicos para analizar el impacto en las poblaciones cercanas.

**6.3.** **Receptores discretos**

A continuación, en la siguiente Tabla se presentan las coordenadas de los receptores discretos en el área del
Proyecto.

Página **15** de **73**

**Tabla 5. Receptores discretos en el área del Proyecto**

|Receptores|Descripción|Altura de<br>receptor (m)|Distancia<br>Proyecto<br>(m)|Coordenadas UTM Huso<br>19S|Col6|
|---|---|---|---|---|---|
|**Receptores**|**Descripción**|**Altura de**<br>**receptor (m)**|**Distancia**<br>**Proyecto**<br>**(m)**|**Este**|**Norte**|
|R1|Galpón Material ligero de un piso|1,5|19|337.026|6.218.934|
|R2|Edificio Material solido de 8 pisos|1,5 - 19|5|336.990|6.218.793|
|R3|Edificio Material solido de 8 pisos|1,5 - 19|22|337.023|6.218.680|
|R4|Jardín infantil de material solido de un piso|1,5|117|337.194|6.218.998|

Fuente: Elaboración en base Tabla 5 Estudio de Ruido y Vibraciones, 2025.

Cabe destacar que, si bien existen otras edificaciones cercanas al área del Proyecto, se han considerado los
puntos de evaluación más cercanos para la evaluación.

A continuación, se presentan fotografías de los puntos receptores considerados.

Página **16** de **73**

|Col1|Tabla 6. fotografías referenciales de receptores|
|---|---|
|R1||
|R2||

|R3|Col2|
|---|---|
|R4||

Fuente: Tabla 5. Estudio de Ruido y Vibración, 2025.

A continuación, en la siguiente Figura se presentan la ubicación de los receptores discretos.

Página **17** de **73**

**Figura 3. Ubicación de receptores discretos**

Fuente: Figura 4 Estudio de Ruido y Vibración, 2025.

**6.4.** **Fuentes de emisión**

En las siguientes Tabla y Figura se presentan las fuentes de emisión como toneladas año y como tasa de
emisión del Proyecto, las cuales han sido ingresadas como datos de entrada para el modelo CALPUFF.

**Tabla 7. Fuentes de emisión del Proyecto**

|Cod. de la<br>fuente|Fuente|Superficie/longitud de la<br>fuente|Actividades incluidas en las<br>fuentes|Emisiones (ton/año)|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Cod. de la**<br>**fuente**|**Fuente**|**Superficie/longitud de la**<br>**fuente**|**Actividades incluidas en las**<br>**fuentes**|**MP10**|**MP2,5**|**NOX **|**SO2 **|**CO **|
|SCR_1|Difusa|42.388,6 m2|Movimiento de tierra|0,07|0,05|0,77|0,00|0,27|
|SCR_2|Móvil|7,24 km|Caminos no pavimentados<br>construcción|0,38|0,04|0,00|0,00|0,00|
|SCR_3|Móvil|133,8 km|Caminos pavimentados construcción|0,10|0,05|0,12|0,00|0,05|
|SCR_4|Difusa|9.287 m2|Escarpe|0,02|0,00|0,00|0,00|0,00|
|SCR_5|Móvil|4,67 km|Rutas pavimentadas operación|0,85|0,21|0,10|0,00|2,66|

Página **18** de **73**

|Cod. de la<br>fuente|Fuente|Superficie/longitud de la<br>fuente|Actividades incluidas en las<br>fuentes|Emisiones (ton/año)|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Cod. de la**<br>**fuente**|**Fuente**|**Superficie/longitud de la**<br>**fuente**|**Actividades incluidas en las**<br>**fuentes**|**MP10**|**MP2,5**|**NOX **|**SO2 **|**CO **|
|SCR_6|Puntual|15 m2|Grupo electrógeno|0,00|0,00|0,00|0,00|0,00|

Fuente: Elaborado propia, 2025.

**Figura 4. Fuentes de emisión del Proyecto**

Fuente: Elaborado propia, 2025.

A continuación, en la siguiente Tabla se presentan los parámetros de ingreso del modelo CALPUFF.

**Tabla 8. Parámetros de entrada al modelo**

|Fuente|Col2|Tipo de fuente|Largo (km)|Área (m2)|Unidad de tasas<br>de emisión|
|---|---|---|---|---|---|
|**Nombre**|**Nombre en modelo**|**Nombre en modelo**|**Nombre en modelo**|**Nombre en modelo**|**Nombre en modelo**|
|SCR_1|Movimiento de tierra|AREA-POLYGONAL|-|42.388,7 m2|g/m2·s|
|SCR_2|Tránsito caminos no<br>pavimentados|ROAD|7,24 km|-|g/m·s|
|SCR_3|Tránsito caminos<br>pavimentados|ROAD|133,80 km|-|g/m·s|
|SCR_4|Escarpe|AREA-POLYGONAL|-|9.287 m2|g/m2·s|
|SCR_5|Rutas pavimentadas<br>operación|ROAD|4,67 km|-|g/m·s|
|SCR_|Grupo electrógeno|AREA-CIRCULAR|-|15|g/m2·s|

Fuente: Elaborado propia, 2025.

Página **19** de **73**

**6.5.** **Análisis de incertidumbre**

**6.5.1.** **Modelo Meteorológico**

De acuerdo con lo recomendado por la Guía para el uso de Modelos de Calidad del Aire en el SEIA, se utilizó
la meteorología del modelo meteorológico WRF, la cual fue ingresa como datos de entrada para el modelo
CALPUFF para la modelación de emisiones atmosféricas.

Los datos del modelo WRF son los siguientes:

 - Periodo modelado: 2024-01-01 00:00:00 - 2025-01-02 20:00:00

 - Coordenadas del dominio:

`o` RLAT0 = 34.159S

`o` RLON0 = 70.767W

`o` XLAT1 = 34.399S

`o` XLAT2 = 33.919S

 - Proyección: Lambert Conic Conformal (LCC)

 - Resolución (grilla): 1 x 1 (km [2] )

 - Tamaño del dominio: 50 x 50 (km [2] )

 - Zona Horario: UTC/GMT UTC -4 horas

 - Datum: NWS-84

Los datos meteorológicos utilizados para el análisis de incertidumbre del modelo meteorológico se obtuvieron
de las estaciones Rancagua I, y Rancagua II, cuyo propietario es el Ministerio del Medio Ambiente y su operador
es Algoritmos y Mediciones Ambientales SpA.

A continuación, en la siguiente Tabla se presenta la información geográfica y las variables utilizadas para la

validación de los datos.

**Tabla 9. Estación utilizada para la validación del modelo WRF**

|Estación|Parámetro|Coordenadas UTM|Col4|Variables<br>utilizadas|Periodo|
|---|---|---|---|---|---|
|**Estación**|**Parámetro**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Rancagua I|Meteorológicos|342.015|6.218.523|Velocidad del<br>viento|2024|
|Rancagua I|Meteorológicos|342.015|6.218.523|Humedad|Humedad|
|Rancagua I|Meteorológicos|342.015|6.218.523|Dirección del<br>viento|Dirección del<br>viento|
|Rancagua I|Meteorológicos|342.015|6.218.523|Temperatura|Temperatura|
|Rancagua II|Meteorológicos|339.842|6.220.527|Velocidad del<br>viento|2024|
|Rancagua II|Meteorológicos|339.842|6.220.527|Humedad|Humedad|
|Rancagua II|Meteorológicos|339.842|6.220.527|Dirección del<br>viento|Dirección del<br>viento|

Página **20** de **73**

|Estación|Parámetro|Coordenadas UTM|Col4|Variables<br>utilizadas|Periodo|
|---|---|---|---|---|---|
|**Estación**|**Parámetro**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|**Estación**|**Parámetro**|||Temperatura|Temperatura|

Fuente: Elaboración propia, 2025.

El periodo de información descargado corresponde al año 2024, el cual es el mismo año de los datos del modelo

WRF.

Además, se señala que la estación de monitoreo cumple con los requisitos establecidos por el Servicio de
Evaluación Ambiental (SEA) en su “Guía para el uso de modelos de calidad del aire en el SEIA” (2023),
cumpliendo con el mínimo requerido de datos válidos para las variables meteorológicas, los cual corresponde
a un 75% de los registros mínimos.

**6.5.2.** **Análisis cualitativo**

A continuación, se presenta el análisis cualitativo de las variables meteorológicas medidas en las estaciones
Rancagua I, y Rancagua II del Ministerio del Medio Ambiente y los datos modelados (WRF).

**6.5.2.1.** **Velocidad del viento**

En la siguiente Figura se presenta la serie de tiempo para la velocidad del viento de la estación de monitoreo
Rancagua I y Rancagua II.

**Figura 5. Datos velocidad del viento WRF Rancagua I**

Fuente: Elaboración propia, 2025.

Página **21** de **73**

**Figura 6. Datos velocidad del viento estación Rancagua I**

Fuente: Elaboración propia, 2025.
**Figura 7. Datos velocidad del viento WRF Rancagua II**

Fuente: Elaboración propia, 2025.

Página **22** de **73**

**Figura 8. Datos velocidad de viento observada en estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 9. Promedio horario velocidad del viento (m/s) WRF Rancagua I**

Fuente: Elaboración propia, 2025.

Página **23** de **73**

**Figura 10. Promedio horario velocidad del viento (m/s) estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 11. Promedio horario velocidad del viento (m/s) WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **24** de **73**

**Figura 12. Promedio horario velocidad del viento (m/s) estación Rancagua II**

Fuente: Elaboración propia 2025.

**6.5.2.2.** **Dirección del Viento**

En la siguientes Figuras se presenta los valores de la dirección del viento para las estaciones Rancagua I,
Rancagua II y WRF.
**Figura 13. Dirección del viento (°) estación Rancagua I**

Fuente: Elaboración propia, 2025.

Página **25** de **73**

**Figura 14. Dirección del viento (°) WRF Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 15. Dirección del viento (°) estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **26** de **73**

**Figura 16. Dirección del viento (°) WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 17. Promedio horario dirección del viento WRF Rancagua I**

Fuente: Elaboración propia, 2025.

Página **27** de **73**

**Figura 18. Promedio horario dirección del viento estación Rancagua I.**

Fuente: Elaboración propia, 2025.

**Figura 19. Promedio horario dirección del viento WRF Rancagua II**

Fuente: Elaboración propia, 2025.

Página **28** de **73**

**Figura 20. Promedio horario dirección del viento estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 21. Ciclo horario y mensual dirección y velocidad del viento estación Rancagua I**

Fuente: Elaboración propia, 2025.

Página **29** de **73**

**Figura 22. Ciclo horario y mensual dirección y velocidad del viento WRF Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 23.Ciclo horario y mensual dirección y velocidad del viento WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **30** de **73**

**Figura 24.Ciclo horario y mensual dirección y velocidad del viento estación Rancagua II**

Fuente: Elaboración propia, 2025. Para el caso de los datos de dirección del viento observados en las figuras
anteriores, e posible observar que presentan la misma tendencia, lo que indica un comportamiento modelado

cercano a la realidad de los datos medidos en la estación meteorológica en estudio.

**6.5.2.3.** **Humedad**

Las siguientes Figuras presenta la comparación entre los datos observados en la estación Rancagua I,
Rancagua II y obtenido del modelo WRF para la variable Humedad.

**Figura 25. % humedad modelo WRF Rancagua I**

Página **31** de **73**

Fuente: Elaboración propia, 2025.

**Figura 26. % humedad estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 27.% humedad modelo WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **32** de **73**

**Figura 28. % humedad estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 29. Promedio horario % humedad estación Rancagua I**

Fuente: Elaboración propia, 2025.

Página **33** de **73**

**Figura 30. Promedio horario % humedad modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 31.Promedio horario % humedad estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **34** de **73**

**Figura 32.Promedio horario % humedad modelo WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 33. Promedio horario y mensual % de humedad modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

Página **35** de **73**

**Figura 34. Promedio horario y mensual % de humedad estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 35. Promedio horario y mensual % de humedad modelo WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **36** de **73**

**Figura 36. Promedio horario y mensual % de humedad estación Rancagua II**

Fuente: Elaboración propia, 2025.

**6.5.2.4.** **Temperatura**

A continuación, en las siguiente Figura se presenta la gráfica comparativa entre la estación Meteorológica
principal, Puchuncavi y el modelo WRF.

**Figura 37. Temperatura (°C) modelo WRF Rancagua I**

Página **37** de **73**

Fuente: Elaboración propia, 2025.

**Figura 38. Temperatura (°C) estación Rancagua I**

Fuente: Elaboración propia, 2025.
**Figura 39. Temperatura (°C) modelo WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **38** de **73**

**Figura 40. Temperatura (°C) estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 41. Promedio horario de temperatura (°C) modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

Página **39** de **73**

**Figura 42. Promedio horario de temperatura (°C) estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 43. Promedio horario de temperatura (°C) modelo WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **40** de **73**

**Figura 44. Promedio horario de temperatura (°C) estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 45. Promedio horario y mensual de temperatura (°C) modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

Página **41** de **73**

**Figura 46. Promedio horario y mensual de temperatura (°C) estación Rancagua I**

Fuente: Elaboración propia, 2025.
**Figura 47. Promedio horario y mensual temperatura (°C) modelo WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **42** de **73**

**Figura 48. Promedio horario y mensual de temperatura (°C) estación Rancagua II**

Fuente: Elaboración propia, 2025.

**6.5.2.5.** **Rosa de los vientos**

A continuación, se presenta la comparación de la rosa de los vientos para la estación Meteorológica principal
y Puchuncavi y el modelo WRF.

**Figura 49. Rosa de los vientos noche modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

Página **43** de **73**

**Figura 50. Rosa de los vientos noche estación Rancagua I**

Fuente: Elaboración propia, 2025.
**Figura 51. Rosa de los vientos mañana, modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

Página **44** de **73**

**Figura 52. Rosa de los vientos mañana, estación Rancagua I**

Fuente: Elaboración propia, 2025.
**Figura 53. Rosa de los vientos tarde, modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

Página **45** de **73**

**Figura 54. Rosa de los vientos tarde, estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 55. Rosa de los vientos diaria, modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

Página **46** de **73**

**Figura 56. Rosa de los vientos diaria, estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 57. Rosa de los vientos noche WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **47** de **73**

**Figura 58. Rosa de los vientos noche estación Rancagua II**

Fuente: Elaboración propia, 2025.
**Figura 59. Rosa de los vientos mañana WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **48** de **73**

**Figura 60. Rosa de los vientos mañana estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 61.Rosa de los vientos tarde WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **49** de **73**

**Figura 62.Rosa de los vientos tarde estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 63. Rosa de los vientos diaria WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **50** de **73**

**Figura 64. Rosa de los vientos diaria WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

**6.5.3.** **Análisis cuantitativo**

El análisis cualitativo se realizado de acuerdo con lo recomendado por la Guía para uso de Modelos de Calidad
del Aire en el SEIA, 2023 utilizando las métricas estadísticas del sesgo (error medio o BIAS), error absoluto
medio (MAE) y la raíz del error cuadrático medio (RMSE). Las ecuaciones para cada una de las métricas se
presentan a continuación.

n

BIAS= [1]

n [∑(S] [i] [−O] [i] [)]

i=0

n

MAE= [1]

n [∑|S] [i] [−O] [i] [|]

i=1

n

RMSE= √ [1]

n

n [∑(S] [i] [−O] [i] [)] [2]

i=1

Donde:

N: Cantidad de datos

S: Valores obtenidos del modelo

Página **51** de **73**

O: Valores observados en estaciones meteorológicas

A su vez, se incorpora de acuerdo con lo recomendado en la Guía mencionada, el cálculo del coeficiente de
correlación (r), que corresponde a una correlación lineal entre los valores modelados y observados. Para medir
el coeficiente de correlación lineal, se utilizan valores que oscilan entre -1 y 1. Un valor de -1 indica una
correlación negativa, lo que significa que cuando aumenta el valor de una variable, la otra disminuye, y
viceversa. Por otro lado, un valor de 1 indica la máxima correlación positiva, lo que implica que ambas variables
se mueven en la misma dirección: cuando una aumenta, la otra también lo hace, y cuando una disminuye, la

otra también lo hace.

**Tabla 10. Estadísticos de sesgo, error absoluto medio y error cuadrático medio**

|Estación|Variable meteorológica|BIAS|MAE|RMSE|r|
|---|---|---|---|---|---|
|Rancagua I|Velocidad del viento (m/s)|-0,56|0,58|0,79|0,90|
|Rancagua I|Temperatura (°C)|-1,57|-1,57|1,90|0,97|
|Rancagua II|Velocidad del viento (m/s)|-0,48|0,48|0,67|0,93|
|Rancagua II|Temperatura (°C)|-1,96|1,96|2,4|0,98|
|Límite*|Velocidad del viento (m/s)|(-2,5;2,5) (m/s)|≤ 3 (m/s)|≤ 3,5 (m/s)|>0,6|
|Límite*|Temperatura (°C)|(-4,4) (°C)|≤ 4 (°C)|≤ 4,5 (°C)|>0,8|
|*Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”, Guía para el uso de modelos<br>de Calidad del Aire en el SEIA.|*Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”, Guía para el uso de modelos<br>de Calidad del Aire en el SEIA.|*Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”, Guía para el uso de modelos<br>de Calidad del Aire en el SEIA.|*Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”, Guía para el uso de modelos<br>de Calidad del Aire en el SEIA.|*Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”, Guía para el uso de modelos<br>de Calidad del Aire en el SEIA.|*Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”, Guía para el uso de modelos<br>de Calidad del Aire en el SEIA.|

Fuente: Elaboración propia, 2025.

Para la estación Rancagua I en comparación a las métricas estadísticas recomendables en el análisis de
incertidumbre para la variable meteorológica de temperatura (°C) de -1,57 para el error cuadrático medio (BIAS),
1,57, para el valor absoluto (MAE) y 1,90 para el error cuadrático medio (RMSE), teniendo que se encuentran
dentro de las métricas estadísticas recomendadas por la Guía para el uso de Modelos de Calidad del Aire.
Además, el coeficiente de correlación lineal de 0,97, el cual representa una buena aproximación.

Para la variable velocidad del viento (m/s) se tiene un valor del error cuadrático medio (BIAS) de -0,56, error
absoluto (MAE) de 0,58 y error cuadrático medio (RMSE) de 0,79, teniendo que, los valores se encuentran
dentro de las métricas estadísticas recomendables por la Guía para el uso de Modelos de Calidad del Aire.
Además, cabe mencionar que, el coeficiente de correlación tiene un valor de 0,90, el cual representa una buena
aproximación.

Respecto a la estación Rancagua II se tiene que, en comparación a las métricas estadísticas recomendables
en el análisis de incertidumbre para la variable meteorológica de temperatura (°C) de -1,96 para el error
cuadrático medio (BIAS), 1,96, para el valor absoluto (MAE) y 2,4 para el error cuadrático medio (RMSE),
teniendo que se encuentran dentro de las métricas estadísticas recomendadas por la Guía para el uso de
Modelos de Calidad del Aire. Además, el coeficiente de correlación lineal de 0,98, el cual representa una buena
aproximación.

Para la variable velocidad del viento (m/s) se tiene un valor del error cuadrático medio (BIAS) de -0,48, error
absoluto (MAE) de 0,48 y error cuadrático medio (RMSE) de 0,67, teniendo que, los valores se encuentran
dentro de las métricas estadísticas recomendables por la Guía para el uso de Modelos de Calidad del Aire.

Página **52** de **73**

Además, cabe mencionar que, el coeficiente de correlación tiene un valor de 0,93, el cual representa una buena
aproximación.

Del análisis se concluye que los datos presentados en el WRF tienen una fiabilidad aceptable para realizar la
modelación de dispersión de contaminantes atmosféricos.

**6.6.** **Topografía**

La información se obtuvo de las cartas topográficas SRTM1, con una resolución aproximada de 30 metros

cuadrados.

**Figura 65. Información topográfica**

Fuente: Elaboración propia, 2025.

**Figura 66. Elevación de la zona de modelación - CALPUFF 3D**

Fuente: Elaboración propia, 2025.

Página **53** de **73**

**6.7.** **Caracterización Ambiental del Proyecto**

La caracterización ambiental del Proyecto se realiza utilizando los datos recopilados por la estación de
monitoreo ubicada en las cercanías del Proyecto y que cumpla con los requerimientos establecidos.

La estación de monitoreo utilizada más cercana, con una base consolidada de información es la estación
Rancagua II, ubicada en la comuna de Rancagua, Provincia de Cachapoal, Región del Libertador General
Bernardo O’Higgins a una distancia de 3,03 km del Proyecto. Los datos extraídos para la caracterización fueron
extraídos del Sistema de Información Nacional de Calidad del Aire (SINCA) el 11 de febrero de 2025.

**6.7.1.** **Material Particulado Respirable (MP** **10** **)**

En la siguiente Figura, se presentan las series de tiempo correspondiente a las concentraciones promedio
anuales para el MP 10 para los años 2022, 2023 y 2024 (últimos 3 años).

**Figura 67. Registro diario. Promedio anual MP** **10** **Estación Rancagua II**

Fuente: Base SINCA, 2025.

Página **54** de **73**

**Figura 68. Concentración diaria MP** **10** **Estación Rancagua II**

Fuente: Base SINCA, 2025.

A continuación, en las siguientes Tablas, se muestran la concentración media anual y el percentil 98 de las
concentraciones de MP 10 registradas en la estación Rancagua II.

**Tabla 11. Concentración Media Anual de MP** **10** **(ug/m** **[3]** **N)**

|Estación|Norma primaria de MP (D.S. N° 12/2021 del MMA) - Media Anual<br>10|Col3|Col4|Trianual|Porcentaje de la<br>norma|
|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 50 (ug/m3N)**|**Valor Norma: 50 (ug/m3N)**|**Valor Norma: 50 (ug/m3N)**|**Valor Norma: 50 (ug/m3N)**|**Valor Norma: 50 (ug/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2022**|**2023**|**2024**|**2024**|**2024**|
|Rancagua II|43,81|44,93|58,74|49,16|98,33%|

Fuente: Elaboración propia, en base a datos del Sistema Nacional de Calidad del Aire (SINCA), 2025.

**Tabla 12. Percentil 98 concentración 24 horas de MP** **10** **(ug/m** **[3]** **N)**

|Estación|Norma primaria de MP (D.S. N° 12/2021 del MMA) - 24 H<br>10|Porcentaje de la norma|
|---|---|---|
|**Estación**|**Valor norma: 130 (ug/m3N)**|**Valor norma: 130 (ug/m3N)**|
|**Estación**|**Año**|**Año**|
|**Estación**|**2024**|**2024**|
|Rancagua II|145,96|112,27%|

Fuente: Elaboración propia, en base a datos del Sistema Nacional de Calidad del Aire (SINCA), 2025.

Página **55** de **73**

**6.7.2.** **Material Particulado Respirable Fino (MP** **2,5** **)**

En la siguiente Figura, se presentan las series de tiempo correspondientes a las concentraciones promedio
anuales para el contaminante MP 2,5 para los años 2022, 2023 y 2024 (últimos 3 años) en la estación Rancagua

II.

**Figura 69. Registro diario. Promedio anual MP** **2,5** **Estación Rancagua II**

Fuente: Base SINCA, 2025.

**Figura 70. Concentración diaria de MP** **2,5** **Estación Rancagua II**

Fuente: Base SINCA, 2025.

Página **56** de **73**

En las siguientes Tablas, se detalla la concentración media anual y el percentil 98 de las concentraciones de
MP 2,5 registradas en la estación Rancagua II.

**Tabla 13. Concentración Media Anual de MP** **2,5** **(ug/m** **[3]** **N)**

|Estación|Norma primaria de MP (D.S. N° 12/2021 del MMA) - Media Anual<br>2,5|Col3|Col4|Trianual|Porcentaje de la<br>norma|
|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 20 (ug/m3N)**|**Valor Norma: 20 (ug/m3N)**|**Valor Norma: 20 (ug/m3N)**|**Valor Norma: 20 (ug/m3N)**|**Valor Norma: 20 (ug/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2022**|**2023**|**2024**|**2024**|**2024**|
|Rancagua II|29,63|22,96|24,14|25,58|127,90%|

Fuente: Elaboración propia, en base a datos del Sistema Nacional de Calidad del Aire (SINCA), 2025.

**Tabla 14. Percentil 98 concentración 24 horas de MP** **2,5** **(ug/m** **[3]** **N)**

|Estación|Norma primaria de MP (D.S. N° 12/2011 del MMA) - 24 H<br>2,5|Porcentaje de la norma|
|---|---|---|
|**Estación**|**Valor norma: 50 (ug/m3N)**|**Valor norma: 50 (ug/m3N)**|
|**Estación**|**Año**|**Año**|
|**Estación**|**2024**|**2024**|
|Rancagua II|87|174%|

Fuente: Elaboración propia, en base a datos del Sistema Nacional de Calidad del Aire (SINCA), 2025.

**6.7.3.** **Dióxido de azufre (SO** **2** **)**

La estación Rancagua II no presenta mediciones de SO 2 .

**6.7.4.** **Óxidos de nitrógeno (NO** **x** **)**

La estación Rancagua II no presenta mediciones de NO x .

**6.7.5.** **Monóxido de carbono (CO)**

La estación Rancagua II no presenta mediciones de CO.

Página **57** de **73**

# 7. Resultados

A continuación, se entregan las concentraciones obtenidas utilizando el modelo meteorológico de meso escala
Weather Research Forecasting Modelo (WRF), como insumo para el software CALPUFF View.

De esta forma fue posible obtener las concentraciones de Material Particulado y gases de combustión en cada
receptor y definir el receptor que presenta la máxima concentración para cada compuesto evaluado.

En virtud de los resultados de la modelación a continuación se presentan las concentraciones de los
contaminantes de MP 10, MP 2,5, CO, NO x y SO x, según periodos versus el valor norma de calidad primaria. Junto
a ello, el valor de la línea base de calidad de aire en área de influencia. (En caso de aplicar).

Respecto a las concentraciones modeladas, se tiene que estas son comparadas con la normativa ambiental
aplicable al Proyecto, es decir, las Normas de Calidad Primaria consideradas para la evaluación del riesgo
sobre la salud de la población identificada.

A continuación, en la siguiente Tabla se presentan los umbrales de las normas citadas.

**Tabla 15. Normas de calidad primaria**

|Normativa|Límite|Concentración|
|---|---|---|
|D.S. N° 12/2022 del MMA Norma de calidad de aire para el MP10|130 μg/m3|Diaria|
|D.S. N° 12/2022 del MMA Norma de calidad de aire para el MP10|50 μg/m3|Anual|
|D.S. N° 12/2010 del MMA Norma de calidad de aire para el MP2,5|50 μg/m3|Diaria|
|D.S. N° 12/2010 del MMA Norma de calidad de aire para el MP2,5|20 μg/m3|Anual|
|D.S. N° 104/2018 del MMA Norma Primaria de Calidad del aire para el<br>SO2|60 μg/m3|Anual|
|D.S. N° 104/2018 del MMA Norma Primaria de Calidad del aire para el<br>SO2|150 μg/m3|Diaria|
|D.S. N° 104/2018 del MMA Norma Primaria de Calidad del aire para el<br>SO2|350 μg/m3|Horaria|
|D.S. N° 114/2002 del MINSEGPRES Norma Primaria de calidad del aire<br>para NO2|400 μg/m3|1 hora|
|D.S. N° 114/2002 del MINSEGPRES Norma Primaria de calidad del aire<br>para NO2|100 μg/m3|Anual|
|D.S. N° 115/2002 del MINSEGPRES Norma Primaria de calidad del aire<br>para CO|10 mg/m3|8 horas|
|D.S. N° 115/2002 del MINSEGPRES Norma Primaria de calidad del aire<br>para CO|30 mg/m3|1 hora|

Fuente: Elaboración propia, 2025.

**7.1.** **Isoconcentración**

En las siguientes Figuras se presentan las curvas de iso concentración generadas mediante el modelo Calpuff
para los contaminantes Material Particulado Respirable (MP 10 ), Material Particulado Fino Respirable (MP 2,5 ),
Dióxido de Azufre (SO 2 ), Óxidos de Nitrógeno (NO x ) y Monóxido de Carbono (CO).

Página **58** de **73**

**Figura 71. Mapa de Isoconcentración MP** **10** **concentración promedio anual**

Fuente: Elaboración propia, 2025.

**Figura 72. Mapa de Isoconcentración MP** **10** **P98 24H**

Fuente: Elaboración propia, 2025.

Página **59** de **73**

**Figura 73. Mapa de Isoconcentración MP** **2,5** **concentración promedio anual**

Fuente: Elaboración propia, 2025.

**Figura 74. Mapa Isoconcentración MP** **2,5** **P98 24H**

Fuente: Elaboración propia, 2025.

Página **60** de **73**

**Figura 75. Mapa de Isoconcentración SO** **2** **concentración promedio anual**

Fuente: Elaboración propia, 2025.

**Figura 76. Mapa de Isoconcentración SO** **2** **, concentración promedio 24H**

Fuente: Elaboración propia, 2025.

Página **61** de **73**

**Figura 77. Mapa de Isoconcentración SO** **2** **concentración P98,5 Horario**

Fuente: Elaboración propia, 2025.

**Figura 78. Mapa de Isoconcentración NO** **X** **concentración promedio anual**

Fuente: Elaboración propia, 2025.

Página **62** de **73**

**Figura 79. Mapa de Isoconcentración NO** **X** **, concentración P99 1H**

Fuente: Elaboración propia, 2025.

**Figura 80. Mapa de Isoconcentración CO, concentración P99 1 hora**

Fuente: Elaboración propia, 2025.

Página **63** de **73**

**Figura 81. Mapa de Isoconcentración CO, concentración P99 8H**

Fuente: Elaboración propia, 2025.

**7.2.** **Aporte del Proyecto**

Para determinar el aporte del Proyecto se consideraron las concentraciones máximas registradas para los
periodos establecidos, los cuales se detallan, a continuación, en las siguientes Tablas.

**Tabla 16. Aportes del Proyecto - concentraciones máximas registradas de MP** **10**

|Receptor|Normativa|Col3|Aporte del Proyecto (μg/m3)|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**24 horas**|**Anual**|**24 horas**|**% Norma**|**Anual**|**% Norma**|
|1|130|50|5,53E-1|0,43%|1,24E-1|0,25%|
|2|130|50|5,38E-1|0,41%|1,01E-1|0,20%|
|3|130|50|4,94E-1|0,38%|5,54E-2|0,11%|
|4|130|50|6,19E-1|0,48%|1,13E-1|0,23%|

Fuente: Elaboración propia, 2025.

**Tabla 17. Aportes del Proyecto - concentraciones máximas registradas de MP** **2,5**

|Receptor|Normativa|Col3|Aporte del Proyecto (μg/m3)|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**24 horas**|**Anual**|**24 horas**|**% Norma**|**Anual**|**% Norma**|
|1|50|20|3,00E-1|0,60%|7,78E-2|0,39%|
|2|50|20|2,47E-1|0,49%|5,85E-2|0,29%|
|3|50|20|2,00E-1|0,40%|2,42E-2|0,12%|
|4|50|20|2,34E-1|0,47%|5,42E-2|0,27%|

Fuente: Elaboración propia, 2025.

Página **64** de **73**

**Tabla 18. Aportes del Proyecto - concentraciones máximas registradas de NO** **X**

|Receptor|Normativa|Col3|Aporte del Proyecto (μg/m3)|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**1 hora**|**Anual**|**1 hora**|**% Norma**|**Anual**|**% Norma**|
|1|400|100|13,83|3,46%|1,05|1,05%|
|2|400|100|11,24|2,81%|7,54E-1|0,75%|
|3|400|100|7,55|1,89%|2,41E-1|0,24%|
|4|400|100|8,73|2,18%|5,95E-1|0,60%|

Fuente: Elaboración propia, 2025.

**-**
**Tabla 19. Aportes del Proyecto** **concentraciones máximas registradas de CO**

|Receptor|Normativa|Col3|Aporte del Proyecto (μg/m3)|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**1 hora**|**8 horas**|**1 hora**|**% Norma**|**8 horas**|**% Norma**|
|1|30.000|10.000|5,95|0,02%|3,44|0,03%|
|2|30.000|10.000|5,06|0,02%|2,98|0,03%|
|3|30.000|10.000|4,37|0,01%|2,82|0,03%|
|4|30.000|10.000|5,21|0,02%|3,21|0,03%|

Fuente: Elaboración propia, 2025.

**Tabla 20. Aportes del Proyecto - concentraciones máximas registradas de SO** **2**

|Receptor|Normativa|Col3|Col4|Aporte del Proyecto (μg/m3)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Horario**|**Diario**|**Anual**|**Horario**|**% Norma**|**Diario**|**% Norma**|**Anual**|**% Norma**|
|1|350|150|60|1,98E-2|0,01%|6,31E-3|0,00%|1,49E-3|0,00%|
|2|350|150|60|1,67E-2|0,00%|4,91E-3|0,00%|1,11E-3|0,00%|
|3|350|150|60|1,18E-2|0,00%|3,77E-3|0,00%|4,00E-4|0,00%|
|4|350|150|60|1,45E-2|0,00%|3,99E-3|0,00%|9,28E-4|0,00%|

Fuente: Elaboración propia, 2025.

Se puede observar que las concentraciones generadas por el Proyecto se mantienen por debajo de los límites
establecidos en la normativa de calidad de aire primaria para los compuestos evaluados, teniendo que las
emisiones son poco significativas, debido a que se encuentran alejados de los valores establecidos en la
normativa aplicable.

**7.3.** **Evaluación del impacto de las emisiones atmosféricas del material particulado MP** **10** **y**

**MP** **2,5** **en zonas saturadas**

La Guía “Criterio de evaluación en el SEIA: Impacto de emisiones en zonas saturadas por material particulado
respirable MP 10 y material particulado fino respirable MP 2,5 ” en adelante la “Guía”, establece los criterios para
definir el concepto de “aumento o disminución significativos”, concepto contenido en el literal a) del artículo 5°
del Reglamento del SEIA, para la evaluación del riesgo para la salud y el uso de normas primarias de calidad
ambiental vigentes.

El presente Proyecto se ubica en la Región del Libertador General Bernardo O’Higgins, la cual se encuentra
declarada como saturada por MP 10, como concentración anual y de 24 horas según D.S N°7/2009 y saturada
por MP 2,5 como concentración anual y de 24 horas según D.S. N°42/2017

Página **65** de **73**

**Figura 82. Ubicación del Proyecto en relación con la zona saturada o latente**

Fuente: Capítulo 1 “Descripción de Proyecto”, 2025.

Las emisiones del Proyecto, de acuerdo con el inventario de emisiones, se presenta en la siguiente Tabla:

**Tabla 21. Resumen de Emisiones del Proyecto**

|Año|Detalle|Tasa de emisión (Ton/año)|Col4|
|---|---|---|---|
|**Año**|**Detalle**|**MP10**|**MP2,5**|
|5|Construcción Etapa 3 + Operación Etapa 1 y 2|1,415|0,346|

Fuente: Elaboración propia, 2025.

Como se puede apreciar, el escenario más desfavorable en cuanto a la generación de emisiones atmosféricas
corresponde al año 5, y dada la duración del impacto de 12 meses, corresponde evaluar la significancia con la

Tabla 2 de la Guía.

**Tabla 22. Comparación de los resultados de la modelación en receptores humanos y valores de significancia de**

**la Tabla 2 de la Guía, para el primer año del Proyecto**

|Receptores|MP (ug/m3)<br>10|Col3|MP 2,5(ug/m3)|Col5|
|---|---|---|---|---|
|**Receptores**|**24 H P98**|**Anual**|**24 H P98**|**Anual**|
|1|5,53E-1|1,24E-1|3,00E-1|7,78E-2|
|2|5,38E-1|1,01E-1|2,47E-1|5,85E-2|
|3|4,94E-1|5,54E-2|2,00E-1|2,42E-2|
|4|6,19E-1|1,13E-1|2,34E-1|5,42E-2|
|**Valor significancia (Tabla-2, 12 meses)**|**10,00**|**3,00**|**5,13**|**0,99**|

Fuente: Elaboración propia, 2025.

De acuerdo con la Tabla anterior, la concentración de material particulado de MP 10 y MP 2,5 en los receptores
humanos, se encuentra **por debajo de los valores de significancia establecidos para la Tabla 2, para 12**
**meses de la Guía durante el año 5, el año que el Proyecto genera la mayor cantidad de emisión.**

Página **66** de **73**

**7.4.** **Evaluación del efecto sinérgico**

Para el desarrollo del escenario sinérgico, se han considerado los siguientes criterios:

 Identificación del Proyectos aprobados en el SEIA cercanos en un radio de 2 km del Proyecto en

evaluación

 RCA aprobada no mayor a 5 años. Se asume que mayor a esos años los proyectos ya estarían
operando y, por lo tanto, las emisiones estarían siendo registradas en la estación de calidad del aire.

 Revisión del estado en que se encuentran los proyectos aprobados en el sitio web de SMA/SNIFA

 Efectuar el análisis de la información, basado en los antecedentes disponibles entregados por los
titulados de los proyectos aprobados

 - Los contaminantes considerados para el análisis de escenario sinérgico corresponden al MP 10 y MP 2,5

A continuación, se presenta el listado de proyectos identificado en el SEIA, según los criterios mencionados.

**Tabla 23. Proyectos Aprobados o en Calificación Ambiental en las cercanías al Proyecto Planta Solar El Cardonal**

|ID|Nombre|Titular|Fecha<br>Ingreso al<br>Sistema|Estado|Distancia al<br>Proyecto|
|---|---|---|---|---|---|
|1|Parrones de Baquedano|Inmobiliaria<br>San<br>Ramón I SPA|07/10/2021|Aprobado|0,94 km|

Fuente: Elaboración propia, 2025.

A continuación, en la siguiente Tabla se evalúa si existe solapamiento entre las fases de construcción de los
proyectos citados anteriormente.

**Tabla 24. Evaluación de solapamiento fase de construcción**

|Proyecto|Fecha de inicio|Fecha de término|¿Existe solapamiento?|
|---|---|---|---|
|Parrones de Baquedano|Primer semestre<br>2022|Segundo semestre 2024|No|

Fuente: Elaboración propia, 2025.

De lo anterior, se tiene que para el proyecto “Parrones de Baquedano” sólo se considerarán las emisiones
generadas durante su fase de operación.

A continuación, en la siguiente Tabla se presentan las tasas a considerar para el análisis del efecto sinérgico
del Proyecto.

**Tabla 25. Tasas de emisión a considerar para la evaluación del efecto sinérgico**

|Proyecto|Tasa de emisión (ton/año)|Col3|Fuente|
|---|---|---|---|
|**Proyecto**|**MP10**|**MP2,5**|**MP2,5**|
|Parrones de Baquedano|0,4826|0,1173|Anexo 3 ADENDA<br>Complementaria|

Fuente: Elaboración propia, 2025.

Para evaluar los efectos se realiza una modelación de los receptores discretos del Presenta Proyecto para el
MP 10 y MP 2,5, donde se obtienen los siguientes resultados.

Página **67** de **73**

**Tabla 26. Resultados aporte proyectos cercanos en receptores**

|Receptor|Métrica|Aporte proyecto cercanos (μg/m3)|Col4|D.S. N° 12/2022<br>del MMA|D.S. N° 12/2011<br>del MMA|
|---|---|---|---|---|---|
|**Receptor**|**Métrica**|**MP10**|**MP2,5**|**Límite MP10 **<br>**(μg/m3) **|**Límite MP2,5 **<br>**(μg/m3) **|
|1|Anual|7,26E-2|1,77E-2|50|20|
|1|Diaria|2,92E-1|7,09E-2|130|50|
|2|Anual|1,18E-1|2,86E-2|50|20|
|2|Diaria|5,04E-1|1,23E-1|130|50|
|3|Anual|1,33E-1|3,24E-2|50|20|
|3|Diaria|6,28E-1|1,53E-1|130|50|
|4|Anual|4,80E-2|1,17E-2|50|20|
|4|Diaria|2,16E-1|5,24E-2|130|50|

Fuente: Elaboración propia, 2025.

 - **Aporte de MP** **10**

Los aportes de MP 10 generados por proyecto cercanos en todos los receptores evaluados en la presente
evaluación son bajos, con valores que oscilan en el orden de los -2 al -1 en términos anuales y diarios, los
cuales están por muy por debajo de los límites establecidos por la normativa (50 μg/m3 anual y 130 μg/m3
diario). Por lo mismo, se concluye que, el impacto de las emisiones de proyectos cercanos en los niveles de
MP 10 es poco significativo.

 - **Aporte de MP** **2,5**

De igual manera, para el MP 2,5 también se tiene que los aportes de los proyectos cercanos son mínimos,
teniendo valores diarios y anuales del orden de los -1 y -2, resultados que están muy por debajo de los límites
normativos (20 μg/m3 anual y 50 μg/m3 diario).

Por lo tanto, se tiene que, las emisiones generadas por otros proyectos son poco significativas y despreciables,
dado que los valores obtenidos en los receptores de la presente evaluación se encuentran muy por debajo de
los límites normativos establecidos en el D.S. N° 12/2022 del MMA para el MP 10 y el D.S. N° 12/2011 del MMA
para el MP 2,5 . Por ende, se desestima la implementación de medidas adicionales de mitigación y coordinación
asociadas a efectos sinérgicos con otros Proyectos.

**7.5.** **Evaluación de los niveles de concentración**

Para evaluar los niveles de concentración de los contaminantes generados como resultados del quinto año del
Proyecto, se realizará una comparación entre estos valores, la condición basal obteniendo a partir de la estación
Rancagua II (Caracterización de calidad del aire obtenidos del SINCA), así como con la normativa primaria
correspondiente a la calidad ambiental y el aporte de otros proyectos. Es preciso indicar que dicha estación no
presenta datos de SO 2, NO x y CO, por lo que la comparativa se realizará en función del MP 10 y MP 2,5 .

La concentración total se obtendrá sumando la línea de base proveniente de la estación Rancagua II, proyectos
cercanos y la contribución adicional del proyecto en los receptores de interés definidos, de acuerdo con la
siguiente formulación:

Concentración Total= Línea de base+ Aporte Total del Proyecto+ Aporte de otros Proyectos

Página **68** de **73**

**Tabla 27. Concentraciones totales de MP** **10**

|Receptores|Coordenadas UTM<br>(m)|Col3|Métrica|Condición o<br>línea de base<br>(μg/m3)|Aporte<br>proyecto<br>(μg/m3)|Aporte otros<br>proyectos con<br>RCA (μg/m3)|Concentración<br>final (μg/m3)|Norma|
|---|---|---|---|---|---|---|---|---|
|**Receptores**|**Este**|**Norte**|**Norte**|**A **|**B **|**C **|**A + B +C**|**A + B +C**|
|1|337.026|6.218.934|Anual|49,16|1,24E-01|7,26E-02|49,36|50|
|1|337.026|6.218.934|24 H|145,96|5,53E-01|2,92E-01|146,81|130|
|2|336.990|6.218.793|Anual|49,16|1,01E-01|1,18E-01|49,38|50|
|2|336.990|6.218.793|24 H|145,96|5,38E-01|5,04E-01|147,00|130|
|3|337.023|6.218.680|Anual|49,16|5,54E-02|1,33E-01|49,35|50|
|3|337.023|6.218.680|24 H|145,96|4,94E-01|6,28E-01|147,08|130|
|4|337.194|6.218.998|Anual|49,16|1,13E-01|4,80E-02|49,32|50|
|4|337.194|6.218.998|24 H|145,96|6,19E-01|2,16E-01|146,80|130|

Fuente: Elaboración propia, 2025.

**Tabla 28. Concentraciones totales de MP** **2,5**

|Receptores|Coordenadas UTM<br>(m)|Col3|Métrica|Condición o<br>línea de base<br>(μg/m3)|Aporte<br>proyecto<br>(μg/m3)|Aporte otros<br>proyectos con<br>RCA (μg/m3)|Concentración<br>final (μg/m3)|Norma|
|---|---|---|---|---|---|---|---|---|
|**Receptores**|**Este**|**Norte**|**Norte**|**A **|**B **|**C **|**A + B +C**|**A + B +C**|
|1|337.026|6.218.934|Anual|25,58|7,78E-02|1,77E-02|25,68|20|
|1|337.026|6.218.934|24 H|87|3,00E-01|7,09E-02|87,37|50|
|2|336.990|6.218.793|Anual|25,58|5,85E-02|2,86E-02|25,67|20|
|2|336.990|6.218.793|24 H|87|2,47E-01|1,23E-01|87,37|50|
|3|337.023|6.218.680|Anual|25,58|2,42E-02|3,24E-02|25,64|20|
|3|337.023|6.218.680|24 H|87|2,00E-01|1,53E-01|87,35|50|
|4|337.194|6.218.998|Anual|25,58|5,42E-02|1,17E-02|25,65|20|
|4|337.194|6.218.998|24 H|87|2,34E-01|5,24E-02|87,29|50|

Fuente: Elaboración propia, 2025.

**Tabla 29. Concentraciones totales de NO** **x**

|Receptores|Coordenadas UTM<br>(m)|Col3|Métrica|Condición o<br>línea de base<br>(μg/m3)|Aporte<br>proyecto<br>(μg/m3)|Aporte otros<br>proyectos con<br>RCA (μg/m3)|Concentración<br>final (μg/m3)|Norma|
|---|---|---|---|---|---|---|---|---|
|**Receptores**|**Este**|**Norte**|**Norte**|**A **|**B **|**C **|**A + B +C**|**A + B +C**|
|1|337.026|6.218.934|Anual|-|1,05|-|1,05|100|
|1|337.026|6.218.934|1H|-|13,83|-|13,83|400|
|2|336.990|6.218.793|Anual|-|7,54E-01|-|0,754|100|
|2|336.990|6.218.793|1H|-|11,24|-|11,24|400|
|3|337.023|6.218.680|Anual|-|2,41E-01|-|0,241|100|
|3|337.023|6.218.680|1H|-|7,55|-|7,55|400|
|4|337.194|6.218.998|Anual|-|5,95E-01|-|0,595|100|
|4|337.194|6.218.998|1H|-|8,73|-|8,73|400|

Fuente: Elaboración propia, 2025.

**Tabla 30. Concentraciones totales de CO**

|Receptores|Coordenadas UTM<br>(m)|Col3|Métrica|Condición o<br>línea de base<br>(μg/m3)|Aporte<br>proyecto<br>(μg/m3)|Aporte otros<br>proyectos con<br>RCA (μg/m3)|Concentración<br>final (μg/m3)|Norma|
|---|---|---|---|---|---|---|---|---|
|**Receptores**|**Este**|**Norte**|**Norte**|**A **|**B **|**C **|**A + B +C**|**A + B +C**|
|1|337.026|6.218.934|8 H|-|3,44|-|3,44|10.000|
|1|337.026|6.218.934|1 H|-|5,95|-|5,95|30.000|
|2|336.990|6.218.793|8 H|-|2,98|-|2,98|10.000|
|2|336.990|6.218.793|1 H|-|5,06|-|5,06|30.000|
|3|337.023|6.218.680|8 H|-|2,82|-|2,82|10.000|
|3|337.023|6.218.680|1 H|-|4,37|-|4,37|30.000|
|4|337.194|6.218.998|8 H|-|3,21|-|3,21|10.000|
|4|337.194|6.218.998|1 H|-|5,21|-|5,21|30.000|

Fuente: Elaboración propia, 2025.

Página **69** de **73**

**Tabla 31. Concentraciones totales de SO** **2**

|Receptores|Coordenadas UTM<br>(m)|Col3|Métrica|Condición o<br>línea de base<br>(μg/m3)|Aporte<br>proyecto<br>(μg/m3)|Aporte otros<br>proyectos con<br>RCA (μg/m3)|Concentración<br>final (μg/m3)|Norma|
|---|---|---|---|---|---|---|---|---|
|**Receptores**|**Este**|**Norte**|**Norte**|**A **|**B **|**C **|**A + B +C**|**A + B +C**|
|1|337.026|6.218.934|Anual|-|1,49E-03|-|0,00149|60|
|1|337.026|6.218.934|24 H|-|6,31E-03|-|0,00631|150|
|1|337.026|6.218.934|1 H|-|1,98E-02|-|0,0198|350|
|2|336.990|6.218.793|Anual|-|1,11E-03|-|0,00111|60|
|2|336.990|6.218.793|24 H|-|4,91E-03|-|0,00491|150|
|2|336.990|6.218.793|1 H|-|1,67E-02|-|0,0167|350|
|3|337.023|6.218.680|Anual|-|4,00E-04|-|0,0004|60|
|3|337.023|6.218.680|24 H|-|3,77E-03|-|0,00377|150|
|3|337.023|6.218.680|1 H|-|1,18E-02|-|0,0118|350|
|4|337.194|6.218.998|Anual|-|9,28E-04|-|0,000928|60|
|4|337.194|6.218.998|24 H|-|3,99E-03|-|0,00399|150|
|4|337.194|6.218.998|1 H|-|1,45E-02|-|0,0145|350|

Fuente: Elaboración propia, 2025.

Página **70** de **73**

**7.6.** **Área de influencia**

El objetivo de determinar el Área de Influencia (AI) de Calidad del Aire es proporcionar la información necesaria
para descartar cualquier posible impacto en la población.

A continuación, se presenta la definición de Área de Influencia, cuyo criterio principal es abarcar el área
geográfica, donde se encuentran los receptores de interés, que podrían verse potencialmente afectadas por las
emisiones del Proyecto.

El área de influencia simulada para el Proyecto se evaluó utilizando la concentración percentil 99 de NO X
horario, obteniéndose como resultado que el área de influencia llega a concentraciones de 1 μg/m [3], esto
considera un área de aproximadamente 96,5 ha, la cual considera todos los receptores de interés.

A continuación, en la siguiente Figura se presenta el área de influencia del Proyecto para la componente aire
(emisiones atmosféricas).

**Figura 83. Área de influencia del Proyecto, componente aire (emisiones atmosféricas)**

Fuente: Elaboración propia, 2025.

# 8. Consideraciones

La base de datos meteorológica y geográfica utilizada para la modelación fue adquirida de una empresa
especializada en modelación para servicios de evaluación ambiental, dado que el análisis de incertidumbre
muestra que la base de datos utilizada cumple con todas las condiciones establecidas por el Servicio de
Evaluación Ambiental (SEA).

Cabe mencionar que, el Proyecto se ubica en la Región del Libertador General Bernardo O’Higgins, la cual se
encuentra declarada como saturada por MP 10, como concentración anual y de 24 horas según D.S N°7/2009 y
saturada por MP 2,5 como concentración anual y de 24 horas según D.S. N°42/2017.

Página **71** de **73**

# 9. Conclusiones

El documento realizado proporcionó una evaluación de la concentración de emisiones generadas durante el
primer año de construcción del Proyecto “Proyecto Parque Las Alamedas I, II y III” (correspondiente al año en
que el Proyecto genera la mayor cantidad de emisiones, con el fin de evaluar un escenario desfavorable). En
este estudio, se modelaron las emisiones de MP 10 y MP 2,5, así como los gases NO X, SO 2 y CO. El objetivo fue
determinar las concentraciones de estos contaminantes en la atmósfera, evaluar su contribución a la línea de
base y prever posibles efectos negativos en la salud de las personas.

Se utilizó una grilla de 50 km X 50 km, tanto para la modelación de emisiones como para el modelo
meteorológico WRF, con una resolución de 1 km.

En el Apéndice N°1 se presenta la planilla con el inventario de emisiones utilizado de INPUT del modelo.

En el Apéndice N° 2 del informe se encuentra una descripción detallada del modelo CALPUFF, incluyendo el
archivo CALPUFF.INP, que es utilizado como archivo de control para el escenario de modelado.
Adicionalmente, se incorporan los archivos de modelación utilizados para evaluar el efecto sinérgico de
proyectos cercanos.

En el Apéndice N° 3 se incluye un archivo KMZ con el área de influencia del Proyecto, la cual incluye todos los
receptores evaluados, en el presente documento.

Se realizó un análisis de incertidumbre del modelo meteorológico, tanto cualitativo como cuantitativo. En las
variables consideradas, dirección del viento, velocidad del viento, porcentaje de humedad, rosa de los vientos
y temperatura se observaron comportamientos similares que indican que los archivos WRF son representativos.

Para determinar la condición basal del área de emplazamiento del Proyecto se utilizó la información
proporcionada por la estación Rancagua II. Para el MP 10 se registró un cumplimiento del 98,33% de la norma
anual y un 112,27% de la norma diaria. En el caso del MP 2,5, se tiene un 127,9% de la norma anual y un 174%
de la norma diaria. Es fundamental destacar que las emisiones de la condición basal no están relacionadas con
el Proyecto, ya que corresponden exclusivamente a la línea base actual de la zona, influenciada por fuentes de
contaminación preexistentes.

Se realizó una modelación de material particulado (MP 10 y MP 2,5 ) y gases se combustión, utilizando la situación
más desfavorable, correspondiente al quinto año del Proyecto, donde se consideró un total de 1,42 ton/año de
MP 10, 0,35 ton/año de MP 2,5, 1,10 ton/año de NO x, 0,01 ton/año de SO 2 y 2,67 ton/año de CO.

De acuerdo con los resultados obtenidos, se tienen las siguientes conclusiones por categoría y contaminantes:

- **MP** **10** **:** El mayor aporte promedio diario de MP 10 corresponde al **Receptor 4**, con una concentración de **0,62**
**μg/m3** diario y el **Receptor 1** con **0,12 μg/m3** anual. Estos valores representan solo el **0,48%** de la norma diaria
(130 μg/m3) y el **0,25%** de la norma anual (50 μg/m3). Esto significa que el aporte del proyecto está
un **99,52%** por debajo del límite diario y un **99,75%** por debajo del límite anual.

- **MP** **2,5** **:** El mayor aporte de MP 2,5 se registra en el **Receptor 1** con una concentración de **0,30 μg/m3** diario
y **0,078 μg/m3** anual. Estos valores equivalen al **0,60%** de la norma diaria (50 μg/m3) y al **0,39%** de la norma
anual (20 μg/m3), lo que indica que el aporte del proyecto está un **99,40%** por debajo del límite diario y
un **99,61%** por debajo del límite anual.

Página **72** de **73**

**1.** **Gases de combustión (NO** **x** **, SO** **2** **y CO)**

- **NO** **x** **:** El **Receptor 1** recibe el mayor aporte de NO x, con una concentración de **13,83 μg/m3** horario y **1,05**
**μg/m3** anual. Estos valores corresponden al **3,46%** de la norma horaria (400 μg/m3) y al **1,05%** de la norma
anual (100 μg/m3), lo que significa que el aporte del proyecto está un **96,54%** por debajo del límite horario y
un **98,95%** por debajo del límite anual.

- **CO:** En el caso del CO, el **Receptor 1** recibe un aporte de **5,95 μg/m3** horario y **3,44 μg/m3** cada 8 horas.
Estos valores representan solo el **0,02%** de la norma horaria (30.000 μg/m3) y el **0,03%** de la norma cada 8
horas (10.000 μg/m3), lo que indica que el aporte del proyecto está un **99,98%** y **99,97%** por debajo de los
límites respectivos.

- **SO** **2** **:** Para el dióxido de azufre (SO 2 ), el mayor aporte lo recibe el **Receptor 1**, con una concentración de **0,019**
**μg/m3** horario, equivalente al **0,01%** de la norma horaria (350 μg/m3), un aporte de **0,006 μg/m3** diario con un
**0,004%** de la norma diaria (150 μg/m3) y **0,0015 μg/m3** anual con un **0,002%** de la norma horaria (20 μg/m3).
Esto significa que el aporte del Proyecto está un **99,99%,** **99,99%** y **99,99%** por debajo de los límites horario,
diario y anual, respectivamente.

Es relevante mencionar que, la estación de calidad de aire utilizada para evaluar la condición basal, corresponde
a la estación Rancagua II y se encuentra a aproximadamente 3,03 km del Proyecto, siendo la estación más
cercana al Proyecto con datos válidos, la cual cumple con el criterio mínimo de contar con un 75% de los datos,
de acuerdo con el numeral 4.3.1 de la Guía para el uso de modelos de Calidad del Aire en el SEIA

Respecto a la evaluación del impacto de las emisiones atmosféricas del material particulado respirable MP 10 y
MP 2,5 en zonas saturadas, se tiene que el escenario más desfavorable corresponde al quinto año de ejecución
del Proyecto. Además, se evalúan las emisiones resultantes de la modelación, obteniendo que el receptor 1
posee los valores más altos para el MP 10 y el MP 2,5 . No obstante, estos se encuentran muy por debajo de lo
establecido en la Tabla 2 de la Guía “Criterio de evaluación en el SEIA: Impacto de emisiones en zonas
saturadas por material particulado respirable MP 10 y material particulado respirable fino MP 2,5 ”.

**En base a lo anterior, se puede inferir que el Proyecto no genera una alteración significativa y negativa**

**en la calidad del aire en la condición basal.**

**En conclusión, es preciso indicar que de acuerdo con los resultados y posteriores análisis no se detecta**
**la presencia de riesgos para la salud de la población en materia de calidad del aire asociado a**
**actividades, obras y acciones del Proyecto, incluso evaluando el escenario más desfavorable, por lo**
**que dado lo acotado del área de intervención y la temporalidad de las actividades del Proyecto se tiene**
**que están no superarán las normas primarias de calidad vigentes, estando en conformidad con el**

**Artículo 5° del D.S. N°40/2012.**

Página **73** de **73**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Límites anual y diario MP** **10** **y MP** **2,5****

| Nivel | MP (μg/m3)<br>10 | MP (μg/m3)<br>2,5 |
| --- | --- | --- |
| Límite anual | 50 | 20 |
| Límite diario | 130 | 50 |
| Normativa | D.S. N° 12/2022 | D.S. N° 12/2011 del MMA |

**Tabla 2.: Límites anual y diario SO** **2****

| Nivel | SO (μg/m3)<br>2 |
| --- | --- |
| Límite anual | 60 |
| Límite diario | 150 |
| Límite horario | 350 |
| Normativa | D.S. N° 104/2019 del MMA |

**Tabla 3.: Límites anual y diario de NO** **2****

| Nivel | NO (μg/m3)<br>2 |
| --- | --- |
| Límite anual | 100 |
| Límite horario | 400 |
| Normativa | D.S. N° 114/2002 del MINSEGPRES |

**Tabla 4.: Límites anual y diario de CO****

| Nivel | CO (mg/m3N) |
| --- | --- |
| Límite horario | 30 |
| Límite 8 horas | 10 |
| Normativa | D.S. N° 115/2002 del MINSEGPRES |

**Tabla 5.: Receptores discretos en el área del Proyecto****

| Receptores | Descripción | Altura de<br>receptor (m) | Distancia<br>Proyecto<br>(m) | Coordenadas UTM Huso<br>19S | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Receptores** | **Descripción** | **Altura de**<br>**receptor (m)** | **Distancia**<br>**Proyecto**<br>**(m)** | **Este** | **Norte** |
| R1 | Galpón Material ligero de un piso | 1,5 | 19 | 337.026 | 6.218.934 |
| R2 | Edificio Material solido de 8 pisos | 1,5 - 19 | 5 | 336.990 | 6.218.793 |
| R3 | Edificio Material solido de 8 pisos | 1,5 - 19 | 22 | 337.023 | 6.218.680 |
| R4 | Jardín infantil de material solido de un piso | 1,5 | 117 | 337.194 | 6.218.998 |

**Tabla 7.: Fuentes de emisión del Proyecto****

| Cod. de la<br>fuente | Fuente | Superficie/longitud de la<br>fuente | Actividades incluidas en las<br>fuentes | Emisiones (ton/año) | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Cod. de la**<br>**fuente** | **Fuente** | **Superficie/longitud de la**<br>**fuente** | **Actividades incluidas en las**<br>**fuentes** | **MP10** | **MP2,5** | **NOX ** | **SO2 ** | **CO ** |
| SCR_1 | Difusa | 42.388,6 m2 | Movimiento de tierra | 0,07 | 0,05 | 0,77 | 0,00 | 0,27 |
| SCR_2 | Móvil | 7,24 km | Caminos no pavimentados<br>construcción | 0,38 | 0,04 | 0,00 | 0,00 | 0,00 |
| SCR_3 | Móvil | 133,8 km | Caminos pavimentados construcción | 0,10 | 0,05 | 0,12 | 0,00 | 0,05 |
| SCR_4 | Difusa | 9.287 m2 | Escarpe | 0,02 | 0,00 | 0,00 | 0,00 | 0,00 |
| SCR_5 | Móvil | 4,67 km | Rutas pavimentadas operación | 0,85 | 0,21 | 0,10 | 0,00 | 2,66 |

**Tabla 8.: Parámetros de entrada al modelo****

| Fuente | Col2 | Tipo de fuente | Largo (km) | Área (m2) | Unidad de tasas<br>de emisión |
| --- | --- | --- | --- | --- | --- |
| **Nombre** | **Nombre en modelo** | **Nombre en modelo** | **Nombre en modelo** | **Nombre en modelo** | **Nombre en modelo** |
| SCR_1 | Movimiento de tierra | AREA-POLYGONAL | - | 42.388,7 m2 | g/m2·s |
| SCR_2 | Tránsito caminos no<br>pavimentados | ROAD | 7,24 km | - | g/m·s |
| SCR_3 | Tránsito caminos<br>pavimentados | ROAD | 133,80 km | - | g/m·s |
| SCR_4 | Escarpe | AREA-POLYGONAL | - | 9.287 m2 | g/m2·s |
| SCR_5 | Rutas pavimentadas<br>operación | ROAD | 4,67 km | - | g/m·s |
| SCR_ | Grupo electrógeno | AREA-CIRCULAR | - | 15 | g/m2·s |

**Tabla 9.: Estación utilizada para la validación del modelo WRF****

| Estación | Parámetro | Coordenadas UTM | Col4 | Variables<br>utilizadas | Periodo |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Parámetro** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| Rancagua I | Meteorológicos | 342.015 | 6.218.523 | Velocidad del<br>viento | 2024 |
| Rancagua I | Meteorológicos | 342.015 | 6.218.523 | Humedad | Humedad |
| Rancagua I | Meteorológicos | 342.015 | 6.218.523 | Dirección del<br>viento | Dirección del<br>viento |
| Rancagua I | Meteorológicos | 342.015 | 6.218.523 | Temperatura | Temperatura |
| Rancagua II | Meteorológicos | 339.842 | 6.220.527 | Velocidad del<br>viento | 2024 |
| Rancagua II | Meteorológicos | 339.842 | 6.220.527 | Humedad | Humedad |
| Rancagua II | Meteorológicos | 339.842 | 6.220.527 | Dirección del<br>viento | Dirección del<br>viento |

**Tabla 10.: Estadísticos de sesgo, error absoluto medio y error cuadrático medio****

| Estación | Variable meteorológica | BIAS | MAE | RMSE | r |
| --- | --- | --- | --- | --- | --- |
| Rancagua I | Velocidad del viento (m/s) | -0,56 | 0,58 | 0,79 | 0,90 |
| Rancagua I | Temperatura (°C) | -1,57 | -1,57 | 1,90 | 0,97 |
| Rancagua II | Velocidad del viento (m/s) | -0,48 | 0,48 | 0,67 | 0,93 |
| Rancagua II | Temperatura (°C) | -1,96 | 1,96 | 2,4 | 0,98 |
| Límite* | Velocidad del viento (m/s) | (-2,5;2,5) (m/s) | ≤ 3 (m/s) | ≤ 3,5 (m/s) | >0,6 |
| Límite* | Temperatura (°C) | (-4,4) (°C) | ≤ 4 (°C) | ≤ 4,5 (°C) | >0,8 |
| *Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”, Guía para el uso de modelos<br>de Calidad del Aire en el SEIA. | *Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”, Guía para el uso de modelos<br>de Calidad del Aire en el SEIA. | *Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”, Guía para el uso de modelos<br>de Calidad del Aire en el SEIA. | *Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”, Guía para el uso de modelos<br>de Calidad del Aire en el SEIA. | *Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”, Guía para el uso de modelos<br>de Calidad del Aire en el SEIA. | *Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”, Guía para el uso de modelos<br>de Calidad del Aire en el SEIA. |

**Tabla 11.: Concentración Media Anual de MP** **10** **(ug/m** **[3]** **N)****

| Estación | Norma primaria de MP (D.S. N° 12/2021 del MMA) - Media Anual<br>10 | Col3 | Col4 | Trianual | Porcentaje de la<br>norma |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 50 (ug/m3N)** | **Valor Norma: 50 (ug/m3N)** | **Valor Norma: 50 (ug/m3N)** | **Valor Norma: 50 (ug/m3N)** | **Valor Norma: 50 (ug/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2022** | **2023** | **2024** | **2024** | **2024** |
| Rancagua II | 43,81 | 44,93 | 58,74 | 49,16 | 98,33% |

**Tabla 12.: Percentil 98 concentración 24 horas de MP** **10** **(ug/m** **[3]** **N)****

| Estación | Norma primaria de MP (D.S. N° 12/2021 del MMA) - 24 H<br>10 | Porcentaje de la norma |
| --- | --- | --- |
| **Estación** | **Valor norma: 130 (ug/m3N)** | **Valor norma: 130 (ug/m3N)** |
| **Estación** | **Año** | **Año** |
| **Estación** | **2024** | **2024** |
| Rancagua II | 145,96 | 112,27% |

**Tabla 13.: Concentración Media Anual de MP** **2,5** **(ug/m** **[3]** **N)****

| Estación | Norma primaria de MP (D.S. N° 12/2021 del MMA) - Media Anual<br>2,5 | Col3 | Col4 | Trianual | Porcentaje de la<br>norma |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 20 (ug/m3N)** | **Valor Norma: 20 (ug/m3N)** | **Valor Norma: 20 (ug/m3N)** | **Valor Norma: 20 (ug/m3N)** | **Valor Norma: 20 (ug/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2022** | **2023** | **2024** | **2024** | **2024** |
| Rancagua II | 29,63 | 22,96 | 24,14 | 25,58 | 127,90% |

**Tabla 14.: Percentil 98 concentración 24 horas de MP** **2,5** **(ug/m** **[3]** **N)****

| Estación | Norma primaria de MP (D.S. N° 12/2011 del MMA) - 24 H<br>2,5 | Porcentaje de la norma |
| --- | --- | --- |
| **Estación** | **Valor norma: 50 (ug/m3N)** | **Valor norma: 50 (ug/m3N)** |
| **Estación** | **Año** | **Año** |
| **Estación** | **2024** | **2024** |
| Rancagua II | 87 | 174% |

**Tabla 15.: Normas de calidad primaria****

| Normativa | Límite | Concentración |
| --- | --- | --- |
| D.S. N° 12/2022 del MMA Norma de calidad de aire para el MP10 | 130 μg/m3 | Diaria |
| D.S. N° 12/2022 del MMA Norma de calidad de aire para el MP10 | 50 μg/m3 | Anual |
| D.S. N° 12/2010 del MMA Norma de calidad de aire para el MP2,5 | 50 μg/m3 | Diaria |
| D.S. N° 12/2010 del MMA Norma de calidad de aire para el MP2,5 | 20 μg/m3 | Anual |
| D.S. N° 104/2018 del MMA Norma Primaria de Calidad del aire para el<br>SO2 | 60 μg/m3 | Anual |
| D.S. N° 104/2018 del MMA Norma Primaria de Calidad del aire para el<br>SO2 | 150 μg/m3 | Diaria |
| D.S. N° 104/2018 del MMA Norma Primaria de Calidad del aire para el<br>SO2 | 350 μg/m3 | Horaria |
| D.S. N° 114/2002 del MINSEGPRES Norma Primaria de calidad del aire<br>para NO2 | 400 μg/m3 | 1 hora |
| D.S. N° 114/2002 del MINSEGPRES Norma Primaria de calidad del aire<br>para NO2 | 100 μg/m3 | Anual |
| D.S. N° 115/2002 del MINSEGPRES Norma Primaria de calidad del aire<br>para CO | 10 mg/m3 | 8 horas |
| D.S. N° 115/2002 del MINSEGPRES Norma Primaria de calidad del aire<br>para CO | 30 mg/m3 | 1 hora |

**Tabla 16.: Aportes del Proyecto - concentraciones máximas registradas de MP** **10****

| Receptor | Normativa | Col3 | Aporte del Proyecto (μg/m3) | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **24 horas** | **Anual** | **24 horas** | **% Norma** | **Anual** | **% Norma** |
| 1 | 130 | 50 | 5,53E-1 | 0,43% | 1,24E-1 | 0,25% |
| 2 | 130 | 50 | 5,38E-1 | 0,41% | 1,01E-1 | 0,20% |
| 3 | 130 | 50 | 4,94E-1 | 0,38% | 5,54E-2 | 0,11% |
| 4 | 130 | 50 | 6,19E-1 | 0,48% | 1,13E-1 | 0,23% |

**Tabla 17.: Aportes del Proyecto - concentraciones máximas registradas de MP** **2,5****

| Receptor | Normativa | Col3 | Aporte del Proyecto (μg/m3) | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **24 horas** | **Anual** | **24 horas** | **% Norma** | **Anual** | **% Norma** |
| 1 | 50 | 20 | 3,00E-1 | 0,60% | 7,78E-2 | 0,39% |
| 2 | 50 | 20 | 2,47E-1 | 0,49% | 5,85E-2 | 0,29% |
| 3 | 50 | 20 | 2,00E-1 | 0,40% | 2,42E-2 | 0,12% |
| 4 | 50 | 20 | 2,34E-1 | 0,47% | 5,42E-2 | 0,27% |

**Tabla 18.: Aportes del Proyecto - concentraciones máximas registradas de NO** **X****

| Receptor | Normativa | Col3 | Aporte del Proyecto (μg/m3) | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **1 hora** | **Anual** | **1 hora** | **% Norma** | **Anual** | **% Norma** |
| 1 | 400 | 100 | 13,83 | 3,46% | 1,05 | 1,05% |
| 2 | 400 | 100 | 11,24 | 2,81% | 7,54E-1 | 0,75% |
| 3 | 400 | 100 | 7,55 | 1,89% | 2,41E-1 | 0,24% |
| 4 | 400 | 100 | 8,73 | 2,18% | 5,95E-1 | 0,60% |

**Tabla 19.: Aportes del Proyecto** **concentraciones máximas registradas de CO****

| Receptor | Normativa | Col3 | Aporte del Proyecto (μg/m3) | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **1 hora** | **8 horas** | **1 hora** | **% Norma** | **8 horas** | **% Norma** |
| 1 | 30.000 | 10.000 | 5,95 | 0,02% | 3,44 | 0,03% |
| 2 | 30.000 | 10.000 | 5,06 | 0,02% | 2,98 | 0,03% |
| 3 | 30.000 | 10.000 | 4,37 | 0,01% | 2,82 | 0,03% |
| 4 | 30.000 | 10.000 | 5,21 | 0,02% | 3,21 | 0,03% |

**Tabla 20.: Aportes del Proyecto - concentraciones máximas registradas de SO** **2****

| Receptor | Normativa | Col3 | Col4 | Aporte del Proyecto (μg/m3) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Horario** | **Diario** | **Anual** | **Horario** | **% Norma** | **Diario** | **% Norma** | **Anual** | **% Norma** |
| 1 | 350 | 150 | 60 | 1,98E-2 | 0,01% | 6,31E-3 | 0,00% | 1,49E-3 | 0,00% |
| 2 | 350 | 150 | 60 | 1,67E-2 | 0,00% | 4,91E-3 | 0,00% | 1,11E-3 | 0,00% |
| 3 | 350 | 150 | 60 | 1,18E-2 | 0,00% | 3,77E-3 | 0,00% | 4,00E-4 | 0,00% |
| 4 | 350 | 150 | 60 | 1,45E-2 | 0,00% | 3,99E-3 | 0,00% | 9,28E-4 | 0,00% |

**Tabla 21.: Resumen de Emisiones del Proyecto****

| Año | Detalle | Tasa de emisión (Ton/año) | Col4 |
| --- | --- | --- | --- |
| **Año** | **Detalle** | **MP10** | **MP2,5** |
| 5 | Construcción Etapa 3 + Operación Etapa 1 y 2 | 1,415 | 0,346 |

**Tabla 23.: Proyectos Aprobados o en Calificación Ambiental en las cercanías al Proyecto Planta Solar El Cardonal****

| ID | Nombre | Titular | Fecha<br>Ingreso al<br>Sistema | Estado | Distancia al<br>Proyecto |
| --- | --- | --- | --- | --- | --- |
| 1 | Parrones de Baquedano | Inmobiliaria<br>San<br>Ramón I SPA | 07/10/2021 | Aprobado | 0,94 km |

**Tabla 24.: Evaluación de solapamiento fase de construcción****

| Proyecto | Fecha de inicio | Fecha de término | ¿Existe solapamiento? |
| --- | --- | --- | --- |
| Parrones de Baquedano | Primer semestre<br>2022 | Segundo semestre 2024 | No |

**Tabla 25.: Tasas de emisión a considerar para la evaluación del efecto sinérgico****

| Proyecto | Tasa de emisión (ton/año) | Col3 | Fuente |
| --- | --- | --- | --- |
| **Proyecto** | **MP10** | **MP2,5** | **MP2,5** |
| Parrones de Baquedano | 0,4826 | 0,1173 | Anexo 3 ADENDA<br>Complementaria |

**Tabla 26.: Resultados aporte proyectos cercanos en receptores****

| Receptor | Métrica | Aporte proyecto cercanos (μg/m3) | Col4 | D.S. N° 12/2022<br>del MMA | D.S. N° 12/2011<br>del MMA |
| --- | --- | --- | --- | --- | --- |
| **Receptor** | **Métrica** | **MP10** | **MP2,5** | **Límite MP10 **<br>**(μg/m3) ** | **Límite MP2,5 **<br>**(μg/m3) ** |
| 1 | Anual | 7,26E-2 | 1,77E-2 | 50 | 20 |
| 1 | Diaria | 2,92E-1 | 7,09E-2 | 130 | 50 |
| 2 | Anual | 1,18E-1 | 2,86E-2 | 50 | 20 |
| 2 | Diaria | 5,04E-1 | 1,23E-1 | 130 | 50 |
| 3 | Anual | 1,33E-1 | 3,24E-2 | 50 | 20 |
| 3 | Diaria | 6,28E-1 | 1,53E-1 | 130 | 50 |
| 4 | Anual | 4,80E-2 | 1,17E-2 | 50 | 20 |
| 4 | Diaria | 2,16E-1 | 5,24E-2 | 130 | 50 |

**Tabla 27.: Concentraciones totales de MP** **10****

| Receptores | Coordenadas UTM<br>(m) | Col3 | Métrica | Condición o<br>línea de base<br>(μg/m3) | Aporte<br>proyecto<br>(μg/m3) | Aporte otros<br>proyectos con<br>RCA (μg/m3) | Concentración<br>final (μg/m3) | Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **Este** | **Norte** | **Norte** | **A ** | **B ** | **C ** | **A + B +C** | **A + B +C** |
| 1 | 337.026 | 6.218.934 | Anual | 49,16 | 1,24E-01 | 7,26E-02 | 49,36 | 50 |
| 1 | 337.026 | 6.218.934 | 24 H | 145,96 | 5,53E-01 | 2,92E-01 | 146,81 | 130 |
| 2 | 336.990 | 6.218.793 | Anual | 49,16 | 1,01E-01 | 1,18E-01 | 49,38 | 50 |
| 2 | 336.990 | 6.218.793 | 24 H | 145,96 | 5,38E-01 | 5,04E-01 | 147,00 | 130 |
| 3 | 337.023 | 6.218.680 | Anual | 49,16 | 5,54E-02 | 1,33E-01 | 49,35 | 50 |
| 3 | 337.023 | 6.218.680 | 24 H | 145,96 | 4,94E-01 | 6,28E-01 | 147,08 | 130 |
| 4 | 337.194 | 6.218.998 | Anual | 49,16 | 1,13E-01 | 4,80E-02 | 49,32 | 50 |
| 4 | 337.194 | 6.218.998 | 24 H | 145,96 | 6,19E-01 | 2,16E-01 | 146,80 | 130 |

**Tabla 28.: Concentraciones totales de MP** **2,5****

| Receptores | Coordenadas UTM<br>(m) | Col3 | Métrica | Condición o<br>línea de base<br>(μg/m3) | Aporte<br>proyecto<br>(μg/m3) | Aporte otros<br>proyectos con<br>RCA (μg/m3) | Concentración<br>final (μg/m3) | Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **Este** | **Norte** | **Norte** | **A ** | **B ** | **C ** | **A + B +C** | **A + B +C** |
| 1 | 337.026 | 6.218.934 | Anual | 25,58 | 7,78E-02 | 1,77E-02 | 25,68 | 20 |
| 1 | 337.026 | 6.218.934 | 24 H | 87 | 3,00E-01 | 7,09E-02 | 87,37 | 50 |
| 2 | 336.990 | 6.218.793 | Anual | 25,58 | 5,85E-02 | 2,86E-02 | 25,67 | 20 |
| 2 | 336.990 | 6.218.793 | 24 H | 87 | 2,47E-01 | 1,23E-01 | 87,37 | 50 |
| 3 | 337.023 | 6.218.680 | Anual | 25,58 | 2,42E-02 | 3,24E-02 | 25,64 | 20 |
| 3 | 337.023 | 6.218.680 | 24 H | 87 | 2,00E-01 | 1,53E-01 | 87,35 | 50 |
| 4 | 337.194 | 6.218.998 | Anual | 25,58 | 5,42E-02 | 1,17E-02 | 25,65 | 20 |
| 4 | 337.194 | 6.218.998 | 24 H | 87 | 2,34E-01 | 5,24E-02 | 87,29 | 50 |

**Tabla 29.: Concentraciones totales de NO** **x****

| Receptores | Coordenadas UTM<br>(m) | Col3 | Métrica | Condición o<br>línea de base<br>(μg/m3) | Aporte<br>proyecto<br>(μg/m3) | Aporte otros<br>proyectos con<br>RCA (μg/m3) | Concentración<br>final (μg/m3) | Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **Este** | **Norte** | **Norte** | **A ** | **B ** | **C ** | **A + B +C** | **A + B +C** |
| 1 | 337.026 | 6.218.934 | Anual | - | 1,05 | - | 1,05 | 100 |
| 1 | 337.026 | 6.218.934 | 1H | - | 13,83 | - | 13,83 | 400 |
| 2 | 336.990 | 6.218.793 | Anual | - | 7,54E-01 | - | 0,754 | 100 |
| 2 | 336.990 | 6.218.793 | 1H | - | 11,24 | - | 11,24 | 400 |
| 3 | 337.023 | 6.218.680 | Anual | - | 2,41E-01 | - | 0,241 | 100 |
| 3 | 337.023 | 6.218.680 | 1H | - | 7,55 | - | 7,55 | 400 |
| 4 | 337.194 | 6.218.998 | Anual | - | 5,95E-01 | - | 0,595 | 100 |
| 4 | 337.194 | 6.218.998 | 1H | - | 8,73 | - | 8,73 | 400 |

**Tabla 30.: Concentraciones totales de CO****

| Receptores | Coordenadas UTM<br>(m) | Col3 | Métrica | Condición o<br>línea de base<br>(μg/m3) | Aporte<br>proyecto<br>(μg/m3) | Aporte otros<br>proyectos con<br>RCA (μg/m3) | Concentración<br>final (μg/m3) | Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **Este** | **Norte** | **Norte** | **A ** | **B ** | **C ** | **A + B +C** | **A + B +C** |
| 1 | 337.026 | 6.218.934 | 8 H | - | 3,44 | - | 3,44 | 10.000 |
| 1 | 337.026 | 6.218.934 | 1 H | - | 5,95 | - | 5,95 | 30.000 |
| 2 | 336.990 | 6.218.793 | 8 H | - | 2,98 | - | 2,98 | 10.000 |
| 2 | 336.990 | 6.218.793 | 1 H | - | 5,06 | - | 5,06 | 30.000 |
| 3 | 337.023 | 6.218.680 | 8 H | - | 2,82 | - | 2,82 | 10.000 |
| 3 | 337.023 | 6.218.680 | 1 H | - | 4,37 | - | 4,37 | 30.000 |
| 4 | 337.194 | 6.218.998 | 8 H | - | 3,21 | - | 3,21 | 10.000 |
| 4 | 337.194 | 6.218.998 | 1 H | - | 5,21 | - | 5,21 | 30.000 |

**Tabla 31.: Concentraciones totales de SO** **2****

| Receptores | Coordenadas UTM<br>(m) | Col3 | Métrica | Condición o<br>línea de base<br>(μg/m3) | Aporte<br>proyecto<br>(μg/m3) | Aporte otros<br>proyectos con<br>RCA (μg/m3) | Concentración<br>final (μg/m3) | Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **Este** | **Norte** | **Norte** | **A ** | **B ** | **C ** | **A + B +C** | **A + B +C** |
| 1 | 337.026 | 6.218.934 | Anual | - | 1,49E-03 | - | 0,00149 | 60 |
| 1 | 337.026 | 6.218.934 | 24 H | - | 6,31E-03 | - | 0,00631 | 150 |
| 1 | 337.026 | 6.218.934 | 1 H | - | 1,98E-02 | - | 0,0198 | 350 |
| 2 | 336.990 | 6.218.793 | Anual | - | 1,11E-03 | - | 0,00111 | 60 |
| 2 | 336.990 | 6.218.793 | 24 H | - | 4,91E-03 | - | 0,00491 | 150 |
| 2 | 336.990 | 6.218.793 | 1 H | - | 1,67E-02 | - | 0,0167 | 350 |
| 3 | 337.023 | 6.218.680 | Anual | - | 4,00E-04 | - | 0,0004 | 60 |
| 3 | 337.023 | 6.218.680 | 24 H | - | 3,77E-03 | - | 0,00377 | 150 |
| 3 | 337.023 | 6.218.680 | 1 H | - | 1,18E-02 | - | 0,0118 | 350 |
| 4 | 337.194 | 6.218.998 | Anual | - | 9,28E-04 | - | 0,000928 | 60 |
| 4 | 337.194 | 6.218.998 | 24 H | - | 3,99E-03 | - | 0,00399 | 150 |
| 4 | 337.194 | 6.218.998 | 1 H | - | 1,45E-02 | - | 0,0145 | 350 |
