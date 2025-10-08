---
title: Sin título
author: JPZH
date: D:20150313131754-03'00'
language: es
type: manual
pages: 37
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - PROYECTO DE INGENIERÍA SISTEMA DE TRATAMIENTO DE LODOS
-->

# PROYECTO DE INGENIERÍA SISTEMA DE TRATAMIENTO DE LODOS

## C anales & H ormazábal I ngenieros L tda .

### C & H I ngenieros

**INDICE DE CONTENIDOS**

1 INTRODUCCIÓN ........................................................................................................................ 1

2 ALCANCE Y OBJETIVOS ........................................................................................................... 3

2.1 Alcance ............................................................................................................................. 3

2.2 Objetivos ......................................................................................................................... 3

2.2.1 Objetivo General ......................................................................................................................................... 3

2.2.2 Objetivos Específicos ................................................................................................................................. 3

3 REQUERIMIENTOS NORMATIVOS DEL MANEJO LODOS ..................................................... 5

4 DESCRIPCIÓN GENERAL DE LA PLANTA DE TRATAMIENTO ............................................... 8

4.1 Ubicación Geográfica de la PTAS ......................................................................... 8

4.2 Caudales y Cargas Afluente al Sistema de Tratamiento ............................ 9

4.3 Componentes del Sistema .................................................................................... 12

5 CARACTERÍSTICAS ESPECÍFICAS LÍNEA DE TRATAMIENTO DE LODOS ......................... 17

5.1 Componentes de la Línea de Lodos.................................................................. 17

5.1.1 Purga de Lodos en Exceso (WAS) ...................................................................................................... 17

5.1.2 Deshidratado de Lodos ......................................................................................................................... 17

5.2 Transporte y Retiro de Lodos .............................................................................. 18

5.2.1 Carga de Lodos ........................................................................................................................................ 18

5.2.2 Transporte y Eliminación de Lodos ................................................................................................... 18

5.3 Características del Diseño de las Componentes Unitarias de la Línea

de Lodos ................................................................................................................................... 19

5.3.1 Producción de Lodos.............................................................................................................................. 19

### C & H I ngenieros

5.3.2 Balance de Masa ...................................................................................................................................... 20

5.3.3 Capacidad de las Componentes Unitarias del Sistema .............................................................. 21

6 CARACTERÍSTICAS DE LOS LODOS GENERADOS Y CLASIFICACIÓN SANITARIA .......... 25

6.1 Características y Cuantificación de los Lodos ............................................... 25

6.2 Clasificación Sanitaria .............................................................................................. 26

7 PROGRAMA DE CONTROL DE PARÁMETROS CRÍTICOS ................................................... 28

7.1 Metodología de Control Propuesta .................................................................. 28

7.2 Parámetros Críticos a Controlar .......................................................................... 29

8 PLAN DE CONTINGENCIAS .................................................................................................... 30

8.1 Procedimientos de Emergencias ........................................................................ 30

8.1.1 Cortes de Energía Eléctrica ................................................................................................................... 31

8.1.2 Desperfectos en los Componentes del Sistema ........................................................................... 32

8.1.3 Déficit en el Suministro de Insumos de Proceso .......................................................................... 32

8.1.4 Generación de Olores ............................................................................................................................ 33

ÍNDICE DE TABLAS

Tabla 1: Resumen Requisitos Normativos D.S. 4/09 .................................................. 7

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- _Rev A._ ### C & H I ngenieros -->

**Tabla 1: RESUMEN REQUISITOS NORMATIVOS D.S. 4/09****

| Col1 | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  | **CLASIFICACIÓN SANITARIA Y REQUISITOS** | **CLASIFICACIÓN SANITARIA Y REQUISITOS** |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | **TIP**<br> | **TIP**<br> | **O DE**<br> |  |  |  |  |  | ~~**LUGA**~~<br>~~**DISPOS**~~ | ~~**LUGA**~~<br>~~**DISPOS**~~ | ~~** DE**~~<br>~~**ICION**~~ |  |
|  |  | ~~**L**~~ | ~~**L**~~ | ~~**ODO**~~ |  |  |  |  |  | ~~**FIN**~~ | ~~**FIN**~~ | ~~**AL**~~ |  |
|  |  | ~~**L**~~ | ~~**L**~~ | ~~**ODO**~~ |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | ~~También se consideran estabilizados si cumplen lo siguiente:~~<br><br> |  |  |  |  |  |  |
|  | Estab | Estab | Estab | ilizados |  |  | ~~•~~<br>~~Reducción del contenido de sólidos volátiles~~<br><br> |  |  |  | •<br>M<br> | ono<br> |  |
|  | SV | SV | SV | < 38% |  |  | ~~•~~<br>~~Tasa máxima específica de oxígeno para lodos de~~<br>digestión aeróbica |  |  |  | ~~re~~ | ~~lleno~~ |  |
|  |  |  |  |  |  |  | •<br>Procesos aeróbicos con temperaturas mayores a 40°C |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | •<br>Adición de material alcalino |  |  |  |  |  |  |
|  |  |  |  |  |  |  | •<br>Reducción de humedad |  |  |  |  |  |  |
|  |  |  |  |  |  |  | •<br>Tiempo de residencia |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | Deben cumplir los siguientes requisitos: |  |  |  |  |  |  |
|  |  |  |  |  |  |  | •<br>Densidad de Coliformes Fecales < 1000 NPM/grST ó<br> |  |  |  |  |  |  |
|  |  |  |  |  |  |  | ~~Salmonella sp < 3 NPM/4 gr de ST~~<br><br> |  |  |  |  |  |  |
|  |  |  |  |  |  |  | ~~•~~<br>~~Ova Helmítica viable < 1 en 4 gr. de ST, demostrando el~~<br>cumplimiento por medio de las condiciones de | ~~•~~<br>~~M~~ | ~~•~~<br>~~M~~ | ~~•~~<br>~~M~~ | ~~•~~<br>~~M~~ | ~~ono~~ | ~~ono~~ |
|  |  |  |  |  |  |  | ~~•~~<br>~~Ova Helmítica viable < 1 en 4 gr. de ST, demostrando el~~<br>cumplimiento por medio de las condiciones de | ~~•~~<br>~~M~~ | ~~•~~<br>~~M~~ | ~~•~~<br>~~M~~ | ~~•~~<br>~~M~~ | ~~ono~~ | ~~ono~~ |
|  |  |  |  |  |  |  | operación de los siguientes procesos:<br><br> |  |  |  | re | lleno |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | ~~S~~ | ~~lase A~~<br>~~ < 38%~~ |  |  | ~~•~~<br>~~Compostaje~~<br>•<br>Secado Térmico |  |  |  | •<br>Re<br> | lleno<br> |  |
|  |  |  |  |  |  |  | •<br>Tratamiento con Calor<br>~~•~~<br> |  |  |  | ~~sa~~<br>~~•~~<br>~~S~~ | ~~itario~~<br>~~uelo~~ |  |
|  |  |  |  |  |  |  | ~~Digestión aeróbica termofílica~~<br>•<br>Irradiación con Haces de Electrones<br> |  |  |  |  |  |  |
|  |  |  |  |  |  |  | ~~•~~<br>~~Irradiación con Rayos Gamma~~<br>•<br>Pasteurización |  |  |  |  |  |  |
|  |  |  |  |  |  |  | •<br>Tratamiento Alcalino<br><br> |  |  |  |  |  |  |
|  |  |  |  |  |  |  | ~~•~~<br>~~Tratamientos térmicos~~ |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | ~~Demostrar el cumplimiento del requisito mediante la~~<br>aprobación de la Autoridad Sanitaria de las condiciones de |  |  |  |  |  |  |
|  |  |  |  |  |  |  | operación de uno de los procesos de higienización señalados<br>~~a continuación:~~ |  |  |  |  |  |  |
|  |  |  |  |  |  |  | operación de uno de los procesos de higienización señalados<br>~~a continuación:~~ |  |  |  |  |  |  |
|  |  | C<br> | C<br> | lase B<br> |  |  | ~~•~~<br>~~Digestión Aeróbica~~ |  |  |  | ~~•~~<br><br>~~r~~ | ~~ono~~<br>~~lleno~~ |  |
|  |  | ~~SV~~<br> | ~~SV~~<br> | ~~ < 38%~~<br>~~edia~~ |  |  | ~~•~~<br>~~Secado de Aire~~ |  |  |  | •<br>R | elleno |  |
|  |  | Ge | Ge | ompetrica |  |  | ~~•~~<br>~~Digestión Anaeróbica~~ |  |  |  | sa<br><br> | nitario<br> |  |
|  |  | C. F<br> | C. F<br> | ecales <<br>~~6~~ |  |  | ~~•~~<br>~~Compostaje~~ |  |  |  | ~~•~~<br> | ~~uelo~~ |  |
|  |  | ~~2 x~~<br> | ~~2 x~~<br> | ~~ x10/gr~~<br>~~e ST~~ |  |  | ~~•~~<br>~~Estabilización con Cal~~ |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |

<!-- Estadísticas: 40 filas, 14 columnas -->
<!-- Contexto posterior: -->
<!-- _Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 7_ _Rev A._ -->
<!-- FIN TABLA 1 -->


Tabla 2: Caudales proyectados ........................................................................................... 10

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- _Rev A._ ### C & H I ngenieros -->

**Tabla 2: CAUDALES PROYECTADOS****

| Col1 | CONDICION DE VERANO | Col3 | Col4 | CONDICION DE INVIERNO | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Año** | <br>Población<br>[hab]<br> | Caudal de Diseño | Caudal de Diseño | <br>Población<br>[hab]<br> | Caudal de Diseño | Caudal de Diseño |
| **Año** | <br>Población<br>[hab]<br> | Qmed<br>[L/s]<br> | Q máxh<br>[L/s]<br> | Q máxh<br>[L/s]<br> | Qmed<br>[L/s]<br> | Q máxh<br>[L/s]<br> |
| 2014<br>2015<br>2016<br>2017<br>2018<br>2019<br>2020<br>2021<br>2022<br>2023<br>2024<br>2025 | 7.189<br>7.374<br>7.559<br>7.750<br>7.857<br>7.930<br>7.967<br>8.004<br>8.041<br>8.078<br>8.116<br>8.154 | 9,0<br>9,2<br>9,4<br>9,6<br>9,6<br>9,5<br>9,4<br>9,3<br>9,2<br>9,1<br>9,0<br>8,9 | 28,0<br>28,4<br>28,9<br>29,3<br>29,3<br>29,2<br>28,8<br>28,4<br>28,1<br>27,7<br>27,4<br>27,0 | 2.054<br>2.107<br>2.160<br>2.214<br>2.245<br>2.266<br>2.276<br>2.287<br>2.297<br>2.308<br>2.319<br>2.330 | 2,1<br>2,2<br>2,2<br>2,2<br>2,2<br>2,2<br>2,2<br>2,2<br>2,1<br>2,1<br>2,1<br>2,1 | 5,7<br>5,8<br>5,9<br>5,9<br>6 <br>5,9<br>5,9<br>5,8<br>5,7<br>5,6<br>5,6<br>5,5 |

<!-- Estadísticas: 3 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Al mismo tiempo la carga orgánica (Demanda Bioquímica de Oxígeno, expresada como DBO 5 ) al año 2025, corresponde a 326 kg/d como promedio en período de verano y 103 -->
<!-- FIN TABLA 2 -->


Tabla 3: Concentraciones y cargas de DBO5 proyectados ..................................... 11

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- _Rev A._ ### C & H I ngenieros -->

**Tabla 3: CONCENTRACIONES Y CARGAS DE DBO5 PROYECTADOS****

| Col1 | CONDICION DE VERANO | Col3 | Col4 | CONDICION DE INVIERNO | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Año** | <br>Población<br>[hab]<br> | DBO5 | DBO5 |  | DBO5 | DBO5 |
| **Año** | <br>Población<br>[hab]<br> | [kg/d] | [mg/L] | Población<br>[hab]<br> | [kg/d] | [mg/L] |
| 2014<br>2015<br>2016<br>2017<br>2018<br>2019<br>2020<br>2021<br>2022<br>2023<br>2024<br>2025 | 7.189<br>7.374<br>7.559<br>7.750<br>7.857<br>7.930<br>7.967<br>8.004<br>8.041<br>8.078<br>8.116<br>8.154 | 288<br>295<br>302<br>310<br>314<br>317<br>319<br>320<br>322<br>323<br>325<br>326 | 368<br>370<br>373<br>375<br>379<br>384<br>391<br>397<br>404<br>411<br>418<br>425 | 2.054<br>2.107<br>2.160<br>2.214<br>2.245<br>2.266<br>2.276<br>2.287<br>2.297<br>2.308<br>2.319<br>2.330 | 82<br>84<br>86<br>89<br>90<br>91<br>91<br>91<br>92<br>92<br>93<br>93 | 449<br>452<br>456<br>459<br>464<br>471<br>479<br>487<br>495<br>503<br>512<br>520 |

<!-- Estadísticas: 3 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- **TABLA 4: CONCENTRACIONES Y CARGAS DE SÓLIDOS SUSPENDIDOS PROYECTADOS** |Col1|CONDICION DE VERANO|Col3|Col4|CONDICION DE INVIERNO|Col6|Col7| |---|---|---|---|---|---|---| -->
<!-- FIN TABLA 3 -->


Tabla 4: Concentraciones y cargas de sólidos suspendidos proyectados ....... 11

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---|---|---|---|---| |**Año**|<br>Población<br>[hab]<br>|DBO5|DBO5||DBO5|DBO5| |**Año**|<br>Población<br>[hab]<br>|[kg/d]|[mg/L]|Población<br>[hab]<br>|[kg/d]|[mg/L]| |2014<br>2015<br>2016<br>2017<br>2018<br>2019<br>2020<br>2021<br>2022<br>2023<br>2024<br>2025|7.189<br>7.374<br>7.559<br>7.750<br>7.857<br>7.930<br>7.967<br>8.004<br>8.041<br>8.078<br>8.116<br>8.154|288<br>295<br>302<br>310<br>314<br>317<br>319<br>320<br>322<br>323<br>325<br>326|368<br>370<br>373<br>375<br>379<br>384<br>391<br>397<br>404<br>411<br>418<br>425|2.054<br>2.107<br>2.160<br>2.214<br>2.245<br>2.266<br>2.276<br>2.287<br>2.297<br>2.308<br>2.319<br>2.330|82<br>84<br>86<br>89<br>90<br>91<br>91<br>91<br>92<br>92<br>93<br>93|449<br>452<br>456<br>459<br>464<br>471<br>479<br>487<br>495<br>503<br>512<br>520| -->

**Tabla 4: CONCENTRACIONES Y CARGAS DE SÓLIDOS SUSPENDIDOS PROYECTADOS****

| Col1 | CONDICION DE VERANO | Col3 | Col4 | CONDICION DE INVIERNO | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Año** | <br>Población<br>[hab]<br> | SST | SST | <br>Población<br>[hab]<br> | SST | SST |
| **Año** | <br>Población<br>[hab]<br> | [kg/d] | [mg/L] | [mg/L] | [kg/d] | [mg/L] |
| 2014<br>2015<br>2016<br>2017 | 7.189<br>7.374<br>7.559<br>7.750 | 230<br>236<br>242<br>248 | 294<br>296<br>298<br>300 | 2.054<br>2.107<br>2.160<br>2.214 | 66<br>67<br>69<br>71 | 359<br>362<br>365<br>367 |

<!-- Estadísticas: 3 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- _Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 11_ _Rev A._ -->
<!-- FIN TABLA 4 -->


Tabla 5: Características del sistema de descarte de Lodos ..................................... 17

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- El lodo activado de exceso se retira de cada componente unitaria de sedimentación por medio de una planta elevadora de lodos de exceso (WAS). -->

**Tabla 5: CARACTERÍSTICAS DEL SISTEMA DE DESCARTE DE LODOS****

| Parámetro | Unidad | Verano | Invierno |
| --- | --- | --- | --- |
| Caudal Medio<br>Caudal Semanal<br>Días de Purga de Lodos<br>Horas de Bombeo WAS | m3/d<br>m3/sem<br>días/sem<br>h <br>m3/h<br>L/s | 44,5<br>311,4<br>5,0<br>4,0<br>15,6<br>4,3 | 13,9<br>97<br>5,0<br>4,0<br>4,9<br>1,3 |

<!-- Estadísticas: 1 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **5.1.2** **D** **ESHIDRATADO DE** **L** **ODOS** La deshidratación de los lodos se efectúa en un sistema de deshidratado mecánico, -->
<!-- FIN TABLA 5 -->


### C & H I ngenieros

Tabla 6: Características de diseño y capacidad máxima del deshidratador .... 18

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- para esta unidad es de 5 días a la semana durante 4 horas al día. La Tabla 7 muestra los criterios de diseño de la unidad y la capacidad máxima de esta. -->

**Tabla 6: CARACTERÍSTICAS DE DISEÑO Y CAPACIDAD MÁXIMA DEL DESHIDRATADOR****

| Parámetro | Unidad | Verano | Invierno |
| --- | --- | --- | --- |
| Carga de Lodos a Deshidratador<br>Concentración de Ingreso<br>Caudal de Ingreso<br> <br>Carga de Sólidos Unitaria de Trabajo<br>Carga de Hidráulica Unitaria de Trabajo<br>Concentración a Alcanzar<br>Caudal de Salida<br> | kg/d<br>kg/m3<br>m3/d<br>kg/h<br>m3/h<br>kg/m3<br>m3/d | 167<br>30<br>5,6<br>42<br>1,4<br>180<br>0,93 | 36<br>30<br>1,2<br>9 <br>0,3<br>180<br>0,20 |

<!-- Estadísticas: 1 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **5.2** **T** **RANSPORTE Y** **R** **ETIRO DE** **L** **ODOS** **5.2.1** **C** **ARGA DE** **L** **ODOS** -->
<!-- FIN TABLA 6 -->


Tabla 7: Producción Medias Esperadas de lodos ........................................................ 20

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- _Rev A._ ### C & H I ngenieros -->

**Tabla 7: PRODUCCIÓN MEDIAS ESPERADAS DE LODOS****

| Año | Tasa de Producción de Lodos | Col3 | Producción Esperada de<br>Lodos | Col5 |
| --- | --- | --- | --- | --- |
| **Año** | **Verano**<br>**Kg/Kg DBO5**<br>**remov** | **Invierno**<br>**Kg/Kg DBO5**<br>**remov** | **Verano**<br>**Kg/día** | **Invierno**<br>**Kg/día** |
| 2014<br>2015<br>2016<br>2017<br>2018<br>2019<br>2020<br>2021<br>2022<br>2023<br>2024<br>2025 | 0,830<br>0,835<br>0,840<br>0,843<br>0,845<br>0,847<br>0,847<br>0,848<br>0,821<br>0,850<br>0,849<br>0,850 | 0,652<br>0,649<br>0,654<br>0,654<br>0,656<br>0,659<br>0,659<br>0,659<br>0,686<br>0,661<br>0,657<br>0,663 | 226<br>233<br>240<br>247<br>251<br>255<br>256<br>258<br>251<br>261<br>263<br>264 | 51<br>52<br>54<br>56<br>57<br>58<br>58<br>58<br>61<br>58<br>59<br>59 |

<!-- Estadísticas: 2 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **5.3.2** **B** **ALANCE DE** **M** **ASA** Considerando la carga de lodos de 264 kg/d (Verano) y 59 Kg/d (Invierno), y una frecuencia -->
<!-- FIN TABLA 7 -->


Tabla 8: Balance de masa de la línea de lodos para Verano 2025....................... 21

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- _Rev A._ ### C & H I ngenieros -->

**Tabla 8: BALANCE DE MASA DE LA LÍNEA DE LODOS PARA VERANO 2025****

| Parámetro | Unidad | WAS | Agua de<br>Retorno | Lodo<br>Deshidratado |
| --- | --- | --- | --- | --- |
| Carga Másica<br>Caudal<br>Concentración | kg/d<br>m3/d<br>kg/m3 | 82,9<br>10,4<br>8 | 0,8<br>10,0<br>0,08 | 82,1<br>0,4<br>200 |

<!-- Estadísticas: 1 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **5.3.3** **C** **APACIDAD DE LAS** **C** **OMPONENTES** **U** **NITARIAS DEL** **S** **ISTEMA** Uno de los aspectos de relevancia para asegurar que el sistema responde satisfactoriamente -->
<!-- FIN TABLA 8 -->


Tabla 9: Balance de masa de la línea de lodos para Invierno 2025 .................... 21

Tabla 10: Produccion de lodos coregida por tiempo de operación .................. 22

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- unidades de deshidratado operan 5 dias por semana, con una operación de 4 horas por día se tiene: -->

**Tabla 10: PRODUCCION DE LODOS CORREGIDA POR TIEMPO DE OPERACIÓN****

| Lodo | Col2 | Verano | Invierno |
| --- | --- | --- | --- |
| Diario Producido (b.s.) | k/d | 261,5 | 58,6 |
| Diario Deshidratado<br>(b.s.) | kg/d | 366,1 | 82,1 |
| Diario Deshidratado<br>(b.s.) | kg/h | 91,5 | 20,5 |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Para cumplir con los requerimientos de manejo de lodos, las capacidades definidas para las unidades de espesamiento y deshidratado son: -->
<!-- FIN TABLA 10 -->


Tabla 11: Características de los lodos generados desde el sistema ................... 25

<!-- INICIO TABLA 11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- posible indicar que las características de los lodos generados desde la planta de tratamiento, es la que a continuación se indica (Tabla 11). -->

**Tabla 11: CARACTERÍSTICAS DE LOS LODOS GENERADOS DESDE EL SISTEMA****

| Año | Población | Col3 | Carga de DBO5 | Col5 | Humedad |
| --- | --- | --- | --- | --- | --- |
| Año | Verano | Invierno | Verano | Invierno | Invierno |
| Año | hab | hab | kg DBO5/d | kg DBO5/d | % |
| 2014<br>2015<br>2016<br>2017<br>2018<br>2019<br>2020<br>2021<br>2022<br>2023<br>2024<br>2025 | 7.189<br>7.374<br>7.559<br>7.750<br>7.857<br>7.930<br>7.967<br>8.004<br>8.041<br>8.078<br>8.116<br>8.154 | 2.054<br>2.107<br>2.160<br>2.214<br>2.245<br>2.266<br>2.276<br>2.287<br>2.297<br>2.308<br>2.319<br>2.330 | 288<br>295<br>302<br>310<br>314<br>317<br>319<br>320<br>322<br>323<br>325<br>326 | 82<br>84<br>86<br>89<br>90<br>91<br>91<br>91<br>92<br>92<br>93<br>93 | 80<br>80<br>80<br>80<br>80<br>80<br>80<br>80<br>80<br>80<br>80<br>80 |

<!-- Estadísticas: 3 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- _Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 25_ _Rev A._ -->
<!-- FIN TABLA 11 -->


Tabla 12: Control de parámetros críticos ....................................................................... 29

<!-- INICIO TABLA 12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- (ver Tabla 10), los que corresponden a registros de operación a realizar in situ y resultados de parámetros medidos en laboratorio. -->

**Tabla 12: CONTROL DE PARÁMETROS CRÍTICOS****

| PARÁMETRO | UNIDAD | FRECUENCIA<br>DE MEDICIÓN<br>(N°/MES) | PUNTO DE MEDICIÓN |
| --- | --- | --- | --- |
| Concentración SSLM | kg/m3 | 1 | Reactor Biológico |
| **PURGA DE LODOS (WAS)** | **PURGA DE LODOS (WAS)** | **PURGA DE LODOS (WAS)** | **PURGA DE LODOS (WAS)** |
| Volumen Diario | m3 | 1 | Línea de WAS |
| Concentración | kg/m3 | 1 | Línea de WAS |
| **LODO DESHIDRATADO** | **LODO DESHIDRATADO** | **LODO DESHIDRATADO** | **LODO DESHIDRATADO** |
| Volumen Diario | m33 | 1 | Salida de Filtro de Bandas |
| Concentración | kg/m3 | 1 | Salida de Filtro de Bandas |

<!-- Estadísticas: 7 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- _Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 29_ _Rev A._ -->
<!-- FIN TABLA 12 -->


ÍNDICE DE FIGURAS

Figura 1: Ubicación de la Localidad de Iloca .................................................................. 8

Figura 2: Ubicación Proyectada de la Planta de Tratamiento .................................. 9

Figura 3: Esquema Tratamiento de aguas servidas y Lodos PTAS Iloca ........... 14

Figura 4: Lay Out general PTAS de Iloca ......................................................................... 16

### C & H I ngenieros

**1** **INTRODUCCIÓN**

En el marco del cumplimiento de lo establecido en el Decreto Supremo N° 4 “ **Reglamento**

**para el Manejo de Lodos Generados en Plantas de Tratamiento de Aguas Servidas** ” del

Ministerio Secretaría General de Gobierno, publicado en el diario oficial el 28 de Octubre de

2009, en adelante D.S. N° 4, se ha elaborado el presente Proyecto de Ingeniería del Sistema

de Tratamiento de Lodos generados en la Planta de Tratamiento de Aguas Servidas (PTAS)

de Iloca, VII Región.

Tal como se establece en el Reglamento, el presente proyecto da cuenta del

almacenamiento, tratamiento, transporte y disposición final de los lodos generados en el

recinto de la Planta de Tratamiento, indicando aquellos procesos efectuados en el interior

de las instalaciones y aquellos llevados a cabo fuera de él.

Conforme a lo anterior, el presente documento revisa los siguientes aspectos:

a) Descripción de los procesos en los que se generan lodos, cuantificación y

caracterización de los lodos generados y clasificación sanitaria de los lodos tratados.

b) Diseño de todas las unidades y equipamiento necesario para conducir, tratar y/o dar

disposición final a los lodos generados durante toda la vida útil prevista de la Planta

de Tratamiento.

c) Identificación y definición de un Programa de Control de Parámetros Críticos de la

Operación del Sistema de Manejo de Lodos.

d) Plan de Contingencia.

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 1_

_Rev A._

### C & H I ngenieros

La localidad de Iloca se encuentra ubicada en la costa de la VII. Conforme a los

antecedentes indicados por Nuevosur S.A., existe una fuerte estacionalidad lo que hace que

la población aumente en período estival, al menos 3,4 veces.

.La Planta corresponde a un tratamiento de lodos activados, de cultivo suspendido en

modalidad carga media y satisface los requerimientos de descarga para una población de

8.154 habitantes proyectados al período de previsión (2025), que considera un caudal de

tratamiento medio de verano de 8,9 l/s.

Cabe señalar que en términos de tratamiento de aguas, la Planta de Tratamiento de aguas

servidas cumple satisfactoriamente los requisitos establecidos en la normativa de emisión

chilena (Decreto Supremo N° 90), lo cual es fiscalizado por la Superintendencia de Servicios

Sanitarios.

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 2_

_Rev A._

### C & H I ngenieros

**2** **ALCANCE** **Y** **OBJETIVOS**

**2.1** **A** **LCANCE**

El alcance del presente documento considera abordar los aspectos exigidos en el D.S. N° 4

que en lo específico establece en el Artículo N°9 que “Toda Planta de Tratamiento de

aguas servidas deberá contar con un proyecto de ingeniería, que deberá ser aprobado por

la Autoridad Sanitaria”.

**2.2** **O** **BJETIVOS**

**2.2.1** **O** **BJETIVO** **G** **ENERAL**

El presente proyecto de ingeniería tiene por objetivo describir el proceso de generación de

lodos en la Planta de Tratamiento, señalando las componentes unitarias para su tratamiento

y disposición final, indicando el grado de estabilización alcanzado y su clasificación

sanitaria, los cuales darán cuenta del cumplimiento de las disposiciones establecidas en el

D.S. N° 4.

**2.2.2** **O** **BJETIVOS** **E** **SPECÍFICOS**

Los objetivos específicos del presente documento son:

 Realizar una descripción de los procesos de generación de lodos en la PTAS, a un

nivel tal que permita su clara comprensión.

 Dar a conocer la cuantificación y características de los lodos generados en la PTAS.

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 3_

_Rev A._

### C & H I ngenieros

 Determinar la clasificación sanitaria a alcanzar a partir del proceso de tratamiento de

los lodos, ya sea en el interior o exterior del recinto de la PTAS, o bien mediante una

combinación de ambos.

 Dar a conocer los principales criterios y parámetros de diseño de las unidades de

tratamiento de lodos en el recinto de la Planta de Tratamiento.

 Presentar el Programa de Control de Parámetros Críticos para la Operación del

Sistema de Manejo de Lodos.

 Presentar el Plan de Contingencia ante eventos que amenacen la continuidad del

tratamiento y que en consecuencia, hagan peligrar el manejo de lodos previsto.

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 4_

_Rev A._

### C & H I ngenieros

**3** **REQUERIMIENTOS** **NORMATIVOS** **DEL** **MANEJO** **LODOS**

Los lodos generados en la Planta de Tratamiento, deberán cumplir con los requisitos

establecidos en el D.S. N° 4 el que tiene por objetivo regular el manejo de lodos generados

en las instalaciones. Para dicho efecto, establece su clasificación sanitaria y las exigencias

mínimas para su manejo, además de las restricciones, requisitos y condiciones técnicas para

la aplicación de lodos en determinados suelos.

El Reglamento establece la clasificación sanitaria de los lodos, en base a parámetros que

determinan la reducción en la atracción de vectores sanitarios y la presencia de patógenos.

En este sentido, se establecen tres categorías:

 - **Lodos Clase A**, el que corresponde a un lodo sin restricciones para la aplicación al

suelo.

 - **Lodos Clase B**, el que corresponde a un lodo apto para aplicación al suelo, con

restricciones sanitarias de aplicación según tipo y localización de los suelos o

cultivos.

 - **Lodos Estabilizados** o con reducción del potencial de atracción de vectores

sanitarios, correspondientes a los que se les ha reducido los Sólidos Volátiles en un

38% como mínimo.

En base a la clasificación sanitaria anteriormente enunciada, el D.S. N° 4/09, indica las

posibilidades de disposición de los lodos, pudiendo ser en un relleno sanitario o en mono

relleno. Además establece la posibilidad de aplicación del lodo al suelo, para lo cual se fijan

procedimientos específicos y características químicas que deben cumplir antes de su

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 5_

_Rev A._

### C & H I ngenieros

aplicación. Un resumen de los requisitos normativos se presenta en la Tabla 1. Además el

reglamento establece procedimientos de medición, control y fiscalización.

**Finalmente, la interpretación realizada del DS 4/09 permite trasladar lodo No**

**estabilizado, hasta un lugar para proceder a su estabilización, previa disposición en**

**monorrelleno.**

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 6_

_Rev A._

### C & H I ngenieros

**TABLA 1: RESUMEN REQUISITOS NORMATIVOS D.S. 4/09**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||**CLASIFICACIÓN SANITARIA Y REQUISITOS**|**CLASIFICACIÓN SANITARIA Y REQUISITOS**||||||
|||||||||||||||
|||||||||||||||
|||**TIP**<br>|**TIP**<br>|**O DE**<br>||||||~~**LUGA**~~<br>~~**DISPOS**~~|~~**LUGA**~~<br>~~**DISPOS**~~|~~** DE**~~<br>~~**ICION**~~||
|||~~**L**~~|~~**L**~~|~~**ODO**~~||||||~~**FIN**~~|~~**FIN**~~|~~**AL**~~||
|||~~**L**~~|~~**L**~~|~~**ODO**~~||||||||||
||||||||~~También se consideran estabilizados si cumplen lo siguiente:~~<br><br>|||||||
||Estab|Estab|Estab|ilizados|||~~•~~<br>~~Reducción del contenido de sólidos volátiles~~<br><br>||||•<br>M<br>|ono<br>||
||SV|SV|SV|< 38%|||~~•~~<br>~~Tasa máxima específica de oxígeno para lodos de~~<br>digestión aeróbica||||~~re~~|~~lleno~~||
||||||||•<br>Procesos aeróbicos con temperaturas mayores a 40°C|||||||
|||||||||||||||
||||||||•<br>Adición de material alcalino|||||||
||||||||•<br>Reducción de humedad|||||||
||||||||•<br>Tiempo de residencia|||||||
|||||||||||||||
||||||||Deben cumplir los siguientes requisitos:|||||||
||||||||•<br>Densidad de Coliformes Fecales < 1000 NPM/grST ó<br>|||||||
||||||||~~Salmonella sp < 3 NPM/4 gr de ST~~<br><br>|||||||
||||||||~~•~~<br>~~Ova Helmítica viable < 1 en 4 gr. de ST, demostrando el~~<br>cumplimiento por medio de las condiciones de|~~•~~<br>~~M~~|~~•~~<br>~~M~~|~~•~~<br>~~M~~|~~•~~<br>~~M~~|~~ono~~|~~ono~~|
||||||||~~•~~<br>~~Ova Helmítica viable < 1 en 4 gr. de ST, demostrando el~~<br>cumplimiento por medio de las condiciones de|~~•~~<br>~~M~~|~~•~~<br>~~M~~|~~•~~<br>~~M~~|~~•~~<br>~~M~~|~~ono~~|~~ono~~|
||||||||operación de los siguientes procesos:<br><br>||||re|lleno||
|||||||||||||||
||||~~S~~|~~lase A~~<br>~~ < 38%~~|||~~•~~<br>~~Compostaje~~<br>•<br>Secado Térmico||||•<br>Re<br>|lleno<br>||
||||||||•<br>Tratamiento con Calor<br>~~•~~<br>||||~~sa~~<br>~~•~~<br>~~S~~|~~itario~~<br>~~uelo~~||
||||||||~~Digestión aeróbica termofílica~~<br>•<br>Irradiación con Haces de Electrones<br>|||||||
||||||||~~•~~<br>~~Irradiación con Rayos Gamma~~<br>•<br>Pasteurización|||||||
||||||||•<br>Tratamiento Alcalino<br><br>|||||||
||||||||~~•~~<br>~~Tratamientos térmicos~~|||||||
|||||||||||||||
|||||||||||||||
||||||||~~Demostrar el cumplimiento del requisito mediante la~~<br>aprobación de la Autoridad Sanitaria de las condiciones de|||||||
||||||||operación de uno de los procesos de higienización señalados<br>~~a continuación:~~|||||||
||||||||operación de uno de los procesos de higienización señalados<br>~~a continuación:~~|||||||
|||C<br>|C<br>|lase B<br>|||~~•~~<br>~~Digestión Aeróbica~~||||~~•~~<br><br>~~r~~|~~ono~~<br>~~lleno~~||
|||~~SV~~<br>|~~SV~~<br>|~~ < 38%~~<br>~~edia~~|||~~•~~<br>~~Secado de Aire~~||||•<br>R|elleno||
|||Ge|Ge|ompetrica|||~~•~~<br>~~Digestión Anaeróbica~~||||sa<br><br>|nitario<br>||
|||C. F<br>|C. F<br>|ecales <<br>~~6~~|||~~•~~<br>~~Compostaje~~||||~~•~~<br>|~~uelo~~||
|||~~2 x~~<br>|~~2 x~~<br>|~~ x10/gr~~<br>~~e ST~~|||~~•~~<br>~~Estabilización con Cal~~|||||||
|||||||||||||||
|||||||||||||||

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 7_

_Rev A._

### C & H I ngenieros

**4** **DESCRIPCIÓN** **GENERAL** **DE** **LA** **PLANTA** **DE** **TRATAMIENTO**

**4.1** **U** **BICACIÓN** **G** **EOGRÁFICA DE LA** **PTAS**

La localidad de Iloca, se ubica en la VII Región del Maule, provincia de Curicó, comuna de

Licanten y limita hacia el norte con la Región del Libertador Bernardo O’Higgins, VI

Región, por medio del estero Chimbarongo. Hacia el este con la comuna de Romeral y su

pre cordillera. Hacia el oeste con la comuna de Chepica, Rauco y Curicó, tras el río Iloca.

La ciudad de Iloca, capital de la comuna del mismo nombre, se encuentra ubicada a 312 km.

al sur de Santiago y a 120 km. al oeste de Curicó. La principal vía de acceso a la localidad de

Iloca es a través de la ruta J-60 que la comunica Iloca y Curicó. A continuación en la Figura

1, se muestra el emplazamiento de la PTAS.

**FIGURA 1: UBICACIÓN DE LA LOCALIDAD DE ILOCA**

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 8_

_Rev A._

### C & H I ngenieros

**FIGURA 2: UBICACIÓN PROYECTADA DE LA PLANTA DE TRATAMIENTO**

**4.2** **C** **AUDALES Y** **C** **ARGAS** **A** **FLUENTE AL** **S** **ISTEMA DE** **T** **RATAMIENTO**

Por las características de la localidad, esta sufre de una gran variación estacional por lo que

para el diseño se considera la condición más exigente y que corresponde a la condición de

verano la que contempla para el final del período de previsión una población de 8.154

habitantes tal como se aprecia en la Tabla 2.

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 9_

_Rev A._

### C & H I ngenieros

**TABLA 2: CAUDALES PROYECTADOS**

|Col1|CONDICION DE VERANO|Col3|Col4|CONDICION DE INVIERNO|Col6|Col7|
|---|---|---|---|---|---|---|
|**Año**|<br>Población<br>[hab]<br>|Caudal de Diseño|Caudal de Diseño|<br>Población<br>[hab]<br>|Caudal de Diseño|Caudal de Diseño|
|**Año**|<br>Población<br>[hab]<br>|Qmed<br>[L/s]<br>|Q máxh<br>[L/s]<br>|Q máxh<br>[L/s]<br>|Qmed<br>[L/s]<br>|Q máxh<br>[L/s]<br>|
|2014<br>2015<br>2016<br>2017<br>2018<br>2019<br>2020<br>2021<br>2022<br>2023<br>2024<br>2025|7.189<br>7.374<br>7.559<br>7.750<br>7.857<br>7.930<br>7.967<br>8.004<br>8.041<br>8.078<br>8.116<br>8.154|9,0<br>9,2<br>9,4<br>9,6<br>9,6<br>9,5<br>9,4<br>9,3<br>9,2<br>9,1<br>9,0<br>8,9|28,0<br>28,4<br>28,9<br>29,3<br>29,3<br>29,2<br>28,8<br>28,4<br>28,1<br>27,7<br>27,4<br>27,0|2.054<br>2.107<br>2.160<br>2.214<br>2.245<br>2.266<br>2.276<br>2.287<br>2.297<br>2.308<br>2.319<br>2.330|2,1<br>2,2<br>2,2<br>2,2<br>2,2<br>2,2<br>2,2<br>2,2<br>2,1<br>2,1<br>2,1<br>2,1|5,7<br>5,8<br>5,9<br>5,9<br>6 <br>5,9<br>5,9<br>5,8<br>5,7<br>5,6<br>5,6<br>5,5|

Al mismo tiempo la carga orgánica (Demanda Bioquímica de Oxígeno, expresada como

DBO 5 ) al año 2025, corresponde a 326 kg/d como promedio en período de verano y 103

kg/d en periodo de invierno. En relación a la carga de sólidos suspendidos totales al

horizonte de previsión (condición media) corresponde a 269 kg/día en período de verano y

78 kg/d en periodo de invierno, tal como se aprecia en las Tablas 3 y 4.

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 10_

_Rev A._

### C & H I ngenieros

**TABLA 3: CONCENTRACIONES Y CARGAS DE DBO5 PROYECTADOS**

|Col1|CONDICION DE VERANO|Col3|Col4|CONDICION DE INVIERNO|Col6|Col7|
|---|---|---|---|---|---|---|
|**Año**|<br>Población<br>[hab]<br>|DBO5|DBO5||DBO5|DBO5|
|**Año**|<br>Población<br>[hab]<br>|[kg/d]|[mg/L]|Población<br>[hab]<br>|[kg/d]|[mg/L]|
|2014<br>2015<br>2016<br>2017<br>2018<br>2019<br>2020<br>2021<br>2022<br>2023<br>2024<br>2025|7.189<br>7.374<br>7.559<br>7.750<br>7.857<br>7.930<br>7.967<br>8.004<br>8.041<br>8.078<br>8.116<br>8.154|288<br>295<br>302<br>310<br>314<br>317<br>319<br>320<br>322<br>323<br>325<br>326|368<br>370<br>373<br>375<br>379<br>384<br>391<br>397<br>404<br>411<br>418<br>425|2.054<br>2.107<br>2.160<br>2.214<br>2.245<br>2.266<br>2.276<br>2.287<br>2.297<br>2.308<br>2.319<br>2.330|82<br>84<br>86<br>89<br>90<br>91<br>91<br>91<br>92<br>92<br>93<br>93|449<br>452<br>456<br>459<br>464<br>471<br>479<br>487<br>495<br>503<br>512<br>520|

**TABLA 4: CONCENTRACIONES Y CARGAS DE SÓLIDOS SUSPENDIDOS PROYECTADOS**

|Col1|CONDICION DE VERANO|Col3|Col4|CONDICION DE INVIERNO|Col6|Col7|
|---|---|---|---|---|---|---|
|**Año**|<br>Población<br>[hab]<br>|SST|SST|<br>Población<br>[hab]<br>|SST|SST|
|**Año**|<br>Población<br>[hab]<br>|[kg/d]|[mg/L]|[mg/L]|[kg/d]|[mg/L]|
|2014<br>2015<br>2016<br>2017|7.189<br>7.374<br>7.559<br>7.750|230<br>236<br>242<br>248|294<br>296<br>298<br>300|2.054<br>2.107<br>2.160<br>2.214|66<br>67<br>69<br>71|359<br>362<br>365<br>367|

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 11_

_Rev A._

### C & H I ngenieros

|Col1|CONDICION DE VERANO|Col3|Col4|CONDICION DE INVIERNO|Col6|Col7|
|---|---|---|---|---|---|---|
|**Año**|<br>Población<br>[hab]<br>|SST|SST|<br>Población<br>[hab]<br>|SST|SST|
|**Año**|<br>Población<br>[hab]<br>|[kg/d]|[mg/L]|[mg/L]|[kg/d]|[mg/L]|
|2018<br>2019<br>2020<br>2021<br>2022<br>2023<br>2024<br>2025|7.857<br>7.930<br>7.967<br>8.004<br>8.041<br>8.078<br>8.116<br>8.154|251<br>254<br>255<br>256<br>257<br>259<br>260<br>261|303<br>308<br>313<br>318<br>323<br>329<br>334<br>340|2.245<br>2.266<br>2.276<br>2.287<br>2.297<br>2.308<br>2.319<br>2.330|72<br>73<br>73<br>73<br>74<br>74<br>74<br>75|371<br>377<br>383<br>389<br>396<br>403<br>409<br>416|

**4.3** **C** **OMPONENTES DEL** **S** **ISTEMA**

La PTAS de Iloca, consiste en un proceso de tratamiento biológico aerobio de lodos

activados, el cual debido a la condición de estacional, deberá operar bajo la modalidad

media carga (SRT 9,2 d) en verano y en la modalidad de aireación extendida (SRT 41,1 d) en

invierno, ambos en mezcla completa y flujo continuo, con desinfección final del efluente

con gas cloro. La línea de lodos considera el circuito de recirculación y deshidratado

mecánico de los lodos a través de filtro banda.

El tratamiento preliminar, consistente en desbaste fino que permita retener partículas

menores a 10 mm, desarenado y desengrasado, que se efectúa en una planta del tipo

compacto que incluye reja fina rotatoria, y desarenador/desgrasador aireado de flujo

horizontal/helicoidal.

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 12_

_Rev A._

### C & H I ngenieros

El tratamiento biológico se lleva a cabo en un estanque de hormigón compuesto por un

selector de cabecera, una zona de aireación y una zona final de desgasificación, lo cual

considera un volumen total de 832 m [3] .

Las aguas tratadas biológicamente son derivadas a la unidad de sedimentación secundaria,

consistente en un estanque de hormigón, de sección circular de 12 m. de diámetro. Desde

el estanque de sedimentación se generan dos corrientes de flujo: el agua clarificada y los

lodos sedimentados. El agua clarificada, con bajos niveles de DBO5 y SST, es derivada a la

cámara de contacto para su desinfección final. El lodo sedimentado es extraído desde el

fondo del sedimentador y enviado a la planta elevadora de recirculación (RAS) y descarte de

lodos (WAS). Desde este sistema, compuesto por tres bombas centrífugas (dos en

operación y una de reserva) nace una impulsión de los lodos de recirculación y el descarte

de lodos está compuesto por un sistema de dos bombas centrifugas operando en la

modalidad 1+1, la cual alimenta al sistema de deshidratado de lodos.

La desinfección final del efluente tratado se realiza con gas cloro para su posterior descarga

al estero Iloca.

Los lodos sedimentados son deshidratados en forma mecánica mediante un sistema

compuesto por espesador y filtro de bandas. Las aguas de drenaje de las unidades de

espesamiento y deshidratado mecánico son conducidas a la cabecera de la planta. Estas

aguas constituyen la línea de aguas de retorno del sistema de tratamiento.

La Figura 3, muestra las componentes del sistema de tratamiento y destaca en él, aquellas

unidades correspondientes a la línea de lodos.

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 13_

_Rev A._

### C & H I ngenieros

**FIGURA 3: ESQUEMA TRATAMIENTO DE AGUAS SERVIDAS Y LODOS PTAS ILOCA**

Conforme a lo anterior se mencionan a continuación los elementos que componen la línea

de agua y lodos de la Planta de Tratamiento.

**Línea de Agua**

La línea de agua incluye las siguientes unidades:

 - Planta Elevadora de Cabecera

 Tratamiento Preliminar: que incluye medidor de caudal, rejas finas mecanizadas y

desarenador/desgrasador

 Tratamiento Secundario: reactor biológico compuesto por selector de cabecera,

zona aireada y cámara de desagasificadora, y los sedimentadores secundarios.

 - Planta elevadora de recirculación de lodos (RAS).

 Desinfección (cámara de contacto y desinfección con cloro gas).

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 14_

_Rev A._

### C & H I ngenieros

**Línea de Lodos**

La línea de lodos cuenta con las siguientes componentes unitarias:

 Planta elevadora de purga de lodos en exceso (WAS)

 Deshidratado mecánico de lodos (espesador y filtro de bandas).

En el siguiente capítulo se explica en detalle los elementos específicos de la línea de lodos,

señalando los parámetros de diseño de procesos, características de los equipos,

capacidades de tratamiento, entre otros aspectos.

A continuación se presenta, en la Figura 4, un Lay Out general de las instalaciones, que

muestra el emplazamiento de las unidades correspondientes de la línea de aguas y línea de

lodos.

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 15_

_Rev A._

### C & H I ngenieros

**FIGURA 4: LAY OUT GENERAL PTAS DE ILOCA**

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 16_

### C & H I ngenieros

**5** **CARACTERÍSTICAS** **ESPECÍFICAS** **LÍNEA** **DE** **TRATAMIENTO** **DE**

**LODOS**

Se realiza a continuación una descripción de los procesos de tratamiento de lodos

efectuados en la PTAS de Iloca.

**5.1** **C** **OMPONENTES DE LA** **L** **ÍNEA DE** **L** **ODOS**

**5.1.1** **P** **URGA DE** **L** **ODOS EN** **E** **XCESO** **(WAS)**

El lodo activado de exceso se retira de cada componente unitaria de sedimentación por

medio de una planta elevadora de lodos de exceso (WAS).

**TABLA 5: CARACTERÍSTICAS DEL SISTEMA DE DESCARTE DE LODOS**

|Parámetro|Unidad|Verano|Invierno|
|---|---|---|---|
|Caudal Medio<br>Caudal Semanal<br>Días de Purga de Lodos<br>Horas de Bombeo WAS|m3/d<br>m3/sem<br>días/sem<br>h <br>m3/h<br>L/s|44,5<br>311,4<br>5,0<br>4,0<br>15,6<br>4,3|13,9<br>97<br>5,0<br>4,0<br>4,9<br>1,3|

**5.1.2** **D** **ESHIDRATADO DE** **L** **ODOS**

La deshidratación de los lodos se efectúa en un sistema de deshidratado mecánico,

compuesto por espesador y filtro de bandas), que incluye un estanque de floculación para

el acondicionamiento químico previo del lodo con polímero. La capacidad de esta unidad

corresponde a 150 kg/h/m, con un ancho de banda de 0,50 metros. La humedad del lodo

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 17_

### C & H I ngenieros

obtenido luego de este proceso es de aproximadamente un 80 %. El período de operación

para esta unidad es de 5 días a la semana durante 4 horas al día.

La Tabla 7 muestra los criterios de diseño de la unidad y la capacidad máxima de esta.

**TABLA 6: CARACTERÍSTICAS DE DISEÑO Y CAPACIDAD MÁXIMA DEL DESHIDRATADOR**

|Parámetro|Unidad|Verano|Invierno|
|---|---|---|---|
|Carga de Lodos a Deshidratador<br>Concentración de Ingreso<br>Caudal de Ingreso<br> <br>Carga de Sólidos Unitaria de Trabajo<br>Carga de Hidráulica Unitaria de Trabajo<br>Concentración a Alcanzar<br>Caudal de Salida<br>|kg/d<br>kg/m3<br>m3/d<br>kg/h<br>m3/h<br>kg/m3<br>m3/d|167<br>30<br>5,6<br>42<br>1,4<br>180<br>0,93|36<br>30<br>1,2<br>9 <br>0,3<br>180<br>0,20|

**5.2** **T** **RANSPORTE Y** **R** **ETIRO DE** **L** **ODOS**

**5.2.1** **C** **ARGA DE** **L** **ODOS**

El carguío de los lodos se puede realizar directamente desde el filtro de bandas al

contenedor o desde la cancha de secado a camiones de la empresa transportista.

Al momento de retirar el contenedor, la empresa transportista dispone en el recinto de un

nuevo contenedor vacío para repetir la operación.

**5.2.2** **T** **RANSPORTE Y** **E** **LIMINACIÓN DE** **L** **ODOS**

El transporte de los lodos será efectuado hacia un sitio de disposición debidamente

autorizado por la autoridad competente en el cual se deberá estabilizar, previo a disponer

en su sistema.

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 18_

_Rev A._

### C & H I ngenieros

**5.3** **C** **ARACTERÍSTICAS DEL** **D** **ISEÑO DE LAS** **C** **OMPONENTES** **U** **NITARIAS DE LA** **L** **ÍNEA DE**

**L** **ODOS**

La PTAS de Iloca, dispone de todas las unidades de proceso necesarias para el tratamiento

de los lodos generados en el tratamiento secundario. En el presente punto se describe la

producción de lodos proyectada al horizonte de previsión y cómo el sistema de tratamiento

responde a dicha condición.

**5.3.1** **P** **RODUCCIÓN DE** **L** **ODOS**

La producción de lodos generada desde el tratamiento secundario, puede ser determinada

a partir de la siguiente ecuación

P L = P x - DBO rem **Ecuación N° 1**

Dónde:

P L : Producción de lodos total del sistema, [kg/d]

P x : Producción de lodos unitaria por DBO 5 removida del afluente, (kg SST/kg DBO rem )

DBO rem : Carga de DBO removida en el sistema, [kg/d]

Para este caso

En función a la marcada estacionalidad que presenta el sistema de tratamiento, se tendrá

que las producciones de lodo presenten variaciones que se indican a continuación

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 19_

_Rev A._

### C & H I ngenieros

**TABLA 7: PRODUCCIÓN MEDIAS ESPERADAS DE LODOS**

|Año|Tasa de Producción de Lodos|Col3|Producción Esperada de<br>Lodos|Col5|
|---|---|---|---|---|
|**Año**|**Verano**<br>**Kg/Kg DBO5**<br>**remov**|**Invierno**<br>**Kg/Kg DBO5**<br>**remov**|**Verano**<br>**Kg/día**|**Invierno**<br>**Kg/día**|
|2014<br>2015<br>2016<br>2017<br>2018<br>2019<br>2020<br>2021<br>2022<br>2023<br>2024<br>2025|0,830<br>0,835<br>0,840<br>0,843<br>0,845<br>0,847<br>0,847<br>0,848<br>0,821<br>0,850<br>0,849<br>0,850|0,652<br>0,649<br>0,654<br>0,654<br>0,656<br>0,659<br>0,659<br>0,659<br>0,686<br>0,661<br>0,657<br>0,663|226<br>233<br>240<br>247<br>251<br>255<br>256<br>258<br>251<br>261<br>263<br>264|51<br>52<br>54<br>56<br>57<br>58<br>58<br>58<br>61<br>58<br>59<br>59|

**5.3.2** **B** **ALANCE DE** **M** **ASA**

Considerando la carga de lodos de 264 kg/d (Verano) y 59 Kg/d (Invierno), y una frecuencia

de operación de 5 d/sem por 4 hr/d, se presenta a continuación, en la Tabla 8 y 9, el

balance de masa proyectado para la línea de lodos de la PTAS de Iloca, corregido por

tiempo de operación, tomando en consideración las cargas en la condición media al final

del periodo de previsión.

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 20_

_Rev A._

### C & H I ngenieros

**TABLA 8: BALANCE DE MASA DE LA LÍNEA DE LODOS PARA VERANO 2025**

|Parámetro|Unidad|WAS|Agua de<br>Retorno|Lodo<br>Deshidratado|
|---|---|---|---|---|
|Carga Másica<br>Caudal<br>Concentración|kg/d<br>m3/d<br>kg/m3|369,8<br>46,2<br>8|3,7<br>44,4<br>0,08|366,1<br>1,8<br>200|

**TABLA 9: BALANCE DE MASA DE LA LÍNEA DE LODOS PARA INVIERNO 2025**

|Parámetro|Unidad|WAS|Agua de<br>Retorno|Lodo<br>Deshidratado|
|---|---|---|---|---|
|Carga Másica<br>Caudal<br>Concentración|kg/d<br>m3/d<br>kg/m3|82,9<br>10,4<br>8|0,8<br>10,0<br>0,08|82,1<br>0,4<br>200|

**5.3.3** **C** **APACIDAD DE LAS** **C** **OMPONENTES** **U** **NITARIAS DEL** **S** **ISTEMA**

Uno de los aspectos de relevancia para asegurar que el sistema responde satisfactoriamente

al tratamiento de los lodos, corresponde a la capacidad que poseen las principales

componentes unitarias en términos de recepción de carga de lodos, la que se evalúa al final

del período de previsión de la planta de tratamiento, el que en este caso, corresponde al

año 2025.

La producción de lodos para la condición de verano se ha estimado en 264 kg/d al año

2025, mientras que aquella generada en período de invierno es de 59 kg/d al horizonte de

previsión (2025)

Para la determinación de la capacidad máxima del espesador y filtro bandas, se

consideraron las tasas ya definidas en las Tablas 7, y tomando en consideración que las

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 21_

_Rev A._

### C & H I ngenieros

unidades de deshidratado operan 5 dias por semana, con una operación de 4 horas por día

se tiene:

**TABLA 10: PRODUCCION DE LODOS CORREGIDA POR TIEMPO DE OPERACIÓN**

Tiempo de Operación

4 h/d

5 d/sem

|Lodo|Col2|Verano|Invierno|
|---|---|---|---|
|Diario Producido (b.s.)|k/d|261,5|58,6|
|Diario Deshidratado<br>(b.s.)|kg/d|366,1|82,1|
|Diario Deshidratado<br>(b.s.)|kg/h|91,5|20,5|

Para cumplir con los requerimientos de manejo de lodos, las capacidades definidas para las

unidades de espesamiento y deshidratado son:

**Espesador de Lodos**

Tipo : Espesador de lodos biológicos

audal de entrada : 15.6 m [3] /h

Carga de Entrada : 104 kg/h

Concentración entrada : 6.7 kg/m [3]

Agua lavado bandas : 0.5 m [3] /h (40 lt/min por 12 min/h)

Material Armazón : Acero Inox AISI 304

Material Banda : Banda filtrante Poliéster

Grupo de lavado banda e

inyectores

: auto limpiantes Acero inox AISI 304

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 22_

_Rev A._

### C & H I ngenieros

**Filtro Banda**

El filtro banda debe ser compatible con el espesador en términos de caudal y concentración

lograda en la unidad. Considerando que el espesador provea una concentración de lodos

de 30 kg/m3, se tiene el siguiente caudal de ingreso al deshidratador.

Tipo : Filtro banda para deshidratación de lodos

Carga de Entrada : 104 kg/h

Ancho de Banda : Ancho banda 800 mm

Superficie de escurrimiento

efectiva

Superficie de baja presión

efectiva

Superficie de alta presión

efectiva

: 1.5 m2

: 1.6 m2

: 1.6 m2

Velocidad bandas : 1.5 - 8 m/min.

Motorización bandas : Menor a 0.75 kW

Agua de lavado bandas : 5 m3/h (7 - 8 bar)

Requisito de calidad para el

agua de lavado

: Max 0.01% DS por Ø max 200 μ

Peso vacío : (~) 1700 Kg

Armazón : Armazón Acero Galvanizado en Caliente

Material Bandas : Bandas filtrantes Poliéster

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 23_

_Rev A._

### C & H I ngenieros

A partir de lo expresado en las características, es posible indicar que las componentes

principales, responden satisfactoriamente a la producción de lodos proyectada al año 2025,

correspondiente al horizonte de previsión de la PTAS. Vale la pena destacar, que el sistema

de tratamiento de lodos no opera todos los días, por lo tanto, la capacidad utilizada podría

ser mayor a la señalada.

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 24_

_Rev A._

### C & H I ngenieros

**6** **CARACTERÍSTICAS** **DE** **LOS** **LODOS** **GENERADOS** **Y** **CLASIFICACIÓN**

**SANITARIA**

**6.1** **C** **ARACTERÍSTICAS Y** **C** **UANTIFICACIÓN DE LOS** **L** **ODOS**

A partir de la infraestructura para el tratamiento de lodos descrita en el punto anterior, es

posible indicar que las características de los lodos generados desde la planta de

tratamiento, es la que a continuación se indica (Tabla 11).

**TABLA 11: CARACTERÍSTICAS DE LOS LODOS GENERADOS DESDE EL SISTEMA**

|Año|Población|Col3|Carga de DBO5|Col5|Humedad|
|---|---|---|---|---|---|
|Año|Verano|Invierno|Verano|Invierno|Invierno|
|Año|hab|hab|kg DBO5/d|kg DBO5/d|%|
|2014<br>2015<br>2016<br>2017<br>2018<br>2019<br>2020<br>2021<br>2022<br>2023<br>2024<br>2025|7.189<br>7.374<br>7.559<br>7.750<br>7.857<br>7.930<br>7.967<br>8.004<br>8.041<br>8.078<br>8.116<br>8.154|2.054<br>2.107<br>2.160<br>2.214<br>2.245<br>2.266<br>2.276<br>2.287<br>2.297<br>2.308<br>2.319<br>2.330|288<br>295<br>302<br>310<br>314<br>317<br>319<br>320<br>322<br>323<br>325<br>326|82<br>84<br>86<br>89<br>90<br>91<br>91<br>91<br>92<br>92<br>93<br>93|80<br>80<br>80<br>80<br>80<br>80<br>80<br>80<br>80<br>80<br>80<br>80|

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 25_

_Rev A._

### C & H I ngenieros

**6.2** **C** **LASIFICACIÓN** **S** **ANITARIA**

Tal como se señaló en el capítulo 3 del presente documento, los lodos generados desde la

Planta de Tratamiento, deberán cumplir con los requisitos establecidos en el D.S. N° 4/09 el

que tiene por objetivo regular el manejo de lodos generados en dichas instalaciones. Para

dicho efecto, establece su clasificación sanitaria y las exigencias mínimas para su manejo,

además de las restricciones, requisitos y condiciones técnicas para la aplicación de lodos en

determinados suelos.

En el Título II del reglamento “De la Clasificación Sanitaria de Lodos”, en el Artículo 6o, se

señala que “se considerarán lodos estabilizados o con reducción del potencial de atracción

de vectores sanitarios, a los lodos que se les ha reducido los sólidos volátiles en un 38 %

como mínimo”.

Además se indica que “Sin perjuicio de lo anterior, también se considerarán **estabilizados**,

los lodos que cumplan con otros requerimientos.

Como se indicó previamente, el tratamiento secundario de la PTAS de Iloca, presenta una

doble modalidad de operación, lo que implica que para la condición de invierno se cumple

con lo indicado en el Reglamento Para el Manejo de Lodos Generados en Plantas de

Tratamiento, específicamente con lo indicado en el Art. 6, párrafo 6, ya que el tiempo de

residencia celular tal como se ha señalado, será mayor a 25 d “en la misma unidad que

ocurre la oxidación biológica de la materia orgánica”.

Para la condición de verano la operación de la planta será en modalidad de media carga

(SRT=9 d), por lo que los lodos generados en la PTAS Iloca no cumplen con los criterios de

lodos estabilizados mencionados en los párrafos anteriores, por lo tanto se consideran

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 26_

_Rev A._

### C & H I ngenieros

lodos **No estabilizados** . Dada esta condición del lodo, se transportarán hacia el un sitio de

disposición debidamente autorizado por la autoridad competente . En esta última

instalación serán estabilizados, para su posterior disposición.

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 27_

_Rev A._

### C & H I ngenieros

**7** **PROGRAMA** **DE** **CONTROL** **DE** **PARÁMETROS** **CRÍTICOS**

El D.S. N° 4 en su Artículo 9°, indica que se debe considerar la identificación y control de

parámetros críticos de operación del sistema de manejo de lodos, con el objeto de prevenir

la emanación de malos olores y en general la ocurrencia de eventos que pongan en riesgo

la salud de las personas y el medio ambiente.

El lodo generado en la PTAS contará con un SRT menor a <25 días en condición de Verano

y un SRT igual o superior a >25 días para el resto del año, por lo que de acuerdo a lo

señalado en el Artículo 6° del D.S. N°4, no es posible clasificarlo como Lodo Estabilizado en

verano y es posible clasificarlo como Lodo Estabilizado para el resto de año, Dado a lo

anterior, el programa de control de parámetros críticos se abocará a demostrar que dichas

condiciones se cumplan satisfactoriamente

Para comprender la propuesta de parámetros de control a aplicar en la línea de lodos de la

PTAS, se da a conocer la metodología que permite determinar el tiempo de residencia de

lodos total (SRT) y posteriormente se entregan los parámetros a determinar y su frecuencia

de control.

**7.1** **M** **ETODOLOGÍA DE** **C** **ONTROL** **P** **ROPUESTA**

Para determinar la edad del lodo en el estanque de aireación se considerará la siguiente

relación:

_Masa_ _total_ _de_ _sólidos_ _en_ _el_ _sistema_ _de_ _aireación_
_SRT_ 

_Masa_ _total_ _extraída_ _del_ _sistema_

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 28_

_Rev A._

### C & H I ngenieros

La expresión corresponde a la ecuación 2:

_V_  _X_
_SRT_  **Ecuación N° 2**

_Qw_  _Xw_

Donde:

V : Volumen del estanque de aireación, [m3]

X : Concentración de sólidos suspendidos totales, [Kg/m3]

Qw : Caudal lodo de desecho (WAS), [m3/d]

Xw : Concentración de sólidos en la línea de purga de lodos (WAS), [Kg/m3]

**7.2** **P** **ARÁMETROS** **C** **RÍTICOS A** **C** **ONTROLAR**

Coherente con las metodologías descritas para la determinación del grado de

estabilización del lodo en el sistema, se consideran los siguientes parámetros a medir

(ver Tabla 10), los que corresponden a registros de operación a realizar in situ y

resultados de parámetros medidos en laboratorio.

**TABLA 12: CONTROL DE PARÁMETROS CRÍTICOS**

|PARÁMETRO|UNIDAD|FRECUENCIA<br>DE MEDICIÓN<br>(N°/MES)|PUNTO DE MEDICIÓN|
|---|---|---|---|
|Concentración SSLM|kg/m3|1|Reactor Biológico|
|**PURGA DE LODOS (WAS)**|**PURGA DE LODOS (WAS)**|**PURGA DE LODOS (WAS)**|**PURGA DE LODOS (WAS)**|
|Volumen Diario|m3|1|Línea de WAS|
|Concentración|kg/m3|1|Línea de WAS|
|**LODO DESHIDRATADO**|**LODO DESHIDRATADO**|**LODO DESHIDRATADO**|**LODO DESHIDRATADO**|
|Volumen Diario|m33|1|Salida de Filtro de Bandas|
|Concentración|kg/m3|1|Salida de Filtro de Bandas|

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 29_

_Rev A._

### C & H I ngenieros

**8** **PLAN** **DE** **CONTINGENCIAS**

El Plan de Contingencias tiene por objetivo lograr el control de cualquier episodio crítico

que se pueda producir en la operación de una planta de tratamiento de aguas servidas y en

particular en la línea de lodos, en el menor tiempo posible y con la mayor coordinación,

sincronización y el menor riesgo de personal involucrado.

Para lograr dicho objetivo se deben identificar los riesgos que amenacen la continuidad del

sistema y proponer la implementación de procedimientos, ante un episodio crítico,

utilizando de manera eficiente los recursos internos y coordinando con instituciones de

apoyo externas.

**8.1** **P** **ROCEDIMIENTOS DE** **E** **MERGENCIAS**

El D.S. N° 4 establece que se debe presentar un Plan de Contingencias que deberá

considerar todas las medidas necesarias para dar cuenta del resultado del Programa de

Control de Parámetros Críticos de la Operación del Sistema de Manejo de Lodos y de

cualquier falla o desperfecto de las unidades, equipos o componentes de dicho Sistema que

puedan tener como resultado riesgos para la salud, el medio ambiente o el bienestar de la

población.

Los episodios críticos de la planta pueden presentarse debido a los siguientes casos y

situaciones:

 Cortes de Energía Eléctrica

 Desperfectos en los Equipos del Sistema

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 30_

_Rev A._

### C & H I ngenieros

 - Déficit en el Suministro de Insumos de Proceso

 - Generación de Olores

El diseño de la planta de tratamiento considera la ocurrencia de estas contingencias, de

modo de poder absorber sus efectos y prevenir las fallas, en vez de confiar en reacciones

coyunturales frente a eventos imprevistos.

Se debe tener en cuenta, que el diseño de la Planta de Tratamiento se realizó para la

población del año 2030, por lo que sus estructuras se encuentran diseñadas para dicho

horizonte.

A continuación se indica la forma en la cual se abordarán los episodios críticos indicados

previamente:

**8.1.1** **C** **ORTES DE** **E** **NERGÍA** **E** **LÉCTRICA**

La Planta de Tratamiento depende para su funcionamiento de la energía eléctrica que

abastece a las instalaciones y equipos. Debido a ello el diseño de la PTAS considera el

respaldo de energía eléctrica a través de la dotación de un grupo generador. El equipo

cuenta con partida automática, que permite, ante una falla del suministro de la red,

energizar inmediatamente y sin intervención del personal de operación, las instalaciones

correspondientes.

La capacidad del grupo electrógeno permite funcionar a las unidades correspondientes de

acuerdo a lo siguiente:

- Bombeo de lodos

Espesador de lodos

- Sistema de aireación

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 31_

_Rev A._

### C & H I ngenieros

Instrumentación y control

- Iluminación

Como cualquier equipo de la planta, el generador tiene una rutina de mantenimiento

definida en el Manual de Mantención, para asegurar su correcto funcionamiento. Sin

embargo, se considera adicionalmente una rutina de partidas programadas, simulando

cortes de energía, para garantizar su funcionamiento cuando sea efectivamente requerido.

**8.1.2** **D** **ESPERFECTOS EN LOS** **C** **OMPONENTES DEL** **S** **ISTEMA**

Todos los equipos mecánicos y eléctricos de la planta se encuentran con unidades de

respaldo (stand by) instaladas, destinadas a operar mientras se realiza mantención o

reparaciones de los equipos restantes.

Para evitar el desperfecto de los equipos, su mantenimiento es una labor muy importante y

rutinaria por lo que se encuentra dentro del programa de actividades del personal

operador. Las reparaciones corresponden a labores accidentales que tienden a ser nulas

cuando el mantenimiento preventivo se realiza adecuadamente.

En el Manual de Mantenimiento se indica para todos los equipos de la planta, las labores y

la frecuencia de mantenimiento preventivo que en cada caso recomienda el fabricante,

incluyendo el cambio de piezas, lubricantes y otros.

**8.1.3** **D** **ÉFICIT EN EL** **S** **UMINISTRO DE** **I** **NSUMOS DE** **P** **ROCESO**

Para la línea de lodos el insumo para el tratamiento corresponde a polímero para el proceso

de deshidratado de lodos. Para éste la planta cuenta con espacio y capacidad de

almacenamiento suficiente, por lo que la programación de abastecimiento resulta fácil y

segura para la operación de la planta. De esta manera se ha previsto evitar eventualidades

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 32_

_Rev A._

### C & H I ngenieros

que afecten el suministro, ya que el tiempo disponible para actuar es más que suficiente. En

caso que se produjese un déficit de estos insumos se recurrirá a stock de emergencia que

podrán ser abastecidos por plantas de localidades cercanas o por bodega central.

**8.1.4** **G** **ENERACIÓN DE** **O** **LORES**

La emanación de olores en un sistema de tratamiento, corresponde a una consecuencia

producto de problemas de funcionamiento en los sistemas de tratamiento. Si la línea de

lodos posee buenas condiciones de operación el equipamiento y los procesos operan

conforme a lo establecido en el diseño, los problemas de olores no debieran existir.

_Proyecto de Ingeniería de Tratamiento de Lodos PTAS Iloca_ _Página 33_

_Rev A._