---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: report
pages: 203
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO C2-18
-->

# ANEXO C2-18

## MODELACIÓN DE CALIDAD DEL AIRE

#### _Cliente_

### Evaluación del Impacto en Calidad del Aire del Proyecto “ Proyecto de modificación para producir celulosa cruda en Planta Laja ”

**PREPARÓ:**

**AIR QUALITY & ODOR MANAGEMENT**

**SPIN OFF DE LA PONTIFICIA UNIVERSIDAD CATÓLICA DE VALPARAÍSO**

**Septiembre 2023**

|Fecha|CONTROL DE<br>REVISIÓN|Nombre|Profesión|Función|Firma|
|---|---|---|---|---|---|
|Septiembre<br>2023|Rev0|Camila Piñones<br>Vásquez|Ingeniero<br>Civil<br>Bioquímico|Revisión.||
|Septiembre<br>2023|Rev0|Jorge Dumont<br>Ortiz|Ingeniero<br>Civil<br>Bioquímico|Ingeniero<br>de<br>proyecto<br>y <br>modelador.||
|Septiembre<br>2023|Rev0|Fabio Carrera<br>Chapela|Ingeniero<br>Químico,<br>Dr.<br>Ingeniería<br>Química|Director Técnico||

**CONFIDENCIALIDAD**

La información contenida en este documento es de carácter confidencial y exclusivo para el

individuo o entidad a la que van dirigidas. De manera que, si usted no es el destinario

individualizado y por error recibiera este documento, le agradeceremos notificar al

remitente y borrar este documento junto con todos sus archivos digitales.

2

#### Resumen Ejecutivo

El proyecto de CMPC Pulp SpA consiste en la modificación de maquina papelera,

modificación de máquina secadora, deshabilitación de planta de blanqueo y sus

instalaciones auxiliares, construcción y operación de planta tall oil, construcción y operación

de área de preparación de maderas, modificación de áreas de fibra y digestor, mejora en

sistema de recolección de gases diluidos y modificaciones sistema de recolección de aguas

lluvia.

La modelación de las emisiones atmosféricas de MP 10, MP 2,5, MPS, NO 2, SO 2, CO, y TRS del

proyecto, se realizó siguiendo las recomendaciones de la guía del SEIA, utilizando para ello

el modelo CALPUFF y empleando como base para la modelación, la meteorología generada

por el modelo WRF para tres años (2020 a 2022).

Para evaluar el impacto de las emisiones de MP 10, MP 2,5, NO 2, SO 2 y CO, se empleó la normativa

vigente para calidad del aire primaria y en el caso de SO 2, se consideró también la norma de

calidad secundaria.

Dado que en Chile no existen normas primarias para MPS y TRS, se consideró en el caso del

MPS a la norma para material particulado sedimentable establecida en la Confederación Suiza

en 1985 (Ordinance on Air pollution. Swiss Federal Council) y en el caso de TRS, a la Resolución

1.541 (2013) de Colombia.

De acuerdo a los estadísticos analizados, se supera la concentración definida por normativa

para el MP 2,5 y la concentración horaria de TRS en la estación San Rosendo (ver Tabla 1). El

resto de los estadísticos para los gases y material particulado analizado, cumplen con los

límites establecidos.

**Tabla 1. Estadísticos con saturación de la línea base.**

|Estación|Estadístico|Línea base en<br>estación|Límite<br>normativo|% normativa|
|---|---|---|---|---|
|Laja|Promedio anual MP2,5 (μg/m3)|22|20|110%|
|Laja|Percentil 98 concentración 24 horas MP2,5 (μg/m3)|89|50|178%|
|San<br>Rosendo|Promedio anual MP2,5 (μg/m3)|26|20|130%|
|San<br>Rosendo|Percentil 98 concentración 24 horas MP2,5 (μg/m3)|101|50|202%|
|San<br>Rosendo|Concentraciones 1h TRS (μg/m3)|61|40|153%|

**Fuente** : antecedentes informe calidad del aire.

Para evaluar el potencial impacto asociado al aporte del proyecto en aquellos estadísticos

que presentan saturación, se estima si es significativo o no, de acuerdo a los niveles de
impacto significativo (SIL) definidos en el informe “ _EVALUACIÓN SIGNIFICANCIA DEL_

_IMPACTO DE LAS EMISIONES DE UN PROYECTO O ACTIVIDAD EN ZONAS SATURADAS EN EL_

_MARCO DEL SEIA_ ”, 2022 (ver sección 6.3 Nivel de impacto significativo).

3

Dado que no se establece un SIL para TRS, que el porcentaje de los SIL respecto a los valores

límite normativos para el resto de los contaminantes definidos están comprendidos entre

un 1- 4,9 %, y que solo hay saturación de la concentración de 1 h de TRS, se considera un

escenario más restrictivo y se estima el SIL para el TRS en un 1% del valor de la norma

homologada (ver sección 6.3 Nivel de impacto significativo).

La estación Laja posee un radio de representatividad de 2 km, dentro de los cuales se

encuentran todos los receptores. Por ello, entrega la línea base en los receptores.

A 21-04-2023, se identificó que hay dos proyectos en fase de construcción, correspondientes

al proyecto “Subestación La señoraza 220/66 kV” de Sociedad Austral de Transmisión Troncal,

y el proyecto “Nueva conexión y ampliación S/E Celulosa Laja” de CMPC Pulp SpA. Para el

aporte de los proyectos se consideró el peor escenario de mayor aporte.

Cabe mencionar que, para efectos de la estimación de la concentración total, se considera

al aporte en la estación Laja de los proyectos colindantes como el aporte de los proyectos

en los receptores estudio.

Se modelaron 3 años y se evaluó para cada receptor, el periodo en el cual reciben la mayorconcentración y/o tasa de deposición (ver APENDICE 6 Resultados Modelación 3 años)

De acuerdo con el análisis presentado en la sección 4.3, los escenarios de mayor emisión se

corresponden con:

 - **Escenario 1** : Fase de construcción entre los meses 13 al 21 e Incremento emisión

Fase operación meses 16 al 24. La línea base presenta el aporte de la operación

actual de la planta, por lo que, durante la operación proyectada, se evalúa el

incremento de la tasa de emisión de los gases y material particulado.

 - **Escenario 2** : Fase de operación proyectada (1 año operación).

 - **Escenario 3** : Fase de cierre del proyecto (1 año).

##### Escenario 1

De acuerdo al análisis de los estadísticos presentados en la Tabla 2 y Tabla 3, se cumple con

los límites definidos por normativa para MP 10, MPS, NO 2, SO 2, CO y la concentración diaria de

TRS.

El análisis de la significancia del aporte del proyecto a la línea base que se presenta en la Tabla

2 y Tabla 3, indica que el aporte del proyecto en el escenario 1 no es significativo para los

estadísticos de MP 2,5 y de TRS horario, y, por lo tanto, el proyecto no genera impactos

significativos sobre la salud de la población.

4

**Tabla 2. Tabla resumen estadísticos** **-** **Escenario 1 parte 1.**

|Ítem|MP *<br>10|Col3|MP **<br>2.5|Col5|MPS*|NO *<br>2|Col8|SO *<br>2|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Ítem**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil**<br>**98 diario**<br>**(μg/m3N)**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil**<br>**98 diario**<br>**(μg/m3N)**|**Tasa de**<br>**deposición**<br>**promedio**<br>**anual**<br>**(mg/m2N/d)**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil**<br>**99**<br>**horario**<br>**(μg/m3N)**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil 99**<br>**diario(μg/m3N)**|**Percentil 98,5**<br>**horario(μg/m3N)**|**Percentil**<br>**99,7**<br>**diario**<br>**(μg/m3N)**|**Percentil**<br>**99,73**<br>**horario**<br>**(μg/m3N)**|
|**Límite**<br>**normativo**|**50**|**130**|**--**|**--**|**200**|**100**|**400**|**60**|**150**|**350**|**260**|**700**|
|**SIL**|**--**|**--**|**0,33**|**1,71**|**--**|**--**|**--**|**--**|**--**|**--**|**--**|**--**|
|Receptor 1|**30**|**71**|**0,08**|**0,45**|**0 **|**9 **|**58**|**1 **|**5 **|**7 **|**8 **|**18**|
|Receptor 2|**30**|**71**|**0,19**|**0,72**|**0 **|**9 **|**55**|**1 **|**6 **|**8 **|**9 **|**18**|
|Receptor 3|**30**|**70**|**0,04**|**0,28**|**0 **|**9 **|**57**|**1 **|**5 **|**6 **|**8 **|**15**|
|Receptor 4|**30**|**71**|**0,10**|**0,55**|**0 **|**9 **|**54**|**1 **|**5 **|**7 **|**8 **|**17**|
|Receptor 5|**30**|**71**|**0,25**|**1,10**|**0 **|**9 **|**58**|**1 **|**6 **|**9 **|**9 **|**20**|
|Receptor 6|**30**|**71**|**0,19**|**0,76**|**0 **|**9 **|**62**|**1 **|**6 **|**8 **|**9 **|**19**|
|Estación<br>Laja|**30**|**71**|**0,06**|**0,42**|**0 **|**9 **|**53**|**1 **|**5 **|**7 **|**7 **|**16**|
|Estación<br>San<br>Rosendo|**37**|**103**|**0,16**|**0,55**|**0 **|**11**|**50**|**3 **|**8 **|**10**|**11**|**19**|

 - Línea base, aporte proyecto y aporte proyectos con RCA. La coloración corresponde a: **cumplimiento** o **incumplimiento** .

** Aporte del proyecto. La coloración corresponde a: **no significativo** o **significativo** .

**Tabla 3. Tabla resumen estadísticos** **-** **Escenario 1 parte 2.**

|Ítem|CO*|Col3|TRS*|Col5|
|---|---|---|---|---|
|**Ítem**|**Percentil 99 horario (mg/m3N)**|**Percentil 99 8 horas (mg/m3N)**|**Concentración diaria (μg/m3N)**|**Concentración horaria (μg/m3N)**|
|**Límite normativo**|**30**|**10**|**7 **|**40**|
|**SIL**|**--**|**--**|**--**|**0,4**|
|Receptor 1|**5 **|**3 **|**4 **|**20**|
|Receptor 2|**5 **|**3 **|**4 **|**20**|
|Receptor 3|**5 **|**3 **|**4 **|**20**|
|Receptor 4|**5 **|**3 **|**4 **|**20**|
|Receptor 5|**5 **|**3 **|**4 **|**20**|
|Receptor 6|**5 **|**3 **|**4 **|**20**|

5

|Ítem|CO*|Col3|TRS*|Col5|
|---|---|---|---|---|
|**Ítem**|**Percentil 99 horario (mg/m3N)**|**Percentil 99 8 horas (mg/m3N)**|**Concentración diaria (μg/m3N)**|**Concentración horaria (μg/m3N)**|
|Estación Laja|**5 **|**3 **|**4 **|**20**|
|Estación San Rosendo|**6 **|**4 **|**4 **|**0,11****|

 - Línea base, aporte proyecto y aporte proyectos con RCA. La coloración corresponde a: **cumplimiento** o **incumplimiento** .

** Aporte del proyecto. La coloración corresponde a: **no significativo** o **significativo** .

##### Escenario 2

En el escenario 2 se genera el cumplimiento de los mismos estadísticos que en el escenario 1, tal como se puede apreciar en la Tabla 4 y la

Tabla 5.

El análisis de la significancia del aporte del proyecto a la línea base que se presenta en la Tabla 4 y la Tabla 5, indica que el aporte del

proyecto en el escenario 2 no es significativo para los estadísticos de MP 2,5 y de TRS horario, y, por tanto, el proyecto no genera impactos

significativos sobre la salud de la población

**Tabla 4. Tabla resumen estadísticos** **-** **Escenario 2 parte 1.**

|Ítem|MP *<br>10|Col3|MP **<br>2.5|Col5|MPS*|NO *<br>2|Col8|SO *<br>2|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Ítem**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil**<br>**98 diario**<br>**(μg/m3N)**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil**<br>**98 diario**<br>**(μg/m3N)**|**Tasa de**<br>**deposición**<br>**promedio**<br>**anual**<br>**(mg/m2N/d)**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil**<br>**99**<br>**horario**<br>**(μg/m3N)**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil 99**<br>**diario(μg/m3N)**|**Percentil 98,5**<br>**horario(μg/m3N)**|**Percentil**<br>**99,7**<br>**diario**<br>**(μg/m3N)**|**Percentil**<br>**99,73**<br>**horario**<br>**(μg/m3N)**|
|**Límite**<br>**normativo**|**50**|**130**|**20**|**50**|**200**|**100**|**400**|**60**|**150**|**350**|**260**|**700**|
|**SIL**|**--**|**--**|**0,33**|**1,71**|**--**|**--**|**--**|**--**|**--**|**--**|**--**|**--**|
|Receptor 1|**30**|**71**|**0,10**|**0,45**|**0 **|**9 **|**57**|**1 **|**5 **|**7 **|**8 **|**18**|
|Receptor 2|**30**|**71**|**0,25**|**0,78**|**0 **|**9 **|**55**|**1 **|**6 **|**8 **|**9 **|**18**|
|Receptor 3|**30**|**70**|**0,05**|**0,28**|**0 **|**9 **|**57**|**1 **|**5 **|**6 **|**8 **|**16**|
|Receptor 4|**30**|**71**|**0,12**|**0,57**|**0 **|**9 **|**54**|**1 **|**5 **|**8 **|**8 **|**17**|
|Receptor 5|**30**|**71**|**0,32**|**1,09**|**0 **|**10**|**58**|**1 **|**6 **|**9 **|**9 **|**20**|
|Receptor 6|**30**|**71**|**0,24**|**0,70**|**0 **|**9 **|**60**|**1 **|**6 **|**8 **|**9 **|**19**|

6

|Ítem|MP *<br>10|Col3|MP **<br>2.5|Col5|MPS*|NO *<br>2|Col8|SO *<br>2|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Ítem**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil**<br>**98 diario**<br>**(μg/m3N)**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil**<br>**98 diario**<br>**(μg/m3N)**|**Tasa de**<br>**deposición**<br>**promedio**<br>**anual**<br>**(mg/m2N/d)**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil**<br>**99**<br>**horario**<br>**(μg/m3N)**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil 99**<br>**diario(μg/m3N)**|**Percentil 98,5**<br>**horario(μg/m3N)**|**Percentil**<br>**99,7**<br>**diario**<br>**(μg/m3N)**|**Percentil**<br>**99,73**<br>**horario**<br>**(μg/m3N)**|
|Estación<br>Laja|**30**|**71**|**0,08**|**0,43**|**0 **|**9 **|**53**|**1 **|**5 **|**7 **|**7 **|**16**|
|Estación<br>San<br>Rosendo|**37**|**103**|**0,22**|**0,56**|**0 **|**11**|**50**|**3 **|**8 **|**10**|**11**|**20**|

 - Línea base, aporte proyecto y aporte proyectos con RCA. La coloración corresponde a: **cumplimiento** o **incumplimiento** .

** Aporte del proyecto. La coloración corresponde a: **no significativo** o **significativo** .

**Tabla 5. Tabla resumen estadísticos** **-** **Escenario 2 parte 2.**

|Ítem|CO*|Col3|TRS*|Col5|
|---|---|---|---|---|
|**Ítem**|**Percentil 99 horario (mg/m3N)**|**Percentil 99 8 horas (mg/m3N)**|**Concentración diaria (μg/m3N)**|**Concentración horaria (μg/m3N)**|
|**Límite normativo**|**30**|**10**|**7 **|**40**|
|**SIL**|**--**|**--**|**--**|**0,4**|
|Receptor 1*|**5 **|**3 **|**4 **|**20**|
|Receptor 2*|**5 **|**3 **|**4 **|**20**|
|Receptor 3*|**5 **|**3 **|**4 **|**20**|
|Receptor 4*|**5 **|**3 **|**4 **|**20**|
|Receptor 5*|**5 **|**3 **|**4 **|**20**|
|Receptor 6*|**5 **|**3 **|**4 **|**20**|
|Estación Laja*|**5 **|**3 **|**4 **|**20**|
|Estación San Rosendo*|**6 **|**4 **|**4 **|**0,11****|

 - Línea base, aporte proyecto y aporte proyectos con RCA. La coloración corresponde a: **cumplimiento** o **incumplimiento** .

** Aporte del proyecto. La coloración corresponde a: **no significativo** o **significativo** .

##### Escenario 3

En el escenario 3 se genera el cumplimiento de los mismos estadísticos que en el escenario 1, tal como se puede apreciar en la Tabla 6 y la

Tabla 7.

7

El análisis de la significancia del aporte del proyecto a la línea base que se presenta en la Tabla 6, indica que el aporte del proyecto en el

escenario 3 no es significativo para los estadísticos de MP 2,5, y, por tanto, el proyecto no genera impactos significativos sobre la salud de la

población

**Tabla 6. Tabla resumen estadísticos** **-** **Escenario 3 parte 1.**

|Ítem|MP *<br>10|Col3|MP **<br>2.5|Col5|MPS*|NO *<br>2|Col8|SO *<br>2|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Ítem**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil**<br>**98 diario**<br>**(μg/m3N)**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil**<br>**98 diario**<br>**(μg/m3N)**|**Tasa de**<br>**deposición**<br>**promedio**<br>**anual**<br>**(mg/m2N/d)**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil**<br>**99**<br>**horario**<br>**(μg/m3N)**|**Promedio**<br>**anual**<br>**(μg/m3N)**|**Percentil 99**<br>**diario(μg/m3N)**|**Percentil 98,5**<br>**horario(μg/m3N)**|**Percentil**<br>**99,7**<br>**diario**<br>**(μg/m3N)**|**Percentil**<br>**99,73**<br>**horario**<br>**(μg/m3N)**|
|**Límite**<br>**normativo**|**50**|**130**|**20**|**50**|**200**|**100**|**400**|**60**|**150**|**350**|**260**|**700**|
|**SIL**|**--**|**--**|**0,33**|**1,71**|**--**|**--**|**--**|**--**|**--**|**--**|**--**|**--**|
|Receptor 1|**30**|**77**|**0,09**|**0,86**|**0 **|**9 **|**61**|**1 **|**4 **|**5 **|**6 **|**13**|
|Receptor 2|**30**|**71**|**0,04**|**0,20**|**0 **|**9 **|**54**|**1 **|**4 **|**5 **|**6 **|**13**|
|Receptor 3|**30**|**72**|**0,03**|**0,30**|**0 **|**9 **|**57**|**1 **|**4 **|**5 **|**6 **|**13**|
|Receptor 4|**30**|**71**|**0,02**|**0,09**|**0 **|**9 **|**52**|**1 **|**4 **|**5 **|**6 **|**13**|
|Receptor 5|**31**|**78**|**0,15**|**1,00**|**0 **|**9 **|**59**|**1 **|**4 **|**5 **|**6 **|**13**|
|Receptor 6|**31**|**84**|**0,14**|**1,49**|**0 **|**9 **|**63**|**1 **|**4 **|**5 **|**6 **|**13**|
|Estación<br>Laja|**30**|**70**|**0,01**|**0,03**|**0 **|**9 **|**51**|**1 **|**4 **|**5 **|**6 **|**13**|
|Estación<br>San<br>Rosendo|**37**|**102**|**0,00**|**0,02**|**0 **|**11**|**48**|**3 **|**7 **|**8 **|**9 **|**17**|

 - Línea base, aporte proyecto y aporte proyectos con RCA. La coloración corresponde a: **cumplimiento** o **incumplimiento** .

** Aporte del proyecto. La coloración corresponde a: **no significativo** o **significativo** .

**Tabla 7. Tabla resumen estadísticos** **-** **Escenario 3 parte 2.**

|Ítem|CO*|Col3|
|---|---|---|
|**Ítem**|**Percentil 99 horario (mg/m3N)**|**Percentil 99 8 horas (mg/m3N)**|
|**Límite normativo**|**30**|**10**|
|**SIL**|**--**|**--**|
|Receptor 1*|**5 **|**3 **|
|Receptor 2*|**5 **|**3 **|
|Receptor 3*|**5 **|**3 **|
|Receptor 4*|**5 **|**3 **|
|Receptor 5*|**5 **|**3 **|

8

|Ítem|CO*|Col3|
|---|---|---|
|**Ítem**|**Percentil 99 horario (mg/m3N)**|**Percentil 99 8 horas (mg/m3N)**|
|Receptor 6*|**5 **|**3 **|
|Estación Laja*|**5 **|**3 **|
|Estación San Rosendo*|**6 **|**4 **|

 - Línea base, aporte proyecto y aporte proyectos con RCA. La coloración corresponde a: **cumplimiento** o **incumplimiento** .

##### Conclusiones

Del presente informe del proyecto “ _Proyecto de modificación para producir_ _celulosa_ _cruda en Planta Laja_ ”, se obtienen las siguientes

conclusiones:

 - El análisis de la concentración total y tasa de deposición total en los receptores discretos y las estaciones de monitoreo para

los estadísticos definidos en normativa para MP 10, MPS, NO 2, SO 2 y CO, permite estimar que no se supera la normativa y que,

por tanto, no hay afectación para los 3 años meteorológicos, para el escenario 1, el escenario 2 y el escenario 3.

 - El análisis de la concentración total en los receptores discretos y las estaciones de monitoreo para el estadístico definido en

normativa para TRS (diario), permite estimar que no se supera la normativa y que, por tanto, no hay afectación para los 3 años

meteorológicos, para el escenario 1 y el escenario 2.

 - El análisis del nivel de significancia del aporte del proyecto para los estadísticos promedio anual y percentil 98 de la

concentración diaria de MP 2,5, indica que el aporte del proyecto no es significativo en los niveles de calidad del aire en el área

de influencia del proyecto para el periodo de 3 años meteorológicos evaluados, por lo que se descarta que el proyecto pueda

producir un impacto significativo en la calidad del aire de la zona y por tanto en la salud de la población, en el escenario 1,

escenario 2 y escenario 3.

 - El análisis del nivel de significancia para el estadístico concentración horaria de TRS, indica que el aporte del proyecto no es

significativo en los niveles de calidad del aire en el área de influencia del proyecto para el periodo de 3 años meteorológicos

evaluados, por lo que se descarta que el proyecto pueda producir un impacto significativo en la calidad del aire de la zona y por

tanto en la salud de la población, en el escenario 1 y escenario 2.

Bajo las condiciones evaluadas, se puede concluir que el proyecto y sus diferentes etapas, no generan un impacto significativo en la

calidad del aire de la zona o en la salud de la población.

9

#### Índice

Resumen Ejecutivo ................................................................................................................. 3

Escenario 1 .......................................................................................................................... 4

Escenario 2 .......................................................................................................................... 6

Escenario 3 .......................................................................................................................... 7

Conclusiones ....................................................................................................................... 9

1. Introducción ................................................................................................................. 26

1.1. Objetivo .................................................................................................................. 27

2. Dominio de simulación ................................................................................................. 28

3. Tipología del Proyecto .................................................................................................. 30

4. Inventario de Emisiones ............................................................................................... 31

4.1. Fuentes de Emisión ................................................................................................ 34

4.1.1. Fase de Construcción ...................................................................................... 34

4.1.2. Fase de Operación .......................................................................................... 34

4.1.3. Fase de Cierre ................................................................................................. 35

4.2. Resultados Inventario de Emisión ......................................................................... 36

4.2.1. Fase de Construcción ...................................................................................... 36

4.2.2. Fase de Operación .......................................................................................... 37

4.2.3. Fase de Cierre ................................................................................................. 39

4.3. Escenarios .............................................................................................................. 40

4.3.1. Escenario 1 ...................................................................................................... 40

4.3.2. Escenario 2 ...................................................................................................... 43

4.3.3. Escenario 3 ...................................................................................................... 43

4.4. Nivel de Actividad de los escenarios ...................................................................... 44

4.4.1. Escenario 1 ...................................................................................................... 44

4.4.2. Escenario 2 ...................................................................................................... 50

4.4.3. Escenario 3 ...................................................................................................... 53

4.4.4. Factor de Variación de la emisión .................................................................. 56

5. Análisis meteorológico ................................................................................................. 60

5.1. Selección de la estación meteorológica de referencia .......................................... 60

10

5.2. Resultados análisis de incertidumbre .................................................................... 61

6. Modelación de Calidad del Aire.................................................................................... 63

6.1. Selección de la Normativa ..................................................................................... 63

6.2. Línea base de calidad del aire ................................................................................ 66

6.3. Nivel de impacto significativo ................................................................................ 69

6.4. Selección del Modelo y su Procesamiento ............................................................ 69

6.5. Aporte de otros proyectos con RCA favorable ...................................................... 69

6.6. Receptores ............................................................................................................. 71

6.7. Modelación de Impactos por Emisión de material particulado y gases ................ 74

6.7.1. Concentración total estimada - Escenario 1 .................................................. 75

6.7.2. Concentración total estimada - Escenario 2 .................................................. 88

6.7.3. Concentración total estimada - Escenario 3 ................................................ 101

7. Conclusiones ............................................................................................................... 113

8. Anexos ........................................................................................................................ 114

9. Apéndices ................................................................................................................... 115

9.1. APENDICE 1 - Archivos de la Modelación ........................................................... 115

9.2. APENDICE 2 - Estimación de emisión de TRS ...................................................... 116

9.3. APENDICE 3 - Selección de la estación meteorológica de referencia ................. 118

9.4. APENDICE 4 - Análisis meteorológico de Datos Observados y Modelados ........ 120

9.4.1. Meteorología 2020 ....................................................................................... 121

a. Viento ................................................................................................................... 121

b. Velocidad del Viento ........................................................................................ 123

c. Dirección del Viento ............................................................................................. 126

d. Temperatura ..................................................................................................... 129

e. Humedad relativa ............................................................................................. 132

f. Análisis de la incertidumbre ................................................................................ 135

9.4.2. Meteorología 2021 ....................................................................................... 135

a. Viento ................................................................................................................... 135

b. Velocidad del Viento ........................................................................................ 137

c. Dirección del Viento ............................................................................................. 140

11

d. Temperatura ..................................................................................................... 143

e. Humedad relativa ............................................................................................. 146

f. Análisis de la incertidumbre ................................................................................ 149

9.4.3. Meteorología 2022 ....................................................................................... 149

a. Viento ................................................................................................................... 149

b. Velocidad del Viento ........................................................................................ 151

c. Dirección del Viento ............................................................................................. 154

d. Temperatura ..................................................................................................... 157

e. Humedad relativa ............................................................................................. 160

f. Análisis de la incertidumbre ................................................................................ 163

9.5. APENDICE 5 - Proyectos aprobados entre 2020 - 2023 ..................................... 164

9.6. APENDICE 6 - Resultados Modelación 3 años ..................................................... 169

9.6.1. Escenario 1 .................................................................................................... 169

9.6.2. Escenario 2 .................................................................................................... 173

9.6.3. Escenario 3 .................................................................................................... 177

9.6.4. PMI ................................................................................................................ 182

9.7. APENDICE 7 - Isolineas de concentración ........................................................... 184

9.7.1. Isolineas de concentración - Escenario 1 ..................................................... 184

9.7.2. Isolineas de concentración - Escenario 2 ..................................................... 192

10. Bibliografía ............................................................................................................... 201

12

#### Índice de Figuras

Figura 1. Dominio del Proyecto. ........................................................................................... 28

Figura 2. Localización del perímetro de la planta................................................................. 29

Figura 3. Geolocalización de fuentes puntuales y difusas - Fase de construcción Escenario

1. ........................................................................................................................................... 48

Figura 4. Geolocalización de fuentes de ruta - Fase de construcción Escenario 1. ............. 48

Figura 5. Geolocalización de fuentes puntuales y difusas - Incremento de la emisión de la

Fase de operación Escenario 1. ............................................................................................ 49

Figura 6. Geolocalización de fuentes de ruta - Incremento de la emisión de la Fase de

operación Escenario 1 .......................................................................................................... 50

Figura 7. Geolocalización de fuentes puntuales y difusas - Incremento de la emisión de la

Fase de operación Escenario 2. ............................................................................................ 52

Figura 8. Geolocalización de fuentes de ruta - Incremento de la emisión de la Fase de

operación Escenario 2. ......................................................................................................... 52

Figura 9. Geolocalización de fuentes puntuales y difusas - Fase de cierre Escenario 3. ..... 55

Figura 10. Geolocalización de fuentes de ruta - Fase de cierre Escenario 3. ...................... 55

Figura 11. Ubicación de la estación meteorológica de referencia seleccionada. ................ 61

Figura 12. Localización de las estaciones de monitoreo de calidad del aire. ....................... 66

Figura 13. Geolocalización puntual de proyectos colindantes no ejecutados con RCA

favorable. .............................................................................................................................. 70

Figura 14. Localización de receptores del proyecto. ............................................................ 72

Figura 15. Zonificación según plan regulador comunal........................................................ 73

Figura 16. Radio de representatividad de estación Laja. ..................................................... 74

Figura 17. Localización de PMI en Escenario 1. .................................................................... 87

Figura 18. Localización de PMI en Escenario 2. .................................................................. 100

Figura 19. Localización de PMI en Escenario 3. .................................................................. 112

Figura 20. Geolocalización de estaciones meteorológicas dentro del dominio de simulación.

............................................................................................................................................ 118

Figura 21. Rosa de viento año 2020 datos observados en estación Laja (izquierda) y

modelados WRF (derecha). UTC+00................................................................................... 122

Figura 22. Rosa de viento año 2020: Horario 08:00 a 18:00. Datos observados en estación

Laja (izquierda) y modelados WRF (derecha). UTC+00. ..................................................... 123

Figura 23. Rosa de viento año 2020: Horario 18:00 a 8:00. Datos observados en estación

Laja (izquierda) y modelados WRF (derecha). UTC+00. ..................................................... 123

Figura 24. Ciclo diario de la velocidad del viento observada en la estación Laja (m/s).

UTC+00. Año 2020. ............................................................................................................. 124

Figura 25. Ciclo diario de la velocidad del viento modelada en la estación Laja (m/s). UTC+00.

Año 2020. ............................................................................................................................ 124

13

Figura 26. Serie de tiempo de la velocidad del viento observada en la estación Laja (m/s).

UTC+00. Año 2020. ............................................................................................................. 125

Figura 27. Serie de tiempo de la velocidad del viento modelada en la estación Laja (m/s).

UTC+00. Año 2020. ............................................................................................................. 125

Figura 28. Ciclo estacional de la velocidad del viento observada en la estación Laja (m/s).

UTC+00. Año 2020. ............................................................................................................. 126

Figura 29. Ciclo estacional de la velocidad del viento modelada en la estación Laja (m/s).

UTC+00. Año 2020. ............................................................................................................. 126

Figura 30. Ciclo diario de la dirección del viento observada en la estación Laja (°). UTC+00.

Año 2020. ............................................................................................................................ 127

Figura 31. Ciclo diario de la dirección del viento modelada en la estación Laja (°). UTC+00.

Año 2020. ............................................................................................................................ 127

Figura 32. Serie de tiempo de la dirección del viento observada en la estación Laja (°).

UTC+00. Año 2020. ............................................................................................................. 128

Figura 33. Serie de tiempo de la dirección del viento modelada en la estación Laja (°).

UTC+00. Año 2020. ............................................................................................................. 128

Figura 34. Ciclo estacional de la dirección del viento observada en la estación Laja (°).

UTC+00. Año 2020. ............................................................................................................. 129

Figura 35. Ciclo estacional de la dirección del viento modelada en la estación Laja (°).

UTC+00. Año 2020. ............................................................................................................. 129

Figura 36. Ciclo diario de la temperatura observada en la estación Laja (°C). UTC+00. Año

2020. ................................................................................................................................... 130

Figura 37. Ciclo diario de la temperatura modelada en la estación Laja (°C). UTC+00. Año

2020. ................................................................................................................................... 130

Figura 38. Serie de tiempo de la temperatura observada en la estación Laja (°C). UTC+00.

Año 2020. ............................................................................................................................ 131

Figura 39. Serie de tiempo de la temperatura modelada en la estación Laja (°C). UTC+00.

Año 2020. ............................................................................................................................ 131

Figura 40. Ciclo estacional de la temperatura del viento observada en la estación Laja (°C).

UTC+00. Año 2020. ............................................................................................................. 132

Figura 41. Ciclo estacional de la temperatura del viento modelada en la estación Laja (°C).

UTC+00. Año 2020. ............................................................................................................. 132

Figura 42. Ciclo diario de la humedad relativa observada en la estación Laja (%). UTC+00.

Año 2020. ............................................................................................................................ 133

Figura 43. Ciclo diario de la humedad relativa modelada en la estación Laja (%). UTC+00.

Año 2020. ............................................................................................................................ 133

Figura 44. Serie de tiempo de la humedad relativa observada en la estación Laja (%).

UTC+00. Año 2020. ............................................................................................................. 134

14

Figura 45. Serie de tiempo de la humedad relativa modelada en la estación Laja (%). UTC+00.

Año 2020. ............................................................................................................................ 134

Figura 46. Ciclo estacional de la humedad relativa observada en la estación Laja (%).

UTC+00. Año 2020. ............................................................................................................. 134

Figura 47. Ciclo estacional de la humedad relativa modelada en la estación Laja (%). UTC+00.

Año 2020. ............................................................................................................................ 135

Figura 48. Rosa de viento año 2021 datos observados en estación Laja (izquierda) y

modelados WRF (derecha). UTC+00................................................................................... 136

Figura 49. Rosa de viento año 2021: Horario 08:00 a 18:00. Datos observados en estación

Laja (izquierda) y modelados WRF (derecha). UTC+00. ..................................................... 136

Figura 50. Rosa de viento año 2021: Horario 18:00 a 8:00. Datos observados en estación

Laja (izquierda) y modelados WRF (derecha). UTC+00. ..................................................... 137

Figura 51. Ciclo diario de la velocidad del viento observada en la estación Laja (m/s).

UTC+00. Año 2021. ............................................................................................................. 137

Figura 52. Ciclo diario de la velocidad del viento modelada en la estación Laja (m/s). UTC+00.

Año 2021. ............................................................................................................................ 138

Figura 53. Serie de tiempo de la velocidad del viento observada en la estación Laja (m/s).

UTC+00. Año 2021. ............................................................................................................. 138

Figura 54. Serie de tiempo de la velocidad del viento modelada en la estación Laja (m/s).

UTC+00. Año 2021. ............................................................................................................. 139

Figura 55. Ciclo estacional de la velocidad del viento observada en la estación Laja (m/s).

UTC+00. Año 2021. ............................................................................................................. 139

Figura 56. Ciclo estacional de la velocidad del viento modelada en la estación Laja (m/s).

UTC+00. Año 2021. ............................................................................................................. 140

Figura 57. Ciclo diario de la dirección del viento observada en la estación Laja (°). UTC+00.

Año 2021. ............................................................................................................................ 141

Figura 58. Ciclo diario de la dirección del viento modelada en la estación Laja (°). UTC+00.

Año 2021. ............................................................................................................................ 141

Figura 59. Serie de tiempo de la dirección del viento observada en la estación Laja (°).

UTC+00. Año 2021. ............................................................................................................. 142

Figura 60. Serie de tiempo de la dirección del viento modelada en la estación Laja (°).

UTC+00. Año 2021. ............................................................................................................. 142

Figura 61. Ciclo estacional de la dirección del viento observada en la estación Laja (°).

UTC+00. Año 2021. ............................................................................................................. 143

Figura 62. Ciclo estacional de la dirección del viento modelada en la estación Laja (°).

UTC+00. Año 2021. ............................................................................................................. 143

Figura 63. Ciclo diario de la temperatura observada en la estación Laja (°C). UTC+00. Año

2021. ................................................................................................................................... 144

15

Figura 64. Ciclo diario de la temperatura modelada en la estación Laja (°C). UTC+00. Año

2021. ................................................................................................................................... 144

Figura 65. Serie de tiempo de la temperatura observada en la estación Laja (°C). UTC+00.

Año 2021. ............................................................................................................................ 145

Figura 66. Serie de tiempo de la temperatura modelada en la estación Laja (°C). UTC+00.

Año 2021. ............................................................................................................................ 145

Figura 67. Ciclo estacional de la temperatura del viento observada en la estación Laja (°C).

UTC+00. Año 2021. ............................................................................................................. 146

Figura 68. Ciclo estacional de la temperatura del viento modelada en la estación Laja (°C).

UTC+00. Año 2021. ............................................................................................................. 146

Figura 69. Ciclo diario de la humedad relativa observada en la estación Laja (%). UTC+00.

Año 2021. ............................................................................................................................ 147

Figura 70. Ciclo diario de la humedad relativa modelada en la estación Laja (%). UTC+00.

Año 2021. ............................................................................................................................ 147

Figura 71. Serie de tiempo de la humedad relativa observada en la estación Laja (%).

UTC+00. Año 2021. ............................................................................................................. 147

Figura 72. Serie de tiempo de la humedad relativa modelada en la estación Laja (%). UTC+00.

Año 2021. ............................................................................................................................ 148

Figura 73. Ciclo estacional de la humedad relativa observada en la estación Laja (%).

UTC+00. Año 2021. ............................................................................................................. 148

Figura 74. Ciclo estacional de la humedad relativa modelada en la estación Laja (%). UTC+00.

Año 2021. ............................................................................................................................ 149

Figura 75. Rosa de viento año 2022 datos observados en estación Laja (izquierda) y

modelados WRF (derecha). UTC+00................................................................................... 150

Figura 76. Rosa de viento año 2022: Horario 08:00 a 18:00. Datos observados en estación

Laja (izquierda) y modelados WRF (derecha). UTC+00. ..................................................... 150

Figura 77. Rosa de viento año 2022: Horario 18:00 a 8:00. Datos observados en estación

Laja (izquierda) y modelados WRF (derecha). UTC+00. ..................................................... 151

Figura 78. Ciclo diario de la velocidad del viento observada en la estación Laja (m/s).

UTC+00. Año 2022. ............................................................................................................. 151

Figura 79. Ciclo diario de la velocidad del viento modelada en la estación Laja (m/s). UTC+00.

Año 2022. ............................................................................................................................ 152

Figura 80. Serie de tiempo de la velocidad del viento observada en la estación Laja (m/s).

UTC+00. Año 2022. ............................................................................................................. 152

Figura 81. Serie de tiempo de la velocidad del viento modelada en la estación Laja (m/s).

UTC+00. Año 2022. ............................................................................................................. 153

Figura 82. Ciclo estacional de la velocidad del viento observada en la estación Laja (m/s).

UTC+00. Año 2022. ............................................................................................................. 153

16

Figura 83. Ciclo estacional de la velocidad del viento modelada en la estación Laja (m/s).

UTC+00. Año 2022. ............................................................................................................. 154

Figura 84. Ciclo diario de la dirección del viento observada en la estación Laja (°). UTC+00.

Año 2022. ............................................................................................................................ 155

Figura 85. Ciclo diario de la dirección del viento modelada en la estación Laja (°). UTC+00.

Año 2022. ............................................................................................................................ 155

Figura 86. Serie de tiempo de la dirección del viento observada en la estación Laja (°).

UTC+00. Año 2022. ............................................................................................................. 156

Figura 87. Serie de tiempo de la dirección del viento modelada en la estación Laja (°).

UTC+00. Año 2022. ............................................................................................................. 156

Figura 88. Ciclo estacional de la dirección del viento observada en la estación Laja (°).

UTC+00. Año 2022. ............................................................................................................. 157

Figura 89. Ciclo estacional de la dirección del viento modelada en la estación Laja (°).

UTC+00. Año 2022. ............................................................................................................. 157

Figura 90. Ciclo diario de la temperatura observada en la estación Laja (°C). UTC+00. Año

2022. ................................................................................................................................... 158

Figura 91. Ciclo diario de la temperatura modelada en la estación Laja (°C). UTC+00. Año

2022. ................................................................................................................................... 158

Figura 92. Serie de tiempo de la temperatura observada en la estación Laja (°C). UTC+00.

Año 2022. ............................................................................................................................ 159

Figura 93. Serie de tiempo de la temperatura modelada en la estación Laja (°C). UTC+00.

Año 2022. ............................................................................................................................ 159

Figura 94. Ciclo estacional de la temperatura del viento observada en la estación Laja (°C).

UTC+00. Año 2022. ............................................................................................................. 160

Figura 95. Ciclo estacional de la temperatura del viento modelada en la estación Laja (°C).

UTC+00. Año 2022. ............................................................................................................. 160

Figura 96. Ciclo diario de la humedad relativa observada en la estación Laja (%). UTC+00.

Año 2022. ............................................................................................................................ 161

Figura 97. Ciclo diario de la humedad relativa modelada en la estación Laja (%). UTC+00.

Año 2022. ............................................................................................................................ 161

Figura 98. Serie de tiempo de la humedad relativa observada en la estación Laja (%).

UTC+00. Año 2022. ............................................................................................................. 161

Figura 99. Serie de tiempo de la humedad relativa modelada en la estación Laja (%). UTC+00.

Año 2022. ............................................................................................................................ 162

Figura 100. Ciclo estacional de la humedad relativa observada en la estación Laja (%).

UTC+00. Año 2022. ............................................................................................................. 162

Figura 101. Ciclo estacional de la humedad relativa modelada en la estación Laja (%).

UTC+00. Año 2022. ............................................................................................................. 163

17

Figura 102. Isolíneas Promedio anual de la concentración de MP 10 - Escenario 1. ........... 184

Figura 103. Isolíneas del percentil 98 de la concentración de 24 horas de MP 10 - Escenario

1. ......................................................................................................................................... 185

Figura 104. Isolíneas Promedio anual de la concentración de MP 2.5 - Escenario 1. ........... 185

Figura 105. Isolíneas del percentil 98 de la concentración de 24 horas de MP 2.5 - Escenario

1. ......................................................................................................................................... 186

Figura 106. Isolíneas de la tasa de deposición promedio anual de MPS - Escenario 1. .... 186

Figura 107. Isolíneas del promedio anual de la concentración de NO 2 - Escenario 1. ...... 187

Figura 108. Isolíneas del percentil 99 de la concentración horaria de NO 2 - Escenario 1. 187

Figura 109. Isolíneas del promedio anual de la concentración de SO 2 - Escenario 1. ....... 188

Figura 110. Isolíneas del percentil 99 de la concentración diaria de SO 2 - Escenario 1. ... 188

Figura 111. Isolíneas del percentil 98,5 de la concentración horaria de SO 2 - Escenario 1.

............................................................................................................................................ 189

Figura 112. Isolíneas del percentil 99,7 de la concentración diaria de SO 2 - Escenario 1. 189

Figura 113. Isolíneas del percentil 99,73 de la concentración horaria de SO 2 - Escenario 1.

............................................................................................................................................ 190

Figura 114. Isolíneas del percentil 99 de la concentración horaria de CO - Escenario 1. . 190

Figura 115. Isolíneas del percentil 99 de la concentración 8 horas de CO - Escenario 1. . 191

Figura 116. Isolíneas de la concentración diaria de TRS - Escenario 1. ............................. 191

Figura 117. Isolíneas de la concentración horaria de TRS - Escenario 1. .......................... 192

Figura 118. Isolíneas Promedio anual de la concentración de MP 10 - Escenario 2. ........... 192

Figura 119. Isolíneas del percentil 98 de la concentración de 24 horas de MP 10 - Escenario

2. ......................................................................................................................................... 193

Figura 120. Isolíneas Promedio anual de la concentración de MP 2.5 - Escenario 2. ........... 193

Figura 121. Isolíneas del percentil 98 de la concentración de 24 horas de MP 2.5 - Escenario

2. ......................................................................................................................................... 194

Figura 122. Isolíneas de la tasa de deposición promedio anual de MPS - Escenario 2. .... 194

Figura 123. Isolíneas del promedio anual de la concentración de NO 2 - Escenario 2. ...... 195

Figura 124. Isolíneas del percentil 99 de la concentración horaria de NO 2 - Escenario 2. 195

Figura 125. Isolíneas del promedio anual de la concentración de SO 2 - Escenario 2. ....... 196

Figura 126. Isolíneas del percentil 99 de la concentración diaria de SO 2 - Escenario 2. ... 196

Figura 127. Isolíneas del percentil 98,5 de la concentración horaria de SO 2 - Escenario 2.

............................................................................................................................................ 197

Figura 128. Isolíneas del percentil 99,7 de la concentración diaria de SO 2 - Escenario 2. 197

Figura 129. Isolíneas del percentil 99,73 de la concentración horaria de SO 2 - Escenario 2.

............................................................................................................................................ 198

Figura 130. Isolíneas del percentil 99 de la concentración horaria de CO - Escenario 2. . 198

Figura 131. Isolíneas del percentil 99 de la concentración 8 horas de CO - Escenario 2. . 199

18

Figura 132. Isolíneas de la concentración diaria de TRS - Escenario 2. ............................. 199

Figura 133. Isolíneas de la concentración horaria de TRS - escenario 2. .......................... 200

19

#### Índice de Tablas

Tabla 1. Estadísticos con saturación de la línea base. 3

Tabla 2. Tabla resumen estadísticos - Escenario 1 parte 1. 5

Tabla 3. Tabla resumen estadísticos - Escenario 1 parte 2. 5

Tabla 4. Tabla resumen estadísticos - Escenario 2 parte 1. 6

Tabla 5. Tabla resumen estadísticos - Escenario 2 parte 2. 7

Tabla 6. Tabla resumen estadísticos - Escenario 3 parte 1. 8

Tabla 7. Tabla resumen estadísticos - Escenario 3 parte 2. 8

Tabla 8. Características del dominio de simulación. 28

Tabla 9. Antecedentes de la proyección del dominio de simulación - Proyección LCC. 29

Tabla 10. Cronograma del proyecto - Fase de construcción. 32

Tabla 11. Cronograma del proyecto - fase de cierre. 33

Tabla 12. Fuentes de emisión durante la fase de construcción del proyecto. 34

Tabla 13. Fuentes de emisión durante la fase de operación del proyecto. 34

Tabla 14. Fuentes de emisión durante la fase de cierre del proyecto. 35

Tabla 15. Inventario de emisiones de la fase de construcción - Mes 4 al mes 12 (año 2024).

36

Tabla 16. Inventario de emisiones de la fase de construcción - Mes 13 al mes 24 (año 2025)

37

Tabla 17. Inventario de emisiones de la fase de operación base - Emisiones de 1 año. 38

Tabla 18. Inventario de emisiones de la fase de operación proyectada - Emisiones de 1 año.

38

Tabla 19. Inventario de emisiones - Incremento emisión de Fase de operación (1 año). 39

Tabla 20. Inventario de emisiones de la fase de cierre - Emisiones de 1 año. 40

Tabla 21. Cronograma de alternativas a evaluar para el escenario 1. 41

Tabla 22. Alternativas de análisis del escenario 1. 41

Tabla 23. Inventario de emisiones - Fase de construcción meses 13 al 21. 42

Tabla 24. Inventario de emisiones - Incremento de emisión de la fase de operación meses

16 al 24. 42

Tabla 25. Inventario de emisiones - Incremento de la emisión de la Fase de operación (1

año). 43

Tabla 26. Inventario de emisiones - Fase de cierre (1 año). 43

Tabla 27. Nivel de actividad para fuente difusa - Escenario 1 Fase de construcción. 44

Tabla 28. Nivel de actividad para fuente puntual - Escenario 1 Fase de construcción. 44

Tabla 29. Nivel de actividad para fuentes de ruta - Escenario 1 Fase de construcción. 45

Tabla 30. Nivel de actividad para fuente difusa - Escenario 1 Incremento de la emisión de la

Fase de operación. 46

20

Tabla 31. Nivel de actividad para fuentes puntuales - Escenario 1 Incremento de la emisión

de la Fase de operación. 46

Tabla 32. Nivel de actividad para fuentes de ruta - Escenario 1 Incremento de la emisión de

la Fase de operación. 46

Tabla 33. Nivel de actividad para fuente difusa - Escenario 2 Incremento de la emisión de la

Fase de operación. 50

Tabla 34. Nivel de actividad para fuentes puntuales - Escenario 2 Incremento de la emisión

de la Fase de operación. 51

Tabla 35. Nivel de actividad para fuentes de ruta - Escenario 2 Incremento de la emisión de

la Fase de operación. 51

Tabla 36. Nivel de actividad para fuentes difusas - Escenario 3 Fase de cierre. 53

Tabla 37. Nivel de actividad para fuente puntual - Escenario 3 Fase de cierre. 53

Tabla 38. Nivel de actividad para fuentes de ruta - Escenario 3 Fase de cierre. 54

Tabla 39. Factor de variación de la emisión de fuentes ruta - Escenario 1 Fase de

construcción. 56

Tabla 40. Factor de variación de la emisión de fuente difusa - Escenario 1 Fase de

construcción. 56

Tabla 41. Factor de variación de la emisión de fuente puntual - Escenario 1 Fase de

construcción. 56

Tabla 42. Factor de variación de la emisión de fuentes de ruta - Escenario 1 incremento de

la emisión de la Fase operación. 57

Tabla 43. Factor de variación de la emisión de fuente puntual - Escenario 1 incremento de

la emisión de la de Fase de operación. 57

Tabla 44. Factor de variación de la emisión de fuentes de ruta - Escenario 2 incremento de

la emisión de la Fase operación. 57

Tabla 45. Factor de variación de la emisión de la fuente puntual - Escenario 3 Fase de cierre.

58

Tabla 46. Factor de variación de la emisión de fuente difusa Cota 45, Tall Oil, Superficie 1 y

Chipscrinning - Escenario 3 Fase de cierre. 58

Tabla 47. Factor de variación de la emisión de la fuente difusa evaporadores, caldera, batch

y horno - Escenario 3 Fase de cierre. 58

Tabla 48. Factor de variación de la emisión de fuente difusa superficie 2 - Escenario 3 Fase

de cierre. 59

Tabla 49. Factor de variación de la emisión de las fuentes de ruta - Escenario 3 Fase de

cierre. 59

Tabla 50. Ubicación de la estación meteorológica superficial. 60

Tabla 51. Valores de los índices de la predicción proporcionada por el modelo para la

estación meteorológica - Años 2020 a 2022 62

21

Tabla 52. Normativas aplicables para material particulado. 63

Tabla 53. Normativas aplicables para gases. 63

Tabla 54. Norma homologada para evaluar impacto por material particulado sedimentable.

65

Tabla 55. Norma homologada para evaluar impacto por TRS. 65

Tabla 56. Datos disponibles en estaciones de monitoreo de calidad del aire. 67

Tabla 57. Línea base. 67

Tabla 58. Resumen SILs. 69

Tabla 59. Aporte proyectos no ejecutados, colindantes al perímetro del proyecto. 70

Tabla 60. Receptores discretos. 71

Tabla 61. Descripción de receptores discretos. 73

Tabla 62. Promedio anual de la concentración de MP 10 - Escenario 1. 75

Tabla 63. Percentil 98 de la concentración diaria de MP 10 - Escenario 1. 76

Tabla 64. Impacto sobre la salud de las personas por el promedio anual de la concentración

de MP 2.5 - Escenario 1. 76

Tabla 65. Impacto sobre la salud de las personas del percentil 98 de la concentración diaria

de MP 2.5 - Escenario 1. 77

Tabla 66. Promedio anual de la tasa de deposición del material particulado sedimentable

(MPS) - Escenario 1. 78

Tabla 67. Promedio anual de la concentración de dióxido de nitrógeno (NO 2 ) - Escenario 1.

78

Tabla 68. Percentil 99 de la concentración horaria de NO 2 - Escenario 1. 79

Tabla 69. Promedio anual de la concentración de dióxido de azufre (SO 2 ) - Escenario 1. 80

Tabla 70. Percentil 99 de la concentración diaria de SO 2 - Escenario 1. 80

Tabla 71. Percentil 98,5 de la concentración de 1 h de SO 2 - Escenario 1. 81

Tabla 72. Percentil 99,7 de la concentración diaria de SO 2 - Escenario 1. 81

Tabla 73. Percentil 99,73 de la concentración horaria de SO 2 - Escenario 1. 82

Tabla 74. Percentil 99 de la concentración de 1 h de CO - Escenario 1. 82

Tabla 75. Percentil 99 de la concentración 8 h de CO - Escenario 1. 83

Tabla 76. Concentración diaria de TRS - Escenario 1. 83Tabla 77. Impacto sobre la salud de las personas por la concentración horaria de TRS

Escenario 1. 84

Tabla 78. Resumen de Punto de Máximo Impacto - Escenario 1. 85

Tabla 79. Cumplimiento de normativa de los estadísticos del PMI - Escenario 1 86

Tabla 80. Promedio anual de la concentración de MP 10 - Escenario 2. 88

Tabla 81. Percentil 98 de la concentración diaria de MP 10 - Escenario 2. 88

Tabla 82. Impacto sobre la salud de las personas por el promedio anual de la concentración

de MP 2.5 - Escenario 2. 89

22

Tabla 83. Impacto sobre la salud de las personas por el percentil 98 de la concentración

diaria de MP 2.5 - Escenario 2. 90

Tabla 84. Promedio anual de la tasa de deposición del material particulado sedimentable

(MPS) - Escenario 2. 90

Tabla 85. Promedio anual de la concentración de dióxido de nitrógeno (NO 2 ) - Escenario 2.

91

Tabla 86. Percentil 99 de la concentración horaria de NO 2 - Escenario 2. 91

Tabla 87. Promedio anual de la concentración de dióxido de azufre (SO 2 ) - Escenario 2. 92

Tabla 88. Percentil 99 de la concentración diaria de SO 2 - Escenario 2. 93

Tabla 89. Percentil 98,5 de la concentración de 1 h de SO 2 - Escenario 2. 93

Tabla 90. Percentil 99,7 de la concentración diaria de SO 2 - Escenario 2. 94

Tabla 91. Percentil 99,73 de la concentración horaria de SO 2 - Escenario 2. 94

Tabla 92. Percentil 99 de la concentración de 1 h de CO - Escenario 2. 95

Tabla 93. Percentil 99 de la concentración 8 h de CO - Escenario 2. 95

Tabla 94. Concentración diaria de TRS - Escenario 2. 96Tabla 95. Impacto sobre la salud de las personas por la concentración horaria de TRS

Escenario 2. 96

Tabla 96. Resumen de Punto de Máximo Impacto - Escenario 2. 98

Tabla 97. Cumplimiento de normativa de los estadísticos del PMI - Escenario 2. 99

Tabla 98. Promedio anual de la concentración de MP 10 - Escenario 3. 101

Tabla 99. Percentil 98 de la concentración diaria de MP 10 - Escenario 3. 101

Tabla 100. Impacto sobre la salud de las personas por el promedio anual de la concentración

de MP 2.5 - Escenario 3. 102

Tabla 101. Impacto sobre la salud de las personas del percentil 98 de la concentración diaria

de MP 2.5 - Escenario 3. 103

Tabla 102. Promedio anual de la tasa de deposición del material particulado sedimentable

(MPS) - Escenario 3. 104

Tabla 103. Promedio anual de la concentración de dióxido de nitrógeno (NO 2 ) - Escenario

3. 104

Tabla 104. Percentil 99 de la concentración horaria de NO 2 - Escenario 3. 105

Tabla 105. Promedio anual de la concentración de dióxido de azufre (SO 2 ) - Escenario 3.

106

Tabla 106. Percentil 99 de la concentración diaria de SO 2 - Escenario 3. 106

Tabla 107. Percentil 98,5 de la concentración de 1 h de SO 2 - Escenario 3. 107

Tabla 108. Percentil 99,7 de la concentración diaria de SO 2 - Escenario 3. 108

Tabla 109. Percentil 99,73 de la concentración horaria de SO 2 - Escenario 3. 108

Tabla 110. Percentil 99 de la concentración de 1 h de CO - Escenario 3. 109

Tabla 111. Percentil 99 de la concentración 8 h de CO - Escenario 3. 109

23

Tabla 112. Resumen de Punto de Máximo Impacto - Escenario 3. 110

Tabla 113. Lista de anexos. 114

Tabla 114. Datos de fuentes puntuales. 116

Tabla 115. Tasa de emisión de TRS en RCA 2009, para producción de 500.000 ton/año. 117

Tabla 116. Resumen de emisión de TRS con datos CEMS y RCA 2009. 117

Tabla 117. Análisis de proximidad de estaciones meteorológicas superficiales dentro del

dominio. 119

Tabla 118. Datos de la estación meteorológica superficial seleccionada. 119

Tabla 119. Criterios estadísticos de aceptación de la predicción proporcionada para un

modelo meteorológico. 121

Tabla 120. Valores de los índices de la predicción proporcionada por el modelo para la

estación meteorológica. Año 2020. 135

Tabla 121. Valores de los índices de la predicción proporcionada por el modelo para la

estación meteorológica. Año 2021. 149

Tabla 122. Valores de los índices de la predicción proporcionada por el modelo para la

estación meteorológica. Año 2022. 163

Tabla 123. Listado proyectos aprobados. 164

Tabla 124. Promedio anual de la concentración de MP 10 - Escenario 1. 169

Tabla 125. Percentil 98 de la concentración diaria de MP 10 - Escenario 1. 169

Tabla 126. Promedio anual de la concentración de MP 2.5 - Escenario 1. 169

Tabla 127. Percentil 98 de la concentración diaria de MP 2.5 - Escenario 1. 170

Tabla 128. Promedio anual de la tasa de deposición del material particulado sedimentable

(MPS) - Escenario 1. 170

Tabla 129. Promedio anual de la concentración de dióxido de nitrógeno (NO 2 ) - Escenario

1. 170

Tabla 130. Percentil 99 de la concentración horaria de NO 2 - Escenario 1. 170

Tabla 131. Promedio anual de la concentración de dióxido de azufre (SO 2 ) - Escenario 1.

170

Tabla 132. Percentil 99 de la concentración diaria de SO 2 - Escenario 1. 171

Tabla 133. Percentil 98,5 de la concentración de 1 h de SO 2 - Escenario 1. 171

Tabla 134. Percentil 99,7 de la concentración diaria de SO 2 - Escenario 1. 171

Tabla 135. Percentil 99,73 de la concentración horaria de SO 2 - Escenario 1. 171

Tabla 136. Percentil 99 de la concentración de 1 h de CO - Escenario 1. 172

Tabla 137. Percentil 99 de la concentración 8 h de CO - Escenario 1. 172

Tabla 138. Concentración diaria de TRS - Escenario 1. 172

Tabla 139. Concentración horaria de TRS - Escenario 1. 173

Tabla 140. Promedio anual de la concentración de MP 10 - Escenario 2. 173

Tabla 141. Percentil 98 de la concentración diaria de MP 10 - Escenario 2. 173

24

Tabla 142. Promedio anual de la concentración de MP 2.5 - Escenario 2. 173

Tabla 143. Percentil 98 de la concentración diaria de MP 2.5 - Escenario 2. 174

Tabla 144. Promedio anual de la tasa de deposición del material particulado sedimentable

(MPS) - Escenario 2. 174

Tabla 145. Promedio anual de la concentración de dióxido de nitrógeno (NO 2 ) - Escenario

2. 174

Tabla 146. Percentil 99 de la concentración horaria de NO 2 - Escenario 2. 174

Tabla 147. Promedio anual de la concentración de dióxido de azufre (SO 2 ) - Escenario 2.

175

Tabla 148. Percentil 99 de la concentración diaria de SO 2 - Escenario 2. 175

Tabla 149. Percentil 98,5 de la concentración de 1 h de SO 2 - Escenario 2. 175

Tabla 150. Percentil 99,7 de la concentración diaria de SO 2 - Escenario 2. 175

Tabla 151. Percentil 99,73 de la concentración horaria de SO 2 - Escenario 2. 176

Tabla 152. Percentil 99 de la concentración de 1 h de CO - Escenario 2. 176

Tabla 153. Percentil 99 de la concentración 8 h de CO - Escenario 2. 176

Tabla 154. Concentración diaria de TRS - Escenario 2. 177

Tabla 155. Concentración horaria TRS - Escenario 2. 177

Tabla 156. Promedio anual de la concentración de MP 10 - Escenario 3. 177

Tabla 157. Percentil 98 de la concentración diaria de MP 10 - Escenario 3. 177

Tabla 158. Promedio anual de la concentración de MP 2.5 - Escenario 3. 178

Tabla 159. Percentil 98 de la concentración diaria de MP 2.5 - Escenario 3. 178

Tabla 160. Promedio anual de la tasa de deposición del material particulado sedimentable

(MPS) - Escenario 3. 178

Tabla 161. Promedio anual de la concentración de dióxido de nitrógeno (NO 2 ) - Escenario

3. 178

Tabla 162. Percentil 99 de la concentración horaria de NO 2 - Escenario 3. 179

Tabla 163. Promedio anual de la concentración de dióxido de azufre (SO 2 ) - Escenario 3.

179

Tabla 164. Percentil 99 de la concentración diaria de SO 2 - Escenario 3. 179

Tabla 165. Percentil 98,5 de la concentración de 1 h de SO 2 - Escenario 3. 179

Tabla 166. Percentil 99,7 de la concentración diaria de SO 2 - Escenario 3. 180

Tabla 167. Percentil 99,73 de la concentración horaria de SO 2 - Escenario 3. 180

Tabla 168. Percentil 99 de la concentración de 1 h de CO - Escenario 3. 180

Tabla 169. Percentil 99 de la concentración 8 h de CO - Escenario 3. 180

Tabla 170. Resumen de PMI para cada MP y gas emitido en los escenarios. 182

25

#### 1. Introducción

El proyecto de _CMPC Pulp SpA_ considera modificaciones en distintas áreas del proceso

productivo de la Planta Laja de CMPC, que permitirán modificar los tipos de productos

cambiando el producto desde pulpa blanca a pulpa no blanqueada.

El proyecto cuenta con tres RCA previas, correspondientes a:

 RCA N°56/2004: se introdujo mejoras a distintos subprocesos para optimizar el

desempeño de la planta y aumentar la producción máxima hasta 439.000 ton/año.

 RCA N°203/2009: modernizó proceso productivo de fabricación de celulosa,

introduciendo cambios en calderas y hornos, y aumenta la capacidad de producción

máxima hasta 500.000 ton/año.

 RCA N°202208101194: La S/E se amplía mediante la construcción de un nuevo paño

J1, conectándose a la sección de la barra principal N°2 de 220 kV. Adicionalmente

se construirá una nueva sala de control y baterías.

Si bien la planta tiene aprobada una producción máxima de 500.000 ton/año, actualmente

la planta tiene una producción aproximada de 360.000 ton/año de productos totales

(celulosa y papeles) y se estima que la ejecución del proyecto permitirá alcanzar una

producción total 400.000 ton/año.

Las modificaciones y actualizaciones a la planta consisten en:

 - **Modificación máquina papelera N°15 (MP15):** Actualización de circuitos de

recuperación de agua de la maquina papelera N°15. Se mantiene maquinas

papeleras existentes MP12 y MP15. Equipamiento asociado al proceso de

terminación.

 - **Modificación máquina secadora N°2** : adecuación de la maquinaria para el nuevo

proceso productivo. Equipamiento asociado al proceso de terminación.

 - **Deshabilitación de la Planta de Blanqueo y sus instalaciones auxiliares** : se

deshabilita la planta, junto a los procesos auxiliares de planta de dióxido de cloro y

planta de oxígeno.

 - **Nueva planta Tall Oil** : planta para aprovechar el jabón obtenido como subproducto

de las plantas laja y tercero. Tiene recepción, almacenaje y extracción (almacenaje

en estanques y se separa por fase jabón y licor negro), preparación y acidulación,

separación, almacenaje o quemado, lavado de gases y neutralización agua ácida.

26

 - **Nueva área de preparación maderas** : nuevo sistema de clasificación de astillas y el

sistema de descortezado, astillado y la prensa de corteza.

 - **Modificaciones áreas de fibra y digestor** : modificación del digestor.

 - **Mejora en sistema de recolección de gases diluidos.**

 - **Modificaciones sistema de recolección de aguas lluvia:** Adición de zona de

recolección, A5 y el incremento de las áreas A6A y A7.

Todas las plantas de CMPC Pulp SPA están certificadas según las normas ISO 9.001, ISO

14.001, ISO 45001 e ISO 50.001.

##### 1.1. Objetivo

Evaluar el potencial impacto de las emisiones de material particulado (MP 10, MP 2.5, MPS) y

“
gases (NO 2, SO 2, CO y TRS) del proyecto _Proyecto de modificación para producir_ _celulosa_

_cruda en Planta Laja_ ”, a través de la modelación de las emisiones atmosféricas procedentes

del proyecto en la fase de construcción, en la fase de operación y fase de cierre.

27

#### 2. Dominio de simulación

La planta Laja se encuentra en la comuna de Laja, en la provincia del Biobío, de la región del

Biobío, a una distancia de 140 kilómetros al Sureste de Concepción y de 74 kilómetros al
Noroeste de Los Ángeles. En la Figura 1 se presenta el dominio de simulación y en la Tabla

8 se presenta las características del dominio de simulación.

**Nota** : En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml.

**Figura 1. Dominio del Proyecto.**

**Tabla 8. Características del dominio de simulación.**

|Descripción|Detalle|
|---|---|
|Periodo de simulación|2020 al 20221|
|Resolución|1 x 1 km|
|Extensión|75 x 75 km|

1 Según la metodología indicada en la “ _Guía para el uso de modelos de calidad del aire en el SEIA_ ” (2023) para la elección
del período modelado, se recomienda que se analicen al menos los tres años anteriores.

28

Se modelaron 3 años y se evalúa para cada receptor, el periodo en el cual reciben la mayor

concentración y/o tasa de deposición. En la sección 9.6 APENDICE 6 - Resultados

Modelación 3 años **,** se presentan los resultados para los 3 años.

**Tabla 9. Antecedentes de la proyección del dominio de simulación - Proyección LCC.**

|Variable|Detalle|
|---|---|
|RLat0|37,263S|
|RLon0|72,711W|
|XLat1|33,402S|
|XLat2|41,178S|

Por otra parte, en la Figura 2 se presenta la localización del perímetro de la planta.

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml .

**Figura 2. Localización del perímetro de la planta.**

29

#### 3. Tipología del Proyecto

La ley N°19.300 sobre Bases Generales del Medio Ambiente, modificada por la Ley N°

20.417, que crea el Ministerio del Medio Ambiente, él SEA y la SMA, en su artículo 10 y

Reglamento del Sistema de Evaluación de Impacto Ambiental D.S N° 40/2012, en su artículo

3, establece que los proyectos o actividades susceptibles a causar impacto ambiental y bajo

las cuales se encuentra el proyecto “ _Proyecto de modificación para producir_ _celulosa_ _cruda_

_en Planta Laja_ ”, corresponden a dos tipologías: una tipología principal (m.4), del Artículo

10 de la Ley de Bases Generales del Medio Ambiente (LBGMA):

**m)** Proyectos de desarrollo o explotación forestales en suelos frágiles, en terrenos

cubiertos de bosque nativo, industrias de celulosa, pasta de papel y papel, Plantas

astilladoras, elaboradoras de madera y aserraderos, todos de dimensiones

industriales:

➢ **Literal m.4.** Toda industria de celulosa, pasta de papel y papel será considerada de

dimensiones industriales.

30

#### 4. Inventario de Emisiones

En esta sección se presenta los inventarios de emisión atmosféricas emitidas por el proyecto
“ _Proyecto de modificación para producir_ _celulosa_ _cruda en Planta Laja_ ” en sus fases de
construcción, operación y cierre.

En el presente proyecto se cuantifica el impacto de las emisiones de MP (MP 10, MP 2,5 y MPS) y

gases (NO 2, SO 2, CO y TRS) en la fase de construcción, el incremento del aporte del proyecto

de la fase operación, el cual corresponde a la diferencia entre las emisiones de la operación

actual y de la operación proyectada, y la fase de cierre. Cabe mencionar que la línea base se

obtiene de las estaciones de monitoreo y se presenta en la sección 6.2 Línea base de calidad

del aire.

La emisión de TRS de las fuentes puntuales fue estimada con los datos de la RCA 2009, para la

producción actual y proyectada. Este criterio se fundamentó en una determinación más

conservadora en los niveles, dado que se sobrestima la emisión con respecto a datos CEMS,

en 1,83 veces para el horno cal, 3,65 veces para la caldera de biomasa y 2,5 veces la calderarecuperadora (ver APENDICE 2 Estimación de emisión de TRS).

A continuación, se presenta el cronograma del proyecto en la **fase de construcción** .

31

**Tabla 10. Cronograma del proyecto** **-** **Fase de construcción.**

|ÁREA|ACTIVIDADES|AÑO|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ÁREA**|**ACTIVIDADES**|**2024**|**2024**|**2024**|**2024**|**2024**|**2024**|**2024**|**2024**|**2024**|**2024**|**2024**|**2024**|**2025**|**2025**|**2025**|**2025**|**2025**|**2025**|**2025**|**2025**|**2025**|**2025**|**2025**|**2025**|
|**ÁREA**|**ACTIVIDADES**|**ENE**|**FEB**|**MAR**|**ABR**|**MAY**|**JUN**|**JUL**|**AGO**|**SEPT**|**OCT**|**NOV**|**DIC**|**ENE**|**FEB**|**MAR**|**ABR**|**MAY**|**JUN**|**JUL**|**AGO**|**SEPT**|**OCT**|**NOV**|**DIC**|
|Área<br>Preparación<br>Maderas|Obras civiles|||||||||||||||||||||||||
|Área<br>Preparación<br>Maderas|Fundaciones|||||||||||||||||||||||||
|Área<br>Preparación<br>Maderas|Montajes<br>electromecánicos|||||||||||||||||||||||||
|Área<br>Preparación<br>Maderas|Puesta en<br>marcha|||||||||||||||||||||||||
|Área fibra y<br>digestor|Obras civiles|||||||||||||||||||||||||
|Área fibra y<br>digestor|Fundaciones|||||||||||||||||||||||||
|Área fibra y<br>digestor|Montajes<br>electromecánicos|||||||||||||||||||||||||
|Área fibra y<br>digestor|Puesta en<br>marcha|||||||||||||||||||||||||
|Máquina<br>secadora N°2|Montajes<br>electromecánicos<br>- 1|||||||||||||||||||||||||
|Máquina<br>secadora N°2|Montajes<br>electromecánicos<br>- 2|||||||||||||||||||||||||
|Máquina<br>secadora N°2|Puesta en<br>marcha|||||||||||||||||||||||||
|Planta Tall Oil|Obras civiles|||||||||||||||||||||||||
|Planta Tall Oil|Fundaciones|||||||||||||||||||||||||
|Planta Tall Oil|Montajes<br>electromecánicos|||||||||||||||||||||||||
|Planta Tall Oil|Puesta en<br>marcha|||||||||||||||||||||||||

**Fuente** : Estimación de emisiones atmosféricas.

La **fase de operación proyectada** del proyecto parte desde el segundo semestre del 2025 y finaliza el 2066.

32

A continuación, se presenta el cronograma de la **fase de cierre** .

**Tabla 11. Cronograma del proyecto - fase de cierre.**

|ACTIVIDADES|Año|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ACTIVIDADES**|**Meses**|**Meses**|**Meses**|**Meses**|**Meses**|**Meses**|**Meses**|**Meses**|**Meses**|**Meses**|**Meses**|**Meses**|
|**ACTIVIDADES**|**ENE**|**FEB**|**MAR**|**ABR**|**MAY**|**JUN**|**JUL**|**AGO**|**SEPT**|**OCT**|**NOV**|**DIC**|
|Habilitación de instalación de faenas|||||||||||||
|Desmantelamiento de estructuras, desarme de fundaciones y desconexiones de equipos|||||||||||||
|Desarme de instalación de faenas|||||||||||||
|Limpieza final|||||||||||||

**Fuente** : Estimación de emisiones atmosféricas.

33

##### 4.1. Fuentes de Emisión

A continuación, se identifica el material particulado y gases que se emiten por actividad de
cada una de las fases del proyecto.

##### 4.1.1. Fase de Construcción

La fase de construcción tiene una duración de 21 meses, distribuidos en el trabajo en el área
de preparación de maderas, área fibra y digestor, maquina secadora N°2 y Planta Tall Oil.

A continuación, se presenta una tabla resumen de las actividades y cuales gases y material
particulado emiten.

**Tabla 12. Fuentes de emisión durante la fase de construcción del proyecto.**

|Actividad|Fuente|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Actividad**|**MP10**|**MP2,5**|**MPS**|**NO2**|**SO2**|**CO**|**TRS**|
|Demolición|X|X|X|--|--|--|--|
|Escarpe|X|X|X|--|--|--|--|
|Excavaciones|X|X|X|--|--|--|--|
|Nivelación|X|X|X|--|--|--|--|
|Compactación|X|X|X|--|--|--|--|
|Transferencia de material|X|X|X|--|--|--|--|
|Transito caminos pavimentados|X|X|X|--|--|--|--|
|Transito caminos no pavimentados|X|X|X|--|--|--|--|
|Combustión vehicular por caminos pavimentados|X|X|X|X|X|X|--|
|Combustión vehicular por caminos no pavimentados|X|X|X|X|X|X|--|
|Combustión de maquinarias|X|X|X|X|X|X|--|
|Combustión grupos electrógenos|X|X|X|X|X|X|--|

**Fuente** : Estimación de emisiones atmosféricas.

##### 4.1.2. Fase de Operación

La fase de operación tiene una operación base (actual) y proyectada. La operación
proyectada se estima que finaliza el año 2066. A continuación, se identifica el material
particulado y gases que se emite por actividad de las fases de operación.

**Tabla 13. Fuentes de emisión durante la fase de operación del proyecto.**

|Actividad|Fuente|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Actividad**|**MP10**|**MP2,5**|**MPS**|**NO2**|**SO2**|**CO**|**TRS**|
|Transferencia de material|X|X|X|--|--|--|--|
|Erosión eólica|X|X|X|--|--|--|--|
|Molienda de biomasa|X|X|X|--|--|--|--|
|Transito caminos pavimentados|X|X|X|--|--|--|--|
|Transito caminos no pavimentados|X|X|X|--|--|--|--|
|Combustión vehicular por caminos pavimentados|X|X|X|X|X|X|--|
|Combustión vehicular por caminos no pavimentados|X|X|X|X|X|X|--|
|Combustión de maquinarias|X|X|X|X|X|X|--|
|Combustión grupos electrógenos|X|X|X|X|X|X|--|
|Transporte en ferrocarril|X|X|X|X|X|X|--|
|Caldera biomasa N°3|X|X|X|X|X|X|X|
|Caldera recuperadora N°6|X|X|X|X|X|X|X|
|Horno de cal N°3|X|X|X|X|X|X|X|
|Incinerador 1|X|X|X|X|X|X|--|
|Incinerador 2|X|X|X|X|X|X|--|

**Fuente** : Estimación de emisiones atmosféricas.

34

##### 4.1.3. Fase de Cierre

La fase de cierre tiene una duración de 1 año. A continuación, se presenta una tabla
resumen de las actividades y cuales gases y material particulado emiten.

**Tabla 14. Fuentes de emisión durante la fase de cierre del proyecto.**

|Actividad|Fuente|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Actividad**|**MP10**|**MP2,5**|**MPS**|**NO2**|**SO2**|**CO**|**TRS**|
|Demolición|X|X|X|--|--|--|--|
|Escarpe|X|X|X|--|--|--|--|
|Excavaciones|X|X|X|--|--|--|--|
|Nivelación|X|X|X|--|--|--|--|
|Compactación|X|X|X|--|--|--|--|
|Transferencia de material|X|X|X|--|--|--|--|
|Transito caminos pavimentados|X|X|X|--|--|--|--|
|Transito caminos no pavimentados|X|X|X|--|--|--|--|
|Combustión vehicular por caminos pavimentados|X|X|X|X|X|X|--|
|Combustión vehicular por caminos no pavimentados|X|X|X|X|X|X|--|
|Combustión de maquinarias|X|X|X|X|X|X|--|
|Combustión grupos electrógenos|X|X|X|X|X|X|--|

**Fuente** : Estimación de emisiones atmosféricas.

35

##### 4.2. Resultados Inventario de Emisión

En esta sección se presenta el inventario de emisiones de las diferentes fases del proyecto, acorde al documento Estimación de

emisiones atmosféricas.

##### 4.2.1. Fase de Construcción

Tal como se menciona previamente, la fase de construcción tiene una duración de 21 meses. Las actividades están distribuidas en dos
años, estimando un inicio de actividades en abril del 2024.

**Tabla 15. Inventario de emisiones de la fase de construcción** **-** **Mes 4 al mes 12 (año 2024).**

|Actividad|SO<br>2|NO<br>x|CO|MP<br>2,5|MP<br>10|PTS|TRS|Unidad|
|---|---|---|---|---|---|---|---|---|
|Demoliciones|0|0|0|0,065|0,652|2,153|0|t/año|
|Escarpe|0|0|0|0,004|0,026|0,026|0|t/año|
|Excavación|0|0|0|0,036|0,066|0,338|0|t/año|
|Nivelación|0|0|0|0,002|0,019|0,064|0|t/año|
|Compactación|0|0|0|0,001|0,002|0,010|0|t/año|
|Transferencia de Material|0|0|0|0|0,001|0,003|0|t/año|
|Maquinaria Fuera de Ruta|0,002|1,252|1,015|0,115|0,115|0,115|0|t/año|
|Grupos Electrógenos|0,002|0,034|0,007|0,002|0,002|0,002|0|t/año|
|Transito Camino Pavimentado|0|0|0|0,283|1,168|6,084|0|t/año|
|Combustión Vehicular Camino Pavimentado|0,006|3,364|0,102|0,021|0,021|0,021|0|t/año|
|Transito Camino No Pavimentado|0|0|0|0,267|2,667|9,333|0|t/año|
|Combustión Vehicular Camino No Pavimentado|0|0,037|0,001|0|0|0|0|t/año|
|**Total**|**0,010**|**4,687**|**1,126**|**0,796**|**4,740**|**18,150**|**0 **|**t/año**|

**Fuente** : Estimación de emisiones atmosféricas.

36

**Tabla 16. Inventario de emisiones de la fase de construcción** **-** **Mes 13 al mes 24 (año 2025)**

|Actividad|SO<br>2|NO<br>x|CO|MP<br>2,5|MP<br>10|PTS|TRS|Unidad|
|---|---|---|---|---|---|---|---|---|
|Demoliciones|0|0|0|0,078|0,784|2,587|0|t/año|
|Escarpe|0|0|0|0|0|0|0|t/año|
|Excavación|0|0|0|0|0|0|0|t/año|
|Nivelación|0|0|0|0|0|0|0|t/año|
|Compactación|0|0|0|0|0|0|0|t/año|
|Transferencia de Material|0|0|0|0|0|0|0|t/año|
|Maquinaria Fuera de Ruta|0,007|4,856|3,668|0,391|0,391|0,391|0|t/año|
|Grupos Electrógenos|0,002|0,034|0,007|0,002|0,002|0,002|0|t/año|
|Transito Camino Pavimentado|0|0|0|0,227|0,937|4,880|0|t/año|
|Combustión Vehicular Camino Pavimentado|0,005|2,436|0,081|0,016|0,016|0,016|0|t/año|
|Transito Camino No Pavimentado|0,000|0,000|0,000|0,187|1,873|6,556|0|t/año|
|Combustión Vehicular Camino No Pavimentado|0,000|0,026|0,001|0|0|0|0|t/año|
|**Total**|**0,014**|**7,352**|**3,757**|**0,902**|**4,003**|**14,432**|**0 **|**t/año**|

**Fuente** : Estimación de emisiones atmosféricas.

##### 4.2.2. Fase de Operación

La fase de operación está dividida en operación base, la cual corresponde a la operación actual de la planta y en operación proyectada.
La operación proyectada parte el segundo semestre del año 2025, por lo que se estima inicia actividades en julio.

Los inventarios de emisión que se presentan corresponden a 1 año de operación.

##### 4.2.2.1. Operación Base

En la fase de operación base, la planta de CMPC Pulp SpA opera 350 días al año.

37

**Tabla 17. Inventario de emisiones de la fase de operación base** **-** **Emisiones de 1 año.**

|Actividad|SO<br>2|NO<br>x|CO|MP<br>2,5|MP<br>10|PTS|TRS|Unidad|
|---|---|---|---|---|---|---|---|---|
|Transferencia de Material|0|0|0|0,001|0,004|0,008|0|t/año|
|Maquinaria Fuera de Ruta|0,138|89,024|71,141|8,799|8,799|8,799|0|t/año|
|Erosión Eólica|0|0|0|0,009|0,057|0,113|0|t/año|
|Molienda Biomasa|0|0|0|0,360|0,360|3,600|0|t/año|
|Transporte Ferrocarril|0,479|6,903|1,027|0,257|0,257|0,257|0|t/año|
|Grupos Electrógenos|0,099|1,066|0,235|0,060|0,060|0,060|0|t/año|
|Fuentes Fijas|751,608|1.043,318|1.379,701|442,760|490,180|932,940|13,140|t/año|
|Transito Camino Pavimentado|0|0|0|0,321|1,327|6,915|0|t/año|
|Combustión Vehicular Camino Pavimentado|0,006|3,210|0,106|0,022|0,022|0,022|0|t/año|
|Transito Camino No Pavimentado|0|0|0|0,661|6,614|23,149|0|t/año|
|Combustión Vehicular Camino No Pavimentado|0|0,067|0,002|0|0|0|0|t/año|
|**Total**|**752,330**|**1.143,589**|**1.452,212**|**453,250**|**507,680**|**975,863**|**13,140**|**t/año**|

**Fuente** : Estimación de emisiones atmosféricas.

##### 4.2.2.2. Operación Proyectada

En la fase de operación proyectada, la planta de CMPC Pulp SpA opera 365 días al año.

**Tabla 18. Inventario de emisiones de la fase de operación proyectada** **-** **Emisiones de 1 año.**

|Actividad|SO<br>2|NO<br>x|CO|MP<br>2,5|MP<br>10|PTS|TRS|Unidad|
|---|---|---|---|---|---|---|---|---|
|Transferencia de Material|0|0|0|0,001|0,004|0,009|0|t/año|
|Maquinaria Fuera de Ruta|0,149|95,576|75,903|9,458|9,458|9,458|0|t/año|
|Erosión Eólica|0|0|0|0,009|0,057|0,113|0|t/año|
|Molienda Biomasa|0|0|0|0,360|0,360|3,600|0|t/año|
|Transporte Ferrocarril|0,479|7,831|1,166|0,291|0,291|0,291|0|t/año|
|Grupos Electrógenos|0,099|1,066|0,235|0,060|0,060|0,060|0|t/año|
|Fuentes Fijas|835,120|1.159,242|1.533,001|491,955|544,645|1.036,600|14,600|t/año|
|Transito Camino Pavimentado|0|0|0|0,339|1,402|7,302|0|t/año|
|Combustión Vehicular Camino Pavimentado|0,006|3,387|0,112|0,023|0,023|0,023|0|t/año|
|Transito Camino No Pavimentado|0|0|0|0,661|6,614|23,149|0|t/año|

38

|Actividad|SO<br>2|NO<br>x|CO|MP<br>2,5|MP<br>10|PTS|TRS|Unidad|
|---|---|---|---|---|---|---|---|---|
|Combustión Vehicular Camino No Pavimentado|0|0,067|0,002|0|0|0|0|t/año|
|**Total**|**835,853**|**1.267,170**|**1.610,418**|**503,158**|**562,914**|**1.080,605**|**14,600**|**t/año**|

**Fuente** : Estimación de emisiones atmosféricas.

##### 4.2.2.3. Incremento de las emisiones fase de operación

Se presenta el delta de la fase de operación, correspondiente al incremento de la tasa de emisión con respecto a la situación actual.

**Tabla 19. Inventario de emisiones** **-** **Incremento emisión de Fase de operación (1 año).**

|Actividad|SO2|NOx|CO|MP2,5|MP10|PTS|TRS|Unidad|
|---|---|---|---|---|---|---|---|---|
|Transferencia de Material|0|0|0|0|0|0|0|t/año|
|Maquinaria Fuera de Ruta|0,010|6,552|4,762|0,659|0,659|0,659|0|t/año|
|Erosión Eólica|0|0|0|0|0|0|0|t/año|
|Molienda Biomasa|0|0|0|0|0|0|0|t/año|
|Transporte Ferrocarril|0|0,928|0,138|0,035|0,035|0,035|0|t/año|
|Grupos Electrógenos|0|0|0|0|0|0|0|t/año|
|Fuentes Fijas|83,512|115,924|153,300|49,196|54,464|103,660|1,460|t/año|
|Transito Camino Pavimentado|0|0|0|0,018|0,074|0,387|0|t/año|
|Combustión Vehicular Camino Pavimentado|0|0,177|0,006|0,001|0,001|0,001|0|t/año|
|Transito Camino No Pavimentado|0|0|0|0|0|0|0|t/año|
|Combustión Vehicular Camino No Pavimentado|0|0|0|0|0|0|0|t/año|
|**Total**|**83,523**|**123,581**|**158,206**|**49,908**|**55,233**|**104,741**|**1,460**|**t/año**|

**Fuente** : Anexo 1.

##### 4.2.3. Fase de Cierre

A continuación, se presenta el inventario de emisiones de la fase de cierre.

39

**Tabla 20. Inventario de emisiones de la fase de cierre** **-** **Emisiones de 1 año.**

|Actividad|SO2|NOx|CO|MP2,5|MP10|PTS|Unidad|
|---|---|---|---|---|---|---|---|
|Demoliciones|0|0|0|0,265|2,647|8,736|t/año|
|Escarpe|0|0|0|0,007|0,048|0,048|t/año|
|Excavación|0|0|0|0,066|0,122|0,623|t/año|
|Nivelación|0|0|0|0,004|0,034|0,118|t/año|
|Compactación|0|0|0|0,002|0,004|0,018|t/año|
|Transferencia de Material|0|0|0|0,000|0,002|0,005|t/año|
|Maquinaria Fuera de Ruta|0,017|11,258|8,631|0,933|0,933|0,933|t/año|
|Grupos Electrógenos|0,008|0,125|0,027|0,009|0,009|0,009|t/año|
|Transito Camino Pavimentado|0|0|0|0,895|3,701|19,280|t/año|
|Combustión Vehicular Camino Pavimentado|0,019|10,689|0,338|0,068|0,068|0,068|t/año|
|Transito Camino No Pavimentado|0|0|0|0,683|6,832|23,910|t/año|
|Combustión Vehicular Camino No Pavimentado|0,000|0,115|0,003|0,001|0,001|0,001|t/año|
|**Total**|**0,044**|**22,187**|**9,000**|**2,933**|**14,400**|**53,748**|**t/año**|

**Fuente** : Anexo 1.

##### 4.3. Escenarios

Para determinar los escenarios a evaluar, se considera un año de emisiones atmosféricas. El impacto en los receptores discretos se
determina de la siguiente manera:

Concentración total

= Línea base en estación de monitoreo+ Aporte otros proyectos en la estación de monitoreo
+ aporte del proyecto

##### 4.3.1. Escenario 1

Para la determinación del escenario 1, se consideró determinar la alternativa en la cual se produce la mayor tasa de emisión:

40

 - Alternativa 1: Abril a diciembre 2024 de la fase de construcción (Documento Estimación de emisiones atmosféricas).

 - Alternativa 2: Enero a diciembre 2025 de la fase de construcción y julio a diciembre 2025 del incremento de emisión de la fase

de operación (Documento Estimación de emisiones atmosféricas).

 - Alternativa 3: Los primeros 12 meses de las emisiones de la fase de construcción (Anexo 1).

 - Alternativa 4: Los meses 13 al 21 de la fase de construcción y los meses 16 al 24 del incremento de emisión de la fase de

operación (Anexo 1).

A continuación, se presenta un cronograma de las distribuciones temporales de las alternativas disponibles para determinar el periodo
con la mayor tasa de emisión.

**Tabla 21. Cronograma de alternativas a evaluar para el escenario 1.**

|Fase|2024|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|2025|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|2026|Col27|Col28|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase**|**ENE**|**FEB**|**MAR**|**ABR**|**MAY**|**JUN**|**JUL**|**AGO**|**SEPT**|**OCT**|**NOV**|**DIC**|**ENE**|**FEB**|**MAR**|**ABR**|**MAY**|**JUN**|**JUL**|**AGO**|**SEPT**|**OCT**|**NOV**|**DIC**|**ENE**|**FEB**|**MAR**|
|Construcción||||||||||||||||||||||||||||
|Operación<br>proyectada||||||||||||||||||||||||||||
|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|**Alternativas de evaluación para análisis del escenario 1**|
|Alternativa 1||||Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024|Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024|Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024|Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024|Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024|Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024|Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024|Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024|Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024||||||||||||||||
|Alternativa 2|||||||||||||Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025|Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025|Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025|Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025|Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025|Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025|Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025|Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025|Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025|Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025|Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025|Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025||||
|Alternativa 3||||Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12)|Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12)|Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12)|Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12)|Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12)|Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12)|Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12)|Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12)|Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12)|Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12)|Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12)|Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12)|||||||||||||
|Alternativa 4||||||||||||||||Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24)|Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24)|Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24)|Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24)|Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24)|Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24)|Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24)|Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24)|Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24)|Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24)|Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24)|Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24)|

**Fuente** : Anexo 1.

La tasa de emisión del material particulado y cada uno de los gases se presenta en la siguiente tabla.

**Tabla 22. Alternativas de análisis del escenario 1.**

|Alternativa|SO<br>2|NO<br>x|CO|MP<br>2,5|MP<br>10|PTS|TRS|Unidad|
|---|---|---|---|---|---|---|---|---|
|**1 **|**0,010**|**4,687**|**1,126**|**0,796**|**4,740**|**18,150**|**0,000**|**t/año**|
|**2 **|**41,775**|**69,142**|**82,860**|**25,856**|**31,620**|**66,803**|**0,730**|**t/año**|
|**3 **|**0,013**|**6,626**|**2,147**|**1,089**|**6,337**|**23,707**|**0,000**|**t/año**|
|**4 **|**62,653**|**98,097**|**121,391**|**38,040**|**43,831**|**87,432**|**1,095**|**t/año**|

41

De las cuatro alternativas presentadas, la número 4 corresponde a aquella que presenta las mayores tasas de emisión a evaluar, por
la que corresponde a la alternativa seleccionada. A continuación, se presenta un desglose de las actividades y su emisión durante el

escenario 1.

**Tabla 23. Inventario de emisiones** **-** **Fase de construcción meses 13 al 21.**

|Actividad|SO<br>2|NO<br>x|CO|MP<br>2,5|MP<br>10|PTS|TRS|Unidad|
|---|---|---|---|---|---|---|---|---|
|Demoliciones|0|0|0|0|0|0|0|ton/año|
|Escarpe|0|0|0|0|0|0|0|ton/año|
|Excavación|0|0|0|0|0|0|0|ton/año|
|Nivelación|0|0|0|0|0|0|0|ton/año|
|Compactación|0|0|0|0|0|0|0|ton/año|
|Transferencia de Material|0|0|0|0|0|0|0|ton/año|
|Maquinaria Fuera de Ruta|0,005|3,532|2,668|0,284|0,284|0,284|0|ton/año|
|Grupos Electrógenos|0,002|0,034|0,007|0,002|0,002|0,002|0|ton/año|
|Transito Camino Pavimentado|0|0|0|0,170|0,702|3,660|0|ton/año|
|Combustión Vehicular Camino Pavimentado|0,003|1,827|0,061|0,012|0,012|0,012|0|ton/año|
|Transito Camino No Pavimentado|0|0|0|0,140|1,405|4,917|0|ton/año|
|Combustión Vehicular Camino No Pavimentado|0|0,019|0,001|0|0|0|0|ton/año|
|**Total**|**0,011**|**5,412**|**2,736**|**0,609**|**2,406**|**8,876**|**0 **|ton/año|

**Fuente** : Anexo 1.

**Tabla 24. Inventario de emisiones** **-** **Incremento de emisión de la fase de operación meses 16 al 24.**

42

|Actividad|SO2|NOx|CO|MP2,5|MP10|PTS|TRS|Unidad|
|---|---|---|---|---|---|---|---|---|
|Transferencia de Material|0|0|0|0|0|0|0|ton/año|
|Maquinaria Fuera de Ruta|0,008|4,914|3,572|0,494|0,494|0,494|0|ton/año|
|Erosión Eólica|0|0|0|0|0|0|0|ton/año|
|Molienda Biomasa|0|0|0|0|0|0|0|ton/año|
|Transporte Ferrocarril|0|0,696|0,104|0,026|0,026|0,026|0|ton/año|
|Grupos Electrógenos|0|0|0|0|0|0|0|ton/año|
|Fuentes Fijas|62,634|86,943|114,975|36,897|40,848|77,745|1,095|ton/año|
|Transito Camino Pavimentado|0,000|0,000|0,000|0,013|0,056|0,290|0|ton/año|
|Combustión Vehicular Camino Pavimentado|0,000|0,133|0,004|0,001|0,001|0,001|0|ton/año|
|Transito Camino No Pavimentado|0|0|0|0|0|0|0|ton/año|
|Combustión Vehicular Camino No Pavimentado|0|0|0|0|0|0|0|ton/año|

|Actividad|SO2|NOx|CO|MP2,5|MP10|PTS|TRS|Unidad|
|---|---|---|---|---|---|---|---|---|
|**Total**|**62,642**|** 92,686**|**118,655**|**37,431**|**41,425**|**78,556**|**1,095**|**ton/año**|

**Fuente** : Anexo 1.

##### 4.3.2. Escenario 2

El escenario 2 corresponde al incremento de la emisión de la fase de operación, la cual genera el incremento de las emisiones con
respecto a la situación actual. A continuación, se presenta el desglose de las emisiones con respecto a las actividades.

**Tabla 25. Inventario de emisiones** **-** **Incremento de la emisión de la Fase de operación (1 año).**

|Actividad|SO2|NOx|CO|MP2,5|MP10|PTS|TRS|Unidad|
|---|---|---|---|---|---|---|---|---|
|Transferencia de Material|0|0|0|0|0|0|0|t/año|
|Maquinaria Fuera de Ruta|0,010|6,552|4,762|0,659|0,659|0,659|0|t/año|
|Erosión Eólica|0|0|0|0|0|0|0|t/año|
|Molienda Biomasa|0|0|0|0|0|0|0|t/año|
|Transporte Ferrocarril|0|0,928|0,138|0,035|0,035|0,035|0|t/año|
|Grupos Electrógenos|0|0|0|0|0|0|0|t/año|
|Fuentes Fijas|83,512|115,924|153,300|49,196|54,464|103,660|1,460|t/año|
|Transito Camino Pavimentado|0|0|0|0,018|0,074|0,387|0|t/año|
|Combustión Vehicular Camino Pavimentado|0|0,177|0,006|0,001|0,001|0,001|0|t/año|
|Transito Camino No Pavimentado|0|0|0|0|0|0|0|t/año|
|Combustión Vehicular Camino No Pavimentado|0|0|0|0|0|0|0|t/año|
|**Total**|**83,523**|**123,581**|**158,206**|**49,908**|**55,233**|**104,741**|**1,460**|**t/año**|

**Fuente** : Anexo 1.

##### 4.3.3. Escenario 3

El escenario 3 corresponde a la fase de cierre. A continuación, se presenta el desglose de las emisiones con respecto a las actividades.

**Tabla 26. Inventario de emisiones** **-** **Fase de cierre (1 año).**

43

|Actividad|SO2|NOx|CO|MP2,5|MP10|PTS|Unidad|
|---|---|---|---|---|---|---|---|
|Demoliciones|0|0|0|0,265|2,647|8,736|t/año|
|Escarpe|0|0|0|0,007|0,048|0,048|t/año|
|Excavación|0|0|0|0,066|0,122|0,623|t/año|

|Actividad|SO2|NOx|CO|MP2,5|MP10|PTS|Unidad|
|---|---|---|---|---|---|---|---|
|Nivelación|0|0|0|0,004|0,034|0,118|t/año|
|Compactación|0|0|0|0,002|0,004|0,018|t/año|
|Transferencia de Material|0|0|0|0,000|0,002|0,005|t/año|
|Maquinaria Fuera de Ruta|0,017|11,258|8,631|0,933|0,933|0,933|t/año|
|Grupos Electrógenos|0,008|0,125|0,027|0,009|0,009|0,009|t/año|
|Transito Camino Pavimentado|0|0|0|0,895|3,701|19,280|t/año|
|Combustión Vehicular Camino Pavimentado|0,019|10,689|0,338|0,068|0,068|0,068|t/año|
|Transito Camino No Pavimentado|0|0|0|0,683|6,832|23,910|t/año|
|Combustión Vehicular Camino No Pavimentado|0,000|0,115|0,003|0,001|0,001|0,001|t/año|
|**Total**|**0,044**|**22,187**|**9,000**|**2,933**|**14,400**|**53,748**|**t/año**|

**Fuente** : Anexo 1.

##### 4.4. Nivel de Actividad de los escenarios

En esta sección se presenta el nivel de actividad de los escenarios seleccionados y el factor de variación de la emisión.

##### 4.4.1. Escenario 1

Se presenta el nivel de actividad para las fuentes difusas, puntuales y de ruta del escenario 1.

**Tabla 27. Nivel de actividad para fuente difusa** **-** **Escenario 1 Fase de construcción.**

|ID|Localización|Fuente|Emisiones|Tipo de<br>fuente|Área<br>(m2)|Altura de la fuente<br>(m)|Meses<br>emite|Periodo emisión|
|---|---|---|---|---|---|---|---|---|
|Comb_maq|Superficie|Combustión<br>de<br>maquinarias|MP10, MP2,5, MPS, NO2, SO2 y CO.|Difusa|12659|1|Mes 13 al 20|Lunes a sábado de 08:00 a 16:00 (UTC-4).|

**Tabla 28. Nivel de actividad para fuente puntual** **-** **Escenario 1 Fase de construcción.**

|ID|Localización|Fuente|Emisiones|Tipo de<br>fuente|N° equipos|Temperatura<br>(K)|Diámetro<br>(m)|Altura<br>de la<br>fuente<br>(m)|Velocidad<br>de<br>emisión<br>(m/s)|Meses<br>emite|Periodo emisión|
|---|---|---|---|---|---|---|---|---|---|---|---|
|GE_11|Grupos<br>electrógenos|Grupos<br>electrógenos|MP10, <br>MP2,5, <br>MPS,<br>NO2, SO2 y CO.|Puntual|2|838,15|0,0635|1,9|77|Mes 20|Lunes a sábado de 11:00 a 19:00(UTC-4).|

44

**Tabla 29. Nivel de actividad para fuentes de ruta** **-** **Escenario 1 Fase de construcción.**

|ID|Fuente|Emisiones|Tipo de<br>fuente|Distancia<br>total (km)|Altura de<br>la fuente<br>(m)|Meses<br>emite|Periodo emisión|
|---|---|---|---|---|---|---|---|
|ID1|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 1|MP10, MP2,5, MPS, NO2, SO2 y CO.|Ruta|159.726|1|Mes 13 al 21|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID2|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 2|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|149.917|1|Mes 13 al 21|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID3|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 3|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|6.674|1|Mes 13 al 21|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID4|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 4|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|45.169|1|Mes 13 al 21|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID5|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 5|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|6.680|1|Mes 13 al 21|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID6|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 6|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|116.422|1|Mes 13 al 21|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID7|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 7|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|12.688|1|Mes 13 al 21|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID8|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 8|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|19.135|1|Mes 13 al 21|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID9|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 9|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|729|1|Mes 13 al 21|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID10|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 10|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|504|1|Mes 13 al 21|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID11|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 11|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|2.127|1|Mes 13 al 21|Lunes a sábado de 08:00 a 18:00(UTC-4).|

45

|ID|Fuente|Emisiones|Tipo de<br>fuente|Distancia<br>total (km)|Altura de<br>la fuente<br>(m)|Meses<br>emite|Periodo emisión|
|---|---|---|---|---|---|---|---|
|ID12|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 12|MP10, MP2,5, MPS, NO2, SO2 y CO.||2.452|1|Mes 13 al 21|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID13|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 13|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|576|1|Mes 13 al 21|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID15|Tránsito<br>y <br>combustión<br>caminos no pavimentados -<br>Ruta ID15|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|4.202|1|Mes 13 al 21|Lunes a sábado de 08:00 a 18:00(UTC-4).|

**Tabla 30. Nivel de actividad para fuente difusa** **-** **Escenario 1 Incremento de la emisión de la Fase de operación.**

|ID|Localización|Fuente|Emisiones|Tipo de<br>fuente|Área<br>(m2)|Altura de la fuente<br>(m)|Meses<br>emite|Periodo<br>emisión|
|---|---|---|---|---|---|---|---|---|
|Prep_11|Preparación<br>madera|Combustión<br>maquinarias|MP10, MP2,5, MPS, NO2, SO2 y CO.|Difusa|20.527|1|Mes 16 al 24|24/7.|

**Tabla 31. Nivel de actividad para fuentes puntuales** **-** **Escenario 1 Incremento de la emisión de la Fase de operación.**

|ID|Fuente|Emisiones|Tipo de<br>fuente|N°<br>equipos|Temperatura<br>(K)|Diámetro<br>(m)|Altura de la<br>fuente (m)|Velocidad de<br>emisión (m/s)|Meses emite|Periodo<br>emisión|
|---|---|---|---|---|---|---|---|---|---|---|
|CB3|Caldera biomasa<br>N°3|MP10, MP2,5, MPS, NO2, SO2, CO y TRS.|Puntual|1|417,15|2,25|75,8|25,3|Mes 16 al 24.|24/7.|
|CR6|Caldera<br>recuperadora<br>N°6|MP10, MP2,5, MPS, NO2, SO2, CO y TRS.|MP10, MP2,5, MPS, NO2, SO2, CO y TRS.|1|428,15|3,6|80|20,6|Mes 16 al 24.|24/7.|
|HC3|Horno cal N°3|MP10, MP2,5, MPS, NO2, SO2, CO y TRS.|MP10, MP2,5, MPS, NO2, SO2, CO y TRS.|1|534,15|1,6|60|11|Mes 16 al 24.|24/7.|

**Tabla 32. Nivel de actividad para fuentes de ruta** **-** **Escenario 1 Incremento de la emisión de la Fase de operación.**

|ID|Fuente|Emisiones|Tipo de<br>fuente|Distancia<br>total (km)|Altura de la<br>fuente (m)|Meses<br>emite|Periodo emisión|
|---|---|---|---|---|---|---|---|
|ID1|Tránsito<br>y <br>combustión<br>caminos<br>pavimentados<br>- <br>Ruta ID 1|MP10, MP2,5, MPS, NO2, SO2 y CO.|Ruta|18.710|1|Mes 16 al 24|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID2|Tránsito<br>y <br>combustión<br>caminos<br>pavimentados<br>- <br>Ruta ID 2|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|18.339|1|Mes 16 al 24|Lunes a sábado de 08:00 a 18:00(UTC-4).|

46

|ID|Fuente|Emisiones|Tipo de<br>fuente|Distancia<br>total (km)|Altura de la<br>fuente (m)|Meses<br>emite|Periodo emisión|
|---|---|---|---|---|---|---|---|
|ID4|Tránsito<br>y <br>combustión<br>caminos<br>pavimentados<br>- <br>Ruta ID 4|MP10, MP2,5, MPS, NO2, SO2 y CO.||3.688|1|Mes 16 al 24|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID9|Tránsito<br>y <br>combustión<br>caminos<br>pavimentados<br>- <br>Ruta ID 9|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|47|1|Mes 16 al 24|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID11|Tránsito<br>y <br>combustión<br>caminos<br>pavimentados<br>- <br>Ruta ID 11|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|47|1|Mes 16 al 24|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID12|Tránsito<br>y <br>combustión<br>caminos<br>pavimentados<br>- <br>Ruta ID 12|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|248|1|Mes 16 al 24|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|Ferr_11_par|Transporte en ferrocarril -<br>Laja a Lirquén|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|630|1|Mes 16 al 24|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|Ferr_11_par|Transporte en ferrocarril -<br>Laja a Coronel|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|1.527|1|Mes 16 al 24|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|Ferr_11_par|Transporte en ferrocarril -<br>Laja a San Vicente|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|261|1|Mes 16 al 24|Lunes a sábado de 08:00 a 18:00(UTC-4).|

47

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml.
**Figura 3. Geolocalización de fuentes puntuales y difusas** **-** **Fase de construcción Escenario 1.**

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml.
**Figura 4. Geolocalización de fuentes de ruta** **-** **Fase de construcción Escenario 1.**

48

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml.
**Figura 5. Geolocalización de fuentes puntuales y difusas** **-** **Incremento de la emisión de la Fase de**

**operación Escenario 1.**

Para efectos de la modelación, en el incremento de la emisión de la de la fase de operación

solo se considera la ruta ferroviaria dentro del dominio de simulación y se estima que emite

la tasa de emisión de todas las rutas ferroviarias. Con el objetivo de no evaluar las

condiciones de borde del dominio, las cuales no representan adecuadamente la

meteorología, la ruta dentro del dominio modelado se limita hasta 5 km del borde del

dominio.

49

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml.

**-**
**Figura 6. Geolocalización de fuentes de ruta** **Incremento de la emisión de la Fase de operación Escenario**

**1**

##### 4.4.2. Escenario 2

Se presenta el nivel de actividad para las fuentes difusas, puntuales y de ruta del escenario

2.

**Tabla 33. Nivel de actividad para fuente difusa** **-** **Escenario 2 Incremento de la emisión de la Fase de**

**operación.**

|ID|Localización|Fuente|Emisiones|Tipo de<br>fuente|Área<br>(m2)|Altura de<br>la fuente<br>(m)|Meses<br>emite|Periodo<br>emisión|
|---|---|---|---|---|---|---|---|---|
|Prep_11|Preparación<br>madera|Combustión<br>maquinaria<br>s|MP10, MP2,5, MPS, NO2, <br>SO2 y CO.|Difusa|20.527|1|Todo<br>el año|24/7.|

50

**Tabla 34. Nivel de actividad para fuentes puntuales** **-** **Escenario 2 Incremento de la emisión de la Fase de operación.**

|ID|Fuente|Emisiones|Tipo de<br>fuente|N° equipos|Temperatura<br>(K)|Diámetro<br>(m)|Altura de<br>la fuente<br>(m)|Velocidad<br>de emisión<br>(m/s)|Meses<br>emite|Periodo<br>emisión|
|---|---|---|---|---|---|---|---|---|---|---|
|CB3|Caldera<br>biomasa N°3|MP10, MP2,5, MPS, NO2, SO2, CO y<br>TRS.|Puntual|1|417,15|2,25|75,8|25,3|Todo el año.|24/7.|
|CR6|Caldera<br>recuperadora<br>N°6|MP10, MP2,5, MPS, NO2, SO2, CO y<br>TRS.|MP10, MP2,5, MPS, NO2, SO2, CO y<br>TRS.|1|428,15|3,6|80|20,6|Todo el año.|24/7.|
|HC3|Horno cal N°3|MP10, MP2,5, MPS, NO2, SO2, CO y<br>TRS.|MP10, MP2,5, MPS, NO2, SO2, CO y<br>TRS.|1|534,15|1,6|60|11|Todo el año.|24/7.|

**Tabla 35. Nivel de actividad para fuentes de ruta - Escenario 2 Incremento de la emisión de la Fase de operación.**

|ID|Fuente|Emisiones|Tipo de<br>fuente|Distancia<br>total (km)|Altura de la<br>fuente (m)|Meses<br>emite|Periodo emisión|
|---|---|---|---|---|---|---|---|
|ID1|Tránsito y combustión caminos<br>pavimentados - Ruta ID 1|MP10, MP2,5, MPS, NO2, SO2 y CO.|Ruta|24.947|1|Todo el año|Lunes a sábado de 08:00 a 18:00.|
|ID2|Tránsito y combustión caminos<br>pavimentados - Ruta ID 2|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|24.452|1|Todo el año|Lunes a sábado de 08:00 a 18:00.|
|ID4|Tránsito y combustión caminos<br>pavimentados - Ruta ID 4|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|4.918|1|Todo el año|Lunes a sábado de 08:00 a 18:00.|
|ID9|Tránsito y combustión caminos<br>pavimentados - Ruta ID 9|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|62,5608|1|Todo el año|Lunes a sábado de 08:00 a 18:00.|
|ID11|Tránsito y combustión caminos<br>pavimentados - Ruta ID 11|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|62|1|Todo el año|Lunes a sábado de 08:00 a 18:00.|
|ID12|Tránsito y combustión caminos<br>pavimentados - Ruta ID 12|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|331|1|Todo el año|Lunes a sábado de 08:00 a 18:00.|
|Ferr_11_par|Transporte en ferrocarril - Laja a<br>Lirquén|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|840|1|Todo el año|Lunes a sábado de 08:00 a 18:00.|
|Ferr_11_par|Transporte en ferrocarril - Laja a<br>Coronel|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|2.036|1|Todo el año|Lunes a sábado de 08:00 a 18:00.|
|Ferr_11_par|Transporte en ferrocarril - Laja a<br>San Vicente|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|347|1|Todo el año|Lunes a sábado de 08:00 a 18:00.|

51

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml.
**Figura 7. Geolocalización de fuentes puntuales y difusas** **-** **Incremento de la emisión de la Fase de**

**operación Escenario 2.**

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml.

**-**
**Figura 8. Geolocalización de fuentes de ruta** **Incremento de la emisión de la Fase de operación Escenario**

**2.**

52

##### 4.4.3. Escenario 3

Se presenta el nivel de actividad para las fuentes difusas, puntuales y de ruta del escenario 3.

**Tabla 36. Nivel de actividad para fuentes difusas** **-** **Escenario 3 Fase de cierre.**

|ID|Localización|Fuente|Emisiones|Tipo<br>de<br>fuente|Área<br>(m2)|Altura<br>de la<br>fuente<br>(m)|Meses emite|Periodo emisión|
|---|---|---|---|---|---|---|---|---|
|Comb_maq|Superficie|Combustión<br>de<br>maquinarias<br>y <br>Transferencia de<br>material|MP10, MP2,5, MPS, NO2, SO2 y CO.|Difusa|12659|1|Mes 1 al 12|Lunes a sábado de 08:00 a 16:00 (UTC-4).|
|Ev11|Evaporador|Demolición|MP10, MP2,5, MPS.|MP10, MP2,5, MPS.|390|1|Mes 2 a 11 (excluido)|Lunes a sábado de 08:00 a 16:00 (UTC-4).|
|Ca11|Caldera|Demolición|MP10, MP2,5, MPS.|MP10, MP2,5, MPS.|488|1|Mes 2 a 11 (excluido)|Lunes a sábado de 08:00 a 16:00 (UTC-4).|
|Ba11|Batch|Demolición|MP10, MP2,5, MPS.|MP10, MP2,5, MPS.|114|1|Mes 2 a 11 (excluido)|Lunes a sábado de 08:00 a 16:00 (UTC-4).|
|Ho11|Horno|Demolición|MP10, MP2,5, MPS.|MP10, MP2,5, MPS.|155|1|Mes 2 a 11 (excluido)|Lunes a sábado de 08:00 a 16:00 (UTC-4).|
|Co45|Cota 45|Escarpe<br>y <br>excavaciones|MP10, MP2,5, MPS.|MP10, MP2,5, MPS.|21183|1|Mes 2 a 11 (excluido)|Lunes a sábado de 08:00 a 16:00 (UTC-4).|
|Su11|Superficie 1|Escarpe,<br>nivelación<br>y <br>compactación|MP10, MP2,5, MPS.|MP10, MP2,5, MPS.|13396|1|Mes 2 a 11 (excluido)|Lunes a sábado de 08:00 a 16:00 (UTC-4).|
|Ta11|Tall Oil|Excavaciones,<br>nivelación<br>y <br>compactación|MP10, MP2,5, MPS.|MP10, MP2,5, MPS.|462|1|Mes 2 a 11 (excluido)|Lunes a sábado de 08:00 a 16:00 (UTC-4).|
|Chi11|Chipscrinning|Excavaciones|MP10, MP2,5, MPS.|MP10, MP2,5, MPS.|127|1|Mes 2 a 11 (excluido)|Lunes a sábado de 08:00 a 16:00 (UTC-4).|

**Tabla 37. Nivel de actividad para fuente puntual** **-** **Escenario 3 Fase de cierre.**

|ID|Localización|Fuente|Emisiones|Tipo de<br>fuente|N° equipos|Temperatura<br>(K)|Diámetro<br>(m)|Altura<br>de la<br>fuente<br>(m)|Velocidad<br>de<br>emisión<br>(m/s)|Meses<br>emite|Periodo emisión|
|---|---|---|---|---|---|---|---|---|---|---|---|
|GE_11|Grupos<br>electrógenos|Grupos<br>electrógenos|MP10, <br>MP2,5, <br>MPS,<br>NO2, SO2 y CO.|Puntual|2|838,15|0,0635|1,9|77|Mes 1|Lunes a sábado de 11:00 a 19:00(UTC-4).|

53

**Tabla 38. Nivel de actividad para fuentes de ruta** **-** **Escenario 3 Fase de cierre.**

|ID|Fuente|Emisiones|Tipo de<br>fuente|Distancia<br>total (km)|Altura de<br>la fuente<br>(m)|Meses<br>emite|Periodo emisión|
|---|---|---|---|---|---|---|---|
|ID6|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 6|MP10, MP2,5, MPS, NO2, SO2 y CO.|Ruta|185.483|1|Mes 1 al 12|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID7|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 7|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|17.985|1|Mes 1 al 12|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID9|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 9|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|1.364|1|Mes 1 al 12|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID10|Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 10|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|1.139|1|Mes 1 al 12|Lunes a sábado de 08:00 a 18:00(UTC-4).|
|ID15|Tránsito<br>y <br>combustión<br>caminos no pavimentados -<br>Ruta ID15|MP10, MP2,5, MPS, NO2, SO2 y CO.|MP10, MP2,5, MPS, NO2, SO2 y CO.|9.375|1|Mes 1 al 12|Lunes a sábado de 08:00 a 18:00(UTC-4).|

54

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml.
**Figura 9. Geolocalización de fuentes puntuales y difusas** **-** **Fase de cierre Escenario 3.**

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml.
**Figura 10. Geolocalización de fuentes de ruta** **-** **Fase de cierre Escenario 3.**

55

##### 4.4.4. Factor de Variación de la emisión

En esta sección se presentan los factores de variación de la emisión en el escenario 1, 2 y 3,
de acuerdo al tipo de fuente que emite en las diferentes fases.

##### 4.4.4.1. Escenario 1

En el escenario 1, la fase de construcción y el incremento de la emisión de la de fase de
operación, poseen variación de la emisión para las fuentes difusas, fuentes puntuales y
fuentes ruta. A continuación, se presentan las tablas con la variación de la emisión.

**Tabla 39. Factor de variación de la emisión de fuentes ruta** **-** **Escenario 1 Fase de construcción.**

|Mes|Hora en UTC+00|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Mes**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**|**23**|
|1|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|2|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|3|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|4|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|5|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|6|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|7|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|8|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|9|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|10|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|11|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|12|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|

**Tabla 40. Factor de variación de la emisión de fuente difusa** **-** **Escenario 1 Fase de construcción.**

|Mes|Hora en UTC+00|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Mes**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**|**23**|
|1|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|
|2|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|
|3|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|
|4|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|5|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|6|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|7|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|8|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|9|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|10|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|11|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|12|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|

**Tabla 41. Factor de variación de la emisión de fuente puntual** **-** **Escenario 1 Fase de construcción.**

56

|Mes|Hora en UTC+00|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Mes**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**|**23**|
|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|2|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|3|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|4|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|5|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|6|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|7|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|

|Mes|Hora en UTC+00|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Mes**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**|**23**|
|8|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|
|9|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|10|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|11|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|12|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|

**Tabla 42. Factor de variación de la emisión de fuentes de ruta** **-** **Escenario 1 incremento de la emisión de la**

**Fase operación.**

|Mes|Hora en UTC+00|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Mes**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**|**23**|
|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|2|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|3|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|4|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|5|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|6|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|7|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|8|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|9|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|10|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|11|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|12|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|

**Tabla 43. Factor de variación de la emisión de fuente puntual** **-** **Escenario 1 incremento de la emisión de la**

**de Fase de operación.**

|Mes<br>1 2 3 4 5 6 7 8 9 10 11 12<br>0 0 0 1 1 1 1 1 1 1 1 1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Mes<br>1 2 3 4 5 6 7 8 9 10 11 12<br>0 0 0 1 1 1 1 1 1<br>1 <br>1 <br>1|2|3|4|5|6|7|8|9|10|11|12|
|Mes<br>1 2 3 4 5 6 7 8 9 10 11 12<br>0 0 0 1 1 1 1 1 1<br>1 <br>1 <br>1|0|0|1|1|1|1|1|1|1|1|1|

##### 4.4.4.2. Escenario 2

En el escenario 2, el incremento de la emisión de la de la fase de operación solo tiene
variación de la emisión de las fuentes de ruta. El resto de las fuentes emite 24/7.

**Tabla 44. Factor de variación de la emisión de fuentes de ruta** **-** **Escenario 2 incremento de la emisión de la**

**Fase operación.**

57

|Mes|Hora en UTC+00|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Mes**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**|**23**|
|1|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|2|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|3|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|4|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|5|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|6|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|7|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|8|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|9|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|10|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|11|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|12|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|

##### 4.4.4.3. Escenario 3

En el escenario 3, correspondiente a la fase de cierre, hay variación de la emisión para las
fuentes difusas, fuente puntual y fuentes de ruta. A continuación, se presentan las tablas

con la variación de la emisión.

**Tabla 45. Factor de variación de la emisión de la fuente puntual** **-** **Escenario 3 Fase de cierre.**

**-**

|Mes|Hora en UTC+00|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Mes**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**|**23**|
|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|
|2|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|3|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|4|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|5|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|6|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|7|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|8|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|9|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|10|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|11|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|12|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|

**Tabla 46. Factor de variación de la emisión de fuente difusa Cota 45, Tall Oil, Superficie 1 y Chipscrinning**

**Escenario 3 Fase de cierre.**

**-**

|Mes|Hora en UTC+00|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Mes**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**|**23**|
|1|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|
|2|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|3|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|4|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|5|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|6|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|7|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|8|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|9|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|10|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|11|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|12|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|

**Tabla 47. Factor de variación de la emisión de la fuente difusa evaporadores, caldera, batch y horno**

**Escenario 3 Fase de cierre.**

58

|Mes|Hora en UTC+00|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Mes**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**|**23**|
|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|2|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|
|3|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|

|Mes|Hora en UTC+00|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Mes**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**|**23**|
|4|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|5|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|6|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|7|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|8|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|9|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|10|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|
|11|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|12|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|

**Tabla 48. Factor de variación de la emisión de fuente difusa superficie 2** **-** **Escenario 3 Fase de cierre.**

|Mes|Hora en UTC+00|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Mes**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**|**23**|
|1|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|
|2|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|
|3|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|
|4|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|5|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|6|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|7|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|8|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|9|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|0|
|10|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|
|11|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|
|12|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|0|0|0|0|

**Tabla 49. Factor de variación de la emisión de las fuentes de ruta** **-** **Escenario 3 Fase de cierre.**

59

|Mes|Hora en UTC+00|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Mes**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**|**23**|
|1|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|2|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|3|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|4|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|5|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|6|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|7|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|8|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|9|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|0|
|10|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|11|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|
|12|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|0|0|

#### 5. Análisis meteorológico

Según los lineamientos indicados en la “ _Guía para el uso de modelos de calidad del aire_ ”

(2023), es imprescindible analizar la incertidumbre del modelo meteorológico para analizar

los resultados obtenidos de la dispersión de contaminantes respecto a la información

disponible. Para esto se contrastan los datos observados en una estación meteorológica

superficial dentro del dominio de simulación, con la serie de datos del modelo de pronóstico

WRF. Por lo tanto, en la presente sección se indica tanto la estación meteorológica de

referencia seleccionada, como los resultados del análisis de incertidumbre desarrollado.

##### 5.1. Selección de la estación meteorológica de referencia

La “ _Guía para el uso de modelos de calidad del aire_ ” (2023) recomienda escoger las

estaciones meteorológicas más representativas de la zona donde se ubican las fuentes de

emisión y receptores del proyecto para evaluar. Para eso se define una serie de criterios

que priorizan tanto la cercanía, asociada a la similitud de las condiciones meteorológicas

con el emplazamiento del proyecto, como la disponibilidad de datos. En este contexto el

APENDICE 3 - Selección de la estación meteorológica de referencia, indica la metodología

utilizada para la selección de dicha estación, desde donde se recoge que se identificaron las

estaciones disponibles en el dominio y se analizaron aquella dentro de un radio de 10 km

desde el centroide del perímetro de la planta y que no tuvieran apantallamiento, eligiendo

finalmente a la estación Laja, por ser la estación localizada a la menor distancia del

perímetro de la planta y con la mayor disponibilidad de datos observados. La ubicación se

indica en la Figura 11. Mientras que, en la Tabla 50 se presentan las principales

características de la estación meteorológica superficial identificada.

**Tabla 50. Ubicación de la estación meteorológica superficial.**

|Nombre<br>estación|Distancia<br>al<br>perímetro<br>del<br>proyecto<br>(km)|Altura<br>m.s.n.m<br>(m)2|Coordenadas UTM<br>Datum WGS 84 Huso<br>18|Col5|Variables meteorológicas1|Col7|Col8|Col9|% datos disponibles4|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Nombre**<br>**estación**|**Distancia**<br>**al**<br>**perímetro**<br>**del**<br>**proyecto**<br>**(km)**|**Altura**<br>**m.s.n.m**<br>**(m)2 **|**Este (m)**|**Norte (m)**|**T3 **|**VV3 **|**DV3 **|**Hr3 **|**Hr3 **|**Hr3 **|**Hr3 **|
|**Nombre**<br>**estación**|**Distancia**<br>**al**<br>**perímetro**<br>**del**<br>**proyecto**<br>**(km)**|**Altura**<br>**m.s.n.m**<br>**(m)2 **|**Este (m)**|**Norte (m)**|**T3 **|**VV3 **|**DV3 **|**Hr3 **|**2020**|**2021**|**2022**|
|**Laja**|1,83|68,33|702.992|5.872.963|√|√|√|√|96%|97,1%|95,3%|

1 Extraído del Sistema de Información Nacional de Calidad del Aire.

2 Extraído desde GRD generado en conjunto con el archivo WRF, el cual extrae datos desde GMTED2010 desde
[https://www.usgs.gov/coastal-changes-and-impacts/gmted2010](https://www.usgs.gov/coastal-changes-and-impacts/gmted2010)
3 Las siglas indican: temperatura (T), velocidad del viento (VV), dirección del viento (DV) y humedad relativa (Hr).
4 Estimado a partir de la disponibilidad de datos de velocidad del viento.

60

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 11. Ubicación de la estación meteorológica de referencia seleccionada.**

##### 5.2. Resultados análisis de incertidumbre

Por otro lado, la metodología y el detalle del análisis de incertidumbre para los 3 periodosde estudio se presenta en el APENDICE 4 Análisis meteorológico de Datos Observados y

Modelados, desde donde se extraen las variables de predicción indicadas en la Tabla 51.

Según esto se puede indicar:

 - De acuerdo a los criterios de aceptación definidos para la temperatura superficial en

la “ _Guía para el uso de modelos de calidad del aire en el SEIA_ ” (2023), para los 3 años

meteorológicos se cumplen con los criterios de aceptación para error absoluto

medio (MAE), sesgo estadístico (BIAS), error cuadrático medio (RMSE) y el

coeficiente de correlación (r). En el caso del RMSE de la temperatura, solamente en

el año 2020 el valor se escapó ligeramente de lo recomendado.

61

**Tabla 51. Valores de los índices de la predicción proporcionada por el modelo para la estación meteorológica** **-** **Años 2020 a 2022**

|Variable Meteorológica|2020|Col3|Col4|Col5|2021|Col7|Col8|Col9|2022|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Variable Meteorológica**|**RMSE**|**MAE**|**BIAS**|**r**|**RMSE**|**MAE**|**BIAS**|**r **|**RMSE**|**MAE**|**BIAS**|**r **|
|**Temperatura Superficial**|4,9 °C|4,0 °C|-3,7 °C|0,9|4,0 °C|3,1°C|-2,1°C|0,9|2,9 °C|2,3 °C|-0,4 °C|0,9|
|**Velocidad Viento**|1,5 m/s|1,1 m/s|0,9 m/s|0,6|1,7 m/s|1,3 m/s|1,1 m/s|0,6|1,5 m/s|1,1 m/s|0,8 m/s|0,6|

62

#### 6. Modelación de Calidad del Aire

En esta sección se presenta las normas aplicables, la línea base de calidad del aire, el nivel

de impacto significativo, la selección del modelo, análisis de proyectos aledaños, definición

de receptores y modelación de los impactos de calidad del aire para a MP 10, MP 2,5, SO 2, NO 2
y TRS en μg/m [3], MPS en mg/m [2] /d y en CO mg/m [3], en los escenarios definidos.

Cabe mencionar que las modelaciones presentadas en la presente sección, consideran la

mayor concentración y tasa de deposición en cada receptor, de los 3 años evaluados.

-
Por su parte, las isolineas de concentración se presentan en la sección APENDICE 7

Isolineas de concentración.

##### 6.1. Selección de la Normativa

Las concentraciones máximas anuales y diarias establecidas para Material Particulado Mp 2,5 y

MP 10 y los criterios de excedencia se presentan en la Tabla 52, mientras que en la Tabla 53 se

presentan para gases (NO 2, SO 2 y CO).

**Tabla 52. Normativas aplicables para material particulado.**

|Contaminante<br>normado|Decreto<br>aplicable|Periodo de<br>Evaluación de<br>Cumplimiento<br>de Norma|Concentración<br>máxima<br>permitida|Criterio de excedencia|
|---|---|---|---|---|
|**Material**<br>**Particulado**<br>**Respirable**<br>**Fino (MP2,5) **|D.S N° 12/2011<br>del Ministerio del<br>Medio Ambiente.|Anual|20 μg/m3N|Cuando el promedio de las concentraciones<br>anuales sea mayor a 20 (μg/m3N).|
|**Material**<br>**Particulado**<br>**Respirable**<br>**Fino (MP2,5) **|D.S N° 12/2011<br>del Ministerio del<br>Medio Ambiente.|24 h|50 μg/m3N|Cuando el percentil 98 de los promedios<br>diarios durante un año, sea mayor a 50<br>(μg/m3N).|
|**Material**<br>**Particulado**<br>**Respirable**<br>**(MP10) **|D.S N° 12/2022<br>del Ministerio del<br>Medio Ambiente.|Anual|50 μg/m3N|Cuando el promedio de las concentraciones<br>anuales sea mayor a 50 (μg/m3N).|
|**Material**<br>**Particulado**<br>**Respirable**<br>**(MP10) **|D.S N° 12/2022<br>del Ministerio del<br>Medio Ambiente.|24 h|130 μg/m3N|Cuando el percentil 98 de los promedios<br>diarios durante un año, sea mayor o igual<br>130 (μg/m3N).|

**Tabla 53. Normativas aplicables para gases.**

|Contaminante<br>normado|Decreto<br>aplicable|Periodo de<br>Evaluación de<br>Cumplimiento<br>de Norma|Concentración<br>máxima<br>permitida|Criterio de excedencia|
|---|---|---|---|---|
|**Dióxido de**<br>**Azufre (SO2)** <br>**Norma**<br>**Primario**|D.S N° 104/2018<br>del Ministerio del<br>Medio Ambiente.|Anual|60 μg/m3N|Cuando el promedio de las concentraciones<br>anuales sea mayor o igual a 60 (μg/m3N).|
|**Dióxido de**<br>**Azufre (SO2)** <br>**Norma**<br>**Primario**|D.S N° 104/2018<br>del Ministerio del<br>Medio Ambiente.|24 h|150 μg/m3N|Cuando el percentil 99 de los promedios<br>diarios durante un año, sea mayor o igual a<br>150 (μg/m3N).|
|**Dióxido de**<br>**Azufre (SO2)** <br>**Norma**<br>**Primario**|D.S N° 104/2018<br>del Ministerio del<br>Medio Ambiente.|1 h|350 μg/m3N|Si<br>en<br>un<br>año<br>calendario,<br>el<br>valor<br>correspondiente al percentil 98,5 de las<br>concentraciones de 1 hora, fuere mayor o<br>igual al doble del valor de la norma que se<br>establece.|
|**Dióxido de**<br>**Azufre (SO2)**|D.S N° 22/2009<br>del Ministerio de|Anual|60 μg/m3N|Cuando el promedio de las concentraciones<br>anuales sea mayor o igual a 60 (μg/m3N).|

63

|Contaminante<br>normado|Decreto<br>aplicable|Periodo de<br>Evaluación de<br>Cumplimiento<br>de Norma|Concentración<br>máxima<br>permitida|Criterio de excedencia|
|---|---|---|---|---|
|**Norma**<br>**Secundariaa **|la Secretaría<br>General de la<br>Presidencia|24 h|260 μg/m3N|Cuando el percentil 99,7 de los promedios<br>diarios durante un año, sea mayor o igual a<br>260 (μg/m3N).|
|**Norma**<br>**Secundariaa **|la Secretaría<br>General de la<br>Presidencia|1 h|700 μg/m3N|Si<br>en<br>un<br>año<br>calendario,<br>el<br>valor<br>correspondiente al percentil 99,73 de las<br>concentraciones de 1 hora, fuere mayor o<br>igual al doble del valor de la norma que se<br>establece.|
|**Dióxido de**<br>**Nitrógeno**<br>**(NO2) **|D.S N° 114/2003<br>del Ministerio<br>Secretaría<br>General de la<br>Presidencia.|Anual|100 μg/m3N|Cuando el promedio de las concentraciones<br>anuales sea mayor o igual a 100 (μg/m3N).|
|**Dióxido de**<br>**Nitrógeno**<br>**(NO2) **|D.S N° 114/2003<br>del Ministerio<br>Secretaría<br>General de la<br>Presidencia.|1 h|400 μg/m3N|Cuando el percentil 99 de los promedios<br>horarios durante un año, sea mayor o igual a<br>400 (μg/m3N).|
|**Monóxido de**<br>**carbono (CO)**|D.S N° 115/2002<br>del Ministerio<br>Secretaría<br>General de la<br>Presidencia.|8 h|10 mg/m3N|Cuando el percentil 99 de los máximos<br>diarios de concentración de 8 horas durante<br>un año, sea mayor o igual a 10 mg/m3N.|
|**Monóxido de**<br>**carbono (CO)**|D.S N° 115/2002<br>del Ministerio<br>Secretaría<br>General de la<br>Presidencia.|1 h|30 mg/m3N|Cuando el percentil 99 de los máximos<br>diarios de concentración de 1 hora durante<br>un año, sea mayor o igual a 30 mg/m3N.|

a Límites corresponden a los definidos para la zona sur.

En Chile no existe una norma primaria para material particulado sedimentable. La norma

actualmente definida corresponde a una norma secundaria, definida para la cuenca del Río

Huasco en la III región (DS 4/1992). Dado que no existe una normativa, el Reglamento del

Sistema de Evaluación Ambiental, en su Artículo 11, permite el uso de normas de calidad

ambiental y de emisión como referencia, dentro de las cuales se identifica la Confederación

Suiza.

Se escoge la norma de la Confederación Suiza de 1985 ( _Ordinance on Air pollution. Swiss_

_Federal Council_ ), pues fue desarrollada para la protección de humanos, animales, plantas, su

hábitat y el suelo, de los efectos dañinos y molestias que puedan producir la contaminación

del aire. La norma no se enfoca solo en limitar las emisiones, sino que también entrega

procedimientos en caso de eventos en los cuales los niveles de contaminación del aire sean

excesivos. La norma de la Confederación Suiza define límites para SO 2, NO 2, CO, O 3, MP 10,

MP 2,5, Pb en MP 10, Cd en MP 10, MPS, entre algunos.

La norma ha sido empleada previamente para evaluar el impacto del MPS de los siguientes

proyectos aprobados en él SEA:

 Estudio de Impacto Ambiental “ _Proyecto_ _Santo Domingo_ ” (RCA 119/2015).

 - Declaración de Impacto Ambiental “ _Mina Cinabrio_ _-_ _San Andrés_ ” (RCA 20220400193).

 - Declaración de Impacto Ambiental “ _Proyecto Actualización Continuidad Franke N°2_ ”

(RCA 202202001119).

64

Como tal, considerando que ya hay normativas de calidad primaria vigentes para el presente

proyecto (MP 10, MP 2,5, SO 2, NO 2, CO) y norma secundaria para el SO 2, y que esta norma ha sido

empleada para evaluar el potencial impacto de MPS de proyectos previamente ingresados y

aprobados, es que se considera el uso de la _Ordinance on Air pollution. Swiss Federal Council_

para evaluar el potencial impacto de MPS del proyecto.

**Tabla 54. Norma homologada para evaluar impacto por material particulado sedimentable.**

|Contaminante<br>normado|Norma<br>homologada|Periodo de<br>Evaluación de<br>Cumplimiento<br>de Norma|Concentración<br>máxima<br>permitida|Criterio de excedencia|
|---|---|---|---|---|
|Material<br>Particulado<br>Sedimentable <br>(MPS)|Ordinance on Air<br>pollution. Swiss<br>Federal Council.|Anual|200<br>mg/(m2*d)|Cuando el promedio de la tasa de deposición<br>anuales sea mayor o igual a 200 mg/(m2*d).|

En Chile no existe una norma en inmisión para TRS, siendo la actualmente disponible enfocada

como norma de emisión (DS37/2013). Como tal, el presente proyecto va a considerar la

evaluación a través de la Resolución 1.541 (2013) de Colombia para determinar el potencial

impacto del proyecto. A continuación, se presenta una tabla con los datos definidos como

máximo permitido.

**Tabla 55. Norma homologada para evaluar impacto por TRS.**

|Contaminante<br>normado|Norma<br>homologada|Periodo de<br>Evaluación de<br>Cumplimiento<br>de Norma|Concentración<br>máxima<br>permitida|Criterio de excedencia|
|---|---|---|---|---|
|Azufre total<br>reducido <br>(TRS)|Resolución 1.541<br>(2013) de<br>Colombia.|24 horas|7 μg/m3|Superación de la máxima exposición.|
|Azufre total<br>reducido <br>(TRS)|Resolución 1.541<br>(2013) de<br>Colombia.|1 hora|40 μg/m3|40 μg/m3|

65

##### 6.2. Línea base de calidad del aire

Las estaciones de monitoreo de calidad del aire que se encuentran próximas al perímetro

de la planta corresponden a la Estación Laja y la Estación de San Rosendo (ver Figura 12).

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 12. Localización de las estaciones de monitoreo de calidad del aire.**

Para el análisis de la línea base, la cual corresponde para efectos del proyecto a evaluar a la

situación actual (operación actual de la planta), se consideró el análisis de 3 años (2020,

2021 y 2022) para todos los gases y material particulado, pero dada la falta de datos para

MP 2,5 en la estación Laja, se consideró también el año 2018 y 2019 para este contaminante.

A continuación, se presenta la tabla resumen con la disponibilidad de datos para los gases

y material particulado.

66

**Tabla 56. Datos disponibles en estaciones de monitoreo de calidad del aire.**

|Estación|Parámetro medido|Periodo medición|Número datos validos|Col5|Col6|Col7|Col8|Porcentaje de datos validos por año|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Estación**|**Parámetro medido**|**Periodo medición**|**2018**|**2019**|**2020**|**2021**|**2022**|**2018**|**2019**|**2020**|**2021**|**2022**|
|Laja|MP10|2020 a 2022|--|--|8.726|8.652|8.669|--|--|99%|99%|99%|
|Laja|MP2,5|2018 a 2020|8.659|8.600|3.647|--|--|99%|98%|42%|--|--|
|Laja|SO2|2020 a 2022|--|--|8.550|8.564|8.474|--|--|97%|98%|97%|
|Laja|NO2|2020 a 2022|--|--|8.584|8.521|8.581|--|--|98%|97%|98%|
|Laja|CO|2020 a 2022|--|--|8.647|8.584|8.545|--|--|97%|97%|98%|
|Laja|TRS|2020 a 2022|--|--|8.485|8.544|8.476|--|--|97%|98%|97%|
|San Rosendo|MP10|2020 a 2022|--|--|8.553|8.332|8.672|--|--|97%|95%|99%|
|San Rosendo|MP2,5|2020 a 2022|--|--|8.553|8.332|8.672|--|--|97%|95%|99%|
|San Rosendo|SO2|2020 a 2022|--|--|8.479|8.358|8.472|--|--|97%|95%|97%|
|San Rosendo|NO2|2020 a 2022|--|--|8.530|8.435|8.570|--|--|97%|96%|98%|
|San Rosendo|CO|2020 a 2022|--|--|8.559|8.502|8.580|--|--|98%|98%|98%|
|San Rosendo|TRS|2020 a 2022|--|--|8.546|8.373|8.473|--|--|97%|96%|97%|

**Fuente** : antecedentes informe calidad del aire.

A continuación, se presenta la línea base para las estaciones de monitoreo.

**Tabla 57. Línea base.**

|Estación|Estadístico|Línea base en estación|Límite normativo|% normativa|
|---|---|---|---|---|
|Laja|Concentración anual MP10 (μg/m3)|29|50|58%|
|Laja|Percentil 98 concentración 24 horas MP10 (μg/m3)|67|130|52%|
|Laja|Promedio anual MP2,5 (μg/m3)|22|20|110%|
|Laja|Percentil 98 concentración 24 horas MP2,5 (μg/m3)|89|50|178%|
|Laja|Concentraciones 24h de SO2, P99 (μg/m3)|4|150|3%|
|Laja|Concentraciones 1h de SO2, P98,5 (μg/m3)|5|350|1%|
|Laja|Promedio Anual SO2 (μg/m3)|1|60|2%|
|Laja|Concentraciones 24h SO2, P99,7 (μg/m3)|6|260|2%|
|Laja|Concentraciones 1h SO2, P99,73 (μg/m3)|12|700|2%|
|Laja|Concentraciones 1h NO2, P99 (μg/m3)|40|400|10%|
|Laja|Promedio Concentraciones NO2 (μg/m3)|8|100|8%|
|Laja|Concentraciones 1h CO, P99 (mg/m3)|5|30|17%|
|Laja|Concentraciones 8h móvil CO, P99 (mg/m3)|3|10|30%|
|Laja|Concentraciones 24h TRS (μg/m3)|4|7|57%|

67

|Estación|Estadístico|Línea base en estación|Límite normativo|% normativa|
|---|---|---|---|---|
||Concentraciones 1h TRS (μg/m3)|20|40|50%|
|San Rosendo|Concentración anual MP10 (μg/m3)|36|50|72%|
|San Rosendo|Percentil 98 concentración 24 horas MP10 (μg/m3)|99|130|76%|
|San Rosendo|Promedio anual MP2,5 (μg/m3)|26|20|130%|
|San Rosendo|Percentil 98 concentración 24 horas MP2,5 (μg/m3)|101|50|202%|
|San Rosendo|Concentraciones 24h de SO2, P99 (μg/m3)|7|150|5%|
|San Rosendo|Concentraciones 1h de SO2, P98,5 (μg/m3)|8|350|2%|
|San Rosendo|Promedio Anual SO2 (μg/m3)|3|60|5%|
|San Rosendo|Concentraciones 24h SO2, P99,7 (μg/m3)|9|260|3%|
|San Rosendo|Concentraciones 1h SO2, P99,73 (μg/m3)|16|700|2%|
|San Rosendo|Concentraciones 1h NO2, P99 (μg/m3)|37|400|9%|
|San Rosendo|Promedio Concentraciones NO2 (μg/m3)|10|100|10%|
|San Rosendo|Concentraciones 1h CO, P99 (mg/m3)|6|30|20%|
|San Rosendo|Concentraciones 8h móvil CO, P99 (mg/m3)|4|10|40%|
|San Rosendo|Concentraciones 24h TRS (μg/m3)|4|7|57%|
|San Rosendo|Concentraciones 1h TRS (μg/m3)|61|40|153%|

**Fuente** : antecedentes informe calidad del aire.

De acuerdo a la Tabla 57, se supera la concentración definida por normativa para el MP 2,5 en la en la estación Laja y San Rosendo

(promedio anual y percentil 98) y la concentración máxima de TRS de los datos horarios. Dado lo anterior, esta estación está saturada

para ambos y para evaluar el potencial impacto del proyecto, se estima si el aporte del proyecto en los diferentes escenarios tiene un

impacto significativo sobre el los niveles registrados en las estaciones.

68

##### 6.3. Nivel de impacto significativo

En el estudio “ _EVALUACIÓN SIGNIFICANCIA DEL IMPACTO DE LAS EMISIONES DE UN_

_PROYECTO O ACTIVIDAD EN ZONAS SATURADAS EN EL MARCO DEL SEIA_ ” realizado por el

DICTUC para él SEA (2022), se define al nivel de impacto de significancia como: “ _**aquella**_

_**concentración definida de un contaminante criterio en el aire ambiente que se consideran**_

_**intrascendentes en comparación con los NAAQS**_ ” (NAAQS por sus siglas en inglés que

significan _National Ambient Air Quality Standards_ ).

El SIL de MP 2,5 fue determinado con los límites establecidos de las normas de calidad

primaria vigentes a la fecha del desarrollo estudio. Dado que no se establece un SIL para

TRS y que el porcentaje de los SIL para el resto de los contaminantes definidos en el informe

de DICTUC están comprendidos entre un 1- 4,9 %, considerando un escenario restrictivo y

que solo hay saturación para concentración de 1 h de TRS, se estima el SIL para el TRS en

un 1% del valor de la norma homologada.

**Tabla 58. Resumen SILs.**

|Contaminante|Periodo|SIL (μg/m3)|
|---|---|---|
|MP2,5|24 horas|1,71|
|MP2,5|Anual|0,33|
|TRS|1 hora|0,4|

##### 6.4. Selección del Modelo y su Procesamiento

Para evaluar la dispersión de las emisiones del proyecto, se analizó los modelos

recomendados en la “ _Guía para el uso de modelos de calidad del aire_ ” (2023) con respecto

a fuentes de emisión con un alcance de impacto de emisiones en un rango menor o igual a

5 km y se escogió el modelo CALPUFF.

El modelo CALPUFF es una combinación del modelo Gaussiano y modelo Langrangeano, el

cual calcula la dispersión de los contaminantes provenientes de una emisión instantánea,

gene rando un “puff” capaz de representar el transporte y dispersión de la emisión

Para la modelación, se empleó el modelo CALPUFF versión 7.2.1 y para el procesamiento de
los datos de salida de CALPUFF, se empleó el modelo CALPOST VERSIÓN 7.1.0.

##### 6.5. Aporte de otros proyectos con RCA favorable

Se realizó un análisis de los proyectos aprobados entre el 01 de enero de 2020 al 21 de abril

de 2023 y solo dos proyectos se encuentran cercanos al presente proyecto (ver APENDICE

5 - Proyectos aprobados entre 2020 - 2023 ), considerando un radio de 2 km desde el

centroide de la planta al punto representativo del proyecto.

69

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 13. Geolocalización puntual de proyectos colindantes no ejecutados con RCA favorable.**

Los proyectos corresponden a “ _Nueva conexión y ampliación S/E Celulosa Laja_ ” de CMPC

Pulp SpA y el proyecto “ _Subestación La señoraza 220/66 kV”._ De acuerdo al SNIFA, ambos

proyectos se encuentran en fase de construcción. Para el aporte de los proyectos se

consideró el peor escenario de mayor aporte.

A continuación, se presenta el aporte de estos proyectos a la línea base.

**Tabla 59. Aporte proyectos no ejecutados, colindantes al perímetro del proyecto.**

|Proyecto|Estadístico|Aporte en<br>estación Laja|
|---|---|---|
|Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1)|Promedio anualMP10 (μg/m3)|1|
|Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1)|Percentil 98 concentración 24 horas MP10 (μg/m3)|3|
|Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1)|Promedio anual MP2,5 (μg/m3)|0|
|Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1)|Percentil 98 concentración 24 horas MP2,5 (μg/m3)|1|
|Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1)|Promedio Concentraciones 24h de SO2, P99 (μg/m3)|0|
|Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1)|Promedio concentraciones 1h de SO2, P98,5 (μg/m3)|0|
|Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1)|Promedio Anual SO2 (μg/m3)|0|
|Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1)|Promedio Concentraciones 24h SO2, P99,7 (μg/m3)|0|
|Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1)|Promedio Concentraciones 1h SO2, P99,73 (μg/m3)|0|
|Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1)|Promedio Concentraciones 1h NO2, P99 (μg/m3)|9|
|Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1)|Promedio Concentraciones NO2 (μg/m3)|0|

70

|Proyecto|Estadístico|Aporte en<br>estación Laja|
|---|---|---|
||Promedio Concentraciones 1h CO, P99 (mg/m3)|0|
||Promedio Concentraciones 8h móvil CO, P99 (mg/m3)|0|
|Subestación La señoraza 220/66 kV<br>(proyecto 2)|Promedio anualMP10 (μg/m3)|0|
|Subestación La señoraza 220/66 kV<br>(proyecto 2)|Percentil 98 concentración 24 horas MP10 (μg/m3)|0|
|Subestación La señoraza 220/66 kV<br>(proyecto 2)|Promedio anual MP2,5 (μg/m3)|0|
|Subestación La señoraza 220/66 kV<br>(proyecto 2)|Percentil 98 concentración 24 horas MP2,5 (μg/m3)|0|
|Subestación La señoraza 220/66 kV<br>(proyecto 2)|Promedio Concentraciones 24h de SO2, P99 (μg/m3)|0|
|Subestación La señoraza 220/66 kV<br>(proyecto 2)|Promedio concentraciones 1h de SO2, P98,5 (μg/m3)|0|
|Subestación La señoraza 220/66 kV<br>(proyecto 2)|Promedio Anual SO2 (μg/m3)|0|
|Subestación La señoraza 220/66 kV<br>(proyecto 2)|Promedio Concentraciones 24h SO2, P99,7 (μg/m3)|0|
|Subestación La señoraza 220/66 kV<br>(proyecto 2)|Promedio Concentraciones 1h SO2, P99,73 (μg/m3)|0|
|Subestación La señoraza 220/66 kV<br>(proyecto 2)|Promedio Concentraciones 1h NO2, P99 (μg/m3)|1|
|Subestación La señoraza 220/66 kV<br>(proyecto 2)|Promedio Concentraciones NO2 (μg/m3)|0|
|Subestación La señoraza 220/66 kV<br>(proyecto 2)|Promedio Concentraciones 1h CO, P99 (mg/m3)|0|
|Subestación La señoraza 220/66 kV<br>(proyecto 2)|Promedio Concentraciones 8h móvil CO, P99 (mg/m3)|0|

**Fuente** : antecedentes informe calidad del aire.

Para efectos de la estimación de la concentración total, se considera al aporte en la estación

Laja de los proyectos colindantes como el aporte de los proyectos en los receptores estudio.

##### 6.6. Receptores

Para la selección de los receptores, se consideró aquellos localizados en el área colindante

del proyecto. De esta forma, se localizaron 6 receptores, entre estos el más cercano a la

planta corresponde al receptor 6 que se encuentran localizados a 47 m del perímetro de la

planta y el receptor más lejano corresponde a la estación San Rosendo, la cual se encuentra

a 2,4 km del perímetro de la planta (ver Figura 14 y Tabla 60).

**Tabla 60. Receptores discretos.**

|ID|Nombre|Altura m.s.n.m<br>(m)1|Distancia al límite del<br>perímetro del proyecto<br>(m)|Coordenadas UTM<br>Datum WGS 84 Huso 18|Col6|
|---|---|---|---|---|---|
|**ID**|**Nombre**|**Altura m.s.n.m**<br>**(m)1 **|**Distancia al límite del**<br>**perímetro del proyecto**<br>**(m)**|**Este (m)**|**Norte (m)**|
|Rr1|Receptor 1|65,3|417|703.097|5.871.334|
|Rr2|Receptor 2|61,3|557|702.696|5.871.708|
|Rr3|Receptor 3|80,2|958|703.688|5.871.455|
|Rr4|Receptor 4|62,8|858|702.929|5.871.976|
|Rr5|Receptor 5|62,2|170|702.686|5.871.321|
|Rr6|Receptor 6|62,1|47|702.519|5.871.048|
|Rr7|Estación Laja|68,3|1.835|702.992|5.872.963|
|Rr8|Estación San<br>Rosendo|80,1|2.393|702.104|5.873.472|

1 La altura se determinó a partir del Archivo GRD de WRF, el cual se basa en datos extraídos desde GMTED2010.

71

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 14. Localización de receptores del proyecto.**

En la Figura 15 se presenta el Plan Regulador Comunal y en la Tabla 61 se presenta los

antecedentes de los receptores discretos: la descripción del receptor y la tipología de

zonificación del Plan Regulador Comunal de la Región del Biobío. Según esto todos los

receptores están ubicados en zonas urbanas.

72

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
Elaborado a partir de Zonificación Planes Reguladores Comunales Región del Biobío. Visitado el 14-12-2022. Disponible

en: http://www.geoportal.cl/geoportal/catalog/search/resource/resumen.page?uuid=%7B5108A7C2-54C9-408B-A300
593CB6126334%7D

**Figura 15. Zonificación según plan regulador comunal.**

**Tabla 61. Descripción de receptores discretos.**

|ID|Descripción|Zonificación del Plan Regulador Comunal, región<br>del biobío1|
|---|---|---|
|Rr1|Colegio San Jorge|Urbano. Zona residencial 3.|
|Rr2|Estacionamiento Hospital Antiguo de Laja.|Urbano. Zona residencial 3.|
|Rr3|Población Nivequeten. Calle Los Magnolios, esquina los<br>manzanos.|Urbano. Zona residencial 3.|
|Rr4|Calle Los Aromos, altura N° 107|Urbano. Zona residencial 3.|
|Rr5|Calle Balmaceda N°52.|Urbano. Zona centro cívico.|
|Rr6|Casa habitación cruce ferroviario.|Urbano. Zona actividades productivas 1.|
|EL|Estación Laja|Urbano. Zona mixta 1.|
|ESR|Estación San Rosendo|No definido. Se encuentra dentro del límite<br>urbano.|

1 Infraestructura de datos geoespaciales. Zonificación Planes Reguladores Comunales Región del Biobío. Visitado el 14-12
2022. Disponible en: [http://www.geoportal.cl/geoportal/catalog/search/resource/resumen.page?uuid=%7B5108A7C2-](http://www.geoportal.cl/geoportal/catalog/search/resource/resumen.page?uuid=%7B5108A7C2-54C9-408B-A300-593CB6126334%7D)

54C9-408B-A300-593CB6126334%7D

73

##### 6.7. Modelación de Impactos por Emisión de material particulado y gases

La estación Laja, la cual corresponde a una estación de monitoreo, posee un radio de

representatividad de 2 km, dentro de los cuales se encuentran todos los receptores. Por

ello, la línea base en los receptores se obtiene de esta estación de monitoreo.

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 16. Radio de representatividad de estación Laja.**

Para efectos del aporte de otros proyectos en los receptores, se emplea la concentración

estimada en la estación Laja, dada la representatividad poblacional de la misma.

Los niveles de inmisión en cada receptor para cada contaminante, se corresponden con

aquellos determinados entre el año 2020 y 2022 en el que se produce el mayor impacto

para el estadístico del contaminante a evaluar, mismo procedimiento que se empleó paradeterminar los PMI de cada estadístico (ver APENDICE 6 Resultados Modelación 3 años).

74

El análisis del PMI considera la presentación del aporte del proyecto en dichas coordenadas y para efectos de la evaluación, solo se

considera el análisis del cumplimiento de normativa de calidad primaria, secundaria u homologada, a aquellos puntos que se

encuentren fuera del perímetro de la planta, pues dentro del perímetro de la planta el límite de exposición está dado por salud

ocupacional.

##### - 6.7.1. Concentración total estimada Escenario 1

En esta sección se presenta la concentración total estimada en cada receptor definido y los PMI para cada gas y material particulado

evaluado en el escenario 1.

##### 6.7.1.1. Material particulado respirable (MP 10 )

El análisis del escenario 1 para el MP 10 indica que la concentración total del proyecto es inferior al límite definido por normativa para el

promedio anual y el percentil 98 diario, por lo que se estima que no hay afectación.

**Tabla 62. Promedio anual de la concentración de MP** **10** **-** **Escenario 1.**

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte proyectos<br>con RCA (proyecto<br>1 + proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N)|Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma|Porcentaje<br>de normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|29|0|1|30|50 μg/m3N|60%|Si|
|Receptor 2|29|0|1|30|30|60%|Si|
|Receptor 3|29|0|1|30|30|60%|Si|
|Receptor 4|29|0|1|30|30|60%|Si|
|Receptor 5|29|0|1|30|30|60%|Si|
|Receptor 6|29|0|1|30|30|60%|Si|
|Estación Laja|29|0|1|30|30|60%|Si|
|Estación San Rosendo|36|0|1|37|37|74%|Si|

75

**Tabla 63. Percentil 98 de la concentración diaria de MP** **10** **-** **Escenario 1.**

|Receptor|Línea base<br>percentil 98<br>24 h<br>(μg/m3N).|Percentil 98 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima permitida<br>percentil 98 de 24<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|67|0|3|71|130 μg/m3N|54%|Si|
|Receptor 2|67|1|3|71|71|54%|Si|
|Receptor 3|67|0|3|70|70|54%|Si|
|Receptor 4|67|1|3|71|71|54%|Si|
|Receptor 5|67|1|3|71|71|55%|Si|
|Receptor 6|67|1|3|71|71|55%|Si|
|Estación Laja|67|0|3|71|71|54%|Si|
|Estación San Rosendo|99|1|3|103|103|79%|Si|

##### 6.7.1.2. Material particulado respirable fino (MP 2.5 )

De acuerdo a la normativa vigente, la línea base para el MP 2,5 promedio anual y percentil 98 diario indica una saturación en la estación laja

y San Rosendo. Dado que se identifica una saturación por MP 2,5, se realizó el análisis del nivel de significancia del aporte del proyecto.

Según los límites definidos respecto a la significancia, el aporte del proyecto en el escenario 1 no es significativo para el promedio anual o

percentil 98 diario del MP 2,5 .

**Tabla 64. Impacto sobre la salud de las personas por el promedio anual de la concentración de MP** **2.5** **-** **Escenario 1.**

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte<br>proyectos<br>con RCA<br>(proyecto 1 +<br>proyecto 2)<br>(μg/m3N)|Total (línea<br>base, aporte<br>proyecto y<br>aporte<br>proyectos con<br>RCA)<br>(μg/m3N)|Concentración<br>máxima<br>permitida<br>Promedio anual<br>Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Significancia|Porcentaje<br>del valor de<br>significancia<br>(%)|Impacto en<br>significativo<br>sobre la<br>salud de las<br>personas|
|---|---|---|---|---|---|---|---|---|---|
|Receptor 1|22|0|0|22|20 μg/m3N|112%|0,33<br>μg/m3N|26%|No|
|Receptor 2|22|0|0|22|22|112%|112%|58%|No|

76

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte<br>proyectos<br>con RCA<br>(proyecto 1 +<br>proyecto 2)<br>(μg/m3N)|Total (línea<br>base, aporte<br>proyecto y<br>aporte<br>proyectos con<br>RCA)<br>(μg/m3N)|Concentración<br>máxima<br>permitida<br>Promedio anual<br>Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Significancia|Porcentaje<br>del valor de<br>significancia<br>(%)|Impacto en<br>significativo<br>sobre la<br>salud de las<br>personas|
|---|---|---|---|---|---|---|---|---|---|
|Receptor 3|22|0|0|22||111%||13%|No|
|Receptor 4|22|0|0|22|22|112%|112%|29%|No|
|Receptor 5|22|0|0|22|22|112%|112%|77%|No|
|Receptor 6|22|0|0|22|22|112%|112%|57%|No|
|Estación Laja|22|0|0|22|22|112%|112%|19%|No|
|Estación San Rosendo|26|0|0|26|26|132%|132%|48%|No|

**Tabla 65. Impacto sobre la salud de las personas del percentil 98 de la concentración diaria de MP** **2.5** **- Escenario 1.**

|Receptor|Línea<br>base<br>percentil<br>98 24 h<br>(μg/m3N).|Aporte<br>Proyecto<br>Percentil 98<br>de la<br>concentración<br>en inmisión<br>24 h<br>(μg/m3N)|Aporte<br>proyectos<br>con RCA<br>(proyecto<br>1 +<br>proyecto<br>2)<br>(μg/m3N)|Total<br>(línea<br>base,<br>aporte<br>proyecto<br>y aporte<br>proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima<br>permitida<br>percentil 98<br>de 24 horas<br>Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Significancia|Porcentaje<br>del valor de<br>significancia<br>(%)|Impacto en<br>significativo<br>sobre la<br>salud de las<br>personas|
|---|---|---|---|---|---|---|---|---|---|
|Receptor 1|89|0|1|90|50 μg/m3N|180%|1,71<br>μg/m3N|26%|**No**|
|Receptor 2|89|1|1|91|91|181%|181%|42%|**No**|
|Receptor 3|89|0|1|90|90|180%|180%|16%|**No**|
|Receptor 4|89|1|1|90|90|181%|181%|32%|**No**|
|Receptor 5|89|1|1|91|91|182%|182%|64%|**No**|
|Receptor 6|89|1|1|91|91|181%|181%|45%|**No**|
|Estación Laja|89|0|1|90|90|180%|180%|25%|**No**|
|Estación San Rosendo|101|1|1|102|102|205%|205%|32%|**No**|

77

##### 6.7.1.3. Material particulado sedimentable (MPS)

El análisis del escenario 1 para el MPS indica que la tasa de deposición promedio anual es inferior al límite definido por normativa

homologada, por lo que se estima que no hay afectación.

**Tabla 66. Promedio anual de la tasa de deposición del material particulado sedimentable (MPS)** **-** **Escenario 1.**

|Receptor|Aporte Proyecto tasa de deposición<br>promedio anual (mg/m2N/d)|Tasa de deposición promedio anual<br>máxima permitida Valor Norma|Porcentaje de<br>normativa (%)|Cumplimiento de la<br>normativa|
|---|---|---|---|---|
|Receptor 1|0|200 mg/(m2*d)|0%|Si|
|Receptor 2|0|0|0%|Si|
|Receptor 3|0|0|0%|Si|
|Receptor 4|0|0|0%|Si|
|Receptor 5|0|0|0%|Si|
|Receptor 6|0|0|0%|Si|
|Estación Laja|0|0|0%|Si|
|Estación San Rosendo|0|0|0%|Si|

##### 6.7.1.4. Dióxido de nitrógeno (NO 2 )

El análisis del escenario 1 para el NO 2 indica que la concentración total del proyecto es inferior al límite definido por normativa para el

promedio anual y el percentil 99 horario. Dado lo anterior, se estima que no hay afectación.

**Tabla 67. Promedio anual de la concentración de dióxido de nitrógeno (NO** **2** **)** **-** **Escenario 1.**

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte proyectos<br>con RCA (proyecto<br>1 + proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N)|Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma|Porcentaje<br>de normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|8|0|0|9|100 μg/m3N|9%|Si|
|Receptor 2|8|1|0|9|9|9%|Si|
|Receptor 3|8|0|0|9|9|9%|Si|
|Receptor 4|8|0|0|9|9|9%|Si|
|Receptor 5|8|1|0|9|9|9%|Si|
|Receptor 6|8|1|0|9|9|9%|Si|
|Estación Laja|8|0|0|9|9|9%|Si|

78

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte proyectos<br>con RCA (proyecto<br>1 + proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N)|Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma|Porcentaje<br>de normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Estación San Rosendo|10|0|0|11||11%|Si|

**Tabla 68. Percentil 99 de la concentración horaria de NO** **2** **-** **Escenario 1.**

|Receptor|Línea base<br>percentil 99<br>1 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 1 h (μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 1<br>hora Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|40|7|11|58|400 μg/m3N|14%|Si|
|Receptor 2|40|5|11|55|55|14%|Si|
|Receptor 3|40|6|11|57|57|14%|Si|
|Receptor 4|40|4|11|54|54|14%|Si|
|Receptor 5|40|7|11|58|58|14%|Si|
|Receptor 6|40|11|11|62|62|15%|Si|
|Estación Laja|40|2|11|53|53|13%|Si|
|Estación San Rosendo|37|3|11|50|50|13%|Si|

##### 6.7.1.5. Dióxido de azufre (SO 2 )

El análisis del escenario 1 para el SO 2 indica que la concentración total del proyecto es inferior al límite definido por normativa primaria de

calidad del aire y secundaria de calidad del aire, por lo que se estima que no hay afectación.

79

**Tabla 69. Promedio anual de la concentración de dióxido de azufre (SO** **2** **)** **-** **Escenario 1.**

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte proyectos<br>con RCA (proyecto<br>1 + proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N)|Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma|Porcentaje<br>de normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|1|0|0|1|60 μg/m3N|2%|Si|
|Receptor 2|1|0|0|1|1|2%|Si|
|Receptor 3|1|0|0|1|1|2%|Si|
|Receptor 4|1|0|0|1|1|2%|Si|
|Receptor 5|1|0|0|1|1|2%|Si|
|Receptor 6|1|0|0|1|1|2%|Si|
|Estación Laja|1|0|0|1|1|2%|Si|
|Estación San Rosendo|3|0|0|3|3|5%|Si|

**Tabla 70. Percentil 99 de la concentración diaria de SO** **2** **-** **Escenario 1.**

|Receptor|Línea base<br>percentil 99<br>24 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 24<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|4|1|0|5|150 μg/m3N|3%|Si|
|Receptor 2|4|2|0|6|6|4%|Si|
|Receptor 3|4|1|0|5|5|3%|Si|
|Receptor 4|4|1|0|5|5|4%|Si|
|Receptor 5|4|2|0|6|6|4%|Si|
|Receptor 6|4|2|0|6|6|4%|Si|
|Estación Laja|4|1|0|5|5|3%|Si|
|Estación San Rosendo|7|1|0|8|8|5%|Si|

80

**Tabla 71. Percentil 98,5 de la concentración de 1 h de SO** **2** **-** **Escenario 1.**

|Receptor|Línea base<br>percentil 98,5<br>1 h (μg/m3N).|Aporte Proyecto<br>Percentil 98,5 de la<br>concentración en<br>inmisión 1 h (μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima permitida<br>Percentil 98,5 de 1 h<br>Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|5|1|0|7|350 μg/m3N|2%|Si|
|Receptor 2|5|3|0|8|8|2%|Si|
|Receptor 3|5|1|0|6|6|2%|Si|
|Receptor 4|5|2|0|7|7|2%|Si|
|Receptor 5|5|3|0|9|9|2%|Si|
|Receptor 6|5|3|0|8|8|2%|Si|
|Estación Laja|5|1|0|7|7|2%|Si|
|Estación San Rosendo|8|2|0|10|10|3%|Si|

**Tabla 72. Percentil 99,7 de la concentración diaria de SO** **2** **-** **Escenario 1.**

|Receptor|Línea base<br>percentil 99,7<br>24 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 99,7 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima permitida<br>percentil 99,7 de 24<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|6|2|0|8|260 μg/m3N|3%|Si|
|Receptor 2|6|2|0|9|9|3%|Si|
|Receptor 3|6|2|0|8|8|3%|Si|
|Receptor 4|6|2|0|8|8|3%|Si|
|Receptor 5|6|3|0|9|9|3%|Si|
|Receptor 6|6|2|0|9|9|3%|Si|
|Estación Laja|6|1|0|7|7|3%|Si|
|Estación San Rosendo|9|2|0|11|11|4%|Si|

81

**Tabla 73. Percentil 99,73 de la concentración horaria de SO** **2** **-** **Escenario 1.**

|Receptor|Línea base<br>percentil<br>99,73 1 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 99,73 de la<br>concentración en<br>inmisión 1 h (μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima permitida<br>percentil 99,73 de 1<br>hora Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|12|5|1|18|700 μg/m3N|3%|Si|
|Receptor 2|12|6|1|18|18|3%|Si|
|Receptor 3|12|3|1|15|15|2%|Si|
|Receptor 4|12|4|1|17|17|2%|Si|
|Receptor 5|12|7|1|20|20|3%|Si|
|Receptor 6|12|7|1|19|19|3%|Si|
|Estación Laja|12|3|1|16|16|2%|Si|
|Estación San Rosendo|16|3|1|19|19|3%|Si|

##### 6.7.1.6. Monóxido de carbono (CO)

El análisis del escenario 1 para el CO indica que la concentración total del proyecto es inferior al límite definido por normativa para el

percentil 99 de 1 hora y el percentil 99 de 8 horas móvil, por lo que se estima que no hay afectación.

**Tabla 74. Percentil 99 de la concentración de 1 h de CO** **-** **Escenario 1.**

|Receptor|Línea base<br>percentil 99 1<br>h (mg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 1 h<br>(mg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(mg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(mg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 1<br>hora Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|5|0|0|5|30 mg/m3N|17%|Si|
|Receptor 2|5|0|0|5|5|17%|Si|
|Receptor 3|5|0|0|5|5|17%|Si|
|Receptor 4|5|0|0|5|5|17%|Si|
|Receptor 5|5|0|0|5|5|17%|Si|
|Receptor 6|5|0|0|5|5|17%|Si|
|Estación Laja|5|0|0|5|5|17%|Si|
|Estación San Rosendo|6|0|0|6|6|20%|Si|

82

**Tabla 75. Percentil 99 de la concentración 8 h de CO** **-** **Escenario 1.**

|Receptor|Línea base<br>percentil 99 8<br>h (mg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 8 h<br>(mg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(mg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(mg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 8<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|3|0|0|3|10 mg/m3N|30%|Si|
|Receptor 2|3|0|0|3|3|30%|Si|
|Receptor 3|3|0|0|3|3|30%|Si|
|Receptor 4|3|0|0|3|3|30%|Si|
|Receptor 5|3|0|0|3|3|30%|Si|
|Receptor 6|3|0|0|3|3|30%|Si|
|Estación Laja|3|0|0|3|3|30%|Si|
|Estación San Rosendo|4|0|0|4|4|40%|Si|

##### 6.7.1.7. Azufre total reducido (TRS)

El TRS está saturado para la concentración de 1 hora en la estación San Rosendo. De acuerdo al análisis de significancia, el aporte es menor

al 1% del límite definido por normativa, por lo que se estima que no es significativo.

El TRS de 24 horas cumple con los límites definidos por norma, por lo que se estima que no hay afectación.

**Tabla 76. Concentración diaria de TRS** **-** **Escenario 1.**

|Receptor|Línea base<br>concentración 24<br>horas (μg/m3N).|Aporte Proyecto<br>concentración 24<br>horas (μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos con<br>RCA) (μg/m3N)|Concentración máxima<br>permitida Concentración<br>24 h Valor Norma|Porcentaje de<br>normativa (%)|Cumplimiento de<br>la normativa|
|---|---|---|---|---|---|---|
|Receptor 1|4|0|4|7 μg/m3N|58%|Si|
|Receptor 2|4|0|4|4|58%|Si|
|Receptor 3|4|0|4|4|58%|Si|
|Receptor 4|4|0|4|4|58%|Si|
|Receptor 5|4|0|4|4|58%|Si|
|Receptor 6|4|0|4|4|58%|Si|
|Estación Laja|4|0|4|4|58%|Si|
|Estación San Rosendo|4|0|4|4|58%|Si|

83

**Tabla 77. Impacto sobre la salud de las personas por la concentración horaria de TRS** **-** **Escenario 1.**

|Receptor|Línea base<br>concentración<br>1 hora<br>(μg/m3N).|Aporte<br>Proyecto<br>concentración<br>1 hora<br>(μg/m3N)|Total (línea<br>base, aporte<br>proyecto y<br>aporte<br>proyectos con<br>RCA)<br>(μg/m3N)|Concentración<br>máxima<br>permitida<br>Concentración<br>1 h Valor<br>Norma|Porcentaje de<br>normativa<br>(%)|Cumplimiento<br>de la<br>normativa|Significancia|Porcentaje<br>del valor de<br>significancia<br>(%)|Impacto<br>significativo<br>sobre la salud<br>de las<br>personas|
|---|---|---|---|---|---|---|---|---|---|
|Receptor 1|20|0|20|40 μg/m3N|51%|Si|0,4 μg/m3N|--|--|
|Receptor 2|20|0|20|20|50%|Si|Si|--|--|
|Receptor 3|20|0|20|20|50%|Si|Si|--|--|
|Receptor 4|20|0|20|20|50%|Si|Si|--|--|
|Receptor 5|20|0|20|20|51%|Si|Si|--|--|
|Receptor 6|20|0|20|20|51%|Si|Si|--|--|
|Estación Laja|20|0|20|20|50%|Si|Si|--|--|
|Estación San Rosendo|61|0|61|61|153%|--|--|28%|No|

##### 6.7.1.8. Punto de Máximo Impacto (PMI)

El resumen del aporte máximo del proyecto por estadístico y año se presenta a continuación, indicando si su localización es dentro o fuera

del perímetro de la planta. Tal como se menciona previamente, el análisis de cumplimiento de normativas de calidad primaria, secundaria

y homologada se realiza solo a aquellos que se encuentran fuera del perímetro de la planta. Los estadísticos de los puntos de máximo

impacto determinados para el escenario 1 que se encuentran fuera de planta corresponden a:

 - Promedio anual tasa de deposición MPS.

 - Concentración 24h de SO 2, P99.

 - Concentración 1h de SO 2, P98,5.

 - Promedio Anual SO 2 .

 - Concentración 24h SO 2, P99,7.

 - Concentración 1h SO 2, P99,73.

84

- Concentración 24h TRS.

- Concentración 1h TRS.

**Tabla 78. Resumen de Punto de Máximo Impacto** **-** **Escenario 1.**

|Estadístico|Año estudio mayor<br>concentración ambiental|Coordenadas UTM|Col4|Aporte máximo<br>del proyecto|Localización (dentro o<br>fuera de planta)|
|---|---|---|---|---|---|
|**Estadístico**|**Año estudio mayor**<br>**concentración ambiental**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|
|**Estadístico**|**Año estudio mayor**<br>**concentración ambiental**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Promedio anual MP10 (μg/m3)|2022|702.904,58|5.870.494,68|0|Dentro de perímetro<br>planta|
|Percentil 98 concentración 24 horas MP10 (μg/m3)|2022|702.904,58|5.870.494,68|2|Dentro de perímetro<br>planta|
|Promedio anual MP2,5 (μg/m3)|2022|702.904,58|5.870.494,68|0|Dentro de perímetro<br>planta|
|Percentil 98 concentración 24 horas MP2,5 (μg/m3)|2022|702.904,58|5.870.494,68|2|Dentro de perímetro<br>planta|
|Promedio anual tasa de deposición MPS (mg/m2/d)|2021|701.948,4|5.872.519,81|7|Fuera de perímetro de<br>planta|
|Concentración 24h de SO2, P99 (μg/m3)|2021|702.686,41|5.871.322,12|2|Fuera de perímetro de<br>planta|
|Concentración 1h de SO2, P98,5 (μg/m3)|2021|702.686,41|5.871.322,12|3|Fuera de perímetro de<br>planta|
|Promedio Anual SO2 (μg/m3)|2021|702.686,41|5.871.322,12|0|Fuera de perímetro de<br>planta|
|Concentración 24h SO2, P99,7 (μg/m3)|2021|702.686,41|5.871.322,12|3|Fuera de perímetro de<br>planta|
|Concentración 1h SO2, P99,73 (μg/m3)|2021|702.686,41|5.871.322,12|7|Fuera de perímetro de<br>planta|
|Concentración 1h NO2, P99 (μg/m3)|2022|702.904,58|5.870.494,68|92|Dentro de perímetro<br>planta|
|Concentración NO2 (μg/m3)|2022|702.904,58|5.870.494,68|5|Dentro de perímetro<br>planta|
|Concentración 1h CO, P99 (mg/m3)|2022|702.904,58|5.870.494,68|0|Dentro de perímetro<br>planta|

85

|Estadístico|Año estudio mayor<br>concentración ambiental|Coordenadas UTM|Col4|Aporte máximo<br>del proyecto|Localización (dentro o<br>fuera de planta)|
|---|---|---|---|---|---|
|**Estadístico**|**Año estudio mayor**<br>**concentración ambiental**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|
|**Estadístico**|**Año estudio mayor**<br>**concentración ambiental**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Concentración 8h móvil CO, P99 (mg/m3)|2022|702.904,58|5.870.494,68|0|Dentro de perímetro<br>planta|
|Concentración 24h TRS (μg/m3)|2020|702.686,41|5.871.322,12|0|Fuera de perímetro de<br>planta|
|Concentración 1h TRS (μg/m3)|2021|702.519|5.871.048|0|Fuera de perímetro de<br>planta|

El análisis del cumplimiento de la normativa de calidad primaria, secundaria y homologada para los PMI, indica que en todos los puntos

fuera del perímetro de la planta cumplen con los límites establecidos, por lo que se estima que no hay afectación.

**Tabla 79. Cumplimiento de normativa de los estadísticos del PMI** **-** **Escenario 1**

|Estadístico|Línea<br>base|Aporte<br>máximo del<br>proyecto|Aporte proyectos con<br>RCA (proyecto 1 +<br>proyecto 2)|Concentración<br>total|Concentración<br>máxima permitida|Porcentaje de<br>normativa (%)|
|---|---|---|---|---|---|---|
|Promedio anual tasa de deposición MPS (mg/m2/d)|ND|7|ND|7|200|3%|
|Concentraciones 24h de SO2, P99 (μg/m3)|4|2|0|6|150|4%|
|Concentraciones 1h de SO2, P98,5 (μg/m3)|5|3|0|9|350|2%|
|Promedio Anual SO2 (μg/m3)|1|0|0|1|60|2%|
|Concentración 24h SO2, P99,7 (μg/m3)|6|3|0|9|260|3%|
|Concentración 1h SO2, P99,73 (μg/m3)|12|7|1|20|700|3%|
|Concentración 24h TRS (μg/m3)|4|0|ND|4|7|58%|
|Concentración 1h TRS (μg/m3)|20|0|ND|20|40|51%|

ND: no disponible.

86

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 17. Localización de PMI en Escenario 1.**

87

##### - 6.7.2. Concentración total estimada Escenario 2

En esta sección se presenta la concentración total estimada en cada receptor definido y los PMI para cada gas y material particulado

evaluado en el escenario 2.

##### 6.7.2.1. Material particulado respirable (MP 10 )

El análisis del escenario 2 para el MP 10 indica que la concentración total del proyecto es inferior al límite definido por normativa para el

promedio anual y el percentil 98 diario, por lo que se estima que no hay afectación.

**Tabla 80. Promedio anual de la concentración de MP** **10** **-** **Escenario 2.**

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte proyectos<br>con RCA (proyecto<br>1 + proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N)|Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma|Porcentaje<br>de normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|29|0|1|30|50 μg/m3N|60%|Si|
|Receptor 2|29|0|1|30|30|60%|Si|
|Receptor 3|29|0|1|30|30|60%|Si|
|Receptor 4|29|0|1|30|30|60%|Si|
|Receptor 5|29|0|1|30|30|61%|Si|
|Receptor 6|29|0|1|30|30|60%|Si|
|Estación Laja|29|0|1|30|30|60%|Si|
|Estación San Rosendo|36|0|1|37|37|74%|Si|

**Tabla 81. Percentil 98 de la concentración diaria de MP** **10** **-** **Escenario 2.**

|Receptor|Línea base<br>percentil 98<br>24 h<br>(μg/m3N).|Percentil 98 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima permitida<br>percentil 98 de 24<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|67|0|3|71|130 μg/m3N|54%|Si|
|Receptor 2|67|1|3|71|71|55%|Si|
|Receptor 3|67|0|3|70|70|54%|Si|

88

|Receptor|Línea base<br>percentil 98<br>24 h<br>(μg/m3N).|Percentil 98 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima permitida<br>percentil 98 de 24<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 4|67|1|3|71||54%|Si|
|Receptor 5|67|1|3|71|71|55%|Si|
|Receptor 6|67|1|3|71|71|54%|Si|
|Estación Laja|67|0|3|71|71|54%|Si|
|Estación San Rosendo|99|1|3|103|103|79%|Si|

##### 6.7.2.2. Material particulado respirable fino (MP 2.5 )

El análisis de significancia del aporte del proyecto para MP 2,5 indica que el aporte del proyecto para el escenario 2 no es significativo para

el promedio anual o percentil 98 diario del MP 2,5 .

**Tabla 82. Impacto sobre la salud de las personas por el promedio anual de la concentración de MP** **2.5** **-** **Escenario 2.**

|Receptor|Línea<br>base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte<br>proyectos<br>con RCA<br>(proyecto<br>1 +<br>proyecto<br>2)<br>(μg/m3N)|Total<br>(línea<br>base,<br>aporte<br>proyecto<br>y aporte<br>proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima<br>permitida<br>Promedio<br>anual Valor<br>Norma|Porcentaje<br>de<br>normativa<br>(%)|Significancia|Porcentaje<br>del valor de<br>significancia<br>(%)|Impacto<br>significativo<br>sobre la<br>salud de las<br>personas|
|---|---|---|---|---|---|---|---|---|---|
|Receptor 1|22|0|0|22|20 μg/m3N|112%|0,33 μg/m3N|30%|No|
|Receptor 2|22|0|0|22|22|112%|112%|76%|No|
|Receptor 3|22|0|0|22|22|111%|111%|16%|No|
|Receptor 4|22|0|0|22|22|112%|112%|38%|No|
|Receptor 5|22|0|0|23|23|113%|113%|98%|No|
|Receptor 6|22|0|0|22|22|112%|112%|72%|No|
|Estación Laja|22|0|0|22|22|112%|112%|26%|No|
|Estación San Rosendo|26|0|0|26|26|132%|132%|66%|No|

89

**Tabla 83. Impacto sobre la salud de las personas por el percentil 98 de la concentración diaria de MP** **2.5** **-** **Escenario 2.**

|Receptor|Línea base<br>percentil 98<br>24 h<br>(μg/m3N).|Aporte<br>Proyecto<br>Percentil 98 de<br>la<br>concentración<br>en inmisión 24<br>h (μg/m3N)|Aporte<br>proyectos<br>con RCA<br>(proyecto<br>1 +<br>proyecto<br>2)<br>(μg/m3N)|Total (línea<br>base, aporte<br>proyecto y<br>aporte<br>proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima<br>permitida<br>percentil 98<br>de 24 horas<br>Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Significancia|Porcentaje<br>del valor de<br>significancia<br>(%)|Impacto<br>significativo<br>sobre la<br>salud de las<br>personas|
|---|---|---|---|---|---|---|---|---|---|
|Receptor 1|89|0|1|90|50 μg/m3N|180%|1,71<br>μg/m3N|26%|No|
|Receptor 2|89|1|1|91|91|181%|181%|46%|No|
|Receptor 3|89|0|1|90|90|180%|180%|16%|No|
|Receptor 4|89|1|1|90|90|181%|181%|34%|No|
|Receptor 5|89|1|1|91|91|182%|182%|64%|No|
|Receptor 6|89|1|1|90|90|181%|181%|41%|No|
|Estación Laja|89|0|1|90|90|180%|180%|25%|No|
|Estación San<br>Rosendo|101|1|1|102|102|205%|205%|33%|No|

##### 6.7.2.3. Material particulado sedimentable (MPS)

El análisis del escenario 2 para el MPS indica que la tasa de deposición promedio anual es inferior al límite definido por normativa

homologada, por lo que se estima que no hay afectación.

**Tabla 84. Promedio anual de la tasa de deposición del material particulado sedimentable (MPS)** **-** **Escenario 2.**

|Receptor|Aporte Proyecto tasa de deposición<br>promedio anual (mg/m2N/d)|Tasa de deposición promedio anual<br>máxima permitida Valor Norma|Porcentaje de<br>normativa (%)|Cumplimiento de la<br>normativa|
|---|---|---|---|---|
|Receptor 1|0|200 mg/(m2*d)|0%|Si|
|Receptor 2|0|0|0%|Si|
|Receptor 3|0|0|0%|Si|
|Receptor 4|0|0|0%|Si|
|Receptor 5|0|0|0%|Si|

90

|Receptor|Aporte Proyecto tasa de deposición<br>promedio anual (mg/m2N/d)|Tasa de deposición promedio anual<br>máxima permitida Valor Norma|Porcentaje de<br>normativa (%)|Cumplimiento de la<br>normativa|
|---|---|---|---|---|
|Receptor 6|0||0%|Si|
|Estación Laja|0|0|0%|Si|
|Estación San Rosendo|0|0|0%|Si|

##### 6.7.2.4. Dióxido de nitrógeno (NO 2 )

El análisis del escenario 2 para el NO 2 indica que la concentración total del proyecto es inferior al límite definido por normativa para el

promedio anual y el percentil 99 horario. Dado lo anterior, se estima que no hay afectación.

**Tabla 85. Promedio anual de la concentración de dióxido de nitrógeno (NO** **2** **)** **-** **Escenario 2.**

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte proyectos<br>con RCA (proyecto<br>1 + proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N)|Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma|Porcentaje<br>de normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|8|0|0|9|100 μg/m3N|9%|Si|
|Receptor 2|8|1|0|9|9|9%|Si|
|Receptor 3|8|0|0|9|9|9%|Si|
|Receptor 4|8|0|0|9|9|9%|Si|
|Receptor 5|8|1|0|10|10|10%|Si|
|Receptor 6|8|1|0|9|9|9%|Si|
|Estación Laja|8|0|0|9|9|9%|Si|
|Estación San Rosendo|10|1|0|11|11|11%|Si|

**Tabla 86. Percentil 99 de la concentración horaria de NO** **2** **-** **Escenario 2.**

|Receptor|Línea base<br>percentil 99<br>1 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 1 h (μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 1<br>hora Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|40|6|11|57|400 μg/m3N|14%|Si|
|Receptor 2|40|5|11|55|55|14%|Si|
|Receptor 3|40|6|11|57|57|14%|Si|

91

|Receptor|Línea base<br>percentil 99<br>1 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 1 h (μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 1<br>hora Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 4|40|4|11|54||14%|Si|
|Receptor 5|40|7|11|58|58|14%|Si|
|Receptor 6|40|10|11|60|60|15%|Si|
|Estación Laja|40|3|11|53|53|13%|Si|
|Estación San Rosendo|37|3|11|50|50|13%|Si|

##### 6.7.2.5. Dióxido de azufre (SO 2 )

El análisis del escenario 2 para el SO 2 indica que la concentración total del proyecto es inferior al límite definido por normativa primaria de

calidad del aire y secundaria de calidad del aire, por lo que se estima que no hay afectación.

**Tabla 87. Promedio anual de la concentración de dióxido de azufre (SO** **2** **)** **-** **Escenario 2.**

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte proyectos<br>con RCA (proyecto<br>1 + proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N)|Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma|Porcentaje<br>de normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|1|0|0|1|60 μg/m3N|2%|Si|
|Receptor 2|1|0|0|1|1|2%|Si|
|Receptor 3|1|0|0|1|1|2%|Si|
|Receptor 4|1|0|0|1|1|2%|Si|
|Receptor 5|1|0|0|1|1|2%|Si|
|Receptor 6|1|0|0|1|1|2%|Si|
|Estación Laja|1|0|0|1|1|2%|Si|
|Estación San Rosendo|3|0|0|3|3|6%|Si|

92

**Tabla 88. Percentil 99 de la concentración diaria de SO** **2** **-** **Escenario 2.**

|Receptor|Línea base<br>percentil 99<br>24 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 24<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|4|1|0|5|150 μg/m3N|4%|Si|
|Receptor 2|4|2|0|6|6|4%|Si|
|Receptor 3|4|1|0|5|5|3%|Si|
|Receptor 4|4|1|0|5|5|4%|Si|
|Receptor 5|4|2|0|6|6|4%|Si|
|Receptor 6|4|2|0|6|6|4%|Si|
|Estación Laja|4|1|0|5|5|3%|Si|
|Estación San Rosendo|7|1|0|8|8|5%|Si|

**Tabla 89. Percentil 98,5 de la concentración de 1 h de SO** **2** **-** **Escenario 2.**

|Receptor|Línea base<br>percentil 98,5<br>1 h (μg/m3N).|Aporte Proyecto<br>Percentil 98,5 de la<br>concentración en<br>inmisión 1 h (μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima permitida<br>Percentil 98,5 de 1 h<br>Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|5|2|0|7|350 μg/m3N|2%|Si|
|Receptor 2|5|3|0|8|8|2%|Si|
|Receptor 3|5|1|0|6|6|2%|Si|
|Receptor 4|5|2|0|8|8|2%|Si|
|Receptor 5|5|4|0|9|9|3%|Si|
|Receptor 6|5|3|0|8|8|2%|Si|
|Estación Laja|5|2|0|7|7|2%|Si|
|Estación San Rosendo|8|2|0|10|10|3%|Si|

93

**Tabla 90. Percentil 99,7 de la concentración diaria de SO** **2** **-** **Escenario 2.**

|Receptor|Línea base<br>percentil 99,7<br>24 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 99,7 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima permitida<br>percentil 99,7 de 24<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|6|2|0|8|260 μg/m3N|3%|Si|
|Receptor 2|6|2|0|9|9|3%|Si|
|Receptor 3|6|2|0|8|8|3%|Si|
|Receptor 4|6|2|0|8|8|3%|Si|
|Receptor 5|6|3|0|9|9|3%|Si|
|Receptor 6|6|2|0|9|9|3%|Si|
|Estación Laja|6|1|0|7|7|3%|Si|
|Estación San Rosendo|9|2|0|11|11|4%|Si|

**Tabla 91. Percentil 99,73 de la concentración horaria de SO** **2** **-** **Escenario 2.**

|Receptor|Línea base<br>percentil<br>99,73 1 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 99,73 de la<br>concentración en<br>inmisión 1 h (μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima permitida<br>percentil 99,73 de 1<br>hora Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|12|6|1|18|700 μg/m3N|3%|Si|
|Receptor 2|12|6|1|18|18|3%|Si|
|Receptor 3|12|3|1|16|16|2%|Si|
|Receptor 4|12|5|1|17|17|2%|Si|
|Receptor 5|12|7|1|20|20|3%|Si|
|Receptor 6|12|7|1|19|19|3%|Si|
|Estación Laja|12|3|1|16|16|2%|Si|
|Estación San Rosendo|16|3|1|20|20|3%|Si|

94

##### 6.7.2.6. Monóxido de carbono (CO)

El análisis del escenario 2 para el CO indica que la concentración total del proyecto es inferior al límite definido por normativa para el

percentil 99 de 1 hora y el percentil 99 de 8 horas móvil, por lo que se estima que no hay afectación.

**Tabla 92. Percentil 99 de la concentración de 1 h de CO** **-** **Escenario 2.**

|Receptor|Línea base<br>percentil 99 1<br>h (mg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 1 h<br>(mg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(mg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(mg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 1<br>hora Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|5|0|0|5|30 mg/m3N|17%|Si|
|Receptor 2|5|0|0|5|5|17%|Si|
|Receptor 3|5|0|0|5|5|17%|Si|
|Receptor 4|5|0|0|5|5|17%|Si|
|Receptor 5|5|0|0|5|5|17%|Si|
|Receptor 6|5|0|0|5|5|17%|Si|
|Estación Laja|5|0|0|5|5|17%|Si|
|Estación San Rosendo|6|0|0|6|6|20%|Si|

**Tabla 93. Percentil 99 de la concentración 8 h de CO** **-** **Escenario 2.**

|Receptor|Línea base<br>percentil 99 8<br>h (mg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 8 h<br>(mg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(mg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(mg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 8<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|3|0|0|3|10 mg/m3N|30%|Si|
|Receptor 2|3|0|0|3|3|30%|Si|
|Receptor 3|3|0|0|3|3|30%|Si|
|Receptor 4|3|0|0|3|3|30%|Si|
|Receptor 5|3|0|0|3|3|30%|Si|
|Receptor 6|3|0|0|3|3|30%|Si|
|Estación Laja|3|0|0|3|3|30%|Si|

95

|Receptor|Línea base<br>percentil 99 8<br>h (mg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 8 h<br>(mg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(mg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(mg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 8<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Estación San Rosendo|4|0|0|4||40%|Si|

##### 6.7.2.7. Azufre total reducido (TRS)

El TRS está saturado para la concentración de 1 hora en la estación San Rosendo. De acuerdo al análisis de significancia, el aporte es menor

al 1% del límite definido por normativa, por lo que se estima que no es significativo.

El TRS de 24 horas cumple con los límites definidos por norma, por lo que se estima que no hay afectación.

**Tabla 94. Concentración diaria de TRS** **-** **Escenario 2.**

|Receptor|Línea base<br>concentración 24<br>horas (μg/m3N).|Aporte Proyecto<br>concentración 24<br>horas (μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos con<br>RCA) (μg/m3N)|Concentración máxima<br>permitida Concentración<br>24 h Valor Norma|Porcentaje de<br>normativa (%)|Cumplimiento de<br>la normativa|
|---|---|---|---|---|---|---|
|Receptor 1|4|0|4|7 μg/m3N|58%|Si|
|Receptor 2|4|0|4|4|58%|Si|
|Receptor 3|4|0|4|4|58%|Si|
|Receptor 4|4|0|4|4|58%|Si|
|Receptor 5|4|0|4|4|58%|Si|
|Receptor 6|4|0|4|4|58%|Si|
|Estación Laja|4|0|4|4|58%|Si|
|Estación San Rosendo|4|0|4|4|58%|Si|

**Tabla 95. Impacto sobre la salud de las personas por la concentración horaria de TRS** **-** **Escenario 2.**

|Receptor|Línea base<br>concentración<br>1 hora<br>(μg/m3N).|Aporte<br>Proyecto<br>concentración<br>1 hora<br>(μg/m3N)|Total (línea<br>base, aporte<br>proyecto y<br>aporte<br>proyectos con<br>RCA)<br>(μg/m3N)|Concentración<br>máxima<br>permitida<br>Concentración<br>1 h Valor<br>Norma|Porcentaje de<br>normativa<br>(%)|Cumplimiento<br>de la<br>normativa|Significancia|Porcentaje<br>del valor de<br>significancia<br>(%)|Impacto<br>significativo<br>sobre la salud<br>de las<br>personas|
|---|---|---|---|---|---|---|---|---|---|
|Receptor 1|20|0|20|40 μg/m3N|51%|Si|0,4 μg/m3N|--|--|

96

|Receptor|Línea base<br>concentración<br>1 hora<br>(μg/m3N).|Aporte<br>Proyecto<br>concentración<br>1 hora<br>(μg/m3N)|Total (línea<br>base, aporte<br>proyecto y<br>aporte<br>proyectos con<br>RCA)<br>(μg/m3N)|Concentración<br>máxima<br>permitida<br>Concentración<br>1 h Valor<br>Norma|Porcentaje de<br>normativa<br>(%)|Cumplimiento<br>de la<br>normativa|Significancia|Porcentaje<br>del valor de<br>significancia<br>(%)|Impacto<br>significativo<br>sobre la salud<br>de las<br>personas|
|---|---|---|---|---|---|---|---|---|---|
|Receptor 2|20|0|20|20|50%|Si|Si|--|--|
|Receptor 3|20|0|20|20|50%|Si|Si|--|--|
|Receptor 4|20|0|20|20|50%|Si|Si|--|--|
|Receptor 5|20|0|20|20|51%|Si|Si|--|--|
|Receptor 6|20|0|20|20|51%|Si|Si|--|--|
|Estación Laja|20|0|20|20|50%|Si|Si|--|--|
|Estación San Rosendo|61|0|61|61|153%|--|--|28%|No|

##### 6.7.2.8. Punto de Máximo Impacto (PMI)

Los estadísticos de los puntos de máximo impacto determinados para el escenario 2 que se encuentran fuera de planta corresponden a:

 - Promedio anual MP 10 .

 - Promedio anual tasa de deposición MPS.

 - Concentración 24h de SO 2, P99.

 - Concentración 1h de SO 2, P98,5.

 - Promedio Anual SO 2 .

 - Concentración 24h SO 2, P99,7.

 - Concentración 1h SO 2, P99,73.

 - Promedio Concentraciones 1h CO, P99.

 - Concentraciones 24h TRS.

 - Concentraciones 1h TRS.

97

**Tabla 96. Resumen de Punto de Máximo Impacto** **-** **Escenario 2.**

|Estadístico|Año estudio mayor<br>concentración|Coordenadas UTM|Col4|Aporte máximo del<br>proyecto|Localización (dentro o<br>fuera de planta)|
|---|---|---|---|---|---|
|**Estadístico**|**Año estudio mayor**<br>**concentración**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|
|**Estadístico**|**Año estudio mayor**<br>**concentración**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Promedio anual MP10 (μg/m3)|2021|702.686,41|5.871.322,12|0|Fuera del perímetro de la<br>planta|
|Percentil 98 concentración 24 horas MP10 (μg/m3)|2020|702.904,58|5.870.494,68|1|Dentro de perímetro<br>planta|
|Promedio anual MP2,5 (μg/m3)|2021|702.904,58|5.870.494,68|0|Dentro de perímetro<br>planta|
|Percentil 98 concentración 24 horas MP2,5 (μg/m3)|2020|702.904,58|5.870.494,68|1|Dentro de perímetro<br>planta|
|Promedio anual tasa de deposición MPS (mg/m2/d)|2021|701.948,4|5872519.81|10|Fuera del perímetro de la<br>planta|
|Concentración 24h de SO2, P99 (μg/m3)|2021|702.686,41|5.871.322,12|2|Fuera del perímetro de la<br>planta|
|Concentración 1h de SO2, P98,5 (μg/m3)|2021|702.686,41|5.871.322,12|4|Fuera del perímetro de la<br>planta|
|Promedio Anual SO2 (μg/m3)|2021|702.686,41|5.871.322,12|0|Fuera del perímetro de la<br>planta|
|Concentración 24h SO2, P99,7 (μg/m3)|2021|702.686,41|5.871.322,12|3|Fuera del perímetro de la<br>planta|
|Concentración 1h SO2, P99,73 (μg/m3)|2021|702.686,41|5.871.322,12|7|Fuera del perímetro de la<br>planta|
|Concentración 1h NO2, P99 (μg/m3)|2022|702.904,58|5.870.494,68|49|Dentro de perímetro<br>planta|
|Concentración NO2 (μg/m3)|2020|702.904,58|5.870.494,68|3|Dentro de perímetro<br>planta|
|Concentración 1h CO, P99 (mg/m3)|2020|703.884,71|5.869.470,07|0|Fuera del perímetro de la<br>planta|
|Concentración 8h móvil CO, P99 (mg/m3)|2020|702.904,58|5.870.494,68|0|Dentro de perímetro<br>planta|
|Concentración 24h TRS (μg/m3)|2020|702.686,41|5.871.322,12|0|Fuera del perímetro de la<br>planta|

98

|Estadístico|Año estudio mayor<br>concentración|Coordenadas UTM|Col4|Aporte máximo del<br>proyecto|Localización (dentro o<br>fuera de planta)|
|---|---|---|---|---|---|
|**Estadístico**|**Año estudio mayor**<br>**concentración**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|
|**Estadístico**|**Año estudio mayor**<br>**concentración**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Concentración 1h TRS (μg/m3)|2021|702.519|5.871.048|0|Fuera del perímetro de la<br>planta|

El análisis del cumplimiento de la normativa de calidad primaria, secundaria y homologada para los PMI, indica que en todos los puntos

fuera del perímetro de la planta cumplen con los límites establecidos, por lo que se estima que no hay afectación.

**Tabla 97. Cumplimiento de normativa de los estadísticos del PMI** **-** **Escenario 2.**

|Estadístico|Línea<br>base|Aporte<br>máximo del<br>proyecto|Aporte proyectos con<br>RCA (proyecto 1 +<br>proyecto 2)|Concentración<br>total|Concentración<br>máxima permitida|Porcentaje de<br>normativa (%)|
|---|---|---|---|---|---|---|
|Promedio anual MP10 (μg/m3)|29|0|1|30|50|61%|
|Promedio anual tasa de deposición MPS (mg/m2/d)|ND|10|ND|10|200|5%|
|Concentración 24h de SO2, P99 (μg/m3)|4|2|0|6|150|4%|
|Concentración 1h de SO2, P98,5 (μg/m3)|5|4|0|9|350|3%|
|Promedio Anual SO2 (μg/m3)|1|0|0|1|60|2%|
|Concentración 24h SO2, P99,7 (μg/m3)|6|3|0|9|260|3%|
|Concentración 1h SO2, P99,73 (μg/m3)|12|7|1|20|700|3%|
|Concentración 1h CO, P99 (mg/m3)|5|0|0|5|30|17%|
|Concentración 24h TRS (μg/m3)|4|0|ND|4|7|58%|
|Concentración 1h TRS (μg/m3)|20|0|ND|20|40|51%|

ND: no disponible.

99

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 18. Localización de PMI en Escenario 2.**

100

##### - 6.7.3. Concentración total estimada Escenario 3

En esta sección se presenta la concentración total estimada en cada receptor definido y los PMI para cada gas y material particulado

evaluado en el escenario 3.

##### 6.7.3.1. Material particulado respirable (MP 10 )

El análisis del escenario 3 para el MP 10 indica que la concentración total del proyecto es inferior al límite definido por normativa para el

promedio anual y el percentil 98 diario, por lo que se estima que no hay afectación.

**Tabla 98. Promedio anual de la concentración de MP** **10** **-** **Escenario 3.**

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte proyectos<br>con RCA<br>(proyecto 1 +<br>proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N)|Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma|Porcentaje<br>de normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|29|1|1|30|50 μg/m3N|61%|Si|
|Receptor 2|29|0|1|30|30|60%|Si|
|Receptor 3|29|0|1|30|30|60%|Si|
|Receptor 4|29|0|1|30|30|60%|Si|
|Receptor 5|29|1|1|31|31|62%|Si|
|Receptor 6|29|1|1|31|31|62%|Si|
|Estación Laja|29|0|1|30|30|60%|Si|
|Estación San Rosendo|36|0|1|37|37|74%|Si|

**Tabla 99. Percentil 98 de la concentración diaria de MP** **10** **-** **Escenario 3.**

101

|Receptor|Línea base<br>percentil 98<br>24 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 98 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (μg/m3N)|Concentración<br>máxima permitida<br>percentil 98 de 24<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|67|7|3|77|130 μg/m3N|60%|Si|
|Receptor 2|67|1|3|71|71|55%|Si|
|Receptor 3|67|2|3|72|72|55%|Si|
|Receptor 4|67|0|3|71|71|54%|Si|
|Receptor 5|67|8|3|78|78|60%|Si|
|Receptor 6|67|14|3|84|84|64%|Si|
|Estación Laja|67|0|3|70|70|54%|Si|
|Estación San Rosendo|99|0|3|102|102|79%|Si|

##### 6.7.3.2. Material particulado respirable fino (MP 2.5 )

Según los límites definidos respecto a la significancia, el aporte del proyecto en el escenario 3 no es significativo para el promedio anual o

percentil 98 diario del MP 2,5 .

**Tabla 100. Impacto sobre la salud de las personas por el promedio anual de la concentración de MP** **2.5** **-** **Escenario 3.**

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte<br>proyectos<br>con RCA<br>(proyecto<br>1 +<br>proyecto<br>2)<br>(μg/m3N)|Total (línea<br>base, aporte<br>proyecto y<br>aporte<br>proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima<br>permitida<br>Promedio<br>anual Valor<br>Norma|Porcentaje<br>de<br>normativa<br>(%)|Significancia|Porcentaje<br>del valor de<br>significancia<br>(%)|Impacto<br>significativo<br>sobre la<br>salud de las<br>personas|
|---|---|---|---|---|---|---|---|---|---|
|Receptor 1|22|0|0|22|20 μg/m3N|112%|0,33 μg/m3N|28%|No|
|Receptor 2|22|0|0|22|22|111%|111%|11%|No|

102

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte<br>proyectos<br>con RCA<br>(proyecto<br>1 +<br>proyecto<br>2)<br>(μg/m3N)|Total (línea<br>base, aporte<br>proyecto y<br>aporte<br>proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima<br>permitida<br>Promedio<br>anual Valor<br>Norma|Porcentaje<br>de<br>normativa<br>(%)|Significancia|Porcentaje<br>del valor de<br>significancia<br>(%)|Impacto<br>significativo<br>sobre la<br>salud de las<br>personas|
|---|---|---|---|---|---|---|---|---|---|
|Receptor 3|22|0|0|22|22|111%|111%|10%|No|
|Receptor 4|22|0|0|22|22|111%|111%|5%|No|
|Receptor 5|22|0|0|22|22|112%|112%|46%|No|
|Receptor 6|22|0|0|22|22|112%|112%|41%|No|
|Estación Laja|22|0|0|22|22|111%|111%|2%|No|
|Estación San Rosendo|26|0|0|26|26|131%|131%|1%|No|

**Tabla 101. Impacto sobre la salud de las personas del percentil 98 de la concentración diaria de MP** **2.5** **- Escenario 3.**

|Receptor|Línea base<br>percentil<br>98 24 h<br>(μg/m3N).|Aporte<br>Proyecto<br>Percentil 98 de<br>la<br>concentración<br>en inmisión 24<br>h (μg/m3N)|Aporte<br>proyectos<br>con RCA<br>(proyecto 1<br>+ proyecto<br>2)<br>(μg/m3N)|Total (línea<br>base,<br>aporte<br>proyecto y<br>aporte<br>proyectos<br>con RCA)<br>(μg/m3N)|Concentración<br>máxima<br>permitida<br>percentil 98 de<br>24 horas Valor<br>Norma|Porcentaje<br>de<br>normativa<br>(%)|Significancia|Porcentaje<br>del valor de<br>significancia<br>(%)|Impacto<br>significativo<br>sobre la<br>salud de las<br>personas|
|---|---|---|---|---|---|---|---|---|---|
|Receptor 1|89|1|1|91|50 μg/m3N|181%|1,71<br>μg/m3N|51%|No|
|Receptor 2|89|0|1|90|90|180%|180%|12%|No|
|Receptor 3|89|0|1|90|90|180%|180%|18%|No|
|Receptor 4|89|0|1|90|90|180%|180%|5%|No|
|Receptor 5|89|1|1|91|91|182%|182%|59%|No|
|Receptor 6|89|1|1|91|91|183%|183%|87%|No|
|Estación Laja|89|0|1|90|90|180%|180%|2%|No|
|Estación San Rosendo|101|0|1|102|102|204%|204%|1%|No|

103

##### 6.7.3.3. Material particulado sedimentable (MPS)

El análisis del escenario 3 para el MPS indica que la tasa de deposición promedio anual es inferior al límite definido por normativa

homologada, por lo que se estima que no hay afectación.

**Tabla 102. Promedio anual de la tasa de deposición del material particulado sedimentable (MPS)** **-** **Escenario 3.**

|Receptor|Aporte Proyecto tasa de deposición<br>promedio anual (mg/m2N/d)|Tasa de deposición promedio anual<br>máxima permitida Valor Norma|Porcentaje de<br>normativa (%)|Cumplimiento de la<br>normativa|
|---|---|---|---|---|
|Receptor 1|0|200 mg/(m2*d)|0%|Si|
|Receptor 2|0|0|0%|Si|
|Receptor 3|0|0|0%|Si|
|Receptor 4|0|0|0%|Si|
|Receptor 5|0|0|0%|Si|
|Receptor 6|0|0|0%|Si|
|Estación Laja|0|0|0%|Si|
|Estación San Rosendo|0|0|0%|Si|

##### 6.7.3.4. Dióxido de nitrógeno (NO 2 )

El análisis del escenario 3 para el NO 2 indica que la concentración total del proyecto es inferior al límite definido por normativa para el

promedio anual y el percentil 99 horario. Dado lo anterior, se estima que no hay afectación.

**Tabla 103. Promedio anual de la concentración de dióxido de nitrógeno (NO** **2** **)** **-** **Escenario 3.**

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte proyectos<br>con RCA<br>(proyecto 1 +<br>proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N)|Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma|Porcentaje<br>de normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|8|0|0|9|100 μg/m3N|9%|Si|
|Receptor 2|8|0|0|9|9|9%|Si|

104

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte proyectos<br>con RCA<br>(proyecto 1 +<br>proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N)|Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma|Porcentaje<br>de normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 3|8|0|0|9|9|9%|Si|
|Receptor 4|8|0|0|9|9|9%|Si|
|Receptor 5|8|1|0|9|9|9%|Si|
|Receptor 6|8|1|0|9|9|9%|Si|
|Estación Laja|8|0|0|9|9|9%|Si|
|Estación San Rosendo|10|0|0|11|11|11%|Si|

**Tabla 104. Percentil 99 de la concentración horaria de NO** **2** **-** **Escenario 3.**

|Receptor|Línea base<br>percentil 99<br>1 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 1 h<br>(μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (μg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 1<br>hora Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|40|11|11|61|400 μg/m3N|15%|Si|
|Receptor 2|40|3|11|54|54|13%|Si|
|Receptor 3|40|6|11|57|57|14%|Si|
|Receptor 4|40|2|11|52|52|13%|Si|
|Receptor 5|40|8|11|59|59|15%|Si|
|Receptor 6|40|13|11|63|63|16%|Si|
|Estación Laja|40|1|11|51|51|13%|Si|
|Estación San Rosendo|37|1|11|48|48|12%|Si|

105

##### 6.7.3.5. Dióxido de azufre (SO 2 )

El análisis del escenario 3 para el SO 2 indica que la concentración total del proyecto es inferior al límite definido por normativa primaria de

calidad del aire y secundaria de calidad del aire, por lo que se estima que no hay afectación.

**Tabla 105. Promedio anual de la concentración de dióxido de azufre (SO** **2** **)** **-** **Escenario 3.**

|Receptor|Línea base<br>promedio<br>anual<br>(μg/m3N).|Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N)|Aporte proyectos<br>con RCA<br>(proyecto 1 +<br>proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N)|Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma|Porcentaje<br>de normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|1|0|0|1|60 μg/m3N|2%|Si|
|Receptor 2|1|0|0|1|1|2%|Si|
|Receptor 3|1|0|0|1|1|2%|Si|
|Receptor 4|1|0|0|1|1|2%|Si|
|Receptor 5|1|0|0|1|1|2%|Si|
|Receptor 6|1|0|0|1|1|2%|Si|
|Estación Laja|1|0|0|1|1|2%|Si|
|Estación San Rosendo|3|0|0|3|3|5%|Si|

**Tabla 106. Percentil 99 de la concentración diaria de SO** **2** **-** **Escenario 3.**

|Receptor|Línea base<br>percentil 99<br>24 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (μg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 24<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|4|0|0|4|150 μg/m3N|3%|Si|
|Receptor 2|4|0|0|4|4|3%|Si|
|Receptor 3|4|0|0|4|4|3%|Si|
|Receptor 4|4|0|0|4|4|3%|Si|
|Receptor 5|4|0|0|4|4|3%|Si|

106

|Receptor|Línea base<br>percentil 99<br>24 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (μg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 24<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 6|4|0|0|4|4|3%|Si|
|Estación Laja|4|0|0|4|4|3%|Si|
|Estación San Rosendo|7|0|0|7|7|5%|Si|

**Tabla 107. Percentil 98,5 de la concentración de 1 h de SO** **2** **-** **Escenario 3.**

|Receptor|Línea base<br>percentil<br>98,5 1 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 98,5 de la<br>concentración en<br>inmisión 1 h<br>(μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (μg/m3N)|Concentración<br>máxima permitida<br>Percentil 98,5 de 1 h<br>Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|5|0|0|5|350 μg/m3N|2%|Si|
|Receptor 2|5|0|0|5|5|2%|Si|
|Receptor 3|5|0|0|5|5|2%|Si|
|Receptor 4|5|0|0|5|5|2%|Si|
|Receptor 5|5|0|0|5|5|2%|Si|
|Receptor 6|5|0|0|5|5|2%|Si|
|Estación Laja|5|0|0|5|5|2%|Si|
|Estación San Rosendo|8|0|0|8|8|2%|Si|

107

**Tabla 108. Percentil 99,7 de la concentración diaria de SO** **2** **-** **Escenario 3.**

|Receptor|Línea base<br>percentil<br>99,7 24 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 99,7 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (μg/m3N)|Concentración<br>máxima permitida<br>percentil 99,7 de 24<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|6|0|0|6|260 μg/m3N|2%|Si|
|Receptor 2|6|0|0|6|6|2%|Si|
|Receptor 3|6|0|0|6|6|2%|Si|
|Receptor 4|6|0|0|6|6|2%|Si|
|Receptor 5|6|0|0|6|6|2%|Si|
|Receptor 6|6|0|0|6|6|2%|Si|
|Estación Laja|6|0|0|6|6|2%|Si|
|Estación San Rosendo|9|0|0|9|9|4%|Si|

**Tabla 109. Percentil 99,73 de la concentración horaria de SO** **2** **-** **Escenario 3.**

|Receptor|Línea base<br>percentil<br>99,73 1 h<br>(μg/m3N).|Aporte Proyecto<br>Percentil 99,73 de la<br>concentración en<br>inmisión 1 h<br>(μg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N)|Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (μg/m3N)|Concentración<br>máxima permitida<br>percentil 99,73 de 1<br>hora Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|12|0|1|13|700 μg/m3N|2%|Si|
|Receptor 2|12|0|1|13|13|2%|Si|
|Receptor 3|12|0|1|13|13|2%|Si|
|Receptor 4|12|0|1|13|13|2%|Si|
|Receptor 5|12|0|1|13|13|2%|Si|
|Receptor 6|12|0|1|13|13|2%|Si|
|Estación Laja|12|0|1|13|13|2%|Si|
|Estación San Rosendo|16|0|1|17|17|2%|Si|

108

##### 6.7.3.6. Monóxido de carbono (CO)

El análisis del escenario 3 para el CO indica que la concentración total del proyecto es inferior al límite definido por normativa para el

percentil 99 de 1 hora y el percentil 99 de 8 horas móvil, por lo que se estima que no hay afectación

**Tabla 110. Percentil 99 de la concentración de 1 h de CO** **-** **Escenario 3.**

|Receptor|Línea base<br>percentil 99 1<br>h (mg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 1 h<br>(mg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(mg/m3N)|Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (mg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 1<br>hora Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|5|0|0|5|30 mg/m3N|17%|Si|
|Receptor 2|5|0|0|5|5|17%|Si|
|Receptor 3|5|0|0|5|5|17%|Si|
|Receptor 4|5|0|0|5|5|17%|Si|
|Receptor 5|5|0|0|5|5|17%|Si|
|Receptor 6|5|0|0|5|5|17%|Si|
|Estación Laja|5|0|0|5|5|17%|Si|
|Estación San Rosendo|6|0|0|6|6|20%|Si|

**Tabla 111. Percentil 99 de la concentración 8 h de CO** **-** **Escenario 3.**

|Receptor|Línea base<br>percentil 99 8<br>h (mg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 8 h<br>(mg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(mg/m3N)|Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (mg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 8<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 1|3|0|0|3|10 mg/m3N|30%|Si|
|Receptor 2|3|0|0|3|3|30%|Si|
|Receptor 3|3|0|0|3|3|30%|Si|
|Receptor 4|3|0|0|3|3|30%|Si|

109

|Receptor|Línea base<br>percentil 99 8<br>h (mg/m3N).|Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 8 h<br>(mg/m3N)|Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(mg/m3N)|Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (mg/m3N)|Concentración<br>máxima permitida<br>percentil 99 de 8<br>horas Valor Norma|Porcentaje<br>de<br>normativa<br>(%)|Cumplimiento<br>de la normativa|
|---|---|---|---|---|---|---|---|
|Receptor 5|3|0|0|3|3|30%|Si|
|Receptor 6|3|0|0|3|3|30%|Si|
|Estación Laja|3|0|0|3|3|30%|Si|
|Estación San Rosendo|4|0|0|4|4|40%|Si|

##### 6.7.3.7. Punto de Máximo Impacto (PMI)

El resumen del aporte máximo del proyecto por estadístico y año se presenta a continuación, indicando si su localización es dentro o fuera

del perímetro de la planta. De acuerdo a la Tabla 112, todos los PMI se encuentran dentro del perímetro de la planta.

**Tabla 112. Resumen de Punto de Máximo Impacto** **-** **Escenario 3.**

|Estadístico|Año estudio mayor<br>concentración ambiental|Coordenadas UTM|Col4|Aporte máximo<br>del proyecto|Localización (dentro o<br>fuera de planta)|
|---|---|---|---|---|---|
|**Estadístico**|**Año estudio mayor**<br>**concentración ambiental**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|
|**Estadístico**|**Año estudio mayor**<br>**concentración ambiental**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Promedio anual MP10 (μg/m3)|2022|702.904,49|5.870.494,79|71|Dentro de perímetro<br>planta|
|Percentil 98 concentración 24 horas MP10 (μg/m3)|2021|702.904,49|5.870.494,79|338|Dentro de perímetro<br>planta|
|Promedio anual MP2,5 (μg/m3)|2020|702.904,49|5.870.494,79|8|Dentro de perímetro<br>planta|
|Percentil 98 concentración 24 horas MP2,5 (μg/m3)|2021|702.904,49|5.870.494,79|35|Dentro de perímetro<br>planta|
|Promedio anual tasa de deposición MPS (mg/m2/d)|2022|702.904,49|5.870.494,79|5759|Dentro de perímetro<br>planta|
|Concentración 24h de SO2, P99 (μg/m3)|2021|702.904,49|5.870.494,79|0|Dentro de perímetro<br>planta|

110

|Estadístico|Año estudio mayor<br>concentración ambiental|Coordenadas UTM|Col4|Aporte máximo<br>del proyecto|Localización (dentro o<br>fuera de planta)|
|---|---|---|---|---|---|
|**Estadístico**|**Año estudio mayor**<br>**concentración ambiental**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|
|**Estadístico**|**Año estudio mayor**<br>**concentración ambiental**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Concentración 1h de SO2, P98,5 (μg/m3)|2020|702.904,49|5.870.494,79|0|Dentro de perímetro<br>planta|
|Promedio Anual SO2 (μg/m3)|2021|702.904,49|5.870.494,79|0|Dentro de perímetro<br>planta|
|Concentración 24h SO2, P99,7 (μg/m3)|2021|702.904,49|5.870.494,79|0|Dentro de perímetro<br>planta|
|Concentración 1h SO2, P99,73 (μg/m3)|2021|702.904,49|5.870.494,79|1|Dentro de perímetro<br>planta|
|Concentración 1h NO2, P99 (μg/m3)|2021|702.904,49|5.870.494,79|197|Dentro de perímetro<br>planta|
|Concentración NO2 (μg/m3)|2020|702.904,49|5.870.494,79|11|Dentro de perímetro<br>planta|
|Concentración 1h CO, P99 (mg/m3)|2021|702.904,49|5.870.494,79|0|Dentro de perímetro<br>planta|
|Concentración 8h móvil CO, P99 (mg/m3)|2020|702.904,49|5.870.494,79|0|Dentro de perímetro<br>planta|

111

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 19. Localización de PMI en Escenario 3.**

112

#### 7. Conclusiones

Del presente informe del proyecto “ _Proyecto de modificación para producir_ _celulosa_ _cruda_

_en Planta Laja_ ”, se obtienen las siguientes conclusiones:

 - El análisis de la concentración total y tasa de deposición total en los receptores

discretos y las estaciones de monitoreo para los estadísticos definidos en normativa

para MP 10, MPS, NO 2, SO 2 y CO, permite estimar que no se supera la normativa y

que, por tanto, no hay afectación para los 3 años meteorológicos, para el escenario

1, el escenario 2 y el escenario 3.

 - El análisis de la concentración total en los receptores discretos y las estaciones de

monitoreo para el estadístico definido en normativa para TRS (diario), permite

estimar que no se supera la normativa y que, por tanto, no hay afectación para los

3 años meteorológicos, para el escenario 1 y el escenario 2.

 - El análisis del nivel de significancia del aporte del proyecto para los estadísticos

promedio anual y percentil 98 de la concentración diaria de MP 2,5, indica que el

aporte del proyecto no es significativo en los niveles de calidad del aire en el área

de influencia del proyecto para el periodo de 3 años meteorológicos evaluados, por

lo que se descarta que el proyecto pueda producir un impacto significativo en la

calidad del aire de la zona y por tanto en la salud de la población, en el escenario 1,

escenario 2 y escenario 3.

 - El análisis del nivel de significancia para el estadístico concentración horaria de TRS,

indica que el aporte del proyecto no es significativo en los niveles de calidad del aire

en el área de influencia del proyecto para el periodo de 3 años meteorológicos

evaluados, por lo que se descarta que el proyecto pueda producir un impacto

significativo en la calidad del aire de la zona y por tanto en la salud de la población,

en el escenario 1 y escenario 2.

 - De acuerdo al análisis de los PMI del proyecto en el escenario 1, escenario 2 y

escenario 3, la concentración total y/o tasa de deposición total en cada punto fuera

de la planta es inferior al límite definido por normativa, por lo que se estima que no

hay afectación.

Bajo las condiciones evaluadas, se puede concluir que el proyecto y sus diferentes etapas,

no generan un impacto significativo en la calidad del aire de la zona o en la salud de la

población.

113

### 8. Anexos

Los Anexos son archivos adjuntos al presente informe, los cuales incluyen archivos de

geolocalización, metodología de cálculo, archivos de modelación, entre otros. La Tabla 113

indica la lista de estos.

**Tabla 113. Lista de anexos.**

|N° anexo|Nombre de archivo|Descripción/comentarios|
|---|---|---|
|Anexo 1|Metodología de cálculo rev0|Metodología de cálculo de tasas de emisión modeladas.|
|Anexo 2|Archivos kml|Archivos de geolocalización.|
|Anexo 3|Cartografía HQ|Imágenes de cartografía en alta calidad.|
|Anexo 4|Norma de Colombia|Norma para TRS en inmisión.|
|Anexo 5|Norma Suiza|Norma de MPS.|
|Anexo 6|Archivos de modelación|Archivos de Calpuff y Calpost.|
|Anexo 7|Archivos meteorología|Archivo meteorológico. 2020-|
|Anexo 7|Archivos meteorología|Archivo txt file. 2020.|
|Anexo 7|Archivos meteorología|Archivo meteorológico. 2021.|
|Anexo 7|Archivos meteorología|Archivo txt file. 2021.|
|Anexo 7|Archivos meteorología|Archivo meteorológico. 2022.|
|Anexo 7|Archivos meteorología|Archivo txt file. 2022.|
|Anexo 8|Archivo GRD|Archivo grd con alturas de la grilla.|
|Anexo 9|Parametrizaciones WRF|Documento que contiene las parametrizaciones de los archivos<br>WRF.|
|Anexo 10|Archivos namelist|Archivo namelist.input y archive namelist.wsp|

114

### 9. Apéndices

##### - 9.1. APENDICE 1 Archivos de la Modelación

De acuerdo a lo señalado en la Ley 19.300 sobre Bases Generales del Medio Ambiente en el

artículo 14 bis, y en el Decreto Supremo 40 que Aprueba Reglamento del Sistema de

Evaluación de Impacto Ambiental (2012), en el artículo 21 inciso N°3 y el artículo 29 inciso

N°1, se informa que dada la naturaleza de los archivos digitales de Modelación

Meteorológica WRF y Modelaciones de Dispersión Atmosférica **CALPUFF y CALPOST**, no es

posible agregarlos al expediente electrónico, motivo por el cual dicha información se

encuentra disponible para el público en general en las oficinas de la Dirección Ejecutiva del

Servicio de Evaluación Ambiental (SEA). Los interesados en obtener acceso a dicha

documentación digital, deben comunicarse con la Oficina de Información y Atención

Ciudadana del SEA, ingresando un requerimiento a través del siguiente formulario:

https://www.portaltransparencia.cl/PortalPdT/

115

##### - 9.2. APENDICE 2 Estimación de emisión de TRS

Se estimo la tasa de emisión de TRS mediante datos CEMS y los datos de la RCA 2009 y se

determinó para considerar un escenario conservador, aquel en el cual se produce la mayor

emisión. La tasa de emisión se determinó para la producción actual de la planta de 360.000

ton/año y se estimó para una producción proyectada de 400.000 ton/año.

Los datos del CEMS se encuentran en ppmv. Por lo que, para estimar la concentración, se

emplea la siguiente ecuación:

mg [= ppmv∙PM∙P]

m [3] R∙T

mg

-10 [−3]
R∙T

**Ecuación 1**

Donde:

PM= peso molecular de H 2 S (34 g/mol).

P= presión (101.325 Pa).

R= 8,314 (J/(mol*K).

T= Temperatura del equipo (K).

Una vez determinada la concentración horaria, se estima la concentración promedio y se

estima la tasa de emisión mediante la siguiente ecuación:

s [= v∙π∙(D] 2

mg

2 ~~[)]~~ [2] [ ∙mg] m [3]

m [3]

**Ecuación 2**

Donde:

v= velocidad de emisión (m/s).

D= diámetro del equipo (m).

A continuación, se presentan la temperatura, velocidad de emisión y diámetro de los

equipos.

**Tabla 114. Datos de fuentes puntuales.**

116

|Item|Caldera recuperadora|Caldera biomasa|Horno de cal|
|---|---|---|---|
|Velocidad de emisión (m/s)|20,6|25,3|11|
|Temperatura de emisión (K)|428,15|417,15|534,15|
|Diámetro de la chimenea (m)|3,6|2,25|1,6|

Por su parte, los datos de la RCA 2009, entregan los datos de emisión de TRS a una escala

estimada de producción de 500.000 ton/año. A continuación, se presenta una tabla

resumen.

**Tabla 115. Tasa de emisión de TRS en RCA 2009,** **para producción de 500.000 ton/año.**

|Item|Caldera recuperadora|Caldera biomasa|Horno de cal|
|---|---|---|---|
|Producción TRS (ton/día)|0,03|0,01|0,01|

**Fuente** : RCA 2009.

A continuación, se presenta una tabla resumen con la tasa de emisión de TRS para el CEMS

y la RCA 2009, de acuerdo a los niveles de producción y la razón de la tasa de emisión.

**Tabla 116. Resumen de emisión de TRS con datos CEMS y RCA 2009.**

|Equipo|Producción TRS datos CEMS (ton/año)|Col3|Col4|Producción TRS datos RCA (ton/año)|Col6|Col7|Razón<br>incremento<br>producción<br>Datos RCA<br>con CEMS|
|---|---|---|---|---|---|---|---|
|**Equipo**|**Producción**<br>**planta**<br>**360.000**<br>**ton/año**|**Producción**<br>**planta**<br>**400.000**<br>**ton/año**|**Incremento**<br>**producción**<br>**(40.000**<br>**ton/año)**|**Producción**<br>**planta**<br>**360.000**<br>**ton/año**|**Producción**<br>**planta**<br>**400.000**<br>**ton/año**|**Incremento**<br>**producción**<br>**(40.000**<br>**ton/año)**|**Incremento**<br>**producción**<br>**(40.000**<br>**ton/año)**|
|Caldera<br>recuperadora|3,16|3,51|0,35|7,88|8,76|0,88|2,5|
|Caldera<br>biomasa|0,75|0,83|0,08|2,63|2,92|0,29|3,65|
|Horno de cal|1,42|1,58|0,16|2,63|2,92|0,29|1,83|

117

##### - 9.3. APENDICE 3 Selección de la estación meteorológica de referencia

Para la selección de la estación meteorológica de referencia, se procede a geolocalizar todas

las estaciones meteorológicas disponibles dentro del dominio de modelación (ver Figura

20 ), luego, acorde a lo indicado por la “ _Guía para el uso de modelos de calidad del aire en el_

_SEIA_ ” (2023), se emplea el primer criterio establecido, el cual indica empl ear la estación

meteorológica presente en el área de emplazamiento del proyecto. Para ello, se estableció

un radio de 10 km desde el centroide del perímetro de la planta y se analizó distancia al

perímetro de la planta y disponibilidad de datos para el periodo 2020 al 2022, priorizando

para su selección, aquella estación con la mayor cercanía que se encuentre dentro del radio

de 10 km desde el centroide del perímetro de la planta, que no tenga apantallamiento y

que tenga una disponibilidad de datos superior al 70% (ver Tabla 117 y Tabla 118).

**Fuente** : datos del SINCA, DMC y Agrometeorología del INIA.

**Figura 20. Geolocalización de estaciones meteorológicas dentro del dominio de simulación.**

118

**Tabla 117. Análisis de proximidad de estaciones meteorológicas superficiales dentro del dominio.**

|Nombre<br>estación|Base de<br>datos|Distancia al perímetro<br>del proyecto (km)|Coordenadas UTM<br>Datum WGS 84 Huso<br>18|Col5|Variables meteorológicas disponibles<br>para periodo 2020 al 2022|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Nombre**<br>**estación**|**Base de**<br>**datos**|**Distancia al perímetro**<br>**del proyecto (km)**|**Este (m)**|**Norte (m)**|**T1 **|**VV1 **|**DV1 **|**Hr1 **|
|**María**<br>**Dolores2 **|DMC|26,5|728.035|5.857.977|X|X|X|X|
|**La colonia3 **|INIA|9,8|713.484|5.870.414|X|X|X|X|
|**Laja**|SINCA|1,83|702.992|5.872.963|√|√|√|√|
|**Club**<br>**de**<br>**empleados**|**Club**<br>**de**<br>**empleados**|21,7|705.393|5.846.899|√|√|√|√|
|**Lautaro**|**Lautaro**|22,7|736.622|5.850.392|√|√|√|√|
|**21 de mayo**|**21 de mayo**|36,24|733.331|5.849.585|√|√|√|√|
|**Los**<br>**ángeles**<br>**oriente**|**Los**<br>**ángeles**<br>**oriente**|37,6|736.622|5.850.392|√|√|√|√|
|**Hualqui**|**Hualqui**|39,17|684.073|5.905.626|√|√|√|√|

1 Las siglas indican: temperatura (T), velocidad del viento (VV), dirección del viento (DV) y humedad relativa (Hr).
2 No presenta serie de datos meteorológicos disponibles para el periodo de análisis.
3 Presenta serie de datos meteorológicos disponibles solo para el periodo 2021 y 2022.

De la Tabla 117, se puede apreciar que la estación Laja se encuentra a una mayor

proximidad del perímetro de la planta y dispone de serie de datos meteorológicos para el

periodo 2020 al 2022. Según la Tabla 118, la Estación Laja dispone sobre un 70% de datos

de la serie de tiempo meteorológica, por lo que es seleccionada como la estación de

referencia para analizar la meteorología.

**Tabla 118. Datos de la estación meteorológica superficial seleccionada.**

|Nombre<br>estación|Distancia<br>al<br>perímetro<br>del<br>proyecto<br>(km)|Altura<br>m.s.n.m<br>(m)2|Coordenadas UTM<br>Datum WGS 84 Huso<br>18|Col5|Variables meteorológicas1|Col7|Col8|Col9|% datos disponibles4|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Nombre**<br>**estación**|**Distancia**<br>**al**<br>**perímetro**<br>**del**<br>**proyecto**<br>**(km)**|**Altura**<br>**m.s.n.m**<br>**(m)2 **|**Este (m)**|**Norte (m)**|**T3 **|**VV3 **|**DV3 **|**Hr3 **|**Hr3 **|**Hr3 **|**Hr3 **|
|**Nombre**<br>**estación**|**Distancia**<br>**al**<br>**perímetro**<br>**del**<br>**proyecto**<br>**(km)**|**Altura**<br>**m.s.n.m**<br>**(m)2 **|**Este (m)**|**Norte (m)**|**T3 **|**VV3 **|**DV3 **|**Hr3 **|**2020**|**2021**|**2022**|
|**Laja**|1,83|68,33|702.992|5.872.963|√|√|√|√|96%|97,1%|95,3%|

1 Extraído del Sistema de Información Nacional de Calidad del Aire.

2 Extraído desde GRD generado en conjunto con el archivo WRF, el cual extrae datos desde GMTED2010 desde
[https://www.usgs.gov/coastal-changes-and-impacts/gmted2010](https://www.usgs.gov/coastal-changes-and-impacts/gmted2010)
3 Las siglas indican: temperatura (T), velocidad del viento (VV), dirección del viento (DV) y humedad relativa (Hr).
4 Estimado a partir de la disponibilidad de datos de velocidad del viento.

119

##### - 9.4. APENDICE 4 Análisis meteorológico de Datos Observados y Modelados

En esta sección se presenta el análisis entre los datos observados y modelados, del periodo

01-01-2020 al 01-01-2023, en la estación Laja, es decir para los años 2020, 2021 y 2022, y

el análisis de incertidumbre entre los datos observados y modelados.

Siguiendo los lineamientos establecidos en la “ _Guía para el uso de modelos de calidad del_

_aire en el SEIA_ ” (2023), para el análisis de la incertidumbre se consideraron los índices

estadísticos cuantitativos error cuadrático medio (RMSE), error absoluto medio (MAE),

sesgo estadístico (BIAS) y el índice de correlación (r), entre los datos observados en la

estación Laja y los datos modelados en la localización de la estación.

El RMSE entrega una medida promedio de la magnitud al cuadrado de los errores, se calcula

mediante la Ecuación 3. Mientas más pequeño sea el valor RMSE, mejor es el ajuste de los

datos observados y modelados.

IJ

RMSE= √ [1]

J

I

i

IJ [∑∑(P] [j]

i −O i

[j] j

i ) 2

**Ecuación 3.**

**Error cuadrático**

**medio.**

j=1

i=1

Donde,

I: corresponde al número total de lugares de observación.
J: corresponde al número total de observaciones temporales.
j: corresponde al tiempo.
i: corresponde al lugar de observación.
P: corresponde a la variable predicha por el modelo.
O: corresponde a la variable observada/medida.

El MAE, entrega la diferencia absoluta entre los datos observados y modelados, se

determina a partir de la Ecuación 4. y el valor optimo del indicador es cero.

J

I

MAE= [1]

i −O i

[j] j

ij |

i

IJ [∑∑|P] [j]

**Ecuación 4.**

**Error absoluto.**

j=1

i=1

A partir del BIAS, determinado según la Ecuación 5., se puede analizar si el modelo

sobreestima (sesgo positivo) o subestima la variable en cuestión (sesgo negativo), mientras

más cercano a cero sea el valor, mejor es la estimación.

J

I

BIAS= [1]

i −O i

[j] j

i )

i

IJ [∑∑(P] [j]

**Ecuación 5.**

**Sesgo**

**estadístico.**

120

j=1

i=1

Por último, se calcula el coeficiente de correlación para determinar la correlación entre los

datos observados y los datos modelados. Cuanto más cercano a 0 es la correlación, más

débil es la capacidad de predicción del modelo. Los valores de r negativos indican una

correlación negativa, en la que los valores de una variable tienden a incrementar mientras

los valores de la otra variable disminuyen. Por su parte, valores de r positivos indican

correlación positiva y que ambas variables incrementan a la par.

**Ecuación 6.**

**Índice de**

**correlación.**

r=

∑ ni=1 (P i −M P ) ∙(O i −M O )

~~√~~ ∑ ~~n~~ i=1 (P i −M P ) [2] ∙∑ ~~n~~ i=1 (O i −M O ) [2]

Donde,
M O : corresponde a la media muestral de los datos observados. Corresponde a
1 n

i=1 O i .
n [∑]

M P : corresponde a la media muestral de los datos predichos. Corresponde a

1 ni=1 P i .

n [∑]

Los índices obtenidos se evaluaron según criterios estadísticos de aceptación definidos en

la “ _Guía para el uso de modelos de calidad del aire en el SEIA_ ” (2023) . A continuación, se

presentan los parámetros para temperatura superficial y velocidad del viento.

**Tabla 119. Criterios estadísticos de aceptación de la predicción proporcionada para un modelo**

**meteorológico** [1] **.**

|Variable Meteorológica|Criterio de validez según parámetro estadístico|Col3|Col4|Col5|
|---|---|---|---|---|
|**Variable Meteorológica**|**RMSE**|**MAE**|**BIAS**|**r **|
|**Temperatura Superficial**|≤ 4,5 °C|≤ 4 °C|≤ ± 4°C|≥ 0,8|
|**Velocidad Viento**|≤ 3,5 m/s|≤ 3 m/s|≤ ± 2,5 m/s|≥ 0,6|

**Fuente:** Servicio de evaluación ambiental 2023.

##### 9.4.1. Meteorología 2020 a. Viento

El análisis del viento se divide en dos secciones, que corresponden a la velocidad del viento

(magnitud) y su dirección. En la presente sección se analiza las rosas de viento de los datos

observados y los obtenidos por el modelo. En las subsecciones siguientes, se presenta el

análisis del ciclo diario de la velocidad y dirección del viento, series de tiempo de la

velocidad y dirección del viento y los ciclos estacionales de la velocidad y dirección del

viento.

1 Servicio de Evaluación de Impacto Ambiental. 2023. Guía para el uso de modelos de calidad del aire en el

SEIA.

121

Para el periodo 2020, se puede apreciar que la dirección del viento predominante de los

datos observados proviene del sur sureste con una frecuencia de incidencia inferior al 7,8%.

Los datos observados poseen una frecuencia de vientos calmos del 25,36% (velocidad

inferior a 0,5 m/s). La velocidad promedio es de 1,19 m/s y la dirección resultante del viento

proviene del sur suroeste (220°).

Los datos modelados para el mismo periodo en la estación Laja, presentan una dirección

del viento predominante que proviene del sur sureste con una frecuencia de incidencia

inferior al 10%. Los datos modelados poseen una frecuencia de vientos calmos del 13%. La

velocidad promedio es de 2,12 m/s y la dirección resultante del viento proviene del sur

sureste (133°).

**Figura 21. Rosa de viento año 2020 datos observados en estación Laja (izquierda) y modelados WRF**

**(derecha). UTC+00.**

Para visualizar las diferencias horarias entre los datos observados y modelados en la

estación Laja, se procede a presentar las rosas de viento en horario de 08:00 a 18:00 y 18:00

a 08:00 UTC+00.

122

**Figura 22. Rosa de viento año 2020: Horario 08:00 a 18:00. Datos observados en estación Laja**

**(izquierda) y modelados WRF (derecha). UTC+00.**

**Figura 23. Rosa de viento año 2020: Horario 18:00 a 8:00. Datos observados en estación Laja (izquierda) y**

**modelados WRF (derecha). UTC+00.**

##### b. Velocidad del Viento

En el ciclo diario de la velocidad del viento observada en la estación Laja (Figura 24), se

puede apreciar un decrecimiento de la velocidad del viento entre las 00:00 a las 09:00

UTC+00, para luego incrementar hasta las 19:00 UTC+00 y volver a disminuir. El ciclo diario

de la velocidad del viento modelado posee un comportamiento similar para el

decrecimiento de la velocidad del viento, generándose su incremento hasta las 18:00 y

volver a disminuir (Figura 25). Los datos modelados presentan una mayor magnitud que los

datos observados de la velocidad del viento.

123

**Figura 24. Ciclo diario de la velocidad del viento observada en la estación Laja (m/s). UTC+00. Año 2020.**

**Figura 25. Ciclo diario de la velocidad del viento modelada en la estación Laja (m/s). UTC+00. Año 2020.**

En la distribución de datos de la serie de tiempo observada (Figura 26), se puede apreciar
un menor rango de velocidad del viento que los datos modelados (Figura 27).

124

**Figura 26. Serie de tiempo de la velocidad del viento observada en la estación Laja (m/s). UTC+00. Año**

**2020.**

**Figura 27. Serie de tiempo de la velocidad del viento modelada en la estación Laja (m/s). UTC+00. Año**

**2020.**

Del análisis del ciclo estacional, se puede apreciar que los datos observados presentan una

menor magnitud horario mensual de la velocidad del viento que los datos modelados (ver

Figura 28 y Figura 29).

125

**Figura 28. Ciclo estacional de la velocidad del viento observada en la estación Laja (m/s). UTC+00. Año**

**2020.**

**Figura 29. Ciclo estacional de la velocidad del viento modelada en la estación Laja (m/s). UTC+00. Año**

**2020.**

##### c. Dirección del Viento

En el ciclo diario de la dirección del viento observada (Figura 30), se puede apreciar que

durante las 00:00 a las 08:00 UTC+00, el viento proviene entre el este noreste y el oeste

noroeste, para luego durante las 09:00 a las 12:00 UTC+00 provenir entre el este noreste y

el oeste suroeste y durante las 13:00 a las 23:00 UTC+00 provenir entre el sur sureste y el

oeste noroeste.

126

En el ciclo diario de la dirección del viento modelada (Figura 31), se puede apreciar que

durante las 00:00 a 02:00 UTC+00, el viento proviene entre el sur sureste y el oeste

noroeste, para luego durante las 02:00 a las 16:00 UTC+00 provenir entre el este noreste y

el sur suroeste y durante las 17:00 a las 23:00 provenir entre el sur sureste y el oeste

noroeste.

**Figura 30. Ciclo diario de la dirección del viento observada en la estación Laja (°). UTC+00. Año 2020.**

**Figura 31. Ciclo diario de la dirección del viento modelada en la estación Laja (°). UTC+00. Año 2020.**

En la serie de tiempo de datos observados y datos modelados, se puede apreciar vientos
procedentes entre el noreste y el suroeste, moviéndose su procedencia en sentido horario
(Figura 32 y Figura 33).

127

**Figura 32. Serie de tiempo de la dirección del viento observada en la estación Laja (°). UTC+00. Año 2020.**

**Figura 33. Serie de tiempo de la dirección del viento modelada en la estación Laja (°). UTC+00. Año 2020.**

En los datos observados del ciclo estacional, se aprecia que la dirección del viento en horario
00:00 a 12:00 UTC+00 proviene entre el este sureste y el oeste suroeste, y en horario de
13:00 a 23:00 UTC+00 proviene entre el sur sureste y oeste suroeste (Figura 34).

En los datos modelados del ciclo estacional, se aprecia que la dirección del viento proviene

entre el este noreste y el sur suroeste (Figura 35).

128

**Figura 34. Ciclo estacional de la dirección del viento observada en la estación Laja (°). UTC+00. Año 2020.**

**Figura 35. Ciclo estacional de la dirección del viento modelada en la estación Laja (°). UTC+00. Año 2020.**

##### d. Temperatura

El análisis de la temperatura presenta los ciclos diarios, series de tiempo y los ciclos

estacionales de los datos observados y aquellos obtenidos por el modelo WRF.

Los datos observados de temperatura en la estación Laja presentan una amplitud entre 0,38

a 39°C y una temperatura promedio de 16 °C (Figura 36). En el ciclo diario de la temperatura

observada, se puede apreciar una disminución de su magnitud hasta las 10:00 UTC+00, para

luego incrementar hasta las 19:00 y volver a disminuir.

Los datos modelados de temperatura en la estación Laja presentan una amplitud entre 1,4

a 27,7 °C y una temperatura promedio de 12,4°C (Figura 37). En el ciclo diario de la

129

temperatura modelada, se puede apreciar un comportamiento horario similar al de los

datos observados.

**Figura 36. Ciclo diario de la temperatura observada en la estación Laja (°C). UTC+00. Año 2020.**

**Figura 37. Ciclo diario de la temperatura modelada en la estación Laja (°C). UTC+00. Año 2020.**

Las series de tiempo de los datos observados y modelados presentan un decrecimiento de

la temperatura en las estaciones de otoño e invierno y un incremento cuando son las

estaciones de primavera y verano (Figura 38 y Figura 39). Los datos observados presentan

mayores máximos y mínimos diarios que los datos modelados.

130

**Figura 38. Serie de tiempo de la temperatura observada en la estación Laja (°C). UTC+00. Año 2020.**

**Figura 39. Serie de tiempo de la temperatura modelada en la estación Laja (°C). UTC+00. Año 2020.**

En los ciclos estacionales, se puede apreciar que la amplitud de datos observados es mayor
que los datos modelados (Figura 40 y Figura 41). Se observa una tendencia en la que los
datos observados presentan mayores temperaturas horario mensuales para todo el año,
con excepción de julio y agosto en horario 06:00 a 12:00 UTC+00.

131

**Figura 40. Ciclo estacional de la temperatura del viento observada en la estación Laja (°C). UTC+00. Año**

**2020.**

**Figura 41. Ciclo estacional de la temperatura del viento modelada en la estación Laja (°C). UTC+00. Año**

**2020.**

##### e. Humedad relativa

El análisis de la humedad relativa presenta los ciclos diarios, series de tiempo y los ciclos

estacionales de los datos observados y aquellos obtenidos por el modelo WRF.

Los datos observados de la humedad relativa en la estación Laja presentan una amplitud de

datos entre 1 al 100% y una humedad relativa promedio de 68,4% (Figura 42). En el ciclo

132

diario de la humedad relativa observada, se puede apreciar un incremento de su magnitud

hasta las 09:00, para luego disminuir hasta las 19:00 y volver a incrementar.

Los datos modelados de la humedad relativa en la estación Laja presentan una amplitud de

datos entre 32,3 a 100% y una humedad relativa promedio de 95,68% (Figura 43). El ciclo

diario de la humedad relativa modelada presenta un comportamiento similar al de los datos

observados, con una menor amplitud horaria.

**Figura 42. Ciclo diario de la humedad relativa observada en la estación Laja (%). UTC+00. Año 2020.**

**Figura 43. Ciclo diario de la humedad relativa modelada en la estación Laja (%). UTC+00. Año 2020.**

Las series de tiempo de los datos observados y los modelados presentan un incremento de

la humedad relativa en las estaciones de otoño e invierno, con los datos modelados

entregando una mayor magnitud diaria de humedad relativa que los datos observados

(Figura 44 y Figura 45).

133

**Figura 44. Serie de tiempo de la humedad relativa observada en la estación Laja (%). UTC+00. Año 2020.**

**Figura 45. Serie de tiempo de la humedad relativa modelada en la estación Laja (%). UTC+00. Año 2020.**

En los ciclos estacionales, se puede apreciar que la amplitud de los datos modelados es

menor que la de los datos observados (Figura 46 y Figura 47). El análisis indica que los datos

modelados presentan una tendencia a entregar mayor humedad relativa horario mensual

que los datos observados.

**Figura 46. Ciclo estacional de la humedad relativa observada en la estación Laja (%). UTC+00. Año 2020.**

134

**Figura 47. Ciclo estacional de la humedad relativa modelada en la estación Laja (%). UTC+00. Año 2020.**

##### f. Análisis de la incertidumbre

Los resultados de los índices estadísticos evaluados para la temperatura superficial y la

velocidad del viento, se exponen en la Tabla 120.

**Tabla 120. Valores de los índices de la predicción proporcionada por el modelo para la estación**

**meteorológica. Año 2020.**

|Variable Meteorológica|Criterio de validez según parámetro estadístico|Col3|Col4|Col5|
|---|---|---|---|---|
|**Variable Meteorológica**|**RMSE**|**MAE**|**BIAS**|**r**|
|**Temperatura Superficial**|4,9 °C|4,0 °C|-3,7 °C|0,9|
|**Velocidad Viento**|1,5 m/s|1,1 m/s|0,9 m/s|0,6|

De acuerdo a los criterios de aceptación, el modelo meteorológico para la temperatura

cumple con el error absoluto medio (MAE), sesgo estadístico (BIAS), error cuadrático medio

(RMSE) y el coeficiente de correlación (r), y el RMSE se escapó ligeramente de lo

recomendado.

De acuerdo a los criterios de aceptación definidos, el modelo meteorológico para la

velocidad del viento cumple con todos.

##### 9.4.2. Meteorología 2021 a. Viento

Para el periodo 2021, se puede apreciar que la dirección del viento predominante de los

datos observados proviene del sursureste con una frecuencia de incidencia superior al 6%.

Los datos observados poseen una frecuencia de vientos calmos del 28,76% (velocidad

inferior a 0,5 m/s). La velocidad promedio es de 1,12 m/s y la dirección resultante del viento

es 260°.

135

Los datos modelados para el mismo periodo en la estación Laja, presentan una dirección

del viento predominante que proviene del sursureste con una frecuencia de incidencia

inferior al 8%. Los datos modelados poseen una frecuencia de vientos calmos del 5,82%. La

velocidad promedio es de 2,32 m/s y la dirección resultante del viento es de 148°.

**Figura 48. Rosa de viento año 2021 datos observados en estación Laja (izquierda) y modelados WRF**

**(derecha). UTC+00.**

Para visualizar las diferencias horarias entre los datos observados y modelados en la

estación Laja, se procede a presentar las rosas de viento en horario de 08:00 a 18:00 y 18:00

a 08:00 UTC+00.

**Figura 49. Rosa de viento año 2021: Horario 08:00 a 18:00. Datos observados en estación Laja**

**(izquierda) y modelados WRF (derecha). UTC+00.**

136

**Figura 50. Rosa de viento año 2021: Horario 18:00 a 8:00. Datos observados en estación Laja (izquierda) y**

**modelados WRF (derecha). UTC+00.**

##### b. Velocidad del Viento

En el ciclo diario de la velocidad del viento observada en la estación Laja (Figura 51), se

puede apreciar un decrecimiento en la velocidad del viento entre las 00:00 a las 09:00

UTC+00, para luego incrementar hasta las 20:00 UTC+00 y volver a disminuir. Por su parte,

en el ciclo diario de la velocidad del viento modelado se puede apreciar un comportamiento

similar al de los datos observados, pero los datos modelados poseen una mayor magnitud

de velocidad del viento (Figura 52).

**Figura 51. Ciclo diario de la velocidad del viento observada en la estación Laja (m/s). UTC+00. Año 2021.**

137

**Figura 52. Ciclo diario de la velocidad del viento modelada en la estación Laja (m/s). UTC+00. Año 2021.**

En la distribución de datos de la serie de tiempo observada (Figura 53), se puede apreciar
un menor rango de velocidad del viento que los datos modelados (Figura 54).

**Figura 53. Serie de tiempo de la velocidad del viento observada en la estación Laja (m/s). UTC+00. Año**

**2021.**

138

**Figura 54. Serie de tiempo de la velocidad del viento modelada en la estación Laja (m/s). UTC+00. Año**

**2021.**

Del análisis del ciclo estacional, se puede apreciar que los datos observados (Figura 55)

poseen un menor rango de datos que los modelados (Figura 56). Los datos modelados

presentan una mayor magnitud horario-mensual que los datos observados.

**Figura 55. Ciclo estacional de la velocidad del viento observada en la estación Laja (m/s). UTC+00. Año**

**2021.**

139

**Figura 56. Ciclo estacional de la velocidad del viento modelada en la estación Laja (m/s). UTC+00. Año**

**2021.**

##### c. Dirección del Viento

En el ciclo diario de la dirección del viento observada (Figura 57), se puede apreciar que

durante las 00:00 a las 08:00 UTC+00, el viento proviene entre el sursureste y el oeste

noroeste, para luego entre las 09:00 a 11:00 UTC+00 provenir entre el este noreste y el

oeste suroeste y finalmente en el tramo restante del ciclo diario, provenir entre el

sursureste y el oeste noroeste.

En el ciclo diario de la dirección del viento modelada (Figura 58), se puede apreciar que

durante las 00:00 a 08:00 UTC+00, el viento proviene entre el este noreste y el oeste

noroeste, para luego entre las 09:00 a 11:00 UTC+00 provenir entre el este noreste y el

oeste suroeste y en el tramo restante del ciclo diario, provenir entre el este noreste y el

oeste noroeste.

140

**Figura 57. Ciclo diario de la dirección del viento observada en la estación Laja (°). UTC+00. Año 2021.**

**Figura 58. Ciclo diario de la dirección del viento modelada en la estación Laja (°). UTC+00. Año 2021.**

En la serie de tiempo de datos observados y datos modelados, se puede apreciar vientos
procedentes entre el noreste y el suroeste, moviéndose su procedencia en sentido horario
(Figura 59 y Figura 60).

141

**Figura 59. Serie de tiempo de la dirección del viento observada en la estación Laja (°). UTC+00. Año 2021.**

**Figura 60. Serie de tiempo de la dirección del viento modelada en la estación Laja (°). UTC+00. Año 2021.**

En los datos observados del ciclo estacional, se aprecia que la dirección del viento en horario
00:00 a 12:00 UTC+00 proviene entre el sursureste y el oeste suroeste, y en horario 13:00
a 23:00 UTC+00 proviene entre el sur sureste y el oeste suroeste (Figura 61).

En los datos modelados del ciclo estacional, se aprecia que la dirección del viento proviene

entre el este sureste y el oeste suroeste (Figura 62).

142

**Figura 61. Ciclo estacional de la dirección del viento observada en la estación Laja (°). UTC+00. Año 2021.**

**Figura 62. Ciclo estacional de la dirección del viento modelada en la estación Laja (°). UTC+00. Año 2021.**

##### d. Temperatura

Los datos observados de temperatura en la estación Laja presentan una amplitud entre
1,28 a 41,75°C y una temperatura promedio de 14,61 °C (Figura 64). En el ciclo diario de la

temperatura observada, se puede apreciar una disminución de su magnitud hasta las 10:00

UTC+00, para luego incrementar hasta las 19:00 y volver a disminuir.

Los datos modelados de temperatura en la estación Laja presentan una amplitud entre 2,2

a 27,9 °C y una temperatura promedio de 12,53°C (Figura 65). En el ciclo diario de la

temperatura modelada, se puede apreciar un comportamiento horario similar al de los

datos observados.

143

**Figura 63. Ciclo diario de la temperatura observada en la estación Laja (°C). UTC+00. Año 2021.**

**Figura 64. Ciclo diario de la temperatura modelada en la estación Laja (°C). UTC+00. Año 2021.**

Las series de tiempo de los datos observados y modelados presentan un decrecimiento de

la temperatura en las estaciones de otoño e invierno y un incremento cuando son las

estaciones de primavera y verano (Figura 66 y Figura 67). Los datos observados presentan

mayores máximos y mínimos diarios que los datos modelados.

144

**Figura 65. Serie de tiempo de la temperatura observada en la estación Laja (°C). UTC+00. Año 2021.**

**Figura 66. Serie de tiempo de la temperatura modelada en la estación Laja (°C). UTC+00. Año 2021.**

En los ciclos estacionales, se puede apreciar que la amplitud de datos observados es mayor
que los datos modelados (Figura 68 y Figura 69). En periodo de primavera y verano, los
datos observados presentan mayores temperaturas que los modelados, mientras que, en
otoño e invierno, en horario de 00:00 a 12:00 UTC+00, los datos modelados presentan
mayores temperaturas que los datos observados, para luego en periodo 13:00 a 23:00

UTC+00 volver a la tendencia visualizada el resto del año.

145

**Figura 67. Ciclo estacional de la temperatura del viento observada en la estación Laja (°C). UTC+00. Año**

**2021.**

**Figura 68. Ciclo estacional de la temperatura del viento modelada en la estación Laja (°C). UTC+00. Año**

**2021.**

##### e. Humedad relativa

Los datos observados de la humedad relativa en la estación Laja presentan una amplitud de

datos entre 5,5 a 100% y una humedad promedio de 70,8% (Figura 69). En el ciclo diario de

la humedad relativa observada, se puede apreciar un incremento de su magnitud hasta las

09:00, para luego disminuir hasta las 19:00 y volver a incrementar.

Los datos modelados de la humedad relativa en la estación Laja presentan una amplitud de

38,5 a 100% y una humedad promedio de 85,5% (Figura 70). El ciclo diario de la humedad

146

relativa modelada presenta un comportamiento similar al de los datos observados, con una

menor amplitud horaria.

**Figura 69. Ciclo diario de la humedad relativa observada en la estación Laja (%). UTC+00. Año 2021.**

**Figura 70. Ciclo diario de la humedad relativa modelada en la estación Laja (%). UTC+00. Año 2021.**

Las series de tiempo de los datos observados y los modelados presentan un incremento de

la humedad relativa en las estaciones de otoño e invierno, con los datos modelados

entregando una mayor magnitud diaria de humedad relativa que los datos observados

(Figura 71 y Figura 72).

**Figura 71. Serie de tiempo de la humedad relativa observada en la estación Laja (%). UTC+00. Año 2021.**

147

**Figura 72. Serie de tiempo de la humedad relativa modelada en la estación Laja (%). UTC+00. Año 2021.**

En los ciclos estacionales, se puede apreciar que la amplitud de datos modelados es menor

que la de los datos observados (Figura 73 y Figura 74). El análisis indica que los datos

modelados presentan una tendencia de entregar mayor humedad relativa horario mensual

que los datos observados.

**Figura 73. Ciclo estacional de la humedad relativa observada en la estación Laja (%). UTC+00. Año 2021.**

148

**Figura 74. Ciclo estacional de la humedad relativa modelada en la estación Laja (%). UTC+00. Año 2021.**

##### f. Análisis de la incertidumbre

Los resultados de los índices estadísticos evaluados para la temperatura superficial y la

velocidad del viento, se exponen en la Tabla 121.

**Tabla 121. Valores de los índices de la predicción proporcionada por el modelo para la estación**

**meteorológica. Año 2021.**

|Variable Meteorológica|Criterio de validez según parámetro estadístico|Col3|Col4|Col5|
|---|---|---|---|---|
|**Variable Meteorológica**|**RMSE**|**MAE**|**BIAS**|**r**|
|**Temperatura Superficial**|4,1 °C|3,1°C|-2,1°C|0,9|
|**Velocidad Viento**|1,7 m/s|1,3 m/s|1,1 m/s|0,6|

De acuerdo a los criterios de aceptación definidos, el modelo meteorológico para la

temperatura y la velocidad del viento cumple con todos.

##### 9.4.3. Meteorología 2022 a. Viento

Para el periodo 2022, se puede apreciar que la dirección del viento predominante de los

datos observados proviene del sursureste con una frecuencia de incidencia superior al 6%.

Los datos observados poseen una frecuencia de vientos calmos del 25,65%. La velocidad

promedio es de 1,24 m/s y la dirección resultante del viento proviene del oeste noroeste

(291°).

Los datos modelados para el mismo periodo en la estación Laja, presentan una dirección

del viento predominante que proviene del sursureste con una frecuencia de incidencia

inferior al 10%. Los datos modelados poseen una frecuencia de vientos calmos del 8,56%.

149

La velocidad promedio es de 2,13 m/s y la dirección resultante del viento proviene del este

sureste (132°).

**Figura 75. Rosa de viento año 2022 datos observados en estación Laja (izquierda) y modelados WRF**

**(derecha). UTC+00.**

Para visualizar las diferencias horarias entre los datos observados y modelados en la

estación Laja, se procede a presentar las rosas de viento en horario de 08:00 a 18:00 y 18:00

a 08:00 UTC+00.

**Figura 76. Rosa de viento año 2022: Horario 08:00 a 18:00. Datos observados en estación Laja**

**(izquierda) y modelados WRF (derecha). UTC+00.**

150

**Figura 77. Rosa de viento año 2022: Horario 18:00 a 8:00. Datos observados en estación Laja (izquierda) y**

**modelados WRF (derecha). UTC+00.**

##### b. Velocidad del Viento

En el ciclo diario de la velocidad del viento observada en la estación Laja (Figura 78), se

puede apreciar un decrecimiento en la velocidad del viento entre las 00:00 a las 09:00

UTC+00, para luego incrementar hasta las 20:00 UTC+00 y volver a disminuir. Por su parte,

en el ciclo diario de la velocidad del viento modelado se puede apreciar un comportamiento

similar al de los datos observados, pero los datos modelados poseen una mayor magnitud

de velocidad del viento (Figura 79).

**Figura 78. Ciclo diario de la velocidad del viento observada en la estación Laja (m/s). UTC+00. Año 2022.**

151

**Figura 79. Ciclo diario de la velocidad del viento modelada en la estación Laja (m/s). UTC+00. Año 2022.**

En la distribución de datos de la serie de tiempo observada (Figura 80), se puede apreciar
un menor rango de velocidad del viento que los datos modelados (Figura 81).

**Figura 80. Serie de tiempo de la velocidad del viento observada en la estación Laja (m/s). UTC+00. Año**

**2022.**

152

**Figura 81. Serie de tiempo de la velocidad del viento modelada en la estación Laja (m/s). UTC+00. Año**

**2022.**

Del análisis del ciclo estacional, se puede apreciar que los datos observados presentan una

menor magnitud horario mensual que los datos modelados (ver Figura 82 y Figura 83).

**Figura 82. Ciclo estacional de la velocidad del viento observada en la estación Laja (m/s). UTC+00. Año**

**2022.**

153

**Figura 83. Ciclo estacional de la velocidad del viento modelada en la estación Laja (m/s). UTC+00. Año**

**2022.**

##### c. Dirección del Viento

En el ciclo diario de la dirección observada (Figura 84), se puede apreciar que durante las

00:00 a las 09:00 UTC+00, el viento proviene entre el este noreste y el oeste noroeste, para

luego entre las 10:00 a 23:00 UTC+00 provenir entre el este sureste y el oeste noroeste.

En el ciclo diario de la dirección del viento modelada (Figura 85), se puede apreciar que

durante las 00:00 a 02:00 UTC+00, el viento proviene entre el este sureste y el oeste

noroeste, para luego entre las 03:00 a 13:00 UTC+00 provenir entre el este noreste y el

oeste suroeste y en el tramo restante del ciclo diario, provenir entre el este sureste y el

oeste noroeste.

154

**Figura 84. Ciclo diario de la dirección del viento observada en la estación Laja (°). UTC+00. Año 2022.**

**Figura 85. Ciclo diario de la dirección del viento modelada en la estación Laja (°). UTC+00. Año 2022.**

En la serie de tiempo de datos observados y datos modelados, se puede apreciar vientos
procedentes entre el noreste y el suroeste (Figura 86 y Figura 87).

155

**Figura 86. Serie de tiempo de la dirección del viento observada en la estación Laja (°). UTC+00. Año 2022.**

**Figura 87. Serie de tiempo de la dirección del viento modelada en la estación Laja (°). UTC+00. Año 2022.**

En los datos observados del ciclo estacional, se aprecia que la dirección del viento en horario
00:00 a 12:00 UTC+00 proviene entre el sursureste y el oeste suroeste, y en horario 13:00
a 23:00 UTC+00 proviene entre el sur sureste y el oeste noroeste (Figura 88).

En los datos modelados del ciclo estacional, se aprecia que la dirección del viento proviene

entre el este sureste y el oeste suroeste (Figura 89).

156

**Figura 88. Ciclo estacional de la dirección del viento observada en la estación Laja (°). UTC+00. Año 2022.**

**Figura 89. Ciclo estacional de la dirección del viento modelada en la estación Laja (°). UTC+00. Año 2022.**

##### d. Temperatura

Los datos observados de temperatura en la estación Laja presentan una amplitud entre
1,85 a 36,76°C y una temperatura promedio de 12,24 °C (Figura 90). En el ciclo diario de la

temperatura observada, se puede apreciar una disminución de su magnitud hasta las 10:00

UTC+00, para luego incrementar hasta las 19:00 y volver a disminuir.

Los datos modelados de temperatura en la estación Laja presentan una amplitud entre
0,18 a 27,1 °C y una temperatura promedio de 11,91°C (Figura 91). En el ciclo diario de la

temperatura modelada, se puede apreciar un comportamiento horario similar al de los

datos observados.

157

**Figura 90. Ciclo diario de la temperatura observada en la estación Laja (°C). UTC+00. Año 2022.**

**Figura 91. Ciclo diario de la temperatura modelada en la estación Laja (°C). UTC+00. Año 2022.**

Las series de tiempo de los datos observados y modelados presentan un decrecimiento de

la temperatura en las estaciones de otoño e invierno y un incremento cuando son las

estaciones de primavera y verano (Figura 92 y Figura 93). Los datos observados presentan

mayores máximos diarios y menores mínimos diarios que los datos modelados.

158

**Figura 92. Serie de tiempo de la temperatura observada en la estación Laja (°C). UTC+00. Año 2022.**

**Figura 93. Serie de tiempo de la temperatura modelada en la estación Laja (°C). UTC+00. Año 2022.**

En los ciclos estacionales, se puede apreciar que la amplitud de datos observados es mayor
que los datos modelados (Figura 94 y Figura 95). En periodo de primavera y verano, los
datos observados presentan mayores temperaturas que los modelados, mientras que, en
otoño e invierno, en horario de 00:00 a 12:00 UTC+00, se observa una tendencia que indica
que los datos modelados presentan mayores temperaturas horario mensual que los datos
observados, para luego en periodo 13:00 a 23:00 UTC+00 volver a la tendencia visualizada

el resto del año.

159

**Figura 94. Ciclo estacional de la temperatura del viento observada en la estación Laja (°C). UTC+00. Año**

**2022.**

**Figura 95. Ciclo estacional de la temperatura del viento modelada en la estación Laja (°C). UTC+00. Año**

**2022.**

##### e. Humedad relativa

Los datos observados de la humedad relativa en la estación Laja presentan una amplitud de

datos entre 6,45 a 100% y una humedad promedio de 72% (Figura 96). En el ciclo diario de

la humedad relativa observada, se puede apreciar un incremento de su magnitud hasta las

09:00, para luego disminuir hasta las 19:00 y volver a incrementar.

160

Los datos modelados de la humedad relativa en la estación Laja presentan una amplitud de

datos entre 31,4 y 100% y una humedad promedio de 86,1% (Figura 97). El ciclo diario de la

humedad relativa moderada presenta un comportamiento similar al de los datos

observados, con una menor amplitud horaria.

**Figura 96. Ciclo diario de la humedad relativa observada en la estación Laja (%). UTC+00. Año 2022.**

**Figura 97. Ciclo diario de la humedad relativa modelada en la estación Laja (%). UTC+00. Año 2022.**

La serie de tiempo de datos observados presenta una mayor variación diaria de la humedad

relativa que los datos modelados (Figura 98 y Figura 99).

**Figura 98. Serie de tiempo de la humedad relativa observada en la estación Laja (%). UTC+00. Año 2022.**

161

**Figura 99. Serie de tiempo de la humedad relativa modelada en la estación Laja (%). UTC+00. Año 2022.**

En los ciclos estacionales, se puede apreciar que la amplitud de datos modelados es menor

que la de los datos observados (Figura 100 y Figura 101). El análisis indica que los datos

modelados presentan una tendencia con mayor magnitud de humedad relativa horario

mensual que los datos observados.

**Figura 100. Ciclo estacional de la humedad relativa observada en la estación Laja (%). UTC+00. Año 2022.**

162

**Figura 101. Ciclo estacional de la humedad relativa modelada en la estación Laja (%). UTC+00. Año 2022.**

##### f. Análisis de la incertidumbre

Los resultados de los índices estadísticos evaluados para la temperatura superficial y la

velocidad del viento, se exponen en la Tabla 122.

**Tabla 122. Valores de los índices de la predicción proporcionada por el modelo para la estación**

**meteorológica. Año 2022.**

|Variable Meteorológica|Criterio de validez según parámetro estadístico|Col3|Col4|Col5|
|---|---|---|---|---|
|**Variable Meteorológica**|**RMSE**|**MAE**|**BIAS**|**r **|
|**Temperatura Superficial**|2,9 °C|2,3°C|-0,4°C|0,9|
|**Velocidad Viento**|1,5 m/s|1,1 m/s|0,8 m/s|0,6|

De acuerdo a los criterios de aceptación del modelo meteorológico para la temperatura y

la velocidad del viento, se identifica que los datos modelados cumplen con el error

cuadrático medio (RMSE), el criterio de error absoluto medio (MAE), sesgo estadístico

(BIAS) y el coeficiente de correlación (r).

163

##### - - 9.5. APENDICE 5 Proyectos aprobados entre 2020 2023

A continuación, se presenta un listado de los proyectos aprobados en la región del Biobío entre el 01-01-2020 al 04-21-2023.

**Tabla 123. Listado proyectos aprobados.**

|Nombre proyecto|Tipo|Titular|Fecha presentación/ingreso|Cercanía al proyecto|
|---|---|---|---|---|
|Proyecto inmobiliario Los Molinos|DIA|MAESTRA QUILPUE DOS SPA|31-08-2022|No|
|Proyecto Pintor Pedro Luna|DIA|CONAVICOOP|11-08-2022|No|
|Conjunto Habitacional Cipreses de Torreones III|DIA|Inmobiliaria Villa Pacifico SpA|05-05-2022|No|
|Extracción de Áridos Sector Avaria|DIA|Sociedad Concesionaria Ruta Nahuelbuta S.A.|14-03-2022|No|
|Proyecto extracción de arena de pozo lastrero, fundo<br>Santa Gregoria|DIA|José Arner Ríos Rodríguez|24-02-2022|No|
|AMPLIACIÓN DEL CONJUNTO HABITACIONAL SAN<br>PEDRO|DIA|Inmobiliaria Socovesa Sur S.A.|22-02-2022|No|
|Extracción de Áridos Pozo Gallegos|DIA|Sociedad Concesionaria Ruta Nahuelbuta S.A.|03-02-2022|No|
|Incremento de la Autonomía Operacional para<br>Peróxido de Hidrógeno|DIA|Celulosa Arauco y Constitución S.A..|31-01-2022|No|
|Viento Norte|DIA|Inmobiliaria Costa Norte SpA|23-12-2021|No|
|Regularización Plantel Lechero y Engorda Fundo Los<br>Varones - Agropecuaria Los Varones Limitada.|DIA|Agropecuaria Los Varones Ltda.|19-11-2021|No|
|Instalación de estanque de almacenamiento de Gas<br>Licuado|DIA|Operaciones Costeras SpA|08-11-2021|No|
|Ampliación en S/E El Avellano|DIA|Compañía General de Electricidad S.A.|22-10-2021|No|
|Planta de Producción de Pellet de Madera|DIA|Eléctrica Nueva Energía S.A.|22-09-2021|No|
|Paillihue Solar|DIA|Villa Prat II Energy SpA|21-09-2021|No|
|Modificación Condominio Alto Mirador|DIA|Constructora PACAL S.A|16-09-2021|No|
|Parque Fotovoltaico El Rosal|DIA|MVC SOLAR 12 SpA|23-08-2021|No|
|Nueva Conexión y Ampliación S/E Celulosa Laja|DIA|CMPC PULP SpA|20-08-2021|Sí|
|Parque Fotovoltaico Doña Ximena|DIA|MVC SOLAR 35 SpA|23-07-2021|No|
|Extracción de Áridos desde el Río Biobío en San<br>Pedro de la Paz|DIA|INGENIERIA, MAQUINARIAS Y CONSTRUCCIONES INGEMAC<br>LIMITADA|12-07-2021|No|
|Jardines de Avellaneda II|DIA|Inmobiliaria Espacio Pacifico S.A.|06-07-2021|No|
|Ampliación Líneas de Transferencia de Productos|DIA|OXIQUIM S.A.|22-06-2021|No|
|Condominio Enrique Tirapegui|DIA|CONAVICOOP|14-06-2021|No|
|Extracción de Áridos en el kilómetro 21 de la Ruta<br>160, Parque Industrial Uno, Escuadrón, Coronel|DIA|Extraccion y Comercializacion de Aridos Lleu-Lleu Limitada|25-05-2021|No|
|Parque Solar Gamma|DIA|Parque Solar Gamma SpA|24-05-2021|No|
|Subestación La Señoraza 220/66 kV|DIA|SOCIEDAD AUSTRAL DE TRANSMISION TRONCAL S.A.|20-05-2021|Sí|

164

|Nombre proyecto|Tipo|Titular|Fecha presentación/ingreso|Cercanía al proyecto|
|---|---|---|---|---|
|Condominio Industrial Dinahue|DIA|Forestal Comaco S.A.|19-05-2021|No|
|PLANTA ASTILLADO DE MADERAS FORESOL,<br>CABRERO|DIA|FORESTAL FORESOL SPA|14-05-2021|No|
|Instalación de 2 Aerogeneradores LA Sur 2|DIA|Windkraft Cinco Chile SpA|22-04-2021|No|
|Parque Fotovoltaico Miño|DIA|Solek Chile Services SpA|21-04-2021|No|
|Minicentral El Portal|DIA|CENTRAL EL ATAJO SPA|20-04-2021|No|
|Parque Fotovoltaico Alcázar Solar|DIA|Juan Solar SPA|20-04-2021|No|
|Parque Eólico San Matías|DIA|Energía Eólica San Matias SpA|20-04-2021|No|
|Ampliación extracción y procesamiento de áridos La<br>Isla|DIA|SOCIEDAD ÁRIDOS Y ASFALTOS SERVITERRA LIMITADA|01-04-2021|No|
|Pozo Lastrero Coyanco|DIA|ARIDOS CANTARUTA LIMITADA|22-02-2021|No|
|Actualización Planta de Salmones Tomé|DIA|Salmones Camanchaca S.A.|18-02-2021|No|
|Extracción de Áridos en Río Biobío para Proyecto<br>Ampliación Conexión Vial Concepción-Chiguayante.<br>Etapa 2|DIA|Echeverria izquierdo Ingenieria y Construcción S.A.|30-12-2020|No|
|Ampliación de Capacidad del Sistema de Tratamiento<br>de Aguas servidas, Aguas San Pedro|DIA|Aguas San Pedro S.A.|23-12-2020|No|
|San Antonio Solar|DIA|SANTA BARBARA ENERGY SpA|23-12-2020|No|
|Transporte Ferroviario de insumos químicos<br>industriales desde Talcahuano a la planta CFI<br>Horcones|DIA|Ferrocarril del Pacifico S. A.|25-11-2020|No|
|Modernización Planta Elaboradora de Congelados|DIA|SOCIEDAD PESQUERA LANDES S.A.|20-11-2020|No|
|Proyecto de extracción y procesamiento de áridos<br>desde pozo lastrero, sector Munilque|DIA|Áridos NPSH SpA|17-11-2020|No|
|Plaza del Estero I y II|DIA|CONSTRUCTORA JOSE MIGUEL GARCIA Y CIA LIMITADA|16-11-2020|No|
|Nueva S/E Seccionadora JMA 220 kV|DIA|TRANSELEC S.A...|22-10-2020|No|
|Parque Eólico Rarinco|DIA|Energia Renovable Verano Tres SpA|21-10-2020|No|
|Ampliación Planta de Productos Congelados Isla<br>Rocuant|DIA|Blumar S.A.|21-10-2020|No|
|Modificación Avel Solar|DIA|SANTA LAURA ENERGY SpA|21-10-2020|No|
|Mejoramiento Planta de RIL Cerro Verde Puerto<br>Lirquén|DIA|Portuaria Lirquén S.A.|20-10-2020|No|
|Fuerte Viejo Lota|DIA|SEC Servicios de Construcción y Edificación S.A.|14-10-2020|No|
|DIA Extracción de Áridos Sector La Suerte|DIA|Sociedad Concesionaria Ruta Nahuelbuta S.A.|30-09-2020|No|
|San Eugenio Solar|DIA|San Eugenio Solar SpA|23-09-2020|No|
|Mejora Ambiental en Generación de Energía Térmica|DIA|ENERGÍAS INDUSTRIALES S.A.|23-09-2020|No|

165

|Nombre proyecto|Tipo|Titular|Fecha presentación/ingreso|Cercanía al proyecto|
|---|---|---|---|---|
|PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS<br>LOCALIDAD ANTIHUALA, TEMUCO CHICO Y LA<br>ARAUCANA|DIA|municipalidad de los alamos|22-09-2020|No|
|Bodega de Almacenamiento de Sustancias Peligrosas<br>ECOLOG|DIA|Ecolog Logistica, Almacenamiento y Distribución SpA|14-09-2020|No|
|Nuevos estanques de almacenamiento|DIA|Occidental Chemical Chile Limitada|08-09-2020|No|
|Parque Fotovoltaico Santa Pamela|DIA|Ruben Solar SPA|24-08-2020|No|
|Parque Solar Mulchén Santa Bárbara 1|DIA|TIERRA SOLAR SpA|21-08-2020|No|
|Parque Fotovoltaico María Dolores|DIA|Pedro Solar SpA|23-07-2020|No|
|Regularización Ambiental Planta de Granos|DIA|Collipulli Red Soil S.A|14-07-2020|No|
|Instalación de estanques de almacenamiento de Gas<br>Licuado|DIA|Lota Protein S.A.|10-07-2020|No|
|Planta Innovación Circular Arauco|DIA|Verde Corp SpA|22-06-2020|No|
|Parque Eólico Cabrero|DIA|Wind 3 SpA|22-06-2020|No|
|Ampliación Plantel Avícola Florida|DIA|Agrícola Sepúlveda Palou Ltda.|22-06-2020|No|
|Extracción y procesamiento de áridos, Cantera Santa<br>Rosa|DIA|Sociedad de Transportes MAF SpA.|12-06-2020|No|
|Proyecto Desarrollo Inmobiliario La Castellana|DIA|Inmobiliaria Alicante SPA|05-06-2020|No|
|PROYECTO INMOBILIARIO BORDE LAGUNA|DIA|Inmobiliaria Los Pellines S.A.|05-06-2020|No|
|Tratamiento y Esterilización de Residuos<br>Hospitalarios-HIMCE|DIA|Empresa de Servicios HIMCE Ltda.|22-05-2020|No|
|Parque Fotovoltaico Trupán|DIA|Sociedad Parque Solar Trupán SpA|22-04-2020|No|
|Parque Solar Don Martín II|DIA|Parque Solar Albor SpA|22-04-2020|No|
|Minicentral Hidroelectrica El Portal|DIA|CENTRAL EL ATAJO SPA|22-04-2020|No|
|Unidad de regasificación de etileno|DIA|Petroquim S.A.|26-03-2020|No|
|Parque Fotovoltaico Chacaico|DIA|Sol del Sur 15 SpA|20-03-2020|No|
|Parque Fotovoltaico La Colonia|DIA|LUZ DE SOL 5 SPA|20-03-2020|No|
|Modificación LTE Los Angeles Sur - Duqueco|DIA|wpd Duqueco S.p.A.|20-03-2020|No|
|Parque Fotovoltaico La Perla|DIA|MVC Solar 38 SpA|20-03-2020|No|
|Proyecto Inmobiliario Altos de Hualpén|DIA|Inmobiliaria GPR Hualpén Limitada|20-02-2020|No|
|El Avellano Solar|DIA|Santa Cecilia Solar SpA|19-02-2020|No|
|Modernización Planta de Congelados|DIA|FoodCorp Chile S.A.|19-02-2020|No|
|Sustitución del Sistema de Descarga de Efluentes de<br>la Central Termoeléctrica Laja|DIA|AES GENER S.A|19-02-2020|No|
|Brisas II|DIA|Inmobiliaria El Bosque S.A.|05-02-2020|No|
|PROYECTO FOTOVOLTAICO CE CANTERAS C9|DIA|Montajes Cielpanel SpA|24-01-2020|No|
|PROYECTO FOTOVOLTAICO CE EL AVELLANO A.9|DIA|Montajes Cielpanel SpA|24-01-2020|No|

166

|Nombre proyecto|Tipo|Titular|Fecha presentación/ingreso|Cercanía al proyecto|
|---|---|---|---|---|
|Conjunto Habitacional Cipreses de Torreones|DIA|Inmobiliaria Villa Pacifico SpA|14-01-2020|No|
|Ampliación capacidad de producción Planta<br>Talcahuano|DIA|FOSFOQUIM S.A|27-12-2019|No|
|El Olivar Solar|DIA|El Olivar Solar SpA|20-12-2019|No|
|Nueva Subestación Los Varones 220/66 kV|DIA|Besalco Energía Renovable S.A.|20-12-2019|No|
|Condominio Alto Arrayán|DIA|Constructora PACAL S.A|20-12-2019|No|
|Lomas de Coronel|DIA|Galilea de Ingeniería y Construcción|19-12-2019|No|
|Condominio Alto Mirador|DIA|Constructora PACAL S.A|02-12-2019|No|
|Duqueco Solar|DIA|Cocharcas Solar SpA|22-11-2019|No|
|Modificación Canalización Subterránea Parque Eólico<br>Alena|DIA|AR Alena SpA|22-11-2019|No|
|Instalación de 3 aerogeneradores LASUR 1|DIA|Windkraft cuatro Chile SpA|04-11-2019|No|
|Nueva Subestación Seccionadora Guindo 220/66 kV|DIA|Besalco Energía Renovable S.A.|23-09-2019|No|
|Continuidad constructiva y Ampliación Condominios<br>Los Arrayanes|DIA|Inmobiliaria Socovesa Sur S.A.|13-09-2019|No|
|AMPLIACIÓN BODEGAS DE ALMACENAMIENTO|DIA|PROQUIEL LTDA|06-09-2019|No|
|Retiro Sur C|DIA|Galilea S.A. de ingeniería y Construcción|28-08-2019|No|
|Parque Fotovoltaico Maquehue|DIA|LUZ DE SOL 1 SPA|23-08-2019|No|
|Lateral Charrúa 2|DIA|Gasoducto del Pacífico S.A.|22-08-2019|No|
|Reubicación Colegio Alemán de Los Ángeles Campus<br>Antuco|DIA|Corporación Sociedad Colegio Alemán de Los Ángeles|02-08-2019|No|
|Planta Elaboradora de Congelados y Conservas|DIA|Sociedad Martínez y Lagos Ltda.|19-07-2019|No|
|CONSTRUCCIÓN NUEVO PUENTE FERROVIARIO<br>BIOBÍO|EIA|EFE Trenes de Chile|26-06-2019|No|
|LTE Los Ángeles Sur - Duqueco|DIA|wpd Duqueco S.p.A.|21-06-2019|No|
|PARQUE FOTOVOLTAICO CORCOLENES|DIA|MVC Solar 27 SpA|20-06-2019|No|
|Planta de Pellet de Madera. Eco Indef Ltda.|DIA|Asesorías Eco Indef Ltda|24-05-2019|No|
|Parque Fotovoltaico Santa Julia|DIA|Andina Solar 17 Este SPA|23-05-2019|No|
|Nueva Subestación Seccionadora Hualqui 220/66 kV|DIA|Mataquito Transmisora de Energía S.A.|17-05-2019|No|
|Parque Fotovoltaico La Quinta|DIA|Sol del Sur 9 SpA|22-04-2019|No|
|Parque Fotovoltaico Laja|DIA|Andina Solar 10 SPA|22-04-2019|No|
|PARQUE EOLICO VIENTO SUR|EIA|Arauco Bioenergía S.A|02-04-2019|No|
|Nuevo Emisario Submarino|DIA|EWOS Chile Alimentos Ltda|22-11-2018|No|
|Renovación Emisario Submarino y Mejoramiento<br>Sistema de Control de Olores|DIA|Pesquera Fiordo Austral S.A.|21-09-2018|No|

167

|Nombre proyecto|Tipo|Titular|Fecha presentación/ingreso|Cercanía al proyecto|
|---|---|---|---|---|
|Modificación de insumo veterinario de desinfección,<br>distribución de estanques y actualización de permiso<br>ambiental sectorial No 139, Piscicultura Ketrun Rayen|DIA|Australis Mar S.A.|07-09-2018|No|
|Parque Eólico Entre Ríos|EIA|NR Entre Ríos SpA|05-06-2018|No|
|Mejoramiento del sistema de tratamiento de<br>digestato y actualización operacional del Plantel<br>Lechero Agrícola Ancali Ltda.|EIA|Agrícola Ancali Ltda|29-05-2018|No|
|Red de Alcantarillado y Planta de Tratamiento de<br>Aguas Servidas Quidico|DIA|Ilustre Municipalidad de Tirúa|24-05-2018|No|

**Fuente** : Servicio de evaluación de impacto ambiental.

El análisis de los proyectos, indica que hay 2 proyectos dentro del radio de 2 km del centroide de la planta al punto representativo del

proyecto y corresponde a los proyectos “Nueva conexión y ampliación S/E Celulosa Laja” de CMPC Pulp SpA y el proyecto “Sub estación

La señoraza 220/66 kV”. De acuerdo al seguimiento ambiental desarrollado por el SNIFA, al 21 -04-2023, ambos proyectos se

encuentran en fase de construcción.

Para el aporte de los proyectos se consideró el peor escenario de mayor aporte.

168

##### - 9.6. APENDICE 6 Resultados Modelación 3 años

En el presente estudio fueron modelados 3 años meteorológicos, por cada escenario

evaluado. Para estimar el peor escenario, se determina la mayor concentración ambiental

en cada receptor, de acuerdo a los 3 años de estudio y también la mayor concentración

ambiental para los puntos de máximo impacto (PMI).

A continuación, se presentan las tablas con las concentraciones ambientales para cada año

y la selección de la mayor concentración en receptores para cada escenario, que es la que

se emplea para evaluar el aporte del proyecto.

##### 9.6.1. Escenario 1

**Tabla 124. Promedio anual de la concentración de MP** **10** **-** **Escenario 1.**

|Receptor|Aporte Proyecto promedio anual<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto promedio anual<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 125. Percentil 98 de la concentración diaria de MP** **10** **-** **Escenario 1.**

|Receptor|Aporte Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|1|1|1|1|
|Receptor 3|0|0|0|0|
|Receptor 4|0|1|0|1|
|Receptor 5|1|1|1|1|
|Receptor 6|1|1|1|1|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|1|1|1|1|

**Tabla 126. Promedio anual de la concentración de MP** **2.5** **-** **Escenario 1.**

|Receptor|Aporte Proyecto promedio anual<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto promedio anual<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

169

**Tabla 127. Percentil 98 de la concentración diaria de MP** **2.5** **-** **Escenario 1.**

|Receptor|Aporte Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|1|1|1|1|
|Receptor 3|0|0|0|0|
|Receptor 4|0|1|0|1|
|Receptor 5|1|1|1|1|
|Receptor 6|1|1|1|1|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|1|1|0|1|

**-**
**Tabla 128. Promedio anual de la tasa de deposición del material particulado sedimentable (MPS)**

**Escenario 1.**

|Receptor|Aporte Proyecto tasa de deposición promedio<br>anual (mg/m2N/d)|Col3|Col4|Aporte máximo Proyecto tasa de deposición<br>promedio anual (mg/m2N/d)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 129. Promedio anual de la concentración de dióxido de nitrógeno (NO** **2** **)** **-** **Escenario 1.**

|Receptor|Aporte Proyecto promedio anual<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto promedio anual<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|1|1|1|1|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|1|1|1|1|
|Receptor 6|1|1|1|1|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 130. Percentil 99 de la concentración horaria de NO** **2** **-** **Escenario 1.**

|Receptor|Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|7|6|7|7|
|Receptor 2|4|5|4|5|
|Receptor 3|5|5|6|6|
|Receptor 4|3|4|3|4|
|Receptor 5|7|7|7|7|
|Receptor 6|9|9|11|11|
|Estación Laja|2|2|2|2|
|Estación San<br>Rosendo|3|3|3|3|

**Tabla 131. Promedio anual de la concentración de dióxido de azufre (SO** **2** **)** **-** **Escenario 1.**

170

|Receptor|Aporte Proyecto promedio anual<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto promedio anual<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 132. Percentil 99 de la concentración diaria de SO** **2** **-** **Escenario 1.**

|Receptor|Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 24 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 24 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|1|1|1|
|Receptor 2|1|2|1|2|
|Receptor 3|0|1|0|1|
|Receptor 4|1|1|1|1|
|Receptor 5|2|2|1|2|
|Receptor 6|1|2|1|2|
|Estación Laja|1|1|1|1|
|Estación San<br>Rosendo|1|1|1|1|

**Tabla 133. Percentil 98,5 de la concentración de 1 h de SO** **2** **-** **Escenario 1.**

|Receptor|Aporte Proyecto Percentil 98,5 de la<br>concentración en inmisión 1 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 98,5 de la<br>concentración en inmisión 1 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|1|1|1|1|
|Receptor 2|2|3|2|3|
|Receptor 3|1|1|1|1|
|Receptor 4|2|2|2|2|
|Receptor 5|3|3|3|3|
|Receptor 6|2|3|2|3|
|Estación Laja|1|1|1|1|
|Estación San<br>Rosendo|2|2|2|2|

**Tabla 134. Percentil 99,7 de la concentración diaria de SO** **2** **-** **Escenario 1.**

|Receptor|Aporte Proyecto Percentil 99,7 de la<br>concentración en inmisión 24 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99,7 de la<br>concentración en inmisión 24 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|1|2|1|2|
|Receptor 2|2|2|1|2|
|Receptor 3|1|2|0|2|
|Receptor 4|1|2|1|2|
|Receptor 5|2|3|2|3|
|Receptor 6|2|2|2|2|
|Estación<br>Laja|1|1|1|1|
|Estación San<br>Rosendo|2|1|1|2|

**Tabla 135. Percentil 99,73 de la concentración horaria de SO** **2** **-** **Escenario 1.**

171

|Receptor|Aporte Proyecto Percentil 99,73 de la<br>concentración en inmisión 1 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99,73 de la<br>concentración en inmisión 1 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|3|5|3|5|
|Receptor 2|5|6|5|6|
|Receptor 3|2|3|2|3|
|Receptor 4|4|4|4|4|
|Receptor 5|5|7|6|7|
|Receptor 6|4|7|5|7|
|Estación<br>Laja|2|3|3|3|
|Estación San<br>Rosendo|3|3|2|3|

**Tabla 136. Percentil 99 de la concentración de 1 h de CO** **-** **Escenario 1.**

|Receptor|Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (mg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (mg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 137. Percentil 99 de la concentración 8 h de CO** **-** **Escenario 1.**

|Receptor|Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 8 h (mg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 8 h (mg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 138. Concentración diaria de TRS** **-** **Escenario 1.**

|Receptor|Aporte Proyecto Concentración diaria<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto concentración diaria<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|

172

|Receptor|Aporte Proyecto Concentración diaria<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto concentración diaria<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 139. Concentración horaria de TRS** **-** **Escenario 1.**

|Receptor|Aporte Proyecto concentración horaria<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto concentración horaria<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

##### 9.6.2. Escenario 2

**Tabla 140. Promedio anual de la concentración de MP** **10** **-** **Escenario 2.**

|Receptor|Aporte Proyecto promedio anual<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto promedio anual<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 141. Percentil 98 de la concentración diaria de MP** **10** **-** **Escenario 2.**

|Receptor|Aporte Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|1|1|1|1|
|Receptor 3|0|0|0|0|
|Receptor 4|0|1|1|1|
|Receptor 5|1|1|1|1|
|Receptor 6|1|1|1|1|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|1|1|1|1|

**Tabla 142. Promedio anual de la concentración de MP** **2.5** **-** **Escenario 2.**

|Receptor|Aporte Proyecto promedio anual<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto promedio anual<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|

173

|Receptor|Aporte Proyecto promedio anual<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto promedio anual<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 143. Percentil 98 de la concentración diaria de MP** **2.5** **-** **Escenario 2.**

|Receptor|Aporte Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|1|1|1|1|
|Receptor 3|0|0|0|0|
|Receptor 4|0|1|0|1|
|Receptor 5|1|1|1|1|
|Receptor 6|1|1|1|1|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|1|1|0|1|

**-**
**Tabla 144. Promedio anual de la tasa de deposición del material particulado sedimentable (MPS)**

**Escenario 2.**

|Receptor|Aporte Proyecto tasa de deposición promedio<br>anual (mg/m2N/d)|Col3|Col4|Aporte máximo Proyecto tasa de deposición<br>promedio anual (mg/m2N/d)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 145. Promedio anual de la concentración de dióxido de nitrógeno (NO** **2** **)** **-** **Escenario 2.**

|Receptor|Aporte Proyecto promedio anual<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto promedio anual<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|1|1|1|1|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|1|1|1|1|
|Receptor 6|1|1|1|1|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|1|0|1|

**Tabla 146. Percentil 99 de la concentración horaria de NO** **2** **-** **Escenario 2.**

174

|Receptor|Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|6|6|6|6|
|Receptor 2|4|5|4|5|
|Receptor 3|5|5|6|6|
|Receptor 4|3|4|4|4|
|Receptor 5|7|7|7|7|
|Receptor 6|8|10|10|10|
|Estación Laja|2|3|3|3|
|Estación San<br>Rosendo|3|3|3|3|

**Tabla 147. Promedio anual de la concentración de dióxido de azufre (SO** **2** **)** **-** **Escenario 2.**

|Receptor|Aporte Proyecto promedio anual<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto promedio anual<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 148. Percentil 99 de la concentración diaria de SO** **2** **-** **Escenario 2.**

|Receptor|Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 24 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 24 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|1|1|1|1|
|Receptor 2|1|2|1|2|
|Receptor 3|0|1|0|1|
|Receptor 4|1|1|1|1|
|Receptor 5|2|2|1|2|
|Receptor 6|1|2|1|2|
|Estación Laja|1|1|1|1|
|Estación San<br>Rosendo|1|1|1|1|

**Tabla 149. Percentil 98,5 de la concentración de 1 h de SO** **2** **-** **Escenario 2.**

|Receptor|Aporte Proyecto Percentil 98,5 de la<br>concentración en inmisión 1 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 98,5 de la<br>concentración en inmisión 1 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|1|2|1|2|
|Receptor 2|3|3|3|3|
|Receptor 3|1|1|1|1|
|Receptor 4|2|2|2|2|
|Receptor 5|3|4|3|4|
|Receptor 6|2|3|3|3|
|Estación Laja|1|2|2|2|
|Estación San<br>Rosendo|2|2|2|2|

**Tabla 150. Percentil 99,7 de la concentración diaria de SO** **2** **-** **Escenario 2.**

175

|Receptor|Aporte Proyecto Percentil 99,7 de la<br>concentración en inmisión 24 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99,7 de la<br>concentración en inmisión 24 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|1|2|1|2|
|Receptor 2|2|2|1|2|
|Receptor 3|1|2|1|2|
|Receptor 4|1|2|1|2|
|Receptor 5|2|3|2|3|
|Receptor 6|2|2|2|2|
|Estación<br>Laja|1|1|1|1|
|Estación San<br>Rosendo|2|1|1|2|

**Tabla 151. Percentil 99,73 de la concentración horaria de SO** **2** **-** **Escenario 2.**

|Receptor|Aporte Proyecto Percentil 99,73 de la<br>concentración en inmisión 1 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99,73 de la<br>concentración en inmisión 1 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|4|6|5|6|
|Receptor 2|5|6|5|6|
|Receptor 3|3|3|3|3|
|Receptor 4|4|5|5|5|
|Receptor 5|6|7|6|7|
|Receptor 6|5|7|5|7|
|Estación<br>Laja|3|3|3|3|
|Estación San<br>Rosendo|3|3|3|3|

**Tabla 152. Percentil 99 de la concentración de 1 h de CO** **-** **Escenario 2.**

|Receptor|Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (mg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (mg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 153. Percentil 99 de la concentración 8 h de CO** **-** **Escenario 2.**

|Receptor|Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 8 h (mg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 8 h (mg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

176

**Tabla 154. Concentración diaria de TRS** **-** **Escenario 2.**

|Receptor|Aporte Proyecto Concentración diaria<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto concentración diaria<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 155. Concentración horaria TRS** **-** **Escenario 2.**

|Receptor|Aporte Proyecto concentración horaria<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto concentración horaria<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

##### 9.6.3. Escenario 3

**Tabla 156. Promedio anual de la concentración de MP** **10** **-** **Escenario 3.**

|Receptor|Aporte Proyecto promedio anual<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto promedio anual<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|1|1|1|1|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|1|1|1|1|
|Receptor 6|1|1|1|1|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 157. Percentil 98 de la concentración diaria de MP** **10** **-** **Escenario 3.**

|Receptor|Aporte Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|7|7|7|7|
|Receptor 2|1|1|1|1|
|Receptor 3|2|1|1|2|
|Receptor 4|0|0|0|0|
|Receptor 5|8|7|8|8|
|Receptor 6|10|9|14|14|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

177

**Tabla 158. Promedio anual de la concentración de MP** **2.5** **-** **Escenario 3.**

|Receptor|Aporte Proyecto promedio anual<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto promedio anual<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 159. Percentil 98 de la concentración diaria de MP** **2.5** **-** **Escenario 3.**

|Receptor|Aporte Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|1|1|1|1|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|1|1|1|1|
|Receptor 6|1|1|1|1|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**-**
**Tabla 160. Promedio anual de la tasa de deposición del material particulado sedimentable (MPS)**

**Escenario 3.**

|Receptor|Aporte Proyecto tasa de deposición promedio<br>anual (mg/m2N/d)|Col3|Col4|Aporte máximo Proyecto tasa de deposición<br>promedio anual (mg/m2N/d)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 161. Promedio anual de la concentración de dióxido de nitrógeno (NO** **2** **)** **-** **Escenario 3.**

|Receptor|Aporte Proyecto promedio anual<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto promedio anual<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|

178

|Receptor|Aporte Proyecto promedio anual<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto promedio anual<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**<br>1|**2021**<br>1|**2022**<br>0|**2020-2022**<br>1|
|Receptor 5|Receptor 5|Receptor 5|Receptor 5|Receptor 5|
|Receptor 6|1|1|1|1|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 162. Percentil 99 de la concentración horaria de NO** **2** **-** **Escenario 3.**

|Receptor|Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|11|8|10|11|
|Receptor 2|3|3|3|3|
|Receptor 3|6|4|4|6|
|Receptor 4|2|2|2|2|
|Receptor 5|8|8|8|8|
|Receptor 6|13|12|12|13|
|Estación Laja|1|1|1|1|
|Estación San<br>Rosendo|0|0|1|1|

**Tabla 163. Promedio anual de la concentración de dióxido de azufre (SO** **2** **)** **-** **Escenario 3.**

|Receptor|Aporte Proyecto promedio anual<br>(μg/m3N)|Col3|Col4|Aporte máximo Proyecto promedio anual<br>(μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 164. Percentil 99 de la concentración diaria de SO** **2** **-** **Escenario 3.**

|Receptor|Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 24 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 24 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 165. Percentil 98,5 de la concentración de 1 h de SO** **2** **-** **Escenario 3.**

|Receptor|Aporte Proyecto Percentil 98,5 de la<br>concentración en inmisión 1 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 98,5 de la<br>concentración en inmisión 1 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|

179

|Receptor|Aporte Proyecto Percentil 98,5 de la<br>concentración en inmisión 1 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 98,5 de la<br>concentración en inmisión 1 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 166. Percentil 99,7 de la concentración diaria de SO** **2** **-** **Escenario 3.**

|Receptor|Aporte Proyecto Percentil 99,7 de la<br>concentración en inmisión 24 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99,7 de la<br>concentración en inmisión 24 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación<br>Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 167. Percentil 99,73 de la concentración horaria de SO** **2** **-** **Escenario 3.**

|Receptor|Aporte Proyecto Percentil 99,73 de la<br>concentración en inmisión 1 h (μg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99,73 de la<br>concentración en inmisión 1 h (μg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación<br>Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 168. Percentil 99 de la concentración de 1 h de CO** **-** **Escenario 3.**

|Receptor|Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (mg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (mg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

**Tabla 169. Percentil 99 de la concentración 8 h de CO** **-** **Escenario 3.**

180

|Receptor|Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 8 h (mg/m3N)|Col3|Col4|Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 8 h (mg/m3N)|
|---|---|---|---|---|
|**Receptor**|**2020**|**2021**|**2022**|**2020-2022**|
|Receptor 1|0|0|0|0|
|Receptor 2|0|0|0|0|
|Receptor 3|0|0|0|0|
|Receptor 4|0|0|0|0|
|Receptor 5|0|0|0|0|
|Receptor 6|0|0|0|0|
|Estación Laja|0|0|0|0|
|Estación San<br>Rosendo|0|0|0|0|

181

##### 9.6.4. PMI

Los puntos de máximo impacto se evaluaron en los 3 años modelados para cada escenario y se determinó cual es el año que presenta

el mayor PMI y cuáles son sus coordenadas, presentado en la tabla a continuación.

**Tabla 170. Resumen de PMI para cada MP y** **gas emitido en los escenarios.**

|PMI|Estadístico|2020|2021|2022|Max|Año|Coordenadas UTM|Col9|
|---|---|---|---|---|---|---|---|---|
|**PMI**|**Estadístico**|**2020**|**2021**|**2022**|**Max**|**Año**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|
|**PMI**|**Estadístico**|**2020**|**2021**|**2022**|**Max**|**Año**|**Este (m)**|**Norte (m)**|
|Escenario 1|Promedio anual MP10 (μg/m3)|0|0|0|0|2022|702.904,58|5.870.494,68|
|Escenario 1|Percentil 98 concentración 24 horas MP10 (μg/m3)|2|2|2|2|2022|702.904,58|5.870.494,68|
|Escenario 1|Promedio anual MP2,5 (μg/m3)|0|0|0|0|2022|702.904,58|5.870.494,68|
|Escenario 1|Percentil 98 concentración 24 horas MP2,5 (μg/m3)|2|2|2|2|2022|702.904,58|5.870.494,68|
|Escenario 1|Promedio anual tasa de deposición MPS (mg/m2/d)|6|7|6|7|2021|701.948,4|5.872.519,81|
|Escenario 1|Concentración 24h de SO2, P99 (μg/m3)|2|2|1|2|2021|702.686,41|5.871.322,12|
|Escenario 1|Concentración 1h de SO2, P98,5 (μg/m3)|3|3|3|3|2021|702.686,41|5.871.322,12|
|Escenario 1|Promedio Anual SO2 (μg/m3)|0|0|0|0|2021|702.686,41|5.871.322,12|
|Escenario 1|Concentración 24h SO2, P99,7 (μg/m3)|2|3|2|3|2021|702.686,41|5.871.322,12|
|Escenario 1|Concentración 1h SO2, P99,73 (μg/m3)|5|7|6|7|2021|702.686,41|5.871.322,12|
|Escenario 1|Concentración 1h NO2, P99 (μg/m3)|85|85|92|92|2022|702.904,58|5.870.494,68|
|Escenario 1|Concentración NO2 (μg/m3)|5|5|5|5|2022|702.904,58|5.870.494,68|
|Escenario 1|Concentración 1h CO, P99 (mg/m3)|0|0|0|0|2022|702.904,58|5.870.494,68|
|Escenario 1|Concentración 8h móvil CO, P99 (mg/m3)|0|0|0|0|2022|702.904,58|5.870.494,68|
|Escenario 1|Concentración 24h TRS (μg/m3)|0|0|0|0|2020|702.686,41|5.871.322,12|
|Escenario 1|Concentración 1h TRS (μg/m3)|0|0|0|0|2021|702.519|5.871.048|
|Escenario 2|Promedio anual MP10 (μg/m3)|0|0|0|0|2021|702.686,41|5.871.322,12|
|Escenario 2|Percentil 98 concentración 24 horas MP10 (μg/m3)|1|1|1|1|2020|702.904,58|5.870.494,68|
|Escenario 2|Promedio anual MP2,5 (μg/m3)|0|0|0|0|2021|702.904,58|5.870.494,68|
|Escenario 2|Percentil 98 concentración 24 horas MP2,5 (μg/m3)|1|1|1|1|2020|702.904,58|5.870.494,68|
|Escenario 2|Promedio anual tasa de deposición MPS (mg/m2/d)|9|10|8|10|2021|701.948,4|5872520|

182

|PMI|Estadístico|2020|2021|2022|Max|Año|Coordenadas UTM|Col9|
|---|---|---|---|---|---|---|---|---|
|**PMI**|**Estadístico**|**2020**|**2021**|**2022**|**Max**|**Año**|**Datum WGS 84 Huso 18**|**Datum WGS 84 Huso 18**|
|**PMI**|**Estadístico**|**2020**|**2021**|**2022**|**Max**|**Año**|**Este (m)**|**Norte (m)**|
|**PMI**|Concentración 24h de SO2, P99 (μg/m3)|2|2|1|2|2021|702.686,41|5.871.322,12|
|**PMI**|Concentración 1h de SO2, P98,5 (μg/m3)|3|4|3|4|2021|702.686,41|5.871.322,12|
|**PMI**|Promedio Anual SO2 (μg/m3)|0|0|0|0|2021|702.686,41|5.871.322,12|
|**PMI**|Concentración 24h SO2, P99,7 (μg/m3)|2|3|2|3|2021|702.686,41|5.871.322,12|
|**PMI**|Concentración 1h SO2, P99,73 (μg/m3)|6|7|6|7|2021|702.686,41|5.871.322,12|
|**PMI**|Concentración 1h NO2, P99 (μg/m3)|46|47|49|49|2022|702.904,58|5.870.494,68|
|**PMI**|Concentración NO2 (μg/m3)|3|3|3|3|2020|702.904,58|5.870.494,68|
|**PMI**|Concentración 1h CO, P99 (mg/m3)|0|0|0|0|2020|703.884,71|5.869.470,07|
|**PMI**|Concentración 8h móvil CO, P99 (mg/m3)|0|0|0|0|2020|702.904,58|5.870.494,68|
|**PMI**|Concentración 24h TRS (μg/m3)|0|0|0|0|2020|702.686,41|5.871.322,12|
|**PMI**|Concentración 1h TRS (μg/m3)|0|0|0|0|2021|702.519|5.871.048|
|Escenario 3|Promedio anual MP10 (μg/m3)|71|70|71|71|2022|702.904,49|5.870.494,79|
|Escenario 3|Percentil 98 concentración 24 horas MP10 (μg/m3)|302|338|311|338|2021|702.904,49|5.870.494,79|
|Escenario 3|Promedio anual MP2,5 (μg/m3)|8|8|8|8|2020|702.904,49|5.870.494,79|
|Escenario 3|Percentil 98 concentración 24 horas MP2,5 (μg/m3)|31|35|32|35|2021|702.904,49|5.870.494,79|
|Escenario 3|Promedio anual tasa de deposición MPS (mg/m2/d)|5713|5682|5759|5759|2022|702.904,49|5.870.494,79|
|Escenario 3|Concentración 24h de SO2, P99 (μg/m3)|0|0|0|0|2021|702.904,49|5.870.494,79|
|Escenario 3|Concentración 1h de SO2, P98,5 (μg/m3)|0|0|0|0|2020|702.904,49|5.870.494,79|
|Escenario 3|Promedio Anual SO2 (μg/m3)|0|0|0|0|2021|702.904,49|5.870.494,79|
|Escenario 3|Concentración 24h SO2, P99,7 (μg/m3)|0|0|0|0|2021|702.904,49|5.870.494,79|
|Escenario 3|Concentración 1h SO2, P99,73 (μg/m3)|1|1|1|1|2021|702.904,49|5.870.494,79|
|Escenario 3|Concentración 1h NO2, P99 (μg/m3)|193|197|190|197|2021|702.904,49|5.870.494,79|
|Escenario 3|Concentración NO2 (μg/m3)|11|10|9|11|2020|702.904,49|5.870.494,79|
|Escenario 3|Concentración 1h CO, P99 (mg/m3)|0|0|0|0|2021|702.904,49|5.870.494,79|
|Escenario 3|Concentración 8h móvil CO, P99 (mg/m3)|0|0|0|0|2020|702.904,49|5.870.494,79|

183

##### - 9.7. APENDICE 7 Isolineas de concentración

Las isolineas de concentración y tasa de deposición que se presentan en este apéndice

corresponden a las determinadas tomando en consideración como criterio de

determinación de la magnitud de la isolinea, los puntos de máximo impacto (PMI) de cada

año modelado para cada estadístico.

El análisis del cumplimiento de normativa por parte de los PMIs localizados fuera del

perímetro de la planta se presentó en la sección Concentración total estimada - Escenario1 y la sección y, Concentración total estimada Escenario 2, por lo que se estima que el

proyecto y sus diferentes etapas no generan un impacto significativo en la calidad del aire

de la zona o la salud de la población, presentándose las isolineas de concentración y de tasa

de deposición con un enfoque informativo.

##### - 9.7.1. Isolineas de concentración Escenario 1 9.7.1.1. Material particulado respirable (MP 10 )

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 102. Isolíneas Promedio anual de la concentración de MP** **10** **- Escenario 1.**

184

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 103. Isolíneas del percentil 98 de la concentración de 24 horas de MP** **10** **-** **Escenario 1.**

##### 9.7.1.2. Material particulado respirable fino (MP 2.5 )

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 104. Isolíneas Promedio anual de la concentración de MP** **2.5** **- Escenario 1.**

185

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 105. Isolíneas del percentil 98 de la concentración de 24 horas de MP** **2.5** **-** **Escenario 1.**

##### 9.7.1.3. Material particulado sedimentable (MPS)

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 106. Isolíneas de la tasa de deposición promedio anual de MPS** **-** **Escenario 1.**

186

##### 9.7.1.4. Dióxido de nitrógeno (NO 2 )

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 107. Isolíneas del promedio anual de la concentración de NO** **2** **-** **Escenario 1.**

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 108. Isolíneas del percentil 99 de la concentración horaria de NO** **2** **-** **Escenario 1.**

187

##### 9.7.1.5. Dióxido de azufre (SO 2 )

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 109. Isolíneas del promedio anual de la concentración de SO** **2** **-** **Escenario 1.**

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 110. Isolíneas del percentil 99 de la concentración diaria de SO** **2** **-** **Escenario 1.**

188

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 111. Isolíneas del percentil 98,5 de la concentración horaria de SO** **2** **-** **Escenario 1.**

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 112. Isolíneas del percentil 99,7 de la concentración diaria de SO** **2** **-** **Escenario 1.**

189

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 113. Isolíneas del percentil 99,73 de la concentración horaria de SO** **2** **-** **Escenario 1.**

##### 9.7.1.6. Monóxido de carbono (CO)

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 114. Isolíneas del percentil 99 de la concentración horaria de CO** **-** **Escenario 1.**

190

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 115. Isolíneas del percentil 99 de la concentración 8 horas de CO** **-** **Escenario 1.**

##### 9.7.1.7. Azufre total reducido (TRS)

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 116. Isolíneas de la concentración diaria de TRS** **-** **Escenario 1.**

191

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 117. Isolíneas de la concentración horaria de TRS** **-** **Escenario 1.**

##### - 9.7.2. Isolineas de concentración Escenario 2 9.7.2.1. Material particulado respirable (MP 10 )

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 118. Isolíneas Promedio anual de la concentración de MP** **10** **- Escenario 2.**

192

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 119. Isolíneas del percentil 98 de la concentración de 24 horas de MP** **10** **-** **Escenario 2.**

##### 9.7.2.2. Material particulado respirable fino (MP 2.5 )

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 120. Isolíneas Promedio anual de la concentración de MP** **2.5** **- Escenario 2.**

193

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 121. Isolíneas del percentil 98 de la concentración de 24 horas de MP** **2.5** **-** **Escenario 2.**

##### 9.7.2.3. Material particulado sedimentable (MPS)

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 122. Isolíneas de la tasa de deposición promedio anual de MPS** **-** **Escenario 2.**

194

##### 9.7.2.4. Dióxido de nitrógeno (NO 2 )

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 123. Isolíneas del promedio anual de la concentración de NO** **2** **-** **Escenario 2.**

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 124. Isolíneas del percentil 99 de la concentración horaria de NO** **2** **-** **Escenario 2.**

195

##### 9.7.2.5. Dióxido de azufre (SO 2 )

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 125. Isolíneas del promedio anual de la concentración de SO** **2** **-** **Escenario 2.**

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 126. Isolíneas del percentil 99 de la concentración diaria de SO** **2** **-** **Escenario 2.**

196

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 127. Isolíneas del percentil 98,5 de la concentración horaria de SO** **2** **-** **Escenario 2.**

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 128. Isolíneas del percentil 99,7 de la concentración diaria de SO** **2** **-** **Escenario 2.**

197

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 129. Isolíneas del percentil 99,73 de la concentración horaria de SO** **2** **-** **Escenario 2.**

##### 9.7.2.6. Monóxido de carbono (CO)

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 130. Isolíneas del percentil 99 de la concentración horaria de CO** **-** **Escenario 2.**

198

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 131. Isolíneas del percentil 99 de la concentración 8 horas de CO** **-** **Escenario 2.**

##### 9.7.2.7. Azufre total reducido (TRS)

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 132. Isolíneas de la concentración diaria de TRS** **-** **Escenario 2.**

199

**Nota:** En el Anexo 2 - Archivos de geolocalización se encuentran los archivos kml y en el Anexo 5 - Cartografía se

entrega la cartografía en alta calidad.
**Figura 133. Isolíneas de la concentración horaria de TRS** **-** **escenario 2.**

200

#### 10. Bibliografía

-
CMPC. 2003. DIA: Proyecto Optimización Planta Laja PROFAL IV. Aprobado.

CMPC. 2009. EIA. Modernización de Planta Laja. Aprobado.

CMPC. 2021. DIA. Nueva Conexión y Ampliación S/E Celulosa Laja. Aprobado.

DICTUC. 2022. EVALUACIÓN SIGNIFICANCIA DEL IMPACTO DE LAS EMISIONES DE UN

PROYECTO O ACTIVIDAD EN ZONAS SATURADAS EN EL MARCO DEL SEIA”

desarrollado por el DICTUC para él SEA. Estudio realizado para el Servicio de

Evaluación Ambiental.

DS N12. 2022. Establece norma primaria de calidad ambiental para material particulado

respirable MP10. Ministerio Secretaría General de la Presidencia.

DS N°12. 2011. Establece norma primaria de calidad ambiental para material particulado

fino respirable MP 2,5. Ministerio del Medio Ambiente.

DS N°104. 2019. Establece norma primaria de calidad de aire para dióxido de azufre (SO2).

Ministerio del Medio Ambiente.

DS N°114. 2003. Establece norma primaria de calidad de aire para dióxido de nitrógeno

(NO2). Ministerio Secretaría General de la Presidencia.

DS N° 115. 2002. Establece norma primaria de calidad de aire para monóxido de carbono

(CO). Ministerio Secretaría General de la Presidencia.

Infraestructura de datos geoespaciales. Zonificación Planes Reguladores Comunales Región

del Biobío. Visitado el 14-12-2022. Disponible en:
http://www.geoportal.cl/geoportal/catalog/search/resource/resumen.page?uuid=

%7B5108A7C2-54C9-408B-A300-593CB6126334%7D

Ministerio del Medio Ambiente. 2012. Decreto 40: Aprueba reglamento del sistema de

evaluación de impacto Ambiental.

Swiss Federal Council. 1985 (Actualización 01-01-2022). Ordinance on Air Pollution Control.

Disponible en: https://www.fedlex.admin.ch/eli/cc/1986/208_208_208/en

Resolución 1541. 2013. Ministerio de Ambiente y Desarrollo Sostenible. Norma de

Colombia.

Servicio de evaluación ambiental. Sección Búsqueda y revisión de proyectos. Visitado el: 21
04-2023. Disponible en: https://www.sea.gob.cl/

Servicio de Evaluación de Impacto Ambiental. 2023. Guía para el uso de modelos de calidad

del aire en el SEIA.

201

Sistema de información de fiscalización ambiental. Seguimiento ambiental de proyectos.

Visitado el 21-04-2023. Disponible en:
https://snifa.sma.gob.cl/SeguimientoAmbiental/RCA

Sistema de Información Nacional de Calidad del Aire. Visitado el 14-12-2022. Disponible en:

https://sinca.mma.gob.cl/index.php/

Swiss Federal Council. 1985 (Actualización 01-01-2022). Ordinance on Air Pollution Control.

Disponible en: https://www.fedlex.admin.ch/eli/cc/1986/208_208_208/en

United States Global Characterization. Global Land Cover Characterization (GLCC): South

America. Visitado el 13-04-2023. Disponible en: https://www.usgs.gov/

Yáñez-Morroni, G., Gironás, J., Caneo, M., Delgado, R., & Garreaud, R. (2018). Using the

Weather Research and Forecasting (WRF) model for precipitation forecasting in an
Andean region with complex topography. Atmosphere, 9(8).

202

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Estadísticos con saturación de la línea base.****

| Estación | Estadístico | Línea base en<br>estación | Límite<br>normativo | % normativa |
| --- | --- | --- | --- | --- |
| Laja | Promedio anual MP2,5 (μg/m3) | 22 | 20 | 110% |
| Laja | Percentil 98 concentración 24 horas MP2,5 (μg/m3) | 89 | 50 | 178% |
| San<br>Rosendo | Promedio anual MP2,5 (μg/m3) | 26 | 20 | 130% |
| San<br>Rosendo | Percentil 98 concentración 24 horas MP2,5 (μg/m3) | 101 | 50 | 202% |
| San<br>Rosendo | Concentraciones 1h TRS (μg/m3) | 61 | 40 | 153% |

**Tabla 2.: Tabla resumen estadísticos** **-** **Escenario 1 parte 1.****

| Ítem | MP *<br>10 | Col3 | MP **<br>2.5 | Col5 | MPS* | NO *<br>2 | Col8 | SO *<br>2 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ítem** | **Promedio**<br>**anual**<br>**(μg/m3N)** | **Percentil**<br>**98 diario**<br>**(μg/m3N)** | **Promedio**<br>**anual**<br>**(μg/m3N)** | **Percentil**<br>**98 diario**<br>**(μg/m3N)** | **Tasa de**<br>**deposición**<br>**promedio**<br>**anual**<br>**(mg/m2N/d)** | **Promedio**<br>**anual**<br>**(μg/m3N)** | **Percentil**<br>**99**<br>**horario**<br>**(μg/m3N)** | **Promedio**<br>**anual**<br>**(μg/m3N)** | **Percentil 99**<br>**diario(μg/m3N)** | **Percentil 98,5**<br>**horario(μg/m3N)** | **Percentil**<br>**99,7**<br>**diario**<br>**(μg/m3N)** | **Percentil**<br>**99,73**<br>**horario**<br>**(μg/m3N)** |
| **Límite**<br>**normativo** | **50** | **130** | **--** | **--** | **200** | **100** | **400** | **60** | **150** | **350** | **260** | **700** |
| **SIL** | **--** | **--** | **0,33** | **1,71** | **--** | **--** | **--** | **--** | **--** | **--** | **--** | **--** |
| Receptor 1 | **30** | **71** | **0,08** | **0,45** | **0 ** | **9 ** | **58** | **1 ** | **5 ** | **7 ** | **8 ** | **18** |
| Receptor 2 | **30** | **71** | **0,19** | **0,72** | **0 ** | **9 ** | **55** | **1 ** | **6 ** | **8 ** | **9 ** | **18** |
| Receptor 3 | **30** | **70** | **0,04** | **0,28** | **0 ** | **9 ** | **57** | **1 ** | **5 ** | **6 ** | **8 ** | **15** |
| Receptor 4 | **30** | **71** | **0,10** | **0,55** | **0 ** | **9 ** | **54** | **1 ** | **5 ** | **7 ** | **8 ** | **17** |
| Receptor 5 | **30** | **71** | **0,25** | **1,10** | **0 ** | **9 ** | **58** | **1 ** | **6 ** | **9 ** | **9 ** | **20** |
| Receptor 6 | **30** | **71** | **0,19** | **0,76** | **0 ** | **9 ** | **62** | **1 ** | **6 ** | **8 ** | **9 ** | **19** |
| Estación<br>Laja | **30** | **71** | **0,06** | **0,42** | **0 ** | **9 ** | **53** | **1 ** | **5 ** | **7 ** | **7 ** | **16** |
| Estación<br>San<br>Rosendo | **37** | **103** | **0,16** | **0,55** | **0 ** | **11** | **50** | **3 ** | **8 ** | **10** | **11** | **19** |

**Tabla 3.: Tabla resumen estadísticos** **-** **Escenario 1 parte 2.****

| Ítem | CO* | Col3 | TRS* | Col5 |
| --- | --- | --- | --- | --- |
| **Ítem** | **Percentil 99 horario (mg/m3N)** | **Percentil 99 8 horas (mg/m3N)** | **Concentración diaria (μg/m3N)** | **Concentración horaria (μg/m3N)** |
| **Límite normativo** | **30** | **10** | **7 ** | **40** |
| **SIL** | **--** | **--** | **--** | **0,4** |
| Receptor 1 | **5 ** | **3 ** | **4 ** | **20** |
| Receptor 2 | **5 ** | **3 ** | **4 ** | **20** |
| Receptor 3 | **5 ** | **3 ** | **4 ** | **20** |
| Receptor 4 | **5 ** | **3 ** | **4 ** | **20** |
| Receptor 5 | **5 ** | **3 ** | **4 ** | **20** |
| Receptor 6 | **5 ** | **3 ** | **4 ** | **20** |

**Tabla 4.: Tabla resumen estadísticos** **-** **Escenario 2 parte 1.****

| Ítem | MP *<br>10 | Col3 | MP **<br>2.5 | Col5 | MPS* | NO *<br>2 | Col8 | SO *<br>2 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ítem** | **Promedio**<br>**anual**<br>**(μg/m3N)** | **Percentil**<br>**98 diario**<br>**(μg/m3N)** | **Promedio**<br>**anual**<br>**(μg/m3N)** | **Percentil**<br>**98 diario**<br>**(μg/m3N)** | **Tasa de**<br>**deposición**<br>**promedio**<br>**anual**<br>**(mg/m2N/d)** | **Promedio**<br>**anual**<br>**(μg/m3N)** | **Percentil**<br>**99**<br>**horario**<br>**(μg/m3N)** | **Promedio**<br>**anual**<br>**(μg/m3N)** | **Percentil 99**<br>**diario(μg/m3N)** | **Percentil 98,5**<br>**horario(μg/m3N)** | **Percentil**<br>**99,7**<br>**diario**<br>**(μg/m3N)** | **Percentil**<br>**99,73**<br>**horario**<br>**(μg/m3N)** |
| **Límite**<br>**normativo** | **50** | **130** | **20** | **50** | **200** | **100** | **400** | **60** | **150** | **350** | **260** | **700** |
| **SIL** | **--** | **--** | **0,33** | **1,71** | **--** | **--** | **--** | **--** | **--** | **--** | **--** | **--** |
| Receptor 1 | **30** | **71** | **0,10** | **0,45** | **0 ** | **9 ** | **57** | **1 ** | **5 ** | **7 ** | **8 ** | **18** |
| Receptor 2 | **30** | **71** | **0,25** | **0,78** | **0 ** | **9 ** | **55** | **1 ** | **6 ** | **8 ** | **9 ** | **18** |
| Receptor 3 | **30** | **70** | **0,05** | **0,28** | **0 ** | **9 ** | **57** | **1 ** | **5 ** | **6 ** | **8 ** | **16** |
| Receptor 4 | **30** | **71** | **0,12** | **0,57** | **0 ** | **9 ** | **54** | **1 ** | **5 ** | **8 ** | **8 ** | **17** |
| Receptor 5 | **30** | **71** | **0,32** | **1,09** | **0 ** | **10** | **58** | **1 ** | **6 ** | **9 ** | **9 ** | **20** |
| Receptor 6 | **30** | **71** | **0,24** | **0,70** | **0 ** | **9 ** | **60** | **1 ** | **6 ** | **8 ** | **9 ** | **19** |

**Tabla 5.: Tabla resumen estadísticos** **-** **Escenario 2 parte 2.****

| Ítem | CO* | Col3 | TRS* | Col5 |
| --- | --- | --- | --- | --- |
| **Ítem** | **Percentil 99 horario (mg/m3N)** | **Percentil 99 8 horas (mg/m3N)** | **Concentración diaria (μg/m3N)** | **Concentración horaria (μg/m3N)** |
| **Límite normativo** | **30** | **10** | **7 ** | **40** |
| **SIL** | **--** | **--** | **--** | **0,4** |
| Receptor 1* | **5 ** | **3 ** | **4 ** | **20** |
| Receptor 2* | **5 ** | **3 ** | **4 ** | **20** |
| Receptor 3* | **5 ** | **3 ** | **4 ** | **20** |
| Receptor 4* | **5 ** | **3 ** | **4 ** | **20** |
| Receptor 5* | **5 ** | **3 ** | **4 ** | **20** |
| Receptor 6* | **5 ** | **3 ** | **4 ** | **20** |
| Estación Laja* | **5 ** | **3 ** | **4 ** | **20** |
| Estación San Rosendo* | **6 ** | **4 ** | **4 ** | **0,11**** |

**Tabla 6.: Tabla resumen estadísticos** **-** **Escenario 3 parte 1.****

| Ítem | MP *<br>10 | Col3 | MP **<br>2.5 | Col5 | MPS* | NO *<br>2 | Col8 | SO *<br>2 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ítem** | **Promedio**<br>**anual**<br>**(μg/m3N)** | **Percentil**<br>**98 diario**<br>**(μg/m3N)** | **Promedio**<br>**anual**<br>**(μg/m3N)** | **Percentil**<br>**98 diario**<br>**(μg/m3N)** | **Tasa de**<br>**deposición**<br>**promedio**<br>**anual**<br>**(mg/m2N/d)** | **Promedio**<br>**anual**<br>**(μg/m3N)** | **Percentil**<br>**99**<br>**horario**<br>**(μg/m3N)** | **Promedio**<br>**anual**<br>**(μg/m3N)** | **Percentil 99**<br>**diario(μg/m3N)** | **Percentil 98,5**<br>**horario(μg/m3N)** | **Percentil**<br>**99,7**<br>**diario**<br>**(μg/m3N)** | **Percentil**<br>**99,73**<br>**horario**<br>**(μg/m3N)** |
| **Límite**<br>**normativo** | **50** | **130** | **20** | **50** | **200** | **100** | **400** | **60** | **150** | **350** | **260** | **700** |
| **SIL** | **--** | **--** | **0,33** | **1,71** | **--** | **--** | **--** | **--** | **--** | **--** | **--** | **--** |
| Receptor 1 | **30** | **77** | **0,09** | **0,86** | **0 ** | **9 ** | **61** | **1 ** | **4 ** | **5 ** | **6 ** | **13** |
| Receptor 2 | **30** | **71** | **0,04** | **0,20** | **0 ** | **9 ** | **54** | **1 ** | **4 ** | **5 ** | **6 ** | **13** |
| Receptor 3 | **30** | **72** | **0,03** | **0,30** | **0 ** | **9 ** | **57** | **1 ** | **4 ** | **5 ** | **6 ** | **13** |
| Receptor 4 | **30** | **71** | **0,02** | **0,09** | **0 ** | **9 ** | **52** | **1 ** | **4 ** | **5 ** | **6 ** | **13** |
| Receptor 5 | **31** | **78** | **0,15** | **1,00** | **0 ** | **9 ** | **59** | **1 ** | **4 ** | **5 ** | **6 ** | **13** |
| Receptor 6 | **31** | **84** | **0,14** | **1,49** | **0 ** | **9 ** | **63** | **1 ** | **4 ** | **5 ** | **6 ** | **13** |
| Estación<br>Laja | **30** | **70** | **0,01** | **0,03** | **0 ** | **9 ** | **51** | **1 ** | **4 ** | **5 ** | **6 ** | **13** |
| Estación<br>San<br>Rosendo | **37** | **102** | **0,00** | **0,02** | **0 ** | **11** | **48** | **3 ** | **7 ** | **8 ** | **9 ** | **17** |

**Tabla 7.: Tabla resumen estadísticos** **-** **Escenario 3 parte 2.****

| Ítem | CO* | Col3 |
| --- | --- | --- |
| **Ítem** | **Percentil 99 horario (mg/m3N)** | **Percentil 99 8 horas (mg/m3N)** |
| **Límite normativo** | **30** | **10** |
| **SIL** | **--** | **--** |
| Receptor 1* | **5 ** | **3 ** |
| Receptor 2* | **5 ** | **3 ** |
| Receptor 3* | **5 ** | **3 ** |
| Receptor 4* | **5 ** | **3 ** |
| Receptor 5* | **5 ** | **3 ** |

**Tabla 8.: Características del dominio de simulación.****

| Descripción | Detalle |
| --- | --- |
| Periodo de simulación | 2020 al 20221 |
| Resolución | 1 x 1 km |
| Extensión | 75 x 75 km |

**Tabla 9.: Antecedentes de la proyección del dominio de simulación - Proyección LCC.****

| Variable | Detalle |
| --- | --- |
| RLat0 | 37,263S |
| RLon0 | 72,711W |
| XLat1 | 33,402S |
| XLat2 | 41,178S |

**Tabla 10.: Cronograma del proyecto** **-** **Fase de construcción.****

| ÁREA | ACTIVIDADES | AÑO | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 | Col26 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ÁREA** | **ACTIVIDADES** | **2024** | **2024** | **2024** | **2024** | **2024** | **2024** | **2024** | **2024** | **2024** | **2024** | **2024** | **2024** | **2025** | **2025** | **2025** | **2025** | **2025** | **2025** | **2025** | **2025** | **2025** | **2025** | **2025** | **2025** |
| **ÁREA** | **ACTIVIDADES** | **ENE** | **FEB** | **MAR** | **ABR** | **MAY** | **JUN** | **JUL** | **AGO** | **SEPT** | **OCT** | **NOV** | **DIC** | **ENE** | **FEB** | **MAR** | **ABR** | **MAY** | **JUN** | **JUL** | **AGO** | **SEPT** | **OCT** | **NOV** | **DIC** |
| Área<br>Preparación<br>Maderas | Obras civiles |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Área<br>Preparación<br>Maderas | Fundaciones |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Área<br>Preparación<br>Maderas | Montajes<br>electromecánicos |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Área<br>Preparación<br>Maderas | Puesta en<br>marcha |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Área fibra y<br>digestor | Obras civiles |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Área fibra y<br>digestor | Fundaciones |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Área fibra y<br>digestor | Montajes<br>electromecánicos |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Área fibra y<br>digestor | Puesta en<br>marcha |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Máquina<br>secadora N°2 | Montajes<br>electromecánicos<br>- 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Máquina<br>secadora N°2 | Montajes<br>electromecánicos<br>- 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Máquina<br>secadora N°2 | Puesta en<br>marcha |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Planta Tall Oil | Obras civiles |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Planta Tall Oil | Fundaciones |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Planta Tall Oil | Montajes<br>electromecánicos |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Planta Tall Oil | Puesta en<br>marcha |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

**Tabla 11.: Cronograma del proyecto - fase de cierre.****

| ACTIVIDADES | Año | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ACTIVIDADES** | **Meses** | **Meses** | **Meses** | **Meses** | **Meses** | **Meses** | **Meses** | **Meses** | **Meses** | **Meses** | **Meses** | **Meses** |
| **ACTIVIDADES** | **ENE** | **FEB** | **MAR** | **ABR** | **MAY** | **JUN** | **JUL** | **AGO** | **SEPT** | **OCT** | **NOV** | **DIC** |
| Habilitación de instalación de faenas |  |  |  |  |  |  |  |  |  |  |  |  |
| Desmantelamiento de estructuras, desarme de fundaciones y desconexiones de equipos |  |  |  |  |  |  |  |  |  |  |  |  |
| Desarme de instalación de faenas |  |  |  |  |  |  |  |  |  |  |  |  |
| Limpieza final |  |  |  |  |  |  |  |  |  |  |  |  |

**Tabla 12.: Fuentes de emisión durante la fase de construcción del proyecto.****

| Actividad | Fuente | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MP10** | **MP2,5** | **MPS** | **NO2** | **SO2** | **CO** | **TRS** |
| Demolición | X | X | X | -- | -- | -- | -- |
| Escarpe | X | X | X | -- | -- | -- | -- |
| Excavaciones | X | X | X | -- | -- | -- | -- |
| Nivelación | X | X | X | -- | -- | -- | -- |
| Compactación | X | X | X | -- | -- | -- | -- |
| Transferencia de material | X | X | X | -- | -- | -- | -- |
| Transito caminos pavimentados | X | X | X | -- | -- | -- | -- |
| Transito caminos no pavimentados | X | X | X | -- | -- | -- | -- |
| Combustión vehicular por caminos pavimentados | X | X | X | X | X | X | -- |
| Combustión vehicular por caminos no pavimentados | X | X | X | X | X | X | -- |
| Combustión de maquinarias | X | X | X | X | X | X | -- |
| Combustión grupos electrógenos | X | X | X | X | X | X | -- |

**Tabla 13.: Fuentes de emisión durante la fase de operación del proyecto.****

| Actividad | Fuente | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MP10** | **MP2,5** | **MPS** | **NO2** | **SO2** | **CO** | **TRS** |
| Transferencia de material | X | X | X | -- | -- | -- | -- |
| Erosión eólica | X | X | X | -- | -- | -- | -- |
| Molienda de biomasa | X | X | X | -- | -- | -- | -- |
| Transito caminos pavimentados | X | X | X | -- | -- | -- | -- |
| Transito caminos no pavimentados | X | X | X | -- | -- | -- | -- |
| Combustión vehicular por caminos pavimentados | X | X | X | X | X | X | -- |
| Combustión vehicular por caminos no pavimentados | X | X | X | X | X | X | -- |
| Combustión de maquinarias | X | X | X | X | X | X | -- |
| Combustión grupos electrógenos | X | X | X | X | X | X | -- |
| Transporte en ferrocarril | X | X | X | X | X | X | -- |
| Caldera biomasa N°3 | X | X | X | X | X | X | X |
| Caldera recuperadora N°6 | X | X | X | X | X | X | X |
| Horno de cal N°3 | X | X | X | X | X | X | X |
| Incinerador 1 | X | X | X | X | X | X | -- |
| Incinerador 2 | X | X | X | X | X | X | -- |

**Tabla 14.: Fuentes de emisión durante la fase de cierre del proyecto.****

| Actividad | Fuente | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MP10** | **MP2,5** | **MPS** | **NO2** | **SO2** | **CO** | **TRS** |
| Demolición | X | X | X | -- | -- | -- | -- |
| Escarpe | X | X | X | -- | -- | -- | -- |
| Excavaciones | X | X | X | -- | -- | -- | -- |
| Nivelación | X | X | X | -- | -- | -- | -- |
| Compactación | X | X | X | -- | -- | -- | -- |
| Transferencia de material | X | X | X | -- | -- | -- | -- |
| Transito caminos pavimentados | X | X | X | -- | -- | -- | -- |
| Transito caminos no pavimentados | X | X | X | -- | -- | -- | -- |
| Combustión vehicular por caminos pavimentados | X | X | X | X | X | X | -- |
| Combustión vehicular por caminos no pavimentados | X | X | X | X | X | X | -- |
| Combustión de maquinarias | X | X | X | X | X | X | -- |
| Combustión grupos electrógenos | X | X | X | X | X | X | -- |

**Tabla 15.: Inventario de emisiones de la fase de construcción** **-** **Mes 4 al mes 12 (año 2024).****

| Actividad | SO<br>2 | NO<br>x | CO | MP<br>2,5 | MP<br>10 | PTS | TRS | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Demoliciones | 0 | 0 | 0 | 0,065 | 0,652 | 2,153 | 0 | t/año |
| Escarpe | 0 | 0 | 0 | 0,004 | 0,026 | 0,026 | 0 | t/año |
| Excavación | 0 | 0 | 0 | 0,036 | 0,066 | 0,338 | 0 | t/año |
| Nivelación | 0 | 0 | 0 | 0,002 | 0,019 | 0,064 | 0 | t/año |
| Compactación | 0 | 0 | 0 | 0,001 | 0,002 | 0,010 | 0 | t/año |
| Transferencia de Material | 0 | 0 | 0 | 0 | 0,001 | 0,003 | 0 | t/año |
| Maquinaria Fuera de Ruta | 0,002 | 1,252 | 1,015 | 0,115 | 0,115 | 0,115 | 0 | t/año |
| Grupos Electrógenos | 0,002 | 0,034 | 0,007 | 0,002 | 0,002 | 0,002 | 0 | t/año |
| Transito Camino Pavimentado | 0 | 0 | 0 | 0,283 | 1,168 | 6,084 | 0 | t/año |
| Combustión Vehicular Camino Pavimentado | 0,006 | 3,364 | 0,102 | 0,021 | 0,021 | 0,021 | 0 | t/año |
| Transito Camino No Pavimentado | 0 | 0 | 0 | 0,267 | 2,667 | 9,333 | 0 | t/año |
| Combustión Vehicular Camino No Pavimentado | 0 | 0,037 | 0,001 | 0 | 0 | 0 | 0 | t/año |
| **Total** | **0,010** | **4,687** | **1,126** | **0,796** | **4,740** | **18,150** | **0 ** | **t/año** |

**Tabla 16.: Inventario de emisiones de la fase de construcción** **-** **Mes 13 al mes 24 (año 2025)****

| Actividad | SO<br>2 | NO<br>x | CO | MP<br>2,5 | MP<br>10 | PTS | TRS | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Demoliciones | 0 | 0 | 0 | 0,078 | 0,784 | 2,587 | 0 | t/año |
| Escarpe | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Excavación | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Nivelación | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Compactación | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Transferencia de Material | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Maquinaria Fuera de Ruta | 0,007 | 4,856 | 3,668 | 0,391 | 0,391 | 0,391 | 0 | t/año |
| Grupos Electrógenos | 0,002 | 0,034 | 0,007 | 0,002 | 0,002 | 0,002 | 0 | t/año |
| Transito Camino Pavimentado | 0 | 0 | 0 | 0,227 | 0,937 | 4,880 | 0 | t/año |
| Combustión Vehicular Camino Pavimentado | 0,005 | 2,436 | 0,081 | 0,016 | 0,016 | 0,016 | 0 | t/año |
| Transito Camino No Pavimentado | 0,000 | 0,000 | 0,000 | 0,187 | 1,873 | 6,556 | 0 | t/año |
| Combustión Vehicular Camino No Pavimentado | 0,000 | 0,026 | 0,001 | 0 | 0 | 0 | 0 | t/año |
| **Total** | **0,014** | **7,352** | **3,757** | **0,902** | **4,003** | **14,432** | **0 ** | **t/año** |

**Tabla 17.: Inventario de emisiones de la fase de operación base** **-** **Emisiones de 1 año.****

| Actividad | SO<br>2 | NO<br>x | CO | MP<br>2,5 | MP<br>10 | PTS | TRS | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Transferencia de Material | 0 | 0 | 0 | 0,001 | 0,004 | 0,008 | 0 | t/año |
| Maquinaria Fuera de Ruta | 0,138 | 89,024 | 71,141 | 8,799 | 8,799 | 8,799 | 0 | t/año |
| Erosión Eólica | 0 | 0 | 0 | 0,009 | 0,057 | 0,113 | 0 | t/año |
| Molienda Biomasa | 0 | 0 | 0 | 0,360 | 0,360 | 3,600 | 0 | t/año |
| Transporte Ferrocarril | 0,479 | 6,903 | 1,027 | 0,257 | 0,257 | 0,257 | 0 | t/año |
| Grupos Electrógenos | 0,099 | 1,066 | 0,235 | 0,060 | 0,060 | 0,060 | 0 | t/año |
| Fuentes Fijas | 751,608 | 1.043,318 | 1.379,701 | 442,760 | 490,180 | 932,940 | 13,140 | t/año |
| Transito Camino Pavimentado | 0 | 0 | 0 | 0,321 | 1,327 | 6,915 | 0 | t/año |
| Combustión Vehicular Camino Pavimentado | 0,006 | 3,210 | 0,106 | 0,022 | 0,022 | 0,022 | 0 | t/año |
| Transito Camino No Pavimentado | 0 | 0 | 0 | 0,661 | 6,614 | 23,149 | 0 | t/año |
| Combustión Vehicular Camino No Pavimentado | 0 | 0,067 | 0,002 | 0 | 0 | 0 | 0 | t/año |
| **Total** | **752,330** | **1.143,589** | **1.452,212** | **453,250** | **507,680** | **975,863** | **13,140** | **t/año** |

**Tabla 18.: Inventario de emisiones de la fase de operación proyectada** **-** **Emisiones de 1 año.****

| Actividad | SO<br>2 | NO<br>x | CO | MP<br>2,5 | MP<br>10 | PTS | TRS | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Transferencia de Material | 0 | 0 | 0 | 0,001 | 0,004 | 0,009 | 0 | t/año |
| Maquinaria Fuera de Ruta | 0,149 | 95,576 | 75,903 | 9,458 | 9,458 | 9,458 | 0 | t/año |
| Erosión Eólica | 0 | 0 | 0 | 0,009 | 0,057 | 0,113 | 0 | t/año |
| Molienda Biomasa | 0 | 0 | 0 | 0,360 | 0,360 | 3,600 | 0 | t/año |
| Transporte Ferrocarril | 0,479 | 7,831 | 1,166 | 0,291 | 0,291 | 0,291 | 0 | t/año |
| Grupos Electrógenos | 0,099 | 1,066 | 0,235 | 0,060 | 0,060 | 0,060 | 0 | t/año |
| Fuentes Fijas | 835,120 | 1.159,242 | 1.533,001 | 491,955 | 544,645 | 1.036,600 | 14,600 | t/año |
| Transito Camino Pavimentado | 0 | 0 | 0 | 0,339 | 1,402 | 7,302 | 0 | t/año |
| Combustión Vehicular Camino Pavimentado | 0,006 | 3,387 | 0,112 | 0,023 | 0,023 | 0,023 | 0 | t/año |
| Transito Camino No Pavimentado | 0 | 0 | 0 | 0,661 | 6,614 | 23,149 | 0 | t/año |

**Tabla 19.: Inventario de emisiones** **-** **Incremento emisión de Fase de operación (1 año).****

| Actividad | SO2 | NOx | CO | MP2,5 | MP10 | PTS | TRS | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Transferencia de Material | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Maquinaria Fuera de Ruta | 0,010 | 6,552 | 4,762 | 0,659 | 0,659 | 0,659 | 0 | t/año |
| Erosión Eólica | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Molienda Biomasa | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Transporte Ferrocarril | 0 | 0,928 | 0,138 | 0,035 | 0,035 | 0,035 | 0 | t/año |
| Grupos Electrógenos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Fuentes Fijas | 83,512 | 115,924 | 153,300 | 49,196 | 54,464 | 103,660 | 1,460 | t/año |
| Transito Camino Pavimentado | 0 | 0 | 0 | 0,018 | 0,074 | 0,387 | 0 | t/año |
| Combustión Vehicular Camino Pavimentado | 0 | 0,177 | 0,006 | 0,001 | 0,001 | 0,001 | 0 | t/año |
| Transito Camino No Pavimentado | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Combustión Vehicular Camino No Pavimentado | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| **Total** | **83,523** | **123,581** | **158,206** | **49,908** | **55,233** | **104,741** | **1,460** | **t/año** |

**Tabla 20.: Inventario de emisiones de la fase de cierre** **-** **Emisiones de 1 año.****

| Actividad | SO2 | NOx | CO | MP2,5 | MP10 | PTS | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Demoliciones | 0 | 0 | 0 | 0,265 | 2,647 | 8,736 | t/año |
| Escarpe | 0 | 0 | 0 | 0,007 | 0,048 | 0,048 | t/año |
| Excavación | 0 | 0 | 0 | 0,066 | 0,122 | 0,623 | t/año |
| Nivelación | 0 | 0 | 0 | 0,004 | 0,034 | 0,118 | t/año |
| Compactación | 0 | 0 | 0 | 0,002 | 0,004 | 0,018 | t/año |
| Transferencia de Material | 0 | 0 | 0 | 0,000 | 0,002 | 0,005 | t/año |
| Maquinaria Fuera de Ruta | 0,017 | 11,258 | 8,631 | 0,933 | 0,933 | 0,933 | t/año |
| Grupos Electrógenos | 0,008 | 0,125 | 0,027 | 0,009 | 0,009 | 0,009 | t/año |
| Transito Camino Pavimentado | 0 | 0 | 0 | 0,895 | 3,701 | 19,280 | t/año |
| Combustión Vehicular Camino Pavimentado | 0,019 | 10,689 | 0,338 | 0,068 | 0,068 | 0,068 | t/año |
| Transito Camino No Pavimentado | 0 | 0 | 0 | 0,683 | 6,832 | 23,910 | t/año |
| Combustión Vehicular Camino No Pavimentado | 0,000 | 0,115 | 0,003 | 0,001 | 0,001 | 0,001 | t/año |
| **Total** | **0,044** | **22,187** | **9,000** | **2,933** | **14,400** | **53,748** | **t/año** |

**Tabla 21.: Cronograma de alternativas a evaluar para el escenario 1.****

| Fase | 2024 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | 2025 | Col15 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 | 2026 | Col27 | Col28 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **ENE** | **FEB** | **MAR** | **ABR** | **MAY** | **JUN** | **JUL** | **AGO** | **SEPT** | **OCT** | **NOV** | **DIC** | **ENE** | **FEB** | **MAR** | **ABR** | **MAY** | **JUN** | **JUL** | **AGO** | **SEPT** | **OCT** | **NOV** | **DIC** | **ENE** | **FEB** | **MAR** |
| Construcción |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Operación<br>proyectada |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** | **Alternativas de evaluación para análisis del escenario 1** |
| Alternativa 1 |  |  |  | Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024 | Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024 | Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024 | Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024 | Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024 | Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024 | Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024 | Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024 | Alternativa 1. Construcción desde abril 2024 hasta<br>diciembre 2024 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Alternativa 2 |  |  |  |  |  |  |  |  |  |  |  |  | Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025 | Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025 | Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025 | Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025 | Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025 | Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025 | Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025 | Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025 | Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025 | Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025 | Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025 | Alternativa 2. Construcción desde enero 2025 hasta diciembre 2025 y<br>Operación proyectada desde julio 2025 hasta diciembre 2025 |  |  |  |
| Alternativa 3 |  |  |  | Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12) | Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12) | Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12) | Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12) | Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12) | Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12) | Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12) | Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12) | Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12) | Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12) | Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12) | Alternativa 3. Construcción desde abril 2024 (mes 1) hasta marzo 2025 (mes<br>12) |  |  |  |  |  |  |  |  |  |  |  |  |
| Alternativa 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24) | Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24) | Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24) | Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24) | Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24) | Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24) | Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24) | Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24) | Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24) | Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24) | Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24) | Alternativa 4. Construcción desde abril 2025 (mes 13) hasta marzo 2026<br>(mes 24) y operación proyectada desde julio 2025 (mes 16) hasta marzo<br>2026 (mes 24) |

**Tabla 22.: Alternativas de análisis del escenario 1.****

| Alternativa | SO<br>2 | NO<br>x | CO | MP<br>2,5 | MP<br>10 | PTS | TRS | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **1 ** | **0,010** | **4,687** | **1,126** | **0,796** | **4,740** | **18,150** | **0,000** | **t/año** |
| **2 ** | **41,775** | **69,142** | **82,860** | **25,856** | **31,620** | **66,803** | **0,730** | **t/año** |
| **3 ** | **0,013** | **6,626** | **2,147** | **1,089** | **6,337** | **23,707** | **0,000** | **t/año** |
| **4 ** | **62,653** | **98,097** | **121,391** | **38,040** | **43,831** | **87,432** | **1,095** | **t/año** |

**Tabla 23.: Inventario de emisiones** **-** **Fase de construcción meses 13 al 21.****

| Actividad | SO<br>2 | NO<br>x | CO | MP<br>2,5 | MP<br>10 | PTS | TRS | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Demoliciones | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ton/año |
| Escarpe | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ton/año |
| Excavación | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ton/año |
| Nivelación | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ton/año |
| Compactación | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ton/año |
| Transferencia de Material | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ton/año |
| Maquinaria Fuera de Ruta | 0,005 | 3,532 | 2,668 | 0,284 | 0,284 | 0,284 | 0 | ton/año |
| Grupos Electrógenos | 0,002 | 0,034 | 0,007 | 0,002 | 0,002 | 0,002 | 0 | ton/año |
| Transito Camino Pavimentado | 0 | 0 | 0 | 0,170 | 0,702 | 3,660 | 0 | ton/año |
| Combustión Vehicular Camino Pavimentado | 0,003 | 1,827 | 0,061 | 0,012 | 0,012 | 0,012 | 0 | ton/año |
| Transito Camino No Pavimentado | 0 | 0 | 0 | 0,140 | 1,405 | 4,917 | 0 | ton/año |
| Combustión Vehicular Camino No Pavimentado | 0 | 0,019 | 0,001 | 0 | 0 | 0 | 0 | ton/año |
| **Total** | **0,011** | **5,412** | **2,736** | **0,609** | **2,406** | **8,876** | **0 ** | ton/año |

**Tabla 24.: Inventario de emisiones** **-** **Incremento de emisión de la fase de operación meses 16 al 24.****

| Actividad | SO2 | NOx | CO | MP2,5 | MP10 | PTS | TRS | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Transferencia de Material | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ton/año |
| Maquinaria Fuera de Ruta | 0,008 | 4,914 | 3,572 | 0,494 | 0,494 | 0,494 | 0 | ton/año |
| Erosión Eólica | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ton/año |
| Molienda Biomasa | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ton/año |
| Transporte Ferrocarril | 0 | 0,696 | 0,104 | 0,026 | 0,026 | 0,026 | 0 | ton/año |
| Grupos Electrógenos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ton/año |
| Fuentes Fijas | 62,634 | 86,943 | 114,975 | 36,897 | 40,848 | 77,745 | 1,095 | ton/año |
| Transito Camino Pavimentado | 0,000 | 0,000 | 0,000 | 0,013 | 0,056 | 0,290 | 0 | ton/año |
| Combustión Vehicular Camino Pavimentado | 0,000 | 0,133 | 0,004 | 0,001 | 0,001 | 0,001 | 0 | ton/año |
| Transito Camino No Pavimentado | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ton/año |
| Combustión Vehicular Camino No Pavimentado | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ton/año |

**Tabla 25.: Inventario de emisiones** **-** **Incremento de la emisión de la Fase de operación (1 año).****

| Actividad | SO2 | NOx | CO | MP2,5 | MP10 | PTS | TRS | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Transferencia de Material | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Maquinaria Fuera de Ruta | 0,010 | 6,552 | 4,762 | 0,659 | 0,659 | 0,659 | 0 | t/año |
| Erosión Eólica | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Molienda Biomasa | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Transporte Ferrocarril | 0 | 0,928 | 0,138 | 0,035 | 0,035 | 0,035 | 0 | t/año |
| Grupos Electrógenos | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Fuentes Fijas | 83,512 | 115,924 | 153,300 | 49,196 | 54,464 | 103,660 | 1,460 | t/año |
| Transito Camino Pavimentado | 0 | 0 | 0 | 0,018 | 0,074 | 0,387 | 0 | t/año |
| Combustión Vehicular Camino Pavimentado | 0 | 0,177 | 0,006 | 0,001 | 0,001 | 0,001 | 0 | t/año |
| Transito Camino No Pavimentado | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| Combustión Vehicular Camino No Pavimentado | 0 | 0 | 0 | 0 | 0 | 0 | 0 | t/año |
| **Total** | **83,523** | **123,581** | **158,206** | **49,908** | **55,233** | **104,741** | **1,460** | **t/año** |

**Tabla 26.: Inventario de emisiones** **-** **Fase de cierre (1 año).****

| Actividad | SO2 | NOx | CO | MP2,5 | MP10 | PTS | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Demoliciones | 0 | 0 | 0 | 0,265 | 2,647 | 8,736 | t/año |
| Escarpe | 0 | 0 | 0 | 0,007 | 0,048 | 0,048 | t/año |
| Excavación | 0 | 0 | 0 | 0,066 | 0,122 | 0,623 | t/año |

**Tabla 27.: Nivel de actividad para fuente difusa** **-** **Escenario 1 Fase de construcción.****

| ID | Localización | Fuente | Emisiones | Tipo de<br>fuente | N° equipos | Temperatura<br>(K) | Diámetro<br>(m) | Altura<br>de la<br>fuente<br>(m) | Velocidad<br>de<br>emisión<br>(m/s) | Meses<br>emite | Periodo emisión |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GE_11 | Grupos<br>electrógenos | Grupos<br>electrógenos | MP10, <br>MP2,5, <br>MPS,<br>NO2, SO2 y CO. | Puntual | 2 | 838,15 | 0,0635 | 1,9 | 77 | Mes 20 | Lunes a sábado de 11:00 a 19:00(UTC-4). |

**Tabla 29.: Nivel de actividad para fuentes de ruta** **-** **Escenario 1 Fase de construcción.****

| ID | Fuente | Emisiones | Tipo de<br>fuente | Distancia<br>total (km) | Altura de<br>la fuente<br>(m) | Meses<br>emite | Periodo emisión |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ID1 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 1 | MP10, MP2,5, MPS, NO2, SO2 y CO. | Ruta | 159.726 | 1 | Mes 13 al 21 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID2 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 2 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 149.917 | 1 | Mes 13 al 21 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID3 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 3 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 6.674 | 1 | Mes 13 al 21 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID4 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 4 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 45.169 | 1 | Mes 13 al 21 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID5 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 5 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 6.680 | 1 | Mes 13 al 21 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID6 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 6 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 116.422 | 1 | Mes 13 al 21 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID7 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 7 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 12.688 | 1 | Mes 13 al 21 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID8 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 8 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 19.135 | 1 | Mes 13 al 21 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID9 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 9 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 729 | 1 | Mes 13 al 21 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID10 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 10 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 504 | 1 | Mes 13 al 21 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID11 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 11 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 2.127 | 1 | Mes 13 al 21 | Lunes a sábado de 08:00 a 18:00(UTC-4). |

**Tabla 30.: Nivel de actividad para fuente difusa** **-** **Escenario 1 Incremento de la emisión de la Fase de operación.****

| ID | Fuente | Emisiones | Tipo de<br>fuente | N°<br>equipos | Temperatura<br>(K) | Diámetro<br>(m) | Altura de la<br>fuente (m) | Velocidad de<br>emisión (m/s) | Meses emite | Periodo<br>emisión |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CB3 | Caldera biomasa<br>N°3 | MP10, MP2,5, MPS, NO2, SO2, CO y TRS. | Puntual | 1 | 417,15 | 2,25 | 75,8 | 25,3 | Mes 16 al 24. | 24/7. |
| CR6 | Caldera<br>recuperadora<br>N°6 | MP10, MP2,5, MPS, NO2, SO2, CO y TRS. | MP10, MP2,5, MPS, NO2, SO2, CO y TRS. | 1 | 428,15 | 3,6 | 80 | 20,6 | Mes 16 al 24. | 24/7. |
| HC3 | Horno cal N°3 | MP10, MP2,5, MPS, NO2, SO2, CO y TRS. | MP10, MP2,5, MPS, NO2, SO2, CO y TRS. | 1 | 534,15 | 1,6 | 60 | 11 | Mes 16 al 24. | 24/7. |

**Tabla 32.: Nivel de actividad para fuentes de ruta** **-** **Escenario 1 Incremento de la emisión de la Fase de operación.****

| ID | Fuente | Emisiones | Tipo de<br>fuente | Distancia<br>total (km) | Altura de la<br>fuente (m) | Meses<br>emite | Periodo emisión |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ID4 | Tránsito<br>y <br>combustión<br>caminos<br>pavimentados<br>- <br>Ruta ID 4 | MP10, MP2,5, MPS, NO2, SO2 y CO. |  | 3.688 | 1 | Mes 16 al 24 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID9 | Tránsito<br>y <br>combustión<br>caminos<br>pavimentados<br>- <br>Ruta ID 9 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 47 | 1 | Mes 16 al 24 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID11 | Tránsito<br>y <br>combustión<br>caminos<br>pavimentados<br>- <br>Ruta ID 11 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 47 | 1 | Mes 16 al 24 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID12 | Tránsito<br>y <br>combustión<br>caminos<br>pavimentados<br>- <br>Ruta ID 12 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 248 | 1 | Mes 16 al 24 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| Ferr_11_par | Transporte en ferrocarril -<br>Laja a Lirquén | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 630 | 1 | Mes 16 al 24 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| Ferr_11_par | Transporte en ferrocarril -<br>Laja a Coronel | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 1.527 | 1 | Mes 16 al 24 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| Ferr_11_par | Transporte en ferrocarril -<br>Laja a San Vicente | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 261 | 1 | Mes 16 al 24 | Lunes a sábado de 08:00 a 18:00(UTC-4). |

**Tabla 33.: Nivel de actividad para fuente difusa** **-** **Escenario 2 Incremento de la emisión de la Fase de****

| ID | Localización | Fuente | Emisiones | Tipo de<br>fuente | Área<br>(m2) | Altura de<br>la fuente<br>(m) | Meses<br>emite | Periodo<br>emisión |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Prep_11 | Preparación<br>madera | Combustión<br>maquinaria<br>s | MP10, MP2,5, MPS, NO2, <br>SO2 y CO. | Difusa | 20.527 | 1 | Todo<br>el año | 24/7. |

**Tabla 34.: Nivel de actividad para fuentes puntuales** **-** **Escenario 2 Incremento de la emisión de la Fase de operación.****

| ID | Fuente | Emisiones | Tipo de<br>fuente | N° equipos | Temperatura<br>(K) | Diámetro<br>(m) | Altura de<br>la fuente<br>(m) | Velocidad<br>de emisión<br>(m/s) | Meses<br>emite | Periodo<br>emisión |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CB3 | Caldera<br>biomasa N°3 | MP10, MP2,5, MPS, NO2, SO2, CO y<br>TRS. | Puntual | 1 | 417,15 | 2,25 | 75,8 | 25,3 | Todo el año. | 24/7. |
| CR6 | Caldera<br>recuperadora<br>N°6 | MP10, MP2,5, MPS, NO2, SO2, CO y<br>TRS. | MP10, MP2,5, MPS, NO2, SO2, CO y<br>TRS. | 1 | 428,15 | 3,6 | 80 | 20,6 | Todo el año. | 24/7. |
| HC3 | Horno cal N°3 | MP10, MP2,5, MPS, NO2, SO2, CO y<br>TRS. | MP10, MP2,5, MPS, NO2, SO2, CO y<br>TRS. | 1 | 534,15 | 1,6 | 60 | 11 | Todo el año. | 24/7. |

**Tabla 35.: Nivel de actividad para fuentes de ruta - Escenario 2 Incremento de la emisión de la Fase de operación.****

| ID | Fuente | Emisiones | Tipo de<br>fuente | Distancia<br>total (km) | Altura de la<br>fuente (m) | Meses<br>emite | Periodo emisión |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ID1 | Tránsito y combustión caminos<br>pavimentados - Ruta ID 1 | MP10, MP2,5, MPS, NO2, SO2 y CO. | Ruta | 24.947 | 1 | Todo el año | Lunes a sábado de 08:00 a 18:00. |
| ID2 | Tránsito y combustión caminos<br>pavimentados - Ruta ID 2 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 24.452 | 1 | Todo el año | Lunes a sábado de 08:00 a 18:00. |
| ID4 | Tránsito y combustión caminos<br>pavimentados - Ruta ID 4 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 4.918 | 1 | Todo el año | Lunes a sábado de 08:00 a 18:00. |
| ID9 | Tránsito y combustión caminos<br>pavimentados - Ruta ID 9 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 62,5608 | 1 | Todo el año | Lunes a sábado de 08:00 a 18:00. |
| ID11 | Tránsito y combustión caminos<br>pavimentados - Ruta ID 11 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 62 | 1 | Todo el año | Lunes a sábado de 08:00 a 18:00. |
| ID12 | Tránsito y combustión caminos<br>pavimentados - Ruta ID 12 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 331 | 1 | Todo el año | Lunes a sábado de 08:00 a 18:00. |
| Ferr_11_par | Transporte en ferrocarril - Laja a<br>Lirquén | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 840 | 1 | Todo el año | Lunes a sábado de 08:00 a 18:00. |
| Ferr_11_par | Transporte en ferrocarril - Laja a<br>Coronel | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 2.036 | 1 | Todo el año | Lunes a sábado de 08:00 a 18:00. |
| Ferr_11_par | Transporte en ferrocarril - Laja a<br>San Vicente | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 347 | 1 | Todo el año | Lunes a sábado de 08:00 a 18:00. |

**Tabla 36.: Nivel de actividad para fuentes difusas** **-** **Escenario 3 Fase de cierre.****

| ID | Localización | Fuente | Emisiones | Tipo<br>de<br>fuente | Área<br>(m2) | Altura<br>de la<br>fuente<br>(m) | Meses emite | Periodo emisión |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Comb_maq | Superficie | Combustión<br>de<br>maquinarias<br>y <br>Transferencia de<br>material | MP10, MP2,5, MPS, NO2, SO2 y CO. | Difusa | 12659 | 1 | Mes 1 al 12 | Lunes a sábado de 08:00 a 16:00 (UTC-4). |
| Ev11 | Evaporador | Demolición | MP10, MP2,5, MPS. | MP10, MP2,5, MPS. | 390 | 1 | Mes 2 a 11 (excluido) | Lunes a sábado de 08:00 a 16:00 (UTC-4). |
| Ca11 | Caldera | Demolición | MP10, MP2,5, MPS. | MP10, MP2,5, MPS. | 488 | 1 | Mes 2 a 11 (excluido) | Lunes a sábado de 08:00 a 16:00 (UTC-4). |
| Ba11 | Batch | Demolición | MP10, MP2,5, MPS. | MP10, MP2,5, MPS. | 114 | 1 | Mes 2 a 11 (excluido) | Lunes a sábado de 08:00 a 16:00 (UTC-4). |
| Ho11 | Horno | Demolición | MP10, MP2,5, MPS. | MP10, MP2,5, MPS. | 155 | 1 | Mes 2 a 11 (excluido) | Lunes a sábado de 08:00 a 16:00 (UTC-4). |
| Co45 | Cota 45 | Escarpe<br>y <br>excavaciones | MP10, MP2,5, MPS. | MP10, MP2,5, MPS. | 21183 | 1 | Mes 2 a 11 (excluido) | Lunes a sábado de 08:00 a 16:00 (UTC-4). |
| Su11 | Superficie 1 | Escarpe,<br>nivelación<br>y <br>compactación | MP10, MP2,5, MPS. | MP10, MP2,5, MPS. | 13396 | 1 | Mes 2 a 11 (excluido) | Lunes a sábado de 08:00 a 16:00 (UTC-4). |
| Ta11 | Tall Oil | Excavaciones,<br>nivelación<br>y <br>compactación | MP10, MP2,5, MPS. | MP10, MP2,5, MPS. | 462 | 1 | Mes 2 a 11 (excluido) | Lunes a sábado de 08:00 a 16:00 (UTC-4). |
| Chi11 | Chipscrinning | Excavaciones | MP10, MP2,5, MPS. | MP10, MP2,5, MPS. | 127 | 1 | Mes 2 a 11 (excluido) | Lunes a sábado de 08:00 a 16:00 (UTC-4). |

**Tabla 37.: Nivel de actividad para fuente puntual** **-** **Escenario 3 Fase de cierre.****

| ID | Localización | Fuente | Emisiones | Tipo de<br>fuente | N° equipos | Temperatura<br>(K) | Diámetro<br>(m) | Altura<br>de la<br>fuente<br>(m) | Velocidad<br>de<br>emisión<br>(m/s) | Meses<br>emite | Periodo emisión |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GE_11 | Grupos<br>electrógenos | Grupos<br>electrógenos | MP10, <br>MP2,5, <br>MPS,<br>NO2, SO2 y CO. | Puntual | 2 | 838,15 | 0,0635 | 1,9 | 77 | Mes 1 | Lunes a sábado de 11:00 a 19:00(UTC-4). |

**Tabla 38.: Nivel de actividad para fuentes de ruta** **-** **Escenario 3 Fase de cierre.****

| ID | Fuente | Emisiones | Tipo de<br>fuente | Distancia<br>total (km) | Altura de<br>la fuente<br>(m) | Meses<br>emite | Periodo emisión |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ID6 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 6 | MP10, MP2,5, MPS, NO2, SO2 y CO. | Ruta | 185.483 | 1 | Mes 1 al 12 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID7 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 7 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 17.985 | 1 | Mes 1 al 12 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID9 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 9 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 1.364 | 1 | Mes 1 al 12 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID10 | Tránsito<br>y <br>combustión<br>caminos pavimentados -<br>Ruta ID 10 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 1.139 | 1 | Mes 1 al 12 | Lunes a sábado de 08:00 a 18:00(UTC-4). |
| ID15 | Tránsito<br>y <br>combustión<br>caminos no pavimentados -<br>Ruta ID15 | MP10, MP2,5, MPS, NO2, SO2 y CO. | MP10, MP2,5, MPS, NO2, SO2 y CO. | 9.375 | 1 | Mes 1 al 12 | Lunes a sábado de 08:00 a 18:00(UTC-4). |

**Tabla 39.: Factor de variación de la emisión de fuentes ruta** **-** **Escenario 1 Fase de construcción.****

| Mes | Hora en UTC+00 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mes** | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Tabla 40.: Factor de variación de la emisión de fuente difusa** **-** **Escenario 1 Fase de construcción.****

| Mes | Hora en UTC+00 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mes** | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Tabla 41.: Factor de variación de la emisión de fuente puntual** **-** **Escenario 1 Fase de construcción.****

| Mes | Hora en UTC+00 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mes** | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Tabla 42.: Factor de variación de la emisión de fuentes de ruta** **-** **Escenario 1 incremento de la emisión de la****

| Mes | Hora en UTC+00 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mes** | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |

**Tabla 43.: Factor de variación de la emisión de fuente puntual** **-** **Escenario 1 incremento de la emisión de la****

| Mes<br>1 2 3 4 5 6 7 8 9 10 11 12<br>0 0 0 1 1 1 1 1 1 1 1 1 | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mes<br>1 2 3 4 5 6 7 8 9 10 11 12<br>0 0 0 1 1 1 1 1 1<br>1 <br>1 <br>1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| Mes<br>1 2 3 4 5 6 7 8 9 10 11 12<br>0 0 0 1 1 1 1 1 1<br>1 <br>1 <br>1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

**Tabla 44.: Factor de variación de la emisión de fuentes de ruta** **-** **Escenario 2 incremento de la emisión de la****

| Mes | Hora en UTC+00 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mes** | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |

**Tabla 45.: Factor de variación de la emisión de la fuente puntual** **-** **Escenario 3 Fase de cierre.****

| Mes | Hora en UTC+00 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mes** | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Tabla 46.: Factor de variación de la emisión de fuente difusa Cota 45, Tall Oil, Superficie 1 y Chipscrinning****

| Mes | Hora en UTC+00 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mes** | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Tabla 47.: Factor de variación de la emisión de la fuente difusa evaporadores, caldera, batch y horno****

| Mes | Hora en UTC+00 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mes** | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |

**Tabla 48.: Factor de variación de la emisión de fuente difusa superficie 2** **-** **Escenario 3 Fase de cierre.****

| Mes | Hora en UTC+00 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mes** | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |

**Tabla 49.: Factor de variación de la emisión de las fuentes de ruta** **-** **Escenario 3 Fase de cierre.****

| Mes | Hora en UTC+00 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mes** | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |

**Tabla 50.: Ubicación de la estación meteorológica superficial.****

| Nombre<br>estación | Distancia<br>al<br>perímetro<br>del<br>proyecto<br>(km) | Altura<br>m.s.n.m<br>(m)2 | Coordenadas UTM<br>Datum WGS 84 Huso<br>18 | Col5 | Variables meteorológicas1 | Col7 | Col8 | Col9 | % datos disponibles4 | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Nombre**<br>**estación** | **Distancia**<br>**al**<br>**perímetro**<br>**del**<br>**proyecto**<br>**(km)** | **Altura**<br>**m.s.n.m**<br>**(m)2 ** | **Este (m)** | **Norte (m)** | **T3 ** | **VV3 ** | **DV3 ** | **Hr3 ** | **Hr3 ** | **Hr3 ** | **Hr3 ** |
| **Nombre**<br>**estación** | **Distancia**<br>**al**<br>**perímetro**<br>**del**<br>**proyecto**<br>**(km)** | **Altura**<br>**m.s.n.m**<br>**(m)2 ** | **Este (m)** | **Norte (m)** | **T3 ** | **VV3 ** | **DV3 ** | **Hr3 ** | **2020** | **2021** | **2022** |
| **Laja** | 1,83 | 68,33 | 702.992 | 5.872.963 | √ | √ | √ | √ | 96% | 97,1% | 95,3% |

**Tabla 51.: Valores de los índices de la predicción proporcionada por el modelo para la estación meteorológica** **-** **Años 2020 a 2022****

| Variable Meteorológica | 2020 | Col3 | Col4 | Col5 | 2021 | Col7 | Col8 | Col9 | 2022 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Variable Meteorológica** | **RMSE** | **MAE** | **BIAS** | **r** | **RMSE** | **MAE** | **BIAS** | **r ** | **RMSE** | **MAE** | **BIAS** | **r ** |
| **Temperatura Superficial** | 4,9 °C | 4,0 °C | -3,7 °C | 0,9 | 4,0 °C | 3,1°C | -2,1°C | 0,9 | 2,9 °C | 2,3 °C | -0,4 °C | 0,9 |
| **Velocidad Viento** | 1,5 m/s | 1,1 m/s | 0,9 m/s | 0,6 | 1,7 m/s | 1,3 m/s | 1,1 m/s | 0,6 | 1,5 m/s | 1,1 m/s | 0,8 m/s | 0,6 |

**Tabla 52.: Normativas aplicables para material particulado.****

| Contaminante<br>normado | Decreto<br>aplicable | Periodo de<br>Evaluación de<br>Cumplimiento<br>de Norma | Concentración<br>máxima<br>permitida | Criterio de excedencia |
| --- | --- | --- | --- | --- |
| **Material**<br>**Particulado**<br>**Respirable**<br>**Fino (MP2,5) ** | D.S N° 12/2011<br>del Ministerio del<br>Medio Ambiente. | Anual | 20 μg/m3N | Cuando el promedio de las concentraciones<br>anuales sea mayor a 20 (μg/m3N). |
| **Material**<br>**Particulado**<br>**Respirable**<br>**Fino (MP2,5) ** | D.S N° 12/2011<br>del Ministerio del<br>Medio Ambiente. | 24 h | 50 μg/m3N | Cuando el percentil 98 de los promedios<br>diarios durante un año, sea mayor a 50<br>(μg/m3N). |
| **Material**<br>**Particulado**<br>**Respirable**<br>**(MP10) ** | D.S N° 12/2022<br>del Ministerio del<br>Medio Ambiente. | Anual | 50 μg/m3N | Cuando el promedio de las concentraciones<br>anuales sea mayor a 50 (μg/m3N). |
| **Material**<br>**Particulado**<br>**Respirable**<br>**(MP10) ** | D.S N° 12/2022<br>del Ministerio del<br>Medio Ambiente. | 24 h | 130 μg/m3N | Cuando el percentil 98 de los promedios<br>diarios durante un año, sea mayor o igual<br>130 (μg/m3N). |

**Tabla 53.: Normativas aplicables para gases.****

| Contaminante<br>normado | Decreto<br>aplicable | Periodo de<br>Evaluación de<br>Cumplimiento<br>de Norma | Concentración<br>máxima<br>permitida | Criterio de excedencia |
| --- | --- | --- | --- | --- |
| **Dióxido de**<br>**Azufre (SO2)** <br>**Norma**<br>**Primario** | D.S N° 104/2018<br>del Ministerio del<br>Medio Ambiente. | Anual | 60 μg/m3N | Cuando el promedio de las concentraciones<br>anuales sea mayor o igual a 60 (μg/m3N). |
| **Dióxido de**<br>**Azufre (SO2)** <br>**Norma**<br>**Primario** | D.S N° 104/2018<br>del Ministerio del<br>Medio Ambiente. | 24 h | 150 μg/m3N | Cuando el percentil 99 de los promedios<br>diarios durante un año, sea mayor o igual a<br>150 (μg/m3N). |
| **Dióxido de**<br>**Azufre (SO2)** <br>**Norma**<br>**Primario** | D.S N° 104/2018<br>del Ministerio del<br>Medio Ambiente. | 1 h | 350 μg/m3N | Si<br>en<br>un<br>año<br>calendario,<br>el<br>valor<br>correspondiente al percentil 98,5 de las<br>concentraciones de 1 hora, fuere mayor o<br>igual al doble del valor de la norma que se<br>establece. |
| **Dióxido de**<br>**Azufre (SO2)** | D.S N° 22/2009<br>del Ministerio de | Anual | 60 μg/m3N | Cuando el promedio de las concentraciones<br>anuales sea mayor o igual a 60 (μg/m3N). |

**Tabla 54.: Norma homologada para evaluar impacto por material particulado sedimentable.****

| Contaminante<br>normado | Norma<br>homologada | Periodo de<br>Evaluación de<br>Cumplimiento<br>de Norma | Concentración<br>máxima<br>permitida | Criterio de excedencia |
| --- | --- | --- | --- | --- |
| Material<br>Particulado<br>Sedimentable <br>(MPS) | Ordinance on Air<br>pollution. Swiss<br>Federal Council. | Anual | 200<br>mg/(m2*d) | Cuando el promedio de la tasa de deposición<br>anuales sea mayor o igual a 200 mg/(m2*d). |

**Tabla 55.: Norma homologada para evaluar impacto por TRS.****

| Contaminante<br>normado | Norma<br>homologada | Periodo de<br>Evaluación de<br>Cumplimiento<br>de Norma | Concentración<br>máxima<br>permitida | Criterio de excedencia |
| --- | --- | --- | --- | --- |
| Azufre total<br>reducido <br>(TRS) | Resolución 1.541<br>(2013) de<br>Colombia. | 24 horas | 7 μg/m3 | Superación de la máxima exposición. |
| Azufre total<br>reducido <br>(TRS) | Resolución 1.541<br>(2013) de<br>Colombia. | 1 hora | 40 μg/m3 | 40 μg/m3 |

**Tabla 56.: Datos disponibles en estaciones de monitoreo de calidad del aire.****

| Estación | Parámetro medido | Periodo medición | Número datos validos | Col5 | Col6 | Col7 | Col8 | Porcentaje de datos validos por año | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Estación** | **Parámetro medido** | **Periodo medición** | **2018** | **2019** | **2020** | **2021** | **2022** | **2018** | **2019** | **2020** | **2021** | **2022** |
| Laja | MP10 | 2020 a 2022 | -- | -- | 8.726 | 8.652 | 8.669 | -- | -- | 99% | 99% | 99% |
| Laja | MP2,5 | 2018 a 2020 | 8.659 | 8.600 | 3.647 | -- | -- | 99% | 98% | 42% | -- | -- |
| Laja | SO2 | 2020 a 2022 | -- | -- | 8.550 | 8.564 | 8.474 | -- | -- | 97% | 98% | 97% |
| Laja | NO2 | 2020 a 2022 | -- | -- | 8.584 | 8.521 | 8.581 | -- | -- | 98% | 97% | 98% |
| Laja | CO | 2020 a 2022 | -- | -- | 8.647 | 8.584 | 8.545 | -- | -- | 97% | 97% | 98% |
| Laja | TRS | 2020 a 2022 | -- | -- | 8.485 | 8.544 | 8.476 | -- | -- | 97% | 98% | 97% |
| San Rosendo | MP10 | 2020 a 2022 | -- | -- | 8.553 | 8.332 | 8.672 | -- | -- | 97% | 95% | 99% |
| San Rosendo | MP2,5 | 2020 a 2022 | -- | -- | 8.553 | 8.332 | 8.672 | -- | -- | 97% | 95% | 99% |
| San Rosendo | SO2 | 2020 a 2022 | -- | -- | 8.479 | 8.358 | 8.472 | -- | -- | 97% | 95% | 97% |
| San Rosendo | NO2 | 2020 a 2022 | -- | -- | 8.530 | 8.435 | 8.570 | -- | -- | 97% | 96% | 98% |
| San Rosendo | CO | 2020 a 2022 | -- | -- | 8.559 | 8.502 | 8.580 | -- | -- | 98% | 98% | 98% |
| San Rosendo | TRS | 2020 a 2022 | -- | -- | 8.546 | 8.373 | 8.473 | -- | -- | 97% | 96% | 97% |

**Tabla 57.: Línea base.****

| Estación | Estadístico | Línea base en estación | Límite normativo | % normativa |
| --- | --- | --- | --- | --- |
| Laja | Concentración anual MP10 (μg/m3) | 29 | 50 | 58% |
| Laja | Percentil 98 concentración 24 horas MP10 (μg/m3) | 67 | 130 | 52% |
| Laja | Promedio anual MP2,5 (μg/m3) | 22 | 20 | 110% |
| Laja | Percentil 98 concentración 24 horas MP2,5 (μg/m3) | 89 | 50 | 178% |
| Laja | Concentraciones 24h de SO2, P99 (μg/m3) | 4 | 150 | 3% |
| Laja | Concentraciones 1h de SO2, P98,5 (μg/m3) | 5 | 350 | 1% |
| Laja | Promedio Anual SO2 (μg/m3) | 1 | 60 | 2% |
| Laja | Concentraciones 24h SO2, P99,7 (μg/m3) | 6 | 260 | 2% |
| Laja | Concentraciones 1h SO2, P99,73 (μg/m3) | 12 | 700 | 2% |
| Laja | Concentraciones 1h NO2, P99 (μg/m3) | 40 | 400 | 10% |
| Laja | Promedio Concentraciones NO2 (μg/m3) | 8 | 100 | 8% |
| Laja | Concentraciones 1h CO, P99 (mg/m3) | 5 | 30 | 17% |
| Laja | Concentraciones 8h móvil CO, P99 (mg/m3) | 3 | 10 | 30% |
| Laja | Concentraciones 24h TRS (μg/m3) | 4 | 7 | 57% |

**Tabla 58.: Resumen SILs.****

| Contaminante | Periodo | SIL (μg/m3) |
| --- | --- | --- |
| MP2,5 | 24 horas | 1,71 |
| MP2,5 | Anual | 0,33 |
| TRS | 1 hora | 0,4 |

**Tabla 59.: Aporte proyectos no ejecutados, colindantes al perímetro del proyecto.****

| Proyecto | Estadístico | Aporte en<br>estación Laja |
| --- | --- | --- |
| Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1) | Promedio anualMP10 (μg/m3) | 1 |
| Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1) | Percentil 98 concentración 24 horas MP10 (μg/m3) | 3 |
| Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1) | Promedio anual MP2,5 (μg/m3) | 0 |
| Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1) | Percentil 98 concentración 24 horas MP2,5 (μg/m3) | 1 |
| Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1) | Promedio Concentraciones 24h de SO2, P99 (μg/m3) | 0 |
| Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1) | Promedio concentraciones 1h de SO2, P98,5 (μg/m3) | 0 |
| Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1) | Promedio Anual SO2 (μg/m3) | 0 |
| Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1) | Promedio Concentraciones 24h SO2, P99,7 (μg/m3) | 0 |
| Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1) | Promedio Concentraciones 1h SO2, P99,73 (μg/m3) | 0 |
| Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1) | Promedio Concentraciones 1h NO2, P99 (μg/m3) | 9 |
| Nueva conexión y ampliación S/E Celulosa<br>Laja (Proyecto 1) | Promedio Concentraciones NO2 (μg/m3) | 0 |

**Tabla 60.: Receptores discretos.****

| ID | Nombre | Altura m.s.n.m<br>(m)1 | Distancia al límite del<br>perímetro del proyecto<br>(m) | Coordenadas UTM<br>Datum WGS 84 Huso 18 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **ID** | **Nombre** | **Altura m.s.n.m**<br>**(m)1 ** | **Distancia al límite del**<br>**perímetro del proyecto**<br>**(m)** | **Este (m)** | **Norte (m)** |
| Rr1 | Receptor 1 | 65,3 | 417 | 703.097 | 5.871.334 |
| Rr2 | Receptor 2 | 61,3 | 557 | 702.696 | 5.871.708 |
| Rr3 | Receptor 3 | 80,2 | 958 | 703.688 | 5.871.455 |
| Rr4 | Receptor 4 | 62,8 | 858 | 702.929 | 5.871.976 |
| Rr5 | Receptor 5 | 62,2 | 170 | 702.686 | 5.871.321 |
| Rr6 | Receptor 6 | 62,1 | 47 | 702.519 | 5.871.048 |
| Rr7 | Estación Laja | 68,3 | 1.835 | 702.992 | 5.872.963 |
| Rr8 | Estación San<br>Rosendo | 80,1 | 2.393 | 702.104 | 5.873.472 |

**Tabla 61.: Descripción de receptores discretos.****

| ID | Descripción | Zonificación del Plan Regulador Comunal, región<br>del biobío1 |
| --- | --- | --- |
| Rr1 | Colegio San Jorge | Urbano. Zona residencial 3. |
| Rr2 | Estacionamiento Hospital Antiguo de Laja. | Urbano. Zona residencial 3. |
| Rr3 | Población Nivequeten. Calle Los Magnolios, esquina los<br>manzanos. | Urbano. Zona residencial 3. |
| Rr4 | Calle Los Aromos, altura N° 107 | Urbano. Zona residencial 3. |
| Rr5 | Calle Balmaceda N°52. | Urbano. Zona centro cívico. |
| Rr6 | Casa habitación cruce ferroviario. | Urbano. Zona actividades productivas 1. |
| EL | Estación Laja | Urbano. Zona mixta 1. |
| ESR | Estación San Rosendo | No definido. Se encuentra dentro del límite<br>urbano. |

**Tabla 62.: Promedio anual de la concentración de MP** **10** **-** **Escenario 1.****

| Receptor | Línea base<br>promedio<br>anual<br>(μg/m3N). | Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N) | Aporte proyectos<br>con RCA (proyecto<br>1 + proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N) | Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma | Porcentaje<br>de normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 29 | 0 | 1 | 30 | 50 μg/m3N | 60% | Si |
| Receptor 2 | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Receptor 3 | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Receptor 4 | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Receptor 5 | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Receptor 6 | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Estación Laja | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Estación San Rosendo | 36 | 0 | 1 | 37 | 37 | 74% | Si |

**Tabla 63.: Percentil 98 de la concentración diaria de MP** **10** **-** **Escenario 1.****

| Receptor | Línea base<br>percentil 98<br>24 h<br>(μg/m3N). | Percentil 98 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima permitida<br>percentil 98 de 24<br>horas Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 67 | 0 | 3 | 71 | 130 μg/m3N | 54% | Si |
| Receptor 2 | 67 | 1 | 3 | 71 | 71 | 54% | Si |
| Receptor 3 | 67 | 0 | 3 | 70 | 70 | 54% | Si |
| Receptor 4 | 67 | 1 | 3 | 71 | 71 | 54% | Si |
| Receptor 5 | 67 | 1 | 3 | 71 | 71 | 55% | Si |
| Receptor 6 | 67 | 1 | 3 | 71 | 71 | 55% | Si |
| Estación Laja | 67 | 0 | 3 | 71 | 71 | 54% | Si |
| Estación San Rosendo | 99 | 1 | 3 | 103 | 103 | 79% | Si |

**Tabla 64.: Impacto sobre la salud de las personas por el promedio anual de la concentración de MP** **2.5** **-** **Escenario 1.****

| Receptor | Línea base<br>promedio<br>anual<br>(μg/m3N). | Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N) | Aporte<br>proyectos<br>con RCA<br>(proyecto 1 +<br>proyecto 2)<br>(μg/m3N) | Total (línea<br>base, aporte<br>proyecto y<br>aporte<br>proyectos con<br>RCA)<br>(μg/m3N) | Concentración<br>máxima<br>permitida<br>Promedio anual<br>Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Significancia | Porcentaje<br>del valor de<br>significancia<br>(%) | Impacto en<br>significativo<br>sobre la<br>salud de las<br>personas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 3 | 22 | 0 | 0 | 22 |  | 111% |  | 13% | No |
| Receptor 4 | 22 | 0 | 0 | 22 | 22 | 112% | 112% | 29% | No |
| Receptor 5 | 22 | 0 | 0 | 22 | 22 | 112% | 112% | 77% | No |
| Receptor 6 | 22 | 0 | 0 | 22 | 22 | 112% | 112% | 57% | No |
| Estación Laja | 22 | 0 | 0 | 22 | 22 | 112% | 112% | 19% | No |
| Estación San Rosendo | 26 | 0 | 0 | 26 | 26 | 132% | 132% | 48% | No |

**Tabla 65.: Impacto sobre la salud de las personas del percentil 98 de la concentración diaria de MP** **2.5** **- Escenario 1.****

| Receptor | Línea<br>base<br>percentil<br>98 24 h<br>(μg/m3N). | Aporte<br>Proyecto<br>Percentil 98<br>de la<br>concentración<br>en inmisión<br>24 h<br>(μg/m3N) | Aporte<br>proyectos<br>con RCA<br>(proyecto<br>1 +<br>proyecto<br>2)<br>(μg/m3N) | Total<br>(línea<br>base,<br>aporte<br>proyecto<br>y aporte<br>proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima<br>permitida<br>percentil 98<br>de 24 horas<br>Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Significancia | Porcentaje<br>del valor de<br>significancia<br>(%) | Impacto en<br>significativo<br>sobre la<br>salud de las<br>personas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 89 | 0 | 1 | 90 | 50 μg/m3N | 180% | 1,71<br>μg/m3N | 26% | **No** |
| Receptor 2 | 89 | 1 | 1 | 91 | 91 | 181% | 181% | 42% | **No** |
| Receptor 3 | 89 | 0 | 1 | 90 | 90 | 180% | 180% | 16% | **No** |
| Receptor 4 | 89 | 1 | 1 | 90 | 90 | 181% | 181% | 32% | **No** |
| Receptor 5 | 89 | 1 | 1 | 91 | 91 | 182% | 182% | 64% | **No** |
| Receptor 6 | 89 | 1 | 1 | 91 | 91 | 181% | 181% | 45% | **No** |
| Estación Laja | 89 | 0 | 1 | 90 | 90 | 180% | 180% | 25% | **No** |
| Estación San Rosendo | 101 | 1 | 1 | 102 | 102 | 205% | 205% | 32% | **No** |

**Tabla 66.: Promedio anual de la tasa de deposición del material particulado sedimentable (MPS)** **-** **Escenario 1.****

| Receptor | Aporte Proyecto tasa de deposición<br>promedio anual (mg/m2N/d) | Tasa de deposición promedio anual<br>máxima permitida Valor Norma | Porcentaje de<br>normativa (%) | Cumplimiento de la<br>normativa |
| --- | --- | --- | --- | --- |
| Receptor 1 | 0 | 200 mg/(m2*d) | 0% | Si |
| Receptor 2 | 0 | 0 | 0% | Si |
| Receptor 3 | 0 | 0 | 0% | Si |
| Receptor 4 | 0 | 0 | 0% | Si |
| Receptor 5 | 0 | 0 | 0% | Si |
| Receptor 6 | 0 | 0 | 0% | Si |
| Estación Laja | 0 | 0 | 0% | Si |
| Estación San Rosendo | 0 | 0 | 0% | Si |

**Tabla 67.: Promedio anual de la concentración de dióxido de nitrógeno (NO** **2** **)** **-** **Escenario 1.****

| Receptor | Línea base<br>promedio<br>anual<br>(μg/m3N). | Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N) | Aporte proyectos<br>con RCA (proyecto<br>1 + proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N) | Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma | Porcentaje<br>de normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 8 | 0 | 0 | 9 | 100 μg/m3N | 9% | Si |
| Receptor 2 | 8 | 1 | 0 | 9 | 9 | 9% | Si |
| Receptor 3 | 8 | 0 | 0 | 9 | 9 | 9% | Si |
| Receptor 4 | 8 | 0 | 0 | 9 | 9 | 9% | Si |
| Receptor 5 | 8 | 1 | 0 | 9 | 9 | 9% | Si |
| Receptor 6 | 8 | 1 | 0 | 9 | 9 | 9% | Si |
| Estación Laja | 8 | 0 | 0 | 9 | 9 | 9% | Si |

**Tabla 68.: Percentil 99 de la concentración horaria de NO** **2** **-** **Escenario 1.****

| Receptor | Línea base<br>percentil 99<br>1 h<br>(μg/m3N). | Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 1 h (μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima permitida<br>percentil 99 de 1<br>hora Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 40 | 7 | 11 | 58 | 400 μg/m3N | 14% | Si |
| Receptor 2 | 40 | 5 | 11 | 55 | 55 | 14% | Si |
| Receptor 3 | 40 | 6 | 11 | 57 | 57 | 14% | Si |
| Receptor 4 | 40 | 4 | 11 | 54 | 54 | 14% | Si |
| Receptor 5 | 40 | 7 | 11 | 58 | 58 | 14% | Si |
| Receptor 6 | 40 | 11 | 11 | 62 | 62 | 15% | Si |
| Estación Laja | 40 | 2 | 11 | 53 | 53 | 13% | Si |
| Estación San Rosendo | 37 | 3 | 11 | 50 | 50 | 13% | Si |

**Tabla 69.: Promedio anual de la concentración de dióxido de azufre (SO** **2** **)** **-** **Escenario 1.****

| Receptor | Línea base<br>promedio<br>anual<br>(μg/m3N). | Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N) | Aporte proyectos<br>con RCA (proyecto<br>1 + proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N) | Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma | Porcentaje<br>de normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 1 | 0 | 0 | 1 | 60 μg/m3N | 2% | Si |
| Receptor 2 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Receptor 3 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Receptor 4 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Receptor 5 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Receptor 6 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Estación Laja | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Estación San Rosendo | 3 | 0 | 0 | 3 | 3 | 5% | Si |

**Tabla 70.: Percentil 99 de la concentración diaria de SO** **2** **-** **Escenario 1.****

| Receptor | Línea base<br>percentil 99<br>24 h<br>(μg/m3N). | Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima permitida<br>percentil 99 de 24<br>horas Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 4 | 1 | 0 | 5 | 150 μg/m3N | 3% | Si |
| Receptor 2 | 4 | 2 | 0 | 6 | 6 | 4% | Si |
| Receptor 3 | 4 | 1 | 0 | 5 | 5 | 3% | Si |
| Receptor 4 | 4 | 1 | 0 | 5 | 5 | 4% | Si |
| Receptor 5 | 4 | 2 | 0 | 6 | 6 | 4% | Si |
| Receptor 6 | 4 | 2 | 0 | 6 | 6 | 4% | Si |
| Estación Laja | 4 | 1 | 0 | 5 | 5 | 3% | Si |
| Estación San Rosendo | 7 | 1 | 0 | 8 | 8 | 5% | Si |

**Tabla 71.: Percentil 98,5 de la concentración de 1 h de SO** **2** **-** **Escenario 1.****

| Receptor | Línea base<br>percentil 98,5<br>1 h (μg/m3N). | Aporte Proyecto<br>Percentil 98,5 de la<br>concentración en<br>inmisión 1 h (μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima permitida<br>Percentil 98,5 de 1 h<br>Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 5 | 1 | 0 | 7 | 350 μg/m3N | 2% | Si |
| Receptor 2 | 5 | 3 | 0 | 8 | 8 | 2% | Si |
| Receptor 3 | 5 | 1 | 0 | 6 | 6 | 2% | Si |
| Receptor 4 | 5 | 2 | 0 | 7 | 7 | 2% | Si |
| Receptor 5 | 5 | 3 | 0 | 9 | 9 | 2% | Si |
| Receptor 6 | 5 | 3 | 0 | 8 | 8 | 2% | Si |
| Estación Laja | 5 | 1 | 0 | 7 | 7 | 2% | Si |
| Estación San Rosendo | 8 | 2 | 0 | 10 | 10 | 3% | Si |

**Tabla 72.: Percentil 99,7 de la concentración diaria de SO** **2** **-** **Escenario 1.****

| Receptor | Línea base<br>percentil 99,7<br>24 h<br>(μg/m3N). | Aporte Proyecto<br>Percentil 99,7 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima permitida<br>percentil 99,7 de 24<br>horas Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 6 | 2 | 0 | 8 | 260 μg/m3N | 3% | Si |
| Receptor 2 | 6 | 2 | 0 | 9 | 9 | 3% | Si |
| Receptor 3 | 6 | 2 | 0 | 8 | 8 | 3% | Si |
| Receptor 4 | 6 | 2 | 0 | 8 | 8 | 3% | Si |
| Receptor 5 | 6 | 3 | 0 | 9 | 9 | 3% | Si |
| Receptor 6 | 6 | 2 | 0 | 9 | 9 | 3% | Si |
| Estación Laja | 6 | 1 | 0 | 7 | 7 | 3% | Si |
| Estación San Rosendo | 9 | 2 | 0 | 11 | 11 | 4% | Si |

**Tabla 73.: Percentil 99,73 de la concentración horaria de SO** **2** **-** **Escenario 1.****

| Receptor | Línea base<br>percentil<br>99,73 1 h<br>(μg/m3N). | Aporte Proyecto<br>Percentil 99,73 de la<br>concentración en<br>inmisión 1 h (μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima permitida<br>percentil 99,73 de 1<br>hora Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 12 | 5 | 1 | 18 | 700 μg/m3N | 3% | Si |
| Receptor 2 | 12 | 6 | 1 | 18 | 18 | 3% | Si |
| Receptor 3 | 12 | 3 | 1 | 15 | 15 | 2% | Si |
| Receptor 4 | 12 | 4 | 1 | 17 | 17 | 2% | Si |
| Receptor 5 | 12 | 7 | 1 | 20 | 20 | 3% | Si |
| Receptor 6 | 12 | 7 | 1 | 19 | 19 | 3% | Si |
| Estación Laja | 12 | 3 | 1 | 16 | 16 | 2% | Si |
| Estación San Rosendo | 16 | 3 | 1 | 19 | 19 | 3% | Si |

**Tabla 74.: Percentil 99 de la concentración de 1 h de CO** **-** **Escenario 1.****

| Receptor | Línea base<br>percentil 99 1<br>h (mg/m3N). | Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 1 h<br>(mg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(mg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(mg/m3N) | Concentración<br>máxima permitida<br>percentil 99 de 1<br>hora Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 5 | 0 | 0 | 5 | 30 mg/m3N | 17% | Si |
| Receptor 2 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Receptor 3 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Receptor 4 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Receptor 5 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Receptor 6 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Estación Laja | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Estación San Rosendo | 6 | 0 | 0 | 6 | 6 | 20% | Si |

**Tabla 75.: Percentil 99 de la concentración 8 h de CO** **-** **Escenario 1.****

| Receptor | Línea base<br>percentil 99 8<br>h (mg/m3N). | Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 8 h<br>(mg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(mg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(mg/m3N) | Concentración<br>máxima permitida<br>percentil 99 de 8<br>horas Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 3 | 0 | 0 | 3 | 10 mg/m3N | 30% | Si |
| Receptor 2 | 3 | 0 | 0 | 3 | 3 | 30% | Si |
| Receptor 3 | 3 | 0 | 0 | 3 | 3 | 30% | Si |
| Receptor 4 | 3 | 0 | 0 | 3 | 3 | 30% | Si |
| Receptor 5 | 3 | 0 | 0 | 3 | 3 | 30% | Si |
| Receptor 6 | 3 | 0 | 0 | 3 | 3 | 30% | Si |
| Estación Laja | 3 | 0 | 0 | 3 | 3 | 30% | Si |
| Estación San Rosendo | 4 | 0 | 0 | 4 | 4 | 40% | Si |

**Tabla 76.: Concentración diaria de TRS** **-** **Escenario 1.****

| Receptor | Línea base<br>concentración 24<br>horas (μg/m3N). | Aporte Proyecto<br>concentración 24<br>horas (μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos con<br>RCA) (μg/m3N) | Concentración máxima<br>permitida Concentración<br>24 h Valor Norma | Porcentaje de<br>normativa (%) | Cumplimiento de<br>la normativa |
| --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 4 | 0 | 4 | 7 μg/m3N | 58% | Si |
| Receptor 2 | 4 | 0 | 4 | 4 | 58% | Si |
| Receptor 3 | 4 | 0 | 4 | 4 | 58% | Si |
| Receptor 4 | 4 | 0 | 4 | 4 | 58% | Si |
| Receptor 5 | 4 | 0 | 4 | 4 | 58% | Si |
| Receptor 6 | 4 | 0 | 4 | 4 | 58% | Si |
| Estación Laja | 4 | 0 | 4 | 4 | 58% | Si |
| Estación San Rosendo | 4 | 0 | 4 | 4 | 58% | Si |

**Tabla 77.: Impacto sobre la salud de las personas por la concentración horaria de TRS** **-** **Escenario 1.****

| Receptor | Línea base<br>concentración<br>1 hora<br>(μg/m3N). | Aporte<br>Proyecto<br>concentración<br>1 hora<br>(μg/m3N) | Total (línea<br>base, aporte<br>proyecto y<br>aporte<br>proyectos con<br>RCA)<br>(μg/m3N) | Concentración<br>máxima<br>permitida<br>Concentración<br>1 h Valor<br>Norma | Porcentaje de<br>normativa<br>(%) | Cumplimiento<br>de la<br>normativa | Significancia | Porcentaje<br>del valor de<br>significancia<br>(%) | Impacto<br>significativo<br>sobre la salud<br>de las<br>personas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 20 | 0 | 20 | 40 μg/m3N | 51% | Si | 0,4 μg/m3N | -- | -- |
| Receptor 2 | 20 | 0 | 20 | 20 | 50% | Si | Si | -- | -- |
| Receptor 3 | 20 | 0 | 20 | 20 | 50% | Si | Si | -- | -- |
| Receptor 4 | 20 | 0 | 20 | 20 | 50% | Si | Si | -- | -- |
| Receptor 5 | 20 | 0 | 20 | 20 | 51% | Si | Si | -- | -- |
| Receptor 6 | 20 | 0 | 20 | 20 | 51% | Si | Si | -- | -- |
| Estación Laja | 20 | 0 | 20 | 20 | 50% | Si | Si | -- | -- |
| Estación San Rosendo | 61 | 0 | 61 | 61 | 153% | -- | -- | 28% | No |

**Tabla 78.: Resumen de Punto de Máximo Impacto** **-** **Escenario 1.****

| Estadístico | Año estudio mayor<br>concentración ambiental | Coordenadas UTM | Col4 | Aporte máximo<br>del proyecto | Localización (dentro o<br>fuera de planta) |
| --- | --- | --- | --- | --- | --- |
| **Estadístico** | **Año estudio mayor**<br>**concentración ambiental** | **Datum WGS 84 Huso 18** | **Datum WGS 84 Huso 18** | **Datum WGS 84 Huso 18** | **Datum WGS 84 Huso 18** |
| **Estadístico** | **Año estudio mayor**<br>**concentración ambiental** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| Promedio anual MP10 (μg/m3) | 2022 | 702.904,58 | 5.870.494,68 | 0 | Dentro de perímetro<br>planta |
| Percentil 98 concentración 24 horas MP10 (μg/m3) | 2022 | 702.904,58 | 5.870.494,68 | 2 | Dentro de perímetro<br>planta |
| Promedio anual MP2,5 (μg/m3) | 2022 | 702.904,58 | 5.870.494,68 | 0 | Dentro de perímetro<br>planta |
| Percentil 98 concentración 24 horas MP2,5 (μg/m3) | 2022 | 702.904,58 | 5.870.494,68 | 2 | Dentro de perímetro<br>planta |
| Promedio anual tasa de deposición MPS (mg/m2/d) | 2021 | 701.948,4 | 5.872.519,81 | 7 | Fuera de perímetro de<br>planta |
| Concentración 24h de SO2, P99 (μg/m3) | 2021 | 702.686,41 | 5.871.322,12 | 2 | Fuera de perímetro de<br>planta |
| Concentración 1h de SO2, P98,5 (μg/m3) | 2021 | 702.686,41 | 5.871.322,12 | 3 | Fuera de perímetro de<br>planta |
| Promedio Anual SO2 (μg/m3) | 2021 | 702.686,41 | 5.871.322,12 | 0 | Fuera de perímetro de<br>planta |
| Concentración 24h SO2, P99,7 (μg/m3) | 2021 | 702.686,41 | 5.871.322,12 | 3 | Fuera de perímetro de<br>planta |
| Concentración 1h SO2, P99,73 (μg/m3) | 2021 | 702.686,41 | 5.871.322,12 | 7 | Fuera de perímetro de<br>planta |
| Concentración 1h NO2, P99 (μg/m3) | 2022 | 702.904,58 | 5.870.494,68 | 92 | Dentro de perímetro<br>planta |
| Concentración NO2 (μg/m3) | 2022 | 702.904,58 | 5.870.494,68 | 5 | Dentro de perímetro<br>planta |
| Concentración 1h CO, P99 (mg/m3) | 2022 | 702.904,58 | 5.870.494,68 | 0 | Dentro de perímetro<br>planta |

**Tabla 79.: Cumplimiento de normativa de los estadísticos del PMI** **-** **Escenario 1****

| Estadístico | Línea<br>base | Aporte<br>máximo del<br>proyecto | Aporte proyectos con<br>RCA (proyecto 1 +<br>proyecto 2) | Concentración<br>total | Concentración<br>máxima permitida | Porcentaje de<br>normativa (%) |
| --- | --- | --- | --- | --- | --- | --- |
| Promedio anual tasa de deposición MPS (mg/m2/d) | ND | 7 | ND | 7 | 200 | 3% |
| Concentraciones 24h de SO2, P99 (μg/m3) | 4 | 2 | 0 | 6 | 150 | 4% |
| Concentraciones 1h de SO2, P98,5 (μg/m3) | 5 | 3 | 0 | 9 | 350 | 2% |
| Promedio Anual SO2 (μg/m3) | 1 | 0 | 0 | 1 | 60 | 2% |
| Concentración 24h SO2, P99,7 (μg/m3) | 6 | 3 | 0 | 9 | 260 | 3% |
| Concentración 1h SO2, P99,73 (μg/m3) | 12 | 7 | 1 | 20 | 700 | 3% |
| Concentración 24h TRS (μg/m3) | 4 | 0 | ND | 4 | 7 | 58% |
| Concentración 1h TRS (μg/m3) | 20 | 0 | ND | 20 | 40 | 51% |

**Tabla 80.: Promedio anual de la concentración de MP** **10** **-** **Escenario 2.****

| Receptor | Línea base<br>promedio<br>anual<br>(μg/m3N). | Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N) | Aporte proyectos<br>con RCA (proyecto<br>1 + proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N) | Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma | Porcentaje<br>de normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 29 | 0 | 1 | 30 | 50 μg/m3N | 60% | Si |
| Receptor 2 | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Receptor 3 | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Receptor 4 | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Receptor 5 | 29 | 0 | 1 | 30 | 30 | 61% | Si |
| Receptor 6 | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Estación Laja | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Estación San Rosendo | 36 | 0 | 1 | 37 | 37 | 74% | Si |

**Tabla 81.: Percentil 98 de la concentración diaria de MP** **10** **-** **Escenario 2.****

| Receptor | Línea base<br>percentil 98<br>24 h<br>(μg/m3N). | Percentil 98 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima permitida<br>percentil 98 de 24<br>horas Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 67 | 0 | 3 | 71 | 130 μg/m3N | 54% | Si |
| Receptor 2 | 67 | 1 | 3 | 71 | 71 | 55% | Si |
| Receptor 3 | 67 | 0 | 3 | 70 | 70 | 54% | Si |

**Tabla 82.: Impacto sobre la salud de las personas por el promedio anual de la concentración de MP** **2.5** **-** **Escenario 2.****

| Receptor | Línea<br>base<br>promedio<br>anual<br>(μg/m3N). | Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N) | Aporte<br>proyectos<br>con RCA<br>(proyecto<br>1 +<br>proyecto<br>2)<br>(μg/m3N) | Total<br>(línea<br>base,<br>aporte<br>proyecto<br>y aporte<br>proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima<br>permitida<br>Promedio<br>anual Valor<br>Norma | Porcentaje<br>de<br>normativa<br>(%) | Significancia | Porcentaje<br>del valor de<br>significancia<br>(%) | Impacto<br>significativo<br>sobre la<br>salud de las<br>personas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 22 | 0 | 0 | 22 | 20 μg/m3N | 112% | 0,33 μg/m3N | 30% | No |
| Receptor 2 | 22 | 0 | 0 | 22 | 22 | 112% | 112% | 76% | No |
| Receptor 3 | 22 | 0 | 0 | 22 | 22 | 111% | 111% | 16% | No |
| Receptor 4 | 22 | 0 | 0 | 22 | 22 | 112% | 112% | 38% | No |
| Receptor 5 | 22 | 0 | 0 | 23 | 23 | 113% | 113% | 98% | No |
| Receptor 6 | 22 | 0 | 0 | 22 | 22 | 112% | 112% | 72% | No |
| Estación Laja | 22 | 0 | 0 | 22 | 22 | 112% | 112% | 26% | No |
| Estación San Rosendo | 26 | 0 | 0 | 26 | 26 | 132% | 132% | 66% | No |

**Tabla 83.: Impacto sobre la salud de las personas por el percentil 98 de la concentración diaria de MP** **2.5** **-** **Escenario 2.****

| Receptor | Línea base<br>percentil 98<br>24 h<br>(μg/m3N). | Aporte<br>Proyecto<br>Percentil 98 de<br>la<br>concentración<br>en inmisión 24<br>h (μg/m3N) | Aporte<br>proyectos<br>con RCA<br>(proyecto<br>1 +<br>proyecto<br>2)<br>(μg/m3N) | Total (línea<br>base, aporte<br>proyecto y<br>aporte<br>proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima<br>permitida<br>percentil 98<br>de 24 horas<br>Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Significancia | Porcentaje<br>del valor de<br>significancia<br>(%) | Impacto<br>significativo<br>sobre la<br>salud de las<br>personas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 89 | 0 | 1 | 90 | 50 μg/m3N | 180% | 1,71<br>μg/m3N | 26% | No |
| Receptor 2 | 89 | 1 | 1 | 91 | 91 | 181% | 181% | 46% | No |
| Receptor 3 | 89 | 0 | 1 | 90 | 90 | 180% | 180% | 16% | No |
| Receptor 4 | 89 | 1 | 1 | 90 | 90 | 181% | 181% | 34% | No |
| Receptor 5 | 89 | 1 | 1 | 91 | 91 | 182% | 182% | 64% | No |
| Receptor 6 | 89 | 1 | 1 | 90 | 90 | 181% | 181% | 41% | No |
| Estación Laja | 89 | 0 | 1 | 90 | 90 | 180% | 180% | 25% | No |
| Estación San<br>Rosendo | 101 | 1 | 1 | 102 | 102 | 205% | 205% | 33% | No |

**Tabla 84.: Promedio anual de la tasa de deposición del material particulado sedimentable (MPS)** **-** **Escenario 2.****

| Receptor | Aporte Proyecto tasa de deposición<br>promedio anual (mg/m2N/d) | Tasa de deposición promedio anual<br>máxima permitida Valor Norma | Porcentaje de<br>normativa (%) | Cumplimiento de la<br>normativa |
| --- | --- | --- | --- | --- |
| Receptor 1 | 0 | 200 mg/(m2*d) | 0% | Si |
| Receptor 2 | 0 | 0 | 0% | Si |
| Receptor 3 | 0 | 0 | 0% | Si |
| Receptor 4 | 0 | 0 | 0% | Si |
| Receptor 5 | 0 | 0 | 0% | Si |

**Tabla 85.: Promedio anual de la concentración de dióxido de nitrógeno (NO** **2** **)** **-** **Escenario 2.****

| Receptor | Línea base<br>promedio<br>anual<br>(μg/m3N). | Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N) | Aporte proyectos<br>con RCA (proyecto<br>1 + proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N) | Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma | Porcentaje<br>de normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 8 | 0 | 0 | 9 | 100 μg/m3N | 9% | Si |
| Receptor 2 | 8 | 1 | 0 | 9 | 9 | 9% | Si |
| Receptor 3 | 8 | 0 | 0 | 9 | 9 | 9% | Si |
| Receptor 4 | 8 | 0 | 0 | 9 | 9 | 9% | Si |
| Receptor 5 | 8 | 1 | 0 | 10 | 10 | 10% | Si |
| Receptor 6 | 8 | 1 | 0 | 9 | 9 | 9% | Si |
| Estación Laja | 8 | 0 | 0 | 9 | 9 | 9% | Si |
| Estación San Rosendo | 10 | 1 | 0 | 11 | 11 | 11% | Si |

**Tabla 86.: Percentil 99 de la concentración horaria de NO** **2** **-** **Escenario 2.****

| Receptor | Línea base<br>percentil 99<br>1 h<br>(μg/m3N). | Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 1 h (μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima permitida<br>percentil 99 de 1<br>hora Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 40 | 6 | 11 | 57 | 400 μg/m3N | 14% | Si |
| Receptor 2 | 40 | 5 | 11 | 55 | 55 | 14% | Si |
| Receptor 3 | 40 | 6 | 11 | 57 | 57 | 14% | Si |

**Tabla 87.: Promedio anual de la concentración de dióxido de azufre (SO** **2** **)** **-** **Escenario 2.****

| Receptor | Línea base<br>promedio<br>anual<br>(μg/m3N). | Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N) | Aporte proyectos<br>con RCA (proyecto<br>1 + proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N) | Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma | Porcentaje<br>de normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 1 | 0 | 0 | 1 | 60 μg/m3N | 2% | Si |
| Receptor 2 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Receptor 3 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Receptor 4 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Receptor 5 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Receptor 6 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Estación Laja | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Estación San Rosendo | 3 | 0 | 0 | 3 | 3 | 6% | Si |

**Tabla 88.: Percentil 99 de la concentración diaria de SO** **2** **-** **Escenario 2.****

| Receptor | Línea base<br>percentil 99<br>24 h<br>(μg/m3N). | Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima permitida<br>percentil 99 de 24<br>horas Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 4 | 1 | 0 | 5 | 150 μg/m3N | 4% | Si |
| Receptor 2 | 4 | 2 | 0 | 6 | 6 | 4% | Si |
| Receptor 3 | 4 | 1 | 0 | 5 | 5 | 3% | Si |
| Receptor 4 | 4 | 1 | 0 | 5 | 5 | 4% | Si |
| Receptor 5 | 4 | 2 | 0 | 6 | 6 | 4% | Si |
| Receptor 6 | 4 | 2 | 0 | 6 | 6 | 4% | Si |
| Estación Laja | 4 | 1 | 0 | 5 | 5 | 3% | Si |
| Estación San Rosendo | 7 | 1 | 0 | 8 | 8 | 5% | Si |

**Tabla 89.: Percentil 98,5 de la concentración de 1 h de SO** **2** **-** **Escenario 2.****

| Receptor | Línea base<br>percentil 98,5<br>1 h (μg/m3N). | Aporte Proyecto<br>Percentil 98,5 de la<br>concentración en<br>inmisión 1 h (μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima permitida<br>Percentil 98,5 de 1 h<br>Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 5 | 2 | 0 | 7 | 350 μg/m3N | 2% | Si |
| Receptor 2 | 5 | 3 | 0 | 8 | 8 | 2% | Si |
| Receptor 3 | 5 | 1 | 0 | 6 | 6 | 2% | Si |
| Receptor 4 | 5 | 2 | 0 | 8 | 8 | 2% | Si |
| Receptor 5 | 5 | 4 | 0 | 9 | 9 | 3% | Si |
| Receptor 6 | 5 | 3 | 0 | 8 | 8 | 2% | Si |
| Estación Laja | 5 | 2 | 0 | 7 | 7 | 2% | Si |
| Estación San Rosendo | 8 | 2 | 0 | 10 | 10 | 3% | Si |

**Tabla 90.: Percentil 99,7 de la concentración diaria de SO** **2** **-** **Escenario 2.****

| Receptor | Línea base<br>percentil 99,7<br>24 h<br>(μg/m3N). | Aporte Proyecto<br>Percentil 99,7 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima permitida<br>percentil 99,7 de 24<br>horas Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 6 | 2 | 0 | 8 | 260 μg/m3N | 3% | Si |
| Receptor 2 | 6 | 2 | 0 | 9 | 9 | 3% | Si |
| Receptor 3 | 6 | 2 | 0 | 8 | 8 | 3% | Si |
| Receptor 4 | 6 | 2 | 0 | 8 | 8 | 3% | Si |
| Receptor 5 | 6 | 3 | 0 | 9 | 9 | 3% | Si |
| Receptor 6 | 6 | 2 | 0 | 9 | 9 | 3% | Si |
| Estación Laja | 6 | 1 | 0 | 7 | 7 | 3% | Si |
| Estación San Rosendo | 9 | 2 | 0 | 11 | 11 | 4% | Si |

**Tabla 91.: Percentil 99,73 de la concentración horaria de SO** **2** **-** **Escenario 2.****

| Receptor | Línea base<br>percentil<br>99,73 1 h<br>(μg/m3N). | Aporte Proyecto<br>Percentil 99,73 de la<br>concentración en<br>inmisión 1 h (μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima permitida<br>percentil 99,73 de 1<br>hora Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 12 | 6 | 1 | 18 | 700 μg/m3N | 3% | Si |
| Receptor 2 | 12 | 6 | 1 | 18 | 18 | 3% | Si |
| Receptor 3 | 12 | 3 | 1 | 16 | 16 | 2% | Si |
| Receptor 4 | 12 | 5 | 1 | 17 | 17 | 2% | Si |
| Receptor 5 | 12 | 7 | 1 | 20 | 20 | 3% | Si |
| Receptor 6 | 12 | 7 | 1 | 19 | 19 | 3% | Si |
| Estación Laja | 12 | 3 | 1 | 16 | 16 | 2% | Si |
| Estación San Rosendo | 16 | 3 | 1 | 20 | 20 | 3% | Si |

**Tabla 92.: Percentil 99 de la concentración de 1 h de CO** **-** **Escenario 2.****

| Receptor | Línea base<br>percentil 99 1<br>h (mg/m3N). | Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 1 h<br>(mg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(mg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(mg/m3N) | Concentración<br>máxima permitida<br>percentil 99 de 1<br>hora Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 5 | 0 | 0 | 5 | 30 mg/m3N | 17% | Si |
| Receptor 2 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Receptor 3 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Receptor 4 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Receptor 5 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Receptor 6 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Estación Laja | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Estación San Rosendo | 6 | 0 | 0 | 6 | 6 | 20% | Si |

**Tabla 93.: Percentil 99 de la concentración 8 h de CO** **-** **Escenario 2.****

| Receptor | Línea base<br>percentil 99 8<br>h (mg/m3N). | Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 8 h<br>(mg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(mg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA)<br>(mg/m3N) | Concentración<br>máxima permitida<br>percentil 99 de 8<br>horas Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 3 | 0 | 0 | 3 | 10 mg/m3N | 30% | Si |
| Receptor 2 | 3 | 0 | 0 | 3 | 3 | 30% | Si |
| Receptor 3 | 3 | 0 | 0 | 3 | 3 | 30% | Si |
| Receptor 4 | 3 | 0 | 0 | 3 | 3 | 30% | Si |
| Receptor 5 | 3 | 0 | 0 | 3 | 3 | 30% | Si |
| Receptor 6 | 3 | 0 | 0 | 3 | 3 | 30% | Si |
| Estación Laja | 3 | 0 | 0 | 3 | 3 | 30% | Si |

**Tabla 94.: Concentración diaria de TRS** **-** **Escenario 2.****

| Receptor | Línea base<br>concentración 24<br>horas (μg/m3N). | Aporte Proyecto<br>concentración 24<br>horas (μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos con<br>RCA) (μg/m3N) | Concentración máxima<br>permitida Concentración<br>24 h Valor Norma | Porcentaje de<br>normativa (%) | Cumplimiento de<br>la normativa |
| --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 4 | 0 | 4 | 7 μg/m3N | 58% | Si |
| Receptor 2 | 4 | 0 | 4 | 4 | 58% | Si |
| Receptor 3 | 4 | 0 | 4 | 4 | 58% | Si |
| Receptor 4 | 4 | 0 | 4 | 4 | 58% | Si |
| Receptor 5 | 4 | 0 | 4 | 4 | 58% | Si |
| Receptor 6 | 4 | 0 | 4 | 4 | 58% | Si |
| Estación Laja | 4 | 0 | 4 | 4 | 58% | Si |
| Estación San Rosendo | 4 | 0 | 4 | 4 | 58% | Si |

**Tabla 95.: Impacto sobre la salud de las personas por la concentración horaria de TRS** **-** **Escenario 2.****

| Receptor | Línea base<br>concentración<br>1 hora<br>(μg/m3N). | Aporte<br>Proyecto<br>concentración<br>1 hora<br>(μg/m3N) | Total (línea<br>base, aporte<br>proyecto y<br>aporte<br>proyectos con<br>RCA)<br>(μg/m3N) | Concentración<br>máxima<br>permitida<br>Concentración<br>1 h Valor<br>Norma | Porcentaje de<br>normativa<br>(%) | Cumplimiento<br>de la<br>normativa | Significancia | Porcentaje<br>del valor de<br>significancia<br>(%) | Impacto<br>significativo<br>sobre la salud<br>de las<br>personas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 2 | 20 | 0 | 20 | 20 | 50% | Si | Si | -- | -- |
| Receptor 3 | 20 | 0 | 20 | 20 | 50% | Si | Si | -- | -- |
| Receptor 4 | 20 | 0 | 20 | 20 | 50% | Si | Si | -- | -- |
| Receptor 5 | 20 | 0 | 20 | 20 | 51% | Si | Si | -- | -- |
| Receptor 6 | 20 | 0 | 20 | 20 | 51% | Si | Si | -- | -- |
| Estación Laja | 20 | 0 | 20 | 20 | 50% | Si | Si | -- | -- |
| Estación San Rosendo | 61 | 0 | 61 | 61 | 153% | -- | -- | 28% | No |

**Tabla 96.: Resumen de Punto de Máximo Impacto** **-** **Escenario 2.****

| Estadístico | Año estudio mayor<br>concentración | Coordenadas UTM | Col4 | Aporte máximo del<br>proyecto | Localización (dentro o<br>fuera de planta) |
| --- | --- | --- | --- | --- | --- |
| **Estadístico** | **Año estudio mayor**<br>**concentración** | **Datum WGS 84 Huso 18** | **Datum WGS 84 Huso 18** | **Datum WGS 84 Huso 18** | **Datum WGS 84 Huso 18** |
| **Estadístico** | **Año estudio mayor**<br>**concentración** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| Promedio anual MP10 (μg/m3) | 2021 | 702.686,41 | 5.871.322,12 | 0 | Fuera del perímetro de la<br>planta |
| Percentil 98 concentración 24 horas MP10 (μg/m3) | 2020 | 702.904,58 | 5.870.494,68 | 1 | Dentro de perímetro<br>planta |
| Promedio anual MP2,5 (μg/m3) | 2021 | 702.904,58 | 5.870.494,68 | 0 | Dentro de perímetro<br>planta |
| Percentil 98 concentración 24 horas MP2,5 (μg/m3) | 2020 | 702.904,58 | 5.870.494,68 | 1 | Dentro de perímetro<br>planta |
| Promedio anual tasa de deposición MPS (mg/m2/d) | 2021 | 701.948,4 | 5872519.81 | 10 | Fuera del perímetro de la<br>planta |
| Concentración 24h de SO2, P99 (μg/m3) | 2021 | 702.686,41 | 5.871.322,12 | 2 | Fuera del perímetro de la<br>planta |
| Concentración 1h de SO2, P98,5 (μg/m3) | 2021 | 702.686,41 | 5.871.322,12 | 4 | Fuera del perímetro de la<br>planta |
| Promedio Anual SO2 (μg/m3) | 2021 | 702.686,41 | 5.871.322,12 | 0 | Fuera del perímetro de la<br>planta |
| Concentración 24h SO2, P99,7 (μg/m3) | 2021 | 702.686,41 | 5.871.322,12 | 3 | Fuera del perímetro de la<br>planta |
| Concentración 1h SO2, P99,73 (μg/m3) | 2021 | 702.686,41 | 5.871.322,12 | 7 | Fuera del perímetro de la<br>planta |
| Concentración 1h NO2, P99 (μg/m3) | 2022 | 702.904,58 | 5.870.494,68 | 49 | Dentro de perímetro<br>planta |
| Concentración NO2 (μg/m3) | 2020 | 702.904,58 | 5.870.494,68 | 3 | Dentro de perímetro<br>planta |
| Concentración 1h CO, P99 (mg/m3) | 2020 | 703.884,71 | 5.869.470,07 | 0 | Fuera del perímetro de la<br>planta |
| Concentración 8h móvil CO, P99 (mg/m3) | 2020 | 702.904,58 | 5.870.494,68 | 0 | Dentro de perímetro<br>planta |
| Concentración 24h TRS (μg/m3) | 2020 | 702.686,41 | 5.871.322,12 | 0 | Fuera del perímetro de la<br>planta |

**Tabla 97.: Cumplimiento de normativa de los estadísticos del PMI** **-** **Escenario 2.****

| Estadístico | Línea<br>base | Aporte<br>máximo del<br>proyecto | Aporte proyectos con<br>RCA (proyecto 1 +<br>proyecto 2) | Concentración<br>total | Concentración<br>máxima permitida | Porcentaje de<br>normativa (%) |
| --- | --- | --- | --- | --- | --- | --- |
| Promedio anual MP10 (μg/m3) | 29 | 0 | 1 | 30 | 50 | 61% |
| Promedio anual tasa de deposición MPS (mg/m2/d) | ND | 10 | ND | 10 | 200 | 5% |
| Concentración 24h de SO2, P99 (μg/m3) | 4 | 2 | 0 | 6 | 150 | 4% |
| Concentración 1h de SO2, P98,5 (μg/m3) | 5 | 4 | 0 | 9 | 350 | 3% |
| Promedio Anual SO2 (μg/m3) | 1 | 0 | 0 | 1 | 60 | 2% |
| Concentración 24h SO2, P99,7 (μg/m3) | 6 | 3 | 0 | 9 | 260 | 3% |
| Concentración 1h SO2, P99,73 (μg/m3) | 12 | 7 | 1 | 20 | 700 | 3% |
| Concentración 1h CO, P99 (mg/m3) | 5 | 0 | 0 | 5 | 30 | 17% |
| Concentración 24h TRS (μg/m3) | 4 | 0 | ND | 4 | 7 | 58% |
| Concentración 1h TRS (μg/m3) | 20 | 0 | ND | 20 | 40 | 51% |

**Tabla 98.: Promedio anual de la concentración de MP** **10** **-** **Escenario 3.****

| Receptor | Línea base<br>promedio<br>anual<br>(μg/m3N). | Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N) | Aporte proyectos<br>con RCA<br>(proyecto 1 +<br>proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N) | Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma | Porcentaje<br>de normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 29 | 1 | 1 | 30 | 50 μg/m3N | 61% | Si |
| Receptor 2 | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Receptor 3 | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Receptor 4 | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Receptor 5 | 29 | 1 | 1 | 31 | 31 | 62% | Si |
| Receptor 6 | 29 | 1 | 1 | 31 | 31 | 62% | Si |
| Estación Laja | 29 | 0 | 1 | 30 | 30 | 60% | Si |
| Estación San Rosendo | 36 | 0 | 1 | 37 | 37 | 74% | Si |

**Tabla 99.: Percentil 98 de la concentración diaria de MP** **10** **-** **Escenario 3.****

| Receptor | Línea base<br>percentil 98<br>24 h<br>(μg/m3N). | Aporte Proyecto<br>Percentil 98 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (μg/m3N) | Concentración<br>máxima permitida<br>percentil 98 de 24<br>horas Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 67 | 7 | 3 | 77 | 130 μg/m3N | 60% | Si |
| Receptor 2 | 67 | 1 | 3 | 71 | 71 | 55% | Si |
| Receptor 3 | 67 | 2 | 3 | 72 | 72 | 55% | Si |
| Receptor 4 | 67 | 0 | 3 | 71 | 71 | 54% | Si |
| Receptor 5 | 67 | 8 | 3 | 78 | 78 | 60% | Si |
| Receptor 6 | 67 | 14 | 3 | 84 | 84 | 64% | Si |
| Estación Laja | 67 | 0 | 3 | 70 | 70 | 54% | Si |
| Estación San Rosendo | 99 | 0 | 3 | 102 | 102 | 79% | Si |

**Tabla 100.: Impacto sobre la salud de las personas por el promedio anual de la concentración de MP** **2.5** **-** **Escenario 3.****

| Receptor | Línea base<br>promedio<br>anual<br>(μg/m3N). | Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N) | Aporte<br>proyectos<br>con RCA<br>(proyecto<br>1 +<br>proyecto<br>2)<br>(μg/m3N) | Total (línea<br>base, aporte<br>proyecto y<br>aporte<br>proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima<br>permitida<br>Promedio<br>anual Valor<br>Norma | Porcentaje<br>de<br>normativa<br>(%) | Significancia | Porcentaje<br>del valor de<br>significancia<br>(%) | Impacto<br>significativo<br>sobre la<br>salud de las<br>personas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 3 | 22 | 0 | 0 | 22 | 22 | 111% | 111% | 10% | No |
| Receptor 4 | 22 | 0 | 0 | 22 | 22 | 111% | 111% | 5% | No |
| Receptor 5 | 22 | 0 | 0 | 22 | 22 | 112% | 112% | 46% | No |
| Receptor 6 | 22 | 0 | 0 | 22 | 22 | 112% | 112% | 41% | No |
| Estación Laja | 22 | 0 | 0 | 22 | 22 | 111% | 111% | 2% | No |
| Estación San Rosendo | 26 | 0 | 0 | 26 | 26 | 131% | 131% | 1% | No |

**Tabla 101.: Impacto sobre la salud de las personas del percentil 98 de la concentración diaria de MP** **2.5** **- Escenario 3.****

| Receptor | Línea base<br>percentil<br>98 24 h<br>(μg/m3N). | Aporte<br>Proyecto<br>Percentil 98 de<br>la<br>concentración<br>en inmisión 24<br>h (μg/m3N) | Aporte<br>proyectos<br>con RCA<br>(proyecto 1<br>+ proyecto<br>2)<br>(μg/m3N) | Total (línea<br>base,<br>aporte<br>proyecto y<br>aporte<br>proyectos<br>con RCA)<br>(μg/m3N) | Concentración<br>máxima<br>permitida<br>percentil 98 de<br>24 horas Valor<br>Norma | Porcentaje<br>de<br>normativa<br>(%) | Significancia | Porcentaje<br>del valor de<br>significancia<br>(%) | Impacto<br>significativo<br>sobre la<br>salud de las<br>personas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 89 | 1 | 1 | 91 | 50 μg/m3N | 181% | 1,71<br>μg/m3N | 51% | No |
| Receptor 2 | 89 | 0 | 1 | 90 | 90 | 180% | 180% | 12% | No |
| Receptor 3 | 89 | 0 | 1 | 90 | 90 | 180% | 180% | 18% | No |
| Receptor 4 | 89 | 0 | 1 | 90 | 90 | 180% | 180% | 5% | No |
| Receptor 5 | 89 | 1 | 1 | 91 | 91 | 182% | 182% | 59% | No |
| Receptor 6 | 89 | 1 | 1 | 91 | 91 | 183% | 183% | 87% | No |
| Estación Laja | 89 | 0 | 1 | 90 | 90 | 180% | 180% | 2% | No |
| Estación San Rosendo | 101 | 0 | 1 | 102 | 102 | 204% | 204% | 1% | No |

**Tabla 102.: Promedio anual de la tasa de deposición del material particulado sedimentable (MPS)** **-** **Escenario 3.****

| Receptor | Aporte Proyecto tasa de deposición<br>promedio anual (mg/m2N/d) | Tasa de deposición promedio anual<br>máxima permitida Valor Norma | Porcentaje de<br>normativa (%) | Cumplimiento de la<br>normativa |
| --- | --- | --- | --- | --- |
| Receptor 1 | 0 | 200 mg/(m2*d) | 0% | Si |
| Receptor 2 | 0 | 0 | 0% | Si |
| Receptor 3 | 0 | 0 | 0% | Si |
| Receptor 4 | 0 | 0 | 0% | Si |
| Receptor 5 | 0 | 0 | 0% | Si |
| Receptor 6 | 0 | 0 | 0% | Si |
| Estación Laja | 0 | 0 | 0% | Si |
| Estación San Rosendo | 0 | 0 | 0% | Si |

**Tabla 103.: Promedio anual de la concentración de dióxido de nitrógeno (NO** **2** **)** **-** **Escenario 3.****

| Receptor | Línea base<br>promedio<br>anual<br>(μg/m3N). | Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N) | Aporte proyectos<br>con RCA<br>(proyecto 1 +<br>proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N) | Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma | Porcentaje<br>de normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 3 | 8 | 0 | 0 | 9 | 9 | 9% | Si |
| Receptor 4 | 8 | 0 | 0 | 9 | 9 | 9% | Si |
| Receptor 5 | 8 | 1 | 0 | 9 | 9 | 9% | Si |
| Receptor 6 | 8 | 1 | 0 | 9 | 9 | 9% | Si |
| Estación Laja | 8 | 0 | 0 | 9 | 9 | 9% | Si |
| Estación San Rosendo | 10 | 0 | 0 | 11 | 11 | 11% | Si |

**Tabla 104.: Percentil 99 de la concentración horaria de NO** **2** **-** **Escenario 3.****

| Receptor | Línea base<br>percentil 99<br>1 h<br>(μg/m3N). | Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 1 h<br>(μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (μg/m3N) | Concentración<br>máxima permitida<br>percentil 99 de 1<br>hora Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 40 | 11 | 11 | 61 | 400 μg/m3N | 15% | Si |
| Receptor 2 | 40 | 3 | 11 | 54 | 54 | 13% | Si |
| Receptor 3 | 40 | 6 | 11 | 57 | 57 | 14% | Si |
| Receptor 4 | 40 | 2 | 11 | 52 | 52 | 13% | Si |
| Receptor 5 | 40 | 8 | 11 | 59 | 59 | 15% | Si |
| Receptor 6 | 40 | 13 | 11 | 63 | 63 | 16% | Si |
| Estación Laja | 40 | 1 | 11 | 51 | 51 | 13% | Si |
| Estación San Rosendo | 37 | 1 | 11 | 48 | 48 | 12% | Si |

**Tabla 105.: Promedio anual de la concentración de dióxido de azufre (SO** **2** **)** **-** **Escenario 3.****

| Receptor | Línea base<br>promedio<br>anual<br>(μg/m3N). | Aporte<br>Proyecto<br>promedio<br>anual<br>(μg/m3N) | Aporte proyectos<br>con RCA<br>(proyecto 1 +<br>proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto y<br>aporte proyectos<br>con RCA) (μg/m3N) | Concentración<br>máxima permitida<br>Promedio anual Valor<br>Norma | Porcentaje<br>de normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 1 | 0 | 0 | 1 | 60 μg/m3N | 2% | Si |
| Receptor 2 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Receptor 3 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Receptor 4 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Receptor 5 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Receptor 6 | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Estación Laja | 1 | 0 | 0 | 1 | 1 | 2% | Si |
| Estación San Rosendo | 3 | 0 | 0 | 3 | 3 | 5% | Si |

**Tabla 106.: Percentil 99 de la concentración diaria de SO** **2** **-** **Escenario 3.****

| Receptor | Línea base<br>percentil 99<br>24 h<br>(μg/m3N). | Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (μg/m3N) | Concentración<br>máxima permitida<br>percentil 99 de 24<br>horas Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 4 | 0 | 0 | 4 | 150 μg/m3N | 3% | Si |
| Receptor 2 | 4 | 0 | 0 | 4 | 4 | 3% | Si |
| Receptor 3 | 4 | 0 | 0 | 4 | 4 | 3% | Si |
| Receptor 4 | 4 | 0 | 0 | 4 | 4 | 3% | Si |
| Receptor 5 | 4 | 0 | 0 | 4 | 4 | 3% | Si |

**Tabla 107.: Percentil 98,5 de la concentración de 1 h de SO** **2** **-** **Escenario 3.****

| Receptor | Línea base<br>percentil<br>98,5 1 h<br>(μg/m3N). | Aporte Proyecto<br>Percentil 98,5 de la<br>concentración en<br>inmisión 1 h<br>(μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (μg/m3N) | Concentración<br>máxima permitida<br>Percentil 98,5 de 1 h<br>Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 5 | 0 | 0 | 5 | 350 μg/m3N | 2% | Si |
| Receptor 2 | 5 | 0 | 0 | 5 | 5 | 2% | Si |
| Receptor 3 | 5 | 0 | 0 | 5 | 5 | 2% | Si |
| Receptor 4 | 5 | 0 | 0 | 5 | 5 | 2% | Si |
| Receptor 5 | 5 | 0 | 0 | 5 | 5 | 2% | Si |
| Receptor 6 | 5 | 0 | 0 | 5 | 5 | 2% | Si |
| Estación Laja | 5 | 0 | 0 | 5 | 5 | 2% | Si |
| Estación San Rosendo | 8 | 0 | 0 | 8 | 8 | 2% | Si |

**Tabla 108.: Percentil 99,7 de la concentración diaria de SO** **2** **-** **Escenario 3.****

| Receptor | Línea base<br>percentil<br>99,7 24 h<br>(μg/m3N). | Aporte Proyecto<br>Percentil 99,7 de la<br>concentración en<br>inmisión 24 h<br>(μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (μg/m3N) | Concentración<br>máxima permitida<br>percentil 99,7 de 24<br>horas Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 6 | 0 | 0 | 6 | 260 μg/m3N | 2% | Si |
| Receptor 2 | 6 | 0 | 0 | 6 | 6 | 2% | Si |
| Receptor 3 | 6 | 0 | 0 | 6 | 6 | 2% | Si |
| Receptor 4 | 6 | 0 | 0 | 6 | 6 | 2% | Si |
| Receptor 5 | 6 | 0 | 0 | 6 | 6 | 2% | Si |
| Receptor 6 | 6 | 0 | 0 | 6 | 6 | 2% | Si |
| Estación Laja | 6 | 0 | 0 | 6 | 6 | 2% | Si |
| Estación San Rosendo | 9 | 0 | 0 | 9 | 9 | 4% | Si |

**Tabla 109.: Percentil 99,73 de la concentración horaria de SO** **2** **-** **Escenario 3.****

| Receptor | Línea base<br>percentil<br>99,73 1 h<br>(μg/m3N). | Aporte Proyecto<br>Percentil 99,73 de la<br>concentración en<br>inmisión 1 h<br>(μg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(μg/m3N) | Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (μg/m3N) | Concentración<br>máxima permitida<br>percentil 99,73 de 1<br>hora Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 12 | 0 | 1 | 13 | 700 μg/m3N | 2% | Si |
| Receptor 2 | 12 | 0 | 1 | 13 | 13 | 2% | Si |
| Receptor 3 | 12 | 0 | 1 | 13 | 13 | 2% | Si |
| Receptor 4 | 12 | 0 | 1 | 13 | 13 | 2% | Si |
| Receptor 5 | 12 | 0 | 1 | 13 | 13 | 2% | Si |
| Receptor 6 | 12 | 0 | 1 | 13 | 13 | 2% | Si |
| Estación Laja | 12 | 0 | 1 | 13 | 13 | 2% | Si |
| Estación San Rosendo | 16 | 0 | 1 | 17 | 17 | 2% | Si |

**Tabla 110.: Percentil 99 de la concentración de 1 h de CO** **-** **Escenario 3.****

| Receptor | Línea base<br>percentil 99 1<br>h (mg/m3N). | Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 1 h<br>(mg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(mg/m3N) | Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (mg/m3N) | Concentración<br>máxima permitida<br>percentil 99 de 1<br>hora Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 5 | 0 | 0 | 5 | 30 mg/m3N | 17% | Si |
| Receptor 2 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Receptor 3 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Receptor 4 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Receptor 5 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Receptor 6 | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Estación Laja | 5 | 0 | 0 | 5 | 5 | 17% | Si |
| Estación San Rosendo | 6 | 0 | 0 | 6 | 6 | 20% | Si |

**Tabla 111.: Percentil 99 de la concentración 8 h de CO** **-** **Escenario 3.****

| Receptor | Línea base<br>percentil 99 8<br>h (mg/m3N). | Aporte Proyecto<br>Percentil 99 de la<br>concentración en<br>inmisión 8 h<br>(mg/m3N) | Aporte<br>proyectos con<br>RCA (proyecto 1<br>+ proyecto 2)<br>(mg/m3N) | Total (línea base,<br>aporte proyecto<br>y aporte<br>proyectos con<br>RCA) (mg/m3N) | Concentración<br>máxima permitida<br>percentil 99 de 8<br>horas Valor Norma | Porcentaje<br>de<br>normativa<br>(%) | Cumplimiento<br>de la normativa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor 1 | 3 | 0 | 0 | 3 | 10 mg/m3N | 30% | Si |
| Receptor 2 | 3 | 0 | 0 | 3 | 3 | 30% | Si |
| Receptor 3 | 3 | 0 | 0 | 3 | 3 | 30% | Si |
| Receptor 4 | 3 | 0 | 0 | 3 | 3 | 30% | Si |

**Tabla 112.: Resumen de Punto de Máximo Impacto** **-** **Escenario 3.****

| Estadístico | Año estudio mayor<br>concentración ambiental | Coordenadas UTM | Col4 | Aporte máximo<br>del proyecto | Localización (dentro o<br>fuera de planta) |
| --- | --- | --- | --- | --- | --- |
| **Estadístico** | **Año estudio mayor**<br>**concentración ambiental** | **Datum WGS 84 Huso 18** | **Datum WGS 84 Huso 18** | **Datum WGS 84 Huso 18** | **Datum WGS 84 Huso 18** |
| **Estadístico** | **Año estudio mayor**<br>**concentración ambiental** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| Promedio anual MP10 (μg/m3) | 2022 | 702.904,49 | 5.870.494,79 | 71 | Dentro de perímetro<br>planta |
| Percentil 98 concentración 24 horas MP10 (μg/m3) | 2021 | 702.904,49 | 5.870.494,79 | 338 | Dentro de perímetro<br>planta |
| Promedio anual MP2,5 (μg/m3) | 2020 | 702.904,49 | 5.870.494,79 | 8 | Dentro de perímetro<br>planta |
| Percentil 98 concentración 24 horas MP2,5 (μg/m3) | 2021 | 702.904,49 | 5.870.494,79 | 35 | Dentro de perímetro<br>planta |
| Promedio anual tasa de deposición MPS (mg/m2/d) | 2022 | 702.904,49 | 5.870.494,79 | 5759 | Dentro de perímetro<br>planta |
| Concentración 24h de SO2, P99 (μg/m3) | 2021 | 702.904,49 | 5.870.494,79 | 0 | Dentro de perímetro<br>planta |

**Tabla 113.: Lista de anexos.****

| N° anexo | Nombre de archivo | Descripción/comentarios |
| --- | --- | --- |
| Anexo 1 | Metodología de cálculo rev0 | Metodología de cálculo de tasas de emisión modeladas. |
| Anexo 2 | Archivos kml | Archivos de geolocalización. |
| Anexo 3 | Cartografía HQ | Imágenes de cartografía en alta calidad. |
| Anexo 4 | Norma de Colombia | Norma para TRS en inmisión. |
| Anexo 5 | Norma Suiza | Norma de MPS. |
| Anexo 6 | Archivos de modelación | Archivos de Calpuff y Calpost. |
| Anexo 7 | Archivos meteorología | Archivo meteorológico. 2020- |
| Anexo 7 | Archivos meteorología | Archivo txt file. 2020. |
| Anexo 7 | Archivos meteorología | Archivo meteorológico. 2021. |
| Anexo 7 | Archivos meteorología | Archivo txt file. 2021. |
| Anexo 7 | Archivos meteorología | Archivo meteorológico. 2022. |
| Anexo 7 | Archivos meteorología | Archivo txt file. 2022. |
| Anexo 8 | Archivo GRD | Archivo grd con alturas de la grilla. |
| Anexo 9 | Parametrizaciones WRF | Documento que contiene las parametrizaciones de los archivos<br>WRF. |
| Anexo 10 | Archivos namelist | Archivo namelist.input y archive namelist.wsp |

**Tabla 114.: Datos de fuentes puntuales.****

| Item | Caldera recuperadora | Caldera biomasa | Horno de cal |
| --- | --- | --- | --- |
| Velocidad de emisión (m/s) | 20,6 | 25,3 | 11 |
| Temperatura de emisión (K) | 428,15 | 417,15 | 534,15 |
| Diámetro de la chimenea (m) | 3,6 | 2,25 | 1,6 |

**Tabla 115.: Tasa de emisión de TRS en RCA 2009,** **para producción de 500.000 ton/año.****

| Item | Caldera recuperadora | Caldera biomasa | Horno de cal |
| --- | --- | --- | --- |
| Producción TRS (ton/día) | 0,03 | 0,01 | 0,01 |

**Tabla 116.: Resumen de emisión de TRS con datos CEMS y RCA 2009.****

| Equipo | Producción TRS datos CEMS (ton/año) | Col3 | Col4 | Producción TRS datos RCA (ton/año) | Col6 | Col7 | Razón<br>incremento<br>producción<br>Datos RCA<br>con CEMS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Equipo** | **Producción**<br>**planta**<br>**360.000**<br>**ton/año** | **Producción**<br>**planta**<br>**400.000**<br>**ton/año** | **Incremento**<br>**producción**<br>**(40.000**<br>**ton/año)** | **Producción**<br>**planta**<br>**360.000**<br>**ton/año** | **Producción**<br>**planta**<br>**400.000**<br>**ton/año** | **Incremento**<br>**producción**<br>**(40.000**<br>**ton/año)** | **Incremento**<br>**producción**<br>**(40.000**<br>**ton/año)** |
| Caldera<br>recuperadora | 3,16 | 3,51 | 0,35 | 7,88 | 8,76 | 0,88 | 2,5 |
| Caldera<br>biomasa | 0,75 | 0,83 | 0,08 | 2,63 | 2,92 | 0,29 | 3,65 |
| Horno de cal | 1,42 | 1,58 | 0,16 | 2,63 | 2,92 | 0,29 | 1,83 |

**Tabla 117.: Análisis de proximidad de estaciones meteorológicas superficiales dentro del dominio.****

| Nombre<br>estación | Base de<br>datos | Distancia al perímetro<br>del proyecto (km) | Coordenadas UTM<br>Datum WGS 84 Huso<br>18 | Col5 | Variables meteorológicas disponibles<br>para periodo 2020 al 2022 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Nombre**<br>**estación** | **Base de**<br>**datos** | **Distancia al perímetro**<br>**del proyecto (km)** | **Este (m)** | **Norte (m)** | **T1 ** | **VV1 ** | **DV1 ** | **Hr1 ** |
| **María**<br>**Dolores2 ** | DMC | 26,5 | 728.035 | 5.857.977 | X | X | X | X |
| **La colonia3 ** | INIA | 9,8 | 713.484 | 5.870.414 | X | X | X | X |
| **Laja** | SINCA | 1,83 | 702.992 | 5.872.963 | √ | √ | √ | √ |
| **Club**<br>**de**<br>**empleados** | **Club**<br>**de**<br>**empleados** | 21,7 | 705.393 | 5.846.899 | √ | √ | √ | √ |
| **Lautaro** | **Lautaro** | 22,7 | 736.622 | 5.850.392 | √ | √ | √ | √ |
| **21 de mayo** | **21 de mayo** | 36,24 | 733.331 | 5.849.585 | √ | √ | √ | √ |
| **Los**<br>**ángeles**<br>**oriente** | **Los**<br>**ángeles**<br>**oriente** | 37,6 | 736.622 | 5.850.392 | √ | √ | √ | √ |
| **Hualqui** | **Hualqui** | 39,17 | 684.073 | 5.905.626 | √ | √ | √ | √ |

**Tabla 118.: Datos de la estación meteorológica superficial seleccionada.****

| Nombre<br>estación | Distancia<br>al<br>perímetro<br>del<br>proyecto<br>(km) | Altura<br>m.s.n.m<br>(m)2 | Coordenadas UTM<br>Datum WGS 84 Huso<br>18 | Col5 | Variables meteorológicas1 | Col7 | Col8 | Col9 | % datos disponibles4 | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Nombre**<br>**estación** | **Distancia**<br>**al**<br>**perímetro**<br>**del**<br>**proyecto**<br>**(km)** | **Altura**<br>**m.s.n.m**<br>**(m)2 ** | **Este (m)** | **Norte (m)** | **T3 ** | **VV3 ** | **DV3 ** | **Hr3 ** | **Hr3 ** | **Hr3 ** | **Hr3 ** |
| **Nombre**<br>**estación** | **Distancia**<br>**al**<br>**perímetro**<br>**del**<br>**proyecto**<br>**(km)** | **Altura**<br>**m.s.n.m**<br>**(m)2 ** | **Este (m)** | **Norte (m)** | **T3 ** | **VV3 ** | **DV3 ** | **Hr3 ** | **2020** | **2021** | **2022** |
| **Laja** | 1,83 | 68,33 | 702.992 | 5.872.963 | √ | √ | √ | √ | 96% | 97,1% | 95,3% |

**Tabla 119.: Criterios estadísticos de aceptación de la predicción proporcionada para un modelo****

| Variable Meteorológica | Criterio de validez según parámetro estadístico | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Variable Meteorológica** | **RMSE** | **MAE** | **BIAS** | **r ** |
| **Temperatura Superficial** | ≤ 4,5 °C | ≤ 4 °C | ≤ ± 4°C | ≥ 0,8 |
| **Velocidad Viento** | ≤ 3,5 m/s | ≤ 3 m/s | ≤ ± 2,5 m/s | ≥ 0,6 |

**Tabla 120.: Valores de los índices de la predicción proporcionada por el modelo para la estación****

| Variable Meteorológica | Criterio de validez según parámetro estadístico | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Variable Meteorológica** | **RMSE** | **MAE** | **BIAS** | **r** |
| **Temperatura Superficial** | 4,9 °C | 4,0 °C | -3,7 °C | 0,9 |
| **Velocidad Viento** | 1,5 m/s | 1,1 m/s | 0,9 m/s | 0,6 |

**Tabla 121.: Valores de los índices de la predicción proporcionada por el modelo para la estación****

| Variable Meteorológica | Criterio de validez según parámetro estadístico | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Variable Meteorológica** | **RMSE** | **MAE** | **BIAS** | **r** |
| **Temperatura Superficial** | 4,1 °C | 3,1°C | -2,1°C | 0,9 |
| **Velocidad Viento** | 1,7 m/s | 1,3 m/s | 1,1 m/s | 0,6 |

**Tabla 122.: Valores de los índices de la predicción proporcionada por el modelo para la estación****

| Variable Meteorológica | Criterio de validez según parámetro estadístico | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Variable Meteorológica** | **RMSE** | **MAE** | **BIAS** | **r ** |
| **Temperatura Superficial** | 2,9 °C | 2,3°C | -0,4°C | 0,9 |
| **Velocidad Viento** | 1,5 m/s | 1,1 m/s | 0,8 m/s | 0,6 |

**Tabla 123.: Listado proyectos aprobados.****

| Nombre proyecto | Tipo | Titular | Fecha presentación/ingreso | Cercanía al proyecto |
| --- | --- | --- | --- | --- |
| Proyecto inmobiliario Los Molinos | DIA | MAESTRA QUILPUE DOS SPA | 31-08-2022 | No |
| Proyecto Pintor Pedro Luna | DIA | CONAVICOOP | 11-08-2022 | No |
| Conjunto Habitacional Cipreses de Torreones III | DIA | Inmobiliaria Villa Pacifico SpA | 05-05-2022 | No |
| Extracción de Áridos Sector Avaria | DIA | Sociedad Concesionaria Ruta Nahuelbuta S.A. | 14-03-2022 | No |
| Proyecto extracción de arena de pozo lastrero, fundo<br>Santa Gregoria | DIA | José Arner Ríos Rodríguez | 24-02-2022 | No |
| AMPLIACIÓN DEL CONJUNTO HABITACIONAL SAN<br>PEDRO | DIA | Inmobiliaria Socovesa Sur S.A. | 22-02-2022 | No |
| Extracción de Áridos Pozo Gallegos | DIA | Sociedad Concesionaria Ruta Nahuelbuta S.A. | 03-02-2022 | No |
| Incremento de la Autonomía Operacional para<br>Peróxido de Hidrógeno | DIA | Celulosa Arauco y Constitución S.A.. | 31-01-2022 | No |
| Viento Norte | DIA | Inmobiliaria Costa Norte SpA | 23-12-2021 | No |
| Regularización Plantel Lechero y Engorda Fundo Los<br>Varones - Agropecuaria Los Varones Limitada. | DIA | Agropecuaria Los Varones Ltda. | 19-11-2021 | No |
| Instalación de estanque de almacenamiento de Gas<br>Licuado | DIA | Operaciones Costeras SpA | 08-11-2021 | No |
| Ampliación en S/E El Avellano | DIA | Compañía General de Electricidad S.A. | 22-10-2021 | No |
| Planta de Producción de Pellet de Madera | DIA | Eléctrica Nueva Energía S.A. | 22-09-2021 | No |
| Paillihue Solar | DIA | Villa Prat II Energy SpA | 21-09-2021 | No |
| Modificación Condominio Alto Mirador | DIA | Constructora PACAL S.A | 16-09-2021 | No |
| Parque Fotovoltaico El Rosal | DIA | MVC SOLAR 12 SpA | 23-08-2021 | No |
| Nueva Conexión y Ampliación S/E Celulosa Laja | DIA | CMPC PULP SpA | 20-08-2021 | Sí |
| Parque Fotovoltaico Doña Ximena | DIA | MVC SOLAR 35 SpA | 23-07-2021 | No |
| Extracción de Áridos desde el Río Biobío en San<br>Pedro de la Paz | DIA | INGENIERIA, MAQUINARIAS Y CONSTRUCCIONES INGEMAC<br>LIMITADA | 12-07-2021 | No |
| Jardines de Avellaneda II | DIA | Inmobiliaria Espacio Pacifico S.A. | 06-07-2021 | No |
| Ampliación Líneas de Transferencia de Productos | DIA | OXIQUIM S.A. | 22-06-2021 | No |
| Condominio Enrique Tirapegui | DIA | CONAVICOOP | 14-06-2021 | No |
| Extracción de Áridos en el kilómetro 21 de la Ruta<br>160, Parque Industrial Uno, Escuadrón, Coronel | DIA | Extraccion y Comercializacion de Aridos Lleu-Lleu Limitada | 25-05-2021 | No |
| Parque Solar Gamma | DIA | Parque Solar Gamma SpA | 24-05-2021 | No |
| Subestación La Señoraza 220/66 kV | DIA | SOCIEDAD AUSTRAL DE TRANSMISION TRONCAL S.A. | 20-05-2021 | Sí |

**Tabla 124.: Promedio anual de la concentración de MP** **10** **-** **Escenario 1.****

| Receptor | Aporte Proyecto promedio anual<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto promedio anual<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 125.: Percentil 98 de la concentración diaria de MP** **10** **-** **Escenario 1.****

| Receptor | Aporte Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 1 | 1 | 1 | 1 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 1 | 0 | 1 |
| Receptor 5 | 1 | 1 | 1 | 1 |
| Receptor 6 | 1 | 1 | 1 | 1 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 1 | 1 | 1 | 1 |

**Tabla 126.: Promedio anual de la concentración de MP** **2.5** **-** **Escenario 1.****

| Receptor | Aporte Proyecto promedio anual<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto promedio anual<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 127.: Percentil 98 de la concentración diaria de MP** **2.5** **-** **Escenario 1.****

| Receptor | Aporte Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 1 | 1 | 1 | 1 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 1 | 0 | 1 |
| Receptor 5 | 1 | 1 | 1 | 1 |
| Receptor 6 | 1 | 1 | 1 | 1 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 1 | 1 | 0 | 1 |

**Tabla 128.: Promedio anual de la tasa de deposición del material particulado sedimentable (MPS)****

| Receptor | Aporte Proyecto tasa de deposición promedio<br>anual (mg/m2N/d) | Col3 | Col4 | Aporte máximo Proyecto tasa de deposición<br>promedio anual (mg/m2N/d) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 129.: Promedio anual de la concentración de dióxido de nitrógeno (NO** **2** **)** **-** **Escenario 1.****

| Receptor | Aporte Proyecto promedio anual<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto promedio anual<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 1 | 1 | 1 | 1 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 1 | 1 | 1 | 1 |
| Receptor 6 | 1 | 1 | 1 | 1 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 130.: Percentil 99 de la concentración horaria de NO** **2** **-** **Escenario 1.****

| Receptor | Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 7 | 6 | 7 | 7 |
| Receptor 2 | 4 | 5 | 4 | 5 |
| Receptor 3 | 5 | 5 | 6 | 6 |
| Receptor 4 | 3 | 4 | 3 | 4 |
| Receptor 5 | 7 | 7 | 7 | 7 |
| Receptor 6 | 9 | 9 | 11 | 11 |
| Estación Laja | 2 | 2 | 2 | 2 |
| Estación San<br>Rosendo | 3 | 3 | 3 | 3 |

**Tabla 131.: Promedio anual de la concentración de dióxido de azufre (SO** **2** **)** **-** **Escenario 1.****

| Receptor | Aporte Proyecto promedio anual<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto promedio anual<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 132.: Percentil 99 de la concentración diaria de SO** **2** **-** **Escenario 1.****

| Receptor | Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 24 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 24 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 1 | 1 | 1 |
| Receptor 2 | 1 | 2 | 1 | 2 |
| Receptor 3 | 0 | 1 | 0 | 1 |
| Receptor 4 | 1 | 1 | 1 | 1 |
| Receptor 5 | 2 | 2 | 1 | 2 |
| Receptor 6 | 1 | 2 | 1 | 2 |
| Estación Laja | 1 | 1 | 1 | 1 |
| Estación San<br>Rosendo | 1 | 1 | 1 | 1 |

**Tabla 133.: Percentil 98,5 de la concentración de 1 h de SO** **2** **-** **Escenario 1.****

| Receptor | Aporte Proyecto Percentil 98,5 de la<br>concentración en inmisión 1 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 98,5 de la<br>concentración en inmisión 1 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 1 | 1 | 1 | 1 |
| Receptor 2 | 2 | 3 | 2 | 3 |
| Receptor 3 | 1 | 1 | 1 | 1 |
| Receptor 4 | 2 | 2 | 2 | 2 |
| Receptor 5 | 3 | 3 | 3 | 3 |
| Receptor 6 | 2 | 3 | 2 | 3 |
| Estación Laja | 1 | 1 | 1 | 1 |
| Estación San<br>Rosendo | 2 | 2 | 2 | 2 |

**Tabla 134.: Percentil 99,7 de la concentración diaria de SO** **2** **-** **Escenario 1.****

| Receptor | Aporte Proyecto Percentil 99,7 de la<br>concentración en inmisión 24 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99,7 de la<br>concentración en inmisión 24 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 1 | 2 | 1 | 2 |
| Receptor 2 | 2 | 2 | 1 | 2 |
| Receptor 3 | 1 | 2 | 0 | 2 |
| Receptor 4 | 1 | 2 | 1 | 2 |
| Receptor 5 | 2 | 3 | 2 | 3 |
| Receptor 6 | 2 | 2 | 2 | 2 |
| Estación<br>Laja | 1 | 1 | 1 | 1 |
| Estación San<br>Rosendo | 2 | 1 | 1 | 2 |

**Tabla 135.: Percentil 99,73 de la concentración horaria de SO** **2** **-** **Escenario 1.****

| Receptor | Aporte Proyecto Percentil 99,73 de la<br>concentración en inmisión 1 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99,73 de la<br>concentración en inmisión 1 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 3 | 5 | 3 | 5 |
| Receptor 2 | 5 | 6 | 5 | 6 |
| Receptor 3 | 2 | 3 | 2 | 3 |
| Receptor 4 | 4 | 4 | 4 | 4 |
| Receptor 5 | 5 | 7 | 6 | 7 |
| Receptor 6 | 4 | 7 | 5 | 7 |
| Estación<br>Laja | 2 | 3 | 3 | 3 |
| Estación San<br>Rosendo | 3 | 3 | 2 | 3 |

**Tabla 136.: Percentil 99 de la concentración de 1 h de CO** **-** **Escenario 1.****

| Receptor | Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (mg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (mg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 137.: Percentil 99 de la concentración 8 h de CO** **-** **Escenario 1.****

| Receptor | Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 8 h (mg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 8 h (mg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 138.: Concentración diaria de TRS** **-** **Escenario 1.****

| Receptor | Aporte Proyecto Concentración diaria<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto concentración diaria<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |

**Tabla 139.: Concentración horaria de TRS** **-** **Escenario 1.****

| Receptor | Aporte Proyecto concentración horaria<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto concentración horaria<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 140.: Promedio anual de la concentración de MP** **10** **-** **Escenario 2.****

| Receptor | Aporte Proyecto promedio anual<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto promedio anual<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 141.: Percentil 98 de la concentración diaria de MP** **10** **-** **Escenario 2.****

| Receptor | Aporte Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 1 | 1 | 1 | 1 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 1 | 1 | 1 |
| Receptor 5 | 1 | 1 | 1 | 1 |
| Receptor 6 | 1 | 1 | 1 | 1 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 1 | 1 | 1 | 1 |

**Tabla 142.: Promedio anual de la concentración de MP** **2.5** **-** **Escenario 2.****

| Receptor | Aporte Proyecto promedio anual<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto promedio anual<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |

**Tabla 143.: Percentil 98 de la concentración diaria de MP** **2.5** **-** **Escenario 2.****

| Receptor | Aporte Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 1 | 1 | 1 | 1 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 1 | 0 | 1 |
| Receptor 5 | 1 | 1 | 1 | 1 |
| Receptor 6 | 1 | 1 | 1 | 1 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 1 | 1 | 0 | 1 |

**Tabla 144.: Promedio anual de la tasa de deposición del material particulado sedimentable (MPS)****

| Receptor | Aporte Proyecto tasa de deposición promedio<br>anual (mg/m2N/d) | Col3 | Col4 | Aporte máximo Proyecto tasa de deposición<br>promedio anual (mg/m2N/d) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 145.: Promedio anual de la concentración de dióxido de nitrógeno (NO** **2** **)** **-** **Escenario 2.****

| Receptor | Aporte Proyecto promedio anual<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto promedio anual<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 1 | 1 | 1 | 1 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 1 | 1 | 1 | 1 |
| Receptor 6 | 1 | 1 | 1 | 1 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 1 | 0 | 1 |

**Tabla 146.: Percentil 99 de la concentración horaria de NO** **2** **-** **Escenario 2.****

| Receptor | Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 6 | 6 | 6 | 6 |
| Receptor 2 | 4 | 5 | 4 | 5 |
| Receptor 3 | 5 | 5 | 6 | 6 |
| Receptor 4 | 3 | 4 | 4 | 4 |
| Receptor 5 | 7 | 7 | 7 | 7 |
| Receptor 6 | 8 | 10 | 10 | 10 |
| Estación Laja | 2 | 3 | 3 | 3 |
| Estación San<br>Rosendo | 3 | 3 | 3 | 3 |

**Tabla 147.: Promedio anual de la concentración de dióxido de azufre (SO** **2** **)** **-** **Escenario 2.****

| Receptor | Aporte Proyecto promedio anual<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto promedio anual<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 148.: Percentil 99 de la concentración diaria de SO** **2** **-** **Escenario 2.****

| Receptor | Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 24 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 24 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 1 | 1 | 1 | 1 |
| Receptor 2 | 1 | 2 | 1 | 2 |
| Receptor 3 | 0 | 1 | 0 | 1 |
| Receptor 4 | 1 | 1 | 1 | 1 |
| Receptor 5 | 2 | 2 | 1 | 2 |
| Receptor 6 | 1 | 2 | 1 | 2 |
| Estación Laja | 1 | 1 | 1 | 1 |
| Estación San<br>Rosendo | 1 | 1 | 1 | 1 |

**Tabla 149.: Percentil 98,5 de la concentración de 1 h de SO** **2** **-** **Escenario 2.****

| Receptor | Aporte Proyecto Percentil 98,5 de la<br>concentración en inmisión 1 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 98,5 de la<br>concentración en inmisión 1 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 1 | 2 | 1 | 2 |
| Receptor 2 | 3 | 3 | 3 | 3 |
| Receptor 3 | 1 | 1 | 1 | 1 |
| Receptor 4 | 2 | 2 | 2 | 2 |
| Receptor 5 | 3 | 4 | 3 | 4 |
| Receptor 6 | 2 | 3 | 3 | 3 |
| Estación Laja | 1 | 2 | 2 | 2 |
| Estación San<br>Rosendo | 2 | 2 | 2 | 2 |

**Tabla 150.: Percentil 99,7 de la concentración diaria de SO** **2** **-** **Escenario 2.****

| Receptor | Aporte Proyecto Percentil 99,7 de la<br>concentración en inmisión 24 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99,7 de la<br>concentración en inmisión 24 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 1 | 2 | 1 | 2 |
| Receptor 2 | 2 | 2 | 1 | 2 |
| Receptor 3 | 1 | 2 | 1 | 2 |
| Receptor 4 | 1 | 2 | 1 | 2 |
| Receptor 5 | 2 | 3 | 2 | 3 |
| Receptor 6 | 2 | 2 | 2 | 2 |
| Estación<br>Laja | 1 | 1 | 1 | 1 |
| Estación San<br>Rosendo | 2 | 1 | 1 | 2 |

**Tabla 151.: Percentil 99,73 de la concentración horaria de SO** **2** **-** **Escenario 2.****

| Receptor | Aporte Proyecto Percentil 99,73 de la<br>concentración en inmisión 1 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99,73 de la<br>concentración en inmisión 1 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 4 | 6 | 5 | 6 |
| Receptor 2 | 5 | 6 | 5 | 6 |
| Receptor 3 | 3 | 3 | 3 | 3 |
| Receptor 4 | 4 | 5 | 5 | 5 |
| Receptor 5 | 6 | 7 | 6 | 7 |
| Receptor 6 | 5 | 7 | 5 | 7 |
| Estación<br>Laja | 3 | 3 | 3 | 3 |
| Estación San<br>Rosendo | 3 | 3 | 3 | 3 |

**Tabla 152.: Percentil 99 de la concentración de 1 h de CO** **-** **Escenario 2.****

| Receptor | Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (mg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (mg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 153.: Percentil 99 de la concentración 8 h de CO** **-** **Escenario 2.****

| Receptor | Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 8 h (mg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 8 h (mg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 154.: Concentración diaria de TRS** **-** **Escenario 2.****

| Receptor | Aporte Proyecto Concentración diaria<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto concentración diaria<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 155.: Concentración horaria TRS** **-** **Escenario 2.****

| Receptor | Aporte Proyecto concentración horaria<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto concentración horaria<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 156.: Promedio anual de la concentración de MP** **10** **-** **Escenario 3.****

| Receptor | Aporte Proyecto promedio anual<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto promedio anual<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 1 | 1 | 1 | 1 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 1 | 1 | 1 | 1 |
| Receptor 6 | 1 | 1 | 1 | 1 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 157.: Percentil 98 de la concentración diaria de MP** **10** **-** **Escenario 3.****

| Receptor | Aporte Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 7 | 7 | 7 | 7 |
| Receptor 2 | 1 | 1 | 1 | 1 |
| Receptor 3 | 2 | 1 | 1 | 2 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 8 | 7 | 8 | 8 |
| Receptor 6 | 10 | 9 | 14 | 14 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 158.: Promedio anual de la concentración de MP** **2.5** **-** **Escenario 3.****

| Receptor | Aporte Proyecto promedio anual<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto promedio anual<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 159.: Percentil 98 de la concentración diaria de MP** **2.5** **-** **Escenario 3.****

| Receptor | Aporte Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 98 de la<br>concentración en inmisión 24 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 1 | 1 | 1 | 1 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 1 | 1 | 1 | 1 |
| Receptor 6 | 1 | 1 | 1 | 1 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 160.: Promedio anual de la tasa de deposición del material particulado sedimentable (MPS)****

| Receptor | Aporte Proyecto tasa de deposición promedio<br>anual (mg/m2N/d) | Col3 | Col4 | Aporte máximo Proyecto tasa de deposición<br>promedio anual (mg/m2N/d) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 161.: Promedio anual de la concentración de dióxido de nitrógeno (NO** **2** **)** **-** **Escenario 3.****

| Receptor | Aporte Proyecto promedio anual<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto promedio anual<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |

**Tabla 162.: Percentil 99 de la concentración horaria de NO** **2** **-** **Escenario 3.****

| Receptor | Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 11 | 8 | 10 | 11 |
| Receptor 2 | 3 | 3 | 3 | 3 |
| Receptor 3 | 6 | 4 | 4 | 6 |
| Receptor 4 | 2 | 2 | 2 | 2 |
| Receptor 5 | 8 | 8 | 8 | 8 |
| Receptor 6 | 13 | 12 | 12 | 13 |
| Estación Laja | 1 | 1 | 1 | 1 |
| Estación San<br>Rosendo | 0 | 0 | 1 | 1 |

**Tabla 163.: Promedio anual de la concentración de dióxido de azufre (SO** **2** **)** **-** **Escenario 3.****

| Receptor | Aporte Proyecto promedio anual<br>(μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto promedio anual<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 164.: Percentil 99 de la concentración diaria de SO** **2** **-** **Escenario 3.****

| Receptor | Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 24 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 24 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 165.: Percentil 98,5 de la concentración de 1 h de SO** **2** **-** **Escenario 3.****

| Receptor | Aporte Proyecto Percentil 98,5 de la<br>concentración en inmisión 1 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 98,5 de la<br>concentración en inmisión 1 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |

**Tabla 166.: Percentil 99,7 de la concentración diaria de SO** **2** **-** **Escenario 3.****

| Receptor | Aporte Proyecto Percentil 99,7 de la<br>concentración en inmisión 24 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99,7 de la<br>concentración en inmisión 24 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación<br>Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 167.: Percentil 99,73 de la concentración horaria de SO** **2** **-** **Escenario 3.****

| Receptor | Aporte Proyecto Percentil 99,73 de la<br>concentración en inmisión 1 h (μg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99,73 de la<br>concentración en inmisión 1 h (μg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación<br>Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 168.: Percentil 99 de la concentración de 1 h de CO** **-** **Escenario 3.****

| Receptor | Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (mg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 1 h (mg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 169.: Percentil 99 de la concentración 8 h de CO** **-** **Escenario 3.****

| Receptor | Aporte Proyecto Percentil 99 de la<br>concentración en inmisión 8 h (mg/m3N) | Col3 | Col4 | Aporte máximo Proyecto Percentil 99 de la<br>concentración en inmisión 8 h (mg/m3N) |
| --- | --- | --- | --- | --- |
| **Receptor** | **2020** | **2021** | **2022** | **2020-2022** |
| Receptor 1 | 0 | 0 | 0 | 0 |
| Receptor 2 | 0 | 0 | 0 | 0 |
| Receptor 3 | 0 | 0 | 0 | 0 |
| Receptor 4 | 0 | 0 | 0 | 0 |
| Receptor 5 | 0 | 0 | 0 | 0 |
| Receptor 6 | 0 | 0 | 0 | 0 |
| Estación Laja | 0 | 0 | 0 | 0 |
| Estación San<br>Rosendo | 0 | 0 | 0 | 0 |

**Tabla 170.: Resumen de PMI para cada MP y** **gas emitido en los escenarios.****

| PMI | Estadístico | 2020 | 2021 | 2022 | Max | Año | Coordenadas UTM | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **PMI** | **Estadístico** | **2020** | **2021** | **2022** | **Max** | **Año** | **Datum WGS 84 Huso 18** | **Datum WGS 84 Huso 18** |
| **PMI** | **Estadístico** | **2020** | **2021** | **2022** | **Max** | **Año** | **Este (m)** | **Norte (m)** |
| Escenario 1 | Promedio anual MP10 (μg/m3) | 0 | 0 | 0 | 0 | 2022 | 702.904,58 | 5.870.494,68 |
| Escenario 1 | Percentil 98 concentración 24 horas MP10 (μg/m3) | 2 | 2 | 2 | 2 | 2022 | 702.904,58 | 5.870.494,68 |
| Escenario 1 | Promedio anual MP2,5 (μg/m3) | 0 | 0 | 0 | 0 | 2022 | 702.904,58 | 5.870.494,68 |
| Escenario 1 | Percentil 98 concentración 24 horas MP2,5 (μg/m3) | 2 | 2 | 2 | 2 | 2022 | 702.904,58 | 5.870.494,68 |
| Escenario 1 | Promedio anual tasa de deposición MPS (mg/m2/d) | 6 | 7 | 6 | 7 | 2021 | 701.948,4 | 5.872.519,81 |
| Escenario 1 | Concentración 24h de SO2, P99 (μg/m3) | 2 | 2 | 1 | 2 | 2021 | 702.686,41 | 5.871.322,12 |
| Escenario 1 | Concentración 1h de SO2, P98,5 (μg/m3) | 3 | 3 | 3 | 3 | 2021 | 702.686,41 | 5.871.322,12 |
| Escenario 1 | Promedio Anual SO2 (μg/m3) | 0 | 0 | 0 | 0 | 2021 | 702.686,41 | 5.871.322,12 |
| Escenario 1 | Concentración 24h SO2, P99,7 (μg/m3) | 2 | 3 | 2 | 3 | 2021 | 702.686,41 | 5.871.322,12 |
| Escenario 1 | Concentración 1h SO2, P99,73 (μg/m3) | 5 | 7 | 6 | 7 | 2021 | 702.686,41 | 5.871.322,12 |
| Escenario 1 | Concentración 1h NO2, P99 (μg/m3) | 85 | 85 | 92 | 92 | 2022 | 702.904,58 | 5.870.494,68 |
| Escenario 1 | Concentración NO2 (μg/m3) | 5 | 5 | 5 | 5 | 2022 | 702.904,58 | 5.870.494,68 |
| Escenario 1 | Concentración 1h CO, P99 (mg/m3) | 0 | 0 | 0 | 0 | 2022 | 702.904,58 | 5.870.494,68 |
| Escenario 1 | Concentración 8h móvil CO, P99 (mg/m3) | 0 | 0 | 0 | 0 | 2022 | 702.904,58 | 5.870.494,68 |
| Escenario 1 | Concentración 24h TRS (μg/m3) | 0 | 0 | 0 | 0 | 2020 | 702.686,41 | 5.871.322,12 |
| Escenario 1 | Concentración 1h TRS (μg/m3) | 0 | 0 | 0 | 0 | 2021 | 702.519 | 5.871.048 |
| Escenario 2 | Promedio anual MP10 (μg/m3) | 0 | 0 | 0 | 0 | 2021 | 702.686,41 | 5.871.322,12 |
| Escenario 2 | Percentil 98 concentración 24 horas MP10 (μg/m3) | 1 | 1 | 1 | 1 | 2020 | 702.904,58 | 5.870.494,68 |
| Escenario 2 | Promedio anual MP2,5 (μg/m3) | 0 | 0 | 0 | 0 | 2021 | 702.904,58 | 5.870.494,68 |
| Escenario 2 | Percentil 98 concentración 24 horas MP2,5 (μg/m3) | 1 | 1 | 1 | 1 | 2020 | 702.904,58 | 5.870.494,68 |
| Escenario 2 | Promedio anual tasa de deposición MPS (mg/m2/d) | 9 | 10 | 8 | 10 | 2021 | 701.948,4 | 5872520 |
