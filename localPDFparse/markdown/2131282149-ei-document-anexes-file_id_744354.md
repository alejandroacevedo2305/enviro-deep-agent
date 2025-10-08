---
title: Sin título
author: Ibereólica
date: D:20160322102716-03'00'
language: es
type: report
pages: 36
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Anexo 6 Estudio de campos electromagnéticos Declaración de Impacto Ambiental Proyecto Fotovoltaico Elena Región de Antofagasta
-->

# Anexo 6 Estudio de campos electromagnéticos Declaración de Impacto Ambiental Proyecto Fotovoltaico Elena Región de Antofagasta

**Marzo, 2016**

ÍNDICE DE CONTENIDOS

1. Introducción ................................................................................................................ 1

2. Objetivos y alcances ................................................................................................... 2

3. Características del Proyecto ....................................................................................... 3

3.1. Subestación Transformadora 33/220 kV .............................................................. 3

3.2. Transformadores de potencia 220/33 kV ............................................................. 4

3.3. Reactancias de puesta a tierra ............................................................................ 6

3.4. Línea Eléctrica de Transmisión de 220 kV ........................................................... 6

4. Magnitud de Campos estimados para la subestación de 220 kV .............................. 10

4.1. Campo eléctrico en subestaciones de 220 kV ................................................... 10

4.1.1. Medidas internacionales ............................................................................. 11

4.2. Campo magnético en subestaciones de 220 kV ................................................ 12

4.2.1. Medidas nacionales .................................................................................... 13

4.2.2. Medidas internacionales ............................................................................. 14

4.3. Campo magnético en torno al transformador ..................................................... 16

4.4. Radio interferencia de subestación .................................................................... 16

4.5. Simulación ......................................................................................................... 18

5. Magnitud de Campos en línea de transmisión de 220 kV ......................................... 24

5.1. Campo eléctrico de baja frecuencia ................................................................... 24

5.2. Campo magnético de baja frecuencia ................................................................ 26

5.3. Campo perturbador o Radio interferencia producida por la línea ....................... 27

6. Valores límites de recomendaciones internacionales ................................................ 29

6.1. Valores límites recomendados de radio interferencia provocada por instalaciones
de alta tensión. ............................................................................................................. 29

6.2. Normas de referencia aplicables en Chile respecto de la exposición humana a
campos electromagnéticos de 50 Hz ............................................................................ 29

7. Conclusiones ............................................................................................................ 31

7.1. Valores de campo eléctrico ................................................................................ 31

7.2. Valores de inducción magnética ........................................................................ 31

7.3. Valor de radio interferencia ................................................................................ 31

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena i

8. Bibliografía y Referencias ......................................................................................... 32

ÍNDICE DE TABLAS

Tabla 1. Características principales de transformadores de nivel intermedio ..................... 3
Tabla 2. Características de transformadores ..................................................................... 4

Tabla 3. Características de reactancias de puesta a tierra ................................................. 6
Tabla 4. Características Línea de Alta Tensión .................................................................. 6

Tabla 5. Características conductores ................................................................................. 7

Tabla 6. Características cable de guardia con fibra óptica (OPGW) ................................... 7
Tabla 7. Valores en borde de franja ................................................................................. 27
Tabla 8. Valores de interferencia de radio recomendado por la Asociación de Normas
canadienses [3] ................................................................................................................ 29
Tabla 9. Límites de exposición humana a campos electromagnéticos de 50 Hz .............. 30

ÍNDICE DE FIGURAS

Figura 1. Emplazamiento del Proyecto .............................................................................. 1
Figura 2. Esquema de subestación .................................................................................... 5
Figura 3. Esquema de estructura de línea ......................................................................... 9
Figura 4. Campo eléctrico atravesando un patio de 220 kV ............................................. 10
Figura 5. Campo eléctrico en el perímetro de la S/E de 220 kV ....................................... 11
Figura 6. Campo magnético en el borde de subestación de 220 kV [5] ............................ 12
Figura 7. Campo magnético en el interior de una S/E de 220 kV ..................................... 13
Figura 8. Campo magnético en el perímetro de una S/E de 220 kV ................................. 14
Figura 9. Inducción magnética medida en la subestación [4] ........................................... 15
Figura 10. Inducción magnética calculada en la subestación [4 ....................................... 15
Figura 11. Inducción magnética fuera de un transformador de 220 MVA, 240 kV [8] ....... 16
Figura 12. Radio interferencia en borde de subestación Pontchartrain a 230 kV [9] ........ 17
Figura 13. Radio interferencia medida en los diferentes puntos del borde de la subestación
Snakefarm de 230 kV [9] ................................................................................................ 18
Figura 14. Trayectorias seleccionadas para la simulación ............................................... 19
Figura 15. Distribución de equipotenciales eléctricas en trayectoria A1 - A2 ................... 20
Figura 16. Campo eléctrico a 1 m sobre el suelo en trayectoria A1 - A2 ......................... 20
Figura 17. Distribución de equipotenciales magnéticas en trayectoria A1 - A2 ................ 21
Figura 18. Inducción magnética a 1 m sobre el suelo en trayectoria A1 - A2 .................. 21
Figura 19. Distribución de equipotenciales eléctricas en trayectoria B1 - B2 ................... 22
Figura 20. Campo eléctrico a 1 m sobre el suelo en trayectoria B1 - B2 ......................... 22
Figura 21. Distribución de equipotenciales magnéticas en trayectoria B1 - B2 ................ 23
Figura 22. Inducción magnética a 1 m sobre el suelo en trayectoria B1 - B2 .................. 23
Figura 23. Modelo con elementos finitos de silueta de torre ............................................. 24

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena ii

Figura 24. Distribución de líneas equipotenciales eléctricas ............................................ 25
Figura 25. Campo eléctrico a 1m sobre el suelo L=50 : eje de la línea ............................ 25
Figura 26. Distribución de líneas equipotenciales magnéticas ......................................... 26
Figura 27. Inducción magnética 1m sobre el suelo; L=50 : eje de la línea ....................... 26

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena iii

**1.** **Introducción**

El presente Anexo da cuenta de los resultados obtenidos en el Estudio de Campos
Electromagnéticos realizado para Proyecto Fotovoltaico Elena (en adelante, el Proyecto)
de Ibereólica Solar Elena, SpA. (en adelante, el Titular).

El Proyecto Fotovoltaico Elena consiste en la construcción y operación de dos plantas
fotovoltaicas idénticas de 223 MW AC cada una, denominadas FV-1 y FV-2, una Subestación
Transformadora 33/220 kV y una Línea de Transmisión Eléctrica de 220 kV aérea de doble
circuito, que permitirá evacuar en forma conjunta la energía eléctrica proveniente de las
plantas fotovoltaicas hasta la Subestación Eléctrica Encuentro existente, propiedad de
Transelec.

El Proyecto Fotovoltaico Elena se ubica en la comuna de María Elena, provincia de
Tocopilla, la II Región de Antofagasta, según se presenta en la figura a continuación. Está
emplazado en una zona desértica, con una altitud media de 1.130 m.s.n.m., y se localiza a
una distancia aproximada de 54 km en dirección sureste de Quillagua, 23 km en dirección
noreste de la localidad de María Elena y a 61km en dirección noroeste de Calama.

Figura 1. Emplazamiento del Proyecto

Fuente: Elaboración propia, 2016.

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 1

Cada Planta Fotovoltaica (FV-1 y FV-2) ocupa una superficie de 603 ha y se encuentra
constituida por 774.144 módulos fotovoltaicos de potencia nominal 320 Wp cada uno, que
se instalarán sobre seguidores solares a un eje horizontal para producir 223 MW AC de
potencia. Los módulos fotovoltaicos se organizan en seguidores o trackers de norte a sur,
y cada seguidor cuenta con 84 módulos. Los seguidores se colocan en filas presentando
una separación entre ejes de 6,5 metros Este-Oeste. Cada seguidor solar cuenta con un
motor alimentado por un módulo fotovoltaico y una batería dedicada.

El Proyecto se construirá en dos etapas; la primera etapa contempla la construcción de la
Planta Fotovoltaica FV-1, la Subestación Transformadora 33/220 kV y la Línea de
Transmisión Eléctrica de 220 kV. La segunda etapa consiste en la construcción de la Planta
Fotovoltaica FV-2.

En el nivel de transformación intermedio, los transformadores elevadores situados anexos
o interiores a los Centros de Transformación son los encargados de elevar la tensión hasta
el nivel de media tensión elegido (33 kV) para transportar la energía hasta la Subestación
Transformadora 33/220 kV. La relación de transformación de los transformadores trifásicos

es 420V/33kV ±2,5%±5%/0,42 kV y 50 Hz, con aislamiento en aceite. Las características
técnicas principales de los transformadores se presentan en la siguiente tabla.

**2.** **Objetivos y alcances**

En este estudio se efectúa una estimación de los campos electromagnéticos de baja y alta
frecuencia que pueden estar presentes durante la operación de las instalaciones del
Proyecto.

Se revisa en primer lugar los antecedentes del Proyecto y luego se entrega las normas de
referencia aplicables en Chile respecto de la exposición humana a campos
electromagnéticos de 50 Hz y los valores límites recomendados de radio interferencia
provocada por instalaciones de alta tensión.

Con el objeto de obtener una estimación de los respectivos valores para las instalaciones
del Proyecto, se presenta posteriormente información recogida de referencias nacionales e
internacionales respecto de valores de campo eléctrico y campo magnético medidos en
instalaciones similares a la subestación y línea de transmisión en estudio. Se incorpora los
resultados de una modelación de las barras de la subestación elevadora, y de la línea de
transmisión de 220 kV, mediante la aplicación del software QuickField [1] que utiliza el
método de elementos finitos para obtener el campo eléctrico y el campo magnético de baja
frecuencia generado en el entorno de dichas instalaciones. El campo eléctrico es
fundamentalmente dependiente del voltaje de los conductores de barras de la subestación
y línea, y la fuente del campo magnético es principalmente los transformadores en el caso
de la subestación y la corriente por los conductores en el caso de barras y línea de
transmisión.

Estos valores se confrontan con las respectivas recomendaciones y límites admisibles para
establecer finalmente una conclusión referente al impacto ambiental de la subestación y de

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 2

la línea en estudio, desde el punto de vista técnico de la emisión electromagnética de baja
frecuencia.

Similarmente se realiza una estimación del nivel de campo perturbador a frecuencias de
radio generado por la subestación y la línea de transmisión debido al fenómeno corona, en
base a medidas referenciales informadas en la bibliografía o cálculo, y se compara con
valores límites establecidos por recomendaciones internacionales.

**3.** **Características del Proyecto**

Tal como se indicó anteriormente, el Proyecto consiste en la construcción y operación de
dos plantas fotovoltaicas idénticas de 223 MW AC cada una (FV-1 y FV-2), una Subestación
Transformadora 33/220 kV y una Línea de Transmisión Eléctrica de 220 kV aérea de doble
circuito

En el nivel de transformación intermedio, los transformadores elevadores situados anexos
o interiores a los Centros de Transformación son los encargados de elevar la tensión hasta
el nivel de media tensión elegido (33 kV) para transportar la energía hasta la Subestación
Transformadora 33/220 kV. La relación de transformación de los transformadores trifásicos

es 420V/33kV ±2,5%±5%/0,42 kV y 50 Hz, con aislamiento en aceite. Las características
técnicas principales de los transformadores se presentan en la siguiente tabla.

Tabla 1. Características principales de transformadores de nivel intermedio

|Tipo:|3 fases / 50 Hz|
|---|---|
|Potencia:|3.500 kVA|
|Número de bobinados trifásicos:|2 (1 MT, 1 BT)|
|Tensión primaria (MT):|33 kV ±2,5%±5%|
|Tensión secundaria (BT):|420 V|
|Estándar:|IEC60076|
|Entorno:|Exterior|
|Temperatura ambiente:|máxima 50 oC|
|Altura de uso máx.:|≤3.000 m sobre el nivel del mar|

Fuente: Elaboración propia, 2016.

**3.1. Subestación Transformadora 33/220 kV**

La Subestación Transformadora 33/220 kV, estará constituida por el edificio eléctrico y el
parque de intemperie. En el edificio eléctrico se recogerá la energía recibida del sistema
colector de las dos Plantas Fotovoltaicas. Este edificio albergará en su sala eléctrica las
celdas de 33 kV, los equipos de control, mando, protección y servicios auxiliares de la
Subestación.

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 3

**3.2. Transformadores de potencia 220/33 kV**

Para la transformación 220/33 kV se ha previsto el montaje de dos transformadores de
potencia, trifásicos, de columnas, en baño de aceite, de intemperie, con tres devanados.

Las características constructivas esenciales son:

Tabla 2. Características de transformadores

|Tipo de servicio|Continuo/Exterior|
|---|---|
|Refrigeración|ONAN/ONAF|
|Potencia nominal|224/112/112 MVA|
|Relación de transformación:||
|Primario|220 ± 10 x 1,25kV (Regulación en carga)|
|Secundario|33 kV|
|Frecuencia|50 Hz|
|Conexión primario|Estrella|
|Conexión secundarios|Triangulo|
|Grupo de conexión|YNd11d11|
|Tensión de cortocircuito para relación 220/33 kV|14,0%|
|Tensión de cortocircuito entre devanados de 33 kV|28,0%|

Fuente: Elaboración propia, 2016.

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 4

Figura 2. Esquema de subestación

Fuente: Plano N° PFVME-09.2 Planta General de la Subestación Transformadora 33/220kV, 2016.

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 5

**3.3. Reactancias de puesta a tierra**

Las reactancias de puesta a tierra de los transformadores irán alojadas en el exterior
próximo al transformador de potencia. Se instalarán cuatro reactancias en la instalación,
una por cada secundario de los dos transformadores.

Las reactancias de puesta a tierra deberán ser capaces de soportar el 100% de la máxima
corriente de falta a tierra, durante 30 segundos, sin exceder el límite de 300oC de
temperatura, sin que se produzcan deformaciones, tanto en la reactancia como en el
aislamiento. Entre otras sus características principales serán:

|Tabla 3. Características de reactancias de puesta a|tierra|
|---|---|
|Número|4|
|Servicio|Continuo, intemperie|
|Tipo|Sumergida en aceite|
|Modo de refrigeración|ONAN|
|No de fases|3|
|Tensión Nominal|33 kV|
|Tensión más elevada para el material|36 kV|
|Máxima corriente de falla a tierra|500 A|
|Duración máxima de falla a tierra|30 s|
|Conexión|Zig-zag|
|Tensión de ensayo a frecuencia industrial|70 kV|
|Tensión de ensayo con onda de choque completa 1,2/50 μs|170 kVcr|

Fuente: Elaboración propia, 2016.

**3.4. Línea Eléctrica de Transmisión de 220 kV**

Para inyectar la energía al Sistema Interconectado del Norte Grande (SING) se construirá
una Línea de Transmisión Eléctrica aérea de doble circuito de 220 kV que partirá de la
Subestación Transformadora 33/220 kV, y se extenderá durante 18,583 km
aproximadamente hasta conectar con la Subestación Encuentro, existente y propiedad de
Transelec.

La Línea de Alta Tensión contará con 56 apoyos metálicos (estructuras) de celosía. En la
siguiente Tabla se presentan las características principales de la Línea de Alta Tensión.

Tabla 4. Características Línea de Alta Tensión

|Característica|Magnitud|Unidad|
|---|---|---|
|Frecuencia|50|Hz|
|Tensión nominal|220|kV|
|Tensión más elevada de la red|245|kV|
|Longitud|18,583|Km|
|Apoyos|56|Unidades|
|Circuitos|2|Unidades|
|Conductores aéreos por fase|2|Unidades|
|Cables a tierra|2|Unidades|

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 6

Tabla 4. Características Línea de Alta Tensión

|Característica|Magnitud|Unidad|
|---|---|---|
|Potencia máxima de transporte por circuito|466|MW|
|Potencia máxima de la línea|2 x 466|MW|
|Número de vértices|11|Unidades|

Fuente: Elaboración propia, 2016.

La franja de servidumbre de la Línea de Alta Tensión está definida por un pasillo de 40
metros de promedio, es decir, 20 metros a cada lado del eje de la misma.

Respecto a los conductores a utilizar, éstos serán del tipo AAAC A3 710 fabricados de una
aleación de aluminio, según Norma IEC 61089. En la siguiente tabla se presentan las
características de los conductores a usar por el Proyecto.

Tabla 5. Características conductores

|Característica|Magnitud|Unidad|
|---|---|---|
|Composición|61/4,15|mm|
|Diámetro del cable completo|37,30|mm|
|Sección total|825,0|mm2|
|Peso|2,230|daN/m|
|Carga de rotura|25.986|daN|
|Módulo de elasticidad|5.586|daN/mm2|
|Coeficiente de dilatación lineal|23 x 10-6|oC-1|
|Resistencia eléctrica a 20oC|0,0407|Ω/Km|

Fuente: Elaboración propia, 2016.

En cuanto al cable a tierra o guardia, este será del tipo OPGW 24 (Optical Guide Wire),
correspondiente a un cable mensajero de acero con cable de fibra óptica para
comunicaciones. Las características del cable de guardia con fibra óptica se presentan en
la Tabla a continuación.

Tabla 6. Características cable de guardia con fibra óptica (OPGW)

|Característica|Magnitud|Unidad|
|---|---|---|
|Diámetro del cable completo|15,6|mm|
|Sección total|114,9|mm2|
|Peso|0,551|daN/m|
|Carga de rotura|8.030|daN|
|Tensión máxima permitida|3.610|kV|
|Módulo de elasticidad|9.700|daN/mm2|
|Coeficiente de dilatación lineal|16,3 10-6|oC - 1|
|Resistencia eléctrica a 20oC|0,396|Ω/Km|
|Radio mínimo de curvatura|235|mm|
|Margen de temperatura|-45 a 80|oC|
|Intensidad del cortocircuito nominal|17,5|kA/0.3s|

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 7

Tabla 6. Características cable de guardia con fibra óptica (OPGW)

|Característica|Magnitud|Unidad|
|---|---|---|
|Máximo de fibras|24|Unidades|

Fuente: Elaboración propia, 2016.

Respecto al aislamiento de la línea, este se realizará mediante cadenas de aisladores de
vidrio templado de tipo caperuza y vástago. Las cadenas de aisladores serán:

Respecto al aislamiento de la línea, este se realizará mediante cadenas de aisladores de
vidrio templado de tipo caperuza y vástago. Las cadenas de aisladores serán:

 En apoyos de ángulo, anclaje y remate, cadena de amarre de 16 aisladores de vidrio
SC para 220 kV tipo U160BLP (U210BLP) según norma IEC-305, con una carga de
rotura de 160 kN (210 kN), con grapa de compresión.

 En apoyos de alineación, cadena de suspensión de 15 aisladores de vidrio SC para
220kV tipo U160BLP según norma IEC-305, con una carga de rotura de 160 kN y
grapa de suspensión preformada.

Dispondrá de una línea de fuga de al menos 7595 mm. Se encuentra en una zona que
debido a tener un ambiente seco, salino y con gran cantidad de polvo, se considera un área
con un nivel de contaminación muy alta, definiendo una línea de fuga nominal (USCD) de
53,7 mm/kV (TS 60815-1 IEC:2008 equivalente a 31 mm/kV según IEC 1986).

Los apoyos o estructuras tienen una altura libre al terreno (distancia de fase inferior al
terreno) de entre 12 m y 36 m, siendo sus alturas máximas (altura a punta de cabeza) de
15 m en pórtico y 50,3 m, respectivamente. Los apoyos utilizados en el presente Proyecto
serán torres metálicas de acero galvanizado, enrejados y auto soportados de doble circuito,
los que se dividen en estructuras con función de amarre y estructuras con función de
suspensión.

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 8

Figura 3. Esquema de estructura de línea

Fuente: Elaboración propia, 2016.

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 9

**4.** **Magnitud de Campos estimados para la subestación de 220 kV**

**4.1. Campo eléctrico en subestaciones de 220 kV**

Se acostumbra caracterizar al campo eléctrico generado por una instalación de alta tensión
por el concepto “Campo eléctrico a nivel del suelo”, que corresponde al campo eléctrico
medido o calculado a 1 metro de altura sobre el suelo. Su magnitud es proporcional al
voltaje de la instalación, por lo que en el caso en estudio, los valores de campo eléctrico
debieran ser similares a valores medidos de campo eléctrico en subestaciones de 220 kV.

Las figuras siguientes muestran los valores medidos en una S/E de 220 kV en el norte de
nuestro país [4]. La Figura 4 muestra los valores obtenidos en un trayecto de medida
transversal en el patio de 220 kV y la Figura 5, los valores obtenidos en un trayecto de
medida efectuado en el perímetro de la subestación.

Figura 4. Campo eléctrico atravesando un patio de 220 kV

El eje horizontal se encuentra en la escala de tiempo, pues el instrumento utilizado (EMDEX
II) registra el tiempo transcurrido durante la medida, no la distancia.

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 10

Figura 5. Campo eléctrico en el perímetro de la S/E de 220 kV

Se observa que a pesar de que en el interior de la instalación se alcanza valores cercanos
a 5 kV/m, los valores de campo eléctrico en el borde de la subestación (extremos de los
gráficos) no superan los **100 V/m** . El campo eléctrico es rápidamente atenuado por
estructuras y vegetación.

_**4.1.1. Medidas internacionales**_

En la figura siguiente se reproduce información de la referencia [5], que presenta el cálculo
del campo eléctrico a 1,0 m de altura en el patio de 220 kV de una subestación.

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 11

Figura 6. Campo magnético en el borde de subestación de 220 kV [5]

Se observa que pueden presentarse altos niveles de campo en el interior de la subestación,
sin embargo, en los bordes de la subestación, bordes del gráfico, el campo eléctrico se
reduce a valores inferiores a **1.000 [V/m].**

**4.2. Campo magnético en subestaciones de 220 kV**

El campo magnético existente en la vecindad de una subestación o línea de alta tensión es
generado por la corriente que circula por los conductores. Se caracteriza normalmente por
la “inducción Magnética” o “densidad de flujo Magnético” B, que tuvo originalmente como
unidad de medida el Gauss. Cuando se normalizó el sistema de unidades MKSA, se
introdujo el Tesla. La relación entre ambas unidades es: 1 Tesla = 10 [4] Gauss. La unidad
práctica de medida actual es el micro Tesla (1T = 10 [-6] Tesla ) o el mili Gauss (1 mili Gauss
= 10 [-3] Gauss ) y se relacionan por: 1 T = 10 mG. Similar al caso eléctrico, se acostumbra
caracterizar al campo magnético generado por una instalación de alta tensión por el
concepto “Inducción magnética a nivel del suelo”, que corresponde a la inducción magnética
medida o calculada a 1 metro de altura sobre el suelo.

Las instalaciones de alta tensión son trifásicas equilibradas, y en operación normal, debido
a condiciones de equilibrio de fases, la suma de las tres corrientes es nula en cualquier
instante, por lo tanto existe un grado de compensación entre los campos magnéticos
generados por los conductores de cada fase. Los elementos de una subestación, pueden
considerarse como elementos tipo conductor (ej. barras) y elementos tipo equipos (ej.

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 12

transformadores). Los elementos tipo conductor generan un campo magnético similar a una
fuente lineal de corriente, que decae con el cuadrado de la distancia. Los elementos tipo
equipo pueden considerarse como fuentes concentradas o puntuales a gran distancia y en
ese caso generan un campo magnético que decae con el cubo de la distancia.

_**4.2.1. Medidas nacionales**_

Las figuras siguientes muestran los valores medidos en una S/E de 345/220 kV en el norte
de nuestro país.

Figura 7. Campo magnético en el interior de una S/E de 220 kV

(1 T = 10 mili Gauss)

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 13

Figura 8. Campo magnético en el perímetro de una S/E de 220 kV

(1 T = 10 mili Gauss)

En el interior de una subestación eléctrica, los niveles de campo magnético son importantes
debido a la densificación de equipo eléctrico de potencia y a las menores distancias entre
conductores. No obstante, considerando que se trata de una fuente emisora “concentrada”,
la ley de decaimiento de dichos campos con la distancia es una potencia mayor que la
conocida para el caso de líneas de transmisión, por lo que tienden a reducirse mucho más
rápidamente al alejarse de la fuente.

Este efecto puede observarse en la Figura anterior, al reducirse drásticamente los valores
de campo magnético en los extremos del eje horizontal, correspondiente a los bordes de la
subestación. La Figura anterior representa una medida en el perímetro de la subestación.
Se observa que en el perímetro de la subestación, la inducción magnética no sobrepasa los
5 mili Gauss.

_**4.2.2. Medidas internacionales**_

En la referencia [6] se presenta en detalle un estudio del campo magnético calculado y
medido en una subestación abierta de 230 kV, con potencias similares a la del presente
estudio. De dicha publicación se presenta los resultados en las Figuras siguientes.

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 14

Figura 9. Inducción magnética medida en la subestación [4]

Figura 10. Inducción magnética calculada en la subestación [4

Los valores máximos en el interior bordean los 40 micro Tesla (400 mili Gauss), pero se
observa que en el perímetro de la subestación, el campo magnético se reduce
drásticamente, a valores inferiores a **5 micro Tesla (50 mili Gauss)** .

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 15

**4.3. Campo magnético en torno al transformador**

El transformador es la fuente concentrada más importante de campo magnético en una
subestación. Sin embargo, por ser una fuente concentrada, el alcance del efecto es
reducido. De la referencia [7] se extrae el gráfico de la figura siguiente, que muestra cómo
se comporta el campo magnético fuera de un transformador de 220 MVA, 240 kV.

Figura 11. Inducción magnética fuera de un transformador de 220 MVA, 240 kV [8]

Se aprecia que a pesar de ser intenso el campo magnético en la vecindad inmediata del
transformador, su decaimiento es rápido, de modo que a 10 m ya el efecto prácticamente
no es relevante. Por lo tanto, esta fuente no es significativa para el impacto ambiental fuera
de las subestaciones.

Similar conclusión se obtiene respecto del campo magnético generado por la reactancia de
puesta a tierra, durante su operación, ya que su constitución es similar a un enrollado de
transformador y además su funcionamiento es esporádico, sólo bajo una situación de falla

a tierra.

**4.4. Radio interferencia de subestación**

Las instalaciones de Alta Tensión producen interferencias electromagnéticas en
frecuencias que van desde unos pocos Hz a los GHz (109 Hz), por tanto abarca todo el
espectro de las telecomunicaciones.

En un conductor de una instalación de alta tensión, está aplicado un elevado nivel de voltaje
respecto de tierra (decenas o centenas de kilo Volts), lo cual provoca un campo eléctrico
extremadamente alto en la superficie del conductor (del orden de 100 veces mayor que el

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 16

existente a nivel del suelo). Este campo eléctrico, aumentado aún más por la presencia de
irregularidades en la superficie del conductor (hebras, polvo, insectos, gotas de agua, etc.)
provoca la ionización del aire en su entorno inmediato: el aire pierde localmente su
propiedad dieléctrica, produciéndose gran cantidad de pequeñas descargas eléctricas en
la superficie del conductor. El efecto luminoso de estas descargas ha dado nombre a este
fenómeno, conociéndose como “corona”.

Dado que este fenómeno se genera por campo eléctrico, depende en consecuencia del
voltaje y su efecto será mayor a mayor nivel de voltaje. En este caso interesa en 220 kV.
En la referencia [9] se informa de medidas efectuadas en una subestación originalmente de
115 kV, después de su conversión a 230 kV, y también en una subestación regularmente
operando en 230 kV. Las medidas se tomaron en puntos del perímetro interior de las
subestaciones. La Figura 12 muestra la situación de la subestación que se convirtió a 230
kV y la Figura 13, la situación en la subestación convencional de 230 kV.

Figura 12. Radio interferencia en borde de subestación Pontchartrain a 230 kV [9]

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 17

Figura 13. Radio interferencia medida en los diferentes puntos del borde de la

subestación Snakefarm de 230 kV [9]

En ambos gráficos se ilustran valores medidos y se incluye en línea roja el valor límite
recomendado para radio interferencia emitida por líneas de transmisión de 220 kV que
corresponde a 53 [dB/1V/m] (decibeles sobre 1 micro Volt por metro)

Se concluye que en el caso de la subestación transformada, dos valores al interior de la
subestación superan levemente los 53 [dB/1V/m]; sin embargo, en el caso de la
subestación diseñada para el nivel 230 kV, el nivel de ruido máximo en el borde interior es
aproximadamente **50 [dB/1**  **V/m],** bajo el límite de 53 [dB/1V/m].

**4.5. Simulación**

La metodología utilizada consiste en una modelación de los conductores energizados de
las barras, utilizando elementos finitos y el software utilitario QuickField [1] para la solución
de campos. Considerando el emplazamiento del Proyecto, el resultado del estudio de
campo eléctrico y campo magnético se presenta en la forma de perfiles de campo evaluados
a una altura de 1,0 m sobre el suelo, a través de la trayectoria A1- A2 y la trayectoria B1B2 mostradas en la Figura a continuación; se escogió el perfil A1 - A2 a la salida de la línea
y el perfil B1 - B2 por atravesar la barras; mediante la información de ambos se tendrá el
efecto en los bordes de la subestación. En el perfil A1-A2, los conductores se consideraron
a una altura de 12 m sobre el suelo, con 3,5 m de separación entre los conductores de
fases.

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 18

Figura 14. Trayectorias seleccionadas para la simulación

A continuación, se muestra el resultado del cálculo del campo eléctrico y del campo
magnético en las trayectorias seleccionadas de la Figura 14. El resultado del cálculo en la
trayectoria A1 - A2 se presenta en Figura 15, Figura 16, Figura 17 y Figura 18. El resultado
del cálculo en la trayectoria B1 - B2 se muestra en Figura 19, Figura 20, Figura 21 y Figura
22. La línea transversal en las figuras indica la superficie del suelo. En los gráficos se indica
la posición horizontal relativa de los conductores y los bordes interiores de la subestación.

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 19

Figura 15. Distribución de equipotenciales eléctricas en trayectoria A1 - A2

Figura 16. Campo eléctrico a 1 m sobre el suelo en trayectoria A1 - A2

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 20

Figura 17. Distribución de equipotenciales magnéticas en trayectoria A1 - A2

Figura 18. Inducción magnética a 1 m sobre el suelo en trayectoria A1 - A2

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 21

Figura 19. Distribución de equipotenciales eléctricas en trayectoria B1 - B2

Figura 20. Campo eléctrico a 1 m sobre el suelo en trayectoria B1 - B2

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 22

Figura 21. Distribución de equipotenciales magnéticas en trayectoria B1 - B2

Figura 22. Inducción magnética a 1 m sobre el suelo en trayectoria B1 - B2

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 23

En la trayectoria A1 - A2, el campo eléctrico bajo los conductores de la línea alcanza 1.550
Volt/m, sin embargo, decae al alejarse de los conductores y en el borde más cercano de la
subestación, llega a **1.350 V/m.** En la misma trayectoria, la inducción magnética máxima es
8,4 micro Tesla, y **4,1 micro Tesla** en el borde más próximo de la subestación.

Por su parte, en la trayectoria B1 - B2, el campo eléctrico bajo los conductores de las barras
alcanza 1.650 Volt/m, y en el borde más cercano de la subestación, llega a **750 V/m.** En la
misma trayectoria, la inducción magnética máxima es 8,0 micro Tesla, y **2,9 micro Tesla**
en el borde más próximo de la subestación.

**5.** **Magnitud de Campos en línea de transmisión de 220 kV**

**5.1. Campo eléctrico de baja frecuencia**

Ocupando la metodología de elementos finitos 1], se evalúa el campo eléctrico en el
entorno de la línea de 220 kV, en dirección transversal a su eje y a un metro de altura sobre
el nivel del terreno, condiciones normalizadas. Se considera sistema equilibrado en voltajes
y se evalúa el campo en el centro del vano, es decir, considerando la flecha media. El detalle
del análisis se muestra a continuación para la estructura de suspensión. La línea transversal
en las figuras indica la superficie del suelo.

Figura 23. Modelo con elementos finitos de silueta de torre

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 24

Figura 24. Distribución de líneas equipotenciales eléctricas

Figura 25. Campo eléctrico a 1m sobre el suelo L=50 : eje de la línea

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 25

**5.2. Campo magnético de baja frecuencia**

Para este estudio se consideró sistema equilibrado en corrientes con 1.223 Amperes por
fase de cada línea de 220 kV, que equivale a una entrega de potencia máxima de 466 MVA
por circuito.

Figura 26. Distribución de líneas equipotenciales magnéticas

Figura 27. Inducción magnética 1m sobre el suelo; L=50 : eje de la línea

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 26

El resultado del análisis se sintetiza en la Tabla siguiente.

Tabla 7. Valores en borde de franja

|Situación|Campo eléctrico en borde de<br>franja<br>[V/m]|Inducción magnética en borde de<br>franja<br>[micro Tesla]|
|---|---|---|
|Estructura de Suspensión|545|0,76|

**5.3. Campo perturbador o Radio interferencia producida por la línea**

Mediante la aplicación del software LINEAS, que permite determinar gradiente en la
superficie de conductores de líneas de Alta Tensión y radio interferencia, se analiza la
disposición de conductores según la estructura de suspensión.

El listado de salida del programa se muestra a continuación:

|Fase|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|Numero de subconductores|1|1|1|1|1|1|
|Radio del subconductor (cm)|1.865|1.865|1.865|1.865|1.865|1.865|
|Posicion lateral del conductor (m)|-4.100|-4.300|-4.100|4.100|4.300|4.100|
|Altura conductor sobre el suelo (m)|34.000|28.500|23.000|34.000|28.500|23.000|

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 27

|Fase|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|RI [dB/1V/m]|24.26|26.60|27.71|25.88|28.79|30.48|
|E [V/m]|16.34|21.38|24.29|19.67|27.52|33.40|
|Efase [V/m]|25.57|34.85|41.30||||
|RI fase [dB/1V/m]|28.16|30.84|32.32||||
|RI línea [dB/1V/m]|33.08||||||

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 28

**6.** **Valores límites de recomendaciones internacionales**

**6.1. Valores límites recomendados de radio interferencia provocada por**

**instalaciones de alta tensión.**

En la referencia [3], se propone la siguiente recomendación para el límite de campo
electromagnético perturbador de alta frecuencia (radio interferencia) emitida por líneas de
transmisión y subestaciones, según su nivel de tensión:

Tabla 8. Valores de interferencia de radio recomendado por la Asociación de Normas

canadienses [3]

|Voltaje nominal entre fases|Nivel de Radio Interferencia|
|---|---|
|**(KV)**|**(dB/ 1μV/m)**|
|Menos de 70|43|
|70 - 200|49|
|200 - 300|53|
|400 - 600|60|
|Sobre 600|63|

Para líneas de transmisión, valores indicados a 15 m de la fase externa y a 0,5 MHz

Para subestaciones, valores medidos a 15 m del cerco del recinto de la subestación

Para una línea de transmisión o subestación de 220 kV, el valor límite corresponde a 53

[dB/1V/m].

**6.2. Normas de referencia aplicables en Chile respecto de la exposición humana a**

**campos electromagnéticos de 50 Hz**

En nuestro país no existe reglamentación relativa a los valores límites permitidos de
exposición de las personas a los campos electromagnéticos de frecuencia industrial. No
obstante, la regulación ambiental que rige el tema de emisiones señala que de no existir
una regulación nacional, debe aplicarse como norma de referencia aquella que se
encuentre vigente en estados específicos.

El Decreto No 40 del Ministerio del Medio Ambiente “Aprueba Reglamento del Sistema de
Evaluación de Impacto Ambiental”, publicado el 12-08-2013, y que entró en vigencia el 2412-2013, indica en su Artículo 11:

_Artículo 11.- Normas de referencia._

_Las normas de calidad ambiental y de emisión que se utilizarán como referencia para los_
_efectos de evaluar si se genera o presenta el riesgo indicado en la letra a) y los efectos_
_adversos señalados en la letra b), ambas del artículo 11 de la Ley, serán aquellas vigentes_
_en los siguientes Estados: República Federal de Alemania, República Argentina, Australia,_
_República Federativa del Brasil, Canadá, Reino de España, Estados Unidos Mexicanos,_
_Estados Unidos de América, Nueva Zelandia, Reino de los Países Bajos, República Italiana,_

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 29

_Japón, Reino de Suecia y Confederación Suiza. Para la utilización de las normas de_
_referencia, se priorizará aquel Estado que posea similitud en sus componentes ambientales,_
_con la situación nacional y/o local, lo que será justificado razonablemente por el proponente._

La tabla que se muestra a continuación presenta las principales normas de referencia
aplicables en Chile, de acuerdo a lo señalado en el Artículo anterior.

Tabla 9. Límites de exposición humana a campos electromagnéticos de 50 Hz

|País|Público general|Col3|Exposición ocupacional|Col5|
|---|---|---|---|---|
|**País**|**Campo**<br>**Eléctric**<br>**o **|**Campo**<br>**magnético**|**Campo**<br>**Eléctrico**|**Campo**<br>**magnético**|
|**País**|**[V/m]**|**[micro Tesla]**|**[V/m]**|**[micro Tesla]**|
|Alemania|5.000|100|5.000|100|
|Argentina|3.000|25|3.000|25|
|Australia|5.000|100|10.000 - 30.000|500|
|Canadá|No<br>existe|No existe|No existe|No existe|
|España|CEU|CEU|CEU|CEU|
|Italia|5.000|10|5.000|10|
|Japón|3.000|No existe|ICNIRP|ICNIRP|
|U.S.A.|2.000 -<br>11.800|15 - 20|2.000 - 11.800|15 - 20|
|Reino<br>de<br>los<br>Países<br>Bajos<br>(Gobierno)<br>(Consejo de Salud)|ICNIRP<br>8.000|ICNIRP<br>120|ICNIRP<br>40.000|ICNIRP<br>600|
|Suecia|No<br>explícito|No explícito|No explícito|No explícito|
|Suiza|5.000|100|5.000|10|
|ICNIRP|5.000|100|10.000|500|
|IEEE|5.000|904|20.000|2710|
|Consejo de Unión Europea (CEU)|5.000|100|10.000|500|

La recomendación de uso más frecuente para público general y exposición permanente, es
la publicada por la ICNIRP [2], organismo no gubernamental reconocido por la Organización
Mundial de la Salud como referente en el tema, que establece 5.000 [V/m] para el campo
eléctrico y 100 [micro Tesla] para la inducción magnética.

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 30

**7.** **Conclusiones**

De los resultados obtenidos en la investigación bibliográfica y en las simulaciones
efectuadas para estimación de la magnitud de los efectos provocados por la subestación y
la línea del Proyecto Fotovoltaico Elena, se concluye:

**7.1. Valores de campo eléctrico**

 La magnitud de campo eléctrico existente a un metro de altura sobre el suelo en el
borde inmediato de la subestación de 220 kV, se estima no supera **1.350 [V/m]** de
acuerdo a cálculos de publicaciones internacionales y simulaciones conforme a las

distancia reales.

 En el caso de la línea de 220 kV, en el borde de la franja se obtiene un valor de
campo eléctrico de **545 [V/m]**

Estos valores son inferiores al límite de **5.000 [V/m]** recomendado por la ICNIRP [2] y
considerado internacionalmente como seguro para las personas.

**7.2. Valores de inducción magnética**

 La magnitud de inducción magnética a un metro de altura sobre el suelo en el borde
de la subestación es inferior a **4,1 micro Tesla** según medidas nacionales y
simulación.

 - En el borde de la franja de seguridad de la línea, se obtiene una magnitud de **0,76**
**micro Tesla.**

Estos valores son inferiores al límite de **100 micro Tesla** propuesto por la ICNIRP [2] y
considerado internacionalmente como seguro para las personas.

**7.3. Valor de radio interferencia**

 El máximo ruido de radio frecuencia (interferencia a las señales de radio y televisión)
generado por una subestación de 220 kV, es de **50 [dB/1**  **V/m]** en el borde interior
de la subestación.

 - El valor estimado de acuerdo a norma [3] (15 m de distancia lateral del conductor
externo, 0,5 MHz) para la línea de 2 x 220 kV, mediante modelo de cargas para los
conductores de la línea y cálculo de gradiente superficial, alcanza **33,08 [dB**
**/1**  **V/m].** Considerando eventualmente lluvia intensa, situación poco probable dada
la situación geográfica de las instalaciones, el valor ascendería a **50,08 [dB /1**  **V/m].**

Estos valores son inferiores al límite de **53 [dB/1**  **V/m]** considerado máximo permitido por
la normativa canadiense, a 15 m del cerco del recinto de la subestación.

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 31

**8.** **Bibliografía y Referencias**

[1] Students' QuickField (TM) Finite Element Analysis System
[Tera Analysis Company www.quickField.com](http://www.quickfield.com/)

2 IRPA International Radiation Protection Association
International Non-ionizing Radiation Committe : “ICNIRP Guidelines for limiting

‐
exposure to time varying electric, magnetic and electromagnetic fields (up to 300
ghz)”

‐
Health Physics 74 (4):494 522; 1998

[3] Association canadienne de normalisation, « Valeurs limites et methods de mesure
du bruit électromagnétique (0,15 à 30 MHz) produit par les reseaux de courant
alternatif ». CAN3- C108.3.1 - M84. Octobre 1984.

[4] Informe medidas efectuadas en S/E ANDES de 345/220 kV de AES Gener.
Departamento de Ingeniería Eléctrica, Universidad de Chile, 2008.

[5] [Sayed A. Word, Samy M. Ghania](http://scialert.net/asci/author.php?author=Sayed&last=A.%20Word) [and Essam M. Shaalan](http://scialert.net/asci/author.php?author=Essam&last=M.%20Shaalan)
Analysis of Electric Field inside HV Substations using Charge simulation method in
three dimensional
Department of Electrical Engineering - Benha University - Cairo, Egypt.
2010 Annual Report Conference on Electrical Insulation and Dielectric Phenomena

[6] Magnetic Field Measurement & Simulation of A 230 kV Substation
I.O. Habiballah, M.M. Dawoud, K. Al-Balawi, A.S. Farag * KFUPM, Dhahran, Saudi
Arabia,* Universiti Tenaga Nasional, Malaysia
[e-mail: ibrahimh@kfupm.edu.sa](mailto:ibrahimh@kfupm.edu.sa)
Proceedings of the International Conference on Non-Ionizing Radiation at UNITEN
(ICNIR 2003) Electromagnetic Fields and Our Health 20 th-22 nd October 2003

[8] Modeling and calculation of electromagnetic field in the surroundings of a large power
transformer
Leonardo ˇSTRAC, Franjo KELEMEN, Damir ˇZARKO
Turk J Elec Eng & Comp Sci, Vol.17, No.3, 2009,

[9] CARTER R. T. ; GRILLE A. W. ; BAZILE G. M. ; PERKINS M. D. ; MAUSER S. F. ;
Analysis of radio interference and substation modifications for uprating a 115-KV
substation to 230 KV
IEEE transactions on Power Delivery (IEEE Trans. Power Deliv.) 1987, vol. 2, no2,
pp. 544-550

Declaración de Impacto Ambiental Anexo 6 Estudio de campos electromagnéticos

Proyecto Fotovoltaico Elena 32

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Características principales de transformadores de nivel intermedio**

| Tipo: | 3 fases / 50 Hz |
| --- | --- |
| Potencia: | 3.500 kVA |
| Número de bobinados trifásicos: | 2 (1 MT, 1 BT) |
| Tensión primaria (MT): | 33 kV ±2,5%±5% |
| Tensión secundaria (BT): | 420 V |
| Estándar: | IEC60076 |
| Entorno: | Exterior |
| Temperatura ambiente: | máxima 50 oC |
| Altura de uso máx.: | ≤3.000 m sobre el nivel del mar |

**Tabla 2.: Características de transformadores**

| Tipo de servicio | Continuo/Exterior |
| --- | --- |
| Refrigeración | ONAN/ONAF |
| Potencia nominal | 224/112/112 MVA |
| Relación de transformación: |  |
| Primario | 220 ± 10 x 1,25kV (Regulación en carga) |
| Secundario | 33 kV |
| Frecuencia | 50 Hz |
| Conexión primario | Estrella |
| Conexión secundarios | Triangulo |
| Grupo de conexión | YNd11d11 |
| Tensión de cortocircuito para relación 220/33 kV | 14,0% |
| Tensión de cortocircuito entre devanados de 33 kV | 28,0% |

**Tabla 4.: Características Línea de Alta Tensión**

| Característica | Magnitud | Unidad |
| --- | --- | --- |
| Potencia máxima de transporte por circuito | 466 | MW |
| Potencia máxima de la línea | 2 x 466 | MW |
| Número de vértices | 11 | Unidades |

**Tabla 5.: Características conductores**

| Característica | Magnitud | Unidad |
| --- | --- | --- |
| Composición | 61/4,15 | mm |
| Diámetro del cable completo | 37,30 | mm |
| Sección total | 825,0 | mm2 |
| Peso | 2,230 | daN/m |
| Carga de rotura | 25.986 | daN |
| Módulo de elasticidad | 5.586 | daN/mm2 |
| Coeficiente de dilatación lineal | 23 x 10-6 | oC-1 |
| Resistencia eléctrica a 20oC | 0,0407 | Ω/Km |

**Tabla 6.: Características cable de guardia con fibra óptica (OPGW)**

| Característica | Magnitud | Unidad |
| --- | --- | --- |
| Máximo de fibras | 24 | Unidades |

**Tabla 7.: Valores en borde de franja**

| Situación | Campo eléctrico en borde de<br>franja<br>[V/m] | Inducción magnética en borde de<br>franja<br>[micro Tesla] |
| --- | --- | --- |
| Estructura de Suspensión | 545 | 0,76 |

**Tabla 8.: Valores de interferencia de radio recomendado por la Asociación de Normas**

| Voltaje nominal entre fases | Nivel de Radio Interferencia |
| --- | --- |
| **(KV)** | **(dB/ 1μV/m)** |
| Menos de 70 | 43 |
| 70 - 200 | 49 |
| 200 - 300 | 53 |
| 400 - 600 | 60 |
| Sobre 600 | 63 |

**Tabla 9.: Límites de exposición humana a campos electromagnéticos de 50 Hz**

| País | Público general | Col3 | Exposición ocupacional | Col5 |
| --- | --- | --- | --- | --- |
| **País** | **Campo**<br>**Eléctric**<br>**o ** | **Campo**<br>**magnético** | **Campo**<br>**Eléctrico** | **Campo**<br>**magnético** |
| **País** | **[V/m]** | **[micro Tesla]** | **[V/m]** | **[micro Tesla]** |
| Alemania | 5.000 | 100 | 5.000 | 100 |
| Argentina | 3.000 | 25 | 3.000 | 25 |
| Australia | 5.000 | 100 | 10.000 - 30.000 | 500 |
| Canadá | No<br>existe | No existe | No existe | No existe |
| España | CEU | CEU | CEU | CEU |
| Italia | 5.000 | 10 | 5.000 | 10 |
| Japón | 3.000 | No existe | ICNIRP | ICNIRP |
| U.S.A. | 2.000 -<br>11.800 | 15 - 20 | 2.000 - 11.800 | 15 - 20 |
| Reino<br>de<br>los<br>Países<br>Bajos<br>(Gobierno)<br>(Consejo de Salud) | ICNIRP<br>8.000 | ICNIRP<br>120 | ICNIRP<br>40.000 | ICNIRP<br>600 |
| Suecia | No<br>explícito | No explícito | No explícito | No explícito |
| Suiza | 5.000 | 100 | 5.000 | 10 |
| ICNIRP | 5.000 | 100 | 10.000 | 500 |
| IEEE | 5.000 | 904 | 20.000 | 2710 |
| Consejo de Unión Europea (CEU) | 5.000 | 100 | 10.000 | 500 |
