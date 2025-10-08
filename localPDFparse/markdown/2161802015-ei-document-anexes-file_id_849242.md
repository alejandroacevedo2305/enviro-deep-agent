---
title: PROCEDIMIENTO xxxxxxxxxxxxx
author: Octubre 2013;Gabriel Leal N.
date: D:20240410095036-04'00'
language: es
type: manual
pages: 43
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - CONTENIDO
  - 1. DESCRIPCIÓN BREVE DEL PROYECTO
  - 2. ALCANCE DEL DOCUMENTO
  - 3. DOCUMENTOS APLICABLES AL PROYECTO
  - 4. CONDICIONES Y CRITERIOS DE DISEÑO
  - 5. CONDICIONES Y CRITERIOS DE DISEÑO
  - 6. PREDISEÑO DEL SISTEMA DE ELECTRICIDAD
-->

|DATA CENTER ST-5 CHILE<br>MEMORIA DESCRIPTIVA SISTEMA DE ELECTRICIDAD<br>PARA DECLARACION IMPACTO AMBIENTAL|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|**C **|**01-04-2024**|**Revisada**|**Revisada**|**H.C**|**H.R.**|||||
|**B **|**15-01-2024**|**Revisada**|**Revisada**|**H.C**|**H.R.**|||||
|**A **|**14-01-2024**|**Emisión Original**|**Emisión Original**|**H.C**|**H.R**|||||
|**REV N° **|**FECHA **|**EMITIDO PARA **|**EMITIDO PARA **|**PREP **|**REV **|||||
|**REV N° **|**FECHA **|**EMITIDO PARA **|**EMITIDO PARA **|**PREP **|**REV **|||**APROBADO POR **|**APROBADO POR **|
|**N° DOCUMENTO CLIENTE**|**N° DOCUMENTO CLIENTE**|||||||**Rev. C**|**Rev. C**|
|**N° DOCUMENTO CLK**|**N° DOCUMENTO CLK**|**ST5-DIA-DOC-ELE-01_B**|**ST5-DIA-DOC-ELE-01_B**|**ST5-DIA-DOC-ELE-01_B**|**ST5-DIA-DOC-ELE-01_B**|**ST5-DIA-DOC-ELE-01_B**|**ST5-DIA-DOC-ELE-01_B**|**ST5-DIA-DOC-ELE-01_B**|**ST5-DIA-DOC-ELE-01_B**|
|||||||||||

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

|APROBACIONES|Col2|Col3|Col4|
|---|---|---|---|
|**CARLOS LEIVA Y COMPAÑÍA LTDA**|**CARLOS LEIVA Y COMPAÑÍA LTDA**|**FIRMAS**|**FECHA**|
|**PREPARADO POR**|Héctor Calderón||**12-01-2024**|
|**REVISADO POR**|Héctor Rosas||**15-01-2024**|
|**APROBADO POR**|Claudio Moreno||**15-01-2024**|

|DIVISIÓN DE PROYECTOS|Col2|FIRMAS|FECHA|
|---|---|---|---|
|**APROBADO POR**||||

**MDC ELECTRICIDAD ST-5-001-RC** **Página 2 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

# CONTENIDO

**Rev. C**

**Fecha: 14-01-2024**

**CONTENIDO ........................................................................................................................... 3**

**1.** **DESCRIPCIÓN BREVE DEL PROYECTO ....................................................................... 5**

**2.** **ALCANCE DEL DOCUMENTO ...................................................................................... 6**

**3.** **DOCUMENTOS APLICABLES AL PROYECTO .............................................................. 6**

**4.** **CONDICIONES Y CRITERIOS DE DISEÑO ................................................................... 7**

4.1. Fórmulas utilizadas ...................................................................................................................... 7

4.1.1. Potencias: ........................................................................................................................................ 7

4.1.2. Potencias de cortocircuito: ....................................................................................................... 8

4.1.3. Energía Témica: ............................................................................................................................. 8

4.1.4. CaÍda de tensión: .......................................................................................................................... 8

4.1.5. Corrección de resistencia por temperatura del cable: ................................................... 9

**5.** **CONDICIONES Y CRITERIOS DE DISEÑO ................................................................. 10**

5.1. OBJETIVO....................................................................................................................................... 10

5.2. SUMINISTRO DE ENERGÍA ...................................................................................................... 10

5.3. EDIFICIO DATA CENTER ST5 .................................................................................................. 12

**6.** **PREDISEÑO DEL SISTEMA DE ELECTRICIDAD ......................................................... 12**

6.1. GENERALIDADES ........................................................................................................................ 12

6.2. ACOMETIDA ................................................................................................................................. 12

6.3. SALAS ELECTRICAS MT (SS/EE) ............................................................................................. 14

6.3.1. SALA ELECTRICA MT UTILITY ................................................................................................. 14

6.3.2. SALAS ELECTRICAS INTERIORES DATA BLOQUES DE ENERGÍA ............................... 15

6.3.3. DATA SHEET CELDAS MT ........................................................................................................ 16

6.3.4. LISTADO CELDAS MT ................................................................................................................ 18

6.4. CONDUCTORES MEDIA TENSIÓN ....................................................................................... 21

6.5. POTENCIA SISTEMA ELÉCTRICO ........................................................................................... 23

6.6. SUBESTACIÓN DE TRANSFORMACIÓN POR BLOQUE DE ENERGÍA ...................... 23

6.7. CÁLCULO DE LAS PROTECCIONES EN MT Y BT ............................................................ 24

**MDC ELECTRICIDAD ST-5-001-RC** **Página 3 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

6.7.1. LADO MT ....................................................................................................................................... 24

6.7.2. LADO BT ........................................................................................................................................ 25

6.8. LISTADO DE TRANSFORMADORES ..................................................................................... 27

6.9. SISTEMA DE RESPALDO ........................................................................................................... 27

6.9.1. CARACTERISTICAS GENERALES. ........................................................................................... 28

6.9.2. MÓDULO DE CONTROL .......................................................................................................... 29

6.9.3. LISTADO DE GRUPOS GENERADORES ............................................................................... 30

6.10. SISTEMA UPS ............................................................................................................................... 30

6.10.1. LISTADO DE UPS ............................................................................................................. 32

6.11. TABLEROS Y PANELES SISTEMAS ELÉCTRICOS ............................................................... 33

6.11.1. Referencia Técnicas. Normativas .............................................................................. 34

6.11.2. Características Mecánicas y de Construcción ...................................................... 35

6.11.3. Cableado Interno ............................................................................................................ 36

6.11.4. Selectividad ...................................................................................................................... 36

6.11.5. Instrumentos de Medición, Señalización .............................................................. 37

6.11.6. Aparellaje ........................................................................................................................... 37

6.11.7. Rotulación Tableros ....................................................................................................... 38

6.11.8. LISTADO DE TABLEROS GENERALES ....................................................................... 39

**MDC ELECTRICIDAD ST-5-001-RC** **Página 4 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

# 1. DESCRIPCIÓN BREVE DEL PROYECTO

**Rev. C**

**Fecha: 14-01-2024**

El presente documento cubre la preingeniería conceptual de la especialidad de electricidad,

para el nuevo Data Center ST-5. El Diseño e Implementación de las soluciones prediseñadas

están basadas en los modelos y criterios de diseño de MK2 y reglas de Ingeniería asociada

a las Instalaciones de Data Center. La preingeniería se orienta a definir los criterios de diseño

y capacidades de potencia de la instalación eléctrica para someter a aprobación la

Declaración de Impacto ambiental El proyecto “DATA CENTERST-5”, en adelante e

indistintamente “el Proyecto”, corresponde a un nuevo Data Center, en el marco de una

instalación definida como de infraestructura de alta tecnología de información, donde el

objetivo principal es proveer de servicios y aplicaciones de internet a diversos clientes. El DC

ST5 estará localizado en la comuna de Pudahuel, Santiago, Región Metropolitana.

El proyecto denominado “Data Center ST5” contempla una superficie útil construida total de

24.4118,27 m2 sobre una superficie de terreno bruta de 42.408,85 m2. Este estará compuesto

de 4 Megachip y un módulo de oficinas (FOH y BOH). Se contará con un total de 16 grupos

electrógenos de emergencia de 3.500 kVA y un grupo electrógeno de 900 KVA para las

oficinas, todos contarán con tanque (subbase) de almacenamiento de petróleo para

autonomía de 30 y 8 horas a plena carga, respectivamente, 16 salas de datos, 26 equipos de

aire acondicionado Chillers (más 2 equipos de reserva) 128 CRAY (más equipos 32 de

reserva), 16 unidades de ventiladores modelo CRAH (más 16 equipos de reserva), 4

inyectadores de aire tipo MAU, un estanque de control de incendios y caseta de guardia.

El edificio de oficinas de 2 niveles considera sala de reuniones, salas de descanso, casilleros,

bodegas de almacenamientos para útiles de aseo y artículos de oficina.

Se proyecta un total de 110 estacionamientos vehiculares (4 unidades para personas con

situación de movilidad reducida), 5 estacionamientos de 30 m2 para camiones y 54

estacionamientos de bicicletas.

El Proyecto se construirá en 4 etapas, contemplando un total de almacenamiento de

petróleo de 337.500 L/286.875 kg (100% full, 17 equipos generadores).

La vida útil del Proyecto se estima de un total de 25 años aproximadamente. Sin perjuicio

de lo anterior, se indica que el edificio data center podría seguir operando, para lo cual se

solicitarán todas las autorizaciones que correspondan.

**MDC ELECTRICIDAD ST-5-001-RC** **Página 5 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

# 2. ALCANCE DEL DOCUMENTO

**Rev. C**

**Fecha: 14-01-2024**

Establecer los criterios de diseño y capacidades de potencia del sistema de electricidad del

Edificio Data Center ST-5, el que deberá ser dimensionado a lo estipulado en las guías de

diseño MK2 y de la normativa chilena vigente

# 3. DOCUMENTOS APLICABLES AL PROYECTO

Las siguientes normas forman parte del proyecto. Salvo que se haga referencia a una edición

concreta, será de aplicación la edición en vigencia. Serán también de aplicación los

documentos referenciados por cada uno de los siguientes Normas Internacionales:

Para el desarrollo de los cálculos justificativos, que respaldan esta memoria descriptiva se

utilizarán la siguientes normativas

Artículo 12 del Decreto Supremo DS 8/2019 que aprueba reglamento de seguridad de las

instalaciones de consumo de energía

 DS No327. Ley General de Servicios Eléctricos, en Servicios Eléctricos.

 Pliego Técnico Normativo RIC No 01 “Empalmes”

 Pliego Técnico Normativo RIC No 02 “Tableros Eléctricos”

 Pliego Técnico Normativo RIC No 03 “Alimentadores y Demanda de una instalación”

 Pliego Técnico Normativo RIC No 04 “Conductores, materiales y sistemas de

canalización”

 Pliego Técnico Normativo RIC No 05 “Medidas de protección contra tensiones

peligrosas y descargas eléctricas”

 Pliego Técnico Normativo RIC No 06 “Puesta a tierra y enlace equipotencial”

 Pliego Técnico Normativo RIC No 07 “Instalaciones de equipos”

 Pliego Técnico Normativo RIC No 08 “Sistemas de emergencia”

 Pliego Técnico Normativo RIC No 09 “Sistemas de autogeneración”

 Pliego Técnico Normativo RIC No 10 “Instalaciones de uso general”

 Pliego Técnico Normativo RIC No 11 “Instalaciones especiales”

 Pliego Técnico Normativo RIC No 12 “Instalaciones en ambientes explosivos”

 Pliego Técnico Normativo RIC No 13 “Subestaciones y salas eléctricas”

 Pliego Técnico Normativo RIC No 14 “Exigencias de eficiencia energética para

edificios”

**MDC ELECTRICIDAD ST-5-001-RC** **Página 6 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

 Pliego Técnico Normativo RIC No 15 “Infraestructura para la recarga de vehículos

eléctricos”

 Pliego Técnico Normativo RIC No 16 “Subsistemas de distribución”

 Pliego Técnico Normativo RIC No 17 “Operación y mantenimiento”

 Pliego Técnico Normativo RIC No 18 “Presentación de proyectos”

 Pliego Técnico Normativo RIC No 19 “Puesta en servicio”

 - Normas NFPA (National Fire Protection Association) relativas a materiales

 - eléctricos).

 - Guías de diseño MK2.

# 4. CONDICIONES Y CRITERIOS DE DISEÑO

## 4.1. Fórmulas utilizadas

**4.1.1.** **Potencias:**

**Sistema Monofásico**

P= VIcos∅

**Sistema Trifásico**

P= ~~√~~ 3VIcos∅

Donde:

p: Potencia

I: Corriente

V: Tensión

Cos  factor de Potencia

**MDC ELECTRICIDAD ST-5-001-RC** **Página 7 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**4.1.2.** **Potencias de cortocircuito:**

S cc3f = ~~√~~ 3V ll I cc3f

Donde:

Scc3f: Potencia de Cortocircuito trifásica [MVA]

Icc3f: Corriente de cortocircuito trifásica [KA]

VLL: Tensión entre fases [KV]

**4.1.3.** **Energía Témica:**

K [2] S [2] ≥I [2] t [A [2] ]

Donde:

**Rev. C**

**Fecha: 14-01-2024**

K: Constante K del cable según su aislación 95 para aislación XLPE o EPR 115 para PVC

S: Sección del cable

I: Corriente de cortocircuito

t: tiempo de duración de la corriente de falla

**4.1.4.** **CaÍda de tensión:**

Para líneas trifásicas de sección mayores a 70 mm [2]

V p = ~~√~~ 3LI L (Rcosφ+ Xsenφ) [V]

Donde:

Vp: Caída de tensión en [V]

L: Largo en [Km]

IL: Corriente de línea en [A]

R: Resistencia del alimentador en [Ω/Km ]

X: Reactancia del alimentador en [Ω/Km ]

cosφ : Factor de Potencia

**MDC ELECTRICIDAD ST-5-001-RC** **Página 8 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

Para líneas menores a 70 mm [2] y distribución trifásica

V p = ~~[√]~~ [3LI] [L] S∂ [(cosφ)] [V]

Donde:

Vp: Caída de tensión en [V]

L: Largo en [m]

IL: Corriente de línea en [A]

S: Sección del conductor en mm2

: Conductividad eléctrica para el cobre de 56 [m/Ωmm [2] ]

cosφ : Factor de Potencia

Para líneas menores a 70 mm2 y distribución monofásica

V p = [2LI] [L] S∂ [(cosφ)] [V]

Donde:

Vp: Caída de tensión en [V]

L: Largo en [m]

IL: Corriente de Línea en [A]

S: Sección del conductor en mm2

: Conductividad eléctrica para el cobre de 56 [m/Ωmm [2] ]

cosφ : Factor de Potencia

**4.1.5.** **Corrección de resistencia por temperatura del cable:**

La temperatura de operación está dada por:

**Rev. C**

**Fecha: 14-01-2024**

T op = T 0 + (T MAX −T 0 ) × (I [I] C

T op = T 0 + (T MAX −T 0 ) × (I [I]

~~)~~

2

[oC]

Donde:

Top: Temperatura de operación en [oC]

T0: Temperatura ambiente del conductor según tabla en [oC]

TMAX: Temperatura máxima del cable en [oC]

I: Corriente provista para el conductor en [A]

IC: Corriente Máxima admisible para el cable según tipo de aislación en [A]

**MDC ELECTRICIDAD ST-5-001-RC** **Página 9 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

La resistencia a diferente temperatura de operación:

R op = R 0 [1+∝(T op −T 0 )] [Ω]

Donde:

Rop: Resistencia del conductor a la Temperatura de operación en [oC]

R0: Resistencia del conductor a la Temperatura ambiente en [oC]

Top: Temperatura de operación en [oC]

To: Temperatura de ambiente en [oC]

: Coeficiente térmico a 20oC (0,00393 para el Cu)

# 5. CONDICIONES Y CRITERIOS DE DISEÑO

## 5.1. OBJETIVO

**Rev. C**

**Fecha: 14-01-2024**

El presente documento tiene como objetivo definir los requerimientos para el diseño del

Proyecto de Infraestructura Eléctrica del Data Center ST5 Las instalaciones eléctricas

consideradas en este proyecto son las siguientes:

 - Celdas de media tensión.

 Transformadores de poder.

 Grupos electrógenos (sistema de respaldo de emergencia).

 UPS (sistema de respaldo crítico).

 Tableros generales.

 - Tableros de distribución.

## 5.2. SUMINISTRO DE ENERGÍA

El suministro de energía se proyecta en Media Tensión de 23 [KV] desde las redes de la red

pública, con dos acometidas hacia las salas utility A. y utility B. Se deja proyectada una tercera

sala Utility C., para una futura acometida de respaldo

Cada utility alimenta a dos salas de distribución secundaria denominadas Room-A y Room

B. Desde estas salas se procede a alimentar los bloques de energía ubicadas al interior del

dta center. Los bloques de energía. Internos contienen las celdas de distribución y los

transformadores 23/0,4 [KV] de distribución

**MDC ELECTRICIDAD ST-5-001-RC** **Página 10 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

En condición normal de operación, la alimentación de energía se inicia en las salas utility A

y utility. B, que corresponden a las SS/EE No1, SS/EE No2 respectivamente. Desde cada SS/EE

se distribuyen dos ramales de energía hacia las salas Room-A y Room-B. que entregan

energía hacia las celdas SWUT-A y SWUT-B. Se deja espacio para una tercera sala para una

futura celda (SWUT-C) de respaldo de las acometidas principales proyectadas

De la sala Room-A y Room-B se distribuye la energía hacia los bloques de energía interiores

del data por medio de dos líneas A y B respectivamente. De aquí en adelante los sistemas

de distribución de energía eléctrica corren independientemente tanto para la carga crítica

(IT) como para los servicios auxiliares y de climatización. La compartimentación de espacios

se presenta a través de líneas de energía A y B, situados en los sectores poniente y oriente

respectivamente, las cuales nacen desde puntos independientes y recorren por zonas y salas

completamente independientes.

Luego se distribuye la energía hacia los transformadores de cada bloque de energía. El

respaldo de energía se produce mediante un anillo en media tensión. que alimenta cada

transformador desde la sala Room-A como de la Room-B

Después de transformada la energía de 23.000 a 400 Volt AC, esta recorre hacia el sistema

de conmutación automática (ATS), el cual decide en configuración automática si la energía

recibida será derivada hacia la carga desde los sistemas de generación o desde el Utility.

En configuración normal, la energía proviene desde el Utility, y la fuente de generación

eléctrica principal (red pública) se mantiene esperando la falla de red de Media Tensión,

Transformadores o líneas de distribución aguas arriba de los sistemas de conmutación (ATS).

Se considera también como falla a un corte del utility, parámetros eléctricos fuera de la

banda de operación nominal (23.000V±3%, 50Hz±0,5%). A la salida de los sistemas de

conmutación (ATS), se alimenta al Centro de Distribución de Carga (CDC), el cual energiza a

los distintos Tableros de Maniobras de UPSs, tanto para la carga crítica como para servicios

auxiliares y climatización independientemente.

Desde los Centros de distribución de carga se alimentan independientemente los Tableros

de comandos de UPS (TCU), los cuales entregan la alimentación de energía a cada módulo

de UPS. Los servicios de TI son protegidos por UPS de 1200 [KW]

**MDC ELECTRICIDAD ST-5-001-RC** **Página 11 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

## 5.3. EDIFICIO DATA CENTER ST5

**Rev. C**

**Fecha: 14-01-2024**

El complejo se compone de edificio con 5 módulos, uno de oficinas (FOH y BOH) y 4 módulos

de salas de data center (denominados MC, Megachip) y salas con instalaciones de apoyo

(electricidad, UPS, Baterías), dispuestas en dos niveles (8 salas data center). Sobre los dos

niveles de salas data center, se ubica un nivel para instalaciones electromecánicas,

denominado nivel superior y sobre este remata un nivel piso mecánico, donde se emplazarán

los enfriadores de agua (Chillers)

El edificio en su obra civil se construirá en dos etapas, la primera etapa incluye las oficinas y

bodegas (FOH y BOH, respectivamente) y los módulos MC-1 y MC-2. Junto con la

construcción se habilitarán en fase 1.1, los recintos administrativos (FOH y BOH) y,

parcialmente, el módulo MC-1, en su segundo nivel. Luego, a futuro se completará la

habilitación del módulo MC-1 (primer nivel). Posteriormente, se habilitarán el módulo MC

2, comenzando la fase 2 con sala Data center del piso 2, y finalmente la sala Data center de

piso 1. Terminada la habilitación de las fases 1 y 2, se construirá la obra civil de la segunda

etapa, que cubre los módulos MC3 y MC-4, que se habilitaran en forma progresiva en fases

3 y 4.

# 6. PREDISEÑO DEL SISTEMA DE ELECTRICIDAD

## 6.1. GENERALIDADES

Las siguientes definiciones hacen referencia a los elementos específicos y componentes de

la infraestructura del Sistema eléctrico que se desea proyectar

## 6.2. ACOMETIDA

La acometida eléctrica será ejecutada por la compañía eléctrica local. Los alimentadores MT

de la acometida serán suministrados por la Cía. Eléctrica

El proyecto considera un empalme para obtener la energía eléctrica, en el nivel 23 kV, desde

la compañía distribuidora local.

La canalización subterránea, desde la cámara exterior de distribución de cia eléctrica local

hasta el recinto de subestación SS/EE es de responsabilidad del proyecto eléctrico.

**MDC ELECTRICIDAD ST-5-001-RC** **Página 12 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

Para el tendido se proyecta utilizar banco de ductos en zanja de paredes verticales y de una

profundidad mínima de 80 cm de la superficie

Para las canalizaciones subterráneas se contempla la utilización de tubos de PVC sch 40 en

zonas de tránsito liviano y sch 80 en zonas de tránsito pesado que cumpla las normas Nch

399 e IEC 614.

En las canalizaciones subterráneas, las tuberías serán conforme a lo establecido en la norma

IEC 61386-24 y sus características mínimas serán las indicadas en la tabla No4.28 de los

“Pliegos Técnicos Normativos RIC N°04 Conductores, Materiales y Sistema de Canalización”.

Tabla 6.1 Características Normativas Ductos PVC Tendido Subterráneo

Las cámaras eléctricas se proyectan del tipo A y según norma de Cia. En referencia este

proyecto utilizará la cámara tipo 2301 o 2300 según su aplicación. Estas cámaras deberán

ser confirmadas por la Cía. Eléctrica y cumplir con lo indicado en los R.I.C. “Reglamento de

seguridad de las instalaciones de consumo de Energía Eléctrica” en el “Pliego Técnico

Normativo N° 04 “Conductores, materiales y sistemas de canalización” Punto 7.9.8.4.1

Cámaras Tipo A

Los sistemas de instalación de las canalizaciones en función de los tipos de conductores o

cables deben estar de acuerdo con la tabla No4.8, siempre y cuando las influencias externas

estén de acuerdo con las prescripciones indicadas en el presente pliego técnico.

**MDC ELECTRICIDAD ST-5-001-RC** **Página 13 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

Se proyecta. una red subterránea mediante un banco de ductos en cañerías de PVC Conduit

Schedule 40 ó 80 de 110mm de diámetro.

Tipo: Serie II de pared gruesa en tiras de 6 mts. Norma ASTM 1785 Schedule

40 ó Schedule 80, Solo para uso exterior subterráneo. Clasificación EN

50086/ 4443.

Norma: NCH No 399, CNH No 769 y norma Chilectra No 51.

Fabricación: P.V.C. denso, RD/UV, resistencia a la radiación total. Tipo Conduit

Norma ASTM 1785 Schedule 40 ó 80,

Acoplamiento: Unión expansiva o coplas de P.V.C., con adhesivos para P.V.C.

Dimensión: Sch 40 ó 80 de 110 mm según corresponda

En general para todas las canalizaciones subterráneas se utilizarán tuberías plásticas de

P.V.C. para uso eléctrico del tipo Conduit industrial fabricado según Norma ASTM 1785

Schedule 40,

## 6.3. SALAS ELECTRICAS MT (SS/EE)

El equipamiento que se considerar en el diseño del recinto de la SS/EE eléctrica, incluye las

siguientes unidades, cuyo equipamiento se montará en un nivel +15 cm por sobre el nivel

de piso terminado

**6.3.1.** **SALA ELECTRICA MT UTILITY**

 Celda de Protección Primaria y Medida de M.T. (Instalada por Cía. Eléctrica)

 Celdas Secundarias de MT de Operación y Maniobra.

 Fuente de Poder DC para control de celdas MT.

Las celdas deben ser del tipo Metal Clad, con interruptores extraíbles y transformadores de

potencial protegidos con fusibles extraíbles, cumpliendo con el nivel de continuidad de

servicios LSC 2B, indicado en la norma IEC 62271-200.

 Certificación sísmica, cumpliendo con ZONA UBC 4, y ETG 1510 de ENDESA Chile.

 Diseño Sísmico de Componentes y Sistemas No estructurales, NCh 3357:2015.

**MDC ELECTRICIDAD ST-5-001-RC** **Página 14 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

El tablero deberá ser diseñado y probado para los siguientes valores eléctricos:

Tensión nominal :23 KV Trifásico

Tensión Máx. de función o Nivel de Aislamiento :25 KV

Frecuencia Nominal :50 hz

Nivel de Aislamiento :50KV-50Hz, 1 min.

95KV-1,2/50 micro sec

Corriente nominal de barras : 630 A

Corriente de corto circuito :25KA - 3 sec

Rendimiento de arco interior :25KA / 1s

**6.3.2.** **SALAS ELECTRICAS INTERIORES DATA BLOQUES DE ENERGÍA**

 Celdas Secundarias de MT de Operación y Maniobra.

 Fuente de Poder DC para control de celdas MT.

 - Transformadores de Poder

Se proyectan celdas secundarias de operación y maniobra para cada. transformadores de

potencia. Estas celdas deberán ser del tipo Metal Enclosed, auto soportados, en base a

unidades modulares ensamblado en fábrica, para uso interior con interruptores fijos y

removibles contenidos en gabinetes metálicos y que usan hexafluoruro de azufre (SF6) como

medio de extinción, a prueba de arco interno en las cuatro caras. Como medida de

protección adicional se deberá considerar equipos con nivel de aislación para 24KV.

Capacidades Nominales:

 - Cubículos blindados de media tensión Clase 25 kV.

 Tensiones nominales y corriente de aguante de corta duración.

El tablero compartimentado debe estar adecuado para operar en sistemas de tres fases a 23

kV y 50 Hz.

La tensión nominal debe ser por lo menos de 23 kV. La corriente de aguante de corto tiempo

debe ser de : 16kA-1s/24kV

Todo el tablero debe ser capaz de aguantar las condiciones arriba mencionadas sin provocar

daño, de acuerdo con los párrafos 4.5, 4.6 y 4.7 de la IEC 60694 y las recomendaciones del

párrafo 4.5 de la IEC 60298.

**MDC ELECTRICIDAD ST-5-001-RC** **Página 15 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**6.3.3.** **DATA SHEET CELDAS MT**

**Rev. C**

**Fecha: 14-01-2024**

El nivel de aislamiento del tablero debe cumplir con las recomendaciones de la IEC y los

valores indicados en las tablas siguientes.

Características eléctricas principales:

Los valores que se presentan son para temperaturas de trabajo de -5°C a +40°C y para una

altitud de operación de 1000 msnm.

Estas celdas deberán estar construidas en forma modular y ampliable en el sitio. Estarán

compuestos por unidades funcionales. Cada cubículo o compartimiento deberá estar

separado del otro y dentro de una envolvente común mediante elementos metálicos, todos

conectados a tierra, tal como lo define la norma IEC 62271-200:

**MDC ELECTRICIDAD ST-5-001-RC** **Página 16 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

|Parametro|Unidad|Microcompact|
|---|---|---|
|Tension Nominal|kV|24|
|Clase aislamiento|kV|25|
|Corriente nominal de barras|A|630|
|Tension soportada a frecuencia industrial / 1<br>min|kV rms|50|
|Tension soportada a impulso tipo rayo|Kv pico|125|
|Frecuencia nominal|Hz|50|
|Corriente de corta duracion|kA/s|16/1|
|Corriente maxima|kA pico|40|
|Corriente soportada al arco interno|kA/s|12,5/1|
|Grado de proteccion|IP|3X|
|**UNIDADES FUNCIONALES CON INTERRUPTOR**|**UNIDADES FUNCIONALES CON INTERRUPTOR**|**UNIDADES FUNCIONALES CON INTERRUPTOR**|
|Corriente Nominal interruptores Alimentadores|A|630|
|Modelo||SF1-B1|
|Corriente nominal|A|630A.- 24KV.|
|Corriente de arco interno|kA/07 seg|12,5|
|**Nivel de Sismicidad**|**Nivel de Sismicidad**|**Nivel de Sismicidad**|
|Nivel mínimo certificado||UBC Zona 4|
|**Características eléctricas de los interruptores**|**Características eléctricas de los interruptores**|**Características eléctricas de los interruptores**|
|Voltaje máximo de uso|KV, 50/60 Hz|24|
|Nivel de aislamiento|KV, rsm 50hz<br>-1min|50|
|Nivel de aislamiento|KV, 1,2/50<br>impulse|125|
|Corriente nominal de las barras principales|A|630|
|Corriente nominal interruptor alimentador|A|630|
|Capacidad de corte de los interruptores|KA rms<br>at>17,5KV|16|
|Capacidad de cierre en falla|KA peek<br>17,5KV|40|
|Soporte al cortocircuito|KV rms 1s|16|
|<br>Tiempo aproximado de reacción|Apertura ms|48|
|<br>Tiempo aproximado de reacción|Corte ms|65|
|<br>Tiempo aproximado de reacción|Cierre ms|65|
|Operaciones mecánica||10.000 operaciones|
|**Tensiones de Control**|**Tensiones de Control**|**Tensiones de Control**|
|Para los motores de carga de resorte|VDC|125|
|Para las bocinas de cierre y de apertura|VDC|125|
|Para relé de proteccion|VDC|125|
|Para los sistemas de calefactores internos|VAC 50HZ|220|

Tabla 6.2 Características técnicas celdas MT

**MDC ELECTRICIDAD ST-5-001-RC** **Página 17 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**6.3.4.** **LISTADO CELDAS MT**

**Rev. C**

**Fecha: 14-01-2024**

|NOMBRE CELDA<br>UT-A.1|UBICACIÓN<br>CELDA SALA UTILITY A<br>CELDA SALA UTILITY A<br>CELDA SALA UTILITY A<br>CELDA SALA UTILITY A<br>CELDA SALA UTILITY A<br>CELDA SALA UTILITY B<br>CELDA SALA UTILITY B<br>CELDA SALA UTILITY B<br>CELDA SALA UTILITY B<br>CELDA SALA UTILITY B|PROTECCIÓN<br>NOMINAL [A]|TENSIÓN<br>NOMINAL [KV]|
|---|---|---|---|
|**NOMBRE CELDA**<br>UT-A.1|**UBICACIÓN**<br>CELDA SALA UTILITY A<br>CELDA SALA UTILITY A<br>CELDA SALA UTILITY A<br>CELDA SALA UTILITY A<br>CELDA SALA UTILITY A<br>CELDA SALA UTILITY B<br>CELDA SALA UTILITY B<br>CELDA SALA UTILITY B<br>CELDA SALA UTILITY B<br>CELDA SALA UTILITY B|630|23|
|UT-A.2|UT-A.2|630|23|
|UT-A.3|UT-A.3|630|23|
|UT-A.4|UT-A.4|630|23|
|UT-A.5<br>UT-B.1|UT-A.5<br>UT-B.1|630<br>630|23<br>23|
|UT-B.2|UT-B.2|630|23|
|UT-B.3|UT-B.3|630|23|
|UT-B.4|UT-B.4|630|23|
|UT-B.5|UT-B.5|630|23|
|UT-C.1|CELDA SALA UTILITY C|630|23|
|UT-C.2|CELDA SALA UTILITY C|630|23<br>23|
|UT-C.3|CELDA SALA UTILITY C|630|630|
|UT-C.4|CELDA SALA UTILITY C|630|23|
|UT-C.5|CELDA SALA UTILITY C|630|23|
|SW A.1|CELDA SALA ROOM-A|630|23<br>23|
|SW A.2|CELDA SALA ROOM-A<br>CELDA SALA ROOM-A|630|630|
|SW A.3|SW A.3|630|23|
|SW A.4|CELDA SALA ROOM-A|630|23|
|SW A.5|CELDA SALA ROOM-A|630|23|
|SW A.6|CELDA SALA ROOM-A|630|23|
|SW A.7|CELDA SALA ROOM-A|630|23|
|SW A.8|CELDA SALA ROOM-A|630|23|
|SW A.9|CELDA SALA ROOM-A<br>CELDA SALA ROOM-A|630|23|
|SW A.10|SW A.10|630|23|
|SW A.11|CELDA SALA ROOM-A|630|23|
|SW A.12|CELDA SALA ROOM-A|630|23|
|SW A.13|CELDA SALA ROOM-A|630|23|

**MDC ELECTRICIDAD ST-5-001-RC** **Página 18 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

|NOMBRE CELDA|UBICACIÓN|PROTECCIÓN<br>NOMINAL [A]|TENSIÓN<br>NOMINAL [KV]|
|---|---|---|---|
|SW B.1|CELDA SALA ROOM-B|630|23|
|SW B.2|CELDA SALA ROOM-B|630|23|
|SW B.3|CELDA SALA ROOM-B|630|23|
|SW B.4|CELDA SALA ROOM-B|630|23|
|SW B.5|CELDA SALA ROOM-B|630|23|
|SW B.6|CELDA SALA ROOM-B|630|23|
|SW B.7|CELDA SALA ROOM-B|630|23|
|SW B.8|CELDA SALA ROOM-B|630|23|
|SW B.9|CELDA SALA ROOM-B|630|23|
|SW B.10|CELDA SALA ROOM-B|630|23|
|SW B.11|CELDA SALA ROOM-B|630|23|
|SW B.12|CELDA SALA ROOM-B|630|23|
|SW B.13|CELDA SALA ROOM-B|630|23|
|A.1|CELDA BLOQUE A|630|23|
|A.2|CELDA BLOQUE A|630|23|
|A.3|CELDA BLOQUE A|630|23|
|B.1|CELDA BLOQUE B|630|23|
|B.2|CELDA BLOQUE B|630|23|
|B.3|CELDA BLOQUE B|630|23|
|C.1|CELDA BLOQUE C|630|23|
|C.2|CELDA BLOQUE C|630|23|
|C.3|CELDA BLOQUE C|630|23|
|D.1|CELDA BLOQUE D|630|23|
|D.2|CELDA BLOQUE D|630|23|
|D.3|CELDA BLOQUE D|630|23|
|E.1|CELDA BLOQUE E|630|23|
|E.2|CELDA BLOQUE E|630|23|
|E.3|CELDA BLOQUE E|630|23|
|P1.1|CELDA BLOQUE P1|630|23|
|P1.2|CELDA BLOQUE P1|630|23|
|P1.3|CELDA BLOQUE P1|630|23|
|P2.1|CELDA BLOQUE P2|630|23|
|P2.2|CELDA BLOQUE P2|630|23|
|P2.3|CELDA BLOQUE P2|630|23|
|F.1|CELDA BLOQUE F|630|23|
|F.2|CELDA BLOQUE F|630|23|
|F.3|CELDA BLOQUE F|630|23|

**MDC ELECTRICIDAD ST-5-001-RC** **Página 19 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

|NOMBRE CELDA<br>G.1|UBICACIÓN<br>CELDA BLOQUE G<br>CELDA BLOQUE G<br>CELDA BLOQUE G<br>CELDA BLOQUE H<br>CELDA BLOQUE H<br>CELDA BLOQUE H<br>CELDA BLOQUE J<br>CELDA BLOQUE J<br>CELDA BLOQUE J<br>CELDA BLOQUE P3<br>CELDA BLOQUE P3<br>CELDA BLOQUE P3|PROTECCIÓN<br>NOMINAL [A]|TENSIÓN<br>NOMINAL [KV]|
|---|---|---|---|
|**NOMBRE CELDA**<br> G.1|**UBICACIÓN**<br>CELDA BLOQUE G<br>CELDA BLOQUE G<br>CELDA BLOQUE G<br>CELDA BLOQUE H<br>CELDA BLOQUE H<br>CELDA BLOQUE H<br>CELDA BLOQUE J<br>CELDA BLOQUE J<br>CELDA BLOQUE J<br>CELDA BLOQUE P3<br>CELDA BLOQUE P3<br>CELDA BLOQUE P3|630|23|
|G.2|G.2|630|23|
|G.3<br> H.1|G.3<br> H.1|630<br>630|23<br>23<br>23<br>23<br>23<br>23<br>23<br>23|
|H.2|H.2|630|630|
|H.3<br> J.1|H.3<br> J.1|630<br>630|630<br>630|
|J.2|J.2|630|630|
|J.3|J.3|630<br>630|630<br>630|
|P3.1|P3.1|P3.1|P3.1|
|P3.2|P3.2|630|23|
|P3.3|P3.3|630|23|
|P4.1|CELDA BLOQUE P4|630|23|
|P4.2|CELDA BLOQUE P4|630<br>630<br>630|23|
|P4.3<br> R1.1|CELDA BLOQUE P4<br>CELDA BLOQUE R1|CELDA BLOQUE P4<br>CELDA BLOQUE R1|23<br>23|
|R1.2|CELDA BLOQUE R1|630|23|
|R1.3<br> R2.1|CELDA BLOQUE R1<br>CELDA BLOQUE R2<br>CELDA BLOQUE R2|630<br>630|23<br>23|
|R2.2|R2.2|630|23|
|R2.3|CELDA BLOQUE R2|630|23|

**MDC ELECTRICIDAD ST-5-001-RC** **Página 20 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

## 6.4. CONDUCTORES MEDIA TENSIÓN

**Rev. C**

**Fecha: 14-01-2024**

Para el uso de los circuitos de Media Tensión, entre celdas, se proyecta cables monopolares

de cobre, aislados con XLPE-TR, 25 KV, 133% NA, 90o C de temperatura de operación y libres

de halógenos. La fabricación y metidos de pruebas deben estar basados en las normas ICEA

S93-639.

Los conductores de media tensión, Clase 25 kV, deberán cumplir con las características

técnicas que se indican a continuación:

 Conductor monopolar aislado con. XLPE-TR 133% NA, 90oC temperatura de

operación, 25 KV, Libre de Halógeno

 El conductor será de cobre blando (recocido), de la(s) sección(s) indicadas en planos,

compuesto de hebras cableadas en forma concéntrica, de la Clase 2 según la norma

IEC 228.

 Capa sobre el conductor en base a compuesto de polietileno semiconductor

extruído.

 Método de prueba basados en las normas ICEA S93-630

 Capa de aislación en base a compuesto de polietileno reticulado.

 Compuesto de polietileno semiconductor extruído sobre capa de aislación.

 Pantalla metálica formada por flejes de cobre dispuestos helicoidalmente.

 Cubierta exterior formado con compuesto de PVC.

 La temperatura de Servicio del conductor no podrá ser inferior a los 90 oC y la de

cortocircuito no inferior a 250 oC.

 Los compuestos de polietileno y de PVC serán de alto retardo a la llama, baja emisión

de humos visibles y de gases tóxicos y corrosivos. (libres de halógenos), y podrán

estar basado en acetato de etilo-vinilo (EVA).

La máxima potencia estimada para cada transformador será la potencia nominal de cada

equipo a un factor de potencia de 0,97. Se estima inicialmente transformadores de 3150

[KVA]

P max =3150 x 0,97=3055,5[KW]

**MDC ELECTRICIDAD ST-5-001-RC** **Página 21 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

Esta potencia es la máxima estimada

Así La corriente en media tensión es :

I Nmt =3055,5/(√3×23×0,97)=79,07[A]

**Rev. C**

**Fecha: 14-01-2024**

El alimentador elegido es el cable XAT/EVA / MONOCONDUCTOR - 2/0 AWG-67,4 mm2

aislación XLPE-TR 25kV

El cable elegido tiene una corriente máxima de transporte tendido en forma subterránea de:

I cable =230[A]

Tabla 6.3 Características técnicas cables MT

**MDC ELECTRICIDAD ST-5-001-RC** **Página 22 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

## 6.5. POTENCIA SISTEMA ELÉCTRICO

**Rev. C**

**Fecha: 14-01-2024**

La potencia de cada bloque de energía considera las cargas de los servicios tecnológicos (TI)

y las cargas de servicios auxiliares, que comprende el consumo hecho por los equipos de

climatización, ventilación, alumbrado, enchufes, CCTV, Control de acceso, entre otros.

En la tabla 6.4 se muestra la potencia estimada por cada bloque de energía

Tabla 6.4 Potencia por bloque de energía

Cada bloque de energía considera la potencia requerida para cada sala de racks del sector.

Cada sector lo alimentará un bloque de energía compuesto por un transformador exclusivo.

En la tabla 6.4 se identifica la potencia demandada por cada área de un bloque de energía.

La potencia total estimada para todo el proyecto una vez construido todo el Data Center es

de 39,2 [MW] de potencia.

## 6.6. SUBESTACIÓN DE TRANSFORMACIÓN POR BLOQUE DE ENERGÍA

Cada transformador de cada bloque de energía del data center ST5 será de las siguientes

características:

El transformador para suministrar será de Alta Eficiencia de acuerdo con estándar EN 50588

1 y poseerá las siguientes características técnicas

 - Potencia : 3150 kVA

 - Refrigeración: Ventilación Natural

 - Aislante : Resina Epóxica.

 - Número de Fases: 3

 - Voltaje Primario : 23 kV

 - Derivaciones : ± 2.5%; ± 5%.

 - Voltaje Secundario : 400/231 V

 - Pérdidas en Vacío (P0) : 5.100 W

 - Pérdidas Bajo Carga (Pk @ 120°C): 26.000 W

 - Nivel de Ruido (LwA) : 83 dB

**MDC ELECTRICIDAD ST-5-001-RC** **Página 23 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

- Frecuencia : 50 Hz

- Grupo de conexión : Dyn 11

**Rev. C**

**Fecha: 14-01-2024**

 - Enrollado secundario : Estrella con neutro accesible

 - Polaridad : Sustractiva

 - Derivaciones en MT: +5%, +2,5%, 0, -2,5% y -5%

 - Impedancia : 6%

 - Régimen de utilización : Continuo

 - Altitud : 1.000 m.s.n.m.

 - Servicio: Interior con envolvente metálica IP31

cada transformador será en aislación seca, encapsulado en resina epoxi, clase de aislación F.

La refrigeración será por convección natural en aire (AN). Temperaturas de diseño:

 - máxima: 40 oC

 - mínima: -5 oC

 - media diaria: ≤ 30 oC

 - media anual ≤ 20 oC.

## 6.7. CÁLCULO DE LAS PROTECCIONES EN MT Y BT

**6.7.1.** **LADO MT**

La potencia de máxima demanda consumida bloque de energía y manejada por el

transformador es:

P N = 3150[KVA]

P N = 3150 ∗0,97[KW]

P N = 3055,5[KW]

La corriente en media tensión es :

3055,5
I N = ~~√~~ 3 × 23 × 0,97

La corriente máxima consumida es de 79,07 [A]

= 79.07[A]

La protección del relé de la celda de media tensión se debe de ajustar en

**MDC ELECTRICIDAD ST-5-001-RC** **Página 24 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

I adj < 79,07[A]

**Rev. C**

**Fecha: 14-01-2024**

Utilizando el criterio de corriente de protección I p mediante interruptor, la corriente

I P = 1,25 × I adj [A]

Con lo cual los límites de protección en el lado primario es :

I adj <= 90,83[A]

La corriente Inrush se define como

I inrush = 8 × I N [A]

Luego

I inrush < 632,56[A]

Para determinar los límites de protecciones del transformador se determina el punto ANSI

(I ANSI ; t ANSI )

I ANSI = 14,4 I N [A]

t ANSI = 5 [s]

Bajo estas condiciones el punto ANSI debe ser:

I adj < 1106,98[A]

t ANSI = 5 [s]

Considerando dejar el sistema a la máxima capacidad de ajustes, los valores elegidos para

las protecciones de la celdas de media tensión son:

I P = 125 [A]

I ANSI = 1106,98[A] ; t ANSI = 5 [s]

Los transformadores de corriente serán definidos a relación de transformación 200/5

**6.7.2.** **LADO BT**

Los valores referidos al secundario

**MDC ELECTRICIDAD ST-5-001-RC** **Página 25 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

La potencia de máxima demanda consumida bloque de energía y manejada por el

transformador es:

P N = 3150[KVA]

P N = 3150 ∗0,97[KW]

P N = 3055,5[KW]

La corriente en baja tensión es :

3055,5
I Nmt = ~~√~~ 3 × 0,38 × 0,97

= 4785[A]

La corriente máxima de salida del transformador es de 4785 [A]

La protección en BT se debe de ajustar

I adj <= 4785[A]

La protección comercial utilizada es un interruptor automático de

I N = 4000[A]

Si se elige el valor de 4000[A]. para el ajuste de la protección, el factor de ajuste es de 1,19

veces I adj

La corriente Inrush se define como

I inrush = 8 × I N [A]

Luego

I inrush = 32000[A]

Para determinar los límites de protecciones del transformador se determina el punto ANSI

(I ANSI ; t ANSI )

I ANSI = 14,4 I N [A]

t ANSI = 5 [s]

Bajo estas condiciones el punto ANSI debe ser:

I ANSI = 56.000 [A]

**MDC ELECTRICIDAD ST-5-001-RC** **Página 26 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

t ANSI = 5 [s]

El ajuste de la protección debe ser:

I N = 4000[A]

I ANSI = 56.000[A] ; t ANSI = 5 [s]

**Rev. C**

**Fecha: 14-01-2024**

Los transformadores de corriente serán definidos a relación de transformación 4000/5

## 6.8. LISTADO DE TRANSFORMADORES

|NOMBRE|BLOQUE DE ENERGÍA|POTENCIA NOMINAL<br>[KVA]|TENSIÓN<br>NOMINAL [KV]|
|---|---|---|---|
|TR- A|BLOQUE A|3150|23<br>23|
|TR-B|BLOQUE B|3150|3150|
|TR-C|BLOQUE C<br>BLOQUE D|3150|23|
|TR-D|TR-D|3150|23|
|TR-E|BLOQUE E|3150|23|
|TR-P1|BLOQUE P1|3150|23|
|TR-P2|BLOQUE P2|3150|23|
|TR-F|BLOQUE F|3150|23|
|TR-G|BLOQUE G|3150|23|
|TR-H|BLOQUE H|3150|23|
|TR-J<br>TR-P3|BLOQUE J|3150|23|
|TR-J<br>TR-P3|BLOQUE P3|3150|23|
|TR-P4|BLOQUE P4|3150|23|
|TR-R1|BLOQUE R1|3150|23|
|TR-R2|BLOQUE R2|3150|23|
|TR-FOH|EDIFICIO ADMINISTRATIVO|500|23|

Tabla 6.6 Listado de transformadores data center ST5

## 6.9. SISTEMA DE RESPALDO

La planta de generación tendrá un grupo electrógeno por cada transformador de poder, es

decir se contará con un grupo electrógeno por cada bloque de energía

Los grupos electrógenos serán todos de iguales características técnicas y de potencia

**MDC ELECTRICIDAD ST-5-001-RC** **Página 27 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

Cada grupo generador deberá tener al menos la potencia considerada para cada

transformador, lo cual permitirá que la planta de generación en su conjunto abastezca el

100% de la potencia proyectada para cada bloque

El sistema de respaldo está diseñado para alimentar la totalidad de las cargas del bloque de

energía, por lo que, en caso de pérdida del suministro normal, el bloque de energía podrá

operar en forma normal estando alimentado desde el grupo electrógeno.

**6.9.1.** **CARACTERISTICAS GENERALES.**

Potencia de salida prime: 3500 KVA (2800 KW)

Horas funcionamiento en potencia Prime: 10%

Factor de potencia: 0.8

Voltaje Nominal: 400/230 volts C.A.

Corriente Nominal: 4431 A

Fases: 3 + neutro

Conexión: ”Y” con neutro accesible

Velocidad de giro: 1.500 r.p.m.

Frecuencia: 50 Hz

Regulación de frecuencia de salida: ±0.5%

Condiciones de operación: < 1000 m.s.n.m.y 40oC

Alternador

Conexión Estrella

Regulador electrónico de tensión AREP R450

Regulación de tensión ± 2,5%

Cortocircuito sostenido 3 In durante 10 s

Número de fases 3

Aislamiento Clase H

Grado de protección IP-23

Factor de potencia 0,8

Frecuencia 50 Hz

Tensión 400/223 V

Baterías

Tensión corriente continua 24 V

Capacidad de cada batería 210 Ah

Tipo Plomo-ácido

**MDC ELECTRICIDAD ST-5-001-RC** **Página 28 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**6.9.2.** **MÓDULO DE CONTROL**

**Rev. C**

**Fecha: 14-01-2024**

El Grupo Electrógeno incluirá un Tablero ubicado sobre la caja de bornes del Generador

Sincrónico, aislado contra vibraciones, el cual incluirá un botón tipo “Push-Button” para

parada de emergencia del grupo generador y un Módulo de Control y Automatismo del tipo

Digital Programable, desde el cual se podrán leer en forma digital todos los parámetros de

operación tanto del Motor como aquellos del Generador. En éste se incorporan las

siguientes funciones automáticas de control, entre otras programables.

Principales Características:

 Función automático y manual.

 Módulo de Sincronismo, que permite al grupo generador sincronizarse con la red

eléctrica y que el retorno de energía no genere una desconexión en el sistema.

Esto debe de ocurrir tanto para un corte de energía o para efectuar pruebas del

grupo generador sin que se deba cortar la energía eléctrica por unos segundos.

 Sistema de comunicación y expansiones Modbus.

 Parámetros del motor: velocidad, presión de aceite, temperatura de refrigerante,

voltaje de batería a nivel de aceite, horas de funcionamiento, tiempos de

arranque y voltaje de carga.

 Parámetros del alternador: frecuencia, voltajes (L-L, L-N) y corriente trifásica.

 Parámetros de potencia: kVA, kW, kVAr, kWh, kVAh, kVArh y factor de potencia.

 Parámetros de red: Frecuencia, voltaje trifásico (L-L, L-N).

 Funciones lógicas a través de PLC (hasta 100).

 Control de red y protección de motor y alternador.

 Velocidad del motor, presión del aceite del motor, temperatura de refrigerante

del motor, voltaje del cargador de batería, voltaje, corriente, frecuencia del

alternador. voltaje y frecuencia de red.

 Posee puertos de comunicación RS232 y RS485.

 - Protocolo de comunicación Modbus RTU

 3 configuraciones alternativas

 12 entradas configurables y 8 salidas configurables.

 Registro de eventos configurable (250)

**MDC ELECTRICIDAD ST-5-001-RC** **Página 29 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**6.9.3.** **LISTADO DE GRUPOS GENERADORES**

**Rev. C**

**Fecha: 14-01-2024**

|NOMBRE<br>GG- A|BLOQUE DE ENERGÍA<br>BLOQUE A<br>BLOQUE B<br>BLOQUE C<br>BLOQUE D<br>BLOQUE E<br>BLOQUE P1<br>BLOQUE P2<br>BLOQUE F|POTENCIA NOMINAL<br>[KVA]<br>3500|TENSIÓN<br>NOMINAL [KV]<br>0,4<br>0,4<br>0,4<br>0,4<br>0,4<br>0,4<br>0,4<br>0,4|
|---|---|---|---|
|GG-B|GG-B|3500|3500|
|GG-C|GG-C|3500|3500|
|GG-D|GG-D|3500|3500|
|GG-E|GG-E|3500|3500|
|GG-P1|GG-P1|3500|3500|
|GG-P2|GG-P2|3500|3500|
|GG-F|GG-F|3500|3500|
|GG-G<br>GG-H|BLOQUE G|3500|0,4|
|GG-G<br>GG-H|BLOQUE H|3500|0,4|
|GG-J|BLOQUE J|3500|0,4|
|GG-P3|BLOQUE P3|3500|0,4<br>0,4|
|GG-P4|BLOQUE P4|3500|3500|
|GG-R1|BLOQUE R1|3500|0,4|
|GG-R2|BLOQUE R2|3500|0,4|
|GG AUG|AUMENTO DE POTENCIA|3500|0,4|
|GG-FOH|EDIFICIO ADMINISTRATIVO|900|0,4|

Tabla 6.7 Listado de grupos generadore data center ST5

## 6.10. SISTEMA UPS

Se proyectan dos UPS para dar respaldo a los sistemas TI exclusivos asociados q cada bloque

de energía. Cada UPS serán de iguales características y capacidad. Una UPS alimentará la

mitad de los rack de cada sala blanca

La potencia TI por bloque es de:

P N = 1931[KW]

Las potencia de cada UPS será la mitad de la potencia total del bloque, así la potencia de

cada UPS será:

P ups = 965,5[KW]

El equipo sólo se puede cargar hasta el 80%, de la potencia total. Aplicando un factor de

carga de un 80% y con un factor de potencia del equipo de 0,96 se obtiene la potencia en

KVA requerida:

**MDC ELECTRICIDAD ST-5-001-RC** **Página 30 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

Potencia Equipo UPS= [D] [max]

f c × f p

[KVA]

Así,

965,5
Potencia Equipo UPS=
0,8 × 0,96 [= 1257[KVA]]

Se requiere de un sistema de respaldo de UPS de 1257 [KVA]. Se elije el valor comercial de

UPS de 1250 [KVA]- 1200[KW] a un F.P de 0,96

**MDC ELECTRICIDAD ST-5-001-RC** **Página 31 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**6.10.1.** **LISTADO DE UPS**

**Rev. C**

**Fecha: 14-01-2024**

|NOMBRE|BLOQUE DE ENERGÍA|POTENCIA NOMINAL<br>[KW]|TENSIÓN<br>NOMINAL [KV]|
|---|---|---|---|
|UPS- A.1|BLOQUE A|1200|0,4|
|UPS- A.2|UPS- A.2|1200|0,4|
|UPS-B.1|BLOQUE B|1200|0,4|
|UPS-B.2|UPS-B.2|1200|0,4|
|UPS-C.1|BLOQUE C|1200|0,4|
|UPS-C.2|UPS-C.2|1200|0,4|
|UPS-D.1|BLOQUE D|1200|0,4|
|UPS-D.2|UPS-D.2|1200|0,4|
|UPS-E.1|BLOQUE E|1200|0,4|
|UPS-E.2|UPS-E.2|1200|0,4|
|UPS-P1.1|BLOQUE P1|1200|0,4|
|UPS-P1.2|UPS-P1.2|1200|0,4|
|UPS-P2.2|BLOQUE P2|1200|0,4|
|UPS-P2.2|UPS-P2.2|1200|0,4|
|UPS-F.1|BLOQUE F|1200|0,4|
|UPS-F.2|UPS-F.2|1200|0,4|
|UPS-G.1|BLOQUE G|1200|0,4|
|UPS-G.2|UPS-G.2|1200|0,4|
|UPS-H.1|BLOQUE H|1200|0,4|
|UPS-H.2|UPS-H.2|1200|0,4|
|UPS-J.1|BLOQUE J|1200|0,4|
|UPS-J.2|UPS-J.2|1200|0,4|
|UPS-P3.1|BLOQUE P3|1200|0,4|
|UPS-P3.2|UPS-P3.2|1200|0,4|
|UPS-P4.1|BLOQUE P4|1200|0,4|
|UPS-P4.2|UPS-P4.2|1200|0,4|
|UPS-R1.1|BLOQUE R1|1200|0,4|
|UPS-R1.2|UPS-R1.2|1200|0,4|
|UPS-R2.1|BLOQUE R2|1200|0,4|
|UPS-R2.2|UPS-R2.2|1200|0,4|

**MDC ELECTRICIDAD ST-5-001-RC** **Página 32 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

## 6.11. TABLEROS Y PANELES SISTEMAS ELÉCTRICOS

**Rev. C**

**Fecha: 14-01-2024**

El proyecto contempla tableros de Entrada y Distribución terminal. Para cargas TI y servicios

auxiliares del data center ST5

 Todos los tableros deberán garantizar un servicio continuo absolutamente seguro

desde todo punto de vista.

 - Estarán construidos con materiales de óptima calidad y ampliamente

experimentados, conforme a las reglas del buen arte y las recomendaciones de la

Comisión Electrotécnica Internacional I.E.C. N° 439; cumpliendo con los ensayos de

tipo establecidos por las mismas y correspondiendo al tipo totalmente probado

 La instalación de cada aparato o grupo de aparatos incluirá los elementos mecánicos

y eléctricos de acometida, soporte, protección y salida que contribuyan a la ejecución

de una sola función (“unidad funcional”). El conjunto de las diversas unidades

funcionales permitirá la ejecución de un conjunto o sistema funcional.

 Los montajes y/o conexionados de partes serán hechos a partir de componentes

prefabricados estándar.

 El diseño de las Celdas deberá permitir la modificación de la distribución interna sin

mayores inconvenientes y durante cualquier etapa de su construcción, instalación o

explotación.

 Tendrán una disposición simple de aparatos y componentes, y su operación será

razonablemente sencilla a fin de evitar maniobras erróneas.

 Brindarán protección al personal y seguridad de servicio. Para cumplir este

requerimiento los tableros estarán protocolizados según la norma AS 3439-1,

mediante el ensayo de falla con arco interno.

**MDC ELECTRICIDAD ST-5-001-RC** **Página 33 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**6.11.1.** **Referencia Técnicas. Normativas**

**Rev. C**

**Fecha: 14-01-2024**

Todos los equipos, así [́] como los dispositivos y accesorios, cubiertos por esta especificación,

deben cumplir los requerimientos aplicables que se indican en la última edición de las

siguientes normas y referencias:

Decreto 8 RIC No 02 Tableros Eléctricos

NEC : National Electrical Code

NEMA National Electric Manufacturers Association

ANSI American National Standard Institute

IEEE: Institute of Electrical and Electronic Engineers

ASTM American Standard for Testing Material

UL: Underwriters Laboratories

IEC: International Electrical Commission en particular IEC 60429

Cada equipo suministrado bajo esta especificación será adecuado para operar al interior de

una Sala Eléctrica con ambiente limpio y ventilada. Además, estará capacitado para una

operación continua (24 hrs. al día, 365 días al año), bajo las siguientes condiciones

ambientales:

 - Ubicación : Sala Eléctrica

 - Altura sobre el Nivel del Mar : 1.000 mts.

 - Contaminación ambiente: Limpio

Además, los equipos suministrados deberán ser capaces de operar en un sistema eléctrico

de las siguientes características de servicio en B. T

 - Voltaje Nominal BT: 380V AC +N+PE

 - Frecuencia: 50Hz

 - No de fases: 3

 - Neutro: Sólidamente Aterrizado

 - Nivel de Corto Circuito: 70KA Para Entrada / 50KA para barra de

distribución

 - Servicio Continuo

 De cualquier manera, estos valores de Niveles de Corto Circuito deberán ser

confirmados mediante Memorias de Cálculos y mediante solicitud a la Cía. Eléctrica

de la zona de estudios de los niveles de Icc en el punto de conexión.

**MDC ELECTRICIDAD ST-5-001-RC** **Página 34 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

Construcción placa de acero espesor 1,5mm

Acceso de barras de distribución por la parte posterior

- Pintura al horno o electrostática, antioxidante.

**Rev. C**

**Fecha: 14-01-2024**

 Tablero compuesto por panel de montaje, interruptores moldeada, instrumentación,

accesorios, soportes de sujeción y ordenadores de cables a la entrada y salida;

bandeja porta documentos en la parte interior (detrás de la puerta).

 Sistema de Ventilación compuesto por controlador de temperatura, ventiladores y

filtros de aire

**6.11.2.** **Características Mecánicas y de Construcción**

Todos los tableros serán fabricados en planchas de acero de 1,5mm. de espesor mínimo;

con puerta abisagrada y reversible, chapa cilíndrica suministrado de fábrica, provista de dos

juegos de llaves (no del tipo triangular o cuadrado) y montaje en chasis. Esta llave debe ser

maestra para que abra todos los tableros de distribución no copiable.

Cubre equipo metálico rígidos es decir, con refuerzos adelante y atrás, el fondo empotrado

y los ángulos redondeados.

Los tableros tendrán protección contra la corrosión, IP 55-IK10 según norma IEC 529; con

una aplicación de revestimiento de poliéster textura do de 60 μ de espesor, Color Beige RAL

7032, equipados en la puerta con una junta de estanqueidad de poliuretano expandido

sellado de una sola pieza y sin uniones, de manera que evite la entrada de polvo, provistos

de una gotera y espacio puerta / armario reducido.

Los tableros auto-soportados se proyectan con un zócalo de 150mm. de alto como mínimo

Todas las barras de Tableros Generales serán de cobre electrolito pintadas. Las barras estarán

aisladas entre sí por medio de separaciones de material aislante con dieléctrico alto (tubo o

manga termo contraíble), baja absorción de polvo y humedad, junto con una elevada

resistencia mecánica de manera de asegurar que resistan, sin destruirse ni deformarse, ante

los esfuerzos electrodinámicos y térmicos provocados por el nivel de cortocircuito.

La capacidad de las barras de distribución se proyecta a un 25% más de la capacidad del

automático general de protección. El cableado de los tableros será con conductor con

aislación tipo PVC o XLPE. En general el dimensionamiento de cables y barras de distribución

se proyecta respetando la norma IEC 60364, ANDE y NP.

Las barras de T.s. y T.p.., en los tableros ubicados dentro de la sala de electricidad, serán

aisladas de los gabinetes, ya que los gabinetes quedan aterrizados a la malla general. (STP.).

**MDC ELECTRICIDAD ST-5-001-RC** **Página 35 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

Las tapas de los tableros estarán conectadas a tierra mediante un cable flexible.

En las puertas de los tableros se instalan pilotos de señalización de fases de 22mm, IP 55.

Estarán conforme a norma IEC 947-3. Estos pilotos serán protegidos con fusibles de 2 A.

Los repartidores serán modulares con montaje a riel din hasta 160 A suministrados con placa

trasera aislante y tapa de protección con cara anterior transparente. Conforme a la norma

EN 60-947-1.

Los repartidores con capacidad superior a 160 A serán del tipo de conexión para terminales

o barras, con pantalla protectora y etiqueta autoadhesiva con indicación de tensión

peligrosa

Donde existan partes energizadas a la vista con probabilidad de contactos accidentales, se

considera una tapa de acrílico transparente de 3mm. de espesor mínimo, apernada para

desmontarse con facilidad.

**6.11.3.** **Cableado Interno**

Todos los cables instalados en el interior del tablero serán con aislación mínima de 630 V y

para 90° de temperatura máxima de trabajo, aislación

La sección de los conductores de alimentación debe sobrepasar la capacidad del interruptor.

El cableado de control se realizará con cable flexible de una sección mínima 1,5 mm2,

aislación 630 V y 90 oC de temperatura de trabajo. Cada extremo del cable de control llevará

terminal de presión y la identificación correspondiente.

Los bornes de control, destinados al cableado de control interno, irán separados de los

bornes de fuerza, si de estos últimos los hubiera.

Los cables alimentadores de entrada y de circuitos para salida al tablero lo harán tanto por

la parte superior como por la parte inferior mediante tapas desmontables y acceso exclusivo.

**6.11.4.** **Selectividad**

Se proyectan los siguientes rangos:

 - Protector General Automático en Tablero General 70 - 50 KA

 - Protector de Tablero General Auxiliar 50 - 36 KA

 - Protectores de generales de tableros de distribución 25 a 15 KA

 - Disyuntores trifásicos y monofásicos 6 a 10 KA

**MDC ELECTRICIDAD ST-5-001-RC** **Página 36 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

Estos valores estarán sujetos al estudio de niveles de cortocircuito.

**6.11.5.** **Instrumentos de Medición, Señalización**

**Rev. C**

**Fecha: 14-01-2024**

Los sistemas de medida en los tableros generales serán con instrumentos digitales, para

lectura de las siguientes variables:

Características:

 Para redes de baja y alta tensión.

 Multimediciones (3U, 3V, 3I, In, +/-3P, +/-ΣP, +/-3Q, +/-ΣQ, ΣS, 3FP, ΣFP y F)

 Max. y última demanda 4I, +/-ΣP, +/-ΣQ y ΣS.

 Valores promedio y máximos (3U, 3V, F).

 kWh (+/-), kvarh (+/-) y medición kVAh.

 - THD 3U, 3V, 3I

 - Además,

 Memorización de los valores máximos y mínimos de los distintos parámetros

eléctricos

 Posibilidad de expansión para la medida de energía activa y reactiva.

**6.11.6.** **Aparellaje**

Todos los automáticos generales o que alimenten otros circuitos se proyectan del tipo “caja

moldeada” para asegurar selectividad, con las corrientes nominales y capacidades de ruptura

que se arroje el estudio correspondiente. Trabajarán sin problemas a 40°C a plena capacidad,

y tendrán un porta etiquetas en la cara frontal de la caja moldeada para la identificación de

los circuitos.

Los disyuntores para los circuitos menores se proyectan a riel DIN, con curvas de operación

B, C o D según correspondan. Tensiones nominales para monofásico y trifásico AC 240/415V

respectivamente, con porta etiqueta en la protección, con borne de entrada y de salida

según el conductor a conectar. Se proyectan con sistema de protección contra el arco

eléctrico, según normativa SEC decreto DS8/2019

Los diferenciales se proyectan cumplir con las siguientes características por tipo de servicio:

Enchufes Normales, Equipos Pequeños de Fuerza y sistema de iluminación:

Servicios generales: Interruptor diferencial que interrumpa automáticamente el circuito en

caso de defecto a tierra igual o superior a 30mA.

**MDC ELECTRICIDAD ST-5-001-RC** **Página 37 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

Los contactores serán del tipo industrial clase AC3 para fuerza y clase AC1 para alumbrado,

garantizados para un mínimo de un millón de operaciones. Responderán a las prescripciones

para aparatos de maniobra de baja Tensión según normas VDE 0660 parte I y a la publicación

IEC 158-I parte I.

Tendrán relés térmicos con reset, contactos auxiliares y bobina de 220V, salvo

especificaciones en contrario de la documentación, en la que también se indicarán las

capacidades, forma de arranque y parámetros eléctricos de los arrancadores.

La salida de los circuitos a las cargas o consumos eléctricos serán por intermedio de bornes

(fase, neutro, tierra) apilables con topes de fijación, que permitan un sistema de marcación

eclipsable. Autoextinguentés, con características de hidroscopocidad para evitar retención

de humedad. Conforme a norma EN 60- 947-7-1.

Para el conexionado del cableado interior de los tableros se utilizarán terminales con cuerpo

aislante. El cableado y conexionado se ejecutará en forma ordenada manteniendo una

identificación adecuada de los conductores con un sistema de marcación aprobado por el

SEC

La canalización de los conductores al interior del tablero se realizará por intermedio de

canaleta porta conductores de P.V.C., ranurada lateralmente con paso de 12,5mm. y tapa,

adhesivo o escritura con lápiz indeleble.

**6.11.7.** **Rotulación Tableros**

Los tableros levarán tarjeteros, además se podrá guardar planos de esquemas unilineales

correspondientes a cada tablero, estos serán termo laminados. Para la identificación de los

circuitos en panel se considerará placas de acrílico negras con letras blancas, lo indicado

será tanto para tableros generales y distribución.

Los circuitos dentro de los tableros serán rematados con borneras. Además, los circuitos

serán ser identificados con letras o números adecuados a la bornera que se usen y se

marcarán los cables a la entrada y salida del automático y de la bornera con collarines

adecuados y la numeración correspondiente.

Cada tablero debe de contar con la con la señalización normalizada de “Riesgo Eléctrico” y

el nombre del tablero

**MDC ELECTRICIDAD ST-5-001-RC** **Página 38 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**6.11.8.** **LISTADO DE TABLEROS GENERALES**

**Rev. C**

**Fecha: 14-01-2024**

|NOMBRE|BLOQUE DE ENERGÍA|POTENCIA NOMINAL<br>[KVA]|PROTECCIÓN<br>NOMINAL [A]|TENSIÓN<br>NOMINAL [KV]|
|---|---|---|---|---|
|TG. ATS G.A|BLOQUE A|2800|4000|0,4|
|MSA A|MSA A|2800|4000|0,4|
|MDSB A-1|MDSB A-1|264|400|0,4|
|MDSB A-MEC|MDSB A-MEC|605|1200|0,4|
|UDP A-1|UDP A-1|1200|2000|0,4|
|UDP A-2|UDP A-2|1200|2000|0,4|
|STS. A 1.1|STS. A 1.1|483|2000|0,4|
|STS. A 1.2|STS. A 1.2|483|2000|0,4|
|STS. A 1.3|STS. A 1.3|483|2000|0,4|
|STS. A 1.4|STS. A 1.4|483|2000|0,4|
|STSSB. A-1|STSSB. A-1|483|2000|0,4|
|STSSB. A-2|STSSB. A-2|483|2000|0,4|
|STSSB. A-3|STSSB. A-3|483|2000|0,4|
|STSSB. A-4|STSSB. A-4|483|2000|0,4|
|TG. ATS G.B|BLOQUE B|2800|4000|0,4|
|MSA B|MSA B|2800|4000|0,4|
|MDSB B-1|MDSB B-1|264|400|0,4|
|MDSB B-MEC|MDSB B-MEC|605|1200|0,4|
|UDP B-1|UDP B-1|1200|2000|0,4|
|UDP B-2|UDP B-2|1200|2000|0,4|
|STS. B 1.1|STS. B 1.1|483|2000|0,4|
|STS. B 1.2|STS. B 1.2|483|2000|0,4|
|STS. B 1.3|STS. B 1.3|483<br>483<br>483|2000|0,4|
|STS. B 1.4|STS. B 1.4|STS. B 1.4|2000|0,4|
|STSSB. B-1|STSSB. B-1|STSSB. B-1|2000|0,4|
|STSSB. B-2|STSSB. B-2|483|2000|0,4|
|STSSB. B-3|STSSB. B-3|483<br>483|2000|0,4|
|STSSB. B-4|STSSB. B-4|STSSB. B-4|2000|0,4|
|TG. ATS G.C|BLOQUE C|2800|4000|0,4|
|MSA C|MSA C|2800<br>264|4000|0,4|
|MDSB C-1|MDSB C-1|MDSB C-1|400|0,4|
|MDSB C-MEC|MDSB C-MEC|605|1200|0,4|
|UDP C-1|UDP C-1|1200|2000|0,4|
|UDP C-2|UDP C-2|1200|2000|0,4|
|STS. C 1.1|STS. C 1.1|483|2000|0,4|
|STS. C 1.2|STS. C 1.2|483|2000|0,4|
|STS. C 1.3|STS. C 1.3|483|2000|0,4|
|STS. C 1.4|STS. C 1.4|483|2000|0,4|
|STSSC. B-1|STSSC. B-1|483|2000|0,4|
|STSSC. B-2|STSSC. B-2|483|2000|0,4|
|STSSC. B-3|STSSC. B-3|483|2000|0,4|
|STSSC. B-4|STSSC. B-4|483|2000|0,4|

**MDC ELECTRICIDAD ST-5-001-RC** **Página 39 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

|NOMBRE|BLOQUE DE ENERGÍA|POTENCIA NOMINAL<br>[KVA]|PROTECCIÓN<br>NOMINAL [A]|TENSIÓN<br>NOMINAL [KV]|
|---|---|---|---|---|
|TG. ATS G.D|BLOQUE D|2800|4000|0,4|
|MSA D|MSA D|2800|4000|0,4|
|MDSB D-1|MDSB D-1|264|400|0,4|
|MDSB D-MEC|MDSB D-MEC|605|1200|0,4|
|UDP D-1|UDP D-1|1200|2000|0,4|
|UDP D-2|UDP D-2|1200|2000|0,4|
|STS. D 1.1|STS. D 1.1|483|2000|0,4|
|STS. D 1.2|STS. D 1.2|483|2000|0,4|
|STS. D 1.3|STS. D 1.3|483|2000|0,4|
|STS. D 1.4|STS. D 1.4|483|2000|0,4|
|STSSC. D-1|STSSC. D-1|483|2000|0,4|
|STSSC. D-2|STSSC. D-2|483|2000|0,4|
|STSSC. D-3|STSSC. D-3|483|2000|0,4|
|STSSC. D-4|STSSC. D-4|483|2000|0,4|
|TG. ATS G.E|BLOQUE E|2800|4000|0,4|
|MSA E|MSA E|2800|4000|0,4|
|MDSB E-1|MDSB E-1|264|400|0,4|
|MDSB E-MEC|MDSB E-MEC|605|1200|0,4|
|UDP E-1|UDP E-1|1200|2000|0,4|
|UDP E-2|UDP E-2|1200|2000|0,4|
|STS. E 1.1|STS. E 1.1|483|2000|0,4|
|STS. E 1.2|STS. E 1.2|483|2000|0,4|
|STS. E 1.3|STS. E 1.3|483<br>483<br>483|2000|0,4|
|STS. E 1.4|STS. E 1.4|STS. E 1.4|2000|0,4|
|STSSC. E-1|STSSC. E-1|STSSC. E-1|2000|0,4|
|STSSC. E-2|STSSC. E-2|483|2000|0,4|
|STSSC. E-3|STSSC. E-3|483<br>483|2000|0,4|
|STSSC. E-4|STSSC. E-4|STSSC. E-4|2000|0,4|
|TG. ATS G.P1|BLOQUE P1|2800|4000|0,4|
|MSA P1|MSA P1|2800<br>264|4000|0,4|
|MDSB P1-1|MDSB P1-1|MDSB P1-1|400|0,4|
|MDSB P1-MEC|MDSB P1-MEC|605|1200|0,4|
|UDP P1-1|UDP P1-1|1200|2000|0,4|
|UDP P1-2|UDP P1-2|1200|2000|0,4|
|STS. P1 1.1|STS. P1 1.1|483|2000|0,4|
|STS. P1 1.2|STS. P1 1.2|483|2000|0,4|
|STS. P1 1.3|STS. P1 1.3|483|2000|0,4|
|STS. P1 1.4|STS. P1 1.4|483|2000|0,4|
|STSSC. P1-1|STSSC. P1-1|483|2000|0,4|
|STSSC. P1-2|STSSC. P1-2|483|2000|0,4|
|STSSC. P1-3|STSSC. P1-3|483|2000|0,4|
|STSSC. P1-4|STSSC. P1-4|483|2000|0,4|

**MDC ELECTRICIDAD ST-5-001-RC** **Página 40 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

|NOMBRE|BLOQUE DE ENERGÍA|POTENCIA NOMINAL<br>[KVA]|PROTECCIÓN<br>NOMINAL [A]|TENSIÓN<br>NOMINAL [KV]|
|---|---|---|---|---|
|TG. ATS G.P2|BLOQUE P2|2800|4000|0,4|
|MSA P2|MSA P2|2800|4000|0,4|
|MDSB P2-1|MDSB P2-1|264|400|0,4|
|MDSB P2-MEC|MDSB P2-MEC|605|1200|0,4|
|UDP P2-1|UDP P2-1|1200|2000|0,4|
|UDP P2-2|UDP P2-2|1200|2000|0,4|
|STS. P2 1.1|STS. P2 1.1|483|2000|0,4|
|STS. P2 1.2|STS. P2 1.2|483|2000|0,4|
|STS. P2 1.3|STS. P2 1.3|483|2000|0,4|
|STS. P2 1.4|STS. P2 1.4|483|2000|0,4|
|STSSC. P2-1|STSSC. P2-1|483|2000|0,4|
|STSSC. P2-2|STSSC. P2-2|483|2000|0,4|
|STSSC. P2-3|STSSC. P2-3|483|2000|0,4|
|STSSC. P2-4|STSSC. P2-4|483|2000|0,4|
|TG. ATS G.F|BLOQUE F|2800|4000|0,4|
|MSA F|MSA F|2800|4000|0,4|
|MDSB F-1|MDSB F-1|264|400|0,4|
|MDSB F-MEC|MDSB F-MEC|605|1200|0,4|
|UDP F-1|UDP F-1|1200|2000|0,4|
|UDP F-2|UDP F-2|1200|2000|0,4|
|STS. F 1.1|STS. F 1.1|483|2000|0,4|
|STS. F 1.2|STS. F 1.2|483|2000|0,4|
|STS. F 1.3|STS. F 1.3|483<br>483<br>483|2000|0,4|
|STS. F 1.4|STS. F 1.4|STS. F 1.4|2000|0,4|
|STSSC. F-1|STSSC. F-1|STSSC. F-1|2000|0,4|
|STSSC. F-2|STSSC. F-2|483|2000|0,4|
|STSSC. F-3|STSSC. F-3|483<br>483|2000|0,4|
|STSSC. F-4|STSSC. F-4|STSSC. F-4|2000|0,4|
|TG. ATS G.G|BLOQUE G|2800|4000|0,4|
|MSA G|MSA G|2800<br>264|4000|0,4|
|MDSB G-1|MDSB G-1|MDSB G-1|400|0,4|
|MDSB G-MEC|MDSB G-MEC|605|1200|0,4|
|UDP G-1|UDP G-1|1200|2000|0,4|
|UDP G-2|UDP G-2|1200|2000|0,4|
|STS. G 1.1|STS. G 1.1|483|2000|0,4|
|STS. G 1.2|STS. G 1.2|483|2000|0,4|
|STS. G 1.3|STS. G 1.3|483|2000|0,4|
|STS. G 1.4|STS. G 1.4|483|2000|0,4|
|STSSC. G-1|STSSC. G-1|483|2000|0,4|
|STSSC. G-2|STSSC. G-2|483|2000|0,4|
|STSSC. G-3|STSSC. G-3|483|2000|0,4|
|STSSC. G-4|STSSC. G-4|483|2000|0,4|

**MDC ELECTRICIDAD ST-5-001-RC** **Página 41 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

|NOMBRE|BLOQUE DE ENERGÍA|POTENCIA NOMINAL<br>[KVA]|PROTECCIÓN<br>NOMINAL [A]|TENSIÓN<br>NOMINAL [KV]|
|---|---|---|---|---|
|TG. ATS G.H|BLOQUE H|2800|4000|0,4|
|MSA H|MSA H|2800|4000|0,4|
|MDSB H-1|MDSB H-1|264|400|0,4|
|MDSB H-MEC|MDSB H-MEC|605|1200|0,4|
|UDP H-1|UDP H-1|1200|2000|0,4|
|UDP H-2|UDP H-2|1200|2000|0,4|
|STS. H 1.1|STS. H 1.1|483|2000|0,4|
|STS. H 1.2|STS. H 1.2|483|2000|0,4|
|STS. H 1.3|STS. H 1.3|483|2000|0,4|
|STS. H 1.4|STS. H 1.4|483|2000|0,4|
|STSSC. H-1|STSSC. H-1|483|2000|0,4|
|STSSC. H-2|STSSC. H-2|483|2000|0,4|
|STSSC. H-3|STSSC. H-3|483|2000|0,4|
|STSSC. H-4|STSSC. H-4|483|2000|0,4|
|TG. ATS G.J|BLOQUE J|2800|4000|0,4|
|MSA J|MSA J|2800|4000|0,4|
|MDSB J-1|MDSB J-1|264|400|0,4|
|MDSB J-MEC|MDSB J-MEC|605|1200|0,4|
|UDP J-1|UDP J-1|1200|2000|0,4|
|UDP J-2|UDP J-2|1200|2000|0,4|
|STS. J 1.1|STS. J 1.1|483|2000|0,4|
|STS. J 1.2|STS. J 1.2|483|2000|0,4|
|STS. J 1.3|STS. J 1.3|483<br>483<br>483|2000|0,4|
|STS. J 1.4|STS. J 1.4|STS. J 1.4|2000|0,4|
|STSSC. J-1|STSSC. J-1|STSSC. J-1|2000|0,4|
|STSSC. J-2|STSSC. J-2|483|2000|0,4|
|STSSC. J-3|STSSC. J-3|483<br>483|2000|0,4|
|STSSC. J-4|STSSC. J-4|STSSC. J-4|2000|0,4|
|TG. ATS G.P3|BLOQUE P3|2800|4000|0,4|
|MSA P3|MSA P3|2800<br>264|4000|0,4|
|MDSB P3-1|MDSB P3-1|MDSB P3-1|400|0,4|
|MDSB P3-MEC|MDSB P3-MEC|605|1200|0,4|
|UDP P3-1|UDP P3-1|1200|2000|0,4|
|UDP P3-2|UDP P3-2|1200|2000|0,4|
|STS. P3 1.1|STS. P3 1.1|483|2000|0,4|
|STS. P3 1.2|STS. P3 1.2|483|2000|0,4|
|STS. P3 1.3|STS. P3 1.3|483|2000|0,4|
|STS. P3 1.4|STS. P3 1.4|483|2000|0,4|
|STSSC. P3-1|STSSC. P3-1|483|2000|0,4|
|STSSC. P3-2|STSSC. P3-2|483|2000|0,4|
|STSSC. P3-3|STSSC. P3-3|483|2000|0,4|
|STSSC. P3-4|STSSC. P3-4|483|2000|0,4|

**MDC ELECTRICIDAD ST-5-001-RC** **Página 42 de 44**

**MEMORIA DESCRIPTIVA CONCEPTUAL**

**SISTEMA DE ELECTRICIDAD**

**Rev. C**

**Fecha: 14-01-2024**

|NOMBRE|BLOQUE DE ENERGÍA|POTENCIA NOMINAL<br>[KVA]|PROTECCIÓN<br>NOMINAL [A]|TENSIÓN<br>NOMINAL [KV]|
|---|---|---|---|---|
|TG. ATS G.P4|BLOQUE P4|2800|4000|0,4|
|MSA P4|MSA P4|2800|4000|0,4|
|MDSB P4-1|MDSB P4-1|264|400|0,4|
|MDSB P4-MEC|MDSB P4-MEC|605|1200|0,4|
|UDP P4-1|UDP P4-1|1200|2000|0,4|
|UDP P4-2|UDP P4-2|1200|2000|0,4|
|STS. P4 1.1|STS. P4 1.1|483|2000|0,4|
|STS. P4 1.2|STS. P4 1.2|483|2000|0,4|
|STS. P4 1.3|STS. P4 1.3|483|2000|0,4|
|STS. P4 1.4|STS. P4 1.4|483|2000|0,4|
|STSSC. P4-1|STSSC. P4-1|483|2000|0,4|
|STSSC. P4-2|STSSC. P4-2|483|2000|0,4|
|STSSC. P4-3|STSSC. P4-3|483|2000|0,4|
|STSSC. P4-4|STSSC. P4-4|483|2000|0,4|
|TG. ATS G.R1|BLOQUE R1|2800|4000|0,4|
|MSA R1|MSA R1|2800|4000|0,4|
|MDSB R1-1|MDSB R1-1|264|400|0,4|
|MDSB R1-MEC|MDSB R1-MEC|605|1200|0,4|
|UDP R1-1|UDP R1-1|1200|2000|0,4|
|UDP R1-2|UDP R1-2|1200|2000|0,4|
|STS. R1 1.1|STS. R1 1.1|483|2000|0,4|
|STS. R1 1.2|STS. R1 1.2|483|2000|0,4|
|STS. R1 1.3|STS. R1 1.3|483<br>483<br>483|2000|0,4|
|STS. R1 1.4|STS. R1 1.4|STS. R1 1.4|2000|0,4|
|STSSC. R1-1|STSSC. R1-1|STSSC. R1-1|2000|0,4|
|STSSC. R1-2|STSSC. R1-2|483|2000|0,4|
|STSSC. R1-3|STSSC. R1-3|483<br>483|2000|0,4|
|STSSC. R1-4|STSSC. R1-4|STSSC. R1-4|2000|0,4|
|TG. ATS G.R2|BLOQUE R2|2800|4000|0,4|
|MSA R2|MSA R2|2800<br>264|4000|0,4|
|MDSB R2-1|MDSB R2-1|MDSB R2-1|400|0,4|
|MDSB R2-MEC|MDSB R2-MEC|605|1200|0,4|
|UDP R2-1|UDP R2-1|1200|2000|0,4|
|UDP R2-2|UDP R2-2|1200|2000|0,4|
|STS. R2 1.1|STS. R2 1.1|483|2000|0,4|
|STS. R2 1.2|STS. R2 1.2|483|2000|0,4|
|STS. R2 1.3|STS. R2 1.3|483|2000|0,4|
|STS. R2 1.4|STS. R2 1.4|483|2000|0,4|
|STSSC. R2-1|STSSC. R2-1|483|2000|0,4|
|STSSC. R2-2|STSSC. R2-2|483|2000|0,4|
|STSSC. R2-3|STSSC. R2-3|483|2000|0,4|
|STSSC. R2-4|STSSC. R2-4|483|2000|0,4|

**MDC ELECTRICIDAD ST-5-001-RC** **Página 43 de 44**