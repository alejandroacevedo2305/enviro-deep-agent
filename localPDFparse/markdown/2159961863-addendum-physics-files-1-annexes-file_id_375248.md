---
title: Sin título
author: kral kral
date: D:20161019170309-03'00'
language: es
type: manual
pages: 25
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELO HIDRAULICO SIN PROYECTO
-->

## PROYECTO DECLARACION DE IMPACTO AMBIENTAL PATAGONIAFRESH S.A. PLANTA MOLINA COMUNA DE MOLINA REGION DEL MAULE

# MODELO HIDRAULICO SIN PROYECTO

Anexo: Modelo Hidráulico SP

**1. PARÁMETROS DE ENTRADA**

 **Coeficiente de rugosidad**

**Cuadro 1**
Coeficiente de rugosidad lecho y planicies

|Factor|Condición|Col3|Valor|
|---|---|---|---|
|n0|Material del lecho|Grava Gruesa|0.028|
|n1|Irregul. Perímetro mojado|Leve|0.005|
|n2|Variación sección|Graduales|0.000|
|n3|Obstrucciones|Despreciable|0.000|
|n4|Densidad vegetación|Baja|0.005|
|**Suma**|**Suma**|**Suma**|**0.038**|
|m|1.000|Leve|1,00|
|**n **|**n **|**n **|**0.038**|

Como resultado de este análisis se adopta un coeficiente de rugosidad del
lecho de 0,04.

 **Coeficientes de contracción y expansión**

El Manual del usuario del Hec-Ras sugiere los siguientes valores:

**Cuadro 2**
Coeficientes de Contracción y Expansión

|Condición|Contracción|Expansión|
|---|---|---|
|Sin pérdida medible|0,0|0,0|
|Transición gradual|0,1|0,3|
|Sección típica de puentes|0,3|0,5|
|Transición brusca|0,6|0,8|

En este caso, se distingue solo una situación: Transición gradual.

2

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

- **Condición de borde**

**Cuadro 3**

Condiciones de borde. Parámetros de entrada modelación

|Parámetro|Valor|Observación|
|---|---|---|
|Caudal|Q1 = 1,0 m~~3~~/s (Tramo 1)<br>Q2 = 4,68 m3/s (Tramo 2)<br>Q3 = 5,68 m3/s (Tramo 3)<br>Q4 = 5,72 m3/s (Tramo 3)<br>Q5 = 4,72 m3/s (Tramo 2)<br>|T100, Periodo de retorno de<br>100 años<br>Q1, por porteo<br>Q4 y Q5, suma de descargas<br>PETAS Q=0,04 m3/s c/u|
|Condición de<br>borde|Primer y último Perfil:<br>Pendiente Normal|Pend. A. Arriba S =0.0078<br>(Tramo 1)<br>Pend. A. Arriba S =0.01<br>(Tramo 2)<br>Pend. A. Abajo S =0.0078<br>(Tramo 3)|
|Flujo|Uniforme|Unidimensional|
|Régimen|Mixto|Modelación|

3

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

**Fig. 1 Perfil Isométrico**

4

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

**Fig. 2 Perfil Longitudinal Tramo 1**

5

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

**Fig. 2 Perfil Longitudinal Tramo 2 y Tramo 3**

6

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

**Cuadro 4**
Eje Hidráulico Patagoniafresh Tramo 1

|Estación<br>del Río|Periodo<br>modelo|PT|Dm|Caudal<br>Total|Elev. Mín<br>Fondo|Altura de<br>Agua|Altura<br>Crítica|Línea de<br>Energía|Pend.<br>Hidráulica|Velocidad|Área de<br>Flujo|Ancho<br>Superior|Radio<br>Hidráulico|No Froud|Tirante|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Estación<br>del Río|Periodo<br>modelo|PT|Dm|(m3/s)|(m)|(m)|(m)|(m)|(m/m)|(m/s)|(m2)|(m)|(m)||(m)|
|545|T100|1|0|1.00|242.32|242.72|242.53|242.74|0.0029|0.57|1.75|6.17|0.28|0.34|0.40|
|500|T100|2|50|1.00|242.16|242.39||242.44|0.0169|1.07|0.93|4.86|0.19|0.78|0.23|
|450|T100|3|86.3|1.00|241.83|242.13|242.00|242.16|0.0043|0.74|1.36|4.65|0.30|0.43|0.30|
|420||||Culvert||||||||||||
|411|T100|4|103|1.00|241.68|242.13||242.14|0.0012|0.45|2.21|5.31|0.39|0.22|0.45|
|400|T100|5|116.3|1.00|241.55|242.07||242.11|0.0047|0.85|1.18|3.06|0.35|0.44|0.53|
|395|T100|6|149.1|1.00|241.23|241.65|241.65|241.79|0.0283|1.65|0.60|2.21|0.25|1.01|0.42|
|311|T100|7|149.9|1.00|240.79|241.07|241.24|241.69|0.2159|3.49|0.29|1.56|0.16|2.61|0.29|
|300|T100|8|196.9|1.00|240.47|241.11|240.90|241.16|0.0062|0.99|1.01|2.37|0.35|0.48|0.64|
|254|T100|9|199.9|1.00|240.43|241.09||241.14|0.0058|0.96|1.04|2.37|0.36|0.47|0.66|
|252|T100|10|201.7|1.00|240.41|241.08||241.13|0.0077|0.95|1.06|3.21|0.28|0.53|0.67|
|250|T100|11|203.9|1.00|240.38|241.07||241.11|0.0067|0.91|1.09|3.11|0.30|0.49|0.69|
|247|T100|12|249.9|1.00|240.18|240.91||240.93|0.0025|0.71|1.41|2.60|0.43|0.31|0.73|
|200|T100|13|260.7|1.00|240.21|240.87||240.90|0.0032|0.74|1.34|2.97|0.38|0.35|0.66|
|150|T100|14|299.9|1.00|240.03|240.75||240.78|0.0030|0.75|1.33|2.68|0.41|0.34|0.72|
|149|T100|15|344.5|1.00|239.91|240.56||240.60|0.0056|0.93|1.07|2.63|0.35|0.47|0.65|
|117|T100|16|349.9|1.00|239.91|240.52||240.57|0.0061|0.96|1.05|2.57|0.34|0.48|0.61|
|103|T100|17|360.8|1.00|239.84|240.45||240.50|0.0073|0.99|1.01|2.77|0.32|0.52|0.61|
|100|T100|18|370.8|1.00|239.78|240.34||240.40|0.0120|1.15|0.87|2.80|0.27|0.66|0.56|
|86|T100|19|399.9|1.00|239.59|240.02||240.09|0.0099|1.09|0.92|2.86|0.29|0.62|0.44|
|50|T100|20|449.9|1.00|238.79|239.16|239.16|239.30|0.0281|1.66|0.60|2.15|0.25|1.00|0.36|

|Max|1.00|242.32|242.72|242.53|242.74|0.22|3.49|2.21|6.17|0.43|2.61|0.73|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Min|1.00|238.79|239.16|239.16|239.30|0.00|0.45|0.29|1.56|0.16|0.22|0.23|
|Promedio|1.00|240.57|241.10|241.25|241.18|0.02|1.08|1.11|3.15|0.31|0.63|0.53|
|Desv Est|0.22|0.94|0.87|1.17|0.86|0.05|0.64|0.41|1.17|0.07|0.51|0.16|

7

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

Eje Hidráulico Patagoniafresh Tramo 2

|Estación<br>del Río|Periodo<br>modelo|PT|Dm|Caudal<br>Total|Elev. Mín<br>Fondo|Altura de<br>Agua|Altura<br>Crítica|Línea de<br>Energía|Pend.<br>Hidráulica|Velocidad|Área de<br>Flujo|Ancho<br>Superior|Radio<br>Hidráulico|No Froud|Tirante|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Estación<br>del Río|Periodo<br>modelo|PT|Dm|(m3/s)|(m)|(m)|(m)|(m)|(m/m)|(m/s)|(m2)|(m)|(m)||(m)|
|675|T100|21|0|4.68|241.25|242.84|241.99|242.86|0.0005|0.61|9.27|11.56|0.73|0.17|1.59|
|674|T100|22|12.5|4.68|241.20|242.73|242.00|242.84|0.0019|1.46|3.21|11.44|1.53|0.38|1.53|
|670||||Culvert||||||||||||
|650|T100|23|18.2|4.68|241.17|242.60||242.62|0.0008|0.72|7.23|10.99|0.61|0.22|1.43|
|644|T100|24|50|4.68|241.04|242.56||242.59|0.0013|0.71|6.66|9.68|0.63|0.26|1.52|
|600|T100|25|100|4.68|241.14|242.23|242.17|242.41|0.0182|1.86|2.51|5.08|0.41|0.85|1.09|
|550|T100|26|150|4.68|240.08|241.12|241.12|241.36|0.0243|2.16|2.16|4.56|0.41|1.00|1.04|
|500|T100|27|198|4.68|239.39|240.21|240.03|240.34|0.0085|1.56|3.00|4.88|0.56|0.63|0.82|
|467|T100|28|200|4.68|239.38|240.19||240.32|0.0087|1.57|2.98|4.89|0.55|0.64|0.82|
|455|T100|29|250|4.68|238.86|239.61||239.78|0.0134|1.83|2.55|4.52|0.51|0.78|0.76|
|450|T100|30|270.2|4.68|238.57|239.48||239.58|0.0066|1.39|3.36|5.50|0.55|0.56|0.91|
|403|T100|31|300|4.72|238.34|239.31||239.40|0.0054|1.29|3.65|5.37|0.59|0.50|0.97|
|400|T100|32|313.3|4.72|238.23|239.22|238.84|239.34|0.0036|1.49|3.18|5.80|0.99|0.48|0.99|
|370||||Culvert||||||||||||
|356|T100|33|324.3|4.72|238.10|238.59|238.63|238.85|0.0293|2.24|2.10|5.31|0.38|1.14|0.49|

|Max|4.72|241.25|242.84|242.17|242.86|0.03|2.24|9.27|11.56|1.53|1.14|1.59|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Min|4.68|238.10|238.59|238.63|238.85|0.00|0.61|2.10|4.52|0.38|0.17|0.49|
|Promedio|4.69|239.75|240.82|240.68|240.95|0.01|1.45|3.99|6.89|0.65|0.59|1.07|
|Desv Est|1.65|1.28|1.58|1.52|1.54|0.01|0.52|2.24|2.85|0.31|0.30|0.34|

8

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

Eje Hidráulico Patagoniafresh Tramo 3

|Estación<br>del Río|Periodo<br>modelo|PT|Dm|Caudal<br>Total|Elev. Mín<br>Fondo|Altura de<br>Agua|Altura<br>Crítica|Línea de<br>Energía|Pend.<br>Hidráulica|Velocidad|Área de<br>Flujo|Ancho<br>Superior|Radio<br>Hidráulico|No Froud|Tirante|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Estación<br>del Río|Periodo<br>modelo|PT|Dm|(m3/s)|(m)|(m)|(m)|(m)|(m/m)|(m/s)|(m2)|(m)|(m)||(m)|
|350|T100|34|332.6|5.68|237.99|238.31|238.55|239.22|0.1830|4.23|1.34|5.25|0.25|2.67|0.31|
|333|T100|35|350|5.68|237.90|238.73|238.37|238.78|0.0028|0.98|5.79|8.10|0.65|0.37|0.82|
|325|T100|36|355.6|5.68|238.01|238.64||238.74|0.0096|1.42|3.99|8.42|0.44|0.66|0.63|
|314|T100|37|400|5.68|237.26|238.39||238.48|0.0040|1.28|4.45|5.19|0.73|0.44|1.13|
|300|T100|38|405.6|5.68|237.24|238.37||238.46|0.0047|1.37|4.14|4.80|0.72|0.47|1.13|
|271|T100|39|450|5.68|236.99|238.13||238.23|0.0052|1.41|4.04|4.88|0.69|0.49|1.15|
|250|T100|40|454.4|5.72|236.96|238.10||238.21|0.0054|1.43|4.00|4.85|0.69|0.50|1.15|
|200|T100|41|466.5|5.72|236.89|238.04||238.14|0.0053|1.43|3.99|4.78|0.70|0.50|1.15|
|198|T100|42|500|5.72|236.71|237.89||237.98|0.0042|1.32|4.34|5.10|0.73|0.46|1.18|
|150|T100|43|550|5.72|236.55|237.62||237.73|0.0059|1.45|3.93|5.26|0.66|0.54|1.07|
|100|T100|44|600|5.72|236.28|237.53||237.57|0.0017|0.89|6.41|7.29|0.80|0.30|1.25|
|50|T100|45|644.1|5.72|236.54|237.37|237.04|237.46|0.0037|1.33|4.30|9.18|0.83|0.47|0.83|
|18|T100|||Culvert||||||||||||
|15||46|674.5|5.72|236.43|237.31||237.35|0.0023|0.92|6.21|8.95|0.66|0.35|0.88|
|13|T100|47|675|5.72|236.42|237.24|237.07|237.34|0.0078|1.39|4.10|7.97|0.50|0.62|0.83|

|Max|5.72|238.01|238.73|238.55|239.22|0.18|4.23|6.41|9.18|0.83|2.67|1.25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Min|5.68|236.28|237.24|237.04|237.34|0.00|0.89|1.34|4.78|0.25|0.30|0.31|
|Promedio|5.70|237.01|237.98|237.76|238.12|0.02|1.49|4.36|6.43|0.65|0.63|0.97|
|Desv Est|1.47|0.60|0.49|0.81|0.58|0.05|0.81|1.23|1.76|0.15|0.59|0.26|

9

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

**Perfiles Transversales Patagoniafresh Tramo 1**

10

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

11

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

12

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

13

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

**Perfiles Transversales Patagoniafresh Tramo 2**

14

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

15

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

16

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

**Perfiles Transversales Patagoniafresh Tramo 3**

17

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

18

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

19

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

**Tablas Perfiles Transversales Patagoniafresh Tramo 1**

E.G. Elev (m) 242.74 Element Left OB Channel Right OB E.G. Elev (m) 242.44 Element Left OB Channel Right OB

W.S. Elev (m) 242.72 Reach Len. (m) 49.8 50 50.23 W.S. Elev (m) 242.39 Reach Len. (m) 36.81 36.33 36.01

Alpha 1 Stream Power (N/m s) 549.83 0 0 Alpha 1 Stream Power (N/m s) 543.55 0 0

C & E Loss (m) 0 Cum SA (1000 m2) 1.46 C & E Loss (m) 0.01 Cum SA (1000 m2) 1.18

|Plan: P_SP TRAMO1 E1 RS: 545 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|242.74|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.02|Wt. n-Val.||0.04||
|W.S. Elev (m)|242.72|Reach Len. (m)|49.8|50|50.23|
|Crit W.S. (m)|242.53|Flow Area (m2)||1.75||
|E.G. Slope (m/m)|0.00289|Area (m2)||1.75||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|6.17|Top Width (m)||6.17||
|Vel Total (m/s)|0.57|Avg. Vel. (m/s)||0.57||
|Max Chl Dpth (m)|0.4|Hydr. Depth (m)||0.28||
|Conv. Total (m3/s)|18.6|Conv. (m3/s)||18.6||
|Length Wtd. (m)|50|Wetted Per. (m)||6.3||
|Min Ch El (m)|242.32|Shear (N/m2)||7.86||
|Alpha|1|Stream Power (N/m s)|549.83|0|0|
|Frctn Loss (m)|0.29|Cum Volume (1000 m3)||0.49||
|C & E Loss (m)|0|Cum SA (1000 m2)||1.46||

|Plan: P_SP TRAMO1 E1 RS: 500 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|242.44|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.06|Wt. n-Val.||0.04||
|W.S. Elev (m)|242.39|Reach Len. (m)|36.81|36.33|36.01|
|Crit W.S. (m)||Flow Area (m2)||0.93||
|E.G. Slope (m/m)|0.016904|Area (m2)||0.93||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|4.86|Top Width (m)||4.86||
|Vel Total (m/s)|1.07|Avg. Vel. (m/s)||1.07||
|Max Chl Dpth (m)|0.23|Hydr. Depth (m)||0.19||
|Conv. Total (m3/s)|7.7|Conv. (m3/s)||7.7||
|Length Wtd. (m)|36.33|Wetted Per. (m)||4.94||
|Min Ch El (m)|242.16|Shear (N/m2)||31.33||
|Alpha|1|Stream Power (N/m s)|543.55|0|0|
|Frctn Loss (m)|0.27|Cum Volume (1000 m3)||0.43||
|C & E Loss (m)|0.01|Cum SA (1000 m2)||1.18||

E.G. Elev (m) 242.16 Element Left OB Channel Right OB E.G. Elev (m) 242.14 Element Left OB Channel Right OB

W.S. Elev (m) 242.13 Reach Len. (m) 17.45 16.74 16.07 W.S. Elev (m) 242.13 Reach Len. (m) 14.53 13.31 12

Alpha 1 Stream Power (N/m s) 328.78 0 0 Alpha 1 Stream Power (N/m s) 391.78 0 0

C & E Loss (m) Cum SA (1000 m2) 1.01 C & E Loss (m) 0 Cum SA (1000 m2) 0.92

|Plan: P_SP TRAMO1 E1 RS: 450 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|242.16|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.03|Wt. n-Val.||0.04||
|W.S. Elev (m)|242.13|Reach Len. (m)|17.45|16.74|16.07|
|Crit W.S. (m)|242|Flow Area (m2)||1.36||
|E.G. Slope (m/m)|0.004265|Area (m2)||1.38||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|4.65|Top Width (m)||4.65||
|Vel Total (m/s)|0.74|Avg. Vel. (m/s)||0.74||
|Max Chl Dpth (m)|0.3|Hydr. Depth (m)||0.3||
|Conv. Total (m3/s)|15.3|Conv. (m3/s)||15.3||
|Length Wtd. (m)|16.74|Wetted Per. (m)||4.5||
|Min Ch El (m)|241.83|Shear (N/m2)||12.64||
|Alpha|1|Stream Power (N/m s)|328.78|0|0|
|Frctn Loss (m)||Cum Volume (1000 m3)||0.38||
|C & E Loss (m)||Cum SA (1000 m2)||1.01||

|Plan: P_SP TRAMO1 E1 RS: 411 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|242.14|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.01|Wt. n-Val.||0.04||
|W.S. Elev (m)|242.13|Reach Len. (m)|14.53|13.31|12|
|Crit W.S. (m)||Flow Area (m2)||2.21||
|E.G. Slope (m/m)|0.00117|Area (m2)||2.21||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|5.31|Top Width (m)||5.31||
|Vel Total (m/s)|0.45|Avg. Vel. (m/s)||0.45||
|Max Chl Dpth (m)|0.45|Hydr. Depth (m)||0.42||
|Conv. Total (m3/s)|29.2|Conv. (m3/s)||29.2||
|Length Wtd. (m)|13.31|Wetted Per. (m)||5.71||
|Min Ch El (m)|241.68|Shear (N/m2)||4.43||
|Alpha|1|Stream Power (N/m s)|391.78|0|0|
|Frctn Loss (m)|0.03|Cum Volume (1000 m3)||0.36||
|C & E Loss (m)|0|Cum SA (1000 m2)||0.92||

E.G. Elev (m) 242.11 Element Left OB Channel Right OB E.G. Elev (m) 241.79 Element Left OB Channel Right OB

W.S. Elev (m) 242.07 Reach Len. (m) 31.11 32.83 33.84 W.S. Elev (m) 241.65 Reach Len. (m) 0.79 0.79 0.79

Alpha 1 Stream Power (N/m s) 399.11 0 0 Alpha 1 Stream Power (N/m s) 348.6 0 0

C & E Loss (m) 0.01 Cum SA (1000 m2) 0.87 C & E Loss (m) 0.03 Cum SA (1000 m2) 0.78

|Plan: P_SP TRAMO1 E1 RS: 400 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|242.11|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.04|Wt. n-Val.||0.04||
|W.S. Elev (m)|242.07|Reach Len. (m)|31.11|32.83|33.84|
|Crit W.S. (m)||Flow Area (m2)||1.18||
|E.G. Slope (m/m)|0.00466|Area (m2)||1.18||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|3.06|Top Width (m)||3.06||
|Vel Total (m/s)|0.85|Avg. Vel. (m/s)||0.85||
|Max Chl Dpth (m)|0.53|Hydr. Depth (m)||0.39||
|Conv. Total (m3/s)|14.6|Conv. (m3/s)||14.6||
|Length Wtd. (m)|32.83|Wetted Per. (m)||3.38||
|Min Ch El (m)|241.55|Shear (N/m2)||15.98||
|Alpha|1|Stream Power (N/m s)|399.11|0|0|
|Frctn Loss (m)|0.31|Cum Volume (1000 m3)||0.34||
|C & E Loss (m)|0.01|Cum SA (1000 m2)||0.87||

|Plan: P_SP TRAMO1 E1 RS: 395 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|241.79|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.14|Wt. n-Val.||0.04||
|W.S. Elev (m)|241.65|Reach Len. (m)|0.79|0.79|0.79|
|Crit W.S. (m)|241.65|Flow Area (m2)||0.6||
|E.G. Slope (m/m)|0.028263|Area (m2)||0.6||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|2.21|Top Width (m)||2.21||
|Vel Total (m/s)|1.65|Avg. Vel. (m/s)||1.65||
|Max Chl Dpth (m)|0.42|Hydr. Depth (m)||0.27||
|Conv. Total (m3/s)|5.9|Conv. (m3/s)||5.9||
|Length Wtd. (m)|0.79|Wetted Per. (m)||2.45||
|Min Ch El (m)|241.23|Shear (N/m2)||68.39||
|Alpha|1|Stream Power (N/m s)|348.6|0|0|
|Frctn Loss (m)|0.01|Cum Volume (1000 m3)||0.31||
|C & E Loss (m)|0.03|Cum SA (1000 m2)||0.78||

E.G. Elev (m) 241.69 Element Left OB Channel Right OB E.G. Elev (m) 241.16 Element Left OB Channel Right OB

W.S. Elev (m) 241.07 Reach Len. (m) 46.97 47 46.99 W.S. Elev (m) 241.11 Reach Len. (m) 3 3 3

Alpha 1 Stream Power (N/m s) 474.42 0 0 Alpha 1 Stream Power (N/m s) 453.83 0 0

C & E Loss (m) 0.05 Cum SA (1000 m2) 0.78 C & E Loss (m) 0 Cum SA (1000 m2) 0.69

|Plan: P_SP TRAMO1 E1 RS: 311 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|241.69|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.62|Wt. n-Val.||0.04||
|W.S. Elev (m)|241.07|Reach Len. (m)|46.97|47|46.99|
|Crit W.S. (m)|241.24|Flow Area (m2)||0.29||
|E.G. Slope (m/m)|0.215884|Area (m2)||0.29||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|1.56|Top Width (m)||1.56||
|Vel Total (m/s)|3.49|Avg. Vel. (m/s)||3.49||
|Max Chl Dpth (m)|0.29|Hydr. Depth (m)||0.18||
|Conv. Total (m3/s)|2.2|Conv. (m3/s)||2.2||
|Length Wtd. (m)|47|Wetted Per. (m)||1.74||
|Min Ch El (m)|240.79|Shear (N/m2)||349.23||
|Alpha|1|Stream Power (N/m s)|474.42|0|0|
|Frctn Loss (m)|0.05|Cum Volume (1000 m3)||0.31||
|C & E Loss (m)|0.05|Cum SA (1000 m2)||0.78||

|Plan: P_SP TRAMO1 E1 RS: 300 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|241.16|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.05|Wt. n-Val.||0.04||
|W.S. Elev (m)|241.11|Reach Len. (m)|3|3|3|
|Crit W.S. (m)|240.9|Flow Area (m2)||1.01||
|E.G. Slope (m/m)|0.006189|Area (m2)||1.01||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|2.37|Top Width (m)||2.37||
|Vel Total (m/s)|0.99|Avg. Vel. (m/s)||0.99||
|Max Chl Dpth (m)|0.64|Hydr. Depth (m)||0.43||
|Conv. Total (m3/s)|12.7|Conv. (m3/s)||12.7||
|Length Wtd. (m)|3|Wetted Per. (m)||2.86||
|Min Ch El (m)|240.47|Shear (N/m2)||21.54||
|Alpha|1|Stream Power (N/m s)|453.83|0|0|
|Frctn Loss (m)|0.02|Cum Volume (1000 m3)||0.28||
|C & E Loss (m)|0|Cum SA (1000 m2)||0.69||

E.G. Elev (m) 241.14 Element Left OB Channel Right OB E.G. Elev (m) 241.13 Element Left OB Channel Right OB

W.S. Elev (m) 241.09 Reach Len. (m) 1.81 1.81 1.81 W.S. Elev (m) 241.08 Reach Len. (m) 2.22 2.22 2.22

Alpha 1 Stream Power (N/m s) 443.15 0 0 Alpha 1 Stream Power (N/m s) 439.04 0 0

C & E Loss (m) 0 Cum SA (1000 m2) 0.68 C & E Loss (m) 0 Cum SA (1000 m2) 0.68

|Plan: P_SP TRAMO1 E1 RS: 252 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|241.13|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.05|Wt. n-Val.||0.04||
|W.S. Elev (m)|241.08|Reach Len. (m)|2.22|2.22|2.22|
|Crit W.S. (m)||Flow Area (m2)||1.06||
|E.G. Slope (m/m)|0.007691|Area (m2)||1.06||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|3.21|Top Width (m)||3.21||
|Vel Total (m/s)|0.95|Avg. Vel. (m/s)||0.95||
|Max Chl Dpth (m)|0.67|Hydr. Depth (m)||0.33||
|Conv. Total (m3/s)|11.4|Conv. (m3/s)||11.4||
|Length Wtd. (m)|2.22|Wetted Per. (m)||3.74||
|Min Ch El (m)|240.41|Shear (N/m2)||21.35||
|Alpha|1|Stream Power (N/m s)|439.04|0|0|
|Frctn Loss (m)|0.02|Cum Volume (1000 m3)||0.27||
|C & E Loss (m)|0|Cum SA (1000 m2)||0.68||

20

|Plan: P_SP TRAMO1 E1 RS: 254 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|241.14|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.05|Wt. n-Val.||0.04||
|W.S. Elev (m)|241.09|Reach Len. (m)|1.81|1.81|1.81|
|Crit W.S. (m)||Flow Area (m2)||1.04||
|E.G. Slope (m/m)|0.00584|Area (m2)||1.04||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|2.37|Top Width (m)||2.37||
|Vel Total (m/s)|0.96|Avg. Vel. (m/s)||0.96||
|Max Chl Dpth (m)|0.66|Hydr. Depth (m)||0.44||
|Conv. Total (m3/s)|13.1|Conv. (m3/s)||13.1||
|Length Wtd. (m)|1.81|Wetted Per. (m)||2.89||
|Min Ch El (m)|240.43|Shear (N/m2)||20.54||
|Alpha|1|Stream Power (N/m s)|443.15|0|0|
|Frctn Loss (m)|0.01|Cum Volume (1000 m3)||0.27||
|C & E Loss (m)|0|Cum SA (1000 m2)||0.68||

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

E.G. Elev (m) 241.11 Element Left OB Channel Right OB E.G. Elev (m) 240.93 Element Left OB Channel Right OB

W.S. Elev (m) 241.07 Reach Len. (m) 46.04 45.97 45.92 W.S. Elev (m) 240.91 Reach Len. (m) 10.76 10.76 10.76

Alpha 1 Stream Power (N/m s) 432.78 0 0 Alpha 1 Stream Power (N/m s) 375.22 0 0

C & E Loss (m) 0.01 Cum SA (1000 m2) 0.67 C & E Loss (m) 0 Cum SA (1000 m2) 0.54

|Plan: P_SP TRAMO1 E1 RS: 250 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|241.11|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.04|Wt. n-Val.||0.04||
|W.S. Elev (m)|241.07|Reach Len. (m)|46.04|45.97|45.92|
|Crit W.S. (m)||Flow Area (m2)||1.09||
|E.G. Slope (m/m)|0.006671|Area (m2)||1.09||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|3.11|Top Width (m)||3.11||
|Vel Total (m/s)|0.91|Avg. Vel. (m/s)||0.91||
|Max Chl Dpth (m)|0.69|Hydr. Depth (m)||0.35||
|Conv. Total (m3/s)|12.2|Conv. (m3/s)||12.2||
|Length Wtd. (m)|45.97|Wetted Per. (m)||3.65||
|Min Ch El (m)|240.38|Shear (N/m2)||19.59||
|Alpha|1|Stream Power (N/m s)|432.78|0|0|
|Frctn Loss (m)|0.18|Cum Volume (1000 m3)||0.27||
|C & E Loss (m)|0.01|Cum SA (1000 m2)||0.67||

|Plan: P_SP TRAMO1 E1 RS: 247 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|240.93|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.03|Wt. n-Val.||0.04||
|W.S. Elev (m)|240.91|Reach Len. (m)|10.76|10.76|10.76|
|Crit W.S. (m)||Flow Area (m2)||1.41||
|E.G. Slope (m/m)|0.002471|Area (m2)||1.41||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|2.6|Top Width (m)||2.6||
|Vel Total (m/s)|0.71|Avg. Vel. (m/s)||0.71||
|Max Chl Dpth (m)|0.73|Hydr. Depth (m)||0.54||
|Conv. Total (m3/s)|20.1|Conv. (m3/s)||20.1||
|Length Wtd. (m)|10.76|Wetted Per. (m)||3.26||
|Min Ch El (m)|240.18|Shear (N/m2)||10.46||
|Alpha|1|Stream Power (N/m s)|375.22|0|0|
|Frctn Loss (m)|0.03|Cum Volume (1000 m3)||0.21||
|C & E Loss (m)|0|Cum SA (1000 m2)||0.54||

E.G. Elev (m) 240.9 Element Left OB Channel Right OB E.G. Elev (m) 240.78 Element Left OB Channel Right OB

W.S. Elev (m) 240.87 Reach Len. (m) 39.11 39.24 39.35 W.S. Elev (m) 240.75 Reach Len. (m) 44.59 44.56 44.53

Alpha 1 Stream Power (N/m s) 395.56 0 0 Alpha 1 Stream Power (N/m s) 383.6 0 0

C & E Loss (m) 0 Cum SA (1000 m2) 0.51 C & E Loss (m) 0 Cum SA (1000 m2) 0.4

|Plan: P_SP TRAMO1 E1 RS: 200 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|240.9|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.03|Wt. n-Val.||0.04||
|W.S. Elev (m)|240.87|Reach Len. (m)|39.11|39.24|39.35|
|Crit W.S. (m)||Flow Area (m2)||1.34||
|E.G. Slope (m/m)|0.00319|Area (m2)||1.34||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|2.97|Top Width (m)||2.97||
|Vel Total (m/s)|0.74|Avg. Vel. (m/s)||0.74||
|Max Chl Dpth (m)|0.66|Hydr. Depth (m)||0.45||
|Conv. Total (m3/s)|17.7|Conv. (m3/s)||17.7||
|Length Wtd. (m)|39.24|Wetted Per. (m)||3.52||
|Min Ch El (m)|240.21|Shear (N/m2)||11.96||
|Alpha|1|Stream Power (N/m s)|395.56|0|0|
|Frctn Loss (m)|0.12|Cum Volume (1000 m3)||0.2||
|C & E Loss (m)|0|Cum SA (1000 m2)||0.51||

|Plan: P_SP TRAMO1 E1 RS: 150 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|240.78|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.03|Wt. n-Val.||0.04||
|W.S. Elev (m)|240.75|Reach Len. (m)|44.59|44.56|44.53|
|Crit W.S. (m)||Flow Area (m2)||1.33||
|E.G. Slope (m/m)|0.002961|Area (m2)||1.33||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|2.68|Top Width (m)||2.68||
|Vel Total (m/s)|0.75|Avg. Vel. (m/s)||0.75||
|Max Chl Dpth (m)|0.72|Hydr. Depth (m)||0.5||
|Conv. Total (m3/s)|18.4|Conv. (m3/s)||18.4||
|Length Wtd. (m)|44.56|Wetted Per. (m)||3.27||
|Min Ch El (m)|240.03|Shear (N/m2)||11.87||
|Alpha|1|Stream Power (N/m s)|383.6|0|0|
|Frctn Loss (m)|0.18|Cum Volume (1000 m3)||0.14||
|C & E Loss (m)|0|Cum SA (1000 m2)||0.4||

E.G. Elev (m) 240.6 Element Left OB Channel Right OB E.G. Elev (m) 240.57 Element Left OB Channel Right OB

W.S. Elev (m) 240.56 Reach Len. (m) 5.43 5.44 5.45 W.S. Elev (m) 240.52 Reach Len. (m) 10.9 10.9 10.9

Alpha 1 Stream Power (N/m s) 398.48 0 0 Alpha 1 Stream Power (N/m s) 388.57 0 0

C & E Loss (m) 0 Cum SA (1000 m2) 0.28 C & E Loss (m) 0 Cum SA (1000 m2) 0.26

|Plan: P_SP TRAMO1 E1 RS: 149 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|240.6|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.04|Wt. n-Val.||0.04||
|W.S. Elev (m)|240.56|Reach Len. (m)|5.43|5.44|5.45|
|Crit W.S. (m)||Flow Area (m2)||1.07||
|E.G. Slope (m/m)|0.005624|Area (m2)||1.07||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|2.63|Top Width (m)||2.63||
|Vel Total (m/s)|0.93|Avg. Vel. (m/s)||0.93||
|Max Chl Dpth (m)|0.65|Hydr. Depth (m)||0.41||
|Conv. Total (m3/s)|13.3|Conv. (m3/s)||13.3||
|Length Wtd. (m)|5.44|Wetted Per. (m)||3.04||
|Min Ch El (m)|239.91|Shear (N/m2)||19.39||
|Alpha|1|Stream Power (N/m s)|398.48|0|0|
|Frctn Loss (m)|0.03|Cum Volume (1000 m3)||0.09||
|C & E Loss (m)|0|Cum SA (1000 m2)||0.28||

|Plan: P_SP TRAMO1 E1 RS: 117 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|240.57|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.05|Wt. n-Val.||0.04||
|W.S. Elev (m)|240.52|Reach Len. (m)|10.9|10.9|10.9|
|Crit W.S. (m)||Flow Area (m2)||1.05||
|E.G. Slope (m/m)|0.00607|Area (m2)||1.05||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|2.57|Top Width (m)||2.57||
|Vel Total (m/s)|0.96|Avg. Vel. (m/s)||0.96||
|Max Chl Dpth (m)|0.61|Hydr. Depth (m)||0.41||
|Conv. Total (m3/s)|12.8|Conv. (m3/s)||12.8||
|Length Wtd. (m)|10.9|Wetted Per. (m)||3.04||
|Min Ch El (m)|239.91|Shear (N/m2)||20.48||
|Alpha|1|Stream Power (N/m s)|388.57|0|0|
|Frctn Loss (m)|0.07|Cum Volume (1000 m3)||0.08||
|C & E Loss (m)|0|Cum SA (1000 m2)||0.26||

E.G. Elev (m) 240.5 Element Left OB Channel Right OB E.G. Elev (m) 240.4 Element Left OB Channel Right OB

W.S. Elev (m) 240.45 Reach Len. (m) 10.11 10.04 9.93 W.S. Elev (m) 240.34 Reach Len. (m) 29.01 29.06 29.13

Alpha 1 Stream Power (N/m s) 390.73 0 0 Alpha 1 Stream Power (N/m s) 383.93 0 0

C & E Loss (m) 0 Cum SA (1000 m2) 0.24 C & E Loss (m) 0 Cum SA (1000 m2) 0.21

|Plan: P_SP TRAMO1 E1 RS: 103 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|240.5|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.05|Wt. n-Val.||0.04||
|W.S. Elev (m)|240.45|Reach Len. (m)|10.11|10.04|9.93|
|Crit W.S. (m)||Flow Area (m2)||1.01||
|E.G. Slope (m/m)|0.007279|Area (m2)||1.01||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|2.77|Top Width (m)||2.77||
|Vel Total (m/s)|0.99|Avg. Vel. (m/s)||0.99||
|Max Chl Dpth (m)|0.61|Hydr. Depth (m)||0.37||
|Conv. Total (m3/s)|11.7|Conv. (m3/s)||11.7||
|Length Wtd. (m)|10.04|Wetted Per. (m)||3.21||
|Min Ch El (m)|239.84|Shear (N/m2)||22.51||
|Alpha|1|Stream Power (N/m s)|390.73|0|0|
|Frctn Loss (m)|0.09|Cum Volume (1000 m3)||0.07||
|C & E Loss (m)|0|Cum SA (1000 m2)||0.24||

|Plan: P_SP TRAMO1 E1 RS: 100 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|240.4|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.07|Wt. n-Val.||0.04||
|W.S. Elev (m)|240.34|Reach Len. (m)|29.01|29.06|29.13|
|Crit W.S. (m)||Flow Area (m2)||0.87||
|E.G. Slope (m/m)|0.012024|Area (m2)||0.87||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|2.8|Top Width (m)||2.8||
|Vel Total (m/s)|1.15|Avg. Vel. (m/s)||1.15||
|Max Chl Dpth (m)|0.56|Hydr. Depth (m)||0.31||
|Conv. Total (m3/s)|9.1|Conv. (m3/s)||9.1||
|Length Wtd. (m)|29.06|Wetted Per. (m)||3.18||
|Min Ch El (m)|239.78|Shear (N/m2)||32.18||
|Alpha|1|Stream Power (N/m s)|383.93|0|0|
|Frctn Loss (m)|0.32|Cum Volume (1000 m3)||0.06||
|C & E Loss (m)|0|Cum SA (1000 m2)||0.21||

E.G. Elev (m) 240.09 Element Left OB Channel Right OB E.G. Elev (m) 239.3 Element Left OB Channel Right OB

W.S. Elev (m) 240.02 Reach Len. (m) 49.9 50 50.05 W.S. Elev (m) 239.16 Reach Len. (m) 0 0 0

Alpha 1 Stream Power (N/m s) 357.94 0 0 Alpha 1 Stream Power (N/m s) 321.98 0 0

|Plan: P_SP TRAMO1 E1 RS: 50 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|239.3|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.14|Wt. n-Val.||0.04||
|W.S. Elev (m)|239.16|Reach Len. (m)|0|0|0|
|Crit W.S. (m)|239.16|Flow Area (m2)||0.6||
|E.G. Slope (m/m)|0.028072|Area (m2)||0.6||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|2.15|Top Width (m)||2.15||
|Vel Total (m/s)|1.66|Avg. Vel. (m/s)||1.66||
|Max Chl Dpth (m)|0.36|Hydr. Depth (m)||0.28||
|Conv. Total (m3/s)|6|Conv. (m3/s)||6||
|Length Wtd. (m)|0|Wetted Per. (m)||2.4||
|Min Ch El (m)|238.79|Shear (N/m2)||68.95||
|Alpha|1|Stream Power (N/m s)|321.98|0|0|
|Frctn Loss (m)|0|Cum Volume (1000 m3)||||
|C & E Loss (m)|0.01|Cum SA (1000 m2)||||

21

|Plan: P_SP TRAMO1 E1 RS: 86 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|240.09|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.06|Wt. n-Val.||0.04||
|W.S. Elev (m)|240.02|Reach Len. (m)|49.9|50|50.05|
|Crit W.S. (m)||Flow Area (m2)||0.92||
|E.G. Slope (m/m)|0.009868|Area (m2)||0.92||
|Q Total (m3/s)|1|Flow (m3/s)||1||
|Top Width (m)|2.86|Top Width (m)||2.86||
|Vel Total (m/s)|1.09|Avg. Vel. (m/s)||1.09||
|Max Chl Dpth (m)|0.44|Hydr. Depth (m)||0.32||
|Conv. Total (m3/s)|10.1|Conv. (m3/s)||10.1||
|Length Wtd. (m)|50|Wetted Per. (m)||3.13||
|Min Ch El (m)|239.59|Shear (N/m2)||28.25||
|Alpha|1|Stream Power (N/m s)|357.94|0|0|
|Frctn Loss (m)|0.78|Cum Volume (1000 m3)||0.04||
|C & E Loss (m)|0.01|Cum SA (1000 m2)||0.13||

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

**Tablas Perfiles Transversales Patagoniafresh Tramo 2**

E.G. Elev (m) 242.86 Element Left OB Channel Right OB E.G. Elev (m) 242.84 Element Left OB Channel Right OB

W.S. Elev (m) 242.84 Reach Len. (m) 12.53 12.51 12.53 W.S. Elev (m) 242.73 Reach Len. (m) 5.5 5.65 5.83

E.G. Slope (m/m) 0.000486 Area (m2) 2.17 5.78 1.33 E.G. Slope (m/m) 0.00194 Area (m2) 1.15 6.44 0.98

Top Width (m) 11.56 Top Width (m) 3.85 4.43 3.29 Top Width (m) 11.44 Top Width (m) 3.18 5.04 3.22

Alpha 1.21 Stream Power (N/m s) 553.61 0 0 Alpha 1 Stream Power (N/m s) 547.62 0 0

Frctn Loss (m) 0.01 Cum Volume (1000 m3) 0.03 1.13 0.02 Frctn Loss (m) Cum Volume (1000 m3) 0.01 1.06 0.01

C & E Loss (m) 0.01 Cum SA (1000 m2) 0.12 1.77 0.13 C & E Loss (m) Cum SA (1000 m2) 0.07 1.71 0.09

|Plan: P_SP TRAMO 2 E2 RS: 675 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|242.86|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.02|Wt. n-Val.|0.04|0.04|0.04|
|W.S. Elev (m)|242.84|Reach Len. (m)|12.53|12.51|12.53|
|Crit W.S. (m)|241.99|Flow Area (m2)|2.17|5.78|1.33|
|E.G. Slope (m/m)|0.000486|Area (m2)|2.17|5.78|1.33|
|Q Total (m3/s)|4.68|Flow (m3/s)|0.77|3.53|0.38|
|Top Width (m)|11.56|Top Width (m)|3.85|4.43|3.29|
|Vel Total (m/s)|0.5|Avg. Vel. (m/s)|0.35|0.61|0.29|
|Max Chl Dpth (m)|1.59|Hydr. Depth (m)|0.56|1.3|0.4|
|Conv. Total (m3/s)|212.3|Conv. (m3/s)|34.9|160|17.4|
|Length Wtd. (m)|12.51|Wetted Per. (m)|4.19|4.95|3.51|
|Min Ch El (m)|241.25|Shear (N/m2)|2.46|5.56|1.8|
|Alpha|1.21|Stream Power (N/m s)|553.61|0|0|
|Frctn Loss (m)|0.01|Cum Volume (1000 m3)|0.03|1.13|0.02|
|C & E Loss (m)|0.01|Cum SA (1000 m2)|0.12|1.77|0.13|

|Plan: P_SP TRAMO 2 E2 RS: 674 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|242.84|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.11|Wt. n-Val.||0.04||
|W.S. Elev (m)|242.73|Reach Len. (m)|5.5|5.65|5.83|
|Crit W.S. (m)|242|Flow Area (m2)||3.21||
|E.G. Slope (m/m)|0.00194|Area (m2)|1.15|6.44|0.98|
|Q Total (m3/s)|4.68|Flow (m3/s)||4.68||
|Top Width (m)|11.44|Top Width (m)|3.18|5.04|3.22|
|Vel Total (m/s)|1.46|Avg. Vel. (m/s)||1.46||
|Max Chl Dpth (m)|1.53|Hydr. Depth (m)||1.53||
|Conv. Total (m3/s)|106.3|Conv. (m3/s)||106.3||
|Length Wtd. (m)|5.65|Wetted Per. (m)||2.1||
|Min Ch El (m)|241.2|Shear (N/m2)||29.04||
|Alpha|1|Stream Power (N/m s)|547.62|0|0|
|Frctn Loss (m)||Cum Volume (1000 m3)|0.01|1.06|0.01|
|C & E Loss (m)||Cum SA (1000 m2)|0.07|1.71|0.09|

E.G. Elev (m) 242.62 Element Left OB Channel Right OB E.G. Elev (m) 242.59 Element Left OB Channel Right OB

Vel Head (m) 0.03 Wt. n-Val. 0.04 0.04 0.04 Vel Head (m) 0.03 Wt. n-Val. 0.04 0.04 0.04

W.S. Elev (m) 242.6 Reach Len. (m) 31.91 31.84 31.75 W.S. Elev (m) 242.56 Reach Len. (m) 49.77 50 50.23

Crit W.S. (m) Flow Area (m2) 0.56 6.08 0.59 Crit W.S. (m) Flow Area (m2) 0.01 6.63 0.02

E.G. Slope (m/m) 0.000819 Area (m2) 0.56 6.08 0.59 E.G. Slope (m/m) 0.001328 Area (m2) 0.01 6.63 0.02

Q Total (m3/s) 4.68 Flow (m3/s) 0.14 4.4 0.14 Q Total (m3/s) 4.68 Flow (m3/s) 0 4.68 0

Top Width (m) 10.99 Top Width (m) 2.74 5.29 2.96 Top Width (m) 9.68 Top Width (m) 0.19 8.98 0.51

Vel Total (m/s) 0.65 Avg. Vel. (m/s) 0.24 0.72 0.24 Vel Total (m/s) 0.7 Avg. Vel. (m/s) 0.08 0.71 0.09

Max Chl Dpth (m) 1.43 Hydr. Depth (m) 0.2 1.15 0.2 Max Chl Dpth (m) 1.52 Hydr. Depth (m) 0.03 0.74 0.03

Conv. Total (m3/s) 163.6 Conv. (m3/s) 4.7 153.8 5 Conv. Total (m3/s) 128.4 Conv. (m3/s) 0 128.4 0

Length Wtd. (m) 31.84 Wetted Per. (m) 2.8 5.97 3 Length Wtd. (m) 50 Wetted Per. (m) 0.23 9.73 0.52

Min Ch El (m) 241.17 Shear (N/m2) 1.6 8.17 1.58 Min Ch El (m) 241.04 Shear (N/m2) 0.37 8.87 0.42

Alpha 1.18 Stream Power (N/m s) 541.49 0 0 Alpha 1.01 Stream Power (N/m s) 490.13 0 0

Frctn Loss (m) 0.03 Cum Volume (1000 m3) 0.01 1.04 0.01 Frctn Loss (m) 0.16 Cum Volume (1000 m3) 0 0.84 0

C & E Loss (m) 0 Cum SA (1000 m2) 0.06 1.68 0.07 C & E Loss (m) 0.02 Cum SA (1000 m2) 0.01 1.46 0.02

|Plan: P_SP TRAMO 2 E2 RS: 650 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|242.62|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.03|Wt. n-Val.|0.04|0.04|0.04|
|W.S. Elev (m)|242.6|Reach Len. (m)|31.91|31.84|31.75|
|Crit W.S. (m)||Flow Area (m2)|0.56|6.08|0.59|
|E.G. Slope (m/m)|0.000819|Area (m2)|0.56|6.08|0.59|
|Q Total (m3/s)|4.68|Flow (m3/s)|0.14|4.4|0.14|
|Top Width (m)|10.99|Top Width (m)|2.74|5.29|2.96|
|Vel Total (m/s)|0.65|Avg. Vel. (m/s)|0.24|0.72|0.24|
|Max Chl Dpth (m)|1.43|Hydr. Depth (m)|0.2|1.15|0.2|
|Conv. Total (m3/s)|163.6|Conv. (m3/s)|4.7|153.8|5|
|Length Wtd. (m)|31.84|Wetted Per. (m)|2.8|5.97|3|
|Min Ch El (m)|241.17|Shear (N/m2)|1.6|8.17|1.58|
|Alpha|1.18|Stream Power (N/m s)|541.49|0|0|
|Frctn Loss (m)|0.03|Cum Volume (1000 m3)|0.01|1.04|0.01|
|C & E Loss (m)|0|Cum SA (1000 m2)|0.06|1.68|0.07|

|Plan: P_SP TRAMO 2 E2 RS: 644 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|242.59|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.03|Wt. n-Val.|0.04|0.04|0.04|
|W.S. Elev (m)|242.56|Reach Len. (m)|49.77|50|50.23|
|Crit W.S. (m)||Flow Area (m2)|0.01|6.63|0.02|
|E.G. Slope (m/m)|0.001328|Area (m2)|0.01|6.63|0.02|
|Q Total (m3/s)|4.68|Flow (m3/s)|0|4.68|0|
|Top Width (m)|9.68|Top Width (m)|0.19|8.98|0.51|
|Vel Total (m/s)|0.7|Avg. Vel. (m/s)|0.08|0.71|0.09|
|Max Chl Dpth (m)|1.52|Hydr. Depth (m)|0.03|0.74|0.03|
|Conv. Total (m3/s)|128.4|Conv. (m3/s)|0|128.4|0|
|Length Wtd. (m)|50|Wetted Per. (m)|0.23|9.73|0.52|
|Min Ch El (m)|241.04|Shear (N/m2)|0.37|8.87|0.42|
|Alpha|1.01|Stream Power (N/m s)|490.13|0|0|
|Frctn Loss (m)|0.16|Cum Volume (1000 m3)|0|0.84|0|
|C & E Loss (m)|0.02|Cum SA (1000 m2)|0.01|1.46|0.02|

E.G. Elev (m) 242.41 Element Left OB Channel Right OB E.G. Elev (m) 241.36 Element Left OB Channel Right OB

W.S. Elev (m) 242.23 Reach Len. (m) 50.43 50 49.46 W.S. Elev (m) 241.12 Reach Len. (m) 47.94 48.03 48.12

Alpha 1 Stream Power (N/m s) 396.61 0 0 Alpha 1 Stream Power (N/m s) 450.81 0 0

Frctn Loss (m) 1.04 Cum Volume (1000 m3) 0 0.61 0 Frctn Loss (m) 0.64 Cum Volume (1000 m3) 0 0.49 0

C & E Loss (m) 0.01 Cum SA (1000 m2) 0 1.1 0 C & E Loss (m) 0.03 Cum SA (1000 m2) 0 0.86 0

|Plan: P_SP TRAMO 2 E2 RS: 600 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|242.41|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.18|Wt. n-Val.||0.04||
|W.S. Elev (m)|242.23|Reach Len. (m)|50.43|50|49.46|
|Crit W.S. (m)|242.17|Flow Area (m2)||2.51||
|E.G. Slope (m/m)|0.018179|Area (m2)||2.51||
|Q Total (m3/s)|4.68|Flow (m3/s)||4.68||
|Top Width (m)|5.08|Top Width (m)||5.08||
|Vel Total (m/s)|1.86|Avg. Vel. (m/s)||1.86||
|Max Chl Dpth (m)|1.09|Hydr. Depth (m)||0.49||
|Conv. Total (m3/s)|34.7|Conv. (m3/s)||34.7||
|Length Wtd. (m)|50|Wetted Per. (m)||6.11||
|Min Ch El (m)|241.14|Shear (N/m2)||73.29||
|Alpha|1|Stream Power (N/m s)|396.61|0|0|
|Frctn Loss (m)|1.04|Cum Volume (1000 m3)|0|0.61|0|
|C & E Loss (m)|0.01|Cum SA (1000 m2)|0|1.1|0|

|Plan: P_SP TRAMO 2 E2 RS: 550 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|241.36|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.24|Wt. n-Val.||0.04||
|W.S. Elev (m)|241.12|Reach Len. (m)|47.94|48.03|48.12|
|Crit W.S. (m)|241.12|Flow Area (m2)||2.16||
|E.G. Slope (m/m)|0.024278|Area (m2)||2.16||
|Q Total (m3/s)|4.68|Flow (m3/s)||4.68||
|Top Width (m)|4.56|Top Width (m)||4.56||
|Vel Total (m/s)|2.16|Avg. Vel. (m/s)||2.16||
|Max Chl Dpth (m)|1.04|Hydr. Depth (m)||0.47||
|Conv. Total (m3/s)|30|Conv. (m3/s)||30||
|Length Wtd. (m)|48.03|Wetted Per. (m)||5.24||
|Min Ch El (m)|240.08|Shear (N/m2)||98.43||
|Alpha|1|Stream Power (N/m s)|450.81|0|0|
|Frctn Loss (m)|0.64|Cum Volume (1000 m3)|0|0.49|0|
|C & E Loss (m)|0.03|Cum SA (1000 m2)|0|0.86|0|

E.G. Elev (m) 240.34 Element Left OB Channel Right OB E.G. Elev (m) 240.32 Element Left OB Channel Right OB

W.S. Elev (m) 240.21 Reach Len. (m) 1.98 1.97 1.98 W.S. Elev (m) 240.19 Reach Len. (m) 49.81 50 50.13

Alpha 1 Stream Power (N/m s) 451.34 0 0 Alpha 1 Stream Power (N/m s) 434.63 0 0

Frctn Loss (m) 0.02 Cum Volume (1000 m3) 0 0.37 0 Frctn Loss (m) 0.53 Cum Volume (1000 m3) 0 0.36 0

C & E Loss (m) 0 Cum SA (1000 m2) 0 0.64 0 C & E Loss (m) 0 Cum SA (1000 m2) 0 0.63 0

|Plan: P_SP TRAMO 2 E2 RS: 500 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|240.34|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.12|Wt. n-Val.||0.04||
|W.S. Elev (m)|240.21|Reach Len. (m)|1.98|1.97|1.98|
|Crit W.S. (m)|240.03|Flow Area (m2)||3||
|E.G. Slope (m/m)|0.008459|Area (m2)||3||
|Q Total (m3/s)|4.68|Flow (m3/s)||4.68||
|Top Width (m)|4.88|Top Width (m)||4.88||
|Vel Total (m/s)|1.56|Avg. Vel. (m/s)||1.56||
|Max Chl Dpth (m)|0.82|Hydr. Depth (m)||0.62||
|Conv. Total (m3/s)|50.9|Conv. (m3/s)||50.9||
|Length Wtd. (m)|1.97|Wetted Per. (m)||5.38||
|Min Ch El (m)|239.39|Shear (N/m2)||46.28||
|Alpha|1|Stream Power (N/m s)|451.34|0|0|
|Frctn Loss (m)|0.02|Cum Volume (1000 m3)|0|0.37|0|
|C & E Loss (m)|0|Cum SA (1000 m2)|0|0.64|0|

|Plan: P_SP TRAMO 2 E2 RS: 467 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|240.32|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.13|Wt. n-Val.||0.04||
|W.S. Elev (m)|240.19|Reach Len. (m)|49.81|50|50.13|
|Crit W.S. (m)||Flow Area (m2)||2.98||
|E.G. Slope (m/m)|0.008683|Area (m2)||2.98||
|Q Total (m3/s)|4.68|Flow (m3/s)||4.68||
|Top Width (m)|4.89|Top Width (m)||4.89||
|Vel Total (m/s)|1.57|Avg. Vel. (m/s)||1.57||
|Max Chl Dpth (m)|0.82|Hydr. Depth (m)||0.61||
|Conv. Total (m3/s)|50.2|Conv. (m3/s)||50.2||
|Length Wtd. (m)|50|Wetted Per. (m)||5.38||
|Min Ch El (m)|239.38|Shear (N/m2)||47.13||
|Alpha|1|Stream Power (N/m s)|434.63|0|0|
|Frctn Loss (m)|0.53|Cum Volume (1000 m3)|0|0.36|0|
|C & E Loss (m)|0|Cum SA (1000 m2)|0|0.63|0|

E.G. Elev (m) 239.78 Element Left OB Channel Right OB E.G. Elev (m) 239.58 Element Left OB Channel Right OB

W.S. Elev (m) 239.61 Reach Len. (m) 20.21 20.21 20.21 W.S. Elev (m) 239.48 Reach Len. (m) 29.82 29.79 29.76

Alpha 1 Stream Power (N/m s) 393.27 0 0 Alpha 1 Stream Power (N/m s) 450.14 0 0

Frctn Loss (m) 0.18 Cum Volume (1000 m3) 0 0.23 0 Frctn Loss (m) 0.18 Cum Volume (1000 m3) 0 0.17 0

C & E Loss (m) 0.02 Cum SA (1000 m2) 0 0.39 0 C & E Loss (m) 0 Cum SA (1000 m2) 0 0.29 0

|Plan: P_SP TRAMO 2 E2 RS: 450 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|239.58|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.1|Wt. n-Val.|0.04|0.04||
|W.S. Elev (m)|239.48|Reach Len. (m)|29.82|29.79|29.76|
|Crit W.S. (m)||Flow Area (m2)|0|3.36||
|E.G. Slope (m/m)|0.00663|Area (m2)|0|3.36||
|Q Total (m3/s)|4.68|Flow (m3/s)|0|4.68||
|Top Width (m)|5.5|Top Width (m)|0.12|5.38||
|Vel Total (m/s)|1.39|Avg. Vel. (m/s)|0.12|1.39||
|Max Chl Dpth (m)|0.91|Hydr. Depth (m)|0.02|0.62||
|Conv. Total (m3/s)|57.5|Conv. (m3/s)|0|57.5||
|Length Wtd. (m)|29.79|Wetted Per. (m)|0.12|5.94||
|Min Ch El (m)|238.57|Shear (N/m2)|0.99|36.8||
|Alpha|1|Stream Power (N/m s)|450.14|0|0|
|Frctn Loss (m)|0.18|Cum Volume (1000 m3)|0|0.17|0|
|C & E Loss (m)|0|Cum SA (1000 m2)|0|0.29|0|

22

|Plan: P_SP TRAMO 2 E2 RS: 455 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|239.78|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.17|Wt. n-Val.||0.04||
|W.S. Elev (m)|239.61|Reach Len. (m)|20.21|20.21|20.21|
|Crit W.S. (m)||Flow Area (m2)||2.55||
|E.G. Slope (m/m)|0.013355|Area (m2)||2.55||
|Q Total (m3/s)|4.68|Flow (m3/s)||4.68||
|Top Width (m)|4.52|Top Width (m)||4.52||
|Vel Total (m/s)|1.83|Avg. Vel. (m/s)||1.83||
|Max Chl Dpth (m)|0.76|Hydr. Depth (m)||0.56||
|Conv. Total (m3/s)|40.5|Conv. (m3/s)||40.5||
|Length Wtd. (m)|20.21|Wetted Per. (m)||5.04||
|Min Ch El (m)|238.86|Shear (N/m2)||66.27||
|Alpha|1|Stream Power (N/m s)|393.27|0|0|
|Frctn Loss (m)|0.18|Cum Volume (1000 m3)|0|0.23|0|
|C & E Loss (m)|0.02|Cum SA (1000 m2)|0|0.39|0|

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

E.G. Elev (m) 239.4 Element Left OB Channel Right OB E.G. Elev (m) 239.34 Element Left OB Channel Right OB

W.S. Elev (m) 239.31 Reach Len. (m) 13.41 13.27 13.17 W.S. Elev (m) 239.22 Reach Len. (m) 11.04 11.03 11.03

E.G. Slope (m/m) 0.005365 Area (m2) 3.65 E.G. Slope (m/m) 0.00356 Area (m2) 0 4.34 0.01

Top Width (m) 5.37 Top Width (m) 5.37 Top Width (m) 5.8 Top Width (m) 0.13 5.42 0.26

Alpha 1 Stream Power (N/m s) 355.64 0 0 Alpha 1 Stream Power (N/m s) 356.02 0 0

C & E Loss (m) 0 Cum SA (1000 m2) 0 0.13 0 C & E Loss (m) Cum SA (1000 m2) 0 0.06 0

|Plan: P_SP TRAMO 2 E2 RS: 400 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|239.34|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.11|Wt. n-Val.||0.04||
|W.S. Elev (m)|239.22|Reach Len. (m)|11.04|11.03|11.03|
|Crit W.S. (m)|238.84|Flow Area (m2)||3.18||
|E.G. Slope (m/m)|0.00356|Area (m2)|0|4.34|0.01|
|Q Total (m3/s)|4.72|Flow (m3/s)||4.72||
|Top Width (m)|5.8|Top Width (m)|0.13|5.42|0.26|
|Vel Total (m/s)|1.49|Avg. Vel. (m/s)||1.49||
|Max Chl Dpth (m)|0.99|Hydr. Depth (m)||0.99||
|Conv. Total (m3/s)|79.1|Conv. (m3/s)||79.1||
|Length Wtd. (m)|11.03|Wetted Per. (m)||3.2||
|Min Ch El (m)|238.23|Shear (N/m2)||34.68||
|Alpha|1|Stream Power (N/m s)|356.02|0|0|
|Frctn Loss (m)||Cum Volume (1000 m3)||0.01||
|C & E Loss (m)||Cum SA (1000 m2)|0|0.06|0|

23

|Plan: P_SP TRAMO 2 E2 RS: 403 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|239.4|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.09|Wt. n-Val.||0.04||
|W.S. Elev (m)|239.31|Reach Len. (m)|13.41|13.27|13.17|
|Crit W.S. (m)||Flow Area (m2)||3.65||
|E.G. Slope (m/m)|0.005365|Area (m2)||3.65||
|Q Total (m3/s)|4.72|Flow (m3/s)||4.72||
|Top Width (m)|5.37|Top Width (m)||5.37||
|Vel Total (m/s)|1.29|Avg. Vel. (m/s)||1.29||
|Max Chl Dpth (m)|0.97|Hydr. Depth (m)||0.68||
|Conv. Total (m3/s)|64.4|Conv. (m3/s)||64.4||
|Length Wtd. (m)|13.27|Wetted Per. (m)||6.13||
|Min Ch El (m)|238.34|Shear (N/m2)||31.27||
|Alpha|1|Stream Power (N/m s)|355.64|0|0|
|Frctn Loss (m)|0.06|Cum Volume (1000 m3)|0|0.06|0|
|C & E Loss (m)|0|Cum SA (1000 m2)|0|0.13|0|

|Plan: P_SP TRAMO 2 E2 RS: 356 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|238.85|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.26|Wt. n-Val.||0.04||
|W.S. Elev (m)|238.59|Reach Len. (m)|8.33|8.27|8.29|
|Crit W.S. (m)|238.63|Flow Area (m2)||2.1||
|E.G. Slope (m/m)|0.029276|Area (m2)||2.1||
|Q Total (m3/s)|4.72|Flow (m3/s)||4.72||
|Top Width (m)|5.31|Top Width (m)||5.31||
|Vel Total (m/s)|2.24|Avg. Vel. (m/s)||2.24||
|Max Chl Dpth (m)|0.49|Hydr. Depth (m)||0.4||
|Conv. Total (m3/s)|27.6|Conv. (m3/s)||27.6||
|Length Wtd. (m)|8.27|Wetted Per. (m)||5.54||
|Min Ch El (m)|238.1|Shear (N/m2)||109.08||
|Alpha|1|Stream Power (N/m s)|478.58|0|0|
|Frctn Loss (m)||Cum Volume (1000 m3)||0.01||
|C & E Loss (m)||Cum SA (1000 m2)||||

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

**Tablas Perfiles Transversales Patagoniafresh Tramo 3**

E.G. Elev (m) 239.22 Element Left OB Channel Right OB E.G. Elev (m) 238.78 Element Left OB Channel Right OB

W.S. Elev (m) 238.31 Reach Len. (m) 17.99 17.43 16.93 W.S. Elev (m) 238.73 Reach Len. (m) 5.6 5.6 5.6

Alpha 1 Stream Power (N/m s) 467.52 0 0 Alpha 1 Stream Power (N/m s) 507.74 0 0

C & E Loss (m) 0.08 Cum SA (1000 m2) 2.17 C & E Loss (m) 0.01 Cum SA (1000 m2) 2.05

|Plan: P_SP TRAMO 3 E3 RS: 350 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|239.22|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.91|Wt. n-Val.||0.04||
|W.S. Elev (m)|238.31|Reach Len. (m)|17.99|17.43|16.93|
|Crit W.S. (m)|238.55|Flow Area (m2)||1.34||
|E.G. Slope (m/m)|0.182999|Area (m2)||1.34||
|Q Total (m3/s)|5.68|Flow (m3/s)||5.68||
|Top Width (m)|5.25|Top Width (m)||5.25||
|Vel Total (m/s)|4.23|Avg. Vel. (m/s)||4.23||
|Max Chl Dpth (m)|0.31|Hydr. Depth (m)||0.26||
|Conv. Total (m3/s)|13.3|Conv. (m3/s)||13.3||
|Length Wtd. (m)|17.43|Wetted Per. (m)||5.39||
|Min Ch El (m)|237.99|Shear (N/m2)||446.73||
|Alpha|1|Stream Power (N/m s)|467.52|0|0|
|Frctn Loss (m)|0|Cum Volume (1000 m3)||1.55||
|C & E Loss (m)|0.08|Cum SA (1000 m2)||2.17||

|Plan: P_SP TRAMO 3 E3 RS: 333 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|238.78|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.05|Wt. n-Val.||0.04||
|W.S. Elev (m)|238.73|Reach Len. (m)|5.6|5.6|5.6|
|Crit W.S. (m)|238.37|Flow Area (m2)||5.79||
|E.G. Slope (m/m)|0.002757|Area (m2)||5.79||
|Q Total (m3/s)|5.68|Flow (m3/s)||5.68||
|Top Width (m)|8.1|Top Width (m)||8.1||
|Vel Total (m/s)|0.98|Avg. Vel. (m/s)||0.98||
|Max Chl Dpth (m)|0.82|Hydr. Depth (m)||0.72||
|Conv. Total (m3/s)|108.2|Conv. (m3/s)||108.2||
|Length Wtd. (m)|5.6|Wetted Per. (m)||8.97||
|Min Ch El (m)|237.9|Shear (N/m2)||17.45||
|Alpha|1|Stream Power (N/m s)|507.74|0|0|
|Frctn Loss (m)|0.03|Cum Volume (1000 m3)||1.49||
|C & E Loss (m)|0.01|Cum SA (1000 m2)||2.05||

E.G. Elev (m) 238.74 Element Left OB Channel Right OB E.G. Elev (m) 238.48 Element Left OB Channel Right OB

W.S. Elev (m) 238.64 Reach Len. (m) 42.72 44.4 46.51 W.S. Elev (m) 238.39 Reach Len. (m) 3.72 2.64 1.66

Alpha 1 Stream Power (N/m s) 513.39 0 0 Alpha 1 Stream Power (N/m s) 698.3 0 0

C & E Loss (m) 0.01 Cum SA (1000 m2) 2.01 C & E Loss (m) 0 Cum SA (1000 m2) 1.7

|Plan: P_SP TRAMO 3 E3 RS: 325 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|238.74|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.1|Wt. n-Val.||0.04||
|W.S. Elev (m)|238.64|Reach Len. (m)|42.72|44.4|46.51|
|Crit W.S. (m)||Flow Area (m2)||3.99||
|E.G. Slope (m/m)|0.009582|Area (m2)||3.99||
|Q Total (m3/s)|5.68|Flow (m3/s)||5.68||
|Top Width (m)|8.42|Top Width (m)||8.42||
|Vel Total (m/s)|1.42|Avg. Vel. (m/s)||1.42||
|Max Chl Dpth (m)|0.63|Hydr. Depth (m)||0.47||
|Conv. Total (m3/s)|58|Conv. (m3/s)||58||
|Length Wtd. (m)|44.4|Wetted Per. (m)||8.99||
|Min Ch El (m)|238.01|Shear (N/m2)||41.71||
|Alpha|1|Stream Power (N/m s)|513.39|0|0|
|Frctn Loss (m)|0.26|Cum Volume (1000 m3)||1.46||
|C & E Loss (m)|0.01|Cum SA (1000 m2)||2.01||

|Plan: P_SP TRAMO 3 E3 RS: 314 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|238.48|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.08|Wt. n-Val.||0.04||
|W.S. Elev (m)|238.39|Reach Len. (m)|3.72|2.64|1.66|
|Crit W.S. (m)||Flow Area (m2)||4.45||
|E.G. Slope (m/m)|0.003975|Area (m2)||4.45||
|Q Total (m3/s)|5.68|Flow (m3/s)||5.68||
|Top Width (m)|5.19|Top Width (m)||5.19||
|Vel Total (m/s)|1.28|Avg. Vel. (m/s)||1.28||
|Max Chl Dpth (m)|1.13|Hydr. Depth (m)||0.86||
|Conv. Total (m3/s)|90.1|Conv. (m3/s)||90.1||
|Length Wtd. (m)|2.64|Wetted Per. (m)||6.1||
|Min Ch El (m)|237.26|Shear (N/m2)||28.44||
|Alpha|1|Stream Power (N/m s)|698.3|0|0|
|Frctn Loss (m)|0.01|Cum Volume (1000 m3)||1.28||
|C & E Loss (m)|0|Cum SA (1000 m2)||1.7||

E.G. Elev (m) 238.46 Element Left OB Channel Right OB E.G. Elev (m) 238.23 Element Left OB Channel Right OB

W.S. Elev (m) 238.37 Reach Len. (m) 48.56 47.36 46.06 W.S. Elev (m) 238.13 Reach Len. (m) 4.39 4.39 4.39

Alpha 1 Stream Power (N/m s) 751.53 0 0 Alpha 1 Stream Power (N/m s) 826.18 0 0

C & E Loss (m) 0 Cum SA (1000 m2) 1.69 C & E Loss (m) 0 Cum SA (1000 m2) 1.46

|Plan: P_SP TRAMO 3 E3 RS: 300 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|238.46|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.1|Wt. n-Val.||0.04||
|W.S. Elev (m)|238.37|Reach Len. (m)|48.56|47.36|46.06|
|Crit W.S. (m)||Flow Area (m2)||4.14||
|E.G. Slope (m/m)|0.004667|Area (m2)||4.14||
|Q Total (m3/s)|5.68|Flow (m3/s)||5.68||
|Top Width (m)|4.8|Top Width (m)||4.8||
|Vel Total (m/s)|1.37|Avg. Vel. (m/s)||1.37||
|Max Chl Dpth (m)|1.13|Hydr. Depth (m)||0.86||
|Conv. Total (m3/s)|83.1|Conv. (m3/s)||83.1||
|Length Wtd. (m)|47.36|Wetted Per. (m)||5.76||
|Min Ch El (m)|237.24|Shear (N/m2)||32.91||
|Alpha|1|Stream Power (N/m s)|751.53|0|0|
|Frctn Loss (m)|0.23|Cum Volume (1000 m3)||1.26||
|C & E Loss (m)|0|Cum SA (1000 m2)||1.69||

|Plan: P_SP TRAMO 3 E3 RS: 271 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|238.23|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.1|Wt. n-Val.||0.04||
|W.S. Elev (m)|238.13|Reach Len. (m)|4.39|4.39|4.39|
|Crit W.S. (m)||Flow Area (m2)||4.04||
|E.G. Slope (m/m)|0.005154|Area (m2)||4.04||
|Q Total (m3/s)|5.68|Flow (m3/s)||5.68||
|Top Width (m)|4.88|Top Width (m)||4.88||
|Vel Total (m/s)|1.41|Avg. Vel. (m/s)||1.41||
|Max Chl Dpth (m)|1.15|Hydr. Depth (m)||0.83||
|Conv. Total (m3/s)|79.1|Conv. (m3/s)||79.1||
|Length Wtd. (m)|4.39|Wetted Per. (m)||5.82||
|Min Ch El (m)|236.99|Shear (N/m2)||35.06||
|Alpha|1|Stream Power (N/m s)|826.18|0|0|
|Frctn Loss (m)|0.02|Cum Volume (1000 m3)||1.07||
|C & E Loss (m)|0|Cum SA (1000 m2)||1.46||

E.G. Elev (m) 238.21 Element Left OB Channel Right OB E.G. Elev (m) 238.14 Element Left OB Channel Right OB

W.S. Elev (m) 238.1 Reach Len. (m) 12.14 12.13 12.13 W.S. Elev (m) 238.04 Reach Len. (m) 33.43 33.48 33.53

Alpha 1 Stream Power (N/m s) 825.46 0 0 Alpha 1 Stream Power (N/m s) 797.5 0 0

C & E Loss (m) 0 Cum SA (1000 m2) 1.44 C & E Loss (m) 0 Cum SA (1000 m2) 1.38

|Plan: P_SP TRAMO 3 E3 RS: 250 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|238.21|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.1|Wt. n-Val.||0.04||
|W.S. Elev (m)|238.1|Reach Len. (m)|12.14|12.13|12.13|
|Crit W.S. (m)||Flow Area (m2)||4||
|E.G. Slope (m/m)|0.005357|Area (m2)||4||
|Q Total (m3/s)|5.72|Flow (m3/s)||5.72||
|Top Width (m)|4.85|Top Width (m)||4.85||
|Vel Total (m/s)|1.43|Avg. Vel. (m/s)||1.43||
|Max Chl Dpth (m)|1.15|Hydr. Depth (m)||0.82||
|Conv. Total (m3/s)|78.2|Conv. (m3/s)||78.2||
|Length Wtd. (m)|12.13|Wetted Per. (m)||5.78||
|Min Ch El (m)|236.96|Shear (N/m2)||36.32||
|Alpha|1|Stream Power (N/m s)|825.46|0|0|
|Frctn Loss (m)|0.06|Cum Volume (1000 m3)||1.05||
|C & E Loss (m)|0|Cum SA (1000 m2)||1.44||

|Plan: P_SP TRAMO 3 E3 RS: 200 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|238.14|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.1|Wt. n-Val.||0.04||
|W.S. Elev (m)|238.04|Reach Len. (m)|33.43|33.48|33.53|
|Crit W.S. (m)||Flow Area (m2)||3.99||
|E.G. Slope (m/m)|0.005292|Area (m2)||3.99||
|Q Total (m3/s)|5.72|Flow (m3/s)||5.72||
|Top Width (m)|4.78|Top Width (m)||4.78||
|Vel Total (m/s)|1.43|Avg. Vel. (m/s)||1.43||
|Max Chl Dpth (m)|1.15|Hydr. Depth (m)||0.83||
|Conv. Total (m3/s)|78.6|Conv. (m3/s)||78.6||
|Length Wtd. (m)|33.48|Wetted Per. (m)||5.7||
|Min Ch El (m)|236.89|Shear (N/m2)||36.31||
|Alpha|1|Stream Power (N/m s)|797.5|0|0|
|Frctn Loss (m)|0.16|Cum Volume (1000 m3)||1.01||
|C & E Loss (m)|0|Cum SA (1000 m2)||1.38||

E.G. Elev (m) 237.98 Element Left OB Channel Right OB E.G. Elev (m) 237.73 Element Left OB Channel Right OB

W.S. Elev (m) 237.89 Reach Len. (m) 50.22 50 49.73 W.S. Elev (m) 237.62 Reach Len. (m) 49.61 50 50.52

Alpha 1 Stream Power (N/m s) 755.18 0 0 Alpha 1 Stream Power (N/m s) 832.75 0 0

C & E Loss (m) 0 Cum SA (1000 m2) 1.22 C & E Loss (m) 0.02 Cum SA (1000 m2) 0.96

|Plan: P_SP TRAMO 3 E3 RS: 150 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|237.73|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.11|Wt. n-Val.||0.04||
|W.S. Elev (m)|237.62|Reach Len. (m)|49.61|50|50.52|
|Crit W.S. (m)||Flow Area (m2)||3.93||
|E.G. Slope (m/m)|0.005852|Area (m2)||3.93||
|Q Total (m3/s)|5.72|Flow (m3/s)||5.72||
|Top Width (m)|5.26|Top Width (m)||5.26||
|Vel Total (m/s)|1.45|Avg. Vel. (m/s)||1.45||
|Max Chl Dpth (m)|1.07|Hydr. Depth (m)||0.75||
|Conv. Total (m3/s)|74.8|Conv. (m3/s)||74.8||
|Length Wtd. (m)|50|Wetted Per. (m)||5.93||
|Min Ch El (m)|236.55|Shear (N/m2)||38.05||
|Alpha|1|Stream Power (N/m s)|832.75|0|0|
|Frctn Loss (m)|0.14|Cum Volume (1000 m3)||0.66||
|C & E Loss (m)|0.02|Cum SA (1000 m2)||0.96||

24

|Plan: P_SP TRAMO 3 E3 RS: 198 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|237.98|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.09|Wt. n-Val.||0.04||
|W.S. Elev (m)|237.89|Reach Len. (m)|50.22|50|49.73|
|Crit W.S. (m)||Flow Area (m2)||4.34||
|E.G. Slope (m/m)|0.004216|Area (m2)||4.34||
|Q Total (m3/s)|5.72|Flow (m3/s)||5.72||
|Top Width (m)|5.1|Top Width (m)||5.1||
|Vel Total (m/s)|1.32|Avg. Vel. (m/s)||1.32||
|Max Chl Dpth (m)|1.18|Hydr. Depth (m)||0.85||
|Conv. Total (m3/s)|88.1|Conv. (m3/s)||88.1||
|Length Wtd. (m)|50|Wetted Per. (m)||5.93||
|Min Ch El (m)|236.71|Shear (N/m2)||30.25||
|Alpha|1|Stream Power (N/m s)|755.18|0|0|
|Frctn Loss (m)|0.25|Cum Volume (1000 m3)||0.87||
|C & E Loss (m)|0|Cum SA (1000 m2)||1.22||

Cruz Consultores Limitada

Anexo: Modelo Hidráulico SP

E.G. Elev (m) 237.57 Element Left OB Channel Right OB E.G. Elev (m) 237.46 Element Left OB Channel Right OB

W.S. Elev (m) 237.53 Reach Len. (m) 44.06 44.1 44.27 W.S. Elev (m) 237.37 Reach Len. (m) 30.15 30.36 30.77

Alpha 1 Stream Power (N/m s) 738.28 0 0 Alpha 1 Stream Power (N/m s) 599.87 0 0

C & E Loss (m) 0 Cum SA (1000 m2) 0.64 C & E Loss (m) Cum SA (1000 m2) 0.28

|Plan: P_SP TRAMO 3 E3 RS: 100 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|237.57|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.04|Wt. n-Val.||0.04||
|W.S. Elev (m)|237.53|Reach Len. (m)|44.06|44.1|44.27|
|Crit W.S. (m)||Flow Area (m2)||6.41||
|E.G. Slope (m/m)|0.001713|Area (m2)||6.41||
|Q Total (m3/s)|5.72|Flow (m3/s)||5.72||
|Top Width (m)|7.29|Top Width (m)||7.29||
|Vel Total (m/s)|0.89|Avg. Vel. (m/s)||0.89||
|Max Chl Dpth (m)|1.25|Hydr. Depth (m)||0.88||
|Conv. Total (m3/s)|138.2|Conv. (m3/s)||138.2||
|Length Wtd. (m)|44.1|Wetted Per. (m)||8||
|Min Ch El (m)|236.28|Shear (N/m2)||13.46||
|Alpha|1|Stream Power (N/m s)|738.28|0|0|
|Frctn Loss (m)|0.11|Cum Volume (1000 m3)||0.4||
|C & E Loss (m)|0|Cum SA (1000 m2)||0.64||

|Plan: P_SP TRAMO 3 E3 RS: 50 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|237.46|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.09|Wt. n-Val.||0.04||
|W.S. Elev (m)|237.37|Reach Len. (m)|30.15|30.36|30.77|
|Crit W.S. (m)|237.04|Flow Area (m2)||4.3||
|E.G. Slope (m/m)|0.003655|Area (m2)||5.83||
|Q Total (m3/s)|5.72|Flow (m3/s)||5.72||
|Top Width (m)|9.18|Top Width (m)||9.18||
|Vel Total (m/s)|1.33|Avg. Vel. (m/s)||1.33||
|Max Chl Dpth (m)|0.83|Hydr. Depth (m)||0.83||
|Conv. Total (m3/s)|94.6|Conv. (m3/s)||94.6||
|Length Wtd. (m)|30.36|Wetted Per. (m)||5.2||
|Min Ch El (m)|236.54|Shear (N/m2)||29.62||
|Alpha|1|Stream Power (N/m s)|599.87|0|0|
|Frctn Loss (m)||Cum Volume (1000 m3)||0.13||
|C & E Loss (m)||Cum SA (1000 m2)||0.28||

E.G. Elev (m) 237.35 Element Left OB Channel Right OB E.G. Elev (m) 237.34 Element Left OB Channel Right OB

Alpha 1 Stream Power (N/m s) 557.2 0 0 Alpha 1 Stream Power (N/m s) 557.2 0 0

|Plan: P_SP TRAMO 3 E3 RS: 0 Profile: T100<br>E.G. Elev (m) 237.34 Element Left OB Channel Right OB|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Vel Head (m)|0.1|Wt. n-Val.||0.04||
|W.S. Elev (m)|237.24|Reach Len. (m)||||
|Crit W.S. (m)|237.07|Flow Area (m2)||4.1||
|E.G. Slope (m/m)<br> Q Total (m3/s)|0.007812<br>5.72|Area (m2)<br> Flow (m3/s)|<br>|4.1<br>5.72|<br>|
|Top Width (m)|7.97|Top Width (m)||7.97||
|Vel Total (m/s)|1.39|Avg. Vel. (m/s)||1.39||
|Max Chl Dpth (m)|0.83|Hydr. Depth (m)||0.52||
|Conv. Total (m3/s)|64.7|Conv. (m3/s)||64.7||
|Length Wtd. (m)||Wetted Per. (m)||8.18||
|Min Ch El (m)|236.42|Shear (N/m2)||38.4||
|Alpha|1|Stream Power (N/m s)|557.2|0|0|
|Frctn Loss (m)||Cum Volume (1000 m3)||||
|C & E Loss (m)||Cum SA (1000 m2)||||

25

|Plan: P_SP TRAMO 3 E3 RS: 13 Profile: T100|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|E.G. Elev (m)|237.35|Element|Left OB|Channel|Right OB|
|Vel Head (m)|0.04|Wt. n-Val.||0.04||
|W.S. Elev (m)|237.31|Reach Len. (m)|0.55|0.54|0.55|
|Crit W.S. (m)||Flow Area (m2)||6.21||
|E.G. Slope (m/m)|0.002341|Area (m2)||6.21||
|Q Total (m3/s)|5.72|Flow (m3/s)||5.72||
|Top Width (m)|8.95|Top Width (m)||8.95||
|Vel Total (m/s)|0.92|Avg. Vel. (m/s)||0.92||
|Max Chl Dpth (m)|0.88|Hydr. Depth (m)||0.69||
|Conv. Total (m3/s)|118.2|Conv. (m3/s)||118.2||
|Length Wtd. (m)|0.54|Wetted Per. (m)||9.34||
|Min Ch El (m)|236.43|Shear (N/m2)||15.26||
|Alpha|1|Stream Power (N/m s)|557.2|0|0|
|Frctn Loss (m)|0|Cum Volume (1000 m3)||0||
|C & E Loss (m)|0.01|Cum SA (1000 m2)||0||

Cruz Consultores Limitada

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: ****

| Factor | Condición | Col3 | Valor |
| --- | --- | --- | --- |
| n0 | Material del lecho | Grava Gruesa | 0.028 |
| n1 | Irregul. Perímetro mojado | Leve | 0.005 |
| n2 | Variación sección | Graduales | 0.000 |
| n3 | Obstrucciones | Despreciable | 0.000 |
| n4 | Densidad vegetación | Baja | 0.005 |
| **Suma** | **Suma** | **Suma** | **0.038** |
| m | 1.000 | Leve | 1,00 |
| **n ** | **n ** | **n ** | **0.038** |

**Tabla 2: ****

| Condición | Contracción | Expansión |
| --- | --- | --- |
| Sin pérdida medible | 0,0 | 0,0 |
| Transición gradual | 0,1 | 0,3 |
| Sección típica de puentes | 0,3 | 0,5 |
| Transición brusca | 0,6 | 0,8 |

**Tabla 3: ****

| Parámetro | Valor | Observación |
| --- | --- | --- |
| Caudal | Q1 = 1,0 m~~3~~/s (Tramo 1)<br>Q2 = 4,68 m3/s (Tramo 2)<br>Q3 = 5,68 m3/s (Tramo 3)<br>Q4 = 5,72 m3/s (Tramo 3)<br>Q5 = 4,72 m3/s (Tramo 2)<br> | T100, Periodo de retorno de<br>100 años<br>Q1, por porteo<br>Q4 y Q5, suma de descargas<br>PETAS Q=0,04 m3/s c/u |
| Condición de<br>borde | Primer y último Perfil:<br>Pendiente Normal | Pend. A. Arriba S =0.0078<br>(Tramo 1)<br>Pend. A. Arriba S =0.01<br>(Tramo 2)<br>Pend. A. Abajo S =0.0078<br>(Tramo 3) |
| Flujo | Uniforme | Unidimensional |
| Régimen | Mixto | Modelación |

**Tabla 4: ****

| Estación<br>del Río | Periodo<br>modelo | PT | Dm | Caudal<br>Total | Elev. Mín<br>Fondo | Altura de<br>Agua | Altura<br>Crítica | Línea de<br>Energía | Pend.<br>Hidráulica | Velocidad | Área de<br>Flujo | Ancho<br>Superior | Radio<br>Hidráulico | No Froud | Tirante |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Estación<br>del Río | Periodo<br>modelo | PT | Dm | (m3/s) | (m) | (m) | (m) | (m) | (m/m) | (m/s) | (m2) | (m) | (m) |  | (m) |
| 545 | T100 | 1 | 0 | 1.00 | 242.32 | 242.72 | 242.53 | 242.74 | 0.0029 | 0.57 | 1.75 | 6.17 | 0.28 | 0.34 | 0.40 |
| 500 | T100 | 2 | 50 | 1.00 | 242.16 | 242.39 |  | 242.44 | 0.0169 | 1.07 | 0.93 | 4.86 | 0.19 | 0.78 | 0.23 |
| 450 | T100 | 3 | 86.3 | 1.00 | 241.83 | 242.13 | 242.00 | 242.16 | 0.0043 | 0.74 | 1.36 | 4.65 | 0.30 | 0.43 | 0.30 |
| 420 |  |  |  | Culvert |  |  |  |  |  |  |  |  |  |  |  |
| 411 | T100 | 4 | 103 | 1.00 | 241.68 | 242.13 |  | 242.14 | 0.0012 | 0.45 | 2.21 | 5.31 | 0.39 | 0.22 | 0.45 |
| 400 | T100 | 5 | 116.3 | 1.00 | 241.55 | 242.07 |  | 242.11 | 0.0047 | 0.85 | 1.18 | 3.06 | 0.35 | 0.44 | 0.53 |
| 395 | T100 | 6 | 149.1 | 1.00 | 241.23 | 241.65 | 241.65 | 241.79 | 0.0283 | 1.65 | 0.60 | 2.21 | 0.25 | 1.01 | 0.42 |
| 311 | T100 | 7 | 149.9 | 1.00 | 240.79 | 241.07 | 241.24 | 241.69 | 0.2159 | 3.49 | 0.29 | 1.56 | 0.16 | 2.61 | 0.29 |
| 300 | T100 | 8 | 196.9 | 1.00 | 240.47 | 241.11 | 240.90 | 241.16 | 0.0062 | 0.99 | 1.01 | 2.37 | 0.35 | 0.48 | 0.64 |
| 254 | T100 | 9 | 199.9 | 1.00 | 240.43 | 241.09 |  | 241.14 | 0.0058 | 0.96 | 1.04 | 2.37 | 0.36 | 0.47 | 0.66 |
| 252 | T100 | 10 | 201.7 | 1.00 | 240.41 | 241.08 |  | 241.13 | 0.0077 | 0.95 | 1.06 | 3.21 | 0.28 | 0.53 | 0.67 |
| 250 | T100 | 11 | 203.9 | 1.00 | 240.38 | 241.07 |  | 241.11 | 0.0067 | 0.91 | 1.09 | 3.11 | 0.30 | 0.49 | 0.69 |
| 247 | T100 | 12 | 249.9 | 1.00 | 240.18 | 240.91 |  | 240.93 | 0.0025 | 0.71 | 1.41 | 2.60 | 0.43 | 0.31 | 0.73 |
| 200 | T100 | 13 | 260.7 | 1.00 | 240.21 | 240.87 |  | 240.90 | 0.0032 | 0.74 | 1.34 | 2.97 | 0.38 | 0.35 | 0.66 |
| 150 | T100 | 14 | 299.9 | 1.00 | 240.03 | 240.75 |  | 240.78 | 0.0030 | 0.75 | 1.33 | 2.68 | 0.41 | 0.34 | 0.72 |
| 149 | T100 | 15 | 344.5 | 1.00 | 239.91 | 240.56 |  | 240.60 | 0.0056 | 0.93 | 1.07 | 2.63 | 0.35 | 0.47 | 0.65 |
| 117 | T100 | 16 | 349.9 | 1.00 | 239.91 | 240.52 |  | 240.57 | 0.0061 | 0.96 | 1.05 | 2.57 | 0.34 | 0.48 | 0.61 |
| 103 | T100 | 17 | 360.8 | 1.00 | 239.84 | 240.45 |  | 240.50 | 0.0073 | 0.99 | 1.01 | 2.77 | 0.32 | 0.52 | 0.61 |
| 100 | T100 | 18 | 370.8 | 1.00 | 239.78 | 240.34 |  | 240.40 | 0.0120 | 1.15 | 0.87 | 2.80 | 0.27 | 0.66 | 0.56 |
| 86 | T100 | 19 | 399.9 | 1.00 | 239.59 | 240.02 |  | 240.09 | 0.0099 | 1.09 | 0.92 | 2.86 | 0.29 | 0.62 | 0.44 |
| 50 | T100 | 20 | 449.9 | 1.00 | 238.79 | 239.16 | 239.16 | 239.30 | 0.0281 | 1.66 | 0.60 | 2.15 | 0.25 | 1.00 | 0.36 |
