---
title: Sin título
author: Felipe Orellana
date: D:20190523091512-04'00'
language: es
type: report
pages: 69
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - CONTENIDO
  - FIGURAS
  - TABLAS
  - ANEXOS
  - CAPÍTULO 1 INTRODUCCIÓN
  - CAPÍTULO 2 NUEVOS TRABAJOS DE TERRENO
  - CAPÍTULO 3 MODELO CONCEPTUAL DE FLUJO
  - CAPÍTULO 4 MODELO NUMÉRICO
  - CAPÍTULO 5 DISEÑO RED DE MONITOREO
  - CAPÍTULO 6 CONCLUSIONES
-->

## ECOBIO MODELO HIDROGEOLÓGICO CONCEPTUAL Y NUMÉRICO RELLENOS RSU Y CITA PARA DISEÑO DE RED DE MONITOREO

### INFORME TÉCNICO

_**HID-18-35**_

### REV. 1

#### Preparado para: Mayo 2019

# CONTENIDO

CAPÍTULO 1 INTRODUCCIÓN 7

1.1 GENERAL 7

1.2 ALCANCES Y OBJETIVOS 7

1.3 LOCALIZACIÓN 7

1.4 REFERENCIAS TÉCNICAS 8

CAPÍTULO 2 NUEVOS TRABAJOS DE TERRENO 10

2.1 PERFORACIONES REALIZADAS 10

2.2 ESTRATIGRAFÍAS 11

2.3 INTERPRETACIÓN DE ENSAYOS SLUG TEST 16

2.3.1 Metodología de Interpretación 16

2.3.2 Resultados 17

2.4 INTERPRETACIÓN DE PRUEBAS DE BOMBEO Y RECUPERACIÓN 18

2.4.1 Metodología de Interpretación 18

2.4.2 Resultados 19

CAPÍTULO 3 MODELO CONCEPTUAL DE FLUJO 21

3.1 INFORMACIÓN DE CALICATAS REALIZADAS EN ESTUDIOS ANTERIORES 21

3.2 ESTRATOS Y ACUÍFEROS RECONOCIDOS 23

3.2.1 Geometría 23

3.2.2 Parámetros Hidráulicos 24

3.3 NIVEL PIEZOMÉTRICO Y CONCEPTUALIZACIÓN DE FLUJO 25

3.4 DOMINIO MODELO CONCEPTUAL 30

3.5 ZONAS DE RECARGA Y DESCARGA 31

3.5.1 Flujo Subterráneo de Entrada 31
3.5.2 Recarga por Precipitación. 32
3.5.3 Flujo Subterráneo de Salida 33

3.6 BALANCE HIDROGEOLÓGICO CONCEPTUAL 33

CAPÍTULO 4 MODELO NUMÉRICO 35

4.1 CONSTRUCCION MODELO NUMÉRICO 35

4.1.1 Código Matemático 35

 - i

CONTENIDO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

4.1.2 Límites y Geometría 35
4.1.3 Discretización Temporal y Periodos de Stress 40

4.1.4 Condiciones de Borde 40

4.1.5 Parámetros Hidrogeológicos del Modelo Numérico 42

4.1.6 Pozos de Observación 43

4.2 CALIBRACIÓN DEL MODELO NUMÉRICO 43

4.2.1 Ajustes de Flujo y Permeabilidad Consideradas 43
4.2.2 Resultados del Ajuste del Modelo 44
4.2.3 Balance Hidrogeológico 46

CAPÍTULO 5 DISEÑO RED DE MONITOREO 48

5.1 SIMULACIÓN FUTURA EN MODELO NUMÉRICO DE FLUJO 48
5.1.1 IMPLEMENTACIÓN DE PROYECCIÓN EN VIDA ÚTIL RSU Y CITA 48

5.2 SIMULACIÓN DE MOVILIDAD DE CONTAMINANTE 49
5.2.1 POTENCIAL DE CONTAMINACIÓN HÍDRICA SUBTERRÁNEA 49
5.2.2 TRAYECTORIAS DE PARTÍCULAS 51

5.2.3 DISEÑO DE RED DE MONITOREO 53

5.3 DISEÑO DE PIEZÓMETROS Y ESPECIFICACIONES TÉCNICAS 57

5.3.1 Perforación Piezómetros 58

5.3.2 Habilitación del Piezómetro 58

5.3.3 Desarrollo 59

5.3.4 Terminación 59

5.3.5 Pruebas de Permeabilidad 59

5.3.6 Muestreo 59

5.3.7 Ficha Técnica 60

5.4 SISTEMA DE MONITOREO 63

5.4.1 Variables a Monitorear 63
5.4.2 FRECUENCIA Y DURACIÓN DE MUESTREO 65

5.4.3 Procedimiento de Toma de Muestra 65

CAPÍTULO 6 CONCLUSIONES 67

 - ii

CONTENIDO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

# FIGURAS

Figura 1.3-1 Ubicación Proyecto Ecobio ...................................................................................... 8
Figura 2.1-1 Ubicación de Piezómetros de Exploración Perforados ......................................... 10
Figura 2.2-1 Resumen Estratigrafías Sondajes de Exploración Habilitados en Acuífero

Intermedio ................................................................................................................................. 14

Figura 2.2-2 Resumen Estratigrafías Sondajes de Exploración Habilitados en Acuífero
Superficial .................................................................................................................................. 15
Figura 2.3-1 Recta de Ajuste a Datos de Campo ....................................................................... 17
Figura 3.1-1 Ubicación de Calicatas Realizadas en HIDRICA, 2017 ........................................... 21
Figura 3.1-2 Ubicación de Calicatas Realizadas en GAC, 2018 .................................................. 22
Figura 3.1-3 Ubicación de Calicatas Realizadas en GAC, 2018b ................................................ 23
Figura 3.3-1 Isopiezas Estimadas y Dirección de Flujo en Sistema Subterráneo (abril 2019) ... 27
Figura 3.3-2 Trazado en Planta de Perfil en Ecobio ................................................................... 28
Figura 3.3-3 Perfil Transversal de Sistema Subterráneo en Ecobio .......................................... 29
Figura 3.4-1 Isopiezas y Dirección de Flujo Regional ................................................................. 30
Figura 3.4-2 Dominio Modelo Conceptual ................................................................................ 31
Figura 3.6-1 Esquema Conceptual Balance Hidrogeológico en Área de Estudio ...................... 34
Figura 4.1-1 Límite Modelo Numérico, Rotado en Visual MODFLOW ...................................... 37
Figura 4.1-2 Grilla de Modelación Usada en Visual MODFLOW ............................................... 37
Figura 4.1-3 Planta con Perfil de Corte en Leapfrog ................................................................. 39
Figura 4.1-4 Perfil de Corte en Leapfrog ................................................................................... 39
Figura 4.1-5 Perfil de Corte en Visual MODFLOW ..................................................................... 40
Figura 4.1-6 Implementación de Condiciones de Borde en Visual MODFLOW ........................ 42
Figura 4.2-1 Resultados Gráficos del Modelo Numérico ........................................................... 45
Figura 4.2-2 Equipotenciales Modelo Numérico Abril 2019 ..................................................... 46
Figura 5.1-1 Sectores Sin Recarga por Precipitación por Avance CITA y RSU ........................... 49
Figura 5.2-1 Zonas de Potenciales Fallas para Actual Disposición de CITA y RSU ..................... 50
Figura 5.2-2 Zonas de Potenciales Fallas para Futura Disposición de CITA y RSU .................... 51
Figura 5.2-3 Líneas de Trayectoria Proyectadas para Cada Partícula ....................................... 52
Figura 5.2-4 Líneas de Trayectoria Proyectadas en Perfil ......................................................... 53
Figura 5.2-5 Ubicación de Pozos de Monitoreo Superficial para Detección de Eventuales Fallas

en Modelo de Movilidad de Contaminante .............................................................................. 54

Figura 5.2-6 Ubicación de Pozos de Monitoreo de Aguas Subterráneas de Operación CITA y RSU

................................................................................................................................................... 55

Figura 5.3-1 Contenido de Ficha Técnica de Piezómetro .......................................................... 61

 - 3

INTRODUCCIÓN

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Figura 5.3-2 Propuesta de Piezómetro de Monitoreo de Aguas Subterráneas de Operación CITA
y RSU .......................................................................................................................................... 62

 - 4

INTRODUCCIÓN

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

# TABLAS

Tabla 2.1-1 Ubicación y Características de Piezómetros ........................................................... 11
Tabla 2.3-1 Resumen de Ensayos Slug Test Realizados ............................................................. 16
Tabla 2.3-2 Resumen de Permeabilidades Determinadas con Slug Test .................................. 17
Tabla 2.4-1 Resumen de Transmisividades (m [2] /d) .................................................................... 20
Tabla 2.4-2 Resumen de Permeabilidades (m/d) ...................................................................... 20

Tabla 3.2-1 Resumen de Permeabilidad de Sistemas Acuíferos Identificados ......................... 25

Tabla 3.2-2 Resumen de Coeficientes de Almacenamiento de Sistemas Acuíferos Identificados

................................................................................................................................................... 25

Tabla 3.2-3 Resumen de Permeabilidad de Acuitardos Identificados ...................................... 25

Tabla 3.3-1 Resumen de Profundidad a Niveles Piezométrico en Nuevos Pozos de Monitoreo

................................................................................................................................................... 26

Tabla 3.3-2 Resumen de Niveles Piezométricos en Nuevos Pozos de Monitoreo .................... 26

Tabla 3.3-3 Resumen de Profundidad a Niveles Piezométrico en Antigua Red de Monitoreo 27
Tabla 3.5-1 Flujo Subterráneo de Entrada a Modelo Conceptual ............................................. 32
Tabla 3.5-2 Recarga Media Anual por Concepto de Precipitación ............................................ 33

Tabla 4.1-1 Coordenadas Límite Dominio Modelación ............................................................. 36

Tabla 4.1-2 Capas de Simulación del Modelo Numérico ........................................................... 38
Tabla 4.1-3 Recarga por Precipitación en Modelo Numérico ................................................... 42
Tabla 4.2-1 Valores de Permeabilidad y Coeficiente de Almacenamiento Adoptados en Modelo

................................................................................................................................................... 44

Tabla 4.2-2 Estadígrafos Calibración ......................................................................................... 45
Tabla 4.2-3 Balance Hidrogeológico- Promedio 2015-2019 ..................................................... 47

Tabla 5.2-1 Resumen Red de Monitoreo ................................................................................... 56

Tabla 5.2-2 Características Red de Monitoreo .......................................................................... 57

Tabla 5.4-1 Parámetros Medidos en Terreno ........................................................................... 63

Tabla 5.4-2 Parámetros Analizados en Laboratorio .................................................................. 63

 - 5

INTRODUCCIÓN

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

# ANEXOS

Anexo A - Base de datos Calidad Pozos Monitoreo 2018 - 2019

Anexo B - Registro Monitoreo Niveles Freáticos Pozos Nuevos

Anexo C - Plano Topografía 2018, EXIMIA

Anexo D - Informe Supervisión de Perforación Pozos Planta Ecobio

Anexo E - Disposición proyectada de RSU y CITA

 - 6

INTRODUCCIÓN

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

# CAPÍTULO 1 INTRODUCCIÓN

**1.1** **GENERAL**

La empresa Ecobio S.A. (en adelante Ecobio), forma parte del Grupo Volta, quien agrupa
además las empresas Ecomaule, Ecoser y Servinor. En la actualidad Ecobio opera el relleno
sanitario Fundo Las Cruces, ubicado 10 km al sur de Chillán Viejo; que fuera aprobado
ambientalmente en 1999 y el proyecto “Centro Integral de Tratamiento Ambiental Fundo Las

Cruces: CITA ECOBIO S.A.”

En junio de 2018, Ecobio presentó una Declaración de Impacto Ambiental (DIA) del Proyecto
“Mejoramiento del Sistema de Monitoreo de Aguas Subterráneas del Relleno Sanitario Fundo
Las Cruces y del Relleno CITA”, el cual tiene por propósito mejorar el sistema de monitoreo
ambiental de las aguas subterráneas, definiendo un plan de alerta temprana, y un plan de
contingencias. En este aspecto, Ecobio ha solicitado a HIDRICA Consultores la realización de un
Modelo Conceptual y Numérico de Flujo y Movilidad de Contaminante para el Diseño de la Red
de Monitoreo, y así poder dar respuesta a las observaciones planteadas por la autoridad,
respecto de los temas vinculados a la hidrogeología del ICSARA 1 de la mencionada DIA.

**1.2** **ALCANCES Y OBJETIVOS**

El objetivo principal fue definir una red de monitoreo para el sistema acuífero presente en el
sector de la planta Ecobio, que permita detectar cambios de nivel y o calidad de las aguas
subterráneas durante la operación y cierre del Proyecto. Para ello se desarrolló un modelo
conceptual y numérico de flujo, y de movilidad de contaminante.

Para llevar a cabo lo anterior, se desarrollarán las siguientes tareas:

- Interpretación de trabajos de terreno ejecutados por Ecobio.

- Desarrollo de modelo conceptual de flujo.

- Desarrollo de modelo numérico de flujo, y movilidad de contaminante.

- Generación de escenarios de falla en RSU y CITA

- Diseño de red de monitoreo.

**1.3** **LOCALIZACIÓN**

El Relleno Sanitario y Centro Integral de Tratamiento Ambiental Fundo Las Cruces de Ecobio,
se ubican a 8 km al sur de la ciudad de Chillán Viejo, comuna de Chillán Viejo, región del Ñuble,
según se muestra de manera referencial en la Figura 1.3-1.

 - 7

INTRODUCCIÓN

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Fuente: Elaboración propia.

**Figura 1.3-1 Ubicación Proyecto Ecobio**

**1.4** **REFERENCIAS TÉCNICAS**

Para lleva a cabo el presente trabajo, se consideró la siguiente información:

 - **DGA, 2011:** Estudio Hidrogeológico Cuencas BioBio e Itata, Aquaterra, 2011.

 - **DGA, 2012:** Instalación de Piezómetros Operativos Región de la Araucanía hasta Región

Los Lagos, 2012.

 - **DGA, 2016:** Análisis Efecto en el Régimen Hídrico por Cambio en Patrones

Meteorológicos, HIDRICA Consultores, 2016.

 - **Ecobio, 1999.** Estudio de Impacto Ambiental Relleno Sanitario Fundo Las Cruces. Julio,

1999.

 - **Ecobio, 2003** : Estudio de Impacto Ambiental CITA, Fdo. Las Cruces, CIDEM Ltda.,

septiembre 2003.

 - **Ecobio, 2019** : Información de análisis de calidad histórica del agua subterránea

colectada en piezómetros de red de monitoreo.

 - 8

INTRODUCCIÓN

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

- **Ecobio, 2019b** : Información de los monitores subterráneos de niveles llevados a cabo

en 2019 en pozos nuevos, en el marco del presente trabajo, cuyos resultados se

adjuntan en el Anexo B.

- **Eximia, 2018** : Plano Topografía 2018, EXIMIA. Adjunto como Anexo C.

- **HIDRICA, 2017:** Evaluación de efectos sobre suelos, HIDRICA Consultores. Informe

Técnico en el marco de respuestas a observaciones realizada por la SMA mediante

Res.Ex.No4/ROL F-011-2017 al programa de cumplimiento.

- **Subgeo, 2019** : Supervisión perforación pozos planta Ecobio, Subgeo Ingeniería.

Adjunto como Anexo D.

- **VOLTA, 2019** : Disposición proyectada de RSU y CITA. Adjunto como Anexo E.

- **GAC, 2018** : Informe de Caracterización de Suelos - DIA Mejoramiento Integral de la

Gestión de Residuos Planta Ecobio.

- **GAC, 2018b** : Anexo 3 Caracterización Hidrológica, Hidrogeológica e Hidroquímica de

Aguas Subterráneas - DIA Mejoramiento del Sistema de Monitoreo de Aguas

Subterráneas del Relleno Sanitario Fundo Las Cruces y Relleno CITA.

- **VOLTA, 2018** : DIA Mejoramiento Integral de la Gestión de Residuos en Planta Ecobio,

VOLTA, agosto 2018. (En evaluación)

- **DS 148 (2004):** Reglamento Sanitario sobre Manejo de Residuos Peligrosos, Decreto

Supremo 148, 2004

- **EPA (1986):** RCRA Ground-Water Monitoring Technical Enforcement Guidance

Document, Environmental Protection Agency, 1986.

- **SEIA (2012):** [Guía para el Uso de Modelos de Aguas Subterráneas en el SEIA.](https://www.sea.gob.cl/sites/default/files/migration_files/guias/Guia_uso_modelo_aguas_subterraneas_seia.pdf)

 - 9

INTRODUCCIÓN

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

# CAPÍTULO 2 NUEVOS TRABAJOS DE TERRENO

Entre enero y marzo de 2019, se realizó la perforación de 4 pozos exploratorios en el sector de
estudio, con el objetivo de generar nueva información para caracterizar de manera adecuada
el sistema subterráneo; y cuyo informe de supervisión en terreno se presenta en el Anexo D.
En el presente capítulo se presenta e interpreta la información generada en terreno, que
permitió actualizar y complementar la información existente para el modelo conceptual.

**2.1** **PERFORACIONES REALIZADAS**

Los 4 piezómetros de exploración fueron perforados sobre los 30 metros de profundidad,
identificando al menos el estrato impermeable, bajo el acuífero intermedio. La ubicación de
éstos se muestra en la Figura 2.1-1, mientras que su profundidad, coordenadas y
especificaciones se presenta en la Tabla 2.1-1.

<!-- INICIO TABLA 2.1-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- MODELO HIDROGEOLÓGICO CONCEPTUAL Y NUMÉRICO RELLENOS RSU Y CITA -->

**Tabla 2.1-1: Ubicación y Características de Piezómetros****

| Piezómetro | Profundidad<br>Perforada<br>(m) | E UTM<br>WGS84<br>(m) | N UTM<br>WGS84<br>(m) | Altura<br>Brocal<br>(m) | Cota<br>(m s.n.m.) | Material | Diámetro | Habilitación<br>en Acuífero |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PM1-I | 33 | 751.363 | 5.935.782 | 1 | 113,2 | PVC | 6” | Intermedio |
| PM2-S | 42 | 751.982 | 5.935.640 | 1 | 114,9 | PVC | 6” | Superior |
| PM6-S | 40 | 751.597 | 5.935.971 | 1 | 113,8 | PVC | 6” | Superior |
| PM3-I | 42 | 753.187 | 5.934.975 | 1 | 118,0 | PVC | 6” | Intermedio |

<!-- Estadísticas: 4 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia a partir de Subgeo, 2019 La supervisión de la perforación estuvo a cargo de la empresa Subgeo Ingeniería, y la empresa perforista fue TECNIBOMBAS. La información de la supervisión de las perforaciones y ensayos -->
<!-- FIN TABLA 2.1-1 -->


Fuente: Elaboración propia.

**Figura 2.1-1 Ubicación de Piezómetros de Exploración Perforados**

 - 10

NUEVOS TRABAJOS DE TERRENO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

**Tabla 2.1-1 Ubicación y Características de Piezómetros**

|Piezómetro|Profundidad<br>Perforada<br>(m)|E UTM<br>WGS84<br>(m)|N UTM<br>WGS84<br>(m)|Altura<br>Brocal<br>(m)|Cota<br>(m s.n.m.)|Material|Diámetro|Habilitación<br>en Acuífero|
|---|---|---|---|---|---|---|---|---|
|PM1-I|33|751.363|5.935.782|1|113,2|PVC|6”|Intermedio|
|PM2-S|42|751.982|5.935.640|1|114,9|PVC|6”|Superior|
|PM6-S|40|751.597|5.935.971|1|113,8|PVC|6”|Superior|
|PM3-I|42|753.187|5.934.975|1|118,0|PVC|6”|Intermedio|

Fuente: Elaboración propia a partir de Subgeo, 2019

La supervisión de la perforación estuvo a cargo de la empresa Subgeo Ingeniería, y la empresa
perforista fue TECNIBOMBAS. La información de la supervisión de las perforaciones y ensayos
realizados, se detalla en el Anexo D.

El método de perforación utilizado correspondió a “perforación a percusión con cable”; el cual
puede aplicarse en cualquier tipo de material, desde las arcillas más blandas hasta las rocas
más duras. A pesar de que los métodos de perforación por rotación o rotopercusión son, en
términos generales, más rápidos, éstos tienen la desventaja del uso de fluidos de perforación
(barros, de cualquier tipo) que puede provocar sellos en las paredes alterando el ingreso de
agua en los pozos, y, en consecuencia, el monitoreo de éstos.

Así también, el método de percusión permite una mejor interpretación de la estratigrafía en
los testigos, dado que sólo agrega agua en cantidades controladas a la excavación para facilitar
la remoción de los materiales; a diferencia de los otros métodos, donde se incorpora una
cantidad de barro considerablemente mayor para la expulsión del material cortado por la

corona rotativa.

Por último, cabe mencionar que, como parte de los trabajos de terreno para caracterizar el
sistema acuífero del sector, se realizaron ensayos de infiltración durante el avance de la
perforación de los sondajes.

**2.2** **ESTRATIGRAFÍAS**

Los 4 piezómetros se perforaron hasta identificar al menos el estrato impermeable, bajo el
acuífero intermedio, independientemente si éstos quedarían habilitados en el acuífero
superior o intermedio, puesto que además fueron construidos con fines de exploración.

La interpretación estratigráfica realizada por el geólogo en terreno, considerando el método
de perforación, permitió identificar de manera más adecuada y con mayor precisión las
columnas litológicas de los sondajes. En este aspecto, la identificación de los tipos de
materiales que componen un estrato, junto con el porcentaje de contenido fino y/o arenas
asociados, permitió establecer con mayor exactitud los estratos que efectivamente
constituirían unidades acuíferas, respecto de aquellas que no.

 - 11

NUEVOS TRABAJOS DE TERRENO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

En términos generales en los 4 sondajes se identificaron los mismos estratos, a profundidades
y espesores similares, lo que indica una cierta uniformidad espacial del acuífero. En un primer
tramo, se identificó un horizonte compuesto por materiales asociados a depósitos de origen
volcanoclástico, seguidos de arenas limosas con importantes porcentajes de contenidos finos.
En términos hidrogeológicos, este estrato constituye una unidad prácticamente impermeable
o de muy baja permeabilidad, que ha sido catalogada como un acuitardo. Más en profundidad,
se identificó un primer acuífero (acuífero superior), conformado por arenas limpias de grano
fino a medio, con escasa presencia de gravas. Posteriormente se identificó otra capa de
materiales finos más impermeables, que presenta un comportamiento de acuitardo, formado
por secuencias limo-arcillosas y arenas arcillosas con importante presencia de limo.
Subyaciendo esta capa, se identificó un segundo acuífero (acuífero intermedio), conformado
por arenas de grano fino de baja plasticidad y humedad media a alta. Seguidamente, se
identificó una capa de arcillas limosas y limos areno-arcillosos, que conforman otro estrato del
tipo acuitardo. Finalmente, dos sondajes identificaron una tercera unidad acuífera (acuífero
inferior), compuesto por arenas finas a muy finas de plasticidad media a baja.

A modo de síntesis, en los siguientes puntos se indica la interpretación realizada en cada
sondaje.

 - **Sondaje PM1-I** : Se detectaron 3 estratos que pueden constituir unidades acuíferas

(acuífero superior, intermedio e inferior), ubicados en estratos de arena de grano fino
a medio, compacidad media y plasticidad baja a nula; de espesores de 2 metros para el
acuífero superior, y 5 metros en el acuífero intermedio. En el caso del acuífero inferior,
se traspasó 3 metros de manera de identificarlo.

El estrato acuitardo que sobreyace al acuífero superior, se compone de material de
origen volcanoclástico y limo-arcilloso, de espesor de 11 metros. El estrato acuitardo
que subyace el acuífero superior presenta una secuencia intercalada de limos y arcillas
junto a arenas limosas de color café, de un espesor de 10 metros. Por último, el
acuitardo que subyace el acuífero intermedio, se compone de un limo areno arcilloso,
de espesor de 2 metros.

 - **Sondaje PM2-S** : Se detectaron 2 estratos que pueden constituir unidades acuíferas

(acuífero superior e intermedio), desarrollados en capas de arena de grano fino a medio
con aislada presencia de gravas; de espesores de 6 metros para el acuífero superior, y

5 metros en el acuífero intermedio.

El estrato acuitardo por sobre el acuífero superior contiene material de origen
volcanoclástico y limo arcilloso, de espesor de 13 metros. El estrato acuitardo que
sobreyace el acuífero intermedio, contiene limos y arcillas arenosas (de grano fino) de
humedad media a alta y consistencia media, con un espesor de 17 metros. Por último,
el acuitardo que subyace al acuífero intermedio se compone de limo areno arcilloso.

 - 12

NUEVOS TRABAJOS DE TERRENO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

 - **Sondaje PM6-S** : Se detectaron 2 estratos que constituyen unidades acuíferas (acuífero

superior e intermedio), ubicados en estratos de arena de grano fino a medio, de
espesores de 4 metros cada uno.

El estrato acuitardo que sobreyace al acuífero superior, se compone de material de
volcánico tipo lahar y arenas limo-arcillosas, de espesor de 12 metros. El estrato
acuitardo que subyace el acuífero superior, presenta intercalaciones de limo arenoarcilloso y arcillas limosas de color gris oscuro, con un espesor de 18 metros. Por último,
el acuitardo que subyace al acuífero intermedio se compone de arcilla limosa.

 - **Sondaje PM3-I** : Se detectaron 3 estratos que pueden constituir unidades acuíferas

(acuífero superior, intermedio e inferior), ubicados en estratos de arena de grano
medio a fino, de espesores de 4 metros. Para identificar el acuífero inferior, la
perforación se continuó por 2 metros de manera de identificarlo.

El acuitardo por sobre el acuífero superior contiene material de origen volcanoclástico
y limo arcilloso, de espesor de 12 metros. El estrato acuitardo que sobreyace el acuífero
intermedio, contiene limo areno-arcilloso y arcillas limosas de alta humedad, con un
espesor de 17 metros. Por último, el acuitardo que subyace el acuífero intermedio, se
compone de arcilla limosa color gris de plasticidad y humedad igualmente alta, de
espesor de 3 metros.

Conforme a la información descrita, en la Figura 2.1-1 se presentan los perfiles estratigráficos
de los 2 sondajes exploratorios habilitados en el acuífero intermedio, y en la Figura 2.2-2 se
presentan los perfiles estratigráficos de los 2 sondajes exploratorios habilitados en el acuífero
superior.

 - 13

NUEVOS TRABAJOS DE TERRENO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Fuente: Elaboración propia a partir de Subgeo, 2019

NUEVOS TRABAJOS DE TERRENO

**Figura 2.2-1 Resumen Estratigrafías Sondajes de Exploración Habilitados en Acuífero Intermedio**

 - 14

MODELO HIDROGEOLÓGICO CONCEPTUAL Y NUMÉRICO RELLENOS RSU Y CITA

Fuente: Elaboración propia a partir de Subgeo, 2019

NUEVOS TRABAJOS DE TERRENO

**Figura 2.2-2 Resumen Estratigrafías Sondajes de Exploración Habilitados en Acuífero Superficial**

 - 15

MODELO HIDROGEOLÓGICO CONCEPTUAL Y NUMÉRICO RELLENOS RSU Y CITA

**2.3** **INTERPRETACIÓN DE ENSAYOS SLUG TEST**

Para generar más información útil que permitiera caracterizar el sistema acuífero, se realizaron
ensayos de infiltración durante el avance de las perforaciones, y determinar así la
permeabilidad de los estratos que fueron identificados. El detalle de los trabajos de terreno se
presenta en el Anexo D; mientras que en Tabla 2.3-1 se resume la cantidad de ensayos,
presentando la profundidad a la que fueron realizados y los estratos considerados.

**Tabla 2.3-1 Resumen de Ensayos Slug Test Realizados**

|Pozo|Ensayos|Rango Ensayos (m)|Col4|Acuitardo<br>Superficial|Acuífero<br>Superior|Acuitardo<br>Intermedio|Acuífero<br>Intermedio|Acuitardo<br>Inferior|Acuífero<br>Inferior|
|---|---|---|---|---|---|---|---|---|---|
|**Pozo**|**Ensayos**|**Inicio**|**Fin**|**Fin**|**Fin**|**Fin**|**Fin**|**Fin**|**Fin**|
|PM1-I|6|7|30|X|X|X|X||X|
|PM2-S|7|3|37|X|X|X|X|||
|PM3-I|7|4|40|X|X|X|X|X||
|PM6-S|6|6|35|X|X|X|X|||

Fuente: Elaboración propia a partir de Subgeo, 2019

**2.3.1** **Metodología de Interpretación**

La interpretación de las pruebas de inyección se realizó mediante el software
Aquifer Test 2011.1, mediante la siguiente metodología.

 - Se ingresan variables de entrada al software: datos de campo obtenidos en las pruebas

de inyección (altura de agua v/s tiempo). Además, valores de la geometría de los
sondajes, conforme a lo estipulado en el Informe de Supervisión de Perforación
(Anexo D).

 - Se ajusta una recta a los datos de campo en el gráfico generado por Aquifer Test, tal

como se muestra en la Figura 2.3-1 . Para esto se debe elegir los métodos de análisis
de Bouwer and Rice y Hvorslev.

 - Finalmente, se registran los valores de conductividad hidráulica calculados por

Aquifer Test.

De esta manera, los resultados de terreno fueron ingresados a Aquifer Test y se analizaron
las curvas de descenso de nivel de agua en cada caso.

 - 16

NUEVOS TRABAJOS DE TERRENO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Fuente: Elaboración propia.

**Figura 2.3-1 Recta de Ajuste a Datos de Campo**

**2.3.2** **Resultados**

Los resultados obtenidos mediante ambos métodos fueron coincidentes entre sí, por lo cual
se consideró el promedio aritmético de ambos como representativo del medio acuífero. De
esta manera, los valores de permeabilidad se resumen en la Tabla 2.3-2.

<!-- INICIO TABLA 2.3-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Los resultados obtenidos mediante ambos métodos fueron coincidentes entre sí, por lo cual se consideró el promedio aritmético de ambos como representativo del medio acuífero. De esta manera, los valores de permeabilidad se resumen en la Tabla 2.3-2. -->

**Tabla 2.3-2: Resumen de Permeabilidades Determinadas con Slug Test****

| Estrato | Permeabilidad (m/d) | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Estrato** | **PM1-I** | **PM2-S** | **PM3-I** | **PM6-S** |
| Acuitardo Superficial | 0,30 | 1,36 | 1,32 | 0,88 |
| Acuífero Superior | 1,65 | 5,55 | 4,15 | 2,85 |
| Acuitardo Intermedio | 0,55 | 0,96 | 0,68 | 1,94 |
| Acuífero Intermedio | 1,69 | 5,17 | 1,89 | 2,91 |
| Acuitardo Intermedio | - | - | 1,12 | - |
| Acuífero Inferior | 2,05 | - | - | - |

<!-- Estadísticas: 7 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Los resultados presentados permiten verificar la diferencia entre los estratos y la conceptualización realizada, identificándose acuitardos de menor permeabilidad frente a lo -->
<!-- FIN TABLA 2.3-2 -->


**Tabla 2.3-2 Resumen de Permeabilidades Determinadas con Slug Test**

|Estrato|Permeabilidad (m/d)|Col3|Col4|Col5|
|---|---|---|---|---|
|**Estrato**|**PM1-I**|**PM2-S**|**PM3-I**|**PM6-S**|
|Acuitardo Superficial|0,30|1,36|1,32|0,88|
|Acuífero Superior|1,65|5,55|4,15|2,85|
|Acuitardo Intermedio|0,55|0,96|0,68|1,94|
|Acuífero Intermedio|1,69|5,17|1,89|2,91|
|Acuitardo Intermedio|-|-|1,12|-|
|Acuífero Inferior|2,05|-|-|-|

Fuente: Elaboración propia.

Los resultados presentados permiten verificar la diferencia entre los estratos y la
conceptualización realizada, identificándose acuitardos de menor permeabilidad frente a lo
estimado en los sectores acuíferos. Sin embargo, respecto a la determinación de las
permeabilidades de cada estrato, la metodología de Slug Test se considera referencial, siendo
finalmente estimadas mediante las pruebas de bombeo analizadas en el acápite siguiente.

 - 17

NUEVOS TRABAJOS DE TERRENO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

**2.4** **INTERPRETACIÓN DE PRUEBAS DE BOMBEO Y RECUPERACIÓN**

Se realizaron pruebas de bombeo y recuperación, de manera de determinar las contantes
elásticas de los acuíferos identificados en los sondajes exploratorios; esto es, transmisividad,
permeabilidad y coeficientes de almacenamiento.

Dada las características de los materiales que constituyen los acuíferos, las pruebas a gasto
constante se ejecutaron con caudales bajos, de manera de no “secar” los sondajes. El detalle
de los trabajos de terreno se presenta en el Anexo D.

**2.4.1** **Metodología de Interpretación**

Para el proceso de análisis se utilizó el software Aquifer Test 2011, en donde se analizaron
cuatro métodos: Theis, Theis con corrección de Jacob, Cooper - Jacob I, y Recuperación de
Theis; los cuales se resumen brevemente:

**Método de Theis**

El método analítico desarrollado por Theis considera un modelo conceptual para la
extracción de agua desde un acuífero confinado, con las siguientes hipótesis:

 - El acuífero posee extensión horizontal infinita y el espesor saturado es constante.

 - El pozo de bombeo penetra completamente el espesor saturado del acuífero.

 - El acuífero se encuentra siempre bajo condiciones de presión (acuífero confinado).

 - El acuífero es homogéneo e isotrópico.

 - El radio del pozo es muy pequeño comparado con las dimensiones del acuífero.

 - El agua bombeada desde el pozo proviene de una liberación instantánea desde

almacenamiento elástico del acuífero confinado.

 - El descenso es despreciable comparado con el espesor saturado del acuífero.

Este método puede ser utilizado para el análisis de un solo pozo o en conjunto con pozos

de observación.

**Método de Theis con Corrección de Jacob**

La corrección de Jacob permite utilizar el análisis de Theis en acuíferos no confinados. Jacob
propone aplicar la siguiente corrección a los datos de descenso medidos:

Donde:

_s’_ = Descenso corregido (m)
_s_ = Descenso medido (m)
_Ho_ = Espesor del acuífero (m)

NUEVOS TRABAJOS DE TERRENO

s [2]
s [′] = s−

s∗H 0

 - 18

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

**Cooper- Jacob I: Método Tiempo - Descenso**
Este método es una simplificación del método de Theis, utilizado para el estudio con radios
de análisis pequeños o tiempos de bombeo largo; considerando las siguientes hipótesis:

- El acuífero posee extensión horizontal infinita y el espesor saturado (b) es constante.

- El pozo de bombeo penetra completamente el espesor saturado del acuífero.

- El acuífero se encuentra siempre bajo condiciones de presión (acuífero confinado).

- El acuífero es homogéneo e isotrópico.

- El radio del pozo es muy pequeño comparado con las dimensiones del acuífero

- El agua bombeada desde el pozo proviene de una liberación instantánea desde

almacenamiento elástico del acuífero confinado.

- El descenso es despreciable comparado con el espesor saturado del acuífero.

- El caudal bombeado es constante.

En este método las transmisividades y almacenamiento se calculan como se muestra a

continuación:

[2,3 Q]

4π∆s [ S= 2,25 Tt] r 2 [0]

T= [2,3 Q]

2

r
0

Donde:
_T_ = Transmisividad (m [2] /d)
_Q_ = Caudal bombeado (m [3] /d)
_Δs_ = Diferencia de descenso medido (m)

_S_ = Almacenamiento
_T_ = Transmisividad (m [2] /d)
_t_ _0_ = Tiempo correspondiente a la intersección de la recta modelada con descenso nulo.
_r_ _0_ _[2]_ = Distancia correspondiente a la intersección de la recta modelada con descenso nulo.

Al igual que el método de Theis, esta solución puede ser utilizada para el análisis de un solo
pozo de bombeo o en conjunto con pozos de observación.

**Método Recuperación de Theis**
Este método es utilizado para analizar los datos obtenidos durante la prueba de
recuperación, los cuales pueden pertenecer al pozo de bombeo o a pozos de observación.
Dado que es un método basado en la metodología original de Theis para pruebas de
bombeo, la solución posee las mismas hipótesis planteadas anteriormente.

**2.4.2** **Resultados**

A continuación, en la Tabla 2.4-1, Tabla 2.4-2 se muestra un resumen de los resultados
obtenidos mediante las metodologías descritas. Se consideró como representativo el
promedio de los valores determinados, debido a que éstos son similares entre sí, o son del
mismo orden de magnitud. No se determinaron valores de coeficientes de almacenamiento
en las pruebas de bombeo, debido a que éstas fueron realizadas evaluando el descenso del

 - 19

NUEVOS TRABAJOS DE TERRENO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

nivel en el mismo pozo bombeado; sumando pérdidas de carga y un escurrimiento no lineal
que no permiten una correcta interpretación de esta variable.

**Tabla 2.4-1 Resumen de Transmisividades (m** **[2]** **/d)**

|Método|PM1-I|PM2-S|PM3-I|PM6-S|
|---|---|---|---|---|
|Theis|1,61|-|1,11|0,84|
|Theis Jacob|2,00|-|1,41|1,33|
|Cooper Jacob I|1,62|-|1,73|2,09|
|Theis Recovery|1,92|0,97|2,09|4,83|
|Promedio<br>|1,79|0,97|1,59|2,27|

Fuente: Elaboración Propia

**Tabla 2.4-2 Resumen de Permeabilidades (m/d)**

|Método|PM1-I|PM2-S|PM3-I|PM6-S|
|---|---|---|---|---|
|Theis|0,32|-|0,28|0,21|
|Theis Jacob|0,40|-|0,35|0,33|
|Cooper Jacob I|0,32|-|0,43|0,52|
|Theis Recovery|0,38|0,16|0,52|1,21|
|Promedio<br>|0,36|0,16|0,40|0,57|

Fuente: Elaboración Propia

 - 20

NUEVOS TRABAJOS DE TERRENO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

# CAPÍTULO 3 MODELO CONCEPTUAL DE FLUJO

En el presente capítulo se presenta el Modelo Conceptual del sistema acuífero, el cual
incorpora la nueva información de terreno descrita en el capítulo anterior junto con la de

estudios anteriores.

**3.1** **INFORMACIÓN DE CALICATAS REALIZADAS EN ESTUDIOS ANTERIORES**

Para complementar la información generada en los trabajos de terreno, se presenta un
resumen de la información de calicatas realizadas entre 2017 y 2018 en la propiedad de Ecobio.

- **HIDRICA, 2017** : En julio de 2017 se realizaron 8 prospecciones en la propiedad de Ecobio,

en el marco del estudio “Evaluación de Efectos Sobre Suelos”. La ubicación de los puntos
muestreados se presenta en la Figura 3.1-1, y se ubican próximos lugares de operación de

la Planta.

Fuente: HIDRICA, 2017.

**Figura 3.1-1 Ubicación de Calicatas Realizadas en HIDRICA, 2017**

 - 21

MODELO CONCEPTUAL DE FLUJO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

En lo que respecta a información que describe el suelo, se indica que no fue posible
realizar calicatas de 2,0 metros en todas las prospecciones, debido a la presencia de un
estrato de suelo no excavable de origen volcánico. Debido a lo anterior, sólo fue posible
perforar 1 metro con la máquina.

 - **GAC, 2018** : Entre enero y abril de 2018 se realizaron 6 calicatas, con profundidades

aproximadas entre 25 y 129 cm, en el marco del “Informe de Caracterización de
Suelos”; cuyas ubicaciones se muestran en la Figura 3.1-2. Según se indica en el
documento, la caracterización física se desglosa principalmente:

`o` **Mollisol:** presenta horizontes superficiales con alto contenido de materia

orgánica.
`o` **Andisol:** formado a partir del proceso de meteorización que generan

minerales, que tienen capacidad de retención de agua. Pueden ser suelos
poco meteorizados con cristales volcánicos hasta muy meteorizados;

esencialmente asociados a materiales volcánicos.

`o` **Vertisol:** alto contenido mineral arcillo expansible, con pronunciados cambios

de volumen ante cambios de humedad, transmitiendo agua muy lentamente

En resumen, se indica que son suelos de clases texturales medias y finas en los
horizontes superficiales (franca arcillosa, franca, franca arcillosa limosa) que se hacen
más finas hacia los horizontes más profundos, inmediatamente sobre la toba, llegando
a textura arcillosa. La toba se encontró entre los 110-130 cm, y entre los 50 y 80 cm.

Fuente: GAC, 2018.

**Figura 3.1-2 Ubicación de Calicatas Realizadas en GAC, 2018**

 - 22

MODELO CONCEPTUAL DE FLUJO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

- **GAC, 2018b** : En el marco de la presente DIA, se realizaron 4 calicatas al poniente de la

proyección actual del CITA, según se muestra en la Figura 3.1-3.

Fuente: GAC, 2018b.

**Figura 3.1-3 Ubicación de Calicatas Realizadas en GAC, 2018b**

Los suelos identificados corresponden a textura fina a muy fina, de baja permeabilidad
moderada a moderadamente lenta, ubicados sobre un sustrato constituido por
conglomerado volcánico de composición petrográfica mixta y muy meteorizada. En
resumen, se indica que los suelos han sufrido una degradación de sus propiedades físicas,
tales como estructura, porosidad, y capacidad de drenaje.

**3.2** **ESTRATOS Y ACUÍFEROS RECONOCIDOS**

**3.2.1** **Geometría**

A partir de la interpretación y correlación de la información obtenida de los sondajes de
exploración, descritos en el Capítulo 2, la información de prospecciones realizadas entre
2017 y 2018, el potencial de las litologías para almacenar y transmitir agua, complementado
con los resultados de pruebas en terreno; fue posible identificar tres estratos que pueden
constituir acuíferos, intercalados entre capas impermeables compuestas de secuencias limo
arcillosas, de importante porcentaje de contenido de finos.

En términos generales, el primer horizonte, de aproximadamente 12 metros de
profundidad, destaca por la presencia de materiales principalmente finos, tipo limoarcilloso, asociado a depósitos de origen volcanoclástico, llamado lahar, de compacidad
muy densa y plasticidad nula, seguidas de arenas limosas con importantes porcentajes de
contenidos finos (40-45%), e intercalaciones de limos y arcillas arenosas de grano fino. Esta

 - 23

MODELO CONCEPTUAL DE FLUJO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

configuración litológica, en términos hidrogeológicos es prácticamente impermeable, y
constituye un **acuitardo** de muy baja permeabilidad.

Siguiendo en profundidad, se identifica un **primer acuífero (acuífero superior)** de entre 2 y
6 metros de espesor, conformado por arenas limpias de grano fino a medio (80-90% de
arena), con escasa presencia de gravas y de baja plasticidad. Dicho estrato, se caracteriza
como la principal potencia acuífera del sistema.

Subyaciendo el acuífero superior se identifica una capa de materiales finos, que presenta
un comportamiento de **acuitardo**, formado por secuencias limo-arcillosas y arenas
arcillosas con importante presencia de limo; del cual es identificaron espesores entre 10 y
17 metros. La permeabilidad de este segundo acuitardo es mayor a la del somero, debido a
que dicho estrato presenta una alta compacidad (muy denso), principalmente dada por la
existencia de sedimentos de origen volcanoclástico recientes.

Más en profundidad se identificó un **segundo acuífero (acuífero intermedio)**, conformado
por arenas de grano fino de baja plasticidad y humedad media a alta, de entre 4 y 5 metros
de espesor. La permeabilidad de este estrato es inferior a la del acuífero superior, debido a
la diferencia entre el tamaño de grano entre ambas arenas.

Seguidamente, se identificó una capa de arcillas limosas y limos arenosos, que conforman
un estrato **acuitardo**, de entre 2 y 3 metros; de similares características físicas al acuitardo

identificado sobre el acuífero intermedio.

Finalmente, dos sondajes identificaron una **tercera unidad acuífera (acuífero inferior)**,
compuesto por arenas finas a muy finas de plasticidad media a baja y humedad alta.

Es importante destacar que esta nueva conceptualización del sistema acuífero ha sido
realizada con mayor cantidad de información y de mucho mejor calidad que la realizada en
el contexto de la Línea Base del Estudio de Impacto Ambiental del Proyecto denominado
“Centro Integral del Tratamiento Ambiental Fundo Las Cruces” (Ecobio, 2003). En esta
nueva información se destaca la perforación exploratoria con un método de perforación
que permite identificar de manera precisa los estratos que efectivamente constituyen
acuíferos, y aquellos que corresponden a unidades acuitardo.

**3.2.2** **Parámetros Hidráulicos**

El flujo de agua subterránea a través del sistema está determinado por los parámetros
hidráulicos de los acuíferos, por lo que su caracterización es fundamental para el
entendimiento del sistema. A partir de la identificación de los estratos acuíferos y
acuitardos en el sistema, pruebas de permeabilidad y bombeo realizadas, junto a
información de características de los suelos del proyecto “Centro Integral del Tratamiento
Ambiental Fundo Las Cruces” (Ecobio, 2003); se asignaron rangos de permeabilidad para los

 - 24

MODELO CONCEPTUAL DE FLUJO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

estratos identificados. En las Tabla 3.2-1, Tabla 3.2-2 y Tabla 3.2-3 se resumen los
parámetros hidráulicos y geometría de los acuíferos y acuitardos.

**Tabla 3.2-1 Resumen de Permeabilidad de Sistemas Acuíferos Identificados**

|Acuífero|Profundidad Aproximada<br>desde Terreno (m)|Espesor<br>(m)|Permeabilidad<br>Pruebas Terreno<br>(m/d)|Permeabilidad<br>Bibliografía (**)<br>(m/d)|
|---|---|---|---|---|
|Acuífero Superior|Desde 11 - 13|2 - 6|0,16 - 1,21|1 - 100|
|Acuífero Intermedio|Desde 23 - 36|4 - 5|0,28 - 0,52|0,01 - 1|
|Acuífero Inferior|Desde 30 - 40|2 (*)|-|0,01 - 1|

Nota: (*) Al menos espesor indicado. Perforista lo identifica y se deja de perforar.
Nota: (**) Fetter, C. W. (2001) - Applied Hydrogeology. Prentice-Hall, 4a ed., 598 pp.
Fuente: Elaboración Propia

**Tabla 3.2-2 Resumen de Coeficientes de Almacenamiento de Sistemas Acuíferos**

**Identificados**

|Acuífero|Profundidad Aproximada<br>desde Terreno (m)|Espesor<br>(m)|Almacenamiento<br>Bibliografía (**)|
|---|---|---|---|
|Acuífero Superior|Desde 11 - 13|2 - 6|10-04 - 10-03|
|Acuífero Intermedio|Desde 23 - 36|4 - 5|10-04 - 10-03|
|Acuífero Inferior|Desde 30 - 40|2 (*)|10-04 - 10-03|

Nota: (*) Al menos espesor indicado. Perforista lo identifica y se deja de perforar.
Nota: (**) Villanueva, M., e Iglesias, A. (1984) Pozos y acuíferos. Técnicas de evaluación mediante ensayos de bombeo. Instituto Geológico y
Minero Español (IGME). Madrid, 426 pp.
Fuente: Elaboración Propia

Es importante destacar que las permeabilidades de los acuíferos, en particular del intermedio,
son relativamente bajas, y se asocian a acuíferos pobres, de bajo rendimiento como productor
de agua. Esto concuerda con lo establecido en DGA (2011), en donde se indica que pozos
aproximadamente 10 km al oriente del área de estudio presentan baja permeabilidad a
moderada, en 50 m de perforación.

**Tabla 3.2-3 Resumen de Permeabilidad de Acuitardos Identificados**

|Acuitardo|Profundidad Aproximada<br>desde Terreno (m)|Espesor<br>(m)|Permeabilidad<br>Pruebas Terreno<br>(m/d)|Permeabilidad<br>Bibliografía (**)<br>(m/d)|
|---|---|---|---|---|
|Acuitardo Superior|-|11 - 13|-|10-04 - 10-01|
|Acuitardo Intermedio|Desde 13 - 19|10 - 18|-|10-04 - 10-01|
|Acuitardo Inferior|Desde 28 - 41|2 - 3|-|10-04 - 10-01|

Nota: (**) Custodio, E., M.R. Llamas, (1983). Hidrología subterránea. Ed. Omega. Barcelona. 2 V
Fuente: Elaboración Propia

**3.3** **NIVEL PIEZOMÉTRICO Y CONCEPTUALIZACIÓN DE FLUJO**

Una vez habilitados los nuevos pozos de monitoreo, se realizaron, entre el 26 de febrero y 11
de abril, 2 monitoreos de niveles piezométricos junto a la medición del nivel estático previo a
la realización de la prueba de bombeo, cuyos resultados se muestran en Tabla 3.3-1 y la Tabla

 - 25

MODELO CONCEPTUAL DE FLUJO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

3.3-2. La ubicación espacial de los pozos se presenta en la Figura 2.1-1. Los pozos PM3-I y
PM1-I monitorean el acuífero intermedio, mientras que los pozos PM6-S y PM2-S monitorean
el acuífero superior.

De la Tabla 3.3-1, al comparar la profundidad al nivel piezométrico con la información de los
perfiles estratigráficos de la Figura 2.2-1, se aprecia que el nivel de agua subterránea en los
pozos está por sobre el tope de los acuíferos que son monitoreados, es decir, se trata de un
sistema con acuíferos confinados. En particular, en los 4 pozos el nivel de energía se encuentra
ubicado en el acuitardo superficial, el cual actuaría como estrato confinante.

**Tabla 3.3-1 Resumen de Profundidad a Niveles Piezométrico en Nuevos Pozos de**

**Monitoreo**

|Campaña|PM3-I|Col3|PM1-I|Col5|PM6-S|Col7|PM2-S|Col9|
|---|---|---|---|---|---|---|---|---|
|Campaña|Acuífero Intermedio|Acuífero Intermedio|Acuífero Intermedio|Acuífero Intermedio|Acuífero Superior|Acuífero Superior|Acuífero Superior|Acuífero Superior|
|Campaña|Fecha|Prof. Nivel<br>(m)|Fecha|Prof. Nivel<br>(m)|Fecha|Prof. Nivel<br>(m)|Fecha|Prof. Nivel<br>(m)|
|1|08-mar|11,5|26 -feb|9,7|07-mar|9,6|27-feb|9,8|
|2|01-abr|11,1|01-abr|8,2|01-abr|8,1|01-abr|8,6|
|3 <br>|11-abr<br>|10,0|11-abr|8,4|11-abr|8,2|11-abr|9,1|

Fuente: Elaboración Propia

**Tabla 3.3-2 Resumen de Niveles Piezométricos en Nuevos Pozos de Monitoreo**

|Campaña|PM3-I|Col3|PM1-I|Col5|PM6-S|Col7|PM2-S|Col9|
|---|---|---|---|---|---|---|---|---|
|Campaña|Acuífero Intermedio|Acuífero Intermedio|Acuífero Intermedio|Acuífero Intermedio|Acuífero Superior|Acuífero Superior|Acuífero Superior|Acuífero Superior|
|Campaña|Fecha|Cota Nivel<br>(m s.n.m.)|Fecha|Cota Nivel<br>(m s.n.m.)|Fecha|Cota Nivel<br>(m s.n.m.)|Fecha|Cota Nivel<br>(m s.n.m.)|
|1|08-mar|107,5|26 -feb|104,5|07-mar|105,2|27-feb|106,0|
|2|01-abr|106,9|01-abr|105,0|01-abr|105,7|01-abr|106,3|
|3 <br>|11-abr<br>|108,0|11-abr|104,8|11-abr|105,6|11-abr|105,8|

Fuente: Elaboración Propia

Complementando lo anterior, se observa que el sector norponiente, donde se ubican los pozos
PM1-I (acuífero intermedio), y los pozos PM6S y PM2-S (acuífero superior), presentan un nivel
de energía similar; y en particular la diferencia entre el acuífero superior e intermedio, difiere
muy poco, aproximadamente entre 70 y 80 cm. Esta configuración daría cuenta de una posible
interconexión entre el acuífero superior e intermedio, aguas arriba de la zona en estudio,
donde la capa acuitardo limo-arcilloso no existiría o estaría reducida, generándose un único
nivel piezométrico entre ambos acuíferos, o, el mismo nivel de energía en ambos acuíferos.

Esta conceptualización de flujo se complementa con los resultados del monitoreo de niveles
llevados a cabo por Ecobio en los antiguos pozos construidos en la propiedad, presentado en
la Tabla 3.3-1. Estos pozos cuentan con profundidades de 8 metros, por lo que sólo

<!-- INICIO TABLA 3.3-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- perfiles estratigráficos de la Figura 2.2-1, se aprecia que el nivel de agua subterránea en los pozos está por sobre el tope de los acuíferos que son monitoreados, es decir, se trata de un sistema con acuíferos confinados. En particular, en los 4 pozos el nivel de energía se encuentra ubicado en el acuitardo superficial, el cual actuaría como estrato confinante. -->

**Tabla 3.3-1: Resumen de Profundidad a Niveles Piezométrico en Nuevos Pozos de****

| Campaña | PM3-I | Col3 | PM1-I | Col5 | PM6-S | Col7 | PM2-S | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Campaña | Acuífero Intermedio | Acuífero Intermedio | Acuífero Intermedio | Acuífero Intermedio | Acuífero Superior | Acuífero Superior | Acuífero Superior | Acuífero Superior |
| Campaña | Fecha | Prof. Nivel<br>(m) | Fecha | Prof. Nivel<br>(m) | Fecha | Prof. Nivel<br>(m) | Fecha | Prof. Nivel<br>(m) |
| 1 | 08-mar | 11,5 | 26 -feb | 9,7 | 07-mar | 9,6 | 27-feb | 9,8 |
| 2 | 01-abr | 11,1 | 01-abr | 8,2 | 01-abr | 8,1 | 01-abr | 8,6 |
| 3 <br> | 11-abr<br> | 10,0 | 11-abr | 8,4 | 11-abr | 8,2 | 11-abr | 9,1 |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia **Tabla 3.3-2 Resumen de Niveles Piezométricos en Nuevos Pozos de Monitoreo** -->
<!-- FIN TABLA 3.3-1 -->

monitorearían la posible agua almacenada en el acuitardo. De acuerdo a los registros, todos
los pozos se encontraron secos, lo que concuerda con los resultados expuestos en la Tabla

 - 26

MODELO CONCEPTUAL DE FLUJO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

3.3-1. Al respecto, cabe mencionar que el acuitardo superficial es de muy baja permeabilidad,
pudiendo almacenar y transmitir agua a una tasa muy reducida a casi nula, lo que justifica que

esos pozos se encuentren secos.

**Tabla 3.3-3 Resumen de Profundidad a Niveles Piezométrico en Antigua Red de Monitoreo**

|Piezómetro|E WGS84<br>(m)|N WGS84<br>(m)|Fecha<br>Monitoreo|Prof Nivel<br>(m)|
|---|---|---|---|---|
|Prsu4|752.528|5.935.117|01-04-2019|Seco|
|PC1|751.980|5.935.644|01-04-2019|Seco|
|PC2|751.725|5.935.700|01-04-2019|Seco|
|P1|752.275|5.935.173|01-04-2019|Seco|
|PC4|751.628|5.935.339|01-04-2019|Seco|
|PC3<br>|751.889<br>|5.935.265|01-04-2019|Seco|

Fuente: Elaboración Propia

Conforme a lo anterior, en la Figura 3.3-1 se presenta la interpretación espacial de las cotas de
nivel piezométrico en el sistema, representadas mediante un mapa de isopiezas. Estas se
realizaron con la última fecha de medición de nivel, que se ha considerado como la medición
más representativa, puesto que toma en cuenta más de un mes de estabilización de los niveles
en los pozos, desde su fecha de construcción.

Fuente: Elaboración Propia

**Figura 3.3-1 Isopiezas Estimadas y Dirección de Flujo en Sistema Subterráneo (abril 2019)**

 - 27

MODELO CONCEPTUAL DE FLUJO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

De la Figura 3.3-1 se evidencia que la dirección preferencial de flujo del sistema es desde el
suroriente hacia el norponiente, con un gradiente de flujo natural estimado de 0,16%.

Por último, en la Figura 3.3-3 se presenta el perfil transversal que atraviesa la propiedad de
Ecobio, desde PM3-I a PM1-I, y cuya planta se presenta en la Figura 3.3-2. En éste se muestra
la interpretación espacial de la litología identificada en los nuevos pozos perforados, donde se
reconocen los 3 estratos de material sedimentario que definen los acuíferos presentes en el
área de emplazamiento del proyecto, y los 3 estratos acuitardos confinantes, que se extienden
de manera solidaria en diferentes niveles. Del mismo modo, se aprecia la cota del nivel
piezométrico, ubicada por sobre los estratos acuíferos, y bajo los antiguos pozos habilitados
en el estrato acuitardo superficial. En el perfil transversal se muestran los sondajes
identificados en la Figura 3.3-2, proyectados sobre el perfil A-A ́.

Fuente: Elaboración Propia

**Figura 3.3-2 Trazado en Planta de Perfil en Ecobio**

 - 28

MODELO CONCEPTUAL DE FLUJO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Fuente: Elaboración Propia
Nota: (PROYECCIÓN) indica que ubicación de piezómetro es proyectada sobre el Perfil A-A ́

**Figura 3.3-3 Perfil Transversal de Sistema Subterráneo en Ecobio**

 - 29

MODELO CONCEPTUAL DE FLUJO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y NUMÉRICO RELLENOS RSU Y CITA

**3.4** **DOMINIO MODELO CONCEPTUAL**

El dominio del modelo se definió de manera de incluir el sistema hidrogeológico presente en
sector de la planta de Ecobio, incluyendo las proyecciones del RSU y CITA al 2033. Asimismo,
se consideró la representación del sistema de flujos subterráneos elaborado en el “Estudio
Hidrogeológico Cuencas Bio Bio e Itata” (DGA, 2011), a partir del cual se establecieron los
límites del dominio en función de los niveles de agua subterránea regionales. En particular, en
dicho estudio se determinaron curvas equipotenciales para el acuífero del río Itata, con las que
se definieron las condiciones de borde para el modelo conceptual DGA (2011). Como
resultado, se obtuvieron isopiezas regionales, que en el área de estudio indican un sentido de
flujo suroriente-norponiente, lo cual concuerda con lo indicado en el acápite 3.3, según se
muestra en la Figura 3.4-1.

Fuente: Elaboración Propia a partir de DGA (2011).

**Figura 3.4-1 Isopiezas y Dirección de Flujo Regional**

De esta forma, el dominio del modelo conceptual se definió en el sentido del flujo regional, de
manera de independizar dos bordes del modelo con una condición de no flujo, según se indica
en la Figura 3.4-2. Con esta consideración, el dominio del modelo conceptual abarca un área
de 12,5 km [2], dado por:

- **Norponiente:** 1,5 km aguas abajo de la propiedad de Ecobio, con un flujo de salida por el

sistema acuífero.

 - 30

MODELO CONCEPTUAL DE FLUJO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

- **Nororiente:** limitado por una barrera de no flujo, dada por el sentido de flujo regional.

- **Suroriente:** 1,5 km aguas arriba de la propiedad de Ecobio, con un flujo de entrada en el

sistema acuífero.

- **Surponiente:** limitado por una barrera de no flujo, dada por el sentido de flujo regional.

- **Límite superior:** nivel de terreno.

- **Límite Inferior:** acuitardo bajo el acuífero intermedio, ubicado a una profundidad por

sobre los 23 metros, de acuerdo a la estratigrafía.

Fuente: Elaboración Propia

**Figura 3.4-2 Dominio Modelo Conceptual**

**3.5** **ZONAS DE RECARGA Y DESCARGA**

El modelo conceptual considera las siguientes entradas y salidas de flujo.

**3.5.1** **Flujo Subterráneo de Entrada**

El flujo subterráneo de entrada se estimó mediante la ecuación de la Ley de Darcy, que
describe el flujo pasante por medios poroso. Para esto se definió una sección rectangular
de control, en las potencias de los acuíferos superior e intermedio. La permeabilidad se
estimó como un promedio de ambos estratos, y se consideró el gradiente regional para la
estimación del flujo. El resumen de la estimación se presenta en la Tabla 3.5-1.

<!-- INICIO TABLA 3.5-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- MODELO HIDROGEOLÓGICO CONCEPTUAL Y NUMÉRICO RELLENOS RSU Y CITA -->

**Tabla 3.5-1: Flujo Subterráneo de Entrada a Modelo Conceptual****

| K equivalente<br>(m/d) | i<br>(m/m) | A<br>(m) | Q<br>(l/s) |
| --- | --- | --- | --- |
| 0,55 | 0,0031 | 2.000 | 0,39 |

<!-- Estadísticas: 1 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia **3.5.2** **Recarga por Precipitación.** -->
<!-- FIN TABLA 3.5-1 -->


 - 31

MODELO CONCEPTUAL DE FLUJO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

**Tabla 3.5-1 Flujo Subterráneo de Entrada a Modelo Conceptual**

|K equivalente<br>(m/d)|i<br>(m/m)|A<br>(m)|Q<br>(l/s)|
|---|---|---|---|
|0,55|0,0031|2.000|0,39|

Fuente: Elaboración Propia

**3.5.2** **Recarga por Precipitación.**

Se utilizó el método de la curva número, el cual permite determinar la recarga potencial
sobre un acuífero a partir de variables hidrológicas como la precipitación y el valor de curva
número asociado a la cuenca en análisis. A partir del método desarrollado por el Soil
Conservation Service (SCS) para abstracciones de precipitación, descrito por V.T. Chow
(1996), al estudiar los resultados obtenidos para muchas cuencas experimentales, se
desarrolló la relación empírica que permite estimar para un evento hidrológico la parte de
precipitación total ( _P_ ) que logra transformarse en escorrentía directa ( _E_ ), en función de la
capacidad de retención máxima, la cual depende de las características del suelo y de las
condiciones climáticas de la zona analizadas. De esta forma, relacionando la escorrentía
directa y la precipitación, junto con las características del suelo (retención máxima y
capacidad de almacenamiento ( _Ia_ )), se puede obtener el valor de la recarga al acuífero por
precipitación directa ( _Re_ ), de acuerdo a la siguiente ecuación.

_Re = P - E - Ia_

Por otro lado, al representar en gráficas la información de _P_ y _E_ en muchas cuencas, el SCS
encontró curvas empíricas que estandarizó definiendo un número adimensional de curva
número ( _CN_ ), tal que _0<CN<100_ . Este número se define para superficies impermeables y
superficies de agua como _CN=100_ ; mientras que para superficies naturales _CN<100_ . Es
decir, los valores de curva número se asocian a cada tipo de cuenca. Asimismo, la capacidad
de retención máxima ( _R_ _max_ ) depende de las características del suelo y de las condiciones
climáticas de la zona analizada. Así, la curva número y la capacidad de retención máxima se
relacionan por la siguiente ecuación.

1.000
CN=

10 +

R max

25,4

La determinación de la curva número, se realizó considerando un suelo desnudo en un
sector cultivable de agricultura, con gran potencial de escurrimiento y baja tasa de
infiltración debido a su textura arcillosa, lo cual genera su expansión cuando es
humedecido. Además, se consideró el ajuste III de la curva número, asociado a zonas con
antecedentes de humedad. Finalmente, los parámetros empíricos utilizados para la
determinación de la recarga por precipitación se ajustaron del estudio “Análisis Efecto en
el Régimen Hídrico por Cambio en Patrones Meteorológicos” (DGA, 2016), para la región
del Bio Bio. Finalmente, se utilizó la estadística de precipitación mensual de la estación
Chillán Viejo, ubicada a aproximadamente a 7 km al nororiente del sector en estudio.

 - 32

MODELO CONCEPTUAL DE FLUJO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Conforme a lo anterior, en la Tabla 3.5-2 se presentan los valores utilizados, junto al valor
promedio de recarga por precipitación estimado.

**Tabla 3.5-2 Recarga Media Anual por Concepto de Precipitación**

|CN|γ<br>(factor empírico)|Pp Anual Media<br>(mm)|Rec Media Anual<br>(mm)|Rec Media Anual<br>(l/s)|
|---|---|---|---|---|
|97,3<br>|0,0067<br>|867|0,5|0,15|

Fuente: Elaboración Propia

**3.5.3** **Flujo Subterráneo de Salida**

Se identifica un flujo subterráneo de salida hacia el norponiente, cuya magnitud no es
posible de determinar con certeza; sin embargo, es posible estimarlo de acuerdo al balance
hidrogeológico del sistema.

**3.6** **BALANCE HIDROGEOLÓGICO CONCEPTUAL**

El balance hidrogeológico corresponde a la sumatoria de flujos de entrada y salida del sistema
en estudio, considerando que se encuentra en equilibrio. De acuerdo a la conceptualización
del modelo de flujo, el balance del sistema se resume en las siguientes ecuaciones.

E TOTAL = S TOTAL

E TOTAL = F SUB ENTRADA + Rec Pp

S TOTAL = F SUB SALIDA

Donde:

_E_ _T_ : Entrada total al sistema

_S_ _T_ : Salida total del sistema

_F_ _SUB ENTRADA_ : Flujo subterráneo de entrada
_F_ _SUB SALIDA_ : Flujo subterráneo de entrada
_Rec_ _Pp_ : Recarga por precipitación

De esta forma, considerando los valores promedios determinados previamente, es posible
estimar un caudal de salida por concepto de flujo subterráneo de 0,54 l/s. La interacción de
flujos se presenta en la Figura 3.6-1.

 - 33

MODELO CONCEPTUAL DE FLUJO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Fuente: Elaboración Propia

**Figura 3.6-1 Esquema Conceptual Balance Hidrogeológico en Área de Estudio**

 - 34

MODELO CONCEPTUAL DE FLUJO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

# CAPÍTULO 4 MODELO NUMÉRICO

En el presente capítulo se describe la construcción y calibración del modelo numérico de flujo
y transporte del sistema subterráneo, el cual permitirá diseñar la red de monitoreo de pozos
en Ecobio. Este modelo constituye una herramienta matemática/numérica confiable, que
representa los acuíferos y permite estudiar la interacción de los flujos subterráneos.

**4.1** **CONSTRUCCION MODELO NUMÉRICO**

**4.1.1** **Código Matemático**

La implementación del modelo numérico fue realizada utilizando el software comercial
Visual MODFLOW (VMF) en su versión 4.6, desarrollado por Waterloo Hydrogeologic Inc.
Este permite modelar la dinámica del flujo saturado en tres dimensiones mediante la
solución de la siguiente ecuación de flujo:

∂
∂x [[K] [XX] [∙∂h] ∂x

[∂]
∂x [] +]

[∂]

∂y [[K] [yy] [∙∂h] ∂y

[∂]
∂y ~~[]]~~ [ +]

[∂]

∂z [[K] [ZZ] [∙∂h] ∂z

∂z [] + W= S] [S] [∙∂h] ∂t

∂t

Donde los índices _x,y,z_ representan los ejes de coordenadas, _K_ es la permeabilidad, _W_
representa una fuente o pérdida de agua (signo negativo para las extracciones), _h_ es la carga
hidráulica, _Ss_ es el almacenamiento específico y _t_ es el tiempo.

La solución numérica (por diferencias finitas) de dicha ecuación anterior se aplica al dominio
de modelación, que representa el sistema acuífero, al cual se le asignan todas sus
propiedades hidráulicas y condiciones de borde para representar de manera precisa el
sistema real. MODFLOW es uno de los programas de modelación subterránea más utilizados
a nivel mundial para la representación regional de acuíferos, siendo además el programa
comúnmente solicitado por la autoridad para estudiar la disponibilidad y gestión de las
aguas subterráneas. Su utilización, de manera criteriosa en este tipo de estudios es
ampliamente aceptada y validada.

**4.1.2** **Límites y Geometría**

**4.1.2.1** **Dominio y Límites de Modelación**

El dominio de modelación comprende el sistema hidrogeológico conformado
principalmente por los acuíferos superior e intermedio, y acuitardos confinantes dentro
de la zona de estudio, identificados en el modelo conceptual.

 - 35

MODELO NUMÉRICO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

La extensión del dominio del modelo se definió en función de las divisorias de flujo, y
aproximante 1,5 km aguas arriba y aguas abajo de la propiedad de Ecobio, de manera de
no imponer condiciones artificiales en el sector en evaluación.

De acuerdo a lo sugerido en la Guía para el Uso de Modelos de Aguas Subterráneas en el
SEIA elaborada por el Servicio de Evaluación Ambiental (SEA), se consideró conveniente
un cambio en la orientación (rotación) del sistema de coordenadas, con la finalidad de
alinear el modelo a las características de la zona de estudio, y fundamentalmente, a las
direcciones principales de flujo. Lo anterior, dado que la descomposición del vector
velocidad según la orientación de la grilla puede producir dispersión numérica.

De esta manera, los límites se definieron como:

- **Oeste:** 1,5 km aguas abajo de la propiedad de Ecobio, con un flujo de salida por el

sistema acuífero.

- **Norte:** limitado por una condición de no flujo, dada por el sentido de flujo regional.

- **Este:** 1,5 km aguas arriba de la propiedad de Ecobio, con un flujo de entrada en el

sistema acuífero.

- **Sur:** limitado por una condición de no flujo, dada por el sentido de flujo regional.

- **Límite superior:** coincidente con el nivel de terreno, definido por la topografía

entregada por Eximia (2018), complementada con la información del modelo de
elevación digital de terreno (DEM) desde el proyecto Earth Data de la NASA.

- **Límite Inferior:** capa superior de acuitardo bajo el acuífero intermedio, interpretado

mediante información estratigráfica con software Leapfrog.

En la Figura 4.1-1 se muestra los límites del dominio del modelo numérico en la
plataforma Visual MODFLOW, con el modelo rotado; mientras que en la Figura 3.4-2 se
presenta el dominio del modelo sobre una imagen satelital, el cual fue definido el modelo
conceptual. Los vértices que definen el dominio, en coordenadas locales y UTM referidas
al datum WGS84 - Huso 18S, se presentan en la Tabla 4.1-1.

<!-- INICIO TABLA 4.1-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- plataforma Visual MODFLOW, con el modelo rotado; mientras que en la Figura 3.4-2 se presenta el dominio del modelo sobre una imagen satelital, el cual fue definido el modelo conceptual. Los vértices que definen el dominio, en coordenadas locales y UTM referidas al datum WGS84 - Huso 18S, se presentan en la Tabla 4.1-1. -->

**Tabla 4.1-1: Coordenadas Límite Dominio Modelación****

| Vértice | Modelo (m) | Col3 | UTM WGS84 (m) | Col5 |
| --- | --- | --- | --- | --- |
| **Vértice** | **X ** | **Y ** | **Este** | **Norte** |
| Superior-Oriente | 5.000 | 2.500 | 755.023 | 5.934.639 |
| Superior-Poniente | 0 | 2.500 | 751.488 | 5.938.175 |
| Inferior-Oriente | 5.000 | 0 | 753.256 | 5.932.871 |
| Inferior-Poniente | 0 | 0 | 749.720 | 5.936.407 |

<!-- Estadísticas: 5 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. De acuerdo a esos límites, el área total cubierta por el modelo tiene una superficie de 12,5 km2, con 2,5 km de extensión en dirección norte-sur, y 5 km oeste-este. -->
<!-- FIN TABLA 4.1-1 -->


**Tabla 4.1-1 Coordenadas Límite Dominio Modelación**

|Vértice|Modelo (m)|Col3|UTM WGS84 (m)|Col5|
|---|---|---|---|---|
|**Vértice**|**X **|**Y **|**Este**|**Norte**|
|Superior-Oriente|5.000|2.500|755.023|5.934.639|
|Superior-Poniente|0|2.500|751.488|5.938.175|
|Inferior-Oriente|5.000|0|753.256|5.932.871|
|Inferior-Poniente|0|0|749.720|5.936.407|

Fuente: Elaboración propia.

De acuerdo a esos límites, el área total cubierta por el modelo tiene una superficie de
12,5 km2, con 2,5 km de extensión en dirección norte-sur, y 5 km oeste-este.

 - 36

MODELO NUMÉRICO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Fuente: Elaboración Propia

**Figura 4.1-1 Límite Modelo Numérico, Rotado en Visual MODFLOW**

**4.1.2.2** **Discretización Horizontal**

La Figura 4.1-2 muestra una vista en planta de la grilla definida en la zona de estudio, en

coordenadas UTM referidas al datum WGS84 - Huso 18S.

Fuente: Elaboración Propia

**Figura 4.1-2 Grilla de Modelación Usada en Visual MODFLOW**

 - 37

MODELO NUMÉRICO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Para la malla, se definió una discretización base de 50 m en el dominio del modelo, es decir,
cada celda posee un tamaño de 50 x 50 m; con un refinado de malla de 10 metros en la
propiedad de Ecobio y sus zonas adyacentes, dado que es el sector que requiere de una
mayor precisión. Para llevar a cabo lo anterior, se realizó un “suavizado” para la correcta
transición entre tamaños de celda. De esta forma, el modelo se compone de 174 filas (de
norte a sur) y 312 columnas (de oeste a este).

**4.1.2.3** **Discretización Vertical**

El modelo numérico ha sido discretizado verticalmente en 4 capas o layers, según las
unidades definidas en el modelo conceptual. De esta forma, la primera capa representa
el acuitardo compuesto por materiales asociado a depósitos de origen volcanoclástico,
seguido por el acuífero superior, el cual sobreyace al acuitardo intermedio, que al mismo
tiempo confina al acuífero intermedio. Lo anterior se resume en la Tabla 4.1-2.

<!-- INICIO TABLA 4.1-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- unidades definidas en el modelo conceptual. De esta forma, la primera capa representa el acuitardo compuesto por materiales asociado a depósitos de origen volcanoclástico, seguido por el acuífero superior, el cual sobreyace al acuitardo intermedio, que al mismo tiempo confina al acuífero intermedio. Lo anterior se resume en la Tabla 4.1-2. -->

**Tabla 4.1-2: Capas de Simulación del Modelo Numérico****

| Capa | Unidad |
| --- | --- |
| 1 | Acuitardo superficial |
| 2 | Acuífero superior |
| 3 | Acuitardo intermedio |
| 4 | Acuífero intermedio |

<!-- Estadísticas: 4 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. En cuanto a la delimitación entre capas, se utilizó como límite superior para la capa 1, la topografía correspondiente Eximia (2018), complementada con la información del -->
<!-- FIN TABLA 4.1-2 -->


**Tabla 4.1-2 Capas de Simulación del Modelo Numérico**

|Capa|Unidad|
|---|---|
|1|Acuitardo superficial|
|2|Acuífero superior|
|3|Acuitardo intermedio|
|4|Acuífero intermedio|

Fuente: Elaboración propia.

En cuanto a la delimitación entre capas, se utilizó como límite superior para la capa 1, la
topografía correspondiente Eximia (2018), complementada con la información del
modelo de elevación digital de terreno (DEM) de la NASA. El resto de los layers fue
interpretado con superficies de contacto mediante el software Leapfrog. Para esto se
consideró la información de estratigrafías y calicatas descritas en el modelo conceptual,
implementando una extensión solidaria a la topografía en el dominio del modelo. De
manera de visualizar lo descrito, en la Figura 4.1-3 se presenta en planta el trazado de
un perfil de corte en Leapfrog, que posteriormente se visualiza en 3D en la Figura 4.1-4.
Finalmente, en la Figura 4.1-5 se presenta el perfil de corte ingresado a Visual MODFLOW
con las 4 capas.

 - 38

MODELO NUMÉRICO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Fuente: Elaboración Propia

**Figura 4.1-3 Planta con Perfil de Corte en Leapfrog**

Acuitardo Superficial

Acuífero

Superior

#### RSU

Acuitardo

Fuente: Elaboración Propia

MODELO NUMÉRICO

#### CITA

Acuífero

Intermedio

**Figura 4.1-4 Perfil de Corte en Leapfrog**

 - 39

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Nota: Distancia vertical exagerada 10x.
Fuente: Elaboración Propia

**Figura 4.1-5 Perfil de Corte en Visual MODFLOW**

**4.1.3** **Discretización Temporal y Periodos de Stress**

A escala temporal, el modelo numérico se discretizó en un total de 51 periodos de definición
de variables temporales (stress), correspondiente a meses calendario. Además, éstos
fueron subdivididos en pasos de tiempo, conforme a las condiciones de borde ingresadas.

El modelo numérico se construyó considerando un régimen transiente de simulación, de
manera de considerar la variabilidad producida por la recarga de precipitación. Conforme a
lo anterior, el primer periodo de stress representa las condiciones de enero de 2015; y los

restantes hasta abril de 2019.

Dada la insuficiente data para representar una calibración, se consideró aceptable sólo
reproducir las condiciones de abril de 2019, dado que representa el único monitoreo de
niveles en los nuevos pozos, con más de un mes de estabilización de niveles, desde su fecha
de construcción. De esta manera, el modelo se opera desde enero de 2015 a abril de 2019,
representando la situación actual en que se encuentran los niveles; y que representará la
condición inicial del sistema para la simulación del escenario futuro. Como condición inicial
para la modelación, se consideró un nivel de agua a la cota de la topografía, de manera de
asegurar saturación en el sistema.

**4.1.4** **Condiciones de Borde**

A continuación, se describe la implementación de las condiciones de borde de la zona de
modelación, las cuales fueron definidas para representar las salidas y entradas del sistema,
de acuerdo a las características descritas en el modelo conceptual. Las condiciones son las
siguientes:

- **Condición de no flujo:** límites sin flujo perpendicular.

- **Condición de flujo conocido** (condición de frontera de segundo tipo, Neumamn):

recargas naturales.

- **Condición carga hidráulica conocida** (condición de frontera de primer tipo, Dirichlet):

aplicada para los flujos subterráneos de entrada y salida del sistema.

 - 40

MODELO NUMÉRICO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

**4.1.4.1** **Límites de No Flujo**

Esta condición de borde se representa como la condición “no flow” y se define en
aquellas zonas de la cuenca donde no existe flujo de aguas subterráneas; en particular,
en divisorias de flujo existentes con el sistema colindante.

Esta condición se designó para distinguir la zona activa del dominio de modelación (zona
en la cual se evalúa la dinámica de flujo subterráneo), de la zona inactiva (zona sin flujo
subterráneo), las que se observan en la Figura 4.1-6.

**4.1.4.2** **Nivel Conocido**

Esta condición de borde se utilizó para representar el flujo de entrada al modelo
numérico por el sector oriente, proveniente como parte del flujo regional aportante. Así
también, se utilizó para caracterizar el flujo descargado por el límite poniente, hacia
aguas abajo.

Estas condiciones se definieron a partir de las curvas equipotenciales determinadas en
el estudio DGA (2011), en donde se refleja una situación estable, y cuya información fue
utilizada para definir los flujos de entrada y salida del modelo conceptual del río Itata.
De esta manera, para su implementación se consideró el ajuste de la superficie
equipotencial regional elaborada en 2011, con la nueva data de nivel piezométrico en la
propiedad de Ecobio. Así también, se consideraron valores de cargas hidráulicas tales
que generasen los flujos pasantes identificados en el modelo conceptual.

De esta manera, se consignó un nivel conocido de 110,2 m s.n.m en el extremo este, y
de 100,5 m s.n.m. en el extremo oeste; como se observa en la Figura 4.1-6.

**4.1.4.3** **Recargas por Precipitación al Sistema Hidrogeológico**

Corresponde a la recarga hacia el acuífero por concepto de precipitaciones. Ésta se
estima a partir de metodologías que permiten obtener, en función de antecedentes
pluviométricos y características del suelo en estudio, la percolación efectiva hacia el
acuífero. Conforme a lo estipulado en el modelo conceptual, estas fueron estimadas
mediante la metodología de la curva número, desarrollado por el Soil Conservation
Service (SCS) para abstracciones de precipitación.

En la Tabla 4.1-3 se presentan los resultados de recargas por concepto de precipitación
para el periodo 2015-2019. Ésta se asigna espacialmente sobre el modelo, a excepción
del sector donde se ubica el CITA y RSU, debido al actual manejo de aguas lluvias con
canales de contorno, que envía el agua contactada hacia la piscina de aguas lluvias de
operación. Lo anterior se resume en la Figura 4.1-6.

 - 41

MODELO NUMÉRICO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

**Tabla 4.1-3 Recarga por Precipitación en Modelo Numérico**

|Año|Recarga (l/s)|
|---|---|
|2015|0,14|
|2016|0,13|
|2017|0,18|
|2018|0,16|
|2019|0,14|

Fuente: Elaboración propia.

Fuente: Elaboración Propia

**Figura 4.1-6 Implementación de Condiciones de Borde en Visual MODFLOW**

**4.1.5** **Parámetros Hidrogeológicos del Modelo Numérico**

Los parámetros hidrogeológicos corresponden a la permeabilidad ( _K_ ), que mide la
capacidad del medio poroso para conducir o transmitir agua subterránea y el
almacenamiento, que representa la capacidad del medio para embalsar o almacenar agua
subterránea. La implementación de un modelo numérico de simulación requiere de una
adecuada aproximación inicial de estos parámetros y su correspondiente distribución
espacial, pues al existir múltiples soluciones posibles, permite acotar el rango de
modificaciones que se realizarán en el proceso de calibración. De acuerdo a lo anterior, se
asignaron preliminarmente al modelo valores y una distribución espacial de permeabilidad,
conforme a las identificadas en el modelo conceptual (ya presentada en la Tabla 3.2-1 y
Tabla 3.2-3).

Asimismo, esta información se complementó con valores puntuales de permeabilidad y
coeficientes de almacenamiento obtenidos en la recopilación de antecedentes, información

 - 42

MODELO NUMÉRICO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

de pruebas de bombeo efectuadas para la solicitud de derechos de agua subterránea y
valores adoptados en el modelo numérico hidrogeológico realizado por DGA (2016).

Su ajuste final se realizó mediante el proceso de calibración, descrito en el acápite 4.2,
donde se ajustaron niveles y flujos para la situación transiente.

**4.1.6** **Pozos de Observación**

De acuerdo a lo establecido en el modelo conceptual, acápite 3.3, los 4 pozos representan
las condiciones del sistema subterráneo, identificándose PM2-S y PM6-S en el acuífero
superior, y PM3-I y PM1-I en el intermedio. Así también, se consideró como válida para la
calibración la fecha de monitoreo de abril de 2019, dado que es la medición más
representativa, puesto que toma en cuenta más de un mes de estabilización de los niveles
en los pozos, desde su fecha de construcción.

**4.2** **CALIBRACIÓN DEL MODELO NUMÉRICO**

Una vez incorporados al modelo todos los elementos definidos en el acápite anterior, el
modelo se calibró en régimen transiente con intervalos de tiempo a escala mensual. El objetivo
fue lograr la mayor aproximación posible entre los niveles piezométricos observadosmodelados; y la dinámica de flujos que ocurren en el sistema.

En este aspecto, es importante mencionar que dada la insuficiente data de monitoreos de
niveles (de los nuevos pozos) con la que se cuenta, se consideró aceptable representar las
condiciones de flujo para abril de 2019, representando también la dinámica de flujos entre
2015 y 2019. De esta manera, en términos prácticos el modelo fue ajustado con un solo
monitoreo de niveles en su periodo transiente, y que servirá como condición inicial para la

simulación de escenarios futuros.

La diferencia entre un nivel simulado numéricamente y el observado, se llama residual, y
permite el cálculo de estadígrafos que permiten estimar la bondad de ajuste asociada a la
calibración. Entre ellos, los más utilizados son el error medio absoluto (MAE) y el error
cuadrático medio (RMS). Así también, es importante considerar el error de cierre del balance
de masa del modelo, correspondiente a la diferencia porcentual entre los flujos de entrada y
salida del modelo. La Guía de Modelación elaborada por el Servicio de Evaluación Ambiental
(SEA), sugiere a modo de referencia que el MAE normalizado de un proceso de calibración

debiese ser a lo sumo un 5% de la diferencia máxima de niveles observados en el dominio del

modelo. Así también, si bien no especifica un criterio para el RMS, se considera aceptable un
valor de RMS normalizado inferior a un 10% para el modelo. Por último, el SEA sugiere que el
error de cierre del balance del modelo, correspondiente a la diferencia porcentual entre las
entradas y salidas del modelo, sea igual o inferior al 1%.

**4.2.1** **Ajustes de Flujo y Permeabilidad Consideradas**

Conforme a lo descrito, se procedió a un proceso de ajuste tipo “ensayo y error”, durante
el cual se ajustaron parámetros y variables en forma cíclica hasta que el grado de similitud

 - 43

MODELO NUMÉRICO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

entre las predicciones y los valores observados en el sistema físico cumplieron con los
objetivos establecidos para el proyecto. Así, se modificaron determinados parámetros y
propiedades del modelo dentro de márgenes físicamente posibles, tales como:

- **Flujos subterráneos de entrada y salida** : según los valores establecidos en el modelo

conceptual, se ajustaron en el dominio activo del modelo.

- **Variación de permeabilidad y almacenamiento en el modelo** : las zonas de

permeabilidad establecidas preliminarmente fueron refinadas de manera tal de ajustar
sus valores en las unidades definidas, de acuerdo a los rangos establecidos en el
modelo conceptual. La distribución final de la permeabilidad, junto a los valores
considerados se presentan en la Tabla 4.2-1.

<!-- INICIO TABLA 4.2-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- permeabilidad establecidas preliminarmente fueron refinadas de manera tal de ajustar sus valores en las unidades definidas, de acuerdo a los rangos establecidos en el modelo conceptual. La distribución final de la permeabilidad, junto a los valores considerados se presentan en la Tabla 4.2-1. -->

**Tabla 4.2-1: Valores de Permeabilidad y Coeficiente de Almacenamiento Adoptados en****

| Layer | Estrato | Sector | Permeabilidad<br>(m/d) | Coeficiente de<br>Almacenamiento | Porosidad efectiva |
| --- | --- | --- | --- | --- | --- |
| Layer 1 | Acuitardo Superior | Toda la capa | 0,04 | 5x10-5 | 5% |
| Layer 2 | Acuífero Superior | Toda la capa | 1,0 | 5x10-5 | 15% |
| Layer 3 | Acuitardo Intermedio | Toda la capa | 0,09 | 5x10-5 | 5% |
| Layer 4<br> | Acuífero Intermedio<br> | oeste / este | 0,2 / 0,75 | 5x10-5 | 15% |

<!-- Estadísticas: 4 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia **4.2.2** **Resultados del Ajuste del Modelo** -->
<!-- FIN TABLA 4.2-1 -->


**Tabla 4.2-1 Valores de Permeabilidad y Coeficiente de Almacenamiento Adoptados en**

**Modelo**

|Layer|Estrato|Sector|Permeabilidad<br>(m/d)|Coeficiente de<br>Almacenamiento|Porosidad efectiva|
|---|---|---|---|---|---|
|Layer 1|Acuitardo Superior|Toda la capa|0,04|5x10-5|5%|
|Layer 2|Acuífero Superior|Toda la capa|1,0|5x10-5|15%|
|Layer 3|Acuitardo Intermedio|Toda la capa|0,09|5x10-5|5%|
|Layer 4<br>|Acuífero Intermedio<br>|oeste / este|0,2 / 0,75|5x10-5|15%|

Fuente: Elaboración Propia

**4.2.2** **Resultados del Ajuste del Modelo**

A continuación, se presentan los resultados del proceso de ajuste, comparando los niveles
piezométricos medidos y resultantes de la simulación, según se muestra en la Figura 4.2-1.

Dada la configuración de niveles medidos, se seleccionaronlos pozos inmediatamente
adyacentes al CITA y RSU: PM1-I, PM3-I, PM2-S para la calibración, a partir de la cual se
aprecia una correlación adecuada en la vecindad de Ecobio.

Así también, en la Tabla 4.2-2 se presentan los estadígrafos asociados al proceso de
calibración en régimen transiente. Se observa un buen ajuste entre los datos simulados y
observados, con estadígrafos de calibración de un MAE normalizado de 2,36% y un RMS
normalizado de 2,57%; cumpliendo las sugerencias de la Guía de Modelación del SEA,
representando una calibración adecuada.

 - 44

MODELO NUMÉRICO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Fuente: Elaboración Propia

**Figura 4.2-1 Resultados Gráficos del Modelo Numérico**

**Tabla 4.2-2 Estadígrafos Calibración**

|Parámetro|Fórmula|Valor|
|---|---|---|
|Coeficiente de<br>Determinación (R2)|<br>|0,998|
|Error Medio (m)||0,057|
|MAE Normalizado (%)|MAE<br>max(Nobs) −min (Nobs)|2,36|
|RMS Normalizado (%)||2,57|

Fuente: Elaboración Propia.

Por último, en la Figura 4.2-2 se presentan las curvas equipotenciales obtenidas al final del
periodo de calibración (abril, 2019), en la cual se aprecia la dirección de flujo en sentido
suroriente-norponiente, en concordancia con lo establecido en el modelo conceptual.

 - 45

MODELO NUMÉRICO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Fuente: Elaboración Propia

**Figura 4.2-2 Equipotenciales Modelo Numérico Abril 2019**

**4.2.3** **Balance Hidrogeológico**

De acuerdo con los resultados de la calibración, en la Tabla 4.2-3 se presenta el balance
hidrogeológico general del modelo numérico, representativo del periodo 2015-2018, para
las diferentes componentes de flujo.

Según el balance de aguas para el modelo calibrado, se reproducen los volúmenes de agua
que interactúan en el sistema, definidos en el modelo conceptual. Asimismo, el error del
balance es de un -0,3%, cumpliendo la sugerencia de la Guía de Modelación del SEA.

 - 46

MODELO NUMÉRICO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

**Tabla 4.2-3 Balance Hidrogeológico- Promedio 2015-2019**

|Entradas|Volumen (m3)|Caudal (l/s)|
|---|---|---|
|Recarga por Precipitación|1.005|0,14|
|Flujo Regional|2.487|0,36|
|Total Entradas|3.491|0,50|
|<br> <br>|<br> <br>|<br> <br>|
|**Salidas**|||
|Flujo Regional|3.502|0,50|
|Total Salidas|3.502|0,50|
|<br> <br>|<br> <br>|<br> <br>|
|**Variación de Almacenamiento**|6|0,00001|
|**Balance**|-10,9|-0,002|
|**Error Balance**<br>|-0,3%|-0,4%|

Fuente: Elaboración Propia

 - 47

MODELO NUMÉRICO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

# CAPÍTULO 5 DISEÑO RED DE MONITOREO

En el presente capítulo se presenta el diseño de la red de monitoreo en Ecobio, a partir de los
resultados de un escenario de simulación predictivo, que permitió analizar la movilidad de flujo
y de un eventual contaminante en el sistema subterráneo, proveniente desde la operación de
la planta.

**5.1** **SIMULACIÓN FUTURA EN MODELO NUMÉRICO DE FLUJO**

**5.1.1** **IMPLEMENTACIÓN DE PROYECCIÓN EN VIDA ÚTIL RSU Y CITA**

La simulación considera el desarrollo de los Proyectos actualmente aprobados por la
autoridad (Ecobio 1999; Ecobio, 2003), con un avance del CITA y RSU hasta el año 2033, y
posterior monitoreo hasta el año 2053, totalizando 34 años de simulación del escenario
predictivo. De esta manera, el modelo numérico se extendió hasta el año 2053, totalizando
456 periodos de stress.

Las condiciones de borde de flujos subterráneos de entrada y salida se mantuvieron del
modelo calibrado, con excepción de la recarga por precipitación en el sector de Ecobio.

De acuerdo al plan de manejo de aguas lluvias, las aguas que caen sobre la superficie en
operación del depósito de seguridad, son susceptibles de contaminarse si entran en
contacto con la masa de residuos, por lo que se recogen con un sistema de canaletas que
conducen el agua hacia las piscinas de lixiviados. Conforme a lo anterior, el modelo
representó el avance progresivo del CITA y RSU, mediante la definición de zona de no flujo
de recarga en estos sectores, según la proyección VOLTA (2019), indicada en la Figura 5.1-1.

 - 48

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Fuente: Elaboración Propia

**Figura 5.1-1 Sectores Sin Recarga por Precipitación por Avance CITA y RSU**

**5.2** **SIMULACIÓN DE MOVILIDAD DE CONTAMINANTE**

**5.2.1** **POTENCIAL DE CONTAMINACIÓN HÍDRICA SUBTERRÁNEA**

El sector donde se emplazan el CITA y el RSU, cuentan con una zona de impermeabilización

en toda su base.

En lo que respecta al CITA, la superficie del depósito de seguridad consta de una capa de
impermeabilización sobre toda la base del depósito, de bentonita de 5 mm. Sobre ésta se
colocó una geomembrana de 1,5 mm subyaciendo una capa drenante de 30 cm. Asimismo,
sobre ésta, se cuenta con otro sistema geomembrana-capa drenante de las mismas
características. Finalmente, se instaló una lámina geotextil para mejorar las propiedades
mecánicas de la impermeabilización.

En lo que se refiere al RSU, se consideró bentonita de 5 mm, bajo una geomembrana de
polietileno de alta densidad texturada en ambas caras, junto a un sistema de drenaje de
percolados. Adicionalmente, como protección mecánica complementaria se incorporó una
capa de geotextil.

Según lo indicado, el CITA y RSU cuentan con un robusto sistema de impermeabilización,
como criterio general de su diseño. No obstante, para evaluar la potencial movilidad de

 - 49

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

contaminante en el modelo numérico de flujo, se ha considerado eventuales zonas de falla,
a partir de las cuales una partícula contaminante pudiese infiltrar al sistema subterráneo,
aun cuando esto se estima como muy improbable, puesto que existe el estrato superficial
impermeable como se ha indicado en el modelo conceptual.

En este aspecto, para la disposición actual del CITA y RSU, Ecobio ha determinado como
potenciales zonas de falla, los sectores indicados en color rosado en la Figura 5.2-1, debido
a que se han identificado como los sectores más bajos de los rellenos.

Fuente: Elaboración Propia

**Figura 5.2-1 Zonas de Potenciales Fallas para Actual Disposición de CITA y RSU**

En lo que respecta a la proyección del CITA y RSU, se definió una proyección lineal de avance
de éstos hacia el año 2033, en bloques bianuales, según se indica en Figura 5.2-2. De esta
manera, y de forma conservadora, se consideró cada una de estas particiones como
potenciales lugares de falla en un escenario futuro.

 - 50

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Fuente: Elaboración Propia

**Figura 5.2-2 Zonas de Potenciales Fallas para Futura Disposición de CITA y RSU**

**5.2.2** **TRAYECTORIAS DE PARTÍCULAS**

Para evaluar la movilidad de un posible contaminante, se utilizaron Pathlines o Líneas de
Trayectorias Proyectadas, mediante el módulo MODPATH de Visual MODFLOW. Este es un
programa de post-procesamiento de seguimiento de partículas, diseñado para trabajar con
la data de flujo que genera MODFLOW en cada periodo de stress; generando los vectores
de velocidad en cada celda y construyendo la distribución de velocidades en el sistema

subterráneo.

Conforme a lo anterior, se implementó el rastreo de partículas en las eventuales zonas de
falla, identificadas en el acápite 5.2.1. De manera conservadora, se supuso que una eventual
partícula contaminante infiltraría directamente en el acuífero superior.

Así también, cada partícula rastreada se incorporó al modelo en el eventual tiempo desde
producida la fuga en que la celda se dispone. De esta manera, en las zonas de eventuales
fallas o fugas, se implementó el rastreo de partículas desde 2019; mientras que para zonas
en que se proyectan celdas con proyección bianual, se implementó el rastreo en el periodo
en que la celda se crea.

 - 51

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Conforme a lo anterior, en la Figura 5.2-3 se presentan los resultados de las trayectorias
proyectadas para cada partícula. Cada segmento de viaje representa la trayectoria de la
partícula al año 2053, y cada flecha indica la ubicación de la partícula los años 2033, 2043 y
2053; en el sistema.

Fuente: Elaboración Propia

**Figura 5.2-3 Líneas de Trayectoria Proyectadas para Cada Partícula**

Se observa cómo las trayectorias de las partículas se dirigen en el sentido del flujo
subterráneo: suroriente-norponiente. Un potencial contaminante, que infiltraría desde una
de las eventuales zonas de falla, podría recorrer entre 65 y 130 metros, dependiendo de la
baja permeabilidad de la zona evaluada, el gradiente hidráulico del sistema subterráneo, y
la fecha en que sería depositada la partícula.

Complementando lo anterior, las trayectorias de partículas modeladas, ingresadas de
manera conservadora en el acuífero superior, recorren todo el periodo de simulación en
dicho estrato, según se muestra en la Figura 5.2-4.

 - 52

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Nota: Distancias verticales exageradas 10x.
Fuente: Elaboración Propia

**Figura 5.2-4 Líneas de Trayectoria Proyectadas en Perfil**

De esta manera, las trayectorias de partículas indican que la movilidad de un potencial
contaminante no infiltraría hacia el acuitardo intermedio, y con mucha menos posibilidad,

infiltraría al acuífero intermedio.

**5.2.3** **DISEÑO DE RED DE MONITOREO**

Con el objetivo de detectar la movilidad de un potencial contaminante desde las eventuales
zonas de falla, se seleccionaron las ubicaciones de los pozos que formarán parte de la red
de monitoreo, según se indica en la Figura 5.2-5. Como se concluyó en el acápite anterior,
las trayectorias de partículas se ubican siempre en el estrato superior, por lo que la red de
pozos dispuesta se propone habilitarla en dicho estrato. Así también, su ubicación se ha
determinado de manera que puedan acceder máquinas para la construcción de los pozos;
en función de la ubicación de las futuras obras que construirá el Proyecto; y considerando
el deslinde de la propiedad de Ecobio.

De la Figura 5.2-5 se observa cómo los pozos propuestos se ubican en las cercanías de las
trayectorias de partículas desde las eventuales zonas de falla; y que además, la detectan de
manera temprana, a partir de una eventual depositación, no postergando su detección.

 - 53

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Fuente: Elaboración Propia
**Figura 5.2-5 Ubicación de Pozos de Monitoreo Superficial para Detección de Eventuales**

**Fallas en Modelo de Movilidad de Contaminante**

Por último, en lo que respecta al diseño red de monitoreo de las aguas subterráneas de la
operación del RSU y CITA, y conforme a lo dispuesto en el artículo 61 del Reglamento
Sanitario Sobre Manejo de Residuos Peligrosos (DS148, 2004), un sistema de monitoreo de
calidad de aguas subterráneas debe “contar con un número suficiente de pozos instalados
en sitios y profundidades adecuadas, para extraer muestras representativas del acuífero
superior”, donde la cantidad, distancia y profundidad de los piezómetros, debe
determinarse a partir de los estudios técnicos con que se cuente en el sitio. Así también,
regulaciones internacionales como la Guía Regulatoria de USA (EPA, 1986), recomiendan un
mínimo de 4 piezómetros de control para monitorear un determinado sector, y en
particular, 1 ubicado aguas arriba y 3 aguas abajo.

Conforme a lo anterior, se propone la red de 13 piezómetros de monitoreo presentada en
la Figura 5.2-6. Esta considera 11 piezómetros habilitados en el acuífero superficial, con
uno ya construido, puesto que formó parte de los trabajos de terreno para la generación de
nueva información de campo.

No obstante que, los resultados del modelo conceptual y numérico de flujo indican que las
trayectorias de las partículas que ingresan al acuífero superior no infiltrarían en ningún caso

 - 54

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

hasta el acuitardo que subyace, de espesor aproximado entre 10 y 18 metros; de todos
modos, se propone considerar en la red de monitoreo los pozos PM1-I y PM3-I, para el
acuífero intermedio. Estos suponen un monitoreo del sistema acuífero solo a nivel
referencial, y se aprovechan, dado que ya se encuentran construidos.

Fuente: Elaboración Propia

**Figura 5.2-6 Ubicación de Pozos de Monitoreo de Aguas Subterráneas de Operación CITA y**

**RSU**

De esta manera, la nueva red de monitoreo se compone de 13 piezómetros, de los cuales

se deben construir 10.

Finalmente, en la Tabla 5.2-1 se presenta un resumen con la ubicación de cada piezómetro,
acuífero monitoreado, y el objetivo que cumple en la red de monitoreo.

 - 55

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

**Tabla 5.2-1 Resumen Red de Monitoreo**

|Piezómetro|Acuífero<br>Habilitado|Objetivo|Ubicación Referencial|
|---|---|---|---|
|PM3-S|Superior|Monitorear aguas arriba<br>operación Ecobio: RSU y CITA|Extremo suroriente de RSU|
|PM12-S|Superior|Monitorear aguas abajo proyección<br>crecimiento de RSU oriente|Norte de proyección de RSU|
|PM9-S|Superior|Monitorear aguas abajo<br>deslinde actual RSU|Norte del RSU|
|PM8-S|Superior|Monitorear aguas abajo proyección<br>crecimiento de RSU poniente|Norte de proyección de RSU|
|PM7-S|Superior|Monitorear aguas abajo proyección<br>crecimiento de RSU poniente|Norte de proyección de RSU|
|PM5-S|Superior|Monitorear aguas abajo<br>deslinde actual CITA|Norte del CITA|
|PM2-S|Superior|Monitorear aguas abajo<br>deslinde actual CITA|Norte del CITA.<br>Ya construido|
|PM4-S|Superior|Monitorear aguas abajo proyección<br>crecimiento CITA poniente|Norte de proyección de CITA|
|PM10-S|Superior|Monitorear aguas abajo proyección<br>crecimiento CITA poniente|Norte de proyección de CITA|
|PM1-S|Superior|Monitorear aguas abajo proyección<br>crecimiento CITA poniente|Extremo norponiente de<br>proyección de CITA|
|PM11-S|Superior|Monitorear aguas abajo proyección<br>crecimiento CITA poniente|Extremo poniente<br>de proyección de CITA|
|PM3-I|Intermedio|Monitorear aguas arriba<br>operación Ecobio: RSU y CITA|Extremo suroriente de<br>proyección oriente RSU.<br>Ya construido|
|PM1-I|Intermedio|Monitorear aguas abajo<br>proyección crecimiento CITA|Extremo norponiente de<br>proyección poniente de CITA.<br>Ya construido|

Fuente: Elaboración Propia

Esta red se ha diseñado considerando 1 piezómetro ubicado aguas arriba de la operación RSU
y CITA; 1 piezómetro para detectar eventuales fallas del deslinde actual del RSU; 3 piezómetros
para la proyección del RSU; 2 piezómetros para la actual ubicación del CITA; y 4 piezómetros
para la proyección del CITA. Por último, el sistema lo completan los 2 pozos habilitados en el
acuífero intermedio, aguas arriba y aguas abajo de la operación RSU y CITA, y que como se ha
detallado, se han propuesto de manera conservadora.

Con la disposición espacial de los piezómetros, ubicados estratégicamente de acuerdo a lo
indicado por el modelo de movilidad de contaminante, se podrá detectar cambios de nivel y/o
calidad de las aguas subterráneas en forma oportuna durante la operación y abandono del

proyecto.

 - 56

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

En lo que respecta a las características de los piezómetros, la selección del diámetro más
apropiado y cribado depende de una serie de factores, y en particular del uso que éstos tengan.
En este caso, los piezómetros se utilizarán para monitorear niveles y muestrear agua para
determinar su calidad, por lo cual es importante definir un diámetro tal que permita la
introducción de un bailer o bomba de muestreo, y que al mismo tiempo no implique un
volumen excesivo de purga. Conforme a lo anterior, se ha seleccionado un diámetro de
habilitación de 6” utilizando PVC ranurado. En Tabla 5.2-2 se presenta un resumen con las
características que se proponen para cada piezómetro de la red de monitoreo.

**Tabla 5.2-2 Características Red de Monitoreo**

|Piezómetro|E WGS84<br>(m)|N WGS84<br>(m)|Profundidad de<br>Perforación<br>Estimada (m)|Diámetro<br>Habilitación<br>(")|Material|Profundidad<br>Estimada de<br>Ranurado (m)|
|---|---|---|---|---|---|---|
|PM1-S|751.383|5.935.749|20|6|PVC|12-19|
|PM2-S (*)|751.976|5.935.642|42|6|PVC|13-19|
|PM3-S|753.138|5.934.983|20|6|PVC|12-19|
|PM4-S|751.842|5.935.649|20|6|PVC|12-19|
|PM5-S|752.119|5.935.596|20|6|PVC|12-19|
|PM7-S|752.384|5.935.511|20|6|PVC|12-19|
|PM8-S|752.526|5.935.476|20|6|PVC|12-19|
|PM9-S|752.739|5.935.422|20|6|PVC|12-19|
|PM10-S|751.623|5.935.702|20|6|PVC|12-19|
|PM11-S|751.366|5.935.546|20|6|PVC|12-19|
|PM12-S|753.122|5.935.334|20|6|PVC|12-19|
|PM3-I (*)|753.182|5.934.982|42|6|PVC|33-37|
|PM1-I (*)|751.384|5.935.769|33|6|PVC|23-28|

(*): Pozo de exploración construido, habilitado para monitoreo.

Nota: Coordenadas referenciales

Fuente: Elaboración Propia

**5.3** **DISEÑO DE PIEZÓMETROS Y ESPECIFICACIONES TÉCNICAS**

Los 10 nuevos piezómetros se realizarán en cuatro etapas, que deberán ser llevadas con
rigurosidad, aunque las características de los diferentes emplazamientos impidan la
estandarización del diseño y construcción de éstos. Las fases constructivas serán las siguientes:

- Perforación del piezómetro

- Habilitación del piezómetro

- Desarrollo

- Terminación

A continuación, se entregan las especificaciones y recomendaciones para su correcta
ejecución.

 - 57

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

**5.3.1** **Perforación Piezómetros**

**Profundidad y Diámetro**
Perforación hasta que se detecte las secuencias limo-arcillosas y arenas arcillosas (acuitardo
intermedio) que subyace al acuífero superior. Se estima que debiese ser del orden de los 20

metros.

Ejecutar con diámetro de 10”, con sistema de perforación que no use aditivos que puedan
alterar la calidad de las aguas que se requiere monitorear, ni la permeabilidad del medio.
En este aspecto, se recomiendan métodos como percusión con cable, o sistemas de tipo
Barber. Durante la perforación se deberá hacer un seguimiento permanente de los niveles
piezométricos, utilizando equipos adecuados para la medición de éstos.

**Antepozo**
El antepozo para cada piezómetro será de tubería metálica de 1,2 m, de los cuales 1 m se
encontrará sobre el nivel del suelo. Adicionalmente se considera la instalación de una tapa
de protección para cerrar el antepozo, con identificación del pozo y candado.

**5.3.2** **Habilitación del Piezómetro**

**Tuberías de Habilitación**

Tubería de habilitación de longitud comprendida desde 0,8 m sobre el nivel de terreno
hasta 0,8 m bajo el acuitardo intermedio. Se estima que la longitud será de
aproximadamente 9 m (Figura 5.3-2). La tubería de habilitación tendrá un diámetro de 6”,
y se recomienda que sea de PVC schedule 80. El ranurado se propone sea estándar slot 40,
ubicado desde un metro bajo la capa de arcilla sobre el acuífero superior, hasta el fondo de
éste (Figura 5.3-2). La habilitación también puede ejecutarse en acero, con la ubicación del
cribado equivalente a la ya descrita.

**Espacio Anular**
El espacio anular será de 2” entre la tubería y la pared de la formación litológica.

**Empaque de Gravas**
Se sugiere que el tamaño de la grava a utilizar sea de procedencia fluvial con un tamaño de
3 a 6 mm, con cantos redondeados, y con bajo porcentaje de material calcáreo.

**Sistema de Engravillado**
Se instalará la grava a través de una tubería ‘tremmie’, disponiéndola en el espacio anular
cuidadosamente desde el fondo, ascendiendo hasta un metro bajo el techo del acuífero.
(Figura 5.3-2).

**Sello de Cemento-Bentonita**

Para asegurar que el flujo interceptado por el piezómetro corresponde al acuífero superior,
es necesario implementar un sello de separación entre las secciones captantes de agua y

 - 58

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

las que no lo son (“ciegas”). Para esto, se recomienda realizar un sello sanitario de cemento
bentonita con acelerante de fraguado, desde el nivel de terreno hasta un metro bajo el
primer estrato impermeable.

**Sello de cemento**

Se instalará un sello de cemento de 0,2 m al fondo del piezómetro para asegurar que la
entrada de flujo subterráneo sea exclusivamente por el ranurado instalado en éste.

**5.3.3** **Desarrollo**

El piezómetro se desarrollará utilizando un sistema de aire comprimido y con herramientas
de ‘jetting y swab’. Se considerará que el piezómetro está desarrollado cuando se encuentre
libre de material fino como arenas finas y limos o cuando el encargado de la perforación lo

estime.

Se considera un desarrollo efectivo de al menos 18 horas, el cual no considera dentro de
este tiempo la limpieza y colocación de equipos o maquinarias.

**5.3.4** **Terminación**

Se considera un brocal de cemento cuadrado para separar el piezómetro del suelo, con
dimensiones de 0,8 m x 0,8 m, y una altura de 40 cm, de los cuales 20 cm se ubican sobre

el nivel de terreno.

Se recomienda que los piezómetros sean debidamente identificados y, en caso de ser
posible, estén en un área cercada, provistos de tapa y señalética que indiquen la prohibición
de ingreso a personas e impedir el paso de animales, para evitar alteraciones en las

mediciones.

**5.3.5** **Pruebas de Permeabilidad**

Se recomienda realizar pruebas Lefranc cada 5 metros, o slug tests, dependiendo de la
profundidad del pozo y del nivel estático.

**5.3.6** **Muestreo**

Se recomienda hacer muestreo de la columna litológica durante la perforación del
piezómetro, por lo que se sugiere obtener muestras de cutting cada 1 m y guardarlas en
bolsas plásticas para contenerlas. Éstas deberán tener una etiqueta que estará dentro de la
bolsa y será visible desde fuera y deberán estar ubicadas lejos del área de maniobras de la
perforación. La etiqueta deberá contener la fecha, nombre del piezómetro y la profundidad
de la columna que representa (comienzo y final de la profundidad de la muestra). Las cajas
deberán ser rotuladas con la misma información que la etiqueta nombrada anteriormente.
Las muestras de las bolsas serán reducidas a muestras de 1 kilo para ser almacenadas en el
lugar que se designe, y el resto será desechado una vez terminada la perforación.

 - 59

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

**5.3.7** **Ficha Técnica**

Para una correcta descripción de la estratigrafía e información asociada al piezómetro, se
deberá realizar una **Ficha Técnica de Construcción**, de acuerdo a los lineamientos que
establece la DGA para la construcción de los piezómetros que componen su red de
monitoreo nacional. En la Figura 5.3-1 se presenta, mediante referencias, una explicación
de los campos que componen la ficha.

En el encabezado se presenta la identificación del piezómetro correspondiente, la
ubicación, sus coordenadas con Datum y Huso, profundidad total alcanzada al momento de
la construcción del piezómetro, el diámetro de habilitación y la fecha de finalización de la
obra. La cota allí expresada es tomada con GPS de mano por lo que su valor es simplemente

referencial.

En el encabezado de cada ficha se registra la cota de boca del pozo medida al momento de
construcción del piezómetro con GPS de mano.

1. Los valores expresados en el recuadro corresponden a los valores de cota, desde la

boca del piezómetro hasta la profundidad final de éste.

2. Contiene una descripción de los materiales encontrados durante la construcción del

piezómetro.

3. Corresponde a un esquema gráfico de los materiales descritos en el punto 2.

4. Representa una regla métrica cuya longitud coincide con la profundidad del

piezómetro. Con ésta se puede medir la potencia de cada estrato descrito en 2) y 3), la

longitud de los tramos ciegos y filtrantes, así como la profundidad dónde se

encontraron el o los aportes de agua (7) y la distancia desde el nivel de terreno hasta

el Nivel Estático (8) al momento de finalizar los trabajos de perforación.

5. Muestra la ubicación y longitud de los tramos ciegos y filtrantes a lo largo del

piezómetro. Sus longitudes pueden ser tomadas usando (4)

6. Describe el material utilizado para el entubamiento del piezómetro y aclara cuando en

(5) se trata de un tramo filtrante o ciego.

7. A medida que el perforista avanza en la construcción del piezómetro, puede identificar

dónde aproximadamente se ubican los aportes de agua que le cambian

significativamente el agua retirada con el aire que inyecta. En el caso de la figura de

ejemplo, el primer aporte fue identificado a los 3 m de profundidad y luego todo el

perfil aporta agua al piezómetro.

8. Indica la distancia desde la superficie de terreno hasta el nivel piezométrico en el

piezómetro al momento de finalizar su construcción.

 - 60

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

|Ficha Técnica Piezómetro N°1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Propietario:|Propietario:||||Fecha:|||
|Ubicación Referencial:|Ubicación Referencial:|||||||
|**_Ubicación Georeferencial Coordenadas UTM_**|**_Ubicación Georeferencial Coordenadas UTM_**|**_Ubicación Georeferencial Coordenadas UTM_**|**_Ubicación Georeferencial Coordenadas UTM_**|**_Ubicación Georeferencial Coordenadas UTM_**|**_Ubicación Georeferencial Coordenadas UTM_**|**_Ubicación Georeferencial Coordenadas UTM_**|**_Ubicación Georeferencial Coordenadas UTM_**|
|Norte:||Este:||Huso:||Datum:||
|**_Datos Técnicos_**|**_Datos Técnicos_**|**_Datos Técnicos_**|**_Datos Técnicos_**|**_Datos Técnicos_**|**_Datos Técnicos_**|**_Datos Técnicos_**|**_Datos Técnicos_**|
|Prof (m):||Caudal:||Diámetro:||Cota (m s.n.m.):||
|Prof<br>(m)<br>Descripción<br>Descripción<br>Tiempo Perforación<br>(min/3 m)<br>Napas<br>Cota<br>(m s.n.m.)|Prof<br>(m)<br>Descripción<br>Descripción<br>Tiempo Perforación<br>(min/3 m)<br>Napas<br>Cota<br>(m s.n.m.)|Prof<br>(m)<br>Descripción<br>Descripción<br>Tiempo Perforación<br>(min/3 m)<br>Napas<br>Cota<br>(m s.n.m.)|Prof<br>(m)<br>Descripción<br>Descripción<br>Tiempo Perforación<br>(min/3 m)<br>Napas<br>Cota<br>(m s.n.m.)|Prof<br>(m)<br>Descripción<br>Descripción<br>Tiempo Perforación<br>(min/3 m)<br>Napas<br>Cota<br>(m s.n.m.)|Prof<br>(m)<br>Descripción<br>Descripción<br>Tiempo Perforación<br>(min/3 m)<br>Napas<br>Cota<br>(m s.n.m.)|Prof<br>(m)<br>Descripción<br>Descripción<br>Tiempo Perforación<br>(min/3 m)<br>Napas<br>Cota<br>(m s.n.m.)|Prof<br>(m)<br>Descripción<br>Descripción<br>Tiempo Perforación<br>(min/3 m)<br>Napas<br>Cota<br>(m s.n.m.)|

Fuente: DGA (2012)

**Figura 5.3-1 Contenido de Ficha Técnica de Piezómetro**

Finalmente, a modo de ejemplo, en las Figura 5.3-2 se entrega un esquema tipo para un
piezómetro de monitoreo de aguas subterráneas.

 - 61

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Nota: Longitudes referenciales
Fuente: Elaboración Propia
**Figura 5.3-2 Propuesta de Piezómetro de Monitoreo de Aguas Subterráneas de Operación**

**CITA y RSU**

 - 62

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

**5.4** **SISTEMA DE MONITOREO**

**5.4.1** **Variables a Monitorear**

A continuación, se indican los parámetros que deberán ser monitoreados en forma regular
y periódica (3 veces al año), distinguiendo entre parámetros de terreno y parámetros
medidos en laboratorio. Los parámetros medidos en terreno corresponden al nivel
piezométrico y parámetros fisicoquímicos in situ, identificados en la Tabla 5.4-1.

**Tabla 5.4-1 Parámetros Medidos en Terreno**

Fuente: Elaboración Propia

Por otra parte, para seleccionar los parámetros a determinar en laboratorio, se tuvo en
cuenta aquellos dispuestos en línea base (Ecobio, 2003), el monitoreo comprometido en
línea base, y monitoreo realizado por Ecobio entre 2012 y 2017. Finalmente, se seleccionó
un conjunto de parámetros, teniendo en cuenta aquellos que actualmente monitorea
Ecobio, y agregando 9 parámetros, que permitirán dar cuenta de la NCh 1333 como
Requisito para Agua de Riego, de manera referencial.

El conjunto completo de parámetros definidos para el seguimiento de la calidad del agua se

indica en la Tabla 5.4-2.

|Tabla 5.4-2 Parámetros Analizados en Laboratorio|Col2|Col3|
|---|---|---|
|**Parámetro**|**Parámetro**|**Unidad**|
|**PARÁMETROS FÍSICO - QUÍMICOS**|Conductividad Eléctrica|μS/cm|
|**PARÁMETROS FÍSICO - QUÍMICOS**|Fenol|mg/l|
|**PARÁMETROS FÍSICO - QUÍMICOS**|pH|-|
|**PARÁMETROS FÍSICO - QUÍMICOS**|Sólidos Disueltos Totales (*)|mg/l|
|**PARÁMETROS FÍSICO - QUÍMICOS**|Solidos Suspendidos Totales|mg/l|
|**PARÁMETROS FÍSICO - QUÍMICOS**|Temperatura|°C|
|**MACROELEMENTOS**|Cloruro|mg/l|
|**MACROELEMENTOS**|Disulfuro|mg/l|
|**MACROELEMENTOS**|Fluoruro|mg/l|
|**MACROELEMENTOS**|Potasio|mg/l|
|**MACROELEMENTOS**|Sulfato|mg/l|

DISEÑO RED DE MONITOREO

 - 63
MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

|Parámetro|Col2|Unidad|
|---|---|---|
|**COMPUESTOS ORGÁNICOS**|Aceites y Grasas|mg/l|
|**COMPUESTOS ORGÁNICOS**|DBO5|mg O2/l|
|**COMPUESTOS ORGÁNICOS**|DQO|mg O2/l|
|**COMPUESTOS ORGÁNICOS**|Nitrógeno Kejdal|mg/l|
|**COMPUSTOS INORGÁNICOS**|Amoniaco|mg/l|
|**COMPUSTOS INORGÁNICOS**|Cianuro|mg/l|
|**COMPUSTOS INORGÁNICOS**|Fosforo Total|mg/l|
|**COMPUSTOS INORGÁNICOS**|Nitrato|mg/l|
|**COMPUSTOS INORGÁNICOS**|Nitrito|mg/l|
|**COMPUSTOS INORGÁNICOS**|Nitrógeno Amoniacal|mg/l|
|**COMPUSTOS INORGÁNICOS**|Razón Nitrato + Nitrito|-|
|**COMPUSTOS INORGÁNICOS**|Sodio (*)|mg/l|
|**MICROELEMENTOS**|Aluminio|mg/l|
|**MICROELEMENTOS**|Arsénico|mg/l|
|**MICROELEMENTOS**|Bario (*)|mg/l|
|**MICROELEMENTOS**|Berilio (*)|mg/l|
|**MICROELEMENTOS**|Boro|mg/l|
|**MICROELEMENTOS**|Cadmio|mg/l|
|**MICROELEMENTOS**|Cobalto (*)|mg/l|
|**MICROELEMENTOS**|Cobre|mg/l|
|**MICROELEMENTOS**|Cromo|mg/l|
|**MICROELEMENTOS**|Cromo Hexavalente|mg/l|
|**MICROELEMENTOS**|Hierro|mg/l|
|**MICROELEMENTOS**|Litio (*)|mg/l|
|**MICROELEMENTOS**|Litio (cítricos) (*)|mg/l|
|**MICROELEMENTOS**|Magnesio|mg/l|
|**MICROELEMENTOS**|Manganeso|mg/l|
|**MICROELEMENTOS**|Mercurio|mg/l|
|**MICROELEMENTOS**|Molibdeno|mg/l|
|**MICROELEMENTOS**|Níquel|mg/l|
|**MICROELEMENTOS**|Plata (*)|mg/l|
|**MICROELEMENTOS**|Plomo|mg/l|
|**MICROELEMENTOS**|Selenio|mg/l|
|**MICROELEMENTOS**|Vanadio (*)|mg/l|
|**MICROELEMENTOS**|Zinc|mg/l|
|**COMPUESTOS MICROBIOLÓGICOS**|Col Fecales|NMP/100 ml|
|**OTROS**|Benceno|μg/l|
|**OTROS**|Cloroformo|mg/l|
|**OTROS**|Hidrocarburos|mg/l|
|**OTROS**|Hidrocarburos Totales|mg/l|
|**OTROS**|Hidrocarburos Volátiles|mg/l|

DISEÑO RED DE MONITOREO

- 64
MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

|Parámetro|Col2|Unidad|
|---|---|---|
|**OTROS**|Óxido de Hierro|mg/l|
|**OTROS**|Pentaclorofenol|μg/l|
|**OTROS**|Pentacloruro|mg/l|
|**OTROS**|Poder Espumógeno|mm|
|**OTROS**|Tetracloroeteno|μg/l|
|**OTROS**|Tolueno|μg/l|
|**OTROS**|Triclorometano|mg/l|
|**OTROS**|Triclorometilo|mg/l|
|**OTROS**|Xileno|μg/l|

Nota (*): Parámetros incorporados para cumplir con NCh 1333 - Riego
Fuente: Elaboración Propia

Por último, durante el registro y muestreo en terreno se deberá dejar constancia de las
condiciones climáticas del día en el cual se realice el trabajo, indicando al menos fecha,
hora, temperatura ambiente, presencia de lluvia, o cualquier situación que pudiese afectar

el análisis.

**5.4.2** **FRECUENCIA Y DURACIÓN DE MUESTREO**

Se considera adecuada una frecuencia de muestreo cada cuatro meses, de manera de
caracterizar estacionalmente la calidad de las aguas subterráneas en el sistema;
monitoreando preferentemente los meses de febrero, junio y octubre.

En particular, se recomienda que los dos pozos habilitados en el acuífero intermedio, se
monitoreen con una frecuencia anual en una campaña coincidente con el monitoreo del
acuífero superior.

La toma de muestras deberá hacerse dentro de los primeros 5 días del mes en cuestión
simultáneamente, es decir, en todos los puntos de monitoreo en un mismo día
preferiblemente.

Finalmente, el monitoreo deberá ejecutarse durante toda la operación del proyecto Ecobio,
extendiéndose 20 años después de su cierre.

**5.4.3** **Procedimiento de Toma de Muestra**

Es importante que en cada muestreo se lleve a cabo los protocolos de monitoreo,
preservación y transporte de muestra para su posterior análisis químico. Cada muestra debe
ser previamente etiquetada para su identificación y preservada de acuerdo con el
parámetro que se requiera determinar posteriormente, y transportadas y almacenadas a
una temperatura aproximada de 12°C. Así también, Los equipos que se utilicen para las
mediciones in-situ deberán llevarse previamente revisados, descontaminados y calibrados.

 - 65

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

Los envases deben ser con tapa de boca ancha de polietileno, propileno o policarbonato de
250 o 500 ml y de 1 litro; y de vidrio de 250 o 500 ml. Los envases de polietileno se usan en
la mayoría de los análisis físicos y químicos, sin embargo, algunos elementos pueden
absorberse en las paredes.

Las condiciones de preservación y manejo de las muestras se regirán en base a las
metodologías establecidas en la norma chilena NCh411/3. Of96. Calidad del aguaMuestreo - Parte 3: Guía sobre la preservación y manejo de las muestras. Los preservantes
que se indican de acuerdo a la anterior norma deberán ser transportados a terreno,
previamente identificados y separados. Es fundamental que se tenga precaución por las
medidas que se tomarán para asegurar la cadena de custodia de las muestras, considerando
eventuales problemas de transporte y preservación de las muestras.

Para la extracción de la muestra debe desecharse (purgar) un volumen de agua igual al triple
del volumen de agua almacenado en el pozo, para asegurar que la muestra represente las
condiciones del acuífero y no del agua estancada dentro del pozo.

Se considerarán laboratorios acreditados en Chile, el cual será el responsable de ejecutar el
Plan de Muestreo, de los respectivos análisis, y los informes de resultados. Estos deberán
incluir los datos de identificación de la muestra, personas responsables y sus firmas, las
fechas de muestreo y análisis, como otra información que se estime relevante para una
correcta presentación de los informes a las autoridades.

 - 66

DISEÑO RED DE MONITOREO

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

# CAPÍTULO 6 CONCLUSIONES

De acuerdo con el presente informe, se tienen las siguientes conclusiones y recomendaciones:

- Los 4 pozos de exploración perforados con el método de percusión con cable, permitieron

identificar de manera más adecuada y con mayor precisión las columnas litológicas de los
sondajes; definiendo con mayor exactitud los estratos que efectivamente constituirían
unidades acuíferas, respecto de aquellas que no. Los 4 sondajes identificaron los mismos
estratos, a profundidades y espesores similares, indicando la uniformidad espacial del
sistema. En un primer tramo, se identificó un horizonte compuesto por materiales que
constituyen una unidad prácticamente impermeable, catalogada como un acuitardo. Más
en profundidad, se identificó un acuífero superior, bajo éste un nuevo estrato acuitardo,
al cual lo subyace un acuífero intermedio.

- En los trabajos elaborados para Ecobio (2003) se identificó entre los 4 y 8 metros de

profundidad un estrato compuesto por material gravoso con presencia de arcillas, y arena
semiconsolidada; que fue descritos como una unidad acuífera. Con la interpretación de
los nuevos trabajos, se identificó de manera más precisa dicho estrato, con características
que lo catalogan ciertamente como un acuitardo; estrato de baja permeabilidad, que
puede almacenar y transmitir agua a una tasa muy reducida a casi nula.

- A partir de la antigua y nueva información generada en terreno, se desarrolló un modelo

conceptual del sistema hidrogeológico, en el cual se definió la geometría de los estratos,
parámetros hidrogeológicos, la conceptualización del flujo subterráneo, y un balance
hidrogeológico preliminar en el sector de estudio.

- A partir del modelo conceptual, se construyó un modelo numérico de flujo en Visual

MODFLOW, del cual se obtuvo un buen ajuste de los datos observados y simulados, con
estadígrafos de calibración de un MAE normalizado de 2,36% y un RMS normalizado de
2,57%, cumpliendo con las sugerencias del SEA. Es decir, el modelo es capaz de
representar adecuadamente el sistema de flujo en el sector de estudio, siendo adecuado
para realizar la estimación de movilidad de contaminante en el acuífero.

- Mediante el uso del módulo MODPATH de Visual MODFLOW, se implementó un escenario

de simulación predictivo, que permitió analizar la movilidad de flujo y un eventual
contaminante en el sistema subterráneo, proveniente desde la operación de la planta
mediante líneas de trayectorias proyectadas hasta el año 2053. A pesar de que los sitios
donde se emplazan el CITA y el RSU cuentan con una zona de impermeabilización en toda

 - 67

CONCLUSIONES

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

su base, para evaluar la potencial movilidad de contaminante, se consideraron eventuales
zonas de fuga o falla para la situación actual y futura, a partir de las cuales una partícula
contaminante pudiese infiltrar al sistema subterráneo. De manera conservadora, se
supuso que una eventual partícula contaminante infiltraría directamente en el acuífero
superior; y se incorporó al modelo en el eventual momento de falla y en qué celda se
produce.

- Los resultados indican que las trayectorias de partículas se dirigen en el sentido del flujo

subterráneo: suroriente-norponiente; con un potencial contaminante recorriendo entre
65 y 130 metros en el periodo de modelación (2019-2053), desde las zonas de falla. Esto
se debe a la baja permeabilidad de la zona evaluada, el gradiente hidráulico del sistema
subterráneo, y de la fecha en la cual se depositaría una potencial partícula.

- Conforme al modelo de flujo y movilidad de contaminante, se definió una red de 13

piezómetros de monitoreo, compuesta por 1 piezómetro aguas arriba de la operación RSU
y CITA; 1 piezómetro para detectar eventuales fallas del deslinde actual del RSU; 3
piezómetros para la proyección del RSU; 2 piezómetros para la actual ubicación del CITA;
y 4 piezómetros para la proyección del CITA. Por último, el sistema lo completan los dos
pozos habilitados en el acuífero intermedio, aguas arriba y aguas abajo de la operación
RSU y CITA, que se han propuesto de manera conservadora.

- Con esta configuración cualquier alteración en la calidad de las aguas será identificada d

manera temprana en el sistema subterráneo de influencia directa del CITA y RSU, ya sea
en su situación actual o proyectada.

- Dentro de las variables a monitorear, se seleccionó un conjunto de parámetros, teniendo

en cuenta aquellos que actualmente monitorea ECOBIO, y agregando 9 parámetros, que
permitirán dar cuenta de la NCh 1333 como Requisito para Agua de Riego, de manera

referencial.

- Como parte de los 10 piezómetros que se proyectan en la red de monitoreo, se entregan

las especificaciones técnicas y recomendaciones para su construcción.

Félix Pérez S.

**Director Ejecutivo**

**HIDRICA Consultores**

Génova 2015, Oficina 11 Providencia

**[www.hidricaconsultores.cl](http://www.hidricaconsultores.cl/)**

 - 68

CONCLUSIONES

MODELO HIDROGEOLÓGICO CONCEPTUAL Y

NUMÉRICO RELLENOS RSU Y CITA

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.3-1: Resumen de Ensayos Slug Test Realizados****

| Pozo | Ensayos | Rango Ensayos (m) | Col4 | Acuitardo<br>Superficial | Acuífero<br>Superior | Acuitardo<br>Intermedio | Acuífero<br>Intermedio | Acuitardo<br>Inferior | Acuífero<br>Inferior |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Pozo** | **Ensayos** | **Inicio** | **Fin** | **Fin** | **Fin** | **Fin** | **Fin** | **Fin** | **Fin** |
| PM1-I | 6 | 7 | 30 | X | X | X | X |  | X |
| PM2-S | 7 | 3 | 37 | X | X | X | X |  |  |
| PM3-I | 7 | 4 | 40 | X | X | X | X | X |  |
| PM6-S | 6 | 6 | 35 | X | X | X | X |  |  |

**Tabla 2.4-1: Resumen de Transmisividades (m** **[2]** **/d)****

| Método | PM1-I | PM2-S | PM3-I | PM6-S |
| --- | --- | --- | --- | --- |
| Theis | 1,61 | - | 1,11 | 0,84 |
| Theis Jacob | 2,00 | - | 1,41 | 1,33 |
| Cooper Jacob I | 1,62 | - | 1,73 | 2,09 |
| Theis Recovery | 1,92 | 0,97 | 2,09 | 4,83 |
| Promedio<br> | 1,79 | 0,97 | 1,59 | 2,27 |

**Tabla 2.4-2: Resumen de Permeabilidades (m/d)****

| Método | PM1-I | PM2-S | PM3-I | PM6-S |
| --- | --- | --- | --- | --- |
| Theis | 0,32 | - | 0,28 | 0,21 |
| Theis Jacob | 0,40 | - | 0,35 | 0,33 |
| Cooper Jacob I | 0,32 | - | 0,43 | 0,52 |
| Theis Recovery | 0,38 | 0,16 | 0,52 | 1,21 |
| Promedio<br> | 0,36 | 0,16 | 0,40 | 0,57 |

**Tabla 3.2-1: Resumen de Permeabilidad de Sistemas Acuíferos Identificados****

| Acuífero | Profundidad Aproximada<br>desde Terreno (m) | Espesor<br>(m) | Permeabilidad<br>Pruebas Terreno<br>(m/d) | Permeabilidad<br>Bibliografía (**)<br>(m/d) |
| --- | --- | --- | --- | --- |
| Acuífero Superior | Desde 11 - 13 | 2 - 6 | 0,16 - 1,21 | 1 - 100 |
| Acuífero Intermedio | Desde 23 - 36 | 4 - 5 | 0,28 - 0,52 | 0,01 - 1 |
| Acuífero Inferior | Desde 30 - 40 | 2 (*) | - | 0,01 - 1 |

**Tabla 3.2-2: Resumen de Coeficientes de Almacenamiento de Sistemas Acuíferos****

| Acuífero | Profundidad Aproximada<br>desde Terreno (m) | Espesor<br>(m) | Almacenamiento<br>Bibliografía (**) |
| --- | --- | --- | --- |
| Acuífero Superior | Desde 11 - 13 | 2 - 6 | 10-04 - 10-03 |
| Acuífero Intermedio | Desde 23 - 36 | 4 - 5 | 10-04 - 10-03 |
| Acuífero Inferior | Desde 30 - 40 | 2 (*) | 10-04 - 10-03 |

**Tabla 3.2-3: Resumen de Permeabilidad de Acuitardos Identificados****

| Acuitardo | Profundidad Aproximada<br>desde Terreno (m) | Espesor<br>(m) | Permeabilidad<br>Pruebas Terreno<br>(m/d) | Permeabilidad<br>Bibliografía (**)<br>(m/d) |
| --- | --- | --- | --- | --- |
| Acuitardo Superior | - | 11 - 13 | - | 10-04 - 10-01 |
| Acuitardo Intermedio | Desde 13 - 19 | 10 - 18 | - | 10-04 - 10-01 |
| Acuitardo Inferior | Desde 28 - 41 | 2 - 3 | - | 10-04 - 10-01 |

**Tabla 3.3-2: Resumen de Niveles Piezométricos en Nuevos Pozos de Monitoreo****

| Campaña | PM3-I | Col3 | PM1-I | Col5 | PM6-S | Col7 | PM2-S | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Campaña | Acuífero Intermedio | Acuífero Intermedio | Acuífero Intermedio | Acuífero Intermedio | Acuífero Superior | Acuífero Superior | Acuífero Superior | Acuífero Superior |
| Campaña | Fecha | Cota Nivel<br>(m s.n.m.) | Fecha | Cota Nivel<br>(m s.n.m.) | Fecha | Cota Nivel<br>(m s.n.m.) | Fecha | Cota Nivel<br>(m s.n.m.) |
| 1 | 08-mar | 107,5 | 26 -feb | 104,5 | 07-mar | 105,2 | 27-feb | 106,0 |
| 2 | 01-abr | 106,9 | 01-abr | 105,0 | 01-abr | 105,7 | 01-abr | 106,3 |
| 3 <br> | 11-abr<br> | 108,0 | 11-abr | 104,8 | 11-abr | 105,6 | 11-abr | 105,8 |

**Tabla 3.3-3: Resumen de Profundidad a Niveles Piezométrico en Antigua Red de Monitoreo****

| Piezómetro | E WGS84<br>(m) | N WGS84<br>(m) | Fecha<br>Monitoreo | Prof Nivel<br>(m) |
| --- | --- | --- | --- | --- |
| Prsu4 | 752.528 | 5.935.117 | 01-04-2019 | Seco |
| PC1 | 751.980 | 5.935.644 | 01-04-2019 | Seco |
| PC2 | 751.725 | 5.935.700 | 01-04-2019 | Seco |
| P1 | 752.275 | 5.935.173 | 01-04-2019 | Seco |
| PC4 | 751.628 | 5.935.339 | 01-04-2019 | Seco |
| PC3<br> | 751.889<br> | 5.935.265 | 01-04-2019 | Seco |

**Tabla 3.5-2: Recarga Media Anual por Concepto de Precipitación****

| CN | γ<br>(factor empírico) | Pp Anual Media<br>(mm) | Rec Media Anual<br>(mm) | Rec Media Anual<br>(l/s) |
| --- | --- | --- | --- | --- |
| 97,3<br> | 0,0067<br> | 867 | 0,5 | 0,15 |

**Tabla 4.1-3: Recarga por Precipitación en Modelo Numérico****

| Año | Recarga (l/s) |
| --- | --- |
| 2015 | 0,14 |
| 2016 | 0,13 |
| 2017 | 0,18 |
| 2018 | 0,16 |
| 2019 | 0,14 |

**Tabla 4.2-2: Estadígrafos Calibración****

| Parámetro | Fórmula | Valor |
| --- | --- | --- |
| Coeficiente de<br>Determinación (R2) | <br> | 0,998 |
| Error Medio (m) |  | 0,057 |
| MAE Normalizado (%) | MAE<br>max(Nobs) −min (Nobs) | 2,36 |
| RMS Normalizado (%) |  | 2,57 |

**Tabla 4.2-3: Balance Hidrogeológico- Promedio 2015-2019****

| Entradas | Volumen (m3) | Caudal (l/s) |
| --- | --- | --- |
| Recarga por Precipitación | 1.005 | 0,14 |
| Flujo Regional | 2.487 | 0,36 |
| Total Entradas | 3.491 | 0,50 |
| <br> <br> | <br> <br> | <br> <br> |
| **Salidas** |  |  |
| Flujo Regional | 3.502 | 0,50 |
| Total Salidas | 3.502 | 0,50 |
| <br> <br> | <br> <br> | <br> <br> |
| **Variación de Almacenamiento** | 6 | 0,00001 |
| **Balance** | -10,9 | -0,002 |
| **Error Balance**<br> | -0,3% | -0,4% |

**Tabla 5.2-1: Resumen Red de Monitoreo****

| Piezómetro | Acuífero<br>Habilitado | Objetivo | Ubicación Referencial |
| --- | --- | --- | --- |
| PM3-S | Superior | Monitorear aguas arriba<br>operación Ecobio: RSU y CITA | Extremo suroriente de RSU |
| PM12-S | Superior | Monitorear aguas abajo proyección<br>crecimiento de RSU oriente | Norte de proyección de RSU |
| PM9-S | Superior | Monitorear aguas abajo<br>deslinde actual RSU | Norte del RSU |
| PM8-S | Superior | Monitorear aguas abajo proyección<br>crecimiento de RSU poniente | Norte de proyección de RSU |
| PM7-S | Superior | Monitorear aguas abajo proyección<br>crecimiento de RSU poniente | Norte de proyección de RSU |
| PM5-S | Superior | Monitorear aguas abajo<br>deslinde actual CITA | Norte del CITA |
| PM2-S | Superior | Monitorear aguas abajo<br>deslinde actual CITA | Norte del CITA.<br>Ya construido |
| PM4-S | Superior | Monitorear aguas abajo proyección<br>crecimiento CITA poniente | Norte de proyección de CITA |
| PM10-S | Superior | Monitorear aguas abajo proyección<br>crecimiento CITA poniente | Norte de proyección de CITA |
| PM1-S | Superior | Monitorear aguas abajo proyección<br>crecimiento CITA poniente | Extremo norponiente de<br>proyección de CITA |
| PM11-S | Superior | Monitorear aguas abajo proyección<br>crecimiento CITA poniente | Extremo poniente<br>de proyección de CITA |
| PM3-I | Intermedio | Monitorear aguas arriba<br>operación Ecobio: RSU y CITA | Extremo suroriente de<br>proyección oriente RSU.<br>Ya construido |
| PM1-I | Intermedio | Monitorear aguas abajo<br>proyección crecimiento CITA | Extremo norponiente de<br>proyección poniente de CITA.<br>Ya construido |

**Tabla 5.2-2: Características Red de Monitoreo****

| Piezómetro | E WGS84<br>(m) | N WGS84<br>(m) | Profundidad de<br>Perforación<br>Estimada (m) | Diámetro<br>Habilitación<br>(") | Material | Profundidad<br>Estimada de<br>Ranurado (m) |
| --- | --- | --- | --- | --- | --- | --- |
| PM1-S | 751.383 | 5.935.749 | 20 | 6 | PVC | 12-19 |
| PM2-S (*) | 751.976 | 5.935.642 | 42 | 6 | PVC | 13-19 |
| PM3-S | 753.138 | 5.934.983 | 20 | 6 | PVC | 12-19 |
| PM4-S | 751.842 | 5.935.649 | 20 | 6 | PVC | 12-19 |
| PM5-S | 752.119 | 5.935.596 | 20 | 6 | PVC | 12-19 |
| PM7-S | 752.384 | 5.935.511 | 20 | 6 | PVC | 12-19 |
| PM8-S | 752.526 | 5.935.476 | 20 | 6 | PVC | 12-19 |
| PM9-S | 752.739 | 5.935.422 | 20 | 6 | PVC | 12-19 |
| PM10-S | 751.623 | 5.935.702 | 20 | 6 | PVC | 12-19 |
| PM11-S | 751.366 | 5.935.546 | 20 | 6 | PVC | 12-19 |
| PM12-S | 753.122 | 5.935.334 | 20 | 6 | PVC | 12-19 |
| PM3-I (*) | 753.182 | 5.934.982 | 42 | 6 | PVC | 33-37 |
| PM1-I (*) | 751.384 | 5.935.769 | 33 | 6 | PVC | 23-28 |
