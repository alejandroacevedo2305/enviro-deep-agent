---
title: Titulo 1
author: asoto
date: D:20190705103512-04'00'
language: es
type: report
pages: 161
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - I NTRODUCCIÓN
  - 1 A JUSTE M ETODOLÓGICO (T AREA 1)
  - 2 R EVISIÓN B IBLIOGRÁFICA (T AREA 2)
  - 3 A NÁLISIS DE I NFORMACIÓN D ISPONIBLE (T AREA 3)
  - 4 D EFINICIÓN DEL Á REA DE E STUDIO (T AREA 4)
  - 5 Z ONIFICACIÓN (T AREA 5)
  - 6 D EFINICIÓN DE LOS P ERIODOS DE M ODELACIÓN (T AREA 6)
  - 7 D EFINICIÓN DE LAS C ATEGORÍAS DE U SUARIO (T AREA 7)
  - 8 D EFINICIÓN DE P ROPÓSITOS DE V IAJE (T AREA 8)
  - 9 D EFINICIÓN DE M ODOS DE T RANSPORTE (T AREA 9)
  ... y 11 secciones más
-->

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**ÍNDICE**

1

Pág.

**INTRODUCCIÓN .................................................................................................................... 12**

**1** **AJUSTE METODOLÓGICO (TAREA 1) ............................................................................. 14**

**2** **REVISIÓN BIBLIOGRÁFICA (TAREA 2) ........................................................................... 15**

2.1 N UEVAS F UNCIONALIDADES EN ESTRAUS ................................................................................................... 18

2.2 M ODELO DE E LECCIÓN H ORARIA .................................................................................................................. 19

2.3 P ERIODO P UNTA T ARDE ................................................................................................................................. 21

**3** **ANÁLISIS DE INFORMACIÓN DISPONIBLE (TAREA 3) ................................................... 24**

3.1 E NCUESTA O RIGEN D ESTINO 2012 ............................................................................................................. 24

3.2 M EDICIONES DE AFOROS DE TRÁFICO Y PERFILES DE CARGA EN SERVICIOS TRONCALES EN EL GRAN

S ANTIAGO .................................................................................................................................................... 25

**4** **DEFINICIÓN DEL ÁREA DE ESTUDIO (TAREA 4) .............................................................. 26**

**5** **ZONIFICACIÓN (TAREA 5) ............................................................................................ 29**

**6** **DEFINICIÓN DE LOS PERIODOS DE MODELACIÓN (TAREA 6) ........................................ 31**

**7** **DEFINICIÓN DE LAS CATEGORÍAS DE USUARIO (TAREA 7) ............................................ 34**

**8** **DEFINICIÓN DE PROPÓSITOS DE VIAJE (TAREA 8) ........................................................ 37**

**9** **DEFINICIÓN DE MODOS DE TRANSPORTE (TAREA 9) .................................................... 39**

**10** **CALIBRACIÓN DE LOS MODELOS DE ASIGNACIÓN (TAREA 10) .................................... 42**

10.1 C ONSTRUCCIÓN DE R EDES DE T RANSPORTE (S UB T AREA 10-1) ..................................................................... 42

10.1.1 Red Vial Estratégica EOD 2012 .................................................................................................. 45

10.1.2 Corredores de Buses, Vías Exclusivas, Pistas Solo Bus y Vías Reversibles ............................... 46

10.1.3 Atributos de la Red Vial ................................................................................................................. 50

10.1.4 Red de Buses Transantiago ........................................................................................................... 51

10.1.5 Red de Metro ................................................................................................................................. 54

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

2

10.1.6 Red de Taxicolectivo ...................................................................................................................... 55

10.2 C ALIBRACIÓN Y V ALIDACIÓN DE R EDES (S UB T AREAS 10-2 Y 10-3) .............................................................. 56

10.2.1 Construcción de matrices observadas ......................................................................................... 56

10.2.2 Matrices de viajes externos ........................................................................................................... 58

10.2.3 Matrices de viajes fijos .................................................................................................................. 58

10.2.4 Calibración de la Red de Transporte Privado ............................................................................. 59

10.2.5 Calibración de Redes de Transporte Público .............................................................................. 61

10.2.6 Definición de relación velocidad transporte privado / velocidad transporte público ............ 63

10.2.7 Tratamiento del transporte de carga ............................................................................................ 65

**11** **ANÁLISIS DE LOS MODELOS DE DEMANDA DE ESTRAUS (TAREA 11) ............................ 67**

11.1 G ENERACIÓN DE V IAJES ................................................................................................................................ 67

11.2 M ODELOS DE D EMANDA (D ISTRIBUCIÓN, P ARTICIÓN M ODAL Y E LECCIÓN H ORARIA ) .................................. 67

**12** **CALIBRACIÓN DE MODELOS DE GENERACIÓN Y ATRACCIÓN (TAREA 12) ..................... 70**

12.1 M ODELOS DE GENERACIÓN DE VIAJES DE IDA BASADOS EN HOGAR ( GENERACIÓN BHI ) ................................ 71

12.1.1 Punta Mañana ................................................................................................................................ 71

12.1.2 Fuera de Punta ............................................................................................................................... 72

12.1.3 Punta Tarde ..................................................................................................................................... 74

12.2 M ODELOS DE GENERACIÓN DE VIAJES BASADOS EN HOGAR RETORNO Y NO BASADO EN EL HOGAR

( GENERACIÓN BHR + NBH ) ............................................................................................................................ 75

12.2.1 Punta Mañana ................................................................................................................................ 75

12.2.2 Fuera de Punta ............................................................................................................................... 76

12.2.3 Punta Tarde ..................................................................................................................................... 77

12.3 M ODELOS DE ATRACCIÓN DE VIAJES BASADOS EN EL HOGAR RETORNO ( ATRACCIÓN BHR ) ............................ 78

12.3.1 Punta Mañana ................................................................................................................................ 78

12.3.2 Fuera de Punta ............................................................................................................................... 79

12.3.3 Punta Tarde ..................................................................................................................................... 81

12.4 M ODELOS DE ATRACCIÓN DE VIAJES BASADOS EN EL HOGAR DE IDA Y NO BASADOS EN EL HOGAR

( ATRACCIÓN BHI + NBH ) ............................................................................................................................... 82

12.4.1 Punta Mañana ................................................................................................................................ 82

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

3

12.4.2 Fuera de Punta ............................................................................................................................... 83

12.4.3 Punta Tarde ..................................................................................................................................... 84

12.5 C ONSIDERACIONES AL MOMENTO DE PREDECIR ............................................................................................ 84

**13** **CALIBRACIÓN DE MODELOS DE PARTICIÓN MODAL (TAREA 13) .................................. 87**

13.1 E STIMACIÓN DE MODELOS MNL................................................................................................................... 87

13.2 E STIMACIÓN DE MODELOS NL O HL ............................................................................................................. 90

13.3 M ODELOS DE P ARTICIÓN M ODAL ................................................................................................................. 91

13.3.1 Punta Mañana (NO implementado en ESTRAUS) ..................................................................... 91

13.3.2 Fuera de Punta ............................................................................................................................... 95

13.3.3 Punta Tarde ..................................................................................................................................... 98

**14** **CALIBRACIÓN DE MODELOS DE DISTRIBUCIÓN (TAREA 14) ........................................ 102**

14.1 E NFOQUE M ETODOLÓGICO ...................................................................................................................... 102

14.2 M ODELOS DE D ISTRIBUCIÓN ...................................................................................................................... 103

**15** **VALIDACIÓN DE LOS MODELOS DE DEMANDA (TAREA 15) ........................................ 104**

15.1 V ALIDACIÓN DE LOS M ODELOS DE P ARTICIÓN M ODAL .............................................................................. 104

15.2 V ALIDACIÓN DE LOS M ODELOS DE P ARTICIÓN M ODAL CON E LECCIÓN H ORARIA ...................................... 104

15.3 V ALIDACIÓN DE LOS M ODELOS DE D ISTRIBUCIÓN ...................................................................................... 104

**16** **DEFINICIÓN MODELO DE ELECCIÓN HORARIA DE VIAJE (TAREA 16) ........................... 106**

16.1 E NFOQUE M ETODOLÓGICO ...................................................................................................................... 106

16.2 M ODELOS DE P ARTICIÓN M ODAL CON E LECCIÓN H ORARIA ...................................................................... 106

16.2.1 Punta Mañana, propósito trabajo ............................................................................................. 107

16.2.2 Punta Mañana, propósito estudio 1 .......................................................................................... 108

16.2.3 Punta Mañana, propósito estudio 2 .......................................................................................... 110

16.2.4 Punta Mañana, propósito otros ................................................................................................. 111

**17** **VALIDACIÓN DEL MODELO COMPLETO (TAREA 17) .................................................... 114**

17.1 V ALIDACIÓN DEL M ODELO EN P UNTA M AÑANA ........................................................................................ 115

17.1.1 Partición Modal ........................................................................................................................... 115

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

4

17.1.2 Flujos en Metro ............................................................................................................................ 123

17.2 V ALIDACIÓN DEL M ODELO EN F UERA DE P UNTA ......................................................................................... 127

17.2.1 Partición Modal ........................................................................................................................... 127

17.2.2 Flujos en Metro ............................................................................................................................ 131

17.3 V ALIDACIÓN DEL M ODELO EN P UNTA T ARDE .............................................................................................. 136

17.3.1 Partición Modal ........................................................................................................................... 136

17.3.2 Flujos en Metro ............................................................................................................................ 140

**18** **ANÁLISIS DEL SISTEMA DE TRANSPORTE EN UN CORTE TEMPORAL FUTURO (TAREA**

**18) ............................................................................................................................. 146**

18.1 D EFINICIONES P REVIAS ............................................................................................................................... 146

18.2 C OMPARACIÓN R ESULTADOS 2012, 2020 Y 2025 ................................................................................. 147

18.2.1 Punta Mañana ............................................................................................................................. 147

18.2.2 Fuera de Punta ............................................................................................................................ 151

18.2.3 Punta Tarde .................................................................................................................................. 152

**19** **CÁLCULO DE FACTORES DE EXPANSIÓN (TAREA 19) ................................................... 155**

19.1 E NFOQUE M ETODOLÓGICO ...................................................................................................................... 155

19.2 F ACTORES DE E XPANSIÓN .......................................................................................................................... 156

**20** **CALIBRACIÓN SIMULTÁNEA DE LOS MODELOS DE DISTRIBUCIÓN DE VIAJES,**

**PARTICIÓN MODAL Y ELECCIÓN DE HORARIO (TAREA 20) ......................................... 160**

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**ÍNDICE DE ILUSTRACIONES**

5

Pág.

Ilustración 2-1 Viajes según Propósito ESTRAUS, PT 2006 .................................................................21

Ilustración 4-1 Área de Estudio ...............................................................................................................28

Ilustración 6-1 Representación Continua (todos los modos por hora media de viaje) ......................31

Ilustración 6-2 Distribución Esqumática de Viajes Interzonales (modos ESTRAUS-14) .....................33

Ilustración 7-1 Histograma de tenencia de vehículos motorizados por hogar ...................................34

Ilustración 7-2 Histograma de ingreso por hogar .................................................................................35

Ilustración 10-1 Catastro Vial EOD 2012 y Red ESTRAUS EOD 2012 ............................................46

Ilustración 10-2 Infraestructura dedicada al Transporte Público en Superficie ..................................47

Ilustración 10-3 Estaciones Intermodales y Terminales de Buses.........................................................48

Ilustración 10-4 Vías Reversibles que operan en Punta Mañana ........................................................49

Ilustración 10-5 Red Modelada de Bus Transantiago ..........................................................................52

Ilustración 10-6 Red Modelada de Bus Transantiago No Comercial, Punta Mañana .....................53

Ilustración 10-7 Red Modelada de Metro y Tren .................................................................................54

Ilustración 10-8 Red Modelada de Taxicolectivo .................................................................................55

Ilustración 10-9 Matriz EOD2012 Transporte Privado y Público, PM1 .............................................57

Ilustración 13-1 Estructura Jerárquica Base ...........................................................................................91

Ilustración 17-1 Perfil de Viajes L1 PM 2012, sentido Oriente-Poniente ......................................... 123

Ilustración 17-2 Perfil de Viajes L1 PM 2012, sentido Poniente-Oriente ......................................... 123

Ilustración 17-3 Perfil de Viajes L2 PM 2012, sentido Sur-Norte ..................................................... 124

Ilustración 17-4 Perfil de Viajes L2 PM 2012, sentido Norte-Sur ..................................................... 124

Ilustración 17-5 Perfil de Viajes L4 PM 2012, sentido Sur-Norte ..................................................... 125

Ilustración 17-6 Perfil de Viajes L4 PM 2012, sentido Norte-Sur ..................................................... 125

Ilustración 17-7 Perfil de Viajes L4A PM 2012, sentido Poniente-Oriente ...................................... 126

Ilustración 17-8 Perfil de Viajes L4A PM 2012, sentido Oriente-Poniente ...................................... 126

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

6

Ilustración 17-9 Perfil de Viajes L5 PM 2012, sentido Poniente-Oriente ......................................... 127

Ilustración 17-10 Perfil de Viajes L5 PM 2012, sentido Oriente-Poniente....................................... 127

Ilustración 17-11 Perfil de Viajes L1 FP 2012, sentido Oriente-Poniente ........................................ 132

Ilustración 17-12 Perfil de Viajes L1 FP 2012, sentido Poniente-Oriente ........................................ 132

Ilustración 17-13 Perfil de Viajes L2 FP 2012, sentido Sur-Norte .................................................... 133

Ilustración 17-14 Perfil de Viajes L2 FP 2012, sentido Norte-Sur .................................................... 133

Ilustración 17-15 Perfil de Viajes L4 FP 2012, sentido Sur-Norte .................................................... 134

Ilustración 17-16 Perfil de Viajes L4 FP 2012, sentido Norte-Sur .................................................... 134

Ilustración 17-17 Perfil de Viajes L4A FP 2012, sentido Poniente-Oriente ...................................... 135

Ilustración 17-18 Perfil de Viajes L4A FP 2012, sentido Oriente-Poniente ...................................... 135

Ilustración 17-19 Perfil de Viajes L5 FP 2012, sentido Poniente-Oriente ........................................ 136

Ilustración 17-20 Perfil de Viajes L5 FP 2012, sentido Oriente-Poniente ........................................ 136

Ilustración 17-21 Perfil de Viajes L1 PT 2012, sentido Oriente-Poniente ........................................ 141

Ilustración 17-22 Perfil de Viajes L1 PT 2012, sentido Poniente-Oriente ........................................ 141

Ilustración 17-23 Perfil de Viajes L2 PT 2012, sentido Sur-Norte .................................................... 142

Ilustración 17-24 Perfil de Viajes L2 PT 2012, sentido Norte-Sur .................................................... 142

Ilustración 17-25 Perfil de Viajes L4 PT 2012, sentido Sur-Norte .................................................... 143

Ilustración 17-26 Perfil de Viajes L4 PT 2012, sentido Norte-Sur .................................................... 143

Ilustración 17-27 Perfil de Viajes L4A PT 2012, sentido Poniente-Oriente ...................................... 144

Ilustración 17-28 Perfil de Viajes L4A PT 2012, sentido Oriente-Poniente ...................................... 144

Ilustración 17-29 Perfil de Viajes L5 PT 2012, sentido Poniente-Oriente ........................................ 145

Ilustración 17-30 Perfil de Viajes L5 PT 2012, sentido Oriente-Poniente ........................................ 145

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**ÍNDICE DE TABLAS**

7

Pág.

Tabla 2-1 Viajes según Propósito EOD-H, PT 2006 .............................................................................22

Tabla 4-1 Área de Estudio .......................................................................................................................26

Tabla 4-2 Zonas Externas ........................................................................................................................27

Tabla 7-1 Categorización de viajeros elegida .....................................................................................36

Tabla 9-1 Partición Modal - Base de Datos Definitiva ........................................................................41

Tabla 10-1 Descripción de Categorías ..................................................................................................50

Tabla 10-2 Capacidad por Pista según Categoría ...............................................................................50

Tabla 10-3 Categorías de Ingreso por Clase de Usuario ....................................................................58

Tabla 10-4 Parámetros BPR por Categoría de Arco Período Punta Mañana ....................................60

Tabla 10-5 Parámetros BPR por Categoría de Arco Periodo Fuera de Punta ...................................60

Tabla 10-6 Parámetros BPR por Categoría de Arco Periodo Punta Tarde .........................................60

Tabla 10-7 Ponderadores de Tiempo por Modo ..................................................................................61

Tabla 10-8 Valores Relación Fija Entre Tiempo de Viaje en Bus y en Auto .......................................64

Tabla 10-9 Parámetros φ y ε finales ......................................................................................................64

Tabla 10-10 Parámetros α y β calibrados ............................................................................................65

Tabla 12-1 Resumen de modelos de generación y atracción de viajes .............................................70

Tabla 12-2 Modelo de generación de viajes bhi PM, propósito trabajo...........................................71

Tabla 12-3 Modelo de generación de viajes bhi PM, propósito estudio 1 .......................................71

Tabla 12-4 Modelo de generación de viajes bhi PM, propósito estudio 2 .......................................72

Tabla 12-5 Modelo de generación de viajes bhi PM, propósito otros ..............................................72

Tabla 12-6 Modelo de generación de viajes bhi FP, propósito trabajo ............................................72

Tabla 12-7 Modelo de generación de viajes bhi FP, propósito estudio .............................................73

Tabla 12-8 Modelo de generación de viajes bhi FP, propósito compras ..........................................73

Tabla 12-9 Modelo de generación de viajes bhi FP, propósito otros ................................................73

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

8

Tabla 12-10 Modelo de generación de viajes bhi PT, propósito trabajo y estudio ..........................74

Tabla 12-11 Modelo de generación de viajes bhi PT, propósito compras ........................................74

Tabla 12-12 Modelo de generación de viajes bhi PT, propósito otros ..............................................74

Tabla 12-13 Modelo de generación de viajes bhr+nbh PM, propósito trabajo ...............................75

Tabla 12-14 Modelo de generación de viajes bhr+nbh PM, propósito estudio 1 ...........................75

Tabla 12-15 Modelo de generación de viajes bhr+nbh PM, propósito estudio 2 ...........................75

Tabla 12-16 Modelo de generación de viajes bhr+nbh PM, propósito otros ...................................75

Tabla 12-17 Modelo de generación de viajes bhr+nbh FP, propósito trabajo .................................76

Tabla 12-18 Modelo de generación de viajes bhr+nbh FP, propósito estudio .................................76

Tabla 12-19 Modelo de generación de viajes bhr+nbh FP, propósito compras ..............................76

Tabla 12-20 Modelo de generación de viajes bhr+nbh FP, propósito otros .....................................76

Tabla 12-21 Modelo de generación de viajes bhr+nbh PT, propósito trabajo y estudio ................77

Tabla 12-22 Modelo de generación de viajes bhr+nbh PT, propósito compras ..............................77

Tabla 12-23 Modelo de generación de viajes bhr+nbh PT, propósito otros .....................................77

Tabla 12-24 Modelo de atracción de viajes bhr PM, propósito trabajo ...........................................78

Tabla 12-25 Modelo de atracción de viajes bhr PM, propósito estudio 1 ........................................78

Tabla 12-26 Modelo de atracción de viajes bhr PM, propósito estudio 2 ........................................79

Tabla 12-27 Modelo de atracción de viajes bhr PM, propósito otros ...............................................79

Tabla 12-28 Modelo de atracción de viajes bhr FP, propósito trabajo .............................................79

Tabla 12-29 Modelo de atracción de viajes bhr FP, propósito estudio .............................................80

Tabla 12-30 Modelo de atracción de viajes bhr FP, propósito compras ...........................................80

Tabla 12-31 Modelo de atracción de viajes bhr FP, propósito otros .................................................80

Tabla 12-32 Modelo de atracción de viajes bhr PT, propósito trabajo y estudio .............................81

Tabla 12-33 Modelo de atracción de viajes bhr PT, propósito compras ...........................................81

Tabla 12-34 Modelo de atracción de viajes bhr PT, propósito otros .................................................81

Tabla 12-35 Modelo de atracción de viajes bhi+nbh PM, propósito trabajo ...................................82

Tabla 12-36 Modelo de atracción de viajes bhi+nbh PM, propósito estudio 1 ...............................82

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

9

Tabla 12-37 Modelo de atracción de viajes bhi+nbh PM, propósito estudio 2 ...............................82

Tabla 12-38 Modelo de atracción de viajes bhi+nbh PM, propósito otros .......................................82

Tabla 12-39 Modelo de atracción de viajes bhi+nbh FP, propósito trabajo ....................................83

Tabla 12-40 Modelo de atracción de viajes bhi+nbh FP, propósito estudio .....................................83

Tabla 12-41 Modelo de atracción de viajes bhi+nbh FP, propósito compras ..................................83

Tabla 12-42 Modelo de atracción de viajes bhi+nbh FP, propósito otros ........................................83

Tabla 12-43 Modelo de atracción de viajes bhi+nbh PT, propósito trabajo y estudio ....................84

Tabla 12-44 Modelo de atracción de viajes bhi+nbh PT, propósito compras ..................................84

Tabla 12-45 Modelo de atracción de viajes bhi+nbh PT, propósito otros ........................................84

Tabla 12-46 Factores de Ajuste para un solo Periodo Punta Mañana ..............................................86

Tabla 13-1 Funciones de Utilidad MNL Base .......................................................................................88

Tabla 13-2 Modelo de Partición Modal PM, propósito trabajo (MNL), NO implementado en
ESTRAUS ...................................................................................................................................................92

Tabla 13-3 Modelo de Partición Modal PM, propósito estudio 1 (MNL), NO implementado en
ESTRAUS ...................................................................................................................................................93

Tabla 13-4 Modelo de Partición Modal PM, propósito estudio 2 (MNL), NO implementado en
ESTRAUS ...................................................................................................................................................93

Tabla 13-5 Modelo de Partición Modal PM, propósito otros (MNL), NO implementado en ESTRAUS
...................................................................................................................................................................94

Tabla 13-6 Modelo de Partición Modal FP, propósito trabajo (MNL) ...............................................95

Tabla 13-7 Modelo de Partición Modal FP, propósito estudio (MNL) ...............................................95

Tabla 13-8 Modelo de Partición Modal FP, propósito vuelta a casa (MNL) ....................................96

Tabla 13-9 Modelo de Partición Modal FP, propósito compras (MNL) ............................................97

Tabla 13-10 Modelo de Partición Modal FP, propósito otros (NL) ....................................................97

Tabla 13-11 Modelo de Partición Modal PT, propósito trabajo y estudio (NL) ................................98

Tabla 13-12 Modelo de Partición Modal PT, propósito vuelta a casa (NL) ......................................99

Tabla 13-13 Modelo de Partición Modal PT, propósito compras (MNL) ....................................... 100

Tabla 13-14 Modelo de Partición Modal PT, propósito otros (NL) ................................................. 100

Tabla 14-1 Modelos de Distribución Implementados en ESTRAUS ................................................. 103

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

10

Tabla 16-1 Modelo de Partición Modal con Elección Horaria PM, propósito trabajo (NL) ........ 107

Tabla 16-2 Modelo de Partición Modal con Elección Horaria PM, propósito estudio 1 (NL) ..... 109

Tabla 16-3 Modelo de Partición Modal con Elección Horaria PM, propósito estudio 2 (NL) ..... 110

Tabla 16-4 Modelo de Partición Modal con Elección Horaria PM, propósito otros (NL) ............ 112

Tabla 17-1 Partición Modal Base de Datos PM Total ....................................................................... 117

Tabla 17-2 Partición Modal Base de Datos PM1 .............................................................................. 118

Tabla 17-3 Partición Modal Base de Datos PM2 .............................................................................. 119

Tabla 17-4 Partición Modal ESTRAUS PM Total ............................................................................... 120

Tabla 17-5 Partición Modal ESTRAUS PM1 ...................................................................................... 121

Tabla 17-6 Partición Modal ESTRAUS PM2 ...................................................................................... 122

Tabla 17-7 Partición Modal Base de Datos FP .................................................................................. 129

Tabla 17-8 Partición Modal ESTRAUS FP ........................................................................................... 130

Tabla 17-9 Partición Modal Base de Datos PT .................................................................................. 138

Tabla 17-10 Partición Modal ESTRAUS PT ........................................................................................ 139

Tabla 18-1 Cambios por Corte Temporal .......................................................................................... 146

Tabla 18-2 Progresión de la Partición Modal PM Total .................................................................... 147

Tabla 18-3 Progresión de la Partición Modal PM1 ........................................................................... 148

Tabla 18-4 Progresión de la Partición Modal PM2 ........................................................................... 149

Tabla 18-5 Progresión de las Velocidades (km/h) PM1 ................................................................... 150

Tabla 18-6 Progresión de las Velocidades (km/h) PM2 ................................................................... 150

Tabla 18-7 Progresión de la Partición Modal FP ............................................................................... 151

Tabla 18-8 Progresión de las Velocidades (km/h) FP ....................................................................... 152

Tabla 18-9 Progresión de la Partición Modal PT ............................................................................... 153

Tabla 18-10 Progresión de las Velocidades (km/h) PT..................................................................... 154

Tabla 19-1 Factores de Expansión Calculados para ESTRAUS, EOD 2012 ................................. 156

Tabla 19-2 Factores de Expansión modelando solo PM1, EOD 2012 .......................................... 158

Tabla 19-3 Factores de Expansión modelando solo PM2, EOD 2012 .......................................... 158

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

11

Tabla 19-4 Factores de Expansión modelando PM1 y PM2, EOD 2012 ...................................... 159

Tabla 19-5 Factores de Expansión modelando PM1 y FP, EOD 2012 .......................................... 159

Tabla 19-6 Factores de Expansión modelando PM1, PM2 y FP, EOD 2012 ................................ 159

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# I NTRODUCCIÓN

12

La Subsecretaría de Transportes llamó, el 1 de septiembre de 2016, a Propuesta

Pública para la realización del Estudio “Actualización del Modelo ESTRAUS con Información

de la EOD 2012”. La finalidad del estudio, según se establece en las Bases Técnicas de sus

Términos de Referencia, es **recalibrar el modelo de equilibrio simultáneo ESTRAUS,**

**validando el modelo con la información recogida para caracterizar el sistema**

**de transporte urbano al año 2012** . Ello, con el propósito de permitir a sus usuarios

disponer de una versión actualizada y eficiente de esta herramienta de modelación que apoyan

el análisis asociado a la planificación de los sistemas de transporte urbano en Chile.

El estudio fue adjudicado a la empresa Fernández y de Cea Ingenieros Limitada,

firmándose el convenio de trabajo correspondiente el 26 de octubre del año 2016. La

tramitación de la correspondiente Resolución Exenta por parte de la Subsecretaría de

Transportes, se realizó con fecha 6 de diciembre de 2016, siendo el día 9 de diciembre del

año 2016 la fecha oficial de inicio del estudio, según lo informado por Sectra.

Las Bases Técnicas de los Términos de Referencia de este estudio definen una serie

de 19 tareas. Adicionalmente, en la propuesta de este Equipo Consultor se ofreció realizar una

tarea adicional.

**T** **AREA** **1** : A JUSTE M ETODOLÓGICO

**T** **AREA** **2** : R EVISIÓN B IBLIOGRÁFICA

**T** **AREA** **3** : A NÁLISIS DE I NFORMACIÓN D ISPONIBLE

**T** **AREA** **4** : D EFINICIÓN DEL Á REA DE E STUDIO

**T** **AREA** **5** : Z ONIFICACIÓN

**T** **AREA** **6** : D EFINICIÓN DE LOS P ERÍODOS DE M ODELACIÓN

**T** **AREA** **7** : D EFINICIÓN DE LAS C ATEGORÍAS DE U SUARIO

**T** **AREA** **8** : D EFINICIÓN DE P ROPÓSITOS DE V IAJE

**T** **AREA** **9** : D EFINICIÓN DE M ODOS DE T RANSPORTE

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**T** **AREA** **10** : C ALIBRACIÓN DE LOS M ODELOS DE A SIGNACIÓN

**T** **AREA** **11** : A NÁLISIS DE LOS M ODELOS DE D EMANDA DE ESTRAUS

**T** **AREA** **12** : C ALIBRACIÓN DE M ODELOS DE G ENERACIÓN Y A TRACCIÓN

**T** **AREA** **13** : C ALIBRACIÓN DE M ODELOS DE P ARTICIÓN M ODAL

**T** **AREA** **14** : C ALIBRACIÓN DE M ODELOS DE D ISTRIBUCIÓN

**T** **AREA** **15** : V ALIDACIONES DE LOS M ODELOS DE D EMANDA

**T** **AREA** **16** : D EFINICIÓN M ODELO DE E LECCIÓN H ORARIA DE V IAJE

**T** **AREA** **17** : V ALIDACIÓN DEL M ODELO C OMPLETO

**T** **AREA** **18** : A NÁLISIS DEL S ISTEMA DE T RANSPORTE EN UN C ORTE T EMPORAL F UTURO

**T** **AREA** **19** : C ÁLCULO DE F ACTORES DE E XPANSIÓN

13

**T** **AREA** **20** : C ALIBRACIÓN S IMULTÁNEA DE LOS M ODELOS DE D ISTRIBUCIÓN DE V IAJES,

P ARTICIÓN M ODAL Y E LECCIÓN DE H ORARIO

El presente documento corresponde al Resumen Ejecutivo del Informe Final y

recopila los principales aspectos del desarrollo de la totalidad de las tareas realizadas.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 1 A JUSTE M ETODOLÓGICO (T AREA 1)

14

Como parte de esta tarea, al inicio del Estudio se revisó y discutió con el Director

del Estudio todas las proposiciones metodológicas contenidas en esta Propuesta Técnica,

incluyendo aquellas relativas a requerimientos de información, enfoques de definición y

calibración de los modelos, adecuada consideración de las últimas actualizaciones

metodológicas incluidas tanto en el modelo matemático como en la implementación

computacional de ESTRAUS, y todas las demás especificaciones de las distintas tareas del

Estudio.

El modelo ESTRAUS es un modelo de equilibrio simultáneo para analizar y evaluar

estratégicamente sistemas multimodales de transporte urbano, con múltiples clases de usuarios.

La actual versión del modelo considera, en su versión más general, equilibrio entre las etapas

de distribución, partición modal, elección de horario y asignación; restricción de capacidad de

las vías y restricción de capacidad de los vehículos que prestan servicios de transporte público.

Por otra parte, en términos de las decisiones de demanda (elección de destinos

según un modelo de distribución consolidado DCM, elección de modos de acuerdo a un

modelo de partición modal de tipo logit jerárquico y elección del horario de inicio de viaje

según un modelo logit multinomial), ESTRAUS las puede suponer simultáneas (distribución y

partición modal al mismo nivel jerárquico), o secuenciales (primero distribución y luego partición

modal), además de contar con la suficiente flexibilidad para permitir formular distintas

estructuras de equilibrio según el problema específico que se desee modelar, a saber:

distribución fija o variable, uno o más sub-periodos (horarios) de realización de los viajes dentro

del periodo de modelación, etc.

La asignación sobre las redes de transporte público y privado se trata como un

problema de equilibrio determinístico, y supone que los viajeros se comportan de acuerdo al

primer principio de Wardrop.

Así, las generaciones y atracciones de viajes son exógenas al modelo y en

consecuencia las relaciones de largo plazo existentes entre el sistema de transporte y el sistema

de actividades no son modeladas por él.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 2 R EVISIÓN B IBLIOGRÁFICA (T AREA 2)

15

En esta tarea se realizó un análisis crítico de cada uno de los documentos

presentados como referencias, revisando cada uno de acuerdo a su relevancia para la

recalibración del modelo ESTRAUS en su aplicación al análisis estratégico de Santiago.

La bibliografía relevante a tener en cuenta para esta tarea, de acuerdo a las Bases

Técnicas del Estudio, es la siguiente (se actualizaron los años y títulos de algunos de los Estudios

a la fecha de entrega del informe final de los mismos):

[ **Referencia 01** ] "Manual del Usuario del Modelo ESTRAUS", Subsecretaría de

Transportes - SECTRA, 2015.

[ **Referencia 02** ] " Actualización y Mantención de Modelos Estratégicos de Transporte

Urbano ", Subsecretaría de Transportes - SECTRA, 2013.

[ **Referencia 03** ] "Actualización Metodología Análisis Sistema de Transporte de Ciudades de

Gran Tamaño y Tamaño Medio (MESPE)"; MIDEPLAN - SECTRA, 2008.

[ **Referencia 04** ] "Análisis Actualización y Mantención de Modelos de Transporte",

Subsecretaría de Transportes - SECTRA, 2015.

[ **Referencia 05** ] "Incorporación de la Velocidad Variable con el Flujo en la Modelación

de Corredores de Buses en ESTRAUS y VIVALDI", Subsecretaría de
Transportes - SECTRA, 2015.

[ **Referencia 06** ] "Incorporación de la Restricción de Capacidad de los Estacionamientos

en los Modelos ESTRAUS y VIVALDI", Subsecretaría de
Transportes - SECTRA, 2015.

[ **Referencia 07** ] "Incorporación en los Modelos ESTRAUS y VIVALDI la Interacción

Asimétrica de Costos en las Autopistas", Subsecretaría de
Transportes - SECTRA, 2015.

[ **Referencia 08** ] "Actualización Generalización del Modelo de Distribución de Viajes en

ESTRAUS y VIVALDI", Subsecretaría de Transportes - SECTRA, 2013.

[ **Referencia 09** ] "Análisis de Nuevos Modelos de Distribución", Subsecretaría de

Transportes - SECTRA, 2011.

[Referencia 10] "Calibración de los Parámetros de Atractividad de Metro", Subsecretaría
de Transportes - SECTRA, 2011.

[ **Referencia 11** ] "Análisis y Modelación del Período Punta Tarde de ESTRAUS",

MIDEPLAN - SECTRA, 2010.

[ **Referencia 12** ] "Análisis y Formulación de Nuevos Modelos de Generación y Atracción

de Viajes", MIDEPLAN - SECTRA, 2010.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

16

[ **Referencia 13** ] "Análisis Desarrollo Asignación Multipropósito en Redes de Transporte

Público", MIDEPLAN - SECTRA, 2010.

[Referencia 14] "Actualización y Recolección de Información del Sistema de Transporte
Urbano, Etapa IX", Subsecretaría de Transportes - SECTRA, 2014.

[Referencia 15] "Mediciones de Aforos de Tráfico y Perfiles de Carga en Servicios Troncales
en el Gran Santiago", Subsecretaría de Transportes - SECTRA, 2013.

[Referencia 16] "Análisis y Desarrollo de Escenarios de Desarrollo Urbano para el Gran
Santiago", Subsecretaría de Transportes - SECTRA, 2016.

[Referencia 17] "Análisis Estratégico de Proyectos de Transporte Urbano, Etapa V, Orden
de Trabajo N°1", Subsecretaría de Transportes - SECTRA, 2015.

[ **Referencia 18** ] "Análisis Modernización de Transporte Público, IV Etapa: Estimación de

Velocidades Comerciales de Buses en Vías de Circulación Compartida
Mediante Microsimulación - Orden de Trabajo N°11",
MIDEPLAN - SECTRA, 2002.

[Referencia 19] "Actualización de Perfiles de Flujos del Modelo MODEM para el Gran
Santiago y Regiones", Subsecretaría de Transportes - SECTRA, 2015.

[ **Referencia 20** ] "Análisis Desarrollo Asignación Multipropósito en Redes de Transporte

Público", MIDEPLAN - SECTRA, 2010.

[ **Referencia 21** ] "Análisis de la Temporalidad de los Viajes", MIDEPLAN - SECTRA, 2002.

[ **Referencia 22** ] "Análisis y Actualización del Modelo ESTRAUS", MIDEPLAN - SECTRA, 2005.

[Referencia 23] "Análisis Estratégico de Proyectos de Transporte Urbano, Etapa V, Orden
de Trabajo N°7", Subsecretaría de Transportes - SECTRA, 2015.

El Equipo Consultor de Fernández y de Cea Ingenieros Ltda. (FDC), que está a

cargo del desarrollo del Estudio, ha participado en la elaboración de 16 de estos 23

documentos (aquellos destacados en negrita), correspondientes a informes finales de estudios y

manuales de los modelos; además cuenta con un vasto conocimiento teórico y práctico del

modelo ESTRAUS (en todas sus aplicaciones), y una gran experiencia en su uso. En efecto, el

equipo de profesionales de nuestra empresa que participa en este Estudio, ha llevado a cabo

las tareas de desarrollo y mantención de ESTRAUS desde su génesis (hace tres décadas), tanto

a nivel de formulación teórica como de implementación práctica de los modelos. De hecho, este

equipo Consultor es responsable de los principales avances a nivel de formulación matemática,

desarrollo algorítmico e implementación computacional de ESTRAUS.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

17

Por lo tanto, adicionalmente a la bibliografía propuesta en las Bases Técnicas del

Estudio, se consideran para efectos de esta tarea, la bibliografía siguiente, también elaborada

por el equipo Técnico de FDC:

[ **Referencia A.1** ] "Manual del Usuario del Modelo ESTRAUS", Subsecretaría de

Transportes - SECTRA, 2016.

[ **Referencia A.2** ] “Programa de Mantención Modelos Estratégicos de Transporte Urbano”,

Subsecretaría de Transportes - SECTRA, 2016.

[ **Referencia A.3** ] “Actualización de Modelos de Distribución de Viajes”, Subsecretaría de

Transportes - SECTRA, 2012.

[ **Referencia A.4** ] “Análisis, Desarrollo y Actualización de Modelos Estratégicos de

Transporte Urbano”, Subsecretaría de Transportes - SECTRA, 2012.

Además, se consideran en esta tarea todos los trabajos científicos que este equipo

consultor ha publicado en revistas internacionales ISI, entre los que se cuentan los siguientes:

 - **DE GRANGE, L., FERNÁNDEZ, J.E., DE CEA, J., IRRAZÁBAL, M.**

**(2010)** “Combined Model Calibration and Spatial Aggregation”.

**Networks and Spatial Economics,** 10, 4, 551-148578.

 - **DE CEA, J.**, **FERNÁNDEZ, J.E.**, **DE GRANGE, L.** **(2008)** “Combined

models with hierarchical demand choices: A multi-objective entropy

optimization approach”. **Transport Reviews,** Julio, 28, 4, 415-438.

 - **FERNÁNDEZ, J.E.**, **DE CEA, J.,** **MALBRÁN, H.,** **(2008)** “Demand

responsive urban public transport system design: Methodology and

application”. **Transportation Research Part A**, 42, 7, 951-972.

 - **SIEGEL J., DE CEA, J., FERNÁNDEZ J.E., RODRÍGUEZ R. AND**

**BOYCE D. (2006)** “Comparisons of urban travel forecasts with the

sequential procedure and a combined model”. **Networks and Spatial**

**Economics,** 6, 2, 135-148.

 - **FERNÁNDEZ, J.E., DE CEA, J., DE GRANGE L. (2005)** “Production

costs, congestion, scope and scale economies in urban bus transportation

corridors”. **Transportation Research A**, Vol 39-5, pp. 383-403.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

18

 **DE CEA CH., J. FERNÁNDEZ J.E., DEKOCK V., SOTO A. (2005)**

“Solving network equilibrium problems on multimodal urban transportation

networks with multiple user classes”. **Transport Reviews**, Vol. 25-3, pp.

293-317(25).

 **FERNÁNDEZ, J.E. DE CEA, J., SOTO A. (2003)** “Multimodal Equilibrium

Models for Predicting Intercity Freight Flows”. (FONDECYT 1950976).

**Transportation Research B**, Vol 37 No 7, pp. 615-640.

 **DE CEA, J., FERNÁNDEZ, J.E. (1996)** “An Empirical Comparison of

Equilibrium and Non Equilibrium Transit Assignment Models”. **Traffic**

**Engineering and Control**, Vol. 37, (7/8) 441-442.

 - **FERNANDEZ, J.E., DE CEA, J. y** **FLORIAN, M** ., **CABRERA, E. (1994)**

“Network equilibrium models with combined modes”, **Transportation**

**Science** (Vol. 28, No3, 182-92).

 **DE CEA, J., FERNANDEZ, J.E. (1993)** Transit assignment for congested

public transport systems: an equilibrium model. **Transportation Science**

(Vol. 27, No2, 133-147).

A continuación, se detallan aquellos aspectos del análisis realizado a la

bibliografía, que resultan más relevantes de tener en cuenta para lograr los objetivos del Estudio.

**2.1** **Nuevas Funcionalidades en ESTRAUS**

Los modelos de transporte desarrollados por el Estado de Chile a través del

Programa de Vialidad y Transporte Urbano SECTRA, del Ministerio de Transporte y

Telecomunicaciones, constituyen una importantísima herramienta para la planificación de los

sistemas de transporte en nuestro país, que ha demostrado ser un ejemplo en este campo y un

referente a nivel mundial.

Estos modelos, en específico el modelo de equilibrio simultáneo ESTRAUS, se

someten a una continua actualización para mantener su sustento teórico al nivel del Estado del

Arte en lo que a este tipo de análisis se refiere. Es así como permanentemente se mejoran las

correspondientes formulaciones matemáticas asociadas para incorporar en ellas las últimas

capacidades de modelación disponibles para tratar el problema de equilibrio simultáneo y para

modelar adecuadamente los fenómenos y comportamientos de los sistemas de transporte a

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

19

evaluar. Del mismo modo, continuamente se efectúan revisiones e implementan correcciones,

mejoras, y nuevos desarrollos para adaptar los programas principales y utilitarios, post

procesos, interfaz gráfica y otras aplicaciones informáticas asociadas a ESTRAUS, de modo de

hacerlos compatibles con las nuevas funcionalidades y desarrollos teóricos de su formulación

matemática (Referencias 01, 02, 08).

En este contexto, en los últimos años, en forma posterior a la última calibración del

modelo para la ciudad de Santiago (Referencia 22, año 2005), se han incorporado a ESTRAUS

capacidades de modelación específicas, algunas de las cuáles son abordadas explícitamente

en este Estudio. Estas nuevas capacidades de modelación y su alcance en el contexto de la

calibración de ESTRAUS, fueron todas implementadas por parte del equipo técnico que este

Consultor propone para la realización del presente Estudio, y que es responsable de los

avances a nivel de formulación matemática, desarrollo algorítmico e implementación

computacional de ESTRAUS desde su génesis.

Las nuevas capacidades de modelación que se abordan explícitamente en este

Estudio son:

 Generalización del modelo de distribución de viajes

`o` Modelo DCM (Referencia 09)

`o` Distribución simplemente acotada a orígenes (Referencia 08)

 Velocidad variable con el flujo en los corredores de transporte público

(Referencia 05)

 Restricción de capacidad de los estacionamientos (Referencia 06)

 Asignación multiclase en transporte público (Referencias 13 y 20)

 Interacción asimétrica de los flujos de automóviles en las autopistas

(Referencia 07)

**2.2** **Modelo de Elección Horaria**

El Ministerio de Planificación y Cooperación (MIDEPLAN), llamó, en mayo de

2001, a Propuesta Pública para la realización del Estudio “Análisis de la Temporalidad de los

Viajes” (Referencia 21, año 2002). La finalidad principal del estudio, según se establece en las

Bases Técnicas de sus Términos de Referencia, fue “incorporar en el proceso de equilibrio del

modelo ESTRAUS, la etapa de generación de viajes, de manera de considerar el efecto de la

congestión en las decisiones de los usuarios sobre la hora de realización de sus viajes”.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

20

El enfoque de modelación utilizado para la incorporación de la elección de horario

consiste en agregar a las decisiones de destino y modo, la de hora de realización de los viajes,

como un nivel adicional en la estructura de decisiones, modelándola mediante un Logit

multinomial (esto, en el marco de los modelos de equilibrio con generaciones y atracciones

exógenas y con estructura jerárquica para las decisiones de demanda). La idea básica en este

caso es que en lugar de que las generaciones de viajes sean fijas para un período (por ejemplo,

para la hora punta), y todos ellos deban realizarse en dicha hora, se define un período más

amplio (por ejemplo, la hora punta, la anterior y la inmediatamente posterior), en el cual las

generaciones y atracciones de viaje son efectivamente fijas (exógenas al modelo de equilibrio).

Sin embargo, en este enfoque, dependiendo de una serie de variables explicativas

que son definidas al momento de calibrar el modelo, la hora específica de realización de un

viaje dentro del período mayor, será el resultado de una serie de decisiones con estructura

jerárquica, que considerará en forma adecuada el grado de congestión de las diferentes redes

modales en los diferentes períodos en que una determinada categoría de usuarios puede

realizar su viaje.

La modelación de la elección de horario busca reconocer que el hecho de mantener

generaciones fijas (datos exógenos al modelo) por período, suele producir problemas en

períodos de punta al modelar algunas situaciones futuras, cuando los aumentos de viajes

predichos para ciertas áreas de la región estudiada resultan ser mayores (bastante mayores en

algunos casos) a los que pueden ser soportados, con niveles de servicio realistas, dada la

capacidad supuesta para el sistema de transporte. Este problema es muy difícil que se presente

en períodos de fuera de punta en los que la capacidad excede considerablemente la demanda

(considérese, por ejemplo, el caso de los sistemas de transporte público, en los que el

dimensionamiento de la oferta casi siempre queda definido por las demandas de punta de día

laboral, que normalmente más que duplican a las de otros períodos).

Es evidente que al interior de un período de punta (por ejemplo 7:00 AM a 9:00

AM en día laboral) la inmensa mayoría de los viajes deben realizarse dentro del período,

independientemente del nivel de congestión existente en el sistema de transporte (por ejemplo,

los viajes al estudio y al trabajo). En consecuencia, el usuario, más que decidir hacer o no hacer

un viaje en el período (como podría resultar de un enfoque de generación de viajes dependiente

del nivel de congestión), frente a situaciones extremas normalmente podrá decidir cambiar la

hora de inicio de su viaje (estudios empíricos muestran que esta es la primera opción de cambio

en los hábitos de viaje, en situaciones de alta congestión) o cambiar de modo (por ejemplo

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

21

cambiar a metro en caso que exista capacidad si los modos de superficie presentan altos niveles

de congestión).

En la práctica se ha observado que la alternativa más probable es que la elección

de modo sea anterior a la de horario, es decir, frente a situaciones extremas, el viajero

normalmente decidirá cambiar la hora de inicio de su viaje antes que cambiar de modo. De

esta forma, aprovechando la estructura jerárquica supuesta en ESTRAUS para las decisiones de

demanda, la consideración de la elección de horario se basa en suponer generaciones fijas

para un determinado período (por ejemplo, dos o tres horas) al interior del cual los usuarios

escogen el sub-período en que realizan sus viajes.

**2.3** **Periodo Punta Tarde**

En la Referencia 11, año 2010, se realiza un análisis de las características de los

viajes del período Punta Tarde, reportados en las encuestas EOD-H 2001 y EOD-H 2006. Para

ello, se toma un período Punta Tarde Ampliado (17:45-19:45).

Para el año 2006, se obtuvo la siguiente distribución de viajes según propósito.

|Propósito ESTRAUS|Viajes|Total%|Registros|Total%|
|---|---|---|---|---|
|AL ESTUDIO<br>AL TRABAJO|423,548<br>923,878|13.78%<br>30.06%|919<br>3,225|8.18%<br>28.69%|
|OTROS<br>Total|1,726,157<br>3,073,584|56.16%<br>100.00%|7,096<br>11,240|63.13%<br>100.00%|
|13.78%<br>30.06%<br>56.16%<br>AL ESTUDIO<br>AL TRABAJO<br>OTROS|13.78%<br>30.06%<br>56.16%<br>AL ESTUDIO<br>AL TRABAJO<br>OTROS|13.78%<br>30.06%<br>56.16%<br>AL ESTUDIO<br>AL TRABAJO<br>OTROS|13.78%<br>30.06%<br>56.16%<br>AL ESTUDIO<br>AL TRABAJO<br>OTROS|13.78%<br>30.06%<br>56.16%<br>AL ESTUDIO<br>AL TRABAJO<br>OTROS|

**Ilustración 2-1 Viajes según Propósito ESTRAUS, PT 2006**

Fuente: EOD-H 2006/Elaboración propia.

Como puede verse el propósito Otros es el que presenta el mayor número de viajes

(mayor a los dos otros propósitos Estudio y Trabajo sumados). Además, el propósito Otros,

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

22

presenta una gran variedad de motivos diferentes de viaje como se puede observar en la

siguiente tabla:

**Tabla 2-1 Viajes según Propósito EOD-H, PT 2006**

Fuente: EOD-H 2006/Elaboración propia.

El propósito “Vuelta a Casa” es el que concentra el mayor número de viajes. Sin

embargo, un viaje “Vuelta a Casa” se agrega en ESTRAUS a alguno de los propósitos primarios

(Trabajo, Estudio u Otros).

Tradicionalmente se ha argumentado que el Período Punta Tarde debe tener

características especiales dado la existencia de viajes “encadenados” y viajes “espejo”. En los

primeros la persona realiza un viaje con propósito especial (Salud, Compras, Otros), previo a

realizar el viaje de Vuelta a Casa, en el segundo caso el viaje de la tarde es el inverso al

realizado en la mañana y posee las mismas características en cuanto al modo utilizado (la

elección de modo en la tarde está determinado por el modo utilizado en el viaje de la mañana).

Sin embargo, el resultado del análisis de los viajes de la EOD-H 2006 para los

tipos de viajes mencionados en el párrafo anterior durante el período Punta Tarde, indica que

los viajes “encadenados” representan un porcentaje muy bajo del total de viajes realizados

durante el período: 2,74% (2,08% desde el Trabajo y 0,66% desde el Estudio). Por lo tanto, no

sería recomendable realizar un tratamiento especial para estos viajes, dada su casi nula

relevancia y la poca cantidad de registros disponibles para análisis.

Por otra parte, para los viajes “espejo” se encontró que un 53% de los viajes con

motivo trabajo son de estas características, por lo que sería recomendable establecer un

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

23

porcentaje de viajes de este propósito para los que no exista elección de modo en la punta

tarde, sino que se replica lo modelado en punta mañana. Respecto de los otros motivos de viaje,

solo el 14,8% de los viajes con motivo Estudio y el 1,64% del motivo Otros tienen la

característica de “espejo”. Esto indica que la gran mayoría de los viajes relacionados con estos

dos propósitos se realizan en forma independiente del comportamiento de los viajes de la Punta

Mañana y por lo tanto debieran modelarse en forma independiente para el Período Punta

Tarde.

Las conclusiones indicadas en los párrafos anteriores fueron corroboradas

analizando las características de los viajes del período Punta Tarde considerando la información

recolectada en la EOD 2012. A partir de dicho análisis se decidió el tratamiento otorgado a

los viajes “encadenados” y “espejo” (ver Tarea 8: Definición de Propósitos de Viaje). Para los

viajes que no posean dichas características se aplicó un procedimiento de calibración

independiente al de los otros períodos.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 3 A NÁLISIS DE I NFORMACIÓN D ISPONIBLE (T AREA 3)

24

En esta tarea se analizó y depuró la información disponible para llevar a cabo la

actualización del modelo ESTRAUS. Sólo se consideró la información entregada por el Director

del Estudio hasta la fecha de ejecución de esta tarea. Adicionalmente, se identifican fuentes

complementarias de información adecuadas para la calibración de cada etapa del modelo

ESTRAUS y se discuten posibles limitantes en la modelación debido a la falta de información.

**3.1** **Encuesta Origen Destino 2012**

La principal fuente de información del estudio es la Encuesta Origen-Destino 2012

(EOD 2012). La información recolectada en esta encuesta se divide en dos grandes grupos:

(i) registros de viajes de una muestra representativa de hogares del Gran Santiago, y

(ii) medición de niveles de servicio en la red de transporte del Gran Santiago. Mientras la

primera fuente se utiliza para calibrar la mayoría de los modelos de demanda (generación y

atracción, distribución, elección horaria, y elección modal), los niveles de servicio se utilizan

tanto para calibrar como validar y ajustar los modelos obtenidos.

Además, la información de la EOD 2012 debe ser complementada con otras

fuentes. La primera de ellas tiene que ver con las principales características agregadas de las

zonas generadoras y atractoras de viajes, las cuales son utilizadas como proxy de la actividad

económica de cada zona. Dado que el transporte es una actividad derivada de la actividad

económica, es de esperar que, a mayor actividad económica en una zona, se registren más

viajes con origen y/o destino en ella. Por ello, se recurre a indicadores de actividad económica

georreferenciados en bases de datos del Servicio de Impuestos Internos (SII).

En segundo lugar, resulta necesario complementar los niveles de servicios

registrados en la EOD 2012 con información sobre los servicios troncales del transporte público,

los cuales fueron excluidos de la EOD 2012, además de mediciones de flujos y pasajeros en

líneas pantalla. Estas mediciones permiten calcular factores de sub(sobre) reporte en base a los

viajes registrados en la EOD 2012 y los realmente observados.

Adicionalmente, en la EOD 2012 se incluye un catastro de las líneas de transporte

público de buses rurales, taxi, y taxi colectivos. También se incluye un resumen de las normativas

y restricciones legales a las que el transporte de carga debe atenerse (e.g. restricciones de

acceder al centro de Santiago en ciertos horarios).

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

25

**3.2** **Mediciones de aforos de tráfico y perfiles de carga en servicios**

**troncales en el gran Santiago**

Dicho estudio contiene tres conjuntos de datos relevantes. El primero corresponde

a mediciones de flujo de vehículos y pasajeros (tasas de ocupación) en 40 puntos de Santiago.

Los datos fueron medidos para todos los períodos del estudio, salvo entre las 23:00 y 6:00

horas. Esta información puede ser utilizada para medir el ajuste del modelo calibrado.

El segundo grupo de datos recolectados en este estudio corresponde a mediciones

de flujo y pasajeros (i.e. tasas de ocupación) en líneas pantalla en Santiago. Estas mediciones

permiten calcular un factor de sub(sobre) reporte al compararse con los viajes registrados en la

EOD 2012.

Finalmente, el tercer grupo de datos relevantes contenidos en el estudio de DICTUC

corresponde a la medición de niveles de servicio de buses troncales del Transantiago,

específicamente sus perfiles de carga y velocidades de operación. Mientras los perfiles de

carga son utilizados para medir el ajuste de los modelos calibrados, las velocidades de

operación pueden ser también utilizadas para fijar una velocidad de diseño a los servicios, por

ejemplo, en lugares donde existen pistas exclusivas o segregadas para el transporte público.

Las mediciones se realizaron para los períodos punta mañana (ambos sub

períodos), fuera de punta, y punta tarde. Se midieron los perfiles de carga en 38 recorridos, y

las velocidades promedio en 40 recorridos por los principales ejes de Santiago.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 4 D EFINICIÓN DEL Á REA DE E STUDIO (T AREA 4)

26

El área de estudio definida corresponde a aquella considerada en la Encuesta

Origen Destino 2012, constituida por 45 comunas de la región Metropolitana: 32 de la

provincia de Santiago, 5 de la provincia de Talagante, 2 de Chacabuco, 3 de Maipo, 2 de

Cordillera y 1 de Melipilla, tal como se detalla en la siguiente tabla:

**Tabla 4-1 Área de Estudio**

Fuente: Informe Final Vol.1, EOD Stgo.2012.

Esta definición cubre todos los lugares, donde se producen o se atraen los viajes

que utilizan el sistema de transporte analizado, albergando aproximadamente 65 millones de

habitantes con una cantidad estimada de 1.160.000 vehículos particulares, 6.300 buses

urbanos, 27.000 taxis básicos, 11.000 taxis colectivos urbanos y cinco líneas de metro con

104 km de vías, según se reporta en el Informe Final de la EOD 2012.

Por otro lado, aunque en transporte urbano el área de estudio está normalmente

asociada con los límites espaciales de la conurbación, muchas veces es necesario considerar

también las influencias externas (por ejemplo, transporte interurbano de pasajeros y de carga).

El modelo explica la operación del sistema de transporte dentro del área de estudio (cuyo

perímetro físico está definido por un **cordón externo** ), y las influencias externas deben ser

tratadas como datos exógenos del problema, que el modelo debe considerar, pero que no

puede explicar. Sobre este punto específico, también se respeta lo definido en el contexto de la

EOD 2012, que consideró 10 zonas externas (exógenas al cordón externo definido), según se

detalla en la siguiente tabla:

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 4-2 Zonas Externas**

Fuente: Informe Final Vol.1, EOD Stgo.2012.

27

Considerando todo lo anterior, la figura siguiente muestra, en color naranjo, el área

de estudio definida para esta calibración del modelo ESTRAUS.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 4-1 Área de Estudio**

Fuente: Elaboración propia.

28

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 5 Z ONIFICACIÓN (T AREA 5)

29

Definido el contexto espacial como parte de la Tarea 4, el área de estudio debía

dividirse en zonas más pequeñas, que constituyeran en adelante la unidad espacial básica del

análisis de transporte. Estas zonas debían ser homogéneas en términos de utilización de suelos

y de características socioeconómicas de la población, dado que éstas son dos variables

fundamentales para explicar la demanda de viajes.

Para definir la nueva zonificación se analizaron las zonificaciones existentes, de tal

forma que la nueva zonificación fuera compatible con ellas. En especial se buscaba

compatibilidad con la zonificación específica de la EOD 2012 (866 zonas internas), de modo

de facilitar el uso del modelo ESTRAUS para actuales y futuros análisis con información

proveniente de dicha encuesta. Por lo tanto, se trabajó en base a la zonificación actualmente

en uso para el modelo ESTRAUS, de 690 zonas (internas), teniendo en cuenta la desagregación

de ella realizada en el Estudio de la Referencia [15], y se logró su adaptación final a la

zonificación EOD 2012, que permite además comparar los nuevos resultados obtenidos con

los de la zonificación anterior.

En específico, se realizaron las siguientes actividades para verificar la que la nueva

zonificación (EOD 2012), fuera adecuada a las necesidades de modelación de este Estudio:

1. Se estudiaron las divisiones administrativas y políticas del área de estudio, a objeto

que la definición geográfica de las zonas las respete.

2. Se estudiaron los distintos sectores del área de estudio, identificando unidades

territoriales que presenten un comportamiento más o menos homogéneo, en

términos de su uso de suelos, nivel socioeconómico de la población, actividad, etc.

3. Se identificaron todas aquellas zonas singulares. Ello se justifica porque

normalmente no poseen un comportamiento de viajes similar al de otras zonas

preferentemente residenciales, comerciales o industriales, siendo aconsejable

identificarlas como una zona independiente.

La ventaja de ello radica en que las zonas resultantes son homogéneas en términos

de su uso de suelos y por lo tanto, los viajes generados y atraídos también lo son.

Su tratamiento no es diferente al de otras zonas, con la salvedad de que en éstas

no es necesario que existan hogares. Es evidente que esto redunda en mejores

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

30

calibraciones de modelos y además, flexibiliza el uso posterior del modelo,

especialmente cuando alguna de estas zonas cambia de uso de suelo.

4. Se analizó la información disponible relativa a viajes, usos de suelo, información

demográfica y socioeconómica.

5. Se analizaron los proyectos específicos de transporte público (líneas de metro,

corredores de buses, etc.), de tal manera que la zonificación propuesta permita

representar de manera adecuada la accesibilidad de los usuarios a dichos

servicios.

6. Se construyó una corrida ESTRAUS con la nueva zonificación (la correspondiente

a la EOD 2012), en base a las corridas Sectra en uso para ese año de modelación

(situación base de Santiago en periodos Punta Mañana y Fuera de Punta), y se

ejecutó para verificar que se reproducían los resultados de la corrida original como

una forma de validar la correctitud de la zonificación definida.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 6 D EFINICIÓN DE LOS P ERIODOS DE M ODELACIÓN (T AREA 6)

31

La elección de períodos a modelar requiere de una clasificación de las distintas

horas del día en grupos que presenten características de operación homogéneas. A fin de

realizar una periodización adecuada al proceso de calibración que se desarrolló en el presente

estudio, es necesario tener presente que el modelo de transporte realiza la hipótesis de flujos

steady state. Sin embargo, esto no ocurre en la práctica y debe tomarse sólo en sentido

aproximado (o interpretarse correctamente).

Analizando los histogramas de viajes por distribución horaria, podemos observar

que los viajes de Transporte Público y Privado presentan perfiles bastante similares, con respecto

a la distribución de períodos Punta y Fuera de Punta, a pesar de que los viajes en transporte

público son en general mayores, para todas las horas del día. Por lo tanto, no hay problemas

de puntas diferentes para ambas categorías de viajes y podemos definir un período único

analizando la distribución horaria de los viajes totales.

**Ilustración 6-1 Representación Continua (todos los modos por hora media de**

**viaje)**

Fuente: Elaboración propia a partir de la EOD2012.

En consideración a lo planteado, para la definición de los períodos de modelación,

se utilizaron los diagramas de distribución horaria de viajes interzonales en los modos que

modelan en ESTRAUS, construidos contabilizando cada viaje en un solo intervalo (período de

15 minutos), correspondiente al punto medio de su desarrollo (tiempo medio de viaje).

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

32

A partir de ellos, se escogen los períodos que representan condiciones de

operación típicas y en torno de los cuales se pueda suponer características operacionales

promedio diferentes a las del resto de los períodos a analizar. Considerando las características

de la implementación computacional de ESTRAUS, cada uno de los periodos a modelar debe

tener una extensión de una hora.

Sobre la base de los análisis realizados se obtuvieron los siguientes períodos:

 Punta mañana (PM): Dada la restricción de tener períodos de modelación de

una hora y que se debe definir un período punta mañana alternativo, es

necesario elegir un total de dos horas para el período total punta mañana, el

que debe ser dividido en dos subperíodos de una hora cada uno. Utilizando

como base el histograma de distribución de viajes por cuarto de hora, se obtuvo

un período PM de dos horas entre 7:00 y 9:00 que maximiza el número de

viajes realizado, entre todas las alternativas de períodos de la misma duración.

Este período total se puede subdividir en dos subperíodos, el primero **PM1**

(7:00-8:00), y el segundo **PM2** (8:00-9:00). El total de viajes realizados en

estos períodos son los siguientes (viajes interzonales en modos ESTRAUS14):

`o` **PM1: 1.542.386 viajes** .

`o` **PM2: 1.069.103 viajes** .

 Fuera de Punta (FP): Hay un período con densidades de viaje bastante similares

que va entre las 9:00 AM y las 15:30 PM. Dada la restricción de considerar

solo una hora de modelación y la necesidad de tener información de conteos

de flujos para la etapa de validación se eligió el período Fuera de Punta (FP)

entre (10:00-11:00) [1] . La cantidad de viajes totales promedio por hora durante

el período **FP** es de **: 665.998 viajes** .

 Punta Tarde (PT): En la tarde hay un período punta entre las 18:00 y las 19:00

que maximiza el número de viajes por hora en el período (15:30-19:00). Este

período presenta puntas extremas de menor magnitud, pero es más extenso que

1 De acuerdo con las densidades de viajes observadas podría considerase también como parte de la FP el período

de 19:00-21:00.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

33

el de punta mañana. La cantidad de viajes totales promedio por hora durante

la hora elegida para **PT** es de: **1.153.506 viajes.**

La representación más adecuada, de acuerdo con las hipótesis de comportamiento

implícitas en el modelo, corresponde a una distribución rectangular que presenta una densidad

constante de tráfico durante todo el período, igual a la densidad promedio por unidad de

tiempo (ver Figura 5). Esta densidad promedio representa las condiciones de operación que se

experimentan en los distintos puntos de cada ruta considerada en la red, a través del período.

A continuación, se muestra una representación esquemática de la distribución

horaria de viajes considerando las densidades promedio de viajes correspondientes a cada

período de modelación definido. En azul se pueden apreciar los viajes viajes totales, en rojo los

realizados en modos de transporte público, y en verde los correspondientes a transporte

privado. Así, por ejemplo, en el periodo PM1, los viajes totales son 1.542.386, en tanto que

los viajes en transporte público y privado son respectivamente, 672.089 y 608.669.

**Ilustración 6-2 Distribución Esqumática de Viajes Interzonales (modos**

**ESTRAUS-14)**

Fuente: Elaboración propia a partir de la EOD2012.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 7 D EFINICIÓN DE LAS C ATEGORÍAS DE U SUARIO (T AREA 7)

34

En esta tarea se definen las diversas categorías de usuarios a utilizar en todas las

simulaciones ESTRAUS que componen la modelación del sistema de transporte del Gran

Santiago. Estas categorías corresponden a una partición de los viajeros en grupos definidos por

cruces de sus características socioeconómicas. Estas características son elegidas a priori, y

deben satisfacer al menos las siguientes propiedades: (i) tener un impacto relevante en el

comportamiento de los viajeros y (ii) ser fáciles de proyectar en escenarios futuros.

Las características socioeconómicas elegidas, en acuerdo con la contraparte,

fueron **ingreso del hogar** y **número de vehículos motorizados en el hogar** . Estas

características han sido utilizadas exitosamente en calibraciones anteriores del modelo

ESTRAUS (e.g. calibración con datos de la EOD 2001). Se decidió excluir el número de

ocupantes del hogar, debido a la dificultad de predecirlo en escenarios futuros.

Las siguientes ilustraciones presentan el histograma de tenencia de vehículos en la

población y la distribución de ingreso en la población. La distribución en la población se obtiene

a partir de expansiones de la muestra aplicando factores de corrección calculados usando

datos censales.

**Ilustración 7-1 Histograma de tenencia de vehículos motorizados por hogar**

Fuente: Elaboración propia a partir de la EOD2012.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

35

**Ilustración 7-2 Histograma de ingreso por hogar**

Fuente: Elaboración propia a partir de la EOD2012.

A partir de la primera ilustración resulta evidente que no se justifica segmentar la

tenencia de vehículos motorizados en más de tres niveles. Por lo tanto, se decidió segmentar la

**tenencia de vehículos motorizados en tres niveles: i. ningún vehículo, ii. un**

**vehículo, y iii. dos o más vehículos** .

La segmentación de los niveles de ingreso, es, sin embargo, más compleja. Para

definirla se estiman tasas de generación de viajes, en busca de una categorización que arroje

tasas crecientes para el cruce de tenencia de vehículos y nivel de ingreso. En otras palabras, se

busca que la cantidad de viajes promedio realizada por un hogar tipo sea creciente con el

número de vehículos y el ingreso.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 7-1 Categorización de viajeros elegida**

|Col1|Observaciones|Distribución<br>de hogares en<br>la población|Tasas de viajes|
|---|---|---|---|
|**Ingreso (M$)**|Núm. de vehículos|Núm. de vehículos|Núm. de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|2769<br>378<br>14<br>3167<br>985<br>56<br>3122<br>1713<br>192<br>1914<br>2351<br>684<br>95<br>353<br>453|18%<br>22%<br>25%<br>28%<br>6%|0.130 0.163 <br>0.464 0.470 0.710<br>0.698 0.699 1.140<br>1.034 1.035 1.318<br>1.126 1.142 1.376|

Fuente: Elaboración propia.

36

La tabla anterior presenta la categorización de ingreso finalmente elegida,

construida a partir de segmentos de ingreso de igual tamaño, los cuales se ajustaron

manualmente.

Dado que la categorización elegida no genera tasas crecientes para algunos

propósitos de viaje, en otros períodos (Fuera de Punta y Punta Tarde), se buscaron nuevas

categorizaciones de usuarios para los períodos Punta Tarde y Fuera de Punta. Si bien fue posible

hallar una nueva categorización adecuada para el propósito “Trabajo + Estudio” en el período

Punta tarde, no fue posible hacerlo en el período Fuera de Punta para el propósito Otros.

Frente a este hecho, se decidió usar la misma categorización del periodo Punta

Mañana en todas las simulaciones de todos los períodos. Esto tiene sentido si consideramos que

los datos usados para diferentes períodos y propósitos provienen de los mismos hogares

encuestados en la EOD y se obtiene la ventaja de homologar las mismas categorías para todos

los casos (períodos o propósitos) que se analicen, facilitando la comparación de resultados

entre períodos, y el uso posterior de los resultados del modelo, como, por ejemplo, la evaluación

de proyectos.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 8 D EFINICIÓN DE P ROPÓSITOS DE V IAJE (T AREA 8)

37

El análisis de los sistemas de transporte ha considerado tradicionalmente tres

propósitos de viajes: trabajo, estudio, y otros, pudiéndose desagregar adicionalmente el

propósito estudio en dos o más clases: viajes de estudiantes de educación básica, de educación

media y de educación técnica-universitaria; esto porque la experiencia ha mostrado que tienen

un comportamiento marcadamente diferente. Así también lo propone la metodología existente

para ciudades de gran tamaño y así lo considera la actual aplicación del modelo de equilibrio

ESTRAUS para el caso de Santiago.

En sus diversas aplicaciones, el modelo ESTRAUS ha sido utilizado no sólo para la

evaluación de proyectos de transporte, sino también para la evaluación de ciertas políticas cuyo

impacto sobre la operación del sistema de transporte urbano es importante (políticas de impacto

estratégico). Entre éstas destacan aquellas relacionadas con la educación (por ejemplo, la

incorporación de la jornada escolar completa).

Al respecto, es deseable que los viajes realizados con ciertos propósitos (por

ejemplo, estudio), puedan ser modelados en forma más desagregada, de tal forma que la

evaluación de las políticas respectivas se realice de una manera más adecuada.

En relación con lo anterior, y en virtud de la información disponible, se analizó la

factibilidad de definir propósitos diferentes según periodo del día, y ampliar los propósitos de

viajes considerados a nivel de los modelos de demanda. Específicamente, se evaluó la

posibilidad de separar el propósito estudio en 3 sub-propósitos (enseñanza básica, media y

superior). Y dado que también podría ser útil desagregar el motivo “Otros” para la modelación

de “viajes no obligados”, se evaluó dividir el propósito “Otros” en dos categorías: “Otros

obligados” y “Otros no obligados”, o alternativamente separar el propósito “Compras” por su

importancia en cantidad de viajes, sobre todo en los periodos fuera de punta y punta tarde.

En resumen, resultante del análisis realizado, los propósitos a modelar son los

siguientes, según periodo del día:

a) PM1 y PM2 (7:00 a 9:00)

i. Trabajo
ii. Estudio1 (prescolar-básica-media)
iii. Estudio2 (técnico-universitario)
iv. Otros

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

b) FP (10:00 a 11:00)

i. Trabajo
ii. Estudio (todos)
iii. Compras
iv. Otros (sin incluir las compras)

v. Vuelta a Casa
c) PT (18:00 a 19:00)

i. Trabajo+Estudio
ii. Compras
iii. Otros (sin incluir las compras)
iv. Vuelta a Casa

38

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 9 D EFINICIÓN DE M ODOS DE T RANSPORTE (T AREA 9)

39

La elección de modos de transporte a considerar, requirió de un análisis cuidadoso

para determinar el uso y la relevancia de los distintos modos disponibles para satisfacer la

demanda por transporte.

En este contexto, la fuente de datos que más información aporta a este respecto, es

la incluida en la EOD a hogares. Consistentemente, los resultados que se obtienen de la EOD a

hogares fueron contrastados con las posibilidades de modelación que ofrece ESTRAUS, en que

se define un modo de transporte como cualquier forma de transporte que pueda ser usada para

viajar entre un origen y un destino, incluyendo modos puros y combinados; los modos de

transporte público pueden ser dependientes o independientes de la red vial (los modos

independientes son los que usan una red distinta a la red vial, y que pueden combinarse con

otros modos puros privados o públicos para formar modos combinados).

Por otro lado, ESTRAUS modela clases de modos de transporte, que corresponden

a agrupaciones de modos de transporte de acuerdo a ciertos principios de comportamiento

asociados a ellos: cualquier modo que cumpla con los principios de comportamiento de alguna

de las 5 clases de modos de transporte actualmente implementados en ESTRAUS, puede ser

modelado. Estas clases son las siguientes (de acuerdo a las características de los modos de

transporte que se agrupan en cada una de ellas):

AUTO: Rutas de viaje definidas en el proceso de equilibrio (por ejemplo, auto-chofer,

auto-acompañante).

TAXI: Rutas de viaje definidas en el proceso de equilibrio y costo de viaje incluye

una tarifa variable (por ejemplo, taxi).

CAMINATA: Rutas de viaje fijas y definidas por las rutas mínimas calculadas con tiempos

fijos de viaje (por ejemplo, caminata, bicicleta).

PUBLICO: Rutas de viaje fijas y predefinidas por su frecuencia y recorrido, además de

tarifa cobrada (por ejemplo, bus, metro, bus-metro).

AUTOMETRO: Combinación de un modo de la clase AUTO y un modo de la clase PUBLICO

con red independiente (por ejemplo, autochofer - metro).

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

40

Originalmente, se definieron 14 modos a modelar. Sin embargo, en Tareas

posteriores a la definición de modos de transporte, se encontraron diversas limitaciones que

obligaron a replantear la elección de los mismos. En particular, los modos de transporte

combinado **Autochofer-Metro y Autoacompañante-Metro fueron descartados**,

debido a su reducida partición modal. Esta complejiza de sobremanera su correcta modelación

e impide alcanzar una confiabilidad suficiente en la misma.

Además, el modo puro **Bus No Transantiago y su forma combinada Bus**

**No Transantiago-Metro también tuvieron que ser descartados** . En este caso, el

problema se dio a nivel de la oferta de transporte disponible para ellos, la cual no fue

correctamente catastrada en la EOD 2012. Por lo tanto, se posee una red de Bus No

Transantiago con una cantidad parcial de recorridos, lo que origina que la asignación de los

viajes reportados en la EOD 2012 se traduzca en niveles de servicio mucho peores a los reales.

Al no conocer la totalidad de la red de servicios de Bus No Transantiago, así como sus

capacidades y frecuencias, no es posible abordar el problema descartando solo los viajes de

aquellas personas que usaron los recorridos no faltantes (ya que no se sabe cuáles son).

**En consecuencia, de los 14 modos originalmente elegidos para**

**modelar, se terminó solo con 10, 8 puros y 2 combinados. A continuación, se**

**presentan los modos implementados en ESTRAUS:**

1. Caminata

2. Autochofer

3. Autoacompañante

4. Taxi

5. Bus (Transantiago)

6. Taxicolectivo

7. Metro (incluye Tren)

8. Bus-Metro

9. Taxicolectivo-Metro

12. Bicicleta

Adicionalmente, debido a inconsistencias en las bases de datos, fue necesario

eliminar observaciones. En particular, se consideró como criterio eliminar los viajes que poseían

zonas de origen y/o destino fuera del rango de la zonificación de la EOD 2012: menores que

1, mayores que 876 o indeterminadas (102.943 viajes). Otro criterio fue quitar viajes que

supuestamente se realizaron en modos que el viajero no tiene disponibles (124.214 viajes):

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

41

 Viajes en Autochofer cuando no hay auto en el hogar o el viajero no tiene

licencia (31.452 viajes)

 Viajes en Autoacompañante cuando no hay auto en el hogar (52.023

viajes)

 Viajes en Bus Transantiago cuando no hay recorridos con accesos en las

zonas de origen o destino (2.784 viajes)

 Viajes en Taxicolectivo cuando no hay recorridos con accesos en las zonas

de origen o destino (12.386 viajes)

 Viajes en Metro cuando no hay recorridos con accesos en las zonas de

origen o destino (2.745 viajes)

 Viajes en Metro-Bus Transantiago cuando no hay recorridos con accesos en

las zonas de origen o destino (15.610 viajes)

 Viajes en Metro-Taxicolectivo cuando no hay recorridos con accesos en las

zonas de origen o destino (114 viajes)

 Viajes en Bicicleta cuando no hay bicicletas en el hogar, diferenciando de

adulto y niño según la edad del viajero (7.100 viajes)

Finalmente, la partición modal a considerar como referencia para la modelación

de ESTRAUS, es la que se exhibe en la siguiente tabla.

**Tabla 9-1 Partición Modal - Base de Datos Definitiva**

|ID|Modo|Viajes<br>PM1|%|Viajes<br>PM2|%|Viajes<br>FP|%|Viajes<br>PT|%|
|---|---|---|---|---|---|---|---|---|---|
|1|**Caminata**|184.846|13,9%|189.064|20,0%|144.076|25,0%|213.021|20,8%|
|2|**Autochofer**|336.504|25,3%|243.227|25,8%|142.647|24,7%|254.345|24,8%|
|3|**Autoacompañante**|178.975|13,5%|68.490|7,3%|24.593|4,3%|61.899|6,0%|
|4|**Taxi**|15.466|1,2%|17.526|1,9%|15.882|2,8%|19.593|1,9%|
|5|**Bus (Transantiago)**|308.310|23,2%|180.229|19,1%|113.555|19,7%|191.596|18,7%|
|6|**Taxicolectivo**|22.773|1,7%|23.006|2,4%|33.956|5,9%|26.269|2,6%|
|7|**Metro y Tren**|69.003|5,2%|68.092|7,2%|46.357|8,0%|88.198|8,6%|
|8|**Bus-Metro**|158.310|11,9%|102.958|10,9%|37.740|6,5%|112.275|10,9%|
|9|**Taxicolectivo-Metro**|10.631|0,8%|7.758|0,8%|5.670|1,0%|6.165|0,6%|
|12|**Bicicleta**|44.878|3,4%|44.059|4,7%|12.668|2,2%|52.366|5,1%|
||**Total**|**1.329.695**|**100,0%**|**944.409**|**100,0%**|**577.144**|**100,0%**|**1.025.727**|**100,0%**|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 10 C ALIBRACIÓN DE LOS M ODELOS DE A SIGNACIÓN (T AREA 10)

42

Esta tarea debe abordar la calibración de las redes utilizadas por los modelos de

asignación de viajes para los distintos períodos analizados en el contexto de este Estudio (punta

mañana, fuera de punta y punta tarde). De acuerdo a lo definido en las Bases Técnicas, nos

referiremos a continuación a las siguientes actividades: **construcción de las redes,**

**calibración de las redes y validación de las redes calibradas** .

**10.1** **Construcción de Redes de Transporte (Sub Tarea 10-1)**

En esta sección se detalla el proceso de construcción de las redes de transporte

asociadas al Modelo ESTRAUS, según las definiciones presentadas en las secciones anteriores.

De acuerdo a dichas definiciones, las redes construidas deben permitir modelar los modos

relevantes, considerando aquellos puros y sus combinaciones posibles. No obstante, previo a

la construcción de las distintas redes de transporte, es necesario definir cuáles son y a qué modos

representan.

Los modos puros, que deben presentar una red propia y diferente al resto, son los

siguientes:

**a)** **Autochofer:** la red del modo Autochofer corresponde a la **red vial**

**estratégica**, cuyos arcos representan las calles o ejes donde circulan los vehículos

y los nodos las intersecciones o cruces de dichas calles o ejes. Sobre esta red se

reparten o asignan también los viajeros de los modos **Autoacompañante** y

**Taxi** . Las características topológicas de esta red, como longitud de los arcos y su

capacidad, se obtiene de las características físicas de diseño de las respectivas

calles y ejes viales que representan. Estas características están asociadas al número

de pistas disponibles, presencia de intersecciones semaforizadas o priorizadas, etc.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

43

Debe notarse que una particularidad importante de la red vial, donde se reparten

o asignan los usuarios de transporte privado en general (modos Autochofer,

Autoacompañante y Taxi) es que el tiempo de viaje depende del flujo vehicular en

ellas, lo que permite representar de manera adecuada el efecto de la congestión.

La forma en que varía el tiempo de viaje en un arco en función de su flujo depende

de las características físicas y operativas del arco. El flujo puede corresponder tanto

a flujo de Automóviles como Taxis y servicios de superficie en general (Bus y

Taxicolectivo). Como se verá más adelante, la relación entre tiempo de viaje y flujo

en un arco corresponde a **funciones de tipo BPR** .

**b)** **Caminata y bicicleta:** estos viajes se reparten en una red construida

directamente a partir de la red vial, con la misma cobertura espacial de arcos y

nodos. No obstante, estas redes tienen la diferencia de no experimentar congestión

en sus arcos en función del flujo (tiempos de viaje constante). Además, todos los

arcos son considerados bi-direccionales.

**c)** **Bus:** la red donde se asignan los viajeros del modo Bus se construye a partir de los

trazados de los distintos servicios de buses que operan en el área de análisis, en

este caso Santiago. A partir de los recorridos, se construyen arcos virtuales

denominadas secciones de ruta cuyas características operativas dependen de

aspectos como la frecuencia, capacidad y velocidad comercial de los buses en los

distintos tramos del recorrido. Es decir, dichas características operativas de los

buses, además de sus trazados, definen la topología de la red donde se repartirán

los usuarios de Bus para realizar sus viajes. Una particularidad que presenta la

modelación de la red de buses dentro de ESTRAUS, en especial como parte del

sub-modelo de asignación ARTP, es que considera el tiempo de espera en paradero

variable en función de la demanda de viajeros sobre los distintos servicios. Es decir,

considera el hecho que si llegan buses con mayores tasas de ocupación, es más

probable que algunos usuarios deban esperar al bus siguiente para realizar su

viaje. Luego, el tiempo de espera en paradero de los usuarios del modo Bus no

depende sólo de la frecuencia de los servicios que le sirven al usuario para realizar

su viaje, sino que además dependerá de cuán ocupados vengan los buses. Además,

la red de buses debe ser absolutamente consistente con la red vial estratégica, en

el sentido de que los trazados de buses deben ser definidos en arcos y nodos que

existan en ella.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

44

Es importante destacar que en la presente calibración el modo bus corresponde

exclusivamente al **BusT** (bus Transantiago).

**d)** **Taxicolectivo:** la red de Taxicolectivo se construye de manera análoga a la red

de buses definida en el párrafo anterior, por lo que además presenta las mismas

propiedades en términos de congestión en paraderos (tiempos de espera) y debe

presentar consistencia con la red vial estratégica.

**e)** **Metro:** la red de Metro, que incluye el tren, se construye de manera análoga a la

red de buses y Taxicolectivos definidas anteriormente, por lo que presenta las

mismas propiedades en términos de congestión en paraderos (tiempos de espera).

No obstante, la cobertura de la red de Metro es significativamente inferior a la

cobertura de las redes de Bus y Taxicolectivo, ya que las Líneas de Metro operan

sobre algunos determinados ejes estratégicos de la ciudad, en mucha menor

medida que las Líneas de Bus y Taxicolectivo. Esto implica también que no debe

necesariamente existir consistencia entre los trazados de la red de Metro y la red

vial estratégica; no obstante, los nodos que representan las estaciones de subida y

bajada de pasajeros de la red de Metro deben pertenecer a la red vial estratégica.

Para efectos de modelación, la red de Metro considera, en la presente

recalibración del Modelo ESTRAUS, el tramo urbano del servicio de Metro-Tren

entre Santiago y Rancagua, además de todas las líneas en operación al año de

calibración de las redes (2012).

**f)** **Modos Combinados** : ESTRAUS permite modelar, además de los modos puros

definidos en los puntos anteriores, viajes que son realizados en combinaciones de

dichos modos. **Las redes donde se asignan estos viajes combinados**

**corresponden simplemente a la superposición de las redes de los**

**modos puros que los conforman** . Por ejemplo, los viajes que realizan la

combinación BusT-Metro (o Metro-BusT) serán asignados a una red conformada

tanto por la red de Metro como por la red de Bus Transantiago; algo análogo

ocurre por ejemplo con los viajes en Taxicolectivo-Metro.

Sin embargo, es importante hacer notar que no todas las combinaciones de modos

son factibles de modelar con ESTRAUS, sino sólo algunas que consideran al modo

Metro como parte del viaje realizado. Las redes para modos combinados son por

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

45

lo tanto en nuestro caso las siguientes: **Bus Transantiago-Metro y**

**Taxicolectivo-Metro.**

La red vial estratégica, a partir de la cual se tipifican y construyen el resto de las

redes de los distintos modos de transporte considerados en la modelación ESTRAUS, está

representada por los ejes viales e intersecciones de calles donde circulan todos los modos de

transporte de superficie, principalmente Automóviles, Buses, Taxicolectivos y Taxis en general.

También en esta red se modelan los flujos de camiones. Por otra parte, los viajes en Caminata

y Bicicleta se asignan a una red con costos fijos cuya cobertura espacial está determinada por

la red vial estratégica. Dichos costos están definidos por la velocidad de desplazamiento de

aquellos modos, las cuales se fijaron en 3,6 km/h [2] para la Caminata y 13,1 km/h [3] para la

Bicicleta.

**10.1.1** **Red Vial Estratégica EOD 2012**

La codificación de la red vial estratégica se realizó a partir del catastro vial de la

EOD 2012 y la red ESTRAUS SECTRA 2012 (en términos globales de la red). La información

detallada de la red se catastró principalmente a partir de fotografías satelitales de Google Earth

y la funcionalidad Street View de la misma aplicación.

En la figura a continuación se puede apreciar la red vial resultante (Red EOD

2012).

2 Valor que representa 1 m/s, usado tradicionalmente en simulaciones estratégicas como ESTRAUS.

3 Valor determinado por la Dirección General de Medio Ambiente de la Comisión Europea, en “En bici, hacia

ciudades sin malos humos”. No se encontró velocidades de desplazamiento estudiadas en Chile, pero se
considera apropiada al encontrarse entre las cotas de 7,5 km/h en intersecciones (Understanding cyclist traffic
behaviour: contrasting cycle-path designs in Santiago de Chile, Waintrub et al., 2015) y 20 km/h de velocidad
en tramos (Uso de la bicicleta en ciudades intermedias de Chile central, San Martín, P., 2013).

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 10-1 Catastro Vial EOD 2012 y Red ESTRAUS EOD 2012**

Fuente: Elaboración propia.

46

**10.1.2** **Corredores de Buses, Vías Exclusivas, Pistas Solo Bus y Vías**

**Reversibles**

La codificación de la red vial estratégica y posterior proceso de calibración

consideró las particularidades que estuvieron operativas durante el año 2012, correspondientes

a dos tipos principales: infraestructura dedicada para transporte público de superficie y vías

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

47

reversibles. El primer tipo se descompone en tres categorías: Corredores de Buses, Vías

Exclusivas y Pistas Solo Bus.

En la figura a continuación se puede apreciar la infraestructura dedicada de

transporte público, en verde los corredores de buses, en violeta las vías exclusivas y en naranja

las pistas solo bus. Posteriormente se pueden apreciar figuras con la ubicación de las Estaciones

Intermodales y los Terminales de Buses, así como las Vías Reversibles que operan en punta

mañana.

**Ilustración 10-2 Infraestructura dedicada al Transporte Público en Superficie**

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 10-3 Estaciones Intermodales y Terminales de Buses**

Fuente: Elaboración propia.

48

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 10-4 Vías Reversibles que operan en Punta Mañana**

Fuente: Elaboración propia.

49

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**10.1.3** **Atributos de la Red Vial**

50

La categorización de los arcos de la nueva red necesarios se realizó utilizando

como referencia cinco categorías, las se describen en la siguiente tabla.

**Tabla 10-1 Descripción de Categorías**

|Col1|Categoría|
|---|---|
|Autopistas urbanas e interurbanas|**1 **|
|Vialidad interurbana|**2 **|
|Vialidad urbana con transporte público mayor|**3 **|
|Vialidad urbana sin transporte público mayor|**4 **|
|Caleteras, accesos, salidas, enlaces y peajes tradicionales de autopistas urbanas e interurbanas.|**5 **|

Fuente: Elaboración propia.

De acuerdo a las categorías anteriores y al tipo de señalización existente en el arco

se definió la capacidad base y sus correspondientes factores de reducción. En la siguiente tabla

se presenta la capacidad base por pista y las capacidades reducidas para cada categoría.

**Tabla 10-2 Capacidad por Pista según Categoría**

|Categoría|Capacidad por pista (veh. equivalentes/h)|Col3|Col4|
|---|---|---|---|
|**Categoría**|**Base**|**Disco Pare**|**Ceda el Paso**|
|1|2.050|-|-|
|2|1.800|1.170|1.260|
|3|1.350|810|878|
|4|1.600|960|1.040|
|5|1.800|1.080|1.170|

Fuente: Elaboración propia.

En el caso de los semáforos, las capacidades se ven afectadas según la proporción

de verde del ciclo de la intersección en particular. A falta de una información más detallada, se

miró cada intersección con Street View. Con ello, se decidió si correspondía una disco pare,

ceda el paso o semáforo, y en este último caso se identificó el número de turnos. El número de

turnos del ciclo semafórico se utiliza para dividir la capacidad de los arcos que llegan a la

intersección.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

51

Si el arco modelado no fue catastrado, entonces se le asignó la capacidad de la

antigua red modelada.

Para el caso particular de los peajes, se definieron capacidades menores: 200

vehículos equivalentes por cada caseta en el caso de los peajes tradicionales (se suma por

número de casetas para el arco correspondiente), y 1400 vehículos equivalentes por cada pista

en el caso de los tele-peajes (stop & go). La capacidad de los pórticos de peaje (TAG o free

flow) es la misma que tendría un arco equivalente sin peaje, ya que no supone una limitación

para el libre desplazamiento; es decir, 2050 vehículos equivalentes por pista (categoría 1).

Para el cálculo de la velocidad a flujo libre se cuenta con la siguiente información:

a) Tiempo flujo libre observado para los arcos de la red ESTRAUS SECTRA

2012, los que se homologaron a la red ESTRAUS EOD 2012.

b) Catastro de la red vial de Santiago.

Las velocidades de cada arco a flujo libre consideradas fueron las máximas

permitidas en cada caso particular, verificando con Street View para la fecha. Cuando NO se

encontró una velocidad máxima explícita, el criterio fue usar las normas generales de velocidad

máxima: 120 km/h para autopistas interurbanas; 80 km/h para autopistas urbanas; 100 km/h

para vialidad interurbana; 60 km/h para vialidad urbana (con o sin transporte público),

caleteras, accesos, salidas y enlaces de autopistas urbanas e interurbanas; y 50 km/h para

peajes tradicionales y tele-peajes. Cabe destacar que, debido a que se está usando el tiempo

de flujo libre como variable, y que este solo puede ingresar como número entero de segundos,

existen perdidas de precisión, lo que origina mayor variabilidad en las velocidades.

Con ese proceso terminado, se introdujeron los virajes prohibidos en los ejes más

importantes de la ciudad, entre los que se incluyen todas las autopistas y sus caleteras, así como

el eje Pajaritos-Alameda-Providencia-Apoquindo-Las Condes, entre otros.

**10.1.4** **Red de Buses Transantiago**

La red de buses de Santiago está conformada por la totalidad de servicios de Buses

licitados que operaban en el año de la Encuesta Origen-Destino en la Capital. La información

utilizada para la modelación de la red de Bus Transantiago se obtuvo a partir del Plan

Operacional de Directorio de Transporte Público Metropolitano (DTPM), para el segundo

semestre del año 2012.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

52

En la Figura siguiente se presenta la red modelada de Bus para la ciudad de

Santiago.

**Ilustración 10-5 Red Modelada de Bus Transantiago**

Fuente: Elaboración propia.

Además, la estructura del ID se diseñó para hacer más sencillo el reconocimiento

del servicio analizado. Su diccionario se puede apreciar en el informe de la Tarea 10.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

53

Adicional a los recorridos de Bus Transantiago que llevan pasajeros, también se

codificaron aquellos de categoría No Comercial (no llevan pasajeros).

En la figura siguiente se presenta la red modelada de Bus Transantiago No

Comercial (BTNC) para la ciudad de Santiago.

**Ilustración 10-6 Red Modelada de Bus Transantiago No Comercial, Punta**

**Mañana**

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**10.1.5** **Red de Metro**

54

La red incluye los servicios de Metro operativos a 2012, así como el servicio de

Metro-Tren a Rancagua, en el tramo entre Alameda y Hospital (ubicado en la comuna de Paine).

**Ilustración 10-7 Red Modelada de Metro y Tren**

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

55

Al tener que construir el modo metro como red independiente, se aprovechó la

instancia de renombrar el ID del nodo de las estaciones de metro. Su diccionario se puede

apreciar en el informe de la Tarea 10.

**10.1.6** **Red de Taxicolectivo**

La información utilizada para la modelación de la red de Taxicolectivo se obtuvo a

partir del catastro que fue realizado en el contexto de la Encuesta Origen-Destino. Cabe

destacar que, al igual que sucede con el modo Bus No Transantiago, el catastro no contaba

con información suficiente para todos los recorridos. En total, el catastro contiene 638 líneas

unidireccionales, 361 de las cuales tenían información apropiada, por lo que el resto o puedo

ser codificado.

En la siguiente figura se presenta la red modelada de Taxicolectivo.

**Ilustración 10-8 Red Modelada de Taxicolectivo**

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**10.2** **Calibración y Validación de Redes (Sub Tareas 10-2 y 10-3)**

56

Esta tarea consiste en la calibración de las distintas redes modales para cada uno

de los períodos de modelación definidos. El proceso de calibración considera, básicamente, la

estimación de los valores de los parámetros de las funciones de costo de los arcos que

conforman dichas redes.

Es muy importante señalar que el estado del arte en calibración simultánea de

modelos de equilibrio indica que por el momento no es factible una calibración total simultánea

de un modelo como ESTRAUS. Específicamente, la calibración simultánea puede abordar las

etapas de demanda del modelo (distribución, partición modal y elección de horario). Sin

embargo, la etapa de oferta no se considera en la calibración simultánea (parámetros de la

función BPR de costo generalizado). Debido a esto, la calibración de redes antecede a la

calibración simultánea de modelos de demanda.

**10.2.1** **Construcción de matrices observadas**

Uno de los aspectos centrales del proceso de calibración de redes fue la

construcción de las matrices de viaje observadas que fueron asignadas sobre la red

correspondiente.

Se generaron matrices de viajes para los períodos de modelación definidos, las que

son representativas de la operación del sistema de transporte en el año 2012. Se requirieron

matrices de viajes para los siguientes modos:

 Transporte Privado

 - Bus

 - Metro

 - Taxicolectivo

Para construir estas matrices se consideró principalmente la información disponible

en la EOD 2012 (Encuesta a Hogares, Encuesta de Intercepción en Cordón Externo).

Las matrices elaboradas a partir de la Encuesta a Hogares se construyeron como

la suma de los viajes realizados en día laboral normal expandidos identificados por modo y

periodo. Se excluyeron aquellos viajes en que no fue posible identificar la zona de origen y la

zona de destino, ya que en su lugar había un número de fuera de la zonificación (menor a 1 ó

mayor a 876); así como aquellos intrazonales.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

57

Para el caso de los modos de transporte público, se diferenció a los usuarios entre

adultos y estudiantes, utilizando el propósito de viaje. De esta forma, es posible identificar

específicamente los viajes que pagan tarifa completa de los que pagan tarifa escolar.

En la siguiente figura se exhibe la estructura de la suma de las matrices para todos

los modos en el periodo PM1.

**Ilustración 10-9 Matriz EOD2012 Transporte Privado y Público, PM1**

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**10.2.2** **Matrices de viajes externos**

58

La matriz de viajes externos se construyó exclusivamente a partir de la Encuesta

Origen Destino de viajes realizada en el Cordón Externo, ya que en la Encuesta de Hogares

no se encontraron viajes válidos para las zonas externas. A diferencia de las matrices de viajes

internos, en este caso solo es posible obtenerlas para vehículos livianos y camiones, y no para

todos los modos de viaje. Otra limitación de estas matrices es que la base de datos a partir de

la que se elaboraron no cuenta con información explícita sobre el ingreso de los viajeros, sino

solo categorías de ingreso, lo que implicó no poder realizar un calce perfecto entre las clases

de usuario definidas en la tabla a continuación y aquellas usadas en los viajes internos.

**Tabla 10-3 Categorías de Ingreso por Clase de Usuario**

|Clase de<br>usuario|Categoría de<br>Ingreso|Ingreso (M $)|Col4|
|---|---|---|---|
|Clase de<br>usuario|Categoría de<br>Ingreso|Mínimo|Máximo|
|1|1 y 2|0|200|
|2|3 y 4|201|500|
|3|5|501|1000|
|4|6 y 7|1001|2000|
|5|8 y 9|2001|∞|

Fuente: Elaboración propia.

Existe una categoría de ingreso adicional, la número 10, correspondiente a las

personas que no contestaron. Los viajes respectivos a esa categoría se repartieron entre las 5

clases de usuario de forma de conservar las proporciones de ellas constantes, para no perder

la información.

**10.2.3** **Matrices de viajes fijos**

Además de las matrices de viajes modelables, se construyeron matrices de viajes

fijos para los modos Autochofer, BusTransantiago y Metro, para cada periodo modelado. Estas

corresponden a viajes de la EOD 2012 que, por diversas razones, no pueden incluirse en las

matrices afectas a la partición modal. Sin embargo, es importante que sean parte del proceso

de asignación, ya que son usuarios de dichos modos, cuyos viajes tienen impactos en los niveles

de servicio experimentados por el resto de las personas, tanto por congestión en el transporte

público como por congestión en la red vial.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

59

Debe notarse que con este ejercicio se incluyen casi todos los viajes catastrados

por la EOD 2012, dejando fuera solo una fracción de las combinaciones entre modos, además

del BusNoTransantiago (para el cual no se tiene la información), el Bus Institucional (por

limitaciones que se explican en la sección 10.2.4.1) y los servicios informales. También se dejó

afuera de las matrices de viajes fijos al modo Taxicolectivo, ya que, por problemas de catastro

de la oferta, la red ya presenta excesos de congestión en este modo.

A continuación, se resumen los parámetros de construcción de las matrices. Cabe

destacar que, para los viajes construidos a partir de etapas, siempre se consideró la zona de

origen y de destino de dicha etapa. No obstante, para la selección del periodo del viaje, se

consideró la hora media del viaje completo.

 Autochofer: equivale a la suma de todas las etapas de viajes realizadas en

dicho modo (y no modeladas en ESTRAUS), los viajes o etapas realizados

en Motochofer multiplicados por 0,50, y los viajes o etapas realizados en

furgón escolar multiplicados por 0,07.

 BusTransantiago: todas las etapas de viajes realizadas en el modo

BusTransantiago, en viajes no modelables en ESTRAUS

 Metro: todas las etapas de viajes realizadas en el modo Metro, en viajes

no modelables en ESTRAUS

**10.2.4** **Calibración de la Red de Transporte Privado**

Se entiende por calibración de la red de transporte privado al proceso de

estimación de los valores de los parámetros de la función de costo (denominadas **curvas flujo-**

**tiempo** ) asociada a los distintos tipos de arcos en la red.

La calibración de la red de transporte privado de punta mañana contó con una

base de datos de conteo de flujo para 486 arcos de la red vial utilizada; para fuera de punta,

se contó con 500 conteos y en punta-tarde, con 489.

Estos valores son obtenidos como resultado directo del proceso de optimización

realizado (algoritmo de Hooke&Jeeves).

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

60

**Tabla 10-4 Parámetros BPR por Categoría de Arco Período Punta Mañana**

|CATEGORIA DE ARCO|ALFA|BETA|
|---|---|---|
|1|3,1815|2,9699|
|2|1,4644|7,7367|
|3|2,7469|7,5237|
|4|1,8433|2,5823|
|5|2,5778|2,6839|
|Correlación|0,7440|0,7440|
|Diferencia porcentual ponderada|40,61 %|40,61 %|
|Función objetivo|158.731.720|158.731.720|

Fuente: Elaboración propia.

**Tabla 10-5 Parámetros BPR por Categoría de Arco Periodo Fuera de Punta**

|CATEGORIA DE ARCO|ALFA|BETA|
|---|---|---|
|1|3,3846|4,5689|
|2|1,2323|8,2790|
|3|4,9618|5,8730|
|4|3,3410|2,1570|
|5|1,0356|2,6085|
|Correlación|0,5248|0,5248|
|Diferencia porcentual ponderada|49,90 %|49,90 %|
|Función objetivo|191.880.800|191.880.800|

Fuente: Elaboración propia.

**Tabla 10-6 Parámetros BPR por Categoría de Arco Periodo Punta Tarde**

|CATEGORIA DE ARCO|ALFA|BETA|
|---|---|---|
|1|0,4699|3,2214|
|2|0,4300|6,7092|
|3|1,7720|7,6440|
|4|1,5715|2,9573|
|5|1,2231|2,8073|
|Correlación|0,57|0,57|
|Diferencia porcentual ponderada|41,00 %|41,00 %|
|Función objetivo|256.728.230|256.728.230|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**10.2.5** **Calibración de Redes de Transporte Público**

61

El proceso de calibración de las redes de transporte público es análogo al de la

red de transporte privado y consiste en estimar los valores de los parámetros de la función de

costo generalizado de viajes, asociados a los arcos de dichas redes. La particularidad en este

caso es que la red de transporte público, aunque conceptualmente no difiere de la de transporte

privado, en la práctica es más compleja.

Los ponderadores obtenidos se detallan en las tablas siguientes

(parámetros/ponderadores pwait, pwalk y vtime). Se incluyen también aquellos ponderadores

resultantes del estudio de calibración de ESTRAUS con la información de la EOD 2012 y del

estudio de calibración del sistema de transporte público (“Análisis Modernización de Transporte

Público, V Etapa”), ya que también fueron probados en la red codificada para la EOD2012, y

usados como punto de partida del algoritmo de calibración (de las corridas 24 a 34 en el

primer caso, y en las demás corridas el segundo).

El valor de R_Corr para cada conjunto de ponderadores estimado, corresponde al

coeficiente de correlación entre flujos observados y modelados; se indica también el valor de

la función objetivo a minimizar: suma de diferencias al cuadrado entre los flujos modelados en

arcos de transporte público (secciones de ruta), y los flujos observados (conteos).

Notar que se calibró también un valor para el parámetro pxfer, que pondera el

número total de secciones de ruta (etapas). Las corridas denominadas *P* tienen un valor inicial

de 10.0 para este parámetro, en tanto las demás parten con un valor 0.0 para pxfer.

**Tabla 10-7 Ponderadores de Tiempo por Modo**

|BUST|V Etapa|EOD2001|corrida 24|corrida 31|corrida 32|corrida 33|702-N|702-P|702-N2|702-P2|
|---|---|---|---|---|---|---|---|---|---|---|
|pwait|1,93|1,93|2,59|1,74|2,49|2,49|1,91|2,04|3,35|2,29|
|pwalk|3,63|3,63|3,99|4,62|4,27|6,99|3,27|3,46|4,08|3,73|
|vtime|3,62|3,62|3,62|3,62|3,62|3,62|3,62|3,62|2,76|3,26|
|pxfer|0,00|0,00|0,00|0,00|0,00|0,00|0,00|10,00|0,00|9,89|
|R<br>R_Corr|||0,5914|0,8121|0,6007|0,6275|0,5996|0,6247|0,5996|0,6592|
|FO(mill)<br>|||2.221,03|5.873,05|2.220,20|2.220,20|2.211,48|2.211,48|2.211,48|2.211,43|

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

62

|TXC|V Etapa|EOD2001|702-N|702-P|702-N2|702-P2|
|---|---|---|---|---|---|---|
|pwait|1,93|1,93|1,91|1,93|2,12|1,93|
|pwalk|3,63|3,63|3,63|3,46|3,27|3,63|
|vtime|3,62|3,62|3,62|3,62|3,62|3,62|
|pxfer|0,00|0,00|0,00|10,00|0,00|10,00|
|R<br>R_Corr|||0,5567|0,5833|0,1007||
|FO(mill)|||9,58|9,58|9,58||

|METBUST<br>pwait<br>pwalk|V Etapa<br>1,93<br>3,63|EOD2001<br>1,93<br>3,63|702-N<br>2,66<br>0,49|702-P<br>3,78<br>0,32|702-N2<br>3,45<br>2,27|702-P2<br>3,55<br>0,55|
|---|---|---|---|---|---|---|
|vtime<br>pxfer<br>R<br>R_Corr|3,62<br>0,00|3,62<br>0,00|13,88<br>0,00<br>0,8956|18,9<br>3,04<br>0,9142|9,05<br>0,00<br>0,9504|10,47<br>1,06<br>0,9482|
|FO(mill)|||57.867,82|57.867,78|57.867,32|57.867,30|

|METTXC<br>pwait|V Etapa<br>1,93|EOD2001<br>1,93|702-N<br>1,93|702-P<br>2,01|702-N2<br>2,12|702-P2<br>1,93|
|---|---|---|---|---|---|---|
|pwalk<br>vtime|3,63<br>3,62|3,63<br>3,62|3,63<br>3,46|3,63<br>3,62|3,63<br>4,34|3,33<br>3,62|
|pxfer<br>R<br>~~R_Corr~~|0,00|0,00|0,00<br>0,3991|10,81<br>0,3628|0,00<br>0,7577|10,00<br>0,7757|
|FO(mill)|||55.666,54|55.666,54|55.666,29|55.666,30|

Fuente: Elaboración propia.

De las tablas anteriores se puede observar que los mejores ajustes por modo se

obtienen de las siguientes corridas de Hooke&Jeeves:

1) Para busT, la corrida 702-P2 (en que se calibró este modo considerando la

suma de las matrices de busT y metbusT).

2) Para txc, la corrida 702-P (en que se calibró este modo considerando sólo flujos

de txc puro).

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

63

3) Para metro, la corrida 702-P (en que se calibró este modo considerando la

suma de las matrices de metro, metbusT, metbusN, mettxc).

4) Para metbusT, la corrida 702-N2 (en que se calibró este modo considerando

la suma de las matrices de metbusT, metro, busT).

5) Para mettxc, la corrida 702-P2 (en que se calibró este modo considerando la

suma de las matrices mettxc, metro, txc).

Considerando los mejores parámetros antes presentados y también aquellos

obtenidos de estudios de calibración anterior, se realizaron múltiples corridas de asignación de

equilibrio. Sin embargo, nuevamente se presentó el problema de que la modelación no estaba

captando las interacciones entre modos puros y combinados al usar el programa de asignación

de equilibrio **artp3_rc** (que asigna un único modo a la vez, ya sea puro o combinado). Para

solucionar esta dificultad, se modificó la implementación del programa ESTRAUS, agregando

un nuevo parámetro de ejecución llamado solo_asignacion, que permite ejecutar el modelo

considerando demanda fija, mediante la lectura de matrices de viaje conocidas a priori para

cada modo de transporte (el detalle de la modificación realizada se reporta como parte del

estudio “Programa de Mantención Modelos Estratégicos de Transporte Urbano”).

**10.2.6** **Definición de relación velocidad transporte privado / velocidad**

**transporte público**

La versión actual del modelo ESTRAUS considera como una opción que el tiempo

de viaje en bus en un determinado arco de flujo compartido con los autos es igual al tiempo de

equilibrio de los automóviles en dicho arco multiplicado por una constante mayor que uno,

entregada exógenamente al modelo. Para cada categoría de arco, se han calibrado valores

para dicha constante.

Los valores de estas razones fijas, que fueron actualizados a partir de información

de la EOD-2001, se definen en el archivo **categorías_modo_tt.dat** y se presentan en la

siguiente tabla para las 5 categorías de arco consideradas (se consideraron iguales para punta

mañana y fuera de punta).

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 10-8 Valores Relación Fija Entre Tiempo de Viaje en Bus y en Auto**

|CATEGORÍA DE ARCO|VEL BUS / VEL AUTO|
|---|---|
|1|1,3000|
|2|1,5545|
|3|1,1068|
|4|1,4210|
|5|1,4222|

Fuente: Elaboración propia.

64

En caso de construir curvas que no representen relaciones constates entre las
velocidades, se calibraron los valores de los parámetros  y  para las distintas categorías de

arcos consideradas en ESTRAUS. En la tabla siguiente se muestran los valores finales de los

parámetros calibrados, actualizados a la categorización de arcos usada en esta calibración

del modelo.

**Tabla 10-9 Parámetros** _**φ**_ **y** _**ε**_ **finales**

|Col1|φ|ε|
|---|---|---|
|CATEGORÍA 1|0.40|0.66|
|CATEGORÍA 2|0.58|0.66|
|CATEGORÍA 3|0.53|0.66|
|CATEGORÍA 4|0.40|0.66|
|CATEGORÍA 5|0.24|0.66|

Fuente: Elaboración propia.

Para el caso de los **taxis colectivos**, dado que su comportamiento se puede

asemejar al de los automóviles, se consideró que las velocidades de operación para este modo

son las mismas que para los autos. En efecto, generalmente los taxis colectivos inician sus viajes

completos desde los paraderos y no presentan un régimen de paradas para recoger/dejar

pasajeros como el caso de los buses.

Respecto de los **corredores exclusivos de buses**, en el contexto del Estudio

“Análisis Modernización de Transporte Público, V Etapa”, encargado por SECTRA, se

calibraron funciones flujo-velocidad para los buses, en distintos tipos de corredores.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

65

A través de simulaciones con Aimsun se determinaron los mejores valores de los

parámetros  y  para cada uno de los tipos de corredor detallados antes, los que se muestran

en la siguiente tabla.

**Tabla 10-10 Parámetros** _**α**_ **y** _**β**_ **calibrados**

|Tipo de corredor|||
|---|---|---|
|1 (cap=471)|9.35|0.15|
|2 (cap=485)|10.25|0.14|
|3 (cap=149)|10.20|0.16|
|4 (cap=205)|6.99|0.16|

Fuente: Elaboración propia.

Estos valores corresponden a la mejor información hasta ahora disponible, por lo

que se propuso usarlos en la nueva calibración de ESTRAUS.

**10.2.7** **Tratamiento del transporte de carga**

En ESTRAUS el transporte de vehículos de carga puede modelarse mediante la

asignación de una matriz de viajes (flujo fijo) en los arcos de la red vial, más específicamente a

una sub-red de ésta, en que el modelador pre-define los arcos por los que pueden circular estos

camiones. Sobre esta subred, se realiza una asignación de equilibrio de Wardrop: en la fase I

del algoritmo de Evans que se ejecuta en cada iteración de Diagonalización, se calculan las

rutas mínimas sobre esta subred (usando costos generalizados medios), y luego la matriz de

viajes fija de camiones (provista exógenamente por el modelador), se asigna sobre estas rutas

mínimas. De esta forma, los viajes de camión asignados influyen a su vez (a la iteración

siguiente), en los costos de viaje entre el par OD sobre el que se cargaron. Notar que, en caso

de existir tarifas sobre los arcos, se usan los ponderadores de tarifa correspondientes a la clase

de usuario que defina el modelador para el chofer de camión. Esta forma de modelar el

transporte de carga, es alternativa a aquella mencionada antes, en que los camiones se tratan

como servicios con itinerario y frecuencia fija.

Dentro de la información disponible para esta calibración de redes, se cuenta con

matrices de viajes de camiones entregadas por Sectra para el corte temporal 2012. En el caso

de la punta mañana, dichas matrices no corresponden exactamente al horario de modelación

considerado en este proceso de calibración, sino que al periodo 7:30 a 8:30 (cabe recordar

que el periodo considerado para la punta mañana en este estudio es de 7 a 8 para el primer

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

66

sub-periodo, y 8 a 9 para el segundo); para la fuera punta, la matriz recibida corresponde al

horario 10 a 12 (siendo 10 a 11 el periodo definido en esta calibración), y para la punta tarde

no hay matriz. Sin embargo, de todos modos, estas matrices sirven para tener una aproximación

no exacta al problema.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 11 A NÁLISIS DE LOS M ODELOS DE D EMANDA DE ESTRAUS (T AREA 11)

**11.1** **Generación de Viajes**

67

Se debe calibrar un modelo estratégico que permita predecir adecuadamente

comportamientos futuros (típicamente a 10 y 20 años), en base a la construcción de un

escenario de transporte y uso de suelos, a partir del cual se estiman generaciones y atracciones

de viaje. Este paso de la metodología de planificación en la que se enmarca ESTRAUS **es**

**claramente la más incierta de todas las etapas de la metodología utilizada** .

**Discutiendo con la contraparte en la etapa de Ajuste Metodológico**

**las ventajas y compromisos del uso de tasas (ACM) y regresiones (RLM), se llegó**

**a la conclusión de que las dificultades que implican en la práctica proyectar las**

**variables explicativas necesarias para formular modelos de RLM, hacen**

**recomendable concentrarse en la calibración de tasas** .

Luego, el problema se reduce a encontrar las tasas de generación de viajes para

cada categoría de hogar y propósito, y éste es precisamente el objetivo del modelo ACM, para

lo cual se ha demostrado teórica y prácticamente muy útil.

**Sin embargo, la generación de viajes no originados en el hogar, así**

**como las atracciones de viajes**, fueron modeladas con los tradicionales modelos de

regresión lineal múltiple (RLM). Esto porque no obstante las limitaciones de este tipo de modelos,

hasta ahora son la única herramienta de análisis disponible en la práctica para los fenómenos

que aquí interesan y así se reconoce en la metodología propuesta para el estudio.

**11.2** **Modelos de Demanda (Distribución, Partición Modal y Elección**

**Horaria)**

La **estrategia de calibración**, propuesta para el presente estudio comienza

calibrando los modelos en forma aislada, hasta obtener una especificación suficientemente

buena. Luego, usando como base estos modelos, se realizó la calibración simultánea de los

modelos de partición modal-elección de horario de viaje y posteriormente la calibración

simultánea de distribución, partición modal, elección de horario. En la calibración aislada del

modelo de partición modal se puede incluir un nivel adicional de elección de horario en la

formulación jerárquica de ESTRAUS, lo que permite calibrar en forma conjunta con métodos

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

68

tradicionales (MNL, HL, estimados en ALOGIT, BIOGEME u otro software), la elección de modo

y la elección de horario.

Un aspecto importante a considerar en el proceso de calibración, es la definición

de las formas funcionales a utilizar en los sub-modelos considerados. Al respecto es fundamental

**considerar las restricciones impuestas por la formulación simultánea de**

**ESTRAUS** . Dicha formulación utiliza una estructura jerárquica de los modelos de demanda, en

la que en cada uno de sus niveles se utilizan funciones de utilidad con expresiones lineales en

los parámetros. Por lo tanto, expresiones no lineales de las funciones utilidad (ej. transformadas

Box-Cox) son inconsistentes con la formulación simultánea de ESTRAUS (ver demostración en

desarrollo matemático incluido en la Tarea 1: Ajuste Metodológico).

Por otra parte, existen desarrollos recientes que pueden mejorar la formulación y

modelación de la Distribución de viajes (Referencias 08 y 09). Durante los últimos años se han

introducido en ESTRAUS generalizaciones en el tratamiento de la etapa de Distribución de

viajes, que son consideradas en la calibración de los modelos que se realizó en el presente

estudio: i. La introducción de **modelos DCM** (Distribution Consolidated Models) y ii. la

incorporación de **modelos simplemente acotados a orígenes** [4] . Ambos fueron incluidos

en el proceso de calibración, tanto secuencial como simultáneo.

Es importante destacar que **estas generalizaciones del modelo de**

**distribución son perfectamente compatibles con la formulación de equilibrio**

**simultáneo oferta-demanda de ESTRAUS,** como se demuestra en la deducción de las

condiciones de optimalidad de su versión general (ver detalle Tarea 1).

Otro tema importante en la calibración de modelos de Distribución es la

determinación del nivel de agregación de zonas a utilizar. En estudios anteriores (Referencia

22) se ha visto que una desagregación a nivel zonal (casi 700 zonas en la implementación

actual para Santiago), puede resultar en la obtención de parámetros de distribución no

significativos. Dado este problema, en el estudio de calibración del 2006 (Referencia 22), se

calibró el mismo modelo de demanda, pero considerando la elección de origen y destino

agregado a nivel comunal, lo que corrigió el problema de estimación obteniéndose parámetros

significativos.

4 Ambas generalizaciones fueron presentadas en un punto anterior de esta sección de Metodología General.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

69

Sin embargo, esta agregación crea un problema de precisión para la definición de

los costos O-D percibidos por los usuarios, ya que, al considerar una agregación a nivel

comunal, el costo de viajar entre un par (i, j) es diferente al costo considerado a nivel zonal;

este aspecto es relevante para obtener los factores de balanceo A i y B j por lo que en el estudio

anterior se consideró el costo compuesto promedio ponderado entre cada par de comunas.

**Posteriormente se usó a nivel zonal el modelo calibrado a nivel comunal,**

obteniéndose buenos resultados en los análisis de validación.

El grado de agregación de los modelos de distribución está también relacionado

con la existencia de ceros en la matriz de distribución. Cuando la desagregación es a nivel

zonal, la gran mayoría de las casillas de la matriz observada tienen valor cero, lo que crea un

problema al predecir las distribuciones de viajes usando un modelo continuo (Modelo

gravitacional). Debido a dicho problema en el pasado se han diseñado enfoques especiales

que consideran el concepto de **“estructura” de la matriz**, a través del cual se definen

celdas con valor cero que no son consideradas en el proceso de calibración.

El problema de agregación de zonas a considerar en la calibración de los modelos

es un problema de orden práctico, que debió ser analizado y resuelto como parte del mismo

proceso de calibración. Para ello, **se consideraron distintos niveles de agregación**

**para comparar los resultados obtenidos en términos de los valores de los**

**parámetros calibrados** [5] **y su grado de significancia estadística** . La solución

adoptada fue acordada en conjunto con la contraparte, ya que este enfoque puede incrementar

significativamente el trabajo de estimación de parámetros.

Con la información resultante de la calibración de los modelos de demanda,

particularmente la estimación de los parámetros de la función de costo generalizado de los

distintos modos de transporte, es factible obtener un estimador del valor subjetivo del tiempo

para las diferentes categorías de viajeros. La obtención de valores del tiempo razonables, en

términos de proporción del ingreso de los individuos, puede ser también un criterio de selección

entre modelos alternativos cuyos indicadores de ajuste estadístico sea similar.

5 Considerando las magnitudes relativas y los signos de los parámetros obtenidas en los distintos casos analizados.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

70

# 12 C ALIBRACIÓN DE M ODELOS DE G ENERACIÓN Y A TRACCIÓN (T AREA 12)

En esta tarea se presentan los modelos de generación y atracción de viajes

estimados a partir de la información disponible. Los viajes pueden clasificarse en tres categorías

según su relación con el hogar de los individuos que los realizan:

i. viajes basados en el hogar de ida ( **bhi** ),

ii. viajes basados en el hogar de retorno ( **bhr** ), y

iii. viajes no basados en el hogar ( **nbh** ).

Los viajes bhi son aquellos cuyo origen es el hogar, los viajes bhr son aquellos cuyo

destino es el hogar, y los viajes nbh son aquellos cuyo origen y destino no es el hogar. Esta

clasificación es útil en la medida que la motivación para realizar cada uno de estos viajes es

distinta, y por tanto es recomendable utilizar modelos distintos para predecir la cantidad

realizada de viajes de cada tipo.

El propósito de viaje es otro aspecto de suma relevancia en la caracterización de

todo viaje. Así, por ejemplo, la cantidad de viajes con motivo trabajo que realiza un individuo

se explica por factores muy distintos a la cantidad de viajes con motivo compras que realiza el

mismo individuo. Por ello, también es importante considerar en la modelación el propósito del

viaje.

La siguiente tabla presenta un resumen de los modelos a estimar. Cada casillero

representa un modelo independiente. ACM indica un conjunto de tasas diferenciadas por

categoría de usuario y RLM indica un modelo de regresión lineal múltiple. Los viajes bhr y nbh

son agrupados en el caso de la generación, al igual que los viajes bhi y nbh en el caso de la

atracción.

**Tabla 12-1 Resumen de modelos de generación y atracción de viajes**

|Col1|Col2|Punta Mañana|Col4|Col5|Col6|Fuera de Punta|Col8|Col9|Col10|Punta Tarde|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|<br>|<br>|**TRA**|**EST1**|**EST2**|**OTR**|**TRA**|**EST**|**COMP**|**OTR**|**T+E**|**COMP**|**OTRO**|
|**Generación**|Basado en hogar de ida (bhi)|ACM|ACM|ACM|ACM|ACM|ACM|ACM|ACM|ACM|ACM|ACM|
|**Generación**|Basado en hogar de retorno (bhr)|RLM|RLM|RLM|RLM|RLM|RLM|RLM|RLM|RLM|RLM|RLM|
|**Generación**|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|
|**Atracción**|Basado en hogar de retorno (bhr)|ACM|ACM|ACM|ACM|ACM|ACM|ACM|ACM|ACM|ACM|ACM|
|**Atracción**|Basado en hogar de ida (bhi)|RLM|RLM|RLM|RLM|RLM|RLM|RLM|RLM|RLM|RLM|RLM|
|**Atracción**|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|No basado en el hogar (nbh)|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

71

A continuación, se presentan los mejores modelos de generación y atracción de

viajes, los cuales se implementaron en ESTRAUS.

**12.1** **Modelos de generación de viajes de ida basados en hogar**

**(generación bhi)**

**12.1.1** **Punta Mañana**

**Tabla 12-2 Modelo de generación de viajes bhi PM, propósito trabajo**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,08472|0,16006|-|0,08472|0,16006|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,34459|0,39692|-|0,34459|0,39692|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,49783|0,52034|0,78513|0,49783|0,52034|0,78513|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,78047|0,86381|1,11753|0,78047|0,86381|1,11753|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|1,09537|0,91902|1,19308|0,96915|0,96915|1,19308|

Fuente: Elaboración propia.

**Tabla 12-3 Modelo de generación de viajes bhi PM, propósito estudio 1**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,13797|0,13389|-|0,13754|0,13754|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,22042|0,33265|-|0,22042|0,27978|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,24477|0,28901|0,64073|0,24477|0,24477|0,48712|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,26481|0,24845|0,44312|0,26481|0,26481|0,26481|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,05362|0,41302|0,54089|0,31085|0,31085|0,54089|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 12-4 Modelo de generación de viajes bhi PM, propósito estudio 2**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,02252|0,11896|-|0,02252|0,05575|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,04493|0,03201|-|0,04493|0,04493|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,05653|0,05281|0,16273|0,06326|0,06326|0,06326|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,04461|0,05341|0,13766|0,06988|0,06988|0,06988|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,18737|0,10994|0,15413|0,13195|0,13195|0,15413|

Fuente: Elaboración propia.

**Tabla 12-5 Modelo de generación de viajes bhi PM, propósito otros**

72

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,09369|0,14221|-|0,08573|0,14221|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,08146|0,15426|-|-|0,15426|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,08447|0,16859|0,35959|0,35959|0,16330|0,32181|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,08578|0,15956|0,31099|0,31099|0,31099|0,31099|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,01716|0,31421|0,35732|0,35732|0,31421|0,35732|

Fuente: Elaboración propia.

**12.1.2** **Fuera de Punta**

**Tabla 12-6 Modelo de generación de viajes bhi FP, propósito trabajo**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,01357|0,09596|-|0,01357|0,05058|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,03680|0,03646|-|0,03294|0,03294|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,02889|0,04863|0,07329|0,07329|0,07329|0,07329|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,07074|0,06635|0,16255|0,09051|0,09051|0,09051|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,24933|0,02923|0,09451|0,09362|0,09362|0,09362|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 12-7 Modelo de generación de viajes bhi FP, propósito estudio**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00891|0,02454|-|0,00891|0,01325|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00944|0,00902|-|0,00944|0,00944|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,01351|0,01422|0,04554|0,01193|0,01422|0,04342|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00956|0,01623|0,04914|0,04914|0,01623|0,01623|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,01636|0,02983|0,03366|0,01636|0,02983|0,02983|

Fuente: Elaboración propia.

**Tabla 12-8 Modelo de generación de viajes bhi FP, propósito compras**

73

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|
|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,06068|0,03699|-|0,05141|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,05396|0,08828|-|-|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,04230|0,06447|0,15104|0,15104|0,09457|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,03701|0,03675|0,08975|0,08975|0,08975|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,08403|0,03560|0,07705|0,07705|0,07705|

Fuente: Elaboración propia.

**Tabla 12-9 Modelo de generación de viajes bhi FP, propósito otros**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,08360|0,10683|-|0,07351|0,08679|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,07657|0,13390|-|-|-|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,06875|0,09029|0,17294|0,17294|0,17294|0,11157|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,06244|0,06567|0,11902|0,11902|0,11902|0,11902|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,03067|0,03477|0,07295|0,07295|0,07295|0,07295|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**12.1.3** **Punta Tarde**

**Tabla 12-10 Modelo de generación de viajes bhi PT, propósito trabajo y**

**estudio**

74

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,01019|0,00359|-|0,01627|0,01939|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,01766|0,02108|-|-|-|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,02174|0,02239|0,02644|0,02644|0,02644|0,02661|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,01630|0,02180|0,02205|0,02205|0,02205|0,02205|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00050|0,03371|0,03371|0,03371|0,03371|

Fuente: Elaboración propia.

**Tabla 12-11 Modelo de generación de viajes bhi PT, propósito compras**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|
|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,02519|0,01160|-|0,02120|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,01807|0,03454|-|-|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,03267|0,01464|0,15932|0,15932|0,07896|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,01811|0,01052|0,03639|0,03639|0,03639|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00114|0,10911|0,10911|0,10911|

Fuente: Elaboración propia.

**Tabla 12-12 Modelo de generación de viajes bhi PT, propósito otros**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,02477|0,02322|-|0,02249|0,03157|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,02042|0,03527|-|-|-|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,02445|0,03703|0,14140|0,14140|0,14140|0,10608|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,02003|0,03041|0,09044|0,09044|0,09044|0,09044|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00845|0,00965|0,11461|0,11461|0,11461|0,11461|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

75

**12.2** **Modelos de generación de viajes basados en hogar retorno y no**

**basado en el hogar (generación bhr + nbh)**

**12.2.1** **Punta Mañana**

**Tabla 12-13 Modelo de generación de viajes bhr+nbh PM, propósito trabajo**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida destinada a servicios|0,0015|5,68|
|Intercepto|1131,9880|4,32|

Fuente: Elaboración propia.

**Tabla 12-14 Modelo de generación de viajes bhr+nbh PM, propósito estudio 1**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Logaritmo natural del ingreso total|29,9306|<br>0,22|
|Intercepto|-348,3436|<br>-0,11|

Fuente: Elaboración propia.

**Tabla 12-15 Modelo de generación de viajes bhr+nbh PM, propósito estudio 2**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida dedicada a industria|0,0001|0,48|
|Intercepto|273,3264|2,16|

Fuente: Elaboración propia.

**Tabla 12-16 Modelo de generación de viajes bhr+nbh PM, propósito otros**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida destinada a educación|0,0099|8,33|
|Superficie construida destinada a otros|0,0017|2,45|
|Intercepto|428,5535|1,25|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**12.2.2** **Fuera de Punta**

76

**Tabla 12-17 Modelo de generación de viajes bhr+nbh FP, propósito trabajo**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida destinada a servicios|0,0012|7,56|
|Intercepto|446,1333|2,77|

Fuente: Elaboración propia.

**Tabla 12-18 Modelo de generación de viajes bhr+nbh FP, propósito estudio**

|Variable<br>Superficie construida destinada a hogares<br>Intercepto|Coeficiente|Test-t<br>1,38<br>0,48|
|---|---|---|
|**Variable**<br>Superficie construida destinada a hogares<br>Intercepto|0,0001|0,0001|
|**Variable**<br>Superficie construida destinada a hogares<br>Intercepto|131,2337|131,2337|

Fuente: Elaboración propia.

**Tabla 12-19 Modelo de generación de viajes bhr+nbh FP, propósito compras**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida destinada a hogares|0,0001|<br>2,06|
|Intercepto|173,4549|<br>0,68|

Fuente: Elaboración propia.

**Tabla 12-20 Modelo de generación de viajes bhr+nbh FP, propósito otros**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida total (excepto hogares)|0,0003|<br>5,00|
|Intercepto|229,9411|<br>1,13|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**12.2.3** **Punta Tarde**

77

**Tabla 12-21 Modelo de generación de viajes bhr+nbh PT, propósito trabajo y**

**estudio**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida destinada a educación|0,0250|5,87|
|Superficie construida destinada a servicios|0,0223|20,77|
|Superficie construida destinada a otros|0,0049|4,28|
|Intercepto|-9,1956|-0,02|

Fuente: Elaboración propia.

**Tabla 12-22 Modelo de generación de viajes bhr+nbh PT, propósito compras**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida destinada a servicios|0,0012|11,83|
|Intercepto|91,9632|0,69|

Fuente: Elaboración propia.

**Tabla 12-23 Modelo de generación de viajes bhr+nbh PT, propósito otros**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida destinada a servicio|0,0015|8,67|
|Intercepto|481,7108|2,45|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

78

**12.3** **Modelos de atracción de viajes basados en el hogar retorno**

**(atracción bhr)**

**12.3.1** **Punta Mañana**

**Tabla 12-24 Modelo de atracción de viajes bhr PM, propósito trabajo**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00039|0,00641|-|0,00485|0,00638|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00467|0,00343|-|-|-|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00614|0,00857|0,00767|0,00767|0,00767|0,00767|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,01046|0,00683|0,01458|0,01458|0,01458|0,01206|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00183|0,00817|0,00817|0,00817|0,00817|

Fuente: Elaboración propia.

**Tabla 12-25 Modelo de atracción de viajes bhr PM, propósito estudio 1**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00028|0,00000|-|0,00025|0,00034|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00021|0,00047|-|-|-|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00133|0,00097|0,00000|0,00057|0,00057|0,00057|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|0,00000|0,00000|0,00000|0,00000|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00358|0,00000|0,00000|0,00000|0,00000|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 12-26 Modelo de atracción de viajes bhr PM, propósito estudio 2**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|-|0,00000|0,00000|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|-|0,00000|0,00000|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|0,00000|0,00000|0,00000|0,00000|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|0,00000|0,00000|0,00000|0,00000|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|0,00000|0,00000|0,00000|0,00000|

Fuente: Elaboración propia.

**Tabla 12-27 Modelo de atracción de viajes bhr PM, propósito otros**

79

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,01978|0,05774|-|0,01978|0,05512|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,03630|0,08356|-|0,03212|0,03212|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,02773|0,05248|0,09327|0,09327|0,09327|0,09327|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,03626|0,03810|0,11567|0,03465|0,03465|0,10318|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00625|0,09308|0,08391|0,08391|0,08391|0,08391|

Fuente: Elaboración propia.

**12.3.2** **Fuera de Punta**

**Tabla 12-28 Modelo de atracción de viajes bhr FP, propósito trabajo**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00077|0,00000|-|0,00077|0,00974|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00210|0,02631|-|0,00210|0,00210|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00735|0,00629|0,00510|0,00546|0,00546|0,02057|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00291|0,00677|0,01565|0,01565|0,01565|0,01565|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00484|0,03499|0,03499|0,03499|0,03499|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 12-29 Modelo de atracción de viajes bhr FP, propósito estudio**

80

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|
|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00025|0,03886|-|0,00025|0,00309|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00098|0,00025|-|0,00095|0,00095|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00158|0,00037|0,00000|0,00000|0,00000|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00040|0,00376|0,00376|0,00376|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,01026|0,00000|0,00000|0,00000|

Fuente: Elaboración propia.

**Tabla 12-30 Modelo de atracción de viajes bhr FP, propósito compras**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|
|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00170|0,00000|-|0,00030|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00038|-|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|0,00000|0,00000|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|0,00000|0,00000|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|0,00000|0,00000|

Fuente: Elaboración propia.

**Tabla 12-31 Modelo de atracción de viajes bhr FP, propósito otros**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|-|0,00000|0,00000|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|-|0,00000|0,00000|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|0,00000|0,00000|0,00000|0,00000|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00020|0,00610|0,00000|0,00018|0,00370|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|0,00000|0,00000|0,00000|0,00000|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**12.3.3** **Punta Tarde**

81

**Tabla 12-32 Modelo de atracción de viajes bhr PT, propósito trabajo y estudio**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,05926|0,11840|-|0,05926|0,11840|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,18096|0,24342|-|0,18096|0,24342|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,23157|0,26723|0,36903|0,23157|0,26723|0,36903|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,35736|0,39375|0,57423|0,35736|0,39375|0,57423|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,65717|0,49803|0,60010|0,54327|0,54327|0,60010|

Fuente: Elaboración propia.

**Tabla 12-33 Modelo de atracción de viajes bhr PT, propósito compras**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|-|0,00000|0,00000|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00105|0,00000|-|0,00050|0,00050|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00034|0,00000|0,00000|0,00000|0,00000|0,00458|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00523|0,00243|0,00572|0,00369|0,00369|0,00369|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00385|0,00485|0,00485|0,00485|0,00485|

Fuente: Elaboración propia.

**Tabla 12-34 Modelo de atracción de viajes bhr PT, propósito otros**

|Col1|Modelo inicial|Col3|Col4|Mejor modelo|Col6|Col7|
|---|---|---|---|---|---|---|
|Ingreso (M$)|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|Número de vehículos|
|Min<br>Max|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|0 <br>1 <br>≥2|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00000|-|0,00000|0,00000|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00062|0,00000|-|0,00047|0,00047|-|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00294|0,00000|0,01721|0,00177|0,00276|0,00276|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,00000|0,00120|0,00454|0,00454|0,00454|0,00454|
|0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞|0,01486|0,00147|0,00358|0,00413|0,00413|0,00413|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

82

**12.4** **Modelos de atracción de viajes basados en el hogar de ida y no**

**basados en el hogar (atracción bhi + nbh)**

**12.4.1** **Punta Mañana**

**Tabla 12-35 Modelo de atracción de viajes bhi+nbh PM, propósito trabajo**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida destinada a servicios|0,0462|33,78|
|Superficie construida destinada a hogares|0,0026|6,52|
|Intercepto|2.023,1410|1,62|

Fuente: Elaboración propia.

**Tabla 12-36 Modelo de atracción de viajes bhi+nbh PM, propósito estudio 1**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Número de matrículas de educación 1|0,2237|6,76|
|Superficie construida destinada a educación|0,0327|8,86|
|Intercepto|497,0596|0,55|

Fuente: Elaboración propia.

**Tabla 12-37 Modelo de atracción de viajes bhi+nbh PM, propósito estudio 2**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Número de matrículas de estudio 2|0,1858|26,71|
|Intercepto|1.082,8780|3,08|

Fuente: Elaboración propia.

**Tabla 12-38 Modelo de atracción de viajes bhi+nbh PM, propósito otros**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida destinada a educación|0,0336|12,33|
|Superficie construida destinada a otros|0,0035|2,17|
|Intercepto|366,7098|0,47|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**12.4.2** **Fuera de Punta**

**Tabla 12-39 Modelo de atracción de viajes bhi+nbh FP, propósito trabajo**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida destinada a educación|0,0071|2,91|
|Superficie construida destinada a servicios|0,0054|9,00|
|Intercepto|-236,1897|-0,70|

Fuente: Elaboración propia.

**Tabla 12-40 Modelo de atracción de viajes bhi+nbh FP, propósito estudio**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Número de matrículas de Estudio 2|0,0437|17,00|
|Intercepto|560,1610|3,57|

Fuente: Elaboración propia.

83

**Tabla 12-41 Modelo de atracción de viajes bhi+nbh FP, propósito compras**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida destinada a comercio|0,0048|9,79|
|Intercepto|1.594,8870|4,91|

Fuente: Elaboración propia.

**Tabla 12-42 Modelo de atracción de viajes bhi+nbh FP, propósito otros**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Número de matrículas de Estudio 1|0,0548|<br>3,23|
|Número de matrículas de Estudio 2|0,0785|<br>2,81|
|Superficie construida destinada a comercio|0,0068|<br>3,03|
|Intercepto|-151,2304|<br>-0,27|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**12.4.3** **Punta Tarde**

84

**Tabla 12-43 Modelo de atracción de viajes bhi+nbh PT, propósito trabajo y**

**estudio**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Número de Matrículas de Estudio 1|0,0169|3,32|
|Número de Matrículas de Estudio 2|0,0980|37,30|
|Intercepto|342,6840|1,83|

Fuente: Elaboración propia.

**Tabla 12-44 Modelo de atracción de viajes bhi+nbh PT, propósito compras**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida destinada a hogares|0,0008|12,19|
|Intercepto|-528,8613|-1,91|

Fuente: Elaboración propia.

**Tabla 12-45 Modelo de atracción de viajes bhi+nbh PT, propósito otros**

|Variable|Coeficiente|Test-t|
|---|---|---|
|Superficie construida destinada a servicios|0,0037|9,81|
|Intercepto|1.292,7820|3,64|

Fuente: Elaboración propia.

**12.5** **Consideraciones al momento de predecir**

Debido a que los modelos RLM se estimaron a nivel comunal, es necesario tener en

cuenta dos consideraciones al momento de utilizarlo a nivel zona. La primera es que los

coeficientes que acompañan a cada una de las variables son insesgados, ya que se utilizaron

mínimos cuadrados para su cálculo, por lo que no se necesita ningún tipo de corrección al

usarlos para predecir con datos que consideren cualquier nivel de agregación.

La segunda es que los interceptos, aunque también se calcularon con mínimos

cuadrados y por tanto son insesgados, están asociados a la escala particular con la que se

estimó el modelo. Por lo tanto, para poder usarlos a nivel de zonas, es necesario normalizarlos

a dicha escala. Ya que las zonas generan y atraen cantidades muy diversas de viajes según los

diferentes propósitos y periodos, lo más apropiado es calcular un intercepto específico para

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

85

cada una de ellas. Para hacerlo, se corrigió el intercepto utilizando un factor igual a la razón

entre los viajes observados para la zona y los viajes observados para la comuna, para cada

propósito y periodo.

Por otro lado, en el caso de que no se cuente con la información a nivel de zonas,

la mejor opción es estimar los viajes a nivel comunal, y luego repartirlos entre las zonas. Dicha

división de los viajes debe realizarse en la misma proporción que se aprecia en los viajes

observados en la EOD 2012 para dicha comuna, periodo y propósito. Los resultados serán

igualmente representativos que en otras comunas, pero solo a nivel agregado, ya que a nivel

zonal existirán distorsiones, cuya magnitud dependerá de las cambios que haya sufrido el

patrón de uso de suelos.

Además, dado que los modelos RLM se estiman a nivel de usuarios en general, pero

ESTRAUS requiere vectores a nivel de categorías de usuario, es necesario establecer una forma

de distribuirlos entre ellas. Ya que los vectores de generación y atracción de viajes determinados

con modelos ACM si son por categorías de usuario, se debe distribuir los viajes estimados con

RLM en igual proporción, para el corte temporal-periodo-propósito-zona deseado.

Dado a que los modelos de generación y atracción son estimados de forma

independiente, el total de viajes predicho generados y atraídos no coincide. Para solucionar

este problema, se propone simplemente escalar los viajes atraídos para cada período y

propósito, de tal manera que igualen a los viajes generados. Se propone utilizar los viajes

generados como referencia pues según experiencias pasadas éstos ofrecen un mayor ajuste.

Por último, debe notarse que en Punta Mañana los modelos de generación y

atracción son estimados considerando ambas horas (7:00 a 9:00). Aunque es deseable utilizar

la implementación de ESTRAUS con ambos horarios, pueden existir casos en que solo use uno.

Para ellos, es necesario aplicar factores de ajuste para la generación y la atracción, los cuales

se detallan en la siguiente tabla. Estos son uniformes entre zonas y comunas, al igual que entre

ACM y RLM, pero difieren según el propósito.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 12-46 Factores de Ajuste para un solo Periodo Punta Mañana**

|Propósito|Factor para PM1|Factor para PM2|
|---|---|---|
|**Trabajo**|0,579|0,421|
|**Estudio 1**|0,712|0,288|
|**Estudio 2**|0,536|0,464|
|**Otros**|0,442|0,558|

Fuente: Elaboración propia.

86

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 13 C ALIBRACIÓN DE M ODELOS DE P ARTICIÓN M ODAL (T AREA 13)

87

Para la calibración de los modelos de demanda se requiere una base de datos que

cuente con información sobre viajes observados, variables socioeconómicas de los viajeros y

atributos de los modos posibles a elegir para el viaje realizado. Los dos primeros pueden

obtenerse a partir de la EOD, mientras que el último se determina a partir de los resultados

obtenidos de simulaciones de la red, usando el modelo ESTRAUS. Dado que no es posible

observar probabilidades de elección, sino directamente la elección de cada individuo,

normalmente se recurre a la técnica estadística de **máxima verosimilitud** para calibrar los

parámetros (en lugar de los típicos mínimos cuadrados).

**13.1** **Estimación de modelos MNL**

Inicialmente, se calibró un modelo (“Base”) usando la totalidad de los datos de la

muestra de calibración (incluyendo todos los propósitos y períodos). El objetivo es determinar

de forma robusta y consistente las valoraciones relativas del “tiempo de acceso” y “tiempo de

espera” con respecto al “tiempo de viaje”. Así, se puede construir una función consistente de

“tiempo generalizado de viaje”. Esto presenta dos ventajas importantes. Primero, se garantiza

que para todos los periodos, propósitos y modos, la relación entre estas variables es siempre la

misma; lo que es una restricción exógena al modelo, pero que resulta razonable y apropiada.

Por otro lado, en los modelos específicos para cada periodo-propósito basta con estimar un

solo parámetro para el tiempo generalizado, lo que incrementa la eficiencia en el uso de la

información disponible, facilitando la estimación y aumentando el nivel de significancia de los

parámetros obtenidos.

En la siguiente tabla se presentan las funciones de utilidad del MNL Base, las cuales

corresponden a la forma más general usada en todos los modelos específicos para cada

periodo y propósito, tanto en sus formas MNL como NL. En el caso de los modelos de Partición

Modal con Elección de Horario (Tarea 16), existe el doble de funciones de utilidad, ya que

cada modo tiene una función independiente para cada horario, pero su forma es análoga.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 13-1 Funciones de Utilidad MNL Base**

88

|Modo ESTRAUS|Forma Funcional|
|---|---|
|1 Caminata|U1 = θ1 + θtv−cam∙tv1|
|2 Auto (chofer)|U2 = θ2 + θtv−auto∙tv2<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I2 + θnAutos∙nAutos|
|3 Auto (acompañante)|U3 = θ3 + θtv−auto∙tv3<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I3 + θnAutos∙nAutos|
|4 Taxi|U4 = θ4 + θtv∙tv4 + θta∙ta4 + θte∙te4<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I4|
|5 Bus Transantiago|U5 = θ5 + θtv∙tv5 + θta∙ta5 + θte∙te5 + θtr∙tr5<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I5|
|6 Taxi colectivo|U6 = θ6 + θtv∙tv6 + θta∙ta6 + θte_CN∙te6 + θtr∙tr6<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I6|
|7 Metro|U7 = θ7 + θtv∙tv7 + θta∙ta7 + θte∙te7<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I7 + θMujer∙δMujer|
|8 Bus Transantiago - Metro|U8 = θ8 + θtv∙tv8 + θta∙ta8 + θte∙te8<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I8 + θMujer∙δMujer|
|9 Taxi colectivo - Metro|U9 = θ9 + θtv∙tv9 + θta∙ta9 + θte_CN∙te9<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I9 + θMujer∙δMujer|
|12 Bicicleta|U12 = θ12 + θtv−bic∙tv12|
|13 Bus No Transantiago|U13 = θ13 + θtv∙tv13 + θta∙ta13 + θte_CN∙te13<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I13|
|14 Bus No Transantiago - Metro|U14 = θ14 + θtv∙tv14 + θta∙ta14 + θte_CN∙te14<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I14 + θMujer∙δMujer|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

Donde:

 - U i : Utilidad del modo i.

 - θ i : Constante del modo i.

 - tv i : Tiempo de viaje del modo i.

 - θ tv : Constante del tiempo de viaje.

 - θ tv−cam : Constante del tiempo de viaje para el modo Caminata.

 - θ tv−bic : Constante del tiempo de viaje para el modo Bicicleta.

 - θ tv−auto : Constante del tiempo de viaje para los modos Auto.

 - ta i : Tiempo de acceso del modo i.

 - θ ta : Constante del tiempo de acceso.

 - te i : Tiempo de espera del modo i.

 - θ te : Constante del tiempo de espera.

89

- θ te_CN : Constante del tiempo de espera para los modos Taxi colectivo, Bus

No Transantiago y sus combinaciones con Metro.

- tr i : Número de transbordos del modo i.

- θ tr : Constante del número de transbordos.

- C_I i : Costo total del modo i dividido por el ingreso del hogar.

- δ Ij : Variable binaria que vale 1 si el hogar pertenece a la clase j de

ingreso, 0 en otro caso.

- θ c Ij : Constante del costo del modo para la clase de hogar j.

- nAutos : Número de autos en el hogar.

- θ nAutos : Constante del número de autos en el hogar.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

90

 - δ Mujer : Variable binaria que vale 1 si el viajero es mujer, 0 en otro caso.

 - θ : Constante de la variable binaria δ .
Mujer Mujer

Utilizando los valores de los parámetros del modelo base para calcular el valor

relativo de los tiempos se obtiene que:

 El valor del “tiempo de acceso” es **3,33 veces** el del “tiempo de viaje”.

 El valor del “tiempo de espera” es **1,84 veces** el del tiempo de viaje.

Estos resultados son similares a los utilizados en la calibración de ESTRAUS a partir

de la EOD 2001, cuyos valores eran 3,63 y 1,93, respectivamente.

Así, la función de tiempo generalizado a utilizar es:

tg i = 3, 33∙ta i + 1, 84∙te i + tv i (9)

Donde tg i es el tiempo generalizado del modo i, y todas las demás variables han

sido previamente definidas.

A partir de esta función se procedió primero a calibrar modelos MNL para cada

periodo y propósito. Para seleccionar los mejores de entre todos los estimados, se tuvo en

consideración el signo de los coeficientes obtenidos, su significancia y la verosimilitud del

modelo conjunto.

**13.2** **Estimación de modelos NL o HL**

Tomando como base las mejores formulaciones obtenidas en los modelos MNL, se

estiman diversas especificaciones de modelos Logit anidados o jerárquicos (NL o HL) a fin de

poder elegir la que posee mejor ajuste estadístico y explica mejor el fenómeno de elección

modelado. Se parte de un modelo con dos nidos: transporte privado y transporte público, ya

que debido a las limitaciones impuestas por ESTRAUS, no es posible utilizar más de dos nidos

a partir de la raíz.

En el nido de transporte privado se ubican los modos Auto (Chofer), Auto

(Acompañante) y Taxi, mientras que en el de transporte público se incluyen todos los demás, a

excepción de los modos no motorizados: Bicicleta y Caminata. Para estos últimos dos modos,

se probaron formulaciones en que pertenecían a cualquiera de los nidos, o simplemente nacían

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

91

de la raíz. Posterior al proceso de partición modal, se incluye un nivel adicional para la elección

horaria en el caso del periodo Punta Mañana.

En la figura a continuación se muestra un ejemplo de la estructura de un árbol Logit

probado, con los modos no motorizados en el nido de transporte privado.

**Ilustración 13-1 Estructura Jerárquica Base**

NOTA: El Tercer Nivel, correspondiente a la elección de horario, solo se modela para el

período PM.
Fuente: Elaboración propia.

**13.3** **Modelos de Partición Modal**

En la presente sección se describen los mejores modelos de Partición Modal para

cada periodo y propósito. **Estos fueron implementados en ESTRAUS para los**

**periodos Fuera de Punta y Punta Tarde, pero no para el periodo Punta Mañana** .

Esto se debe a que el modelo de Partición Modal con Elección Horaria (ver Tarea 16) presenta

un mejor ajuste para el periodo Punta Mañana, por lo que fue el implementado en ESTRAUS.

**13.3.1** **Punta Mañana (NO implementado en ESTRAUS)**

A continuación, se presentan los modelos MNL para Punta Mañana, aunque **estos**

**NO fueron implementados en ESTRAUS**, ya que los modelos con Elección Horaria

(Tarea 16) presentan mejor ajuste.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 13-2 Modelo de Partición Modal PM, propósito trabajo (MNL), NO**

**implementado en ESTRAUS**

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ1|1,2004|8,30|
|θ2|0,7436|4,42|
|θ3|-1,8281|-9,31|
|θ4|-1,8004|-8,78|
|θ5|0,0000|-|
|θ6|-1,0930|-5,89|
|θ7|1,7598|12,59|
|θ8|-0,4993|-8,37|
|θ9|-2,0878|-10,05|
|θ12|0,6042|4,35|
|θtg1|-0,0466|-13,71|
|θtg2|-0,0163|-8,08|
|θtg−ayt|-0,0225|-7,51|

|Parámetro|Valor|Test-t|
|---|---|---|
|θtg−bus|-0,0083|-6,39|
|θtg−txc|-0,0164|-6,25|
|θtg7|-0,0332|-18,38|
|θtg12|-0,0916|-12,06|
|θtr|-1,2821|-16,72|
|θcI1|-0,0004|-2,55|
|θcI2|-0,0002|-2,88|
|θcI3|-0,0001|-3,88|
|θcI4|-0,0001|-6,38|
|θcI5|-0,0001|-3,73|
|θnAutos|0,6864|6,46|
|θMujer|-0,3553|-3,07|

Fuente: Elaboración propia.

92

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

93

**Tabla 13-3 Modelo de Partición Modal PM, propósito estudio 1 (MNL), NO**

**implementado en ESTRAUS**

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ1|1,5457|12,63|
|θ2|-0,5230|-0,98|
|θ3|-0,6786|-3,24|
|θ4|-3,7017|-14,27|
|θ5|0,0000|-|
|θ6|-2,4441|-9,80|
|θ7|-0,2000|-0,67|
|θ8|-1,4090|-10,23|
|θ9|-4,2810|-9,01|

|Parámetro|Valor|Test-t|
|---|---|---|
|θ12|-2,5465|-9,85|
|θtg−act|-0,0478|-14,27|
|θtg−aut|-0,0259|-5,30|
|θtg−tyc|-0,0108|-2,43|
|θtg−bus|-0,0069|-2,44|
|θtg7|-0,0221|-5,42|
|θtr|-0,9141|-6,62|
|θnAutos|1,1917|8,11|
|θMujer|-0,4380|-2,57|

Fuente: Elaboración propia.

**Tabla 13-4 Modelo de Partición Modal PM, propósito estudio 2 (MNL), NO**

**implementado en ESTRAUS**

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ12|0,1027|0,20|
|θtg1|-0,0309|-2,89|
|θtg−aut|-0,0153|-2,50|
|θtg−pub|-0,0134|-4,70|
|θtg12|-0,0982|-4,70|

www.FDCConsult.com

|Parámetro|Valor|Test-t|
|---|---|---|
|θ1|-0,4200|-0,62|
|θ2|-1,6315|-3,83|
|θ3|-2,4610|-5,74|
|θ5|0,0000|-|
|θ6|-2,9706|-6,50|

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ7|0,8060|5,11|
|θ8|0,2658|1,91|
|θ9|-2,6356|-8,92|

|Parámetro|Valor|Test-t|
|---|---|---|
|θtr|-1,0292|-5,60|
|θnAutos|0,5373|3,29|

Fuente: Elaboración propia.

**Tabla 13-5 Modelo de Partición Modal PM, propósito otros (MNL), NO**

**implementado en ESTRAUS**

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ1|1,8169|8,06|
|θ2|2,2921|7,36|
|θ3|-0,8727|-2,73|
|θ4|-1,3278|-5,83|
|θ5|0,0000|-|
|θ6|-1,4163|-8,33|
|θ7|-0,5731|-2,18|
|θ8|-0,9943|-4,55|
|θ9|-2,6838|-7,12|
|θ12|-2,3040|-8,85|

|Parámetro|Valor|Test-t|
|---|---|---|
|θtg−act|-0,0607|-7,65|
|θtg−aut|-0,0182|-2,76|
|θtg−pub|-0,0111|-3,20|
|θtr|-1,3574|-6,62|
|θcI1|-0,0003|-3,08|
|θcI2|-0,0002|-2,43|
|θcI3|-0,0001|-2,09|
|θcI45|-0,0001|-2,00|
|θnAutos|0,4674|2,28|
|θMujer|-0,6119|-2,65|

Fuente: Elaboración propia.

94

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**13.3.2** **Fuera de Punta**

**Tabla 13-6 Modelo de Partición Modal FP, propósito trabajo (MNL)**

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ1|1,8348|4,74|
|θ2|1,3151|3,64|
|θ3|-2,7699|-6,35|
|θ4|-2,5445|-6,11|
|θ5|0,0000|-|
|θ6|-1,2903|-5,78|
|θ7|0,6069|2,32|
|θ8|-0,2422|-2,42|

|Parámetro|Valor|Test-t|
|---|---|---|
|θ9|-2,1718|-6,22|
|θ12|0,6511|1,43|
|θtg−act|-3,9713|-6,31|
|θtg−pri|-2,3107|-1,97|
|θtg−pub|-1,2146|-4,28|
|θC|-0,2120|-3,43|
|θnAutos2|1,9292|5,69|

Fuente: Elaboración propia.

95

Los coeficientes de tiempo generalizado aplican para más de un modo: θ tg−act es
válido para 1 y 12; θ tg−pri es válido para 2, 3 y 4; θ tg−pub es válido para 5, 6, 7, 8 y 9.

θ nAutos2 aplica solo en los modos 2 y 3, para aquellos viajeros de hogares con 2 o más

vehículos.

**Tabla 13-7 Modelo de Partición Modal FP, propósito estudio (MNL)**

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ8|0,3853|1,32|
|θ9|-3,1918|-3,81|
|θ12|1,2298|3,10|

www.FDCConsult.com

|Parámetro|Valor|Test-t|
|---|---|---|
|θ1|2,3374|4,38|
|θ2|-0,3642|-1,76|
|θ3|-2,4870|-3,11|

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ5|0,0000|-|
|θ6|-2,3287|-3,89|
|θ7|0,3263|1,35|

|Parámetro|Valor|Test-t|
|---|---|---|
|θtg−act|-3,7936|-4,52|
|θtg−veh|-0,3866|-1,13|
|θnAutos2|2,1916|3,31|

Fuente: Elaboración propia.

96

Los coeficientes de tiempo generalizado aplican para más de un modo: θ tg−act es
válido para 1 y 12; θ tg−veh es válido para 2, 3, 5, 6, 7, 8 y 9. θ nAutos2 aplica solo en los

modos 2 y 3, para aquellos viajeros de hogares con 2 o más vehículos.

Debe notarse que en la base de datos no se cuenta con observaciones válidas para

el modo Taxi en este propósito, por lo que no fue posible modelarlo y no se encontrará

disponible en ESTRAUS.

**Tabla 13-8 Modelo de Partición Modal FP, propósito vuelta a casa (MNL)**

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ1|3,1359|8,07|
|θ2|2,5592|6,03|
|θ3|-0,7409|-2,25|
|θ4|-1,3974|-3,83|
|θ5|0,0000|-|
|θ6|0,0375|1,85|
|θ7|0,9622|2,67|

|Parámetro|Valor|Test-t|
|---|---|---|
|θ8|-0,6510|-3,64|
|θ9|-3,5821|-3,67|
|θ12|0,0939|0,01|
|θtg−act|-6,2317|-7,56|
|θtg−veh|-1,5536|-3,33|
|θC|-0,2718|-2,82|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

97

Los coeficientes de tiempo generalizado aplican para más de un modo: θ tg−act es
válido para 1 y 12; θ tg−veh es válido para 2, 3, 4, 5, 6, 7, 8 y 9.

**Tabla 13-9 Modelo de Partición Modal FP, propósito compras (MNL)**

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ1|2,5658|12,23|
|θ2|1,7743|5,35|
|θ3|-0,9926|-3,31|
|θ4|-3,1061|-6,69|
|θ5|0,0000|-|
|θ6|-0,5695|-3,83|
|θ7|-0,0357|-0,73|

|Parámetro|Valor|Test-t|
|---|---|---|
|θ8|-2,0514|-5,73|
|θ9|-1,9548|-5,02|
|θ12|0,1146|1,50|
|θtg−act|-4,0060|-8,51|
|θtg−veh|-1,2030|-8,51|
|θC|-0,1765|-1,86|
|θnAutos2|0,4397|1,07|

Fuente: Elaboración propia.

Los coeficientes de tiempo generalizado aplican para más de un modo: θ tg−act es
válido para 1 y 12; θ tg−veh es válido para 2, 3, 4, 5, 6, 7, 8 y 9. θ nAutos2 aplica solo en los

modos 2 y 3, para aquellos viajeros de hogares con 2 o más vehículos.

**Tabla 13-10 Modelo de Partición Modal FP, propósito otros (NL)**

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ7|0,0819|0,33|
|θ8|-0,2382|-3,16|
|θ9|-0,4332|-3,25|
|θ12|-1,6310|-3,67|

www.FDCConsult.com

|Parámetro|Valor|Test-t|
|---|---|---|
|φ[1]|1,0000|-|
|φ[2]|0,1594|17,51|
|θ1|1,0166|4,67|
|θ2|0,6372|3,84|

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ3|-2,0609|-9,18|
|θ4|-2,0824|-11,55|
|θ5|0,0000|-|
|θ6|-0,1150|-3,07|

|Parámetro|Valor|Test-t|
|---|---|---|
|θtg−act|-3,7472|-8,68|
|θtg−veh|-0,0973|-2,11|
|θc|-0,2093|-4,20|
|θnAutos2|1,1941|4,09|

Fuente: Elaboración propia.

98

El nido de transporte privado (φ [1] ) se encuentra colapsado, pero no el de
transporte público (φ [2] ). Los coeficientes de tiempo generalizado aplican para más de un

modo: θ tg−act es válido para 1 y 12; θ tg−veh es válido para 2, 3, 4, 5, 6, 7, 8 y 9. θ nAutos2

aplica solo en los modos 2 y 3, para aquellos viajeros de hogares con 2 o más vehículos.

**13.3.3** **Punta Tarde**

**Tabla 13-11 Modelo de Partición Modal PT, propósito trabajo y estudio (NL)**

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ9|-1,0203|-4,95|
|θ12|0,3113|-0,01|
|θtg−act|-2,5644|-11,25|
|θtg−pri|-1,4989|-7,17|
|θtg−pub|-0,7060|-5,54|
|θtg7|-1,0560|-6,08|
|θcI12|-0,6681|-5,08|
|θcI345|-0,2033|-6,83|

www.FDCConsult.com

|Parámetro|Valor|Test-t|
|---|---|---|
|φ[1]|1,0000|-|
|φ[2]|0,3964|8,74|
|θ1|0,9992|3,81|
|θ2|1,1197|6,94|
|θ3|-1,8040|-11,67|
|θ4|-3,4464|-12,71|
|θ5|0,0000|-|
|θ6|-0,6224|-4,54|

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ7|0,7496|5,31|
|θ8|-0,0458|-1,73|

|Parámetro|Valor|Test-t|
|---|---|---|
|θnAutos2|0,9820|6,58|

Fuente: Elaboración propia.

99

El nido de transporte privado (φ [1] ) se encuentra colapsado, pero no el de
transporte público (φ [2] ). Los coeficientes de tiempo generalizado aplican para más de un

modo, excepto el modo 7: θ tg−act es válido para 1 y 12; θ tg−pri es válido para 2, 3 y 4;
θ tg−pub es válido para 5, 6, 8 y 9. Los coeficientes de costo se encuentran agrupados por clase
de usuario: θ c I12 es válido para 1 y 2; θ c I345 es válido para 3, 4 y 5. θ nAutos2 aplica solo en

los modos 2 y 3, para aquellos viajeros de hogares con 2 o más vehículos.

**Tabla 13-12 Modelo de Partición Modal PT, propósito vuelta a casa (NL)**

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|φ[1]|1,0000|-|
|φ[2]|0,0988|21,36|
|θ1|2,3271|12,19|
|θ2|1,9037|10,42|
|θ3|-0,3508|-3,37|
|θ4|-1,8631|-8,97|
|θ5|0,0000|-|
|θ6|-0,0379|-1,76|

|Parámetro|Valor|Test-t|
|---|---|---|
|θ7|0,0482|0,64|
|θ8|-0,0849|-2,08|
|θ9|-0,4140|-2,24|
|θ12|0,2885|0,33|
|θtg−act|-4,5482|-11,59|
|θtg−veh|-0,0911|-1,84|
|θC|-0,1410|-2,81|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

100

El nido de transporte privado (φ [1] ) se encuentra colapsado, pero no el de
transporte público (φ [2] ). Los coeficientes de tiempo generalizado aplican para más de un

modo: θ tg−act es válido para 1 y 12; θ tg−veh es válido para 2, 3, 4, 5, 6, 7, 8 y 9.

**Tabla 13-13 Modelo de Partición Modal PT, propósito compras (MNL)**

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ1|3,1033|7,37|
|θ2|2,8084|6,57|
|θ3|1,5870|2,91|
|θ4|-0,5124|-1,22|
|θ5|0,0000|-|
|θ6|-1,5461|-2,79|
|θ7|-0,2192|-0,47|

|Parámetro|Valor|Test-t|
|---|---|---|
|θ8|-2,2527|-3,23|
|θ9|-4,2020|-2,79|
|θ12|0,2644|0,59|
|θtg−act|-4,4566|-5,96|
|θtg−pri|-6,8042|-4,46|
|θtg−pub|-1,7857|-2,35|

Fuente: Elaboración propia.

Los coeficientes de tiempo generalizado aplican para más de un modo, excepto el
modo 7: θ tg−act es válido para 1 y 12; θ tg−pri es válido para 2, 3 y 4; θ tg−pub es válido para

5, 6, 8 y 9. No existe un coeficiente para el costo en este modelo, ya que dicha variable no

explica el comportamiento de los usuarios en base a los datos disponibles.

**Tabla 13-14 Modelo de Partición Modal PT, propósito otros (NL)**

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ7|0,5513|2,50|
|θ8|-0,7959|-2,95|
|θ9|-2,6935|-4,43|

www.FDCConsult.com

|Parámetro|Valor|Test-t|
|---|---|---|
|φ[1]|0,8060|1,30|
|φ[2]|1,0000|-|
|θ1|2,4306|7,03|

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Parámetro** **Valor** **Test-t** **Parámetro** **Valor** **Test-t**

|Parámetro|Valor|Test-t|
|---|---|---|
|θ2|1,8110|4,97|
|θ3|-0,6932|-2,24|
|θ4|-1,9443|-6,08|
|θ5|0,0000|-|
|θ6|-1,2250|-3,45|

|Parámetro|Valor|Test-t|
|---|---|---|
|θ12|0,9804|1,02|
|θtg−act|-4,2379|-8,65|
|θtg−veh|-1,7976|-4,76|
|θC|-0,1258|-2,12|
|θnAutos2|1,1023|3,53|

Fuente: Elaboración propia.

101

El nido de transporte público (φ [2] ) se encuentra colapsado, pero no el de
transporte privado (φ [1] ). Los coeficientes de tiempo generalizado aplican para más de un

modo: θ tg−act es válido para 1 y 12; θ tg−veh es válido para 2, 3, 4, 5, 6, 7, 8 y 9. θ nAutos2

aplica solo en los modos 2 y 3, para aquellos viajeros de hogares con 2 o más vehículos.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 14 C ALIBRACIÓN DE M ODELOS DE D ISTRIBUCIÓN (T AREA 14)

**14.1** **Enfoque Metodológico**

102

**La base de datos que se utiliza en la calibración de los modelos de**

**Distribución fue definida en la Sección 13.2 de la Tarea 13.**

Tradicionalmente, para modelar la Distribución de Viajes ESTRAUS ha usado

modelos Gravitacionales de Maximización de Entropía. Sin embargo, durante los últimos años

se han introducido en el código respectivo generalizaciones en la formulación de dichos

modelos: i. La introducción de **modelos DCM** (Distribution Consolidated Models) y ii. la

incorporación de **modelos simplemente acotados a orígenes** [6] . Ambos son

considerados en el presente estudio en la calibración, tanto secuencial como simultáneo.

Se estimaron modelos Gravitacionales Doblemente Acotados (DC_D) para cada
periodo-propósito. En el caso del propósito compras para los periodos Fuera de Punta y Punta
Tarde, también se calibró un modelo Simplemente Acotado a Orígenes (DC_S). En él, la
superficie de comercio fue utilizada como atractividad de los destinos.

También se estimaron modelos Gravitacionales Doblemente Acotados con Efectos

por Distancia (DC_D_S) para cada periodo-propósito. En el caso del propósito compras para
los periodos Fuera de Punta y Punta Tarde, también se calibró un modelo Simplemente Acotado
a Orígenes (DC_S_S). En él, la superficie de comercio fue utilizada como atractividad de los

destinos.

Por último, se estimaron modelos DCM doblemente acotados (DC_D_S_M)
estimados para cada periodo-propósito. En general se espera que el parámetro adicional que
incluyen estos modelos, permita un mejor ajuste que los modelos Gravitacionales tradicionales.
En el caso del propósito compras para los periodos Fuera de Punta y Punta Tarde, también se
calibró un modelo Simplemente Acotado a Orígenes (DC_S_S_M). En él, la superficie de

comercio fue utilizada como atractividad de los destinos.

6 Ambas generalizaciones fueron presentadas en el Informe 1.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**14.2** **Modelos de Distribución**

103

En la presente sección se describen los mejores modelos de Distribución para cada

periodo y propósito, **los cuales fueron implementados en ESTRAUS** .

**Tabla 14-115 Modelos de Distribución Implementados en ESTRAUS**

|Periodo|Propósito|Acotado|β|ρ|γ|
|---|---|---|---|---|---|
|PM|Trabajo|Doblemente|1,3059|0,5302|-|
|PM|Estudio 1|Doblemente|1,6860|0,8368|-|
|PM|Estudio 2|Doblemente|4,5252|-|-|
|PM|Otros|Doblemente|1,1627|0,6420|-|
|FP|Trabajo|Doblemente|1,3732|-|-|
|FP|Estudio|Doblemente|3,0551|-|-|
|FP|Vuelta a Casa|Doblemente|1,3112|-|-|
|FP|Compras|Simplemente|1,9312|-|-|
|FP|Otros|Doblemente|2,4896|0,4977|-|
|PT|Trabajo y Estudio|Doblemente|0,6051|0,6902|-|
|PT|Vuelta a Casa|Doblemente|1,1494|0,3230|-|
|PT|Compras|Doblemente|1,2001|-|-|
|PT|Otros|Doblemente|1,2280|-|-|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 15 V ALIDACIÓN DE LOS M ODELOS DE D EMANDA (T AREA 15)

104

Una vez calibrados todos los parámetros de los modelos de demanda endógenos

(Distribución, Partición Modal y Elección de Horario) se procede a su validación. Cabe destacar

que este proceso es independiente de ESTRAUS. Para dicha validación, referirse a la Tarea 17:

Validación del Modelo Completo.

**15.1** **Validación de los Modelos de Partición Modal**

En la presente sección se resumen las validaciones realizadas sobre los mejores

Modelos de Partición Modal para cada periodo-propósito (Tarea 13):

 - En **Punta Mañana**, para todos los propósitos, los mejores modelos fueron

**NL**, los cuales **predicen correctamente 166** de las observaciones,

equivalente al **52%** del total. **Estos modelos no fueron**

**implementados en ESTRAUS en desmedro de aquellos con**

**elección horaria (ver siguiente sub-sección).**

 - En **Fuera de Punta**, los mejores modelos fueron **MNL** para los propósitos

Trabajo, Estudio, Vuelta a Casa y Compras; mientras que fue **NL** para los

propósitos Otros. En conjunto, **predicen correctamente 2.252** de las

observaciones, equivalente al **96,2%** del total.

 - En **Punta Tarde**, los mejores modelos fueron **NL** para los propósitos

Trabajo y Estudio, Vuelta a Casa y Otros; mientras que fue **MNL** para el

propósito Compras. En conjunto, **predicen correctamente 4.369** de las

observaciones, equivalente al **96,0%** del total.

**15.2** **Validación de los Modelos de Partición Modal con Elección Horaria**

En la presente sección se resumen las validaciones realizadas sobre los mejores

Modelos de Partición Modal con Elección Horaria para cada propósito del periodo Punta

Mañana (Tarea 16): los mejores modelos **predicen correctamente 11.643** de las

observaciones, equivalente al **99,8%** del total.

**15.3** **Validación de los Modelos de Distribución**

En la presente sección se resumen las validaciones realizadas sobre los mejores

Modelos de Distribución para cada periodo-propósito (Tarea 14):

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

105

- En todos los modelos de **Punta Mañana**, el mejor modelo siempre es el

Gravitacional con Efecto de Distancia (DC_D_S), excepto en Estudio 2, en

que lo es el Gravitacional (DC_D). Sus **R** **[2]** **oscilan entre 0,83 y 0,95** .

- En el caso de **Fuera de Punta**, el mejor modelo siempre es el

Gravitacional (DC_D), excepto en Otros, en que lo es el DC_D_S. Sus **R** **[2]**

**oscilan entre 0,91 y 0,97** . Para el propósito Compras, en FP el mejor

modelo es DC_S acotados a orígenes con la Superficie de Comercio como

factor de atracción (DC_S).

- En el caso de **Punta Tarde**, el mejor modelo siempre es el Gravitacional

(DC_D), excepto en Trabajo y Estudio y Vuelta a Casa. Sus **R** **[2]** **oscilan**

**entre 0,86 y 0,95** .

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 16 D EFINICIÓN M ODELO DE E LECCIÓN H ORARIA DE V IAJE (T AREA 16)

**16.1** **Enfoque Metodológico**

106

El concepto de **elección de horario** de viaje tiene sentido cuando determinados

viajeros, a fin de percibir mejores niveles de servicio, adelantan (o atrasan) el horario de

realización de su viaje. En este contexto, es factible que algunos usuarios, por ejemplo, para

pagar una menor tarifa en el Metro, o para evitarse el desagrado que implica la congestión en

la punta mañana, adelanten el horario de realización del viaje.

La elección de horario, requiere de la subdivisión del período Punta Mañana en al

menos 2 subperíodos de modelación, por lo que los usuarios que tienen la alternativa real de

elegir el período en el que realizarán su viaje, optarán por aquel período en que se maximice

su utilidad individual.

Para el presente estudio de calibración, en la Tarea 13 se propone una estimación

del modelo de Elección de Horario en conjunto con el de Partición Modal, agregando un nivel

adicional de elección como si fuera un pseudo modo. El modelo calibrado con este

procedimiento puede usarse posteriormente como solución inicial de dichas elecciones, para la

aplicación de método de calibración simultánea que se realizó en la Tarea 20.

En la Tarea 13 se calibraron modelos jerárquicos de partición modal para el total

de la punta mañana (7:00 a 9:00). Los modelos calibrados en esta sección poseen la misma

estructura de nidos y función de utilidad en los modos que las presentadas en la Tarea 13.

**La base de datos que se utiliza en la calibración de los modelos de**

**Partición Modal con Elección Horaria fue definida en la Sección 13.2 de la Tarea**

**13.**

**16.2** **Modelos de Partición Modal con Elección Horaria**

En la presente sección se describen los mejores modelos de Partición Modal con

Elección Horaria para todos los propósitos del periodo Punta Mañana, con las constantes

modales ajustadas. **Estos se implementaron en ESTRAUS, pues presentan mejor**

**ajuste que los modelos de Partición Modal sin elección horaria (Tarea 13).**

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**16.2.1** **Punta Mañana, propósito trabajo**

107

El mejor modelo obtenido para este caso considera las funciones de utilidad del

mejor NL para este mismo periodo y propósito, excepto por la agrupación de las constantes de

ingreso para las clases 3, 4 y 5. El árbol corresponde a la estructura jerárquica, pero en el

proceso de calibración para elegir el mejor modelo, se debió deshacer el nido de transporte
privado (φ [1] = 1). Además, todos los nidos de elección horaria colapsaron (φ [A] = φ [B] =
φ [C] = φ [D] = φ [E] = φ [F] = φ [G] = φ [H] = φ [I] = φ [J] = 1). La diferencia en las funciones

de utilidad dentro de un mismo modo, pero distinto horario, es únicamente el valor de la

constante modal, ya que comparten el resto de los parámetros. Los correspondientes valores de

los parámetros obtenidos se muestran en la tabla siguiente.

**Tabla 16-1 Modelo de Partición Modal PM con Elección Horaria, Propósito**

**Trabajo**

**Parámetro** **Valor** **Parámetro** **Valor**

|Parámetro|Valor|
|---|---|
|θ5H2|-0,5323|
|θ6H2|-1,5154|
|θ7H2|0,4298|
|θ8H2|0,0115|
|θ9H2|-1,9831|
|θ12H2|-0,3859|
|θtg1|-3,2003|
|θtg−pri|-0,2198|
|θtg−bus|-0,1850|
|θtg−txc|-0,2404|
|θtg7|-0,5702|

www.FDCConsult.com

|Parámetro|Valor|
|---|---|
|φ[1]|1,0000|
|φ[2]|0,2201|
|φ[A]|1,0000|
|θ1H1|0,2139|
|θ2H1|0,5588|
|θ3H1|-2,1190|
|θ4H1|-3,7021|
|θ5H1|0,0000|
|θ6H1|-1,2508|
|θ7H1|0,4324|
|θ8H1|0,4490|

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Parámetro** **Valor** **Parámetro** **Valor**

|Parámetro|Valor|
|---|---|
|θ9H1|-1,5773|
|θ12H1|-0,2915|
|θ1H2|0,7117|
|θ2H2|0,2184|
|θ3H2|-2,8098|
|θ4H2|-3,5089|

|Parámetro|Valor|
|---|---|
|θtg12|-2,1234|
|θcI1|-0,4016|
|θcI2|-0,3337|
|θcI345|-0,2186|
|θnAutos2|1,1391|

Fuente: Elaboración propia.

108

Los coeficientes de tiempo generalizado aplican para más de un modo, excepto en
los modos 1, 7 y 12: θ tg−pri es válido para 2, 3 y 4; θ tg−bus es válido para 5 y 8; θ tg−txc es

válido para 6 y 9. θ nAutos2 aplica solo en los modos 2 y 3, para aquellos viajeros de hogares

con 2 o más vehículos.

**16.2.2** **Punta Mañana, propósito estudio 1**

El mejor modelo obtenido para este caso considera las funciones de utilidad del

mejor NL para este mismo periodo y propósito. El árbol corresponde a la estructura jerárquica

base, pero en el proceso de calibración para elegir el mejor modelo, se debió deshacer el nido
de transporte privado (φ [1] = 1). Además, todos los nidos de elección horaria colapsaron
(φ [A] = φ [B] = φ [C] = φ [D] = φ [E] = φ [F] = φ [G] = φ [H] = φ [I] = φ [J] = 1). La diferencia

en las funciones de utilidad dentro de un mismo modo, pero distinto horario, es únicamente el

valor de la constante modal, ya que comparten el resto de los parámetros. Los correspondientes

valores de los parámetros obtenidos se muestran en la tabla siguiente.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

109

**Tabla 16-2 Modelo de Partición Modal PM con Elección Horaria, Propósito**

**Estudio 1**

**Parámetro** **Valor** **Parámetro** **Valor**

|Parámetro|Valor|
|---|---|
|φ[1]|1,0000|
|φ[2]|0,5481|
|φ[A]|1,0000|
|θ1H1|1,1529|
|θ3H1|-0,2104|
|θ4H1|-3,0652|
|θ5H1|-0,1500|
|θ6H1|-2,9674|
|θ7H1|-0,0764|
|θ8H1|-0,7366|
|θ9H1|-5,4593|
|θ12H1|-2,5164|
|θ1H2|0,9122|

|Parámetro|Valor|
|---|---|
|θ3H2|-1,3480|
|θ4H2|-4,1753|
|θ5H2|-1,1918|
|θ6H2|-5,1397|
|θ7H2|-1,4137|
|θ8H2|-2,0699|
|θ12H2|-1,8630|
|θtg−act|-3,2396|
|θtg−pri|-0,3147|
|θtg−pub|-0,3912|
|θtg7|-0,8598|
|θnAutos2|1,5032|
|θC|-0,7799|

Fuente: Elaboración propia.

Los coeficientes de tiempo generalizado aplican para más de un modo, excepto en
el modo 7: θ tg−act es válido para 1 y 12; θ tg−pri es válido para 2, 3 y 4; θ tg−pub es válido

para 5, 6, 8 y 9. θ nAutos2 aplica solo en los modos 2 y 3, para aquellos viajeros de hogares

con 2 o más vehículos.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

110

Debe notarse que en la base de datos no se cuenta con observaciones válidas para

el modo combinado Taxicolectivo-Metro en el horario dos en este propósito, por lo que no fue

posible modelarlo y no se encontrará disponible en ESTRAUS.

**16.2.3** **Punta Mañana, propósito estudio 2**

El mejor modelo obtenido para este caso considera las funciones de utilidad del

mejor NL para este mismo periodo y propósito. El árbol corresponde a la estructura jerárquica

base, pero en el proceso de calibración para elegir el mejor modelo, se debió deshacer el nido
de transporte privado (φ [1] = 1). Además, todos los nidos de elección horaria colapsaron
(φ [A] = φ [B] = φ [C] = φ [D] = φ [E] = φ [F] = φ [G] = φ [H] = φ [I] = φ [J] = 1). La diferencia

en las funciones de utilidad dentro de un mismo modo, pero distinto horario, es únicamente el

valor de la constante modal, ya que comparten el resto de los parámetros. Los correspondientes

valores de los parámetros obtenidos se muestran en la tabla siguiente.

**Tabla 16-3 Modelo de Partición Modal PM con Elección Horaria, Propósito**

**Estudio 2**

**Parámetro** **Valor** **Parámetro** **Valor**

www.FDCConsult.com

|Parámetro|Valor|
|---|---|
|φ[1]|1,0000|
|φ[2]|0,2614|
|φ[A]|1,0000|
|θ1H1|-2,3310|
|θ2H1|-2,2864|
|θ3H1|-2,5753|
|θ5H1|-0,6102|
|θ6H1|-3,8750|
|θ7H1|0,2767|

|Parámetro|Valor|
|---|---|
|θ2H2|-2,6583|
|θ3H2|-2,7795|
|θ5H2|-0,8493|
|θ6H2|-3,9413|
|θ7H2|0,3684|
|θ8H2|0,1948|
|θ9H2|-6,4186|
|θ12H2|-1,2918|
|θtg1|-2,1205|

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Parámetro** **Valor** **Parámetro** **Valor**

|Parámetro|Valor|
|---|---|
|θ8H1|0,4129|
|θ9H1|-2,6275|
|θ12H1|-0,4361|
|θ1H2|-1,0081|

|Parámetro|Valor|
|---|---|
|θtg−veh|-0,2517|
|θtg12|-2,4939|
|θnAutos2|0,8675|
|θC|-0,0021|

Fuente: Elaboración propia.

111

El coeficiente de tiempo generalizado θ tg−veh aplica para todos los modos de

transporte motorizado, mientras que los no motorizados (1 y 12) tienen sus propios coeficientes.

θ nAutos2 aplica solo en los modos 2 y 3, para aquellos viajeros de hogares con 2 o más

vehículos.

Debe notarse que en la base de datos no se cuenta con observaciones válidas para

el modo Taxi en ningún horario en este propósito, por lo que no fue posible modelarlo y no se

encontrará disponible en ESTRAUS.

**16.2.4** **Punta Mañana, propósito otros**

El mejor modelo obtenido para este caso considera las funciones de utilidad del

mejor NL para este mismo periodo y propósito. El árbol corresponde a la estructura jerárquica

base, pero en el proceso de calibración para elegir el mejor modelo, se debió deshacer el nido
de transporte privado (φ [1] = 1). Además, todos los nidos de elección horaria colapsaron
(φ [A] = φ [B] = φ [C] = φ [D] = φ [E] = φ [F] = φ [G] = φ [H] = φ [I] = φ [J] = 1). La diferencia

en las funciones de utilidad dentro de un mismo modo, pero distinto horario, es únicamente el

valor de la constante modal, ya que comparten el resto de los parámetros. El valor de la función

**Log-Verosimilitud es de -3.299** . Los correspondientes valores de los parámetros obtenidos

se muestran en la tabla siguiente.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

112

**Tabla 16-4 Modelo de Partición Modal PM con Elección Horaria, Propósito**

**Otro**

**Parámetro** **Valor** **Parámetro** **Valor**

|Parámetro|Valor|
|---|---|
|φ[1]|1,0000|
|φ[2]|0,2105|
|φ[A]|1,0000|
|θ1H1|1,5522|
|θ2H1|1,6451|
|θ3H1|-0,8834|
|θ4H1|-2,5913|
|θ5H1|-0,1000|
|θ6H1|-0,7558|
|θ7H1|-0,2854|
|θ8H1|-0,2790|
|θ9H1|-5,7526|
|θ12H1|-1,2448|
|θ1H2|2,3939|
|θ2H2|1,3269|

|Parámetro|Valor|
|---|---|
|θ3H2|-1,4242|
|θ4H2|-1,9846|
|θ5H2|0,5125|
|θ6H2|-0,1501|
|θ7H2|-0,0434|
|θ8H2|-0,0922|
|θ9H2|-5,3691|
|θ12H2|-0,8631|
|θtg−act|-2,9175|
|θtg−veh|-0,1809|
|θcI1|-0,3485|
|θcI23|-0,3269|
|θcI45|-0,1069|
|θnAutos2|0,8817|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

113

Los coeficientes de tiempo generalizado aplican para más de un modo: θ tg−act es
válido para 1 y 12; θ tg−veh es válido para 2, 3, 4, 5, 6, 7, 8 y 9. θ nAutos2 aplica solo en los

modos 2 y 3, para aquellos viajeros de hogares con 2 o más vehículos.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 17 V ALIDACIÓN DEL M ODELO C OMPLETO (T AREA 17)

114

En esta tarea se realiza una validación del modelo completo ESTRAUS incluyendo

todos los submodelos recalibrados en el presente estudio (Distribución, Partición Modal,

Elección de Horario y Asignación). Para este fin, se comparan los resultados obtenidos de

asignaciones de equilibrio de ESTRAUS para el año de calibración (2012), con la información

disponible de la EOD 2012 y diversas fuentes para dicho año, de los flujos y niveles de servicio,

correspondientes a los modos y redes consideradas en la modelación.

La implementación computacional disponible del algoritmo de solución del modelo

matemático (a la que normalmente también se hace referencia como ESTRAUS) permite resolver

cualquiera de los problemas siguientes [7] :

 - D-PM-A Distribución, Partición Modal, Asignación

 - PM-A Partición Modal, Asignación

 - D-PM-EH-A Distribución, Partición Modal, Elección Horario, Asignación

 - PM-EH-A Partición Modal, Elección Horario, Asignación

La modelación más completa es la tercera, que considera todas las elecciones

involucradas en la operación del sistema de transporte urbano simuladas en ESTRAUS. Todas

las otras opciones de modelación son subconjuntos de esta, y eliminan las elecciones de Destino

(segunda y cuarta) y/o Elección de Horario (primera y segunda).

Dado que la modelación produce soluciones de equilibrio entre todas las

elecciones consideradas en cada caso y que los modelos utilizados en todos los casos son

exactamente los mismos (iguales funciones y parámetros de calibración) todas las opciones de

modelación consideradas son subconjuntos de la opción más detallada (tercera).

7 En la sección 2.3.2, de las Bases del presente estudio, se señalan además las opciones de modelación D-EH-PM
A y EH-PM-A. Sin embargo, ellas no están en la actualidad implementadas en el algoritmo de solución, por lo
que no se incluyen en las opciones consideradas.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

115

Por lo tanto, para comparar la solución de equilibrio obtenida para las distintas

alternativas de modelación, las corridas de ESTRAUS correspondientes a los casos parciales (D
PM-A, PM-A, PM-EH-A) deben suponer los valores de equilibrio de las opciones no

consideradas: i. Distribución en los casos segundo y cuarto y ii. Elección de Horario en los casos

primero y segundo. Además, en dichos casos parciales los valores supuestos para las elecciones

no consideradas debieran ser iguales a las observadas en la EOD-2012 [8] . Dicho lo anterior es

obvio que la solución de los casos parciales para las opciones modeladas debe coincidir

exactamente con la correspondiente a la obtenida en el caso más detallado [9] .

Considerando lo anterior, la solución de equilibrio de todos los casos arriba

considerados debe ser exactamente la misma para todos los submodelos de elección

modelados o supuestos. Esto garantiza que la validación de la opción más completa (D-PM-EH
A), asegura la validación de todas las otras opciones parciales.

Para realizar la validación primero se incorporan los parámetros de los cuatro

modelos involucrados, en el programa computacional que implementa el modelo de equilibrio

simultáneo (ESTRAUS). Además de ello, se genera todo el conjunto de datos necesarios para

la correcta ejecución del modelo (redes de transporte privado y público, vectores origen-destino,

matrices de viajes externas, etc., para cada una de las opciones disponibles en ESTRAUS y para

los tres períodos del día considerados). Cumplidas estas tareas, se realizan las corridas del

modelo ESTRAUS recalibrado para los tres períodos de modelación (punta mañana, fuera de

punta y punta tarde) en el año de calibración (2012). Los resultados obtenidos de dichas

corridas son confrontados con la situación observada en dicho año a través de la información

contenida en la EOD y las fuentes complementarias mencionadas anteriormente.

**17.1** **Validación del Modelo en Punta Mañana**

**17.1.1** **Partición Modal**

En las siguientes tablas se presentan las particiones modales objetivos y aquellas

obtenidas a partir de ESTRAUS para el año 2012, periodo Punta Mañana. Cabe destacar que

8 Ya que el modelo más detallado debiera reproducir dichos valores observados, que son la base de comparación

para las validaciones.

9 Esto fue comprobado empíricamente en el Estudio de Recalibración de ESTRAUS de 2005, Análisis y

Actualización del Modelo ESTRAUS, Volumen 3, Capítulo 16. Oct-2005.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

116

el número de viajes asignados es mayor al de la base de datos de la EOD 2012, pues se

incluyen viajes fijos en AutoChofer (que representan viajes en MotoChofer, Furgón Escolar

Pasajero y partes de viajes en combinaciones de AutoChofer no modeladas), Bus Transantiago

(que representan partes de viajes en combinaciones de BusTransantiago no modeladas) y Metro

(que representan partes de viajes en combinaciones de Metro no modeladas).

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 17-1 Partición Modal Base de Datos PM Total**

117

|Modo|Total PM|Col3|Trabajo|Col5|Estudio 1|Col7|Estudio 2|Col9|Otros|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Caminata**|** 373.910**|<br>**16,4%**|85.284|<br>7,1%|199.158|<br>36,1%|1.587|<br>1,3%|87.880|<br>21,9%|
|**Autochofer**|** 579.731**|<br>**25,5%**|392.096|<br>32,8%|1.038|0,2%|11.841|<br>9,3%|174.755|<br>43,6%|
|**Autoacompañante**|** 247.465**|<br>**10,9%**|54.354|<br>4,6%|162.312|<br>29,4%|8.409|<br>6,6%|22.390|<br>5,6%|
|**Taxi**|** 32.992**|<br>**1,5%**|14.258|<br>1,2%|7.301|<br>1,3%|34|<br>0,0%|11.399|<br>2,8%|
|**BusTransantiago**|** 488.538**|<br>**21,5%**|269.009|<br>22,5%|131.843|<br>23,9%|26.525|<br>20,9%|61.161|<br>15,2%|
|**Taxicolectivo**|** 45.779**|<br>**2,0%**|24.900|<br>2,1%|8.142|<br>1,5%|1.802|<br>1,4%|10.934|<br>2,7%|
|**Metro**|** 137.095**|<br>**6,0%**|86.920|<br>7,3%|10.564|<br>1,9%|31.640|<br>24,9%|7.970|<br>2,0%|
|**Metro-BusTransantiago**|** 261.268**|<br>**11,5%**|185.824|<br>15,6%|20.252|<br>3,7%|40.056|<br>31,6%|15.135|<br>3,8%|
|**Metro-Taxicolectivo**|** 18.389**|<br>**0,8%**|14.488|<br>1,2%|1.392|<br>0,3%|1.507|<br>1,2%|1.002|<br>0,2%|
|**Bicicleta**|** 88.937**|<br>**3,9%**|67.149|<br>5,6%|9.614|<br>1,7%|3.528|<br>2,8%|8.646|<br>2,2%|
|**Total**|** 2.274.104**|** 100,0%**|1.194.284|100,0%|551.616|100,0%|126.932|100,0%|401.272|100,0%|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 17-2 Partición Modal Base de Datos PM1**

118

|Modo|Total PM1|Col3|Trabajo|Col5|Estudio 1|Col7|Estudio 2|Col9|Otros|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Caminata**|** 184.846**|**13,9%**|34.417|5,0%|122.012|31,1%|311|0,5%|28.106|15,8%|
|**Autochofer**|** 336.504**|**25,3%**|231.014|33,4%|666|0,2%|6.714|9,9%|98.110|55,3%|
|**Autoacompañante**|** 178.975**|**13,5%**|33.912|4,9%|127.639|32,5%|4.228|6,2%|13.195|7,4%|
|**Taxi**|** 15.466**|**1,2%**|6.110|0,9%|5.436|1,4%|-|0,0%|3.920|2,2%|
|**BusTransantiago**|** 308.310**|**23,2%**|174.233|25,2%|99.041|25,2%|15.006|22,1%|20.030|11,3%|
|**Taxicolectivo**|** 22.773**|**1,7%**|13.358|1,9%|5.300|1,4%|855|1,3%|3.259|1,8%|
|**Metro**|** 69.003**|**5,2%**|41.264|6,0%|9.507|2,4%|15.615|23,0%|2.618|1,5%|
|**Metro-BusTransantiago**|** 158.310**|**11,9%**|114.650|16,6%|17.761|4,5%|21.779|32,0%|4.119|2,3%|
|**Metro-Taxicolectivo**|** 10.631**|**0,8%**|7.726|1,1%|1.392|0,4%|1.035|1,5%|478|0,3%|
|**Bicicleta**|** 44.878**|**3,4%**|35.159|5,1%|3.736|1,0%|2.476|3,6%|3.508|2,0%|
|**Total**|** 1.329.695**|**100,0%**|691.843|100,0%|392.490|100,0%|68.021|100,0%|177.341|100,0%|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 17-3 Partición Modal Base de Datos PM2**

119

|Modo|Total PM2|Col3|Trabajo|Col5|Estudio 1|Col7|Estudio 2|Col9|Otros|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Caminata**|** 189.064**|**20,0%**|50.867|10,1%|77.147|48,5%|1.275|2,2%|59.774|26,7%|
|**Autochofer**|** 243.227**|**25,8%**|161.082|32,1%|372|0,2%|5.127|8,7%|76.645|34,2%|
|**Autoacompañante**|** 68.490**|**7,3%**|20.442|4,1%|34.672|21,8%|4.181|7,1%|9.195|4,1%|
|**Taxi**|** 17.526**|**1,9%**|8.148|1,6%|1.865|1,2%|34|0,1%|7.479|3,3%|
|**BusTransantiago**|** 180.229**|**19,1%**|94.776|18,9%|32.802|20,6%|11.519|19,6%|41.131|18,4%|
|**Taxicolectivo**|** 23.006**|**2,4%**|11.542|2,3%|2.842|1,8%|947|1,6%|7.675|3,4%|
|**Metro**|** 68.092**|**7,2%**|45.657|9,1%|1.057|0,7%|16.026|27,2%|5.353|2,4%|
|**Metro-BusTransantiago**|** 102.958**|**10,9%**|71.174|14,2%|2.491|1,6%|18.277|31,0%|11.016|4,9%|
|**Metro-Taxicolectivo**|** 7.758**|**0,8%**|6.762|1,3%|-|0,0%|472|0,8%|524|0,2%|
|**Bicicleta**|** 44.059**|**4,7%**|31.990|6,4%|5.879|3,7%|1.052|1,8%|5.138|2,3%|
|**Total**|** 944.409**|**100,0%**|502.441|100,0%|159.126|100,0%|58.911|100,0%|223.931|100,0%|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 17-4 Partición Modal ESTRAUS PM Total**

120

|Modo|Total|Col3|Trabajo|Col5|Estudio 1|Col7|Estudio 2|Col9|Otros|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Caminata**|** 382.827**|** 16,0%**|80.159|<br>6,2%|209.851|36,9%|2.110|<br>1,6%|90.708|21,9%|
|**Autochofer**|** 626.694**|** 26,1%**|428.342|33,4%|-|0,0%|10.344|<br>7,9%|188.009|45,3%|
|**Autoacompañante**|** 228.306**|<br>**9,5%**|42.240|<br>3,3%|158.977|27,9%|8.386|<br>6,4%|18.703|<br>4,5%|
|**Taxi**|** 18.881**|<br>**0,8%**|9.046|<br>0,7%|3.523|<br>0,6%|-|0,0%|6.312|<br>1,5%|
|**BusTransantiago**|** 513.732**|** 21,4%**|287.053|22,4%|138.854|24,4%|28.603|21,9%|59.222|14,3%|
|**Taxicolectivo**|** 74.750**|<br>**3,1%**|51.755|<br>4,0%|4.938|<br>0,9%|789|<br>0,6%|17.269|<br>4,2%|
|**Metro**|** 162.162**|<br>**6,8%**|97.792|<br>7,6%|19.914|<br>3,5%|32.102|24,6%|12.355|<br>3,0%|
|**Metro-BusTransantiago**|** 264.814**|** 11,0%**|178.823|13,9%|27.604|<br>4,9%|42.830|32,8%|15.556|<br>3,8%|
|**Metro-Taxicolectivo**|** 21.458**|<br>**0,9%**|20.186|<br>1,6%|217|<br>0,0%|986|<br>0,8%|70|<br>0,0%|
|**Bicicleta**|** 104.441**|<br>**4,4%**|88.488|<br>6,9%|4.984|<br>0,9%|4.351|<br>3,3%|6.618|<br>1,6%|
|**Total**|** 2.398.065**|** 100,0%**|1.283.884|100,0%|568.862|100,0%|130.501|100,0%|414.822|100,0%|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 17-5 Partición Modal ESTRAUS PM1**

121

|Modo|Total|Col3|Trabajo|Col5|Estudio 1|Col7|Estudio 2|Col9|Otros|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Caminata**|** 175.571**|** 12,9%**|30.305|<br>4,2%|117.502|30,7%|444|<br>0,6%|27.320|14,4%|
|**Autochofer**|** 357.314**|** 26,2%**|244.250|33,7%|-|0,0%|5.975|<br>8,6%|107.089|56,6%|
|**Autoacompañante**|** 162.575**|** 11,9%**|27.606|<br>3,8%|118.811|31,0%|4.498|<br>6,5%|11.660|<br>6,2%|
|**Taxi**|** 8.787**|<br>**0,6%**|3.971|<br>0,5%|2.638|<br>0,7%|-|0,0%|2.178|<br>1,2%|
|**BusTransantiago**|** 312.854**|** 22,9%**|176.897|24,4%|100.351|26,2%|15.474|22,4%|20.132|10,6%|
|**Taxicolectivo**|** 38.906**|<br>**2,8%**|28.265|<br>3,9%|4.319|<br>1,1%|392|<br>0,6%|5.930|<br>3,1%|
|**Metro**|** 84.266**|<br>**6,2%**|48.036|<br>6,6%|15.650|<br>4,1%|15.179|21,9%|5.401|<br>2,9%|
|**Metro-BusTransantiago**|** 158.832**|** 11,6%**|107.130|14,8%|21.539|<br>5,6%|23.236|33,6%|6.927|<br>3,7%|
|**Metro-Taxicolectivo**|** 13.082**|<br>**1,0%**|11.874|<br>1,6%|217|<br>0,1%|963|<br>1,4%|28|<br>0,0%|
|**Bicicleta**|** 53.794**|<br>**3,9%**|46.350|<br>6,4%|1.706|<br>0,4%|3.053|<br>4,4%|2.685|<br>1,4%|
|**Total**|** 1.365.981**|** 100,0%**|724.684|100,0%|382.733|100,0%|69.214|100,0%|189.350|100,0%|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 17-6 Partición Modal ESTRAUS PM2**

122

|Modo|Total|Col3|Trabajo|Col5|Estudio 1|Col7|Estudio 2|Col9|Otros|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Caminata**|** 207.282**|** 20,1%**|49.862|<br>8,9%|92.364|49,6%|1.666|<br>2,7%|63.391|28,1%|
|**Autochofer**|** 269.420**|** 26,1%**|184.129|32,9%|-|0,0%|4.368|<br>7,1%|80.923|35,9%|
|**Autoacompañante**|** 65.745**|<br>**6,4%**|14.640|<br>2,6%|40.173|21,6%|3.888|<br>6,3%|7.043|<br>3,1%|
|**Taxi**|** 10.096**|<br>**1,0%**|5.076|<br>0,9%|886|<br>0,5%|-|0,0%|4.134|<br>1,8%|
|**BusTransantiago**|** 200.916**|** 19,5%**|110.187|19,7%|38.510|20,7%|13.129|21,4%|39.090|17,3%|
|**Taxicolectivo**|** 35.852**|<br>**3,5%**|23.496|<br>4,2%|620|<br>0,3%|397|<br>0,6%|11.339|<br>5,0%|
|**Metro**|** 77.899**|<br>**7,5%**|49.757|<br>8,9%|4.265|<br>2,3%|16.923|27,6%|6.954|<br>3,1%|
|**Metro-BusTransantiago**|** 105.988**|** 10,3%**|71.699|12,8%|6.066|<br>3,3%|19.594|32,0%|8.629|<br>3,8%|
|**Metro-Taxicolectivo**|** 8.377**|<br>**0,8%**|8.312|<br>1,5%|-|0,0%|23|<br>0,0%|42|<br>0,0%|
|**Bicicleta**|** 50.682**|<br>**4,9%**|42.173|<br>7,5%|3.278|<br>1,8%|1.298|<br>2,1%|3.934|<br>1,7%|
|**Total**|** 1.032.257**|** 100,0%**|559.331|100,0%|186.162|100,0%|61.286|100,0%|225.479|100,0%|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**17.1.2** **Flujos en Metro**

123

A continuación, se presentan los flujos modelados a lo largo de cada una de las

líneas de metro, comparándolas con los reportados por Metro. Se puede apreciar como el

ajuste es remarcablemente bueno, especialmente para los sentidos más cargados.

**Ilustración 17-1 Perfil de Viajes L1 PM 2012, sentido Oriente-Poniente**

Fuente: Metro/Elaboración propia.

**Ilustración 17-2 Perfil de Viajes L1 PM 2012, sentido Poniente-Oriente**

Fuente: Metro/Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 17-3 Perfil de Viajes L2 PM 2012, sentido Sur-Norte**

Fuente: Metro/Elaboración propia.

**Ilustración 17-4 Perfil de Viajes L2 PM 2012, sentido Norte-Sur**

Fuente: Metro/Elaboración propia.

124

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 17-5 Perfil de Viajes L4 PM 2012, sentido Sur-Norte**

Fuente: Metro/Elaboración propia.

**Ilustración 17-6 Perfil de Viajes L4 PM 2012, sentido Norte-Sur**

Fuente: Metro/Elaboración propia.

125

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 17-7 Perfil de Viajes L4A PM 2012, sentido Poniente-Oriente**

Fuente: Metro/Elaboración propia.

**Ilustración 17-8 Perfil de Viajes L4A PM 2012, sentido Oriente-Poniente**

Fuente: Metro/Elaboración propia.

126

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 17-9 Perfil de Viajes L5 PM 2012, sentido Poniente-Oriente**

Fuente: Metro/Elaboración propia.

**Ilustración 17-10 Perfil de Viajes L5 PM 2012, sentido Oriente-Poniente**

Fuente: Metro/Elaboración propia.

**17.2** **Validación del Modelo en Fuera de Punta**

**17.2.1** **Partición Modal**

127

En las siguientes tablas se presentan las particiones modales objetivos y aquellas

obtenidas a partir de ESTRAUS para el año 2012, periodo Fuera de Punta. Cabe destacar que

el número de viajes asignados es mayor al de la base de datos de la EOD 2012, pues se

incluyen viajes fijos en AutoChofer (que representan viajes en MotoChofer, Furgón Escolar

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

128

Pasajero y partes de viajes en combinaciones de AutoChofer no modeladas), Bus Transantiago

(que representan partes de viajes en combinaciones de BusTransantiago no modeladas) y Metro

(que representan partes de viajes en combinaciones de Metro no modeladas).

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 17-7 Partición Modal Base de Datos FP**

129

|Modo|Total FP|Col3|Trabajo|Col5|Estudio|Col7|Vuelta a Casa|Col9|Compras|Col11|Otros|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Caminata**|**144.076**|**25,0%**|16.904|<br>12,0%|4.068|10,9%|31.569|39,5%|60.991|48,2%|30.544|15,9%|
|**Autochofer**|**142.647**|**24,7%**|58.644|<br>41,5%|6.992|18,8%|17.577|22,0%|23.168|18,3%|36.268|18,9%|
|**Autoacompañante**|**24.593**|**4,3%**|2.965|<br>2,1%|1.835|4,9%|3.640|4,6%|7.435|5,9%|8.718|4,5%|
|**Taxi**|**15.882**|**2,8%**|2.147|<br>1,5%|-|0,0%|3.458|4,3%|1.216|1,0%|9.060|4,7%|
|**BusTransantiago**|**113.555**|**19,7%**|27.698|<br>19,6%|7.431|19,9%|8.308|10,4%|15.562|12,3%|54.557|28,4%|
|**Taxicolectivo**|**33.956**|**5,9%**|5.157|<br>3,6%|626|1,7%|5.857|7,3%|6.300|5,0%|16.016|8,3%|
|**Metro**|**46.357**|**8,0%**|10.047|<br>7,1%|4.333|11,6%|4.629|5,8%|4.256|3,4%|23.091|12,0%|
|**Metro-BusTransantiago**|**37.740**|**6,5%**|13.210|<br>9,3%|9.991|26,8%|3.182|4,0%|1.715|1,4%|9.643|5,0%|
|**Metro-Taxicolectivo**|**5.670**|**1,0%**|1.098|<br>0,8%|261|0,7%|144|0,2%|1.595|1,3%|2.572|1,3%|
|**Bicicleta**|**12.668**|**2,2%**|3.559|<br>2,5%|1.748|4,7%|1.549|1,9%|4.361|3,4%|1.452|0,8%|
|**Total**|**577.144**|**100,0%**|141.427|100,0%|37.286|100,0%|79.913|100,0%|126.599|100,0%|191.920|100,0%|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 17-8 Partición Modal ESTRAUS FP**

130

|Modo|Total|Col3|Trabajo|Col5|Estudio|Col7|Vuelta a Casa|Col9|Compras|Col11|Otros|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Caminata**|** 90.648**|<br>**14,1%**|11.096|<br>6,9%|7.141|<br>16,9%|16.201|<br>18,3%|35.019|<br>26,2%|21.192|<br>9,8%|
|**Autochofer**|** 233.004**|<br>**36,3%**|71.147|<br>44,2%|5.823|<br>13,7%|36.613|<br>41,5%|50.875|<br>38,1%|68.545|<br>31,6%|
|**Autoacompañante**|** 16.095**|<br>**2,5%**|2.044|<br>1,3%|1.893|<br>4,5%|1.668|<br>1,9%|4.127|<br>3,1%|6.362|<br>2,9%|
|**Taxi**|** 15.824**|<br>**2,5%**|1.336|<br>0,8%|6.759|<br>16,0%|3.059|<br>3,5%|1.035|<br>0,8%|3.635|<br>1,7%|
|**BusTransantiago**|** 109.332**|<br>**17,0%**|27.479|<br>17,1%|5.176|<br>12,2%|12.259|<br>13,9%|21.528|<br>16,1%|42.890|<br>19,8%|
|**Taxicolectivo**|** 34.691**|<br>**5,4%**|2.417|<br>1,5%|212|<br>0,5%|3.179|<br>3,6%|4.296|<br>3,2%|24.588|<br>11,3%|
|**Metro**|** 50.452**|<br>**7,9%**|14.089|<br>8,7%|3.893|<br>9,2%|8.123|<br>9,2%|5.359|<br>4,0%|18.988|<br>8,8%|
|**Metro-BusTransantiago**|** 25.456**|<br>**4,0%**|7.289|<br>4,5%|2.577|<br>6,1%|1.007|<br>1,1%|916|<br>0,7%|13.668|<br>6,3%|
|**Metro-Taxicolectivo**|** 9.330**|<br>**1,5%**|632|<br>0,4%|95|<br>0,2%|128|<br>0,1%|260|<br>0,2%|8.217|<br>3,8%|
|**Bicicleta**|** 57.528**|<br>**9,0%**|23.526|<br>14,6%|8.797|<br>20,8%|6.085|<br>6,9%|10.188|<br>7,6%|8.932|<br>4,1%|
|**Total**|** 642.309**|** 100,0%**|161.040|100,0%|42.367|100,0%|88.318|100,0%|133.594|100,0%|216.991|100,0%|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**17.2.2** **Flujos en Metro**

131

A continuación, se presentan los flujos modelados a lo largo de cada una de las

líneas de metro, comparándolas con los reportados por Metro.

Se puede observar que, en general, los perfiles de flujos de metro modelados son

de menor magnitud que los reportados por el operador. A este respecto, cabe señalar que un

resultado similar se observó cuando se comparó, para el período Fuera de Punta, los flujos

reportados por el operador con los flujos **obtenidos al asignar a la red de metro las**

**Matrices obtenidas directamente de la EOD** (viajes OD observados por la EOD). Estos

resultados se reportan en el Capítulo 10 del presente informe (ver Ilustraciones 10-70 a 10-78).

Por lo tanto, los resultados de la modelación reproducen las características de la información

utilizada para calibrar los modelos de ESTRAUS.

Existen varias explicaciones de por qué se da este resultado en la EOD y, por

consiguiente, en la aplicación de los modelos recalibrados. En particular, existen viajes que no

son incluidos en la EOD y que especialmente se dan en el período fuera de punta. Estos

corresponden a viajes “externos”, que se generan en zonas externas al área modelada y viajes

especiales de pasajeros turistas y otros no incluidos en la EOD.

En consecuencia, para reproducir adecuadamente los flujos observados en estos

períodos sería necesario agregar a la asignación modelada los viajes no incluidos en la EOD.

Si corrigiéramos los modelos para reproducir los viajes reportados por el operador, estaríamos

introduciendo sesgos que afectarían a las predicciones futuras. La modelación debe reproducir

lo que se observó en la EOD, que fue la base para la calibración de los modelos, que en la

práctica es lo que se logra.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 17-11 Perfil de Viajes L1 FP 2012, sentido Oriente-Poniente**

Fuente: Metro/Elaboración propia.

**Ilustración 17-12 Perfil de Viajes L1 FP 2012, sentido Poniente-Oriente**

Fuente: Metro/Elaboración propia.

132

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 17-13 Perfil de Viajes L2 FP 2012, sentido Sur-Norte**

Fuente: Metro/Elaboración propia.

**Ilustración 17-14 Perfil de Viajes L2 FP 2012, sentido Norte-Sur**

Fuente: Metro/Elaboración propia.

133

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 17-15 Perfil de Viajes L4 FP 2012, sentido Sur-Norte**

Fuente: Metro/Elaboración propia.

**Ilustración 17-16 Perfil de Viajes L4 FP 2012, sentido Norte-Sur**

Fuente: Metro/Elaboración propia.

134

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 17-17 Perfil de Viajes L4A FP 2012, sentido Poniente-Oriente**

Fuente: Metro/Elaboración propia.

**Ilustración 17-18 Perfil de Viajes L4A FP 2012, sentido Oriente-Poniente**

Fuente: Metro/Elaboración propia.

135

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 17-19 Perfil de Viajes L5 FP 2012, sentido Poniente-Oriente**

Fuente: Metro/Elaboración propia.

**Ilustración 17-20 Perfil de Viajes L5 FP 2012, sentido Oriente-Poniente**

Fuente: Metro/Elaboración propia.

**17.3** **Validación del Modelo en Punta Tarde**

**17.3.1** **Partición Modal**

136

En las siguientes tablas se presentan las particiones modales objetivos y aquellas

obtenidas a partir de ESTRAUS para el año 2012, periodo Punta Tarde. Cabe destacar que el

número de viajes asignados es mayor al de la base de datos de la EOD 2012, pues se incluyen

viajes fijos en AutoChofer (que representan viajes en MotoChofer, Furgón Escolar Pasajero y

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

137

partes de viajes en combinaciones de AutoChofer no modeladas), Bus Transantiago (que

representan partes de viajes en combinaciones de BusTransantiago no modeladas) y Metro

(que representan partes de viajes en combinaciones de Metro no modeladas).

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 17-9 Partición Modal Base de Datos PT**

138

|Modo|Total PT|Col3|Trabajo y Estudio|Col5|Vuelta a Casa|Col7|Compras|Col9|Otros|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Caminata**|** 213.021**|** 20,8%**|80.871|12,5%|66.763|34,0%|37.705|50,1%|27.682|25,5%|
|**Autochofer**|** 254.345**|** 24,8%**|165.708|25,7%|38.452|19,6%|13.978|18,6%|36.207|33,4%|
|**Autoacompañante**|** 61.899**|<br>**6,0%**|27.141|<br>4,2%|16.504|<br>8,4%|7.801|10,4%|10.453|<br>9,6%|
|**Taxi**|** 19.593**|<br>**1,9%**|4.882|<br>0,8%|7.305|<br>3,7%|4.050|<br>5,4%|3.356|<br>3,1%|
|**BusTransantiago**|** 191.596**|** 18,7%**|144.358|22,4%|29.046|14,8%|6.467|<br>8,6%|11.725|10,8%|
|**Taxicolectivo**|** 26.269**|<br>**2,6%**|11.786|<br>1,8%|11.152|<br>5,7%|1.011|<br>1,3%|2.320|<br>2,1%|
|**Metro**|** 88.198**|<br>**8,6%**|69.531|10,8%|11.107|<br>5,6%|1.917|<br>2,5%|5.642|<br>5,2%|
|**Metro-BusTransantiago**|** 112.275**|** 10,9%**|97.496|15,1%|9.721|<br>4,9%|532|<br>0,7%|4.526|<br>4,2%|
|**Metro-Taxicolectivo**|** 6.165**|<br>**0,6%**|5.294|<br>0,8%|322|<br>0,2%|54|<br>0,1%|494|<br>0,5%|
|**Bicicleta**|** 52.366**|<br>**5,1%**|38.267|<br>5,9%|6.232|<br>3,2%|1.736|<br>2,3%|6.131|<br>5,6%|
|**Total**|** 1.025.727**|** 100,0%**|645.334|100,0%|196.604|100,0%|75.251|100,0%|108.537|100,0%|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 17-10 Partición Modal ESTRAUS PT**

139

|Modo|Total|Col3|Trabajo y Estudio|Col5|Vuelta a Casa|Col7|Compras|Col9|Otros|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Caminata**|** 101.995**|<br>**9,9%**|51.408|<br>7,6%|20.363|<br>10,1%|25.075|<br>33,9%|5.149|<br>7,0%|
|**Autochofer**|** 317.206**|<br>**30,8%**|192.940|<br>28,3%|76.299|<br>37,9%|25.416|<br>34,3%|22.550|<br>30,5%|
|**Autoacompañante**|** 35.499**|<br>**3,4%**|19.259|<br>2,8%|8.477|<br>4,2%|4.810|<br>6,5%|2.953|<br>4,0%|
|**Taxi**|** 10.853**|<br>**1,1%**|1.751|<br>0,3%|5.417|<br>2,7%|2.700|<br>3,6%|985|<br>1,3%|
|**BusTransantiago**|** 243.651**|<br>**23,7%**|180.482|<br>26,5%|31.228|<br>15,5%|9.959|<br>13,4%|21.982|<br>29,7%|
|**Taxicolectivo**|** 55.443**|<br>**5,4%**|30.861|<br>4,5%|21.332|<br>10,6%|792|<br>1,1%|2.459|<br>3,3%|
|**Metro**|** 104.492**|<br>**10,1%**|75.358|<br>11,1%|15.666|<br>7,8%|3.106|<br>4,2%|10.362|<br>14,0%|
|**Metro-BusTransantiago**|** 82.753**|<br>**8,0%**|67.205|<br>9,9%|10.991|<br>5,5%|395|<br>0,5%|4.162|<br>5,6%|
|**Metro-Taxicolectivo**|** 23.344**|<br>**2,3%**|14.692|<br>2,2%|7.105|<br>3,5%|80|<br>0,1%|1.467|<br>2,0%|
|**Bicicleta**|** 55.532**|<br>**5,4%**|47.449|<br>7,0%|4.384|<br>2,2%|1.717|<br>2,3%|1.983|<br>2,7%|
|**Total**|** 1.030.047**|** 100,0%**|680.699|100,0%|201.248|100,0%|74.049|100,0%|74.050|100,0%|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**17.3.2** **Flujos en Metro**

140

A continuación, se presentan los flujos modelados a lo largo de cada una de las

líneas de metro, comparándolas con los reportados por Metro.

Se puede observar que, en general, los perfiles de flujos de metro modelados son

de menor magnitud que los reportados por el operador, al igual que lo sucedido en Fuera de

Punta. A este respecto, cabe señalar que un resultado similar se observó cuando se comparó,

para el período Punta Tarde, los flujos reportados por el operador con los flujos **obtenidos al**

**asignar a la red de metro las Matrices obtenidas directamente de la EOD** (viajes

OD observados por la EOD). Estos resultados se reportan en el Capítulo 10 del presente

informe. Por lo tanto, los resultados de la modelación reproducen las características de la

información utilizada para calibrar los modelos de ESTRAUS.

Existen varias explicaciones de por qué se da este resultado en la EOD y, por

consiguiente, en la aplicación de los modelos recalibrados. En particular, existen viajes que no

son incluidos en la EOD y que especialmente se dan en el período punta tarde. Estos

corresponden a viajes “externos”, que se generan en zonas externas al área modelada y viajes

especiales de pasajeros turistas y otros no incluidos en la EOD.

En consecuencia, para reproducir adecuadamente los flujos observados en estos

períodos sería necesario agregar a la asignación modelada los viajes no incluidos en la EOD.

Si corrigiéramos los modelos para reproducir los viajes reportados por el operador, estaríamos

introduciendo sesgos que afectarían a las predicciones futuras. La modelación debe reproducir

lo que se observó en la EOD, que fue la base para la calibración de los modelos, que en la

práctica es lo que se logra.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 17-21 Perfil de Viajes L1 PT 2012, sentido Oriente-Poniente**

Fuente: Metro/Elaboración propia.

**Ilustración 17-22 Perfil de Viajes L1 PT 2012, sentido Poniente-Oriente**

Fuente: Metro/Elaboración propia.

141

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 17-23 Perfil de Viajes L2 PT 2012, sentido Sur-Norte**

Fuente: Metro/Elaboración propia.

**Ilustración 17-24 Perfil de Viajes L2 PT 2012, sentido Norte-Sur**

Fuente: Metro/Elaboración propia.

142

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 17-25 Perfil de Viajes L4 PT 2012, sentido Sur-Norte**

Fuente: Metro/Elaboración propia.

**Ilustración 17-26 Perfil de Viajes L4 PT 2012, sentido Norte-Sur**

Fuente: Metro/Elaboración propia.

143

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 17-27 Perfil de Viajes L4A PT 2012, sentido Poniente-Oriente**

Fuente: Metro/Elaboración propia.

**Ilustración 17-28 Perfil de Viajes L4A PT 2012, sentido Oriente-Poniente**

Fuente: Metro/Elaboración propia.

144

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Ilustración 17-29 Perfil de Viajes L5 PT 2012, sentido Poniente-Oriente**

Fuente: Metro/Elaboración propia.

**Ilustración 17-30 Perfil de Viajes L5 PT 2012, sentido Oriente-Poniente**

Fuente: Metro/Elaboración propia.

145

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

146

# 18 A NÁLISIS DEL S ISTEMA DE T RANSPORTE EN UN C ORTE T EMPORAL F UTURO (T AREA 18)

**18.1** **Definiciones Previas**

Para analizar el sistema de transporte en el futuro, se debe comenzar por

determinar cortes apropiados para el análisis. Dado que la calibración se basa en el año 2012,

el primer corte propuesto es el 2018 (situación actual). Dicho corte permite comparar los

resultados obtenidos con datos reales, como los perfiles de carga del metro. Adicionalmente,

también se proponen los cortes futuros 2020 y 2025. Todos estos cortes se codificaron en los

tres periodos modelados: Punta Mañana, Fuera de Punta y Punta Tarde.

En cada uno de los cortes se efectuaron cambios sobre la red de transporte de

2012, de forma de reflejar la situación actual (para 2018) y las situaciones esperadas (2020

y 2025). Estos incluyen cambios en estructuras tarifarias y la implementación de proyectos, los

cuales se detallan en la tabla a continuación.

**Tabla 18-1 Cambios por Corte Temporal**

Corredor Vicuña Mackenna Túnel Cerro Renca (Lo Ruiz)

Corredor Rinconada Prolongación Costanera Norte

Kennedy - Costanera Norte Corredor Independencia

Manquehue - Kennedy Extensión Línea 2 de Metro

Costanera Sur **2025** Extensión Línea 3 de Metro

Costanera Norte - Ruta 5 Extensión Línea 6 de Metro

Costanera Norte - Gral. Velásquez Terceras Pistas Ruta 78

|Corte|Nombre|
|---|---|
|**2018**|Línea 6 de Metro|
|**2018**|Cambio Tarifa Metrotrén|
|**2018**|Tramo Urbano Ruta 5 Norte|
|**2018**|Corredor Vicuña Mackenna|
|**2018**|Corredor Rinconada|
|**2018**|Kennedy - Costanera Norte|
|**2018**|Túnel Kennedy|
|**2018**|Manquehue - Kennedy|
|**2018**|Costanera Sur|
|**2018**|Costanera Norte - Ruta 5|
|**2018**|Costanera Norte - Gral. Velásquez|
|**2018**|Ruta 5 - Centro|

|Corte|Nombre|
|---|---|
|**2018**|Salida La Concepción|
|**2018**|Cambio Velocidad Máxima Urbana|
|**2020**|Línea 3 de Metro|
|**2020**|Túnel Cerro Renca (Lo Ruiz)|
|**2020**|Prolongación Costanera Norte|
|**2020**|Corredor Independencia|
|**2025**|Línea 7 de Metro|
|**2025**|Extensión Línea 2 de Metro|
|**2025**|Extensión Línea 3 de Metro|
|**2025**|Extensión Línea 6 de Metro|
|**2025**|Terceras Pistas Ruta 78|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

147

Además de los proyectos, es necesario determinar un nuevo patrón y magnitud de

viajes en las zonas modeladas. Para ello se aplican los modelos de generación y atracción de

viajes definidos en la Tarea 12: Calibración de Modelos de Generación y Atracción, pero con

variables independientes proyectadas para los cortes futuros [10] . La base de datos para este fin

fue proporcionada por SECTRA, y se divide en tres áreas: hogares, matrículas y uso de suelo.

**18.2** **Comparación Resultados 2012, 2020 y 2025**

**18.2.1** **Punta Mañana**

En la presente sección se aprecian las variaciones de los principales resultados del

periodo PM a lo largo de los diferentes cortes temporales. A continuación, se exhiben las

variaciones en los viajes por modo.

**Tabla 18-2 Progresión de la Partición Modal PM Total**

|Modo|2012|2012-2020|2020|2020-2025|2025|
|---|---|---|---|---|---|
|**Caminata**|259.068|<br>-6,0%|243.479|<br>74,0%|423.621|
|**Autochofer**|729.571|<br>34,8%|983.508|<br>22,8%|1.207.704|
|**Autoacompañante**|205.418|<br>-33,1%|137.511|<br>310,2%|564.119|
|**Taxi**|19.002|<br>139,1%|45.435|<br>-55,3%|20.318|
|**BusTransantiago**|546.987|<br>-49,5%|276.028|<br>138,0%|657.078|
|**Taxicolectivo**|139.889|<br>-5,5%|132.205|<br>-13,2%|114.811|
|**Metro**|144.530|<br>-11,5%|127.881|<br>157,1%|328.828|
|**Metro-BusTransantiago**|183.968|<br>-29,3%|130.139|<br>55,2%|201.939|
|**Metro-Taxicolectivo**|70.364|<br>15,7%|81.378|<br>-11,7%|71.830|
|**Bicicleta**|99.298|<br>284,9%|382.152|<br>-61,8%|146.070|
|**Total**|** 2.389.046**|<br>**5,9%**|** 2.529.022**|<br>**45,0%**|** 3.667.451**|
|**No Motorizado**|358.366|<br>74,6%|625.631|<br>-8,9%|569.691|
|**Transporte Público**|1.085.738|<br>-31,1%|747.631|<br>83,8%|1.374.486|
|**Transporte Privado**|953.991|<br>22,3%|1.166.454|<br>53,6%|1.792.141|

Fuente: Elaboración propia.

Como se puede apreciar, los modos de transporte privado sufren incrementos

significativos a lo largo del tiempo, al contrario de los modos de transporte público. La

10 Este procedimiento se aplicó a los cortes 2020 y 2025, pero el corte 2018 se elaboró con una metodología

alternativa de tasas de crecimiento poblacional.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

148

excepción es Metro, que presenta una fuerte alza en sus viajes entre 2020 y 2025, atribuible

a la habilitación de las extensiones de la Línea 2 (4 estaciones hacia el sur), Línea 3 (3

estaciones hacia el norponiente) y Línea 6 (1 estación hacia el nororiente); y la implementación

de la Línea 7 (19 estaciones, trazado entre Renca y Vitacura).

**Tabla 18-3 Progresión de la Partición Modal PM1**

|Modo|2012|2012-2020|2020|2020-2025|2025|
|---|---|---|---|---|---|
|**Caminata**|133.059|<br>-1,5%|131.095|<br>74,7%|228.991|
|**Autochofer**|430.639|<br>49,3%|643.148|<br>8,7%|699.317|
|**Autoacompañante**|153.735|<br>-73,7%|40.363|<br>945,8%|422.126|
|**Taxi**|8.767|<br>119,0%|19.199|<br>-46,3%|10.301|
|**BusTransantiago**|308.311|<br>-56,5%|134.114|<br>181,0%|376.847|
|**Taxicolectivo**|70.962|<br>-12,2%|62.293|<br>-6,0%|58.543|
|**Metro**|76.758|<br>-14,4%|65.708|<br>185,8%|187.763|
|**Metro-BusTransantiago**|101.462|<br>-31,3%|69.742|<br>65,2%|115.248|
|**Metro-Taxicolectivo**|37.630|<br>1,4%|38.143|<br>3,4%|39.421|
|**Bicicleta**|51.072|<br>278,0%|193.073|<br>-60,2%|76.841|
|**Total**|** 1.370.300**|<br>**1,7%**|** 1.393.476**|<br>**57,7%**|** 2.197.134**|
|**No Motorizado**|184.131|<br>76,1%|324.168|<br>-5,7%|305.832|
|**Transporte Público**|595.123|<br>-37,8%|370.000|<br>110,2%|777.822|
|**Transporte Privado**|593.141|<br>18,5%|702.710|<br>61,1%|1.131.744|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 18-4 Progresión de la Partición Modal PM2**

149

|Modo|2012|2012-2020|2020|2020-2025|2025|
|---|---|---|---|---|---|
|**Caminata**|126.029|<br>-10,8%|112.410|<br>73,3%|194.776|
|**Autochofer**|298.971|<br>13,9%|340.480|<br>49,6%|509.231|
|**Autoacompañante**|51.694|<br>87,9%|97.151|<br>47,1%|142.895|
|**Taxi**|10.236|<br>156,3%|26.239|<br>-61,8%|10.032|
|**BusTransantiago**|238.706|<br>-40,5%|141.927|<br>97,6%|280.473|
|**Taxicolectivo**|68.936|<br>1,4%|69.917|<br>-19,4%|56.327|
|**Metro**|67.774|<br>-8,3%|62.174|<br>126,9%|141.096|
|**Metro-BusTransantiago**|82.509|<br>-26,8%|60.399|<br>43,6%|86.711|
|**Metro-Taxicolectivo**|32.735|<br>32,1%|43.236|<br>-25,0%|32.414|
|**Bicicleta**|48.259|<br>291,9%|189.124|<br>-63,3%|69.369|
|**Total**|** 1.024.319**|<br>**11,4%**|** 1.141.084**|<br>**32,2%**|** 1.508.637**|
|**No Motorizado**|174.288|<br>73,0%|301.534|<br>-12,4%|264.145|
|**Transporte Público**|490.660|<br>-23,0%|377.653|<br>58,1%|597.021|
|**Transporte Privado**|360.901|<br>28,5%|463.870|<br>42,7%|662.158|

Fuente: Elaboración propia.

Se puede notar como entre los dos horarios los cambios son relativamente

consistentes, al tiempo que en general el horario 1 presenta un 25% más de viajes que el horario

2.

A continuación, se exhiben los cambios en las velocidades de viaje para cada

modo motorizado a lo largo de los cortes temporales. Se considera que esta variable es la más

representativa respecto a los cambios en la red, pues trae implícita la congestión en las vías y

en los vehículos (por mayores tiempos de espera en los modos de transporte público).

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 18-5 Progresión de las Velocidades (km/h) PM1**

150

|Modo|2012|2012-2020|2020|2020-2025|2025|
|---|---|---|---|---|---|
|**Autochofer**|21,2|<br>-20,8%|16,8|<br>-24,2%|12,7|
|**Autoacompañante**|22,6|<br>-13,7%|19,5|<br>-20,2%|15,6|
|**Taxi**|20,6|<br>-16,5%|17,2|<br>-15,7%|14,5|
|**BusTransantiago**|16,3|<br>-14,7%|13,9|<br>-16,1%|11,7|
|**Taxicolectivo**|16,9|<br>-17,8%|13,9|<br>-23,5%|10,6|
|**Metro**|34,1|<br>13,5%|38,7|<br>-2,1%|37,9|
|**Metro-BusTransantiago**|26,1|<br>0,0%|26,1|<br>-4,8%|24,8|
|**Metro-Taxicolectivo**|28,8|<br>-3,1%|27,9|<br>-7,6%|25,8|

Fuente: Elaboración propia.

**Tabla 18-6 Progresión de las Velocidades (km/h) PM2**

|Modo|2012|2012-2020|2020|2020-2025|2025|
|---|---|---|---|---|---|
|**Autochofer**|31,3|-22,4%|24,3|-26,4%|17,9|
|**Autoacompañante**|30,8|-17,2%|25,5|-23,1%|19,6|
|**Taxi**|27,4|-23,7%|20,9|-22,3%|16,2|
|**BusTransantiago**|22,0|-18,6%|17,9|-19,5%|14,4|
|**Taxicolectivo**|25,7|-21,0%|20,3|-25,1%|15,2|
|**Metro**|35,0|10,9%|38,8|-1,9%|38,1|
|**Metro-BusTransantiago**|29,4|-3,4%|28,4|-3,7%|27,3|
|**Metro-Taxicolectivo**|33,0|-1,2%|32,6|-7,2%|30,3|

Fuente: Elaboración propia.

Se puede notar como en el periodo 2012-2020, las velocidades sufrieron mermas

en el transporte privado y Bus Transantiago. Por el contrario, Metro incrementó su velocidad, lo

que es atribuible a la puesta en marcha de las nuevas Líneas 3 y 6, con estaciones más alejadas

entre sí y velocidades de circulación mayores. En cambio, en el periodo 2020-2025 se aprecia

una significativa reducción en las velocidades de todos los modos, especialmente en el

transporte privado. Estos efectos son consistentes en ambos horarios, aunque levemente

mayores en PM2.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**18.2.2** **Fuera de Punta**

151

En la presente sección se aprecian las variaciones de los principales resultados del

periodo PM a lo largo de los diferentes cortes temporales. A continuación, se exhiben las

variaciones en los viajes por modo.

**Tabla 18-7 Progresión de la Partición Modal FP**

|Modo|2012|2012-2020|2020|2020-2025|2025|
|---|---|---|---|---|---|
|**Caminata**|90.648|<br>2,4%|92.808|<br>2,6%|95.202|
|**Autochofer**|233.004|<br>16,5%|271.394|<br>26,4%|343.162|
|**Autoacompañante**|16.095|<br>29,2%|20.789|<br>30,4%|27.117|
|**Taxi**|15.824|<br>3,0%|16.304|<br>1,2%|16.506|
|**BusTransantiago**|109.332|<br>2,0%|111.568|<br>-3,9%|107.252|
|**Taxicolectivo**|34.691|<br>-0,2%|34.605|<br>-4,0%|33.228|
|**Metro**|50.452|<br>6,3%|53.654|<br>34,0%|71.873|
|**Metro-BusTransantiago**|25.456|<br>13,3%|28.849|<br>-11,3%|25.576|
|**Metro-Taxicolectivo**|9.330|<br>30,7%|12.195|<br>-10,2%|10.953|
|**Bicicleta**|57.528|<br>11,4%|64.067|<br>8,5%|69.524|
|**Total**|** 642.309**|<br>**9,1%**|** 700.758**|<br>**13,3%**|** 793.714**|
|**No Motorizado**|148.176|<br>5,9%|156.875|<br>5,0%|164.726|
|**Transporte Público**|229.261|<br>5,1%|240.871|<br>3,3%|248.882|
|**Transporte Privado**|264.923|<br>16,4%|308.487|<br>25,4%|386.785|

Fuente: Elaboración propia.

Como se puede apreciar, los modos de transporte privado sufren incrementos

significativos y estables a lo largo del tiempo, al contrario de los modos de transporte público.

La excepción es Metro, que presenta una fuerte alza en sus viajes entre 2020 y 2025, atribuible

a la habilitación de las extensiones de la Línea 2 (4 estaciones hacia el sur), Línea 3 (3

estaciones hacia el norponiente) y Línea 6 (1 estación hacia el nororiente); y la implementación

de la Línea 7 (19 estaciones, trazado entre Renca y Vitacura). Sin embargo, la mayor parte de

esos nuevos viajes provienen de usuarios que antes utilizaban modos combinados con metro,

por lo que el uso global de transporte público solo se incrementa un 3,3%.

A continuación, se exhiben los cambios en las velocidades de viaje para cada

modo motorizado a lo largo de los cortes temporales. Se considera que esta variable es la más

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

152

representativa respecto a los cambios en la red, pues trae implícita la congestión en las vías y

en los vehículos (por mayores tiempos de espera en los modos de transporte público).

**Tabla 18-8 Progresión de las Velocidades (km/h) FP**

|Modo|2012|2012-2020|2020|2020-2025|2025|
|---|---|---|---|---|---|
|**Autochofer**|38,9|<br>-4,1%|37,3|<br>-21,9%|29,1|
|**Autoacompañante**|38,9|<br>-3,1%|37,7|<br>-22,4%|29,3|
|**Taxi**|34,5|<br>-9,9%|31,1|<br>-23,2%|23,9|
|**BusTransantiago**|25,3|<br>-5,9%|23,8|<br>-15,4%|20,1|
|**Taxicolectivo**|28,3|<br>4,9%|29,7|<br>-17,3%|24,6|
|**Metro**|35,2|<br>17,3%|41,3|<br>-9,2%|37,5|
|**Metro-BusTransantiago**|28,4|<br>10,6%|31,4|<br>-8,1%|28,9|
|**Metro-Taxicolectivo**|31,2|<br>27,9%|39,9|<br>-9,3%|36,2|

Fuente: Elaboración propia.

Se puede notar como en el periodo 2012-2020, las velocidades sufrieron mermas

relativamente menores en el transporte privado y Bus Transantiago. Por el contrario, Metro

incrementó sustantivamente su velocidad, lo que es atribuible a la puesta en marcha de las

nuevas Líneas 3 y 6, con estaciones más alejadas entre sí y velocidades de circulación mayores.

En cambio, en el periodo 2020-2025 se aprecia una significativa reducción en las velocidades

de todos los modos, especialmente en el transporte privado.

**18.2.3** **Punta Tarde**

En la presente sección se aprecian las variaciones de los principales resultados del

periodo PM a lo largo de los diferentes cortes temporales. A continuación, se exhiben las

variaciones en los viajes por modo.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 18-9 Progresión de la Partición Modal PT**

153

|Modo|2012|2012-2020|2020|2020-2025|2025|
|---|---|---|---|---|---|
|**Caminata**|101.995|<br>2,9%|105.000|<br>7,2%|112.564|
|**Autochofer**|317.206|<br>23,8%|392.793|<br>22,5%|481.326|
|**Autoacompañante**|35.499|<br>29,1%|45.815|<br>21,7%|55.737|
|**Taxi**|10.853|<br>7,6%|11.676|<br>3,0%|12.032|
|**BusTransantiago**|243.651|<br>0,4%|244.709|<br>1,4%|248.177|
|**Taxicolectivo**|55.443|<br>-7,1%|51.533|<br>4,8%|54.003|
|**Metro**|104.492|<br>16,4%|121.677|<br>39,0%|169.104|
|**Metro-BusTransantiago**|82.753|<br>18,2%|97.790|<br>-2,7%|95.115|
|**Metro-Taxicolectivo**|23.344|<br>29,7%|30.284|<br>4,3%|31.600|
|**Bicicleta**|55.532|<br>3,5%|57.460|<br>4,7%|60.155|
|**Total**|** 1.030.047**|<br>**11,8%**|** 1.151.659**|<br>**13,9%**|** 1.311.559**|
|**No Motorizado**|157.527|<br>3,1%|162.460|<br>6,3%|172.719|
|**Transporte Público**|509.683|<br>7,1%|545.993|<br>9,5%|597.999|
|**Transporte Privado**|363.558|<br>23,9%|450.284|<br>21,9%|549.095|

Fuente: Elaboración propia.

Como se puede apreciar, los modos de transporte privado sufren incrementos

significativos y estables a lo largo del tiempo, al contrario de los modos de transporte público.

La excepción es Metro, que presenta una fuerte alza en sus viajes entre 2020 y 2025, atribuible

a la habilitación de las extensiones de la Línea 2 (4 estaciones hacia el sur), Línea 3 (3

estaciones hacia el norponiente) y Línea 6 (1 estación hacia el nororiente); y la implementación

de la Línea 7 (19 estaciones, trazado entre Renca y Vitacura). Sin embargo, la mayor parte de

esos nuevos viajes provienen de usuarios que antes utilizaban modos combinados con metro,

por lo que el uso global de transporte público solo se incrementa un 6,3%.

A continuación, se exhiben los cambios en las velocidades de viaje para cada

modo motorizado a lo largo de los cortes temporales. Se considera que esta variable es la más

representativa respecto a los cambios en la red, pues trae implícita la congestión en las vías y

en los vehículos (por mayores tiempos de espera en los modos de transporte público).

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 18-10 Progresión de las Velocidades (km/h) PT**

154

|Modo|2012|2012-2020|2020|2020-2025|2025|
|---|---|---|---|---|---|
|**Autochofer**|28,5|<br>-7,5%|26,4|<br>-18,1%|21,6|
|**Autoacompañante**|29,9|<br>-8,6%|27,3|<br>-16,6%|22,8|
|**Taxi**|29,7|<br>-15,7%|25,0|<br>-21,7%|19,6|
|**BusTransantiago**|21,0|<br>-6,6%|19,6|<br>-13,4%|17,0|
|**Taxicolectivo**|25,2|<br>-2,9%|24,5|<br>-17,9%|20,1|
|**Metro**|35,9|<br>15,8%|41,6|<br>-7,6%|38,4|
|**Metro-BusTransantiago**|25,3|<br>22,9%|31,1|<br>-6,7%|29,0|
|**Metro-Taxicolectivo**|32,6|<br>9,3%|35,6|<br>-8,8%|32,5|

Fuente: Elaboración propia.

Se puede notar como en el periodo 2012-2020, las velocidades sufrieron mermas

en el transporte privado y Bus Transantiago. Por el contrario, Metro incrementó su velocidad, lo

que es atribuible a la puesta en marcha de las nuevas Líneas 3 y 6, con estaciones más alejadas

entre sí y velocidades de circulación mayores. En cambio, en el periodo 2020-2025 se aprecia

una significativa reducción en las velocidades de todos los modos, especialmente en el

transporte privado.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

# 19 C ÁLCULO DE F ACTORES DE E XPANSIÓN (T AREA 19)

**19.1** **Enfoque Metodológico**

155

Los modelos que se calibraron en este estudio consideran cuatro períodos

operacionales diferentes del sistema de transporte urbano modelado por ESTRAUS. Sin

embargo, para evaluar proyectos o planes de inversión en el sistema de transporte urbano

modelado, se requiere expandir los resultados de los beneficios y/o costos, calculados para

cada uno de los períodos horarios modelados, al total de un año de operación. Así, se obtienen

flujos anuales, a partir de los cuales se puedan calcular los indicadores de VAN y TIR usados

normalmente para valorar la bondad de un proyecto. Lo anterior requiere calcular factores de

expansión para cada período modelado.

Cada uno de los períodos modelados por ESTRAUS representa unas condiciones

operacionales concretas características de un conjunto de horas (Pn) de un día representativo

(Día laboral, fin de semana, día festivo o estival, etc.). El enfoque de modelación supone que

cada una de las horas que componen un período de análisis Pn, presentan condiciones

homogéneas de operación; por lo tanto, todas ellas aportan los mismos beneficios o costos a la

evaluación de un proyecto que se esté analizando.

Para expandir los beneficios o costos de un período modelado (ej. Hora Punta

Mañana) se debe determinar cuántas horas de este tipo existen en un año. Para ello se

determina primero cuantas horas existen en un día en que se den estas condiciones de

operación y luego se multiplica por el número de estos días que existen en un año. Al valor así

obtenido se le denomina Factor de Expansión.

Es necesario considerar dos factores de expansión, uno para expandir los costos

de operación (Factor de Oferta, definido de forma independiente para cada modo) y otro para

los beneficios (Factor de Demanda, único para todos los modos).

Para extrapolar al año, se consideran 5 tipos de día (considerando la información

disponible de acuerdo al Informe Ejecutivo de la EOD-2012):

a) Día Laboral Normal

b) Día Sábado Normal

c) Día Domingo o Festivo Normal

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

d) Día Laboral Estival

e) Día Sábado, Domingo o Festivo Normal

156

Para calcular los factores de expansión anuales correspondientes a cada período

de modelación, se considera que el año tiene 52 semanas, de las cuales 44 son “normales” y
8 de período estival. Se supone que **un año promedio tiene 16 días feriados (1 de**

**ellos en temporada estival)** [11], los que se consideran como un día de fin de semana y se

restan de los días laborales normales. Se asume que cada semana tiene 5 días laborales, de

manera que el año tiene 44*5-15=205 días laborales normales y 8*5-1=39 días laborales

estivales. Los días sábados normales son uno por cada día de la semana normal: 44*1=44.

Los domingos normales son uno por cada día la semana normal, a los cuales se les suma los

días feriados del período normal: 44*1+15=59. Los sábados y domingo estivales se

consideran iguales entre sí, de manera que en total hay 8*2+1=17.

Cabe destacar que la caminata, a pesar de tener una alta partición modal diaria,

no fue considerada en el análisis de factores de oferta, ya que la metodología actual no permite

capturar costos o beneficios asociados a la misma en proyectos estratégicos. Por otro lado,

modos como el Autoacompañante, que no tienen incorporado un costo de operación en la

oferta, no es necesario considerarlos.

**19.2** **Factores de Expansión**

**Tabla 19-1 Factores de Expansión Calculados para ESTRAUS, EOD 2012**

|Col1|Oferta|Col3|Col4|Col5|Demanda|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Modo**|**PM1**|**PM2**|**FP**|**PT**|**PM1**|**PM2**|**FP**|**PT**|
|**Autochofer**|205|205|3.671|869|**205**|**205**|**3.930**|**949**|
|**Bus Transantiago**|205|205|4.877|859|859|859|859|859|
|**Metro**|205|205|4.633|901|901|901|901|901|
|**Taxicolectivo**|205|205|2.637|1.188|1.188|1.188|1.188|1.188|

Fuente: Elaboración propia.

11 Promedio para los años 2018, 2019 y 2020 (www.feriados.cl).

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

157

Los factores de expansión obtenidos son consistentes con lo esperado, y similares a

los considerados en estudios anteriores.

Cabe destacar que, en el caso de la oferta, los factores para cada modo son

diferentes, a pesar de que las horas consideras para cada periodo son las mismas. Esto se debe

a las diferencias en las proporciones de viajes realizados por cada uno durante las horas de

los diversos días, así como a la sobreoferta proveída por los sistemas de transporte público

mayores (Bus Transantiago y Metro) [12] .

Si el análisis realizado para evaluar un proyecto considera la modelación de los

cuatro principales períodos de operación (PM1, PM2, PT y FP), usando los cuatro factores de

expansión exhibidos en la sección anterior para expandir los beneficios y/o costos obtenidos

a partir de la modelación de cada período, se puede calcular el beneficio total anual o el costo

total anual correspondiente.

Sin embargo, puede haber casos especiales en que se realice solo la modelación

de algunos de los cuatro períodos definidos. Debe notarse que **esto no es recomendable**

**de realizar**, ya que hay fuertes diferencias en los niveles de congestión existentes entre los

periodos, especialmente en Punta Mañana, lo que producirá una distorsión en la determinación

de los beneficios. En particular, expandir los resultados utilizando solo periodos punta,

incrementará artificialmente los beneficios (o desbeneficios) del proyecto analizado, pudiendo

impactar al punto de hacer socialmente rentable una iniciativa que evaluada correctamente [13]

no lo sería.

Los casos especiales a considerar son:

i. Modelación de solo el período Punta Mañana 1

ii. Modelación de solo el período Punta Mañana 2

iii. Modelación de solo el período Punta Mañana Completo (1 y 2)

iv. Modelación de solo Punta Mañana 1 y Fuera de Punta

12 Esta sobreoferta responde a la necesidad de satisfacer peaks de demanda temporales y espaciales, con
frecuencias de línea que son constantes (temporal y espacialmente) dentro de un periodo determinado. En cambio,
tanto autochofer como taxicolectivo responden de forma directa a la demanda.

13 Dado que ahora se cuenta con cuatro periodos modelados, que hacen posible una simulación más precisa de
la realidad y con menos simplificaciones que en el pasado.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

158

v. Modelación de solo Punta Mañana Completo (1 y 2) y Fuera de Punta

En los dos primeros casos, todos los tipos de periodos se llevan a las horas punta

mañana respectivas. En el tercer caso, PM2 representa todos los periodos, excepto PM1. En el

cuarto caso, PM1 representa todas las “horas punta”, mientras que FP representa el resto de las

horas. En el quinto caso, PM” representa todas las “horas punta”, excepto PM1, y FP representa

el resto de las horas.

A continuación, se presentan tablas con los factores de expansión para cada uno

de los casos especiales.

**Tabla 19-2 Factores de Expansión modelando solo PM1, EOD 2012**

|Col1|Oferta|Demanda|
|---|---|---|
|**Modo**|**PM1**|**PM1**|
|**Autochofer**|2.635|**2.895**|
|**Bus Transantiago**|4.276|4.276|
|**Metro**|4.375|4.375|
|**Taxicolectivo**|4.673|4.673|

Fuente: Elaboración propia.

**Tabla 19-3 Factores de Expansión modelando solo PM2, EOD 2012**

|Col1|Oferta|Demanda|
|---|---|---|
|**Modo**|**PM2**|**PM2**|
|**Autochofer**|3.383|**3.654**|
|**Bus Transantiago**|4.777|4.777|
|**Metro**|4.375|4.375|
|**Taxicolectivo**|4.640|4.640|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

**Tabla 19-4 Factores de Expansión modelando PM1 y PM2, EOD 2012**

|Col1|Oferta|Col3|Demanda|Col5|
|---|---|---|---|---|
|**Modo**|**PM1**|**PM2**|**PM1**|**PM2**|
|**Autochofer**|205|3.120|**205**|**3.395**|
|**Bus Transantiago**|205|4.548|4.548|4.548|
|**Metro**|205|4.170|4.170|4.170|
|**Taxicolectivo**|205|4.437|4.437|4.437|

Fuente: Elaboración propia.

**Tabla 19-5 Factores de Expansión modelando PM1 y FP, EOD 2012**

|Col1|Oferta|Col3|Demanda|Col5|
|---|---|---|---|---|
|**Modo**|**PM1**|**FP**|**PM1**|**FP**|
|**Autochofer**|1.036|3.671|**1.110**|**3.930**|
|**Bus Transantiago**|1.197|4.877|4.877|4.877|
|**Metro**|1.286|4.633|4.633|4.633|
|**Taxicolectivo**|1.460|2.637|2.637|2.637|

Fuente: Elaboración propia.

159

**Tabla 19-6 Factores de Expansión modelando PM1, PM2 y FP, EOD 2012**

|Col1|Oferta|Col3|Col4|Demanda|Col6|Col7|
|---|---|---|---|---|---|---|
|**Modo**|**PM1**|**PM2**|**FP**|**PM1**|**PM2**|**FP**|
|**Autochofer**|205|1.067|3.671|**205**|**1.142**|**3.930**|
|**Bus Transantiago**|205|1.108|4.877|4.877|4.877|4.877|
|**Metro**|205|1.081|4.633|4.633|4.633|4.633|
|**Taxicolectivo**|205|1.246|2.637|2.637|2.637|2.637|

Fuente: Elaboración propia.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

160

# 20 C ALIBRACIÓN S IMULTÁNEA DE LOS M ODELOS DE D ISTRIBUCIÓN DE V IAJES, P ARTICIÓN M ODAL Y E LECCIÓN DE H ORARIO (T AREA 20)

En esta Tarea se realiza la calibración simultánea de modelos de partición modal

y distribución, para los principales períodos y propósitos de viaje. **La base de datos que se**

**utiliza fue definida en la Sección 13.2 de la Tarea 13.**

Los resultados muestran que el procedimiento de calibración simultánea

Distribución-Partición Modal, presenta importantes limitaciones en el caso aquí analizado. Por

las razones que se describen a continuación, ninguno de estos modelos fue implementado en

ESTRAUS, en favor de los modelos estimados de forma independiente.

En primer lugar, las estructuras jerárquicas más complejas no son avaladas por los

datos. En específico, el pódelo de Punta Mañana para propósito Estudio 2 presenta un valor
de β < λ pub, lo cual es contradictorio con la teoría. De forma similar, varios nidos colapsan a

un modelo sin correlación entre alternativas, a saber, los nidos de horario en Punta Mañana
Estudio 2, y el nido de automóvil en Punta Tarde - Otros.

En segundo lugar, se aprecia un coeficiente positivo y significativo del costo en los

modelos con propósito Estudio para los períodos Punta Mañana y Fuera de Punta, además del

modelo con propósito Compras en el período Punta Tarde. Si bien coeficientes de precio

positivos en los modelos con propósito estudio no son extraños (debido a que los estudiantes

no tienen ingreso, y por tanto se puede argumentar que no son sensibles al precio), la situación

es más compleja en el caso de los viajes con propósito compras.

En tercer lugar, los test-t reportados para los modelos simultáneos no son

completamente confiables. La estimación simultánea se debió llevar a cabo utilizando

maximización restringida de la utilidad, es decir, limitando a priori los posibles valores de los

parámetros a un rango. En el caso de los modelos de partición modal este rango fue entre -7 y
7, para los parámetros ρ y γ fue entre -2 y 2, y para los parámetros de estructura jerárquica fue

entre 0 y 1. Se debió recurrir a esta técnica para asegurar estabilidad numérica.

Sin embargo, la maximización restringida implica que los errores estándar

calculados (y por tanto los test-t) sean sesgados si el valor del parámetro se encuentra cercano

a uno de sus valores límite. Este problema podría afectar de manera especial a los parámetros

de la estructura jerárquica, debido a su rango más estrecho.

www.FDCConsult.com

Actualización del Modelo ESTRAUS con Información de la EOD 2012

161

La diferencia en el valor de los parámetros entre los modelos secuencial y

simultáneo se puede explicar principalmente por dos razones. En primer lugar, el modelo

secuencial se estimó sin escalar (es decir, asignar pesos diferenciados) los viajes reportados en

la encuesta origen-destino. En otras palabras, cada viaje reportado pesó lo mismo. Esto se hizo

así pues el uso de pesos diferentes para cada observación reduce la eficiencia de la estimación

(i.e. disminuye el valor de los test-t) al tiempo que su mayor efecto se reduce al valor de las

constantes modales.

El modelo simultáneo, en cambio, al ser estimado a nivel de pares origen-destino,

fue estimado escalando los viajes reportados. Esto lleva a grandes diferencias en las constantes

modales. En segundo lugar, la diferencia entre los coeficientes de tiempo generalizado y costo

se puede explicar por la nueva estructura jerárquica, que agrega un nuevo nivel a la decisión

del individuo.

Todos estos problemas se reflejan en un ajuste mucho menor de la estimación

simultánea comparada con estimación secuencial. Esto se puede apreciar en el indicador R2 y

la log-verosimilitud de los modelos reportados. Adicionalmente, el menor ajuste se puede deber

a la mayor cantidad de restricciones impuestas en la estimación simultánea, a saber: el doble

rol del parámetro beta y su consecuente limitación a un valor entre 0 y 1, además de todos los

problemas ya discutidos.

Finalmente, cabe destacar que el código utilizado para la estimación simultánea de

los modelos de partición modal y distribución fue testeado mediante simulación,

comprobándose su capacidad de recuperar los parámetros de una base de datos simulada.

www.FDCConsult.com

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 7-1: Categorización de viajeros elegida****

| Col1 | Observaciones | Distribución<br>de hogares en<br>la población | Tasas de viajes |
| --- | --- | --- | --- |
| **Ingreso (M$)** | Núm. de vehículos | Núm. de vehículos | Núm. de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 2769<br>378<br>14<br>3167<br>985<br>56<br>3122<br>1713<br>192<br>1914<br>2351<br>684<br>95<br>353<br>453 | 18%<br>22%<br>25%<br>28%<br>6% | 0.130 0.163 <br>0.464 0.470 0.710<br>0.698 0.699 1.140<br>1.034 1.035 1.318<br>1.126 1.142 1.376 |

**Tabla 9-1: Partición Modal - Base de Datos Definitiva****

| ID | Modo | Viajes<br>PM1 | % | Viajes<br>PM2 | % | Viajes<br>FP | % | Viajes<br>PT | % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Caminata** | 184.846 | 13,9% | 189.064 | 20,0% | 144.076 | 25,0% | 213.021 | 20,8% |
| 2 | **Autochofer** | 336.504 | 25,3% | 243.227 | 25,8% | 142.647 | 24,7% | 254.345 | 24,8% |
| 3 | **Autoacompañante** | 178.975 | 13,5% | 68.490 | 7,3% | 24.593 | 4,3% | 61.899 | 6,0% |
| 4 | **Taxi** | 15.466 | 1,2% | 17.526 | 1,9% | 15.882 | 2,8% | 19.593 | 1,9% |
| 5 | **Bus (Transantiago)** | 308.310 | 23,2% | 180.229 | 19,1% | 113.555 | 19,7% | 191.596 | 18,7% |
| 6 | **Taxicolectivo** | 22.773 | 1,7% | 23.006 | 2,4% | 33.956 | 5,9% | 26.269 | 2,6% |
| 7 | **Metro y Tren** | 69.003 | 5,2% | 68.092 | 7,2% | 46.357 | 8,0% | 88.198 | 8,6% |
| 8 | **Bus-Metro** | 158.310 | 11,9% | 102.958 | 10,9% | 37.740 | 6,5% | 112.275 | 10,9% |
| 9 | **Taxicolectivo-Metro** | 10.631 | 0,8% | 7.758 | 0,8% | 5.670 | 1,0% | 6.165 | 0,6% |
| 12 | **Bicicleta** | 44.878 | 3,4% | 44.059 | 4,7% | 12.668 | 2,2% | 52.366 | 5,1% |
|  | **Total** | **1.329.695** | **100,0%** | **944.409** | **100,0%** | **577.144** | **100,0%** | **1.025.727** | **100,0%** |

**Tabla 10-1: Descripción de Categorías****

| Col1 | Categoría |
| --- | --- |
| Autopistas urbanas e interurbanas | **1 ** |
| Vialidad interurbana | **2 ** |
| Vialidad urbana con transporte público mayor | **3 ** |
| Vialidad urbana sin transporte público mayor | **4 ** |
| Caleteras, accesos, salidas, enlaces y peajes tradicionales de autopistas urbanas e interurbanas. | **5 ** |

**Tabla 10-2: Capacidad por Pista según Categoría****

| Categoría | Capacidad por pista (veh. equivalentes/h) | Col3 | Col4 |
| --- | --- | --- | --- |
| **Categoría** | **Base** | **Disco Pare** | **Ceda el Paso** |
| 1 | 2.050 | - | - |
| 2 | 1.800 | 1.170 | 1.260 |
| 3 | 1.350 | 810 | 878 |
| 4 | 1.600 | 960 | 1.040 |
| 5 | 1.800 | 1.080 | 1.170 |

**Tabla 10-3: Categorías de Ingreso por Clase de Usuario****

| Clase de<br>usuario | Categoría de<br>Ingreso | Ingreso (M $) | Col4 |
| --- | --- | --- | --- |
| Clase de<br>usuario | Categoría de<br>Ingreso | Mínimo | Máximo |
| 1 | 1 y 2 | 0 | 200 |
| 2 | 3 y 4 | 201 | 500 |
| 3 | 5 | 501 | 1000 |
| 4 | 6 y 7 | 1001 | 2000 |
| 5 | 8 y 9 | 2001 | ∞ |

**Tabla 10-4: Parámetros BPR por Categoría de Arco Período Punta Mañana****

| CATEGORIA DE ARCO | ALFA | BETA |
| --- | --- | --- |
| 1 | 3,1815 | 2,9699 |
| 2 | 1,4644 | 7,7367 |
| 3 | 2,7469 | 7,5237 |
| 4 | 1,8433 | 2,5823 |
| 5 | 2,5778 | 2,6839 |
| Correlación | 0,7440 | 0,7440 |
| Diferencia porcentual ponderada | 40,61 % | 40,61 % |
| Función objetivo | 158.731.720 | 158.731.720 |

**Tabla 10-5: Parámetros BPR por Categoría de Arco Periodo Fuera de Punta****

| CATEGORIA DE ARCO | ALFA | BETA |
| --- | --- | --- |
| 1 | 3,3846 | 4,5689 |
| 2 | 1,2323 | 8,2790 |
| 3 | 4,9618 | 5,8730 |
| 4 | 3,3410 | 2,1570 |
| 5 | 1,0356 | 2,6085 |
| Correlación | 0,5248 | 0,5248 |
| Diferencia porcentual ponderada | 49,90 % | 49,90 % |
| Función objetivo | 191.880.800 | 191.880.800 |

**Tabla 10-6: Parámetros BPR por Categoría de Arco Periodo Punta Tarde****

| CATEGORIA DE ARCO | ALFA | BETA |
| --- | --- | --- |
| 1 | 0,4699 | 3,2214 |
| 2 | 0,4300 | 6,7092 |
| 3 | 1,7720 | 7,6440 |
| 4 | 1,5715 | 2,9573 |
| 5 | 1,2231 | 2,8073 |
| Correlación | 0,57 | 0,57 |
| Diferencia porcentual ponderada | 41,00 % | 41,00 % |
| Función objetivo | 256.728.230 | 256.728.230 |

**Tabla 10-7: Ponderadores de Tiempo por Modo****

| BUST | V Etapa | EOD2001 | corrida 24 | corrida 31 | corrida 32 | corrida 33 | 702-N | 702-P | 702-N2 | 702-P2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pwait | 1,93 | 1,93 | 2,59 | 1,74 | 2,49 | 2,49 | 1,91 | 2,04 | 3,35 | 2,29 |
| pwalk | 3,63 | 3,63 | 3,99 | 4,62 | 4,27 | 6,99 | 3,27 | 3,46 | 4,08 | 3,73 |
| vtime | 3,62 | 3,62 | 3,62 | 3,62 | 3,62 | 3,62 | 3,62 | 3,62 | 2,76 | 3,26 |
| pxfer | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 10,00 | 0,00 | 9,89 |
| R<br>R_Corr |  |  | 0,5914 | 0,8121 | 0,6007 | 0,6275 | 0,5996 | 0,6247 | 0,5996 | 0,6592 |
| FO(mill)<br> |  |  | 2.221,03 | 5.873,05 | 2.220,20 | 2.220,20 | 2.211,48 | 2.211,48 | 2.211,48 | 2.211,43 |

**Tabla 10-8: Valores Relación Fija Entre Tiempo de Viaje en Bus y en Auto****

| CATEGORÍA DE ARCO | VEL BUS / VEL AUTO |
| --- | --- |
| 1 | 1,3000 |
| 2 | 1,5545 |
| 3 | 1,1068 |
| 4 | 1,4210 |
| 5 | 1,4222 |

**Tabla 10-9: Parámetros** _**φ**_ **y** _**ε**_ **finales****

| Col1 | φ | ε |
| --- | --- | --- |
| CATEGORÍA 1 | 0.40 | 0.66 |
| CATEGORÍA 2 | 0.58 | 0.66 |
| CATEGORÍA 3 | 0.53 | 0.66 |
| CATEGORÍA 4 | 0.40 | 0.66 |
| CATEGORÍA 5 | 0.24 | 0.66 |

**Tabla 10-10: Parámetros** _**α**_ **y** _**β**_ **calibrados****

| Tipo de corredor |  |  |
| --- | --- | --- |
| 1 (cap=471) | 9.35 | 0.15 |
| 2 (cap=485) | 10.25 | 0.14 |
| 3 (cap=149) | 10.20 | 0.16 |
| 4 (cap=205) | 6.99 | 0.16 |

**Tabla 12-1: Resumen de modelos de generación y atracción de viajes****

| Col1 | Col2 | Punta Mañana | Col4 | Col5 | Col6 | Fuera de Punta | Col8 | Col9 | Col10 | Punta Tarde | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <br> | <br> | **TRA** | **EST1** | **EST2** | **OTR** | **TRA** | **EST** | **COMP** | **OTR** | **T+E** | **COMP** | **OTRO** |
| **Generación** | Basado en hogar de ida (bhi) | ACM | ACM | ACM | ACM | ACM | ACM | ACM | ACM | ACM | ACM | ACM |
| **Generación** | Basado en hogar de retorno (bhr) | RLM | RLM | RLM | RLM | RLM | RLM | RLM | RLM | RLM | RLM | RLM |
| **Generación** | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) |
| **Atracción** | Basado en hogar de retorno (bhr) | ACM | ACM | ACM | ACM | ACM | ACM | ACM | ACM | ACM | ACM | ACM |
| **Atracción** | Basado en hogar de ida (bhi) | RLM | RLM | RLM | RLM | RLM | RLM | RLM | RLM | RLM | RLM | RLM |
| **Atracción** | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) | No basado en el hogar (nbh) |

**Tabla 12-2: Modelo de generación de viajes bhi PM, propósito trabajo****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,08472 | 0,16006 | - | 0,08472 | 0,16006 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,34459 | 0,39692 | - | 0,34459 | 0,39692 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,49783 | 0,52034 | 0,78513 | 0,49783 | 0,52034 | 0,78513 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,78047 | 0,86381 | 1,11753 | 0,78047 | 0,86381 | 1,11753 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 1,09537 | 0,91902 | 1,19308 | 0,96915 | 0,96915 | 1,19308 |

**Tabla 12-3: Modelo de generación de viajes bhi PM, propósito estudio 1****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,13797 | 0,13389 | - | 0,13754 | 0,13754 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,22042 | 0,33265 | - | 0,22042 | 0,27978 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,24477 | 0,28901 | 0,64073 | 0,24477 | 0,24477 | 0,48712 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,26481 | 0,24845 | 0,44312 | 0,26481 | 0,26481 | 0,26481 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,05362 | 0,41302 | 0,54089 | 0,31085 | 0,31085 | 0,54089 |

**Tabla 12-4: Modelo de generación de viajes bhi PM, propósito estudio 2****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,02252 | 0,11896 | - | 0,02252 | 0,05575 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,04493 | 0,03201 | - | 0,04493 | 0,04493 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,05653 | 0,05281 | 0,16273 | 0,06326 | 0,06326 | 0,06326 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,04461 | 0,05341 | 0,13766 | 0,06988 | 0,06988 | 0,06988 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,18737 | 0,10994 | 0,15413 | 0,13195 | 0,13195 | 0,15413 |

**Tabla 12-5: Modelo de generación de viajes bhi PM, propósito otros****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,09369 | 0,14221 | - | 0,08573 | 0,14221 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,08146 | 0,15426 | - | - | 0,15426 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,08447 | 0,16859 | 0,35959 | 0,35959 | 0,16330 | 0,32181 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,08578 | 0,15956 | 0,31099 | 0,31099 | 0,31099 | 0,31099 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,01716 | 0,31421 | 0,35732 | 0,35732 | 0,31421 | 0,35732 |

**Tabla 12-6: Modelo de generación de viajes bhi FP, propósito trabajo****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,01357 | 0,09596 | - | 0,01357 | 0,05058 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,03680 | 0,03646 | - | 0,03294 | 0,03294 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,02889 | 0,04863 | 0,07329 | 0,07329 | 0,07329 | 0,07329 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,07074 | 0,06635 | 0,16255 | 0,09051 | 0,09051 | 0,09051 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,24933 | 0,02923 | 0,09451 | 0,09362 | 0,09362 | 0,09362 |

**Tabla 12-7: Modelo de generación de viajes bhi FP, propósito estudio****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00891 | 0,02454 | - | 0,00891 | 0,01325 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00944 | 0,00902 | - | 0,00944 | 0,00944 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,01351 | 0,01422 | 0,04554 | 0,01193 | 0,01422 | 0,04342 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00956 | 0,01623 | 0,04914 | 0,04914 | 0,01623 | 0,01623 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,01636 | 0,02983 | 0,03366 | 0,01636 | 0,02983 | 0,02983 |

**Tabla 12-8: Modelo de generación de viajes bhi FP, propósito compras****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 |
| --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,06068 | 0,03699 | - | 0,05141 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,05396 | 0,08828 | - | - | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,04230 | 0,06447 | 0,15104 | 0,15104 | 0,09457 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,03701 | 0,03675 | 0,08975 | 0,08975 | 0,08975 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,08403 | 0,03560 | 0,07705 | 0,07705 | 0,07705 |

**Tabla 12-9: Modelo de generación de viajes bhi FP, propósito otros****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,08360 | 0,10683 | - | 0,07351 | 0,08679 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,07657 | 0,13390 | - | - | - | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,06875 | 0,09029 | 0,17294 | 0,17294 | 0,17294 | 0,11157 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,06244 | 0,06567 | 0,11902 | 0,11902 | 0,11902 | 0,11902 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,03067 | 0,03477 | 0,07295 | 0,07295 | 0,07295 | 0,07295 |

**Tabla 12-10: Modelo de generación de viajes bhi PT, propósito trabajo y****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,01019 | 0,00359 | - | 0,01627 | 0,01939 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,01766 | 0,02108 | - | - | - | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,02174 | 0,02239 | 0,02644 | 0,02644 | 0,02644 | 0,02661 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,01630 | 0,02180 | 0,02205 | 0,02205 | 0,02205 | 0,02205 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00050 | 0,03371 | 0,03371 | 0,03371 | 0,03371 |

**Tabla 12-11: Modelo de generación de viajes bhi PT, propósito compras****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 |
| --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,02519 | 0,01160 | - | 0,02120 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,01807 | 0,03454 | - | - | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,03267 | 0,01464 | 0,15932 | 0,15932 | 0,07896 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,01811 | 0,01052 | 0,03639 | 0,03639 | 0,03639 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00114 | 0,10911 | 0,10911 | 0,10911 |

**Tabla 12-12: Modelo de generación de viajes bhi PT, propósito otros****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,02477 | 0,02322 | - | 0,02249 | 0,03157 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,02042 | 0,03527 | - | - | - | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,02445 | 0,03703 | 0,14140 | 0,14140 | 0,14140 | 0,10608 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,02003 | 0,03041 | 0,09044 | 0,09044 | 0,09044 | 0,09044 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00845 | 0,00965 | 0,11461 | 0,11461 | 0,11461 | 0,11461 |

**Tabla 12-13: Modelo de generación de viajes bhr+nbh PM, propósito trabajo****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida destinada a servicios | 0,0015 | 5,68 |
| Intercepto | 1131,9880 | 4,32 |

**Tabla 12-14: Modelo de generación de viajes bhr+nbh PM, propósito estudio 1****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Logaritmo natural del ingreso total | 29,9306 | <br>0,22 |
| Intercepto | -348,3436 | <br>-0,11 |

**Tabla 12-15: Modelo de generación de viajes bhr+nbh PM, propósito estudio 2****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida dedicada a industria | 0,0001 | 0,48 |
| Intercepto | 273,3264 | 2,16 |

**Tabla 12-16: Modelo de generación de viajes bhr+nbh PM, propósito otros****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida destinada a educación | 0,0099 | 8,33 |
| Superficie construida destinada a otros | 0,0017 | 2,45 |
| Intercepto | 428,5535 | 1,25 |

**Tabla 12-17: Modelo de generación de viajes bhr+nbh FP, propósito trabajo****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida destinada a servicios | 0,0012 | 7,56 |
| Intercepto | 446,1333 | 2,77 |

**Tabla 12-18: Modelo de generación de viajes bhr+nbh FP, propósito estudio****

| Variable<br>Superficie construida destinada a hogares<br>Intercepto | Coeficiente | Test-t<br>1,38<br>0,48 |
| --- | --- | --- |
| **Variable**<br>Superficie construida destinada a hogares<br>Intercepto | 0,0001 | 0,0001 |
| **Variable**<br>Superficie construida destinada a hogares<br>Intercepto | 131,2337 | 131,2337 |

**Tabla 12-19: Modelo de generación de viajes bhr+nbh FP, propósito compras****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida destinada a hogares | 0,0001 | <br>2,06 |
| Intercepto | 173,4549 | <br>0,68 |

**Tabla 12-20: Modelo de generación de viajes bhr+nbh FP, propósito otros****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida total (excepto hogares) | 0,0003 | <br>5,00 |
| Intercepto | 229,9411 | <br>1,13 |

**Tabla 12-21: Modelo de generación de viajes bhr+nbh PT, propósito trabajo y****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida destinada a educación | 0,0250 | 5,87 |
| Superficie construida destinada a servicios | 0,0223 | 20,77 |
| Superficie construida destinada a otros | 0,0049 | 4,28 |
| Intercepto | -9,1956 | -0,02 |

**Tabla 12-22: Modelo de generación de viajes bhr+nbh PT, propósito compras****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida destinada a servicios | 0,0012 | 11,83 |
| Intercepto | 91,9632 | 0,69 |

**Tabla 12-23: Modelo de generación de viajes bhr+nbh PT, propósito otros****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida destinada a servicio | 0,0015 | 8,67 |
| Intercepto | 481,7108 | 2,45 |

**Tabla 12-24: Modelo de atracción de viajes bhr PM, propósito trabajo****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00039 | 0,00641 | - | 0,00485 | 0,00638 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00467 | 0,00343 | - | - | - | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00614 | 0,00857 | 0,00767 | 0,00767 | 0,00767 | 0,00767 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,01046 | 0,00683 | 0,01458 | 0,01458 | 0,01458 | 0,01206 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00183 | 0,00817 | 0,00817 | 0,00817 | 0,00817 |

**Tabla 12-25: Modelo de atracción de viajes bhr PM, propósito estudio 1****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00028 | 0,00000 | - | 0,00025 | 0,00034 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00021 | 0,00047 | - | - | - | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00133 | 0,00097 | 0,00000 | 0,00057 | 0,00057 | 0,00057 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00358 | 0,00000 | 0,00000 | 0,00000 | 0,00000 |

**Tabla 12-26: Modelo de atracción de viajes bhr PM, propósito estudio 2****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | - | 0,00000 | 0,00000 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | - | 0,00000 | 0,00000 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 |

**Tabla 12-27: Modelo de atracción de viajes bhr PM, propósito otros****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,01978 | 0,05774 | - | 0,01978 | 0,05512 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,03630 | 0,08356 | - | 0,03212 | 0,03212 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,02773 | 0,05248 | 0,09327 | 0,09327 | 0,09327 | 0,09327 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,03626 | 0,03810 | 0,11567 | 0,03465 | 0,03465 | 0,10318 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00625 | 0,09308 | 0,08391 | 0,08391 | 0,08391 | 0,08391 |

**Tabla 12-28: Modelo de atracción de viajes bhr FP, propósito trabajo****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00077 | 0,00000 | - | 0,00077 | 0,00974 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00210 | 0,02631 | - | 0,00210 | 0,00210 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00735 | 0,00629 | 0,00510 | 0,00546 | 0,00546 | 0,02057 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00291 | 0,00677 | 0,01565 | 0,01565 | 0,01565 | 0,01565 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00484 | 0,03499 | 0,03499 | 0,03499 | 0,03499 |

**Tabla 12-29: Modelo de atracción de viajes bhr FP, propósito estudio****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 |
| --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00025 | 0,03886 | - | 0,00025 | 0,00309 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00098 | 0,00025 | - | 0,00095 | 0,00095 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00158 | 0,00037 | 0,00000 | 0,00000 | 0,00000 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00040 | 0,00376 | 0,00376 | 0,00376 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,01026 | 0,00000 | 0,00000 | 0,00000 |

**Tabla 12-30: Modelo de atracción de viajes bhr FP, propósito compras****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo |
| --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00170 | 0,00000 | - | 0,00030 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00038 | - | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | 0,00000 | 0,00000 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | 0,00000 | 0,00000 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | 0,00000 | 0,00000 |

**Tabla 12-31: Modelo de atracción de viajes bhr FP, propósito otros****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | - | 0,00000 | 0,00000 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | - | 0,00000 | 0,00000 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00020 | 0,00610 | 0,00000 | 0,00018 | 0,00370 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 |

**Tabla 12-32: Modelo de atracción de viajes bhr PT, propósito trabajo y estudio****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,05926 | 0,11840 | - | 0,05926 | 0,11840 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,18096 | 0,24342 | - | 0,18096 | 0,24342 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,23157 | 0,26723 | 0,36903 | 0,23157 | 0,26723 | 0,36903 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,35736 | 0,39375 | 0,57423 | 0,35736 | 0,39375 | 0,57423 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,65717 | 0,49803 | 0,60010 | 0,54327 | 0,54327 | 0,60010 |

**Tabla 12-33: Modelo de atracción de viajes bhr PT, propósito compras****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | - | 0,00000 | 0,00000 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00105 | 0,00000 | - | 0,00050 | 0,00050 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00034 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00458 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00523 | 0,00243 | 0,00572 | 0,00369 | 0,00369 | 0,00369 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00385 | 0,00485 | 0,00485 | 0,00485 | 0,00485 |

**Tabla 12-34: Modelo de atracción de viajes bhr PT, propósito otros****

| Col1 | Modelo inicial | Col3 | Col4 | Mejor modelo | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Ingreso (M$) | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos | Número de vehículos |
| Min<br>Max | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 | 0 <br>1 <br>≥2 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00000 | - | 0,00000 | 0,00000 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00062 | 0,00000 | - | 0,00047 | 0,00047 | - |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00294 | 0,00000 | 0,01721 | 0,00177 | 0,00276 | 0,00276 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,00000 | 0,00120 | 0,00454 | 0,00454 | 0,00454 | 0,00454 |
| 0 <br>230<br>231<br>420<br>421<br>725<br>726<br>1793<br>1794<br>∞ | 0,01486 | 0,00147 | 0,00358 | 0,00413 | 0,00413 | 0,00413 |

**Tabla 12-35: Modelo de atracción de viajes bhi+nbh PM, propósito trabajo****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida destinada a servicios | 0,0462 | 33,78 |
| Superficie construida destinada a hogares | 0,0026 | 6,52 |
| Intercepto | 2.023,1410 | 1,62 |

**Tabla 12-36: Modelo de atracción de viajes bhi+nbh PM, propósito estudio 1****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Número de matrículas de educación 1 | 0,2237 | 6,76 |
| Superficie construida destinada a educación | 0,0327 | 8,86 |
| Intercepto | 497,0596 | 0,55 |

**Tabla 12-37: Modelo de atracción de viajes bhi+nbh PM, propósito estudio 2****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Número de matrículas de estudio 2 | 0,1858 | 26,71 |
| Intercepto | 1.082,8780 | 3,08 |

**Tabla 12-38: Modelo de atracción de viajes bhi+nbh PM, propósito otros****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida destinada a educación | 0,0336 | 12,33 |
| Superficie construida destinada a otros | 0,0035 | 2,17 |
| Intercepto | 366,7098 | 0,47 |

**Tabla 12-39: Modelo de atracción de viajes bhi+nbh FP, propósito trabajo****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida destinada a educación | 0,0071 | 2,91 |
| Superficie construida destinada a servicios | 0,0054 | 9,00 |
| Intercepto | -236,1897 | -0,70 |

**Tabla 12-40: Modelo de atracción de viajes bhi+nbh FP, propósito estudio****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Número de matrículas de Estudio 2 | 0,0437 | 17,00 |
| Intercepto | 560,1610 | 3,57 |

**Tabla 12-41: Modelo de atracción de viajes bhi+nbh FP, propósito compras****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida destinada a comercio | 0,0048 | 9,79 |
| Intercepto | 1.594,8870 | 4,91 |

**Tabla 12-42: Modelo de atracción de viajes bhi+nbh FP, propósito otros****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Número de matrículas de Estudio 1 | 0,0548 | <br>3,23 |
| Número de matrículas de Estudio 2 | 0,0785 | <br>2,81 |
| Superficie construida destinada a comercio | 0,0068 | <br>3,03 |
| Intercepto | -151,2304 | <br>-0,27 |

**Tabla 12-43: Modelo de atracción de viajes bhi+nbh PT, propósito trabajo y****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Número de Matrículas de Estudio 1 | 0,0169 | 3,32 |
| Número de Matrículas de Estudio 2 | 0,0980 | 37,30 |
| Intercepto | 342,6840 | 1,83 |

**Tabla 12-44: Modelo de atracción de viajes bhi+nbh PT, propósito compras****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida destinada a hogares | 0,0008 | 12,19 |
| Intercepto | -528,8613 | -1,91 |

**Tabla 12-45: Modelo de atracción de viajes bhi+nbh PT, propósito otros****

| Variable | Coeficiente | Test-t |
| --- | --- | --- |
| Superficie construida destinada a servicios | 0,0037 | 9,81 |
| Intercepto | 1.292,7820 | 3,64 |

**Tabla 12-46: Factores de Ajuste para un solo Periodo Punta Mañana****

| Propósito | Factor para PM1 | Factor para PM2 |
| --- | --- | --- |
| **Trabajo** | 0,579 | 0,421 |
| **Estudio 1** | 0,712 | 0,288 |
| **Estudio 2** | 0,536 | 0,464 |
| **Otros** | 0,442 | 0,558 |

**Tabla 13-1: Funciones de Utilidad MNL Base****

| Modo ESTRAUS | Forma Funcional |
| --- | --- |
| 1 Caminata | U1 = θ1 + θtv−cam∙tv1 |
| 2 Auto (chofer) | U2 = θ2 + θtv−auto∙tv2<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I2 + θnAutos∙nAutos |
| 3 Auto (acompañante) | U3 = θ3 + θtv−auto∙tv3<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I3 + θnAutos∙nAutos |
| 4 Taxi | U4 = θ4 + θtv∙tv4 + θta∙ta4 + θte∙te4<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I4 |
| 5 Bus Transantiago | U5 = θ5 + θtv∙tv5 + θta∙ta5 + θte∙te5 + θtr∙tr5<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I5 |
| 6 Taxi colectivo | U6 = θ6 + θtv∙tv6 + θta∙ta6 + θte_CN∙te6 + θtr∙tr6<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I6 |
| 7 Metro | U7 = θ7 + θtv∙tv7 + θta∙ta7 + θte∙te7<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I7 + θMujer∙δMujer |
| 8 Bus Transantiago - Metro | U8 = θ8 + θtv∙tv8 + θta∙ta8 + θte∙te8<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I8 + θMujer∙δMujer |
| 9 Taxi colectivo - Metro | U9 = θ9 + θtv∙tv9 + θta∙ta9 + θte_CN∙te9<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I9 + θMujer∙δMujer |
| 12 Bicicleta | U12 = θ12 + θtv−bic∙tv12 |
| 13 Bus No Transantiago | U13 = θ13 + θtv∙tv13 + θta∙ta13 + θte_CN∙te13<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I13 |
| 14 Bus No Transantiago - Metro | U14 = θ14 + θtv∙tv14 + θta∙ta14 + θte_CN∙te14<br>+ (θcI1 ∙δI1 + θcI2 ∙δI2 + θcI3 ∙δI3 + θcI4 ∙δI4 + θcI5<br>∙δI5) ∙C_I14 + θMujer∙δMujer |

**Tabla 13-2: Modelo de Partición Modal PM, propósito trabajo (MNL), NO****

| Parámetro | Valor | Test-t |
| --- | --- | --- |
| θ1 | 1,2004 | 8,30 |
| θ2 | 0,7436 | 4,42 |
| θ3 | -1,8281 | -9,31 |
| θ4 | -1,8004 | -8,78 |
| θ5 | 0,0000 | - |
| θ6 | -1,0930 | -5,89 |
| θ7 | 1,7598 | 12,59 |
| θ8 | -0,4993 | -8,37 |
| θ9 | -2,0878 | -10,05 |
| θ12 | 0,6042 | 4,35 |
| θtg1 | -0,0466 | -13,71 |
| θtg2 | -0,0163 | -8,08 |
| θtg−ayt | -0,0225 | -7,51 |

**Tabla 13-3: Modelo de Partición Modal PM, propósito estudio 1 (MNL), NO****

| Parámetro | Valor | Test-t |
| --- | --- | --- |
| θ1 | 1,5457 | 12,63 |
| θ2 | -0,5230 | -0,98 |
| θ3 | -0,6786 | -3,24 |
| θ4 | -3,7017 | -14,27 |
| θ5 | 0,0000 | - |
| θ6 | -2,4441 | -9,80 |
| θ7 | -0,2000 | -0,67 |
| θ8 | -1,4090 | -10,23 |
| θ9 | -4,2810 | -9,01 |

**Tabla 13-4: Modelo de Partición Modal PM, propósito estudio 2 (MNL), NO****

| Parámetro | Valor | Test-t |
| --- | --- | --- |
| θ12 | 0,1027 | 0,20 |
| θtg1 | -0,0309 | -2,89 |
| θtg−aut | -0,0153 | -2,50 |
| θtg−pub | -0,0134 | -4,70 |
| θtg12 | -0,0982 | -4,70 |

**Tabla 13-5: Modelo de Partición Modal PM, propósito otros (MNL), NO****

| Parámetro | Valor | Test-t |
| --- | --- | --- |
| θ1 | 1,8169 | 8,06 |
| θ2 | 2,2921 | 7,36 |
| θ3 | -0,8727 | -2,73 |
| θ4 | -1,3278 | -5,83 |
| θ5 | 0,0000 | - |
| θ6 | -1,4163 | -8,33 |
| θ7 | -0,5731 | -2,18 |
| θ8 | -0,9943 | -4,55 |
| θ9 | -2,6838 | -7,12 |
| θ12 | -2,3040 | -8,85 |

**Tabla 13-6: Modelo de Partición Modal FP, propósito trabajo (MNL)****

| Parámetro | Valor | Test-t |
| --- | --- | --- |
| θ1 | 1,8348 | 4,74 |
| θ2 | 1,3151 | 3,64 |
| θ3 | -2,7699 | -6,35 |
| θ4 | -2,5445 | -6,11 |
| θ5 | 0,0000 | - |
| θ6 | -1,2903 | -5,78 |
| θ7 | 0,6069 | 2,32 |
| θ8 | -0,2422 | -2,42 |

**Tabla 13-7: Modelo de Partición Modal FP, propósito estudio (MNL)****

| Parámetro | Valor | Test-t |
| --- | --- | --- |
| θ8 | 0,3853 | 1,32 |
| θ9 | -3,1918 | -3,81 |
| θ12 | 1,2298 | 3,10 |

**Tabla 13-8: Modelo de Partición Modal FP, propósito vuelta a casa (MNL)****

| Parámetro | Valor | Test-t |
| --- | --- | --- |
| θ1 | 3,1359 | 8,07 |
| θ2 | 2,5592 | 6,03 |
| θ3 | -0,7409 | -2,25 |
| θ4 | -1,3974 | -3,83 |
| θ5 | 0,0000 | - |
| θ6 | 0,0375 | 1,85 |
| θ7 | 0,9622 | 2,67 |

**Tabla 13-9: Modelo de Partición Modal FP, propósito compras (MNL)****

| Parámetro | Valor | Test-t |
| --- | --- | --- |
| θ1 | 2,5658 | 12,23 |
| θ2 | 1,7743 | 5,35 |
| θ3 | -0,9926 | -3,31 |
| θ4 | -3,1061 | -6,69 |
| θ5 | 0,0000 | - |
| θ6 | -0,5695 | -3,83 |
| θ7 | -0,0357 | -0,73 |

**Tabla 13-10: Modelo de Partición Modal FP, propósito otros (NL)****

| Parámetro | Valor | Test-t |
| --- | --- | --- |
| θ7 | 0,0819 | 0,33 |
| θ8 | -0,2382 | -3,16 |
| θ9 | -0,4332 | -3,25 |
| θ12 | -1,6310 | -3,67 |

**Tabla 13-11: Modelo de Partición Modal PT, propósito trabajo y estudio (NL)****

| Parámetro | Valor | Test-t |
| --- | --- | --- |
| θ9 | -1,0203 | -4,95 |
| θ12 | 0,3113 | -0,01 |
| θtg−act | -2,5644 | -11,25 |
| θtg−pri | -1,4989 | -7,17 |
| θtg−pub | -0,7060 | -5,54 |
| θtg7 | -1,0560 | -6,08 |
| θcI12 | -0,6681 | -5,08 |
| θcI345 | -0,2033 | -6,83 |

**Tabla 13-12: Modelo de Partición Modal PT, propósito vuelta a casa (NL)****

| Parámetro | Valor | Test-t |
| --- | --- | --- |
| φ[1] | 1,0000 | - |
| φ[2] | 0,0988 | 21,36 |
| θ1 | 2,3271 | 12,19 |
| θ2 | 1,9037 | 10,42 |
| θ3 | -0,3508 | -3,37 |
| θ4 | -1,8631 | -8,97 |
| θ5 | 0,0000 | - |
| θ6 | -0,0379 | -1,76 |

**Tabla 13-13: Modelo de Partición Modal PT, propósito compras (MNL)****

| Parámetro | Valor | Test-t |
| --- | --- | --- |
| θ1 | 3,1033 | 7,37 |
| θ2 | 2,8084 | 6,57 |
| θ3 | 1,5870 | 2,91 |
| θ4 | -0,5124 | -1,22 |
| θ5 | 0,0000 | - |
| θ6 | -1,5461 | -2,79 |
| θ7 | -0,2192 | -0,47 |

**Tabla 13-14: Modelo de Partición Modal PT, propósito otros (NL)****

| Parámetro | Valor | Test-t |
| --- | --- | --- |
| θ7 | 0,5513 | 2,50 |
| θ8 | -0,7959 | -2,95 |
| θ9 | -2,6935 | -4,43 |

**Tabla 14-115: Modelos de Distribución Implementados en ESTRAUS****

| Periodo | Propósito | Acotado | β | ρ | γ |
| --- | --- | --- | --- | --- | --- |
| PM | Trabajo | Doblemente | 1,3059 | 0,5302 | - |
| PM | Estudio 1 | Doblemente | 1,6860 | 0,8368 | - |
| PM | Estudio 2 | Doblemente | 4,5252 | - | - |
| PM | Otros | Doblemente | 1,1627 | 0,6420 | - |
| FP | Trabajo | Doblemente | 1,3732 | - | - |
| FP | Estudio | Doblemente | 3,0551 | - | - |
| FP | Vuelta a Casa | Doblemente | 1,3112 | - | - |
| FP | Compras | Simplemente | 1,9312 | - | - |
| FP | Otros | Doblemente | 2,4896 | 0,4977 | - |
| PT | Trabajo y Estudio | Doblemente | 0,6051 | 0,6902 | - |
| PT | Vuelta a Casa | Doblemente | 1,1494 | 0,3230 | - |
| PT | Compras | Doblemente | 1,2001 | - | - |
| PT | Otros | Doblemente | 1,2280 | - | - |

**Tabla 16-1: Modelo de Partición Modal PM con Elección Horaria, Propósito****

| Parámetro | Valor |
| --- | --- |
| θ5H2 | -0,5323 |
| θ6H2 | -1,5154 |
| θ7H2 | 0,4298 |
| θ8H2 | 0,0115 |
| θ9H2 | -1,9831 |
| θ12H2 | -0,3859 |
| θtg1 | -3,2003 |
| θtg−pri | -0,2198 |
| θtg−bus | -0,1850 |
| θtg−txc | -0,2404 |
| θtg7 | -0,5702 |

**Tabla 16-2: Modelo de Partición Modal PM con Elección Horaria, Propósito****

| Parámetro | Valor |
| --- | --- |
| φ[1] | 1,0000 |
| φ[2] | 0,5481 |
| φ[A] | 1,0000 |
| θ1H1 | 1,1529 |
| θ3H1 | -0,2104 |
| θ4H1 | -3,0652 |
| θ5H1 | -0,1500 |
| θ6H1 | -2,9674 |
| θ7H1 | -0,0764 |
| θ8H1 | -0,7366 |
| θ9H1 | -5,4593 |
| θ12H1 | -2,5164 |
| θ1H2 | 0,9122 |

**Tabla 16-3: Modelo de Partición Modal PM con Elección Horaria, Propósito****

| Parámetro | Valor |
| --- | --- |
| φ[1] | 1,0000 |
| φ[2] | 0,2614 |
| φ[A] | 1,0000 |
| θ1H1 | -2,3310 |
| θ2H1 | -2,2864 |
| θ3H1 | -2,5753 |
| θ5H1 | -0,6102 |
| θ6H1 | -3,8750 |
| θ7H1 | 0,2767 |

**Tabla 16-4: Modelo de Partición Modal PM con Elección Horaria, Propósito****

| Parámetro | Valor |
| --- | --- |
| φ[1] | 1,0000 |
| φ[2] | 0,2105 |
| φ[A] | 1,0000 |
| θ1H1 | 1,5522 |
| θ2H1 | 1,6451 |
| θ3H1 | -0,8834 |
| θ4H1 | -2,5913 |
| θ5H1 | -0,1000 |
| θ6H1 | -0,7558 |
| θ7H1 | -0,2854 |
| θ8H1 | -0,2790 |
| θ9H1 | -5,7526 |
| θ12H1 | -1,2448 |
| θ1H2 | 2,3939 |
| θ2H2 | 1,3269 |

**Tabla 17-1: Partición Modal Base de Datos PM Total****

| Modo | Total PM | Col3 | Trabajo | Col5 | Estudio 1 | Col7 | Estudio 2 | Col9 | Otros | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Caminata** | ** 373.910** | <br>**16,4%** | 85.284 | <br>7,1% | 199.158 | <br>36,1% | 1.587 | <br>1,3% | 87.880 | <br>21,9% |
| **Autochofer** | ** 579.731** | <br>**25,5%** | 392.096 | <br>32,8% | 1.038 | 0,2% | 11.841 | <br>9,3% | 174.755 | <br>43,6% |
| **Autoacompañante** | ** 247.465** | <br>**10,9%** | 54.354 | <br>4,6% | 162.312 | <br>29,4% | 8.409 | <br>6,6% | 22.390 | <br>5,6% |
| **Taxi** | ** 32.992** | <br>**1,5%** | 14.258 | <br>1,2% | 7.301 | <br>1,3% | 34 | <br>0,0% | 11.399 | <br>2,8% |
| **BusTransantiago** | ** 488.538** | <br>**21,5%** | 269.009 | <br>22,5% | 131.843 | <br>23,9% | 26.525 | <br>20,9% | 61.161 | <br>15,2% |
| **Taxicolectivo** | ** 45.779** | <br>**2,0%** | 24.900 | <br>2,1% | 8.142 | <br>1,5% | 1.802 | <br>1,4% | 10.934 | <br>2,7% |
| **Metro** | ** 137.095** | <br>**6,0%** | 86.920 | <br>7,3% | 10.564 | <br>1,9% | 31.640 | <br>24,9% | 7.970 | <br>2,0% |
| **Metro-BusTransantiago** | ** 261.268** | <br>**11,5%** | 185.824 | <br>15,6% | 20.252 | <br>3,7% | 40.056 | <br>31,6% | 15.135 | <br>3,8% |
| **Metro-Taxicolectivo** | ** 18.389** | <br>**0,8%** | 14.488 | <br>1,2% | 1.392 | <br>0,3% | 1.507 | <br>1,2% | 1.002 | <br>0,2% |
| **Bicicleta** | ** 88.937** | <br>**3,9%** | 67.149 | <br>5,6% | 9.614 | <br>1,7% | 3.528 | <br>2,8% | 8.646 | <br>2,2% |
| **Total** | ** 2.274.104** | ** 100,0%** | 1.194.284 | 100,0% | 551.616 | 100,0% | 126.932 | 100,0% | 401.272 | 100,0% |

**Tabla 17-2: Partición Modal Base de Datos PM1****

| Modo | Total PM1 | Col3 | Trabajo | Col5 | Estudio 1 | Col7 | Estudio 2 | Col9 | Otros | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Caminata** | ** 184.846** | **13,9%** | 34.417 | 5,0% | 122.012 | 31,1% | 311 | 0,5% | 28.106 | 15,8% |
| **Autochofer** | ** 336.504** | **25,3%** | 231.014 | 33,4% | 666 | 0,2% | 6.714 | 9,9% | 98.110 | 55,3% |
| **Autoacompañante** | ** 178.975** | **13,5%** | 33.912 | 4,9% | 127.639 | 32,5% | 4.228 | 6,2% | 13.195 | 7,4% |
| **Taxi** | ** 15.466** | **1,2%** | 6.110 | 0,9% | 5.436 | 1,4% | - | 0,0% | 3.920 | 2,2% |
| **BusTransantiago** | ** 308.310** | **23,2%** | 174.233 | 25,2% | 99.041 | 25,2% | 15.006 | 22,1% | 20.030 | 11,3% |
| **Taxicolectivo** | ** 22.773** | **1,7%** | 13.358 | 1,9% | 5.300 | 1,4% | 855 | 1,3% | 3.259 | 1,8% |
| **Metro** | ** 69.003** | **5,2%** | 41.264 | 6,0% | 9.507 | 2,4% | 15.615 | 23,0% | 2.618 | 1,5% |
| **Metro-BusTransantiago** | ** 158.310** | **11,9%** | 114.650 | 16,6% | 17.761 | 4,5% | 21.779 | 32,0% | 4.119 | 2,3% |
| **Metro-Taxicolectivo** | ** 10.631** | **0,8%** | 7.726 | 1,1% | 1.392 | 0,4% | 1.035 | 1,5% | 478 | 0,3% |
| **Bicicleta** | ** 44.878** | **3,4%** | 35.159 | 5,1% | 3.736 | 1,0% | 2.476 | 3,6% | 3.508 | 2,0% |
| **Total** | ** 1.329.695** | **100,0%** | 691.843 | 100,0% | 392.490 | 100,0% | 68.021 | 100,0% | 177.341 | 100,0% |

**Tabla 17-3: Partición Modal Base de Datos PM2****

| Modo | Total PM2 | Col3 | Trabajo | Col5 | Estudio 1 | Col7 | Estudio 2 | Col9 | Otros | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Caminata** | ** 189.064** | **20,0%** | 50.867 | 10,1% | 77.147 | 48,5% | 1.275 | 2,2% | 59.774 | 26,7% |
| **Autochofer** | ** 243.227** | **25,8%** | 161.082 | 32,1% | 372 | 0,2% | 5.127 | 8,7% | 76.645 | 34,2% |
| **Autoacompañante** | ** 68.490** | **7,3%** | 20.442 | 4,1% | 34.672 | 21,8% | 4.181 | 7,1% | 9.195 | 4,1% |
| **Taxi** | ** 17.526** | **1,9%** | 8.148 | 1,6% | 1.865 | 1,2% | 34 | 0,1% | 7.479 | 3,3% |
| **BusTransantiago** | ** 180.229** | **19,1%** | 94.776 | 18,9% | 32.802 | 20,6% | 11.519 | 19,6% | 41.131 | 18,4% |
| **Taxicolectivo** | ** 23.006** | **2,4%** | 11.542 | 2,3% | 2.842 | 1,8% | 947 | 1,6% | 7.675 | 3,4% |
| **Metro** | ** 68.092** | **7,2%** | 45.657 | 9,1% | 1.057 | 0,7% | 16.026 | 27,2% | 5.353 | 2,4% |
| **Metro-BusTransantiago** | ** 102.958** | **10,9%** | 71.174 | 14,2% | 2.491 | 1,6% | 18.277 | 31,0% | 11.016 | 4,9% |
| **Metro-Taxicolectivo** | ** 7.758** | **0,8%** | 6.762 | 1,3% | - | 0,0% | 472 | 0,8% | 524 | 0,2% |
| **Bicicleta** | ** 44.059** | **4,7%** | 31.990 | 6,4% | 5.879 | 3,7% | 1.052 | 1,8% | 5.138 | 2,3% |
| **Total** | ** 944.409** | **100,0%** | 502.441 | 100,0% | 159.126 | 100,0% | 58.911 | 100,0% | 223.931 | 100,0% |

**Tabla 17-4: Partición Modal ESTRAUS PM Total****

| Modo | Total | Col3 | Trabajo | Col5 | Estudio 1 | Col7 | Estudio 2 | Col9 | Otros | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Caminata** | ** 382.827** | ** 16,0%** | 80.159 | <br>6,2% | 209.851 | 36,9% | 2.110 | <br>1,6% | 90.708 | 21,9% |
| **Autochofer** | ** 626.694** | ** 26,1%** | 428.342 | 33,4% | - | 0,0% | 10.344 | <br>7,9% | 188.009 | 45,3% |
| **Autoacompañante** | ** 228.306** | <br>**9,5%** | 42.240 | <br>3,3% | 158.977 | 27,9% | 8.386 | <br>6,4% | 18.703 | <br>4,5% |
| **Taxi** | ** 18.881** | <br>**0,8%** | 9.046 | <br>0,7% | 3.523 | <br>0,6% | - | 0,0% | 6.312 | <br>1,5% |
| **BusTransantiago** | ** 513.732** | ** 21,4%** | 287.053 | 22,4% | 138.854 | 24,4% | 28.603 | 21,9% | 59.222 | 14,3% |
| **Taxicolectivo** | ** 74.750** | <br>**3,1%** | 51.755 | <br>4,0% | 4.938 | <br>0,9% | 789 | <br>0,6% | 17.269 | <br>4,2% |
| **Metro** | ** 162.162** | <br>**6,8%** | 97.792 | <br>7,6% | 19.914 | <br>3,5% | 32.102 | 24,6% | 12.355 | <br>3,0% |
| **Metro-BusTransantiago** | ** 264.814** | ** 11,0%** | 178.823 | 13,9% | 27.604 | <br>4,9% | 42.830 | 32,8% | 15.556 | <br>3,8% |
| **Metro-Taxicolectivo** | ** 21.458** | <br>**0,9%** | 20.186 | <br>1,6% | 217 | <br>0,0% | 986 | <br>0,8% | 70 | <br>0,0% |
| **Bicicleta** | ** 104.441** | <br>**4,4%** | 88.488 | <br>6,9% | 4.984 | <br>0,9% | 4.351 | <br>3,3% | 6.618 | <br>1,6% |
| **Total** | ** 2.398.065** | ** 100,0%** | 1.283.884 | 100,0% | 568.862 | 100,0% | 130.501 | 100,0% | 414.822 | 100,0% |

**Tabla 17-5: Partición Modal ESTRAUS PM1****

| Modo | Total | Col3 | Trabajo | Col5 | Estudio 1 | Col7 | Estudio 2 | Col9 | Otros | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Caminata** | ** 175.571** | ** 12,9%** | 30.305 | <br>4,2% | 117.502 | 30,7% | 444 | <br>0,6% | 27.320 | 14,4% |
| **Autochofer** | ** 357.314** | ** 26,2%** | 244.250 | 33,7% | - | 0,0% | 5.975 | <br>8,6% | 107.089 | 56,6% |
| **Autoacompañante** | ** 162.575** | ** 11,9%** | 27.606 | <br>3,8% | 118.811 | 31,0% | 4.498 | <br>6,5% | 11.660 | <br>6,2% |
| **Taxi** | ** 8.787** | <br>**0,6%** | 3.971 | <br>0,5% | 2.638 | <br>0,7% | - | 0,0% | 2.178 | <br>1,2% |
| **BusTransantiago** | ** 312.854** | ** 22,9%** | 176.897 | 24,4% | 100.351 | 26,2% | 15.474 | 22,4% | 20.132 | 10,6% |
| **Taxicolectivo** | ** 38.906** | <br>**2,8%** | 28.265 | <br>3,9% | 4.319 | <br>1,1% | 392 | <br>0,6% | 5.930 | <br>3,1% |
| **Metro** | ** 84.266** | <br>**6,2%** | 48.036 | <br>6,6% | 15.650 | <br>4,1% | 15.179 | 21,9% | 5.401 | <br>2,9% |
| **Metro-BusTransantiago** | ** 158.832** | ** 11,6%** | 107.130 | 14,8% | 21.539 | <br>5,6% | 23.236 | 33,6% | 6.927 | <br>3,7% |
| **Metro-Taxicolectivo** | ** 13.082** | <br>**1,0%** | 11.874 | <br>1,6% | 217 | <br>0,1% | 963 | <br>1,4% | 28 | <br>0,0% |
| **Bicicleta** | ** 53.794** | <br>**3,9%** | 46.350 | <br>6,4% | 1.706 | <br>0,4% | 3.053 | <br>4,4% | 2.685 | <br>1,4% |
| **Total** | ** 1.365.981** | ** 100,0%** | 724.684 | 100,0% | 382.733 | 100,0% | 69.214 | 100,0% | 189.350 | 100,0% |

**Tabla 17-6: Partición Modal ESTRAUS PM2****

| Modo | Total | Col3 | Trabajo | Col5 | Estudio 1 | Col7 | Estudio 2 | Col9 | Otros | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Caminata** | ** 207.282** | ** 20,1%** | 49.862 | <br>8,9% | 92.364 | 49,6% | 1.666 | <br>2,7% | 63.391 | 28,1% |
| **Autochofer** | ** 269.420** | ** 26,1%** | 184.129 | 32,9% | - | 0,0% | 4.368 | <br>7,1% | 80.923 | 35,9% |
| **Autoacompañante** | ** 65.745** | <br>**6,4%** | 14.640 | <br>2,6% | 40.173 | 21,6% | 3.888 | <br>6,3% | 7.043 | <br>3,1% |
| **Taxi** | ** 10.096** | <br>**1,0%** | 5.076 | <br>0,9% | 886 | <br>0,5% | - | 0,0% | 4.134 | <br>1,8% |
| **BusTransantiago** | ** 200.916** | ** 19,5%** | 110.187 | 19,7% | 38.510 | 20,7% | 13.129 | 21,4% | 39.090 | 17,3% |
| **Taxicolectivo** | ** 35.852** | <br>**3,5%** | 23.496 | <br>4,2% | 620 | <br>0,3% | 397 | <br>0,6% | 11.339 | <br>5,0% |
| **Metro** | ** 77.899** | <br>**7,5%** | 49.757 | <br>8,9% | 4.265 | <br>2,3% | 16.923 | 27,6% | 6.954 | <br>3,1% |
| **Metro-BusTransantiago** | ** 105.988** | ** 10,3%** | 71.699 | 12,8% | 6.066 | <br>3,3% | 19.594 | 32,0% | 8.629 | <br>3,8% |
| **Metro-Taxicolectivo** | ** 8.377** | <br>**0,8%** | 8.312 | <br>1,5% | - | 0,0% | 23 | <br>0,0% | 42 | <br>0,0% |
| **Bicicleta** | ** 50.682** | <br>**4,9%** | 42.173 | <br>7,5% | 3.278 | <br>1,8% | 1.298 | <br>2,1% | 3.934 | <br>1,7% |
| **Total** | ** 1.032.257** | ** 100,0%** | 559.331 | 100,0% | 186.162 | 100,0% | 61.286 | 100,0% | 225.479 | 100,0% |

**Tabla 17-7: Partición Modal Base de Datos FP****

| Modo | Total FP | Col3 | Trabajo | Col5 | Estudio | Col7 | Vuelta a Casa | Col9 | Compras | Col11 | Otros | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Caminata** | **144.076** | **25,0%** | 16.904 | <br>12,0% | 4.068 | 10,9% | 31.569 | 39,5% | 60.991 | 48,2% | 30.544 | 15,9% |
| **Autochofer** | **142.647** | **24,7%** | 58.644 | <br>41,5% | 6.992 | 18,8% | 17.577 | 22,0% | 23.168 | 18,3% | 36.268 | 18,9% |
| **Autoacompañante** | **24.593** | **4,3%** | 2.965 | <br>2,1% | 1.835 | 4,9% | 3.640 | 4,6% | 7.435 | 5,9% | 8.718 | 4,5% |
| **Taxi** | **15.882** | **2,8%** | 2.147 | <br>1,5% | - | 0,0% | 3.458 | 4,3% | 1.216 | 1,0% | 9.060 | 4,7% |
| **BusTransantiago** | **113.555** | **19,7%** | 27.698 | <br>19,6% | 7.431 | 19,9% | 8.308 | 10,4% | 15.562 | 12,3% | 54.557 | 28,4% |
| **Taxicolectivo** | **33.956** | **5,9%** | 5.157 | <br>3,6% | 626 | 1,7% | 5.857 | 7,3% | 6.300 | 5,0% | 16.016 | 8,3% |
| **Metro** | **46.357** | **8,0%** | 10.047 | <br>7,1% | 4.333 | 11,6% | 4.629 | 5,8% | 4.256 | 3,4% | 23.091 | 12,0% |
| **Metro-BusTransantiago** | **37.740** | **6,5%** | 13.210 | <br>9,3% | 9.991 | 26,8% | 3.182 | 4,0% | 1.715 | 1,4% | 9.643 | 5,0% |
| **Metro-Taxicolectivo** | **5.670** | **1,0%** | 1.098 | <br>0,8% | 261 | 0,7% | 144 | 0,2% | 1.595 | 1,3% | 2.572 | 1,3% |
| **Bicicleta** | **12.668** | **2,2%** | 3.559 | <br>2,5% | 1.748 | 4,7% | 1.549 | 1,9% | 4.361 | 3,4% | 1.452 | 0,8% |
| **Total** | **577.144** | **100,0%** | 141.427 | 100,0% | 37.286 | 100,0% | 79.913 | 100,0% | 126.599 | 100,0% | 191.920 | 100,0% |

**Tabla 17-8: Partición Modal ESTRAUS FP****

| Modo | Total | Col3 | Trabajo | Col5 | Estudio | Col7 | Vuelta a Casa | Col9 | Compras | Col11 | Otros | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Caminata** | ** 90.648** | <br>**14,1%** | 11.096 | <br>6,9% | 7.141 | <br>16,9% | 16.201 | <br>18,3% | 35.019 | <br>26,2% | 21.192 | <br>9,8% |
| **Autochofer** | ** 233.004** | <br>**36,3%** | 71.147 | <br>44,2% | 5.823 | <br>13,7% | 36.613 | <br>41,5% | 50.875 | <br>38,1% | 68.545 | <br>31,6% |
| **Autoacompañante** | ** 16.095** | <br>**2,5%** | 2.044 | <br>1,3% | 1.893 | <br>4,5% | 1.668 | <br>1,9% | 4.127 | <br>3,1% | 6.362 | <br>2,9% |
| **Taxi** | ** 15.824** | <br>**2,5%** | 1.336 | <br>0,8% | 6.759 | <br>16,0% | 3.059 | <br>3,5% | 1.035 | <br>0,8% | 3.635 | <br>1,7% |
| **BusTransantiago** | ** 109.332** | <br>**17,0%** | 27.479 | <br>17,1% | 5.176 | <br>12,2% | 12.259 | <br>13,9% | 21.528 | <br>16,1% | 42.890 | <br>19,8% |
| **Taxicolectivo** | ** 34.691** | <br>**5,4%** | 2.417 | <br>1,5% | 212 | <br>0,5% | 3.179 | <br>3,6% | 4.296 | <br>3,2% | 24.588 | <br>11,3% |
| **Metro** | ** 50.452** | <br>**7,9%** | 14.089 | <br>8,7% | 3.893 | <br>9,2% | 8.123 | <br>9,2% | 5.359 | <br>4,0% | 18.988 | <br>8,8% |
| **Metro-BusTransantiago** | ** 25.456** | <br>**4,0%** | 7.289 | <br>4,5% | 2.577 | <br>6,1% | 1.007 | <br>1,1% | 916 | <br>0,7% | 13.668 | <br>6,3% |
| **Metro-Taxicolectivo** | ** 9.330** | <br>**1,5%** | 632 | <br>0,4% | 95 | <br>0,2% | 128 | <br>0,1% | 260 | <br>0,2% | 8.217 | <br>3,8% |
| **Bicicleta** | ** 57.528** | <br>**9,0%** | 23.526 | <br>14,6% | 8.797 | <br>20,8% | 6.085 | <br>6,9% | 10.188 | <br>7,6% | 8.932 | <br>4,1% |
| **Total** | ** 642.309** | ** 100,0%** | 161.040 | 100,0% | 42.367 | 100,0% | 88.318 | 100,0% | 133.594 | 100,0% | 216.991 | 100,0% |

**Tabla 17-9: Partición Modal Base de Datos PT****

| Modo | Total PT | Col3 | Trabajo y Estudio | Col5 | Vuelta a Casa | Col7 | Compras | Col9 | Otros | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Caminata** | ** 213.021** | ** 20,8%** | 80.871 | 12,5% | 66.763 | 34,0% | 37.705 | 50,1% | 27.682 | 25,5% |
| **Autochofer** | ** 254.345** | ** 24,8%** | 165.708 | 25,7% | 38.452 | 19,6% | 13.978 | 18,6% | 36.207 | 33,4% |
| **Autoacompañante** | ** 61.899** | <br>**6,0%** | 27.141 | <br>4,2% | 16.504 | <br>8,4% | 7.801 | 10,4% | 10.453 | <br>9,6% |
| **Taxi** | ** 19.593** | <br>**1,9%** | 4.882 | <br>0,8% | 7.305 | <br>3,7% | 4.050 | <br>5,4% | 3.356 | <br>3,1% |
| **BusTransantiago** | ** 191.596** | ** 18,7%** | 144.358 | 22,4% | 29.046 | 14,8% | 6.467 | <br>8,6% | 11.725 | 10,8% |
| **Taxicolectivo** | ** 26.269** | <br>**2,6%** | 11.786 | <br>1,8% | 11.152 | <br>5,7% | 1.011 | <br>1,3% | 2.320 | <br>2,1% |
| **Metro** | ** 88.198** | <br>**8,6%** | 69.531 | 10,8% | 11.107 | <br>5,6% | 1.917 | <br>2,5% | 5.642 | <br>5,2% |
| **Metro-BusTransantiago** | ** 112.275** | ** 10,9%** | 97.496 | 15,1% | 9.721 | <br>4,9% | 532 | <br>0,7% | 4.526 | <br>4,2% |
| **Metro-Taxicolectivo** | ** 6.165** | <br>**0,6%** | 5.294 | <br>0,8% | 322 | <br>0,2% | 54 | <br>0,1% | 494 | <br>0,5% |
| **Bicicleta** | ** 52.366** | <br>**5,1%** | 38.267 | <br>5,9% | 6.232 | <br>3,2% | 1.736 | <br>2,3% | 6.131 | <br>5,6% |
| **Total** | ** 1.025.727** | ** 100,0%** | 645.334 | 100,0% | 196.604 | 100,0% | 75.251 | 100,0% | 108.537 | 100,0% |

**Tabla 17-10: Partición Modal ESTRAUS PT****

| Modo | Total | Col3 | Trabajo y Estudio | Col5 | Vuelta a Casa | Col7 | Compras | Col9 | Otros | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Caminata** | ** 101.995** | <br>**9,9%** | 51.408 | <br>7,6% | 20.363 | <br>10,1% | 25.075 | <br>33,9% | 5.149 | <br>7,0% |
| **Autochofer** | ** 317.206** | <br>**30,8%** | 192.940 | <br>28,3% | 76.299 | <br>37,9% | 25.416 | <br>34,3% | 22.550 | <br>30,5% |
| **Autoacompañante** | ** 35.499** | <br>**3,4%** | 19.259 | <br>2,8% | 8.477 | <br>4,2% | 4.810 | <br>6,5% | 2.953 | <br>4,0% |
| **Taxi** | ** 10.853** | <br>**1,1%** | 1.751 | <br>0,3% | 5.417 | <br>2,7% | 2.700 | <br>3,6% | 985 | <br>1,3% |
| **BusTransantiago** | ** 243.651** | <br>**23,7%** | 180.482 | <br>26,5% | 31.228 | <br>15,5% | 9.959 | <br>13,4% | 21.982 | <br>29,7% |
| **Taxicolectivo** | ** 55.443** | <br>**5,4%** | 30.861 | <br>4,5% | 21.332 | <br>10,6% | 792 | <br>1,1% | 2.459 | <br>3,3% |
| **Metro** | ** 104.492** | <br>**10,1%** | 75.358 | <br>11,1% | 15.666 | <br>7,8% | 3.106 | <br>4,2% | 10.362 | <br>14,0% |
| **Metro-BusTransantiago** | ** 82.753** | <br>**8,0%** | 67.205 | <br>9,9% | 10.991 | <br>5,5% | 395 | <br>0,5% | 4.162 | <br>5,6% |
| **Metro-Taxicolectivo** | ** 23.344** | <br>**2,3%** | 14.692 | <br>2,2% | 7.105 | <br>3,5% | 80 | <br>0,1% | 1.467 | <br>2,0% |
| **Bicicleta** | ** 55.532** | <br>**5,4%** | 47.449 | <br>7,0% | 4.384 | <br>2,2% | 1.717 | <br>2,3% | 1.983 | <br>2,7% |
| **Total** | ** 1.030.047** | ** 100,0%** | 680.699 | 100,0% | 201.248 | 100,0% | 74.049 | 100,0% | 74.050 | 100,0% |

**Tabla 18-2: Progresión de la Partición Modal PM Total****

| Modo | 2012 | 2012-2020 | 2020 | 2020-2025 | 2025 |
| --- | --- | --- | --- | --- | --- |
| **Caminata** | 259.068 | <br>-6,0% | 243.479 | <br>74,0% | 423.621 |
| **Autochofer** | 729.571 | <br>34,8% | 983.508 | <br>22,8% | 1.207.704 |
| **Autoacompañante** | 205.418 | <br>-33,1% | 137.511 | <br>310,2% | 564.119 |
| **Taxi** | 19.002 | <br>139,1% | 45.435 | <br>-55,3% | 20.318 |
| **BusTransantiago** | 546.987 | <br>-49,5% | 276.028 | <br>138,0% | 657.078 |
| **Taxicolectivo** | 139.889 | <br>-5,5% | 132.205 | <br>-13,2% | 114.811 |
| **Metro** | 144.530 | <br>-11,5% | 127.881 | <br>157,1% | 328.828 |
| **Metro-BusTransantiago** | 183.968 | <br>-29,3% | 130.139 | <br>55,2% | 201.939 |
| **Metro-Taxicolectivo** | 70.364 | <br>15,7% | 81.378 | <br>-11,7% | 71.830 |
| **Bicicleta** | 99.298 | <br>284,9% | 382.152 | <br>-61,8% | 146.070 |
| **Total** | ** 2.389.046** | <br>**5,9%** | ** 2.529.022** | <br>**45,0%** | ** 3.667.451** |
| **No Motorizado** | 358.366 | <br>74,6% | 625.631 | <br>-8,9% | 569.691 |
| **Transporte Público** | 1.085.738 | <br>-31,1% | 747.631 | <br>83,8% | 1.374.486 |
| **Transporte Privado** | 953.991 | <br>22,3% | 1.166.454 | <br>53,6% | 1.792.141 |

**Tabla 18-3: Progresión de la Partición Modal PM1****

| Modo | 2012 | 2012-2020 | 2020 | 2020-2025 | 2025 |
| --- | --- | --- | --- | --- | --- |
| **Caminata** | 133.059 | <br>-1,5% | 131.095 | <br>74,7% | 228.991 |
| **Autochofer** | 430.639 | <br>49,3% | 643.148 | <br>8,7% | 699.317 |
| **Autoacompañante** | 153.735 | <br>-73,7% | 40.363 | <br>945,8% | 422.126 |
| **Taxi** | 8.767 | <br>119,0% | 19.199 | <br>-46,3% | 10.301 |
| **BusTransantiago** | 308.311 | <br>-56,5% | 134.114 | <br>181,0% | 376.847 |
| **Taxicolectivo** | 70.962 | <br>-12,2% | 62.293 | <br>-6,0% | 58.543 |
| **Metro** | 76.758 | <br>-14,4% | 65.708 | <br>185,8% | 187.763 |
| **Metro-BusTransantiago** | 101.462 | <br>-31,3% | 69.742 | <br>65,2% | 115.248 |
| **Metro-Taxicolectivo** | 37.630 | <br>1,4% | 38.143 | <br>3,4% | 39.421 |
| **Bicicleta** | 51.072 | <br>278,0% | 193.073 | <br>-60,2% | 76.841 |
| **Total** | ** 1.370.300** | <br>**1,7%** | ** 1.393.476** | <br>**57,7%** | ** 2.197.134** |
| **No Motorizado** | 184.131 | <br>76,1% | 324.168 | <br>-5,7% | 305.832 |
| **Transporte Público** | 595.123 | <br>-37,8% | 370.000 | <br>110,2% | 777.822 |
| **Transporte Privado** | 593.141 | <br>18,5% | 702.710 | <br>61,1% | 1.131.744 |

**Tabla 18-4: Progresión de la Partición Modal PM2****

| Modo | 2012 | 2012-2020 | 2020 | 2020-2025 | 2025 |
| --- | --- | --- | --- | --- | --- |
| **Caminata** | 126.029 | <br>-10,8% | 112.410 | <br>73,3% | 194.776 |
| **Autochofer** | 298.971 | <br>13,9% | 340.480 | <br>49,6% | 509.231 |
| **Autoacompañante** | 51.694 | <br>87,9% | 97.151 | <br>47,1% | 142.895 |
| **Taxi** | 10.236 | <br>156,3% | 26.239 | <br>-61,8% | 10.032 |
| **BusTransantiago** | 238.706 | <br>-40,5% | 141.927 | <br>97,6% | 280.473 |
| **Taxicolectivo** | 68.936 | <br>1,4% | 69.917 | <br>-19,4% | 56.327 |
| **Metro** | 67.774 | <br>-8,3% | 62.174 | <br>126,9% | 141.096 |
| **Metro-BusTransantiago** | 82.509 | <br>-26,8% | 60.399 | <br>43,6% | 86.711 |
| **Metro-Taxicolectivo** | 32.735 | <br>32,1% | 43.236 | <br>-25,0% | 32.414 |
| **Bicicleta** | 48.259 | <br>291,9% | 189.124 | <br>-63,3% | 69.369 |
| **Total** | ** 1.024.319** | <br>**11,4%** | ** 1.141.084** | <br>**32,2%** | ** 1.508.637** |
| **No Motorizado** | 174.288 | <br>73,0% | 301.534 | <br>-12,4% | 264.145 |
| **Transporte Público** | 490.660 | <br>-23,0% | 377.653 | <br>58,1% | 597.021 |
| **Transporte Privado** | 360.901 | <br>28,5% | 463.870 | <br>42,7% | 662.158 |

**Tabla 18-5: Progresión de las Velocidades (km/h) PM1****

| Modo | 2012 | 2012-2020 | 2020 | 2020-2025 | 2025 |
| --- | --- | --- | --- | --- | --- |
| **Autochofer** | 21,2 | <br>-20,8% | 16,8 | <br>-24,2% | 12,7 |
| **Autoacompañante** | 22,6 | <br>-13,7% | 19,5 | <br>-20,2% | 15,6 |
| **Taxi** | 20,6 | <br>-16,5% | 17,2 | <br>-15,7% | 14,5 |
| **BusTransantiago** | 16,3 | <br>-14,7% | 13,9 | <br>-16,1% | 11,7 |
| **Taxicolectivo** | 16,9 | <br>-17,8% | 13,9 | <br>-23,5% | 10,6 |
| **Metro** | 34,1 | <br>13,5% | 38,7 | <br>-2,1% | 37,9 |
| **Metro-BusTransantiago** | 26,1 | <br>0,0% | 26,1 | <br>-4,8% | 24,8 |
| **Metro-Taxicolectivo** | 28,8 | <br>-3,1% | 27,9 | <br>-7,6% | 25,8 |

**Tabla 18-6: Progresión de las Velocidades (km/h) PM2****

| Modo | 2012 | 2012-2020 | 2020 | 2020-2025 | 2025 |
| --- | --- | --- | --- | --- | --- |
| **Autochofer** | 31,3 | -22,4% | 24,3 | -26,4% | 17,9 |
| **Autoacompañante** | 30,8 | -17,2% | 25,5 | -23,1% | 19,6 |
| **Taxi** | 27,4 | -23,7% | 20,9 | -22,3% | 16,2 |
| **BusTransantiago** | 22,0 | -18,6% | 17,9 | -19,5% | 14,4 |
| **Taxicolectivo** | 25,7 | -21,0% | 20,3 | -25,1% | 15,2 |
| **Metro** | 35,0 | 10,9% | 38,8 | -1,9% | 38,1 |
| **Metro-BusTransantiago** | 29,4 | -3,4% | 28,4 | -3,7% | 27,3 |
| **Metro-Taxicolectivo** | 33,0 | -1,2% | 32,6 | -7,2% | 30,3 |

**Tabla 18-7: Progresión de la Partición Modal FP****

| Modo | 2012 | 2012-2020 | 2020 | 2020-2025 | 2025 |
| --- | --- | --- | --- | --- | --- |
| **Caminata** | 90.648 | <br>2,4% | 92.808 | <br>2,6% | 95.202 |
| **Autochofer** | 233.004 | <br>16,5% | 271.394 | <br>26,4% | 343.162 |
| **Autoacompañante** | 16.095 | <br>29,2% | 20.789 | <br>30,4% | 27.117 |
| **Taxi** | 15.824 | <br>3,0% | 16.304 | <br>1,2% | 16.506 |
| **BusTransantiago** | 109.332 | <br>2,0% | 111.568 | <br>-3,9% | 107.252 |
| **Taxicolectivo** | 34.691 | <br>-0,2% | 34.605 | <br>-4,0% | 33.228 |
| **Metro** | 50.452 | <br>6,3% | 53.654 | <br>34,0% | 71.873 |
| **Metro-BusTransantiago** | 25.456 | <br>13,3% | 28.849 | <br>-11,3% | 25.576 |
| **Metro-Taxicolectivo** | 9.330 | <br>30,7% | 12.195 | <br>-10,2% | 10.953 |
| **Bicicleta** | 57.528 | <br>11,4% | 64.067 | <br>8,5% | 69.524 |
| **Total** | ** 642.309** | <br>**9,1%** | ** 700.758** | <br>**13,3%** | ** 793.714** |
| **No Motorizado** | 148.176 | <br>5,9% | 156.875 | <br>5,0% | 164.726 |
| **Transporte Público** | 229.261 | <br>5,1% | 240.871 | <br>3,3% | 248.882 |
| **Transporte Privado** | 264.923 | <br>16,4% | 308.487 | <br>25,4% | 386.785 |

**Tabla 18-8: Progresión de las Velocidades (km/h) FP****

| Modo | 2012 | 2012-2020 | 2020 | 2020-2025 | 2025 |
| --- | --- | --- | --- | --- | --- |
| **Autochofer** | 38,9 | <br>-4,1% | 37,3 | <br>-21,9% | 29,1 |
| **Autoacompañante** | 38,9 | <br>-3,1% | 37,7 | <br>-22,4% | 29,3 |
| **Taxi** | 34,5 | <br>-9,9% | 31,1 | <br>-23,2% | 23,9 |
| **BusTransantiago** | 25,3 | <br>-5,9% | 23,8 | <br>-15,4% | 20,1 |
| **Taxicolectivo** | 28,3 | <br>4,9% | 29,7 | <br>-17,3% | 24,6 |
| **Metro** | 35,2 | <br>17,3% | 41,3 | <br>-9,2% | 37,5 |
| **Metro-BusTransantiago** | 28,4 | <br>10,6% | 31,4 | <br>-8,1% | 28,9 |
| **Metro-Taxicolectivo** | 31,2 | <br>27,9% | 39,9 | <br>-9,3% | 36,2 |

**Tabla 18-9: Progresión de la Partición Modal PT****

| Modo | 2012 | 2012-2020 | 2020 | 2020-2025 | 2025 |
| --- | --- | --- | --- | --- | --- |
| **Caminata** | 101.995 | <br>2,9% | 105.000 | <br>7,2% | 112.564 |
| **Autochofer** | 317.206 | <br>23,8% | 392.793 | <br>22,5% | 481.326 |
| **Autoacompañante** | 35.499 | <br>29,1% | 45.815 | <br>21,7% | 55.737 |
| **Taxi** | 10.853 | <br>7,6% | 11.676 | <br>3,0% | 12.032 |
| **BusTransantiago** | 243.651 | <br>0,4% | 244.709 | <br>1,4% | 248.177 |
| **Taxicolectivo** | 55.443 | <br>-7,1% | 51.533 | <br>4,8% | 54.003 |
| **Metro** | 104.492 | <br>16,4% | 121.677 | <br>39,0% | 169.104 |
| **Metro-BusTransantiago** | 82.753 | <br>18,2% | 97.790 | <br>-2,7% | 95.115 |
| **Metro-Taxicolectivo** | 23.344 | <br>29,7% | 30.284 | <br>4,3% | 31.600 |
| **Bicicleta** | 55.532 | <br>3,5% | 57.460 | <br>4,7% | 60.155 |
| **Total** | ** 1.030.047** | <br>**11,8%** | ** 1.151.659** | <br>**13,9%** | ** 1.311.559** |
| **No Motorizado** | 157.527 | <br>3,1% | 162.460 | <br>6,3% | 172.719 |
| **Transporte Público** | 509.683 | <br>7,1% | 545.993 | <br>9,5% | 597.999 |
| **Transporte Privado** | 363.558 | <br>23,9% | 450.284 | <br>21,9% | 549.095 |

**Tabla 18-10: Progresión de las Velocidades (km/h) PT****

| Modo | 2012 | 2012-2020 | 2020 | 2020-2025 | 2025 |
| --- | --- | --- | --- | --- | --- |
| **Autochofer** | 28,5 | <br>-7,5% | 26,4 | <br>-18,1% | 21,6 |
| **Autoacompañante** | 29,9 | <br>-8,6% | 27,3 | <br>-16,6% | 22,8 |
| **Taxi** | 29,7 | <br>-15,7% | 25,0 | <br>-21,7% | 19,6 |
| **BusTransantiago** | 21,0 | <br>-6,6% | 19,6 | <br>-13,4% | 17,0 |
| **Taxicolectivo** | 25,2 | <br>-2,9% | 24,5 | <br>-17,9% | 20,1 |
| **Metro** | 35,9 | <br>15,8% | 41,6 | <br>-7,6% | 38,4 |
| **Metro-BusTransantiago** | 25,3 | <br>22,9% | 31,1 | <br>-6,7% | 29,0 |
| **Metro-Taxicolectivo** | 32,6 | <br>9,3% | 35,6 | <br>-8,8% | 32,5 |

**Tabla 19-1: Factores de Expansión Calculados para ESTRAUS, EOD 2012****

| Col1 | Oferta | Col3 | Col4 | Col5 | Demanda | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Modo** | **PM1** | **PM2** | **FP** | **PT** | **PM1** | **PM2** | **FP** | **PT** |
| **Autochofer** | 205 | 205 | 3.671 | 869 | **205** | **205** | **3.930** | **949** |
| **Bus Transantiago** | 205 | 205 | 4.877 | 859 | 859 | 859 | 859 | 859 |
| **Metro** | 205 | 205 | 4.633 | 901 | 901 | 901 | 901 | 901 |
| **Taxicolectivo** | 205 | 205 | 2.637 | 1.188 | 1.188 | 1.188 | 1.188 | 1.188 |

**Tabla 19-2: Factores de Expansión modelando solo PM1, EOD 2012****

| Col1 | Oferta | Demanda |
| --- | --- | --- |
| **Modo** | **PM1** | **PM1** |
| **Autochofer** | 2.635 | **2.895** |
| **Bus Transantiago** | 4.276 | 4.276 |
| **Metro** | 4.375 | 4.375 |
| **Taxicolectivo** | 4.673 | 4.673 |

**Tabla 19-3: Factores de Expansión modelando solo PM2, EOD 2012****

| Col1 | Oferta | Demanda |
| --- | --- | --- |
| **Modo** | **PM2** | **PM2** |
| **Autochofer** | 3.383 | **3.654** |
| **Bus Transantiago** | 4.777 | 4.777 |
| **Metro** | 4.375 | 4.375 |
| **Taxicolectivo** | 4.640 | 4.640 |

**Tabla 19-4: Factores de Expansión modelando PM1 y PM2, EOD 2012****

| Col1 | Oferta | Col3 | Demanda | Col5 |
| --- | --- | --- | --- | --- |
| **Modo** | **PM1** | **PM2** | **PM1** | **PM2** |
| **Autochofer** | 205 | 3.120 | **205** | **3.395** |
| **Bus Transantiago** | 205 | 4.548 | 4.548 | 4.548 |
| **Metro** | 205 | 4.170 | 4.170 | 4.170 |
| **Taxicolectivo** | 205 | 4.437 | 4.437 | 4.437 |

**Tabla 19-5: Factores de Expansión modelando PM1 y FP, EOD 2012****

| Col1 | Oferta | Col3 | Demanda | Col5 |
| --- | --- | --- | --- | --- |
| **Modo** | **PM1** | **FP** | **PM1** | **FP** |
| **Autochofer** | 1.036 | 3.671 | **1.110** | **3.930** |
| **Bus Transantiago** | 1.197 | 4.877 | 4.877 | 4.877 |
| **Metro** | 1.286 | 4.633 | 4.633 | 4.633 |
| **Taxicolectivo** | 1.460 | 2.637 | 2.637 | 2.637 |

**Tabla 19-6: Factores de Expansión modelando PM1, PM2 y FP, EOD 2012****

| Col1 | Oferta | Col3 | Col4 | Demanda | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Modo** | **PM1** | **PM2** | **FP** | **PM1** | **PM2** | **FP** |
| **Autochofer** | 205 | 1.067 | 3.671 | **205** | **1.142** | **3.930** |
| **Bus Transantiago** | 205 | 1.108 | 4.877 | 4.877 | 4.877 | 4.877 |
| **Metro** | 205 | 1.081 | 4.633 | 4.633 | 4.633 | 4.633 |
| **Taxicolectivo** | 205 | 1.246 | 2.637 | 2.637 | 2.637 | 2.637 |
