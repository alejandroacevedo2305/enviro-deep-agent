---
title: Compromisos voluntarios
author: Mauricio Paredes
date: D:20230712155217-04'00'
language: es
type: report
pages: 4
has_toc: True
has_tables: False
extraction_quality: high
keywords: [TEMPLATE JIA;JIA;2017]
---

**ANEXO 10**

ARCHIVOS NAMELIST

_Cliente_

Viña del Mar, 8 de junio de 2023

A continuación, se presentan los resultados de las configuraciones utilizadas y la descripción de
los dominios correspondientes al servicio de “Modelación Meteorológica con WRF
correspondientes al periodo 2020, 2021 y 2022 para la Zona de Laja, Dominio de 75 x 75 km.

 - Periodo de simulación: 00:00:00_01-01-2020 - 00:00:00_01-01-2023 (UTC-04).

 - Resolución horizontal dominio interior: 1.0 km.

 - Extensión horizontal del dominio interior: 75 x 75 km.

 - Centro Dominio: -37.263, -72.711.

 - Proyección: Lambert Conformal Conic (LCC)

 - True Lat 1: -33.402

 - True Lat 2: -41.178

 - Datum: NWS-84

En la siguiente se presentan el dominio de modelación con su resolución y usos de suelo:

**Figura 1:** Ubicación del dominio y usos de suelo.

Las características de las simulaciones se resumen en la siguiente tabla:

Modelo numérico WRF-ARW v4.2

Periodo de simulación Enero a diciembre

Años de simulación 2020, 2021 y 2022

Resolución horizontal 1 km

Coordenadas verticales 44 niveles

Condición de borde GFS FNL 0.25o x 0.25o

Topografía SRTM 90 m
Características superficie MODIS

Las parametrizaciones utilizadas del modelo WRF utilizada se corresponden a las recomendadas
por el Ministerio de Energía, la Agencia de Cooperación Internacional Alemana (GIZ) y el
Departamento de geofísica de la Universidad de Chile [1] . Estas parametrizaciones se
corresponden con los mejores resultados obtenidos entre diferentes conjuntos analizados y la
Base de Datos de Observaciones Meteorológicas nacionales con 420 anemómetros.

En todos los casos se utilizaron todos los años disponibles para evaluar estadísticamente la
bondad del modelo WRF a lo largo del país (Figura 2):

**Figura 2:** Diagrama de dispersión del viento medio observado y modelado (extraído de DGF UChile) . [2]

1
http://ernc.dgf.uchile.cl/Explorador/Eolico/info/Documentacion_Explorador_Eolico_V2_Full.pdf
2
Están incluidas datos de 420 sensores de viento en 360 ubicaciones geográficas distintas. Los puntos rojos y verdes indican las estaciones de viento
mantenidas por el Ministerio de Energía en el Norte Grande (rojo) y Norte Chico (verde). El mapa a la derecha indica la ubicación de la estaciones de medición de
viento incluidas en la comparación

Las estadísticas presentadas en el informe proveen información cuantitativa sobre el desempeño
de la predicción del viento medio, con valores comprendidos situándose dentro de los rangos
recomendados por el SEA en su guía de calidad del aire (BIAS = [-2.5; 2.5] m/s, r [2] - 0.6): BIAS=
1.8 m/s y coeficiente de determinación r [2] = 0.74, lo cual indica un desarrollo altamente
significativo y recomendable en su uso.

**Parametrización** **Selección**

Microfísica WSM-5

Radiación onda larga RRTM

Radiación onda corta Dudhia

Capa límite QNSE
Capa superficial QNSE
Cúmulos Betts-Miller-Janjic
Suelo 5-layer thermal diffusion

Sin otro particular,

Dr Fabio Carrera Chapela

Director Técnico

AQOM Ltda.