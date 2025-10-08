---
title: Sin título
author: Felipe de França
date: D:20240614122640-03'00'
language: en
type: report
pages: 21
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - PARA APROBACIÓN FOR APPROVAL
  - Index:
-->

Status:

**C L A S I F I C A T I O N OF INFORMATION**

_I N T E R I O R_

# PARA APROBACIÓN FOR APPROVAL

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|0A|Emisión Inicial / Initial Issue|05/23/2024|MUA|PI|RB|
|**Versión/**<br>**Version**|**Descripción/Description**|**Fecha/Date**|**Preparado/**<br>**Designed**<br>**by **|**Verificado/**<br>**Verified by**|**Aprobado/**<br>**Approved by**|

Proyecto/Project

|Calendario de Revisiones / Revision Control Table|Col2|Col3|
|---|---|---|
||Proveedor/Supplier<br>|Proveedor/Supplier<br>|
||Código/Code|SSCLHB01-G-PQC-DC01-CI50-<br>RT-0001-0A|
||Versión/Version|0A|

## HUECHURABA - SSCLHB01

Fase/Phase
## BASIC DESIGN Título/Title RAINWATER SPECIALTY DESCRIPTIVE REPORT

SCALA

_Código: FR-EEC-08-01_

# Index:

_1.0_ _GENERAL TOPIC_ _2_
_1.1_ _Sector under Study_ _2_
_2.0_ _HYDROLOGY_ _3_
2.1 Isohyet Map Method and Frequency Coefficients 3

2.1.1 Maximum Precipitation in 24hrs T=100 3

2.1.2 Frequency Coefficients 4

2.1.3 Maximum Rainfall with Frequency Coefficient 5

2.2 Rainfall Information and Probability Distribution Functions Method 6

2.2.1 Rainfall Station Data 6

2.2.2 Probability Distribution Functions 1

2.2.3 Goodness of Fit 4

2.2.4 Maximum Rainfall according to Normal Log Function 5

2.3 Summary and Conclusions 6

_3.0_ _GEOHECRAS MODELLING_ _6_

3.1 Runoff flow 6

3.2 Modelling Result 9

_4.0_ _CONCLUSION_ _11_

_Table 1: Maximum Rainfall according to the Maximum Rainfall Manual for 1, 2 and 3 days DGA._ _7_
_Table 2: Average Daily Precipitation Month (mm)_ _9_
_Table 3: Functions Distribution_ _Parameters_ _14_

_Table 4: Goodness of Fit Result_ _14_

_Table 5: Maximum Rainfall - Maximum Gumbel Distribution Function_ _16_

_Table 6: Morphometric Parameters_ _17_
_Table 7: Rainfall Intensity (mm/hr)_ _18_
_Table 8: Runoff Coefficients_ _18_

_Table 9: Runoff Flows (m3/s)_ _19_

_Illustration 1: Land under study location_ _4_
_Illustration 2: Isohyets map for 1, 2 and 3 days DGA._ _5_
_Illustration 3: Frequency Coefficients_ _6_
_Illustration 4: Weather Station Data_ _8_
_Illustration 5: INIA - Quinta Normal Agrometeorological Station Location_ _11_
_Illustration 6: Normal Function - Probability Density_ _12_
_Illustration 7: Maximum Gumbel Function - Probability Density_ _12_
_Illustration 8: Pearson Function - Probability Density_ _13_
_Illustration 9: Lognormal Function - Probability Density_ _13_
_Illustration 10: Cumulative Distribution Graph - Lognormal Function_ _15_
_Illustration 11: Terrain Huechuraba 2D Model_ _20_
_Illustration 12: Flood area with water height_ _21_

DATA CENTER SCALA, HUECHURABA - General Study

1.0 GENERAL TOPIC

The objective of this paper is to develop the Hydrological Study in Huechuraba’s Commune, specifically

where SCALA Company Data Center is projected.

The study’s development has the goal to determine the rainfall for a duration of 24 hours for different return

periods from 2 to 200 years. To achieve this goal, it is considered to use two methods, which are:

1. Determination of Maximum Rainfall for different return periods, according to the DGA’s Isohyeta

Maps, and subsequent application of frequency coefficients of the Roads Directorate’s Highway

Manual.

2. Determination of Maximum Rainfall for different return periods by applying probability distribution

functions to rainfall information downloaded from the DGAC station, Quinta Normal, Santiago.

1.1 Sector under Study

The land to be analyzed is in Huechuraba’s Commune, near the Plaza Norte Mall, north of Américo Vespucio

and west of Route 5 North, according to the following image.

_Illustration 1: Land under study location_

The site of the SCALA Data Center is considered on the aforementioned land.

2

DATA CENTER SCALA, HUECHURABA - General Study

2.0 HYDROLOGY

The calculation to determine the maximum precipitation in 24 hours for different return periods, according to

two calculation methodologies, is presented below.

2.1 Isohyet Map Method and Frequency Coefficients

According to the DGA's Manual of Maximum Rainfall for 1, 2 and 3 days, it is possible to determine the

maximum precipitation for a duration t and frequency T, according to the following expression.

P t [T] = CF t [T] x CD t x P 24 [100 ]

Where:

P t [T] = Maximum precipitation in mm, with duration t and frequency T.

CF t [T] = Frequency Coefficient for Return Period T and Duration t.

CD t = Duration Coefficient for time t.

P 24 [100] = Maximum rainfall in mm, for a duration of 24 hours and return period 100 years.

2.1.1 Maximum Precipitation in 24hrs T=100

According to the data above, it is necessary to determine the maximum rainfall in 24 hours and a return

period of 100 years for the area under study, for which the Manual mentioned above, "Maximum Rainfall for

1, 2 and 3 days" of the DGA, is used.

3

DATA CENTER SCALA, HUECHURABA - General Study

_Illustration 2: Isohyets map for 1, 2 and 3 days DGA._

According to the previous image, the Maximum Precipitation for 24 hours and T=100 years for the area under

study, is equivalent to **P** **24** **[100]** **=105mm.**

2.1.2 Frequency Coefficients

Considering that it is necessary to determine the maximum precipitation while maintaining the duration of 24

hours, but with different return periods, it is necessary to know the Frequency Coefficient.

The frequency coefficients used were obtained from the Road Directorate’ Highway Manual in accordance

with Table 3.702.403B for the Santiago Quinta Normal Station, being the most complete in statistics to the

place under study.

4

DATA CENTER SCALA, HUECHURABA - General Study

_Illustration 3: Frequency Coefficients_

Labels
Estación pluviográfica = Raingauge station
Período de retorno (años) = Return Period (Years)

2.1.3 Maximum Rainfall with Frequency Coefficient

Applying the formula mentioned in point 2.1 together with the precipitation P24100=105mm and the

frequency coefficients of the previous Table, the following rainfall is obtained.

5

DATA CENTER SCALA, HUECHURABA - General Study

_Table 1: Maximum Rainfall according to the Maximum Rainfall Manual for 1, 2 and 3 days DGA._

Labels
Estación Santiago = Santiago station
Precipitación 24hrs para T (mm) = Precipitation 24hrs to T (mm)

2.2 Rainfall Information and Probability Distribution Functions Method

This method consists of processing the rainfall information of a station near the place under study, and then

applying at least 3 probability distribution functions, usually being those recommended by the DGA for this

type of study; Normal, Gumbel Max, Lognormal and Pearson.

Subsequently, a Goodness of Fit method is applied, which in this case are Kolmogorov Smirnov, Anderson

Darling and Chi Square, and then select the best-fitting function.

After that, the value of precipitation is calculated for a certain probability of occurrence associated with the

required return time.

2.2.1 Rainfall Station Data

The data used corresponds to the Quinta Normal-Santiago station of the Chilean Meteorological Directorate,

with information from January 1950 to May 2024. However, information obtained from the General

Directorate of Civil Aeronautics, Meteorological Directorate of Chile- Climate Services, which has the

Climatological Yearbook, where we have information archived by this entity, and which complements us from

the year 1950 to the year 1920, fulfilling the 100 historical years requested.

The information at source is available at:

_**[https://climatologia.meteochile.gob.cl/application/publicaciones/anuario,](https://climatologia.meteochile.gob.cl/application/publicaciones/anuario)**_

_**[https://www.cr2.cl/datos-de-precipitacion/?cp_Precipitacion=2,](https://www.cr2.cl/datos-de-precipitacion/?cp_Precipitacion=2)**_

_**[https://climatologia.meteochile.gob.cl/application/informacion/buscadorEstaciones](https://climatologia.meteochile.gob.cl/application/informacion/buscadorEstaciones)**_

6

DATA CENTER SCALA, HUECHURABA - General Study

The monthly climatological bulletin synthesizes and provides a vision of the month’s climatological behaviour.

This bulletin arises from the need to plan the various national activities in the medium term.

It satisfies the need for information that the community has and the understanding of the monthly behaviour

of climatological variables.

Table Number 2 shows the rainfall with which the calculations required for the results presented are made.

_Illustration 4: Weather Station Data_

In this case, the maximum average rainfall in 24 hours that occurred during each month was used, with which

the following table was obtained.

7

DATA CENTER SCALA, HUECHURABA - General Study

_Table 2: Average Daily Precipitation/Month (mm)_

Labels

Mes = Month
Enero = January
Febrero = February

March = Marzo

Abril = April
Mayo = May
Junio = June

Julio = July
Agosto = August
Septiembre = September

Octubre = October

Noviembre = November

Diciembre = December

8

Labels

Mes = Month
Enero = January
Febrero = February

March = Marzo

Abril = April
Mayo = May
Junio = June

Julio = July
Agosto = August
Septiembre = September

Octubre = October

Noviembre = November

Diciembre = December

_Illustration 5: INIA - Quinta Normal Agrometeorological Station Location_

2.2.2 Probability Distribution Functions

For the processing of rainfall information, the Easyfit 5.5 Software was used for the application of the following

distribution functions:

 - Normal

 - Gumbel Máximo

 - Pearson

 Lognormal

The probability distribution graphs are as follows:

DATA CENTER SCALA, HUECHURABA - General Study

_Illustration 6: Normal Function - Probability Density_

Labels
Función de densidad de probabilidad = Probability density function

_Illustration 7: Maximum Gumbel Function - Probability Density_

Labels
Función de densidad de probabilidad = Probability density function

2

DATA CENTER SCALA, HUECHURABA - General Study

_Illustration 8: Pearson Function - Probability Density_

Labels
Función de densidad de probabilidad = Probability density function

_Illustration 9: Lognormal Function - Probability Density_

Labels
Función de densidad de probabilidad = Probability density function

3

DATA CENTER SCALA, HUECHURABA - General Study

_Table 3: Functions Distribution Parameters_

Labels
Distribución = Distribution

Parámetros = Parameters

2.2.3 Goodness of Fit

To process rainfall`s information, Easyfit 5.5 Software was used, for the application of the following

distribution functions:

1. Kolmogorov-Smirnov

2. Anderson-Darling

3. Chi Square

The results obtained according to the Software are as followed:

_Table 4: Goodness of Fit Result_

Labels

Distribución = Distribution

Estadística = Statistics

Rango = Range
Chi-cuadrado = Chi-Square

4

DATA CENTER SCALA, HUECHURABA - General Study

According to the table above, the Maximum Gumbel function is in first place for the Chi-Square and Anderson

Darling Tests, and in second place for the Kolmogorov Smirnov Test, therefore, the **Maximum Gumbel**

distribution function is selected as the best fit to calculate the Maximum Precipitation values.

The cumulative distribution graph is as follows.

_Illustration 10: Cumulative Distribution Graph - Lognormal Function_

Labels
Función de distribución acumulativa = Cumulative distribution function

2.2.4 Maximum Rainfall according to Normal Log Function

According to the graphic above, it is possible to calculate the value of precipitation according to the value of

F(x) and the return period T, this relationship being as:

F(x) = 1 − [1]

T
Being:

T: Return period to use.

5

DATA CENTER SCALA, HUECHURABA - General Study

In accordance with the data above, the precipitation values, according to the rainfall information for 5 years,

are as follows:

_Table 5: Maximum Rainfall - Maximum Gumbel Distribution Function_

Labels
Período de Retorno (T) = Return Period (T)
Precipitación (24hrs) (mm) = Precipitation (24hrs) (mm)

2.3 Summary and Conclusions

It is observed that there are a lot of similarities between one method and the other, with the precipitation

values in 24 hours for T=100 using the Isohyetas Map equal to P=105.0mm and P=99.81mm using rainfall

information from the last 100 years.

In the case of the method of applying the distribution functions, the average daily rainfall that occurred in a

month in the last 100 years was used.

**According to the information above, the maximum rainfall in 24 hours for a return period of T=100**

**amounts to a value of P24100=99.81mm of water, according to rainfall information for the last 100**

**years.**

3.0 GEOHECRAS MODELLING

To determine the points of accumulation of water in the ground, a 2D modelling is carried out using the Geo

Hec-Ras Software, for which it is considered to determine the flow that could drain through the ground

considering a flow for a return period of 100 years.

To carry out the above, it is necessary to determine the aforementioned flow rate.

3.1 Runoff flow

6

DATA CENTER SCALA, HUECHURABA - General Study

In the runoff flow calculation, the rational formula will be applied:

Q= [C x i x A]

3.6

Where:

Q: is the flow rate in m3/s

I: rain intensity in mm/hr

A: area in km2

Therefore, the previous parameters must be defined in order to calculate the contributing flows.

Area:

The land was divided into thirds with an approximate area of 0.5 hectares each. The following morphometric

data were obtained.

_Table 6: Morphometric Parameters_

Labels
Area (km2) = Area (km2)
Longidud (km) = Longitud (km)
Desnivel medio (m) = Average level difference (m)
Desnivel máximo (m) = Maximum level difference (m)

Pendiente (m/m) = Slope (m/m)

Rain intensity:

Considering the precipitation in 24 hours with T=100 determined through the use of area rainfall information

and the application of distribution functions, it was obtained that the P24100=99.81mm (Table N°5).

7

DATA CENTER SCALA, HUECHURABA - General Study

The area concentration time was obtained by means of Kirpich's formula, which yielded a value of t=3.5min.

Finally, obtaining the rainfall intensities for different return periods.

_Table 7: Rainfall Intensity (mm/hr)_

Labels
Período de Retorno (T) = Return Period (T)

Intensidad (mm/h) = Intensity (mm/h)

Flows:

Finally, the runoff coefficients applied according to each return period are:

_Table 8: Runoff Coefficients_

Labels
Período de Retorno (T) = Return Period (T)

C corregido = Corrected C

And applying the formula, the following flow values are obtained.

8

DATA CENTER SCALA, HUECHURABA - General Study

_Table 9: Runoff Flows (m3/s)_

Labels

Método Racional = Rational Method
Período de Retorno (T) = Return Period (T)

3.2 Modelling Result

The model considers a period of 24 hours with the runoff flow on 3 sides towards a low point, where the water

should evacuate.

The generated model considered a mesh on a DEM (Digital Elevation Model) extracted from the same

software, according to the following image.

9

DATA CENTER SCALA, HUECHURABA - General Study

_Illustration 11: Terrain Huechuraba 2D Model_

The flow rate of Q100=9.0 l/s enters through each of the 3 sides (yellow arrows) and drains to a low point

indicated by the orange arrow.

When running the model, the software delivers the next flood area, where the maximum water height reached

on the ground is also indicated.

10

DATA CENTER SCALA, HUECHURABA - General Study

_Illustration 12: Flood area with water height_

0.03m

0.04m

4.0 CONCLUSION

0.01m

0.01m

0.01m

According to the study presented, considering rainfall with a return time of 100 years (9.00 l/s), the highest

water level reached on the ground would be 0.04m (image above). Taking into account the construction

standard of the site, in which the project's floor is 1.20m high in relation to the external floor, it is

guaranteed that there is no possibility of flooding occurring and reaching the internal areas of the site.

The only recommendation is that external equipment be at least 0.10m above the finished floor, such as

generators, pump rooms, and other equipment that is installed in the external area of the site.

11