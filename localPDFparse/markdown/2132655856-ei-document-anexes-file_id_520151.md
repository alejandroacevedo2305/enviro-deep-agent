---
title: Tipo de Informe o Capítulo
author: Catalina Sandoval
date: D:20170811130451-04'00'
language: es
type: report
pages: 67
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Anexo 2.4: Análisis de suspensión de sedimentos
-->

# Anexo 2.4: Análisis de suspensión de sedimentos

## Adecuación Planta Desaladora RT Sulfuros

#### Región de Antofagasta

Agosto, 2017

Elaborado por:

**Gestión Ambiental Consultores S.A.**

Padre Mariano 103 of. 307, Providencia

Fono: +56 2 2719 5600

www.gac.cl

**DEPARTAMENTO DE OCEANOGRAFÍA FÍSICA Y MODELAMIENTO NUMÉRICO**

##### INFORME TÉCNICO

#### _ANÁLISIS DE SUSPENSIÓN DE SEDIMENTOS_ _SUBMAREALES DURANTE CONSTRUCCION DE_ _OBRAS MARÍTIMAS EN EL PROYECTO_ _“EXPLOTACIÓN DE SULFUROS RADOMIRO TOMIC_ _FASE II, TOCOPILLA, REGIÓN DE ANTOFAGASTA”_

**Preparado por:**

**SEPTIEMBRE 2015**

**MODELACIÓN NUMÉRICA**

Suspensión de sedimentos Km 14

**DEPARTAMENTO DE OCEANOGRAFÍA FÍSICA Y MODELAMIENTO NUMÉRICO**

### Solicitado por:
#### Consorcio INIMA - CVV

###### Casa Central

Presidente Riesco 5561,

Of. 1804, Las Condes

Santiago, Chile
Teléfonos: (56-2) 221-35001

### Elaborado por:
#### EcoTecnosS.A.

###### Casa Central

Limache 3405 Oficina 31, Viña del Mar

Fonos 56 32 2189200

info@neotecnos.cl

**Control de Documentos**

|Control de Documentos|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**Versión**|**Autor**|**Revisión**|**Aprobación**|**Fecha**|
|B|MQL|MQL|MQL|11.09.15|
|A|MQL|MHA|MHA|12.09.15|
|O|MQL|MHA|AA|14.09.15|

B: Emitido para revisión interna
A: Emitido para aprobación del cliente
0: Aprobado

**MODELACIÓN NUMÉRICA**

Suspensión de sedimentos Km 14

**DEPARTAMENTO DE OCEANOGRAFÍA FÍSICA Y MODELAMIENTO NUMÉRICO**

#### Profesionales Responsables
##### EcoTecnosS.A.

**Departamento de Oceanografía Física y Modelamiento Matemático**

##### Prof. Dr. Humberto Díaz O.

Dr. en Ingeniería mención Biotecnología

##### Ing. Sr. Matías Quezada L.

Ingeniero Civil Oceánico, Diploma en Ingeniería Marítima

##### Ing. Srta. Pía Monreal D.

Ingeniero Civil Oceánico

##### Abog. Sr. Mario Herrera A.

Derecho Ambiental y Marítimo - Edición y Coordinación

**MODELACIÓN NUMÉRICA**

Suspensión de sedimentos Km 14

**DEPARTAMENTO DE OCEANOGRAFÍA FÍSICA Y MODELAMIENTO NUMÉRICO**

**ECOTECNOS S.A.**

Calle Limache N°3405, Oficina 31

Edificio Reitz de las Empresas
El Salto, Viña del Mar, Chile

Este documento ha sido elaborado por la empresa EcoTecnos S.A. a requerimiento de INIMA CVV,
por mandato de Codelco VP, por lo que solamente puede ser utilizado y reproducido con expresa
autorización de esta última empresa, quedando terminantemente prohibido su copia, reproducción
total o parcial de él, ya que la información contenida en este documento se encuentra protegida,
entre otras normas, por la Ley N° 17.336 sobre Propiedad Intelectual, publicada en el Diario Oficial

N° 27.761, de 2 de octubre de 1970.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|5|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**ÍNDICE DE CONTENIDOS**

**1** **INTRODUCCIÓN ........................................................................................ 9**

**2** **OBJETIVOS ............................................................................................. 11**

**3** **REFERENCIAS ........................................................................................ 11**

**4** **MATERIALES Y MÉTODOS .................................................................... 12**

4.1 MATERIALES ........................................................................................... 12

_4.1.1_ _Descripción del modelo numérico CMS-WAVE ......................................... 13_
_4.1.2_ _Descripción del modelo numérico CMS-FLOW ......................................... 16_
_4.1.3_ _Descripción del modelo numérico PTM ..................................................... 18_
4.2 METODOLOGÍA ....................................................................................... 21

_4.2.1_ _Calibración y validación de los modelos numéricos................................... 21_
_4.2.2_ _Modelación numérica de la suspensión ..................................................... 27_
_4.2.3_ _Descripción de los métodos de escritorio implementados ......................... 29_

**5** **RESULTADOS ......................................................................................... 31**
5.1 CALIBRACIÓN DEL MODELO NUMÉRICO DE OLEAJE ......................... 31

_5.1.1_ _Sedimentos ............................................................................................... 31_
5.2 CALIBRACIÓN DEL MODELO NUMÉRICO HIDRODINÁMICO ............... 34

_5.2.1_ _Calibración del nivel del mar ..................................................................... 34_

_5.2.2_ _Calibración de las corrientes ..................................................................... 38_
5.3 MODELACION NUMÉRICA DE LA SUSPENSION DE SEDIMENTOS ..... 50

_5.3.1_ _Cantidad de sedimentos en suspensión .................................................... 50_
_5.3.2_ _Caracterización de los ciclos diarios ......................................................... 51_

_5.3.3_ _Dispersión de sedimentos en las zanjas de excavación ............................ 55_

**6** **CONCLUSIONES ..................................................................................... 65**
6.1 CON RESPECTO DE LAS HERRAMIENTAS NUMÉRICAS Y MÉTODOS

APLICADOS ............................................................................................. 65
6.2 CON RESPECTO DE LA FASE DE CONSTRUCCIÓN DE LAS OBRAS

MARITIMAS .............................................................................................. 65

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|6|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**LISTADO DE FIGURAS**

Figura 4.1: Aplicación de los modelos CMS-WAVE y CMS-FLOW. ................................................. 13

Figura 4.2: Diagrama de flujo de aplicación del modelo PTM. ......................................................... 19

Figura 4.3: Esquema estimación del oleaje para la caracterización hidrodinámica del sector de

estudio. .............................................................................................................................................. 22

Figura 4.4: Dominio numérico empleado para resolver el oleaje. ..................................................... 23

Figura 4.5: Extensión de la grilla numérica empleada para la modelación hidrodinámica. .............. 25

Figura 4.6: Configuración general de las obras marítimas contempladas en el proyecto de

concentradora de mineral. ................................................................................................................. 28

Figura 5.1: Resultados característicos del modelo CMS-WAVE para Km 14. ................................. 31

Figura 5.2: Comparación altura significativa para campaña de invierno. ......................................... 33

Figura 5.3: Comparación altura significativa para campaña de verano. ........................................... 33

Figura 5.4: Comparación de las series de tiempo de nivel del mar para la campaña de Invierno en
Km 14, Tocopilla. ............................................................................................................................... 35

Figura 5.5: Comparación dato a dato de los niveles del mar simulados y medidos en la campaña de

Invierno para Km 14, Tocopilla. ......................................................................................................... 35

Figura 5.6: Comparación de las series de tiempo de nivel del mar para la campaña de Verano en
Km 14, Tocopilla. ............................................................................................................................... 37

Figura 5.7: Comparación dato a dato de los niveles del mar simulados y medidos en la campaña de

Verano para Km 14, Tocopilla. .......................................................................................................... 37

Figura 5.8: Resultados típicos de la hidrodinámica del modelo CMS-FLOW para cada uno de los
ensayos realizados, Invierno. ............................................................................................................ 40

Figura 5.9: Comparación de las series de tiempo de corrientes medidas, con los resultados del
ensayo 1, para la campaña de Invierno en Km 14, Tocopilla. .......................................................... 41

Figura 5.10: Comparación de las series de tiempo de corrientes medidas, con los resultados del
ensayo 2, para la campaña de Invierno en Km 14, Tocopilla. .......................................................... 42

Figura 5.11: Comparación de las series de tiempo de corrientes medidas, con los resultados del
ensayo 3, para la campaña de Invierno en Km 14, Tocopilla. .......................................................... 43

Figura 5.12: Comparación dato a dato de las corrientes medidas en la campaña de Invierno y
resultados del ensayo 2 para Km 14, Tocopilla. ............................................................................... 44

Figura 5.13: Comparación dato a dato de las corrientes medidas en la campaña de Invierno y
resultados del ensayo 3 para Km 14, Tocopilla. ............................................................................... 45

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|7|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Figura 5.14: Comparación de las series de tiempo de corrientes medidas y simuladas, para la
campaña de Verano, instrumento SONTEK fondeado en Km 14, Tocopilla. ................................... 46

Figura 5.15: Comparación de las series de tiempo de corrientes medidas y simuladas, para la
campaña de Verano, instrumento RDI fondeado en Km 14, Tocopilla. ............................................ 47

Figura 5.16: Comparación dato a dato de las corrientes medidas y simuladas, para la campaña de
Verano, instrumento SONTEK fondeado en Km 14, Tocopilla. ........................................................ 48

Figura 5.17: Comparación dato a dato de las corrientes medidas y simuladas, para la campaña de
Verano, instrumento RDI fondeado en Km 14, Tocopilla. ................................................................. 49

Figura 5.18: Estimación de la cantidad de sedimentos en suspensión debido al proceso de
excavación de las zanjas de cruce de la rompiente.......................................................................... 50

Figura 5.19: Magnitudes de concentración de sedimentos en suspensión empleados en el modelo
numérico de dispersión de partículas PTM. A) En la zona de rompientes y B) Después de la zona
de rompientes. ................................................................................................................................... 51

Figura 5.20: Identificación de los ciclos diarios para los datos oceanográficos de la campaña de

Invierno en Km 14. ............................................................................................................................ 53

Figura 5.21: Identificación de los ciclos diarios para los datos oceanográficos de la campaña de

Verano en Km 14. .............................................................................................................................. 54

Figura 5.22: Resultados de la dispersión de sedimentos en suspensión en el tiempo según el
modelo numérico PTM, para todos los escenarios hidrodinámicos considerando entibaciones

laterales. ............................................................................................................................................ 55

Figura 5.23: Área total esperada con partículas suspendidas con y sin entibaciones, para la zanja
de descarga en el escenario hidrodinámico 1. .................................................................................. 56

Figura 5.24: Área total esperada con partículas suspendidas con y sin entibaciones, para la zanja
de descarga en el escenario hidrodinámico 2. .................................................................................. 57

Figura 5.25: Área total esperada con partículas suspendidas con y sin entibaciones, para la zanja
de descarga en el escenario hidrodinámico 3. .................................................................................. 58

Figura 5.26: Área total esperada con partículas suspendidas con y sin entibaciones, para la zanja
de descarga en el escenario hidrodinámico 4. .................................................................................. 59

Figura 5.27: Resultados de la dispersión de sedimentos en suspensión en el tiempo según el
modelo numérico PTM, para todos los escenarios hidrodinámicos considerando entibaciones

laterales. ............................................................................................................................................ 60

Figura 5.28: Área total esperada con partículas suspendidas con y sin entibaciones, para la zanja
de toma en el escenario hidrodinámico 1. ........................................................................................ 61

Figura 5.29: Área total esperada con partículas suspendidas con y sin entibaciones, para la zanja
de toma en el escenario hidrodinámico 2. ........................................................................................ 62

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|8|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Figura 5.30: Área total esperada con partículas suspendidas con y sin entibaciones, para la zanja
de toma en el escenario hidrodinámico 3. ........................................................................................ 63

Figura 5.31: Área total esperada con partículas suspendidas con y sin entibaciones, para la zanja
de toma en el escenario hidrodinámico 4. ........................................................................................ 64

**LISTADO DE TABLAS**

Tabla 4.1: Escenarios a simular para el proceso de excavación de las zanjas. ............................... 30

<!-- INICIO TABLA 4.1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- para la estación de invierno y verano. En función de estas condiciones oceanográficas se han configurado dos sets de escenarios a simular, los que se presentan en la Tabla 4.1. -->

**Tabla 4.1: Escenarios a simular para el proceso de excavación de las zanjas.****

| Col1 | INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14 | No DOCUMENTO<br>IT -MOD-INIMA012015 | EDICIÓN / REVISIÓN<br>2/2 | 31 |
| --- | --- | --- | --- | --- |
|  | **INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14** | Fecha de emisión:<br>14/09/2015 | Emitido por:<br>EcoTecnos S.A. | Emitido por:<br>EcoTecnos S.A. |

<!-- Estadísticas: 1 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **5** **RESULTADOS** **5.1** **CALIBRACIÓN DEL MODELO NUMÉRICO DE OLEAJE** -->
<!-- FIN TABLA 4.1 -->


Tabla 5.1: Indicadores estadísticos de la comparación de los niveles del mar simulados y medidos

<!-- INICIO TABLA 5.1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|36| |---|---|---|---|---| ||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.| -->

**Tabla 5.1: Indicadores estadísticos de la comparación de los niveles del mar****

| Indicador Estadístico | Valor |
| --- | --- |
| Coeficiente de correlación | 0.98 |
| Error típico (m) | 0.07 |
| Covarianza (m) | 0.09 |

<!-- Estadísticas: 3 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Aplicando la misma configuración del modelo empleada para el invierno, se simuló la condición de verano obteniéndose resultados similares a los datos de campo. La comparación de las series de tiempo mostradas en la Figura 5.6 es indicadora de la -->
<!-- FIN TABLA 5.1 -->

para la campaña de Invierno en Km 14, Tocopilla. ........................................................................... 36

Tabla 5.2: Indicadores estadísticos de la comparación de los niveles del mar simulados y medidos

<!-- INICIO TABLA 5.2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|38| |---|---|---|---|---| ||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.| -->

**Tabla 5.2: Indicadores estadísticos de la comparación de los niveles del mar****

| Indicador Estadístico | Valor |
| --- | --- |
| Coeficiente de correlación | 0.99 |
| Error típico (m) | 0.05 |
| Covarianza (m) | 0.09 |

<!-- Estadísticas: 3 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **5.2.2 Calibración de las corrientes** En la Figura 5.8 se ilustran las magnitudes de corriente asociadas a la estación de Invierno para Km 14, para cada uno de los ensayos numéricos propuestos para el día 24 -->
<!-- FIN TABLA 5.2 -->


para la campaña de Verano en Km 14, Tocopilla. ............................................................................ 38

Tabla 5.3: Áreas esperadas con sólidos suspendidos debido a las faenas de excavación de la

<!-- INICIO TABLA 5.3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Para ilustrar los efectos de las entibaciones laterales, se presenta en la Tabla 5.3 que compara las áreas con sólidos suspendidos desde las faenas de excavación de la zanja de lanzamiento de las tuberías de descarga. De ella, se advierte que en todos los escenarios los efectos de disminución de la zona de influencia superarían los 1000 m [2] . -->

**Tabla 5.3: Áreas esperadas con sólidos suspendidos debido a las faenas de****

| Escenario | Con entibaciones (m2) | Sin entibaciones (m2) | Disminución por<br>entibaciones (m2) |
| --- | --- | --- | --- |
| 1 | 4053 | 7400 | 3347 |
| 2 | 3555 | 6761 | 3206 |
| 3 | 3427 | 5180 | 1753 |
| 4 | 3158 | 6954 | 3796 |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- De modo complementario, a través de las figuras 4.23 a la 4.26, se muestran las áreas que tendrían sólidos suspendidos, considerando tanto la situación con y sin entibaciones. **Figura 5.23: Área total esperada con partículas suspendidas con y sin entibaciones,** -->
<!-- FIN TABLA 5.3 -->

zanja de descarga. ............................................................................................................................ 56

Tabla 5.4: Áreas esperadas con sólidos suspendidos debido a las faenas de excavación de la

<!-- INICIO TABLA 5.4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|61| |---|---|---|---|---| ||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.| -->

**Tabla 5.4: Áreas esperadas con sólidos suspendidos debido a las faenas de****

| Escenario | Con entibaciones (m2) | Sin entibaciones (m2) | Disminución por<br>entibaciones (m2) |
| --- | --- | --- | --- |
| 1 | 2780 | 11769 | 8989 |
| 2 | 2949 | 11717 | 8768 |
| 3 | 2449 | 9567 | 7118 |
| 4 | 3174 | 9174 | 6000 |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Figura 5.28: Área total esperada con partículas suspendidas con y sin entibaciones,** **para la zanja de toma en el escenario hidrodinámico 1.** -->
<!-- FIN TABLA 5.4 -->

zanja de toma. ................................................................................................................................... 61

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|9|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**1** **INTRODUCCIÓN**

La construcción de obras marítimas, desde un punto de vista ambiental, podría
considerarse como un proceso invasivo que generaría efectos no deseados sobre el
medio, ya sea alterando la composición geomorfológica de la costa, movimientos de
sedimentos que afecten las comunidades bentónicas u otras acciones.

Usualmente, los métodos constructivos propuestos por la ingeniería marítima se basan en
muelles auxiliares y/o plataformas de operación que arrancan desde la costa y en pocas
ocasiones se construye desde el mar, siendo el primer conjunto de procedimientos
responsable de colocar sedimentos en suspensión que entran inmediatamente en
contacto con la línea de costa, produciendo una pluma de turbidez la que no
necesariamente es reflejo de contaminación marina.

En el presente estudio, la empresa EcoTecnos S.A., quien por requerimiento de la
empresa INIMA CVV, ha evaluado el potencial de suspensión de sedimentos, debido a la
construcción de las obras marítimas asociadas a la planta desalinizadora del proyecto
“Explotación de Sulfuros Radomiro Tomic Fase II”, el cual se instalará en el sector Km 14
de la comuna de Tocopilla, Región de Antofagasta, determinándose en una primera
instancia los efectos de la excavación de zanjas en zona de rompiente.

El método constructivo modifica el considerado en el EIA mediante la incorporación de
placas de entibación y una menor longitud de excavación de la zanja, las que se han
proyectado con la finalidad de brindar un control lateral del transporte de sedimentos
durante el periodo de construcción de las obras, con la finalidad de contener la
suspensión y adicionalmente, evitar ingresos no deseados de sedimentos en la zanja, que
ocasionalmente producen aumentos de dragado para alcanzar la cota de proyecto.

Las características del nuevo muelle provisorio son:

 - Longitud: 168 metros.

 - Ancho: 16.20 metros.

 Líneas de pilotes: 3 paralelas

 Número de pilotes: 87

Lo anterior considera una reducción de la longitud del nuevo muelle y el ancho de
intervención del fondo macizo, en comparación con el proyectado y mencionado en el EIA
que indicó 384 metros de longitud y 34 de ancho de fondo de mar intervenido.

Para la determinación de la suspensión y posterior transporte de sedimentos estos,
EcoTecnos S.A. ha desarrollado estudios de modelación numérica de oleaje,
hidrodinámica y seguimiento de partículas, complementados con cálculos de escritorio,
para evaluar si las plumas de sedimentos entran en contacto con la línea de costa.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|10|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

En consecuencia, el presente documento contiene la metodología, resultados,
conclusiones y recomendaciones obtenidas a partir del estudio de dispersión de
sedimentos en suspensión y sus eventuales interacciones con la línea de costa, tomando
como referencia el estudio previamente desarrollad y reportado, considerando el método
constructivo anterior y que se recoge en el anexo 38 adenda N°1 del EIA.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|11|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**2** **OBJETIVOS**

El objetivo general del presente estudio es determinar de manera numérica el
comportamiento de los sedimentos suspendidos por las faenas de excavación de las
zanjas en la zona de rompientes, con la metodología propuesta por el consorcio INIMA
CVV.

Para el cumplimiento del objetivo general del estudio, se desarrollaron las siguientes
actividades específicas:

 Análisis general de los antecedentes de oceanografía física.

 Estimación de las tasas de suspensión de sedimentos, debido a la acción del
clamshell.

 Modelación numérica del oleaje, corrientes y transporte de sedimentos.

 Modelación lagrangiana del seguimiento de las partículas de sedimentos.

**3** **REFERENCIAS**

Para la realización del presente estudio se han considerado como referencias del
proyecto, los siguientes documentos y planos:

 Lay out: OOMM R13403-I1-INICVV-07100-100OM02-6370-001

 - Anexo 38 adenda N°1 EIA.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|12|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**4** **MATERIALES Y MÉTODOS**

La estimación de la suspensión de sedimentos debido a la acción de corrientes u otro
fenómeno natural o antrópico, corresponde a una de las variables de interés en la
evaluación ambiental de un proyecto de índole marítimo y por lo tanto, el enfoque
metodológico debe ser capaz de incorporar de manera correcta cada uno de las
forzantes.

El presente estudio corresponde a una estimación empírico-numérica de la suspensión de
sedimentos en la zona de Tocopilla, específicamente en Km 14, aplicando la metodología
que se describe a seguir.

Los antecedentes oceanográficos y características de los sedimentos superficiales que
componen la capa de sobrecarga, fueron analizados y reportados sus resultados en
estudios anteriores, de tal modo que en el presente informe se consideran como
información base y de referencia (ver Anexo 38 adenda N°1 EIA).

**4.1** **MATERIALES**

La representación numérica de la hidrodinámica está altamente influenciada por el tipo de
ambiente que se quiera simular, ya que cada uno de ellos tiene su propio conjunto de
forzantes y/o agentes dominantes. En el caso de una costa abierta como Tocopilla y el
sector de Km 14, se pueden identificar como agentes principales las siguientes forzantes:

 Oleaje

 - Viento

 - Mareas

En el caso del oleaje es importante destacar que su principal influencia en la
hidrodinámica ocurre en la zona previa a la rompiente, en la misma rotura y en la zona de
ascenso-descenso del oleaje sobre la playa. Por su parte los vientos son capaces de
influenciar de manera superficial amplias zonas del mar y de manera complementaria a la
generación de oleaje, inducen corrientes y modifican el patrón de circulación de la
columna de agua mediante transferencia turbulenta de energía desde las capas
superiores a las inferiores.

Las mareas son las principales responsables de las corrientes cíclicas en las costas
mediante la acción de la llenante y vaciante, las que inducen flujos y reflujos. La magnitud
de las corrientes de mareas son definidas por dos características, una es la amplitud del
movimiento oscilatorio (diferencia entre la plea y bajamar) y la segunda la composición
geomorfológica de la costa en la cual actúa, ya que se pueden amplificar los efectos.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|13|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Otros agentes de menor relevancia son las corrientes inducidas por variaciones de las
propiedades físicas de la columna de agua, las de carácter oceánico y la de Coriolis.

Para la modelación numérica de la hidrodinámica, se ha propuesto en este estudio la
aplicación de dos modelos numéricos: el primero para la representación del oleaje
denominado CMS-WAVE y el segundo la hidrodinámica completa, llamado CMS-FLOW.

El Coastal Modelling System (CMS) corresponde a una herramienta integrada de la suite
SMS y permite aplicar de manera acoplada su módulo de oleaje y corrientes, simulando
una gran variedad de procesos siendo su esquema de aplicación usualmente como es
ilustrado en la Figura 4.1.

**Figura 4.1: Aplicación de los modelos CMS-WAVE y CMS-FLOW.**

Para la determinación del movimiento de las partículas de sedimentos una vez
suspendidas, se aplicó el modelo numérico PTM, el cual describe de manera lagrangiana

el movimiento.

A continuación se describe de manera más profunda cada uno de los módulos aplicados a
la caracterización de la hidrodinámica del sector denominado Km 14, en la comuna de
Tocopilla.

**4.1.1 Descripción del modelo numérico CMS-WAVE**

CMS-WAVE fue desarrollado por Lin _et al._ (2006b) y Demirbilek _et al._ (2007), previamente
este modelo se llamó WABED (Wave-Action Balance Equation Diffraction) y corresponde
a un modelo espectral bidimensional basado en la ecuación con aproximación parabólica,

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|14|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

incluyendo disipación de energía y términos que simulan la difracción de acuerdo con
Mase _et al._ (2005a).

Las principales capacidades de CMS-WAVE son:

 - Refracción

 _Shoaling_

 - Rompiente

 Disipación debido a la rotura

 Disipación por fricción de fondo

 - Difracción

 - Reflexión

 Interacción oleaje corrientes

 - Generación y crecimiento del oleaje (incluyendo _withecapping_ )

 - Sobrepaso y _run-up_ del oleaje en playas

 Interacción no lineal del oleaje

La ecuación principal que resuelve el modelo CMS-WAVE es la de acción de ondas,
descrita según la ecuación 4.1

**Ecuación 4.1**

x N) + [∂][(][C] [y] [N][)]

∂x

[θ] [N)]

= [k]
∂θ

[k]

2σ [[(CC] [g] [cos] [2] [θN] [y] [)] [y] [−CC] 2 [g]

∂(C x N)

[C] [y] [N][)]

+ [∂(C] [θ] [N)]
∂y ∂θ

[g]

2 [cos] [2] [θN] [yy] [] −ε] [b] [N−S]

N= [E(σ, θ)]

σ

De donde:

N: Acción de onda.

E: Densidad de energía espectral.

: Frecuencia.

: Dirección.

C: Celeridad de la onda.

C g : Celeridad de grupo.

N y y N YY : Primera y segunda derivada de N respecto de y.

C x, y,  : Celeridad de la onda respecto de x, y o , respectivamente.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|15|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

k: Parámetro empírico que representa la intensidad de la difracción.

 b : Disipación de energía debido a la rotura.

S: términos fuente, incluyendo ingreso y pérdidas de energía.

Cabe destacar que el primer término de la derecha de la ecuación 2.1, corresponde a la
difracción de acuerdo a la aproximación de Mase _et al._ (2005b), que según diversos
ensayos de laboratorios desarrollados por el mismo autor, es capaz de representar los
efectos de obras de longitud semi infinitas y diversas configuraciones, mediante la
calibración del coeficiente k.

Para determinar la interacción oleaje corrientes, CMS-WAVE incorpora la metodología de
Larson & Kraus (2002) considerando el efecto “Doopler shiftting”, que según la
investigación desarrollada por Lai _et al._ (1989) permite que la teoría lineal del oleaje se
ajuste de manera adecuada.

Respecto de la reflexión del oleaje CMS-WAVE aplica un coeficiente sin representar el
fenómeno físico propiamente tal, mientras que para estimar la altura de oleaje rompiente
aplica el criterio de Miche (1951) y para la disipación de energía debido a rotura se puede
emplear alguno de los siguientes métodos:

 - Ecuación extendida de Goda (Sakai _et al._ 1989).

 - Ecuación extendida de Miche (Batjjes 1972; Mase _et al._ 2005b).

 - Batjjes & Janssen (1978).

 Chawla & Kirby (2002).

La pérdida de energía por fricción de fondo es calculada mediante la metodología de
Collins (1972) usando coeficientes del tipo Darcy-Weisbach.

En el caso de la interacción con estructuras, CMS-WAVE incluye el _run-up_ y sobrepaso,
tal como se comentó previamente. En el caso de la primera variable ( _run-up_ ) se resuelve
la ecuación de momento, mientras que la segunda, se realiza mediante coeficientes de
transmisión.

Desde un punto de vista numérico, CMS-WAVE es un modelo en diferencias finitas que
permite usar grillas con elementos rectangulares y anidar [1] para optimizar la resolución.

1
El anidamiento puede ser entre varias grillas y con distintas orientaciones, es decir, no necesariamente la grilla fina debe
tener la misma dirección principal que la gruesa. Sin embargo, no se recomienda exceder un ángulo de 45°.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|16|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**4.1.2 Descripción del modelo numérico CMS-FLOW**

CMS-FLOW es un modelo bidimensional (2D) hidro - morfodinámico en elementos finitos,
que integra en la vertical las ecuaciones de continuidad y momento para representar los
movimientos de las masas de agua. Las capacidades principales de esta herramienta se
describen a continuación:

 Representación de la hidrodinámica por mareas y vientos.

 Representación de la hidrodinámica por olas, integrando resultados de CMS
WAVE.

 Capacidad de simular procesos de mojado/secado de celdas (inundaciones).

 Determinación del transporte de sedimentos mediante la aplicación de la ecuación
de advección difusión.

 - Evolución morfodinámica.

Considerando los objetivos de este estudio, solo se presentarán de manera ampliadas las
capacidades hidrodinámicas del modelo CMS-FLOW sin incluir el transporte de
sedimentos ni la evolución morfológica del fondo.

Para determinar las velocidades de corriente integradas en la vertical y las
desnivelaciones instantáneas de la superficie del mar, CMS-FLOW resuelve la ecuación
de continuidad (Ecuación 4.2) y la de conservación de momentum (Ecuación 4.3 y 4.4).

**Ecuación** **4.2**

∂(h+  )

[x]

∂x [+ ∂yq] [y]

 )

+ [∂q] [x]
∂t ∂x

= 0
∂y

**Ecuación 4.3**

∂x [D] [x]

∂q x

∂q x

∂t [+ ∂uq] ∂x [x]

[x]

∂x [+ ∂vq] [x]

[x]

∂y [+ 1] 2

2 [g∂(h+] ∂x [ ] [)] [2]

∂y [D] [y]

[ ] [)] = [∂]

∂x

∂q x

∂q x

[∂]
∂x [+]

∂q x

∂y [+ fq] [y] [−τ] [bx] [+ τ] [wx] [+ τ] [Sx]

**Ecuación 4.4**

∂x [D] [x]

∂q y

y

∂t [+ ∂uq] ∂x [y]

[y]

∂x [+ ∂vq] [y]

[y]

∂y [+ 1] 2

2 [g∂(h+] [ ] [)] [2]

∂y [D] [y]

[ ] [)] = [∂]

∂y

∂q x

∂q x

[∂]
∂x [+]

∂q y

∂y [+ fq] [y] [−τ] [by] [+ τ] [wy] [+ τ] [Sy]

De donde:

h: Profundidad del agua respecto del nivel medio.

: Desnivelación instantánea del océano.

t: Tiempo.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|17|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

q x y q y : Flujo por unidad de ancho paralelo al eje x e y, respectivamente.

u y v: Velocidades de corriente, integradas en la vertical, paralelas al eje x e y,

respectivamente.

g: Aceleración de gravedad.

D x y D y : Coeficiente de difusión en la dirección x e y, respectivamente.

: Parámetro de Coriolis.

 bx y  by : Tensión en el fondo paralela al eje x e y, respectivamente.

 wx y  wy : Tensión superficial paralela al eje x e y, respectivamente.

 Sx y  Sy : Tensión debido al oleaje paralela al eje x e y, respectivamente.

Para la determinación de las tensiones en el fondo, se incorpora el coeficiente de Chezy,
mediante la rugosidad de manning. Para la inclusión de la acción del oleaje, se emplea la
aproximación corregida de acuerdo a la formulación de Nishimura (1988).

En el caso de las tensiones superficiales, estas son asociadas íntegramente a la acción
del viento, considerando la presencia de un coeficiente de arrastre (drag), la velocidad y
dirección de la forzante.

Las tensiones debido a oleaje se obtienen mediante la incorporación de los tensores de
radiación provenientes desde el modelo CMS-WAVE, los que son determinados de
manera espectral.

Los términos difusivos dependen de la mezcla en la columna de agua, la cual es
incorporada mediante la técnica de Eddy Viscosity. Cuando se simula sin la consideración
del aporte del oleaje, CMS-FLOW aplica la aproximación de Falconer (1980), mientras
que en caso contrario se considera la de Smith _et al._ (1993).

CMS-FLOW puede ser configurado para considerar las siguientes condiciones de borde:

 Serie de tiempo de desnivelaciones del nivel del mar.

 Serie de tiempo de mareas construida a partir de la definición de las constituyentes
armónicas conocidas.

 Serie de tiempo de velocidades.

 Serie de tiempo de caudales.

 Borde reflejante o cerrado.

 Condición de borde de ajuste de oleaje, niveles del mar y velocidades.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|18|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Numéricamente CMS-FLOW resuelve las ecuaciones sobre una grilla rectangular de
celda regular o irregular, mediante elementos finitos. Todos los términos espaciales (x e y)
son resueltos mediante diferencias centradas con la excepción de los asociados a la
advección, ya que los aproxima mediante un algoritmo basado en diferencias hacia
adelante.

**4.1.3 Descripción del modelo numérico PTM**

El Particle Tracking Model (PTM), es un modelo numérico desarrollado por el Coastal
Inlets Research Program que permite determinar los movimientos lagrangianos que tienen
las partículas (sedimentos u otras) en un ambiente costero.

El modelo PTM permite la inclusión de la hidrodinámica debido a vientos, mareas y olas,
ya que puede acoplarse a los resultados de modelaciones realizadas en CMS-WAVE y
CMS-FLOW, los que han sido descritos previamente.

Algunas de las características principales del modelo PTM, le permiten estimar la tasa de
sedimentos en suspensión, depositación y transporte total de sedimentos; y al emplear
técnicas lagrangianas, es capaz de identificar el movimiento de cada partícula, las cuales
son caracterizadas como una masa.

Las capacidades más relevantes del modelo PTM se describen a continuación:

 - Determinación de las formas de fondo.

 - Inicio del movimiento de los sedimentos.

 - Transporte de sedimentos.

 Cambios en el fondo (evolución morfodinámica de corto plazo).

 Movimiento de las partículas.

 Cálculo de las trayectorias de las partículas.

 Simulación de trampas de sedimentos.

El esquema general de cálculo del modelo PTM, se muestra en la Figura 4.2. De ella se
destaca que como datos de entrada se necesitan las características batimétricas, de los
sedimentos que actualmente componen el fondo, la rugosidad del lecho. Posteriormente
mediante las características de la hidrodinámica ( _flows_ ) y el oleaje ( _waves_ ) se determinan
los flujos, el transporte, las formas de fondo y el seguimiento de partículas.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|19|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Figura 4.2: Diagrama de flujo de aplicación del modelo PTM.**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|20|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Si bien el modelo PTM emplea las soluciones de modelos numéricos 2D de oleaje y/o
hidrodinámica, es capaz de determinar la distribución vertical de las velocidades de la
corriente mediante la aplicación de la ecuación de Yalin (1977).

PTM puede ser configurado para realizar cálculos en modo bidimensional (2D), quasi
tridimensional (Q3D) o tridimensional (3D). Tanto la configuración Q3D como la 3D,
proveen una buena estimación del comportamiento de las partículas de sedimentos en la
columna de agua, siendo más eficiente desde un punto de vista del gasto computacional
el Q3D.

Cuando el modelo PTM se configura en modo Q3D, son simulados los procesos de
suspensión y depositación de sedimentos, siendo posible incorporar la re-suspensión.
Complementariamente se estiman las mezclas entre el material depositado y el sedimento

nativo.

Algunas de las formulaciones principales que aplica el modelo PTM se describen a
continuación de manera general:

 - _**Rugosidad del fondo**_ : La estima en función de los diámetros d 50 y d 90 del material
nativo.

 - _**Tensión de corte:**_ La puede determinar considerando la acción de las corrientes,
el oleaje y la combinación de ambos, aplicando ecuaciones clásicas como las de
O’Connor & Yoo (1988) y Van Rijn (1993).

 - _**Inicio del movimiento:**_ Considera el criterio general propuesto por Shields.

 - _**Formas de fondo:**_ Las determina mediante las aproximaciones de Van Rijn
(1984c).

 - _**Tasa de transporte de sedimentos:**_ Aplica la fórmula de Soulsby-Van Rijn
(1997).

Para determinar la posición de las partículas, PTM aplica la ecuación 4.5 que se describe
a continuación:

**Ecuación 4.5**

x [′] = x n + [1] 2 [(u] [a] [dt+ u] [d] [dt)]

De donde:

u a : Velocidad de advección, determinada en función de la concentración de sedimentos en

suspensión.

U d : Velocidad de difusión, determinada de manera separada para la horizontal y la

vertical.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|21|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**4.2** **METODOLOGÍA**

**4.2.1 Calibración y validación de los modelos numéricos**

En el ámbito de la modelación numérica es común de emplear dos términos
convencionales: calibración y validación. El primero de ellos corresponde al proceso en el
cual los modelos numéricos son ajustados mediante la modificación de coeficientes y
parámetros para poder representar las condiciones de terreno que han sido medidas
previamente.

Por su parte, la validación corresponde a la simulación de un segundo periodo de tiempo,
diferente al de la calibración, en el cual se verifican los supuestos y modificaciones
implementadas previamente.

A continuación se describe la metodología empleada para la calibración y validación de
los modelos numéricos de oleaje e hidrodinámico.

_**4.2.1.1 Calibración y validación del modelo de oleaje**_

El siguiente apartado presenta la metodología con la cual se obtuvo el oleaje para todos
los estados de mar necesarios para efectos del presente estudio.

La cuantificación del oleaje es importante dependiendo de la dominancia de éste en
relación a las forzantes presentes en el sector de estudio. Generalmente para efectos del
transporte de sedimentos en la costa el oleaje se torna importante dentro de la zona de
surf, acá el proceso de transformación que predomina es la rotura del oleaje. Sin
embargo, en aguas intermedia donde el oleaje no es capaz de romper por profundidad las
corrientes inducidas por el oleaje pueden transportar sedimentos, por lo que a priori no se
puede descartar el oleaje como ingrediente relevante en el movimiento de los granos en el
fondo y en suspensión.

El proceso de calibración del oleaje tiene por objetivo generar a partir de los datos
medidos, el campo de oleaje necesario para complementar la cuantificación de la
hidrodinámica del sector de estudio.

Para realizar se genera una grilla numérica, en donde se resuelven las ecuaciones de
gobierno del modelo descrito en el apartado 4.1.1.; para luego, propagar de manera
inversa los estados de mar hasta el borde numérico de la misma, la cual fue realizada
simulando las condiciones de período y dirección más representativas de oleaje medido
en el sector de estudio, para luego obtener las funciones superficiales discretas,
asociadas a los coeficientes de transformación de energía y dirección (estos incluyen los
procesos de propagación del oleaje, asomeramiento, refracción, difracción, etc.).

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|22|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Posteriormente, para cada estado de mar medido, se obtuvo los respectivos coeficientes
mediante una interpolación superficial para la obtención de los parámetros asociados a
las mediciones en el borde de la grilla de cómputo. Estos parámetros son empleados para
resolver el oleaje sobre todo el dominio numérico, ejercicio necesario para la
determinación de las corrientes inducidas por oleaje y posterior cuantificación de la
hidrodinámica del sector.

La Figura 4.3 representa un esquema explicativo del proceso descrito anteriormente.
Cabe destacar, que este está desarrollado en relación a los requerimientos del estudio, a
la información disponible para cuantificar el oleaje y a las condiciones particulares del
sector de interés.

**Figura 4.3: Esquema estimación del oleaje para la caracterización hidrodinámica del**

**sector de estudio.**

Para evaluar si el mencionado método era suficientemente aceptable para los efectos
requeridos, los resultados fueron sometidos a un proceso de validación, en donde a partir
de las mediciones de campo disponibles se evaluó la correspondencia entre éstas y las
condiciones obtenidas de la modelación.

El dominio numérico fue establecido, considerando un área suficientemente extensa, con
el fin de que los fenómenos físicos resueltos en la propagación del oleaje no sean
afectados por las condiciones numéricas en los bordes. En este tipo de modelos, fue
preciso cuidar que la grilla numérica contenga todas las direcciones de interés en las

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|23|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

localidades a estudiar. Asimismo, la orientación de ésta es la óptima para contener todos
los casos de oleaje, necesarios para su caracterización en el presente estudio.

En la Figura 4.4 se ilustra la extensión total del dominio numérico empleado en el
presente estudio, nótese que se comenzó la transferencia del oleaje desde una
profundidad mayor a los 500 metros, con la finalidad de asegurar que el oleaje comience
la propagación desde aguas profundas.

**Figura 4.4: Dominio numérico empleado para resolver el oleaje.**

El modelo utilizado para la resolución del oleaje, fue del tipo integrado en la fase de la ola,
por lo que el tamaño de las celdas de la grilla no estuvieron ligadas a la longitud de onda,
sino más bien la densidad de elementos de la malla asociada a la correcta representación
del fondo en función de las sondas de profundidad disponibles.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|24|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

El tipo de celda en el modelo empleado posee una geometría cuadrada, cuyo lado es
constante para todo el dominio. Para este caso, y de acuerdo a la densidad de la
información batimétrica disponible, se consideró una discretización con un espaciamiento
(Δx) de 25 m, siendo este un valor típico en la resolución del oleaje en los sectores de
detalle del modelo.

En el modelo CMS-Wave todas las celdas poseen los mismos atributos, debido a que en
función de la profundidad el modelo discrimina cuando resolver las magnitudes físicas de
interés, es decir, no es necesario definir celdas de tierra como en modelos semejantes.

La grilla espectral se configuró para representar una forma sintética en frecuencias del
tipo TMA; mientras que direccionalmente fue de características cosenoidal con potencia
(nn) definida en función del periodo.

La resolución en el dominio de las frecuencias fue compuesta con 50 componentes,
distribuidas linealmente entre el rango de frecuencias compuesto por 0.04 hz (25
segundos) y 0.53 hz (1.9 segundos.). En el caso de las direcciones se emplearon 35
componentes con resolución de 5° contenidas en el rango de +85° y - 85°, matemáticos
respecto del eje de la grilla, es decir, ángulos náuticos entre 255° y 185°.

_**1.1.1.1 Calibración y validación del modelo hidrodinámico**_

La calibración del modelo numérico hidrodinámico se realizó considerando tanto las

mediciones de niveles del mar (mareas) como las de corriente para la campaña de
invierno, mientras que en la validación se emplearon los de verano.

Se configuró un dominio numérico que abarcó desde los 200 metros de profundidad hasta
la costa, con una grilla de elementos cuadrados de 50 metros de lado. En el dominio del
tiempo, se seleccionó un ΔT de 0.7 segundos, de acuerdo al criterio de courant y un
intervalo de pre-corrida de 5 horas, para alcanzar la estabilidad. En la Figura 4.5 se ilustra
la grilla empleada en la simulación.

En total se simuló la hidrodinámica de 60 días para invierno y 30 días para verano,
aproximadamente

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|25|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Figura 4.5: Extensión de la grilla numérica empleada para la modelación**

**hidrodinámica.**

**Niveles del mar**

El proceso de calibración se enfocó en primera instancia en los niveles del mar, para lo
cual se empleó una serie de tiempo de mareas como forzante, la que fue construida a
partir de las constituyentes armónicas obtenidas desde las mediciones en el sector de
Tocopilla, posteriormente fue trasladada hacia aguas profundas con correcciones de la
amplitud en función de las recomendaciones de la literatura especializada.

Como dato de campo para la comparación se determinó el nivel del mar a partir de las
mediciones de profundidad del instrumento de oleaje fondeado en la zona de estudio, el
que se vinculó geométricamente al NRS de Tocopilla, con la finalidad de mantener el
plano de referencia

Los resultados obtenidos se presentaron de dos formas: series de tiempo y comparación
dato a dato. En la primera ilustración se buscó demostrar que los niveles del mar
determinados por el modelo, se comportan de similar manera a los registrados
instrumentalmente en la zona de estudio.

La comparación dato a dato, se realizó con la finalidad de evaluar directamente si la
relación del modelo numérico con los datos de terreno se ajusta a una recta de pendiente
1:1, es decir, si un metro de marea medido es también representado con dicha magnitud
en el modelo numérico, sin importar el instante de tiempo donde ocurra.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|26|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Estos dos enfoques de comparación permiten definir si el modelo numérico es lo
suficientemente robusto tanto en su evolución temporal como estadística.
Complementariamente se determinó el coeficiente de correlación y el error típico.

**Corrientes**

Una vez calibradas las mareas o niveles del mar, se procedió a simular las corrientes para
lo cual se realizó una serie de ensayos numéricos con la finalidad de evaluar la
importancia de distintas forzantes, los cuales se describen a continuación:

 - Ensayo 1: Forzado solo por mareas.

 - Ensayo 2: Forzado por mareas y vientos.

 - Ensayo 3: Forzado por mareas, vientos y oleaje.

La información de la forzante de viento se obtuvo desde las mediciones instrumentales

con anemómetro realizadas en Km 14, corriéndolas para llevarlas a 10 metros de alturas
sobre el nivel del mar y trasladarlas desde continente a mar. Dentro del modelo numérico
se consideró variable en el tiempo y constantes en el espacio, tanto para las magnitudes
como las direcciones.

La forzante de oleaje se consideró a partir de los resultados del modelo numérico CMSWAVE para el proceso de calibración y validación descrito previamente, considerando el
campo variable en el espacio y tiempo de los tensores de radiación.

Para cada ensayo se obtuvieron las componentes ortogonales del modelo numérico (u y
v), las que se sumaron vectorialmente para obtener la magnitud total de la corriente.

Respecto de las direcciones de las corrientes, no fue posible comparar los datos del
modelo con los de terreno, debido a que en el proceso de integración solo se incluyen las
magnitudes.

Los resultados del modelo numérico para cada uno de estos ensayos, se comparó con los
datos de terreno provenientes desde el ADCP RDI. Cabe destacar que para hacer
homologables ambos valores (corrientes medidas v/s simuladas), fue necesario realizar
una integración en la vertical de las magnitudes de las corrientes registradas, ya que el
modelo empleado sólo considera las corrientes bidimensionales.

La presentación de los resultados se realizó, de igual manera a las mareas, es decir,
verificando el comportamiento temporal y estadístico, por lo que se procedió a determinar
los mismos indicadores que son utilizados para las mareas.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|27|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**4.2.2 Modelación numérica de la suspensión**

_**4.2.2.1 Aspectos generales**_

El inicio del movimiento de los sedimentos de un lecho, es un proceso altamente dinámico
y producido por el desbalance de fuerzas que generan las corrientes (cualquiera sea su
origen) sobre las partículas que lo componen. Toda vez que la velocidad del fluido supere
la condición máxima de equilibrio de los granos, se generará el transporte de sedimentos.

Al iniciar el movimiento los sedimentos tienen diversos mecanismos para hacerlo, uno de
ellos es la conocida carga de fondo, la que corresponde a las partículas que van rodando
o saltando por el lecho. Otra forma de transporte es la conocida como suspensión, la cual
se produce para velocidades mayores que el caso anterior.

Físicamente la suspensión de los sedimentos se producirá cuando la magnitud de la
corriente supere una proporción de la velocidad de sedimentación de las partículas y
diversos autores han propuesto formulaciones para determinar ese umbral.

En los procesos constructivos de las obras marítimas, las acciones generadas por los
equipos, instrumentos y los mismos elementos que componen la estructura, inducen
velocidades de corrientes en el medio y eventualmente tienen el potencial de poner en
suspensión los sedimentos que componen el lecho, los que una vez incorporados en la
columna de agua pueden moverse de acuerdo a las características de la hidrodinámica de
la zona.

En la actualidad no existen formulaciones o ecuaciones que permitan determinar la
suspensión de sedimentos a partir de los parámetros de la obra, métodos constructivos o
dimensiones de las estructuras, por lo cual en el presente estudio se propone una
metodología empírico-numérica, en base a la aplicación de métodos de escritorio y un
modelo numérico de seguimiento de partículas mediante técnicas lagrangianas, la que
corresponde al estado del arte en este tipo de simulaciones.

_**4.2.2.2 Descripción de la obra a evaluar**_

Las obras para las cuales se evaluará la suspensión de sedimentos, corresponde a las
tuberías de una planta desalinizadora, tanto para la toma como para la descarga. El
método constructivo ha sido propuesto previamente presentándose en este estudio los
aspectos más relevantes.

El Proyecto RT Sulfuros considera una nueva planta concentradora de capacidad 200
ktpd, y se abastecerá de agua desde una nueva planta desalinizadora con un caudal de
diseño de 1.956 l/s y un caudal nominal de 1.630 l/s de agua para uso industrial.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|28|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

El proyecto considera la construcción tanto de obras terrestres como marítimas, siendo de
principal atención para este estudio las zanjas donde se ubicarán las tuberías del sistema
de descarga y toma de agua de mar. En la Figura 4.6 se muestra un layout general de las
obras marítimas a evaluar.

Cabe destacar que una vez instaladas las tuberías, se estima que la suspensión de
sedimentos será baja, ya que éstas no tendrán mayores movimientos en el fondo debido a
que los lastres han sido diseñados para brindar la estabilidad necesaria.

Se ha incorporado la modelación de la suspensión de sedimentos inducida por las faenas
de construcción de las zanjas de cruce de la rompiente, tanto para la tubería de captación
como de descarga.

Las zanjas de cruce de la rompiente se extienden la distancia necesaria para brindar
protección a las tuberías hasta una profundidad de - 6 metros, por lo cual en esa
profundidad se ha definido el límite de transición para evaluar suspensión debido a la
construcción de las tuberías (lanzamiento y hundimiento) y la excavación.

Las excavaciones se realizan bajo el muelle auxiliar, siguiendo las guías del mismo en la
longitudinal. Como mecanismo de control del transporte de sedimentos, se dispone de
entibaciones laterales, las que evitaran tanto el ingreso como salida de sólidos
suspendidos.

**Figura 4.6: Configuración general de las obras marítimas contempladas en el**

**proyecto de concentradora de mineral.**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|29|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**4.2.3 Descripción de los métodos de escritorio implementados**

_**4.2.3.1 Estimación de la suspensión de sedimentos debido a la excavación**_

Para determinar los sólidos suspendidos debido al proceso de excavación se ha
implementado un método basado en las investigaciones realizadas por Collins (1995) [2],
acerca de los efectos de las excavadoras y clamshell, en la suspensión de sedimentos
durante el proceso de dragado. Cabe destacar, que de acuerdo a lo descrito en el método
constructivo, las ecuaciones propuestas por Collins son aplicables y representarán de
manera adecuada la cantidad total de sólidos en la columna de agua.

De acuerdo a la metodología de Collins (1995), la cantidad de sedimentos en suspensión
debido a faenas de excavación se puede estimar a partir de la Ecuación 4.6.

**Ecuación 4.6**

C= 0.0023ρ
~~(~~ T [B] C

3

)

Dónde:

C: Concentración total promedio en la columna de agua.

: Densidad del fluido.

B: Parámetro de la cuchara de Collins, calculado de acuerdo a:

B=

1

(2V cb ~~)~~ 3

h

Dónde:

V cb : Volumen de la cuchara de la excavadora o del clamshell.

h: Profundidad a la cual se ejecuta la excavación submarina.

T C : Tiempo de ciclo adimensional del proceso de excavación, calculado según :

T C = [v] [3] h [τ] [cb]

Dónde:

2
Dredging-induced near-field resuspended sediment concentrations and source streghts. Miscellaneous paper D-95-2. US
Army Corps of Engineers, Waterways experiment station.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|30|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

v 3 : Velocidad de sedimentación de las partículas de sedimentos.

τ cb : Tiempo de ciclo de la cuchara.

Con los resultados obtenidos desde esta estimación de la cantidad de sedimentos en

suspensión, se configuró el modelo numérico de seguimiento de partículas denominado
Particle Tracking Model (PTM), mediante el cual se estimó la dispersión y se describe a
continuación.

_**4.2.3.2 Descripción de las situaciones a modelar**_

Para cada obra marítima que se evalúa en el presente estudio, se ha considerado que su
proceso constructivo se debe realizar en condiciones de “buen tiempo”, es decir, para
condiciones oceanográficas que permitan una maniobra segura. Sin embargo, en
operación cada estructura debe ser capaz de soportar las condiciones extremas de las
variables oceanográficas, sin embargo, en el caso de las excavaciones, estas solo se
realizan en condiciones medias que permiten el correcto funcionamiento de las palas y
clamshell al ingresar en el medio marino.

Para determinar las condiciones oceanográficas medias, se realizó un análisis de clico
diario de vientos y oleaje, obteniéndose las características medias (promedio) y extrema
(máximo). Este procedimiento se realizó tanto para la estación de invierno como de
verano. En el caso de las mareas se determinó la condición de sicigias y cuadraturas,
para la estación de invierno y verano.

En función de estas condiciones oceanográficas se han configurado dos sets de
escenarios a simular, los que se presentan en la Tabla 4.1.

**Tabla 4.1: Escenarios a simular para el proceso de excavación de las zanjas.**

|Escenario|Vientos|Oleaje|Marea|Estación|
|---|---|---|---|---|
|1|Ciclo Medio|Ciclo Medio|Sicigias|Invierno|
|2|Ciclo Medio|Ciclo Medio|Cuadratura|Invierno|
|3|Ciclo Medio|Ciclo Medio|Sicigias|Verano|
|4|Ciclo Medio|Ciclo Medio|Cuadratura|Verano|

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|31|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**5** **RESULTADOS**

**5.1** **CALIBRACIÓN DEL MODELO NUMÉRICO DE OLEAJE**

**5.1.1 Sedimentos**

El oleaje como agente responsable del transporte de sedimentos es principalmente
dominante en zonas muy someras en donde la rotura del oleaje controla los procesos de
transformación de las olas. En aguas intermedias la inducción de corrientes producto de la
presencia de oleaje, puede transportar sedimentos dependiendo de sus características y
de los sedimentos presentes en la zona de estudio.

Determinar cómo evoluciona el oleaje al propagarse hacia la costa es un fenómeno
complejo de cuantificar. La metodología empleada en el presente estudio se describe en
el apartado 4.1.1 y tiene como objetivo alimentar al modelo de flujos para representar la
hidrodinámica del sector.

En la Figura 5.1 se muestra un resultado característico de los resultados de la modelación
numérica del oleaje desde aguas profundas hacia las cercanías de la costa.

**Figura 5.1: Resultados característicos del modelo CMS-WAVE para Km 14.**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|32|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Para cuantificar la bondad del modelo de oleaje, se procedió a comparar los parámetros
que resumen las características del oleaje simulados y medidos. Para ilustrar la buena
correspondencia entre las mediciones y el modelo se presenta a continuación la
comparación entre las alturas de ola significativa medidas y las simuladas.

La Figura 5.2 muestra la comparación entre alturas de olas simuladas y medidas en el
tiempo para la campaña de invierno, en esta se puede observar la buena correspondencia
entre ambas curvas de estado, la cuantificación adecuada de la cantidad de energía (la
cual se asocia con la altura de la ola) es generalmente la más relevante en la predicción
del oleaje en las cercanías de la costa.

La Figura 5.3 muestra que las alturas de olas poseen un comportamiento en el tiempo
inusual, se aprecia una tendencia al aumento de la energía en el punto de medición,
además se observa una variabilidad muy grande en la primera mitad de la serie. Esta
conducta en el tiempo pone en duda la calidad de las mediciones en la campaña de
verano, sin embargo, se ha comparado el modelo contra las mediciones disponibles,
obteniendo una correspondencia de calidad inferior a la campaña de invierno. Los
resultados de la comparación para la campaña de verano muestran que la relación entre
los datos medidos y simulados es aceptable y se ajusta a las mediciones en forma y
magnitud considerando los aspectos mencionados anteriormente.

Respectos de las características frecuenciales del oleaje, estas se consideran constantes
a lo largo de la propagación debido el enfoque paramétrico, por lo que un análisis de
comparación dato a dato o de similitud estadístico es irrelevante en el presente estudio.

Las direcciones del oleaje en el enfoque paramétrico quedan determinadas en CMS-wave
por la teoría lineal del oleaje, a través de la refracción que sufre el oleaje al propagarse
hacia la costa. La caracterización a partir de lo anteriormente expuesto es simple y
suficiente para efectos de este estudio. Para mejorar el valor del análisis direccional del
oleaje, es necesario contar con espectros direccionales en aguas profundas de modo de
cuantificar los efectos de los sistemas de olas provenientes del SW y NW los cuales
arriban en este tipo de costas abiertas.

Considerando los resultados expuestos anteriormente, se considera validado y calibrado
el modelo de oleaje.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|33|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Figura 5.2: Comparación altura significativa para campaña de invierno.**

**Figura 5.3: Comparación altura significativa para campaña de verano.**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|34|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**5.2** **CALIBRACIÓN DEL MODELO NUMÉRICO HIDRODINÁMICO**

**5.2.1 Calibración del nivel del mar**

Los resultados obtenidos de la calibración del nivel del mar para la estación de Invierno en
Km 14 son mostrados en la Figura 5.4 para las series de tiempo y Figura 5.5, para la
comparación dato a dato.

El comportamiento temporal de la evolución del nivel del mar demostró una alta
compatibilidad entre las mediciones y los resultados del modelo CMS-FLOW, tanto para la
plea como la baja mar, sin desfases ni diferencias significativas. Nótese que la simulación
numérica fue capaz de representar los ciclos de sicigias y cuadraturas típicos del
comportamiento mareal.

El valor de nivel del mar máximo medido para el periodo de análisis fue de 2.79 metros,
mientras que lo determinado por el modelo fue de 2.71 metros. Por su parte, el mínimo
fue de 1.42 y 1.44 metros para las mediciones y el modelo, respectivamente. En el caso
de los promedios ambas muestras tuvieron el mismo resultado.

La comparación dato a dato (ver Figura 5.5) mostró una buena relación entre las
mediciones y los resultados del modelo numérico CMS-FLOW. Esto es un indicador de
que las magnitudes del nivel del mar son bien reflejadas independientes del tiempo en el
que ocurran. La correlación entre ambas muestras fue de 0.98, valor que puede ser
considerado como correcto para los objetivos del estudio (ver Tabla 5.1).

El error típico, es decir, la diferencia que se determinó de la comparación de los datos
medidos y simulados fue del orden de 7 centímetros, valor que es poco significativo y de
bajo impacto en la caracterización de la hidrodinámica de Km 14.

En función de estos resultados es posible establecer que el modelo numérico es capaz de
representar correctamente las características de la variación del nivel del mar en Km 14,
por lo cual se puede considerar como una herramienta calibrada.

**Comparación entre mediciones y modelaciones del niveles del mar**

**Datos de campa de invierno 2011 - Km 14- Tocopilla**

3,0

2,8

2,6

2,4

2,2

2,0

1,8

1,6

1,4

1,2

1,0

|Col1|Col2|Col3|
|---|---|---|
||||
||||
||||
||||
||||
||||
||||
|Mediciones (m)<br>Modelo Numérico (m)|||
||||

20-08 25-08 30-08 04-09 09-09 14-09 19-09 24-09 29-09 04-10 09-10 14-10 19-10

**Fecha**

**Figura 5.4: Comparación de las series de tiempo de nivel del mar para la campaña**

**de Invierno en Km 14, Tocopilla.**

**Figura 5.5: Comparación dato a dato de los niveles del mar simulados y medidos en**

**la campaña de Invierno para Km 14, Tocopilla** **.**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|36|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Tabla 5.1: Indicadores estadísticos de la comparación de los niveles del mar**

**simulados y medidos para la campaña de Invierno en Km 14, Tocopilla.**

|Indicador Estadístico|Valor|
|---|---|
|Coeficiente de correlación|0.98|
|Error típico (m)|0.07|
|Covarianza (m)|0.09|

Aplicando la misma configuración del modelo empleada para el invierno, se simuló la
condición de verano obteniéndose resultados similares a los datos de campo.

La comparación de las series de tiempo mostradas en la Figura 5.6 es indicadora de la
buena correspondencia entre el modelo CMS-FLOW y las mediciones de terreno, sin
detectarse desfases significativos. El valor máximo simulado fue de 2.76 metros mientras
que el campo 2.82 metros. Para el caso del mínimo las mediciones mostraron un valor de
1.46 metros, mientras que CMW-FLOW 1.52 metros.

La comparación dato a dato de la Figura 5.7 presentó una buena relación entre los
resultados modelados y los medidos, ajustándose de manera significativa a la recta de
45°. La correlación obtenida fue de 0.99 con un error típico de 0.05 metros (ver Tabla 5.2),
resultados que pueden ser considerados como correctos.

En función de los resultados obtenidos para la campaña de Verano, considerando la
configuración calibrada de Invierno, se puede concluir que el modelo CMS-FLOW se
encuentra validado para representar las condiciones de nivel del mar en la zona de Km

14.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO EDICIÓN / REVISIÓN<br>IT -MOD-INIMA012015 2/2|37|
|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015<br>Emitido por:<br>EcoTecnos S.A.|Fecha de emisión:<br>14/09/2015<br>Emitido por:<br>EcoTecnos S.A.|

**Comparación entre mediciones y modelaciones del niveles del mar**

**Datos de campa de Verano 2012 - Km 14 - Tocopilla**

3,0

2,8

2,6

2,4

2,2

2,0

1,8

1,6

1,4

1,2

1,0

|Col1|Col2|Col3|
|---|---|---|
||||
||||
||||
||||
||||
||||
||||
||Mediciones (m)<br>Modelo Numérico (m)||
||||

12-01 17-01 22-01 27-01 01-02 06-02 11-02 16-02 21-02 26-02

**Fecha**

**Figura 5.6: Comparación de las series de tiempo de nivel del mar para la campaña**

**de Verano en Km 14, Tocopilla.**

**Figura 5.7: Comparación dato a dato de los niveles del mar simulados y medidos en**

**la campaña de Verano para Km 14, Tocopilla** **.**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|38|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Tabla 5.2: Indicadores estadísticos de la comparación de los niveles del mar**

**simulados y medidos para la campaña de Verano en Km 14, Tocopilla** **.**

|Indicador Estadístico|Valor|
|---|---|
|Coeficiente de correlación|0.99|
|Error típico (m)|0.05|
|Covarianza (m)|0.09|

**5.2.2 Calibración de las corrientes**

En la Figura 5.8 se ilustran las magnitudes de corriente asociadas a la estación de
Invierno para Km 14, para cada uno de los ensayos numéricos propuestos para el día 24
de Agosto de 2011 a las 07:00 hrs. En primera instancia se presentan los resultados
obtenidos para la condición forzada solo con mareas (ensayo 1) de la cual se logra
apreciar que las velocidades inducidas serían del orden de 0 a 0.004 m/s (0.4 cm/s).

Al incluirse los efectos conjuntos de mareas y vientos (ensayo 2), se aprecia que las
magnitudes se incrementan en las cercanías de la costa alcanzando valores del orden de
0.02 m/s (2 cm/s). Esta condición podría estar dada por efectos de apilamiento que
genera el viento al soplar sobre una costa abierta ( _wind setup_ ), debido al trasporte de

masa.

Comparativamente los resultados del ensayo 1 y 2 mostraron el mismo patrón de
circulación, sin embargo, las magnitudes aumentaron significativamente en torno a un
94% cuando se incorporó la acción del viento.

La incorporación del oleaje a la generación de corrientes (ensayo 3) induce un
comportamiento más caótico, con aumento de las magnitudes de las corrientes en todo el
dominio numérico con magnitudes en torno a 0.02 m/s (2 cm/s). En las cercanías de la
costa las modificaciones del patrón de circulación no presentaron incrementos
significativos.

De la comparación de los resultados obtenidos del ensayo 2 y 3, se determinó que la
inclusión de las olas tiene una tendencia promedio a disminuir las magnitudes de la
corriente total en un 40% aproximadamente. Esto podría deberse a que la naturaleza
oscilatoria del oleaje induce flujos de masa en el sentido de avance del tren de ondas,
mientras que las mareas y vientos tienen una mayor variabilidad direccional, lo que

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|39|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

vectorialmente implicaría instantes de suma y otros de restas a la composición final de la
corriente.

Al compararse los ensayos 1, 2 y 3 con los datos de campo recopilados durante el
invierno de 2011, se obtuvieron resultados dispares y se detectó que las principales
forzantes son las mareas y vientos, mientras que el oleaje actúa en menor manera.

En la Figura 5.9 se presentan los resultados de la comparación de las series de tiempo de
corrientes generadas por mareas obtenidas desde el modelo CMS-FLOW y las
mediciones de campo. Del análisis de esta ilustración se advierte que considerar sólo las
mareas como forzante de la hidrodinámica de Km 14, no es correcto ya que las
magnitudes son bajas y no representa el funcionamiento de la zona de estudio.

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|40|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

|Col1|Col2|Col3|
|---|---|---|
|Ensayo 1: Mareas<br>24 - Agosto - 2011 07:00|Ensayo 2: Mareas+Vientos<br>24 - Agosto - 2011 07:00|Ensayo 3: Mareas+Vientos+Olas<br>24 - Agosto - 2011 07:00|
|Leyenda:<br>|Leyenda:<br>|Leyenda:<br>|

**Figura 5.8: Resultados típicos de la hidrodinámica del modelo CMS-FLOW para cada uno de los ensayos realizados, Invierno.**

Este comportamiento encontrado en la Figura 5.9 se puede considerar como esperable,
ya que las mareas cobran una principal importancia en la hidrodinámica cuando la
configuración geomorfológica de la costa es del tipo Bahía o presenta encajonamientos
significativos, mientras que para litorales abiertos son menos relevantes.

**Comparación entre mediciones y modelaciones de corrientes - Ensayo 1**

**Datos de campa de invierno 2011 - Km 14 - Tocopilla**

0,7

0,6

0,5

0,4

0,3

0,2

0,1

0,0

|Mediciones (m)<br>Modelo Numérico (m)|Col2|Col3|
|---|---|---|
||||
||||
||||
||||
||||
||||

20-08 25-08 30-08 04-09 09-09 14-09 19-09 24-09 29-09 04-10 09-10 14-10 19-10

**Fecha**

**Figura 5.9: Comparación de las series de tiempo de corrientes medidas, con los**

**resultados del ensayo 1, para la campaña de Invierno en Km 14, Tocopilla.**

En la Figura 5.10 se presentan los resultados de la comparación de las series de tiempo
de corrientes medidas y modeladas para el ensayo 2, es decir, considerando como
forzantes las mareas y el viento. Nótese que ambas señales se comparan de manera
adecuada y si bien no son exactamente iguales, esto podría deberse a que el modelo
numérico CMS-FLOW es del tipo bidimensional y por lo tanto las magnitudes de las
corrientes son integradas en la vertical.

El modelo numérico CMS-FLOW al ser forzado con vientos y mareas, mostró un
comportamiento similar a las mediciones, indicando valores máximos en periodos de
tiempo compatibles con lo indicado en las mediciones. En el caso de los mínimos, se
obtuvo una leve tendencia a la sub-estimación.

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

En términos generales las diferencias obtenidas entre los resultados del modelo numérico
y los datos de campo, podrían asociarse a los siguientes factores principales:

 - Incertidumbre propia de las mediciones de campo (vientos, corrientes y mareas),
debido a los instrumentos.

 Tridimensionalidad de los procesos físicos.

Sin embargo, se estima que estas diferencias son adecuadas para el desarrollo del
estudio de suspensión de sedimentos y no afectarán los resultados globales.

**Comparación entre mediciones y modelaciones de corrientes - Ensayo 2**

**Datos de campa de invierno 2011 - Km 14 - Tocopilla**

0,6

0,5

0,4

0,3

0,2

0,1

0,0

|Mediciones (m)<br>Modelo Numérico (m)|Col2|Col3|
|---|---|---|
||||
||||
||||
||||
||||

20-08 25-08 30-08 04-09 09-09 14-09 19-09 24-09 29-09 04-10 09-10 14-10 19-10

**Fecha**

**Figura 5.10: Comparación de las series de tiempo de corrientes medidas, con los**

**resultados del ensayo 2, para la campaña de Invierno en Km 14, Tocopilla.**

En la Figura 5.11 se presentan los resultados obtenidos para la comparación de los
resultados del ensayo numérico 3 realizado en el modelo y los datos de campo. De su
análisis se advierte que la inclusión de las corrientes por oleaje induce disminuciones de
las magnitudes totales de corriente, tal como se comentara previamente.

Al comparar la forma de las series de tiempo, se puede apreciar que presentan algunas
diferencias, no siendo un buen ajuste entre ambas bases de datos.

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

**Comparación entre mediciones y modelaciones de corrientes - Ensayo 3**

**Datos de campa de invierno 2011 - Km 14 - Tocopilla**

0,6

0,5

0,4

0,3

0,2

0,1

0,0

|Mediciones (m)<br>Modelo Numérico (m)|Col2|Col3|
|---|---|---|
||||
||||
||||
||||
||||

20-08 25-08 30-08 04-09 09-09 14-09 19-09 24-09 29-09 04-10 09-10 14-10 19-10

**Fecha**

**Figura 5.11: Comparación de las series de tiempo de corrientes medidas, con los**

**resultados del ensayo 3, para la campaña de Invierno en Km 14, Tocopilla.**

A continuación se presentan los resultados obtenidos de la comparación dato a dato,
despreciando el tiempo en el que ocurren las magnitudes. Cabe destacar, que se han
omitidos los resultados asociados al ensayo numérico 1, ya que en el análisis de series de
tiempo se demostró que considerar las mareas como única forzante, no se representa de
manera correcta la hidrodinámica de Km 14 (ver Figura 5.9).

La comparación dato a dato para el ensayo 2 mostrada en la Figura 5.12, indicó que
existe una asociación adecuada entre los resultados del modelo y las mediciones, con un
coeficiente de correlación de 0.63 y un error típico de 0.07 m/s. La mayoría de los datos
se ajustó correctamente a la línea de 45°, con una desviación estándar del orden de 0.08

m/s.

Si bien el coeficiente de correlación puede ser considerado como bajo, el error típico
también lo es. Al comparar los valores promedio de las corrientes modeladas y medidas,
se determinó que las magnitudes ascienden a 0.17 m/s y 0.18 m/s, respectivamente. En el
caso de los extremos (máximo y mínimo) el modelo numérico presentó corrientes de 0.45
m/s y 0.01 m/s, mientras que los datos de campo 0.59 m/s y 0.02 m/s.

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|44|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Los indicadores estadísticos descritos recientemente, permiten establecer que considerar
las forzantes de mareas y vientos de manera conjunto, es adecuado y representa de
manera correcta la hidrodinámica de la zona de estudio.

**Figura 5.12: Comparación dato a dato de las corrientes medidas en la campaña de**

**Invierno y resultados del ensayo 2 para Km 14, Tocopilla.**

La comparación de los datos modelados y medidos para en el ensayo 3, es decir,
incluyendo el efecto del oleaje, es presentado en la Figura 5.13. De similar manera a lo
presentado previamente para forzantes de viento y marea, la asociación de los datos con
la recta de 45° es adecuada, a pesar de las desviaciones que se presentan en la
dispersión.

La correlación obtenida entre las mediciones y modelaciones fue de 0.55 con error típico
de 0.07 m/s. Este descenso en la correspondencia en comparación al ensayo 2 (de 0.63 a
0.55), podría deberse a la subestimación que presentó el modelo al incluirse el oleaje. Los
valores promedios obtenidos fueron de 0.17 m/s y 0.18 m/s para el modelo y mediciones,
respectivamente.

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|45|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Para el caso de los valores máximos y mínimos modelados, se obtuvieron magnitudes
iguales a 0.44 m/s y 0.01 m/s, respectivamente, mientras que en las mediciones, estos
mismos indicadores estadísticos mostraron valores iguales a 0.59 m/s y 0.02 m/s.

**Figura 5.13: Comparación dato a dato de las corrientes medidas en la campaña de**

**Invierno y resultados del ensayo 3 para Km 14, Tocopilla.**

En función de los resultados obtenidos para la campaña de invierno, se puede concluir
que la configuración del modelo numérico considerando solamente vientos y mareas
como forzantes de la hidrodinámica, así como también el tamaño y resolución de la grilla,
es adecuada y se pude considerar como calibrado.

Para verificar la validez de los supuestos y configuración del modelo numérico, se
presentan a continuación los resultados de la comparación entre las corrientes simuladas
y las medidas.

En la Figura 5.14 se muestran los resultados de la comparación de las series de tiempo
de magnitud de corrientes para el instrumento SONTEK, mientras que para el ADCP RDI
se preparó la Figura 5.15.

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

En el caso del instrumento SONTEK (ver Figura 5.14), las series de tiempo medidas y
simuladas mostraron una buena correspondencia entre ellas. La leve sub-estimación
detectada en el proceso de calibración disminuye para los datos de Verano en esta
locación, lo que podría deberse a la menor variabilidad climática, propia de esta estación
del año.

**Comparación entre mediciones y modelaciones de corrientes - Ensayo 2**

**Datos de campa de Verano 2012 - Km 14 - Tocopilla**

0,6

0,5

0,4

0,3

0,2

0,1

0,0

|Mediciones (m)<br>Modelo Numérico (m)|Col2|
|---|---|
|||
|||
|||
|||
|||

12-01 17-01 22-01 27-01 01-02 06-02 11-02 16-02 21-02 26-02

**Fecha**

**Figura 5.14: Comparación de las series de tiempo de corrientes medidas y**
**simuladas, para la campaña de Verano, instrumento SONTEK fondeado en Km 14,**

**Tocopilla.**

El comportamiento de las series de tiempo de corriente para el instrumento RDI (ver
Figura 5.15), mostraron un comportamiento similar al detectado para el ADCP SONTEK,
es decir, existe una buena correspondencia entre los resultados del modelo numérico y
las mediciones de campo; además la tendencia a la sub-estimación disminuyó.

Cabe destacar, que si bien el modelo numérico presenta resultados temporales que no se
ajusta en un 100% con las mediciones, tanto para el caso del instrumento SONTEK como
RDI, las corrientes simuladas se encuentran dentro de la dispersión de los datos con
tendencias similares.

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

De manera complementaria, se presentan los resultados de la comparación dato a dato
entre las modelaciones numéricas y mediciones, tanto para la locación del instrumento
SONTEK como el RDI.

**Comparación entre mediciones y modelaciones de corrientes - Ensayo 2**

**Datos de campa de Verano 2012 - Km 14 - Tocopilla**

0,6

0,5

0,4

0,3

0,2

0,1

0,0

|Mediciones (m)<br>Modelo Numérico (m)|Col2|
|---|---|
|||
|||
|||
|||
|||

12-01 17-01 22-01 27-01 01-02 06-02 11-02 16-02 21-02 26-02

**Fecha**

**Figura 5.15: Comparación de las series de tiempo de corrientes medidas y**
**simuladas, para la campaña de Verano, instrumento RDI fondeado en Km 14,**

**Tocopilla.**

En la Figura 5.16 se presentan los resultados de la comparación dato a dato de
magnitudes de corriente para la ubicación del instrumento SONTEK. Del análisis de ella,
se advierte que existe una asociación adecuada entre los datos simulados y los
registrados en terreno. El índice de correlación obtenido fue de 0.72 y el error típico de
0.09 m/s.

El valor promedio de la corriente modelada fue de 0.20 m/s, mientras que la medida 0.21
m/s. Para el caso de los valores extremos (máximo y mínimo) la simulación arrojó valores
de 0.37 m/s y 0.01 m/s, mientras que los datos de campo 0.55 m/s y 0.03 m/s,
respectivamente.

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|48|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

La comparación de los indicadores estadísticos presentados recientemente, muestran que
el comportamiento general del modelo CMS-FLOW para la ubicación del instrumento
SONTEK es concordante con los valores de corriente registrados durante la campaña de
Verano. Cabe destacar que las diferencias obtenidas, no serían significativas y por lo
tanto no afectarían la caracterización de la hidrodinámica mediante esta herramienta

numérica.

**Figura 5.16: Comparación dato a dato de las corrientes medidas y simuladas, para**

**la campaña de Verano, instrumento SONTEK fondeado en Km 14, Tocopilla.**

En la Figura 5.17 se presentan los resultados obtenidos de la comparación dato a dato
entre las mediciones de campo del instrumento RDI y la simulación numérica. Se advierte
que la correspondencia entre ambas bases de datos es adecuada, ya que se ajustan de
manera significativa en torno a la recta de 45°.

El coeficiente de correlación encontrado para el caso del instrumento RDI fue de 0.71,
mientras que el error típico de 0.08 m/s. Nuevamente se repite similar tendencia que la
encontrada para el instrumento SONTEK (ver Figura 5.16), con un aumento significativo

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|49|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

de la correspondencia (desde 0.63 a 0.71) el cual podría deberse a la menor variabilidad
climática de la estación de verano.

La magnitud promedio de la corriente mostró resultados de 0.21 m/s y 0.16 m/s, para el
modelo y mediciones, respectivamente. Para el caso del máximo se obtuvo 0.40 m/s y
0.53 m/s, mientras que para los mínimos 0.01 m/s y 0.02 m/s, para la simulación y los
datos de campo, respectivamente.

Al igual que en el caso del instrumento SONTEK, el modelo numérico CMS-FLOW es
capaz de representar de manera correcta la hidrodinámica para la estación de Verano

**Figura 5.17: Comparación dato a dato de las corrientes medidas y simuladas, para**

**la campaña de Verano, instrumento RDI fondeado en Km 14, Tocopilla.**

En función de los resultados obtenidos, tanto para la campaña de invierno como de
verano, se puede concluir que el modelo CMS-WAVE representa de manera correcta la
hidrodinámica cuando es forzado con mareas y vientos, siendo las diferencias
encontradas de la comparación de la simulación y los datos de campo, despreciables para
los efectos del presente estudio.

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|50|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**5.3** **MODELACION NUMÉRICA DE LA SUSPENSION DE SEDIMENTOS**

**5.3.1 Cantidad de sedimentos en suspensión**

Los resultados obtenidos desde la aplicación de los métodos de gabinete para estimar la
cantidad de sedimentos en suspensión, son presentados a continuación de manera
gráfica.

En el caso de las excavaciones los resultados son mostrados en la Figura 5.18, la que
ilustra un análisis de sensibilidad para distintas capacidades de las palas, en cada una de
las profundidades que se construirá la zanja.

Cabe destacar que las concentraciones de sedimentos en suspensión corresponden a
promedios totales en la columna de agua y debido a eso es que se obtienen magnitudes
más bajas para profundidades más altas.

Considerando que las excavaciones se realizarán mediante equipamientos con capacidad
de 45 toneladas y un clamshell, se ha considerado que las concentraciones de
sedimentos en suspensión asociadas a un volumen de pala de 2.5 m [3], es el que mejor
representa la situación.

**Figura 5.18: Estimación de la cantidad de sedimentos en suspensión debido al**

**proceso de excavación de las zanjas de cruce de la rompiente.**

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|51|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Como datos de entrada para la modelación de la dispersión se ha ingresado la
concentración de sedimentos en suspensión de manera variable en función de la distancia
y profundidad del perfil de excavación, siendo sus valores integrados en la profundidad
mostrados en la Figura 5.19.

**Figura 5.19: Magnitudes de concentración de sedimentos en suspensión empleados**

**en el modelo numérico de dispersión de partículas PTM. A) En la zona de**

**rompientes y B) Después de la zona de rompientes.**

Nótese que todas las magnitudes de sólidos suspendidos, están por debajo del límite
máximo establecido por el D.S. N° 90/2000.

**5.3.2 Caracterización de los ciclos diarios**

Los resultados obtenidos para los ciclos diarios de las variables oceanográficas
empleadas para la simulación de los escenarios de suspensión de sedimentos de cada
una de las estructuras evaluadas, se presentan en la Figura 5.20 para la estación de
invierno y Figura 5.21 para Verano.

En términos generales las condiciones de invierno son más energéticas que las de
Verano, con algunas excepciones.

En el caso de los vientos se aprecia que en condición media la máxima magnitud es de
7.9 m/s en Invierno, mientras que en Verano 8.4 m/s. Además se aprecia una rotación de
la direcciones de menor magnitud.

El ciclo diario medio y extremo de vientos en la estación de Verano mostró una mayor
tendencia al aumento de las magnitudes a partir de las 08:00, alcanzando el valor máximo
a las 18:00. Este comportamiento no se detectó para las direcciones.

Las características de las alturas de olas mostraron un aumento significativo al pasar de
Verano a Invierno, creciendo en promedio 0.5 metros aproximadamente. Para el caso de

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|52|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

los periodos, ambas estaciones mostraron valores asociados a oleaje tipo swell de
generación remota con valores medios cercanos a 13 segundos y máximos similares a 20
segundos.

Las alturas de olas mostraron un comportamiento promedio de Verano de 1.0 metros y
máximo de 1.5 metros, mientras que el Invierno de 1.5 metros y mayor a 2.5 metros, para
similares características.

Las direcciones de oleaje mostraron una leve tendencia a acercarse a norte en la medida
que se cambia de la estación de Invierno a Verano. Esta condición podría deberse al
arribo del oleaje energético de largo periodo asociado al swell de generación remota del
hemisferio Norte.

Por su parte, las mareas mostraron amplitudes similares entre los ciclos diarios de
Invierno y Verano, independiente de si se analizan las sicigias o las cuadraturas. La
máxima pleamar presentó una altura por sobre los 2.5 metros, mientras que la mínima
bajamar fue de 1.5 metros.

Preliminarmente se puede establecer que las máximas condiciones de suspensión y
dispersión de los sedimentos se producirán para los ciclos diarios asociados a los valores
máximos, ya que su energía presenta un mayor potencial de transportar las partículas a lo
largo de la costa.

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|53|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Figura 5.20: Identificación de los ciclos diarios para los datos oceanográficos de la**

**campaña de Invierno en Km 14.**

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|54|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Figura 5.21: Identificación de los ciclos diarios para los datos oceanográficos de la**

**campaña de Verano en Km 14** **.**

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|55|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**5.3.3 Dispersión de sedimentos en las zanjas de excavación**

Para facilitar la comparación con lo previamente desarrollado y presentado en la EIA
incluido en el Anexo 38 de la adenda N°1, se ha modelado la excavación de las zanjas
solo con inclusión de las entibaciones, manteniendo la totalidad de parámetros empleados
anteriormente, siendo estos el largo y ancho.

_**5.3.3.1 Zanja de excavación - Descarga**_

En la Figura 5.22 se presentan los resultados de la simulación de dispersión de partículas
para cada uno de los escenarios hidrodinámicos considerados, en función de las faenas
de excavación de la zanja de lanzamiento de las tuberías de descarga. Nótese que las
líneas negras de cada una de las figuras, simbolizan las entibaciones laterales que se han
proyectado para el proceso constructivo.

Para todos los casos simulados se aprecia que los sólidos suspendidos no abandonan las
zonas de las faenas, debido a las entibaciones laterales reduciendo de este modo su zona

de influencia.

Las mayores concentraciones de partículas se presentarían para las profundidades más
bajas de inicio de excavación, situación que es concordante con las estimaciones de
sólidos suspendidos para distintos tamaños de palas ilustrada previamente en la Figura

5.18.

**Figura 5.22: Resultados de la dispersión de sedimentos en suspensión en el tiempo**

**según el modelo numérico PTM, para todos los escenarios hidrodinámicos**

**considerando entibaciones laterales.**

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|56|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Es importante destacar que, el control de la dispersión de las partículas está dado por la
acción de las entibaciones laterales.

Para ilustrar los efectos de las entibaciones laterales, se presenta en la Tabla 5.3 que
compara las áreas con sólidos suspendidos desde las faenas de excavación de la zanja
de lanzamiento de las tuberías de descarga. De ella, se advierte que en todos los
escenarios los efectos de disminución de la zona de influencia superarían los 1000 m [2] .

**Tabla 5.3: Áreas esperadas con sólidos suspendidos debido a las faenas de**

**excavación de la zanja de descarga.**

|Escenario|Con entibaciones (m2)|Sin entibaciones (m2)|Disminución por<br>entibaciones (m2)|
|---|---|---|---|
|1|4053|7400|3347|
|2|3555|6761|3206|
|3|3427|5180|1753|
|4|3158|6954|3796|

De modo complementario, a través de las figuras 4.23 a la 4.26, se muestran las áreas
que tendrían sólidos suspendidos, considerando tanto la situación con y sin entibaciones.

**Figura 5.23: Área total esperada con partículas suspendidas con y sin entibaciones,**

**para la zanja de descarga en el escenario hidrodinámico 1.**

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|57|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Figura 5.24: Área total esperada con partículas suspendidas con y sin entibaciones,**

**para la zanja de descarga en el escenario hidrodinámico 2.**

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|58|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Figura 5.25: Área total esperada con partículas suspendidas con y sin entibaciones,**

**para la zanja de descarga en el escenario hidrodinámico 3.**

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|59|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Figura 5.26: Área total esperada con partículas suspendidas con y sin entibaciones,**

**para la zanja de descarga en el escenario hidrodinámico 4.**

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|60|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

_**5.3.3.2 Zanja de excavación - Toma**_

En la Figura 5.27 se presentan los resultados obtenidos para la simulación de la
dispersión de sedimentos suspendidos, considerando la excavación para las tuberías de
toma en todos los escenarios hidrodinámicos. Las líneas negras que se han incluido,
delimitan las entibaciones laterales, mientras que los puntos naranjos simbolizan los
sedimentos suspendidos.

Para todos los escenarios hidrodinámicos, se advierte que los sedimentos suspendidos
son contenidos por las entibaciones laterales, sin permitir fugas significativas en sus
fronteras abiertas.

**Figura 5.27: Resultados de la dispersión de sedimentos en suspensión en el tiempo**

**según el modelo numérico PTM, para todos los escenarios hidrodinámicos**

**considerando entibaciones laterales.**

De similar manera a lo indicado para las tuberías de descarga, los efectos de las
entibaciones laterales es significativo y disminuye el área de influencia de los sólidos
suspendidos en las faenas de excavación.

En la Tabla 5.4, se indican las áreas estimadas para la situación con y sin entibaciones,
así como también las diferencias esperadas. De ella se advierte que en todos los
escenarios hidrodinámicos se esperan disminuciones mayores a 6000 m [2] .

Finalmente y a modo de complementar la información mostrada anteriormente, se
presenta en las figuras 4.28 a la 4.31, las áreas de influencia en condición con y sin
entibaciones, para cada uno de loes escenarios hidrodinámicos testeados.

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|61|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Tabla 5.4: Áreas esperadas con sólidos suspendidos debido a las faenas de**

**excavación de la zanja de toma.**

|Escenario|Con entibaciones (m2)|Sin entibaciones (m2)|Disminución por<br>entibaciones (m2)|
|---|---|---|---|
|1|2780|11769|8989|
|2|2949|11717|8768|
|3|2449|9567|7118|
|4|3174|9174|6000|

**Figura 5.28: Área total esperada con partículas suspendidas con y sin entibaciones,**

**para la zanja de toma en el escenario hidrodinámico 1.**

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|62|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Figura 5.29: Área total esperada con partículas suspendidas con y sin entibaciones,**

**para la zanja de toma en el escenario hidrodinámico 2.**

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|63|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Figura 5.30: Área total esperada con partículas suspendidas con y sin entibaciones,**

**para la zanja de toma en el escenario hidrodinámico 3.**

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|64|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Figura 5.31: Área total esperada con partículas suspendidas con y sin entibaciones,**

**para la zanja de toma en el escenario hidrodinámico 4.**

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|65|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**6** **CONCLUSIONES**

A partir de lo expuesto precedentemente, se ha logrado concluir en lo siguiente:

**6.1** **CON RESPECTO DE LAS HERRAMIENTAS NUMÉRICAS Y MÉTODOS**

**APLICADOS**

CMS-wave presenta ventajas respecto de los modelos basados en la teoría de ondas y
promediados en la fase que resuelven la ecuación de acción de onda, ya que incorpora de
forma teóricamente robusta los fenómenos de transformación dependientes de la fase,
como lo son reflexión y difracción.

La metodología implementada es adecuada para caracterizar los casos de oleaje, con el
objeto de complementar la modelación de la hidrodinámica del sector. La calibración y
validación muestran que la correspondencia entre los datos medidos y simulados es
adecuada, concluyéndose válido el modelo implementado.

El aporte del oleaje en la circulación para los sectores en estudio, no fue dominante
respecto de otras forzantes consideradas en la caracterización hidrodinámica de la zona
de interés.

El modelo numérico CMS-FLOW representa de manera correcta las condiciones
hidrodinámicas de Km 14, siendo una herramienta confiable para representar los niveles
del mar y las magnitudes de las corrientes inducidas por mareas y vientos costeros.

De esta forma, la metodología que ha sido utilizada para lograr la estimación de los
sedimentos en suspensión y su dispersión, permite conocer de manera efectiva los
efectos de la construcción y operación de un conjunto de obras marítimas en el medio,
siendo el modelo numérico PTM una herramienta de gran utilidad que, mezclado con
métodos convencionales de escritorio, permiten describir de manera adecuada los efectos
inducidos en el medio.

**6.2** **CON RESPECTO DE LA FASE DE CONSTRUCCIÓN DE LAS OBRAS**

**MARITIMAS**

Los resultados de la aplicación del modelo numérico PTM y los métodos de escritorio en
el proceso de construcción de las tuberías de captación y descarga, permiten detectar que
existe un potencial de suspensión de sedimentos que entrarían en contacto con la línea
de costa mediante la dispersión inducida por la hidrodinámica, siendo la zona de
rompientes la que proveería la mayor concentración de partículas distribuidas de manera
relativamente homogénea en la columna de agua.

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN DE SUSPENSION DE<br>SEDIMENTOS Km 14|No DOCUMENTO<br>IT -MOD-INIMA012015|EDICIÓN / REVISIÓN<br>2/2|66|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN DE SUSPENSION DE**<br>**SEDIMENTOS Km 14**|Fecha de emisión:<br>14/09/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

El proceso de excavación pondrá en suspensión concentraciones de sedimentos bajo los
300 mg/L en la zona de rompientes y su dispersión, debido al proceso de advección
generado por las corrientes, se encontraría acotado por la acción de las entibaciones
laterales.

En consecuencia, la presencia de las entibaciones laterales proyectadas para el muelle
auxiliar, aportarán de manera positiva a la disminución del área de influencia de los
sólidos suspendidos, acotando la dispersión de los sedimentos tanto de manera lateral
como longitudinal.

Adicionalmente y considerando la menor longitud de muelle,menor ancho de fondo de
mar intervenido y menor largo de las zanjas, se concluye por extensión que la nueva
metodología de construcción del muelle auxiliar y zanjas, propuestas por el consorcio
INIMA CVV, tendrá un impacto considerablemente menor que el declarado en el EIA, en
lo relativo a la suspensión de sólidos debido a las faenas de construcción.

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**