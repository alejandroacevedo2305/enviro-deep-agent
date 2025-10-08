---
title: Informe Láser Aerotransportado
author: Cliente: Ingeniería Cuatro S.A. Fecha: Junio 2016
date: D:20171002174229-03'00'
language: es
type: report
pages: 26
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Informe Láser Aerotransportado
-->

# Informe Láser Aerotransportado

## 2229 Bocatoma Portillo

### Cliente: Tinguiririca Energía Fecha: Octubre 2017

INFORME LiDAR

**CONTENIDO**

**1.** **IDENTIFICACIÓN ................................................................................................................ 3**

**2.** **ANTECEDENTES .................................................................................................................. 4**

**3.** **METODOLOGÍA DE TRABAJO ........................................................................................ 5**
3.1 PLANIFICACIÓN DE VUELO ................................................................................ 5
3.1.1 METEOROLOGÍA .................................................................................................... 7
3.2 EJECUCIÓN DEL VUELO ...................................................................................... 8
3.3 EVALUACIÓN DE LOS DATOS OBTENIDOS EN VUELO .............................. 10

3.4 CONTROL DE COBERTURA ............................................................................... 11

3.5 PROCESAMIENTO DE DATOS ........................................................................... 12
3.5.1 PROCESO DE FOTOGRAFÍAS ............................................................................. 12

3.5.2 REVELADO ............................................................................................................ 12
3.5.3 ARCHIVO DE ORIENTACIÓN DE CADA FOTO ............................................... 14
3.5.4 ORTORECTIFICACIÓN ........................................................................................ 15

3.5.5 MOSAICO ............................................................................................................... 16

3.6 PROCESO DE NUBE DE PUNTOS ...................................................................... 17

3.7 MODELO DIGITAL DE TERRENO (DTM) ......................................................... 18
3.8 MODELO DIGITAL DE SUPERFICIE (DSM) ..................................................... 18
3.9 CURVAS DE NIVEL Y PLANIMETRÍA .............................................................. 19

**4.** **RED GEODÉSICA ............................................................................................................... 20**

**5.** **EQUIPAMIENTO EMPLEADO ........................................................................................ 22**
4.1 TRABAJOS DE TERRENO .................................................................................... 22
4.2 PRODUCCIÓN DE CARTOGRAFÍA LÁSER ...................................................... 22

**6.** **PRODUCTOS OBTENIDOS ............................................................................................... 24**

2229 Bocatoma Portillo
Revisión: 01 Página 1 de 25

INFORME LiDAR

**ÍNDICE DE IMÁGENES**

Ilustración 1. Referencia ubicación geográfica ........................................................................................................ 3
Ilustración 2 . Imagen referencial de captura de datos ............................................................................................. 5
Ilustración 3. Líneas de vuelo planificadas............................................................................................................... 6
Ilustración 4. Meteorología. ..................................................................................................................................... 7
Ilustración 5. Trayectoria de vuelo realizado ........................................................................................................... 9
Ilustración 6. Cobertura del levantamiento ............................................................................................................. 11

Ilustración 7. Imagen en formato nativo ................................................................................................................. 13
Ilustración 8. Resultado de revelado ....................................................................................................................... 13
Ilustración 9. Balance de brillos y contrastes ......................................................................................................... 13
Ilustración 10. Proceso de enfoque ......................................................................................................................... 13
Ilustración 11. EO-file ............................................................................................................................................ 14

Ilustración 12. Ortofotografía ................................................................................................................................. 15
Ilustración 13. Mosaico preliminar y mosaico final (balanceado) .......................................................................... 16
Ilustración 14. Representación 3D de nube de puntos con atributos RGB ............................................................. 17
Ilustración 15. Modelo digital de terreno ............................................................................................................... 18
Ilustración 16. Modelo digital ................................................................................................................................ 18
Ilustración 17. Cartografía del área de estudio ....................................................................................................... 19
Ilustración 18. Imagen panorámica vértice EVELYN ............................................................................................ 20
Ilustración 19. Imagen de detalle vértice EVELYN ............................................................................................... 20
Ilustración 20. Imagen panorámica vértice PR-1 ................................................................................................... 21

**ÍNDICE DE TABLAS**

Tabla 1. Parámetros láser escala 1/500 ..................................................................................................................... 5
Tabla 2. Parámetros foto digital escala 1/500 ........................................................................................................... 5
Tabla 3. Estación de apoyo 1 .................................................................................................................................... 8
Tabla 4. Estación de apoyo 2 .................................................................................................................................... 8
Tabla 5. Control de cambios documento ................................................................................................................ 25

2229 Bocatoma Portillo
Revisión: 01 Página 2 de 25

INFORME LiDAR

**1.** **IDENTIFICACIÓN**

### Tinguiririca Energía, ha encomendado a AEROTOP S.A., la ejecución del

“Levantamiento con Tecnología Láser y Confección de Ortofotos” a escala 1/500 del proyecto
“Valle del Tinguiririca sector Bocatoma Portillo” El proyecto está ubicado geográficamente
en la VI Región del Libertador General Bernardo O'Higgins. Comprende al área de influencia
del polígono entregado por el cliente.

**Ilustración 1. Referencia ubicación geográfica**

2229 Bocatoma Portillo
Revisión: 01 Página 3 de 25

INFORME LiDAR

**2.** **ANTECEDENTES**

Aerotop consta con un equipo de Laser Aero-transportado LiDAR _(Light Detection_
_and Ranging)._ Este sistema consiste en tres componentes principales:

 - Sistema de posicionamiento;

 - Sistema de adquisición de imágenes;

 - Sistema de escaneo láser terrestre.

El componente de posicionamiento del sistema está compuesto por una Plataforma de
Movimiento Inercial (IMU), un GPS (Global Positioning System) instalado abordo y un
estación GPS base, proveyendo posicionamiento en modo diferencial (DGPS). Los datos del
instrumental mencionado son combinados para proporcionar un preciso posicionamiento 3D
en coordenadas absolutas del sensor de escaneo durante el tiempo de emisión del láser. Para
minimizar errores en los cálculos del DGPS (Differential Global Positioning System), el rango
permisible de vuelo desde la estación base y la proximidad de ésta al área del proyecto son
seleccionadas para asegurar que se cumplan los requerimientos de precisión del proyecto.

Para el desarrollo de este trabajo se contó con los siguientes antecedentes:

 - Escala de Proyecto: 1/500

 - Tipo de Relieve: Cordillera

 - Tipo de Vegetación: Baja (Ciudad - Cordillera Alta)

 - Productos a entregar:

 - Tile Index en formato dwg, que muestra una vista general del área,

junto a la nomenclatura de cada archivo.

 - Modelo Digital de Terreno: DTM en formato ASCII con tamaño de

píxel de 0,25 m.

 - Ortofoto a color en formato Geotiff con tamaño de píxel de 0,1 m

 - Curvas de nivel cada 0,5 m con la vectorización en 3D, toponimia y

ortofoto ecw insertada.

2229 Bocatoma Portillo
Revisión: 01 Página 4 de 25

INFORME LiDAR

**3.** **METODOLOGÍA DE TRABAJO**

Planificación de vuelo, aplicando parámetros para escala 1/500:

 - Medición GPS de los vértices EVELYN, PR- 01, utilizados como apoyo al vuelo.

**3.1** **PLANIFICACIÓN DE VUELO**

Según lo anterior, se realizó la planificación del vuelo con los siguientes parámetros
ajustados a las especificaciones solicitadas por el cliente:

**Tabla 1. Parámetros láser escala 1/500**

|Características de los puntos|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|ΔX (m.)<br>ΔY (m.)<br>Espaciamiento<br>Densidad (pt/m2)|0,58 <br>0,58<br>0,58<br>3,01|Densidad ptos. :<br>Resolución Hz:<br>Resolución V:|**DSM**<br>6,0<br>0,097<br>0,155|**DTM**<br>5,418<br>0,108<br>0,186|

**Tabla 2. Parámetros foto digital escala 1/500**

|Características de la foto|Col2|Col3|
|---|---|---|
|Tamaño px:<br>Resolución:<br>Escala: 1/500|0,087<br>250<br>855|m.<br>dpi<br>|

**Ilustración 2 . Imagen referencial de captura de datos**

2229 Bocatoma Portillo
Revisión: 01 Página 5 de 25

INFORME LiDAR

A continuación se presentan los trazados de las líneas de vuelo correspondientes al
proyecto.

**Ilustración 3. Líneas de vuelo planificadas**

La planificación de la escala requerida se realizó en base a las características de los
equipos utilizados para la captura de datos. Estos son: Láser Toposys Harrier 56/G4 - Riegl
LMS-Q560, Cámara Rollei AIC P45 (Distancia focal: 47 mm).

Durante la planificación se ha tenido en cuenta la reflectividad del terreno, los
elementos e infraestructuras subyacentes, vegetación y orografía, de manera de obtener los
datos que permitan representar la zona apropiadamente.

2229 Bocatoma Portillo
Revisión: 01 Página 6 de 25

INFORME LiDAR

**3.1.1** **METEOROLOGÍA**

Junto al estudio de la planificación de líneas de vuelo, se determinó los días óptimos
para el vuelo dentro de los plazos establecidos para su ejecución. Las condiciones
meteorológicas para esta fecha fueron informadas a través del Servicio Meteorológico de
Chile, y el reporte señala: Sin nubes bajo los 5,000 pies o bajo del MSA (Mínimo de
Seguridad del Aeródromo), sin cumulonimbus y sin fenómenos de tiempo significativo en el
aeródromo o alrededores.

Se adjunta a este reporte un detalle de la carta sinóptica otorgada por el servicio de
imaginería de la Administración Nacional de la Aeronáutica y del Espacio (NASA, EE.UU.),
que permite una visualización general de la zona de interés (recuadro rojo) y sectores
aledaños.

**Ilustración 4. Meteorología.**

_Fuente: worldview.earthdata.nasa.gov_

2229 Bocatoma Portillo
Revisión: 01 Página 7 de 25

INFORME LiDAR

**3.2** **EJECUCIÓN DEL VUELO**

Eligiendo los horarios de trabajo adecuados para la zona y siempre dentro de los
ángulos solares propicios para la toma fotográfica, se maximizaron el tiempo y los recursos
para poder llevar a cabo el vuelo dentro de los plazos programados.

La base de operaciones para el vuelo fue el aeródromo de Tobalaba y la fecha en que
se efectuó es la siguiente:

 - Vuelo 17091501: 15 de Septiembre del 2017

Como apoyo al vuelo se utilizaron las siguientes bases GPS.

**Tabla 3. Estación de apoyo 1**

|Estación EVELYN|Col2|
|---|---|
|Este (m)<br>Norte (m)<br>Altura (m)|343.033,105<br>6.153.195,762<br>750,071|

**Tabla 4. Estación de apoyo 2**

|Estación PR-01|Col2|
|---|---|
|Este (m)<br>Norte (m)<br>Altura (m)|343.069,422<br>6.153.082,415<br>778,062|

_Nota:_ Las coordenadas están referidas al Datum SIRGAS2000 (WGS-84) sobre proyección
UTM Huso 19 Sur, y la elevación del punto corresponde a la cota Elipsoidal.

2229 Bocatoma Portillo
Revisión: 01 Página 8 de 25

INFORME LiDAR

A continuación, se grafica la trayectoria desarrollada por la aeronave en la zona de
trabajo:

**Ilustración 5. Trayectoria de vuelo realizado**

_Fuente: Google Earth_

2229 Bocatoma Portillo
Revisión: 01 Página 9 de 25

INFORME LiDAR

**3.3** **EVALUACIÓN DE LOS DATOS OBTENIDOS EN VUELO**

Una vez concretado el vuelo, se realiza la evaluación del mismo que comienza con el
cálculo de la trayectoria. Posterior a este proceso, obtenemos los datos necesarios para hacer
cálculo de cobertura y estimar la precisión de los datos capturados.

En general los puntos importantes que se revisan en esta etapa, de acuerdo a los
gráficos resultantes son:

 - Error medio cuadrático en posición para cada instante de la trayectoria durante el

vuelo.

 - Errores respectivos a los movimientos angulares de alabeo, cabeceo y guiñada.

 - Parámetros de velocidad del avión y altura de vuelo.

 - No se recomiendan giros con un ángulo mayor a 30o en los virajes y 5o dentro de la

línea.

 - Aceleraciones que afectan al eje vertical Z y que dan indicación del efecto de

turbulencia a lo largo del vuelo.

 - Evaluación individual a las mediciones GPS obtenidas durante el vuelo.

 - Número de satélites usados en el proceso, para obtener una trayectoria de calidad se

recomienda un número superior a 6 satélites, si esta condición no se cumple las líneas
son repetidas para garantizar la calidad de los datos.

2229 Bocatoma Portillo
Revisión: 01 Página 10 de 25

INFORME LiDAR

**3.4** **CONTROL DE COBERTURA**

En la imagen presentada a continuación, se observan las coberturas de las mediciones
láser sobre el polígono proyectado. Como se puede observar, no existen zonas sin cobertura y
se asegura que la información cubre en un 100% el área solicitada por el cliente.

**Ilustración 6. Cobertura del levantamiento**

2229 Bocatoma Portillo
Revisión: 01 Página 11 de 25

INFORME LiDAR

**3.5** **PROCESAMIENTO DE DATOS**

Una vez evaluadas las trayectorias y coberturas, se procede a la descarga de datos
capturados por la cámara digital y el equipo láser.

En esta parte el trabajo se divide en dos etapas, una para el proceso de la nube de
puntos y otra para las fotografías. A continuación se describen cada una de ellas.

Para ello también se analiza el tipo de proyección y Datum el cual el cliente desea:

**Proyección:** UTM HUSO 19 SUR.
**Datum:** Sirgas2000

**3.5.1** **PROCESO DE FOTOGRAFÍAS**

Después que las imágenes son descargadas siguen las siguientes etapas:

 - Revelado

 - Obtención de archivo que permite la orientación de cada foto

 - Ortorectificación

 - Confección de Mosaico

 - Preparación de imagen final

**3.5.2** **REVELADO**

En esta etapa las imágenes son transformadas de su formato nativo a un formato que
permite ser reconocido por los programas que se utilizan en los siguientes procesos. Además
se regulan y definen los siguientes puntos:

 - Balance de blancos

 - Histograma, exposición, rangos, claridad.

 - Enfoque

2229 Bocatoma Portillo
Revisión: 01 Página 12 de 25

INFORME LiDAR

**Ilustración 7. Imagen en formato nativo** **Ilustración 8. Resultado de revelado**

**Ilustración 9. Balance de brillos y contrastes** **Ilustración 10. Proceso de enfoque**

2229 Bocatoma Portillo
Revisión: 01 Página 13 de 25

INFORME LiDAR

**3.5.3** **ARCHIVO DE ORIENTACIÓN DE CADA FOTO**

Para dar inicio el proceso de ortorectificación es necesario obtener el archivo de
orientación externa llamado “ _eo_file_ ” el cual contiene los datos de la cámara utilizada, las
coordenadas de cada imagen y el tiempo en que fue tomada cada una de ellas. De esta forma
solo resta el modelo digital de superficie DSM para seguir con el proceso de imágenes.

A continuación mostramos una imagen referencial de parte del archivo de orientación
externa utilizado para la ortorectificación de las fotografías aéreas digitales

**Ilustración 11. EO-file**

2229 Bocatoma Portillo
Revisión: 01 Página 14 de 25

INFORME LiDAR

**3.5.4** **ORTORECTIFICACIÓN**

Esta etapa consiste en que mediante un modelo digital de superficie (DSM) se
ortorectifica (posiciona en una coordenada conocida) cada píxel de las fotos, quedando estas
referenciadas al sistema en el que el modelo de superficie este orientado.

**Ilustración 12. Ortofotografía**

2229 Bocatoma Portillo
Revisión: 01 Página 15 de 25

INFORME LiDAR

**3.5.5** **MOSAICO**

En este proceso todas las imágenes ortorectificadas se juntan y se fusionan en una sola
imagen. Para ello se procede a una serie de ajustes que permiten fusionar las fotos sin que se
noten los bordes de cada una, además de realizar un balance de colores, contraste y definir un
solo producto homogéneo y acorde a los colores reales de la zona de trabajo.

La imagen que sigue a continuación muestra la diferencia que existe en una serie de
ortofotos antes de armar el mosaico y el resultado final:

**Ilustración 13. Mosaico preliminar y mosaico final (balanceado)**

2229 Bocatoma Portillo
Revisión: 01 Página 16 de 25

INFORME LiDAR

**3.6** **PROCESO DE NUBE DE PUNTOS**

La segunda etapa en la que se divide el procesamiento de los datos es el trabajo que se
hace con la nube de puntos. En este punto, la nube de puntos se procesa tomando en cuenta la
proyección cartográfica con la que se trabajará. Se nivela cada línea de vuelo para que no
existan diferencias de altura entre una línea y otra y el resultado de la nube completa sea
homogéneo. Luego el trabajo se divide en dos rutas una para la obtención del Modelo Digital
de Terreno (DTM) y otra para la obtención del Modelo Digital de Superficie (DSM).

**Ilustración 14. Representación 3D de nube de puntos con atributos RGB**

2229 Bocatoma Portillo
Revisión: 01 Página 17 de 25

INFORME LiDAR

**3.7** **MODELO DIGITAL DE TERRENO (DTM)**

Este producto representa el modelamiento del terreno sin ningún tipo de elemento
estructural o de vegetación presente en el lugar. Permite generar las curvas de nivel y también
sirve para dar cota a cualquier elemento vectorial que se dibuje. Para lograr obtener este
producto a partir del DSM, se realiza un trabajo de filtrado automático y depurado manual
para asegurar que se elimine cualquier elemento que no sea terreno.

**3.8** **MODELO DIGITAL DE SUPERFICIE (DSM)**

Este producto tiene la propiedad de representar el terreno con todos los elementos
presentes en el área de interés, se usa específicamente para el proceso de ortorectificación
explicado anteriormente.

2229 Bocatoma Portillo
Revisión: 01 Página 18 de 25

INFORME LiDAR

**3.9** **CURVAS DE NIVEL Y PLANIMETRÍA**

Las curvas de nivel se obtienen mediante el DTM y representan la topografía de la
zona de interés. La planimetría es la foto-interpretación de los elementos observados en la
zona de interés, clasificando por capas según corresponda el tipo de elemento y otorgando
atributos de altura según las cotas definidas.

Como producto final obtendremos la cartografía, compuesta de la unión de las curvas
de nivel más la planimetría, incluyendo la ortofoto asociada. Este producto se subdivide en
láminas que permiten su estudio individual.

**Ilustración 17. Cartografía del área de estudio**

2229 Bocatoma Portillo
Revisión: 01 Página 19 de 25

INFORME LiDAR

**4.** **RED GEODÉSICA**

La Red Geodésica del estudio fue proporcionada por el cliente, esta red está compuesta
por 2 vértices, siendo el principal el denominado “EVELYN” el cual es la base para el apoyo
del vuelo Laser.

Según la información proporcionada por el cliente este vértice posee las siguientes
coordenadas:

**Ilustración 18. Imagen panorámica vértice EVELYN**

**Ilustración 19. Imagen de detalle vértice EVELYN**

2229 Bocatoma Portillo
Revisión: 01 Página 20 de 25

INFORME LiDAR

El apoyo del vuelo Laser se realizó directamente al vértice EVELYN, con instrumental
GPS de doble frecuencia, el cual estuvo colectando datos al unísono mientras se realizaba el
vuelo laser.

Por razones de seguridad (de respaldo de datos) se realizaron mediciones redundantes a
un vértice denominado “PR-1”, el cual también colectó datos mientras se realizaba el vuelo.

**Ilustración 20. Imagen panorámica vértice PR-1**

2229 Bocatoma Portillo
Revisión: 01 Página 21 de 25

INFORME LiDAR

**5.** **EQUIPAMIENTO EMPLEADO**

**4.1** **Trabajos de Terreno**

a) GPS bases utilizadas para la georreferenciación del vuelo:

 - Receptores GPS Trimble modelo 5700 de doble frecuencia (L1 y L2). Su precisión

nominal en método estático es de 5mm + 1 ppm.

 - Antenas Trimble Zephyr y Zephyr-Geodetic L1/L2.

b) Transporte Aéreo:

 - Avión monomotor turbo Cessna 206 habilitado con foso aerofotogramétrico en el

fuselaje y sistema eléctrico adaptado para los equipos de captura de datos.

c) Equipo de captura de datos:

 - Toposys Harrier 56/G4 integrado por los siguientes sistemas:

 - LiDAR Scanner Riegl LMS-Q560 de 240 kHz.

 - Cámara Rollei AIC P45 de 39 Mpx.

 - Sistema Inercial de alta precisión IMU LN200 tipo 410.

 - Colector de datos presurizado Riegl DR560.

 - 2 Notebook Core2Duo, utilizados para la verificación de captura de datos en tiempo real,

planificación, cálculo y revisión de coberturas.

**4.2** **Producción de Cartografía Láser**

 - Equipamiento para trabajos de gabinete:

 - Hardware de proceso:

 6 PC Core2Quad, 4 Gb. RAM, 1 Tb. HD

 4 PC Core2Duo, 4 Gb. RAM, 500 Gb. HD

 - Hardware de edición:

 - 12 PC Dual Core/ Celeron / 2 Gb RAM

 - PosPac (GPS-IMU) de Applanix: Resolución de trayectoria. Integración de GPS

diferencial con datos inerciales.

 - RiAnalize de Riegl: Decodificación y control de datos crudos LiDAR.

 - Capture One de Phase One: Revelado Digital de fotografías.

 - Toppit de Toposys: Postproceso de nubes de puntos, DSM/DTM y ortorectificación.

 - DTMaster de Inpho: Clasificación, edición y revisión de nubes de puntos y DTM.

 - Orthovista de Inpho: Generación de mosaicos de ortofotos.

 - Global Mapper: Control de Calidad.

2229 Bocatoma Portillo
Revisión: 01 Página 22 de 25

INFORME LiDAR

 - Tracker de Track’Air: Generación de planes de vuelo.

 - Autocad de Autodesk, versión 2011: edición cartográfica.

 - Módulo MapEditor, de Datem, utilizado en la plataforma Autocad para edición

cartográfica.

2229 Bocatoma Portillo
Revisión: 01 Página 23 de 25

INFORME LiDAR

**6.** **PRODUCTOS OBTENIDOS**

En base a los datos obtenidos y el proceso de ellos, se obtienen los productos
detallados a continuación:

**Área escala 1/500.**
**PROYECCIÓN: UTM**

1. **Tile Index (dwg):** Archivo en formato dwg que muestra la distribución y

nomenclatura de la subdivisión del área en tiles de 1.000 x 1.000 m.

2. **DTM (ASCII):** Modelo Digital de Terreno con tamaño de píxel de 0,25 m.

3. **Cartografía (dwg):** Láminas de curvas de nivel (cada 0.5 m.) en formato dwg. Incluye

la vectorización y quebradas 3D, la ortofoto asociada en formato ecw.

4. **Ortofotos (tif):** Ortofotos en formato geotiff, con tamaño de píxel 0,1 cm.

5. **Planimetría (dwg):** Modelo de planimetría completo en formato dwg.

6. **Informe (doc - pdf):** Documento el cual contiene las especificaciones técnicas del

procesamiento LiDAR.

2229 Bocatoma Portillo
Revisión: 01 Página 24 de 25

INFORME LiDAR

**Tabla 5. Control de cambios documento**

|Actividad|Responsable|Fecha|
|---|---|---|
|Generación informe<br> <br> <br> <br> <br> <br> <br>|Aerotop S.A.<br> <br> <br> <br> <br> <br> <br>|xx/xx/xxxx<br> <br> <br> <br> <br> <br> <br>|

2229 Bocatoma Portillo
Revisión: 01 Página 25 de 25

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Parámetros láser escala 1/500****

| Características de la foto | Col2 | Col3 |
| --- | --- | --- |
| Tamaño px:<br>Resolución:<br>Escala: 1/500 | 0,087<br>250<br>855 | m.<br>dpi<br> |

**Tabla 3.: Estación de apoyo 1****

| Estación PR-01 | Col2 |
| --- | --- |
| Este (m)<br>Norte (m)<br>Altura (m) | 343.069,422<br>6.153.082,415<br>778,062 |

**Tabla 5.: Control de cambios documento****

| Actividad | Responsable | Fecha |
| --- | --- | --- |
| Generación informe<br> <br> <br> <br> <br> <br> <br> | Aerotop S.A.<br> <br> <br> <br> <br> <br> <br> | xx/xx/xxxx<br> <br> <br> <br> <br> <br> <br> |
