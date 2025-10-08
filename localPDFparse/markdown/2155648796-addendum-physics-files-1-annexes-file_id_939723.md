---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: report
pages: 10
has_toc: False
has_tables: True
extraction_quality: high
---

|SUR SOLAR SPA|ADENDA<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA LAS<br>GUINDILLAS|Col3|Col4|
|---|---|---|---|
|<br>SUR SOLAR SPA|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|
|<br>SUR SOLAR SPA|OCTUBRE 2022|Rev.: 0|Rev.: 0|

**ÍNDICE DE CONTENIDOS**

**1.** **INTRODUCCIÓN ................................................................................................................................... 3**

**2.** **OBJETIVO ............................................................................................................................................ 3**

**3.** **MODELACIÓN DE EMISIONES ATMOSFÉRICAS MEDIANTE MODELO DE DISPERSIÓN ........................... 3**

3.1 S CREEN V IEW ........................................................................................................................................ 4

3.2 C ARACTERÍSTICAS DEL P ROYECTO .............................................................................................................. 4

3.3 M ODELACIÓN SCREEN VIEW ................................................................................................................. 4

_3.3.1_ _Etapa de Construcción .................................................................................................................. 5_

**4.** **CONCLUSIÓN ..................................................................................................................................... 10**

**ÍNDICE DE FIGURAS**

F IGURA 1: C ONCENTRACIÓN DE MP10 V / S D ISTANCIA - E. C ONSTRUCCIÓN ...................................................................... 5

F IGURA 2 C ONCENTRACIÓN DE MP2.5 V / S D ISTANCIA - E. C ONSTRUCCIÓN ...................................................................... 6

F IGURA 3: C ONCENTRACIÓN DE CO V / S D ISTANCIA - E. C ONSTRUCCIÓN ........................................................................... 7

F IGURA 4: C ONCENTRACIÓN DE NO V / S D ISTANCIA - E. C ONSTRUCCIÓN .......................................................................... 8

F IGURA 5: C ONCENTRACIÓN DE SO V / S D ISTANCIA - E. C ONSTRUCCIÓN ........................................................................... 9

**ÍNDICE DE TABLAS**

T ABLA 1: F ACTORES DE CORRECCIÓN SEGÚN TEMPORALIDAD ........................................................................................... 4

T ABLA 2: T RANSFORMACIÓN DE EMISIÓN, F ASE C ONSTRUCCIÓN ...................................................................................... 5

T ABLA 3: V ERIFICA M ARCO N ORMATIVO, M ATERIAL P ARTICULADO MP10 - E. C ONSTRUCCIÓN ........................................... 5

T ABLA 4: V ERIFICA M ARCO N ORMATIVO, M ATERIAL P ARTICULADO MP2.5 - E. C ONSTRUCCIÓN .......................................... 6

T ABLA 5: V ERIFICA M ARCO N ORMATIVO, M ONÓXIDO DE C ARBONO - E. C ONSTRUCCIÓN .................................................... 7

T ABLA 6: V ERIFICA M ARCO N ORMATIVO, D IÓXIDO DE NITRÓGENO - E. C ONSTRUCCIÓN ...................................................... 8

T ABLA 7: V ERIFICA M ARCO N ORMATIVO, D IÓXIDO DE AZUFRE -E. C ONSTRUCCIÓN .............................................................. 9

Anexo 10: Análisis de contaminantes-Normas de calidad primaria del aire Página **2** de **10**

|SUR SOLAR SPA|ADENDA<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA LAS<br>GUINDILLAS|Col3|Col4|
|---|---|---|---|
|<br>SUR SOLAR SPA|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|
|<br>SUR SOLAR SPA|OCTUBRE 2022|Rev.: 0|Rev.: 0|

**1.** **INTRODUCCIÓN**

El presente apéndice expondrá los antecedentes que fundamenten la no generación de riesgo a la
salud de la población, según lo señalado en el literal a) del artículo 5° del Reglamento del Sistema
de Evaluación de Impacto Ambiental (RSEIA).

La Nueva Central Solar Fotovoltaica Las Guindillas generará emisión de contaminantes en cada una
de sus fases (Construcción, Operación y Cierre) y cuya estimación fue declarada en el Anexo 7:
Informe de emisiones atmosféricas, entregado en el marco de presentación de la DIA, informe que
es actualizado e incorporado en el Anexo 6: E.E Actualizada de la presente adenda. Los resultados
obtenidos en la estimación serán modelados a través del programa SCREEN VIEW 4.0.1 mediante
dispersión atmosféricas, para luego efectuar un análisis de los valores en términos de
concentraciones (ug/m3) y ser comparados con los periodos establecidos en las Normas de Calidad
vigentes (Norma de calidad primaria para material particulado respirable MP10, Norma de calidad
primaria para material particulado respirable MP2,5, norma primaria de calidad de aire para dióxido
de azufre, norma primaria de calidad de aire para dióxido de nitrógeno y norma primaria de calidad
de aire para monóxido de carbono).

**2.** **OBJETIVO**

Verificar el cumplimiento normativo a nivel de concentración de contaminantes para cada fase del
proyecto, garantizando con ello, la no generación de riesgo a la salud de la población producto de
la materialización y ejecución de la Nueva Central Solar Fotovoltaica Las Guindillas.

**3.** **MODELACIÓN DE EMISIONES ATMOSFÉRICAS MEDIANTE MODELO DE DISPERSIÓN**

Los resultados presentados en el Anexo 6: E.E Actualizada de la presente Adenda, serán modelados
a través del programa Screening Air Dispersion Model (SCREEN VIEW) con el objeto de obtener un
espectro de dispersión de los contaminantes.

Dado que el proyecto transitará por diferentes fases (Construcción, Operación y Cierre), la
modelación propuesta considera efectuar el análisis de contaminantes sobre la fase que genera la
mayor fuente de emisión. Por tanto, el análisis se efectuará para los valores obtenidos en la fase de

Construcción.

La modelación a realizar responde a la necesidad de evaluar la polución emitida por la ejecución del
proyecto en su fase más contaminante, respecto de los límites establecidos por las normas primarias
de calidad del Aire para cada uno de ellos.

A continuación, se establece el programa a utilizar y los datos requeridos por el mismo para
implementar la modelación propuesta.

Anexo 10: Análisis de contaminantes-Normas de calidad primaria del aire Página **3** de **10**

|SUR SOLAR SPA|ADENDA<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA LAS<br>GUINDILLAS|Col3|Col4|
|---|---|---|---|
|<br>SUR SOLAR SPA|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|
|<br>SUR SOLAR SPA|OCTUBRE 2022|Rev.: 0|Rev.: 0|

**3.1** **Screen View**

El software computacional utilizado es un modelo de sondeo de la dispersión de contaminantes en
el aire a partir de diversas fuentes. Este software está basado en el código abierto del modelo
SCREEN3, desarrollado por EPA.

Considerado que el software (SCREEN VIEW), tienen como restricción la entrega de concentraciones
horarias y que los límites establecidos en las normas primarias de calidad del Aire están referidas a
concentraciones diarias y anuales, la homologación de éstas concentraciones se realiza mediante
factores de corrección establecidos en “Screening Procedures for Estimating the Air Quality Impact
of Stationary Sources” [1] ; documento emitido por la Agencia de Protección Ambiental de los Estados
Unidos (EPA). En virtud de lo referenciado, se establecen los factores de corrección señalados para
cada condición temporal.

**Tabla 1: Factores de corrección según temporalidad**

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- factores de corrección establecidos en “Screening Procedures for Estimating the Air Quality Impact of Stationary Sources” [1] ; documento emitido por la Agencia de Protección Ambiental de los Estados Unidos (EPA). En virtud de lo referenciado, se establecen los factores de corrección señalados para cada condición temporal. -->

**Tabla 1: Factores de corrección según temporalidad****

| Temporalidad | Factor de Corrección |
| --- | --- |
| 8 horas | 0.7 |
| 24 horas | 0.4 |
| Anual | 0.08 |

<!-- Estadísticas: 3 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia Respecto de las unidades presentadas en la valorización de la estimación de emisiones atmosféricas actualizadas entregadas en Anexo 6 de la presente Adenda, esto es, ton/año, éstas deben ser -->
<!-- FIN TABLA 1 -->


|Temporalidad|Factor de Corrección|
|---|---|
|8 horas|0.7|
|24 horas|0.4|
|Anual|0.08|

Fuente: Elaboración propia

Respecto de las unidades presentadas en la valorización de la estimación de emisiones atmosféricas
actualizadas entregadas en Anexo 6 de la presente Adenda, esto es, ton/año, éstas deben ser
transformadas a la unidad solicitada por el programa (g/s/m2).

**3.2** **Características del Proyecto**

El proyecto será emplazado en un predio rural, ubicado en la Región de O ́Higgins y abarcará un área
total de 16 hectárea de superficie plana y libre de sinuosidades, por lo cual el terreno es considerado
plano y simple para efectos de la modelación, asumiendo una altura de emisión de 0.5m, puesto
que todas las actividades se materializan a nivel de terreno.

En cuanto al valor de la velocidad del viento, se ha considerado el valor peack registrado a través de
la fuente online del Explorador Eólico del Ministerio de Energía; valor que se establece en 3,8m/s.
De la misma fuente, se estima que la dirección del viento proviene de orientación Sur,
específicamente a un promedio de 200 grados; Valor deducido como promedio de la gráfica
configurada para la rosa de vientos del sector.

**3.3** **Modelación SCREEN VIEW**

A continuación, se presenta la modelación efectuada para la fase de construcción del Proyecto.

1 [https://nepis.epa.gov/Exe/ZyPDF.cgi/2000J3ER.PDF?Dockey=2000J3ER.PDF](https://nepis.epa.gov/Exe/ZyPDF.cgi/2000J3ER.PDF?Dockey=2000J3ER.PDF)

Anexo 10: Análisis de contaminantes-Normas de calidad primaria del aire Página **4** de **10**

|SUR SOLAR SPA|ADENDA<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA LAS<br>GUINDILLAS|Col3|Col4|
|---|---|---|---|
|<br>SUR SOLAR SPA|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|
|<br>SUR SOLAR SPA|OCTUBRE 2022|Rev.: 0|Rev.: 0|

**3.3.1** **Etapa de Construcción**

Los resultados obtenidos en la estimación de emisiones atmosféricas y la transformación de unidad
requerida para cada contaminante se ilustran en la siguiente tabla.

**Tabla 2: Transformación de emisión, Fase Construcción**

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **3.3.1** **Etapa de Construcción** Los resultados obtenidos en la estimación de emisiones atmosféricas y la transformación de unidad requerida para cada contaminante se ilustran en la siguiente tabla. -->

**Tabla 2: Transformación de emisión, Fase Construcción****

| Contaminante | Emisión<br>(ton/fase) | Emisión<br>(g/s/m2) |
| --- | --- | --- |
| MP10 | 1.027347 | 2.03x10-7 |
| MP2,5 | 0.470099 | 9.31x10-8 |
| COX | 0.798378 | 1.58x10-7 |
| NOX | 2.795217 | 5.54x10-7 |
| SOX | 0.079109 | 1.57x10-8 |

<!-- Estadísticas: 5 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia Los resultados de la modelación para la fase en análisis se presentan a continuación. -->
<!-- FIN TABLA 2 -->


|Contaminante|Emisión<br>(ton/fase)|Emisión<br>(g/s/m2)|
|---|---|---|
|MP10|1.027347|2.03x10-7|
|MP2,5|0.470099|9.31x10-8|
|COX|0.798378|1.58x10-7|
|NOX|2.795217|5.54x10-7|
|SOX|0.079109|1.57x10-8|

Fuente: Elaboración propia

Los resultados de la modelación para la fase en análisis se presentan a continuación.

 - **MP10**

**Figura 1: Concentración de MP10 v/s Distancia - E. Construcción**

Fuente: Elaboración propia

**Tabla 3: Verifica Marco Normativo, Material Particulado MP10 - E. Construcción**

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 1: Concentración de MP10 v/s Distancia - E. Construcción** Fuente: Elaboración propia -->

**Tabla 3: Verifica Marco Normativo, Material Particulado MP10 - E. Construcción****

| Contaminante | Concentración<br>Proyecto<br>(ug/m3) | Corrección por<br>Concentración<br>24 horas<br>(ug/m3) | Corrección por<br>Concentración<br>Anual<br>(ug/m3) | Límite<br>Normativo<br>Decreto<br>12/2021<br>24 h<br>(ug/m3) | Límite<br>Normativo<br>Decreto<br>12/2021<br>Anual<br>(ug/m3) | Verificación<br>marco<br>Normativo |
| --- | --- | --- | --- | --- | --- | --- |
| **MP10** | **17.19 ** | **6.88** | **1.38** | **130** | **50** | **Cumple** |

<!-- Estadísticas: 1 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia Considerando los resultados obtenidos, se puede corroborar que el proyecto generará una concentración de contaminantes que está muy por debajo de lo impuesto por la normativa, -->
<!-- FIN TABLA 3 -->


|Contaminante|Concentración<br>Proyecto<br>(ug/m3)|Corrección por<br>Concentración<br>24 horas<br>(ug/m3)|Corrección por<br>Concentración<br>Anual<br>(ug/m3)|Límite<br>Normativo<br>Decreto<br>12/2021<br>24 h<br>(ug/m3)|Límite<br>Normativo<br>Decreto<br>12/2021<br>Anual<br>(ug/m3)|Verificación<br>marco<br>Normativo|
|---|---|---|---|---|---|---|
|**MP10**|**17.19 **|**6.88**|**1.38**|**130**|**50**|**Cumple**|

Fuente: Elaboración propia

Considerando los resultados obtenidos, se puede corroborar que el proyecto generará una
concentración de contaminantes que está muy por debajo de lo impuesto por la normativa,
asegurando la no superación de concentración de material particulado grueso en esta fase. Además,
se puede establecer que la concentración de MP10 disminuye drásticamente a una distancia de
300m del proyecto, con lo cual se descarta la generación de riesgo a la salud de la población.

Anexo 10: Análisis de contaminantes-Normas de calidad primaria del aire Página **5** de **10**

|SUR SOLAR SPA|ADENDA<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA LAS<br>GUINDILLAS|Col3|Col4|
|---|---|---|---|
|<br>SUR SOLAR SPA|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|
|<br>SUR SOLAR SPA|OCTUBRE 2022|Rev.: 0|Rev.: 0|

- **MP2.5**

**Figura 2 Concentración de MP2.5 v/s Distancia - E. Construcción**

Fuente: Elaboración propia

**Tabla 4: Verifica Marco Normativo, Material Particulado MP2.5 - E. Construcción**

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 2 Concentración de MP2.5 v/s Distancia - E. Construcción** Fuente: Elaboración propia -->

**Tabla 4: Verifica Marco Normativo, Material Particulado MP2.5 - E. Construcción****

| Contaminante | Concentración<br>Proyecto<br>(ug/m3) | Corrección por<br>Concentración<br>24 horas<br>(ug/m3) | Corrección por<br>Concentración<br>Anual<br>(ug/m3) | Límite<br>Normativo<br>Decreto<br>12/2011<br>24 h<br>(ug/m3) | Límite<br>Normativo<br>Decreto<br>12/2011<br>Anual<br>(ug/m3) | Verificación<br>marco<br>Normativo |
| --- | --- | --- | --- | --- | --- | --- |
| **MP2.5** | **7.885 ** | **3.154** | **0.6308** | **50** | **20** | **Cumple** |

<!-- Estadísticas: 1 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia Considerando los resultados obtenidos, se puede corroborar que el proyecto generará una concentración de contaminantes que está muy por debajo de lo impuesto por la normativa, -->
<!-- FIN TABLA 4 -->


|Contaminante|Concentración<br>Proyecto<br>(ug/m3)|Corrección por<br>Concentración<br>24 horas<br>(ug/m3)|Corrección por<br>Concentración<br>Anual<br>(ug/m3)|Límite<br>Normativo<br>Decreto<br>12/2011<br>24 h<br>(ug/m3)|Límite<br>Normativo<br>Decreto<br>12/2011<br>Anual<br>(ug/m3)|Verificación<br>marco<br>Normativo|
|---|---|---|---|---|---|---|
|**MP2.5**|**7.885 **|**3.154**|**0.6308**|**50**|**20**|**Cumple**|

Fuente: Elaboración propia

Considerando los resultados obtenidos, se puede corroborar que el proyecto generará una
concentración de contaminantes que está muy por debajo de lo impuesto por la normativa,
asegurando la no superación de concentración de material particulado fino en esta fase. Además,
se puede establecer que la concentración de MP2.5 disminuye drásticamente a una distancia de
300m del proyecto, con lo cual se descarta la generación de riesgo a la salud de la población.

Anexo 10: Análisis de contaminantes-Normas de calidad primaria del aire Página **6** de **10**

|SUR SOLAR SPA|ADENDA<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA LAS<br>GUINDILLAS|Col3|Col4|
|---|---|---|---|
|<br>SUR SOLAR SPA|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|
|<br>SUR SOLAR SPA|OCTUBRE 2022|Rev.: 0|Rev.: 0|

- **CO** **X**

**Figura 3: Concentración de CO v/s Distancia - E. Construcción**

Fuente: Elaboración propia

**Tabla 5: Verifica Marco Normativo, Monóxido de Carbono - E. Construcción**

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 3: Concentración de CO v/s Distancia - E. Construcción** Fuente: Elaboración propia -->

**Tabla 5: Verifica Marco Normativo, Monóxido de Carbono - E. Construcción****

| Contaminante | Concentración Proyecto (ug/m3) | Conversión2 Concentración 1 horas (mg/m3) | Corrección por 3Concentración 8h (mg/m3) | Límite Normativo Decreto 115/2002 1 h (mg/m3N) | Límite Normativo Decreto 115/2002 8 h (mg/m3N) | Verificación marco Normativo 1h | Verificación marco Normativo 8h |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CO** | **13.38** | **0.01338** | **0.00937** | **30** | **10** | **Cumple** | **Cumple** |

<!-- Estadísticas: 1 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia Considerando los resultados obtenidos, se puede corroborar que el proyecto generará una concentración de contaminantes que está muy por debajo de lo impuesto por la normativa, -->
<!-- FIN TABLA 5 -->


|Contaminante|Concentración Proyecto (ug/m3)|Conversión2 Concentración 1 horas (mg/m3)|Corrección por 3Concentración 8h (mg/m3)|Límite Normativo Decreto 115/2002 1 h (mg/m3N)|Límite Normativo Decreto 115/2002 8 h (mg/m3N)|Verificación marco Normativo 1h|Verificación marco Normativo 8h|
|---|---|---|---|---|---|---|---|
|**CO**|**13.38**|**0.01338**|**0.00937**|**30**|**10**|**Cumple**|**Cumple**|

Fuente: Elaboración propia

Considerando los resultados obtenidos, se puede corroborar que el proyecto generará una
concentración de contaminantes que está muy por debajo de lo impuesto por la normativa,
asegurando la no superación de concentración de monóxido de carbono en esta fase. Además, se
puede establecer que la concentración de CO disminuye drásticamente a una distancia de 300m del
proyecto, con lo cual se descarta la generación de riesgo a la salud de la población.

2 Conversión de Microgramo a Miligramo
3 Valor establecido por corrección por concentración y conversión de unidad

Anexo 10: Análisis de contaminantes-Normas de calidad primaria del aire Página **7** de **10**

|SUR SOLAR SPA|ADENDA<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA LAS<br>GUINDILLAS|Col3|Col4|
|---|---|---|---|
|<br>SUR SOLAR SPA|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|
|<br>SUR SOLAR SPA|OCTUBRE 2022|Rev.: 0|Rev.: 0|

- **NO** **X**

**Figura 4: Concentración de NO v/s Distancia - E. Construcción**

Fuente: Elaboración propia

**Tabla 6: Verifica Marco Normativo, Dióxido de nitrógeno - E. Construcción**

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 4: Concentración de NO v/s Distancia - E. Construcción** Fuente: Elaboración propia -->

**Tabla 6: Verifica Marco Normativo, Dióxido de nitrógeno - E. Construcción****

| Contaminante | Concentración Proyecto (ug/m3) | Concentración 1 horas (ug/m3N) | Corrección por Concentración Anual (ug/m3N) | Límite Normativo Decreto 114/2002 1 h (ug/m3N) | Límite Normativo Decreto 114/2002 Anual (ug/m3N) | Verificación marco Normativo 1h | Verificación marco Normativo Anual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **NO** | **46.92** | **46.92** | **3.754** | **400** | **100** | **Cumple** | **Cumple** |

<!-- Estadísticas: 1 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia Considerando los resultados obtenidos, se puede corroborar que el proyecto generará una concentración de contaminantes que está muy por debajo de lo impuesto por la normativa, -->
<!-- FIN TABLA 6 -->


|Contaminante|Concentración Proyecto (ug/m3)|Concentración 1 horas (ug/m3N)|Corrección por Concentración Anual (ug/m3N)|Límite Normativo Decreto 114/2002 1 h (ug/m3N)|Límite Normativo Decreto 114/2002 Anual (ug/m3N)|Verificación marco Normativo 1h|Verificación marco Normativo Anual|
|---|---|---|---|---|---|---|---|
|**NO**|**46.92**|**46.92**|**3.754**|**400**|**100**|**Cumple**|**Cumple**|

Fuente: Elaboración propia

Considerando los resultados obtenidos, se puede corroborar que el proyecto generará una
concentración de contaminantes que está muy por debajo de lo impuesto por la normativa,
asegurando la no superación de concentración de dióxido de nitrógeno en esta fase. Además, se
puede establecer que la concentración de “NO” disminuye drásticamente a una distancia de 300m
del proyecto, con lo cual se descarta la generación de riesgo a la salud de la población.

Anexo 10: Análisis de contaminantes-Normas de calidad primaria del aire Página **8** de **10**

|SUR SOLAR SPA|ADENDA<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA LAS<br>GUINDILLAS|Col3|Col4|
|---|---|---|---|
|<br>SUR SOLAR SPA|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|
|<br>SUR SOLAR SPA|OCTUBRE 2022|Rev.: 0|Rev.: 0|

- **SO** **X**

**Figura 5: Concentración de SO v/s Distancia - E. Construcción**

Fuente: Elaboración propia

**Tabla 7: Verifica Marco Normativo, Dióxido de azufre -E. Construcción**

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 5: Concentración de SO v/s Distancia - E. Construcción** Fuente: Elaboración propia -->

**Tabla 7: Verifica Marco Normativo, Dióxido de azufre -E. Construcción****

| Contaminante | Concentración Proyecto (ug/m3N) | Corrección por Concentración 24h (ug/m3N) | Corrección por Concentración Anual (ug/m3N) | Límite Normativo Decreto 113/2010 24 h (ug/m3N) | Límite Normativo Decreto 113/2002 Anual (ug/m3N) | Verificación marco Normativo 24h | Verificación marco Normativo Anual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SO** | **1.330** | **0.532** | **0.1064** | **150** | **60** | **Cumple** | **Cumple** |

<!-- Estadísticas: 1 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia Considerando los resultados obtenidos, se puede corroborar que el proyecto generará una concentración de contaminantes que está muy por debajo de lo impuesto por la normativa, -->
<!-- FIN TABLA 7 -->


|Contaminante|Concentración Proyecto (ug/m3N)|Corrección por Concentración 24h (ug/m3N)|Corrección por Concentración Anual (ug/m3N)|Límite Normativo Decreto 113/2010 24 h (ug/m3N)|Límite Normativo Decreto 113/2002 Anual (ug/m3N)|Verificación marco Normativo 24h|Verificación marco Normativo Anual|
|---|---|---|---|---|---|---|---|
|**SO**|**1.330**|**0.532**|**0.1064**|**150**|**60**|**Cumple**|**Cumple**|

Fuente: Elaboración propia

Considerando los resultados obtenidos, se puede corroborar que el proyecto generará una
concentración de contaminantes que está muy por debajo de lo impuesto por la normativa,
asegurando la no superación de concentración de dióxido de azufre en esta fase. Además, se puede
establecer que la concentración de SOx disminuye drásticamente a una distancia de 300m del
proyecto, con lo cual se descarta la generación de riesgo a la salud de la población.

Anexo 10: Análisis de contaminantes-Normas de calidad primaria del aire Página **9** de **10**

|SUR SOLAR SPA|ADENDA<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA LAS<br>GUINDILLAS|Col3|Col4|
|---|---|---|---|
|<br>SUR SOLAR SPA|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|ANEXO 10: ANALISIS DE CONTAMINANTES|
|<br>SUR SOLAR SPA|OCTUBRE 2022|Rev.: 0|Rev.: 0|

**4.** **CONCLUSIÓN**

El desarrollo del presente apéndice entregó los antecedentes necesarios para demostrar el
cumplimiento normativo por parte del proyecto Nueva Central Solar Fotovoltaica Las Guindillas, en
relación a las normas primarias de calidad del aire para los contaminantes, Material Particulado
Respirable MP10, Material Particulado Respirable MP2.5, Dióxido de nitrógeno, Dióxido de azufre y
Monóxido de carbono, al no sobrepasar los límites de concentración interpuestos por la normativa
vigente en su etapa de mayor generación de niveles de emisiones, por tanto, se puede concluir que
la NCSF Las Guindillas, no superará la normativa en ninguna de sus fases (Construcción, operación y
cierre). Lo anterior, refleja que la dispersión de los contaminantes en cada una de las fases está muy
por debajo de los máximos permitidos.

Finalmente, señalar que la concentración de las emisiones se densifica y alcanza su máximo a una
distancia de 300m alrededor del proyecto, presentando una disminución gradual a medida que la
distancia aumenta y por ende se aleja del ente emisor (Nueva Central Solar Fotovoltaica).

En virtud de los resultados obtenidos en el presente análisis de concentración, se puede descartar:

1.- La generación de riesgo a la salud de la población.

2.- Sobrepasar los límites máximos indicados por la normativa.

Anexo 10: Análisis de contaminantes-Normas de calidad primaria del aire Página **10** de **10**