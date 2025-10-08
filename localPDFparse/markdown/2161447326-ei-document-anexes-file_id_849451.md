---
title: Sin título
author: Windows User
date: D:20240407181256-04'00'
language: es
type: report
pages: 16
has_toc: False
has_tables: True
extraction_quality: high
---

|SAE VOLCÁN LANIN<br>ESTUDIO DE INUNDACIÓN|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|C|Marzo 2024|Revisión<br>Cliente|MFC|PML|PML|||
|B|Febrero 2024|Revisión<br>Cliente|MFC|PML|PML|||
|A|Febrero 2024|Revisión<br>Interna|MFC|PML|PML|||
|**REV**|**FECHA**|**EMITIDO**<br>**PARA**|**POR**|**REV.**|**APR.**|**REV**|**APR**|
|**REV**|**FECHA**|**EMITIDO**<br>**PARA**|**PML INGENIERÍA LTDA.**|**PML INGENIERÍA LTDA.**|**PML INGENIERÍA LTDA.**|**BIWO Renewables**|**BIWO Renewables**|

|Col1|Proyecto<br>SAE Volcán Lanin|Estudio de Inundación|Col4|
|---|---|---|---|
||Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>i de ii|

**CONTENIDO**

1 INTRODUCCIÓN ................................................................................................................................... 1

2 ANTECEDENTES .................................................................................................................................. 2

2.1 ANTECEDENTES CARTOGRÁFICOS ......................................................................................... 2

2.2 HIDROLOGÍA DE CRECIDAS ...................................................................................................... 2

3 METODOLOGÍA ..................................................................................................................................... 3

3.1 CONSIDERACIONES GENERALES ............................................................................................ 3

3.2 CAUDAL DE INTERÉS ................................................................................................................. 3

3.3 CONDICIONES DE BORDE ......................................................................................................... 3

3.4 COEFICIENTE DE RUGOSIDAD.................................................................................................. 4

4 EJES HIDRÁULICOS ............................................................................................................................. 5

4.1 CONDICIONES DE BORDE ......................................................................................................... 5

4.2 COEFICIENTE DE RUGOSIDAD.................................................................................................. 5

4.3 CÁLCULO DE EJE HIDRÁULICO ................................................................................................. 5

5 CONCLUSIONES ................................................................................................................................... 9

6 BIBLIOGRAFÍA .................................................................................................................................... 10

**ANEXOS**

Anexo A: Hidrología de Crecidas
Anexo B: Modelo HEC-RAS

Anexo C: Poza de Inundación T=100 años (Archivo Digital KMZ)

SAE Volcán Lanin. Estudio de Inundación

|Col1|Proyecto<br>SAE Volcán Lanin|Estudio de Inundación|Col4|
|---|---|---|---|
||Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>ii de ii|

**Índice de Figuras**

Figura 1.1. Ubicación General de Proyecto .................................................................................................. 1
Figura 3.1. Esquema Planta y Perfiles Transversales .................................................................................. 3
Figura 4.1. Perfil Longitudinal con Eje Hidráulico ......................................................................................... 6
Figura 4.2. Perfil Transversal PT-16 ............................................................................................................. 6
Figura 5.1. Zona de Inundación .................................................................................................................... 9

**Índice de Tablas**

Tabla 2.1. Caudales de Crecidas .................................................................................................................. 2

Tabla 3.1. Valores de Coeficientes para Método de Cowan ......................................................................... 4
Tabla 4.1. Coeficiente de Rugosidad - Método de Cowan ............................................................................ 5
Tabla 4.2. Resultado Eje Hidráulico, TR=100 años ...................................................................................... 8

SAE Volcán Lanin. Estudio de Inundación

|Col1|Proyecto<br>SAE Volcán Lanin|Estudio de Inundación|Col4|
|---|---|---|---|
||Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>1 de 13|

**1** **INTRODUCCIÓN**

El presente informe tiene por objetivo calcular la poza de inundación en el río Amantible para la crecida de
100 años de período de retorno que limita con la zona del proyecto SAE Volcán Lanin.

El proyecto se ubica aproximadamente 1 km al norponiente de la localidad de Curacautín, comuna de
Curacautín, provincia de Malleco, Región de La Araucanía.

En la Figura 1.1 se presenta la ubicación general de la zona de interés.

**Figura 1.1. Ubicación General de Proyecto**

**Fuente** : Elaboración Propia. Imágenes Satelitales

SAE Volcán Lanin. Estudio de Inundación

|Col1|Proyecto<br>SAE Volcán Lanin|Estudio de Inundación|Col4|
|---|---|---|---|
||Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>2 de 13|

**2** **ANTECEDENTES**

2.1 ANTECEDENTES CARTOGRÁFICOS

Se dispone de un levantamiento topográfico del proyecto, proporcionado por el Mandante, en escala
1:1000, en coordenadas UTM, Datum WGS 1984, Huso 19.

Por otro lado, se levantaron 20 perfiles transversales espaciados cada 20 m en el cauce, totalizando un
tramo de 380 m.

La información fue complementada con imágenes satelitales.

2.2 HIDROLOGÍA DE CRECIDAS

El estudio de hidrología de crecidas se incluye en el Anexo A de presente informe. En la Tabla 2.1 se
presentan los caudales de crecidas para distintos períodos de retorno para el sector en estudio.

**Tabla 2.1. Caudales de Crecidas**

SAE Volcán Lanin. Estudio de Inundación

|T|Cuenca<br>Amantible [m3/s]|
|---|---|
|**[años]**|**[años]**|
|2|27,9|
|5|40,8|
|10|51,5|
|25|67,6|
|50|81,6|
|100|97,4|
|200|115,1|

|Col1|Proyecto<br>SAE Volcán Lanin|Estudio de Inundación|Col4|
|---|---|---|---|
||Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>3 de 13|

**3** **METODOLOGÍA**

3.1 CONSIDERACIONES GENERALES

El estudio hidráulico del tramo de interés se realizó sobre la base de los antecedentes presentados en el
capítulo 2 de este informe.

Se utilizaron perfiles transversales obtenidos del levantamiento topográfico mencionado en 2.2, espaciados
cada 20 m en una longitud total de 380 m sobre el río Amantible, totalizando 20 perfiles transversales.

El modelo hidráulico se desarrolló utilizando el software HEC-RAS versión 6.3.1 desarrollado por el U.S.
Army Corps of Engineers. Este software realiza la modelación unidimensional del flujo, siendo ampliamente
utilizado para este tipo de estudios.

En la Figura 3.1 se presenta un esquema con la planta de la zona y los perfiles transversales considerados.

**Figura 3.1. Esquema Planta y Perfiles Transversales**

3.2 CAUDAL DE INTERÉS

El caudal de interés corresponde al caudal de 100 años de período de retorno. A partir del estudio
hidrológico de crecidas, incluido en el Anexo A, se obtiene que el caudal de interés es de 97,4 m [3] /s.

3.3 CONDICIONES DE BORDE

El modelo fue evaluado en la condición de flujo de régimen mixto. Para las condiciones de borde, se
consideró altura normal tomando la pendiente promedio del lecho para el sector de aguas abajo y para el
sector de aguas arriba.

SAE Volcán Lanin. Estudio de Inundación

|Col1|Proyecto<br>SAE Volcán Lanin|Estudio de Inundación|Col4|
|---|---|---|---|
||Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>4 de 13|

3.4 COEFICIENTE DE RUGOSIDAD

Para estimar la rugosidad en el cauce se empleó el método de Cowan, cuya relación se presenta a
continuación.

_n_ = _m_  ( _n_ 0 + _n_ 1 + _n_ 2 + _n_ 3 + _n_ 4 )

Donde:

n 0 : Rugosidad base para un canal recto, uniforme, prismático y rugosidad homogénea.
n 1 : Rugosidad adicional debida a irregulares superficiales del perímetro mojado a lo largo del tramo en

estudio.

n 2 : Rugosidad adicional equivalente debida a la variación de forma y de dimensiones de las secciones a

lo largo del tramo en estudio.
n 3 : Rugosidad adicional equivalente debida a obstrucciones existentes en el cauce.
n 4 : Rugosidad adicional equivalente debida a la presencia de vegetación.

m: Factor de corrección para incorporar efecto de sinuosidad del cauce o presencia de meandros.

En la Tabla 3.1 se presentan rangos de valores de los parámetros presentados en la fórmula de Cowan, a
partir de los cuales es posible estimar el valor del coeficiente de rugosidad de Manning.

**Tabla 3.1. Valores de Coeficientes para Método de Cowan**

**Fuente** : Manual de Carreteras, Volumen 3, Sección 3.705

El cálculo de los coeficientes de rugosidad del cauce se encuentra en el capítulo 4 del presente informe.

SAE Volcán Lanin. Estudio de Inundación

|Col1|Proyecto<br>SAE Volcán Lanin|Estudio de Inundación|Col4|
|---|---|---|---|
||Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>5 de 13|

**4** **EJES HIDRÁULICOS**

En este capítulo se presenta en detalle el cálculo y resultado del eje hidráulico asociado al caudal de interés.

4.1 CONDICIONES DE BORDE

El modelo fue evaluado en la condición de régimen mixto, por ende, se requieren condiciones de borde
para el tramo de aguas arriba y para el tramo de aguas abajo del cauce. En ambos sectores se adopta
altura normal con pendiente de 0,5%.

4.2 COEFICIENTE DE RUGOSIDAD

De acuerdo con la geometría y características del cauce, en la Tabla 4.1 se presentan los valores
adoptados según la expresión de Cowan.

**Tabla 4.1. Coeficiente de Rugosidad - Método de Cowan**

|Factor|Descripción|Condición|Valor|
|---|---|---|---|
|n0|Material del lecho|Grava Fina|0,024|
|n1|Grado de irregularidad Perímetro mojado|Leve|0,005|
|n2|Variaciones de secciones|Graduales|0,000|
|n3|Efecto relativo a las obstrucciones|Despreciable - Leve|0,005|
|n4|Densidad de vegetación|Baja- Media|0,010|
|m|Sinuosidad y frecuencia de meandros|Leve|1,000,|
|n|Coeficiente de Rugosidad||0,044|
|**n **|**Coeficiente de Rugosidad Adoptado**||**0,045**|

Los valores del coeficiente de rugosidad definidos anteriormente corresponden al lecho, para las riberas
del cauce se considera un aumento de rugosidad asociado al factor vegetación (Alta), adoptándose un
valor de 0,070.

4.3 CÁLCULO DE EJE HIDRÁULICO

Sobre la base de las consideraciones y metodología antes presentadas, el resultado del eje hidráulico para
el caudal de crecida de 100 años de período de retorno se muestra en el perfil longitudinal presentado en
la Figura 4.1 y en la Figura 4.2 se muestra el resultado del eje hidráulico para el perfil transversal PT-16,
perfil ubicado frente al sector del proyecto.

SAE Volcán Lanin. Estudio de Inundación

|Col1|Proyecto<br>SAE Volcán Lanin<br>Tipo documento<br>Informe|Estudio de Inundación|Col4|
|---|---|---|---|
||<br>Proyecto<br>**SAE Volcán Lanin**<br>Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>6 de 13|

**Figura 4.1. Perfil Longitudinal con Eje Hidráulico**

**Figura 4.2. Perfil Transversal PT-16**

SAE Volcán Lanin. Estudio de Inundación

|Col1|Proyecto<br>SAE Volcán Lanin|Estudio de Inundación|Col4|
|---|---|---|---|
||Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>7 de 13|

En el Anexo B se presenta el modelo HEC-RAS con el detalle de los resultados hidráulicos en cada perfil
transversal.

De acuerdo con los resultados obtenidos se observa que el escurrimiento en el cauce es de régimen
subcrítico en gran parte del tramo estudiado. La velocidad de escurrimiento promedio es de
aproximadamente 1,7 m/s y el promedio de la altura de agua es 3,91 m.

A continuación, en la Tabla 4.2 se presentan los parámetros obtenidos de la modelación hidráulica
realizada para el tramo de cauce en estudio.

SAE Volcán Lanin. Estudio de Inundación

|Col1|Proyecto<br>SAE Volcán Lanin|Estudio de Inundación|Col4|
|---|---|---|---|
||Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>8 de 13|

**Tabla 4.2. Resultado Eje Hidráulico, TR=100 años**

|Perfil<br>Transversal|Caudal<br>[m3/s]|Z Fondo<br>[m s.n.m.]|Z E.H.<br>[m s.n.m.]|Z H.C.<br>[m s.n.m.]|J<br>[m/m]|B<br>[m]|H<br>[m]|V<br>[m/s]|A<br>[m2]|L<br>[m]|X<br>[m]|Rh<br>[m]|Fr<br>[-]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|PT-01|97.4|495.54|499.32|497.62|0.0011|499.42|3.78|1.10|88.3|49.0|50.7|1.74|0.34|
|PT-02|97.4|492.33|499.36|494.95|0.0002|499.40|7.03|0.69|141.4|44.0|47.2|2.99|0.16|
|PT-03|97.4|495.04|499.32|497.44|0.0007|499.39|4.28|1.00|97.2|51.4|52.5|1.85|0.27|
|PT-04|97.4|495.30|499.08|497.88|0.0027|499.34|3.78|1.99|49.0|30.5|31.8|1.54|0.57|
|PT-05|97.4|495.73|498.92|498.24|0.0048|499.26|3.19|2.36|41.4|24.8|25.9|1.60|0.64|
|PT-06|97.4|494.82|499.06|497.00|0.0008|499.16|4.24|1.22|79.7|39.4|41.2|1.94|0.31|
|PT-07|97.4|494.97|499.05|497.12|0.0008|499.14|4.08|1.17|83.6|45.8|47.7|1.75|0.32|
|PT-08|97.4|495.62|498.83|498.02|0.0036|499.09|3.21|1.97|49.5|30.4|31.7|1.56|0.56|
|PT-09|97.4|495.83|498.20|498.20|0.0142|498.92|2.37|3.31|29.5|22.0|22.6|1.30|1.04|
|PT-10|97.4|495.02|498.37|497.42|0.0028|498.58|3.35|1.79|54.4|32.7|33.4|1.63|0.51|
|PT-11|97.4|494.88|498.37|496.78|0.0015|498.52|3.49|1.57|62.1|32.9|34.5|1.80|0.40|
|PT-12|97.4|491.81|498.41|495.34|0.0005|498.48|6.60|0.97|100.8|45.2|48.5|2.08|0.25|
|PT-13|97.4|493.99|498.20|496.80|0.0023|498.45|4.21|1.90|51.3|22.4|24.4|2.10|0.47|
|PT-14|97.4|494.90|498.29|496.78|0.0010|498.37|3.39|1.09|89.2|50.2|51.9|1.72|0.29|
|PT-15|97.4|494.46|498.23|496.80|0.0012|498.34|3.77|1.06|92.1|59.9|62.0|1.49|0.38|
|PT-16|97.4|493.99|498.10|496.97|0.0026|498.30|4.11|1.38|70.8|64.8|67.1|1.05|0.60|
|PT-17|97.4|494.66|497.91|497.20|0.0045|498.22|3.25|2.25|43.3|23.6|24.8|1.74|0.58|
|Aguas Arriba Puente|97.4|494.66|497.90|Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s|Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s|Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s|Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s|Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s|Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s|Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s|Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s|Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s|Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s|
|Aguas Abajo Puente|97.4|494.29|497.51|Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s|Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s|Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s|Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s|Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s|Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s|Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s|Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s|Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s|Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s|
|PT-18|97.4|494.29|497.53|496.76|0.0111|497.94|3.24|2.48|39.3|16.2|30.9|1.27|0.58|
|PT-19|97.4|494.23|497.35|496.86|0.0058|497.78|3.12|2.41|40.4|23.4|24.7|1.64|0.70|
|PT-20|97.4|493.50|497.21|496.37|0.0050|497.67|3.71|2.33|41.8|26.9|28.5|1.47|0.77|

Z Fondo: Cota de Fondo [m s.n.m.] J: Pendiente Línea de Energía [m/m] V: Velocidad Media de Escurrimiento [m/s] X: Perímetro Mojado [m]

Z E.H.: Cota Eje Hidráulico [m s.n.m.] B: Bernoulli [m] A: Área de Flujo [m2] Rh: Radio Hidráulico [m]

Z H.C.: Cota Altura Crítica [m s.n.m.] H: Altura de Escurrimiento [m] L: Ancho Lámina de Agua [m] Fr: Número de Froude

SAE Volcán Lanin. Estudio de Inundación

|Col1|Proyecto<br>SAE Volcán Lanin|Estudio de Inundación|Col4|
|---|---|---|---|
||Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>9 de 13|

**5** **CONCLUSIONES**

En la Figura 5.1 se presenta la poza de inundación obtenida para la crecida de 100 años de período de

retorno.

**Figura 5.1. Zona de Inundación**

Se concluye que la poza de inundación para la crecida de interés no afecta la zona del proyecto. La
distancia entre el límite del área de inundación y el polígono del proyecto es de al menos 70 m.

SAE Volcán Lanin. Estudio de Inundación

|Col1|Proyecto<br>SAE Volcán Lanin|Estudio de Inundación|Col4|
|---|---|---|---|
||Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>10 de 13|

**6** **BIBLIOGRAFÍA**

 - Manual de Carreteras, Volumen No 3, Instrucciones y Criterios de Diseño, Ministerio de Obras
Públicas, 2022

 - Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas sin Información Fluviométrica.
Dirección General de Aguas, Ministerio de Obras Públicas, 1995.

 - Elementos de Hidrología. Basilio Espíldora C., Ernesto Brown F., Guillermo Cabrera F., Pablo
Isensee M. Universidad de Chile, 1975.

 - Hidrología Aplicada. Ven Te Chow, 1994.

 - Hydrologic Soil Groups. National Engineering Handbook, Part 630, Hydrology Chapter 7. USDANRCS.

 - Hidráulica Aplicada al Diseño de Obras, Horacio Mery M., RIL EDITORES, 2013.

 - Guías Metodológicas para Presentación y Revisión Técnica de Proyectos de Modificación de
Cauces Naturales y Artificiales. Dirección General de Aguas, 2016.

 - Guía de Permisos ambientales Sectoriales en el SEIA. Permiso para Efectuar Modificaciones de
Cauce.

SAE Volcán Lanin. Estudio de Inundación

|Col1|Proyecto<br>SAE Volcán Lanin|Estudio de Inundación|Col4|
|---|---|---|---|
||Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>11 de 13|

## ANEXO A HIDROLOGÍA DE CRECIDAS

SAE Volcán Lanin. Estudio de Inundación

|Col1|Proyecto<br>SAE Volcán Lanin|Estudio de Inundación|Col4|
|---|---|---|---|
||Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>12 de 13|

SAE Volcán Lanin. Estudio de Inundación

## ANEXO B MODELO HEC-RAS

|Col1|Proyecto<br>SAE Volcán Lanin|Estudio de Inundación|Col4|
|---|---|---|---|
||Tipo documento<br> <br>**Informe**|Revisión<br>C|Página<br>13 de 13|

## ANEXO C POZA DE INUNDACIÓN T=100 AÑOS (ARCHIVO DIGITAL KMZ)

SAE Volcán Lanin. Estudio de Inundación

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.1.: Caudales de Crecidas****

| T | Cuenca<br>Amantible [m3/s] |
| --- | --- |
| **[años]** | **[años]** |
| 2 | 27,9 |
| 5 | 40,8 |
| 10 | 51,5 |
| 25 | 67,6 |
| 50 | 81,6 |
| 100 | 97,4 |
| 200 | 115,1 |

**Tabla 3.1.: Valores de Coeficientes para Método de Cowan****

| Col1 | Proyecto<br>SAE Volcán Lanin | Estudio de Inundación | Col4 |
| --- | --- | --- | --- |
|  | Tipo documento<br> <br>**Informe** | Revisión<br>C | Página<br>5 de 13 |

**Tabla 4.1.: Coeficiente de Rugosidad - Método de Cowan****

| Factor | Descripción | Condición | Valor |
| --- | --- | --- | --- |
| n0 | Material del lecho | Grava Fina | 0,024 |
| n1 | Grado de irregularidad Perímetro mojado | Leve | 0,005 |
| n2 | Variaciones de secciones | Graduales | 0,000 |
| n3 | Efecto relativo a las obstrucciones | Despreciable - Leve | 0,005 |
| n4 | Densidad de vegetación | Baja- Media | 0,010 |
| m | Sinuosidad y frecuencia de meandros | Leve | 1,000, |
| n | Coeficiente de Rugosidad |  | 0,044 |
| **n ** | **Coeficiente de Rugosidad Adoptado** |  | **0,045** |

**Tabla 4.2.: Resultado Eje Hidráulico, TR=100 años****

| Perfil<br>Transversal | Caudal<br>[m3/s] | Z Fondo<br>[m s.n.m.] | Z E.H.<br>[m s.n.m.] | Z H.C.<br>[m s.n.m.] | J<br>[m/m] | B<br>[m] | H<br>[m] | V<br>[m/s] | A<br>[m2] | L<br>[m] | X<br>[m] | Rh<br>[m] | Fr<br>[-] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PT-01 | 97.4 | 495.54 | 499.32 | 497.62 | 0.0011 | 499.42 | 3.78 | 1.10 | 88.3 | 49.0 | 50.7 | 1.74 | 0.34 |
| PT-02 | 97.4 | 492.33 | 499.36 | 494.95 | 0.0002 | 499.40 | 7.03 | 0.69 | 141.4 | 44.0 | 47.2 | 2.99 | 0.16 |
| PT-03 | 97.4 | 495.04 | 499.32 | 497.44 | 0.0007 | 499.39 | 4.28 | 1.00 | 97.2 | 51.4 | 52.5 | 1.85 | 0.27 |
| PT-04 | 97.4 | 495.30 | 499.08 | 497.88 | 0.0027 | 499.34 | 3.78 | 1.99 | 49.0 | 30.5 | 31.8 | 1.54 | 0.57 |
| PT-05 | 97.4 | 495.73 | 498.92 | 498.24 | 0.0048 | 499.26 | 3.19 | 2.36 | 41.4 | 24.8 | 25.9 | 1.60 | 0.64 |
| PT-06 | 97.4 | 494.82 | 499.06 | 497.00 | 0.0008 | 499.16 | 4.24 | 1.22 | 79.7 | 39.4 | 41.2 | 1.94 | 0.31 |
| PT-07 | 97.4 | 494.97 | 499.05 | 497.12 | 0.0008 | 499.14 | 4.08 | 1.17 | 83.6 | 45.8 | 47.7 | 1.75 | 0.32 |
| PT-08 | 97.4 | 495.62 | 498.83 | 498.02 | 0.0036 | 499.09 | 3.21 | 1.97 | 49.5 | 30.4 | 31.7 | 1.56 | 0.56 |
| PT-09 | 97.4 | 495.83 | 498.20 | 498.20 | 0.0142 | 498.92 | 2.37 | 3.31 | 29.5 | 22.0 | 22.6 | 1.30 | 1.04 |
| PT-10 | 97.4 | 495.02 | 498.37 | 497.42 | 0.0028 | 498.58 | 3.35 | 1.79 | 54.4 | 32.7 | 33.4 | 1.63 | 0.51 |
| PT-11 | 97.4 | 494.88 | 498.37 | 496.78 | 0.0015 | 498.52 | 3.49 | 1.57 | 62.1 | 32.9 | 34.5 | 1.80 | 0.40 |
| PT-12 | 97.4 | 491.81 | 498.41 | 495.34 | 0.0005 | 498.48 | 6.60 | 0.97 | 100.8 | 45.2 | 48.5 | 2.08 | 0.25 |
| PT-13 | 97.4 | 493.99 | 498.20 | 496.80 | 0.0023 | 498.45 | 4.21 | 1.90 | 51.3 | 22.4 | 24.4 | 2.10 | 0.47 |
| PT-14 | 97.4 | 494.90 | 498.29 | 496.78 | 0.0010 | 498.37 | 3.39 | 1.09 | 89.2 | 50.2 | 51.9 | 1.72 | 0.29 |
| PT-15 | 97.4 | 494.46 | 498.23 | 496.80 | 0.0012 | 498.34 | 3.77 | 1.06 | 92.1 | 59.9 | 62.0 | 1.49 | 0.38 |
| PT-16 | 97.4 | 493.99 | 498.10 | 496.97 | 0.0026 | 498.30 | 4.11 | 1.38 | 70.8 | 64.8 | 67.1 | 1.05 | 0.60 |
| PT-17 | 97.4 | 494.66 | 497.91 | 497.20 | 0.0045 | 498.22 | 3.25 | 2.25 | 43.3 | 23.6 | 24.8 | 1.74 | 0.58 |
| Aguas Arriba Puente | 97.4 | 494.66 | 497.90 | Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s | Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s | Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s | Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s | Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s | Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s | Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s | Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s | Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s | Altura de Escurrimiento = 3,23 m; Velocidad de Escurrimiento 2,31 m/s |
| Aguas Abajo Puente | 97.4 | 494.29 | 497.51 | Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s | Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s | Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s | Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s | Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s | Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s | Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s | Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s | Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s | Altura de Escurrimiento = 3,22 m; Velocidad de Escurrimiento 2,97 m/s |
| PT-18 | 97.4 | 494.29 | 497.53 | 496.76 | 0.0111 | 497.94 | 3.24 | 2.48 | 39.3 | 16.2 | 30.9 | 1.27 | 0.58 |
| PT-19 | 97.4 | 494.23 | 497.35 | 496.86 | 0.0058 | 497.78 | 3.12 | 2.41 | 40.4 | 23.4 | 24.7 | 1.64 | 0.70 |
| PT-20 | 97.4 | 493.50 | 497.21 | 496.37 | 0.0050 | 497.67 | 3.71 | 2.33 | 41.8 | 26.9 | 28.5 | 1.47 | 0.77 |
