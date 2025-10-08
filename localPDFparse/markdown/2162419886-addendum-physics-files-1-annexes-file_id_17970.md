---
title: Sin título
author: ALUVIAL CONSULTORES
date: D:20241213152526-03'00'
language: es
type: report
pages: 35
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INTRODUCCIÓN
  - MARCO HIDROGEOLÓGICO
  - RESUMEN MODELO NUMÉRICO DE FLUJO
  - MODELO DE TRANSPORTE
  - CONCLUSIONES
-->

## Modelo numérico Modelo numérico de transporte del Tranque de Relaves Ladera Sur

**CAPSTONE COPPER**

### Diciembre 2024

## Preparada por Aluvial Consultoría Hidrogeológica Spa

## CONTENIDO

INTRODUCCIÓN ..................................................................................................................... 5

1.1 OBJETIVOS ...................................................................................................................... 5

MARCO HIDROGEOLÓGICO................................................................................................... 6

RESUMEN MODELO NUMÉRICO DE FLUJO ......................................................................... 14

MODELO DE TRANSPORTE .................................................................................................. 24

4.1 PROCESOS DEL TRANSPORTE DE SOLUTOS ................................................................. 25

4.2 CONDICIONES DE CONTORNO, INICIALES Y PARÁMETROS HIDROGEOLÓGICOS

ADOPTADOS EN EL MODELO TRANSPORTE ........................................................................... 27

4.2.1 Condición de carga de solutos en la fuente ......................................................... 27

4.2.2 Condición inicial de concentración de solutos en el sistema ............................... 27

4.2.3 Parámetros de transporte .................................................................................... 28

4.3 RESULTADOS Y ANÁLISIS .............................................................................................. 29

**Sensibilidad del modelo** ..................................................................................................... 33

CONCLUSIONES ................................................................................................................... 34

## ÍNDICE DE FIGURAS

Figura 2.1. Sistema hidrogeológico entorno a la operación. Fuente: Aluvial Consultores. ......... 7

Figura 2.2 Pozos y/o sondajes con ensayos de permeabilidad. Fuente: Aluvial Consultores. .... 9

Figura 2.3. Niveles piezométricos en el sistema hidrogeológico. Fuente: Aluvial Consultores. 11

Figura 2.4 Representación del tipo de aguas mediante diagramas de Stiff modificados. Fuente:

Aluvial Consultores. .................................................................................................................... 12

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 2 de 35

Figura 2.5 Concentración de sulfato registrado en los últimos 12 meses. Fuente: Aluvial

Consultores. ................................................................................................................................ 13

Figura 3.1. Dominio de modelación y malla de diferencias finitas. Fuente: Aluvial Consultores.

.................................................................................................................................................... 15

Figura 3.2. Infiltración en el tiempo simulada desde el tranque para el escenario Base y error

balance (%). Infiltración en escala logarítmica. Fuente: Aluvial Consultores, 2023. ................. 19

Figura 3.3. Infiltración en el tiempo simulada desde el tranque para el escenario E1 y error

balance (%). Infiltración en escala logarítmica. Fuente: Aluvial Consultores, 2023. ................. 20

Figura 3.4. Volumen infiltrado acumulado en el tiempo para el escenario E1. Infiltración en

escala logarítmica. Fuente: Aluvial Consultores. ....................................................................... 20

Figura 3.5. Niveles en el tiempo en pozos simulados durante la etapa de operación y cierre del

TSF para el escenario E1. Fuente: Aluvial Consultores. ............................................................. 21

Figura 3.6. Piezometría al final de la etapa de operación estimada para el escenario E1. Fuente:

Aluvial Consultores. .................................................................................................................... 21

Figura 3.7. Piezometría al final de la etapa de cierre estimada para el escenario E1. Fuente:

Aluvial Consultores. .................................................................................................................... 22

Figura 3.8. Infiltración en el tiempo simulada desde el tranque para el escenario E2 y error

balance (%). Infiltración en escala logarítmica. Fuente: Aluvial Consultores, 2023. ................. 23

Figura 3.9. Infiltración en el tiempo simulada desde el tranque para el escenario E3 y error

balance (%). Infiltración en escala logarítmica. Fuente: Aluvial Consultores, 2023. ................. 24

Figura 4.1. Distribución espacial de la concentración en el tiempo estimada. Caso base, 2000

mg/l de sulfato en la fuente. ...................................................................................................... 31

Figura 4.2. Concentración relativa estimada en el tiempo en los pozos de monitoreo. Fuente:

Aluvial Consultores. .................................................................................................................... 32

Figura 4.3. Concentración en el tiempo en los pozos de monitoreo para concentraciones de

2000, 3000, 4000, 5000 mg/l de sulfato en la fuente. Fuente: Aluvial Consultores. ................. 32

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 3 de 35

Figura 4.4. Concentración relativa estimada en el tiempo en los pozos de monitoreo

considerando una dispersividad longitudinal de 100 m. Fuente: Aluvial Consultores. ............. 33

## ÍNDICE DE TABLAS

Tabla 3.1. Cotas de la laguna operacional proyectadas en plan de depositación. .................... 17

Tabla 3.2. Parámetros considerados para el escenario Base y análisis de sensibilidad. ........... 18

Tabla 3.3. Resumen balance hídrico........................................................................................... 19

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 4 de 35

# INTRODUCCIÓN

El tranque de relaves Ladera Sur, ubicado en el sector intermedio y bajo de la Quebrada de

Guamanga, es la estructura diseñada para contener los relaves de la operación Mantoverde.

Las posibles infiltraciones de aguas desde el tranque hacia el sistema hidrogeológico

constituyen un potencial impacto en la cantidad y calidad de las aguas subterráneas locales.

Debido a esto se realiza un modelo numérico de transporte de solutos para evaluar los posibles

efectos en la calidad del agua subterránea, tomando como base el modelo conceptual y

numérico de flujo existente para el tranque (Aluvial, 2023).

Si bien las simulaciones se enfocan en los posibles efectos del tranque de relaves en las aguas

subterráneas, el área del modelo abarca la totalidad del modelo de flujo existente.

El informe se organiza en capítulos, que cubren un marco hidrogeológico del área del tranque,

un resumen del modelo numérico de flujo existente que constituye la base de flujo para la

resolución del transporte, los principios y metodología del modelo de transporte, los resultados

obtenidos relacionados al transporte y conclusiones.

### 1.1 OBJETIVOS

El objetivo principal del modelo es evaluar el comportamiento del transporte de solutos en el

sistema hidrogeológico, simular la propagación de los solutos desde el tranque de relaves hasta

el acuífero durante la etapa de operación y cierre del tranque, evaluando su impacto en las

concentraciones de los solutos en el agua subterránea y su velocidad de propagación.

El modelo se utilizará como herramienta para robustecer el plan de monitoreo de aguas

subterráneas y las medidas de control de las posibles infiltraciones del tranque.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 5 de 35

# MARCO HIDROGEOLÓGICO

En el Modelo Conceptual y Numérico de Flujo existente (Aluvial, 2023) se presenta una

caracterización hidrogeológica detallada del sistema de Guamanga, cuyos principales aspectos

se resumen a continuación.

El tranque de relaves Ladera Sur se emplaza entre las Ramas Central y Occidental del Sistema

de Fallas de Atacama (SFA), las cuales han ejercido un control estructural sobre la geología

regional y local. La quebrada de Guamanga correspondería a un sistema hidrogeológico

localmente confinado y alojado en la base del relleno sedimentario, en la interfaz

roca/sedimentos, con comportamientos hidráulicos e hidroquímicos de carácter local,

desconectado a lo largo de la quebrada Guamanga.

Presentándose en general características de baja permeabilidad en sedimento y en roca, a lo

largo de la quebrada de Guamanga, las aguas se encontrarían en almacenamientos locales con

limitada conexión hidráulica a lo largo de la quebrada (Figura 2.1).

En las zonas de falla la geometría del basamento impone un control piezométrico, que da lugar

a zonas de embalse subterráneo, que constituyen los principales almacenamientos del recurso

identificados en la quebrada de Guamanga. Éstos se desarrollan en la roca fracturada en torno

al sistema local de fallas y bajo el relleno sedimentario, que actúa como estrato confinante.

Se ha identificado en el sector Gighlino, ubicado aguas abajo del TSF, una zona de embalse

local. Además, se ha identificado un almacenamiento local frente al futuro tranque, a la vez

que podría haber otros almacenamientos locales no identificados aun por ausencia de

información. Fuera de las zonas de embalse se presentaría una baja permeabilidad y

transmisividad que limitaría los flujos pasantes de agua subterránea a lo largo de la quebrada.

Las diferencias litológicas y de permeabilidad de las distintas unidades condicionan los tiempos

de residencia del agua subterránea, y en parte la concentración de solutos en éstas.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 6 de 35

Figura 2.1. Sistema hidrogeológico entorno a la operación. Fuente: Aluvial Consultores.

#### Parámetros hidráulicos

Para el sistema fracturado y sedimentario de Guamanga, los antecedentes indican un rango

amplio de valores para la permeabilidad equivalente (1E-4 a 15 m/d), identificándose los

valores medios altos (0.1 - 15 m/d) en torno a las zonas de basamento fracturado en las zonas

de embalse, y los valores medios bajos (1E-4 - 0.1 m/d) entre dichas zonas (Figura 2.2).

Para las pruebas de bombeo de los pozos SQG-1A, GWP-1C (Xterrae 2015, Golder 2015), GWP

02, PB-02, PB-03, PB-04 y PM-05 (Xterrae 2015, Golder 2015, Aluvial 2023), se han estimado

permeabilidades de entre 0.1 y 5 m/d, mientras que en los pozos PB-07 y PB-08 (Aluvial 2023),

se estiman valores del orden de 10 y 15 m/d. Los coeficientes de almacenamiento de roca

fracturada y depósitos se estiman en general en el rango 1E-4 - 1E-3 [1/m] (Xterrae, 2015,

Aluvial, 2023), indicando condiciones de confinamiento.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 7 de 35

Las pruebas realizadas en los pozos PB-01, PB-05, PB-06, PM-01, PM-02, PM-04 y PM-06

(Aluvial, 2023) y las demás pruebas puntuales, permiten identificar en general condiciones de

baja permeabilidad (< 5E-2 m/d) fuera de las zonas de falla.

De forma particular, las pruebas de bombeo de los pozos PB-02, PB-03 y PB-04, han permitido

identificar un aporte asociado a la roca y estratos sobreyacentes que permiten un

almacenamiento local, con permeabilidad equivalente estimada en torno a los 5 m/d. Las

pruebas puntuales realizadas en el entorno en sondajes a distintas profundidades (Xterrae

2015, Golder 2015), registran valores de conductividad hidráulica media baja, en el rango 1E-4

- 0.1 m/d para roca y sedimento, presentándose una baja permeabilidad en profundidad, en

general menor a 0.05 m/d bajo los 10 m de profundidad. Las permeabilidades de sedimentos

en subsuperficie (1 - 10 m de profundidad) en dicho sector se han estimado entre 0.01 y 6.7

m/d a partir de las pruebas puntuales y ensayos de infiltración realizados en calicatas (Golder,

2015).

El basamento no fracturado puede caracterizarse con almacenamiento y permeabilidades muy

bajas a nulas.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 8 de 35

Figura 2.2 Pozos y/o sondajes con ensayos de permeabilidad. Fuente: Aluvial Consultores.

#### Niveles de agua subterránea

La profundidad del nivel piezométrico es coherente con el comportamiento de la pendiente

topográfica del terreno y con el relieve del basamento, el cual se eleva en las ZFA Oriental y

Occidental, dando lugar a una disminución de la profundidad del nivel en el entorno aguas

arriba de las citadas fallas.En torno a la zona en que se ubica el tranque se observan niveles

piezométricos a profundidades de entre 40 y 73 m bajo el nivel de terreno, a una cota del orden

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 9 de 35

de 662 msnm, registrándose niveles asociados a agua en el relleno sedimentario y también

niveles en roca (Figura 2.3).

El acuífero de Guamanga se desarrollaría confinado/semiconfinado bajo el tranque proyectado,

al sur del eje actual del drenaje superficial de la quebrada Guamanga.

De esta forma, el flujo subterráneo ocurriría de forma preferencial a profundidades mayores

que las del nivel piezométrico señalado, presentando cierto grado de desconexión con la

superficie debido a las características de baja permeabilidad de los sedimentos que los

confinan.

Inmediatamente aguas abajo del tranque se observa un descenso de niveles con aumento local

del gradiente hidráulico, luego disminuye la profundidad del nivel piezométrico hacia la ZFA

Occidental estableciéndose un menor gradiente en torno al 0.3% hacia la zona terminal del

acuífero, donde la geometría del basamento limita al acuífero sedimentario Guamanga.

Se han presentado niveles dinámicos históricos en las zonas de embalse oriental y occidental,

y en acuífero Mantoverde debido a las labores de dewatering.

Los descensos producidos permiten inferir que la recarga de dicho sector es inferior a la

descarga y extracciones, ocurriendo estas últimas desde el almacenamiento del acuífero.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 10 de 35

Figura 2.3. Niveles piezométricos en el sistema hidrogeológico. Fuente: Aluvial Consultores.

#### Hidroquímica

La calidad del agua de los sistemas acuíferos de la Falla Mantoverde y de la Quebrada

Guamanga corresponde al tipo clorurado sódico (Figura 2.4), con significativas diferencias

espaciales en la concentración del agua para algunos solutos, lo que podría explicarse debido

a diferencias en los tiempos de residencia y variabilidad litológica.

A la vez se observa variabilidad temporal significativa en algunos periodos de monitoreo en

algunos pozos, lo que en parte podría explicarse por irregularidades en el muestreo y/o errores

de medición de laboratorio.

Se ha definido la línea base de los parámetros críticos (CE, pH, Cobre, Molibdeno, Sulfato,

Cloruro y PNE) que podrían verse afectados en el sistema hidrogeológico, la cual se presenta

en el plan de monitoreo de aguas subterráneas. Para esto se han considerado los registros de

calidad de las aguas y registros de profundidad del nivel freático desde noviembre 2022 a

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 11 de 35

noviembre 2023, de la actual red de control de MV y de las ultima analíticas de los 13 nuevos

pozos de monitoreo y bombeo que han sido construidos en torno al Tranque.

En particular se presentan las concentraciones de sulfato en los pozos aguas arriba del tranque,

en el sector del tranque y aguas debajo de este (Figura 2.5). Mayor detalle se presenta en el

modelo conceptual y numérico de flujo (Aluvial, 2023).

Figura 2.4 Representación del tipo de aguas mediante diagramas de Stiff modificados. Fuente:

Aluvial Consultores.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 12 de 35

Figura 2.5 Concentración de sulfato registrado en los últimos 12 meses. Fuente: Aluvial

Consultores.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 13 de 35

# RESUMEN MODELO NUMÉRICO DE FLUJO

El modelo numérico de flujo con el que se cuenta para el TSF y la Quebrada de Guamanga

(Aluvial, 2023) se ha desarrollado en función de modelo conceptual con el código de diferencias

finitas MODFLOW, en su interface VISUAL MODFLOW CLASSIC y MODFLOW FLEX 8.0. Detalles

específicos del modelo numérico de flujo y sus resultados de calibración se encuentran en el

informe Modelo Conceptual y Numérico de Flujo Actualización 2023 (Aluvial, 2023), para el cual

se consideran futuras actualizaciones.

El modelo numérico de flujo constituye la base para la modelación de transporte.

**Discretización**

La discretización horizontal del modelo se ha realizado con celdas del orden de 5 m en los pozos

de bombeos ubicados en las zonas de embalse, aumentando su tamaño al alejarse de estas,

alcanzando el orden de los 50 - 150 m en la zona del tranque, y hasta 300 m en otras zonas de

menor interés ( Figura 3.1 ). Los efectos de infiltración desde el tranque se han considerado

resolviendo el flujo en condiciones de saturación variable utilizando el código MODFLOW

SURFACT.

Para esto el modelo ha sido discretizado en 14 capas en la vertical, de menor espesor en torno

a la interfaz de infiltración.

Se han evaluado discretizaciones más finas, las cuales aumentan los tiempos de ejecución,

entregando resultados similares a la malla antes comentada finalmente empleada. El uso de

mallas refinadas debe evaluarse en caso de contar con mayor información que justifique

posibles heterogeneidades y de requerirse detalles espaciales en zonas específicas según los

resultados generales levantados.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 14 de 35

Figura 3.1. Dominio de modelación y malla de diferencias finitas. Fuente: Aluvial Consultores.

**Parametrización**

La zonificación de las unidades con sus respectivos parámetros hidráulicos se realizó acorde al

modelo conceptual, la caracterización geológica-estratigráfica y de parámetros hidráulicos,

considerando magnitudes de estos en torno a los obtenidas a partir de los ensayos de bombeo

realizados el 2023 en los 13 pozos del TSF, de las pruebas de permeabilidad puntual (Xterrae

2015, Golder 2015) y los ensayos de bombeo existentes en los pozos GWP-2 y GWP-1C.

Fuera de las zonas de embalse el modelo se ha calibrado con una conductividad hidráulica

homogénea de 0.001 m/d y conductividades hidráulicas mayores, en torno a los 3 - 9 m/d, en

las zonas de embalse identificadas. Para la zona de baja permeabilidad se ha calibrado un

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 15 de 35

coeficiente de almacenamiento de 0.1 en sedimento y de 0.025 para la roca. En las zonas de

embalse se calibran coeficientes de almacenamiento del orden de 0.2.

En cuanto a las simulaciones de infiltración desde el tranque, si bien los relaves alcanzarían

permeabilidades de entre 1E-3 y 1E-5 m/d (Golder 2016) durante su procedo de compactación,

de forma conservadora se supone que la permeabilidad del suelo controla la infiltración, la cual

se ha caracterizado en 0.001 m/d para la zona no saturada bajo el tranque.

Se han simulado además escenarios en condiciones desfavorables para evaluar la infiltración

desde el tranque, considerando una permeabilidad un orden de magnitud mayor, o sea, de

0.01 m/d fuera de las zonas de embalse y una disminución de la porosidad en un orden de

magnitud en dichas zonas.

**Condiciones de borde y condición inicial de niveles**

De acuerdo a niveles observados en pozos, se han fijado condiciones de borde de nivel fijo en

los extremos de aguas arriba (924 msnm) y abajo del modelo (596.8 msnm) para simular la

entrada y salida subterránea del sistema. Estas condiciones han sido ubicadas lo

suficientemente lejos de las zonas de interés a estudiar para descartar la influencia efectos de

las condiciones de contorno.

Bajo la última capa y por los bordes del modelo se ubica el basamento o roca fundamental, el

cual ha sido considerado como condición de no flujo debido a sus características de muy baja

permeabilidad.

Las conductividades hidráulicas calibradas han permitido ajustar los niveles simulados a los

observados para el año 1997, considerando que el sistema se encuentra en un estado

estacionario para dicho año (no se encuentra experimentando cambios importantes en el

almacenamiento), obteniendo así una condición piezométrica inicial estable para el modelo.

Luego, las conductividades hidráulicas calibradas junto a la calibración de coeficientes de

almacenamiento permiten reproducir el periodo transiente observado hasta el año 2023

validando el modelo numérico hasta el momento previo al inicio de la operación del tranque

de relaves, y permitiendo contar con una condición inicial de niveles antes de la depositación.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 16 de 35

Para simular la infiltración desde el tranque se considera las cotas de laguna operacional

asociadas al nuevo plan de depositación (Tabla 3.1). En función de estas se imponen una

condición de nivel fijo en la base del depósito, dando lugar a una infiltración que es

directamente proporcional a la permeabilidad de la interfaz de infiltración y el área.

Si bien la depositación del relave es gradual en el tiempo, para efectos de las simulaciones

realizadas se discretiza en etapas de crecimiento asumiendo llenado instantáneo. Así, los

resultados sobreestiman la infiltración al inicio de cada etapa, cuando los suelos están secos y

los altos gradientes hidráulicos producto de las fuerzas capilares controlan la infiltración. En los

análisis realizados de los resultados, se consideró como representativa la tasa estabilizada se

infiltración en cada etapa.

Tabla 3.1. Cotas de la laguna operacional proyectadas en plan de depositación .

|Año|Cota Laguna<br>Operacional<br>[msnm]|
|---|---|
|1|735.78|
|5|755.78|
|10|767.20|
|20|786.32|

Se supuso que los relaves se mantienen saturados durante toda la operación del tranque

imponiendo una condición de nivel igual a la de la laguna operacional en la base del depósito.

Al final de la etapa de operación se inactiva la condición de nivel, dejando drenar el relave

depositado bajo la cota final de operación.

**Análisis de sensibilidad modelo de flujo**

Se realizó un análisis de sensibilidad del modelo a la variación de la permeabilidad de la zona

no saturada y el almacenamiento de esta. A parte del caso base, se evalúan los escenarios E1 y

E2, los cuales aumentarían la infiltración y acortarían los tiempos de tránsito. Se simula un

tercer escenario E3 (cambio climático), que considera un aumento en la recarga como flujo

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 17 de 35

subterráneo entrante al modelo por aguas arriba debido a un posible aumento de la recarga

en la cuenca alta de Guamanga, donde ocurren las precipitaciones intensas.

Considerar que el escenario E3 reproduce los mismos resultados que el escenario base para los

tiempos simulados, debido a que la baja transmisividad del sistema retiene localmente los

efectos de un posible aumento de recarga en el límite este del modelo.

Tabla 3.2. Parámetros considerados para el escenario Base y análisis de sensibilidad.

|Escenario|K [m/d]|Sy [-]|
|---|---|---|
|Base|0.001|0.1|
|E1|**0.01**|0.1|
|E2|0.001|**0.01**|
|E3*|0.001|0.1|

_E3* corresponde a un aumento en el flujo de recarga por aguas arriba debido a los efectos de_

_cambio climático proyectados._

**Resultados del modelo de flujo**

El detalle de la calibración y validación del modelo de flujo se presentan en el informe Modelo

Conceptual y Numérico de Flujo Actualización 2023 (Aluvial, 2023).

Se presentan los resultados de las modelaciones de flujo asociadas a la infiltración desde el TSF

(Tabla 3.3, Figura 3.2, Figura 3.3, Figura 3.5, Figura 3.6, Figura 3.7, Figura 3.8, Figura 3.9), las

cuales constituyen la base para la modelación de transporte de solutos desde el tranque.

Dado que para el escenario base de flujo (K fuera de las zonas de embalse de 0.001 m/d) los

efectos de ascenso de niveles en los pozos de monitoreo no se perciben para el tiempo de

simulación evaluado, las simulaciones de transporte se realizan considerando las condiciones

de flujo asociadas al escenario E1, el cual corresponde a una condición más desfavorable al

considerar una permeabilidad K fuera de las zonas de embalse de 0.01 m/d.

Los resultados de las simulaciones indican que los flujos de entrada por la condición de borde

de nivel fijo aguas arriba y aguas abajo en el modelo, no varían a lo largo de la simulación. La

infiltración desde el tranque se traducen en un aumento del almacenamiento del sistema en el

tiempo. En cuanto al error de cierre del balance, este se encuentra en todo periodo bajo el 1%.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 18 de 35

Tabla 3.3. Resumen balance hídrico.

|Balance Hídrico|Escenario|Col3|Col4|Col5|
|---|---|---|---|---|
|**Balance Hídrico**|**Base**|**E1**|**E2**|**E3**|
|**Entradas [l/s]**|**0.019 l/s**(CB nivel<br>fijo) +**Infiltración**<br>**transiente desde el**<br>**tranque** (Figura 3.2)|**0.022 l/s**(CB nivel<br>fijo) +**Infiltración**<br>**transiente desde el**<br>**tranque** (Figura 3.3)|**0.019 l/s**(CB nivel<br>fijo) +**Infiltración**<br>**transiente desde el**<br>**tranque** (Figura 3.8)|**0.0226 l/s** (CB pozos<br>inyección) +**Infiltración**<br>**transiente desde el**<br>**tranque**(Figura 3.9)|
|**Salidas [l/s]**|**0.019 l/s** (CB nivel<br>fijo)|**0.022 l/s** (CB nivel<br>fijo)|**0.019 l/s** (CB nivel<br>fijo)|**0.019 l/s** (CB nivel fijo)|
|**Variación**<br>**almacenamiento**<br>**[l/s]**|**~ Infiltración**<br>**transiente desde el**<br>**tranque** (Figura 3.2)|**~ Infiltración**<br>**transiente desde el**<br>**tranque** (Figura 3.3)|**~ Infiltración**<br>**transiente desde el**<br>**tranque** (Figura 3.8)|**~ Infiltración transiente**<br>**desde el tranque** <br>(Figura 3.9) +** 0.0036**<br>**l/s** (diferencia CB)|
|**Error Balance [%]**|**< 0.4 %** (Figura 3.2)|**< 0.1 %** (Figura 3.3)|**< 0.3 %** (Figura 3.8)|**< 0.3 %** (Figura 3.9)|

Figura 3.2. Infiltración en el tiempo simulada desde el tranque para el escenario Base y error

balance (%). Infiltración en escala logarítmica. Fuente: Aluvial Consultores, 2023.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 19 de 35

Figura 3.3. Infiltración en el tiempo simulada desde el tranque para el escenario E1 y error

balance (%). Infiltración en escala logarítmica. Fuente: Aluvial Consultores, 2023.

Figura 3.4. Volumen infiltrado acumulado en el tiempo para el escenario E1. Infiltración en

escala logarítmica. Fuente: Aluvial Consultores.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 20 de 35

Figura 3.5. Niveles en el tiempo en pozos simulados durante la etapa de operación y cierre del

TSF para el escenario E1. Fuente: Aluvial Consultores.

Figura 3.6. Piezometría al final de la etapa de operación estimada para el escenario E1. Fuente:

Aluvial Consultores.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 21 de 35

Figura 3.7. Piezometría al final de la etapa de cierre estimada para el escenario E1. Fuente: Aluvial

Consultores.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 22 de 35

Figura 3.8. Infiltración en el tiempo simulada desde el tranque para el escenario E2 y error

balance (%). Infiltración en escala logarítmica. Fuente: Aluvial Consultores, 2023.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 23 de 35

Figura 3.9. Infiltración en el tiempo simulada desde el tranque para el escenario E3 y error

balance (%). Infiltración en escala logarítmica. Fuente: Aluvial Consultores, 2023.

# MODELO DE TRANSPORTE

El modelo de transporte se basa en el modelo de flujo existente, considerando la misma

geometría, zonificación, malla numérica de diferencias finitas, condiciones de borde de carga

en el tranque, y los resultados del campo de flujo calculado. Para modelar el transporte de

solutos se utilizó el software M3TDS (Modular 3D Transport and Dispersión Solver),

especializado en la simulación del transporte de solutos en medios prosos tridimensionales.

Este resuelve las ecuaciones de advección-dispersión para un campo de flujo proporcionado

por modelos de flujo tales como MODFLOW.

Se ha considerado un tiempo de simulación de 200 años, que comprende desde el inicio de la

etapa de operación del tranque de relaves y la etapa de cierre.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 24 de 35

Los parámetros de transporte del modelo fueron ajustados, y evaluada su sensibilidad, de

acuerdo a valores típicos de dispersión y difusión, y considerando condiciones conservadoras

para estimar afección a las aguas subterráneas.

Dado que no se cuenta con medidas de concentración del agua de relave (fuente), se realizan

supuestos sobre esta para el análisis del transporte y mezcla. Las simulaciones serán

actualizadas y complementadas posteriormente en función de las próximas analíticas de

laboratorio **.**

De igual forma, el modelo será recalibrado y validado en el tiempo en función de las

observaciones futuras de concentración y niveles levantadas.

### 4.1 PROCESOS DEL TRANSPORTE DE SOLUTOS

El modelo de transporte de solutos realizado se basa en las ecuaciones de advección

dispersión, considerando la propagación de los solutos bajo la influencia del flujo subterráneo

calculado con el modelo numérico de flujo. Se considera transporte conservativo. No se

consideran procesos de adsorción ni reactivos.

El transporte de solutos en medios porosos es gobernado principalmente por los siguientes

procesos y condiciones:

- **Advección:** transporte causado por el movimiento del agua a través del medio poroso. Este

depende de la velocidad del flujo, la cual es función de la conductividad hidráulica, el

gradiente hidráulico y la porosidad efectiva.

La velocidad del flujo es una de las magnitudes más importantes que determinan el alcance

del transporte advectivo, y queda determinada por el modelo de flujo.

- **Dispersión mecánicaa:** corresponde a la mezcla mecánica del soluto debido a diferencias en

las velocidades del flujo dentro del medio poroso, y se caracteriza por la Dispersividad (α),

el cual corresponde a un parámetro empírico de ajuste dependiente de la escala de

observación o simulación:

**Dispersividad longitudinal (α** **L** **):** abarca la dirección del flujo principal, con valores

típicos en la literatura que se encuentran en el rango de 10 - 100 m.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 25 de 35

Para modelaciones numéricas, la dispersividad generalmente no debe ser mucho menor

que el tamaño de las celdas para evitar problemas de subrepresentación de la

dispersión, considerándose apropiado un rango de 1/10 a 1/2 del tamaño de la celda

para asegurar que los efectos de la dispersión sean resueltos de manera adecuada.

**Dispersividad transversal (α** **T** **):** Perpendicular al flujo principal. Suele ser

significativamente menor que la longitudinal, adoptándose en general un orden de

magnitud de 0.1α L .

- **Difusión molecular:** el coeficiente de difusión molecular describe el transporte de moléculas

de soluto en el agua debido a un gradiente de concentración, independiente del movimiento

del agua. El valor del coeficiente de difusión puede variar en función del tamaño de las

moléculas de soluto y su interacción con el agua. En medios porosos el coeficiente efectivo

de difusión molecular D* es menor que en agua pura debido a la tortuosidad, indicándose

en términos generales para solutos comunes un rango de 1E-6 a 1E-4 m [2] /d.

- **Dispersión hidrodinámica total:** el coeficiente de dispersión total D incluye tanto la

dispersión mecánica como la difusión molecular, D = αv + D*, donde v corresponde a la

velocidad del flujo. En general la dispersión mecánica domina sobre la difusión molecular a

medida que aumenta la permeabilidad.

- **Reacciones químicas** : procesos de atenuación o transformación del soluto por adsorción

con el medio poroso o degradación por decaimiento del soluto. Procesos no considerados

en las modelaciones del presente estudio.

- **Condiciones de borde y fuente:** flujo de solutos generado por la recarga desde el tranque

asociada a la infiltración de agua con carga de solutos, y por la entrada del modelo por aguas

arriba.

- **Condición inicial:** corresponde a la condición inicial de concentraciones de solutos en el

sistema, previo a la etapa de operación y a la infiltración desde el tranque. Esta condición se

genera a partir de las observaciones en pozos de monitoreo.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 26 de 35

### 4.2 CONDICIONES DE CONTORNO, INICIALES Y PARÁMETROS HIDROGEOLÓGICOS ADOPTADOS EN EL MODELO TRANSPORTE

Lo parámetros hidráulicos y condiciones de contorno e iniciales de flujo corresponden a las

aplicadas en el modelo numérico de flujo descrito anteriormente, las que proporcionan la

información de salida del campo de flujo utilizado como entrada para M3TDS.

Dado que para el escenario base de flujo (K fuera de las zonas de embalse de 0.001 m/d) los

efectos de ascenso de niveles en los pozos de monitoreo no se perciben para el tiempo de

simulación evaluado, las simulaciones de transporte se realizan considerando las condiciones

de flujo asociadas al escenario E1, que considerar una permeabilidad K fuera de las zonas de

embalse de 0.01 m/d.

#### 4.2.1 Condición de carga de solutos en la fuente

Para evaluar los procesos de transporte y mezcla se toma como indicador el contenido de

sulfatos, soluto característico en aguas de relave, y que contrastaría con las aguas naturales. La

condición de concentración de la fuente se aplica en las mismas celdas en que se aplica la

condición de nivel de la laguna operacional, realizándose supuestos sobre la calidad del agua

del relave para el análisis de la magnitud del transporte y mezcla, condición que será validada

con los futuros análisis de agua del tranque.

Se simula un escenario base considerando una concentración de 2000 mg/l de sulfato para la

fuente. Posteriormente, dado que no se consideran procesos de adsorción ni reacción, y las

condiciones de flujo se mantienen, se supone una relación lineal de mezcla en relación a una

variación de la concentración de la fuente, proyectándose así los resultados para

concentraciones de 3000, 4000 y 5000 mg/l de sulfato a partir de la concentración relativa de

mezcla determinada para el caso base. Esto permite estimar la magnitud de mezcla para

diferentes concentraciones de la fuente.

#### 4.2.2 Condición inicial de concentración de solutos en el sistema

Con el objetivo de analizar netamente los efectos de las infiltraciones del tranque de relave en

las aguas subterráneas, se ha adoptado una concentración inicial de 700 mg/l de sulfatos en el

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 27 de 35

sistema antes del inicio de la operación, cifra que se considera representativa de la magnitud

característica del sistema de acuerdo al modelo conceptual, en particular en la serie de pozos

PB y el pozo PM-4 durante el último trimestre de 2023. Este supuesto robustece el análisis de

las proporciones de mezcla en relación a los efectos del tranque.

Se ha considerado un tiempo de simulación de 200 años, que comprende desde el inicio de la

etapa de operación del tranque de relaves y la etapa de cierre.

#### 4.2.3 Parámetros de transporte

Se ha adoptado un valor de dispersividad longitudinal (α L ) de 50 m y una dispersividad

transversal α T = 0.1α L = 5 m, en concordancia con los valores típicos reportados en la literatura

para escalas intermedias y regionales. Estos valores son consistentes con la discretización

espacial del modelo, donde el tamaño de las celdas varía entre 50 m y 150 m en la zona del

tranque, asegurando una adecuada representación de los procesos de dispersión sin introducir

errores significativos de dispersión numérica. Además, considerando que el tranque

dimensiones del orden de 2.5 km x 2 km y que los pozos de monitoreo se encuentran en el

entorno de 0.5 a 4 km en la ruta de exposición, estos valores permiten capturar de manera

efectiva el transporte de solutos en las escalas de interés.

El coeficiente de difusión molecular adoptado es de 1E-5 m2/d, valor razonable para sulfatos y

otros solutos típicos en el agua subterránea, considerando medios porosos tipo limos con un

factor de tortuosidad moderado. Este valor asegura que la contribución difusiva se represente

adecuadamente en zonas de baja velocidad de flujo.

Adicionalmente, se han considerado un valor de dispersividad longitudinal alternativo de 100

m para evaluar la sensibilidad del modelo, abarcando un escenario con mayor dispersión. Esto

permite analizar la incertidumbre asociada al transporte de solutos, evaluando el impacto en

la concentración de solutos en los pozos de monitoreo a diferentes distancias.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 28 de 35

### 4.3 RESULTADOS Y ANÁLISIS

A continuación, se realiza un análisis de la distribución espacial y evolución temporal de solutos

en el sistema.

El modelo de transporte en su condición base predice que los solutos en torno al tranque se

propagan a través del acuífero con una velocidad del orden de 0.1 m/d a medida que desciende

la infiltración verticalmente por la zona no saturada, luego la velocidad se reduce un orden de

magnitud al alcanzar el nivel saturado, disminuyendo gradualmente a un orden de magnitud a

medida que toma relevancia la componente horizontal de la velocidad hacia los extremos del

domo de recarga

Se estima que las concentraciones de solutos se distribuyen de manera relativamente uniforme

en el acuífero de forma radial en torno al tranque, alcanzando la concentración máxima bajo el

tranque durante la etapa de operación, extendiéndose la pluma por dispersión

aproximadamente en torno a los 350 - 450 m más allá de la cubeta del tranque al fin de la etapa

de operación, y en promedio propagándose del orden de 100 m cada 5 años en torno al

tranque.

Con el paso del tiempo, las concentraciones de solutos en el acuífero aumentan gradualmente,

alcanzándose los valores máximos al final de la etapa de cierre. La concentración tiende a la

estabilización en los pozos de la serie PB frente al tranque al final del periodo de simulación,

indicando que la dispersión y difusión están equilibrando la propagación del soluto.

La mezcla se registra en torno a los 2 años luego de finalizar la etapa de operación en los pozos

PB-1 a 5, siendo el pozo PB-2, ubicado aproximadamente a 0.5 km del tranque el primero en

registrar mezcla (Figura 4.2). La mayor proporción de mezcla se estima en los pozos PB-2, PB-3

y PB-1. Se observa una acumulación de solutos en los pozos frente al tranque, lo que se debería

a la existencia de zonas de estancamiento o muy baja velocidad. En torno a los 50 años desde

el inicio de la operación se estima que la pluma se habría propagado aproximadamente a 0.85

m del tranque, a aproximadamente a 1.35 km del tranque en torno a los 75 años, y

aproximadamente a 1.75 km a los 120 años.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 29 de 35

Para el análisis de magnitud del transporte y mezcla, se ha simulado un escenario base

considerando una concentración de 2000 mg/l de sulfato para la fuente (Figura 4.1).

Posteriormente, dado que no se consideran procesos de adsorción ni reacción, y las

condiciones de flujo se mantienen, se supone una relación lineal de mezcla en relación a una

variación de la concentración de la fuente, proyectándose así los resultados para

concentraciones de 3000, 4000 y 5000 mg/l de sulfato a partir de la concentración relativa de

mezcla determinada a partir del caso base. Esto permite estimar la magnitud de mezcla para

diferentes concentraciones de la fuente (Figura 4.3). Como es de esperar, se observa que a

medida que aumenta la concentración en la fuente se alcanza antes el aumento del 25% de la

concentración en los pozos respecto a su condición de línea base, correspondiente al umbral

establecido en el plan de monitoreo de aguas subterráneas.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 30 de 35

Figura 4.1. Distribución espacial de la concentración en el tiempo estimada. Caso base, 2000

mg/l de sulfato en la fuente.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 31 de 35

Figura 4.2. Concentración relativa estimada en el tiempo en los pozos de monitoreo. Fuente:

Aluvial Consultores.

Figura 4.3. Concentración en el tiempo en los pozos de monitoreo para concentraciones de 2000,

3000, 4000, 5000 mg/l de sulfato en la fuente. Fuente: Aluvial Consultores.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 32 de 35

**Sensibilidad del modelo**

Al considerar una dispersividad longitudinal de 100 m se observa que la propagación de la

pluma es similar en el tiempo, comenzando un par de años antes la mezcla con el agua de la

fuente. La magnitud de la mezcla es similar para ambas dispersividades, con una ligera

disminución al considerar la dispersividad longitudinal de 100 m.

De acuerdo a esto el modelo se considera que el modelo es robusto frente a un aumento del

parámetro se dispersividad, lo que permite estimar de forma conservadora la propagación de

solutos.

Figura 4.4. Concentración relativa estimada en el tiempo en los pozos de monitoreo considerando

una dispersividad longitudinal de 100 m. Fuente: Aluvial Consultores.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 33 de 35

# CONCLUSIONES

El modelo de transporte realizado, basado en el modelo hidrogeológico conceptual y numérico

de flujo existente (Aluvial, 2023), establece una base para simular el transporte de solutos en

el sistema hidrogeológico. Se ha considerado un tiempo de simulación de 200 años, que

comprende desde el inicio de la etapa de operación del tranque de relaves y la etapa de cierre.

Si bien las simulaciones se enfocan en los posibles efectos del tranque de relaves en las aguas

subterráneas, el área del modelo abarca la totalidad del modelo de flujo existente.

Dado que para el escenario base de flujo (K fuera de las zonas de embalse de 0.001 m/d) los

efectos de ascenso de niveles en los pozos de monitoreo no se perciben para el tiempo de

simulación evaluado, las simulaciones de transporte se realizan considerando las condiciones

de flujo asociadas al escenario E1, el cual considerar una permeabilidad K fuera de las zonas de

embalse de 0.01 m/d.

Se han considerado procesos advectivos, dispersivos y de difusión, adoptando un valore de

dispersividad longitudinal de 50 m (y transversal de 0.1 veces la longitudinal) y un coeficiente

de difusión molecular de 1×10−5 m/d, valores consistentes con la literatura y escala del

modelo, y que permiten capturar las dinámicas principales del transporte. Incluir procesos

como adsorción o reacciones químicas podría reducir la movilidad de sulfatos de solutos no

conservativos.

Se ha utilizado una concentración inicial de sulfatos de 700 mg/l como referencia

representativa para el análisis de transporte y mezcla.

El transporte de solutos ocurre inicialmente con una velocidad del orden de 0.1 m/d en la zona

no saturada, que disminuye significativamente a uno y dos órdenes de magnitud al alcanzar el

nivel saturado.

La pluma de solutos se extiende radialmente desde el tranque, alcanzando hasta 450 m al final

de la etapa de operación. Posteriormente, la propagación horizontal promedio se estima del

orden de 100 m cada 5 años.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 34 de 35

Las zonas de muy baja velocidad de flujo o estancamiento, generadas por ejemplo al centro del

tranque y al frente de este en los pozos de la serie PB (1-5), actuarían como áreas de

acumulación de solutos al considerar una dispersividad longitudinal de 50 m. La acumulación

se reduce al considerar una dispersividad longitudinal de 100 m.

Se estima que la pluma alcanzaría distancias en torno a los 0.5 km a los 22 años de inicio de la

operación, y distancias de entre 0.85 y 1.75 km en plazos que varían entre los 50 y 120 años.

Hacia el final de la etapa de cierre del tranque, las concentraciones tienden a estabilizarse en

los pozos de monitoreo más cercanos (PB-1 a 5).

Se han realizado supuestos sobre la calidad del agua del relave para el análisis de la magnitud

del transporte y mezcla, condición que será validada con los futuros análisis de agua del

tranque. Además, el modelo será recalibrado y validado en el tiempo en función de las

observaciones futuras de concentración y niveles levantadas en los pozos de monitoreo. Esto

permitirá reducir la incertidumbre en los resultados y validar las proyecciones actuales.

Se han evaluado distintas concentraciones de la fuente, comenzando con un nivel base de 2000

mg/l de sulfato.

Escenarios con mayores concentraciones iniciales en la fuente (3000, 4000 y 5000 mg/l)

confirmaron que el umbral de aumento del 25% en la concentración en los pozos monitoreados

se alcanza más rápidamente.

El modelo mostró robustez frente a variaciones en parámetros como la dispersividad

longitudinal y la concentración de la fuente, lo que permite estimar de forma conservadora la

magnitud de la propagación de solutos.

_A_ luvial Consultores - Pedro de Valdivia N°1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvialconsultores.cl - info@aluvialconsultores.cl

Página 35 de 35

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3.1.: Cotas de la laguna operacional proyectadas en plan de depositación .**

| Año | Cota Laguna<br>Operacional<br>[msnm] |
| --- | --- |
| 1 | 735.78 |
| 5 | 755.78 |
| 10 | 767.20 |
| 20 | 786.32 |

**Tabla 3.2.: Parámetros considerados para el escenario Base y análisis de sensibilidad.**

| Escenario | K [m/d] | Sy [-] |
| --- | --- | --- |
| Base | 0.001 | 0.1 |
| E1 | **0.01** | 0.1 |
| E2 | 0.001 | **0.01** |
| E3* | 0.001 | 0.1 |

**Tabla 3.3.: Resumen balance hídrico.**

| Balance Hídrico | Escenario | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Balance Hídrico** | **Base** | **E1** | **E2** | **E3** |
| **Entradas [l/s]** | **0.019 l/s**(CB nivel<br>fijo) +**Infiltración**<br>**transiente desde el**<br>**tranque** (Figura 3.2) | **0.022 l/s**(CB nivel<br>fijo) +**Infiltración**<br>**transiente desde el**<br>**tranque** (Figura 3.3) | **0.019 l/s**(CB nivel<br>fijo) +**Infiltración**<br>**transiente desde el**<br>**tranque** (Figura 3.8) | **0.0226 l/s** (CB pozos<br>inyección) +**Infiltración**<br>**transiente desde el**<br>**tranque**(Figura 3.9) |
| **Salidas [l/s]** | **0.019 l/s** (CB nivel<br>fijo) | **0.022 l/s** (CB nivel<br>fijo) | **0.019 l/s** (CB nivel<br>fijo) | **0.019 l/s** (CB nivel fijo) |
| **Variación**<br>**almacenamiento**<br>**[l/s]** | **~ Infiltración**<br>**transiente desde el**<br>**tranque** (Figura 3.2) | **~ Infiltración**<br>**transiente desde el**<br>**tranque** (Figura 3.3) | **~ Infiltración**<br>**transiente desde el**<br>**tranque** (Figura 3.8) | **~ Infiltración transiente**<br>**desde el tranque** <br>(Figura 3.9) +** 0.0036**<br>**l/s** (diferencia CB) |
| **Error Balance [%]** | **< 0.4 %** (Figura 3.2) | **< 0.1 %** (Figura 3.3) | **< 0.3 %** (Figura 3.8) | **< 0.3 %** (Figura 3.9) |
