---
title: Sin título
author: Hilda Castro
date: D:20240322151935-03'00'
language: es
type: report
pages: 12
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME CORRENTOMETRÍA CONCESIÓN DE ACUICULTURA CODIGO CENTRO 102908
  - Cultivos Quechomó
-->

CCS - INFORME CORRENTOMETRÍA CENTRO 102908

# INFORME CORRENTOMETRÍA CONCESIÓN DE ACUICULTURA CODIGO CENTRO 102908

Karen Sánchez Rodríguez
# Cultivos Quechomó

Realizada por

Laboratorio Ramalab

Castro, Febrero 2024

Laboratorio RAMALAB EIRL, Pje. Narciso Vargas S/N casa 2, Castro - Chiloé. Fono: (65) 2636132



CCS - INFORME CORRENTOMETRÍA CENTRO 102908

**1) INTRODUCCION**

Del 13 al 14 de febrero de 2023, se efectuó el estudio de correntometría de 24 horas en la

concesión 102908 ubicada en el sector Punta Quechomó (Puerto Haro), Isla Lemuy, Canal Yal,

comuna de Puqueldón, Región de los Lagos. P erteneciente a la empresa Cultivos Quechomó. El

objetivo es caracterizar el comportamiento dinámico de la columna de agua durante la cuadratura,

con la intensión de tener una estimación de las condiciones mínimas de transporte de alimento,

retención o dispersión del material en suspensión (fecas, restos de organismos). Siendo

importante los primeros metros de la columna de agua, debido a que en ese sector se produce la

primera dilución del material, así como la formación de compuestos que en función de su

densidad precipitaran o no, además de producir un incremento del consumo de oxígeno y

minerales disueltos, lo que afecta finalmente a la capacidad de carga del sistema. Mientras que las

mediciones cerca del fondo dan cuenta de la capacidad de las corrientes de resuspender material,

así como de liberar gases que se generan de la degradación de la materia orgánica depositada,

aunque la menor resuspensión se producirá durante la cuadratura.

En la zona de canales, el principal agente forzante o generador de las corrientes es la marea,

actuando sobre toda la columna de agua, seguido por el viento que actúa sobre los primeros

metros de la columna de agua, siendo mayor su efecto cuando el viento es más intenso. Los

gradientes de densidad, verticales y horizontales también juegan un rol importante en la

generación de las corrientes, mas su relevancia es variable y debe ser analizada para cada lugar.

Las corrientes generadas por estos agentes son modificadas por la forma de la línea de la costa, así

como por la batimetría de cada lugar, especialmente si existen bajos, umbrales u otras variaciones

batimétricas que pueden acelerar o frenar las corrientes.

En cuanto a las mediciones que se realizan por medio de los correntómetros ADCP, hay que tener

presente que hay sectores de la columna de agua en la cual no sé realiza mediciones, y que en

algunos casos la primera capa no puede ser utilizada por presentar mucho ruido que altera las

mediciones, ya sea porque la capa de blanking es pequeña y/o hay mucho sedimento en

suspensión que introduce mucho ruido en la señal acústica. En tanto que cerca de la superficie

también se pierde una o más capas por la diferencia de densidad entre el agua de mar y el aire, la

variación del nivel del mar, y por la acción turbulenta del viento sobre el agua.

**2) METODOLOGÍA**

La correntometría se realizó con un correntómetro acústico marca Aanderaa modelo Seaward II
Sensor 5400 de 600 kHz, anclado en la concesión 102908 en la posición 42°38'48.02"S;

73°38'24.69"W” (Figura 1). El registro analizado fue desde las 11:00 hrs. del 13 de febrero hasta

Laboratorio RAMALAB EIRL, Pje. Narciso Vargas S/N casa 2, Castro - Chiloé. Fono: (65) 2636132



CCS - INFORME CORRENTOMETRÍA CENTRO 102908

las 11:00 hrs. del 14 de febrero de 2023, durante este período el equipo registro capas de 2 m

desde el fondo a la superficie cada 10 minutos durante un intervalo de 60 segundos, quedando a

una profundidad promedio de 45,2 m perfilando hacia la superficie, en la figura 2 se muestra el

esquema de medición del ADCP. El sistema de fondeo consistió en un trípode con pesos muertos

en cada una de sus patas, en cual se instaló el ADCP, el trípode fue amarrado con una cuerda por

el fondo hasta una de las boyas de inicio de línea localizada a unos 150 m. Tanto la programación

del equipo y recuperación de los datos fue realizada por medio de los programas provistos por el

fabricante, mientras que el procesamiento fue realizado por medio de rutinas escritas en MATLAB

para estos fines. La dirección fue corregida por la declinación magnética que para el lugar es de

+8°54’ (este) (https://www.magnetic-declination.com) (NCEI Geomagnetic Modeling Team and

British Geological Survey. 2019. World Magnetic Model 2020. NOAA National Centers for

Environmental Information. doi: 10.25921/11v3-da71).

El control de calidad de los datos inicialmente se realiza automáticamente mediante el software

del equipo, el que elimina aquellos datos que tuviesen un error en la medición mayor al 50%.

Durante el postproceso se determinan los datos anómalos u outliers mediante el análisis

estadistico donde se eliminan los datos escapados utilizando la media + 3 desviaciones estándares

(Emery and Thomson, 1997).

**Figura 1.** Ubicación del anclaje del ADCP y área de la concesión 102908 (línea blanca), imagen

de Google Earth

Laboratorio RAMALAB EIRL, Pje. Narciso Vargas S/N casa 2, Castro - Chiloé. Fono: (65) 2636132



CCS - INFORME CORRENTOMETRÍA CENTRO 102908

**Figura 2.** Esquema de distribución de las capas desde los transductores a la superficie y registro

de presión.

**3)** **RESULTADOS**

De acuerdo con el registro del sensor de presión, el equipo estuvo en promedio a 45,2 m de

profundidad (Figura 3). Por las características del equipo y de la programación se registraron 21

capas bajo la variación de la marea, quedando la capa número 1 centrada a 2 m de profundidad

respecto al valor más bajo de la marea del período (Tabla 1). El rango de marea observado fue de

1,9 m. Se optó referir todo a la menor marea del período de observación (46.2 m) por

desconocerse cuál es el nivel de reducción de sonda del sector.

**Figura 3.** Variación del nivel del mar durante el período de mediciones.

**Tabla 1.** Profundidades de las capas de fondo, intermedia y superficie efectivas de medición

utilizadas.

|Capa|Distancia al Transductor [m]|Col3|Col4|Profundidad [m]|Col6|Col7|
|---|---|---|---|---|---|---|
|**Capa**|**Media**|**Inicio**|**Termino**|**Media**|**Inicio**|**Termino**|
|1 <br>11 <br>21|2 <br>22 <br>42|1 <br>21 <br>41|3 <br>23 <br>43|2 <br>22 <br>42|1 <br>21 <br>41|3 <br>23 <br>43|

Laboratorio RAMALAB EIRL, Pje. Narciso Vargas S/N casa 2, Castro - Chiloé. Fono: (65) 2636132



CCS - INFORME CORRENTOMETRÍA CENTRO 102908

La capa 1 se define como superficie de la cual determinan las capas hasta 1 m del instrumento, se

usará la capa 21 como la capa de fondo que corresponde a 42 m de profundidad y la capa 1 como

la más próxima a la superficie.

En la tabla 2 se muestra la estadística básica de las mediciones de corriente en cada capa, la

velocidad promedio estuvo entre 0,019 y 0,204 m/s, registrándose la mínima en la capa 4 (8 m), y

la máxima se registró en la capa 1 (2 m). La magnitud máxima registrada en el período de estudio

fue de 0,58 m/s que corresponde a 1,12 nudos en la capa 1 (2 m), mientras que la mínima

velocidad máxima fue de 0,07 m/s registrada en la capa 4 y equivale a 0,13 nudos. La **velocidad**

**media** en los primeros 20 m de profundidad es de **0.23 m/s.**

**Tabla 2** . Estadística básica de la magnitud de la corriente en la columna de agua (en metros por

segundo y en nudos).

|Capa|Profundidad<br>(m)|N|Magnitud [m/s]|Col5|Col6|Col7|Coeficiente|Magnitud [nudos]|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Capa**|**Profundidad**<br>**(m)**|**N **|**Mínimo**|**Promedio**|**Máximo**|**Des. Est.**|**Variación**|**Promedio**|**Máximo**|
|1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10 <br>11 <br>12 <br>13 <br>14 <br>15 <br>16 <br>17<br>18<br>19 <br>20 <br>21|2 <br>4 <br>6 <br>8 <br>10 <br>12 <br>14 <br>16 <br>18 <br>20 <br>22 <br>24 <br>26 <br>28 <br>30 <br>32 <br>34<br>36<br>38 <br>40 <br>42|145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145<br>145<br>145 <br>145 <br>145|0.012 <br>0.001 <br>0.000 <br>0.001 <br>0.001 <br>0.002 <br>0.006 <br>0.006 <br>0.019 <br>0.010 <br>0.003 <br>0.005 <br>0.003 <br>0.008 <br>0.011 <br>0.004 <br>0.007<br>0.003<br>0.009 <br>0.002 <br>0.004|0.198 <br>0.090 <br>0.022 <br>0.019 <br>0.023 <br>0.036 <br>0.071 <br>0.088 <br>0.094 <br>0.093 <br>0.086 <br>0.080 <br>0.074 <br>0.071 <br>0.072 <br>0.077 <br>0.083<br>0.087<br>0.091 <br>0.090 <br>0.086|0.579 <br>0.458 <br>0.156 <br>0.080 <br>0.088 <br>0.095 <br>0.139 <br>0.241 <br>0.256 <br>0.258 <br>0.249 <br>0.229 <br>0.190 <br>0.182 <br>0.165 <br>0.157 <br>0.184<br>0.206<br>0.206 <br>0.195 <br>0.182|0.170 <br>0.095 <br>0.024 <br>0.016 <br>0.017 <br>0.021 <br>0.028 <br>0.038 <br>0.039 <br>0.038 <br>0.038 <br>0.038 <br>0.038 <br>0.036 <br>0.034 <br>0.036 <br>0.040<br>0.046<br>0.048 <br>0.050 <br>0.049|86.1 <br>105.9 <br>109.4 <br>79.9 <br>73.7 <br>59.4 <br>40.0 <br>42.7 <br>41.8 <br>41.5 <br>44.0 <br>47.0 <br>50.9 <br>50.4 <br>47.3 <br>46.8 <br>48.7<br>53.2<br>53.1 <br>55.1 <br>56.2|0.385 <br>0.174 <br>0.043 <br>0.038 <br>0.045 <br>0.070 <br>0.138 <br>0.171 <br>0.183 <br>0.180 <br>0.167 <br>0.155 <br>0.144 <br>0.138 <br>0.140 <br>0.149 <br>0.161<br>0.169<br>0.177 <br>0.175 <br>0.168|1.126 <br>0.890 <br>0.303 <br>0.156 <br>0.172 <br>0.185 <br>0.271 <br>0.468 <br>0.498 <br>0.502 <br>0.484 <br>0.445 <br>0.369 <br>0.353 <br>0.320 <br>0.306 <br>0.357<br>0.400<br>0.400 <br>0.380 <br>0.354|

Las figuras 4 y 5 muestran los resultados de las corrientes en la capa de fondo (21), intermedia (11)

y la más próxima a la superficie (1). Ambas componentes de la corriente muestran gran

variabilidad, con influencia del ciclo mareal en casi toda la columna de agua, aumentando la

corriente en la capa superficial y decreciendo el efecto de la marea en las capas más profundas. El

día 13 de febrero se observa una aceleración de la corriente en el fondo durante la marea llenante

y que termina con la estoa e inicio de la vaciante.

Laboratorio RAMALAB EIRL, Pje. Narciso Vargas S/N casa 2, Castro - Chiloé. Fono: (65) 2636132



CCS - INFORME CORRENTOMETRÍA CENTRO 102908

**Figura 4.** Variación de la velocidad en el tiempo por componente (u: Este-Oeste; v: Norte-Sur).

**Figura 5.** Variación temporal de los vectores de corrientes para las capas de superficie, intermedia

y fondo.

Laboratorio RAMALAB EIRL, Pje. Narciso Vargas S/N casa 2, Castro - Chiloé. Fono: (65) 2636132



CCS - INFORME CORRENTOMETRÍA CENTRO 102908

**Figura 6.** Gráfico de vectores progresivos de la corriente de la capa de superficie (línea azul),

intermedia (línea roja) y la más profunda (línea negra).

El diagrama de vectores progresivos (Figura 6) muestra un transporte neto en la capa de superficie

de 15,6 km al E, en la intermedia de 7,2 km al E y en la capa fondo de 0,4 km al SW. Estos

resultados junto con lo que muestra las figuras 7, 8, 10, 11 y 12 indican un sistema de circulación

de dos capas, donde el flujo entre los 1 y 15 m de profundidad tiene dirección al E (paralelo a la

costa), un flujo intermedio en dirección E, rotando al SW a medida que se profundiza y una capa

de fondo en dirección E-W.

La tabla de frecuencia por rango de velocidad muestra un predomino de las magnitudes entre 5 y

15 cm/s entre 15 y 45 m (Tabla 3 y Figura 7), la capa 1 y 2 hay un aumento de las corrientes con

intensidades por sobre los 15 cm/s. En dirección se observan cambios importantes debido al flujo

de marea a lo largo del canal, con predominio de las corrientes con componentes E que

corresponde al eje del canal (Tabla 4 y Figura 8), con excepción de la capa de fondo donde se

observan corrientes en dirección E y W. Lo anterior se refleja claramente en las rosas de corrientes

de las capas de fondo, intermedia y superficie (Figura 9).

Laboratorio RAMALAB EIRL, Pje. Narciso Vargas S/N casa 2, Castro - Chiloé. Fono: (65) 2636132



CCS - INFORME CORRENTOMETRÍA CENTRO 102908

**Figura 7.** Frecuencia de observaciones por rango de velocidad en cada capa de medición.

**Tabla 3.** Frecuencias de velocidad encontradas en el sitio %.

|Capa|Profundidad<br>(m)|Rango de magnitud [cm/s]|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|Capa|Profundidad<br>(m)|<1,5|1,5<br>3,0|3,0<br>5,0|5,0<br>10,0|10,0<br>15,0|15,0<br>20,0|20,0<br>25,0|25,0<br>30,0|>30.0|
|1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10 <br>11 <br>12 <br>13 <br>14 <br>15 <br>16 <br>17 <br>18 <br>19 <br>20 <br>21|2 <br>4 <br>6 <br>8 <br>10 <br>12 <br>14 <br>16 <br>18 <br>20 <br>22 <br>24 <br>26 <br>28 <br>30 <br>32 <br>34 <br>36 <br>38 <br>40 <br>42|1.4 <br>32.4 <br>47.6 <br>53.1 <br>40.7 <br>15.2 <br>1.4 <br>1.4 <br>0.0 <br>3.4 <br>3.4 <br>4.1 <br>3.4 <br>2.8 <br>2.8 <br>2.8 <br>0.7 <br>2.1 <br>1.4 <br>4.8 <br>3.4|9.7 <br>13.8 <br>33.1 <br>29.7 <br>32.4 <br>31.7 <br>5.5 <br>2.8 <br>4.1 <br>4.1 <br>2.8 <br>7.6 <br>7.6 <br>13.8 <br>9.0 <br>6.2 <br>5.5 <br>6.2 <br>4.1 <br>6.2 <br>10.3|9.7 <br>11.0 <br>9.7 <br>11.0 <br>17.9 <br>30.3 <br>19.3 <br>14.5 <br>8.3 <br>4.8 <br>12.4 <br>13.1 <br>24.1 <br>13.8 <br>19.3 <br>16.6 <br>20.0 <br>16.6 <br>17.9 <br>14.5 <br>13.8|28.3 <br>5.5 <br>6.9 <br>6.2 <br>9.0 <br>22.8 <br>56.6 <br>43.4 <br>42.1 <br>46.9 <br>49.0 <br>45.5 <br>35.2 <br>43.4 <br>42.1 <br>46.9 <br>36.6 <br>34.5 <br>35.2 <br>33.1 <br>32.4|6.2 <br>6.9 <br>2.1 <br>0.0 <br>0.0 <br>0.0 <br>17.2 <br>33.8 <br>38.6 <br>33.8 <br>29.7 <br>26.9 <br>27.6 <br>24.8 <br>25.5 <br>26.2 <br>31.0 <br>30.3 <br>27.6 <br>26.9 <br>26.2|3.4 <br>9.7 <br>0.7 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>2.8 <br>5.5 <br>6.2 <br>2.1 <br>2.1 <br>2.1 <br>1.4 <br>1.4 <br>1.4 <br>6.2 <br>9.7 <br>13.1 <br>14.5 <br>13.8|3.4 <br>15.9 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>1.4 <br>0.7 <br>0.0 <br>0.7 <br>0.7 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.7 <br>0.7 <br>0.0 <br>0.0|7.6 <br>4.1 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.7 <br>0.7 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0|30.3 <br>0.7 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0|

Laboratorio RAMALAB EIRL, Pje. Narciso Vargas S/N casa 2, Castro - Chiloé. Fono: (65) 2636132



CCS - INFORME CORRENTOMETRÍA CENTRO 102908

**Figura 8.** Frecuencia de observaciones por dirección en cada capa de medición.

**Tabla 4** . Frecuencias de dirección encontradas en el sitio (%).

|Capa|Profundidad<br>(m)|Dirección|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Capa**<br>|**Profundidad**<br>**(m)**|**N **|**NE**|**E **|**SE**|**S **|**SW**|**W **|**NW**|
|1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10 <br>11 <br>12 <br>13 <br>14 <br>15 <br>16 <br>17 <br>18 <br>19 <br>20 <br>21|2 <br>4 <br>6 <br>8 <br>10 <br>12 <br>14 <br>16 <br>18 <br>20 <br>22 <br>24 <br>26 <br>28 <br>30 <br>32 <br>34 <br>36 <br>38 <br>40 <br>42|0.0 <br>3.4 <br>9.7 <br>12.4 <br>8.3 <br>4.1 <br>0.0 <br>0.7 <br>0.0 <br>1.4 <br>0.7 <br>2.1 <br>4.1 <br>4.8 <br>6.2 <br>6.9 <br>4.8 <br>3.4 <br>3.4 <br>2.8 <br>5.5|9.7 <br>26.2 <br>11.7 <br>9.7 <br>15.2 <br>23.4 <br>29.7 <br>18.6 <br>17.2 <br>17.9 <br>17.2 <br>13.1 <br>15.2 <br>10.3 <br>3.4 <br>4.8 <br>3.4 <br>1.4 <br>3.4 <br>2.8 <br>3.4|47.6 <br>38.6 <br>10.3 <br>31.0 <br>38.6 <br>49.7 <br>54.5 <br>66.2 <br>69.0 <br>67.6 <br>64.1 <br>62.1 <br>53.8 <br>49.0 <br>55.2 <br>47.6 <br>43.4 <br>37.2 <br>31.0 <br>31.0 <br>23.4|39.3 <br>17.9 <br>25.5 <br>22.8 <br>26.2 <br>10.3 <br>15.9 <br>7.6 <br>4.8 <br>3.4 <br>8.3 <br>10.3 <br>9.7 <br>13.8 <br>7.6 <br>10.3 <br>10.3 <br>13.8 <br>14.5 <br>11.0 <br>11.7|2.8 <br>8.3 <br>13.1 <br>14.5 <br>4.1 <br>4.8 <br>0.0 <br>6.2 <br>8.3 <br>6.9 <br>4.8 <br>5.5 <br>5.5 <br>4.1 <br>4.8 <br>2.8 <br>2.1 <br>2.8 <br>3.4 <br>3.4 <br>4.8|0.7 <br>0.7 <br>9.0 <br>2.1 <br>1.4 <br>2.8 <br>0.0 <br>0.7 <br>0.7 <br>0.7 <br>1.4 <br>2.8 <br>8.3 <br>7.6 <br>10.3 <br>7.6 <br>7.6 <br>9.7 <br>7.6 <br>8.3 <br>9.7|0.0 <br>4.8 <br>4.1 <br>3.4 <br>0.7 <br>2.1 <br>0.0 <br>0.0 <br>0.0 <br>1.4 <br>1.4 <br>1.4 <br>2.1 <br>6.9 <br>10.3 <br>20.0 <br>24.8 <br>27.6 <br>33.1 <br>37.2 <br>36.6|0.0 <br>0.0 <br>16.6 <br>4.1 <br>5.5 <br>2.8 <br>0.0 <br>0.0 <br>0.0 <br>0.7 <br>2.1 <br>2.8 <br>1.4 <br>3.4 <br>2.1 <br>0.0 <br>3.4 <br>4.1 <br>3.4 <br>3.4 <br>4.8|

Laboratorio RAMALAB EIRL, Pje. Narciso Vargas S/N casa 2, Castro - Chiloé. Fono: (65) 2636132



CCS - INFORME CORRENTOMETRÍA CENTRO 102908

**Figura 9.** Rosa de las corrientes en las capas de fondo (capa 21), intermedia (capa 11) y

superficie (capa 1).

Laboratorio RAMALAB EIRL, Pje. Narciso Vargas S/N casa 2, Castro - Chiloé. Fono: (65) 2636132



CCS - INFORME CORRENTOMETRÍA CENTRO 102908

Para resumir, los resultados del periodo las corrientes registradas se presentan en el diagrama de

la figura 10, en el cual se observa que el flujo neto en las capas de superficie e intermedias al E y la

de fondo al SW. En la figura 11 y 12 se muestra la magnitud de la corriente en toda la columna de

agua, donde es más intenso el flujo de la capa superficial al inicio del periodo de medición y que

corresponde a marea vaciante. El flujo se acelera durante la llenante especialmente en la capa

intermedia, esta intensificación en corriente a media agua es producto de la fricción con la línea de

costa y la batimetría durante periodo llenante, disminuyendo notablemente la corriente durante

la estoa. Toda la columna es afectada por la marea sin embargo otras fuerzas serian dominantes

en las capas superficial e intermedia.

**Figura 10.** Representación de los flujos netos obtenidos para el periodo de medición en las

capas de fondo, intermedia y superficial.

**Figura 11. Perfil de magnitud de la corriente durante el periodo.**

Laboratorio RAMALAB EIRL, Pje. Narciso Vargas S/N casa 2, Castro - Chiloé. Fono: (65) 2636132



CCS - INFORME CORRENTOMETRÍA CENTRO 102908

**Figura 12.** **Perfil promedio de las componentes u (este-oeste) y v (norte-sur) de la velocidad**

**de la corriente**

Laboratorio RAMALAB EIRL, Pje. Narciso Vargas S/N casa 2, Castro - Chiloé. Fono: (65) 2636132


---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: ** Profundidades de las capas de fondo, intermedia y superficie efectivas de medición**

| Capa | Distancia al Transductor [m] | Col3 | Col4 | Profundidad [m] | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Capa** | **Media** | **Inicio** | **Termino** | **Media** | **Inicio** | **Termino** |
| 1 <br>11 <br>21 | 2 <br>22 <br>42 | 1 <br>21 <br>41 | 3 <br>23 <br>43 | 2 <br>22 <br>42 | 1 <br>21 <br>41 | 3 <br>23 <br>43 |

**Tabla 2: ** . Estadística básica de la magnitud de la corriente en la columna de agua (en metros por**

| Capa | Profundidad<br>(m) | N | Magnitud [m/s] | Col5 | Col6 | Col7 | Coeficiente | Magnitud [nudos] | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Capa** | **Profundidad**<br>**(m)** | **N ** | **Mínimo** | **Promedio** | **Máximo** | **Des. Est.** | **Variación** | **Promedio** | **Máximo** |
| 1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10 <br>11 <br>12 <br>13 <br>14 <br>15 <br>16 <br>17<br>18<br>19 <br>20 <br>21 | 2 <br>4 <br>6 <br>8 <br>10 <br>12 <br>14 <br>16 <br>18 <br>20 <br>22 <br>24 <br>26 <br>28 <br>30 <br>32 <br>34<br>36<br>38 <br>40 <br>42 | 145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145 <br>145<br>145<br>145 <br>145 <br>145 | 0.012 <br>0.001 <br>0.000 <br>0.001 <br>0.001 <br>0.002 <br>0.006 <br>0.006 <br>0.019 <br>0.010 <br>0.003 <br>0.005 <br>0.003 <br>0.008 <br>0.011 <br>0.004 <br>0.007<br>0.003<br>0.009 <br>0.002 <br>0.004 | 0.198 <br>0.090 <br>0.022 <br>0.019 <br>0.023 <br>0.036 <br>0.071 <br>0.088 <br>0.094 <br>0.093 <br>0.086 <br>0.080 <br>0.074 <br>0.071 <br>0.072 <br>0.077 <br>0.083<br>0.087<br>0.091 <br>0.090 <br>0.086 | 0.579 <br>0.458 <br>0.156 <br>0.080 <br>0.088 <br>0.095 <br>0.139 <br>0.241 <br>0.256 <br>0.258 <br>0.249 <br>0.229 <br>0.190 <br>0.182 <br>0.165 <br>0.157 <br>0.184<br>0.206<br>0.206 <br>0.195 <br>0.182 | 0.170 <br>0.095 <br>0.024 <br>0.016 <br>0.017 <br>0.021 <br>0.028 <br>0.038 <br>0.039 <br>0.038 <br>0.038 <br>0.038 <br>0.038 <br>0.036 <br>0.034 <br>0.036 <br>0.040<br>0.046<br>0.048 <br>0.050 <br>0.049 | 86.1 <br>105.9 <br>109.4 <br>79.9 <br>73.7 <br>59.4 <br>40.0 <br>42.7 <br>41.8 <br>41.5 <br>44.0 <br>47.0 <br>50.9 <br>50.4 <br>47.3 <br>46.8 <br>48.7<br>53.2<br>53.1 <br>55.1 <br>56.2 | 0.385 <br>0.174 <br>0.043 <br>0.038 <br>0.045 <br>0.070 <br>0.138 <br>0.171 <br>0.183 <br>0.180 <br>0.167 <br>0.155 <br>0.144 <br>0.138 <br>0.140 <br>0.149 <br>0.161<br>0.169<br>0.177 <br>0.175 <br>0.168 | 1.126 <br>0.890 <br>0.303 <br>0.156 <br>0.172 <br>0.185 <br>0.271 <br>0.468 <br>0.498 <br>0.502 <br>0.484 <br>0.445 <br>0.369 <br>0.353 <br>0.320 <br>0.306 <br>0.357<br>0.400<br>0.400 <br>0.380 <br>0.354 |

**Tabla 3.: ** Frecuencias de velocidad encontradas en el sitio %.**

| Capa | Profundidad<br>(m) | Rango de magnitud [cm/s] | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Capa | Profundidad<br>(m) | <1,5 | 1,5<br>3,0 | 3,0<br>5,0 | 5,0<br>10,0 | 10,0<br>15,0 | 15,0<br>20,0 | 20,0<br>25,0 | 25,0<br>30,0 | >30.0 |
| 1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10 <br>11 <br>12 <br>13 <br>14 <br>15 <br>16 <br>17 <br>18 <br>19 <br>20 <br>21 | 2 <br>4 <br>6 <br>8 <br>10 <br>12 <br>14 <br>16 <br>18 <br>20 <br>22 <br>24 <br>26 <br>28 <br>30 <br>32 <br>34 <br>36 <br>38 <br>40 <br>42 | 1.4 <br>32.4 <br>47.6 <br>53.1 <br>40.7 <br>15.2 <br>1.4 <br>1.4 <br>0.0 <br>3.4 <br>3.4 <br>4.1 <br>3.4 <br>2.8 <br>2.8 <br>2.8 <br>0.7 <br>2.1 <br>1.4 <br>4.8 <br>3.4 | 9.7 <br>13.8 <br>33.1 <br>29.7 <br>32.4 <br>31.7 <br>5.5 <br>2.8 <br>4.1 <br>4.1 <br>2.8 <br>7.6 <br>7.6 <br>13.8 <br>9.0 <br>6.2 <br>5.5 <br>6.2 <br>4.1 <br>6.2 <br>10.3 | 9.7 <br>11.0 <br>9.7 <br>11.0 <br>17.9 <br>30.3 <br>19.3 <br>14.5 <br>8.3 <br>4.8 <br>12.4 <br>13.1 <br>24.1 <br>13.8 <br>19.3 <br>16.6 <br>20.0 <br>16.6 <br>17.9 <br>14.5 <br>13.8 | 28.3 <br>5.5 <br>6.9 <br>6.2 <br>9.0 <br>22.8 <br>56.6 <br>43.4 <br>42.1 <br>46.9 <br>49.0 <br>45.5 <br>35.2 <br>43.4 <br>42.1 <br>46.9 <br>36.6 <br>34.5 <br>35.2 <br>33.1 <br>32.4 | 6.2 <br>6.9 <br>2.1 <br>0.0 <br>0.0 <br>0.0 <br>17.2 <br>33.8 <br>38.6 <br>33.8 <br>29.7 <br>26.9 <br>27.6 <br>24.8 <br>25.5 <br>26.2 <br>31.0 <br>30.3 <br>27.6 <br>26.9 <br>26.2 | 3.4 <br>9.7 <br>0.7 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>2.8 <br>5.5 <br>6.2 <br>2.1 <br>2.1 <br>2.1 <br>1.4 <br>1.4 <br>1.4 <br>6.2 <br>9.7 <br>13.1 <br>14.5 <br>13.8 | 3.4 <br>15.9 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>1.4 <br>0.7 <br>0.0 <br>0.7 <br>0.7 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.7 <br>0.7 <br>0.0 <br>0.0 | 7.6 <br>4.1 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.7 <br>0.7 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 | 30.3 <br>0.7 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 <br>0.0 |

**Tabla 4: ** . Frecuencias de dirección encontradas en el sitio (%).**

| Capa | Profundidad<br>(m) | Dirección | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Capa**<br> | **Profundidad**<br>**(m)** | **N ** | **NE** | **E ** | **SE** | **S ** | **SW** | **W ** | **NW** |
| 1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10 <br>11 <br>12 <br>13 <br>14 <br>15 <br>16 <br>17 <br>18 <br>19 <br>20 <br>21 | 2 <br>4 <br>6 <br>8 <br>10 <br>12 <br>14 <br>16 <br>18 <br>20 <br>22 <br>24 <br>26 <br>28 <br>30 <br>32 <br>34 <br>36 <br>38 <br>40 <br>42 | 0.0 <br>3.4 <br>9.7 <br>12.4 <br>8.3 <br>4.1 <br>0.0 <br>0.7 <br>0.0 <br>1.4 <br>0.7 <br>2.1 <br>4.1 <br>4.8 <br>6.2 <br>6.9 <br>4.8 <br>3.4 <br>3.4 <br>2.8 <br>5.5 | 9.7 <br>26.2 <br>11.7 <br>9.7 <br>15.2 <br>23.4 <br>29.7 <br>18.6 <br>17.2 <br>17.9 <br>17.2 <br>13.1 <br>15.2 <br>10.3 <br>3.4 <br>4.8 <br>3.4 <br>1.4 <br>3.4 <br>2.8 <br>3.4 | 47.6 <br>38.6 <br>10.3 <br>31.0 <br>38.6 <br>49.7 <br>54.5 <br>66.2 <br>69.0 <br>67.6 <br>64.1 <br>62.1 <br>53.8 <br>49.0 <br>55.2 <br>47.6 <br>43.4 <br>37.2 <br>31.0 <br>31.0 <br>23.4 | 39.3 <br>17.9 <br>25.5 <br>22.8 <br>26.2 <br>10.3 <br>15.9 <br>7.6 <br>4.8 <br>3.4 <br>8.3 <br>10.3 <br>9.7 <br>13.8 <br>7.6 <br>10.3 <br>10.3 <br>13.8 <br>14.5 <br>11.0 <br>11.7 | 2.8 <br>8.3 <br>13.1 <br>14.5 <br>4.1 <br>4.8 <br>0.0 <br>6.2 <br>8.3 <br>6.9 <br>4.8 <br>5.5 <br>5.5 <br>4.1 <br>4.8 <br>2.8 <br>2.1 <br>2.8 <br>3.4 <br>3.4 <br>4.8 | 0.7 <br>0.7 <br>9.0 <br>2.1 <br>1.4 <br>2.8 <br>0.0 <br>0.7 <br>0.7 <br>0.7 <br>1.4 <br>2.8 <br>8.3 <br>7.6 <br>10.3 <br>7.6 <br>7.6 <br>9.7 <br>7.6 <br>8.3 <br>9.7 | 0.0 <br>4.8 <br>4.1 <br>3.4 <br>0.7 <br>2.1 <br>0.0 <br>0.0 <br>0.0 <br>1.4 <br>1.4 <br>1.4 <br>2.1 <br>6.9 <br>10.3 <br>20.0 <br>24.8 <br>27.6 <br>33.1 <br>37.2 <br>36.6 | 0.0 <br>0.0 <br>16.6 <br>4.1 <br>5.5 <br>2.8 <br>0.0 <br>0.0 <br>0.0 <br>0.7 <br>2.1 <br>2.8 <br>1.4 <br>3.4 <br>2.1 <br>0.0 <br>3.4 <br>4.1 <br>3.4 <br>3.4 <br>4.8 |
