---
title: Sin título
author: Oscar Suárez Loira
date: D:20180309161041-03'00'
language: es
type: report
pages: 27
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Listado de Figuras
  - Listado de Tablas
  - LISTADO DE ANEXOS
  - 1 INTRODUCCIÓN Y OBJETIVOS
  - 2 DETERMINACIÓN DE LA PRECIPITACIÓN MÁXIMA EN 24 HORAS
  - 3 MÉTODOS DGA PARA CÁLCULO DE CRECIDAS EN CUENCAS SIN CONTROL
  - 4 REGULACION DE EMBALSES
  - 5 CONCLUSIONES Y RECOMENDACIONES
-->

**DECLARACIÓN DE IMPACTO AMBIENTAL**

**PROYECTO MINERA EL TURCO**

**MODIFICACIÓN DE CAUCE ESTERO ZÁRATE**

**PERMISO AMBIENTAL SECTORIAL 156**

**MEMORIA DE CÁLCULO DE HIDROLOGÍA**

**Y CÁLCULO DE CAUDALES**

**OT9588-HI-C-CAL-001**

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|B|16-02-2018|Para Aprobación del Cliente|MBB|PVC||
|A|13-11-2017|Para coordinación interna|MBB|PVC||
|**REV**|**FECHA**|**DESCRIPCIÓN DE LA**<br>**REVISIÓN**|**AUTOR**<br>**ORIGINAL**|**REVISOR**|**CLIENTE**|

**ÍNDICE DE CONTENIDOS**

1 INTRODUCCIÓN Y OBJETIVOS .................................................................................................. 5

2 DETERMINACIÓN DE LA PRECIPITACIÓN MÁXIMA EN 24 HORAS ........................................ 5

3 MÉTODOS DGA PARA CÁLCULO DE CRECIDAS EN CUENCAS SIN CONTROL
FLUVIOMÉTRICO .......................................................................................................................... 8

3.1 MÉTODO RACIONAL MODIFICADO ............................................................................................ 8

3.2 MÉTODO DE VERNI Y KING MODIFICADO .............................................................................. 10

3.3 MÉTODO DGA-AC ...................................................................................................................... 12

3.4 CÁLCULO DE CAUDALES MÁXIMOS INSTANTÁNEOS POR MÉTODO ................................. 15

3.4.1 Método Racional Modificado ........................................................................................................ 16

3.4.2 Método Verni y King ..................................................................................................................... 16

3.4.3 Método DGA-AC .......................................................................................................................... 17

3.5 Resumen de resultados ............................................................................................................... 18

4 REGULACION DE EMBALSES ................................................................................................... 20

5 CONCLUSIONES Y RECOMENDACIONES .............................................................................. 23

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE

# Listado de Figuras

Figura 2.1: Correlación Est. Lagunillas y Est. San Antonio - Pp. máx en 24 hrs. ......................................... 5

Figura 2.2: Correlación Est. Cerrillos de Leyda y Est. San Antonio - Pp. máx. en 24 hrs. ........................... 6

Figura 2.3: Correlación Est. Cerrillos de Leyda y Est. Lagunillas - Pp. máx. en 24 hrs. .............................. 6

Figura 3.1: Extrapolación Coeficientes de duración de Varas y Sánchez (1983). Estación Rapel. ...... 9

Figura 3.2: Extrapolación de los coeficientes de frecuencia para V Región, método Verni y King ............ 11

Figura 3.3: Precipitación media anual de la estación Cerrillos de Leyda. .................................................. 13

Figura 3.4: Extrapolación de los coeficientes de frecuencia, método DGA-AC .......................................... 14

Figura 3.5: Plano de Cuencas IGM ............................................................................................................. 15

Figura 3.6: Fotografía Estero La Viña Aguas Abajo Embalse Las Palmas I ............................................... 19

Figura 4.1: Plano de Sub-cuencas IGM con y Con Regulación de Embalse .............................................. 20

# Listado de Tablas

Tabla 2.1: Resultados del análisis de frecuencia .......................................................................................... 7

<!-- INICIO TABLA 2.1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- retorno de 100 y 200 años. Se realizó un ajuste de la serie de datos con 5 distribuciones de probabilidad (Normal, Log-Normal, Pearson III, Log-Pearson y Gumbel) de manera de identificar aquella distribución que mejor se ajustaba al conjunto de los datos. Los resultados de este análisis se muestran en forma resumida en la Tabla 2.1. -->

**Tabla 2.1: Resultados del análisis de frecuencia****

| Distribución de<br>probabilidad | Coeficiente<br>R2 | Pp. Máx 24 Hrs<br>Tr=10 | Pp. Máx 24<br>Hrs Tr=25 | Pp. Máx 24 Hrs<br>Tr=100 | Pp. Máx 24<br>Hrs Tr=200 |
| --- | --- | --- | --- | --- | --- |
| ~~Normal (*)~~ | ~~0,916~~ | ~~85~~ | ~~96~~<br> | ~~108~~ | ~~114~~ |
| Log Normal | 0,982 | 85 | ~~101~~<br> | 125 | 137 |
| Peason III | 0,981 | 86 | ~~102~~<br> | 124 | 134 |
| Log Pearson III | 0,982 | 86 | ~~105~~<br> | 135 | 152 |
| Gumbel | 0,981<br> | 88<br> | ~~106~~<br> | 132 | 145 |

<!-- Estadísticas: 5 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. (*) La distribución Normal no aprueba el test Chi-cuadrado Como se observa, todas las distribuciones muestran un buen ajuste a la serie de datos de la -->
<!-- FIN TABLA 2.1 -->


Tabla 2.2: Precipitaciones de diseño y verificación ...................................................................................... 7

<!-- INICIO TABLA 2.2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- para un período de retorno de 100 años, se aplicó un criterio conservador, eligiéndose el valor que entrega el ajuste de la distribución **Log Pearson III** . De esta forma, las precipitaciones para diseño (T=10, T=25 y T=100 años) y verificación (T=200 años) son las mostradas en la Tabla 2.2 siguiente: -->

**Tabla 2.2: Precipitaciones de diseño y verificación****

| Período de retorno | Pp. Máx 24 Hrs |
| --- | --- |
| T=10 | 86 |
| T=25 | 105 |
| T=100 | 135 |
| T=200<br> | 152<br> |

<!-- Estadísticas: 4 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. En el Anexo A se incluye la serie de datos de la estación Cerrillos de Leyda y en el Anexo B los gráficos con los ajustes para todas las distribuciones de probabilidad. -->
<!-- FIN TABLA 2.2 -->


Tabla 3.1: Coeficientes de duración de Varas y Sánchez (1983) para estación Rapel ................................ 9

<!-- INICIO TABLA 3.1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- DIA MINERA EL TURCO HIDROLOGIA Y CALCULO DE CAUDALES PAS 156 ESTERO ZÁRATE 8 -->

**Tabla 3.1: Coeficientes de duración de Varas y Sánchez (1983) para estación Rapel****

| Duración (hr) | CD |
| --- | --- |
| 1 | 0,15 |
| 2 | 0,23 |
| 4 | 0,34 |
| 6 | 0,47 |
| 8 | 0,56 |
| 10 | 0,64 |
| 12 | 0,71 |
| 14 | 0,79 |
| 18 | 0,91 |
| 24<br> | 1,00<br> |

<!-- Estadísticas: 10 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Modificado de DGA (1995). En la Figura 3.1 se presenta un ajuste logarítmico estimado a partir de los valores presentados en la Tabla 3.1. Esta relación permitirá estimar los coeficientes de duración para un tiempo igual -->
<!-- FIN TABLA 3.1 -->


Tabla 3.2: Coeficientes de frecuencia, método Verni y King para V Región .............................................. 11

<!-- INICIO TABLA 3.2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- PAS 156 ESTERO ZÁRATE 10 **Figura 3.2: Extrapolación de los coeficientes de frecuencia para V Región, método Verni y** **King** -->

**Tabla 3.2: Coeficientes de frecuencia, método Verni y King para V Región****

| Período de<br>retorno<br>(años) | C(T)/C(T=10) |
| --- | --- |
| 2 | 0,38 |
| 5 | 0,84 |
| 10 | 1,00 |
| 20 | 1,15 |
| 25 | 1,22 |
| 50 | 1,38 |
| 100 | 1,59 |
| 200<br> | 1,81<br> |

<!-- Estadísticas: 8 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Modificado de DGA (1995). (*) Valor extrapolado. DIA MINERA EL TURCO HIDROLOGIA Y CALCULO DE CAUDALES -->
<!-- FIN TABLA 3.2 -->


Tabla 3.3: Coeficientes de frecuencia, método DGA-AC ............................................................................ 14

<!-- INICIO TABLA 3.3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- HIDROLOGIA Y CALCULO DE CAUDALES PAS 156 ESTERO ZÁRATE 13 **Figura 3.4: Extrapolación de los coeficientes de frecuencia, método DGA-AC** -->

**Tabla 3.3: Coeficientes de frecuencia, método DGA-AC****

| Período de<br>retorno<br>(años) | C T<br>F |
| --- | --- |
| 2 | 0,18 |
| 5 | 0,56 |
| 10 | 1,00 |
| 20 | 1,61 |
| 25 | 1,86 |
| 50 | 2,77 |
| 75 | 3,44 |
| 100 | 3,97 |
| 200<br> | 4,21*<br> |

<!-- Estadísticas: 9 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Modificado de DGA (1995). (*) Valor extrapolado. DIA MINERA EL TURCO HIDROLOGIA Y CALCULO DE CAUDALES -->
<!-- FIN TABLA 3.3 -->


Tabla 3.4: Parámetros morfométricos de las cuencas en estudio. ............................................................. 15

<!-- INICIO TABLA 3.4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 3.5: Plano de Cuencas IGM** Fuente: Elaboración propia en base a IGM -->

**Tabla 3.4: Parámetros morfométricos de las cuencas en estudio.****

| Cuenca | A (km2)<br>p | ∆H (m) | L (km) | i (m/m) | t (hr)<br>c |
| --- | --- | --- | --- | --- | --- |
| A | 68,20 | 847 | 18,918 | 0,045 | 2,11 |
| B | 30,38 | 197 | 11,272 | 0,017 | 2,04 |

<!-- Estadísticas: 2 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Es posible advertir que los tiempos de concentración son casi iguales, razón por la cual la superposición de ambos caudales en un 100% es una condición conservadora pero realista. Se detallan a continuación los resultados obtenidos con cada uno de los métodos de cálculo -->
<!-- FIN TABLA 3.4 -->


Tabla 3.5: Caudales máximos para cuenca A, método racional modificado. ............................................. 16

<!-- INICIO TABLA 3.5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la Tabla 3.5 se detalla el cálculo para la estimación de los caudales máximos en la cuenca A, de acuerdo con el método racional modificado. La Tabla 3.6 muestra la misma estimación, pero para la cuenca B. -->

**Tabla 3.5: Caudales máximos para cuenca A, método racional modificado.****

| Período<br>de<br>Retorno T<br>(años) | Pp Max<br>24 hr<br>(mm) | C(T) | T (hr)<br>C | CD | Intensidad<br>Tc (mm/hr) | Q máx. (m3/s) | Rendimiento<br>(m3/s/km2) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ~~10~~<br> | ~~86~~<br> | ~~0,080~~<br> | ~~2,11~~<br> | ~~0,238~~<br> | ~~10~~<br> | ~~14,7~~<br> | ~~0,22~~<br> |
| ~~25~~<br> | ~~105~~<br> | ~~0,098~~<br> | ~~2,11~~<br> | ~~0,238~~<br> | ~~12~~<br> | ~~22,8~~<br> | ~~0,33~~<br> |
| ~~100~~ | ~~135~~ | ~~0,127~~ | ~~2,11~~ | ~~0,238~~ | ~~15~~ | ~~35,8~~ | ~~0,53~~ |
| 200<br> | 152 | 0,145 | 2,11 | 0,238 | 17 | 47,0 | 0,69 |

<!-- Estadísticas: 4 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 3.6: Caudales máximos para cuenca B, método racional modificado.** |Período<br>de<br>Retorno T<br>(años)|Pp Max<br>24 hr<br>(mm)|C(T)|T (hr)<br>C|CD|Intensidad<br>Tc (mm/hr)|Q máx. (m3/s)|Rendimiento<br>(m3/s/km2)| |---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 3.5 -->


Tabla 3.6: Caudales máximos para cuenca B, método racional modificado. ............................................. 16

<!-- INICIO TABLA 3.6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |~~10~~<br>|~~86~~<br>|~~0,080~~<br>|~~2,11~~<br>|~~0,238~~<br>|~~10~~<br>|~~14,7~~<br>|~~0,22~~<br>| |~~25~~<br>|~~105~~<br>|~~0,098~~<br>|~~2,11~~<br>|~~0,238~~<br>|~~12~~<br>|~~22,8~~<br>|~~0,33~~<br>| |~~100~~|~~135~~|~~0,127~~|~~2,11~~|~~0,238~~|~~15~~|~~35,8~~|~~0,53~~| |200<br>|152|0,145|2,11|0,238|17|47,0|0,69| -->

**Tabla 3.6: Caudales máximos para cuenca B, método racional modificado.****

| Período<br>de<br>Retorno T<br>(años) | Pp Max<br>24 hr<br>(mm) | C(T) | T (hr)<br>C | CD | Intensidad<br>Tc (mm/hr) | Q máx. (m3/s) | Rendimiento<br>(m3/s/km2) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ~~10~~<br> | ~~86~~<br> | ~~0,080~~<br> | ~~2,04~~<br> | ~~0,233~~<br> | ~~10~~<br> | ~~6,6~~<br> | ~~0,22~~<br> |
| ~~25~~<br> | ~~105~~<br> | ~~0,098~~<br> | ~~2,04~~<br> | ~~0,233~~<br> | ~~12~~<br> | ~~9,8~~<br> | ~~0,32~~<br> |
| ~~100~~ | ~~135~~ | ~~0,127~~ | ~~2,04~~ | ~~0,233~~ | ~~15~~ | ~~16,5~~ | ~~0,54~~ |
| 200<br> | 152 | 0,145 | 2,04 | 0,233 | 17 | 21,2 | 0,70 |

<!-- Estadísticas: 4 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- ### 3.4.2 Método Verni y King En la Tabla 3.7 se detalla el cálculo para la estimación de los caudales máximos en la cuenca A, de acuerdo con el método de Verni y King. La Tabla 3.8 muestra la misma estimación, pero para -->
<!-- FIN TABLA 3.6 -->


Tabla 3.7: Caudales máximos para cuenca A, método de Verni y King. .................................................... 16

<!-- INICIO TABLA 3.7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la Tabla 3.7 se detalla el cálculo para la estimación de los caudales máximos en la cuenca A, de acuerdo con el método de Verni y King. La Tabla 3.8 muestra la misma estimación, pero para la cuenca B. -->

**Tabla 3.7: Caudales máximos para cuenca A, método de Verni y King.****

| Período de<br>Retorno T<br>(años) | Pp Max 24<br>hr (mm) | C(T) | Q máx.<br>(m3/s) | Rendimiento<br>(m3/s/km2) |
| --- | --- | --- | --- | --- |
| ~~10~~<br> | ~~86~~<br> | ~~0,290~~<br> | ~~18,4~~<br> | ~~0,27~~<br> |
| ~~25~~<br> | ~~105~~<br> | ~~0,354~~<br> | ~~28,8~~<br> | ~~0,42~~<br> |
| ~~100~~ | ~~135~~ | ~~0,461~~ | ~~51,4~~ | ~~0,75~~ |
| 200 | 152 | 0,526 | 67,7 | 0,99 |

<!-- Estadísticas: 4 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- DIA MINERA EL TURCO HIDROLOGIA Y CALCULO DE CAUDALES PAS 156 ESTERO ZÁRATE 16 -->
<!-- FIN TABLA 3.7 -->


Tabla 3.8: Caudales máximos para cuenca B, método de Verni y King. .................................................... 17

<!-- INICIO TABLA 3.8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- DIA MINERA EL TURCO HIDROLOGIA Y CALCULO DE CAUDALES PAS 156 ESTERO ZÁRATE 16 -->

**Tabla 3.8: Caudales máximos para cuenca B, método de Verni y King.****

| Período de<br>Retorno T<br>(años) | Pp Max 24<br>hr (mm) | C(T) | Q máx.<br>(m3/s) | Rendimiento<br>(m3/s/km2) |
| --- | --- | --- | --- | --- |
| ~~10~~<br> | ~~86~~<br> | ~~0,290~~<br> | ~~9,0~~<br> | ~~0,30~~<br> |
| ~~25~~<br> | ~~105~~<br> | ~~0,354~~<br> | ~~14,1~~<br> | ~~0,46~~<br> |
| ~~100~~ | ~~135~~ | ~~0,461~~ | ~~25,2~~ | ~~0,83~~ |
| 200 | 152 | 0,526 | 33,2 | 1,09 |

<!-- Estadísticas: 4 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- ### 3.4.3 Método DGA-AC En la Tabla 3.9 se detalla el cálculo para la estimación de los caudales máximos en la cuenca A, de acuerdo con el método DGA-AC. La Tabla 3.10 muestra la misma estimación, pero para la -->
<!-- FIN TABLA 3.8 -->


Tabla 3.9: Caudales máximos para cuenca A, método DGA-AC. .............................................................. 17

<!-- INICIO TABLA 3.9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la Tabla 3.9 se detalla el cálculo para la estimación de los caudales máximos en la cuenca A, de acuerdo con el método DGA-AC. La Tabla 3.10 muestra la misma estimación, pero para la cuenca B. -->

**Tabla 3.9: Caudales máximos para cuenca A, método DGA-AC.****

| Período de<br>Retorno T<br>(años) | Pp Max 24<br>hr (mm) | Q máx.<br>(m3/s) | Rendimiento<br>(m3/s/km2) |
| --- | --- | --- | --- |
| 10 | 86 | 21,0 | 0,31 |
| 25 | 105 | 39,0 | 0,57 |
| 100 | 135 | 83,2 | 1,22 |
| 200 | 152 | 88,2<br> | 1,29 |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 3.10: Caudales máximos para cuenca B, método DGA-AC.** |Período de<br>Retorno T<br>(años)|Pp Max 24<br>hr (mm)|Qmax<br>(m3/s)|Rendimiento<br>(m3/s/km2)| |---|---|---|---| -->
<!-- FIN TABLA 3.9 -->


Tabla 3.10: Caudales máximos para cuenca B, método DGA-AC. ............................................................ 17

<!-- INICIO TABLA 3.10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |10|86|21,0|0,31| |25|105|39,0|0,57| |100|135|83,2|1,22| |200|152|88,2<br>|1,29| -->

**Tabla 3.10: Caudales máximos para cuenca B, método DGA-AC.****

| Período de<br>Retorno T<br>(años) | Pp Max 24<br>hr (mm) | Qmax<br>(m3/s) | Rendimiento<br>(m3/s/km2) |
| --- | --- | --- | --- |
| 10 | 86 | 10,0 | 0,33 |
| 25 | 105 | 18,6 | 0,61 |
| 100 | 135 | 39,7 | 1,31 |
| 200 | 152 | 42,1 | 1,39 |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- DIA MINERA EL TURCO HIDROLOGIA Y CALCULO DE CAUDALES PAS 156 ESTERO ZÁRATE 17 -->
<!-- FIN TABLA 3.10 -->


Tabla 3.11: Resumen de los resultados obtenidos ..................................................................................... 18

<!-- INICIO TABLA 3.11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- ## 3.5 Res umen de resultados La Tabla 3.11 muestra un resumen de los resultados obtenidos. -->

**Tabla 3.11: Resumen de los resultados obtenidos****

| T | Método Racional Modificado | Col3 | Método Verni-King<br>Modificado | Col5 | Método DGA-AC | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **T ** | **Cuenca A** | **Cuenca B** | **Cuenca A** | **Cuenca B** | **Cuenca A** | **Cuenca B** |
| 10 | 14,7 | 6,6 | 18,4 | 9,0 | 21,0 | 10,0 |
| 25 | 22,8 | 9,8 | 28,8 | 14,1 | 39,0 | 18,6 |
| 100 | 35,8 | 16,5 | 51,4 | 25,2 | 83,2 | 39,7 |
| 200<br> | 47,0 | 21,2 | 67,7 | 33,2 | 88,2 | 42,1 |

<!-- Estadísticas: 5 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- La Tabla 3.12 muestra, para cada período de retorno, los caudales promediados de los 3 métodos para una de las cuencas. Se incluye además el rendimiento obtenido para cada caso. **Tabla 3.12: Caudales promediados para los 3 métodos de cálculo.** -->
<!-- FIN TABLA 3.11 -->


Tabla 3.12: Caudales promediados para los 3 métodos de cálculo. .......................................................... 18

<!-- INICIO TABLA 3.12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |200<br>|47,0|21,2|67,7|33,2|88,2|42,1| La Tabla 3.12 muestra, para cada período de retorno, los caudales promediados de los 3 métodos para una de las cuencas. Se incluye además el rendimiento obtenido para cada caso. -->

**Tabla 3.12: Caudales promediados para los 3 métodos de cálculo.****

| T | Cuenca A | Col3 | Cuenca B | Col5 |
| --- | --- | --- | --- | --- |
| **T ** | **Q prom (m3/s)** | **Rend. (m3/s/km2) ** | **Q prom (m3/s)** | **Rend. (m3/s/km2) ** |
| 10 | 18,0 | 0,26 | 8,6 | 0,28 |
| 25 | ~~30,2~~ | ~~0,44~~ | ~~14,2~~ | ~~0,47~~ |
| 100 | ~~56,8~~ | ~~0,83~~ | ~~27,1~~ | ~~0,89~~ |
| 200 | 67,6 | 0,99 | 32,2 | 1,06 |

<!-- Estadísticas: 5 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Los caudales mostrados anteriormente se han determinado bajo el supuesto de que no existe regulación de los embalses y que el 100% del área mostrada en la Figura 3.5 contribuye en su cálculo. -->
<!-- FIN TABLA 3.12 -->


Tabla 4.1: Superficies Aportantes Sub cuencas ......................................................................................... 21

<!-- INICIO TABLA 4.1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- PAS 156 ESTERO ZÁRATE 20 En la Tabla 4.1 se muestra las superficies aportantes de las sub cuencas que se encuentran aguas arriba y aguas abajo de los embalses, de acuerdo a la Figura 4.1. -->

**Tabla 4.1: Superficies Aportantes Sub cuencas****

| Cuenca | A (km2)<br>p | Sub-<br>cuenca | A (km2)<br>p | Observaciones |
| --- | --- | --- | --- | --- |
| **A ** | 68,20 | A1 | 17,75 | Aguas abajo Embalse - No regulado |
| **A ** | 68,20 | A2 | 50,45 | Aguas arriba Embalse - regulado |
| **B ** | 30,38 | B1 | 16,63 | Aguas abajo Embalse - No regulado |
| **B ** | 30,38 | B2 | 13,75 | Aguas arriba Embalse - regulado |

<!-- Estadísticas: 4 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Además para el presente análisis se asumieron las siguientes hipótesis: i. El caudal especifico de cada cuenca A y B, se mantienen para las subcuencas aguas arriba y agua abajo. -->
<!-- FIN TABLA 4.1 -->


Tabla 4.2: Caudales Aportantes Aguas Abajo de los Embalses T =25 años ............................................. 21

<!-- INICIO TABLA 4.2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Con los supuestos anteriormente señalados se determinaron los caudales aportantes de las cuencas A1 y B1, ambas aguas abajo de los embalses, las cuales se muestran en la Tabla 4.2 para T= 25 años período de retorno y Tabla 4.3 para T= 100 años -->

**Tabla 4.2: Caudales Aportantes Aguas Abajo de los Embalses T =25 años****

| Sub-cuenca | A (km2)<br>p | Rend.<br>(m3/s/km2) | Q (m3/s)<br>T= 25 años |
| --- | --- | --- | --- |
| A1 | 17,75 | 0,44 | ~~ 7,86~~<br> |
| B1 | 16,63 | 0,47 | ~~ 7.75~~<br> |
| Total (*)<br> | --- | ----- | ~~ 15,61~~ |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- DIA MINERA EL TURCO HIDROLOGIA Y CALCULO DE CAUDALES PAS 156 ESTERO ZÁRATE 21 -->
<!-- FIN TABLA 4.2 -->


Tabla 4.3: Caudales Aportantes Aguas Abajo de los Embalses. T= 100 años .......................................... 22

<!-- INICIO TABLA 4.3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- DIA MINERA EL TURCO HIDROLOGIA Y CALCULO DE CAUDALES PAS 156 ESTERO ZÁRATE 21 -->

**Tabla 4.3: Caudales Aportantes Aguas Abajo de los Embalses. T= 100 años****

| Sub-cuenca | A (km2)<br>p | Rend.<br>(m3/s/km2) | Q (m3/s)<br>T= 25 años |
| --- | --- | --- | --- |
| A1 | 17,75 | 0,83 | ~~ 14,79~~<br> |
| B1 | 16,63 | 0,89 | ~~ 14,84~~<br> |
| Total (*) | --- | ----- | ~~ 29,63~~ |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Para ambos casos se ha supuesto la condición más desfavorable al considerar que la superposición de los caudales es la suma de ambos peaks. Finalmente para la determinación de los caudales de diseño del nuevo badén, es necesario -->
<!-- FIN TABLA 4.3 -->


Tabla 4.4: Caudales de diseño para Badén T =25 años ............................................................................. 22

<!-- INICIO TABLA 4.4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- desfavorable de lluvia extrema y descarga del embalse en forma simultánea. En la Tabla 4.4 y Tabla 4.5 se muestran los resultados para los caudales de diseño para T= 25 y T= 100 años de período de retorno. -->

**Tabla 4.4: Caudales de diseño para Badén T =25 años****

| Sub-cuenca | Q (m3/s)<br>T= 25 años | Q base<br>(m3/s) | Q Diseño (m3/s)<br>T= 25 años |
| --- | --- | --- | --- |
| A1 | ~~7,86~~<br> | ~~5,00~~<br> | ~~ 12,86~~<br> |
| B1 | ~~7.75~~<br> | ~~0.75~~<br> | ~~ 8,50~~<br> |
| Total (*) | ~~15,61 ~~ | ~~5,75 ~~ | ~~**21,36**~~ |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 4.5: Caudales de diseño para Badén T =100 años** |Sub-cuenca|Q (m3/s)<br>T= 100 años|Q base<br>(m3/s)|Q Diseño (m3/s)<br>T= 100 años| |---|---|---|---| -->
<!-- FIN TABLA 4.4 -->


Tabla 4.5: Caudales de diseño para Badén T =100 años ........................................................................... 22

<!-- INICIO TABLA 4.5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---|---| |A1|~~7,86~~<br>|~~5,00~~<br>|~~ 12,86~~<br>| |B1|~~7.75~~<br>|~~0.75~~<br>|~~ 8,50~~<br>| |Total (*)|~~15,61 ~~|~~5,75 ~~|~~**21,36**~~| -->

**Tabla 4.5: Caudales de diseño para Badén T =100 años****

| Sub-cuenca | Q (m3/s)<br>T= 100 años | Q base<br>(m3/s) | Q Diseño (m3/s)<br>T= 100 años |
| --- | --- | --- | --- |
| A1 | ~~ 14,79~~<br> | ~~5,00~~<br> | ~~ 19,79~~<br> |
| B1 | ~~ 14,84~~<br> | ~~0.75~~<br> | ~~ 15,59~~<br> |
| Total (*) | ~~ 29,63~~ | ~~5,75 ~~ | ~~** 35,38**~~ |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- DIA MINERA EL TURCO HIDROLOGIA Y CALCULO DE CAUDALES PAS 156 ESTERO ZÁRATE 22 -->
<!-- FIN TABLA 4.5 -->


DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE

# LISTADO DE ANEXOS

A- Serie de Datos Estación Cerrillos de Leyda.

B- Gráficos con los ajustes.

C- Planos de Cuencas

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE

# 1 INTRODUCCIÓN Y OBJETIVOS

El presente documento tiene por objetivo desarrollar los cálculos de hidrología y determinación
de los caudales de diseño asociados al Estero Zárate y la obra de atravieso, en desarrollo
actualmente para presentar el permiso ambiental sectorial PAS 156 dentro del contexto de la
presentación de la DIA Minera El Turco.

En la presente memoria de Cálculo se entrega estudian los siguientes antecedentes:

Hidrología del área de estudio.

Determinación del caudal de diseño para T= 25 años para los tubos del badén y de T= 100
años para la verificación hidráulica y cálculos de socavación, en el punto de control asociado
a la obra de atravieso existente y la obra proyectada, del presente permiso ambiental
sectorial.

# 2 DETERMINACIÓN DE LA PRECIPITACIÓN MÁXIMA EN 24 HORAS

En el entorno del sitio del proyecto existen 3 estaciones meteorológicas de la DGA: la estación
Lagunillas, ubicada a aproximadamente 12 km al norte, la estación Cerrillos de Leyda, ubicada
9,5 km al sur, y la San Antonio (Punta Panul), que se ubica unos 12,5 km al oeste. La estación
Lagunillas dispone de registro desde al año 1986. Por otra parte, la estación Cerrillos de Leyda
presenta registros desde 1932; finalmente, la estación San Antonio mantiene estadísticas
continuas desde el año 1971.

Para verificar la consistencia de las mediciones de estas estaciones, se realizó una correlación
entre los 3 registros para el período concurrente en cada caso. Las Figuras 2.1, 2,2 y 2,3 muestran
el resultado de estas correlaciones.

**Figura 2.1: Correlación Est. Lagunillas y Est. San Antonio - Pp. máx en 24 hrs.**

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 5

Fuente: Elaboración propia.

**Figura 2.2: Correlación Est. Cerrillos de Leyda y Est. San Antonio - Pp. máx. en 24 hrs.**

**.**

**Figura 2.3: Correlación Est. Cerrillos de Leyda y Est. Lagunillas - Pp. máx. en 24 hrs.**

Como se aprecia en las figuras anteriores, las correlaciones entre las tres estaciones muestran
algún grado de dispersión, lo que indicaría que existen algunos efectos locales en la distribución
de la precipitación principalmente asociados a la orografía. Sin embargo, el rango de las
precipitaciones en las 3 estaciones es bastante similar, obteniéndose como factor de relación
entre ambas series valores en torno a 1.

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 6

Para efectos de cálculo de las precipitaciones, se considerará para el análisis la serie de datos
de la estación Cerrillos de Leyda, teniendo en cuenta su mayor cercanía con el sitio de estudio y
su mayor longitud de registro.
De la serie completa (1932 a 2016), se descartó el año 1969, dado que presenta un valor alejado
de la tendencia general de los registros (1 mm). Luego, a partir de estos 83 valores, se realizó un
análisis de frecuencia para determinar la precipitación máxima en 24 horas para un período de
retorno de 100 y 200 años. Se realizó un ajuste de la serie de datos con 5 distribuciones de
probabilidad (Normal, Log-Normal, Pearson III, Log-Pearson y Gumbel) de manera de identificar
aquella distribución que mejor se ajustaba al conjunto de los datos. Los resultados de este análisis
se muestran en forma resumida en la Tabla 2.1.

**Tabla 2.1: Resultados del análisis de frecuencia**

|Distribución de<br>probabilidad|Coeficiente<br>R2|Pp. Máx 24 Hrs<br>Tr=10|Pp. Máx 24<br>Hrs Tr=25|Pp. Máx 24 Hrs<br>Tr=100|Pp. Máx 24<br>Hrs Tr=200|
|---|---|---|---|---|---|
|~~Normal (*)~~|~~0,916~~|~~85~~|~~96~~<br>|~~108~~|~~114~~|
|Log Normal|0,982|85|~~101~~<br>|125|137|
|Peason III|0,981|86|~~102~~<br>|124|134|
|Log Pearson III|0,982|86|~~105~~<br>|135|152|
|Gumbel|0,981<br>|88<br>|~~106~~<br>|132|145|

Fuente: Elaboración propia.
(*) La distribución Normal no aprueba el test Chi-cuadrado

Como se observa, todas las distribuciones muestran un buen ajuste a la serie de datos de la
estación Cerrillos de Leyda. Luego, para definir el valor de la precipitación máxima en 24 horas
para un período de retorno de 100 años, se aplicó un criterio conservador, eligiéndose el valor
que entrega el ajuste de la distribución **Log Pearson III** . De esta forma, las precipitaciones para
diseño (T=10, T=25 y T=100 años) y verificación (T=200 años) son las mostradas en la Tabla 2.2
siguiente:

**Tabla 2.2: Precipitaciones de diseño y verificación**

|Período de retorno|Pp. Máx 24 Hrs|
|---|---|
|T=10|86|
|T=25|105|
|T=100|135|
|T=200<br>|152<br>|

Fuente: Elaboración propia.

En el Anexo A se incluye la serie de datos de la estación Cerrillos de Leyda y en el Anexo B los
gráficos con los ajustes para todas las distribuciones de probabilidad.

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 7

# 3 MÉTODOS DGA PARA CÁLCULO DE CRECIDAS EN CUENCAS SIN CONTROL

FLUVIOMÉTRICO

El documento “Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas sin Información
Fluviométrica” de la DGA (1995), propone 3 métodos empíricos para el cálculo directo del caudal
instantáneo máximo en cuencas sin control fluviométrico. Los métodos mencionados se detallan

a continuación.

## 3.1 MÉTODO RACIONAL MODIFICADO

La fórmula racional es ampliamente utilizada en hidrología por su simplicidad. En términos
generales, esta expresión relaciona, mediante un coeficiente de escorrentía empírico, el caudal
máximo instantáneo con el área pluvial de la cuenca y la intensidad de lluvia de la siguiente forma:

QQ= [CC∙ii∙AA] [p]
3,6

Dónde:

Q: Caudal máximo instantáneo de período de retorno T (m [3] /s)
C: coeficiente empírico para un período de retorno T
i: intensidad media de lluvia asociada al período de retorno T y a una duración igual
al tiempo de concentración de la cuenca pluvial (mm/hr)
A p : Área pluvial de la cuenca (km [2] )

De acuerdo a DGA (1995), el coeficiente de escorrentía se determina, en primera instancia, para
el período de retorno de 10 años (C(T=10)). Este parámetro depende de la ubicación geográfica
de la cuenca en estudio.
En este caso, se utilizará el correspondiente a la V Región, que es igual a **0,08** .

Para estimar el coeficiente de escorrentía para el resto de los períodos de retorno, aplican los
mismos valores estimados para el método de Verni y King, según DGA (1995). De esta forma, se
utiliza la misma relación C(T)/C(T=10) que se muestra más adelante en la Tabla 3.2.

Para el cálculo de la intensidad media de lluvia para una tormenta de duración igual al tiempo de
concentración, de acuerdo a la recomendación DGA (1995) se utilizarán los coeficientes de
duración propuestos por Varas y Sánchez (1983). Para la zona en estudio, se aplicarán los
coeficientes de duración para la estación Rapel, los se muestran en la Tabla 3.1.

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 8

**Tabla 3.1: Coeficientes de duración de Varas y Sánchez (1983) para estación Rapel**

|Duración (hr)|CD|
|---|---|
|1|0,15|
|2|0,23|
|4|0,34|
|6|0,47|
|8|0,56|
|10|0,64|
|12|0,71|
|14|0,79|
|18|0,91|
|24<br>|1,00<br>|

Fuente: Modificado de DGA (1995).

En la Figura 3.1 se presenta un ajuste logarítmico estimado a partir de los valores presentados
en la Tabla 3.1. Esta relación permitirá estimar los coeficientes de duración para un tiempo igual
al tiempo de concentración de cada cuenca en estudio.

**Figura 3.1: Extrapolación Coeficientes de duración de Varas y Sánchez (1983).**
**Estación Rapel.**

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 9

Para la estimación del tiempo de concentración de las cuencas existen diversas fórmulas. La
recomendación de DGA (1995) es utilizar la fórmula del California Highways and Public Works de
Estados Unidos:

##  L 3 ,0385

,095 ⋅  []  []

 ∆ _H_ 

##  L 3

_tc_ =,095 ⋅  []
∆ _H_

##  L 3 

 []  []
 ∆ _H_ 

Donde:

t c : Tiempo de concentración de la cuenca (h)
L : Longitud del cauce principal (km)
∆H : Desnivel máximo de la cuenca (m)

## 3.2 MÉTODO DE VERNI Y KING MODIFICADO

La fórmula de Verni y King original relaciona el caudal instantáneo máximo de una crecida con la
precipitación diaria máxima y el área pluvial a través de una relación de potencias. Esta fórmula
se modificó agregándole un coeficiente empírico variable con el período de retorno. La expresión
resultante tiene la siguiente forma:

QQ= CC(TT) ∙0,00618 ∙PP 241,24 ∙AA 0,88pp

Dónde:

Q: Caudal máximo instantáneo de período de retorno T (m [3] /s)
C(T): coeficiente empírico para un período de retorno T
A p : Área pluvial de la cuenca (km [2] )
P 24 : Precipitación diaria máxima de período de retorno T (mm)

Para el cálculo del coeficiente empírico C(T), en primer lugar se define su valor para un período
de retorno de 10 años, según la ubicación geográfica de la zona de estudio; luego, se utiliza la
curva de frecuencia para estimada para la misma zona.

En este caso, se utilizarán los valores estimados para la V Región. Para un período de retorno
de 10 años, **C(T) = 0,290** .

Dado que DGA (1995) sólo define el resto de los coeficientes hasta el período de retorno de 100
años, se realizó una extrapolación para el período de retorno de 200 años en base a los valores
estimados en el mencionado documento. La Figura 3.2 muestra gráficamente el resultado de esta
extrapolación. La Tabla 3.2 muestra los valores del coeficiente de frecuencia para distintos
períodos de retorno.

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 10

**Figura 3.2: Extrapolación de los coeficientes de frecuencia para V Región, método Verni y**
**King**

**Tabla 3.2: Coeficientes de frecuencia, método Verni y King para V Región**

|Período de<br>retorno<br>(años)|C(T)/C(T=10)|
|---|---|
|2|0,38|
|5|0,84|
|10|1,00|
|20|1,15|
|25|1,22|
|50|1,38|
|100|1,59|
|200<br>|1,81<br>|

Fuente: Modificado de DGA (1995). (*) Valor extrapolado.

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 11

## 3.3 MÉTODO DGA-AC

El método DGA-AC permite calcular los caudales máximos instantáneos a partir del caudal medio
diario máximo de período de retorno de 10 años (Q 10 ) y las curvas de frecuencia regionales del
mismo método.

El cálculo de Q 10 depende de la región en la que se ubique la cuenca. Para efectos de este
permiso, se utilizará aquella que maximiza el caudal, correspondiente al tramo comprendido entre
la V y VI región, incluyendo la RM:

QQ 10 = 5,42 ∙10 [−8] ∙AA 0,915pp ∙(PP 2410 ) 3,432
Dónde:

Q 10 : Caudal medio diario máximo de período de retorno de 10 años (m [3] /s)
A p : Área pluvial de la cuenca (km [2] )
P 24 [10] : Precipitación diaria máxima de período de retorno de 10 años (mm)

Para pasar del caudal medio diario máximo al caudal máximo instantáneo, se utiliza la siguiente
expresión:

QQ TT = αα∙CC FFTT ∙QQ 10
Dónde:

Q T : Caudal máximo instantáneo de período de retorno T (m [3] /s)
α: factor de conversión de acuerdo a zona homogénea
C F [T] : coeficiente de frecuencia para un período de retorno T
Q 10 : Caudal medio diario máximo de período de retorno de 10 años (m [3] /s)

Para el área de estudio, la zona homogénea que aplica corresponde a la denominada Np,
perteneciente a las cuencas entre Aconcagua y Rapel (32°S < latitud de la cuenca < 35°S). Aplica
esta zona homogénea dado la precipitación media es inferior a los 600 mm (416 mm) para el
período comprendido entre 1979 y 2016, como se aprecia en la Figura 3.3, la precipitación
máxima en 24 horas para un período de retorno de 10 años es mayor a 80 mm (86 mm, ver Tabla
2.2, y el área de las cuencas involucradas es menor a 145 km [2] (ver Tabla 3.4).

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 12

**Figura 3.3: Precipitación media anual de la estación Cerrillos de Leyda.**

La estimación de la precipitación media anual se realizó utilizando la serie mensual de la estación
para el período comprendido entre 1932 y 2017. De la totalidad de los registros para ese período,
se descartaron los años hidrológicos 1968/69, 1969/70, 1970/71 y 1976/77, por contar con menos
de 11 meses de información. La totalidad de los meses incluidos en el cálculo poseían, al menos,
20 días de información.

De esta forma, para esta zona homogénea, se concluye que el valor de α es **1,87** .

Respecto al coeficiente de frecuencia, dado que DGA (1995) sólo define sus valores hasta el
período de retorno de 100 años, se realizó una extrapolación para el período de retorno de 200
años en base a los valores estimados en el mencionado documento. La Figura 3.4 muestra
gráficamente el resultado de esta extrapolación. La Tabla 3.3 muestra los valores del coeficiente
de frecuencia para distintos períodos de retorno.

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 13

**Figura 3.4: Extrapolación de los coeficientes de frecuencia, método DGA-AC**

**Tabla 3.3: Coeficientes de frecuencia, método DGA-AC**

|Período de<br>retorno<br>(años)|C T<br>F|
|---|---|
|2|0,18|
|5|0,56|
|10|1,00|
|20|1,61|
|25|1,86|
|50|2,77|
|75|3,44|
|100|3,97|
|200<br>|4,21*<br>|

Fuente: Modificado de DGA (1995). (*) Valor extrapolado.

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 14

## 3.4 CÁLCULO DE CAUDALES MÁXIMOS INSTANTÁNEOS POR MÉTODO

La Tabla 3.4 muestra los resultados de la estimación de los parámetros morfométricos de las
cuencas en estudio, en tanto en el Anexo C se incluye como plano:

**Figura 3.5: Plano de Cuencas IGM**

Fuente: Elaboración propia en base a IGM

**Tabla 3.4: Parámetros morfométricos de las cuencas en estudio.**

|Cuenca|A (km2)<br>p|∆H (m)|L (km)|i (m/m)|t (hr)<br>c|
|---|---|---|---|---|---|
|A|68,20|847|18,918|0,045|2,11|
|B|30,38|197|11,272|0,017|2,04|

Es posible advertir que los tiempos de concentración son casi iguales, razón por la cual la
superposición de ambos caudales en un 100% es una condición conservadora pero realista.

Se detallan a continuación los resultados obtenidos con cada uno de los métodos de cálculo
descritos en los puntos anteriores y los parámetros morfométricos de las cuencas.

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 15

## 3.4.1 Método Racional Modificado

En la Tabla 3.5 se detalla el cálculo para la estimación de los caudales máximos en la cuenca A,
de acuerdo con el método racional modificado. La Tabla 3.6 muestra la misma estimación, pero
para la cuenca B.

**Tabla 3.5: Caudales máximos para cuenca A, método racional modificado.**

|Período<br>de<br>Retorno T<br>(años)|Pp Max<br>24 hr<br>(mm)|C(T)|T (hr)<br>C|CD|Intensidad<br>Tc (mm/hr)|Q máx. (m3/s)|Rendimiento<br>(m3/s/km2)|
|---|---|---|---|---|---|---|---|
|~~10~~<br>|~~86~~<br>|~~0,080~~<br>|~~2,11~~<br>|~~0,238~~<br>|~~10~~<br>|~~14,7~~<br>|~~0,22~~<br>|
|~~25~~<br>|~~105~~<br>|~~0,098~~<br>|~~2,11~~<br>|~~0,238~~<br>|~~12~~<br>|~~22,8~~<br>|~~0,33~~<br>|
|~~100~~|~~135~~|~~0,127~~|~~2,11~~|~~0,238~~|~~15~~|~~35,8~~|~~0,53~~|
|200<br>|152|0,145|2,11|0,238|17|47,0|0,69|

**Tabla 3.6: Caudales máximos para cuenca B, método racional modificado.**

|Período<br>de<br>Retorno T<br>(años)|Pp Max<br>24 hr<br>(mm)|C(T)|T (hr)<br>C|CD|Intensidad<br>Tc (mm/hr)|Q máx. (m3/s)|Rendimiento<br>(m3/s/km2)|
|---|---|---|---|---|---|---|---|
|~~10~~<br>|~~86~~<br>|~~0,080~~<br>|~~2,04~~<br>|~~0,233~~<br>|~~10~~<br>|~~6,6~~<br>|~~0,22~~<br>|
|~~25~~<br>|~~105~~<br>|~~0,098~~<br>|~~2,04~~<br>|~~0,233~~<br>|~~12~~<br>|~~9,8~~<br>|~~0,32~~<br>|
|~~100~~|~~135~~|~~0,127~~|~~2,04~~|~~0,233~~|~~15~~|~~16,5~~|~~0,54~~|
|200<br>|152|0,145|2,04|0,233|17|21,2|0,70|

### 3.4.2 Método Verni y King

En la Tabla 3.7 se detalla el cálculo para la estimación de los caudales máximos en la cuenca A,
de acuerdo con el método de Verni y King. La Tabla 3.8 muestra la misma estimación, pero para
la cuenca B.

**Tabla 3.7: Caudales máximos para cuenca A, método de Verni y King.**

|Período de<br>Retorno T<br>(años)|Pp Max 24<br>hr (mm)|C(T)|Q máx.<br>(m3/s)|Rendimiento<br>(m3/s/km2)|
|---|---|---|---|---|
|~~10~~<br>|~~86~~<br>|~~0,290~~<br>|~~18,4~~<br>|~~0,27~~<br>|
|~~25~~<br>|~~105~~<br>|~~0,354~~<br>|~~28,8~~<br>|~~0,42~~<br>|
|~~100~~|~~135~~|~~0,461~~|~~51,4~~|~~0,75~~|
|200|152|0,526|67,7|0,99|

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 16

**Tabla 3.8: Caudales máximos para cuenca B, método de Verni y King.**

|Período de<br>Retorno T<br>(años)|Pp Max 24<br>hr (mm)|C(T)|Q máx.<br>(m3/s)|Rendimiento<br>(m3/s/km2)|
|---|---|---|---|---|
|~~10~~<br>|~~86~~<br>|~~0,290~~<br>|~~9,0~~<br>|~~0,30~~<br>|
|~~25~~<br>|~~105~~<br>|~~0,354~~<br>|~~14,1~~<br>|~~0,46~~<br>|
|~~100~~|~~135~~|~~0,461~~|~~25,2~~|~~0,83~~|
|200|152|0,526|33,2|1,09|

### 3.4.3 Método DGA-AC

En la Tabla 3.9 se detalla el cálculo para la estimación de los caudales máximos en la cuenca A,
de acuerdo con el método DGA-AC. La Tabla 3.10 muestra la misma estimación, pero para la
cuenca B.

**Tabla 3.9: Caudales máximos para cuenca A, método DGA-AC.**

|Período de<br>Retorno T<br>(años)|Pp Max 24<br>hr (mm)|Q máx.<br>(m3/s)|Rendimiento<br>(m3/s/km2)|
|---|---|---|---|
|10|86|21,0|0,31|
|25|105|39,0|0,57|
|100|135|83,2|1,22|
|200|152|88,2<br>|1,29|

**Tabla 3.10: Caudales máximos para cuenca B, método DGA-AC.**

|Período de<br>Retorno T<br>(años)|Pp Max 24<br>hr (mm)|Qmax<br>(m3/s)|Rendimiento<br>(m3/s/km2)|
|---|---|---|---|
|10|86|10,0|0,33|
|25|105|18,6|0,61|
|100|135|39,7|1,31|
|200|152|42,1|1,39|

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 17

## 3.5 Res umen de resultados

La Tabla 3.11 muestra un resumen de los resultados obtenidos.

**Tabla 3.11: Resumen de los resultados obtenidos**

|T|Método Racional Modificado|Col3|Método Verni-King<br>Modificado|Col5|Método DGA-AC|Col7|
|---|---|---|---|---|---|---|
|**T **|**Cuenca A**|**Cuenca B**|**Cuenca A**|**Cuenca B**|**Cuenca A**|**Cuenca B**|
|10|14,7|6,6|18,4|9,0|21,0|10,0|
|25|22,8|9,8|28,8|14,1|39,0|18,6|
|100|35,8|16,5|51,4|25,2|83,2|39,7|
|200<br>|47,0|21,2|67,7|33,2|88,2|42,1|

La Tabla 3.12 muestra, para cada período de retorno, los caudales promediados de los 3 métodos
para una de las cuencas. Se incluye además el rendimiento obtenido para cada caso.

**Tabla 3.12: Caudales promediados para los 3 métodos de cálculo.**

|T|Cuenca A|Col3|Cuenca B|Col5|
|---|---|---|---|---|
|**T **|**Q prom (m3/s)**|**Rend. (m3/s/km2) **|**Q prom (m3/s)**|**Rend. (m3/s/km2) **|
|10|18,0|0,26|8,6|0,28|
|25|~~30,2~~|~~0,44~~|~~14,2~~|~~0,47~~|
|100|~~56,8~~|~~0,83~~|~~27,1~~|~~0,89~~|
|200|67,6|0,99|32,2|1,06|

Los caudales mostrados anteriormente se han determinado bajo el supuesto de que no existe
regulación de los embalses y que el 100% del área mostrada en la Figura 3.5 contribuye en su
cálculo.

No obstante, habiendo recorrido el terreno y sus esteros, se ve poco probable que éstos puedan
ser capaces de portear 80 m3/s como se muestra en la tabla anterior.

A modo de ejemplo, en la Figura 3.6 se muestra una fotografía del estero La Viña,
aproximadamente 1 km aguas abajo del Embalse las Palmas I, que se muestra en la Figura 3.5
de las cuencas IGM,

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 18

**Figura 3.6: Fotografía Estero La Viña Aguas Abajo Embalse Las Palmas I**

Fuente: Elaboración Propia

En la fotografía anterior se muestra que la sección del estero La Viña no supera un ancho
superficial de 4 m y una altura de 2 m, que en términos generales podría portear un caudal
comprendido entre 12 m3/s a 20 m3/s, y no 50 m3/s como se deduce del análisis hidrológico
efectuado en anteriormente, que utiliza la cuenca completa como superficie aportante y no
considera el efecto de regulación de los embalses.

En el siguiente capítulo se hace un análisis de la influencia de ambos embalses de manera de
determinar un caudal que realmente sea capaz de portear por el estero Zárate para el diseño del
badén proyectado.

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 19

# 4 REGULACION DE EMBALSES

Tal como se mencionó anteriormente, a presencia de dos embalses en la zona de la influencia
del área aportante, ponen de manifiesto la necesidad de revisar la regulación de éstos ante
crecidas extremas.

Los Embalses Las Palmas I y II, son de propiedad privada del Fundo Las Palmas y en
conversación telefónica con uno de sus propietarios, se indicó los siguientes antecedentes
referenciales que permiten ser utilizados en el presente análisis:

a) Ambos embalses datan de los años 1950 aproximadamente.
b) Ambos embalses han regulado las crecidas que han ocurrido en el período.
c) La capacidad de almacenamiento de ambos embalses es aproximadamente 575.000 m3.

En base al hecho que efectivamente ambos embalses regulan las crecidas, se procedió a
subdividir las áreas aportantes aguas abajo de los embalses (A1 y B1) y las áreas aportantes
aguas arriba de ambos embalse y que por ende las crecidas son reguladas por ellos (A2 y B2).

En la Figura 4.1 se muestra las cuencas A y B subdivididas en las subcuencas aguas abajo (A1
y B1) y las subcuencas aguas arriba de ambos embalses (A2 y B2), en tanto que en el Anexo C
se incluye como plano.

**Figura 4.1: Plano de Sub-cuencas IGM con Regulación de Embalse**

Fuente: Elaboración propia en base a IGM

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 20

En la Tabla 4.1 se muestra las superficies aportantes de las sub cuencas que se encuentran
aguas arriba y aguas abajo de los embalses, de acuerdo a la Figura 4.1.

**Tabla 4.1: Superficies Aportantes Sub cuencas**

|Cuenca|A (km2)<br>p|Sub-<br>cuenca|A (km2)<br>p|Observaciones|
|---|---|---|---|---|
|**A **|68,20|A1|17,75|Aguas abajo Embalse - No regulado|
|**A **|68,20|A2|50,45|Aguas arriba Embalse - regulado|
|**B **|30,38|B1|16,63|Aguas abajo Embalse - No regulado|
|**B **|30,38|B2|13,75|Aguas arriba Embalse - regulado|

Además para el presente análisis se asumieron las siguientes hipótesis:

i. El caudal especifico de cada cuenca A y B, se mantienen para las subcuencas
aguas arriba y agua abajo.

ii. Se asume que ambos embalses tiene un caudal base que se mantendrá durante
los eventos de crecidas extremas.

iii. Bajo esta condición se ha supuesto la siguiente distribución de caudales en función
de la capacidad de almacenamiento de cada embalse:

 - Caudal Base Embalse Las Palmas I = 5 m3/s

 - Caudal Base Embalse Las Palmas II = 0,75 m3/s.

Con los supuestos anteriormente señalados se determinaron los caudales aportantes de las
cuencas A1 y B1, ambas aguas abajo de los embalses, las cuales se muestran en la Tabla 4.2
para T= 25 años período de retorno y Tabla 4.3 para T= 100 años

**Tabla 4.2: Caudales Aportantes Aguas Abajo de los Embalses T =25 años**

|Sub-cuenca|A (km2)<br>p|Rend.<br>(m3/s/km2)|Q (m3/s)<br>T= 25 años|
|---|---|---|---|
|A1|17,75|0,44|~~ 7,86~~<br>|
|B1|16,63|0,47|~~ 7.75~~<br>|
|Total (*)<br>|---|-----|~~ 15,61~~|

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 21

**Tabla 4.3: Caudales Aportantes Aguas Abajo de los Embalses. T= 100 años**

|Sub-cuenca|A (km2)<br>p|Rend.<br>(m3/s/km2)|Q (m3/s)<br>T= 25 años|
|---|---|---|---|
|A1|17,75|0,83|~~ 14,79~~<br>|
|B1|16,63|0,89|~~ 14,84~~<br>|
|Total (*)|---|-----|~~ 29,63~~|

Para ambos casos se ha supuesto la condición más desfavorable al considerar que la
superposición de los caudales es la suma de ambos peaks.

Finalmente para la determinación de los caudales de diseño del nuevo badén, es necesario
incorporar los caudales bases aportantes de ambos embalses, asumiendo la condición más
desfavorable de lluvia extrema y descarga del embalse en forma simultánea.

En la Tabla 4.4 y Tabla 4.5 se muestran los resultados para los caudales de diseño para T= 25 y
T= 100 años de período de retorno.

**Tabla 4.4: Caudales de diseño para Badén T =25 años**

|Sub-cuenca|Q (m3/s)<br>T= 25 años|Q base<br>(m3/s)|Q Diseño (m3/s)<br>T= 25 años|
|---|---|---|---|
|A1|~~7,86~~<br>|~~5,00~~<br>|~~ 12,86~~<br>|
|B1|~~7.75~~<br>|~~0.75~~<br>|~~ 8,50~~<br>|
|Total (*)|~~15,61 ~~|~~5,75 ~~|~~**21,36**~~|

**Tabla 4.5: Caudales de diseño para Badén T =100 años**

|Sub-cuenca|Q (m3/s)<br>T= 100 años|Q base<br>(m3/s)|Q Diseño (m3/s)<br>T= 100 años|
|---|---|---|---|
|A1|~~ 14,79~~<br>|~~5,00~~<br>|~~ 19,79~~<br>|
|B1|~~ 14,84~~<br>|~~0.75~~<br>|~~ 15,59~~<br>|
|Total (*)|~~ 29,63~~|~~5,75 ~~|~~** 35,38**~~|

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 22

# 5 CONCLUSIONES Y RECOMENDACIONES

 De la visita a terreno fue posible corroborar que la capacidad de los esteros está por muy
debajo de los caudales de ambas cuencas por separado y que inevitablemente el efecto
de regulación de los embalses existe.

 - La existencia de ambos embalses permiten amortiguar crecidas ante lluvias extremas, en
este informe se han supuesto antecedentes que deberán ser validados cuando se
disponga de información explicita del funcionamiento de ambos embalses.

 Antecedentes de la operación del Embalse y capacidad de regulación deben ser
gestionados con los propietarios de ambos embalses para una siguiente etapa de
permisos sectoriales.

 Aun cuando se hicieron cálculos con hipótesis para determinar los caudales de diseño, es
un hecho que el caudal para T=100 años período de retorno, en el tramo analizado en la
memoria de cálculo hidráulica (doc. N° OT9588-HI-C-CAL-002), está al límite real de la
capacidad del estero Zárate en el área del proyecto.

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 23

**ANEXOS**

D- Serie de Datos Estación Cerrillos de Leyda.

E- Gráficos con los ajustes.

F- Planos de Cuencas

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 24

**A- REGISTROS ESTACIÓN CERRILLOS DE LEYDA**

|Año|Fecha|Precipitación en 24 hrs.<br>(mm)|Año|Fecha|Precipitación en 24 hrs.<br>(mm)|
|---|---|---|---|---|---|
|~~1932~~ <br>|~~24/07~~ <br>|~~61,5~~ <br>|~~1975~~ <br>|~~14/11~~ <br>|~~29~~ <br>|
|~~1933~~ <br>|~~13/01~~ <br>|~~57~~ <br>|~~1976~~ <br>|~~02/10~~ <br>|~~46~~ <br>|
|~~1934~~ <br>|~~16/05~~ <br>|~~52~~ <br>|~~1977~~ <br>|~~22/07~~ <br>|~~50~~ <br>|
|~~1935~~ <br>|~~07/07~~ <br>|~~34~~ <br>|~~1978~~ <br>|~~20/07~~ <br>|~~44~~ <br>|
|~~1936~~ <br>|~~23/05~~ <br>|~~47~~ <br>|~~1979~~ <br>|~~25/07~~ <br>|~~69~~ <br>|
|~~1937~~ <br>|~~23/06~~ <br>|~~55~~ <br>|~~1980~~ <br>|~~09/05~~ <br>|~~108~~ <br>|
|~~1938~~ <br>|~~08/03~~ <br>|~~35~~ <br>|~~1981~~ <br>|~~11/05~~ <br>|~~94~~ <br>|
|~~1939~~ <br>|~~08/08~~ <br>|~~54~~ <br>|~~1982~~ <br>|~~08/05~~ <br>|~~71~~ <br>|
|~~1940~~ <br>|~~12/07~~ <br>|~~124~~ <br>|~~1983~~ <br>|~~20/06~~ <br>|~~67.5~~ <br>|
|~~1941~~ <br>|~~07/05~~ <br>|~~75~~ <br>|~~1984~~ <br>|~~04/07~~ <br>|~~85.5~~ <br>|
|~~1942~~ <br>|~~14/07~~ <br>|~~44~~ <br>|~~1985~~ <br>|~~28/07~~ <br>|~~49~~ <br>|
|~~1943~~ <br>|~~20/05~~ <br>|~~43~~ <br>|~~1986~~ <br>|~~26/05~~ <br>|~~73~~ <br>|
|~~1944~~ <br>|~~07/08~~ <br>|~~50~~ <br>|~~1987~~ <br>|~~13/07~~ <br>|~~84~~ <br>|
|~~1945~~ <br>|~~03/02~~ <br>|~~49~~ <br>|~~1988~~ <br>|~~18/08~~ <br>|~~37.1~~ <br>|
|~~1946~~ <br>|~~08/07~~ <br>|~~27~~ <br>|~~1989~~ <br>|~~25/07~~ <br>|~~44.5~~ <br>|
|~~1947~~ <br>|~~15/07~~ <br>|~~40~~ <br>|~~1990~~ <br>|~~16/07~~ <br>|~~48.2~~ <br>|
|~~1948~~ <br>|~~10/07~~ <br>|~~40~~ <br>|~~1991~~ <br>|~~19/06~~ <br>|~~46~~ <br>|
|~~1949~~ <br>|~~18/05~~ <br>|~~45~~ <br>|~~1992~~ <br>|~~06/05~~ <br>|~~122~~ <br>|
|~~1950~~ <br>|~~05/04~~ <br>|~~35~~ <br>|~~1993~~ <br>|~~16/04~~ <br>|~~44.4~~ <br>|
|~~1951~~ <br>|~~18/07~~ <br>|~~74~~ <br>|~~1994~~ <br>|~~26/04~~ <br>|~~45~~ <br>|
|~~1952~~ <br>|~~22/06~~ <br>|~~84~~ <br>|~~1995~~ <br>|~~04/07~~ <br>|~~34.6~~ <br>|
|~~1953~~ <br>|~~19/08~~ <br>|~~78~~ <br>|~~1996~~ <br>|~~06/07~~ <br>|~~38~~ <br>|
|~~1954~~ <br>|~~04/07~~ <br>|~~29~~ <br>|~~1997~~ <br>|~~03/06~~ <br>|~~77~~ <br>|
|~~1955~~ <br>|~~16/05~~ <br>|~~41~~ <br>|~~1998~~ <br>|~~22/05~~ <br>|~~11.5~~ <br>|
|~~1956~~ <br>|~~19/08~~ <br>|~~72~~ <br>|~~1999~~ <br>|~~07/09~~ <br>|~~31.1~~ <br>|
|~~1957~~ <br>|~~19/05~~ <br>|~~75~~ <br>|~~2000~~ <br>|~~13/06~~ <br>|~~79.5~~ <br>|
|~~1958~~ <br>|~~07/05~~ <br>|~~58~~ <br>|~~2001~~ <br>|~~29/07~~ <br>|~~100.5~~ <br>|
|~~1959~~ <br>|~~18/04~~ <br>|~~30~~ <br>|~~2002~~ <br>|~~24/05~~ <br>|~~84.8~~ <br>|
|~~1960~~ <br>|~~20/06~~ <br>|~~50~~ <br>|~~2003~~ <br>|~~20/05~~ <br>|~~86.2~~ <br>|
|~~1961~~ <br>|~~02/06~~ <br>|~~34~~ <br>|~~2004~~ <br>|~~12/11~~ <br>|~~41.6~~ <br>|
|~~1962~~ <br>|~~13/08~~ <br>|~~43~~ <br>|~~2005~~ <br>|~~27/06~~ <br>|~~54.4~~ <br>|
|~~1963~~ <br>|~~21/05~~ <br>|~~44~~ <br>|~~2006~~ <br>|~~07/06~~ <br>|~~78.5~~ <br>|
|~~1964~~ <br>|~~15/08~~ <br>|~~37~~ <br>|~~2007~~ <br>|~~08/08~~ <br>|~~36.1~~ <br>|
|~~1965~~ <br>|~~23/07~~ <br>|~~75~~ <br>|~~2008~~ <br>|~~20/05~~ <br>|~~78.2~~ <br>|
|~~1966~~ <br>|~~09/06~~ <br>|~~30~~ <br>|~~2009~~ <br>|~~15/08~~ <br>|~~54.1~~ <br>|
|~~1967~~ <br>|~~15/07~~ <br>|~~48~~ <br>|~~2010~~ <br>|~~13/06~~ <br>|~~41.6~~ <br>|
|~~1968~~ <br>|~~16/08~~ <br>|~~27~~ <br>|~~2011~~ <br>|~~18/06~~ <br>|~~35.9~~ <br>|
|~~1969~~ <br>|~~09/12~~ <br>|~~1~~ <br>|~~2012~~ <br>|~~26/05~~ <br>|~~89.2~~ <br>|
|~~1970~~ <br>|~~14/07~~ <br>|~~42~~ <br>|~~2013~~<br>|~~27/05~~<br>|~~97.9~~<br>|
|~~1971~~ <br>|~~20/06~~ <br>|~~56~~ <br>|~~2014~~<br>|~~11/06~~<br>|~~50.2~~<br>|
|~~1972~~ <br>|~~04/07~~ <br>|~~48~~ <br>|~~2015~~<br>|~~06/08~~<br>|~~43.6~~<br>|
|~~1973~~ <br>|~~14/06~~ <br>|~~66~~ <br>|~~2016~~<br>|~~24/07~~<br>|~~43.5~~<br>|
|~~1974~~ <br>|~~18/05~~|~~67~~||||

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 25

**B- RESULTADOS ANÁLISIS DE FRECUENCIAS**

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 26

DIA MINERA EL TURCO
HIDROLOGIA Y CALCULO DE CAUDALES
PAS 156 ESTERO ZÁRATE 27