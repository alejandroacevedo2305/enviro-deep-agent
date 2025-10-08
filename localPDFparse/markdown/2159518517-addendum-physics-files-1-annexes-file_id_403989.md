---
title: Sin título
author: Víctor Benavides
date: D:20231205215159-03'00'
language: es
type: report
pages: 40
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Informe técnico levantamiento topográfico.
  - Índice de Contenidos
-->

# Informe técnico levantamiento topográfico.

### “Levantamiento con sistema Lidar terrestre y batimetría CMPC”

/12/2023
### Departamento de geomática ENLACE RED

1

# Índice de Contenidos

1. Generalidades. 2

2. Definiciones. 5

3. Instrumental utilizado. 6

3.1 Sistema Receptor GNSS. 6

3.2 Sistema Lidar Terrestre. 7

4. Metodología utilizada. 10

4.1 Levantamiento Lidar: Metodología Móvil y Estática. 11

4.2 Georreferenciación: Integración de Metodologías Estáticas y Móviles. 11

4.3 Integración de Metodologías: 12

4.4 Procesamiento nube de puntos de ambas metodologías (Móvil y Estática). 12

5. Antecedentes 15

5.1 Ficha BN13 15

5.2 Certificado IGM BN13 16

5.3 Vértice Georreferenciado (Base) 17

5.4 Informe de Procesamiento Línea Base (Sector Tranque y Canal Sur) 17

5.5 Coordenadas RTK de cambios de posición (Sector Tranque). 20

5.6 Coordenadas RTK de cambios de posición (Sector Canal Sur) 21

5.7 Coordenadas RTK de cambios de posición (Sector La Descarga) 22

5.8 Levantamiento móvil 23

5.9 Informe de Procesamiento Línea Base (Sector La Descarga) 23

5.10 Procesamineto de trayectoria 25

5.11 Error RMS 27

5.12 Base Carburera 1 28

5.13 Informe de Procesamiento Línea Base (Sector La Carburera 1) 28

5.14 Coordenadas RTK de cambios de posición (Sector Carburera 1) 30

5.15 Base Carburera 2 32

5.16 Informe de Procesamiento Línea Base (Sector La Carburera 2) 32

5.17 Coordenadas RTK de cambios de posición (Sector Carburera 2) 34

5.18 Base Las Vertientes 36

5.19 Informe de Procesamiento Línea Base (Sector Las Vertientes) 36

5.20 Coordenadas RTK de cambios de posición (Sector Las vertientes) 38

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

2

## 1. Generalidades.

El presente informe detalla exhaustivamente los alcances y métodos técnicos empleados
durante la realización de un meticuloso levantamiento topográfico y batimétrico. Este
estudio abarca varias áreas clave del canal Eyzaguirre y Tranque Peralillo, situados
dentro de la Compañía Manufacturera de Papeles y Cartones (CMPC), así como
diversos sectores del Río Maipo. El levantamiento se divide en tres zonas principales:
La Descarga, Carburera y San Carlos, todas ubicadas en la comuna de Puente Alto,
perteneciente a la Región Metropolitana. Este trabajo fue encargado específicamente
por la empresa CMPC y se llevó a cabo con el objetivo de obtener una comprensión
detallada y precisa de estas áreas geográficas clave.

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

3

Figura 1.1 - Primer Sector del levantamiento CMPC

Figura 1.2 - Primer Sector del levantamiento (La Descarga, Rio Maipo)

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

4

Figura 1.3 - Primer Sector del levantamiento (Las Vertientes, Rio Maipo)

Figura 1.4 - Primer Sector del levantamiento (Carburera, Rio Maipo)

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

5

## 2. Definiciones.

 - Sistema Lidar: (Detección por luz y distancia): Es un sistema láser que permite
medir la distancia entre el punto de emisión de ese láser hasta un objeto o
superficie. El tiempo que tarda ese láser en llegar a su objetivo y volver del
mismo, es lo que nos dice la distancia entre los dos puntos. El resultado es que
se puede obtener un mapa en 3D de alta resolución para conocer el terreno en
cuestión.

 - Sistema Lidar Terrestre: Sistema utilizado para realizar proceso de
levantamiento, visualización, medición y generación de información geoespacial.
El equipo este compuesto por la integración de georreceptores GNSS, cámaras,
fotográficas digitales de alta gama, unidad de movimiento inercial, sensor Lidar
de alto rendimiento y sistema computacionales a bordo del vehículo. La
sincronización de todos esto dispositivos permite la obtención de información
geoespacial en grandes volúmenes, a gran velocidad y con alta precisión. Este
sistema está desarrollado para obtener máxima productividad en trabajos que
abarquen rutas longitudinales grandes y en tiempos muy cortos de operación.
Manual de carretera V2 2.304.403

 - Sistema GNSS: Sistema global de navegación por satélite es una constelación de
satélites que transmite rangos de señales utilizados para el posicionamiento y
localización en cualquier parte del globo terrestre, ya sea en tierra, mar o aire.

 Receptor GNSS: Los receptores GNSS son la interfaz de usuario a cualquier
Sistema Global de Navegación por Satélite (GNSS) y su objetivo es procesar las
Señales En el Espacio (SIS) transmitidas por los satélites. La mayoría de ellos
se basan en soluciones de navegación del receptor que proporcionan posición,
velocidad y tiempo.

Las características principales de los receptores GNSS son:

 Tipo y constelación que se recibe

 Precisión de medida (Estático, Cinemático, RTK, Diferencial o SBAS)

 Disponibilidad o no de telefonía integrada

 Vértice o punto geodésico : es un punto señalizado que indica una posición
geográfica exacta conformando una red de triangulación con otros vértices
geodésicos.

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

6

## 3. Instrumental utilizado.

3.1 Sistema Receptor GNSS.

Sistema GPS RTK L1/L2 Trimble R8s

Precisión horizontal.

Posicionamiento GNSS de código diferencial Horizontal ...0,25 m + 1 ppm RMS
Vertical ...................................................................................0,50 m + 1 ppm RMS
Precisión de posicionamiento SBAS diferencial .....................típico <5 m 3DRMS

Medición Estática

GNSS Estática de alta precisión Horizontal ........................3 mm + 0,1 ppm RMS
Vertical ...............................................................................3,5 mm + 0,4 ppm RMS
Estática y Estática Rápida Horizontal .................................3 mm + 0,5 ppm RMS
Vertical ..................................................................................5 mm + 0,5 ppm RMS

Medición GNSS Cinemática con Post-procesamiento PPK

Horizontal ...............................................8 mm + 1 ppm RMS
Vertical ..................................................15 mm + 1 ppm RMS

Medición Cinemática en tiempo real .

línea base individual <30 km Horizontal ..........................8 mm + 1 ppm RMS
Vertical ..............................................................................15 mm + 1 ppm RMS
RED RTK3 Horizontal .....................................................8 mm + 0,5 ppm RMS
Vertical ...........................................................................15 mm + 0,5 ppm RMS

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

7

3.2 Sistema Lidar Terrestre.

 Configuración Avanzada del Sistema:
El procedimiento para el levantamiento topográfico con la metodología móvil inicia con
una meticulosa configuración del sistema, utilizando el avanzado escáner LiDAR
RIEGL VZ-400i. Este equipo se monta cuidadosamente en un vehículo especialmente
adaptado, asegurando su total estabilidad durante la movilización. La integración
precisa de un receptor GNSS en el vehículo, en perfecta sincronización con el escáner
LiDAR, es esencial para garantizar una georreferenciación exacta y confiable de todos
los datos recolectados.

 Proceso Innovador de Adquisición de Datos en Movimiento:
En el transcurso del levantamiento, el escáner LiDAR RIEGL VZ-400i, dotado de
tecnología puntera de pulsos láser, realiza mediciones de distancias con una precisión
extraordinaria a nivel milimétrico. Paralelamente, una cámara fotográfica integrada
captura imágenes detalladas del entorno circundante. Esta adquisición de datos en
tiempo real facilita la creación de una nube de puntos tridimensional, reflejando
fielmente la topografía y las características físicas del terreno analizado.

 Georreferenciación Dinámica y Precisa:
La metodología móvil se enriquece con la capacidad del sistema de ejecutar una
georreferenciación dinámica eficiente. Esto se logra mediante el uso del receptor GNSS,
que determina con exactitud la posición del escáner en tiempo real. La información
recabada se integra sin fisuras al sistema de coordenadas geodésicas, proporcionando
un marco de referencia detallado y preciso para los datos capturados durante el
movimiento.

 Cumplimiento Riguroso de Normativas:
Es crucial subrayar que este proceso se lleva a cabo en estricta conformidad con las
normativas actuales, particularmente siguiendo las directrices del MC Vol2 V2
2.304.403. Este cumplimiento normativo es un pilar fundamental para asegurar la
calidad superior y la total fiabilidad de los datos obtenidos mediante el levantamiento
topográfico y la metodología móvil con el escáner LiDAR RIEGL VZ-400i..

Figura 3.1 - Sistema escáner móvil terrestre

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

8

Método Estático del Escáner LIDAR Fijo RIEGL VZ-400i:

 Posicionamiento y Configuración:
La metodología estática del escáner LIDAR RIEGL VZ-400i implica una instalación fija
en un punto estratégico de interés. El proceso comienza con la cuidadosa selección del
sitio, asegurando una posición que permita la captura óptima de datos. Una vez
posicionado, se procede a la configuración del escáner, garantizando su nivelación y
calibración adecuadas para maximizar la precisión en la adquisición de datos.

 Captura de Datos de Alta Precisión:
Con el escáner en posición estática, se inicia la captura de datos. El escáner LIDAR
RIEGL VZ-400i utiliza su tecnología de pulsos láser de alta frecuencia para realizar
mediciones extremadamente precisas de la topografía circundante. La velocidad y
exactitud de estas mediciones permiten la creación de una nube de puntos
tridimensional detallada y altamente precisa.

 Integración de GNSS para Georreferenciación:
Para garantizar la georreferenciación precisa de los datos, se integra un receptor GNSS
al escáner LIDAR. Este receptor se conecta al sistema de coordenadas geodésicas,
permitiendo la asociación exacta de cada punto capturado con su posición geográfica.
La precisión de esta integración es esencial para la coherencia y utilidad de los datos
en aplicaciones geoespaciales.

 - Evaluación de Intensidad de Retorno del Punto:
El escáner LIDAR RIEGL VZ-400i no solo mide la distancia de cada punto, sino que
también evalúa la intensidad del retorno láser. Este dato adicional proporciona
información sobre las características reflectivas de la superficie, permitiendo una
mayor comprensión y clasificación de los objetos y terrenos capturados.

 Validación Normativa y Calidad del Datos:
La metodología estática del escáner LIDAR RIEGL VZ-400i se ejecuta en conformidad
con las normativas establecidas, en este caso, siguiendo las directrices del MC Vol2
2.302.2. La validación normativa asegura la calidad y coherencia de los datos,
cumpliendo con estándares rigurosos y garantizando la fiabilidad de la información
capturada mediante este método.

Figura 3.2 - Sistema escáner estático

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

9

3.3 **Batimetría con HyDrone Seafloor.**

 El HyDrone Seafloor es un vehículo no tripulado de superficie (USV, por sus
siglas en inglés) diseñado específicamente para tareas de levantamiento
hidrográfico y batimétrico. Este USV es conocido por su versatilidad y eficacia
en la recopilación de datos en cuerpos de agua como lagos, ríos, y áreas costeras.
A continuación, se presentan algunas características y capacidades clave del
HyDrone Seafloor:

 - Diseño y Estructura:
El HyDrone Seafloor suele ser compacto y portátil, lo que facilita su transporte y
despliegue en diferentes ubicaciones. Su diseño robusto lo hace apto para operar en
diversas condiciones ambientales.

 Tecnología de Sensores y Equipamiento:
Este USV está equipado con tecnología avanzada de sensores, incluyendo ecosondas y
sonares, que permiten realizar mediciones precisas de la profundidad y la topografía
del lecho marino. Algunos modelos pueden incorporar GPS de alta precisión y otros
instrumentos para la recopilación de datos geoespaciales.

 Control y Navegación:
El HyDrone Seafloor puede ser controlado de manera remota, lo que permite a los
operadores dirigirlo y recopilar datos desde una ubicación segura. Esto es
particularmente útil en áreas inaccesibles o peligrosas.

 Aplicaciones en Levantamientos Hidrográficos:
Es ampliamente utilizado para realizar levantamientos hidrográficos en proyectos de
ingeniería, estudios ambientales, y en la gestión de recursos hídricos. Su capacidad para
recopilar datos detallados del fondo marino lo hace indispensable en la cartografía y en
la planificación de proyectos submarinos.

Figura 3.3 - HyDrone Seafloor

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

10

## 4. Metodología utilizada.

4.1 Batimetria

El levantamiento batimétrico con el HyDrone Seafloor de un tranque se realizó
siguiendo varios pasos y consideraciones técnicas clave:

 Preparación y Planificación:
Inspección del Sitio: Inicialmente, se llevó a cabo una inspección del tranque para
identificar posibles obstáculos y áreas de interés.

 - Planificación de la Misión:
Se establecieron las trayectorias de navegación del HyDrone Seafloor, definiendo líneas
de sondeo y puntos de inicio y finalización.

 - Montaje de Equipos:
Se instalaron y calibraron equipos como ecosondas y GPS en el HyDrone Seafloor.

 - Verificación del Sistema:
Se verificó el correcto funcionamiento de todos los sistemas y equipos del USV antes de
su despliegue en el agua.

 Despliegue y Operación:
Lanzamiento del HyDrone: El HyDrone Seafloor fue colocado en el agua y comenzó la
navegación siguiendo las líneas de sondeo preestablecidas.

 - Recolección de Datos:
Durante la navegación, el USV recopiló datos batimétricos, midiendo la profundidad
del agua y registrando características del lecho del tranque.
Monitoreo y Control Remoto:

 Control y Supervisión:
Los operadores, desde un punto de control en tierra, supervisaron y controlaron el
HyDrone Seafloor, ajustando su ruta según fuera necesario.
Procesamiento de Datos:

 Descarga y Análisis:
Una vez completado el levantamiento, los datos recogidos fueron descargados y
procesados utilizando software especializado.

 Interpretación de Datos:
Se analizaron los datos procesados para interpretar características del lecho del
tranque.

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

11

Figura 4.1 - Batimetria Tranque Peralillo.

4.2 Levantamiento Lidar: Metodología Móvil y Estática.

En esta fase, se implementa una combinación de metodologías móvil y estática para
llevar a cabo el levantamiento Lidar. Se procede instalando un receptor GNSS en uno
de los monolitos del proyecto, utilizando el vértice activo del Ministerio de Bienes
Nacionales. Posteriormente, se desplaza un sistema Lidar móvil montado en un
vehículo a lo largo de la ruta designada. Conforme avanza, el sistema captura
información geoespacial mediante la medición de distancias y la obtención de imágenes
a través de su cámara fotográfica. Es importante destacar que este método se encuentra
validado de acuerdo con la normativa vigente (MC Vol2 V2 2.304.403).

4.3 Georreferenciación: Integración de Metodologías Estáticas y Móviles.

La georreferenciación de los vértices del proyecto se lleva a cabo mediante un sistema
de receptores GNSS RTK. Este sistema permite vincular el proyecto a la red geodésica
nacional, siguiendo las directrices establecidas por la normativa vigente (MC Vol2
2.302.2). Con este propósito, se instalan receptores en un monolito de la red nacional y
otro conectado al escáner láser, posibilitando la adquisición de coordenadas precisas de
cada estación en tiempo real. En esta instancia, se utiliza el vértice geodésico del
Ministerio de Bienes Nacionales denominado BN13 . Esta integración de metodologías
estáticas y móviles garantiza una georreferenciación precisa y conforme a los
estándares normativos establecidos.

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

12

4.4 Integración de Metodologías:

La integración eficiente de ambas metodologías permite a los profesionales maximizar
la utilidad del escáner LIDAR RIEGL VZ-400i. La flexibilidad proporcionada por estos
enfoques complementarios asegura que el proceso técnico se adapte de manera óptima
a la naturaleza y objetivos específicos de cada proyecto. El escáner LIDAR RIEGL VZ400i, respaldado por su capacidad técnica avanzada, se posiciona como una herramienta
integral para la captura de datos geoespaciales, brindando resultados precisos y
detallados en diversos entornos y aplicaciones.

Figura 4.2 - Coordenadas UTM vértice HUSO 19.

4.5 Procesamiento nube de puntos de ambas metodologías (Móvil y Estática).

Metodologías de Captura de Datos:

 Utilización de escáner LIDAR fijo RIEGL VZ-400i para captura de datos.

 Metodología móvil: desplazamiento en vehículo.

 Metodología estática: instalación fija para alta precisión.

Procesamiento con POSPac:

 Procesamiento previo con POSPac para ajuste de la trayectoria de los
levantamientos móviles.

 Asegura una georreferenciación precisa y alineación de datos de la metodología
móvil.

Procesamiento con RiPROCESS:

 Aplicación de RiPROCESS para el post procesamiento de los levantamientos
móviles.

 Garantiza la calidad, precisión y consistencia de los datos procesados.

Procesamiento con RiSCAN Pro:

 Utilización de RiSCAN Pro para el procesamiento de levantamientos estáticos.

 Permite la organización eficiente de datos y asegura su calidad antes de la
integración.

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

13

Carga de Nubes Procesadas en TBC:

 Las nubes de puntos procesadas tanto por RiPROCESS como por RiSCAN Pro
se cargan en Trimble Business Center (TBC).

 TBC facilita el manejo y análisis eficiente de grandes conjuntos de datos.

Generación de Superficies en TBC:

 Utilización de las nubes de puntos procesadas en TBC para la generación de
superficies detalladas.

 El objetivo es crear modelos 3D de alta calidad que representen con precisión el
terreno capturado por ambas metodologías.

Análisis Topográfico Detallado:

 Las superficies modeladas en TBC se utilizan para análisis topográficos
detallados.

 Aplicaciones en ingeniería civil, arquitectura y otros campos que requieren
representaciones precisas del terreno.

El objetivo principal es realizar el modelamiento de la nube de puntos con ambas
metodologías utilizadas (móvil y estático) en esta etapa se generaron la nube de puntos,
las que se exportaron con el sistema de coordenadas UTM WGS84 Sistema Geoidal
EGM 2008, zona 19 Sur.
El resultado es la generación de superficies de calidad que sirven como base para
estudio de análisis en diversos campos.

Figura 4.3 - Nube de puntos

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

14

Figura 4.4 - Definición de nube de puntos

Figura 4.5 - Superficie LandXML

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

15

## 5. Antecedentes

5.1 Ficha BN13

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

16

5.2 Certificado IGM BN13

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

17

5.3 Vértice Georreferenciado (Base)

5.4 Informe de Procesamiento Línea Base (Sector Tranque y Canal Sur)

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

18

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

19

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

20

5.5 Coordenadas RTK de cambios de posición (Sector Tranque).

Figura 5.1 - Imagen Georreferenciada con cambios de posición en levantamiento LIDAR RTK

(Sector Tranque).

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

21

5.6 Coordenadas RTK de cambios de posición (Sector Canal Sur)

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

22

Figura 5.2 - Imagen Georreferenciada con cambios de posición en levantamiento LIDAR RTK

(Sector Canal Sur).

5.7 Coordenadas RTK de cambios de posición (Sector La Descarga)

Figura 5.3 - Imagen Georreferenciada con cambios de posición en levantamiento LIDAR RTK

(Sector La Descarga).

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

23

5.8 Levantamiento móvil
Vértice Georreferenciado (Sector La Descarga)

5.9 Informe de Procesamiento Línea Base (Sector La Descarga)

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

24

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

25

5.10 Procesamineto de trayectoria

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

26

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

27

5.11 Error RMS

Figura 5.4 - Imagen Georreferenciada con levantamiento Estático y Móvil (Sector La

Descarga).

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

28

5.12 Base Carburera 1

5.13 Informe de Procesamiento Línea Base (Sector La Carburera 1)

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

29

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

30

5.14 Coordenadas RTK de cambios de posición (Sector Carburera 1)

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

31

Figura 5.5 - Imagen Georreferenciada con cambios de posición en levantamiento LIDAR RTK

(Sector Carburera 1).

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

32

5.15 Base Carburera 2

5.16 Informe de Procesamiento Línea Base (Sector La Carburera 2)

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

33

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

34

5.17 Coordenadas RTK de cambios de posición (Sector Carburera 2)

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

35

Figura 5.6 - Imagen Georreferenciada con cambios de posición en levantamiento LIDAR RTK

(Sector Carburera 2).

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

36

5.18 Base Las Vertientes

5.19 Informe de Procesamiento Línea Base (Sector Las Vertientes)

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

37

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

38

5.20 Coordenadas RTK de cambios de posición (Sector Las vertientes)

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)

39

Figura 5.7 - Imagen Georreferenciada con cambios de posición en levantamiento LIDAR RTK

(Sector Las Vertientes).

[Enlace Red Ltda. Puyehue N°1401, Providencia. Fono:02-24245670 - Contactos@enlacered.cl](mailto:Contactos@enlacered.cl)