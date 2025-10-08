---
title: Sin título
author: Bárbara
date: D:20200804104556-04'00'
language: es
type: report
pages: 38
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Modelación atmosférica Odorantes “Proyecto Planta de Elaboración de Quesos y Planta de Tratamiento de Riles LACSUR.”
  - 1 Introducción
  - 2 Modelo Calpuff
  - 3 Metodología
  - 4 Marco legal aplicable
  - 5 Resultados
  - 6 Conclusiones
  - Informe elaborado por contanto@ekosambiente.cl Asesoría y Capacitación Ambiente Social SpA. Consultoría, asesoría y capacitaciones ambientales contacto@ambientesocial.cl www.ambientesocial.cl
-->

# Modelación atmosférica Odorantes “Proyecto Planta de Elaboración de Quesos y Planta de Tratamiento de Riles LACSUR.”

Julio, 2020

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

**Tabla de contenidos**

**1** **Introducción ___________________________________________ 4**

**2** **Modelo Calpuff __________________________________________ 6**

**3** **Metodología ____________________________________________ 7**

**3.1** **Recopilación y procesamiento de datos meteorológicos, topográficos y de uso**
**de suelo del área de estudio. _____________________________________ 7**

3.1.1 Área de estudio ____________________________________________________________7
3.1.2 Recopilación y procesamiento de los escenarios de emisión propuesto para la modelación Areal en
CALPUFF. ___________________________________________________________10
3.1.3 Factores de emisión considerados para la estimación de olores. __________________________11
3.1.4 Emisiones de olores ___________________________________________________________15
3.1.5 Análisis de los resultados _________________________________________________________16
**4** **Marco legal aplicable ____________________________________ 20**

**5** **Resultados ____________________________________________ 21**

**5.1** **Caracterización Geofísica ______________________________________ 21**

5.1.1 Topografía ___________________________________________________________21
**5.2** **Caracterización Meteorológica __________________________________ 21**

5.2.1 Viento ___________________________________________________________21
5.2.1.1 Dirección y velocidad de vientos predominantes anuales ________________________________22
5.2.2 Temperatura del aire ___________________________________________________________26
5.2.3 Análisis de incertidumbre _________________________________________________________27
**5.3** **Concentración de odorantes ____________________________________ 30**
**5.4** **Evaluación discreta de las emisiones de olor ________________________ 32**

**6** **Conclusiones __________________________________________ 36**

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 2 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

**Figuras**

Figura 1. Ubicación de proyecto ______________________________________________ 5
Figura 2. Planta general zonas de riego ________________________________________ 5
Figura 3. Área de estudio ___________________________________________________ 9
Figura 4. Ubicación de las fuentes generadoras de olor. __________________________ 14
Figura 5. Ubicación de las fuentes generadoras de olor (riego de emergencia). _______ 14
Figura 6. Ubicación de receptores discretos en el Proyecto. _______________________ 18
Figura 7. Ubicación de receptores discretos en el área de riego de emergencia. _______ 18
Figura 8. Elevación de terreno de la zona. _____________________________________ 21
Figura 9. Rosa de viento anual WRF Osorno, 2019. _____________________________ 22
Figura 10. Frecuencia velocidades de viento anual WRF Osorno, 2019. ______________ 23
Figura 11. Vientos estacionales WRF Osorno, 2019. _____________________________ 24
Figura 12. Velocidad del viento estacional WRF Osorno, 2019. _____________________ 26
Figura 13. Temperatura del aire WRF Osorno, 2019. ____________________________ 27
Figura 14. Ciclos diarios de velocidad del viento observados vs modelados, año 2019. __ 28
Figura 15. Ciclos diarios de temperatura superficial observada vs modelada, año 2019. _ 28
Figura 16. Rosas de vientos anuales de Estación Osorno versus WRF, Año 2019. ______ 29
Figura 17. Dispersión de Odorantes __________________________________________ 31
Figura 18. Curvas de iso-concentración horaria _________________________________ 32

**Tablas**

Tabla 1. Coordenadas UTM del área de estudio. Datum WGS-84, Huso 18 Sur. ________ 9
Tabla 2. Factores de emisión. _______________________________________________ 11
Tabla 3. Ubicación y superficie de las unidades críticas de olores del proyecto. _______ 12
Tabla 4. Fuentes y características de emisión de olor del proyecto. _________________ 15
Tabla 5 Características de receptores discretos. ________________________________ 19
Tabla 6. Normativa internacional para concentraciones de olor. ____________________ 20
Tabla 7. Vientos estacionales WRF Osorno, 2019. _______________________________ 25
Tabla 8. Concentraciones de olor modeladas en receptores discretos (percentil 98) Norma

UK. ___________________________________________________________________ 33
Tabla 9. Concentraciones de olor modeladas en receptores discretos (percentil 98) Norma

Holandesa. _____________________________________________________________ 34

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 3 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

# 1 Introducción

El presente estudio tiene como objetivo estimar y evaluar la dispersión atmosférica de
emisiones de olores que generará el proyecto **“Planta de Elaboración de Quesos y**
**Planta de Tratamiento de Riles LACSUR.”** ubicado en la Comuna de Río Negro,
Provincia de Osorno, Región de Los Lagos.

El proyecto pretende la construcción y operación de una planta de elaboración de quesos,
junto con su planta de tratamiento de Riles. Los Riles a tratar serán los producidos en el
proceso productivo de LACSUR, empresa que se dedica a la fabricación exclusiva de quesos,
los efluentes tratados serán descargados al estero Huilma durante los meses de lluvias
(cuando el estero posea caudal de dilución), en los meses de verano serán utilizados para
riego. En la planta se tratarán riles con carga orgánica, mediante la tecnología BIDA®, en
la cual se realiza el tratamiento de los riles mediante filtros biológicos dinámicos aerobios.

El Proyecto de riego de praderas mediante aspersión, corresponde a la construcción de un
sistema de riego nuevo, consistente en la instalación de una unidad de bombeo eléctrica,
una matriz de PVC hidráulico con laterales y líneas móviles con tazones con aspersores para
la aplicación del agua en la pradera. Se utilizará Irripod Plus2 o similar como sistema de
riego. Es un sistema flexible y rentable de rociadores de tuberías de riego para los cultivos
de pastos y forraje, diseñados para funcionar a baja presión y distribuir el agua en una tasa
de absorción lenta durante un periodo de 12 a 24 horas

En Chile a la fecha no se cuenta con normas de olores de calidad del aire, sin embargo,
para efectos comparativos se considerará como referencia la normativa internacional. En el
presente estudio se utilizaron para comparación, criterios establecidos en el Reino Unido,
norma IPPCH4 que fija un nivel de inmisión de 5 uo/m [3] percentil 98 anual de los promedios
horario. También la norma Holandesa de olores, es la más estricta, estableciendo en la
“Netherlands Emission Guidelines for Air”, un límite de 3,5 uo/m [3] para viviendas aisladas
cercanas a plantas depuradoras de aguas residuales.

Para evaluar el efecto de las eventuales emisiones futuras, generadas por las unidades
críticas, se utilizó un modelo de dispersión tipo puff, llamado CALPUFF, el cual es
recomendado por el Ministerio de Medio Ambiente en la Guía para el uso de modelos de
calidad del aire en el SEIA, publicada el año 2012. CALPUFF es un modelo de dispersión
utilizado en todo el mundo para simulaciones de concentraciones ambientales de las
emisiones de operaciones normales, con el objeto de establecer, desarrollar y analizar
escenarios de emisión y regulación.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 4 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

**Figura 1. Ubicación de proyecto**

Fuente: Elaboración propia.

**Figura 2. Planta general zonas de riego**

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 5 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

# 2 Modelo Calpuff

De acuerdo a la “Guía para el uso de modelos de calidad del aire en el SEIA” los modelos
existentes se pueden clasificar en Gaussianos, Eulerianos, Langrangeanos y tipo “Puff”.

La modelación de dispersión atmosférica de los contaminantes provenientes del proyecto,
se realizó con un modelo tipo “Puff”, específicamente el modelo CALPUFF.

Los modelos tipo “puff” son una combinación entre los modelos Gaussianos y los modelos
Langrangeanos, en el sentido de que esencialmente calculan la dispersión de contaminantes
provenientes de una emisión instantánea, llamada “puff”, a lo largo de una trayectoria. Su
aproximación matemática consiste en estimar la dispersión en forma Gaussiana en cada
punto de una trayectoria; es decir, los modelos tipo “puff” sólo requieren una trayectoria
por “puff”, lo que hace su cálculo mucho más rápido. En el caso de emisiones continuas, se
simulan las trayectorias y la dispersión Gaussiana de muchos “puffs”.

Considerando las características del terreno, las distintas unidades geomorfológicas del área
de influencia del proyecto y el dominio de la modelación se consideró utilizar el modelo
CALPUFF para simular la dispersión de los contaminantes generados por la operación futura
del proyecto.

CALPUFF, es un modelo no estacionario desarrollado por “TRC Scientists”, ha sido usado en
una amplia variedad de estudios de modelación de calidad del aire, incluyendo: deposición
de contaminantes tóxicos, impactos de incendios forestales, evaluaciones de visibilidad y
un largo rango de estudios de transporte.

Así mismo, es un modelo completo que incorpora herramientas para procesar datos
meteorológicos y geofísicos, modelos de dispersión y pos procesamiento. Dicho modelo es
recomendado por la agencia de protección ambiental (EPA) para modelar transporte a larga
distancia de contaminantes.

**CALPUFF se compone de tres módulos:**

 - CALMET: Es un modelo meteorológico que desarrolla campos horarios de
viento y temperatura en una grilla de tres dimensiones. También asocia
campos en dos dimensiones de altura y usos de suelo.

 - CALPUFF: Es un modelo de transporte y dispersión emitido desde fuentes
modeladas, simulando procesos de dispersión y transformación. CALPUFF
utiliza los datos generados por CALMET. Los archivos de salida de CALPUFF
contienen las concentraciones horarias o deposición por hora de flujos
evaluados en receptores seleccionados.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 6 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

 - CALPOST: Es usado para procesar aquellos archivos generados por
CALMET y CALPUFF, produciendo tabulaciones que resumen los resultados
de la simulación, identificando, por ejemplo, la concentración promedio de
24 horas para cada receptor.

En la presente Modelación se utilizó un CALMET generado con WRF.

**Ecuación del modelo CALPUFF**

La ecuación básica que utiliza el modelo para realizar la modelación es la siguiente:

Dónde:

**C** : concentración a nivel del suelo

(g/m3), **Q:** masa de contaminantes
(g) en la nube.
**σx** : desviación estándar (m) de la distribución de Gauss en el viento a lo largo de la dirección.
**σy:** desviación estándar (m) de la distribución de Gauss en el viento de

costado **σz:** desviación estándar (m) de la distribución de Gauss en la
dirección vertical. **da:** distancia (m) del centro de la nube al receptor en la
dirección del viento a lo largo. **dc:** distancia (m) del centro de la nube al
receptor en la dirección de viento cruzado.

# 3 Metodología

La modelación de la dispersión de olores se realizó de acuerdo a la siguiente metodología.

**3.1** **Recopilación y procesamiento de datos meteorológicos, topográficos y de**
**uso de suelo del área de estudio.**

**3.1.1** **Área de estudio**

La modelación fue realizada utilizando meteorología modelada con el modelo de pronóstico
Weather Research and Forecasting (WRF). Modelo recomendado por la “Guía para el Uso

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 7 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

de Modelos de Calidad del Aire en el SEIA”, siendo uno de los modelos meteorológicos de
pronóstico más avanzados y completos, el que es mantenido por

NCAR/NOAA de Estados Unidos. Además, se ha ocupado en la mayoría de los proyectos
relacionados con modelación atmosférica cargados por organismos estatales, como el
Servicio de Evaluación Ambiental (SEA; antiguamente CONAMA) y la Comisión Nacional de
Energía (CNE) en los últimos cinco años.

Se utilizó una grilla meteorológica de 50 km x 50 km, de resolución horizontal 1 km,
generado a partir del modelo de pronóstico meteorológico WRF para el periodo 1 de enero
al 31 de diciembre del 2019.

Por otra parte, para medir que tan cercano a la realidad meteorológica de la zona fueron
modelados los datos WRF, se realizó un Análisis de Incertidumbre de estos, comparando
datos de viento y temperatura con los medidos por la Estación de monitoreo Osorno

Sin embargo, la modelación de dispersión se realizó en una grilla más pequeña, la cual
incluyó el área donde se desarrollarán las obras del proyecto.

Para el estudio de la dispersión de emisiones se consideró una grilla de 15 x 15 km [2] .

En la siguiente figura se presenta el área de estudio que se consideró en la modelación de
emisiones atmosféricas del proyecto.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 8 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

**Figura 3. Área de estudio**

Fuente: Elaboración propia.

En la siguiente tabla se presentan las coordenadas del área de estudio.

**Tabla 1. Coordenadas UTM del área de estudio. Datum WGS-84, Huso 18**

**Sur.**

|Vértice|Este (m)|Norte (m)|
|---|---|---|
|a|639.715|5.483.356|
|b|654.715|5.483.356|
|c|639.715|5.498.356|
|d|654.715|5.498.356|

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 9 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

**3.1.2** **Recopilación y procesamiento de los escenarios de emisión propuesto**

**para la modelación Areal en CALPUFF.**

Tal como se indicó, el objetivo del informe es evaluar la dispersión atmosférica de olores
del proyecto, considerando las fuentes que se construirán y serán parte del proyecto.

**Estimación de emisión de olores**

Para realizar la estimación de las emisiones de olores del proyecto se utilizará como
metodología, factores de emisión de literatura (F.E.). En la siguiente tabla se presentan los
principales factores de emisión para las unidades críticas del proyecto. El F.E. se mide en
unidades de olor por unidad de tiempo y por unidad de superficie (uo/s/m [2] ). Cabe destacar
que los factores de emisión utilizados son específicamente para plantas de tratamiento de
aguas servidas, sin embargo, las unidades generadoras de olor son las mismas que para
una planta de tratamiento de RILes.

Se le informa a la autoridad, que la modelación de olor realizada, fue realizada utilizando
meteorología modelada con el modelo de pronóstico Weather Research and Forecasting
(WRF). Modelo recomendado por la “Guía para el Uso de Modelos de Calidad del Aire en el
SEIA”, siendo uno de los modelos meteorológicos de pronóstico más avanzados y
completos, el que es mantenido por NCAR/NOAA de Estados Unidos. Además, se ha
ocupado en la mayoría de los proyectos relacionados con modelación atmosférica cargados
por organismos estatales, como el Servicio de Evaluación Ambiental (SEA; antiguamente
CONAMA) y la Comisión Nacional de Energía (CNE) en los últimos cinco años.

Se utilizó una grilla meteorológica de 50 km x 50 km, de resolución horizontal 1 km,
generado a partir del modelo de pronóstico meteorológico WRF para el periodo 1 de enero
al 31 de diciembre del 2019.

Por otra parte, para medir que tan cercano a la realidad meteorológica de la zona fueron
modelados los datos WRF, se realizó un Análisis de Incertidumbre de estos, comparando
datos de viento y temperatura con los medidos por la Estación de monitoreo Osorno.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 10 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

**3.1.3** **Factores de emisión considerados para la estimación de olores.**

**Tabla 2. Factores de emisión**

|Descripción|Unidad del tratamiento|FE (uo/s-m2)|
|---|---|---|
|Factor de emisión para olores/sistema de acceso y<br>pretratamiento/separador de partículas gruesas (en<br>área superficial)|Filtro parabólico|7,5|
|Factor de emisión para olores/sistema de acceso y<br>pretratamiento/selector (aireado)|<br>DAF|6|
|Factor de emisión para olores/línea de agua/estanque<br>de aireación/zona aeróbica/aireación en punto único<br>sin cobertura|Biofiltro|2,5|
|Fórmula<br>de<br>emisión<br>para<br>olores/línea<br>de<br>agua/sedimentador secundario (en área de acceso)|<br>Decantador|1,65|
|Fórmula<br>de<br>emisión<br>para<br>olores/línea<br>de<br>agua/sedimentador secundario (en área superficial y<br>puntos de descarga)|<br> <br>Piscina de Acumulación|1,3|
|Fórmula<br>de<br>emisión<br>para<br>olores/línea<br>de<br>agua/sedimentador secundario (en área superficial y<br>puntos de descarga)|Riego y Riego de<br>Emergencia|1,3|

Fuente: Informe final servicio de recopilación y sistematización de factores de emisión al aire para el SEA,

2015

Para evaluar el efecto en la calidad del aire producido por los olores provenientes de las
unidades críticas del proyecto, se realizará una simulación de la dispersión y concentración
de los olores. A continuación, se presentan las coordenadas y superficies de las unidades
críticas que generarán olores en un evento puntal de emisión.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 11 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

**Tabla 3. Ubicación y superficie de las unidades críticas de olores del proyecto**

|Unidad|Elevación (msnm)|Vértices|UTM, Huso 18, Datum WGS-84|Col5|
|---|---|---|---|---|
|**Unidad**|**Elevación (msnm)**|**Vértices**|**Este (km)**|**Norte (km)**|
|Filtro parabólico|132|a|647,816|5491,162|
|Filtro parabólico|132|b|647,820|5491,161|
|Filtro parabólico|132|c|647,817|5491,165|
|Filtro parabólico|132|d|647,821|5491,164|
|DAF|132|a|647,802|5491,165|
|DAF|132|b|647,813|5491,162|
|DAF|132|c|647,803|5491,168|
|DAF|132|d|647,814|5491,165|
|Biofiltro|131|a|647,800|5491,180|
|Biofiltro|131|b|647,815|5491,176|
|Biofiltro|131|c|647,810|5491,218|
|Biofiltro|131|d|647,825|5491,215|
|Decantador|130|a|647,820|5491,217|
|Decantador|130|b|647,824|5491,216|
|Decantador|130|c|647,820|5491,220|
|Decantador|130|d|647,825|5491,219|
|Piscina de Acumulación|131|a|647,766|5491,134|
|Piscina de Acumulación|131|b|647,781|5491,128|
|Piscina de Acumulación|131|c|647,740|5491,085|
|Piscina de Acumulación|131|d|647,756|5491,076|
|Riego|123|a|647,477|5491,569|
|Riego|123|b|647,893|5491,176|
|Riego|123|c|647,508|5491,602|
|Riego|123|d|647,918|5491,199|
|Riego de Emergencia I|107|a|644,503|5488,415|
|Riego de Emergencia I|107|b|644,622|5488,464|
|Riego de Emergencia I|107|c|644,532|5488,155|
|Riego de Emergencia I|107|d|644,693|5488,163|
|Riego de Emergencia II|95|a|644,674|5488,570|

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 12 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

|Unidad|Elevación (msnm)|Vértices|UTM, Huso 18, Datum WGS-84|Col5|
|---|---|---|---|---|
|**Unidad**|**Elevación (msnm)**|**Vértices**|**Este (km)**|**Norte (km)**|
|**Unidad**|**Elevación (msnm)**|b|645,066|5488,568|
|**Unidad**|**Elevación (msnm)**|c|644,622|5488,464|
|**Unidad**|**Elevación (msnm)**|d|645,067|5488,449|
|Riego de Emergencia III|99|a|644,622|5488,464|
|Riego de Emergencia III|99|b|645,130|5488,444|
|Riego de Emergencia III|99|c|644,659|5488,335|
|Riego de Emergencia III|99|d|645,090|5488,265|
|Riego de Emergencia IV|100|a|644,659|5488,335|
|Riego de Emergencia IV|100|b|644,994|5488,275|
|Riego de Emergencia IV|100|c|644,693|5488,163|
|Riego de Emergencia IV|100|d|644,948|5488,089|
|Riego de Emergencia V|86|a|645,066|5488,568|
|Riego de Emergencia V|86|b|645,108|5488,533|
|Riego de Emergencia V|86|c|645,067|5488,449|
|Riego de Emergencia V|86|d|645,130|5488,444|
|Riego de Emergencia VI|85|a|645,130|5488,444|
|Riego de Emergencia VI|85|b|645,250|5488,389|
|Riego de Emergencia VI|85|c|645,090|5488,265|
|Riego de Emergencia VI|85|d|645,202|5488,183|
|Riego de Emergencia VII|83|a|645,243|5488,325|
|Riego de Emergencia VII|83|b|645,291|5488,267|
|Riego de Emergencia VII|83|c|645,202|5488,183|
|Riego de Emergencia VII|83|d|645,244|5488,153|

***Se divide el área de riego de emergencia en VII áreas diferentes para su mejor modelación, la**
**superficie total es de 25,8 ha.**

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 13 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

**Figura 4. Ubicación de las fuentes generadoras de olor**

**Figura 5. Ubicación de las fuentes generadoras de olor (riego de emergencia)**

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 14 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

**3.1.4** **Emisiones de olores**

Cabe destacar que los factores de emisión de olor utilizados, son propios de plantas de
tratamiento de aguas residuales, esto asume un escenario peor, ya que las aguas servidas
generan mayores emisiones de olor que los RILes.

A continuación, se presenta la emisión de unidades de olor (uo/s) para cada unidad de la
planta. Lo cual en su totalidad generaría 369.180,71 uo/s al evaluar el peor escenario, el
cual incorpora la zona de riego de emergencia (335.400 uo/s), emisiones por el proyecto
(3.226,81 uo/s) y el riego existente en el predio (30.553,9 uo/s).

Es importante señalar, que el área de riego de emergencia utilizada en la modelación,
contempla toda la superficie destinada dentro del proyecto de riego, a modo de ser prolijos
al momento de evaluar la posible afectación a los receptores cercanos. Sin embargo, el área
de riego efectiva a utilizar corresponde al 10% del área total modelada.

**Tabla 4. Fuentes y características de emisión de olor del proyecto**

|Descripción|Unidad del<br>tratamiento|FE<br>(uo/sm2)|Superficie<br>(m2)|Emisión<br>(uo/s)|Tipo de<br>Fuente|Régimen<br>Anual|Régimen<br>Diario|
|---|---|---|---|---|---|---|---|
|Factor de emisión para<br>olores/sistema<br>de<br>acceso<br>y <br>pretratamiento/<br>separador de partículas<br>gruesas (en área <br>superficial)|Filtro<br>parabólico|7,5|12,7|95,25|Areal|Constante|24 horas|
|Factor de emisión para<br>olores/sistema<br>de<br>acceso<br>y <br>pretratamiento/selector<br>(aireado)|DAF|6|35,3|211,8|Areal|Constante|24 horas|
|Factor de emisión para<br>olores/línea<br>de<br>agua/estanque<br>de<br>aireación/zona<br>aeróbica/aireación<br>en<br>punto<br>único<br>sin<br>cobertura|Biofiltro|2,5|600|1.500|Areal|Constante|24 horas|
|Fórmula<br>de<br>emisión<br>para olores/línea de<br>agua/sedimentador<br>secundario (en área de<br>acceso)|Decantador|1,65|12,7|20,96|Areal|Constante|24 horas|

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 15 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

|Descripción|Unidad del<br>tratamiento|FE<br>(uo/sm2)|Superficie<br>(m2)|Emisión<br>(uo/s)|Tipo de<br>Fuente|Régimen<br>Anual|Régimen<br>Diario|
|---|---|---|---|---|---|---|---|
|Fórmula de<br>emisión<br> <br>para<br>olores/línea<br>de<br>agua/sedimentador<br>secundario (en<br>área<br>superficial y puntos de<br>descarga)|Piscina de<br>Acumulación|1,3|1.076|1.398,8|Areal|Sólo Abril1|24 horas|
|Fórmula de<br>emisión<br> <br>para<br>olores/línea<br>de<br>agua/sedimentador<br>secundario (en<br>área<br>superficial y puntos de<br>descarga)|Riego|1,3|23.503|30.553,9|Areal|Solo<br>Periodo<br>Estival<br>|12 horas|
|Fórmula de<br>emisión<br> <br>para<br>olores/línea<br>de<br>agua/sedimentador<br>secundario (en<br>área<br>superficial y puntos de<br>descarga)|Riego de<br>Emergencia|1,3|258.000|335.400|Areal|10 dias de<br>abril y<br>marzo2|12 horas|

Fuente: Elaboración propia en base a Tabla N°26 del informe final Servicio de Recopilación y

Sistematización de Factores de Emisión al Aire para el SEA, 2015.

**3.1.5** **Análisis de los resultados**

Para analizar los resultados de la modelación de dispersión de olores, se realizaron mapas
de iso-concentración de las emisiones generadas por la operación del proyecto. Dichos
mapas permitieron evaluar los niveles de concentración, en toda el área de estudio.

Por otro lado, con el fin de analizar el impacto en la calidad del aire en los poblados más
cercanos, se realizó una modelación discreta, en receptores específicos, para obtener la
concentración en el aire, generada por el proyecto.

Para realizar la evaluación discreta se definieron 11 puntos, los cuales 8 se ubicaron en los
sectores más cercanos a la planta y 3 cercanos a la zona de riego de emergencia. A

1 Sólo en caso de que no haya superficie de riego disponible.
2 De acuerdo al balance hídrico, se consideran aproximadamente 10 días entre los meses de marzo
y abril para riego en caso de emergencia, asumiendo peor escenario a evaluar (cuando la piscina de
acumulación no sea suficiente). Ver Anexo 11.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 16 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

continuación, se presenta la ubicación y coordenadas de los receptores discretos utilizados
en la modelación.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 17 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

**Figura 6. Ubicación de receptores discretos en el Proyecto**

**Figura 7. Ubicación de receptores discretos en el área de riego de emergencia**

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 18 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

En la siguiente tabla se presentan las coordenadas UTM de los puntos receptores. Los cuales
fueron evaluados a una altura de 1,8 metros y están ubicados en zona rural.

**Tabla 5 Características de receptores discretos**

|RECEPTOR|Coord. UTM 18 G|Col3|DISTANCIA<br>AL PROYECTO<br>(m)|DESCRIPCIÓN|
|---|---|---|---|---|
|**RECEPTOR **|**Este**|**Norte**|**Norte**|**Norte**|
|1|647.680|5.491.513|320|Vivienda ubicada al lado norponiente del Proyecto|
|2|647.515|5.491.671|540|Vivienda ubicada al lado norponiente del Proyecto|
|3|647.073|5.491.915|1.015|Vivienda ubicada al lado norponiente del Proyecto|
|4|647.212|5.492.387|1.310|Vivienda ubicada al lado norponiente del Proyecto|
|5|646.585|5.490.920|1.175|Vivienda ubicada al lado surponiente del Proyecto|
|6|646.840|5.490.640|1.000|Vivienda ubicada al lado surponiente del Proyecto|
|7|648.497|5.490.810|716|Vivienda ubicada al lado suroriente del Proyecto|
|8|648.571|5.491.670|867|Vivienda ubicada al lado nororiente del Proyecto|
|9|645.232|5.488.531|140|Vivienda ubicada al lado este del área de riego de<br>emergencia|
|10|644.723|5.488.732|175|Vivienda ubicada al lado noreste del área de riego<br>de emergencia|
|11|644.305|5.488.108|262|Lechería ubicada al este de zona de riego de<br>emergencia|

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 19 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

# 4 Marco legal aplicable

En Chile a la fecha no se cuenta con normas de olores de calidad del aire, sin embargo,
para efectos de estudio se considera como referencia, normativa internacional. En el
presente estudio se utilizaron para comparación criterios establecidos en el Reino Unido y
un límite establecido en la norma Holandesa para plantas de tratamiento de aguas
residuales.

**Tabla 6. Normativa internacional para concentraciones de olor**

|País|Concentración máxima (percentil 98<br>anual, promedio 1 hora)|
|---|---|
|Reino Unido (Norma IPPCH4)|5,0 (uo/m3)|
|Holanda (Netherlands Emission Guidelines for<br>Air)|3,5 (uo/m3)|

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 20 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

# 5 Resultados

**5.1** **Caracterización Geofísica**

**5.1.1** **Topografía**

**Figura 8. Elevación de terreno de la zona**

En la topografía se puede observar la elevación del terreno, de donde se desprende que
dicha elevación varía entre los 20 a 360 m.s.n.m. Hacia el oeste es donde se evidencia las

mayores alturas, siendo que el proyecto está presente entre los 100 y 140 m.s.n.m.

**5.2** **Caracterización Meteorológica**

**5.2.1** **Viento**

A continuación, se presenta la caracterización para la variable vientos.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 21 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

**5.2.1.1** **Dirección y velocidad de vientos predominantes anuales**

A continuación, se presenta la rosa de vientos anual, construida en base a los datos
generados con el modelo WRF con datos del año 2019 para la ciudad donde se emplaza el
Proyecto y sus alrededores. La rosa de vientos, es un método gráfico que consiste en
representar conjuntamente las distribuciones de frecuencias de la dirección y la velocidad
del viento.

**Figura 9. Rosa de viento anual WRF Osorno, 2019**

De acuerdo a la dirección de vientos modelados para el año 2019, se puede apreciar que el
vector resultante apunta en dirección oeste noroeste (ONO), es decir, que la cantidad
principal de vientos se origina desde esta dirección, lo que es consistente con la influencia
de abundantes sistemas frontales. En base a lo anterior, es esperable que la mayor
dispersión de contaminantes ocurra en dirección este sureste (ESE).

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 22 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

**Figura 10. Frecuencia velocidades de viento anual WRF Osorno, 2019**

45

40

35

30

25

20

15

10

5

0

Anual

|Col1|39,8|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
||||**21,7**|||
|||**20,9**||||
|||||||
|||||**9,1**||
|**6,5**|||||**1,9**|
|||||||

Calmos 0,5-2,1 2,1-3,6 3,6-5,7 >=5,7 >=8,8

**Velocidad de viento (m/s)**

Con respecto a las velocidades de viento, se puede apreciar que predominan las velocidades
entre 0,5 2,1 m/s con un 39,8% de frecuencia, seguido por las velocidades entre 3,6 y 5,7
m/s, con un 21,7%. Cabe destacar que los vientos con menor frecuencias son aquellos
mayores o iguales a 8.8 m/s.

**Vientos estacionales**

A continuación, se presenta la dirección y velocidad del viento para cada estación del año
de acuerdo al WRF, 2019 para la zona de estudio.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 23 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

**Dirección y velocidad de viento estacional**

**Figura 11. Vientos estacionales WRF Osorno, 2019**

**VERANO** **OTOÑO**

**INVIERNO** **PRIMAVERA**

Las rosas de vientos estacionales, muestran que los vectores resultantes son nornoroeste
(NNO) durante las estaciones de otoño e invierno, mientras que para la para la estación de
verano los vientos se originan principalmente en dirección suroeste (SO) y en primavera en
dirección oeste (O). En base a lo anterior, se observa un evidente contraste entre las rosas
de los meses cálidos con las de los meses fríos de (otoño e invierno), observándose que
durante los meses fríos aparece un componente norte (N) que disminuye
considerablemente durante los meses de buen tiempo correspondientes a verano. Esto

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 24 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

ultimó está asociado a frentes de mal tiempo que suelen aparecer durante otoño - invierno,
trayendo consigo fuertes vientos norte.

**Tabla 7. Vientos estacionales WRF Osorno, 2019**

|Estación|Dirección de<br>Vector<br>Resultante|Velocidades y<br>Calmas (m/s)|Frecuencia %|
|---|---|---|---|
|Verano|OSO (24%)|0,5-2,1|39,1|
|Verano|OSO (24%)|2,1-3,6|25,0|
|Verano|OSO (24%)|3,6-5,7|24,7|
|Verano|OSO (24%)|5,7-8,8|6,0|
|Verano|OSO (24%)|Calma|4,6|
|Otoño|NNO (7%)|0,5-2,1|47,8|
|Otoño|NNO (7%)|2,1-3,6|16,4|
|Otoño|NNO (7%)|3,6-5,7|14,0|
|Otoño|NNO (7%)|5,7-8,8|8,9|
|Otoño|NNO (7%)|Calma|10,0|
|Invierno|NNO (8%)|0,5-2,1|39,8|
|Invierno|NNO (8%)|2,1-3,6|22,5|
|Invierno|NNO (8%)|3,6-5,7|18,0|
|Invierno|NNO (8%)|5,7-8,8|11,2|
|Invierno|NNO (8%)|Calma|5,8|
|Primavera|O (37%)|0,5-2,1|33,4|
|Primavera|O (37%)|2,1-3,6|19,7|
|Primavera|O (37%)|3,6-5,7|30,1|
|Primavera|O (37%)|5,7-8,8|10,4|
|Primavera|O (37%)|Calma|5,6|

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 25 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

**Figura 12. Velocidad del viento estacional WRF Osorno, 2019**

Se observa principalmente que, para todas las estaciones, priman las velocidades de vientos
entre 0,5 y 2,1 m/s principalmente, siendo en los meses de otoño en donde ocurren con
mayor frecuencia. Cabe destacar que, para la estación de otoño, es también donde ocurre
el mayor porcentaje de frecuencia anual de vientos calmos con un (10%).

**5.2.2** **Temperatura del aire**

A continuación, se presenta el perfil de la temperatura mensual simulada por el

modelo meteorológico (WRF) para el año 2019.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 26 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

**Figura 13. Temperatura del aire WRF Osorno, 2019**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sept|Oct|Nov|Dic|
|Temp prom|11,6|13,5|11,9|10,4|8,7|7,1|6,5|6,0|6,7|7,8|10,4|11,7|
|Temp max|20,2|26,4|22,1|18,1|14,6|13,7|11,8|11,6|16,9|17,4|19,7|18,8|
|Temp min|2,5|4,8|4,5|3,4|-0,4|-2,5|-1,5|-2,0|-0,2|-0,5|2,1|3,8|

Temp prom Temp max Temp min

La figura sugiere que la temperatura promedio mensual disminuye principalmente en los
meses de junio - octubre y aumenta en los meses de noviembre - mayo.

En este sentido la temperatura promedio más alta se simuló para el mes de febrero, donde
alcanzarían los 13,5°C, en tanto que la mínima temperatura promedio mensual se espera
en el mes de agosto donde llegaría a los 6,0°C.

Con respecto a la amplitud térmica se observa que esta es mayor en el mes de febrero con
oscilaciones de 21,5oC, mientras que la más baja ocurre en el mes de julio con 13,3oC.

**5.2.3** **Análisis de incertidumbre**

A continuación, se presenta un resumen del análisis de la capacidad predictiva del modelo
meteorológico WRF, donde se realiza una comparación entre la meteorología observada por
la Estación de Monitoreo Osorno y la meteorología modelada por WRF para el año 2019.

Las gráficas siguientes presentan la comparación entre los valores observados y modelados
para la variable de velocidad de viento en el punto donde se ubica la Estación Osorno.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 27 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

**Figura 14. Ciclos diarios de velocidad del viento observados vs modelados, año**

**2019**

Fuente: Elaboración propia en base a registros de estación Osorno y datos modelados con WRF, 2019.

Se aprecia en el gráfico anterior que ambos siguen el mismo patrón de ciclo diario, sin
embargo, la modelación meteorológica manifiesta una leve subestimación de la velocidad
del viento que permiten establecer que las concentraciones de olor modeladas no se
encontraran subestimadas.

**Figura 15. Ciclos diarios de temperatura superficial observada vs modelada,**

**año 2019**

Fuente: Elaboración propia en base a registros de estación Osorno y datos modelados con WRF, 2019.

Del gráfico anterior se aprecia que las curvas de las temperaturas superficial observada y
modelada siguen la misma tendencia, no obstante, el modelo subestima levemente la

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 28 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

temperatura, por ende, el modelo de dispersión podría presentar diferencias en ciertos
periodos de tiempo donde la temperatura modelada y observada no convergen.

Al comparar los ciclos diarios observados y de pronóstico, se evidencia que el modelo
reproduce correctamente la trayectoria de las curvas de velocidad del viento y temperatura
superficial, donde el modelo subestima levemente la intensidad del viento y la temperatura
superficial.

**Rosas de Viento**

A continuación, en las siguientes figuras se presenta la dirección de vientos anuales
observados por Estación Osorno y modelados por WRF para el año 2019.

**Figura 16. Rosas de vientos anuales de Estación Osorno versus WRF, Año 2019**

Fuente: Elaboración propia en base a registros de estación Osorno y datos modelados con WRF, 2019.

En la figura anterior se puede observar las direcciones de vientos observados y las
generados por el modelo de pronóstico WRF, ambas rosas muestran una predominancia de
vientos Oeste Noroeste, de acuerdo al vector resultante y las velocidades varían entre los
mismos rangos (0,5 -2,10 y 2,10 a 3,6 m/s).

A modo de conclusión, el modelo WRF generado en la zona del Proyecto, simula
correctamente los parámetros meteorológicos, observándose que la mayor diferencia se
aprecia en las velocidades de vientos que son levemente sobrestimados por el modelo. Para
contrarrestar lo anterior y evitar una posible subestimación de concentraciones modeladas,
se modeló el peor escenario posible, eligiendo los factores de emisión más conservadores,
de manera de modelar las tasas de emisión más altas y considerándolas de manera
constante durante todo el año (las 24 horas del día), solo con excepción de la piscina de
acumulación, la cual funcionará exclusivamente el mes de abril, riego que debido a que

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 29 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

funcionará solo en periodo estival fue modelado esos meses y riego de emergencia, el cual
en base al balance hídrico se estima el uso solo de 10 días entre los meses de marzo y abril.

**5.3** **Concentración de odorantes**

Tal como se mencionó en la metodología, los resultados de la modelación de dispersión de
olor, fueron evaluados a través de curvas de dispersión e iso-concentración en toda el área
de estudio.

A continuación, se presentan las curvas de dispersión e iso-concentración de olor en
unidades de olor (uo/m [3] ), como concentración horaria, correspondiente al percentil 98 anual
de los promedios horarios.

En la Figura 17, se observa la dispersión de olores producidos por el Proyecto. Los resultados
de la modelación sugieren que:

1) Las plumas de dispersión (presentes para el Proyecto y zona de riego de emergencia)

presentan una forma ovalada, con una leve inclinación en la dispersión de los
contaminantes hacia el noreste. Pese a lo anterior esta, no posee una dirección definida,
resultando las máximas concentraciones se localizan en una zona de pradera no
habitada. Esto último puede estar asociado a las bajas velocidades de vientos de la zona
y la topografía de ésta.
2) La pluma de dispersión presenta concentraciones modelas que van desde 1,00 uo/m3 a

3,02 uo/m3.
3) El área total que abarca la pluma comprende 257 hectáreas de las cuales 101 ha

corresponden al proyecto y 156 ha a la zona de riego de emergencia.
4) En la figura anterior se observa que el punto de máximo impacto se encuentra fuera del

área de proyecto, dirigiéndose levemente al noreste, en una zona de pradera no
habitada, lo que se considera un resultado favorable.

En la Figura 18, se observa la isoconcentración de olores del proyecto, de lo que se puede
destacar lo siguiente:

1) La pluma que se simula producto de las concentraciones odorantes del Proyecto se

extiende desde la isodora de mayor concentración, hasta los 907 m por el norte y 695
m al sur, mientras que aquella simulada por la zona de riego de emergencia se extiende
hasta los 570 m por el norte y 556 m al sur; en estos lugares las concentraciones
modeladas son de 0,75 uo/m3 y representan una reducción del 75% de la
isoconcentración más alta modelada.

2) La isodora de mayor concentración abarca una superficie aproximada de 0,48 ha y la

concentración sería cercana a los 3,00 uo/m3. Esta isodora se simula a 20 m al noreste
del proyecto.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 30 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

**Figura 17. Dispersión de Odorantes**

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 31 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

**Figura 18. Curvas de iso-concentración horaria**

**5.4** **Evaluación discreta de las emisiones de olor**

El objetivo de esta evaluación es conocer, mediante el modelo CALPUFF, las concentraciones
de olor (uo/m [3] ), que pueden recibir los puntos o receptores discretos cercanos al proyecto.
La modelación discreta se realizó a 1,8 metros de altura con respecto al suelo para todos
los puntos receptores.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 32 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

**Concentración de olor (uo/m** **[3]** **)**

La siguiente tabla permite evaluar el aporte de las concentraciones de olor generadas en la
operación del proyecto.

**Tabla 8. Concentraciones de olor modeladas en receptores discretos (percentil**

**98) Norma UK**

|Contaminante|Estadístico y<br>Periodo|Receptor|Aporte de<br>Proyecto<br>(uo/m3)|Límite de<br>Norma UK<br>(uo/m3)|% Relación<br>Límite<br>Norma|
|---|---|---|---|---|---|
|Olor <br>|Percentil 98<br>anual de 1 hora|1|2,449|5|49|
|Olor <br>|Percentil 98<br>anual de 1 hora|2|0,944|5|19|
|Olor <br>|Percentil 98<br>anual de 1 hora|3|0,091|5|2|
|Olor <br>|Percentil 98<br>anual de 1 hora|4|0,062|5|1|
|Olor <br>|Percentil 98<br>anual de 1 hora|5|0,060|5|1|
|Olor <br>|Percentil 98<br>anual de 1 hora|6|0,053|5|1|
|Olor <br>|Percentil 98<br>anual de 1 hora|7|0,158|5|3|
|Olor <br>|Percentil 98<br>anual de 1 hora|8|0,034|5|1|
|Olor <br>|Percentil 98<br>anual de 1 hora|9|3,227|5|65|
|Olor <br>|Percentil 98<br>anual de 1 hora|10|1,615|5|32|
|Olor <br>|Percentil 98<br>anual de 1 hora|11|0,243|5|5|

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 33 de 38

Informe de Modelación Atmosférica Emisiones Odorantes

“Proyecto Planta de Elaboración de Quesos y Planta de

Tratamiento de Riles LACSUR.”

**Tabla 9. Concentraciones de olor modeladas en receptores discretos (percentil**

**98) Norma Holandesa**

|Contaminante|Estadístico y<br>Periodo|Receptor|Aporte de<br>Proyecto<br>(uo/m3)|Límite de<br>Norma<br>Holandesa<br>(uo/m3)|%<br>Relación<br>Límite<br>Norma|
|---|---|---|---|---|---|
|Olor|Percentil 98<br>anual de 1 hora|1|2,449|3,5|70|
|Olor|Percentil 98<br>anual de 1 hora|2|0,944|3,5|27|
|Olor|Percentil 98<br>anual de 1 hora|3|0,091|3,5|3|
|Olor|Percentil 98<br>anual de 1 hora|4|0,062|3,5|2|
|Olor|Percentil 98<br>anual de 1 hora|5|0,060|3,5|2|
|Olor|Percentil 98<br>anual de 1 hora|6|0,053|3,5|2|
|Olor|Percentil 98<br>anual de 1 hora|7|0,158|3,5|5|
|Olor|Percentil 98<br>anual de 1 hora|8|0,034|3,5|1|
|Olor|Percentil 98<br>anual de 1 hora|9|3,227|3,5|92|
|Olor|Percentil 98<br>anual de 1 hora|10|1,615|3,5|46|
|Olor|Percentil 98<br>anual de 1 hora|11|0,243|3,5|7|

En la tabla anterior se presentan las concentraciones modeladas en los 11 puntos o
receptores discretos cercanos al proyecto y zona de riego. Tal como se puede apreciar, el
receptor localizado en la parte norte (en relación a la localización del proyecto),
correspondiente a receptor 1, presenta la concentración de olor más alta modelada,
aportando 2,449 (uo/m [3] ) la cual se encuentra en un 51% inferior al límite establecido por
la normativa de Inglaterra y un 30% inferior en relación a la norma Holandesa.

De acuerdo a la zona de riego de emergencia, el receptor cuya concentración modelada
presenta su valor más alto, correspondería al receptor 9, el cual se encuentra al este de
dicha zona, y simula una concentración de 3,227 (uo/m [3] ), valor que es inferior a ambas
normativas analizadas. Cabe destacar que dicha zona de riego de emergencia, como su
nombre lo dice, sólo será utilizada en casos de emergencias, los cuales en un peor escenario
ocurrirían con un máximo de 10 días entre los meses de marzo y abril, por tanto, la
concentración de olor en dicho sector y específicamente en aquel receptor (9), podría tener
una incidencia del 2,7% de un año calendario. Sumado a lo anterior, cabe recalcar, que
esta zona de riego, es muy poco probable que sea utilizada.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 34 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

Con respecto a las normas internacionales, se concluye que para todos los receptores se
cumplen los límites establecidos por el Reino Unido (5 ou/m [3] ) y Holanda (3,5 ou/m [3] ).

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 35 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

# 6 Conclusiones

El presente estudio tuvo como objetivo, estimar y evaluar la dispersión atmosférica de las
emisiones de olor que generará el proyecto: **“Planta de Elaboración de Quesos y Planta**
**de Tratamiento de Riles LACSUR.”**, considerando las unidades críticas de emisión de
olores que tendrá la planta en operación y simulando el peor escenario posible. Para evaluar
el efecto de las eventuales emisiones futuras, generadas por las unidades críticas, se utilizó
un modelo de dispersión tipo puff, llamado CALPUFF, el cual es recomendado por el
Ministerio de Medio Ambiente en la Guía para el uso de modelos de calidad del aire en el
SEIA, publicada el año 2012. Cabe destacar que dado a que **no existe norma de olores**
**vigente en Chile**, se recurrió a normas internacionales, con el fin de poder comparar los
resultados obtenidos en la modelación. Las normas internacionales correspondieron a la del
Reino Unido (5 uo/m [3] ) y Holanda (3,5 uo/m [3] ).

Además, para el análisis de la modelación, es importante considerar que la concentración
en el aire de odorantes puede ser influenciada por diversos factores, entre los cuales están:
la tasa de emisión, las condiciones en que son liberados a la atmósfera, la topografía del
entorno, e indudablemente las condiciones meteorológicas; es decir, la dispersión y
concentración de odorantes queda determinado por las condiciones ambientales en donde
estos son liberados, como por ejemplo: gradiente de presión, gradiente de temperatura,
velocidad y dirección del viento (los que a su vez están influenciados por las características
topográficas del lugar), entre otros.

De acuerdo a los resultados obtenidos en la modelación se puede concluir que:

 - En relación a la estimación de emisiones de olor presentadas en la planta de RILes,
se prevé que esta generaría 369.180,71 uo/s, siendo la actividad de efluente
utilizado para riego de predio y riego de emergencia, aquellos que emiten mayores
unidades de olor, cada uno aportando con un 8,28% y 90,84%, respectivamente.
Los cuales en conjunto representan un 99,12%, lo cual está ligado directamente al
nivel de actividad que poseen, es decir, el área de disposición para riego
correspondiente a 28,15 ha.

Además, dentro del peor escenario (o caso más extremo), también se consideró
para el área de riego de emergencia utilizada en la modelación, toda la superficie
destinada dentro del proyecto de riego (25,8 ha), a modo de ser prolijos al momento
de evaluar la posible afectación a los receptores cercanos. Sin embargo, el área de
riego efectiva a utilizar corresponde al 10% del área total modelada, por lo que las
concentraciones provenientes de esta fuente se encuentran sobreestimadas.

 - Cabe destacar, que estas actividades de riego, ocurrirían sólo periódicamente, en el
primer caso del riego del predio, esta ocurriría en los meses de periodo estival y, en
el caso del riego de emergencia, este se realizaría solamente en los meses de marzo

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 36 de 38

Informe de Modelación Atmosférica Emisiones Odorantes
“Proyecto Planta de Elaboración de Quesos y Planta de
Tratamiento de Riles LACSUR.”

y abril, con un número aproximado de 10 días dentro de ese período (cuya incidencia
correspondería al 2,7% de un año calendario).

En base a lo anterior, es importante señalar que el peor escenario solo tendría
ocurrencia durante el mes de marzo, ya que en este mes habría emisión de la planta
de RILes exceptuando la piscina de acumulación la cual solo funcionará para el mes
de abril, además de ambos riegos, los cuales se encuentran a una distancia de 9
kilómetros aproximadamente, lo que implicaría que estas fuentes de olor no se
encuentran en el mismo sector y por lo tanto no generarían un efecto sinérgico,
haciendo que las concentraciones de odorantes que generan estas actividades no
afecten significativamente a la población aledaña.

Sumado a lo anterior, resulta importante destacar que en virtud de la periodicidad
que cuentan algunas fuentes, el escenario más probable (para los meses de mayo
a octubre) correspondería única y exclusivamente al uso de la planta de RILes
exceptuando la piscina de acumulación, para lo cual se estiman 1.828,81 uo/s.

Además, se concluye que:

 - La pluma de dispersión no sigue una dirección predominante, sin embargo, las
mayores concentraciones de olor se ubicaron en el sector noreste de la planta.

 - De acuerdo a las curvas de iso concentración modeladas, la máxima concentración
modelada es cerca a los 3 uo/m [3] y se simula a 20 m al noreste del. Este valor permite
concluir que las máximas concentraciones simuladas estarían en conformidad con
las normas de olor del Reino Unido (5 uo/m [3] ) y Holanda (3,5 uo/m [3] ).

 - Con respecto a los receptores discretos utilizados, se concluye que el receptor
localizado en la parte norte (en relación a la localización del proyecto),
correspondiente a receptor 1, presenta la concentración de olor más alta modelada,
aportando 2,449 (uo/m [3] ) la cual se encuentra en un 51% inferior al límite
establecido por la normativa de Inglaterra y un 30% inferior en relación a la norma
Holandesa. De acuerdo a la zona de riego de emergencia, el receptor cuya
concentración modelada presenta su valor más alto, correspondería al receptor 9, el
cual se encuentra al este de dicha zona, y simula una concentración de 3,227
(uo/m [3] ), valor que es inferior a ambas normativas.

Por lo cual, a partir de los resultados obtenidos se concluye que los olores producidos por
el funcionamiento de la Planta de RILes no generará un impacto significativo en la emisión
de odorantes en el lugar.

Asesoría y Consultoría Ambiente-Social SpA..

Concepción-Chile. Telf.: **41-3366142**
contacto@ambientesocial.cl • www.ambientesocial.cl

Página 37 de 38

# Informe elaborado por contanto@ekosambiente.cl Asesoría y Capacitación Ambiente Social SpA. Consultoría, asesoría y capacitaciones ambientales contacto@ambientesocial.cl www.ambientesocial.cl

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Coordenadas UTM del área de estudio. Datum WGS-84, Huso 18****

| Vértice | Este (m) | Norte (m) |
| --- | --- | --- |
| a | 639.715 | 5.483.356 |
| b | 654.715 | 5.483.356 |
| c | 639.715 | 5.498.356 |
| d | 654.715 | 5.498.356 |

**Tabla 2.: Factores de emisión****

| Descripción | Unidad del tratamiento | FE (uo/s-m2) |
| --- | --- | --- |
| Factor de emisión para olores/sistema de acceso y<br>pretratamiento/separador de partículas gruesas (en<br>área superficial) | Filtro parabólico | 7,5 |
| Factor de emisión para olores/sistema de acceso y<br>pretratamiento/selector (aireado) | <br>DAF | 6 |
| Factor de emisión para olores/línea de agua/estanque<br>de aireación/zona aeróbica/aireación en punto único<br>sin cobertura | Biofiltro | 2,5 |
| Fórmula<br>de<br>emisión<br>para<br>olores/línea<br>de<br>agua/sedimentador secundario (en área de acceso) | <br>Decantador | 1,65 |
| Fórmula<br>de<br>emisión<br>para<br>olores/línea<br>de<br>agua/sedimentador secundario (en área superficial y<br>puntos de descarga) | <br> <br>Piscina de Acumulación | 1,3 |
| Fórmula<br>de<br>emisión<br>para<br>olores/línea<br>de<br>agua/sedimentador secundario (en área superficial y<br>puntos de descarga) | Riego y Riego de<br>Emergencia | 1,3 |

**Tabla 3.: Ubicación y superficie de las unidades críticas de olores del proyecto****

| Unidad | Elevación (msnm) | Vértices | UTM, Huso 18, Datum WGS-84 | Col5 |
| --- | --- | --- | --- | --- |
| **Unidad** | **Elevación (msnm)** | **Vértices** | **Este (km)** | **Norte (km)** |
| Filtro parabólico | 132 | a | 647,816 | 5491,162 |
| Filtro parabólico | 132 | b | 647,820 | 5491,161 |
| Filtro parabólico | 132 | c | 647,817 | 5491,165 |
| Filtro parabólico | 132 | d | 647,821 | 5491,164 |
| DAF | 132 | a | 647,802 | 5491,165 |
| DAF | 132 | b | 647,813 | 5491,162 |
| DAF | 132 | c | 647,803 | 5491,168 |
| DAF | 132 | d | 647,814 | 5491,165 |
| Biofiltro | 131 | a | 647,800 | 5491,180 |
| Biofiltro | 131 | b | 647,815 | 5491,176 |
| Biofiltro | 131 | c | 647,810 | 5491,218 |
| Biofiltro | 131 | d | 647,825 | 5491,215 |
| Decantador | 130 | a | 647,820 | 5491,217 |
| Decantador | 130 | b | 647,824 | 5491,216 |
| Decantador | 130 | c | 647,820 | 5491,220 |
| Decantador | 130 | d | 647,825 | 5491,219 |
| Piscina de Acumulación | 131 | a | 647,766 | 5491,134 |
| Piscina de Acumulación | 131 | b | 647,781 | 5491,128 |
| Piscina de Acumulación | 131 | c | 647,740 | 5491,085 |
| Piscina de Acumulación | 131 | d | 647,756 | 5491,076 |
| Riego | 123 | a | 647,477 | 5491,569 |
| Riego | 123 | b | 647,893 | 5491,176 |
| Riego | 123 | c | 647,508 | 5491,602 |
| Riego | 123 | d | 647,918 | 5491,199 |
| Riego de Emergencia I | 107 | a | 644,503 | 5488,415 |
| Riego de Emergencia I | 107 | b | 644,622 | 5488,464 |
| Riego de Emergencia I | 107 | c | 644,532 | 5488,155 |
| Riego de Emergencia I | 107 | d | 644,693 | 5488,163 |
| Riego de Emergencia II | 95 | a | 644,674 | 5488,570 |

**Tabla 4.: Fuentes y características de emisión de olor del proyecto****

| Descripción | Unidad del<br>tratamiento | FE<br>(uo/sm2) | Superficie<br>(m2) | Emisión<br>(uo/s) | Tipo de<br>Fuente | Régimen<br>Anual | Régimen<br>Diario |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Factor de emisión para<br>olores/sistema<br>de<br>acceso<br>y <br>pretratamiento/<br>separador de partículas<br>gruesas (en área <br>superficial) | Filtro<br>parabólico | 7,5 | 12,7 | 95,25 | Areal | Constante | 24 horas |
| Factor de emisión para<br>olores/sistema<br>de<br>acceso<br>y <br>pretratamiento/selector<br>(aireado) | DAF | 6 | 35,3 | 211,8 | Areal | Constante | 24 horas |
| Factor de emisión para<br>olores/línea<br>de<br>agua/estanque<br>de<br>aireación/zona<br>aeróbica/aireación<br>en<br>punto<br>único<br>sin<br>cobertura | Biofiltro | 2,5 | 600 | 1.500 | Areal | Constante | 24 horas |
| Fórmula<br>de<br>emisión<br>para olores/línea de<br>agua/sedimentador<br>secundario (en área de<br>acceso) | Decantador | 1,65 | 12,7 | 20,96 | Areal | Constante | 24 horas |

**Tabla 5: Características de receptores discretos****

| RECEPTOR | Coord. UTM 18 G | Col3 | DISTANCIA<br>AL PROYECTO<br>(m) | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| **RECEPTOR ** | **Este** | **Norte** | **Norte** | **Norte** |
| 1 | 647.680 | 5.491.513 | 320 | Vivienda ubicada al lado norponiente del Proyecto |
| 2 | 647.515 | 5.491.671 | 540 | Vivienda ubicada al lado norponiente del Proyecto |
| 3 | 647.073 | 5.491.915 | 1.015 | Vivienda ubicada al lado norponiente del Proyecto |
| 4 | 647.212 | 5.492.387 | 1.310 | Vivienda ubicada al lado norponiente del Proyecto |
| 5 | 646.585 | 5.490.920 | 1.175 | Vivienda ubicada al lado surponiente del Proyecto |
| 6 | 646.840 | 5.490.640 | 1.000 | Vivienda ubicada al lado surponiente del Proyecto |
| 7 | 648.497 | 5.490.810 | 716 | Vivienda ubicada al lado suroriente del Proyecto |
| 8 | 648.571 | 5.491.670 | 867 | Vivienda ubicada al lado nororiente del Proyecto |
| 9 | 645.232 | 5.488.531 | 140 | Vivienda ubicada al lado este del área de riego de<br>emergencia |
| 10 | 644.723 | 5.488.732 | 175 | Vivienda ubicada al lado noreste del área de riego<br>de emergencia |
| 11 | 644.305 | 5.488.108 | 262 | Lechería ubicada al este de zona de riego de<br>emergencia |

**Tabla 6.: Normativa internacional para concentraciones de olor****

| País | Concentración máxima (percentil 98<br>anual, promedio 1 hora) |
| --- | --- |
| Reino Unido (Norma IPPCH4) | 5,0 (uo/m3) |
| Holanda (Netherlands Emission Guidelines for<br>Air) | 3,5 (uo/m3) |

**Tabla 7.: Vientos estacionales WRF Osorno, 2019****

| Estación | Dirección de<br>Vector<br>Resultante | Velocidades y<br>Calmas (m/s) | Frecuencia % |
| --- | --- | --- | --- |
| Verano | OSO (24%) | 0,5-2,1 | 39,1 |
| Verano | OSO (24%) | 2,1-3,6 | 25,0 |
| Verano | OSO (24%) | 3,6-5,7 | 24,7 |
| Verano | OSO (24%) | 5,7-8,8 | 6,0 |
| Verano | OSO (24%) | Calma | 4,6 |
| Otoño | NNO (7%) | 0,5-2,1 | 47,8 |
| Otoño | NNO (7%) | 2,1-3,6 | 16,4 |
| Otoño | NNO (7%) | 3,6-5,7 | 14,0 |
| Otoño | NNO (7%) | 5,7-8,8 | 8,9 |
| Otoño | NNO (7%) | Calma | 10,0 |
| Invierno | NNO (8%) | 0,5-2,1 | 39,8 |
| Invierno | NNO (8%) | 2,1-3,6 | 22,5 |
| Invierno | NNO (8%) | 3,6-5,7 | 18,0 |
| Invierno | NNO (8%) | 5,7-8,8 | 11,2 |
| Invierno | NNO (8%) | Calma | 5,8 |
| Primavera | O (37%) | 0,5-2,1 | 33,4 |
| Primavera | O (37%) | 2,1-3,6 | 19,7 |
| Primavera | O (37%) | 3,6-5,7 | 30,1 |
| Primavera | O (37%) | 5,7-8,8 | 10,4 |
| Primavera | O (37%) | Calma | 5,6 |

**Tabla 8.: Concentraciones de olor modeladas en receptores discretos (percentil****

| Contaminante | Estadístico y<br>Periodo | Receptor | Aporte de<br>Proyecto<br>(uo/m3) | Límite de<br>Norma UK<br>(uo/m3) | % Relación<br>Límite<br>Norma |
| --- | --- | --- | --- | --- | --- |
| Olor <br> | Percentil 98<br>anual de 1 hora | 1 | 2,449 | 5 | 49 |
| Olor <br> | Percentil 98<br>anual de 1 hora | 2 | 0,944 | 5 | 19 |
| Olor <br> | Percentil 98<br>anual de 1 hora | 3 | 0,091 | 5 | 2 |
| Olor <br> | Percentil 98<br>anual de 1 hora | 4 | 0,062 | 5 | 1 |
| Olor <br> | Percentil 98<br>anual de 1 hora | 5 | 0,060 | 5 | 1 |
| Olor <br> | Percentil 98<br>anual de 1 hora | 6 | 0,053 | 5 | 1 |
| Olor <br> | Percentil 98<br>anual de 1 hora | 7 | 0,158 | 5 | 3 |
| Olor <br> | Percentil 98<br>anual de 1 hora | 8 | 0,034 | 5 | 1 |
| Olor <br> | Percentil 98<br>anual de 1 hora | 9 | 3,227 | 5 | 65 |
| Olor <br> | Percentil 98<br>anual de 1 hora | 10 | 1,615 | 5 | 32 |
| Olor <br> | Percentil 98<br>anual de 1 hora | 11 | 0,243 | 5 | 5 |

**Tabla 9.: Concentraciones de olor modeladas en receptores discretos (percentil****

| Contaminante | Estadístico y<br>Periodo | Receptor | Aporte de<br>Proyecto<br>(uo/m3) | Límite de<br>Norma<br>Holandesa<br>(uo/m3) | %<br>Relación<br>Límite<br>Norma |
| --- | --- | --- | --- | --- | --- |
| Olor | Percentil 98<br>anual de 1 hora | 1 | 2,449 | 3,5 | 70 |
| Olor | Percentil 98<br>anual de 1 hora | 2 | 0,944 | 3,5 | 27 |
| Olor | Percentil 98<br>anual de 1 hora | 3 | 0,091 | 3,5 | 3 |
| Olor | Percentil 98<br>anual de 1 hora | 4 | 0,062 | 3,5 | 2 |
| Olor | Percentil 98<br>anual de 1 hora | 5 | 0,060 | 3,5 | 2 |
| Olor | Percentil 98<br>anual de 1 hora | 6 | 0,053 | 3,5 | 2 |
| Olor | Percentil 98<br>anual de 1 hora | 7 | 0,158 | 3,5 | 5 |
| Olor | Percentil 98<br>anual de 1 hora | 8 | 0,034 | 3,5 | 1 |
| Olor | Percentil 98<br>anual de 1 hora | 9 | 3,227 | 3,5 | 92 |
| Olor | Percentil 98<br>anual de 1 hora | 10 | 1,615 | 3,5 | 46 |
| Olor | Percentil 98<br>anual de 1 hora | 11 | 0,243 | 3,5 | 7 |
