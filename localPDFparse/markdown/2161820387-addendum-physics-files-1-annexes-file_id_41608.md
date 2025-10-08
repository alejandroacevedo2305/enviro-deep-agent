---
title: User Manual
author: Huawei Technologies Co., Ltd.
date: D:20240204184953+08'00'
language: en
type: report
pages: 105
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - User Manual About This Document About This Document
  - User Manual Contents Contents
  - User Manual 1 Safety Information 1
  - Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 1
  - User Manual 2 Product Description 2
  - User Manual 3 Storage Requirements 3
  - User Manual 4 Installation 4 Installation
  - User Manual 5 Cable Connection 5 Cable Connection
  - User Manual 6 Checking Before Power-On 6
  - User Manual 7 Power-On and Commissioning 7
  ... y 10 secciones más
-->

**LUNA2000-200KTL-H1 Smart Power Control**

**System**

**User Manual**

**Issue** 08

**Date** 2024-01-23

**HUAWEI TECHNOLOGIES CO., LTD.**

**Copyright © Huawei Technologies Co., Ltd. 2024. All rights reserved.**

No part of this document may be reproduced or transmitted in any form or by any means without prior
written consent of Huawei Technologies Co., Ltd.

**Trademarks and Permissions**

and other Huawei trademarks are trademarks of Huawei Technologies Co., Ltd.
All other trademarks and trade names mentioned in this document are the property of their respective
holders.

**Notice**

The purchased products, services and features are stipulated by the contract made between Huawei and
the customer. All or part of the products, services and features described in this document may not be
within the purchase scope or the usage scope. Unless otherwise specified in the contract, all statements,
information, and recommendations in this document are provided "AS IS" without warranties, guarantees
or representations of any kind, either express or implied.

The information in this document is subject to change without notice. Every effort has been made in the
preparation of this document to ensure accuracy of the contents, but all statements, information, and
recommendations in this document do not constitute a warranty of any kind, express or implied.

**Huawei Technologies Co., Ltd.**

Address: Huawei Industrial Base

Bantian, Longgang
Shenzhen 518129

People's Republic of China

Website: [https://e.huawei.com](https://e.huawei.com)

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. i

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual About This Document About This Document

**Purpose**

This document describes the installation, electrical connections, commissioning,
maintenance, and troubleshooting of LUNA2000-200KTL-H1 Smart Power Control
System (also referred to as Smart PCS). Before installing and operating the Smart
PCS, ensure that you are familiar with the features, functions, and safety
precautions provided in this document.

**Intended Audience**

This document is intended for:

 - Installers

 - Users

**Symbol Conventions**

The symbols that may be found in this document are defined as follows:

|Symbol|Description|
|---|---|
||Indicates a hazard with a high level of risk which, if not avoided,<br>will result in death or serious injury.|
||Indicates a hazard with a medium level of risk which, if not<br>avoided, could result in death or serious injury.|
||Indicates a hazard with a low level of risk which, if not avoided,<br>could result in minor or moderate injury.|
||Indicates a potentially hazardous situation which, if not avoided,<br>could result in equipment damage, data loss, performance<br>deterioration, or unanticipated results.<br>**NOTICE** is used to address practices not related to personal injury.|
||Supplements the important information in the main text.<br>**NOTE** is used to address information not related to personal<br>injury, equipment damage, and environment deterioration.|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. ii

LUNA2000-200KTL-H1 Smart Power Control System
User Manual About This Document

**Change History**

Changes between document issues are cumulative. The latest document issue
contains all the changes made in earlier issues.

**Issue 08 (2024-01-23)**

Updated **1.3 Environment Requirements** .

Updated **2.1 Model** .

Updated **2.6 Label Description** .

Updated **3 Storage Requirements** .

Updated **4.2.1 Site Selection Requirements** .

Updated **5.8.1 Connecting FE Communications Cables** .

**Issue 07 (2023-10-16)**

Updated **5.8.1 Connecting FE Communications Cables** .

**Issue 06 (2023-09-30)**

Updated **2 Product Description** .

Updated **2.2 Networking Application** .

Updated **4.2.1 Site Selection Requirements** .

Updated **B Grid Codes** .

**Issue 05 (2023-07-30)**

Updated **2.2 Networking Application** .

Updated **5.2 Preparing Cables** .

Deleted the content related to CAN communication.

**Issue 04 (2023-06-30)**

Updated **2.2 Networking Application** .

Updated **4.5 Moving the Smart PCS** .

Updated **9 Technical Specifications** .

Adjusted the document structure.

**Issue 03 (2023-05-10)**

Updated **5.8.1 Connecting FE Communications Cables** .

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. iii

LUNA2000-200KTL-H1 Smart Power Control System
User Manual About This Document

**Issue 02 (2023-01-10)**

Updated **1 Safety Information** .

Updated **4.4 Pre-installation Check** .

Updated **5.1 Precautions** .

Updated **5.7 Connecting AC Power Cables** .

Updated **5.8.1 Connecting FE Communications Cables** .

Updated **7.1 Powering on the Smart PCS** .

Updated **8 Device Maintenance** .

Updated **8.5 Replacing the Smart PCS** .

Added **C Resetting Password** .

**Issue 01 (2022-08-31)**

This issue is used for first office application (FOA).

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. iv

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual Contents Contents

**About This Document................................................................................................................ ii**

**1 Safety Information.................................................................................................................. 1**

1.1 Personal Safety.........................................................................................................................................................................2

1.2 Electrical Safety........................................................................................................................................................................4

1.3 Environment Requirements................................................................................................................................................. 6

1.4 Mechanical Safety................................................................................................................................................................... 8

**2 Product Description.............................................................................................................. 13**

2.1 Model........................................................................................................................................................................................ 14

2.2 Networking Application .................................................................................................................................................... 15

2.3 Appearance............................................................................................................................................................................. 19

2.4 Circuit Diagram......................................................................................................................................................................22

2.5 Working Modes..................................................................................................................................................................... 22

2.6 Label Description.................................................................................................................................................................. 24

**3 Storage Requirements..........................................................................................................26**

**4 Installation..............................................................................................................................27**

4.1 Installation Modes................................................................................................................................................................ 27

4.2 Installation Requirements.................................................................................................................................................. 27

4.2.1 Site Selection Requirements.......................................................................................................................................... 27

4.2.2 Mounting Structure Requirements.............................................................................................................................. 29

4.2.3 Clearance Requirements................................................................................................................................................. 30

4.2.4 Angle Requirements......................................................................................................................................................... 32

4.3 Preparing Tools...................................................................................................................................................................... 32

4.4 Pre-installation Check......................................................................................................................................................... 34

4.5 Moving the Smart PCS........................................................................................................................................................ 35

4.6 Support Mounting................................................................................................................................................................ 37

4.7 Wall Mounting....................................................................................................................................................................... 40

4.8 DCBOX Mounting..................................................................................................................................................................42

**5 Cable Connection.................................................................................................................. 44**

5.1 Precautions..............................................................................................................................................................................44

5.2 Preparing Cables................................................................................................................................................................... 45

5.3 Connecting a PE Cable........................................................................................................................................................ 46

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. v

LUNA2000-200KTL-H1 Smart Power Control System
User Manual Contents

5.4 Opening the Maintenance Compartment Door.........................................................................................................47

5.4.1 Opening the DC Maintenance Compartment Door.............................................................................................. 47

5.4.2 Opening the AC Maintenance Compartment Door...............................................................................................48

5.5 (Optional) Replacing Crimping Modules......................................................................................................................49

5.6 Connecting DC Power Cables........................................................................................................................................... 50

5.7 Connecting AC Power Cables............................................................................................................................................53

5.8 Connecting Communications Cables..............................................................................................................................55

5.8.1 Connecting FE Communications Cables.................................................................................................................... 56

5.9 Closing the Maintenance Compartment Door........................................................................................................... 59

5.9.1 Closing the DC Maintenance Compartment Door.................................................................................................59

5.9.2 Closing the AC Maintenance Compartment Door................................................................................................. 60

**6 Checking Before Power-On................................................................................................. 61**

**7 Power-On and Commissioning...........................................................................................63**

7.1 Powering on the Smart PCS.............................................................................................................................................. 63

7.1.1 On-Grid Power-On............................................................................................................................................................ 64

7.1.2 Off-Grid Power-On............................................................................................................................................................64

7.1.3 Commissioning the Smart PCS Using the App........................................................................................................65

7.1.3.1 Downloading the App.................................................................................................................................................. 65

7.1.3.2 Logging In to the App.................................................................................................................................................. 66

**8 Device Maintenance............................................................................................................. 69**

8.1 Routine Maintenance.......................................................................................................................................................... 69

8.2 Powering Off the System................................................................................................................................................... 71

8.3 Alarm Reference.................................................................................................................................................................... 72

8.4 Replacing a Fan..................................................................................................................................................................... 73

8.5 Replacing the Smart PCS....................................................................................................................................................77

8.6 Disposing of the Smart PCS.............................................................................................................................................. 83

**9 Technical Specifications.......................................................................................................84**

**A Crimping an OT or DT Terminal........................................................................................ 87**

**B Grid Codes...............................................................................................................................90**

**C Resetting Password...............................................................................................................93**

**D Certificate Management and Maintenance................................................................... 94**

**E Contact Information............................................................................................................. 95**

**F Digital Power Customer Service........................................................................................ 97**

**G Acronyms and Abbreviations............................................................................................. 98**

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. vi

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual 1 Safety Information 1

**Safety Information**

**Statement**

**Before transporting, storing, installing, operating, using, and/or maintaining**
**the equipment, read this document, strictly follow the instructions provided**
**herein, and follow all the safety instructions on the equipment and in this**
**document.** In this document, "equipment" refers to the products, software,
components, spare parts, and/or services related to this document; "the Company"
refers to the manufacturer (producer), seller, and/or service provider of the
equipment; "you" refers to the entity that transports, stores, installs, operates,
uses, and/or maintains the equipment.

The **Danger**, **Warning**, **Caution**, and **Notice** statements described in this
document do not cover all the safety precautions. You also need to comply with
relevant international, national, or regional standards and industry practices. **The**
**Company shall not be liable for any consequences that may arise due to**
**violations of safety requirements or safety standards concerning the design,**
**production, and usage of the equipment.**

The equipment shall be used in an environment that meets the design
specifications. Otherwise, the equipment may be faulty, malfunctioning, or
damaged, which is not covered under the warranty. The Company shall not be
liable for any property loss, personal injury, or even death caused thereby.

Comply with applicable laws, regulations, standards, and specifications during
transportation, storage, installation, operation, use, and maintenance.

Do not perform reverse engineering, decompilation, disassembly, adaptation,
implantation, or other derivative operations on the equipment software. Do not
study the internal implementation logic of the equipment, obtain the source code
of the equipment software, violate intellectual property rights, or disclose any of
the performance test results of the equipment software.

**The Company shall not be liable for any of the following circumstances or**
**their consequences:**

 The equipment is damaged due to force majeure such as earthquakes, floods,
volcanic eruptions, debris flows, lightning strikes, fires, wars, armed conflicts,
typhoons, hurricanes, tornadoes, and other extreme weather conditions.

 The equipment is operated beyond the conditions specified in this document.

# Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 1

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 1 Safety Information

 - The equipment is installed or used in environments that do not comply with
international, national, or regional standards.

 The equipment is installed or used by unqualified personnel.

 - You fail to follow the operation instructions and safety precautions on the
product and in the document.

 - You remove or modify the product or modify the software code without
authorization.

 - You or a third party authorized by you cause the equipment damage during
transportation.

 - The equipment is damaged due to storage conditions that do not meet the
requirements specified in the product document.

 - You fail to prepare materials and tools that comply with local laws,
regulations, and related standards.

 - The equipment is damaged due to your or a third party's negligence,
intentional breach, gross negligence, or improper operations, or other reasons
not related to the Company.

## 1.1 Personal Safety

Ensure that power is off during installation. Do not install or remove a cable with
power on. Transient contact between the core of the cable and the conductor will
generate electric arcs or sparks, which may cause a fire or personal injury.

Non-standard and improper operations on the energized equipment may cause
fire, electric shocks, or explosion, resulting in property damage, personal injury, or
even death.

Before operations, remove conductive objects such as watches, bracelets, bangles,
rings, and necklaces to prevent electric shocks.

During operations, use dedicated insulated tools to prevent electric shocks or short
circuits. The dielectric withstanding voltage level must comply with local laws,
regulations, standards, and specifications.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 2

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 1 Safety Information

During operations, wear personal protective equipment such as protective
clothing, insulated shoes, goggles, safety helmets, and insulated gloves.

**Figure 1-1** Personal protective equipment

**General Requirements**

 - Do not stop protective devices. Pay attention to the warnings, cautions, and
related precautionary measures in this document and on the equipment.

 - If there is a likelihood of personal injury or equipment damage during
operations, immediately stop, report the case to the supervisor, and take
feasible protective measures.

 Do not power on the equipment before it is installed or confirmed by
professionals.

 - Do not touch the power supply equipment directly or with conductors such as
damp objects. Before touching any conductor surface or terminal, measure
the voltage at the contact point to ensure that there is no risk of electric
shock.

 - Do not touch operating equipment because the enclosure is hot.

 - Do not touch a running fan with your hands, components, screws, tools, or
boards. Otherwise, personal injury or equipment damage may occur.

 In the case of a fire, immediately leave the building or the equipment area
and activate the fire alarm or call emergency services. Do not enter the
affected building or equipment area under any circumstances.

**Personnel Requirements**

 - Only professionals and trained personnel are allowed to operate the
equipment.

-
Professionals: personnel who are familiar with the working principles and
structure of the equipment, trained or experienced in equipment
operations and are clear of the sources and degree of various potential
hazards in equipment installation, operation, maintenance

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 3

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 1 Safety InformationTrained personnel: personnel who are trained in technology and safety,
have required experience, are aware of possible hazards on themselves in
certain operations, and are able to take protective measures to minimize
the hazards on themselves and other people

 - Personnel who plan to install or maintain the equipment must receive
adequate training, be able to correctly perform all operations, and understand
all necessary safety precautions and local relevant standards.

 Only qualified professionals or trained personnel are allowed to install,
operate, and maintain the equipment.

 Only qualified professionals are allowed to remove safety facilities and inspect
the equipment.

 - Personnel who will perform special tasks such as electrical operations,
working at heights, and operations of special equipment must possess the
required local qualifications.

 - Only authorized professionals are allowed to replace the equipment or
components (including software).

 - Only personnel who need to work on the equipment are allowed to access
the equipment.

## 1.2 Electrical Safety

Before connecting cables, ensure that the equipment is intact. Otherwise, electric
shocks or fire may occur.

Non-standard and improper operations may result in fire or electric shocks.

Prevent foreign matter from entering the equipment during operations. Otherwise,
equipment damage, load power derating, power failure, or personal injury may

occur.

For the equipment that needs to be grounded, install the ground cable first when
installing the equipment and remove the ground cable last when removing the
equipment.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 4

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 1 Safety Information

Do not route cables near the air intake or exhaust vents of the equipment.

**General Requirements**

 - Follow the procedures described in the document for installation, operation,
and maintenance. Do not reconstruct or alter the equipment, add
components, or change the installation sequence without permission.

 - Obtain approval from the national or local electric utility company before
connecting the equipment to the grid.

 - Observe the power plant safety regulations, such as the operation and work
ticket mechanisms.

 - Install temporary fences or warning ropes and hang "No Entry" signs around
the operation area to keep unauthorized personnel away from the area.

 Before installing or removing power cables, turn off the switches of the
equipment and its upstream and downstream switches.

 - Before performing operations on the equipment, check that all tools meet the
requirements and record the tools. After the operations are complete, collect
all of the tools to prevent them from being left inside the equipment.

 - Before installing power cables, check that cable labels are correct and cable
terminals are insulated.

 - When installing the equipment, use a torque tool of a proper measurement
range to tighten the screws. When using a wrench to tighten the screws,
ensure that the wrench does not tilt and the torque error does not exceed
10% of the specified value.

 - Ensure that bolts are tightened with a torque tool and marked in red and blue
after double-check. Installation personnel mark tightened bolts in blue.
Quality inspection personnel confirm that the bolts are tightened and then
mark them in red. (The marks must cross the edges of the bolts.)

 - If the equipment has multiple inputs, disconnect all the inputs before
operating the equipment.

 - Before maintaining a downstream electrical or power distribution device, turn
off the output switch on the power supply equipment.

 - During equipment maintenance, attach "Do not switch on" labels near the
upstream and downstream switches or circuit breakers as well as warning
signs to prevent accidental connection. The equipment can be powered on
only after troubleshooting is complete.

 - Do not open equipment panels.

 - Check equipment connections periodically, ensuring that all screws are
securely tightened.

 Only qualified professionals can replace a damaged cable.

 - Do not scrawl, damage, or block any labels or nameplates on the equipment.
Promptly replace labels that have worn out.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 5

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 1 Safety Information

 - Do not use solvents such as water, alcohol, or oil to clean electrical
components inside or outside of the equipment.

**Grounding**

 - Ensure that the grounding impedance of the equipment complies with local
electrical standards.

 - Ensure that the equipment is connected permanently to the protective
ground. Before operating the equipment, check its electrical connection to
ensure that it is reliably grounded.

 - Do not work on the equipment in the absence of a properly installed ground
conductor.

 - Do not damage the ground conductor.

**Cabling Requirements**

 - When selecting, installing, and routing cables, follow local safety regulations
and rules.

 - When routing power cables, ensure that there is no coiling or twisting. Do not
join or weld power cables. If necessary, use a longer cable.

 - Ensure that all cables are properly connected and insulated, and meet
specifications.

 - Ensure that the slots and holes for routing cables are free from sharp edges,
and that the positions where cables are routed through pipes or cable holes
are equipped with cushion materials to prevent the cables from being
damaged by sharp edges or burrs.

 - Ensure that cables of the same type are bound together neatly and straight
and that the cable sheath is intact. When routing cables of different types,
ensure that they are away from each other without entanglement and
overlapping.

 - Secure buried cables using cable supports and cable clips. Ensure that the
cables in the backfill area are in close contact with the ground to prevent
cable deformation or damage during backfilling.

 - If the external conditions (such as the cable layout or ambient temperature)
change, verify the cable usage in accordance with the IEC-60364-5-52 or local
laws and regulations. For example, check that the current-carrying capacity
meets requirements.

 - When routing cables, reserve at least 30 mm clearance between the cables
and heat-generating components or areas. This prevents deterioration or
damage to the cable insulation layer.

## 1.3 Environment Requirements

Do not expose the equipment to flammable or explosive gas or smoke. Do not
perform any operation on the equipment in such environments.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 6

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 1 Safety Information

Do not store any flammable or explosive materials in the equipment area.

Do not place the equipment near heat sources or fire sources, such as smoke,
candles, heaters, or other heating devices. Overheat may damage the equipment
or cause a fire.

Install the equipment in an area far away from liquids. Do not install it under
areas prone to condensation, such as under water pipes and air exhaust vents, or
areas prone to water leakage, such as air conditioner vents, ventilation vents, or
feeder windows of the equipment room. Ensure that no liquid enters the
equipment to prevent faults or short circuits.

To prevent damage or fire due to high temperature, ensure that the ventilation
vents or heat dissipation systems are not obstructed or covered by other objects
while the equipment is running.

**General Requirements**

 - Store the equipment according to the storage requirements. Equipment
damage caused by unqualified storage conditions is not covered under the
warranty.

 - Keep the installation and operating environments of the equipment within the
allowed ranges. Otherwise, its performance and safety will be compromised.

 - The operating temperature range provided in the equipment's technical
specifications refers to the ambient temperatures in equipment's installation
environment.

 - Do not install, use, or operate outdoor equipment and cables (including but
not limited to moving equipment, operating equipment and cables, inserting
connectors to or removing connectors from signal ports connected to outdoor
facilities, working at heights, performing outdoor installation, and opening
doors) in harsh weather conditions such as lightning, rain, snow, and level 6
or stronger wind.

 - Do not install the equipment in an environment with dust, smoke, volatile or
corrosive gases, infrared and other radiations, organic solvents, or salty air.

 - Do not install the equipment in an environment with conductive metal or
magnetic dust.

 - Do not install the equipment in an area conducive to the growth of
microorganisms such as fungus or mildew.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 7

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 1 Safety Information

 - Do not install the equipment in an area with strong vibration, noise, or
electromagnetic interference. The equipment shall be installed in an
environment with a magnetic field strength less than 4 Gauss. If the magnetic
field strength is greater than or equal to 4 Gauss, the equipment may fail to
work properly. If the magnetic field strength is high, for example, in a
smeltery, you are advised to use a gauss meter to measure the magnetic field
strength of the equipment installation position when the smelting equipment
is running normally.

 - Ensure that the site complies with local laws, regulations, and related
standards.

 - Ensure that the ground in the installation environment is solid, free from
spongy or soft soil, and not prone to subsidence. The site must not be located
in a low-lying land prone to water or snow accumulation, and the horizontal
level of the site must be above the highest water level of that area in history.

 - Do not install the equipment in a position that may be submerged in water.

 Do not install the equipment outdoors in salt-affected areas because it may
be corroded. A salt-affected area refers to the region within 500 m of the
coast or prone to sea breeze. Regions prone to sea breeze vary with weather
conditions (such as typhoons and monsoons) or terrains (such as dams and
hills).

 - Before opening doors during the installation, operation, and maintenance of
the equipment, clean up any water, ice, snow, or other foreign objects on the
top of the equipment to prevent foreign objects from falling into the
equipment.

 - When installing the equipment, ensure that the installation surface is solid
enough to bear the weight of the equipment.

 - After installing the equipment, remove the packing materials such as cartons,
foam, plastics, and cable ties from the equipment area.

## 1.4 Mechanical Safety

Ensure that all necessary tools are ready and inspected by a professional
organization. Do not use tools that have signs of scratches or fail to pass the
inspection or whose inspection validity period has expired. Ensure that the tools
are secure and not overloaded.

Do not drill holes into the equipment. Doing so may affect the sealing
performance and electromagnetic containment of the equipment and damage
components or cables inside. Metal shavings from drilling may short-circuit boards
inside the equipment.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 8

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 1 Safety Information

**General Requirements**

 - Repaint any paint scratches caused during equipment transportation or
installation in a timely manner. Equipment with scratches must not be
exposed for an extended period of time.

 - Do not perform operations such as arc welding and cutting on the equipment
without evaluation by the Company.

 - Do not install other devices on the top of the equipment without evaluation
by the Company.

 - When performing operations over the top of the equipment, take measures to
protect the equipment against damage.

 - Use correct tools and operate them in the correct way.

**Moving Heavy Objects**

 - Be cautious to prevent injury when moving heavy objects.

 - If multiple persons need to move a heavy object together, determine the
manpower and work division with consideration of height and other
conditions to ensure that the weight is equally distributed.

 - If two persons or more move a heavy object together, ensure that the object
is lifted and landed simultaneously and moved at a uniform pace under the
supervision of one person.

 - Wear personal protective gears such as protective gloves and shoes when
manually moving the equipment.

 - To move an object by hand, approach to the object, squat down, and then lift
the object gently and stably by the force of the legs instead of your back. Do
not lift it suddenly or turn your body around.

 - Do not quickly lift a heavy object above your waist. Place the object on a
workbench that is half-waist high or any other appropriate place, adjust the
positions of your palms, and then lift it.

 - Move a heavy object stably with balanced force at an even and low speed. Put
down the object stably and slowly to prevent any collision or drop from
scratching the surface of the equipment or damaging the components and
cables.

 - When moving a heavy object, be aware of the workbench, slope, staircase,
and slippery places. When moving a heavy object through a door, ensure that
the door is wide enough to move the object and avoid bumping or injury.

 - When transferring a heavy object, move your feet instead of turning your
waist around. When lifting and transferring a heavy object, ensure that your
feet point to the target direction of movement.

 - When transporting the equipment using a pallet truck or forklift, ensure that
the tynes are properly positioned so that the equipment does not topple.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 9

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 1 Safety Information

Before moving the equipment, secure it to the pallet truck or forklift using
ropes. When moving the equipment, assign dedicated personnel to take care
of it.

 - Choose sea, roads in good conditions, or airplanes for transportation. Do not
transport the equipment by railway. Avoid tilt or jolt during transportation.

**Using Ladders**

 - Use wooden or insulated ladders when you need to perform live-line working
at heights.

 - Platform ladders with protective rails are preferred. Single ladders are not
recommended.

 Before using a ladder, check that it is intact and confirm its load bearing
capacity. Do not overload it.

 Ensure that the ladder is securely positioned and held firm.

 - When climbing up the ladder, keep your body stable and your center of
gravity between the side rails, and do not overreach to the sides.

 - When a step ladder is used, ensure that the pull ropes are secured.

 - If a single ladder is used, the recommended angle for the ladder against the
floor is 75 degrees, as shown in the following figure. A square can be used to
measure the angle.

 - If a single ladder is used, ensure that the wider end of the ladder is at the
bottom, and take protective measures to prevent the ladder from sliding.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 10

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 1 Safety Information

 - If a single ladder is used, do not climb higher than the fourth rung of the
ladder from the top.

 - If you use a single ladder to climb up to a platform, ensure that the ladder is
at least 1 m higher than the platform.

**Hoisting**

 Only trained and qualified personnel are allowed to perform hoisting
operations.

 - Install temporary warning signs or fences to isolate the hoisting area.

 - Ensure that the foundation where hoisting is performed on meets the loadbearing requirements.

 Before hoisting objects, ensure that hoisting tools are firmly secured onto a
fixed object or wall that meets the load-bearing requirements.

 - During hoisting, do not stand or walk under the crane or the hoisted objects.

 - Do not drag steel ropes and hoisting tools or bump the hoisted objects
against hard objects during hoisting.

 - Ensure that the angle between two hoisting ropes is no more than 90
degrees, as shown in the following figure.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 11

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 1 Safety Information

**Drilling Holes**

 - Obtain consent from the customer and contractor before drilling holes.

 - Wear protective equipment such as safety goggles and protective gloves when
drilling holes.

 - To avoid short circuits or other risks, do not drill holes into buried pipes or
cables.

 - When drilling holes, protect the equipment from shavings. After drilling, clean
up any shavings.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 12

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual 2 Product Description 2

**Product Description**

On-grid:

 The Smart PCS implements rectification and inversion through a three-phase
three-level converter.

 The rectified output is converted from three-phase AC power to DC power
and then stored in the energy storage system (ESS).

 The inverted output is filtered to three-phase AC power, which is then isolated
and boosted by a three-phase transformer and fed into the power grid.

Off-grid:

 When the Smart PCS is off-grid, it can also implement rectification and
inversion through a three-phase three-level converter.

 The rectified output is converted from three-phase AC power to DC power
and then stored in the ESS.

 - The inverted output is converted from DC power to three-phase AC power,
which is then isolated and converted by a transformer and supplied to loads.

For details about on-grid scenarios, see **[On-Grid Utility-Scale Energy Storage](https://support.huawei.com/enterprise/en/doc/EDOC1100321648/426cffd9)**
**[Solution Quick Guide](https://support.huawei.com/enterprise/en/doc/EDOC1100321648/426cffd9)** . For details about microgrid scenarios, see **[Medium-](https://support.huawei.com/enterprise/en/doc/EDOC1100263853/426cffd9)**
**[Voltage Microgrid Energy Storage Solution Quick Guide](https://support.huawei.com/enterprise/en/doc/EDOC1100263853/426cffd9)** .

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 13

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 2 Product Description

## 2.1 Model

**Model Description**

**Figure 2-1** Model

**Table 2-1** Model description

<!-- INICIO TABLA 2-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Model Description** **Figure 2-1** Model -->

**Tabla 2-1: ** Model description**

| No. | Meaning | Description |
| --- | --- | --- |
| 1 | Product family<br>identifer | LUNA2000: Smart PCS |
| 2 | Power level<br>identifer | 200K: The power level is 200 kW. |
| 3 | Topology<br>identifer | TL: transformerless |
| 4 | Product series<br>identifer | H1: product series with the 1500 V DC voltage |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Model Label Positions** You can obtain the device model from the model label on the outer packaging and the nameplate on the side of the enclosure. -->
<!-- FIN TABLA 2-1 -->


|No.|Meaning|Description|
|---|---|---|
|1|Product family<br>identifer|LUNA2000: Smart PCS|
|2|Power level<br>identifer|200K: The power level is 200 kW.|
|3|Topology<br>identifer|TL: transformerless|
|4|Product series<br>identifer|H1: product series with the 1500 V DC voltage|

**Model Label Positions**

You can obtain the device model from the model label on the outer packaging
and the nameplate on the side of the enclosure.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 14

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 2 Product Description

**Figure 2-2** Position of the model label on the outer packaging

(1) Position of the model label

**Figure 2-3** Position of the nameplate

(1) Position of the nameplate

## 2.2 Networking Application

The system consists of the ESS (including the Smart Rack Controller), Smart Power
Control System (PCS), Smart Transformer Station (STS), Distribution Transformer
(DTS), and other equipment.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 15

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 2 Product Description

**Figure 2-4** Networking application (on-grid scenario)

**Figure 2-5** Networking application (off-grid scenario)

NO TE

By default, the Smart PCS supports on-grid mode. If off-grid functions are required,
purchase the off-grid license and load the license by referring to **[License Management](https://support.huawei.com/enterprise/en/doc/EDOC1100108365/a276fcca/license-management)** in
the SmartLogger3000 User Manual. Otherwise, off-grid functions cannot be used.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 16

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 2 Product Description

|(A) PV array|(B) Inverter|(C) Combiner box|
|---|---|---|
|(D) Smart Array<br>Controller (SACU)|(E) STS|(F) Medium-voltage<br>power distribution<br>cabinet|
|(G) Critical load|(H) Common load|(I) Power grid|
|(J) ESS|(K) Smart PCS|(L) Diesel generator<br>system|
|(M) DTS|-|-|

NO TE

The grid forming function is supported only by the Smart PCS with the BOM code
01076613. For details about how to set grid forming parameters, see the following table.

|Parameter|Value (Grid Forming<br>Scenario)|Value (Non-Grid<br>Forming Scenario)|
|---|---|---|
|**Scenario** under**Arrays**<br>**Operation Scenario**|On-grid|On-grid|
|**Working mode** under<br>**Parameter Confguration**|VSG|PQ|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 17

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 2 Product Description

|Parameter|Value (Grid Forming<br>Scenario)|Value (Non-Grid<br>Forming Scenario)|
|---|---|---|
|**Microgrid compatibility**<br>under**Parameter**<br>**Confguration**|Disable|Disable|
|**Active Power Baseline (kW)**<br>under**Parameter**<br>**Confguration**|83.33|200|
|**Apparent Power Baseline**<br>**(kVA)** under**Parameter**<br>**Confguration**|83.33|200|
|**Maximum Overload Active**<br>**Power (kW)** under<br>**Parameter Confguration**|105|240|
|**Maximum Overload**<br>**Apparent Power (kVA)** under<br>**Parameter Confguration**|250|240|
|Grid Code|Set this parameter based on the grid code of<br>the country or region where the devices are<br>used.|Set this parameter based on the grid code of<br>the country or region where the devices are<br>used.|

**Earthing System**

The Smart PCS supports the IT earthing system.

**Figure 2-6** Earthing system

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 18

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 2 Product Description

## 2.3 Appearance

**Appearance and Ports**

**Figure 2-7** Appearance and ports

(1) AC maintenance
compartment

(2) Communications
cable hole (FE)

(4) Protective cover (5) DC maintenance
compartment

(7) External fan tray (8) Security Torx
wrench [[1]]

(10) Communications cable
hole (COM)

(11) AC power cable
holes

(3) Panel

(6) LED indicators

(9) Protective earthing
point

(12) Ventilation valve

(13) USB port (USB) (14) DC power cable
holes

Note [1]: The security Torx wrench is delivered with the device and is tied to the
bracket on the top of the device. Remove the security Torx wrench from the
bracket and keep it safe.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 19

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 2 Product Description

**Dimensions**

**Figure 2-8** Dimensions

**Indicator Description**

You can check the operating status of the Smart PCS by observing the LED
indicators on the panel.

**Figure 2-9** LED indicators

**Table 2-2** LED indicator description

<!-- INICIO TABLA 2-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- You can check the operating status of the Smart PCS by observing the LED indicators on the panel. **Figure 2-9** LED indicators -->

**Tabla 2-2: ** LED indicator description**

| No. | Category | Status (Blinking Fast: On<br>for 0.2s and Off for 0.2s;<br>Blinking Slowly: On for 1s<br>and Off for 1s) | Meaning |
| --- | --- | --- | --- |
| 1 | DC indication | Steady green | The DC side is properly connected, and<br>the auxiliary power supply inside the<br>device is working. |

<!-- Estadísticas: 1 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 20 LUNA2000-200KTL-H1 Smart Power Control System User Manual 2 Product Description -->
<!-- FIN TABLA 2-2 -->


|No.|Category|Status (Blinking Fast: On<br>for 0.2s and Off for 0.2s;<br>Blinking Slowly: On for 1s<br>and Off for 1s)|Meaning|
|---|---|---|---|
|1|DC indication|Steady green|The DC side is properly connected, and<br>the auxiliary power supply inside the<br>device is working.|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 20

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 2 Product Description

|No.|Category|Status (Blinking Fast: On<br>for 0.2s and Of f for 0.2s;<br>Blinking Slowly: On for 1s<br>and Off for 1s)|Meaning|
|---|---|---|---|
|||Blinking green slowly|The device is in standby or cable<br>connection detection state.|
|||Blinking red fast|An environmental fault occurred on the<br>DC side.|
|||Of|The DC side is not properly connected,<br>or the auxiliary power supply inside the<br>device is not working.|
|2|Running<br>indication|Steady green|The device is operating in grid-tied<br>mode.|
|2|Running<br>indication|Steady yellow|The device is operating in of-grid mode.|
|2|Running<br>indication|Blinking green slowly|The system environment is normal but<br>the device is not in the working state.|
|2|Running<br>indication|Blinking red fast|An environmental fault occurred on the<br>AC side.|
|2|Running<br>indication|Of|The AC side is not connected to the<br>power grid.|
|3|Communication<br>indication|Blinking green fast|The device receives data through<br>northbound FE communication.|
|3|Communication<br>indication|Of|The device has not received data<br>through northbound FE communication<br>in at least 10s.|
|4|Fault/<br>Maintenance<br>indication|Steady red|A major alarm was generated on the<br>device.|
|4|Fault/<br>Maintenance<br>indication|Blinking red fast|A minor alarm was generated on the<br>device.|
|4|Fault/<br>Maintenance<br>indication|Blinking red slowly|A warning was generated on the device.|
|4|Fault/<br>Maintenance<br>indication|Blinking green slowly|The device is under local maintenance<br>or shut down after receiving a<br>command.|
|4|Fault/<br>Maintenance<br>indication|Of|There is no alarm, and no local<br>maintenance operations are performed.|

 - If the Smart PCS is installed on the DC LV Panel (or the installation height is
about 2.4 m), you are advised to use the SmartLogger or app to check the
device running status. The optimal viewing range of the Smart PCS indicators
is 3 m to 5 m, and the viewing angle is less than or equal to 15°.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 21

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 2 Product Description

**Figure 2-10** Optimal viewing range of indicators

NO TE

 - If the DC indicator and running indicator do not blink red fast and the fault/
maintenance indicator is steady red, replace parts or the entire device.

 - Local maintenance refers to the operation that requires inserting a WLAN module into
the USB port of the device, for example, connecting to the SUN2000 app through the
WLAN module.

 - If alarms are generated during the local maintenance, the fault/maintenance indicator
shows the local maintenance state first. After the WLAN module is removed, the
indicator shows the alarm state.

## 2.4 Circuit Diagram

**Figure 2-11** Circuit diagram

## 2.5 Working Modes

The Smart PCS has three working modes: standby, operating, and shutdown.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 22

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 2 Product Description

**Figure 2-12** Working modes

**Table 2-3** Working mode description

<!-- INICIO TABLA 2-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- LUNA2000-200KTL-H1 Smart Power Control System User Manual 2 Product Description **Figure 2-12** Working modes -->

**Tabla 2-3: ** Working mode description**

| Working<br>Mode | Description |
| --- | --- |
| Standby | The Smart PCS enters standby mode when the external<br>environment does not meet the operating requirements. In standby<br>mode:<br>●The Smart PCS continuously detects its operation status. Once<br>the operation conditions are met, the Smart PCS enters<br>operating mode.<br>●If the Smart PCS detects a shutdown command or a fault after<br>startup, it enters shutdown mode. |
| Operating | In operating mode:<br>●The Smart PCS controls charge and discharge based on system<br>commands.<br>●The Smart PCS enters shutdown mode after detecting a fault or<br>receiving a shutdown command. |
| Shutdown | ●In standby or operating mode, if the Smart PCS detects a<br>shutdown command or a fault, it enters shutdown mode.<br>●In shutdown mode, the Smart PCS enters standby mode when a<br>startup command is received and faults are rectifed, the DC<br>power is insufcient, or the DC external switch is turned of. |

<!-- Estadísticas: 3 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 23 LUNA2000-200KTL-H1 Smart Power Control System User Manual 2 Product Description -->
<!-- FIN TABLA 2-3 -->


|Working<br>Mode|Description|
|---|---|
|Standby|The Smart PCS enters standby mode when the external<br>environment does not meet the operating requirements. In standby<br>mode:<br>●The Smart PCS continuously detects its operation status. Once<br>the operation conditions are met, the Smart PCS enters<br>operating mode.<br>●If the Smart PCS detects a shutdown command or a fault after<br>startup, it enters shutdown mode.|
|Operating|In operating mode:<br>●The Smart PCS controls charge and discharge based on system<br>commands.<br>●The Smart PCS enters shutdown mode after detecting a fault or<br>receiving a shutdown command.|
|Shutdown|●In standby or operating mode, if the Smart PCS detects a<br>shutdown command or a fault, it enters shutdown mode.<br>●In shutdown mode, the Smart PCS enters standby mode when a<br>startup command is received and faults are rectifed, the DC<br>power is insufcient, or the DC external switch is turned of.|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 23

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 2 Product Description

## 2.6 Label Description

**Table 2-4** Enclosure labels

<!-- INICIO TABLA 2-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- LUNA2000-200KTL-H1 Smart Power Control System User Manual 2 Product Description ## 2.6 Label Description -->

**Tabla 2-4: ** Enclosure labels**

| Symbol | Name | Meaning |
| --- | --- | --- |
|  | Operation warning | Potential hazards exist after the<br>device is powered on. Take<br>protective measures when working<br>on the device. |
|  | High temperature hazard | Do not touch the device, as the<br>enclosure is hot when the device is<br>running. |
|  | Electric shock hazard | Hazardous voltage exists after the<br>device is powered on. Take<br>protective measures during<br>operation and maintenance (O&M). |
|  | Delayed discharge | ●High voltage may occur after the<br>device is powered on. Only<br>qualifed and trained electrical<br>technicians are allowed to install<br>and operate the device.<br>●Residual voltage exists after the<br>device is powered of. It takes 15<br>minutes for the device to<br>discharge to the safe voltage. |
|  | Refer to documentation | Reminds operators to refer to the<br>documentation provided with the<br>device. Losses caused by operations<br>that do not comply with the<br>requirements of site selection,<br>storage, or mounting specifed in the<br>user manual are not covered under<br>the warranty. |
|  | Protective earthing | Indicates the position for connecting<br>the protective earthing (PE) cable. |
|  | Equipotential bonding | Indicates the position for<br>equipotential bonding. |
|  | Fan operation warning | Do not touch the fan when the<br>device is running to prevent<br>mechanical injury. |

<!-- Estadísticas: 8 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 24 LUNA2000-200KTL-H1 Smart Power Control System User Manual 2 Product Description -->
<!-- FIN TABLA 2-4 -->


|Symbol|Name|Meaning|
|---|---|---|
||Operation warning|Potential hazards exist after the<br>device is powered on. Take<br>protective measures when working<br>on the device.|
||High temperature hazard|Do not touch the device, as the<br>enclosure is hot when the device is<br>running.|
||Electric shock hazard|Hazardous voltage exists after the<br>device is powered on. Take<br>protective measures during<br>operation and maintenance (O&M).|
||Delayed discharge|●High voltage may occur after the<br>device is powered on. Only<br>qualifed and trained electrical<br>technicians are allowed to install<br>and operate the device.<br>●Residual voltage exists after the<br>device is powered of. It takes 15<br>minutes for the device to<br>discharge to the safe voltage.|
||Refer to documentation|Reminds operators to refer to the<br>documentation provided with the<br>device. Losses caused by operations<br>that do not comply with the<br>requirements of site selection,<br>storage, or mounting specifed in the<br>user manual are not covered under<br>the warranty.|
||Protective earthing|Indicates the position for connecting<br>the protective earthing (PE) cable.|
||Equipotential bonding|Indicates the position for<br>equipotential bonding.|
||Fan operation warning|Do not touch the fan when the<br>device is running to prevent<br>mechanical injury.|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 24

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 2 Product Description

|Symbol|Name|Meaning|
|---|---|---|
||Fan replacement warning|Before replacing the fan, disconnect<br>its power connector.|
||Weight|The device needs to be carried by<br>four persons or using a forklift.|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 25

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual 3 Storage Requirements 3

**Storage Requirements**

NO TICE

 - Store Smart PCSs according to the storage requirements. Device damage
caused by unqualified storage conditions is not covered under the warranty.

 - Do not store Smart PCSs without outer packaging.

 - Do not tilt a packing case or place it upside down.

If Smart PCSs will not be put into use immediately, store them according to the
requirements specified in this section. Device damage caused by unqualified
storage conditions is not covered under the warranty. Store Smart PCSs with outer
packaging in a ventilated, dry, and clean indoor environment. In addition, ensure
that the following requirements are met:

 - If Smart PCSs are unpacked but will not be used immediately, put them back
to the original packaging with the desiccant, and seal with tape.

 - When temporarily storing Smart PCSs outdoors, do not stack them on a
pallet. Take rainproof measures such as using tarpaulins to protect Smart
PCSs from rain and water.

 - Smart PCSs must be stored in a clean and dry environment with appropriate
temperature and humidity. The air must not contain corrosive or flammable
gases. Maintain a storage temperature between -40°C to +70°C, and humidity
between 5%-95% RH.

 - A maximum of four Smart PCSs can be stacked. To avoid personal injury or
device damage, exercise caution when stacking Smart PCSs to prevent them
from falling over.

 - Do not remove the outer packaging. Check the packaging regularly
(recommended: once every three months). Replace any packaging that is
damaged during storage.

 - Do not store Smart PCSs for more than two years. If Smart PCSs have been
stored for two years or longer, they must be checked and tested by
professionals before being put into use.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 26

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual 4 Installation 4 Installation

## 4.1 Installation Modes

The Smart PCS can be installed on a support, wall, or DC LV Panel (also referred
to as DCBOX).

**Table 4-1** Installation modes

<!-- INICIO TABLA 4-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- ## 4.1 Installation Modes The Smart PCS can be installed on a support, wall, or DC LV Panel (also referred to as DCBOX). -->

**Tabla 4-1: ** Installation modes**

| Installation<br>Mode | Screw Specifications | Description |
| --- | --- | --- |
| Wall<br>mounting | M12x60 stainless steel expansion bolt | Prepared by the<br>customer |
| Support<br>mounting | M12 bolt assembly | Prepared by the<br>customer |
| DCBOX<br>mounting | - | Purchased from<br>the Company |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- ## 4.2 Installation Requirements ### 4.2.1 Site Selection Requirements -->
<!-- FIN TABLA 4-1 -->


|Installation<br>Mode|Screw Specifications|Description|
|---|---|---|
|Wall<br>mounting|M12x60 stainless steel expansion bolt|Prepared by the<br>customer|
|Support<br>mounting|M12 bolt assembly|Prepared by the<br>customer|
|DCBOX<br>mounting|-|Purchased from<br>the Company|

## 4.2 Installation Requirements

### 4.2.1 Site Selection Requirements

 - Do not install the Smart PCS in working or living areas to avoid personal
injury or property loss caused by accidental contact by non-professionals or
other reasons during device operation.

 - Do not install the Smart PCS in noise-sensitive areas (such as residential
areas, office areas, and schools) to avoid complaints. If the preceding areas
are unavoidable, the distance between the installation position and noisesensitive areas must be greater than or equal to 40 m.

 - If the equipment is installed in a place with abundant vegetation, in addition
to routine weeding, harden the ground underneath the equipment using
cement or gravel (the area shall be greater than or equal to 3 m x 2.5 m).

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 27

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

 - If the Smart PCS is installed in public places (such as parking lots, stations,
and factories) other than working and living areas, install a protective net
outside the device and set up a safety warning sign to isolate the device. This
is to avoid personal injury or property loss caused by accidental contact by
non-professionals or other reasons during device operation.

 Do not install the Smart PCS in areas containing flammable materials (such
as sulfur, phosphorus, liquefied petroleum gas, marsh gas, flour, and cotton)
to avoid personal injury or property loss caused by fire or other reasons.

 - Do not install the Smart PCS in areas containing explosives (such as blasting
agents, display shells, fireworks, and firecrackers) to avoid personal injury or
property loss caused by explosion or other reasons.

 - Do not install the Smart PCS in areas with corrosive substances (such as
sulfuric acid, hydrochloric acid, nitric acid, hydrogen sulfide, and chlorine) to
avoid Smart PCS failure caused by corrosion, which is not covered under the
warranty.

 The mounting structure for the Smart PCS must be fireproof. Do not install
the Smart PCS on flammable building materials to avoid personal injury or
property loss caused by fire or other reasons.

 - The anti-corrosion level of the Smart PCS is C5 Medium. Therefore, the site
must be a class C or better environment but not a class D or E environment.

 - Do not install the Smart PCS in an easily accessible place, because the voltage
is high and its enclosure and heat sink are hot during device operation. This is
to avoid personal injury or property loss caused by accidental contact by nonprofessionals or other reasons during device operation.

 - The Smart PCS shall be installed in a well-ventilated environment to ensure
good heat dissipation. The Smart PCS provides self-protection in hightemperature environments. If the Smart PCS is installed in a poorly ventilated
environment, the power of the Smart PCS may decrease as the ambient
temperature increases.

 - Do not install the equipment in an area with strong vibration, noise, or
electromagnetic interference. The equipment shall be installed in an
environment with a magnetic field strength less than 4 Gauss. If the magnetic
field strength is greater than or equal to 4 Gauss, the equipment may fail to
work properly. If the magnetic field strength is high, for example, in a
smeltery, you are advised to use a gauss meter to measure the magnetic field
strength of the equipment installation position when the smelting equipment
is running normally.

 - If the Smart PCS is installed in an enclosed environment, a heat dissipation
device or ventilation device shall be installed. The indoor ambient
temperature must not be higher than the outdoor ambient temperature. The
Smart PCS provides self-protection in high-temperature environments. The
power of the Smart PCS may decrease as the ambient temperature increases.

 In off-grid scenarios, install the Smart PCS in a place with a sunshade or
install an awning for the Smart PCS in case of high temperature or direct
sunlight.

 - The Smart PCS shall be installed in a sheltered place to avoid exposure to
direct sunlight or adverse weather conditions (such as snow, rain, and
lightning). The Smart PCS provides self-protection in high-temperature
environments. If the Smart PCS is installed in a place subject to direct

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 28

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

sunlight, the power of the Smart PCS may decrease as the ambient
temperature increases.

 - If the Smart PCS has not been running for six months or longer after being
mounted, it may fail and must be checked and tested by professionals before
being put into operation.

 - Ensure that the installation surface is solid enough to bear the weight of the
Smart PCS (for details, see **Figure 4-1** ) to avoid personal injury or property
loss caused by the collapse of the mounting structure or other reasons.

 - Take waterproof and insulation measures for unused DC power cables to
avoid personal injury or property loss caused by accidental contact with high
voltage or other reasons.

 - AC and DC power cables must be vertically routed into combiner boxes and
wiring terminals to avoid damage caused by horizontal stress on the
terminals, which is not covered under the warranty.

 The Smart PCS will be corroded in salt-affected areas. Before installing the
Smart PCS outdoors in salt-affected areas, consult the Company. A saltaffected area refers to a region within 500 m of the coast or prone to sea
breeze. Regions prone to sea breeze vary with weather conditions (such as
typhoons and monsoons) or terrains (such as dams and hills).

NO TE

 - Class C environment: Outdoor areas more than 500 m away from the sea. If a site
is near a pollution source, it is 1500-3000 m away from heavy pollution sources,
such as smelteries, coal mines, and thermal power plants; 1000-2000 m away from
medium pollution sources such as chemical factories, rubber plants, and
electroplating factories; or 500-1000 m away from light pollution sources, such as
packing houses, tanneries, boiler rooms, slaughterhouses, landfill sites, and sewage
treatment plants.

 - Class D environment: Sea environments or outdoor areas within 500 m away from
the sea. If a site is near a pollution source, it is within 1500 m away from heavy
pollution sources such as smelteries, coal mines, and thermal power plants; within
1000 m away from medium pollution sources such as chemical factories, rubber
plants, and electroplating factories; or within 500 m away from light pollution
sources such as packing houses, tanneries, boiler rooms, slaughterhouses, landfill
sites, and sewage treatment plants.

 - Class E environment: Special environments, such as underground or underwater
environments.

### 4.2.2 Mounting Structure Requirements

 The structure where the device is installed must be fireproof.

 Do not install the device on flammable building materials.

 - The device is heavy. Ensure that the installation surface is solid enough to
bear the weight of the device.

 - In residential areas, do not install the device on gypsum boards or walls made
of similar materials with weak sound insulation performance to avoid
disturbing residents.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 29

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

**Figure 4-1** Mounting structure

### 4.2.3 Clearance Requirements

Reserve sufficient clearance around the Smart PCS for installation and heat
dissipation.

**Figure 4-2** Installation clearance (support-mounting and wall-mounting
scenarios)

NO TE

For ease of installation, cable connection, and maintenance, reserve 600-730 mm clearance
underneath. For further questions regarding the clearance, consult local technical support
engineers.

When installing multiple devices, install them in horizontal mode if sufficient
space is available and install them in triangle mode if no sufficient space is
available. Stacked installation is not recommended.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 30

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

**Figure 4-3** Horizontal installation (recommended)

**Figure 4-4** Triangle installation mode (recommended)

**Figure 4-5** Stacked installation mode (not recommended)

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 31

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

### 4.2.4 Angle Requirements

**Figure 4-6** Installation angle

## 4.3 Preparing Tools

Before installation, the following tools need to be prepared.

**Installation Tools**

Hammer drill Drill bit (Ф14 mm
and Ф16 mm)

Insulated torque
socket wrench
(including an
extension bar ≥ 50
mm)

Phillips insulated
torque screwdriver

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 32

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

|Wire stripper|Rubber mallet|Utility knife|Diagonal pliers|
|---|---|---|---|
|Cable cutter|RJ45 crimping tool|Vacuum cleaner|Hydraulic pliers|
|Marker|Steel measuring<br>tape|Level|Cable tie|
|Heat shrink tubing|Heat gun|Ladder|Digital multimeter<br>DC voltage<br>measurement<br>range ≥ 1500 V DC<br>AC voltage<br>measurement<br>range ≥ 800 V AC|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 33

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 InstallationCrane

Hoisting capability
≥ 3 t; working
radius ≥ 2 m

Lifting sling

Length ≥ 1.8 m

**Personal Protective Equipment (PPE)**

|Insulated gloves|Goggles|Dust mask|Insulated shoes|
|---|---|---|---|
|Refective vest|Safety helmet|Protective gloves|-|

## 4.4 Pre-installation Check

**Checking Outer Packaging**

NO TICE

 - After placing the equipment in the installation position, unpack it with care to
prevent scratches. Keep the equipment stable during unpacking.

Before unpacking the device, check the outer packaging for damage, such as holes
and cracks, and check the device model. If any damage is found or the device
model is not what you requested, do not unpack the product and contact your
vendor as soon as possible.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 34

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

NO TE

You are advised to remove the outer packaging within 24 hours before installing the device.

**Unpacking the Device**

**Step 1** Use diagonal pliers to cut the packaging tape, and use a utility knife to slice the
tape along the gap on the packing case. Slice the tape with caution to avoid
scratching the device inside.

**Step 2** Open the packing case and check the deliverables.

**----End**

**Checking Deliverables**

After unpacking the device, check that the deliverables are intact and complete
according to the packing list, and check that the device is free from any obvious
damage. If any item is missing or damaged, contact your vendor.

NO TE

For details about the quantity of deliverables, see the packing list in the packing case.

## 4.5 Moving the Smart PCS

**Precautions**

Ensure that the lifting handles are installed to the correct screw holes. Do not
install them to the mounting bracket screw holes on the top. Incorrect installation
may cause device damage or personal injury.

NO TICE

 - Four persons or appropriate transportation tools are required to move the
device.

 - Place a foam pad or cardboard under the device to protect its enclosure from
damage.

 - Use lifting handles to facilitate installation, which are optional and delivered
separately. Ensure that the lifting handles are securely installed. After the
installation is complete, remove the lifting handles and keep them properly.

 - Secure the lifting handles (with the steel washers of the lifting handles closely
fitted to the device).

 - If the stud of a lifting handle is bent, replace the lifting handle in time.

 - Slowly and steadily hoist, land, and move the Smart PCS to avoid bumping and
damaging the device enclosure.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 35

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

**Method**

If the installation position is high and a crane is required, run a sling (strong
enough to bear the weight of the Smart PCS) through the two lifting eyes to hoist
the Smart PCS.

**Table 4-2** Method description

<!-- INICIO TABLA 4-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- If the installation position is high and a crane is required, run a sling (strong enough to bear the weight of the Smart PCS) through the two lifting eyes to hoist the Smart PCS. -->

**Tabla 4-2: ** Method description**

| Method | Tool | Description |
| --- | --- | --- |
| Manual<br>handling | Lifting handles | Prepared by the<br>customer |
| Hoisting | Crane sling[1] | Prepared by the<br>customer |
| Note [1]: The hoisting capability of the crane shall be greater than or equal to 3<br>t, the working radius shall be greater than or equal to 2 m, and the length of<br>the lifting sling shall be greater than or equal to 1.8 m. To prevent damage to<br>the device surfaces, you are advised not to use metal slings such as steel wire<br>ropes. | Note [1]: The hoisting capability of the crane shall be greater than or equal to 3<br>t, the working radius shall be greater than or equal to 2 m, and the length of<br>the lifting sling shall be greater than or equal to 1.8 m. To prevent damage to<br>the device surfaces, you are advised not to use metal slings such as steel wire<br>ropes. | Note [1]: The hoisting capability of the crane shall be greater than or equal to 3<br>t, the working radius shall be greater than or equal to 2 m, and the length of<br>the lifting sling shall be greater than or equal to 1.8 m. To prevent damage to<br>the device surfaces, you are advised not to use metal slings such as steel wire<br>ropes. |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Hole Description** (1) Lifting handle screw hole (2) Mounting bracket screw holes -->
<!-- FIN TABLA 4-2 -->


|Method|Tool|Description|
|---|---|---|
|Manual<br>handling|Lifting handles|Prepared by the<br>customer|
|Hoisting|Crane sling[1]|Prepared by the<br>customer|
|Note [1]: The hoisting capability of the crane shall be greater than or equal to 3<br>t, the working radius shall be greater than or equal to 2 m, and the length of<br>the lifting sling shall be greater than or equal to 1.8 m. To prevent damage to<br>the device surfaces, you are advised not to use metal slings such as steel wire<br>ropes.|Note [1]: The hoisting capability of the crane shall be greater than or equal to 3<br>t, the working radius shall be greater than or equal to 2 m, and the length of<br>the lifting sling shall be greater than or equal to 1.8 m. To prevent damage to<br>the device surfaces, you are advised not to use metal slings such as steel wire<br>ropes.|Note [1]: The hoisting capability of the crane shall be greater than or equal to 3<br>t, the working radius shall be greater than or equal to 2 m, and the length of<br>the lifting sling shall be greater than or equal to 1.8 m. To prevent damage to<br>the device surfaces, you are advised not to use metal slings such as steel wire<br>ropes.|

**Hole Description**

(1) Lifting handle screw hole (2) Mounting bracket screw holes

**Procedure**

**Step 1** Take the device out of the packing case and move it to the specified position.

**Figure 4-7** Using the lifting handles

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 36

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

**Figure 4-8** Manual handling

**Figure 4-9** Hoisting

**----End**

## 4.6 Support Mounting

**Mounting Bracket Dimensions**

Purchase the mounting bracket separately from the Company.

The mounting bracket of the Smart PCS has four groups of tapped holes, each
group containing four tapped holes. Mark any hole in each group based on site
requirements and mark four holes in total. The two round holes are
recommended.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 37

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

**Figure 4-10** Hole dimensions

**Procedure**

**Step 1** Install the mounting bracket.

**Figure 4-11** Installing the mounting bracket

NO TE

If the bolt length does not meet the installation requirements, prepare M12 bolts and use
them together with the delivered M12 nuts.

**Step 2** Install the mounting ears.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 38

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

**Figure 4-12** Installing the mounting ears

**Step 3** Install the device on the mounting bracket.

**Step 4** Tighten the two screws at the bottom of the device.

**Figure 4-13** Installing the Smart PCS

NO TE

After the Smart PCS is secured, you need to configure a DC power distribution cabinet by
yourself. For details about the specifications, contact local technical support engineers.

**----End**

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 39

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

## 4.7 Wall Mounting

**Precautions**

Avoid drilling holes into the water pipes and power cables buried in the wall.

NO TICE

 - To prevent dust inhalation or contact with eyes, wear safety goggles and a dust
mask when drilling holes.

 - Use a vacuum cleaner to clean up dust in and around the holes, and measure
the spacing. If the holes are inaccurately positioned, drill the holes again.

 - Level the top of the expansion sleeve with the concrete wall after removing the
bolt, spring washer, and flat washer. Otherwise, the mounting bracket will not
be securely installed on the concrete wall.

**Mounting Bracket Dimensions**

Purchase the mounting bracket separately from the Company. The M12x60
stainless expansion bolts need to be purchased separately.

The mounting bracket of the Smart PCS has four groups of tapped holes, each
group containing four tapped holes. Mark any hole in each group based on site
requirements and mark four holes in total. The two round holes are
recommended.

**Figure 4-14** Hole dimensions

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 40

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

**Procedure**

**Step 1** Install the mounting bracket.

**Figure 4-15** Installing the mounting bracket

**Step 2** Install the mounting ears.

**Figure 4-16** Installing the mounting ears

**Step 3** Install the device on the mounting bracket.

**Step 4** Tighten the two screws at the bottom of the device.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 41

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

**Figure 4-17** Installing the Smart PCS

NO TE

After the Smart PCS is secured, you need to configure a DC power distribution cabinet by
yourself. For details about the specifications, contact local technical support engineers.

**----End**

## 4.8 DCBOX Mounting

**Installation Description**

 - The DCBOX-9/5-H0 is purchased from the Company.

 - For details about the installation procedure, see the **[DCBOX DC LV Panel](https://support.huawei.com/enterprise/en/doc/EDOC1100212120)**
**[User Manual](https://support.huawei.com/enterprise/en/doc/EDOC1100212120)** .

NO TE

 A maximum of five Smart PCSs can be installed on the top of the DCBOX. If less
than five Smart PCSs will be installed, install them from left to right. Otherwise,
the Smart PCS fasteners cannot be used.

 - The installation method of all Smart PCSs is the same. Install the Smart PCS
according to the direction shown in the figure. This section uses one Smart PCS as
an example.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 42

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 4 Installation

**Installation Diagram**

**Figure 4-18** Installation diagram

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 43

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual 5 Cable Connection 5 Cable Connection

## 5.1 Precautions

- Before connecting cables, ensure that the external switches on the AC and DC
sides of the Smart PCS are off to disconnect all external connections of the
Smart PCS. Otherwise, the high voltage of the device may cause electric shocks.

- The site must be equipped with qualified fire fighting facilities, such as fire sand
and carbon dioxide fire extinguishers.

- Wear personal protective equipment and use dedicated insulated tools to avoid
electric shocks or short circuits.

- Device damage caused by incorrect cable connections is not covered by the
product warranty.

- Only professional electrical technicians are allowed to perform electrical
connection operations.

- Connect cables according to the wiring labels inside the device.

- Operation personnel must wear PPE when connecting cables.

- Before connecting cables to ports, leave enough slack to reduce the tension on
the cables and prevent poor cable connections.

 - Stay away from the equipment when preparing cables to prevent cable scraps
from entering the equipment. Cable scraps may cause sparks and result in
personal injury and equipment damage.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 44

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

NO TE

The cable colors shown in the electrical connection diagrams provided in this section are for
reference only. Select cables in accordance with local cable specifications (green-and-yellow
cables are only used for protective earthing). The factors that affect cable selection include
the rated current, cable type, routing mode, ambient temperature, and maximum expected
line loss.

## 5.2 Preparing Cables

**Table 5-1** Cable description (S indicates the conductor cross-sectional area of the AC cable, and S p

<!-- INICIO TABLA 5-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- the rated current, cable type, routing mode, ambient temperature, and maximum expected line loss. ## 5.2 Preparing Cables -->

**Tabla 5-1: ** Cable description (S indicates the conductor cross-sectional area of the AC cable, and S p**

| Cable | Type | Conductor Cross-<br>Sectional Area | Outer<br>Diameter | Source |
| --- | --- | --- | --- | --- |
| DC power<br>cable<br>(multi-<br>core) | Two-core outdoor cable and<br>M12 OT/DT terminal | 70-185 mm2 | 30-60 mm | Prepared<br>by the<br>customer<br>(In the<br>DCBOX<br>scenario,<br>the DC<br>cables are<br>preinstalle<br>d on the<br>DCBOX<br>and do<br>not need<br>to be<br>prepared.) |
| DC power<br>cable<br>(single-<br>core) | Single-core outdoor cable and<br>M12 OT/DT terminal | 50-185 mm2 | 15-35 mm | 15-35 mm |
| PE cable[1] | Single-core outdoor copper<br>cable and M10 OT/DT terminal | Sp ≥ S/2 | - | Prepared<br>by the<br>customer |
| Communic<br>ations<br>cable | FE: CAT 5E outdoor shielded<br>network cable (internal<br>resistance ≤ 1 ohm/10 m) and<br>the shielded RJ45 connector | 0.2 mm2 | 4.5-7.5 mm | ●1.2 m,<br>delivere<br>d with<br>the<br>device<br>●You can<br>also<br>prepare<br>a cable<br>accordi<br>ng to<br>site<br>require<br>ments. |

<!-- Estadísticas: 4 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 45 LUNA2000-200KTL-H1 Smart Power Control System User Manual 5 Cable Connection -->
<!-- FIN TABLA 5-1 -->

indicates the conductor cross-sectional area of the PE cable)

|Cable|Type|Conductor Cross-<br>Sectional Area|Outer<br>Diameter|Source|
|---|---|---|---|---|
|DC power<br>cable<br>(multi-<br>core)|Two-core outdoor cable and<br>M12 OT/DT terminal|70-185 mm2|30-60 mm|Prepared<br>by the<br>customer<br>(In the<br>DCBOX<br>scenario,<br>the DC<br>cables are<br>preinstalle<br>d on the<br>DCBOX<br>and do<br>not need<br>to be<br>prepared.)|
|DC power<br>cable<br>(single-<br>core)|Single-core outdoor cable and<br>M12 OT/DT terminal|50-185 mm2|15-35 mm|15-35 mm|
|PE cable[1]|Single-core outdoor copper<br>cable and M10 OT/DT terminal|Sp ≥ S/2|-|Prepared<br>by the<br>customer|
|Communic<br>ations<br>cable|FE: CAT 5E outdoor shielded<br>network cable (internal<br>resistance ≤ 1 ohm/10 m) and<br>the shielded RJ45 connector|0.2 mm2|4.5-7.5 mm|●1.2 m,<br>delivere<br>d with<br>the<br>device<br>●You can<br>also<br>prepare<br>a cable<br>accordi<br>ng to<br>site<br>require<br>ments.|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 45

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

|Cable|Type|Conductor Cross-<br>Sectional Area|Outer<br>Diameter|Source|
|---|---|---|---|---|
|AC power<br>cable<br>(multi-<br>core)|Three-core (L1, L2, L3) outdoor<br>cable and M12 OT/DT terminal<br>(L1, L2, L3)|70-240 mm2|30-65 mm|Prepared<br>by the<br>customer|
|AC power<br>cable<br>(single-<br>core)|Single-core outdoor cable and<br>M12 OT/DT terminal|70-240 mm2|15-35 mm|Prepared<br>by the<br>customer|
|Note [1]: The Sp value is valid only if the conductors of the PE cable and AC power cable use the<br>same material. If the materials are diferent, ensure that the conductor cross-sectional area of the<br>PE cable produces a conductance equivalent to that specifed in this table. The specifcations of<br>the PE cable are subject to this table or calculated according to IEC 60364-5-54.|Note [1]: The Sp value is valid only if the conductors of the PE cable and AC power cable use the<br>same material. If the materials are diferent, ensure that the conductor cross-sectional area of the<br>PE cable produces a conductance equivalent to that specifed in this table. The specifcations of<br>the PE cable are subject to this table or calculated according to IEC 60364-5-54.|Note [1]: The Sp value is valid only if the conductors of the PE cable and AC power cable use the<br>same material. If the materials are diferent, ensure that the conductor cross-sectional area of the<br>PE cable produces a conductance equivalent to that specifed in this table. The specifcations of<br>the PE cable are subject to this table or calculated according to IEC 60364-5-54.|Note [1]: The Sp value is valid only if the conductors of the PE cable and AC power cable use the<br>same material. If the materials are diferent, ensure that the conductor cross-sectional area of the<br>PE cable produces a conductance equivalent to that specifed in this table. The specifcations of<br>the PE cable are subject to this table or calculated according to IEC 60364-5-54.|Note [1]: The Sp value is valid only if the conductors of the PE cable and AC power cable use the<br>same material. If the materials are diferent, ensure that the conductor cross-sectional area of the<br>PE cable produces a conductance equivalent to that specifed in this table. The specifcations of<br>the PE cable are subject to this table or calculated according to IEC 60364-5-54.|

## 5.3 Connecting a PE Cable

**Precautions**

NO TICE

 - The grounding shall comply with the local electrical safety regulations.

 - It is recommended that the Smart PCS be connected to a nearby ground point.
The ground points of all Smart PCSs in the same array need to be connected to
ensure equipotential bonding for PE cables.

 - The ground point in the AC maintenance compartment serves only as the
equipotential bonding point for the PE point and cannot replace the PE point of
the enclosure.

**Procedure**

**Step 1** Connect the PE cable.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 46

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

**Figure 5-1** Connecting the PE cable (AC side of the enclosure)

**----End**

**Follow-up Procedure**

To enhance the corrosion resistance of a ground terminal, apply silicone grease or
paint on it after connecting the PE cable.

## 5.4 Opening the Maintenance Compartment Door

**Precautions**

NO TICE

 - Do not open the panel of the Smart PCS.

 - Before opening a maintenance compartment door of the Smart PCS, turn off
the external switches on the AC and DC sides.

 - Do not open the maintenance compartment door on rainy or snowy days. If
you need to, take protective measures to prevent rain or snow from entering
the maintenance compartment. If protective measures cannot be taken, do not
open the maintenance compartment door.

 - Do not leave unused screws in the maintenance compartment.

### 5.4.1 Opening the DC Maintenance Compartment Door

**Step 1** Open the DC maintenance compartment door.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 47

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

**Figure 5-2** Opening the DC maintenance compartment door

**Step 2** Remove the accessories from the DC maintenance compartment and store them
properly for future use.

**Figure 5-3** Removing accessories from the DC maintenance compartment

(1) Spare screws on the door panel of
the maintenance compartment

**----End**

(2) Crimping module

### 5.4.2 Opening the AC Maintenance Compartment Door

**Step 1** Open the AC maintenance compartment door.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 48

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

**Figure 5-4** Opening the AC maintenance compartment door

**Step 2** Remove the accessories from the AC maintenance compartment and store them
properly for future use.

**Figure 5-5** Removing accessories from the AC maintenance compartment

(1) Spare screws on the door panel of
the maintenance compartment

**----End**

(2) Crimping module

## 5.5 (Optional) Replacing Crimping Modules

NO TE

If AC and DC power cables are multi-core cables, replace the crimping modules.

**Step 1** Replace the crimping modules.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 49

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

**Figure 5-6** Replacing the crimping module (on the DC side)

**Figure 5-7** Replacing the crimping module (on the AC side)

**----End**

## 5.6 Connecting DC Power Cables

**Precautions**

Before connecting the DC power cables, check the following items:

 - Check that the DC switches between the DC side of the Smart PCS and the DC
LV Panel busbar are off.

 - Check the polarities of the cables and label them properly.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 50

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

NO TICE

 - The cable outer diameter can be measured using the ruler sticker in the
maintenance compartment.

 - Ensure that the cable jacket is in the maintenance compartment.

 - Ensure that the DC power cables are connected securely. Otherwise, the
Smart PCS may fail to operate, or be overheated in operation due to
unreliable connection, which will damage the terminal block.

 - Do not pull the cables horizontally after they have been secured, as this
may damage the wiring terminals.

**Procedure**

**Step 1** Prepare the cables. For details, see **A Crimping an OT or DT Terminal** .

**Step 2** Remove a rubber ring based on the cable diameter range. Cut off the joints
between rubber rings using scissors and then remove the rubber ring. All rubber
rings are removed in the same way.

NO TE

Remove a rubber ring strictly based on the cable diameter range and ensure that the
crimping module is not damaged. Otherwise, the ingress protection (IP) rating of the device
will be affected.

**Figure 5-8** Removing a rubber ring

**Step 3** Connect the DC power cables to the terminal block and ensure that the cables are
securely connected.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 51

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

**Figure 5-9** Single-core cable connection (recommended)

**Figure 5-10** Multi-core cable connection (not recommended)

**----End**

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 52

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

## 5.7 Connecting AC Power Cables

**Precautions**

A three-phase AC switch shall be installed on the AC side of the Smart PCS. To
ensure that the Smart PCS can be safely disconnected from the power grid when
an exception occurs, select a proper overcurrent protection device in compliance
with local power distribution regulations.

- Do not connect loads between a Smart PCS and an AC switch that directly
connects to the Smart PCS. Otherwise, the switch may trip by mistake.

- If an AC switch is used with specifications beyond local standards, regulations,
or the Company's recommendations, the switch may fail to turn off in a timely
manner in case of exceptions, causing serious faults.

Each Smart PCS shall be equipped with an AC output switch. Multiple Smart PCSs
shall not connect to the same AC switch.

NO TICE

 - The cable outer diameter can be measured using the ruler sticker in the
maintenance compartment.

 - If a cable has a jacket, ensure that the jacket is in the maintenance
compartment.

 - Ensure that the AC power cables are connected securely. Otherwise, the Smart
PCS may fail to operate, or be overheated in operation due to unreliable
connection, which will damage the terminal block.

 - Do not pull the cables horizontally after they have been secured, as this may
damage the wiring terminals.

 - The AC power cables to all Smart PCSs in an array shall be connected in the
sequence of L1, L2, and L3. The phase sequence shall be consistent with that of
the transformer station.

**Step 1** Prepare cables by referring to the section **Crimping an OT or DT Terminal** .

**Step 2** Remove a rubber ring based on the cable diameter range. Cut off the joints
between rubber rings using scissors and then remove the rubber ring. All rubber
rings are removed in the same way.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 53

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

NO TE

Remove a rubber ring strictly based on the cable diameter range and ensure that the
crimping module is not damaged. Otherwise, the IP rating of the device will be affected.

**Figure 5-11** Removing a rubber ring

**Step 3** Connect the AC power cables to the terminal block and ensure that the cables are
securely connected.

NO TE

The cable colors shown in the figures are for reference only. Select an appropriate cable
according to the local standards.

**Figure 5-12** Single-core cable connection

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 54

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

**Figure 5-13** Multi-core cable connection

NO TE

It is recommended that the stripped length of the L2 wire be 15 mm shorter than that of
the L1 or L3 wire.

**----End**

## 5.8 Connecting Communications Cables

NO TICE

 - If multiple Smart PCSs are used, connect all Smart PCSs into a ring network in
hand-in-hand mode through FE communications cables.

 - The FE communications cables delivered with the Smart PCS are 1.2 m long.
Use the original cables if possible.

 - For parallel communication between multiple Smart PCSs, connect all the
Smart PCSs in hand-in-hand mode via COM ports.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 55

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

**Communications Ports**

**Figure 5-14** Port description

(1) Network port 2 (FE2) (2) Network port 1 (FE1) (3) Communications port
(COM)

### 5.8.1 Connecting FE Communications Cables

 - If the SmartACU2000D-D-06 is used, connect the Smart PCSs to the
SmartACU through FE communications cables. Ensure that the two ends are
connected to G2-G7 of the SmartACU (SWITCH02). A maximum of three ring
networks are supported.

 - If the SmartACU2000D-D-00, SmartACU2000D-D-01, or SmartACU2000DD-03 is used, connect the Smart PCSs to the SmartModule through FE
communications cables. Ensure that the two ends are connected to GE2 and
GE3 of the SmartModule. A maximum of one ring network is supported.

NO TE

The SmartACU2000D-D-00 and SmartACU2000D-D-01 can be configured with the
SmartModule optionally. The SmartACU2000D-D-03 is configured with the
SmartModule by default.

**Figure 5-15** Connecting FE communications cables (to the SmartACU2000D-D-06)

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 56

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

**Figure 5-16** Connecting FE communications cables (to the SmartACU2000D-D-00,
SmartACU2000D-D-01, or SmartACU2000D-D-03)

**Procedure**

**Step 1** Remove an appropriate length of the insulation layer from the shielded network
cable using a wire stripper.

**Step 2** Insert the shielded network cable through the sealing nut, sealing ring, coupling
nut, and plastic housing in sequence.

**Figure 5-17** Waterproof RJ45 connector composition

(1) Shielded plug (2) Plastic housing (3) Coupling nut

 (4) Sealing ring (5) Sealing nut

**Step 3** Line up the exposed wires of the shielded network cable in sequence and connect
them to the corresponding pins in the plug.

**Figure 5-18** Connecting a plug

**Step 4** Crimp the plug using a crimping tool.

**Step 5** Secure the plastic housing to the plug.

**Figure 5-19** Connecting a plastic housing

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 57

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

**Step 6** Insert the sealing ring into the plastic housing and secure the coupling nut to the
plastic housing.

**Figure 5-20** Connecting a sealing ring and a coupling nut

**Step 7** Secure the sealing nut to the plastic housing.

**Figure 5-21** Connecting a sealing nut

NO TICE

Ensure that the sealing nut is secured.

**Step 8** Insert the plugs into the FE ports on the Smart PCS and tighten the coupling nuts.

**Figure 5-22** Connecting the FE communications cables

(1) White-and
orange

(2) Orange (3) White-and
green

(4) Blue

(8) Brown

(5) White-and-blue (6) Green (7) White-andbrown

**Step 9** When multiple Smart PCSs are connected in parallel, bind the FE communications
cables connecting to the SmartACU or SmartModule at proper positions near the
ports.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 58

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

If Smart PCSs are installed on the DCBOX, bind the cables as shown in the
following figure.

**Figure 5-23** Binding FE communications cables

**----End**

## 5.9 Closing the Maintenance Compartment Door

**Precautions**

NO TICE

 - Before closing a maintenance compartment door, check that the cables are
connected correctly and securely, close the terminal block cover, and remove
any foreign object from the maintenance compartment.

 - If a screw on the maintenance compartment door is lost, obtain a spare screw
from the accessory bag in the maintenance compartment.

### 5.9.1 Closing the DC Maintenance Compartment Door

**Step 1** Adjust the support bar, close the maintenance compartment door, and tighten the
two screws on the door.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 59

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 5 Cable Connection

**Figure 5-24** Closing the DC maintenance compartment door

**----End**

### 5.9.2 Closing the AC Maintenance Compartment Door

**Step 1** Adjust the support bar, close the maintenance compartment door, and tighten the
two screws on the door.

**Figure 5-25** Closing the AC maintenance compartment door

**----End**

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 60

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual 6 Checking Before Power-On 6

**Checking Before Power-On**

Check the items listed in the following table. In case of any nonconforming items,
rectify the fault and reinstall the parts. Then check the items in the table again
until all they all pass the check.

**Table 6-1** Item

<!-- INICIO TABLA 6-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Check the items listed in the following table. In case of any nonconforming items, rectify the fault and reinstall the parts. Then check the items in the table again until all they all pass the check. -->

**Tabla 6-1: ** Item**

| Check Item | Expected Result |
| --- | --- |
| Installation<br>checks | The Smart PCS is not deformed or damaged. |
| Installation<br>checks | The Smart PCS is properly installed. |
| Installation<br>checks | The clearance around the Smart PCS meets requirements. |
| Electrical<br>connection<br>checks | The external switches on the AC and DC sides are in the OFF<br>position. |
| Electrical<br>connection<br>checks | All cables are intact and free from any damage or cracks. |
| Electrical<br>connection<br>checks | All ground cables are connected securely and reliably. |
| Electrical<br>connection<br>checks | All AC power cables are connected correctly and securely, and<br>no open circuits or short circuits occur. |
| Electrical<br>connection<br>checks | All DC cables are connected securely in correct polarity, and no<br>open circuits or short circuits occur. |
| Electrical<br>connection<br>checks | The communications cables are connected correctly and<br>securely. |
| Other check<br>items | The crimping module is securely installed. |
| Other check<br>items | The AC maintenance compartment is clean and tidy. |
| Other check<br>items | The DC maintenance compartment is clean and tidy. |
| Other check<br>items | The AC maintenance compartment door is closed and the<br>screws on the door are tightened. |
| Other check<br>items | The DC maintenance compartment door is closed and the<br>screws on the door are tightened. |

<!-- Estadísticas: 14 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 61 LUNA2000-200KTL-H1 Smart Power Control System User Manual 6 Checking Before Power-On -->
<!-- FIN TABLA 6-1 -->


|Check Item|Expected Result|
|---|---|
|Installation<br>checks|The Smart PCS is not deformed or damaged.|
|Installation<br>checks|The Smart PCS is properly installed.|
|Installation<br>checks|The clearance around the Smart PCS meets requirements.|
|Electrical<br>connection<br>checks|The external switches on the AC and DC sides are in the OFF<br>position.|
|Electrical<br>connection<br>checks|All cables are intact and free from any damage or cracks.|
|Electrical<br>connection<br>checks|All ground cables are connected securely and reliably.|
|Electrical<br>connection<br>checks|All AC power cables are connected correctly and securely, and<br>no open circuits or short circuits occur.|
|Electrical<br>connection<br>checks|All DC cables are connected securely in correct polarity, and no<br>open circuits or short circuits occur.|
|Electrical<br>connection<br>checks|The communications cables are connected correctly and<br>securely.|
|Other check<br>items|The crimping module is securely installed.|
|Other check<br>items|The AC maintenance compartment is clean and tidy.|
|Other check<br>items|The DC maintenance compartment is clean and tidy.|
|Other check<br>items|The AC maintenance compartment door is closed and the<br>screws on the door are tightened.|
|Other check<br>items|The DC maintenance compartment door is closed and the<br>screws on the door are tightened.|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 61

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 6 Checking Before Power-On

|Check Item|Expected Result|
|---|---|
||The waterproof plugs on the unused USB, COM, and FE ports<br>are secured.|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 62

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual 7 Power-On and Commissioning 7

**Power-On and Commissioning**

 - The Smart PCS can be commissioned on the SmartLogger WebUI or SUN2000
app. The SmartLogger can manage multiple devices. For details, see the
**[SmartLogger3000 User Manual](https://support.huawei.com/enterprise/en/doc/EDOC1100108365)** . The app is used for local commissioning,
mainly to modify the parameters and upgrade the software version of a single
Smart PCS.

 - Perform deployment commissioning for the Smart PCS and ESS together. For
details, see the **[LUNA2000-2.0MWH Series Smart String ESS User Manual](https://support.huawei.com/enterprise/en/doc/EDOC1100223175)** .

## 7.1 Powering on the Smart PCS

**Precautions**

Ensure that all the items in **6 Checking Before Power-On** are checked and meet
the requirements before power-on.

 - Wear personal protective equipment and use dedicated insulated tools to avoid
electric shocks or short circuits.

NO TICE

 - Before turning on the AC switch between the Smart PCS and the power grid,
check whether the AC voltage is within the allowed range using a multimeter.
(See the local power grid standard.)

 - Before the equipment is put into operation for the first time, ensure that the
parameters are set correctly by professional personnel. Incorrect parameter
settings may result in noncompliance with local grid connection requirements
and affect the normal operations of the equipment.

 - If the Smart PCS has not been used for six months or longer after being
installed, it must be checked and tested by professionals before operation.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 63

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 7 Power-On and Commissioning

### 7.1.1 On-Grid Power-On

**Procedure**

**Step 1** Turn on the AC switch between the AC side of the Smart PCS and the power grid.

**Step 2** Ensure that the DC side of the Smart PCS is properly connected to the ESS output.

**Step 3** Send a startup command on the SUN2000 app, SmartLogger, or management
system, and wait for the system soft start.

NO TE

Before sending a startup command to the Smart PCS, ensure that the DC voltage is within
the normal range.

**Step 4** Observe the LED indicators to check the running status of the Smart PCS.

**----End**

### 7.1.2 Off-Grid Power-On

For details about how to power on a medium-voltage microgrid system, see the
Medium-Voltage Microgrid Energy Storage Solution Quick Guide.

**Prerequisites**

 When there is no power supply from the power grid, turn off the high-voltage
side of the transformer station.

 - Check that the A/B/C phase sequence of the cable between the Smart PCS
and the low-voltage side of the transformer station is correct. The Smart PCSs
for the same ESS must be connected to the same low-voltage power
distribution system of the transformer station (in the double-split transformer
scenario).

 - The SACU and the CMU in the ESS are powered by the UPS.

 - The SACU and the CMU in the ESS have been networked.

**Procedure**

**Step 1** Ensure that the DC side of the Smart PCS is properly connected to the ESS output.

**Step 2** Turn on the AC switch between the AC side of the Smart PCS and the transformer
station.

**Step 3** Send a startup command on the SUN2000 app, SmartLogger, or management
system, and wait for the system soft start.

NO TE

Before sending a startup command to the Smart PCS, ensure that the DC voltage is within
the normal range.

**Step 4** Observe the LED indicators to check the running status of the Smart PCS.

**----End**

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 64

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 7 Power-On and Commissioning

### 7.1.3 Commissioning the Smart PCS Using the App

#### 7.1.3.1 Downloading the App

**App Functions**

The SUN2000 app (also referred to as the app) is a convenient local maintenance
platform that connects to the Smart PCS through WLAN and allows users to query
alarms, configure parameters, and perform routine maintenance.

The Smart PCS can be commissioned using the SmartLogger or app. For details
about how to commission the SmartLogger, see the **[SmartLogger3000 User](https://support.huawei.com/enterprise/en/doc/EDOC1100108365)**
**[Manual](https://support.huawei.com/enterprise/en/doc/EDOC1100108365)** . The app is used for local commissioning, mainly to modify the
parameters and upgrade the software version of a single Smart PCS.

**Downloading the App**

Access Huawei AppGallery, search for **SUN2000**, and download the app.
Alternatively, scan the following QR codes to download the app installation
package.

QR codes:

**Connecting the Smart PCS to the App**

After the DC or AC side of the Smart PCS is powered on, the app can connect to
the Smart PCS through the WLAN module.

NO TICE

 - The USB-Adapter2000-C WLAN module is supported.

 - The mobile phone operating system must be Android 5.0 or later.

 - Huawei and Samsung phones are recommended.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 65

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 7 Power-On and Commissioning

**Figure 7-1** WLAN module connection

(A) Smart PCS (B) WLAN module (C) Mobile phone

NO TICE

 - If the AC switch between the Smart PCS and the power grid is turned on, but
the external switch on the DC side of the Smart PCS is turned off, some
parameters cannot be set. Turn on the external switch on the DC side, and then
reconfigure the parameters.

 - Changing the grid code will restore some parameters to factory defaults. After
the grid code is changed, check whether the previously set parameters are
affected.

 - When the Smart PCS receives a reset, shutdown, or upgrade command, it may
disconnect from the grid, affecting the energy yield.

 - When the Smart PCS is powered on for the first time, ensure that the
parameters are set correctly by professionals. Incorrect parameter settings may
result in noncompliance with local requirements and affect the normal
operations of the Smart PCS.

 - Only professionals are allowed to set the grid, protection, feature, and power
adjustment parameters of the Smart PCS. If the grid, protection, and feature
parameters are set incorrectly, the Smart PCS may disconnect from the grid. If
the power adjustment parameters are set incorrectly, the Smart PCS may not
connect to the power grid as required. In these cases, the energy yield will be
affected.

NO TE

 Configurable parameters vary depending on the grid code.

 - The parameter names, value ranges, and default values are subject to change. The
actual display may vary.

#### 7.1.3.2 Logging In to the App

**Prerequisites**

 - The DC or AC side of the Smart PCS has been powered on.

 - When connecting through a WLAN module:

a. The WLAN module has been inserted into the **USB** port at the bottom of
the Smart PCS.

b. The WLAN function has been enabled on your phone.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 66

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 7 Power-On and Commissioning

c. Keep the mobile phone within 5 m from the Smart PCS. Otherwise, the
communication between them might be affected.

**Procedure**

**Step 1** In the SUN2000 app, select a connection mode.

NO TE

 - The screenshots in this section correspond to the SUN2000 app 6.23.00.125 (Android).

 - When the WLAN connection is used, scan the QR code of the WLAN module to access
the login screen.

 - When the WLAN connection is used, the initial name of the WLAN hotspot is **Adapter-**
**WLAN module SN** and the initial password is **Changeme** . Use the initial password for
the first login and change it immediately after login. To ensure account security, protect
the password by changing it periodically, and keep it secure. Your password might be
stolen or cracked if it is left unchanged for extended periods. If a password is lost,
devices cannot be accessed. In these cases, the Company shall not be liable for any loss
caused to the plant.

**Figure 7-2** Selecting a connection mode

**Step 2** Select the login user and enter the login password. The main menu screen is
displayed.

NO TICE

 - When you log in to the system for the first time, set the login password. To
ensure account security, protect the password by changing it periodically, and
keep it secure. Your password might be stolen or cracked if it is left unchanged
for extended periods. If a password is lost, devices cannot be accessed. In these
cases, the Company shall not be liable for any loss caused to the plant.

 - You will be locked out for 10 minutes after five consecutive failed password
attempts at an interval of less than 2 minutes.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 67

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 7 Power-On and Commissioning

**Figure 7-3** Login

NO TE

Set the correct grid code based on the application area and scenario of the Smart PCS.

**----End**

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 68

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual 8 Device Maintenance 8 Device Maintenance

## 8.1 Routine Maintenance

**Precautions**

- Wear personal protective equipment and use dedicated insulated tools to avoid
electric shocks or short circuits.

- Before performing maintenance, power off the equipment, follow the
instructions on the delayed discharge label, and wait for a period of time as
specified to ensure that the equipment is not energized.

When cleaning the system, connecting cables, and checking grounding reliability,
power off the system and ensure that the external switches on the DC and AC
sides are turned off.

**Maintenance Items**

To ensure that the device operates properly for a long term, you are advised to
perform routine maintenance as described in this section.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 69

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 8 Device Maintenance

**Table 8-1** Maintenance checklist

<!-- INICIO TABLA 8-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 69 LUNA2000-200KTL-H1 Smart Power Control System User Manual 8 Device Maintenance -->

**Tabla 8-1: ** Maintenance checklist**

| Check Item | Check Method | Maintenance<br>Interval |
| --- | --- | --- |
| ●Cleanness of<br>the air intake<br>vent<br>●Cleanness of<br>the air exhaust<br>vent<br>●Fan | ●Check whether there is dust on<br>the air intake and exhaust vents.<br>If necessary, remove and clean<br>the bafe plates.<br>●Check whether the fans<br>generate abnormal noise during<br>operation. | Once every 6 to 12<br>months |
| System status | ●Check whether the enclosure is<br>damaged or deformed.<br>●Check whether the device<br>generates abnormal sounds<br>during operation.<br>●Check whether the parameters<br>are correctly set during<br>operation. | Once every 6 months |
| Cable connection | ●Check whether cables are<br>disconnected or loose.<br>●Check whether cables are<br>damaged, especially whether<br>the cable sheath that contacts a<br>metal surface is damaged.<br>●Check whether the unused<br>COM, USB, and FE ports are<br>locked by waterproof caps. | 6 months after the<br>frst commissioning<br>and once every 6 to<br>12 months after that |
| Grounding<br>reliability | Check whether the ground cables<br>are securely grounded. | 6 months after the<br>frst commissioning<br>and once every 6 to<br>12 months after that |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Removing the Baffle Plate from the Air Intake Vent** **Figure 8-1** Removing the baffle plate -->
<!-- FIN TABLA 8-1 -->


|Check Item|Check Method|Maintenance<br>Interval|
|---|---|---|
|●Cleanness of<br>the air intake<br>vent<br>●Cleanness of<br>the air exhaust<br>vent<br>●Fan|●Check whether there is dust on<br>the air intake and exhaust vents.<br>If necessary, remove and clean<br>the bafe plates.<br>●Check whether the fans<br>generate abnormal noise during<br>operation.|Once every 6 to 12<br>months|
|System status|●Check whether the enclosure is<br>damaged or deformed.<br>●Check whether the device<br>generates abnormal sounds<br>during operation.<br>●Check whether the parameters<br>are correctly set during<br>operation.|Once every 6 months|
|Cable connection|●Check whether cables are<br>disconnected or loose.<br>●Check whether cables are<br>damaged, especially whether<br>the cable sheath that contacts a<br>metal surface is damaged.<br>●Check whether the unused<br>COM, USB, and FE ports are<br>locked by waterproof caps.|6 months after the<br>frst commissioning<br>and once every 6 to<br>12 months after that|
|Grounding<br>reliability|Check whether the ground cables<br>are securely grounded.|6 months after the<br>frst commissioning<br>and once every 6 to<br>12 months after that|

**Removing the Baffle Plate from the Air Intake Vent**

**Figure 8-1** Removing the baffle plate

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 70

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 8 Device Maintenance

NO TICE

After the cleaning is complete, reinstall the baffle plate to the air intake vent.
Tighten the screws with a torque of 1.2 N·m.

**Removing the Protective Cover from the Air Exhaust Vent**

**Figure 8-2** Removing the protective cover

NO TICE

After the cleaning is complete, reinstall the protective cover to the air exhaust
vent. Tighten the screws with a torque of 1.2 N·m.

## 8.2 Powering Off the System

**Precautions**

To prevent personal injury and equipment damage, perform the following
procedure to power off the Smart PCS for troubleshooting or replacement.

 - If the DC switch between the Smart PCS and the DC LV Panel busbar has been
turned off automatically, do not turn on the switch before the fault is rectified.

 - If the AC switch between the Smart PCS and the power grid has been turned
off automatically, do not turn it on before the fault is rectified.

 - Before power-off for maintenance, do not touch the energized components of
the Smart PCS. Otherwise, electric shocks or arcs may occur.

**Procedure**

**Step 1** Wear proper PPE.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 71

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 8 Device Maintenance

**Step 2** Send a shutdown command on the SUN2000 app, SmartLogger, or management
system.

**Step 3** Turn off the AC switch between the Smart PCS and the power grid or load.

**Step 4** Open the AC maintenance compartment door, install a support bar, and use a
multimeter to check the voltage between the AC terminal block and the ground.
Ensure that the AC side of the Smart PCS is powered off.

**Step 5** Turn off the DC switch between the Smart PCS and the DC LV Panel busbar.

**Step 6** Open the DC maintenance compartment door, install a support bar, and use a
multimeter to check the voltage between DC terminal blocks. Ensure that the DC
side of the Smart PCS is powered off.

**Step 7** Wait for 15 minutes and troubleshoot or repair the Smart PCS.

**Figure 8-3** Power-off for maintenance

 - Do not open the panel for maintenance if the Smart PCS is emitting abnormal
smell or smoke, or has obvious exceptions.

 - If the Smart PCS does not emit abnormal smell or smoke and is intact, repair or
restart it based on the alarm handling suggestions.

**----End**

## 8.3 Alarm Reference

For details about alarms, see the **[LUNA2000-100KTL and 200KTL Series Smart](https://support.huawei.com/enterprise/en/doc/EDOC1100315385)**
**[Power Control System Alarm Reference](https://support.huawei.com/enterprise/en/doc/EDOC1100315385)** .

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 72

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 8 Device Maintenance

## 8.4 Replacing a Fan

**Precautions**

 - Before replacing a fan, power off the Smart PCS.

 - When replacing a fan, use insulated tools and wear PPE.

NO TE

If the fan gets stuck when being pulled or pushed, slightly lift it.

**Procedure**

**Step 1** Remove the screws from the fan tray and store them properly. Pull out the fan
tray until the fan tray is flush with the Smart PCS.

**Figure 8-4** Pulling out the fan tray (1)

**Step 2** Remove the cable ties shared by the cables, unscrew the connectors, and
disconnect the cables.

**Figure 8-5** Disconnecting cables

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 73

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 8 Device Maintenance

**Step 3** Pull out the fan tray completely.

**Figure 8-6** Pulling out the fan tray (2)

**Step 4** Remove cable ties of the faulty fan.

 - FAN 1 is faulty.

**Figure 8-7** Removing cable ties from FAN 1

 - FAN 2 is faulty.

**Figure 8-8** Removing cable ties from FAN 2

 - FAN 3 is faulty.

**Figure 8-9** Removing cable ties from FAN 3

**Step 5** Remove the faulty fan (FAN 1 is used as an example).

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 74

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 8 Device Maintenance

**Figure 8-10** Removing the fan

**Step 6** Install a new fan (FAN 1 is used as an example).

**Figure 8-11** Installing a fan

**Step 7** Bind the fan cables.

 - Binding positions for FAN 1

**Figure 8-12** Binding the cables of FAN 1

 - Binding positions for FAN 2

**Figure 8-13** Binding the cables of FAN 2

 - Binding positions for FAN 3

**Figure 8-14** Binding the cables of FAN 3

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 75

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 8 Device Maintenance

**Step 8** Push in the fan tray until the fan baffle plate is flush with the Smart PCS.

**Figure 8-15** Pushing in the fan tray

**Step 9** Connect the cables correctly according to the cable labels and bind the cables.

**Figure 8-16** Binding cables

**Step 10** Push in the fan tray completely and tighten the screws.

**Figure 8-17** Reinstalling the fan tray

**----End**

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 76

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 8 Device Maintenance

## 8.5 Replacing the Smart PCS

**Context**

The device enclosure is severely damaged or the device hardware is faulty due to
external forces.

**Procedure**

**Step 1** Send a shutdown command on the SUN2000 app, SmartLogger, or management
system.

**Step 2** Turn off the external switches on the DC and AC sides.

**Step 3** Remove the DC power cables, AC power cables, communications cables, and PE
cable from the Smart PCS in sequence.

**Step 4** Remove the Smart PCS based on site requirements.

1. Support-mounted or wall-mounted

**Figure 8-18** Removing the Smart PCS

2. Installed on the DCBOX

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 77

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 8 Device Maintenance

**Figure 8-19** Removing screws from the Smart PCS

**Figure 8-20** Removing the Smart PCS

**Step 5** Install the new Smart PCS.

**Step 6** Connect the PE cable, DC power cables, AC power cables, and communications
cables in sequence. For details, see **5 Cable Connection** .

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 78

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 8 Device Maintenance

**Step 7** Power on the Smart PCS. Observe the LED indicators to check the running status
of the Smart PCS and verify that the replacement is successful.

**----End**

**Follow-up Procedure**

**Step 1** Log in to the SmartLogger WebUI, choose **Maintenance > Connect Device**, select

the ESS, and click to send a startup command. Observe LED indicators of the
Smart PCS and ensure that the DC side of the Smart PCS is powered on.

**Step 2** Upgrade software of the new Smart PCS. Ensure that the software version of the
new Smart PCS is the same as that of other Smart PCSs on site.

**Step 3** Choose **Monitoring > Running Param. > Grid Parameters**, and set **Grid code** .
Ensure that the grid code setting of the new Smart PCS matches the local grid
code. Wait for 10s, and then go to step 4.

**Step 4** The settings of **Grid Parameters**, **Protection Parameters**, **Feature Parameters**,
**Power Adjustment**, and **Power Baseline** of the new device must be synchronized
from other devices. This section uses **Grid Parameters** settings as an example to
describe how to synchronize data. The operations for setting other parameters are
similar.

Click **Monitoring**, select a running device, choose **Running Param. > Grid**
**Parameters > All > Batch configurations**, and click **Confirm** to synchronize data
to the new device.

**Figure 8-21** Setting running parameters

**Step 5** Click **Monitoring** .

1. Select the faulty Smart PCS, choose **Running Param. > Adjustment**, and
record the values of **Adjust total energy yield** and **Calibration of total**
**power supply from grid** .

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 79

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 8 Device Maintenance

2. Select the new device, choose **Running Param. > Adjustment**, and set **Adjust**
**total energy yield** and **Calibration of total power supply from grid** to be
the same as those of the original device.

**Figure 8-22** Energy yield calibration

**Step 6** (Optional) If a third-party NMS that complies with the IEC 104 protocol is
connected, choose **Settings > IEC104**, and ensure that the teleindication,
telemetering, telecontrol, and teleadjust signal numbers of the new Smart PCS on
all tab pages under IEC104 are the same as those of the faulty Smart PCS.

**Step 7** Identify the topology.

 - For SmartLogger V300R024C00 and later versions, enter the SNs of the old
and new devices and click **Submit** . The devices in the topology are
automatically updated.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 80

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 8 Device Maintenance

**Figure 8-23** Replacing devices

 - For versions earlier than SmartLogger V300R024C00, go to **Deployment**
**Wizard** and click **Search for Device** to check cable connections and allocate

addresses.

**Figure 8-24** Searching for devices

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 81

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 8 Device Maintenance

NO TE

- During the process of **Search for Device**, do not perform upgrade operations (such
as upgrading through the app, management system, or WebUI).

- When you click **Search for Device**, cable connections (DC and AC) will be checked
before device search (not applicable to third-party devices), and device addresses
will be automatically allocated.

-
After the cable connection check and device search are complete, if a cable

connection alarm is generated, you can click the alarm icon to view the
corresponding alarm information.

-
If an alarm is generated when the cable connection check fails, click the alarm icon

to view the alarm cause and handling suggestions. After the fault is rectified,
check the cable connections again.

- After the cable connection check and device search are complete, click to view
the corresponding topology information.

- After a device is added or deleted, you need to click **Search for Device** again in
**Deployment Wizard** . Otherwise, the system topology will not be updated.

**Step 8** Delete the faulty Smart PCS.

Choose **Maintenance > Connect Device**, select the faulty Smart PCS, click
**Remove Devices**, and click **Confirm** .

**Figure 8-25** Deleting a device

**Step 9** Choose **Maintenance > Connect Device**, select the Smart PCS, and click to
send a startup command. After the Smart PCS is started, check that it is running
properly.

**Step 10** (Optional) Log in to the PV plant management system, access the plant, choose
**Device Management**, select the faulty Smart PCS, click **Delete**, and click **OK** .

NO TE

 - Perform this step if you purchase and use the PV plant management system.

 - The software version corresponding to the user interface (UI) screenshot in this step is
iMaster NetEco V600R023C00SPC110. The UI may vary by software versions and the
screenshot is for reference only.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 82

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 8 Device Maintenance

**Figure 8-26** Deleting a device

**----End**

## 8.6 Disposing of the Smart PCS

If the Smart PCS reaches the end of its service life, dispose of the device according
to local regulations for the disposal of electrical equipment.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 83

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual 9 Technical Specifications 9

**Technical Specifications**

**Efficiency**

**DC Side**

**Protection**

|Item|LUNA2000-200KTL-H1|
|---|---|
|Maximum efciency|99.01%|

|Item|LUNA2000-200KTL-H1|
|---|---|
|Number of DC routes|1|
|Maximum DC voltage|1500 V|
|Maximum DC power|245 kW|
|Maximum DC current|207.6 A|
|Minimum startup voltage[1]|540 V|
|Full-load voltage range|1180-1350 V (rectifer mode)<br>1180-1280 V (inverter mode)|
|Operating voltage range|1180-1500 V|
|Rated DC voltage|1180 V|
|Note [1]: The minimum startup voltage is the minimum startup voltage of the<br>auxiliary power supply inside the device.|Note [1]: The minimum startup voltage is the minimum startup voltage of the<br>auxiliary power supply inside the device.|

|Item|LUNA2000-200KTL-H1|
|---|---|
|Anti-islanding protection|Supported|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 84

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 9 Technical Specifications

|Item|LUNA2000-200KTL-H1|
|---|---|
|AC overcurrent protection|Supported|
|DC reverse connection protection|Supported|
|DC surge protection|Type II|
|AC surge protection|Type II|
|Insulation resistance detection|Supported|
|Residual current monitoring unit<br>(RCMU)|Supported|
|Overvoltage category|DC II/AC III|

**Display and Communication**

|Item|LUNA2000-200KTL-H1|
|---|---|
|Display|LED indicators and WLAN module+app|
|Ethernet|Supported|
|USB|Supported|

**General Specifications**

|Item|LUNA2000-200KTL-H1|
|---|---|
|Dimensions (H x W x D)|820 mm x 875 mm x 365 mm|
|Net weight|< 99 kg|
|Operating temperature|-25°C to +60°C (derated at +40°C or<br>higher)|
|Cooling mode|Smart air cooling|
|Maximum operating altitude|4000 m (derated when the altitude is<br>greater than 2000 m)|
|Relative humidity|0%-100% RH|
|AC/DC terminal|OT/DT terminal|
|IP rating|IP66|
|Topology|Transformerless|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 85

LUNA2000-200KTL-H1 Smart Power Control System
User Manual 9 Technical Specifications

**On-Grid Parameters**

|Item|LUNA2000-200KTL-H1|
|---|---|
|Rated AC voltage|800 V|
|Rated AC power|200 kW|
|Maximum apparent power|240 kVA|
|Maximum active power|240 kW|
|Rated AC current|144.3 A|
|Maximum AC current|173.2 A|
|Supported power grid frequency|50 Hz/60 Hz|
|Power factor|1 leading and 1 lagging|
|Maximum total harmonic distortion<br>(rated power)|< 3%|

**Off-Grid Parameters**

|Item|LUNA2000-200KTL-H1|
|---|---|
|AC output voltage|800 V (line voltage)|
|DC component in output voltage|±0.1% (with a transformer)|
|Output frequency|50 Hz/60 Hz|
|Phase diference (three-phase voltage)|120±1° (balanced load)|
|Rated output power|200 kW|
|Voltage THD_linear load|< 1.5% (0.8 leading and 0.8 lagging)|
|Unbalanced load|100% unbalanced (with a transformer)|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 86

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual A Crimping an OT or DT Terminal A

**Crimping an OT or DT Terminal**

**Requirements for OT/DT terminals**

 - If a copper cable is used, use copper wiring terminals.

 - If a copper-clad aluminum cable is used, use copper wiring terminals.

 - If an aluminum alloy cable is used, use copper-to-aluminum wiring terminals,
or aluminum wiring terminals with copper-to-aluminum washers.

NO TICE

 - Do not connect aluminum wiring terminals directly to the AC or DC terminal
block, as this may lead to electrochemical corrosion which affects the reliability
of cable connections.

 - Comply with IEC 61238-1 requirements when using copper-to-aluminum wiring
terminals, or aluminum wiring terminals with copper-to-aluminum washers.

 - Ensure that the aluminum side of the washer contacts the aluminum wiring
terminal, and the copper side contacts the terminal block.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 87

LUNA2000-200KTL-H1 Smart Power Control System
User Manual A Crimping an OT or DT Terminal

**Figure A-1** Requirements for OT/DT terminals

**Crimping an OT or DT Terminal**

NO TICE

 - Avoid scratching the core wire when stripping a cable.

 - The cavity formed after the conductor crimp strip of the OT or DT terminal has
been crimped must completely wrap around the core wires. In addition, the
core wires must be in close contact with the OT or DT terminal.

 - Wrap the wire crimping area with heat-shrink tubing or insulation tape. Heatshrink tubing is used in this section as an example.

 - Take care when using a heat gun to avoid heat damage to the equipment.

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 88

LUNA2000-200KTL-H1 Smart Power Control System
User Manual A Crimping an OT or DT Terminal

**Figure A-2** Crimping an OT terminal

(1) Cable (2) Core (3) Heat-shrink tubing

(4) OT terminal (5) Hydraulic pliers (6) Heat gun

**Figure A-3** Crimping a DT terminal

(1) Cable (2) Core (3) Heat-shrink tubing

(4) DT terminal (5) Hydraulic pliers (6) Heat gun

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 89

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual B Grid Codes B Grid Codes

NO TE

The grid codes are subject to change. The listed codes are for reference only.

Set the correct grid code for the Smart PCS based on regions and application
scenarios.

|No.|Grid Code|Description|LUNA2000-200KTL-H1|
|---|---|---|---|
|1|IEC61727-MV800|IEC 61727 medium-voltage<br>standard power grid (50 Hz)|Supported|
|2|Chile-MV800|Chile power grid|Supported|
|3|TAI-PEA-MV800|Thailand power grid|Supported|
|4|SAUDI-MV800|Saudi Arabia power grid|Supported|
|5|EN50549-MV800|Ireland power grid|Supported|
|6|IEC 61727-MV800-60HZ|General power grid|Supported|
|7|CEI0-16-MV800|Italy medium-voltage power<br>grid|Supported|
|8|NIGERIA-MV800|Nigeria medium-voltage<br>power grid|Supported|
|9|VDE-AR-N4120-HV800|VDE 4120 standard power<br>grid|Supported|
|10|CHILE-PMGD-MV800|Chile PMGD medium-<br>voltage power grid (800 V)|Supported|
|11|GHANA-MV800|Ghana medium-voltage<br>power grid (800 V)|Supported|
|12|TAI-MEA-MV800|Thailand medium-voltage<br>power grid|Supported|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 90

LUNA2000-200KTL-H1 Smart Power Control System
User Manual B Grid Codes

|No.|Grid Code|Description|LUNA2000-200KTL-H1|
|---|---|---|---|
|13|G99-TYPEB-HV-MV800|UK G99_TypeB_HV medium-<br>voltage power grid|Supported|
|14|G99-TYPEC-HV-MV800|UK G99_TypeC_HV medium-<br>voltage power grid|Supported|
|15|G99-TYPED-MV800|UK G99_TypeD medium-<br>voltage power grid|Supported|
|16|VDE-AR-N4110-MV800|Germany medium-voltage<br>power grid (800 V)|Supported|
|17|NTS-MV800|Spain medium-voltage<br>power grid|Supported|
|18|PERU-MV800|Peru medium-voltage power<br>grid|Supported|
|19|AUSTRIA-MV800|Austria Type B medium-<br>voltage power grid|Supported|
|20|POLAND-EN50549-MV800|Poland medium-voltage<br>power grid|Supported|
|21|CHINA-GBT34120-MV800|China medium-voltage<br>power grid for commercial<br>energy storage|Supported|
|22|Japan-MV550-50Hz|Japan medium-voltage<br>power grid|Supported|
|23|Japan-MV550-60Hz|Japan medium-voltage<br>power grid|Supported|
|24|ABNT NBR 16149-MV800|Brazil power grid|Supported|
|25|UTE C 15-712-1-MV800|France power grid|Supported|
|26|Philippines-MV800|Philippines power grid|Supported|
|27|NRS-097-2-1-MV800|South Africa power grid|Supported|
|28|Jordan-Transmission-<br>MV800|Jordan power grid|Supported|
|29|Jordan-Distribution-<br>MV800|Jordan power grid|Supported|
|30|DUBAI-MV800|Dubai power grid|Supported|
|31|IEEE 1547-MV800|IEEE 1547 standard power<br>grid|Supported|
|32|C10/11-MV800|Belgium power grid|Supported|
|33|IEC61727-MV800|IEC 61727 medium-voltage<br>standard power grid|Supported|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 91

LUNA2000-200KTL-H1 Smart Power Control System
User Manual B Grid Codes

|No.|Grid Code|Description|LUNA2000-200KTL-H1|
|---|---|---|---|
|34|Mexico-MV800|Mexico power grid|Supported|
|35|SA_RPPs-MV800|South Africa power grid|Supported|
|36|Israel-MV800|Israel power grid|Supported|
|37|AUSTRALIA-NER-MV800|Australia NER standard<br>power grid|Supported|
|38|RD1699/661-MV800|Spain medium-voltage<br>power grid|Supported|
|39|Israel-HV800|Israel high-voltage power<br>grid (161 kV)|Supported|
|40|AUSTRIA-HV800|Austria medium-voltage<br>power grid (type D)|Supported|
|41|DENMARK-EN50549-<br>MV800|Denmark power grid|Supported|
|42|FINLAND-EN50549-<br>MV800|Finland power grid|Supported|
|43|EN50549-SE-MV800|Sweden power grid|Supported|
|44|CEPM-MV800|Dominican Republic<br>medium-voltage power grid|Supported|
|45|SA-BESF-L-MV800|South Africa BESF-L<br>medium-voltage power grid|Supported|
|46|SA-BESF-H-MV800|South Africa BESF-H<br>medium-voltage power grid|Supported|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 92

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual C Resetting Password C

**Resetting Password**

NO TICE

You are advised to reset the password in the morning or at night when the solar
irradiance is low.

Reset the password only when the AC power is supplied to the Smart PCS from
the power grid, diesel generator, or other voltage-source PCSs.

**Step 1** Check that the AC and DC sides of the Smart PCS are both powered on, and
indicators and are steady green or blinking slowly for more than 3 minutes.

**Step 2** Turn off the AC switch between the AC side of the Smart PCS and the power grid
to power off the AC side of the Smart PCS.

**Step 3** Turn off the DC switch between the DC side of the Smart PCS and the ESS to
power off the DC side of the Smart PCS.

**Step 4** After the Smart PCS is powered off, complete the following operations within 4
minutes:

1. Turn on the AC switch and wait for about 90s or until the Smart PCS indicator

blinks.

2. Turn off the AC switch, and wait for about 30s or until all LED indicators on
the Smart PCS panel turn off.

3. Turn on the AC switch and wait for about 90s or until the Smart PCS indicator

blinks.

**Step 5** Log in to the app and reset the password within 10 minutes. Otherwise, all
parameters of the Smart PCS remain unchanged.

**----End**

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 93

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual D Certificate Management and Maintenance D

**Certificate Management and**

**Maintenance**

**Preconfigured Certificate Risk Disclaimer**

The Huawei-issued certificates preconfigured on Huawei devices during
manufacturing are mandatory identity credentials for Huawei devices. The
disclaimer statements for using the certificates are as follows:

1. Preconfigured Huawei-issued certificates are used only in the deployment
phase, for establishing initial security channels between devices and the
customer's network. Huawei does not promise or guarantee the security of
preconfigured certificates.

2. The customer shall bear consequences of all security risks and security
incidents arising from using preconfigured Huawei-issued certificates as
service certificates.

3. A preconfigured Huawei-issued certificate is valid from the manufacturing
date until October 2041.

4. Services using a preconfigured Huawei-issued certificate will be interrupted
when the certificate expires.

5. It is recommended that customers deploy a PKI system to issue certificates for
devices and software on the live network and manage the lifecycle of the
certificates. To ensure security, certificates with short validity periods are
recommended.

**Application Scenarios of Preconfigured Certificates**

|File Path and Name|Scenario|Replacement|
|---|---|---|
|f:/ca.crt|Two-way certifcate<br>authentication is<br>performed when the<br>Smart PCS<br>communicates with the<br>SACU through Modbus-<br>TCP.|For details about how to<br>replace a certifcate,<br>contact technical support<br>engineers to obtain the<br>corresponding security<br>maintenance manual.|
|f:/tomcat_client.crt|f:/tomcat_client.crt|f:/tomcat_client.crt|
|f:/tomcat_client.key|f:/tomcat_client.key|f:/tomcat_client.key|

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 94

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual E Contact Information E Contact Information

If you have any questions about this product, please contact us.

**[https://digitalpower.huawei.com](https://digitalpower.huawei.com)**

Path: **About Us** - **Contact Us** - **Service Hotlines**

To ensure faster and better services, we kindly request your assistance in providing
the following information:

 - Model

 - Serial number (SN)

 - Software version

 - Alarm ID or name

 - Brief description of the fault symptom

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 95

LUNA2000-200KTL-H1 Smart Power Control System
User Manual E Contact Information

NO TE

EU Representative Information: Huawei Technologies Hungary Kft.

Add.: HU-1133 Budapest, Váci út 116-118., 1. Building, 6. floor.

Email: hungary.reception@huawei.com

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 96

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual F Digital Power Customer Service F

**Digital Power Customer Service**

**[https://digitalpower.huawei.com/robotchat/](https://digitalpower.huawei.com/robotchat/)**

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 97

LUNA2000-200KTL-H1 Smart Power Control System
# User Manual G Acronyms and Abbreviations G

**Acronyms and Abbreviations**

**F**

**FE** Fast Ethernet

# G

**GE** Gigabit Ethernet

**L**

**LED** Light Emitting Diode

**R**

**RCMU** Residual Current
Monitoring Unit

**S**

**Smart PCS** Smart Power Control

System

**W**

**WLAN** Wireless Local Area

Network

Issue 08 (2024-01-23) Copyright © Huawei Technologies Co., Ltd. 98