---
title: INGECOSAL – Gerencia de Proyectos
author: Mariana Correa
date: D:20230215131838-03'00'
language: es
type: general
pages: 10
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - “MEMORIA DE CÁLCULO ESTRUCTURAL LOSAS”
-->

**1512-INM-001-CIV-MC-001**

# “MEMORIA DE CÁLCULO ESTRUCTURAL LOSAS”

## SRES. INMOBILIARIA CONSORCIO HABITACIONAL DE CHILE

**REVISIÓN 0**

**FEBRERO 2023**

**INGECOSAL - Gerencia de Proyectos** **1512-INM-001-CIV-MC-001- REV 0**

|1. REVISIONES|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Ediciones del Documento**|**Ediciones del Documento**|**Ediciones del Documento**|**Ediciones del Documento**|**Ediciones del Documento**|**Ediciones del Documento**|
|**Revisión**|**Fecha**|**Estado del Documento**|**Por**|**Rev.**|**Apr.**|
|A|DIC-22|EMISION PRELIMINAR|CPC|CTS|JQS|
|B|DIC-22|SE INCORPORAN COMENTARIOS|CPC|CTS|JQS|
|0|FEB-23|EMITIDO PARA CONSTRUCCIÓN|CPC|CTS|JQS|
|||||||
|||||||
|||||||

Este documento es propiedad de Ingecosal, por lo que queda prohibida su utilización parcial o total con otro propósito que no sea
el estipulado en el contrato. 

**INGECOSAL - Gerencia de Proyectos** **1512-INM-001-CIV-MC-001- REV 0**

### 2. ANTECEDENTES GENERALES 2.1.Alcance

La presente memoria de cálculo muestra el análisis y dimensionamiento de la losa de
hormigón armado de la Sala de Operadores y Sala Eléctrica Modular (Losa 1) y
Generador (Losa 2) de la planta de aguas de Praderas de Lo Aguirre.

### 2.2.Descripción de la Estructura

Las dimensiones de las losas son de 8.7 m de largo por 8.14 m de ancho para la Losa 1
y 8.7 m de largo por 4.44 m de ancho para la Losa 2, ambas con un espesor de 15 cm,
donde sobre esta se ubicarán los contenedores correspondientes a la sala eléctrica, sala
de operaciones y generador.

Figura 1. Losa Sala de Operadores y Sala Eléctrica Modular.

Este documento es propiedad de Ingecosal, por lo que queda prohibida su utilización parcial o total con otro propósito que no sea
el estipulado en el contrato. 

**INGECOSAL - Gerencia de Proyectos** **1512-INM-001-CIV-MC-001- REV 0**

Figura 2. Losa Generador.

### 2.3. Modelación y Análisis realizados 2.3.1. Modelación

Las losas de hormigón armado fueron modeladas y diseñadas en el software SAP2000
V23.2.0, de donde se obtienen los resultados de esfuerzos en el suelo y en la losa.

Este documento es propiedad de Ingecosal, por lo que queda prohibida su utilización parcial o total con otro propósito que no sea
el estipulado en el contrato. 

**INGECOSAL - Gerencia de Proyectos** **1512-INM-001-CIV-MC-001- REV 0**

Figura 3. Esquema 3D de modelación de la Losa 1 en diseño.

Figura 4. Esquema 3D de modelación de la Losa 2 en diseño.

Este documento es propiedad de Ingecosal, por lo que queda prohibida su utilización parcial o total con otro propósito que no sea
el estipulado en el contrato. 

**INGECOSAL - Gerencia de Proyectos** **1512-INM-001-CIV-MC-001- REV 0**

### 3. CÓDIGOS Y DOCUMENTOS

Las siguientes son las normas y reglamentos a considerar en el estudio:

✓ NCh 1537 of 2009: Cargas permanentes y sobrecargas de uso.
✓ Nch 3171 of 2010: Diseño estructural. Disposiciones generales y combinaciones

de cargas.
✓ NCh 204 of 2006: Acero-Barras Laminado en Caliente para Hormigón Armado.
✓ NCh 211 of 2012: Barras con resaltes en obras de hormigón armado.
✓ NCh 170 of 2016: Hormigones - Requisitos Generales.
✓ NCh 2369 of 2003: Diseño Sísimo de estructuras e instalaciones industriales.

✓ ACI 318-2019: American concrete Institute.

### 4. MATERIALES 4.1.Hormigón

Para las losas se empleará un hormigón, grado G20 con una resistencia característica
R 28 3 200 kg/cm [2] a los 28 días y 90 % de nivel de confianza. El diseño de los elementos
de Hormigón armado se realiza según el código ACI 318R-11. Las características
principales del hormigón empleado son:

Peso específico: 2400 kg/m [3]
Modulo de Elasticidad: 250000 kg/cm [2]
Coeficiente de Poison: 0.2
Resistencia de diseño (f’c) 200 kg/cm [2]

**4.2.** **Acero**

El acero de refuerzo empleado para hormigón armado es calidad A 44-28 H de alta
resistencia, con una tensión de fluencia mínima fy 3 2.800 kg/cm [2] (con resaltes).

### 5. CARGAS DE DISEÑO

Las cargas y sobrecargas se estiman según las normas indicadas en el punto 3 del
presente documento. El análisis estructural las cargas se consideran según su
naturaleza, esto es:

✓ Cargas permanentes: Peso propio y sobrecarga.
✓ Cargas eventuales: Sismo y viento.

Este documento es propiedad de Ingecosal, por lo que queda prohibida su utilización parcial o total con otro propósito que no sea
el estipulado en el contrato. 

**INGECOSAL - Gerencia de Proyectos** **1512-INM-001-CIV-MC-001- REV 0**

**5.1.** **Peso Propio**

Las cargas de peso propio (PP) son las producidas por la aceleración de gravedad sobre
los elementos de hormigón de la estructura. Para ello se utiliza el peso específico de los
materiales, y la aceleración de gravedad con un valor de 9.8 m/s [2] . El programa SAP2000
V23.2.0, utilizado en la modelación, calcula de manera interna el peso de la estructura.
Los pesos específicos de los materiales considerados son:

Hormigón Armado 2400 kg/m [3]
Acero estructural 7850 kg/m [3]

**5.2.** **Sobrecarga**

Las sobrecargas (SC) consideradas se ajustan a lo indicado en la norma Nch 1537
y son las siguientes:

Sobrecarga de uso en losas 500 kg/m [2]

### 5.3.Sismo

Para la acción sísmica sobre la estructura, se realiza un análisis estático equivalente, el
cual se aplica en dos direcciones horizontales y ortogonales entre sí, además de
considerarse en la dirección vertical (SV).

La masa sísmica utilizada para el cálculo de las cargas sísmicas se efectuará
considerando los siguientes porcentajes:

100% carga permanente (D) + 25% de la sobrecarga de techo (SC)
*Nota: Se incorpora el 25% de la sobrecarga de techo como un criterio conservador.

Las características del edificio y del terreno son las siguientes:
Zona Sísmica: 2

Tipo de Suelo: III
Clategoría Estructura: C2
Cmáx: 0.300

Cv: 0.200

Este documento es propiedad de Ingecosal, por lo que queda prohibida su utilización parcial o total con otro propósito que no sea
el estipulado en el contrato. 

**INGECOSAL - Gerencia de Proyectos** **1512-INM-001-CIV-MC-001- REV 0**

**5.4.** **Carga Equipos**

Los equipos soportados por la Losa 1, corresponden a un contenedor para la sala de
operaciones y un contenedor para la sala eléctrica, ambos de 6 Ton. El equipo soportado
por la Losa 2 corresponde a un contenedor con un generador en su interior de 6 Ton.

### 6. RESULTADO DEL ANÁLISIS

El diseño está de acuerdo a las normas y cumple con las limitaciones de diseño de
acuerdo a la normativa vigente.

**6.1.** **Verificación de Desplazamientos**

Losa 1:

El máximo punto de desplazamiento corresponde al nodo 1000 y es de 0.74 mm.

Figura 5. Desplazamientos máximos (mm).

Losa 2:

El máximo punto de desplazamiento corresponde al nodo 277 y es de 0.75 mm.

Este documento es propiedad de Ingecosal, por lo que queda prohibida su utilización parcial o total con otro propósito que no sea
el estipulado en el contrato. 

**INGECOSAL - Gerencia de Proyectos** **1512-INM-001-CIV-MC-001- REV 0**

Figura 6. Desplazamientos máximos (mm).

**6.2.** **Verificación de Refuerzos**

Losa 1:

El máximo momento obtenido (combinaciones LRFD para Hormigón) es de Mu=0.23
Tm para la combinación LRFD1, con el cual el diseño cumple para la verificación a
flexión y corte.

Este documento es propiedad de Ingecosal, por lo que queda prohibida su utilización parcial o total con otro propósito que no sea
el estipulado en el contrato. 

**INGECOSAL - Gerencia de Proyectos** **1512-INM-001-CIV-MC-001- REV 0**

Losa 2:

El máximo momento obtenido (combinaciones LRFD para Hormigón) es de Mu=0.24
Tm para la combinación LRFD1, con el cual el diseño cumple para la verificación a
flexión y corte.

**7.** **CONCLUSIONES**

Se ha realizado el análisis estructural de los elementos Losas descritos en esta Memoria

de Cálculo Estructural para su diseño. Considerando la normativa vigente a la fecha,
dichos elementos cumplen con los criterios de la normativa nacional vigente y los
criterios de diseño mencionados en el presente documento.

Este documento es propiedad de Ingecosal, por lo que queda prohibida su utilización parcial o total con otro propósito que no sea
el estipulado en el contrato. 