---
title: Proyecto Iquique Terminal Internacional
author: José Ribba Esteva
date: D:20211018100946-03'00'
language: es
type: report
pages: 166
has_toc: False
has_tables: True
extraction_quality: high
keywords: [“Suministro Hídrico Compañía Minera Cerro Colorado”]
---

**Estudio de Vientos**

**Proyecto Iquique Terminal Internacional**

Solicitado Por:

**Casa Central**
Esmeralda 340, Oficina 720

Edificio Esmeralda

Iquique, Chile.

Preparado Por:

**Casa Matriz**
Limache 3405, Of. 31-33,
Edificio Reitz de las Empresas

El Salto, Viña Del Mar - Chile

Teléfono 56 32 2189200

info@ecotecnos.cl

|Rev.|Fecha|Propósito de la emisión|Por|Rev.|Apr.|
|---|---|---|---|---|---|
|B|31-05-2021|Revisión Interna|A. González|P. Monreal|M. Quezada|
|A1|09-07-2021|Revisión SHOA|A. González|P. Monreal|SHOA|
|A2|19-10-2021|Revisión SHOA|A. González|P. Monreal|SHOA|
|||||||
|||||||

B: Emitido para revisión interna.
A: Emitido para aprobación del cliente.
0: Aprobado.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

## Profesionales Responsables
### Ecotecnos S.A.

**Departamento de Oceanografía y Modelamiento Matemático**

**Ph.D. Ing. Sr. Matías Quezada L.**
Jefe del Departamento de Oceanografía

Física y Modelamiento Matemático

Doctor en Fluidodinámica

Ingeniero Civil Oceánico

**Ing. Srta. Pía Monreal D.**
Líder en Oceanografía Física

Ingeniero Civil Oceánico

**Ing. Sr. Ariel González A.**

Ingeniero Civil Oceánico

### Ariel González Acevedo

Profesional Ejecutor del Informe

Ing. Civil Oceánico

Rut: 18.457.857-3

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

**ECOTECNOS S.A.**

Limache 3405, Of. 31-33,
Edificio Reitz de las Empresas
El Salto, Viña Del Mar - Chile

El presente informe fue elaborado por ECOTECNOS S.A. a requerimiento de la empresa
Iquique Terminal Internacional S. A., por lo que este documento solamente puede ser utilizado
y divulgado con la autorización expresa de sus propietarios, quedando terminantemente
prohibido el uso y divulgación, de todo o parte, del referido documento, en cualquiera de sus
formas. La información de este documento se encuentra protegida, entre otras normas, por la
Ley N° 17.336 sobre Propiedad Intelectual, publicada en el Diario Oficial N° 27.761, de 2 de

octubre de 1970.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|1|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

## Resumen

En el presente documento se entrega una caracterización del viento reinante (operacional) y
dominante (de diseño) en el sector de estudio comprendido en la Bahía de Iquique, Región de
Tarapacá, bajo la finalidad de dar cumplimiento a lo solicitado en el instructivo SHOA N° 3201.
Estos análisis se realizaron en el marco del estudio de la línea base para el proyecto “Proyecto
Extensión Norte Sitio N° 4, Puerto de Iquique, Región de Tarapacá” requerido por Iquique

Terminal Internacional S. A.

Para cumplir los objetivos del estudio se empleó una base de datos históricos superior a 10
años, comprendidos desde el año 2011 y hasta los primeros meses del año 2021, de
información de magnitud y dirección del viento medidos en la estación ubicada en el aeropuerto
Diego Aracena, Región de Tarapacá y perteneciente a la Dirección Meteorológica de Chile
(DMC). Junto a lo anterior, se contó con los vientos levantados en campo dentro del sector del
proyecto como parte de los estudios de línea base medio marino, en un intervalo aproximado
a un año, el cual se encontró contenido en el periodo de los datos históricos. Ambas bases de
datos fueron correlacionadas, verificándose similitudes en el comportamiento en el tiempo de
la velocidad del viento en ambas series, aunque los base de datos históricos sobrestimó
levemente a las mediciones. La descomposición vectorial demostró una mayor semejanza de
la componente V en comportamiento y magnitud, mientras que, la componente U de las
mediciones _in situ_ demostró una menor intensidad. Por otro lado, las direcciones de ambos
registros coincidieron en su principal concentración de datos sobre el tercer cuadrante.

La base de datos histórica demostró que la velocidad del viento, caracterizada mediante la
escala de Beaufort, predominó en la categoría Aire Ligero y, en segundo lugar, la Brisa Ligera,
concentrándose los registros desde las direcciones SSW, S, SW y WSW. La intensidad del
viento redució su intensidad principalmente durante las estaciones de otoño e invierno,
además de aumentar la dispersión en sus direcciones. El viento durante el día demostró una
reducción de su magnitud en las primeras horas, respecto a su hora UTC, que se incrementó
pasado el medio día.

Referente a las proyecciones estimadas para un periodo de retorno de 30 años, se identificaron
como las direcciones más energéticas serían el S, E y SW con intensidades superiores a los
4 m/s, desde cada una.

### Humberto Díaz Oviedo

Representante Legal

Ecotecnos. S. A.

12.225.916-1

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|2|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

## CONTENIDO

**1** **INTRODUCCIÓN ........................................................................................................... 11**

**2** **OBJETIVOS .................................................................................................................. 13**

**2.1** **Generales .......................................................................................................... 13**

**2.2** **Específicos ....................................................................................................... 13**

**3** **MATERIALES Y MÉTODOS ......................................................................................... 14**

**3.1** **Mediciones de Campo ...................................................................................... 14**

**3.2** **Correlación de la base de datos. ..................................................................... 17**

**3.3** **Caracterización Estadística del registro de datos históricos ........................ 19**
3.3.1 Análisis de ocurrencia para la estacionalidad mensual. ................................... 21
3.3.2 Análisis de ocurrencia para la estacionalidad estacional. ................................. 21
3.3.3 Análisis de ocurrencia para la estacionalidad diaria. ........................................ 21

**3.4** **Clima Extremo de Vientos ................................................................................ 22**

**4** **RESULTADOS .............................................................................................................. 23**

**4.1** **Análisis y Caracterización Estadística de los Datos de Campo .................... 23**
4.1.1 Estadística Descriptiva ..................................................................................... 23
4.1.2 Análisis Espectral ............................................................................................. 29
4.1.3 Vectores Progresivos ....................................................................................... 30

4.1.4 Caracterización Estadística -Mensual ............................................................. 31

4.1.5 Caracterización Estadística -Estacional .......................................................... 55

4.1.6 Caracterización Estadística -Diaria ................................................................. 65

**4.2** **Correlación de la base de datos ...................................................................... 78**

**4.3** **Análisis y Caracterización Estadística de la base de datos histórica ........... 86**
4.3.1 Estadística Descriptiva ..................................................................................... 86
4.3.2 Análisis Espectral ............................................................................................. 92

4.3.3 Caracterización Estadística -Mensual ............................................................. 93

4.3.4 Caracterización Estadística -Estacional ........................................................ 117

4.3.5 Caracterización Estadística -Diaria ............................................................... 127

4.3.6 Análisis de Clima Extremo de Vientos ............................................................ 140

**5** **CONCLUSIÓN ............................................................................................................ 146**

**5.1** **Respecto a los Datos de Campo ................................................................... 146**
**5.2** **Respecto de la Correlación de la Base de Datos ......................................... 147**
**5.3** **Respecto a la Base de Datos histórica ......................................................... 148**

5.3.1 Caracterización Estadística de la Base de Datos Histórico ............................ 148

5.3.2 Clima Extremo de Vientos .............................................................................. 150

**6** **REFERENCIAS ........................................................................................................... 151**

**7** **ANEXO AUTORIZACIÓN DE TRABAJOS ................................................................. 152**

**8** **ANEXO ACTAS DE INSPECCIÓN.............................................................................. 155**

**8.1** **Invierno 2020 ................................................................................................... 155**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|3|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**8.2** **Verano 2020 .................................................................................................... 158**

**9** **ANEXO CERTIFICADOS DE VIGENCIA DE LA SOCIEDAD ..................................... 161**

**10** **ANEXO NOMBRAMIENTO DEL REPRESENTANTE LEGAL .................................... 162**

**LISTADO DE ANEXOS DIGITALES**

Anexo A Acta de Inspección SHOA
Anexo B Estación Meteorológica en sector ITI
Anexo C Estación Base Histórica Diego Aracena
Anexo D Año Medio a partir de la Base Histórica

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|4|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**LISTADO DE TABLAS**

Tabla 1.1: Ubicación aproximada de estaciones meteorológicas. ......................................... 11

<!-- INICIO TABLA 1.1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- contienen el intervalo temporal de las mediciones en el sector de ITI. La información antes descrita, así como los periodos que se han considerado para el presente estudio, se detallan en la Tabla 1.1. -->

**Tabla 1.1: Ubicación aproximada de estaciones meteorológicas.****

| Estudio | Ubicación | Periodo |
| --- | --- | --- |
| Mediciones de Meteorología<br>Diego Aracena | 376.877E 7.727.300N | Desde el 01 enero del 2011 al 17 de<br>marzo del 2021 |
| Mediciones de Meteorología ELB<br>Proyecto Extensión Norte Sitio<br>N° 4. | 379.198E 7.765.592N1 | Desde el 14 febrero del 2020 al 17<br>de marzo del 2021 |

<!-- Estadísticas: 2 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. La ubicación general del sector de proyecto y de las estaciones antes señaladas, se presentan en la Figura 1.1. La distancia que separa a ambas estaciones es aproximadamente de **38 Km**, -->
<!-- FIN TABLA 1.1 -->


Tabla 3-1: Valores de declinación magnética obtenido para la estación de ITI. .................... 14

<!-- INICIO TABLA 3-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- magnitud promedio del viento a una altura aproximada de 13 m.s.n.m., cuyos datos fueron incluidos en el Anexo B. Se debe señalar que la variable tiempo de los datos registrados fue transformada desde el huso horario en el cual fueron medidos al sistema UTC, para permitir la comparación con los datos históricos. -->

**Tabla 3-1: Valores de declinación magnética obtenido para la estación de ITI.****

| Fecha | Valor (°) | Dirección | Modelo |
| --- | --- | --- | --- |
| 01-02-2020 | 5,51 | W | WMM |
| 01-03-2020 | 5,53 | W | WMM |
| 01-04-2020 | 5,55 | W | WMM |
| 01-05-2020 | 5,57 | W | WMM |
| 01-06-2020 | 5,59 | W | WMM |
| 01-07-2020 | 5,60 | W | WMM |
| 01-08-2020 | 5,62 | W | WMM |
| 01-09-2020 | 5,64 | W | WMM |
| 01-10-2020 | 5,66 | W | WMM |
| 01-11-2020 | 5,68 | W | WMM |
| 01-12-2020 | 5,70 | W | WMM |
| 01-01-2021 | 5,72 | W | WMM |
| 01-02-2021 | 5,73 | W | WMM |
| 01-03-2021 | 5,75 | W <br> | WMM<br> |
| **Promedio** | 5,63 | <br> | <br> |

<!-- Estadísticas: 15 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. La información recopilada se procesó para calcular indicadores estadísticos tales como los valores promedios y máximos de toda la serie, y por dirección de procedencia. Los registros -->
<!-- FIN TABLA 3-1 -->


Tabla 3-2: Categorización de la fuerza del viento, de acuerdo a su intensidad. .................... 15

<!-- INICIO TABLA 3-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 2018) [2] y no presentar una dirección clara identificable. Por esta razón, del periodo de mediciones empleado para caracterizar el sector de estudio, desde 14 de febrero del 2020 15:25 hasta 17 de marzo del 2021 17:50, se presenta un total de registros de 114.366 y se contabilizó un total de 25.589 Calmas, lo que representa 22,375 % de los datos. -->

**Tabla 3-2: Categorización de la fuerza del viento, de acuerdo a su intensidad.****

| Col1 | Royal Meteorological Society (2018) | Col3 | Col4 | Modificada | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Fuerza**<br>**Viento** | **Categoría** | **Intensidad**<br>**(km/h)** | **(m/s)** | **Categoría** | **(m/s)** |
| 0 | Calm | <1 | <0,28 | Calma | <0,28 |
| 1 | Light Air | 1-5 | 0,28 - 1,39 | Aire Ligero | [0,28 - 1,39[ |
| 2 | Light Breeze | 6-11 | 1,67 - 3,06 | Brisa Ligera | [1,39 - 3,06[ |
| 3 | Gentle Breeze | 12-19 | 3,33 - 5,28 | Brisa Suave | [3,06 - 5,28[ |
| 4 | Moderate Breeze | 20-28 | 5,56 - 7,78 | Brisa Moderada | [5,28 - 7,78[ |
| 5 | Fresh Breeze | 29-38 | 8,06 - 10,56 | Brisa Fresca | [7,78 - 10,56[ |
| 6 | Strong Breeze | 38-49 | 10,56 - 13,61 | Brisa Fuerte | [10,56 - 13,61[ |
| 7 | Near Gale | 50-61 | 13,89 - 16,94 | Casi Vendaval | [13,61 - 16,94[ |
| 8 | Gale | 62-74 | 17,22 - 20,56 | Vendaval | [16,94 - 20,56[ |
| 9 | Strong Gale | 75-88 | 20,83 - 24,44 | Vendaval Fuerte | [20,56 - 24,44[ |
| 10 | Storm | 89-102 | 24,72 - 28,33 | Tormenta | [24,44 - 28,33[ |
| 11 | Violent Storm | 103-117 | 28,61 - 32,50 | Tormenta<br>Violenta | [28,33 - 32,50[ |
| 12 | Hurricane | 118 plus | ≥32,50 | Huracán | ≥32,50 |

<!-- Estadísticas: 14 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia con información de la Royal Meteorological Society (2018). Adicionalmente, se generaron diagramas de trazos, mediante un código de programación propio que emplea la intensidad y dirección de cada dato, y, en función de la intensidad del -->
<!-- FIN TABLA 3-2 -->


Tabla 3.3: Extracto de la tabla de parámetros friccionales recomendadas por la ROM. ........ 18

<!-- INICIO TABLA 3.3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|18| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 3.3: Extracto de la tabla de parámetros friccionales recomendadas por la ROM.****

| Tipo de Superficie | z (m)<br>0 |
| --- | --- |
| I. Mar abierto y campo abierto llano sin<br>obstáculos (p.e. zonas costeras llanas,<br>desiertos, ...). | 0,001 - 0,01 |
| II. Mar con oleaje muy fuerte y campo<br>abierto, llano u ondulado, con obstáculos<br>dispersos (p.e. praderas, páramos, ...). | 0,01 - 0,3 |
| III. Superficies boscosas, campo con<br>obstáculos abundantes y pequeñas zonas<br>urbanas (obstáculos con alturas entre 9 y 15<br>m). | 0,3 - 1,0 |
| IV. Superficies con grandes y frecuentes<br>obstáculos, y grandes ciudades. | 1,0 - 5,0 |

<!-- Estadísticas: 4 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, a partir de tabla contenida en el documento ROM-04-95-2. Posteriormente, se generó una serie horaria de los registros de vientos medidos en el sitio del proyecto, para hacerla comparable con la del registro histórico del aeropuerto Diego Aracena. -->
<!-- FIN TABLA 3.3 -->


Tabla 4-1: Tabla de incidencia del viento registrado. Mediciones sector ITI. ......................... 26

<!-- INICIO TABLA 4-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|26| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-1: Tabla de incidencia del viento registrado. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 2,203 | 0,673 | 0,020 | - | - | - | 2,896 |
| **NNE** | - | 2,988 | 0,492 | 0,002 | - | - | - | 3,482 |
| **NE** | - | 2,085 | 0,143 | - | - | - | - | 2,228 |
| **ENE** | - | 2,412 | 0,429 | - | - | - | - | 2,841 |
| **E ** | - | 0,716 | 0,021 | - | - | - | - | 0,737 |
| **ESE** | - | 0,632 | 0,042 | - | - | - | - | 0,674 |
| **SE** | - | 0,561 | 0,010 | - | - | - | - | 0,571 |
| **SSE** | - | 0,622 | 0,010 | - | - | - | - | 0,632 |
| **S ** | - | 1,971 | 0,106 | - | - | - | - | 2,077 |
| **SSW** | - | 24,273 | 8,360 | 0,002 | - | - | - | 32,635 |
| **SW** | - | 13,234 | 3,893 | 0,002 | - | - | - | 17,128 |
| **WSW** | - | 2,739 | 0,025 | - | - | - | - | 2,765 |
| **W ** | - | 2,844 | 0,018 | - | - | - | - | 2,862 |
| **WNW** | - | 1,987 | 0,003 | - | - | - | - | 1,991 |
| **NW** | - | 2,171 | 0,016 | - | - | - | - | 2,187 |
| **NNW** | - | 1,747 | 0,170 | 0,003 | - | - | - | 1,920 |
| **Calmas** | 22,375 | - | - | - | - | - | - | 22,375 |
| **Sub Total**<br>**(%)**<br> | 22,375<br> | 63,185<br> | 14,412<br> | 0,029<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 114.366 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-1 -->


Tabla 4-2: Intensidades promedio y máxima globales y por dirección de procedencia de los

<!-- INICIO TABLA 4-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Fuente: Ecotecnos, 2021. **Gráfico 4-5: Variación de la magnitud promedio y máxima del viento por dirección de** **procedencia. Mediciones sector ITI.** -->

**Tabla 4-2: Intensidades promedio y máxima globales y por dirección de procedencia****

| Col1 | Intensidad del viento | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Direcciones** | **Máxima** | **Máxima** | **Promedio** | **Promedio** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N ** | 3,931 | 7,626 | 1,107 | 1,461 |
| **NNE** | 3,141 | 6,094 | 0,961 | 1,864 |
| **NE** | 2,553 | 4,953 | 0,749 | 1,453 |
| **ENE** | 2,948 | 5,719 | 0,913 | 1,770 |
| **E ** | 2,553 | 4,953 | 0,625 | 1,213 |
| **ESE** | 2,553 | 4,953 | 0,727 | 1,411 |
| **SE** | 2,158 | 4,187 | 0,621 | 1,204 |
| **SSE** | 2,755 | 5,345 | 0,617 | 1,197 |
| **S ** | 2,755 | 5,345 | 0,730 | 1,417 |
| **SSW** | 3,141 | 6,094 | 1,133 | 2,197 |
| **SW** | 3,141 | 6,094 | 1,095 | 2,124 |
| **WSW** | 2,360 | 4,578 | 0,696 | 1,351 |
| **W ** | 1,773 | 3,440 | 0,753 | 1,461 |
| **WNW** | 1,570 | 3,046 | 0,717 | 1,391 |
| **NW** | 1,965 | 3,812 | 0,740 | 1,435 |
| **NNW** | 3,536 | 6,860 | 0,885 | 1,716 |
| **Global** | 3,931 | 7,626 | 0,808 | 1,567 |

<!-- Estadísticas: 19 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-2 -->


vientos. Mediciones sector ITI. .............................................................................................. 27

Tabla 4-3: Valores estadísticos de las componentes ortogonales de la intensidad del viento.

<!-- INICIO TABLA 4-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|28| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-3: Valores estadísticos de las componentes ortogonales de la intensidad del****

| Valores | Componente U | Componente V |
| --- | --- | --- |
| **Promedio (m/s)** | 0,381 | 0,497 |
| **Desviación estándar (m/s)** | 0,498 | 0,792 |
| **Máximo (m/s)** | 2,045 | 2,779 |
| **Mínimo (m/s)** | -2,692 | -3,866 |
| **Porcentaje de participación (%)** | 33,166 | 66,834 |

<!-- Estadísticas: 5 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Fuente: Ecotecnos, 2021. **Gráfico 4-6: Valores centrados de las componentes ortogonales junto a su** -->
<!-- FIN TABLA 4-3 -->


Mediciones sector ITI. ........................................................................................................... 28

Tabla 4-4: Tabla de incidencia del viento, enero. Mediciones sector ITI................................ 32

<!-- INICIO TABLA 4-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|32| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-4: Tabla de incidencia del viento, enero. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 2,487 | 0,269 | - | - | - | - | 2,755 |
| **NNE** | - | 3,439 | 0,190 | - | - | - | - | 3,629 |
| **NE** | - | 1,098 | 0,011 | - | - | - | - | 1,109 |
| **ENE** | - | 0,717 | - | - | - | - | - | 0,717 |
| **E ** | - | 0,437 | - | - | - | - | - | 0,437 |
| **ESE** | - | 0,403 | - | - | - | - | - | 0,403 |
| **SE** | - | 0,302 | - | - | - | - | - | 0,302 |
| **SSE** | - | 0,370 | 0,011 | - | - | - | - | 0,381 |
| **S ** | - | 1,221 | - | - | - | - | - | 1,221 |
| **SSW** | - | 25,045 | 7,012 | - | - | - | - | 32,056 |
| **SW** | - | 12,903 | 1,501 | - | - | - | - | 14,404 |
| **WSW** | - | 1,770 | - | - | - | - | - | 1,770 |
| **W ** | - | 1,949 | 0,011 | - | - | - | - | 1,960 |
| **WNW** | - | 2,195 | - | - | - | - | - | 2,195 |
| **NW** | - | 3,024 | 0,011 | - | - | - | - | 3,035 |
| **NNW** | - | 2,173 | 0,134 | - | - | - | - | 2,307 |
| **Calmas** | 31,317 | - | - | - | - | - | - | 31,317 |
| **Sub Total**<br>**(%)**<br> | 31,317<br> | 59,532<br> | 9,151<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 8.928 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-4 -->


Tabla 4-5: Tabla de incidencia del viento, febrero. Mediciones sector ITI. ............................ 33

<!-- INICIO TABLA 4-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|33| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-5: Tabla de incidencia del viento, febrero. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 1,474 | 0,480 | 0,056 | - | - | - | 2,010 |
| **NNE** | - | 1,938 | 0,056 | - | - | - | - | 1,994 |
| **NE** | - | 1,610 | 0,024 | - | - | - | - | 1,634 |
| **ENE** | - | 1,177 | 0,016 | - | - | - | - | 1,193 |
| **E ** | - | 0,480 | - | - | - | - | - | 0,480 |
| **ESE** | - | 0,232 | - | - | - | - | - | 0,232 |
| **SE** | - | 0,304 | - | - | - | - | - | 0,304 |
| **SSE** | - | 0,569 | 0,024 | - | - | - | - | 0,593 |
| **S ** | - | 2,330 | 0,368 | - | - | - | - | 2,699 |
| **SSW** | - | 26,275 | 15,176 | 0,008 | - | - | - | 41,459 |
| **SW** | - | 10,203 | 2,306 | - | - | - | - | 12,509 |
| **WSW** | - | 1,890 | - | - | - | - | - | 1,890 |
| **W ** | - | 2,162 | 0,008 | - | - | - | - | 2,170 |
| **WNW** | - | 2,098 | 0,008 | - | - | - | - | 2,106 |
| **NW** | - | 1,850 | 0,016 | - | - | - | - | 1,866 |
| **NNW** | - | 1,321 | 0,280 | 0,032 | - | - | - | 1,634 |
| **Calmas** | 25,226 | - | - | - | - | - | - | 25,226 |
| **Sub Total**<br>**(%)**<br> | 25,226<br> | 55,914<br> | 18,764<br> | 0,096<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 12.487 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-5 -->


Tabla 4-6: Tabla de incidencia del viento, marzo. Mediciones sector ITI. .............................. 34

<!-- INICIO TABLA 4-6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|34| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-6: Tabla de incidencia del viento, marzo. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 1,098 | 0,182 | - | - | - | - | 1,280 |
| **NNE** | - | 1,556 | 0,036 | - | - | - | - | 1,593 |
| **NE** | - | 1,811 | - | - | - | - | - | 1,811 |
| **ENE** | - | 1,324 | 0,007 | - | - | - | - | 1,331 |
| **E ** | - | 0,589 | - | - | - | - | - | 0,589 |
| **ESE** | - | 0,473 | - | - | - | - | - | 0,473 |
| **SE** | - | 0,313 | - | - | - | - | - | 0,313 |
| **SSE** | - | 0,604 | 0,022 | - | - | - | - | 0,625 |
| **S ** | - | 2,480 | 0,400 | - | - | - | - | 2,880 |
| **SSW** | - | 28,689 | 13,643 | 0,007 | - | - | - | 42,339 |
| **SW** | - | 9,330 | 2,334 | - | - | - | - | 11,665 |
| **WSW** | - | 2,851 | 0,007 | - | - | - | - | 2,858 |
| **W ** | - | 2,785 | 0,036 | - | - | - | - | 2,822 |
| **WNW** | - | 1,360 | 0,007 | - | - | - | - | 1,367 |
| **NW** | - | 1,382 | 0,036 | - | - | - | - | 1,418 |
| **NNW** | - | 1,091 | 0,051 | - | - | - | - | 1,142 |
| **Calmas** | 25,496 | - | - | - | - | - | - | 25,496 |
| **Sub Total**<br>**(%)**<br> | 25,496<br> | 57,734<br> | 16,762<br> | 0,007<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 13.751 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-6 -->


Tabla 4-7: Tabla de incidencia del viento, abril. Mediciones sector ITI. ................................. 35

<!-- INICIO TABLA 4-7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|35| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-7: Tabla de incidencia del viento, abril. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 2,257 | 0,104 | - | - | - | - | 2,361 |
| **NNE** | - | 2,465 | 0,023 | - | - | - | - | 2,488 |
| **NE** | - | 1,701 | 0,012 | - | - | - | - | 1,713 |
| **ENE** | - | 1,586 | 0,185 | - | - | - | - | 1,771 |
| **E ** | - | 0,810 | - | - | - | - | - | 0,810 |
| **ESE** | - | 0,463 | - | - | - | - | - | 0,463 |
| **SE** | - | 0,556 | - | - | - | - | - | 0,556 |
| **SSE** | - | 0,845 | 0,023 | - | - | - | - | 0,868 |
| **S ** | - | 1,620 | - | - | - | - | - | 1,620 |
| **SSW** | - | 22,384 | 8,530 | - | - | - | - | 30,914 |
| **SW** | - | 13,750 | 3,576 | - | - | - | - | 17,326 |
| **WSW** | - | 2,928 | 0,012 | - | - | - | - | 2,940 |
| **W ** | - | 2,419 | 0,012 | - | - | - | - | 2,431 |
| **WNW** | - | 1,215 | - | - | - | - | - | 1,215 |
| **NW** | - | 1,238 | - | - | - | - | - | 1,238 |
| **NNW** | - | 1,424 | - | - | - | - | - | 1,424 |
| **Calmas** | 29,861 | - | - | - | - | - | - | 29,861 |
| **Sub Total**<br>**(%)**<br> | 29,861<br> | 57,662<br> | 12,477<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 8.640 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-7 -->


Tabla 4-8: Tabla de incidencia del viento, mayo. Mediciones sector ITI. ............................... 36

<!-- INICIO TABLA 4-8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|36| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-8: Tabla de incidencia del viento, mayo. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 2,632 | 0,123 | - | - | - | - | 2,755 |
| **NNE** | - | 4,772 | 0,325 | - | - | - | - | 5,096 |
| **NE** | - | 2,901 | 0,090 | - | - | - | - | 2,991 |
| **ENE** | - | 4,592 | 0,840 | - | - | - | - | 5,432 |
| **E ** | - | 1,221 | - | - | - | - | - | 1,221 |
| **ESE** | - | 0,918 | - | - | - | - | - | 0,918 |
| **SE** | - | 0,683 | 0,022 | - | - | - | - | 0,706 |
| **SSE** | - | 0,862 | - | - | - | - | - | 0,862 |
| **S ** | - | 2,419 | - | - | - | - | - | 2,419 |
| **SSW** | - | 17,596 | 3,248 | - | - | - | - | 20,845 |
| **SW** | - | 11,234 | 0,706 | - | - | - | - | 11,940 |
| **WSW** | - | 4,514 | 0,011 | - | - | - | - | 4,525 |
| **W ** | - | 5,399 | - | - | - | - | - | 5,399 |
| **WNW** | - | 2,240 | - | - | - | - | - | 2,240 |
| **NW** | - | 2,923 | - | - | - | - | - | 2,923 |
| **NNW** | - | 2,386 | 0,022 | - | - | - | - | 2,408 |
| **Calmas** | 27,319 | - | - | - | - | - | - | 27,319 |
| **Sub Total**<br>**(%)**<br> | 27,319<br> | 67,294<br> | 5,388<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 8.928 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-8 -->


Tabla 4-9: Tabla de incidencia del viento, junio. Mediciones sector ITI. ................................ 37

<!-- INICIO TABLA 4-9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|37| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-9: Tabla de incidencia del viento, junio. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 2,882 | 1,563 | - | - | - | - | 4,444 |
| **NNE** | - | 4,329 | 1,400 | 0,012 | - | - | - | 5,741 |
| **NE** | - | 2,801 | 0,359 | - | - | - | - | 3,160 |
| **ENE** | - | 3,704 | 1,157 | - | - | - | - | 4,861 |
| **E ** | - | 1,400 | 0,185 | - | - | - | - | 1,586 |
| **ESE** | - | 1,400 | 0,127 | - | - | - | - | 1,528 |
| **SE** | - | 1,100 | 0,046 | - | - | - | - | 1,146 |
| **SSE** | - | 1,134 | - | - | - | - | - | 1,134 |
| **S ** | - | 4,294 | 0,058 | - | - | - | - | 4,352 |
| **SSW** | - | 23,125 | 5,764 | - | - | - | - | 28,889 |
| **SW** | - | 9,583 | 1,539 | - | - | - | - | 11,123 |
| **WSW** | - | 1,563 | - | - | - | - | - | 1,563 |
| **W ** | - | 2,674 | - | - | - | - | - | 2,674 |
| **WNW** | - | 1,910 | - | - | - | - | - | 1,910 |
| **NW** | - | 2,813 | 0,035 | - | - | - | - | 2,847 |
| **NNW** | - | 1,968 | 0,590 | - | - | - | - | 2,558 |
| **Calmas** | 20,486 | - | - | - | - | - | - | 20,486 |
| **Sub Total**<br>**(%)**<br> | 20,486<br> | 66,678<br> | 12,824<br> | 0,012<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 8.640 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-9 -->


Tabla 4-10: Tabla de incidencia del viento, julio. Mediciones sector ITI. ............................... 38

<!-- INICIO TABLA 4-10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|38| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-10: Tabla de incidencia del viento, julio. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 4,133 | 2,666 | 0,067 | - | - | - | 6,866 |
| **NNE** | - | 5,634 | 1,893 | - | - | - | - | 7,527 |
| **NE** | - | 4,547 | 0,728 | - | - | - | - | 5,276 |
| **ENE** | - | 7,818 | 2,442 | - | - | - | - | 10,260 |
| **E ** | - | 1,803 | 0,078 | - | - | - | - | 1,882 |
| **ESE** | - | 1,736 | 0,325 | - | - | - | - | 2,061 |
| **SE** | - | 1,389 | 0,045 | - | - | - | - | 1,434 |
| **SSE** | - | 1,042 | - | - | - | - | - | 1,042 |
| **S ** | - | 1,579 | 0,011 | - | - | - | - | 1,591 |
| **SSW** | - | 13,217 | 6,944 | - | - | - | - | 20,161 |
| **SW** | - | 10,439 | 1,602 | - | - | - | - | 12,041 |
| **WSW** | - | 3,304 | 0,022 | - | - | - | - | 3,327 |
| **W ** | - | 4,010 | 0,011 | - | - | - | - | 4,021 |
| **WNW** | - | 2,016 | - | - | - | - | - | 2,016 |
| **NW** | - | 3,047 | - | - | - | - | - | 3,047 |
| **NNW** | - | 3,170 | 0,358 | - | - | - | - | 3,528 |
| **Calmas** | 13,922 | - | - | - | - | - | - | 13,922 |
| **Sub Total**<br>**(%)**<br> | 13,922<br> | 68,884<br> | 17,126<br> | 0,067<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 8.928 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-10 -->


Tabla 4-11: Tabla de incidencia del viento, agosto. Mediciones sector ITI. ........................... 39

<!-- INICIO TABLA 4-11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|39| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-11: Tabla de incidencia del viento, agosto. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 2,531 | 0,762 | - | - | - | - | 3,293 |
| **NNE** | - | 3,629 | 0,403 | - | - | - | - | 4,032 |
| **NE** | - | 3,483 | 0,246 | - | - | - | - | 3,730 |
| **ENE** | - | 4,402 | 0,750 | - | - | - | - | 5,152 |
| **E ** | - | 0,784 | 0,011 | - | - | - | - | 0,795 |
| **ESE** | - | 0,952 | 0,078 | - | - | - | - | 1,030 |
| **SE** | - | 0,795 | 0,011 | - | - | - | - | 0,806 |
| **SSE** | - | 0,661 | 0,034 | - | - | - | - | 0,694 |
| **S ** | - | 2,039 | 0,146 | - | - | - | - | 2,184 |
| **SSW** | - | 19,366 | 6,149 | - | - | - | - | 25,515 |
| **SW** | - | 16,140 | 10,506 | 0,022 | - | - | - | 26,669 |
| **WSW** | - | 5,018 | 0,190 | - | - | - | - | 5,208 |
| **W ** | - | 3,024 | 0,056 | - | - | - | - | 3,080 |
| **WNW** | - | 1,378 | - | - | - | - | - | 1,378 |
| **NW** | - | 1,613 | 0,034 | - | - | - | - | 1,647 |
| **NNW** | - | 1,478 | 0,168 | - | - | - | - | 1,647 |
| **Calmas** | 13,138 | - | - | - | - | - | - | 13,138 |
| **Sub Total**<br>**(%)**<br> | 13,138<br> | 67,294<br> | 19,545<br> | 0,022<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 8.928 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-11 -->


Tabla 4-12: Tabla de incidencia del viento, septiembre. Mediciones sector ITI. .................... 40

<!-- INICIO TABLA 4-12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|40| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-12: Tabla de incidencia del viento, septiembre. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 2,523 | 0,405 | - | - | - | - | 2,928 |
| **NNE** | - | 2,477 | 0,336 | - | - | - | - | 2,813 |
| **NE** | - | 1,632 | 0,139 | - | - | - | - | 1,771 |
| **ENE** | - | 1,806 | 0,127 | - | - | - | - | 1,933 |
| **E ** | - | 0,313 | - | - | - | - | - | 0,313 |
| **ESE** | - | 0,266 | - | - | - | - | - | 0,266 |
| **SE** | - | 0,301 | - | - | - | - | - | 0,301 |
| **SSE** | - | 0,417 | - | - | - | - | - | 0,417 |
| **S ** | - | 1,644 | 0,012 | - | - | - | - | 1,655 |
| **SSW** | - | 27,558 | 7,118 | - | - | - | - | 34,676 |
| **SW** | - | 16,296 | 4,954 | - | - | - | - | 21,250 |
| **WSW** | - | 3,380 | 0,012 | - | - | - | - | 3,391 |
| **W ** | - | 4,456 | 0,035 | - | - | - | - | 4,491 |
| **WNW** | - | 3,715 | - | - | - | - | - | 3,715 |
| **NW** | - | 3,079 | - | - | - | - | - | 3,079 |
| **NNW** | - | 2,569 | 0,012 | - | - | - | - | 2,581 |
| **Calmas** | 14,421 | - | - | - | - | - | - | 14,421 |
| **Sub Total**<br>**(%)**<br> | 14,421<br> | 72,431<br> | 13,148<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 8.640 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-12 -->


Tabla 4-13: Tabla de incidencia del viento, octubre. Mediciones sector ITI. .......................... 41

<!-- INICIO TABLA 4-13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|41| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-13: Tabla de incidencia del viento, octubre. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 1,815 | 0,582 | 0,112 | - | - | - | 2,509 |
| **NNE** | - | 2,576 | 0,482 | 0,011 | - | - | - | 3,069 |
| **NE** | - | 1,546 | 0,190 | - | - | - | - | 1,736 |
| **ENE** | - | 1,378 | 0,011 | - | - | - | - | 1,389 |
| **E ** | - | 0,482 | - | - | - | - | - | 0,482 |
| **ESE** | - | 0,459 | 0,011 | - | - | - | - | 0,470 |
| **SE** | - | 0,336 | - | - | - | - | - | 0,336 |
| **SSE** | - | 0,426 | - | - | - | - | - | 0,426 |
| **S ** | - | 1,019 | - | - | - | - | - | 1,019 |
| **SSW** | - | 30,354 | 3,685 | - | - | - | - | 34,039 |
| **SW** | - | 19,881 | 6,732 | - | - | - | - | 26,613 |
| **WSW** | - | 1,669 | 0,022 | - | - | - | - | 1,691 |
| **W ** | - | 1,927 | 0,034 | - | - | - | - | 1,960 |
| **WNW** | - | 2,610 | - | - | - | - | - | 2,610 |
| **NW** | - | 1,792 | 0,022 | - | - | - | - | 1,815 |
| **NNW** | - | 1,322 | 0,202 | - | - | - | - | 1,523 |
| **Calmas** | 18,313 | - | - | - | - | - | - | 18,313 |
| **Sub Total**<br>**(%)**<br> | 18,313<br> | 69,590<br> | 11,974<br> | 0,123<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 8.928 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-13 -->


Tabla 4-14: Tabla de incidencia del viento, noviembre. Mediciones sector ITI. ..................... 42

<!-- INICIO TABLA 4-14 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|42| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-14: Tabla de incidencia del viento, noviembre. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 2,512 | 1,065 | - | - | - | - | 3,576 |
| **NNE** | - | 3,345 | 1,169 | - | - | - | - | 4,514 |
| **NE** | - | 1,493 | 0,035 | - | - | - | - | 1,528 |
| **ENE** | - | 0,949 | - | - | - | - | - | 0,949 |
| **E ** | - | 0,278 | - | - | - | - | - | 0,278 |
| **ESE** | - | 0,266 | - | - | - | - | - | 0,266 |
| **SE** | - | 0,440 | - | - | - | - | - | 0,440 |
| **SSE** | - | 0,197 | - | - | - | - | - | 0,197 |
| **S ** | - | 0,440 | - | - | - | - | - | 0,440 |
| **SSW** | - | 23,600 | 6,829 | - | - | - | - | 30,428 |
| **SW** | - | 19,109 | 5,984 | - | - | - | - | 25,093 |
| **WSW** | - | 2,326 | - | - | - | - | - | 2,326 |
| **W ** | - | 2,292 | - | - | - | - | - | 2,292 |
| **WNW** | - | 2,141 | 0,023 | - | - | - | - | 2,164 |
| **NW** | - | 2,280 | 0,012 | - | - | - | - | 2,292 |
| **NNW** | - | 1,563 | 0,023 | - | - | - | - | 1,586 |
| **Calmas** | 21,632 | - | - | - | - | - | - | 21,632 |
| **Sub Total**<br>**(%)**<br> | 21,632<br> | 63,229<br> | 15,139<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 8.640 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-14 -->


Tabla 4-15: Tabla de incidencia del viento, diciembre. Mediciones sector ITI. ...................... 43

<!-- INICIO TABLA 4-15 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|43| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-15: Tabla de incidencia del viento, diciembre. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 1,019 | 0,235 | - | - | - | - | 1,254 |
| **NNE** | - | 0,907 | 0,045 | - | - | - | - | 0,952 |
| **NE** | - | 0,717 | - | - | - | - | - | 0,717 |
| **ENE** | - | 0,515 | - | - | - | - | - | 0,515 |
| **E ** | - | 0,157 | - | - | - | - | - | 0,157 |
| **ESE** | - | 0,258 | - | - | - | - | - | 0,258 |
| **SE** | - | 0,459 | - | - | - | - | - | 0,459 |
| **SSE** | - | 0,370 | - | - | - | - | - | 0,370 |
| **S ** | - | 2,151 | - | - | - | - | - | 2,151 |
| **SSW** | - | 30,869 | 10,484 | - | - | - | - | 41,353 |
| **SW** | - | 13,441 | 6,463 | - | - | - | - | 19,904 |
| **WSW** | - | 1,915 | 0,045 | - | - | - | - | 1,960 |
| **W ** | - | 1,344 | 0,011 | - | - | - | - | 1,355 |
| **WNW** | - | 1,299 | - | - | - | - | - | 1,299 |
| **NW** | - | 1,591 | 0,011 | - | - | - | - | 1,602 |
| **NNW** | - | 1,042 | 0,213 | - | - | - | - | 1,254 |
| **Calmas** | 24,440 | - | - | - | - | - | - | 24,440 |
| **Sub Total**<br>**(%)**<br> | 24,440<br> | 58,053<br> | 17,507<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 8.928 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-15 -->


Tabla 4-16: Intensidades máxima globales y por dirección de procedencia de los vientos, entre

<!-- INICIO TABLA 4-16 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|51| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-16: Intensidades máxima globales y por dirección de procedencia de los vientos, entre los meses enero-junio.****

| Col1 | Intensidad máxima del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Meses** | **Enero** | **Enero** | **Febrero** | **Febrero** | **Marzo** | **Marzo** | **Abril** | **Abril** | **Mayo** | **Mayo** | **Junio** | **Junio** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N ** | 1,773 | 3,440 | 3,931 | 7,626 | 2,158 | 4,187 | 1,570 | 3,046 | 1,773 | 3,440 | 2,755 | 5,345 |
| **NNE** | 1,965 | 3,812 | 2,553 | 4,953 | 1,773 | 3,440 | 1,570 | 3,046 | 2,158 | 4,187 | 3,141 | 6,094 |
| **NE** | 1,570 | 3,046 | 2,158 | 4,187 | 1,175 | 2,280 | 1,570 | 3,046 | 1,773 | 3,440 | 2,158 | 4,187 |
| **ENE** | 0,588 | 1,141 | 1,570 | 3,046 | 1,570 | 3,046 | 1,965 | 3,812 | 2,948 | 5,719 | 2,948 | 5,719 |
| **E ** | 0,790 | 1,533 | 1,175 | 2,280 | 0,983 | 1,907 | 1,378 | 2,673 | 1,175 | 2,280 | 2,360 | 4,578 |
| **ESE** | 0,588 | 1,141 | 1,175 | 2,280 | 1,175 | 2,280 | 0,790 | 1,533 | 1,378 | 2,673 | 2,158 | 4,187 |
| **SE** | 0,983 | 1,907 | 0,983 | 1,907 | 0,983 | 1,907 | 1,175 | 2,280 | 1,570 | 3,046 | 2,158 | 4,187 |
| **SSE** | 1,570 | 3,046 | 2,360 | 4,578 | 1,773 | 3,440 | 1,570 | 3,046 | 1,175 | 2,280 | 1,378 | 2,673 |
| **S ** | 1,175 | 2,280 | 2,360 | 4,578 | 2,755 | 5,345 | 1,378 | 2,673 | 1,378 | 2,673 | 1,570 | 3,046 |
| **SSW** | 2,553 | 4,953 | 3,141 | 6,094 | 3,141 | 6,094 | 2,755 | 5,345 | 2,553 | 4,953 | 2,553 | 4,953 |
| **SW** | 2,553 | 4,953 | 2,755 | 5,345 | 2,948 | 5,719 | 2,948 | 5,719 | 2,360 | 4,578 | 2,158 | 4,187 |
| **WSW** | 1,175 | 2,280 | 1,175 | 2,280 | 1,773 | 3,440 | 1,570 | 3,046 | 1,570 | 3,046 | 1,378 | 2,673 |
| **W ** | 1,570 | 3,046 | 1,570 | 3,046 | 1,570 | 3,046 | 1,570 | 3,046 | 1,378 | 2,673 | 1,175 | 2,280 |
| **WNW** | 1,378 | 2,673 | 1,570 | 3,046 | 1,570 | 3,046 | 1,175 | 2,280 | 1,378 | 2,673 | 1,175 | 2,280 |
| **NW** | 1,570 | 3,046 | 1,773 | 3,440 | 1,965 | 3,812 | 1,378 | 2,673 | 1,378 | 2,673 | 1,965 | 3,812 |
| **NNW** | 1,773 | 3,440 | 3,536 | 6,860 | 1,965 | 3,812 | 1,378 | 2,673 | 1,570 | 3,046 | 2,553 | 4,953 |
| **Global** | 2,553 | 4,953 | 3,931 | 7,626 | 3,141 | 6,094 | 2,948 | 5,719 | 2,948 | 5,719 | 3,141 | 6,094 |

<!-- Estadísticas: 19 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-16 -->

los meses enero-junio. Mediciones sector ITI. ...................................................................... 51

Tabla 4-17: Intensidades máxima globales y por dirección de procedencia de los vientos, entre

<!-- INICIO TABLA 4-17 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|52| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-17: Intensidades máxima globales y por dirección de procedencia de los vientos, entre los meses julio-diciembre.****

| Col1 | Intensidad máxima del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Meses** | **Julio** | **Julio** | **Agosto** | **Agosto** | **Septiembre** | **Septiembre** | **Octubre** | **Octubre** | **Noviembre** | **Noviembre** | **Diciembre** | **Diciembre** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N ** | 3,343 | 6,485 | 2,360 | 4,578 | 1,965 | 3,812 | 3,728 | 7,232 | 2,553 | 4,953 | 2,158 | 4,187 |
| **NNE** | 2,948 | 5,719 | 2,553 | 4,953 | 1,965 | 3,812 | 3,141 | 6,094 | 2,755 | 5,345 | 2,158 | 4,187 |
| **NE** | 2,553 | 4,953 | 2,553 | 4,953 | 1,570 | 3,046 | 1,965 | 3,812 | 1,570 | 3,046 | 1,175 | 2,280 |
| **ENE** | 2,553 | 4,953 | 2,755 | 5,345 | 1,570 | 3,046 | 1,570 | 3,046 | 0,790 | 1,533 | 0,790 | 1,533 |
| **E ** | 2,553 | 4,953 | 1,570 | 3,046 | 0,983 | 1,907 | 0,983 | 1,907 | 0,790 | 1,533 | 0,395 | 0,766 |
| **ESE** | 2,553 | 4,953 | 1,965 | 3,812 | 1,175 | 2,280 | 1,570 | 3,046 | 0,983 | 1,907 | 1,378 | 2,673 |
| **SE** | 2,158 | 4,187 | 1,773 | 3,440 | 1,175 | 2,280 | 1,175 | 2,280 | 1,175 | 2,280 | 1,378 | 2,673 |
| **SSE** | 1,378 | 2,673 | 2,755 | 5,345 | 1,378 | 2,673 | 1,378 | 2,673 | 0,983 | 1,907 | 1,175 | 2,280 |
| **S ** | 1,570 | 3,046 | 2,360 | 4,578 | 1,570 | 3,046 | 0,983 | 1,907 | 0,983 | 1,907 | 1,378 | 2,673 |
| **SSW** | 2,553 | 4,953 | 2,553 | 4,953 | 2,755 | 5,345 | 2,553 | 4,953 | 2,360 | 4,578 | 2,360 | 4,578 |
| **SW** | 2,755 | 5,345 | 3,141 | 6,094 | 2,755 | 5,345 | 2,553 | 4,953 | 2,948 | 5,719 | 2,755 | 5,345 |
| **WSW** | 1,570 | 3,046 | 2,360 | 4,578 | 1,570 | 3,046 | 1,570 | 3,046 | 1,378 | 2,673 | 1,773 | 3,440 |
| **W ** | 1,570 | 3,046 | 1,773 | 3,440 | 1,773 | 3,440 | 1,570 | 3,046 | 1,378 | 2,673 | 1,570 | 3,046 |
| **WNW** | 1,175 | 2,280 | 1,175 | 2,280 | 1,378 | 2,673 | 1,378 | 2,673 | 1,570 | 3,046 | 1,378 | 2,673 |
| **NW** | 1,175 | 2,280 | 1,570 | 3,046 | 1,378 | 2,673 | 1,570 | 3,046 | 1,570 | 3,046 | 1,570 | 3,046 |
| **NNW** | 2,553 | 4,953 | 2,360 | 4,578 | 1,570 | 3,046 | 2,360 | 4,578 | 1,773 | 3,440 | 2,360 | 4,578 |
| **Global** | 3,343 | 6,485 | 3,141 | 6,094 | 2,755 | 5,345 | 3,728 | 7,232 | 2,948 | 5,719 | 2,755 | 5,345 |

<!-- Estadísticas: 19 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-17 -->

los meses julio-diciembre. Mediciones sector ITI. ................................................................. 52

Tabla 4-18: Intensidades promedio globales y por dirección de procedencia de los vientos,

<!-- INICIO TABLA 4-18 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|53| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-18: Intensidades promedio globales y por dirección de procedencia de los vientos, entre los meses enero-junio.****

| Col1 | Intensidad promedio del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Meses** | **Enero** | **Enero** | **Febrero** | **Febrero** | **Marzo** | **Marzo** | **Abril** | **Abril** | **Mayo** | **Mayo** | **Junio** | **Junio** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N ** | 0,866 | 1,681 | 1,116 | 2,164 | 0,829 | 1,608 | 0,839 | 1,628 | 0,872 | 1,692 | 1,242 | 2,409 |
| **NNE** | 0,767 | 1,488 | 0,746 | 1,448 | 0,647 | 1,255 | 0,710 | 1,377 | 0,832 | 1,614 | 1,150 | 2,230 |
| **NE** | 0,526 | 1,020 | 0,562 | 1,091 | 0,532 | 1,032 | 0,671 | 1,303 | 0,732 | 1,419 | 0,882 | 1,712 |
| **ENE** | 0,464 | 0,901 | 0,537 | 1,041 | 0,558 | 1,083 | 0,774 | 1,501 | 0,955 | 1,853 | 1,069 | 2,074 |
| **E ** | 0,485 | 0,940 | 0,506 | 0,981 | 0,491 | 0,953 | 0,535 | 1,037 | 0,560 | 1,086 | 0,818 | 1,588 |
| **ESE** | 0,449 | 0,870 | 0,469 | 0,910 | 0,557 | 1,080 | 0,453 | 0,879 | 0,624 | 1,211 | 0,803 | 1,558 |
| **SE** | 0,453 | 0,879 | 0,487 | 0,945 | 0,481 | 0,933 | 0,497 | 0,964 | 0,610 | 1,183 | 0,710 | 1,376 |
| **SSE** | 0,544 | 1,056 | 0,633 | 1,229 | 0,648 | 1,256 | 0,614 | 1,191 | 0,565 | 1,096 | 0,657 | 1,274 |
| **S ** | 0,594 | 1,152 | 0,938 | 1,820 | 0,882 | 1,710 | 0,557 | 1,080 | 0,587 | 1,139 | 0,721 | 1,399 |
| **SSW** | 1,106 | 2,145 | 1,267 | 2,459 | 1,221 | 2,370 | 1,147 | 2,225 | 1,012 | 1,963 | 1,074 | 2,084 |
| **SW** | 0,952 | 1,847 | 1,022 | 1,982 | 1,045 | 2,027 | 1,090 | 2,114 | 0,885 | 1,717 | 0,988 | 1,917 |
| **WSW** | 0,555 | 1,076 | 0,612 | 1,188 | 0,727 | 1,411 | 0,762 | 1,479 | 0,739 | 1,434 | 0,596 | 1,157 |
| **W ** | 0,670 | 1,300 | 0,686 | 1,331 | 0,756 | 1,467 | 0,775 | 1,503 | 0,799 | 1,551 | 0,704 | 1,365 |
| **WNW** | 0,719 | 1,394 | 0,775 | 1,504 | 0,676 | 1,312 | 0,621 | 1,204 | 0,670 | 1,300 | 0,607 | 1,178 |
| **NW** | 0,729 | 1,413 | 0,748 | 1,451 | 0,684 | 1,327 | 0,675 | 1,310 | 0,713 | 1,382 | 0,731 | 1,419 |
| **NNW** | 0,859 | 1,666 | 1,011 | 1,962 | 0,778 | 1,509 | 0,811 | 1,573 | 0,810 | 1,572 | 1,079 | 2,093 |
| **Global** | 0,675 | 1,310 | 0,837 | 1,624 | 0,806 | 1,563 | 0,723 | 1,403 | 0,653 | 1,266 | 0,803 | 1,558 |

<!-- Estadísticas: 19 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-18 -->

entre los meses enero-junio. Mediciones sector ITI. ............................................................. 53

Tabla 4-19: Intensidades promedio globales y por dirección de procedencia de los vientos,

<!-- INICIO TABLA 4-19 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|54| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-19: Intensidades promedio globales y por dirección de procedencia de los vientos, entre los meses julio-diciembre.****

| Col1 | Intensidad promedio del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Meses** | **Julio** | **Julio** | **Agosto** | **Agosto** | **Septiembre** | **Septiembre** | **Octubre** | **Octubre** | **Noviembre** | **Noviembre** | **Diciembre** | **Diciembre** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N ** | 1,359 | 2,636 | 1,059 | 2,055 | 1,012 | 1,964 | 1,251 | 2,427 | 1,234 | 2,394 | 0,927 | 1,799 |
| **NNE** | 1,171 | 2,272 | 0,914 | 1,773 | 0,986 | 1,913 | 0,993 | 1,926 | 1,182 | 2,293 | 0,713 | 1,383 |
| **NE** | 0,931 | 1,806 | 0,812 | 1,575 | 0,808 | 1,568 | 0,797 | 1,546 | 0,630 | 1,223 | 0,545 | 1,057 |
| **ENE** | 1,105 | 2,143 | 0,927 | 1,798 | 0,816 | 1,583 | 0,668 | 1,296 | 0,505 | 0,979 | 0,514 | 0,997 |
| **E ** | 0,707 | 1,372 | 0,762 | 1,478 | 0,511 | 0,991 | 0,558 | 1,083 | 0,460 | 0,893 | 0,395 | 0,766 |
| **ESE** | 0,883 | 1,713 | 0,874 | 1,696 | 0,693 | 1,343 | 0,745 | 1,446 | 0,633 | 1,229 | 0,643 | 1,247 |
| **SE** | 0,708 | 1,374 | 0,721 | 1,399 | 0,620 | 1,203 | 0,558 | 1,082 | 0,601 | 1,166 | 0,562 | 1,090 |
| **SSE** | 0,635 | 1,232 | 0,666 | 1,293 | 0,651 | 1,262 | 0,554 | 1,075 | 0,580 | 1,125 | 0,495 | 0,961 |
| **S ** | 0,687 | 1,333 | 0,791 | 1,535 | 0,596 | 1,156 | 0,506 | 0,982 | 0,565 | 1,096 | 0,647 | 1,254 |
| **SSW** | 1,237 | 2,399 | 1,126 | 2,185 | 1,066 | 2,068 | 0,933 | 1,809 | 1,081 | 2,098 | 1,122 | 2,176 |
| **SW** | 1,029 | 1,996 | 1,330 | 2,580 | 1,066 | 2,069 | 1,115 | 2,164 | 1,128 | 2,188 | 1,181 | 2,291 |
| **WSW** | 0,709 | 1,376 | 0,822 | 1,595 | 0,582 | 1,129 | 0,643 | 1,247 | 0,652 | 1,266 | 0,686 | 1,331 |
| **W ** | 0,785 | 1,522 | 0,768 | 1,489 | 0,748 | 1,452 | 0,712 | 1,381 | 0,776 | 1,506 | 0,795 | 1,543 |
| **WNW** | 0,646 | 1,254 | 0,568 | 1,101 | 0,710 | 1,377 | 0,831 | 1,612 | 0,839 | 1,627 | 0,836 | 1,621 |
| **NW** | 0,672 | 1,304 | 0,702 | 1,363 | 0,750 | 1,455 | 0,803 | 1,558 | 0,830 | 1,611 | 0,890 | 1,727 |
| **NNW** | 0,891 | 1,729 | 0,847 | 1,642 | 0,802 | 1,556 | 0,887 | 1,720 | 0,778 | 1,510 | 1,013 | 1,965 |
| **Global** | 0,913 | 1,771 | 0,950 | 1,843 | 0,845 | 1,639 | 0,810 | 1,572 | 0,836 | 1,622 | 0,829 | 1,608 |

<!-- Estadísticas: 19 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-19 -->

entre los meses julio-diciembre. Mediciones sector ITI. ........................................................ 54

Tabla 4-20: Tabla de incidencia del viento, verano promedio. Mediciones sector ITI. ........... 56

<!-- INICIO TABLA 4-20 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|56| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-20: Tabla de incidencia del viento, verano promedio. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N** | - | 1,613 | 0,310 | 0,020 | - | - | - | 1,943 |
| **NNE** | - | 2,182 | 0,082 | - | - | - | - | 2,264 |
| **NE** | - | 1,576 | 0,011 | - | - | - | - | 1,587 |
| **ENE** | - | 1,107 | 0,009 | - | - | - | - | 1,115 |
| **E** | - | 0,481 | - | - | - | - | - | 0,481 |
| **ESE** | - | 0,361 | - | - | - | - | - | 0,361 |
| **SE** | - | 0,336 | - | - | - | - | - | 0,336 |
| **SSE** | - | 0,518 | 0,011 | - | - | - | - | 0,529 |
| **S** | - | 2,105 | 0,287 | - | - | - | - | 2,392 |
| **SSW** | - | 26,818 | 12,724 | 0,006 | - | - | - | 39,548 |
| **SW** | - | 10,451 | 2,259 | - | - | - | - | 12,709 |
| **WSW** | - | 2,224 | 0,009 | - | - | - | - | 2,233 |
| **W** | - | 2,187 | 0,020 | - | - | - | - | 2,207 |
| **WNW** | - | 1,863 | 0,003 | - | - | - | - | 1,866 |
| **NW** | - | 1,988 | 0,023 | - | - | - | - | 2,011 |
| **NNW** | - | 1,468 | 0,154 | 0,011 | - | - | - | 1,633 |
| **Calmas** | 26,784 | - | - | - | - | - | - | 26,784 |
| **Sub Total**<br>**(%)** <br> | 26,784<br> | 57,278<br> | 15,901<br> | 0,037<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 35.155 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-20 -->


Tabla 4-21: Tabla de incidencia del viento, otoño promedio. Mediciones sector ITI. ............. 57

<!-- INICIO TABLA 4-21 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|57| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-21: Tabla de incidencia del viento, otoño promedio. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N** | - | 2,345 | 0,510 | - | - | - | - | 2,854 |
| **NNE** | - | 3,274 | 0,468 | 0,004 | - | - | - | 3,746 |
| **NE** | - | 1,933 | 0,091 | - | - | - | - | 2,024 |
| **ENE** | - | 2,560 | 0,517 | - | - | - | - | 3,077 |
| **E** | - | 0,997 | 0,060 | - | - | - | - | 1,057 |
| **ESE** | - | 0,695 | 0,019 | - | - | - | - | 0,714 |
| **SE** | - | 0,653 | 0,023 | - | - | - | - | 0,676 |
| **SSE** | - | 0,921 | 0,019 | - | - | - | - | 0,940 |
| **S** | - | 2,851 | 0,019 | - | - | - | - | 2,870 |
| **SSW** | - | 22,907 | 6,483 | - | - | - | - | 29,390 |
| **SW** | - | 11,999 | 2,375 | - | - | - | - | 14,374 |
| **WSW** | - | 2,922 | 0,008 | - | - | - | - | 2,930 |
| **W** | - | 3,311 | 0,004 | - | - | - | - | 3,315 |
| **WNW** | - | 1,461 | 0,004 | - | - | - | - | 1,465 |
| **NW** | - | 1,899 | 0,011 | - | - | - | - | 1,911 |
| **NNW** | - | 1,729 | 0,185 | - | - | - | - | 1,914 |
| **Calmas** | 26,743 | - | - | - | - | - | - | 26,743 |
| **Sub Total**<br>**(%)** <br> | 26,743<br> | 62,458<br> | 10,795<br> | 0,004<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 26.485 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-21 -->


Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|5|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Tabla 4-22: Tabla de incidencia del viento, invierno promedio. Mediciones sector ITI........... 58

<!-- INICIO TABLA 4-22 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|58| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-22: Tabla de incidencia del viento, invierno promedio. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N** | - | 3,111 | 1,299 | 0,023 | - | - | - | 4,433 |
| **NNE** | - | 4,372 | 0,982 | - | - | - | - | 5,354 |
| **NE** | - | 3,685 | 0,430 | - | - | - | - | 4,116 |
| **ENE** | - | 5,354 | 1,318 | - | - | - | - | 6,672 |
| **E** | - | 1,174 | 0,030 | - | - | - | - | 1,204 |
| **ESE** | - | 1,246 | 0,159 | - | - | - | - | 1,405 |
| **SE** | - | 0,955 | 0,019 | - | - | - | - | 0,974 |
| **SSE** | - | 0,793 | 0,011 | - | - | - | - | 0,804 |
| **S** | - | 1,790 | 0,057 | - | - | - | - | 1,846 |
| **SSW** | - | 19,064 | 6,366 | - | - | - | - | 25,429 |
| **SW** | - | 13,140 | 5,048 | 0,008 | - | - | - | 18,195 |
| **WSW** | - | 3,625 | 0,076 | - | - | - | - | 3,700 |
| **W** | - | 3,866 | 0,034 | - | - | - | - | 3,900 |
| **WNW** | - | 2,443 | - | - | - | - | - | 2,443 |
| **NW** | - | 2,745 | 0,011 | - | - | - | - | 2,756 |
| **NNW** | - | 2,330 | 0,193 | - | - | - | - | 2,522 |
| **Calmas** | 14,246 | - | - | - | - | - | - | 14,246 |
| **Sub Total**<br>**(%)** <br> | 14,246<br> | 69,692<br> | 16,032<br> | 0,030<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 26.485 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-22 -->


Tabla 4-23: Tabla de incidencia del viento, primavera promedio. Mediciones sector ITI. ...... 59

<!-- INICIO TABLA 4-23 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|59| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-23: Tabla de incidencia del viento, primavera promedio. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N** | - | 1,935 | 0,695 | 0,038 | - | - | - | 2,668 |
| **NNE** | - | 2,382 | 0,573 | 0,004 | - | - | - | 2,958 |
| **NE** | - | 1,305 | 0,080 | - | - | - | - | 1,386 |
| **ENE** | - | 1,038 | 0,008 | - | - | - | - | 1,046 |
| **E** | - | 0,286 | - | - | - | - | - | 0,286 |
| **ESE** | - | 0,313 | 0,004 | - | - | - | - | 0,317 |
| **SE** | - | 0,374 | - | - | - | - | - | 0,374 |
| **SSE** | - | 0,286 | - | - | - | - | - | 0,286 |
| **S** | - | 1,088 | - | - | - | - | - | 1,088 |
| **SSW** | - | 27,469 | 6,432 | - | - | - | - | 33,901 |
| **SW** | - | 18,281 | 6,459 | - | - | - | - | 24,739 |
| **WSW** | - | 2,355 | 0,015 | - | - | - | - | 2,371 |
| **W** | - | 2,222 | 0,015 | - | - | - | - | 2,237 |
| **WNW** | - | 2,229 | 0,008 | - | - | - | - | 2,237 |
| **NW** | - | 2,111 | 0,015 | - | - | - | - | 2,126 |
| **NNW** | - | 1,554 | 0,153 | - | - | - | - | 1,706 |
| **Calmas** | 20,273 | - | - | - | - | - | - | 20,273 |
| **Sub Total**<br>**(%)** <br> | 20,273<br> | 65,229<br> | 14,456<br> | 0,042<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 26.197 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-23 -->


Tabla 4-24: Intensidades máxima globales y por dirección de procedencia de los vientos, por

<!-- INICIO TABLA 4-24 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|63| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-24: Intensidades máxima globales y por dirección de procedencia de los****

| Col1 | Intensidad máxima del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Estaciones** | **Verano** | **Verano** | **Otoño** | **Otoño** | **Invierno** | **Invierno** | **Primavera** | **Primavera** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N** | 3,931 | 7,626 | 2,755 | 5,345 | 3,343 | 6,485 | 3,728 | 7,232 |
| **NNE** | 2,553 | 4,953 | 3,141 | 6,094 | 2,948 | 5,719 | 3,141 | 6,094 |
| **NE** | 2,158 | 4,187 | 2,158 | 4,187 | 2,553 | 4,953 | 1,965 | 3,812 |
| **ENE** | 1,570 | 3,046 | 2,948 | 5,719 | 2,755 | 5,345 | 1,570 | 3,046 |
| **E** | 1,175 | 2,280 | 2,360 | 4,578 | 2,553 | 4,953 | 0,983 | 1,907 |
| **ESE** | 1,175 | 2,280 | 2,158 | 4,187 | 2,553 | 4,953 | 1,570 | 3,046 |
| **SE** | 1,378 | 2,673 | 2,158 | 4,187 | 2,158 | 4,187 | 1,175 | 2,280 |
| **SSE** | 2,360 | 4,578 | 1,773 | 3,440 | 2,755 | 5,345 | 1,378 | 2,673 |
| **S** | 2,755 | 5,345 | 1,570 | 3,046 | 2,360 | 4,578 | 1,378 | 2,673 |
| **SSW** | 3,141 | 6,094 | 2,948 | 5,719 | 2,553 | 4,953 | 2,755 | 5,345 |
| **SW** | 2,948 | 5,719 | 2,948 | 5,719 | 3,141 | 6,094 | 2,948 | 5,719 |
| **WSW** | 1,773 | 3,440 | 1,570 | 3,046 | 2,360 | 4,578 | 1,773 | 3,440 |
| **W** | 1,570 | 3,046 | 1,570 | 3,046 | 1,773 | 3,440 | 1,570 | 3,046 |
| **WNW** | 1,570 | 3,046 | 1,570 | 3,046 | 1,378 | 2,673 | 1,570 | 3,046 |
| **NW** | 1,965 | 3,812 | 1,965 | 3,812 | 1,570 | 3,046 | 1,570 | 3,046 |
| **NNW** | 3,536 | 6,860 | 2,553 | 4,953 | 2,553 | 4,953 | 2,360 | 4,578 |
| **Global** | 3,931 | 7,626 | 3,141 | 6,094 | 3,343 | 6,485 | 3,728 | 7,232 |

<!-- Estadísticas: 19 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-24 -->


estaciones. Mediciones sector ITI. ........................................................................................ 63

Tabla 4-25: Intensidades promedio globales y por dirección de procedencia de los vientos, por

<!-- INICIO TABLA 4-25 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|64| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-25: Intensidades promedio globales y por dirección de procedencia de los****

| Col1 | Intensidad promedio del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Estaciones** | **Verano** | **Verano** | **Otoño** | **Otoño** | **Invierno** | **Invierno** | **Primavera** | **Primavera** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N** | 0,945 | 1,834 | 1,028 | 1,995 | 1,205 | 2,338 | 1,188 | 2,304 |
| **NNE** | 0,725 | 1,407 | 0,935 | 1,815 | 1,059 | 2,054 | 1,056 | 2,050 |
| **NE** | 0,544 | 1,056 | 0,728 | 1,413 | 0,882 | 1,710 | 0,697 | 1,352 |
| **ENE** | 0,535 | 1,038 | 0,938 | 1,820 | 1,032 | 2,002 | 0,608 | 1,179 |
| **E** | 0,495 | 0,961 | 0,632 | 1,226 | 0,715 | 1,387 | 0,509 | 0,988 |
| **ESE** | 0,509 | 0,987 | 0,629 | 1,220 | 0,857 | 1,663 | 0,702 | 1,362 |
| **SE** | 0,496 | 0,962 | 0,601 | 1,165 | 0,710 | 1,377 | 0,573 | 1,111 |
| **SSE** | 0,576 | 1,117 | 0,638 | 1,237 | 0,654 | 1,269 | 0,544 | 1,055 |
| **S** | 0,865 | 1,678 | 0,655 | 1,270 | 0,695 | 1,347 | 0,597 | 1,157 |
| **SSW** | 1,219 | 2,365 | 1,096 | 2,126 | 1,120 | 2,172 | 1,040 | 2,018 |
| **SW** | 1,022 | 1,982 | 1,026 | 1,990 | 1,171 | 2,271 | 1,129 | 2,190 |
| **WSW** | 0,654 | 1,269 | 0,729 | 1,414 | 0,739 | 1,434 | 0,642 | 1,246 |
| **W** | 0,705 | 1,368 | 0,770 | 1,494 | 0,773 | 1,499 | 0,756 | 1,467 |
| **WNW** | 0,725 | 1,407 | 0,639 | 1,240 | 0,662 | 1,284 | 0,820 | 1,591 |
| **NW** | 0,725 | 1,406 | 0,685 | 1,330 | 0,718 | 1,394 | 0,838 | 1,625 |
| **NNW** | 0,889 | 1,725 | 0,919 | 1,783 | 0,856 | 1,660 | 0,883 | 1,712 |
| **Global** | 0,788 | 1,529 | 0,729 | 1,415 | 0,891 | 1,729 | 0,829 | 1,608 |

<!-- Estadísticas: 19 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-25 -->


estaciones. Mediciones sector ITI. ........................................................................................ 64

Tabla 4-26: Tabla de incidencia del viento; Intervalo [0 - 4[ hrs. Mediciones sector ITI. ....... 66

<!-- INICIO TABLA 4-26 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|66| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-26: Tabla de incidencia del viento; Intervalo [0 - 4[ hrs. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 2,750 | 0,798 | 0,010 | - | - | - | 3,558 |
| **NNE** | - | 3,899 | 0,729 | - | - | - | - | 4,628 |
| **NE** | - | 2,487 | 0,278 | - | - | - | - | 2,766 |
| **ENE** | - | 1,627 | 0,100 | - | - | - | - | 1,726 |
| **E ** | - | 0,425 | - | - | - | - | - | 0,425 |
| **ESE** | - | 0,394 | - | - | - | - | - | 0,394 |
| **SE** | - | 0,320 | 0,005 | - | - | - | - | 0,325 |
| **SSE** | - | 0,630 | 0,010 | - | - | - | - | 0,640 |
| **S ** | - | 2,152 | 0,084 | - | - | - | - | 2,236 |
| **SSW** | - | 30,300 | 1,270 | - | - | - | - | 31,570 |
| **SW** | - | 16,740 | 0,803 | - | - | - | - | 17,543 |
| **WSW** | - | 2,173 | - | - | - | - | - | 2,173 |
| **W ** | - | 1,601 | - | - | - | - | - | 1,601 |
| **WNW** | - | 1,417 | - | - | - | - | - | 1,417 |
| **NW** | - | 1,800 | 0,037 | - | - | - | - | 1,837 |
| **NNW** | - | 2,251 | 0,194 | - | - | - | - | 2,445 |
| **Calmas** | 24,717 | - | - | - | - | - | - | 24,717 |
| **Sub Total**<br>**(%)**<br> | 24,717<br> | 70,965<br> | 4,308<br> | 0,010<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 19.056 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-26 -->


Tabla 4-27: Tabla de incidencia del viento; Intervalo [4 - 8[ hrs. Mediciones sector ITI. ....... 67

<!-- INICIO TABLA 4-27 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|67| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-27: Tabla de incidencia del viento; Intervalo [4 - 8[ hrs. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 2,382 | 0,352 | 0,005 | - | - | - | 2,739 |
| **NNE** | - | 3,700 | 0,897 | 0,005 | - | - | - | 4,602 |
| **NE** | - | 4,041 | 0,299 | - | - | - | - | 4,340 |
| **ENE** | - | 4,865 | 0,546 | - | - | - | - | 5,410 |
| **E ** | - | 1,622 | 0,005 | - | - | - | - | 1,627 |
| **ESE** | - | 1,454 | 0,047 | - | - | - | - | 1,501 |
| **SE** | - | 1,008 | 0,016 | - | - | - | - | 1,023 |
| **SSE** | - | 0,777 | 0,016 | - | - | - | - | 0,792 |
| **S ** | - | 1,952 | 0,010 | - | - | - | - | 1,963 |
| **SSW** | - | 15,517 | 0,420 | - | - | - | - | 15,937 |
| **SW** | - | 8,270 | 0,063 | - | - | - | - | 8,333 |
| **WSW** | - | 1,627 | 0,005 | - | - | - | - | 1,632 |
| **W ** | - | 0,955 | - | - | - | - | - | 0,955 |
| **WNW** | - | 0,855 | - | - | - | - | - | 0,855 |
| **NW** | - | 1,317 | 0,005 | - | - | - | - | 1,322 |
| **NNW** | - | 1,737 | 0,084 | - | - | - | - | 1,821 |
| **Calmas** | 45,146 | - | - | - | - | - | - | 45,146 |
| **Sub Total**<br>**(%)**<br> | 45,146<br> | 52,078<br> | 2,766<br> | 0,010<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 19.056 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-27 -->


Tabla 4-28: Tabla de incidencia del viento; Intervalo [8 - 12[ hrs. Mediciones sector ITI. ..... 68

<!-- INICIO TABLA 4-28 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|68| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-28: Tabla de incidencia del viento; Intervalo [8 - 12[ hrs. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 1,322 | 0,194 | 0,037 | - | - | - | 1,553 |
| **NNE** | - | 1,963 | 0,126 | - | - | - | - | 2,089 |
| **NE** | - | 3,038 | 0,236 | - | - | - | - | 3,275 |
| **ENE** | - | 5,736 | 1,506 | - | - | - | - | 7,242 |
| **E ** | - | 1,810 | 0,042 | - | - | - | - | 1,852 |
| **ESE** | - | 1,580 | 0,173 | - | - | - | - | 1,753 |
| **SE** | - | 1,616 | 0,037 | - | - | - | - | 1,653 |
| **SSE** | - | 1,244 | 0,016 | - | - | - | - | 1,259 |
| **S ** | - | 2,577 | 0,047 | - | - | - | - | 2,624 |
| **SSW** | - | 16,861 | 0,178 | - | - | - | - | 17,039 |
| **SW** | - | 7,090 | 0,026 | - | - | - | - | 7,116 |
| **WSW** | - | 1,238 | 0,021 | - | - | - | - | 1,259 |
| **W ** | - | 0,682 | 0,005 | - | - | - | - | 0,687 |
| **WNW** | - | 0,745 | 0,005 | - | - | - | - | 0,750 |
| **NW** | - | 0,567 | - | - | - | - | - | 0,567 |
| **NNW** | - | 0,866 | 0,094 | 0,021 | - | - | - | 0,981 |
| **Calmas** | 48,300 | - | - | - | - | - | - | 48,300 |
| **Sub Total**<br>**(%)**<br> | 48,300<br> | 48,935<br> | 2,708<br> | 0,058<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 19.056 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-28 -->


Tabla 4-29: Tabla de incidencia del viento; Intervalo [12 - 16[ hrs. Mediciones sector ITI. ... 69

<!-- INICIO TABLA 4-29 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|69| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-29: Tabla de incidencia del viento; Intervalo [12 - 16[ hrs. Mediciones sector****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 3,137 | 0,845 | 0,031 | - | - | - | 4,013 |
| **NNE** | - | 3,803 | 0,561 | 0,005 | - | - | - | 4,370 |
| **NE** | - | 2,130 | 0,037 | - | - | - | - | 2,167 |
| **ENE** | - | 2,135 | 0,425 | - | - | - | - | 2,560 |
| **E ** | - | 0,372 | 0,079 | - | - | - | - | 0,451 |
| **ESE** | - | 0,336 | 0,031 | - | - | - | - | 0,367 |
| **SE** | - | 0,294 | - | - | - | - | - | 0,294 |
| **SSE** | - | 0,467 | 0,010 | - | - | - | - | 0,477 |
| **S ** | - | 1,128 | 0,031 | - | - | - | - | 1,159 |
| **SSW** | - | 22,027 | 6,867 | - | - | - | - | 28,894 |
| **SW** | - | 14,935 | 3,247 | - | - | - | - | 18,182 |
| **WSW** | - | 5,639 | 0,042 | - | - | - | - | 5,681 |
| **W ** | - | 6,054 | 0,005 | - | - | - | - | 6,059 |
| **WNW** | - | 4,517 | 0,016 | - | - | - | - | 4,532 |
| **NW** | - | 4,632 | 0,021 | - | - | - | - | 4,653 |
| **NNW** | - | 3,158 | 0,289 | - | - | - | - | 3,446 |
| **Calmas** | 12,695 | - | - | - | - | - | - | 12,695 |
| **Sub Total**<br>**(%)**<br> | 12,695<br> | 74,763<br> | 12,506<br> | 0,037<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 19.063 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-29 -->


Tabla 4-30: Tabla de incidencia del viento; Intervalo [16 - 20[ hrs. Mediciones sector ITI. ... 70

<!-- INICIO TABLA 4-30 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|70| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-30: Tabla de incidencia del viento; Intervalo [16 - 20[ hrs. Mediciones sector****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 2,159 | 1,431 | 0,037 | - | - | - | 3,627 |
| **NNE** | - | 2,563 | 0,419 | - | - | - | - | 2,982 |
| **NE** | - | 0,335 | 0,005 | - | - | - | - | 0,341 |
| **ENE** | - | 0,026 | - | - | - | - | - | 0,026 |
| **E ** | - | 0,016 | - | - | - | - | - | 0,016 |
| **ESE** | - | 0,005 | - | - | - | - | - | 0,005 |
| **SE** | - | 0,010 | - | - | - | - | - | 0,010 |
| **SSE** | - | 0,031 | - | - | - | - | - | 0,031 |
| **S ** | - | 0,477 | 0,168 | - | - | - | - | 0,645 |
| **SSW** | - | 21,353 | 26,202 | 0,010 | - | - | - | 47,565 |
| **SW** | - | 13,669 | 11,929 | 0,005 | - | - | - | 25,604 |
| **WSW** | - | 4,156 | 0,084 | - | - | - | - | 4,240 |
| **W ** | - | 5,891 | 0,100 | - | - | - | - | 5,991 |
| **WNW** | - | 3,255 | - | - | - | - | - | 3,255 |
| **NW** | - | 3,491 | 0,031 | - | - | - | - | 3,522 |
| **NNW** | - | 1,557 | 0,283 | - | - | - | - | 1,840 |
| **Calmas** | 0,299 | - | - | - | - | - | - | 0,299 |
| **Sub Total**<br>**(%)**<br> | 0,299<br> | 58,997<br> | 40,652<br> | 0,052<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 19.079 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-30 -->


Tabla 4-31: Tabla de incidencia del viento; Intervalo [20 - 0[ hrs. Mediciones sector ITI. ..... 71

<!-- INICIO TABLA 4-31 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|71| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-31: Tabla de incidencia del viento; Intervalo [20 - 0[ hrs. Mediciones sector ITI.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 1,464 | 0,420 | - | - | - | - | 1,884 |
| **NNE** | - | 1,999 | 0,220 | - | - | - | - | 2,220 |
| **NE** | - | 0,483 | - | - | - | - | - | 0,483 |
| **ENE** | - | 0,084 | - | - | - | - | - | 0,084 |
| **E ** | - | 0,052 | - | - | - | - | - | 0,052 |
| **ESE** | - | 0,026 | - | - | - | - | - | 0,026 |
| **SE** | - | 0,121 | - | - | - | - | - | 0,121 |
| **SSE** | - | 0,582 | 0,010 | - | - | - | - | 0,593 |
| **S ** | - | 3,542 | 0,294 | - | - | - | - | 3,836 |
| **SSW** | - | 39,583 | 15,203 | - | - | - | - | 54,786 |
| **SW** | - | 18,698 | 7,279 | 0,005 | - | - | - | 25,981 |
| **WSW** | - | 1,601 | - | - | - | - | - | 1,601 |
| **W ** | - | 1,873 | - | - | - | - | - | 1,873 |
| **WNW** | - | 1,134 | - | - | - | - | - | 1,134 |
| **NW** | - | 1,217 | - | - | - | - | - | 1,217 |
| **NNW** | - | 0,913 | 0,073 | - | - | - | - | 0,987 |
| **Calmas** | 3,122 | - | - | - | - | - | - | 3,122 |
| **Sub Total**<br>**(%)**<br> | 3,122<br> | 73,373<br> | 23,499<br> | 0,005<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 19.056 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-31 -->


Tabla 4-32: Intensidades máxima globales y por dirección de procedencia de los vientos, por

<!-- INICIO TABLA 4-32 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|76| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-32: Intensidades máxima globales y por dirección de procedencia de los vientos, por intervalos horarios. Mediciones****

| Col1 | Intensidad máxima del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intervalos (hrs)** | **[0 - 4[** | **[0 - 4[** | **[4 - 8[** | **[4 - 8[** | **[8 - 12[** | **[8 - 12[** | **[12 - 16[** | **[12 - 16[** | **[16 - 20[** | **[16 - 20[** | **[20 - 0[** | **[20 - 0[** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N ** | 3,141 | 6,094 | 3,141 | 6,094 | 3,931 | 7,626 | 3,536 | 6,860 | 3,728 | 7,232 | 2,553 | 4,953 |
| **NNE** | 2,755 | 5,345 | 3,141 | 6,094 | 2,553 | 4,953 | 3,141 | 6,094 | 2,553 | 4,953 | 2,360 | 4,578 |
| **NE** | 2,553 | 4,953 | 2,360 | 4,578 | 2,553 | 4,953 | 1,773 | 3,440 | 1,570 | 3,046 | 1,175 | 2,280 |
| **ENE** | 1,773 | 3,440 | 2,553 | 4,953 | 2,948 | 5,719 | 2,360 | 4,578 | 0,588 | 1,141 | 1,175 | 2,280 |
| **E ** | 1,175 | 2,280 | 1,570 | 3,046 | 1,965 | 3,812 | 2,553 | 4,953 | 0,588 | 1,141 | 0,790 | 1,533 |
| **ESE** | 1,378 | 2,673 | 1,965 | 3,812 | 2,158 | 4,187 | 2,553 | 4,953 | 0,395 | 0,766 | 1,175 | 2,280 |
| **SE** | 1,570 | 3,046 | 2,158 | 4,187 | 2,158 | 4,187 | 1,175 | 2,280 | 0,588 | 1,141 | 1,378 | 2,673 |
| **SSE** | 1,570 | 3,046 | 2,360 | 4,578 | 2,755 | 5,345 | 1,773 | 3,440 | 1,378 | 2,673 | 1,570 | 3,046 |
| **S ** | 1,965 | 3,812 | 2,158 | 4,187 | 2,360 | 4,578 | 1,773 | 3,440 | 2,360 | 4,578 | 2,755 | 5,345 |
| **SSW** | 2,553 | 4,953 | 2,553 | 4,953 | 2,158 | 4,187 | 2,755 | 5,345 | 3,141 | 6,094 | 2,948 | 5,719 |
| **SW** | 2,158 | 4,187 | 1,965 | 3,812 | 1,773 | 3,440 | 2,948 | 5,719 | 3,141 | 6,094 | 3,141 | 6,094 |
| **WSW** | 1,378 | 2,673 | 1,570 | 3,046 | 2,360 | 4,578 | 1,773 | 3,440 | 1,773 | 3,440 | 1,378 | 2,673 |
| **W ** | 1,378 | 2,673 | 1,175 | 2,280 | 1,773 | 3,440 | 1,570 | 3,046 | 1,773 | 3,440 | 1,378 | 2,673 |
| **WNW** | 1,378 | 2,673 | 0,983 | 1,907 | 1,570 | 3,046 | 1,570 | 3,046 | 1,378 | 2,673 | 1,175 | 2,280 |
| **NW** | 1,965 | 3,812 | 1,570 | 3,046 | 1,175 | 2,280 | 1,570 | 3,046 | 1,965 | 3,812 | 1,378 | 2,673 |
| **NNW** | 2,360 | 4,578 | 2,360 | 4,578 | 3,536 | 6,860 | 2,553 | 4,953 | 2,553 | 4,953 | 2,158 | 4,187 |
| **Global** | 3,141 | 6,094 | 3,141 | 6,094 | 3,931 | 7,626 | 3,536 | 6,860 | 3,728 | 7,232 | 3,141 | 6,094 |

<!-- Estadísticas: 19 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-32 -->


intervalos horarios. Mediciones sector ITI. ............................................................................ 76

Tabla 4-33: Intensidades promedio globales y por dirección de procedencia de los vientos, por

<!-- INICIO TABLA 4-33 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|77| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-33: Intensidades promedio globales y por dirección de procedencia de los vientos, por intervalos horarios Mediciones****

| Col1 | Intensidad promedio del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intervalos (hrs)** | **[0 - 4[** | **[0 - 4[** | **[4 - 8[** | **[4 - 8[** | **[8 - 12[** | **[8 - 12[** | **[12 - 16[** | **[12 - 16[** | **[16 - 20[** | **[16 - 20[** | **[20 - 0[** | **[20 - 0[** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N ** | 1,039 | 2,016 | 0,905 | 1,756 | 0,910 | 1,765 | 1,065 | 2,065 | 1,443 | 2,800 | 1,138 | 2,207 |
| **NNE** | 0,956 | 1,854 | 1,000 | 1,940 | 0,777 | 1,507 | 0,914 | 1,773 | 1,124 | 2,181 | 0,938 | 1,820 |
| **NE** | 0,809 | 1,569 | 0,759 | 1,472 | 0,786 | 1,524 | 0,633 | 1,229 | 0,778 | 1,510 | 0,571 | 1,108 |
| **ENE** | 0,732 | 1,420 | 0,838 | 1,626 | 1,017 | 1,974 | 0,912 | 1,770 | 0,472 | 0,916 | 0,529 | 1,026 |
| **E ** | 0,525 | 1,019 | 0,587 | 1,140 | 0,644 | 1,249 | 0,794 | 1,540 | 0,524 | 1,016 | 0,513 | 0,994 |
| **ESE** | 0,638 | 1,237 | 0,695 | 1,348 | 0,778 | 1,509 | 0,726 | 1,408 | 0,395 | 0,766 | 0,628 | 1,219 |
| **SE** | 0,571 | 1,108 | 0,607 | 1,177 | 0,636 | 1,234 | 0,626 | 1,215 | 0,492 | 0,954 | 0,659 | 1,278 |
| **SSE** | 0,587 | 1,139 | 0,584 | 1,134 | 0,576 | 1,117 | 0,668 | 1,296 | 0,689 | 1,337 | 0,734 | 1,425 |
| **S ** | 0,696 | 1,350 | 0,587 | 1,139 | 0,572 | 1,109 | 0,692 | 1,342 | 1,084 | 2,103 | 0,885 | 1,716 |
| **SSW** | 0,822 | 1,595 | 0,719 | 1,395 | 0,662 | 1,284 | 1,151 | 2,234 | 1,523 | 2,955 | 1,229 | 2,384 |
| **SW** | 0,797 | 1,545 | 0,694 | 1,347 | 0,654 | 1,268 | 1,054 | 2,046 | 1,446 | 2,805 | 1,227 | 2,381 |
| **WSW** | 0,544 | 1,055 | 0,536 | 1,041 | 0,519 | 1,008 | 0,715 | 1,387 | 0,881 | 1,710 | 0,649 | 1,259 |
| **W ** | 0,509 | 0,988 | 0,512 | 0,993 | 0,504 | 0,977 | 0,753 | 1,460 | 0,913 | 1,771 | 0,665 | 1,290 |
| **WNW** | 0,543 | 1,054 | 0,490 | 0,950 | 0,526 | 1,020 | 0,758 | 1,470 | 0,866 | 1,679 | 0,642 | 1,246 |
| **NW** | 0,620 | 1,202 | 0,590 | 1,144 | 0,549 | 1,065 | 0,749 | 1,453 | 0,904 | 1,754 | 0,662 | 1,285 |
| **NNW** | 0,837 | 1,624 | 0,773 | 1,499 | 0,871 | 1,689 | 0,896 | 1,738 | 1,081 | 2,097 | 0,815 | 1,582 |
| **Global** | 0,630 | 1,221 | 0,444 | 0,861 | 0,415 | 0,805 | 0,866 | 1,679 | 1,363 | 2,645 | 1,128 | 2,189 |

<!-- Estadísticas: 19 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-33 -->


intervalos horarios Mediciones sector ITI. ............................................................................. 77

Tabla 4-34: Coeficientes de correlación en las componentes ortogonales en sus respectivos

<!-- INICIO TABLA 4-34 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1| |---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-34: Coeficientes de correlación en las componentes ortogonales en sus****

| Desfase (hrs.) | Componente<br>U (-) | Componente<br>V (-) | Desfase (hrs.) | Componente<br>U (-) | Componente<br>V (-) |
| --- | --- | --- | --- | --- | --- |
| -24 | -0,018 | 0,051 | 1 | 0,594 | 0,603 |
| -23 | 0,043 | 0,057 | 2 | 0,501 | 0,566 |
| -22 | 0,119 | 0,078 | 3 | 0,377 | 0,510 |
| -21 | 0,201 | 0,107 | 4 | 0,250 | 0,440 |
| -20 | 0,263 | 0,145 | 5 | 0,113 | 0,370 |
| -19 | 0,324 | 0,185 | 6 | -0,012 | 0,296 |
| -18 | 0,364 | 0,230 | 7 | -0,118 | 0,228 |
| -17 | 0,361 | 0,262 | 8 | -0,192 | 0,161 |
| -16 | 0,323 | 0,276 | 9 | -0,224 | 0,122 |
| -15 | 0,264 | 0,284 | 10 | -0,214 | 0,094 |
| -14 | 0,178 | 0,282 | 11 | -0,157 | 0,092 |
| -13 | 0,085 | 0,272 | 12 | -0,080 | 0,107 |
| -12 | -0,015 | 0,246 | 13 | 0,015 | 0,133 |
| -11 | -0,103 | 0,218 | 14 | 0,122 | 0,168 |
| -10 | -0,169 | 0,187 | 15 | 0,212 | 0,207 |
| -9 | -0,201 | 0,160 | 16 | 0,286 | 0,246 |
| -8 | -0,188 | 0,128 | 17 | 0,339 | 0,277 |
| -7 | -0,134 | 0,114 | 18 | 0,350 | 0,281 |
| -6 | -0,052 | 0,132 | 19 | 0,333 | 0,285 |
| -5 | 0,061 | 0,174 | 20 | 0,291 | 0,270 |
| -4 | 0,198 | 0,243 | 21 | 0,224 | 0,240 |
| -3 | 0,337 | 0,337 | 22 | 0,149 | 0,206 |
| -2 | 0,461 | 0,431 | 23 | 0,080 | 0,170 |
| -1 | 0,562 | 0,529 | 24 | 0,011 | 0,128 |
| 0 | 0,625 | 0,601 | <br> <br> | <br> <br> | <br> <br> |

<!-- Estadísticas: 25 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-34 -->


desfases. .............................................................................................................................. 82

Tabla 4-35: Estadística magnitud del viento entre estaciones meteorológicas. Medición y base

<!-- INICIO TABLA 4-35 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|85| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-35: Estadística magnitud del viento entre estaciones meteorológicas. Medición****

| Magnitud viento (m/s) | Medición | Histórica | Diferencia |
| --- | --- | --- | --- |
| **Promedio** | 0,81 | 1,28 | 0,47 |
| **Desviación estándar** | 0,58 | 0,76 | 0,18 |
| **75 Percentil** | 0,40 | 0,63 | 0,24 |
| **25 Percentil** | 1,18 | 1,90 | 0,72 |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. **Tabla 4-36: Estadística direccional del viento entre estaciones meteorológicas.** -->
<!-- FIN TABLA 4-35 -->

de dato histórica, 2020-2021. ................................................................................................ 85

Tabla 4-36: Estadística direccional del viento entre estaciones meteorológicas. Medición y

<!-- INICIO TABLA 4-36 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |**75 Percentil**|0,40|0,63|0,24| |**25 Percentil**|1,18|1,90|0,72| Fuente: Ecotecnos, 2021. -->

**Tabla 4-36: Estadística direccional del viento entre estaciones meteorológicas.****

| Col1 | Medición | Histórica | Diferencia |
| --- | --- | --- | --- |
| **U promedio (m/s)** | 0,38 | 0,83 | -0,45 |
| **V promedio (m/s)** | 0,49 | 0,70 | -0,21 |
| **Dirección promedio (°)** | 217,69 | 229,91 | -12,22 |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. En base de los resultados antes expuestos, es posible establecer la relación del comportamiento de las intensidades del viento entre las mediciones efectuadas por la DMC, -->
<!-- FIN TABLA 4-36 -->

base de dato histórica, 2020-2021. ....................................................................................... 85

Tabla 4-37: Tabla de incidencia del viento. Base de datos histórica. .................................... 89

<!-- INICIO TABLA 4-37 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|89| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-37: Tabla de incidencia del viento. Base de datos histórica.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 1,837 | 0,240 | - | - | - | - | 2,078 |
| **NNE** | - | 1,182 | 0,047 | - | - | - | - | 1,229 |
| **NE** | - | 0,893 | 0,012 | - | - | - | - | 0,905 |
| **ENE** | - | 1,111 | 0,018 | - | - | - | - | 1,129 |
| **E ** | - | 2,272 | 0,131 | 0,001 | 0,002 | - | - | 2,406 |
| **ESE** | - | 2,555 | 0,254 | - | - | - | - | 2,809 |
| **SE** | - | 2,544 | 0,181 | - | - | - | - | 2,725 |
| **SSE** | - | 3,783 | 0,332 | - | - | - | - | 4,115 |
| **S ** | - | 10,091 | 5,906 | 0,108 | - | - | - | 16,106 |
| **SSW** | - | 8,353 | 15,427 | 0,956 | - | - | - | 24,736 |
| **SW** | - | 4,922 | 10,389 | 0,382 | - | - | - | 15,693 |
| **WSW** | - | 3,853 | 5,090 | 0,020 | - | - | - | 8,963 |
| **W ** | - | 3,419 | 1,083 | - | - | - | - | 4,502 |
| **WNW** | - | 1,641 | 0,190 | - | - | - | - | 1,831 |
| **NW** | - | 1,263 | 0,055 | - | - | - | - | 1,318 |
| **NNW** | - | 1,453 | 0,196 | - | - | - | - | 1,649 |
| **VRB** | - | 1,387 | 0,003 | - | - | - | - | 1,390 |
| **Calmas** | 6,417 | - | - | - | - | - | - | 6,417 |
| **Sub Total**<br>**(%)**<br> | 6,417<br> | 52,561<br> | 39,553<br> | 1,467<br> | 0,002<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 89.472 |

<!-- Estadísticas: 23 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-37 -->


Tabla 4-38: Intensidades promedio y máxima globales y por dirección de procedencia de los

<!-- INICIO TABLA 4-38 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Fuente: Ecotecnos, 2021. **Gráfico 4-34: Variación de la magnitud promedio y máxima del viento por dirección de** **procedencia. Base de datos histórica.** -->

**Tabla 4-38: Intensidades promedio y máxima globales y por dirección de procedencia****

| Col1 | Intensidad del viento | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Direcciones** | **Máxima** | **Máxima** | **Promedio** | **Promedio** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N ** | 2,843 | 5,515 | 0,837 | 1,624 |
| **NNE** | 2,370 | 4,598 | 0,716 | 1,389 |
| **NE** | 1,896 | 3,678 | 0,672 | 1,304 |
| **ENE** | 1,896 | 3,678 | 0,649 | 1,259 |
| **E ** | 5,529 | 10,726 | 0,720 | 1,396 |
| **ESE** | 2,370 | 4,598 | 0,804 | 1,561 |
| **SE** | 3,001 | 5,822 | 0,782 | 1,518 |
| **SSE** | 3,001 | 5,822 | 0,826 | 1,603 |
| **S ** | 4,423 | 8,581 | 1,257 | 2,439 |
| **SSW** | 4,423 | 8,581 | 1,749 | 3,393 |
| **SW** | 4,107 | 7,968 | 1,707 | 3,312 |
| **WSW** | 3,475 | 6,742 | 1,463 | 2,838 |
| **W ** | 2,528 | 4,904 | 1,017 | 1,973 |
| **WNW** | 2,843 | 5,515 | 0,872 | 1,692 |
| **NW** | 2,528 | 4,904 | 0,792 | 1,537 |
| **NNW** | 2,686 | 5,211 | 0,865 | 1,677 |
| **Global** | 5,529 | 10,726 | 1,261 | 2,447 |

<!-- Estadísticas: 19 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-38 -->


vientos. Base de datos histórica. .......................................................................................... 90

Tabla 4-39 Valores estadísticos de las componentes ortogonales de la intensidad del viento.

Base de datos histórica. ........................................................................................................ 91

Tabla 4-40: Tabla de incidencia del viento, enero promedio. Base de datos histórica. .......... 94

<!-- INICIO TABLA 4-40 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|94| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-40: Tabla de incidencia del viento, enero promedio. Base de datos histórica.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | - | - | - | - | - | - | 0,000 |
| **NNE** | - | - | - | - | - | - | - | 0,000 |
| **NE** | - | - | - | - | - | - | - | 0,000 |
| **ENE** | - | - | - | - | - | - | - | 0,000 |
| **E ** | - | - | - | - | - | - | - | 0,000 |
| **ESE** | - | 0,403 | - | - | - | - | - | 0,403 |
| **SE** | - | 2,688 | - | - | - | - | - | 2,688 |
| **SSE** | - | 9,274 | - | - | - | - | - | 9,274 |
| **S ** | - | 20,968 | 1,075 | - | - | - | - | 22,043 |
| **SSW** | - | 11,290 | 23,118 | - | - | - | - | 34,409 |
| **SW** | - | 4,704 | 26,075 | - | - | - | - | 30,780 |
| **WSW** | - | 0,403 | - | - | - | - | - | 0,403 |
| **W ** | - | - | - | - | - | - | - | 0,000 |
| **WNW** | - | - | - | - | - | - | - | 0,000 |
| **NW** | - | - | - | - | - | - | - | 0,000 |
| **NNW** | - | - | - | - | - | - | - | 0,000 |
| **Calmas** | - | - | - | - | - | - | - | 0,000 |
| **Sub Total**<br>**(%)**<br> | 0,000<br> | 49,731<br> | 50,269<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 744 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-40 -->


Tabla 4-41: Tabla de incidencia del viento, febrero promedio. Base de datos histórica. ........ 95

<!-- INICIO TABLA 4-41 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|95| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-41: Tabla de incidencia del viento, febrero promedio. Base de datos histórica.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | - | - | - | - | - | - | 0,000 |
| **NNE** | - | - | - | - | - | - | - | 0,000 |
| **NE** | - | 0,144 | - | - | - | - | - | 0,144 |
| **ENE** | - | - | - | - | - | - | - | 0,000 |
| **E ** | - | - | - | - | - | - | - | 0,000 |
| **ESE** | - | - | - | - | - | - | - | 0,000 |
| **SE** | - | 1,149 | - | - | - | - | - | 1,149 |
| **SSE** | - | 5,316 | - | - | - | - | - | 5,316 |
| **S ** | - | 28,017 | 0,431 | - | - | - | - | 28,448 |
| **SSW** | - | 11,638 | 32,615 | - | - | - | - | 44,253 |
| **SW** | - | 2,155 | 18,103 | - | - | - | - | 20,259 |
| **WSW** | - | 0,287 | 0,144 | - | - | - | - | 0,431 |
| **W ** | - | - | - | - | - | - | - | 0,000 |
| **WNW** | - | - | - | - | - | - | - | 0,000 |
| **NW** | - | - | - | - | - | - | - | 0,000 |
| **NNW** | - | - | - | - | - | - | - | 0,000 |
| **Calmas** | - | - | - | - | - | - | - | 0,000 |
| **Sub Total**<br>**(%)**<br> | 0,000<br> | 48,707<br> | 51,293<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 696 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-41 -->


Tabla 4-42: Tabla de incidencia del viento, marzo promedio. Base de datos histórica. ......... 96

<!-- INICIO TABLA 4-42 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|96| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-42: Tabla de incidencia del viento, marzo promedio. Base de datos histórica.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | - | - | - | - | - | - | 0,000 |
| **NNE** | - | - | - | - | - | - | - | 0,000 |
| **NE** | - | - | - | - | - | - | - | 0,000 |
| **ENE** | - | - | - | - | - | - | - | 0,000 |
| **E ** | - | - | - | - | - | - | - | 0,000 |
| **ESE** | - | - | - | - | - | - | - | 0,000 |
| **SE** | - | 1,075 | - | - | - | - | - | 1,075 |
| **SSE** | - | 9,946 | - | - | - | - | - | 9,946 |
| **S ** | - | 28,360 | 2,016 | - | - | - | - | 30,376 |
| **SSW** | - | 9,677 | 28,360 | - | - | - | - | 38,038 |
| **SW** | - | 2,285 | 17,070 | - | - | - | - | 19,355 |
| **WSW** | - | 0,672 | 0,269 | - | - | - | - | 0,941 |
| **W ** | - | - | - | - | - | - | - | 0,000 |
| **WNW** | - | - | - | - | - | - | - | 0,000 |
| **NW** | - | - | - | - | - | - | - | 0,000 |
| **NNW** | - | - | - | - | - | - | - | 0,000 |
| **Calmas** | 0,269 | - | - | - | - | - | - | 0,269 |
| **Sub Total**<br>**(%)**<br> | 0,269<br> | 52,016<br> | 47,715<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 744 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-42 -->


Tabla 4-43: Tabla de incidencia del viento, abril promedio. Base de datos histórica. ............ 97

<!-- INICIO TABLA 4-43 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|97| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-43: Tabla de incidencia del viento, abril promedio. Base de datos histórica.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | - | - | - | - | - | - | 0,000 |
| **NNE** | - | - | - | - | - | - | - | 0,000 |
| **NE** | - | - | - | - | - | - | - | 0,000 |
| **ENE** | - | - | - | - | - | - | - | 0,000 |
| **E ** | - | - | - | - | - | - | - | 0,000 |
| **ESE** | - | 0,417 | - | - | - | - | - | 0,417 |
| **SE** | - | 4,306 | - | - | - | - | - | 4,306 |
| **SSE** | - | 17,500 | - | - | - | - | - | 17,500 |
| **S ** | - | 24,306 | 2,778 | - | - | - | - | 27,083 |
| **SSW** | - | 7,222 | 22,083 | - | - | - | - | 29,306 |
| **SW** | - | 2,500 | 18,056 | - | - | - | - | 20,556 |
| **WSW** | - | 0,417 | - | - | - | - | - | 0,417 |
| **W ** | - | - | - | - | - | - | - | 0,000 |
| **WNW** | - | - | - | - | - | - | - | 0,000 |
| **NW** | - | - | - | - | - | - | - | 0,000 |
| **NNW** | - | - | - | - | - | - | - | 0,000 |
| **Calmas** | 0,417 | - | - | - | - | - | - | 0,417 |
| **Sub Total**<br>**(%)**<br> | 0,417<br> | 56,667<br> | 42,917<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 720 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-43 -->


Tabla 4-44: Tabla de incidencia del viento, mayo promedio. Base de datos histórica. .......... 98

<!-- INICIO TABLA 4-44 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|98| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-44: Tabla de incidencia del viento, mayo promedio. Base de datos histórica.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | - | - | - | - | - | - | 0,000 |
| **NNE** | - | - | - | - | - | - | - | 0,000 |
| **NE** | - | 0,269 | - | - | - | - | - | 0,269 |
| **ENE** | - | 0,403 | - | - | - | - | - | 0,403 |
| **E ** | - | 1,075 | - | - | - | - | - | 1,075 |
| **ESE** | - | 4,839 | - | - | - | - | - | 4,839 |
| **SE** | - | 9,409 | - | - | - | - | - | 9,409 |
| **SSE** | - | 16,935 | - | - | - | - | - | 16,935 |
| **S ** | - | 15,457 | 0,269 | - | - | - | - | 15,726 |
| **SSW** | - | 12,231 | 7,124 | - | - | - | - | 19,355 |
| **SW** | - | 4,301 | 22,984 | - | - | - | - | 27,285 |
| **WSW** | - | 2,419 | 2,151 | - | - | - | - | 4,570 |
| **W ** | - | - | - | - | - | - | - | 0,000 |
| **WNW** | - | - | - | - | - | - | - | 0,000 |
| **NW** | - | - | - | - | - | - | - | 0,000 |
| **NNW** | - | - | - | - | - | - | - | 0,000 |
| **Calmas** | 0,134 | - | - | - | - | - | - | 0,134 |
| **Sub Total**<br>**(%)**<br> | 0,134<br> | 67,339<br> | 32,527<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 744 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-44 -->


Tabla 4-45: Tabla de incidencia del viento, junio promedio. Base de datos histórica. ........... 99

<!-- INICIO TABLA 4-45 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|99| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-45: Tabla de incidencia del viento, junio promedio. Base de datos histórica.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 0,417 | - | - | - | - | - | 0,417 |
| **NNE** | - | 0,694 | - | - | - | - | - | 0,694 |
| **NE** | - | 0,972 | - | - | - | - | - | 0,972 |
| **ENE** | - | 1,389 | - | - | - | - | - | 1,389 |
| **E ** | - | 2,083 | - | - | - | - | - | 2,083 |
| **ESE** | - | 4,861 | - | - | - | - | - | 4,861 |
| **SE** | - | 10,694 | - | - | - | - | - | 10,694 |
| **SSE** | - | 12,222 | - | - | - | - | - | 12,222 |
| **S ** | - | 10,694 | - | - | - | - | - | 10,694 |
| **SSW** | - | 15,694 | 3,750 | - | - | - | - | 19,444 |
| **SW** | - | 6,944 | 16,806 | - | - | - | - | 23,750 |
| **WSW** | - | 6,528 | 4,444 | - | - | - | - | 10,972 |
| **W ** | - | 1,111 | - | - | - | - | - | 1,111 |
| **WNW** | - | 0,417 | - | - | - | - | - | 0,417 |
| **NW** | - | 0,278 | - | - | - | - | - | 0,278 |
| **NNW** | - | - | - | - | - | - | - | 0,000 |
| **Calmas** | - | - | - | - | - | - | - | 0,000 |
| **Sub Total**<br>**(%)**<br> | 0,000<br> | 75,000<br> | 25,000<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 720 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-45 -->


Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|6|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Tabla 4-46: Tabla de incidencia del viento, julio promedio. Base de datos histórica. .......... 100

<!-- INICIO TABLA 4-46 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|100| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-46: Tabla de incidencia del viento, julio promedio. Base de datos histórica.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 1,075 | - | - | - | - | - | 1,075 |
| **NNE** | - | 1,344 | - | - | - | - | - | 1,344 |
| **NE** | - | 1,210 | - | - | - | - | - | 1,210 |
| **ENE** | - | 0,941 | - | - | - | - | - | 0,941 |
| **E ** | - | 1,882 | - | - | - | - | - | 1,882 |
| **ESE** | - | 5,376 | - | - | - | - | - | 5,376 |
| **SE** | - | 7,796 | - | - | - | - | - | 7,796 |
| **SSE** | - | 11,022 | - | - | - | - | - | 11,022 |
| **S ** | - | 8,065 | - | - | - | - | - | 8,065 |
| **SSW** | - | 11,828 | 1,747 | - | - | - | - | 13,575 |
| **SW** | - | 11,828 | 16,532 | - | - | - | - | 28,360 |
| **WSW** | - | 6,586 | 7,930 | - | - | - | - | 14,516 |
| **W ** | - | 1,613 | 0,269 | - | - | - | - | 1,882 |
| **WNW** | - | 1,075 | - | - | - | - | - | 1,075 |
| **NW** | - | 0,806 | - | - | - | - | - | 0,806 |
| **NNW** | - | 0,941 | - | - | - | - | - | 0,941 |
| **Calmas** | 0,134 | - | - | - | - | - | - | 0,134 |
| **Sub Total**<br>**(%)**<br> | 0,134<br> | 73,387<br> | 26,478<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 744 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-46 -->


Tabla 4-47: Tabla de incidencia del viento, agosto promedio. Base de datos histórica. ...... 101

<!-- INICIO TABLA 4-47 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|101| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-47: Tabla de incidencia del viento, agosto promedio. Base de datos histórica.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 0,941 | - | - | - | - | - | 0,941 |
| **NNE** | - | 0,672 | - | - | - | - | - | 0,672 |
| **NE** | - | 0,672 | - | - | - | - | - | 0,672 |
| **ENE** | - | 0,538 | - | - | - | - | - | 0,538 |
| **E ** | - | 1,613 | - | - | - | - | - | 1,613 |
| **ESE** | - | 3,495 | - | - | - | - | - | 3,495 |
| **SE** | - | 9,946 | - | - | - | - | - | 9,946 |
| **SSE** | - | 7,527 | - | - | - | - | - | 7,527 |
| **S ** | - | 5,511 | - | - | - | - | - | 5,511 |
| **SSW** | - | 10,081 | 1,747 | - | - | - | - | 11,828 |
| **SW** | - | 13,575 | 15,591 | - | - | - | - | 29,167 |
| **WSW** | - | 5,914 | 12,500 | - | - | - | - | 18,414 |
| **W ** | - | 3,898 | 0,538 | - | - | - | - | 4,435 |
| **WNW** | - | 2,151 | - | - | - | - | - | 2,151 |
| **NW** | - | 1,344 | - | - | - | - | - | 1,344 |
| **NNW** | - | 1,747 | - | - | - | - | - | 1,747 |
| **Calmas** | - | - | - | - | - | - | - | 0,000 |
| **Sub Total**<br>**(%)**<br> | 0,000<br> | 69,624<br> | 30,376<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 744 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-47 -->


Tabla 4-48: Tabla de incidencia del viento, septiembre promedio. Base de datos histórica. 102

<!-- INICIO TABLA 4-48 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|102| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-48: Tabla de incidencia del viento, septiembre promedio. Base de datos****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | 0,139 | - | - | - | - | - | 0,139 |
| **NNE** | - | - | - | - | - | - | - | 0,000 |
| **NE** | - | - | - | - | - | - | - | 0,000 |
| **ENE** | - | - | - | - | - | - | - | 0,000 |
| **E ** | - | 0,278 | - | - | - | - | - | 0,278 |
| **ESE** | - | 0,972 | - | - | - | - | - | 0,972 |
| **SE** | - | 2,083 | - | - | - | - | - | 2,083 |
| **SSE** | - | 6,111 | - | - | - | - | - | 6,111 |
| **S ** | - | 12,222 | - | - | - | - | - | 12,222 |
| **SSW** | - | 12,917 | 3,750 | - | - | - | - | 16,667 |
| **SW** | - | 15,694 | 22,639 | - | - | - | - | 38,333 |
| **WSW** | - | 9,028 | 11,111 | - | - | - | - | 20,139 |
| **W ** | - | 2,222 | 0,556 | - | - | - | - | 2,778 |
| **WNW** | - | 0,139 | - | - | - | - | - | 0,139 |
| **NW** | - | 0,139 | - | - | - | - | - | 0,139 |
| **NNW** | - | - | - | - | - | - | - | 0,000 |
| **Calmas** | - | - | - | - | - | - | - | 0,000 |
| **Sub Total**<br>**(%)**<br> | 0,000<br> | 61,944<br> | 38,056<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 720 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-48 -->


Tabla 4-49: Tabla de incidencia del viento, octubre promedio. Base de datos histórica ...... 103

<!-- INICIO TABLA 4-49 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|103| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-49: Tabla de incidencia del viento, octubre promedio. Base de datos histórica****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | - | - | - | - | - | - | 0,000 |
| **NNE** | - | - | - | - | - | - | - | 0,000 |
| **NE** | - | 0,134 | - | - | - | - | - | 0,134 |
| **ENE** | - | - | - | - | - | - | - | 0,000 |
| **E ** | - | - | - | - | - | - | - | 0,000 |
| **ESE** | - | 0,269 | - | - | - | - | - | 0,269 |
| **SE** | - | 1,075 | - | - | - | - | - | 1,075 |
| **SSE** | - | 4,167 | - | - | - | - | - | 4,167 |
| **S ** | - | 12,231 | - | - | - | - | - | 12,231 |
| **SSW** | - | 21,774 | 7,930 | - | - | - | - | 29,704 |
| **SW** | - | 12,500 | 25,134 | - | - | - | - | 37,634 |
| **WSW** | - | 5,511 | 7,661 | - | - | - | - | 13,172 |
| **W ** | - | 0,806 | 0,134 | - | - | - | - | 0,941 |
| **WNW** | - | 0,403 | - | - | - | - | - | 0,403 |
| **NW** | - | 0,269 | - | - | - | - | - | 0,269 |
| **NNW** | - | - | - | - | - | - | - | 0,000 |
| **Calmas** | - | - | - | - | - | - | - | 0,000 |
| **Sub Total**<br>**(%)**<br> | 0,000<br> | 59,140<br> | 40,860<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 744 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-49 -->


Tabla 4-50: Tabla de incidencia del viento, noviembre promedio. Base de datos histórica. 104

<!-- INICIO TABLA 4-50 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|104| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-50: Tabla de incidencia del viento, noviembre promedio. Base de datos****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | - | - | - | - | - | - | 0,000 |
| **NNE** | - | - | - | - | - | - | - | 0,000 |
| **NE** | - | - | - | - | - | - | - | 0,000 |
| **ENE** | - | - | - | - | - | - | - | 0,000 |
| **E ** | - | 0,139 | - | - | - | - | - | 0,139 |
| **ESE** | - | 0,694 | - | - | - | - | - | 0,694 |
| **SE** | - | 1,806 | - | - | - | - | - | 1,806 |
| **SSE** | - | 7,778 | - | - | - | - | - | 7,778 |
| **S ** | - | 16,111 | - | - | - | - | - | 16,111 |
| **SSW** | - | 19,306 | 10,556 | - | - | - | - | 29,861 |
| **SW** | - | 5,278 | 27,222 | - | - | - | - | 32,500 |
| **WSW** | - | 3,472 | 7,083 | - | - | - | - | 10,556 |
| **W ** | - | 0,278 | 0,139 | - | - | - | - | 0,417 |
| **WNW** | - | - | - | - | - | - | - | 0,000 |
| **NW** | - | - | - | - | - | - | - | 0,000 |
| **NNW** | - | - | - | - | - | - | - | 0,000 |
| **Calmas** | 0,139 | - | - | - | - | - | - | 0,139 |
| **Sub Total**<br>**(%)**<br> | 0,139<br> | 54,861<br> | 45,000<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 720 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-50 -->


Tabla 4-51: Tabla de incidencia del viento, diciembre promedio. Base de datos histórica. . 105

<!-- INICIO TABLA 4-51 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|105| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-51: Tabla de incidencia del viento, diciembre promedio. Base de datos****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N ** | - | - | - | - | - | - | - | 0,000 |
| **NNE** | - | - | - | - | - | - | - | 0,000 |
| **NE** | - | - | - | - | - | - | - | 0,000 |
| **ENE** | - | - | - | - | - | - | - | 0,000 |
| **E ** | - | - | - | - | - | - | - | 0,000 |
| **ESE** | - | 0,134 | - | - | - | - | - | 0,134 |
| **SE** | - | 3,360 | - | - | - | - | - | 3,360 |
| **SSE** | - | 12,769 | - | - | - | - | - | 12,769 |
| **S ** | - | 17,339 | 0,134 | - | - | - | - | 17,473 |
| **SSW** | - | 13,710 | 15,323 | - | - | - | - | 29,032 |
| **SW** | - | 4,167 | 32,124 | - | - | - | - | 36,290 |
| **WSW** | - | 0,403 | 0,538 | - | - | - | - | 0,941 |
| **W ** | - | - | - | - | - | - | - | 0,000 |
| **WNW** | - | - | - | - | - | - | - | 0,000 |
| **NW** | - | - | - | - | - | - | - | 0,000 |
| **NNW** | - | - | - | - | - | - | - | 0,000 |
| **Calmas** | - | - | - | - | - | - | - | 0,000 |
| **Sub Total**<br>**(%)**<br> | 0,000<br> | 51,882<br> | 48,118<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 744 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-51 -->


Tabla 4-52: Intensidades máxima globales y por dirección de procedencia de los vientos, entre

<!-- INICIO TABLA 4-52 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|113| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-52: Intensidades máxima globales y por dirección de procedencia de los vientos, entre los meses enero-junio. Base de****

| Col1 | Intensidad máxima del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Meses** | **Enero** | **Enero** | **Febrero** | **Febrero** | **Marzo** | **Marzo** | **Abril** | **Abril** | **Mayo** | **Mayo** | **Junio** | **Junio** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N ** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,553 | 1,073 |
| **NNE** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,679 | 1,318 |
| **NE** | 0,000 | 0,000 | 0,474 | 0,920 | 0,000 | 0,000 | 0,000 | 0,000 | 0,632 | 1,226 | 0,853 | 1,655 |
| **ENE** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,743 | 1,441 | 1,043 | 2,023 |
| **E ** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,885 | 1,717 | 0,980 | 1,900 |
| **ESE** | 0,761 | 1,477 | 0,000 | 0,000 | 0,000 | 0,000 | 0,711 | 1,379 | 0,948 | 1,839 | 1,059 | 2,054 |
| **SE** | 0,704 | 1,365 | 0,869 | 1,686 | 0,934 | 1,811 | 0,901 | 1,747 | 0,995 | 1,931 | 1,074 | 2,084 |
| **SSE** | 0,991 | 1,923 | 0,991 | 1,923 | 1,122 | 2,176 | 1,059 | 2,054 | 1,027 | 1,992 | 1,090 | 2,115 |
| **S ** | 1,910 | 3,706 | 1,810 | 3,511 | 2,198 | 4,263 | 1,912 | 3,709 | 1,643 | 3,188 | 1,232 | 2,391 |
| **SSW** | 2,930 | 5,683 | 2,815 | 5,460 | 2,780 | 5,394 | 2,670 | 5,179 | 2,196 | 4,260 | 1,896 | 3,678 |
| **SW** | 2,858 | 5,544 | 2,571 | 4,988 | 2,559 | 4,965 | 2,496 | 4,842 | 2,259 | 4,383 | 2,149 | 4,168 |
| **WSW** | 1,379 | 2,675 | 1,738 | 3,372 | 1,659 | 3,218 | 1,201 | 2,330 | 1,785 | 3,463 | 1,849 | 3,586 |
| **W ** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 1,327 | 2,575 |
| **WNW** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 1,011 | 1,962 |
| **NW** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,664 | 1,287 |
| **NNW** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| **Global** | 2,930 | 5,683 | 2,815 | 5,460 | 2,780 | 5,394 | 2,670 | 5,179 | 2,259 | 4,383 | 2,149 | 4,168 |

<!-- Estadísticas: 19 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-52 -->

los meses enero-junio. Base de datos histórica. ................................................................. 113

Tabla 4-53: Intensidades máxima globales y por dirección de procedencia de los vientos, entre

<!-- INICIO TABLA 4-53 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|114| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-53: Intensidades máxima globales y por dirección de procedencia de los vientos, entre los meses julio-diciembre. Base****

| Col1 | Intensidad máxima del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Meses** | **Julio** | **Julio** | **Agosto** | **Agosto** | **Septiembre** | **Septiembre** | **Octubre** | **Octubre** | **Noviembre** | **Noviembre** | **Diciembre** | **Diciembre** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N ** | 0,743 | 1,441 | 0,869 | 1,686 | 0,600 | 1,165 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| **NNE** | 0,727 | 1,410 | 0,790 | 1,533 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| **NE** | 0,807 | 1,566 | 0,727 | 1,410 | 0,000 | 0,000 | 0,474 | 0,920 | 0,000 | 0,000 | 0,000 | 0,000 |
| **ENE** | 0,837 | 1,625 | 0,790 | 1,533 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| **E ** | 1,011 | 1,962 | 0,806 | 1,563 | 0,711 | 1,379 | 0,000 | 0,000 | 0,442 | 0,858 | 0,000 | 0,000 |
| **ESE** | 0,995 | 1,931 | 0,901 | 1,747 | 0,916 | 1,778 | 0,442 | 0,858 | 0,600 | 1,165 | 0,474 | 0,920 |
| **SE** | 0,964 | 1,870 | 1,122 | 2,176 | 0,901 | 1,747 | 0,774 | 1,502 | 0,822 | 1,594 | 0,843 | 1,635 |
| **SSE** | 1,074 | 2,084 | 0,980 | 1,900 | 1,043 | 2,023 | 1,090 | 2,115 | 0,901 | 1,747 | 1,027 | 1,992 |
| **S ** | 1,185 | 2,299 | 0,948 | 1,839 | 1,011 | 1,962 | 1,106 | 2,146 | 1,343 | 2,605 | 1,533 | 2,973 |
| **SSW** | 1,912 | 3,709 | 2,022 | 3,923 | 2,243 | 4,352 | 2,307 | 4,475 | 2,701 | 5,241 | 2,512 | 4,873 |
| **SW** | 2,322 | 4,505 | 2,117 | 4,107 | 2,307 | 4,475 | 2,480 | 4,812 | 2,607 | 5,057 | 2,591 | 5,027 |
| **WSW** | 1,770 | 3,433 | 2,133 | 4,138 | 2,085 | 4,046 | 2,165 | 4,199 | 2,038 | 3,954 | 1,580 | 3,065 |
| **W ** | 1,454 | 2,820 | 1,596 | 3,096 | 1,517 | 2,943 | 1,596 | 3,096 | 1,533 | 2,973 | 0,000 | 0,000 |
| **WNW** | 0,901 | 1,747 | 0,964 | 1,870 | 0,727 | 1,410 | 0,648 | 1,257 | 0,000 | 0,000 | 0,000 | 0,000 |
| **NW** | 0,758 | 1,471 | 0,964 | 1,870 | 0,664 | 1,287 | 0,632 | 1,226 | 0,000 | 0,000 | 0,000 | 0,000 |
| **NNW** | 0,743 | 1,441 | 0,853 | 1,655 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| **Global** | 2,322 | 4,505 | 2,133 | 4,138 | 2,307 | 4,475 | 2,480 | 4,812 | 2,701 | 5,241 | 2,591 | 5,027 |

<!-- Estadísticas: 19 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-53 -->

los meses julio-diciembre. Base de datos histórica. ............................................................ 114

Tabla 4-54: Intensidades promedio globales y por dirección de procedencia de los vientos,

<!-- INICIO TABLA 4-54 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|115| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-54: Intensidades promedio globales y por dirección de procedencia de los vientos, entre los meses enero-junio. Base de****

| Col1 | Intensidad promedio del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Meses** | **Enero** | **Enero** | **Febrero** | **Febrero** | **Marzo** | **Marzo** | **Abril** | **Abril** | **Mayo** | **Mayo** | **Junio** | **Junio** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N ** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,458 | 0,889 |
| **NNE** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,521 | 1,012 |
| **NE** | 0,000 | 0,000 | 0,474 | 0,920 | 0,000 | 0,000 | 0,000 | 0,000 | 0,593 | 1,149 | 0,607 | 1,178 |
| **ENE** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,695 | 1,349 | 0,638 | 1,238 |
| **E ** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,648 | 1,257 | 0,635 | 1,232 |
| **ESE** | 0,560 | 1,087 | 0,000 | 0,000 | 0,000 | 0,000 | 0,674 | 1,308 | 0,612 | 1,188 | 0,702 | 1,362 |
| **SE** | 0,562 | 1,091 | 0,660 | 1,280 | 0,666 | 1,291 | 0,610 | 1,184 | 0,670 | 1,300 | 0,683 | 1,324 |
| **SSE** | 0,676 | 1,312 | 0,718 | 1,393 | 0,653 | 1,267 | 0,682 | 1,324 | 0,700 | 1,359 | 0,724 | 1,404 |
| **S ** | 0,800 | 1,553 | 0,843 | 1,635 | 0,828 | 1,605 | 0,889 | 1,724 | 0,764 | 1,482 | 0,767 | 1,488 |
| **SSW** | 1,722 | 3,340 | 1,922 | 3,728 | 1,864 | 3,616 | 1,778 | 3,448 | 1,263 | 2,450 | 1,036 | 2,009 |
| **SW** | 1,964 | 3,811 | 1,984 | 3,849 | 1,897 | 3,680 | 1,851 | 3,590 | 1,657 | 3,214 | 1,464 | 2,840 |
| **WSW** | 0,986 | 1,913 | 1,264 | 2,452 | 1,174 | 2,277 | 0,948 | 1,839 | 1,339 | 2,598 | 1,311 | 2,544 |
| **W ** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,932 | 1,808 |
| **WNW** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,779 | 1,512 |
| **NW** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,593 | 1,149 |
| **NNW** | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| **Global** | 1,457 | 2,827 | 1,544 | 2,995 | 1,411 | 2,738 | 1,296 | 2,513 | 1,101 | 2,135 | 1,019 | 1,977 |

<!-- Estadísticas: 19 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-54 -->

entre los meses enero-junio. Base de datos histórica. ........................................................ 115

Tabla 4-55: Intensidades promedio globales y por dirección de procedencia de los vientos,

<!-- INICIO TABLA 4-55 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|116| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-55: Intensidades promedio globales y por dirección de procedencia de los vientos, entre los meses julio-diciembre.****

| Col1 | Intensidad promedio del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Meses** | **Julio** | **Julio** | **Agosto** | **Agosto** | **Septiembre** | **Septiembre** | **Octubre** | **Octubre** | **Noviembre** | **Noviembre** | **Diciembre** | **Diciembre** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N ** | 0,587 | 1,138 | 0,747 | 1,449 | 0,600 | 1,165 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| **NNE** | 0,594 | 1,153 | 0,648 | 1,257 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| **NE** | 0,597 | 1,158 | 0,623 | 1,208 | 0,000 | 0,000 | 0,474 | 0,920 | 0,000 | 0,000 | 0,000 | 0,000 |
| **ENE** | 0,650 | 1,261 | 0,735 | 1,425 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| **E ** | 0,677 | 1,314 | 0,652 | 1,264 | 0,648 | 1,257 | 0,000 | 0,000 | 0,442 | 0,858 | 0,000 | 0,000 |
| **ESE** | 0,698 | 1,355 | 0,689 | 1,336 | 0,713 | 1,384 | 0,395 | 0,766 | 0,528 | 1,024 | 0,474 | 0,920 |
| **SE** | 0,685 | 1,330 | 0,743 | 1,442 | 0,753 | 1,461 | 0,640 | 1,241 | 0,666 | 1,292 | 0,610 | 1,183 |
| **SSE** | 0,742 | 1,440 | 0,711 | 1,379 | 0,772 | 1,498 | 0,721 | 1,398 | 0,640 | 1,241 | 0,680 | 1,319 |
| **S ** | 0,743 | 1,442 | 0,711 | 1,379 | 0,758 | 1,470 | 0,704 | 1,366 | 0,680 | 1,319 | 0,780 | 1,512 |
| **SSW** | 1,001 | 1,941 | 0,968 | 1,879 | 1,044 | 2,025 | 1,108 | 2,150 | 1,217 | 2,360 | 1,478 | 2,867 |
| **SW** | 1,380 | 2,677 | 1,361 | 2,640 | 1,459 | 2,830 | 1,617 | 3,137 | 1,848 | 3,586 | 1,960 | 3,803 |
| **WSW** | 1,297 | 2,517 | 1,438 | 2,790 | 1,351 | 2,620 | 1,363 | 2,644 | 1,488 | 2,886 | 1,388 | 2,693 |
| **W ** | 1,055 | 2,047 | 1,090 | 2,114 | 0,988 | 1,917 | 1,038 | 2,014 | 1,390 | 2,697 | 0,000 | 0,000 |
| **WNW** | 0,551 | 1,069 | 0,784 | 1,521 | 0,727 | 1,410 | 0,542 | 1,052 | 0,000 | 0,000 | 0,000 | 0,000 |
| **NW** | 0,656 | 1,272 | 0,793 | 1,539 | 0,664 | 1,287 | 0,545 | 1,057 | 0,000 | 0,000 | 0,000 | 0,000 |
| **NNW** | 0,632 | 1,226 | 0,685 | 1,329 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| **Global** | 1,026 | 1,990 | 1,085 | 2,105 | 1,200 | 2,327 | 1,256 | 2,436 | 1,303 | 2,527 | 1,398 | 2,712 |

<!-- Estadísticas: 19 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-55 -->

entre los meses julio-diciembre. Base de datos histórica. ................................................... 116

Tabla 4-56: Tabla de incidencia del viento, verano promedio. Base de datos histórica. ...... 118

<!-- INICIO TABLA 4-56 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|118| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-56: Tabla de incidencia del viento, verano promedio. Base de datos histórica.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N** | - | - | - | - | - | - | - | 0,000 |
| **NNE** | - | - | - | - | - | - | - | 0,000 |
| **NE** | - | 0,046 | - | - | - | - | - | 0,046 |
| **ENE** | - | - | - | - | - | - | - | 0,000 |
| **E** | - | - | - | - | - | - | - | 0,000 |
| **ESE** | - | 0,183 | - | - | - | - | - | 0,183 |
| **SE** | - | 2,015 | - | - | - | - | - | 2,015 |
| **SSE** | - | 8,104 | - | - | - | - | - | 8,104 |
| **S** | - | 24,496 | 1,007 | - | - | - | - | 25,504 |
| **SSW** | - | 11,310 | 26,282 | - | - | - | - | 37,592 |
| **SW** | - | 3,571 | 22,253 | - | - | - | - | 25,824 |
| **WSW** | - | 0,458 | 0,183 | - | - | - | - | 0,641 |
| **W** | - | - | - | - | - | - | - | 0,000 |
| **WNW** | - | - | - | - | - | - | - | 0,000 |
| **NW** | - | - | - | - | - | - | - | 0,000 |
| **NNW** | - | - | - | - | - | - | - | 0,000 |
| **Calmas** | 0,092 | - | - | - | - | - | - | 0,092 |
| **Sub Total**<br>**(%)** <br> | 0,092<br> | 50,183<br> | 49,725<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 2.184 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-56 -->


Tabla 4-57: Tabla de incidencia del viento, otoño promedio. Base de datos histórica. ........ 119

<!-- INICIO TABLA 4-57 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|119| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-57: Tabla de incidencia del viento, otoño promedio. Base de datos histórica.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N** | - | 0,091 | - | - | - | - | - | 0,091 |
| **NNE** | - | 0,091 | - | - | - | - | - | 0,091 |
| **NE** | - | 0,272 | - | - | - | - | - | 0,272 |
| **ENE** | - | 0,543 | - | - | - | - | - | 0,543 |
| **E** | - | 0,906 | - | - | - | - | - | 0,906 |
| **ESE** | - | 3,034 | - | - | - | - | - | 3,034 |
| **SE** | - | 7,382 | - | - | - | - | - | 7,382 |
| **SSE** | - | 15,263 | - | - | - | - | - | 15,263 |
| **S** | - | 18,524 | 1,223 | - | - | - | - | 19,746 |
| **SSW** | - | 10,779 | 13,859 | - | - | - | - | 24,638 |
| **SW** | - | 4,121 | 18,976 | - | - | - | - | 23,098 |
| **WSW** | - | 2,400 | 1,857 | - | - | - | - | 4,257 |
| **W** | - | 0,272 | - | - | - | - | - | 0,272 |
| **WNW** | - | 0,136 | - | - | - | - | - | 0,136 |
| **NW** | - | 0,091 | - | - | - | - | - | 0,091 |
| **NNW** | - | - | - | - | - | - | - | 0,000 |
| **Calmas** | 0,181 | - | - | - | - | - | - | 0,181 |
| **Sub Total**<br>**(%)** <br> | 0,181<br> | 63,904<br> | 35,915<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 2.208 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-57 -->


Tabla 4-58: Tabla de incidencia del viento, invierno promedio. Base de datos histórica. .... 120

<!-- INICIO TABLA 4-58 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|120| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-58: Tabla de incidencia del viento, invierno promedio. Base de datos histórica.****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N** | - | 0,725 | - | - | - | - | - | 0,725 |
| **NNE** | - | 0,815 | - | - | - | - | - | 0,815 |
| **NE** | - | 0,770 | - | - | - | - | - | 0,770 |
| **ENE** | - | 0,543 | - | - | - | - | - | 0,543 |
| **E** | - | 1,359 | - | - | - | - | - | 1,359 |
| **ESE** | - | 3,487 | - | - | - | - | - | 3,487 |
| **SE** | - | 7,473 | - | - | - | - | - | 7,473 |
| **SSE** | - | 9,013 | - | - | - | - | - | 9,013 |
| **S** | - | 8,786 | - | - | - | - | - | 8,786 |
| **SSW** | - | 12,545 | 2,627 | - | - | - | - | 15,172 |
| **SW** | - | 12,228 | 17,799 | - | - | - | - | 30,027 |
| **WSW** | - | 6,748 | 9,466 | - | - | - | - | 16,214 |
| **W** | - | 2,446 | 0,408 | - | - | - | - | 2,853 |
| **WNW** | - | 1,087 | - | - | - | - | - | 1,087 |
| **NW** | - | 0,725 | - | - | - | - | - | 0,725 |
| **NNW** | - | 0,906 | - | - | - | - | - | 0,906 |
| **Calmas** | 0,045 | - | - | - | - | - | - | 0,045 |
| **Sub Total**<br>**(%)** <br> | 0,045<br> | 69,656<br> | 30,299<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 2.208 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-58 -->


Tabla 4-59: Tabla de incidencia del viento, primavera promedio. Base de datos histórica. . 121

<!-- INICIO TABLA 4-59 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|121| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-59: Tabla de incidencia del viento, primavera promedio. Base de datos****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N** | - | 0,046 | - | - | - | - | - | 0,046 |
| **NNE** | - | - | - | - | - | - | - | 0,000 |
| **NE** | - | 0,046 | - | - | - | - | - | 0,046 |
| **ENE** | - | - | - | - | - | - | - | 0,000 |
| **E** | - | 0,092 | - | - | - | - | - | 0,092 |
| **ESE** | - | 0,458 | - | - | - | - | - | 0,458 |
| **SE** | - | 1,603 | - | - | - | - | - | 1,603 |
| **SSE** | - | 7,830 | - | - | - | - | - | 7,830 |
| **S** | - | 14,469 | - | - | - | - | - | 14,469 |
| **SSW** | - | 17,857 | 9,753 | - | - | - | - | 27,610 |
| **SW** | - | 8,791 | 27,244 | - | - | - | - | 36,035 |
| **WSW** | - | 4,258 | 6,456 | - | - | - | - | 10,714 |
| **W** | - | 0,595 | 0,137 | - | - | - | - | 0,733 |
| **WNW** | - | 0,183 | - | - | - | - | - | 0,183 |
| **NW** | - | 0,137 | - | - | - | - | - | 0,137 |
| **NNW** | - | - | - | - | - | - | - | 0,000 |
| **Calmas** | 0,046 | - | - | - | - | - | - | 0,046 |
| **Sub Total**<br>**(%)** <br> | 0,046<br> | 56,364<br> | 43,590<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 2.184 |

<!-- Estadísticas: 22 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-59 -->


Tabla 4-60: Intensidades máxima globales y por dirección de procedencia de los vientos, por

<!-- INICIO TABLA 4-60 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|125| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-60: Intensidades máxima globales y por dirección de procedencia de los****

| Col1 | Intensidad máxima del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Estaciones** | **Verano** | **Verano** | **Otoño** | **Otoño** | **Invierno** | **Invierno** | **Primavera** | **Primavera** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N** | 0,000 | 0,000 | 0,553 | 1,073 | 0,869 | 1,686 | 0,600 | 1,165 |
| **NNE** | 0,000 | 0,000 | 0,664 | 1,287 | 0,790 | 1,533 | 0,000 | 0,000 |
| **NE** | 0,474 | 0,920 | 0,853 | 1,655 | 0,807 | 1,566 | 0,474 | 0,920 |
| **ENE** | 0,000 | 0,000 | 1,043 | 2,023 | 0,837 | 1,625 | 0,000 | 0,000 |
| **E** | 0,000 | 0,000 | 0,980 | 1,900 | 1,011 | 1,962 | 0,711 | 1,379 |
| **ESE** | 0,761 | 1,477 | 1,059 | 2,054 | 0,995 | 1,931 | 0,774 | 1,502 |
| **SE** | 0,934 | 1,811 | 1,074 | 2,084 | 1,122 | 2,176 | 0,843 | 1,635 |
| **SSE** | 1,122 | 2,176 | 1,090 | 2,115 | 1,074 | 2,084 | 1,090 | 2,115 |
| **S** | 2,198 | 4,263 | 1,912 | 3,709 | 1,232 | 2,391 | 1,343 | 2,605 |
| **SSW** | 2,930 | 5,683 | 2,780 | 5,394 | 2,243 | 4,352 | 2,701 | 5,241 |
| **SW** | 2,858 | 5,544 | 2,559 | 4,965 | 2,322 | 4,505 | 2,607 | 5,057 |
| **WSW** | 1,738 | 3,372 | 1,849 | 3,586 | 2,133 | 4,138 | 2,165 | 4,199 |
| **W** | 0,000 | 0,000 | 1,327 | 2,575 | 1,596 | 3,096 | 1,596 | 3,096 |
| **WNW** | 0,000 | 0,000 | 1,011 | 1,962 | 0,964 | 1,870 | 0,727 | 1,410 |
| **NW** | 0,000 | 0,000 | 0,664 | 1,287 | 0,964 | 1,870 | 0,664 | 1,287 |
| **NNW** | 0,000 | 0,000 | 0,000 | 0,000 | 0,853 | 1,655 | 0,000 | 0,000 |
| **Global** | 2,930 | 5,683 | 2,780 | 5,394 | 2,322 | 4,505 | 2,701 | 5,241 |

<!-- Estadísticas: 19 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-60 -->


estaciones. Base de datos histórica. ................................................................................... 125

Tabla 4-61: Intensidades promedio globales y por dirección de procedencia de los vientos, por

<!-- INICIO TABLA 4-61 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|126| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-61: Intensidades promedio globales y por dirección de procedencia de los****

| Col1 | Intensidad promedio del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Estaciones** | **Verano** | **Verano** | **Otoño** | **Otoño** | **Invierno** | **Invierno** | **Primavera** | **Primavera** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N** | 0,000 | 0,000 | 0,545 | 1,057 | 0,638 | 1,238 | 0,600 | 1,165 |
| **NNE** | 0,000 | 0,000 | 0,600 | 1,165 | 0,588 | 1,141 | 0,000 | 0,000 |
| **NE** | 0,474 | 0,920 | 0,640 | 1,241 | 0,593 | 1,151 | 0,474 | 0,920 |
| **ENE** | 0,000 | 0,000 | 0,666 | 1,292 | 0,664 | 1,287 | 0,000 | 0,000 |
| **E** | 0,000 | 0,000 | 0,662 | 1,284 | 0,645 | 1,252 | 0,577 | 1,119 |
| **ESE** | 0,539 | 1,045 | 0,657 | 1,275 | 0,693 | 1,345 | 0,547 | 1,061 |
| **SE** | 0,596 | 1,156 | 0,673 | 1,306 | 0,709 | 1,376 | 0,639 | 1,240 |
| **SSE** | 0,684 | 1,327 | 0,693 | 1,345 | 0,739 | 1,433 | 0,674 | 1,307 |
| **S** | 0,821 | 1,593 | 0,833 | 1,616 | 0,755 | 1,465 | 0,711 | 1,378 |
| **SSW** | 1,812 | 3,515 | 1,536 | 2,979 | 1,013 | 1,964 | 1,222 | 2,371 |
| **SW** | 1,938 | 3,760 | 1,688 | 3,275 | 1,417 | 2,749 | 1,745 | 3,385 |
| **WSW** | 1,158 | 2,247 | 1,316 | 2,553 | 1,364 | 2,647 | 1,401 | 2,719 |
| **W** | 0,000 | 0,000 | 1,009 | 1,957 | 1,063 | 2,062 | 1,024 | 1,987 |
| **WNW** | 0,000 | 0,000 | 0,779 | 1,512 | 0,706 | 1,370 | 0,589 | 1,142 |
| **NW** | 0,000 | 0,000 | 0,593 | 1,149 | 0,742 | 1,439 | 0,585 | 1,134 |
| **NNW** | 0,000 | 0,000 | 0,000 | 0,000 | 0,666 | 1,293 | 0,000 | 0,000 |
| **Global** | 1,467 | 2,847 | 1,181 | 2,292 | 1,086 | 2,107 | 1,295 | 2,513 |

<!-- Estadísticas: 19 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-61 -->


estaciones. Base de datos histórica. ................................................................................... 126

Tabla 4-62: Tabla de incidencia del viento; Intervalo [0 - 4[ hrs. Base de datos histórica. .. 128

<!-- INICIO TABLA 4-62 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- (Tabla 4-69) se estima que el mayor valor medio corresponde a 2,378 m/s (4,614 nudos) durante el intervalo (16 - 20 hrs) y desde la dirección SSW. En general, las menores intensidades se asocian al primer y cuarto cuadrante y, en contraste, las mayores magnitudes se generan en el tercer cuadrante. -->

**Tabla 4-62: Tabla de incidencia del viento; Intervalo [0 - 4[ hrs. Base de datos****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N** | - | 2,340 | 0,402 | - | - | - | - | 2,742 |
| **NNE** | - | 1,180 | 0,027 | - | - | - | - | 1,207 |
| **NE** | - | 0,738 | 0,007 | - | - | - | - | 0,744 |
| **ENE** | - | 0,717 | 0,040 | - | - | - | - | 0,758 |
| **E** | - | 0,798 | 0,013 | - | - | - | - | 0,811 |
| **ESE** | - | 0,972 | 0,054 | - | - | - | - | 1,026 |
| **SE** | - | 1,207 | 0,094 | - | - | - | - | 1,301 |
| **SSE** | - | 3,192 | 0,691 | - | - | - | - | 3,882 |
| **S** | - | 16,374 | 14,007 | 0,020 | - | - | - | 30,401 |
| **SSW** | - | 15,791 | 13,652 | - | - | - | - | 29,442 |
| **SW** | - | 7,825 | 4,687 | - | - | - | - | 12,512 |
| **WSW** | - | 3,534 | 0,127 | - | - | - | - | 3,661 |
| **W** | - | 2,508 | 0,007 | - | - | - | - | 2,514 |
| **WNW** | - | 1,100 | 0,013 | - | - | - | - | 1,113 |
| **NW** | - | 0,939 | 0,007 | - | - | - | - | 0,945 |
| **NNW** | - | 1,770 | 0,194 | - | - | - | - | 1,965 |
| **VRB** | - | 1,080 | - | - | - | - | - | 1,080 |
| **Calmas** | 3,896 | - | - | - | - | - | - | 3,896 |
| **Sub Total**<br>**(%)** <br> | 3,896<br> | 62,062<br> | 34,022<br> | 0,020<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 14.914 |

<!-- Estadísticas: 23 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-62 -->


Tabla 4-63: Tabla de incidencia del viento; Intervalo [4 - 8[ hrs. Base de datos histórica. .. 129

<!-- INICIO TABLA 4-63 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|129| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-63: Tabla de incidencia del viento; Intervalo [4 - 8[ hrs. Base de datos****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N** | - | 3,454 | 0,483 | - | - | - | - | 3,937 |
| **NNE** | - | 2,408 | 0,107 | - | - | - | - | 2,515 |
| **NE** | - | 1,952 | 0,020 | - | - | - | - | 1,972 |
| **ENE** | - | 2,314 | 0,020 | - | - | - | - | 2,334 |
| **E** | - | 4,728 | 0,148 | - | - | - | - | 4,876 |
| **ESE** | - | 4,675 | 0,349 | - | - | - | - | 5,023 |
| **SE** | - | 4,708 | 0,161 | - | - | - | - | 4,869 |
| **SSE** | - | 6,881 | 0,315 | - | - | - | - | 7,197 |
| **S** | - | 17,860 | 3,253 | - | - | - | - | 21,113 |
| **SSW** | - | 11,938 | 2,233 | - | - | - | - | 14,172 |
| **SW** | - | 4,977 | 0,423 | - | - | - | - | 5,399 |
| **WSW** | - | 2,676 | 0,020 | - | - | - | - | 2,696 |
| **W** | - | 2,468 | - | - | - | - | - | 2,468 |
| **WNW** | - | 1,133 | - | - | - | - | - | 1,133 |
| **NW** | - | 1,335 | 0,027 | - | - | - | - | 1,362 |
| **NNW** | - | 1,992 | 0,094 | - | - | - | - | 2,086 |
| **VRB** | - | 2,475 | - | - | - | - | - | 2,475 |
| **Calmas** | 14,373 | - | - | - | - | - | - | 14,373 |
| **Sub Total**<br>**(%)** <br> | 14,373<br> | 77,975<br> | 7,653<br> | 0,000<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 14.910 |

<!-- Estadísticas: 23 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-63 -->


Tabla 4-64: Tabla de incidencia del viento; Intervalo [8 - 12[ hrs. Base de datos histórica. 130

<!-- INICIO TABLA 4-64 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|130| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-64: Tabla de incidencia del viento; Intervalo [8 - 12[ hrs. Base de datos****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N** | - | 1,958 | 0,141 | - | - | - | - | 2,099 |
| **NNE** | - | 1,737 | 0,060 | - | - | - | - | 1,797 |
| **NE** | - | 1,764 | 0,027 | - | - | - | - | 1,791 |
| **ENE** | - | 2,461 | 0,047 | - | - | - | - | 2,508 |
| **E** | - | 6,411 | 0,483 | 0,007 | - | - | - | 6,901 |
| **ESE** | - | 7,558 | 0,905 | - | - | - | - | 8,464 |
| **SE** | - | 7,223 | 0,637 | - | - | - | - | 7,860 |
| **SSE** | - | 9,000 | 0,577 | - | - | - | - | 9,577 |
| **S** | - | 16,753 | 2,944 | - | - | - | - | 19,697 |
| **SSW** | - | 9,872 | 1,717 | - | - | - | - | 11,589 |
| **SW** | - | 4,386 | 0,423 | - | - | - | - | 4,809 |
| **WSW** | - | 2,273 | 0,020 | - | - | - | - | 2,294 |
| **W** | - | 1,489 | - | - | - | - | - | 1,489 |
| **WNW** | - | 0,758 | 0,007 | - | - | - | - | 0,765 |
| **NW** | - | 0,624 | 0,013 | - | - | - | - | 0,637 |
| **NNW** | - | 0,885 | 0,020 | - | - | - | - | 0,905 |
| **VRB** | - | 2,669 | - | - | - | - | - | 2,669 |
| **Calmas** | 14,151 | - | - | - | - | - | - | 14,151 |
| **Sub Total**<br>**(%)** <br> | 14,151<br> | 77,822<br> | 8,021<br> | 0,007<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 14.911 |

<!-- Estadísticas: 23 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-64 -->


Tabla 4-65: Tabla de incidencia del viento; Intervalo [12 - 16[ hrs. Base de datos histórica.

<!-- INICIO TABLA 4-65 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|131| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-65: Tabla de incidencia del viento; Intervalo [12 - 16[ hrs. Base de datos****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N** | - | 2,212 | 0,127 | - | - | - | - | 2,340 |
| **NNE** | - | 1,609 | 0,060 | - | - | - | - | 1,669 |
| **NE** | - | 0,885 | 0,020 | - | - | - | - | 0,905 |
| **ENE** | - | 1,153 | - | - | - | - | - | 1,153 |
| **E** | - | 1,689 | 0,141 | - | 0,013 | - | - | 1,844 |
| **ESE** | - | 2,119 | 0,215 | - | - | - | - | 2,333 |
| **SE** | - | 2,119 | 0,188 | - | - | - | - | 2,306 |
| **SSE** | - | 3,560 | 0,275 | - | - | - | - | 3,835 |
| **S** | - | 8,233 | 2,963 | 0,034 | - | - | - | 11,230 |
| **SSW** | - | 7,763 | 11,987 | 0,215 | - | - | - | 19,965 |
| **SW** | - | 6,403 | 9,527 | 0,060 | - | - | - | 15,990 |
| **WSW** | - | 6,684 | 5,625 | 0,007 | - | - | - | 12,316 |
| **W** | - | 6,423 | 1,153 | - | - | - | - | 7,576 |
| **WNW** | - | 3,533 | 0,188 | - | - | - | - | 3,721 |
| **NW** | - | 2,501 | 0,054 | - | - | - | - | 2,554 |
| **NNW** | - | 2,326 | 0,161 | - | - | - | - | 2,487 |
| **VRB** | - | 1,911 | - | - | - | - | - | 1,911 |
| **Calmas** | 5,866 | - | - | - | - | - | - | 5,866 |
| **Sub Total**<br>**(%)** <br> | 5,866<br> | 61,122<br> | 32,683<br> | 0,315<br> | 0,013<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 14.916 |

<!-- Estadísticas: 23 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-65 -->


........................................................................................................................................... 131

Tabla 4-66: Tabla de incidencia del viento; Intervalo [16 - 20[ hrs. Base de datos histórica.

<!-- INICIO TABLA 4-66 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|132| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-66: Tabla de incidencia del viento; Intervalo [16 - 20[ hrs. Base de datos****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N** | - | 0,402 | 0,188 | - | - | - | - | 0,590 |
| **NNE** | - | 0,054 | 0,020 | - | - | - | - | 0,074 |
| **NE** | - | 0,007 | - | - | - | - | - | 0,007 |
| **ENE** | - | 0,007 | - | - | - | - | - | 0,007 |
| **E** | - | - | - | - | - | - | - | 0,000 |
| **ESE** | - | 0,007 | - | - | - | - | - | 0,007 |
| **SE** | - | - | - | - | - | - | - | 0,000 |
| **SSE** | - | 0,013 | 0,013 | - | - | - | - | 0,027 |
| **S** | - | 0,127 | 3,072 | 0,168 | - | - | - | 3,367 |
| **SSW** | - | 0,778 | 25,022 | 2,911 | - | - | - | 28,710 |
| **SW** | - | 1,885 | 25,659 | 1,234 | - | - | - | 28,777 |
| **WSW** | - | 4,185 | 17,698 | 0,094 | - | - | - | 21,977 |
| **W** | - | 5,124 | 4,654 | - | - | - | - | 9,778 |
| **WNW** | - | 2,327 | 0,892 | - | - | - | - | 3,219 |
| **NW** | - | 1,469 | 0,194 | - | - | - | - | 1,663 |
| **NNW** | - | 1,100 | 0,550 | - | - | - | - | 1,650 |
| **VRB** | - | 0,080 | 0,007 | - | - | - | - | 0,087 |
| **Calmas** | 0,060 | - | - | - | - | - | - | 0,060 |
| **Sub Total**<br>**(%)** <br> | 0,060<br> | 17,564<br> | 77,969<br> | 4,406<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 14.911 |

<!-- Estadísticas: 23 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-66 -->


........................................................................................................................................... 132

Tabla 4-67: Tabla de incidencia del viento; Intervalo [20 - 0[ hrs. Base de datos histórica. 133

<!-- INICIO TABLA 4-67 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|133| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-67: Tabla de incidencia del viento; Intervalo [20 - 0[ hrs. Base de datos****

| Intensidad<br>(m/s) | [0,00- | [0,28- | [1,39- | [3,06- | [5,28- | [7,78- | [10,56- | Sub<br>Total (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intensidad**<br>**(m/s)** | **0,28[** | **1,39[** | **3,06[** | **5,28[** | **7,78[** | **10,56[** | **13,61[** | **13,61[** |
| **Escala de**<br>**Beaufort** | **Calmas** | **Aire**<br>**Ligero** | **Brisa**<br>**Ligera** | **Brisa**<br>**Suave** | **Brisa**<br>**Moderada** | **Brisa**<br>**Fresca** | **Brisa**<br>**Fuerte** | **Brisa**<br>**Fuerte** |
| **N** | - | 0,657 | 0,101 | - | - | - | - | 0,758 |
| **NNE** | - | 0,107 | 0,007 | - | - | - | - | 0,114 |
| **NE** | - | 0,013 | - | - | - | - | - | 0,013 |
| **ENE** | - | 0,013 | - | - | - | - | - | 0,013 |
| **E** | - | 0,007 | - | - | - | - | - | 0,007 |
| **ESE** | - | - | - | - | - | - | - | 0,000 |
| **SE** | - | 0,007 | 0,007 | - | - | - | - | 0,013 |
| **SSE** | - | 0,054 | 0,121 | - | - | - | - | 0,174 |
| **S** | - | 1,201 | 9,195 | 0,429 | - | - | - | 10,825 |
| **SSW** | - | 3,977 | 37,954 | 2,609 | - | - | - | 44,541 |
| **SW** | - | 4,058 | 21,616 | 0,999 | - | - | - | 26,673 |
| **WSW** | - | 3,763 | 7,049 | 0,020 | - | - | - | 10,832 |
| **W** | - | 2,502 | 0,684 | - | - | - | - | 3,186 |
| **WNW** | - | 0,993 | 0,040 | - | - | - | - | 1,033 |
| **NW** | - | 0,711 | 0,034 | - | - | - | - | 0,744 |
| **NNW** | - | 0,644 | 0,154 | - | - | - | - | 0,798 |
| **VRB** | - | 0,107 | 0,013 | - | - | - | - | 0,121 |
| **Calmas** | 0,154 | - | - | - | - | - | - | 0,154 |
| **Sub Total**<br>**(%)** <br> | 0,154<br> | 18,813<br> | 76,975<br> | 4,058<br> | 0,000<br> | 0,000<br> | 0,000 | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **Total** | 100,000 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **N°**<br>**Datos** | 14.910 |

<!-- Estadísticas: 23 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-67 -->


Tabla 4-68: Intensidades máxima globales y por dirección de procedencia de los vientos, por

<!-- INICIO TABLA 4-68 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|138| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-68: Intensidades máxima globales y por dirección de procedencia de los vientos, por intervalos horarios. Base de datos****

| Col1 | Intensidad máxima del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intervalos (hrs)** | **[0 - 4[** | **[0 - 4[** | **[4 - 8[** | **[4 - 8[** | **[8 - 12[** | **[8 - 12[** | **[12 - 16[** | **[12 - 16[** | **[16 - 20[** | **[16 - 20[** | **[20 - 0[** | **[20 - 0[** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N** | 2,054 | 3,985 | 2,843 | 5,515 | 1,580 | 3,065 | 2,843 | 5,515 | 2,054 | 3,985 | 1,738 | 3,372 |
| **NNE** | 1,738 | 3,372 | 2,054 | 3,985 | 1,896 | 3,678 | 1,580 | 3,065 | 2,370 | 4,598 | 1,422 | 2,759 |
| **NE** | 1,422 | 2,759 | 1,896 | 3,678 | 1,422 | 2,759 | 1,422 | 2,759 | 0,948 | 1,839 | 0,632 | 1,226 |
| **ENE** | 1,896 | 3,678 | 1,422 | 2,759 | 1,580 | 3,065 | 1,264 | 2,452 | 0,790 | 1,533 | 0,632 | 1,226 |
| **E** | 1,422 | 2,759 | 2,370 | 4,598 | 4,739 | 9,194 | 5,529 | 10,726 | 0,000 | 0,000 | 0,474 | 0,920 |
| **ESE** | 2,054 | 3,985 | 2,054 | 3,985 | 2,212 | 4,291 | 2,370 | 4,598 | 0,790 | 1,533 | 0,000 | 0,000 |
| **SE** | 1,896 | 3,678 | 3,001 | 5,822 | 2,212 | 4,291 | 2,054 | 3,985 | 0,000 | 0,000 | 1,580 | 3,065 |
| **SSE** | 2,528 | 4,904 | 2,054 | 3,985 | 2,370 | 4,598 | 2,054 | 3,985 | 2,054 | 3,985 | 3,001 | 5,822 |
| **S** | 3,317 | 6,435 | 2,843 | 5,515 | 3,001 | 5,822 | 3,475 | 6,742 | 4,423 | 8,581 | 4,107 | 7,968 |
| **SSW** | 2,843 | 5,515 | 2,686 | 5,211 | 2,843 | 5,515 | 3,791 | 7,355 | 4,423 | 8,581 | 4,265 | 8,274 |
| **SW** | 3,001 | 5,822 | 2,528 | 4,904 | 3,001 | 5,822 | 3,633 | 7,048 | 4,107 | 7,968 | 4,107 | 7,968 |
| **WSW** | 1,738 | 3,372 | 1,422 | 2,759 | 1,580 | 3,065 | 3,159 | 6,128 | 3,475 | 6,742 | 3,475 | 6,742 |
| **W** | 1,580 | 3,065 | 1,106 | 2,146 | 0,948 | 1,839 | 1,896 | 3,678 | 2,528 | 4,904 | 2,212 | 4,291 |
| **WNW** | 1,422 | 2,759 | 0,948 | 1,839 | 1,738 | 3,372 | 2,212 | 4,291 | 1,896 | 3,678 | 2,843 | 5,515 |
| **NW** | 1,422 | 2,759 | 1,738 | 3,372 | 1,580 | 3,065 | 2,528 | 4,904 | 2,054 | 3,985 | 2,212 | 4,291 |
| **NNW** | 2,370 | 4,598 | 2,212 | 4,291 | 1,738 | 3,372 | 1,896 | 3,678 | 2,528 | 4,904 | 2,686 | 5,211 |
| **Global** | 3,317 | 6,435 | 3,001 | 5,822 | 4,739 | 9,194 | 5,529 | 10,726 | 4,423 | 8,581 | 4,265 | 8,274 |

<!-- Estadísticas: 19 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-68 -->


intervalos horarios. Base de datos histórica. ....................................................................... 138

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|7|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Tabla 4-69: Intensidades promedio globales y por dirección de procedencia de los vientos, por

<!-- INICIO TABLA 4-69 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|139| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-69: Intensidades promedio globales y por dirección de procedencia de los vientos, por intervalos horarios. Base de****

| Col1 | Intensidad promedio del viento | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Intervalos (hrs)** | **[0 - 4[** | **[0 - 4[** | **[4 - 8[** | **[4 - 8[** | **[8 - 12[** | **[8 - 12[** | **[12 - 16[** | **[12 - 16[** | **[16 - 20[** | **[16 - 20[** | **[20 - 0[** | **[20 - 0[** |
| **Direcciones** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** | **(m/s)** | **nudos** |
| **N** | 0,896 | 1,739 | 0,827 | 1,605 | 0,719 | 1,395 | 0,755 | 1,465 | 1,192 | 2,313 | 0,979 | 1,899 |
| **NNE** | 0,740 | 1,435 | 0,712 | 1,381 | 0,673 | 1,306 | 0,722 | 1,401 | 1,106 | 2,146 | 0,892 | 1,731 |
| **NE** | 0,740 | 1,436 | 0,657 | 1,274 | 0,656 | 1,272 | 0,682 | 1,324 | 0,948 | 1,839 | 0,553 | 1,073 |
| **ENE** | 0,702 | 1,362 | 0,625 | 1,212 | 0,675 | 1,309 | 0,609 | 1,182 | 0,790 | 1,533 | 0,474 | 0,920 |
| **E** | 0,620 | 1,203 | 0,667 | 1,294 | 0,755 | 1,464 | 0,772 | 1,498 | 0,000 | 0,000 | 0,474 | 0,920 |
| **ESE** | 0,724 | 1,404 | 0,747 | 1,449 | 0,843 | 1,635 | 0,825 | 1,601 | 0,790 | 1,533 | 0,000 | 0,000 |
| **SE** | 0,769 | 1,492 | 0,721 | 1,399 | 0,806 | 1,563 | 0,836 | 1,623 | 0,000 | 0,000 | 1,422 | 2,759 |
| **SSE** | 0,976 | 1,893 | 0,752 | 1,458 | 0,803 | 1,558 | 0,826 | 1,602 | 1,304 | 2,529 | 1,768 | 3,430 |
| **S** | 1,324 | 2,569 | 0,952 | 1,847 | 0,949 | 1,841 | 1,107 | 2,149 | 2,276 | 4,415 | 2,063 | 4,001 |
| **SSW** | 1,328 | 2,576 | 0,974 | 1,889 | 0,954 | 1,851 | 1,559 | 3,024 | 2,378 | 4,614 | 2,159 | 4,189 |
| **SW** | 1,214 | 2,356 | 0,832 | 1,614 | 0,818 | 1,586 | 1,496 | 2,902 | 2,086 | 4,047 | 1,995 | 3,870 |
| **WSW** | 0,794 | 1,540 | 0,649 | 1,260 | 0,624 | 1,211 | 1,295 | 2,513 | 1,777 | 3,448 | 1,622 | 3,146 |
| **W** | 0,600 | 1,165 | 0,545 | 1,058 | 0,525 | 1,019 | 0,974 | 1,889 | 1,335 | 2,591 | 1,067 | 2,071 |
| **WNW** | 0,592 | 1,149 | 0,532 | 1,032 | 0,504 | 0,979 | 0,859 | 1,666 | 1,189 | 2,307 | 0,882 | 1,712 |
| **NW** | 0,678 | 1,315 | 0,609 | 1,181 | 0,552 | 1,071 | 0,777 | 1,508 | 1,105 | 2,144 | 0,833 | 1,615 |
| **NNW** | 0,843 | 1,636 | 0,724 | 1,405 | 0,637 | 1,235 | 0,786 | 1,524 | 1,236 | 2,397 | 1,020 | 1,978 |
| **Global** | 1,128 | 2,189 | 0,692 | 1,342 | 0,702 | 1,362 | 1,115 | 2,163 | 1,967 | 3,816 | 1,963 | 3,808 |

<!-- Estadísticas: 19 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-69 -->


intervalos horarios. Base de datos histórica. ....................................................................... 139

Tabla 4-70 Lista de eventos máximos para clima extremo de vientos en las direcciones N, NE,
E y SE ................................................................................................................................ 141

Tabla 4-71 Lista de eventos máximos para clima extremo de vientos en direcciones S, SW, W
y NW ................................................................................................................................... 142

Tabla 4-72: Resumen de los parámetros de ajustes a la distribución. ................................. 143

<!-- INICIO TABLA 4-72 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La Tabla 4-72 señala los ajustes empleados para la distribución de cada dirección, donde se destacan elevados coeficientes de determinación, sobre 0,8, con excepción de la dirección E. El menor coeficiente (0,737) puede deberse a presencia de un valor de intensidad del viento disperso, respecto a los valores de los otros años. -->

**Tabla 4-72: Resumen de los parámetros de ajustes a la distribución.****

| Col1 | Índices | Col3 | Col4 |
| --- | --- | --- | --- |
| **Direcciones** | **R2 ** | **A ** | **B ** |
| **N ** | 0,908 | 0,341 | 1,929 |
| **NE** | 0,835 | 0,163 | 1,539 |
| **E ** | 0,737 | 0,855 | 1,844 |
| **SE** | 0,969 | 0,327 | 1,987 |
| **S ** | 0,871 | 0,371 | 3,590 |
| **SW** | 0,925 | 0,189 | 3,657 |
| **W ** | 0,938 | 0,494 | 2,308 |
| **NW** | 0,941 | 0,318 | 1,945 |

<!-- Estadísticas: 9 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. La proyección estimada por dirección se señala en la Tabla 4-73 y se ilustra en el Gráfico 4-54 para cada periodo de retorno. En la dirección E, por sentidos gráficos, se omitió de la ilustración -->
<!-- FIN TABLA 4-72 -->


Tabla 4-73: Tabla con la intensidad del viento asociada a distintos periodos de retorno, su

<!-- INICIO TABLA 4-73 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|144| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-73: Tabla con la intensidad del viento asociada a distintos periodos de retorno, su intervalo superior e inferior de ajuste.****

| Periodo de<br>retorno | 5 | Col3 | Col4 | 10 | Col6 | Col7 | 15 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Direcciones** | **Intervalo**<br>**Superior** | **Ajustes** | **Intervalo**<br>**Inferior** | **Intervalo**<br>**Superior** | **Ajustes** | **Intervalo**<br>**Inferior** | **Intervalo**<br>**Superior** | **Ajustes** | **Intervalo**<br>**Inferior** |
| **N ** | 3,289 | 2,441 | 1,592 | 3,545 | 2,697 | 1,848 | 3,690 | 2,841 | 1,993 |
| **NE** | 2,206 | 1,784 | 1,361 | 2,328 | 1,906 | 1,483 | 2,397 | 1,975 | 1,552 |
| **E ** | 5,486 | 3,126 | 0,765 | 6,128 | 3,767 | 1,407 | 6,490 | 4,129 | 1,769 |
| **SE** | 3,267 | 2,478 | 1,690 | 3,512 | 2,724 | 1,935 | 3,651 | 2,863 | 2,074 |
| **S ** | 5,088 | 4,146 | 3,204 | 5,367 | 4,425 | 3,483 | 5,524 | 4,582 | 3,640 |
| **SW** | 4,407 | 3,941 | 3,474 | 4,549 | 4,083 | 3,616 | 4,629 | 4,163 | 3,696 |
| **W ** | 4,258 | 3,049 | 1,839 | 4,629 | 3,420 | 2,210 | 4,839 | 3,629 | 2,419 |
| **NW** | 3,198 | 2,422 | 1,645 | 3,437 | 2,660 | 1,884 | 3,571 | 2,795 | 2,018 |
| **Periodo de**<br>**retorno** | **25** | **25** | **25** | **30** | **30** | **30** | <br> <br> | <br> <br> | <br> <br> |
| **Direcciones** | **Intervalo**<br>**Superior** | **Ajustes** | **Intervalo**<br>**Inferior** | **Intervalo**<br>**Superior** | **Ajustes** | **Intervalo**<br>**Inferior** | <br> <br> <br><br><br> | <br> <br> <br><br><br> | <br> <br> <br><br><br> |
| **N ** | 3,869 | 3,020 | 2,172 | 3,932 | 3,084 | 2,235 | <br> <br> <br><br><br> | <br> <br> <br><br><br> | <br> <br> <br><br><br> |
| **NE** | 2,483 | 2,060 | 1,638 | 2,513 | 2,091 | 1,668 | <br> <br> <br><br><br> | <br> <br> <br><br><br> | <br> <br> <br><br><br> |
| **E ** | 6,939 | 4,578 | 2,218 | 7,097 | 4,737 | 2,377 | <br> <br> <br><br><br> | <br> <br> <br><br><br> | <br> <br> <br><br><br> |
| **SE** | 3,823 | 3,034 | 2,246 | 3,884 | 3,095 | 2,307 | <br> <br> <br><br><br> | <br> <br> <br><br><br> | <br> <br> <br><br><br> |
| **S ** | 5,719 | 4,776 | 3,834 | 5,787 | 4,845 | 3,903 | <br> <br> <br><br><br> | <br> <br> <br><br><br> | <br> <br> <br><br><br> |
| **SW** | 4,728 | 4,262 | 3,796 | 4,764 | 4,297 | 3,831 | <br> <br> <br><br><br> | <br> <br> <br><br><br> | <br> <br> <br><br><br> |
| **W ** | 5,098 | 3,889 | 2,679 | 5,190 | 3,980 | 2,771 | <br> <br> <br><br><br> | <br> <br> <br><br><br> | <br> <br> <br><br><br> |
| **NW** | 3,738 | 2,962 | 2,185 | 3,797 | 3,021 | 2,244 | <br> <br> | <br> <br> | <br> <br> |

<!-- Estadísticas: 19 filas, 10 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl -->
<!-- FIN TABLA 4-73 -->

intervalo superior e inferior de ajuste. ................................................................................. 144

**LISTADO DE FIGURAS**

Figura 1-1: Ubicación de los instrumentos meteorológicos. .................................................. 12

**LISTADO DE GRÁFICOS**

Gráfico 4-1: Registro vectorial del viento medido. Mediciones sector ITI............................... 23

Gráfico 4-2: Histograma de frecuencia relativa de la intensidad del viento. Mediciones sector

ITI. ........................................................................................................................................ 24

Gráfico 4-3: Histograma de frecuencia relativa de la dirección del viento. Mediciones sector ITI.

............................................................................................................................................. 24

Gráfico 4-4: Rosa de intensidad por dirección del viento. Mediciones sector ITI. .................. 25

Gráfico 4-5: Variación de la magnitud promedio y máxima del viento por dirección de
procedencia. Mediciones sector ITI. ...................................................................................... 27

Gráfico 4-6: Valores centrados de las componentes ortogonales junto a su componente
principal. Mediciones sector ITI. ............................................................................................ 28

Gráfico 4-7: Densidad espectral de las componentes U y V del viento. Mediciones sector ITI.

............................................................................................................................................. 29

Gráfico 4-8: Diagrama de vectores progresivos del viento registrado en el período. Mediciones

sector ITI. .............................................................................................................................. 30

Gráfico 4-9: Histogramas de intensidad del viento promedio entre los meses enero y junio.

Mediciones sector ITI. ........................................................................................................... 44

Gráfico 4-10: Histogramas de intensidad del viento promedio entre los meses julio y diciembre.

Base de datos histórica. ........................................................................................................ 45

Gráfico 4-11: Histogramas de dirección del viento promedio entre los meses enero y junio.

Base de datos histórica. ........................................................................................................ 46

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|8|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Gráfico 4-12: Histogramas de dirección del viento promedio entre los meses julio y diciembre.

Mediciones sector ITI. ........................................................................................................... 47

Gráfico 4-13: Rosa de los vientos entre los meses enero y junio. Mediciones sector ITI. ...... 48

Gráfico 4-14: Rosa de los vientos entre los meses julio y diciembre. Mediciones sector ITI. . 49

Gráfico 4-15: Histograma de intensidad del viento promedio en un ciclo anual. Mediciones

sector ITI. .............................................................................................................................. 50

Gráfico 4-16: Ocurrencia de la incidencia del viento por dirección en un ciclo anual. Mediciones

sector ITI. .............................................................................................................................. 50

Gráfico 4-17: Histogramas de intensidad del viento promedio por estación del año. Mediciones

sector ITI. .............................................................................................................................. 60

Gráfico 4-18: Histogramas de dirección del viento promedio por estación del año. Mediciones

sector ITI. .............................................................................................................................. 61

Gráfico 4-19: Rosa de los vientos entre estaciones. Mediciones sector ITI. .......................... 62

Gráfico 4-20: Histograma de frecuencia relativa de la intensidad del viento por intervalos

horarios. Mediciones sector ITI. ............................................................................................ 72

Gráfico 4-21: Histograma de frecuencia relativa de la dirección del viento por intervalos

horarios. Mediciones sector ITI. ............................................................................................ 73

Gráfico 4-22: Rosa de los vientos por intervalos. Mediciones sector ITI................................ 74

Gráfico 4-23: Histograma de intensidad del viento promedio en un ciclo diario. Mediciones

sector ITI. .............................................................................................................................. 75

Gráfico 4-24: Ocurrencia de la incidencia del viento por dirección en un ciclo diario. Mediciones

sector ITI. .............................................................................................................................. 75

Gráfico 4-25: Serie de tiempo de la intensidad y dirección del viento. Medición y base de dato
histórica, 2020-2021. ............................................................................................................ 79

Gráfico 4-26: Análisis excedencias (izquierda) y cuantil-cuantil (derecha) de la intensidad del
viento (arriba) y dirección del viento (abajo) en la serie histórica vs serie medida. Medición y
base de dato histórica, 2020-2021. ....................................................................................... 80

Gráfico 4-27: Análisis excedencias (izquierda) y cuantil-cuantil (derecha) de la componente U
(arriba) y componente V (abajo) del viento en la serie histórica vs serie medida. Medición y
base de dato histórica, 2020-2021. ....................................................................................... 81

Gráfico 4-28: Correlación cruzada de las componentes ortogonales del viento. Medición y base
de dato histórica, 2020-2021. ................................................................................................ 83

Gráfico 4-29: Comparación entre espectros de la componente U (izquierda) y de la
componente V (derecha). Medición y base de dato histórica, 2020-2021. ............................ 84

Gráfico 4-30: Registro vectorial del viento. Base de datos histórica. ..................................... 86

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|9|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Gráfico 4-31: Histograma de frecuencia relativa de la intensidad del viento. Base de datos

histórica. ............................................................................................................................... 87

Gráfico 4-32: Histograma de frecuencia relativa de la dirección del viento. Base de datos

histórica ................................................................................................................................ 87

Gráfico 4-33: Rosa de intensidad por dirección del viento. Base de datos histórica. ............. 88

Gráfico 4-34: Variación de la magnitud promedio y máxima del viento por dirección de
procedencia. Base de datos histórica. .................................................................................. 90

Gráfico 4-35: Valores centrados de las componentes ortogonales junto a su componente
principal. Base de datos histórica.......................................................................................... 91

Gráfico 4-36: Densidad espectral de las componentes U y V del viento. Base de datos histórica.

............................................................................................................................................. 92

Gráfico 4-37: Histogramas de intensidad del viento promedio entre los meses enero y junio.

Base de datos histórica. ...................................................................................................... 106

Gráfico 4-38: Histogramas de intensidad del viento promedio entre los meses julio y diciembre.

Base de datos histórica. ...................................................................................................... 107

Gráfico 4-39: Histogramas de dirección del viento promedio entre los meses enero y junio.

Base de datos histórica. ...................................................................................................... 108

Gráfico 4-40: Histogramas de dirección del viento promedio entre los meses julio y diciembre.

Base de datos histórica. ...................................................................................................... 109

Gráfico 4-41: Rosa de los vientos entre los meses enero y junio. Base de datos histórica. 110

Gráfico 4-42: Rosa de los vientos entre los meses julio y diciembre. Base de datos histórica.

........................................................................................................................................... 111

Gráfico 4-43: Histograma de intensidad del viento promedio en un ciclo anual. Base de datos

histórica. ............................................................................................................................. 112

Gráfico 4-44: Ocurrencia de la incidencia del viento por dirección en un ciclo anual. Base de

datos histórica..................................................................................................................... 112

Gráfico 4-45: Histogramas de intensidad del viento promedio por estación del año. Base de

datos histórica..................................................................................................................... 122

Gráfico 4-46: Histogramas de dirección del viento promedio por estación del año. Base de

datos histórica..................................................................................................................... 123

Gráfico 4-47: Rosa de los vientos entre estaciones. Base de datos histórica. ..................... 124

Gráfico 4-48: Histograma de frecuencia relativa de la intensidad del viento por intervalos

horarios. Base de datos histórica. ....................................................................................... 134

Gráfico 4-49: Histograma de frecuencia relativa de la dirección del viento por intervalos

horarios. Base de datos histórica. ....................................................................................... 135

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|10|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Gráfico 4-50: Rosa de los vientos por intervalos. Base de datos histórica. ......................... 136

Gráfico 4-51: Histograma de intensidad del viento promedio en un ciclo diario. Base de datos

histórica. ............................................................................................................................. 137

Gráfico 4-52: Ocurrencia de la incidencia del viento por dirección en un ciclo diario. Base de

datos histórica..................................................................................................................... 137

Gráfico 4-53: Eventos seleccionados por direcciones para análisis del clima extremo. ....... 140

Gráfico 4-54: Curva de proyección de eventos extremos para diversos periodos de retorno.

........................................................................................................................................... 145

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|11|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 1 INTRODUCCIÓN

Ecotecnos S.A. ha sido contratado por Iquique Terminal Internacional S. A., para la realización
de un estudio orientado a determinar las características del viento, operacionales y de diseño,
al interior de Iquique Terminal Internacional, en adelante ITI, localizado en el Bahía de Iquique,
Región de Tarapacá.

Los vientos históricos analizados en el presente estudio, corresponden a una serie de más de
10 años de datos de magnitud y dirección del viento medida en el aeropuerto Diego Aracena,
en la Región de Tarapacá, considerándose el periodo de mediciones entre los años 2011 y
2020, además de algunos meses correspondientes al 2021. Para este estudio también se
contó con los vientos levantados en campo, durante un periodo superior a un año, en el sector
de ITI, como parte de los estudios de línea base medio ambiental. Con el fin de verificar la
similitud entre ambas bases de datos, las mediciones en el aeropuerto Diego Aracena
contienen el intervalo temporal de las mediciones en el sector de ITI. La información antes
descrita, así como los periodos que se han considerado para el presente estudio, se detallan

en la Tabla 1.1.

**Tabla 1.1: Ubicación aproximada de estaciones meteorológicas.**

|Estudio|Ubicación|Periodo|
|---|---|---|
|Mediciones de Meteorología<br>Diego Aracena|376.877E 7.727.300N|Desde el 01 enero del 2011 al 17 de<br>marzo del 2021|
|Mediciones de Meteorología ELB<br>Proyecto Extensión Norte Sitio<br>N° 4.|379.198E 7.765.592N1|Desde el 14 febrero del 2020 al 17<br>de marzo del 2021|

Fuente: Ecotecnos, 2021.

La ubicación general del sector de proyecto y de las estaciones antes señaladas, se presentan
en la Figura 1.1. La distancia que separa a ambas estaciones es aproximadamente de **38 Km**,
aproximadamente, motivo por el cual se ha estimado que la estación Diego Aracena se
encuentra cercana al sitio de proyecto; calificando el estudio de acuerdo al **numeral 3.5.4** del
instructivo **SHOA N° 3201**, como **Caso 2**, es decir, **se correlacionará la base de datos con**

**las mediciones efectuadas durante al menos 1 año** .

Es necesario señalar que las correlaciones esperadas para los estudios de vientos calificados
como Caso 2, deben presentar una similitud temporal adecuada y comportamiento estadístico
comparable entre ellas, situación que se cumple de acuerdo a los resultados que se ilustran
en los siguientes capítulos.

1 Según consigna en las Actas SHOA N°06/2020 y N°15/2020.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|12|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Figura 1-1: Ubicación de los instrumentos meteorológicos.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|13|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 2 OBJETIVOS 2.1 Generales

Determinar las características del viento reinante (operacional) y dominante (de diseño) de la
zona de estudio, de acuerdo con lo requerido por el Servicio Hidrográfico y Oceanográfico de
la Armada (SHOA), en su instructivo N° 3201 4a ed. 2019.

#### 2.2 Específicos

Para el desarrollo del objetivo antes planteado, se han elaborado una serie de tareas
específicas, las que se puntean a continuación:

- Correlacionar la base de datos histórica con el registro en la zona de proyecto.

- Determinar la relación estadística entre la base de datos histórica y el registro en la zona
de proyecto.

- Determinar y describir la estadística de la base de datos completa.

- Determinar y describir la estacionalidad mensual del viento para la zona de estudio.

- Determinar y describir la estacionalidad diaria del viento para la zona de estudio.

- Determinar y describir las características extremas de viento para la zona de estudio.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|14|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 3 MATERIALES Y MÉTODOS 3.1 Mediciones de Campo

Para analizar el comportamiento del viento, se utilizó el registro obtenido desde la estación
meteorológica marca HOBO modelo _Micro Station_ número de serie 20717417. La posición
inspeccionada y georreferenciada marcada por el GPS fue 20°12'12,15"S; 70°9'22,5"W
(Proyección UTM Datum WGS84, Zona 19 K: 7.765.592 N; 379.198 E, según consta en las
actas de inspección N° 06/2020 y N° 15/2020 (Anexo A). El instrumento midió datos por mayor
a un año con una frecuencia de registros de cada 5 minutos, capturando la dirección y
magnitud promedio del viento a una altura aproximada de 13 m.s.n.m., cuyos datos fueron
incluidos en el Anexo B. Se debe señalar que la variable tiempo de los datos registrados fue
transformada desde el huso horario en el cual fueron medidos al sistema UTC, para permitir
la comparación con los datos históricos.

**Tabla 3-1: Valores de declinación magnética obtenido para la estación de ITI.**

|Fecha|Valor (°)|Dirección|Modelo|
|---|---|---|---|
|01-02-2020|5,51|W|WMM|
|01-03-2020|5,53|W|WMM|
|01-04-2020|5,55|W|WMM|
|01-05-2020|5,57|W|WMM|
|01-06-2020|5,59|W|WMM|
|01-07-2020|5,60|W|WMM|
|01-08-2020|5,62|W|WMM|
|01-09-2020|5,64|W|WMM|
|01-10-2020|5,66|W|WMM|
|01-11-2020|5,68|W|WMM|
|01-12-2020|5,70|W|WMM|
|01-01-2021|5,72|W|WMM|
|01-02-2021|5,73|W|WMM|
|01-03-2021|5,75|W <br>|WMM<br>|
|**Promedio**|5,63|<br>|<br>|

Fuente: Ecotecnos, 2021.

La información recopilada se procesó para calcular indicadores estadísticos tales como los
valores promedios y máximos de toda la serie, y por dirección de procedencia. Los registros
de dirección del viento fueron corregidos empleando la aplicación de la declinación magnética
obtenida desde la _National Oceanic and Atmospheric Administration_ (NOAA), la cual es
determinada en base al _World Magnetic Model_ (WMM). Considerando que las diferencias entre
las declinaciones de los meses analizados fueron menores a 0,5° (Tabla 3-2), se consideró
obtener y emplear el valor medio, el cual correspondió a 5,63° W.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|15|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

La caracterización de las ocurrencias se realizó utilizando tablas bivariadas que contienen
dirección e intensidad del viento. La dirección se discretizó cada 22,5° y la intensidad,
siguiendo los rangos de la escala de Beaufort publicada por la Royal Meteorological Society
(2018), con leves modificaciones para calzar los rangos, dado que esta se encuentra
expresada en km/h con valores enteros. Los rangos, categorías y modificaciones empleadas
a dicha escala, se señalan la Tabla 3-2.

Es importante destacar, que a los registros cuyas intensidades fueron menores a 0,28 m/s, se
les descartó la direccionalidad, al ser consideradas Calmas en la escala de Beaufort (RMets,
2018) [2] y no presentar una dirección clara identificable. Por esta razón, del periodo de
mediciones empleado para caracterizar el sector de estudio, desde 14 de febrero del 2020
15:25 hasta 17 de marzo del 2021 17:50, se presenta un total de registros de 114.366 y se
contabilizó un total de 25.589 Calmas, lo que representa 22,375 % de los datos.

**Tabla 3-2: Categorización de la fuerza del viento, de acuerdo a su intensidad.**

|Col1|Royal Meteorological Society (2018)|Col3|Col4|Modificada|Col6|
|---|---|---|---|---|---|
|**Fuerza**<br>**Viento**|**Categoría**|**Intensidad**<br>**(km/h)**|**(m/s)**|**Categoría**|**(m/s)**|
|0|Calm|<1|<0,28|Calma|<0,28|
|1|Light Air|1-5|0,28 - 1,39|Aire Ligero|[0,28 - 1,39[|
|2|Light Breeze|6-11|1,67 - 3,06|Brisa Ligera|[1,39 - 3,06[|
|3|Gentle Breeze|12-19|3,33 - 5,28|Brisa Suave|[3,06 - 5,28[|
|4|Moderate Breeze|20-28|5,56 - 7,78|Brisa Moderada|[5,28 - 7,78[|
|5|Fresh Breeze|29-38|8,06 - 10,56|Brisa Fresca|[7,78 - 10,56[|
|6|Strong Breeze|38-49|10,56 - 13,61|Brisa Fuerte|[10,56 - 13,61[|
|7|Near Gale|50-61|13,89 - 16,94|Casi Vendaval|[13,61 - 16,94[|
|8|Gale|62-74|17,22 - 20,56|Vendaval|[16,94 - 20,56[|
|9|Strong Gale|75-88|20,83 - 24,44|Vendaval Fuerte|[20,56 - 24,44[|
|10|Storm|89-102|24,72 - 28,33|Tormenta|[24,44 - 28,33[|
|11|Violent Storm|103-117|28,61 - 32,50|Tormenta<br>Violenta|[28,33 - 32,50[|
|12|Hurricane|118 plus|≥32,50|Huracán|≥32,50|

Fuente: Elaboración Propia con información de la Royal Meteorological Society (2018).

Adicionalmente, se generaron diagramas de trazos, mediante un código de programación
propio que emplea la intensidad y dirección de cada dato, y, en función de la intensidad del
viento, la longitud del trazo es escalada y orientada a la dirección de incidencia que
corresponde. Finalmente, considerando la cantidad total de datos que conforman los registros,
y dado que la figura pretende ilustrar la distribución general de la base datos, se le dio un paso

2 Royal Meteorological Society: https://www.rmets.org/resource/beaufort-scale visitado 09-12-2020.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|16|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

temporal de 30 datos por trazo para las mediciones de campo y 45 datos por trazo a los vientos

de la base de datos históricos.

En cumplimiento con el **numeral 3.5.3** del instructivo **SHOA N°3201** (punto h), tanto para la
medición de campo como la serie histórica, se analizaron las componentes ortogonales
generadas a partir de sus respectiva magnitud y dirección del viento, obteniéndose
estadísticos como los valores máximos, medios y mínimos. Por otro lado, el porcentaje de
participación se obtuvo mediante el análisis de las componentes principales (PCA) sobre las
componentes ortogonales U y V centradas en el origen. Este estudio consistió en la obtención
de la componente principal que representase de la mejor forma la varianza expresada entre
las componentes ortogonales del viento. Para este fin, se emplearon las variables, según lo
mencionado en Emery & Thomson (1997), bajo la siguiente expresión matemática:

Cv−λv= 0

Donde:

C : Matriz de covarianza.
v : Vector propio.
λ : Valo propio.

A partir de esta se obtienen los valores propios (λ) que permiten detectar la componente
principal y la varianza total cubierta por ella. Por otro lado, el vector propio (v) indica la
participación de cada componente ortogonal dentro de la componente principal detectada. Los
cálculos mencionados para esta metodología se efectuaron mediante herramientas
matemáticas bajo scripts de programación desarrollados.

Por otro lado, debido a que la medición en el sector de ITI corresponde a un periodo levemente
superior a un año, los análisis asociados a las caracterizaciones mensuales y estacionales, no
pudieron ser efectuados sobre un año medio construido a partir de estos datos y, por esta
razón, solo se filtraron los datos, aplicando los análisis mencionados en el capítulo 3.3.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|17|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 3.2 Correlación de la base de datos.

La construcción del registro histórico requirió emplear los datos de la estación meteorológica
del aeropuerto Diego Aracena (Anexo C), los cuales fueron adquiridos a través de la Dirección
Meteorológica de Chile (DMC) [3] . A partir de esta base de datos, se recopiló un periodo superior
a 10 años de parámetros de velocidad en nudos y dirección con escala sexagesimal del viento.
La frecuencia de medición de esta estación fue horaria, manteniendo la variable tiempo en
UTC. Según señala el reporte generado por la entidad antes mencionada, la altura a la que se
encuentra el instrumento de medición es de 48 m.s.n.m, mientras que, las coordenadas
geográficas de referencia son 20°32’57,02” S y 70°10’52,00” W (Proyección UTM: 376.877 m
E, 7.727.300 m S, Datum WGS84, Zona 19 K). Cabe recalcar que el periodo de contraste
correspondió al intervalo de mediciones de campo.

Previo a realizar el proceso de correlación entre ambas fuentes de información, es necesario
efectuar un ajuste numérico que permita uniformar ambas mediciones a un mismo nivel vertical
de referencia. Para los análisis de este informe se empleó una altura de 10 m.s.n.m. y con el
fin de lograr dicha uniformidad, se ha utilizado la ecuación del perfil logarítmico, cuya expresión

matemática es:

V i (h) = V c ∗

Ln [h]
~~(~~ z 0 [)]

Ln( [h] z 0 [c] [)]

(1)

Donde:

V i (h) es la velocidad promedio del viento a la altura h que se desea conocer.

V c es la velocidad del viento conocida a una altura h c, también conocida.

z 0 es la altura de la rugosidad superficial.

El valor adoptado para la rugosidad superficial se definió según lo establecido por las
recomendaciones para obras marítimas (ROM 04-95). La Tabla 3.3 presenta un extracto de
rugosidades sugeridas en la referencia indicada. Para los datos históricos se aplicó una
rugosidad superficial de 5 m, debido a que la estación meteorológica en el sitio de estudio se
encuentra al interior del puerto, donde se emplazan variadas estructuras de gran altura que
pueden afectar el viento en dicho sector. Pese a lo mencionado, como los datos medidos en
el sector de ITI se encuentran a una altura aproximada de 13 m, se consideró que ya se
encuentran bajo la interacción de las estructuras portuarias y, para no subestimar la velocidad
del viento en dicho sector, se eligió una rugosidad superficial de 0,01 m.

3 https://climatologia.meteochile.gob.cl/application/informacion/ficha-de-estacion/200006 visitado el 20-06-2021

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|18|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 3.3: Extracto de la tabla de parámetros friccionales recomendadas por la ROM.**

|Tipo de Superficie|z (m)<br>0|
|---|---|
|I. Mar abierto y campo abierto llano sin<br>obstáculos (p.e. zonas costeras llanas,<br>desiertos, ...).|0,001 - 0,01|
|II. Mar con oleaje muy fuerte y campo<br>abierto, llano u ondulado, con obstáculos<br>dispersos (p.e. praderas, páramos, ...).|0,01 - 0,3|
|III. Superficies boscosas, campo con<br>obstáculos abundantes y pequeñas zonas<br>urbanas (obstáculos con alturas entre 9 y 15<br>m).|0,3 - 1,0|
|IV. Superficies con grandes y frecuentes<br>obstáculos, y grandes ciudades.|1,0 - 5,0|

Fuente: Ecotecnos, a partir de tabla contenida en el documento ROM-04-95-2.

Posteriormente, se generó una serie horaria de los registros de vientos medidos en el sitio del
proyecto, para hacerla comparable con la del registro histórico del aeropuerto Diego Aracena.
Finalmente, para analizar la similitud entre ambas, se consideraron los siguientes aspectos:

 - Forma de ambas señales en el tiempo (cualitativa).

 - Forma espectral de las componentes U y V de ambas señales.

 - Comparación cuantil-cuantil entre ambos registros.

 - Resumen estadístico entre ambas series.

 - Correlación cruzada de las componentes U y V de ambas señales con un desfase de

+/- 24 horas.

En el análisis de la correlación cruzada se consideró una varianza de [1 ] ⁄n (Contreras, 2001),
con n como el número de datos. Por esta razón, para una confianza del 95% se requiere

emplear 2 desviaciones estándar y, por ello, los limites de confianza es estimaron como ± [2] ⁄

~~√~~ n

Si bien, la base de datos histórica cuenta con el periodo en que se registraron vientos en la
zona de proyecto, es necesario que la correlación y comparación estadística entre ambas
señales sea cuantil - cuantil y no dato a dato, ya que el registro histórico presenta algunos
gaps propios de instrumentos que miden por largos periodos (p.e. mantenciones), además, las
direcciones variables, que son indicadas como “VRB” por la DMC, no permiten construir las
componentes U y V de dichos datos, al igual que lo que ocurre con el intervalo de “Calmas”.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|19|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Para obtener la forma espectral de las componentes ortogonales, se calculó la densidad
espectral, según las metodologías propuestas por Emery & Thomson (1997) y Hearn &
Metcalfe (2004) con 8 grados de libertad y un intervalo de confianza del 95%.

#### 3.3 Caracterización Estadística del registro de datos históricos

Posterior a la correlación de las series, la información histórica se procesó para calcular tablas
de incidencia e indicadores estadísticos, tales como, los valores promedios y máximos de toda
la serie y su dirección de procedencia. Además, los resultados se complementaron con rosas
direccionales e histogramas, para facilitar su visualización.

Lo anterior se realizó dando conformidad a lo señalado en el **numeral 3.5.3** del instructivo

**SHOA N°3201** (punto d), donde establece que el estudio deberá contar con una tabla que
posea, al menos, 8 columnas de direcciones y 6 filas de bandas de intensidad de viento,
conteniendo la frecuencia de ocurrencia en cada combinación, para el resumen de todo el
largo de la base de datos.

Junto a esto, se analizaron las componentes ortogonales U y V de la base de datos histórica
mediante los principales estadísticos, además de estimar las densidades espectrales de

ambas.

De la base de datos históricos, medida en la estación Diego Aracena, se consideró el periodo
entre el 01-01-2011 00:00 hasta el 17-03-2021 17:00, el cual presentó un total 18 gaps, tanto
para la intensidad como dirección, que fueron despreciados de los análisis efectuados en este
informe, quedando 89.472 datos para la caracterización estadística. De estos registros, 5.741
datos (6,417 %) presentaron una intensidad menor a 0,28 m/s, considerados como Calmas y
cuya direccionalidad fue descartada, mientras que, 1.244 datos (1,390 %) se encontraron con
un parámetro dirección variables (VRB).

Para dar cumplimiento a los puntos que requieren la caracterización mensual y estacional,
manteniendo un escenario estadístico conservador, se generó un año promedio (Anexo D) con
la serie histórica. Estos análisis fueron realizados mediante herramientas matemáticas bajo
scripts de programación desarrollados, que permitieron filtrar los datos con GAPs y agrupar el
total de registros (velocidad y dirección del viento) asociados al intervalo temporal definido
como cada 1 hora de cada día correspondiente a un año, identificando años bisiestos. De este
modo, si en algún intervalo temporal correspondiente a uno de los años presentó un GAP en
el registro, dicho dato fue removido del total. La velocidad del viento de cada paso temporal
del año medio se determinó como la media aritmética del total de los valores agrupados en el
respectivo intervalo. En el caso de la dirección, adicionalmente se retiraron los datos de
direcciones correspondientes a las calmas y todos aquellos carentes de dirección, para luego
descomponer los datos en sus componentes ortogonales (U y V), mediante las siguientes

relaciones:

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|20|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

U= −|v H [π]
| ∗sin[

[π] [π]

180 [∗∅] [MET] [(deg)] V= −|v] [H] [| ∗cos[]

180 [∗∅] [MET] [(deg)]]

Donde:

- U : Componente ortogonal del viento en el eje x .

- V : Componente ortogonal del viento en el eje y .

- v H : Intensidad del viento registrada.

- ∅ MET : Dirección del viento registrada.

Se debe mencionar que el signo negativo en la estimación de las componentes ortogonales
es requerido, pues la dirección del viento ( ∅ MET ) corresponde a la descripción meteorológica,
indicando el barlovento (desde donde viene), en cambio, las componentes ortogonales
describen el viento en forma vectorial [4] (hacia donde va). Por ello, la componente U es positiva
hacia el Este y la componente V es positiva hacia el Norte.

Luego, el promedio de las componentes, se obtuvo de acuerdo a lo siguiente:

n

U [̅ ] = [1]

n [∑U] [i]

i=1

n

V [̅ ] = [1]

n [∑V] [i]

i=1

Donde:

- U [̅] : Componente ortogonal promedio del viento, en el eje x .

- V [̅] : Componente ortogonal promedio del viento, en el eje y .

- n : El número efectivo de registros para cada paso temporal.

Una vez obtenidos los valores de U [̅] y V [̅], para cada intervalo temporal del año medio, se
reconstruyó la dirección, de acuerdo a las relaciones que se presentan a continuación:

θ [̅ ] =

[ 180 | ] [U] [̅ = 0 ∧ ] [V] [̅ > 0]

360 | U [̅ ] = 0 ∧ V [̅ ] < 0
270 | V [̅ ] = 0 ∧ U [̅ ] - 0
90 | V [̅ ] = 0 ∧ U [̅ ] < 0

{

X−180 | X> 180
X+ 180 | X< 180

Con:

X= ATAN2 [5] ( V [̅], U [̅] ) ∗ [180]

π [ | (] [U] [̅,] [ V] [̅) ≠(0,0)]

4 http://mst.nerc.ac.uk/wind_vect_convs.html
5 ATAN2, referencia a la función arcotangente entre dos parámetros. Esta nomenclatura se usa en varios programas de cálculo

como Microsoft Excel, Python, Matlab, entre otros.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|21|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**3.3.1 Análisis de ocurrencia para la estacionalidad mensual.**

Con el fin de dar cumplimiento al punto e del mismo numeral, mencionado anteriormente, se
realizaron tablas para cada mes que conforma el año medio construido desde los datos del
registro histórico. Este análisis se complementó con histogramas de intensidad y dirección,
además de rosas de vientos para cada mes en la serie. Juntos a esto, se agregaron gráficos
del ciclo anual para la intensidad y dirección del viento. Para cada mes se indicaron las
intensidades máximas y medias, correspondientes a cada dirección.

**3.3.2 Análisis de ocurrencia para la estacionalidad estacional.**

Para ahondar más aún en la estacionalidad anual del año medio obtenido del registro histórico,
se realizaron análisis estadísticos de las estaciones verano, otoño, invierno y primavera,
mediante tablas, histogramas de intensidad y dirección, así como también, rosas de vientos.
El periodo considerado para cada estación del año fue:

 - verano: 21 de diciembre 00:00 - 20 de marzo 23:00,

 - otoño: 21 de marzo 00:00 - 20 de junio 23:00,

 - invierno: 21 de junio 00:00 - 20 de septiembre 23:00

 - primavera: 21 de septiembre 00:00 - 20 de diciembre 23:00.

Para cada estación estudiada se definieron sus intensidades medias y máximas por cada

dirección.

**3.3.3 Análisis de ocurrencia para la estacionalidad diaria.**

Con el fin de analizar la estadística diaria de los vientos del registro histórico, de acuerdo a lo
que solicita el instructivo antes mencionado, se discretizó cada 4 horas y se generaron tablas
de incidencia, histogramas, y rosas de viento para intervalos de 6 horas discretas del día. Para
cada periodo de tiempo se determinaron las intensidades medias y máximas por dirección.
Los intervalos horarios empleados para este análisis fueron: [0-4 hrs [, [4-8 hrs [, [8-12 hrs [,

[12-16 hrs [, [16-20 hrs [ y [20-0 hrs [.

Adicionalmente se calculó el ciclo medio diario del registro completo, con la finalidad de
complementar dichos resultados.

Cabe señalar que, en estos análisis se contabilizó el largo de la base de datos completa, es
decir, se incluyeron las Calmas, aunque se siguió despreciando su direccionalidad.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|22|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 3.4 Clima Extremo de Vientos

Para definir el clima de diseño o extremo, se realizó un ajuste de la función de distribución del
tipo Gumbel a la serie de datos extremos. Los valores empleados sobre este ajuste se
seleccionaron a partir de la base de datos históricos, agrupados en 8 direcciones (cada 45°).
Sobre cada conjunto de direcciones se eligió el mayor valor de cada año y, por ello, se
seleccionó una cantidad de datos igual al número de años de registro por dirección, con la
finalidad de determinar escenarios conservadores. Para este análisis se emplearon los datos
entre los años 2011 y 2020 (10 años), debido a que el año 2021 no se encuentra completo y,
por tanto, se excluyeron estos datos para conservar datos representativos de años completos.

La probabilidad de no excedencia definida por la distribución Gumbel, tiene la siguiente
expresión:

B ~~[)]~~

P(v> V) = e [−e] [−(V−A]

A : Parámetro de escala.

B : Parámetro de ubicación.

V : Velocidad máxima del viento (m/s).

La probabilidad de no excedencia asociada a cada elemento de la muestra, se puede obtener
mediante la expresión de Gringorten, que describe de modo auxiliar la probabilidad de ploteo,
debido a que se ha demostrado que da resultados no sesgados (Goda, 1992); y cuya expresión
es la siguiente:

P o = F i = 1 − [i−0,44]

n+ 0,12

Donde:

i : Ubicación del dato, considerando orden decreciente.

n : Número de datos.

Efectuando un análisis de regresión lineal, utilizando el método de mínimos cuadrados, para
ajustar la función de los datos, se obtienen los valores de parámetros de cada distribución. Se
presenta el coeficiente de determinación ( R [2] ) que varía entre 0 y 1, e indica el porcentaje de
datos que el modelo es capaz de explicar, en relación con las observaciones.

Los periodos de retorno ( Tr ) considerados en el presente estudio fueron 5, 10, 15, 25 y 30
años y un intervalo de confianza del 95%.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|23|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 4 RESULTADOS

#### 4.1 Análisis y Caracterización Estadística de los Datos de Campo

**4.1.1 Estadística Descriptiva**

Las mediciones del viento en el sector de ITI, según su representación mediante chascones
(Gráfico 4-1), demuestra el predominio del viento desde el tercer cuadrante, en direcciones
cercanas al sur y, en forma más escasa, algunos vientos desde el primer y cuarto cuadrante.
La intensidad del viento registrado se presenta mediante histograma (Gráfico 4-2) y tabla de
incidencia (Tabla 4-1) donde, según escala de Beaufort, el viento se encuentra en las
categorías Calmas (0,00 - 0,28m/s), Aire Ligero (0,28 - 1,39 m/s), Brisa Ligera
(1,39 - 3,06 m/s) y Brisa Suave (3,06 - 5,28 m/s). El predominio se encuentra en la clase Aire
Ligero con una ocurrencia del 63,185 % de los casos, mientras que, la Brisa Ligera se
encuentra con una frecuencia de 14,412 % y la Brisa Suave en 0,029 %. De este registro el
22,375 % de los datos corresponden a Calmas.

En cuanto a la direccionalidad, esta se representa mediante tabla de incidencia (Tabla 4-1),
histograma (Gráfico 4-3) y rosa de viento (Gráfico 4-4). El viento registrado se concentra en el
tercer cuadrante, con el predominio en la dirección SSW (32,635 %) y, en segundo lugar, SW
(17,128 %). Por otro lado, ocurren frecuencias relevantes desde el norte, donde destaca la
dirección NNE (3,482 %).

Según lo señalado en el Gráfico 4-5 y la Tabla 4-2, el mayor registro de la serie corresponde
3,931 m/s (7,626 nudos) proveniente desde la dirección N. Es importante mencionar que, las
menores intensidades se generan en la proximidad de la dirección W. Respecto a los valores
medios por dirección, el mayor valor se estima desde la dirección SSW con 1,133 m/s
(2,197 nudos), aunque también desde la dirección N se presenta un importante valor igual a
1,107 m/s (1,461 nudos).

Fuente: Ecotecnos, 2021.
**Gráfico 4-1: Registro vectorial del viento medido. Mediciones sector ITI.**

En la Tabla 4-3 se presentan los principales estadísticos de las componentes ortogonales que
conforman el registro de datos. La componente U señala un valor medio de 0,381 m/s
indicando su predominio hacia la dirección E, encontrándose entre los valores 2,045 m/s y

- 2,692 m/s. En contraste, en la componente V se estima un valor medio de 0,497 m/s
reflejando su tendencia hacia la dirección N, dentro del rango construido con los valores

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|24|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

2,779 m/s y -3,866 m/s. Por otro lado, en relación a la desviación estándar, se evidencia una
mayor dispersión de los datos para la componente V (0,792 m/s), en comparación de la
componente U (0,498 m/s). Según lo ilustrado en el Gráfico 4-6, se determina la componente
principal (PCA) de los datos analizados, la cual representa sobre el 85 % de la varianza de los
datos y la componente V destacó por su participación (66,834 %), frente a la componente U
(33,166 %).

Fuente: Ecotecnos, 2021.
**Gráfico 4-2: Histograma de frecuencia relativa de la intensidad del viento. Mediciones**

**sector ITI.**

Fuente: Ecotecnos, 2021.
**Gráfico 4-3: Histograma de frecuencia relativa de la dirección del viento. Mediciones**

**sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|25|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Gráfico 4-4: Rosa de intensidad por dirección del viento. Mediciones sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|26|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-1: Tabla de incidencia del viento registrado. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|2,203|0,673|0,020|-|-|-|2,896|
|**NNE**|-|2,988|0,492|0,002|-|-|-|3,482|
|**NE**|-|2,085|0,143|-|-|-|-|2,228|
|**ENE**|-|2,412|0,429|-|-|-|-|2,841|
|**E **|-|0,716|0,021|-|-|-|-|0,737|
|**ESE**|-|0,632|0,042|-|-|-|-|0,674|
|**SE**|-|0,561|0,010|-|-|-|-|0,571|
|**SSE**|-|0,622|0,010|-|-|-|-|0,632|
|**S **|-|1,971|0,106|-|-|-|-|2,077|
|**SSW**|-|24,273|8,360|0,002|-|-|-|32,635|
|**SW**|-|13,234|3,893|0,002|-|-|-|17,128|
|**WSW**|-|2,739|0,025|-|-|-|-|2,765|
|**W **|-|2,844|0,018|-|-|-|-|2,862|
|**WNW**|-|1,987|0,003|-|-|-|-|1,991|
|**NW**|-|2,171|0,016|-|-|-|-|2,187|
|**NNW**|-|1,747|0,170|0,003|-|-|-|1,920|
|**Calmas**|22,375|-|-|-|-|-|-|22,375|
|**Sub Total**<br>**(%)**<br>|22,375<br>|63,185<br>|14,412<br>|0,029<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|114.366|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|27|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Gráfico 4-5: Variación de la magnitud promedio y máxima del viento por dirección de**

**procedencia. Mediciones sector ITI.**

**Tabla 4-2: Intensidades promedio y máxima globales y por dirección de procedencia**

**de los vientos. Mediciones sector ITI.**

|Col1|Intensidad del viento|Col3|Col4|Col5|
|---|---|---|---|---|
|**Direcciones**|**Máxima**|**Máxima**|**Promedio**|**Promedio**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N **|3,931|7,626|1,107|1,461|
|**NNE**|3,141|6,094|0,961|1,864|
|**NE**|2,553|4,953|0,749|1,453|
|**ENE**|2,948|5,719|0,913|1,770|
|**E **|2,553|4,953|0,625|1,213|
|**ESE**|2,553|4,953|0,727|1,411|
|**SE**|2,158|4,187|0,621|1,204|
|**SSE**|2,755|5,345|0,617|1,197|
|**S **|2,755|5,345|0,730|1,417|
|**SSW**|3,141|6,094|1,133|2,197|
|**SW**|3,141|6,094|1,095|2,124|
|**WSW**|2,360|4,578|0,696|1,351|
|**W **|1,773|3,440|0,753|1,461|
|**WNW**|1,570|3,046|0,717|1,391|
|**NW**|1,965|3,812|0,740|1,435|
|**NNW**|3,536|6,860|0,885|1,716|
|**Global**|3,931|7,626|0,808|1,567|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|28|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-3: Valores estadísticos de las componentes ortogonales de la intensidad del**

**viento. Mediciones sector ITI.**

|Valores|Componente U|Componente V|
|---|---|---|
|**Promedio (m/s)**|0,381|0,497|
|**Desviación estándar (m/s)**|0,498|0,792|
|**Máximo (m/s)**|2,045|2,779|
|**Mínimo (m/s)**|-2,692|-3,866|
|**Porcentaje de participación (%)**|33,166|66,834|

Fuente: Ecotecnos, 2021.

Fuente: Ecotecnos, 2021.
**Gráfico 4-6: Valores centrados de las componentes ortogonales junto a su**

**componente principal. Mediciones sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|29|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**4.1.2 Análisis Espectral**

Mediante el análisis espectral (Gráfico 4-7) se representan las densidades energéticas de las
componentes ortogonales del viento (U y V), las cuales se asemejan en forma, aunque la
componente V resalta por una mayor energía. En la serie de vientos medidos destacan peaks
energéticos asociados a los ciclos diurnos (24 hrs) y semidiurnos (12 hrs). Las menores
frecuencias contienen una menor densidad energética, las cuales se encuentran asociadas a
fenómenos de mayor escala, tales como efectos sinópticos y/o meteorológicos en la capa
geostrófica, donde se hace más notoria la relevancia de la componente V. En cuanto a las
mayores frecuencias, que representan las turbulencias por efecto de la capa límite, ambas
componentes ortogonales se asemejan en la energía estimada. Es necesario señalar que las
frecuencias mayores, en su conjunto, podrían resultar un aporte importante a las
características energéticas del viento.

Fuente: Ecotecnos, 2021.
**Gráfico 4-7: Densidad espectral de las componentes U y V del viento. Mediciones**

**sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|30|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**4.1.3 Vectores Progresivos**

El análisis del vector progresivo (Gráfico 4-8) indica que una partícula de aire hipotética, en la
posición de la estación meteorológica, en el sector de ITI, consigue desplazarse 16.000 km
aproximadamente, durante el tiempo de medición que supera un año. Esta partícula se mueve,
casi directamente, hacia el NE con una velocidad neta de 0,49 m/s. El transporte de la partícula
es coincidente con el elevado predominio del viento desde el tercer cuadrante.

Fuente: Ecotecnos, 2021.
**Gráfico 4-8: Diagrama de vectores progresivos del viento registrado en el período.**

**Mediciones sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|31|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**4.1.4 Caracterización Estadística -Mensual**

Con los datos registrados en el sector de ITI durante un periodo superior a un año, se filtraron
y caracterizaron los meses correspondientes en su intensidad y dirección del viento.

Los datos de viento entre los meses analizados se representan mediante tablas de incidencia
(desde la Tabla 4-4 a la Tabla 4-15) e histogramas (Gráfico 4-9 y Gráfico 4-10). En estos
registros predominan las categorías Calmas (0,00 - 0,28 m/s), Aire Ligero (0,28 - 1,39 m/s) y
Brisa Ligera (1,39 - 3,06 m/s). En todos los meses analizados destaca la categoría Aire Ligero
que, en enero presenta una concentración de 59,532 % y, en adelante, se muestra una
tendencia de crecimiento hasta septiembre, cuando alcanza el 72,431 %. En el resto de meses
se reduce la frecuencia de esta categoría hasta el 58,053 % de los datos en diciembre. En
cuanto a las Calmas, la menor categoría, su mayor ocurrencia se encuentra en enero con
31,317 % y la menor en agosto, con 13,138 %. Entre los meses noviembre y abril las Calmas
se mantuvieron con una frecuencia sobre el 20 %. Por otro lado, en todos los meses la
categoría Brisa Ligera se encuentra bajo los 20 %, además de registrar una alta variabilidad
en sus ocurrencias, estimándose su mínima frecuencia en mayo con 5,388 % y la máxima en
agosto con 19,545 %. En el ciclo anual de intensidades (Gráfico 4-15) resalta agosto, al
presentar el mayor valor medio, 0,950 m/s, y el menor en el mes de mayo con 0,653 m/s, sin
embargo, como este análisis se realizó con una cantidad levemente mayor a un año, se refleja

una alta variabilidad en los valores medios.

Mediante las tablas de incidencia (desde la Tabla 4-4 a la Tabla 4-15), histogramas (Gráfico
4-11 y Gráfico 4-12) y rosas de vientos (Gráfico 4-13 y Gráfico 4-14) se representa la
direccionalidad de los vientos registrados. En los distintos meses destaca el predominio de los
vientos provenientes del tercer cuadrante, centradas en las direcciones SSW y SW. Entre los
meses mayo y agosto aumenta la aparición desde el primer y cuarto cuadrante. Este
comportamiento se verifica en el ciclo mensual (Gráfico 4-16), pues, durante los meses
mencionados, se reduce la concentración del SSW y se releva una mayor dispersión hacia las
direcciones con componente N.

El mayor valor del registro (Tabla 4-16 y Tabla 4-17) corresponde a 3,931 m/s (7,626 nudos)
proveniente de la dirección N, durante el mes de febrero. Por otro lado, en el mes de octubre
se presenta otra magnitud importante igual a 3,728 m/s (7,232 nudos), también desde la
dirección N. Con la obtención del valor medio por dirección para cada mes (Tabla 4-18 y Tabla
4-19), se revela que el mayor valor, 1,359 m/s (2,636 nudos), se ubica durante el mes de julio
en la dirección N. En general, los valores medios muestran que los menores valores ocurren
entre el primer y segundo cuadrante, en cercanía de la dirección E. En contraste, en todos los
meses analizados se concentran grandes intensidades en la dirección SSW y SW.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|32|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-4: Tabla de incidencia del viento, enero. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|2,487|0,269|-|-|-|-|2,755|
|**NNE**|-|3,439|0,190|-|-|-|-|3,629|
|**NE**|-|1,098|0,011|-|-|-|-|1,109|
|**ENE**|-|0,717|-|-|-|-|-|0,717|
|**E **|-|0,437|-|-|-|-|-|0,437|
|**ESE**|-|0,403|-|-|-|-|-|0,403|
|**SE**|-|0,302|-|-|-|-|-|0,302|
|**SSE**|-|0,370|0,011|-|-|-|-|0,381|
|**S **|-|1,221|-|-|-|-|-|1,221|
|**SSW**|-|25,045|7,012|-|-|-|-|32,056|
|**SW**|-|12,903|1,501|-|-|-|-|14,404|
|**WSW**|-|1,770|-|-|-|-|-|1,770|
|**W **|-|1,949|0,011|-|-|-|-|1,960|
|**WNW**|-|2,195|-|-|-|-|-|2,195|
|**NW**|-|3,024|0,011|-|-|-|-|3,035|
|**NNW**|-|2,173|0,134|-|-|-|-|2,307|
|**Calmas**|31,317|-|-|-|-|-|-|31,317|
|**Sub Total**<br>**(%)**<br>|31,317<br>|59,532<br>|9,151<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|8.928|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|33|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-5: Tabla de incidencia del viento, febrero. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|1,474|0,480|0,056|-|-|-|2,010|
|**NNE**|-|1,938|0,056|-|-|-|-|1,994|
|**NE**|-|1,610|0,024|-|-|-|-|1,634|
|**ENE**|-|1,177|0,016|-|-|-|-|1,193|
|**E **|-|0,480|-|-|-|-|-|0,480|
|**ESE**|-|0,232|-|-|-|-|-|0,232|
|**SE**|-|0,304|-|-|-|-|-|0,304|
|**SSE**|-|0,569|0,024|-|-|-|-|0,593|
|**S **|-|2,330|0,368|-|-|-|-|2,699|
|**SSW**|-|26,275|15,176|0,008|-|-|-|41,459|
|**SW**|-|10,203|2,306|-|-|-|-|12,509|
|**WSW**|-|1,890|-|-|-|-|-|1,890|
|**W **|-|2,162|0,008|-|-|-|-|2,170|
|**WNW**|-|2,098|0,008|-|-|-|-|2,106|
|**NW**|-|1,850|0,016|-|-|-|-|1,866|
|**NNW**|-|1,321|0,280|0,032|-|-|-|1,634|
|**Calmas**|25,226|-|-|-|-|-|-|25,226|
|**Sub Total**<br>**(%)**<br>|25,226<br>|55,914<br>|18,764<br>|0,096<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|12.487|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|34|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-6: Tabla de incidencia del viento, marzo. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|1,098|0,182|-|-|-|-|1,280|
|**NNE**|-|1,556|0,036|-|-|-|-|1,593|
|**NE**|-|1,811|-|-|-|-|-|1,811|
|**ENE**|-|1,324|0,007|-|-|-|-|1,331|
|**E **|-|0,589|-|-|-|-|-|0,589|
|**ESE**|-|0,473|-|-|-|-|-|0,473|
|**SE**|-|0,313|-|-|-|-|-|0,313|
|**SSE**|-|0,604|0,022|-|-|-|-|0,625|
|**S **|-|2,480|0,400|-|-|-|-|2,880|
|**SSW**|-|28,689|13,643|0,007|-|-|-|42,339|
|**SW**|-|9,330|2,334|-|-|-|-|11,665|
|**WSW**|-|2,851|0,007|-|-|-|-|2,858|
|**W **|-|2,785|0,036|-|-|-|-|2,822|
|**WNW**|-|1,360|0,007|-|-|-|-|1,367|
|**NW**|-|1,382|0,036|-|-|-|-|1,418|
|**NNW**|-|1,091|0,051|-|-|-|-|1,142|
|**Calmas**|25,496|-|-|-|-|-|-|25,496|
|**Sub Total**<br>**(%)**<br>|25,496<br>|57,734<br>|16,762<br>|0,007<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|13.751|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|35|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-7: Tabla de incidencia del viento, abril. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|2,257|0,104|-|-|-|-|2,361|
|**NNE**|-|2,465|0,023|-|-|-|-|2,488|
|**NE**|-|1,701|0,012|-|-|-|-|1,713|
|**ENE**|-|1,586|0,185|-|-|-|-|1,771|
|**E **|-|0,810|-|-|-|-|-|0,810|
|**ESE**|-|0,463|-|-|-|-|-|0,463|
|**SE**|-|0,556|-|-|-|-|-|0,556|
|**SSE**|-|0,845|0,023|-|-|-|-|0,868|
|**S **|-|1,620|-|-|-|-|-|1,620|
|**SSW**|-|22,384|8,530|-|-|-|-|30,914|
|**SW**|-|13,750|3,576|-|-|-|-|17,326|
|**WSW**|-|2,928|0,012|-|-|-|-|2,940|
|**W **|-|2,419|0,012|-|-|-|-|2,431|
|**WNW**|-|1,215|-|-|-|-|-|1,215|
|**NW**|-|1,238|-|-|-|-|-|1,238|
|**NNW**|-|1,424|-|-|-|-|-|1,424|
|**Calmas**|29,861|-|-|-|-|-|-|29,861|
|**Sub Total**<br>**(%)**<br>|29,861<br>|57,662<br>|12,477<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|8.640|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|36|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-8: Tabla de incidencia del viento, mayo. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|2,632|0,123|-|-|-|-|2,755|
|**NNE**|-|4,772|0,325|-|-|-|-|5,096|
|**NE**|-|2,901|0,090|-|-|-|-|2,991|
|**ENE**|-|4,592|0,840|-|-|-|-|5,432|
|**E **|-|1,221|-|-|-|-|-|1,221|
|**ESE**|-|0,918|-|-|-|-|-|0,918|
|**SE**|-|0,683|0,022|-|-|-|-|0,706|
|**SSE**|-|0,862|-|-|-|-|-|0,862|
|**S **|-|2,419|-|-|-|-|-|2,419|
|**SSW**|-|17,596|3,248|-|-|-|-|20,845|
|**SW**|-|11,234|0,706|-|-|-|-|11,940|
|**WSW**|-|4,514|0,011|-|-|-|-|4,525|
|**W **|-|5,399|-|-|-|-|-|5,399|
|**WNW**|-|2,240|-|-|-|-|-|2,240|
|**NW**|-|2,923|-|-|-|-|-|2,923|
|**NNW**|-|2,386|0,022|-|-|-|-|2,408|
|**Calmas**|27,319|-|-|-|-|-|-|27,319|
|**Sub Total**<br>**(%)**<br>|27,319<br>|67,294<br>|5,388<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|8.928|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|37|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-9: Tabla de incidencia del viento, junio. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|2,882|1,563|-|-|-|-|4,444|
|**NNE**|-|4,329|1,400|0,012|-|-|-|5,741|
|**NE**|-|2,801|0,359|-|-|-|-|3,160|
|**ENE**|-|3,704|1,157|-|-|-|-|4,861|
|**E **|-|1,400|0,185|-|-|-|-|1,586|
|**ESE**|-|1,400|0,127|-|-|-|-|1,528|
|**SE**|-|1,100|0,046|-|-|-|-|1,146|
|**SSE**|-|1,134|-|-|-|-|-|1,134|
|**S **|-|4,294|0,058|-|-|-|-|4,352|
|**SSW**|-|23,125|5,764|-|-|-|-|28,889|
|**SW**|-|9,583|1,539|-|-|-|-|11,123|
|**WSW**|-|1,563|-|-|-|-|-|1,563|
|**W **|-|2,674|-|-|-|-|-|2,674|
|**WNW**|-|1,910|-|-|-|-|-|1,910|
|**NW**|-|2,813|0,035|-|-|-|-|2,847|
|**NNW**|-|1,968|0,590|-|-|-|-|2,558|
|**Calmas**|20,486|-|-|-|-|-|-|20,486|
|**Sub Total**<br>**(%)**<br>|20,486<br>|66,678<br>|12,824<br>|0,012<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|8.640|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|38|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-10: Tabla de incidencia del viento, julio. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|4,133|2,666|0,067|-|-|-|6,866|
|**NNE**|-|5,634|1,893|-|-|-|-|7,527|
|**NE**|-|4,547|0,728|-|-|-|-|5,276|
|**ENE**|-|7,818|2,442|-|-|-|-|10,260|
|**E **|-|1,803|0,078|-|-|-|-|1,882|
|**ESE**|-|1,736|0,325|-|-|-|-|2,061|
|**SE**|-|1,389|0,045|-|-|-|-|1,434|
|**SSE**|-|1,042|-|-|-|-|-|1,042|
|**S **|-|1,579|0,011|-|-|-|-|1,591|
|**SSW**|-|13,217|6,944|-|-|-|-|20,161|
|**SW**|-|10,439|1,602|-|-|-|-|12,041|
|**WSW**|-|3,304|0,022|-|-|-|-|3,327|
|**W **|-|4,010|0,011|-|-|-|-|4,021|
|**WNW**|-|2,016|-|-|-|-|-|2,016|
|**NW**|-|3,047|-|-|-|-|-|3,047|
|**NNW**|-|3,170|0,358|-|-|-|-|3,528|
|**Calmas**|13,922|-|-|-|-|-|-|13,922|
|**Sub Total**<br>**(%)**<br>|13,922<br>|68,884<br>|17,126<br>|0,067<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|8.928|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|39|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-11: Tabla de incidencia del viento, agosto. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|2,531|0,762|-|-|-|-|3,293|
|**NNE**|-|3,629|0,403|-|-|-|-|4,032|
|**NE**|-|3,483|0,246|-|-|-|-|3,730|
|**ENE**|-|4,402|0,750|-|-|-|-|5,152|
|**E **|-|0,784|0,011|-|-|-|-|0,795|
|**ESE**|-|0,952|0,078|-|-|-|-|1,030|
|**SE**|-|0,795|0,011|-|-|-|-|0,806|
|**SSE**|-|0,661|0,034|-|-|-|-|0,694|
|**S **|-|2,039|0,146|-|-|-|-|2,184|
|**SSW**|-|19,366|6,149|-|-|-|-|25,515|
|**SW**|-|16,140|10,506|0,022|-|-|-|26,669|
|**WSW**|-|5,018|0,190|-|-|-|-|5,208|
|**W **|-|3,024|0,056|-|-|-|-|3,080|
|**WNW**|-|1,378|-|-|-|-|-|1,378|
|**NW**|-|1,613|0,034|-|-|-|-|1,647|
|**NNW**|-|1,478|0,168|-|-|-|-|1,647|
|**Calmas**|13,138|-|-|-|-|-|-|13,138|
|**Sub Total**<br>**(%)**<br>|13,138<br>|67,294<br>|19,545<br>|0,022<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|8.928|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|40|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-12: Tabla de incidencia del viento, septiembre. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|2,523|0,405|-|-|-|-|2,928|
|**NNE**|-|2,477|0,336|-|-|-|-|2,813|
|**NE**|-|1,632|0,139|-|-|-|-|1,771|
|**ENE**|-|1,806|0,127|-|-|-|-|1,933|
|**E **|-|0,313|-|-|-|-|-|0,313|
|**ESE**|-|0,266|-|-|-|-|-|0,266|
|**SE**|-|0,301|-|-|-|-|-|0,301|
|**SSE**|-|0,417|-|-|-|-|-|0,417|
|**S **|-|1,644|0,012|-|-|-|-|1,655|
|**SSW**|-|27,558|7,118|-|-|-|-|34,676|
|**SW**|-|16,296|4,954|-|-|-|-|21,250|
|**WSW**|-|3,380|0,012|-|-|-|-|3,391|
|**W **|-|4,456|0,035|-|-|-|-|4,491|
|**WNW**|-|3,715|-|-|-|-|-|3,715|
|**NW**|-|3,079|-|-|-|-|-|3,079|
|**NNW**|-|2,569|0,012|-|-|-|-|2,581|
|**Calmas**|14,421|-|-|-|-|-|-|14,421|
|**Sub Total**<br>**(%)**<br>|14,421<br>|72,431<br>|13,148<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|8.640|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|41|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-13: Tabla de incidencia del viento, octubre. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|1,815|0,582|0,112|-|-|-|2,509|
|**NNE**|-|2,576|0,482|0,011|-|-|-|3,069|
|**NE**|-|1,546|0,190|-|-|-|-|1,736|
|**ENE**|-|1,378|0,011|-|-|-|-|1,389|
|**E **|-|0,482|-|-|-|-|-|0,482|
|**ESE**|-|0,459|0,011|-|-|-|-|0,470|
|**SE**|-|0,336|-|-|-|-|-|0,336|
|**SSE**|-|0,426|-|-|-|-|-|0,426|
|**S **|-|1,019|-|-|-|-|-|1,019|
|**SSW**|-|30,354|3,685|-|-|-|-|34,039|
|**SW**|-|19,881|6,732|-|-|-|-|26,613|
|**WSW**|-|1,669|0,022|-|-|-|-|1,691|
|**W **|-|1,927|0,034|-|-|-|-|1,960|
|**WNW**|-|2,610|-|-|-|-|-|2,610|
|**NW**|-|1,792|0,022|-|-|-|-|1,815|
|**NNW**|-|1,322|0,202|-|-|-|-|1,523|
|**Calmas**|18,313|-|-|-|-|-|-|18,313|
|**Sub Total**<br>**(%)**<br>|18,313<br>|69,590<br>|11,974<br>|0,123<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|8.928|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|42|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-14: Tabla de incidencia del viento, noviembre. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|2,512|1,065|-|-|-|-|3,576|
|**NNE**|-|3,345|1,169|-|-|-|-|4,514|
|**NE**|-|1,493|0,035|-|-|-|-|1,528|
|**ENE**|-|0,949|-|-|-|-|-|0,949|
|**E **|-|0,278|-|-|-|-|-|0,278|
|**ESE**|-|0,266|-|-|-|-|-|0,266|
|**SE**|-|0,440|-|-|-|-|-|0,440|
|**SSE**|-|0,197|-|-|-|-|-|0,197|
|**S **|-|0,440|-|-|-|-|-|0,440|
|**SSW**|-|23,600|6,829|-|-|-|-|30,428|
|**SW**|-|19,109|5,984|-|-|-|-|25,093|
|**WSW**|-|2,326|-|-|-|-|-|2,326|
|**W **|-|2,292|-|-|-|-|-|2,292|
|**WNW**|-|2,141|0,023|-|-|-|-|2,164|
|**NW**|-|2,280|0,012|-|-|-|-|2,292|
|**NNW**|-|1,563|0,023|-|-|-|-|1,586|
|**Calmas**|21,632|-|-|-|-|-|-|21,632|
|**Sub Total**<br>**(%)**<br>|21,632<br>|63,229<br>|15,139<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|8.640|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|43|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-15: Tabla de incidencia del viento, diciembre. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|1,019|0,235|-|-|-|-|1,254|
|**NNE**|-|0,907|0,045|-|-|-|-|0,952|
|**NE**|-|0,717|-|-|-|-|-|0,717|
|**ENE**|-|0,515|-|-|-|-|-|0,515|
|**E **|-|0,157|-|-|-|-|-|0,157|
|**ESE**|-|0,258|-|-|-|-|-|0,258|
|**SE**|-|0,459|-|-|-|-|-|0,459|
|**SSE**|-|0,370|-|-|-|-|-|0,370|
|**S **|-|2,151|-|-|-|-|-|2,151|
|**SSW**|-|30,869|10,484|-|-|-|-|41,353|
|**SW**|-|13,441|6,463|-|-|-|-|19,904|
|**WSW**|-|1,915|0,045|-|-|-|-|1,960|
|**W **|-|1,344|0,011|-|-|-|-|1,355|
|**WNW**|-|1,299|-|-|-|-|-|1,299|
|**NW**|-|1,591|0,011|-|-|-|-|1,602|
|**NNW**|-|1,042|0,213|-|-|-|-|1,254|
|**Calmas**|24,440|-|-|-|-|-|-|24,440|
|**Sub Total**<br>**(%)**<br>|24,440<br>|58,053<br>|17,507<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|8.928|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|44|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Enero**

**Marzo**

**Mayo**

**Febrero**

**Abril**

**Junio**

Fuente: Ecotecnos, 2021.
**Gráfico 4-9: Histogramas de intensidad del viento promedio entre los meses enero y junio. Mediciones sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|45|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Julio**

**Septiembre**

**Noviembre**

**Agosto**

**Octubre**

**Diciembre**

Fuente: Ecotecnos, 2021.
**Gráfico 4-10: Histogramas de intensidad del viento promedio entre los meses julio y diciembre. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|46|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Enero**

**Marzo**

**Mayo**

**Febrero**

**Abril**

**Junio**

Fuente: Ecotecnos, 2021.
**Gráfico 4-11: Histogramas de dirección del viento promedio entre los meses enero y junio. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|47|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Julio**

**Septiembre**

**Noviembre**

**Agosto**

**Octubre**

**Diciembre**

Fuente: Ecotecnos, 2021.
**Gráfico 4-12: Histogramas de dirección del viento promedio entre los meses julio y diciembre. Mediciones sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|48|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

|Enero|Febrero|
|---|---|
|**Marzo**|**Abril**|
|**Mayo**|**Junio**|

Fuente: Ecotecnos, 2021.
**Gráfico 4-13: Rosa de los vientos entre los meses enero y junio. Mediciones sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|49|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

|Julio|Agosto|
|---|---|
|**Septiembre**|**Octubre**|
|**Noviembre**|**Diciembre**|

Fuente: Ecotecnos, 2021.
**Gráfico 4-14: Rosa de los vientos entre los meses julio y diciembre. Mediciones sector**

**ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|50|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Gráfico 4-15: Histograma de intensidad del viento promedio en un ciclo anual. Mediciones sector ITI.**

Fuente: Ecotecnos, 2021.
**Gráfico 4-16: Ocurrencia de la incidencia del viento por dirección en un ciclo anual. Mediciones sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|51|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-16: Intensidades máxima globales y por dirección de procedencia de los vientos, entre los meses enero-junio.**

**Mediciones sector ITI.**

|Col1|Intensidad máxima del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Meses**|**Enero**|**Enero**|**Febrero**|**Febrero**|**Marzo**|**Marzo**|**Abril**|**Abril**|**Mayo**|**Mayo**|**Junio**|**Junio**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N **|1,773|3,440|3,931|7,626|2,158|4,187|1,570|3,046|1,773|3,440|2,755|5,345|
|**NNE**|1,965|3,812|2,553|4,953|1,773|3,440|1,570|3,046|2,158|4,187|3,141|6,094|
|**NE**|1,570|3,046|2,158|4,187|1,175|2,280|1,570|3,046|1,773|3,440|2,158|4,187|
|**ENE**|0,588|1,141|1,570|3,046|1,570|3,046|1,965|3,812|2,948|5,719|2,948|5,719|
|**E **|0,790|1,533|1,175|2,280|0,983|1,907|1,378|2,673|1,175|2,280|2,360|4,578|
|**ESE**|0,588|1,141|1,175|2,280|1,175|2,280|0,790|1,533|1,378|2,673|2,158|4,187|
|**SE**|0,983|1,907|0,983|1,907|0,983|1,907|1,175|2,280|1,570|3,046|2,158|4,187|
|**SSE**|1,570|3,046|2,360|4,578|1,773|3,440|1,570|3,046|1,175|2,280|1,378|2,673|
|**S **|1,175|2,280|2,360|4,578|2,755|5,345|1,378|2,673|1,378|2,673|1,570|3,046|
|**SSW**|2,553|4,953|3,141|6,094|3,141|6,094|2,755|5,345|2,553|4,953|2,553|4,953|
|**SW**|2,553|4,953|2,755|5,345|2,948|5,719|2,948|5,719|2,360|4,578|2,158|4,187|
|**WSW**|1,175|2,280|1,175|2,280|1,773|3,440|1,570|3,046|1,570|3,046|1,378|2,673|
|**W **|1,570|3,046|1,570|3,046|1,570|3,046|1,570|3,046|1,378|2,673|1,175|2,280|
|**WNW**|1,378|2,673|1,570|3,046|1,570|3,046|1,175|2,280|1,378|2,673|1,175|2,280|
|**NW**|1,570|3,046|1,773|3,440|1,965|3,812|1,378|2,673|1,378|2,673|1,965|3,812|
|**NNW**|1,773|3,440|3,536|6,860|1,965|3,812|1,378|2,673|1,570|3,046|2,553|4,953|
|**Global**|2,553|4,953|3,931|7,626|3,141|6,094|2,948|5,719|2,948|5,719|3,141|6,094|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|52|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-17: Intensidades máxima globales y por dirección de procedencia de los vientos, entre los meses julio-diciembre.**

**Mediciones sector ITI.**

|Col1|Intensidad máxima del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Meses**|**Julio**|**Julio**|**Agosto**|**Agosto**|**Septiembre**|**Septiembre**|**Octubre**|**Octubre**|**Noviembre**|**Noviembre**|**Diciembre**|**Diciembre**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N **|3,343|6,485|2,360|4,578|1,965|3,812|3,728|7,232|2,553|4,953|2,158|4,187|
|**NNE**|2,948|5,719|2,553|4,953|1,965|3,812|3,141|6,094|2,755|5,345|2,158|4,187|
|**NE**|2,553|4,953|2,553|4,953|1,570|3,046|1,965|3,812|1,570|3,046|1,175|2,280|
|**ENE**|2,553|4,953|2,755|5,345|1,570|3,046|1,570|3,046|0,790|1,533|0,790|1,533|
|**E **|2,553|4,953|1,570|3,046|0,983|1,907|0,983|1,907|0,790|1,533|0,395|0,766|
|**ESE**|2,553|4,953|1,965|3,812|1,175|2,280|1,570|3,046|0,983|1,907|1,378|2,673|
|**SE**|2,158|4,187|1,773|3,440|1,175|2,280|1,175|2,280|1,175|2,280|1,378|2,673|
|**SSE**|1,378|2,673|2,755|5,345|1,378|2,673|1,378|2,673|0,983|1,907|1,175|2,280|
|**S **|1,570|3,046|2,360|4,578|1,570|3,046|0,983|1,907|0,983|1,907|1,378|2,673|
|**SSW**|2,553|4,953|2,553|4,953|2,755|5,345|2,553|4,953|2,360|4,578|2,360|4,578|
|**SW**|2,755|5,345|3,141|6,094|2,755|5,345|2,553|4,953|2,948|5,719|2,755|5,345|
|**WSW**|1,570|3,046|2,360|4,578|1,570|3,046|1,570|3,046|1,378|2,673|1,773|3,440|
|**W **|1,570|3,046|1,773|3,440|1,773|3,440|1,570|3,046|1,378|2,673|1,570|3,046|
|**WNW**|1,175|2,280|1,175|2,280|1,378|2,673|1,378|2,673|1,570|3,046|1,378|2,673|
|**NW**|1,175|2,280|1,570|3,046|1,378|2,673|1,570|3,046|1,570|3,046|1,570|3,046|
|**NNW**|2,553|4,953|2,360|4,578|1,570|3,046|2,360|4,578|1,773|3,440|2,360|4,578|
|**Global**|3,343|6,485|3,141|6,094|2,755|5,345|3,728|7,232|2,948|5,719|2,755|5,345|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|53|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-18: Intensidades promedio globales y por dirección de procedencia de los vientos, entre los meses enero-junio.**

**Mediciones sector ITI.**

|Col1|Intensidad promedio del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Meses**|**Enero**|**Enero**|**Febrero**|**Febrero**|**Marzo**|**Marzo**|**Abril**|**Abril**|**Mayo**|**Mayo**|**Junio**|**Junio**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N **|0,866|1,681|1,116|2,164|0,829|1,608|0,839|1,628|0,872|1,692|1,242|2,409|
|**NNE**|0,767|1,488|0,746|1,448|0,647|1,255|0,710|1,377|0,832|1,614|1,150|2,230|
|**NE**|0,526|1,020|0,562|1,091|0,532|1,032|0,671|1,303|0,732|1,419|0,882|1,712|
|**ENE**|0,464|0,901|0,537|1,041|0,558|1,083|0,774|1,501|0,955|1,853|1,069|2,074|
|**E **|0,485|0,940|0,506|0,981|0,491|0,953|0,535|1,037|0,560|1,086|0,818|1,588|
|**ESE**|0,449|0,870|0,469|0,910|0,557|1,080|0,453|0,879|0,624|1,211|0,803|1,558|
|**SE**|0,453|0,879|0,487|0,945|0,481|0,933|0,497|0,964|0,610|1,183|0,710|1,376|
|**SSE**|0,544|1,056|0,633|1,229|0,648|1,256|0,614|1,191|0,565|1,096|0,657|1,274|
|**S **|0,594|1,152|0,938|1,820|0,882|1,710|0,557|1,080|0,587|1,139|0,721|1,399|
|**SSW**|1,106|2,145|1,267|2,459|1,221|2,370|1,147|2,225|1,012|1,963|1,074|2,084|
|**SW**|0,952|1,847|1,022|1,982|1,045|2,027|1,090|2,114|0,885|1,717|0,988|1,917|
|**WSW**|0,555|1,076|0,612|1,188|0,727|1,411|0,762|1,479|0,739|1,434|0,596|1,157|
|**W **|0,670|1,300|0,686|1,331|0,756|1,467|0,775|1,503|0,799|1,551|0,704|1,365|
|**WNW**|0,719|1,394|0,775|1,504|0,676|1,312|0,621|1,204|0,670|1,300|0,607|1,178|
|**NW**|0,729|1,413|0,748|1,451|0,684|1,327|0,675|1,310|0,713|1,382|0,731|1,419|
|**NNW**|0,859|1,666|1,011|1,962|0,778|1,509|0,811|1,573|0,810|1,572|1,079|2,093|
|**Global**|0,675|1,310|0,837|1,624|0,806|1,563|0,723|1,403|0,653|1,266|0,803|1,558|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|54|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-19: Intensidades promedio globales y por dirección de procedencia de los vientos, entre los meses julio-diciembre.**

**Mediciones sector ITI.**

|Col1|Intensidad promedio del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Meses**|**Julio**|**Julio**|**Agosto**|**Agosto**|**Septiembre**|**Septiembre**|**Octubre**|**Octubre**|**Noviembre**|**Noviembre**|**Diciembre**|**Diciembre**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N **|1,359|2,636|1,059|2,055|1,012|1,964|1,251|2,427|1,234|2,394|0,927|1,799|
|**NNE**|1,171|2,272|0,914|1,773|0,986|1,913|0,993|1,926|1,182|2,293|0,713|1,383|
|**NE**|0,931|1,806|0,812|1,575|0,808|1,568|0,797|1,546|0,630|1,223|0,545|1,057|
|**ENE**|1,105|2,143|0,927|1,798|0,816|1,583|0,668|1,296|0,505|0,979|0,514|0,997|
|**E **|0,707|1,372|0,762|1,478|0,511|0,991|0,558|1,083|0,460|0,893|0,395|0,766|
|**ESE**|0,883|1,713|0,874|1,696|0,693|1,343|0,745|1,446|0,633|1,229|0,643|1,247|
|**SE**|0,708|1,374|0,721|1,399|0,620|1,203|0,558|1,082|0,601|1,166|0,562|1,090|
|**SSE**|0,635|1,232|0,666|1,293|0,651|1,262|0,554|1,075|0,580|1,125|0,495|0,961|
|**S **|0,687|1,333|0,791|1,535|0,596|1,156|0,506|0,982|0,565|1,096|0,647|1,254|
|**SSW**|1,237|2,399|1,126|2,185|1,066|2,068|0,933|1,809|1,081|2,098|1,122|2,176|
|**SW**|1,029|1,996|1,330|2,580|1,066|2,069|1,115|2,164|1,128|2,188|1,181|2,291|
|**WSW**|0,709|1,376|0,822|1,595|0,582|1,129|0,643|1,247|0,652|1,266|0,686|1,331|
|**W **|0,785|1,522|0,768|1,489|0,748|1,452|0,712|1,381|0,776|1,506|0,795|1,543|
|**WNW**|0,646|1,254|0,568|1,101|0,710|1,377|0,831|1,612|0,839|1,627|0,836|1,621|
|**NW**|0,672|1,304|0,702|1,363|0,750|1,455|0,803|1,558|0,830|1,611|0,890|1,727|
|**NNW**|0,891|1,729|0,847|1,642|0,802|1,556|0,887|1,720|0,778|1,510|1,013|1,965|
|**Global**|0,913|1,771|0,950|1,843|0,845|1,639|0,810|1,572|0,836|1,622|0,829|1,608|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|55|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**4.1.5 Caracterización Estadística -Estacional**

Para profundizar el análisis de la variación anual de las mediciones, se decidió segmentar las
mediciones del sector de ITI según sus estaciones. La magnitud del viento durante las
estaciones fue exhibida mediante tablas de incidencia (desde la Tabla 4-20 a la Tabla 4-23) e
histogramas (Gráfico 4-17).

En las estaciones analizadas predominan, según la escala de Beaufort, las categorías de
Calmas (0,00 - 0,28 m/s), Aire Ligero (0,28 - 1,39 m/s) y Brisa Ligera (1,39 - 3,06 m/s). En
aspectos generales, las intensidades del viento se asemejaron entre el verano y otoño, debido
a que en ambos destaca la categoría Aire Ligero por su frecuencia (cerca del 60%, en ambos),
las Calmas se encuentran sobre el 25 % y la Brisa Ligera con una frecuencia superior al 10 %
de los datos registrados. En contraste, durante el invierno y primavera, la categoría Aire Ligero
incrementa aún más su protagonismo con ocurrencias sobre el 65 %. En invierno las
categorías Brisa Ligera y Calmas se asemejan en su frecuencia, cerca del 15 %, siendo la
Brisa Ligera levemente mayor. En contraste, en la primavera, las Calmas alcanzan el 20,273 %
y la Brisa Ligera el 14,456 % de los datos.

La direccionalidad de las estaciones analizadas se señala mediante tablas de incidencia

(desde la Tabla 4-20 a la Tabla 4-23), histogramas (Gráfico 4-18) y rosas de vientos (Gráfico
4-19). Se verifica que lo vientos proceden habitualmente desde el tercer cuadrante, centrado
en las direcciones SSW y SW, independiente de las estaciones, sin embargo, en invierno y
otoño los datos se dispersan, apareciendo vientos desde el primer y cuarto cuadrante.

El máximo valor presente en el registro (Tabla 4-24) corresponde a 3,931 m/s (7,626 nudos)
desde la dirección N, durante la estación de verano, mientras que, el máximo más bajo ocurre
en la estación de primavera en la dirección E. Según la media de los vientos por estación y
dirección (Tabla 4-25), la mayor intensidad media se estima en la estación de verano con
1,219 m/s (2,365 nudos) desde la dirección SSW.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|56|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-20: Tabla de incidencia del viento, verano promedio. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N**|-|1,613|0,310|0,020|-|-|-|1,943|
|**NNE**|-|2,182|0,082|-|-|-|-|2,264|
|**NE**|-|1,576|0,011|-|-|-|-|1,587|
|**ENE**|-|1,107|0,009|-|-|-|-|1,115|
|**E**|-|0,481|-|-|-|-|-|0,481|
|**ESE**|-|0,361|-|-|-|-|-|0,361|
|**SE**|-|0,336|-|-|-|-|-|0,336|
|**SSE**|-|0,518|0,011|-|-|-|-|0,529|
|**S**|-|2,105|0,287|-|-|-|-|2,392|
|**SSW**|-|26,818|12,724|0,006|-|-|-|39,548|
|**SW**|-|10,451|2,259|-|-|-|-|12,709|
|**WSW**|-|2,224|0,009|-|-|-|-|2,233|
|**W**|-|2,187|0,020|-|-|-|-|2,207|
|**WNW**|-|1,863|0,003|-|-|-|-|1,866|
|**NW**|-|1,988|0,023|-|-|-|-|2,011|
|**NNW**|-|1,468|0,154|0,011|-|-|-|1,633|
|**Calmas**|26,784|-|-|-|-|-|-|26,784|
|**Sub Total**<br>**(%)** <br>|26,784<br>|57,278<br>|15,901<br>|0,037<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|35.155|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|57|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-21: Tabla de incidencia del viento, otoño promedio. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N**|-|2,345|0,510|-|-|-|-|2,854|
|**NNE**|-|3,274|0,468|0,004|-|-|-|3,746|
|**NE**|-|1,933|0,091|-|-|-|-|2,024|
|**ENE**|-|2,560|0,517|-|-|-|-|3,077|
|**E**|-|0,997|0,060|-|-|-|-|1,057|
|**ESE**|-|0,695|0,019|-|-|-|-|0,714|
|**SE**|-|0,653|0,023|-|-|-|-|0,676|
|**SSE**|-|0,921|0,019|-|-|-|-|0,940|
|**S**|-|2,851|0,019|-|-|-|-|2,870|
|**SSW**|-|22,907|6,483|-|-|-|-|29,390|
|**SW**|-|11,999|2,375|-|-|-|-|14,374|
|**WSW**|-|2,922|0,008|-|-|-|-|2,930|
|**W**|-|3,311|0,004|-|-|-|-|3,315|
|**WNW**|-|1,461|0,004|-|-|-|-|1,465|
|**NW**|-|1,899|0,011|-|-|-|-|1,911|
|**NNW**|-|1,729|0,185|-|-|-|-|1,914|
|**Calmas**|26,743|-|-|-|-|-|-|26,743|
|**Sub Total**<br>**(%)** <br>|26,743<br>|62,458<br>|10,795<br>|0,004<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|26.485|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|58|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-22: Tabla de incidencia del viento, invierno promedio. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N**|-|3,111|1,299|0,023|-|-|-|4,433|
|**NNE**|-|4,372|0,982|-|-|-|-|5,354|
|**NE**|-|3,685|0,430|-|-|-|-|4,116|
|**ENE**|-|5,354|1,318|-|-|-|-|6,672|
|**E**|-|1,174|0,030|-|-|-|-|1,204|
|**ESE**|-|1,246|0,159|-|-|-|-|1,405|
|**SE**|-|0,955|0,019|-|-|-|-|0,974|
|**SSE**|-|0,793|0,011|-|-|-|-|0,804|
|**S**|-|1,790|0,057|-|-|-|-|1,846|
|**SSW**|-|19,064|6,366|-|-|-|-|25,429|
|**SW**|-|13,140|5,048|0,008|-|-|-|18,195|
|**WSW**|-|3,625|0,076|-|-|-|-|3,700|
|**W**|-|3,866|0,034|-|-|-|-|3,900|
|**WNW**|-|2,443|-|-|-|-|-|2,443|
|**NW**|-|2,745|0,011|-|-|-|-|2,756|
|**NNW**|-|2,330|0,193|-|-|-|-|2,522|
|**Calmas**|14,246|-|-|-|-|-|-|14,246|
|**Sub Total**<br>**(%)** <br>|14,246<br>|69,692<br>|16,032<br>|0,030<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|26.485|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|59|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-23: Tabla de incidencia del viento, primavera promedio. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N**|-|1,935|0,695|0,038|-|-|-|2,668|
|**NNE**|-|2,382|0,573|0,004|-|-|-|2,958|
|**NE**|-|1,305|0,080|-|-|-|-|1,386|
|**ENE**|-|1,038|0,008|-|-|-|-|1,046|
|**E**|-|0,286|-|-|-|-|-|0,286|
|**ESE**|-|0,313|0,004|-|-|-|-|0,317|
|**SE**|-|0,374|-|-|-|-|-|0,374|
|**SSE**|-|0,286|-|-|-|-|-|0,286|
|**S**|-|1,088|-|-|-|-|-|1,088|
|**SSW**|-|27,469|6,432|-|-|-|-|33,901|
|**SW**|-|18,281|6,459|-|-|-|-|24,739|
|**WSW**|-|2,355|0,015|-|-|-|-|2,371|
|**W**|-|2,222|0,015|-|-|-|-|2,237|
|**WNW**|-|2,229|0,008|-|-|-|-|2,237|
|**NW**|-|2,111|0,015|-|-|-|-|2,126|
|**NNW**|-|1,554|0,153|-|-|-|-|1,706|
|**Calmas**|20,273|-|-|-|-|-|-|20,273|
|**Sub Total**<br>**(%)** <br>|20,273<br>|65,229<br>|14,456<br>|0,042<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|26.197|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|60|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**VERANO** **OTOÑO**

**INVIERNO** **PRIMAVERA**

Fuente: Ecotecnos, 2021.
**Gráfico 4-17: Histogramas de intensidad del viento promedio por estación del año. Mediciones sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|61|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**VERANO**

**INVIERNO**

**OTOÑO**

**PRIMAVERA**

Fuente: Ecotecnos, 2021.
**Gráfico 4-18: Histogramas de dirección del viento promedio por estación del año. Mediciones sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|62|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

|Verano|Otoño|
|---|---|
|**Invierno**|**Primavera**|

Fuente: Ecotecnos, 2021.
**Gráfico 4-19: Rosa de los vientos entre estaciones. Mediciones sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|63|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-24: Intensidades máxima globales y por dirección de procedencia de los**

**vientos,** **por estaciones. Mediciones sector ITI.**

|Col1|Intensidad máxima del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Estaciones**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N**|3,931|7,626|2,755|5,345|3,343|6,485|3,728|7,232|
|**NNE**|2,553|4,953|3,141|6,094|2,948|5,719|3,141|6,094|
|**NE**|2,158|4,187|2,158|4,187|2,553|4,953|1,965|3,812|
|**ENE**|1,570|3,046|2,948|5,719|2,755|5,345|1,570|3,046|
|**E**|1,175|2,280|2,360|4,578|2,553|4,953|0,983|1,907|
|**ESE**|1,175|2,280|2,158|4,187|2,553|4,953|1,570|3,046|
|**SE**|1,378|2,673|2,158|4,187|2,158|4,187|1,175|2,280|
|**SSE**|2,360|4,578|1,773|3,440|2,755|5,345|1,378|2,673|
|**S**|2,755|5,345|1,570|3,046|2,360|4,578|1,378|2,673|
|**SSW**|3,141|6,094|2,948|5,719|2,553|4,953|2,755|5,345|
|**SW**|2,948|5,719|2,948|5,719|3,141|6,094|2,948|5,719|
|**WSW**|1,773|3,440|1,570|3,046|2,360|4,578|1,773|3,440|
|**W**|1,570|3,046|1,570|3,046|1,773|3,440|1,570|3,046|
|**WNW**|1,570|3,046|1,570|3,046|1,378|2,673|1,570|3,046|
|**NW**|1,965|3,812|1,965|3,812|1,570|3,046|1,570|3,046|
|**NNW**|3,536|6,860|2,553|4,953|2,553|4,953|2,360|4,578|
|**Global**|3,931|7,626|3,141|6,094|3,343|6,485|3,728|7,232|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|64|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-25: Intensidades promedio globales y por dirección de procedencia de los**

**vientos,** **por estaciones. Mediciones sector ITI.**

|Col1|Intensidad promedio del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Estaciones**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N**|0,945|1,834|1,028|1,995|1,205|2,338|1,188|2,304|
|**NNE**|0,725|1,407|0,935|1,815|1,059|2,054|1,056|2,050|
|**NE**|0,544|1,056|0,728|1,413|0,882|1,710|0,697|1,352|
|**ENE**|0,535|1,038|0,938|1,820|1,032|2,002|0,608|1,179|
|**E**|0,495|0,961|0,632|1,226|0,715|1,387|0,509|0,988|
|**ESE**|0,509|0,987|0,629|1,220|0,857|1,663|0,702|1,362|
|**SE**|0,496|0,962|0,601|1,165|0,710|1,377|0,573|1,111|
|**SSE**|0,576|1,117|0,638|1,237|0,654|1,269|0,544|1,055|
|**S**|0,865|1,678|0,655|1,270|0,695|1,347|0,597|1,157|
|**SSW**|1,219|2,365|1,096|2,126|1,120|2,172|1,040|2,018|
|**SW**|1,022|1,982|1,026|1,990|1,171|2,271|1,129|2,190|
|**WSW**|0,654|1,269|0,729|1,414|0,739|1,434|0,642|1,246|
|**W**|0,705|1,368|0,770|1,494|0,773|1,499|0,756|1,467|
|**WNW**|0,725|1,407|0,639|1,240|0,662|1,284|0,820|1,591|
|**NW**|0,725|1,406|0,685|1,330|0,718|1,394|0,838|1,625|
|**NNW**|0,889|1,725|0,919|1,783|0,856|1,660|0,883|1,712|
|**Global**|0,788|1,529|0,729|1,415|0,891|1,729|0,829|1,608|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|65|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**4.1.6 Caracterización Estadística -Diaria**

Con el fin de analizar la variación diaria de los vientos registrados en el sector de ITI, se
clasificaron en 6 intervalos horarios, (0 - 4 hrs), (4 - 8 hrs), (8 - 12 hrs), (12 - 16 hrs), (1620 hrs) y (20 - 0 hrs).

La intensidad del viento se caracteriza según la escala de Beaufort y se representa mediante
tablas de incidencia (entre la Tabla 4-26 y la Tabla 4-31) e histogramas (Gráfico 4-20) y, junto
a ello, se establece el ciclo diario de magnitud (Gráfico 4-23). En el comienzo del día (0 - 4 hrs)
lidera la categoría Aire Ligero (70,965 %), junto a las Calmas (24,717 %) y, en tercer lugar, la
Brisa Ligera (4;308 %). Según lo señalado en el ciclo diario, este periodo se distingue por un
descenso de la intensidad del viento y, en los siguientes dos intervalos (4 - 8 hrs) y (8 - 12
hrs), la magnitud se encuentra en sus menores valores medios, siendo el mínimo igual a 0,408
m/s. En estos últimos intervalos la ocurrencia del Aire Ligero se reduce y las Calmas se
incrementan, alcanzando frecuencias semejantes (cerca al 48%). En el próximo intervalo,
(12 - 16 hrs), los vientos registrados se concentran en la categoría Aire Ligero (74,763 %),
manteniendo las Calmas y Brisa Ligera en 12 % aproximadamente. Este periodo corresponde,
según el ciclo diario, a un incremento de las velocidades del viento durante el día. En el
intervalo (12 - 16 hrs) se alcanzan las mayores velocidades dentro del día, con la intensidad
de 1,406 m/s. Dentro de este periodo las ocurrencias de las Calmas se vuelven despreciables,
agrupándose los vientos en las categorías de Aire Ligero (58,997 %) y Brisa Ligera (40,652 %).
Finalmente, en el intervalo (20 - 00 hrs), la categoría Aire Ligero sobresale del resto con una
frecuencia 73,373 %.

Los cambios en las direcciones se representan mediante tablas de incidencia (entre la Tabla
4-26 y la Tabla 4-31), histogramas (Gráfico 4-20) y rosas de viento, además del apoyo de un
esquema del ciclo diario de las direcciones (Gráfico 4-24). Durante el comienzo del día los
datos de viento predominan notablemente desde el tercer cuadrante, concentrados en las
direcciones SSW y SW. En los intervalos (4 - 8 hrs) y (8 - 12 hrs) se aparecen vientos desde
el primer cuadrante en una cantidad relevante. Luego, en el intervalo (12 - 16 hrs) se
apreciaron vientos desde el cuarto cuadrante. En las horas restantes, se concentran los
vientos, casi exclusivamente, desde el tercer cuadrante, con mayor concentración en la

dirección SSW.

Respecto a los valores máximos del viento por dirección e intervalo horario (Tabla 4-32), se
determina que la mayor intensidad corresponde a 3,931 m/s (7,626 nudos), proveniente desde
la dirección N, durante el intervalo (8 - 12 hrs). En contraste, con los valores medios por
dirección y por periodo horario (Tabla 4-33), el mayor valor medio corresponde a 1,523 m/s
(2,955 nudos) desde la dirección SSW durante el intervalo (16 - 20 hrs). El menor valor se
estimó durante el mismo intervalo desde la dirección ESE, con un valor 0,395m/s
(0,766 nudos), conducta que responde a la concentración del viento en el tercer cuadrante en

las horas mencionadas.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|66|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-26: Tabla de incidencia del viento; Intervalo [0 - 4[ hrs. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|2,750|0,798|0,010|-|-|-|3,558|
|**NNE**|-|3,899|0,729|-|-|-|-|4,628|
|**NE**|-|2,487|0,278|-|-|-|-|2,766|
|**ENE**|-|1,627|0,100|-|-|-|-|1,726|
|**E **|-|0,425|-|-|-|-|-|0,425|
|**ESE**|-|0,394|-|-|-|-|-|0,394|
|**SE**|-|0,320|0,005|-|-|-|-|0,325|
|**SSE**|-|0,630|0,010|-|-|-|-|0,640|
|**S **|-|2,152|0,084|-|-|-|-|2,236|
|**SSW**|-|30,300|1,270|-|-|-|-|31,570|
|**SW**|-|16,740|0,803|-|-|-|-|17,543|
|**WSW**|-|2,173|-|-|-|-|-|2,173|
|**W **|-|1,601|-|-|-|-|-|1,601|
|**WNW**|-|1,417|-|-|-|-|-|1,417|
|**NW**|-|1,800|0,037|-|-|-|-|1,837|
|**NNW**|-|2,251|0,194|-|-|-|-|2,445|
|**Calmas**|24,717|-|-|-|-|-|-|24,717|
|**Sub Total**<br>**(%)**<br>|24,717<br>|70,965<br>|4,308<br>|0,010<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|19.056|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|67|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-27: Tabla de incidencia del viento; Intervalo [4 - 8[ hrs. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|2,382|0,352|0,005|-|-|-|2,739|
|**NNE**|-|3,700|0,897|0,005|-|-|-|4,602|
|**NE**|-|4,041|0,299|-|-|-|-|4,340|
|**ENE**|-|4,865|0,546|-|-|-|-|5,410|
|**E **|-|1,622|0,005|-|-|-|-|1,627|
|**ESE**|-|1,454|0,047|-|-|-|-|1,501|
|**SE**|-|1,008|0,016|-|-|-|-|1,023|
|**SSE**|-|0,777|0,016|-|-|-|-|0,792|
|**S **|-|1,952|0,010|-|-|-|-|1,963|
|**SSW**|-|15,517|0,420|-|-|-|-|15,937|
|**SW**|-|8,270|0,063|-|-|-|-|8,333|
|**WSW**|-|1,627|0,005|-|-|-|-|1,632|
|**W **|-|0,955|-|-|-|-|-|0,955|
|**WNW**|-|0,855|-|-|-|-|-|0,855|
|**NW**|-|1,317|0,005|-|-|-|-|1,322|
|**NNW**|-|1,737|0,084|-|-|-|-|1,821|
|**Calmas**|45,146|-|-|-|-|-|-|45,146|
|**Sub Total**<br>**(%)**<br>|45,146<br>|52,078<br>|2,766<br>|0,010<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|19.056|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|68|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-28: Tabla de incidencia del viento; Intervalo [8 - 12[ hrs. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|1,322|0,194|0,037|-|-|-|1,553|
|**NNE**|-|1,963|0,126|-|-|-|-|2,089|
|**NE**|-|3,038|0,236|-|-|-|-|3,275|
|**ENE**|-|5,736|1,506|-|-|-|-|7,242|
|**E **|-|1,810|0,042|-|-|-|-|1,852|
|**ESE**|-|1,580|0,173|-|-|-|-|1,753|
|**SE**|-|1,616|0,037|-|-|-|-|1,653|
|**SSE**|-|1,244|0,016|-|-|-|-|1,259|
|**S **|-|2,577|0,047|-|-|-|-|2,624|
|**SSW**|-|16,861|0,178|-|-|-|-|17,039|
|**SW**|-|7,090|0,026|-|-|-|-|7,116|
|**WSW**|-|1,238|0,021|-|-|-|-|1,259|
|**W **|-|0,682|0,005|-|-|-|-|0,687|
|**WNW**|-|0,745|0,005|-|-|-|-|0,750|
|**NW**|-|0,567|-|-|-|-|-|0,567|
|**NNW**|-|0,866|0,094|0,021|-|-|-|0,981|
|**Calmas**|48,300|-|-|-|-|-|-|48,300|
|**Sub Total**<br>**(%)**<br>|48,300<br>|48,935<br>|2,708<br>|0,058<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|19.056|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|69|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-29: Tabla de incidencia del viento; Intervalo [12 - 16[ hrs. Mediciones sector**

**ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|3,137|0,845|0,031|-|-|-|4,013|
|**NNE**|-|3,803|0,561|0,005|-|-|-|4,370|
|**NE**|-|2,130|0,037|-|-|-|-|2,167|
|**ENE**|-|2,135|0,425|-|-|-|-|2,560|
|**E **|-|0,372|0,079|-|-|-|-|0,451|
|**ESE**|-|0,336|0,031|-|-|-|-|0,367|
|**SE**|-|0,294|-|-|-|-|-|0,294|
|**SSE**|-|0,467|0,010|-|-|-|-|0,477|
|**S **|-|1,128|0,031|-|-|-|-|1,159|
|**SSW**|-|22,027|6,867|-|-|-|-|28,894|
|**SW**|-|14,935|3,247|-|-|-|-|18,182|
|**WSW**|-|5,639|0,042|-|-|-|-|5,681|
|**W **|-|6,054|0,005|-|-|-|-|6,059|
|**WNW**|-|4,517|0,016|-|-|-|-|4,532|
|**NW**|-|4,632|0,021|-|-|-|-|4,653|
|**NNW**|-|3,158|0,289|-|-|-|-|3,446|
|**Calmas**|12,695|-|-|-|-|-|-|12,695|
|**Sub Total**<br>**(%)**<br>|12,695<br>|74,763<br>|12,506<br>|0,037<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|19.063|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|70|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-30: Tabla de incidencia del viento; Intervalo [16 - 20[ hrs. Mediciones sector**

**ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|2,159|1,431|0,037|-|-|-|3,627|
|**NNE**|-|2,563|0,419|-|-|-|-|2,982|
|**NE**|-|0,335|0,005|-|-|-|-|0,341|
|**ENE**|-|0,026|-|-|-|-|-|0,026|
|**E **|-|0,016|-|-|-|-|-|0,016|
|**ESE**|-|0,005|-|-|-|-|-|0,005|
|**SE**|-|0,010|-|-|-|-|-|0,010|
|**SSE**|-|0,031|-|-|-|-|-|0,031|
|**S **|-|0,477|0,168|-|-|-|-|0,645|
|**SSW**|-|21,353|26,202|0,010|-|-|-|47,565|
|**SW**|-|13,669|11,929|0,005|-|-|-|25,604|
|**WSW**|-|4,156|0,084|-|-|-|-|4,240|
|**W **|-|5,891|0,100|-|-|-|-|5,991|
|**WNW**|-|3,255|-|-|-|-|-|3,255|
|**NW**|-|3,491|0,031|-|-|-|-|3,522|
|**NNW**|-|1,557|0,283|-|-|-|-|1,840|
|**Calmas**|0,299|-|-|-|-|-|-|0,299|
|**Sub Total**<br>**(%)**<br>|0,299<br>|58,997<br>|40,652<br>|0,052<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|19.079|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|71|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-31: Tabla de incidencia del viento; Intervalo [20 - 0[ hrs. Mediciones sector ITI.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|1,464|0,420|-|-|-|-|1,884|
|**NNE**|-|1,999|0,220|-|-|-|-|2,220|
|**NE**|-|0,483|-|-|-|-|-|0,483|
|**ENE**|-|0,084|-|-|-|-|-|0,084|
|**E **|-|0,052|-|-|-|-|-|0,052|
|**ESE**|-|0,026|-|-|-|-|-|0,026|
|**SE**|-|0,121|-|-|-|-|-|0,121|
|**SSE**|-|0,582|0,010|-|-|-|-|0,593|
|**S **|-|3,542|0,294|-|-|-|-|3,836|
|**SSW**|-|39,583|15,203|-|-|-|-|54,786|
|**SW**|-|18,698|7,279|0,005|-|-|-|25,981|
|**WSW**|-|1,601|-|-|-|-|-|1,601|
|**W **|-|1,873|-|-|-|-|-|1,873|
|**WNW**|-|1,134|-|-|-|-|-|1,134|
|**NW**|-|1,217|-|-|-|-|-|1,217|
|**NNW**|-|0,913|0,073|-|-|-|-|0,987|
|**Calmas**|3,122|-|-|-|-|-|-|3,122|
|**Sub Total**<br>**(%)**<br>|3,122<br>|73,373<br>|23,499<br>|0,005<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|19.056|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|72|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Intervalo [0- 4[ hrs.**

**Intervalo [8- 12[ hrs.**

**Intervalo [16- 20[ hrs.**

**Intervalo [4- 8[ hrs.**

**Intervalo [12- 16[ hrs.**

**Intervalo [20- 0[ hrs.**

Fuente: Ecotecnos, 2021.
**Gráfico 4-20: Histograma de frecuencia relativa de la intensidad del viento por intervalos horarios. Mediciones sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|73|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Intervalo [0- 4[ hrs.**

**Intervalo [8- 12[ hrs.**

**Intervalo [16- 20[ hrs.**

**Intervalo [4- 8[ hrs.**

**Intervalo [12- 16[ hrs.**

**Intervalo [20- 0[ hrs.**

Fuente: Ecotecnos, 2021.
**Gráfico 4-21: Histograma de frecuencia relativa de la dirección del viento por intervalos horarios. Mediciones sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|74|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

|Intervalo [0- 4[ hrs.|Intervalo [4- 8[ hrs.|
|---|---|
|**Intervalo [8- 12[ hrs.**|**Intervalo [12- 16[ hrs.** <br>|
|**Intervalo [16- 20[ hrs.**|**Intervalo [20- 0[ hrs.**|

Fuente: Ecotecnos, 2021.
**Gráfico 4-22: Rosa de los vientos por intervalos. Mediciones sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|75|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Gráfico 4-23: Histograma de intensidad del viento promedio en un ciclo diario. Mediciones sector ITI.**

Fuente: Ecotecnos, 2021.
**Gráfico 4-24: Ocurrencia de la incidencia del viento por dirección en un ciclo diario. Mediciones sector ITI.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|76|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-32: Intensidades máxima globales y por dirección de procedencia de los vientos, por intervalos horarios. Mediciones**

**sector ITI.**

|Col1|Intensidad máxima del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Intervalos (hrs)**|**[0 - 4[**|**[0 - 4[**|**[4 - 8[**|**[4 - 8[**|**[8 - 12[**|**[8 - 12[**|**[12 - 16[**|**[12 - 16[**|**[16 - 20[**|**[16 - 20[**|**[20 - 0[**|**[20 - 0[**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N **|3,141|6,094|3,141|6,094|3,931|7,626|3,536|6,860|3,728|7,232|2,553|4,953|
|**NNE**|2,755|5,345|3,141|6,094|2,553|4,953|3,141|6,094|2,553|4,953|2,360|4,578|
|**NE**|2,553|4,953|2,360|4,578|2,553|4,953|1,773|3,440|1,570|3,046|1,175|2,280|
|**ENE**|1,773|3,440|2,553|4,953|2,948|5,719|2,360|4,578|0,588|1,141|1,175|2,280|
|**E **|1,175|2,280|1,570|3,046|1,965|3,812|2,553|4,953|0,588|1,141|0,790|1,533|
|**ESE**|1,378|2,673|1,965|3,812|2,158|4,187|2,553|4,953|0,395|0,766|1,175|2,280|
|**SE**|1,570|3,046|2,158|4,187|2,158|4,187|1,175|2,280|0,588|1,141|1,378|2,673|
|**SSE**|1,570|3,046|2,360|4,578|2,755|5,345|1,773|3,440|1,378|2,673|1,570|3,046|
|**S **|1,965|3,812|2,158|4,187|2,360|4,578|1,773|3,440|2,360|4,578|2,755|5,345|
|**SSW**|2,553|4,953|2,553|4,953|2,158|4,187|2,755|5,345|3,141|6,094|2,948|5,719|
|**SW**|2,158|4,187|1,965|3,812|1,773|3,440|2,948|5,719|3,141|6,094|3,141|6,094|
|**WSW**|1,378|2,673|1,570|3,046|2,360|4,578|1,773|3,440|1,773|3,440|1,378|2,673|
|**W **|1,378|2,673|1,175|2,280|1,773|3,440|1,570|3,046|1,773|3,440|1,378|2,673|
|**WNW**|1,378|2,673|0,983|1,907|1,570|3,046|1,570|3,046|1,378|2,673|1,175|2,280|
|**NW**|1,965|3,812|1,570|3,046|1,175|2,280|1,570|3,046|1,965|3,812|1,378|2,673|
|**NNW**|2,360|4,578|2,360|4,578|3,536|6,860|2,553|4,953|2,553|4,953|2,158|4,187|
|**Global**|3,141|6,094|3,141|6,094|3,931|7,626|3,536|6,860|3,728|7,232|3,141|6,094|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|77|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-33: Intensidades promedio globales y por dirección de procedencia de los vientos, por intervalos horarios Mediciones**

**sector ITI.**

|Col1|Intensidad promedio del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Intervalos (hrs)**|**[0 - 4[**|**[0 - 4[**|**[4 - 8[**|**[4 - 8[**|**[8 - 12[**|**[8 - 12[**|**[12 - 16[**|**[12 - 16[**|**[16 - 20[**|**[16 - 20[**|**[20 - 0[**|**[20 - 0[**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N **|1,039|2,016|0,905|1,756|0,910|1,765|1,065|2,065|1,443|2,800|1,138|2,207|
|**NNE**|0,956|1,854|1,000|1,940|0,777|1,507|0,914|1,773|1,124|2,181|0,938|1,820|
|**NE**|0,809|1,569|0,759|1,472|0,786|1,524|0,633|1,229|0,778|1,510|0,571|1,108|
|**ENE**|0,732|1,420|0,838|1,626|1,017|1,974|0,912|1,770|0,472|0,916|0,529|1,026|
|**E **|0,525|1,019|0,587|1,140|0,644|1,249|0,794|1,540|0,524|1,016|0,513|0,994|
|**ESE**|0,638|1,237|0,695|1,348|0,778|1,509|0,726|1,408|0,395|0,766|0,628|1,219|
|**SE**|0,571|1,108|0,607|1,177|0,636|1,234|0,626|1,215|0,492|0,954|0,659|1,278|
|**SSE**|0,587|1,139|0,584|1,134|0,576|1,117|0,668|1,296|0,689|1,337|0,734|1,425|
|**S **|0,696|1,350|0,587|1,139|0,572|1,109|0,692|1,342|1,084|2,103|0,885|1,716|
|**SSW**|0,822|1,595|0,719|1,395|0,662|1,284|1,151|2,234|1,523|2,955|1,229|2,384|
|**SW**|0,797|1,545|0,694|1,347|0,654|1,268|1,054|2,046|1,446|2,805|1,227|2,381|
|**WSW**|0,544|1,055|0,536|1,041|0,519|1,008|0,715|1,387|0,881|1,710|0,649|1,259|
|**W **|0,509|0,988|0,512|0,993|0,504|0,977|0,753|1,460|0,913|1,771|0,665|1,290|
|**WNW**|0,543|1,054|0,490|0,950|0,526|1,020|0,758|1,470|0,866|1,679|0,642|1,246|
|**NW**|0,620|1,202|0,590|1,144|0,549|1,065|0,749|1,453|0,904|1,754|0,662|1,285|
|**NNW**|0,837|1,624|0,773|1,499|0,871|1,689|0,896|1,738|1,081|2,097|0,815|1,582|
|**Global**|0,630|1,221|0,444|0,861|0,415|0,805|0,866|1,679|1,363|2,645|1,128|2,189|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|78|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 4.2 Correlación de la base de datos

Con el fin de realizar la correlación entre la serie de tiempo medida e histórica, se seleccionó
el periodo de medición en el sector de ITI, comprendido entre 14-02-2020 13:00 y el 17-032021 17:00, que se encuentra también en el registro de vientos de la estación del aeropuerto
Diego Aracena. El intervalo temporal escogido supera un año de mediciones y, por tanto,
contiene las variaciones estacionales del viento correspondientes a un año. El Gráfico 4-25
ilustra las correspondientes series de tiempo de los datos medidos e históricos de los
parámetros, en orden descendente:

 - Magnitud de la velocidad del viento,

 - Componentes U de la velocidad del viento,

 - Componentes V de la velocidad del viento,

 - Dirección del viento.

Adicionalmente, se realizaron los análisis de excedencia y cuantil-cuantil sobre los parámetros
mencionados, en el Gráfico 4-26 se incluyeron las ilustraciones de la magnitud y dirección del
viento, mientras que, el Gráfico 4-27 contiene las componentes ortogonales U y V del viento.

En cuanto a la intensidad del viento, ambos registros describen un comportamiento semejante
a lo largo del periodo analizado, aunque la estación medida presenta una intensidad del viento
menor que la histórica, lo cual puede deberse a la interacción del viento con estructuras
portuarias localizadas en el sector de ITI (p.e. grúas, buques, contenedores, etc.). A pesar de
ello, el coeficiente de correlación (R [2] ) presenta un elevado valor de 0,98 y, junto a esto, el error
cuadrático medio (RMS) es igual a 0,51 m/s. En las componentes ortogonales, la componente
U demuestra una menor energía en la estación medida, sobre todo en los valores positivos,
los cuales representan los vientos dirigidos hacia la tierra. Lo anterior se verifica en los análisis
de excedencia y cuantil - cuantil, pese a esto, el coeficiente de correlación (R [2] ) alcanza un
valor de 0,93 y un RMS de 0,58 m/s. En contraste, la serie de tiempo de la componente V
demuestra una gran semejanza en ambos registros, tanto en sus valores como en el
comportamiento durante el periodo de medición. La elevada similitud se refleja en su análisis
de excedencia y cuantil - cuantil, además de los estadísticos con un elevado R [2] de 0,98 y un
RMS de 0,24 m/s. Por último, en el parámetro dirección, en su serie de tiempo, se observa una
tendencia cercana al tercer cuadrante en ambos registros, además de una semejanza en las
variaciones de las direcciones del viento, las cuales oscilan de mayor forma durante el invierno.
La similitud en ambos registros se verifica en los gráficos de excedencia y de cuantil - cuantil,
y mediante los estadísticos, R [2] igual a 0,95 y un RMS de 28,13 °. En el gráfico cuantil - cuantil
se visualizan diferencias en las direcciones del primer y segundo cuadrante, sectores donde
hay menores ocurrencias de vientos, según lo señalado en el capítulo anterior. Debido a la
buena concordancia de la dirección y como este parámetro se construye a partir de las
componentes ortogonales, es posible asumir que la semejanza de la componente V presenta
un mayor peso que las diferencias de la componente U.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|79|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Gráfico 4-25: Serie de tiempo de la intensidad y dirección del viento. Medición y base de dato histórica, 2020-2021.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|80|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Gráfico 4-26: Análisis excedencias (izquierda) y cuantil-cuantil (derecha) de la**
**intensidad del viento (arriba) y dirección del viento (abajo) en la serie histórica vs serie**

**medida. Medición y base de dato histórica, 2020-2021.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|81|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Gráfico 4-27: Análisis excedencias (izquierda) y cuantil-cuantil (derecha) de la**
**componente U (arriba) y componente V (abajo) del viento en la serie histórica vs serie**

**medida. Medición y base de dato histórica, 2020-2021.**

Para analizar en forma más profunda la relación entre ambas series, se realizaron los análisis
de la correlación cruzada sobre las correspondientes componentes ortogonales (U y V) (Tabla
4-34 y Gráfico 4-28) para cada serie con desfases cada una hora durante ± 24 horas. Bajo
estas estimaciones, se identifica para la componente U un coeficiente máximo de correlación
de 0,625 y para la componente V de 0,603, estos valores se consiguieron para ambas variables
con bajos desfases temporales, además se verifica que se encontraron por sobre los limites

de confianza.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

82

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|
|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-34: Coeficientes de correlación en las componentes ortogonales en sus**

**respectivos desfases.**

|Desfase (hrs.)|Componente<br>U (-)|Componente<br>V (-)|Desfase (hrs.)|Componente<br>U (-)|Componente<br>V (-)|
|---|---|---|---|---|---|
|-24|-0,018|0,051|1|0,594|0,603|
|-23|0,043|0,057|2|0,501|0,566|
|-22|0,119|0,078|3|0,377|0,510|
|-21|0,201|0,107|4|0,250|0,440|
|-20|0,263|0,145|5|0,113|0,370|
|-19|0,324|0,185|6|-0,012|0,296|
|-18|0,364|0,230|7|-0,118|0,228|
|-17|0,361|0,262|8|-0,192|0,161|
|-16|0,323|0,276|9|-0,224|0,122|
|-15|0,264|0,284|10|-0,214|0,094|
|-14|0,178|0,282|11|-0,157|0,092|
|-13|0,085|0,272|12|-0,080|0,107|
|-12|-0,015|0,246|13|0,015|0,133|
|-11|-0,103|0,218|14|0,122|0,168|
|-10|-0,169|0,187|15|0,212|0,207|
|-9|-0,201|0,160|16|0,286|0,246|
|-8|-0,188|0,128|17|0,339|0,277|
|-7|-0,134|0,114|18|0,350|0,281|
|-6|-0,052|0,132|19|0,333|0,285|
|-5|0,061|0,174|20|0,291|0,270|
|-4|0,198|0,243|21|0,224|0,240|
|-3|0,337|0,337|22|0,149|0,206|
|-2|0,461|0,431|23|0,080|0,170|
|-1|0,562|0,529|24|0,011|0,128|
|0|0,625|0,601|<br> <br>|<br> <br>|<br> <br>|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|83|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Gráfico 4-28: Correlación cruzada de las componentes ortogonales del viento.**

**Medición y base de dato histórica, 2020-2021.**

En el Gráfico 4-29 se ilustraron los respectivos espectros de las componentes ortogonales de
cada registro para su comparación, donde se evidencia una clara similitud entre registros en
la forma de la densidad espectral. Tanto en la medición como en la señal histórica se destacan
los peaks correspondientes al ciclo diurno (24 horas) y ciclo semidiurno (12 horas) para ambas
componentes. En la componente U se evidencian diferencias sobre las menores frecuencias
donde la serie histórica señala una mayor energía. Estas frecuencias se pueden asociar a
fenómenos de mayor escala, como efectos sinópticos. En contraste, la componente V presenta
una elevada similitud en ambos registros, además, se debe recalcar que, la energía
correspondiente a la componente V contiene una mayor magnitud que en la componente U,
respaldando la mayor relevancia de la componente V.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Informe Técnic<br>Oceanografía Física y Modelam<br>Estudio de Vient|o<br>iento Numérico::<br>os|No DOCUMENTO EDICIÓN / REVISIÓN<br>IT-ITI-VIENTOS2021 1/1|84|
|---|---|---|---|
|<br>**Informe Técnic**<br>**Oceanografía Física y Modelam**<br>**Estudio de Vient**|**o**<br>**iento Numérico::**<br>**os**|Fecha de emisión:<br>09-07-2021<br>Emitido por:<br>Ecotecnos S.A.|Fecha de emisión:<br>09-07-2021<br>Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Gráfico 4-29: Comparación entre espectros de la componente U (izquierda) y de la**

**componente V (derecha). Medición y base de dato histórica, 2020-2021.**

Para complementar los resultados anteriormente señalados, se estimaron los principales
estadísticos de la intensidad (Tabla 4-35) y para la dirección del viento (Tabla 4-36), tanto para
los registros del sector de estudio, como para la base histórica. La intensidad del viento se
analizó mediante el promedio, desviación estándar, percentil 75 y percentil 25, cabe señalar
que los estadísticos de la dirección se obtuvieron de manera vectorial.

En los valores estadísticos de la intensidad, se estima una diferencia de sus valores promedios
de 0,47 m/s, siendo el valor medio del registro histórico el mayor. Tras la estimación de los
percentiles 75 y 25, los valores de la estación histórica continúan siendo los mayores,
presentando diferencias de 0,24 m/s y 0,72 m/s, respectivamente. Sobre la direccionalidad del
viento, se verifica que, en ambos registros, la dirección media se localiza en el tercer
cuadrante, con una diferencia de 12,22 °.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|85|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-35: Estadística magnitud del viento entre estaciones meteorológicas. Medición**

**y base de dato histórica, 2020-2021.**

|Magnitud viento (m/s)|Medición|Histórica|Diferencia|
|---|---|---|---|
|**Promedio**|0,81|1,28|0,47|
|**Desviación estándar**|0,58|0,76|0,18|
|**75 Percentil**|0,40|0,63|0,24|
|**25 Percentil**|1,18|1,90|0,72|

Fuente: Ecotecnos, 2021.

**Tabla 4-36: Estadística direccional del viento entre estaciones meteorológicas.**

**Medición y base de dato histórica, 2020-2021.**

|Col1|Medición|Histórica|Diferencia|
|---|---|---|---|
|**U promedio (m/s)**|0,38|0,83|-0,45|
|**V promedio (m/s)**|0,49|0,70|-0,21|
|**Dirección promedio (°)**|217,69|229,91|-12,22|

Fuente: Ecotecnos, 2021.

En base de los resultados antes expuestos, es posible establecer la relación del
comportamiento de las intensidades del viento entre las mediciones efectuadas por la DMC,
en el aeropuerto Diego Aracena, con la zona de estudio, en el sector de ITI. Pese a la presencia
de algunos diferenciales en las magnitudes del viento, tras analizar las componentes
ortogonales, se verifica que las diferencias se concentran en la componente U, mientras que,
la componente V, coinciden tanto en comportamiento como magnitud, siendo esta última la
componente más energética. La direccionalidad obtenida en ambas series, describen
direcciones desde el tercer cuadrante con una baja diferencia en sus valores medios. Es
importante agregar que, como la intensidad del viento en el sector de ITI puede encontrarse
reducida por el obstáculo de estructuras portuarias, una sobrestimación de la base de datos
históricas se vuelve aceptable.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|86|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 4.3 Análisis y Caracterización Estadística de la base de datos histórica

**4.3.1 Estadística Descriptiva**

La base de datos histórica, representada en forma de chascones (Gráfico 4-30), exhibe el
predominio del viento desde el tercer cuadrante a lo largo de la base de datos, con la aparición
de vientos ocasionales desde el primer y cuarto cuadrante. Los datos correspondientes a la
intensidad del viento se señalaron mediante tabla de incidencia (Tabla 4-37) e histogramas
(Gráfico 4-31), según la categorización de la escala de Beaufort. En la base de datos histórica
se encuentran las categorías Calmas (0,00 - 0,28 m/s), Aire Ligero (0,28-1,39 m/s), Brisa
Ligera (1,39 - 3,06 m/s), Brisa Suave (3,06 - 5,28 m/s) y Brisa Moderada (5,28 - 7,78 m/s). El
predominio se encuentra en la categoría Aire Ligero con una frecuencia de 52,561 % y, en
segundo lugar, la Brisa Ligera con 39,553 %. En contraste, las categorías de Brisa Suave y
Brisa Moderada se presentaron bajo el 2 % de los casos. Las Calmas ocurren el 6,417 % de
los casos, de las cuales su direccionalidad fue despreciada.

Las direcciones de la base de datos histórica se representaron mediante tabla de incidencia
(Tabla 4-37), histograma (Gráfico 4-32) y rosa de vientos (Gráfico 4-33). En su mayoría, el
viento proviene desde el tercer cuadrante, predominando la dirección SSW (24,736 %) y,
luego, en orden de ocurrencia, la dirección S (16,106 %), SW (15,693 %) y WSW (8,963 %).
La ocurrencia del resto de las direcciones, en los otros cuadrantes, se encuentran bajo el 5 %,

de cada una.

Fuente: Ecotecnos, 2021.
**Gráfico 4-30: Registro vectorial del viento. Base de datos histórica.**

En la Gráfico 4-34 y la Tabla 4-38 se obtuvieron los registros máximos y medios por direcciones
de la base de datos histórica, donde resalta el mayor valor, 5,529 m/s (10,726 nudos)
provenientes desde la dirección E. En el promedio por direcciones destaca la mayor magnitud
desde la dirección SSW el valor 1,749 m/s (3,393 nudos). Las intensidades medias más
grandes se encuentran en las cercanías de tercer cuadrante y los menores valores se estiman
en el segundo cuadrante.

De la base de datos históricas se estudiaron las componentes ortogonales del viento mediante
sus principales estadísticos (Tabla 4-39). Para la componente U se estima un valor medio de

<!-- INICIO TABLA 4-39 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|91| |---|---|---|---|---| ||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.| -->

**Tabla 4-39: Valores estadísticos de las componentes ortogonales de la intensidad del****

| Valores | Componente U | Componente V |
| --- | --- | --- |
| **Promedio (m/s)** | 0,535 | 0,909 |
| **Desviación estándar (m/s)** | 0,721 | 0,859 |
| **Máximo (m/s)** | 3,265 | 4,356 |
| **Mínimo (m/s)** | -5,445 | -2,843 |
| **Porcentaje de participación (%)** | 39,585 | 60,415 |

<!-- Estadísticas: 5 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Ecotecnos, 2021. Fuente: Ecotecnos, 2021. **Gráfico 4-35: Valores centrados de las componentes ortogonales junto a su** -->
<!-- FIN TABLA 4-39 -->

0,535 m/s, representando su tendencia hacia la dirección E, donde su valor máximo y mínimo
corresponde a 3,265 m/s y -5,445 m/s, respectivamente. Por su parte, la componente V

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|87|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

presenta un valor medio de 0,909 m/s, indicando la tendencia del viento hacia la dirección N,
dentro de los valores extremos 4,356 m/s y -2,843 m/s. Respecto a la desviación estándar
señalada, los valores en la componente V experimentan una mayor dispersión (0,859 m/s),
que la componente U (0,721 m/s). Con la información analizada se determina una componente
principal (PCA) que demuestra la representación sobre el 70% de la varianza de los datos y,
dentro de la cual, la mayor participación corresponde a la componente V con 60,415 %, frente
a la componente U con 39,585 %.

Fuente: Ecotecnos, 2021.
**Gráfico 4-31: Histograma de frecuencia relativa de la intensidad del viento. Base de**

**datos histórica.**

Fuente: Ecotecnos, 2021.
**Gráfico 4-32: Histograma de frecuencia relativa de la dirección del viento. Base de**

**datos histórica**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|88|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Gráfico 4-33: Rosa de intensidad por dirección del viento. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|89|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-37: Tabla de incidencia del viento. Base de datos histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|1,837|0,240|-|-|-|-|2,078|
|**NNE**|-|1,182|0,047|-|-|-|-|1,229|
|**NE**|-|0,893|0,012|-|-|-|-|0,905|
|**ENE**|-|1,111|0,018|-|-|-|-|1,129|
|**E **|-|2,272|0,131|0,001|0,002|-|-|2,406|
|**ESE**|-|2,555|0,254|-|-|-|-|2,809|
|**SE**|-|2,544|0,181|-|-|-|-|2,725|
|**SSE**|-|3,783|0,332|-|-|-|-|4,115|
|**S **|-|10,091|5,906|0,108|-|-|-|16,106|
|**SSW**|-|8,353|15,427|0,956|-|-|-|24,736|
|**SW**|-|4,922|10,389|0,382|-|-|-|15,693|
|**WSW**|-|3,853|5,090|0,020|-|-|-|8,963|
|**W **|-|3,419|1,083|-|-|-|-|4,502|
|**WNW**|-|1,641|0,190|-|-|-|-|1,831|
|**NW**|-|1,263|0,055|-|-|-|-|1,318|
|**NNW**|-|1,453|0,196|-|-|-|-|1,649|
|**VRB**|-|1,387|0,003|-|-|-|-|1,390|
|**Calmas**|6,417|-|-|-|-|-|-|6,417|
|**Sub Total**<br>**(%)**<br>|6,417<br>|52,561<br>|39,553<br>|1,467<br>|0,002<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|89.472|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|90|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Gráfico 4-34: Variación de la magnitud promedio y máxima del viento por dirección de**

**procedencia. Base de datos histórica.**

**Tabla 4-38: Intensidades promedio y máxima globales y por dirección de procedencia**

**de los vientos. Base de datos histórica.**

|Col1|Intensidad del viento|Col3|Col4|Col5|
|---|---|---|---|---|
|**Direcciones**|**Máxima**|**Máxima**|**Promedio**|**Promedio**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N **|2,843|5,515|0,837|1,624|
|**NNE**|2,370|4,598|0,716|1,389|
|**NE**|1,896|3,678|0,672|1,304|
|**ENE**|1,896|3,678|0,649|1,259|
|**E **|5,529|10,726|0,720|1,396|
|**ESE**|2,370|4,598|0,804|1,561|
|**SE**|3,001|5,822|0,782|1,518|
|**SSE**|3,001|5,822|0,826|1,603|
|**S **|4,423|8,581|1,257|2,439|
|**SSW**|4,423|8,581|1,749|3,393|
|**SW**|4,107|7,968|1,707|3,312|
|**WSW**|3,475|6,742|1,463|2,838|
|**W **|2,528|4,904|1,017|1,973|
|**WNW**|2,843|5,515|0,872|1,692|
|**NW**|2,528|4,904|0,792|1,537|
|**NNW**|2,686|5,211|0,865|1,677|
|**Global**|5,529|10,726|1,261|2,447|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|91|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-39 Valores estadísticos de las componentes ortogonales de la intensidad del**

**viento. Base de datos histórica.**

|Valores|Componente U|Componente V|
|---|---|---|
|**Promedio (m/s)**|0,535|0,909|
|**Desviación estándar (m/s)**|0,721|0,859|
|**Máximo (m/s)**|3,265|4,356|
|**Mínimo (m/s)**|-5,445|-2,843|
|**Porcentaje de participación (%)**|39,585|60,415|

Fuente: Ecotecnos, 2021.

Fuente: Ecotecnos, 2021.
**Gráfico 4-35: Valores centrados de las componentes ortogonales junto a su**

**componente principal. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|92|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**4.3.2 Análisis Espectral**

Sobre las componentes ortogonales del viento, correspondientes a la base de datos histórica,
se realizó un análisis de densidad espectral (Gráfico 4-36). Para ambas componentes
ortogonales se evidencian los peak energéticos correspondientes a los ciclos diurnos
(24 horas) y semidiurnos (12 horas), los cuales pueden responder al fenómeno de brisa
marina, el que se relaciona con los diferenciales térmicos durante el día y noche, causado por
la capacidad calorífica entre el mar y la tierra. En las frecuencias más altas se revelan altas
concentraciones de energía, así como peak más pequeños. Esta energía es asociable a la
turbulencia generada por efecto de la capa límite y podrían resultar un aporte importante a las
características energéticas del viento. Por otro lado, las menores frecuencias presentan una
menor energía, las cuales se relacionan con fenómenos de mayor escala, tales como efectos
sinópticos y/o meteorológicos en la capa geostrófica. En estas frecuencias se hace notoria la
mayor energía de la componente V, en comparación con la componente U.

Fuente: Ecotecnos, 2021.
**Gráfico 4-36: Densidad espectral de las componentes U y V del viento. Base de datos**

**histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|93|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**4.3.3 Caracterización Estadística -Mensual**

Con la estimación del valor medio de cada registro horario, por cada mes correspondiente en
un año, durante la totalidad de la base de datos (incluidos el 29 de febrero en años bisiestos),
se obtuvo un año medio. Cada mes estimado fue analizado según su respectiva intensidad y

dirección del viento.

La intensidad del viento de los distintos meses es clasificada según la escala de Beaufort y
analizada mediante tablas de incidencia (desde la Tabla 4-40 a la Tabla 4-51) y con apoyo de
histogramas (Gráfico 4-37 y Gráfico 4-38). Tras el cálculo de año medio, solo se presentan las
categorías Aire Ligero (0,28 - 1,39 m/s) y Brisa Ligera (1,39 - 3,06 m/s). En el mes de enero
predomina levemente la categoría Brisa Ligera (50,269 %), lo cual cambia desde el mes de
marzo, cuando la categoría Aire Ligero toma el predominio (52,016 %). Con el paso de los
meses incrementa progresivamente la frecuencia de esta categoría hasta el mes de junio
cuando el Aire Ligero alcanza una ocurrencia de 75,000 %. A partir de julio, la categoría Aire
Ligero (73,387 %) comienza a reducirse y a incrementarse la Brisa Ligera (26,478 %),
progresivamente, hasta el mes de diciembre cuando las ocurrencias de las categorías
mencionadas alcanzan 51,882 % y 48,118 %, respectivamente. En el ciclo mensual de
intensidades (Gráfico 4-43) se identifican las intensidades medias por mes, de las cuales,
destaca el mes de febrero con la mayor intensidad, 1,544 m/s, y el mes de junio con la menor
intensidad, igual a 1,019 m/s.

La direccionalidad del año medio del registro histórico se analiza mediante tablas de
incidencias (desde la Tabla 4-40 a la Tabla 4-51), histogramas (Gráfico 4-39 y Gráfico 4-40) y
rosas de vientos (Gráfico 4-41 y Gráfico 4-42) y, junto a esto, se agrega el ciclo mensual
(Gráfico 4-44). En los meses analizados se evidencia el predominio del tercer cuadrante, en
general, en las direcciones S y SSW. Entre los meses abril y agosto las direcciones
incrementan su dispersión aumentando la ocurrencia de direcciones desde el segundo
cuadrante. Los vientos provenientes desde esta dirección, generalmente, presentan una

menor intensidad.

Tras la búsqueda de los mayores datos por mes y dirección en el año medio (Tabla 4-52 y
Tabla 4-53) se estima que la mayor intensidad corresponde a 2,930 m/s (5,683 nudos) durante
el mes de enero, proveniente de la dirección SSW. En general, las intensidades más grandes
pertenecen al tercer cuadrante y, en contraste, en el primer y cuarto cuadrante se estiman los
menores valores, además en varias ocasiones no se encuentran datos en estas direcciones.
Con la obtención de los valores medios por dirección y mes (Tabla 4-54 y Tabla 4-55) se
visualiza que el mayor valor medio corresponde a mes de diciembre, desde la dirección SW,
siendo igual a 1,960 m/s (3,803 nudos). Los mayores valores medios se concentran en el tercer
cuadrante, en la cercanía de la dirección SW.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|94|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-40: Tabla de incidencia del viento, enero promedio. Base de datos histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|-|-|-|-|-|-|0,000|
|**NNE**|-|-|-|-|-|-|-|0,000|
|**NE**|-|-|-|-|-|-|-|0,000|
|**ENE**|-|-|-|-|-|-|-|0,000|
|**E **|-|-|-|-|-|-|-|0,000|
|**ESE**|-|0,403|-|-|-|-|-|0,403|
|**SE**|-|2,688|-|-|-|-|-|2,688|
|**SSE**|-|9,274|-|-|-|-|-|9,274|
|**S **|-|20,968|1,075|-|-|-|-|22,043|
|**SSW**|-|11,290|23,118|-|-|-|-|34,409|
|**SW**|-|4,704|26,075|-|-|-|-|30,780|
|**WSW**|-|0,403|-|-|-|-|-|0,403|
|**W **|-|-|-|-|-|-|-|0,000|
|**WNW**|-|-|-|-|-|-|-|0,000|
|**NW**|-|-|-|-|-|-|-|0,000|
|**NNW**|-|-|-|-|-|-|-|0,000|
|**Calmas**|-|-|-|-|-|-|-|0,000|
|**Sub Total**<br>**(%)**<br>|0,000<br>|49,731<br>|50,269<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|744|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|95|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-41: Tabla de incidencia del viento, febrero promedio. Base de datos histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|-|-|-|-|-|-|0,000|
|**NNE**|-|-|-|-|-|-|-|0,000|
|**NE**|-|0,144|-|-|-|-|-|0,144|
|**ENE**|-|-|-|-|-|-|-|0,000|
|**E **|-|-|-|-|-|-|-|0,000|
|**ESE**|-|-|-|-|-|-|-|0,000|
|**SE**|-|1,149|-|-|-|-|-|1,149|
|**SSE**|-|5,316|-|-|-|-|-|5,316|
|**S **|-|28,017|0,431|-|-|-|-|28,448|
|**SSW**|-|11,638|32,615|-|-|-|-|44,253|
|**SW**|-|2,155|18,103|-|-|-|-|20,259|
|**WSW**|-|0,287|0,144|-|-|-|-|0,431|
|**W **|-|-|-|-|-|-|-|0,000|
|**WNW**|-|-|-|-|-|-|-|0,000|
|**NW**|-|-|-|-|-|-|-|0,000|
|**NNW**|-|-|-|-|-|-|-|0,000|
|**Calmas**|-|-|-|-|-|-|-|0,000|
|**Sub Total**<br>**(%)**<br>|0,000<br>|48,707<br>|51,293<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|696|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|96|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-42: Tabla de incidencia del viento, marzo promedio. Base de datos histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|-|-|-|-|-|-|0,000|
|**NNE**|-|-|-|-|-|-|-|0,000|
|**NE**|-|-|-|-|-|-|-|0,000|
|**ENE**|-|-|-|-|-|-|-|0,000|
|**E **|-|-|-|-|-|-|-|0,000|
|**ESE**|-|-|-|-|-|-|-|0,000|
|**SE**|-|1,075|-|-|-|-|-|1,075|
|**SSE**|-|9,946|-|-|-|-|-|9,946|
|**S **|-|28,360|2,016|-|-|-|-|30,376|
|**SSW**|-|9,677|28,360|-|-|-|-|38,038|
|**SW**|-|2,285|17,070|-|-|-|-|19,355|
|**WSW**|-|0,672|0,269|-|-|-|-|0,941|
|**W **|-|-|-|-|-|-|-|0,000|
|**WNW**|-|-|-|-|-|-|-|0,000|
|**NW**|-|-|-|-|-|-|-|0,000|
|**NNW**|-|-|-|-|-|-|-|0,000|
|**Calmas**|0,269|-|-|-|-|-|-|0,269|
|**Sub Total**<br>**(%)**<br>|0,269<br>|52,016<br>|47,715<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|744|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|97|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-43: Tabla de incidencia del viento, abril promedio. Base de datos histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|-|-|-|-|-|-|0,000|
|**NNE**|-|-|-|-|-|-|-|0,000|
|**NE**|-|-|-|-|-|-|-|0,000|
|**ENE**|-|-|-|-|-|-|-|0,000|
|**E **|-|-|-|-|-|-|-|0,000|
|**ESE**|-|0,417|-|-|-|-|-|0,417|
|**SE**|-|4,306|-|-|-|-|-|4,306|
|**SSE**|-|17,500|-|-|-|-|-|17,500|
|**S **|-|24,306|2,778|-|-|-|-|27,083|
|**SSW**|-|7,222|22,083|-|-|-|-|29,306|
|**SW**|-|2,500|18,056|-|-|-|-|20,556|
|**WSW**|-|0,417|-|-|-|-|-|0,417|
|**W **|-|-|-|-|-|-|-|0,000|
|**WNW**|-|-|-|-|-|-|-|0,000|
|**NW**|-|-|-|-|-|-|-|0,000|
|**NNW**|-|-|-|-|-|-|-|0,000|
|**Calmas**|0,417|-|-|-|-|-|-|0,417|
|**Sub Total**<br>**(%)**<br>|0,417<br>|56,667<br>|42,917<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|720|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|98|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-44: Tabla de incidencia del viento, mayo promedio. Base de datos histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|-|-|-|-|-|-|0,000|
|**NNE**|-|-|-|-|-|-|-|0,000|
|**NE**|-|0,269|-|-|-|-|-|0,269|
|**ENE**|-|0,403|-|-|-|-|-|0,403|
|**E **|-|1,075|-|-|-|-|-|1,075|
|**ESE**|-|4,839|-|-|-|-|-|4,839|
|**SE**|-|9,409|-|-|-|-|-|9,409|
|**SSE**|-|16,935|-|-|-|-|-|16,935|
|**S **|-|15,457|0,269|-|-|-|-|15,726|
|**SSW**|-|12,231|7,124|-|-|-|-|19,355|
|**SW**|-|4,301|22,984|-|-|-|-|27,285|
|**WSW**|-|2,419|2,151|-|-|-|-|4,570|
|**W **|-|-|-|-|-|-|-|0,000|
|**WNW**|-|-|-|-|-|-|-|0,000|
|**NW**|-|-|-|-|-|-|-|0,000|
|**NNW**|-|-|-|-|-|-|-|0,000|
|**Calmas**|0,134|-|-|-|-|-|-|0,134|
|**Sub Total**<br>**(%)**<br>|0,134<br>|67,339<br>|32,527<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|744|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|99|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-45: Tabla de incidencia del viento, junio promedio. Base de datos histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|0,417|-|-|-|-|-|0,417|
|**NNE**|-|0,694|-|-|-|-|-|0,694|
|**NE**|-|0,972|-|-|-|-|-|0,972|
|**ENE**|-|1,389|-|-|-|-|-|1,389|
|**E **|-|2,083|-|-|-|-|-|2,083|
|**ESE**|-|4,861|-|-|-|-|-|4,861|
|**SE**|-|10,694|-|-|-|-|-|10,694|
|**SSE**|-|12,222|-|-|-|-|-|12,222|
|**S **|-|10,694|-|-|-|-|-|10,694|
|**SSW**|-|15,694|3,750|-|-|-|-|19,444|
|**SW**|-|6,944|16,806|-|-|-|-|23,750|
|**WSW**|-|6,528|4,444|-|-|-|-|10,972|
|**W **|-|1,111|-|-|-|-|-|1,111|
|**WNW**|-|0,417|-|-|-|-|-|0,417|
|**NW**|-|0,278|-|-|-|-|-|0,278|
|**NNW**|-|-|-|-|-|-|-|0,000|
|**Calmas**|-|-|-|-|-|-|-|0,000|
|**Sub Total**<br>**(%)**<br>|0,000<br>|75,000<br>|25,000<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|720|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|100|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-46: Tabla de incidencia del viento, julio promedio. Base de datos histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|1,075|-|-|-|-|-|1,075|
|**NNE**|-|1,344|-|-|-|-|-|1,344|
|**NE**|-|1,210|-|-|-|-|-|1,210|
|**ENE**|-|0,941|-|-|-|-|-|0,941|
|**E **|-|1,882|-|-|-|-|-|1,882|
|**ESE**|-|5,376|-|-|-|-|-|5,376|
|**SE**|-|7,796|-|-|-|-|-|7,796|
|**SSE**|-|11,022|-|-|-|-|-|11,022|
|**S **|-|8,065|-|-|-|-|-|8,065|
|**SSW**|-|11,828|1,747|-|-|-|-|13,575|
|**SW**|-|11,828|16,532|-|-|-|-|28,360|
|**WSW**|-|6,586|7,930|-|-|-|-|14,516|
|**W **|-|1,613|0,269|-|-|-|-|1,882|
|**WNW**|-|1,075|-|-|-|-|-|1,075|
|**NW**|-|0,806|-|-|-|-|-|0,806|
|**NNW**|-|0,941|-|-|-|-|-|0,941|
|**Calmas**|0,134|-|-|-|-|-|-|0,134|
|**Sub Total**<br>**(%)**<br>|0,134<br>|73,387<br>|26,478<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|744|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|101|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-47: Tabla de incidencia del viento, agosto promedio. Base de datos histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|0,941|-|-|-|-|-|0,941|
|**NNE**|-|0,672|-|-|-|-|-|0,672|
|**NE**|-|0,672|-|-|-|-|-|0,672|
|**ENE**|-|0,538|-|-|-|-|-|0,538|
|**E **|-|1,613|-|-|-|-|-|1,613|
|**ESE**|-|3,495|-|-|-|-|-|3,495|
|**SE**|-|9,946|-|-|-|-|-|9,946|
|**SSE**|-|7,527|-|-|-|-|-|7,527|
|**S **|-|5,511|-|-|-|-|-|5,511|
|**SSW**|-|10,081|1,747|-|-|-|-|11,828|
|**SW**|-|13,575|15,591|-|-|-|-|29,167|
|**WSW**|-|5,914|12,500|-|-|-|-|18,414|
|**W **|-|3,898|0,538|-|-|-|-|4,435|
|**WNW**|-|2,151|-|-|-|-|-|2,151|
|**NW**|-|1,344|-|-|-|-|-|1,344|
|**NNW**|-|1,747|-|-|-|-|-|1,747|
|**Calmas**|-|-|-|-|-|-|-|0,000|
|**Sub Total**<br>**(%)**<br>|0,000<br>|69,624<br>|30,376<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|744|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|102|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-48: Tabla de incidencia del viento, septiembre promedio. Base de datos**

**histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|0,139|-|-|-|-|-|0,139|
|**NNE**|-|-|-|-|-|-|-|0,000|
|**NE**|-|-|-|-|-|-|-|0,000|
|**ENE**|-|-|-|-|-|-|-|0,000|
|**E **|-|0,278|-|-|-|-|-|0,278|
|**ESE**|-|0,972|-|-|-|-|-|0,972|
|**SE**|-|2,083|-|-|-|-|-|2,083|
|**SSE**|-|6,111|-|-|-|-|-|6,111|
|**S **|-|12,222|-|-|-|-|-|12,222|
|**SSW**|-|12,917|3,750|-|-|-|-|16,667|
|**SW**|-|15,694|22,639|-|-|-|-|38,333|
|**WSW**|-|9,028|11,111|-|-|-|-|20,139|
|**W **|-|2,222|0,556|-|-|-|-|2,778|
|**WNW**|-|0,139|-|-|-|-|-|0,139|
|**NW**|-|0,139|-|-|-|-|-|0,139|
|**NNW**|-|-|-|-|-|-|-|0,000|
|**Calmas**|-|-|-|-|-|-|-|0,000|
|**Sub Total**<br>**(%)**<br>|0,000<br>|61,944<br>|38,056<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|720|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|103|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-49: Tabla de incidencia del viento, octubre promedio. Base de datos histórica**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|-|-|-|-|-|-|0,000|
|**NNE**|-|-|-|-|-|-|-|0,000|
|**NE**|-|0,134|-|-|-|-|-|0,134|
|**ENE**|-|-|-|-|-|-|-|0,000|
|**E **|-|-|-|-|-|-|-|0,000|
|**ESE**|-|0,269|-|-|-|-|-|0,269|
|**SE**|-|1,075|-|-|-|-|-|1,075|
|**SSE**|-|4,167|-|-|-|-|-|4,167|
|**S **|-|12,231|-|-|-|-|-|12,231|
|**SSW**|-|21,774|7,930|-|-|-|-|29,704|
|**SW**|-|12,500|25,134|-|-|-|-|37,634|
|**WSW**|-|5,511|7,661|-|-|-|-|13,172|
|**W **|-|0,806|0,134|-|-|-|-|0,941|
|**WNW**|-|0,403|-|-|-|-|-|0,403|
|**NW**|-|0,269|-|-|-|-|-|0,269|
|**NNW**|-|-|-|-|-|-|-|0,000|
|**Calmas**|-|-|-|-|-|-|-|0,000|
|**Sub Total**<br>**(%)**<br>|0,000<br>|59,140<br>|40,860<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|744|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|104|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-50: Tabla de incidencia del viento, noviembre promedio. Base de datos**

**histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|-|-|-|-|-|-|0,000|
|**NNE**|-|-|-|-|-|-|-|0,000|
|**NE**|-|-|-|-|-|-|-|0,000|
|**ENE**|-|-|-|-|-|-|-|0,000|
|**E **|-|0,139|-|-|-|-|-|0,139|
|**ESE**|-|0,694|-|-|-|-|-|0,694|
|**SE**|-|1,806|-|-|-|-|-|1,806|
|**SSE**|-|7,778|-|-|-|-|-|7,778|
|**S **|-|16,111|-|-|-|-|-|16,111|
|**SSW**|-|19,306|10,556|-|-|-|-|29,861|
|**SW**|-|5,278|27,222|-|-|-|-|32,500|
|**WSW**|-|3,472|7,083|-|-|-|-|10,556|
|**W **|-|0,278|0,139|-|-|-|-|0,417|
|**WNW**|-|-|-|-|-|-|-|0,000|
|**NW**|-|-|-|-|-|-|-|0,000|
|**NNW**|-|-|-|-|-|-|-|0,000|
|**Calmas**|0,139|-|-|-|-|-|-|0,139|
|**Sub Total**<br>**(%)**<br>|0,139<br>|54,861<br>|45,000<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|720|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|105|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-51: Tabla de incidencia del viento, diciembre promedio. Base de datos**

**histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N **|-|-|-|-|-|-|-|0,000|
|**NNE**|-|-|-|-|-|-|-|0,000|
|**NE**|-|-|-|-|-|-|-|0,000|
|**ENE**|-|-|-|-|-|-|-|0,000|
|**E **|-|-|-|-|-|-|-|0,000|
|**ESE**|-|0,134|-|-|-|-|-|0,134|
|**SE**|-|3,360|-|-|-|-|-|3,360|
|**SSE**|-|12,769|-|-|-|-|-|12,769|
|**S **|-|17,339|0,134|-|-|-|-|17,473|
|**SSW**|-|13,710|15,323|-|-|-|-|29,032|
|**SW**|-|4,167|32,124|-|-|-|-|36,290|
|**WSW**|-|0,403|0,538|-|-|-|-|0,941|
|**W **|-|-|-|-|-|-|-|0,000|
|**WNW**|-|-|-|-|-|-|-|0,000|
|**NW**|-|-|-|-|-|-|-|0,000|
|**NNW**|-|-|-|-|-|-|-|0,000|
|**Calmas**|-|-|-|-|-|-|-|0,000|
|**Sub Total**<br>**(%)**<br>|0,000<br>|51,882<br>|48,118<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|744|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|106|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Enero**

**Marzo**

**Mayo**

**Febrero**

**Abril**

**Junio**

Fuente: Ecotecnos, 2021.
**Gráfico 4-37: Histogramas de intensidad del viento promedio entre los meses enero y junio. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|107|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Julio**

**Septiembre**

**Noviembre**

**Agosto**

**Octubre**

**Diciembre**

Fuente: Ecotecnos, 2021.
**Gráfico 4-38: Histogramas de intensidad del viento promedio entre los meses julio y diciembre. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|108|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Enero**

**Marzo**

**Mayo**

**Febrero**

**Abril**

**Junio**

Fuente: Ecotecnos, 2021.
**Gráfico 4-39: Histogramas de dirección del viento promedio entre los meses enero y junio. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|109|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Julio**

**Septiembre**

**Noviembre**

**Agosto**

**Octubre**

**Diciembre**

Fuente: Ecotecnos, 2021.
**Gráfico 4-40: Histogramas de dirección del viento promedio entre los meses julio y diciembre. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|110|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

|Enero|Febrero|
|---|---|
|**Marzo**|**Abril**|
|**Mayo**|**Junio**|

Fuente: Ecotecnos, 2021.
**Gráfico 4-41: Rosa de los vientos entre los meses enero y junio. Base de datos**

**histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|111|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

|Julio|Agosto|
|---|---|
|**Septiembre**|**Octubre**|
|**Noviembre**|**Diciembre**|

Fuente: Ecotecnos, 2021.
**Gráfico 4-42: Rosa de los vientos entre los meses julio y diciembre. Base de datos**

**histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|112|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Gráfico 4-43: Histograma de intensidad del viento promedio en un ciclo anual. Base de datos histórica.**

Fuente: Ecotecnos, 2021.
**Gráfico 4-44: Ocurrencia de la incidencia del viento por dirección en un ciclo anual. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|113|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-52: Intensidades máxima globales y por dirección de procedencia de los vientos, entre los meses enero-junio. Base de**

**datos histórica.**

|Col1|Intensidad máxima del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Meses**|**Enero**|**Enero**|**Febrero**|**Febrero**|**Marzo**|**Marzo**|**Abril**|**Abril**|**Mayo**|**Mayo**|**Junio**|**Junio**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N **|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,553|1,073|
|**NNE**|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,679|1,318|
|**NE**|0,000|0,000|0,474|0,920|0,000|0,000|0,000|0,000|0,632|1,226|0,853|1,655|
|**ENE**|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,743|1,441|1,043|2,023|
|**E **|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,885|1,717|0,980|1,900|
|**ESE**|0,761|1,477|0,000|0,000|0,000|0,000|0,711|1,379|0,948|1,839|1,059|2,054|
|**SE**|0,704|1,365|0,869|1,686|0,934|1,811|0,901|1,747|0,995|1,931|1,074|2,084|
|**SSE**|0,991|1,923|0,991|1,923|1,122|2,176|1,059|2,054|1,027|1,992|1,090|2,115|
|**S **|1,910|3,706|1,810|3,511|2,198|4,263|1,912|3,709|1,643|3,188|1,232|2,391|
|**SSW**|2,930|5,683|2,815|5,460|2,780|5,394|2,670|5,179|2,196|4,260|1,896|3,678|
|**SW**|2,858|5,544|2,571|4,988|2,559|4,965|2,496|4,842|2,259|4,383|2,149|4,168|
|**WSW**|1,379|2,675|1,738|3,372|1,659|3,218|1,201|2,330|1,785|3,463|1,849|3,586|
|**W **|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|1,327|2,575|
|**WNW**|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|1,011|1,962|
|**NW**|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,664|1,287|
|**NNW**|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|
|**Global**|2,930|5,683|2,815|5,460|2,780|5,394|2,670|5,179|2,259|4,383|2,149|4,168|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|114|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-53: Intensidades máxima globales y por dirección de procedencia de los vientos, entre los meses julio-diciembre. Base**

**de datos histórica.**

|Col1|Intensidad máxima del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Meses**|**Julio**|**Julio**|**Agosto**|**Agosto**|**Septiembre**|**Septiembre**|**Octubre**|**Octubre**|**Noviembre**|**Noviembre**|**Diciembre**|**Diciembre**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N **|0,743|1,441|0,869|1,686|0,600|1,165|0,000|0,000|0,000|0,000|0,000|0,000|
|**NNE**|0,727|1,410|0,790|1,533|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|
|**NE**|0,807|1,566|0,727|1,410|0,000|0,000|0,474|0,920|0,000|0,000|0,000|0,000|
|**ENE**|0,837|1,625|0,790|1,533|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|
|**E **|1,011|1,962|0,806|1,563|0,711|1,379|0,000|0,000|0,442|0,858|0,000|0,000|
|**ESE**|0,995|1,931|0,901|1,747|0,916|1,778|0,442|0,858|0,600|1,165|0,474|0,920|
|**SE**|0,964|1,870|1,122|2,176|0,901|1,747|0,774|1,502|0,822|1,594|0,843|1,635|
|**SSE**|1,074|2,084|0,980|1,900|1,043|2,023|1,090|2,115|0,901|1,747|1,027|1,992|
|**S **|1,185|2,299|0,948|1,839|1,011|1,962|1,106|2,146|1,343|2,605|1,533|2,973|
|**SSW**|1,912|3,709|2,022|3,923|2,243|4,352|2,307|4,475|2,701|5,241|2,512|4,873|
|**SW**|2,322|4,505|2,117|4,107|2,307|4,475|2,480|4,812|2,607|5,057|2,591|5,027|
|**WSW**|1,770|3,433|2,133|4,138|2,085|4,046|2,165|4,199|2,038|3,954|1,580|3,065|
|**W **|1,454|2,820|1,596|3,096|1,517|2,943|1,596|3,096|1,533|2,973|0,000|0,000|
|**WNW**|0,901|1,747|0,964|1,870|0,727|1,410|0,648|1,257|0,000|0,000|0,000|0,000|
|**NW**|0,758|1,471|0,964|1,870|0,664|1,287|0,632|1,226|0,000|0,000|0,000|0,000|
|**NNW**|0,743|1,441|0,853|1,655|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|
|**Global**|2,322|4,505|2,133|4,138|2,307|4,475|2,480|4,812|2,701|5,241|2,591|5,027|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|115|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-54: Intensidades promedio globales y por dirección de procedencia de los vientos, entre los meses enero-junio. Base de**

**datos histórica.**

|Col1|Intensidad promedio del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Meses**|**Enero**|**Enero**|**Febrero**|**Febrero**|**Marzo**|**Marzo**|**Abril**|**Abril**|**Mayo**|**Mayo**|**Junio**|**Junio**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N **|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,458|0,889|
|**NNE**|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,521|1,012|
|**NE**|0,000|0,000|0,474|0,920|0,000|0,000|0,000|0,000|0,593|1,149|0,607|1,178|
|**ENE**|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,695|1,349|0,638|1,238|
|**E **|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,648|1,257|0,635|1,232|
|**ESE**|0,560|1,087|0,000|0,000|0,000|0,000|0,674|1,308|0,612|1,188|0,702|1,362|
|**SE**|0,562|1,091|0,660|1,280|0,666|1,291|0,610|1,184|0,670|1,300|0,683|1,324|
|**SSE**|0,676|1,312|0,718|1,393|0,653|1,267|0,682|1,324|0,700|1,359|0,724|1,404|
|**S **|0,800|1,553|0,843|1,635|0,828|1,605|0,889|1,724|0,764|1,482|0,767|1,488|
|**SSW**|1,722|3,340|1,922|3,728|1,864|3,616|1,778|3,448|1,263|2,450|1,036|2,009|
|**SW**|1,964|3,811|1,984|3,849|1,897|3,680|1,851|3,590|1,657|3,214|1,464|2,840|
|**WSW**|0,986|1,913|1,264|2,452|1,174|2,277|0,948|1,839|1,339|2,598|1,311|2,544|
|**W **|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,932|1,808|
|**WNW**|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,779|1,512|
|**NW**|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,593|1,149|
|**NNW**|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|
|**Global**|1,457|2,827|1,544|2,995|1,411|2,738|1,296|2,513|1,101|2,135|1,019|1,977|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|116|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-55: Intensidades promedio globales y por dirección de procedencia de los vientos, entre los meses julio-diciembre.**

**Base de datos histórica.**

|Col1|Intensidad promedio del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Meses**|**Julio**|**Julio**|**Agosto**|**Agosto**|**Septiembre**|**Septiembre**|**Octubre**|**Octubre**|**Noviembre**|**Noviembre**|**Diciembre**|**Diciembre**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N **|0,587|1,138|0,747|1,449|0,600|1,165|0,000|0,000|0,000|0,000|0,000|0,000|
|**NNE**|0,594|1,153|0,648|1,257|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|
|**NE**|0,597|1,158|0,623|1,208|0,000|0,000|0,474|0,920|0,000|0,000|0,000|0,000|
|**ENE**|0,650|1,261|0,735|1,425|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|
|**E **|0,677|1,314|0,652|1,264|0,648|1,257|0,000|0,000|0,442|0,858|0,000|0,000|
|**ESE**|0,698|1,355|0,689|1,336|0,713|1,384|0,395|0,766|0,528|1,024|0,474|0,920|
|**SE**|0,685|1,330|0,743|1,442|0,753|1,461|0,640|1,241|0,666|1,292|0,610|1,183|
|**SSE**|0,742|1,440|0,711|1,379|0,772|1,498|0,721|1,398|0,640|1,241|0,680|1,319|
|**S **|0,743|1,442|0,711|1,379|0,758|1,470|0,704|1,366|0,680|1,319|0,780|1,512|
|**SSW**|1,001|1,941|0,968|1,879|1,044|2,025|1,108|2,150|1,217|2,360|1,478|2,867|
|**SW**|1,380|2,677|1,361|2,640|1,459|2,830|1,617|3,137|1,848|3,586|1,960|3,803|
|**WSW**|1,297|2,517|1,438|2,790|1,351|2,620|1,363|2,644|1,488|2,886|1,388|2,693|
|**W **|1,055|2,047|1,090|2,114|0,988|1,917|1,038|2,014|1,390|2,697|0,000|0,000|
|**WNW**|0,551|1,069|0,784|1,521|0,727|1,410|0,542|1,052|0,000|0,000|0,000|0,000|
|**NW**|0,656|1,272|0,793|1,539|0,664|1,287|0,545|1,057|0,000|0,000|0,000|0,000|
|**NNW**|0,632|1,226|0,685|1,329|0,000|0,000|0,000|0,000|0,000|0,000|0,000|0,000|
|**Global**|1,026|1,990|1,085|2,105|1,200|2,327|1,256|2,436|1,303|2,527|1,398|2,712|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|117|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**4.3.4 Caracterización Estadística -Estacional**

Para profundizar en mayor forma acerca del ciclo anual correspondiente al año medio
construido a partir de la data histórica, se clasificó su información en las estaciones.

La intensidad del viento de estos datos fue analizada mediante tablas de incidencia (entre la
Tabla 4-56 y la Tabla 4-59) e histogramas (Gráfico 4-45), en las cuales se clasificaron según
categorías de la escala de Beaufort. En las distintas estaciones se encuentran las categorías
Aire Ligero (0,28 - 1,39 m/s) y Brisa Ligera (1,39 - 3,06 m/s), durante el verano ambas
categorías se mantienen cercanas en su frecuencia (50,183 % y 49,725 %, respectivamente).
En las estaciones de otoño e invierno, el Aire Ligero comienza a predominar con frecuencias
superiores al 60 %. Finalmente, durante la primavera la ocurrencia de ambas categorías
empieza a igualarse, terminando con una frecuencia de 56,364 % el Aire Ligero y 43,590 % la
Brisa Ligera.

Para analizar la direccionalidad de estos datos se emplearon tablas de incidencia (entre la
Tabla 4-56 y la Tabla 4-59), histogramas (Gráfico 4-46) y rosas de viento (Gráfico 4-47).
Durante el verano, el viento predomina desde el tercer cuadrante, centrado en la dirección
SSW (37,592 %), mientras que, en las estaciones de otoño e invierno se agregan vientos del
segundo cuadrante, manteniendo el predominio en las direcciones SSW y SW. En la primavera
los vientos aumentan su concentración sobre el tercer cuadrante, destacando la dirección SW
(36,035 %).

Con la selección de los máximos valores entre los datos correspondientes del año medio por
estación y dirección (Tabla 4-60), se determina el máximo valor con 2,930 m/s (5,683 nudos)
durante la estación de verano, desde la dirección SSW. Por otro lado, con la obtención del
valor medio por estación y dirección (Tabla 4-61), se encuentra que el mayor valor medio fue
1,938 m/s (3,760 nudos), correspondiente a la estación de verano, desde la dirección SW. En
general las mayores intensidades medias provienen desde el tercer cuadrante, mientras que,
desde el primer y cuarto cuadrante, son despreciables, en especial en las estaciones de verano
y primavera.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|118|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-56: Tabla de incidencia del viento, verano promedio. Base de datos histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N**|-|-|-|-|-|-|-|0,000|
|**NNE**|-|-|-|-|-|-|-|0,000|
|**NE**|-|0,046|-|-|-|-|-|0,046|
|**ENE**|-|-|-|-|-|-|-|0,000|
|**E**|-|-|-|-|-|-|-|0,000|
|**ESE**|-|0,183|-|-|-|-|-|0,183|
|**SE**|-|2,015|-|-|-|-|-|2,015|
|**SSE**|-|8,104|-|-|-|-|-|8,104|
|**S**|-|24,496|1,007|-|-|-|-|25,504|
|**SSW**|-|11,310|26,282|-|-|-|-|37,592|
|**SW**|-|3,571|22,253|-|-|-|-|25,824|
|**WSW**|-|0,458|0,183|-|-|-|-|0,641|
|**W**|-|-|-|-|-|-|-|0,000|
|**WNW**|-|-|-|-|-|-|-|0,000|
|**NW**|-|-|-|-|-|-|-|0,000|
|**NNW**|-|-|-|-|-|-|-|0,000|
|**Calmas**|0,092|-|-|-|-|-|-|0,092|
|**Sub Total**<br>**(%)** <br>|0,092<br>|50,183<br>|49,725<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|2.184|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|119|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-57: Tabla de incidencia del viento, otoño promedio. Base de datos histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N**|-|0,091|-|-|-|-|-|0,091|
|**NNE**|-|0,091|-|-|-|-|-|0,091|
|**NE**|-|0,272|-|-|-|-|-|0,272|
|**ENE**|-|0,543|-|-|-|-|-|0,543|
|**E**|-|0,906|-|-|-|-|-|0,906|
|**ESE**|-|3,034|-|-|-|-|-|3,034|
|**SE**|-|7,382|-|-|-|-|-|7,382|
|**SSE**|-|15,263|-|-|-|-|-|15,263|
|**S**|-|18,524|1,223|-|-|-|-|19,746|
|**SSW**|-|10,779|13,859|-|-|-|-|24,638|
|**SW**|-|4,121|18,976|-|-|-|-|23,098|
|**WSW**|-|2,400|1,857|-|-|-|-|4,257|
|**W**|-|0,272|-|-|-|-|-|0,272|
|**WNW**|-|0,136|-|-|-|-|-|0,136|
|**NW**|-|0,091|-|-|-|-|-|0,091|
|**NNW**|-|-|-|-|-|-|-|0,000|
|**Calmas**|0,181|-|-|-|-|-|-|0,181|
|**Sub Total**<br>**(%)** <br>|0,181<br>|63,904<br>|35,915<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|2.208|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|120|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-58: Tabla de incidencia del viento, invierno promedio. Base de datos histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N**|-|0,725|-|-|-|-|-|0,725|
|**NNE**|-|0,815|-|-|-|-|-|0,815|
|**NE**|-|0,770|-|-|-|-|-|0,770|
|**ENE**|-|0,543|-|-|-|-|-|0,543|
|**E**|-|1,359|-|-|-|-|-|1,359|
|**ESE**|-|3,487|-|-|-|-|-|3,487|
|**SE**|-|7,473|-|-|-|-|-|7,473|
|**SSE**|-|9,013|-|-|-|-|-|9,013|
|**S**|-|8,786|-|-|-|-|-|8,786|
|**SSW**|-|12,545|2,627|-|-|-|-|15,172|
|**SW**|-|12,228|17,799|-|-|-|-|30,027|
|**WSW**|-|6,748|9,466|-|-|-|-|16,214|
|**W**|-|2,446|0,408|-|-|-|-|2,853|
|**WNW**|-|1,087|-|-|-|-|-|1,087|
|**NW**|-|0,725|-|-|-|-|-|0,725|
|**NNW**|-|0,906|-|-|-|-|-|0,906|
|**Calmas**|0,045|-|-|-|-|-|-|0,045|
|**Sub Total**<br>**(%)** <br>|0,045<br>|69,656<br>|30,299<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|2.208|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|121|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-59: Tabla de incidencia del viento, primavera promedio. Base de datos**

**histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N**|-|0,046|-|-|-|-|-|0,046|
|**NNE**|-|-|-|-|-|-|-|0,000|
|**NE**|-|0,046|-|-|-|-|-|0,046|
|**ENE**|-|-|-|-|-|-|-|0,000|
|**E**|-|0,092|-|-|-|-|-|0,092|
|**ESE**|-|0,458|-|-|-|-|-|0,458|
|**SE**|-|1,603|-|-|-|-|-|1,603|
|**SSE**|-|7,830|-|-|-|-|-|7,830|
|**S**|-|14,469|-|-|-|-|-|14,469|
|**SSW**|-|17,857|9,753|-|-|-|-|27,610|
|**SW**|-|8,791|27,244|-|-|-|-|36,035|
|**WSW**|-|4,258|6,456|-|-|-|-|10,714|
|**W**|-|0,595|0,137|-|-|-|-|0,733|
|**WNW**|-|0,183|-|-|-|-|-|0,183|
|**NW**|-|0,137|-|-|-|-|-|0,137|
|**NNW**|-|-|-|-|-|-|-|0,000|
|**Calmas**|0,046|-|-|-|-|-|-|0,046|
|**Sub Total**<br>**(%)** <br>|0,046<br>|56,364<br>|43,590<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|2.184|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|122|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**VERANO**

**OTOÑO**

**INVIERNO** **PRIMAVERA**

Fuente: Ecotecnos, 2021.
**Gráfico 4-45: Histogramas de intensidad del viento promedio por estación del año. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|123|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**VERANO**

**INVIERNO**

**OTOÑO**

**PRIMAVERA**

Fuente: Ecotecnos, 2021.
**Gráfico 4-46: Histogramas de dirección del viento promedio por estación del año. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|124|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

|Verano|Otoño|
|---|---|
|**Invierno**|**Primavera**|

Fuente: Ecotecnos, 2021.
**Gráfico 4-47: Rosa de los vientos entre estaciones. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|125|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-60: Intensidades máxima globales y por dirección de procedencia de los**

**vientos,** **por estaciones. Base de datos histórica.**

|Col1|Intensidad máxima del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Estaciones**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N**|0,000|0,000|0,553|1,073|0,869|1,686|0,600|1,165|
|**NNE**|0,000|0,000|0,664|1,287|0,790|1,533|0,000|0,000|
|**NE**|0,474|0,920|0,853|1,655|0,807|1,566|0,474|0,920|
|**ENE**|0,000|0,000|1,043|2,023|0,837|1,625|0,000|0,000|
|**E**|0,000|0,000|0,980|1,900|1,011|1,962|0,711|1,379|
|**ESE**|0,761|1,477|1,059|2,054|0,995|1,931|0,774|1,502|
|**SE**|0,934|1,811|1,074|2,084|1,122|2,176|0,843|1,635|
|**SSE**|1,122|2,176|1,090|2,115|1,074|2,084|1,090|2,115|
|**S**|2,198|4,263|1,912|3,709|1,232|2,391|1,343|2,605|
|**SSW**|2,930|5,683|2,780|5,394|2,243|4,352|2,701|5,241|
|**SW**|2,858|5,544|2,559|4,965|2,322|4,505|2,607|5,057|
|**WSW**|1,738|3,372|1,849|3,586|2,133|4,138|2,165|4,199|
|**W**|0,000|0,000|1,327|2,575|1,596|3,096|1,596|3,096|
|**WNW**|0,000|0,000|1,011|1,962|0,964|1,870|0,727|1,410|
|**NW**|0,000|0,000|0,664|1,287|0,964|1,870|0,664|1,287|
|**NNW**|0,000|0,000|0,000|0,000|0,853|1,655|0,000|0,000|
|**Global**|2,930|5,683|2,780|5,394|2,322|4,505|2,701|5,241|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|126|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-61: Intensidades promedio globales y por dirección de procedencia de los**

**vientos,** **por estaciones. Base de datos histórica.**

|Col1|Intensidad promedio del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Estaciones**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N**|0,000|0,000|0,545|1,057|0,638|1,238|0,600|1,165|
|**NNE**|0,000|0,000|0,600|1,165|0,588|1,141|0,000|0,000|
|**NE**|0,474|0,920|0,640|1,241|0,593|1,151|0,474|0,920|
|**ENE**|0,000|0,000|0,666|1,292|0,664|1,287|0,000|0,000|
|**E**|0,000|0,000|0,662|1,284|0,645|1,252|0,577|1,119|
|**ESE**|0,539|1,045|0,657|1,275|0,693|1,345|0,547|1,061|
|**SE**|0,596|1,156|0,673|1,306|0,709|1,376|0,639|1,240|
|**SSE**|0,684|1,327|0,693|1,345|0,739|1,433|0,674|1,307|
|**S**|0,821|1,593|0,833|1,616|0,755|1,465|0,711|1,378|
|**SSW**|1,812|3,515|1,536|2,979|1,013|1,964|1,222|2,371|
|**SW**|1,938|3,760|1,688|3,275|1,417|2,749|1,745|3,385|
|**WSW**|1,158|2,247|1,316|2,553|1,364|2,647|1,401|2,719|
|**W**|0,000|0,000|1,009|1,957|1,063|2,062|1,024|1,987|
|**WNW**|0,000|0,000|0,779|1,512|0,706|1,370|0,589|1,142|
|**NW**|0,000|0,000|0,593|1,149|0,742|1,439|0,585|1,134|
|**NNW**|0,000|0,000|0,000|0,000|0,666|1,293|0,000|0,000|
|**Global**|1,467|2,847|1,181|2,292|1,086|2,107|1,295|2,513|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|127|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**4.3.5 Caracterización Estadística -Diaria**

Los vientos correspondientes a los registros de la base histórica se categorizaron en 6
intervalos horarios, (0 - 4 hrs), (4 - 8 hrs), (8 - 12 hrs), (12 - 16 hrs), (16 - 20 hrs) y (20 - 0 hrs)

con la finalidad de realizar un análisis de la variación diaria del viento.

La intensidad del viento, para cada intervalo horario seleccionado, es presentada con tablas
de incidencia (entre la Tabla 4-62 y Tabla 4-67) y con el apoyo de histogramas (Gráfico 4-48).
Con el fin de ahondar en el análisis de las intensidades se incluye el esquema del ciclo diario
de las intensidades en el Gráfico 4-51. En el periodo inicial (0 - 4 hrs) la categoría principal
corresponde al Aire Ligero (0,28 - 1,39 m/s) con el 62,062 % de los datos, mientras que, la
Brisa Ligera (1,39 - 3,06 m/s) representa al 34,022 % y las Calmas (0,00 - 0,28 m/s) en el
3,896 % de los datos. Según lo ilustrado en el ciclo medio, el intervalo anterior destaca por la
reducción de las intensidades del viento, por otro lado, los dos periodos siguientes (4 - 8 hrs)
y (8 - 12 hrs), revelan las intensidades más bajas del día, siendo la mínima magnitud
0,666 m/s. En los intervalos anteriormente mencionados, resalta la categoría Aire Ligero (77 %
aproximadamente, en cada uno), donde también, la categoría Calmas aumenta cerca al 14 %
en ambos intervalos y la Brisa Ligera disminuye al 7%, aproximadamente, en ambos intervalos.
El periodo (12 - 16 hrs), dentro del ciclo diario, corresponde al momento del día cuando se
incrementan las intensidades y, acorde a esto, se reducen los vientos asociados a las Calmas
(5,866 %) y Aire Ligero (61,122 %), aumentando la frecuencia de la Brisa Ligera (32,683 %),
aunque solo alcanza al segundo lugar en frecuencias. En las próximas horas, (16 - 20 hrs), se
genera el peak diario, identificado con el valor 2,103 m/s. En relación a esto, la frecuencia de
las Calmas se vuelve despreciable, la categoría Brisa Ligera se convierte en la principal
(77,969 %) y la Brisa Suave aparece con una ocurrencia notable (4,406 %). Finalmente, en las
últimas horas, (20 - 0 hrs), las intensidades comienzan a reducirse, aunque se mantuvo una
distribución similar entre las categorías, al intervalo anterior.

Las direcciones se informan mediante tablas de incidencia (entre la Tabla 4-62 y Tabla 4-67),
histogramas (Gráfico 4-49) y rosas de vientos (Gráfico 4-50), además del apoyo del ciclo diario
de las direcciones señalada en el Gráfico 4-52. En el inicio del día, (0 - 4 hrs), el viento
predomina en las direcciones S (30,401 %) y SSW (29,442 %). En las horas siguientes,
(4 - 8 hrs) y (8 - 12 hrs), según lo señalado en el ciclo diario, se presenta una dispersión en
las direcciones hacia el segundo cuadrante con bajas frecuencias, sin embargo, sigue
predominando la dirección S con una ocurrencia cercana al 20 %, en ambos intervalos. En el
periodo (12 - 16 hrs) se vuelven a acentuar los vientos desde el tercer cuadrante, con un
mayor predominio en la dirección SSW, además, en estas horas se presenta una elevada
dispersión en los vientos dentro del mismo cuadrante, como se indica en el ciclo diario. Luego,
en el intervalo (16 - 20 hrs), se comienzan a agrupar los vientos en las direcciones SSW
(28,710 %), SW (28,777 %) y WSW (21,977 %) y, en las horas finales del día, (20 - 0 hrs), el
viento se concentra en las direcciones SSW (44,541 %) y SW (26,673 %).

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|128|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Según la selección de las magnitudes máximas por intervalos horarios y por direcciones (Tabla
4-68), se identifica el mayor valor con 5,529 m/s (10,726 nudos) durante el periodo (12 - 16
hrs) desde la dirección E. Con el cálculo del promedio por intervalo horario y por direcciones
(Tabla 4-69) se estima que el mayor valor medio corresponde a 2,378 m/s (4,614 nudos)
durante el intervalo (16 - 20 hrs) y desde la dirección SSW. En general, las menores
intensidades se asocian al primer y cuarto cuadrante y, en contraste, las mayores magnitudes
se generan en el tercer cuadrante.

**Tabla 4-62: Tabla de incidencia del viento; Intervalo [0 - 4[ hrs. Base de datos**

**histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N**|-|2,340|0,402|-|-|-|-|2,742|
|**NNE**|-|1,180|0,027|-|-|-|-|1,207|
|**NE**|-|0,738|0,007|-|-|-|-|0,744|
|**ENE**|-|0,717|0,040|-|-|-|-|0,758|
|**E**|-|0,798|0,013|-|-|-|-|0,811|
|**ESE**|-|0,972|0,054|-|-|-|-|1,026|
|**SE**|-|1,207|0,094|-|-|-|-|1,301|
|**SSE**|-|3,192|0,691|-|-|-|-|3,882|
|**S**|-|16,374|14,007|0,020|-|-|-|30,401|
|**SSW**|-|15,791|13,652|-|-|-|-|29,442|
|**SW**|-|7,825|4,687|-|-|-|-|12,512|
|**WSW**|-|3,534|0,127|-|-|-|-|3,661|
|**W**|-|2,508|0,007|-|-|-|-|2,514|
|**WNW**|-|1,100|0,013|-|-|-|-|1,113|
|**NW**|-|0,939|0,007|-|-|-|-|0,945|
|**NNW**|-|1,770|0,194|-|-|-|-|1,965|
|**VRB**|-|1,080|-|-|-|-|-|1,080|
|**Calmas**|3,896|-|-|-|-|-|-|3,896|
|**Sub Total**<br>**(%)** <br>|3,896<br>|62,062<br>|34,022<br>|0,020<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|14.914|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|129|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-63: Tabla de incidencia del viento; Intervalo [4 - 8[ hrs. Base de datos**

**histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N**|-|3,454|0,483|-|-|-|-|3,937|
|**NNE**|-|2,408|0,107|-|-|-|-|2,515|
|**NE**|-|1,952|0,020|-|-|-|-|1,972|
|**ENE**|-|2,314|0,020|-|-|-|-|2,334|
|**E**|-|4,728|0,148|-|-|-|-|4,876|
|**ESE**|-|4,675|0,349|-|-|-|-|5,023|
|**SE**|-|4,708|0,161|-|-|-|-|4,869|
|**SSE**|-|6,881|0,315|-|-|-|-|7,197|
|**S**|-|17,860|3,253|-|-|-|-|21,113|
|**SSW**|-|11,938|2,233|-|-|-|-|14,172|
|**SW**|-|4,977|0,423|-|-|-|-|5,399|
|**WSW**|-|2,676|0,020|-|-|-|-|2,696|
|**W**|-|2,468|-|-|-|-|-|2,468|
|**WNW**|-|1,133|-|-|-|-|-|1,133|
|**NW**|-|1,335|0,027|-|-|-|-|1,362|
|**NNW**|-|1,992|0,094|-|-|-|-|2,086|
|**VRB**|-|2,475|-|-|-|-|-|2,475|
|**Calmas**|14,373|-|-|-|-|-|-|14,373|
|**Sub Total**<br>**(%)** <br>|14,373<br>|77,975<br>|7,653<br>|0,000<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|14.910|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|130|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-64: Tabla de incidencia del viento; Intervalo [8 - 12[ hrs. Base de datos**

**histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N**|-|1,958|0,141|-|-|-|-|2,099|
|**NNE**|-|1,737|0,060|-|-|-|-|1,797|
|**NE**|-|1,764|0,027|-|-|-|-|1,791|
|**ENE**|-|2,461|0,047|-|-|-|-|2,508|
|**E**|-|6,411|0,483|0,007|-|-|-|6,901|
|**ESE**|-|7,558|0,905|-|-|-|-|8,464|
|**SE**|-|7,223|0,637|-|-|-|-|7,860|
|**SSE**|-|9,000|0,577|-|-|-|-|9,577|
|**S**|-|16,753|2,944|-|-|-|-|19,697|
|**SSW**|-|9,872|1,717|-|-|-|-|11,589|
|**SW**|-|4,386|0,423|-|-|-|-|4,809|
|**WSW**|-|2,273|0,020|-|-|-|-|2,294|
|**W**|-|1,489|-|-|-|-|-|1,489|
|**WNW**|-|0,758|0,007|-|-|-|-|0,765|
|**NW**|-|0,624|0,013|-|-|-|-|0,637|
|**NNW**|-|0,885|0,020|-|-|-|-|0,905|
|**VRB**|-|2,669|-|-|-|-|-|2,669|
|**Calmas**|14,151|-|-|-|-|-|-|14,151|
|**Sub Total**<br>**(%)** <br>|14,151<br>|77,822<br>|8,021<br>|0,007<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|14.911|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|131|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-65: Tabla de incidencia del viento; Intervalo [12 - 16[ hrs. Base de datos**

**histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N**|-|2,212|0,127|-|-|-|-|2,340|
|**NNE**|-|1,609|0,060|-|-|-|-|1,669|
|**NE**|-|0,885|0,020|-|-|-|-|0,905|
|**ENE**|-|1,153|-|-|-|-|-|1,153|
|**E**|-|1,689|0,141|-|0,013|-|-|1,844|
|**ESE**|-|2,119|0,215|-|-|-|-|2,333|
|**SE**|-|2,119|0,188|-|-|-|-|2,306|
|**SSE**|-|3,560|0,275|-|-|-|-|3,835|
|**S**|-|8,233|2,963|0,034|-|-|-|11,230|
|**SSW**|-|7,763|11,987|0,215|-|-|-|19,965|
|**SW**|-|6,403|9,527|0,060|-|-|-|15,990|
|**WSW**|-|6,684|5,625|0,007|-|-|-|12,316|
|**W**|-|6,423|1,153|-|-|-|-|7,576|
|**WNW**|-|3,533|0,188|-|-|-|-|3,721|
|**NW**|-|2,501|0,054|-|-|-|-|2,554|
|**NNW**|-|2,326|0,161|-|-|-|-|2,487|
|**VRB**|-|1,911|-|-|-|-|-|1,911|
|**Calmas**|5,866|-|-|-|-|-|-|5,866|
|**Sub Total**<br>**(%)** <br>|5,866<br>|61,122<br>|32,683<br>|0,315<br>|0,013<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|14.916|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|132|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-66: Tabla de incidencia del viento; Intervalo [16 - 20[ hrs. Base de datos**

**histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N**|-|0,402|0,188|-|-|-|-|0,590|
|**NNE**|-|0,054|0,020|-|-|-|-|0,074|
|**NE**|-|0,007|-|-|-|-|-|0,007|
|**ENE**|-|0,007|-|-|-|-|-|0,007|
|**E**|-|-|-|-|-|-|-|0,000|
|**ESE**|-|0,007|-|-|-|-|-|0,007|
|**SE**|-|-|-|-|-|-|-|0,000|
|**SSE**|-|0,013|0,013|-|-|-|-|0,027|
|**S**|-|0,127|3,072|0,168|-|-|-|3,367|
|**SSW**|-|0,778|25,022|2,911|-|-|-|28,710|
|**SW**|-|1,885|25,659|1,234|-|-|-|28,777|
|**WSW**|-|4,185|17,698|0,094|-|-|-|21,977|
|**W**|-|5,124|4,654|-|-|-|-|9,778|
|**WNW**|-|2,327|0,892|-|-|-|-|3,219|
|**NW**|-|1,469|0,194|-|-|-|-|1,663|
|**NNW**|-|1,100|0,550|-|-|-|-|1,650|
|**VRB**|-|0,080|0,007|-|-|-|-|0,087|
|**Calmas**|0,060|-|-|-|-|-|-|0,060|
|**Sub Total**<br>**(%)** <br>|0,060<br>|17,564<br>|77,969<br>|4,406<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|14.911|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|133|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-67: Tabla de incidencia del viento; Intervalo [20 - 0[ hrs. Base de datos**

**histórica.**

|Intensidad<br>(m/s)|[0,00-|[0,28-|[1,39-|[3,06-|[5,28-|[7,78-|[10,56-|Sub<br>Total (%)|
|---|---|---|---|---|---|---|---|---|
|**Intensidad**<br>**(m/s)**|**0,28[**|**1,39[**|**3,06[**|**5,28[**|**7,78[**|**10,56[**|**13,61[**|**13,61[**|
|**Escala de**<br>**Beaufort**|**Calmas**|**Aire**<br>**Ligero**|**Brisa**<br>**Ligera**|**Brisa**<br>**Suave**|**Brisa**<br>**Moderada**|**Brisa**<br>**Fresca**|**Brisa**<br>**Fuerte**|**Brisa**<br>**Fuerte**|
|**N**|-|0,657|0,101|-|-|-|-|0,758|
|**NNE**|-|0,107|0,007|-|-|-|-|0,114|
|**NE**|-|0,013|-|-|-|-|-|0,013|
|**ENE**|-|0,013|-|-|-|-|-|0,013|
|**E**|-|0,007|-|-|-|-|-|0,007|
|**ESE**|-|-|-|-|-|-|-|0,000|
|**SE**|-|0,007|0,007|-|-|-|-|0,013|
|**SSE**|-|0,054|0,121|-|-|-|-|0,174|
|**S**|-|1,201|9,195|0,429|-|-|-|10,825|
|**SSW**|-|3,977|37,954|2,609|-|-|-|44,541|
|**SW**|-|4,058|21,616|0,999|-|-|-|26,673|
|**WSW**|-|3,763|7,049|0,020|-|-|-|10,832|
|**W**|-|2,502|0,684|-|-|-|-|3,186|
|**WNW**|-|0,993|0,040|-|-|-|-|1,033|
|**NW**|-|0,711|0,034|-|-|-|-|0,744|
|**NNW**|-|0,644|0,154|-|-|-|-|0,798|
|**VRB**|-|0,107|0,013|-|-|-|-|0,121|
|**Calmas**|0,154|-|-|-|-|-|-|0,154|
|**Sub Total**<br>**(%)** <br>|0,154<br>|18,813<br>|76,975<br>|4,058<br>|0,000<br>|0,000<br>|0,000|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**Total**|100,000|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**N°**<br>**Datos**|14.910|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|134|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Intervalo [0- 4[ hrs.**

**Intervalo [8- 12[ hrs.**

**Intervalo [16- 20[ hrs.**

**Intervalo [4- 8[ hrs.**

**Intervalo [12- 16[ hrs.**

**Intervalo [20- 0[ hrs.**

Fuente: Ecotecnos, 2021.
**Gráfico 4-48: Histograma de frecuencia relativa de la intensidad del viento por intervalos horarios. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|135|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Intervalo [0- 4[ hrs.**

**Intervalo [8- 12[ hrs.**

**Intervalo [16- 20[ hrs.**

**Intervalo [4- 8[ hrs.**

**Intervalo [12- 16[ hrs.**

**Intervalo [20- 0[ hrs.**

Fuente: Ecotecnos, 2021.
**Gráfico 4-49: Histograma de frecuencia relativa de la dirección del viento por intervalos horarios. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|136|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

|Intervalo [0- 4[ hrs.|Intervalo [4- 8[ hrs.|
|---|---|
|**Intervalo [8- 12[ hrs.**|**Intervalo [12- 16[ hrs.**|
|**Intervalo [16- 20[ hrs.** <br>|**Intervalo [20- 0[ hrs.** <br>|

Fuente: Ecotecnos, 2021.
**Gráfico 4-50: Rosa de los vientos por intervalos. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|137|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Gráfico 4-51: Histograma de intensidad del viento promedio en un ciclo diario. Base de datos histórica.**

Fuente: Ecotecnos, 2021.
**Gráfico 4-52: Ocurrencia de la incidencia del viento por dirección en un ciclo diario. Base de datos histórica.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|138|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-68: Intensidades máxima globales y por dirección de procedencia de los vientos, por intervalos horarios. Base de datos**

**histórica.**

|Col1|Intensidad máxima del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Intervalos (hrs)**|**[0 - 4[**|**[0 - 4[**|**[4 - 8[**|**[4 - 8[**|**[8 - 12[**|**[8 - 12[**|**[12 - 16[**|**[12 - 16[**|**[16 - 20[**|**[16 - 20[**|**[20 - 0[**|**[20 - 0[**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N**|2,054|3,985|2,843|5,515|1,580|3,065|2,843|5,515|2,054|3,985|1,738|3,372|
|**NNE**|1,738|3,372|2,054|3,985|1,896|3,678|1,580|3,065|2,370|4,598|1,422|2,759|
|**NE**|1,422|2,759|1,896|3,678|1,422|2,759|1,422|2,759|0,948|1,839|0,632|1,226|
|**ENE**|1,896|3,678|1,422|2,759|1,580|3,065|1,264|2,452|0,790|1,533|0,632|1,226|
|**E**|1,422|2,759|2,370|4,598|4,739|9,194|5,529|10,726|0,000|0,000|0,474|0,920|
|**ESE**|2,054|3,985|2,054|3,985|2,212|4,291|2,370|4,598|0,790|1,533|0,000|0,000|
|**SE**|1,896|3,678|3,001|5,822|2,212|4,291|2,054|3,985|0,000|0,000|1,580|3,065|
|**SSE**|2,528|4,904|2,054|3,985|2,370|4,598|2,054|3,985|2,054|3,985|3,001|5,822|
|**S**|3,317|6,435|2,843|5,515|3,001|5,822|3,475|6,742|4,423|8,581|4,107|7,968|
|**SSW**|2,843|5,515|2,686|5,211|2,843|5,515|3,791|7,355|4,423|8,581|4,265|8,274|
|**SW**|3,001|5,822|2,528|4,904|3,001|5,822|3,633|7,048|4,107|7,968|4,107|7,968|
|**WSW**|1,738|3,372|1,422|2,759|1,580|3,065|3,159|6,128|3,475|6,742|3,475|6,742|
|**W**|1,580|3,065|1,106|2,146|0,948|1,839|1,896|3,678|2,528|4,904|2,212|4,291|
|**WNW**|1,422|2,759|0,948|1,839|1,738|3,372|2,212|4,291|1,896|3,678|2,843|5,515|
|**NW**|1,422|2,759|1,738|3,372|1,580|3,065|2,528|4,904|2,054|3,985|2,212|4,291|
|**NNW**|2,370|4,598|2,212|4,291|1,738|3,372|1,896|3,678|2,528|4,904|2,686|5,211|
|**Global**|3,317|6,435|3,001|5,822|4,739|9,194|5,529|10,726|4,423|8,581|4,265|8,274|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|139|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-69: Intensidades promedio globales y por dirección de procedencia de los vientos, por intervalos horarios. Base de**

**datos histórica.**

|Col1|Intensidad promedio del viento|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Intervalos (hrs)**|**[0 - 4[**|**[0 - 4[**|**[4 - 8[**|**[4 - 8[**|**[8 - 12[**|**[8 - 12[**|**[12 - 16[**|**[12 - 16[**|**[16 - 20[**|**[16 - 20[**|**[20 - 0[**|**[20 - 0[**|
|**Direcciones**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|**(m/s)**|**nudos**|
|**N**|0,896|1,739|0,827|1,605|0,719|1,395|0,755|1,465|1,192|2,313|0,979|1,899|
|**NNE**|0,740|1,435|0,712|1,381|0,673|1,306|0,722|1,401|1,106|2,146|0,892|1,731|
|**NE**|0,740|1,436|0,657|1,274|0,656|1,272|0,682|1,324|0,948|1,839|0,553|1,073|
|**ENE**|0,702|1,362|0,625|1,212|0,675|1,309|0,609|1,182|0,790|1,533|0,474|0,920|
|**E**|0,620|1,203|0,667|1,294|0,755|1,464|0,772|1,498|0,000|0,000|0,474|0,920|
|**ESE**|0,724|1,404|0,747|1,449|0,843|1,635|0,825|1,601|0,790|1,533|0,000|0,000|
|**SE**|0,769|1,492|0,721|1,399|0,806|1,563|0,836|1,623|0,000|0,000|1,422|2,759|
|**SSE**|0,976|1,893|0,752|1,458|0,803|1,558|0,826|1,602|1,304|2,529|1,768|3,430|
|**S**|1,324|2,569|0,952|1,847|0,949|1,841|1,107|2,149|2,276|4,415|2,063|4,001|
|**SSW**|1,328|2,576|0,974|1,889|0,954|1,851|1,559|3,024|2,378|4,614|2,159|4,189|
|**SW**|1,214|2,356|0,832|1,614|0,818|1,586|1,496|2,902|2,086|4,047|1,995|3,870|
|**WSW**|0,794|1,540|0,649|1,260|0,624|1,211|1,295|2,513|1,777|3,448|1,622|3,146|
|**W**|0,600|1,165|0,545|1,058|0,525|1,019|0,974|1,889|1,335|2,591|1,067|2,071|
|**WNW**|0,592|1,149|0,532|1,032|0,504|0,979|0,859|1,666|1,189|2,307|0,882|1,712|
|**NW**|0,678|1,315|0,609|1,181|0,552|1,071|0,777|1,508|1,105|2,144|0,833|1,615|
|**NNW**|0,843|1,636|0,724|1,405|0,637|1,235|0,786|1,524|1,236|2,397|1,020|1,978|
|**Global**|1,128|2,189|0,692|1,342|0,702|1,362|1,115|2,163|1,967|3,816|1,963|3,808|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|140|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**4.3.6 Análisis de Clima Extremo de Vientos**

La base de datos histórica fue clasificada en 8 direcciones, sobre cada una de ellas se eligió
el mayor dato por año recopilado, obteniéndose 10 registros por dirección. En la Tabla 4-70 y
Tabla 4-71 se presentan los datos seleccionados, ordenados de mayor a menor junto a la
fecha asociada. En forma complementaria se incluyó el Gráfico 4-53, para ilustrar la
distribución de sus correspondientes intensidades y direcciones.

La repetición de intensidades del viento, en algunas direcciones, se puede explicar por la
similitud en las intensidades entre los años analizados y a la capacidad de medición de la
estación meteorológica, Diego Aracena, la cual registra la velocidad del viento en nudos, en

forma discreta.

En ciertas direcciones se observa que algunos datos de vientos mostraron intensidades en
forma dispersa, en comparación con las magnitudes de los otros años. Los eventos de
mayores intensidades suelen ser sumamente variables en las direcciones, por ello, al emplear
registros horarios, es posible que las direcciones registradas no representen a la verdadera
del evento como se menciona en Palutikof, Brabson, Lister, & Adcock (1999). Por esta razón,

el análisis realizado resulta ser bastante conservador.

El mayor valor del registro corresponde a 5,529 m/s desde la dirección E, aunque esta
intensidad se encuentra dispersa de los mayores de los eventos correspondiente a los otros
años. En general, los mayores eventos de las direcciones SW y S presentaron magnitudes de
viento importantes.

Fuente: Ecotecnos, 2021.
**Gráfico 4-53: Eventos seleccionados por direcciones para análisis del clima extremo.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|141|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-70 Lista de eventos máximos para clima extremo de vientos en las direcciones N, NE, E y SE**

|N|Col2|Col3|NE|Col5|Col6|E|Col8|Col9|SE|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Fecha|Intensidad<br>(m/s)|Dirección<br>(°)|Fecha|Intensidad<br>(m/s)|Dirección<br>(°)|Fecha|Intensidad<br>(m/s)|Dirección<br>(°)|Fecha|Intensidad<br>(m/s)|Dirección<br>(°)|
|09-09-2013<br>7:00|2,843|350,000|22-10-2011<br>3:00|1,896|60,000|08-07-2016<br>13:00|5,529|100,000|05-09-2020<br>5:00|3,001|140,000|
|09-08-2015<br>14:00|2,843|360,000|09-08-2015<br>7:00|1,896|40,000|25-05-2014<br>5:00|2,370|100,000|05-02-2017<br>0:00|2,528|150,000|
|16-07-2014<br>4:00|2,212|340,000|29-06-2016<br>8:00|1,896|30,000|14-07-2015<br>8:00|2,370|100,000|15-07-2016<br>12:00|2,370|120,000|
|31-08-2011<br>0:00|2,054|10,000|31-07-2019<br>5:00|1,738|30,000|23-08-2017<br>12:00|2,212|110,000|18-09-2014<br>11:00|2,212|120,000|
|12-06-2016<br>17:00|2,054|340,000|27-04-2012<br>8:00|1,580|60,000|17-06-2011<br>6:00|2,054|110,000|16-08-2011<br>10:00|2,054|130,000|
|20-06-2019<br>4:00|2,054|10,000|15-07-2018<br>2:00|1,580|60,000|01-09-2013<br>8:00|2,054|110,000|23-08-2012<br>8:00|2,054|130,000|
|14-07-2012<br>4:00|1,896|10,000|05-05-2013<br>10:00|1,422|30,000|02-01-2018<br>10:00|1,896|100,000|09-06-2019<br>7:00|2,054|140,000|
|13-12-2017<br>9:00|1,864|16,000|29-07-2014<br>12:00|1,422|50,000|18-07-2012<br>10:00|1,580|110,000|12-04-2013<br>11:00|1,896|120,000|
|10-07-2020<br>6:00|1,738|10,000|10-05-2017<br>10:00|1,422|60,000|28-07-2020<br>12:00|1,580|110,000|24-01-2015<br>11:00|1,896|130,000|
|22-06-2018<br>10:00|1,580|10,000|19-06-2020<br>3:00|1,422|40,000|28-03-2019<br>5:00|1,422|110,000|29-08-2018<br>10:00|1,580|120,000|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|142|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-71 Lista de eventos máximos para clima extremo de vientos en direcciones S, SW, W y NW**

|S|Col2|Col3|SW|Col5|Col6|W|Col8|Col9|NW|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Fecha|Intensidad<br>(m/s)|Dirección<br>(°)|Fecha|Intensidad<br>(m/s)|Dirección<br>(°)|Fecha|Intensidad<br>(m/s)|Dirección<br>(°)|Fecha|Intensidad<br>(m/s)|Dirección<br>(°)|
|18-01-2014<br>17:00|4,423|190,000|26-01-2011<br>21:00|4,107|210,000|15-01-2012<br>18:00|3,475|250,000|02-01-2018<br>23:00|2,843|300,000|
|02-01-2011<br>19:00|4,265|200,000|16-04-2012<br>18:00|4,107|230,000|20-11-2011<br>18:00|3,317|250,000|13-03-2016<br>15:00|2,528|320,000|
|22-02-2019<br>21:00|4,265|200,000|08-07-2016<br>18:00|3,949|220,000|11-05-2019<br>17:00|3,001|250,000|09-09-2013<br>1:00|2,370|330,000|
|08-07-2016<br>16:00|3,949|200,000|28-01-2013<br>20:00|3,791|210,000|29-09-2020<br>18:00|3,001|250,000|16-12-2015<br>20:00|2,212|320,000|
|10-02-2015<br>18:00|3,791|200,000|07-02-2020<br>18:00|3,791|230,000|15-10-2014<br>16:00|2,528|280,000|09-11-2019<br>15:00|2,212|300,000|
|07-02-2018<br>20:00|3,791|200,000|01-03-2017<br>22:00|3,633|210,000|21-07-2018<br>18:00|2,528|280,000|09-06-2014<br>16:00|2,054|330,000|
|13-09-2017<br>19:00|3,633|200,000|05-02-2018<br>18:00|3,633|210,000|18-02-2013<br>16:00|2,212|250,000|07-08-2011<br>15:00|1,738|330,000|
|02-01-2012<br>18:00|3,475|200,000|29-06-2019<br>17:00|3,633|220,000|29-01-2017<br>20:00|2,054|260,000|15-03-2012<br>15:00|1,738|320,000|
|20-09-2013<br>20:00|3,475|200,000|08-01-2014<br>17:00|3,475|220,000|06-11-2015<br>18:00|1,896|250,000|11-07-2017<br>8:00|1,738|300,000|
|06-04-2020<br>20:00|2,843|200,000|07-01-2015<br>18:00|3,475|210,000|01-01-2016<br>17:00|1,738|250,000|30-08-2020<br>17:00|1,738|300,000|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|143|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

La Tabla 4-72 señala los ajustes empleados para la distribución de cada dirección, donde se
destacan elevados coeficientes de determinación, sobre 0,8, con excepción de la dirección E.
El menor coeficiente (0,737) puede deberse a presencia de un valor de intensidad del viento
disperso, respecto a los valores de los otros años.

**Tabla 4-72: Resumen de los parámetros de ajustes a la distribución.**

|Col1|Índices|Col3|Col4|
|---|---|---|---|
|**Direcciones**|**R2 **|**A **|**B **|
|**N **|0,908|0,341|1,929|
|**NE**|0,835|0,163|1,539|
|**E **|0,737|0,855|1,844|
|**SE**|0,969|0,327|1,987|
|**S **|0,871|0,371|3,590|
|**SW**|0,925|0,189|3,657|
|**W **|0,938|0,494|2,308|
|**NW**|0,941|0,318|1,945|

Fuente: Ecotecnos, 2021.

La proyección estimada por dirección se señala en la Tabla 4-73 y se ilustra en el Gráfico 4-54
para cada periodo de retorno. En la dirección E, por sentidos gráficos, se omitió de la ilustración
el mayor evento, pues la dispersión en sus valores provocó un elevado periodo de retorno.

Según las estimaciones realizadas, desde la dirección S se presenta la mayor intensidad
proyectada en 30 años, con un valor de 4,845 m/s, con un intervalo superior de 5,787 m/s. En
segundo lugar, se encuentra la dirección E con una intensidad de 4,737 m/s, aunque la elevada
variación en sus valores provoca que la intensidad del intervalo superior alcance 7,097 m/s.
Luego, predominan las intensidades de las direcciones SW y W, con intensidades iguales a
4,297 m/s y 3,980 m/s, respectivamente.

Las menores intensidades proyectadas en 30 años se estiman desde las direcciones NE, NW
y N, con magnitudes iguales a 2,091 m/s, 3,021 m/s y 3,084 m/s, respectivamente. En la
dirección se evidencia una curva de proyección algo aplanada, debido a una baja variabilidad
de los máximos eventos seleccionados por año.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|144|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

**Tabla 4-73: Tabla con la intensidad del viento asociada a distintos periodos de retorno, su intervalo superior e inferior de ajuste.**

|Periodo de<br>retorno|5|Col3|Col4|10|Col6|Col7|15|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Direcciones**|**Intervalo**<br>**Superior**|**Ajustes**|**Intervalo**<br>**Inferior**|**Intervalo**<br>**Superior**|**Ajustes**|**Intervalo**<br>**Inferior**|**Intervalo**<br>**Superior**|**Ajustes**|**Intervalo**<br>**Inferior**|
|**N **|3,289|2,441|1,592|3,545|2,697|1,848|3,690|2,841|1,993|
|**NE**|2,206|1,784|1,361|2,328|1,906|1,483|2,397|1,975|1,552|
|**E **|5,486|3,126|0,765|6,128|3,767|1,407|6,490|4,129|1,769|
|**SE**|3,267|2,478|1,690|3,512|2,724|1,935|3,651|2,863|2,074|
|**S **|5,088|4,146|3,204|5,367|4,425|3,483|5,524|4,582|3,640|
|**SW**|4,407|3,941|3,474|4,549|4,083|3,616|4,629|4,163|3,696|
|**W **|4,258|3,049|1,839|4,629|3,420|2,210|4,839|3,629|2,419|
|**NW**|3,198|2,422|1,645|3,437|2,660|1,884|3,571|2,795|2,018|
|**Periodo de**<br>**retorno**|**25**|**25**|**25**|**30**|**30**|**30**|<br> <br>|<br> <br>|<br> <br>|
|**Direcciones**|**Intervalo**<br>**Superior**|**Ajustes**|**Intervalo**<br>**Inferior**|**Intervalo**<br>**Superior**|**Ajustes**|**Intervalo**<br>**Inferior**|<br> <br> <br><br><br>|<br> <br> <br><br><br>|<br> <br> <br><br><br>|
|**N **|3,869|3,020|2,172|3,932|3,084|2,235|<br> <br> <br><br><br>|<br> <br> <br><br><br>|<br> <br> <br><br><br>|
|**NE**|2,483|2,060|1,638|2,513|2,091|1,668|<br> <br> <br><br><br>|<br> <br> <br><br><br>|<br> <br> <br><br><br>|
|**E **|6,939|4,578|2,218|7,097|4,737|2,377|<br> <br> <br><br><br>|<br> <br> <br><br><br>|<br> <br> <br><br><br>|
|**SE**|3,823|3,034|2,246|3,884|3,095|2,307|<br> <br> <br><br><br>|<br> <br> <br><br><br>|<br> <br> <br><br><br>|
|**S **|5,719|4,776|3,834|5,787|4,845|3,903|<br> <br> <br><br><br>|<br> <br> <br><br><br>|<br> <br> <br><br><br>|
|**SW**|4,728|4,262|3,796|4,764|4,297|3,831|<br> <br> <br><br><br>|<br> <br> <br><br><br>|<br> <br> <br><br><br>|
|**W **|5,098|3,889|2,679|5,190|3,980|2,771|<br> <br> <br><br><br>|<br> <br> <br><br><br>|<br> <br> <br><br><br>|
|**NW**|3,738|2,962|2,185|3,797|3,021|2,244|<br> <br>|<br> <br>|<br> <br>|

Fuente: Ecotecnos, 2021.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|145|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Fuente: Ecotecnos, 2021.
**Gráfico 4-54: Curva de proyección de eventos extremos para diversos periodos de retorno.**

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|146|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 5 CONCLUSIÓN

#### 5.1 Respecto a los Datos de Campo

Los registros obtenidos en el sector de ITI identificaron que la intensidad del viento durante el
periodo de medición, respecto a la escala de Beaufort, correspondieron a las categorías
Calmas, Aire Ligero, Brisa Ligera y Brisa Suave. De entre las cuales predominó el Aire Ligero
(63,185 %), seguidos por las Calmas (22,375 %) y la Brisa Ligera (14,412 %). En cuanto a la
direccionalidad, fue notorio el predominio desde el tercer cuadrante centrado en las
direcciones SSW (32,635 %) y SW (17,128 %) y, junto a estas, se acumularon ocurrencias
relevantes en las direcciones NNE (3,482 %).

Mediante los valores estadísticos de las componentes ortogonales, se determinó que la
componente U presentó un valor medio de 0,381 m/s, reflejándose su tendencia hacia el E, y
la componente V, con un promedio de 0,497 m/s, indicó su predominio hacia el N. Mediante la
desviación estándar se evidenció que la componente V expresó una mayor dispersión
(0,792 m/s) en los datos, en comparación, de la componente U (0,498 m/s). Consistente con
lo anterior, se determinó que, respecto a la componente principal, la componente V presentó
una mayor participación (66,834 %) que la componente U (33,166 %).

El análisis espectral de las componentes ortogonales del viento, U y V, demostró una similitud
en el espectro de ambas componentes, con una mayor concentración energética en la
componente V. Del espectro obtenido resaltan los peaks energéticos con ciclos diurnos
(24 horas) y semidiurnos (12 horas).

De acuerdo a la representación del vector progresivo del registro medido, durante un periodo
superior de un año, se demostró la relevancia del viento desde el tercer cuadrante con el
desplazamiento casi recto hacia la dirección NE por 16.000 km aproximadamente, con una
velocidad neta de 0,49 m/s.

La caracterización mensual, obtenida mediante la clasificación por cada mes, reveló que
independiente de los meses analizados, la categoría Aire Ligero concentró la mayor cantidad
de registros. Desde el mes de enero se evidenció una tendencia de crecimiento de esta
categoría hasta septiembre, cuando alcanzó su máximo valor (72,431 %), tras lo cual, su
frecuencia disminuyó. Entre los meses noviembre y abril, las Calmas se encontraron sobre el
20 % de los datos en cada mes, a diferencia de la categoría Brisa Ligera, a la cual se le estimó
una ocurrencia bajo el 20 % en todos los meses. En cuanto a la direccionalidad del viento, en
todos los meses se distinguió la gran acumulación de datos en el tercer cuadrante, centradas
en las direcciones SSW y SW, sin embargo, entre los meses mayo y agosto, las direcciones
se dispersaron, reuniéndose una cantidad importante de vientos desde el primer y cuarto
cuadrante, cercanos a la dirección N.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|147|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Mediante el análisis estacional, se verificó la superioridad de ocurrencia de la categoría Aire
Ligero. Las estaciones verano y otoño mostraron una distribución semejante de sus
categorías, donde el Aire Ligero alcanzó una frecuencia cercana al 60 %. En las estaciones
invierno y primavera se incrementó la concentración de datos en esta categoría. La ocurrencia
de las Calmas fue mayor a la Brisa Ligera en todas las estaciones, con excepción del invierno,
cuando ambas categorías presentaron ocurrencias semejantes, siendo la Brisa Ligera
levemente superior. Las direcciones se agruparon principalmente en el tercer cuadrante,
aunque en las estaciones de otoño e invierno aparecieron tenues concentraciones desde el
primer y cuarto cuadrante.

Con la caracterización diaria se reveló que, durante las primeras horas del día, (0 - 4 hrs), las
intensidades del viento se redujeron progresivamente con el paso de las horas. En este
intervalo predominó la categoría Aire Ligero, seguido por las Calmas y Brisa Ligera. En las
siguientes horas, (4 - 8 hrs) y (8 - 12 hrs) se presentaron las menores intensidades del viento
del día, entre las cuales resaltó la intensidad media 0,408 m/s, como la más baja, durante este
tiempo se incrementó notablemente la frecuencia de las Calmas, alcanzando la categoría del
Aire Ligero. El siguiente periodo, (12 - 16 hrs), el viento mostró un incremento en su magnitud
y, junto a ello, la distribución del viento se volvió a concentrar en la categoría Aire Ligero. En
el intervalo (16 - 20 hrs), se localizó el máximo valor del día, 1,406 m/s, además las categorías
de Aire Ligero y Brisa Ligera se asemejaron en su ocurrencia (58,997 % y 40,652 %). En las
últimas horas del día, (20 - 00 hrs), el Aire Ligero volvió a tomar el predominio (73,373 %). En
cuanto a la direccionalidad, durante el día predominó el viento desde el tercer cuadrante,
aunque en los intervalos (4 - 8 hrs) y (8 - 12 hrs) aparecieron bajas frecuencias de vientos
desde el primer cuadrante y en las horas (12 - 16 hrs) se generaron ligeras variaciones desde

el cuarto cuadrante.

El mayor valor de la serie correspondió a 3,931 m/s desde la dirección N, dato que ocurrió
durante la estación verano, en el mes de febrero y durante el intervalo horario (8 - 12 hrs).
Con la obtención del valor medio de la serie completa por direcciones se obtuvo que el mayor
fue 1,133 m/s desde el SSW. En cambio, con el promedio por mes, el mayor valor se determinó
en el mes de julio desde la dirección N igual a 1,359 m/s y según la media por estaciones, el
máximo valor se encontró en verano, con 1,219 m/s, proveniente del SSW. Con la media por
intervalo horario, se determinó que el mayor valor medio perteneció al periodo (16 - 20 hrs),
con 1,523 m/s desde el SSW. Los valores medios permitieron verificar que, en general, los
mayores valores provienen desde el tercer cuadrante y los menores desde el primer y segundo

cuadrante.

#### 5.2 Respecto de la Correlación de la Base de Datos

Los registros de la estación en el sector de ITI (mediciones de campo) y del aeropuerto Diego
Aracena (base de datos histórica) fueron contrastados en el mismo periodo, donde se
determinó que ambas series de tiempo presentaron comportamientos similares, aunque la

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|148|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

medición en el sector de ITI resultó con una intensidad menor que la histórica, lo cual puede
relacionarse con estructuras portuarias que obstruían el viento. Pese a esto, para la magnitud
del viento se estimó un coeficiente de correlación de 0,98 (R [2] ) y un error cuadrático medio
(RMS) de 0,51 m/s. En la componente ortogonal U, también se reflejaron menores valores en
las mediciones, sobre todo en los valores positivos, de todas formas, se calculó un R [2] de 0,93
y RMS de 0,58 m/s. Por otro lado, en la componente ortogonal V se reflejó una alta similitud
entre ambas series, tanto en las intensidades como en el comportamiento en el tiempo, lo cual
se verificó cuantitativamente con un R [2] de 0,98 y un RMS de 0,24 m/s. Según lo analizado, fue
posible determinar que la componente ortogonal V contiene mayor energía en comparación
de la componente U. En cuanto a la dirección se asemeja el comportamiento de las series de
tiempo, con un predominio desde el tercer cuadrante. Los estadísticos verificaron la similitud
de la dirección con el R [2] de 0,95 y un RMS de 28,13 °. Por último, el análisis de la correlación
cruzada de las componentes ortogonales de ambas series, demostró un coeficiente sobre 0,6
para ambas variables, con bajos desfases temporales, lo cual se presentó sobre los intervalos

de confianza.

Con esta información fue posible demostrar las similitudes en las series de tiempo de las
mediciones del sector de ITI y la base de datos histórica en el aeropuerto Diego Aracena. Pese
al menor valor en la intensidad de las mediciones, bajo la posibilidad que la intensidad en el
sector de ITI se encontrase reducida por las estructuras portuarias, una sobrestimación en la
magnitud en la base de datos históricas se volvió admisible para estos análisis.

#### 5.3 Respecto a la Base de Datos histórica

**5.3.1 Caracterización Estadística de la Base de Datos Histórico**

La intensidad del viento en la base de datos histórica, según la escala de Beaufort, se presentó
bajo las categorías Calmas, Aire Ligero, Brisa Ligera y Brisa Suave y Brisa Moderada. La
principal categoría fue el Aire Ligero (52,561 %), seguido por la Brisa Ligera (39,553 %) y las
Calmas (6,417 %), mientras el resto de las categorías se encontraron bajo el 2 % de los datos.
La direccionalidad de estos vientos predominó desde el tercer cuadrante, donde dominaron en
frecuencia la dirección SSW (24,736 %), junto al S (16,106 %) y SW (15,693 %), WSW
(8,963 %). Las ocurrencias del resto de las direcciones, en los otros cuadrantes, se
encontraron bajo el 5 % de los datos.

Los estadísticos obtenidos sobre las componentes ortogonales (U y V) de la serie, indicaron
que la componente U presentó un valor medio de 0,535 m/s, revelando su predominio hacia la
dirección E y, en contraste, la media de la componente V se estimó con un valor de 0,909 m/s
señalando el predominio hacia el N. Mediante la desviación estándar se evidencia que la
componente V (0,859 m/s) revela mayor dispersión en sus datos que la componente U
(0,721 m/s). Respecto a la componente principal determinada para los datos analizados, la
componente V demostró una mayor participación (60,415 %) que la componente U (39,585 %).

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|149|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Según el análisis de densidad espectral, para ambas componentes ortogonales, destacaron
los ciclos diurnos (24 horas) y semidiurnos (12 horas), los cuales pueden estar asociados al
fenómeno de la brisa marina. En las mayores frecuencias se visualizaron algunos peaks de
menores valores. En contraste, en las menores frecuencias se señaló una energía levemente
menor y es en estas frecuencias donde se hizo más notoria la mayor energía de la componente
V, en comparación a la componente U.

En la caracterización mensual y estacional, respecto del año medio estimado desde la base
de datos histórica, se demostró el predominio de las categorías Aire Ligero y Brisa Ligera. En
el inicio del año, ambas categorías ocurrieron en cantidades similares, con el dominio en la
Brisa Ligera (50,269 %), aunque con el paso de los meses, la frecuencia del Aire Ligero
comenzó a incrementarse, representando la reducción en la intensidad del viento que sucedió
sobre todo en las estaciones de otoño e invierno. A partir del mes de junio (cuando el Aire
Ligero alcanzó 75 %), comenzaron a disminuir los vientos correspondientes a la categoría Aire
Ligero y, con ello, aumentó la Brisa Ligera y, finalmente, en diciembre lograron igualar su
ocurrencia (51,882 % y 48,118 %, respectivamente). La direccionalidad de estos datos
demostró un predominio durante el año del tercer cuadrante, sobre las direcciones S y SSW.
Entre los meses abril y agosto, dentro de las estaciones otoño e invierno, las direcciones
sufrieron una dispersión en el predominio de sus direcciones, aumentando el viento desde el
segundo cuadrante, aunque, en general, estos datos destacaron por sus bajas intensidades.

Con la caracterización diaria se determinó que durante el intervalo horario (0 - 4 hrs), las
intensidades del viento se redujeron progresivamente y, en estas horas, destacaron las
categorías Aire Ligero y Brisa Ligera (62,062 % y 34,022 %, respectivamente). En las
siguientes horas, (4 - 8 hrs) y (8 - 12 hrs), se presentaron las intensidades del viento más
bajas, resaltando el menor valor medio de 0,666 m/s. En estas horas comenzaron a
predominar la categoría Aire Ligero (77 % en ambos intervalos). Durante las horas,
(12 - 16 hrs), cuando se incrementaron las intensidades del viento, de forma que, en las horas
(16 - 20 hrs) se produjo la mayor intensidad media del día, con 2,103 m/s y predominó la
categoría Brisa Ligera (77,969 %), además de la aparición de Brisa Suave (4,406 %). En
cuanto a la direccionalidad, desde el inicio del día predominó el viento desde el tercer
cuadrante, en las cercanías de las direcciones S y SSW, sin embargo, en las horas (4 - 8 hrs)
y (8 - 12 hrs), se generó una mayor dispersión en los vientos, con bajas ocurrencias desde el
segundo cuadrante. Desde el periodo (12 - 16 hrs) el viento enfrentó una mayor dispersión
dentro del tercer cuadrante, pero centrado en la dirección SSW. Con el paso de las horas, la
concentración de los vientos se dirigió a la dirección SSW.

De la base de datos históricos, se identificó que el mayor valor determinado correspondió a
5,529 m/s desde de la dirección E, el cual ocurrió en el intervalo horario (12 - 16 hrs). Tras el
cálculo del promedio por direcciones, destacó la dirección SSW, desde donde se obtuvo el
mayor valor 1,749 m/s. Con el cálculo de la media por intervalos horarios por direcciones, se
identificó que el mayor valor fue 2,378 m/s, desde la dirección SSW, dentro del intervalo

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|150|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

(16 - 20 hrs). En general, los menores valores medios se generaron desde el primer y cuarto
cuadrante, mientras que, los mayores generalmente provinieron del tercer cuadrante.

Del año medio construido con la misma base de datos históricos, se estimó que el mayor valor
fue igual a 2,930 m/s desde la dirección SSW, que se produjo durante el mes de enero, en la
estación de verano. Con la estimación del valor medio por meses y direcciones, se identificó
que el mayor valor correspondió a 1,960 m/s desde la dirección SW, durante el mes de
diciembre. Por otro lado, con el cálculo del promedio por estaciones y direcciones, se estimó
que el mayor valor fue igual a 1,938 m/s desde la dirección SW, durante la estación de verano.

**5.3.2 Clima Extremo de Vientos**

Con el análisis extremo de los vientos históricos, se estableció una proyección de hasta 30
años del periodo de retorno en las 8 direcciones seleccionadas. La dirección S presentó el
mayor valor proyectado en 30 años, con un valor de 4,845 m/s y un intervalo superior de
5,787 m/s. En segundo lugar, clasificó la dirección E con un valor proyectado de 4,737 m/s,
sin embargo, debido a que el máximo valor se encontraba disperso en su magnitud, el intervalo
superior alcanzó un valor de 7,097 m/s. Luego, les siguieron las intensidades proyectadas para
las direcciones SW y W, con valores de 4,297 m/s y 3,980 m/s, respectivamente. En contraste,
las direcciones NE, NW y N, destacaron por sus bajas intensidades, con valores iguales a
2,091 m/s, 3,021 m/s y 3,084 m/s.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|151|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 6 REFERENCIAS

04-95, ROM. (1995). Acciones Climáticas II: Viento.

Contreras, M. L. (2001). Introducción a las series de tiempo para oceanografía y geo-ciencias.

Valparaíso, Chile: Universidad Católica de Valparaíso.

Hearn G, & Metcalfe. 2004. Spectral Analysis in Engineering Concepts and Cases. ELSEVIER

B.V., Burlington.

Palutikof J., Brabson, B., Lister, D., & Adcock, S. 1999. A review of methods to calculate

extreme wind speeds. Meteorol. Appl.

Servicio Hidrográfico y Oceanográfico de la Armada de Chile (SHOA), 2019. Instrucciones

Oceanográficas No1. SHOA PUB 3201. 4a Edición.

William J. Emery & Richard E. Thomson. (1997), Data Analysis Methods in Physical

Oceanography. Segunda Edición. ELSEVIER.

Y. Goda, “Uncertainty of design parameters from viewpoint of extreme statistics”, Trans. Amer.

Soc. Mech. Engrg. 114 (1992), pp. 76-82.

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|152|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 7 ANEXO AUTORIZACIÓN DE TRABAJOS

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|153|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|154|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|155|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 8 ANEXO ACTAS DE INSPECCIÓN 8.1 Invierno 2020

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|156|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|157|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|158|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 8.2 Verano 2020

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|159|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|160|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|161|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 9 ANEXO CERTIFICADOS DE VIGENCIA DE LA SOCIEDAD

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

|Col1|Informe Técnico<br>Oceanografía Física y Modelamiento Numérico::<br>Estudio de Vientos|No DOCUMENTO<br>IT-ITI-VIENTOS2021|EDICIÓN / REVISIÓN<br>1/1|162|
|---|---|---|---|---|
||**Informe Técnico**<br>**Oceanografía Física y Modelamiento Numérico::**<br>**Estudio de Vientos**|Fecha de emisión:<br>09-07-2021|Emitido por:<br>Ecotecnos S.A.|Emitido por:<br>Ecotecnos S.A.|

#### 10 ANEXO NOMBRAMIENTO DEL REPRESENTANTE LEGAL

Limache # 3405, Of. 31 - 32, Edif. Reitz - Viña del Mar - Fonos: 56 32 2189200 - info@ecotecnos.cl - www.ecotecnos.cl

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4-70: Lista de eventos máximos para clima extremo de vientos en las direcciones N, NE, E y SE****

| N | Col2 | Col3 | NE | Col5 | Col6 | E | Col8 | Col9 | SE | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fecha | Intensidad<br>(m/s) | Dirección<br>(°) | Fecha | Intensidad<br>(m/s) | Dirección<br>(°) | Fecha | Intensidad<br>(m/s) | Dirección<br>(°) | Fecha | Intensidad<br>(m/s) | Dirección<br>(°) |
| 09-09-2013<br>7:00 | 2,843 | 350,000 | 22-10-2011<br>3:00 | 1,896 | 60,000 | 08-07-2016<br>13:00 | 5,529 | 100,000 | 05-09-2020<br>5:00 | 3,001 | 140,000 |
| 09-08-2015<br>14:00 | 2,843 | 360,000 | 09-08-2015<br>7:00 | 1,896 | 40,000 | 25-05-2014<br>5:00 | 2,370 | 100,000 | 05-02-2017<br>0:00 | 2,528 | 150,000 |
| 16-07-2014<br>4:00 | 2,212 | 340,000 | 29-06-2016<br>8:00 | 1,896 | 30,000 | 14-07-2015<br>8:00 | 2,370 | 100,000 | 15-07-2016<br>12:00 | 2,370 | 120,000 |
| 31-08-2011<br>0:00 | 2,054 | 10,000 | 31-07-2019<br>5:00 | 1,738 | 30,000 | 23-08-2017<br>12:00 | 2,212 | 110,000 | 18-09-2014<br>11:00 | 2,212 | 120,000 |
| 12-06-2016<br>17:00 | 2,054 | 340,000 | 27-04-2012<br>8:00 | 1,580 | 60,000 | 17-06-2011<br>6:00 | 2,054 | 110,000 | 16-08-2011<br>10:00 | 2,054 | 130,000 |
| 20-06-2019<br>4:00 | 2,054 | 10,000 | 15-07-2018<br>2:00 | 1,580 | 60,000 | 01-09-2013<br>8:00 | 2,054 | 110,000 | 23-08-2012<br>8:00 | 2,054 | 130,000 |
| 14-07-2012<br>4:00 | 1,896 | 10,000 | 05-05-2013<br>10:00 | 1,422 | 30,000 | 02-01-2018<br>10:00 | 1,896 | 100,000 | 09-06-2019<br>7:00 | 2,054 | 140,000 |
| 13-12-2017<br>9:00 | 1,864 | 16,000 | 29-07-2014<br>12:00 | 1,422 | 50,000 | 18-07-2012<br>10:00 | 1,580 | 110,000 | 12-04-2013<br>11:00 | 1,896 | 120,000 |
| 10-07-2020<br>6:00 | 1,738 | 10,000 | 10-05-2017<br>10:00 | 1,422 | 60,000 | 28-07-2020<br>12:00 | 1,580 | 110,000 | 24-01-2015<br>11:00 | 1,896 | 130,000 |
| 22-06-2018<br>10:00 | 1,580 | 10,000 | 19-06-2020<br>3:00 | 1,422 | 40,000 | 28-03-2019<br>5:00 | 1,422 | 110,000 | 29-08-2018<br>10:00 | 1,580 | 120,000 |

**Tabla 4-71: Lista de eventos máximos para clima extremo de vientos en direcciones S, SW, W y NW****

| S | Col2 | Col3 | SW | Col5 | Col6 | W | Col8 | Col9 | NW | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fecha | Intensidad<br>(m/s) | Dirección<br>(°) | Fecha | Intensidad<br>(m/s) | Dirección<br>(°) | Fecha | Intensidad<br>(m/s) | Dirección<br>(°) | Fecha | Intensidad<br>(m/s) | Dirección<br>(°) |
| 18-01-2014<br>17:00 | 4,423 | 190,000 | 26-01-2011<br>21:00 | 4,107 | 210,000 | 15-01-2012<br>18:00 | 3,475 | 250,000 | 02-01-2018<br>23:00 | 2,843 | 300,000 |
| 02-01-2011<br>19:00 | 4,265 | 200,000 | 16-04-2012<br>18:00 | 4,107 | 230,000 | 20-11-2011<br>18:00 | 3,317 | 250,000 | 13-03-2016<br>15:00 | 2,528 | 320,000 |
| 22-02-2019<br>21:00 | 4,265 | 200,000 | 08-07-2016<br>18:00 | 3,949 | 220,000 | 11-05-2019<br>17:00 | 3,001 | 250,000 | 09-09-2013<br>1:00 | 2,370 | 330,000 |
| 08-07-2016<br>16:00 | 3,949 | 200,000 | 28-01-2013<br>20:00 | 3,791 | 210,000 | 29-09-2020<br>18:00 | 3,001 | 250,000 | 16-12-2015<br>20:00 | 2,212 | 320,000 |
| 10-02-2015<br>18:00 | 3,791 | 200,000 | 07-02-2020<br>18:00 | 3,791 | 230,000 | 15-10-2014<br>16:00 | 2,528 | 280,000 | 09-11-2019<br>15:00 | 2,212 | 300,000 |
| 07-02-2018<br>20:00 | 3,791 | 200,000 | 01-03-2017<br>22:00 | 3,633 | 210,000 | 21-07-2018<br>18:00 | 2,528 | 280,000 | 09-06-2014<br>16:00 | 2,054 | 330,000 |
| 13-09-2017<br>19:00 | 3,633 | 200,000 | 05-02-2018<br>18:00 | 3,633 | 210,000 | 18-02-2013<br>16:00 | 2,212 | 250,000 | 07-08-2011<br>15:00 | 1,738 | 330,000 |
| 02-01-2012<br>18:00 | 3,475 | 200,000 | 29-06-2019<br>17:00 | 3,633 | 220,000 | 29-01-2017<br>20:00 | 2,054 | 260,000 | 15-03-2012<br>15:00 | 1,738 | 320,000 |
| 20-09-2013<br>20:00 | 3,475 | 200,000 | 08-01-2014<br>17:00 | 3,475 | 220,000 | 06-11-2015<br>18:00 | 1,896 | 250,000 | 11-07-2017<br>8:00 | 1,738 | 300,000 |
| 06-04-2020<br>20:00 | 2,843 | 200,000 | 07-01-2015<br>18:00 | 3,475 | 210,000 | 01-01-2016<br>17:00 | 1,738 | 250,000 | 30-08-2020<br>17:00 | 1,738 | 300,000 |
