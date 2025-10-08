---
title: Sin título
author: Pc
date: D:20230518092538-04'00'
language: es
type: report
pages: 21
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - BALANCE DE MASAS PARA EL MANEJO DE RILES Y LODO. PISCICULTURA SAN PABLO Elaborado por: DESARROLLOS ACUÍCOLAS SAN PABLO SpA Abril, 2023
-->

# BALANCE DE MASAS PARA EL MANEJO DE RILES Y LODO. PISCICULTURA SAN PABLO Elaborado por: DESARROLLOS ACUÍCOLAS SAN PABLO SpA Abril, 2023

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

**ÍNDICE**

1. IDENTIFICACIÓN ..................................................................................................... 2

2. OBJETIVO.......................................................................................................................................... 2

3. MEMORIA DE CÁLCULO EFLUENTE..................................................................... 2

3.1. CUANTIFICACIÓN DE CAUDALES Y COMPOSICIONES CRUDAS.......................... 3

3.2. COMPOSICIONES RIL TRATADO.................................................................... 9

4. MEMORIA DE CÁLCULOS LODOS...................................................................................... 11

4.1. LODOS CRUDOS (F3).................................................................................... 11

4.2. LODOS CONCENTRADOS POR SEDIMENTADOR (F5).......................................... 12

5. ITERACIÓN PARA INCLUIR RETORNO.................................................................... 15

6. ANÁLISIS LEGAL................................................................................................ 18

ANEXOS............................................................................................................... 21

ANEXO 1. PLAN DE PRODUCCIÓN

ANEXO 2. CATALOGO TÉCNICO DEL ALIMENTO NUTRA FRY

ANEXO 3. FILTRATION AND REUSE OF WATER IN FISH FARMING, HYDROTECH AB

 - 1

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

**1.** **IDENTIFICACIÓN.**

Institución Mandante: Desarrollos Acuícolas San Pablo SpA.
R.U.T. de la Empresa: 99.544.470-4
Dirección Oficina: La Capellanía 1661, Lo Barnechea.
Región: Región Metropolitana.

**2.** **OBJETIVO.**

Se realiza el balance de masas para el manejo de residuos líquidos y lodos del proyecto
Piscicultura San Pablo con el objetivo de calcular los parámetros fisicoquímicos a la salida
del sistema de tratamiento mecánico por Filtros Rotatorios, los cuales se emplearán en el
modelo bidimensional de contaminantes en el cuerpo receptor. Además, estos resultados se
compararán con la normativa vigente (D.S. No90. Norma de Emisión para la Regulación de
Contaminantes Asociados a las Descargas de Residuos Líquidos a Aguas Marinas y
Continentales Superficiales).

**3.** **MEMORIA DE CÁLCULO EFLUENTE.**

El Proyecto Piscicultura San Pablo consiste en la construcción y operación de un centro de
cultivo (Piscicultura) de flujo abierto para una producción máxima anual de 2.622 ton/año
de salmónidos a cosecha. El Proyecto considera la implementación de 108 estanques de
350m [3] cada uno, con una capacidad instalada de 37.800 m [3], para la crianza de salmónidos
desde 3 hasta 250 gramos de peso promedio, con una proyección de generación anual de
biomasa de 3.614 ton/año (850 Ton stock + 2.622 ton/año de biomasa a cosecha + 142
ton/año mortalidad proyectada).

Se considera como especies objetivo el grupo de especies salmónidos, principalmente:
Salmón del Atlántico (Salmo salar), Trucha Arcoíris (Oncorhynchus mykiss) y Salmón
Coho (Oncorhynchus kisutch), en el cual se desarrollarán el cultivo de alevines hasta smolt,
en ciclo abierto.

El centro de cultivo será de flujo abierto, requiriendo 10 m [3] /s de agua (en periodo peak)
para mantener los procesos de cultivo. El Proyecto considera el abastecimiento de agua
dulce desde un derecho de aprovechamiento de aguas de carácter no consuntivo desde el
Río Pilmaiquén otorgado por Res DGA 196/08 por 10.000 lt/seg (10 m [3] /s).

Se presenta el Plan de Producción en Anexo 1. A continuación, el resumen del Plan de
Producción en Tabla 1.

 - 2

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

**Tabla 1.** Resumen Alimento según Planificación para Año de Máxima Producción.

|Col1|ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Grupo 1|1.264|0|35.130|**50.796**|77.012|94.212|111.530|119.865|134.348|143.540|145.313|1.264|
|Grupo 2|119.865|134.348|143.540|**145.313**|1.264|0|35.130|50.796|77.012|94.212|111.530|119.865|
|Grupo 3|50.796|77.012|94.212|**111.530**|119.865|134.348|143.540|145.313|1.264|0|35.130|50.796|
|Total Mes|171.925|211.360|272.882|**307.639**|198.141|228.560|290.200|315.974|212.624|237.752|291.973|171.925|
|Total Día|5.546|7.549|8.803|**10.255**|6.392|7.619|9.361|10.193|7.087|7.669|9.732|5.546|

Fuente: Información Extraida de Plan de Producción del Titular, presentado en Anexo 1 del presente documento.

Realizando un análisis estacional, la programación productiva establecida para el Proyecto
Piscicultura San Pablo establece que el escenario más desfavorable ambientalmente se
producirá en otoño, específicamente en el mes abril. Por ende, en base a la alimentación de
abril, con 10.255Kg diarios, se cuantifican cargas y concentraciones iniciales y posteriores
al sistema de tratamiento.

**3.1.** **CUANTIFICACIÓN DE CAUDALES Y COMPOSICIONES CRUDAS.**

Para cuantificar calidad de efluente final se debe simular el escenario con máxima

producción para obtener el caso más crítico desde un punto de vista ambiental. En este
contexto, el alimento suministrado en capacidad máxima correspondiente a un caudal de
10000l/s con un alimento mensual de 307.639Kg, correspondiente al mes de abril. A
continuación, se presentan los principales valores de entrada al balance.

**Tabla 2.** Principales valores de entrada al balance.

|Variable|Valor|Unidad|
|---|---|---|
|Caudal|10.000|l/s|
|Mes Máxima Alimentación|Abril|Mes|
|Máxima Alimentación|307.639|kg/mes|
|Máxima Alimentación|10.255|Kg/día|

Para obtener la composición del efluente, se emplean los siguientes supuestos:

- La carga total de contaminantes del efluente depende del alimento y de la tasa de

conversión. Para el flujo de producción del presente proyecto el alimento no consumido
representa el 10% del alimento suministrado.

- El alimento suministrado se cuantifica en el Plan de Producción presentado en Anexo 1,

el cual se elabora según parámetros propios del proyecto, como etapas productivas,
tamaños de peces por etapa y temperatura del agua.

 - 3

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

- Se empleará un alimento con valores promedios de 51% en proteína, 20% en grasa, 8%

Humedad, 8% Nitrógeno, 1,3% Fósforo y 9.5% Cenizas (Ver Anexo 2. Catálogo
Técnico del Alimento).

- El alimento consumido corresponde al 90% del alimento suministrado.

- El flujo másico de fecas representa el 13% del alimento consumido.

- El flujo másico de orina representa el 12% del alimento consumido.

- Las fecas se constituyen en un 70% de cenizas, por lo cual solo el 30% restante es

posible de ser oxidado.

- La orina se constituye de un 50% de nitrógeno en forma de urea. El resto, está

constituido por agua y sales minerales.

- Se asume la condición de estado estacionario.

A continuación, se presenta la identificación de las fuentes de aporte al efluente.

**Tabla 3.** Cuantificación de las fuentes de aporte al efluente.

|Variable|Valor|Unidad|
|---|---|---|
|Mes Máxima Alimentación|Abril|Mes|
|Máxima Alimentación|307.639|kg/mes|
|Max. Alimento Suministrado|10.255|Kg/día|
|Caudal Máximo|10,0|m3/s|
|Alimento Consumido (0.90)|9229|Kg/día|
|Alimento No Consumido (0.10)|1025|Kg/día|
|Flujo de Fecas (0.13 sobre el alimento consumido)|1200|Kg/día|
|Flujo de Orina (0.12 sobre el alimento consumido)|1108|Kg/día|
|Sólidos Suspendidos Totales<br>(Alimento no consumido + Flujo de Fecas)|2225|Kg/día|

Se considera un alimento de alta eficiencia, el cual tiene una alta disponibilidad actual en el
mercado nacional, el cual corresponde a alimento pelletizado, extruído, altamente
energético, con bajo contenido de fósforo, alta digestibilidad y enriquecido con
suplementos vitamínicos (vitamina C) y minerales. Estos pellets corresponden a la marca
de alimento de peces Nutra Fry 5 y Nutra Fry 15 de la empresa Skretting o similar (Ver
Catálogo Técnico del Alimento en Anexo 2).

Para determinar concentraciones, se considera la distribución química del alimento de
empresa Skretting, presentada en tabla 4. En la misma tabla se presenta una segunda

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- - 4 B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO . -->

**Tabla 4: ** . Composición y porcentaje en alimento.**

| Parámetro | Valor % peso Nutra Fry<br>5/15 | Valor % peso, Ref* |
| --- | --- | --- |
| ~~Proteína~~<br> | ~~**51**~~<br> | ~~50~~<br> |
| ~~Lípidos~~<br> | ~~**20**~~<br> | ~~20~~<br> |
| ~~Humedad~~<br> | ~~**8 **~~<br> | ~~10~~<br> |
| ~~Nitrógeno~~<br> | ~~**8 **~~<br> | ~~8 ~~<br> |
| ~~Fósforo~~<br> | ~~**1,30**~~<br> | ~~1,3~~<br> |
| ~~Ceniza~~<br> | ~~**9,2**~~<br> | ~~10~~<br> |
| ~~Otros~~ | ~~**2,2**~~ | ~~0.7~~ |

<!-- Estadísticas: 7 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Referencia*: Jensen A. Marine Ecotoxicological Tests with Seaweeds. In: Ecotoxicological Testing For The Marine Environment. G. Persoone, E. Jaspers, and C. Claus (Eds). State Univ. Ghent and Inst. Mar. Scient. Res., Bredene. Belgium: 1984; 1: 798. -->
<!-- FIN TABLA 4 -->

distribución a modo de referencia.

 - 4

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

**Tabla 4** . Composición y porcentaje en alimento.

|Parámetro|Valor % peso Nutra Fry<br>5/15|Valor % peso, Ref*|
|---|---|---|
|~~Proteína~~<br>|~~**51**~~<br>|~~50~~<br>|
|~~Lípidos~~<br>|~~**20**~~<br>|~~20~~<br>|
|~~Humedad~~<br>|~~**8 **~~<br>|~~10~~<br>|
|~~Nitrógeno~~<br>|~~**8 **~~<br>|~~8 ~~<br>|
|~~Fósforo~~<br>|~~**1,30**~~<br>|~~1,3~~<br>|
|~~Ceniza~~<br>|~~**9,2**~~<br>|~~10~~<br>|
|~~Otros~~|~~**2,2**~~|~~0.7~~|

Referencia*: Jensen A. Marine Ecotoxicological Tests with Seaweeds. In: Ecotoxicological Testing For The Marine
Environment. G. Persoone, E. Jaspers, and C. Claus (Eds). State Univ. Ghent and Inst. Mar. Scient. Res., Bredene.
Belgium: 1984; 1: 798.

Considerando los criterios y supuestos descritos anteriormente, los valores de Tabla 3 y la
composición del alimento Skretting de Tabla 4, se obtienen los flujos másicos para cada
uno de los constituyentes químicos que determinarán la demanda teórica de oxígeno (Tabla
5).

**Tabla** **5.** Flujos Másicos de los Constituyentes del Residuo Total.

|PARÁMETRO|VALOR|UNIDAD|
|---|---|---|
|Proteína|21,79|kg/h|
|Lípidos|8,55|kg/h|
|Nitrógeno|26,49|kg/h|
|Fósforo|0,56|kg/h|
|Cenizas|39,05|kg/h|
|SST|92,72|kg/h|

*Los sólidos suspendidos totales (SST) se obtienen de la suma de
fecas y alimento no consumido presentado en Tabla 3.

Con excepción a las cenizas, los compuestos presentados en Tabla 5 conforman la fracción
orgánica de los residuos líquidos que la actividad emitirá. Los sólidos totales representan la
fase de gran parte de dicha fracción de materia orgánica. Esta fracción se oxida ocupando el
oxígeno disuelto del agua a diferentes tasas, las que obedecen a las reacciones químicas de
oxidación como se muestra a continuación para cada componente.

_**Cálculo DTeO Proteínas.**_

Se calcula la Demanda Biológica de Oxígeno como Demanda Teórica de Oxígeno
empleando una proteína estándar constituida de 200 aminoácidos.

Como el peso molecular promedio de un aminoácido es de 75 gProteína/mol, considerando
una proteína de 200 aminoácidos como lo señala el referido texto anterior, un mol de
proteína pesa 15.000 gramos (200 aminoácidos * 75 gProteína/mol). Por otra parte, los
pesos moleculares de las diferentes proteínas varían entre 5500 y 220.000 (Revista de

 - 5

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

Divulgación Científica y Tecnológica de la Asociación Ciencia Hoy. Volumen 5 - No29).
En este contexto, para el análisis presente, el empleo del peso de 15.000 gramos por mol de
proteína, es aplicable. A continuación, se presentan las siguientes reacciones de oxidación.

Reacción igualada de la demanda de oxígeno por carbono:

##  CH 2 ( NH 2 ) COOH  200 + 300 O 2 → 200 NH 3 + 400 CO 2 + 200 H 2 O

Reacción igualada de demanda de oxígeno por nitrógeno:

_NH_ 3 + _O_ 2 → _HNO_ 2 + _H_ 2 _O_

_HNO_ 2 + _O_ 2 → _HNO_ 3

_NH_ + [3 ] _O_

3 2

2 [→] _[HNO]_ 3 [+] _[H ]_ 2 _[O ]_

Para la demanda de oxígeno por proteínas, los valores son los siguientes:

**Tabla** **6.** Resumen Cálculo Demanda de Oxígeno por Proteína.

|PARÁMETRO|VALOR|UNIDAD|
|---|---|---|
|Peso molecular proteína|15.000|g/gmol<br>|
|DteO por proteína|0,0075|~~gO~~2~~/g proteína~~|
|Proteína Total|21791|g/h<br>|
|DteO|162,7|~~g O~~2~~/h~~|

_**Cálculo DteO Lípidos (Grasas).**_

Independiente a la cantidad de grasa a oxidar, se cumple por reacción estequiométrica que
se requiere 1 mol de oxígeno para oxidar 1 mol de grasa. Esto se debe porque el sujeto de
oxidación es el terminal CH 2 cercano a la instauración, con formación de hidroperóxido.

Así, se utiliza la siguiente grasa estándar:

### 1 mol . grasa + 1 molO 2 → CO 2 + H 2 O

Para la demanda de oxígeno por lípidos, los valores son los siguientes:

 - 6

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

**Tabla 7.** Resumen Cálculo Demanda de Oxígeno por Lípidos.

|PARÁMETRO|VALOR|UNIDAD|
|---|---|---|
|Peso molecular lípidos|7.500|g/gmol|
|Moles de lípidos|1,139|mol|
|Lípidos Totales|8546|g/h<br>|
|DteO|36,46|~~g O~~2~~/h~~|

_**Cálculo DteO Nitrógeno**_

Se estima que la demanda teórica de oxígeno debido a la oxidación del nitrógeno, esta dada
por el nitrógeno amoniacal, ya que la demanda teórica de oxígeno del nitrógeno orgánico
ya fue calculada con la proteína. Por ende, la reacción igualada de demanda de oxígeno por
nitrógeno, es la siguiente:

_NH_ 3 + _O_ 2 → _HNO_ 2 + _H_ 2 _O_

_HNO_ 2 + _O_ 2 → _HNO_ 3

_NH_ + [3 ] _O_

3 2

2 [→] _[HNO]_ 3 [+] _[H ]_ 2 _[O ]_

Para la demanda de oxígeno por nitrógeno, los valores son los siguientes:

**Tabla 8.** Resumen Cálculo Demanda de Oxígeno por Nitrógeno

|PARÁMETRO|VALOR|UNIDAD|
|---|---|---|
|Peso molecular amonio|17|g/gmol<br>|
|DteO por amonio|64|~~g O~~2~~/mol amonio.~~|
|Amonio Total|26491|g/h<br>|
|DteO|99731|~~g O~~2~~/h~~|

Por lo tanto, la Demanda Teórica de Oxígeno (DteO) total estará dada por la suma de las
demandas de oxígeno de cada uno de los tres componentes, y la expresión puede ser de la
siguiente forma:

_DTeO_ . _Total_ = _DTeO_ .Pr _oteina_ + _DTeO_ . _Lípidos_ + _DTeO_ . _Nitrógeno_

Reemplazando los valores de las tres tablas anteriores, se obtiene lo siguiente:

DTeO Total = 99. 930,5gO 2 /h

 - 7

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

Finalmente, expresándose en unidades de concentración y para un efluente de 10.000 l/s, la
demanda biológica de oxígeno del fluido es la siguiente:

DTeO Total = 2,78gO 2 /h

Retomando los valores presentados en Tabla 5 y agregando el resultado de la demanda
teórica de oxígeno, se presentan las cargas y concentraciones definitivas para el flujo que
alimenta al sistema de Filtros Rotatorios en tabla 9.

**Tabla 9.** Máximas cargas y concentraciones diarias Ril Crudo “Preliminar” (F1).

|PARÁMETRO|CARGA|UNIDAD|CONCENTRACIÓN|UNIDAD|
|---|---|---|---|---|
|Proteína|21,79|kg/h|0,61|mg/l|
|Lípidos<br>|8,55<br>|kg/h<br>|0,24<br>|mg/l<br>|
|~~Nitrógeno~~|~~26,49~~|~~kg/h~~|~~0,74~~|~~mg/l~~|
|Fósforo|0,56|kg/h|0,0154|mg/l|
|Cenizas|39,05|kg/h|1,08|mg/l|
|Sólidos Suspendidos T.<br>|92,72<br>|kg/h<br>|2,58<br>|mg/l<br>|
|~~DTeO~~|~~99,93~~|~~kg/h~~|~~2,78~~|~~mg/l~~|

Para convertir el valor de carga a concentración se emplea el caudal de 10.000l/s.

Se consideran valores “preliminares” debido a que el sistema de tratamiento de efluentes
contiene un flujo de retorno, el cual presenta concentraciones de los parámetros en análisis
(no es un flujo prístino) y en consecuencia, se agrega posteriormente al cálculo en forma de
iteración matemática.

 - 8

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

**3.2.** **COMPOSICIONES RIL TRATADO.**

A continuación, se presenta en Figura 1, el diagrama de flujos del sistema de tratamiento
propuesto.

**Figura 1.** Diagrama de flujo del sistema de tratamiento.

Donde:

F1: Ril Crudo o entrada al sistema

F2: Ril Tratado o restitución al Río

F3: Lodo Crudo del Sistema de tratamiento de RILes

F4: Retorno del sedimentador al Ril crudo antes de Filtros Rotatorios.

F5: Lodo Concentrado por el sedimentador, para el transporte a disposición final.

A partir de las composiciones del Ril Crudo (F1) presentadas en Tabla 9 y de las eficiencias
en remoción de los filtros rotatorios, se debe obtener la caracterización del Ril tratado (F2).
Para esto, se presenta en Tabla 10 los rangos publicados para la remoción de los principales
compuestos.

**Tabla 10.** Eficiencias de Filtros de Tambor Rotatorios.

|Compuesto|% Remoción*|% Remoción**|
|---|---|---|
|Sólidos Suspendidos Totales (SST)|60 a 95|80 a 90|
|Fósforo Total|40 a 75|70 a 80|
|Nitrógeno Total|10 a 85|20 a 50|
|Aceites y Grasas|5 a 15|-|
|DBO5|-|70 a 80|

Fuentes: * Catálogo Filtros Rotatorios Texinox. ** Filtration and reuse of
water in fish farming, Hydrotech AB, Suecia (Ver Anexo 3)

 - 9

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

Se homologan las eficiencias de remoción de cenizas (parámetro referencial no empleado
en el modelo bidimensional), para los Filtros rotatorios y después para sedimentación,
como iguales a los lípidos.

Siendo conservador dentro del rango de eficiencias, se emplea la siguiente distribución de
% de remoción:

**Tabla 11.** Eficiencias empleadas para Filtros Rotatorios.

|Compuesto|% Remoción|Observaciones|
|---|---|---|
|Proteína|70|Se asume como parte de la DBO<br>|
|Lípidos|45|~~Obtenido como la media de Carbono (DBO~~5~~) y N.~~|
|Nitrógeno|20|Mínimo del rango** Tabla 10.|
|Fósforo|70|Mínimo del rango** Tabla 10.|
|Cenizas|45|Se asume similar a Lípidos.|
|SST|80|Mínimo del rango** Tabla 10.|
|DBO5 (como DTeO)|70|Mínimo del rango** Tabla 10.|

Aplicando las remociones señaladas en Tabla 11 y asumiendo “Preliminarmente” que la
carga del retorno rebalse del sedimentador (F4) es despreciable, las cargas y
concentraciones para el RIL tratados (F2) se presentan a continuación.

**Tabla 12.** Máximas cargas y concentraciones diarias Ril Tratado “Preliminar” F2.

|PARÁMETRO|CARGA|UNIDAD|CONCENTRACIÓN|UNIDAD|
|---|---|---|---|---|
|Proteína|6,54|kg/h|0,18|mg/l|
|Lípidos|4,70|kg/h|0,13|mg/l|
|Nitrógeno|21,19|kg/h|0,59|mg/l|
|Fósforo|0,17|kg/h|0,00463|mg/l|
|Cenizas|21,48|kg/h|0,60|mg/l|
|Sólidos Suspendidos|18,54|kg/h|0,52|mg/l|
|DTeO|29,98|kg/h|0,83|mg/l|

Nota: Se consideran valores “preliminares” debido a que el sistema de tratamiento de
efluentes contiene un flujo de retorno, el cual presenta concentraciones de los parámetros
en análisis (no es un flujo prístino) y en consecuencia, se agrega posteriormente al cálculo
en forma de iteración matemática.

 - 10

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

**4.** **MEMORIA DE CÁLCULOS LODOS.**

**4.1.** **LODOS CRUDOS (F3).**

En la Piscicultura San Pablo se generará un flujo de lodos crudos (F3) en base seca de
74,18 Kg/día, provenientes de los 92,72Kg diarios de SST de entrada en F1 (Tabla 5) por el
80% de eficiencia en remoción en SST de los filtros rotatorios según lo presentado en Tabla
11.

Para obtener el flujo másico de lodos crudos F3 en base húmeda, se aplica una humedad
representativa final del 99,6% y una densidad relativa de 1,02. Bajo estos supuestos, el flujo
másico será de 18.180 litros/horas, equivalentes a 436m [3] /día. Estos valores se validan con
un caudal máximo de 0,36l/s del agua de retrolavado en régimen continuo (caso más
desfavorable) de cada uno de los 14 filtros rotatorios activos (no se consideran los dos
equipos de respaldo para este cálculo), los que generan 31,2m [3] /d cada uno, con un total de
435,5m [3] /d considerando las 14 unidades.

En la ecuación de la continuidad o de conservación de masa para volúmenes constantes al
interior de un sistema, ante condiciones estacionarias o de régimen permanente, la derivada
temporal en la ecuación se hace cero y todos los valores de Caudal y Concentración son
constantes. Por ende, el término simplificado será:

## +

Donde:

F 1 : Caudal de Ril Crudo, l/h
F 2 : Caudal Ril Tratado, l/h
F 3 : Caudal de Lodos Crudo, l/h
C 1 : Concentración determinado compuesto en Ril Crudo, mg/l
C 2 : Concentración determinado compuesto en Ril Tratado, mg/l
C 3 : Concentración determinado compuesto en Ril Lodos Crudo, mg/l

Para obtener las concentraciones de flujo de Lodo Crudo F3, se emplean los siguientes
valores:

- El valor de F1 es de 36.000.000l/h (proveniente de los 10m [3] /s presentados en tabla 2).

- El valor de F2 es de 18.180l/h según lo expuesto anteriormente, para una humedad del

99,6% y una densidad relativa de 1,02.

- Los valores calculados para C1 se presentaron en Tabla 9.

- Los valores calculados para C2 se presentaron en Tabla 12.

 - 11

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

Los resultados preliminares para el Flujo de Lodos Crudos F3, se presenta en la siguiente

tabla.

**Tabla 13.** Máximas cargas y concentraciones diarias Lodo Crudo “Preliminar” (F3).

|PARÁMETRO|CARGA|UNIDAD|CONCENTRACIÓN|UNIDAD|
|---|---|---|---|---|
|Proteína|15,25|kg/h|839|mg/l|
|Lípidos|3,85|kg/h|212|mg/l|
|Nitrógeno|5,30|kg/h|291|mg/l|
|Fósforo|0,39|kg/h|21|mg/l|
|Cenizas|17,57|kg/h|967|mg/l|
|Sólidos Suspendidos Tot.|74,18|kg/h|4080|mg/l|
|DTeO|69,95|kg/h|3848|mg/l|

**4.2.** **LODOS CONCENTRADOS POR SEDIMENTADOR (F5).**

Los sedimentadores consisten en estructuras diseñadas de tal manera de promover la
separación de partículas de diferentes densidades, esto por acción de la gravedad. Con esto
se disminuye la velocidad horizontal del flujo líquido, de tal forma de que la velocidad
vertical de sedimentación de la partícula sea mayor o igual, sedimentando esta y
clarificando el agua. En el caso particular de Piscicultura San Pablo, se dispondrá de un
sedimentador gravitacional laminar para los 18.180l/h (436m [3] /d) de lodos crudos (F3)
generados por el retrolavado de los filtros rotatorios. De esta forma se calcula a
continuación, mediante la ecuación de continuidad, las concentraciones y Flujos
“Preliminares” de lodos concentrados F5 y recirculación del mismo equipo (F4).

Los tanques de sedimentación primaria contribuyen de manera importante al tratamiento
del agua residual. Cuando se utilizan como único medio de tratamiento, su objetivo
principal es la eliminación de: 1) sólidos capaces de formar depósitos de fango en las aguas
receptoras; 2) aceite libre, grasas y otras materias flotantes, y 3) parte de la carga orgánica
vertida a las aguas receptoras. Cuando los tanques se emplean como paso previo de
tratamientos biológicos, el cual es el caso del proyecto, su función es la reducción de la
carga afluente a los reactores biológicos.

Las características del sedimentador de lodos, denominado en la DIA Piscicultura San
Pablo, como Cámara de lodos es la siguiente:

 - 12

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

_Los sólidos producto del retrolavado del sistema de tratamiento del efluente, serán_
_dispuestos en un estanque de concreto armado, con hormigón H25, con adición de aditivo_
_impermeabilizante, a bajo nivel, de 100 m_ _[3]_ _de capacidad (DIA Piscicultura San Pablo)._

Para obtener rangos de eficiencias en los principales parámetros, se emplea la metodología
descrita por Crites y Tchobanoglous, 2000 y Metcalf & Eddy, 1996.

La expresión establecida por Crites y Tchobanoglous, 2000 se obtiene a partir de
observaciones realizadas a sedimentadores en funcionamiento, generando información
acerca de la eficiencia en la remoción de DBO y SST en tanques de sedimentación
primaria, como función de la concentración del afluente y el tiempo de retención.

Lo anterior puede modelarse matemáticamente como una hipérbola regular usando la
siguiente expresión:

Donde

R = porcentaje de remoción de DBO ó SST esperado, %
t = tiempo de retención, h
a,b = constantes empíricas

De acuerdo a Crites y Tchobanoglous (2000), las constantes a y b pueden tomar los
siguientes valores a 20oC (Tabla 14):

**Tabla 14.** Valores de las constantes empíricas a y b.

|Variable|a|b|
|---|---|---|
|DBO|0,018|0,020|
|SST|0,0075|0,014|

Fuente: Crites y Tchobanoglous, 2000.

El tiempo de retención para el sedimentador de Piscicultura San Pablo será de 5,5 horas
para un flujo de ingreso F3 de 436m [3] /d y un volumen de 100m [3] de sedimentador.

Reemplazando los términos a y b, para un t=5,5h, las eficiencias son las siguientes:

DBO: 42,97%
SST: 65,09%

 - 13

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

Finalmente, las eficiencias a emplear para el cálculo de salidas del sedimentador (F4 y F5)
se presentan en Tabla 15.

**Tabla 15.** Eficiencias empleadas para la Sedimentación.

|Compuesto|% Remoción|Observaciones|
|---|---|---|
|Proteína|42,97|Se asume como parte de la DBO|
|Lípidos|29,62|Obtenido como la media de Carbono (DBO5) y N.|
|Nitrógeno|16,27|Obtenido en la misma proporción N-SST que en<br>Tabla 11. Eficiencia Fitros Rotatorios|
|Fósforo|56,95|Obtenido en la misma proporción P-SST que en<br>Tabla 11. Eficiencia Fitros Rotatorios|
|Cenizas|29,62|Se asume similar a Lípidos.|
|SST|65,09|Metodología Crites y Tchobanoglous (2000)|
|DBO5 (como DTeO)|42,97|Metodología Crites y Tchobanoglous (2000)|

Fuente: Elaboración Propia.

Para obtener el flujo másico de lodos Concentrado en base húmeda F5, se aplica una
humedad representativa del 95% y una densidad relativa de 1,08. El flujo másico será de
894 litros/horas, equivalentes a 21,5m [3] /día. El flujo de recirculación F4 será de 17286l/h,
equivalente a 415m [3] /día.

Empleando la ecuación de continuidad, los resultados preliminares son los siguientes:

**Tabla 16.** Máximas cargas y concentraciones diarias Lodo Concentrado “Preliminar” (F5).

|PARÁMETRO|CARGA|UNIDAD|CONCENTRACIÓN|UNIDAD|
|---|---|---|---|---|
|Proteína|6,55|kg/h|7331|mg/l|
|Lípidos|1,14|kg/h|1274|mg/l|
|Nitrógeno|0,86|kg/h|964|mg/l|
|Fósforo|0,22|kg/h|248|mg/l|
|Cenizas|5,21|kg/h|5822|mg/l|
|Sólidos Suspendidos Tot.|48,28|kg/h|54000|mg/l|
|DTeO|30,06|kg/h|33619|mg/l|

**Tabla 17.** Máximas cargas y concentraciones diarias recirculación 1 “Preliminar” (F4).

|PARÁMETRO|CARGA|UNIDAD|CONCENTRACIÓN|UNIDAD|
|---|---|---|---|---|
|Proteína|8,70|kg/h|503,26|mg/l|
|Lípidos|2,71|kg/h|156,57|mg/l|
|Nitrógeno|4,44|kg/h|256,63|mg/l|
|Fósforo|0,17|kg/h|9,68|mg/l|
|Cenizas|12,37|kg/h|715,51|mg/l|
|Sólidos Suspendidos Tot.|25,90|kg/h|1498,03|mg/l|
|DTeO|9,16|kg/h|1775,92|mg/l|

 - 14

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

**5.** **ITERACIÓN PARA INCLUIR RETORNO.**

Las concentraciones y Flujos “Preliminares” de F1 a F5 presentados en Tablas anteriores
tienen como principal supuesto “que no existen los Retornos asociados a la Recirculación
del sedimentador (F4 en diagrama de flujos Figura 1)”. Vale decir, las concentraciones de
F4 no inciden en aporte de cargas sobre F1 Ril crudo de entrada al sistema.

Dado que este supuesto realmente es significativo dentro del funcionamiento de los
sistemas de tratamiento de RILes y Lodos, es que en se realiza una iteración matemática
aplicando la función repetidamente, usando la salida de una iteración como la entrada a la
siguiente, de tal forma de asumir la significancia de los retornos.

De forma explicativa, la primera ronda de resultados, la cual se presenta en Tablas
anteriores como “Preliminares”, arroja valores de flujo y concentración para el retorno F4.
Luego en la segunda iteración se adiciona al flujo de entrada F1 las cargas (g/l) de F4 para
obtener un nuevo resultado. Esta operación se repite tantas veces como sea necesario para
que las concentraciones de F2 (RIL Tratado) se hagan contantes respecto a la iteración
anterior. Esto resultó en la séptima iteración.

Los resultados finales y definitivos son los siguientes:

**Tabla 18.** Máximas cargas y concentraciones diarias Ril Crudo “Definitivo” (F1)

|PARÁMETRO|CARGA|UNIDAD|CONCENTRACIÓN|UNIDAD|
|---|---|---|---|---|
|Proteína|29,22|kg/h|0,81|mg/l|
|Lípidos|10,49|kg/h|0,29|mg/l|
|Nitrógeno|28,91|kg/h|0,80|mg/l|
|Fósforo|0,70|kg/h|0,02|mg/l|
|Cenizas|47,94|kg/h|1,33|mg/l|
|Sólidos Suspendidos Tot.|116,92|kg/h|3,25|mg/l|
|DTeO|134,00|kg/h|3,72|mg/l|

**Tabla 19.** Máximas cargas y concentraciones diarias Ril Tratado “Definitivo” F2.

|PARÁMETRO|CARGA|UNIDAD|CONCENTRACIÓN|UNIDAD|
|---|---|---|---|---|
|Proteína|8,77|kg/h|**0,244**|mg/l|
|Lípidos|5,77|kg/h|**0,160**|mg/l|
|Nitrógeno|23,13|kg/h|**0,643**|mg/l|
|Fósforo|0,21|kg/h|**0,006**|mg/l|
|Cenizas|26,37|kg/h|**0,733**|mg/l|
|Sólidos Suspendidos Tot.|23,38|kg/h|**0,650**|mg/l|
|DTeO|40,20|kg/h|**1,117**|mg/l|

 - 15

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

**Tabla 20.** Máximas cargas y concentraciones diarias Lodo Crudo “Definitivo” (F3).

|PARÁMETRO|CARGA|UNIDAD|CONCENTRACIÓN|UNIDAD|
|---|---|---|---|---|
|Proteína|13,03|kg/h|766|mg/l|
|Lípidos|2,78|kg/h|163|mg/l|
|Nitrógeno|3,36|kg/h|198|mg/l|
|Fósforo|0,34|kg/h|20|mg/l|
|Cenizas|12,69|kg/h|747|mg/l|
|Sólidos Suspendidos Tot.|69,33|kg/h|4080|mg/l|
|DTeO|59,73|kg/h|3515|mg/l|

**Tabla 21.** Máximas cargas y concentraciones diarias recirculación 1 “Definitivo” (F4).

|PARÁMETRO|CARGA|UNIDAD|CONCENTRACIÓN|UNIDAD|
|---|---|---|---|---|
|Proteína|7,43|kg/h|459,74|mg/l|
|Lípidos|1,95|kg/h|120,91|mg/l|
|Nitrógeno|2,82|kg/h|174,36|mg/l|
|Fósforo|0,15|kg/h|9,17|mg/l|
|Cenizas|8,93|kg/h|552,57|mg/l|
|Sólidos Suspendidos Tot.|24,21|kg/h|1498,03|mg/l|
|DTeO|34,07|kg/h|2108,29|mg/l|

**Tabla 22.** Máximas cargas y concentraciones diarias Lodo Concentrado “Definitivo” (F5).

|PARÁMETRO|CARGA|UNIDAD|CONCENTRACIÓN|UNIDAD|
|---|---|---|---|---|
|Proteína|5,60|kg/h|6697|mg/l|
|Lípidos|0,82|kg/h|984|mg/l|
|Nitrógeno|0,55|kg/h|655|mg/l|
|Fósforo|0,20|kg/h|235|mg/l|
|Cenizas|3,76|kg/h|4496|mg/l|
|Sólidos Suspendidos Tot.|45,13|kg/h|54000|mg/l|
|DTeO|25,67|kg/h|30712|mg/l|

Finalmente, la distribución de flujos asociada a cada corriente F1 al F5, se presenta en
Tabla 23.

**Tabla 23.** Flujos definitivos de cada corriente, m [3] /día.

|SIMBOLOGÍA|DESCRIPCIÓN|FLUJO, m3/d|
|---|---|---|
|F1|RIL Crudo|864000|
|F2|RIL Tratado|863592|
|F3|Lodo Crudo|407,85|
|F4|Recirculación 1|387,79|
|F5|Lodo Concentrado|20,06|

 - 16

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

A modo de Ejemplo, se presenta en la siguiente tabla los valores y diferencias porcentuales
entre las concentraciones del Ril tratado F2 “Preliminar” y el “Iterado” (este último
considera el retorno).

**Tabla 24.** Aumento de concentraciones del RIL tratado por efecto del Retornos F4.

|SIMBOLOGÍA|Concentración,<br>mg/l Preliminar|Concentración Final,<br>mg/l Iterada|Incremento<br>por Retornos, %|
|---|---|---|---|
|Proteína|0,18|0,24|34|
|Lípidos|0,13|0,16|23|
|Nitrógeno|0,59|0,64|9|
|Fósforo|0,0046|0,01|27|
|Cenizas|0,60|0,73|23|
|Sólidos S. Tot.|0,52|0,65|26|
|DTeO|0,83|1,12|34|
|Promedio Incremento por Retornos|Promedio Incremento por Retornos|Promedio Incremento por Retornos|25|

Nota: Todas las cargas y concentraciones señaladas en las tables “Definitivas” para F1 a
F5 corresponden a valores de aporte y no al efluente final. Para los valores de efluente
final, se debe adicionar las concentraciones del afluente de la piscicultura (agua de
ingreso o línea de base) provenientes de Tabla 8 de capítulo 2.4 de “Informe Datos de
Entrada, Modelo Bidimensional de Contaminantes en Cuerpo Receptor, Piscicultura San
Pablo”.

Nótese que se considera una tolerancia del 50% sobre el aporte Piscicultura sobre el RIL
Tratado, como se presenta en cuarta columna de la Tabla 25. De esta forma, los
resultados finales del balance de masa contendrán un 50% de margen y constituirán los
parámetros objetivos de operación de la planta de RILES, como se establece en la
Observación 1.18 de ICSARA Complementario.

**Tabla 25.** Aporte Ril Tratado F2, 50% Margen de Tolerancia y Aporte Total.

|CONTAMINANTES|UNIDAD|Aporte a RIL<br>TRATADO<br>(Tabla 19 Balance<br>Masa)|Tolerancia<br>50% Sobre<br>Aporte|Aporte a RIL<br>TRATADO<br>con Tolerancia|
|---|---|---|---|---|
|Aceites y Grasas (Lípidos)|mg/l|0,16|0,08|**0,240**|
|Nitrógeno|mg/l|0,643|0,3215|**0,965**|
|Fósforo|mg/l|0,006|0,003|**0,009**|
|Sólidos Suspendidos Totales|mg/l|0,65|0,325|**0,975**|
|Demanda Biológica de Oxígeno|mg/l|1,117|0,5585|**1,676**|

 - 17

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

A continuación, la Tabla 26 presenta los valores finales para el RIL o efluente tratado.
Nótese que se ordena alfabéticamente el listado de parámetros para la siguiente tabla.

**Tabla 26.** Concentraciones Finales Efluente.

|CONTAMINANTES|UNIDAD|Aporte a RIL<br>TRATADO<br>con Tolerancia|Concentraciones<br>en el Río (línea<br>de base)*|Total, Efluente|
|---|---|---|---|---|
|Aceites y Grasas (Lípidos)|mg/l|0,240|2,0025|**2,243**|
|DBO5|mg/l|1,676|1,0008|**2,676**|
|Fósforo|mg/l|0,009|0,0137|**0,023**|
|Nitrógeno|mg/l|0,965|0,0418|**1,006**|
|Sólidos Suspendidos Totales|mg/l|0,975|1,806|**2,781**|

- Tabla 13 Capítulo 2.3 “Informe Datos de Entrada, Modelo Bidimensional de
Contaminantes en Cuerpo Receptor, Piscicultura San Pablo”.

**6.** **ANÁLISIS LEGAL.**

Para verificar, mediante los resultados obtenidos en el presente balance de masas, si el
establecimiento es o no fuente emisora, se cita parte de la _**Tabla Establecimiento Emisor**_
del cuerpo legal DS 90. Establece Norma de Emisión Para la Regulación de Contaminantes
Asociados a las Descargas de Residuos Líquidos a Aguas Marinas y Continentales
Superficiales.

**Tabla 27.** Fragmento tabla _**Establecimiento Emisor**_ del cuerpo legal DS No90.

|Contaminante|Valor Característico|Carga contaminante media diaria<br>(equiv. 100 Hab/día)|
|---|---|---|
|~~Aceites y Grasas (Lípidos)~~|~~60 mg/L~~|~~960 g/d~~|
|Nitrógeno total|50 mg/L|800 g/d|
|Fósforo Total<br>|10 mg/L<br>|160 g/d<br>|
|~~Sólidos Suspendidos Totales~~|~~220 mg/L~~|~~3520 g/d~~|
|DBO5|250 mg O2/L|4000 g/d|

Comparando los valores de Tabla 9 (RIL Crudo sin carga de afluente o línea de base) con
las cargas de la normativa (Tabla 27), se concluye lo siguiente:

 - 18

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

**Tabla 28.** Comparación de cargas de RIL Crudo con cuerpo legal.

|Contaminante|Carga contaminante<br>media diaria (equiv. 100<br>Hab/día)|Carga del Ril Crudo* g/d|
|---|---|---|
|~~Aceites y Grasas (Lípidos)~~|~~960 g/d~~|~~205.093~~|
|Nitrógeno total|800 g/d|635.787|
|Fósforo Total<br>|160 g/d<br>|13.331<br>|
|~~Sólidos Suspendidos Totales~~<br>|~~3520 g/d~~|~~2.225.255~~|
|~~DBO~~5|4000 g/d|2.398.332|

 - Valores obtenidos de Tabla 9 transformando cargas de kg/h a g/d. Nótese que para
este análisis solo se consideran valores “preliminares” para evitar incorporar el
retorno del sedimentador del sistema de tratamiento y así solo considerar las
concentraciones fuentes.

Cabe destacar que la Piscicultura San Pablo será Fuente Emisora según lo establece el DS
N°90.

En cuanto al cumplimiento de concentraciones en el efluente o Ril Tratado, se cita
fragmento de _**Tabla No1 Límites Máximos Permitidos para la Descarga de Residuos**_
_**Líquidos a Cuerpos de Agua Fluviales, DS N°90.**_

**Tabla 29.** Fragmento de _**Tabla No 1**_ del cuerpo legal DS No90.

|CONTAMINANTES|UNIDAD|EXPRESION|LIMITE MAXIMO<br>PERMITIDO|
|---|---|---|---|
|~~Aceites y Grasas (Lípidos)~~|~~mg/l~~|~~A y G~~|~~20~~|
|Nitrógeno total|mg/l|NTK|50|
|Fósforo<br>|mg/l<br>|P <br>|10<br>|
|~~Sólidos Suspendidos Totales~~|~~mg/l~~|~~SST~~<br>|~~80~~|
|Demanda Biológica de Oxígeno|mg/l|~~DBO~~5|35|

Como resumen se presenta en Tabla 30 la comparación de concentraciones teóricas entre el
Ril Tratado F2 (Tabla 26) y la normativa ambiental vigente.

**Tabla 30.** Comparación de concentraciones de efluente con cuerpo legal.

|CONTAMINANTES|UNIDAD|LIMITE<br>MAXIMO<br>PERMITIDO|RIL<br>TRATADO*|
|---|---|---|---|
|Aceites y Grasas (Lípidos)<br>|mg/l<br>|20<br>|**2,243**<br>|
|~~DBO~~5|~~mg/l~~|~~35~~|~~**2,676**~~|
|Fósforo|mg/l|10|**0,023**|
|Nitrógeno|mg/l|50|**1,006**|
|Sólidos Suspendidos Totales|mg/l|80|**2,781**|

 - Valores obtenidos de última columna Tabla 26.

 - 19

B ALANCE DE M ASAS PARA EL M ANEJO DE R ILES Y L ODO, P ISCICULTURA S AN P ABLO .

Como se presenta anteriormente para los escenarios más desfavorable ambientalmente en la
proyección del centro y así como se deberá verificar mediante las analíticas mensuales de
monitoreo y autocontrol, Piscicultura San Pablo se mantiene por debajo los parámetros
establecidos como máximos en el DS N°90.

**Los valores de concentración presentados en última columna de Tabla 30, serán los**
**que se deberán emplear para el desarrollo del modelo bidimensional de contaminantes**
**en el cuerpo receptor.**

M.Sc. CHRISTIAN HERRERA CÁRDENAS

INGENIERO AMBIENTAL - INGENIERO CIVIL INDUSTRIAL

RUT: 10.056.935-3

 - 20

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: ** Resumen Alimento según Planificación para Año de Máxima Producción.**

| Col1 | ene | feb | mar | abr | may | jun | jul | ago | sep | oct | nov | dic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Grupo 1 | 1.264 | 0 | 35.130 | **50.796** | 77.012 | 94.212 | 111.530 | 119.865 | 134.348 | 143.540 | 145.313 | 1.264 |
| Grupo 2 | 119.865 | 134.348 | 143.540 | **145.313** | 1.264 | 0 | 35.130 | 50.796 | 77.012 | 94.212 | 111.530 | 119.865 |
| Grupo 3 | 50.796 | 77.012 | 94.212 | **111.530** | 119.865 | 134.348 | 143.540 | 145.313 | 1.264 | 0 | 35.130 | 50.796 |
| Total Mes | 171.925 | 211.360 | 272.882 | **307.639** | 198.141 | 228.560 | 290.200 | 315.974 | 212.624 | 237.752 | 291.973 | 171.925 |
| Total Día | 5.546 | 7.549 | 8.803 | **10.255** | 6.392 | 7.619 | 9.361 | 10.193 | 7.087 | 7.669 | 9.732 | 5.546 |

**Tabla 2.: ** Principales valores de entrada al balance.**

| Variable | Valor | Unidad |
| --- | --- | --- |
| Caudal | 10.000 | l/s |
| Mes Máxima Alimentación | Abril | Mes |
| Máxima Alimentación | 307.639 | kg/mes |
| Máxima Alimentación | 10.255 | Kg/día |

**Tabla 3.: ** Cuantificación de las fuentes de aporte al efluente.**

| Variable | Valor | Unidad |
| --- | --- | --- |
| Mes Máxima Alimentación | Abril | Mes |
| Máxima Alimentación | 307.639 | kg/mes |
| Max. Alimento Suministrado | 10.255 | Kg/día |
| Caudal Máximo | 10,0 | m3/s |
| Alimento Consumido (0.90) | 9229 | Kg/día |
| Alimento No Consumido (0.10) | 1025 | Kg/día |
| Flujo de Fecas (0.13 sobre el alimento consumido) | 1200 | Kg/día |
| Flujo de Orina (0.12 sobre el alimento consumido) | 1108 | Kg/día |
| Sólidos Suspendidos Totales<br>(Alimento no consumido + Flujo de Fecas) | 2225 | Kg/día |

**Tabla 7.: ** Resumen Cálculo Demanda de Oxígeno por Lípidos.**

| PARÁMETRO | VALOR | UNIDAD |
| --- | --- | --- |
| Peso molecular lípidos | 7.500 | g/gmol |
| Moles de lípidos | 1,139 | mol |
| Lípidos Totales | 8546 | g/h<br> |
| DteO | 36,46 | ~~g O~~2~~/h~~ |

**Tabla 8.: ** Resumen Cálculo Demanda de Oxígeno por Nitrógeno**

| PARÁMETRO | VALOR | UNIDAD |
| --- | --- | --- |
| Peso molecular amonio | 17 | g/gmol<br> |
| DteO por amonio | 64 | ~~g O~~2~~/mol amonio.~~ |
| Amonio Total | 26491 | g/h<br> |
| DteO | 99731 | ~~g O~~2~~/h~~ |

**Tabla 9.: ** Máximas cargas y concentraciones diarias Ril Crudo “Preliminar” (F1).**

| PARÁMETRO | CARGA | UNIDAD | CONCENTRACIÓN | UNIDAD |
| --- | --- | --- | --- | --- |
| Proteína | 21,79 | kg/h | 0,61 | mg/l |
| Lípidos<br> | 8,55<br> | kg/h<br> | 0,24<br> | mg/l<br> |
| ~~Nitrógeno~~ | ~~26,49~~ | ~~kg/h~~ | ~~0,74~~ | ~~mg/l~~ |
| Fósforo | 0,56 | kg/h | 0,0154 | mg/l |
| Cenizas | 39,05 | kg/h | 1,08 | mg/l |
| Sólidos Suspendidos T.<br> | 92,72<br> | kg/h<br> | 2,58<br> | mg/l<br> |
| ~~DTeO~~ | ~~99,93~~ | ~~kg/h~~ | ~~2,78~~ | ~~mg/l~~ |

**Tabla 10.: ** Eficiencias de Filtros de Tambor Rotatorios.**

| Compuesto | % Remoción* | % Remoción** |
| --- | --- | --- |
| Sólidos Suspendidos Totales (SST) | 60 a 95 | 80 a 90 |
| Fósforo Total | 40 a 75 | 70 a 80 |
| Nitrógeno Total | 10 a 85 | 20 a 50 |
| Aceites y Grasas | 5 a 15 | - |
| DBO5 | - | 70 a 80 |

**Tabla 11.: ** Eficiencias empleadas para Filtros Rotatorios.**

| Compuesto | % Remoción | Observaciones |
| --- | --- | --- |
| Proteína | 70 | Se asume como parte de la DBO<br> |
| Lípidos | 45 | ~~Obtenido como la media de Carbono (DBO~~5~~) y N.~~ |
| Nitrógeno | 20 | Mínimo del rango** Tabla 10. |
| Fósforo | 70 | Mínimo del rango** Tabla 10. |
| Cenizas | 45 | Se asume similar a Lípidos. |
| SST | 80 | Mínimo del rango** Tabla 10. |
| DBO5 (como DTeO) | 70 | Mínimo del rango** Tabla 10. |

**Tabla 12.: ** Máximas cargas y concentraciones diarias Ril Tratado “Preliminar” F2.**

| PARÁMETRO | CARGA | UNIDAD | CONCENTRACIÓN | UNIDAD |
| --- | --- | --- | --- | --- |
| Proteína | 6,54 | kg/h | 0,18 | mg/l |
| Lípidos | 4,70 | kg/h | 0,13 | mg/l |
| Nitrógeno | 21,19 | kg/h | 0,59 | mg/l |
| Fósforo | 0,17 | kg/h | 0,00463 | mg/l |
| Cenizas | 21,48 | kg/h | 0,60 | mg/l |
| Sólidos Suspendidos | 18,54 | kg/h | 0,52 | mg/l |
| DTeO | 29,98 | kg/h | 0,83 | mg/l |

**Tabla 13.: ** Máximas cargas y concentraciones diarias Lodo Crudo “Preliminar” (F3).**

| PARÁMETRO | CARGA | UNIDAD | CONCENTRACIÓN | UNIDAD |
| --- | --- | --- | --- | --- |
| Proteína | 15,25 | kg/h | 839 | mg/l |
| Lípidos | 3,85 | kg/h | 212 | mg/l |
| Nitrógeno | 5,30 | kg/h | 291 | mg/l |
| Fósforo | 0,39 | kg/h | 21 | mg/l |
| Cenizas | 17,57 | kg/h | 967 | mg/l |
| Sólidos Suspendidos Tot. | 74,18 | kg/h | 4080 | mg/l |
| DTeO | 69,95 | kg/h | 3848 | mg/l |

**Tabla 14.: ** Valores de las constantes empíricas a y b.**

| Variable | a | b |
| --- | --- | --- |
| DBO | 0,018 | 0,020 |
| SST | 0,0075 | 0,014 |

**Tabla 15.: ** Eficiencias empleadas para la Sedimentación.**

| Compuesto | % Remoción | Observaciones |
| --- | --- | --- |
| Proteína | 42,97 | Se asume como parte de la DBO |
| Lípidos | 29,62 | Obtenido como la media de Carbono (DBO5) y N. |
| Nitrógeno | 16,27 | Obtenido en la misma proporción N-SST que en<br>Tabla 11. Eficiencia Fitros Rotatorios |
| Fósforo | 56,95 | Obtenido en la misma proporción P-SST que en<br>Tabla 11. Eficiencia Fitros Rotatorios |
| Cenizas | 29,62 | Se asume similar a Lípidos. |
| SST | 65,09 | Metodología Crites y Tchobanoglous (2000) |
| DBO5 (como DTeO) | 42,97 | Metodología Crites y Tchobanoglous (2000) |

**Tabla 16.: ** Máximas cargas y concentraciones diarias Lodo Concentrado “Preliminar” (F5).**

| PARÁMETRO | CARGA | UNIDAD | CONCENTRACIÓN | UNIDAD |
| --- | --- | --- | --- | --- |
| Proteína | 6,55 | kg/h | 7331 | mg/l |
| Lípidos | 1,14 | kg/h | 1274 | mg/l |
| Nitrógeno | 0,86 | kg/h | 964 | mg/l |
| Fósforo | 0,22 | kg/h | 248 | mg/l |
| Cenizas | 5,21 | kg/h | 5822 | mg/l |
| Sólidos Suspendidos Tot. | 48,28 | kg/h | 54000 | mg/l |
| DTeO | 30,06 | kg/h | 33619 | mg/l |

**Tabla 17.: ** Máximas cargas y concentraciones diarias recirculación 1 “Preliminar” (F4).**

| PARÁMETRO | CARGA | UNIDAD | CONCENTRACIÓN | UNIDAD |
| --- | --- | --- | --- | --- |
| Proteína | 8,70 | kg/h | 503,26 | mg/l |
| Lípidos | 2,71 | kg/h | 156,57 | mg/l |
| Nitrógeno | 4,44 | kg/h | 256,63 | mg/l |
| Fósforo | 0,17 | kg/h | 9,68 | mg/l |
| Cenizas | 12,37 | kg/h | 715,51 | mg/l |
| Sólidos Suspendidos Tot. | 25,90 | kg/h | 1498,03 | mg/l |
| DTeO | 9,16 | kg/h | 1775,92 | mg/l |

**Tabla 18.: ** Máximas cargas y concentraciones diarias Ril Crudo “Definitivo” (F1)**

| PARÁMETRO | CARGA | UNIDAD | CONCENTRACIÓN | UNIDAD |
| --- | --- | --- | --- | --- |
| Proteína | 29,22 | kg/h | 0,81 | mg/l |
| Lípidos | 10,49 | kg/h | 0,29 | mg/l |
| Nitrógeno | 28,91 | kg/h | 0,80 | mg/l |
| Fósforo | 0,70 | kg/h | 0,02 | mg/l |
| Cenizas | 47,94 | kg/h | 1,33 | mg/l |
| Sólidos Suspendidos Tot. | 116,92 | kg/h | 3,25 | mg/l |
| DTeO | 134,00 | kg/h | 3,72 | mg/l |

**Tabla 19.: ** Máximas cargas y concentraciones diarias Ril Tratado “Definitivo” F2.**

| PARÁMETRO | CARGA | UNIDAD | CONCENTRACIÓN | UNIDAD |
| --- | --- | --- | --- | --- |
| Proteína | 8,77 | kg/h | **0,244** | mg/l |
| Lípidos | 5,77 | kg/h | **0,160** | mg/l |
| Nitrógeno | 23,13 | kg/h | **0,643** | mg/l |
| Fósforo | 0,21 | kg/h | **0,006** | mg/l |
| Cenizas | 26,37 | kg/h | **0,733** | mg/l |
| Sólidos Suspendidos Tot. | 23,38 | kg/h | **0,650** | mg/l |
| DTeO | 40,20 | kg/h | **1,117** | mg/l |

**Tabla 20.: ** Máximas cargas y concentraciones diarias Lodo Crudo “Definitivo” (F3).**

| PARÁMETRO | CARGA | UNIDAD | CONCENTRACIÓN | UNIDAD |
| --- | --- | --- | --- | --- |
| Proteína | 13,03 | kg/h | 766 | mg/l |
| Lípidos | 2,78 | kg/h | 163 | mg/l |
| Nitrógeno | 3,36 | kg/h | 198 | mg/l |
| Fósforo | 0,34 | kg/h | 20 | mg/l |
| Cenizas | 12,69 | kg/h | 747 | mg/l |
| Sólidos Suspendidos Tot. | 69,33 | kg/h | 4080 | mg/l |
| DTeO | 59,73 | kg/h | 3515 | mg/l |

**Tabla 21.: ** Máximas cargas y concentraciones diarias recirculación 1 “Definitivo” (F4).**

| PARÁMETRO | CARGA | UNIDAD | CONCENTRACIÓN | UNIDAD |
| --- | --- | --- | --- | --- |
| Proteína | 7,43 | kg/h | 459,74 | mg/l |
| Lípidos | 1,95 | kg/h | 120,91 | mg/l |
| Nitrógeno | 2,82 | kg/h | 174,36 | mg/l |
| Fósforo | 0,15 | kg/h | 9,17 | mg/l |
| Cenizas | 8,93 | kg/h | 552,57 | mg/l |
| Sólidos Suspendidos Tot. | 24,21 | kg/h | 1498,03 | mg/l |
| DTeO | 34,07 | kg/h | 2108,29 | mg/l |

**Tabla 22.: ** Máximas cargas y concentraciones diarias Lodo Concentrado “Definitivo” (F5).**

| PARÁMETRO | CARGA | UNIDAD | CONCENTRACIÓN | UNIDAD |
| --- | --- | --- | --- | --- |
| Proteína | 5,60 | kg/h | 6697 | mg/l |
| Lípidos | 0,82 | kg/h | 984 | mg/l |
| Nitrógeno | 0,55 | kg/h | 655 | mg/l |
| Fósforo | 0,20 | kg/h | 235 | mg/l |
| Cenizas | 3,76 | kg/h | 4496 | mg/l |
| Sólidos Suspendidos Tot. | 45,13 | kg/h | 54000 | mg/l |
| DTeO | 25,67 | kg/h | 30712 | mg/l |

**Tabla 23.**

| SIMBOLOGÍA | DESCRIPCIÓN | FLUJO, m3/d |
| --- | --- | --- |
| F1 | RIL Crudo | 864000 |
| F2 | RIL Tratado | 863592 |
| F3 | Lodo Crudo | 407,85 |
| F4 | Recirculación 1 | 387,79 |
| F5 | Lodo Concentrado | 20,06 |

**Tabla 24.: ** Aumento de concentraciones del RIL tratado por efecto del Retornos F4.**

| SIMBOLOGÍA | Concentración,<br>mg/l Preliminar | Concentración Final,<br>mg/l Iterada | Incremento<br>por Retornos, % |
| --- | --- | --- | --- |
| Proteína | 0,18 | 0,24 | 34 |
| Lípidos | 0,13 | 0,16 | 23 |
| Nitrógeno | 0,59 | 0,64 | 9 |
| Fósforo | 0,0046 | 0,01 | 27 |
| Cenizas | 0,60 | 0,73 | 23 |
| Sólidos S. Tot. | 0,52 | 0,65 | 26 |
| DTeO | 0,83 | 1,12 | 34 |
| Promedio Incremento por Retornos | Promedio Incremento por Retornos | Promedio Incremento por Retornos | 25 |

**Tabla 25.: ** Aporte Ril Tratado F2, 50% Margen de Tolerancia y Aporte Total.**

| CONTAMINANTES | UNIDAD | Aporte a RIL<br>TRATADO<br>(Tabla 19 Balance<br>Masa) | Tolerancia<br>50% Sobre<br>Aporte | Aporte a RIL<br>TRATADO<br>con Tolerancia |
| --- | --- | --- | --- | --- |
| Aceites y Grasas (Lípidos) | mg/l | 0,16 | 0,08 | **0,240** |
| Nitrógeno | mg/l | 0,643 | 0,3215 | **0,965** |
| Fósforo | mg/l | 0,006 | 0,003 | **0,009** |
| Sólidos Suspendidos Totales | mg/l | 0,65 | 0,325 | **0,975** |
| Demanda Biológica de Oxígeno | mg/l | 1,117 | 0,5585 | **1,676** |

**Tabla 26.: ** Concentraciones Finales Efluente.**

| CONTAMINANTES | UNIDAD | Aporte a RIL<br>TRATADO<br>con Tolerancia | Concentraciones<br>en el Río (línea<br>de base)* | Total, Efluente |
| --- | --- | --- | --- | --- |
| Aceites y Grasas (Lípidos) | mg/l | 0,240 | 2,0025 | **2,243** |
| DBO5 | mg/l | 1,676 | 1,0008 | **2,676** |
| Fósforo | mg/l | 0,009 | 0,0137 | **0,023** |
| Nitrógeno | mg/l | 0,965 | 0,0418 | **1,006** |
| Sólidos Suspendidos Totales | mg/l | 0,975 | 1,806 | **2,781** |

**Tabla 27.: ** Fragmento tabla _**Establecimiento Emisor**_ del cuerpo legal DS No90.**

| Contaminante | Valor Característico | Carga contaminante media diaria<br>(equiv. 100 Hab/día) |
| --- | --- | --- |
| ~~Aceites y Grasas (Lípidos)~~ | ~~60 mg/L~~ | ~~960 g/d~~ |
| Nitrógeno total | 50 mg/L | 800 g/d |
| Fósforo Total<br> | 10 mg/L<br> | 160 g/d<br> |
| ~~Sólidos Suspendidos Totales~~ | ~~220 mg/L~~ | ~~3520 g/d~~ |
| DBO5 | 250 mg O2/L | 4000 g/d |

**Tabla 28.: ** Comparación de cargas de RIL Crudo con cuerpo legal.**

| Contaminante | Carga contaminante<br>media diaria (equiv. 100<br>Hab/día) | Carga del Ril Crudo* g/d |
| --- | --- | --- |
| ~~Aceites y Grasas (Lípidos)~~ | ~~960 g/d~~ | ~~205.093~~ |
| Nitrógeno total | 800 g/d | 635.787 |
| Fósforo Total<br> | 160 g/d<br> | 13.331<br> |
| ~~Sólidos Suspendidos Totales~~<br> | ~~3520 g/d~~ | ~~2.225.255~~ |
| ~~DBO~~5 | 4000 g/d | 2.398.332 |

**Tabla 29.: ** Fragmento de _**Tabla No 1**_ del cuerpo legal DS No90.**

| CONTAMINANTES | UNIDAD | EXPRESION | LIMITE MAXIMO<br>PERMITIDO |
| --- | --- | --- | --- |
| ~~Aceites y Grasas (Lípidos)~~ | ~~mg/l~~ | ~~A y G~~ | ~~20~~ |
| Nitrógeno total | mg/l | NTK | 50 |
| Fósforo<br> | mg/l<br> | P <br> | 10<br> |
| ~~Sólidos Suspendidos Totales~~ | ~~mg/l~~ | ~~SST~~<br> | ~~80~~ |
| Demanda Biológica de Oxígeno | mg/l | ~~DBO~~5 | 35 |

**Tabla 30.: ** Comparación de concentraciones de efluente con cuerpo legal.**

| CONTAMINANTES | UNIDAD | LIMITE<br>MAXIMO<br>PERMITIDO | RIL<br>TRATADO* |
| --- | --- | --- | --- |
| Aceites y Grasas (Lípidos)<br> | mg/l<br> | 20<br> | **2,243**<br> |
| ~~DBO~~5 | ~~mg/l~~ | ~~35~~ | ~~**2,676**~~ |
| Fósforo | mg/l | 10 | **0,023** |
| Nitrógeno | mg/l | 50 | **1,006** |
| Sólidos Suspendidos Totales | mg/l | 80 | **2,781** |
