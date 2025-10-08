---
title: Sin título
author: claudio cortes
date: D:20241108220414-03'00'
language: es
type: report
pages: 85
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Modelación de Dispersión e Impacto por Olores “Ampliación Planta de Tratamiento de Aguas Servidas Peralillo”
-->

# Modelación de Dispersión e Impacto por Olores “Ampliación Planta de Tratamiento de Aguas Servidas Peralillo”

## Peralillo, Chile Octubre 2024

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

## CONTENIDO

1. Introducción ............................................................................................................................................... 5

2. Clima y meteorología ................................................................................................................................. 7

2.1 Análisis de temperatura ......................................................................................................................... 11

2.2 Análisis de humedad .............................................................................................................................. 16

2.3 Análisis de viento .................................................................................................................................... 21

2.4 Análisis de radiación ............................................................................................................................... 35

2.5 Análisis de precipitación ........................................................................................................................ 40

3. Modelación meteorológica y dispersión .................................................................................................. 45

4. Análisis de incertidumbre......................................................................................................................... 53

4.1 Comparación cuantitativa de variables ................................................................................................. 60

5. Fuentes consideradas y receptores discretos definidos ........................................................................... 61

5.1 Fuentes consideradas ............................................................................................................................ 61

5.1 Cálculo de Tasa de Emisión de Olor ...................................................................................................... 66

5.2 Receptores discretos definidos ............................................................................................................. 70

6. Resultados de la modelación ................................................................................................................... 72

6.1 Isolíneas de concentraciones ................................................................................................................. 72

6.2 Aportes de Olor en los Receptores........................................................................................................ 77

6.1 Área de Influencia .................................................................................................................................. 78

7. Discusión .................................................................................................................................................. 79

8. Conclusión ................................................................................................................................................ 83

9. Bibliografía ............................................................................................................................................... 84

ÍNDICE DE TABLAS

Tabla 1-1. Coordenadas Punto Representativo del Proyecto (Datum WGS 84). ........................................................................ 6

Tabla 2-1. Estación considerada para el análisis meteorológico.................................................................................................. 9

Tabla 2-2. Porcentaje de disponibilidad de datos. ........................................................................................................................ 9

Tabla 3-1. Configuración física del modelo WRF 4.3, dominio más pequeño, de mayor resolución. ...................................... 46

Tabla 3-2. Configuración del modelo CALPUFF. .......................................................................................................................... 48

Página 2 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Tabla 3-3. Tipos de uso de suelos y parámetros considerados por CALPUFF, parámetros por defecto. ................................ 52

Tabla 4-1. Comparación cuantitativa de variables. ..................................................................................................................... 60

Tabla 5-1. Fuentes de olor del Proyecto. ..................................................................................................................................... 61

Tabla 5-2. Homologación de Fuentes. ......................................................................................................................................... 64

Tabla 5-3. Dimensiones, ubicación y tasas de emisión de fuentes. ........................................................................................... 65

Tabla 5-4. Escala de Intensidad de Olor. ..................................................................................................................................... 67

Tabla 5-5. Escala Tono Hedónico. ................................................................................................................................................ 67

Tabla 5-6. Descripción de emisiones odorantes. ........................................................................................................................ 68

Tabla 5-7. Tasas de emisión por unidad. ..................................................................................................................................... 68

Tabla 5-8. Coordenadas de receptores discretos definidos (UTM WGS-84 19S). ..................................................................... 70

Tabla 6-1. Aportes de Olor en los receptores. ............................................................................................................................ 77

Tabla 7-1. Concentración y percepción. ...................................................................................................................................... 80

Tabla 16. Límites Propuestos Normativa Holandesa. ................................................................................................................. 82

ÍNDICE DE FIGURAS

Figura 1-1. Ubicación de PTAS Peralillo. ........................................................................................................................................ 6

Figura 2-1. Estación considerada para el análisis de variables meteorológicas. ......................................................................... 8

Figura 2-2. Temperatura diaria 2020-2022 Nilahue-La Quebrada. ............................................................................................ 12

Figura 2-3. Ciclo diario de temperatura 2020-2022 Nilahue-La Quebrada. .............................................................................. 12

Figura 2-4.Ciclo anual de temperatura 2020-2022 Nilahue-La Quebrada. ............................................................................... 12

Figura 2-5. Datos de temperatura 2020-2022 Nilahue-La Quebrada. ....................................................................................... 13

Figura 2-6. Humedad relativa diaria 2020-2022 Nilahue-La Quebrada. .................................................................................... 17

Figura 2-7. Ciclo diario de humedad 2020-2022 Nilahue-La Quebrada. ................................................................................... 17

Figura 2-8. Ciclo anual de humedad 2020-2022 Nilahue-La Quebrada. .................................................................................... 17

Figura 2-9. Datos de humedad 2020-2022 Nilahue-La Quebrada. ............................................................................................ 18

Figura 2-10. Velocidad del viento diaria 2020-2022 Nilahue-La Quebrada. ............................................................................. 22

Figura 2-11. Ciclo diario de velocidad del viento 2020-2022 Nilahue-La Quebrada. ................................................................ 22

Figura 2-12. Ciclo anual de velocidad 2020-2022 Nilahue-La Quebrada................................................................................... 22

Figura 2-13. Datos de velocidad del viento 2020-2022 Nilahue-La Quebrada. ........................................................................ 23

Figura 2-14. Datos de porcentaje de calmas 2020-2022 Nilahue-La Quebrada. ...................................................................... 26

Figura 2-15. Datos de dirección de viento 2020-2022 Nilahue-La Quebrada. .......................................................................... 29

Figura 2-16. Rosa de frecuencias de velocidad y dirección de viento 2020-2022 Nilahue-La Quebrada. ............................... 32

Figura 2-17. Radiación solar diaria 2020-2022 Nilahue-La Quebrada. ...................................................................................... 36

Figura 2-18. Ciclo diario de radiación solar 2020-2022 Nilahue-La Quebrada.......................................................................... 36

Figura 2-19. Ciclo anual de radiación solar 2020-2022 Nilahue-La Quebrada. ......................................................................... 36

Figura 2-20. Datos de radiación solar 2020-2022 Nilahue-La Quebrada. ................................................................................. 37

Página 3 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-21. Precipitación diaria 2020-2022 Nilahue-La Quebrada. .......................................................................................... 41

Figura 2-22 Perfil diario de precipitación 2020-2022 Nilahue-La Quebrada. ............................................................................ 41

Figura 2-23. Perfil anual de precipitación 2020-2022 Nilahue-La Quebrada. ........................................................................... 41

Figura 2-24. Datos de precipitación 2020-2022 Nilahue-La Quebrada. .................................................................................... 42

Figura 3-1. Dominio y resolución para la modelación de dispersión. ........................................................................................ 49

Figura 3-2. Topografía utilizada (SRTM1 a 30 metros de resolución). ....................................................................................... 50

Figura 3-3. Dominio de modelación y los distintos usos de suelo considerados (GLCC a 1 Km de resolución). ..................... 51

Figura 4-1. Comparación de ciclo diario de velocidad observada y modelada. ........................................................................ 54

Figura 4-2. Comparación de ciclo anual de velocidad observada y modelada.......................................................................... 55

Figura 4-3. Comparación de dirección del viento observada y modelada. ............................................................................... 56

Figura 4-4. Comparación de velocidades de viento observada y modelada. ............................................................................ 56

Figura 4-5 Comparación de ciclo diario de temperatura observada y modelada. .................................................................... 58

Figura 4-6. Comparación de ciclo anual de temperatura observada y modelada. ................................................................... 59

Figura 5-1. Ubicación de fuentes consideradas. ......................................................................................................................... 62

Figura 5-2. Rueda de descriptores de olor relacionada con Aguas Servidas. ............................................................................ 67

Figura 5-3. Mapa de receptores discretos definidos. ................................................................................................................. 70

Figura 6-1. Isolínea de concentración de olor, percentil 99,5. ................................................................................................... 73

Figura 6-2. Isolínea de concentración de olor, percentil 98. ...................................................................................................... 74

Figura 6-3. Isolínea de concentración de olor, horas de excedencia de 3,5 UO. ...................................................................... 75

Figura 6-4. Isolínea de concentración de olor, horas de excedencia de 5 UO. ......................................................................... 76

Figura 6-5. Área de influencia. ..................................................................................................................................................... 78

Página 4 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

## 1. Introducción

El presente informe da cuenta de los resultados obtenidos de la modelación de dispersión

de olores y los impactos asociados al proyecto “Ampliación Planta de Tratamiento de Aguas

Servidas Peralillo.

Essbio es la empresa encargada de administrar las concesiones de servicios sanitarios en las

regiones del Libertador Bernardo O’Higgins, Ñuble y Biobío. Además, mantiene en la región

del Maule la administración de los servicios sanitarios de esa región a través de Nuevosur

S.A. Con 33 años prestando servicio, Essbio es unas de las empresas con más experiencia en

el rubro y la segunda mayor sanitaria del país. Para cumplir con este objetivo mantiene en

las regiones de concesión diversas plantas potabilizadoras y plantas de tratamiento de aguas

servidas (PTAS).

Dentro de su red de infraestructura, se encuentra la Panta de Tratamiento de Aguas Servidas

Peralillo (PTAS Peralillo) planta de tratamiento que trata las aguas residuales provenientes

de la localidad de Peralillo.

El Proyecto consiste en la incorporación de nuevas unidades de tratamiento y la

modificación, tanto en la línea de agua de la Planta, como en la línea de lodos. El objetivo

principal de la ampliación de la PTAS es soportar mayores caudales y cargas orgánicas en el

afluente del sistema, proyectando su operatividad al año 2034.

Dado todo esto, el proyecto debe ser evaluado ambientalmente para asegurar que no genere

impactos negativos hacia el medio ambiente y las personas que le rodean. El presente

estudio busca evaluar específicamente el proyecto en lo que corresponde a la posible

emisión de olores molestos provenientes de la ampliación de la Planta de Aguas Servidas.

Página 5 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

La PTAS Peralillo se encuentra emplazada a se encuentra emplazado a aproximadamente a

0,70 Kilómetros lineales al Noreste de la plaza de armas de la comuna de Peralillo,

específicamente en la Provincia de Colchagua, Sexta Región del Libertador General Bernardo

O’Higgins.

Figura 1-1. Ubicación de PTAS Peralillo.

(Fuente: Elaboración Propia).

Tabla 1-1. Coordenadas Punto Representativo del Proyecto (Datum WGS 84).

|Coordenadas Del Proyecto<br>(UTM 19H WGS 84)|Col2|
|---|---|
|Coordenada Este (m)|Coordenada Norte (m)|
|271.601|6.181.886|

Página 6 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

## 2. Clima y meteorología

El Proyecto se desarrollará en la Región del Libertador General Bernardo O’Higgins, las

principales características climáticas que presenta la región corresponden a un clima

predominante del tipo Templado Mediterráneo, el cual presenta variaciones por efecto de

la topografía local.

En la costa se presenta nuboso, mientras que hacia el interior debido a la sequedad

experimenta fuertes contrastes térmicos. Las precipitaciones son mayores en la costa y en la

Cordillera de los Andes, debido al relieve que no deja entrada a los vientos húmedos

oceánicos.

En el litoral, que recibe la influencia oceánica predomina el clima templado nuboso,

caracterizado por una mayor humedad y abundante nubosidad. En el sector de la depresión

intermedia predomina un clima templado de tipo mediterráneo cálido con una estación seca

de seis meses y un invierno lluvioso.

A medida que se asciende por la cordillera, las temperaturas descienden bajo los cero grados

en los meses de invierno. Sobre los 3.500 metros de altura se pasa al clima frío de altura con

predominio de nieves eternas. [1]

En cuanto a la meteorología, para el análisis de variables meteorológicas, se utilizó la estación

más próxima con información disponible, que es la estación Nilahue-La Quebrada ubicada

en Pumanque, propiedad de la Dirección Meteorológica de Chile (DMC), cuyos datos se

encuentran disponibles públicamente en su plataforma [http://agrometeorologia.cl. Su](http://agrometeorologia.cl/)

ubicación, se muestra en la Figura 2-1.

.

1 https://www.bcn.cl/siit/nuestropais/region6/clima.htm

Página 7 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-1. Estación considerada para el análisis de variables meteorológicas.

Mas detalles de la estación considerada se presentan en la Tabla 2-1. El análisis corresponde

a la información de los años 2020, 2021 y 2022.

Página 8 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Tabla 2-1. Estación considerada para el análisis meteorológico.

|Estación|UTME 19S<br>WGS-84 (m)|UTMN 19S<br>WGS-84 (m)|Altitud<br>(metros)|Variables monitoreadas|
|---|---|---|---|---|
|Nilahue-La Quebrada|249.823,23|6.161.269,49|81|• <br>Temperatura ambiente<br>(°C).<br>• <br>Humedad relativa (%).<br>• <br>Velocidad del viento<br>(m/s).<br>• <br>Dirección del viento (°).<br>• <br>Radiación global (W/m2).<br>• <br>Precipitación (mm).|

A continuación, se presenta un análisis de variables de interés para los fenómenos

atmosféricos que inciden en la dispersión y transporte de contaminantes. Se analizaron los

años 2020, 2021 y 2022, donde el porcentaje de disponibilidad de datos se presenta en la

Tabla 2-1, y se puede ver que en general no se cumple con la cantidad de información

necesaria del 75% para considerar el análisis como representativo, de manera que el análisis

se llevará a cabo considerando este factor y enfocado en 2022, año donde sí se supera el

porcentaje mínimo de datos requeridos.

Tabla 2-2. Porcentaje de disponibilidad de datos.

|Variable y año|Período inicio|Período fin|Disponibilidad de datos Nilahue-La Quebrada|
|---|---|---|---|
|Temperatura|Temperatura|Temperatura|Temperatura|
|Temperatura 2020|01/01/2020 00:00|31/12/2020 23:00|46,46%|
|Temperatura 2021|01/01/2021 00:00|31/12/2021 23:00|65,54%|
|Temperatura 2022|01/01/2022 00:00|31/12/2022 23:00|95,86%|
|Humedad Relativa|Humedad Relativa|Humedad Relativa|Humedad Relativa|
|Humedad relativa 2020|01/01/2020 00:00|31/12/2020 23:00|46,46%|
|Humedad relativa 2021|01/01/2021 00:00|31/12/2021 23:00|65,54%|
|Humedad relativa 2022|01/01/2022 00:00|31/12/2022 23:00|95,86%|
|Velocidad del viento|Velocidad del viento|Velocidad del viento|Velocidad del viento|
|Velocidad del viento<br>2020|01/01/2020 00:00|31/12/2020 23:00|50,33%|
|Velocidad del viento<br>2021|01/01/2021 00:00|31/12/2021 23:00|65,17%|
|Velocidad del viento<br>2022|01/01/2022 00:00|31/12/2022 23:00|95,09%|

Página 9 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Variable y año|Período inicio|Período fin|Disponibilidad de datos Nilahue-La Quebrada|
|---|---|---|---|
|Dirección del viento|Dirección del viento|Dirección del viento|Dirección del viento|
|Dirección del viento<br>2020|01/01/2020 00:00|31/12/2020 23:00|50,33%|
|Dirección del viento<br>2021|01/01/2021 00:00|31/12/2021 23:00|65,17%|
|Dirección del viento<br>2022|01/01/2022 00:00|31/12/2022 23:00|95,09%|
|Radiación Solar|Radiación Solar|Radiación Solar|Radiación Solar|
|Radiación Solar 2020|01/01/2020 00:00|31/12/2020 23:00|50,78%|
|Radiación Solar 2021|01/01/2021 00:00|31/12/2021 23:00|65,54%|
|Radiación Solar 2022|01/01/2022 00:00|31/12/2022 23:00|95,86%|
|Precipitación|Precipitación|Precipitación|Precipitación|
|Precipitación 2020|01/01/2020 00:00|31/12/2020 23:00|50,78%|
|Precipitación 2021|01/01/2021 00:00|31/12/2021 23:00|65,54%|
|Precipitación 2022|01/01/2022 00:00|31/12/2022 23:00|95,86%|

Página 10 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

### 2.1 Análisis de temperatura

A continuación, se presentan figuras que describen el comportamiento de esta variable. Se

puede ver, como es de esperar, que las mayores temperaturas se registran en el período

diurno, durante la tarde, alrededor de las 15 horas de los meses de enero y febrero,

disminuyendo hacia alcanzar las temperaturas más bajas hacia las primeras horas de la

mañana de los meses de junio y julio, siendo el año 2022 el año más frío de acuerdo con los

datos registrados por la estación.

Como es de esperar también para una estación ubicada en la depresión intermedia, la

amplitud térmica diaria es considerable, con valores promedio de aproximadamente 5 °C

durante el período nocturno a máximas promedio de 25°C durante el período diurno. Por

otro lado, la variación intra anual sigue el mismo patrón, con máximas promedio bordean los

30 °C en verano, descendiendo a temperaturas mínimas que bajan a valores en torno a los

5°C en invierno.

Página 11 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-2. Temperatura diaria 2020-2022 Nilahue-La Quebrada.

Figura 2-3. Ciclo diario de temperatura 2020-2022 Nilahue-La Quebrada.

Figura 2-4. Ciclo anual de temperatura 2020-2022 Nilahue-La Quebrada.

Página 12 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-5. Datos de temperatura 2020-2022 Nilahue-La Quebrada.

|Datos de temperatura (°C) 2020 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2020**|**2020**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2020**|**2020**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|14.2|13|12.3|10.1|9.2|6|||||||
|**Magrugada**|**1**|13.7|12.3|12.1|9.5|8.8|5.7|||||||
|**Magrugada**|**2**|13.3|11.8|11.6|9.3|8.5|5.4|||||||
|**Magrugada**|**3**|12.9|11.4|11.3|9.1|8.1|5.4|||||||
|**Magrugada**|**4**|12.5|11.1|11.2|8.7|7.9|5.4|||||||
|**Magrugada**|**5**|12.1|10.8|10.9|8.4|7.7|5.3|||||||
|**Mañana**|**6**|12.8|11|10.7|8.3|7.4|5.1|||||||
|**Mañana**|**7**|15.2|13.7|11.7|8.6|7.3|5|||||||
|**Mañana**|**8**|17.6|16.6|14.5|11.5|8.5|5.3|||||||
|**Mañana**|**9**|20.2|19.3|17.3|14.3|11.2|6.9|||||||
|**Mañana**|**10**|22.9|22|20.3|16.9|13.4|8.8|||||||
|**Mañana**|**11**|25.4|24.6|23|19.3|15.5|10.9|||||||
|**Tarde**|**12**|27.2|26.6|25.2|21.3|17.3|12.6|||||||
|**Tarde**|**13**|27.8|27.7|26.7|23|18.7|13.9|||||||
|**Tarde**|**14**|27.5|27.8|26.9|23.8|19.5|14.3|||||||
|**Tarde**|**15**|27|27.1|26|23.5|19.6|14.6|||||||
|**Tarde**|**16**|26.4|26.2|25|22.5|19|14.3|||||||
|**Tarde**|**17**|25.3|25|23.3|20.6|17.2|13.3|||||||
|**Noche**|**18**|23.5|22.8|21.1|18|15.1|11.2|||||||
|**Noche**|**19**|21|19.8|18.2|15.5|13.3|9.6|||||||
|**Noche**|**20**|18.4|17.4|16.3|13.7|11.9|8.8|||||||
|**Noche**|**21**|16.8|15.9|14.9|12.6|10.9|8.2|||||||
|**Noche**|**22**|15.8|14.7|13.8|11.7|10.2|7.3|||||||
|**Noche**|**23**|14.9|13.7|12.9|11|9.7|6.7|||||||
|**x mensual**|**x mensual**|**19.4**|**18.4**|**17.4**|**14.6**|**12.3**|**8.8**|||||||
|**x estacional**|**x estacional**|**18.4**|**18.4**|**18.4**|**11.9**|**11.9**|**11.9**|||||||
|**x anual**|**x anual**|**15.2**|**15.2**|**15.2**|**15.2**|**15.2**|**15.2**|**15.2**|**15.2**|**15.2**|**15.2**|**15.2**|**15.2**|

Página 13 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Datos de temperatura (°C) 2021 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2021**|**2021**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2021**|**2021**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|||||7.3|7.4|4|6.8|7.4|8.8|10.4|11.6|
|**Magrugada**|**1**|||||6.8|7.3|3.8|6.6|6.9|8.4|10|11.1|
|**Magrugada**|**2**|||||6.2|6.9|3.5|6.4|6.5|8.1|9.6|10.8|
|**Magrugada**|**3**|||||5.8|6.6|3.4|6.1|6.1|7.6|9.2|10.4|
|**Magrugada**|**4**|||||5.7|6.3|3.3|5.9|5.7|7.3|8.9|10.2|
|**Magrugada**|**5**|||||5.5|6.1|3|5.6|5.4|6.9|8.7|10.1|
|**Mañana**|**6**|||||5.5|6|2.7|5.4|5.2|7.4|10.3|11.5|
|**Mañana**|**7**|||||5.6|5.8|2.4|5.4|6.1|9.9|12.8|13.7|
|**Mañana**|**8**|||||6.4|6|2.6|6|8.5|12.6|15.1|16|
|**Mañana**|**9**|||||9|7.9|5.1|7.7|10.8|15.1|17.2|18.4|
|**Mañana**|**10**|||||11.6|10.1|7.5|9.4|13.3|17.2|19.5|20.9|
|**Mañana**|**11**|||||13.9|12|9.7|11.4|15.1|19|21.6|23.2|
|**Tarde**|**12**|||||15.9|13.5|11.4|13|16.6|20.5|23.2|24.6|
|**Tarde**|**13**|||||17.2|14.7|12.8|14.1|17.6|21.4|23.8|25|
|**Tarde**|**14**|||||18|15.5|13.7|14.7|18.2|21.6|23.7|24.8|
|**Tarde**|**15**|||||17.8|15.5|14.1|14.9|17.9|21.3|23.1|24.5|
|**Tarde**|**16**|||||17.1|15|13.6|14.5|17.2|20.6|22.3|23.7|
|**Tarde**|**17**|||||15.5|13.7|12.2|13.4|16|19.4|21|22.6|
|**Noche**|**18**|||||13.1|11.7|10|11.7|14|16.8|18.9|21.1|
|**Noche**|**19**|||||11.5|10.3|8.3|10.3|12.1|14.1|16|18.7|
|**Noche**|**20**|||||10.3|9.3|6.9|9|10.5|12.3|13.9|16|
|**Noche**|**21**|||||9.4|8.5|5.8|8.2|9.4|11|12.7|14.5|
|**Noche**|**22**|||||8.8|8.2|5.1|7.8|8.5|10.1|11.7|13.4|
|**Noche**|**23**|||||8.1|7.7|4.6|7.3|7.8|9.3|10.9|12.5|
|**x mensual**|**x mensual**|||||**10.5**|**9.7**|**7.1**|**9.2**|**11**|**13.6**|**15.6**|**17.1**|
|**x estacional**|**x estacional**||||**10.1**|**10.1**|**10.1**|**9.1**|**9.1**|**9.1**|**15.4**|**15.4**|**15.4**|
|**x anual**|**x anual**|**11.7**|**11.7**|**11.7**|**11.7**|**11.7**|**11.7**|**11.7**|**11.7**|**11.7**|**11.7**|**11.7**|**11.7**|

Página 14 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Datos de temperatura (°C) 2022 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2022**|**2022**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2022**|**2022**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|12.6|12.6|10.8|9.2|7.7|7.4|5.7|6.4|6.8|8.6|10.9|12.6|
|**Magrugada**|**1**|12|12.2|10.5|8.6|7.3|7.1|5.4|5.9|6.5|8.2|10.5|12.4|
|**Magrugada**|**2**|11.8|11.6|10.5|8.2|7|6.8|5.1|5.5|6.1|8.1|10.3|12|
|**Magrugada**|**3**|11.5|11.2|10.4|8.1|6.8|6.6|4.9|5.2|5.7|7.8|10.1|11.6|
|**Magrugada**|**4**|11.4|11|10.1|7.9|6.4|6.7|4.8|5.1|5.6|7.4|9.9|11.3|
|**Magrugada**|**5**|11.3|10.8|9.8|7.6|6|6.7|4.8|5|5.5|7.2|9.7|10.9|
|**Mañana**|**6**|12|10.7|9.7|7.4|5.8|6.7|4.7|4.9|5.3|7.5|10.3|13.1|
|**Mañana**|**7**|14.4|13|10.7|7.9|5.8|6.6|4.7|4.6|5.9|9.5|12.1|16.1|
|**Mañana**|**8**|16.4|15.7|13.7|10.2|6.9|6.7|4.8|5.9|7.9|11.8|13.9|18.7|
|**Mañana**|**9**|18.5|18.4|16.2|12.6|9|7.7|6|7.9|10|14.1|15.7|21.4|
|**Mañana**|**10**|20.5|21.2|18.6|14.8|10.8|9.2|7.7|9.7|12.1|16.2|17.5|23.7|
|**Mañana**|**11**|22.6|23.7|20.8|16.8|12.4|10.8|9.4|11.5|14|18.1|19.1|25.7|
|**Tarde**|**12**|24.3|25.5|22.9|18.7|13.8|12.3|11|13.1|15.4|19.6|20.5|26.9|
|**Tarde**|**13**|25.2|26.4|24.3|20|14.8|13.5|12.2|14.3|16.3|20.7|20.9|27.4|
|**Tarde**|**14**|25.4|26.3|25|20.4|15.6|14.1|12.9|15.1|16.8|20.8|20.7|27.3|
|**Tarde**|**15**|25.1|25.8|24.8|20.4|15.9|14.1|13.1|15.1|16.9|20.4|20|26.9|
|**Tarde**|**16**|24.3|25|24|19.7|15.2|13.7|12.7|14.7|16.4|19.4|19.4|26|
|**Tarde**|**17**|23.2|23.7|22.5|18|13.6|12.6|11.6|13.7|15.3|18.3|18.1|24.9|
|**Noche**|**18**|21.6|21.9|19.9|15.4|11.7|10.9|9.9|11.8|13.2|16.2|16.7|23.2|
|**Noche**|**19**|19.4|19.4|17|13.2|10.2|9.9|8.6|10.1|11|13.9|14.9|20.7|
|**Noche**|**20**|16.8|17.1|14.9|11.8|9.3|9.3|7.7|8.9|9.4|12.2|13.6|17.9|
|**Noche**|**21**|15.4|15.5|13.5|10.8|8.7|8.8|7|8.1|8.4|10.8|12.7|16|
|**Noche**|**22**|14.3|14.1|12.3|10.1|8.1|8.4|6.2|7.4|7.7|9.8|12|14.5|
|**Noche**|**23**|13.3|13.2|11.4|9.5|7.7|8.1|5.8|7.1|7.2|9.1|11.3|13.4|
|**x mensual**|**x mensual**|**17.6**|**17.8**|**16**|**12.8**|**9.9**|**9.4**|**7.8**|**9**|**10.2**|**13.2**|**14.6**|**18.9**|
|**x estacional**|**x estacional**|**17.1**|**17.1**|**17.1**|**10.7**|**10.7**|**10.7**|**9**|**9**|**9**|**15.6**|**15.6**|**15.6**|
|**x anual**|**x anual**|**13.1**|**13.1**|**13.1**|**13.1**|**13.1**|**13.1**|**13.1**|**13.1**|**13.1**|**13.1**|**13.1**|**13.1**|

Página 15 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

### 2.2 Análisis de humedad

Las siguientes figuras que describen el comportamiento de esta variable. Se puede ver que

la mayor humedad se registra en el período nocturno, durante las madrugadas de los meses

de junio y julio, disminuyendo hacia alcanzar los valores de humedad más baja durante las

tardes de los meses de enero y febrero, coincidente con las máximas temperaturas, entre las

15 y 16 horas.

Los años 2021 y 2022 se presenta ligeramente más húmedos que el año 2020, sin embargo,

es de considerar que dicho año carece de parte de la información para los meses más

húmedos. En general, la humedad se presenta alta para una estación ubicada en la depresión

intermedia, dando cuenta que aún se manifiesta una ligera influencia oceánica, los valores

de humedad promedio se encuentran ligeramente bajo el 70% con una amplia variabilidad

intra diaria, con valores promedio de 20% durante el período diurno a que llegan al 100%

durante el período nocturno.

Por otro lado, la variación intra anual también presenta variaciones, siendo las estaciones

cálidas las más secas con una humedad promedio del 60% y las estaciones frías con valores

de humedad promedio entre el 70% al 80%.

Estos altos valores de humedad durante el período nocturno de las estaciones frías producto

de las bajas temperaturas podrían dar cuenta de la presencia de neblinas bajo condiciones

de estabilidad atmosférica, fenómeno que daría cuenta de la proximidad de eventos de altas

concentraciones producto la falta de ventilación, pero aún falta un factor para el desarrollo

de este fenómeno que sería el viento, factor que será desarrollado más adelante,

complementando el análisis.

Página 16 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-6. Humedad relativa diaria 2020-2022 Nilahue-La Quebrada.

Figura 2-7. Ciclo diario de humedad 2020-2022 Nilahue-La Quebrada.

Figura 2-8. Ciclo anual de humedad 2020-2022 Nilahue-La Quebrada.

Página 17 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-9. Datos de humedad 2020-2022 Nilahue-La Quebrada.

|Datos de humedad (%) 2020 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2020**|**2020**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2020**|**2020**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|75.3|74.1|78.9|77|86.8|94|||||||
|**Magrugada**|**1**|76.2|75.9|79.9|78.8|88.5|94.7|||||||
|**Magrugada**|**2**|77.3|77.6|81|79.8|90|94.9|||||||
|**Magrugada**|**3**|78.4|78.9|82.1|80.9|91.6|94.6|||||||
|**Magrugada**|**4**|79.9|79.8|83.3|82.7|92.8|94.2|||||||
|**Magrugada**|**5**|80.9|80.7|84|84.4|93.2|94.4|||||||
|**Mañana**|**6**|79.3|80.1|85.1|85.3|93.9|94.3|||||||
|**Mañana**|**7**|73|73|82.9|84.7|94.3|94.1|||||||
|**Mañana**|**8**|65|65.4|76.1|77.5|92.3|93.7|||||||
|**Mañana**|**9**|55.8|56.9|66.8|69|83.1|91.5|||||||
|**Mañana**|**10**|47.7|47.9|56.5|60.9|74.7|86.8|||||||
|**Mañana**|**11**|41|40.5|47.4|53.1|66|79.6|||||||
|**Tarde**|**12**|37.1|35.6|41.3|46.7|58.4|73.6|||||||
|**Tarde**|**13**|35.9|33.4|37.5|42.2|52.9|68.4|||||||
|**Tarde**|**14**|36.2|34.1|37.7|40.7|49.3|67.6|||||||
|**Tarde**|**15**|36.8|35.2|40.2|41.8|48.7|65.5|||||||
|**Tarde**|**16**|37.7|36.6|43|44.3|50.1|67.1|||||||
|**Tarde**|**17**|40.1|38.9|47.3|48.8|56.6|71.7|||||||
|**Noche**|**18**|44.9|44.2|53.7|56.1|64.1|79.9|||||||
|**Noche**|**19**|52.6|54|62.5|64.1|70.9|85.8|||||||
|**Noche**|**20**|62.5|62.6|69.2|68.7|76.9|88.8|||||||
|**Noche**|**21**|68.9|68|73.2|71.2|79.8|90.6|||||||
|**Noche**|**22**|72.6|71.3|75|73.2|82.2|91|||||||
|**Noche**|**23**|74.5|72.7|76.2|75.3|84.5|92.7|||||||
|**x mensual**|**x mensual**|**59.6**|**59.1**|**65**|**66.1**|**75.9**|**85.4**|||||||
|**x estacional**|**x estacional**|**61.2**|**61.2**|**61.2**|**75.8**|**75.8**|**75.8**|||||||
|**x anual**|**x anual**|**68.5**|**68.5**|**68.5**|**68.5**|**68.5**|**68.5**|**68.5**|**68.5**|**68.5**|**68.5**|**68.5**|**68.5**|

Página 18 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Datos de humedad (%) 2021 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2021**|**2021**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2021**|**2021**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|||||94|94.5|93.4|92.4|91.1|84.4|82.6|83.3|
|**Magrugada**|**1**|||||94.7|94.9|94|92.9|92.2|85.2|83.9|84.5|
|**Magrugada**|**2**|||||95.6|95.5|94.5|93.5|92.9|85.5|85.2|85.7|
|**Magrugada**|**3**|||||96.1|96|94.6|93.8|93.7|86.9|86.4|86.9|
|**Magrugada**|**4**|||||96.4|96.4|94.5|94|94.3|87.4|87.7|87.7|
|**Magrugada**|**5**|||||97.1|96|94.9|94.3|94.9|88.1|88.5|88.4|
|**Mañana**|**6**|||||97.6|95.7|95|94.7|95.5|87.2|83.7|85.4|
|**Mañana**|**7**|||||97.3|96.1|95.9|94.8|93.2|79.2|75.3|78.6|
|**Mañana**|**8**|||||96.8|96.2|96.2|94|86.9|68.8|67|69.5|
|**Mañana**|**9**|||||92|92.4|91.3|90.4|78.6|59.4|59.1|60.8|
|**Mañana**|**10**|||||83.8|85.2|83.4|85.6|68.2|51.8|51.4|52.7|
|**Mañana**|**11**|||||73.9|77.9|76.5|78|60.9|45.8|45.3|46.5|
|**Tarde**|**12**|||||64.8|72.8|70.7|70.1|54.8|42|41.6|43|
|**Tarde**|**13**|||||58.1|67.9|65.4|65.3|51.3|40.1|40.8|42.3|
|**Tarde**|**14**|||||54.8|64.8|61.3|62.5|50.4|40.2|41.5|42.2|
|**Tarde**|**15**|||||55.5|64.7|60.4|62.6|52|42.6|42.8|42.5|
|**Tarde**|**16**|||||57.3|66.8|62.7|64.1|53.6|45|44.3|44.2|
|**Tarde**|**17**|||||64.5|72.6|68.4|69.1|58.8|47.8|47.3|46.8|
|**Noche**|**18**|||||74.6|81.8|76.6|76.7|66.4|55.6|53.2|50.9|
|**Noche**|**19**|||||81.9|86.9|82.6|81.9|74.7|65.1|63.2|58.6|
|**Noche**|**20**|||||85.5|89.4|86.4|86|81.2|72.4|71.4|67.9|
|**Noche**|**21**|||||88.2|91.5|89.1|88.3|85.3|77.2|76|74.3|
|**Noche**|**22**|||||90.3|92.3|91.2|90|87.9|80|78.8|79.1|
|**Noche**|**23**|||||91.7|93.6|92.4|91.3|89.6|82.5|80.7|81.3|
|**x mensual**|**x mensual**|||||**82.6**|**85.9**|**83.8**|**83.6**|**77**|**66.7**|**65.7**|**66**|
|**x estacional**|**x estacional**||||**84.3**|**84.3**|**84.3**|**81.5**|**81.5**|**81.5**|**66.1**|**66.1**|**66.1**|
|**x anual**|**x anual**|**76.4**|**76.4**|**76.4**|**76.4**|**76.4**|**76.4**|**76.4**|**76.4**|**76.4**|**76.4**|**76.4**|**76.4**|

Página 19 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Datos de humedad (%) 2022 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2022**|**2022**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2022**|**2022**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|83.1|83.4|76.9|82.4|92.1|93.4|94.3|93.1|93.5|86.1|85.8|81.5|
|**Magrugada**|**1**|84.2|84|77.9|84.2|92.8|94.1|94.6|93.6|94.2|87.2|87.2|81.6|
|**Magrugada**|**2**|85.3|85.5|79.2|85.1|93.3|95|95.3|94.2|94.3|87.2|87.3|83.1|
|**Magrugada**|**3**|86.3|86.9|80.5|86|93.6|95.3|96|94.9|94.5|87.2|88|84.2|
|**Magrugada**|**4**|86.8|88|81.7|87.5|94|95.5|96.1|95.1|94.8|87.4|88.7|84.8|
|**Magrugada**|**5**|87.2|88.8|83|88.9|94.8|95.3|96.4|95.4|95.2|87.5|89.7|85.9|
|**Mañana**|**6**|85.2|88.8|84.1|89.6|95.3|94.9|96.6|95.1|95.5|86.9|88.7|79.2|
|**Mañana**|**7**|78|82.3|81.5|88.1|95.4|94.9|96.3|95.3|94.9|81.9|83.3|69.3|
|**Mañana**|**8**|71|74|73.6|82.1|94|95|96.1|93.5|90.3|73.3|76.4|60.1|
|**Mañana**|**9**|63.2|63.8|65.6|74.9|88.7|93.3|95|87.5|82.5|65.5|69.1|51.3|
|**Mañana**|**10**|56.1|53.6|57|67.2|81.5|88.9|90.6|81.8|73.3|57.9|62.1|44.4|
|**Mañana**|**11**|49.6|46|49.7|59.9|75.2|83.3|85.9|74.9|65.4|51.8|57.9|39.6|
|**Tarde**|**12**|44.8|41.8|43.4|53.7|69.6|78|80.8|68.1|60.2|47.5|53.5|37.6|
|**Tarde**|**13**|42.8|39.8|39.7|49.4|64.9|72.8|74.2|64.2|57.5|44.7|52.4|36.7|
|**Tarde**|**14**|41.9|39.8|37.9|48.3|62|69.6|70.2|61.2|57|45.3|53.3|37.1|
|**Tarde**|**15**|41.5|40.7|37.8|48.6|61.4|70.5|69.3|61.6|56.9|47|55.9|37.8|
|**Tarde**|**16**|42.9|42.4|39.5|50.9|64.1|72.1|71.5|63.5|59.1|49.4|56.5|39.9|
|**Tarde**|**17**|45.3|45|43|56.5|70.3|77.3|76.9|67.7|63|52|59.4|41.8|
|**Noche**|**18**|49.8|50.6|49.8|66.1|78.5|85.7|84.5|76|70.7|59.6|65|45.1|
|**Noche**|**19**|57.5|59.7|59.9|73.9|85|88.9|88.9|83.7|80.1|68.5|72.1|52.8|
|**Noche**|**20**|68|69.2|67.6|77|88|90.5|91|88.3|86.5|75.4|77.9|63.1|
|**Noche**|**21**|74.4|75.8|71.6|79.7|89.8|91.5|92.9|90.2|89.9|80.2|82.4|71.7|
|**Noche**|**22**|79.4|80|74.2|80.9|91|92.4|93.9|92.2|91.6|82.4|85|76.9|
|**Noche**|**23**|81.8|82.3|75.2|82.3|91.7|92.6|94.7|92.3|92.8|83.9|87|80|
|**x mensual**|**x mensual**|**66.1**|**66.3**|**63.8**|**72.6**|**83.6**|**87.5**|**88.4**|**83.5**|**80.6**|**69.8**|**73.5**|**61.1**|
|**x estacional**|**x estacional**|**65.4**|**65.4**|**65.4**|**81.2**|**81.2**|**81.2**|**84.2**|**84.2**|**84.2**|**68.1**|**68.1**|**68.1**|
|**x anual**|**x anual**|**74.7**|**74.7**|**74.7**|**74.7**|**74.7**|**74.7**|**74.7**|**74.7**|**74.7**|**74.7**|**74.7**|**74.7**|

Página 20 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

### 2.3 Análisis de viento

En las figuras siguientes se presenta el comportamiento del viento. A nivel de ciclo diario se

puede ver que las velocidades de viento más bajas se presentan durante todo el período

nocturno, ascendiendo en magnitud hasta lograr las velocidades más altas durante el

período diurno, más específicamente, durante la tarde.

A nivel intra anual, las mayores velocidades de viento se presentan durante las estaciones

cálidas del año, específicamente durante las tardes del mes de enero alrededor de las 14

horas, consistente con las horas de mayor temperatura y menor humedad, y las velocidades

mínimas se presentan durante las madrugadas de las estaciones cálidas del año. En cuanto

a las calmas, éstas se presentan abundantes desarrollándose con mayor frecuencia durante

las madrugadas de las estaciones cálidas del año.

Con relación a la dirección del viento, los años 2020 y 2021 no brindan mayor claridad del

patrón de comportamiento de esta variable, sin embargo, para 2022 se pueden observar tres

componentes predominantes, una desde el nornoreste, una desde el sur y otra desde el

oeste. Respecto de las componentes del nornoreste y sur, ella se manifiesta durante las

estaciones frías del año con vientos débiles durante el otoño a moderados hacia el invierno.

Ya para el período primavera-verano, se manifiesta la componente del oeste con vientos

débiles a moderados.

Página 21 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-10. Velocidad del viento diaria 2020-2022 Nilahue-La Quebrada.

Figura 2-11. Ciclo diario de velocidad del viento 2020-2022 Nilahue-La Quebrada.

Figura 2-12. Ciclo anual de velocidad 2020-2022 Nilahue-La Quebrada.

Página 22 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-13. Datos de velocidad del viento 2020-2022 Nilahue-La Quebrada.

|Datos de velocidad (m/s) 2020 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2020**|**2020**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2020**|**2020**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|0.5|0.5|0.3|0.4|0.6|0.5|0.7||||||
|**Magrugada**|**1**|0.5|0.4|0.4|0.4|0.6|0.4|0.6||||||
|**Magrugada**|**2**|0.5|0.5|0.4|0.5|0.6|0.4|0.8||||||
|**Magrugada**|**3**|0.5|0.4|0.4|0.5|0.4|0.5|0.9||||||
|**Magrugada**|**4**|0.5|0.4|0.4|0.4|0.6|0.5|0.8||||||
|**Magrugada**|**5**|0.5|0.3|0.4|0.5|0.5|0.6|0.8||||||
|**Mañana**|**6**|0.6|0.4|0.4|0.5|0.5|0.6|1.1||||||
|**Mañana**|**7**|0.7|0.5|0.4|0.6|0.6|0.6|0.8||||||
|**Mañana**|**8**|1.1|1.2|0.8|0.7|0.6|0.7|1.7||||||
|**Mañana**|**9**|1.5|1.7|1.2|1.3|1.1|0.7|0.8||||||
|**Mañana**|**10**|1.7|1.9|1.5|1.8|1.6|0.9|1.1||||||
|**Mañana**|**11**|2|2|1.8|2.1|1.9|0.9|1.5||||||
|**Tarde**|**12**|2.6|2.5|2.2|2.2|2.3|1.2|1.5||||||
|**Tarde**|**13**|3.5|3.2|2.7|2.3|2.6|1.5|1.5||||||
|**Tarde**|**14**|3.9|3.6|3.4|2.8|2.8|1.4|1.5||||||
|**Tarde**|**15**|3.6|3.6|3.5|3.1|2.8|1.4|1.6||||||
|**Tarde**|**16**|3.2|3.2|3|2.9|2.7|1.4|1.7||||||
|**Tarde**|**17**|2.9|2.8|2.3|2.1|2.1|1.4|1.5||||||
|**Noche**|**18**|2.4|2.1|1.6|1.2|1.1|1|0.8||||||
|**Noche**|**19**|1.6|1.4|0.8|0.6|0.8|0.9|0.7||||||
|**Noche**|**20**|1|0.9|0.6|0.6|0.7|0.9|0.9||||||
|**Noche**|**21**|0.6|0.7|0.4|0.5|0.7|0.8|0.7||||||
|**Noche**|**22**|0.4|0.5|0.3|0.5|0.7|0.7|0.6||||||
|**Noche**|**23**|0.5|0.4|0.3|0.5|0.8|0.6|0.7||||||
|**x mensual**|**x mensual**|**1.5**|**1.5**|**1.2**|**1.2**|**1.2**|**0.9**|**1.1**||||||
|**x estacional**|**x estacional**|**1.4**|**1.4**|**1.4**|**1.1**|**1.1**|**1.1**|**1.1**|**1.1**|**1.1**||||
|**x anual**|**x anual**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|

Página 23 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Datos de velocidad (m/s) 2021 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2021**|**2021**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2021**|**2021**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|||||0.4|0.5|0.6|0.6|0.4|0.6|0.7|0.3|
|**Magrugada**|**1**|||||0.4|0.6|0.6|0.6|0.4|0.7|0.7|0.3|
|**Magrugada**|**2**|||||0.4|0.6|0.6|0.6|0.4|0.7|0.6|0.4|
|**Magrugada**|**3**|||||0.3|0.7|0.5|0.7|0.4|0.6|0.6|0.3|
|**Magrugada**|**4**|||||0.4|0.6|0.7|0.6|0.5|0.8|0.6|0.3|
|**Magrugada**|**5**|||||0.4|0.6|0.6|0.7|0.4|0.7|0.6|0.3|
|**Mañana**|**6**|||||0.4|0.7|0.6|0.7|0.4|0.9|0.7|0.4|
|**Mañana**|**7**<br>**8**<br>**9**|||||0.4<br>0.5<br>0.6|0.5<br>0.5<br>0.7|0.6<br>0.5<br>0.8|0.7<br>0.6<br>0.7|0.4<br>0.8<br>1.3|1.4<br>2.3<br>2.6|1.3<br>2<br>2.1|0.7<br>0.9<br>1.2|
|**Mañana**|**10**|||||1.1|0.8|1.2|1.1|2|2.9|2.3|1.5|
|**Mañana**|**11**|||||1.7|1.4|1.6|1.5|2.3|2.9|2.5|1.8|
|**Tarde**|**12**|||||1.9|1.6|2|1.7|2.5|3|2.8|2.4|
|**Tarde**|**13**|||||2.3|1.9|2.3|1.8|2.6|3.2|3.4|3.1|
|**Tarde**|**14**|||||2.4|2.1|2.4|2|2.9|3.6|3.7|3.3|
|**Tarde**|**15**|||||2.6|2.1|2.5|2.1|3.2|3.5|3.5|3.3|
|**Tarde**|**16**|||||2.3|1.9|2.3|2|3.1|3.1|3|3|
|**Tarde**|**17**|||||1.6|1.5|1.7|1.7|2.4|2.8|2.7|2.7|
|**Noche**|**18**|||||1|1|1.2|1.1|1.6|1.9|2.2|2.2|
|**Noche**|**19**|||||0.8|0.8|1|0.8|0.8|0.9|1.5|1.4|
|**Noche**|**20**|||||0.7|0.6|0.8|0.7|0.5|0.5|0.9|0.9|
|**Noche**|**21**|||||0.7|0.6|0.8|0.6|0.5|0.5|0.8|0.7|
|**Noche**|**22**|||||0.6|0.6|0.6|0.5|0.5|0.5|0.7|0.5|
|**Noche**|**23**|||||0.5|0.6|0.6|0.5|0.5|0.5|0.7|0.4|
|**x mensual**|**x mensual**|||||**1**|**1**|**1.1**|**1**|**1.3**|**1.7**|**1.7**|**1.3**|
|**x estacional**|**x estacional**||||**1**|**1**|**1**|**1.1**|**1.1**|**1.1**|**1.6**|**1.6**|**1.6**|
|**x anual**|**x anual**|**1.3**|**1.3**|**1.3**|**1.3**|**1.3**|**1.3**|**1.3**|**1.3**|**1.3**|**1.3**|**1.3**|**1.3**|

Página 24 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Datos de velocidad (m/s) 2022 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2022**|**2022**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2022**|**2022**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|0.4|0.3|0.6|0.6|0.7|0.6|0.6|0.7|0.3|0.6|0.6|0.4|
|**Magrugada**|**1**|0.4|0.5|0.6|0.5|0.7|0.6|0.7|0.6|0.2|0.8|0.5|0.7|
|**Magrugada**|**2**|0.4|0.4|0.7|0.6|0.7|0.6|0.6|0.5|0.3|0.8|0.5|0.6|
|**Magrugada**|**3**|0.4|0.3|0.9|0.5|0.7|0.6|0.6|0.4|0.2|0.8|0.4|0.6|
|**Magrugada**|**4**|0.5|0.4|0.8|0.5|0.6|0.6|0.7|0.5|0.3|0.9|0.4|0.6|
|**Magrugada**|**5**|0.5|0.4|0.8|0.6|0.5|0.6|0.6|0.5|0.3|0.9|0.4|0.6|
|**Mañana**|**6**|0.5|0.5|0.8|0.6|0.5|0.6|0.6|0.5|0.3|0.9|0.4|0.7|
|**Mañana**|**7**<br>**8**<br>**9**|0.7<br>1.2<br>1.5|0.4<br>0.9<br>1.2|0.7<br>1.2<br>2|0.6<br>0.8<br>1.3|0.5<br>0.6<br>1|0.6<br>0.6<br>0.7|0.6<br>0.7<br>0.7|0.5<br>0.5<br>1.1|0.4<br>0.6<br>1.2|1<br>1.8<br>2.2|0.5<br>0.6<br>0.9|1.2<br>1.6<br>1.9|
|**Mañana**|**10**|1.7|1.6|2.2|1.7|1.3|0.9|0.8|1.6|1.6|2.4|1.1|2.1|
|**Mañana**|**11**|1.9|1.8|2.3|2|1.5|1.1|1|2|1.9|2.5|1.3|2.3|
|**Tarde**|**12**|2.2|2.2|2.4|2.1|1.5|1.2|1.2|2.3|2|2.8|1.9|2.7|
|**Tarde**|**13**|2.9|2.9|2.8|2.3|1.8|1.4|1.6|2.4|2.4|3.1|2.5|3.3|
|**Tarde**|**14**|3.4|3.4|3.1|2.8|1.8|1.4|1.7|2.5|2.6|3.7|2.6|3.5|
|**Tarde**|**15**|3.5|3.6|3.1|2.8|2.1|1.4|1.7|2.5|2.5|3.5|2.8|3.4|
|**Tarde**|**16**|3.3|3.1|3|2.6|2.2|1.5|1.9|2.5|2.5|3.4|2.7|2.9|
|**Tarde**|**17**|2.9|2.7|2.4|2|1.5|1.2|1.4|1.9|2|2.7|2.4|2.6|
|**Noche**|**18**|2.3|2.2|1.7|1.1|0.9|0.9|0.9|1|1.1|1.9|1.8|2|
|**Noche**|**19**|1.5|1.3|1.2|0.7|0.8|0.9|0.8|0.7|0.5|1|1.1|1.4|
|**Noche**|**20**|0.9|0.8|0.9|0.5|0.7|0.6|0.8|0.5|0.5|0.7|0.9|0.8|
|**Noche**|**21**|0.6|0.5|0.8|0.5|0.6|0.7|0.7|0.5|0.4|0.6|0.7|0.3|
|**Noche**|**22**|0.5|0.3|0.6|0.6|0.6|0.7|0.6|0.5|0.4|0.6|0.6|0.2|
|**Noche**|**23**|0.4|0.3|0.5|0.6|0.7|0.6|0.5|0.7|0.3|0.6|0.6|0.3|
|**x mensual**|**x mensual**|**1.4**|**1.3**|**1.5**|**1.2**|**1**|**0.9**|**0.9**|**1.1**|**1**|**1.7**|**1.2**|**1.5**|
|**x estacional**|**x estacional**|**1.4**|**1.4**|**1.4**|**1**|**1**|**1**|**1**|**1**|**1**|**1.5**|**1.5**|**1.5**|
|**x anual**|**x anual**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|**1.2**|

Página 25 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-14. Datos de porcentaje de calmas 2020-2022 Nilahue-La Quebrada.

|Porcentaje de calmas, velocidad inferior a 0.5 (m/s) 2020 Nilahue-La Quebrada<br>Verano Otoño Invierno Primavera<br>2020 ene feb mar abr may jun jul ago sept oct nov dic<br>0 3.3% 3.1% 3.9% 3.2% 1.9% 1.8% 0.8%<br>1 3.2% 3.2% 3.5% 3.3% 2.2% 1.9% 0.8% Magrugada<br>2 3.2% 2.6% 3.1% 3.1% 2.4% 1.7% 0.3%<br>3 3.3% 2.6% 3.3% 3.2% 2.8% 1.7% 0.3%<br>4 3.2% 2.8% 3.1% 3.2% 2.8% 1.8% 0.4%<br>5 3.1% 2.8% 3.5% 2.8% 2.6% 1.4% 0.4%<br>6 3.1% 2.9% 2.8% 3.1% 2.6% 1.5% 0.3%<br>7 2.6% 2.4% 2.9% 2.4% 2.1% 1.4% 0.6%<br>Mañana<br>8 0.7% 0.7% 2.1% 2.5% 2.4% 1.3% 0.1%<br>9 0.1% 0.0% 0.3% 1.0% 1.8% 1.5% 1.0%<br>10 0.0% 0.0% 0.1% 0.3% 1.1% 1.1% 0.8%<br>11 0.0% 0.0% 0.0% 0.1% 0.3% 1.3% 0.0%<br>12 0.0% 0.0% 0.0% 0.0% 0.1% 0.4% 0.6%<br>13 0.0% 0.0% 0.0% 0.0% 0.0% 0.6% 0.3%<br>14 0.0% 0.0% 0.0% 0.0% 0.0% 0.4% 0.3% Tarde<br>15 0.0% 0.0% 0.0% 0.0% 0.0% 0.7% 0.3%<br>16 0.0% 0.0% 0.0% 0.0% 0.1% 0.4% 0.1%<br>17 0.0% 0.0% 0.0% 0.1% 0.0% 0.4% 0.1%<br>18 0.0% 0.0% 0.1% 0.4% 0.8% 1.3% 1.5%<br>19 0.0% 0.3% 1.1% 2.2% 1.8% 1.7% 1.5%<br>20 0.8% 0.8% 2.4% 2.6% 1.8% 1.5% 1.0% Noche<br>21 2.2% 1.7% 3.6% 2.8% 1.9% 1.7% 1.3%<br>22 3.2% 2.5% 4.0% 3.1% 2.1% 1.7% 1.5%<br>23 2.9% 3.1% 3.6% 3.3% 1.8% 1.5% 1.3%|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2020**<br>**ene**<br>**feb**<br>**mar**<br>**abr**<br>**may**<br>**jun**<br>**jul**<br>**ago**<br>**sept**<br>**oct**<br>**nov**<br>**dic**<br>**0**<br>3.3%<br>3.1%<br>3.9%<br>3.2%<br>1.9%<br>1.8%<br>0.8%<br>**1**<br>3.2%<br>3.2%<br>3.5%<br>3.3%<br>2.2%<br>1.9%<br>0.8%<br>**2**<br>3.2%<br>2.6%<br>3.1%<br>3.1%<br>2.4%<br>1.7%<br>0.3%<br>**3**<br>3.3%<br>2.6%<br>3.3%<br>3.2%<br>2.8%<br>1.7%<br>0.3%<br>**4**<br>3.2%<br>2.8%<br>3.1%<br>3.2%<br>2.8%<br>1.8%<br>0.4%<br>**5**<br>3.1%<br>2.8%<br>3.5%<br>2.8%<br>2.6%<br>1.4%<br>0.4%<br>**6**<br>3.1%<br>2.9%<br>2.8%<br>3.1%<br>2.6%<br>1.5%<br>0.3%<br>**7**<br>2.6%<br>2.4%<br>2.9%<br>2.4%<br>2.1%<br>1.4%<br>0.6%<br>**8**<br>0.7%<br>0.7%<br>2.1%<br>2.5%<br>2.4%<br>1.3%<br>0.1%<br>**9**<br>0.1%<br>0.0%<br>0.3%<br>1.0%<br>1.8%<br>1.5%<br>1.0%<br>**10**<br>0.0%<br>0.0%<br>0.1%<br>0.3%<br>1.1%<br>1.1%<br>0.8%<br>**11**<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.3%<br>1.3%<br>0.0%<br>**12**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.6%<br>**13**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.6%<br>0.3%<br>**14**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.4%<br>0.3%<br>**15**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.7%<br>0.3%<br>**16**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.1%<br>**17**<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.0%<br>0.4%<br>0.1%<br>**18**<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.8%<br>1.3%<br>1.5%<br>**19**<br>0.0%<br>0.3%<br>1.1%<br>2.2%<br>1.8%<br>1.7%<br>1.5%<br>**20**<br>0.8%<br>0.8%<br>2.4%<br>2.6%<br>1.8%<br>1.5%<br>1.0%<br>**21**<br>2.2%<br>1.7%<br>3.6%<br>2.8%<br>1.9%<br>1.7%<br>1.3%<br>**22**<br>3.2%<br>2.5%<br>4.0%<br>3.1%<br>2.1%<br>1.7%<br>1.5%<br>**23**<br>2.9%<br>3.1%<br>3.6%<br>3.3%<br>1.8%<br>1.5%<br>1.3%<br>**Primavera**<br>Porcentaje de calmas, velocidad inferior a 0.5 (m/s) 2020 Nilahue-La Quebrada<br>**Magrugada**<br>**Mañana**<br>**Verano**<br>**Otoño**<br>**Invierno**<br>**Tarde**<br>**Noche**|**8**|0.7%|0.7%|2.1%|2.5%|2.4%|1.3%|0.1%||||||
|**2020**<br>**ene**<br>**feb**<br>**mar**<br>**abr**<br>**may**<br>**jun**<br>**jul**<br>**ago**<br>**sept**<br>**oct**<br>**nov**<br>**dic**<br>**0**<br>3.3%<br>3.1%<br>3.9%<br>3.2%<br>1.9%<br>1.8%<br>0.8%<br>**1**<br>3.2%<br>3.2%<br>3.5%<br>3.3%<br>2.2%<br>1.9%<br>0.8%<br>**2**<br>3.2%<br>2.6%<br>3.1%<br>3.1%<br>2.4%<br>1.7%<br>0.3%<br>**3**<br>3.3%<br>2.6%<br>3.3%<br>3.2%<br>2.8%<br>1.7%<br>0.3%<br>**4**<br>3.2%<br>2.8%<br>3.1%<br>3.2%<br>2.8%<br>1.8%<br>0.4%<br>**5**<br>3.1%<br>2.8%<br>3.5%<br>2.8%<br>2.6%<br>1.4%<br>0.4%<br>**6**<br>3.1%<br>2.9%<br>2.8%<br>3.1%<br>2.6%<br>1.5%<br>0.3%<br>**7**<br>2.6%<br>2.4%<br>2.9%<br>2.4%<br>2.1%<br>1.4%<br>0.6%<br>**8**<br>0.7%<br>0.7%<br>2.1%<br>2.5%<br>2.4%<br>1.3%<br>0.1%<br>**9**<br>0.1%<br>0.0%<br>0.3%<br>1.0%<br>1.8%<br>1.5%<br>1.0%<br>**10**<br>0.0%<br>0.0%<br>0.1%<br>0.3%<br>1.1%<br>1.1%<br>0.8%<br>**11**<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.3%<br>1.3%<br>0.0%<br>**12**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.6%<br>**13**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.6%<br>0.3%<br>**14**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.4%<br>0.3%<br>**15**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.7%<br>0.3%<br>**16**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.1%<br>**17**<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.0%<br>0.4%<br>0.1%<br>**18**<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.8%<br>1.3%<br>1.5%<br>**19**<br>0.0%<br>0.3%<br>1.1%<br>2.2%<br>1.8%<br>1.7%<br>1.5%<br>**20**<br>0.8%<br>0.8%<br>2.4%<br>2.6%<br>1.8%<br>1.5%<br>1.0%<br>**21**<br>2.2%<br>1.7%<br>3.6%<br>2.8%<br>1.9%<br>1.7%<br>1.3%<br>**22**<br>3.2%<br>2.5%<br>4.0%<br>3.1%<br>2.1%<br>1.7%<br>1.5%<br>**23**<br>2.9%<br>3.1%<br>3.6%<br>3.3%<br>1.8%<br>1.5%<br>1.3%<br>**Primavera**<br>Porcentaje de calmas, velocidad inferior a 0.5 (m/s) 2020 Nilahue-La Quebrada<br>**Magrugada**<br>**Mañana**<br>**Verano**<br>**Otoño**<br>**Invierno**<br>**Tarde**<br>**Noche**|**9**<br>**10**<br>**11**<br>**12**|0.1%<br>0.0%<br>0.0%<br>0.0%|0.0%<br>0.0%<br>0.0%<br>0.0%|0.3%<br>0.1%<br>0.0%<br>0.0%|1.0%<br>0.3%<br>0.1%<br>0.0%|1.8%<br>1.1%<br>0.3%<br>0.1%|1.5%<br>1.1%<br>1.3%<br>0.4%|1.0%<br>0.8%<br>0.0%<br>0.6%||||||
|**2020**<br>**ene**<br>**feb**<br>**mar**<br>**abr**<br>**may**<br>**jun**<br>**jul**<br>**ago**<br>**sept**<br>**oct**<br>**nov**<br>**dic**<br>**0**<br>3.3%<br>3.1%<br>3.9%<br>3.2%<br>1.9%<br>1.8%<br>0.8%<br>**1**<br>3.2%<br>3.2%<br>3.5%<br>3.3%<br>2.2%<br>1.9%<br>0.8%<br>**2**<br>3.2%<br>2.6%<br>3.1%<br>3.1%<br>2.4%<br>1.7%<br>0.3%<br>**3**<br>3.3%<br>2.6%<br>3.3%<br>3.2%<br>2.8%<br>1.7%<br>0.3%<br>**4**<br>3.2%<br>2.8%<br>3.1%<br>3.2%<br>2.8%<br>1.8%<br>0.4%<br>**5**<br>3.1%<br>2.8%<br>3.5%<br>2.8%<br>2.6%<br>1.4%<br>0.4%<br>**6**<br>3.1%<br>2.9%<br>2.8%<br>3.1%<br>2.6%<br>1.5%<br>0.3%<br>**7**<br>2.6%<br>2.4%<br>2.9%<br>2.4%<br>2.1%<br>1.4%<br>0.6%<br>**8**<br>0.7%<br>0.7%<br>2.1%<br>2.5%<br>2.4%<br>1.3%<br>0.1%<br>**9**<br>0.1%<br>0.0%<br>0.3%<br>1.0%<br>1.8%<br>1.5%<br>1.0%<br>**10**<br>0.0%<br>0.0%<br>0.1%<br>0.3%<br>1.1%<br>1.1%<br>0.8%<br>**11**<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.3%<br>1.3%<br>0.0%<br>**12**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.6%<br>**13**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.6%<br>0.3%<br>**14**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.4%<br>0.3%<br>**15**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.7%<br>0.3%<br>**16**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.1%<br>**17**<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.0%<br>0.4%<br>0.1%<br>**18**<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.8%<br>1.3%<br>1.5%<br>**19**<br>0.0%<br>0.3%<br>1.1%<br>2.2%<br>1.8%<br>1.7%<br>1.5%<br>**20**<br>0.8%<br>0.8%<br>2.4%<br>2.6%<br>1.8%<br>1.5%<br>1.0%<br>**21**<br>2.2%<br>1.7%<br>3.6%<br>2.8%<br>1.9%<br>1.7%<br>1.3%<br>**22**<br>3.2%<br>2.5%<br>4.0%<br>3.1%<br>2.1%<br>1.7%<br>1.5%<br>**23**<br>2.9%<br>3.1%<br>3.6%<br>3.3%<br>1.8%<br>1.5%<br>1.3%<br>**Primavera**<br>Porcentaje de calmas, velocidad inferior a 0.5 (m/s) 2020 Nilahue-La Quebrada<br>**Magrugada**<br>**Mañana**<br>**Verano**<br>**Otoño**<br>**Invierno**<br>**Tarde**<br>**Noche**|**13**<br>**14**<br>**15**<br>**16**<br>**17**<br>**18**<br>**19**|0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%|0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.3%|0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>1.1%|0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>2.2%|0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.0%<br>0.8%<br>1.8%|0.6%<br>0.4%<br>0.7%<br>0.4%<br>0.4%<br>1.3%<br>1.7%|0.3%<br>0.3%<br>0.3%<br>0.1%<br>0.1%<br>1.5%<br>1.5%||||||
|**2020**<br>**ene**<br>**feb**<br>**mar**<br>**abr**<br>**may**<br>**jun**<br>**jul**<br>**ago**<br>**sept**<br>**oct**<br>**nov**<br>**dic**<br>**0**<br>3.3%<br>3.1%<br>3.9%<br>3.2%<br>1.9%<br>1.8%<br>0.8%<br>**1**<br>3.2%<br>3.2%<br>3.5%<br>3.3%<br>2.2%<br>1.9%<br>0.8%<br>**2**<br>3.2%<br>2.6%<br>3.1%<br>3.1%<br>2.4%<br>1.7%<br>0.3%<br>**3**<br>3.3%<br>2.6%<br>3.3%<br>3.2%<br>2.8%<br>1.7%<br>0.3%<br>**4**<br>3.2%<br>2.8%<br>3.1%<br>3.2%<br>2.8%<br>1.8%<br>0.4%<br>**5**<br>3.1%<br>2.8%<br>3.5%<br>2.8%<br>2.6%<br>1.4%<br>0.4%<br>**6**<br>3.1%<br>2.9%<br>2.8%<br>3.1%<br>2.6%<br>1.5%<br>0.3%<br>**7**<br>2.6%<br>2.4%<br>2.9%<br>2.4%<br>2.1%<br>1.4%<br>0.6%<br>**8**<br>0.7%<br>0.7%<br>2.1%<br>2.5%<br>2.4%<br>1.3%<br>0.1%<br>**9**<br>0.1%<br>0.0%<br>0.3%<br>1.0%<br>1.8%<br>1.5%<br>1.0%<br>**10**<br>0.0%<br>0.0%<br>0.1%<br>0.3%<br>1.1%<br>1.1%<br>0.8%<br>**11**<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.3%<br>1.3%<br>0.0%<br>**12**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.6%<br>**13**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.6%<br>0.3%<br>**14**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.4%<br>0.3%<br>**15**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.7%<br>0.3%<br>**16**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.1%<br>**17**<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.0%<br>0.4%<br>0.1%<br>**18**<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.8%<br>1.3%<br>1.5%<br>**19**<br>0.0%<br>0.3%<br>1.1%<br>2.2%<br>1.8%<br>1.7%<br>1.5%<br>**20**<br>0.8%<br>0.8%<br>2.4%<br>2.6%<br>1.8%<br>1.5%<br>1.0%<br>**21**<br>2.2%<br>1.7%<br>3.6%<br>2.8%<br>1.9%<br>1.7%<br>1.3%<br>**22**<br>3.2%<br>2.5%<br>4.0%<br>3.1%<br>2.1%<br>1.7%<br>1.5%<br>**23**<br>2.9%<br>3.1%<br>3.6%<br>3.3%<br>1.8%<br>1.5%<br>1.3%<br>**Primavera**<br>Porcentaje de calmas, velocidad inferior a 0.5 (m/s) 2020 Nilahue-La Quebrada<br>**Magrugada**<br>**Mañana**<br>**Verano**<br>**Otoño**<br>**Invierno**<br>**Tarde**<br>**Noche**|**20**<br>**21**|0.8%<br>2.2%|0.8%<br>1.7%|2.4%<br>3.6%|2.6%<br>2.8%|1.8%<br>1.9%|1.5%<br>1.7%|1.0%<br>1.3%||||||
|**2020**<br>**ene**<br>**feb**<br>**mar**<br>**abr**<br>**may**<br>**jun**<br>**jul**<br>**ago**<br>**sept**<br>**oct**<br>**nov**<br>**dic**<br>**0**<br>3.3%<br>3.1%<br>3.9%<br>3.2%<br>1.9%<br>1.8%<br>0.8%<br>**1**<br>3.2%<br>3.2%<br>3.5%<br>3.3%<br>2.2%<br>1.9%<br>0.8%<br>**2**<br>3.2%<br>2.6%<br>3.1%<br>3.1%<br>2.4%<br>1.7%<br>0.3%<br>**3**<br>3.3%<br>2.6%<br>3.3%<br>3.2%<br>2.8%<br>1.7%<br>0.3%<br>**4**<br>3.2%<br>2.8%<br>3.1%<br>3.2%<br>2.8%<br>1.8%<br>0.4%<br>**5**<br>3.1%<br>2.8%<br>3.5%<br>2.8%<br>2.6%<br>1.4%<br>0.4%<br>**6**<br>3.1%<br>2.9%<br>2.8%<br>3.1%<br>2.6%<br>1.5%<br>0.3%<br>**7**<br>2.6%<br>2.4%<br>2.9%<br>2.4%<br>2.1%<br>1.4%<br>0.6%<br>**8**<br>0.7%<br>0.7%<br>2.1%<br>2.5%<br>2.4%<br>1.3%<br>0.1%<br>**9**<br>0.1%<br>0.0%<br>0.3%<br>1.0%<br>1.8%<br>1.5%<br>1.0%<br>**10**<br>0.0%<br>0.0%<br>0.1%<br>0.3%<br>1.1%<br>1.1%<br>0.8%<br>**11**<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.3%<br>1.3%<br>0.0%<br>**12**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.6%<br>**13**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.6%<br>0.3%<br>**14**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.4%<br>0.3%<br>**15**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.7%<br>0.3%<br>**16**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.1%<br>**17**<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.0%<br>0.4%<br>0.1%<br>**18**<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.8%<br>1.3%<br>1.5%<br>**19**<br>0.0%<br>0.3%<br>1.1%<br>2.2%<br>1.8%<br>1.7%<br>1.5%<br>**20**<br>0.8%<br>0.8%<br>2.4%<br>2.6%<br>1.8%<br>1.5%<br>1.0%<br>**21**<br>2.2%<br>1.7%<br>3.6%<br>2.8%<br>1.9%<br>1.7%<br>1.3%<br>**22**<br>3.2%<br>2.5%<br>4.0%<br>3.1%<br>2.1%<br>1.7%<br>1.5%<br>**23**<br>2.9%<br>3.1%<br>3.6%<br>3.3%<br>1.8%<br>1.5%<br>1.3%<br>**Primavera**<br>Porcentaje de calmas, velocidad inferior a 0.5 (m/s) 2020 Nilahue-La Quebrada<br>**Magrugada**<br>**Mañana**<br>**Verano**<br>**Otoño**<br>**Invierno**<br>**Tarde**<br>**Noche**|**22**|3.2%|2.5%|4.0%|3.1%|2.1%|1.7%|1.5%||||||
|**2020**<br>**ene**<br>**feb**<br>**mar**<br>**abr**<br>**may**<br>**jun**<br>**jul**<br>**ago**<br>**sept**<br>**oct**<br>**nov**<br>**dic**<br>**0**<br>3.3%<br>3.1%<br>3.9%<br>3.2%<br>1.9%<br>1.8%<br>0.8%<br>**1**<br>3.2%<br>3.2%<br>3.5%<br>3.3%<br>2.2%<br>1.9%<br>0.8%<br>**2**<br>3.2%<br>2.6%<br>3.1%<br>3.1%<br>2.4%<br>1.7%<br>0.3%<br>**3**<br>3.3%<br>2.6%<br>3.3%<br>3.2%<br>2.8%<br>1.7%<br>0.3%<br>**4**<br>3.2%<br>2.8%<br>3.1%<br>3.2%<br>2.8%<br>1.8%<br>0.4%<br>**5**<br>3.1%<br>2.8%<br>3.5%<br>2.8%<br>2.6%<br>1.4%<br>0.4%<br>**6**<br>3.1%<br>2.9%<br>2.8%<br>3.1%<br>2.6%<br>1.5%<br>0.3%<br>**7**<br>2.6%<br>2.4%<br>2.9%<br>2.4%<br>2.1%<br>1.4%<br>0.6%<br>**8**<br>0.7%<br>0.7%<br>2.1%<br>2.5%<br>2.4%<br>1.3%<br>0.1%<br>**9**<br>0.1%<br>0.0%<br>0.3%<br>1.0%<br>1.8%<br>1.5%<br>1.0%<br>**10**<br>0.0%<br>0.0%<br>0.1%<br>0.3%<br>1.1%<br>1.1%<br>0.8%<br>**11**<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.3%<br>1.3%<br>0.0%<br>**12**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.6%<br>**13**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.6%<br>0.3%<br>**14**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.4%<br>0.3%<br>**15**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.7%<br>0.3%<br>**16**<br>0.0%<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.1%<br>**17**<br>0.0%<br>0.0%<br>0.0%<br>0.1%<br>0.0%<br>0.4%<br>0.1%<br>**18**<br>0.0%<br>0.0%<br>0.1%<br>0.4%<br>0.8%<br>1.3%<br>1.5%<br>**19**<br>0.0%<br>0.3%<br>1.1%<br>2.2%<br>1.8%<br>1.7%<br>1.5%<br>**20**<br>0.8%<br>0.8%<br>2.4%<br>2.6%<br>1.8%<br>1.5%<br>1.0%<br>**21**<br>2.2%<br>1.7%<br>3.6%<br>2.8%<br>1.9%<br>1.7%<br>1.3%<br>**22**<br>3.2%<br>2.5%<br>4.0%<br>3.1%<br>2.1%<br>1.7%<br>1.5%<br>**23**<br>2.9%<br>3.1%<br>3.6%<br>3.3%<br>1.8%<br>1.5%<br>1.3%<br>**Primavera**<br>Porcentaje de calmas, velocidad inferior a 0.5 (m/s) 2020 Nilahue-La Quebrada<br>**Magrugada**<br>**Mañana**<br>**Verano**<br>**Otoño**<br>**Invierno**<br>**Tarde**<br>**Noche**|**23**|2.9%|3.1%|3.6%|3.3%|1.8%|1.5%|1.3%||||||
|**Total calmas mes**|**Total calmas mes**|**35.0%**|**31.4%**|**43.3%**|**42.6%**|**35.6%**|**30.6%**|**15.6%**||||||

Página 26 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Porcentaje de calmas, velocidad inferior a 0.5 (m/s) 2021 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2021**|**2021**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2021**|**2021**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**<br>**Mañana**|**0**|||||2.5%|2.4%|2.8%|2.5%|3.2%|2.6%|2.8%|3.6%|
|**Magrugada**<br>**Mañana**|**1**|||||2.8%|2.2%|2.9%|2.6%|2.9%|2.5%|2.5%|3.8%|
|**Magrugada**<br>**Mañana**|**2**|||||2.6%|2.6%|2.5%|2.8%|3.1%|2.5%|2.6%|3.2%|
|**Magrugada**<br>**Mañana**|**3**|||||2.8%|2.6%|3.2%|2.5%|2.8%|2.4%|2.5%|2.9%|
|**Magrugada**<br>**Mañana**|**4**|||||2.8%|2.4%|2.5%|2.9%|2.9%|2.1%|2.8%|3.6%|
|**Magrugada**<br>**Mañana**|**5**<br>**6**<br>**7**<br>**8**<br>**9**|||||2.4%<br>3.1%<br>2.6%<br>2.5%<br>1.9%|2.5%<br>2.5%<br>2.8%<br>2.8%<br>2.2%|2.6%<br>2.2%<br>2.4%<br>2.5%<br>1.8%|2.9%<br>2.9%<br>2.8%<br>2.9%<br>2.4%|2.8%<br>3.1%<br>2.9%<br>1.9%<br>0.7%|2.6%<br>2.1%<br>1.5%<br>0.7%<br>0.0%|2.6%<br>2.2%<br>1.1%<br>0.0%<br>0.0%|2.5%<br>2.6%<br>1.1%<br>0.8%<br>0.1%|
|**Magrugada**<br>**Mañana**|**10**<br>**11**|||||1.0%<br>0.6%|1.9%<br>0.8%|1.5%<br>0.6%|1.0%<br>0.6%|0.3%<br>0.0%|0.0%<br>0.0%|0.0%<br>0.0%|0.0%<br>0.0%|
|**Tarde**|**12**|||||0.6%|0.7%|0.4%|0.4%|0.0%|0.0%|0.0%|0.0%|
|**Tarde**|**13**|||||0.1%|0.7%|0.1%|0.3%|0.0%|0.0%|0.0%|0.0%|
|**Tarde**|**14**|||||0.1%|0.4%|0.3%|0.1%|0.0%|0.0%|0.0%|0.0%|
|**Tarde**|**15**<br>**16**|||||0.0%<br>0.1%|0.7%<br>0.7%|0.1%<br>0.4%|0.1%<br>0.0%|0.0%<br>0.0%|0.0%<br>0.0%|0.0%<br>0.0%|0.0%<br>0.0%|
|**Tarde**|**17**|||||0.3%|0.4%|0.8%|0.0%|0.1%|0.0%|0.0%|0.0%|
|**Noche**|**18**|||||1.4%|1.5%|1.0%|1.0%|0.4%|0.0%|0.0%|0.0%|
|**Noche**|**19**|||||1.8%|1.3%|1.7%|1.8%|2.1%|1.7%|0.1%|0.0%|
|**Noche**|**20**|||||1.8%|2.4%|1.9%|2.2%|3.2%|2.9%|1.4%|0.6%|
|**Noche**|**21**|||||1.8%|2.4%|2.1%|2.4%|3.2%|3.2%|2.2%|1.7%|
|**Noche**|**22**|||||1.8%|2.6%|2.6%|2.4%|3.2%|3.1%|2.8%|2.8%|
|**Noche**|**23**|||||2.5%|2.8%|2.8%|2.8%|2.9%|2.8%|2.5%|3.3%|
|**Total calmas mes**|**Total calmas mes**|||||**39.9%**|**44.3%**|**41.8%**|**42.2%**|**41.7%**|**32.6%**|**28.2%**|**32.6%**|

Página 27 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Porcentaje de calmas, velocidad inferior a 0.5 (m/s) 2022 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2022**|**2022**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2022**|**2022**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**<br>**Mañana**|**0**|3.5%|3.5%|2.9%|2.5%|2.2%|2.6%|2.9%|2.6%|3.5%|2.9%|1.3%|3.5%|
|**Magrugada**<br>**Mañana**|**1**|3.3%|2.9%|2.9%|2.9%|2.2%|2.6%|2.8%|3.1%|3.6%|2.6%|1.4%|3.1%|
|**Magrugada**<br>**Mañana**|**2**|2.9%|3.2%|2.9%|2.5%|2.5%|2.8%|2.5%|3.2%|3.6%|3.3%|1.3%|3.5%|
|**Magrugada**<br>**Mañana**|**3**|3.5%|3.3%|2.2%|2.8%|2.4%|2.5%|2.8%|3.3%|3.6%|3.1%|1.5%|2.9%|
|**Magrugada**<br>**Mañana**|**4**|2.8%|2.8%|2.2%|2.8%|2.6%|2.1%|2.6%|2.5%|3.8%|2.2%|1.7%|2.9%|
|**Magrugada**<br>**Mañana**|**5**<br>**6**<br>**7**<br>**8**<br>**9**|3.1%<br>2.8%<br>1.9%<br>0.4%<br>0.3%|2.8%<br>2.6%<br>3.1%<br>1.5%<br>0.4%|1.9%<br>2.1%<br>2.9%<br>1.1%<br>0.3%|2.8%<br>2.6%<br>2.5%<br>2.4%<br>1.8%|2.6%<br>2.9%<br>3.2%<br>2.6%<br>1.7%|2.4%<br>2.4%<br>1.7%<br>2.4%<br>2.1%|2.5%<br>2.4%<br>2.5%<br>2.2%<br>2.4%|2.6%<br>2.8%<br>2.4%<br>2.8%<br>1.5%|3.5%<br>3.2%<br>2.8%<br>2.2%<br>1.3%|2.2%<br>2.2%<br>2.2%<br>0.7%<br>0.0%|1.5%<br>1.7%<br>1.3%<br>0.8%<br>0.1%|3.1%<br>2.9%<br>1.9%<br>0.7%<br>0.1%|
|**Magrugada**<br>**Mañana**|**10**<br>**11**|0.0%<br>0.0%|0.0%<br>0.0%|0.1%<br>0.1%|0.3%<br>0.4%|1.1%<br>1.1%|1.7%<br>1.1%|1.5%<br>1.5%|1.0%<br>0.6%|0.3%<br>0.0%|0.0%<br>0.0%|0.0%<br>0.0%|0.0%<br>0.0%|
|**Tarde**|**12**|0.0%|0.0%|0.1%|0.0%|1.1%|1.3%|0.4%|0.1%|0.0%|0.0%|0.0%|0.0%|
|**Tarde**|**13**|0.0%|0.0%|0.0%|0.1%|0.4%|0.7%|0.4%|0.1%|0.0%|0.0%|0.0%|0.0%|
|**Tarde**|**14**|0.0%|0.0%|0.0%|0.1%|0.4%|0.6%|0.4%|0.1%|0.1%|0.0%|0.0%|0.0%|
|**Tarde**|**15**<br>**16**|0.0%<br>0.0%|0.0%<br>0.0%|0.1%<br>0.0%|0.0%<br>0.0%|0.4%<br>0.3%|0.7%<br>0.4%|0.3%<br>0.7%|0.1%<br>0.1%|0.1%<br>0.3%|0.0%<br>0.1%|0.0%<br>0.0%|0.0%<br>0.0%|
|**Tarde**|**17**|0.0%|0.0%|0.0%|0.1%|0.6%|0.8%|0.8%|0.1%|0.1%|0.1%|0.1%|0.0%|
|**Noche**|**18**|0.0%|0.0%|0.0%|0.4%|1.1%|1.7%|1.9%|1.0%|0.6%|0.1%|0.3%|0.1%|
|**Noche**|**19**|0.1%|0.1%|0.6%|1.8%|1.4%|1.5%|1.7%|1.8%|2.4%|1.1%|0.1%|0.1%|
|**Noche**|**20**|1.3%|1.1%|1.9%|2.5%|1.7%|2.1%|2.2%|2.8%|2.8%|1.9%|0.8%|0.8%|
|**Noche**|**21**|1.5%|2.4%|2.4%|2.9%|2.8%|1.8%|2.4%|2.9%|2.8%|2.8%|1.1%|3.6%|
|**Noche**|**22**|2.5%|2.9%|3.3%|2.8%|2.5%|1.9%|2.6%|2.5%|3.6%|3.1%|1.4%|3.9%|
|**Noche**|**23**|3.2%|3.2%|3.5%|2.8%|2.6%|2.5%|2.8%|2.5%|3.8%|2.9%|1.3%|3.9%|
|**Total calmas mes**|**Total calmas mes**|**33.1%**|**35.8%**|**33.8%**|**39.9%**|**42.5%**|**42.2%**|**45.3%**|**42.6%**|**47.8%**|**33.8%**|**17.6%**|**37.1%**|

Página 28 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-15. Datos de dirección de viento 2020-2022 Nilahue-La Quebrada.

|Datos de dirección (°) 2020 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2020**|**2020**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2020**|**2020**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|223|200|42|128|146|51|29||||||
|**Magrugada**|**1**|158|17|140|58|164|2|24||||||
|**Magrugada**|**2**|228|109|182|112|179|52|18||||||
|**Magrugada**|**3**|200|154|162|169|158|41|30||||||
|**Magrugada**|**4**|197|162|197|114|188|49|38||||||
|**Magrugada**|**5**|199|174|228|131|166|35|20||||||
|**Mañana**|**6**|212|117|227|123|134|64|24||||||
|**Mañana**|**7**|197|149|162|180|160|24|36||||||
|**Mañana**|**8**|212|198|193|177|163|47|20||||||
|**Mañana**|**9**|200|203|214|207|194|17|6||||||
|**Mañana**|**10**|229|218|199|191|198|18|102||||||
|**Mañana**|**11**|198|194|188|200|199|16|114||||||
|**Tarde**|**12**|237|230|214|211|211|62|177||||||
|**Tarde**|**13**|262|247|217|206|193|24|212||||||
|**Tarde**|**14**|270|266|250|223|202|347|216||||||
|**Tarde**|**15**|273|273|262|238|201|35|227||||||
|**Tarde**|**16**|284|275|272|262|202|257|223||||||
|**Tarde**|**17**|271|284|275|253|212|314|256||||||
|**Noche**|**18**|275|272|280|257|205|3|276||||||
|**Noche**|**19**|264|277|289|248|188|45|70||||||
|**Noche**|**20**|290|283|324|120|163|33|51||||||
|**Noche**|**21**|275|271|327|125|194|32|45||||||
|**Noche**|**22**|243|281|31|103|160|11|23||||||
|**Noche**|**23**|235|236|46|139|156|48|45||||||
|||||||||||||||
|**Grados**|0|30|60|90|120|150|180|210|240|270|300|330|360|
|**Comp**|Norte|Noreste|Noreste|Este|Sureste|Sureste|Sur|Suroeste|Suroeste|Oeste|Noroeste|Noroeste|Norte|

Página 29 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Datos de dirección (°) 2021 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2021**|**2021**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2021**|**2021**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|49|124|202|29|27|158|205|293|
|**Magrugada**|**1**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|74|42|141|61|12|197|219|319|
|**Magrugada**|**2**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|47|104|134|39|38|211|221|332|
|**Magrugada**|**3**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|52|73|131|37|40|189|242|355|
|**Magrugada**|**4**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|34|41|127|40|39|184|240|37|
|**Magrugada**|**5**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|36|354|193|30|47|201|202|323|
|**Mañana**|**6**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|59|17|162|36|31|186|214|7|
|**Mañana**|**7**<br>**8**<br>**9**|#¡VALOR!<br>#¡VALOR!<br>#¡VALOR!|#¡VALOR!<br>#¡VALOR!<br>#¡VALOR!|#¡VALOR!<br>#¡VALOR!<br>#¡VALOR!|#¡VALOR!<br>#¡VALOR!<br>#¡VALOR!|26<br>6<br>59|57<br>41<br>127|199<br>95<br>185|48<br>20<br>25|55<br>157<br>188|189<br>196<br>190|195<br>194<br>190|13<br>231<br>230|
|**Mañana**|**10**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|193|207|188|89|193|200|214|208|
|**Mañana**|**11**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|193|181|196|195|202|199|210|252|
|**Tarde**|**12**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|208|186|196|212|198|184|211|234|
|**Tarde**|**13**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|190|182|192|209|228|207|259|268|
|**Tarde**|**14**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|202|199|198|212|226|243|258|282|
|**Tarde**|**15**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|205|204|197|228|239|244|273|277|
|**Tarde**|**16**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|211|196|208|241|258|257|275|271|
|**Tarde**|**17**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|220|194|211|240|258|257|283|281|
|**Noche**|**18**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|215|203|195|279|269|254|267|277|
|**Noche**|**19**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|186|192|191|24|297|261|262|274|
|**Noche**|**20**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|160|147|176|53|314|264|264|295|
|**Noche**|**21**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|123|85|179|31|26|272|261|273|
|**Noche**|**22**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|69|77|147|28|43|297|232|288|
|**Noche**|**23**|#¡VALOR!|#¡VALOR!|#¡VALOR!|#¡VALOR!|60|14|195|35|24|201|217|248|
|||||||||||||||
|**Grados**|0|30|60|90|120|150|180|210|240|270|300|330|360|
|**Comp**|Norte|Noreste|Noreste|Este|Sureste|Sureste|Sur|Suroeste|Suroeste|Oeste|Noroeste|Noroeste|Norte|

Página 30 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Datos de dirección (°) 2022 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2022**|**2022**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2022**|**2022**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|259|308|190|197|171|69|43|109|142|178|302|214|
|**Magrugada**|**1**|207|209|170|251|126|42|26|342|120|204|326|203|
|**Magrugada**|**2**|134|175|182|199|112|61|25|89|83|217|277|186|
|**Magrugada**|**3**|208|204|182|171|91|75|4|62|79|213|9|191|
|**Magrugada**|**4**|298|223|200|258|107|52|17|122|91|215|1|202|
|**Magrugada**|**5**|225|199|219|121|106|48|31|213|345|192|330|203|
|**Mañana**|**6**|158|211|227|155|200|30|48|169|79|214|292|204|
|**Mañana**|**7**<br>**8**<br>**9**|218<br>214<br>212|187<br>215<br>205|221<br>222<br>209|191<br>116<br>166|161<br>207<br>187|5<br>48<br>58|42<br>8<br>42|194<br>159<br>159|34<br>210<br>193|205<br>193<br>194|15<br>342<br>293|199<br>200<br>198|
|**Mañana**|**10**|209|208|202|193|176|37|34|186|200|203|350|202|
|**Mañana**|**11**|218|202|203|210|198|22|13|194|186|197|8|215|
|**Tarde**|**12**|237|231|211|204|201|67|141|193|195|204|264|230|
|**Tarde**|**13**|281|249|213|205|205|100|198|191|201|225|288|257|
|**Tarde**|**14**|280|277|227|230|191|208|188|190|215|249|292|265|
|**Tarde**|**15**|281|271|254|234|204|230|181|211|225|246|272|277|
|**Tarde**|**16**|284|273|258|244|194|255|226|215|240|248|291|272|
|**Tarde**|**17**|270|287|256|250|202|285|272|209|262|252|285|284|
|**Noche**|**18**|279|268|264|251|207|339|17|213|266|254|296|277|
|**Noche**|**19**|287|282|259|271|187|77|66|258|298|253|285|281|
|**Noche**|**20**|297|302|246|270|175|96|48|77|300|230|261|296|
|**Noche**|**21**|292|297|231|280|176|46|46|32|38|227|286|329|
|**Noche**|**22**|296|106|168|134|162|58|44|55|77|197|264|8|
|**Noche**|**23**|301|54|157|227|161|61|66|111|121|192|307|251|
|||||||||||||||
|**Grados**|0|30|60|90|120|150|180|210|240|270|300|330|360|
|**Comp**|Norte|Noreste|Noreste|Este|Sureste|Sureste|Sur|Suroeste|Suroeste|Oeste|Noroeste|Noroeste|Norte|

Página 31 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-16. Rosa de frecuencias de velocidad y dirección de viento 2020-2022 Nilahue-La Quebrada.

|Rosa de vientos, frecuencias por dirección y velocidad 2020 Nilahue-La Quebrada<br>N<br>NNO 6% NNE<br>[0,1[<br>5%<br>NO NE<br>4% [1-2[<br>3%<br>[2,3[<br>ONO ENE<br>2%<br>[3,4[<br>1%<br>O 0% E [4,5[<br>[5,6[<br>OSO ESE<br>[6,7[<br>[7,8[<br>SO SE<br>[8,9[<br>SSO SSE<br>S|Col2|
|---|---|
|0,0%<br>1,0%<br>2,0%<br>3,0%<br>4,0%<br>5,0%<br>6,0%<br>N<br>NNE<br>NE<br>ENE<br>E<br>ESE<br>SE<br>SSE<br>S<br>SSO<br>SO<br>OSO<br>O<br>ONO<br>NO<br>NNO<br>Rosa de vientos, frecuencias por dirección<br>y velocidad, verano 2020 Nilahue-La<br>Quebrada<br>[0,1[<br>[1-2[<br>[2,3[<br>[3,4[<br>[4,5[<br>[5,6[<br>[6,7[<br>[7,8[<br>[8,9[|0,0%<br>1,0%<br>2,0%<br>3,0%<br>4,0%<br>N<br>NNE<br>NE<br>ENE<br>E<br>ESE<br>SE<br>SSE<br>S<br>SSO<br>SO<br>OSO<br>O<br>ONO<br>NO<br>NNO<br>Rosa de vientos, frecuencias por dirección<br>y velocidad, otoño 2020 Nilahue-La<br>Quebrada<br>[0,1[<br>[1-2[<br>[2,3[<br>[3,4[<br>[4,5[<br>[5,6[<br>[6,7[<br>[7,8[<br>[8,9[|
|0,0%<br>0,5%<br>1,0%<br>1,5%<br>2,0%<br>2,5%<br>3,0%<br>3,5%<br>4,0%<br>N<br>NNE<br>NE<br>ENE<br>E<br>ESE<br>SE<br>SSE<br>S<br>SSO<br>SO<br>OSO<br>O<br>ONO<br>NO<br>NNO<br>Rosa de vientos, frecuencias por dirección<br>y velocidad, invierno 2020 Nilahue-La<br>Quebrada<br>[0,1[<br>[1-2[<br>[2,3[<br>[3,4[<br>[4,5[<br>[5,6[<br>[6,7[<br>[7,8[<br>[8,9[|0,0%<br>0,5%<br>1,0%<br>1,5%<br>2,0%<br>2,5%<br>3,0%<br>3,5%<br>4,0%<br>N<br>NNE<br>NE<br>ENE<br>E<br>ESE<br>SE<br>SSE<br>S<br>SSO<br>SO<br>OSO<br>O<br>ONO<br>NO<br>NNO<br>Rosa de vientos, frecuencias por dirección<br>y velocidad, primavera 2020 Nilahue-La<br>Quebrada<br>[0,1[<br>[1-2[<br>[2,3[<br>[3,4[<br>[4,5[<br>[5,6[<br>[6,7[<br>[7,8[<br>[8,9[|

Página 32 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Página 33 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Página 34 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

### 2.4 Análisis de radiación

Con relación a la radiación solar, su modulación obedece principalmente a fenómenos de

escala planetaria, atenuada o exacerbada ligeramente por la nubosidad, donde la magnitud

de los valores obedece principalmente a la latitud y época del año de las mediciones. Como

es de esperar, se observa mayor radiación solar durante las estaciones cálidas, entre los

meses de diciembre y enero, conforme se avanza hacia mediaros de año se puede ver otro

comportamiento esperable, que es la disminución en magnitud de los valores de radiación

solar y la duración en que este fenómeno se manifiesta.

Página 35 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-17. Radiación solar diaria 2020-2022 Nilahue-La Quebrada.

Figura 2-18. Ciclo diario de radiación solar 2020-2022 Nilahue-La Quebrada.

Figura 2-19. Ciclo anual de radiación solar 2020-2022 Nilahue-La Quebrada.

Página 36 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-20. Datos de radiación solar 2020-2022 Nilahue-La Quebrada.

|Datos de radiación solar (W/m2) 2020 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2020**|**2020**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2020**|**2020**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|0|0|0|0|0|0|0||||||
|**Magrugada**|**1**|0|0|0|0|0|0|0||||||
|**Magrugada**|**2**|0|0|0|0|0|0|0||||||
|**Magrugada**|**3**|0|0|0|0|0|0|0||||||
|**Magrugada**|**4**|0|0|0|0|0|0|0||||||
|**Magrugada**|**5**|3.2|0|0|0|0|0|0||||||
|**Mañana**|**6**|59.5|32.6|0.8|0|0|0.1|0||||||
|**Mañana**|**7**|206.6|145.8|28|7.9|4.6|0.4|0||||||
|**Mañana**|**8**|408.3|348.6|226.7|149.8|75|35.7|45.9||||||
|**Mañana**|**9**|620.1|569.2|427.6|308.2|196.3|122.9|177.3||||||
|**Mañana**|**10**|808.5|754.8|614.4|457.6|325|229.5|262.8||||||
|**Mañana**|**11**|934.7|886.8|745.1|564|412.5|322.1|355.9||||||
|**Tarde**|**12**|995.3|961.5|824.1|625.1|463.4|346|388.7||||||
|**Tarde**|**13**|1009.1|976.6|828.6|629.6|474.6|318.8|365.5||||||
|**Tarde**|**14**|958.9|927.7|781.9|574.8|406.4|275|338.8||||||
|**Tarde**|**15**|857.7|821.7|657.2|460.5|304.1|203.4|243.5||||||
|**Tarde**|**16**|685.4|648.8|487.6|298.6|159.2|66.7|124||||||
|**Tarde**|**17**|465.6|422.5|268.6|115.2|22.5|9.9|20||||||
|**Noche**|**18**|233.8|188.2|39.2|0.5|0|0|0||||||
|**Noche**|**19**|50.1|0|0|0|0|0|0||||||
|**Noche**|**20**|0|0|0|0|0|0|0||||||
|**Noche**|**21**|0|0|0|0|0|0|0||||||
|**Noche**|**22**|0|0|0|0|0|0|0||||||
|**Noche**|**23**|0|0|0|0|0|0|0||||||
|**x mensual**|**x mensual**|**345.7**|**320.2**|**247.1**|**174.7**|**118.5**|**80.4**|**96.8**||||||
|**x estacional**|**x estacional**|**304.3**|**304.3**|**304.3**|**124.5**|**124.5**|**124.5**|**96.8**|**96.8**|**96.8**||||
|**x anual**|**x anual**|**197.6**|**197.6**|**197.6**|**197.6**|**197.6**|**197.6**|**197.6**|**197.6**|**197.6**|**197.6**|**197.6**|**197.6**|

Página 37 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Datos de radiación solar (W/m2) 2021 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2021**|**2021**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2021**|**2021**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|||||0|0|0|0|0|0|0|0|
|**Magrugada**|**1**|||||0|0|0|0|0|0|0|0|
|**Magrugada**|**2**|||||0|0|0|0|0|0|0|0|
|**Magrugada**|**3**|||||0|0|0|0|0|0|0|0|
|**Magrugada**|**4**|||||0|0|0|0|0|0|0|0|
|**Magrugada**|**5**|||||0|0|0|0|0|0.1|4.7|5.8|
|**Mañana**|**6**|||||0|0|0|0|2.5|41.3|88|77.9|
|**Mañana**|**7**|||||3.6|0.1|0.2|8.3|73.3|207|248.3|217.4|
|**Mañana**|**8**|||||72.1|37.8|44.6|74.2|217.5|429.2|437.6|401.5|
|**Mañana**|**9**|||||177.9|149.1|153.4|168.1|391.2|621.5|645.5|575.8|
|**Mañana**|**10**|||||292.2|242.8|265|281.4|578.3|773.5|842.6|775.9|
|**Mañana**|**11**|||||417.7|337.7|354.5|389.2|697.3|882.9|966.4|913.4|
|**Tarde**|**12**|||||455.8|373.9|398.6|457.3|763.4|915|987.2|983|
|**Tarde**|**13**|||||461|392.9|416.7|438.6|710.9|901.5|1004.5|959.9|
|**Tarde**|**14**|||||389.1|327.6|377.4|378.5|632.4|809.1|913|907.8|
|**Tarde**|**15**|||||278.4|230.2|306.3|321.4|511.4|674.8|776.7|803.1|
|**Tarde**|**16**|||||141|78.7|136.8|212.4|349.6|491.1|602.7|625.7|
|**Tarde**|**17**|||||17.6|11.4|18.8|68.6|171.3|282.1|383.2|436|
|**Noche**|**18**|||||0|0|0|1.5|22.1|73.5|159.6|225.6|
|**Noche**|**19**|||||0|0|0|0|0|0.1|13.8|48.5|
|**Noche**|**20**|||||0|0|0|0|0|0|0|0|
|**Noche**|**21**|||||0|0|0|0|0|0|0|0|
|**Noche**|**22**|||||0|0|0|0|0|0|0|0|
|**Noche**|**23**|||||0|0|0|0|0|0|0|0|
|**x mensual**|**x mensual**|||||**112.8**|**90.9**|**103**|**116.6**|**213.4**|**295.9**|**336.4**|**331.6**|
|**x estacional**|**x estacional**||||**101.9**|**101.9**|**101.9**|**144.3**|**144.3**|**144.3**|**321.3**|**321.3**|**321.3**|
|**x anual**|**x anual**|**200.1**|**200.1**|**200.1**|**200.1**|**200.1**|**200.1**|**200.1**|**200.1**|**200.1**|**200.1**|**200.1**|**200.1**|

Página 38 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Datos de radiación solar (W/m2) 2022 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2022**|**2022**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2022**|**2022**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|0|0|0|0|0|0|0|0|0|0|0|0|
|**Magrugada**|**1**|0|0|0|0|0|0|0|0|0|0|0|0|
|**Magrugada**|**2**|0|0|0|0|0|0|0|0|0|0.1|0|0|
|**Magrugada**|**3**|0|0|0|0|0|0|0|0|0|0|0|0|
|**Magrugada**|**4**|0|0|0|0|0|0|0|0|0|0|0|0|
|**Magrugada**|**5**|0.5|0|0|0|0|0|0|0|0|0.1|2.1|8.7|
|**Mañana**|**6**|49.5|14.6|1.2|0|0|0|0|0|2.2|36.9|56.2|119.7|
|**Mañana**|**7**|176.8|128.2|66.1|25.8|4.2|0.2|0.4|10.4|59.4|168.3|176.3|310.8|
|**Mañana**|**8**|342.5|312.7|224.2|142.1|70.6|29.3|38.8|93.3|194.5|347.3|334.6|528.4|
|**Mañana**|**9**|526.1|521.3|413.5|282.6|174.6|114.6|130.2|212.9|341.1|539.3|460|717.6|
|**Mañana**|**10**|690.6|701.1|595.7|419.1|285.1|220.9|223|338.4|505.5|704.5|578.4|887.3|
|**Mañana**|**11**|844.5|832.3|722.9|524.1|375.9|297.7|318.5|466.2|598.8|841.7|729.5|989.8|
|**Tarde**|**12**|954|899|813.2|593.2|413.6|343.6|353.8|514.2|624.6|902.4|823.3|1046|
|**Tarde**|**13**|998.8|911.7|815.7|567.2|412.9|341.2|367.6|506.9|622.9|891|797.4|1048.7|
|**Tarde**|**14**|957.4|862.8|769|520.8|345.6|275.4|330.5|463.7|555.1|787|704.1|988.4|
|**Tarde**|**15**|861|755.8|657.8|406.4|271|203.3|266.1|346.1|459.2|664.9|617.4|871.1|
|**Tarde**|**16**|690.7|594.4|495.3|276|139.1|66.8|119.9|220.7|326.4|476.9|483.3|691.3|
|**Tarde**|**17**|481|393.3|289.1|115.5|21.5|10.7|21.7|78.5|156.3|278.1|281.8|474.9|
|**Noche**|**18**|263.3|183.3|82.1|7.4|0|0|0|1.9|21.9|78.6|118.4|248.4|
|**Noche**|**19**|71.6|27.1|1.1|0|0|0|0|0|0|0.3|9.9|54|
|**Noche**|**20**|0.1|0|0|0|0|0|0|0|0|0|0|0|
|**Noche**|**21**|0|0|0|0|0|0|0|0|0|0|0|0|
|**Noche**|**22**|0|0|0|0|0|0|0|0|0|0|0|0|
|**Noche**|**23**|0|0|0|0|0|0|0|0|0|0|0|0|
|**x mensual**|**x mensual**|**329.5**|**297.4**|**247.8**|**161.7**|**104.8**|**79.3**|**90.4**|**135.6**|**186.2**|**279.9**|**257.2**|**374.4**|
|**x estacional**|**x estacional**|**291.6**|**291.6**|**291.6**|**115.3**|**115.3**|**115.3**|**137.4**|**137.4**|**137.4**|**303.8**|**303.8**|**303.8**|
|**x anual**|**x anual**|**212**|**212**|**212**|**212**|**212**|**212**|**212**|**212**|**212**|**212**|**212**|**212**|

Página 39 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

### 2.5 Análisis de precipitación

Analizando las precipitaciones, en las figuras siguientes se puede ver que las precipitaciones

se distribuyen en otoño-invierno e inicios de la primavera. De los días en que se registró

precipitación, se puede ver que, a nivel diario, se presentan mayoritariamente durante el

período de transición madrugada-mañana y el período de transición tarde-noche.

En general, las precipitaciones son abundantes y se distribuyen a lo largo de varios meses del

año, y los días en que se registran precipitaciones, estas abarcan gran cantidad de las horas

del día, siendo 2020 el año que registró la menor cantidad de precipitaciones.

Página 40 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-21. Precipitación diaria 2020-2022 Nilahue-La Quebrada.

Figura 2-22 Perfil diario de precipitación 2020-2022 Nilahue-La Quebrada.

Figura 2-23. Perfil anual de precipitación 2020-2022 Nilahue-La Quebrada.

Página 41 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 2-24 . Datos de precipitación 2020-2022 Nilahue-La Quebrada.

|Precipitación acumulada (mm) 2020 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2020**|**2020**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2020**|**2020**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|0|0|0|0.6|0|3.1|0|0|0|0|0|0|
|**Magrugada**|**1**|0|0|0|0.8|0.4|3.2|0|0|0|0|0|0|
|**Magrugada**|**2**|0|0|0|0.8|0.1|3.7|0.1|0|0|0|0|0|
|**Magrugada**|**3**|0|0|0|1.1|0.5|3.1|0|0|0|0|0|0|
|**Magrugada**|**4**|0|0|0|1.4|0.4|2.9|0|0|0|0|0|0|
|**Magrugada**|**5**|0|0|0|1.1|0.2|2.7|0.2|0|0|0|0|0|
|**Mañana**|**6**|0|0|0|0.7|0.5|2.8|0.2|0|0|0|0|0|
|**Mañana**|**7**|0|0|0|0.7|0.3|2.6|0.1|0|0|0|0|0|
|**Mañana**|**8**|0|0|0|0.5|0.4|2.1|0|0|0|0|0|0|
|**Mañana**|**9**|0|0|0|0.3|0.3|2.6|0.5|0|0|0|0|0|
|**Mañana**|**10**|0|0|0|0.3|0.2|2.9|0.4|0|0|0|0|0|
|**Mañana**|**11**|0|0|0|0.4|0.2|2.7|0.3|0|0|0|0|0|
|**Tarde**|**12**|0|0|0|0.3|0.1|3|0.4|0|0|0|0|0|
|**Tarde**|**13**|0|0|0|0.2|0.3|2.4|0.1|0|0|0|0|0|
|**Tarde**|**14**|0|0|0|0.4|0.2|2.1|0.3|0|0|0|0|0|
|**Tarde**|**15**|0|0|0|0.2|0.2|2.4|0|0|0|0|0|0|
|**Tarde**|**16**|0|0|0|0.1|0.1|2.1|0.7|0|0|0|0|0|
|**Tarde**|**17**|0|0|0|0.1|0|2.5|0.4|0|0|0|0|0|
|**Noche**|**18**|0|0|0|0.3|0.1|2.3|0.1|0|0|0|0|0|
|**Noche**|**19**|0|0|0|0.3|0.1|2.1|0.3|0|0|0|0|0|
|**Noche**|**20**|0|0|0|0.1|0|2.1|0.1|0|0|0|0|0|
|**Noche**|**21**|0|0|0|0.3|0|1.9|0.1|0|0|0|0|0|
|**Noche**|**22**|0|0|0|0.3|0.1|2.5|0.1|0|0|0|0|0|
|**Noche**|**23**|0|0|0|0.3|0.1|3|0.1|0|0|0|0|0|
|**Σ mensual**|**Σ mensual**|**0**|**0**|**0**|**11.6**|**4.8**|**62.8**|**4.5**|**0**|**0**|**0**|**0**|**0**|
|**Σ estacional**|**Σ estacional**|**0**|**0**|**0**|**79.2**|**79.2**|**79.2**|**4.5**|**4.5**|**4.5**|**0**|**0**|**0**|
|**Σ anual**|**Σ anual**|**83.7**|**83.7**|**83.7**|**83.7**|**83.7**|**83.7**|**83.7**|**83.7**|**83.7**|**83.7**|**83.7**|**83.7**|

Página 42 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Precipitación acumulada (mm) 2021 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2021**|**2021**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2021**|**2021**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|0|0|0|0|0|2.6|2.8|1.4|6.7|1.4|0|0|
|**Magrugada**|**1**|0|0|0|0|0|6.2|1.8|0.7|4.4|0.1|0|0|
|**Magrugada**|**2**|0|0|0|0|1.2|4.9|0.5|0.3|5.1|0.5|0|0|
|**Magrugada**|**3**|0|0|0|0|0.6|7.2|0.3|0.2|0.5|0.6|0|0|
|**Magrugada**|**4**|0|0|0|0|2.9|2.7|0.2|1.7|0.6|0.4|0.1|0|
|**Magrugada**|**5**|0|0|0|0|8.1|3.6|0.1|7|0.3|0.1|0.1|0|
|**Mañana**|**6**|0|0|0|0|3.7|0.6|0.1|2.9|0.2|0.1|0|0|
|**Mañana**|**7**|0|0|0|0|2.2|9.5|0.5|2.6|0|0|0|0|
|**Mañana**|**8**|0|0|0|0|2.3|2.9|1.9|3.9|0.8|0|0|0|
|**Mañana**|**9**|0|0|0|0|3|1.4|1.8|2|0.1|0|0|0|
|**Mañana**|**10**|0|0|0|0|3.3|0.1|1.8|4.5|0|0|0|0|
|**Mañana**|**11**|0|0|0|0|3|0|0.1|3.9|0.1|0|0|0|
|**Tarde**|**12**|0|0|0|0|0.4|0.9|0|3.7|0|0|0|0|
|**Tarde**|**13**|0|0|0|0|0.1|0.9|0|6.1|0.1|0|0|0|
|**Tarde**|**14**|0|0|0|0|0|0|0|8.2|0|0|0|0|
|**Tarde**|**15**|0|0|0|0|0.3|0.3|0.2|6.8|0|0|0|0|
|**Tarde**|**16**|0|0|0|0|0.1|0.2|0.1|4.5|0|0|0|0|
|**Tarde**|**17**|0|0|0|0|0.1|0.1|0|3.8|0.1|0|0|0|
|**Noche**|**18**|0|0|0|0|0|0|0|5.8|2.5|0|0|0|
|**Noche**|**19**|0|0|0|0|0|0|0|6.4|6.9|0|0|0|
|**Noche**|**20**|0|0|0|0|0|0|0|2.6|3.9|0|0|0|
|**Noche**|**21**|0|0|0|0|0|0|0|2.9|0.7|0|0|0|
|**Noche**|**22**|0|0|0|0|0|0.2|0|2.1|0.1|0.8|0|0|
|**Noche**|**23**|0|0|0|0|0|0.9|0|2.1|0|2.2|0|0|
|**Σ mensual**|**Σ mensual**|**0**|**0**|**0**|**0**|**31.3**|**45.2**|**12.2**|**86.1**|**33.1**|**6.2**|**0.2**|**0**|
|**Σ estacional**|**Σ estacional**|**0**|**0**|**0**|**76.5**|**76.5**|**76.5**|**131.4**|**131.4**|**131.4**|**6.4**|**6.4**|**6.4**|
|**Σ anual**|**Σ anual**|**214.3**|**214.3**|**214.3**|**214.3**|**214.3**|**214.3**|**214.3**|**214.3**|**214.3**|**214.3**|**214.3**|**214.3**|

Página 43 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Precipitación acumulada (mm) 2022 Nilahue-La Quebrada|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2022**|**2022**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2022**|**2022**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|0|0|0|0.5|1|1.8|6|0.2|0.7|0|0.2|0|
|**Magrugada**|**1**|0|0|0|0.1|1.9|1.6|5.1|0.2|0.3|0.2|0.3|0|
|**Magrugada**|**2**|0|0|0|0.8|0.6|3.2|3.5|0.4|0|0|0.1|0|
|**Magrugada**|**3**|0|0|0|0.2|0.7|2.2|8.9|0.7|0|0|0|0|
|**Magrugada**|**4**|0|0.1|0|0.8|1|3|10.1|1.2|0.1|0|0|0|
|**Magrugada**|**5**|0|0|0|1.7|1.5|0.7|10|5.5|0|0|1.4|0|
|**Mañana**|**6**|0|0|0|1.1|3|2.7|7.2|4.3|0.2|0|4.3|0|
|**Mañana**|**7**|0|0|0|1|1.6|2.4|2.5|2.4|0.1|0|5.9|0|
|**Mañana**|**8**|0|0|0|0.6|2.8|3.7|6.9|0.8|0.2|0|1.4|0|
|**Mañana**|**9**|0|0|0|1.9|0.7|3.5|2.1|1.5|0|0|0.3|0|
|**Mañana**|**10**|0|0|0|0.3|0.3|1.5|2.8|1.4|0|0|0|0|
|**Mañana**|**11**|0|0|0|0.1|0.1|1.6|5.7|0.7|0|0|0.7|0|
|**Tarde**|**12**|0|0.6|0|0.2|0.1|2.2|8.4|4.3|2.2|0|0.2|0|
|**Tarde**|**13**|0|0.4|0.2|1.9|0|3.3|5.5|4.9|2.8|0|0|0|
|**Tarde**|**14**|0|0|0|12.1|0.1|4.8|2.6|0.5|3.7|0|0|2|
|**Tarde**|**15**|0|0|0|5.7|0.1|2.8|0.4|2.6|1.2|0|2|0|
|**Tarde**|**16**|0|0.1|0|0.8|1.1|3.5|2.5|2.2|1.4|0|0.8|0|
|**Tarde**|**17**|0|0|0|5.4|0.4|4.9|1.4|0.8|2.1|0|0.4|0|
|**Noche**|**18**|0|0|0|4.1|0.9|3|1|1.4|2.3|0|0.3|0|
|**Noche**|**19**|0|0|0|3.9|1.4|3.6|0.2|2.9|1.7|0|0|0|
|**Noche**|**20**|0|0|0|0.6|3.1|4|0.1|3.6|0.7|0|0|0|
|**Noche**|**21**|0|0|0|0.3|2.1|2.7|6|0.8|0.9|0|0|0|
|**Noche**|**22**|0|0|0|0.4|2.1|4.6|12.8|0|1.4|0|0|0|
|**Noche**|**23**|0|0|0|0.8|1|6.1|5.7|0.1|0.6|0|0|0|
|**Σ mensual**|**Σ mensual**|**0**|**1.2**|**0.2**|**45.3**|**27.6**|**73.4**|**117.4**|**43.4**|**22.6**|**0.2**|**18.3**|**2**|
|**Σ estacional**|**Σ estacional**|**1.4**|**1.4**|**1.4**|**146.3**|**146.3**|**146.3**|**183.4**|**183.4**|**183.4**|**20.5**|**20.5**|**20.5**|
|**Σ anual**|**Σ anual**|**351.6**|**351.6**|**351.6**|**351.6**|**351.6**|**351.6**|**351.6**|**351.6**|**351.6**|**351.6**|**351.6**|**351.6**|

Página 44 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas de Rengo

## 3. Modelación meteorológica y dispersión

Para la generación de la base de datos de variables meteorológicas, se utilizó el modelo WRF

versión 4.3. Éste es un modelo meteorológico de alta resolución, desarrollado para la

simulación de variables meteorológicas, mediante la resolución de las ecuaciones físicas que

describen los movimientos de la atmósfera, utilizando aproximaciones basadas en métodos

numéricos.

Este modelo se encuentra en constante desarrollo y mejora por medio de una asociación

colaborativa, principalmente entre el National Center Research (NCAR, USA), National

Oceanic and Atmospheric Administration (NCEP, USA), Forecast Systems Laboratory (FSL,

USA), Air Force Weather Agency (AFWA, USA), el Naval Research Laboratory, University of

Oklahoma, y la Federal Aviation Administration (FAA, USA). WRF es un Software Libre y

comunitario, por lo que su desarrollo y mejoramiento se realiza en distintos sitios alrededor

del mundo por voluntarios que deseen contribuir al proyecto [2] .

En el presente informe se utilizó la información meteorológica correspondiente al año

meteorológico completo y validado 2022. Esta información se obtuvo a partir del CISL

Research Data Archive (NCAR, USA), utilizándose el conjunto de datos de entrada ds083.2.

NCAR (National Center for Atmospherical Research) ofrece a los científicos de Estados Unidos

y del mundo, una gran cantidad de herramientas, desde modelos comunitarios hasta aviones

de investigación, supercomputadores y talleres. Los científicos internos de NCAR colaboran

con sus colegas en el mundo académico, el gobierno y el sector privado para construir,

refinar y ampliar los recursos de la comunidad de NCAR para que sean lo más relevantes y

útiles posible [3] .

Para el dominio de modelación, la configuración del modelo WRF, comprendió la

parametrización de variables propias de los fenómenos de microescala que inciden en la

dispersión de los contaminantes, esto es: parametrizaciones de microfísica de nubes,

2 [The Weather Research & Forecasting Model, NCAR/UCAR, https://www.mmm.ucar.edu/weather-research-](https://www.mmm.ucar.edu/weather-research-and-forecasting-model)
[and-forecasting-model](https://www.mmm.ucar.edu/weather-research-and-forecasting-model)
3 [National Center for Atmospheric Research, NCAR/UCAR, https://ncar.ucar.edu/what-we-offer](https://ncar.ucar.edu/what-we-offer)

Página 45 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

fenómenos radiativos, altura de la capa de mezcla y fenómenos turbulentos causados por la

orografía. En la Tabla 3-1 se detallan las configuraciones de importancia con las cuales se

ejecutó la modelación.

Tabla 3-1. Configuración física del modelo WRF 4.3, dominio más pequeño, de mayor resolución.

|Parámetro|Configuración|
|---|---|
|Centro Latitud (WGS-84)|-34,477943|
|Centro Longitud (WGS-84)|-71,485390|
|Condiciones de entrada|https://rda.ucar.edu FNL DS083.2 2022|
|Proyección cartográfica|Lambert Conformal|
|Puntos en X|50|
|Puntos en Y|50|
|Topografía|GTOPO30 (Aproximadamente 1 Kilómetro)|
|Uso de suelo|USGS (Aproximadamente 1 Kilómetro)|
|Resolución horizontal (Km)|1|
|Resolución vertical (niveles)|35 niveles hasta 5 hPa|
|Microfísica<br>mp_physics = 6|“WRF Single-Moment 6-class scheme”. Esquema<br>micro físico de 6 clases, que incorpora además de<br>líquidos, hielo y nieve. Parametrización ideal para<br>simulaciones a alta resolución. Esquema que<br>diferencia el tipo de precipitación liquida o sólida,<br>variables necesarias para CALPUFF|
|Radiación (Onda larga y Corta)<br>ra_lw_physics = 1<br>ra_sw_physics = 1|“RRTMG”. Esquema radiativo simple y eficiente,<br>capaz de simular los fenómenos radiativos de onda<br>larga a través del solapamiento de capas nubosas.<br>Esquema<br>simple<br>y <br>eficiente,<br>ampliamente<br>documentado. Utilizado como parametrización por<br>defecto por WRF y por el equipo de testeo y mejora<br>continua.|
|Modelo de suelo<br>sf_sfclay_physics =2|“Noah LSM”. Modelo de Superficie de Tierra (Land<br>Surface Model, LSM), que tiene en cuenta una serie<br>de procesos importantes en la capa superficial de<br>suelo, como el flujo de calor sensible, el flujo de calor<br>latente, la humedad del suelo y la temperatura del<br>suelo. Proporciona una descripción detallada de la<br>interacción suelo-atmósfera y se utiliza en una|

Página 46 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Col1|variedad de aplicaciones meteorológicas y<br>climáticas.|
|---|---|
|Interacción suelo atmósfera<br>sf_surface_physics = 2|“Noah LSM”. Esquema de difusión que considera<br>múltiples factores: Transferencia de calor sensible y<br>latente, Almacenamiento de calor en el suelo,<br>Humedad del suelo, Parámetros y características del<br>suelo y Modelado de la cubierta terrestre.|
|Capa planetaria<br>bl_pbl_physics = 2|“MYJ”. Esquela Mellor - Yamada - Janjic, que<br>considera procesos de Turbulencia y mezcla vertical,<br>además de Estabilidad atmosférica|
|Física urbana<br>sf_urban_physics = 1|“Single-layer, UCM”. Parametrización incorporada<br>para mejorar la representación de las interacciones<br>suelo-atmósfera en zonas donde se concentra y se<br>presenta uso de suelos con clasificación urbana.|
|Sombra topográfica<br>topo_shading =1|Efectos de sombra topográfica en vecindades de<br>accidentes geográficos de importancia. Activado.<br>Parametrización incorporada para considerar los<br>efectos de diferencia de calentamiento en zonas<br>ubicadas a la sombra de accidentes geográficos. Las<br>diferencias de calentamiento influyen en la<br>generación de viento térmico.|
|Corrección de viento por topografía<br>topo_wind = 2|Corrección topográfica de los vientos en superficie<br>para representar el arrastre adicional de la<br>topografía. Se muestra que reduce los sesgos de<br>viento de 10 m, estando diseñado para resoluciones<br>menores a 2 km, por lo que aplica la presente<br>modelación.|

En relación con las parametrizaciones dinámicas, no han sido modificadas en relación con la

configuración por defecto y recomendada. De lo anterior se desprende que el dominio más

pequeño definido, considera una zona de 50x50 kilómetros a 1 kilómetro de resolución

espacial, los que se consideran lo suficientemente amplios como para incorporar fenómenos

de escala sinóptica en sus dominios parentales, propios de la zona como los sistemas

frontales o la incursión de altas frías migratorias, con la capacidad de incorporar fenómenos

de meso escala como oscilaciones en la capa altura de la mezcla por efecto radiativo o

fenómenos de intercambio turbulento causados por la orografía.

Para la modelación de calidad del aire, se han seguido los procedimientos establecidos por

la “Guía metodológica de uso de modelos de dispersión en el SEIA” (SEA, 2023), la cual

recomienda el uso de CALPUFF como uno de los modelos de dispersión de contaminantes.

Para propósitos particulares de este estudio, se ha utilizado la versión 7. CALPUFF es un

Página 47 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

modelo lagrangiano de dispersión de contaminantes basado en un sistema de “puffs”, los

cuales varían en su forma y posición en función del tiempo, del espacio, la estabilidad

atmosférica y los vientos, entre otros parámetros. Es un modelo que soporta múltiples tipos

de fuentes con diferentes tipos de tratamiento para cada una de ellas: Fuentes de área,

fuentes de volumen, fuentes puntuales y fuentes de línea [4] . En la Tabla 3-2, se presenta la

configuración del dominio utilizado para la modelación de dispersión de realizada con

CALPUFF, el que utiliza como insumo la modelación realizada con WRF, incrementando el

nivel de detalle a una grilla de 300x300 metros de resolución espacial.

Tabla 3-2. Configuración del modelo CALPUFF.

|Parámetro|Configuración|
|---|---|
|Centro UTM E (m) WGS-84|271.747 m UTM WGS-84 19S|
|Centro UTM N (m) WGS-94|6.182.045 m UTM WGS-84 19S|
|Resolución espacial (m)|300|
|Puntos en X|100|
|Puntos en Y|100|
|Topografía|SRTM1 (Aproximadamente 30 metros de resolución)|
|Uso de suelo|GLCC (USGS30 aproximadamente a 1 Kilómetro e resolución)|

Se ha definido el año de modelación como 2022, puesto que es el año que representa de

manera más reciente el estado actual de la atmósfera. En la Figura 3-1, Figura 3-2 y Figura

3-3, se presentan detalles del dominio considerado en la modelación.

4 A User’s Guide for the CALPUFF Dispersion Model (Version 5), Earth Tech Inc.

Página 48 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 3-1. Dominio y resolución para la modelación de dispersión.

Página 49 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 3-2. Topografía utilizada (SRTM1 a 30 metros de resolución).

Página 50 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 3-3. Dominio de modelación y los distintos usos de suelo considerados (GLCC a 1 Km de resolución).

Página 51 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Tabla 3-3. Tipos de uso de suelos y parámetros considerados por CALPUFF, parámetros por defecto.

|Categorí<br>a<br>CALPUFF|Categorí<br>a GLCC|Rugosida<br>d|Albedo|Bowen|Flujo de<br>calor<br>natural|Flujo de calor<br>antropogénic<br>o|Área<br>foliar|Descripción|
|---|---|---|---|---|---|---|---|---|
|20|21|0.25|0.15|1|0.15|0|3|Cultivo o Pastoreo|
|20|22|0.25|0.15|1|0.15|0|3|Huertos, Arboledas,<br>Viñedos, Viveros|
|20|23|0.25|0.15|1|0.15|0|3|Operaciones de<br>alimentación<br>confinada|
|20|24|0.25|0.15|1|0.15|0|3|Agricultura|
|30|31|0.05|0.25|1|0.15|0|0.5|Pastizales<br>herbáceos|
|30|32|0.05|0.25|1|0.15|0|0.5|Pastizales de<br>arbustos y<br>matorrales|
|30|33|0.05|0.25|1|0.15|0|0.5|Pastizales mixtos|
|40|41|1|0.1|1|0.15|0|7|Tierra de bosque<br>caducifolio|
|40|42|1|0.1|1|0.15|0|7|Tierra de bosque<br>siempre verde|
|40|43|1|0.1|1|0.15|0|7|Tierra forestal<br>mixta|
|51|53|0.001|0.1|0|0|0|0|Reservorios|

Página 52 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

## 4. Análisis de incertidumbre

Para el análisis de incertidumbre, se utilizó la estación más con información pública

disponible que corresponde a la estación Nilahue-La Quebrada. Las variables para analizar

corresponden a la Magnitud y Dirección del viento, puesto que esta combinación de variables

incide el transporte y dispersión de contaminantes. Se extrajo desde el dominio de

modelación, el punto de grilla correspondiente a la posición de la estación, de manera de

analizar la incertidumbre de los datos modelados versus los datos observados.

En cuanto a la comparación cualitativa de variables, en la Figura 4-1, se presenta el ciclo

diario de la velocidad del viento observada y modelada, se puede ver que el ciclo es

capturado de manera adecuada por parte del modelo. Sin embargo, en términos de

promedios se puede ver que el modelo tiende a sobreestimar las velocidades del viento. En

cuanto a la dirección del viento, se puede ver que el modelo representa los tres ejes de

transporte con una deviación de 22.5° en sentido antihorario en el eje de la componente del

oeste, presentando, por parte del modelo, una componente predominante del oeste

suroeste (OSO).

Página 53 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 4-1. Comparación de ciclo diario de velocidad observada y modelada.

En la Figura 4-2, se observa el ciclo anual de la velocidad del viento observada y modelada,

se puede ver cómo el modelo captura de manera adecuada el comportamiento intra anual

de esta variable, con una sobreestimación de las velocidades durante el mes de julio.

Página 54 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 4-2. Comparación de ciclo anual de velocidad observada y modelada.

En la Figura 4-3 se presenta una comparación de la dirección del viento observado y

modelado, el modelo logra representar el eje de transporte, proveniente desde el cuadrante

sursuroeste, con una desviación de 22,5° en sentido antihorario en la componente del Oeste.

Página 55 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 4-3. Comparación de dirección del viento observada y modelada.

En la Figura 4-4 se observa una comparación de las velocidades de viento. Se puede ver que,

en promedio, el modelo sobrestima la velocidad del viento en verano con un valor promedio

de 1,5 m/s y con una sobrestimación máxima en primavera de 1,6 m/s.

Figura 4-4. Comparación de velocidades de viento observada y modelada.

Página 56 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Datos de velocidad (m/s) 2022 Nilahue-La Quebrada<br>Verano Otoño Invierno Primavera<br>2022 ene feb mar abr may jun jul ago sept oct nov dic<br>0 0.4 0.3 0.5 0.6 0.7 0.6 0.6 0.6 0.3 0.6 0.3 0.4<br>1 0.4 0.5 0.6 0.5 0.7 0.5 0.7 0.6 0.2 0.8 0.3 0.6 Magrugada<br>2 0.4 0.4 0.7 0.6 0.7 0.5 0.6 0.5 0.3 0.8 0.2 0.6<br>3 0.4 0.3 0.8 0.5 0.7 0.5 0.6 0.4 0.2 0.8 0.2 0.6<br>4 0.5 0.4 0.7 0.5 0.6 0.6 0.6 0.4 0.3 0.9 0.2 0.6<br>5 0.4 0.4 0.8 0.6 0.5 0.6 0.6 0.5 0.3 0.9 0.2 0.6<br>6 0.5 0.4 0.8 0.6 0.5 0.6 0.5 0.5 0.3 0.9 0.2 0.7<br>7 0.7 0.4 0.7 0.6 0.5 0.6 0.6 0.5 0.4 1 0.3 1.2<br>Mañana<br>8 1.2 0.9 1.2 0.8 0.6 0.6 0.7 0.5 0.6 1.8 0.4 1.6<br>9 1.5 1.2 2 1.3 1 0.6 0.7 1.1 1.2 2.2 0.5 1.9<br>10 1.7 1.6 2.2 1.7 1.3 0.8 0.8 1.6 1.6 2.4 0.6 2.1<br>11 1.9 1.8 2.3 2 1.5 1.1 1 2 1.9 2.5 0.8 2.3<br>12 2.2 2.2 2.4 2.1 1.5 1.1 1.2 2.3 2 2.8 1.1 2.7<br>13 2.9 2.9 2.8 2.3 1.8 1.3 1.6 2.4 2.4 3.1 1.4 3.3<br>14 3.4 3.4 3.1 2.8 1.8 1.3 1.7 2.5 2.6 3.7 1.4 3.5 Tarde<br>15 3.5 3.6 3.1 2.8 2.1 1.3 1.7 2.5 2.5 3.5 1.5 3.4<br>16 3.3 3.1 3 2.6 2.2 1.4 1.9 2.5 2.5 3.4 1.4 2.9<br>17 2.9 2.7 2.4 2 1.5 1.1 1.4 1.9 2 2.7 1.3 2.6<br>18 2.3 2.2 1.7 1.1 0.9 0.9 0.9 1 1.1 1.9 1 2<br>19 1.5 1.3 1.2 0.7 0.8 0.8 0.8 0.7 0.5 1 0.7 1.4<br>20 0.9 0.8 0.9 0.5 0.7 0.6 0.8 0.5 0.5 0.7 0.5 0.8 Noche<br>21 0.6 0.5 0.8 0.5 0.6 0.6 0.7 0.5 0.4 0.6 0.4 0.3<br>22 0.4 0.3 0.6 0.6 0.6 0.6 0.6 0.5 0.4 0.6 0.3 0.2<br>23 0.4 0.3 0.5 0.6 0.7 0.6 0.5 0.6 0.3 0.6 0.3 0.3<br>x ̄mensual 1.4 1.3 1.5 1.2 1 0.8 0.9 1.1 1 1.7 0.6 1.5|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2022**<br>**ene**<br>**feb**<br>**mar**<br>**abr**<br>**may**<br>**jun**<br>**jul**<br>**ago**<br>**sept**<br>**oct**<br>**nov**<br>**dic**<br>**0**<br>0.4<br>0.3<br>0.5<br>0.6<br>0.7<br>0.6<br>0.6<br>0.6<br>0.3<br>0.6<br>0.3<br>0.4<br>**1**<br>0.4<br>0.5<br>0.6<br>0.5<br>0.7<br>0.5<br>0.7<br>0.6<br>0.2<br>0.8<br>0.3<br>0.6<br>**2**<br>0.4<br>0.4<br>0.7<br>0.6<br>0.7<br>0.5<br>0.6<br>0.5<br>0.3<br>0.8<br>0.2<br>0.6<br>**3**<br>0.4<br>0.3<br>0.8<br>0.5<br>0.7<br>0.5<br>0.6<br>0.4<br>0.2<br>0.8<br>0.2<br>0.6<br>**4**<br>0.5<br>0.4<br>0.7<br>0.5<br>0.6<br>0.6<br>0.6<br>0.4<br>0.3<br>0.9<br>0.2<br>0.6<br>**5**<br>0.4<br>0.4<br>0.8<br>0.6<br>0.5<br>0.6<br>0.6<br>0.5<br>0.3<br>0.9<br>0.2<br>0.6<br>**6**<br>0.5<br>0.4<br>0.8<br>0.6<br>0.5<br>0.6<br>0.5<br>0.5<br>0.3<br>0.9<br>0.2<br>0.7<br>**7**<br>0.7<br>0.4<br>0.7<br>0.6<br>0.5<br>0.6<br>0.6<br>0.5<br>0.4<br>1<br>0.3<br>1.2<br>**8**<br>1.2<br>0.9<br>1.2<br>0.8<br>0.6<br>0.6<br>0.7<br>0.5<br>0.6<br>1.8<br>0.4<br>1.6<br>**9**<br>1.5<br>1.2<br>2<br>1.3<br>1<br>0.6<br>0.7<br>1.1<br>1.2<br>2.2<br>0.5<br>1.9<br>**10**<br>1.7<br>1.6<br>2.2<br>1.7<br>1.3<br>0.8<br>0.8<br>1.6<br>1.6<br>2.4<br>0.6<br>2.1<br>**11**<br>1.9<br>1.8<br>2.3<br>2<br>1.5<br>1.1<br>1<br>2<br>1.9<br>2.5<br>0.8<br>2.3<br>**12**<br>2.2<br>2.2<br>2.4<br>2.1<br>1.5<br>1.1<br>1.2<br>2.3<br>2<br>2.8<br>1.1<br>2.7<br>**13**<br>2.9<br>2.9<br>2.8<br>2.3<br>1.8<br>1.3<br>1.6<br>2.4<br>2.4<br>3.1<br>1.4<br>3.3<br>**14**<br>3.4<br>3.4<br>3.1<br>2.8<br>1.8<br>1.3<br>1.7<br>2.5<br>2.6<br>3.7<br>1.4<br>3.5<br>**15**<br>3.5<br>3.6<br>3.1<br>2.8<br>2.1<br>1.3<br>1.7<br>2.5<br>2.5<br>3.5<br>1.5<br>3.4<br>**16**<br>3.3<br>3.1<br>3<br>2.6<br>2.2<br>1.4<br>1.9<br>2.5<br>2.5<br>3.4<br>1.4<br>2.9<br>**17**<br>2.9<br>2.7<br>2.4<br>2<br>1.5<br>1.1<br>1.4<br>1.9<br>2<br>2.7<br>1.3<br>2.6<br>**18**<br>2.3<br>2.2<br>1.7<br>1.1<br>0.9<br>0.9<br>0.9<br>1<br>1.1<br>1.9<br>1<br>2<br>**19**<br>1.5<br>1.3<br>1.2<br>0.7<br>0.8<br>0.8<br>0.8<br>0.7<br>0.5<br>1<br>0.7<br>1.4<br>**20**<br>0.9<br>0.8<br>0.9<br>0.5<br>0.7<br>0.6<br>0.8<br>0.5<br>0.5<br>0.7<br>0.5<br>0.8<br>**21**<br>0.6<br>0.5<br>0.8<br>0.5<br>0.6<br>0.6<br>0.7<br>0.5<br>0.4<br>0.6<br>0.4<br>0.3<br>**22**<br>0.4<br>0.3<br>0.6<br>0.6<br>0.6<br>0.6<br>0.6<br>0.5<br>0.4<br>0.6<br>0.3<br>0.2<br>**23**<br>0.4<br>0.3<br>0.5<br>0.6<br>0.7<br>0.6<br>0.5<br>0.6<br>0.3<br>0.6<br>0.3<br>0.3<br>**1.4**<br>**1.3**<br>**1.5**<br>**1.2**<br>**1**<br>**0.8**<br>**0.9**<br>**1.1**<br>**1**<br>**1.7**<br>**0.6**<br>**1.5**<br>**Magrugada**<br>**Mañana**<br>**Tarde**<br>**Noche**<br>Datos de velocidad (m/s) 2022 Nilahue-La Quebrada<br>**Verano**<br>**Otoño**<br>**Invierno**<br>**Primavera**<br>**x mensual**|**16**|3.3|3.1|3|2.6|2.2|1.4|1.9|2.5|2.5|3.4|1.4|2.9|
|**2022**<br>**ene**<br>**feb**<br>**mar**<br>**abr**<br>**may**<br>**jun**<br>**jul**<br>**ago**<br>**sept**<br>**oct**<br>**nov**<br>**dic**<br>**0**<br>0.4<br>0.3<br>0.5<br>0.6<br>0.7<br>0.6<br>0.6<br>0.6<br>0.3<br>0.6<br>0.3<br>0.4<br>**1**<br>0.4<br>0.5<br>0.6<br>0.5<br>0.7<br>0.5<br>0.7<br>0.6<br>0.2<br>0.8<br>0.3<br>0.6<br>**2**<br>0.4<br>0.4<br>0.7<br>0.6<br>0.7<br>0.5<br>0.6<br>0.5<br>0.3<br>0.8<br>0.2<br>0.6<br>**3**<br>0.4<br>0.3<br>0.8<br>0.5<br>0.7<br>0.5<br>0.6<br>0.4<br>0.2<br>0.8<br>0.2<br>0.6<br>**4**<br>0.5<br>0.4<br>0.7<br>0.5<br>0.6<br>0.6<br>0.6<br>0.4<br>0.3<br>0.9<br>0.2<br>0.6<br>**5**<br>0.4<br>0.4<br>0.8<br>0.6<br>0.5<br>0.6<br>0.6<br>0.5<br>0.3<br>0.9<br>0.2<br>0.6<br>**6**<br>0.5<br>0.4<br>0.8<br>0.6<br>0.5<br>0.6<br>0.5<br>0.5<br>0.3<br>0.9<br>0.2<br>0.7<br>**7**<br>0.7<br>0.4<br>0.7<br>0.6<br>0.5<br>0.6<br>0.6<br>0.5<br>0.4<br>1<br>0.3<br>1.2<br>**8**<br>1.2<br>0.9<br>1.2<br>0.8<br>0.6<br>0.6<br>0.7<br>0.5<br>0.6<br>1.8<br>0.4<br>1.6<br>**9**<br>1.5<br>1.2<br>2<br>1.3<br>1<br>0.6<br>0.7<br>1.1<br>1.2<br>2.2<br>0.5<br>1.9<br>**10**<br>1.7<br>1.6<br>2.2<br>1.7<br>1.3<br>0.8<br>0.8<br>1.6<br>1.6<br>2.4<br>0.6<br>2.1<br>**11**<br>1.9<br>1.8<br>2.3<br>2<br>1.5<br>1.1<br>1<br>2<br>1.9<br>2.5<br>0.8<br>2.3<br>**12**<br>2.2<br>2.2<br>2.4<br>2.1<br>1.5<br>1.1<br>1.2<br>2.3<br>2<br>2.8<br>1.1<br>2.7<br>**13**<br>2.9<br>2.9<br>2.8<br>2.3<br>1.8<br>1.3<br>1.6<br>2.4<br>2.4<br>3.1<br>1.4<br>3.3<br>**14**<br>3.4<br>3.4<br>3.1<br>2.8<br>1.8<br>1.3<br>1.7<br>2.5<br>2.6<br>3.7<br>1.4<br>3.5<br>**15**<br>3.5<br>3.6<br>3.1<br>2.8<br>2.1<br>1.3<br>1.7<br>2.5<br>2.5<br>3.5<br>1.5<br>3.4<br>**16**<br>3.3<br>3.1<br>3<br>2.6<br>2.2<br>1.4<br>1.9<br>2.5<br>2.5<br>3.4<br>1.4<br>2.9<br>**17**<br>2.9<br>2.7<br>2.4<br>2<br>1.5<br>1.1<br>1.4<br>1.9<br>2<br>2.7<br>1.3<br>2.6<br>**18**<br>2.3<br>2.2<br>1.7<br>1.1<br>0.9<br>0.9<br>0.9<br>1<br>1.1<br>1.9<br>1<br>2<br>**19**<br>1.5<br>1.3<br>1.2<br>0.7<br>0.8<br>0.8<br>0.8<br>0.7<br>0.5<br>1<br>0.7<br>1.4<br>**20**<br>0.9<br>0.8<br>0.9<br>0.5<br>0.7<br>0.6<br>0.8<br>0.5<br>0.5<br>0.7<br>0.5<br>0.8<br>**21**<br>0.6<br>0.5<br>0.8<br>0.5<br>0.6<br>0.6<br>0.7<br>0.5<br>0.4<br>0.6<br>0.4<br>0.3<br>**22**<br>0.4<br>0.3<br>0.6<br>0.6<br>0.6<br>0.6<br>0.6<br>0.5<br>0.4<br>0.6<br>0.3<br>0.2<br>**23**<br>0.4<br>0.3<br>0.5<br>0.6<br>0.7<br>0.6<br>0.5<br>0.6<br>0.3<br>0.6<br>0.3<br>0.3<br>**1.4**<br>**1.3**<br>**1.5**<br>**1.2**<br>**1**<br>**0.8**<br>**0.9**<br>**1.1**<br>**1**<br>**1.7**<br>**0.6**<br>**1.5**<br>**Magrugada**<br>**Mañana**<br>**Tarde**<br>**Noche**<br>Datos de velocidad (m/s) 2022 Nilahue-La Quebrada<br>**Verano**<br>**Otoño**<br>**Invierno**<br>**Primavera**<br>**x mensual**|**17**<br>**18**<br>**19**<br>**20**<br>**21**<br>**22**|2.9<br>2.3<br>1.5<br>0.9<br>0.6<br>0.4|2.7<br>2.2<br>1.3<br>0.8<br>0.5<br>0.3|2.4<br>1.7<br>1.2<br>0.9<br>0.8<br>0.6|2<br>1.1<br>0.7<br>0.5<br>0.5<br>0.6|1.5<br>0.9<br>0.8<br>0.7<br>0.6<br>0.6|1.1<br>0.9<br>0.8<br>0.6<br>0.6<br>0.6|1.4<br>0.9<br>0.8<br>0.8<br>0.7<br>0.6|1.9<br>1<br>0.7<br>0.5<br>0.5<br>0.5|2<br>1.1<br>0.5<br>0.5<br>0.4<br>0.4|2.7<br>1.9<br>1<br>0.7<br>0.6<br>0.6|1.3<br>1<br>0.7<br>0.5<br>0.4<br>0.3|2.6<br>2<br>1.4<br>0.8<br>0.3<br>0.2|
|**2022**<br>**ene**<br>**feb**<br>**mar**<br>**abr**<br>**may**<br>**jun**<br>**jul**<br>**ago**<br>**sept**<br>**oct**<br>**nov**<br>**dic**<br>**0**<br>0.4<br>0.3<br>0.5<br>0.6<br>0.7<br>0.6<br>0.6<br>0.6<br>0.3<br>0.6<br>0.3<br>0.4<br>**1**<br>0.4<br>0.5<br>0.6<br>0.5<br>0.7<br>0.5<br>0.7<br>0.6<br>0.2<br>0.8<br>0.3<br>0.6<br>**2**<br>0.4<br>0.4<br>0.7<br>0.6<br>0.7<br>0.5<br>0.6<br>0.5<br>0.3<br>0.8<br>0.2<br>0.6<br>**3**<br>0.4<br>0.3<br>0.8<br>0.5<br>0.7<br>0.5<br>0.6<br>0.4<br>0.2<br>0.8<br>0.2<br>0.6<br>**4**<br>0.5<br>0.4<br>0.7<br>0.5<br>0.6<br>0.6<br>0.6<br>0.4<br>0.3<br>0.9<br>0.2<br>0.6<br>**5**<br>0.4<br>0.4<br>0.8<br>0.6<br>0.5<br>0.6<br>0.6<br>0.5<br>0.3<br>0.9<br>0.2<br>0.6<br>**6**<br>0.5<br>0.4<br>0.8<br>0.6<br>0.5<br>0.6<br>0.5<br>0.5<br>0.3<br>0.9<br>0.2<br>0.7<br>**7**<br>0.7<br>0.4<br>0.7<br>0.6<br>0.5<br>0.6<br>0.6<br>0.5<br>0.4<br>1<br>0.3<br>1.2<br>**8**<br>1.2<br>0.9<br>1.2<br>0.8<br>0.6<br>0.6<br>0.7<br>0.5<br>0.6<br>1.8<br>0.4<br>1.6<br>**9**<br>1.5<br>1.2<br>2<br>1.3<br>1<br>0.6<br>0.7<br>1.1<br>1.2<br>2.2<br>0.5<br>1.9<br>**10**<br>1.7<br>1.6<br>2.2<br>1.7<br>1.3<br>0.8<br>0.8<br>1.6<br>1.6<br>2.4<br>0.6<br>2.1<br>**11**<br>1.9<br>1.8<br>2.3<br>2<br>1.5<br>1.1<br>1<br>2<br>1.9<br>2.5<br>0.8<br>2.3<br>**12**<br>2.2<br>2.2<br>2.4<br>2.1<br>1.5<br>1.1<br>1.2<br>2.3<br>2<br>2.8<br>1.1<br>2.7<br>**13**<br>2.9<br>2.9<br>2.8<br>2.3<br>1.8<br>1.3<br>1.6<br>2.4<br>2.4<br>3.1<br>1.4<br>3.3<br>**14**<br>3.4<br>3.4<br>3.1<br>2.8<br>1.8<br>1.3<br>1.7<br>2.5<br>2.6<br>3.7<br>1.4<br>3.5<br>**15**<br>3.5<br>3.6<br>3.1<br>2.8<br>2.1<br>1.3<br>1.7<br>2.5<br>2.5<br>3.5<br>1.5<br>3.4<br>**16**<br>3.3<br>3.1<br>3<br>2.6<br>2.2<br>1.4<br>1.9<br>2.5<br>2.5<br>3.4<br>1.4<br>2.9<br>**17**<br>2.9<br>2.7<br>2.4<br>2<br>1.5<br>1.1<br>1.4<br>1.9<br>2<br>2.7<br>1.3<br>2.6<br>**18**<br>2.3<br>2.2<br>1.7<br>1.1<br>0.9<br>0.9<br>0.9<br>1<br>1.1<br>1.9<br>1<br>2<br>**19**<br>1.5<br>1.3<br>1.2<br>0.7<br>0.8<br>0.8<br>0.8<br>0.7<br>0.5<br>1<br>0.7<br>1.4<br>**20**<br>0.9<br>0.8<br>0.9<br>0.5<br>0.7<br>0.6<br>0.8<br>0.5<br>0.5<br>0.7<br>0.5<br>0.8<br>**21**<br>0.6<br>0.5<br>0.8<br>0.5<br>0.6<br>0.6<br>0.7<br>0.5<br>0.4<br>0.6<br>0.4<br>0.3<br>**22**<br>0.4<br>0.3<br>0.6<br>0.6<br>0.6<br>0.6<br>0.6<br>0.5<br>0.4<br>0.6<br>0.3<br>0.2<br>**23**<br>0.4<br>0.3<br>0.5<br>0.6<br>0.7<br>0.6<br>0.5<br>0.6<br>0.3<br>0.6<br>0.3<br>0.3<br>**1.4**<br>**1.3**<br>**1.5**<br>**1.2**<br>**1**<br>**0.8**<br>**0.9**<br>**1.1**<br>**1**<br>**1.7**<br>**0.6**<br>**1.5**<br>**Magrugada**<br>**Mañana**<br>**Tarde**<br>**Noche**<br>Datos de velocidad (m/s) 2022 Nilahue-La Quebrada<br>**Verano**<br>**Otoño**<br>**Invierno**<br>**Primavera**<br>**x mensual**|**17**<br>**18**<br>**19**<br>**20**<br>**21**<br>**22**|0.4<br>**1.4**|0.3<br>**1.3**|0.5<br>**1.5**|0.6<br>**1.2**|0.7<br>**1**|0.6<br>**0.8**|0.5<br>**0.9**|0.6<br>**1.1**|0.3<br>**1**|0.6<br>**1.7**|0.3<br>**0.6**|0.3<br>**1.5**|
|**x estacional**<br>**x anual**|**x estacional**<br>**x anual**|**1.4**<br>**1**<br>**1**<br>**1.3**<br>**1.2**|**1.4**<br>**1**<br>**1**<br>**1.3**<br>**1.2**|**1.4**<br>**1**<br>**1**<br>**1.3**<br>**1.2**|**1.4**<br>**1**<br>**1**<br>**1.3**<br>**1.2**|**1.4**<br>**1**<br>**1**<br>**1.3**<br>**1.2**|**1.4**<br>**1**<br>**1**<br>**1.3**<br>**1.2**|**1.4**<br>**1**<br>**1**<br>**1.3**<br>**1.2**|**1.4**<br>**1**<br>**1**<br>**1.3**<br>**1.2**|**1.4**<br>**1**<br>**1**<br>**1.3**<br>**1.2**|**1.4**<br>**1**<br>**1**<br>**1.3**<br>**1.2**|**1.4**<br>**1**<br>**1**<br>**1.3**<br>**1.2**|**1.4**<br>**1**<br>**1**<br>**1.3**<br>**1.2**|

|Datos de velocidad (m/s) 2022 Modelo|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2022**|**2022**|**Verano**|**Verano**|**Verano**|**Otoño**|**Otoño**|**Otoño**|**Invierno**|**Invierno**|**Invierno**|**Primavera**|**Primavera**|**Primavera**|
|**2022**|**2022**|**ene**|**feb**|**mar**|**abr**|**may**|**jun**|**jul**|**ago**|**sept**|**oct**|**nov**|**dic**|
|**Magrugada**|**0**|1.3|1.2|1.6|1.9|2.1|2.6|2.9|2.1|1.6|2.1|1.9|1.6|
|**Magrugada**|**1**|1.2|0.9|1.6|2.2|2.1|2.5|2.9|2|1.6|1.9|1.9|1.7|
|**Magrugada**|**2**|1.2|1|1.6|2.2|1.9|2.4|2.9|2.3|1.7|2|1.9|1.7|
|**Magrugada**|**3**|1.2|1.1|1.7|2.1|1.9|2.5|2.9|2.5|1.7|2|1.8|1.7|
|**Magrugada**|**4**|1.2|1.2|1.8|2.3|1.9|2.5|2.9|2.6|1.8|2|1.7|1.8|
|**Magrugada**|**5**|1.2|1.2|1.9|2.3|2|2.6|2.9|2.6|1.8|2|1.8|1.8|
|**Mañana**|**6**|1.1|1.3|1.9|2.5|2.2|2.5|3|2.5|1.8|1.8|1.6|1.3|
|**Mañana**|**7**|1.4|1.3|1.7|2.1|2.1|2.3|3.1|2.5|1.6|2|2|2.2|
|**Mañana**|**8**|1.9|2|2.2|2.1|1.7|2.2|3|2.3|1.9|2.5|2.3|2.5|
|**Mañana**|**9**|2.3|2.1|2.8|2.6|1.8|2.4|2.7|2.7|2.3|2.7|2.5|2.9|
|**Mañana**|**10**|2.9|2.5|3.1|2.8|2.1|2.5|3.4|3.1|2.4|2.9|3|3.4|
|**Mañana**|**11**|3.6|3.4|3.2|3.2|2.1|2.8|3.5|3.2|2.6|3.3|3.7|4.3|
|**Tarde**|**12**|4.7|4.7|4|3.6|2.3|2.9|3.4|3|2.9|3.8|4.7|5|
|**Tarde**|**13**|5.6|5.5|4.8|4.2|2.6|3.1|3.5|3.3|3.3|4.5|5.1|5.6|
|**Tarde**|**14**|5.9|5.9|5.3|4.5|2.8|3|3.6|3.6|3.7|5|5.4|5.9|
|**Tarde**|**15**|5.8|5.7|5.4|4.4|3.1|3|3.4|3.4|3.9|5|5.4|5.7|
|**Tarde**|**16**|5.4|5.2|5.1|4.2|2.9|2.8|3|3.2|3.9|4.8|5.1|5.3|
|**Tarde**|**17**|4.8|4.4|4.2|3.4|2.3|2.6|3.1|2.8|3.3|4.2|4.4|4.6|
|**Noche**|**18**|3.9|3.5|3.1|2.6|1.8|2.2|2.7|2.2|2.5|3|3.2|3.5|
|**Noche**|**19**|2.7|2.4|2.5|2.1|1.7|2.4|2.7|2|1.9|2.3|2.1|2.5|
|**Noche**|**20**|2.2|1.9|1.9|2|1.7|2.4|2.9|2|1.8|2.1|2|2.2|
|**Noche**|**21**|1.7|1.6|1.7|2|1.7|2.4|2.6|2.1|1.7|2|2|1.8|
|**Noche**|**22**|1.6|1.6|1.9|1.9|1.8|2.6|2.6|2|1.7|2.1|2.1|1.8|
|**Noche**|**23**|1.4|1.4|1.7|1.9|2|2.6|2.7|2.1|1.6|2.1|2.1|1.7|
|**x mensual**|**x mensual**|**2.8**|**2.6**|**2.8**|**2.7**|**2.1**|**2.6**|**3**|**2.6**|**2.3**|**2.8**|**2.9**|**3**|
|**x estacional**|**x estacional**|**2.7**|**2.7**|**2.7**|**2.5**|**2.5**|**2.5**|**2.6**|**2.6**|**2.6**|**2.9**|**2.9**|**2.9**|
|**x anual**|**x anual**|**2.7**|**2.7**|**2.7**|**2.7**|**2.7**|**2.7**|**2.7**|**2.7**|**2.7**|**2.7**|**2.7**|**2.7**|

Respecto a la variable Temperatura, a continuación, se presenta una comparación entre lo

modelado y lo observado para el punto donde se encuentra emplazada la estación Nilahue

Página 57 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

La Quebrada. Tal como se puede ver en la Figura 4-5 y Figura 4-6, la representación de esta

variable concuerda con lo monitoreado en dicha estación.

Figura 4-5 Comparación de ciclo diario de temperatura observada y modelada.

Página 58 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 4-6. Comparación de ciclo anual de temperatura observada y modelada.

Página 59 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

### 4.1 Comparación cuantitativa de variables

En la Tabla 4-1, se puede ver los estadísticos que comparan el desempeño del modelo para

las variables de Velocidad del viento y Temperatura. Se puede ver que en general los rangos

están dentro de las métricas recomendables de análisis de incertidumbre.

Tabla 4-1. Comparación cuantitativa de variables.

|Estadístico|Velocidad del viento|Temperatura|
|---|---|---|
|BIAS|-1,336|-0,522|
|MAE|1,428|2,800|
|RMSE|1,212|2,353|
|Coeficiente de correlación (r)|0,637|0,893|

Página 60 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

## 5. Fuentes consideradas y receptores discretos definidos

### 5.1 Fuentes consideradas

Para el presente proyecto se consideraron las fuentes de emisión descritas en la Tabla 5-1 y

mostrada en la Figura 5-1 . En las siguientes páginas se hará una completa descripción de las

fuentes (punto 3.3 de la “Guía”) y las características de sus emisiones (punto 2.3.1 de la

“Guía”) [ 5] .

Tabla 5-1. Fuentes de olor del Proyecto.

|ID|Fuente|Estado|Código SRC|Tipo de<br>Fuente|Principales factores<br>operacionales que<br>influyen en la emisión de<br>olor|Régimen de<br>Funcionamient<br>o|
|---|---|---|---|---|---|---|
|1|Cámara de<br>Rejas|Existente|SRC_1|Puntual|Exposición al ambiente<br>por recepción e<br>impulsión de aguas<br>servidas.|24 horas, 7 días<br>a la semana,<br>365 días al año|
|2|PEAS|Proyectada|SRC_2|Puntual|Exposición puntual al<br>ambiente por ingreso y<br>elevación de aguas<br>servidas a tratamiento.|24 horas, 7 días<br>a la semana,<br>365 días al año|
|3|Cámara de<br>Entrada|Proyectada|SRC_3|Puntual|Exposición al ambiente<br>por acumulación y<br>circulación de aguas<br>servidas.|24 horas, 7 días<br>a la semana,<br>365 días al año|
|4|Pretratamiento|Proyectada|SRC_4|Difusa|Exposición al ambiente<br>por acumulación y<br>tratamiento preliminar<br>de aguas servidas.|24 horas, 7 días<br>a la semana,<br>365 días al año|
|5|Contenedores<br>de Sólidos 1|Proyectada|SRC_5|Puntual|Exposición puntual al<br>ambiente<br>por acumulación de<br>residuos orgánicos.|24 horas, 7 días<br>a la semana,<br>365 días al año|
|6|Contenedores<br>de Sólidos 2|Proyectada|SRC_6|Puntual|Puntual|24 horas, 7 días<br>a la semana,<br>365 días al año|
|7|Laguna de<br>Aireación|Proyectada|SRC_7|Superficial<br>Activa|Exposición al ambiente<br>por acumulación y<br>aireación y presencia de<br>sobrenadantes de aguas<br>servidas.|24 horas, 7 días<br>a la semana,<br>365 días al año|
|8|Laguna<br>Parcialmente 1|Proyectada|SRC_8|Superficial<br>Pasiva|Exposición al ambiente<br>por acumulación y<br>aireación de aguas<br>servidas.|24 horas, 7 días<br>a la semana,<br>365 días al año|
|9|Laguna<br>Parcialmente 2|Proyectada|SRC_9|Superficial<br>Pasiva|Exposición al ambiente<br>por acumulación y<br>aireación de aguas<br>servidas.|24 horas, 7 días<br>a la semana,<br>365 días al año|

5 Guía para la predicción y evaluación de impactos por olor en el SEIA, Servicio de Evaluación Ambiental (SEA), 2017. Chile.

Página 61 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|ID|Fuente|Estado|Código SRC|Tipo de<br>Fuente|Principales factores<br>operacionales que<br>influyen en la emisión de<br>olor|Régimen de<br>Funcionamient<br>o|
|---|---|---|---|---|---|---|
|1<br>0|Laguna<br>Parcialmente 3|Proyectada|SRC_10|Superficial<br>Pasiva|Exposición al ambiente<br>por acumulación y<br>sedimentación de aguas<br>servidas.|24 horas, 7 días<br>a la semana,<br>365 días al año|
|1<br>1|Planta<br>Elevadora de<br>Retornos|Proyectada|SRC_11|Superficial<br>Pasiva|Exposición al ambiente<br>conducción de aguas<br>servidas.|24 horas, 7 días<br>a la semana,<br>365 días al año|
|1<br>2|Cámara de<br>Contacto<br>Ampliada|Proyectada|SRC_12|Superficial<br>Pasiva|Exposición al ambiente<br>por acumulación y<br>circulación de aguas<br>tratadas.|24 horas, 7 días<br>a la semana,<br>365 días al año|
|1<br>3|Lecho de<br>Secado|Proyectada|SRC_13|Superficial<br>Pasiva|Exposición al ambiente<br>por acumulación de<br>lodos en secado.|24 horas, 7 días<br>a la semana,<br>365 días al año|

Figura 5-1. Ubicación de fuentes consideradas.

Página 62 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Las fuentes fueron seleccionadas mediante una visita a terreno por parte de panelistas

expertos en monitoreo de olores. Estas fuentes representan los principales puntos de

emisión de olor dentro del proceso de tratamiento de agua servidas.

Para la presente modelación se utilizaron datos obtenidos mediante una campaña de

medición de olfatometría Dinámica, llevada a cabo por la empresa GCA Ambiental, el día 08

de Octubre de 2024, en conformidad a la normativa correspondiente:

 - La toma de muestra se realizó en función de la Guía Metodológica 3386:2015 [6 ]

 - El análisis de las muestras se realizó según NCh 3190:2010 [7 ]

 - Las normas mencionadas anteriormente dan cuenta de la metodología y

procedimientos adecuados para la toma de muestra y la determinación de su

concentración.

El Proyecto contempla la ampliación de la PTAS de Peralillo. Para la realización del inventario

de emisiones de olor se utilizaron los obtenidos de análisis de Olfatometría Dinámica para

las fuentes existentes y se utilizó información bibliográfica para la fuente proyectada

Pretratamiento, utilizando como referencia el Estudio de Olor asociado a la Declaración de

Impacto del Proyecto Planta de Tratamiento de Aguas Servidas Buin Poniente, aprobado

favorablemente el año 2021 por el Servicio de Evaluación Ambiental.

El proyecto “Planta de Tratamiento de Aguas Servidas Buin Poniente”, consistía en la

construcción de una planta de aguas servidas en la localidad de Buin, la cual permite

satisfacer las necesidades de 12.000 clientes proyectados al año 2034. La Planta de

Tratamiento consta de las siguientes unidades: Planta elevadora de cabecera,

Pretratamiento (Compuesta por tres equipos compactos que realizan las funciones de

6 Instituto Nacional de Normalización (2015). Norma Chilena 3386:2015 “Muestreo estático para olfatometría”. Chile.

7 Instituto Nacional de Normalización (2010). Norma Chilena 3190:2010 “Calidad del aire - Determinación de la
concentración de olor por olfatometría dinámica”. Chile.

Página 63 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

cribado, desarenado y desgrasado), Tratamiento Biológico (Compuesto por tres líneas, cada

una con un estanque de aireación (o reactor biológico)) y un sedimentador secundario,

Sistema de Desinfección, compuesta por tres cámaras de contacto en las cuales se realizará

la desinfección a través de la adición de cloro, sistema de presurización de agua de servicio

(agua tratada), espesado de lodos (compuesto por tres espesadores gravitacionales

convencionales por lotes, sin limitación de tiempo, con capacidad de almacenar lodo

espesado, permitiendo así la gestión de la operación de deshidratado posterior) y

deshidratado mecánico (batería de tres filtros banda con adición de polímero para alcanzar

una sequedad del 18%).

Las fuentes homologadas son mostradas en la siguiente Tabla.

Tabla 5-2. Homologación de Fuentes.

|ID|Fuente|Se Homologa con la siguiente fuente:|
|---|---|---|
|1|Cámara de Rejas|Fuente Cámara de Entrada (ACTUAL)|
|2|PEAS|Fuente Cámara de Entrada (ACTUAL)|
|4|Pretratamiento|Fuente Cámara de Entrada (ACTUAL)|
|5|Contenedores de Sólidos 1 y 2|Fuente Cámara de Entrada (ACTUAL)|
|8|Laguna Parcialmente 1, 2 y 3|Fuente Laguna de Aireación (ACTUAL)|
|11|Planta Elevadora de Retornos|Fuente Laguna de Aireación (ACTUAL)|
|13|Lecho de Secado|Fuente Cancha de Acopio de Lodos - DIA “Planta de Tratamiento de Aguas<br>Servidas Buin Poniente”.|

En la Tabla 5.-3 se muestra las Dimensiones, Ubicación y Tasas de Emisión de Fuentes

modeladas.

Página 64 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Tabla 5-3. Dimensiones, ubicación y tasas de emisión de fuentes.

|Fuente|Unidades|Tipo de Fuente|Dimensiones|Col5|Área<br>Expuesta<br>(m2)|Concentración<br>de Olor<br>(Uo/m3)|Tasa de<br>Emisión<br>por Área<br>(Uo/s*m2)|Tasa de<br>Emisión<br>Odorante<br>(Uo/s)|Coordenada Central (m)|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|Fuente|Unidades|Tipo de Fuente|Ancho (m) x<br>Largo (m) o<br>Diámetro (m)|Alto (m)|Alto (m)|Alto (m)|Alto (m)|Alto (m)|Este|Norte|
|Cámara de Rejas|1|Puntual|ø = 2,72|Ras del Suelo|3,66|386,00|6,43|37,38|271.749,947|6.182.045,770|
|PEAS|1|Puntual|ø = 2,19|Ras del Suelo|3,29|386,00|6,43|24,23|271.746,870|6.182.050,182|
|Cámara de Entrada|1|Puntual|1,2 x 3,25|Ras del Suelo|3,90|386,00|6,43|25,09|271.529,224|6.181.879,788|
|Pretratamiento|1|Difusa|1,60 x 5,50|2,40|8,80|386,00|6,43|56,58|271.527,229|6.181.872,615|
|Contenedores de Sólidos<br>1|1|Puntual|1,22 x 0,78|2,00|0,95|-|6,43|6,12|271.525,200|6.181.872,718|
|Contenedores de Sólidos<br>2|1|Puntual|1,22 x 0,78|2,00|0,95|-|6,43|6,12|271.526,539|6.181.870,176|
|Laguna de Aireación|1|Superficial Activa|43,00 x 33,00|Ras del Suelo|1.419,00|98,00|0,80|1.135,20|271.564,980|6.181.883,790|
|Laguna Parcialmente 1|1|Superficial Pasiva|28,50 x 16,50|Ras del Suelo|470,25|98,00|0,80|376,20|271.611,400|6.181.915,720|
|Laguna Parcialmente 2|1|Superficial Pasiva|28,50 x 16,50|Ras del Suelo|470,25|98,00|0,80|376,20|271.617,630|6.181.899,930|
|Laguna Parcialmente 3|1|Superficial Pasiva|28,50 x 16,50|Ras del Suelo|507,30|98,00|0,80|405,84|271.635,650|6.181.867,670|
|Planta Elevadora de<br>Retornos|1|Superficial Pasiva|1,0 x 1,10|Ras del Suelo|1,10|98,00|0,80|0,88|271.592,638|6.181.811,719|
|Cámara de Contacto<br>Ampliada|1|Superficial Pasiva|8,20 x 7,82|Ras del Suelo|64,12|85,00|0,70|44,89|271.666,641|6.181.904,831|
|Lecho de Secado|1|Superficial Pasiva|45,00 x 21,90|Ras del Suelo|985,50|-|3,95|3.892,73|271.585,720|6.181.834,070|

Página 65 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

### 5.1 Cálculo de Tasa de Emisión de Olor

La Tasa de Emisión Total de Olor (Uo/s), de las fuentes odorantes, se basa en la cantidad de

unidades de olor europea que pasan a través de una superficie dada por unidad de tiempo

(Uo/s), siendo el producto de la concentración de olor (Uo/m [3] ), la velocidad de salida (m/s)

y el área de emisión (m [2] ).

En otras palabras, el valor de Emisión de Olor por área y la Tasa de Emisión de Olor, se calcula

mediante las siguientes ecuaciones:

[Uo]
EO (m [2]

[Uo]

m [2] s ~~[)]~~ [ = CO(Uo] m [3]

m [3] ~~[)]~~ [ x v (m/s)]

TEO ( [Uo] s

[Uo]
s ~~[)]~~ [ = EO (] m [2]

m [2] s [) x A (m] [2] [)]

Donde:

EO : Emisión de Olor

CO : Concentración de Olor

A : Área de emisión

v : Velocidad de salida de aire oloroso

La Tasa de Emisión Total de Olor (Uo/s), de las fuentes del tipo volumétricas, se calcula

multiplicando la Concentración de Olor (Uo/m [3] ) por el flujo volumétrico (m [3] /s) o, en su

defecto, por la velocidad de salida de la fuente (m/s) y por el área transversal (m [2] ). En el caso

de las fuentes superficiales, para obtener el Tasa de Emisión Total de Olor (Uo/s) se debe

multiplicar la Tasa de Emisión por Área (Uo/m [2] x s) por el área transversal de la fuente (m [2] ).

En la Tabla 13, se muestra la descripción de cada una de las fuentes: Calidad, Tipo de olor,

Intensidad (Tabla 5-4), Tono Hedónico (Tabla 5-5), entre otros. En la

Figura 5-2 se muestra la Descripción de emisiones odorantes de la Planta de Tratamiento.

Página 66 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Tabla 5-4. Escala de Intensidad de Olor.

Tabla 5-5 . Escala Tono Hedónico .

|Número|Intensidad|
|---|---|
|0|Sin Olor|
|1|Muy Suave|
|2|Suave|
|3|Medio|
|4|Fuerte|
|5|Muy Fuerte|
|6|Extremadamente Fuerte|

|Número|Tono Hedónico|
|---|---|
|4|Extremadamente agradable|
|3|Muy agradable|
|2|Agradable|
|1|Levemente agradable|
|0|Neutro|
|-1|Levemente desagradable|
|-2|Desagradable|
|-3|Muy Desagradable|
|-4|Extremadamente Desagradable|

Figura 5-2. Rueda de descriptores de olor relacionada con Aguas Servidas.

(Fuente: Burlingame et al., 2004) [8]

8 Referencia: Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA, 2017, pág. 24.

Página 67 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Tabla 5-6. Descripción de emisiones odorantes.

|Zona|Fuente de Olor|Calidad|Tipo de Olor|Intensidad|Tono<br>Hedónico|
|---|---|---|---|---|---|
|Tratamiento<br>de Aguas<br>Servidas|Cámara de Rejas|Grasa,<br>descomposición,<br>picante.|Compuesto|2|-2|
|Tratamiento<br>de Aguas<br>Servidas|PEAS|Descomposición,<br>aguas servidas,<br>vegetales,<br>descompuestos.|Compuesto|2|-2|
|Tratamiento<br>de Aguas<br>Servidas|Cámara de Entrada|Descomposicion,<br>picante, sulforoso.|Compuesto|2|-2|
|Tratamiento<br>de Aguas<br>Servidas|Pretratamiento|Descomposicion,<br>tierra, aguas servidas.|Compuesto|2|-2|
|Tratamiento<br>de Aguas<br>Servidas|Contenedor de Sólidos 1|Vegetales<br>descompuestos,<br>podrido, humedad.|Compuesto|3|-3|
|Tratamiento<br>de Aguas<br>Servidas|Contenedor de Sólidos 2|Vegetales<br>descompuestos,<br>podrido, humedad.|Compuesto|3|-3|
|Tratamiento<br>de Aguas<br>Servidas|Laguna de Aireación|Humeda, lavazas,<br>tierra, ajoso.|Compuesto|2|-2|
|Tratamiento<br>de Aguas<br>Servidas|Laguna Parcialmente<br>Aireada 1|Humeda, lavazas,<br>tierra, ajoso.|Compuesto|2|-2|
|Tratamiento<br>de Aguas<br>Servidas|Laguna Parcialmente<br>Aireada 2|Humeda, lavazas,<br>tierra, ajoso.|Compuesto|2|-2|
|Tratamiento<br>de Aguas<br>Servidas|Laguna Parcialmente<br>Aireada 3|Humeda, lavazas,<br>tierra, ajoso.|Compuesto|2|-2|
|Tratamiento<br>de Aguas<br>Servidas|Planta Elevadora de<br>Retornos|Fecal, humedad,<br>descomposición.|Compuesto|1|-1|
|Tratamiento<br>de Aguas<br>Servidas|Cámara de Contacto<br>Ampliada|Desinfectante, cloro.|Compuesto|1|-1|
|Tratamiento<br>de Lodos|Lecho de Secado|Descomposición, Fecal,<br>Lodos, Humedad.|Compuesto|3|-3|

Los valores de emisión utilizados se muestran en la Tabla 5-7, ordenados desde mayor a

menor emisión, a modo de ranking de emisiones.

Tabla 5-7. Tasas de emisión por unidad.

|Fuente de Olor|Tasa de Emisión Total<br>(Uo/s)9|
|---|---|
|Lecho de Secado|3892,73|
|Laguna de Aireación|1135,20|

9 El valor de Tasa de Emisión de Olor se calcula multiplicando el valor de concentración de olor por la superficie
de la fuente, en el caso de las fuentes superficiales. Para las fuentes puntuales, para obtener el valor de Tasa
de Emisión de Olor, se debe multiplicar el flujo volumétrico de la fuente por el valor de concentración de olor.

Página 68 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Fuente de Olor|Tasa de Emisión Total<br>(Uo/s)9|
|---|---|
|Laguna Parcialmente 3|405,84|
|Laguna Parcialmente 1|376,20|
|Laguna Parcialmente 2|376,20|
|Pretratamiento|56,58|
|Cámara de Contacto Ampliada|44,89|
|Cámara de Rejas|37,38|
|Cámara de Entrada|25,09|
|PEAS|24,23|
|Contenedores de Sólidos 1|6,12|
|Contenedores de Sólidos 2|6,12|
|Planta Elevadora de Retornos|0,88|

Página 69 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

### 5.2 Receptores discretos definidos

Respecto a los receptores definidos, se consideraron 12 receptores discretos, tal como lo

muestra la Figura 5-3.

Figura 5-3. Mapa de receptores discretos definidos.

La ubicación y el detalle de los receptores definidos se presenta en la Tabla 5-8.

Tabla 5-8. Coordenadas de receptores discretos definidos (UTM WGS-84 19S).

|Receptor10|Coordenadas (m)|Col3|Altitud<br>(m)|Distancia *<br>(m)|Altura<br>(m)|Descripción|
|---|---|---|---|---|---|---|
|Receptor10|Coordenada<br>Este<br>(m)|Coordenada<br>Norte<br>(m)|Coordenada<br>Norte<br>(m)|Coordenada<br>Norte<br>(m)|Coordenada<br>Norte<br>(m)|Coordenada<br>Norte<br>(m)|
|R01|271.106|6.181.717|136,27|436,81|1,5|Vivienda|

10 Receptores 01 al 03, son Receptores de Ruido entregado por el Titular. Receptores 04 al 12 son Receptores
propuestos de Olores.

Página 70 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

|Receptor10|Coordenadas (m)|Col3|Altitud<br>(m)|Distancia *<br>(m)|Altura<br>(m)|Descripción|
|---|---|---|---|---|---|---|
|Receptor10|Coordenada<br>Este<br>(m)|Coordenada<br>Norte<br>(m)|Coordenada<br>Norte<br>(m)|Coordenada<br>Norte<br>(m)|Coordenada<br>Norte<br>(m)|Coordenada<br>Norte<br>(m)|
|R02|271.689|6.181.970|133,44|41,16|1,5|Galpón<br>(Vulcanización)|
|R03|271.600|6.182.114|132,8|157,18|1,5|Vivienda|
|R04|270.747|6.181.808|145,35|761,81|1,5|Vivienda|
|R05|270.609|6.182.546|133,62|1108,27|1,5|Vivienda|
|R06|271.280|6.182.427|131,4|565,65|1,5|Vivienda|
|R07|271.683|6.182.063|133,17|106,88|1,5|Vivienda|
|R08|271.889|6.182.079|133,6|265,69|1,5|Vivienda|
|R09|271.867|6.181.947|133,85|185,57|1,5|Vivienda|
|R10|271.981|6.181.780|134,43|289,63|1,5|Vivienda|
|R11|271.878|6.180.054|143,2|1766,09|1,5|Vivienda|
|R12|271.148|6.181.563|136,3|469,48|1,5|Cementerio|

*Distancia desde el Receptor hasta los Límites del Proyecto.

Para la determinación de los receptores, se tomó en cuenta la presencia de casas y viviendas

cercanas al proyecto, ya que principalmente en estas se concentra la población susceptible

de ser afectada por las emisiones del proyecto (su salud y sistema de vida). No se

encontraron actividades de tipo turístico en la zona, que pudiesen verse afectadas

negativamente por las emisiones del proyecto. Tampoco se identificaron grupos de

población protegida en la zona.

Página 71 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

## 6. Resultados de la modelación

### 6.1 Isolíneas de concentraciones

A continuación, se presentan las isolíneas de concentración de Unidades de Olor para cada

uno de sus estadígrafos normados. Las isolíneas han sido trazadas desde valores de 1 Uo para

Percentil 98 y Percentil 99,5 y desde valores de 1 hora para la identificación de horas de

excedencia. El Punto de Máximo Impacto (PMI) se ha destacado en color rojo, mostrando la

ubicación de dicho punto, cuyas coordenadas se presentan a un costado de cada imagen,

junto a la escala de colores.

En las siguientes Figuras, se puede observar que el Punto de Máximo Impacto, está ubicado

al interior del Proyecto, entregando valores de 27 y 35 Uo/m [3], para el Percentil 98 y 99,5,

respectivamente.

Página 72 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 6-1. Isolínea de concentración de olor, percentil 99,5.

Página 73 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 6-2. Isolínea de concentración de olor, percentil 98.

Página 74 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 6-3. Isolínea de concentración de olor, horas de excedencia de 3,5 UO.

Página 75 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Figura 6-4. Isolínea de concentración de olor, horas de excedencia de 5 UO.

Página 76 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Tabla 6-1. Aportes de Olor en los receptores.

### 6.2 Aportes de Olor en los Receptores

|Receptor|Coord. UTM WGS-84 19S|Col3|Percentiles|Col5|Límite de 3,5 UO|Col7|Límite de 5 UO|Col9|
|---|---|---|---|---|---|---|---|---|
|<br>Receptor|UTMX (m)|UTMY (m)|P98<br>1 hora (UO/m3)|P99,5<br>1 hora (UO/m3)|N° Horas<br>sobre 3,5 UO<br>Máximo normado<br>175|% Horas<br>sobre 3,5 UO<br>Máximo normado<br>2%|N° Horas<br>sobre 5 UO<br>Máximo normado<br>175|% Horas<br>sobre 5 UO<br>Máximo normado<br>2%|
|R01|271.106|6.181.717|0,738|0,980|0|0,0%|0|0,0%|
|R02|271.689|6.181.970|4,660|5,493|384|4,4%|126|1,4%|
|R03|271.600|6.182.114|2,660|3,316|32|0,4%|0|0,0%|
|R04|270.747|6.181.808|0,312|0,529|0|0,0%|0|0,0%|
|R05|270.609|6.182.546|0,306|0,431|0|0,0%|0|0,0%|
|R06|271.280|6.182.427|0,779|0,957|0|0,0%|0|0,0%|
|R07|271.683|6.182.063|2,881|3,519|46|0,5%|0|0,0%|
|R08|271.889|6.182.079|1,714|2,106|0|0,0%|0|0,0%|
|R09|271.867|6.181.947|2,726|3,353|27|0,3%|0|0,0%|
|R10|271.981|6.181.780|1,647|1,965|0|0,0%|0|0,0%|
|R11|271.878|6.180.054|0,086|0,118|0|0,0%|0|0,0%|
|R12|271.148|6.181.563|0,577|0,802|0|0,0%|0|0,0%|
|PMI|271.597|6.181.842|27,370|35,122|5889|67,2%|4451|50,8%|

Página 77 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

### 6.1 Área de Influencia

Siguiendo los lineamientos entregados en la Guía para la Predicción y Evaluación de Olores

establecidos por el Servicio de Evaluación Ambiental, se presenta a continuación el área de

influencia por olores del presente proyecto, para los percentiles 98 y 99,5.

Figura 6-5. Área de influencia.

En este caso, el área de influencia abarca una superficie de 0,79 km [2] y 1,133 km [2], para

Percentil 98 y 99,5 respectivamente.

Página 78 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

## 7. Discusión

El Proyecto se desarrollará en la Región del Libertador General Bernardo O’Higgins, la que

presenta un clima predominante del tipo Templado Mediterráneo, con variaciones por

efecto de la topografía local. En la costa se presenta nuboso, mientras que hacia el interior

debido a la sequedad experimenta fuertes contrastes térmicos. Las precipitaciones son

mayores en la costa y en la Cordillera de los Andes, debido al relieve que no deja entrada a

los vientos húmedos oceánicos. En el litoral, que recibe la influencia oceánica predomina el

clima templado nuboso, caracterizado por una mayor humedad y abundante nubosidad. En

el sector de la depresión intermedia predomina un clima templado de tipo mediterráneo

cálido con una estación seca de seis meses y un invierno lluvioso.

Para el análisis de variables meteorológicas, se utilizó la estación Nilahue-La Quebrada

ubicada en Pumanque, siendo la estación meteorológica más próxima con información

meteorológica disponible.

En relación con las temperaturas, los mayores valores se registran en el período diurno,

durante la tarde, alrededor de las 15 horas de los meses de enero y febrero, disminuyendo

hacia alcanzar las temperaturas más bajas hacia las primeras horas de la mañana de los

meses de junio y julio, siendo el año 2022 el año más frío de acuerdo con los datos registrados

por la estación. En cuanto a la humedad los mayores valores se registran en el período

nocturno, durante las madrugadas de los meses de junio y julio, disminuyendo hacia alcanzar

los valores de humedad más baja durante las tardes de los meses de enero y febrero,

coincidente con las máximas temperaturas, entre las 15 y 16 horas.

Respecto al viento, a nivel de ciclo diario las velocidades de viento más bajas se presentan

durante todo el período nocturno, ascendiendo en magnitud hasta lograr las velocidades

más altas durante el período diurno, más específicamente, durante la tarde. A nivel intra

anual, las mayores velocidades de viento se presentan durante las estaciones cálidas del año,

específicamente durante las tardes del mes de enero alrededor de las horas, consistente con

Página 79 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

las horas de mayor temperatura y menor humedad, y las velocidades mínimas se presentan

durante las madrugadas de las estaciones cálidas del año. En cuanto a las calmas, éstas se

presentan abundantes desarrollándose con mayor frecuencia durante las madrugadas de las

estaciones cálidas del año. Con relación a la dirección del viento, se pueden observar tres

componentes predominantes, una desde el nornoreste, una desde el sur y otra desde el

oeste. Respecto de las componentes del nornoreste y sur, ella se manifiesta durante las

estaciones frías del año con vientos débiles durante el otoño a moderados hacia el invierno.

Ya para el período primavera-verano, se manifiesta la componente del oeste con vientos

débiles a moderados.

Para la generación de la base de datos de variables meteorológicas, se utilizó el modelo WRF

versión 4.3 y para la modelación de calidad del aire, se han seguido los procedimientos

establecidos por la “Guía metodológica de uso de modelos de dispersión en el SEIA” (SEA,

2023), la cual recomienda el uso de CALPUFF como uno de los modelos de dispersión de

contaminantes. De acuerdo con el análisis de incertidumbre, los rangos de análisis

cuantitativo están dentro de las métricas recomendables de análisis de incertidumbre.

Respecto del análisis de los resultados, estos permiten cuantificar las emisiones de olor del

proyecto. La escala de percepciones y concentración de olores generalmente aceptada a

nivel internacional las que se resumen en la siguente tabla:

Tabla 7-1. Concentración y percepción.

|Concentración|Percepción|
|---|---|
|1 Uo/m3|50% de la población puede comenzar a percibir un olor|
|3 Uo/m3|50% de la población puede reconocer o comenzar a reconocer un olor|
|5 Uo/m3|El olor es calificable y puede comenzar a recibirse quejas (puede ser<br>identificado)|
|10 Uo/m3|Los olores son reconocibles y se pueden recibir reclamos|

Página 80 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

Varias jurisdicciones alrededor del mundo han implementado con éxito programas de

gestión de olores, que proponen criterios de percepción de olor que oscilan entre 1 y 10

Uo/m [3], e incluso valores mayores [11] . También se han considerado distintos criterios de

evaluación, siendo el percentil 98 del total de horas modeladas uno de los que más se repiten

en la normativa internacional.

De acuerdo con lo establecido en el DS 40 “Reglamento del Sistema de Evaluación de Impacto

Ambiental” de Agosto de 2013, en su artículo 11:

_“_
_Normas de referencia_ _._

_Las normas de calidad ambiental y de emisión que se utilizarán como referencia para los_

_efectos de evaluar si se genera o presenta el riesgo indicado en la letra a) y los efectos_

_adversos señalados en la letra b), ambas del artículo 11 de la Ley, serán aquellas vigentes en_

_los siguientes Estados: República Federal de Alemania, República Argentina, Australia,_

_República Federativa del Brasil, Canadá, Reino de España, Estados Unidos Mexicanos, Estados_

_Unidos de América, Nueva Zelandia, Reino de los Países Bajos, República Italiana, Japón,_

_Reino de Suecia y Confederación Suiza. Para la utilización de las normas de referencia, se_

_priorizará aquel Estado que posea similitud en sus componentes ambientales, con la situación_

_nacional y/o local, lo que será justificado razonablemente por el proponente._

_Cuando el proponente señale las normas de referencia extranjeras que utiliza deberá_

_acompañar un ejemplar íntegro y vigente de dicha norma.”_

En base a lo señalado, como referencia a utilizar en el presente Proyecto, se cita la

Netherlands Emission Guidelines for Air (“Normativa de Emisiones de Holanda”) [12] del año

2005, donde se estipula en el capítulo _G3: Instalaciones de Tratamiento de Aguas Residuales_,

11 Referencia: ECOTEC (2013), “Antecedentes para la Regulación de Olores en Chile”, realizado para la
Subsecretaría del Medio Ambiente, Santiago de Chile, agosto.
12 Referencia: https://olores.mma.gob.cl/wp-content/uploads/2019/03/Netherlands-Emission-Guidelines-for-Air.zip.

Página 81 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

la cual es de aplicación especial a las instalaciones de tratamiento de aguas residuales. En la

siguiente tabla, se muestra los límites propuestos, según la Normativa Holandesa:

Tabla 2. Límites Propuestos Normativa Holandesa.

|Col1|Límites Propuestos|Col3|
|---|---|---|
||Proyectos Nuevos|Proyectos Existentes|
|Para áreas residenciales densamente pobladas,<br>aglomeraciones de edificios situados a lo largo de<br>carreteras u otros objetos sensibles a las molestias<br>por olores|0,5 Uo/m3 - Percentil 98|1,5 Uo/m3 - Percentil 98|
|Para áreas con viviendas dispersas y agrupaciones<br>residenciales en polígonos industriales|1,0 Uo /m3- Percentil 98|3,5 Uo /m3- Percentil 98|

En el caso del presente proyecto el cual contempla la ampliación de la Planta de Tratamiento

existente y teniendo en cuenta que esta se encuentra inmerso en una zona de agrícola rural

se propone un nivel máximo permisible de 3,5 Uo/m [3] para Percentil 98.

En la Tabla 6-1, se observa que el Receptor R2 presenta horas de excedencia sobre el límite

propuesto de 3,5 Uo/m [3] con un valor de 4,4%, equivalente a 384 horas de excedencia anual.

Los valores de inmisión en los demás Receptores son bajos, no sobrepasando el límite

propuesto de 3,5 Uo/m [3] .

Respecto al punto de máximo impacto, los resultados indican que se encuentra al interior de

las dependencias del proyecto, alcanzando 27 y 35 Uo/m [3] para Percentil 98 y 99,5

respectivamente.

En la Figura 6-5 se puede apreciar área de Influencia, donde los Receptores R2, R3, R7, R8,

R9 y R10 quedan inmersos en la isolínea 1 Uo/m [3], tanto para percentil 98, como Percentil

99,5. Las áreas de influencia tienen una superficie de 0,79 y 1,133 km [2], para Percentil 98 y

99,5 respectivamente.

Página 82 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

## 8. Conclusión

En función de los resultados, que indican que de los doce receptores evaluados, solo el

Receptor 2, el cual se encuentra distante a 41 m de los límites de Planta de Tratamiento y

que es una Vulcanización con funcionamiento en horario laboral, supera el limite de inmision

propuesto de 3,5 OUE/m3 (con 385 horas de olor, equivalentes al 4,4% de superación), en

tanto los restantes receptores presentan concentraciones de inmisión bajo el límite de 3,5

OUE/m3 establecido en la norma internacional de referencia. Esto evidencia que el impacto

odorífero generado por la emisiones de olor del proyecto es cercano, limitado y leve.

Es importante considerar que el modelo tiende a sobreestimar los valores lo que implica que

los resultados acá mostrados corresponden a un escenario más desfavorable. Ademas, es

significativo considerar que la zona de emplazamiento del proyecto corresponde a una zona

rural, fuera del alcance de la zonificación establecida en el Plan Regulador comunal. De igual

forma en el entorno y cercanias de la PTAS no existe presencia de reclamos por malos olores

hacia el proyecto, lo que es un buen indicador al respecto e implica que no existe afectacion

en la comunidad.

Por último, para asegurar el cumplimiento de las normativas de referencia propuestas y

eliminar y/o disminuir el reducido impacto y alcance odorante presentado por el proyecto,

se sugiere implementar un Plan de Gestión de Olores con medidas rigurosas y seguimiento

de olores al interior y exterior del recinto y aplicar las mejores técnicas disponibles (MTD).

En conclusión y en vista de los resultados, se considera que los impactos por emisión de

olores del presente proyecto son poco significativos, no generando modificaciones ni efectos

negativos, tanto para la salud y costumbres de grupos humanos en el area de influencia como

al exterior de esta, ni a los elementos del medio ambiente suceptible de ser afectados.

Página 83 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

- [https://www.bcn.cl/siit/nuestropais/region6/clima.htm.](https://www.bcn.cl/siit/nuestropais/region6/clima.htm)

## 9. Bibliografía

- The Weather Research & Forecasting Model, NCAR/UCAR,
[https://www.mmm.ucar.edu/weather-research-and-forecasting-model](https://www.mmm.ucar.edu/weather-research-and-forecasting-model)

- National Center for Atmospheric Research, NCAR/UCAR, [https://ncar.ucar.edu/what-we-](https://ncar.ucar.edu/what-we-offer)

[offer](https://ncar.ucar.edu/what-we-offer)

- A User’s Guide for the CALPUFF Dispersion Model (Version 5), Earth Tech Inc.

- Guía para la predicción y evaluación de impactos por olor en el SEIA, Servicio de

Evaluación Ambiental (SEA), 2017. Chile.

- Instituto Nacional de Normalización (2015). Norma Chilena 3386:2015 “Muestreo

estático para olfatometría”. Chile.

- Instituto Nacional de Normalización (2010). Norma Chilena 3190:2010 “Calidad del aire

- Determinación de la concentración de olor por olfatometría dinámica”. Chile.

- ECOTEC (2013), “Antecedentes para la Regulación de Olores en Chile”, realizado para la

Subsecretaría del Medio Ambiente, Santiago de Chile, agosto.

- Res. 1541:2013. Ministerio de Medio Ambiente y Desarrollo Sostenible. Colombia. 2013.

 - https://olores.mma.gob.cl/wp [content/uploads/2019/03/Colombia](https://olores.mma.gob.cl/wp-content/uploads/2019/03/Colombia-res_1541_2013.pdf) res_1541_2013.pdf

- [www.e-seia.cl](http://www.e-seia.cl/)

[http://portal.mma.gob.cl/aire/olores/](http://portal.mma.gob.cl/aire/olores/)

- [www.meteochile.cl](http://www.meteochile.cl/)

- ECOTEC (2013), “Antecedentes para la Regulación de Olores en Chile”, realizado para la

Subsecretaría del Medio Ambiente, Santiago de Chile, agosto.

- Los mapas utilizados fueron obtenidos desde QGIS, versión 3.22.7.

Página 84 de 85

Modelación de Dispersión e Impacto por Olores
Ampliación Planta de Tratamiento de Aguas Servidas Peralillo

**www.essconsultores.cl**

**La Capitanía 80, Oficina 108, Las Condes**

**Santiago, Chile**

**+562 23034022**

**+569 82234583**

Página 85 de 85

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1-1.: Coordenadas Punto Representativo del Proyecto (Datum WGS 84).**

| Coordenadas Del Proyecto<br>(UTM 19H WGS 84) | Col2 |
| --- | --- |
| Coordenada Este (m) | Coordenada Norte (m) |
| 271.601 | 6.181.886 |

**Tabla 2-1.: Estación considerada para el análisis meteorológico.**

| Estación | UTME 19S<br>WGS-84 (m) | UTMN 19S<br>WGS-84 (m) | Altitud<br>(metros) | Variables monitoreadas |
| --- | --- | --- | --- | --- |
| Nilahue-La Quebrada | 249.823,23 | 6.161.269,49 | 81 | • <br>Temperatura ambiente<br>(°C).<br>• <br>Humedad relativa (%).<br>• <br>Velocidad del viento<br>(m/s).<br>• <br>Dirección del viento (°).<br>• <br>Radiación global (W/m2).<br>• <br>Precipitación (mm). |

**Tabla 2-2.: Porcentaje de disponibilidad de datos.**

| Variable y año | Período inicio | Período fin | Disponibilidad de datos Nilahue-La Quebrada |
| --- | --- | --- | --- |
| Temperatura | Temperatura | Temperatura | Temperatura |
| Temperatura 2020 | 01/01/2020 00:00 | 31/12/2020 23:00 | 46,46% |
| Temperatura 2021 | 01/01/2021 00:00 | 31/12/2021 23:00 | 65,54% |
| Temperatura 2022 | 01/01/2022 00:00 | 31/12/2022 23:00 | 95,86% |
| Humedad Relativa | Humedad Relativa | Humedad Relativa | Humedad Relativa |
| Humedad relativa 2020 | 01/01/2020 00:00 | 31/12/2020 23:00 | 46,46% |
| Humedad relativa 2021 | 01/01/2021 00:00 | 31/12/2021 23:00 | 65,54% |
| Humedad relativa 2022 | 01/01/2022 00:00 | 31/12/2022 23:00 | 95,86% |
| Velocidad del viento | Velocidad del viento | Velocidad del viento | Velocidad del viento |
| Velocidad del viento<br>2020 | 01/01/2020 00:00 | 31/12/2020 23:00 | 50,33% |
| Velocidad del viento<br>2021 | 01/01/2021 00:00 | 31/12/2021 23:00 | 65,17% |
| Velocidad del viento<br>2022 | 01/01/2022 00:00 | 31/12/2022 23:00 | 95,09% |

**Tabla 3-1.: Configuración física del modelo WRF 4.3, dominio más pequeño, de mayor resolución.**

| Parámetro | Configuración |
| --- | --- |
| Centro Latitud (WGS-84) | -34,477943 |
| Centro Longitud (WGS-84) | -71,485390 |
| Condiciones de entrada | https://rda.ucar.edu FNL DS083.2 2022 |
| Proyección cartográfica | Lambert Conformal |
| Puntos en X | 50 |
| Puntos en Y | 50 |
| Topografía | GTOPO30 (Aproximadamente 1 Kilómetro) |
| Uso de suelo | USGS (Aproximadamente 1 Kilómetro) |
| Resolución horizontal (Km) | 1 |
| Resolución vertical (niveles) | 35 niveles hasta 5 hPa |
| Microfísica<br>mp_physics = 6 | “WRF Single-Moment 6-class scheme”. Esquema<br>micro físico de 6 clases, que incorpora además de<br>líquidos, hielo y nieve. Parametrización ideal para<br>simulaciones a alta resolución. Esquema que<br>diferencia el tipo de precipitación liquida o sólida,<br>variables necesarias para CALPUFF |
| Radiación (Onda larga y Corta)<br>ra_lw_physics = 1<br>ra_sw_physics = 1 | “RRTMG”. Esquema radiativo simple y eficiente,<br>capaz de simular los fenómenos radiativos de onda<br>larga a través del solapamiento de capas nubosas.<br>Esquema<br>simple<br>y <br>eficiente,<br>ampliamente<br>documentado. Utilizado como parametrización por<br>defecto por WRF y por el equipo de testeo y mejora<br>continua. |
| Modelo de suelo<br>sf_sfclay_physics =2 | “Noah LSM”. Modelo de Superficie de Tierra (Land<br>Surface Model, LSM), que tiene en cuenta una serie<br>de procesos importantes en la capa superficial de<br>suelo, como el flujo de calor sensible, el flujo de calor<br>latente, la humedad del suelo y la temperatura del<br>suelo. Proporciona una descripción detallada de la<br>interacción suelo-atmósfera y se utiliza en una |

**Tabla 3-2.: Configuración del modelo CALPUFF.**

| Parámetro | Configuración |
| --- | --- |
| Centro UTM E (m) WGS-84 | 271.747 m UTM WGS-84 19S |
| Centro UTM N (m) WGS-94 | 6.182.045 m UTM WGS-84 19S |
| Resolución espacial (m) | 300 |
| Puntos en X | 100 |
| Puntos en Y | 100 |
| Topografía | SRTM1 (Aproximadamente 30 metros de resolución) |
| Uso de suelo | GLCC (USGS30 aproximadamente a 1 Kilómetro e resolución) |

**Tabla 3-3.: Tipos de uso de suelos y parámetros considerados por CALPUFF, parámetros por defecto.**

| Categorí<br>a<br>CALPUFF | Categorí<br>a GLCC | Rugosida<br>d | Albedo | Bowen | Flujo de<br>calor<br>natural | Flujo de calor<br>antropogénic<br>o | Área<br>foliar | Descripción |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | 21 | 0.25 | 0.15 | 1 | 0.15 | 0 | 3 | Cultivo o Pastoreo |
| 20 | 22 | 0.25 | 0.15 | 1 | 0.15 | 0 | 3 | Huertos, Arboledas,<br>Viñedos, Viveros |
| 20 | 23 | 0.25 | 0.15 | 1 | 0.15 | 0 | 3 | Operaciones de<br>alimentación<br>confinada |
| 20 | 24 | 0.25 | 0.15 | 1 | 0.15 | 0 | 3 | Agricultura |
| 30 | 31 | 0.05 | 0.25 | 1 | 0.15 | 0 | 0.5 | Pastizales<br>herbáceos |
| 30 | 32 | 0.05 | 0.25 | 1 | 0.15 | 0 | 0.5 | Pastizales de<br>arbustos y<br>matorrales |
| 30 | 33 | 0.05 | 0.25 | 1 | 0.15 | 0 | 0.5 | Pastizales mixtos |
| 40 | 41 | 1 | 0.1 | 1 | 0.15 | 0 | 7 | Tierra de bosque<br>caducifolio |
| 40 | 42 | 1 | 0.1 | 1 | 0.15 | 0 | 7 | Tierra de bosque<br>siempre verde |
| 40 | 43 | 1 | 0.1 | 1 | 0.15 | 0 | 7 | Tierra forestal<br>mixta |
| 51 | 53 | 0.001 | 0.1 | 0 | 0 | 0 | 0 | Reservorios |

**Tabla 4-1.: Comparación cuantitativa de variables.**

| Estadístico | Velocidad del viento | Temperatura |
| --- | --- | --- |
| BIAS | -1,336 | -0,522 |
| MAE | 1,428 | 2,800 |
| RMSE | 1,212 | 2,353 |
| Coeficiente de correlación (r) | 0,637 | 0,893 |

**Tabla 5-1.: Fuentes de olor del Proyecto.**

| ID | Fuente | Estado | Código SRC | Tipo de<br>Fuente | Principales factores<br>operacionales que<br>influyen en la emisión de<br>olor | Régimen de<br>Funcionamient<br>o |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Cámara de<br>Rejas | Existente | SRC_1 | Puntual | Exposición al ambiente<br>por recepción e<br>impulsión de aguas<br>servidas. | 24 horas, 7 días<br>a la semana,<br>365 días al año |
| 2 | PEAS | Proyectada | SRC_2 | Puntual | Exposición puntual al<br>ambiente por ingreso y<br>elevación de aguas<br>servidas a tratamiento. | 24 horas, 7 días<br>a la semana,<br>365 días al año |
| 3 | Cámara de<br>Entrada | Proyectada | SRC_3 | Puntual | Exposición al ambiente<br>por acumulación y<br>circulación de aguas<br>servidas. | 24 horas, 7 días<br>a la semana,<br>365 días al año |
| 4 | Pretratamiento | Proyectada | SRC_4 | Difusa | Exposición al ambiente<br>por acumulación y<br>tratamiento preliminar<br>de aguas servidas. | 24 horas, 7 días<br>a la semana,<br>365 días al año |
| 5 | Contenedores<br>de Sólidos 1 | Proyectada | SRC_5 | Puntual | Exposición puntual al<br>ambiente<br>por acumulación de<br>residuos orgánicos. | 24 horas, 7 días<br>a la semana,<br>365 días al año |
| 6 | Contenedores<br>de Sólidos 2 | Proyectada | SRC_6 | Puntual | Puntual | 24 horas, 7 días<br>a la semana,<br>365 días al año |
| 7 | Laguna de<br>Aireación | Proyectada | SRC_7 | Superficial<br>Activa | Exposición al ambiente<br>por acumulación y<br>aireación y presencia de<br>sobrenadantes de aguas<br>servidas. | 24 horas, 7 días<br>a la semana,<br>365 días al año |
| 8 | Laguna<br>Parcialmente 1 | Proyectada | SRC_8 | Superficial<br>Pasiva | Exposición al ambiente<br>por acumulación y<br>aireación de aguas<br>servidas. | 24 horas, 7 días<br>a la semana,<br>365 días al año |
| 9 | Laguna<br>Parcialmente 2 | Proyectada | SRC_9 | Superficial<br>Pasiva | Exposición al ambiente<br>por acumulación y<br>aireación de aguas<br>servidas. | 24 horas, 7 días<br>a la semana,<br>365 días al año |

**Tabla 5-2.: Homologación de Fuentes.**

| ID | Fuente | Se Homologa con la siguiente fuente: |
| --- | --- | --- |
| 1 | Cámara de Rejas | Fuente Cámara de Entrada (ACTUAL) |
| 2 | PEAS | Fuente Cámara de Entrada (ACTUAL) |
| 4 | Pretratamiento | Fuente Cámara de Entrada (ACTUAL) |
| 5 | Contenedores de Sólidos 1 y 2 | Fuente Cámara de Entrada (ACTUAL) |
| 8 | Laguna Parcialmente 1, 2 y 3 | Fuente Laguna de Aireación (ACTUAL) |
| 11 | Planta Elevadora de Retornos | Fuente Laguna de Aireación (ACTUAL) |
| 13 | Lecho de Secado | Fuente Cancha de Acopio de Lodos - DIA “Planta de Tratamiento de Aguas<br>Servidas Buin Poniente”. |

**Tabla 5-3.: Dimensiones, ubicación y tasas de emisión de fuentes.**

| Fuente | Unidades | Tipo de Fuente | Dimensiones | Col5 | Área<br>Expuesta<br>(m2) | Concentración<br>de Olor<br>(Uo/m3) | Tasa de<br>Emisión<br>por Área<br>(Uo/s*m2) | Tasa de<br>Emisión<br>Odorante<br>(Uo/s) | Coordenada Central (m) | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fuente | Unidades | Tipo de Fuente | Ancho (m) x<br>Largo (m) o<br>Diámetro (m) | Alto (m) | Alto (m) | Alto (m) | Alto (m) | Alto (m) | Este | Norte |
| Cámara de Rejas | 1 | Puntual | ø = 2,72 | Ras del Suelo | 3,66 | 386,00 | 6,43 | 37,38 | 271.749,947 | 6.182.045,770 |
| PEAS | 1 | Puntual | ø = 2,19 | Ras del Suelo | 3,29 | 386,00 | 6,43 | 24,23 | 271.746,870 | 6.182.050,182 |
| Cámara de Entrada | 1 | Puntual | 1,2 x 3,25 | Ras del Suelo | 3,90 | 386,00 | 6,43 | 25,09 | 271.529,224 | 6.181.879,788 |
| Pretratamiento | 1 | Difusa | 1,60 x 5,50 | 2,40 | 8,80 | 386,00 | 6,43 | 56,58 | 271.527,229 | 6.181.872,615 |
| Contenedores de Sólidos<br>1 | 1 | Puntual | 1,22 x 0,78 | 2,00 | 0,95 | - | 6,43 | 6,12 | 271.525,200 | 6.181.872,718 |
| Contenedores de Sólidos<br>2 | 1 | Puntual | 1,22 x 0,78 | 2,00 | 0,95 | - | 6,43 | 6,12 | 271.526,539 | 6.181.870,176 |
| Laguna de Aireación | 1 | Superficial Activa | 43,00 x 33,00 | Ras del Suelo | 1.419,00 | 98,00 | 0,80 | 1.135,20 | 271.564,980 | 6.181.883,790 |
| Laguna Parcialmente 1 | 1 | Superficial Pasiva | 28,50 x 16,50 | Ras del Suelo | 470,25 | 98,00 | 0,80 | 376,20 | 271.611,400 | 6.181.915,720 |
| Laguna Parcialmente 2 | 1 | Superficial Pasiva | 28,50 x 16,50 | Ras del Suelo | 470,25 | 98,00 | 0,80 | 376,20 | 271.617,630 | 6.181.899,930 |
| Laguna Parcialmente 3 | 1 | Superficial Pasiva | 28,50 x 16,50 | Ras del Suelo | 507,30 | 98,00 | 0,80 | 405,84 | 271.635,650 | 6.181.867,670 |
| Planta Elevadora de<br>Retornos | 1 | Superficial Pasiva | 1,0 x 1,10 | Ras del Suelo | 1,10 | 98,00 | 0,80 | 0,88 | 271.592,638 | 6.181.811,719 |
| Cámara de Contacto<br>Ampliada | 1 | Superficial Pasiva | 8,20 x 7,82 | Ras del Suelo | 64,12 | 85,00 | 0,70 | 44,89 | 271.666,641 | 6.181.904,831 |
| Lecho de Secado | 1 | Superficial Pasiva | 45,00 x 21,90 | Ras del Suelo | 985,50 | - | 3,95 | 3.892,73 | 271.585,720 | 6.181.834,070 |

**Tabla 5-4.: Escala de Intensidad de Olor.**

| Número | Intensidad |
| --- | --- |
| 0 | Sin Olor |
| 1 | Muy Suave |
| 2 | Suave |
| 3 | Medio |
| 4 | Fuerte |
| 5 | Muy Fuerte |
| 6 | Extremadamente Fuerte |

**Tabla 5-6.: Descripción de emisiones odorantes.**

| Zona | Fuente de Olor | Calidad | Tipo de Olor | Intensidad | Tono<br>Hedónico |
| --- | --- | --- | --- | --- | --- |
| Tratamiento<br>de Aguas<br>Servidas | Cámara de Rejas | Grasa,<br>descomposición,<br>picante. | Compuesto | 2 | -2 |
| Tratamiento<br>de Aguas<br>Servidas | PEAS | Descomposición,<br>aguas servidas,<br>vegetales,<br>descompuestos. | Compuesto | 2 | -2 |
| Tratamiento<br>de Aguas<br>Servidas | Cámara de Entrada | Descomposicion,<br>picante, sulforoso. | Compuesto | 2 | -2 |
| Tratamiento<br>de Aguas<br>Servidas | Pretratamiento | Descomposicion,<br>tierra, aguas servidas. | Compuesto | 2 | -2 |
| Tratamiento<br>de Aguas<br>Servidas | Contenedor de Sólidos 1 | Vegetales<br>descompuestos,<br>podrido, humedad. | Compuesto | 3 | -3 |
| Tratamiento<br>de Aguas<br>Servidas | Contenedor de Sólidos 2 | Vegetales<br>descompuestos,<br>podrido, humedad. | Compuesto | 3 | -3 |
| Tratamiento<br>de Aguas<br>Servidas | Laguna de Aireación | Humeda, lavazas,<br>tierra, ajoso. | Compuesto | 2 | -2 |
| Tratamiento<br>de Aguas<br>Servidas | Laguna Parcialmente<br>Aireada 1 | Humeda, lavazas,<br>tierra, ajoso. | Compuesto | 2 | -2 |
| Tratamiento<br>de Aguas<br>Servidas | Laguna Parcialmente<br>Aireada 2 | Humeda, lavazas,<br>tierra, ajoso. | Compuesto | 2 | -2 |
| Tratamiento<br>de Aguas<br>Servidas | Laguna Parcialmente<br>Aireada 3 | Humeda, lavazas,<br>tierra, ajoso. | Compuesto | 2 | -2 |
| Tratamiento<br>de Aguas<br>Servidas | Planta Elevadora de<br>Retornos | Fecal, humedad,<br>descomposición. | Compuesto | 1 | -1 |
| Tratamiento<br>de Aguas<br>Servidas | Cámara de Contacto<br>Ampliada | Desinfectante, cloro. | Compuesto | 1 | -1 |
| Tratamiento<br>de Lodos | Lecho de Secado | Descomposición, Fecal,<br>Lodos, Humedad. | Compuesto | 3 | -3 |

**Tabla 5-7.: Tasas de emisión por unidad.**

| Fuente de Olor | Tasa de Emisión Total<br>(Uo/s)9 |
| --- | --- |
| Lecho de Secado | 3892,73 |
| Laguna de Aireación | 1135,20 |

**Tabla 5-8.: Coordenadas de receptores discretos definidos (UTM WGS-84 19S).**

| Receptor10 | Coordenadas (m) | Col3 | Altitud<br>(m) | Distancia *<br>(m) | Altura<br>(m) | Descripción |
| --- | --- | --- | --- | --- | --- | --- |
| Receptor10 | Coordenada<br>Este<br>(m) | Coordenada<br>Norte<br>(m) | Coordenada<br>Norte<br>(m) | Coordenada<br>Norte<br>(m) | Coordenada<br>Norte<br>(m) | Coordenada<br>Norte<br>(m) |
| R01 | 271.106 | 6.181.717 | 136,27 | 436,81 | 1,5 | Vivienda |

**Tabla 6-1.: Aportes de Olor en los receptores.**

| Receptor | Coord. UTM WGS-84 19S | Col3 | Percentiles | Col5 | Límite de 3,5 UO | Col7 | Límite de 5 UO | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <br>Receptor | UTMX (m) | UTMY (m) | P98<br>1 hora (UO/m3) | P99,5<br>1 hora (UO/m3) | N° Horas<br>sobre 3,5 UO<br>Máximo normado<br>175 | % Horas<br>sobre 3,5 UO<br>Máximo normado<br>2% | N° Horas<br>sobre 5 UO<br>Máximo normado<br>175 | % Horas<br>sobre 5 UO<br>Máximo normado<br>2% |
| R01 | 271.106 | 6.181.717 | 0,738 | 0,980 | 0 | 0,0% | 0 | 0,0% |
| R02 | 271.689 | 6.181.970 | 4,660 | 5,493 | 384 | 4,4% | 126 | 1,4% |
| R03 | 271.600 | 6.182.114 | 2,660 | 3,316 | 32 | 0,4% | 0 | 0,0% |
| R04 | 270.747 | 6.181.808 | 0,312 | 0,529 | 0 | 0,0% | 0 | 0,0% |
| R05 | 270.609 | 6.182.546 | 0,306 | 0,431 | 0 | 0,0% | 0 | 0,0% |
| R06 | 271.280 | 6.182.427 | 0,779 | 0,957 | 0 | 0,0% | 0 | 0,0% |
| R07 | 271.683 | 6.182.063 | 2,881 | 3,519 | 46 | 0,5% | 0 | 0,0% |
| R08 | 271.889 | 6.182.079 | 1,714 | 2,106 | 0 | 0,0% | 0 | 0,0% |
| R09 | 271.867 | 6.181.947 | 2,726 | 3,353 | 27 | 0,3% | 0 | 0,0% |
| R10 | 271.981 | 6.181.780 | 1,647 | 1,965 | 0 | 0,0% | 0 | 0,0% |
| R11 | 271.878 | 6.180.054 | 0,086 | 0,118 | 0 | 0,0% | 0 | 0,0% |
| R12 | 271.148 | 6.181.563 | 0,577 | 0,802 | 0 | 0,0% | 0 | 0,0% |
| PMI | 271.597 | 6.181.842 | 27,370 | 35,122 | 5889 | 67,2% | 4451 | 50,8% |

**Tabla 7-1.: Concentración y percepción.**

| Concentración | Percepción |
| --- | --- |
| 1 Uo/m3 | 50% de la población puede comenzar a percibir un olor |
| 3 Uo/m3 | 50% de la población puede reconocer o comenzar a reconocer un olor |
| 5 Uo/m3 | El olor es calificable y puede comenzar a recibirse quejas (puede ser<br>identificado) |
| 10 Uo/m3 | Los olores son reconocibles y se pueden recibir reclamos |

**Tabla 2.: Límites Propuestos Normativa Holandesa.**

| Col1 | Límites Propuestos | Col3 |
| --- | --- | --- |
|  | Proyectos Nuevos | Proyectos Existentes |
| Para áreas residenciales densamente pobladas,<br>aglomeraciones de edificios situados a lo largo de<br>carreteras u otros objetos sensibles a las molestias<br>por olores | 0,5 Uo/m3 - Percentil 98 | 1,5 Uo/m3 - Percentil 98 |
| Para áreas con viviendas dispersas y agrupaciones<br>residenciales en polígonos industriales | 1,0 Uo /m3- Percentil 98 | 3,5 Uo /m3- Percentil 98 |
