---
title: MCH EH canal drenaje Nº2 PS Parral
author: Edic Ingeneiros SpA
date: D:20230704220158+00'00'
language: es
type: report
pages: 76
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1. INTRODUCCIÓN
  - 2. ANTECEDENTES
  - 3. DESCRIPCIÓN DEL CIRCUITO HIDRÁULICO SIN Y CON PROYECTO
  - 4. MODELACIÓN HIDRÁULICA
  - 5. RESULTADOS DEL EJE HIDRÁULICO PARA LA SITUACIÓN SIN
  - 6. EJE HIDRÁULICO PARA SITUACIÓN CON PROYECTO
  - 7. ANÁLISIS COMPARATIVO ENTRE SITUACIÓN SIN Y CON
-->

|PARQUE SOLAR PARRAL<br>MEMORIA DE CÁLCULO HIDRÁULICO<br>EJES HIDRÁULICOS SIN Y CON PROYECTO<br>MODIFICACIÓN DE TRAZADO DE CANAL<br>783-22-OT-O0-MC-HI-001|Col2|Col3|
|---|---|---|
||||
||||
|PARA REVISIÓN CLIENTE||B|
|PARA REVISIÓN INTERNA|04.07.2023|A|
|**REVISIÓN**|**FECHA**<br>**REVISIÓN**|**No REVISIÓN**|
||||
|**PREPARÓ**|Jaime García P.|Jaime García P.|
|**REVISÓ**|Roberto Lüders R.|Roberto Lüders R.|
|**APROBÓ**|Roberto Lüders R.|Roberto Lüders R.|

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 2 de 76|

**MEMORIA DE CÁLCULO HIDRÁULICO**

**EJES HIDRÁULICOS SIN Y CON PROYECTO EN MODIFICACIÓN DE**

**TRAZADO DE CANAL**

**TABLA DE CONTENIDOS**

**Pág.**

**1.** **INTRODUCCIÓN ........................................................................................ 1**

**2.** **ANTECEDENTES ......................................................................................... 2**

2.1 ESTUDIO DE PRECIPITACIONES ..................................................... 2

2.2 ESTUDIO DE CRECIDAS ................................................................ 2

2.3 ESTUDIO DE INUNDACIÓN DEL ÁREA DEL PROYECTO ........................ 2

2.4 PROYECTO DE MODIFICACIÓN DE CANALES DE RIEGO Y DRENAJE....... 3

2.5 VISITA A TERRENO ...................................................................... 3

2.6 ANTECEDENTES TOPOGRÁFICOS .................................................... 3

2.6.1 Topografía satelital ALOS ................................................... 3

2.6.2 Levantamiento topográfico ................................................. 4

2.6.3 Levantamiento de cauces naturales y de canales.................... 5
2.6.4 Disposición de obras actualizado ......................................... 6

2.7 ANTECEDENTES GEOTÉCNICOS ..................................................... 7

2.8 ANTECEDENTES BIBLIOGRÁFICOS. ................................................. 8

**3.** **DESCRIPCIÓN** **DEL** **CIRCUITO** **HIDRÁULICO** **SIN** **Y** **CON**

**PROYECTO ............................................................................................... 10**
3.1 SITUACIÓN SIN PROYECTO (ACTUAL) ........................................... 10

3.2 SITUACIÓN CON PROYECTO ........................................................ 11

**4.** **MODELACIÓN HIDRÁULICA .................................................................... 14**
4.1 METODOLOGÍA DE CÁLCULO HIDRÁULICO ..................................... 14

4.2 ELABORACIÓN DEL MODELO HEC-RAS .......................................... 14

4.3 CONDICIONES DE BORDE INICIALES DEL MODELO PARA CÁLCULO DE EJE
HIDRÁULICO............................................................................. 15

4.4 CAUDALES ............................................................................... 15

4.5 GEOMETRÍA .............................................................................. 16

4.6 RUGOSIDAD DE LECHO Y RIBERA ................................................. 16

**5.** **RESULTADOS DEL EJE HIDRÁULICO PARA LA SITUACIÓN SIN**

**PROYECTO ............................................................................................... 18**
5.1 CAUDAL DE CRECIDA T=100 AÑOS............................................... 18

**6.** **EJE HIDRÁULICO PARA SITUACIÓN CON PROYECTO ............................. 23**
6.1 CAUDAL DE CRECIDA T=100 AÑOS............................................... 23

**7.** **ANÁLISIS COMPARATIVO ENTRE SITUACIÓN SIN Y CON**

**PROYECTO ............................................................................................... 28**

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 3 de 76|

**MEMORIA DE CÁLCULO HIDRÁULICO**

**EJES HIDRÁULICOS SIN Y CON PROYECTO EN MODIFICACIÓN DE**

**TRAZADO DE CANAL**

**ANEXOS**

**ANEXO A:** SITUACIÓN SIN PROYECTO - EJES HIDRÁULICOS CRECIDAS DE

PROBABILIDAD DE EXCEDENCIA 95%, 80% Y 60%; Y 2, 5, 10, 20, 50,
100 Y 200 AÑOS DE RETORNO

**ANEXO B:** SITUACIÓN CON PROYECTO - EJES HIDRÁULICOS CRECIDAS DE
PROBABILIDAD DE EXCEDENCIA 95%, 80% Y 60%; Y 2, 5, 10, 20, 50,
100 Y 200 AÑOS DE RETORNO

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 1 de 76|

# 1. INTRODUCCIÓN

En este documento se presenta los ejes hidráulicos sin y con proyecto para el proyecto de
modificación de trazado de un canal catalogado como cauce natural por el IGM. Este cauce
se encuentra al interior del área de panales del proyecto del Parque Solar Parral. Actualmente,
el cauce en estudio se utiliza como canal de drenaje por los agricultores del área, y es

denominado localmente canal de _drenaje N°2_ .

El proyecto Parque Solar Parral consiste en un proyecto de generación fotovoltaica que se

encuentra en una zona rural de la comuna de Retiro, a unos 13 km al noroeste de la ciudad
de Parral, en la Provincia de Linares de la Región del Maule, según se muestra en la Figura

1.1 .

**Figura 1.1: Ubicación aproximada del proyecto Parque Solar Parral**

Los ejes hidráulicos serán determinados de acuerdo con lo indicado en la guía “Trámite PAS
Artículo 157 Reglamento del SEIA”, es decir, para caudales frecuentes de una probabilidad de
excedencia de 95%, 80% y 60% y para las crecidas correspondientes a los distintos períodos
de retorno de 2, 5, 10, 25, 50 y 100 años, como mínimo, en condiciones con y sin proyecto.

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 2 de 76|

# 2. ANTECEDENTES

## 2.1 ESTUDIO DE PRECIPITACIONES

El estudio de precipitaciones en el área del Parque Solar Parral se desarrolló en el Informe
“Estudio de Precipitaciones”, código 783-22-OT-00-IN-HD-001, Edic Ingenieros SpA, enero
2022. Según este documento, las precipitaciones máximas para el área del Proyecto para
## diferentes periodos de retorno son las mostradas en el Cuadro 2.1 :

**Cuadro 2.1: Precipitaciones Máximas Diarias (mm) para distintos períodos de retorno. Área**

**del Proyecto del Parque Solar Parral**

|T|Pmáx [mm]|
|---|---|
|**[años]**|**Área del Proyecto**<br>**del PS Parral**|
|2 <br>5 <br>10<br>25<br>50<br>100<br>200|65<br>88<br>104<br>125<br>142<br>158<br>175|

## 2.2 ESTUDIO DE CRECIDAS

El estudio de crecidas del cauce en estudio ubicado en el área del Parque Solar Parral se
desarrolló en el Informe “Estudio de Crecidas en cuenca afluente a canal catalogado como
cauce natural por el IGM”, código 783-22-OT-00-IN-HD-003, Edic Ingenieros SpA, junio 2023.
Según este documento, las crecidas afluentes al canal en estudio para diferentes periodos de

## retorno son las mostradas en el Cuadro 2.2 :

**Cuadro 2.2: Caudales máximos instantáneos**

|T<br>[años]|Caudal afluente<br>[m3/s]|
|---|---|
|2 <br>5 <br>10<br>20<br>50<br>100|0,15 <br>0,20 <br>0,24 <br>0,30 <br>0,40 <br>0,46|

En el documento señalado, además, se demuestra que el cauce no tiene potencial de flujo

detrítico.

## 2.3 ESTUDIO DE INUNDACIÓN DEL ÁREA DEL PROYECTO

El estudio de inundación del área del Parque Solar Parral se desarrolló en el Informe “Estudio
de Inundación”, código 783-22-OT-00-IN-HI-001, Edic Ingenieros SpA, abril 2022. En este
documento se determinó el área de inundación para la situación sin proyecto para las crecidas

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 3 de 76|

de 100 y 200 años de periodo de retorno, identificando sectores que pudieran afectar el

emplazamiento de los paneles fotovoltaicos, y a partir de estos resultados se propusieron
resultados de modificación de la red actual de canales distribuidos en el área del proyecto.

## 2.4 PROYECTO DE MODIFICACIÓN DE CANALES DE RIEGO Y DRENAJE

El proyecto de modificación de canales de riego y drenaje del área del Parque Solar Parral se
desarrolló en el Informe “Proyecto de modificación de canales de riego y drenaje”, código
783-22-OT-00-IN-HI-002, Edic Ingenieros SpA, julio 2022. En este documento se definieron

una serie de modificaciones a la red de canales de riego y de drenaje que cruzan las parcelas

del PS Parral.

El presente estudio corresponde a la actualización del estudio de inundabilidad, en el cual se

realizaron optimizaciones al layout de canales.

## 2.5 VISITA A TERRENO

El día 17 de marzo de 2022 se realizó la visita a terreno, la cual fue efectuada por los Sres.
Ingenieros Roberto Lüders R. y Jaime García P. de Edic Ingenieros Spa.

## 2.6 ANTECEDENTES TOPOGRÁFICOS

### 2.6.1 Topografía satelital ALOS

Topografía Satelital ALOS para el área de estudio proveída por la Agencia de Exploración
Aeroespacial de Japón, (malla de aprox. 30 m x30 m).

En la Figura 2.1 se muestra la cobertura topográfica satelital en el área del estudio:

**Figura 2.1: Topografía Satelital ALOS - Interpretación GIS**

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 4 de 76|

### 2.6.2 Levantamiento topográfico

El levantamiento topográfico del área del proyecto corresponde a una restitución
aerofotogramétrica Lidar, fue efectuado en escala 1:500, y contiene con curvas de nivel cada

0,5 m.

El levantamiento anterior se complementó en los canales y cauces naturales con un
levantamiento topobatimétrico con perfiles transversales de acuerdo con los siguientes
criterios: 1) En cauces naturales se levantaron perfiles transversales cada 40 m y en los

puntos singulares. 2) En los canales de riego se levantaron perfiles transversales cada 50 m

y en cada punto singular.

Ambos levantamientos fueron efectuados por Quarzo Ingeniería, febrero 2022.

**Figura 2.2: Restitución aerofotogramétrica del proyecto solar**

Adicionalmente a lo anterior el mandante entregó el archivo “DTM_Suavisado.tif”
correspondiente a la topografía del área del proyecto, el cual se muestra en la siguiente figura:

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 5 de 76|

**Figura 2.3: DTM_Suavisado.Tif**

### 2.6.3 Levantamiento de cauces naturales y de canales

Topografía batimétrica del levantamiento de la red de cauces naturales y canales en el área
del proyecto. Los perfiles batimétricos fueron levantados cada 50 m. El cual fue aportado por

el mandante en el archivo “Cauces y canales PS_Parral.dwg”. y se muestra en la siguiente
figura:

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 6 de 76|

**Figura 2.4: Extracto de archivo “Cauces y canales PS_Parral.dwg”**

### 2.6.4 Disposición de obras actualizado

La disposición de obras actualizada se muestra en la Figura 2.5, y fue aportado por el
Mandante mediante el archivo “PSU Parral - modificación canales.kmz”. Se muestra, además,
la disposición actualizada de los canales, en el cual se destaca en color verde aquellos canales
que se mantienen, en color rojo los que serán eliminados y en color violeta los tramos que

tendrán modificaciones.

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 7 de 76|

**Figura 2.5: Layout actualizado del proyecto. (Verde: canales que se mantienen; Rojo:**

**canales que se eliminan; Violeta: canales que se modifican)**

## 2.7 ANTECEDENTES GEOTÉCNICOS

### a. “2.2 Resultados de Análisis Físicos de Muestras por Estratas” Elaborado por

SueloAmbiente Consultores, en agosto del 2022.

Como antecedente de lecho, se cuenta con un análisis de suelo el cuál se realiza para la zona
del parque. A continuación, se muestra la ubicación de las calicatas:

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 8 de 76|

**Figura 2.6: Ubicación calicatas**

El estudio muestra una zona con tipo de suelo cohesivos, en general homogéneo, con suelos
de clase textural Arcillosa/Fco. Arcillosa, compuestos de arena, limo y arcilla.

## 2.8 ANTECEDENTES BIBLIOGRÁFICOS.

Para la elaboración del presente estudio se utilizaron los siguientes antecedentes
bibliográficos:

### Ref.1. Precipitaciones Máximas en 1, 2 y 3 Días”. Dirección General de Aguas del

Ministerio de Obras Públicas, 1991.

### Ref.2. Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas Sin Información

Fluviométrica”. Dirección General de Aguas del Ministerio de Obras Públicas,

1995.

### Ref.3. Hidrología Aplicada, Ven Te Chow, 2001. Ref.4. Estimación de crecidas en cuencas no controladas. Verni, F. y King. H. Tercer

Coloquio Nacional. SOCHID. 1977.

### Ref.5. Manual de Carreteras, Volumen N°3, Instrucciones y Criterios de Diseño. MOP,

marzo 2008.

### Ref.6. Espíldora, B, Brown, E, Isensee, P. y Cabrera, G. Elementos de Hidrología.

Universidad de Chile (1975).

### Ref.7. Guías metodológicas para presentación y revisión técnica de proyectos de

modificación de cauces naturales y artificiales. Ministerio de Obras Públicas.

2016.

### Ref.8. Ven Te Chow (2014). Hidráulica de Canales Abiertos. Ref.9 . Mery, H. (2013). Hidráulica Aplicada al Diseño de Obras.

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 9 de 76|

### Ref.10. Cowan (1956). Estimating Hydraulic Roughness Coefficients. Ref.11. U.S. Department of Interior (1989). Guide for Selecting Manning’s Roughness

Coefficients for Natural Channels and Flood Plains.

### Ref.12 . Barnes (1967). Roughness Characteristics of Natural Channels. Ref.13. U.S. Department of Transportation - Federal Highway Administration (2001).

Evaluation Scour at Bridges. Fourth Edition.

### Ref.14. Diez & Llorente (2009). Mapas de Peligrosidad de Avenidas e Inundaciones.

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 10 de 76|

# 3. DESCRIPCIÓN DEL CIRCUITO HIDRÁULICO SIN Y CON PROYECTO

## 3.1 SITUACIÓN SIN PROYECTO (ACTUAL)

Actualmente el cauce en estudio (canal de drenaje N°2) tiene un trazado que va de oriente a

poniente, dividiendo la parcela 5 y descargando al canal de drenaje N°3 en un punto ubicado

650 m aguas abajo de su inicio.

El inicio del cauce en estudio (km 0) se ubica a la derecha del canal Intrapredial N°9, el cual
portea aguas en la dirección Sur a Norte con un trazado que corresponde a la divisoria de

predios.

El cauce en estudio capta aguas producto de afloramiento de infiltraciones del predio ubicado

al oriente del canal Intrapredial N°9.

En el siguiente cuadro se muestran las coordenadas de referencia del punto de inicio y término

del cauce en estudio:

**Cuadro 3.1: Vértices del cauce en estudio (canal de drenaje N°2)**

|Vértice N°|Observación|Este<br>[m]|Norte<br>[m]|
|---|---|---|---|
|1|Inicio Cauce existente (canal drenaje N°2)|236.699|6.004.015|
|2|Conexión cauce en estudio con canal de drenaje N°3|236.329|6.004.500|
|3|100 m aguas abajo de conexión cauce en estudio y<br>canal de drenaje N°3|236.303|6.004.581|

La descripción y vértices indicados se puede observar en la siguiente figura, en la cual se

muestra en rojo el trazado del cauce en estudio, en verde el trazado del canal de drenaje N°3

y en amarillo el canal Intrapredial N°9:

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 11 de 76|

**V3**

**V2**

**Canal Drenaje N°3**

**Cauce natural**
**(localmente Canal Drenaje 2)**

**Trazado actual**

**V1**

**Figura 3.1: Vista general de la situación sin proyecto**

## 3.2 SITUACIÓN CON PROYECTO

A continuación, en la siguiente figura se muestra la situación con proyecto:

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 12 de 76|

**V5**

**V4**

**Canal Drenaje N°3**

**V3**

**V6**

**V1**

**Figura 3.2: Vista general de la situación con proyecto**

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 13 de 76|

**De acuerdo con lo mostrado en la Figura 3.2**

**Figura 3.2: Vista general de la situación con proyecto**

, se proyecta el desvío de un tramo del cauce existente (drenaje N°2) hacia el canal de drenaje

N°3, el nuevo trazado tiene como objetivo conducir el agua del cauce existente y transportarla
hacia el canal de drenaje N°3 para, desde allí sea conducida en la dirección hacia aguas abajo.

Actualmente el canal de drenaje N°3 empalma con el cauce en estudio en un punto ubicado
aguas abajo (V3) y será desplazado aproximadamente 290 m aguas arriba (V2), desde el
nuevo punto de empalme se conduce las aguas conjuntas en dirección hacia aguas abajo.

El tramo del cauce existente que quedará en desuso será rellenado y nivelado.

En el siguiente cuadro se muestra las coordenadas del proyecto de modificación del canal:

**Cuadro 3.2: Vértices - situación con proyecto**

|Vértice N°|Observación|Este<br>[m]|Norte<br>[m]|
|---|---|---|---|
|1|~~Inicio Cauce existente (canal drenaje N°2)~~|236.699|6.004.015|
|2|Inicio tramo proyectado|236.681|6.004.062|
|3|Fin nuevo tramo proyectado<br>Conexión con canal de drenaje N°3|236.593|6.004.378|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 14 de 76|

|Vértice N°|Observación|Este<br>[m]|Norte<br>[m]|
|---|---|---|---|
|4|Conexión de la situación sin proyecto del cauce en<br>estudio con canal de drenaje N°3<br>|236.329|6.004.500|
|5|~~100 m aguas abajo de conexión de la situación sin~~<br>proyecto del cauce en estudio y canal de drenaje N°3|236.303|6.004.581|
|6|160 m aguas arriba desde la conexión del nuevo<br>tramo de canal y canal de drenaje N°3|236.739|6.004.317|

El nuevo tramo de canal tiene aproximadamente 350 m de longitud, pendiente 0,001 m/m.
El caudal de diseño del canal es 460 l/s. Sección transversal trapecial. Este canal sería
excavado en el suelo y revestido con hormigón, presentando un ancho basal de 0,60 metros,
una altura variable de 0,65 a 1,00 metros y taludes en proporción de 3H:2V.

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 15 de 76|

# 4. MODELACIÓN HIDRÁULICA

## 4.1 METODOLOGÍA DE CÁLCULO HIDRÁULICO

 **Ecuación de Energía**

_ZB_ = _ZF_ + _B_

_ZB_ 1 = _ZB_ 2 +  ( _hf_ +  _hs_ )

Donde:

_ZF_ = cota de fondo del canal (m s.n.m.)

_B_ = _H_ + _h_ _v_ Bernoulli con respecto al fondo (m)

_h_ _v_ = _V_ [2 ] / 2 _g_ altura de velocidad del flujo (m)

_V_ = _Q_ / _A_ velocidad media del flujo (m/s)

_A_ = área mojada del canal (m2)

 - **Ecuaciones para las pérdidas de carga singulares:**

En el caso de un ensanche la pérdida de carga singular se puede calcular con la ecuación
de Borda:

 _h_ _e_ = _K_ _e_ x ( _V_ 1 - _V_ 2 ) [2] / _2g_

En el caso de un angostamiento se puede calcular con la ecuación:

 _h_ _a_ = _K_ _a_ x _V_ 2 [2] / 2 _g_

## 4.2 ELABORACIÓN DEL MODELO HEC-RAS

Para determinar las condiciones hidráulicas en los ríos estudiados, se analizó el eje hidráulico
unidimensional (1D) integrado en toda su extensión. Para ello se utilizará el software HecRas.

En los acápites siguientes se muestra la metodología utilizada y los resultados del cálculo del
eje hidráulico para las condiciones actual y proyectada, para diferentes caudales.

Los cuadros presentados en los puntos siguientes y anexos contienen parámetros abreviados

de acuerdo con la nomenclatura mostrada en el cuadro siguiente:

**Cuadro 4.1 Nomenclatura de resultados ejes hidráulicos**

River Station : Perfil Transversal (mayor valor desde aguas arriba)

Q : Caudal total [m [3] /s]

Min Ch El : Cota de Fondo [m s.n.m.]

W.S. Elev. : Cota eje hidráulico [m s.n.m.]

Crit. W.S. : Cota escurrimiento crítico [m s.n.m.]

E.G. Elev. : Pendiente de la línea de energía [m/m]

E.G. Slope : Gradiente hidráulico [m/m]

Vel Chnl. : Velocidad media de escurrimiento [m/s]

Flow Área : Área del flujo [m [2] ]

Top Width : Ancho superficial del escurrimiento [m]

Fr : No de Froude [-].

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 16 de 76|

## 4.3 CONDICIONES DE BORDE INICIALES DEL MODELO PARA CÁLCULO DE EJE

**HIDRÁULICO**

Para efectos del modelamiento en Hec-Ras se ha considerado un régimen mixto, por lo que
se establecerán condiciones de borde iniciales por aguas arriba y por aguas abajo, dado la
baja pendiente del cauce se adoptarán las siguientes condiciones de escurrimiento

seudonormal:

- En el extremo de aguas abajo se considera escurrimiento seudonormal para una pendiente

de cauce i=0,006.

En el extremo de aguas arriba se adoptará escurrimiento crítico, cabe señalar que esta es
una condición inicial para el cálculo, la cual se modifica una vez ejecutada la simulación.

## 4.4 CAUDALES

Los ejes hidráulicos serán determinados para los caudales indicados en el Cuadro 2.2 . además

de los correspondientes a las probabilidades de excedencia 95%, 80% y 60%.

Para determinar las crecidas de las probabilidades de excedencia se considerará extrapolación
semilogarítmica a partir de los caudales del Cuadro 2.2 . adoptando, además, la relación

_P_ _ex_ =1/ _T_ . Resultando los siguientes caudales:

**Cuadro 4.2: Caudales en cauce en estudio**

|T<br>[años]|Probabilidad de<br>Caudal afluente<br>excedencia<br>[m3/s]<br>[%]|Col3|
|---|---|---|
|1,05<br>1,25<br>1,67<br>2 <br>5 <br>10<br>25<br>50<br>100|~~0,95~~<br>0,80<br>0,60<br>0,50<br>0,20<br>0,10<br>0,04<br>0,02<br>0,01|0,11 <br>0,12 <br>0,14 <br>0,15 <br>0,20 <br>0,24 <br>0,31 <br>0,40 <br>0,46|

Adicionalmente a lo anterior, los caudales afluentes al canal drenaje N°3 se determinan
aplicando transposición de caudales contemplando igualdad de rendimiento. Dado que la
cuenca afluente al cauce natural en estudio tiene un área aportante de 0,22 km2 y que la
cuenca afluente al canal de drenaje N°3 cuenta con 0,14 km2 de cuenca aportante. Y que
ambas cuencas están una al costado de la otra, se asume igualdad de precipitación.

Resultando las siguientes crecidas:

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 17 de 76|

**Cuadro 4.3: Crecidas [m3/s]**

|T<br>[años]|Probabilidad de Caudal afluente Caudal afluente<br>excedencia Cauce en estudio Canal Drenaje<br>(Drenaje N°2) N°3<br>[m3/s] [m3/s]|Col3|Col4|
|---|---|---|---|
|1,05<br>1,25<br>1,67<br>2 <br>5 <br>10<br>25<br>50<br>100|0,95<br>0,80<br>0,60<br>0,50<br>0,20<br>0,10<br>0,04<br>0,02<br>0,01|0,11 <br>0,12 <br>0,14 <br>0,15 <br>0,20 <br>0,24 <br>0,31 <br>0,40 <br>0,46|0,07<br>0,07<br>0,09<br>0,10<br>0,13<br>0,15<br>0,20<br>0,25<br>0,29|

## 4.5 GEOMETRÍA

Para la elaboración del modelo Hec-Ras unidimensional (1D) se utilizaron los perfiles
transversales topobatimétricos levantados en la campaña de terreno señalada en el

antecedente 2.6.3.

## 4.6 RUGOSIDAD DE LECHO Y RIBERA

Para la rugosidad del lecho se considera lo observado en terreno, sumado a la experiencia del

consultor, permite adoptar los siguientes valores del coeficiente de rugosidad de Manning:

**Cuadro 4.4: Coeficientes de rugosidad de Manning en canales de tierra (Mery, 2013)**

**(En verde los valores utilizados)**

|Descripción|Mínimo|Medio|Máximo|
|---|---|---|---|
|Con musgos y pastos<br>|0,025|0,030|0,033|
|~~Fondo pedregoso y taludes con~~<br>vegetación|0,025|0,035|0,040|
|Sin vegetación|0,025|0,028|0,033|
|Hormigón liso||0,016||

A continuación, se muestran fotografías de terreno, representativas de los coeficientes de
rugosidad considerados.

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 18 de 76|

a) Fondo pedregoso y taludes con vegetación ( _n_ =0,035)

**Figura 4.1: Imagen representativa del coeficiente de rugosidad en canales de tierra**

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 19 de 76|

# 5. RESULTADOS DEL EJE HIDRÁULICO PARA LA SITUACIÓN SIN

**PROYECTO**

En el actual numeral se indica para el escenario actual (sin proyecto) el eje hidráulico
determinado para la crecida de 100 años de retorno, en el apéndice A, se incluyen los ejes
hidráulicos asociados a las crecidas de 2, 5, 10, 20, y 50 años y para los caudales asociados

a las probabilidades de excedencia 95%, 80% y 60%

## 5.1 CAUDAL DE CRECIDA T=100 AÑOS

A continuación, se presentan los resultados del eje hidráulico para la situación sin proyecto

considerando la crecida de 100 años de retorno:

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 20 de 76|

**Cuadro 5.1: Eje hidráulico - Situación Sin Proyecto (T=100 años)**

|Cauce|Tramo|Km<br>[m]|River<br>Sta|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S. Elev<br>[m snm]|Crit W.S.<br>[m snm]|E.G. Elev<br>[m snm]|E.G.<br>Slope<br>[m/m]|Vel<br>Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=100|0,46|144,50|145,11|144,82|145,12|0,00088|0,57|1,06|3,09|0,24|
|D2|arriba junta|59,77|11,794|T=100|0,46|144,48|145,09|144,81|145,10|0,00094|0,59|1,06|3,24|0,25|
|D2|arriba junta|79,77|11,589|T=100|0,46|144,47|145,07|144,79|145,08|0,00100|0,60|1,05|3,36|0,26|
|D2|arriba junta|99,8|11,383|T=100|0,46|144,45|145,05|144,78|145,06|0,00105|0,61|1,06|3,64|0,27|
|D2|arriba junta|119,84|11,178|T=100|0,46|144,43|145,03|144,76|145,04|0,00096|0,58|1,08|3,38|0,25|
|D2|arriba junta|137,16|11|T=100|0,46|144,42|145,01|144,75|145,03|0,00097|0,58|1,06|3,25|0,25|
|D2|arriba junta|157,14|10,755|T=100|0,46|144,34|144,99|144,71|145,01|0,00097|0,61|1,09|3,62|0,25|
|D2|arriba junta|177,14|10,51|T=100|0,46|144,27|144,97|144,66|144,99|0,00095|0,61|1,08|3,46|0,24|
|D2|arriba junta|197,15|10,265|T=100|0,46|144,19|144,96|144,61|144,97|0,00097|0,60|1,04|2,96|0,23|
|D2|arriba junta|217,16|10,02|T=100|0,46|144,12|144,93|144,58|144,95|0,00108|0,58|0,97|2,45|0,23|
|D2|arriba junta|218,76|10|T=100|0,46|144,11|144,93|144,58|144,95|0,00110|0,58|0,97|2,42|0,23|
|D2|arriba junta|238,71|9,6435|T=100|0,46|144,09|144,92|144,51|144,93|0,00064|0,50|1,17|2,84|0,20|
|D2|arriba junta|258,85|9,287|T=100|0,46|144,07|144,91|144,46|144,92|0,00041|0,42|1,39|3,57|0,17|
|D2|arriba junta|274,9|9|T=100|0,46|144,05|144,91|144,42|144,91|0,00023|0,32|2,08|7,64|0,13|
|D2|arriba junta|294,69|8,7528|T=100|0,46|144,04|144,90|144,43|144,91|0,00033|0,38|1,54|3,87|0,15|
|D2|arriba junta|314,91|8,5056|T=100|0,46|144,04|144,89|144,43|144,90|0,00037|0,40|1,48|3,80|0,16|
|D2|arriba junta|335|8,2583|T=100|0,46|144,03|144,88|144,44|144,89|0,00043|0,42|1,42|3,48|0,16|
|D2|arriba junta|354,94|8,0111|T=100|0,46|144,02|144,87|144,45|144,88|0,00052|0,43|1,35|3,43|0,17|
|D2|arriba junta|355,82|8|T=100|0,46|144,02|144,87|144,45|144,88|0,00052|0,43|1,35|3,43|0,17|
|D2|arriba junta|375,18|7,775|T=100|0,46|144,07|144,86|144,50|144,87|0,00064|0,49|1,26|3,43|0,19|
|D2|arriba junta|395,64|7,5501|T=100|0,46|144,12|144,85|144,54|144,85|0,00080|0,55|1,16|3,43|0,22|
|D2|arriba junta|416,02|7,3251|T=100|0,46|144,18|144,82|144,57|144,84|0,00107|0,61|1,06|3,42|0,25|
|D2|arriba junta|435,99|7,1001|T=100|0,46|144,23|144,80|144,59|144,81|0,00158|0,68|0,94|3,37|0,31|
|D2|arriba junta|444,77|7|T=100|0,46|144,25|144,78|144,60|144,79|0,00198|0,72|0,87|3,32|0,34|
|D2|arriba junta|464,76|6,7923|T=100|0,46|144,18|144,74|144,56|144,75|0,00201|0,76|0,83|3,02|0,35|
|D2|arriba junta|485,72|6,5846|T=100|0,46|144,12|144,69|144,51|144,71|0,00201|0,79|0,81|2,75|0,35|
|D2|arriba junta|505,61|6,3769|T=100|0,46|144,05|144,65|144,46|144,67|0,00198|0,78|0,79|2,53|0,34|
|D2|arriba junta|524,94|6,1693|T=100|0,46|143,98|144,61|144,39|144,63|0,00195|0,77|0,78|2,33|0,33|
|D2|arriba junta|541,11|6|T=100|0,46|143,93|144,58|144,34|144,60|0,00194|0,75|0,77|2,19|0,33|
|D2|arriba junta|560,93|5,7904|T=100|0,46|143,92|144,55|144,30|144,57|0,00175|0,74|0,79|2,27|0,33|
|D2|arriba junta|580,98|5,5807|T=100|0,46|143,90|144,51|144,26|144,53|0,00154|0,71|0,83|2,37|0,31|
|D2|arriba junta|601,4|5,3711|T=100|0,46|143,89|144,49|144,22|144,50|0,00131|0,67|0,88|2,51|0,29|
|D2|arriba junta|621,65|5,1614|T=100|0,46|143,87|144,46|144,18|144,48|0,00107|0,62|0,95|2,74|0,27|
|D2|arriba junta|636,55|5|T=100|0,46|143,86|144,45|144,15|144,46|0,00091|0,58|1,03|3,05|0,25|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 21 de 76|

|Cauce|Tramo|Km<br>[m]|River<br>Sta|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S. Elev<br>[m snm]|Crit W.S.<br>[m snm]|E.G. Elev<br>[m snm]|E.G.<br>Slope<br>[m/m]|Vel<br>Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|647,85|4|T=100|0,46|143,91|144,44|144,20|144,45|0,00125|0,59|0,90|2,61|0,28|
|D3|arriba junta|0|9|T=100|0,29|144,95|145,21|145,12|145,22|0,00252|0,55|0,66|4,00|0,36|
|D3|arriba junta|19,85|8,7368|T=100|0,29|144,81|145,16|145,06|145,17|0,00235|0,65|0,61|3,56|0,37|
|D3|arriba junta|39,67|8,4737|T=100|0,29|144,68|145,11|144,94|145,13|0,00209|0,73|0,57|3,07|0,36|
|D3|arriba junta|59,49|8,2105|T=100|0,29|144,54|145,05|144,84|145,08|0,00240|0,88|0,46|2,10|0,40|
|D3|arriba junta|75,33|8|T=100|0,29|144,43|144,99|144,79|145,04|0,00313|1,07|0,36|1,19|0,46|
|D3|arriba junta|95,39|7,759|T=100|0,29|144,39|144,93|0,00|144,97|0,00314|1,04|0,42|2,26|0,46|
|D3|arriba junta|115,46|7,5181|T=100|0,29|144,36|144,88|0,00|144,91|0,00249|0,92|0,48|2,21|0,41|
|D3|arriba junta|135,52|7,2771|T=100|0,29|144,32|144,85|0,00|144,87|0,00172|0,77|0,57|2,38|0,34|
|D3|arriba junta|155,6|7,0361|T=100|0,29|144,29|144,83|0,00|144,84|0,00109|0,62|0,70|2,69|0,27|
|D3|arriba junta|158,61|7|T=100|0,29|144,28|144,82|0,00|144,83|0,00102|0,60|0,72|2,75|0,26|
|D3|arriba junta|198,72|6,42|T=100|0,29|144,22|144,79|0,00|144,81|0,00142|0,65|0,58|2,18|0,29|
|D3|arriba junta|218,77|6,18|T=100|0,29|144,20|144,75|0,00|144,78|0,00195|0,70|0,49|1,76|0,33|
|D3|arriba junta|237,8|6|T=100|0,29|144,17|144,71|144,52|144,73|0,00270|0,74|0,43|1,31|0,37|
|D3|arriba junta|257,8|5,802|T=100|0,29|144,13|144,65|144,47|144,68|0,00258|0,73|0,43|1,35|0,37|
|D3|arriba junta|277,79|5,604|T=100|0,29|144,10|144,60|144,42|144,63|0,00245|0,72|0,44|1,40|0,36|
|D3|arriba junta|297,78|5,4059|T=100|0,29|144,06|144,56|144,37|144,58|0,00223|0,70|0,46|1,46|0,35|
|D3|arriba junta|317,75|5,2079|T=100|0,29|144,02|144,52|144,32|144,54|0,00197|0,67|0,49|1,54|0,33|
|D3|arriba junta|337,72|5,0099|T=100|0,29|143,98|144,48|144,27|144,50|0,00164|0,62|0,53|1,63|0,31|
|D3|arriba junta|338,72|5|T=100|0,29|143,98|144,48|144,27|144,50|0,00162|0,62|0,53|1,63|0,31|
|D3|arriba junta|358,41|4,8131|T=100|0,29|143,91|144,46|144,17|144,48|0,00086|0,51|0,66|1,91|0,23|
|D3|arriba junta|378,39|4,6262|T=100|0,29|143,83|144,46|144,08|144,46|0,00046|0,41|0,86|2,45|0,17|
|D3|arriba junta|398,88|4,4393|T=100|0,29|143,76|144,45|144,00|144,46|0,00026|0,34|1,06|2,59|0,13|
|D3|arriba junta|420,1|4,2523|T=100|0,29|143,69|144,45|143,91|144,45|0,00016|0,29|1,24|2,51|0,11|
|D3|arriba junta|440,31|4,0654|T=100|0,29|143,62|144,44|143,83|144,45|0,00012|0,26|1,35|2,30|0,09|
|D3|arriba junta|445,94|4|T=100|0,29|143,59|144,44|143,81|144,45|0,00011|0,26|1,37|2,20|0,09|
|D3|bajo junta|452,26|3|T=100|0,75|143,95|144,42|144,23|144,44|0,00176|0,67|1,46|6,20|0,33|
|D3|bajo junta|471,1|2|T=100|0,75|143,64|144,39|144,06|144,41|0,00139|0,74|1,28|3,02|0,30|
|D3|bajo junta|491,09|1,6942|T=100|0,75|143,66|144,36|144,08|144,38|0,00154|0,81|1,26|3,58|0,32|
|D3|bajo junta|511,09|1,3884|T=100|0,75|143,68|144,32|144,10|144,35|0,00186|0,83|1,18|3,85|0,35|
|D3|bajo junta|531,1|1,0826|T=100|0,75|143,70|144,25|144,10|144,30|0,00360|0,99|0,96|4,30|0,47|
|D3|bajo junta|536,51|1|T=100|0,75|143,71|144,21|144,11|144,27|0,00601|1,16|0,78|3,79|0,60|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 22 de 76|

**Figura 5.1: Eje Hidráulico situación Sin Proyecto - Canal Drenaje N°3 (T=100 años)**

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 23 de 76|

**Figura 5.2: Eje Hidráulico situación Sin Proyecto - Cauce en estudio (Drenaje N°2) (T=100 años)**

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 24 de 76|

# 6. EJE HIDRÁULICO PARA SITUACIÓN CON PROYECTO

En el actual numeral se indica para el escenario proyectado (con proyecto) el eje hidráulico
determinado para la crecida de 100 años de retorno, en el apéndice A, se incluyen los ejes
hidráulicos asociados a las crecidas de 2, 5, 10, 20, y 50 años y para los caudales asociados

a las probabilidades de excedencia 95%, 80% y 60%

## 6.1 CAUDAL DE CRECIDA T=100 AÑOS

A continuación, se presentan los resultados del eje hidráulico para la situación con proyecto

considerando la crecida de 100 años de retorno:

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 25 de 76|

**Cuadro 6.1: Eje hidráulico - Situación Con Proyecto (T=100 años)**

|Cauce|Tramo|Km<br>[m]|River<br>Sta|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S. Elev<br>[m snm]|Crit W.S.<br>[m snm]|E.G. Elev<br>[m snm]|E.G.<br>Slope<br>[m/m]|Vel<br>Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=100|0,46|144,50|145,15|144,82|145,16|0,00063|0,51|1,21|3,30|0,21|
|D2|arriba junta|61,4|11|T=100|0,46|144,63|145,13|0,00|145,15|0,00037|0,76|0,77|2,30|0,34|
|D2|arriba junta|81,4|10,722|T=100|0,46|144,61|145,12|0,00|145,14|0,00033|0,73|0,80|2,34|0,33|
|D2|arriba junta|101,4|10,444|T=100|0,46|144,59|145,12|0,00|145,14|0,00030|0,70|0,84|2,38|0,31|
|D2|arriba junta|121,4|10,167|T=100|0,46|144,57|145,11|0,00|145,13|0,00026|0,67|0,88|2,43|0,29|
|D2|arriba junta|133,4|10|T=100|0,46|144,56|145,11|0,00|145,13|0,00025|0,66|0,90|2,46|0,28|
|D2|arriba junta|153,4|9,8601|T=100|0,46|144,54|145,11|0,00|145,12|0,00022|0,63|0,94|2,51|0,27|
|D2|arriba junta|173,4|9,7203|T=100|0,46|144,52|145,10|0,00|145,12|0,00019|0,61|0,98|2,56|0,25|
|D2|arriba junta|193,4|9,5804|T=100|0,46|144,50|145,10|0,00|145,11|0,00017|0,59|1,03|2,61|0,24|
|D2|arriba junta|213,4|9,4406|T=100|0,46|144,48|145,10|0,00|145,11|0,00015|0,56|1,07|2,66|0,23|
|D2|arriba junta|233,4|9,3007|T=100|0,46|144,46|145,10|0,00|145,11|0,00014|0,54|1,12|2,71|0,22|
|D2|arriba junta|253,4|9,1608|T=100|0,46|144,44|145,10|0,00|145,11|0,00012|0,52|1,17|2,77|0,20|
|D2|arriba junta|273,4|9,021|T=100|0,46|144,42|145,09|0,00|145,10|0,00011|0,50|1,22|2,82|0,19|
|D2|arriba junta|276,4|9|T=100|0,46|144,42|145,09|0,00|145,10|0,00011|0,50|1,23|2,83|0,19|
|D2|arriba junta|296,4|8,8519|T=100|0,46|144,40|145,09|0,00|145,10|0,00010|0,48|1,28|2,89|0,18|
|D2|arriba junta|316,4|8,7037|T=100|0,46|144,38|145,09|0,00|145,10|0,00009|0,46|1,34|2,94|0,17|
|D2|arriba junta|336,4|8,5556|T=100|0,46|144,36|145,09|0,00|145,10|0,00008|0,44|1,39|3,00|0,17|
|D2|arriba junta|356,4|8,4074|T=100|0,46|144,34|145,09|0,00|145,09|0,00007|0,43|1,45|3,06|0,16|
|D2|arriba junta|376,4|8,2593|T=100|0,46|144,31|145,09|0,00|145,09|0,00006|0,41|1,51|3,12|0,15|
|D2|arriba junta|396,4|8,1111|T=100|0,46|144,30|145,09|0,00|145,09|0,00006|0,40|1,57|3,17|0,14|
|D2|arriba junta|411,4|8|T=100|0,46|144,28|145,09|144,56|145,09|0,00005|0,39|1,62|3,22|0,14|
|D3|arriba junta|0|9|T=100|0,29|144,95|145,22|145,12|145,23|0,00210|0,51|0,70|4,05|0,33|
|D3|arriba junta|19,85|8,7368|T=100|0,29|144,81|145,18|145,06|145,19|0,00158|0,57|0,70|3,71|0,30|
|D3|arriba junta|39,67|8,4737|T=100|0,29|144,68|145,16|144,94|145,17|0,00114|0,58|0,72|3,31|0,27|
|D3|arriba junta|59,49|8,2105|T=100|0,29|144,54|145,13|144,84|145,14|0,00114|0,67|0,64|2,46|0,28|
|D3|arriba junta|75,33|8|T=100|0,29|144,43|145,11|144,79|145,13|0,00092|0,66|0,77|3,60|0,26|
|D3|arriba junta|95,39|7,759|T=100|0,29|144,39|145,10|0,00|145,11|0,00056|0,53|0,96|3,97|0,20|
|D3|arriba junta|115,46|7,5181|T=100|0,29|144,36|145,10|0,00|145,10|0,00034|0,43|1,18|4,39|0,16|
|D3|arriba junta|135,52|7,2771|T=100|0,29|144,32|145,09|0,00|145,10|0,00022|0,35|1,46|5,22|0,13|
|D3|arriba junta|155,6|7,0361|T=100|0,29|144,29|145,09|0,00|145,09|0,00014|0,29|1,78|6,00|0,10|
|D3|arriba junta|158,61|7|T=100|0,29|144,28|145,09|144,54|145,09|0,00013|0,28|1,83|6,10|0,10|
|D3|bajo junta|178,67|6,9|T=100|0,75|144,28|145,08|0,00|145,09|0,00096|0,76|1,75|5,84|0,27|
|D3|bajo junta|198,72|6,42|T=100|0,75|144,22|145,02|0,00|145,04|0,00152|0,86|1,60|8,42|0,32|
|D3|bajo junta|218,77|6,18|T=100|0,75|144,19|144,99|0,00|145,01|0,00160|0,83|1,58|8,53|0,32|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 26 de 76|

|Cauce|Tramo|Km<br>[m]|River<br>Sta|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S. Elev<br>[m snm]|Crit W.S.<br>[m snm]|E.G. Elev<br>[m snm]|E.G.<br>Slope<br>[m/m]|Vel<br>Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|bajo junta|237,8|6|T=100|0,75|144,17|144,96|144,71|144,98|0,00182|0,84|1,44|7,41|0,33|
|D3|bajo junta|257,8|5,802|T=100|0,75|144,13|144,89|144,66|144,94|0,00276|1,03|0,97|3,61|0,41|
|D3|bajo junta|277,79|5,604|T=100|0,75|144,10|144,83|144,60|144,88|0,00287|1,05|0,94|3,45|0,42|
|D3|bajo junta|297,78|5,4059|T=100|0,75|144,06|144,77|144,55|144,82|0,00306|1,08|0,90|3,21|0,44|
|D3|bajo junta|317,75|5,2079|T=100|0,75|144,02|144,70|144,50|144,76|0,00344|1,12|0,84|2,86|0,47|
|D3|bajo junta|337,72|5,0099|T=100|0,75|143,98|144,62|144,44|144,68|0,00416|1,19|0,76|2,31|0,51|
|D3|bajo junta|338,72|5|T=100|0,75|143,98|144,61|144,44|144,67|0,00419|1,19|0,76|2,28|0,51|
|D3|bajo junta|358,41|4,8131|T=100|0,75|143,91|144,55|144,34|144,60|0,00325|1,09|0,85|2,57|0,46|
|D3|bajo junta|378,39|4,6262|T=100|0,75|143,83|144,50|144,25|144,54|0,00223|0,95|0,98|2,69|0,39|
|D3|bajo junta|398,88|4,4393|T=100|0,75|143,76|144,47|144,16|144,50|0,00150|0,83|1,12|2,67|0,33|
|D3|bajo junta|420,1|4,2523|T=100|0,75|143,69|144,45|144,07|144,47|0,00105|0,74|1,25|2,52|0,28|
|D3|bajo junta|440,31|4,0654|T=100|0,75|143,62|144,43|143,99|144,46|0,00081|0,69|1,32|2,28|0,25|
|D3|bajo junta|445,94|4|T=100|0,75|143,59|144,43|143,96|144,45|0,00075|0,68|1,34|2,18|0,24|
|D3|bajo junta|452,26|3|T=100|0,75|143,95|144,42|144,23|144,44|0,00176|0,67|1,46|6,20|0,33|
|D3|bajo junta|471,1|2|T=100|0,75|143,64|144,39|144,06|144,41|0,00139|0,74|1,28|3,02|0,30|
|D3|bajo junta|491,09|1,6942|T=100|0,75|143,66|144,36|144,08|144,38|0,00154|0,81|1,26|3,58|0,32|
|D3|bajo junta|511,09|1,3884|T=100|0,75|143,68|144,32|144,10|144,35|0,00186|0,83|1,18|3,85|0,35|
|D3|bajo junta|531,1|1,0826|T=100|0,75|143,70|144,25|144,10|144,30|0,00360|0,99|0,96|4,30|0,47|
|D3|bajo junta|536,51|1|T=100|0,75|143,71|144,21|144,11|144,27|0,00601|1,16|0,78|3,79|0,60|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 27 de 76|

**Figura 6.1: Eje Hidráulico situación Con Proyecto - Canal Drenaje N°3 (T=100 años)**

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 28 de 76|

**Figura 6.2: Eje Hidráulico situación Con Proyecto - Cauce en estudio (Drenaje N°2) (T=100 años)**

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 29 de 76|

# 7. ANÁLISIS COMPARATIVO ENTRE SITUACIÓN SIN Y CON

**PROYECTO**

Para determinar adecuadamente el impacto del cambio en el trazado del cauce en
estudio, se mostrará gráficamente la altura de escurrimiento de la crecida de 100 años
para los escenarios sin y con proyecto del tramo afectado por dicha modificación, este
tramo corresponde al canal denominado drenaje N°3, el tramo afectado está

comprendido desde el nuevo empalme proyectado hasta el empalme con el cauce natural
existente. Se analizará al menos 100 m aguas arriba y aguas abajo de dichos extremos.

En el siguiente cuadro se muestra la altura de aguas sin y con proyecto para la crecida

de 100 años:

**Cuadro 7.1: Eje hidráulico - Comparativa Sin v/s Con Proyecto (T=100 años)**

|Perfil<br>HecRas|X<br>[m]|Cota de<br>fondo<br>[m s.n.m.]|Cota aguas Sin<br>Proyecto<br>[m s.n.m.]|Cota aguas<br>Con Proyecto<br>[m s.n.m.]|Diferencia<br>[m]|
|---|---|---|---|---|---|
|9|0|144,95|145,21|145,22|0,01|
|8,7368*|19,85|144,81|145,16|145,18|0,02|
|8,4737*|39,67|144,68|145,11|145,16|0,05|
|8,2105*|59,49|144,54|145,05|145,13|0,08|
|8|75,33|144,43|144,99|145,11|0,12|
|7,759*|95,39|144,39|144,93|145,10|0,17|
|7,5181*|115,46|144,36|144,88|145,10|0,22|
|7,2771*|135,52|144,32|144,85|145,09|0,24|
|7,0361*|155,6|144,29|144,83|145,09|0,26|
|7 <br>Conexión<br>Proyectada|158,61|144,28|144,82|145,09|0,27|
|6,42*|198,72|144,22|144,79|145,02|0,23|
|6,18*|218,77|144,19|144,75|144,99|0,24|
|6|237,8|144,17|144,71|144,96|0,25|
|5,802*|257,8|144,13|144,65|144,89|0,24|
|5,604*|277,79|144,10|144,60|144,83|0,23|
|5,4059*|297,78|144,06|144,56|144,77|0,21|
|5,2079*|317,75|144,02|144,52|144,70|0,18|
|5,0099*|337,72|143,98|144,48|144,62|0,14|
|5|338,72|143,98|144,48|144,61|0,13|
|4,8131*|358,41|143,91|144,46|144,55|0,09|
|4,6262*|378,39|143,83|144,46|144,50|0,04|
|4,4393*|398,88|143,76|144,45|144,47|0,02|
|4,2523*|420,1|143,69|144,45|144,45|0,00|
|4,0654*|440,31|143,62|144,44|144,43|-0,01|
|4|445,94|143,59|144,44|144,43|-0,01|
|3 <br>Conexión Actual|452,26|143,95|144,42|144,42|0,00|
|2|471,1|143,64|144,39|144,39|0,00|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 30 de 76|

|Perfil<br>HecRas|X<br>[m]|Cota de<br>fondo<br>[m s.n.m.]|Cota aguas Sin<br>Proyecto<br>[m s.n.m.]|Cota aguas<br>Con Proyecto<br>[m s.n.m.]|Diferencia<br>[m]|
|---|---|---|---|---|---|
|1,6942*|491,09|143,66|144,36|144,36|0,00|
|1,3884*|511,09|143,68|144,32|144,32|0,00|
|1,0826*|531,1|143,70|144,25|144,25|0,00|
|1|536,51|143,71|144,21|144,21|0,00|

***:** perfil interpolado en HecRas.

En el cuadro anterior se observa el incremento del nivel del agua a partir del km 0+400,
es decir aproximadamente 50 m aguas arriba del punto actual de conexión entre los dos
cauces (sin proyecto), dicho incremento alcanza el máximo de 0,27 m en el punto
proyectado de nueva conexión, y disminuye hasta ser casi nulo en 150 m aguas arriba
de la conexión proyectada.

En el siguiente cuadro se muestra la revancha en ambos bordes para la situación con

proyecto, indicando en negrita aquellos tramos que requieren peralte de borde para
cumplir una revancha mínima de 0,20 m. Se considera que el peralte será implementado
mediante un bloque de hormigón de 0,2 m de altura.

**Cuadro 7.2: (T=100 años)**

|Perfil<br>HecRas|X<br>[m]|Cota borde<br>izquierdo<br>[m s.n.m.]|Cota borde<br>derecho<br>[m s.n.m.]|Cota de<br>aguas con<br>Proyecto<br>[m s.n.m.]|Revancha<br>borde<br>izquierdo<br>[m]|Revancha<br>borde<br>derecho<br>[m]|Peralte<br>borde<br>izquierdo<br>[m]|Peralte<br>borde<br>derecho<br>[m]|
|---|---|---|---|---|---|---|---|---|
|9|0|145,47|145,53|145,22|0,25|0,31|||
|8|75,33|145,35|145,50|145,11|0,24|0,39|||
|7|158,61|145,17|145,22|145,09|**0,08**|**0,13**|0,2|0,2|
|6|237,80|144,96|144,96|144,96|**0,00**|**0,00**|0,2|0,2|
|5|338,72|144,99|144,98|144,61|0,38|0,37|||
|4|445,94|144,64|144,64|144,43|0,21|0,21|||
|3|452,26|144,39|144,52|144,42|**-0,03**|**0,10**|0,25|0,2|
|2|471,10|144,58|144,47|144,39|**0,19**|**0,08**|0,2|0,2|
|1|536,51|144,47|144,49|144,21|0,26|0,28|||

En el siguiente gráfico se muestra los resultados del cuadro anterior:

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** 31 de 76|

**Conexión actual**

**con Cauce en**

**estudio (D2)**

**Requiere peralte**

**Figura 7.1: Perfil hidráulico sin y con Proyecto - Canal Drenaje N°3 (T=100 años)**

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.1 de A.1|

**ANEXO A**

**Situación Sin Proyecto**

**Ejes Hidráulicos crecidas de probabilidad de excedencia**
**95%, 80% y 60%; y 2, 5, 10, 20, 50, 100 y 200 años de**

**retorno**

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.1 de A.22|

A.1 Eje hidráulico Sin Proyecto - Probabilidad de excedencia 95%

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|Pexc 95%|0,11|144,50|144,83|144,66|144,83|0,00085|0,35|0,37|1,87|0,21|
|D2|arriba junta|59,77|11,794|Pexc 95%|0,11|144,48|144,81|144,65|144,82|0,00094|0,37|0,36|1,83|0,22|
|D2|arriba junta|79,77|11,589|Pexc 95%|0,11|144,47|144,79|144,63|144,80|0,00104|0,38|0,35|1,81|0,23|
|D2|arriba junta|99,8|11,383|Pexc 95%|0,11|144,45|144,77|144,62|144,77|0,00119|0,40|0,33|1,82|0,25|
|D2|arriba junta|119,84|11,178|Pexc 95%|0,11|144,43|144,74|144,61|144,75|0,00137|0,42|0,32|1,81|0,27|
|D2|arriba junta|137,16|11|Pexc 95%|0,11|144,42|144,72|144,59|144,72|0,00158|0,43|0,31|1,82|0,28|
|D2|arriba junta|157,14|10,755|Pexc 95%|0,11|144,34|144,69|144,53|144,70|0,00114|0,42|0,33|1,71|0,24|
|D2|arriba junta|177,14|10,51|Pexc 95%|0,11|144,27|144,67|144,47|144,68|0,00083|0,38|0,36|1,65|0,20|
|D2|arriba junta|197,15|10,265|Pexc 95%|0,11|144,19|144,66|144,42|144,66|0,00069|0,34|0,39|1,60|0,18|
|D2|arriba junta|217,16|10,02|Pexc 95%|0,11|144,12|144,64|144,38|144,65|0,00068|0,31|0,39|1,53|0,17|
|D2|arriba junta|218,76|10|Pexc 95%|0,11|144,11|144,64|144,38|144,65|0,00068|0,31|0,39|1,52|0,16|
|D2|arriba junta|238,71|9,6435|Pexc 95%|0,11|144,09|144,63|144,33|144,64|0,00033|0,25|0,51|1,81|0,13|
|D2|arriba junta|258,85|9,287|Pexc 95%|0,11|144,07|144,63|144,29|144,63|0,00018|0,19|0,65|2,13|0,10|
|D2|arriba junta|274,9|9|Pexc 95%|0,11|144,05|144,63|144,26|144,63|0,00011|0,16|0,77|2,42|0,08|
|D2|arriba junta|294,69|8,7528|Pexc 95%|0,11|144,04|144,63|144,26|144,63|0,00013|0,17|0,74|2,36|0,09|
|D2|arriba junta|314,91|8,5056|Pexc 95%|0,11|144,04|144,62|144,26|144,62|0,00015|0,18|0,70|2,31|0,09|
|D2|arriba junta|335|8,2583|Pexc 95%|0,11|144,03|144,62|144,26|144,62|0,00018|0,20|0,66|2,26|0,10|
|D2|arriba junta|354,94|8,0111|Pexc 95%|0,11|144,02|144,61|144,26|144,62|0,00023|0,21|0,62|2,23|0,10|
|D2|arriba junta|355,82|8|Pexc 95%|0,11|144,02|144,61|144,27|144,62|0,00023|0,21|0,62|2,23|0,10|
|D2|arriba junta|375,18|7,775|Pexc 95%|0,11|144,07|144,61|144,31|144,61|0,00031|0,25|0,55|2,19|0,12|
|D2|arriba junta|395,64|7,5501|Pexc 95%|0,11|144,12|144,60|144,35|144,60|0,00045|0,30|0,48|2,14|0,15|
|D2|arriba junta|416,02|7,3251|Pexc 95%|0,11|144,18|144,59|144,40|144,59|0,00073|0,36|0,41|2,09|0,19|
|D2|arriba junta|435,99|7,1001|Pexc 95%|0,11|144,23|144,56|144,43|144,57|0,00151|0,44|0,32|1,96|0,27|
|D2|arriba junta|444,77|7|Pexc 95%|0,11|144,25|144,54|144,44|144,55|0,00255|0,50|0,27|1,83|0,34|
|D2|arriba junta|464,76|6,7923|Pexc 95%|0,11|144,18|144,49|144,39|144,50|0,00269|0,56|0,25|1,69|0,36|
|D2|arriba junta|485,72|6,5846|Pexc 95%|0,11|144,12|144,44|144,34|144,45|0,00266|0,58|0,24|1,57|0,36|
|D2|arriba junta|505,61|6,3769|Pexc 95%|0,11|144,05|144,39|144,27|144,40|0,00247|0,56|0,25|1,49|0,34|
|D2|arriba junta|524,94|6,1693|Pexc 95%|0,11|143,98|144,34|144,21|144,35|0,00218|0,51|0,26|1,44|0,31|
|D2|arriba junta|541,11|6|Pexc 95%|0,11|143,93|144,31|144,16|144,32|0,00192|0,45|0,27|1,42|0,29|
|D2|arriba junta|560,93|5,7904|Pexc 95%|0,11|143,92|144,27|144,13|144,28|0,00177|0,45|0,28|1,48|0,29|
|D2|arriba junta|580,98|5,5807|Pexc 95%|0,11|143,90|144,24|144,10|144,25|0,00156|0,43|0,29|1,55|0,28|
|D2|arriba junta|601,4|5,3711|Pexc 95%|0,11|143,89|144,21|144,06|144,22|0,00126|0,40|0,32|1,64|0,25|
|D2|arriba junta|621,65|5,1614|Pexc 95%|0,11|143,87|144,19|144,03|144,20|0,00093|0,36|0,36|1,75|0,22|
|D2|arriba junta|636,55|5|Pexc 95%|0,11|143,86|144,18|144,00|144,18|0,00070|0,32|0,40|1,86|0,20|
|D2|arriba junta|647,85|4|Pexc 95%|0,11|143,91|144,16|144,06|144,17|0,00199|0,40|0,29|1,84|0,30|
|D3|arriba junta|0|9|Pexc 95%|0,07|144,95|145,08|145,04|145,09|0,00497|0,45|0,19|2,70|0,44|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.2 de A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|arriba junta|19,85|8,7368|Pexc 95%|0,07|144,81|144,96|144,92|144,98|0,00608|0,57|0,13|1,17|0,51|
|D3|arriba junta|39,67|8,4737|Pexc 95%|0,07|144,68|144,84|144,79|144,86|0,00572|0,62|0,12|0,91|0,50|
|D3|arriba junta|59,49|8,2105|Pexc 95%|0,07|144,54|144,76|144,67|144,77|0,00349|0,59|0,13|0,74|0,41|
|D3|arriba junta|75,33|8|Pexc 95%|0,07|144,43|144,71|144,58|144,73|0,00230|0,57|0,14|0,64|0,35|
|D3|arriba junta|95,39|7,759|Pexc 95%|0,07|144,39|144,67|0,00|144,68|0,00226|0,56|0,15|0,69|0,35|
|D3|arriba junta|115,46|7,5181|Pexc 95%|0,07|144,36|144,62|0,00|144,64|0,00211|0,54|0,16|0,77|0,34|
|D3|arriba junta|135,52|7,2771|Pexc 95%|0,07|144,32|144,59|0,00|144,60|0,00164|0,48|0,18|0,98|0,30|
|D3|arriba junta|155,6|7,0361|Pexc 95%|0,07|144,29|144,57|0,00|144,57|0,00088|0,36|0,24|1,26|0,22|
|D3|arriba junta|158,61|7|Pexc 95%|0,07|144,28|144,57|0,00|144,57|0,00078|0,34|0,26|1,30|0,21|
|D3|arriba junta|198,72|6,42|Pexc 95%|0,07|144,22|144,55|0,00|144,55|0,00113|0,37|0,21|1,05|0,23|
|D3|arriba junta|218,77|6,18|Pexc 95%|0,07|144,20|144,52|0,00|144,53|0,00147|0,38|0,19|1,00|0,25|
|D3|arriba junta|237,8|6|Pexc 95%|0,07|144,17|144,48|144,37|144,49|0,00258|0,43|0,17|0,99|0,32|
|D3|arriba junta|257,8|5,802|Pexc 95%|0,07|144,13|144,43|144,32|144,44|0,00251|0,42|0,17|1,01|0,32|
|D3|arriba junta|277,79|5,604|Pexc 95%|0,07|144,10|144,38|144,28|144,39|0,00252|0,42|0,17|1,04|0,32|
|D3|arriba junta|297,78|5,4059|Pexc 95%|0,07|144,06|144,33|144,23|144,34|0,00247|0,42|0,17|1,08|0,32|
|D3|arriba junta|317,75|5,2079|Pexc 95%|0,07|144,02|144,28|144,18|144,29|0,00258|0,42|0,17|1,12|0,33|
|D3|arriba junta|337,72|5,0099|Pexc 95%|0,07|143,98|144,21|144,14|144,22|0,00421|0,49|0,15|1,13|0,41|
|D3|arriba junta|338,72|5|Pexc 95%|0,07|143,98|144,21|144,13|144,22|0,00435|0,49|0,15|1,12|0,42|
|D3|arriba junta|358,41|4,8131|Pexc 95%|0,07|143,91|144,16|144,05|144,17|0,00146|0,35|0,21|1,25|0,26|
|D3|arriba junta|378,39|4,6262|Pexc 95%|0,07|143,83|144,15|143,96|144,15|0,00043|0,24|0,31|1,40|0,15|
|D3|arriba junta|398,88|4,4393|Pexc 95%|0,07|143,76|144,15|143,88|144,15|0,00016|0,17|0,44|1,56|0,09|
|D3|arriba junta|420,1|4,2523|Pexc 95%|0,07|143,69|144,15|143,80|144,15|0,00007|0,13|0,59|1,79|0,07|
|D3|arriba junta|440,31|4,0654|Pexc 95%|0,07|143,62|144,14|143,72|144,15|0,00004|0,11|0,73|1,84|0,05|
|D3|arriba junta|445,94|4|Pexc 95%|0,07|143,59|144,14|143,70|144,15|0,00003|0,10|0,77|1,81|0,05|
|D3|bajo junta|452,26|3|Pexc 95%|0,17|143,95|144,12|144,09|144,14|0,01163|0,71|0,25|2,47|0,68|
|D3|bajo junta|471,1|2|Pexc 95%|0,17|143,64|144,10|143,87|144,10|0,00070|0,34|0,55|2,04|0,19|
|D3|bajo junta|491,09|1,6942|Pexc 95%|0,17|143,66|144,08|143,87|144,09|0,00075|0,38|0,53|2,10|0,20|
|D3|bajo junta|511,09|1,3884|Pexc 95%|0,17|143,68|144,06|143,88|144,07|0,00114|0,43|0,44|2,24|0,25|
|D3|bajo junta|531,1|1,0826|Pexc 95%|0,17|143,70|144,02|143,92|144,03|0,00282|0,54|0,33|1,71|0,37|
|D3|bajo junta|536,51|1|Pexc 95%|0,17|143,71|143,99|143,93|144,01|0,00600|0,66|0,27|1,70|0,52|
||||||||||||||||

A.2 Eje hidráulico Sin Proyecto - Probabilidad de excedencia 80%

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|Pexc 80%|0,12|144,50|144,84|144,67|144,85|0,00085|0,36|0,40|1,92|0,22|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.3 de A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|59,77|11,794|Pexc 80%|0,12|144,48|144,82|144,66|144,83|0,00094|0,38|0,38|1,88|0,23|
|D2|arriba junta|79,77|11,589|Pexc 80%|0,12|144,47|144,80|144,64|144,81|0,00104|0,39|0,37|1,87|0,24|
|D2|arriba junta|99,8|11,383|Pexc 80%|0,12|144,45|144,78|144,63|144,79|0,00118|0,41|0,35|1,87|0,25|
|D2|arriba junta|119,84|11,178|Pexc 80%|0,12|144,43|144,75|144,61|144,76|0,00134|0,43|0,34|1,87|0,27|
|D2|arriba junta|137,16|11|Pexc 80%|0,12|144,42|144,73|144,60|144,74|0,00151|0,44|0,33|1,88|0,28|
|D2|arriba junta|157,14|10,755|Pexc 80%|0,12|144,34|144,70|144,54|144,71|0,00112|0,43|0,35|1,77|0,24|
|D2|arriba junta|177,14|10,51|Pexc 80%|0,12|144,27|144,68|144,48|144,69|0,00084|0,39|0,38|1,70|0,21|
|D2|arriba junta|197,15|10,265|Pexc 80%|0,12|144,19|144,67|144,43|144,68|0,00071|0,36|0,41|1,65|0,18|
|D2|arriba junta|217,16|10,02|Pexc 80%|0,12|144,12|144,66|144,39|144,66|0,00070|0,32|0,42|1,57|0,17|
|D2|arriba junta|218,76|10|Pexc 80%|0,12|144,11|144,66|144,38|144,66|0,00071|0,32|0,41|1,56|0,17|
|D2|arriba junta|238,71|9,6435|Pexc 80%|0,12|144,09|144,65|144,34|144,65|0,00035|0,26|0,53|1,85|0,13|
|D2|arriba junta|258,85|9,287|Pexc 80%|0,12|144,07|144,64|144,30|144,64|0,00019|0,20|0,68|2,17|0,10|
|D2|arriba junta|274,9|9|Pexc 80%|0,12|144,05|144,64|144,27|144,64|0,00012|0,17|0,80|2,45|0,08|
|D2|arriba junta|294,69|8,7528|Pexc 80%|0,12|144,04|144,64|144,27|144,64|0,00014|0,18|0,77|2,40|0,09|
|D2|arriba junta|314,91|8,5056|Pexc 80%|0,12|144,04|144,63|144,27|144,64|0,00016|0,19|0,73|2,36|0,09|
|D2|arriba junta|335|8,2583|Pexc 80%|0,12|144,03|144,63|144,27|144,63|0,00019|0,21|0,69|2,32|0,10|
|D2|arriba junta|354,94|8,0111|Pexc 80%|0,12|144,02|144,63|144,27|144,63|0,00024|0,22|0,65|2,28|0,11|
|D2|arriba junta|355,82|8|Pexc 80%|0,12|144,02|144,63|144,27|144,63|0,00024|0,22|0,64|2,28|0,11|
|D2|arriba junta|375,18|7,775|Pexc 80%|0,12|144,07|144,62|144,32|144,62|0,00033|0,26|0,58|2,25|0,13|
|D2|arriba junta|395,64|7,5501|Pexc 80%|0,12|144,12|144,61|144,36|144,61|0,00047|0,31|0,51|2,20|0,15|
|D2|arriba junta|416,02|7,3251|Pexc 80%|0,12|144,18|144,60|144,41|144,60|0,00075|0,37|0,43|2,15|0,20|
|D2|arriba junta|435,99|7,1001|Pexc 80%|0,12|144,23|144,57|144,44|144,58|0,00153|0,46|0,34|2,02|0,27|
|D2|arriba junta|444,77|7|Pexc 80%|0,12|144,25|144,55|144,45|144,56|0,00253|0,51|0,29|1,90|0,34|
|D2|arriba junta|464,76|6,7923|Pexc 80%|0,12|144,18|144,50|144,40|144,51|0,00266|0,57|0,27|1,75|0,36|
|D2|arriba junta|485,72|6,5846|Pexc 80%|0,12|144,12|144,45|144,35|144,46|0,00264|0,59|0,26|1,63|0,36|
|D2|arriba junta|505,61|6,3769|Pexc 80%|0,12|144,05|144,40|144,28|144,41|0,00245|0,57|0,26|1,54|0,34|
|D2|arriba junta|524,94|6,1693|Pexc 80%|0,12|143,98|144,35|144,22|144,36|0,00218|0,52|0,28|1,49|0,32|
|D2|arriba junta|541,11|6|Pexc 80%|0,12|143,93|144,32|144,17|144,33|0,00193|0,47|0,29|1,45|0,29|
|D2|arriba junta|560,93|5,7904|Pexc 80%|0,12|143,92|144,28|144,14|144,29|0,00178|0,46|0,30|1,51|0,29|
|D2|arriba junta|580,98|5,5807|Pexc 80%|0,12|143,90|144,25|144,11|144,26|0,00156|0,45|0,31|1,58|0,28|
|D2|arriba junta|601,4|5,3711|Pexc 80%|0,12|143,89|144,22|144,07|144,23|0,00127|0,41|0,34|1,67|0,26|
|D2|arriba junta|621,65|5,1614|Pexc 80%|0,12|143,87|144,20|144,03|144,21|0,00094|0,37|0,38|1,78|0,22|
|D2|arriba junta|636,55|5|Pexc 80%|0,12|143,86|144,19|144,01|144,20|0,00072|0,34|0,42|1,90|0,20|
|D2|arriba junta|647,85|4|Pexc 80%|0,12|143,91|144,17|144,07|144,18|0,00191|0,41|0,31|1,87|0,30|
|D3|arriba junta|0|9|Pexc 80%|0,07|144,95|145,08|145,04|145,09|0,00497|0,45|0,19|2,70|0,44|
|D3|arriba junta|19,85|8,7368|Pexc 80%|0,07|144,81|144,96|144,92|144,98|0,00608|0,57|0,13|1,17|0,51|
|D3|arriba junta|39,67|8,4737|Pexc 80%|0,07|144,68|144,84|144,79|144,86|0,00572|0,62|0,12|0,91|0,50|
|D3|arriba junta|59,49|8,2105|Pexc 80%|0,07|144,54|144,76|144,67|144,77|0,00349|0,59|0,13|0,74|0,41|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.4 de A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|arriba junta|75,33|8|Pexc 80%|0,07|144,43|144,71|144,58|144,73|0,00230|0,57|0,14|0,64|0,35|
|D3|arriba junta|95,39|7,759|Pexc 80%|0,07|144,39|144,67|0,00|144,68|0,00226|0,56|0,15|0,69|0,35|
|D3|arriba junta|115,46|7,5181|Pexc 80%|0,07|144,36|144,62|0,00|144,64|0,00211|0,54|0,16|0,77|0,34|
|D3|arriba junta|135,52|7,2771|Pexc 80%|0,07|144,32|144,59|0,00|144,60|0,00164|0,48|0,18|0,98|0,30|
|D3|arriba junta|155,6|7,0361|Pexc 80%|0,07|144,29|144,57|0,00|144,57|0,00087|0,36|0,24|1,26|0,22|
|D3|arriba junta|158,61|7|Pexc 80%|0,07|144,28|144,57|0,00|144,57|0,00078|0,34|0,26|1,30|0,21|
|D3|arriba junta|198,72|6,42|Pexc 80%|0,07|144,22|144,55|0,00|144,55|0,00113|0,37|0,21|1,05|0,23|
|D3|arriba junta|218,77|6,18|Pexc 80%|0,07|144,20|144,52|0,00|144,53|0,00147|0,38|0,19|1,00|0,25|
|D3|arriba junta|237,8|6|Pexc 80%|0,07|144,17|144,48|144,37|144,49|0,00258|0,43|0,17|0,99|0,32|
|D3|arriba junta|257,8|5,802|Pexc 80%|0,07|144,13|144,43|144,32|144,44|0,00251|0,42|0,17|1,01|0,32|
|D3|arriba junta|277,79|5,604|Pexc 80%|0,07|144,10|144,38|144,28|144,39|0,00252|0,42|0,17|1,04|0,32|
|D3|arriba junta|297,78|5,4059|Pexc 80%|0,07|144,06|144,33|144,23|144,34|0,00247|0,42|0,17|1,08|0,32|
|D3|arriba junta|317,75|5,2079|Pexc 80%|0,07|144,02|144,28|144,18|144,29|0,00258|0,42|0,17|1,12|0,33|
|D3|arriba junta|337,72|5,0099|Pexc 80%|0,07|143,98|144,21|144,14|144,23|0,00383|0,47|0,15|1,14|0,39|
|D3|arriba junta|338,72|5|Pexc 80%|0,07|143,98|144,21|144,13|144,22|0,00394|0,47|0,15|1,14|0,40|
|D3|arriba junta|358,41|4,8131|Pexc 80%|0,07|143,91|144,18|144,05|144,18|0,00118|0,33|0,22|1,27|0,23|
|D3|arriba junta|378,39|4,6262|Pexc 80%|0,07|143,83|144,17|143,96|144,17|0,00036|0,22|0,34|1,43|0,14|
|D3|arriba junta|398,88|4,4393|Pexc 80%|0,07|143,76|144,16|143,88|144,16|0,00014|0,17|0,47|1,58|0,09|
|D3|arriba junta|420,1|4,2523|Pexc 80%|0,07|143,69|144,16|143,80|144,16|0,00006|0,13|0,61|1,83|0,06|
|D3|arriba junta|440,31|4,0654|Pexc 80%|0,07|143,62|144,16|143,72|144,16|0,00003|0,11|0,76|1,86|0,05|
|D3|arriba junta|445,94|4|Pexc 80%|0,07|143,59|144,16|143,70|144,16|0,00003|0,10|0,80|1,83|0,04|
|D3|bajo junta|452,26|3|Pexc 80%|0,19|143,95|144,13|144,10|144,16|0,00880|0,68|0,29|2,57|0,61|
|D3|bajo junta|471,1|2|Pexc 80%|0,19|143,64|144,11|143,88|144,12|0,00074|0,36|0,58|2,08|0,20|
|D3|bajo junta|491,09|1,6942|Pexc 80%|0,19|143,66|144,10|143,88|144,10|0,00079|0,40|0,56|2,15|0,21|
|D3|bajo junta|511,09|1,3884|Pexc 80%|0,19|143,68|144,07|143,89|144,08|0,00119|0,46|0,48|2,26|0,26|
|D3|bajo junta|531,1|1,0826|Pexc 80%|0,19|143,70|144,03|143,92|144,05|0,00292|0,57|0,35|1,73|0,38|
|D3|bajo junta|536,51|1|Pexc 80%|0,19|143,71|144,00|143,94|144,02|0,00600|0,69|0,29|1,71|0,52|
||||||||||||||||

A.3 Eje hidráulico Sin Proyecto - Probabilidad de excedencia 60%

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|Pexc 60%|0,14|144,50|144,86|144,68|144,87|0,00086|0,38|0,44|2,01|0,22|
|D2|arriba junta|59,77|11,794|Pexc 60%|0,14|144,48|144,85|144,67|144,85|0,00094|0,40|0,43|1,97|0,23|
|D2|arriba junta|79,77|11,589|Pexc 60%|0,14|144,47|144,82|144,66|144,83|0,00104|0,42|0,41|1,98|0,24|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.5 de A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|99,8|11,383|Pexc 60%|0,14|144,45|144,80|144,64|144,81|0,00117|0,43|0,40|1,98|0,25|
|D2|arriba junta|119,84|11,178|Pexc 60%|0,14|144,43|144,78|144,63|144,79|0,00129|0,45|0,39|1,98|0,26|
|D2|arriba junta|137,16|11|Pexc 60%|0,14|144,42|144,75|144,61|144,76|0,00141|0,45|0,38|2,00|0,27|
|D2|arriba junta|157,14|10,755|Pexc 60%|0,14|144,34|144,73|144,56|144,74|0,00109|0,44|0,40|1,89|0,24|
|D2|arriba junta|177,14|10,51|Pexc 60%|0,14|144,27|144,71|144,49|144,72|0,00085|0,41|0,43|1,80|0,21|
|D2|arriba junta|197,15|10,265|Pexc 60%|0,14|144,19|144,70|144,44|144,70|0,00074|0,38|0,45|1,74|0,19|
|D2|arriba junta|217,16|10,02|Pexc 60%|0,14|144,12|144,68|144,40|144,69|0,00075|0,35|0,46|1,65|0,18|
|D2|arriba junta|218,76|10|Pexc 60%|0,14|144,11|144,68|144,40|144,69|0,00075|0,34|0,45|1,64|0,18|
|D2|arriba junta|238,71|9,6435|Pexc 60%|0,14|144,09|144,67|144,36|144,67|0,00038|0,28|0,58|1,92|0,14|
|D2|arriba junta|258,85|9,287|Pexc 60%|0,14|144,07|144,67|144,31|144,67|0,00021|0,22|0,73|2,24|0,11|
|D2|arriba junta|274,9|9|Pexc 60%|0,14|144,05|144,66|144,28|144,67|0,00013|0,18|0,86|2,52|0,09|
|D2|arriba junta|294,69|8,7528|Pexc 60%|0,14|144,04|144,66|144,28|144,66|0,00015|0,20|0,82|2,48|0,09|
|D2|arriba junta|314,91|8,5056|Pexc 60%|0,14|144,04|144,66|144,28|144,66|0,00018|0,21|0,78|2,44|0,10|
|D2|arriba junta|335|8,2583|Pexc 60%|0,14|144,03|144,65|144,29|144,66|0,00021|0,22|0,74|2,41|0,11|
|D2|arriba junta|354,94|8,0111|Pexc 60%|0,14|144,02|144,65|144,29|144,65|0,00027|0,24|0,70|2,39|0,11|
|D2|arriba junta|355,82|8|Pexc 60%|0,14|144,02|144,65|144,29|144,65|0,00027|0,24|0,70|2,39|0,11|
|D2|arriba junta|375,18|7,775|Pexc 60%|0,14|144,07|144,64|144,33|144,64|0,00036|0,28|0,63|2,35|0,13|
|D2|arriba junta|395,64|7,5501|Pexc 60%|0,14|144,12|144,63|144,38|144,64|0,00051|0,33|0,55|2,31|0,16|
|D2|arriba junta|416,02|7,3251|Pexc 60%|0,14|144,18|144,62|144,43|144,62|0,00080|0,40|0,48|2,26|0,20|
|D2|arriba junta|435,99|7,1001|Pexc 60%|0,14|144,23|144,59|144,45|144,60|0,00156|0,48|0,38|2,14|0,28|
|D2|arriba junta|444,77|7|Pexc 60%|0,14|144,25|144,57|144,46|144,58|0,00249|0,53|0,32|2,02|0,35|
|D2|arriba junta|464,76|6,7923|Pexc 60%|0,14|144,18|144,52|144,42|144,53|0,00260|0,60|0,31|1,87|0,36|
|D2|arriba junta|485,72|6,5846|Pexc 60%|0,14|144,12|144,47|144,36|144,48|0,00256|0,61|0,30|1,74|0,36|
|D2|arriba junta|505,61|6,3769|Pexc 60%|0,14|144,05|144,42|144,30|144,43|0,00242|0,59|0,30|1,64|0,34|
|D2|arriba junta|524,94|6,1693|Pexc 60%|0,14|143,98|144,37|144,23|144,39|0,00218|0,55|0,31|1,57|0,32|
|D2|arriba junta|541,11|6|Pexc 60%|0,14|143,93|144,34|144,19|144,35|0,00195|0,50|0,32|1,51|0,30|
|D2|arriba junta|560,93|5,7904|Pexc 60%|0,14|143,92|144,30|144,15|144,31|0,00180|0,49|0,33|1,57|0,30|
|D2|arriba junta|580,98|5,5807|Pexc 60%|0,14|143,90|144,27|144,12|144,28|0,00159|0,47|0,35|1,64|0,29|
|D2|arriba junta|601,4|5,3711|Pexc 60%|0,14|143,89|144,24|144,08|144,25|0,00131|0,44|0,37|1,73|0,26|
|D2|arriba junta|621,65|5,1614|Pexc 60%|0,14|143,87|144,22|144,05|144,23|0,00100|0,40|0,41|1,84|0,23|
|D2|arriba junta|636,55|5|Pexc 60%|0,14|143,86|144,21|144,02|144,21|0,00078|0,36|0,45|1,95|0,21|
|D2|arriba junta|647,85|4|Pexc 60%|0,14|143,91|144,19|144,08|144,20|0,00191|0,43|0,34|1,92|0,31|
|D3|arriba junta|0|9|Pexc 60%|0,09|144,95|145,10|145,06|145,10|0,00443|0,47|0,24|2,99|0,43|
|D3|arriba junta|19,85|8,7368|Pexc 60%|0,09|144,81|144,98|144,93|145,00|0,00572|0,62|0,16|1,23|0,50|
|D3|arriba junta|39,67|8,4737|Pexc 60%|0,09|144,68|144,87|144,81|144,89|0,00502|0,65|0,15|0,95|0,49|
|D3|arriba junta|59,49|8,2105|Pexc 60%|0,09|144,54|144,79|144,69|144,81|0,00320|0,63|0,16|0,79|0,41|
|D3|arriba junta|75,33|8|Pexc 60%|0,09|144,43|144,75|144,61|144,77|0,00239|0,64|0,17|0,68|0,37|
|D3|arriba junta|95,39|7,759|Pexc 60%|0,09|144,39|144,70|0,00|144,72|0,00235|0,62|0,17|0,73|0,36|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.6 de A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|arriba junta|115,46|7,5181|Pexc 60%|0,09|144,36|144,66|0,00|144,67|0,00220|0,60|0,18|0,84|0,35|
|D3|arriba junta|135,52|7,2771|Pexc 60%|0,09|144,32|144,62|0,00|144,63|0,00169|0,52|0,22|1,09|0,31|
|D3|arriba junta|155,6|7,0361|Pexc 60%|0,09|144,29|144,60|0,00|144,61|0,00091|0,40|0,29|1,35|0,23|
|D3|arriba junta|158,61|7|Pexc 60%|0,09|144,28|144,60|0,00|144,61|0,00082|0,38|0,30|1,38|0,22|
|D3|arriba junta|198,72|6,42|Pexc 60%|0,09|144,22|144,58|0,00|144,59|0,00122|0,42|0,24|1,13|0,25|
|D3|arriba junta|218,77|6,18|Pexc 60%|0,09|144,20|144,55|0,00|144,56|0,00157|0,43|0,22|1,05|0,27|
|D3|arriba junta|237,8|6|Pexc 60%|0,09|144,17|144,51|144,39|144,52|0,00261|0,47|0,20|1,03|0,33|
|D3|arriba junta|257,8|5,802|Pexc 60%|0,09|144,13|144,46|144,34|144,47|0,00255|0,47|0,20|1,06|0,33|
|D3|arriba junta|277,79|5,604|Pexc 60%|0,09|144,10|144,41|144,30|144,42|0,00257|0,47|0,20|1,09|0,33|
|D3|arriba junta|297,78|5,4059|Pexc 60%|0,09|144,06|144,36|144,25|144,37|0,00253|0,47|0,20|1,13|0,33|
|D3|arriba junta|317,75|5,2079|Pexc 60%|0,09|144,02|144,30|144,20|144,32|0,00267|0,47|0,20|1,16|0,34|
|D3|arriba junta|337,72|5,0099|Pexc 60%|0,09|143,98|144,24|144,16|144,25|0,00359|0,51|0,18|1,18|0,39|
|D3|arriba junta|338,72|5|Pexc 60%|0,09|143,98|144,24|144,15|144,25|0,00365|0,51|0,18|1,19|0,40|
|D3|arriba junta|358,41|4,8131|Pexc 60%|0,09|143,91|144,20|144,06|144,21|0,00129|0,37|0,26|1,31|0,25|
|D3|arriba junta|378,39|4,6262|Pexc 60%|0,09|143,83|144,19|143,98|144,19|0,00044|0,26|0,37|1,47|0,15|
|D3|arriba junta|398,88|4,4393|Pexc 60%|0,09|143,76|144,19|143,89|144,19|0,00018|0,20|0,50|1,64|0,10|
|D3|arriba junta|420,1|4,2523|Pexc 60%|0,09|143,69|144,18|143,81|144,18|0,00009|0,16|0,66|1,88|0,07|
|D3|arriba junta|440,31|4,0654|Pexc 60%|0,09|143,62|144,18|143,74|144,18|0,00005|0,13|0,80|1,89|0,06|
|D3|arriba junta|445,94|4|Pexc 60%|0,09|143,59|144,18|143,71|144,18|0,00004|0,12|0,84|1,86|0,05|
|D3|bajo junta|452,26|3|Pexc 60%|0,22|143,95|144,16|144,11|144,18|0,00652|0,66|0,36|2,70|0,54|
|D3|bajo junta|471,1|2|Pexc 60%|0,22|143,64|144,13|143,90|144,14|0,00079|0,39|0,63|2,14|0,21|
|D3|bajo junta|491,09|1,6942|Pexc 60%|0,22|143,66|144,12|143,90|144,13|0,00084|0,43|0,61|2,22|0,22|
|D3|bajo junta|511,09|1,3884|Pexc 60%|0,22|143,68|144,09|143,90|144,10|0,00125|0,49|0,52|2,29|0,27|
|D3|bajo junta|531,1|1,0826|Pexc 60%|0,22|143,70|144,05|143,94|144,07|0,00304|0,61|0,38|1,76|0,39|
|D3|bajo junta|536,51|1|Pexc 60%|0,22|143,71|144,02|143,95|144,04|0,00600|0,73|0,32|1,74|0,53|
||||||||||||||||

A.4 Eje hidráulico Sin Proyecto - T=2 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=2|0,15|144,50|144,87|144,69|144,88|0,00086|0,39|0,46|2,06|0,22|
|D2|arriba junta|59,77|11,794|T=2|0,15|144,48|144,86|144,67|144,86|0,00095|0,41|0,45|2,02|0,23|
|D2|arriba junta|79,77|11,589|T=2|0,15|144,47|144,84|144,66|144,84|0,00104|0,43|0,43|2,03|0,24|
|D2|arriba junta|99,8|11,383|T=2|0,15|144,45|144,81|144,65|144,82|0,00116|0,44|0,42|2,03|0,25|
|D2|arriba junta|119,84|11,178|T=2|0,15|144,43|144,79|144,63|144,80|0,00127|0,45|0,41|2,04|0,26|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.7 de A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|137,16|11|T=2|0,15|144,42|144,77|144,61|144,77|0,00137|0,46|0,40|2,06|0,27|
|D2|arriba junta|157,14|10,755|T=2|0,15|144,34|144,74|144,56|144,75|0,00108|0,45|0,42|1,95|0,24|
|D2|arriba junta|177,14|10,51|T=2|0,15|144,27|144,72|144,50|144,73|0,00085|0,42|0,45|1,85|0,21|
|D2|arriba junta|197,15|10,265|T=2|0,15|144,19|144,71|144,45|144,71|0,00075|0,39|0,48|1,78|0,19|
|D2|arriba junta|217,16|10,02|T=2|0,15|144,12|144,69|144,41|144,70|0,00076|0,36|0,48|1,69|0,18|
|D2|arriba junta|218,76|10|T=2|0,15|144,11|144,69|144,41|144,70|0,00077|0,35|0,47|1,68|0,18|
|D2|arriba junta|238,71|9,6435|T=2|0,15|144,09|144,68|144,36|144,69|0,00039|0,29|0,60|1,96|0,14|
|D2|arriba junta|258,85|9,287|T=2|0,15|144,07|144,68|144,32|144,68|0,00021|0,23|0,76|2,27|0,11|
|D2|arriba junta|274,9|9|T=2|0,15|144,05|144,68|144,29|144,68|0,00014|0,19|0,89|2,55|0,09|
|D2|arriba junta|294,69|8,7528|T=2|0,15|144,04|144,67|144,29|144,67|0,00016|0,20|0,85|2,51|0,10|
|D2|arriba junta|314,91|8,5056|T=2|0,15|144,04|144,67|144,29|144,67|0,00019|0,22|0,81|2,48|0,10|
|D2|arriba junta|335|8,2583|T=2|0,15|144,03|144,66|144,29|144,67|0,00022|0,23|0,77|2,45|0,11|
|D2|arriba junta|354,94|8,0111|T=2|0,15|144,02|144,66|144,30|144,66|0,00028|0,25|0,72|2,43|0,12|
|D2|arriba junta|355,82|8|T=2|0,15|144,02|144,66|144,30|144,66|0,00028|0,25|0,72|2,43|0,12|
|D2|arriba junta|375,18|7,775|T=2|0,15|144,07|144,65|144,34|144,66|0,00037|0,29|0,65|2,40|0,14|
|D2|arriba junta|395,64|7,5501|T=2|0,15|144,12|144,64|144,39|144,65|0,00053|0,35|0,58|2,36|0,17|
|D2|arriba junta|416,02|7,3251|T=2|0,15|144,18|144,63|144,43|144,63|0,00081|0,41|0,50|2,31|0,21|
|D2|arriba junta|435,99|7,1001|T=2|0,15|144,23|144,60|144,46|144,61|0,00157|0,49|0,40|2,19|0,28|
|D2|arriba junta|444,77|7|T=2|0,15|144,25|144,58|144,47|144,59|0,00247|0,55|0,34|2,08|0,35|
|D2|arriba junta|464,76|6,7923|T=2|0,15|144,18|144,53|144,42|144,54|0,00258|0,61|0,32|1,92|0,36|
|D2|arriba junta|485,72|6,5846|T=2|0,15|144,12|144,48|144,37|144,49|0,00253|0,62|0,32|1,79|0,36|
|D2|arriba junta|505,61|6,3769|T=2|0,15|144,05|144,43|144,31|144,44|0,00240|0,60|0,32|1,69|0,34|
|D2|arriba junta|524,94|6,1693|T=2|0,15|143,98|144,39|144,24|144,40|0,00215|0,56|0,33|1,60|0,32|
|D2|arriba junta|541,11|6|T=2|0,15|143,93|144,35|144,19|144,36|0,00193|0,51|0,34|1,55|0,30|
|D2|arriba junta|560,93|5,7904|T=2|0,15|143,92|144,32|144,16|144,33|0,00176|0,50|0,35|1,61|0,30|
|D2|arriba junta|580,98|5,5807|T=2|0,15|143,90|144,28|144,12|144,29|0,00153|0,48|0,37|1,68|0,28|
|D2|arriba junta|601,4|5,3711|T=2|0,15|143,89|144,26|144,09|144,27|0,00125|0,44|0,40|1,77|0,26|
|D2|arriba junta|621,65|5,1614|T=2|0,15|143,87|144,24|144,05|144,24|0,00094|0,40|0,44|1,89|0,23|
|D2|arriba junta|636,55|5|T=2|0,15|143,86|144,22|144,02|144,23|0,00074|0,37|0,48|2,01|0,20|
|D2|arriba junta|647,85|4|T=2|0,15|143,91|144,21|144,08|144,22|0,00163|0,42|0,38|1,97|0,29|
|D3|arriba junta|0|9|T=2|0,10|144,95|145,10|145,06|145,11|0,00441|0,48|0,26|3,10|0,43|
|D3|arriba junta|19,85|8,7368|T=2|0,10|144,81|144,99|144,94|145,01|0,00585|0,65|0,17|1,25|0,51|
|D3|arriba junta|39,67|8,4737|T=2|0,10|144,68|144,89|144,81|144,91|0,00477|0,67|0,16|0,97|0,48|
|D3|arriba junta|59,49|8,2105|T=2|0,10|144,54|144,81|144,70|144,83|0,00309|0,65|0,17|0,80|0,41|
|D3|arriba junta|75,33|8|T=2|0,10|144,43|144,77|144,62|144,79|0,00243|0,67|0,18|0,69|0,37|
|D3|arriba junta|95,39|7,759|T=2|0,10|144,39|144,72|0,00|144,74|0,00239|0,65|0,19|0,75|0,37|
|D3|arriba junta|115,46|7,5181|T=2|0,10|144,36|144,67|0,00|144,69|0,00223|0,62|0,20|0,88|0,36|
|D3|arriba junta|135,52|7,2771|T=2|0,10|144,32|144,64|0,00|144,65|0,00171|0,54|0,23|1,15|0,31|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.8 de A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|arriba junta|155,6|7,0361|T=2|0,10|144,29|144,62|0,00|144,62|0,00093|0,41|0,31|1,40|0,23|
|D3|arriba junta|158,61|7|T=2|0,10|144,28|144,62|0,00|144,62|0,00083|0,39|0,33|1,42|0,22|
|D3|arriba junta|198,72|6,42|T=2|0,10|144,22|144,59|0,00|144,60|0,00125|0,44|0,26|1,19|0,25|
|D3|arriba junta|218,77|6,18|T=2|0,10|144,20|144,56|0,00|144,57|0,00161|0,45|0,24|1,07|0,27|
|D3|arriba junta|237,8|6|T=2|0,10|144,17|144,52|144,40|144,53|0,00262|0,49|0,21|1,05|0,33|
|D3|arriba junta|257,8|5,802|T=2|0,10|144,13|144,47|144,35|144,48|0,00256|0,49|0,21|1,07|0,33|
|D3|arriba junta|277,79|5,604|T=2|0,10|144,10|144,42|144,31|144,43|0,00257|0,49|0,21|1,11|0,34|
|D3|arriba junta|297,78|5,4059|T=2|0,10|144,06|144,37|144,26|144,38|0,00254|0,49|0,21|1,15|0,34|
|D3|arriba junta|317,75|5,2079|T=2|0,10|144,02|144,32|144,21|144,33|0,00266|0,49|0,21|1,19|0,35|
|D3|arriba junta|337,72|5,0099|T=2|0,10|143,98|144,26|144,16|144,27|0,00325|0,51|0,20|1,21|0,38|
|D3|arriba junta|338,72|5|T=2|0,10|143,98|144,25|144,16|144,27|0,00327|0,52|0,20|1,22|0,38|
|D3|arriba junta|358,41|4,8131|T=2|0,10|143,91|144,22|144,07|144,23|0,00118|0,37|0,28|1,35|0,24|
|D3|arriba junta|378,39|4,6262|T=2|0,10|143,83|144,21|143,98|144,21|0,00043|0,27|0,40|1,50|0,15|
|D3|arriba junta|398,88|4,4393|T=2|0,10|143,76|144,21|143,90|144,21|0,00019|0,21|0,54|1,72|0,11|
|D3|arriba junta|420,1|4,2523|T=2|0,10|143,69|144,20|143,82|144,21|0,00009|0,17|0,70|1,93|0,08|
|D3|arriba junta|440,31|4,0654|T=2|0,10|143,62|144,20|143,74|144,20|0,00005|0,14|0,84|1,93|0,06|
|D3|arriba junta|445,94|4|T=2|0,10|143,59|144,20|143,71|144,20|0,00004|0,13|0,88|1,89|0,06|
|D3|bajo junta|452,26|3|T=2|0,25|143,95|144,18|144,12|144,20|0,00526|0,65|0,42|2,82|0,49|
|D3|bajo junta|471,1|2|T=2|0,25|143,64|144,16|143,91|144,16|0,00084|0,42|0,68|2,19|0,22|
|D3|bajo junta|491,09|1,6942|T=2|0,25|143,66|144,14|143,92|144,15|0,00089|0,46|0,65|2,29|0,23|
|D3|bajo junta|511,09|1,3884|T=2|0,25|143,68|144,11|143,92|144,12|0,00130|0,52|0,57|2,32|0,27|
|D3|bajo junta|531,1|1,0826|T=2|0,25|143,70|144,06|143,95|144,09|0,00315|0,64|0,41|1,78|0,40|
|D3|bajo junta|536,51|1|T=2|0,25|143,71|144,03|143,96|144,06|0,00600|0,77|0,34|1,76|0,54|
||||||||||||||||

A.5 Eje hidráulico Sin Proyecto - T=5 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=5|0,20|144,50|144,92|144,71|144,93|0,00087|0,44|0,57|2,25|0,23|
|D2|arriba junta|59,77|11,794|T=5|0,20|144,48|144,91|144,70|144,91|0,00095|0,45|0,55|2,25|0,24|
|D2|arriba junta|79,77|11,589|T=5|0,20|144,47|144,89|144,69|144,89|0,00103|0,47|0,54|2,25|0,25|
|D2|arriba junta|99,8|11,383|T=5|0,20|144,45|144,86|144,67|144,87|0,00112|0,48|0,53|2,26|0,26|
|D2|arriba junta|119,84|11,178|T=5|0,20|144,43|144,84|144,66|144,85|0,00121|0,49|0,52|2,34|0,26|
|D2|arriba junta|137,16|11|T=5|0,20|144,42|144,82|144,64|144,83|0,00123|0,49|0,52|2,31|0,27|
|D2|arriba junta|157,14|10,755|T=5|0,20|144,34|144,80|144,59|144,81|0,00103|0,48|0,54|2,23|0,24|
|D2|arriba junta|177,14|10,51|T=5|0,20|144,27|144,78|144,54|144,79|0,00087|0,46|0,56|2,06|0,22|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.9 de A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|197,15|10,265|T=5|0,20|144,19|144,76|144,48|144,77|0,00080|0,44|0,58|1,98|0,20|
|D2|arriba junta|217,16|10,02|T=5|0,20|144,12|144,75|144,45|144,75|0,00085|0,41|0,57|1,85|0,19|
|D2|arriba junta|218,76|10|T=5|0,20|144,11|144,74|144,45|144,75|0,00086|0,41|0,57|1,84|0,19|
|D2|arriba junta|238,71|9,6435|T=5|0,20|144,09|144,73|144,40|144,74|0,00045|0,34|0,71|2,15|0,16|
|D2|arriba junta|258,85|9,287|T=5|0,20|144,07|144,73|144,35|144,73|0,00025|0,27|0,87|2,43|0,12|
|D2|arriba junta|274,9|9|T=5|0,20|144,05|144,73|144,32|144,73|0,00017|0,22|1,02|2,70|0,10|
|D2|arriba junta|294,69|8,7528|T=5|0,20|144,04|144,72|144,32|144,72|0,00019|0,24|0,98|2,68|0,11|
|D2|arriba junta|314,91|8,5056|T=5|0,20|144,04|144,72|144,32|144,72|0,00022|0,26|0,94|2,66|0,12|
|D2|arriba junta|335|8,2583|T=5|0,20|144,03|144,71|144,33|144,72|0,00027|0,27|0,89|2,66|0,12|
|D2|arriba junta|354,94|8,0111|T=5|0,20|144,02|144,71|144,33|144,71|0,00033|0,29|0,84|2,65|0,13|
|D2|arriba junta|355,82|8|T=5|0,20|144,02|144,71|144,33|144,71|0,00034|0,29|0,84|2,65|0,13|
|D2|arriba junta|375,18|7,775|T=5|0,20|144,07|144,70|144,37|144,70|0,00044|0,34|0,77|2,63|0,15|
|D2|arriba junta|395,64|7,5501|T=5|0,20|144,12|144,69|144,42|144,69|0,00060|0,39|0,69|2,59|0,18|
|D2|arriba junta|416,02|7,3251|T=5|0,20|144,18|144,67|144,46|144,68|0,00089|0,46|0,60|2,54|0,22|
|D2|arriba junta|435,99|7,1001|T=5|0,20|144,23|144,64|144,49|144,65|0,00160|0,54|0,49|2,44|0,29|
|D2|arriba junta|444,77|7|T=5|0,20|144,25|144,62|144,50|144,64|0,00238|0,59|0,43|2,34|0,35|
|D2|arriba junta|464,76|6,7923|T=5|0,20|144,18|144,57|144,45|144,59|0,00245|0,65|0,41|2,17|0,36|
|D2|arriba junta|485,72|6,5846|T=5|0,20|144,12|144,52|144,40|144,54|0,00243|0,67|0,40|2,01|0,36|
|D2|arriba junta|505,61|6,3769|T=5|0,20|144,05|144,48|144,34|144,49|0,00230|0,65|0,40|1,87|0,34|
|D2|arriba junta|524,94|6,1693|T=5|0,20|143,98|144,43|144,27|144,45|0,00210|0,61|0,41|1,75|0,32|
|D2|arriba junta|541,11|6|T=5|0,20|143,93|144,40|144,22|144,41|0,00194|0,56|0,42|1,68|0,31|
|D2|arriba junta|560,93|5,7904|T=5|0,20|143,92|144,36|144,19|144,38|0,00176|0,55|0,43|1,74|0,30|
|D2|arriba junta|580,98|5,5807|T=5|0,20|143,90|144,33|144,15|144,34|0,00154|0,53|0,45|1,81|0,29|
|D2|arriba junta|601,4|5,3711|T=5|0,20|143,89|144,30|144,12|144,31|0,00127|0,50|0,48|1,90|0,27|
|D2|arriba junta|621,65|5,1614|T=5|0,20|143,87|144,28|144,08|144,29|0,00099|0,45|0,53|2,03|0,24|
|D2|arriba junta|636,55|5|T=5|0,20|143,86|144,27|144,05|144,28|0,00079|0,41|0,58|2,16|0,22|
|D2|arriba junta|647,85|4|T=5|0,20|143,91|144,26|144,11|144,27|0,00151|0,46|0,47|2,10|0,28|
|D3|arriba junta|0|9|T=5|0,13|144,95|145,13|145,07|145,14|0,00344|0,48|0,34|3,54|0,39|
|D3|arriba junta|19,85|8,7368|T=5|0,13|144,81|145,02|144,96|145,05|0,00565|0,72|0,22|2,18|0,52|
|D3|arriba junta|39,67|8,4737|T=5|0,13|144,68|144,93|144,84|144,95|0,00416|0,71|0,20|1,03|0,46|
|D3|arriba junta|59,49|8,2105|T=5|0,13|144,54|144,86|144,73|144,88|0,00288|0,70|0,21|0,86|0,40|
|D3|arriba junta|75,33|8|T=5|0,13|144,43|144,81|144,65|144,84|0,00256|0,75|0,21|0,73|0,39|
|D3|arriba junta|95,39|7,759|T=5|0,13|144,39|144,76|0,00|144,79|0,00253|0,73|0,22|0,80|0,39|
|D3|arriba junta|115,46|7,5181|T=5|0,13|144,36|144,72|0,00|144,74|0,00232|0,69|0,24|1,00|0,37|
|D3|arriba junta|135,52|7,2771|T=5|0,13|144,32|144,68|0,00|144,70|0,00174|0,60|0,29|1,31|0,32|
|D3|arriba junta|155,6|7,0361|T=5|0,13|144,29|144,66|0,00|144,67|0,00096|0,46|0,37|1,51|0,24|
|D3|arriba junta|158,61|7|T=5|0,13|144,28|144,66|0,00|144,67|0,00087|0,44|0,39|1,53|0,23|
|D3|arriba junta|198,72|6,42|T=5|0,13|144,22|144,63|0,00|144,64|0,00133|0,49|0,31|1,33|0,26|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.10 de<br>A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|arriba junta|218,77|6,18|T=5|0,13|144,20|144,60|0,00|144,61|0,00171|0,50|0,28|1,14|0,29|
|D3|arriba junta|237,8|6|T=5|0,13|144,17|144,56|144,42|144,57|0,00265|0,55|0,25|1,10|0,34|
|D3|arriba junta|257,8|5,802|T=5|0,13|144,13|144,51|144,38|144,52|0,00259|0,54|0,25|1,13|0,34|
|D3|arriba junta|277,79|5,604|T=5|0,13|144,10|144,45|144,33|144,47|0,00258|0,54|0,25|1,16|0,35|
|D3|arriba junta|297,78|5,4059|T=5|0,13|144,06|144,40|144,28|144,42|0,00255|0,54|0,25|1,20|0,35|
|D3|arriba junta|317,75|5,2079|T=5|0,13|144,02|144,35|144,23|144,37|0,00256|0,53|0,26|1,25|0,35|
|D3|arriba junta|337,72|5,0099|T=5|0,13|143,98|144,30|144,19|144,32|0,00263|0,53|0,26|1,29|0,35|
|D3|arriba junta|338,72|5|T=5|0,13|143,98|144,30|144,18|144,31|0,00262|0,53|0,26|1,30|0,35|
|D3|arriba junta|358,41|4,8131|T=5|0,13|143,91|144,27|144,09|144,28|0,00103|0,40|0,35|1,44|0,23|
|D3|arriba junta|378,39|4,6262|T=5|0,13|143,83|144,26|144,00|144,27|0,00043|0,30|0,48|1,59|0,16|
|D3|arriba junta|398,88|4,4393|T=5|0,13|143,76|144,26|143,92|144,26|0,00020|0,24|0,63|1,90|0,11|
|D3|arriba junta|420,1|4,2523|T=5|0,13|143,69|144,26|143,84|144,26|0,00011|0,19|0,80|2,05|0,08|
|D3|arriba junta|440,31|4,0654|T=5|0,13|143,62|144,25|143,76|144,26|0,00006|0,16|0,94|2,00|0,07|
|D3|arriba junta|445,94|4|T=5|0,13|143,59|144,25|143,73|144,25|0,00006|0,16|0,98|1,95|0,06|
|D3|bajo junta|452,26|3|T=5|0,33|143,95|144,23|144,14|144,25|0,00361|0,64|0,57|3,10|0,43|
|D3|bajo junta|471,1|2|T=5|0,33|143,64|144,21|143,94|144,22|0,00095|0,49|0,79|2,31|0,23|
|D3|bajo junta|491,09|1,6942|T=5|0,33|143,66|144,19|143,95|144,20|0,00100|0,53|0,77|2,46|0,25|
|D3|bajo junta|511,09|1,3884|T=5|0,33|143,68|144,16|143,95|144,17|0,00141|0,58|0,67|2,47|0,29|
|D3|bajo junta|531,1|1,0826|T=5|0,33|143,70|144,10|143,98|144,13|0,00338|0,73|0,48|1,85|0,43|
|D3|bajo junta|536,51|1|T=5|0,33|143,71|144,07|143,99|144,11|0,00600|0,86|0,41|1,82|0,55|
||||||||||||||||

A.6 Eje hidráulico Sin Proyecto - T=10 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=10|0,24|144,50|144,96|144,73|144,97|0,00088|0,46|0,65|2,41|0,23|
|D2|arriba junta|59,77|11,794|T=10|0,24|144,48|144,94|144,72|144,95|0,00095|0,48|0,63|2,41|0,24|
|D2|arriba junta|79,77|11,589|T=10|0,24|144,47|144,92|144,71|144,93|0,00102|0,49|0,62|2,41|0,25|
|D2|arriba junta|99,8|11,383|T=10|0,24|144,45|144,90|144,69|144,91|0,00109|0,50|0,61|2,42|0,26|
|D2|arriba junta|119,84|11,178|T=10|0,24|144,43|144,88|144,68|144,89|0,00116|0,51|0,61|2,56|0,26|
|D2|arriba junta|137,16|11|T=10|0,24|144,42|144,86|144,66|144,87|0,00116|0,51|0,61|2,49|0,26|
|D2|arriba junta|157,14|10,755|T=10|0,24|144,34|144,83|144,61|144,84|0,00100|0,51|0,63|2,42|0,24|
|D2|arriba junta|177,14|10,51|T=10|0,24|144,27|144,82|144,56|144,83|0,00088|0,49|0,64|2,23|0,22|
|D2|arriba junta|197,15|10,265|T=10|0,24|144,19|144,80|144,51|144,81|0,00084|0,47|0,65|2,14|0,21|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.11 de<br>A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|217,16|10,02|T=10|0,24|144,12|144,78|144,48|144,79|0,00090|0,44|0,64|1,97|0,20|
|D2|arriba junta|218,76|10|T=10|0,24|144,11|144,78|144,47|144,79|0,00091|0,44|0,64|1,95|0,20|
|D2|arriba junta|238,71|9,6435|T=10|0,24|144,09|144,77|144,42|144,78|0,00049|0,37|0,79|2,29|0,17|
|D2|arriba junta|258,85|9,287|T=10|0,24|144,07|144,76|144,37|144,77|0,00028|0,30|0,96|2,60|0,13|
|D2|arriba junta|274,9|9|T=10|0,24|144,05|144,76|144,34|144,76|0,00019|0,25|1,12|2,80|0,11|
|D2|arriba junta|294,69|8,7528|T=10|0,24|144,04|144,76|144,34|144,76|0,00022|0,27|1,07|2,81|0,12|
|D2|arriba junta|314,91|8,5056|T=10|0,24|144,04|144,75|144,34|144,75|0,00025|0,28|1,03|2,82|0,12|
|D2|arriba junta|335|8,2583|T=10|0,24|144,03|144,75|144,35|144,75|0,00030|0,30|0,98|2,81|0,13|
|D2|arriba junta|354,94|8,0111|T=10|0,24|144,02|144,74|144,35|144,74|0,00037|0,32|0,93|2,80|0,14|
|D2|arriba junta|355,82|8|T=10|0,24|144,02|144,74|144,35|144,74|0,00038|0,32|0,93|2,80|0,14|
|D2|arriba junta|375,18|7,775|T=10|0,24|144,07|144,73|144,39|144,73|0,00048|0,37|0,85|2,78|0,16|
|D2|arriba junta|395,64|7,5501|T=10|0,24|144,12|144,72|144,44|144,72|0,00065|0,42|0,77|2,75|0,19|
|D2|arriba junta|416,02|7,3251|T=10|0,24|144,18|144,70|144,49|144,71|0,00094|0,49|0,68|2,71|0,23|
|D2|arriba junta|435,99|7,1001|T=10|0,24|144,23|144,67|144,51|144,68|0,00161|0,57|0,57|2,61|0,30|
|D2|arriba junta|444,77|7|T=10|0,24|144,25|144,65|144,52|144,67|0,00230|0,62|0,50|2,52|0,35|
|D2|arriba junta|464,76|6,7923|T=10|0,24|144,18|144,60|144,47|144,62|0,00237|0,67|0,48|2,33|0,36|
|D2|arriba junta|485,72|6,5846|T=10|0,24|144,12|144,55|144,42|144,57|0,00234|0,69|0,47|2,14|0,35|
|D2|arriba junta|505,61|6,3769|T=10|0,24|144,05|144,51|144,36|144,53|0,00222|0,68|0,46|1,99|0,34|
|D2|arriba junta|524,94|6,1693|T=10|0,24|143,98|144,47|144,29|144,48|0,00206|0,64|0,47|1,86|0,33|
|D2|arriba junta|541,11|6|T=10|0,24|143,93|144,44|144,25|144,45|0,00194|0,60|0,47|1,78|0,31|
|D2|arriba junta|560,93|5,7904|T=10|0,24|143,92|144,40|144,21|144,41|0,00174|0,59|0,49|1,83|0,31|
|D2|arriba junta|580,98|5,5807|T=10|0,24|143,90|144,37|144,17|144,38|0,00152|0,56|0,52|1,91|0,29|
|D2|arriba junta|601,4|5,3711|T=10|0,24|143,89|144,34|144,14|144,35|0,00125|0,53|0,55|2,01|0,27|
|D2|arriba junta|621,65|5,1614|T=10|0,24|143,87|144,32|144,10|144,33|0,00098|0,48|0,61|2,14|0,24|
|D2|arriba junta|636,55|5|T=10|0,24|143,86|144,31|144,07|144,32|0,00080|0,44|0,66|2,27|0,22|
|D2|arriba junta|647,85|4|T=10|0,24|143,91|144,29|144,12|144,30|0,00137|0,48|0,55|2,21|0,28|
|D3|arriba junta|0|9|T=10|0,15|144,95|145,14|145,08|145,15|0,00325|0,49|0,39|3,62|0,38|
|D3|arriba junta|19,85|8,7368|T=10|0,15|144,81|145,04|144,97|145,07|0,00499|0,72|0,26|2,41|0,50|
|D3|arriba junta|39,67|8,4737|T=10|0,15|144,68|144,95|144,85|144,98|0,00385|0,73|0,23|1,07|0,45|
|D3|arriba junta|59,49|8,2105|T=10|0,15|144,54|144,89|144,74|144,91|0,00279|0,73|0,24|0,89|0,40|
|D3|arriba junta|75,33|8|T=10|0,15|144,43|144,84|144,67|144,87|0,00264|0,80|0,23|0,76|0,40|
|D3|arriba junta|95,39|7,759|T=10|0,15|144,39|144,79|0,00|144,82|0,00262|0,78|0,24|0,85|0,40|
|D3|arriba junta|115,46|7,5181|T=10|0,15|144,36|144,74|0,00|144,76|0,00237|0,73|0,26|1,08|0,38|
|D3|arriba junta|135,52|7,2771|T=10|0,15|144,32|144,71|0,00|144,72|0,00174|0,63|0,32|1,41|0,32|
|D3|arriba junta|155,6|7,0361|T=10|0,15|144,29|144,69|0,00|144,69|0,00098|0,48|0,41|1,57|0,24|
|D3|arriba junta|158,61|7|T=10|0,15|144,28|144,68|0,00|144,69|0,00089|0,46|0,43|1,59|0,23|
|D3|arriba junta|198,72|6,42|T=10|0,15|144,22|144,66|0,00|144,67|0,00136|0,52|0,35|1,43|0,27|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.12 de<br>A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|arriba junta|218,77|6,18|T=10|0,15|144,20|144,62|0,00|144,64|0,00176|0,53|0,31|1,18|0,30|
|D3|arriba junta|237,8|6|T=10|0,15|144,17|144,58|144,44|144,60|0,00265|0,58|0,27|1,13|0,35|
|D3|arriba junta|257,8|5,802|T=10|0,15|144,13|144,53|144,39|144,54|0,00257|0,57|0,28|1,16|0,35|
|D3|arriba junta|277,79|5,604|T=10|0,15|144,10|144,48|144,34|144,49|0,00254|0,57|0,28|1,20|0,35|
|D3|arriba junta|297,78|5,4059|T=10|0,15|144,06|144,43|144,29|144,44|0,00244|0,56|0,28|1,24|0,34|
|D3|arriba junta|317,75|5,2079|T=10|0,15|144,02|144,38|144,25|144,39|0,00235|0,55|0,29|1,30|0,34|
|D3|arriba junta|337,72|5,0099|T=10|0,15|143,98|144,33|144,20|144,35|0,00218|0,53|0,30|1,36|0,33|
|D3|arriba junta|338,72|5|T=10|0,15|143,98|144,33|144,20|144,35|0,00216|0,53|0,30|1,36|0,33|
|D3|arriba junta|358,41|4,8131|T=10|0,15|143,91|144,31|144,10|144,32|0,00089|0,40|0,41|1,50|0,22|
|D3|arriba junta|378,39|4,6262|T=10|0,15|143,83|144,30|144,01|144,31|0,00040|0,31|0,54|1,66|0,15|
|D3|arriba junta|398,88|4,4393|T=10|0,15|143,76|144,30|143,93|144,30|0,00020|0,25|0,71|2,04|0,11|
|D3|arriba junta|420,1|4,2523|T=10|0,15|143,69|144,30|143,85|144,30|0,00011|0,20|0,88|2,15|0,09|
|D3|arriba junta|440,31|4,0654|T=10|0,15|143,62|144,29|143,77|144,30|0,00007|0,17|1,02|2,07|0,07|
|D3|arriba junta|445,94|4|T=10|0,15|143,59|144,29|143,74|144,29|0,00006|0,17|1,05|2,01|0,07|
|D3|bajo junta|452,26|3|T=10|0,40|143,95|144,27|144,16|144,29|0,00294|0,64|0,70|3,32|0,40|
|D3|bajo junta|471,1|2|T=10|0,40|143,64|144,25|143,96|144,26|0,00104|0,54|0,89|2,43|0,25|
|D3|bajo junta|491,09|1,6942|T=10|0,40|143,66|144,22|143,99|144,24|0,00107|0,57|0,86|2,57|0,26|
|D3|bajo junta|511,09|1,3884|T=10|0,40|143,68|144,19|143,98|144,21|0,00149|0,63|0,76|2,67|0,30|
|D3|bajo junta|531,1|1,0826|T=10|0,40|143,70|144,13|144,00|144,17|0,00353|0,80|0,54|2,34|0,45|
|D3|bajo junta|536,51|1|T=10|0,40|143,71|144,10|144,01|144,14|0,00600|0,92|0,46|1,87|0,56|
||||||||||||||||

A.7 Eje hidráulico Sin Proyecto - T=20 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=20|0,30|144,50|145,01|144,76|145,02|0,00088|0,50|0,77|2,62|0,24|
|D2|arriba junta|59,77|11,794|T=20|0,30|144,48|144,99|144,75|145,00|0,00095|0,52|0,75|2,63|0,25|
|D2|arriba junta|79,77|11,589|T=20|0,30|144,47|144,97|144,73|144,98|0,00100|0,53|0,74|2,62|0,25|
|D2|arriba junta|99,8|11,383|T=20|0,30|144,45|144,95|144,72|144,96|0,00107|0,54|0,73|2,67|0,26|
|D2|arriba junta|119,84|11,178|T=20|0,30|144,43|144,92|144,71|144,93|0,00110|0,54|0,74|2,86|0,26|
|D2|arriba junta|137,16|11|T=20|0,30|144,42|144,91|144,69|144,92|0,00108|0,53|0,74|2,73|0,26|
|D2|arriba junta|157,14|10,755|T=20|0,30|144,34|144,89|144,64|144,90|0,00096|0,54|0,76|2,67|0,24|
|D2|arriba junta|177,14|10,51|T=20|0,30|144,27|144,87|144,59|144,88|0,00091|0,53|0,76|2,54|0,23|
|D2|arriba junta|197,15|10,265|T=20|0,30|144,19|144,85|144,54|144,86|0,00088|0,51|0,76|2,35|0,22|
|D2|arriba junta|217,16|10,02|T=20|0,30|144,12|144,83|144,51|144,84|0,00096|0,49|0,74|2,12|0,21|
|D2|arriba junta|218,76|10|T=20|0,30|144,11|144,83|144,51|144,84|0,00098|0,48|0,73|2,10|0,21|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.13 de<br>A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|238,71|9,6435|T=20|0,30|144,09|144,82|144,45|144,82|0,00054|0,41|0,90|2,46|0,18|
|D2|arriba junta|258,85|9,287|T=20|0,30|144,07|144,81|144,40|144,81|0,00032|0,34|1,09|2,82|0,14|
|D2|arriba junta|274,9|9|T=20|0,30|144,05|144,81|144,37|144,81|0,00022|0,28|1,25|3,08|0,12|
|D2|arriba junta|294,69|8,7528|T=20|0,30|144,04|144,80|144,37|144,81|0,00025|0,30|1,21|3,06|0,13|
|D2|arriba junta|314,91|8,5056|T=20|0,30|144,04|144,80|144,37|144,80|0,00029|0,32|1,16|3,04|0,14|
|D2|arriba junta|335|8,2583|T=20|0,30|144,03|144,79|144,38|144,79|0,00034|0,34|1,11|3,02|0,14|
|D2|arriba junta|354,94|8,0111|T=20|0,30|144,02|144,78|144,39|144,79|0,00042|0,35|1,05|3,00|0,15|
|D2|arriba junta|355,82|8|T=20|0,30|144,02|144,78|144,39|144,79|0,00042|0,35|1,05|3,00|0,15|
|D2|arriba junta|375,18|7,775|T=20|0,30|144,07|144,77|144,43|144,78|0,00053|0,41|0,97|2,98|0,17|
|D2|arriba junta|395,64|7,5501|T=20|0,30|144,12|144,76|144,48|144,76|0,00070|0,47|0,88|2,96|0,20|
|D2|arriba junta|416,02|7,3251|T=20|0,30|144,18|144,74|144,51|144,75|0,00099|0,53|0,79|2,93|0,24|
|D2|arriba junta|435,99|7,1001|T=20|0,30|144,23|144,71|144,54|144,72|0,00162|0,61|0,67|2,85|0,30|
|D2|arriba junta|444,77|7|T=20|0,30|144,25|144,69|144,54|144,71|0,00220|0,65|0,60|2,77|0,35|
|D2|arriba junta|464,76|6,7923|T=20|0,30|144,18|144,64|144,50|144,66|0,00225|0,71|0,58|2,54|0,35|
|D2|arriba junta|485,72|6,5846|T=20|0,30|144,12|144,60|144,45|144,62|0,00222|0,72|0,56|2,33|0,35|
|D2|arriba junta|505,61|6,3769|T=20|0,30|144,05|144,55|144,39|144,57|0,00213|0,71|0,56|2,16|0,34|
|D2|arriba junta|524,94|6,1693|T=20|0,30|143,98|144,51|144,33|144,53|0,00201|0,68|0,56|2,01|0,33|
|D2|arriba junta|541,11|6|T=20|0,30|143,93|144,48|144,28|144,50|0,00193|0,65|0,56|1,91|0,32|
|D2|arriba junta|560,93|5,7904|T=20|0,30|143,92|144,45|144,24|144,46|0,00173|0,63|0,58|1,96|0,31|
|D2|arriba junta|580,98|5,5807|T=20|0,30|143,90|144,41|144,20|144,43|0,00150|0,61|0,61|2,04|0,30|
|D2|arriba junta|601,4|5,3711|T=20|0,30|143,89|144,39|144,16|144,40|0,00125|0,57|0,65|2,14|0,28|
|D2|arriba junta|621,65|5,1614|T=20|0,30|143,87|144,37|144,12|144,38|0,00099|0,52|0,71|2,28|0,25|
|D2|arriba junta|636,55|5|T=20|0,30|143,86|144,35|144,09|144,36|0,00081|0,48|0,77|2,42|0,23|
|D2|arriba junta|647,85|4|T=20|0,30|143,91|144,34|144,14|144,35|0,00128|0,51|0,66|2,34|0,27|
|D3|arriba junta|0|9|T=20|0,19|144,95|145,16|145,10|145,17|0,00316|0,52|0,46|3,73|0,39|
|D3|arriba junta|19,85|8,7368|T=20|0,19|144,81|145,08|144,99|145,10|0,00380|0,70|0,36|2,84|0,45|
|D3|arriba junta|39,67|8,4737|T=20|0,19|144,68|145,00|144,88|145,03|0,00332|0,76|0,30|1,82|0,43|
|D3|arriba junta|59,49|8,2105|T=20|0,19|144,54|144,94|144,77|144,97|0,00268|0,79|0,29|1,05|0,40|
|D3|arriba junta|75,33|8|T=20|0,19|144,43|144,89|144,71|144,92|0,00280|0,89|0,27|0,80|0,42|
|D3|arriba junta|95,39|7,759|T=20|0,19|144,39|144,84|0,00|144,87|0,00275|0,86|0,28|1,01|0,42|
|D3|arriba junta|115,46|7,5181|T=20|0,19|144,36|144,79|0,00|144,81|0,00251|0,81|0,32|1,33|0,40|
|D3|arriba junta|135,52|7,2771|T=20|0,19|144,32|144,75|0,00|144,77|0,00171|0,67|0,39|1,58|0,33|
|D3|arriba junta|155,6|7,0361|T=20|0,19|144,29|144,73|0,00|144,74|0,00102|0,53|0,49|1,81|0,25|
|D3|arriba junta|158,61|7|T=20|0,19|144,28|144,73|0,00|144,74|0,00095|0,51|0,50|1,87|0,25|
|D3|arriba junta|198,72|6,42|T=20|0,19|144,22|144,70|0,00|144,71|0,00139|0,56|0,41|1,60|0,28|
|D3|arriba junta|218,77|6,18|T=20|0,19|144,20|144,67|0,00|144,68|0,00184|0,59|0,36|1,24|0,31|
|D3|arriba junta|237,8|6|T=20|0,19|144,17|144,62|144,47|144,64|0,00267|0,63|0,32|1,19|0,36|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.14 de<br>A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|arriba junta|257,8|5,802|T=20|0,19|144,13|144,57|144,42|144,59|0,00259|0,63|0,32|1,22|0,36|
|D3|arriba junta|277,79|5,604|T=20|0,19|144,10|144,52|144,37|144,54|0,00253|0,62|0,33|1,26|0,35|
|D3|arriba junta|297,78|5,4059|T=20|0,19|144,06|144,47|144,32|144,49|0,00238|0,61|0,34|1,31|0,35|
|D3|arriba junta|317,75|5,2079|T=20|0,19|144,02|144,42|144,27|144,44|0,00220|0,59|0,35|1,37|0,34|
|D3|arriba junta|337,72|5,0099|T=20|0,19|143,98|144,38|144,22|144,40|0,00192|0,56|0,37|1,44|0,32|
|D3|arriba junta|338,72|5|T=20|0,19|143,98|144,38|144,22|144,40|0,00190|0,56|0,37|1,45|0,32|
|D3|arriba junta|358,41|4,8131|T=20|0,19|143,91|144,36|144,13|144,37|0,00086|0,43|0,49|1,59|0,22|
|D3|arriba junta|378,39|4,6262|T=20|0,19|143,83|144,35|144,03|144,36|0,00042|0,34|0,63|1,90|0,16|
|D3|arriba junta|398,88|4,4393|T=20|0,19|143,76|144,35|143,95|144,35|0,00022|0,28|0,82|2,22|0,12|
|D3|arriba junta|420,1|4,2523|T=20|0,19|143,69|144,35|143,87|144,35|0,00012|0,23|0,99|2,27|0,09|
|D3|arriba junta|440,31|4,0654|T=20|0,19|143,62|144,34|143,79|144,35|0,00008|0,20|1,12|2,14|0,08|
|D3|arriba junta|445,94|4|T=20|0,19|143,59|144,34|143,77|144,34|0,00007|0,20|1,16|2,07|0,07|
|D3|bajo junta|452,26|3|T=20|0,50|143,95|144,32|144,18|144,34|0,00243|0,65|0,87|3,60|0,37|
|D3|bajo junta|471,1|2|T=20|0,50|143,64|144,29|143,99|144,31|0,00115|0,60|1,01|2,60|0,26|
|D3|bajo junta|491,09|1,6942|T=20|0,50|143,66|144,27|144,02|144,29|0,00117|0,63|0,99|2,75|0,27|
|D3|bajo junta|511,09|1,3884|T=20|0,50|143,68|144,24|144,01|144,26|0,00157|0,69|0,89|3,04|0,32|
|D3|bajo junta|531,1|1,0826|T=20|0,50|143,70|144,17|144,03|144,21|0,00362|0,88|0,66|3,17|0,46|
|D3|bajo junta|536,51|1|T=20|0,50|143,71|144,14|144,04|144,18|0,00601|1,01|0,54|2,58|0,58|
||||||||||||||||

A.8 Eje hidráulico Sin Proyecto - T=25 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=25|0,31|144,50|145,01|144,76|145,02|0,00088|0,51|0,79|2,65|0,24|
|D2|arriba junta|59,77|11,794|T=25|0,31|144,48|144,99|144,75|145,00|0,00095|0,52|0,77|2,68|0,25|
|D2|arriba junta|79,77|11,589|T=25|0,31|144,47|144,97|144,74|144,98|0,00100|0,53|0,76|2,66|0,25|
|D2|arriba junta|99,8|11,383|T=25|0,31|144,45|144,95|144,72|144,96|0,00107|0,54|0,75|2,73|0,26|
|D2|arriba junta|119,84|11,178|T=25|0,31|144,43|144,93|144,71|144,94|0,00109|0,54|0,76|2,90|0,26|
|D2|arriba junta|137,16|11|T=25|0,31|144,42|144,91|144,69|144,92|0,00107|0,53|0,76|2,77|0,26|
|D2|arriba junta|157,14|10,755|T=25|0,31|144,34|144,89|144,65|144,90|0,00096|0,54|0,78|2,71|0,24|
|D2|arriba junta|177,14|10,51|T=25|0,31|144,27|144,87|144,60|144,88|0,00092|0,54|0,78|2,60|0,23|
|D2|arriba junta|197,15|10,265|T=25|0,31|144,19|144,86|144,54|144,87|0,00089|0,52|0,78|2,38|0,22|
|D2|arriba junta|217,16|10,02|T=25|0,31|144,12|144,84|144,51|144,85|0,00097|0,49|0,75|2,14|0,21|
|D2|arriba junta|218,76|10|T=25|0,31|144,11|144,84|144,51|144,85|0,00099|0,49|0,75|2,12|0,21|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.15 de<br>A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|238,71|9,6435|T=25|0,31|144,09|144,82|144,45|144,83|0,00055|0,42|0,92|2,49|0,18|
|D2|arriba junta|258,85|9,287|T=25|0,31|144,07|144,82|144,40|144,82|0,00033|0,34|1,11|2,86|0,15|
|D2|arriba junta|274,9|9|T=25|0,31|144,05|144,81|144,37|144,82|0,00023|0,29|1,28|3,13|0,12|
|D2|arriba junta|294,69|8,7528|T=25|0,31|144,04|144,81|144,38|144,81|0,00026|0,31|1,23|3,09|0,13|
|D2|arriba junta|314,91|8,5056|T=25|0,31|144,04|144,80|144,38|144,81|0,00030|0,33|1,18|3,07|0,14|
|D2|arriba junta|335|8,2583|T=25|0,31|144,03|144,80|144,38|144,80|0,00035|0,35|1,13|3,05|0,15|
|D2|arriba junta|354,94|8,0111|T=25|0,31|144,02|144,79|144,39|144,79|0,00043|0,36|1,07|3,03|0,15|
|D2|arriba junta|355,82|8|T=25|0,31|144,02|144,79|144,39|144,79|0,00043|0,36|1,07|3,03|0,15|
|D2|arriba junta|375,18|7,775|T=25|0,31|144,07|144,78|144,43|144,78|0,00054|0,41|0,99|3,01|0,17|
|D2|arriba junta|395,64|7,5501|T=25|0,31|144,12|144,76|144,48|144,77|0,00071|0,47|0,90|2,99|0,20|
|D2|arriba junta|416,02|7,3251|T=25|0,31|144,18|144,74|144,52|144,75|0,00100|0,54|0,80|2,96|0,24|
|D2|arriba junta|435,99|7,1001|T=25|0,31|144,23|144,72|144,54|144,73|0,00162|0,61|0,69|2,88|0,30|
|D2|arriba junta|444,77|7|T=25|0,31|144,25|144,70|144,55|144,71|0,00219|0,66|0,62|2,80|0,35|
|D2|arriba junta|464,76|6,7923|T=25|0,31|144,18|144,65|144,50|144,67|0,00224|0,71|0,59|2,57|0,35|
|D2|arriba junta|485,72|6,5846|T=25|0,31|144,12|144,60|144,45|144,62|0,00221|0,73|0,58|2,36|0,35|
|D2|arriba junta|505,61|6,3769|T=25|0,31|144,05|144,56|144,39|144,58|0,00213|0,72|0,57|2,18|0,34|
|D2|arriba junta|524,94|6,1693|T=25|0,31|143,98|144,52|144,33|144,54|0,00201|0,69|0,57|2,03|0,33|
|D2|arriba junta|541,11|6|T=25|0,31|143,93|144,49|144,28|144,50|0,00194|0,65|0,57|1,93|0,32|
|D2|arriba junta|560,93|5,7904|T=25|0,31|143,92|144,45|144,24|144,47|0,00174|0,64|0,59|1,98|0,31|
|D2|arriba junta|580,98|5,5807|T=25|0,31|143,90|144,42|144,21|144,43|0,00152|0,62|0,62|2,05|0,30|
|D2|arriba junta|601,4|5,3711|T=25|0,31|143,89|144,39|144,17|144,41|0,00126|0,58|0,66|2,16|0,28|
|D2|arriba junta|621,65|5,1614|T=25|0,31|143,87|144,37|144,13|144,38|0,00101|0,53|0,72|2,29|0,25|
|D2|arriba junta|636,55|5|T=25|0,31|143,86|144,36|144,10|144,37|0,00083|0,49|0,78|2,44|0,23|
|D2|arriba junta|647,85|4|T=25|0,31|143,91|144,34|144,15|144,36|0,00129|0,52|0,67|2,35|0,28|
|D3|arriba junta|0|9|T=25|0,20|144,95|145,16|145,10|145,18|0,00309|0,53|0,48|3,75|0,38|
|D3|arriba junta|19,85|8,7368|T=25|0,20|144,81|145,09|145,00|145,11|0,00359|0,69|0,38|2,95|0,43|
|D3|arriba junta|39,67|8,4737|T=25|0,20|144,68|145,01|144,88|145,04|0,00318|0,76|0,32|2,06|0,43|
|D3|arriba junta|59,49|8,2105|T=25|0,20|144,54|144,95|144,78|144,98|0,00266|0,80|0,30|1,22|0,40|
|D3|arriba junta|75,33|8|T=25|0,20|144,43|144,90|144,72|144,94|0,00284|0,91|0,28|0,81|0,43|
|D3|arriba junta|95,39|7,759|T=25|0,20|144,39|144,85|0,00|144,88|0,00278|0,88|0,29|1,05|0,42|
|D3|arriba junta|115,46|7,5181|T=25|0,20|144,36|144,80|0,00|144,82|0,00253|0,82|0,33|1,40|0,40|
|D3|arriba junta|135,52|7,2771|T=25|0,20|144,32|144,76|0,00|144,78|0,00171|0,68|0,41|1,62|0,33|
|D3|arriba junta|155,6|7,0361|T=25|0,20|144,29|144,74|0,00|144,75|0,00103|0,54|0,51|1,88|0,26|
|D3|arriba junta|158,61|7|T=25|0,20|144,28|144,74|0,00|144,75|0,00096|0,52|0,52|1,94|0,25|
|D3|arriba junta|198,72|6,42|T=25|0,20|144,22|144,71|0,00|144,73|0,00140|0,57|0,43|1,64|0,28|
|D3|arriba junta|218,77|6,18|T=25|0,20|144,20|144,68|0,00|144,69|0,00186|0,61|0,37|1,29|0,31|
|D3|arriba junta|237,8|6|T=25|0,20|144,17|144,63|144,47|144,65|0,00268|0,65|0,33|1,20|0,36|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.16 de<br>A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|arriba junta|257,8|5,802|T=25|0,20|144,13|144,58|144,42|144,60|0,00259|0,64|0,33|1,24|0,36|
|D3|arriba junta|277,79|5,604|T=25|0,20|144,10|144,53|144,37|144,55|0,00253|0,63|0,34|1,28|0,36|
|D3|arriba junta|297,78|5,4059|T=25|0,20|144,06|144,48|144,32|144,50|0,00240|0,62|0,35|1,33|0,35|
|D3|arriba junta|317,75|5,2079|T=25|0,20|144,02|144,43|144,27|144,45|0,00222|0,60|0,36|1,39|0,34|
|D3|arriba junta|337,72|5,0099|T=25|0,20|143,98|144,39|144,23|144,41|0,00196|0,57|0,38|1,46|0,32|
|D3|arriba junta|338,72|5|T=25|0,20|143,98|144,39|144,23|144,40|0,00194|0,57|0,38|1,46|0,32|
|D3|arriba junta|358,41|4,8131|T=25|0,20|143,91|144,37|144,13|144,38|0,00090|0,45|0,50|1,60|0,23|
|D3|arriba junta|378,39|4,6262|T=25|0,20|143,83|144,36|144,04|144,36|0,00045|0,36|0,65|1,94|0,17|
|D3|arriba junta|398,88|4,4393|T=25|0,20|143,76|144,35|143,96|144,36|0,00023|0,29|0,83|2,25|0,12|
|D3|arriba junta|420,1|4,2523|T=25|0,20|143,69|144,35|143,87|144,35|0,00013|0,24|1,01|2,28|0,10|
|D3|arriba junta|440,31|4,0654|T=25|0,20|143,62|144,35|143,80|144,35|0,00009|0,21|1,14|2,15|0,08|
|D3|arriba junta|445,94|4|T=25|0,20|143,59|144,35|143,77|144,35|0,00008|0,20|1,17|2,08|0,08|
|D3|bajo junta|452,26|3|T=25|0,51|143,95|144,33|144,18|144,35|0,00236|0,65|0,89|3,63|0,37|
|D3|bajo junta|471,1|2|T=25|0,51|143,64|144,30|144,00|144,31|0,00115|0,61|1,02|2,62|0,27|
|D3|bajo junta|491,09|1,6942|T=25|0,51|143,66|144,28|144,02|144,29|0,00116|0,64|1,00|2,78|0,27|
|D3|bajo junta|511,09|1,3884|T=25|0,51|143,68|144,24|144,01|144,26|0,00166|0,71|0,90|3,23|0,32|
|D3|bajo junta|531,1|1,0826|T=25|0,51|143,70|144,18|144,04|144,21|0,00361|0,88|0,67|3,20|0,46|
|D3|bajo junta|536,51|1|T=25|0,51|143,71|144,14|144,05|144,19|0,00601|1,02|0,55|2,64|0,58|
||||||||||||||||

A.9 Eje hidráulico Sin Proyecto - T=50 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=50|0,40|144,50|145,07|144,80|145,08|0,00088|0,55|0,96|2,93|0,24|
|D2|arriba junta|59,77|11,794|T=50|0,40|144,48|145,05|144,79|145,07|0,00094|0,56|0,94|3,03|0,25|
|D2|arriba junta|79,77|11,589|T=50|0,40|144,47|145,03|144,77|145,05|0,00100|0,58|0,93|3,08|0,26|
|D2|arriba junta|99,8|11,383|T=50|0,40|144,45|145,01|144,76|145,03|0,00106|0,59|0,93|3,26|0,26|
|D2|arriba junta|119,84|11,178|T=50|0,40|144,43|144,99|144,74|145,00|0,00102|0,57|0,95|3,28|0,26|
|D2|arriba junta|137,16|11|T=50|0,40|144,42|144,98|144,73|144,99|0,00100|0,57|0,94|3,07|0,26|
|D2|arriba junta|157,14|10,755|T=50|0,40|144,34|144,96|144,69|144,97|0,00093|0,57|0,96|3,04|0,24|
|D2|arriba junta|177,14|10,51|T=50|0,40|144,27|144,94|144,64|144,95|0,00095|0,59|0,96|3,14|0,24|
|D2|arriba junta|197,15|10,265|T=50|0,40|144,19|144,92|144,59|144,93|0,00094|0,57|0,94|2,72|0,23|
|D2|arriba junta|217,16|10,02|T=50|0,40|144,12|144,90|144,55|144,91|0,00104|0,55|0,89|2,34|0,22|
|D2|arriba junta|218,76|10|T=50|0,40|144,11|144,90|144,55|144,91|0,00106|0,55|0,88|2,31|0,22|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.17 de<br>A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|238,71|9,6435|T=50|0,40|144,09|144,88|144,49|144,89|0,00061|0,47|1,07|2,71|0,19|
|D2|arriba junta|258,85|9,287|T=50|0,40|144,07|144,88|144,44|144,88|0,00037|0,39|1,28|3,14|0,16|
|D2|arriba junta|274,9|9|T=50|0,40|144,05|144,87|144,40|144,88|0,00027|0,33|1,47|3,54|0,13|
|D2|arriba junta|294,69|8,7528|T=50|0,40|144,04|144,87|144,41|144,87|0,00030|0,35|1,41|3,43|0,14|
|D2|arriba junta|314,91|8,5056|T=50|0,40|144,04|144,86|144,41|144,86|0,00034|0,37|1,36|3,35|0,15|
|D2|arriba junta|335|8,2583|T=50|0,40|144,03|144,85|144,42|144,86|0,00040|0,39|1,30|3,31|0,16|
|D2|arriba junta|354,94|8,0111|T=50|0,40|144,02|144,84|144,43|144,85|0,00048|0,41|1,25|3,28|0,16|
|D2|arriba junta|355,82|8|T=50|0,40|144,02|144,84|144,43|144,85|0,00049|0,41|1,24|3,28|0,16|
|D2|arriba junta|375,18|7,775|T=50|0,40|144,07|144,83|144,47|144,84|0,00060|0,46|1,16|3,27|0,18|
|D2|arriba junta|395,64|7,5501|T=50|0,40|144,12|144,81|144,52|144,82|0,00077|0,52|1,06|3,26|0,21|
|D2|arriba junta|416,02|7,3251|T=50|0,40|144,18|144,79|144,55|144,81|0,00105|0,58|0,96|3,25|0,25|
|D2|arriba junta|435,99|7,1001|T=50|0,40|144,23|144,77|144,57|144,78|0,00160|0,66|0,84|3,19|0,31|
|D2|arriba junta|444,77|7|T=50|0,40|144,25|144,75|144,58|144,76|0,00206|0,70|0,77|3,13|0,34|
|D2|arriba junta|464,76|6,7923|T=50|0,40|144,18|144,70|144,54|144,72|0,00210|0,75|0,74|2,85|0,35|
|D2|arriba junta|485,72|6,5846|T=50|0,40|144,12|144,66|144,49|144,68|0,00208|0,77|0,72|2,61|0,35|
|D2|arriba junta|505,61|6,3769|T=50|0,40|144,05|144,62|144,43|144,64|0,00204|0,76|0,70|2,40|0,34|
|D2|arriba junta|524,94|6,1693|T=50|0,40|143,98|144,58|144,37|144,60|0,00198|0,74|0,70|2,22|0,33|
|D2|arriba junta|541,11|6|T=50|0,40|143,93|144,55|144,32|144,57|0,00195|0,71|0,69|2,09|0,33|
|D2|arriba junta|560,93|5,7904|T=50|0,40|143,92|144,51|144,28|144,53|0,00175|0,70|0,71|2,15|0,32|
|D2|arriba junta|580,98|5,5807|T=50|0,40|143,90|144,48|144,24|144,50|0,00154|0,67|0,75|2,23|0,31|
|D2|arriba junta|601,4|5,3711|T=50|0,40|143,89|144,45|144,20|144,47|0,00130|0,63|0,79|2,34|0,29|
|D2|arriba junta|621,65|5,1614|T=50|0,40|143,87|144,43|144,16|144,44|0,00105|0,58|0,86|2,51|0,26|
|D2|arriba junta|636,55|5|T=50|0,40|143,86|144,42|144,13|144,43|0,00088|0,54|0,93|2,72|0,24|
|D2|arriba junta|647,85|4|T=50|0,40|143,91|144,40|144,18|144,42|0,00127|0,57|0,81|2,51|0,28|
|D3|arriba junta|0|9|T=50|0,25|144,95|145,19|145,11|145,20|0,00276|0,54|0,58|3,89|0,37|
|D3|arriba junta|19,85|8,7368|T=50|0,25|144,81|145,13|145,05|145,15|0,00276|0,67|0,51|3,40|0,39|
|D3|arriba junta|39,67|8,4737|T=50|0,25|144,68|145,07|144,91|145,09|0,00262|0,76|0,45|2,74|0,40|
|D3|arriba junta|59,49|8,2105|T=50|0,25|144,54|145,01|144,82|145,04|0,00250|0,85|0,38|1,71|0,40|
|D3|arriba junta|75,33|8|T=50|0,25|144,43|144,95|144,76|144,99|0,00307|1,01|0,32|1,01|0,45|
|D3|arriba junta|95,39|7,759|T=50|0,25|144,39|144,89|0,00|144,93|0,00290|0,96|0,35|1,49|0,44|
|D3|arriba junta|115,46|7,5181|T=50|0,25|144,36|144,85|0,00|144,88|0,00249|0,88|0,41|1,73|0,40|
|D3|arriba junta|135,52|7,2771|T=50|0,25|144,32|144,81|0,00|144,83|0,00171|0,73|0,49|1,96|0,33|
|D3|arriba junta|155,6|7,0361|T=50|0,25|144,29|144,79|0,00|144,80|0,00108|0,59|0,61|2,34|0,27|
|D3|arriba junta|158,61|7|T=50|0,25|144,28|144,79|0,00|144,80|0,00101|0,57|0,63|2,40|0,26|
|D3|arriba junta|198,72|6,42|T=50|0,25|144,22|144,76|0,00|144,78|0,00141|0,62|0,51|1,91|0,29|
|D3|arriba junta|218,77|6,18|T=50|0,25|144,20|144,72|0,00|144,74|0,00193|0,66|0,44|1,57|0,32|
|D3|arriba junta|237,8|6|T=50|0,25|144,17|144,67|144,50|144,70|0,00269|0,70|0,38|1,26|0,37|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.18 de<br>A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|arriba junta|257,8|5,802|T=50|0,25|144,13|144,62|144,45|144,65|0,00258|0,69|0,39|1,30|0,36|
|D3|arriba junta|277,79|5,604|T=50|0,25|144,10|144,57|144,40|144,59|0,00248|0,69|0,40|1,35|0,36|
|D3|arriba junta|297,78|5,4059|T=50|0,25|144,06|144,52|144,35|144,55|0,00228|0,66|0,41|1,41|0,35|
|D3|arriba junta|317,75|5,2079|T=50|0,25|144,02|144,48|144,30|144,50|0,00204|0,64|0,43|1,48|0,33|
|D3|arriba junta|337,72|5,0099|T=50|0,25|143,98|144,45|144,25|144,46|0,00172|0,60|0,47|1,56|0,31|
|D3|arriba junta|338,72|5|T=50|0,25|143,98|144,45|144,25|144,46|0,00169|0,59|0,47|1,56|0,31|
|D3|arriba junta|358,41|4,8131|T=50|0,25|143,91|144,43|144,16|144,44|0,00084|0,48|0,60|1,71|0,23|
|D3|arriba junta|378,39|4,6262|T=50|0,25|143,83|144,42|144,07|144,42|0,00045|0,39|0,77|2,25|0,17|
|D3|arriba junta|398,88|4,4393|T=50|0,25|143,76|144,41|143,98|144,42|0,00024|0,31|0,97|2,46|0,13|
|D3|arriba junta|420,1|4,2523|T=50|0,25|143,69|144,41|143,90|144,41|0,00015|0,27|1,14|2,42|0,10|
|D3|arriba junta|440,31|4,0654|T=50|0,25|143,62|144,41|143,82|144,41|0,00010|0,24|1,26|2,24|0,09|
|D3|arriba junta|445,94|4|T=50|0,25|143,59|144,41|143,79|144,41|0,00009|0,23|1,29|2,15|0,08|
|D3|bajo junta|452,26|3|T=50|0,65|143,95|144,39|144,21|144,41|0,00206|0,68|1,11|3,95|0,35|
|D3|bajo junta|471,1|2|T=50|0,65|143,64|144,36|144,04|144,37|0,00130|0,69|1,18|2,86|0,29|
|D3|bajo junta|491,09|1,6942|T=50|0,65|143,66|144,33|144,06|144,35|0,00130|0,72|1,16|2,99|0,29|
|D3|bajo junta|511,09|1,3884|T=50|0,65|143,68|144,29|144,08|144,32|0,00176|0,78|1,07|3,62|0,34|
|D3|bajo junta|531,1|1,0826|T=50|0,65|143,70|144,23|144,08|144,27|0,00364|0,96|0,84|3,95|0,47|
|D3|bajo junta|536,51|1|T=50|0,65|143,71|144,18|144,08|144,24|0,00600|1,11|0,69|3,50|0,59|

A.10 Eje hidráulico Sin Proyecto - T=100 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=100|0,46|144,50|145,11|144,82|145,12|0,00088|0,57|1,06|3,09|0,24|
|D2|arriba junta|59,77|11,794|T=100|0,46|144,48|145,09|144,81|145,10|0,00094|0,59|1,06|3,24|0,25|
|D2|arriba junta|79,77|11,589|T=100|0,46|144,47|145,07|144,79|145,08|0,00100|0,60|1,05|3,36|0,26|
|D2|arriba junta|99,8|11,383|T=100|0,46|144,45|145,05|144,78|145,06|0,00105|0,61|1,06|3,64|0,27|
|D2|arriba junta|119,84|11,178|T=100|0,46|144,43|145,03|144,76|145,04|0,00096|0,58|1,08|3,38|0,25|
|D2|arriba junta|137,16|11|T=100|0,46|144,42|145,01|144,75|145,03|0,00097|0,58|1,06|3,25|0,25|
|D2|arriba junta|157,14|10,755|T=100|0,46|144,34|144,99|144,71|145,01|0,00097|0,61|1,09|3,62|0,25|
|D2|arriba junta|177,14|10,51|T=100|0,46|144,27|144,97|144,66|144,99|0,00095|0,61|1,08|3,46|0,24|
|D2|arriba junta|197,15|10,265|T=100|0,46|144,19|144,96|144,61|144,97|0,00097|0,60|1,04|2,96|0,23|
|D2|arriba junta|217,16|10,02|T=100|0,46|144,12|144,93|144,58|144,95|0,00108|0,58|0,97|2,45|0,23|
|D2|arriba junta|218,76|10|T=100|0,46|144,11|144,93|144,58|144,95|0,00110|0,58|0,97|2,42|0,23|
|D2|arriba junta|238,71|9,6435|T=100|0,46|144,09|144,92|144,51|144,93|0,00064|0,50|1,17|2,84|0,20|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.19 de<br>A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|258,85|9,287|T=100|0,46|144,07|144,91|144,46|144,92|0,00041|0,42|1,39|3,57|0,17|
|D2|arriba junta|274,9|9|T=100|0,46|144,05|144,91|144,42|144,91|0,00023|0,32|2,08|7,64|0,13|
|D2|arriba junta|294,69|8,7528|T=100|0,46|144,04|144,90|144,43|144,91|0,00033|0,38|1,54|3,87|0,15|
|D2|arriba junta|314,91|8,5056|T=100|0,46|144,04|144,89|144,43|144,90|0,00037|0,40|1,48|3,80|0,16|
|D2|arriba junta|335|8,2583|T=100|0,46|144,03|144,88|144,44|144,89|0,00043|0,42|1,42|3,48|0,16|
|D2|arriba junta|354,94|8,0111|T=100|0,46|144,02|144,87|144,45|144,88|0,00052|0,43|1,35|3,43|0,17|
|D2|arriba junta|355,82|8|T=100|0,46|144,02|144,87|144,45|144,88|0,00052|0,43|1,35|3,43|0,17|
|D2|arriba junta|375,18|7,775|T=100|0,46|144,07|144,86|144,50|144,87|0,00064|0,49|1,26|3,43|0,19|
|D2|arriba junta|395,64|7,5501|T=100|0,46|144,12|144,85|144,54|144,85|0,00080|0,55|1,16|3,43|0,22|
|D2|arriba junta|416,02|7,3251|T=100|0,46|144,18|144,82|144,57|144,84|0,00107|0,61|1,06|3,42|0,25|
|D2|arriba junta|435,99|7,1001|T=100|0,46|144,23|144,80|144,59|144,81|0,00158|0,68|0,94|3,37|0,31|
|D2|arriba junta|444,77|7|T=100|0,46|144,25|144,78|144,60|144,79|0,00198|0,72|0,87|3,32|0,34|
|D2|arriba junta|464,76|6,7923|T=100|0,46|144,18|144,74|144,56|144,75|0,00201|0,76|0,83|3,02|0,35|
|D2|arriba junta|485,72|6,5846|T=100|0,46|144,12|144,69|144,51|144,71|0,00201|0,79|0,81|2,75|0,35|
|D2|arriba junta|505,61|6,3769|T=100|0,46|144,05|144,65|144,46|144,67|0,00198|0,78|0,79|2,53|0,34|
|D2|arriba junta|524,94|6,1693|T=100|0,46|143,98|144,61|144,39|144,63|0,00195|0,77|0,78|2,33|0,33|
|D2|arriba junta|541,11|6|T=100|0,46|143,93|144,58|144,34|144,60|0,00194|0,75|0,77|2,19|0,33|
|D2|arriba junta|560,93|5,7904|T=100|0,46|143,92|144,55|144,30|144,57|0,00175|0,74|0,79|2,27|0,33|
|D2|arriba junta|580,98|5,5807|T=100|0,46|143,90|144,51|144,26|144,53|0,00154|0,71|0,83|2,37|0,31|
|D2|arriba junta|601,4|5,3711|T=100|0,46|143,89|144,49|144,22|144,50|0,00131|0,67|0,88|2,51|0,29|
|D2|arriba junta|621,65|5,1614|T=100|0,46|143,87|144,46|144,18|144,48|0,00107|0,62|0,95|2,74|0,27|
|D2|arriba junta|636,55|5|T=100|0,46|143,86|144,45|144,15|144,46|0,00091|0,58|1,03|3,05|0,25|
|D2|arriba junta|647,85|4|T=100|0,46|143,91|144,44|144,20|144,45|0,00125|0,59|0,90|2,61|0,28|
|D3|arriba junta|0|9|T=100|0,29|144,95|145,21|145,12|145,22|0,00252|0,55|0,66|4,00|0,36|
|D3|arriba junta|19,85|8,7368|T=100|0,29|144,81|145,16|145,06|145,17|0,00235|0,65|0,61|3,56|0,37|
|D3|arriba junta|39,67|8,4737|T=100|0,29|144,68|145,11|144,94|145,13|0,00209|0,73|0,57|3,07|0,36|
|D3|arriba junta|59,49|8,2105|T=100|0,29|144,54|145,05|144,84|145,08|0,00240|0,88|0,46|2,10|0,40|
|D3|arriba junta|75,33|8|T=100|0,29|144,43|144,99|144,79|145,04|0,00313|1,07|0,36|1,19|0,46|
|D3|arriba junta|95,39|7,759|T=100|0,29|144,39|144,93|0,00|144,97|0,00314|1,04|0,42|2,26|0,46|
|D3|arriba junta|115,46|7,5181|T=100|0,29|144,36|144,88|0,00|144,91|0,00249|0,92|0,48|2,21|0,41|
|D3|arriba junta|135,52|7,2771|T=100|0,29|144,32|144,85|0,00|144,87|0,00172|0,77|0,57|2,38|0,34|
|D3|arriba junta|155,6|7,0361|T=100|0,29|144,29|144,83|0,00|144,84|0,00109|0,62|0,70|2,69|0,27|
|D3|arriba junta|158,61|7|T=100|0,29|144,28|144,82|0,00|144,83|0,00102|0,60|0,72|2,75|0,26|
|D3|arriba junta|198,72|6,42|T=100|0,29|144,22|144,79|0,00|144,81|0,00142|0,65|0,58|2,18|0,29|
|D3|arriba junta|218,77|6,18|T=100|0,29|144,20|144,75|0,00|144,78|0,00195|0,70|0,49|1,76|0,33|
|D3|arriba junta|237,8|6|T=100|0,29|144,17|144,71|144,52|144,73|0,00270|0,74|0,43|1,31|0,37|
|D3|arriba junta|257,8|5,802|T=100|0,29|144,13|144,65|144,47|144,68|0,00258|0,73|0,43|1,35|0,37|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.20 de<br>A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|arriba junta|277,79|5,604|T=100|0,29|144,10|144,60|144,42|144,63|0,00245|0,72|0,44|1,40|0,36|
|D3|arriba junta|297,78|5,4059|T=100|0,29|144,06|144,56|144,37|144,58|0,00223|0,70|0,46|1,46|0,35|
|D3|arriba junta|317,75|5,2079|T=100|0,29|144,02|144,52|144,32|144,54|0,00197|0,67|0,49|1,54|0,33|
|D3|arriba junta|337,72|5,0099|T=100|0,29|143,98|144,48|144,27|144,50|0,00164|0,62|0,53|1,63|0,31|
|D3|arriba junta|338,72|5|T=100|0,29|143,98|144,48|144,27|144,50|0,00162|0,62|0,53|1,63|0,31|
|D3|arriba junta|358,41|4,8131|T=100|0,29|143,91|144,46|144,17|144,48|0,00086|0,51|0,66|1,91|0,23|
|D3|arriba junta|378,39|4,6262|T=100|0,29|143,83|144,46|144,08|144,46|0,00046|0,41|0,86|2,45|0,17|
|D3|arriba junta|398,88|4,4393|T=100|0,29|143,76|144,45|144,00|144,46|0,00026|0,34|1,06|2,59|0,13|
|D3|arriba junta|420,1|4,2523|T=100|0,29|143,69|144,45|143,91|144,45|0,00016|0,29|1,24|2,51|0,11|
|D3|arriba junta|440,31|4,0654|T=100|0,29|143,62|144,44|143,83|144,45|0,00012|0,26|1,35|2,30|0,09|
|D3|arriba junta|445,94|4|T=100|0,29|143,59|144,44|143,81|144,45|0,00011|0,26|1,37|2,20|0,09|
|D3|bajo junta|452,26|3|T=100|0,75|143,95|144,42|144,23|144,44|0,00176|0,67|1,46|6,20|0,33|
|D3|bajo junta|471,1|2|T=100|0,75|143,64|144,39|144,06|144,41|0,00139|0,74|1,28|3,02|0,30|
|D3|bajo junta|491,09|1,6942|T=100|0,75|143,66|144,36|144,08|144,38|0,00154|0,81|1,26|3,58|0,32|
|D3|bajo junta|511,09|1,3884|T=100|0,75|143,68|144,32|144,10|144,35|0,00186|0,83|1,18|3,85|0,35|
|D3|bajo junta|531,1|1,0826|T=100|0,75|143,70|144,25|144,10|144,30|0,00360|0,99|0,96|4,30|0,47|
|D3|bajo junta|536,51|1|T=100|0,75|143,71|144,21|144,11|144,27|0,00601|1,16|0,78|3,79|0,60|
||||||||||||||||

A.11 Eje hidráulico Sin Proyecto - T=200 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=200|0,51|144,50|145,14|144,84|145,15|0,00088|0,59|1,15|3,22|0,25|
|D2|arriba junta|59,77|11,794|T=200|0,51|144,48|145,12|144,82|145,13|0,00093|0,61|1,15|3,40|0,25|
|D2|arriba junta|79,77|11,589|T=200|0,51|144,47|145,10|144,81|145,11|0,00100|0,62|1,14|3,55|0,26|
|D2|arriba junta|99,8|11,383|T=200|0,51|144,45|145,08|144,80|145,09|0,00099|0,62|1,16|3,64|0,26|
|D2|arriba junta|119,84|11,178|T=200|0,51|144,43|145,06|144,78|145,07|0,00094|0,60|1,18|3,54|0,25|
|D2|arriba junta|137,16|11|T=200|0,51|144,42|145,04|144,76|145,06|0,00094|0,60|1,16|3,39|0,25|
|D2|arriba junta|157,14|10,755|T=200|0,51|144,34|145,02|144,72|145,04|0,00092|0,61|1,20|3,71|0,25|
|D2|arriba junta|177,14|10,51|T=200|0,51|144,27|145,01|144,68|145,02|0,00096|0,64|1,20|3,90|0,24|
|D2|arriba junta|197,15|10,265|T=200|0,51|144,19|144,99|144,64|145,00|0,00102|0,63|1,14|3,33|0,24|
|D2|arriba junta|217,16|10,02|T=200|0,51|144,12|144,96|144,60|144,98|0,00114|0,61|1,05|2,61|0,24|
|D2|arriba junta|218,76|10|T=200|0,51|144,11|144,96|144,60|144,97|0,00116|0,61|1,04|2,57|0,24|
|D2|arriba junta|238,71|9,6435|T=200|0,51|144,09|144,95|144,53|144,96|0,00068|0,53|1,25|3,04|0,21|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.21 de<br>A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|258,85|9,287|T=200|0,51|144,07|144,94|144,48|144,94|0,00043|0,44|1,50|3,83|0,17|
|D2|arriba junta|274,9|9|T=200|0,51|144,05|144,94|144,44|144,94|0,00022|0,33|2,29|7,78|0,13|
|D2|arriba junta|294,69|8,7528|T=200|0,51|144,04|144,93|144,44|144,93|0,00035|0,40|1,65|4,19|0,15|
|D2|arriba junta|314,91|8,5056|T=200|0,51|144,04|144,92|144,45|144,93|0,00040|0,43|1,58|4,11|0,16|
|D2|arriba junta|335|8,2583|T=200|0,51|144,03|144,91|144,46|144,92|0,00046|0,45|1,51|3,72|0,17|
|D2|arriba junta|354,94|8,0111|T=200|0,51|144,02|144,90|144,47|144,91|0,00054|0,45|1,44|3,55|0,17|
|D2|arriba junta|355,82|8|T=200|0,51|144,02|144,90|144,47|144,91|0,00054|0,45|1,44|3,54|0,17|
|D2|arriba junta|375,18|7,775|T=200|0,51|144,07|144,89|144,52|144,89|0,00066|0,51|1,35|3,55|0,19|
|D2|arriba junta|395,64|7,5501|T=200|0,51|144,12|144,87|144,56|144,88|0,00082|0,57|1,25|3,55|0,22|
|D2|arriba junta|416,02|7,3251|T=200|0,51|144,18|144,85|144,59|144,86|0,00108|0,63|1,15|3,55|0,26|
|D2|arriba junta|435,99|7,1001|T=200|0,51|144,23|144,82|144,61|144,84|0,00156|0,70|1,02|3,56|0,31|
|D2|arriba junta|444,77|7|T=200|0,51|144,25|144,80|144,61|144,82|0,00198|0,74|0,95|3,58|0,34|
|D2|arriba junta|464,76|6,7923|T=200|0,51|144,18|144,76|144,57|144,78|0,00195|0,78|0,91|3,15|0,34|
|D2|arriba junta|485,72|6,5846|T=200|0,51|144,12|144,72|144,53|144,74|0,00196|0,80|0,88|2,87|0,34|
|D2|arriba junta|505,61|6,3769|T=200|0,51|144,05|144,68|144,47|144,70|0,00195|0,80|0,86|2,63|0,34|
|D2|arriba junta|524,94|6,1693|T=200|0,51|143,98|144,64|144,41|144,66|0,00194|0,79|0,84|2,42|0,34|
|D2|arriba junta|541,11|6|T=200|0,51|143,93|144,61|144,36|144,63|0,00196|0,78|0,83|2,27|0,33|
|D2|arriba junta|560,93|5,7904|T=200|0,51|143,92|144,57|144,32|144,59|0,00177|0,76|0,85|2,35|0,33|
|D2|arriba junta|580,98|5,5807|T=200|0,51|143,90|144,54|144,28|144,56|0,00156|0,74|0,89|2,46|0,32|
|D2|arriba junta|601,4|5,3711|T=200|0,51|143,89|144,51|144,24|144,53|0,00134|0,69|0,94|2,63|0,30|
|D2|arriba junta|621,65|5,1614|T=200|0,51|143,87|144,49|144,20|144,51|0,00111|0,65|1,02|2,91|0,28|
|D2|arriba junta|636,55|5|T=200|0,51|143,86|144,47|144,17|144,49|0,00094|0,60|1,10|3,27|0,25|
|D2|arriba junta|647,85|4|T=200|0,51|143,91|144,46|144,21|144,48|0,00127|0,62|0,96|2,68|0,29|
|D3|arriba junta|0|9|T=200|0,32|144,95|145,22|145,13|145,24|0,00240|0,56|0,71|4,07|0,35|
|D3|arriba junta|19,85|8,7368|T=200|0,32|144,81|145,17|145,07|145,19|0,00218|0,65|0,67|3,66|0,36|
|D3|arriba junta|39,67|8,4737|T=200|0,32|144,68|145,13|144,95|145,15|0,00191|0,72|0,64|3,18|0,35|
|D3|arriba junta|59,49|8,2105|T=200|0,32|144,54|145,07|144,86|145,11|0,00229|0,89|0,51|2,21|0,39|
|D3|arriba junta|75,33|8|T=200|0,32|144,43|145,01|144,81|145,06|0,00332|1,13|0,39|1,29|0,48|
|D3|arriba junta|95,39|7,759|T=200|0,32|144,39|144,95|0,00|144,99|0,00303|1,05|0,47|2,44|0,45|
|D3|arriba junta|115,46|7,5181|T=200|0,32|144,36|144,90|0,00|144,94|0,00241|0,93|0,53|2,44|0,40|
|D3|arriba junta|135,52|7,2771|T=200|0,32|144,32|144,87|0,00|144,89|0,00168|0,78|0,63|2,61|0,34|
|D3|arriba junta|155,6|7,0361|T=200|0,32|144,29|144,85|0,00|144,86|0,00108|0,64|0,77|2,94|0,27|
|D3|arriba junta|158,61|7|T=200|0,32|144,28|144,85|0,00|144,86|0,00101|0,62|0,79|3,00|0,26|
|D3|arriba junta|198,72|6,42|T=200|0,32|144,22|144,82|0,00|144,84|0,00142|0,67|0,64|2,43|0,29|
|D3|arriba junta|218,77|6,18|T=200|0,32|144,20|144,78|0,00|144,80|0,00195|0,72|0,54|1,95|0,33|
|D3|arriba junta|237,8|6|T=200|0,32|144,17|144,73|144,54|144,76|0,00270|0,77|0,46|1,34|0,38|
|D3|arriba junta|257,8|5,802|T=200|0,32|144,13|144,68|144,48|144,70|0,00258|0,76|0,46|1,39|0,37|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:**EH en modificación de trazado cauce IGM|**Hoja:** A.22 de<br>A.22|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch<br>El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|arriba junta|277,79|5,604|T=200|0,32|144,10|144,63|144,43|144,65|0,00243|0,75|0,48|1,44|0,37|
|D3|arriba junta|297,78|5,4059|T=200|0,32|144,06|144,58|144,38|144,61|0,00221|0,72|0,50|1,52|0,35|
|D3|arriba junta|317,75|5,2079|T=200|0,32|144,02|144,54|144,33|144,57|0,00194|0,69|0,53|1,59|0,33|
|D3|arriba junta|337,72|5,0099|T=200|0,32|143,98|144,51|144,29|144,53|0,00161|0,64|0,57|1,67|0,31|
|D3|arriba junta|338,72|5|T=200|0,32|143,98|144,51|144,28|144,53|0,00159|0,64|0,57|1,68|0,31|
|D3|arriba junta|358,41|4,8131|T=200|0,32|143,91|144,49|144,19|144,50|0,00088|0,53|0,72|2,12|0,24|
|D3|arriba junta|378,39|4,6262|T=200|0,32|143,83|144,48|144,10|144,49|0,00047|0,43|0,92|2,58|0,18|
|D3|arriba junta|398,88|4,4393|T=200|0,32|143,76|144,48|144,01|144,48|0,00027|0,35|1,13|2,68|0,14|
|D3|arriba junta|420,1|4,2523|T=200|0,32|143,69|144,47|143,93|144,48|0,00017|0,31|1,30|2,57|0,11|
|D3|arriba junta|440,31|4,0654|T=200|0,32|143,62|144,47|143,85|144,47|0,00013|0,28|1,41|2,34|0,10|
|D3|arriba junta|445,94|4|T=200|0,32|143,59|144,47|143,82|144,47|0,00012|0,27|1,43|2,23|0,09|
|D3|bajo junta|452,26|3|T=200|0,83|143,95|144,45|144,25|144,47|0,00162|0,67|1,63|6,68|0,32|
|D3|bajo junta|471,1|2|T=200|0,83|143,64|144,42|144,08|144,44|0,00140|0,77|1,45|4,31|0,30|
|D3|bajo junta|491,09|1,6942|T=200|0,83|143,66|144,38|144,10|144,41|0,00162|0,85|1,34|3,77|0,33|
|D3|bajo junta|511,09|1,3884|T=200|0,83|143,68|144,34|144,12|144,37|0,00192|0,87|1,27|4,03|0,36|
|D3|bajo junta|531,1|1,0826|T=200|0,83|143,70|144,28|144,12|144,32|0,00350|1,01|1,06|4,58|0,47|
|D3|bajo junta|536,51|1|T=200|0,83|143,71|144,23|144,14|144,29|0,00600|1,20|0,87|4,32|0,60|
||||||||||||||||

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.1 de B.1|

**ANEXO B**

**Situación Con Proyecto**

**Ejes Hidráulicos crecidas de probabilidad de excedencia**
**95%, 80% y 60%; y 2, 5, 10, 20, 50, 100 y 200 años de**

**retorno**

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.1 de B.18|

B.1 Eje hidráulico Con Proyecto - Probabilidad de excedencia 95%

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|Pexc 95%|0,11|144,50|144,85|144,66|144,85|0,00063|0,32|0,41|1,96|0,19|
|D2|arriba junta|61,4|11|Pexc 95%|0,11|144,63|144,82|0,00|144,84|0,00085|0,60|0,21|1,37|0,44|
|D2|arriba junta|81,4|10,722|Pexc 95%|0,11|144,61|144,81|0,00|144,82|0,00079|0,59|0,21|1,38|0,43|
|D2|arriba junta|101,4|10,444|Pexc 95%|0,11|144,59|144,79|0,00|144,81|0,00071|0,57|0,22|1,40|0,41|
|D2|arriba junta|121,4|10,167|Pexc 95%|0,11|144,57|144,78|0,00|144,79|0,00062|0,54|0,23|1,42|0,38|
|D2|arriba junta|133,4|10|Pexc 95%|0,11|144,56|144,77|0,00|144,78|0,00057|0,53|0,24|1,44|0,37|
|D2|arriba junta|153,4|9,8601|Pexc 95%|0,11|144,54|144,76|0,00|144,77|0,00047|0,50|0,25|1,47|0,34|
|D2|arriba junta|173,4|9,7203|Pexc 95%|0,11|144,52|144,76|0,00|144,76|0,00038|0,47|0,27|1,51|0,31|
|D2|arriba junta|193,4|9,5804|Pexc 95%|0,11|144,50|144,75|0,00|144,76|0,00031|0,44|0,29|1,55|0,28|
|D2|arriba junta|213,4|9,4406|Pexc 95%|0,11|144,48|144,74|0,00|144,75|0,00025|0,41|0,32|1,60|0,25|
|D2|arriba junta|233,4|9,3007|Pexc 95%|0,11|144,46|144,74|0,00|144,75|0,00020|0,38|0,34|1,65|0,23|
|D2|arriba junta|253,4|9,1608|Pexc 95%|0,11|144,44|144,74|0,00|144,74|0,00016|0,35|0,37|1,70|0,20|
|D2|arriba junta|273,4|9,021|Pexc 95%|0,11|144,42|144,74|0,00|144,74|0,00013|0,33|0,40|1,75|0,19|
|D2|arriba junta|276,4|9|Pexc 95%|0,11|144,42|144,74|0,00|144,74|0,00012|0,32|0,41|1,76|0,18|
|D2|arriba junta|296,4|8,8519|Pexc 95%|0,11|144,40|144,73|0,00|144,74|0,00010|0,30|0,44|1,81|0,17|
|D2|arriba junta|316,4|8,7037|Pexc 95%|0,11|144,38|144,73|0,00|144,74|0,00008|0,28|0,48|1,87|0,15|
|D2|arriba junta|336,4|8,5556|Pexc 95%|0,11|144,36|144,73|0,00|144,73|0,00007|0,26|0,51|1,93|0,14|
|D2|arriba junta|356,4|8,4074|Pexc 95%|0,11|144,34|144,73|0,00|144,73|0,00005|0,25|0,55|1,98|0,13|
|D2|arriba junta|376,4|8,2593|Pexc 95%|0,11|144,31|144,73|0,00|144,73|0,00004|0,23|0,59|2,04|0,11|
|D2|arriba junta|396,4|8,1111|Pexc 95%|0,11|144,30|144,73|0,00|144,73|0,00004|0,22|0,63|2,10|0,11|
|D2|arriba junta|411,4|8|Pexc 95%|0,11|144,28|144,73|144,40|144,73|0,00003|0,21|0,66|2,15|0,10|
|D3|arriba junta|0|9|Pexc 95%|0,07|144,95|145,08|145,04|145,09|0,00497|0,45|0,19|2,70|0,44|
|D3|arriba junta|19,85|8,7368|Pexc 95%|0,07|144,81|144,96|144,92|144,98|0,00616|0,58|0,13|1,17|0,51|
|D3|arriba junta|39,67|8,4737|Pexc 95%|0,07|144,68|144,85|144,79|144,86|0,00506|0,60|0,13|0,91|0,48|
|D3|arriba junta|59,49|8,2105|Pexc 95%|0,07|144,54|144,79|144,67|144,80|0,00201|0,50|0,16|0,78|0,32|
|D3|arriba junta|75,33|8|Pexc 95%|0,07|144,43|144,77|144,58|144,78|0,00118|0,47|0,18|0,69|0,26|
|D3|arriba junta|95,39|7,759|Pexc 95%|0,07|144,39|144,75|0,00|144,76|0,00084|0,41|0,21|0,78|0,22|
|D3|arriba junta|115,46|7,5181|Pexc 95%|0,07|144,36|144,74|0,00|144,74|0,00054|0,34|0,26|1,07|0,18|
|D3|arriba junta|135,52|7,2771|Pexc 95%|0,07|144,32|144,73|0,00|144,73|0,00029|0,27|0,36|1,51|0,13|
|D3|arriba junta|155,6|7,0361|Pexc 95%|0,07|144,29|144,73|0,00|144,73|0,00014|0,20|0,48|1,80|0,09|
|D3|arriba junta|158,61|7|Pexc 95%|0,07|144,28|144,73|144,40|144,73|0,00013|0,19|0,50|1,87|0,09|
|D3|bajo junta|178,67|6,9|Pexc 95%|0,17|144,28|144,72|0,00|144,73|0,00080|0,47|0,49|1,83|0,23|
|D3|bajo junta|198,72|6,42|Pexc 95%|0,17|144,22|144,67|0,00|144,69|0,00147|0,55|0,37|1,48|0,28|
|D3|bajo junta|218,77|6,18|Pexc 95%|0,17|144,19|144,64|0,00|144,65|0,00195|0,57|0,32|1,19|0,31|
|D3|bajo junta|237,8|6|Pexc 95%|0,17|144,17|144,60|144,45|144,62|0,00271|0,61|0,29|1,16|0,36|
|D3|bajo junta|257,8|5,802|Pexc 95%|0,17|144,13|144,55|144,40|144,56|0,00268|0,61|0,30|1,19|0,36|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.2 de B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|bajo junta|277,79|5,604|Pexc 95%|0,17|144,10|144,49|144,35|144,51|0,00271|0,61|0,30|1,22|0,36|
|D3|bajo junta|297,78|5,4059|Pexc 95%|0,17|144,06|144,44|144,31|144,46|0,00277|0,61|0,30|1,26|0,37|
|D3|bajo junta|317,75|5,2079|Pexc 95%|0,17|144,02|144,38|144,26|144,40|0,00303|0,62|0,29|1,29|0,39|
|D3|bajo junta|337,72|5,0099|Pexc 95%|0,17|143,98|144,30|144,21|144,33|0,00446|0,70|0,26|1,30|0,46|
|D3|bajo junta|338,72|5|Pexc 95%|0,17|143,98|144,30|144,21|144,32|0,00459|0,70|0,26|1,29|0,47|
|D3|bajo junta|358,41|4,8131|Pexc 95%|0,17|143,91|144,22|144,11|144,24|0,00338|0,64|0,28|1,35|0,41|
|D3|bajo junta|378,39|4,6262|Pexc 95%|0,17|143,83|144,18|144,03|144,19|0,00178|0,52|0,35|1,45|0,31|
|D3|bajo junta|398,88|4,4393|Pexc 95%|0,17|143,76|144,16|143,94|144,17|0,00083|0,41|0,46|1,58|0,22|
|D3|bajo junta|420,1|4,2523|Pexc 95%|0,17|143,69|144,15|143,86|144,15|0,00041|0,32|0,59|1,80|0,16|
|D3|bajo junta|440,31|4,0654|Pexc 95%|0,17|143,62|144,15|143,78|144,15|0,00022|0,27|0,73|1,84|0,12|
|D3|bajo junta|445,94|4|Pexc 95%|0,17|143,59|144,14|143,75|144,15|0,00019|0,25|0,77|1,81|0,11|
|D3|bajo junta|452,26|3|Pexc 95%|0,17|143,95|144,12|144,09|144,14|0,01163|0,71|0,25|2,47|0,68|
|D3|bajo junta|471,1|2|Pexc 95%|0,17|143,64|144,10|143,87|144,10|0,00070|0,34|0,55|2,04|0,19|
|D3|bajo junta|491,09|1,6942|Pexc 95%|0,17|143,66|144,08|143,87|144,09|0,00075|0,38|0,53|2,10|0,20|
|D3|bajo junta|511,09|1,3884|Pexc 95%|0,17|143,68|144,06|143,88|144,07|0,00114|0,43|0,44|2,24|0,25|
|D3|bajo junta|531,1|1,0826|Pexc 95%|0,17|143,70|144,02|143,92|144,03|0,00282|0,54|0,33|1,71|0,37|
|D3|bajo junta|536,51|1|Pexc 95%|0,17|143,71|143,99|143,93|144,01|0,00600|0,66|0,27|1,70|0,52|

B.2 Eje hidráulico Con Proyecto - Probabilidad de excedencia 80%

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|Pexc 80%|0,12|144,50|144,86|144,67|144,87|0,00064|0,33|0,44|2,01|0,19|
|D2|arriba junta|61,4|11|Pexc 80%|0,12|144,63|144,83|0,00|144,85|0,00080|0,61|0,22|1,41|0,43|
|D2|arriba junta|81,4|10,722|Pexc 80%|0,12|144,61|144,82|0,00|144,83|0,00073|0,59|0,23|1,42|0,41|
|D2|arriba junta|101,4|10,444|Pexc 80%|0,12|144,59|144,81|0,00|144,82|0,00064|0,57|0,24|1,45|0,39|
|D2|arriba junta|121,4|10,167|Pexc 80%|0,12|144,57|144,80|0,00|144,81|0,00055|0,54|0,26|1,47|0,36|
|D2|arriba junta|133,4|10|Pexc 80%|0,12|144,56|144,79|0,00|144,80|0,00050|0,53|0,26|1,49|0,35|
|D2|arriba junta|153,4|9,8601|Pexc 80%|0,12|144,54|144,78|0,00|144,79|0,00041|0,49|0,28|1,53|0,32|
|D2|arriba junta|173,4|9,7203|Pexc 80%|0,12|144,52|144,78|0,00|144,78|0,00034|0,46|0,30|1,57|0,29|
|D2|arriba junta|193,4|9,5804|Pexc 80%|0,12|144,50|144,77|0,00|144,78|0,00027|0,43|0,33|1,61|0,26|
|D2|arriba junta|213,4|9,4406|Pexc 80%|0,12|144,48|144,77|0,00|144,77|0,00022|0,40|0,35|1,66|0,24|
|D2|arriba junta|233,4|9,3007|Pexc 80%|0,12|144,46|144,76|0,00|144,77|0,00018|0,38|0,38|1,71|0,22|
|D2|arriba junta|253,4|9,1608|Pexc 80%|0,12|144,44|144,76|0,00|144,77|0,00014|0,35|0,41|1,76|0,20|
|D2|arriba junta|273,4|9,021|Pexc 80%|0,12|144,42|144,76|0,00|144,76|0,00012|0,33|0,44|1,82|0,18|
|D2|arriba junta|276,4|9|Pexc 80%|0,12|144,42|144,76|0,00|144,76|0,00011|0,32|0,45|1,82|0,18|
|D2|arriba junta|296,4|8,8519|Pexc 80%|0,12|144,40|144,76|0,00|144,76|0,00009|0,30|0,48|1,88|0,16|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.3 de B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|316,4|8,7037|Pexc 80%|0,12|144,38|144,75|0,00|144,76|0,00008|0,28|0,52|1,94|0,15|
|D2|arriba junta|336,4|8,5556|Pexc 80%|0,12|144,36|144,75|0,00|144,76|0,00006|0,27|0,56|1,99|0,13|
|D2|arriba junta|356,4|8,4074|Pexc 80%|0,12|144,34|144,75|0,00|144,76|0,00005|0,25|0,60|2,05|0,12|
|D2|arriba junta|376,4|8,2593|Pexc 80%|0,12|144,31|144,75|0,00|144,75|0,00004|0,24|0,64|2,11|0,11|
|D2|arriba junta|396,4|8,1111|Pexc 80%|0,12|144,30|144,75|0,00|144,75|0,00004|0,22|0,68|2,17|0,11|
|D2|arriba junta|411,4|8|Pexc 80%|0,12|144,28|144,75|144,40|144,75|0,00003|0,21|0,71|2,21|0,10|
|D3|arriba junta|0|9|Pexc 80%|0,07|144,95|145,08|145,04|145,09|0,00497|0,45|0,19|2,70|0,44|
|D3|arriba junta|19,85|8,7368|Pexc 80%|0,07|144,81|144,96|144,92|144,98|0,00636|0,58|0,13|1,17|0,52|
|D3|arriba junta|39,67|8,4737|Pexc 80%|0,07|144,68|144,85|144,79|144,87|0,00465|0,58|0,13|0,92|0,46|
|D3|arriba junta|59,49|8,2105|Pexc 80%|0,07|144,54|144,80|144,67|144,81|0,00170|0,47|0,17|0,80|0,30|
|D3|arriba junta|75,33|8|Pexc 80%|0,07|144,43|144,78|144,58|144,79|0,00100|0,44|0,19|0,71|0,24|
|D3|arriba junta|95,39|7,759|Pexc 80%|0,07|144,39|144,77|0,00|144,77|0,00069|0,39|0,22|0,80|0,20|
|D3|arriba junta|115,46|7,5181|Pexc 80%|0,07|144,36|144,76|0,00|144,76|0,00044|0,32|0,28|1,14|0,16|
|D3|arriba junta|135,52|7,2771|Pexc 80%|0,07|144,32|144,75|0,00|144,76|0,00023|0,25|0,39|1,59|0,12|
|D3|arriba junta|155,6|7,0361|Pexc 80%|0,07|144,29|144,75|0,00|144,75|0,00012|0,18|0,53|1,95|0,09|
|D3|arriba junta|158,61|7|Pexc 80%|0,07|144,28|144,75|144,40|144,75|0,00011|0,18|0,55|2,03|0,08|
|D3|bajo junta|178,67|6,9|Pexc 80%|0,19|144,28|144,74|0,00|144,75|0,00082|0,49|0,53|1,98|0,23|
|D3|bajo junta|198,72|6,42|Pexc 80%|0,19|144,22|144,69|0,00|144,71|0,00149|0,57|0,40|1,56|0,29|
|D3|bajo junta|218,77|6,18|Pexc 80%|0,19|144,19|144,66|0,00|144,67|0,00199|0,60|0,35|1,23|0,32|
|D3|bajo junta|237,8|6|Pexc 80%|0,19|144,17|144,62|144,47|144,64|0,00274|0,64|0,32|1,18|0,36|
|D3|bajo junta|257,8|5,802|Pexc 80%|0,19|144,13|144,56|144,42|144,58|0,00271|0,64|0,32|1,22|0,36|
|D3|bajo junta|277,79|5,604|Pexc 80%|0,19|144,10|144,51|144,37|144,53|0,00274|0,64|0,32|1,25|0,37|
|D3|bajo junta|297,78|5,4059|Pexc 80%|0,19|144,06|144,45|144,32|144,47|0,00280|0,64|0,32|1,29|0,37|
|D3|bajo junta|317,75|5,2079|Pexc 80%|0,19|144,02|144,40|144,27|144,42|0,00307|0,65|0,31|1,32|0,39|
|D3|bajo junta|337,72|5,0099|Pexc 80%|0,19|143,98|144,32|144,22|144,34|0,00439|0,72|0,28|1,32|0,46|
|D3|bajo junta|338,72|5|Pexc 80%|0,19|143,98|144,31|144,22|144,34|0,00451|0,73|0,28|1,32|0,47|
|D3|bajo junta|358,41|4,8131|Pexc 80%|0,19|143,91|144,24|144,13|144,26|0,00332|0,66|0,31|1,38|0,41|
|D3|bajo junta|378,39|4,6262|Pexc 80%|0,19|143,83|144,20|144,03|144,21|0,00182|0,54|0,38|1,48|0,31|
|D3|bajo junta|398,88|4,4393|Pexc 80%|0,19|143,76|144,18|143,95|144,18|0,00089|0,43|0,49|1,61|0,23|
|D3|bajo junta|420,1|4,2523|Pexc 80%|0,19|143,69|144,17|143,87|144,17|0,00045|0,35|0,62|1,84|0,17|
|D3|bajo junta|440,31|4,0654|Pexc 80%|0,19|143,62|144,16|143,79|144,16|0,00025|0,29|0,76|1,86|0,13|
|D3|bajo junta|445,94|4|Pexc 80%|0,19|143,59|144,16|143,77|144,16|0,00021|0,27|0,80|1,83|0,12|
|D3|bajo junta|452,26|3|Pexc 80%|0,19|143,95|144,13|144,10|144,16|0,00880|0,68|0,29|2,57|0,61|
|D3|bajo junta|471,1|2|Pexc 80%|0,19|143,64|144,11|143,88|144,12|0,00074|0,36|0,58|2,08|0,20|
|D3|bajo junta|491,09|1,6942|Pexc 80%|0,19|143,66|144,10|143,88|144,10|0,00079|0,40|0,56|2,15|0,21|
|D3|bajo junta|511,09|1,3884|Pexc 80%|0,19|143,68|144,07|143,89|144,08|0,00119|0,46|0,48|2,26|0,26|
|D3|bajo junta|531,1|1,0826|Pexc 80%|0,19|143,70|144,03|143,92|144,05|0,00292|0,57|0,35|1,73|0,38|
|D3|bajo junta|536,51|1|Pexc 80%|0,19|143,71|144,00|143,94|144,02|0,00600|0,69|0,29|1,71|0,52|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.4 de B.18|

B.3 Eje hidráulico Con Proyecto - Probabilidad de excedencia 60%

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|Pexc 60%|0,14|144,50|144,89|144,68|144,89|0,00066|0,35|0,49|2,10|0,19|
|D2|arriba junta|61,4|11|Pexc 60%|0,14|144,63|144,86|0,00|144,87|0,00073|0,63|0,26|1,48|0,42|
|D2|arriba junta|81,4|10,722|Pexc 60%|0,14|144,61|144,84|0,00|144,86|0,00066|0,61|0,27|1,50|0,40|
|D2|arriba junta|101,4|10,444|Pexc 60%|0,14|144,59|144,83|0,00|144,85|0,00057|0,58|0,28|1,52|0,38|
|D2|arriba junta|121,4|10,167|Pexc 60%|0,14|144,57|144,82|0,00|144,84|0,00049|0,55|0,30|1,56|0,35|
|D2|arriba junta|133,4|10|Pexc 60%|0,14|144,56|144,82|0,00|144,83|0,00045|0,53|0,31|1,57|0,34|
|D2|arriba junta|153,4|9,8601|Pexc 60%|0,14|144,54|144,81|0,00|144,82|0,00037|0,50|0,33|1,61|0,31|
|D2|arriba junta|173,4|9,7203|Pexc 60%|0,14|144,52|144,81|0,00|144,81|0,00030|0,47|0,35|1,66|0,28|
|D2|arriba junta|193,4|9,5804|Pexc 60%|0,14|144,50|144,80|0,00|144,81|0,00025|0,44|0,38|1,70|0,26|
|D2|arriba junta|213,4|9,4406|Pexc 60%|0,14|144,48|144,80|0,00|144,80|0,00020|0,41|0,41|1,75|0,23|
|D2|arriba junta|233,4|9,3007|Pexc 60%|0,14|144,46|144,79|0,00|144,80|0,00017|0,39|0,44|1,80|0,21|
|D2|arriba junta|253,4|9,1608|Pexc 60%|0,14|144,44|144,79|0,00|144,80|0,00014|0,36|0,47|1,86|0,20|
|D2|arriba junta|273,4|9,021|Pexc 60%|0,14|144,42|144,79|0,00|144,79|0,00011|0,34|0,50|1,91|0,18|
|D2|arriba junta|276,4|9|Pexc 60%|0,14|144,42|144,79|0,00|144,79|0,00011|0,34|0,51|1,92|0,18|
|D2|arriba junta|296,4|8,8519|Pexc 60%|0,14|144,40|144,79|0,00|144,79|0,00009|0,32|0,54|1,97|0,16|
|D2|arriba junta|316,4|8,7037|Pexc 60%|0,14|144,38|144,79|0,00|144,79|0,00008|0,30|0,58|2,03|0,15|
|D2|arriba junta|336,4|8,5556|Pexc 60%|0,14|144,36|144,79|0,00|144,79|0,00006|0,28|0,62|2,09|0,14|
|D2|arriba junta|356,4|8,4074|Pexc 60%|0,14|144,34|144,78|0,00|144,79|0,00005|0,27|0,66|2,15|0,13|
|D2|arriba junta|376,4|8,2593|Pexc 60%|0,14|144,31|144,78|0,00|144,79|0,00004|0,25|0,70|2,21|0,12|
|D2|arriba junta|396,4|8,1111|Pexc 60%|0,14|144,30|144,78|0,00|144,79|0,00004|0,24|0,75|2,26|0,11|
|D2|arriba junta|411,4|8|Pexc 60%|0,14|144,28|144,78|144,42|144,78|0,00003|0,23|0,78|2,31|0,10|
|D3|arriba junta|0|9|Pexc 60%|0,09|144,95|145,10|145,06|145,10|0,00445|0,47|0,24|2,99|0,43|
|D3|arriba junta|19,85|8,7368|Pexc 60%|0,09|144,81|144,98|144,93|145,00|0,00614|0,63|0,15|1,22|0,52|
|D3|arriba junta|39,67|8,4737|Pexc 60%|0,09|144,68|144,89|144,81|144,90|0,00379|0,60|0,16|0,97|0,43|
|D3|arriba junta|59,49|8,2105|Pexc 60%|0,09|144,54|144,84|144,69|144,85|0,00169|0,52|0,20|0,84|0,31|
|D3|arriba junta|75,33|8|Pexc 60%|0,09|144,43|144,82|144,61|144,83|0,00114|0,51|0,22|0,74|0,26|
|D3|arriba junta|95,39|7,759|Pexc 60%|0,09|144,39|144,80|0,00|144,81|0,00083|0,45|0,25|0,90|0,23|
|D3|arriba junta|115,46|7,5181|Pexc 60%|0,09|144,36|144,79|0,00|144,80|0,00054|0,38|0,32|1,37|0,18|
|D3|arriba junta|135,52|7,2771|Pexc 60%|0,09|144,32|144,79|0,00|144,79|0,00027|0,28|0,45|1,71|0,13|
|D3|arriba junta|155,6|7,0361|Pexc 60%|0,09|144,29|144,78|0,00|144,79|0,00015|0,22|0,59|2,26|0,10|
|D3|arriba junta|158,61|7|Pexc 60%|0,09|144,28|144,78|144,42|144,78|0,00014|0,21|0,62|2,35|0,09|
|D3|bajo junta|178,67|6,9|Pexc 60%|0,22|144,28|144,78|0,00|144,78|0,00086|0,52|0,60|2,27|0,24|
|D3|bajo junta|198,72|6,42|Pexc 60%|0,22|144,22|144,72|0,00|144,74|0,00151|0,60|0,45|1,68|0,29|
|D3|bajo junta|218,77|6,18|Pexc 60%|0,22|144,19|144,68|0,00|144,70|0,00205|0,64|0,38|1,27|0,33|
|D3|bajo junta|237,8|6|Pexc 60%|0,22|144,17|144,65|144,48|144,67|0,00277|0,68|0,35|1,22|0,37|
|D3|bajo junta|257,8|5,802|Pexc 60%|0,22|144,13|144,59|144,43|144,61|0,00274|0,67|0,35|1,25|0,37|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.5 de B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|bajo junta|277,79|5,604|Pexc 60%|0,22|144,10|144,54|144,38|144,56|0,00279|0,68|0,35|1,29|0,38|
|D3|bajo junta|297,78|5,4059|Pexc 60%|0,22|144,06|144,48|144,33|144,50|0,00285|0,68|0,35|1,33|0,38|
|D3|bajo junta|317,75|5,2079|Pexc 60%|0,22|144,02|144,42|144,29|144,44|0,00313|0,69|0,34|1,36|0,40|
|D3|bajo junta|337,72|5,0099|Pexc 60%|0,22|143,98|144,34|144,24|144,37|0,00437|0,76|0,31|1,36|0,47|
|D3|bajo junta|338,72|5|Pexc 60%|0,22|143,98|144,34|144,24|144,36|0,00447|0,77|0,31|1,36|0,47|
|D3|bajo junta|358,41|4,8131|Pexc 60%|0,22|143,91|144,26|144,14|144,29|0,00326|0,69|0,34|1,42|0,41|
|D3|bajo junta|378,39|4,6262|Pexc 60%|0,22|143,83|144,22|144,05|144,24|0,00185|0,58|0,42|1,52|0,32|
|D3|bajo junta|398,88|4,4393|Pexc 60%|0,22|143,76|144,20|143,96|144,21|0,00096|0,47|0,53|1,69|0,24|
|D3|bajo junta|420,1|4,2523|Pexc 60%|0,22|143,69|144,19|143,88|144,19|0,00050|0,38|0,66|1,89|0,18|
|D3|bajo junta|440,31|4,0654|Pexc 60%|0,22|143,62|144,18|143,80|144,19|0,00029|0,32|0,80|1,89|0,14|
|D3|bajo junta|445,94|4|Pexc 60%|0,22|143,59|144,18|143,78|144,18|0,00025|0,30|0,84|1,86|0,13|
|D3|bajo junta|452,26|3|Pexc 60%|0,22|143,95|144,16|144,11|144,18|0,00652|0,66|0,36|2,70|0,54|
|D3|bajo junta|471,1|2|Pexc 60%|0,22|143,64|144,13|143,90|144,14|0,00079|0,39|0,63|2,14|0,21|
|D3|bajo junta|491,09|1,6942|Pexc 60%|0,22|143,66|144,12|143,90|144,13|0,00084|0,43|0,61|2,22|0,22|
|D3|bajo junta|511,09|1,3884|Pexc 60%|0,22|143,68|144,09|143,90|144,10|0,00125|0,49|0,52|2,29|0,27|
|D3|bajo junta|531,1|1,0826|Pexc 60%|0,22|143,70|144,05|143,94|144,07|0,00304|0,61|0,38|1,76|0,39|
|D3|bajo junta|536,51|1|Pexc 60%|0,22|143,71|144,02|143,95|144,04|0,00600|0,73|0,32|1,74|0,53|

B.4 Eje hidráulico Con Proyecto - T=2 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=2|0,15|144,50|144,90|144,68|144,91|0,00064|0,36|0,52|2,16|0,19|
|D2|arriba junta|61,4|11|T=2|0,15|144,63|144,87|0,00|144,89|0,00064|0,62|0,28|1,53|0,40|
|D2|arriba junta|81,4|10,722|T=2|0,15|144,61|144,86|0,00|144,88|0,00056|0,59|0,30|1,55|0,38|
|D2|arriba junta|101,4|10,444|T=2|0,15|144,59|144,85|0,00|144,87|0,00048|0,56|0,31|1,59|0,35|
|D2|arriba junta|121,4|10,167|T=2|0,15|144,57|144,85|0,00|144,86|0,00041|0,53|0,33|1,62|0,32|
|D2|arriba junta|133,4|10|T=2|0,15|144,56|144,84|0,00|144,85|0,00037|0,51|0,34|1,64|0,31|
|D2|arriba junta|153,4|9,8601|T=2|0,15|144,54|144,84|0,00|144,85|0,00030|0,48|0,37|1,69|0,28|
|D2|arriba junta|173,4|9,7203|T=2|0,15|144,52|144,83|0,00|144,84|0,00025|0,45|0,40|1,74|0,26|
|D2|arriba junta|193,4|9,5804|T=2|0,15|144,50|144,83|0,00|144,83|0,00021|0,43|0,42|1,78|0,24|
|D2|arriba junta|213,4|9,4406|T=2|0,15|144,48|144,82|0,00|144,83|0,00017|0,40|0,46|1,84|0,22|
|D2|arriba junta|233,4|9,3007|T=2|0,15|144,46|144,82|0,00|144,83|0,00014|0,38|0,49|1,89|0,20|
|D2|arriba junta|253,4|9,1608|T=2|0,15|144,44|144,82|0,00|144,82|0,00012|0,35|0,52|1,94|0,18|
|D2|arriba junta|273,4|9,021|T=2|0,15|144,42|144,82|0,00|144,82|0,00010|0,33|0,56|2,00|0,17|
|D2|arriba junta|276,4|9|T=2|0,15|144,42|144,82|0,00|144,82|0,00009|0,33|0,56|2,00|0,17|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.6 de B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|296,4|8,8519|T=2|0,15|144,40|144,82|0,00|144,82|0,00008|0,31|0,60|2,06|0,15|
|D2|arriba junta|316,4|8,7037|T=2|0,15|144,38|144,82|0,00|144,82|0,00007|0,29|0,64|2,12|0,14|
|D2|arriba junta|336,4|8,5556|T=2|0,15|144,36|144,81|0,00|144,82|0,00006|0,28|0,68|2,18|0,13|
|D2|arriba junta|356,4|8,4074|T=2|0,15|144,34|144,81|0,00|144,82|0,00005|0,26|0,73|2,23|0,12|
|D2|arriba junta|376,4|8,2593|T=2|0,15|144,31|144,81|0,00|144,82|0,00004|0,25|0,77|2,29|0,11|
|D2|arriba junta|396,4|8,1111|T=2|0,15|144,30|144,81|0,00|144,81|0,00003|0,24|0,82|2,35|0,10|
|D2|arriba junta|411,4|8|T=2|0,15|144,28|144,81|144,42|144,81|0,00003|0,23|0,85|2,40|0,10|
|D3|arriba junta|0|9|T=2|0,10|144,95|145,10|145,06|145,11|0,00439|0,48|0,26|3,10|0,43|
|D3|arriba junta|19,85|8,7368|T=2|0,10|144,81|144,99|144,94|145,01|0,00587|0,65|0,17|1,25|0,51|
|D3|arriba junta|39,67|8,4737|T=2|0,10|144,68|144,91|144,81|144,93|0,00328|0,60|0,19|1,01|0,41|
|D3|arriba junta|59,49|8,2105|T=2|0,10|144,54|144,87|144,70|144,88|0,00154|0,52|0,22|0,86|0,30|
|D3|arriba junta|75,33|8|T=2|0,10|144,43|144,85|144,62|144,86|0,00110|0,52|0,24|0,76|0,26|
|D3|arriba junta|95,39|7,759|T=2|0,10|144,39|144,83|0,00|144,84|0,00079|0,46|0,28|1,00|0,22|
|D3|arriba junta|115,46|7,5181|T=2|0,10|144,36|144,82|0,00|144,83|0,00050|0,38|0,37|1,57|0,18|
|D3|arriba junta|135,52|7,2771|T=2|0,10|144,32|144,82|0,00|144,82|0,00027|0,29|0,50|2,01|0,13|
|D3|arriba junta|155,6|7,0361|T=2|0,10|144,29|144,81|0,00|144,81|0,00014|0,22|0,66|2,56|0,10|
|D3|arriba junta|158,61|7|T=2|0,10|144,28|144,81|144,43|144,81|0,00013|0,21|0,69|2,65|0,09|
|D3|bajo junta|178,67|6,9|T=2|0,25|144,28|144,80|0,00|144,81|0,00088|0,55|0,67|2,56|0,24|
|D3|bajo junta|198,72|6,42|T=2|0,25|144,22|144,75|0,00|144,77|0,00152|0,63|0,50|1,84|0,30|
|D3|bajo junta|218,77|6,18|T=2|0,25|144,19|144,71|0,00|144,73|0,00212|0,68|0,42|1,45|0,34|
|D3|bajo junta|237,8|6|T=2|0,25|144,17|144,67|144,50|144,69|0,00280|0,71|0,38|1,25|0,37|
|D3|bajo junta|257,8|5,802|T=2|0,25|144,13|144,61|144,45|144,64|0,00278|0,71|0,38|1,29|0,38|
|D3|bajo junta|277,79|5,604|T=2|0,25|144,10|144,56|144,40|144,58|0,00282|0,71|0,38|1,33|0,38|
|D3|bajo junta|297,78|5,4059|T=2|0,25|144,06|144,50|144,35|144,53|0,00289|0,72|0,38|1,37|0,39|
|D3|bajo junta|317,75|5,2079|T=2|0,25|144,02|144,44|144,30|144,47|0,00317|0,73|0,37|1,40|0,41|
|D3|bajo junta|337,72|5,0099|T=2|0,25|143,98|144,36|144,25|144,39|0,00433|0,80|0,34|1,40|0,47|
|D3|bajo junta|338,72|5|T=2|0,25|143,98|144,36|144,25|144,39|0,00441|0,80|0,34|1,40|0,48|
|D3|bajo junta|358,41|4,8131|T=2|0,25|143,91|144,29|144,16|144,31|0,00321|0,72|0,38|1,46|0,41|
|D3|bajo junta|378,39|4,6262|T=2|0,25|143,83|144,24|144,07|144,26|0,00189|0,61|0,45|1,56|0,33|
|D3|bajo junta|398,88|4,4393|T=2|0,25|143,76|144,22|143,98|144,23|0,00102|0,50|0,56|1,77|0,25|
|D3|bajo junta|420,1|4,2523|T=2|0,25|143,69|144,21|143,90|144,22|0,00055|0,41|0,71|1,94|0,19|
|D3|bajo junta|440,31|4,0654|T=2|0,25|143,62|144,20|143,82|144,21|0,00033|0,35|0,84|1,93|0,15|
|D3|bajo junta|445,94|4|T=2|0,25|143,59|144,20|143,79|144,21|0,00028|0,33|0,87|1,89|0,14|
|D3|bajo junta|452,26|3|T=2|0,25|143,95|144,18|144,12|144,20|0,00526|0,65|0,42|2,82|0,49|
|D3|bajo junta|471,1|2|T=2|0,25|143,64|144,16|143,91|144,16|0,00084|0,42|0,68|2,19|0,22|
|D3|bajo junta|491,09|1,6942|T=2|0,25|143,66|144,14|143,92|144,15|0,00089|0,46|0,65|2,29|0,23|
|D3|bajo junta|511,09|1,3884|T=2|0,25|143,68|144,11|143,92|144,12|0,00130|0,52|0,57|2,32|0,27|
|D3|bajo junta|531,1|1,0826|T=2|0,25|143,70|144,06|143,95|144,09|0,00315|0,64|0,41|1,78|0,40|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.7 de B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|bajo junta|536,51|1|T=2|0,25|143,71|144,03|143,96|144,06|0,00600|0,77|0,34|1,76|0,54|

B.5 Eje hidráulico Con Proyecto - T=5 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=5|0,20|144,50|144,95|144,71|144,96|0,00063|0,39|0,64|2,39|0,20|
|D2|arriba junta|61,4|11|T=5|0,20|144,63|144,93|0,00|144,95|0,00052|0,64|0,37|1,70|0,37|
|D2|arriba junta|81,4|10,722|T=5|0,20|144,61|144,92|0,00|144,94|0,00045|0,61|0,39|1,73|0,35|
|D2|arriba junta|101,4|10,444|T=5|0,20|144,59|144,91|0,00|144,93|0,00039|0,58|0,42|1,77|0,32|
|D2|arriba junta|121,4|10,167|T=5|0,20|144,57|144,91|0,00|144,92|0,00033|0,55|0,44|1,81|0,30|
|D2|arriba junta|133,4|10|T=5|0,20|144,56|144,91|0,00|144,92|0,00030|0,53|0,46|1,84|0,29|
|D2|arriba junta|153,4|9,8601|T=5|0,20|144,54|144,90|0,00|144,91|0,00025|0,50|0,49|1,88|0,27|
|D2|arriba junta|173,4|9,7203|T=5|0,20|144,52|144,90|0,00|144,91|0,00021|0,47|0,52|1,93|0,25|
|D2|arriba junta|193,4|9,5804|T=5|0,20|144,50|144,89|0,00|144,90|0,00018|0,45|0,55|1,98|0,23|
|D2|arriba junta|213,4|9,4406|T=5|0,20|144,48|144,89|0,00|144,90|0,00015|0,42|0,58|2,04|0,21|
|D2|arriba junta|233,4|9,3007|T=5|0,20|144,46|144,89|0,00|144,90|0,00013|0,40|0,62|2,09|0,20|
|D2|arriba junta|253,4|9,1608|T=5|0,20|144,44|144,89|0,00|144,89|0,00011|0,38|0,66|2,14|0,18|
|D2|arriba junta|273,4|9,021|T=5|0,20|144,42|144,89|0,00|144,89|0,00009|0,36|0,70|2,20|0,17|
|D2|arriba junta|276,4|9|T=5|0,20|144,42|144,89|0,00|144,89|0,00009|0,36|0,71|2,21|0,17|
|D2|arriba junta|296,4|8,8519|T=5|0,20|144,40|144,88|0,00|144,89|0,00008|0,34|0,75|2,26|0,16|
|D2|arriba junta|316,4|8,7037|T=5|0,20|144,38|144,88|0,00|144,89|0,00007|0,32|0,79|2,32|0,14|
|D2|arriba junta|336,4|8,5556|T=5|0,20|144,36|144,88|0,00|144,89|0,00006|0,31|0,84|2,38|0,14|
|D2|arriba junta|356,4|8,4074|T=5|0,20|144,34|144,88|0,00|144,88|0,00005|0,29|0,88|2,44|0,13|
|D2|arriba junta|376,4|8,2593|T=5|0,20|144,31|144,88|0,00|144,88|0,00004|0,28|0,93|2,50|0,12|
|D2|arriba junta|396,4|8,1111|T=5|0,20|144,30|144,88|0,00|144,88|0,00004|0,27|0,98|2,55|0,11|
|D2|arriba junta|411,4|8|T=5|0,20|144,28|144,88|144,45|144,88|0,00003|0,26|1,02|2,60|0,11|
|D3|arriba junta|0|9|T=5|0,13|144,95|145,13|145,07|145,14|0,00358|0,49|0,34|3,52|0,40|
|D3|arriba junta|19,85|8,7368|T=5|0,13|144,81|145,03|144,96|145,05|0,00490|0,68|0,23|2,26|0,49|
|D3|arriba junta|39,67|8,4737|T=5|0,13|144,68|144,97|144,84|144,98|0,00245|0,60|0,24|1,09|0,36|
|D3|arriba junta|59,49|8,2105|T=5|0,13|144,54|144,93|144,73|144,95|0,00135|0,55|0,28|0,93|0,29|
|D3|arriba junta|75,33|8|T=5|0,13|144,43|144,91|144,65|144,93|0,00110|0,57|0,29|0,82|0,27|
|D3|arriba junta|95,39|7,759|T=5|0,13|144,39|144,90|0,00|144,91|0,00076|0,49|0,36|1,67|0,22|
|D3|arriba junta|115,46|7,5181|T=5|0,13|144,36|144,89|0,00|144,89|0,00046|0,40|0,50|2,29|0,18|
|D3|arriba junta|135,52|7,2771|T=5|0,13|144,32|144,88|0,00|144,89|0,00025|0,31|0,66|2,73|0,13|
|D3|arriba junta|155,6|7,0361|T=5|0,13|144,29|144,88|0,00|144,88|0,00014|0,24|0,86|3,24|0,10|
|D3|arriba junta|158,61|7|T=5|0,13|144,28|144,88|144,45|144,88|0,00013|0,23|0,89|3,32|0,09|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.8 de B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|bajo junta|178,67|6,9|T=5|0,33|144,28|144,87|0,00|144,88|0,00088|0,59|0,86|3,23|0,25|
|D3|bajo junta|198,72|6,42|T=5|0,33|144,22|144,81|0,00|144,83|0,00154|0,69|0,63|2,40|0,30|
|D3|bajo junta|218,77|6,18|T=5|0,33|144,19|144,77|0,00|144,80|0,00218|0,76|0,52|1,87|0,35|
|D3|bajo junta|237,8|6|T=5|0,33|144,17|144,73|144,54|144,76|0,00287|0,80|0,46|1,34|0,39|
|D3|bajo junta|257,8|5,802|T=5|0,33|144,13|144,67|144,49|144,70|0,00286|0,80|0,46|1,38|0,39|
|D3|bajo junta|277,79|5,604|T=5|0,33|144,10|144,61|144,44|144,64|0,00291|0,80|0,46|1,42|0,40|
|D3|bajo junta|297,78|5,4059|T=5|0,33|144,06|144,56|144,39|144,59|0,00298|0,80|0,46|1,46|0,41|
|D3|bajo junta|317,75|5,2079|T=5|0,33|144,02|144,49|144,34|144,52|0,00325|0,82|0,45|1,49|0,42|
|D3|bajo junta|337,72|5,0099|T=5|0,33|143,98|144,41|144,29|144,45|0,00418|0,87|0,42|1,50|0,48|
|D3|bajo junta|338,72|5|T=5|0,33|143,98|144,41|144,29|144,45|0,00424|0,88|0,41|1,50|0,48|
|D3|bajo junta|358,41|4,8131|T=5|0,33|143,91|144,34|144,19|144,37|0,00313|0,80|0,46|1,56|0,42|
|D3|bajo junta|378,39|4,6262|T=5|0,33|143,83|144,30|144,10|144,32|0,00197|0,69|0,54|1,65|0,34|
|D3|bajo junta|398,88|4,4393|T=5|0,33|143,76|144,27|144,01|144,29|0,00114|0,57|0,66|1,96|0,27|
|D3|bajo junta|420,1|4,2523|T=5|0,33|143,69|144,26|143,93|144,27|0,00066|0,48|0,81|2,07|0,21|
|D3|bajo junta|440,31|4,0654|T=5|0,33|143,62|144,25|143,85|144,26|0,00042|0,41|0,93|2,00|0,17|
|D3|bajo junta|445,94|4|T=5|0,33|143,59|144,25|143,82|144,26|0,00037|0,40|0,97|1,95|0,16|
|D3|bajo junta|452,26|3|T=5|0,33|143,95|144,23|144,14|144,25|0,00361|0,64|0,57|3,10|0,43|
|D3|bajo junta|471,1|2|T=5|0,33|143,64|144,21|143,94|144,22|0,00095|0,49|0,79|2,31|0,23|
|D3|bajo junta|491,09|1,6942|T=5|0,33|143,66|144,19|143,95|144,20|0,00100|0,53|0,77|2,46|0,25|
|D3|bajo junta|511,09|1,3884|T=5|0,33|143,68|144,16|143,95|144,17|0,00141|0,58|0,67|2,47|0,29|
|D3|bajo junta|531,1|1,0826|T=5|0,33|143,70|144,10|143,98|144,13|0,00338|0,73|0,48|1,85|0,43|
|D3|bajo junta|536,51|1|T=5|0,33|143,71|144,07|143,99|144,11|0,00600|0,86|0,41|1,82|0,55|

B.6 Eje hidráulico Con Proyecto - T=10 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=10|0,24|144,50|145,00|144,73|145,00|0,00061|0,41|0,75|2,58|0,20|
|D2|arriba junta|61,4|11|T=10|0,24|144,63|144,97|0,00|144,99|0,00044|0,64|0,45|1,83|0,35|
|D2|arriba junta|81,4|10,722|T=10|0,24|144,61|144,97|0,00|144,98|0,00039|0,62|0,47|1,87|0,33|
|D2|arriba junta|101,4|10,444|T=10|0,24|144,59|144,96|0,00|144,97|0,00033|0,59|0,50|1,91|0,31|
|D2|arriba junta|121,4|10,167|T=10|0,24|144,57|144,96|0,00|144,97|0,00028|0,56|0,53|1,95|0,29|
|D2|arriba junta|133,4|10|T=10|0,24|144,56|144,95|0,00|144,96|0,00026|0,54|0,55|1,98|0,28|
|D2|arriba junta|153,4|9,8601|T=10|0,24|144,54|144,95|0,00|144,96|0,00022|0,51|0,58|2,03|0,26|
|D2|arriba junta|173,4|9,7203|T=10|0,24|144,52|144,95|0,00|144,95|0,00019|0,49|0,61|2,08|0,24|
|D2|arriba junta|193,4|9,5804|T=10|0,24|144,50|144,94|0,00|144,95|0,00016|0,46|0,65|2,13|0,22|
|D2|arriba junta|213,4|9,4406|T=10|0,24|144,48|144,94|0,00|144,95|0,00014|0,44|0,69|2,18|0,21|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.9 de B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|233,4|9,3007|T=10|0,24|144,46|144,94|0,00|144,95|0,00012|0,42|0,73|2,24|0,19|
|D2|arriba junta|253,4|9,1608|T=10|0,24|144,44|144,94|0,00|144,94|0,00010|0,40|0,77|2,29|0,18|
|D2|arriba junta|273,4|9,021|T=10|0,24|144,42|144,94|0,00|144,94|0,00009|0,38|0,81|2,35|0,17|
|D2|arriba junta|276,4|9|T=10|0,24|144,42|144,93|0,00|144,94|0,00009|0,38|0,82|2,36|0,17|
|D2|arriba junta|296,4|8,8519|T=10|0,24|144,40|144,93|0,00|144,94|0,00008|0,36|0,86|2,41|0,16|
|D2|arriba junta|316,4|8,7037|T=10|0,24|144,38|144,93|0,00|144,94|0,00007|0,34|0,91|2,47|0,15|
|D2|arriba junta|336,4|8,5556|T=10|0,24|144,36|144,93|0,00|144,94|0,00006|0,33|0,96|2,53|0,14|
|D2|arriba junta|356,4|8,4074|T=10|0,24|144,34|144,93|0,00|144,93|0,00005|0,31|1,01|2,59|0,13|
|D2|arriba junta|376,4|8,2593|T=10|0,24|144,31|144,93|0,00|144,93|0,00004|0,30|1,06|2,65|0,12|
|D2|arriba junta|396,4|8,1111|T=10|0,24|144,30|144,93|0,00|144,93|0,00004|0,28|1,11|2,70|0,11|
|D2|arriba junta|411,4|8|T=10|0,24|144,28|144,93|144,47|144,93|0,00004|0,28|1,15|2,75|0,11|
|D3|arriba junta|0|9|T=10|0,15|144,95|145,14|145,08|145,15|0,00348|0,50|0,38|3,61|0,40|
|D3|arriba junta|19,85|8,7368|T=10|0,15|144,81|145,06|144,97|145,07|0,00370|0,64|0,30|2,57|0,43|
|D3|arriba junta|39,67|8,4737|T=10|0,15|144,68|145,01|144,85|145,02|0,00198|0,59|0,30|1,89|0,33|
|D3|arriba junta|59,49|8,2105|T=10|0,15|144,54|144,98|144,74|144,99|0,00120|0,56|0,33|1,44|0,27|
|D3|arriba junta|75,33|8|T=10|0,15|144,43|144,96|144,67|144,97|0,00104|0,59|0,33|1,05|0,26|
|D3|arriba junta|95,39|7,759|T=10|0,15|144,39|144,94|0,00|144,95|0,00071|0,50|0,46|2,39|0,22|
|D3|arriba junta|115,46|7,5181|T=10|0,15|144,36|144,94|0,00|144,94|0,00039|0,39|0,62|2,77|0,16|
|D3|arriba junta|135,52|7,2771|T=10|0,15|144,32|144,93|0,00|144,94|0,00021|0,30|0,81|3,20|0,12|
|D3|arriba junta|155,6|7,0361|T=10|0,15|144,29|144,93|0,00|144,93|0,00012|0,23|1,04|3,75|0,09|
|D3|arriba junta|158,61|7|T=10|0,15|144,28|144,93|144,47|144,93|0,00011|0,23|1,07|3,82|0,09|
|D3|bajo junta|178,67|6,9|T=10|0,40|144,28|144,92|0,00|144,93|0,00086|0,62|1,04|3,72|0,25|
|D3|bajo junta|198,72|6,42|T=10|0,40|144,22|144,86|0,00|144,89|0,00150|0,73|0,76|2,92|0,31|
|D3|bajo junta|218,77|6,18|T=10|0,40|144,19|144,82|0,00|144,85|0,00214|0,80|0,62|2,32|0,35|
|D3|bajo junta|237,8|6|T=10|0,40|144,17|144,78|144,57|144,81|0,00296|0,87|0,52|1,68|0,40|
|D3|bajo junta|257,8|5,802|T=10|0,40|144,13|144,72|144,52|144,75|0,00294|0,86|0,52|1,56|0,40|
|D3|bajo junta|277,79|5,604|T=10|0,40|144,10|144,66|144,47|144,69|0,00298|0,86|0,52|1,54|0,41|
|D3|bajo junta|297,78|5,4059|T=10|0,40|144,06|144,60|144,42|144,63|0,00305|0,87|0,52|1,56|0,42|
|D3|bajo junta|317,75|5,2079|T=10|0,40|144,02|144,53|144,37|144,57|0,00330|0,88|0,51|1,57|0,43|
|D3|bajo junta|337,72|5,0099|T=10|0,40|143,98|144,46|144,32|144,50|0,00410|0,93|0,48|1,57|0,48|
|D3|bajo junta|338,72|5|T=10|0,40|143,98|144,45|144,32|144,49|0,00414|0,94|0,48|1,57|0,48|
|D3|bajo junta|358,41|4,8131|T=10|0,40|143,91|144,38|144,22|144,42|0,00308|0,85|0,53|1,63|0,42|
|D3|bajo junta|378,39|4,6262|T=10|0,40|143,83|144,34|144,13|144,37|0,00205|0,75|0,61|1,84|0,35|
|D3|bajo junta|398,88|4,4393|T=10|0,40|143,76|144,32|144,04|144,33|0,00122|0,63|0,75|2,11|0,28|
|D3|bajo junta|420,1|4,2523|T=10|0,40|143,69|144,30|143,96|144,31|0,00074|0,53|0,89|2,16|0,22|
|D3|bajo junta|440,31|4,0654|T=10|0,40|143,62|144,29|143,88|144,30|0,00049|0,47|1,01|2,06|0,19|
|D3|bajo junta|445,94|4|T=10|0,40|143,59|144,29|143,85|144,30|0,00043|0,45|1,04|2,00|0,18|
|D3|bajo junta|452,26|3|T=10|0,40|143,95|144,27|144,16|144,29|0,00294|0,64|0,70|3,32|0,40|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.10 de<br>B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|bajo junta|471,1|2|T=10|0,40|143,64|144,25|143,96|144,26|0,00104|0,54|0,89|2,43|0,25|
|D3|bajo junta|491,09|1,6942|T=10|0,40|143,66|144,22|143,99|144,24|0,00107|0,57|0,86|2,57|0,26|
|D3|bajo junta|511,09|1,3884|T=10|0,40|143,68|144,19|143,98|144,21|0,00149|0,63|0,76|2,67|0,30|
|D3|bajo junta|531,1|1,0826|T=10|0,40|143,70|144,13|144,00|144,17|0,00353|0,80|0,54|2,34|0,45|
|D3|bajo junta|536,51|1|T=10|0,40|143,71|144,10|144,01|144,14|0,00600|0,92|0,46|1,87|0,56|

B.7 Eje hidráulico Con Proyecto - T=20 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=20|0,30|144,50|145,05|144,76|145,06|0,00059|0,44|0,89|2,83|0,20|
|D2|arriba junta|61,4|11|T=20|0,30|144,63|145,03|0,00|145,05|0,00039|0,67|0,56|1,99|0,34|
|D2|arriba junta|81,4|10,722|T=20|0,30|144,61|145,02|0,00|145,04|0,00034|0,64|0,58|2,03|0,32|
|D2|arriba junta|101,4|10,444|T=20|0,30|144,59|145,02|0,00|145,03|0,00030|0,61|0,61|2,08|0,30|
|D2|arriba junta|121,4|10,167|T=20|0,30|144,57|145,01|0,00|145,03|0,00026|0,58|0,65|2,13|0,28|
|D2|arriba junta|133,4|10|T=20|0,30|144,56|145,01|0,00|145,02|0,00024|0,57|0,67|2,15|0,27|
|D2|arriba junta|153,4|9,8601|T=20|0,30|144,54|145,01|0,00|145,02|0,00020|0,54|0,70|2,20|0,25|
|D2|arriba junta|173,4|9,7203|T=20|0,30|144,52|145,00|0,00|145,01|0,00018|0,51|0,74|2,26|0,24|
|D2|arriba junta|193,4|9,5804|T=20|0,30|144,50|145,00|0,00|145,01|0,00015|0,49|0,78|2,31|0,22|
|D2|arriba junta|213,4|9,4406|T=20|0,30|144,48|145,00|0,00|145,01|0,00013|0,47|0,82|2,36|0,21|
|D2|arriba junta|233,4|9,3007|T=20|0,30|144,46|145,00|0,00|145,00|0,00012|0,45|0,86|2,41|0,19|
|D2|arriba junta|253,4|9,1608|T=20|0,30|144,44|145,00|0,00|145,00|0,00010|0,43|0,91|2,47|0,18|
|D2|arriba junta|273,4|9,021|T=20|0,30|144,42|144,99|0,00|145,00|0,00009|0,41|0,96|2,52|0,17|
|D2|arriba junta|276,4|9|T=20|0,30|144,42|144,99|0,00|145,00|0,00009|0,40|0,96|2,53|0,17|
|D2|arriba junta|296,4|8,8519|T=20|0,30|144,40|144,99|0,00|145,00|0,00008|0,39|1,01|2,59|0,16|
|D2|arriba junta|316,4|8,7037|T=20|0,30|144,38|144,99|0,00|145,00|0,00007|0,37|1,06|2,65|0,15|
|D2|arriba junta|336,4|8,5556|T=20|0,30|144,36|144,99|0,00|145,00|0,00006|0,36|1,11|2,70|0,14|
|D2|arriba junta|356,4|8,4074|T=20|0,30|144,34|144,99|0,00|144,99|0,00005|0,34|1,17|2,76|0,13|
|D2|arriba junta|376,4|8,2593|T=20|0,30|144,31|144,99|0,00|144,99|0,00005|0,33|1,22|2,82|0,13|
|D2|arriba junta|396,4|8,1111|T=20|0,30|144,30|144,99|0,00|144,99|0,00004|0,31|1,27|2,88|0,12|
|D2|arriba junta|411,4|8|T=20|0,30|144,28|144,99|144,50|144,99|0,00004|0,30|1,32|2,92|0,12|
|D3|arriba junta|0|9|T=20|0,19|144,95|145,16|145,10|145,17|0,00300|0,51|0,47|3,74|0,38|
|D3|arriba junta|19,85|8,7368|T=20|0,19|144,81|145,10|144,99|145,12|0,00253|0,60|0,42|3,11|0,37|
|D3|arriba junta|39,67|8,4737|T=20|0,19|144,68|145,06|144,88|145,08|0,00163|0,60|0,43|2,69|0,31|
|D3|arriba junta|59,49|8,2105|T=20|0,19|144,54|145,03|144,77|145,05|0,00114|0,60|0,43|1,99|0,27|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.11 de<br>B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|arriba junta|75,33|8|T=20|0,19|144,43|145,01|144,71|145,03|0,00112|0,66|0,40|1,32|0,28|
|D3|arriba junta|95,39|7,759|T=20|0,19|144,39|145,00|0,00|145,01|0,00063|0,51|0,61|2,95|0,21|
|D3|arriba junta|115,46|7,5181|T=20|0,19|144,36|145,00|0,00|145,00|0,00035|0,40|0,80|3,34|0,16|
|D3|arriba junta|135,52|7,2771|T=20|0,19|144,32|144,99|0,00|144,99|0,00020|0,31|1,01|3,76|0,12|
|D3|arriba junta|155,6|7,0361|T=20|0,19|144,29|144,99|0,00|144,99|0,00012|0,25|1,28|4,36|0,09|
|D3|arriba junta|158,61|7|T=20|0,19|144,28|144,99|144,49|144,99|0,00011|0,24|1,32|4,41|0,09|
|D3|bajo junta|178,67|6,9|T=20|0,50|144,28|144,98|0,00|144,99|0,00083|0,65|1,27|4,31|0,25|
|D3|bajo junta|198,72|6,42|T=20|0,50|144,22|144,92|0,00|144,95|0,00146|0,77|0,97|3,92|0,31|
|D3|bajo junta|218,77|6,18|T=20|0,50|144,19|144,88|0,00|144,91|0,00196|0,83|0,85|5,04|0,34|
|D3|bajo junta|237,8|6|T=20|0,50|144,17|144,84|144,62|144,88|0,00293|0,93|0,64|2,38|0,41|
|D3|bajo junta|257,8|5,802|T=20|0,50|144,13|144,77|144,56|144,82|0,00300|0,94|0,63|2,18|0,42|
|D3|bajo junta|277,79|5,604|T=20|0,50|144,10|144,71|144,51|144,75|0,00309|0,95|0,61|1,94|0,42|
|D3|bajo junta|297,78|5,4059|T=20|0,50|144,06|144,65|144,46|144,69|0,00313|0,95|0,61|1,72|0,43|
|D3|bajo junta|317,75|5,2079|T=20|0,50|144,02|144,59|144,41|144,63|0,00336|0,96|0,60|1,68|0,45|
|D3|bajo junta|337,72|5,0099|T=20|0,50|143,98|144,51|144,36|144,55|0,00403|1,01|0,56|1,67|0,49|
|D3|bajo junta|338,72|5|T=20|0,50|143,98|144,50|144,35|144,55|0,00406|1,01|0,56|1,67|0,49|
|D3|bajo junta|358,41|4,8131|T=20|0,50|143,91|144,44|144,26|144,48|0,00308|0,92|0,62|1,73|0,43|
|D3|bajo junta|378,39|4,6262|T=20|0,50|143,83|144,39|144,17|144,42|0,00213|0,82|0,72|2,12|0,37|
|D3|bajo junta|398,88|4,4393|T=20|0,50|143,76|144,37|144,08|144,39|0,00132|0,70|0,86|2,29|0,30|
|D3|bajo junta|420,1|4,2523|T=20|0,50|143,69|144,35|143,99|144,37|0,00084|0,60|1,00|2,28|0,24|
|D3|bajo junta|440,31|4,0654|T=20|0,50|143,62|144,34|143,91|144,35|0,00059|0,54|1,11|2,13|0,21|
|D3|bajo junta|445,94|4|T=20|0,50|143,59|144,33|143,89|144,35|0,00053|0,52|1,14|2,06|0,20|
|D3|bajo junta|452,26|3|T=20|0,50|143,95|144,32|144,18|144,34|0,00243|0,65|0,87|3,60|0,37|
|D3|bajo junta|471,1|2|T=20|0,50|143,64|144,29|143,99|144,31|0,00115|0,60|1,01|2,60|0,26|
|D3|bajo junta|491,09|1,6942|T=20|0,50|143,66|144,27|144,02|144,29|0,00117|0,63|0,99|2,75|0,27|
|D3|bajo junta|511,09|1,3884|T=20|0,50|143,68|144,24|144,01|144,26|0,00157|0,69|0,89|3,04|0,32|
|D3|bajo junta|531,1|1,0826|T=20|0,50|143,70|144,17|144,03|144,21|0,00362|0,88|0,66|3,17|0,46|
|D3|bajo junta|536,51|1|T=20|0,50|143,71|144,14|144,04|144,18|0,00601|1,01|0,54|2,58|0,58|

B.8 Eje hidráulico Con Proyecto - T=25 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=25|0,31|144,50|145,06|144,76|145,06|0,00060|0,44|0,91|2,86|0,20|
|D2|arriba junta|61,4|11|T=25|0,31|144,63|145,03|0,00|145,05|0,00039|0,67|0,57|2,01|0,34|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.12 de<br>B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|81,4|10,722|T=25|0,31|144,61|145,03|0,00|145,05|0,00034|0,65|0,59|2,05|0,32|
|D2|arriba junta|101,4|10,444|T=25|0,31|144,59|145,02|0,00|145,04|0,00030|0,62|0,63|2,10|0,30|
|D2|arriba junta|121,4|10,167|T=25|0,31|144,57|145,02|0,00|145,03|0,00026|0,59|0,66|2,14|0,28|
|D2|arriba junta|133,4|10|T=25|0,31|144,56|145,02|0,00|145,03|0,00024|0,58|0,68|2,17|0,27|
|D2|arriba junta|153,4|9,8601|T=25|0,31|144,54|145,01|0,00|145,02|0,00021|0,55|0,71|2,22|0,25|
|D2|arriba junta|173,4|9,7203|T=25|0,31|144,52|145,01|0,00|145,02|0,00018|0,52|0,75|2,27|0,24|
|D2|arriba junta|193,4|9,5804|T=25|0,31|144,50|145,01|0,00|145,02|0,00016|0,50|0,79|2,32|0,22|
|D2|arriba junta|213,4|9,4406|T=25|0,31|144,48|145,00|0,00|145,01|0,00014|0,48|0,83|2,38|0,21|
|D2|arriba junta|233,4|9,3007|T=25|0,31|144,46|145,00|0,00|145,01|0,00012|0,46|0,88|2,43|0,20|
|D2|arriba junta|253,4|9,1608|T=25|0,31|144,44|145,00|0,00|145,01|0,00010|0,43|0,92|2,49|0,19|
|D2|arriba junta|273,4|9,021|T=25|0,31|144,42|145,00|0,00|145,01|0,00009|0,42|0,97|2,54|0,17|
|D2|arriba junta|276,4|9|T=25|0,31|144,42|145,00|0,00|145,01|0,00009|0,41|0,98|2,55|0,17|
|D2|arriba junta|296,4|8,8519|T=25|0,31|144,40|145,00|0,00|145,00|0,00008|0,40|1,02|2,60|0,16|
|D2|arriba junta|316,4|8,7037|T=25|0,31|144,38|145,00|0,00|145,00|0,00007|0,38|1,07|2,66|0,15|
|D2|arriba junta|336,4|8,5556|T=25|0,31|144,36|145,00|0,00|145,00|0,00006|0,36|1,13|2,72|0,15|
|D2|arriba junta|356,4|8,4074|T=25|0,31|144,34|144,99|0,00|145,00|0,00005|0,35|1,18|2,78|0,14|
|D2|arriba junta|376,4|8,2593|T=25|0,31|144,31|144,99|0,00|145,00|0,00005|0,33|1,23|2,84|0,13|
|D2|arriba junta|396,4|8,1111|T=25|0,31|144,30|144,99|0,00|145,00|0,00004|0,32|1,29|2,89|0,12|
|D2|arriba junta|411,4|8|T=25|0,31|144,28|144,99|144,50|145,00|0,00004|0,31|1,33|2,94|0,12|
|D3|arriba junta|0|9|T=25|0,20|144,95|145,17|145,10|145,18|0,00290|0,51|0,49|3,77|0,37|
|D3|arriba junta|19,85|8,7368|T=25|0,20|144,81|145,11|145,00|145,12|0,00245|0,60|0,45|3,21|0,36|
|D3|arriba junta|39,67|8,4737|T=25|0,20|144,68|145,07|144,88|145,08|0,00162|0,60|0,46|2,77|0,31|
|D3|arriba junta|59,49|8,2105|T=25|0,20|144,54|145,04|144,78|145,06|0,00119|0,61|0,45|2,07|0,28|
|D3|arriba junta|75,33|8|T=25|0,20|144,43|145,02|144,72|145,04|0,00118|0,68|0,40|1,35|0,29|
|D3|arriba junta|95,39|7,759|T=25|0,20|144,39|145,01|0,00|145,02|0,00066|0,52|0,63|3,01|0,21|
|D3|arriba junta|115,46|7,5181|T=25|0,20|144,36|145,00|0,00|145,01|0,00037|0,41|0,82|3,39|0,16|
|D3|arriba junta|135,52|7,2771|T=25|0,20|144,32|145,00|0,00|145,00|0,00022|0,32|1,03|3,82|0,13|
|D3|arriba junta|155,6|7,0361|T=25|0,20|144,29|144,99|0,00|145,00|0,00013|0,26|1,30|4,41|0,10|
|D3|arriba junta|158,61|7|T=25|0,20|144,28|144,99|144,50|145,00|0,00012|0,25|1,34|4,46|0,09|
|D3|bajo junta|178,67|6,9|T=25|0,51|144,28|144,98|0,00|145,00|0,00083|0,65|1,29|4,36|0,25|
|D3|bajo junta|198,72|6,42|T=25|0,51|144,22|144,93|0,00|144,95|0,00146|0,77|0,99|4,31|0,31|
|D3|bajo junta|218,77|6,18|T=25|0,51|144,19|144,89|0,00|144,92|0,00193|0,83|0,88|5,16|0,34|
|D3|bajo junta|237,8|6|T=25|0,51|144,17|144,84|144,62|144,88|0,00292|0,94|0,66|2,44|0,41|
|D3|bajo junta|257,8|5,802|T=25|0,51|144,13|144,78|144,57|144,82|0,00299|0,95|0,64|2,25|0,42|
|D3|bajo junta|277,79|5,604|T=25|0,51|144,10|144,72|144,52|144,76|0,00310|0,96|0,62|2,00|0,43|
|D3|bajo junta|297,78|5,4059|T=25|0,51|144,06|144,66|144,46|144,70|0,00313|0,95|0,62|1,75|0,43|
|D3|bajo junta|317,75|5,2079|T=25|0,51|144,02|144,59|144,41|144,63|0,00336|0,97|0,60|1,70|0,45|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.13 de<br>B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|bajo junta|337,72|5,0099|T=25|0,51|143,98|144,51|144,36|144,56|0,00401|1,01|0,57|1,68|0,49|
|D3|bajo junta|338,72|5|T=25|0,51|143,98|144,51|144,36|144,56|0,00405|1,02|0,57|1,68|0,49|
|D3|bajo junta|358,41|4,8131|T=25|0,51|143,91|144,44|144,26|144,48|0,00308|0,93|0,63|1,75|0,43|
|D3|bajo junta|378,39|4,6262|T=25|0,51|143,83|144,40|144,17|144,43|0,00213|0,82|0,73|2,15|0,37|
|D3|bajo junta|398,88|4,4393|T=25|0,51|143,76|144,37|144,08|144,39|0,00132|0,70|0,87|2,31|0,30|
|D3|bajo junta|420,1|4,2523|T=25|0,51|143,69|144,36|144,00|144,37|0,00084|0,60|1,02|2,29|0,24|
|D3|bajo junta|440,31|4,0654|T=25|0,51|143,62|144,34|143,92|144,36|0,00059|0,54|1,12|2,14|0,21|
|D3|bajo junta|445,94|4|T=25|0,51|143,59|144,34|143,89|144,35|0,00053|0,53|1,15|2,07|0,20|
|D3|bajo junta|452,26|3|T=25|0,51|143,95|144,33|144,18|144,35|0,00236|0,65|0,89|3,63|0,37|
|D3|bajo junta|471,1|2|T=25|0,51|143,64|144,30|144,00|144,31|0,00115|0,61|1,02|2,62|0,27|
|D3|bajo junta|491,09|1,6942|T=25|0,51|143,66|144,28|144,02|144,29|0,00116|0,64|1,00|2,78|0,27|
|D3|bajo junta|511,09|1,3884|T=25|0,51|143,68|144,24|144,01|144,26|0,00166|0,71|0,90|3,23|0,32|
|D3|bajo junta|531,1|1,0826|T=25|0,51|143,70|144,18|144,04|144,21|0,00361|0,88|0,67|3,20|0,46|
|D3|bajo junta|536,51|1|T=25|0,51|143,71|144,14|144,05|144,19|0,00601|1,02|0,55|2,64|0,58|

B.9 Eje hidráulico Con Proyecto - T=50 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=50|0,40|144,50|145,12|144,80|145,13|0,00061|0,48|1,10|3,14|0,20|
|D2|arriba junta|61,4|11|T=50|0,40|144,63|145,10|0,00|145,12|0,00037|0,72|0,70|2,20|0,34|
|D2|arriba junta|81,4|10,722|T=50|0,40|144,61|145,09|0,00|145,11|0,00033|0,69|0,73|2,24|0,32|
|D2|arriba junta|101,4|10,444|T=50|0,40|144,59|145,09|0,00|145,10|0,00029|0,67|0,76|2,28|0,30|
|D2|arriba junta|121,4|10,167|T=50|0,40|144,57|145,08|0,00|145,10|0,00026|0,64|0,80|2,33|0,29|
|D2|arriba junta|133,4|10|T=50|0,40|144,56|145,08|0,00|145,09|0,00024|0,62|0,82|2,36|0,28|
|D2|arriba junta|153,4|9,8601|T=50|0,40|144,54|145,08|0,00|145,09|0,00021|0,60|0,86|2,41|0,26|
|D2|arriba junta|173,4|9,7203|T=50|0,40|144,52|145,07|0,00|145,09|0,00018|0,57|0,90|2,46|0,25|
|D2|arriba junta|193,4|9,5804|T=50|0,40|144,50|145,07|0,00|145,08|0,00016|0,55|0,95|2,51|0,23|
|D2|arriba junta|213,4|9,4406|T=50|0,40|144,48|145,07|0,00|145,08|0,00014|0,53|0,99|2,57|0,22|
|D2|arriba junta|233,4|9,3007|T=50|0,40|144,46|145,07|0,00|145,07|0,00013|0,50|1,04|2,62|0,21|
|D2|arriba junta|253,4|9,1608|T=50|0,40|144,44|145,06|0,00|145,07|0,00011|0,48|1,09|2,67|0,20|
|D2|arriba junta|273,4|9,021|T=50|0,40|144,42|145,06|0,00|145,07|0,00010|0,47|1,13|2,73|0,19|
|D2|arriba junta|276,4|9|T=50|0,40|144,42|145,06|0,00|145,07|0,00010|0,46|1,14|2,74|0,18|
|D2|arriba junta|296,4|8,8519|T=50|0,40|144,40|145,06|0,00|145,07|0,00009|0,44|1,19|2,79|0,17|
|D2|arriba junta|316,4|8,7037|T=50|0,40|144,38|145,06|0,00|145,07|0,00008|0,43|1,25|2,85|0,17|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.14 de<br>B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|336,4|8,5556|T=50|0,40|144,36|145,06|0,00|145,06|0,00007|0,41|1,30|2,91|0,16|
|D2|arriba junta|356,4|8,4074|T=50|0,40|144,34|145,06|0,00|145,06|0,00006|0,39|1,36|2,96|0,15|
|D2|arriba junta|376,4|8,2593|T=50|0,40|144,31|145,06|0,00|145,06|0,00006|0,38|1,42|3,02|0,14|
|D2|arriba junta|396,4|8,1111|T=50|0,40|144,30|145,06|0,00|145,06|0,00005|0,37|1,48|3,08|0,13|
|D2|arriba junta|411,4|8|T=50|0,40|144,28|145,05|144,54|145,06|0,00005|0,36|1,52|3,13|0,13|
|D3|arriba junta|0|9|T=50|0,25|144,95|145,20|145,11|145,21|0,00237|0,51|0,61|3,93|0,35|
|D3|arriba junta|19,85|8,7368|T=50|0,25|144,81|145,15|145,05|145,17|0,00182|0,57|0,60|3,54|0,32|
|D3|arriba junta|39,67|8,4737|T=50|0,25|144,68|145,12|144,91|145,14|0,00125|0,58|0,62|3,15|0,28|
|D3|arriba junta|59,49|8,2105|T=50|0,25|144,54|145,10|144,82|145,11|0,00113|0,64|0,56|2,31|0,28|
|D3|arriba junta|75,33|8|T=50|0,25|144,43|145,08|144,76|145,10|0,00095|0,65|0,66|3,28|0,26|
|D3|arriba junta|95,39|7,759|T=50|0,25|144,39|145,07|0,00|145,08|0,00056|0,52|0,84|3,63|0,20|
|D3|arriba junta|115,46|7,5181|T=50|0,25|144,36|145,06|0,00|145,07|0,00033|0,41|1,05|4,01|0,16|
|D3|arriba junta|135,52|7,2771|T=50|0,25|144,32|145,06|0,00|145,06|0,00021|0,33|1,30|4,70|0,12|
|D3|arriba junta|155,6|7,0361|T=50|0,25|144,29|145,06|0,00|145,06|0,00013|0,27|1,60|5,33|0,10|
|D3|arriba junta|158,61|7|T=50|0,25|144,28|145,06|144,52|145,06|0,00012|0,26|1,65|5,45|0,10|
|D3|bajo junta|178,67|6,9|T=50|0,65|144,28|145,05|0,00|145,06|0,00087|0,70|1,59|5,22|0,26|
|D3|bajo junta|198,72|6,42|T=50|0,65|144,22|144,99|0,00|145,01|0,00140|0,80|1,38|8,40|0,31|
|D3|bajo junta|218,77|6,18|T=50|0,65|144,19|144,96|0,00|144,98|0,00157|0,80|1,36|8,23|0,31|
|D3|bajo junta|237,8|6|T=50|0,65|144,17|144,91|144,67|144,95|0,00279|0,99|0,85|3,24|0,41|
|D3|bajo junta|257,8|5,802|T=50|0,65|144,13|144,85|144,62|144,89|0,00285|1,00|0,83|3,11|0,41|
|D3|bajo junta|277,79|5,604|T=50|0,65|144,10|144,79|144,57|144,84|0,00298|1,02|0,80|2,91|0,43|
|D3|bajo junta|297,78|5,4059|T=50|0,65|144,06|144,72|144,52|144,77|0,00319|1,05|0,76|2,63|0,44|
|D3|bajo junta|317,75|5,2079|T=50|0,65|144,02|144,65|144,46|144,71|0,00353|1,08|0,72|2,26|0,47|
|D3|bajo junta|337,72|5,0099|T=50|0,65|143,98|144,58|144,41|144,63|0,00397|1,10|0,68|1,81|0,49|
|D3|bajo junta|338,72|5|T=50|0,65|143,98|144,57|144,41|144,63|0,00399|1,10|0,68|1,80|0,50|
|D3|bajo junta|358,41|4,8131|T=50|0,65|143,91|144,51|144,31|144,55|0,00323|1,03|0,75|2,25|0,45|
|D3|bajo junta|378,39|4,6262|T=50|0,65|143,83|144,46|144,22|144,50|0,00220|0,91|0,87|2,48|0,38|
|D3|bajo junta|398,88|4,4393|T=50|0,65|143,76|144,43|144,13|144,46|0,00143|0,78|1,02|2,53|0,31|
|D3|bajo junta|420,1|4,2523|T=50|0,65|143,69|144,41|144,04|144,43|0,00097|0,69|1,15|2,43|0,26|
|D3|bajo junta|440,31|4,0654|T=50|0,65|143,62|144,40|143,96|144,42|0,00072|0,63|1,25|2,23|0,23|
|D3|bajo junta|445,94|4|T=50|0,65|143,59|144,39|143,93|144,41|0,00066|0,62|1,27|2,14|0,22|
|D3|bajo junta|452,26|3|T=50|0,65|143,95|144,39|144,21|144,41|0,00206|0,68|1,11|3,95|0,35|
|D3|bajo junta|471,1|2|T=50|0,65|143,64|144,36|144,04|144,37|0,00130|0,69|1,18|2,86|0,29|
|D3|bajo junta|491,09|1,6942|T=50|0,65|143,66|144,33|144,06|144,35|0,00130|0,72|1,16|2,99|0,29|
|D3|bajo junta|511,09|1,3884|T=50|0,65|143,68|144,29|144,08|144,32|0,00176|0,78|1,07|3,62|0,34|
|D3|bajo junta|531,1|1,0826|T=50|0,65|143,70|144,23|144,08|144,27|0,00364|0,96|0,84|3,95|0,47|
|D3|bajo junta|536,51|1|T=50|0,65|143,71|144,18|144,08|144,24|0,00600|1,11|0,69|3,50|0,59|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.15 de<br>B.18|

B.10 Eje hidráulico Con Proyecto - T=100 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=100|0,46|144,50|145,15|144,82|145,16|0,00063|0,51|1,21|3,30|0,21|
|D2|arriba junta|61,4|11|T=100|0,46|144,63|145,13|0,00|145,15|0,00037|0,76|0,77|2,30|0,34|
|D2|arriba junta|81,4|10,722|T=100|0,46|144,61|145,12|0,00|145,14|0,00033|0,73|0,80|2,34|0,33|
|D2|arriba junta|101,4|10,444|T=100|0,46|144,59|145,12|0,00|145,14|0,00030|0,70|0,84|2,38|0,31|
|D2|arriba junta|121,4|10,167|T=100|0,46|144,57|145,11|0,00|145,13|0,00026|0,67|0,88|2,43|0,29|
|D2|arriba junta|133,4|10|T=100|0,46|144,56|145,11|0,00|145,13|0,00025|0,66|0,90|2,46|0,28|
|D2|arriba junta|153,4|9,8601|T=100|0,46|144,54|145,11|0,00|145,12|0,00022|0,63|0,94|2,51|0,27|
|D2|arriba junta|173,4|9,7203|T=100|0,46|144,52|145,10|0,00|145,12|0,00019|0,61|0,98|2,56|0,25|
|D2|arriba junta|193,4|9,5804|T=100|0,46|144,50|145,10|0,00|145,11|0,00017|0,59|1,03|2,61|0,24|
|D2|arriba junta|213,4|9,4406|T=100|0,46|144,48|145,10|0,00|145,11|0,00015|0,56|1,07|2,66|0,23|
|D2|arriba junta|233,4|9,3007|T=100|0,46|144,46|145,10|0,00|145,11|0,00014|0,54|1,12|2,71|0,22|
|D2|arriba junta|253,4|9,1608|T=100|0,46|144,44|145,10|0,00|145,11|0,00012|0,52|1,17|2,77|0,20|
|D2|arriba junta|273,4|9,021|T=100|0,46|144,42|145,09|0,00|145,10|0,00011|0,50|1,22|2,82|0,19|
|D2|arriba junta|276,4|9|T=100|0,46|144,42|145,09|0,00|145,10|0,00011|0,50|1,23|2,83|0,19|
|D2|arriba junta|296,4|8,8519|T=100|0,46|144,40|145,09|0,00|145,10|0,00010|0,48|1,28|2,89|0,18|
|D2|arriba junta|316,4|8,7037|T=100|0,46|144,38|145,09|0,00|145,10|0,00009|0,46|1,34|2,94|0,17|
|D2|arriba junta|336,4|8,5556|T=100|0,46|144,36|145,09|0,00|145,10|0,00008|0,44|1,39|3,00|0,17|
|D2|arriba junta|356,4|8,4074|T=100|0,46|144,34|145,09|0,00|145,09|0,00007|0,43|1,45|3,06|0,16|
|D2|arriba junta|376,4|8,2593|T=100|0,46|144,31|145,09|0,00|145,09|0,00006|0,41|1,51|3,12|0,15|
|D2|arriba junta|396,4|8,1111|T=100|0,46|144,30|145,09|0,00|145,09|0,00006|0,40|1,57|3,17|0,14|
|D2|arriba junta|411,4|8|T=100|0,46|144,28|145,09|144,56|145,09|0,00005|0,39|1,62|3,22|0,14|
|D3|arriba junta|0|9|T=100|0,29|144,95|145,22|145,12|145,23|0,00210|0,51|0,70|4,05|0,33|
|D3|arriba junta|19,85|8,7368|T=100|0,29|144,81|145,18|145,06|145,19|0,00158|0,57|0,70|3,71|0,30|
|D3|arriba junta|39,67|8,4737|T=100|0,29|144,68|145,16|144,94|145,17|0,00114|0,58|0,72|3,31|0,27|
|D3|arriba junta|59,49|8,2105|T=100|0,29|144,54|145,13|144,84|145,14|0,00114|0,67|0,64|2,46|0,28|
|D3|arriba junta|75,33|8|T=100|0,29|144,43|145,11|144,79|145,13|0,00092|0,66|0,77|3,60|0,26|
|D3|arriba junta|95,39|7,759|T=100|0,29|144,39|145,10|0,00|145,11|0,00056|0,53|0,96|3,97|0,20|
|D3|arriba junta|115,46|7,5181|T=100|0,29|144,36|145,10|0,00|145,10|0,00034|0,43|1,18|4,39|0,16|
|D3|arriba junta|135,52|7,2771|T=100|0,29|144,32|145,09|0,00|145,10|0,00022|0,35|1,46|5,22|0,13|
|D3|arriba junta|155,6|7,0361|T=100|0,29|144,29|145,09|0,00|145,09|0,00014|0,29|1,78|6,00|0,10|
|D3|arriba junta|158,61|7|T=100|0,29|144,28|145,09|144,54|145,09|0,00013|0,28|1,83|6,10|0,10|
|D3|bajo junta|178,67|6,9|T=100|0,75|144,28|145,08|0,00|145,09|0,00096|0,76|1,75|5,84|0,27|
|D3|bajo junta|198,72|6,42|T=100|0,75|144,22|145,02|0,00|145,04|0,00152|0,86|1,60|8,42|0,32|
|D3|bajo junta|218,77|6,18|T=100|0,75|144,19|144,99|0,00|145,01|0,00160|0,83|1,58|8,53|0,32|
|D3|bajo junta|237,8|6|T=100|0,75|144,17|144,96|144,71|144,98|0,00182|0,84|1,44|7,41|0,33|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.16 de<br>B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|bajo junta|257,8|5,802|T=100|0,75|144,13|144,89|144,66|144,94|0,00276|1,03|0,97|3,61|0,41|
|D3|bajo junta|277,79|5,604|T=100|0,75|144,10|144,83|144,60|144,88|0,00287|1,05|0,94|3,45|0,42|
|D3|bajo junta|297,78|5,4059|T=100|0,75|144,06|144,77|144,55|144,82|0,00306|1,08|0,90|3,21|0,44|
|D3|bajo junta|317,75|5,2079|T=100|0,75|144,02|144,70|144,50|144,76|0,00344|1,12|0,84|2,86|0,47|
|D3|bajo junta|337,72|5,0099|T=100|0,75|143,98|144,62|144,44|144,68|0,00416|1,19|0,76|2,31|0,51|
|D3|bajo junta|338,72|5|T=100|0,75|143,98|144,61|144,44|144,67|0,00419|1,19|0,76|2,28|0,51|
|D3|bajo junta|358,41|4,8131|T=100|0,75|143,91|144,55|144,34|144,60|0,00325|1,09|0,85|2,57|0,46|
|D3|bajo junta|378,39|4,6262|T=100|0,75|143,83|144,50|144,25|144,54|0,00223|0,95|0,98|2,69|0,39|
|D3|bajo junta|398,88|4,4393|T=100|0,75|143,76|144,47|144,16|144,50|0,00150|0,83|1,12|2,67|0,33|
|D3|bajo junta|420,1|4,2523|T=100|0,75|143,69|144,45|144,07|144,47|0,00105|0,74|1,25|2,52|0,28|
|D3|bajo junta|440,31|4,0654|T=100|0,75|143,62|144,43|143,99|144,46|0,00081|0,69|1,32|2,28|0,25|
|D3|bajo junta|445,94|4|T=100|0,75|143,59|144,43|143,96|144,45|0,00075|0,68|1,34|2,18|0,24|
|D3|bajo junta|452,26|3|T=100|0,75|143,95|144,42|144,23|144,44|0,00176|0,67|1,46|6,20|0,33|
|D3|bajo junta|471,1|2|T=100|0,75|143,64|144,39|144,06|144,41|0,00139|0,74|1,28|3,02|0,30|
|D3|bajo junta|491,09|1,6942|T=100|0,75|143,66|144,36|144,08|144,38|0,00154|0,81|1,26|3,58|0,32|
|D3|bajo junta|511,09|1,3884|T=100|0,75|143,68|144,32|144,10|144,35|0,00186|0,83|1,18|3,85|0,35|
|D3|bajo junta|531,1|1,0826|T=100|0,75|143,70|144,25|144,10|144,30|0,00360|0,99|0,96|4,30|0,47|
|D3|bajo junta|536,51|1|T=100|0,75|143,71|144,21|144,11|144,27|0,00601|1,16|0,78|3,79|0,60|

B.11 Eje hidráulico Con Proyecto - T=200 años

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|39,82|12|T=200|0,51|144,50|145,18|144,84|145,19|0,00065|0,53|1,29|3,41|0,21|
|D2|arriba junta|61,4|11|T=200|0,51|144,63|145,15|0,00|145,18|0,00038|0,79|0,82|2,36|0,35|
|D2|arriba junta|81,4|10,722|T=200|0,51|144,61|145,15|0,00|145,17|0,00035|0,77|0,86|2,40|0,33|
|D2|arriba junta|101,4|10,444|T=200|0,51|144,59|145,14|0,00|145,16|0,00031|0,74|0,89|2,45|0,32|
|D2|arriba junta|121,4|10,167|T=200|0,51|144,57|145,14|0,00|145,15|0,00028|0,71|0,93|2,49|0,30|
|D2|arriba junta|133,4|10|T=200|0,51|144,56|145,13|0,00|145,15|0,00026|0,70|0,95|2,52|0,29|
|D2|arriba junta|153,4|9,8601|T=200|0,51|144,54|145,13|0,00|145,15|0,00023|0,67|0,99|2,57|0,28|
|D2|arriba junta|173,4|9,7203|T=200|0,51|144,52|145,13|0,00|145,14|0,00021|0,64|1,04|2,62|0,26|
|D2|arriba junta|193,4|9,5804|T=200|0,51|144,50|145,12|0,00|145,14|0,00019|0,62|1,08|2,67|0,25|
|D2|arriba junta|213,4|9,4406|T=200|0,51|144,48|145,12|0,00|145,13|0,00017|0,60|1,13|2,72|0,24|
|D2|arriba junta|233,4|9,3007|T=200|0,51|144,46|145,12|0,00|145,13|0,00015|0,57|1,18|2,77|0,23|
|D2|arriba junta|253,4|9,1608|T=200|0,51|144,44|145,12|0,00|145,13|0,00013|0,55|1,23|2,83|0,21|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.17 de<br>B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D2|arriba junta|273,4|9,021|T=200|0,51|144,42|145,11|0,00|145,12|0,00012|0,53|1,28|2,88|0,20|
|D2|arriba junta|276,4|9|T=200|0,51|144,42|145,11|0,00|145,12|0,00012|0,53|1,29|2,89|0,20|
|D2|arriba junta|296,4|8,8519|T=200|0,51|144,40|145,11|0,00|145,12|0,00010|0,51|1,34|2,95|0,19|
|D2|arriba junta|316,4|8,7037|T=200|0,51|144,38|145,11|0,00|145,12|0,00009|0,49|1,39|3,00|0,18|
|D2|arriba junta|336,4|8,5556|T=200|0,51|144,36|145,11|0,00|145,12|0,00008|0,47|1,45|3,06|0,17|
|D2|arriba junta|356,4|8,4074|T=200|0,51|144,34|145,11|0,00|145,11|0,00008|0,46|1,51|3,12|0,17|
|D2|arriba junta|376,4|8,2593|T=200|0,51|144,31|145,11|0,00|145,11|0,00007|0,44|1,57|3,17|0,16|
|D2|arriba junta|396,4|8,1111|T=200|0,51|144,30|145,11|0,00|145,11|0,00006|0,43|1,63|3,23|0,15|
|D2|arriba junta|411,4|8|T=200|0,51|144,28|145,10|144,58|145,11|0,00006|0,42|1,68|3,27|0,15|
|D3|arriba junta|0|9|T=200|0,32|144,95|145,24|145,13|145,25|0,00199|0,52|0,76|4,13|0,32|
|D3|arriba junta|19,85|8,7368|T=200|0,32|144,81|145,20|145,07|145,21|0,00153|0,57|0,77|3,85|0,30|
|D3|arriba junta|39,67|8,4737|T=200|0,32|144,68|145,17|144,95|145,18|0,00114|0,59|0,78|3,39|0,27|
|D3|arriba junta|59,49|8,2105|T=200|0,32|144,54|145,15|144,86|145,16|0,00102|0,65|0,82|3,82|0,27|
|D3|arriba junta|75,33|8|T=200|0,32|144,43|145,13|144,81|145,15|0,00092|0,68|0,84|3,81|0,26|
|D3|arriba junta|95,39|7,759|T=200|0,32|144,39|145,12|0,00|145,13|0,00057|0,55|1,04|4,18|0,21|
|D3|arriba junta|115,46|7,5181|T=200|0,32|144,36|145,12|0,00|145,12|0,00035|0,44|1,27|4,62|0,16|
|D3|arriba junta|135,52|7,2771|T=200|0,32|144,32|145,11|0,00|145,12|0,00023|0,37|1,56|5,54|0,13|
|D3|arriba junta|155,6|7,0361|T=200|0,32|144,29|145,11|0,00|145,11|0,00015|0,31|1,90|6,41|0,11|
|D3|arriba junta|158,61|7|T=200|0,32|144,28|145,11|144,56|145,11|0,00014|0,30|1,95|6,49|0,10|
|D3|bajo junta|178,67|6,9|T=200|0,83|144,28|145,10|0,00|145,11|0,00104|0,80|1,86|6,22|0,28|
|D3|bajo junta|198,72|6,42|T=200|0,83|144,22|145,03|0,00|145,06|0,00151|0,87|1,74|8,42|0,32|
|D3|bajo junta|218,77|6,18|T=200|0,83|144,19|145,00|0,00|145,03|0,00158|0,84|1,72|8,53|0,32|
|D3|bajo junta|237,8|6|T=200|0,83|144,17|144,98|144,73|145,00|0,00167|0,82|1,70|8,61|0,32|
|D3|bajo junta|257,8|5,802|T=200|0,83|144,13|144,93|144,68|144,96|0,00223|0,96|1,37|7,29|0,37|
|D3|bajo junta|277,79|5,604|T=200|0,83|144,10|144,86|144,63|144,91|0,00285|1,08|1,04|3,97|0,43|
|D3|bajo junta|297,78|5,4059|T=200|0,83|144,06|144,80|144,57|144,85|0,00299|1,10|1,00|3,63|0,44|
|D3|bajo junta|317,75|5,2079|T=200|0,83|144,02|144,73|144,52|144,79|0,00337|1,15|0,94|3,27|0,47|
|D3|bajo junta|337,72|5,0099|T=200|0,83|143,98|144,64|144,47|144,71|0,00423|1,24|0,83|2,69|0,52|
|D3|bajo junta|338,72|5|T=200|0,83|143,98|144,64|144,46|144,71|0,00427|1,24|0,83|2,66|0,52|
|D3|bajo junta|358,41|4,8131|T=200|0,83|143,91|144,57|144,37|144,63|0,00326|1,13|0,92|2,80|0,46|
|D3|bajo junta|378,39|4,6262|T=200|0,83|143,83|144,53|144,27|144,57|0,00227|0,99|1,06|2,84|0,39|
|D3|bajo junta|398,88|4,4393|T=200|0,83|143,76|144,50|144,18|144,53|0,00156|0,87|1,19|2,76|0,33|
|D3|bajo junta|420,1|4,2523|T=200|0,83|143,69|144,48|144,10|144,50|0,00113|0,78|1,31|2,58|0,29|
|D3|bajo junta|440,31|4,0654|T=200|0,83|143,62|144,46|144,01|144,48|0,00089|0,74|1,38|2,32|0,26|
|D3|bajo junta|445,94|4|T=200|0,83|143,59|144,45|143,99|144,48|0,00083|0,72|1,39|2,21|0,25|
|D3|bajo junta|452,26|3|T=200|0,83|143,95|144,45|144,25|144,47|0,00162|0,67|1,63|6,68|0,32|
|D3|bajo junta|471,1|2|T=200|0,83|143,64|144,42|144,08|144,44|0,00140|0,77|1,45|4,31|0,30|

783-22-OT-00-MC-HI-001

|Col1|Proyecto: Parque Solar Parral|Col3|
|---|---|---|
||<br>**Tema:** EH en modificación de trazado cauce IGM|**Hoja:** B.18 de<br>B.18|

|Cauce|Tramo|Km<br>[m]|River Sta<br>HecRas<br>[-]|Col5|Q Total<br>[m3/s]|Min Ch El<br>[m snm]|W.S Elev<br>[m snm]|Crit W.S<br>[m snm]|E.G Elev<br>[m snm]|E.G<br>Slope<br>[-]|Vel Chnl<br>[m/s]|Flow<br>Area<br>[m2]|Top<br>Width<br>[m]|Froude<br># Chl<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D3|bajo junta|491,09|1,6942|T=200|0,83|143,66|144,38|144,10|144,41|0,00162|0,85|1,34|3,77|0,33|
|D3|bajo junta|511,09|1,3884|T=200|0,83|143,68|144,34|144,12|144,37|0,00192|0,87|1,27|4,03|0,36|
|D3|bajo junta|531,1|1,0826|T=200|0,83|143,70|144,28|144,12|144,32|0,00350|1,01|1,06|4,58|0,47|
|D3|bajo junta|536,51|1|T=200|0,83|143,71|144,23|144,14|144,29|0,00600|1,20|0,87|4,32|0,60|

783-22-OT-00-MC-HI-001

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.1: Precipitaciones Máximas Diarias (mm) para distintos períodos de retorno. Área****

| T | Pmáx [mm] |
| --- | --- |
| **[años]** | **Área del Proyecto**<br>**del PS Parral** |
| 2 <br>5 <br>10<br>25<br>50<br>100<br>200 | 65<br>88<br>104<br>125<br>142<br>158<br>175 |

**Tabla 2.2: Caudales máximos instantáneos****

| T<br>[años] | Caudal afluente<br>[m3/s] |
| --- | --- |
| 2 <br>5 <br>10<br>20<br>50<br>100 | 0,15 <br>0,20 <br>0,24 <br>0,30 <br>0,40 <br>0,46 |

**Tabla 3.1: Vértices del cauce en estudio (canal de drenaje N°2)****

| Vértice N° | Observación | Este<br>[m] | Norte<br>[m] |
| --- | --- | --- | --- |
| 1 | Inicio Cauce existente (canal drenaje N°2) | 236.699 | 6.004.015 |
| 2 | Conexión cauce en estudio con canal de drenaje N°3 | 236.329 | 6.004.500 |
| 3 | 100 m aguas abajo de conexión cauce en estudio y<br>canal de drenaje N°3 | 236.303 | 6.004.581 |

**Tabla 3.2: Vértices - situación con proyecto****

| Vértice N° | Observación | Este<br>[m] | Norte<br>[m] |
| --- | --- | --- | --- |
| 1 | ~~Inicio Cauce existente (canal drenaje N°2)~~ | 236.699 | 6.004.015 |
| 2 | Inicio tramo proyectado | 236.681 | 6.004.062 |
| 3 | Fin nuevo tramo proyectado<br>Conexión con canal de drenaje N°3 | 236.593 | 6.004.378 |

**Tabla 4.2: Caudales en cauce en estudio****

| T<br>[años] | Probabilidad de<br>Caudal afluente<br>excedencia<br>[m3/s]<br>[%] | Col3 |
| --- | --- | --- |
| 1,05<br>1,25<br>1,67<br>2 <br>5 <br>10<br>25<br>50<br>100 | ~~0,95~~<br>0,80<br>0,60<br>0,50<br>0,20<br>0,10<br>0,04<br>0,02<br>0,01 | 0,11 <br>0,12 <br>0,14 <br>0,15 <br>0,20 <br>0,24 <br>0,31 <br>0,40 <br>0,46 |

**Tabla 4.3: Crecidas [m3/s]****

| T<br>[años] | Probabilidad de Caudal afluente Caudal afluente<br>excedencia Cauce en estudio Canal Drenaje<br>(Drenaje N°2) N°3<br>[m3/s] [m3/s] | Col3 | Col4 |
| --- | --- | --- | --- |
| 1,05<br>1,25<br>1,67<br>2 <br>5 <br>10<br>25<br>50<br>100 | 0,95<br>0,80<br>0,60<br>0,50<br>0,20<br>0,10<br>0,04<br>0,02<br>0,01 | 0,11 <br>0,12 <br>0,14 <br>0,15 <br>0,20 <br>0,24 <br>0,31 <br>0,40 <br>0,46 | 0,07<br>0,07<br>0,09<br>0,10<br>0,13<br>0,15<br>0,20<br>0,25<br>0,29 |

**Tabla 4.4: Coeficientes de rugosidad de Manning en canales de tierra (Mery, 2013)****

| Descripción | Mínimo | Medio | Máximo |
| --- | --- | --- | --- |
| Con musgos y pastos<br> | 0,025 | 0,030 | 0,033 |
| ~~Fondo pedregoso y taludes con~~<br>vegetación | 0,025 | 0,035 | 0,040 |
| Sin vegetación | 0,025 | 0,028 | 0,033 |
| Hormigón liso |  | 0,016 |  |

**Tabla 5.1: Eje hidráulico - Situación Sin Proyecto (T=100 años)****

| Cauce | Tramo | Km<br>[m] | River<br>Sta | Col5 | Q Total<br>[m3/s] | Min Ch El<br>[m snm] | W.S. Elev<br>[m snm] | Crit W.S.<br>[m snm] | E.G. Elev<br>[m snm] | E.G.<br>Slope<br>[m/m] | Vel<br>Chnl<br>[m/s] | Flow<br>Area<br>[m2] | Top<br>Width<br>[m] | Froude<br># Chl<br>[-] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D2 | arriba junta | 39,82 | 12 | T=100 | 0,46 | 144,50 | 145,11 | 144,82 | 145,12 | 0,00088 | 0,57 | 1,06 | 3,09 | 0,24 |
| D2 | arriba junta | 59,77 | 11,794 | T=100 | 0,46 | 144,48 | 145,09 | 144,81 | 145,10 | 0,00094 | 0,59 | 1,06 | 3,24 | 0,25 |
| D2 | arriba junta | 79,77 | 11,589 | T=100 | 0,46 | 144,47 | 145,07 | 144,79 | 145,08 | 0,00100 | 0,60 | 1,05 | 3,36 | 0,26 |
| D2 | arriba junta | 99,8 | 11,383 | T=100 | 0,46 | 144,45 | 145,05 | 144,78 | 145,06 | 0,00105 | 0,61 | 1,06 | 3,64 | 0,27 |
| D2 | arriba junta | 119,84 | 11,178 | T=100 | 0,46 | 144,43 | 145,03 | 144,76 | 145,04 | 0,00096 | 0,58 | 1,08 | 3,38 | 0,25 |
| D2 | arriba junta | 137,16 | 11 | T=100 | 0,46 | 144,42 | 145,01 | 144,75 | 145,03 | 0,00097 | 0,58 | 1,06 | 3,25 | 0,25 |
| D2 | arriba junta | 157,14 | 10,755 | T=100 | 0,46 | 144,34 | 144,99 | 144,71 | 145,01 | 0,00097 | 0,61 | 1,09 | 3,62 | 0,25 |
| D2 | arriba junta | 177,14 | 10,51 | T=100 | 0,46 | 144,27 | 144,97 | 144,66 | 144,99 | 0,00095 | 0,61 | 1,08 | 3,46 | 0,24 |
| D2 | arriba junta | 197,15 | 10,265 | T=100 | 0,46 | 144,19 | 144,96 | 144,61 | 144,97 | 0,00097 | 0,60 | 1,04 | 2,96 | 0,23 |
| D2 | arriba junta | 217,16 | 10,02 | T=100 | 0,46 | 144,12 | 144,93 | 144,58 | 144,95 | 0,00108 | 0,58 | 0,97 | 2,45 | 0,23 |
| D2 | arriba junta | 218,76 | 10 | T=100 | 0,46 | 144,11 | 144,93 | 144,58 | 144,95 | 0,00110 | 0,58 | 0,97 | 2,42 | 0,23 |
| D2 | arriba junta | 238,71 | 9,6435 | T=100 | 0,46 | 144,09 | 144,92 | 144,51 | 144,93 | 0,00064 | 0,50 | 1,17 | 2,84 | 0,20 |
| D2 | arriba junta | 258,85 | 9,287 | T=100 | 0,46 | 144,07 | 144,91 | 144,46 | 144,92 | 0,00041 | 0,42 | 1,39 | 3,57 | 0,17 |
| D2 | arriba junta | 274,9 | 9 | T=100 | 0,46 | 144,05 | 144,91 | 144,42 | 144,91 | 0,00023 | 0,32 | 2,08 | 7,64 | 0,13 |
| D2 | arriba junta | 294,69 | 8,7528 | T=100 | 0,46 | 144,04 | 144,90 | 144,43 | 144,91 | 0,00033 | 0,38 | 1,54 | 3,87 | 0,15 |
| D2 | arriba junta | 314,91 | 8,5056 | T=100 | 0,46 | 144,04 | 144,89 | 144,43 | 144,90 | 0,00037 | 0,40 | 1,48 | 3,80 | 0,16 |
| D2 | arriba junta | 335 | 8,2583 | T=100 | 0,46 | 144,03 | 144,88 | 144,44 | 144,89 | 0,00043 | 0,42 | 1,42 | 3,48 | 0,16 |
| D2 | arriba junta | 354,94 | 8,0111 | T=100 | 0,46 | 144,02 | 144,87 | 144,45 | 144,88 | 0,00052 | 0,43 | 1,35 | 3,43 | 0,17 |
| D2 | arriba junta | 355,82 | 8 | T=100 | 0,46 | 144,02 | 144,87 | 144,45 | 144,88 | 0,00052 | 0,43 | 1,35 | 3,43 | 0,17 |
| D2 | arriba junta | 375,18 | 7,775 | T=100 | 0,46 | 144,07 | 144,86 | 144,50 | 144,87 | 0,00064 | 0,49 | 1,26 | 3,43 | 0,19 |
| D2 | arriba junta | 395,64 | 7,5501 | T=100 | 0,46 | 144,12 | 144,85 | 144,54 | 144,85 | 0,00080 | 0,55 | 1,16 | 3,43 | 0,22 |
| D2 | arriba junta | 416,02 | 7,3251 | T=100 | 0,46 | 144,18 | 144,82 | 144,57 | 144,84 | 0,00107 | 0,61 | 1,06 | 3,42 | 0,25 |
| D2 | arriba junta | 435,99 | 7,1001 | T=100 | 0,46 | 144,23 | 144,80 | 144,59 | 144,81 | 0,00158 | 0,68 | 0,94 | 3,37 | 0,31 |
| D2 | arriba junta | 444,77 | 7 | T=100 | 0,46 | 144,25 | 144,78 | 144,60 | 144,79 | 0,00198 | 0,72 | 0,87 | 3,32 | 0,34 |
| D2 | arriba junta | 464,76 | 6,7923 | T=100 | 0,46 | 144,18 | 144,74 | 144,56 | 144,75 | 0,00201 | 0,76 | 0,83 | 3,02 | 0,35 |
| D2 | arriba junta | 485,72 | 6,5846 | T=100 | 0,46 | 144,12 | 144,69 | 144,51 | 144,71 | 0,00201 | 0,79 | 0,81 | 2,75 | 0,35 |
| D2 | arriba junta | 505,61 | 6,3769 | T=100 | 0,46 | 144,05 | 144,65 | 144,46 | 144,67 | 0,00198 | 0,78 | 0,79 | 2,53 | 0,34 |
| D2 | arriba junta | 524,94 | 6,1693 | T=100 | 0,46 | 143,98 | 144,61 | 144,39 | 144,63 | 0,00195 | 0,77 | 0,78 | 2,33 | 0,33 |
| D2 | arriba junta | 541,11 | 6 | T=100 | 0,46 | 143,93 | 144,58 | 144,34 | 144,60 | 0,00194 | 0,75 | 0,77 | 2,19 | 0,33 |
| D2 | arriba junta | 560,93 | 5,7904 | T=100 | 0,46 | 143,92 | 144,55 | 144,30 | 144,57 | 0,00175 | 0,74 | 0,79 | 2,27 | 0,33 |
| D2 | arriba junta | 580,98 | 5,5807 | T=100 | 0,46 | 143,90 | 144,51 | 144,26 | 144,53 | 0,00154 | 0,71 | 0,83 | 2,37 | 0,31 |
| D2 | arriba junta | 601,4 | 5,3711 | T=100 | 0,46 | 143,89 | 144,49 | 144,22 | 144,50 | 0,00131 | 0,67 | 0,88 | 2,51 | 0,29 |
| D2 | arriba junta | 621,65 | 5,1614 | T=100 | 0,46 | 143,87 | 144,46 | 144,18 | 144,48 | 0,00107 | 0,62 | 0,95 | 2,74 | 0,27 |
| D2 | arriba junta | 636,55 | 5 | T=100 | 0,46 | 143,86 | 144,45 | 144,15 | 144,46 | 0,00091 | 0,58 | 1,03 | 3,05 | 0,25 |

**Tabla 6.1: Eje hidráulico - Situación Con Proyecto (T=100 años)****

| Cauce | Tramo | Km<br>[m] | River<br>Sta | Col5 | Q Total<br>[m3/s] | Min Ch El<br>[m snm] | W.S. Elev<br>[m snm] | Crit W.S.<br>[m snm] | E.G. Elev<br>[m snm] | E.G.<br>Slope<br>[m/m] | Vel<br>Chnl<br>[m/s] | Flow<br>Area<br>[m2] | Top<br>Width<br>[m] | Froude<br># Chl<br>[-] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D2 | arriba junta | 39,82 | 12 | T=100 | 0,46 | 144,50 | 145,15 | 144,82 | 145,16 | 0,00063 | 0,51 | 1,21 | 3,30 | 0,21 |
| D2 | arriba junta | 61,4 | 11 | T=100 | 0,46 | 144,63 | 145,13 | 0,00 | 145,15 | 0,00037 | 0,76 | 0,77 | 2,30 | 0,34 |
| D2 | arriba junta | 81,4 | 10,722 | T=100 | 0,46 | 144,61 | 145,12 | 0,00 | 145,14 | 0,00033 | 0,73 | 0,80 | 2,34 | 0,33 |
| D2 | arriba junta | 101,4 | 10,444 | T=100 | 0,46 | 144,59 | 145,12 | 0,00 | 145,14 | 0,00030 | 0,70 | 0,84 | 2,38 | 0,31 |
| D2 | arriba junta | 121,4 | 10,167 | T=100 | 0,46 | 144,57 | 145,11 | 0,00 | 145,13 | 0,00026 | 0,67 | 0,88 | 2,43 | 0,29 |
| D2 | arriba junta | 133,4 | 10 | T=100 | 0,46 | 144,56 | 145,11 | 0,00 | 145,13 | 0,00025 | 0,66 | 0,90 | 2,46 | 0,28 |
| D2 | arriba junta | 153,4 | 9,8601 | T=100 | 0,46 | 144,54 | 145,11 | 0,00 | 145,12 | 0,00022 | 0,63 | 0,94 | 2,51 | 0,27 |
| D2 | arriba junta | 173,4 | 9,7203 | T=100 | 0,46 | 144,52 | 145,10 | 0,00 | 145,12 | 0,00019 | 0,61 | 0,98 | 2,56 | 0,25 |
| D2 | arriba junta | 193,4 | 9,5804 | T=100 | 0,46 | 144,50 | 145,10 | 0,00 | 145,11 | 0,00017 | 0,59 | 1,03 | 2,61 | 0,24 |
| D2 | arriba junta | 213,4 | 9,4406 | T=100 | 0,46 | 144,48 | 145,10 | 0,00 | 145,11 | 0,00015 | 0,56 | 1,07 | 2,66 | 0,23 |
| D2 | arriba junta | 233,4 | 9,3007 | T=100 | 0,46 | 144,46 | 145,10 | 0,00 | 145,11 | 0,00014 | 0,54 | 1,12 | 2,71 | 0,22 |
| D2 | arriba junta | 253,4 | 9,1608 | T=100 | 0,46 | 144,44 | 145,10 | 0,00 | 145,11 | 0,00012 | 0,52 | 1,17 | 2,77 | 0,20 |
| D2 | arriba junta | 273,4 | 9,021 | T=100 | 0,46 | 144,42 | 145,09 | 0,00 | 145,10 | 0,00011 | 0,50 | 1,22 | 2,82 | 0,19 |
| D2 | arriba junta | 276,4 | 9 | T=100 | 0,46 | 144,42 | 145,09 | 0,00 | 145,10 | 0,00011 | 0,50 | 1,23 | 2,83 | 0,19 |
| D2 | arriba junta | 296,4 | 8,8519 | T=100 | 0,46 | 144,40 | 145,09 | 0,00 | 145,10 | 0,00010 | 0,48 | 1,28 | 2,89 | 0,18 |
| D2 | arriba junta | 316,4 | 8,7037 | T=100 | 0,46 | 144,38 | 145,09 | 0,00 | 145,10 | 0,00009 | 0,46 | 1,34 | 2,94 | 0,17 |
| D2 | arriba junta | 336,4 | 8,5556 | T=100 | 0,46 | 144,36 | 145,09 | 0,00 | 145,10 | 0,00008 | 0,44 | 1,39 | 3,00 | 0,17 |
| D2 | arriba junta | 356,4 | 8,4074 | T=100 | 0,46 | 144,34 | 145,09 | 0,00 | 145,09 | 0,00007 | 0,43 | 1,45 | 3,06 | 0,16 |
| D2 | arriba junta | 376,4 | 8,2593 | T=100 | 0,46 | 144,31 | 145,09 | 0,00 | 145,09 | 0,00006 | 0,41 | 1,51 | 3,12 | 0,15 |
| D2 | arriba junta | 396,4 | 8,1111 | T=100 | 0,46 | 144,30 | 145,09 | 0,00 | 145,09 | 0,00006 | 0,40 | 1,57 | 3,17 | 0,14 |
| D2 | arriba junta | 411,4 | 8 | T=100 | 0,46 | 144,28 | 145,09 | 144,56 | 145,09 | 0,00005 | 0,39 | 1,62 | 3,22 | 0,14 |
| D3 | arriba junta | 0 | 9 | T=100 | 0,29 | 144,95 | 145,22 | 145,12 | 145,23 | 0,00210 | 0,51 | 0,70 | 4,05 | 0,33 |
| D3 | arriba junta | 19,85 | 8,7368 | T=100 | 0,29 | 144,81 | 145,18 | 145,06 | 145,19 | 0,00158 | 0,57 | 0,70 | 3,71 | 0,30 |
| D3 | arriba junta | 39,67 | 8,4737 | T=100 | 0,29 | 144,68 | 145,16 | 144,94 | 145,17 | 0,00114 | 0,58 | 0,72 | 3,31 | 0,27 |
| D3 | arriba junta | 59,49 | 8,2105 | T=100 | 0,29 | 144,54 | 145,13 | 144,84 | 145,14 | 0,00114 | 0,67 | 0,64 | 2,46 | 0,28 |
| D3 | arriba junta | 75,33 | 8 | T=100 | 0,29 | 144,43 | 145,11 | 144,79 | 145,13 | 0,00092 | 0,66 | 0,77 | 3,60 | 0,26 |
| D3 | arriba junta | 95,39 | 7,759 | T=100 | 0,29 | 144,39 | 145,10 | 0,00 | 145,11 | 0,00056 | 0,53 | 0,96 | 3,97 | 0,20 |
| D3 | arriba junta | 115,46 | 7,5181 | T=100 | 0,29 | 144,36 | 145,10 | 0,00 | 145,10 | 0,00034 | 0,43 | 1,18 | 4,39 | 0,16 |
| D3 | arriba junta | 135,52 | 7,2771 | T=100 | 0,29 | 144,32 | 145,09 | 0,00 | 145,10 | 0,00022 | 0,35 | 1,46 | 5,22 | 0,13 |
| D3 | arriba junta | 155,6 | 7,0361 | T=100 | 0,29 | 144,29 | 145,09 | 0,00 | 145,09 | 0,00014 | 0,29 | 1,78 | 6,00 | 0,10 |
| D3 | arriba junta | 158,61 | 7 | T=100 | 0,29 | 144,28 | 145,09 | 144,54 | 145,09 | 0,00013 | 0,28 | 1,83 | 6,10 | 0,10 |
| D3 | bajo junta | 178,67 | 6,9 | T=100 | 0,75 | 144,28 | 145,08 | 0,00 | 145,09 | 0,00096 | 0,76 | 1,75 | 5,84 | 0,27 |
| D3 | bajo junta | 198,72 | 6,42 | T=100 | 0,75 | 144,22 | 145,02 | 0,00 | 145,04 | 0,00152 | 0,86 | 1,60 | 8,42 | 0,32 |
| D3 | bajo junta | 218,77 | 6,18 | T=100 | 0,75 | 144,19 | 144,99 | 0,00 | 145,01 | 0,00160 | 0,83 | 1,58 | 8,53 | 0,32 |

**Tabla 7.1: Eje hidráulico - Comparativa Sin v/s Con Proyecto (T=100 años)****

| Perfil<br>HecRas | X<br>[m] | Cota de<br>fondo<br>[m s.n.m.] | Cota aguas Sin<br>Proyecto<br>[m s.n.m.] | Cota aguas<br>Con Proyecto<br>[m s.n.m.] | Diferencia<br>[m] |
| --- | --- | --- | --- | --- | --- |
| 9 | 0 | 144,95 | 145,21 | 145,22 | 0,01 |
| 8,7368* | 19,85 | 144,81 | 145,16 | 145,18 | 0,02 |
| 8,4737* | 39,67 | 144,68 | 145,11 | 145,16 | 0,05 |
| 8,2105* | 59,49 | 144,54 | 145,05 | 145,13 | 0,08 |
| 8 | 75,33 | 144,43 | 144,99 | 145,11 | 0,12 |
| 7,759* | 95,39 | 144,39 | 144,93 | 145,10 | 0,17 |
| 7,5181* | 115,46 | 144,36 | 144,88 | 145,10 | 0,22 |
| 7,2771* | 135,52 | 144,32 | 144,85 | 145,09 | 0,24 |
| 7,0361* | 155,6 | 144,29 | 144,83 | 145,09 | 0,26 |
| 7 <br>Conexión<br>Proyectada | 158,61 | 144,28 | 144,82 | 145,09 | 0,27 |
| 6,42* | 198,72 | 144,22 | 144,79 | 145,02 | 0,23 |
| 6,18* | 218,77 | 144,19 | 144,75 | 144,99 | 0,24 |
| 6 | 237,8 | 144,17 | 144,71 | 144,96 | 0,25 |
| 5,802* | 257,8 | 144,13 | 144,65 | 144,89 | 0,24 |
| 5,604* | 277,79 | 144,10 | 144,60 | 144,83 | 0,23 |
| 5,4059* | 297,78 | 144,06 | 144,56 | 144,77 | 0,21 |
| 5,2079* | 317,75 | 144,02 | 144,52 | 144,70 | 0,18 |
| 5,0099* | 337,72 | 143,98 | 144,48 | 144,62 | 0,14 |
| 5 | 338,72 | 143,98 | 144,48 | 144,61 | 0,13 |
| 4,8131* | 358,41 | 143,91 | 144,46 | 144,55 | 0,09 |
| 4,6262* | 378,39 | 143,83 | 144,46 | 144,50 | 0,04 |
| 4,4393* | 398,88 | 143,76 | 144,45 | 144,47 | 0,02 |
| 4,2523* | 420,1 | 143,69 | 144,45 | 144,45 | 0,00 |
| 4,0654* | 440,31 | 143,62 | 144,44 | 144,43 | -0,01 |
| 4 | 445,94 | 143,59 | 144,44 | 144,43 | -0,01 |
| 3 <br>Conexión Actual | 452,26 | 143,95 | 144,42 | 144,42 | 0,00 |
| 2 | 471,1 | 143,64 | 144,39 | 144,39 | 0,00 |

**Tabla 7.2: (T=100 años)****

| Perfil<br>HecRas | X<br>[m] | Cota borde<br>izquierdo<br>[m s.n.m.] | Cota borde<br>derecho<br>[m s.n.m.] | Cota de<br>aguas con<br>Proyecto<br>[m s.n.m.] | Revancha<br>borde<br>izquierdo<br>[m] | Revancha<br>borde<br>derecho<br>[m] | Peralte<br>borde<br>izquierdo<br>[m] | Peralte<br>borde<br>derecho<br>[m] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | 0 | 145,47 | 145,53 | 145,22 | 0,25 | 0,31 |  |  |
| 8 | 75,33 | 145,35 | 145,50 | 145,11 | 0,24 | 0,39 |  |  |
| 7 | 158,61 | 145,17 | 145,22 | 145,09 | **0,08** | **0,13** | 0,2 | 0,2 |
| 6 | 237,80 | 144,96 | 144,96 | 144,96 | **0,00** | **0,00** | 0,2 | 0,2 |
| 5 | 338,72 | 144,99 | 144,98 | 144,61 | 0,38 | 0,37 |  |  |
| 4 | 445,94 | 144,64 | 144,64 | 144,43 | 0,21 | 0,21 |  |  |
| 3 | 452,26 | 144,39 | 144,52 | 144,42 | **-0,03** | **0,10** | 0,25 | 0,2 |
| 2 | 471,10 | 144,58 | 144,47 | 144,39 | **0,19** | **0,08** | 0,2 | 0,2 |
| 1 | 536,51 | 144,47 | 144,49 | 144,21 | 0,26 | 0,28 |  |  |
