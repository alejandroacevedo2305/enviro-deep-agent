---
title: Sin título
author: Andrés Burboa Lizama
date: D:20230707124548-04'00'
language: es
type: manual
pages: 31
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ESTUDIO DE INUNDACIÓN PARQUE FOTOVOLTAICO ZALDÍVAR
  - Contenidos
  - Figuras
  - Tablas
  - 1. Introducción
  - 2. Descripción del modelo
  - 3. Parámetros de entrada
  - n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)
  - n 3 : Coeficiente asociado al efecto relativo de las obstrucciones
  - 4. Resultados
  ... y 1 secciones más
-->

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
# ESTUDIO DE INUNDACIÓN PARQUE FOTOVOLTAICO ZALDÍVAR

para ZAPALERI SPA

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|07/07/2023|Revisión cliente|CJS|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comuna de Antofagasta<br>Región de Antofagasta|Col3|
|---|---|---|
||FPG-B22028(3)-EHID2-DOC-02.01.03|Rev. A|

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

# Contenidos

1. Introducción ......................................................................................................................................... 4

2. Descripción del modelo ...................................................................................................................... 4

3. Parámetros de entrada ...................................................................................................................... 5

3.1. Coeficiente de rugosidad .................................................................................................................... 5
3.2. Condiciones de borde e iniciales ....................................................................................................... 6

3.3. Otras Consideraciones .......................................................................................................................23

4. Resultados ......................................................................................................................................... 24

4.1. Tormenta periodo de retorno 100 años ....................................................................................... 24

5. Referencias ....................................................................................................................................... 30

# Figuras

Figura 2-1. Ejemplo de refinamiento de la malla de cálculo. Refinamiento cauces (negro), refinamiento línea

férrea (amarillo) .......................................................................................................................................................................5

Figura 3-1. Ubicación condiciones de borde ..................................................................................................................... 8

Figura 3-2. Ubicación condiciones de borde ..................................................................................................................... 9

Figura 3-3. Hidrograma de crecida CB AG_04_00 ........................................................................................................ 9

Figura 3-4. Hidrograma de crecida CB AG_04_01 ........................................................................................................ 10

Figura 3-5. Hidrograma de crecida CB AG_04_02 ........................................................................................................ 10

Figura 3-6. Hidrograma de crecida CB AG_05_00 ........................................................................................................ 11

Figura 3-7. Hidrograma de crecida CB AG_05_01 .......................................................................................................... 11

Figura 3-8. Hidrograma de crecida CB AG_05_02 ........................................................................................................ 12

Figura 3-9. Hidrograma de crecida CB AG_06_00 ....................................................................................................... 12

Figura 3-10.Hidrograma de crecida CB AG_06_01 ........................................................................................................ 13

Figura 3-11. Hidrograma de crecida CB AG_06_02 ....................................................................................................... 13

Figura 3-12. Hidrograma de crecida CB AG_06_03 ...................................................................................................... 14

Figura 3-13. Hidrograma de crecida CB AG_06_04 ...................................................................................................... 14

Figura 3-14. Hidrograma de crecida CB AG_06_05 ...................................................................................................... 15

Figura 3-15. Hidrograma de crecida CB AG_07_00 ...................................................................................................... 15

Figura 3-16. Hidrograma de crecida CB AG_07_01 ....................................................................................................... 16

Figura 3-17. Hidrograma de crecida CB AG_07_02 ....................................................................................................... 16

Figura 3-18. Hidrograma de crecida CB AG_07_03 ...................................................................................................... 17

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-19. Hidrograma de crecida CB AG_08_00 ..................................................................................................... 17

Figura 3-20. Hidrograma de crecida CB AG_08_01 ...................................................................................................... 18

Figura 3-21. Hidrograma de crecida CB AG_08_02 ...................................................................................................... 18

Figura 3-22. Hidrograma de crecida CB AG_08_03...................................................................................................... 19

Figura 3-23. Hidrograma de crecida CB AG_08_04 ..................................................................................................... 19

Figura 3-24. Hidrograma de crecida CB AG_08_05 .................................................................................................... 20

Figura 3-25. Hidrograma de crecida CB AG_08_06 .................................................................................................... 20

Figura 3-26. Hidrograma de crecida CB AG_08_07 ..................................................................................................... 21

Figura 3-27. Hidrograma de crecida CB AG_08_08 ..................................................................................................... 21

Figura 3-28. Hidrograma de crecida CB QC_00 .............................................................................................................22

Figura 3-29. Hidrograma de crecida CB QC_01 ..............................................................................................................22

Figura 3-30. Hidrograma de crecida CB QC_02 ............................................................................................................ 23

Figura 4-1. Profundidad máxima periodo de retorno 100 años. Área de generación (negro) .......................... 24

Figura 4-2. Profundidad máxima periodo de retorno 100 años. Sector 1 ............................................................... 25

Figura 4-3. Profundidad máxima periodo de retorno 100 años. Sector 2 .............................................................. 25

Figura 4-4. Profundidad máxima periodo de retorno 100 años. Sector 3.............................................................. 26

Figura 4-5. Profundidad máxima periodo de retorno 100 años. Sector 4.............................................................. 26

Figura 4-6. Velocidad máxima periodo de retorno 100 años. Área de generación (negro) ................................ 27

Figura 4-7. Velocidad máxima periodo de retorno 100 años. Sector 1 ..................................................................... 27

Figura 4-8. Velocidad máxima periodo de retorno 100 años. Sector 2 ................................................................... 28

Figura 4-9. Velocidad máxima periodo de retorno 100 años. Sector 3 ................................................................... 28

Figura 4-10. Velocidad máxima periodo de retorno 100 años. Sector 4 ................................................................. 29

# Tablas

Tabla 3-1. Condición de los cauces para el cálculo del coeficiente de Manning con método de Cowan ........... 6

Tabla 3-2. Condiciones de borde e iniciales ...................................................................................................................... 6

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

# 1. Introducción

A continuación, se detallan los antecedentes y metodología empleada para la construcción del modelo

hidráulico AG_Z3, que forma parte del estudio de inundación del Área de Generación (AG) y la Línea de Alta

Tensión (LAT) del proyecto Parque Fotovoltaico Zaldívar.

El modelo se basa en la topografía de detalle del proyecto, la cual fue representada mediante un Modelo

Digital de Terreno (MDT), que fue obtenido a partir de un vuelo fotogramétrico.

Se tomaron en cuenta los resultados del análisis hidrológico (Anexo 1), donde se consideró una tormenta de

duración de 6 horas y periodo de retorno de 100 años.

Los resultados obtenidos permiten conocer las características del eje hidráulico y las áreas de inundación. A

continuación, se presentan las consideraciones para elaborar el modelo y los principales resultados

obtenidos.

# 2. Descripción del modelo

Se construyó el modelo hidráulico de la Zona 3 (AG_Z3) empleando el software HEC-RAS (HEC, 2022),

representando la condición actual de los cauces y utilizando para su cálculo un flujo bidimensional.

El área de estudio AG_Z3 contiene los cauces de los grupos AG_04, AG_05, AG_06, AG_07, AG_08 y el

grupo de la Quebrada Chimborazo AG_QC. El modelo posee una malla general de resolución 6 x 6 m, la cual

fue refinada en los cauces presentes al interior del área de cálculo. Para esto, se utilizó como referencia la

red de drenaje obtenida a partir del MDT, generando una malla de 3 x 3 m en una extensión de 2 m hacia

cada lado de los cauces. Este procedimiento se realizó también en la línea férrea considerando una malla de

3 x 3 m en una extensión de 9 m hacia cada lado de la infraestructura, para representar el efecto que presenta

como barrera al flujo.

Se realizaron ingresos de caudal mediante el hidrograma de crecida de las cuencas de los grupos antes

mencionados.

A modo de ejemplo, se muestra la resolución de la malla en la siguiente figura:

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 2-1. Ejemplo de refinamiento de la malla de cálculo. Refinamiento cauces (negro), refinamiento línea

férrea (amarillo)

# 3. Parámetros de entrada

## 3.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2020)

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

# n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición de los cauces según los criterios del método:

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Tabla 3-1. Condición de los cauces para el cálculo del coeficiente de Manning con método de Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Moderado|n1|0.010|
|Variación de las secciones transversales|Alternándose<br>Ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Baja|n4|0.000|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.045|

## 3.2. Condiciones de borde e iniciales

Se definieron tres tipos de condiciones de borde (CB): (i) inicial o aguas arriba, (ii) intermedia y (iii) final o

aguas abajo. La CB de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés. Por

otro lado, parte del modelo posee una longitud de cauce significativa y sus caudales pueden variar bastante

entre su inicio y final, ya que el área drenante de su cuenca aumenta a medida que se avanza hacia aguas

abajo. En estos casos se agrega una CB intermedia, cuyo objetivo es añadir un incremento de caudal al

modelo para representar el aumento del caudal a lo largo del cauce. Por último, se incluye la CB aguas abajo

para permitir la salida del flujo.

La condición de borde aguas arriba e intermedia incluyen los hidrogramas de crecida de las cuencas asociadas

al periodo de retorno de 100 años. Además, las tres CB poseen condición de borde de altura normal,

definiendo el parámetro de pendiente normal a partir de la topografía del modelo. La pendiente y los

caudales peak de los cuatro periodos de retorno se presentan a continuación:

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|Tipo de CB|Caudal peak<br>[m3 /s]<br>0.21|Pendiente<br>[mm]<br>0.07|
|---|---|---|---|
|US_AG_04_00|Intermedia|Intermedia|Intermedia|
|US_AG_04_01|Intermedia|0.39|0.04|
|US_AG_04_02|Aguas arriba|0.34|0.07|
|US_AG_05_00|Intermedia|0.43|0.04|
|US_AG_05_01|Intermedia|0.17|0.04|

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

|Nombre CB|Tipo de CB|Caudal peak<br>[m3 /s]<br>0.33|Pendiente<br>[mm]<br>0.06|
|---|---|---|---|
|US_AG_05_02|Aguas arriba|Aguas arriba|Aguas arriba|
|US_AG_06_00|Intermedia|0.40|0.04|
|US_AG_06_01|Intermedia|1.06|0.04|
|US_AG_06_02|Intermedia|0.08|0.05|
|US_AG_06_03|Intermedia|1.83|0.01|
|US_AG_06_04|Intermedia|2.80|0.03|
|US_AG_06_05|Aguas arriba|3.09|0.05|
|US_AG_07_00|Intermedia|0.75|0.03|
|US_AG_07_01|Intermedia|1.04|0.03|
|US_AG_07_02|Intermedia|0.80|0.02|
|US_AG_07_03|Intermedia|0.57|0.03|
|US_AG_08_00|Intermedia|2.03|0.03|
|US_AG_08_01|Intermedia|2.43|0.03|
|US_AG_08_02|Intermedia|1.90|0.04|
|US_AG_08_03|Aguas arriba|0.14|0.04|
|US_AG_08_04|Aguas arriba|0.13|0.04|
|US_AG_08_05|Intermedia|2.14|0.04|
|US_AG_08_06|Aguas arriba|9.15|0.04|
|US_AG_08_07|Aguas arriba|0.44|0.05|
|US_AG_08_08|Aguas arriba|0.36|0.05|
|US_QC_00|Intermedia|28.59|0.03|
|US_QC_01|Intermedia|21.46|0.03|
|US_QC_02|Aguas arriba|216.99|0.02|
|DS_00|Aguas abajo|-|0.03|
|DS_01|Aguas abajo|-|0.03|
|DS_02|Aguas abajo|-|0.03|
|DS_03|Aguas abajo|-|0.03|

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

|Nombre CB|Tipo de CB|Caudal peak<br>[m3 /s]<br>-|Pendiente<br>[mm]<br>0.03|
|---|---|---|---|
|DS_04|Aguas abajo|Aguas abajo|Aguas abajo|

Por otro lado, la ubicación de las condiciones de borde y los hidrogramas de crecida se presentan en las

siguientes Figuras:

Figura 3-1. Ubicación condiciones de borde

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-2. Ubicación condiciones de borde

Figura 3-3. Hidrograma de crecida CB AG_04_00

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-4. Hidrograma de crecida CB AG_04_01

Figura 3-5. Hidrograma de crecida CB AG_04_02

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-6. Hidrograma de crecida CB AG_05_00

Figura 3-7. Hidrograma de crecida CB AG_05_01

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-8. Hidrograma de crecida CB AG_05_02

Figura 3-9. Hidrograma de crecida CB AG_06_00

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-10.Hidrograma de crecida CB AG_06_01

Figura 3-11. Hidrograma de crecida CB AG_06_02

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-12. Hidrograma de crecida CB AG_06_03

Figura 3-13. Hidrograma de crecida CB AG_06_04

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-14. Hidrograma de crecida CB AG_06_05

Figura 3-15. Hidrograma de crecida CB AG_07_00

15 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-16. Hidrograma de crecida CB AG_07_01

Figura 3-17. Hidrograma de crecida CB AG_07_02

16 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-18. Hidrograma de crecida CB AG_07_03

Figura 3-19. Hidrograma de crecida CB AG_08_00

17 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-20. Hidrograma de crecida CB AG_08_01

Figura 3-21. Hidrograma de crecida CB AG_08_02

18 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-22. Hidrograma de crecida CB AG_08_03

Figura 3-23. Hidrograma de crecida CB AG_08_04

19 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-24. Hidrograma de crecida CB AG_08_05

Figura 3-25. Hidrograma de crecida CB AG_08_06

20 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-26. Hidrograma de crecida CB AG_08_07

Figura 3-27. Hidrograma de crecida CB AG_08_08

21 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-28. Hidrograma de crecida CB QC_00

Figura 3-29. Hidrograma de crecida CB QC_01

22 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-30. Hidrograma de crecida CB QC_02

## 3.3. Otras Consideraciones

En el modelo hidráulico AG_Z3, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant

(opción SWE-ELM en HEC-RAS). Se consideró una malla de cálculo de distintas resoluciones, siendo estas 6

y 3 m.

Se utilizo un paso de tiempo de 1 segundo ajustado en función de los numero de Courant del modelo, donde

se empleó un máximo de 0.4 y un mínimo de 0.15.

El tiempo de modelación se consideró en función del tiempo del hidrograma de crecida, en particular el

modelo AG_Z3 tiene un tiempo de modelación de 20 horas.

23 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

# 4. Resultados

## 4.1. Tormenta periodo de retorno 100 años

Figura 4-1. Profundidad máxima periodo de retorno 100 años. Área de generación (negro)

La visualización anterior permite observar los resultados completos del modelo AG_Z3, sin embargo, debido

a la escala presentada los resultados no se aprecian con alta resolución. A continuación, se muestran los

resultados de profundidad por sectores:

24 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 4-2. Profundidad máxima periodo de retorno 100 años. Sector 1

Figura 4-3. Profundidad máxima periodo de retorno 100 años. Sector 2

25 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 4-4. Profundidad máxima periodo de retorno 100 años. Sector 3

Figura 4-5. Profundidad máxima periodo de retorno 100 años. Sector 4

26 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 4-6. Velocidad máxima periodo de retorno 100 años. Área de generación (negro)

De la misma manera que los resultados de profundidad se muestran los resultados de velocidad por sectores.

Figura 4-7. Velocidad máxima periodo de retorno 100 años. Sector 1

27 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 4-8. Velocidad máxima periodo de retorno 100 años. Sector 2

Figura 4-9. Velocidad máxima periodo de retorno 100 años. Sector 3

28 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 4-10. Velocidad máxima periodo de retorno 100 años. Sector 4

Figura 4-3. Hidrograma de salida periodo de retorno de 100 años

29 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01.03 MODELO HIDRAULICO AG_Z3
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

# 5. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. HEC-RAS. Versión 6.2. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

30 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3-1.: Condición de los cauces para el cálculo del coeficiente de Manning con método de Cowan**

| Condición del cauce | Col2 | Símbolo | Valor |
| --- | --- | --- | --- |
| Material del lecho | Tierra | n0 | 0.020 |
| Grado de irregularidad del perímetro mojado | Moderado | n1 | 0.010 |
| Variación de las secciones transversales | Alternándose<br>Ocasionalmente | n2 | 0.005 |
| Efecto relativo de las obstrucciones | Leve | n3 | 0.010 |
| Densidad de vegetación | Baja | n4 | 0.000 |
| Sinuosidad y frecuencia de meandros | Leve | m | 1.000 |
| Coeficiente de rugosidad | Coeficiente de rugosidad | n | 0.045 |

**Tabla 3-2.: Condiciones de borde e iniciales**

| Nombre CB | Tipo de CB | Caudal peak<br>[m3 /s]<br>0.21 | Pendiente<br>[mm]<br>0.07 |
| --- | --- | --- | --- |
| US_AG_04_00 | Intermedia | Intermedia | Intermedia |
| US_AG_04_01 | Intermedia | 0.39 | 0.04 |
| US_AG_04_02 | Aguas arriba | 0.34 | 0.07 |
| US_AG_05_00 | Intermedia | 0.43 | 0.04 |
| US_AG_05_01 | Intermedia | 0.17 | 0.04 |
