---
title: Tipo Informe
author: Bravo, Lucy
date: D:20210903121227-04'00'
language: es
type: report
pages: 20
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Tabla de Contenidos
  - 1. Introducción
  - 2. Objetivos
  - 3. Alcances
  - 4. Límite de Batería
  - 5. Referencias
  - 6. Descripción General del Proceso
  - 7. Filosofía de Operación en Condiciones Normales
  - 8. Filosofía de Control
  - 9. Procedimiento de Detención
  ... y 1 secciones más
-->

|CORPORACIÓN NACIONAL DEL COBRE DE CHILE<br>VICEPRESIDENCIA DE PROYECTOS<br>CE-001 INGENIERÍA BÁSICA, SISTEMA DE TRANSPORTE<br>ESPESAMIENTO Y DEPOSITACION DE RELAVES<br>ESTUDIO ACTUALIZACIÓN DE FACTIBILIDAD<br>CONTRATO N° 4400241113<br>INGENIERÍA BÁSICA|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ÁREA:**|**ÁREA:**|**ÁREA:**|**GENERAL**|**GENERAL**|**GENERAL**|**GENERAL**|**GENERAL**|**GENERAL**|**GENERAL**|
|**SUBÁREA:**|**SUBÁREA:**|**SUBÁREA:**||||||||
|**CONTENIDO:**|**CONTENIDO:**|**CONTENIDO:**|**PLAN DE OPERACIÓN NORMAL - AGUA RECUPERADA PEAD**|**PLAN DE OPERACIÓN NORMAL - AGUA RECUPERADA PEAD**|**PLAN DE OPERACIÓN NORMAL - AGUA RECUPERADA PEAD**|**PLAN DE OPERACIÓN NORMAL - AGUA RECUPERADA PEAD**|**PLAN DE OPERACIÓN NORMAL - AGUA RECUPERADA PEAD**|**PLAN DE OPERACIÓN NORMAL - AGUA RECUPERADA PEAD**|**PLAN DE OPERACIÓN NORMAL - AGUA RECUPERADA PEAD**|
|**TIPO DE DOCUMENTO:**|**TIPO DE DOCUMENTO:**|**TIPO DE DOCUMENTO:**|**INFORME TÉCNICO**|**INFORME TÉCNICO**|**INFORME TÉCNICO**|**INFORME TÉCNICO**|**INFORME TÉCNICO**|**INFORME TÉCNICO**|**INFORME TÉCNICO**|
|**CÓDIGO VP:**|**CÓDIGO VP:**|**CÓDIGO VP:**|**4400241113-0000-PNLSU-00009**|**4400241113-0000-PNLSU-00009**|**4400241113-0000-PNLSU-00009**|**4400241113-0000-PNLSU-00009**|**4400241113-0000-PNLSU-00009**|**4400241113-0000-PNLSU-00009**|**4400241113-0000-PNLSU-00009**|
|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|
|||||||||||
|**P **|**03/09/21**|**Siguiente Fase**|**Siguiente Fase**|**AGV**|**RSM**|**HAN**|**JBT**|**PMP**|**GCP**|
|**B **|**17/06/21**|**Revisión Cliente**|**Revisión Cliente**|**NPQ**|**AGV**|**RSM**|**JBT**|**PMP**|**GCP**|
|**A **|**02/06/21**|**Revisión Interna**|**Revisión Interna**|**NPQ**|**AGV**|**RSM**||||
|**REV N°**|**FECHA**|**EMITIDO PARA**|**EMITIDO PARA**|**POR**|**REV.**|**APR.**|**I.ESP./L.EWP**|**J.ING.**|**DIR./GER.**|
|**REV N°**|**FECHA**|**EMITIDO PARA**|**EMITIDO PARA**|**HATCH **|**HATCH **|**HATCH **|**CODELCO **|**CODELCO **|**CODELCO **|

|Col1|N° DE PROYECTO: H362274|Pág. 1 de 20|
|---|---|---|
||**H362274-0000-124-050-0007**|**REV.** **P **|

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

# Tabla de Contenidos

**1.** **Introducción .................................................................................................................................... 4**

**2.** **Objetivos ......................................................................................................................................... 4**

**3.** **Alcances .......................................................................................................................................... 4**

**4.** **Límite de Batería ............................................................................................................................. 5**

**5.** **Referencias ...................................................................................................................................... 5**

**6.** **Descripción General del Proceso ................................................................................................... 5**

**7.** **Filosofía de Operación en Condiciones Normales ........................................................................ 8**

**8.** **Filosofía de Control ....................................................................................................................... 12**

8.1 Arquitectura Sistema de Control ............................................................................................. 12
8.2 Simbología en Instrumentación y Control ................................................................................ 14
8.3 Centro de Supervisión y Operación......................................................................................... 14
8.4 Modos de Operación .............................................................................................................. 15
8.5 Mantenimiento ........................................................................................................................ 15

**9.** **Procedimiento de Detención ........................................................................................................ 15**

9.1 Descripción General ............................................................................................................... 16
9.2 Blackout ................................................................................................................................. 16
9.3 Protección de equipos ............................................................................................................ 16
9.4 Situaciones Accidentales ........................................................................................................ 17

**10.** **Resolución de Problemas Operacionales .................................................................................... 17**

10.1 Problemas Operacionales en la PEAD que afectan el agua recuperada .................................. 17

10.1.1 Falla Bombas Principales de Alimentación Distribuidor Presurizado ............................ 17
10.1.2 Falla en Distribuidor Presurizado ................................................................................. 18
10.1.3 Espesadores Fuera de Servicio ................................................................................... 18
10.1.4 Falla en Bomba Principal de Relaves Espesado de Descarga ..................................... 18
10.1.5 Falla en Bomba de Cizalle ........................................................................................... 18
10.2 Problemas Operacionales en Espesadores de Alta Densidad ................................................. 18

10.2.1 Torque Excesivo del Espesador .................................................................................. 19
10.2.2 Baja Concentración de Sólidos en Relaves Espesados ............................................... 19
10.2.3 Aumento de Turbidez Agua Recuperada ..................................................................... 20

_**Lista de Tablas**_

Tabla 7-1: Caudal unitario de agua recuperada por espesador ................................................................ 8

<!-- INICIO TABLA 7-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- - Concentración de sólidos en la descarga del espesador Los caudales unitarios máximo, nominal y mínimo por espesador de las divisiones CH-MH y RT se presentan en la siguiente tabla. -->

**Tabla 7-1: Caudal unitario de agua recuperada por espesador****

| División | Caudal por Espesador [m3/h] | Col3 | Col4 |
| --- | --- | --- | --- |
| **División** | **Máximo** | **Nominal** | **Mínimo** |
| CH-MH | 1.016 | 550 | 302 |
| RT | 926 | 558 | 360 |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- La recuperación de agua desde los espesadores sobre la plataforma de la PEAD se proyecta en sistemas independientes para CH-MH y RT, utilizando canaletas de hormigón dispuestas a nivel de la plataforma de la PEAD (3765-CNL-1001/2001). El sistema RT, comienza en los espesadores 3762-ERV-2001 & 2003 y continua su recorrido de modo de recolectar el agua -->
<!-- FIN TABLA 7-1 -->

Tabla 9-1: Alarmas y Causas Típicas de Detención Motores Eléctricos .................................................. 17

<!-- INICIO TABLA 9-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la Tabla 9-1 se indican las alarmas y causa típicas de detención para el caso de motores eléctricos. -->

**Tabla 9-1: Alarmas y Causas Típicas de Detención Motores Eléctricos****

| Alarma | Causa |
| --- | --- |
| Sobrecarga de motor | Fallas en las protecciones eléctricas o problemas de<br>comunicación |
| Temperatura excesiva motor | Temperatura excesiva motor |
| Falla variador de frecuencia | Falla real o problemas de comunicación |

<!-- Estadísticas: 3 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **9.4** **Situaciones Accidentales** Estas situaciones se describen en el “Plan de Preparación y Respuesta ante Emergencias Sistema de Agua Recuperada PEAD” (4400241113-0000-PLNSU-00010). -->
<!-- FIN TABLA 9-1 -->


_**Lista de Figuras**_

Figura 6-1: Esquema Simplificado Proyecto de Relaves Espesados Talabre............................................ 7
Figura 7-1: Sistema de Recuperación de Agua de PEAD, ver detalle en Ref. 5 ...................................... 10
Figura 7-2: Modelo BIM Sistema de Recuperación de Agua en PEAD ................................................... 11

H362274-0000-124-050-0007
Pág. 2 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

Figura 7-3: Modelo BIM Canaletas y Cajón disipador de AR .................................................................. 11
Figura 7-4: Modelo BIM Cajón Distribuidor y Piscinas de AR ................................................................. 12
Figura 7-5: Modelo BIM Sentina de AR .................................................................................................. 12

H362274-0000-124-050-0007
Pág. 3 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

# 1. Introducción

La Corporación Nacional del Cobre de Chile, CODELCO, a través de la Gerencia de Proyectos
Relaves de la Vicepresidencia de Proyectos (Codelco-VP), ha adjudicado a HATCH el servicio
de “Ingeniería Básica, Sistema de Transporte, Espesamiento y Depositación de Relaves,

Estudio Actualización de Factibilidad” del proyecto Relaves Espesados Talabre (PRET).

El proyecto se localiza en la División Chuquicamata, Región de Antofagasta, provincia de El
Loa, comuna de Calama, a 250 km al Noreste de la ciudad de Antofagasta. El tranque de
relaves Talabre recibe actualmente la totalidad de los relaves generados por las plantas
concentradoras de División Chuquicamata (DCH) y División Ministro Hales (DMH), y en un
futuro de la División Radomiro Tomic (DRT).

En la actualidad el tranque Talabre opera de manera convencional y su vida útil se ha
extendido en el tiempo mediante el peraltamiento de sus muros perimetrales y variadas obras
anexas que le permiten operar los sistemas de relave y agua del distrito norte (DN). Los
análisis realizados durante la prefactibilidad del proyecto permitieron concluir que la solución
técnico económica óptima que resuelve el manejo de los relaves del DN es implementar un
Proyecto de Relaves Espesados en Talabre posterior a la operación de la IX Etapa

convencional.

De acuerdo a los niveles productivos indicados en el PND2020 y a la capacidad de
almacenamiento de la VIII y IX etapa, durante el primer semestre del año 2027 se requiere
iniciar la operación en régimen del Proyecto Relaves Espesados Talabre (PRET) que
representa la solución a largo plazo para la disposición de los relaves del Distrito Norte de

Codelco.

El PRET se encuentra amparado por la Resolución de Calificación Ambiental del año 2016
(RCA 022/2016) en la cual se aprobó la depositación de relaves espesados en Talabre y

variadas obras anexas.

# 2. Objetivos

El objetivo del Plan de Operación Normal es proporcionar la información esencial de las
instalaciones asociadas al sistema de recuperación de agua de la PEAD, sus principales
particularidades y los aspectos técnicos que rigen la operación normal de éstas.

# 3. Alcances

El alcance del Plan de Operación Normal considera obras específicas del sistema de
recuperación de agua de la PEAD, desde los espesadores hasta las piscinas de agua
recuperada, incluyendo lo siguiente:

H362274-0000-124-050-0007
Pág. 4 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

 - Descripción del funcionamiento de las obras del sistema de agua recuperada.

 - Filosofía de control de las instalaciones.

 - Filosofía de operación de las instalaciones.

 - Resolución de problemas operacionales.

# 4. Límite de Batería

El límite de batería corresponde a las instalaciones asociadas al sistema de recuperación de
agua de la PEAD, incluidas las siguientes:

 - Canaletas colectoras de CHMH y RT(3765-CNL-1001/2001)

 - Cajón Disipador CHMH-RT (3765-CAJ-0001)

 - Canaleta de Agua Recuperada CHMH-RT (3765-CNL-0001)

 - Cajón Distribuidor de Agua Recuperada (3765-CAJ-0002)

# 5. Referencias

Ref. 1: Filosofía de Control, N°4400241113-5940-INFAT-00001.

Ref. 2: Filosofía de Operación Global, N° 4400241113-0000-INFPR-00010.

Ref. 3: Manual de Operaciones en Régimen, N° 4400241113-0000-MNLPR-00001.

Ref. 4: Criterio de Diseño de Procesos, N°4400241113-0000-CRTPR-00002.

Ref. 5: Diagrama de Flujo Agua Recuperada PEAD, N° 4400241113-0000-202PR-00006.

Ref. 6: Descripción Sistema de Control y Monitoreo Agua Recuperada, N° 4400241113-0000
INFSU-00040.

Ref. 7: Planes de Inspección de Seguridad (Regular y Extraordinaria) - Conducción de Agua
Recuperada, N° 4400241113-0000-PLNSU-00007.

Ref. 8: Memoria de Cálculo Sistema Gravitacional de Recuperación de Agua desde
Espesadores, N° 4400241113-3765-MDCCA-00001.

# 6. Descripción General del Proceso

El PRET considera la implementación de 2 módulos o bloques de procesamiento, uno para
los relaves provenientes desde Chuquicamata (CH) y Ministro Hales (MH) existentes y otro
para Radomiro Tomic (RT), Proyecto Sulfuros RT II futuro.

El relave convencional proveniente de CH y MH, es transportado de forma gravitacional
mediante cañerías presurizadas hasta la estación de bombeo de relaves (EBR), desde donde

H362274-0000-124-050-0007
Pág. 5 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

la pulpa se impulsa hacia el cajón repartidor ubicado en la planta de espesamiento de alta
densidad (PEAD).

Por su parte, los relaves convencionales provenientes de RT, se recepcionan en el cajón RT
y se transportan de forma gravitacional y presurizada, hasta el cajón repartidor de relaves

ubicado en la PEAD.

Los relaves de CH-MH y RT recibidos en los cajones de la PEAD, se reparten de manera
independiente hacia 5 distribuidores presurizados (3 para CH-MH y 2 para RT), que alimentan
de forma individual los módulos de espesadores de alta densidad de la PEAD (3 submódulos
para CH-MH, compuestos por 3-2-2 espesadores de alta densidad y 2 submódulos para RT,
compuestos por 3 espesadores cada uno).

El proceso de espesamiento, permite obtener relave espesado con una concentración de
sólidos del orden del 65%, el cual posteriormente es impulsado mediante trenes de bombas
de desplazamiento positivo (BDP), hasta su disposición final en el Tranque Talabre.

El agua recuperada desde los espesadores, es conducida por canaletas colectoras
independientes para CH-MH y RT hasta un dropbox, que permite disipar la energía del flujo y
conducirlo mediante una canaleta hasta el distribuidor de las piscinas de agua recuperada, las
cuales, acumulan el agua para su utilización al interior de la planta y retorno a las divisiones
CH-MH (Estación PS2) y RT (Sentina RT).

En la Figura 6-1 se presenta un esquema simplificado del PRET.

H362274-0000-124-050-0007
Pág. 6 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P
03-09-2021

**Figura 6-1: Esquema Simplificado Proyecto de Relaves Espesados Talabre**

H362274-0000-124-050-0007

Pág. 7 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

# 7. Filosofía de Operación en Condiciones Normales

El agua recuperada de la PEAD proviene directamente del proceso de sedimentación de los
espesadores, en el cual se separa la parte sólida y líquida del relave, mediante la acción de
una solución floculante que produce la coalescencia de las partículas sólidas finas, formando
flóculos de alta velocidad de sedimentación que se separan del agua, la cual fluye a la
superficie del espesador y rebosa hacia la canaleta perimetral para ser conducida hacia las
piscinas de agua recuperada.

Las tasas de recuperación de agua están determinadas por 3 factores:

 - Tasa de procesamiento

 - Concentración de sólidos de la alimentación del espesador

 - Concentración de sólidos en la descarga del espesador

Los caudales unitarios máximo, nominal y mínimo por espesador de las divisiones CH-MH y
RT se presentan en la siguiente tabla.

**Tabla 7-1: Caudal unitario de agua recuperada por espesador**

|División|Caudal por Espesador [m3/h]|Col3|Col4|
|---|---|---|---|
|**División**|**Máximo**|**Nominal**|**Mínimo**|
|CH-MH|1.016|550|302|
|RT|926|558|360|

La recuperación de agua desde los espesadores sobre la plataforma de la PEAD se proyecta
en sistemas independientes para CH-MH y RT, utilizando canaletas de hormigón dispuestas
a nivel de la plataforma de la PEAD (3765-CNL-1001/2001). El sistema RT, comienza en los
espesadores 3762-ERV-2001 & 2003 y continua su recorrido de modo de recolectar el agua
de todos los espesadores de RT. El sistema de CH-MH comienza desde los espesadores
3762-ERV-1001 & 1003 y continua su recorrido para recolectar el agua recuperada de todos
los espesadores de CH-MH. Para las descargas que van desde cada espesador hacia la
canaleta colectora principal se utilizan cañerías secundarias que se proyectan de forma tal que
la descarga del flujo se materialice en el sentido del flujo principal.

Cabe señalar que las cañerías de rebose se diseñan para el caudal máximo por espesador
indicado en la Tabla 7-1 según división. Las canaletas colectoras de CH-MH y RT se diseñan
por tramo, dependiendo del número de espesadores que estén aportando agua recuperada
(ver detalle en Ref. 8) y el resto del sistema ubicado aguas abajo de estas canaletas, se diseña
para el caudal máximo por módulo de espesadores de cada división, es decir, 7.112 [m [3] /h]
para los 7 espesadores de CH-MH y 5.556 [m [3] /h] para los 6 espesadores de RT.

Luego de la descarga del último espesador de CH-MH (3762-ERV-1007), ambas canaletas
(3765-CNL-1001/2001), descargan el agua recuperada al cajón disipador (3765-CAJ-0001)

H362274-0000-124-050-0007
Pág. 8 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

proyectado. Esta obra permite disipar la energía de la caída de nivel para luego empalmar en
la canaleta de agua recuperada (3765-CNL-0001), que conduce el flujo hasta el cajón
distribuidor (3765-CAJ-0002) que alimenta las 2 piscinas de agua recuperada (3765-PSC0001/0002).

_**Cabe destacar que el sistema de agua recuperada es un sistema que es controlado de**_
_**manera indirecta por la operación de los espesadores (su descarga de fondo). No cuenta**_
_**con sistemas de válvulas ni reguladores de flujo.**_

Las piscinas de agua recuperada oriente (3765-PSC-0001) y poniente (3765-PSC-0002),
conducen el agua recuperada a la sentina (5421-SEN-0001), donde operan bombas verticales
de diferente tipo para impulsar el agua recuperada hacia los respectivos puntos de consumo.
A continuación, se detalla la distribución y aplicación de las 18 bombas verticales que operan

en la sentina:

- **Bombas 5421-BVT-1001@1003:** Estas tres bombas verticales (dos operando y una

standby) impulsan agua recuperada desde la sentina hasta el estanque PS2 de
recuperación de agua de CH-MH.

- **Bombas 5421-BVT-2001@2004:** Estas cuatro bombas verticales (tres operando y una

standby) impulsan agua recuperada desde la sentina hasta la sentina RT de recuperación
de agua de RT.

- **Bombas 5421-BVT-0013/0014:** Estas dos bombas verticales impulsan agua recuperada

desde la sentina hasta los manifold de succión de todas las bombas de desplazamiento
positivo (BDP), para el lavado de las líneas de depositación. La primera de las bombas
opera de manera intermitente y la segunda en standby.

- **Bombas 5421-BVT-0001/0002/0009:** Las bombas verticales 5421-BVT-0001/0002 y 0009

(primeras dos operando y una standby), impulsan el agua recuperada desde la sentina
hasta los filtros Polisher de la PEAD, utilizados para la filtración de agua. La bomba vertical
5421-BVT-0001 alimenta el filtro N°1 para producir agua filtrada que se utilizará como agua
de sello de bombas. La bomba vertical 5421-BVT-0002 alimenta el filtro N°2 para producir
agua filtrada que se utilizará en la planta de preparación de floculante. La bomba vertical
5421-BVT-0009 opera en standby y reemplaza a cualquiera de las otras dos bombas.

- **Bombas 5421-BVT-2009/1007/0008:** Estas tres bombas verticales (dos operando y una

standby) impulsan agua recuperada desde la sentina hasta los estanques de dilución de
las plantas de floculante de CH-MH y RT.

- **Bombas 5421-BVT-0003@0005:** Estas tres bombas verticales (dos operando y una

standby) impulsan agua recuperada desde la sentina hasta el estanque de almacenamiento
de agua de lavado y flushing (5422-EST-0002).

En la Figura 7-1, se muestra un esquema del sistema de recuperación de agua de la PEAD y
en la Figura 7-2 a Figura 7-5 imágenes del modelo BIM de sus obras asociadas.

H362274-0000-124-050-0007
Pág. 9 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P
03-09-2021

**Figura 7-1: Sistema de Recuperación de Agua de PEAD, ver detalle en Ref. 5**

H362274-0000-124-050-0007

Pág. 10 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

**Figura 7-2: Modelo BIM Sistema de Recuperación de Agua en PEAD**

**Figura 7-3: Modelo BIM Canaletas y Cajón disipador de AR**

H362274-0000-124-050-0007
Pág. 11 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

**Figura 7-4: Modelo BIM Cajón Distribuidor y Piscinas de AR**

**Figura 7-5: Modelo BIM Sentina de AR**

# 8. Filosofía de Control

**8.1** **Arquitectura Sistema de Control**

La arquitectura del sistema de control está basada en la utilización de controladores de lógica
programables PLC con procesador redundante, distribuidos en las salas eléctricas del

proyecto.

H362274-0000-124-050-0007
Pág. 12 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

Todos estos equipos están comunicados mediante enlace redundante de red a los equipos de
acceso del sistema de control, y luego estos últimos conectados a la red RISC en alta
disponibilidad y calidad de servicio. Toda la comunicación entre los equipos es realizada
mediante fibra óptica.

Cada uno de los controladores posee tres tipos de comunicaciones y/o protocolos de
funcionamiento utilizando Profibus DP y Foundation Fieldbus para la lectura de instrumentos,
equipos y válvulas y red Ethernet IP para la lectura de equipos en terreno incluidos en su

funcionamiento.

Para la comunicación con las salas, se utilizará el protocolo definido por el proveedor,
soportado sobre Ethernet TCP/IP para comunicar los DCS con los servidores dispuestos en

las salas de datos.

Mediante los servidores y las estaciones de operación dispuestas en la sala de control, se
realizará todo el control del proyecto basado en un alto nivel de automatización en el
funcionamiento del proyecto. El sistema funcionará como una estación de visualización
mientras se mantenga el enlace de comunicación y como una estación de operación al
momento de perder el enlace de comunicación.

El proyecto ha considerado utilizar el Sistema de Control basado en PLC incorporando todas
las señales de instrumentos, válvulas y equipos.

Las señales de los instrumentos serán agrupadas en segmentos de Foundation Fieldbus que
serán conectados a los gabinetes de control. Las señales de las válvulas con actuador
hidráulico serán alambradas a la unidad hidráulica correspondiente.

Las señales de las válvulas con actuador neumático y actuador eléctrico serán alambradas a
los rack remotos de entradas y salidas.

Para el intercambio de señales con los equipos eléctricos de protección, comandos y medidas
ubicados en los Centros de Control de Motores (CCM) y variadores de frecuencia (VDF) se
utilizarán buses de campo con protocolo Profibus DP. Estas señales serán llevadas al sistema
de control mediante segmentos de red Profibus DP.

Cabe señalar que si bien, el sistema de recuperación de agua desde los espesadores hasta
las piscinas no cuenta con instrumentación, el control general se realiza mediante el inventario
de agua recuperada en las piscinas, para lo cual se cuenta con sensores de nivel y otros
instrumentos detallados en el informe de Descripción del Sistema de Control y Monitoreo de
Agua Recuperada, Ref. 6.

Por su parte, las conducciones de agua recuperada (cañerías, canaletas y cajones) están
dimensionadas para cumplir con todo el rango de operación más un factor de seguridad en
caso que estos sean sobrepasados.

H362274-0000-124-050-0007
Pág. 13 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

Como control, deberá considerarse además lo establecido en los Planes de Inspección de
Seguridad (Regular y Extraordinaria) de la Conducción de Agua Recuperada, Ref. 7.

**8.2** **Simbología en Instrumentación y Control**

En los planos N°4400241113-0000-201CA-00004 “Simbología y Nomenclatura
Instrumentación. Diagrama de Cañerías e Instrumentación” y N°4400241113-0000-201CA00005 “Tipos de Control de Motores y Control de Válvulas. Diagrama de Cañerías e
Instrumentación”, se presenta la simbología del sistema de instrumentación y control.

**8.3** **Centro de Supervisión y Operación**

El Sistema de Control de la planta será diseñado para permitir un proceso constante de
espesamiento mediante el ajuste entre el relave convencional alimentado a los espesadores
y el relave espesado que descarga y las operaciones aguas abajo de los espesadores.

La información de proceso será almacenada en archivos del Sistema de Control para
proporcionar los antecedentes necesarios para la presentación de informes y administración
de la planta.

El Sistema de Control será equipado con un sistema de administración de alarma para
proporcionar una notificación eficiente a los operadores. El sistema de administración de
alarma será capaz de priorizar las alarmas del proceso a través del Sistema de Control.

El control será principalmente remoto. El control local será sólo para mantenimiento y se
proporcionarán botoneras de prueba y paradas de emergencia cerca de cada motor. El
operador de la sala de control habilitará la operación local de las botoneras de prueba, las
paradas de emergencia estarán siempre habilitadas.

La supervisión y operación de los equipos de la planta se realizará desde la Sala de Control
ubicada en la PEAD y se implementarán en las estaciones de operación (EOP) proyectadas
todos los despliegues gráficos, tendencias, páginas de alarmas y despliegues de eventos que
serán la interfaz usuario entre el sistema de control y el operador. La información requerida
como flujos, presión, niveles, pH, alarmas, entre otros, será proporcionada a cada operador
de la Sala de Control para permitir una operación eficiente y segura en las instalaciones.

La operación normal de las diferentes unidades de proceso y equipos se realizará en el
Sistema de Control y será supervisadas por el operador desde las estaciones de operación
ubicadas en el Sala de Control. Las pantallas gráficas interactivas serán la interfaz usuario
entre el operador y los equipos de terreno mostrando todas las unidades de proceso: cajones
de distribución, cajones de traspaso, estanques, espesadores e instrumentación de terreno.
Las pantallas gráficas serán una fiel representación de los diagramas de proceso e
instrumentación (P&ID).

H362274-0000-124-050-0007
Pág. 14 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

En puntos estratégicos de la PEAD, se utilizará un circuito cerrado de televisión (CCTV) con

cámaras de video. Estas cámaras a través de un servidor de video se conectarán a las

estaciones de operación existentes y se utilizarán como apoyo a la operación de los diferentes

procesos productivos de la planta.

La operación local de los equipos se realizará exclusivamente para tareas de mantenimiento.
Los equipos proyectados consideran el suministro de un panel de control local.

**8.4** **Modos de Operación**

En el control lógico o digital existe una diversidad de soluciones, pero se adopta dejar los
estándares de Codelco que tiene selectores de acuerdo al estado de operación de los equipos,
el lugar de donde se opera y la participación del operador. Estos selectores son de software
pudiendo existir en algunos casos dualidad porque algunos equipos traen sus propios
selectores. En este caso la mayor jerarquía la tendrá siempre el operador del centro de
operaciones. La combinación de estos selectores define diferentes modos de control.

Para la operación, el control de equipos y motores del proyecto se han definido tres tipos de
selectores configurados en el sistema de control central que están asociados a los modos de
operación de los equipos y una estación de control local ubicada al lado del equipo en terreno
que tendrá una botonera de Parada de Emergencia y botoneras “Partir / Parar” para operación
local del equipo en terreno.

**8.5** **Mantenimiento**

El Sistema de Control debe ser fácil de mantener por el personal de instrumentación, se
utilizarán equipos y tecnologías probadas. En el diseño deberán ser considerados accesos y
ergonomía para las reparaciones.

El Sistema de Control no deberá ser interrumpido por una falla en el suministro de electricidad
por lo que todos los equipos requeridos para soportar su operación serán alimentados
eléctricamente desde un sistema de alimentación ininterrumpido (UPS). Las UPS tendrán

respaldo desde la planta principal o desde una planta de emergencia.

# 9. Procedimiento de Detención

El sistema de recuperación de agua de la PEAD depende del funcionamiento de los
espesadores de alta densidad, por lo que si los espesadores dejan de recibir carga,
automáticamente se detiene el flujo de agua recuperada.

La operación deberá en ese momento gestionar el inventario de agua de las piscinas para los
consumos internos de la planta.

H362274-0000-124-050-0007
Pág. 15 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

**9.1** **Descripción General**

Las detenciones de emergencias pueden ocurrir por diversas causas. El operador de la sala
de control y los operadores de terreno deben determinar las causas y las acciones necesarias
para enfrentar la emergencia e iniciar la secuencia de partida para restablecer la operación de

los sistemas.

Las principales causas que pueden producir una detención de emergencia son las siguientes:

 - Blackout

 - Protección de equipos

 - Situaciones accidentales

**9.2** **Blackout**

En caso de una caída en la alimentación de energía, los espesadores dejarán de recibir
relaves, por lo cual se detiene el flujo de agua recuperada, quedando este sistema sin

funcionamiento.

Se debe tener en consideración que los volúmenes de agua en el sistema (piscinas), deberán
permitir respaldar los siguientes equipos:

 - Red de incendio junto con su bomba de alimentación.

 - Bombas shear thinning.

 - Bombas de sentina para alimentar estanque de lavado y flushing

 - Bomba desde estanque de lavado y flushing

 - Bomba de sentina para el lavado de líneas entre BDP y depósito.

 - Bombas de agua de flushing de PEAD/CH-MH.

En caso de que el sistema de respaldo eléctrico no se encuentre disponible, los espesadores
pueden vaciarse a través de las cañerías de drenaje hacia la canaleta de emergencia. No se
requiere del vaciado total del espesador, ya que se puede vaciar solamente la pulpa que se
encuentre en su interior, dejando el agua remanente en el equipo. Esto evitará perder el agua
en el tranque y ahorrará tiempo para la posterior puesta en servicio de los espesadores.

**9.3** **Protección de equipos**

Los equipos principales se encuentran provistos de instrumentación para detectar condiciones
anormales de operación y detener el funcionamiento del equipo en caso de detectarse alguna

falla.

H362274-0000-124-050-0007
Pág. 16 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

En la Tabla 9-1 se indican las alarmas y causa típicas de detención para el caso de motores

eléctricos.

**Tabla 9-1: Alarmas y Causas Típicas de Detención Motores Eléctricos**

|Alarma|Causa|
|---|---|
|Sobrecarga de motor|Fallas en las protecciones eléctricas o problemas de<br>comunicación|
|Temperatura excesiva motor|Temperatura excesiva motor|
|Falla variador de frecuencia|Falla real o problemas de comunicación|

**9.4** **Situaciones Accidentales**

Estas situaciones se describen en el “Plan de Preparación y Respuesta ante Emergencias Sistema de Agua Recuperada PEAD” (4400241113-0000-PLNSU-00010).

# 10. Resolución de Problemas Operacionales

A continuación se describen los principales problemas operacionales que pueden presentarse
en la PEAD y afectar la operación normal del sistema de recuperación de agua, junto a las
acciones que deben efectuarse para su resolución.

Cabe destacar que mientras el proceso de espesamiento se encuentre detenido por problemas
operacionales no se recuperará agua.

**10.1** **Problemas Operacionales en la PEAD que afectan el agua recuperada**

_**10.1.1**_ _**Falla Bombas Principales de Alimentación Distribuidor Presurizado**_

Si alguna de las bombas de alimentación a los distribuidores falla es posible realizar el cambio
de bomba poniendo en servicio la bomba stand-by provista. Para esto se debe seguir la

siguiente secuencia:

1. Abrir válvulas de alimentación a ramal de bomba stand-by desde el cajón repartidor de

relaves y abrir válvula de descarga de bomba stand-by.

2. Detener en caso de que no se haya detenido la bomba que quedará fuera de servicio.

Cerrar válvulas de succión y descarga.

3. Dar partida a bomba stand-by y monitorear presiones en las líneas de alimentación a

espesadores y el flujómetro de alimentación a distribuidor presurizado.

4. Drenar y lavar tramos de cañerías detenidos.

H362274-0000-124-050-0007
Pág. 17 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

_**10.1.2**_ _**Falla en Distribuidor Presurizado**_

Una falla en un distribuidor presurizado implica la detención del bombeo de una línea de
transporte de relave convencional. Con esto, tres espesadores de relave quedan fuera de

servicio.

Al detener la operación de las líneas de transporte se debe efectuar el drenaje de la cañería
correspondiente. Los espesadores pueden quedar en modo de recirculación a través de la
bomba shear thinning mientras se efectúa la reparación o el cambio de distribuidor.

_**10.1.3**_ _**Espesadores Fuera de Servicio**_

Si debido a problemas operacionales o mantenciones programadas es necesario dejar un
espesador fuera de servicio, el diseño considera que los otros dos (o tres) espesadores del
módulo absorben el flujo del espesador detenido. En el caso que dos espesadores del mismo
módulo se encuentren fuera de servicio, es necesario disminuir el flujo de relaves
convencionales aguas arriba y detener el grupo completo.

_**10.1.4**_ _**Falla en Bomba Principal de Relaves Espesado de Descarga**_

En caso de producirse una falla en la bombas principal de descarga de relave espesado, es
necesario emplear la bomba en standby. Esto se puede realizar mediante la siguiente

secuencia:

1. Detener bomba principal, si no se encuentra detenida.

2. Cerrar válvulas de succión y de descarga de la bomba principal.

3. Cerrar válvula de ramal de la bomba de cizalle y válvula de recirculación a feedwell.

4. Abrir válvulas de succión y descarga de bomba de reserva.

5. Dar partida a la bomba de reserva.

6. Activar lazos de control sobre la bomba reserva.

7. Realizar flushing de cañerías de la bomba principal.

_**10.1.5**_ _**Falla en Bomba de Cizalle**_

La bomba de cizalle es un equipo de emergencia o respaldo, por lo cual la falla no es crítica.
En caso de que la reología sea muy alta y la bomba este en falla, se debe aumentar el flujo de
descarga por sobre el equilibrio masico a fin de producir la disminución de altura de cama y
con esto bajar la concentración de sólidos y en consecuencia la reología.

**10.2** **Problemas Operacionales en Espesadores de Alta Densidad**

A continuación se entregan recomendaciones generales para los problemas más comunes
que se pueden presentar durante la operación de los espesadores y que pueden afectar el
proceso de recuperación de agua en la PEAD. Las acciones exactas a ejecutar por el operador

H362274-0000-124-050-0007
Pág. 18 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

dependen de la evaluación de las condiciones y del análisis de los parámetros de operación

una vez iniciado su funcionamiento.

_**10.2.1**_ _**Torque Excesivo del Espesador**_

Un aumento del torque del espesador se debe al aumento en la resistencia que ejerce el relave
al movimiento de las rastras. Las causas pueden ser variaciones en granulometría,
mineralogía que afecten la reología del relave, excesiva altura de la cama de sólidos y/o

dosificación de floculante excesiva.

_Bomba de cizalle_

Como medida inicial se deben revisar las mediciones de tensión de fluencia. Si esta es superior
al diseño, se debe poner en funcionamiento la bomba de shear thinning del espesador y seguir
controlando tensión de fluencia y torque. La recirculación a través de la bomba ayudará a
disminuir la tensión de fluencia del relave y disminución del torque.

_Dosificación de floculante_

Como segunda opción se debe verificar la dosificación de floculante porque una dosificación
excesiva puede aumentar la tensión de fluencia del relave aumentando el torque. Verificar
lazos de control de dosificación y la concentración de preparación de la solución madre de
floculante. Se puede verificar la adición de floculante tomando una muestra desde el feedwell
del espesador para observar la estructura y el tamaño de los flóculos de relave. Un tamaño

excesivo se debe a sobrefloculación del relave.

_Altura de cama de sólidos_

Es posible disminuir la altura de la cama de sólidos descargando el espesador a una tasa
mayor que la tasa de alimentación. Esto hará que el torque descienda y a su vez puede
descender la concentración de sólidos de descarga debido al menor tiempo de residencia del
relave al interior del espesador. Si este es el caso, se debe encontrar el equilibrio para
mantener los parámetros de descarga del relave dentro del diseño.

_Cambios de mineralogía y/o granulometría_

En caso de cambios drásticos y permanentes en la mineralogía o granulometría del relave, se
debe evaluar el cambio en la dosificación o tipo de floculante mediante la realización de
pruebas de sedimentación con distintos proveedores.

_**10.2.2**_ _**Baja Concentración de Sólidos en Relaves Espesados**_

La disminución en la concentración de sólidos de los relaves espesados puede deberse a
tiempo insuficiente de residencia de la pulpa en el espesador o una baja dosificación de

floculante.

H362274-0000-124-050-0007
Pág. 19 de 20

Informe Técnico

Contrato N°4400241113
General **-** Plan de Operación Normal - Agua Recuperada PEAD

4400241113-0000-PNLSU-00009, Rev. P

03-09-2021

_Tiempo de residencia_

El tiempo de residencia de la pulpa en el espesador se incrementa aumentando la altura del
inventario de sólidos en el equipo. Para esto, se debe disminuir la tasa de descarga del
espesador por debajo de la tasa de alimentación. El aumento del tiempo de residencia
aumenta la concentración de sólidos de descarga.

_Dosificación de floculante_

Verificar lazos de control de dosificación y la concentración de preparación de la solución
madre de floculante. Se puede verificar la adición de floculante tomando una muestra desde
el feedwell del espesador para observar la estructura y el tamaño de los flóculos de relave.
Flóculos de tamaño pequeño con una baja velocidad de sedimentación indicaría una baja

adición de floculante.

_**10.2.3**_ _**Aumento de Turbidez Agua Recuperada**_

La turbidez se produce cuando parte de las partículas del relave permanecen en suspensión
siendo arrastradas hacia el rebose del agua recuperada. Siempre se produce este fenómeno
en menor medida, pero se puede incrementar afectando gravemente la calidad de agua
recuperada debido a dos situaciones: floculación deficiente y/o altura de cama de sólidos

excesiva.

_Floculación deficiente_

Como se indicó anteriormente, una dosificación de floculante inferior al óptimo puede provocar
en una floculación deficiente. Por esto, es recomendable verificar la adición de floculante

tomando una muestra desde el feedwell del espesador para observar la estructura y el tamaño
de los flóculos de relave. Flóculos de tamaño pequeño con una baja velocidad de
sedimentación indican una baja adición de floculante.

_Altura de cama de sólidos excesiva_

Una altura excesiva de la cama de sólidos puede provocar que quede poco espacio entre el
feedwell del espesador y el lecho de sólidos para que las partículas tengan el tiempo suficiente
para sedimentar. Esto provoca que las partículas sean arrastradas hacia el rebose del
espesador y se debe disminuir la altura de la cama de sólidos mediante un aumento en la tasa
de descarga del espesador por sobre la tasa de alimentación.

H362274-0000-124-050-0007
Pág. 20 de 20