---
title: Sin título
author: Antonia Barrientos
date: D:20250619172333-04'00'
language: es
type: report
pages: 89
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO N°20 Modelación atmosférica ADENDA Complementaria PROYECTO “Parque Las Alamedas I,II y III”
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

# ANEXO N°20 Modelación atmosférica ADENDA Complementaria PROYECTO “Parque Las Alamedas I,II y III”

Mayo, 2025.

Modelación atmosférica
“Parque Las Alamedas I,II y III”

# ÍNDICE DE CONTENIDOS

**1.** **INTRODUCCIÓN ...................................................................................................................................... 6**

**2.** **ANTECEDENTES GENERALES DEL PROYECTO ........................................................................................... 6**

_2.1.1._ _Descripción ............................................................................................................................... 6_

_2.1.2._ _Localización .............................................................................................................................. 7_

**3.** **OBJETIVOS .............................................................................................................................................. 8**

3.1. O BJETIVO G ENERAL ................................................................................................................................ 8

3.2. O BJETIVOS E SPECÍFICOS .......................................................................................................................... 8

**4.** **NORMATIVA CALIDAD DE AIRE ............................................................................................................... 9**

4.1. M ATERIAL PARTICULADO (MP 10 Y MP 2,5 ) ................................................................................................... 9

4.2. D IÓXIDO DE AZUFRE (SO 2 ) ..................................................................................................................... 10

4.3. D IÓXIDO DE NITRÓGENO (NO 2 ) .............................................................................................................. 11

4.4. M ONÓXIDO DE CARBONO (CO) .............................................................................................................. 13

**5.** **JUSTIFICACIÓN DE LOS MODELOS UTILIZADOS ..................................................................................... 16**

5.1. U SO DEL M ODELO CALPUFF ................................................................................................................ 16

5.2. E CUACIÓN DEL MODELO CALPUFF ......................................................................................................... 17

5.3. U SO DEL M ODELO WRF ....................................................................................................................... 17

**6.** **METODOLOGÍA ..................................................................................................................................... 18**

6.1. M ODELACIÓN METEOROLÓGICA .............................................................................................................. 18

6.2. M ODELACIÓN CALPUFF ...................................................................................................................... 18

6.3. R ECEPTORES DISCRETOS ......................................................................................................................... 19

6.4. F UENTES DE EMISIÓN ............................................................................................................................ 22

6.5. A NÁLISIS DE INCERTIDUMBRE ................................................................................................................. 25

_6.5.1._ _Modelo Meteorológico ........................................................................................................... 25_
_6.5.2._ _Análisis cualitativo .................................................................................................................. 26_
_6.5.3._ _Análisis cuantitativo ............................................................................................................... 58_

6.6. T OPOGRAFÍA ....................................................................................................................................... 60

6.7. C ARACTERIZACIÓN A MBIENTAL DEL P ROYECTO ........................................................................................... 61

_6.7.1._ _Material Particulado Respirable (MP_ _10_ _).................................................................................. 61_
_6.7.2._ _Material Particulado Respirable Fino (MP_ _2,5_ _) ......................................................................... 63_
_6.7.3._ _Dióxido de azufre (SO_ _2_ _) ........................................................................................................... 65_
_6.7.4._ _Óxidos de nitrógeno (NO_ _x_ _) ...................................................................................................... 65_

_6.7.5._ _Monóxido de carbono (CO) ..................................................................................................... 65_

**7.** **RESULTADOS ......................................................................................................................................... 65**

7.1. I SOCONCENTRACIÓN ............................................................................................................................. 66

7.2. A PORTE DEL P ROYECTO ......................................................................................................................... 73

7.3. E VALUACIÓN DEL IMPACTO DE LAS EMISIONES ATMOSFÉRICAS DEL MATERIAL PARTICULADO MP 10 Y MP 2,5 EN ZONAS

SATURADAS ...................................................................................................................................................... 75

7.4. E VALUACIÓN DEL EFECTO SINÉRGICO ........................................................................................................ 77

Página **1** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

7.5. E VALUACIÓN DE LOS NIVELES DE CONCENTRACIÓN ...................................................................................... 80

7.6. Á REA DE INFLUENCIA ............................................................................................................................ 83

**8.** **CONSIDERACIONES ............................................................................................................................... 84**

**9.** **CONCLUSIONES .................................................................................................................................... 84**

Página **2** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

# ÍNDICE DE TABLAS

**T** **ABLA** **1.** **L** **ÍMITES ANUAL Y DIARIO** **MP** **10** **Y** **MP** **2,5** ........................................................................................................ 9

**T** **ABLA** **2.** **L** **ÍMITES ANUAL Y DIARIO** **SO** **2** .................................................................................................................... 10

**T** **ABLA** **3.** **L** **ÍMITES ANUAL Y DIARIO DE** **NO** **2** ............................................................................................................... 12

**T** **ABLA** **4.** **L** **ÍMITES ANUAL Y DIARIO DE** **CO** ................................................................................................................. 14

**T** **ABLA** **5.** **R** **ECEPTORES DISCRETOS EN EL ÁREA DEL** **P** **ROYECTO** ....................................................................................... 20

**T** **ABLA** **6.** **FOTOGRAFÍAS REFERENCIALES DE RECEPTORES** ............................................................................................... 20

**T** **ABLA** **7.** **F** **UENTES DE EMISIÓN DEL** **P** **ROYECTO** ........................................................................................................... 22

**T** **ABLA** **8.** **P** **ARÁMETROS DE ENTRADA AL MODELO** .......................................................... **¡E** **RROR** **!** **M** **ARCADOR NO DEFINIDO** **.**

**T** **ABLA** **9.** **E** **STACIÓN UTILIZADA PARA LA VALIDACIÓN DEL MODELO** **WRF** ......................................................................... 26

**T** **ABLA** **10.** **E** **STADÍSTICOS DE SESGO** **,** **ERROR ABSOLUTO MEDIO Y ERROR CUADRÁTICO MEDIO** .............................................. 58
**T** **ABLA** **11.** **C** **ONCENTRACIÓN** **M** **EDIA** **A** **NUAL DE** **MP** **10** **(** **UG** **/** **M** **[3]** **N)** ................................................................................. 62
**T** **ABLA** **12.** **P** **ERCENTIL** **98** **CONCENTRACIÓN** **24** **HORAS DE** **MP** **10** **(** **UG** **/** **M** **[3]** **N)** ................................................................... 63
**T** **ABLA** **13.** **C** **ONCENTRACIÓN** **M** **EDIA** **A** **NUAL DE** **MP** **2,5** **(** **UG** **/** **M** **[3]** **N)** ................................................................................ 64
**T** **ABLA** **14.** **P** **ERCENTIL** **98** **CONCENTRACIÓN** **24** **HORAS DE** **MP** **2,5** **(** **UG** **/** **M** **[3]** **N)** ................................................................... 65

**T** **ABLA** **15.** **N** **ORMAS DE CALIDAD PRIMARIA** ............................................................................................................... 66

**T** **ABLA** **16.** **A** **PORTES DEL** **P** **ROYECTO** **-** **CONCENTRACIONES MÁXIMAS REGISTRADAS DE** **MP** **10** ............................................. 73

**T** **ABLA** **17.** **A** **PORTES DEL** **P** **ROYECTO** **-** **CONCENTRACIONES MÁXIMAS REGISTRADAS DE** **MP** **2,5** ............................................ 73

**T** **ABLA** **18.** **A** **PORTES DEL** **P** **ROYECTO** **-** **CONCENTRACIONES MÁXIMAS REGISTRADAS DE** **NO** **X** .............................................. 74

**T** **ABLA** **19.** **A** **PORTES DEL** **P** **ROYECTO** **-** **CONCENTRACIONES MÁXIMAS REGISTRADAS DE** **CO** ................................................ 74

**T** **ABLA** **20.** **A** **PORTES DEL** **P** **ROYECTO** **-** **CONCENTRACIONES MÁXIMAS REGISTRADAS DE** **SO** **2** ............................................... 74

**T** **ABLA** **21.** **R** **ESUMEN DE** **E** **MISIONES DEL** **P** **ROYECTO** ....................................................... **¡E** **RROR** **!** **M** **ARCADOR NO DEFINIDO** **.**

**T** **ABLA** **22.** **C** **OMPARACIÓN DE LOS RESULTADOS DE LA MODELACIÓN EN RECEPTORES HUMANOS Y VALORES DE SIGNIFICANCIA DE**

**LA** **T** **ABLA** **2** **DE LA** **G** **UÍA** **,** **PARA EL PRIMER AÑO DEL** **P** **ROYECTO** ................................. **¡E** **RROR** **!** **M** **ARCADOR NO DEFINIDO** **.**

**T** **ABLA** **23.** **P** **ROYECTOS** **A** **PROBADOS O EN** **C** **ALIFICACIÓN** **A** **MBIENTAL EN LAS CERCANÍAS AL** **P** **ROYECTO** **P** **LANTA** **S** **OLAR** **E** **L**

**C** **ARDONAL** .................................................................................................................................................. 78

**T** **ABLA** **24.** **E** **VALUACIÓN DE SOLAPAMIENTO FASE DE CONSTRUCCIÓN** ............................................................................. 78

**T** **ABLA** **25.** **T** **ASAS DE EMISIÓN A CONSIDERAR PARA LA EVALUACIÓN DEL EFECTO SINÉRGICO** ............................................... 78

**T** **ABLA** **26.** **R** **ESULTADOS APORTE PROYECTOS CERCANOS EN RECEPTORES** ......................................................................... 79

**T** **ABLA** **27.** **C** **ONCENTRACIONES TOTALES DE** **MP** **10** ....................................................................................................... 80

**T** **ABLA** **28.** **C** **ONCENTRACIONES TOTALES DE** **MP** **2,5** ...................................................................................................... 80

**T** **ABLA** **29.** **C** **ONCENTRACIONES TOTALES DE** **NO** **X** ........................................................................................................ 81

**T** **ABLA** **30.** **C** **ONCENTRACIONES TOTALES DE** **CO** .......................................................................................................... 81

**T** **ABLA** **31.** **C** **ONCENTRACIONES TOTALES DE** **SO** **2** ......................................................................................................... 82

Página **3** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

# ÍNDICE DE FIGURAS

**F** **IGURA** **1.** **U** **BICACIÓN Y VÉRTICES DEL** **P** **ROYECTO** **..................................................................................................... 8**

**F** **IGURA** **2.** **D** **OMINIO DE LA MODELACIÓN** **............................................................................................................. 18**

**F** **IGURA** **3.** **U** **BICACIÓN DE RECEPTORES DISCRETOS** **.................................................................................................. 22**

**F** **IGURA** **4.** **F** **UENTES DE EMISIÓN DEL** **P** **ROYECTO** **..................................................................................................... 23**

**F** **IGURA** **5.** **D** **ATOS VELOCIDAD DEL VIENTO** **WRF** **R** **ANCAGUA** **I ................................................................................... 27**

**F** **IGURA** **6.** **D** **ATOS VELOCIDAD DEL VIENTO ESTACIÓN** **R** **ANCAGUA** **I .............................................................................. 27**

**F** **IGURA** **7.** **D** **ATOS VELOCIDAD DEL VIENTO** **WRF** **R** **ANCAGUA** **II .................................................................................. 28**

**F** **IGURA** **8.** **D** **ATOS VELOCIDAD DE VIENTO OBSERVADA EN ESTACIÓN** **R** **ANCAGUA** **II .......................................................... 28**

**F** **IGURA** **9.** **P** **ROMEDIO HORARIO VELOCIDAD DEL VIENTO** **(** **M** **/** **S** **)** **WRF** **R** **ANCAGUA** **I ........................................................ 29**
**F** **IGURA** **10.** **P** **ROMEDIO HORARIO VELOCIDAD DEL VIENTO** **(** **M** **/** **S** **)** **ESTACIÓN** **R** **ANCAGUA** **I ................................................. 29**
**F** **IGURA** **11.** **P** **ROMEDIO HORARIO VELOCIDAD DEL VIENTO** **(** **M** **/** **S** **)** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ........................................ 30**
**F** **IGURA** **12.** **P** **ROMEDIO HORARIO VELOCIDAD DEL VIENTO** **(** **M** **/** **S** **)** **ESTACIÓN** **R** **ANCAGUA** **II ................................................ 30**

**F** **IGURA** **13.** **D** **IRECCIÓN DEL VIENTO** **(°)** **ESTACIÓN** **R** **ANCAGUA** **I ................................................................................. 31**

**F** **IGURA** **14.** **D** **IRECCIÓN DEL VIENTO** **(°)** **WRF** **R** **ANCAGUA** **I ...................................................................................... 31**

**F** **IGURA** **15.** **D** **IRECCIÓN DEL VIENTO** **(°)** **ESTACIÓN** **R** **ANCAGUA** **II ................................................................................ 32**

**F** **IGURA** **16.** **D** **IRECCIÓN DEL VIENTO** **(°)** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ........................................................................ 32**

**F** **IGURA** **17.** **P** **ROMEDIO HORARIO DIRECCIÓN DEL VIENTO** **WRF** **R** **ANCAGUA** **I ............................................................... 33**

**F** **IGURA** **18.** **P** **ROMEDIO HORARIO DIRECCIÓN DEL VIENTO ESTACIÓN** **R** **ANCAGUA** **I. ......................................................... 33**

**F** **IGURA** **19.** **P** **ROMEDIO HORARIO DIRECCIÓN DEL VIENTO** **WRF** **R** **ANCAGUA** **II .............................................................. 34**

**F** **IGURA** **20.** **P** **ROMEDIO HORARIO DIRECCIÓN DEL VIENTO ESTACIÓN** **R** **ANCAGUA** **II ......................................................... 34**

**F** **IGURA** **21.** **C** **ICLO HORARIO Y MENSUAL DIRECCIÓN Y VELOCIDAD DEL VIENTO ESTACIÓN** **R** **ANCAGUA** **I ................................ 35**

**F** **IGURA** **22.** **C** **ICLO HORARIO Y MENSUAL DIRECCIÓN Y VELOCIDAD DEL VIENTO** **WRF** **R** **ANCAGUA** **I ..................................... 35**

**F** **IGURA** **23.C** **ICLO HORARIO Y MENSUAL DIRECCIÓN Y VELOCIDAD DEL VIENTO** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ........................ 36**

**F** **IGURA** **24.C** **ICLO HORARIO Y MENSUAL DIRECCIÓN Y VELOCIDAD DEL VIENTO ESTACIÓN** **R** **ANCAGUA** **II ................................ 36**

**F** **IGURA** **25.** **%** **HUMEDAD MODELO** **WRF** **R** **ANCAGUA** **I ............................................................................................ 37**

**F** **IGURA** **26.** **%** **HUMEDAD ESTACIÓN** **R** **ANCAGUA** **I ................................................................................................... 38**

**F** **IGURA** **27.%** **HUMEDAD MODELO** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II .............................................................................. 38**

**F** **IGURA** **28.** **%** **HUMEDAD ESTACIÓN** **R** **ANCAGUA** **II .................................................................................................. 39**

**F** **IGURA** **29.** **P** **ROMEDIO HORARIO** **%** **HUMEDAD ESTACIÓN** **R** **ANCAGUA** **I....................................................................... 39**

**F** **IGURA** **30.** **P** **ROMEDIO HORARIO** **%** **HUMEDAD MODELO** **WRF** **R** **ANCAGUA** **I................................................................ 40**

**F** **IGURA** **31.P** **ROMEDIO HORARIO** **%** **HUMEDAD ESTACIÓN** **R** **ANCAGUA** **II ...................................................................... 40**

**F** **IGURA** **32.P** **ROMEDIO HORARIO** **%** **HUMEDAD MODELO** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II .................................................. 41**

**F** **IGURA** **33.** **P** **ROMEDIO HORARIO Y MENSUAL** **%** **DE HUMEDAD MODELO** **WRF** **R** **ANCAGUA** **I ............................................ 41**

**F** **IGURA** **34.** **P** **ROMEDIO HORARIO Y MENSUAL** **%** **DE HUMEDAD ESTACIÓN** **R** **ANCAGUA** **I ................................................... 42**

**F** **IGURA** **35.** **P** **ROMEDIO HORARIO Y MENSUAL** **%** **DE HUMEDAD MODELO** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II .............................. 42**

**F** **IGURA** **36.** **P** **ROMEDIO HORARIO Y MENSUAL** **%** **DE HUMEDAD ESTACIÓN** **R** **ANCAGUA** **II .................................................. 43**

**F** **IGURA** **37.** **T** **EMPERATURA** **(°C)** **MODELO** **WRF** **R** **ANCAGUA** **I ................................................................................... 44**

**F** **IGURA** **38.** **T** **EMPERATURA** **(°C)** **ESTACIÓN** **R** **ANCAGUA** **I .......................................................................................... 44**

**F** **IGURA** **39.** **T** **EMPERATURA** **(°C)** **MODELO** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ..................................................................... 45**

**F** **IGURA** **40.** **T** **EMPERATURA** **(°C)** **ESTACIÓN** **R** **ANCAGUA** **II ......................................................................................... 45**

**F** **IGURA** **41.** **P** **ROMEDIO HORARIO DE TEMPERATURA** **(°C)** **MODELO** **WRF** **R** **ANCAGUA** **I ................................................... 46**

**F** **IGURA** **42.** **P** **ROMEDIO HORARIO DE TEMPERATURA** **(°C)** **ESTACIÓN** **R** **ANCAGUA** **I .......................................................... 46**

**F** **IGURA** **43.** **P** **ROMEDIO HORARIO DE TEMPERATURA** **(°C)** **MODELO** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ..................................... 47**

**F** **IGURA** **44.** **P** **ROMEDIO HORARIO DE TEMPERATURA** **(°C)** **ESTACIÓN** **R** **ANCAGUA** **II ......................................................... 47**

Página **4** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**F** **IGURA** **45.** **P** **ROMEDIO HORARIO Y MENSUAL DE TEMPERATURA** **(°C)** **MODELO** **WRF** **R** **ANCAGUA** **I .................................... 48**

**F** **IGURA** **46.** **P** **ROMEDIO HORARIO Y MENSUAL DE TEMPERATURA** **(°C)** **ESTACIÓN** **R** **ANCAGUA** **I ........................................... 48**

**F** **IGURA** **47.** **P** **ROMEDIO HORARIO Y MENSUAL TEMPERATURA** **(°C)** **MODELO** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II .......................... 49**

**F** **IGURA** **48.** **P** **ROMEDIO HORARIO Y MENSUAL DE TEMPERATURA** **(°C)** **ESTACIÓN** **R** **ANCAGUA** **II.......................................... 49**

**F** **IGURA** **49.** **R** **OSA DE LOS VIENTOS NOCHE MODELO** **WRF** **R** **ANCAGUA** **I ...................................................................... 50**

**F** **IGURA** **50.** **R** **OSA DE LOS VIENTOS NOCHE ESTACIÓN** **R** **ANCAGUA** **I ............................................................................. 50**

**F** **IGURA** **51.** **R** **OSA DE LOS VIENTOS MAÑANA** **,** **MODELO** **WRF** **R** **ANCAGUA** **I .................................................................. 51**

**F** **IGURA** **52.** **R** **OSA DE LOS VIENTOS MAÑANA** **,** **ESTACIÓN** **R** **ANCAGUA** **I ......................................................................... 51**

**F** **IGURA** **53.** **R** **OSA DE LOS VIENTOS TARDE** **,** **MODELO** **WRF** **R** **ANCAGUA** **I ...................................................................... 52**

**F** **IGURA** **54.** **R** **OSA DE LOS VIENTOS TARDE** **,** **ESTACIÓN** **R** **ANCAGUA** **I ............................................................................. 52**

**F** **IGURA** **55.** **R** **OSA DE LOS VIENTOS DIARIA** **,** **MODELO** **WRF** **R** **ANCAGUA** **I...................................................................... 53**

**F** **IGURA** **56.** **R** **OSA DE LOS VIENTOS DIARIA** **,** **ESTACIÓN** **R** **ANCAGUA** **I ............................................................................ 53**

**F** **IGURA** **57.** **R** **OSA DE LOS VIENTOS NOCHE** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II .................................................................... 54**

**F** **IGURA** **58.** **R** **OSA DE LOS VIENTOS NOCHE ESTACIÓN** **R** **ANCAGUA** **II ............................................................................ 54**

**F** **IGURA** **59.** **R** **OSA DE LOS VIENTOS MAÑANA** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ................................................................. 55**

**F** **IGURA** **60.** **R** **OSA DE LOS VIENTOS MAÑANA ESTACIÓN** **R** **ANCAGUA** **II ......................................................................... 55**

**F** **IGURA** **61.R** **OSA DE LOS VIENTOS TARDE** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II ...................................................................... 56**

**F** **IGURA** **62.R** **OSA DE LOS VIENTOS TARDE ESTACIÓN** **R** **ANCAGUA** **II .............................................................................. 56**

**F** **IGURA** **63.** **R** **OSA DE LOS VIENTOS DIARIA** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II .................................................................... 57**

**F** **IGURA** **64.** **R** **OSA DE LOS VIENTOS DIARIA** **WRF** **ESTACIÓN** **R** **ANCAGUA** **II .................................................................... 57**

**F** **IGURA** **65.** **I** **NFORMACIÓN TOPOGRÁFICA** **............................................................................................................ 60**

**F** **IGURA** **66.** **E** **LEVACIÓN DE LA ZONA DE MODELACIÓN** **-** **CALPUFF** **3D ....................................................................... 60**

**F** **IGURA** **67.** **R** **EGISTRO DIARIO** **.** **P** **ROMEDIO ANUAL** **MP** **10** **E** **STACIÓN** **R** **ANCAGUA** **II ......................................................... 61**

**F** **IGURA** **68.** **C** **ONCENTRACIÓN DIARIA** **MP** **10** **E** **STACIÓN** **R** **ANCAGUA** **II ......................................................................... 62**

**F** **IGURA** **69.** **R** **EGISTRO DIARIO** **.** **P** **ROMEDIO ANUAL** **MP** **2,5** **E** **STACIÓN** **R** **ANCAGUA** **II ........................................................ 63**

**F** **IGURA** **70.** **C** **ONCENTRACIÓN DIARIA DE** **MP** **2,5** **E** **STACIÓN** **R** **ANCAGUA** **II ..................................................................... 64**

**F** **IGURA** **71.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **MP** **10** **CONCENTRACIÓN PROMEDIO ANUAL** **.................................................. 67**

**F** **IGURA** **72.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **MP** **10** **P98** **24H .................................................................................... 67**

**F** **IGURA** **73.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **MP** **2,5** **CONCENTRACIÓN PROMEDIO ANUAL** **.................................................. 68**

**F** **IGURA** **74.** **M** **APA** **I** **SOCONCENTRACIÓN** **MP** **2,5** **P98** **24H ........................................................................................ 68**

**F** **IGURA** **75.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **SO** **2** **CONCENTRACIÓN PROMEDIO ANUAL** **..................................................... 69**

**F** **IGURA** **76.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **SO** **2** **,** **CONCENTRACIÓN PROMEDIO** **24H ...................................................... 69**

**F** **IGURA** **77.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **SO** **2** **CONCENTRACIÓN** **P98,5** **H** **ORARIO** **...................................................... 70**

**F** **IGURA** **78.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **NO** **X** **CONCENTRACIÓN PROMEDIO ANUAL** **.................................................... 70**

**F** **IGURA** **79.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **NO** **X** **,** **CONCENTRACIÓN** **P99** **1H ................................................................ 71**

**F** **IGURA** **80.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **CO,** **CONCENTRACIÓN** **P99** **1** **HORA** **............................................................ 72**

**F** **IGURA** **81.** **M** **APA DE** **I** **SOCONCENTRACIÓN** **CO,** **CONCENTRACIÓN** **P99** **8H .................................................................. 72**

**F** **IGURA** **82.** **U** **BICACIÓN DEL** **P** **ROYECTO EN RELACIÓN CON LA ZONA SATURADA O LATENTE** **............................................... 75**
**F** **IGURA** **83.** **Á** **REA DE INFLUENCIA DEL** **P** **ROYECTO** **,** **COMPONENTE AIRE** **(** **EMISIONES ATMOSFÉRICAS** **) ................................... 83**

Página **5** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

# 1. Introducción

El Proyecto “Parque Las Alamedas I, II y III”, se ubica en la comuna de Rancagua, provincia
de Cachapoal de la Región del Libertador General Bernardo O'Higgins.

El presente documento corresponde a la evaluación de la dispersión y concentración
ambiental de los contaminantes emitidos a la atmósfera producto de las actividades del
Proyecto, dentro del área de estudio, mediante las herramientas de modelación sugeridas
por el Servicio de Evaluación Ambiental, en base a los lineamientos establecidos en la Guía
“Uso de Modelos de Calidad del Aire en el SEIA”, 2023.

En esta modelación, se estimarán las concentraciones horarias utilizando el modelo tipo
“Puff” (Utilizando el programa Calpuff View versión 7.0) de MP 10, MP 2,5, CO, NO X y SO 2 para
evaluar el cumplimiento de las normas de calidad de aire durante el escenario más
desfavorable del Proyecto.

# 2. Antecedentes generales del proyecto

**2.1.1.** **Descripción**

Parque Las Alamedas I, II y III está ubicado en la Av. Libertador Bernardo O’Higgins Lote
2B, Comuna de Rancagua, Región del Libertador General Bernardo O’Higgins, la cual
contempla la construcción y operación de una solución habitacional de tres edificios de 9
pisos, el cual contempla un total de 633 departamentos, 3 locales comerciales y 648
estacionamientos vehiculares y 30 estacionamientos para bicicletas. El proyecto presenta
una superficie de construcción de 42.388,65 m [2] y una superficie predial de 26.340 m [2], donde
se incorporarán 3.123 m [2] de áreas verdes con el objeto de brindar un entorno más amigable
a los futuros propietarios.

El proyecto considera tres etapas constructivas, la cual tendrá una duración de 24 meses
cada una y que se evaluarán íntegramente en la presente DIA.

A continuación, se presentan la descripción de cada etapa.

Etapa N°1: Consiste en la construcción y operación de un edificio de 9 pisos de 211
departamentos, 1 local comercial, 216 estacionamientos vehiculares y 10 estacionamientos
para bicicletas. Posee una superficie de construcción es de 14.129,55 m [2] en un predio de
8.527,2 m [2] .

Etapa N°2: Consiste en la construcción y operación de un edificio de 9 pisos de 211
departamentos, 1 local comercial, 216 estacionamientos vehiculares y 10 estacionamientos
para bicicletas. Posee una superficie de construcción es de 14.129,55 m [2] en un predio de
8.527,2 m [2] .

Página **6** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

Etapa N°3: Consiste en la construcción y operación de un edificio de 9 pisos de 211
departamentos, 1 local comercial, 216 estacionamientos vehiculares y 10 estacionamientos
para bicicletas. Posee una superficie de construcción es de 14.129,55 m [2] en un predio de
9.285,6 m [2] .

Adicionalmente, El proyecto forma parte del Plan de Emergencia Habitacional, de acuerdo
con lo dispuesto en el D.S. N°19/2016 del Ministerio de Vivienda y Urbanismo “Programa de
Integración Social y Territorial”.

De acuerdo con el artículo 8° de la Ley N° 19.300, "Los Proyectos o actividades señaladas
en el artículo 10 sólo podrán ejecutarse o modificarse previa evaluación de su impacto
ambiental, de acuerdo con lo establecido en la presente Ley".

A su vez, el artículo 10 de la citada Ley enumera la lista de “los Proyectos o actividades
susceptibles de causar impacto ambiental, en cualesquiera de sus fases, que deberán
someterse al sistema de evaluación de impacto ambiental”, los cuales son precisados, en
cuanto a sus características y dimensiones, en el artículo 3° del Reglamento del SEIA
(“RSEIA”).

De conformidad con las disposiciones legales y reglamentarias citadas y, específicamente,
el artículo 3° del RSEIA, las siguientes tipologías resultan aplicables al Proyecto:

h) Proyectos industriales o inmobiliarios que se ejecuten en zonas declaradas latentes o

saturadas.

h.1. Se entenderá por proyectos inmobiliarios aquellos loteos o conjuntos de viviendas que
contemplen obras de edificación y/o urbanización, así como los proyectos destinados a
equipamiento, y que presenten alguna de las siguientes características:

h.1.3. Que se emplacen en una superficie igual o superior a siete hectáreas (7 ha) o
consulten la construcción de trescientas (300) o más viviendas.

Debido a que el Proyecto se ubica en la Región del Libertador General Bernardo O’Higgins,
la cual se encuentra declarada como saturada por MP 10, como concentración anual y de 24
horas según D.S N°7/2009 y saturada por MP 2,5 como concentración anual y de 24 horas
según D.S. N°42/2017, además de contemplar la construcción de 633 viviendas, es posible
concluir que el proyecto debe ingresar al SEIA por el literal h.1.3.

**2.1.2.** **Localización**

La ubicación político-administrativa a nivel Regional, Provincial y Comunal del Proyecto es
la siguiente:

**Región:** del Libertador General Bernardo O'Higgins

**Provincia:** Cachapoal

Página **7** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Comuna:** Rancagua

El Proyecto se encuentra ubicado en Av. Libertador Bernardo O’Higgins, Lote 2B.

**Figura 1. Ubicación y vértices del Proyecto**

Fuente: Cartografía 6 Capítulo 1 “Descripción de Proyecto”, 2025.

# 3. Objetivos

**3.1.** **Objetivo General**

El objetivo principal de este estudio atmosférico es evaluar el efecto de las emisiones de
contaminantes del Proyecto “Parque Las Alamedas I, II y III” en la atmósfera.

El propósito es determinar si existe alguna afectación potencial a la salud y calidad de vida
de las personas que realicen actividades en las proximidades del área del Proyecto, en
conformidad al artículo 5° del D.S. N° 40/12.

**3.2.** **Objetivos Específicos**

1. Determinar y evaluar la extensión de la dispersión de los contaminantes MP 10, MP 2,5,
óxidos de azufre (SOx), óxidos de nitrógeno (NOx) y monóxido de carbono (CO) con
el objetivo de predecir las áreas de impacto máximo y mínimo.

2. Determinar y evaluar la extensión de la dispersión de los contaminantes MP 10, MP 2,5,
óxidos de azufre (SOx), óxidos de nitrógeno (NOx) y monóxido de carbono (CO), en
los receptores detectados en las cercanías del proyecto.

Página **8** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

3. Determinar y evaluar la extensión de la dispersión de los contaminantes MP 10, MP 2,5,
SOx, CO y NOx en las Estaciones de Monitoreo con Representatividad Poblacional
(EMRP) cercanas al Proyecto.

4. Realizar un análisis de la línea de base de calidad del aire, en el cual se busca conocer
la concentración de material particulado característico del área del Proyecto.

# 4. Normativa Calidad de Aire

**4.1.** **Material particulado (MP** **10** **y MP** **2,5** **)**

Para llevar a cabo la evaluación de los aportes y la exposición a las concentraciones de estos
contaminantes, los cuales están regulados bajo normas de calidad primaria. Estas
regulaciones tienen como objetivo principal proteger la salud de las personas frente a los
efectos agudos y crónicos, por lo tanto, su aplicación es fundamental para salvaguardar la
calidad del aire en el país.

A continuación, en la siguiente Tabla, se detalla la normativa ambiental relacionada con los
contaminantes MP 10 y MP 2,5 .

**Tabla 1. Límites anual y diario MP** **10** **y MP** **2,5**

|Nivel|MP (μg/m3)<br>10|MP (μg/m3)<br>2,5|
|---|---|---|
|Límite anual|50|20|
|Límite diario|130|50|
|Normativa|D.S. N° 12/2022|D.S. N° 12/2011 del MMA|

Fuente: Elaborado por FCM en base a D.S. N° 12/2022 y D.S. N° 12/2011 del MMA, 2025.

La superación del límite normativa no es motivo de condiciones de superación de la norma,
sino que se considera que la norma es incumplida bajos las siguientes condiciones:

Artículo 4° D.S. N° 12/2022 del MMA, “Se considerará sobrepasada la norma primaria de
calidad ambiental para material particulado respirable MP10 como concentración anual,
cuando el promedio aritmético de tres años calendarios consecutivos, en cualquier estación
monitora calificada como EMRP, sea mayor o igual a 50 μg/m [3] N”

Artículo 5° D.S. N° 12/2022 del MMA, “Se considerará sobrepasada la norma primaria de
calidad ambiental para material particulado respirable MP10, como concentración de 24
horas, cuando ocurra, en cualquier estación monitora calificada como EMRP, una de las
siguientes condiciones:

Página **9** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

a. En un año calendario, el valor correspondiente al percentil 98 de las concentraciones
de 24 horas registradas, sea mayor o igual a 130 μg/m3N

b. Si antes que concluya un año calendario, el número de días con mediciones sobre el
valor de 130 μg/m3N, sea mayor que siete”

Artículo 4° D.S. N° 12/2011 del MMA, “Se considerará sobrepasada la norma primaria de
calidad del aire para material particulado fino respirable MP2,5, en los siguientes casos:

a) Cuando el percentil 98 de los promedios diarios registrados durante un año, sea mayor
a 50(μg/m3), en cualquier estación monitora calificada como EMRP; o

b) Cuando el promedio tri-anual de las concentraciones anuales sea mayor a 20(μg/m3),
en cualquier estación monitora calificada como EMRP.”

**4.2.** **Dióxido de azufre (SO** **2** **)**

En relación con los contaminantes de dióxido de azufre (SO 2 ), éstos están sujetos a
regulación de acuerdo con el D.S. N° 104/2019 del Ministerio del Medio Ambiente. Esta
normativa establece los límites máximos permisibles de concentración de SO 2 en el aire, así
como los estándares de calidad del aire aplicables. Este decreto corresponde a una norma
de calidad primaria, cuyo propósito es proteger la salud de las personas de los efectos
agudos y crónicos derivados de la exposición a estos contaminantes, manteniendo un nivel
de riesgo aceptable. Para lograr esto, se establecen límites de concentración permitidos, así
como condiciones que definen la superación de la norma.

**Tabla 2. Límites anual y diario SO** **2**

|Nivel|SO (μg/m3)<br>2|
|---|---|
|Límite anual|60|
|Límite diario|150|
|Límite horario|350|
|Normativa|D.S. N° 104/2019 del MMA|

Fuente: Elaboración por FCM en base al D.S. N° 104/2019 del MMA, 2025.

De acuerdo con lo indicado en el D.S. N° 104/2019 del MMA, se tiene lo siguiente:

**Artículo 3°**

“La norma primaria de calidad de aire para dióxido de azufre como concentración anual será
de 60 μg/m3N, equivalente a 23 ppbv.

Página **10** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

Se considerará sobrepasada la norma primaria de calidad de aire para dióxido de azufre
como concentración anual, cuando ocurra al menos, una de las siguientes condiciones:

a) El promedio aritmético de tres años calendario sucesivos de los valores de concentración
anual, fuere mayor o igual al valor de la norma que se establece.

b) Si en un año calendario, el valor de la concentración anual, fuere mayor o igual al doble
del valor de la norma que se establece.”

**Artículo 4°**

“La norma primaria de calidad de aire para dióxido de azufre como concentración de 24
horas será de 150 μg/m3N, equivalente a 57 ppbv.

Se considerará sobrepasada la norma primaria de calidad de aire para dióxido de azufre
como concentración de 24 horas, cuando ocurra al menos, una de las siguientes

condiciones:

a) El promedio aritmético de tres años calendario sucesivos de los valores del percentil 99
de las concentraciones de 24 horas registradas cada año, fuere mayor o igual al valor de la
norma que se establece.

b) Si en un año calendario, el valor correspondiente al percentil 99 de las concentraciones
de 24 horas registradas, fuere mayor o igual al doble del valor de la norma que se establece.”

**Artículo 5°**

“La norma primaria de calidad de aire para dióxido de azufre como concentración de 1 hora
será de 350 μg/m3N, equivalente a 134 ppbv.

Se considerará sobrepasada la norma primaria de calidad de aire para dióxido de azufre
como concentración de 1 hora, cuando ocurra al menos, una de las siguientes condiciones:

a) El promedio aritmético de tres años calendario sucesivos de los valores del percentil 98,5
de las concentraciones de 1 hora registradas cada año, fuere mayor o igual al valor de la
norma que se establece. A partir del cuarto año calendario de publicada la norma en el
Diario Oficial, se considera un percentil 99 para evaluar esta condición.

b) Si en un año calendario, el valor correspondiente al percentil 98,5 de las concentraciones
de 1 hora registradas, fuere mayor o igual al doble del valor de la norma que se establece.
A partir del cuarto año calendario de publicada la norma en el Diario Oficial, se considera
un percentil 99 para evaluar esta condición”.

**4.3.** **Dióxido de nitrógeno (NO** **2** **)**

El dióxido de nitrógeno (NO 2 ) se encuentra sujeto a regulación normativa mediante una
norma de calidad primaria, la cual tiene como objetivo proteger la salud de las personas

Página **11** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

frente a los efectos agudos y crónicos derivados de la exposición al NO 2 en el aire. Con este
objetivo, se establecen límites de concentración permitidos y condiciones para la superación
de la norma. La regulación del NO 2 se encuentra establecida en el D.S. N° 40/2040 del

Ministerio de Medio Ambiente.

Este decreto establece los límites máximos permisibles de concentración de NO 2 en el aire,
así como los estándares de calidad del aire correspondientes, los cuales se presentan en la
siguiente tabla.

**Tabla 3. Límites anual y diario de NO** **2**

|Nivel|NO (μg/m3)<br>2|
|---|---|
|Límite anual|40|
|Límite diario|100|
|Límite horario|200|
|Normativa|D.S. N° 40/2024 del MMA|

Fuente: Elaboración propia en base a D.S. N° 40/2024 del MMA, 2025.

De acuerdo con lo indicado en el D.S. N° 40/2024 del MMA, se tiene lo siguiente:

**Artículo 3°**

“La norma primaria de calidad de aire para dióxido de nitrógeno como concentración anual
será de 40 μg/m3N.

Se considerará sobrepasada la norma primaria de calidad de aire para dióxido de nitrógeno
como concentración anual, cuando ocurra al menos, una de las siguientes condiciones:

a) El promedio aritmético de tres años calendario sucesivos de los valores de

concentración anual, fuere mayor o igual al valor de la norma que se establece.

b) Si en un año calendario, el valor de la concentración anual, fuere mayor o igual al

doble del valor de la norma que se establece.”

**Artículo 4°**

“La norma primaria de calidad de aire para dióxido de nitrógeno como concentración de 24
horas será de 100 μg/m3N.

Se considerará sobrepasada la norma primaria de calidad de aire para dióxido de
nitrógeno como concentración de 24 horas, cuando ocurra al menos, una de las siguientes

condiciones:

Página **12** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

a) El promedio aritmético de tres años calendario sucesivos de los valores del percentil

99 de la concentración de 24 horas registrados durante un año, fuere mayor o igual
al valor de la norma que se establece.

b) Si en el primer o segundo periodo de 12 meses a partir del mes de inicio de las

mediciones y, al reemplazar el percentil 99 de concentración de 24 horas para los
periodos faltantes por cero, el promedio aritmético de los tres periodos resultare
mayor o igual al nivel de la norma”.

**Artículo 5°**

“La norma primaria de calidad de aire para dióxido de nitrógeno como concentración de 1
hora será de 200 μg/m3N.

Se considerará sobrepasada la norma primaria de calidad de aire para dióxido de
nitrógeno como concentración de 1 hora, cuando ocurra al menos, una de las siguientes

condiciones:

a) El promedio aritmético de tres años calendario sucesivos de los valores del percentil 99

de los máximos diarios de concentración de 1 hora registrados cada año, fuere mayor
o igual al valor de la norma que se establece.

b) Si en el primer o segundo periodo de 12 meses a partir del mes de inicio de las

mediciones y, al reemplazar el percentil 99 de los máximos diarios de concentración de
1 hora para los periodos faltantes por cero, el promedio aritmético de los tres periodos
resultare mayor o igual al nivel de la norma.”

**4.4.** **Monóxido de carbono (CO)**

El monóxido de carbono (CO) se encuentra sujeto a regulación normativa mediante una
norma de calidad primaria, la cual tiene como objetivo proteger la salud de las personas
frente a los efectos agudos y crónicos derivados de la exposición al CO en el aire. Con este
objetivo, se establecen límites de concentración permitidos y condiciones para la superación
de la norma. La regulación del CO se encuentra establecida en el D.S. N° 115/2002 del

MINSEGPRES.

Este decreto establece los límites máximos permisibles de concentración de CO en el aire,
así como los estándares de calidad del aire correspondientes, los cuales se presentan en la
siguiente tabla.

Página **13** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Tabla 4. Límites anual y diario de CO**

|Nivel|CO (mg/m3N)|
|---|---|
|Límite horario|30|
|Límite 8 horas|10|
|Normativa|D.S. N° 115/2002 del MINSEGPRES|

Fuente: Elaboración propia en base a D.S. N° 115/2002 del MINSEGPRES, 2025.

De acuerdo con lo indicado en el D.S. N° 115/2002 del MINSEGPRES, se tiene lo siguiente:

**Artículo 3°**

“La norma primaria de calidad de aire para monóxido de carbono como concentración de 8
horas será de 9 ppmv (10mg/m [3] N).

Se considerará sobrepasada la norma primaria de calidad de aire para monóxido de carbono
como concentración de 8 horas, cuando el promedio aritmético de tres años sucesivos, del
percentil 99 de los máximos diarios de concentración de 8 horas registrados durante un año
calendario, en cualquier estación monitora EMRPG fuere mayor o igual al nivel indicado en
el inciso precedente.

Si el período de medición en una estación monitora EMPRG no comenzare el 1o de enero,
se considerarán los tres primeros períodos de 12 meses a partir del mes de inicio de las
mediciones hasta disponer de tres años calendarios sucesivos de mediciones.

Se considerará sobrepasada la norma primaria de calidad de aire para monóxido de carbono
como concentración de 8 horas, si en el primer o segundo período de 12 meses a partir del
mes de inicio de las mediciones y, al reemplazar el percentil 99 de los máximos diarios de
concentración de 8 horas para los períodos faltantes por cero, el promedio aritmético de los
tres períodos resultare mayor o igual al nivel de la norma.”

**Artículo 4°**

“La norma primaria de calidad de aire para monóxido de carbono como concentración de 1
hora será de 26 ppmv (30 mg/m [3] N).

Se considerará sobrepasada la norma primaria de calidad de aire para monóxido de carbono
como concentración de 1 hora, cuando el promedio aritmético de tres años sucesivos, del
percentil 99 de los máximos diarios de concentración de 1 hora registrados durante un año
calendario, en cualquier estación monitora EMRPG, fuere mayor o igual al nivel indicado en
el inciso precedente.

Página **14** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

Si el período de medición en una estación monitora EMPRG no comenzare el 1o de enero,
se considerarán los tres primeros períodos de 12 meses a partir del mes de inicio de las
mediciones hasta disponer de tres años calendarios sucesivos de mediciones.

Se considerará sobrepasada la norma primaria de calidad de aire para monóxido de carbono
como concentración de 1 hora, si en el primer o segundo período de 12 meses a partir del
mes de inicio de las mediciones y, al reemplazar el percentil 99 de los máximos diarios de
concentración de 1 hora para los períodos faltantes por cero, el promedio aritmético de los
tres períodos resultare mayor o igual al nivel de la norma.”

Página **15** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica “Proyecto Inmobiliario de

Integración Social y Territorial D.S. N° 19

Condominio Los Arrayanes II”

# 5. Justificación de los modelos utilizados

**5.1.** **Uso del Modelo CALPUFF**

Los modelos de calidad del aire disponibles se clasifican principalmente en cuatro categorías:
modelos Gaussianos, modelos Eulerianos, modelos Lagrangeanos y modelos tipo puff.

Para efectos de esta modelación de dispersión de contaminantes atmosféricos provenientes
del Proyecto, se realizó con un modelo tipo “Puff”, específicamente el modelo CALPUFF,
modelo recomendado en el punto 3.2 a) de la “Guía para el uso de modelos de calidad del
aire en el SEIA”, 2023, para contaminantes primarios en un radio de 5 km desde la fuente
de emisión.

De acuerdo con lo indicado por la “Guía para el uso de modelos de calidad del aire en el
SEIA”, 2023, “los modelos tipo puff son una combinación entre los modelos Gaussianos y
los modelos Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de
contaminantes provenientes de una emisión instantánea, llamada puff, a lo largo de una
trayectoria. Su aproximación matemática consiste en estimar la dispersión en forma
Gaussiana en cada punto de una trayectoria; es decir, a diferencia de los modelos
Lagrangeanos que necesitan el cálculo de un gran número de trayectorias para una fuente,
los modelos tipo puff solo requieren una trayectoria por puff, lo que hace su cálculo mucho
más rápido. En el caso de emisiones continuas, se simulan las trayectorias y la dispersión
Gaussiana de muchos puff”.

CALPUFF se compone de tres módulos: CALMET, CALPUFF y CALPOST.

El módulo CALMET es un modelo meteorológico que genera campos horarios de viento y
temperatura en una grilla tridimensional. También asigna campos en dos dimensiones de
altura y usos del suelo. Es importante destacar que este módulo puede ser reemplazado por

el modelo WRF.

El módulo CALPUFF, por su parte, es un modelo de transporte y dispersión que simula los
procesos de dispersión y transformación de contaminantes emitidos desde fuentes
modeladas. CALPUFF utiliza los datos generados por CALMET como entrada y genera
archivos de salida que contienen las concentraciones horarias o la deposición por hora de
los flujos evaluados en receptores seleccionados.

Además, el módulo CALPOST se utiliza para procesar los archivos generados por CALMET y
CALPUFF, produciendo tabulaciones que resumen los resultados de la simulación.

Por último, se destaca que la modelación CALPUFF es la más recomendable para este caso,
debido a que, es especialmente útil para modelar la dispersión de contaminantes a largas
distancias (mayores a 50 km). Además, este tiene la capacidad de manejar condiciones

Página **16** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

meteorológicas no estacionarias y complejas, como vientos variables en el tiempo, espacio
y terrenos irregulares, al considerar la topografía y meteorología del emplazamiento del
Proyecto, brindando así una mayor precisión en el resultado.

**5.2.** **Ecuación del modelo CALPUFF**

La ecuación básica que utiliza el modelo para realizar la modelación es la siguiente:

[−d] 2σ y [2][c2] []]

Q
C=
2πQ x Q y

g exp

~~[~~ [−d] 2σ x [2][a2]

[−d] 2σ x [2][a2] []exp] ~~[[]~~ [−d] 2σ y [2][c2]

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

 C, es concentración a nivel del suelo (g/m3),

 Q, es masa de contaminantes (g) en la nube.

 - σ x, es desviación estándar (m) de la distribución de Gauss en el viento a lo largo de
la dirección.

 - σ y, es desviación estándar (m) de la distribución de Gauss en el viento de costado

 - σ z, es desviación estándar (m) de la distribución de Gauss en la dirección vertical.

 da, es distancia (m) del centro de la nube al receptor en la dirección del viento a lo
largo.

 dc, es distancia (m) del centro de la nube al receptor en la dirección de viento

cruzado.

 g, es el término vertical (m) de la ecuación Gaussiana.

 H, es la altura afectiva (m) desde el nivel del suelo del hojaldre.

 h, es la altura de la capa de mezcla.

**5.3.** **Uso del Modelo WRF**

Modelo numérico recomendado para la generación de datos meteorológicos corresponde al
modelo WRF, Weather Research and Forecasting Model por sus siglas en inglés, es uno de
los simuladores meteorológicos de pronóstico más avanzados y completos que se encuentra
en constante mejora por el National Center for Atmospheric Research (NCAR) y la National
Oceanic and Atmospheric Administration (NOAA) (además de otras instituciones como el
NCEP, ESRL, AFWA, etc.).

Página **17** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

El modelo WRF es una herramienta de predicción numérica del tiempo desarrollada tanto
para fines de investigación como para aplicaciones operativas.

# 6. Metodología

La metodología utilizada para llevar a cabo la modelación de la dispersión de material
particulado y gases de combustión se describe, a continuación.

**6.1.** **Modelación meteorológica**

El modelo WRF es un modelo matemático que realiza la simulación de las condiciones
meteorológicas en un dominio de modelación, utilizando las variables que influyen en la
meteorología. Para el caso de la presente modelación de emisiones, se utilizó para el año

2024.

**6.2.** **Modelación CALPUFF**

Para la modelación meteorológica, se adoptaron los siguientes criterios. La modelación
CALPUFF se realizó en un dominio de 50 km x 50 km, que abarca toda el área del Proyecto,
como se muestra en la siguiente Figura.

**Figura 2. Dominio de la modelación**

Fuente: Elaborado por FCM, 2025.

En cuanto a los escenarios de modelación, se generó un mapa de iso-concentración para
analizar los resultados de la dispersión de MP 2,5, MP 10, SO x, CO y NO x, los cuales
corresponden a las emisiones generadas por las actividades del Proyecto. Este mapa
permitió evaluar los niveles de concentración en toda el área de estudio.

Página **18** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

El mapa se obtuvo mediante la modelación del dominio, el cual se representó mediante una
grilla con una resolución de 1 km. Esta grilla proporciona datos de concentración en cada
vértice. Los mapas resultantes son el producto de la interpolación entre los datos de
modelación en cada vértice. Además, los datos de concentración generados por el modelo
corresponden a la concentración promedio de la primera capa de modelación.

Dado lo anterior, es necesario considerar que el mapa de iso-concentración es una
representación espacial de la dispersión y no debe tomarse como una referencia precisa de
la concentración, ya que tiende a sobreestimar los valores. Por el contrario, la evaluación
de la concentración en puntos discretos ofrece una estimación más precisa y libre de
distorsiones de la magnitud del impacto en la calidad del aire. Por esta razón, se realizó una
modelación discreta en receptores específicos para analizar el impacto en las poblaciones

cercanas.

**6.3.** **Receptores discretos**

A continuación, en la siguiente Tabla se presentan las coordenadas de los receptores
discretos en el área del Proyecto.

**Tabla 5. Receptores discretos modelación atmosférica**

|Receptores|Localización en coordenadas<br>UTM (WGS 84, Huso 19)|Col3|Altitud (m.s.n.m.)|Breve descripción|
|---|---|---|---|---|
|**Receptores**|**Este**|**Norte**|**Norte**|**Norte**|
|R1|337.026|6.218.934|480,11|Galpón Material ligero<br>de un piso|
|R2|336.990|6.218.793|481,56|Edificio Material solido<br>de 8 pisos|
|R3|337.023|6.218.680|483,24|Edificio Material solido<br>de 8 pisos|
|R4|337.194|6.218.998|480,62|Jardín<br>infantil<br>de<br>material solido de un<br>piso|

Fuente: Elaboración propia, 2025.

A continuación, en la siguiente Tabla se presenta la altura y la distancia de cada receptor.

Página **19** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Tabla 6. Altura y distancia de receptores discretos en el área del Proyecto**

|Receptores|Descripción|Altura de<br>receptor<br>(m)|Distancia<br>Proyecto<br>(m)|Coordenadas UTM<br>Huso 19S|Col6|
|---|---|---|---|---|---|
|**Receptores**|**Descripción**|**Altura de**<br>**receptor**<br>**(m)**|**Distancia**<br>**Proyecto**<br>**(m)**|**Este**|**Norte**|
|R1|Galpón Material ligero de un piso|1,5|19|337.026|6.218.934|
|R2|Edificio Material solido de 8 pisos|1,5 - 19|5|336.990|6.218.793|
|R3|Edificio Material solido de 8 pisos|1,5 - 19|22|337.023|6.218.680|
|R4|Jardín infantil de material solido de un<br>piso|1,5|117|337.194|6.218.998|

Fuente: Elaboración en base Tabla 5 Estudio de Ruido y Vibraciones, 2025.

Cabe destacar que, si bien existen otras edificaciones cercanas al área del Proyecto, se han
considerado los puntos de evaluación más cercanos para la evaluación.

A continuación, se presentan fotografías de los puntos receptores considerados.

**Tabla 7. fotografías referenciales de receptores**

Página **20** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

|R2|Col2|
|---|---|
|R3||
|R4||

Fuente: Tabla 5. Estudio de Ruido y Vibración, 2025.

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Página **21** de **89**

Modelación atmosférica
“Parque Las Alamedas I,II y III”

A continuación, en la siguiente Figura se presentan la ubicación de los receptores discretos.

**Figura 3. Ubicación de receptores discretos**

Fuente: Figura 4 Estudio de Ruido y Vibración, 2025.

**6.4.** **Fuentes de emisión**

En las siguientes Tabla y Figura se presentan las fuentes de emisión como toneladas año y
como tasa de emisión del Proyecto, las cuales han sido ingresadas como datos de entrada
para el modelo CALPUFF.

**Tabla 8. Fuentes de emisión del Proyecto**

|Cod.<br>de la<br>fuente|Fuente|Descripción|Longitud<br>(km)|Superficie<br>(m2)|Altura<br>m.s.n.m|Altura<br>de<br>emisión|Sigma<br>inicial|Mese<br>que<br>emite|Periodo<br>de<br>emisión|
|---|---|---|---|---|---|---|---|---|---|
|SCR_1|AREA-<br>POLYGONAL|Movimientos<br>de tierra|-|42.339|481,17|0|0|12<br>meses|Lunes a<br>viernes<br>de 08:00<br>- 18:00|

Página **22** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

|Cod.<br>de la<br>fuente|Fuente|Descripción|Longitud<br>(km)|Superficie<br>(m2)|Altura<br>m.s.n.m|Altura<br>de<br>emisión|Sigma<br>inicial|Mese<br>que<br>emite|Periodo<br>de<br>emisión|
|---|---|---|---|---|---|---|---|---|---|
|SCR_2|ROAD|Tránsito<br>caminos no<br>pavimentados<br>construcción|7,24|-|480|0,5|0|12<br>meses|Lunes a<br>viernes<br>de 08:00<br>- 18:00|
|SCR_3|ROAD|Tránsito<br>caminos<br>pavimentados<br>construcción|133,80|-|470 - 530|0,5|0|12<br>meses|Lunes a<br>viernes<br>de 08:00<br>- 18:00|
|SCR_5|ROAD|Tránsito<br>caminos<br>pavimentados<br>operación|4,67|-|470 -<br>530|0,5|0|12<br>meses|Continuo|
|SCR_6|POINT|Zona grupo<br>electrógeno|-|-|480|0,8|0|-|0,94 al<br>año|

Fuente: Elaborado por FCM, 2025.

**Figura 4. Fuentes de emisión del Proyecto**

Fuente: Elaborado por FCM, 2025.

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Página **23** de **89**

Modelación atmosférica
“Parque Las Alamedas I,II y III”

A continuación, en la siguiente Tabla se presenta, la tasa de emisión de cada fuente
considerada en la modelación.

**Tabla 9. Tasas de emisión (ton/año) de cada fuente generadora de emisiones**

|Código de<br>fuente|Tasa de emisión (ton/año)|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Código de**<br>**fuente**|**MP10**|**MP2,5**|**NOX **|**SO2 **|**CO**|
|SCR_1|6,25E-2|5,45E-2|1,16|1,60E-3|4,05E-1|
|SCR_2|3,66E-1|3,67E-2|2,50E-2|2,00E-6|6,00E-4|
|SCR_3|7,38E-2|2,66E-2|1,10E-1|1,00E-4|4,57E-2|
|SCR_5|8,14E-1|1,98E-1|1,40E-|1,03E-3|1,25|
|SCR_6|4,34E-4|4,34E-4|5,31E-2|1,15E-3|1,40E-3|
|**Total**|**1,32**|**0,32**|**1,35**|**3,88E-3**|**1,70**|

Fuente: Elaboración propia, 2025.

Dado que las fuentes son del tipo “ROAD”, “AREA-POLYGONAL” y “POINT”, se deben realizar
los siguientes cambios de unidades para ser ingresadas al software.

 - ROAD

[(g)] 1 (año)

1 (ton) [∙] 31.536.000 (s)

INPUT ~~(~~ [g]

m∙s [) =]

Tasa de emisión ~~(~~ [ton]

Longitud (km) ∙ [1000 ][(][m][)]

1 (km)

[ton]

año ~~[)]~~ [ ∙10] 1 [6] ton [(g)]

- AREA - POLYGONAL

INPUT(m [2] g· s [) =]

- POINT

[ton]

año ~~[)]~~ [ ∙10] 1 [6] ton [(g)]

[ton] [(g)] 1 (año)

año ~~[)]~~ [ ∙10] 1 (ton) [∙] 31.536.000 (s)

Superficie de impacto (m [2] )

Tasa de emisión ( [ton]

[g] s [) = Tasa de emisión (ton] año

[(g)] 1 (año)

1 (ton) [∙] 31.536.000 (s)

INPUT( [g]

año ~~[)]~~ [ ∙10] [6] [(g)]

Por lo tanto, tras la conversión de unidades se tienen las siguientes tasas de emisión.

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Página **24** de **89**

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Tabla 10. INPUT Software CALPUFF**

|Código de<br>fuente|INPUT software*|Col3|Col4|Col5|Col6|Unidad|
|---|---|---|---|---|---|---|
|**Código de**<br>**fuente**|**MP10**|**MP2,5**|**NOX **|**SO2 **|**CO**|**CO**|
|SCR_1|4,67E-08|4,07E-08|8,68E-07|1,20E-09|3,03E-07|g/m2·s|
|SCR_2|1,60E-06|1,61E-07|1,09E-08|8,76E-12|2,63E-09|g/m·s|
|SCR_3|1,75E-08|6,31E-09|2,60E-08|2,37E-11|1,08E-08|g/m·s|
|SCR_5|5,53E-06|1,34E-06|9,51E-07|6,99E-09|8,46E-06|g/m·s|
|SCR_6|1,38E-05|1,38E-05|1,68E-03|3,65E-05|4,44E-05|g/s|

Fuente: Elaboración propia, 2025.

**6.5.** **Análisis de incertidumbre**

**6.5.1.** **Modelo Meteorológico**

De acuerdo con lo recomendado por la Guía para el uso de Modelos de Calidad del Aire en
el SEIA, se utilizó la meteorología del modelo meteorológico WRF, la cual fue ingresa como
datos de entrada para el modelo CALPUFF para la modelación de emisiones atmosféricas.

Los datos del modelo WRF son los siguientes:

 - Periodo modelado: 2024-01-01 00:00:00 - 2025-01-02 20:00:00

 - Coordenadas del dominio:

`o` RLAT0 = 34.159S

`o` RLON0 = 70.767W

`o` XLAT1 = 34.399S

`o` XLAT2 = 33.919S

 Proyección: Lambert Conic Conformal (LCC)

 Resolución (grilla): 1 x 1 (km [2] )

 Tamaño del dominio: 50 x 50 (km [2] )

 - Zona Horario: UTC/GMT UTC -4 horas

 - Datum: NWS-84

Los datos meteorológicos utilizados para el análisis de incertidumbre del modelo
meteorológico se obtuvieron de las estaciones Rancagua I, y Rancagua II, cuyo propietario
es el Ministerio del Medio Ambiente y su operador es Algoritmos y Mediciones Ambientales
SpA.

A continuación, en la siguiente Tabla se presenta la información geográfica y las variables
utilizadas para la validación de los datos.

Página **25** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Tabla 11. Estación utilizada para la validación del modelo WRF**

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
|Rancagua II|Meteorológicos|339.842|6.220.527|Temperatura|Temperatura|

Fuente: Elaboración propia, 2025.

El periodo de información descargado corresponde al año 2024, el cual es el mismo año de

los datos del modelo WRF.

Además, se señala que la estación de monitoreo cumple con los requisitos establecidos por
el Servicio de Evaluación Ambiental (SEA) en su “Guía para el uso de modelos de calidad
del aire en el SEIA” (2023), cumpliendo con el mínimo requerido de datos válidos para las
variables meteorológicas, los cual corresponde a un 75% de los registros mínimos.

**6.5.2.** **Análisis cualitativo**

A continuación, se presenta el análisis cualitativo de las variables meteorológicas medidas
en las estaciones Rancagua I, y Rancagua II del Ministerio del Medio Ambiente y los datos
modelados (WRF).

**6.5.2.1.** **Velocidad del viento**

En la siguiente Figura se presenta la serie de tiempo para la velocidad del viento de la
estación de monitoreo Rancagua I y Rancagua II.

Página **26** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 5. Datos velocidad del viento WRF Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 6. Datos velocidad del viento estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Página **27** de **89**

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 7. Datos velocidad del viento WRF Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 8. Datos velocidad de viento observada en estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **28** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 9. Promedio horario velocidad del viento (m/s) WRF Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 10. Promedio horario velocidad del viento (m/s) estación Rancagua I**

Fuente: Elaboración propia, 2025.

Página **29** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 11. Promedio horario velocidad del viento (m/s) WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 12. Promedio horario velocidad del viento (m/s) estación Rancagua II**

Fuente: Elaboración propia 2025.

Página **30** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**6.5.2.2.** **Dirección del Viento**

En la siguientes Figuras se presenta los valores de la dirección del viento para las estaciones
Rancagua I, Rancagua II y WRF.
**Figura 13. Dirección del viento (°) estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 14. Dirección del viento (°) WRF Rancagua I**

Fuente: Elaboración propia, 2025.

Página **31** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 15. Dirección del viento (°) estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 16. Dirección del viento (°) WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Página **32** de **89**

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 17. Promedio horario dirección del viento WRF Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 18. Promedio horario dirección del viento estación Rancagua I.**

Fuente: Elaboración propia, 2025.

Página **33** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 19. Promedio horario dirección del viento WRF Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 20. Promedio horario dirección del viento estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **34** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 21. Ciclo horario y mensual dirección y velocidad del viento estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 22. Ciclo horario y mensual dirección y velocidad del viento WRF Rancagua I**

Fuente: Elaboración propia, 2025.

Página **35** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 23.Ciclo horario y mensual dirección y velocidad del viento WRF estación**

**Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 24.Ciclo horario y mensual dirección y velocidad del viento estación Rancagua II**

Página **36** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

Fuente: Elaboración propia, 2025. Para el caso de los datos de dirección del viento observados

en las figuras anteriores, e posible observar que presentan la misma tendencia, lo que

indica un comportamiento modelado cercano a la realidad de los datos medidos en la

estación meteorológica en estudio.

**6.5.2.3.** **Humedad**

Las siguientes Figuras presenta la comparación entre los datos observados en la estación
Rancagua I, Rancagua II y obtenido del modelo WRF para la variable Humedad.

**Figura 25. % humedad modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

Página **37** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 26. % humedad estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 27.% humedad modelo WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Página **38** de **89**

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 28. % humedad estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 29. Promedio horario % humedad estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Página **39** de **89**

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 30. Promedio horario % humedad modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 31.Promedio horario % humedad estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **40** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 32.Promedio horario % humedad modelo WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 33. Promedio horario y mensual % de humedad modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

Página **41** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 34. Promedio horario y mensual % de humedad estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 35. Promedio horario y mensual % de humedad modelo WRF estación Rancagua**

**II**

Fuente: Elaboración propia, 2025.

Página **42** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 36. Promedio horario y mensual % de humedad estación Rancagua II**

Fuente: Elaboración propia, 2025.

**6.5.2.4.** **Temperatura**

A continuación, en las siguiente Figura se presenta la gráfica comparativa entre la estación
Meteorológica principal, Puchuncavi y el modelo WRF.

Página **43** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 37. Temperatura (°C) modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 38. Temperatura (°C) estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Página **44** de **89**

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 39. Temperatura (°C) modelo WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 40. Temperatura (°C) estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **45** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 41. Promedio horario de temperatura (°C) modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 42. Promedio horario de temperatura (°C) estación Rancagua I**

Fuente: Elaboración propia, 2025.

Página **46** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 43. Promedio horario de temperatura (°C) modelo WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 44. Promedio horario de temperatura (°C) estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **47** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 45. Promedio horario y mensual de temperatura (°C) modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 46. Promedio horario y mensual de temperatura (°C) estación Rancagua I**

Fuente: Elaboración propia, 2025.

Página **48** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 47. Promedio horario y mensual temperatura (°C) modelo WRF estación**

**Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 48. Promedio horario y mensual de temperatura (°C) estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **49** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**6.5.2.5.** **Rosa de los vientos**

A continuación, se presenta la comparación de la rosa de los vientos para la estación
Rancagua I y II; y el modelo WRF.

**Figura 49. Rosa de los vientos noche modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 50. Rosa de los vientos noche estación Rancagua I**

Fuente: Elaboración propia, 2025.

Página **50** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 51. Rosa de los vientos mañana, modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 52. Rosa de los vientos mañana, estación Rancagua I**

Fuente: Elaboración propia, 2025.

Página **51** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 53. Rosa de los vientos tarde, modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 54. Rosa de los vientos tarde, estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Página **52** de **89**

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 55. Rosa de los vientos diaria, modelo WRF Rancagua I**

Fuente: Elaboración propia, 2025.

**Figura 56. Rosa de los vientos diaria, estación Rancagua I**

Fuente: Elaboración propia, 2025.

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Página **53** de **89**

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 57. Rosa de los vientos noche WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 58. Rosa de los vientos noche estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **54** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 59. Rosa de los vientos mañana WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 60. Rosa de los vientos mañana estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **55** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 61.Rosa de los vientos tarde WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 62.Rosa de los vientos tarde estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Página **56** de **89**

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 63. Rosa de los vientos diaria WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

**Figura 64. Rosa de los vientos diaria WRF estación Rancagua II**

Fuente: Elaboración propia, 2025.

Página **57** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**6.5.3.** **Análisis cuantitativo**

El análisis cualitativo se realizado de acuerdo con lo recomendado por la Guía para uso de
Modelos de Calidad del Aire en el SEIA, 2023 utilizando las métricas estadísticas del sesgo
(error medio o BIAS), error absoluto medio (MAE) y la raíz del error cuadrático medio
(RMSE). Las ecuaciones para cada una de las métricas se presentan a continuación.

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

O: Valores observados en estaciones meteorológicas

A su vez, se incorpora de acuerdo con lo recomendado en la Guía mencionada, el cálculo
del coeficiente de correlación (r), que corresponde a una correlación lineal entre los valores
modelados y observados. Para medir el coeficiente de correlación lineal, se utilizan valores
que oscilan entre -1 y 1. Un valor de -1 indica una correlación negativa, lo que significa que
cuando aumenta el valor de una variable, la otra disminuye, y viceversa. Por otro lado, un
valor de 1 indica la máxima correlación positiva, lo que implica que ambas variables se
mueven en la misma dirección: cuando una aumenta, la otra también lo hace, y cuando una
disminuye, la otra también lo hace.

**Tabla 12. Estadísticos de sesgo, error absoluto medio y error cuadrático medio**

|Estación|Variable<br>meteorológica|BIAS|MAE|RMSE|r|
|---|---|---|---|---|---|
|Rancagua I|Velocidad del viento<br>(m/s)|-0,56|0,58|0,79|0,90|
|Rancagua I|Temperatura (°C)|-1,57|-1,57|1,90|0,97|
|Rancagua II|Velocidad del viento<br>(m/s)|-0,48|0,48|0,67|0,93|

Página **58** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

|Estación|Variable<br>meteorológica|BIAS|MAE|RMSE|r|
|---|---|---|---|---|---|
||Temperatura (°C)|-1,96|1,96|2,4|0,98|
|Límite*|Velocidad del viento<br>(m/s)|(-2,5;2,5) (m/s)|≤ 3 (m/s)|≤ 3,5 (m/s)|>0,6|
|Límite*|Temperatura (°C)|(-4,4) (°C)|≤ 4 (°C)|≤ 4,5 (°C)|>0,8|
|*Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”,<br>Guía para el uso de modelos de Calidad del Aire en el SEIA.|*Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”,<br>Guía para el uso de modelos de Calidad del Aire en el SEIA.|*Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”,<br>Guía para el uso de modelos de Calidad del Aire en el SEIA.|*Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”,<br>Guía para el uso de modelos de Calidad del Aire en el SEIA.|*Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”,<br>Guía para el uso de modelos de Calidad del Aire en el SEIA.|*Tabla 2 “Métrica estadísticas recomendables en el análisis de incertidumbre para las variables meteorológicas medias”,<br>Guía para el uso de modelos de Calidad del Aire en el SEIA.|

Fuente: Elaboración propia, 2025.

Para la estación Rancagua I en comparación a las métricas estadísticas recomendables en
el análisis de incertidumbre para la variable meteorológica de temperatura (°C) de -1,57
para el error cuadrático medio (BIAS), 1,57, para el valor absoluto (MAE) y 1,90 para el
error cuadrático medio (RMSE), teniendo que se encuentran dentro de las métricas
estadísticas recomendadas por la Guía para el uso de Modelos de Calidad del Aire. Además,
el coeficiente de correlación lineal de 0,97, el cual representa una buena aproximación.

Para la variable velocidad del viento (m/s) se tiene un valor del error cuadrático medio
(BIAS) de -0,56, error absoluto (MAE) de 0,58 y error cuadrático medio (RMSE) de 0,79,
teniendo que, los valores se encuentran dentro de las métricas estadísticas recomendables
por la Guía para el uso de Modelos de Calidad del Aire. Además, cabe mencionar que, el
coeficiente de correlación tiene un valor de 0,90, el cual representa una buena aproximación.

Respecto a la estación Rancagua II se tiene que, en comparación a las métricas estadísticas
recomendables en el análisis de incertidumbre para la variable meteorológica de
temperatura (°C) de -1,96 para el error cuadrático medio (BIAS), 1,96, para el valor absoluto
(MAE) y 2,4 para el error cuadrático medio (RMSE), teniendo que se encuentran dentro de
las métricas estadísticas recomendadas por la Guía para el uso de Modelos de Calidad del
Aire. Además, el coeficiente de correlación lineal de 0,98, el cual representa una buena
aproximación.

Para la variable velocidad del viento (m/s) se tiene un valor del error cuadrático medio
(BIAS) de -0,48, error absoluto (MAE) de 0,48 y error cuadrático medio (RMSE) de 0,67,
teniendo que, los valores se encuentran dentro de las métricas estadísticas recomendables
por la Guía para el uso de Modelos de Calidad del Aire. Además, cabe mencionar que, el
coeficiente de correlación tiene un valor de 0,93, el cual representa una buena aproximación.

Del análisis se concluye que los datos presentados en el WRF tienen una fiabilidad aceptable
para realizar la modelación de dispersión de contaminantes atmosféricos.

Página **59** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**6.6.** **Topografía**

La información se obtuvo de las cartas topográficas SRTM1, con una resolución aproximada

de 30 metros cuadrados.

**Figura 65. Información topográfica**

Fuente: Elaboración propia, 2025.

**Figura 66. Elevación de la zona de modelación - CALPUFF 3D**

Fuente: Elaboración propia, 2025.

Página **60** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**6.7.** **Caracterización Ambiental del Proyecto**

La caracterización ambiental del Proyecto se realiza utilizando los datos recopilados por la
estación de monitoreo ubicada en las cercanías del Proyecto y que cumpla con los
requerimientos establecidos.

La estación de monitoreo utilizada más cercana, con una base consolidada de información
es la estación Rancagua II, ubicada en la comuna de Rancagua, Provincia de Cachapoal,
Región del Libertador General Bernardo O’Higgins a una distancia de 3,03 km del Proyecto.
Los datos extraídos para la caracterización fueron extraídos del Sistema de Información
Nacional de Calidad del Aire (SINCA) el 11 de febrero de 2025.

**6.7.1.** **Material Particulado Respirable (MP** **10** **)**

En la siguiente Figura, se presentan las series de tiempo correspondiente a las
concentraciones promedio anuales para el MP 10 para los años 2022, 2023 y 2024 (últimos 3
años).

**Figura 67. Registro diario. Promedio anual MP** **10** **Estación Rancagua II**

Fuente: Base SINCA, 2025.

Página **61** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 68. Concentración diaria MP** **10** **Estación Rancagua II**

Fuente: Base SINCA, 2025.

A continuación, en las siguientes Tablas, se muestran la concentración media anual y el
percentil 98 de las concentraciones de MP 10 registradas en la estación Rancagua II.

**Tabla 13. Concentración Media Anual de MP** **10** **(ug/m** **[3]** **N)**

|Estación|Norma primaria de MP (D.S. N° 12/2021 del MMA)<br>10<br>- Media Anual|Col3|Col4|Trianual|Porcentaje de<br>la norma|
|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 50 (ug/m3N)**|**Valor Norma: 50 (ug/m3N)**|**Valor Norma: 50 (ug/m3N)**|**Valor Norma: 50 (ug/m3N)**|**Valor Norma: 50 (ug/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2022**|**2023**|**2024**|**2024**|**2024**|
|Rancagua II|43,81|44,93|58,74|49,16|98,33%|

Fuente: Elaboración propia, en base a datos del Sistema Nacional de Calidad del Aire (SINCA),

2025.

Página **62** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Tabla 14. Percentil 98 concentración 24 horas de MP** **10** **(ug/m** **[3]** **N)**

|Estación|Norma primaria de MP (D.S. N° 12/2021 del<br>10<br>MMA) - 24 H|Porcentaje de la norma|
|---|---|---|
|**Estación**|**Valor norma: 130 (ug/m3N)**|**Valor norma: 130 (ug/m3N)**|
|**Estación**|**Año**|**Año**|
|**Estación**|**2024**|**2024**|
|Rancagua II|145,96|112,27%|

Fuente: Elaboración propia, en base a datos del Sistema Nacional de Calidad del Aire (SINCA),

2025.

**6.7.2.** **Material Particulado Respirable Fino (MP** **2,5** **)**

En la siguiente Figura, se presentan las series de tiempo correspondientes a las
concentraciones promedio anuales para el contaminante MP 2,5 para los años 2022, 2023 y
2024 (últimos 3 años) en la estación Rancagua II.

**Figura 69. Registro diario. Promedio anual MP** **2,5** **Estación Rancagua II**

Fuente: Base SINCA, 2025.

Página **63** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 70. Concentración diaria de MP** **2,5** **Estación Rancagua II**

Fuente: Base SINCA, 2025.

En las siguientes Tablas, se detalla la concentración media anual y el percentil 98 de las
concentraciones de MP 2,5 registradas en la estación Rancagua II.

**Tabla 15. Concentración Media Anual de MP** **2,5** **(ug/m** **[3]** **N)**

|Estación|Norma primaria de MP (D.S. N° 12/2021 del<br>2,5<br>MMA) - Media Anual|Col3|Col4|Trianual|Porcentaje de<br>la norma|
|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 20 (ug/m3N)**|**Valor Norma: 20 (ug/m3N)**|**Valor Norma: 20 (ug/m3N)**|**Valor Norma: 20 (ug/m3N)**|**Valor Norma: 20 (ug/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2022**|**2023**|**2024**|**2024**|**2024**|
|Rancagua II|29,63|22,96|24,14|25,58|127,90%|

Fuente: Elaboración propia, en base a datos del Sistema Nacional de Calidad del Aire (SINCA),

2025.

Página **64** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Tabla 16. Percentil 98 concentración 24 horas de MP** **2,5** **(ug/m** **[3]** **N)**

|Estación|Norma primaria de MP (D.S. N° 12/2011 del<br>2,5<br>MMA) - 24 H|Porcentaje de la norma|
|---|---|---|
|**Estación**|**Valor norma: 50 (ug/m3N)**|**Valor norma: 50 (ug/m3N)**|
|**Estación**|**Año**|**Año**|
|**Estación**|**2024**|**2024**|
|Rancagua II|87|174%|

Fuente: Elaboración propia, en base a datos del Sistema Nacional de Calidad del Aire (SINCA),

2025.

**6.7.3.** **Dióxido de azufre (SO** **2** **)**

La estación Rancagua II no presenta mediciones de SO 2 .

**6.7.4.** **Óxidos de nitrógeno (NO** **x** **)**

La estación Rancagua II no presenta mediciones de NO x .

**6.7.5.** **Monóxido de carbono (CO)**

La estación Rancagua II no presenta mediciones de CO.

# 7. Resultados

A continuación, se entregan las concentraciones obtenidas utilizando el modelo
meteorológico de meso escala Weather Research Forecasting Modelo (WRF), como insumo
para el software CALPUFF View.

De esta forma fue posible obtener las concentraciones de Material Particulado y gases de
combustión en cada receptor y definir el receptor que presenta la máxima concentración
para cada compuesto evaluado.

En virtud de los resultados de la modelación a continuación se presentan las concentraciones
de los contaminantes de MP 10, MP 2,5, CO, NO x y SO x, según periodos versus el valor norma
de calidad primaria. Junto a ello, el valor de la línea base de calidad de aire en área de
influencia. (En caso de aplicar).

Respecto a las concentraciones modeladas, se tiene que estas son comparadas con la
normativa ambiental aplicable al Proyecto, es decir, las Normas de Calidad Primaria
consideradas para la evaluación del riesgo sobre la salud de la población identificada.

Página **65** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

A continuación, en la siguiente Tabla se presentan los umbrales de las normas citadas.

**Tabla 17. Normas de calidad primaria**

|Normativa|Límite|Concentración|
|---|---|---|
|D.S. N° 12/2022 del MMA Norma de calidad de aire para el<br>MP10|130 μg/m3|Diaria|
|D.S. N° 12/2022 del MMA Norma de calidad de aire para el<br>MP10|50 μg/m3|Anual|
|D.S. N° 12/2010 del MMA Norma de calidad de aire para el<br>MP2,5|50 μg/m3|Diaria|
|D.S. N° 12/2010 del MMA Norma de calidad de aire para el<br>MP2,5|20 μg/m3|Anual|
|D.S. N° 104/2018 del MMA Norma Primaria de Calidad del<br>aire para el SO2|60 μg/m3|Anual|
|D.S. N° 104/2018 del MMA Norma Primaria de Calidad del<br>aire para el SO2|150 μg/m3|Diaria|
|D.S. N° 104/2018 del MMA Norma Primaria de Calidad del<br>aire para el SO2|350 μg/m3|Horaria|
|D.S. N° 40/2024 del MMA Norma Primaria de calidad del aire<br>para NO2|40 μg/m3|Anual|
|D.S. N° 40/2024 del MMA Norma Primaria de calidad del aire<br>para NO2|100 μg/m3|Diaria|
|D.S. N° 40/2024 del MMA Norma Primaria de calidad del aire<br>para NO2|200 μg/m3|1 hora|
|D.S. N° 115/2002 del MINSEGPRES Norma Primaria de<br>calidad del aire para CO|10 mg/m3|8 horas|
|D.S. N° 115/2002 del MINSEGPRES Norma Primaria de<br>calidad del aire para CO|30 mg/m3|1 hora|

Fuente: Elaboración propia, 2025.

**7.1.** **Isoconcentración**

En las siguientes Figuras se presentan las curvas de iso concentración generadas mediante
el modelo Calpuff para los contaminantes Material Particulado Respirable (MP 10 ), Material
Particulado Fino Respirable (MP 2,5 ), Dióxido de Azufre (SO 2 ), Óxidos de Nitrógeno (NO x ) y
Monóxido de Carbono (CO).

Página **66** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 71. Mapa de Isoconcentración MP** **10** **concentración promedio anual**

Fuente: Elaboración propia, 2025.

**Figura 72. Mapa de Isoconcentración MP** **10** **P98 24H**

Fuente: Elaboración propia, 2025.

Página **67** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 73. Mapa de Isoconcentración MP** **2,5** **concentración promedio anual**

Fuente: Elaboración propia, 2025.

**Figura 74. Mapa Isoconcentración MP** **2,5** **P98 24H**

Fuente: Elaboración propia, 2025.

Página **68** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 75. Mapa de Isoconcentración SO** **2** **concentración promedio anual**

Fuente: Elaboración propia, 2025.

**Figura 76. Mapa de Isoconcentración SO** **2** **, concentración promedio 24H**

Fuente: Elaboración propia, 2025.

Página **69** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 77. Mapa de Isoconcentración SO** **2** **concentración P98,5 Horario**

Fuente: Elaboración propia, 2025.

**Figura 78. Mapa de Isoconcentración NO** **X** **concentración promedio anual**

Fuente: Elaboración propia, 2025.

Página **70** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 79. Mapa de Isoconcentración NO** **x** **, concentración P99 24 H**

Fuente: Elaboración propia, 2025.

**Figura 80. Mapa de Isoconcentración NO** **X** **, concentración P99 1H**

Fuente: Elaboración propia, 2025.

Página **71** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Figura 81. Mapa de Isoconcentración CO, concentración P99 1 hora**

Fuente: Elaboración propia, 2025.

**Figura 82. Mapa de Isoconcentración CO, concentración P99 8H**

Fuente: Elaboración propia, 2025.

Página **72** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**7.2.** **Aporte del Proyecto**

Para determinar el aporte del Proyecto se consideraron las concentraciones máximas
registradas para los periodos establecidos, los cuales se detallan, a continuación, en las
siguientes Tablas.

**Tabla 18. Aportes del Proyecto - concentraciones máximas registradas de MP** **10**

|Receptor|Normativa|Col3|Aporte del Proyecto (μg/m3)|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**24 horas**|**Anual**|**24 horas**|**% Norma**|**Anual**|**% Norma**|
|1|130|50|4,991E-1|0,38%|1,149E-1|0,23%|
|2|130|50|4,981E-1|0,38%|9,315E-2|0,19%|
|3|130|50|4,554E-1|0,35%|5,098E-2|0,10%|
|4|130|50|5,758E-1|0,44%|1,052E-1|0,21%|

Fuente: Elaboración propia, 2025.

**Tabla 19. Aportes del Proyecto - concentraciones máximas registradas de MP** **2,5**

|Receptor|Normativa|Col3|Aporte del Proyecto (μg/m3)|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**24 horas**|**Anual**|**24 horas**|**% Norma**|**Anual**|**% Norma**|
|1|50|20|3,039E-1|0,61%|8,023E-2|0,40%|
|2|50|20|2,532E-1|0,51%|6,012E-2|0,30%|
|3|50|20|1,940E-1|0,39%|2,439E-2|0,12%|
|4|50|20|2,308E-1|0,46%|5,461E-2|0,27%|

Fuente: Elaboración propia, 2025.

Página **73** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Tabla 20. Aportes del Proyecto - concentraciones máximas registradas de NO** **X**

|Receptor|Normativa|Col3|Col4|Aporte del Proyecto (μg/m3)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**1H**|**24H**|**Anual**|**1H**|**% **<br>**Norma**|**24H**|**% **<br>**Norma**|**Anual**|**% **<br>**Norma**|
|1|200|100|40|20,79|10,40%|6,647|6,65%|1,581|3,95%|
|2|200|100|40|16,91|8,46%|4,868|4,87%|1,134|2,84%|
|3|200|100|40|11,33|5,67%|3,132|3,13%|3,614E-1|0,90%|
|4|200|100|40|13,11|6,56%|3,478|3,48%|8,936E-1|2,23%|

Fuente: Elaboración propia, 2025.

**Tabla 21. Aportes del Proyecto - concentraciones máximas registradas de CO**

|Receptor|Normativa|Col3|Aporte del Proyecto (μg/m3)|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**1 hora**|**8 horas**|**1 hora**|**% Norma**|**8 horas**|**% Norma**|
|1|30.000|10.000|7,952|0,03%|3,80|0,04%|
|2|30.000|10.000|6,609|0,02%|3,19|0,03%|
|3|30.000|10.000|4,823|0,02%|2,32|0,02%|
|4|30.000|10.000|5,936|0,02%|2,62|0,03%|

Fuente: Elaboración propia, 2025.

**Tabla 22. Aportes del Proyecto - concentraciones máximas registradas de SO** **2**

|Receptor|Normativa|Col3|Col4|Aporte del Proyecto (μg/m3)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Horario**|**Diario**|**Anual**|**Horario**|**% Norma**|**Diario**|**% Norma**|**Anual**|**% Norma**|
|1|350|150|60|2,929E-2|0,01%|9,400E-3|0,01%|2,226E-3|0,004%|
|2|350|150|60|2,427E-2|0,01%|6,964E-3|0,005%|1,626E-3|0,003%|
|3|350|150|60|1,653E-2|0,005%|4,757E-3|0,003%|5,377E-4|0,001%|
|4|350|150|60|1,953E-2|0,01%|4,807E-3|0,003%|1,293E-3|0,002%|

Fuente: Elaboración propia, 2025.

Se puede observar que las concentraciones generadas por el Proyecto se mantienen por
debajo de los límites establecidos en la normativa de calidad de aire primaria para los

Página **74** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

compuestos evaluados, teniendo que las emisiones son poco significativas, debido a que se
encuentran alejados de los valores establecidos en la normativa aplicable.

**7.3.** **Evaluación del impacto de las emisiones atmosféricas del material**

**particulado MP** **10** **y MP** **2,5** **en zonas saturadas**

La Guía “Criterio de evaluación en el SEIA: Impacto de emisiones en zonas saturadas por
material particulado respirable MP 10 y material particulado fino respirable MP 2,5 ” en adelante
la “Guía”, establece los criterios para definir el concepto de “aumento o disminución
significativos”, concepto contenido en el literal a) del artículo 5° del Reglamento del SEIA,
para la evaluación del riesgo para la salud y el uso de normas primarias de calidad ambiental
vigentes.

El presente Proyecto se ubica en la Región del Libertador General Bernardo O’Higgins, la
cual se encuentra declarada como saturada por MP 10, como concentración anual y de 24
horas según D.S N°7/2009 y saturada por MP 2,5 como concentración anual y de 24 horas
según D.S. N°42/2017.

**Figura 83. Ubicación del Proyecto en relación con la zona saturada o latente**

Fuente: Capítulo 1 “Descripción de Proyecto”, 2025.

Página **75** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

A continuación, se presenta el resumen de las emisiones totales por cada año y cada
contaminante (MP 10 y MP 2,5 ), para cada una de las fases del Proyecto.

**Tabla 23. Resumen de emisiones total por cada año para el MP** **10**

|Fase|Col2|MP (ton/año)<br>10|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Fase**|**Año 1**|**Año 2**|**Año 3**|**Año 4**|**Año 6**|**Año “n” ***|
|Construcción|1,011|0,423|0,502|-|-|-|
|Operación|-|0,135|0,815|1,231|1,231|1,231|
|**Total**|**1,011**|**0,558**|**1,317**|**1,231**|**1,231**|**1,231**|
|*El Proyecto no contempla fase de cierre.|*El Proyecto no contempla fase de cierre.|*El Proyecto no contempla fase de cierre.|*El Proyecto no contempla fase de cierre.|*El Proyecto no contempla fase de cierre.|*El Proyecto no contempla fase de cierre.|*El Proyecto no contempla fase de cierre.|

Fuente: Elaboración propia, 2025.

**Tabla 24. Resumen de emisiones total por cada año para el MP** **2,5**

|Fase|Col2|MP (ton/año)<br>2,5|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Fase**|**Año 1**|**Año 2**|**Año 3**|**Año 4**|**Año 6**|**Año “n” ***|
|Construcción|0,251|0,094|0,118|-|-|-|
|Operación|-|0,033|0,198|0,299|0,299|0,299|
|**Total**|**0,251**|**0,127**|**0,316**|**0,299**|**0,299**|**0,299**|
||*El Proyecto no contempla fase de cierre.|*El Proyecto no contempla fase de cierre.|*El Proyecto no contempla fase de cierre.|*El Proyecto no contempla fase de cierre.|*El Proyecto no contempla fase de cierre.|*El Proyecto no contempla fase de cierre.|

Fuente: Elaboración propia, 2025.

De las Tablas anteriores se observa que la generación máxima de emisiones se da en el
tercer año, correspondiente a la construcción de la etapa 3, operación total de la etapa 1 y
la operación parcial de la etapa 2.

Tras analizar la aplicabilidad de la Tabla 1 y 2 del Anexo A de la Guía Criterio de Evaluación
en el SEIA “Impactos de emisiones en zonas saturadas por material particulado respirable
MP 10 y material particulado respirable fino MP 2,5 ” (SEA, 2023), se tiene que el presente
Proyecto no corresponde a ninguno de los 3 casos expuestos, debido a que, no corresponde
a un proyecto en el cual se produce la fase de construcción y operación de forma secuencial
(que no se superponen) como establece el caso 1, no corresponde a un proyecto de
continuidad operacional como establece el caso 2 y no corresponde a un proyecto que
considera la extensión y ampliación de su vida útil como establece el caso 3. Teniendo que
corresponde a un Proyecto nuevo ingreso a evaluación ambiental, donde sus fases de
construcción y operación se ven solapadas, durante el año 2 y 3. Por lo tanto, y producto
de su semejanza, el presente Proyecto se analizará con respecto al caso 2 del Anexo A de
la Guía, considerando el año 3 como el más desfavorable, pero como si este tuviera una
extensión mayor o igual a 3 años, aplicando los valores correspondientes a la Tabla 1 de la
Guía, cuyo análisis se presenta, a continuación, en la siguiente Tabla.

Página **76** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Tabla 25. Comparación de los resultados de la modelación en receptores humanos y**

**valores de significancia de la Tabla 1 de la Guía para el año 3 del Proyecto.**

|Receptores|MP (ug/m3)<br>10|Col3|MP (ug/m3)<br>2,5|Col5|
|---|---|---|---|---|
|**Receptores**|**24 H P98**|**Anual**|**24 H P98**|**Anual**|
|1|4,991E-1|1,149E-1|3,039E-1|8,023E-2|
|2|4,981E-1|9,315E-2|2,532E-1|6,012E-2|
|3|4,554E-1|5,098E-2|1,940E-1|2,439E-2|
|4|5,758E-1|1,052E-1|2,308E-1|5,461E-2|
|**Valor significancia Tabla 1**|**5,00**|**1,00**|**1,71**|**0,33**|

Fuente: Elaboración propia, 2025.

De acuerdo con la Tabla anterior, la concentración de material particulado de MP 10 y MP 2,5
en los receptores humanos, se encuentra **por debajo de los valores de significancia**
**establecidos para la Tabla, para el año que el Proyecto genera la mayor cantidad**
**de emisión.**

**7.4.** **Evaluación del efecto sinérgico**

Para el desarrollo del escenario sinérgico, se han considerado los siguientes criterios:

 Identificación del Proyectos aprobados en el SEIA cercanos en un radio de 2 km del
Proyecto en evaluación

 RCA aprobada no mayor a 5 años. Se asume que mayor a esos años los proyectos
ya estarían operando y, por lo tanto, las emisiones estarían siendo registradas en la
estación de calidad del aire.

 Revisión del estado en que se encuentran los proyectos aprobados en el sitio web
de SMA/SNIFA

 Efectuar el análisis de la información, basado en los antecedentes disponibles
entregados por los titulados de los proyectos aprobados

 Los contaminantes considerados para el análisis de escenario sinérgico corresponden
al MP 10 y MP 2,5

A continuación, se presenta el listado de proyectos identificado en el SEIA, según los criterios

mencionados.

Página **77** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Tabla 26. Proyectos Aprobados o en Calificación Ambiental en las cercanías al Proyecto**

**Planta Solar El Cardonal**

|ID|Nombre|Titular|Fecha<br>Ingreso al<br>Sistema|Estado|Distancia al<br>Proyecto|
|---|---|---|---|---|---|
|1|Parrones de Baquedano|Inmobiliaria San<br>Ramón I SPA|07/10/2021|Aprobado|0,94 km|

Fuente: Elaboración propia, 2025.

A continuación, en la siguiente Tabla se evalúa si existe solapamiento entre las fases de
construcción de los proyectos citados anteriormente.

**Tabla 27. Evaluación de solapamiento fase de construcción**

|Proyecto|Fecha de<br>inicio|Fecha de término|¿Existe<br>solapamiento?|
|---|---|---|---|
|Parrones de Baquedano|Primer<br>semestre 2022|Segundo semestre<br>2024|No|

Fuente: Elaboración propia, 2025.

De lo anterior, se tiene que para el proyecto “Parrones de Baquedano” sólo se considerarán
las emisiones generadas durante su fase de operación.

A continuación, en la siguiente Tabla se presentan las tasas a considerar para el análisis del
efecto sinérgico del Proyecto.

**Tabla 28. Tasas de emisión a considerar para la evaluación del efecto sinérgico**

|Proyecto|Tasa de emisión (ton/año)|Col3|Fuente|
|---|---|---|---|
|**Proyecto**|**MP10**|**MP2,5**|**MP2,5**|
|Parrones de Baquedano|0,4826|0,1173|Anexo 3 ADENDA<br>Complementaria|

Fuente: Elaboración propia, 2025.

Para evaluar los efectos se realiza una modelación de los receptores discretos del Presenta
Proyecto para el MP 10 y MP 2,5, donde se obtienen los siguientes resultados.

Página **78** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Tabla 29. Resultados aporte proyectos cercanos en receptores**

|Receptor|Métrica|Aporte proyecto cercanos (μg/m3)|Col4|D.S. N°<br>12/2022 del<br>MMA|D.S. N°<br>12/2011 del<br>MMA|
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

Los aportes de MP 10 generados por proyecto cercanos en todos los receptores evaluados en
la presente evaluación son bajos, con valores que oscilan en el orden de los -2 al -1 en
términos anuales y diarios, los cuales están por muy por debajo de los límites establecidos
por la normativa (50 μg/m3 anual y 130 μg/m3 diario). Por lo mismo, se concluye que, el
impacto de las emisiones de proyectos cercanos en los niveles de MP 10 es poco significativo.

 - **Aporte de MP** **2,5**

De igual manera, para el MP 2,5 también se tiene que los aportes de los proyectos cercanos
son mínimos, teniendo valores diarios y anuales del orden de los -1 y -2, resultados que
están muy por debajo de los límites normativos (20 μg/m3 anual y 50 μg/m3 diario).

Por lo tanto, se tiene que, las emisiones generadas por otros proyectos son poco
significativas y despreciables, dado que los valores obtenidos en los receptores de la
presente evaluación se encuentran muy por debajo de los límites normativos establecidos
en el D.S. N° 12/2022 del MMA para el MP 10 y el D.S. N° 12/2011 del MMA para el MP 2,5 .
Por ende, se desestima la implementación de medidas adicionales de mitigación y
coordinación asociadas a efectos sinérgicos con otros Proyectos.

Página **79** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**7.5.** **Evaluación de los niveles de concentración**

Para evaluar los niveles de concentración de los contaminantes generados como resultados
del quinto año del Proyecto, se realizará una comparación entre estos valores, la condición
basal obteniendo a partir de la estación Rancagua II (Caracterización de calidad del aire
obtenidos del SINCA), así como con la normativa primaria correspondiente a la calidad
ambiental y el aporte de otros proyectos. Es preciso indicar que dicha estación no presenta
datos de SO 2, NO x y CO, por lo que la comparativa se realizará en función del MP 10 y MP 2,5 .

La concentración total se obtendrá sumando la línea de base proveniente de la estación
Rancagua II, proyectos cercanos y la contribución adicional del proyecto en los receptores
de interés definidos, de acuerdo con la siguiente formulación:

Concentración Total= Línea de base+ Aporte Total del Proyecto+ Aporte de otros Proyectos

**Tabla 30. Concentraciones totales de MP** **10**

|Receptores|Coordenadas UTM<br>(m)|Col3|Métrica|Condición<br>o línea de<br>base<br>(μg/m3)|Aporte<br>proyecto<br>(μg/m3)|Aporte<br>otros<br>proyectos<br>con RCA<br>(μg/m3)|Concentración<br>final (μg/m3)|Norma|
|---|---|---|---|---|---|---|---|---|
|**Receptores**|**Este**|**Norte**|**Norte**|**A **|**B **|**C **|**A + B +C**|**A + B +C**|
|1|337.026|6.218.934|Anual|49,16|1,15E-1|7,26E-02|49,348|50|
|1|337.026|6.218.934|24 H|145,96|4,99E-1|2,92E-01|146,751|130|
|2|336.990|6.218.793|Anual|49,16|9,32E-2|1,18E-01|49,371|50|
|2|336.990|6.218.793|24 H|145,96|4,98E-1|5,04E-01|146,962|130|
|3|337.023|6.218.680|Anual|49,16|5,10E-2|1,33E-01|49,344|50|
|3|337.023|6.218.680|24 H|145,96|4,55E-1|6,28E-01|147,043|130|
|4|337.194|6.218.998|Anual|49,16|1,05E-1|4,80E-02|49,313|50|
|4|337.194|6.218.998|24 H|145,96|5,76E-1|2,16E-01|146,752|130|

Fuente: Elaboración propia, 2025.

**Tabla 31. Concentraciones totales de MP** **2,5**

|Receptores|Coordenadas UTM<br>(m)|Col3|Métrica|Condición<br>o línea de<br>base<br>(μg/m3)|Aporte<br>proyecto<br>(μg/m3)|Aporte<br>otros<br>proyectos<br>con RCA<br>(μg/m3)|Concentración<br>final (μg/m3)|Norma|
|---|---|---|---|---|---|---|---|---|
|**Receptores**|**Este**|**Norte**|**Norte**|**A **|**B **|**C **|**A + B +C**|**A + B +C**|
|1|337.026|6.218.934|Anual|25,58|8,02E-2|1,77E-02|25,678|20|
|1|337.026|6.218.934|24 H|87|3,04E-1|7,09E-02|87,375|50|
|2|336.990|6.218.793|Anual|25,58|6,01E-2|2,86E-02|25,669|20|
|2|336.990|6.218.793|24 H|87|2,53E-1|1,23E-01|87,376|50|
|3|337.023|6.218.680|Anual|25,58|2,44E-2|3,24E-02|25,637|20|
|3|337.023|6.218.680|24 H|87|1,94E-1|1,53E-01|87,347|50|
|4|337.194|6.218.998|Anual|25,58|5,46E-2|1,17E-02|25,646|20|

Página **80** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

|Receptores|Coordenadas UTM<br>(m)|Col3|Métrica|Condición<br>o línea de<br>base<br>(μg/m3)|Aporte<br>proyecto<br>(μg/m3)|Aporte<br>otros<br>proyectos<br>con RCA<br>(μg/m3)|Concentración<br>final (μg/m3)|Norma|
|---|---|---|---|---|---|---|---|---|
|**Receptores**|**Este**|**Norte**|**Norte**|**A **|**B **|**C **|**A + B +C**|**A + B +C**|
|**Receptores**|||24 H|87|2,31E-1|5,24E-02|87,283|50|

Fuente: Elaboración propia, 2025.

**Tabla 32. Concentraciones totales de NO** **x**

|Receptores|Coordenadas UTM<br>(m)|Col3|Métrica|Condición<br>o línea de<br>base<br>(μg/m3)|Aporte<br>proyecto<br>(μg/m3)|Aporte<br>otros<br>proyectos<br>con RCA<br>(μg/m3)|Concentración<br>final (μg/m3)|Norma|
|---|---|---|---|---|---|---|---|---|
|**Receptores**|**Este**|**Norte**|**Norte**|**A **|**B **|**C **|**A + B +C**|**A + B +C**|
|1|337.026|6.218.934|Anual|-|1,58|-|1,58|40|
|1|337.026|6.218.934|24H||6,65||6,65|100|
|1|337.026|6.218.934|1H|-|20,79|-|20,79|200|
|2|336.990|6.218.793|Anual|-|1,13|-|1,13|40|
|2|336.990|6.218.793|24H||4,87||4,87|100|
|2|336.990|6.218.793|1H|-|16,91|-|16,91|200|
|3|337.023|6.218.680|Anual|-|3,61E-1|-|3,61E-1|40|
|3|337.023|6.218.680|24H||3,13||3,13|100|
|3|337.023|6.218.680|1H|-|11,33|-|11,33|200|
|4|337.194|6.218.998|Anual|-|8,94E-1|-|8,94E-1|40|
|4|337.194|6.218.998|24H||3,48||3,48|100|
|4|337.194|6.218.998|1H|-|13,11|-|13,11|200|

Fuente: Elaboración propia, 2025.

**Tabla 33. Concentraciones totales de CO**

|Receptores|Coordenadas UTM<br>(m)|Col3|Métrica|Condición<br>o línea de<br>base<br>(μg/m3)|Aporte<br>proyecto<br>(μg/m3)|Aporte<br>otros<br>proyectos<br>con RCA<br>(μg/m3)|Concentración<br>final (μg/m3)|Norma|
|---|---|---|---|---|---|---|---|---|
|**Receptores**|**Este**|**Norte**|**Norte**|**A **|**B **|**C **|**A + B +C**|**A + B +C**|
|1|337.026|6.218.934|8 H|-|3,80|-|3,80|10.000|
|1|337.026|6.218.934|1 H|-|7,95|-|7,95|30.000|
|2|336.990|6.218.793|8 H|-|3,19|-|3,19|10.000|
|2|336.990|6.218.793|1 H|-|6,61|-|6,61|30.000|
|3|337.023|6.218.680|8 H|-|2,32|-|2,32|10.000|
|3|337.023|6.218.680|1 H|-|4,82|-|4,82|30.000|
|4|337.194|6.218.998|8 H|-|2,62|-|2,62|10.000|
|4|337.194|6.218.998|1 H|-|5,94|-|5,94|30.000|

Fuente: Elaboración propia, 2025.

Página **81** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Tabla 34. Concentraciones totales de SO** **2**

|Receptores|Coordenadas UTM<br>(m)|Col3|Métrica|Condición<br>o línea de<br>base<br>(μg/m3)|Aporte<br>proyecto<br>(μg/m3)|Aporte<br>otros<br>proyectos<br>con RCA<br>(μg/m3)|Concentración<br>final (μg/m3)|Norma|
|---|---|---|---|---|---|---|---|---|
|**Receptores**|**Este**|**Norte**|**Norte**|**A **|**B **|**C **|**A + B +C**|**A + B +C**|
|1|337.026|6.218.934|Anual|-|2,23E-3|-|2,23E-3|60|
|1|337.026|6.218.934|24 H|-|9,40E-3|-|9,40E-3|150|
|1|337.026|6.218.934|1 H|-|2,93E-2|-|2,93E-2|350|
|2|336.990|6.218.793|Anual|-|1,63E-3|-|1,63E-3|60|
|2|336.990|6.218.793|24 H|-|6,96E-3|-|6,96E-3|150|
|2|336.990|6.218.793|1 H|-|2,43E-2|-|2,43E-2|350|
|3|337.023|6.218.680|Anual|-|5,38E-4|-|5,38E-4|60|
|3|337.023|6.218.680|24 H|-|4,76E-3|-|4,76E-3|150|
|3|337.023|6.218.680|1 H|-|1,65E-2|-|1,65E-2|350|
|4|337.194|6.218.998|Anual|-|1,29E-3|-|1,29E-3|60|
|4|337.194|6.218.998|24 H|-|4,81E-3|-|4,81E-3|150|
|4|337.194|6.218.998|1 H|-|1,95E-2|-|1,95E-2|350|

Fuente: Elaboración propia, 2025.

Página **82** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**7.6.** **Área de influencia**

El objetivo de determinar el Área de Influencia (AI) de Calidad del Aire es proporcionar la
información necesaria para descartar cualquier posible impacto en la población.

A continuación, se presenta la definición de Área de Influencia, cuyo criterio principal es
abarcar el área geográfica, donde se encuentran los receptores de interés, que podrían
verse potencialmente afectadas por las emisiones del Proyecto.

El área de influencia simulada para el Proyecto se evaluó utilizando la concentración
percentil 99 de NO X horario, obteniéndose como resultado que el área de influencia llega a
concentraciones de 1 μg/m [3], esto considera un área de aproximadamente 176 ha, la cual
considera todos los receptores de interés.

A continuación, en la siguiente Figura se presenta el área de influencia del Proyecto para la
componente aire (emisiones atmosféricas).

**Figura 84. Área de influencia del Proyecto, componente aire (emisiones atmosféricas)**

Fuente: Elaboración propia, 2025.

Página **83** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

# 8. Consideraciones

La base de datos meteorológica y geográfica utilizada para la modelación fue adquirida de
una empresa especializada en modelación para servicios de evaluación ambiental, dado que
el análisis de incertidumbre muestra que la base de datos utilizada cumple con todas las
condiciones establecidas por el Servicio de Evaluación Ambiental (SEA).

Cabe mencionar que, el Proyecto se ubica en la Región del Libertador General Bernardo
O’Higgins, la cual se encuentra declarada como saturada por MP 10, como concentración
anual y de 24 horas según D.S N°7/2009 y saturada por MP 2,5 como concentración anual y
de 24 horas según D.S. N°42/2017.

# 9. Conclusiones

El documento realizado proporcionó una evaluación de la concentración de emisiones
generadas durante el primer año de construcción del Proyecto “Proyecto Inmobiliario de
Integración Social y Territorial D.S. N° 19 Condominio Los Arrayanes II” (correspondiente
al año en que el Proyecto genera la mayor cantidad de emisiones, con el fin de evaluar un
escenario desfavorable). En este estudio, se modelaron las emisiones de MP 10 y MP 2,5, así
como los gases NO X, SO 2 y CO. El objetivo fue determinar las concentraciones de estos
contaminantes en la atmósfera, evaluar su contribución a la línea de base y prever posibles
efectos negativos en la salud de las personas.

Se utilizó una grilla de 50 km X 50 km, tanto para la modelación de emisiones como para el
modelo meteorológico WRF, con una resolución de 1 km.

En el Apéndice N°1 se presenta la planilla con el inventario de emisiones utilizado de INPUT

del modelo.

En el Apéndice N° 2 del informe se encuentra una descripción detallada del modelo
CALPUFF, incluyendo el archivo CALPUFF.INP, que es utilizado como archivo de control para
el escenario de modelado. Adicionalmente, se incorporan los archivos de modelación
utilizados para evaluar el efecto sinérgico de proyectos cercanos.

En el Apéndice N° 3 se incluye un archivo KMZ con el área de influencia del Proyecto, la
cual incluye todos los receptores evaluados, en el presente documento.

Se realizó un análisis de incertidumbre del modelo meteorológico, tanto cualitativo como
cuantitativo. En las variables consideradas, dirección del viento, velocidad del viento,
porcentaje de humedad, rosa de los vientos y temperatura se observaron comportamientos
similares que indican que los archivos WRF son representativos.

Para determinar la condición basal del área de emplazamiento del Proyecto se utilizó la
información proporcionada por la estación Rancagua II. Para el MP 10 se registró un

Página **84** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

cumplimiento del 98,33% de la norma anual y un 112,27% de la norma diaria. En el caso
del MP 2,5, se tiene un 127,9% de la norma anual y un 174% de la norma diaria. Es
fundamental destacar que las emisiones de la condición basal no están relacionadas con el
Proyecto, ya que corresponden exclusivamente a la línea base actual de la zona, influenciada
por fuentes de contaminación preexistentes.

Se realizó una modelación de material particulado (MP 10 y MP 2,5 ) y gases se combustión,
utilizando la situación más desfavorable, correspondiente al tercer año del Proyecto, donde
se consideró un total de 1,317 ton/año de MP 10, 0,316 ton/año de MP 2,5, 1,466 ton/año de
NO x, 0,004 ton/año de SO 2 y 1,700 ton/año de CO.

De acuerdo con los resultados obtenidos, se tienen las siguientes conclusiones por categoría
y contaminantes:

**Material particulado (MP** **10** **y MP** **2,5** **)**

- **MP** **10** **:** El mayor aporte promedio diario de MP 10 corresponde al **Receptor 4**, con una
concentración de **0,576 μg/m3** diario y el **Receptor 1** con **0,115 μg/m3** anual. Estos
valores representan solo el **0,44%** de la norma diaria (130 μg/m3) y el **0,2%** de la norma
anual (50 μg/m3). Esto significa que el aporte del proyecto está un **99,56%** por debajo del
límite diario y un **99,77%** por debajo del límite anual.

- **MP** **2,5** **:** El mayor aporte de MP 2,5 se registra en el **Receptor 1** con una concentración
de **0,304 μg/m3** diario y **0,080 μg/m3** anual. Estos valores equivalen al **0,61%** de la
norma diaria (50 μg/m3) y al **0,40%** de la norma anual (20 μg/m3), lo que indica que el
aporte del proyecto está un **99,39%** por debajo del límite diario y un **99,60%** por debajo
del límite anual.

**Gases de combustión (NO** **x** **, SO** **2** **y CO)**

- **NO** **x** **:** El **Receptor 1** recibe el mayor aporte de NO x, con una concentración de **20,79**
**μg/m3** horario, **6,65** **μg/m3** diario y **1,59 μg/m3** anual. Estos valores corresponden
al **10,40%** de la norma horaria (200 μg/m3), **6,65%** de la norma diaria (100 μg/m3) y
al **3,95%** de la norma anual (40 μg/m3), lo que significa que el aporte del proyecto está
un **89,6%** por debajo del límite horario, **93,35%** por debajo del límite diario y
un **96,05%** por debajo del límite anual.

- **CO:** En el caso del CO, el **Receptor 1** recibe un aporte de **7,95 μg/m3** horario y **3,80**
**μg/m3** cada 8 horas. Estos valores representan solo el **0,03%** de la norma horaria (30.000
μg/m3) y el **0,04%** de la norma cada 8 horas (10.000 μg/m3), lo que indica que el aporte
del proyecto está un **99,97%** y **99,96%** por debajo de los límites respectivos.

- **SO** **2** **:** Para el dióxido de azufre (SO 2 ), el mayor aporte lo recibe el **Receptor 1**, con una
concentración de **0,029 μg/m3** horario, equivalente al **0,01%** de la norma horaria (350
μg/m3), un aporte de **0,009 μg/m3** diario con un **0,01%** de la norma diaria (150 μg/m3)

Página **85** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

y **0,002 μg/m3** anual con un **0,004%** de la norma horaria (60 μg/m3). Esto significa que
el aporte del Proyecto está un **99,99%,** **99,99%** y **99,996%** por debajo de los límites
horario, diario y anual, respectivamente.

Es relevante mencionar que, la estación de calidad de aire utilizada para evaluar la condición
basal, corresponde a la estación Rancagua II y se encuentra a aproximadamente 3,03 km
del Proyecto, siendo la estación más cercana al Proyecto con datos válidos, la cual cumple
con el criterio mínimo de contar con un 75% de los datos, de acuerdo con el numeral 4.3.1
de la Guía para el uso de modelos de Calidad del Aire en el SEIA

Respecto a la evaluación del impacto de las emisiones atmosféricas del material particulado
respirable MP 10 y MP 2,5 en zonas saturadas, se tiene que el escenario más desfavorable
corresponde al tercer año del Proyecto. Además, se evalúan las emisiones resultantes de la
modelación, obteniendo que el receptor 1 posee los valores más altos para el MP 10 y el
MP 2,5 . No obstante, estos se encuentran muy por debajo de lo establecido en la Tabla 1 de
la Guía “Criterio de evaluación en el SEIA: Impacto de emisiones en zonas saturadas por
material particulado respirable MP 10 y material particulado respirable fino MP 2,5 ”.

**En base a lo anterior, se puede inferir que el Proyecto no genera una alteración**
**significativa y negativa en la calidad del aire en la condición basal.**

**En conclusión, es preciso indicar que de acuerdo con los resultados y posteriores**
**análisis no se detecta la presencia de riesgos para la salud de la población en**
**materia de calidad del aire asociado a actividades, obras y acciones del Proyecto,**
**incluso evaluando el escenario más desfavorable, por lo que dado lo acotado del**
**área de intervención y la temporalidad de las actividades del Proyecto se tiene**
**que están no superarán las normas primarias de calidad vigentes, estando en**
**conformidad con el Artículo 5° del D.S. N°40/2012.**

Página **86** de **89**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Informe elaborado por**

**Joshua Tobar Gutiérrez**

**Ingeniero Civil Ambiental**

**Asesoría y Consultoría - FCM Consultores**

**-**
**[administración@fcm](mailto:administración@fcm-consultores.cl)** **consultores.cl**

**-**
**www.fcm** **[consultores.cl](http://www.fcm-consultores.cl/)**

**+569 97419212**

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Página **87** de **89**

Modelación atmosférica
“Parque Las Alamedas I,II y III”

**Asesoría y Consultoría - FCM Consultores**

[administracion@fcm-consultores.cl](mailto:administracion@fcm-consultores.cl) [francisco.caro@fcm-consultores.cl](mailto:francisco.caro@fcm-consultores.cl)

www.fcm-consultores.cl

+569 9741 9212

Página **88** de **89**

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
| Límite anual | 40 |
| Límite diario | 100 |
| Límite horario | 200 |
| Normativa | D.S. N° 40/2024 del MMA |

**Tabla 4.: Límites anual y diario de CO****

| Nivel | CO (mg/m3N) |
| --- | --- |
| Límite horario | 30 |
| Límite 8 horas | 10 |
| Normativa | D.S. N° 115/2002 del MINSEGPRES |

**Tabla 5.: Receptores discretos modelación atmosférica****

| Receptores | Localización en coordenadas<br>UTM (WGS 84, Huso 19) | Col3 | Altitud (m.s.n.m.) | Breve descripción |
| --- | --- | --- | --- | --- |
| **Receptores** | **Este** | **Norte** | **Norte** | **Norte** |
| R1 | 337.026 | 6.218.934 | 480,11 | Galpón Material ligero<br>de un piso |
| R2 | 336.990 | 6.218.793 | 481,56 | Edificio Material solido<br>de 8 pisos |
| R3 | 337.023 | 6.218.680 | 483,24 | Edificio Material solido<br>de 8 pisos |
| R4 | 337.194 | 6.218.998 | 480,62 | Jardín<br>infantil<br>de<br>material solido de un<br>piso |

**Tabla 6.: Altura y distancia de receptores discretos en el área del Proyecto****

| Receptores | Descripción | Altura de<br>receptor<br>(m) | Distancia<br>Proyecto<br>(m) | Coordenadas UTM<br>Huso 19S | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Receptores** | **Descripción** | **Altura de**<br>**receptor**<br>**(m)** | **Distancia**<br>**Proyecto**<br>**(m)** | **Este** | **Norte** |
| R1 | Galpón Material ligero de un piso | 1,5 | 19 | 337.026 | 6.218.934 |
| R2 | Edificio Material solido de 8 pisos | 1,5 - 19 | 5 | 336.990 | 6.218.793 |
| R3 | Edificio Material solido de 8 pisos | 1,5 - 19 | 22 | 337.023 | 6.218.680 |
| R4 | Jardín infantil de material solido de un<br>piso | 1,5 | 117 | 337.194 | 6.218.998 |

**Tabla 8.: Fuentes de emisión del Proyecto****

| Cod.<br>de la<br>fuente | Fuente | Descripción | Longitud<br>(km) | Superficie<br>(m2) | Altura<br>m.s.n.m | Altura<br>de<br>emisión | Sigma<br>inicial | Mese<br>que<br>emite | Periodo<br>de<br>emisión |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCR_1 | AREA-<br>POLYGONAL | Movimientos<br>de tierra | - | 42.339 | 481,17 | 0 | 0 | 12<br>meses | Lunes a<br>viernes<br>de 08:00<br>- 18:00 |

**Tabla 9.: Tasas de emisión (ton/año) de cada fuente generadora de emisiones****

| Código de<br>fuente | Tasa de emisión (ton/año) | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Código de**<br>**fuente** | **MP10** | **MP2,5** | **NOX ** | **SO2 ** | **CO** |
| SCR_1 | 6,25E-2 | 5,45E-2 | 1,16 | 1,60E-3 | 4,05E-1 |
| SCR_2 | 3,66E-1 | 3,67E-2 | 2,50E-2 | 2,00E-6 | 6,00E-4 |
| SCR_3 | 7,38E-2 | 2,66E-2 | 1,10E-1 | 1,00E-4 | 4,57E-2 |
| SCR_5 | 8,14E-1 | 1,98E-1 | 1,40E- | 1,03E-3 | 1,25 |
| SCR_6 | 4,34E-4 | 4,34E-4 | 5,31E-2 | 1,15E-3 | 1,40E-3 |
| **Total** | **1,32** | **0,32** | **1,35** | **3,88E-3** | **1,70** |

**Tabla 10.: INPUT Software CALPUFF****

| Código de<br>fuente | INPUT software* | Col3 | Col4 | Col5 | Col6 | Unidad |
| --- | --- | --- | --- | --- | --- | --- |
| **Código de**<br>**fuente** | **MP10** | **MP2,5** | **NOX ** | **SO2 ** | **CO** | **CO** |
| SCR_1 | 4,67E-08 | 4,07E-08 | 8,68E-07 | 1,20E-09 | 3,03E-07 | g/m2·s |
| SCR_2 | 1,60E-06 | 1,61E-07 | 1,09E-08 | 8,76E-12 | 2,63E-09 | g/m·s |
| SCR_3 | 1,75E-08 | 6,31E-09 | 2,60E-08 | 2,37E-11 | 1,08E-08 | g/m·s |
| SCR_5 | 5,53E-06 | 1,34E-06 | 9,51E-07 | 6,99E-09 | 8,46E-06 | g/m·s |
| SCR_6 | 1,38E-05 | 1,38E-05 | 1,68E-03 | 3,65E-05 | 4,44E-05 | g/s |

**Tabla 11.: Estación utilizada para la validación del modelo WRF****

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
| Rancagua II | Meteorológicos | 339.842 | 6.220.527 | Temperatura | Temperatura |

**Tabla 12.: Estadísticos de sesgo, error absoluto medio y error cuadrático medio****

| Estación | Variable<br>meteorológica | BIAS | MAE | RMSE | r |
| --- | --- | --- | --- | --- | --- |
| Rancagua I | Velocidad del viento<br>(m/s) | -0,56 | 0,58 | 0,79 | 0,90 |
| Rancagua I | Temperatura (°C) | -1,57 | -1,57 | 1,90 | 0,97 |
| Rancagua II | Velocidad del viento<br>(m/s) | -0,48 | 0,48 | 0,67 | 0,93 |

**Tabla 13.: Concentración Media Anual de MP** **10** **(ug/m** **[3]** **N)****

| Estación | Norma primaria de MP (D.S. N° 12/2021 del MMA)<br>10<br>- Media Anual | Col3 | Col4 | Trianual | Porcentaje de<br>la norma |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 50 (ug/m3N)** | **Valor Norma: 50 (ug/m3N)** | **Valor Norma: 50 (ug/m3N)** | **Valor Norma: 50 (ug/m3N)** | **Valor Norma: 50 (ug/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2022** | **2023** | **2024** | **2024** | **2024** |
| Rancagua II | 43,81 | 44,93 | 58,74 | 49,16 | 98,33% |

**Tabla 14.: Percentil 98 concentración 24 horas de MP** **10** **(ug/m** **[3]** **N)****

| Estación | Norma primaria de MP (D.S. N° 12/2021 del<br>10<br>MMA) - 24 H | Porcentaje de la norma |
| --- | --- | --- |
| **Estación** | **Valor norma: 130 (ug/m3N)** | **Valor norma: 130 (ug/m3N)** |
| **Estación** | **Año** | **Año** |
| **Estación** | **2024** | **2024** |
| Rancagua II | 145,96 | 112,27% |

**Tabla 15.: Concentración Media Anual de MP** **2,5** **(ug/m** **[3]** **N)****

| Estación | Norma primaria de MP (D.S. N° 12/2021 del<br>2,5<br>MMA) - Media Anual | Col3 | Col4 | Trianual | Porcentaje de<br>la norma |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 20 (ug/m3N)** | **Valor Norma: 20 (ug/m3N)** | **Valor Norma: 20 (ug/m3N)** | **Valor Norma: 20 (ug/m3N)** | **Valor Norma: 20 (ug/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2022** | **2023** | **2024** | **2024** | **2024** |
| Rancagua II | 29,63 | 22,96 | 24,14 | 25,58 | 127,90% |

**Tabla 16.: Percentil 98 concentración 24 horas de MP** **2,5** **(ug/m** **[3]** **N)****

| Estación | Norma primaria de MP (D.S. N° 12/2011 del<br>2,5<br>MMA) - 24 H | Porcentaje de la norma |
| --- | --- | --- |
| **Estación** | **Valor norma: 50 (ug/m3N)** | **Valor norma: 50 (ug/m3N)** |
| **Estación** | **Año** | **Año** |
| **Estación** | **2024** | **2024** |
| Rancagua II | 87 | 174% |

**Tabla 17.: Normas de calidad primaria****

| Normativa | Límite | Concentración |
| --- | --- | --- |
| D.S. N° 12/2022 del MMA Norma de calidad de aire para el<br>MP10 | 130 μg/m3 | Diaria |
| D.S. N° 12/2022 del MMA Norma de calidad de aire para el<br>MP10 | 50 μg/m3 | Anual |
| D.S. N° 12/2010 del MMA Norma de calidad de aire para el<br>MP2,5 | 50 μg/m3 | Diaria |
| D.S. N° 12/2010 del MMA Norma de calidad de aire para el<br>MP2,5 | 20 μg/m3 | Anual |
| D.S. N° 104/2018 del MMA Norma Primaria de Calidad del<br>aire para el SO2 | 60 μg/m3 | Anual |
| D.S. N° 104/2018 del MMA Norma Primaria de Calidad del<br>aire para el SO2 | 150 μg/m3 | Diaria |
| D.S. N° 104/2018 del MMA Norma Primaria de Calidad del<br>aire para el SO2 | 350 μg/m3 | Horaria |
| D.S. N° 40/2024 del MMA Norma Primaria de calidad del aire<br>para NO2 | 40 μg/m3 | Anual |
| D.S. N° 40/2024 del MMA Norma Primaria de calidad del aire<br>para NO2 | 100 μg/m3 | Diaria |
| D.S. N° 40/2024 del MMA Norma Primaria de calidad del aire<br>para NO2 | 200 μg/m3 | 1 hora |
| D.S. N° 115/2002 del MINSEGPRES Norma Primaria de<br>calidad del aire para CO | 10 mg/m3 | 8 horas |
| D.S. N° 115/2002 del MINSEGPRES Norma Primaria de<br>calidad del aire para CO | 30 mg/m3 | 1 hora |

**Tabla 18.: Aportes del Proyecto - concentraciones máximas registradas de MP** **10****

| Receptor | Normativa | Col3 | Aporte del Proyecto (μg/m3) | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **24 horas** | **Anual** | **24 horas** | **% Norma** | **Anual** | **% Norma** |
| 1 | 130 | 50 | 4,991E-1 | 0,38% | 1,149E-1 | 0,23% |
| 2 | 130 | 50 | 4,981E-1 | 0,38% | 9,315E-2 | 0,19% |
| 3 | 130 | 50 | 4,554E-1 | 0,35% | 5,098E-2 | 0,10% |
| 4 | 130 | 50 | 5,758E-1 | 0,44% | 1,052E-1 | 0,21% |

**Tabla 19.: Aportes del Proyecto - concentraciones máximas registradas de MP** **2,5****

| Receptor | Normativa | Col3 | Aporte del Proyecto (μg/m3) | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **24 horas** | **Anual** | **24 horas** | **% Norma** | **Anual** | **% Norma** |
| 1 | 50 | 20 | 3,039E-1 | 0,61% | 8,023E-2 | 0,40% |
| 2 | 50 | 20 | 2,532E-1 | 0,51% | 6,012E-2 | 0,30% |
| 3 | 50 | 20 | 1,940E-1 | 0,39% | 2,439E-2 | 0,12% |
| 4 | 50 | 20 | 2,308E-1 | 0,46% | 5,461E-2 | 0,27% |

**Tabla 20.: Aportes del Proyecto - concentraciones máximas registradas de NO** **X****

| Receptor | Normativa | Col3 | Col4 | Aporte del Proyecto (μg/m3) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **1H** | **24H** | **Anual** | **1H** | **% **<br>**Norma** | **24H** | **% **<br>**Norma** | **Anual** | **% **<br>**Norma** |
| 1 | 200 | 100 | 40 | 20,79 | 10,40% | 6,647 | 6,65% | 1,581 | 3,95% |
| 2 | 200 | 100 | 40 | 16,91 | 8,46% | 4,868 | 4,87% | 1,134 | 2,84% |
| 3 | 200 | 100 | 40 | 11,33 | 5,67% | 3,132 | 3,13% | 3,614E-1 | 0,90% |
| 4 | 200 | 100 | 40 | 13,11 | 6,56% | 3,478 | 3,48% | 8,936E-1 | 2,23% |

**Tabla 21.: Aportes del Proyecto - concentraciones máximas registradas de CO****

| Receptor | Normativa | Col3 | Aporte del Proyecto (μg/m3) | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **1 hora** | **8 horas** | **1 hora** | **% Norma** | **8 horas** | **% Norma** |
| 1 | 30.000 | 10.000 | 7,952 | 0,03% | 3,80 | 0,04% |
| 2 | 30.000 | 10.000 | 6,609 | 0,02% | 3,19 | 0,03% |
| 3 | 30.000 | 10.000 | 4,823 | 0,02% | 2,32 | 0,02% |
| 4 | 30.000 | 10.000 | 5,936 | 0,02% | 2,62 | 0,03% |

**Tabla 22.: Aportes del Proyecto - concentraciones máximas registradas de SO** **2****

| Receptor | Normativa | Col3 | Col4 | Aporte del Proyecto (μg/m3) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Horario** | **Diario** | **Anual** | **Horario** | **% Norma** | **Diario** | **% Norma** | **Anual** | **% Norma** |
| 1 | 350 | 150 | 60 | 2,929E-2 | 0,01% | 9,400E-3 | 0,01% | 2,226E-3 | 0,004% |
| 2 | 350 | 150 | 60 | 2,427E-2 | 0,01% | 6,964E-3 | 0,005% | 1,626E-3 | 0,003% |
| 3 | 350 | 150 | 60 | 1,653E-2 | 0,005% | 4,757E-3 | 0,003% | 5,377E-4 | 0,001% |
| 4 | 350 | 150 | 60 | 1,953E-2 | 0,01% | 4,807E-3 | 0,003% | 1,293E-3 | 0,002% |

**Tabla 23.: Resumen de emisiones total por cada año para el MP** **10****

| Fase | Col2 | MP (ton/año)<br>10 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Año 1** | **Año 2** | **Año 3** | **Año 4** | **Año 6** | **Año “n” *** |
| Construcción | 1,011 | 0,423 | 0,502 | - | - | - |
| Operación | - | 0,135 | 0,815 | 1,231 | 1,231 | 1,231 |
| **Total** | **1,011** | **0,558** | **1,317** | **1,231** | **1,231** | **1,231** |
| *El Proyecto no contempla fase de cierre. | *El Proyecto no contempla fase de cierre. | *El Proyecto no contempla fase de cierre. | *El Proyecto no contempla fase de cierre. | *El Proyecto no contempla fase de cierre. | *El Proyecto no contempla fase de cierre. | *El Proyecto no contempla fase de cierre. |

**Tabla 24.: Resumen de emisiones total por cada año para el MP** **2,5****

| Fase | Col2 | MP (ton/año)<br>2,5 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Año 1** | **Año 2** | **Año 3** | **Año 4** | **Año 6** | **Año “n” *** |
| Construcción | 0,251 | 0,094 | 0,118 | - | - | - |
| Operación | - | 0,033 | 0,198 | 0,299 | 0,299 | 0,299 |
| **Total** | **0,251** | **0,127** | **0,316** | **0,299** | **0,299** | **0,299** |
|  | *El Proyecto no contempla fase de cierre. | *El Proyecto no contempla fase de cierre. | *El Proyecto no contempla fase de cierre. | *El Proyecto no contempla fase de cierre. | *El Proyecto no contempla fase de cierre. | *El Proyecto no contempla fase de cierre. |

**Tabla 25.: Comparación de los resultados de la modelación en receptores humanos y****

| Receptores | MP (ug/m3)<br>10 | Col3 | MP (ug/m3)<br>2,5 | Col5 |
| --- | --- | --- | --- | --- |
| **Receptores** | **24 H P98** | **Anual** | **24 H P98** | **Anual** |
| 1 | 4,991E-1 | 1,149E-1 | 3,039E-1 | 8,023E-2 |
| 2 | 4,981E-1 | 9,315E-2 | 2,532E-1 | 6,012E-2 |
| 3 | 4,554E-1 | 5,098E-2 | 1,940E-1 | 2,439E-2 |
| 4 | 5,758E-1 | 1,052E-1 | 2,308E-1 | 5,461E-2 |
| **Valor significancia Tabla 1** | **5,00** | **1,00** | **1,71** | **0,33** |

**Tabla 26.: Proyectos Aprobados o en Calificación Ambiental en las cercanías al Proyecto****

| ID | Nombre | Titular | Fecha<br>Ingreso al<br>Sistema | Estado | Distancia al<br>Proyecto |
| --- | --- | --- | --- | --- | --- |
| 1 | Parrones de Baquedano | Inmobiliaria San<br>Ramón I SPA | 07/10/2021 | Aprobado | 0,94 km |

**Tabla 27.: Evaluación de solapamiento fase de construcción****

| Proyecto | Fecha de<br>inicio | Fecha de término | ¿Existe<br>solapamiento? |
| --- | --- | --- | --- |
| Parrones de Baquedano | Primer<br>semestre 2022 | Segundo semestre<br>2024 | No |

**Tabla 28.: Tasas de emisión a considerar para la evaluación del efecto sinérgico****

| Proyecto | Tasa de emisión (ton/año) | Col3 | Fuente |
| --- | --- | --- | --- |
| **Proyecto** | **MP10** | **MP2,5** | **MP2,5** |
| Parrones de Baquedano | 0,4826 | 0,1173 | Anexo 3 ADENDA<br>Complementaria |

**Tabla 29.: Resultados aporte proyectos cercanos en receptores****

| Receptor | Métrica | Aporte proyecto cercanos (μg/m3) | Col4 | D.S. N°<br>12/2022 del<br>MMA | D.S. N°<br>12/2011 del<br>MMA |
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

**Tabla 30.: Concentraciones totales de MP** **10****

| Receptores | Coordenadas UTM<br>(m) | Col3 | Métrica | Condición<br>o línea de<br>base<br>(μg/m3) | Aporte<br>proyecto<br>(μg/m3) | Aporte<br>otros<br>proyectos<br>con RCA<br>(μg/m3) | Concentración<br>final (μg/m3) | Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **Este** | **Norte** | **Norte** | **A ** | **B ** | **C ** | **A + B +C** | **A + B +C** |
| 1 | 337.026 | 6.218.934 | Anual | 49,16 | 1,15E-1 | 7,26E-02 | 49,348 | 50 |
| 1 | 337.026 | 6.218.934 | 24 H | 145,96 | 4,99E-1 | 2,92E-01 | 146,751 | 130 |
| 2 | 336.990 | 6.218.793 | Anual | 49,16 | 9,32E-2 | 1,18E-01 | 49,371 | 50 |
| 2 | 336.990 | 6.218.793 | 24 H | 145,96 | 4,98E-1 | 5,04E-01 | 146,962 | 130 |
| 3 | 337.023 | 6.218.680 | Anual | 49,16 | 5,10E-2 | 1,33E-01 | 49,344 | 50 |
| 3 | 337.023 | 6.218.680 | 24 H | 145,96 | 4,55E-1 | 6,28E-01 | 147,043 | 130 |
| 4 | 337.194 | 6.218.998 | Anual | 49,16 | 1,05E-1 | 4,80E-02 | 49,313 | 50 |
| 4 | 337.194 | 6.218.998 | 24 H | 145,96 | 5,76E-1 | 2,16E-01 | 146,752 | 130 |

**Tabla 31.: Concentraciones totales de MP** **2,5****

| Receptores | Coordenadas UTM<br>(m) | Col3 | Métrica | Condición<br>o línea de<br>base<br>(μg/m3) | Aporte<br>proyecto<br>(μg/m3) | Aporte<br>otros<br>proyectos<br>con RCA<br>(μg/m3) | Concentración<br>final (μg/m3) | Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **Este** | **Norte** | **Norte** | **A ** | **B ** | **C ** | **A + B +C** | **A + B +C** |
| 1 | 337.026 | 6.218.934 | Anual | 25,58 | 8,02E-2 | 1,77E-02 | 25,678 | 20 |
| 1 | 337.026 | 6.218.934 | 24 H | 87 | 3,04E-1 | 7,09E-02 | 87,375 | 50 |
| 2 | 336.990 | 6.218.793 | Anual | 25,58 | 6,01E-2 | 2,86E-02 | 25,669 | 20 |
| 2 | 336.990 | 6.218.793 | 24 H | 87 | 2,53E-1 | 1,23E-01 | 87,376 | 50 |
| 3 | 337.023 | 6.218.680 | Anual | 25,58 | 2,44E-2 | 3,24E-02 | 25,637 | 20 |
| 3 | 337.023 | 6.218.680 | 24 H | 87 | 1,94E-1 | 1,53E-01 | 87,347 | 50 |
| 4 | 337.194 | 6.218.998 | Anual | 25,58 | 5,46E-2 | 1,17E-02 | 25,646 | 20 |

**Tabla 32.: Concentraciones totales de NO** **x****

| Receptores | Coordenadas UTM<br>(m) | Col3 | Métrica | Condición<br>o línea de<br>base<br>(μg/m3) | Aporte<br>proyecto<br>(μg/m3) | Aporte<br>otros<br>proyectos<br>con RCA<br>(μg/m3) | Concentración<br>final (μg/m3) | Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **Este** | **Norte** | **Norte** | **A ** | **B ** | **C ** | **A + B +C** | **A + B +C** |
| 1 | 337.026 | 6.218.934 | Anual | - | 1,58 | - | 1,58 | 40 |
| 1 | 337.026 | 6.218.934 | 24H |  | 6,65 |  | 6,65 | 100 |
| 1 | 337.026 | 6.218.934 | 1H | - | 20,79 | - | 20,79 | 200 |
| 2 | 336.990 | 6.218.793 | Anual | - | 1,13 | - | 1,13 | 40 |
| 2 | 336.990 | 6.218.793 | 24H |  | 4,87 |  | 4,87 | 100 |
| 2 | 336.990 | 6.218.793 | 1H | - | 16,91 | - | 16,91 | 200 |
| 3 | 337.023 | 6.218.680 | Anual | - | 3,61E-1 | - | 3,61E-1 | 40 |
| 3 | 337.023 | 6.218.680 | 24H |  | 3,13 |  | 3,13 | 100 |
| 3 | 337.023 | 6.218.680 | 1H | - | 11,33 | - | 11,33 | 200 |
| 4 | 337.194 | 6.218.998 | Anual | - | 8,94E-1 | - | 8,94E-1 | 40 |
| 4 | 337.194 | 6.218.998 | 24H |  | 3,48 |  | 3,48 | 100 |
| 4 | 337.194 | 6.218.998 | 1H | - | 13,11 | - | 13,11 | 200 |

**Tabla 33.: Concentraciones totales de CO****

| Receptores | Coordenadas UTM<br>(m) | Col3 | Métrica | Condición<br>o línea de<br>base<br>(μg/m3) | Aporte<br>proyecto<br>(μg/m3) | Aporte<br>otros<br>proyectos<br>con RCA<br>(μg/m3) | Concentración<br>final (μg/m3) | Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **Este** | **Norte** | **Norte** | **A ** | **B ** | **C ** | **A + B +C** | **A + B +C** |
| 1 | 337.026 | 6.218.934 | 8 H | - | 3,80 | - | 3,80 | 10.000 |
| 1 | 337.026 | 6.218.934 | 1 H | - | 7,95 | - | 7,95 | 30.000 |
| 2 | 336.990 | 6.218.793 | 8 H | - | 3,19 | - | 3,19 | 10.000 |
| 2 | 336.990 | 6.218.793 | 1 H | - | 6,61 | - | 6,61 | 30.000 |
| 3 | 337.023 | 6.218.680 | 8 H | - | 2,32 | - | 2,32 | 10.000 |
| 3 | 337.023 | 6.218.680 | 1 H | - | 4,82 | - | 4,82 | 30.000 |
| 4 | 337.194 | 6.218.998 | 8 H | - | 2,62 | - | 2,62 | 10.000 |
| 4 | 337.194 | 6.218.998 | 1 H | - | 5,94 | - | 5,94 | 30.000 |

**Tabla 34.: Concentraciones totales de SO** **2****

| Receptores | Coordenadas UTM<br>(m) | Col3 | Métrica | Condición<br>o línea de<br>base<br>(μg/m3) | Aporte<br>proyecto<br>(μg/m3) | Aporte<br>otros<br>proyectos<br>con RCA<br>(μg/m3) | Concentración<br>final (μg/m3) | Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **Este** | **Norte** | **Norte** | **A ** | **B ** | **C ** | **A + B +C** | **A + B +C** |
| 1 | 337.026 | 6.218.934 | Anual | - | 2,23E-3 | - | 2,23E-3 | 60 |
| 1 | 337.026 | 6.218.934 | 24 H | - | 9,40E-3 | - | 9,40E-3 | 150 |
| 1 | 337.026 | 6.218.934 | 1 H | - | 2,93E-2 | - | 2,93E-2 | 350 |
| 2 | 336.990 | 6.218.793 | Anual | - | 1,63E-3 | - | 1,63E-3 | 60 |
| 2 | 336.990 | 6.218.793 | 24 H | - | 6,96E-3 | - | 6,96E-3 | 150 |
| 2 | 336.990 | 6.218.793 | 1 H | - | 2,43E-2 | - | 2,43E-2 | 350 |
| 3 | 337.023 | 6.218.680 | Anual | - | 5,38E-4 | - | 5,38E-4 | 60 |
| 3 | 337.023 | 6.218.680 | 24 H | - | 4,76E-3 | - | 4,76E-3 | 150 |
| 3 | 337.023 | 6.218.680 | 1 H | - | 1,65E-2 | - | 1,65E-2 | 350 |
| 4 | 337.194 | 6.218.998 | Anual | - | 1,29E-3 | - | 1,29E-3 | 60 |
| 4 | 337.194 | 6.218.998 | 24 H | - | 4,81E-3 | - | 4,81E-3 | 150 |
| 4 | 337.194 | 6.218.998 | 1 H | - | 1,95E-2 | - | 1,95E-2 | 350 |
