---
title: Sin título
author: Camila Villanueva
date: D:20231209105859-03'00'
language: es
type: general
pages: 12
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Adenda de Declaración de Impacto Ambiental “Adecuación Cronograma y Obras Collahuasi” Anexo 2.1 Memo Cambio Climático
-->

# Adenda de Declaración de Impacto Ambiental “Adecuación Cronograma y Obras Collahuasi” Anexo 2.1 Memo Cambio Climático

## Elaborado por: Diciembre, 2023

P-5315 MEMORANDUM TÉCNICO Apoyo tramitación Adenda, Simulaciones Cambio

Climático

**1** **INTRODUCCIÓN**

Arcadis se encuentra dando soporte y apoyo técnico a CMDIC en lo referente a las
consultas generadas en el ICSARA de la DIA “Adecuación cronograma y obras Collahuasi”
para la elaboración de la Adenda 1 respectiva. En este marco, se elaboró este memorando
técnico referente a las simulaciones con cambio climático, las que se efectúan en el marco
de la nueva guía del SEA “Criterio de evaluación en el SEIA: Cambio climático en la
evaluación ambiental del recurso hídrico” publicada en noviembre del año 2023.

**2** **DESCRIPCIÓN DEL ESCENARIO DE CAMBIO CLIMATICO.**

Para la actualización de la estimación de recarga por precipitaciones y su proyección a
futuro en el marco de la DIA en tramitación, se utilizó el modelo hidrológico construido
durante el EIA “Desarrollo de Infraestructura y Mejoramiento de Capacidad Productiva de
Collahuasi” (CMDIC, 2019), la Guía Metodológica para la Consideración del Cambio
Climático en el SEIA, segunda edición (SEA, 2023) y la actualización del documento
“Criterio de evaluación en el SEIA: Cambio climático en la evaluación ambiental del recurso
hídrico” publicada en noviembre del año 2023, que establece una metodología para
proyectar los cambios de precipitación y temperatura producto del cambio climático.

El modelo hidrológico utiliza como forzantes meteorológicas información pública de
precipitación, temperatura y evaporación de tanque (principalmente estaciones
meteorológicas DGA como Ujina, Collacagua y Copaquire), que se complementaron con
registros propios de CMDIC por la falta de registros públicos durante los últimos años. Para
el caso de la simulación y proyección del aporte de las precipitaciones al acuífero de las
subcuencas Vertiente Pacífico (SVP) del sector de Rosario, la falta de registros
meteorológicos dificulta una actualización robusta del funcionamiento hidrológico del
sistema por lo que, para definir el escenario hídrico futuro, se asumió el mismo
comportamiento que para la cuenca del salar de Michincha.

El período histórico para la evaluación y análisis hidrológico quedó definido entre enero de
1981 y diciembre de 2020, periodo en el que se observan valores de precipitación de 143
mm/año, una temperatura media diaria de 3,6°C y una evaporación potencial de 4,1
mm/día.

Para proyectar a futuro estas forzantes, se utilizó la guía desarrollada por el SEA (2023),
con lo que, para el área de estudio, se estima una disminución de 11,6% de las
precipitaciones medias y un aumento de 1,4°C en la temperatura media. Para transformar
el aumento de temperatura medio en aumento de evaporación potencial, se utilizó la
ecuación de Hargreaves, estimándose así un aumento de evaporación potencial de 6,57%
respecto a la serie histórica estimada.

Considerando los supuestos anteriores, se obtuvieron valores de recarga para el período
futuro de 533 L/s para la cuenca de Coposa y de 165 L/s para Michincha. Esto equivale, en
Coposa, a una disminución del 17.1% respecto al período de simulación del modelo
hidrogeológico (643 l/s) y de 16,4 % en Michincha (198 l/s). Aplicando la misma disminución
de recarga respecto al período de modelación para SVP, se obtiene un aporte desde las
precipitaciones al acuífero de 118 L/s, en contraste con los 142 l/s del periodo de simulación
del modelo hidrogeológico.

Referencia: Página: 2/12
5315-2000-RH-MMT-003

P-5315 MEMORANDUM TÉCNICO Apoyo tramitación Adenda, Simulaciones Cambio

Climático

**3** **IMPLEMENTACIÓN DE LAS CONDICIONES DE BORDE EN EL MODELO**
**NUMÉRICO.**

Los cambios en los parámetros hidrológicos asociados al cambio climático repercuten en la
condición de borde de Recarga superficial dado por la precipitación y en la evaporación
potencial, dado por el aumento en la temperatura. Se generó una nueva serie de recarga
para el periodo de evaluación del proyecto y una nueva serie de evaporación potencial para
las cuencas de Coposa y Michincha, las que fueron incorporadas al modelo numérico a
partir del año 2023.

3.1 RECARGA NATURAL POR PRECIPITACIÓN

La recarga natural por precipitación obtenida desde el modelo hidrológico fue incorporada
al modelo numérico mediante la condición de borde RCH de MODFLOW USG, siguiendo
la misma metodología utilizada en el modelo presentado en la DIA, variando solamente su
magnitud a partir del año 2023, dando cuenta del periodo donde inicia el proyecto a evaluar.
La recarga utilizada en la cuenca de Coposa para el periodo de evaluación del proyecto es
constante, según el valor indicado en la Tabla 1 y presentado gráficamente como una serie
de tiempo en el Gráfico 1 .

**Tabla 1: Evaporación potencial trimestral por sector (mm/día)**

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- magnitud a partir del año 2023, dando cuenta del periodo donde inicia el proyecto a evaluar. La recarga utilizada en la cuenca de Coposa para el periodo de evaluación del proyecto es constante, según el valor indicado en la Tabla 1 y presentado gráficamente como una serie de tiempo en el Gráfico 1 . -->

**Tabla 1: Evaporación potencial trimestral por sector (mm/día)****

| Periodo | Pp (mm/año) | T (°C) | Ev (mm/d) | Recarga (m3/s) |
| --- | --- | --- | --- | --- |
| **Periodo** | **Coposa** | **Coposa** | **Coposa** | **Coposa** |
| 1993 a 2020 | 134 | 3,58 | 4,13 | 0,632 |
| 2023 a 2100 | 126,2 | 5 | 4,4 | 0,533 |

<!-- Estadísticas: 3 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Arcadis, 2023. . -->
<!-- FIN TABLA 1 -->


|Periodo|Pp (mm/año)|T (°C)|Ev (mm/d)|Recarga (m3/s)|
|---|---|---|---|---|
|**Periodo**|**Coposa**|**Coposa**|**Coposa**|**Coposa**|
|1993 a 2020|134|3,58|4,13|0,632|
|2023 a 2100|126,2|5|4,4|0,533|

Fuente: Arcadis, 2023.

.

Referencia: Página: 3/12
5315-2000-RH-MMT-003

P-5315 MEMORANDUM TÉCNICO Apoyo tramitación Adenda, Simulaciones Cambio

Climático

**Gráfico 1: Variación temporal de la recarga impuesta en el modelo en la cuenca de Coposa.**

Fuente: Arcadis, 2023.
3.2 EVAPORACIÓN DESDE AGUAS SUBTERRÁNEAS

La evaporación desde aguas subterráneas fue modificada solamente en su magnitud con
respecto a lo presentado previamente en el modelo DIA. Los valores implementados en
esta modelación, correspondiente al incremento de temperatura dado por el cambio
climático se presentan en la Tabla 2.

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La evaporación desde aguas subterráneas fue modificada solamente en su magnitud con respecto a lo presentado previamente en el modelo DIA. Los valores implementados en esta modelación, correspondiente al incremento de temperatura dado por el cambio climático se presentan en la Tabla 2. -->

**Tabla 2: Evaporación potencial trimestral por sector (mm/día)****

| Periodo | Michincha | Coposa |
| --- | --- | --- |
| Permanente (anual) | 4,476 | 4,689 |
| Enero-Marzo | 4,870 | 5,296 |
| Abril-Junio | 3,304 | 3,378 |
| Julio-Septiembre | 3,698 | 3,868 |
| Octubre-Diciembre | 5,787 | 6,074 |

<!-- Estadísticas: 5 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Arcadis, 2023. 3.3 RESULTADOS -->
<!-- FIN TABLA 2 -->


**Tabla 2: Evaporación potencial trimestral por sector (mm/día)**

|Periodo|Michincha|Coposa|
|---|---|---|
|Permanente (anual)|4,476|4,689|
|Enero-Marzo|4,870|5,296|
|Abril-Junio|3,304|3,378|
|Julio-Septiembre|3,698|3,868|
|Octubre-Diciembre|5,787|6,074|

Fuente: Arcadis, 2023.

3.3 RESULTADOS

Se presenta la comparación de resultados obtenidos entre los casos evaluados (casos Base
y Proyecto) considerando cambio climático.

**3.3.1 Hidrogramas de niveles subterráneos y afloramiento vertiente Jachucoposa**

A continuación, se presentan la evolución temporal de los niveles de agua subterránea en
siete pozos seleccionados (ver Figura 1 **)** y el caudal aflorado en la vertiente Jachucoposa,
con el fin de mostrar cualitativamente la respuesta del modelo en la cuenca de Coposa ante
los cambios efectuados debido a la implementación de una recarga que considera el cambio
climático.

Referencia: Página: 4/12
5315-2000-RH-MMT-003

P-5315 MEMORANDUM TÉCNICO Apoyo tramitación Adenda, Simulaciones Cambio

Climático

En términos generales, tanto el comportamiento del nivel subterráneo como el caudal
aflorado en la vertiente Jachucoposa se mantienen por debajo de las simulaciones
realizadas en el caso Base y el Proyecto sin cambio climático. Esto era de esperarse debido
a la menor recarga asociada y al aumento de la evaporación. No obstante, es importante
destacar que persisten las tendencias presentadas en la Declaración de Impacto Ambiental
(DIA), es decir, los niveles y caudales del Caso Proyecto siguen estando por encima de lo
simulado para el caso Base.

Referencia: Página: 5/12
5315-2000-RH-MMT-003

P-5315 MEMORANDUM TÉCNICO Apoyo tramitación Adenda, Simulaciones Cambio

Climático

**Figura 1: Localización geográfica de pozos monitoreo**

Fuente: Arcadis, 2023

Referencia: Página: 6/12
5315-2000-RH-MMT-003

P-5315 MEMORANDUM TÉCNICO Apoyo tramitación Adenda, Simulaciones Cambio

Climático

**Gráfico 2: Evolución temporal de niveles pozo DPEC-04 simulación.**

Fuente: Arcadis, 2023.

**Gráfico 3: Evolución temporal de niveles pozo PPS-02B simulación.**

Fuente: Arcadis, 2023.

Referencia: Página: 7/12
5315-2000-RH-MMT-003

P-5315 MEMORANDUM TÉCNICO Apoyo tramitación Adenda, Simulaciones Cambio

Climático

**Gráfico 4: Evolución temporal de niveles pozo PC-04 simulación.**

Fuente: Arcadis, 2023.

**Gráfico 5: Evolución temporal de niveles pozo CWE-05 simulación.**

Fuente: Arcadis, 2023.

Referencia: Página: 8/12
5315-2000-RH-MMT-003

P-5315 MEMORANDUM TÉCNICO Apoyo tramitación Adenda, Simulaciones Cambio

Climático

**Gráfico 6: Evolución temporal de niveles pozo CWP-01 simulación.**

Fuente: Arcadis, 2023.

**Gráfico 7: Evolución temporal de niveles pozo DPEC-08 simulación.**

Fuente: Arcadis, 2023.

Referencia: Página: 9/12
5315-2000-RH-MMT-003

P-5315 MEMORANDUM TÉCNICO Apoyo tramitación Adenda, Simulaciones Cambio

Climático

**Gráfico 8: Evolución temporal de niveles pozo PEP-01 simulación.**

Fuente: Arcadis, 2023.

El Gráfico 9 muestra la evolución temporal de los caudales simulados para el Caso Base y el Caso
Proyecto considerando efectos del cambio climático en la vertiente Jachucoposa.

**Gráfico 9: Evolución temporal caudal vertiente Jachucoposa simulación.**

Fuente: Arcadis, 2023.

Referencia: Página: 10/12
5315-2000-RH-MMT-003

P-5315 MEMORANDUM TÉCNICO Apoyo tramitación Adenda, Simulaciones Cambio

Climático

El comportamiento de los caudales de la vertiente Jachucoposa mostrados en el Gráfico 9, se
mantienen relativamente similares en ambos casos hasta el 2041. A partir de esta fecha, se aprecia
una mejora de los resultados del Proyecto, tal como se vio en las simulaciones de la DIA, sin
embargo, la recuperación observada en la vertiente es inferior respecto a dichos escenarios, en cerca
de 10 l/s.

2. Recargas y descargas subterráneas

En el Gráfico 10 y Gráfico 11 se presentan la variación de los caudales pasantes en los pasos de
Portezuelo y Coposa Norte, respectivamente. Al igual que en el caso de la vertiente, el
comportamiento es similar a lo observado en las simulaciones sin cambio climático, pero con una
magnitud inferior, debido a la disminución de la recarga considerada.

**Gráfico 10: Evolución temporal caudal pasante desde Portezuelo.**

Fuente: Arcadis, 2023.

Referencia: Página: 11/12
5315-2000-RH-MMT-003

P-5315 MEMORANDUM TÉCNICO Apoyo tramitación Adenda, Simulaciones Cambio

Climático

**Gráfico 11: Evolución temporal caudal pasante hacia Coposa Norte.**

Fuente: Arcadis, 2023.

Saluda atentamente,

ARCADIS

Gabriel Letelier

Ingeniero de Proyectos

Referencia: Página: 12/12
5315-2000-RH-MMT-003