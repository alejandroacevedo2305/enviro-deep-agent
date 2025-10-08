---
title: Sin título
author: mesenia atenas
date: D:20151214104216-03'00'
language: es
type: report
pages: 33
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1. INTRODUCCIÓN ......................................................................................................................... 1
-->

INFORME FINAL
MODELO NUMÉRICO DE FLUJO

EFECTO DE DRENAJE DEL RAJO DMH

**Rev0**

**Preparado para**

**10 de Diciembre de 2015**

Preparado por

HIDROMAS LTDA

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**TABLA DE CONTENIDOS**

# 1. INTRODUCCIÓN ......................................................................................................................... 1

1.1 Aspectos Generales .......................................................................................................................... 1

1.2 Objetivos del Estudio ........................................................................................................................ 2

1.3 Metodología de Trabajo ................................................................................................................... 2

1.3.1 Revisión y Análisis de Información Histórica Disponible ........................................................... 2

1.3.2 Revisión y Análisis de Modelos Hidrogeológicos Existentes ...................................................... 2

1.3.3 Calibración del Modelo Numérico Ampliado de Flujo ............................................................... 2

1.3.4 Generación de Escenarios de Explotación ................................................................................. 3

1.4 Modelo Hidrogeológico Integrado Sector Calama, Pampa Talabre, CPH (2005) ............................. 3

**2.** **CALIBRACIÓN MODELO NUMÉRICO AMPLIADO DE FLUJO .......................................................... 5**

2.1 Aspectos Generales .......................................................................................................................... 5

2.2 Proceso de Calibración Modelo Numérico Ampliado ...................................................................... 8

2.2.1 Régimen Permanente ................................................................................................................ 8

2.2.2 Régimen Transiente ................................................................................................................... 8

2.3 Balance Hídrico ............................................................................................................................... 17

**3.** **ANÁLISIS DEL EFECTO DE DRENAJE DEL RAJO DMH ................................................................... 22**

3.1 Descripción de Escenarios .............................................................................................................. 22

3.2 Efecto Neto del Drenaje del Rajo DMH en los Niveles de Agua Subterránea ................................ 22

3.3 Efecto Neto del Drenaje del Rajo DMH en los Caudales de Cauces Superficiales ......................... 26

**4.** **LÍNEAS DE TRABAJO ................................................................................................................ 30**

4.1 Modelo Conceptual ........................................................................................................................ 30

4.2 Modelo Numérico .......................................................................................................................... 30

**5.** **REFERENCIAS BIBLIOGRÁFICAS ................................................................................................ 31**

**ANEXOS**

Anexo A Modelo Numérico de Flujo

Anexo B Niveles Observados vs Calculados

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia i

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**1.** **INTRODUCCIÓN**

**1.1** **Aspectos Generales**

La Dirección de Recursos Hídricos de la Gerencia de Desarrollo Distrito Norte de CODELCO (DNC), solicitó
a HIDROMAS efectuar el servicio de “Calibración Preliminar del Modelo Numérico de Flujo del Sector del
Rajo DMH”. El presente servicio tiene por objetivo calibrar el modelo numérico de flujo del acuífero de
Calama en el sector cercano al Rajo DMH.

En base a la información existente de los modelos hidrogeológicos y los datos de monitoreo disponibles
de la cuenca de Calama, así como las extracciones actuales de drenaje del Rajo de DMH, se requiere
calibrar el modelo numérico en el sector cercano al Rajo DMH, con el objetivo de obtener los efectos
netos del drenaje del rajo en términos de niveles de aguas subterráneas y de caudales de los cauces
superficiales.

La RCA N°311/2005 entregó la autorización ambiental para la construcción del proyecto minero DMH, el
que incluye el desarrollo de un rajo para la extracción del mineral, cuyo centro se ubica a unos 5 km al
Norte de la ciudad de Calama y a unos 6 km al Sur del campamento Chuquicamata. Al término de la vida
útil del proyecto, el límite Sur del rajo se ubicará aproximadamente a 4 km al Norte del límite urbano de
Calama. En la Figura 1.1 se presenta el rajo DMH y su entorno.

**Figura 1.1**
**Ubicación del Área de Estudio**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 1

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**1.2** **Objetivos del Estudio**

Tal como se ha indicado previamente, el objetivo principal del presente estudio es calibrar
preliminarmente el modelo numérico de flujo del acuífero de Calama, en el sector cercano al Rajo DMH.

Para realizar la calibración del modelo numérico se consideró toda la información existente de los

modelos hidrogeológicos y los datos de monitoreo disponibles de la cuenca de Calama, así como las
extracciones actuales de drenaje del Rajo de DMH.

De acuerdo a las necesidades que involucra realizar la calibración del modelo numérico del acuífero de
Calama en el sector cercano del Rajo DMH, se tienen los siguientes objetivos específicos:

- Revisión y análisis de los datos de monitoreo de la cuenca de Calama.

- Revisión y análisis de los modelos hidrogeológicos existentes.

- Calibración del modelo numérico de flujo.

- Generación de escenarios de explotación.

**1.3** **Metodología de Trabajo**

Para realizar la calibración del modelo numérico de aguas subterráneas se siguió el siguiente plan de
trabajo, el que pone énfasis en los siguientes puntos:

1.3.1 Revisión y Análisis de Información Histórica Disponible

Se revisaron y evaluaron los datos de monitoreo de niveles de aguas subterráneas de la cuenca de
Calama, así como también las extracciones actuales de drenaje del Rajo de DMH.

1.3.2 Revisión y Análisis de Modelos Hidrogeológicos Existentes

Se realizó una revisión y evaluación de los modelos hidrogeológicos realizados para el acuífero de la

cuenca de Calama:

- Modelo Hidrogeológico Integrado Sector Calama, Pampa Talabre, CPH (2005).

- Modelamiento Hidráulico Tranque Talabre y su Relación con los Acuíferos y Cauces Superficiales,
Knight Piésold (2010).

- Servicio de Construcción y Validación de Modelamiento Numérico - Modelación Hidrogeológica del
Acuífero de Calama, HIDROMAS (2012).

- Actualización Modelo de Flujo - Estudio Infiltración Tranque Talabre, HIDROMAS (2014).

- Análisis Integrado Río Loa, Región de Antofagasta, DGA - Knight Piésold (2014).

1.3.3 Calibración del Modelo Numérico Ampliado de Flujo

A través del tiempo se han realizando diferentes modelos numéricos del área de estudio, los que han ido
incorporando mejoras en diferentes aspectos del modelo conceptual y numérico, basadas en nueva
información de terreno. Los elementos que se han ido modificando en el modelo conceptual y numérico

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 2

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

son: la geometría del acuífero, las condiciones de borde, la ubicación del tranque (estrato acuífero), las
filtraciones del tranque, el área activa, la interacción río-acuífero, entre otros. Las modificaciones
anteriormente mencionadas se encuentran incorporadas en el modelo numérico que se reporta en el
presente informe, el que se denominará modelo numérico ampliado.

Para la calibración del modelo numérico ampliado se realizó la actualización de los niveles de agua
subterránea y caudales de bombeo de los pozos de propiedad de CODELCO, hasta Junio de 2015 del
modelo de flujo de aguas subterráneas. La actualización se la realizó a partir de información recabada en
la base de datos de niveles piezométricos de DNC y los caudales de bombeo fueron proporcionados por

DNC.

En el caso de los niveles de agua subterránea y los caudales de bombeo de los pozos de propiedad de El
Tesoro, se obtuvo la información del estudio “Análisis Integrado Río Loa, Región de Antofagasta”, DGAKnight Piésold (2014).

1.3.4 Generación de Escenarios de Explotación

Los escenarios de explotación se utilizaron para evaluar cambios en el sistema de aguas subterráneas
debido a diferentes escenarios de extracción del recurso hídrico en el sector. Para estos efectos se

consideraron situaciones de interés, para las cuales la operación del modelo de simulación permitió

evaluar las consecuencias de estos cambios.

**1.4** **Modelo Hidrogeológico Integrado Sector Calama, Pampa Talabre, CPH (2005)**

El modelo tuvo por objetivo determinar las características hidráulicas subterráneas del área estudiada:
direcciones y magnitudes del flujo subterráneo en los dos medios permeables existentes en la zona
(acuífero freático alojado en rocas calcáreas de la Formación El Loa y acuífero preferentemente
confinado, correspondiente a gravas y arenas de la Formación Calama). Además, se utilizó para analizar
el efecto de drenaje del futuro rajo del proyecto Alejandro Hales sobre el acuífero inferior de gravas y
sobre el acuífero superior freático de las Calizas, siendo éste último el que alimenta al sector de vegas
que dan origen al río San Salvador y Ojos de Opache.

El área modelada abarca por el Norte desde una línea localizada cercana a Chuquicamata y Mina Sur
hasta el trazado aproximado del río Loa por el Sur y Este. Por el Oeste hasta poco aguas abajo de la
ciudad de Calama, de acuerdo a la Figura 1.2.

El modelo consideró una malla de 248 filas por 339 columnas y tres estratos. La geometría de los
estratos representados en el modelo numérico se definió a partir del modelo hidrogeológico que poseía
Codelco en ese momento, basado principalmente en la perforación de sondajes y geofísica.

La superficie de terreno se representó a partir de una topografía con curvas de nivel cada 5 m,
combinada con otra obtenida de cartas IGM 1.50.000. También se consideró la topografía original en
donde hoy se ubica el Tranque Talabre que data de 1952, el que en el modelo numérico se representó
fundado sobre la unidad de arcillas y arcillolitas, es decir el Estrato 2.

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 3

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 1.2**
**Área de Modelación CPH 2005**

Fuente: CPH (2005)

En cuanto a la calibración del modelo, se informa que para los niveles observados en el Estrato 1, el RMS
obtenido fue de 2,9% y para el Estrato 3 un RMS de 2,2%. En el caso del Estrato 1 (calizas) se utilizó un
total de 14 pozos de control y en el caso del Estrato 3 (gravas) fueron 13 sondajes.

En las conclusiones de este trabajo se señala que el efecto del drenaje del futuro rajo del proyecto MMH
se manifestaría casi exclusivamente en el acuífero inferior de gravas. Asimismo la reducción del caudal
de salida de este acuífero (entre cerros Calama y La Cruz) sería del orden del 6%. El efecto en el estrato
superior sería menor o caso despreciable. Esto también implicaría que no se vería afectada la vertiente
de Ojos de Opache, así como el nacimiento del río San Salvador. El modelo entrega como resultado que
el acuífero freático ubicado al norte y al norponiente del río Loa, aporta un caudal de aproximadamente
250 l/s.

Dentro de las recomendaciones de este estudio se destacan la necesidad de estudiar con mayor detalle
los sectores hacia el Este y Sur del río Loa, hasta aguas abajo de Calama, incluyendo los sectores de Ojos
de Opache, desarrollar un estudio específico de infiltración del tranque Talabre y mejorar la geología a

una escala de 1:5.000 en las zonas cercanas al río Loa.

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 4

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**2.** **CALIBRACIÓN MODELO NUMÉRICO AMPLIADO DE FLUJO**

**2.1** **Aspectos Generales**

La elaboración del modelo de simulación numérico incluye la definición dentro de la estructura del
software de los límites de la zona de modelación, la discretización horizontal y vertical, la distribución
espacial de parámetros hidrogeológicos, la asignación de condiciones de borde y la incorporación de las
acciones externas al sistema modelado, lo que incluye las recargas y descargas.

Con base en la información disponible se ha supuesto que el sistema de aguas subterráneas en el
acuífero de Calama es un medio poroso tradicional, lo que permite utilizar herramientas clásicas en la
modelación de este sistema como el programa MODFLOW, desarrollado por McDonald y Harbaugh
pertenecientes al U.S. Geological Survey (1988).

En el caso particular de este estudio se utiliza el software Visual MODFLOW, desarrollado por la empresa
canadiense Waterloo Hydrogeologic Inc. El modelo Visual MODFLOW, es una herramienta
computacional muy útil y fácil de operar, por sus características visuales y de manejo de datos.

Para completar la fase de modelación numérica se procede a calibrar el modelo, para lo cual se
selecciona un período de tiempo que disponga de información suficiente. A continuación se mencionan
las principales actividades realizadas para la etapa de calibración del modelo hidrogeológico de la cuenca

de Calama:

- Extensión de las tasas de recarga y las condiciones de borde (nivel conocido, dren y río) del régimen

transiente hasta Junio de 2015.

- Actualización de los niveles de agua subterránea y de los caudales de bombeo hasta Junio de 2015.

- Definición del sector cercano al Rajo MH, el que se presenta en las Figura 2.1a y 2.1b junto con los
pozos de observación del régimen transiente.

- Calibración de la conductividad hidráulica (régimen permanente) y coeficiente de almacenamiento
(régimen transiente) del sector cercano al Rajo MH.

En el Anexo A se presentan las principales características constructivas del modelo numérico ampliado
de flujo del acuífero de Calama.

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 5

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 2.1a**
**Sector de Calibración Cercano al Rajo DMH**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 6

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 2.1b**
**Detalle del Sector de Calibración Cercano al Rajo DMH**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 7

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**2.2** **Proceso de Calibración Modelo Numérico Ampliado**

2.2.1 Régimen Permanente

El proceso de calibración en régimen permanente, consistió principalmente en reproducir, tanto
cualitativa como cuantitativamente, los aspectos geométricos, relaciones funcionales y comportamiento
del sistema de aguas subterráneas (mediante niveles, dirección del flujo, relación río-acuífero, zonas de
recarga, sectores secos de la unidad de Calizas, etc.). En particular y para efectos de tener una certeza
numérica del ajuste, se trató de reproducir los niveles estáticos registrados en los pozos de observación.

La calibración del modelo hidrogeológico ampliado se realizó en régimen permanente, para lo cual se
dispuso de 37 puntos con información medida de los niveles de agua subterránea en el acuífero de la
cuenca de Calama, cuya ubicación se muestra gráficamente en la Figura 2.2.

Las condiciones de borde para el modelo en régimen permanente fueron definidas para Enero de 2003,
por lo que los niveles que fueron contrastados son aquellos observados o proyectados para esta fecha.

Durante la calibración del modelo hidrogeológico ampliado se modificó los valores de la conductividad
hidráulica hasta conseguir que los valores medidos y simulados de los niveles de agua en los 37 puntos
fueran lo más parecidos posibles entre ellos.

Al finalizar el proceso de calibración del modelo numérico ampliado mediante el proceso de prueba y
error, se obtuvieron ajustes globales satisfactorios entre los valores simulados y medidos, lo que se mide
a través de diversos indicadores de bondad de ajuste. El indicador más utilizado para medir la calidad del
ajuste es el denominado error cuadrático medio normalizado (NRMS) el que alcanzó un valor de 2,756%,
lo que se considera como adecuado para una calibración en condiciones de régimen permanente.

En la Figura 2.3 se muestra el RMS Normalizado obtenido en el proceso de calibración y una
comparación gráfica entre los valores medidos y simulados de los niveles de agua para el modelo
numérico ampliado de la cuenca de Calama.

2.2.2 Régimen Transiente

La calibración en régimen transiente del modelo numérico ampliado se realizó para el período
comprendido desde Enero de 2003 hasta Junio de 2015, para lo cual se dispuso de 202 puntos con
información medida de los niveles de agua subterránea en los acuíferos superior e inferior de la cuenca
de Calama. La ubicación de los pozos de observación se muestra gráficamente en la Figura 2.4.

Durante la calibración del modelo hidrogeológico ampliado en régimen transiente se modificó los valores
de los coeficientes de almacenamientos hasta conseguir ajustar que los valores medidos y simulados de
los niveles de agua en los 202 puntos fueran lo más parecidos posibles entre ellos.

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 8

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 2.2**
**Ubicación Pozos de Observación - Régimen Permanente**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 9

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 2.3**
**Indicadores de Ajuste en Proceso de Calibración en Régimen Permanente**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 10

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 2.4**
**Ubicación Pozos de Observación - Régimen Transiente**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 11

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

El indicador utilizado para medir la calidad del ajuste entre los valores simulados y medidos durante la
fase de calibración fue el Normalized RMS (Root Mean Squared) el que alcanzó un valor de 2,135%. En
las Figuras 2.5 y 2.6 se muestran los RMS Normalizados obtenidos en el proceso de calibración en
régimen transiente y una comparación gráfica entre los valores medidos y simulados de los niveles de
agua para toda el área del modelo numérico ampliado de la cuenca de Calama y para el sector cercano al
Rajo DMH, respectivamente.

En la Tabla 2.1 se presentan los resultados obtenidos del RMS Normalizado para toda el área de
modelación y el sector cercano al Rajo DMH, en términos del gradiente regional y del gradiente local
para ambos sectores. Cabe mencionar, que durante el proceso de calibración se dio mayor prioridad en
lograr un mejor ajuste en los pozos más cercanos al Rajo DMH.

**Figura 2.5**
**Indicadores de Ajuste en Proceso de Calibración en Régimen Transiente - Toda el Área de Modelación**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 12

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 2.6**
**Indicadores de Ajuste en Proceso de Calibración en Régimen Transiente - Sector Cercano al Rajo DMH**

Fuente: Elaboración Propia

**Tabla 2.1**

**RMS Normalizado**

|Grupo|NRMS% dh Local|NRMS% dh Regional|
|---|---|---|
|Todos|2,135|2,135|
|Sector Rajo DMH|6,693|2,381|

Fuente: Elaboración Propia

En las Figuras 2.7 a 2.13 se presentan los resultados de los niveles medidos y simulados de algunos
pozos de observación del modelo hidrogeológico ubicados en el sector cercano al Rajo DMH. En el
Anexo B se presentan los resultados de los niveles medidos y simulados de todos los pozos de
observación del sector cercano al Rajo DMH, utilizados en el proceso de calibración del modelo numérico
ampliado de la cuenca de Calama.

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 13

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 2.7**
**Niveles Simulados y Observados - PBMM-4 (IL)**

Fuente: Elaboración Propia

**Figura 2.8**
**Niveles Simulados y Observados - CC-16 (IC)**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 14

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 2.9**
**Niveles Simulados y Observados - CC-18 (S)**

Fuente: Elaboración Propia

**Figura 2.10**
**Niveles Simulados y Observados - CC-9 (S)**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 15

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 2.11**
**Niveles Simulados y Observados - SI-8C (S)**

Fuente: Elaboración Propia

**Figura 2.12**
**Niveles Simulados y Observados - CC-11 (S)**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 16

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 2.13**
**Niveles Simulados y Observados - CC-10 (IC)**

Fuente: Elaboración Propia

**2.3** **Balance Hídrico**

El balance hídrico del sistema subterráneo del acuífero de la cuenca de Calama depende de términos que
dan cuenta del aporte de agua a la napa subterránea (recarga) y de términos que dan cuenta de la
extracción de agua subterránea (descarga) en forma natural y artificial.

Una vez calibrado el modelo hidrogeológico del acuífero del área de estudio, es posible cuantificar los
flujos de entrada y salida del sistema acuífero, y por ende conocer el balance hídrico del sistema.

La información resumida del balance hídrico general en régimen permanente del acuífero de la cuenca
de Calama se presenta en la Tabla 2.2. En la Figura 2.14 se presentan los errores de cierre del balance

<!-- INICIO TABLA 2.2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- INFORME MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH _______________________________________________________________ -->

**Tabla 2.2: ****

| Entradas | m3/d | l/s |
| --- | --- | --- |
| Recarga | 33680 | 390 |
| Nivel Conocido | 129859 | 1514 |
| Ríos | 2290 | 26 |
| **TOTAL** | **166770** | **1930** |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- |Salidas|m3/d|l/s| |---|---|---| |Nivel Conocido|35988|420| |Ríos|113437|1316| -->
<!-- FIN TABLA 2.2 -->

hídrico del modelo en régimen transiente para el período de calibración. La Figura 2.15 muestra la
ubicación de las condiciones de borde que representan los cauces superficiales incorporados
específicamente en el modelo numérico ampliado. En las Figuras 2.16, 2.17 y 2.18 se presentan los
caudales de salida a través de las condiciones de borde que representan al río San Salvador, el
nacimiento de la vertiente Ojos de Opache y el río Loa en sector más cercano al Rajo DMH,
respectivamente.

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 17

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Tabla 2.2**

**Balance Hídrico General**

|Entradas|m3/d|l/s|
|---|---|---|
|Recarga|33680|390|
|Nivel Conocido|129859|1514|
|Ríos|2290|26|
|**TOTAL**|**166770**|**1930**|

|Salidas|m3/d|l/s|
|---|---|---|
|Nivel Conocido|35988|420|
|Ríos|113437|1316|
|Drenes|16570|197|
|**TOTAL**|**166980**|**1933**|

Fuente: Elaboración Propia

**Figura 2.14**
**Error de Cierre - Régimen Transiente**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 18

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 2.15**
**Ubicación de Condiciones de Borde y Rajo DMH**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 19

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 2.16**

**Caudales de Salida Río San Salvador**

Fuente: Elaboración Propia

**Figura 2.17**
**Caudales de Salida Vertiente Ojos de Opache**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 20

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 2.18**
**Caudales de Salida Río Loa Sector Más Cercano a Rajo DMH**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 21

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**3.** **ANÁLISIS DEL EFECTO DE DRENAJE DEL RAJO DMH**

**3.1** **Descripción de Escenarios**

Una vez que el modelo numérico ampliado de flujo del acuífero de la cuenca de Calama fue calibrado de
manera preliminar, se utilizó para evaluar cambios en el sistema de aguas subterráneas debido a

diferentes escenarios de extracción del recurso hídrico en el sector. Para estos efectos se consideraron

dos situaciones de interés, para las cuales la operación del modelo de simulación permitió evaluar las

consecuencias de estos cambios.

Los escenarios futuros que se analizaron responden a dos situaciones diferentes, las cuales permiten
estudiar los impactos que se producen sobre los niveles de aguas subterráneas y los caudales de los
cauces superficiales de la zona. Los escenarios a modelar para el acuífero de la cuenca de Calama son los
siguientes:

- **Escenario Sin Proyecto:** representa la situación sin explotación de los pozos de bombeo del Rajo
DMH hasta Agosto de 2050.

- **Escenario Con Proyecto:** representa la situación con explotación de los pozos de bombeo del Rajo
DMH a partir de Agosto de 2010 hasta Agosto de 2030, posteriormente se detiene el bombeo de los
pozos del Rajo DMH y se simula el modelo hasta Agosto de 2050.

**3.2** **Efecto Neto del Drenaje del Rajo DMH en los Niveles de Agua Subterránea**

Para determinar el efecto neto del drenaje del Rajo DMH en los niveles de agua subterránea del acuífero
de Calama, se restaron los niveles de agua calculados obtenidos del escenario sin proyecto menos los
niveles calculados del escenario con proyecto (escenario sin proyecto - escenario con proyecto). En la
Figura 3.1 se muestra la ubicación de los pozos de observación (enmarcados en color rojo) de la “Línea
de No Afectación” y los pozos SI-8C (S), CC-11 (S) y CC-10 (IC), en los cuales se determinó el efecto neto
del drenaje del Rajo DMH.

En las Figuras 3.2 y 3.3 se presenta el efecto neto del drenaje del Rajo DMH en los niveles de agua
subterránea del primer (acuífero libre) y tercer (acuífero confinado) estrato del acuífero de Calama para
los pozos de observación de la “Línea de No Afectación”. En las figuras anteriormente mencionadas se
observa el efecto neto del drenaje del rajo para los meses de Agosto de los años 2015, 2020, 2025 y
2030, produciéndose los mayores efectos en Agosto de 2030. También se observa que los mayores
efectos del drenaje del Rajo DMH en la “Línea de No Afectación” se producen en el estrato inferior. Cabe
mencionar que el drenaje del rajo minero se inició en Agosto de 2010.

En las Figuras 3.4, 3.5 y 3.6 se muestra el efecto neto producido por el drenaje del rajo en los niveles de
agua subterránea de los pozos de observación SI-8C (S), CC-11 (S) y CC-10 (IC) para todo el período de
simulación del modelo numérico ampliado. En el pozo SI-8C (S) se produce el mayor efecto neto (1,89 m
en Enero del año 2033) ocasionado por el drenaje del rajo, mientras en los pozos CC-11 (S) (0,32 m en
Abril del año 2040) y CC-10 (IC) (0,50 m en Enero del año 2038) el efecto es menor.

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 22

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 3.1**

**Ubicación de Pozos de Observación**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 23

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 3.2**
**Efecto Neto en la Línea de No Afectación - Acuífero Superior**

Fuente: Elaboración Propia

**Figura 3.3**

**Efecto Neto en la Línea de No Afectación - Acuífero Inferior**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 24

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 3.4**
**Efecto Neto en el Pozo SI-8C (S) - Acuífero Superior**

Fuente: Elaboración Propia

**Figura 3.5**
**Efecto Neto en el Pozo CC-11 (S) - Acuífero Superior**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 25

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 3.6**
**Efecto Neto en el Pozo CC-10 (IC) - Acuífero Inferior**

Fuente: Elaboración Propia

Los efectos observados son, en muchos casos, el reflejo de información incompleta a nivel local, lo que
hace que el modelo refleje adecuadamente la situación a nivel regional, pero no permita diferenciar
tendencias naturales a nivel local, lo que incrementa al efecto del drenaje del rajo DMH.

**3.3** **Efecto Neto del Drenaje del Rajo DMH en los Caudales de Cauces Superficiales**

Para determinar el efecto neto del drenaje del Rajo DMH en los caudales de los cauces superficiales
cercanos al rajo, se restaron los caudales calculados de salida de los cauces superficiales del escenario sin
proyecto menos los caudales calculados de salida de los cauces superficiales del escenario con proyecto
(escenario sin proyecto - escenario con proyecto). En la Figura 3.7 se muestra la ubicación de las
condiciones de borde que representan los cauces superficiales en el modelo numérico ampliado.

En las Figuras 3.8, 3.9 y 3.10 se muestra el efecto neto producido por el drenaje del rajo en los caudales
de salida de los cauces superficiales del río Loa, del nacimiento de la vertiente Ojos de Opache y del río
San Salvador para todo el período de simulación del modelo numérico ampliado. En términos de
caudales de cauces superficiales, el mayor efecto neto producido por el drenaje del rajo minero, se
observa en el río San Salvador con una disminución del caudal de hasta 1,82 l/s en Junio del año 2032.

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 26

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 3.7**
**Ubicación de Cauces Superficiales**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 27

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 3.8**

**Efecto Neto en Río Loa**

Fuente: Elaboración Propia

**Figura 3.9**
**Efecto Neto en Vertiente Ojos de Opache**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 28

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**Figura 3.10**

**Efecto Neto en Río San Salvador**

Fuente: Elaboración Propia

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 29

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**4.** **LÍNEAS DE TRABAJO**

Tal como se menciona al inicio de este documento, lo que se trató de alcanzar es la mejor calibración
regional, así como también a un nivel local, utilizando la información disponible a la fecha. En el proceso
se logró identificar una serie de elementos que indican que alguno de los efectos observados no tienen
relación con el drenaje del rajo DMH sino que son el resultado de información incompleta que hace que
el modelo actual no permita reflejar adecuadamente la situación existente.

Con base en los resultados anteriores es posible cerrar este informe con una serie de lineamientos a
seguir en el modelo conceptual y modelo numérico ampliado con el objetivo de mejorar la herramienta
numérica, permitiendo de este modo mejor la evaluación de los cambios en el sistema de aguas

subterráneas debido a diferentes escenarios de extracción del recurso hídrico.

A continuación se resumen los lineamientos identificados, separándolos en los temas de modelo
conceptual y modelo numérico.

**4.1** **Modelo Conceptual**

Temas a mejorar o analizar en relación con el modelo conceptual:

- Actualización de las condiciones de borde.

- Actualización de las recargas del área del modelo.

- Revisión de las cotas de los pozos de observación pertenecientes a CODELCO y a terceros.

- Incorporación de la nueva información geofísica y estratigráfica en la geometría del acuífero.

- Actualización de las zonas de permeabilidad y coeficiente de almacenamiento, incorporando la
nueva información obtenida de pruebas hidráulicas realizadas en terreno **.**

- Actualización de las extracciones realizadas por terceros en la cuenca de Calama.

- Actualización del balance hídrico del sistema acuífero.

- El modelo conceptual debe ser elaborado tomando en cuenta las recomendaciones de la Guía para
el Uso de Modelos de Aguas Subterráneas del SEIA.

**4.2** **Modelo Numérico**

Temas a mejorar o analizar en relación con el modelo numérico:

- Implementar en el modelo numérico los cambios recomendados a ser realizados en el modelo
conceptual.

- Verificar la representatividad del modelo numérico respecto al sistema real.

- Iniciar la calibración del modelo numérico tomando como base las zonas de permeabilidad y
coeficiente de almacenamiento actualizadas en el modelo conceptual.

- Actualizar el software Visual MODFLOW a la última versión disponible.

- El modelo numérico debe ser elaborado tomando en cuenta las recomendaciones de la Guía para el
Uso de Modelos de Aguas Subterráneas del SEIA.

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 30

[www.hidromas.cl](http://www.hidromas.cl/)

INFORME
MODELO NUMÉRICO DE FLUJO. EFECTO DE DRENAJE DEL RAJO DMH

_______________________________________________________________

**5.** **REFERENCIAS BIBLIOGRÁFICAS**

- CPH. (2005). Modelo Hidrogeológico Integrado Sector Calama, Pampa Talabre.

- Knight Piésold. (2010). Modelamiento Hidráulico Tranque Talabre y su Relación con los Acuíferos y
Cauces Superficiales.

- HIDROMAS. (2012). Servicio de Construcción y Validación de Modelamiento Numérico - Modelación
Hidrogeológica del Acuífero de Calama.

- HIDROMAS. (2014). Actualización Modelo de Flujo - Estudio Infiltración Tranque Talabre.

- DGA - Knight Piésold. (2014). Análisis Integrado Río Loa, Región de Antofagasta.

Hidrogeología y Medio Ambiente Sustentable Ltda.
Suecia 211, Oficina 1301-B

Providencia 31

[www.hidromas.cl](http://www.hidromas.cl/)

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.1: ****

| Grupo | NRMS% dh Local | NRMS% dh Regional |
| --- | --- | --- |
| Todos | 2,135 | 2,135 |
| Sector Rajo DMH | 6,693 | 2,381 |
