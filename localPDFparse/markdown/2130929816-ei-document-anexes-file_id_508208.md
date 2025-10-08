---
title: Planta General
author: Desconocido
date: D:20151116135825-03'00'
language: es
type: report
pages: 61
has_toc: True
has_tables: True
extraction_quality: high
---

Anexo 4

Estudio de Redes

|ESTUDIO DE SISTEMA<br>PROYECTO N° 15034<br>ESTUDIO DE CONEXIÓN DE PMGD<br>PMGD HBS GNL 6,75[MW]|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|0|28-10-15|Revisión Final|Revisión Final|RMC|SAS|MVC|JCM|
|B|22-09-15|Revisión Cliente|Revisión Cliente|RMC|MVM|MVC|JCM|
|A|21-09-15|Revisión Interna|Revisión Interna|RMC|MVM|MVC||
|**REV**|**FECHA**|**MOTIVO REVISIÓN**|**MOTIVO REVISIÓN**|**POR**|**REV**|**APR**|**CLIENTE**|
|TECNORED<br>HBS GNL|TECNORED<br>HBS GNL|TECNORED<br>HBS GNL|DOCUMENTO N°<br>15034-E-IN-004|DOCUMENTO N°<br>15034-E-IN-004|DOCUMENTO N°<br>15034-E-IN-004|DOCUMENTO N°<br>15034-E-IN-004|REV<br>0|

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

## TABLA DE CONTENIDOS TABLA DE CONTENIDOS .................................................................................................................................... 2

**1** **INTRODUCCIÓN ....................................................................................................................................... 4**

**2** **ALCANCES DEL ESTUDIO .......................................................................................................................... 6**

2.1 Objetivos ........................................................................................................................................... 6

**3** **REPRESENTACIÓN DEL ALIMENTADOR..................................................................................................... 7**

3.1 Alimentador Laja .............................................................................................................................. 7

3.2 Modelación ....................................................................................................................................... 8

**4** **INFORMACIÓN TÉCNICA DE LA MODELACIÓN ........................................................................................12**

4.1 Parámetros Conductores ................................................................................................................ 12

4.2 Transformadores ............................................................................................................................ 12

4.3 Bancos Capacitores ......................................................................................................................... 13

4.4 Generadores ................................................................................................................................... 13

**5** **CONSIDERACIÓN NORMATIVA................................................................................................................13**

**6** **METODOLOGÍA .......................................................................................................................................16**

6.1 Escenario de Demanda ................................................................................................................... 16

6.2 Escenario de Operación .................................................................................................................. 18

6.3 Estudio de Cortocircuito ................................................................................................................. 18

6.4 Estudio de Flujos de Potencia ......................................................................................................... 19

6.5 Estudio de Comportamiento Dinámico .......................................................................................... 19

**7** **DESARROLLO ESTUDIO DE CORTOCIRCUITO ...........................................................................................20**

7.1 Resultados Estudio de Cortocircuito .............................................................................................. 20

7.1.1 Escenario CC-00 .............................................................................................................................. 21

7.1.2 Escenario CC-12 .............................................................................................................................. 22

7.2 Valores Máximos ............................................................................................................................ 23

7.3 Capacidad Nominal de los Interruptores y Equipos de Protección ................................................ 23

7.4 Comentarios Resultados ECC .......................................................................................................... 24

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 2 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

**8** **DESARROLLO ESTUDIO DE FLUJOS DE POTENCIA ....................................................................................26**

8.1 Resultados Flujos de Potencia Sin PMGD HBS GNL ........................................................................ 26

8.1.1 Escenario: FA1600 .......................................................................................................................... 27

8.1.2 Escenario: FB1600 .......................................................................................................................... 29

8.1.3 Resumen Resultados Flujos de Potencia Sin PMGD HBS GNL ........................................................ 30

8.2 Resultados Flujos de Potencia Con PMGD HBS GNL ....................................................................... 32

8.2.1 Escenario: FA1611 .......................................................................................................................... 32

8.2.2 Escenario: FB1611 .......................................................................................................................... 34

8.2.3 Escenario: FB1612 .......................................................................................................................... 37

8.2.4 Resumen Resultados Flujos de Potencia Con PMGD HBS GNL ....................................................... 38

8.2.5 Revisión Ajuste del Nivel de Tensión con PMGD HBS GNL ............................................................. 40

8.3 Comentarios Resultados Estudio de Flujos de Potencia ................................................................. 41

**9** **ESTUDIO DE COMPORTAMIENTO DINÁMICO..........................................................................................42**

9.1 Configuración de los Estudios Dinámicos ....................................................................................... 42

9.2 Resultados Desconexión Intempestiva de Generación .................................................................. 43

9.2.1 Escenario DA-1-PG .......................................................................................................................... 43

9.2.2 Escenario DB-1-PG .......................................................................................................................... 47

9.3 Resultados Falla en Elemento Serie del Alimentador ..................................................................... 50

9.3.1 Escenario DA-1-CC .......................................................................................................................... 51

9.3.2 Escenario DB-1-CC .......................................................................................................................... 55

9.4 Comentarios Resultados Comportamiento Dinámico .................................................................... 58

**10** **CONCLUSIONES FINALES .........................................................................................................................59**

**11** **ANEXOS ..................................................................................................................................................60**

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 3 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

## 1 INTRODUCCIÓN

Con la finalidad de dar cumplimiento a lo estipulado en el Decreto Supremo N°244 (DS) y

la Norma Técnica de Conexión y Operación (NTCO), en lo que respecta a la conexión de

Pequeños Medios de Generación Distribuida (PMGD), Tecnored S.A o el Consultor

desarrolló el presente documento para determinar el impacto que producirá la nueva

central en el punto de conexión y repercusión considerando la existencia de otro PMGD

denominado HBS Energía.

El punto de inyección escogido para la entrega de los excedentes de energía de la

empresa HBS GNL, es el alimentador Laja en un nivel de tensión de 23[kV], perteneciente

al Sistema de Distribución (Dx) propiedad de CGE Distribución, ubicado en la ciudad de

Los Ángeles, VIII Región, Chile. Mediante el Formulario N°1 enviado con copia a la

Superintendencia de Electricidad y Combustible (SEC), se solicitaron los antecedentes

para poder realizar las gestiones de inyección de potencia en el Poste N° 126610 parte

del alimentador antes mencionado. Este documento contempla utilizar la base de datos

DIgSILENT de CDEC-SIC de Agosto de 2015, para el desarrollo de los siguientes análisis:

 - Estudio de Cortocircuito.

 Estudio de Flujos de Potencia.

 - Estudio Dinámico.

Como resultados se obtendrá el desempeño del alimentador con la nueva inyección y la

generación existente, determinando si algún equipo ve superada su capacidad de ruptura

de cortocircuito, plan de obras de cargo del PMGD y además una propuesta de un plan

de obra de cargo del distribuidor, sólo en caso de ser necesario.

Se proyectó la potencia informada por el Cliente que suma un total de 6,75[MW]

instalados, parámetro que permitirá estimar una sección adecuada para los eventuales

refuerzos y tramos propios de línea para poder así despachar la totalidad de la

generación sin limitación térmica. Para la modelación del alimentador se utilizó

solamente la información entregada por CGE Distribución mediante el Formulario N°2 y

los antecedentes que el Consultor recibió de parte del Cliente HBS GNL.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 4 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

**Figura 1: Vista General Alimentador Laja Georeferenciado.**

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 5 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

## 2 ALCANCES DEL ESTUDIO

### 2.1 Objetivos

El presente informe tiene como objetivo, de acuerdo al Artículo 2-4 de la NTCO, evaluar

el impacto sistémico estático y dinámico de la conexión del PMGD “HBS GNL” basado en

los siguientes puntos:

 Estudio de Cortocircuito: Verificación de los interruptores proyectados y

existentes, determinando el aumento de cortocircuito en la red denominada

Laja.

 Estudio de Flujos de Potencia: Cuantificar el comportamiento estático del

sistema en cuanto a los niveles de tensión, requerimiento de reactivos,

porcentajes de carga y potencias transmitidas. Con estos resultados se

propondrá las obras requeridas para la conexión del PMGD, identificando la

empresa que debe hacerse cargo de cada una de las mejoras planteadas.

 Estudio Dinámicos: Analizar el comportamiento en función del tiempo, de la

tensión ante la pérdida intempestiva de generación y/o ante una eventual

contingencia en la cabecera del alimentador, verificando la salida del

generador antes de la primera reconexión.

Para cada uno de los puntos anteriores, a lo menos se identificará el impacto en el punto

de conexión y el punto de repercusión, siendo estos últimos como se define en la NTCO

en el Artículo 1-10 Numeral 18, los puntos con clientes o posibles clientes más cercanos

al lugar de inyección del generador.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 6 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

## 3 REPRESENTACIÓN DEL ALIMENTADOR

Conforme a lo informado por el cliente HBS GNL, se consideró la conexión de los nuevos

generadores en el alimentador Laja energizado desde la S/E El Avellano 66/23[kV]. Esta

subestación cuenta con dos transformadores de poder, donde el equipo T2 energiza la

barra desde donde se extiende el alimentador en análisis.

### 3.1 Alimentador Laja

Esta red de distribución está emplazada con una forma predominantemente radial, con

una extensión en su troncal de unos 26,74[km] aproximadamente, contando con dos

equipos de compensación de reactivos. Este alimentador en los puntos cercanos a las

instalaciones donde se emplazará el PMGD, tiene los siguientes calibres de conductor:

 Cable Aluminio AAAC 2AWG: Este se encuentra desde el poste 702963 (Punto

de Conexión Solicitado) hasta el poste 126468, este conductor a 75[°C] en un

nivel de 23[kV] tiene límite térmico de 5[MVA]. Existen algunos tramos con

Cobre Protegido 70 mm2 en esta sección.

 Cobre Desnudo 85 mm2: Este se encuentra desde el poste 126468 hasta

prácticamente la S/E El avellano, este conductor a 75[°C] en un nivel de 23[kV]

tiene límite térmico de 12[MVA].

 Cobre Protegido 185 mm2: Existen tramos intermedios del trocal donde se

encuentra este conductor, siendo a 75[°C] en un nivel de 23[kV] un elemento

con límite térmico de 14[MVA].

 - XLPE 120 mm2: De manera similar al cable anterior este existe en una tramo

cercano a la S/E El Avellano, con un límite térmico a 75[°C] en un nivel de

23[kV] de 12,4[MVA].

Este alimentador de acuerdo a la información recibida con el Formulario N°2, no cuenta

con un plan de obras a corto plazo.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 7 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

### 3.2 Modelación

El análisis se desarrolló con el software PowerFactory DIgSILENT versión 15.2, creando

una base de datos con la modelación exacta del alimentador de acuerdo a la información

oficial entregada por la empresa distribuidora propietaria de las instalaciones. La base

contempló los siguientes hitos:

1. Modelación de cada poste como un nodo cuyo nombre es igual al rótulo

informado del elemento.

2. Se ubicaron los 1100 puntos georeferenciado respetando sus coordenadas (X,Y)

informadas por el distribuidor.

### 3. Se crearon los 1090 tramos de líneas respetando los postes de los extremos,

longitud informada y tipo de conductor.

4. Se incorporaron las 99 Subestaciones de Distribución (SED) como cargas

puntuales tipo domiciliarias [1], respetando cada uno de los postes de conexión de

estos elementos.

5. Se incorporó cada elemento de compensación de reactivos existente.

6. Se incorporó las máquinas del PMGD HBS GNL.

7. Se realizó el merge entre la modelación del alimentador modelado y la base de

datos de CDEC-SIC de Agosto de 2015.

1 De acuerdo al documento “Metodología para la preparación de escenarios base que se utilizan en los estudios de operación del sic”,

actualizado al mes de Enero de 2014.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 8 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

**Figura 2: Modelación Georeferenciada del Alimentador Laja.**

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 9 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|DIgSILENT<br>S/E El Avellano<br>T ra fo T 2<br>Line01112<br>Avellano 23[kV]<br>66[kV..<br>Avellano<br>Avellano 66[kV]<br>Punto de Conexión Punto de Repercusión<br>Line00010<br>PP126609 Line01051 Id_8145455<br>PP126610<br>Line00090<br>ESTUDIO DE CONEXIÓN DE PMGD Project: 15034<br>CENTRAL HBS ENERGÍA Graphic: Resumen Ejecutiv<br>Propiedad de HBS Energía - Tomaval Date: 9/17/2015<br>Pow erFactory 15.1.7 Realizó Ing. René Moraga Castillo Annex: ES|Col2|Col3|Col4|
|---|---|---|---|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/17/2015<br> Annex: ES<br>Id_8145455<br>**Line01051**<br>**Line00090**<br>**Line01112**<br>**Trafo T2**<br>**Line00010**<br>**DIgSILENT**||ESTUDIO DE CONEXIÓN DE PMGD<br>|Project: 15034|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/17/2015<br> Annex: ES<br>Id_8145455<br>**Line01051**<br>**Line00090**<br>**Line01112**<br>**Trafo T2**<br>**Line00010**<br>**DIgSILENT**||CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br><br><br>|Graphic: Resumen Ejecutiv|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/17/2015<br> Annex: ES<br>Id_8145455<br>**Line01051**<br>**Line00090**<br>**Line01112**<br>**Trafo T2**<br>**Line00010**<br>**DIgSILENT**||CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br><br><br>|Date: 9/17/2015|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/17/2015<br> Annex: ES<br>Id_8145455<br>**Line01051**<br>**Line00090**<br>**Line01112**<br>**Trafo T2**<br>**Line00010**<br>**DIgSILENT**|Pow erFactory 15.1.7|Pow erFactory 15.1.7|Pow erFactory 15.1.7|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/17/2015<br> Annex: ES<br>Id_8145455<br>**Line01051**<br>**Line00090**<br>**Line01112**<br>**Trafo T2**<br>**Line00010**<br>**DIgSILENT**|Pow erFactory 15.1.7|Pow erFactory 15.1.7|Annex: ES|

**Figura 3: Resumen Ejecutivo, con Puntos Relevantes a Monitorear.**

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 10 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|CONFIGURACIÓN PMGD HBS Energía|Project: 15034|
|---|---|---|
||ESTUDIO DE SISTEMA<br> Propiedad de HBS Generación<br> Realizó TECNORED - Ing René Moraga C.<br><br><br>|Graphic: HBS GNL|
||ESTUDIO DE SISTEMA<br> Propiedad de HBS Generación<br> Realizó TECNORED - Ing René Moraga C.<br><br><br>|Date: 9/17/2015|
|PowerFactory 15.1.7|PowerFactory 15.1.7|Annex: Unilineal|

**Figura 4: Modelación Configuración Central HBS Energía.**

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

PÁGINA 11 DE 60

www.tecnored.cl, +56(032)2452686-+56(9)94797525

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

## 4 INFORMACIÓN TÉCNICA DE LA MODELACIÓN

En esta sección se detalla la información técnica más relevante de los equipos

proyectados para la modelación del alimentador Laja, utilizada para la modelación de la

base de datos del software PF DIgSILENT utilizando la información proporcionada por

HBS GNL y CGE Distribución Energía. En la Figura 2, se aprecian los elementos a detallar a

continuación como son el transformador de poder N°02, líneas, bancos de capacitores y

las máquinas sincrónicas. Los parámetros de los cables se recibieron en el Formulario N°2

por lo tanto son los autorizados por CGE Distribución.

### 4.1 Parámetros Conductores

**Tabla 1: Parámetros Conductores.**

**Conductor** **Tensión [kV]** **Corriente máx. a 30°C [kA]** **Fases** **R [Ω/km]** **X [Ω/km]** **R0 [Ω/km]** **X0 [Ω/km]**

AlambreCu 10mm 2ø 23 0,081 2 1,87 0,419 2,018 1,686

AlambreCu 10mm 3ø 23 0,081 3 1,87 0,419 2,018 1,686

CAl 2 AAAC 2ø 23 0,124 2 0,963 0,372 1,111 0,743

CAl 2 AAAC 3ø 23 0,124 3 0,961 0,384 5,966 1,651

CAl 3/0 AAAC 3ø 23 0,226 3 0,38 0,355 3,788 1,622

CCo 150 mm2 3ø 25KV 23 0,298 3 0,248 0,219 0,396 1,841

CCu 16 mm2 2ø 23 0,108 2 1,199 0,409 1,347 1,676

CCu 16 mm2 3ø 23 0,108 3 1,199 0,409 1,347 1,676

CCu 33.6 mm2 3ø 23 0,169 3 0,594 0,387 0,742 1,654

CCu 53.5 mm2 3ø 23 0,228 3 0,377 0,372 0,525 1,639

CCu 85 mm2 3ø 23 0,306 3 0,237 0,358 0,385 1,625

CPR 50 MM2 3Ø 25 KV 23 0,143 3 0,77 0,372 0,918 1,639

CPr 185 MM2 3Ø 25KV 23 0,345 3 0,198 0,331 0,346 1,598

CPr 50 mm2 2ø 25 KV 23 0,143 2 0,77 0,372 0,918 1,639

CPr 70 mm2 2ø 25 KV 23 0,182 2 0,533 0,361 0,681 1,628

CPr 70 mm2 3ø 25 KV 23 0,182 3 0,533 0,361 0,681 1,628

CPr 95 mm2 3ø 25KV 23 0,246 3 0,323 0,14 1,291 0,562

CableCu #5AWG 3ø 23 0,108 3 1,199 0,409 1,347 1,676

XAT Cocesa #1 23kV 3 23 0,17 3 0,524 0,978 0,672 0,715

XLPE # 1 AWG 3F 23K 23 0,17 3 0,524 0,978 0,672 0,715

XLPE 120 mm 23F 23KV 23 0,313 3 0,195 0,964 0,343 0,7

XLPE 70 mm 23F 23KV 23 0,275 3 0,339 0,092 2,454 0,139

### 4.2 Transformadores

**Tabla 2: Parámetros Transformadores.**

**Equipos** **Potencia [MVA]** **Grupo** **Razón** **Z [%]** **Z0 [%]**

T2 10 Dyn1 66/23[kV] 8,64 8,79

23/0.4 [kV] 1,5 [MVA] 1,5 Ynd1 23/0,4[kV] 6,18 6,0

23/0.4 [kV] 2,5 [MVA] 2,5 Ynd1 23/0,4[kV] 6,62 6,0

23/0.4 [kV] 3,2 [MVA] 3,2 Ynd1 23/0,4[kV] 6,62 6,0

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 12 DE 60

### 4.3 Bancos Capacitores 4.4 Generadores

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

**Tabla 3: Parámetros Transformadores.**

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- ESTUDIO DE SISTEMA 15034-E-IN-004 PMGD HBS GNL 6,75[MW] -->

**Tabla 3: Parámetros Transformadores.****

| Potencia<br>Tensión<br>FP<br>Eficiencia<br>Conexión | 1 - 1,355[MW]<br>0,4 [kV]<br>0,8<br>0,98<br>Y |
| --- | --- |
| **XD ** | 2,51[pu] |
| **XQ ** | 2,51 [pu] |
| **X0 ** | 0,03[pu] |
| **X2 ** | 0,21 [pu] |
| **XD**<br>~~**’**~~ | 0,15 [pu] |
| **XD**<br>~~**”**~~ | 0,11 [pu] |
| **rstr** | 0,01[pu] |
| **XdSAT **<br> | 1,2 [pu] |
| **TD**<br>~~**’**~~ | 0,01785235 [s] |
| **TD**<br>~~**”**~~ | 0,00714286 [s] |
| **Cte. Aceleración** | 5,575 [s] |

<!-- Estadísticas: 11 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- ## 5 CONSIDERACIÓN NORMATIVA Este ítem resume los artículos de la NTCO que define los rangos de control de tensión, -->
<!-- FIN TABLA 3 -->


**ID** **Tensión [kV]** **Potencia [MVAr]**

126466 23 0,45

126354 23 0,45

|Potencia<br>Tensión<br>FP<br>Eficiencia<br>Conexión|1 - 1,355[MW]<br>0,4 [kV]<br>0,8<br>0,98<br>Y|
|---|---|
|**XD **|2,51[pu]|
|**XQ **|2,51 [pu]|
|**X0 **|0,03[pu]|
|**X2 **|0,21 [pu]|
|**XD**<br>~~**’**~~|0,15 [pu]|
|**XD**<br>~~**”**~~|0,11 [pu]|
|**rstr**|0,01[pu]|
|**XdSAT **<br>|1,2 [pu]|
|**TD**<br>~~**’**~~|0,01785235 [s]|
|**TD**<br>~~**”**~~|0,00714286 [s]|
|**Cte. Aceleración**|5,575 [s]|

## 5 CONSIDERACIÓN NORMATIVA

Este ítem resume los artículos de la NTCO que define los rangos de control de tensión,

frecuencia, oscilaciones electromecánicas dinámicas y estáticas.

**Artículo 1-4**

Las exigencias que se plantean en la presente NT deben ser cumplidas en el punto de

repercusión o de conexión asociado a cada PMGD, según corresponda de acuerdo al

Reglamento. Dichas exigencias serán aplicables independientemente de que la energía

eléctrica sea producida por unidades generadoras sincrónicas o asincrónicas, con o sin

convertidor de frecuencia, o por unidades generadoras de corriente continua con

inversor.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 13 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

**Artículo 3-18**

Un PMGD no deberá regular activamente la tensión en el punto de repercusión. En el

caso en que la empresa respectiva necesite que el PMGD regule tensión, este servicio

deberá ser acordado por las partes referidas. La elevación de tensión originada por los

PMGD que operan en una red de media tensión de un SD no debe exceder, en el punto

de repercusión asociado a cada uno de ellos, el 6% de la tensión existente sin dichas

inyecciones.

**Artículo 3-26**

El PMGD deberá separarse automáticamente de la red de media tensión del SD, durante

fallas en el circuito al cual está conectado. Cuando el PMGD esté conectado a una red de

media tensión de un SD en el que existe reconexión, el tiempo de despeje de la

protección de desacoplamiento deberá ser lo suficientemente breve como para

garantizar que el PMGD se separe de la red de media tensión durante el período sin

tensión, antes de la reconexión. La conexión o cierre del interruptor de acoplamiento

deberá ser impedida mientras la tensión de la red de media tensión del SD se mantenga

por debajo del valor de operación de la protección contra caídas de la tensión, según se

especifica en el Artículo 3-31 de la presente NT.

**Artículo 3-28**

Si cualquiera de las tensiones entre fases medidas alcanza uno de los rangos indicados en

el presente artículo, el PMGD deberá separarse de la red de media tensión del SD, en el

tiempo de despeje señalado. Se entenderá como tiempo de despeje como el tiempo que

transcurre entre el inicio de la condición en Estado de Alerta y la separación de la red de

media tensión del SD. Los ajustes de tensión y tiempo de despeje podrán ser ajustables

en terreno.

**Tabla 4: Rangos de Tensión.**

**Tensión [% Vn]** **T. Despeje [s]**

V < 50 0,16

50 ≤ V ≤ 90 2

110 < V < 120 1

V ≥ 120 0,16

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 14 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

**Artículo 3-29**

Cuando la frecuencia nominal del SD está en los rangos indicados en el presente artículo,

el PMGD deberá separarse de la red de media tensión del SD, en los tiempos de despeje

señalados que se indican. Los ajustes de frecuencia y tiempo de despeje podrán ser

ajustables en terreno.

**Tabla 5: Rangos Frecuencia.**

**Frecuencia [% Fn]** **T.Despeje [s]**

 - 50,5 0,16

(49,5 a 48) de 16 a 300

< 48 0,16

**Artículo 3-31**

El PMGD no podrá ser conectado a la red de media tensión del SD, luego de ocurrida una

perturbación en la red de media tensión, hasta que la tensión y la frecuencia en el punto

de conexión estén en los rangos 0,94 a 1,06 VC y 49,6 a 50,4 Hz, respectivamente. La

reconexión del PMGD a la red deberá hacerse en conformidad con el mecanismo de

coordinación acordado con la empresa respectiva.

**Artículo 3-35**

En caso de presentarse una operación en isla de manera involuntaria debido a una falla

en el SD, la Instalación de Conexión del PMGD deberá detectar la situación y

desconectarse de la red de media tensión del SD en un tiempo máximo de 2 segundos.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 15 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

## 6 METODOLOGÍA

En este capítulo se define la metodología utilizada para el desarrollo de los Estudios de

Impacto debido a la conexión del PMGD HBS GNL, para esto se utilizaron una serie de

escenarios con el fin de identificar los diferentes escenarios de operación, las obras

requeridas para cumplir con la NTCO y el responsable de realizar dicho plan de obras.

En primer lugar con la modelación detallada del alimentador y el plan de obras de este,

se creará un escenario de operación que corresponde a las demandas del año que ha

sido entregado junto al Formulario N°2 (en este caso años 2014-2015), recibiendo el

nombre de Caso Base. Con el porcentaje de crecimiento del sistema recibido, se

proyectará la demanda máxima a la fecha de puesta en servicio del PMGD, con este

“Caso Base Proyectado”, a partir de este se realizan las simulaciones de flujo de potencia

para las condiciones más extremas como son demanda baja observando el

comportamiento del perfil de tensiones y el porcentaje de carga, en caso de existir

problemas con alguno de los dos parámetros monitoreados se propondrá un plan de

obra para solucionar los incumplimientos normativos. Este plan de obra será de cargo de

la empresa distribuidora, ya que solo se ha analizado el crecimiento vegetativo de las

cargas.

Luego se proyectará la demanda mínima a la fecha de puesta en servicio, incorporando

las obras requeridas con el análisis anterior. El escenario creado será “Caso Base + Obras

del Dx”, se procederá a despachar el PMGD a su máxima potencia y monitorear las

variables de interés; en este caso la potencia inyectada por el PMGD recorrerá el mayor

camino eléctrico debido a ser un escenario de demanda baja, por lo que si existen

problemas de tensión o sobrecargas, serán estas obras de cargo del propietario de la

nueva generación.

### 6.1 Escenario de Demanda

Para la proyección de demanda, se ha utilizado los datos horarios de los año 2014-2015

identificando la máxima y mínima demanda, las que han sido proyectadas de acuerdo al

porcentaje de crecimiento de 5,1% informado por el propietario del alimentador.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 16 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

**Tabla 6: Proyección Demanda.**

**2014-2015** **2016**

**Demanda Alta** 3,81 4,20

**Demanda Baja** 0,36 0,33

A continuación se presentan dos gráficos, una es la curva de demanda horaria del

alimentador Laja, la otra gráfica corresponde al ordenamiento de mayor a menor de las

demandas anuales, esto con el fin de determinar los valores extremos requeridos para la

actualización de las demandas.

**Figura 5: Curva de Demanda Horaria.**

**Figura 6: Curva Demanda Horaria Ordenada de Mayor a Menor.**

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 17 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

### 6.2 Escenario de Operación

La identificación de los escenarios para cada uno de los estudios, se ha creado mediante

una serie de claves que permitirán otorgar nombres simples, pero que de forma efectiva

darán una información muy completa de los casos analizados. Estas claves se detallan en

la Tabla 7.

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- darán una información muy completa de los casos analizados. Estas claves se detallan en la Tabla 7. -->

**Tabla 7: Código para Identificación de Escenarios Simulados.****

| Ítem | Abreviatura | Descripción |
| --- | --- | --- |
| Estudio | CC | Cortocircuito |
| Estudio | D | Dinámico |
| Estudio | FP | Flujo de Potencia |
| Demanda | A | Alta |
| Demanda | B | Baja |
| Caso | 0 | Base + Obras del Dx + PMGD existente |
| Caso | 1 | Caso 0 + Obras Propuestas al Dx |
| Caso | 2 | Caso 1 + Obras del PMGD GNL |
| PMGD GNL | 0 | Off |
| PMGD GNL | 1 | On |
| Sin Identificación | - | - |
| Falla | 3F | Falla Trifásica |
| Falla | 2F | Falla Bifásica |
| Falla | 2FT | Falla Bifásica a Tierra |
| Falla | 1FT | Falla Monofásica a Tierra |
| Contingencia | PG | Perdida Generación |
| Contingencia | CC | Cortocircuito |

<!-- Estadísticas: 17 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Con estos códigos, en cada sección de los diferentes estudios se identificarán los escenarios utilizados para obtener el impacto de la conexión del PMGD al alimentador -->
<!-- FIN TABLA 7 -->


**Tabla 7: Código para Identificación de Escenarios Simulados.**

|Ítem|Abreviatura|Descripción|
|---|---|---|
|Estudio|CC|Cortocircuito|
|Estudio|D|Dinámico|
|Estudio|FP|Flujo de Potencia|
|Demanda|A|Alta|
|Demanda|B|Baja|
|Caso|0|Base + Obras del Dx + PMGD existente|
|Caso|1|Caso 0 + Obras Propuestas al Dx|
|Caso|2|Caso 1 + Obras del PMGD GNL|
|PMGD GNL|0|Off|
|PMGD GNL|1|On|
|Sin Identificación|-|-|
|Falla|3F|Falla Trifásica|
|Falla|2F|Falla Bifásica|
|Falla|2FT|Falla Bifásica a Tierra|
|Falla|1FT|Falla Monofásica a Tierra|
|Contingencia|PG|Perdida Generación|
|Contingencia|CC|Cortocircuito|

Con estos códigos, en cada sección de los diferentes estudios se identificarán los

escenarios utilizados para obtener el impacto de la conexión del PMGD al alimentador

Laja.

### 6.3 Estudio de Cortocircuito

El estudio de cortocircuito forma parte de los análisis del comportamiento estático de la

conexión del PMGD, para fines de verificación de los interruptores existentes y

proyectados. El cálculo de las corrientes de falla se realizó utilizando el Método IEC

60909, seleccionando la determinación de las corrientes máximas, el modelo con las tres

mallas de secuencia disponibles y una condición de pre-falla con un factor de tensión de

1,1 en los nodos del sistema.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 18 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

Se determinaron los niveles de corrientes de falla en los distintos postes, siendo los más

relevantes las corrientes obtenidas en el punto de conexión y los de repercusión.; Las

corrientes de falla evaluadas son monofásica a tierra, bifásica, bifásica a tierra y trifásica.

**Tabla 8: Escenarios Simulados Estudio Cortocircuito.**

Item1 PMGD Caso

CC 0 0

CC 1 2

### 6.4 Estudio de Flujos de Potencia

La verificación de lo establecidos en la NTCO sobre la calidad de servicio, se realizó

analizando la operación del alimentador en condiciones estáticas determinando el

desempeño del perfil de tensión, porcentaje de carga de los elementos serie, potencia

transferida, entre otros. En la Tabla 9, se presentan los escenarios simulados en el

estudio de flujo de potencia.

**Tabla 9: Escenarios Simulados Estudio Flujos de Potencia.**

Item1 Item2 Año PMGD Caso

F A 16 0 0

F A 16 1 1

F A 16 1 2

F B 16 0 0

F B 16 1 1

F B 16 1 2

### 6.5 Estudio de Comportamiento Dinámico

La verificación del impacto en la estabilidad dinámica del alimentador Laja, corresponde

a la simulación en función del tiempo de contingencias ocurridas en la red de

distribución, tanto para fallas ocurridas en tramos de líneas como pérdida de la

generación.

La evaluación del impacto que provoca el ingreso del nuevo generador se realizará de

manera cualitativa, mediante las variables como tensión, frecuencia del sistema y

generación del PMGD, se considerará un tiempo de 400[ms] para los elementos de

protección del alimentador y 120[ms] para la protección del generador.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 19 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

**Tabla 10: Escenarios Simulados Estudio Dinámico.**

Item2 Item1 PMGD Contingencia

D A 1 PG

D A 1 CC

D B 1 PG

D B 1 CC

## 7 DESARROLLO ESTUDIO DE CORTOCIRCUITO

La determinación del impacto que presenta la incorporación del PMGD, se determinó

mediante simulaciones con y sin excedentes de energía para poder determinar el

impacto en los casos extremos del alimentador. El cálculo de cortocircuitos se efectuó en

toda la extensión del alimentador Laja, considerando instalaciones con niveles de tensión

desde 66[kV] a 23[kV], calculando la máxima corriente de cortocircuito esperada

utilizando el procedimiento DO, de esta forma se cuantifica la máxima solicitud posible a

la que podrían estar expuestos los equipos de interrupción de corrientes de falla. Los

resultados de las corrientes de falla se han realizado cumpliendo con lo siguiente:

 En los casos con PMGD, se ha despachado a potencia máxima y con todo el

alimentador conectado.

 El cálculo se efectúa para un nivel de tensión de pre falla en barras de 110%

sobre las tensiones nominales de cada barra del sistema, según la

metodología indicada anteriormente.

### 7.1 Resultados Estudio de Cortocircuito

Los resultados de los niveles de cortocircuitos se encuentran resumidos en las tablas

siguientes y en los anexos digitales, donde se incluye las corrientes de cortocircuito

estacionario (Iks), potencia de cortocircuito (Skss), corriente residual (3xI0), Corriente de

Ruptura (Ib), y corriente máxima (ip).

En el cuerpo del informe se presentarán los postes más relevantes, estando la totalidad

de los resultados como anexo digital en formato PDF. Lo puntos destacados son:

 Avellano: Barra 66[kV] en S/E El Avellano.

 539738 ó Avellano 23[kV]: Cabecera alimentador 23[kV] en S/E El Avellano.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 20 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

 126610: Punto de Conexión 23[kV].

 126609: Punto de Repercusión más cercano 23[kV].

#### 7.1.1 Escenario CC-00

**Tabla 11 : Resultados Cortocircuito Trifásico.**

**Ubicación Falla** **Skss [MVA]** **Iks [kA]** **ip** **[kA]** **Ib [kA]**

Avellano 23[kV] 78,216 1,963 4,895 1,963

Avellano 66[kV] 326,051 2,852 6,096 2,852

126609 38,436 0,965 1,801 0,965

126610 38,38 0,963 1,798 0,963

821739 38,322 0,962 1,791 0,962

**Tabla 12: Resultados Cortocircuito Bifásico.**

**Ubicación Falla** **Skss [MVA]** **Iks [kA]** **ip** **[kA]** **Ib [kA]**

Avellano 23[kV] 22,604 1,702 4,25 1,702

Avellano 66[kV] 94,611 2,483 5,331 2,483

126609 11,103 0,836 1,561 0,836

126610 11,087 0,835 1,558 0,835

821739 11,07 0,834 1,553 0,834

**Tabla 13: Resultados Cortocircuito Bifásico a Tierra.**

**Ubicación Falla** **Skss [MVA]** **Iks [kA]** **ip** **[kA]** **Ib [kA]** **3xI0 [kA]**

Avellano 23[kV] 26,597 2,003 5,101 2,003 2,308

Avellano 66[kV] 108,847 2,856 6,138 2,856 2,892

126609 11,187 0,842 1,602 0,842 0,501

126610 11,169 0,841 1,599 0,841 0,5

821739 11,17 0,841 1,594 0,841 0,499

**Tabla 14: Resultados Cortocircuito Monofásica a Tierra.**

**Ubicación Falla** **Skss [MVA]** **Iks [kA]** **ip** **[kA]** **Ib [kA]** **3xI0 [kA]**

Avellano 23[kV] 28,219 2,125 5,484 2,125 2,125

Avellano 66[kV] 110,007 2,887 6,236 2,887 2,887

126609 8,782 0,661 1,324 0,661 0,661

126610 8,766 0,66 1,321 0,66 0,66

821739 8,744 0,658 1,311 0,658 0,658

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 21 DE 60

#### 7.1.2 Escenario CC-12

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

**Tabla 15: Resultados Cortocircuito Trifásico.**

**Ubicación Falla** **Skss [MVA]** **Iks [kA]** **ip** **[kA]** **Ib [kA]**

Avellano 23[kV] 109,749 2,705 6,411 2,725

Avellano 66[kV] 350,839 2,995 6,531 3,066

126609 94,743 2,353 5,056 2,116

126610 94,788 2,354 5,063 2,115

821739 94,158 2,338 4,982 2,106

B23kV-Energia 94,015 2,335 4,995 2,099

B23kV-GNL 94,788 2,354 5,063 2,115

**Tabla 16: Resultados Cortocircuito Bifásico.**

**Ubicación Falla** **Skss [MVA]** **Iks [kA]** **ip** **[kA]** **Ib [kA]**

Avellano 23[kV] 31,214 2,351 5,513 2,351

Avellano 66[kV] 101,42 2,662 5,694 2,662

126609 25,362 1,91 4,092 1,91

126610 25,367 1,91 4,097 1,91

821739 25,222 1,899 4,037 1,899

B23kV-Energia 25,15 1,894 4,038 1,894

B23kV-GNL 25,367 1,91 4,097 1,91

**Tabla 17: Resultados Cortocircuito Bifásico a Tierra.**

**Ubicación Falla** **Skss [MVA]** **Iks [kA]** **ip** **[kA]** **Ib [kA]** **3xI0 [kA]**

Avellano 23[kV] 35,829 2,698 6,457 2,698 2,922

Avellano 66[kV] 115,578 3,033 6,496 3,033 2,971

126609 37,793 2,846 6,262 2,846 4,277

126610 38,05 2,865 6,318 2,865 4,335

821739 38,079 2,868 6,089 2,868 4,133

B23kV-Energia 37,65 2,835 6,192 2,835 4,251

B23kV-GNL 38,05 2,865 6,318 2,865 4,335

**Tabla 18: Resultados Cortocircuito Monofásica a Tierra.**

**Ubicación Falla** **Skss [MVA]** **Iks [kA]** **ip** **[kA]** **Ib [kA]** **3xI0 [kA]**

Avellano 23[kV] 35,829 2,698 6,457 2,698 2,922

Avellano 66[kV] 115,578 3,033 6,496 3,033 2,971

126609 37,793 2,846 6,262 2,846 4,277

126610 38,05 2,865 6,318 2,865 4,335

821739 38,079 2,868 6,089 2,868 4,133

B23kV-Energia 37,65 2,835 6,192 2,835 4,251

B23kV-GNL 38,05 2,865 6,318 2,865 4,335

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 22 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

### 7.2 Valores Máximos

En este punto se presentan los valores máximos obtenidos para las corrientes simétricas,

asimétricas y peak (SOTF), con el fin de poder contrastar estos con los valores de cada

equipo; en caso que ningún dispositivo de protección tengo un valor de ruptura inferior a

los máximos, significa que bajo ningún escenario de operación existe un elemento que

vea superada su capacidad de ruptura.

**Tabla 19: Resumen de Valores Máximos.**

**Ubicación Falla** **Skss [MVA]** **Iks [kA]** **Iks [kA]** **ip [kA]** **Ib [kA]** **3xI0 [kA]**

Avellano 23[kV] 109,749 2,796 2,796 6,842 2,796 2,922

126609 94,743 2,846 2,846 6,262 2,846 4,277

126610 94,788 2,865 2,865 6,318 2,865 4,335

821739 94,158 2,868 2,868 6,089 2,868 4,133

B23kV-Energia 94,015 2,835 2,835 6,192 2,835 4,251

B-BG#1 28,061 40,503 40,165 90,079 37,655 0

B-BG#2 30,251 43,664 43,322 97,417 38,578 0

B-BG#3 29,565 42,673 42,342 91,78 37,589 0

B-BG#4 29,565 42,673 42,342 91,78 37,589 0

B23kV-GNL 94,788 2,865 2,865 6,318 2,865 4,335

B-GN#1 35,85 51,745 51,275 116,455 48,821 0

B-GN#2 28,102 40,562 40,222 90,305 37,714 0

B-GN#3 28,102 40,562 40,222 90,305 37,714 0

B-GN#4 43,687 63,056 62,555 142,38 57,236 0

B-GN#5 43,687 63,056 62,555 142,38 57,236 0

### 7.3 Capacidad Nominal de los Interruptores y Equipos de Protección

La verificación de la correcta capacidad de ruptura de los equipos existentes, se realizará

en base a la información oficial recibida desde la empresa propietaria del alimentador y

el cliente dueño del PMGD. En la tabla siguiente se resume la información de los equipos

de protección utilizados y que están presentes en diferentes ubicaciones dentro del

sistema de distribución, asimismo en las instalaciones de generación.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 23 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

**Tabla 20: Interruptores y Equipos de Protección Involucrados.**

**Equipo** **Tensión[kV]** **Inominal[A]** **Iruptura Sim.[kA]** **Iruptura Asim.[kA]** **SOTF[kA]**

Cabecera NOVA-27 27 630 12,5 20 32

Punto Conexión NOJA-27 27 630 12,5 20 31,5

Int.Mitsubishi [2] 0,4 3200 50 65 94,5

### 7.4 Comentarios Resultados ECC

De acuerdo a la información presentada en Tabla 19 y Tabla 20, el procedimiento DO

indica que los interruptores de los generadores verían superada su capacidad de ruptura;

sin embargo, se debe utilizar el método detallado para analizar la corriente que verán

realmente esos equipos. De la Figura 7, se aprecia que los generadores aportan 11[kA]

aproximadamente a las fallas [3] siendo capaces de soportar su aporte a las corrientes de

fallas; la corriente restante una parte viene del sistema que se ve reflejada por la razón

de trasformación (23/0,4[kV]) y los generadores cercanos (Energía & GNL).

Por lo tanto, no existen equipos de protección que vean superada su capacidad de

ruptura en ningún escenario. Cabe señalar que los mayores aumentos de corrientes de

falla, por topografía ocurren en el punto de conexión producto del PMGD y Cabecera por

aportes del Sistema.

2 Este equipo es referencial, el dispositivo final será este o uno de iguales características.

3 Aporte del generador depende de la tensión y la reactancia inductiva de la máquina.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 24 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|CONFIGURACIÓN PMGD HBS Energía|Project: 15034|
|---|---|---|
||ESTUDIO DE SISTEMA<br> Propiedad de HBS Generación<br> Realizó TECNORED - Ing René Moraga C.<br><br><br>|Graphic: HBS GNL|
||ESTUDIO DE SISTEMA<br> Propiedad de HBS Generación<br> Realizó TECNORED - Ing René Moraga C.<br><br><br>|Date: 9/21/2015|
|PowerFactory 15.1.7|PowerFactory 15.1.7|Annex: Unilineal|

**Figura 7: Resultados Método Detallado.**

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

PÁGINA 25 DE 60

www.tecnored.cl, +56(032)2452686-+56(9)94797525

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

## 8 DESARROLLO ESTUDIO DE FLUJOS DE POTENCIA

Con el estudio de flujos de potencia se busca examinar el desempeño del sistema de

distribución, ante diferentes niveles de demanda, operación, refuerzos y equipos de

compensación. Este capítulo utilizó la Metodología explicada al comienzo del Capítulo 6,

comenzando con simulaciones del caso base para luego incorporar el PMGD, con el fin de

poder evaluar el desempeño del sistema identificando las obras de refuerzo requeridas.

Los resultados son entregados en forma de tablas resúmenes en el cuerpo del informe,

encontrándose la totalidad de los resultados y archivos nativos en forma de anexos. La

principal información incluida es:

 Tensiones en los principales postes (nodos).

 Transferencias por elementos series.

 Nivel de Carga por elementos series.

 Nivel de carga transformadores de la red de distribución.

### 8.1 Resultados Flujos de Potencia Sin PMGD HBS GNL

En esta sección mediante la proyección de la demanda al año de puesta en servicio del

PMGD, se buscará identificar si existe alguna necesidad de mejora en el alimentador, que

no se encuentre en el plan de obra recibido, que signifique un eventual reforzado o

compensación en el alimentador para cumplir con lo establecido en la NTCO

considerando el aumento de demanda. En esta sección se considerará demanda baja y

alta del alimentador, sumado al PMGD HBS Energía despachado en todo momento.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 26 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

#### 8.1.1 Escenario: FA1600

|DIgSILENT<br>1,0900<br>[p.u.]<br>1,0540<br>1,0180<br>0,9820<br>0,9460<br>0,9100<br>-0,0000 5,7814 11,563 17,344 23,126 [km] 28,907<br>Avell.. 525592 494227 469428 926574 204845 241785 494252 242000 494264 494272 494280 494287 494296 126354 703089 126371 470378 126387 126395 126403 282515 126421 126431 126439 126447 126455 239904 239910 204480 239928 239935 239941 239946 126516 126524 126532 126540 126548 126556 126564 126572 126580 126588 126596 126604 126612 126620 126628 126636 126644 282572 204839 126663 126671 126679 126687 126695 823103 468313 126719 610640 126735 126743 126751 126759 279293<br>El<br>S/E<br>Voltage, Magnitude Voltage, Magnitude<br>Voltage, Magnitude|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>PerfilTensión-Laja<br>CENTRAL HBS GNL<br>Realizó TECNORED - Ing. René Moraga Castillo<br><br>|Date: 9/21/2015<br> Annex: /1|

**Figura 8: Perfil de Tensión, Tensión Cabecera = 1[pu].**

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 27 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|DIgSILENT<br>S/E El Avellano<br>Ul=22,652 kV Grid: Summary Grid<br>u=0,985 p.u.<br>Generation = 7336,20 MW 756,26 Mvar 7375,07 MVA<br>Ul=65,774 kV phiu=-29,698 deg External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br>u=0,997 p.u. Inter Area Flow = 0,00 MW 0,00 Mvar<br>phiu=0,422 deg Load P(U) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br>Load P(Un) = 6996,51 MW 1339,32 Mvar 7123,55 MVA rP = -0,2 3 9 M W<br>Load P(Un-U) = -0,00 MW -0,00 Mvar AQ = -1,0 5 1 M va<br>Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA Losses = 339,69 MW 336,31 Mvar Line Charging = -2684,50 Mvar Compensation ind. = 1111,61 Mvar varP = 0,2 51 M W lo a d in g = 1 3,7 0 7 %Trafo T2 I= 0,0 2 7 kAS = 1,0 7 7 M V P I QS l = === o0 011, a,,,2 d000 i 3 257. n.. ... ... . Line01112<br>Avellano 23[kV] Compensation cap. = -2030,97 Mvar Installed Capacity = 9680,22 MW kAS = 1,0 93 M V AQ = 1,06 4 M<br>Spinning Reserve = 2344,02 MW Total Power Factor: Generation = 0,99 [-] 66[kV.. lo adin g= 1 3,707 %I= 0,010<br>Load/Motor = 0,98 / 0,00 [-] 0u6,95 =,. 90.....<br>Avellano 66[kV] Avellano upUl =h= i<br>Punto Conexión Punto Repercusión<br>Id_9048591<br>Ul=23,409 kV u=1,018 p.u. Q=0,169 MW P=0,827 loadin.. I=0,02.. S=0,84.. Q=-0,1.. P=-0,8..<br>Ul=23,410 kV P=0,002 MW phiu=-27,917 deg 0,844 r = Sa Mv Line00126<br>u=1,018 p.u. Q=0,000 Mvar phiu=-27,916 deg S=0,002 MVA % ading=11,437 oA lk I=0,021 MVA kAS = 0,1 0 6 M V AQ = 0,0 2 1 M va rP = 0,1 0 4 M W<br>PP702963 Line01019 P=0,102 MW Q=0,021 Mvar kAS = 3,1 4 6 M V AQ = -0,3 2 9 M va rP = 3,1 2 8 M W lo a d iL ni gne =0 2,10 11 18 3 %I= 0,0 0 3 Il SP Q =o=== 0- a0-,, 0 0d01, i, 01 n00 .. ..... ...<br>PP702966 S=0,105 MVA I=0,003 kA Line lo a d i0 n g = 40 2,6 21 8 %2 I=5 0,0 7 8<br>loading=2,079 %<br>ESTUDIO DE CONEXIÓN DE PMGD Project: 15034<br>CENTRAL HBS ENERGÍA Graphic: Resumen Ejecutiv<br>Propiedad de HBS energía - Tomaval Date: 9/21/2015<br>Pow erFactory 15.1.7 Realizó Ing. René Moraga Castillo Annex: ES|Col2|Col3|Col4|
|---|---|---|---|
|**_PP702966_**<br>**_PP702963_**<br>**_Punto Repercusión_**<br>**_Punto Conexión_**<br>~~**_A_**~~**_vellano 66[kV]_**<br>**_Avellano 23[kV]_**<br>**_S/E El Avellano_**<br>Avellano 66[kV..<br>Ul=65,..<br>u=0,99..<br>phiu=0..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/21/2015<br> Annex: ES<br>~~U~~l~~=65,774~~ ~~kV~~<br>u=0,997 p.u.<br>phiu=0,422 deg<br>~~ G~~r~~i~~d~~:~~ ~~Summar~~y~~ G~~r~~i~~d <br> <br> Generation = 7336,20 MW 756,26 Mvar 7375,07 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un-U) = -0,00 MW -0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 339,69 MW 336,31 Mvar<br> Line Charging = -2684,50 Mvar<br> Compensation ind. = 1111,61 Mvar<br> Compensation cap. = -2030,97 Mvar<br> Installed Capacity = 9680,22 MW<br> Spinning Reserve = 2344,02 MW<br> Total Power Factor:<br> Generation = 0,99 [-]<br> Load/Motor = 0,98 / 0,00 [-] <br>~~Ul=22~~,~~652 kV~~<br>u=0,985 p.u.<br>phiu=-29,698 deg<br>~~Ul=23~~,~~410~~ ~~kV~~<br>u=1,018 p.u.<br>phiu=-27,916 deg<br>~~U~~l~~=23,40~~9~~ kV~~<br>u=1,018 p.u.<br>phiu=-27,917 deg<br>Id_9048591<br>~~P=0~~,~~002~~ ~~MW~~<br>Q=0,000 Mvar<br>S=0,002 MVA<br>Line01019<br>~~P=0~~,~~10~~2~~ MW~~<br>Q=0,021 Mvar<br>S=0,105 MVA<br>I=0,003 kA<br>loading=2,079 %<br>Line01018<br>P=0,104 MW<br>Q=0,021 Mvar<br>S=0,106 MVA<br>I=0,003 kA<br>loading=2,113 %<br>P=-0,1..<br>Q=-0,0..<br>S=0,10..<br>I=0,00..<br>loadin..<br>Line00126<br>P=0,827 MW<br>Q=0,169 Mvar<br>S=0,844 MVA<br>I=0,021 kA<br>loading=11,437 %<br>P=-0,8..<br>Q=-0,1..<br>S=0,84..<br>I=0,02..<br>loadin..<br>Line00125<br>P=3,128 MW<br>Q=-0,329 Mvar<br>S=3,146 MVA<br>I=0,078 kA<br>loading=42,628 %<br>Trafo T2<br>P=0,251 MW<br>Q=1,064 Mvar<br>S=1,093 MVA<br>I=0,010 kA<br>loading=13,707 %<br>P=-0,239 MW<br>Q=-1,051 Mvar<br>S=1,077 MVA<br>I=0,027 kA<br>loading=13,707 %<br>Line01112<br>P=0,23..<br>Q=1,05..<br>S=1,07..<br>I=0,02..<br>loadin..<br>**DIgSILENT**||ESTUDIO DE CONEXIÓN DE PMGD<br>|Project: 15034|
|**_PP702966_**<br>**_PP702963_**<br>**_Punto Repercusión_**<br>**_Punto Conexión_**<br>~~**_A_**~~**_vellano 66[kV]_**<br>**_Avellano 23[kV]_**<br>**_S/E El Avellano_**<br>Avellano 66[kV..<br>Ul=65,..<br>u=0,99..<br>phiu=0..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/21/2015<br> Annex: ES<br>~~U~~l~~=65,774~~ ~~kV~~<br>u=0,997 p.u.<br>phiu=0,422 deg<br>~~ G~~r~~i~~d~~:~~ ~~Summar~~y~~ G~~r~~i~~d <br> <br> Generation = 7336,20 MW 756,26 Mvar 7375,07 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un-U) = -0,00 MW -0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 339,69 MW 336,31 Mvar<br> Line Charging = -2684,50 Mvar<br> Compensation ind. = 1111,61 Mvar<br> Compensation cap. = -2030,97 Mvar<br> Installed Capacity = 9680,22 MW<br> Spinning Reserve = 2344,02 MW<br> Total Power Factor:<br> Generation = 0,99 [-]<br> Load/Motor = 0,98 / 0,00 [-] <br>~~Ul=22~~,~~652 kV~~<br>u=0,985 p.u.<br>phiu=-29,698 deg<br>~~Ul=23~~,~~410~~ ~~kV~~<br>u=1,018 p.u.<br>phiu=-27,916 deg<br>~~U~~l~~=23,40~~9~~ kV~~<br>u=1,018 p.u.<br>phiu=-27,917 deg<br>Id_9048591<br>~~P=0~~,~~002~~ ~~MW~~<br>Q=0,000 Mvar<br>S=0,002 MVA<br>Line01019<br>~~P=0~~,~~10~~2~~ MW~~<br>Q=0,021 Mvar<br>S=0,105 MVA<br>I=0,003 kA<br>loading=2,079 %<br>Line01018<br>P=0,104 MW<br>Q=0,021 Mvar<br>S=0,106 MVA<br>I=0,003 kA<br>loading=2,113 %<br>P=-0,1..<br>Q=-0,0..<br>S=0,10..<br>I=0,00..<br>loadin..<br>Line00126<br>P=0,827 MW<br>Q=0,169 Mvar<br>S=0,844 MVA<br>I=0,021 kA<br>loading=11,437 %<br>P=-0,8..<br>Q=-0,1..<br>S=0,84..<br>I=0,02..<br>loadin..<br>Line00125<br>P=3,128 MW<br>Q=-0,329 Mvar<br>S=3,146 MVA<br>I=0,078 kA<br>loading=42,628 %<br>Trafo T2<br>P=0,251 MW<br>Q=1,064 Mvar<br>S=1,093 MVA<br>I=0,010 kA<br>loading=13,707 %<br>P=-0,239 MW<br>Q=-1,051 Mvar<br>S=1,077 MVA<br>I=0,027 kA<br>loading=13,707 %<br>Line01112<br>P=0,23..<br>Q=1,05..<br>S=1,07..<br>I=0,02..<br>loadin..<br>**DIgSILENT**||CENTRAL HBS ENERGÍA<br> Propiedad de HBS energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br><br><br>|Graphic: Resumen Ejecutiv|
|**_PP702966_**<br>**_PP702963_**<br>**_Punto Repercusión_**<br>**_Punto Conexión_**<br>~~**_A_**~~**_vellano 66[kV]_**<br>**_Avellano 23[kV]_**<br>**_S/E El Avellano_**<br>Avellano 66[kV..<br>Ul=65,..<br>u=0,99..<br>phiu=0..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/21/2015<br> Annex: ES<br>~~U~~l~~=65,774~~ ~~kV~~<br>u=0,997 p.u.<br>phiu=0,422 deg<br>~~ G~~r~~i~~d~~:~~ ~~Summar~~y~~ G~~r~~i~~d <br> <br> Generation = 7336,20 MW 756,26 Mvar 7375,07 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un-U) = -0,00 MW -0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 339,69 MW 336,31 Mvar<br> Line Charging = -2684,50 Mvar<br> Compensation ind. = 1111,61 Mvar<br> Compensation cap. = -2030,97 Mvar<br> Installed Capacity = 9680,22 MW<br> Spinning Reserve = 2344,02 MW<br> Total Power Factor:<br> Generation = 0,99 [-]<br> Load/Motor = 0,98 / 0,00 [-] <br>~~Ul=22~~,~~652 kV~~<br>u=0,985 p.u.<br>phiu=-29,698 deg<br>~~Ul=23~~,~~410~~ ~~kV~~<br>u=1,018 p.u.<br>phiu=-27,916 deg<br>~~U~~l~~=23,40~~9~~ kV~~<br>u=1,018 p.u.<br>phiu=-27,917 deg<br>Id_9048591<br>~~P=0~~,~~002~~ ~~MW~~<br>Q=0,000 Mvar<br>S=0,002 MVA<br>Line01019<br>~~P=0~~,~~10~~2~~ MW~~<br>Q=0,021 Mvar<br>S=0,105 MVA<br>I=0,003 kA<br>loading=2,079 %<br>Line01018<br>P=0,104 MW<br>Q=0,021 Mvar<br>S=0,106 MVA<br>I=0,003 kA<br>loading=2,113 %<br>P=-0,1..<br>Q=-0,0..<br>S=0,10..<br>I=0,00..<br>loadin..<br>Line00126<br>P=0,827 MW<br>Q=0,169 Mvar<br>S=0,844 MVA<br>I=0,021 kA<br>loading=11,437 %<br>P=-0,8..<br>Q=-0,1..<br>S=0,84..<br>I=0,02..<br>loadin..<br>Line00125<br>P=3,128 MW<br>Q=-0,329 Mvar<br>S=3,146 MVA<br>I=0,078 kA<br>loading=42,628 %<br>Trafo T2<br>P=0,251 MW<br>Q=1,064 Mvar<br>S=1,093 MVA<br>I=0,010 kA<br>loading=13,707 %<br>P=-0,239 MW<br>Q=-1,051 Mvar<br>S=1,077 MVA<br>I=0,027 kA<br>loading=13,707 %<br>Line01112<br>P=0,23..<br>Q=1,05..<br>S=1,07..<br>I=0,02..<br>loadin..<br>**DIgSILENT**||CENTRAL HBS ENERGÍA<br> Propiedad de HBS energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br><br><br>|Date: 9/21/2015|
|**_PP702966_**<br>**_PP702963_**<br>**_Punto Repercusión_**<br>**_Punto Conexión_**<br>~~**_A_**~~**_vellano 66[kV]_**<br>**_Avellano 23[kV]_**<br>**_S/E El Avellano_**<br>Avellano 66[kV..<br>Ul=65,..<br>u=0,99..<br>phiu=0..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/21/2015<br> Annex: ES<br>~~U~~l~~=65,774~~ ~~kV~~<br>u=0,997 p.u.<br>phiu=0,422 deg<br>~~ G~~r~~i~~d~~:~~ ~~Summar~~y~~ G~~r~~i~~d <br> <br> Generation = 7336,20 MW 756,26 Mvar 7375,07 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un-U) = -0,00 MW -0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 339,69 MW 336,31 Mvar<br> Line Charging = -2684,50 Mvar<br> Compensation ind. = 1111,61 Mvar<br> Compensation cap. = -2030,97 Mvar<br> Installed Capacity = 9680,22 MW<br> Spinning Reserve = 2344,02 MW<br> Total Power Factor:<br> Generation = 0,99 [-]<br> Load/Motor = 0,98 / 0,00 [-] <br>~~Ul=22~~,~~652 kV~~<br>u=0,985 p.u.<br>phiu=-29,698 deg<br>~~Ul=23~~,~~410~~ ~~kV~~<br>u=1,018 p.u.<br>phiu=-27,916 deg<br>~~U~~l~~=23,40~~9~~ kV~~<br>u=1,018 p.u.<br>phiu=-27,917 deg<br>Id_9048591<br>~~P=0~~,~~002~~ ~~MW~~<br>Q=0,000 Mvar<br>S=0,002 MVA<br>Line01019<br>~~P=0~~,~~10~~2~~ MW~~<br>Q=0,021 Mvar<br>S=0,105 MVA<br>I=0,003 kA<br>loading=2,079 %<br>Line01018<br>P=0,104 MW<br>Q=0,021 Mvar<br>S=0,106 MVA<br>I=0,003 kA<br>loading=2,113 %<br>P=-0,1..<br>Q=-0,0..<br>S=0,10..<br>I=0,00..<br>loadin..<br>Line00126<br>P=0,827 MW<br>Q=0,169 Mvar<br>S=0,844 MVA<br>I=0,021 kA<br>loading=11,437 %<br>P=-0,8..<br>Q=-0,1..<br>S=0,84..<br>I=0,02..<br>loadin..<br>Line00125<br>P=3,128 MW<br>Q=-0,329 Mvar<br>S=3,146 MVA<br>I=0,078 kA<br>loading=42,628 %<br>Trafo T2<br>P=0,251 MW<br>Q=1,064 Mvar<br>S=1,093 MVA<br>I=0,010 kA<br>loading=13,707 %<br>P=-0,239 MW<br>Q=-1,051 Mvar<br>S=1,077 MVA<br>I=0,027 kA<br>loading=13,707 %<br>Line01112<br>P=0,23..<br>Q=1,05..<br>S=1,07..<br>I=0,02..<br>loadin..<br>**DIgSILENT**|Pow erFactory 15.1.7|Pow erFactory 15.1.7|Pow erFactory 15.1.7|
|**_PP702966_**<br>**_PP702963_**<br>**_Punto Repercusión_**<br>**_Punto Conexión_**<br>~~**_A_**~~**_vellano 66[kV]_**<br>**_Avellano 23[kV]_**<br>**_S/E El Avellano_**<br>Avellano 66[kV..<br>Ul=65,..<br>u=0,99..<br>phiu=0..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/21/2015<br> Annex: ES<br>~~U~~l~~=65,774~~ ~~kV~~<br>u=0,997 p.u.<br>phiu=0,422 deg<br>~~ G~~r~~i~~d~~:~~ ~~Summar~~y~~ G~~r~~i~~d <br> <br> Generation = 7336,20 MW 756,26 Mvar 7375,07 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un-U) = -0,00 MW -0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 339,69 MW 336,31 Mvar<br> Line Charging = -2684,50 Mvar<br> Compensation ind. = 1111,61 Mvar<br> Compensation cap. = -2030,97 Mvar<br> Installed Capacity = 9680,22 MW<br> Spinning Reserve = 2344,02 MW<br> Total Power Factor:<br> Generation = 0,99 [-]<br> Load/Motor = 0,98 / 0,00 [-] <br>~~Ul=22~~,~~652 kV~~<br>u=0,985 p.u.<br>phiu=-29,698 deg<br>~~Ul=23~~,~~410~~ ~~kV~~<br>u=1,018 p.u.<br>phiu=-27,916 deg<br>~~U~~l~~=23,40~~9~~ kV~~<br>u=1,018 p.u.<br>phiu=-27,917 deg<br>Id_9048591<br>~~P=0~~,~~002~~ ~~MW~~<br>Q=0,000 Mvar<br>S=0,002 MVA<br>Line01019<br>~~P=0~~,~~10~~2~~ MW~~<br>Q=0,021 Mvar<br>S=0,105 MVA<br>I=0,003 kA<br>loading=2,079 %<br>Line01018<br>P=0,104 MW<br>Q=0,021 Mvar<br>S=0,106 MVA<br>I=0,003 kA<br>loading=2,113 %<br>P=-0,1..<br>Q=-0,0..<br>S=0,10..<br>I=0,00..<br>loadin..<br>Line00126<br>P=0,827 MW<br>Q=0,169 Mvar<br>S=0,844 MVA<br>I=0,021 kA<br>loading=11,437 %<br>P=-0,8..<br>Q=-0,1..<br>S=0,84..<br>I=0,02..<br>loadin..<br>Line00125<br>P=3,128 MW<br>Q=-0,329 Mvar<br>S=3,146 MVA<br>I=0,078 kA<br>loading=42,628 %<br>Trafo T2<br>P=0,251 MW<br>Q=1,064 Mvar<br>S=1,093 MVA<br>I=0,010 kA<br>loading=13,707 %<br>P=-0,239 MW<br>Q=-1,051 Mvar<br>S=1,077 MVA<br>I=0,027 kA<br>loading=13,707 %<br>Line01112<br>P=0,23..<br>Q=1,05..<br>S=1,07..<br>I=0,02..<br>loadin..<br>**DIgSILENT**|Pow erFactory 15.1.7|Pow erFactory 15.1.7|Annex: ES|

**Figura 9: Resumen Ejecutivo del PMGD HBS Energía.**

Observando el perfil de tensiones y el anexo con los porcentajes de carga de las líneas, se

concluye que no es necesario para este año realizar obras adicionales.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 28 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

#### 8.1.2 Escenario: FB1600

|DIgSILENT<br>1,0900<br>[p.u.]<br>1,0540<br>1,0180<br>0,9820<br>0,9460<br>0,9100<br>-0,0000 5,7814 11,563 17,344 23,126 [km] 28,907<br>Avell.. 525592 494227 469428 926574 204845 241785 494252 242000 494264 494272 494280 494287 494296 126354 703089 126371 470378 126387 126395 126403 282515 126421 126431 126439 126447 126455 239904 239910 204480 239928 239935 239941 239946 126516 126524 126532 126540 126548 126556 126564 126572 126580 126588 126596 126604 126612 126620 126628 126636 126644 282572 204839 126663 126671 126679 126687 126695 823103 468313 126719 610640 126735 126743 126751 126759 279293<br>El<br>S/E<br>Voltage, Magnitude Voltage, Magnitude<br>Voltage, Magnitude|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>PerfilTensión-Laja<br>CENTRAL HBS GNL<br>Realizó TECNORED - Ing. René Moraga Castillo<br><br>|Date: 9/21/2015<br> Annex: /1|

**Figura 10: Perfil de Tensión, Tensión Cabecera = 1,01[pu].**

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 29 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|DIgSILENT<br>S/E El Avellano<br>Ul=22,776 kV Grid: Summary Grid<br>u=0,990 p.u.<br>Generation = 5208,93 MW 56,62 Mvar 5209,23 MVA<br>Ul=66,489 kV phiu=-15,917 deg External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br>u=1,007 p.u. Inter Area Flow = 0,00 MW 0,00 Mvar<br>phiu=11,969 deg Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br>Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA rP = 3,3 5 1 M W<br>Load P(Un-U) = -0,00 MW 0,00 Mvar AQ = -0,3 9 4 M va<br>Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA Losses = 182,03 MW -1195,08 Mvar Line Charging = -2703,42 Mvar Compensation ind. = 1295,64 Mvar Avellano 23[kV] Compensation cap. = -1053,65 Mvar Installed Capacity = 7703,62 MW kAS = 3,3 73 M V AQ = 0,51 9 M varP = -3,33 3 M W lo a d in g = 4 2,5 9 1 %Trafo T2 I= 0,0 8 6 kAS = 3,3 7 4 M V I P QS l==== o- 003 a,, 3,, d033 i 3 8. 97 n... ..... . Line01112<br>Spinning Reserve = 2494,70 MW Total Power Factor: Generation = 1,00 [-] 66[kV.. lo adin g= 4 2,591 %I= 0,029<br>Load/Motor = 0,98 / 0,00 [-] 1u6,06 =,. 01.....<br>Avellano 66[kV] Avellano upUl =h= i<br>Punto Conexión Punto Repercusión<br>Id_9048591<br>Ul=24,189 kV u=1,052 p.u. Q=0,015 MW P=0,075 loadin.. I=0,00.. S=0,07.. Q=-0,0.. P=-0,0..<br>Ul=24,189 kV P=0,000 MW phiu=-13,014 deg 0,076 r = Sa Mv Line00126<br>u=1,052 p.u. Q=0,000 Mvar phiu=-13,014 deg S=0,000 MVA % ading=1,000 loA k I=0,002 MVA kAS = 0,0 1 0 M V AQ = 0,0 0 2 M va rP = 0,0 0 9 M W<br>PP702963 Line01019 P=0,009 MW Q=0,002 Mvar kAS = 3,8 8 6 M V AQ = -0,1 6 6 M va rP = 3,8 8 2 M W lo a d iL ni gne =0 0,10 11 88 6 %I= 0,0 0 0 Il SP Q =o=== 0- a0-,, 0 0d00, i, 00 n10 .. ..... ...<br>PP702966 S=0,009 MVA I=0,000 kA Line lo a d i0 n g = 50 0,9 61 2 %2 I=5 0,0 9 3<br>loading=0,183 %<br>ESTUDIO DE CONEXIÓN DE PMGD Project: 15034<br>CENTRAL HBS ENERGÍA Graphic: Resumen Ejecutiv<br>Propiedad de HBS energía - Tomaval Date: 9/22/2015<br>Pow erFactory 15.1.7 Realizó Ing. René Moraga Castillo Annex: ES|Col2|Col3|Col4|
|---|---|---|---|
|**_PP702966_**<br>**_PP702963_**<br>**_Punto Repercusión_**<br>**_Punto Conexión_**<br>~~**_A_**~~**_vellano 66[kV]_**<br>**_Avellano 23[kV]_**<br>**_S/E El Avellano_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~U~~l~~=66,489~~ ~~kV~~<br>u=1,007 p.u.<br>phiu=11,969 deg<br>~~ G~~r~~i~~d~~:~~ ~~Summar~~y~~ G~~r~~i~~d <br> <br> Generation = 5208,93 MW 56,62 Mvar 5209,23 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 182,03 MW -1195,08 Mvar<br> Line Charging = -2703,42 Mvar<br> Compensation ind. = 1295,64 Mvar<br> Compensation cap. = -1053,65 Mvar<br> Installed Capacity = 7703,62 MW<br> Spinning Reserve = 2494,70 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00 [-] <br>~~Ul=22~~,~~776 kV~~<br>u=0,990 p.u.<br>phiu=-15,917 deg<br>~~Ul=24~~,~~189~~ ~~kV~~<br>u=1,052 p.u.<br>phiu=-13,014 deg<br>~~U~~l~~=24,18~~9~~ kV~~<br>u=1,052 p.u.<br>phiu=-13,014 deg<br>Id_9048591<br>~~P=0~~,~~000~~ ~~MW~~<br>Q=0,000 Mvar<br>S=0,000 MVA<br>Line01019<br>~~P=0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>I=0,000 kA<br>loading=0,183 %<br>Line01018<br>P=0,009 MW<br>Q=0,002 Mvar<br>S=0,010 MVA<br>I=0,000 kA<br>loading=0,186 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,01..<br>I=0,00..<br>loadin..<br>Line00126<br>P=0,075 MW<br>Q=0,015 Mvar<br>S=0,076 MVA<br>I=0,002 kA<br>loading=1,000 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,07..<br>I=0,00..<br>loadin..<br>Line00125<br>P=3,882 MW<br>Q=-0,166 Mvar<br>S=3,886 MVA<br>I=0,093 kA<br>loading=50,962 %<br>Trafo T2<br>P=-3,333 MW<br>Q=0,519 Mvar<br>S=3,373 MVA<br>I=0,029 kA<br>loading=42,591 %<br>P=3,351 MW<br>Q=-0,394 Mvar<br>S=3,374 MVA<br>I=0,086 kA<br>loading=42,591 %<br>Line01112<br>P=-3,3..<br>Q=0,39..<br>S=3,37..<br>I=0,08..<br>loadin..<br>**DIgSILENT**||ESTUDIO DE CONEXIÓN DE PMGD<br>|Project: 15034|
|**_PP702966_**<br>**_PP702963_**<br>**_Punto Repercusión_**<br>**_Punto Conexión_**<br>~~**_A_**~~**_vellano 66[kV]_**<br>**_Avellano 23[kV]_**<br>**_S/E El Avellano_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~U~~l~~=66,489~~ ~~kV~~<br>u=1,007 p.u.<br>phiu=11,969 deg<br>~~ G~~r~~i~~d~~:~~ ~~Summar~~y~~ G~~r~~i~~d <br> <br> Generation = 5208,93 MW 56,62 Mvar 5209,23 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 182,03 MW -1195,08 Mvar<br> Line Charging = -2703,42 Mvar<br> Compensation ind. = 1295,64 Mvar<br> Compensation cap. = -1053,65 Mvar<br> Installed Capacity = 7703,62 MW<br> Spinning Reserve = 2494,70 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00 [-] <br>~~Ul=22~~,~~776 kV~~<br>u=0,990 p.u.<br>phiu=-15,917 deg<br>~~Ul=24~~,~~189~~ ~~kV~~<br>u=1,052 p.u.<br>phiu=-13,014 deg<br>~~U~~l~~=24,18~~9~~ kV~~<br>u=1,052 p.u.<br>phiu=-13,014 deg<br>Id_9048591<br>~~P=0~~,~~000~~ ~~MW~~<br>Q=0,000 Mvar<br>S=0,000 MVA<br>Line01019<br>~~P=0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>I=0,000 kA<br>loading=0,183 %<br>Line01018<br>P=0,009 MW<br>Q=0,002 Mvar<br>S=0,010 MVA<br>I=0,000 kA<br>loading=0,186 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,01..<br>I=0,00..<br>loadin..<br>Line00126<br>P=0,075 MW<br>Q=0,015 Mvar<br>S=0,076 MVA<br>I=0,002 kA<br>loading=1,000 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,07..<br>I=0,00..<br>loadin..<br>Line00125<br>P=3,882 MW<br>Q=-0,166 Mvar<br>S=3,886 MVA<br>I=0,093 kA<br>loading=50,962 %<br>Trafo T2<br>P=-3,333 MW<br>Q=0,519 Mvar<br>S=3,373 MVA<br>I=0,029 kA<br>loading=42,591 %<br>P=3,351 MW<br>Q=-0,394 Mvar<br>S=3,374 MVA<br>I=0,086 kA<br>loading=42,591 %<br>Line01112<br>P=-3,3..<br>Q=0,39..<br>S=3,37..<br>I=0,08..<br>loadin..<br>**DIgSILENT**||CENTRAL HBS ENERGÍA<br> Propiedad de HBS energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br><br><br>|Graphic: Resumen Ejecutiv|
|**_PP702966_**<br>**_PP702963_**<br>**_Punto Repercusión_**<br>**_Punto Conexión_**<br>~~**_A_**~~**_vellano 66[kV]_**<br>**_Avellano 23[kV]_**<br>**_S/E El Avellano_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~U~~l~~=66,489~~ ~~kV~~<br>u=1,007 p.u.<br>phiu=11,969 deg<br>~~ G~~r~~i~~d~~:~~ ~~Summar~~y~~ G~~r~~i~~d <br> <br> Generation = 5208,93 MW 56,62 Mvar 5209,23 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 182,03 MW -1195,08 Mvar<br> Line Charging = -2703,42 Mvar<br> Compensation ind. = 1295,64 Mvar<br> Compensation cap. = -1053,65 Mvar<br> Installed Capacity = 7703,62 MW<br> Spinning Reserve = 2494,70 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00 [-] <br>~~Ul=22~~,~~776 kV~~<br>u=0,990 p.u.<br>phiu=-15,917 deg<br>~~Ul=24~~,~~189~~ ~~kV~~<br>u=1,052 p.u.<br>phiu=-13,014 deg<br>~~U~~l~~=24,18~~9~~ kV~~<br>u=1,052 p.u.<br>phiu=-13,014 deg<br>Id_9048591<br>~~P=0~~,~~000~~ ~~MW~~<br>Q=0,000 Mvar<br>S=0,000 MVA<br>Line01019<br>~~P=0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>I=0,000 kA<br>loading=0,183 %<br>Line01018<br>P=0,009 MW<br>Q=0,002 Mvar<br>S=0,010 MVA<br>I=0,000 kA<br>loading=0,186 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,01..<br>I=0,00..<br>loadin..<br>Line00126<br>P=0,075 MW<br>Q=0,015 Mvar<br>S=0,076 MVA<br>I=0,002 kA<br>loading=1,000 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,07..<br>I=0,00..<br>loadin..<br>Line00125<br>P=3,882 MW<br>Q=-0,166 Mvar<br>S=3,886 MVA<br>I=0,093 kA<br>loading=50,962 %<br>Trafo T2<br>P=-3,333 MW<br>Q=0,519 Mvar<br>S=3,373 MVA<br>I=0,029 kA<br>loading=42,591 %<br>P=3,351 MW<br>Q=-0,394 Mvar<br>S=3,374 MVA<br>I=0,086 kA<br>loading=42,591 %<br>Line01112<br>P=-3,3..<br>Q=0,39..<br>S=3,37..<br>I=0,08..<br>loadin..<br>**DIgSILENT**||CENTRAL HBS ENERGÍA<br> Propiedad de HBS energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br><br><br>|Date: 9/22/2015|
|**_PP702966_**<br>**_PP702963_**<br>**_Punto Repercusión_**<br>**_Punto Conexión_**<br>~~**_A_**~~**_vellano 66[kV]_**<br>**_Avellano 23[kV]_**<br>**_S/E El Avellano_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~U~~l~~=66,489~~ ~~kV~~<br>u=1,007 p.u.<br>phiu=11,969 deg<br>~~ G~~r~~i~~d~~:~~ ~~Summar~~y~~ G~~r~~i~~d <br> <br> Generation = 5208,93 MW 56,62 Mvar 5209,23 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 182,03 MW -1195,08 Mvar<br> Line Charging = -2703,42 Mvar<br> Compensation ind. = 1295,64 Mvar<br> Compensation cap. = -1053,65 Mvar<br> Installed Capacity = 7703,62 MW<br> Spinning Reserve = 2494,70 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00 [-] <br>~~Ul=22~~,~~776 kV~~<br>u=0,990 p.u.<br>phiu=-15,917 deg<br>~~Ul=24~~,~~189~~ ~~kV~~<br>u=1,052 p.u.<br>phiu=-13,014 deg<br>~~U~~l~~=24,18~~9~~ kV~~<br>u=1,052 p.u.<br>phiu=-13,014 deg<br>Id_9048591<br>~~P=0~~,~~000~~ ~~MW~~<br>Q=0,000 Mvar<br>S=0,000 MVA<br>Line01019<br>~~P=0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>I=0,000 kA<br>loading=0,183 %<br>Line01018<br>P=0,009 MW<br>Q=0,002 Mvar<br>S=0,010 MVA<br>I=0,000 kA<br>loading=0,186 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,01..<br>I=0,00..<br>loadin..<br>Line00126<br>P=0,075 MW<br>Q=0,015 Mvar<br>S=0,076 MVA<br>I=0,002 kA<br>loading=1,000 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,07..<br>I=0,00..<br>loadin..<br>Line00125<br>P=3,882 MW<br>Q=-0,166 Mvar<br>S=3,886 MVA<br>I=0,093 kA<br>loading=50,962 %<br>Trafo T2<br>P=-3,333 MW<br>Q=0,519 Mvar<br>S=3,373 MVA<br>I=0,029 kA<br>loading=42,591 %<br>P=3,351 MW<br>Q=-0,394 Mvar<br>S=3,374 MVA<br>I=0,086 kA<br>loading=42,591 %<br>Line01112<br>P=-3,3..<br>Q=0,39..<br>S=3,37..<br>I=0,08..<br>loadin..<br>**DIgSILENT**|Pow erFactory 15.1.7|Pow erFactory 15.1.7|Pow erFactory 15.1.7|
|**_PP702966_**<br>**_PP702963_**<br>**_Punto Repercusión_**<br>**_Punto Conexión_**<br>~~**_A_**~~**_vellano 66[kV]_**<br>**_Avellano 23[kV]_**<br>**_S/E El Avellano_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~U~~l~~=66,489~~ ~~kV~~<br>u=1,007 p.u.<br>phiu=11,969 deg<br>~~ G~~r~~i~~d~~:~~ ~~Summar~~y~~ G~~r~~i~~d <br> <br> Generation = 5208,93 MW 56,62 Mvar 5209,23 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 182,03 MW -1195,08 Mvar<br> Line Charging = -2703,42 Mvar<br> Compensation ind. = 1295,64 Mvar<br> Compensation cap. = -1053,65 Mvar<br> Installed Capacity = 7703,62 MW<br> Spinning Reserve = 2494,70 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00 [-] <br>~~Ul=22~~,~~776 kV~~<br>u=0,990 p.u.<br>phiu=-15,917 deg<br>~~Ul=24~~,~~189~~ ~~kV~~<br>u=1,052 p.u.<br>phiu=-13,014 deg<br>~~U~~l~~=24,18~~9~~ kV~~<br>u=1,052 p.u.<br>phiu=-13,014 deg<br>Id_9048591<br>~~P=0~~,~~000~~ ~~MW~~<br>Q=0,000 Mvar<br>S=0,000 MVA<br>Line01019<br>~~P=0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>I=0,000 kA<br>loading=0,183 %<br>Line01018<br>P=0,009 MW<br>Q=0,002 Mvar<br>S=0,010 MVA<br>I=0,000 kA<br>loading=0,186 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,01..<br>I=0,00..<br>loadin..<br>Line00126<br>P=0,075 MW<br>Q=0,015 Mvar<br>S=0,076 MVA<br>I=0,002 kA<br>loading=1,000 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,07..<br>I=0,00..<br>loadin..<br>Line00125<br>P=3,882 MW<br>Q=-0,166 Mvar<br>S=3,886 MVA<br>I=0,093 kA<br>loading=50,962 %<br>Trafo T2<br>P=-3,333 MW<br>Q=0,519 Mvar<br>S=3,373 MVA<br>I=0,029 kA<br>loading=42,591 %<br>P=3,351 MW<br>Q=-0,394 Mvar<br>S=3,374 MVA<br>I=0,086 kA<br>loading=42,591 %<br>Line01112<br>P=-3,3..<br>Q=0,39..<br>S=3,37..<br>I=0,08..<br>loadin..<br>**DIgSILENT**|Pow erFactory 15.1.7|Pow erFactory 15.1.7|Annex: ES|

**Figura 11: Resumen Ejecutivo del PMGD HBS Energía.**

Observando el perfil de tensiones y el anexo con los porcentajes de carga de las líneas, se

concluye que no es necesario para este año realizar obras adicionales.

#### 8.1.3 Resumen Resultados Flujos de Potencia Sin PMGD HBS GNL

En esta sección se presenta el resumen de los resultados de los escenarios, considerando

la inyección del total de la potencia del PMGD existente en el alimentador considerando

un factor de potencia igual a la unidad, observando el comportamiento de los niveles de

tensión, el porcentaje de carga de elementos serie y el transformador de poder.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 30 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

**Tabla 21: Tensiones en Puntos de Interés.**

**Escenario** **Barra** **Tensión[pu]** **Mín. de FP[-]**

FA-16-00

FB-16-00

126609 1,017 0,99

126610 1,017 0,99

821739 1,017 0,98

Avellano 23[kV] 0,985 0,97

Avellano 66[kV] 0,997 0,97

126609 1,05 1,00

126610 1,051 1,00

821739 1,05 0,98

Avellano 23[kV] 0,99 1,00

Avellano 66[kV] 1,007 1,00

Como se aprecia en la Tabla 21, los niveles de tensión en el año 2016 considerando la

inyección de los 4[MW] del PMGD existente, se encuentran dentro de los niveles

establecidos por la normativa vigente, por lo que no se identifican requerimientos de

obras adicionales.

**Tabla 22: Máximos Porcentajes de Carga en Tramos de Línea.**

**Escenario** **Máx. de Carga[%]** **Máx. de P[MW]** **Máx. de Q[MVAr]**

FA-16-00 62,567 3,128 1,051

FB-16-00 74,8 3,882 0,026

En la Tabla 22 se aprecian que no existen problemas de sobrecarga en el alimentador,

por lo que no se identifican requerimientos de refuerzos de tramos de líneas.

**Tabla 23: Máximos Porcentajes de Carga en Transformador.**

**Escenario** **Equipo** **Snom[MW]** **S[MVA]** **Carga[%]**

FA-16-00 Trafo T2 10 1,093 10,93

FB-16-00 Trafo T2 10 3,373 33,73

Los porcentajes de carga del transformador de poder, se encuentran dentro de los

niveles aceptables.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 31 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

### 8.2 Resultados Flujos de Potencia Con PMGD HBS GNL

En esta sección se reitera la proyección de las demandas pero incorporando el PMGD

HBS GNL 6,75[MW], esto para analizar el comportamiento estático de la red y buscar

identificar si existe una fecha en que debería ser reforzado o compensado el alimentador

debido a la entrada en servicio del PMGD, con el fin de cumplir con lo establecido en la

NTCO.

#### 8.2.1 Escenario: FA1611

|DIgSILENT<br>1,0900<br>[p.u.]<br>1,0540<br>1,0180<br>0,9820<br>0,9460<br>0,9100<br>0,0000 5,3836 10,767 16,151 21,534 [km] 26,918<br>Avell.. 525652 494225 534561 494231 494236 904182 241782 241777 470463 494265 163460 494280 494287 494295 560215 126359 126367 470376 469942 126391 126399 282511 282519 470320 743501 758709 282521 126458 239906 204476 239920 282657 282665 239941 126508 239951 126523 126531 126539 126547 126555 126563 126571 126579 126587 126595 126603 126611 126619 126627 126635 126643 282570 204838 126662 126670 126678 126686 814309 126701 468342 126716 629208 126731 126739 126747 1000271575 126762 279296<br>El<br>S/E<br>Voltage, Magnitude|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Voltage Profile-Laja<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/21/2015<br> Annex: /1|

**Figura 12: Perfil de Tensión, Tensión Cabecera = 0,98[pu].**

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 32 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|DIgSILENT<br>Grid: Summary Grid<br>S/E El Avellano Ul=22,489 kV<br>Generation = 7336,70 MW 750,81 Mvar 7375,02 MVA<br>u=0,978 p.u.<br>Ul=65,968 kV External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br>phiu=-24,748 deg Inter Area Flow = 0,00 MW 0,00 Mvar<br>u=1,000 p.u.<br>Load P(U) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br>phiu=1,799 deg Load P(Un) = 6996,51 MW 1339,32 Mvar 7123,55 MVA rP = 5,3 5 9 M W<br>Load P(Un-U) = -0,00 MW -0,00 Mvar AQ = -2,0 6 5 M va<br>Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA MW P=-5,328 T ra fo T 2 kAS = 5,7 4 3 M V<br>Losses = 340,19 MW 330,72 Mvar Line Charging = -2684,89 Mvar Compensation ind. = 1111,90 Mvar kA I=0,051 MVA S=5,859 Mvar Q=2,437 lo a d in g = 7 3,4 1 4 %I= 0,1 4 7 P Q I S l== == o-250a, 5,,, d071i 3. 644n.. . ...... Line01112<br>Avellano 23[kV] Compensation cap. = -2031,13 Mvar % loading=73,414<br>Installed Capacity = 9686,61 MW 66[kV..<br>Spinning Reserve = 2349,91 MW 1u6,05 =,. 01.....<br>Total Power Factor: Avellano upUl =h= i<br>Avellano 66[kV] Generation = 0,99 [-]<br>Load/Motor = 0,98 / 0,00 [-]<br>Punto de Conexión Punto de Repercusión<br>Ul=25,368 kV MW P=-3,131<br>u=1,103 p.u. Mvar Q=0,308<br>MVA S=3,146<br>phiu=-18,222 deg kA I=0,072 Line00010<br>% loading=57,706<br>P=0,102 MW<br>Q=0,021 Mvar P=0,102 MW PP126609 S=0,105 MVALine01051 Q=0,021 Mvar PP126610 Ul=25,4 kV I=0,002 kA S=0,105 MVA Il SQP =o === 0- 0 a-,, 0 00 d1, i, 01 00 n.. .. ... .. . Id_8145455<br>u=1,10 p.u. loading=1,918 %<br>phiu=-18,2 deg<br>P=9,815<br>MW<br>Q=-0,641<br>loading=180,392 kA 4 L 22 i I=0, ne VA 0 M 835 0 S=9, 0 r 9 Mva 0<br>%<br>ESTUDIO DE CONEXIÓN DE PMGD Project: 15034<br>CENTRAL HBS ENERGÍA Graphic: Resumen Ejecutiv<br>Propiedad de HBS Energía - Tomaval Date: 9/22/2015<br>Pow erFactory 15.1.7 Realizó Ing. René Moraga Castillo Annex: ES|Col2|Col3|Col4|
|---|---|---|---|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=65,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~Ul=25~~,~~4 kV~~<br>u=1,10 p.u.<br>phiu=-18,2 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 7336,70 MW 750,81 Mvar 7375,02 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un-U) = -0,00 MW -0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 340,19 MW 330,72 Mvar<br> Line Charging = -2684,89 Mvar<br> Compensation ind. = 1111,90 Mvar<br> Compensation cap. = -2031,13 Mvar<br> Installed Capacity = 9686,61 MW<br> Spinning Reserve = 2349,91 MW<br> Total Power Factor:<br> Generation = 0,99 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=65~~,~~968~~ ~~kV~~<br>u=1,000 p.u.<br>phiu=1,799 deg<br>~~U~~l~~=22,48~~9~~ kV~~<br>u=0,978 p.u.<br>phiu=-24,748 deg<br>~~U~~l~~=25,~~3~~68 kV~~<br>u=1,103 p.u.<br>phiu=-18,222 deg<br>Line01051<br>~~P~~=~~0~~,~~10~~2~~ MW~~<br>Q=0,021 Mvar<br>S=0,105 MV~~A~~<br>I=0,002 kA<br>loading=1,918 %<br>P=-0,1..<br>Q=-0,0..<br>S=0,10..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-5,328 MW<br>Q=2,437 Mvar<br>S=5,859 MVA<br>I=0,051 kA<br>loading=73,414 %<br>P=5,359 MW<br>Q=-2,065 Mvar<br>S=5,743 MVA<br>I=0,147 kA<br>loading=73,414 %<br>Line01112<br>P=-5,3..<br>Q=2,06..<br>S=5,74..<br>I=0,14..<br>loadin..<br>Line00090<br>P=9,815 MW<br>Q=-0,641 Mvar<br>S=9,835 MVA<br>I=0,224 kA<br>loading=180,392 %<br>Line00010<br>P=-3,131 MW<br>Q=0,308 Mvar<br>S=3,146 MVA<br>I=0,072 kA<br>loading=57,706 %<br>Id_8145455<br>~~P=~~0~~,~~1~~02~~ ~~MW~~<br>Q=0,021 Mvar<br>S=0,105 MVA<br>**DIgSILENT**||ESTUDIO DE CONEXIÓN DE PMGD<br>|Project: 15034|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=65,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~Ul=25~~,~~4 kV~~<br>u=1,10 p.u.<br>phiu=-18,2 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 7336,70 MW 750,81 Mvar 7375,02 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un-U) = -0,00 MW -0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 340,19 MW 330,72 Mvar<br> Line Charging = -2684,89 Mvar<br> Compensation ind. = 1111,90 Mvar<br> Compensation cap. = -2031,13 Mvar<br> Installed Capacity = 9686,61 MW<br> Spinning Reserve = 2349,91 MW<br> Total Power Factor:<br> Generation = 0,99 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=65~~,~~968~~ ~~kV~~<br>u=1,000 p.u.<br>phiu=1,799 deg<br>~~U~~l~~=22,48~~9~~ kV~~<br>u=0,978 p.u.<br>phiu=-24,748 deg<br>~~U~~l~~=25,~~3~~68 kV~~<br>u=1,103 p.u.<br>phiu=-18,222 deg<br>Line01051<br>~~P~~=~~0~~,~~10~~2~~ MW~~<br>Q=0,021 Mvar<br>S=0,105 MV~~A~~<br>I=0,002 kA<br>loading=1,918 %<br>P=-0,1..<br>Q=-0,0..<br>S=0,10..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-5,328 MW<br>Q=2,437 Mvar<br>S=5,859 MVA<br>I=0,051 kA<br>loading=73,414 %<br>P=5,359 MW<br>Q=-2,065 Mvar<br>S=5,743 MVA<br>I=0,147 kA<br>loading=73,414 %<br>Line01112<br>P=-5,3..<br>Q=2,06..<br>S=5,74..<br>I=0,14..<br>loadin..<br>Line00090<br>P=9,815 MW<br>Q=-0,641 Mvar<br>S=9,835 MVA<br>I=0,224 kA<br>loading=180,392 %<br>Line00010<br>P=-3,131 MW<br>Q=0,308 Mvar<br>S=3,146 MVA<br>I=0,072 kA<br>loading=57,706 %<br>Id_8145455<br>~~P=~~0~~,~~1~~02~~ ~~MW~~<br>Q=0,021 Mvar<br>S=0,105 MVA<br>**DIgSILENT**||CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br><br><br>|Graphic: Resumen Ejecutiv|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=65,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~Ul=25~~,~~4 kV~~<br>u=1,10 p.u.<br>phiu=-18,2 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 7336,70 MW 750,81 Mvar 7375,02 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un-U) = -0,00 MW -0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 340,19 MW 330,72 Mvar<br> Line Charging = -2684,89 Mvar<br> Compensation ind. = 1111,90 Mvar<br> Compensation cap. = -2031,13 Mvar<br> Installed Capacity = 9686,61 MW<br> Spinning Reserve = 2349,91 MW<br> Total Power Factor:<br> Generation = 0,99 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=65~~,~~968~~ ~~kV~~<br>u=1,000 p.u.<br>phiu=1,799 deg<br>~~U~~l~~=22,48~~9~~ kV~~<br>u=0,978 p.u.<br>phiu=-24,748 deg<br>~~U~~l~~=25,~~3~~68 kV~~<br>u=1,103 p.u.<br>phiu=-18,222 deg<br>Line01051<br>~~P~~=~~0~~,~~10~~2~~ MW~~<br>Q=0,021 Mvar<br>S=0,105 MV~~A~~<br>I=0,002 kA<br>loading=1,918 %<br>P=-0,1..<br>Q=-0,0..<br>S=0,10..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-5,328 MW<br>Q=2,437 Mvar<br>S=5,859 MVA<br>I=0,051 kA<br>loading=73,414 %<br>P=5,359 MW<br>Q=-2,065 Mvar<br>S=5,743 MVA<br>I=0,147 kA<br>loading=73,414 %<br>Line01112<br>P=-5,3..<br>Q=2,06..<br>S=5,74..<br>I=0,14..<br>loadin..<br>Line00090<br>P=9,815 MW<br>Q=-0,641 Mvar<br>S=9,835 MVA<br>I=0,224 kA<br>loading=180,392 %<br>Line00010<br>P=-3,131 MW<br>Q=0,308 Mvar<br>S=3,146 MVA<br>I=0,072 kA<br>loading=57,706 %<br>Id_8145455<br>~~P=~~0~~,~~1~~02~~ ~~MW~~<br>Q=0,021 Mvar<br>S=0,105 MVA<br>**DIgSILENT**||CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br><br><br>|Date: 9/22/2015|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=65,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~Ul=25~~,~~4 kV~~<br>u=1,10 p.u.<br>phiu=-18,2 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 7336,70 MW 750,81 Mvar 7375,02 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un-U) = -0,00 MW -0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 340,19 MW 330,72 Mvar<br> Line Charging = -2684,89 Mvar<br> Compensation ind. = 1111,90 Mvar<br> Compensation cap. = -2031,13 Mvar<br> Installed Capacity = 9686,61 MW<br> Spinning Reserve = 2349,91 MW<br> Total Power Factor:<br> Generation = 0,99 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=65~~,~~968~~ ~~kV~~<br>u=1,000 p.u.<br>phiu=1,799 deg<br>~~U~~l~~=22,48~~9~~ kV~~<br>u=0,978 p.u.<br>phiu=-24,748 deg<br>~~U~~l~~=25,~~3~~68 kV~~<br>u=1,103 p.u.<br>phiu=-18,222 deg<br>Line01051<br>~~P~~=~~0~~,~~10~~2~~ MW~~<br>Q=0,021 Mvar<br>S=0,105 MV~~A~~<br>I=0,002 kA<br>loading=1,918 %<br>P=-0,1..<br>Q=-0,0..<br>S=0,10..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-5,328 MW<br>Q=2,437 Mvar<br>S=5,859 MVA<br>I=0,051 kA<br>loading=73,414 %<br>P=5,359 MW<br>Q=-2,065 Mvar<br>S=5,743 MVA<br>I=0,147 kA<br>loading=73,414 %<br>Line01112<br>P=-5,3..<br>Q=2,06..<br>S=5,74..<br>I=0,14..<br>loadin..<br>Line00090<br>P=9,815 MW<br>Q=-0,641 Mvar<br>S=9,835 MVA<br>I=0,224 kA<br>loading=180,392 %<br>Line00010<br>P=-3,131 MW<br>Q=0,308 Mvar<br>S=3,146 MVA<br>I=0,072 kA<br>loading=57,706 %<br>Id_8145455<br>~~P=~~0~~,~~1~~02~~ ~~MW~~<br>Q=0,021 Mvar<br>S=0,105 MVA<br>**DIgSILENT**|Pow erFactory 15.1.7|Pow erFactory 15.1.7|Pow erFactory 15.1.7|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=65,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~Ul=25~~,~~4 kV~~<br>u=1,10 p.u.<br>phiu=-18,2 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 7336,70 MW 750,81 Mvar 7375,02 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un) = 6996,51 MW 1339,32 Mvar 7123,55 MVA<br> Load P(Un-U) = -0,00 MW -0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 340,19 MW 330,72 Mvar<br> Line Charging = -2684,89 Mvar<br> Compensation ind. = 1111,90 Mvar<br> Compensation cap. = -2031,13 Mvar<br> Installed Capacity = 9686,61 MW<br> Spinning Reserve = 2349,91 MW<br> Total Power Factor:<br> Generation = 0,99 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=65~~,~~968~~ ~~kV~~<br>u=1,000 p.u.<br>phiu=1,799 deg<br>~~U~~l~~=22,48~~9~~ kV~~<br>u=0,978 p.u.<br>phiu=-24,748 deg<br>~~U~~l~~=25,~~3~~68 kV~~<br>u=1,103 p.u.<br>phiu=-18,222 deg<br>Line01051<br>~~P~~=~~0~~,~~10~~2~~ MW~~<br>Q=0,021 Mvar<br>S=0,105 MV~~A~~<br>I=0,002 kA<br>loading=1,918 %<br>P=-0,1..<br>Q=-0,0..<br>S=0,10..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-5,328 MW<br>Q=2,437 Mvar<br>S=5,859 MVA<br>I=0,051 kA<br>loading=73,414 %<br>P=5,359 MW<br>Q=-2,065 Mvar<br>S=5,743 MVA<br>I=0,147 kA<br>loading=73,414 %<br>Line01112<br>P=-5,3..<br>Q=2,06..<br>S=5,74..<br>I=0,14..<br>loadin..<br>Line00090<br>P=9,815 MW<br>Q=-0,641 Mvar<br>S=9,835 MVA<br>I=0,224 kA<br>loading=180,392 %<br>Line00010<br>P=-3,131 MW<br>Q=0,308 Mvar<br>S=3,146 MVA<br>I=0,072 kA<br>loading=57,706 %<br>Id_8145455<br>~~P=~~0~~,~~1~~02~~ ~~MW~~<br>Q=0,021 Mvar<br>S=0,105 MVA<br>**DIgSILENT**|Pow erFactory 15.1.7|Pow erFactory 15.1.7|Annex: ES|

**Figura 13: Resumen Ejecutivo del PMGD HBS GNL.**

Observando el perfil de tensiones, se aprecia claramente que existen sobretensiones

producto de limitaciones de transmisión existentes, en el anexo correspondiente es

posible identificar los elementos serie con sobrecargas hasta un 180%.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 33 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

#### 8.2.2 Escenario: FB1611

|DIgSILENT<br>1,0900<br>[p.u.]<br>1,0540<br>1,0180<br>0,9820<br>0,9460<br>0,9100<br>0,0000 5,3836 10,767 16,151 21,534 [km] 26,918<br>Avell.. 525652 494225 534561 494231 494236 904182 241782 241777 470463 494265 163460 494280 494287 494295 560215 126359 126367 470376 469942 126391 126399 282511 282519 470320 743501 758709 282521 126458 239906 204476 239920 282657 282665 239941 126508 239951 126523 126531 126539 126547 126555 126563 126571 126579 126587 126595 126603 126611 126619 126627 126635 126643 282570 204838 126662 126670 126678 126686 814309 126701 468342 126716 629208 126731 126739 126747 1000271575 126762 279296<br>El<br>S/E<br>Voltage, Magnitude|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Voltage Profile-Laja<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/21/2015<br> Annex: /1|

**Figura 14: Perfil de Tensión, Tensión Cabecera = 1[pu].**

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 34 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|DIgSILENT<br>Grid: Summary Grid<br>S/E El Avellano Ul=22,741 kV<br>Generation = 5210,00 MW 55,23 Mvar 5210,29 MVA<br>u=0,989 p.u.<br>Ul=66,420 kV External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br>phiu=-11,245 deg Inter Area Flow = 0,00 MW 0,00 Mvar<br>u=1,006 p.u.<br>Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br>phiu=13,256 deg Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA rP = 8,7 6 4 M W<br>Load P(Un-U) = -0,00 MW 0,00 Mvar AQ = -1,6 2 1 M va<br>Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA MW P=-8,709 T ra fo T 2 kAS = 8,9 1 3 M V<br>Losses = 183,10 MW -1196,55 Mvar Line Charging = -2703,49 Mvar Compensation ind. = 1295,72 Mvar kA I=0,079 MVA S=9,060 Mvar Q=2,497 lo a d in g = 1 1 2,6 8 3 %I= 0,2 2 6 P Q I S l== == o-180a, 8,,, d692i 7. 212n.. . ...... Line01112<br>Avellano 23[kV] Compensation cap. = -1053,64 Mvar % loading=112,683<br>Installed Capacity = 7710,02 MW 66[kV..<br>Spinning Reserve = 2500,02 MW 1u6,06 =,. 01.....<br>Total Power Factor: Avellano upUl =h= i<br>Avellano 66[kV] Generation = 1,00 [-]<br>Load/Motor = 0,98 / 0,00 [-]<br>Punto de Conexión Punto de Repercusión<br>Ul=26,160 kV MW P=-3,883<br>u=1,137 p.u. Mvar Q=0,148<br>MVA S=3,886<br>phiu=-3,878 deg kA I=0,086 Line00010<br>% loading=69,113<br>P=0,009 MW<br>Q=0,002 Mvar P=0,009 MW PP126609 S=0,009 MVALine01051 Q=0,002 Mvar PP126610 Ul=26,2 kV I=0,000 kA S=0,009 MVA Il SQP =o === 0- 0 a-,, 0 00 d0, i, 00 00 n.. .. ... .. . Id_8145455<br>u=1,14 p.u. loading=0,169 %<br>phiu=-3,9 deg<br>P=10,569<br>MW<br>Q=-0,463<br>loading=188,157 kA 3 L 23 i I=0, ne MVA 0,579 0 S=10 0 r 9 Mva 0<br>%<br>ESTUDIO DE CONEXIÓN DE PMGD Project: 15034<br>CENTRAL HBS ENERGÍA Graphic: Resumen Ejecutiv<br>Propiedad de HBS Energía - Tomaval Date: 9/22/2015<br>Pow erFactory 15.1.7 Realizó Ing. René Moraga Castillo Annex: ES|Col2|Col3|Col4|
|---|---|---|---|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~Ul=26~~,~~2 kV~~<br>u=1,14 p.u.<br>phiu=-3,9 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 5210,00 MW 55,23 Mvar 5210,29 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 183,10 MW -1196,55 Mvar<br> Line Charging = -2703,49 Mvar<br> Compensation ind. = 1295,72 Mvar<br> Compensation cap. = -1053,64 Mvar<br> Installed Capacity = 7710,02 MW<br> Spinning Reserve = 2500,02 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=66~~,~~420~~ ~~kV~~<br>u=1,006 p.u.<br>phiu=13,256 deg<br>~~U~~l~~=22,74~~1~~ kV~~<br>u=0,989 p.u.<br>phiu=-11,245 deg<br>~~U~~l~~=26,~~1~~60 kV~~<br>u=1,137 p.u.<br>phiu=-3,878 deg<br>Line01051<br>~~P~~=~~0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MV~~A~~<br>I=0,000 kA<br>loading=0,169 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,00..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-8,709 MW<br>Q=2,497 Mvar<br>S=9,060 MVA<br>I=0,079 kA<br>loading=112,683 %<br>P=8,764 MW<br>Q=-1,621 Mvar<br>S=8,913 MVA<br>I=0,226 kA<br>loading=112,683 %<br>Line01112<br>P=-8,7..<br>Q=1,62..<br>S=8,91..<br>I=0,22..<br>loadin..<br>Line00090<br>P=10,569 MW<br>Q=-0,463 Mvar<br>S=10,579 MVA<br>I=0,233 kA<br>loading=188,157 %<br>Line00010<br>P=-3,883 MW<br>Q=0,148 Mvar<br>S=3,886 MVA<br>I=0,086 kA<br>loading=69,113 %<br>Id_8145455<br>~~P=~~0~~,~~0~~09~~ ~~MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>**DIgSILENT**||ESTUDIO DE CONEXIÓN DE PMGD<br>|Project: 15034|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~Ul=26~~,~~2 kV~~<br>u=1,14 p.u.<br>phiu=-3,9 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 5210,00 MW 55,23 Mvar 5210,29 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 183,10 MW -1196,55 Mvar<br> Line Charging = -2703,49 Mvar<br> Compensation ind. = 1295,72 Mvar<br> Compensation cap. = -1053,64 Mvar<br> Installed Capacity = 7710,02 MW<br> Spinning Reserve = 2500,02 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=66~~,~~420~~ ~~kV~~<br>u=1,006 p.u.<br>phiu=13,256 deg<br>~~U~~l~~=22,74~~1~~ kV~~<br>u=0,989 p.u.<br>phiu=-11,245 deg<br>~~U~~l~~=26,~~1~~60 kV~~<br>u=1,137 p.u.<br>phiu=-3,878 deg<br>Line01051<br>~~P~~=~~0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MV~~A~~<br>I=0,000 kA<br>loading=0,169 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,00..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-8,709 MW<br>Q=2,497 Mvar<br>S=9,060 MVA<br>I=0,079 kA<br>loading=112,683 %<br>P=8,764 MW<br>Q=-1,621 Mvar<br>S=8,913 MVA<br>I=0,226 kA<br>loading=112,683 %<br>Line01112<br>P=-8,7..<br>Q=1,62..<br>S=8,91..<br>I=0,22..<br>loadin..<br>Line00090<br>P=10,569 MW<br>Q=-0,463 Mvar<br>S=10,579 MVA<br>I=0,233 kA<br>loading=188,157 %<br>Line00010<br>P=-3,883 MW<br>Q=0,148 Mvar<br>S=3,886 MVA<br>I=0,086 kA<br>loading=69,113 %<br>Id_8145455<br>~~P=~~0~~,~~0~~09~~ ~~MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>**DIgSILENT**||CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br><br><br>|Graphic: Resumen Ejecutiv|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~Ul=26~~,~~2 kV~~<br>u=1,14 p.u.<br>phiu=-3,9 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 5210,00 MW 55,23 Mvar 5210,29 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 183,10 MW -1196,55 Mvar<br> Line Charging = -2703,49 Mvar<br> Compensation ind. = 1295,72 Mvar<br> Compensation cap. = -1053,64 Mvar<br> Installed Capacity = 7710,02 MW<br> Spinning Reserve = 2500,02 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=66~~,~~420~~ ~~kV~~<br>u=1,006 p.u.<br>phiu=13,256 deg<br>~~U~~l~~=22,74~~1~~ kV~~<br>u=0,989 p.u.<br>phiu=-11,245 deg<br>~~U~~l~~=26,~~1~~60 kV~~<br>u=1,137 p.u.<br>phiu=-3,878 deg<br>Line01051<br>~~P~~=~~0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MV~~A~~<br>I=0,000 kA<br>loading=0,169 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,00..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-8,709 MW<br>Q=2,497 Mvar<br>S=9,060 MVA<br>I=0,079 kA<br>loading=112,683 %<br>P=8,764 MW<br>Q=-1,621 Mvar<br>S=8,913 MVA<br>I=0,226 kA<br>loading=112,683 %<br>Line01112<br>P=-8,7..<br>Q=1,62..<br>S=8,91..<br>I=0,22..<br>loadin..<br>Line00090<br>P=10,569 MW<br>Q=-0,463 Mvar<br>S=10,579 MVA<br>I=0,233 kA<br>loading=188,157 %<br>Line00010<br>P=-3,883 MW<br>Q=0,148 Mvar<br>S=3,886 MVA<br>I=0,086 kA<br>loading=69,113 %<br>Id_8145455<br>~~P=~~0~~,~~0~~09~~ ~~MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>**DIgSILENT**||CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br><br><br>|Date: 9/22/2015|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~Ul=26~~,~~2 kV~~<br>u=1,14 p.u.<br>phiu=-3,9 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 5210,00 MW 55,23 Mvar 5210,29 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 183,10 MW -1196,55 Mvar<br> Line Charging = -2703,49 Mvar<br> Compensation ind. = 1295,72 Mvar<br> Compensation cap. = -1053,64 Mvar<br> Installed Capacity = 7710,02 MW<br> Spinning Reserve = 2500,02 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=66~~,~~420~~ ~~kV~~<br>u=1,006 p.u.<br>phiu=13,256 deg<br>~~U~~l~~=22,74~~1~~ kV~~<br>u=0,989 p.u.<br>phiu=-11,245 deg<br>~~U~~l~~=26,~~1~~60 kV~~<br>u=1,137 p.u.<br>phiu=-3,878 deg<br>Line01051<br>~~P~~=~~0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MV~~A~~<br>I=0,000 kA<br>loading=0,169 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,00..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-8,709 MW<br>Q=2,497 Mvar<br>S=9,060 MVA<br>I=0,079 kA<br>loading=112,683 %<br>P=8,764 MW<br>Q=-1,621 Mvar<br>S=8,913 MVA<br>I=0,226 kA<br>loading=112,683 %<br>Line01112<br>P=-8,7..<br>Q=1,62..<br>S=8,91..<br>I=0,22..<br>loadin..<br>Line00090<br>P=10,569 MW<br>Q=-0,463 Mvar<br>S=10,579 MVA<br>I=0,233 kA<br>loading=188,157 %<br>Line00010<br>P=-3,883 MW<br>Q=0,148 Mvar<br>S=3,886 MVA<br>I=0,086 kA<br>loading=69,113 %<br>Id_8145455<br>~~P=~~0~~,~~0~~09~~ ~~MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>**DIgSILENT**|Pow erFactory 15.1.7|Pow erFactory 15.1.7|Pow erFactory 15.1.7|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS ENERGÍA<br> Propiedad de HBS Energía - Tomaval<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/22/2015<br> Annex: ES<br>~~Ul=26~~,~~2 kV~~<br>u=1,14 p.u.<br>phiu=-3,9 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 5210,00 MW 55,23 Mvar 5210,29 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 183,10 MW -1196,55 Mvar<br> Line Charging = -2703,49 Mvar<br> Compensation ind. = 1295,72 Mvar<br> Compensation cap. = -1053,64 Mvar<br> Installed Capacity = 7710,02 MW<br> Spinning Reserve = 2500,02 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=66~~,~~420~~ ~~kV~~<br>u=1,006 p.u.<br>phiu=13,256 deg<br>~~U~~l~~=22,74~~1~~ kV~~<br>u=0,989 p.u.<br>phiu=-11,245 deg<br>~~U~~l~~=26,~~1~~60 kV~~<br>u=1,137 p.u.<br>phiu=-3,878 deg<br>Line01051<br>~~P~~=~~0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MV~~A~~<br>I=0,000 kA<br>loading=0,169 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,00..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-8,709 MW<br>Q=2,497 Mvar<br>S=9,060 MVA<br>I=0,079 kA<br>loading=112,683 %<br>P=8,764 MW<br>Q=-1,621 Mvar<br>S=8,913 MVA<br>I=0,226 kA<br>loading=112,683 %<br>Line01112<br>P=-8,7..<br>Q=1,62..<br>S=8,91..<br>I=0,22..<br>loadin..<br>Line00090<br>P=10,569 MW<br>Q=-0,463 Mvar<br>S=10,579 MVA<br>I=0,233 kA<br>loading=188,157 %<br>Line00010<br>P=-3,883 MW<br>Q=0,148 Mvar<br>S=3,886 MVA<br>I=0,086 kA<br>loading=69,113 %<br>Id_8145455<br>~~P=~~0~~,~~0~~09~~ ~~MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>**DIgSILENT**|Pow erFactory 15.1.7|Pow erFactory 15.1.7|Annex: ES|

**Figura 15: Resumen Ejecutivo del PMGD HBS GNL.**

De similar manera al caso anterior, en demanda baja se aprecian sobretensiones y

sobrecargas ya que este es el caso más exigente para el alimentador, debido a la

incorporación de inyección de generación. En la Figura XX, se aprecia la zona con

sobrecarga la que deberá ser reforzada a costo del PMGD HBS GNL, la que tiene una

extensión de 7,26[km] y se propone reforzarlo con un conductor de aluminio 4/0 o AAAC

equivalente.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 35 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

**Figura 16: Zona con Sobrecarga de Alimentador Laja.**

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 36 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

#### 8.2.3 Escenario: FB1612

|DIgSILENT<br>1,0900<br>[p.u.]<br>1,0540<br>1,0180<br>0,9820<br>0,9460<br>0,9100<br>0,0000 5,3836 10,767 16,151 21,534 [km] 26,918<br>Avell.. 525652 494225 534561 494231 494236 904182 241782 241777 470463 494265 163460 494280 494287 494295 560215 126359 126367 470376 469942 126391 126399 282511 282519 470320 743501 758709 282521 126458 239906 204476 239920 282657 282665 239941 126508 239951 126523 126531 126539 126547 126555 126563 126571 126579 126587 126595 126603 126611 126619 126627 126635 126643 282570 204838 126662 126670 126678 126686 814309 126701 468342 126716 629208 126731 126739 126747 1000271575 126762 279296<br>El<br>S/E<br>Voltage, Magnitude|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Voltage Profile-Laja<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/21/2015<br> Annex: /1|

**Figura 17: Perfil de Tensión, Tensión Cabecera = 1,01[pu].**

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 37 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|DIgSILENT<br>Grid: Summary Grid<br>S/E El Avellano Ul=22,680 kV<br>Generation = 5209,37 MW 55,19 Mvar 5209,66 MVA<br>u=0,986 p.u.<br>Ul=66,393 kV External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br>phiu=-10,698 deg Inter Area Flow = 0,00 MW 0,00 Mvar<br>u=1,006 p.u.<br>Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br>phiu=13,402 deg Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA rP = 9,3 6 9 M W<br>Load P(Un-U) = -0,00 MW 0,00 Mvar AQ = -1,7 8 9 M va<br>Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA MW P=-9,307 T ra fo T 2 kAS = 9,5 3 8 M V<br>Losses = 182,47 MW -1196,60 Mvar Line Charging = -2703,50 Mvar Compensation ind. = 1295,72 Mvar kA I=0,085 MVA S=9,718 Mvar Q=2,797 lo a d in g = 1 2 0,9 1 2 %I= 0,2 4 3 P Q I S l== == o-190a, 9,,, d752i 3. 834n.. . ...... Line01112<br>Avellano 23[kV] Compensation cap. = -1053,64 Mvar % loading=120,912<br>Installed Capacity = 7710,02 MW 66[kV..<br>Spinning Reserve = 2500,65 MW 1u6,06 =,. 01.....<br>Total Power Factor: Avellano upUl =h= i<br>Avellano 66[kV] Generation = 1,00 [-]<br>Load/Motor = 0,98 / 0,00 [-]<br>Punto de Conexión Punto de Repercusión<br>Ul=24,421 kV MW P=-3,880<br>u=1,062 p.u. Mvar Q=0,165<br>MVA S=3,883<br>phiu=-3,209 deg kA I=0,092 Line00010<br>% loading=74,017<br>P=0,009 MW<br>Q=0,002 Mvar P=0,009 MW PP126609 S=0,009 MVALine01051 Q=0,002 Mvar PP126610 Ul=24,4 kV I=0,000 kA S=0,009 MVA Il SQP =o === 0- 0 a-,, 0 00 d0, i, 00 00 n.. .. ... .. . Id_8145455<br>u=1,06 p.u. loading=0,181 %<br>phiu=-3,2 deg<br>P=10,560<br>MW<br>Q=-0,521<br>loading=79,330 kA 0 L 25 i I=0, ne MVA 0,572 0 S=10 0 r 9 Mva 0<br>%<br>ESTUDIO DE CONEXIÓN DE PMGD Project: 15034<br>CENTRAL HBS GNL Graphic: Resumen Ejecutiv<br>Propiedad de HBS GNL Date: 9/21/2015<br>Pow erFactory 15.1.7 Realizó Ing. René Moraga Castillo Annex: ES|Col2|Col3|Col4|
|---|---|---|---|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS GNL<br> Propiedad de HBS GNL<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/21/2015<br> Annex: ES<br>~~Ul=24~~,~~4 kV~~<br>u=1,06 p.u.<br>phiu=-3,2 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 5209,37 MW 55,19 Mvar 5209,66 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 182,47 MW -1196,60 Mvar<br> Line Charging = -2703,50 Mvar<br> Compensation ind. = 1295,72 Mvar<br> Compensation cap. = -1053,64 Mvar<br> Installed Capacity = 7710,02 MW<br> Spinning Reserve = 2500,65 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=66~~,~~393~~ ~~kV~~<br>u=1,006 p.u.<br>phiu=13,402 deg<br>~~U~~l~~=22,68~~0~~ kV~~<br>u=0,986 p.u.<br>phiu=-10,698 deg<br>~~U~~l~~=24,~~4~~21 kV~~<br>u=1,062 p.u.<br>phiu=-3,209 deg<br>Line01051<br>~~P~~=~~0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MV~~A~~<br>I=0,000 kA<br>loading=0,181 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,00..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-9,307 MW<br>Q=2,797 Mvar<br>S=9,718 MVA<br>I=0,085 kA<br>loading=120,912 %<br>P=9,369 MW<br>Q=-1,789 Mvar<br>S=9,538 MVA<br>I=0,243 kA<br>loading=120,912 %<br>Line01112<br>P=-9,3..<br>Q=1,78..<br>S=9,53..<br>I=0,24..<br>loadin..<br>Line00090<br>P=10,560 MW<br>Q=-0,521 Mvar<br>S=10,572 MVA<br>I=0,250 kA<br>loading=79,330 %<br>Line00010<br>P=-3,880 MW<br>Q=0,165 Mvar<br>S=3,883 MVA<br>I=0,092 kA<br>loading=74,017 %<br>Id_8145455<br>~~P=~~0~~,~~0~~09~~ ~~MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>**DIgSILENT**||ESTUDIO DE CONEXIÓN DE PMGD<br>|Project: 15034|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS GNL<br> Propiedad de HBS GNL<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/21/2015<br> Annex: ES<br>~~Ul=24~~,~~4 kV~~<br>u=1,06 p.u.<br>phiu=-3,2 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 5209,37 MW 55,19 Mvar 5209,66 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 182,47 MW -1196,60 Mvar<br> Line Charging = -2703,50 Mvar<br> Compensation ind. = 1295,72 Mvar<br> Compensation cap. = -1053,64 Mvar<br> Installed Capacity = 7710,02 MW<br> Spinning Reserve = 2500,65 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=66~~,~~393~~ ~~kV~~<br>u=1,006 p.u.<br>phiu=13,402 deg<br>~~U~~l~~=22,68~~0~~ kV~~<br>u=0,986 p.u.<br>phiu=-10,698 deg<br>~~U~~l~~=24,~~4~~21 kV~~<br>u=1,062 p.u.<br>phiu=-3,209 deg<br>Line01051<br>~~P~~=~~0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MV~~A~~<br>I=0,000 kA<br>loading=0,181 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,00..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-9,307 MW<br>Q=2,797 Mvar<br>S=9,718 MVA<br>I=0,085 kA<br>loading=120,912 %<br>P=9,369 MW<br>Q=-1,789 Mvar<br>S=9,538 MVA<br>I=0,243 kA<br>loading=120,912 %<br>Line01112<br>P=-9,3..<br>Q=1,78..<br>S=9,53..<br>I=0,24..<br>loadin..<br>Line00090<br>P=10,560 MW<br>Q=-0,521 Mvar<br>S=10,572 MVA<br>I=0,250 kA<br>loading=79,330 %<br>Line00010<br>P=-3,880 MW<br>Q=0,165 Mvar<br>S=3,883 MVA<br>I=0,092 kA<br>loading=74,017 %<br>Id_8145455<br>~~P=~~0~~,~~0~~09~~ ~~MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>**DIgSILENT**||CENTRAL HBS GNL<br> Propiedad de HBS GNL<br> Realizó Ing. René Moraga Castillo<br><br><br>|Graphic: Resumen Ejecutiv|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS GNL<br> Propiedad de HBS GNL<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/21/2015<br> Annex: ES<br>~~Ul=24~~,~~4 kV~~<br>u=1,06 p.u.<br>phiu=-3,2 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 5209,37 MW 55,19 Mvar 5209,66 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 182,47 MW -1196,60 Mvar<br> Line Charging = -2703,50 Mvar<br> Compensation ind. = 1295,72 Mvar<br> Compensation cap. = -1053,64 Mvar<br> Installed Capacity = 7710,02 MW<br> Spinning Reserve = 2500,65 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=66~~,~~393~~ ~~kV~~<br>u=1,006 p.u.<br>phiu=13,402 deg<br>~~U~~l~~=22,68~~0~~ kV~~<br>u=0,986 p.u.<br>phiu=-10,698 deg<br>~~U~~l~~=24,~~4~~21 kV~~<br>u=1,062 p.u.<br>phiu=-3,209 deg<br>Line01051<br>~~P~~=~~0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MV~~A~~<br>I=0,000 kA<br>loading=0,181 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,00..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-9,307 MW<br>Q=2,797 Mvar<br>S=9,718 MVA<br>I=0,085 kA<br>loading=120,912 %<br>P=9,369 MW<br>Q=-1,789 Mvar<br>S=9,538 MVA<br>I=0,243 kA<br>loading=120,912 %<br>Line01112<br>P=-9,3..<br>Q=1,78..<br>S=9,53..<br>I=0,24..<br>loadin..<br>Line00090<br>P=10,560 MW<br>Q=-0,521 Mvar<br>S=10,572 MVA<br>I=0,250 kA<br>loading=79,330 %<br>Line00010<br>P=-3,880 MW<br>Q=0,165 Mvar<br>S=3,883 MVA<br>I=0,092 kA<br>loading=74,017 %<br>Id_8145455<br>~~P=~~0~~,~~0~~09~~ ~~MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>**DIgSILENT**||CENTRAL HBS GNL<br> Propiedad de HBS GNL<br> Realizó Ing. René Moraga Castillo<br><br><br>|Date: 9/21/2015|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS GNL<br> Propiedad de HBS GNL<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/21/2015<br> Annex: ES<br>~~Ul=24~~,~~4 kV~~<br>u=1,06 p.u.<br>phiu=-3,2 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 5209,37 MW 55,19 Mvar 5209,66 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 182,47 MW -1196,60 Mvar<br> Line Charging = -2703,50 Mvar<br> Compensation ind. = 1295,72 Mvar<br> Compensation cap. = -1053,64 Mvar<br> Installed Capacity = 7710,02 MW<br> Spinning Reserve = 2500,65 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=66~~,~~393~~ ~~kV~~<br>u=1,006 p.u.<br>phiu=13,402 deg<br>~~U~~l~~=22,68~~0~~ kV~~<br>u=0,986 p.u.<br>phiu=-10,698 deg<br>~~U~~l~~=24,~~4~~21 kV~~<br>u=1,062 p.u.<br>phiu=-3,209 deg<br>Line01051<br>~~P~~=~~0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MV~~A~~<br>I=0,000 kA<br>loading=0,181 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,00..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-9,307 MW<br>Q=2,797 Mvar<br>S=9,718 MVA<br>I=0,085 kA<br>loading=120,912 %<br>P=9,369 MW<br>Q=-1,789 Mvar<br>S=9,538 MVA<br>I=0,243 kA<br>loading=120,912 %<br>Line01112<br>P=-9,3..<br>Q=1,78..<br>S=9,53..<br>I=0,24..<br>loadin..<br>Line00090<br>P=10,560 MW<br>Q=-0,521 Mvar<br>S=10,572 MVA<br>I=0,250 kA<br>loading=79,330 %<br>Line00010<br>P=-3,880 MW<br>Q=0,165 Mvar<br>S=3,883 MVA<br>I=0,092 kA<br>loading=74,017 %<br>Id_8145455<br>~~P=~~0~~,~~0~~09~~ ~~MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>**DIgSILENT**|Pow erFactory 15.1.7|Pow erFactory 15.1.7|Pow erFactory 15.1.7|
|**_PP126609_**<br>**_PP126610_**<br>**_Avellano 23[kV]_**<br>**_Avellano 66[kV]_**<br>**_S/E El Avellano_**<br>**_Punto de Repercusión_**<br>**_Punto de Conexión_**<br>Avellano 66[kV..<br>Ul=66,..<br>u=1,00..<br>phiu=1..<br> Pow erFactory 15.1.7<br> ESTUDIO DE CONEXIÓN DE PMGD<br> CENTRAL HBS GNL<br> Propiedad de HBS GNL<br> Realizó Ing. René Moraga Castillo<br> Project: 15034<br> Graphic: Resumen Ejecutiv<br> Date: 9/21/2015<br> Annex: ES<br>~~Ul=24~~,~~4 kV~~<br>u=1,06 p.u.<br>phiu=-3,2 deg<br> ~~Gr~~i~~d~~: ~~Summa~~r~~y~~ ~~Gr~~i~~d~~ <br> <br> Generation = 5209,37 MW 55,19 Mvar 5209,66 MVA<br> External Infeed = 0,00 MW 0,00 Mvar 0,00 MVA<br> Inter Area Flow = 0,00 MW 0,00 Mvar<br> Load P(U) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un) = 5026,90 MW 1009,70 Mvar 5127,30 MVA<br> Load P(Un-U) = -0,00 MW 0,00 Mvar<br> Motor Load P = 0,00 MW 0,00 Mvar 0,00 MVA<br> Losses = 182,47 MW -1196,60 Mvar<br> Line Charging = -2703,50 Mvar<br> Compensation ind. = 1295,72 Mvar<br> Compensation cap. = -1053,64 Mvar<br> Installed Capacity = 7710,02 MW<br> Spinning Reserve = 2500,65 MW<br> Total Power Factor:<br> Generation = 1,00 [-]<br> Load/Motor = 0,98 / 0,00[-] <br>~~Ul=66~~,~~393~~ ~~kV~~<br>u=1,006 p.u.<br>phiu=13,402 deg<br>~~U~~l~~=22,68~~0~~ kV~~<br>u=0,986 p.u.<br>phiu=-10,698 deg<br>~~U~~l~~=24,~~4~~21 kV~~<br>u=1,062 p.u.<br>phiu=-3,209 deg<br>Line01051<br>~~P~~=~~0~~,~~00~~9~~ MW~~<br>Q=0,002 Mvar<br>S=0,009 MV~~A~~<br>I=0,000 kA<br>loading=0,181 %<br>P=-0,0..<br>Q=-0,0..<br>S=0,00..<br>I=0,00..<br>loadin..<br>Trafo T2<br>P=-9,307 MW<br>Q=2,797 Mvar<br>S=9,718 MVA<br>I=0,085 kA<br>loading=120,912 %<br>P=9,369 MW<br>Q=-1,789 Mvar<br>S=9,538 MVA<br>I=0,243 kA<br>loading=120,912 %<br>Line01112<br>P=-9,3..<br>Q=1,78..<br>S=9,53..<br>I=0,24..<br>loadin..<br>Line00090<br>P=10,560 MW<br>Q=-0,521 Mvar<br>S=10,572 MVA<br>I=0,250 kA<br>loading=79,330 %<br>Line00010<br>P=-3,880 MW<br>Q=0,165 Mvar<br>S=3,883 MVA<br>I=0,092 kA<br>loading=74,017 %<br>Id_8145455<br>~~P=~~0~~,~~0~~09~~ ~~MW~~<br>Q=0,002 Mvar<br>S=0,009 MVA<br>**DIgSILENT**|Pow erFactory 15.1.7|Pow erFactory 15.1.7|Annex: ES|

**Figura 18: Resumen Ejecutivo del PMGD HBS GNL.**

Observando el perfil de tensiones y el anexo con los porcentajes de carga de las líneas, se

concluye que con el refuerzo propuesto se cumple con el nivel de tensión y los

porcentajes de carga para mantener la calidad de servicio del alimentador.

#### 8.2.4 Resumen Resultados Flujos de Potencia Con PMGD HBS GNL

En esta sección se presenta el resumen de los resultados de los escenarios, considerando

la inyección del total de la potencia de los dos PMGD considerando un factor de potencia

igual a la unidad, observando el comportamiento de los niveles de tensión, el porcentaje

de carga de elementos serie y el transformador de poder.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 38 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

**Tabla 24: Tensiones en Puntos de Interés.**

**Escenario** **Barra** **Tensión[pu]** **Mín. de FP[-]**

FA-16-11

FA-16-12

FB-16-11

FB-16-12

126609 1,103 1,00

126610 1,104 1,00

821739 1,103 0,98

Avellano 23[kV] 0,978 0,99

Avellano 66[kV] 1 0,99

126609 1,032 1,00

126610 1,033 1,00

821739 1,032 0,98

Avellano 23[kV] 0,976 0,99

Avellano 66[kV] 1 0,99

126609 1,137 1,00

126610 1,138 1,00

821739 1,137 0,98

Avellano 23[kV] 0,989 1,00

Avellano 66[kV] 1,006 0,99

126609 1,062 1,00

126610 1,062 1,00

821739 1,062 0,98

Avellano 23[kV] 0,986 1,00

Avellano 66[kV] 1,006 0,99

Como se aprecia en la Tabla 24, los niveles de tensión en el año 2016 considerando la

inyección de los 10,75[MW] de ambos PMGD, se encuentran dentro de los niveles

establecidos por la normativa vigente debido a la incorporación del refuerzo propuesto.

**Tabla 25: Máximos Porcentajes de Carga en Tramos de Línea.**

**Escenario** **Máx. de Carga[%]** **Máx. de P[MW]** **Máx. de Q[MVAr]**

FA-16-11 180,392 9,815 0,292

FA-16-12 75,845 9,804 0,292

FB-16-11 188,157 10,569 0,026

FB-16-12 107,449 10,56 0,026

En la Tabla 25 se aprecian que existen problemas de sobrecarga en el alimentador tanto

en demanda alta y baja, por lo que no al incluir el refuerzo se cumple con los porcentajes

de carga considerando una temperatura de operación de 25°C, lo que significa que tiene

una holgura mayor este conductor al proyectar el aumento de ampacidad por

temperatura de operación.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 39 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

**Tabla 26: Máximos Porcentajes de Carga en Transformador.**

**Escenario** **Equipo** **Snom[MW]** **S[MVA]** **Carga[%]**

FA-16-11 Trafo T2 10 5,859 58,59

FB-16-11 Trafo T2 10 9,06 90,6

FA-16-12 Trafo T2 10 6,446 64,46

FB-16-12 Trafo T2 10 9,718 97,18

Los porcentajes de carga del transformador de poder se encuentran dentro de los niveles

aceptables.

#### 8.2.5 Revisión Ajuste del Nivel de Tensión con PMGD HBS GNL

En este punto se analiza los niveles de tensión para las situaciones con y sin inyección de

potencia del PMGD HBS GNL, con el fin de determinar si existen inconvenientes para que

este opere en modalidad PQ. En caso de no ser posible la operación con un factor de

potencia fijo, se propondrá un rango de ajuste de tensión de los generadores para su

operación como PV.

**Tabla 27: Tabla Análisis Nivel de Tensión en Punto de Repercusión.**

 **% Resp.**
**Escenario** **Barra** **Tensión[pu]** **-6%** **6%** **Con PMGD**
**Valor Obtenido**

 **% Respecto**

**a 1[pu]**

**¿Tensión Dentro**

**de Norma?**

FA-16-00

FA-16-11

FA-16-12

FB-16-00

FB-16-11

FB-16-12

126609 1,02 0,96 1,08 1,03 1% 3% Sí

821739 1,02 0,96 1,08 1,03 1% 3% Sí

Avellano 23[kV] 0,99 0,93 1,04 0,98 1% 2% Sí

126609 1,10 1,04 1,17 - - -
821739 1,10 1,04 1,17 - - -
Avellano 23[kV] 0,98 0,92 1,04 - - -

126609 1,03 0,97 1,09 - - -
821739 1,03 0,97 1,09 - - -
Avellano 23[kV] 0,98 0,92 1,03 - - -

126609 1,05 0,99 1,11 1,06 1% 6% Sí

821739 1,05 0,99 1,11 1,06 1% 6% Sí

Avellano 23[kV] 0,99 0,93 1,05 0,99 0% 1% Sí

126609 1,14 1,07 1,21 - - -
821739 1,14 1,07 1,21 - - -
Avellano 23[kV] 0,99 0,93 1,05 - - -

126609 1,06 1,00 1,13 - - -
821739 1,06 1,00 1,13 - - -
Avellano 23[kV] 0,99 0,93 1,05 - - -

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 40 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

A partir de los resultados de la Tabla 27, se aprecia que la variación de tensión en el

punto de repercusión es inferir al ±6% que exige la normativa. En vista de los resultados

obtenidos de la tensión, es posible despachar los 10,75[MW] en modalidad PQ sin

afectar al punto de repercusión.

### 8.3 Comentarios Resultados Estudio de Flujos de Potencia

Con los resultados del estudio de flujos de potencia, se obtienen las siguientes

conclusiones parciales:

 Son requeridas obras adicionales por parte del PMGD HBS GNL, esto debido a

que existen sobrecarga en los elementos de la red de distribución.

 El despacho a plena carga del PMGD en modalidad PQ no afecta al punto de

repercusión, manteniendo este último una variación de tensión dentro del

rango exigido por el DS244 y la NTCO.

 El factor de potencia mantiene el valor exigido por la normativa, tanto en

23[kV] como en la barra de 66[kV].

Respetando los hitos mencionados, tanto el PMGD como el alimentador Laja no tendrán

problemas desde el punto de vista estático.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 41 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

## 9 ESTUDIO DE COMPORTAMIENTO DINÁMICO

Para determinar el comportamiento dinámico del sistema, considerando la incorporación

de las inyecciones de los excedentes de la energía del PMGD HBS GNL, se realizaron

simulaciones donde se examinan las principales variables eléctricas en función del

tiempo.

Considerando los requerimientos normativos y la probabilidad de ocurrencia de las

distintas contingencias en un sistema de distribución, es que se ha determinado como

casos de estudios los siguientes escenarios:

 Pérdida de Generación: Corresponde a un escenario con despacho máxima y

posterior pérdida total de la generación.

 Fallas en Elementos Serie: Corresponde a un escenario con la falla más común

en el sistema de distribución (1FT), considerando la operación de las

protecciones en un tiempo máximo de 20 ciclos y la desconexión de la

generación antes de la primera reconexión.

En las secciones siguientes se presentan los resultados, verificando que la recuperación

de tensión luego de 10[ms] de ocurrida la contingencia esté por sobre 0,7[pu], la

estabilización ocurra antes de 20[s], que no descienda la frecuencia a niveles bajo

normativa y la observación del comportamiento de las unidades del PMGD en cuanto a

salida antes de la primera reconexión.

### 9.1 Configuración de los Estudios Dinámicos

**Tabla 28: Configuración Simulación por Pérdida de Generación.**

Tiempo [s] Pérdida de Generación

0,00 Régimen Permanente (inicio de la simulación).
0,10 Desconexión Intempestiva de la Generación.
2,1 Fin de la simulación.

**Tabla 29: Configuración Simulación por Falla.**

Tiempo [s] Falla en Línea

0,00 Régimen Permanente (inicio de la simulación).
0,10 Cortocircuito monofásico a tierra.
0,22 Desconexión del Generador.
0,5 Operación equipos de protección de la red Dx.
3,5 Reconexión
10,1 Fin de la simulación.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 42 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

### 9.2 Resultados Desconexión Intempestiva de Generación

A continuación se observará el comportamiento de los niveles de tensión, frecuencia y

ángulos rotóricos de algunas máquinas del sistema, ante la ocurrencia de una

contingencia que deja fuera la totalidad de la inyección de excedentes de potencia del

PMGD HBS Energía 4[MW] y HBS GNL 6,75[MW].

#### 9.2.1 Escenario DA-1-PG

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||1.013 p.u.||
||||||||
||||||1.002 p.u.||
||||||||
||||||||
||||||||
||||||0.996 p.u.||
||||||0.993 p.u.<br>||
||||||||
||||||||

|DIgSILENT<br>1,03<br>1,02<br>1.013 p.u.<br>1,01<br>1.002 p.u.<br>1,00<br>0.996 p.u.<br>0.993 p.u.<br>0,99<br>0,98<br>0,0000 0,4200 0,8399 1,2599 1,6799 [s] 2,0998<br>Avellano 23[kV]: Voltage, Magnitude in p.u.<br>S/E El Avellano\Avellano 66[kV]: Voltage, Magnitude in p.u.<br>MVelas\B-MansoVelasco: Voltage, Magnitude in p.u.<br>LA\B2-LosAngeles: Voltage, Magnitude in p.u.|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Tensiones<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /5|

**Figura 19: Tensiones del Sistema.**

De la Figura 19 se aprecia que al perder la generación de ambos PMGD’s la tensión

desciende levemente en el sistema y el regulador del transformador T2 rectifica la

tensión en 23[kV]. Los niveles de tensión están dentro de los límites establecidos por la

normativa mucho antes de los 20[s] de permitidos para la estabilización.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 43 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||49.990 Hz||
|||||||
|||||||
|||||||

|DIgSILENT<br>51,00<br>50,60<br>50,20<br>49.990 Hz<br>49,80<br>49,40<br>49,00<br>0,0000 0,4200 0,8399 1,2599 1,6799 [s] 2,0998<br>Avellano 23[kV]: Electrical Frequency in Hz<br>S/E El Avellano\Avellano 66[kV]: Electrical Frequency in Hz<br>MVelas\B-MansoVelasco: Electrical Frequency in Hz<br>LA\B2-LosAngeles: Electrical Frequency in Hz|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Frecuencia<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /4|

**Figura 20: Frecuencia del Sistema.**

No existen cambios significativos en la frecuencia, producto de la pérdida completa de

generación existente y proyectada en el alimentador Laja.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 44 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||7.472 deg||
|||||0.000 deg<br>||
|||||||
|||||-19.003 deg||
|||||||
|||||||

|DIgSILENT<br>20,00<br>10,00<br>7.472 deg<br>0,00 0.000 deg<br>-10,00<br>-19.003 deg<br>-20,00<br>-30,00<br>0,0000 0,4200 0,8399 1,2599 1,6799 [s] 2,0998<br>Cholguán: Rotor angle with reference to reference machine angle in deg<br>Ralco U1: MW<br>Ralco U2: MW|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Ángulos Rotóricos<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /3|

**Figura 21: Excursiones Angulares.**

No se experimentan excursiones angulares que pongan en riesgo la estabilidad del

sistema interconectado.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 45 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|DIgSILENT<br>1,20<br>0,90<br>0,60<br>0,30<br>0,00<br>-0,30<br>0,0000 0,4200 0,8399 1,2599 1,6799 [s] 2,0998<br>BG#1: Electrical Power in p.u.<br>BG#2: Electrical Power in p.u.<br>BG#3: Electrical Power in p.u.<br>BG#4: Electrical Power in p.u.<br>GN#1: Electrical Power in p.u.<br>GN#2: Electrical Power in p.u.<br>GN#3: Electrical Power in p.u.<br>GN#4: Electrical Power in p.u.<br>GN#5: Electrical Power in p.u.|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>PMGD<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /6|

**Figura 22: Potencia PMGD.**

Se ha incluido la presentación de las potencias activas de los generadores a fin de

demostrar su salida del sistema.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 46 DE 60

#### 9.2.2 Escenario DB-1-PG

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||1.016 p.u.||
||||||1.011 p.u.<br>||
||||||||
||||||1.008 p.u.||
||||||1.003 p.u.<br>||
||||||||
||||||||
||||||||

|DIgSILENT<br>1,03<br>1,02<br>1.016 p.u.<br>1.011 p.u.<br>1,01<br>1.008 p.u.<br>1.003 p.u.<br>1,00<br>0,99<br>0,98<br>0,0000 0,4200 0,8399 1,2599 1,6799 [s] 2,0998<br>Avellano 23[kV]: Voltage, Magnitude in p.u.<br>S/E El Avellano\Avellano 66[kV]: Voltage, Magnitude in p.u.<br>MVelas\B-MansoVelasco: Voltage, Magnitude in p.u.<br>LA\B2-LosAngeles: Voltage, Magnitude in p.u.|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Tensiones<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /5|

**Figura 23: Tensiones del Sistema.**

Se aprecia que al perder la generación de ambos PMGD’s la tensión desciende levemente

en el sistema y el regulador del transformador T2 rectifica la tensión en 23[kV], debido a

la inversión de los flujos. Los niveles de tensión están dentro de los límites establecidos

por la normativa mucho antes de los 20[s] de permitidos para la estabilización.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 47 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||49.986 Hz||
|||||||
|||||||
|||||||

|DIgSILENT<br>51,00<br>50,60<br>50,20<br>49.986 Hz<br>49,80<br>49,40<br>49,00<br>0,0000 0,4200 0,8399 1,2599 1,6799 [s] 2,0998<br>Avellano 23[kV]: Electrical Frequency in Hz<br>S/E El Avellano\Avellano 66[kV]: Electrical Frequency in Hz<br>MVelas\B-MansoVelasco: Electrical Frequency in Hz<br>LA\B2-LosAngeles: Electrical Frequency in Hz|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Frecuencia<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /4|

**Figura 24: Frecuencia del Sistema.**

No existen cambios significativos en la frecuencia, producto de la pérdida completa de

generación del PMGD HBS Energía.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 48 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||6.792 deg||
|||||0.000 deg<br>||
|||||||
|||||-19.010 deg||
|||||||
|||||||

|DIgSILENT<br>20,00<br>10,00<br>6.792 deg<br>0,00 0.000 deg<br>-10,00<br>-19.010 deg<br>-20,00<br>-30,00<br>0,0000 0,4200 0,8399 1,2599 1,6799 [s] 2,0998<br>Cholguán: Rotor angle with reference to reference machine angle in deg<br>Ralco U1: MW<br>Ralco U2: MW|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Ángulos Rotóricos<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /3|

**Figura 25: Excursiones Angulares.**

No se experimentan excursiones angulares que pongan en riesgo la estabilidad del

sistema interconectado.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 49 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|DIgSILENT<br>1,20<br>0,90<br>0,60<br>0,30<br>0,00<br>-0,30<br>0,0000 0,4200 0,8399 1,2599 1,6799 [s] 2,0998<br>BG#1: Electrical Power in p.u.<br>BG#2: Electrical Power in p.u.<br>BG#3: Electrical Power in p.u.<br>BG#4: Electrical Power in p.u.<br>GN#1: Electrical Power in p.u.<br>GN#2: Electrical Power in p.u.<br>GN#3: Electrical Power in p.u.<br>GN#4: Electrical Power in p.u.<br>GN#5: Electrical Power in p.u.|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>PMGD<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /6|

**Figura 26: Potencia PMGD.**

Se ha incluido la presentación de las potencias activas de los generadores a fin de

demostrar su salida del sistema.

### 9.3 Resultados Falla en Elemento Serie del Alimentador

A continuación se observará el comportamiento de los niveles de tensión, frecuencia,

excursiones angulares y despacho del PMGD, ante la ocurrencia de una contingencia en

un tramo de línea cercano a la cabecera del alimentador Laja, el que será despejado por

los equipos de la propia red y estará coordinado con la salida del PMGD existente y el

proyectado, antes de la primera reconexión.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 50 DE 60

#### 9.3.1 Escenario DA-1-CC

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|Col2|1.015 p.u.<br>1.000 p.u.|Col4|Col5|Col6|1.013 p.u.<br>1.002 p.u.<br>0.993 p.u.|Col8|
|---|---|---|---|---|---|---|---|
|||~~ 1.000 p.u.~~<br> 1.015 p.u.||||~~ 0.993 p.u.~~<br> 1.002 p.u.<br> 1.013 p.u.||
|||||||||
|||||||||
|||||||||
|||||||||

|DIgSILENT<br>1,20<br>1.013 p.u.<br>1.015 p.u. 1.002 p.u.<br>1.000 p.u. 0.993 p.u.<br>0,90<br>0,60<br>0,30<br>0,00<br>-0,30<br>0,0000 2,0198 4,0397 6,0595 8,0793 [s] 10,099<br>Avellano 23[kV]: Voltage, Magnitude in p.u.<br>S/E El Avellano\Avellano 66[kV]: Voltage, Magnitude in p.u.<br>MVelas\B-MansoVelasco: Voltage, Magnitude in p.u.<br>LA\B2-LosAngeles: Voltage, Magnitude in p.u.|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Tensiones<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /5|

**Figura 27: Tensiones del Sistema.**

Se observa que tras la ocurrencia de falla se aprecia un descenso en la tensión de las

barras de la zona de influencia, que 10[ms] luego de despejada la contingencia se

encuentra por sobre 0,7[pu] como exige la normativa. La estabilización ocurre mucho

antes a los 20[s] establecidos.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 51 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||49.982 Hz||
|||||49.982 Hz||
|||||||
|||||||

|DIgSILENT<br>51,00<br>50,60<br>50,20<br>49.982 Hz<br>49,80<br>49,40<br>49,00<br>0,0000 2,0198 4,0397 6,0595 8,0793 [s] 10,099<br>Avellano 23[kV]: Electrical Frequency in Hz<br>S/E El Avellano\Avellano 66[kV]: Electrical Frequency in Hz<br>MVelas\B-MansoVelasco: Electrical Frequency in Hz<br>LA\B2-LosAngeles: Electrical Frequency in Hz|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Frecuencia<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /4|

**Figura 28: Frecuencia del Sistema.**

No existen cambios significativos en la frecuencia, producto de la falla en la cabecera del

alimentador y pérdida completa de la generación existente y proyectada en el

alimentador Laja.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 52 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||0.000 deg<br> 7.477 deg||
|||||0.000 deg<br> 7.477 deg||
|||||||
|||||-18.997 deg||
|||||-18.997 deg||
|||||||

|DIgSILENT<br>20,00<br>10,00<br>7.477 deg<br>0,00 0.000 deg<br>-10,00<br>-18.997 deg<br>-20,00<br>-30,00<br>0,0000 2,0198 4,0397 6,0595 8,0793 [s] 10,099<br>Cholguán: Rotor angle with reference to reference machine angle in deg<br>Ralco U1: MW<br>Ralco U2: MW|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Ángulos Rotóricos<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /3|

**Figura 29: Excursiones Angulares.**

No se experimentan excursiones angulares que pongan en riesgo la estabilidad del

sistema interconectado.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 53 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||0.000 p.u.||
|||||||||

|DIgSILENT<br>1,60<br>1,20<br>0,80<br>0,40<br>0,00 0.000 p.u.<br>-0,40<br>0,0000 2,0198 4,0397 6,0595 8,0793 [s] 10,099<br>BG#1: Electrical Power in p.u.<br>BG#2: Electrical Power in p.u.<br>BG#3: Electrical Power in p.u.<br>BG#4: Electrical Power in p.u.<br>GN#1: Electrical Power in p.u.<br>GN#2: Electrical Power in p.u.<br>GN#3: Electrical Power in p.u.<br>GN#4: Electrical Power in p.u.<br>GN#5: Electrical Power in p.u.|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>PMGD<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /6|

**Figura 30: Potencia PMGD.**

Se ha incluido la presentación de las potencias activas de los generadores a fin de

demostrar su salida del sistema, al ocurrir la contingencia y antes de la primera

reconexión ajustada en 3[s] [4] .

4 De acuerdo a lo informado mediante Formulario N°2.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 54 DE 60

#### 9.3.2 Escenario DB-1-CC

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|Col2|1.014 p.u.<br>1.005 p.u.<br>0.991 p.u.|Col4|Col5|Col6|1.011 p.u.<br>1.003 p.u.|Col8|
|---|---|---|---|---|---|---|---|
|||~~ 0.991 p.u.~~<br> 1.005 p.u.<br> 1.014 p.u.||||~~ 1.003 p.u.~~<br> 1.011 p.u.||
|||||||||
|||||||||
|||||||||
|||||||||

|DIgSILENT<br>1,20<br>011 ... 900 901 154 ppp ... uuu ... 11 .. 00 01 31 pp .. uu ..<br>0,90<br>0,60<br>0,30<br>0,00<br>-0,30<br>0,0000 2,0198 4,0397 6,0595 8,0793 [s] 10,099<br>Avellano 23[kV]: Voltage, Magnitude in p.u.<br>S/E El Avellano\Avellano 66[kV]: Voltage, Magnitude in p.u.<br>MVelas\B-MansoVelasco: Voltage, Magnitude in p.u.<br>LA\B2-LosAngeles: Voltage, Magnitude in p.u.|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Tensiones<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /5|

**Figura 31: Tensiones del Sistema.**

Se observa que tras la ocurrencia de falla se aprecia un descenso en la tensión de las

barras de la zona de influencia, que 10[ms] luego de despejada la contingencia se

encuentra por sobre 0,7[pu] como exige la normativa. La estabilización ocurre mucho

antes a los 20[s] establecidos.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 55 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||49.974 Hz||
|||||49.974 Hz||
|||||||
|||||||

|DIgSILENT<br>51,00<br>50,60<br>50,20<br>49.974 Hz<br>49,80<br>49,40<br>49,00<br>0,0000 2,0198 4,0397 6,0595 8,0793 [s] 10,099<br>Avellano 23[kV]: Electrical Frequency in Hz<br>S/E El Avellano\Avellano 66[kV]: Electrical Frequency in Hz<br>MVelas\B-MansoVelasco: Electrical Frequency in Hz<br>LA\B2-LosAngeles: Electrical Frequency in Hz|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Frecuencia<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /4|

**Figura 32: Frecuencia del Sistema.**

No existen cambios significativos en la frecuencia, producto de la falla en la cabecera del

alimentador y pérdida completa de la generación existente y proyectada en el

alimentador Laja.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 56 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||0.000 deg<br> 6.800 deg||
|||||0.000 deg<br> 6.800 deg||
|||||||
|||||-18.977 deg||
|||||-18.977 deg||
|||||||

|DIgSILENT<br>20,00<br>10,00<br>6.800 deg<br>0,00 0.000 deg<br>-10,00<br>-18.977 deg<br>-20,00<br>-30,00<br>0,0000 2,0198 4,0397 6,0595 8,0793 [s] 10,099<br>Cholguán: Rotor angle with reference to reference machine angle in deg<br>Ralco U1: MW<br>Ralco U2: MW|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>Ángulos Rotóricos<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /3|

**Figura 33: Excursiones Angulares.**

No se experimentan excursiones angulares que pongan en riesgo la estabilidad del

sistema interconectado.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 57 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||0.000 p.u.||
|||||||||

|DIgSILENT<br>1,60<br>1,20<br>0,80<br>0,40<br>0,00 0.000 p.u.<br>-0,40<br>0,0000 2,0198 4,0397 6,0595 8,0793 [s] 10,099<br>BG#1: Electrical Power in p.u.<br>BG#2: Electrical Power in p.u.<br>BG#3: Electrical Power in p.u.<br>BG#4: Electrical Power in p.u.<br>GN#1: Electrical Power in p.u.<br>GN#2: Electrical Power in p.u.<br>GN#3: Electrical Power in p.u.<br>GN#4: Electrical Power in p.u.<br>GN#5: Electrical Power in p.u.|Col2|Col3|
|---|---|---|
||ESTUDIO DE CONEXIÓN DE PMGD<br>PMGD<br>CENTRAL HBS ENERGÍA<br>RealizóIng. René Moraga Castillo<br><br>|Date: 9/17/2015<br> Annex: /6|

**Figura 34: Potencia PMGD.**

Se ha incluido la presentación de las potencias activas de los generadores a fin de

demostrar su salida del sistema, al ocurrir la contingencia y antes de la primera

reconexión ajustada en 3[s].

### 9.4 Comentarios Resultados Comportamiento Dinámico

De acuerdo a los resultados observados en los diagramas, es posible notar que ante

contingencias de pérdidas de generación y el despeje tripolar de fallas, los niveles de

tensión se recuperan dentro de los primeros 10[ms], sin presentar grandes oscilaciones

por lo que no se ve afectada la frecuencia del sistema.

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 58 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

## 10 CONCLUSIONES FINALES

Conforme a los resultados obtenidos en el estudio de cortocircuito, se concluye que no

existen equipos que vean superadas las corrientes máximas de ruptura producto del

nuevo proyecto de generación.

El estudio efectuado cumple con lo requerido en la DS N°244 y la NTCO, analizando

diferentes demandas, modos de operación y contingencias en el sistema de distribución,

no presentando problemas e incumplimientos de lo establecido en la normativa vigente.

Con los diferentes casos analizados y las obras propuestas a cargo del PMGD HBS GNL, se

ha determinado que el impacto de la nueva central en la operación del alimentador Laja

está dentro de los márgenes normales.

A partir de las variables observadas se obtienen las siguientes conclusiones:

 Los estudios estáticos de flujos de carga demuestran utilizando el refuerzo

propuesto para el tramo de 7,26[km] no se pone en riesgo la operación del

sistema. No presentando sobrecarga en elementos serie considerando el plan

de obra, ni en el transformador de poder existente.

 Los estudios estáticos de flujos de carga demuestran que la tensión se

mantiene dentro de lo establecido por la NTCO frente a las distintas

contingencias considerando la nueva obra.

 El despacho a plena carga del PMGD en modalidad PQ no afecta al punto de

repercusión, manteniendo este último una variación de tensión dentro del

rango exigido por el DS244 y la NTCO, posterior a la incorporación del

refuerzo de tramos de líneas

 Los estudios dinámicos han demostrado que ante las contingencias

analizadas, las nuevas instalaciones no afectan la respuesta amortiguada de

los elementos críticos. Los niveles de tensión se encuentran dentro de los

límites transcurridos 10[ms] luego de aclarada la contingencia y se estabiliza,

en menos de los 20[s] permitidos.

En función de los resultados arrojados por los diversos estudios se concluye que la

incorporación del nuevo “PMGD HBS GNL 6,75[MW]” no provocará efecto adverso en la

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 59 DE 60

ESTUDIO DE SISTEMA

15034-E-IN-004
PMGD HBS GNL 6,75[MW]

operación normal del sistema así como tampoco en condiciones de falla, ante las

contingencias analizadas en este estudio.

## 11 ANEXOS

 Anexo 1: Estudio de Flujos de Potencia

 - Anexo 2: Estudio de Cortocircuito

 - Anexo 3: Estudio Dinámico

TECNORED INGENIERÍA Y SERVICIOS

CERRO EL PLOMO 3819, PARQUE INDUSTRIAL CURAUMA, VALPARAÍSO

www.tecnored.cl, +56(032)2452686-+56(9)94797525

PÁGINA 60 DE 60