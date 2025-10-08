---
title: User Manual
author: Huawei Technologies Co.,Ltd.
date: D:20240201200115+08'00'
language: en
type: report
pages: 67
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - User Manual About This Document About This Document
  - User Manual Contents Contents
  - 1 Safet Information
  - Copyright © Huawei Digital Power Technologies Co., Ltd. 1
  - 2 Overview
  - 3 Trans ortation and Stora e
  - 4 Site Re uirements
  - 5 Installin ESS
  - 6 Installin Cables
  - 7 Power-On and Commissionin
  ... y 3 secciones más
-->

**LUNA2000-4.5MWH-2H1 Smart String ESS**

**User Manual**

**Issue** **Preliminary Version**

**Date** **2024-01-23**

**HUAWEI DIGITAL POWER TECHNOLOGIES CO., LTD.**

**Copyright © Huawei Digital Power Technologies Co., Ltd 2024. All rights reserved.**

No part of this document may be reproduced or transmitted in any form or by any means without prior
written consent of Huawei Digital Power Technologies Co., Ltd

**Trademarks and Permissions**

and other Huawei trademarks are the property of Huawei Technologies Co., Ltd.

All other trademarks and trade names mentioned in this document are the property of their respective
holders.

**Notice**

The purchased products, services and features are stipulated by the contract made between Huawei Digital
Power Technologies Co., Ltd. and the customer. All or part of the products, services and features described
in this document may not be within the purchase scope or the usage scope. Unless otherwise specified in
the contract, all statements, information, and recommendations in this document are provided "AS IS"
without warranties, guarantees or representations of any kind, either express or implied.

The information in this document is subject to change without notice. Every effort has been made in the
preparation of this document to ensure accuracy of the contents, but all statements, information, and
recommendations in this document do not constitute a warranty of any kind, express or implied.

Huawei Digital Power Technologies Co., Ltd

Address: Huawei Digital Power Antuoshan Headquarters

Futian, Shenzhen 518043

People's Republic of China

Website: [https://digitalpower.huawei.com](https://digitalpower.huawei.com/)

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. i

LUNA2000-4.5MWH-2H1 Smart String ESS
# User Manual About This Document About This Document

**Purpose**

This document describes the safety information, appearance, transportation and storage, site
requirements, installation, electrical connections, commissioning and maintenance of
LUNA2000-4.5MWH-2H1 Smart String Energy Storage System (also referred to as ESS).
Before installing and operating the ESS, ensure that you are familiar with this document.

**Intended Audience**

The document is intended for:

 Technical support engineers

 Hardware installation engineers

 Commissioning engineers

 Maintenance engineer

**Symbol Conventions**

The symbols that may be found in this document are defined as follows.

|Symbol|Description|
|---|---|
||Indicates a hazard with a high level of risk which, if not avoided, will<br>result in death or serious injury.|
||Indicates a hazard with a medium level of risk which, if not avoided,<br>could result in death or serious injury.|
||Indicates a hazard with a low level of risk which, if not avoided, could<br>result in minor or moderate injury.|
||Indicates a potentially hazardous situation which, if not avoided, could<br>result in equipment damage, data loss, performance deterioration, or<br>unanticipated results.<br>NOTICE is used to address practices not related to personal injury.|
||Supplements the important information in the main text.<br>NOTE is used to address information not related to personal injury,<br>equipment damage, and environment deterioration.|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. ii

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual About This Document

**Change History**

Changes between document issues are cumulative. The latest document issue contains all
updates made in previous issues.

**Issue Draft B (2024-01-23)**

Update 2.1 Model Description, 2.2 Appearance, 10 Technical Specifications.

**Issue Draft A (2023-12-15)**

Initial release.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. iii

LUNA2000-4.5MWH-2H1 Smart String ESS
# User Manual Contents Contents

**About This Document .................................................................................................................... ii**

**1 Safety Information ........................................................................................................................ 1**

1.1 Personal Safety ............................................................................................................................................................. 2

1.2 Electrical Safety ............................................................................................................................................................ 4

1.3 Environment Requirements .......................................................................................................................................... 7

1.4 Mechanical Safety ........................................................................................................................................................ 9

1.5 Equipment Safety ........................................................................................................................................................ 14

1.5.1 ESS Safety ............................................................................................................................................................... 14

1.5.2 Battery Safety .......................................................................................................................................................... 15

**2 Overview ....................................................................................................................................... 21**

2.1 Model Description ...................................................................................................................................................... 21

2.2 Appearance ................................................................................................................................................................. 21

**3 Transportation and Storage ....................................................................................................... 23**

3.1 Transportation Requirements ...................................................................................................................................... 23

3.2 Storage Requirements ................................................................................................................................................. 26

**4 Site Requirements ....................................................................................................................... 29**

4.1 Site Selection Requirements ....................................................................................................................................... 29

4.2 Clearance Requirements ............................................................................................................................................. 31

4.3 Foundation Requirements ........................................................................................................................................... 32

**5 Installing ESS............................................................................................................................... 34**

5.1 Installation Preparations ............................................................................................................................................. 34

5.1.1 Preparing Tools ........................................................................................................................................................ 34

5.1.2 Installation Environment Check .............................................................................................................................. 36

5.2 Unpacking and Acceptance ......................................................................................................................................... 36

5.3 Determining the Installation Position of the ESS ....................................................................................................... 37

5.4 Securing the ESS ........................................................................................................................................................ 38

**6 Installing Cables ......................................................................................................................... 41**

**7 Power-On and Commissioning ................................................................................................ 46**

7.1 Prerequisites ................................................................................................................................................................ 46

7.1.1 Checking Before Power-On ..................................................................................................................................... 46

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. iv

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual Contents

7.1.2 Fire Suppression System Test .................................................................................................................................. 47

7.2 Device Power-On ........................................................................................................................................................ 48

7.3 Deployment and Commissioning ................................................................................................................................ 49

**8 Maintenance ................................................................................................................................. 51**

8.1 Routine Maintenance .................................................................................................................................................. 51

8.1.1 Unscheduled Maintenance ....................................................................................................................................... 51

8.1.2 Quarterly Maintenance ............................................................................................................................................ 51

8.1.3 Semi-annual Maintenance ........................................................................................................................................ 52

8.1.4 Annual Maintenance ................................................................................................................................................ 53

8.2 Troubleshooting .......................................................................................................................................................... 55

8.2.1 CMU Alarms ............................................................................................................................................................ 55

8.2.2 ESC and BCU Alarms.............................................................................................................................................. 56

8.2.3 BMU Alarms ............................................................................................................................................................ 56

**9 Emergency Handling .................................................................................................................. 58**

**10 Technical Specifications .......................................................................................................... 60**

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. v

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

# 1 Safet Information

**y**

**Statement**

**Before transporting, storing, installing, operating, using, and/or maintaining the**
**equipment, read this document, strictly follow the instructions provided herein, and**
**follow all the safety instructions on the equipment and in this document.** In this document,
"equipment" refers to the products, software, components, spare parts, and/or services related
to this document; "the Company" refers to the manufacturer (producer), seller, and/or service
provider of the equipment; "you" refers to the entity that transports, stores, installs, operates,
uses, and/or maintains the equipment.

The **Danger**, **Warning**, **Caution**, and **Notice** statements described in this document do not
cover all the safety precautions. You also need to comply with relevant international, national,
or regional standards and industry practices. **The Company shall not be liable for any**
**consequences that may arise due to violations of safety requirements or safety standards**
**concerning the design, production, and usage of the equipment.**

The equipment shall be used in an environment that meets the design specifications.
Otherwise, the equipment may be faulty, malfunctioning, or damaged, which is not covered
under the warranty. The Company shall not be liable for any property loss, personal injury, or
even death caused thereby.

Comply with applicable laws, regulations, standards, and specifications during transportation,
storage, installation, operation, use, and maintenance.

Do not perform reverse engineering, decompilation, disassembly, adaptation, implantation, or
other derivative operations on the equipment software. Do not study the internal
implementation logic of the equipment, obtain the source code of the equipment software,
violate intellectual property rights, or disclose any of the performance test results of the
equipment software.

**The Company shall not be liable for any of the following circumstances or their**

**consequences:**

 The equipment is damaged due to force majeure such as earthquakes, floods, volcanic
eruptions, debris flows, lightning strikes, fires, wars, armed conflicts, typhoons,
hurricanes, tornadoes, and other extreme weather conditions.

 The equipment is operated beyond the conditions specified in this document.

 The equipment is installed or used in environments that do not comply with international,
national, or regional standards.

 The equipment is installed or used by unqualified personnel.

Issue Draft B

(2024-01-23)

# Copyright © Huawei Digital Power Technologies Co., Ltd. 1

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

 You fail to follow the operation instructions and safety precautions on the product and in
the document.

 You remove or modify the product or modify the software code without authorization.

 You or a third party authorized by you cause the equipment damage during
transportation.

 The equipment is damaged due to storage conditions that do not meet the requirements
specified in the product document.

 You fail to prepare materials and tools that comply with local laws, regulations, and
related standards.

 The equipment is damaged due to your or a third party's negligence, intentional breach,
gross negligence, or improper operations, or other reasons not related to the Company.

**1.1 Personal Safety**

Ensure that power is off during installation. Do not install or remove a cable with power on.
Transient contact between the core of the cable and the conductor will cause electric arcs,
sparks, fire, or explosion, which may result in personal injury.

Non-standard and improper operations on the energized equipment may cause fire, electric
shocks, or explosion, resulting in property damage, personal injury, or even death.

Before operations, remove conductive objects such as watches, bracelets, bangles, rings, and
necklaces to prevent electric shocks.

During operations, use dedicated insulated tools to prevent electric shocks or short circuits.
The dielectric withstanding voltage level must comply with local laws, regulations, standards,
and specifications.

During operations, wear personal protective equipment such as protective clothing, insulated
shoes, goggles, safety helmets, and insulated gloves.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 2

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

**Figure 1-1** Personal protective equipment

**General Requirements**

 Do not stop protective devices. Pay attention to the warnings, cautions, and related
precautionary measures in this document and on the equipment.

 If there is a likelihood of personal injury or equipment damage during operations,
immediately stop, report the case to the supervisor, and take feasible protective

measures.

 Do not power on the equipment before it is installed or confirmed by professionals.

 Do not touch the power supply equipment directly or with conductors such as damp
objects. Before touching any conductor surface or terminal, measure the voltage at the
contact point to ensure that there is no risk of electric shock.

 Do not touch operating equipment because the enclosure is hot.

 Do not touch a running fan with your hands, components, screws, tools, or boards.
Otherwise, personal injury or equipment damage may occur.

 In the case of a fire, immediately leave the building or the equipment area and activate
the fire alarm or call emergency services. Do not enter the affected building or
equipment area under any circumstances.

**Personnel Requirements**

 Only professionals and trained personnel are allowed to operate the equipment.

−
Professionals: personnel who are familiar with the working principles and structure
of the equipment, trained or experienced in equipment operations and are clear of
the sources and degree of various potential hazards in equipment installation,
operation, maintenance

−
Trained personnel: personnel who are trained in technology and safety, have
required experience, are aware of possible hazards on themselves in certain
operations, and are able to take protective measures to minimize the hazards on
themselves and other people

 Personnel who plan to install or maintain the equipment must receive adequate training,
be able to correctly perform all operations, and understand all necessary safety
precautions and local relevant standards.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 3

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

 Only qualified professionals or trained personnel are allowed to install, operate, and
maintain the equipment.

 Only qualified professionals are allowed to remove safety facilities and inspect the
equipment.

 Personnel who will perform special tasks such as electrical operations, working at
heights, and operations of special equipment must possess the required local
qualifications.

 Only authorized professionals are allowed to replace the equipment or components
(including software).

 Only personnel who need to work on the equipment are allowed to access the equipment.

**1.2 Electrical Safety**

Before connecting cables, ensure that the equipment is intact. Otherwise, electric shocks or
fire may occur.

Non-standard and improper operations may result in fire or electric shocks.

Prevent foreign matter from entering the equipment during operations. Otherwise, equipment
damage, load power derating, power failure, or personal injury may occur.

For the equipment that needs to be grounded, install the ground cable first when installing the
equipment and remove the ground cable last when removing the equipment.

Do not route cables near the air intake or exhaust vents of the equipment.

**General Requirements**

 Follow the procedures described in the document for installation, operation, and
maintenance. Do not reconstruct or alter the equipment, add components, or change the
installation sequence without permission.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 4

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

 Obtain approval from the national or local electric utility company before connecting the
equipment to the grid.

 Observe the power plant safety regulations, such as the operation and work ticket
mechanisms.

 Install temporary fences or warning ropes and hang "No Entry" signs around the
operation area to keep unauthorized personnel away from the area.

 Before installing or removing power cables, turn off the switches of the equipment and
its upstream and downstream switches.

 If any liquid is detected inside the equipment, disconnect the power supply immediately
and do not use the equipment.

 Before performing operations on the equipment, check that all tools meet the
requirements and record the tools. After the operations are complete, collect all of the
tools to prevent them from being left inside the equipment.

 Before installing power cables, check that cable labels are correct and cable terminals are
insulated.

 When installing the equipment, use a torque tool of a proper measurement range to
tighten the screws. When using a wrench to tighten the screws, ensure that the wrench
does not tilt and the torque error does not exceed 10% of the specified value.

 Ensure that bolts are tightened with a torque tool and marked in red and blue after
double-check. Installation personnel mark tightened bolts in blue. Quality inspection
personnel confirm that the bolts are tightened and then mark them in red. (The marks
must cross the edges of the bolts.)

 After the installation is complete, ensure that protective cases, insulation tubes, and other
necessary items for all electrical components are in position to avoid electric shocks.

 If the equipment has multiple inputs, disconnect all the inputs before operating the
equipment.

 Before maintaining a downstream electrical or power distribution device, turn off the
output switch on the power supply equipment.

 During equipment maintenance, attach "Do not switch on" labels near the upstream and
downstream switches or circuit breakers as well as warning signs to prevent accidental
connection. The equipment can be powered on only after troubleshooting is complete.

 If fault diagnosis and troubleshooting need to be performed after power-off, take the
following safety measures: Disconnect the power supply. Check whether the equipment
is live. Install a ground cable. Hang warning signs and set up fences.

 Check equipment connections periodically, ensuring that all screws are securely
tightened.

 Only qualified professionals can replace a damaged cable.

 Do not scrawl, damage, or block any labels or nameplates on the equipment. Promptly
replace labels that have worn out.

 Do not use solvents such as water, alcohol, or oil to clean electrical components inside or
outside of the equipment.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 5

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

**Grounding**

 Ensure that the grounding impedance of the equipment complies with local electrical
standards.

 Ensure that the equipment is connected permanently to the protective ground. Before
operating the equipment, check its electrical connection to ensure that it is reliably
grounded.

 Do not work on the equipment in the absence of a properly installed ground conductor.

 Do not damage the ground conductor.

 For the equipment that uses a three-pin socket, ensure that the ground terminal in the
socket is connected to the protective ground point.

 If high touch current may occur on the equipment, ground the protective ground terminal
on the equipment enclosure before connecting the power supply; otherwise, electric
shock as a result of touch current may occur.

**Cabling Requirements**

 When selecting, installing, and routing cables, follow local safety regulations and rules.

 When routing power cables, ensure that there is no coiling or twisting. Do not join or
weld power cables. If necessary, use a longer cable.

 Ensure that all cables are properly connected and insulated, and meet specifications.

 Ensure that the slots and holes for routing cables are free from sharp edges, and that the
positions where cables are routed through pipes or cable holes are equipped with cushion
materials to prevent the cables from being damaged by sharp edges or burrs.

 If a cable is routed into the cabinet from the top, bend the cable in a U shape outside the
cabinet and then route it into the cabinet.

 Ensure that cables of the same type are bound together neatly and straight and that the
cable sheath is intact. When routing cables of different types, ensure that they are at least
30 mm away from each other.

 When cable connection is completed or paused for a short period of time, seal the cable
holes with sealing putty immediately to prevent small animals or moisture from entering.

 Secure buried cables using cable supports and cable clips. Ensure that the cables in the
backfill area are in close contact with the ground to prevent cable deformation or damage
during backfilling.

 If the external conditions (such as the cable layout or ambient temperature) change,
verify the cable usage in accordance with the IEC-60364-5-52 or local laws and
regulations. For example, check that the current-carrying capacity meets requirements.

 When routing cables, reserve at least 30 mm clearance between the cables and
heat-generating components or areas. This prevents deterioration or damage to the cable
insulation layer.

 When the temperature is low, violent impact or vibration may damage the plastic cable
sheathing. To ensure safety, comply with the following requirements:

−
Cables can be laid or installed only when the temperature is higher than 0°C.
Handle cables with caution, especially at a low temperature.

−
Cables stored at below 0°C must be stored at room temperature for more than 24
hours before they are laid out.

 Do not perform any improper operations, for example, dropping cables directly from a
vehicle. Otherwise, the cable performance may deteriorate due to cable damage, which
affects the current-carrying capacity and temperature rise.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 6

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

**ESD**

The static electricity generated by human bodies may damage the electrostatic-sensitive
components on boards, for example, the large-scale integrated (LSI) circuits.

 When touching the equipment and handling boards, modules with exposed circuit boards,
or application-specific integrated circuits (ASICs), observe ESD protection regulations
and wear ESD clothing and ESD gloves or a well-grounded ESD wrist strap.

**Figure 1-2** Wearing an ESD wrist strap

 When holding a board or a module with exposed circuit boards, hold its edge without
touching any components. Do not touch the components with bare hands.

 Package boards or modules with ESD packaging materials before storing or transporting
them.

**1.3 Environment Requirements**

Do not expose the equipment to flammable or explosive gas or smoke. Do not perform any
operation on the equipment in such environments.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 7

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

Do not store any flammable or explosive materials in the equipment area.

Do not place the equipment near heat sources or fire sources, such as smoke, candles, heaters,
or other heating devices. Overheat may damage the equipment or cause a fire.

Install the equipment in an area far away from liquids. Do not install it under areas prone to
condensation, such as under water pipes and air exhaust vents, or areas prone to water leakage,
such as air conditioner vents, ventilation vents, or feeder windows of the equipment room.
Ensure that no liquid enters the equipment to prevent faults or short circuits.

To prevent damage or fire due to high temperature, ensure that the ventilation vents or heat
dissipation systems are not obstructed or covered by other objects while the equipment is
running.

**General Requirements**

 Ensure that the equipment is stored in a clean, dry, and well ventilated area with proper
temperature and humidity and is protected from dust and condensation.

 Keep the installation and operating environments of the equipment within the allowed
ranges. Otherwise, its performance and safety will be compromised.

 Do not install, use, or operate outdoor equipment and cables (including but not limited to
moving equipment, operating equipment and cables, inserting connectors to or removing
connectors from signal ports connected to outdoor facilities, working at heights,
performing outdoor installation, and opening doors) in harsh weather conditions such as
lightning, rain, snow, sandstorm, and level 6 or stronger wind.

 Do not install the equipment in an environment with dust, smoke, volatile or corrosive
gases, infrared and other radiations, organic solvents, or salty air.

 Do not install the equipment in an environment with conductive metal or magnetic dust.

 Do not install the equipment in an area conducive to the growth of microorganisms such
as fungus or mildew.

 Do not install the equipment in an area with strong vibration, noise, or electromagnetic
interference.

 Ensure that the site complies with local laws, regulations, and related standards.

 Ensure that the ground in the installation environment is solid, free from spongy or soft
soil, and not prone to subsidence. The site must not be located in a low-lying land prone
to water or snow accumulation, and the horizontal level of the site must be above the
highest water level of that area in history.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 8

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

 Do not install the equipment in a position that may be submerged in water.

 If the equipment is installed in a place with abundant vegetation, in addition to routine
weeding, harden the ground underneath the equipment using cement or gravel.

 Before opening doors during the installation, operation, and maintenance of the
equipment, clean up any water, ice, snow, or other foreign objects on the top of the
equipment to prevent foreign objects from falling into the equipment.

 When installing the equipment, ensure that the installation surface is solid enough to bear
the weight of the equipment.

 All cable holes must be sealed. Seal the used cable holes with sealing putty. Seal the
unused cable holes with the caps delivered with the equipment. The following figure
shows the criteria for correct sealing with sealing putty.

 After installing the equipment, remove the packing materials such as cartons, foam,
plastics, and cable ties from the equipment area.

**1.4 Mechanical Safety**

When working at heights, wear a safety helmet and safety harness or waist belt and fasten it to
a solid structure. Do not mount it on an insecure moveable object or metal object with sharp
edges. Make sure that the hooks will not slide off.

Ensure that all necessary tools are ready and inspected by a professional organization. Do not
use tools that have signs of scratches or fail to pass the inspection or whose inspection validity
period has expired. Ensure that the tools are secure and not overloaded.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 9

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

Before installing equipment in a cabinet, ensure that the cabinet is securely fastened with a
balanced center of gravity. Otherwise, tipping or falling cabinets may cause bodily injury and
equipment damage.

When pulling equipment out of a cabinet, be aware of unstable or heavy objects in the cabinet
to prevent injury.

Do not drill holes into the equipment. Doing so may affect the sealing performance and
electromagnetic containment of the equipment and damage components or cables inside.
Metal shavings from drilling may short-circuit boards inside the equipment.

**General Requirements**

 Repaint any paint scratches caused during equipment transportation or installation in a
timely manner. Equipment with scratches must not be exposed for an extended period of
time.

 Do not perform operations such as arc welding and cutting on the equipment without
evaluation by the Company.

 Do not install other devices on the top of the equipment without evaluation by the
Company.

 When performing operations over the top of the equipment, take measures to protect the
equipment against damage.

 Use correct tools and operate them in the correct way.

**Moving Heavy Objects**

 Be cautious to prevent injury when moving heavy objects.

 If multiple persons need to move a heavy object together, determine the manpower and
work division with consideration of height and other conditions to ensure that the weight
is equally distributed.

 If two persons or more move a heavy object together, ensure that the object is lifted and
landed simultaneously and moved at a uniform pace under the supervision of one person.

 Wear personal protective gears such as protective gloves and shoes when manually
moving the equipment.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 10

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

 To move an object by hand, approach to the object, squat down, and then lift the object
gently and stably by the force of the legs instead of your back. Do not lift it suddenly or
turn your body around.

 Move or lift the equipment by holding its handles or lower edges. Do not hold the
handles of modules that are installed in the equipment.

 Do not quickly lift a heavy object above your waist. Place the object on a workbench that
is half-waist high or any other appropriate place, adjust the positions of your palms, and
then lift it.

 Move a heavy object stably with balanced force at an even and low speed. Put down the
object stably and slowly to prevent any collision or drop from scratching the surface of
the equipment or damaging the components and cables.

 When moving a heavy object, be aware of the workbench, slope, staircase, and slippery
places. When moving a heavy object through a door, ensure that the door is wide enough
to move the object and avoid bumping or injury.

 When transferring a heavy object, move your feet instead of turning your waist around.
When lifting and transferring a heavy object, ensure that your feet point to the target
direction of movement.

 When transporting the equipment using a pallet truck or forklift, ensure that the tynes are
properly positioned so that the equipment does not topple. Before moving the equipment,
secure it to the pallet truck or forklift using ropes. When moving the equipment, assign
dedicated personnel to take care of it.

 Choose sea or roads in good conditions for transportation. Do not transport the
equipment by railway or air. Avoid tilt or jolt during transportation.

 The tilt angle of the ESS shall meet the requirements shown in the figure: α ≤ 5°.

 When moving and transporting an air conditioner, keep it upright and do not place it
horizontally or upside down. If the package of the air conditioner is damaged or the tilt
indicator on the package changes color, contact the Company's service engineers.

**Working at Heights**

 Any operations performed 2 m or higher above the ground shall be supervised properly.

 Only trained and qualified personnel are allowed to work at heights.

 Do not work at heights when steel pipes are wet or other risky situations exist. After the
preceding conditions no longer exist, the safety owner and relevant technical personnel
need to check the involved equipment. Operators can begin working only after safety is
confirmed.

 Set a restricted area and prominent signs for working at heights to warn away irrelevant
personnel.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 11

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

 Set guard rails and warning signs at the edges and openings of the area involving
working at heights to prevent falls.

 Do not pile up scaffolding, springboards, or other objects on the ground under the area
involving working at heights. Do not allow people to stay or pass under the area
involving working at heights.

 Carry operation machines and tools properly to prevent equipment damage or personal
injury caused by falling objects.

 Personnel involving working at heights are not allowed to throw objects from the height
to the ground, or vice versa. Objects shall be transported by slings, hanging baskets,
aerial work platforms, or cranes.

 Do not perform operations on the upper and lower layers at the same time. If
unavoidable, install a dedicated protective shelter between the upper and lower layers or
take other protective measures. Do not pile up tools or materials on the upper layer.

 Dismantle the scaffolding from top down after finishing the job. Do not dismantle the
upper and lower layers at the same time. When removing a part, ensure that other parts
will not collapse.

 Ensure that personnel working at heights strictly comply with the safety regulations. The
Company is not responsible for any accident caused by violation of the safety regulations
on working at heights.

 Behave cautiously when working at heights. Do not rest at heights.

**Using Ladders**

 Use wooden or insulated ladders when you need to perform live-line working at heights.

 Platform ladders with protective rails are preferred. Do not use single ladders.

 Before using a ladder, check that it is intact and confirm its load bearing capacity. Do not
overload it.

 Ensure that the ladder is securely positioned and held firm.

 When climbing up the ladder, keep your body stable and your center of gravity between
the side rails, and do not overreach to the sides.

 When a step ladder is used, ensure that the pull ropes are secured.

**Hoisting**

 Only trained and qualified personnel are allowed to perform hoisting operations.

 Install temporary warning signs or fences to isolate the hoisting area.

 Ensure that the foundation where hoisting is performed on meets the load-bearing
requirements.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 12

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

 Before hoisting objects, ensure that hoisting tools are firmly secured onto a fixed object
or wall that meets the load-bearing requirements.

 During hoisting, do not stand or walk under the crane or the hoisted objects.

 Do not drag steel ropes and hoisting tools or bump the hoisted objects against hard
objects during hoisting.

 Ensure that the angle between two hoisting ropes is no more than 90 degrees, as shown
in the following figure.

**Drilling Holes**

 Obtain consent from the customer and contractor before drilling holes.

 Wear protective equipment such as safety goggles and protective gloves when drilling
holes.

 To avoid short circuits or other risks, do not drill holes into buried pipes or cables.

 When drilling holes, protect the equipment from shavings. After drilling, clean up any
shavings.

**Welding**

 A welder must have a work permit. Obtain consent from the customer before welding.

 Ensure that at least two persons are present onsite for welding and that fire extinguishers,
wet cloth, and water containers are available.

 Ensure that the welding site is free from inflammables.

 Do not weld or cut on pressurized containers or pipes. Electric devices must be powered
off before welding.

 A burning welding torch must not be placed on a component or on the floor, and must
not be placed in a metal container with acetylene and oxygen. Otherwise, the gas may
leak and cause a fire.

 High-temperature pipes after welding must be promptly cooled.

**Using a Jack**

 A hydraulic jack is used to lift the container. Load bearing requirement: 41 t

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 13

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

 Only one side of the equipment can be raised or lowered. Before applying force, place
wood sleepers and pads and take measures to prevent the jack from slipping and the
equipment from vibrating.

 You can use two jacks to apply even forces simultaneously at two points on a short side
of the equipment. Lift the equipment only from one side and then the other side,
alternately. The height shall not exceed 120 mm each time the equipment is lifted.

**1.5 Equipment Safety**

**1.5.1 ESS Safety**

Do not open battery cabin doors when the system is running.

If the ESS is faulty, do not stand within the opening range of the battery cabin doors.

The equipment is equipped with a fire suppression system. Start the fire suppression system
only in emergency.

Do not disable the protection devices.

Evacuate from the site immediately once the fire alarm horn/strobe is triggered.

Take protection and isolation measures for the ESS, such as installing fences, walls, and
safety warning signs to prevent personal injury or property damage caused by unauthorized
access during operations.

 When installing the ESS, comply with the fire separation distance or fire wall
requirements specified in local standards, including but not limited to _GB 51048-2014_

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 14

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

_Design Code for Electrochemical Energy Storage Station_ and _NFPA 855 Standard for the_
_Installation of Stationary Energy Storage Systems_ .

 Check the fire safety of the ESS regularly, at least once a month.

 When inspecting the system with power on, pay attention to the hazard warning signs on
the equipment. Do not stand at the battery cabin doors. You are advised to perform the
inspection near the control unit cabin.

 After power components of the ESS are replaced or cable connections are changed, you
need to manually start cable connection detection and topology identification to prevent
system malfunction.

 After the equipment is powered off, wait for 15 minutes and ensure that the equipment is
not energized before operations.

 It is recommended that you prepare a camera to record the detailed processes of
equipment installation, operation, and maintenance.

**1.5.2 Battery Safety**

Do not connect the positive and negative poles of a battery together. Otherwise, the battery
may be short-circuited. Battery short circuits can generate high instantaneous current and
releases a large amount of energy, which may cause battery leakage, smoke, flammable gas
release, thermal runaway, fire, or explosion. To avoid battery short circuits, do not maintain
batteries with power on.

Do not expose batteries at high temperatures or around heat sources, such as scorching
sunlight, fire sources, transformers, and heaters. Battery overheating may cause leakage,
smoke, flammable gas release, thermal runaway, fire, or explosion.

Protect batteries from mechanical vibration, falling, collision, punctures, and strong impact.
Otherwise, the batteries may be damaged or catch fire.

To avoid leakage, smoke, flammable gas release, thermal runaway, fire, or explosion, do not
disassemble, alter, or damage batteries, for example, insert foreign objects into batteries,
squeeze batteries, or immerse batteries in water or other liquids.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 15

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

Do not touch battery terminals with other metal objects, which may cause heat or electrolyte
leakage.

There is a risk of fire or explosion if the model of the battery in use or used for replacement is
incorrect. Use a battery of the model recommended by the manufacturer.

Battery electrolyte is toxic and volatile. Do not get contact with leaked liquids or inhale gases
in the case of battery leakage or odor. In such cases, stay away from the battery and contact
professionals immediately. Professionals must wear safety goggles, rubber gloves, gas masks,
and protective clothing, power off the equipment, remove the battery, and contact technical
engineers.

A battery is an enclosed system and will not release any gases under normal operations. If a
battery is improperly treated, for example, burnt, needle-pricked, squeezed, struck by
lightning, overcharged, or subject to other adverse conditions that may cause battery thermal
runaway, the battery may be damaged or an abnormal chemical reaction may occur inside the
battery, resulting in electrolyte leakage or production of gases such as CO and H 2 . To prevent
fire or device corrosion, ensure that flammable gas is properly exhausted.

The gas generated by a burning battery may irritate your eyes, skin, and throat. Take
protective measures promptly.

Install batteries in a dry area. Do not install them under areas prone to water leakage, such as
air conditioner vents, ventilation vents, feeder windows of the equipment room, or water pipes.
Ensure that no liquid enters the equipment to prevent faults or short circuits.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 16

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

Before installing and commissioning batteries, prepare fire fighting facilities, such as fire sand
and carbon dioxide fire extinguishers, according to construction standards and regulations.
Before putting into operation, ensure that fire fighting facilities that comply with local laws
and regulations are installed.

Before unpacking, storage, and transportation, ensure that the packing cases are intact and the
batteries are correctly placed according to the labels on the packing cases. Do not place a
battery upside down or vertically, lay it on one side, or tilt it. Stack the batteries according to
the stacking requirements on the packing cases. Ensure that the batteries do not fall or get
damaged. Otherwise, they will need to be scrapped.

After unpacking batteries, place them in the required direction. Do not place a battery upside
down or vertically, lay it on one side, tilt it, or stack it. Ensure that the batteries do not fall or
get damaged. Otherwise, they will need to be scrapped.

Tighten the screws on copper bars or cables to the torque specified in this document.
Periodically confirm whether the screws are tightened, check for rust, corrosion, or other
foreign objects, and clean them up if any. Loose screw connections will result in excessive
voltage drops and batteries may catch fire when the current is high.

After batteries are discharged, charge them in time to avoid damage due to overdischarge.

**Statement**

**The Company shall not be liable for any damage or other consequences to the batteries**
**it provides due to the following reasons:**

 Batteries are damaged due to force majeure such as earthquakes, floods, volcanic
eruptions, debris flows, lightning strikes, fires, wars, armed conflicts, typhoons,
hurricanes, tornadoes, and other extreme weather conditions.

 Batteries are damaged because the onsite equipment operating environment or external
power parameters do not meet the environment requirements for normal operation, for
example, the actual operating temperature of batteries is too high or too low, or the
power grid is unstable and experiences outages frequently.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 17

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

 Batteries are damaged, fall, leak, or crack due to improper operations or incorrect
connection.

 After being installed and connected to the system, the batteries are not powered on in
time due to your reasons, which causes damage to the batteries due to overdischarge.

 Batteries are damaged because they are not accepted in time due to your reasons.

 You set battery operating parameters incorrectly.

 You use batteries of different types together, causing acceleration of capacity attenuation.
For example, you use our batteries together with batteries of other vendors or with
batteries of different rated capacity.

 You maintain batteries improperly, causing frequent overdischarge; you expand the load
capacity without notifying us; or you have not fully charged the batteries for a long time.

 You do not perform battery maintenance based on the operation guide, such as failure to
check battery terminals regularly.

 Batteries are damaged because you do not store them in accordance with storage
requirements (for example, in an environment that is damp or prone to rain).

 Batteries are not charged as required during storage due to your reasons, resulting in
capacity loss or other irreversible damages to the batteries.

 Batteries are damaged due to your or a third party's reasons, for example, relocating or
reinstalling the batteries without complying with the Company's requirements.

 You change the battery use scenarios without notifying the Company.

 You connect extra loads to the batteries.

 The battery storage period has exceeded the upper limit.

 The battery warranty period has expired. You are advised not to use a battery whose
warranty period has expired, as this poses safety risks.

**General Requirements**

To ensure battery safety and battery management accuracy, use batteries provided by the
Company. The Company is not responsible for any faults of batteries not provided by it.

 Before installing, operating, and maintaining batteries, read the battery manufacturer's
instructions and comply with their requirements. The safety precautions specified in this
document are highly important and require special attention. For additional safety
precautions, see the instructions provided by the battery manufacturer.

 Use batteries within the specified temperature range. When the ambient temperature of
the batteries is lower than the allowed range, do not charge the batteries to prevent
internal short circuits caused during low-temperature charging.

 Before unpacking batteries, check whether the packaging is intact. Do not use batteries
with damaged packaging. If any damage is found, notify the carrier and manufacturer
immediately.

 Install batteries within 24 hours after unpacking. If the batteries cannot be installed in
time, put them in the original packaging and place them in a dry indoor environment
without corrosive gases. The process from unpacking batteries to powering on the
system must be completed within 72 hours. During routine maintenance, ensure that the
power-off time does not exceed 24 hours.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 18

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

 Do not use a damaged battery (such as damage caused when a battery is dropped,
bumped, bulged, or dented on the enclosure), because the damage may cause electrolyte
leakage or flammable gas release. In the case of electrolyte leakage or structural
deformation, contact the installer or professional O&M personnel immediately to remove
or replace the battery. Do not store the damaged battery near other devices or flammable
materials and keep it away from non-professionals.

 Before working on a battery, ensure that there is no irritant or scorched smell around the
battery.

 When installing batteries, do not place installation tools, metal parts, or sundries on the
batteries. After the installation is complete, clean up the objects on the batteries and the
surrounding area.

 Do not install battery packs on rainy, snowy, or foggy days. Otherwise, the battery packs
may be corroded by moisture or rain.

 If batteries are exposed to water accidentally, do not install them. Instead, transport the
batteries to a safe isolation point and dispose of them in a timely manner.

 Before installing a battery pack, check that its enclosure is not deformed or damaged.

 Check whether the positive and negative battery terminals are grounded unexpectedly. If
so, disconnect the battery terminals from the ground.

 Do not perform welding or grinding work around batteries to prevent fire caused by
electric sparks or arcs.

 If batteries are left unused for a long period of time, store and charge them according to
the battery requirements.

 Do not charge or discharge batteries by using a device that does not comply with local
laws and regulations.

 Keep the battery loop disconnected during installation and maintenance.

 Monitor damaged batteries during storage for signs of smoke, flame, electrolyte leakage,
or heat.

 If a battery is faulty, its surface temperature may be high. Do not touch the battery to
avoid scalds.

 Do not stand on, lean on, or sit on the top of the equipment.

 In backup power scenarios, do not use the batteries for the following situations:

−
Medical devices substantially important to human life

−
Control equipment such as trains and elevators, as this may cause personal injury

−
Computer systems of social and public importance

− Locations near medical devices

− Other devices similar to those described above

**Short-Circuit Protection**

 When installing and maintaining batteries, wrap the exposed cable terminals on the
batteries with insulation tape.

 Avoid foreign objects (such as conductive objects, screws, and liquids) from entering a
battery, as this may cause short circuits.

**Leakage Handling**

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 19

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 1 Safety Information

Electrolyte leakage may damage the equipment. It will corrode metal parts and boards, and
ultimately damage the boards.

Electrolyte is corrosive and can cause irritation and chemical burns. If you come into direct
contact with the battery electrolyte, do as follows:

 Inhalation: Evacuate from contaminated areas, get fresh air immediately, and seek
immediate medical attention.

 Eye contact: Immediately wash your eyes with water for at least 15 minutes, do not rub
your eyes, and seek immediate medical attention.

 Skin contact: Wash the affected areas immediately with soap and water and seek
immediate medical attention.

 Intake: Seek immediate medical attention.

**Recycling**

 Dispose of waste batteries in accordance with local laws and regulations. Do not dispose
of batteries as household waste. Improper disposal of batteries may result in
environmental pollution or an explosion.

 If a battery leaks or is damaged, contact technical support or a battery recycling company
for disposal.

 If batteries are out of service life, contact a battery recycling company for disposal.

 Do not expose waste batteries to high temperatures or direct sunlight.

 Do not place waste batteries in environments with high humidity or corrosive substances.

 Do not use faulty batteries. Contact a battery recycling company to scrap them as soon as
possible to avoid environmental pollution.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 20

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 2 Overview

# 2 Overview

**2.1 Model Description**

**Figure 2-1** Model number

**Table 2-1** Model number description

<!-- INICIO TABLA 2-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **2.1 Model Description** **Figure 2-1** Model number -->

**Tabla 2-1: ** Model number description**

| No. | Meaning | Description |
| --- | --- | --- |
| 1 | Product family | LUNA2000: Smart String ESS |
| 2 | Capacity level | 4.5MWH: nominal capacity[1] |
| 3 | Backup power | 2H1: Applies to scenarios where the backup<br>duration is greater than or equal to 2 hours |
| Note [1]: The nominal capacity is on the nameplate. | Note [1]: The nominal capacity is on the nameplate. | Note [1]: The nominal capacity is on the nameplate. |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **2.2 Appearance** FusionSolar Smart String ESS adopts a modular design and consists of the battery cabin, the liquid-cooled unit cabin, and the control unit cabin. -->
<!-- FIN TABLA 2-1 -->


|No.|Meaning|Description|
|---|---|---|
|1|Product family|LUNA2000: Smart String ESS|
|2|Capacity level|4.5MWH: nominal capacity[1]|
|3|Backup power|2H1: Applies to scenarios where the backup<br>duration is greater than or equal to 2 hours|
|Note [1]: The nominal capacity is on the nameplate.|Note [1]: The nominal capacity is on the nameplate.|Note [1]: The nominal capacity is on the nameplate.|

**2.2 Appearance**

FusionSolar Smart String ESS adopts a modular design and consists of the battery cabin, the
liquid-cooled unit cabin, and the control unit cabin.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 21

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 2 Overview

**Figure 2-2** LUNA2000-4.5MWH-2H1 appearance

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 22

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 3 Transportation and Storage

# 3 Trans ortation and Stora e

**p** **g**

**3.1 Transportation Requirements**

**General Requirements**

 Be cautious to prevent injury when moving heavy objects.

 If multiple persons need to move a heavy object together, determine the manpower and
work division with consideration of height and other conditions to ensure that the weight
is equally distributed.

 If two persons or more move a heavy object together, ensure that the object is lifted and
landed simultaneously and moved at a uniform pace under the supervision of one person.

 Wear personal protective gears such as protective gloves and shoes when manually
moving the equipment.

 To move an object by hand, approach to the object, squat down, and then lift the object
gently and stably by the force of the legs instead of your back. Do not lift it suddenly or
turn your body around.

 Move or lift the equipment by holding its handles or lower edges. Do not hold the
handles of modules that are installed in the equipment.

 Do not quickly lift a heavy object above your waist. Place the object on a workbench that
is half-waist high or any other appropriate place, adjust the positions of your palms, and
then lift it.

 Move a heavy object stably with balanced force at an even and low speed. Put down the
object stably and slowly to prevent any collision or drop from scratching the surface of
the equipment or damaging the components and cables.

 When moving a heavy object, be aware of the workbench, slope, staircase, and slippery
places. When moving a heavy object through a door, ensure that the door is wide enough
to move the object and avoid bumping or injury.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 23

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 3 Transportation and Storage

 When transferring a heavy object, move your feet instead of turning your waist around.
When lifting and transferring a heavy object, ensure that your feet point to the target
direction of movement.

 When transporting the equipment using a pallet truck or forklift, ensure that the tynes are
properly positioned so that the equipment does not topple. Before moving the equipment,
secure it to the pallet truck or forklift using ropes. When moving the equipment, assign
dedicated personnel to take care of it.

 The tilt angle of the ESS shall meet the requirements shown in the figure: α ≤ 5°.

 When moving and transporting an air conditioner, keep it upright and do not place it
horizontally or upside down. If the package of the air conditioner is damaged or the tilt
indicator on the package changes color, contact the Company's service engineers.

**Transportation Requirements**

Load or unload batteries with caution. Otherwise, the batteries may be short-circuited or
damaged (such as leakage and crack), catch fire, or explode.

Do not move a battery by holding its terminals, bolts, or cables. Otherwise, the battery may be
damaged.

Keep batteries in the correct direction during transportation. They must not be placed upside
down or tilted, and must be protected against falling down, mechanical impact, rains, snows,
and falling into water during transportation.

 Batteries have obtained the certifications of the UN38.3 (UN38.3: section 38.3 of the
sixth Revised Edition of the Recommendations on the Transport of Dangerous Goods,
Manual of Tests and Criteria) and SN/T 0370.2-2009 (Part 2: Performance Test of the
Rules for the Inspection of Packaging for Exporting Dangerous Goods). This product
belongs to class 9 dangerous goods.

 The transportation service provider must be qualified to transport dangerous goods. Open
truck transportation is not allowed.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 24

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 3 Transportation and Storage

 Comply with the international regulations on the transport of dangerous goods and meet
the requirements of the transportation regulatory authorities in the countries of departure,
route, and destination.

 Choose sea or roads in good conditions for transportation. Do not transport the
equipment by railway or air. Avoid tilt or jolt during transportation.

 Maritime transport must comply with the _International Maritime Dangerous Goods_
_Code_ (IMDG Code).

 Monitor the entire transportation process.

 Vehicles for road transport shall meet the load bearing capacity requirements: The weight
of a single ESS is about 41 t.

 The speed limit for road transport is 80 km/h on flat roads and 60 km/h on rough roads.
In the case of any conflict, comply with local traffic laws and regulations.

 Stacking requirements at ports and during shipping: A maximum of five ESSs shall be
permitted to be stacked.

 Road transport must comply with the _Agreement Concerning the International Carriage_
_of Dangerous Goods by Road_ (ADR) or JT/T 617.

 Before transportation, ensure that the ESS container is intact, the cabin doors are closed
and locked, no foreign matter protrudes from the container, and there is no smell of
smoke or burning. Otherwise, do not transport the ESS.

 Before transportation, check that the battery package is intact and that there is no
abnormal odor, leakage, smoke, or sign of burning. Otherwise, the batteries must not be
transported.

 Handle the ESS with care during loading, unloading, and transportation and
moisture-proof measures must be in place. The product specifications upon delivery may
be affected subsequently by the environment conditions, such as temperature,
transportation, and storage.

 The packing case must be secured for transportation. Handle the case with care during
loading and unloading, and take moisture-proof measures during transportation.

 Exercise caution when moving batteries to prevent bumping and ensure personal safety.

 Unless otherwise specified, dangerous goods must not be mixed with goods containing
food, medicine, animal feed, or their additives in the same vehicle or container.

 Unless otherwise specified, when dangerous goods packages are loaded in the same
vehicle or container as ordinary goods, they shall be separated in either of the following

ways:

−
Use a spacer that is as high as the packages.

−
Keep a distance of at least 0.8 m around.

 Before transporting a faulty battery (with scorch, leakage, bulge, or water intrusion),
insulate its positive and negative terminals, pack it, and place it in an insulated
explosion-proof box as soon as possible. Record information such as the site name,
address, time, and fault symptom on the box.

 When transporting faulty batteries, avoid approaching flammable material storage areas,
residential areas, or other densely populated places, such as mass transit facilities or
elevators.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 25

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 3 Transportation and Storage

**3.2 Storage Requirements**

**General Requirements**

 Proof that the product is stored according to the requirements must be available, such as
temperature and humidity log data, storage environment photos, and inspection reports.

 The storage environment must be clean and dry. The product must be protected against
rain and water.

 The air must not contain corrosive or flammable gases.

 Do not tilt the product or place it upside down.

 If equipment except battery packs has been stored for more than two years, it must be
checked and tested by professionals before use.

**ESS Storage Requirements**

 Do not stack the ESSs.

 The ground for (long-term or temporary) storage is level, and the height tolerance of the
ground in contact with the container is less than 5 mm.

 The container doors are closed tightly.

 Storage temperature: -40°C to +60°C; relative humidity: 5%-95% RH

 Place desiccant in control unit cabins and battery cabins for long-term storage.

 The main power loop of the ESS must be disconnected during storage. It is
recommended that the auxiliary power loop be powered on to ensure that the monitoring
system works properly.

**Battery Storage Requirements**

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 26

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 3 Transportation and Storage

 Ensure that batteries are stored in a dry, clean, and ventilated indoor environment that is
free from sources of strong infrared or other radiations, organic solvents, corrosive gases,
and conductive metal dust. Do not expose batteries to direct sunlight or rain and keep them
far away from sources of heat and ignition.

 If a battery is faulty (with scorch, leakage, bulge, or water intrusion), move it to a
dangerous goods warehouse for separate storage. The distance between the battery and any
combustible materials must be at least 3 m. The battery must be scrapped as soon as
possible.

 Place batteries correctly according to the signs on the packing case during storage. Do not
place batteries upside down, lay them on one side, or tilt them. Stack batteries in
accordance with the stacking requirements on the packing cases.

 Store batteries in a separate place. Do not store batteries together with other devices. Do
not stack batteries too high. The site must be equipped with qualified fire fighting facilities,
such as fire sand and fire extinguishers.

 After batteries are powered off, static power consumption and self-discharge loss may
occur in internal modules, which may cause battery damage due to overdischarge. Do not
store batteries in low SOC and charge batteries in a timely manner. Permanent battery
faults caused by delayed charge are not covered by the warranty. Storing the batteries in
low SOC occurs in scenarios including but not limited to the following:

 The power cables or signal cables are not connected.

 The batteries cannot be charged due to a system fault after discharge.

 The batteries cannot be charged due to incorrect configurations in the system.

 The batteries cannot be charged due to long-term mains failure.

 The batteries cannot be charged because the switch of the Smart Rack Controller, Smart
PCS, or main loop component is off.

It is recommended that batteries be used soon after being deployed onsite. Batteries that have
been stored for an extended period shall be charged periodically. Otherwise, they may be
damaged.

 The batteries in storage must be disconnected from external devices. The indicators (if
any) on the batteries must be off.

 The storage duration starts from the latest charge time labeled on the battery package. If
a battery is qualified after charge, update the latest charge time (recommended format:
YYYY-MM-DD HH:MM) and the next charge time (Next charge time = Latest charge
time + Charge interval) on the label.

 Do not unpack batteries. If charging is necessary, they must be charged by professionals
as required and then returned to their original packaging after charging.

 The warehouse keeper shall collect battery storage information every month and
periodically report the battery inventory information. The batteries in long-term storage
shall be charged in a timely manner.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 27

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 3 Transportation and Storage

 Only trained and qualified personnel are allowed to charge batteries. Wear insulated gloves
and use dedicated insulated tools during the operation.

 Observe onsite during charge and handle any exceptions in a timely manner.

 If a battery experiences an abnormality such as bulging or smoking during charge, stop
charging immediately and dispose of it.

 If batteries have been stored for longer than allowed, promptly report the event to the
person in charge.

 Ensure that batteries are delivered based on the "first in, first out" rule.

 Handle batteries with caution to avoid damage.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 28

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 4 Site Requirements

# 4 Site Re uirements

**q**

**4.1 Site Selection Requirements**

Refer to the GB 51048 _Design code for electrochemical energy storage station_, NFPA 855
_Standard for the Installation of Stationary Energy Storage Systems_, and local laws and
regulations.

The site selection requirements for the ESS are as follows:

 The ESS applies only to outdoor scenarios and must not be deployed indoors.

 The horizontal level of the installation site shall be above the highest water level of that
area in history and at least 300 mm above the ground. The site must not be located in a
low-lying land.

 No obstacle shall be above the ESS. For example, the ESS must not be installed under a
parking shed and PV modules must not be installed on the top of the ESS.

 For safety purposes, keep safety distances between the ESS and surrounding buildings
and facilities.

−
The distance between the ESS and residential buildings must be greater than or
equal to 12 m, and the distance between the ESS and densely populated buildings
such as schools and hospitals must be greater than 30.5 m.

−
The distance between the ESS and production buildings in commercial and
industrial scenarios must be greater than or equal to 12 m. If the distance does not
meet the requirement, fire walls shall be installed between the ESS and production
buildings. The fire walls shall have a 3-hour or higher fire resistance rating and
shall extend 1.5 m above and 1.5 m beyond the physical boundary of the ESS. In
addition, the clearance requirements for equipment transportation, installation, and
maintenance shall be considered.

 There must be no vegetation, especially flammable plants within 3 m of the ESS or the
site to protect the ESS from possible fires.

 It is recommended that outdoor open electrochemical energy storage plants be equipped
with fences and walls. The external walls of an electrochemical energy storage plant
deployed in a power plant or power transformation and distribution station shall be
permitted to serve as the enclosure and isolation walls.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 29

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 4 Site Requirements

 The safety distances between the ESS and buildings shall comply with local fire
protection regulations or standards.

 The ESS and the site must be in an environment free from explosion risks.

 Transportation to the site shall be convenient and fire suppression facilities shall be
reliable.

 When installing, commissioning, and operating the ESS, ensure that at least two gas fire
extinguishers are provided near each unit to ensure fire safety.

 The distance between the exhaust device of an ESS and the heating and ventilation vents, air intake
vents of air conditioners, windows, doors, unloading platforms, and fire sources of other buildings or
facilities must be greater than 4.6 m.

 Reserve sockets for the water fire suppression system at the ESS site.

 Outdoor fire hydrants shall be installed around the plant. The distance between fire hydrants shall be
less than or equal to 60 m. The number of outdoor fire hydrants shall be calculated based on the flow
rate and protection radius of fire hydrants. The maximum protection radius shall be less than or
equal to 150 m, and the flow rate shall be greater than or equal to 15 L/s.

 The site area must meet the requirements and there shall be space for capacity expansion.

 The site shall be in a well-ventilated place.

 The ESS shall not be installed in salt-affected or polluted areas because this will cause
corrosion. The ESS shall be used in the following or better environments:

−
Outdoor environment more than 2000 m away from the coast. You are advised not
to use the ESS in an area 500 m to 2000 m away from the coast. (If you need to use
it, confirm with the vendor or the Company's engineers.) Do not use the ESS in an
area less than 500 m away from the coast.

−
More than 1500-3000 m away from heavy pollution sources such as smelteries,
coal mines, and thermal power plants

−
More than 1000-2000 m away from medium pollution sources such as chemical,
rubber, and electroplating industries

−
More than 500-1000 m away from light pollution sources such as packing houses,
tanneries, boiler rooms, slaughterhouses, landfill sites, and sewage treatment plants

You are advised to select another site if the safety distance for a site cannot meet the requirements of
relevant national standards.

Do not select the sites that are not recommended by industry standards and regulations,
including but not limited to the following areas:

 Areas with sources of strong vibration, loud noises, and strong electromagnetic
interference

 Areas with dust, oil fumes, harmful gases, corrosive gases, etc.

 Areas with corrosive, flammable, and explosive materials

 Areas with existing underground facilities

 Areas with adverse geological conditions such as rubbery soil and soft soil layer, or
prone to waterlogging and land subsidence

 Under a reservoir, water landscape, and water room

 If areas prone to waterlogging cannot be avoided, install water blocking and drainage facilities or
raise the ground.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 30

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 4 Site Requirements

 Cable trenches shall not be used for drainage. Fire retardant sealing shall be implemented at cable
holes (such as holes through partition walls and floors).

 Areas prone to earthquakes and with seismic fortification intensity higher than 9

 Areas prone to debris flow, landslide, quicksand, karst caves, and other direct hazards

 Areas within the mining land subsidence (dislocation) zone

 Areas within the scope of blasting hazard

 Areas prone to flood due to a dam or levee failure

 Protection areas for important water supply sources

 Protection areas for historic relics

 Populated areas, high-rise buildings, and underground buildings

 Intersections and busy roads of urban main roads

Requirements for flood and waterlogging prevention in site selection:

 The site design elevation of a large-scale electrochemical energy storage system (power
≥ 100 MW) shall be higher than the flood level with a probability of 1% or the historical
highest waterlogging level.

 The site design elevation of a medium- or small-scale electrochemical energy storage
system (power < 100 MW) shall be higher than the flood level with a probability of 2%
or the historical highest waterlogging level.

 If the site design elevation cannot meet the preceding requirements, change the site
location or take different flood and waterlogging prevention measures based on the site
requirements.

 For energy storage plants prone to wind and waves from rivers, lakes, and seas, the
elevation of flood prevention facilities shall consider the wind and wave height with a
probability of 2% and an additional safety height of 0.5 m.

 When a large amount of catchment water flows into or passes through the site, it is
recommended that side ditches or drainage ditches be built to drain water from the
ground in an organized manner.

Security fencing:

It is recommended that physical walls or fences be used for isolation and protection in the
energy storage equipment area. The fences shall be equipped with a door lock and the
recommended fence height is greater than 2.2 m. Fire walls shall be permitted to be
substituted for part or all of the fences, depending on the actual design plans.

**4.2 Clearance Requirements**

Clearance must be reserved for installation and O&M, as required in the following:

 Reserve at least 3000 mm clearance on the long sides and the control unit cabin side of
the ESS, respectively.

If the preceding safety distance requirements cannot be met, install fire walls between the ESSs. Ensure
that the length and height of the fire walls extending above and beyond the physical boundary of the
ESS installation meet the requirements in section ''Site Selection Requirements''.

 Set up a maintenance aisle around or on one side of the container. The net width of the
aisle shall be no less than 1200 mm.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 31

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 4 Site Requirements

 The preceding clearance requirements are for reference only in terms of installation and
O&M. The clearances must also comply with local fire control requirements.

**4.3 Foundation Requirements**

The foundation layout design should meet the space requirements for ESS installation and O&M. The
design institute can contact local Huawei pre-sales engineers to obtain the drawings about the
foundation.

Before installation, build a concrete platform and trenches on the selected ground. The
foundation construction requirements are as follows:

 The dimensions of the foundation should meet the installation and bearing requirements
of the equipment.

 The foundation must be above the highest water level of the local area in history and at
least 300 mm above the ground.

 The horizontal error between the foundation and the contact surface of the equipment
should be less than 5 mm.

 The resistance of a bond should be less than or equal to 0.1 ohms.

 The ESS uses bottom cabling. Cables need to be pre-buried under the control unit cabin.

 The inner diameter of the protective tube should not be less than 1.5 times of the outer
diameter of the cable (including the protective layer).

 Construct drainage facilities based on the local geological conditions and municipal
drainage requirements to ensure that no water will accumulate at the equipment
foundation. The foundation should meet the local drainage requirements for the local
historical maximum rainfall. Drained water should be disposed of in accordance with
local laws and regulations.

 After the foundation is excavated, prevent water from entering the foundation. If water
enters the foundation, excavate and refill the affected parts.

 A cable trench (if any) cannot be used for drainage. Fire retardant sealing should be
implemented at cable holes (such as holes through partition walls and floors).

**Check Item**

|No.|Check Item|Acceptance Criteria|
|---|---|---|
|1|Cabling space<br>at the bottom| If there is no maintenance space at the bottom, it is<br>recommended that the cabling space at the bottom of the<br>container be no less than 1.1 m.<br> If there is maintenance space at the bottom, it is<br>recommended that the cabling space at the bottom of the<br>container be no less than 1.3 m.|
|2|Cable| The bending radius of the cables is not less than 15 times<br>the cable diameter.<br> The voltage drop of the farthest loop does not exceed 5%.<br> The sensitivity, voltage level, and thermal stability of the<br>cables meet the local design specifications.|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 32

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 4 Site Requirements

**Figure 4-1** Diagram of foundation

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 33

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 5 Installing ESS

# 5 Installin ESS

**g**

**5.1 Installation Preparations**

**5.1.1 Preparing Tools**

 The tools shown in the figures are for reference only.

 The tool table may not list out some tools required onsite. Onsite installation personnel and the
customer need to prepare the tools based on site requirements.

**Installation Tools**

Tools such as socket wrenches, torque wrenches, and screwdrivers must be insulated tools.

|Adjustable<br>torque wrench|Insulated torque<br>socket wrench<br>(including an<br>extension bar)|Insulated torque socket<br>wrench (including an<br>extended socket)|Phillips insulated torque<br>screwdriver|
|---|---|---|---|
|<br>Flat-head<br>insulated torque<br>screwdriver|<br>Wire strippers|<br>Diagonal pliers|<br>Utility knife|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 34

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 5 Installing ESS

|Cable cutter|RJ45 crimping<br>tool|Vacuum cleaner|Multimeter<br>DC voltage measurement<br>range ≥ 1500 V DC|
|---|---|---|---|
|<br>Marker|<br>Steel measuring<br>tape|<br>Digital or bubble level|<br>Hydraulic pliers|
|<br>Heat-shrink<br>tubing|<br>Heat gun|<br>Cable tie|<br>Insulation ladder|
|<br>Crane|<br>Hoisting rope<br>and lifting eye|<br>Rubber mallet|<br>Hammer drill|
|<br>Drill bit<br>(φ14/φ16/φ20)|-|-|-|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 35

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 5 Installing ESS

**Personal Protective Equipment (PPE)**

|Insulated gloves|Protective gloves|Safety goggles|Dust mask|
|---|---|---|---|
|<br>Safety shoes|<br>Reflective vest|<br>Safety helmet|<br>Safety harness|
|<br>Medical kit|-|-|-|

**5.1.2 Installation Environment Check**

Check the site requirements one by one, and start installation only after all requirements are
met. The Company will not be liable for any consequences in the case that the installation
environment does not meet the requirements.

Mark the safe zone: Use red caution belts to delimit a safe zone, clean up obstacles in the safe
zone, and place construction signs and warning signs in prominent positions.

**5.2 Unpacking and Acceptance**

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 36

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 5 Installing ESS

 After placing the equipment in the installation position, unpack it with care to prevent
scratches. Keep the equipment stable during unpacking.

 After unpacking, check whether the fastening components and removable components are
loose. If they are loose, notify the carrier and manufacturer immediately.

 The blue adhesive plastic film on the outdoor air conditioner unit of the ESS is used to
prevent foreign objects from entering the air conditioner unit during storage. Do not
remove the blue adhesive plastic film during storage. Remove the blue adhesive plastic
film before power-on and commissioning.

**5.3 Determining the Installation Position of the ESS**

**Prerequisites**

 The site requirements are met.

 Check and adjust the height of the concrete platforms to ensure that the height difference
between the upper surfaces of all platforms does not exceed 5 mm.

Ensure that the concrete platforms meet requirements.

 Determine the installation position and orientation of the ESS based on site conditions.

**Procedure**

**Step 1** Determine the reference points for installing the ESS on the concrete platforms. Mark the
reference points using a marker.

**Step 2** On the basis of the reference points, mark the mounting positions for the four corner fittings
of the ESS using an ink fountain and a long soft measure tape.

**Figure 5-1** Position of corner fittings (top view)

**----End**

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 37

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 5 Installing ESS

**5.4 Securing the ESS**

**Step 1** Open the door of the control unit cabin to get the angle steels in the carton. Secure the ESS
using four angle steels. One angle steel at the bottom of the left and right sides, and three
angle steels at the bottom of the back.

 Place a wooden block on the top of an expansion bolt, and then knock at the wooden block
using a claw hammer to avoid damaging the expansion bolt.

 Ensure that the expansion bolts are tightened when securing the angle steel to the base.

 There are four mounting holes where angle steel brackets contact the base. Mark all mounting holes.

 Each angle steel bracket must be secured by two mounting holes. It is recommended that the outer
two mounting holes be used. If steel bars in a concrete base block the drill bit or when the position
deviation occurs during the first drilling, use the inner mounting holes.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 38

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 5 Installing ESS

**Figure 5-2** Securing the ESS

**----End**

**Follow-up Procedure**

After the ESS is installed, verify the installation to ensure normal use of products and smooth
subsequent installation.

**Table 5-1** Verifying the installation

<!-- INICIO TABLA 5-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Follow-up Procedure** After the ESS is installed, verify the installation to ensure normal use of products and smooth subsequent installation. -->

**Tabla 5-1: ** Verifying the installation**

| No. | Check Item | Check Method | Criteria |
| --- | --- | --- | --- |
| 1 | Bolts and nuts | Tighten the bolts<br>and nuts again using<br>a wrench with the<br>same torque. | Bolts and nuts are<br>tightened. |
| 2 | Check whether the doors of the<br>ESS can be opened and closed | Open and close the<br>doors of the ESS. | All doors of the ESS<br>can be opened and |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Issue Draft B (2024-01-23) -->
<!-- FIN TABLA 5-1 -->


|No.|Check Item|Check Method|Criteria|
|---|---|---|---|
|1|Bolts and nuts|Tighten the bolts<br>and nuts again using<br>a wrench with the<br>same torque.|Bolts and nuts are<br>tightened.|
|2|Check whether the doors of the<br>ESS can be opened and closed|Open and close the<br>doors of the ESS.|All doors of the ESS<br>can be opened and|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 39

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 5 Installing ESS

|No.|Check Item|Check Method|Criteria|
|---|---|---|---|
||~~properly.~~||~~closed properly.~~|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 40

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 6 Installing Cables

# 6 Installin Cables

**g**

 Do not smoke or have an open flame around batteries.

 The site must be equipped with qualified fire fighting facilities, such as fire sand and
carbon dioxide fire extinguishers.

 Wear personal protective equipment and use dedicated insulated tools to avoid electric
shocks or short circuits.

 Do not connect two or more cables to the positive or negative power port of a battery in
parallel.

 Stay away from the equipment when preparing cables to prevent cable scraps from
entering the equipment. Cable scraps may cause sparks and result in personal injury and
equipment damage.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 41

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 6 Installing Cables

 Do not install battery packs on rainy, snowy, or foggy days. Otherwise, the battery packs
may be corroded by moisture or rain.

**Figure 6-1** Installing cables

**Table 6-1** ESS Cable Connection Description

<!-- INICIO TABLA 6-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!--  Do not install battery packs on rainy, snowy, or foggy days. Otherwise, the battery packs may be corroded by moisture or rain. **Figure 6-1** Installing cables -->

**Tabla 6-1: ** ESS Cable Connection Description**

| Wiri<br>ng<br>Posi<br>tion | No. | Descr<br>iptio<br>n | Cabl<br>e<br>Hol<br>e<br>Posi<br>tion | External<br>Device | Cabl<br>e<br>Len<br>gth | Cable<br>Specificati<br>ons | Nu<br>mbe<br>r of<br>Cabl<br>es | Func<br>tion | Terminal<br>Specifica<br>tions | Remarks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Left<br>side<br>of<br>the<br>powe<br>r <br>distri<br>butio<br>n <br>com<br>part<br>ment | 1 | DC<br>power<br>output<br>termin<br>al | D | Energy<br>storage<br>converter<br>(PCS) | > 3<br>m <br>outsi<br>de<br>the<br>cabin<br>et | Directly<br>buried<br>(armored)<br>single-core<br>cable with a<br>cross-sectio<br>nal area of<br>240 mm2, <br>DC 1500 V,<br>two cables<br>for each<br>PCS (one<br>cable for | 24 | Powe<br>r <br>input<br>and<br>outpu<br>t | Cord end<br>DT/OT<br>copper<br>terminal or<br>copper-alu<br>minum<br>transfer<br>terminal,<br>M12 bolt<br>connection | In the<br>0.5C_GFM<br>scenario, 48<br>routes are<br>connected. |

<!-- Estadísticas: 1 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- Issue Draft B (2024-01-23) -->
<!-- FIN TABLA 6-1 -->


|Wiri<br>ng<br>Posi<br>tion|No.|Descr<br>iptio<br>n|Cabl<br>e<br>Hol<br>e<br>Posi<br>tion|External<br>Device|Cabl<br>e<br>Len<br>gth|Cable<br>Specificati<br>ons|Nu<br>mbe<br>r of<br>Cabl<br>es|Func<br>tion|Terminal<br>Specifica<br>tions|Remarks|
|---|---|---|---|---|---|---|---|---|---|---|
|Left<br>side<br>of<br>the<br>powe<br>r <br>distri<br>butio<br>n <br>com<br>part<br>ment|1|DC<br>power<br>output<br>termin<br>al|D|Energy<br>storage<br>converter<br>(PCS)|> 3<br>m <br>outsi<br>de<br>the<br>cabin<br>et|Directly<br>buried<br>(armored)<br>single-core<br>cable with a<br>cross-sectio<br>nal area of<br>240 mm2, <br>DC 1500 V,<br>two cables<br>for each<br>PCS (one<br>cable for|24|Powe<br>r <br>input<br>and<br>outpu<br>t|Cord end<br>DT/OT<br>copper<br>terminal or<br>copper-alu<br>minum<br>transfer<br>terminal,<br>M12 bolt<br>connection|In the<br>0.5C_GFM<br>scenario, 48<br>routes are<br>connected.|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 42

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 6 Installing Cables

|Wiri<br>ng<br>Posi<br>tion|No.|Descr<br>iptio<br>n|Cabl<br>e<br>Hol<br>e<br>Posi<br>tion|External<br>Device|Cabl<br>e<br>Len<br>gth|Cable<br>Specificati<br>ons|Nu<br>mbe<br>r of<br>Cabl<br>es|Func<br>tion|Terminal<br>Specifica<br>tions|Remarks|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||~~positive and~~<br>one cable<br>for negative<br>poles)|||||
||2|Groun<br>d bar|D|Power<br>cable<br>armor<br>layer (if<br>any)|> 3<br>m <br>outsi<br>de<br>the<br>cabin<br>et|Power cable<br>armor layer<br>grounding,<br>lead 120<br>mm2|24|Grou<br>nding<br>of the<br>armor<br>layer<br>of the<br>powe<br>r <br>cable|Cord end<br>DT/OT<br>copper<br>terminal,<br>M8 bolt<br>connection|In the<br>0.5C_GFM<br>scenario,<br>crimp two<br>armored<br>ground<br>cables for<br>each ground<br>terminal.|
|Righ<br>t side<br>of<br>the<br>powe<br>r <br>distri<br>butio<br>n <br>com<br>part<br>ment|3|Main<br>groun<br>d <br>point<br>of the<br>batter<br>y <br>contai<br>ner|C|Power<br>plant<br>ground<br>grid<br>groundin<br>g cable|> 3<br>m <br>outsi<br>de<br>the<br>cabin<br>et|120 mm2 <br>single-core<br>directly<br>buried bare<br>copper<br>ground<br>cable|1|ESS<br>groun<br>ding|Cord end<br>DT/OT<br>copper<br>terminal<br>M10 bolt<br>connection|Main<br>grounding<br>wire|
|Righ<br>t side<br>of<br>the<br>powe<br>r <br>distri<br>butio<br>n <br>com<br>part<br>ment|5|AC<br>auxili<br>ary<br>power<br>input|C|DTS<br>cabinet or<br>station<br>transform<br>er|> 3<br>m <br>outsi<br>de<br>the<br>cabin<br>et|Directly<br>buried<br>(armored)<br>5-core<br>copper/alu<br>minum<br>cable, AC<br>400 V,<br>25mm2-150<br>mm2 <br>(L1/L2/L3),<br>25mm2-95<br>mm2 <br>(N/PE),<br>cable outer<br>diameter: ≤<br>59.5 mm|1|Exter<br>nal<br>auxili<br>ary<br>sourc<br>e|Cord end<br>DT/OT<br>copper<br>terminal or<br>copper-alu<br>minum<br>transfer<br>terminal,<br>M10 bolt<br>connection<br>(L1/L2/L3<br>/N)|AC<br>auxiliary<br>power<br>supply|
|Righ<br>t side<br>of<br>the<br>powe<br>r <br>distri<br>butio<br>n <br>com<br>part<br>ment|3|AC<br>auxili<br>ary<br>groun<br>d <br>cable|AC<br>auxili<br>ary<br>groun<br>d <br>cable|AC<br>auxili<br>ary<br>groun<br>d <br>cable|AC<br>auxili<br>ary<br>groun<br>d <br>cable|AC<br>auxili<br>ary<br>groun<br>d <br>cable|AC<br>auxili<br>ary<br>groun<br>d <br>cable|AC<br>auxili<br>ary<br>groun<br>d <br>cable|M10<br>bolted<br>connection<br>(PE)|M10<br>bolted<br>connection<br>(PE)|
|Righ<br>t side<br>of<br>the<br>powe<br>r <br>distri<br>butio<br>n <br>com<br>part<br>ment|4|UPS<br>power<br>input|A|Passenger<br>UPS<br>power<br>supply|> 3<br>m <br>outsi<br>de|Two-core<br>outdoor<br>armored<br>copper|1|Exter<br>nal<br>UPS|2.5 mm2 to<br>10 mm2 <br>pin<br>terminal|Optional|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 43

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 6 Installing Cables

|Wiri<br>ng<br>Posi<br>tion|No.|Descr<br>iptio<br>n|Cabl<br>e<br>Hol<br>e<br>Posi<br>tion|External<br>Device|Cabl<br>e<br>Len<br>gth|Cable<br>Specificati<br>ons|Nu<br>mbe<br>r of<br>Cabl<br>es|Func<br>tion|Terminal<br>Specifica<br>tions|Remarks|
|---|---|---|---|---|---|---|---|---|---|---|
||||||~~the~~<br>cabin<br>et|~~cable with a~~<br>cross-sectio<br>nal area of<br>2.5 mm2 to<br>10 mm2|||||
||7|FE<br>port<br>(CMU<br>)|B|Other<br>energy<br>storage<br>container<br>s or<br>SmartLog<br>ger in the<br>SACU|> 3<br>m <br>outsi<br>de<br>the<br>cabin<br>et|Outdoor<br>shielded<br>network<br>cable with<br>armor,<br>CAT5e<br>(For ring<br>network<br>communica<br>tion, the<br>quantity is<br>2.)|1|North<br>boun<br>d <br>netw<br>ork<br>com<br>muni<br>catio<br>n|RJ45<br>connector|Select one<br>of the two.<br>When<br>connecting<br>optical<br>fibers,<br>connect the<br>optical fiber<br>connecting<br>tray first<br>and then<br>connect the<br>optical fiber<br>to the<br>CMU.|
||7|Optica<br>l port|Optica<br>l port|Other<br>energy<br>storage<br>container<br>s or<br>SACUs|> 3<br>m <br>outsi<br>de<br>the<br>cabin<br>et|Directly<br>buried<br>armored<br>shielded<br>optical<br>cable<br>(For ring<br>network<br>communica<br>tion, the<br>quantity is<br>2.)|1|North<br>boun<br>d <br>fiber<br>com<br>muni<br>catio<br>n|Optical<br>fiber<br>terminal|Optical<br>fiber<br>terminal|
||9|CAN<br>and<br>FAST<br>I/O<br>comm<br>unicat<br>ion|B|Energy<br>storage<br>converter<br>(PCS)|> 3<br>m <br>outsi<br>de<br>the<br>cabin<br>et|Outdoor<br>directly<br>buried<br>shielded<br>and<br>armored<br>network<br>cable,<br>CAT5e|6|Com<br>muni<br>catio<br>n <br>betwe<br>en the<br>ESS<br>and<br>PCS|RJ45<br>connector|In the 0.5C<br>scenario,<br>two<br>network<br>cables in<br>each power<br>loop are<br>connected<br>to the<br>correspondi<br>ng RJ45<br>network<br>port.<br>In the<br>0.5C_GFM<br>scenario,|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 44

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 6 Installing Cables

|Wiri<br>ng<br>Posi<br>tion|No.|Descr<br>iptio<br>n|Cabl<br>e<br>Hol<br>e<br>Posi<br>tion|External<br>Device|Cabl<br>e<br>Len<br>gth|Cable<br>Specificati<br>ons|Nu<br>mbe<br>r of<br>Cabl<br>es|Func<br>tion|Terminal<br>Specifica<br>tions|Remarks|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||~~connect the~~<br>four PCS<br>network<br>cables in<br>each power<br>loop to the<br>correspondi<br>ng RJ45<br>network<br>port.|
|Pane<br>l of<br>the<br>powe<br>r <br>distri<br>butio<br>n <br>com<br>part<br>ment|6|Socke<br>t|/|On-site<br>commissi<br>oning<br>equipmen<br>t|> 3<br>m <br>outsi<br>de<br>the<br>cabin<br>et|AC 230<br>V/10 A, no<br>cable trench|1|Temp<br>orary<br>powe<br>r <br>suppl<br>y for<br>on-sit<br>e <br>com<br>missi<br>oning<br>equip<br>ment|National<br>standard<br>plug|Connect to<br>a laptop or<br>other|
|Pane<br>l of<br>the<br>powe<br>r <br>distri<br>butio<br>n <br>com<br>part<br>ment|8|Wi-Fi<br>hotspo<br>t|/|Mobile<br>phone or<br>tablet|Wire<br>less<br>trans<br>missi<br>on|No cable<br>trenches|1|Conn<br>ect<br>the<br>mobil<br>e <br>phon<br>e to<br>the<br>CMU<br>throu<br>gh<br>Wi-Fi<br>.|/|Open the<br>right door<br>of the<br>power<br>distribution<br>compartme<br>nt to<br>activate the<br>Wi-Fi<br>hotspot.|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 45

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 7 Power-On and Commissioning

# 7 Power-On and Commissionin

**g**

**7.1 Prerequisites**

**7.1.1 Checking Before Power-On**

|Item|Check Item|Acceptance Criteria|
|---|---|---|
|Gener<br>al<br>inspec<br>tion|Equipment appearance| The equipment is intact and free from rust or paint<br>flake-off. If paint flakes off, repaint the equipment.<br> The labels on the equipment are clear. Damaged<br>labels must be replaced.|
|Gener<br>al<br>inspec<br>tion|Cable appearance| Cable sheathings are properly wrapped and not<br>damaged.<br> Cable hoses are intact.|
|Gener<br>al<br>inspec<br>tion|Cable connections| Cables are connected in the designed positions.<br> Terminals are prepared as required and securely<br>connected.<br> Labels on both ends of each cable are clear and<br>specific, and attached in the same direction.|
|Gener<br>al<br>inspec<br>tion|Cable layout| Electrical and ELV cables are routed separately.<br> Cables are neat and tidy.<br> Cable tie joints are evenly cut without burrs.<br> Cables are placed properly and reserve some slack<br>at bending points to avoid stress.<br> Cables are routed neatly without twists or<br>crossovers in the cabinet.|
|Gener<br>al<br>inspec<br>tion|Switch| The DC LV Panel switch is set to OFF.<br> The battery rack switch is set to OFF.|
|ESS|Installation| The installation meets the design requirements.<br> The ESS is level, and each door can be opened<br>properly.|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 46

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 7 Power-On and Commissioning

|Item|Check Item|Acceptance Criteria|
|---|---|---|
||Grounding|Each ESS has at least two ground points and is<br>grounded securely. The resistance of a bond shall be<br>less than or equal to 0.1 ohms.|
||Accessory|The number and positions of external accessories<br>installed meet design requirements.|
||Label|All labels are correct, clear, and complete.|
||Cleanness|The ESS is clean and tidy inside, without any<br>unnecessary cables, cable ends, terminals, or tools. No<br>garbage is found outside the equipment.|
|Batter<br>y <br>cabin|Circuit breaker|The MCCBs are set to OFF.|
|Batter<br>y <br>cabin|Copper bar|The copper bar is not deformed, and no foreign objects<br>are placed on the copper bar.|
|Batter<br>y <br>cabin|Cable|The bolts for installing the cables are tightened and the<br>cables are not loose.|
|Batter<br>y <br>cabin|Cable hole sealing|Cable holes have been sealed.|
|Batter<br>y <br>cabin|Component|All components are intact.|
|Batter<br>y <br>cabin|Foreign object|Remove all foreign objects from the battery cabin, such<br>as tools and remaining installation materials.|
|Contr<br>ol unit<br>cabin|SPD|The SPD indicator is green.|
|Contr<br>ol unit<br>cabin|AC meter|The buttons of the AC meter function properly and the<br>screen is free of cracks.|
|Contr<br>ol unit<br>cabin|Cable|The bolts for installing the cables are tightened and the<br>cables are not loose.|
|Contr<br>ol unit<br>cabin|Foreign object|There are no foreign objects in the control unit cabin,<br>such as packing materials.|
|Contr<br>ol unit<br>cabin|Component (such as CMU, adapter,<br>extinguishant control panel)|All components are intact.|
|Contr<br>ol unit<br>cabin|Fire cylinder|The pressure of fire cylinder is normal.|

**7.1.2 Fire Suppression System Test**

**Step 1** Use an electronic smoke generator to generate smoke and point it at the smoke detector in the
ESS until a smoke alarm is triggered.

**Step 2** Use a heat gun to heat the temperature detector and observe the alarm status of the fire control
panel.

**Step 3** Check whether the solenoid valve striker is ejected.

**Step 4** Reset solenoid valve.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 47

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 7 Power-On and Commissioning

**Step 5** Reset the fire control panel and check whether the alarm is cleared.

**----End**

**7.2 Device Power-On**

 Before the equipment is put into operation for the first time, ensure that the parameters are
set correctly by professional personnel. Incorrect parameter settings may result in
noncompliance with local grid connection requirements and affect the normal operations
of the equipment.

 Before turning on the switches in the secondary devices of the ESS, check that the AC
voltage of the auxiliary power supply and bus voltage are within the normal ranges.

 If the ESS has not been used for six months or longer after being installed, it must be
checked and tested by professionals before operation.

 Perform power-on within two weeks after cables are connected. Otherwise, replace the
desiccants with new ones (Montmorillonite desiccant, 500 g).

 Before power-on, remove the desiccants from the cabins and dispose of them according to
the applicable local waste disposal act.

 Before power-on, remove the blue protective films with the label .

 Do not open the battery compartment door after power-on. Otherwise, the system will shut
down.

**Procedure**

**Step 1** Switch on the DC circuit breakers of battery racks in the Battery cabin.

**Step 2** (Optional) Switch on UPS circuit breaker.

 The UPS switch position is reserved only in some models. If the UPS switch is needed, install it by
yourself.

 Perform this operation only in microgrid or off-grid scenarios.

**Step 3** Switch on circuit breaker on the SPD and check that the SPD display window is green.

**Step 4** Switch on the circuit breaker for the AC input power cable of the ESS.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 48

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 7 Power-On and Commissioning

 After turning on the main switch, immediately check that the L1, L2, and L3 phase
voltages are 220 V AC/230 V AC.

 If the phase voltage displayed on the digital display meter is 400 V or other values, the
cables between the L1, L2, L3, and N wires may be incorrectly connected. In this case,
check the cables. Do not power on devices before checking cables. Otherwise, devices
such as air conditioners may be damaged.

**Step 5** Switch on all circuit breakers of the ESS power distribution system.

1. Switch on the AC power circuit breakers of the liquid cooling unit in sequence.

2. Switch on ESS adapter circuit breaker, extinguishant control panel circuit breaker,
lighting system circuit breaker in sequence.

3. Switch on 220/230 V socket circuit breaker.

4. Open the extinguishant control panel and turn on the two power switches inside. Switch
off extinguishant control panel circuit breaker, make sure it running well using the
battery power supply. Switch on the circuit breaker.

5. Switch on the PSU AC input circuit breaker

6. On the subrack, switch on the DC input circuit breakers and the exhaust fan controller
circuit breakers, and the air conditioner circuit breaker of the power distribution cabin in

sequence.

**Step 6** Switch on the DC circuit breakers in the power distribution cabin.

**----End**

**7.3 Deployment and Commissioning**

**Step 1** Complete the power-on authorization operation.

**Step 2** Complete the liquid cooling unit self-check.

**Step 3** Log in to the monitoring management system.

**Step 4** Upgrade the software version of the monitoring management system.

1. choose **Monitoring** - **Logger(Local)** - **About** to check the monitoring management
system software version.

**Figure 7-1** Checking the software version of the monitoring management system

2. If the software version is not the latest, upgrade the software according to the upgrade
guide of the software package.

**Step 5** Set up a network connection.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 49

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 7 Power-On and Commissioning

When the monitoring management system connects to the network over a wired network,
choose **Settings** - **Comm. Param.** - **Wired Network**, and set parameters such as the IP
address according to the actual planning on the user side.

**Step 6** Complete the deployment configuration according to the deployment guide of the monitoring
and management system.

**Step 7** Complete the cable connection test.

**Step 8** Complete the devices searching.

**Step 9** Set the end SOC according to the actual planning.

**----End**

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 50

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 8 Maintenance

# 8 Maintenance

**8.1 Routine Maintenance**

**8.1.1 Unscheduled Maintenance**

Log in to the management system and check whether there are major or minor alarms.

**8.1.2 Quarterly Maintenance**

**Table 8-1** Quarterly maintenance checklist

<!-- INICIO TABLA 8-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Log in to the management system and check whether there are major or minor alarms. **8.1.2 Quarterly Maintenance** -->

**Tabla 8-1: ** Quarterly maintenance checklist**

| Maintenan<br>ce Category | Maintenance Action | Expected Result | System<br>Powered Off<br>or Not |
| --- | --- | --- | --- |
| Container | Visual inspection:<br> Appearance<br> Rust condition<br> Door lock<br> Ventilation vent[1] |  The coating is not peeling<br>or scratched.<br> There is no obvious paint<br>peeling or rust.<br> The door locks are not<br>damaged.<br> There is no dust and foreign<br>objects at the ventilation<br>vents.<br> There are no insects,<br>rodents, snakes and other<br>animals. | No |
| Adapter | Check the indicator status. | The indicator is steady green. | No |
| Battery<br>cabin, power<br>distribution<br>cabin and<br>liquid<br>cooling<br>cabin | Check whether there are foreign objects<br>in the cabin. | The cabin is clean and free<br>from foreign objects. | No |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Issue Draft B (2024-01-23) -->
<!-- FIN TABLA 8-1 -->


|Maintenan<br>ce Category|Maintenance Action|Expected Result|System<br>Powered Off<br>or Not|
|---|---|---|---|
|Container|Visual inspection:<br> Appearance<br> Rust condition<br> Door lock<br> Ventilation vent[1]| The coating is not peeling<br>or scratched.<br> There is no obvious paint<br>peeling or rust.<br> The door locks are not<br>damaged.<br> There is no dust and foreign<br>objects at the ventilation<br>vents.<br> There are no insects,<br>rodents, snakes and other<br>animals.|No|
|Adapter|Check the indicator status.|The indicator is steady green.|No|
|Battery<br>cabin, power<br>distribution<br>cabin and<br>liquid<br>cooling<br>cabin|Check whether there are foreign objects<br>in the cabin.|The cabin is clean and free<br>from foreign objects.|No|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 51

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 8 Maintenance

|Maintenan<br>ce Category|Maintenance Action|Expected Result|System<br>Powered Off<br>or Not|
|---|---|---|---|
|Note [1]: Maintain the ventilation vents once after each sandstorm.|Note [1]: Maintain the ventilation vents once after each sandstorm.|Note [1]: Maintain the ventilation vents once after each sandstorm.|Note [1]: Maintain the ventilation vents once after each sandstorm.|

**8.1.3 Semi-annual Maintenance**

**Table 8-2** Semi-annual maintenance checklist

<!-- INICIO TABLA 8-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---|---| |Note [1]: Maintain the ventilation vents once after each sandstorm.|Note [1]: Maintain the ventilation vents once after each sandstorm.|Note [1]: Maintain the ventilation vents once after each sandstorm.|Note [1]: Maintain the ventilation vents once after each sandstorm.| **8.1.3 Semi-annual Maintenance** -->

**Tabla 8-2: ** Semi-annual maintenance checklist**

| Maintenan<br>ce Category | Maintenance Action | Expected Result | System<br>Powered Off<br>or Not |
| --- | --- | --- | --- |
| Liquid<br>cooling unit |  Check the appearance.<br> Check whether the V-shaped outdoor<br>heat exchanger has sand<br>accumulation.<br> Remove and clean the filter[1]. <br> Cleaning the outdoor heat<br>exchanger[2] <br> Clean the external fan[3]. |  There is no obvious damage<br>to the appearance.<br> There is no obvious paint<br>peeling or rust.<br> The screws are secured.<br> The fan rotates properly<br>without abnormal sound. Its<br>surface is clean without<br>sand, dust or foreign object.<br> The filter is clean and not<br>blocked.<br> The outdoor heat exchanger<br>is free of sand and<br>blockage. | No |
| Air-cooled<br>air<br>conditioner |  Check the appearance.<br> Remove and clean the filter[1]. <br> Clean the condenser[2]. <br> Clean the external fan[3]. |  There is no obvious damage<br>to the appearance.<br> There is no obvious paint<br>peeling or rust.<br> The screws are secured.<br> The fan rotates properly<br>without abnormal sound. Its<br>surface is clean without<br>sand, dust or foreign object.<br> The filter is clean and not<br>blocked.<br> The outdoor heat exchanger<br>is not blocked. | No |
| Coolant | Visual inspection | Coolant position above<br>minimum scale | No |
| Note [1]: Monthly maintenance is recommended in a high-temperature (≥ 35°C) or low-temperature (≤ 0°C)<br>environment. The first maintenance interval starts when the ESS is installed.<br>Note [2]: You are advised to clean the condenser after each occurrence of a sandstorm and before summer in<br>sandstorm-stricken areas. In other areas, clean the condenser according to the actual situation and ensure that | Note [1]: Monthly maintenance is recommended in a high-temperature (≥ 35°C) or low-temperature (≤ 0°C)<br>environment. The first maintenance interval starts when the ESS is installed.<br>Note [2]: You are advised to clean the condenser after each occurrence of a sandstorm and before summer in<br>sandstorm-stricken areas. In other areas, clean the condenser according to the actual situation and ensure that | Note [1]: Monthly maintenance is recommended in a high-temperature (≥ 35°C) or low-temperature (≤ 0°C)<br>environment. The first maintenance interval starts when the ESS is installed.<br>Note [2]: You are advised to clean the condenser after each occurrence of a sandstorm and before summer in<br>sandstorm-stricken areas. In other areas, clean the condenser according to the actual situation and ensure that | Note [1]: Monthly maintenance is recommended in a high-temperature (≥ 35°C) or low-temperature (≤ 0°C)<br>environment. The first maintenance interval starts when the ESS is installed.<br>Note [2]: You are advised to clean the condenser after each occurrence of a sandstorm and before summer in<br>sandstorm-stricken areas. In other areas, clean the condenser according to the actual situation and ensure that |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Issue Draft B (2024-01-23) -->
<!-- FIN TABLA 8-2 -->


|Maintenan<br>ce Category|Maintenance Action|Expected Result|System<br>Powered Off<br>or Not|
|---|---|---|---|
|Liquid<br>cooling unit| Check the appearance.<br> Check whether the V-shaped outdoor<br>heat exchanger has sand<br>accumulation.<br> Remove and clean the filter[1]. <br> Cleaning the outdoor heat<br>exchanger[2] <br> Clean the external fan[3].| There is no obvious damage<br>to the appearance.<br> There is no obvious paint<br>peeling or rust.<br> The screws are secured.<br> The fan rotates properly<br>without abnormal sound. Its<br>surface is clean without<br>sand, dust or foreign object.<br> The filter is clean and not<br>blocked.<br> The outdoor heat exchanger<br>is free of sand and<br>blockage.|No|
|Air-cooled<br>air<br>conditioner| Check the appearance.<br> Remove and clean the filter[1]. <br> Clean the condenser[2]. <br> Clean the external fan[3].| There is no obvious damage<br>to the appearance.<br> There is no obvious paint<br>peeling or rust.<br> The screws are secured.<br> The fan rotates properly<br>without abnormal sound. Its<br>surface is clean without<br>sand, dust or foreign object.<br> The filter is clean and not<br>blocked.<br> The outdoor heat exchanger<br>is not blocked.|No|
|Coolant|Visual inspection|Coolant position above<br>minimum scale|No|
|Note [1]: Monthly maintenance is recommended in a high-temperature (≥ 35°C) or low-temperature (≤ 0°C)<br>environment. The first maintenance interval starts when the ESS is installed.<br>Note [2]: You are advised to clean the condenser after each occurrence of a sandstorm and before summer in<br>sandstorm-stricken areas. In other areas, clean the condenser according to the actual situation and ensure that|Note [1]: Monthly maintenance is recommended in a high-temperature (≥ 35°C) or low-temperature (≤ 0°C)<br>environment. The first maintenance interval starts when the ESS is installed.<br>Note [2]: You are advised to clean the condenser after each occurrence of a sandstorm and before summer in<br>sandstorm-stricken areas. In other areas, clean the condenser according to the actual situation and ensure that|Note [1]: Monthly maintenance is recommended in a high-temperature (≥ 35°C) or low-temperature (≤ 0°C)<br>environment. The first maintenance interval starts when the ESS is installed.<br>Note [2]: You are advised to clean the condenser after each occurrence of a sandstorm and before summer in<br>sandstorm-stricken areas. In other areas, clean the condenser according to the actual situation and ensure that|Note [1]: Monthly maintenance is recommended in a high-temperature (≥ 35°C) or low-temperature (≤ 0°C)<br>environment. The first maintenance interval starts when the ESS is installed.<br>Note [2]: You are advised to clean the condenser after each occurrence of a sandstorm and before summer in<br>sandstorm-stricken areas. In other areas, clean the condenser according to the actual situation and ensure that|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 52

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 8 Maintenance

|Maintenan<br>ce Category|Maintenance Action|Expected Result|System<br>Powered Off<br>or Not|
|---|---|---|---|
|~~the filter and condenser are not blocked. You are advised to use a high-pressure water gun or air blow gun. For~~<br>a high-pressure water gun, the pressure shall be less than or equal to 30 kPa, the flow rate shall be less than or<br>equal to 12.5 L/min, and the recommended working distance is 2.5 m to 3 m. For a high-pressure air blow gun,<br>the recommended working distance is 0.5 m to 1 m.<br>Note [3]: You are advised to clean the fan once a quarter in areas with heavy sandstorm and dust. In other areas,<br>clean the fan according to the actual situation and ensure that there is no sand or dust on the fan blades of the air<br>conditioner. To clean the fan blades, you need to remove the front cover of the air conditioner. You are advised<br>to use a dust brush or a high-pressure air blow gun and meet the corresponding requirement in Note [2].|~~the filter and condenser are not blocked. You are advised to use a high-pressure water gun or air blow gun. For~~<br>a high-pressure water gun, the pressure shall be less than or equal to 30 kPa, the flow rate shall be less than or<br>equal to 12.5 L/min, and the recommended working distance is 2.5 m to 3 m. For a high-pressure air blow gun,<br>the recommended working distance is 0.5 m to 1 m.<br>Note [3]: You are advised to clean the fan once a quarter in areas with heavy sandstorm and dust. In other areas,<br>clean the fan according to the actual situation and ensure that there is no sand or dust on the fan blades of the air<br>conditioner. To clean the fan blades, you need to remove the front cover of the air conditioner. You are advised<br>to use a dust brush or a high-pressure air blow gun and meet the corresponding requirement in Note [2].|~~the filter and condenser are not blocked. You are advised to use a high-pressure water gun or air blow gun. For~~<br>a high-pressure water gun, the pressure shall be less than or equal to 30 kPa, the flow rate shall be less than or<br>equal to 12.5 L/min, and the recommended working distance is 2.5 m to 3 m. For a high-pressure air blow gun,<br>the recommended working distance is 0.5 m to 1 m.<br>Note [3]: You are advised to clean the fan once a quarter in areas with heavy sandstorm and dust. In other areas,<br>clean the fan according to the actual situation and ensure that there is no sand or dust on the fan blades of the air<br>conditioner. To clean the fan blades, you need to remove the front cover of the air conditioner. You are advised<br>to use a dust brush or a high-pressure air blow gun and meet the corresponding requirement in Note [2].|~~the filter and condenser are not blocked. You are advised to use a high-pressure water gun or air blow gun. For~~<br>a high-pressure water gun, the pressure shall be less than or equal to 30 kPa, the flow rate shall be less than or<br>equal to 12.5 L/min, and the recommended working distance is 2.5 m to 3 m. For a high-pressure air blow gun,<br>the recommended working distance is 0.5 m to 1 m.<br>Note [3]: You are advised to clean the fan once a quarter in areas with heavy sandstorm and dust. In other areas,<br>clean the fan according to the actual situation and ensure that there is no sand or dust on the fan blades of the air<br>conditioner. To clean the fan blades, you need to remove the front cover of the air conditioner. You are advised<br>to use a dust brush or a high-pressure air blow gun and meet the corresponding requirement in Note [2].|

**8.1.4 Annual Maintenance**

**Product Maintenance**

**Table 8-3** Annual maintenance checklist

<!-- INICIO TABLA 8-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **8.1.4 Annual Maintenance** **Product Maintenance** -->

**Tabla 8-3: ** Annual maintenance checklist**

| Maintenance<br>Category | Maintenance Action | Expected Result | System<br>Powered Off<br>or Not |
| --- | --- | --- | --- |
| Battery pack | Visual inspection:<br> Appearance<br> Rust condition<br> Screw<br> Signal and power connection<br>terminals |  There is no obvious damage to<br>the appearance.<br> There is no obvious paint<br>peeling or rust.<br> The screws are secured.<br> The signal and power terminals<br>are not loose or disconnected. | Yes. Power off<br>ESSs<br>connected to<br>the same DC<br>bus. |
| Smoke detector<br>and heat detector | Spot check the detectors using<br>dedicated devices to generate<br>smoke or heat.[1][2] |  The detector indicator is steady<br>red.<br> The extinguishant control panel<br>reports the corresponding alarm. | Power off a<br>single ESS. In<br>the ESS, the<br>battery rack<br>DC circuit<br>breakers of<br>battery cabins<br>are OFF, and<br>the DC circuit<br>breakers of the<br>power<br>distribution<br>cabin are OFF.<br>The AC<br>auxiliary<br>power supply<br>is not powered<br>off. |
| Extinguishant |  Check the working status of |  The display is normal. | Power off a |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Issue Draft B (2024-01-23) -->
<!-- FIN TABLA 8-3 -->


|Maintenance<br>Category|Maintenance Action|Expected Result|System<br>Powered Off<br>or Not|
|---|---|---|---|
|Battery pack|Visual inspection:<br> Appearance<br> Rust condition<br> Screw<br> Signal and power connection<br>terminals| There is no obvious damage to<br>the appearance.<br> There is no obvious paint<br>peeling or rust.<br> The screws are secured.<br> The signal and power terminals<br>are not loose or disconnected.|Yes. Power off<br>ESSs<br>connected to<br>the same DC<br>bus.|
|Smoke detector<br>and heat detector|Spot check the detectors using<br>dedicated devices to generate<br>smoke or heat.[1][2]| The detector indicator is steady<br>red.<br> The extinguishant control panel<br>reports the corresponding alarm.|Power off a<br>single ESS. In<br>the ESS, the<br>battery rack<br>DC circuit<br>breakers of<br>battery cabins<br>are OFF, and<br>the DC circuit<br>breakers of the<br>power<br>distribution<br>cabin are OFF.<br>The AC<br>auxiliary<br>power supply<br>is not powered<br>off.|
|Extinguishant| Check the working status of| The display is normal.|Power off a|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 53

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 8 Maintenance

|Maintenance<br>Category|Maintenance Action|Expected Result|System<br>Powered Off<br>or Not|
|---|---|---|---|
|~~control panel~~|~~devices in the extinguishant~~<br>control panel such as display<br>and indicators.<br> Clean the extinguishant control<br>panel as required.<br> Perform the self-check for the<br>solenoid valve and LLVD.| ~~The text on the maintenance~~<br>card is correct and clear. The<br>extinguishant control panel is<br>clean and free from dust.<br> The alarm and response of the<br>extinguishant control panel are<br>normal.|~~single ESS. In~~<br>the ESS, the<br>battery rack<br>DC circuit<br>breakers of<br>battery cabins<br>are OFF, and<br>the DC circuit<br>breakers of the<br>power<br>distribution<br>cabin are OFF.<br>The AC<br>auxiliary<br>power supply<br>is not powered<br>off.|
|Extinguishant<br>control panel<br>power supply| Appearance of backup<br>batteries.[3] <br> Test the automatic switchover<br>of the main and standby power<br>supply.[4]| The batteries are not deformed,<br>damaged, or leaking.<br> The standby power supply can<br>start automatically and support<br>the extinguishant control panel<br>and terminal devices to work for<br>at least 30 minutes.|No|
|Fire cylinder[5]|Check the pressure gauge on the<br>fire cylinder.|All components are free from<br>collision, deformation, or other<br>mechanical damage, the surfaces<br>are free from rust, and the<br>protective layer is intact.|No|
|Coolant|Visual inspection| No visible impurities (grain size<br>greater than 0.6 mm) (visual<br>inspection)<br> pH greater than 6.5* (pH test<br>paper)|No|
|Liquid-cooled<br>pipes|Visual inspection|No visible leakage (visual<br>inspection)|No|
|Note [1]: Remove cables from the solenoid valve in advance to prevent extinguishant release.<br>Note [2]: After the check is complete, perform a reset on the extinguishant control panel.<br>Note [3]: Annual maintenance is performed for new batteries in the first two years. Quarterly maintenance is<br>performed from the third year until the batteries are replaced with new ones.<br>Note [4]: The ESS shuts down during switchover of the main and standby power supply.<br>Note [5]: Comply with local regulations or standards when using the fire cylinder.|Note [1]: Remove cables from the solenoid valve in advance to prevent extinguishant release.<br>Note [2]: After the check is complete, perform a reset on the extinguishant control panel.<br>Note [3]: Annual maintenance is performed for new batteries in the first two years. Quarterly maintenance is<br>performed from the third year until the batteries are replaced with new ones.<br>Note [4]: The ESS shuts down during switchover of the main and standby power supply.<br>Note [5]: Comply with local regulations or standards when using the fire cylinder.|Note [1]: Remove cables from the solenoid valve in advance to prevent extinguishant release.<br>Note [2]: After the check is complete, perform a reset on the extinguishant control panel.<br>Note [3]: Annual maintenance is performed for new batteries in the first two years. Quarterly maintenance is<br>performed from the third year until the batteries are replaced with new ones.<br>Note [4]: The ESS shuts down during switchover of the main and standby power supply.<br>Note [5]: Comply with local regulations or standards when using the fire cylinder.|Note [1]: Remove cables from the solenoid valve in advance to prevent extinguishant release.<br>Note [2]: After the check is complete, perform a reset on the extinguishant control panel.<br>Note [3]: Annual maintenance is performed for new batteries in the first two years. Quarterly maintenance is<br>performed from the third year until the batteries are replaced with new ones.<br>Note [4]: The ESS shuts down during switchover of the main and standby power supply.<br>Note [5]: Comply with local regulations or standards when using the fire cylinder.|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 54

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 8 Maintenance

**Environment Maintenance**

Check whether the site environment meets requirements by referring to section "Site Selection
Requirements"

**8.2 Troubleshooting**

**8.2.1 CMU Alarms**

**Liquid Cooling Unit Water Supply Temperature High**

 Possible Cause: The supply water temperature is higher than the high temperature alarm
threshold.

 Suggestion:

a. Check the liquid cooling unit parameter High Temperature Alarm Threshold and
ensure that the parameter is set properly. The default value is 55°C.

b. If the parameters are set properly, check other alarms related to the liquid cooling
unit and rectify the fault according to the corresponding handling suggestions. If no
other alarm is generated, shut down the liquid cooling unit and contact technical
support.

**Liquid Cooling Unit Water Supply Temperature Low**

 Possible Cause: The supply water temperature is lower than the low temperature alarm
threshold.

 Suggestion:

a. Check the liquid cooling unit parameter Low Temperature Alarm Threshold and
ensure that the parameter is set properly. The default value is 12°C.

b. If the parameters are set properly, check other alarms related to the liquid cooling
unit and rectify the fault according to the corresponding handling suggestions. If no
other alarm is generated, shut down the liquid cooling unit and contact technical
support.

**Liquid Cooling Unit Compressor Faulty**

 Possible Cause:

a. The compressor cable is loose.

b. The compressor is damaged.

 Suggestion:

a. Shut down the system at a proper time and take security measures.

b. Power off the liquid cooling unit, open the shell of the liquid cooling unit, and
check whether the compressor cable is loose. If yes, tighten the cable. Check
whether the compressor is obviously damaged and whether there is a burning smell.
If yes, contact technical support.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 55

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 8 Maintenance

**8.2.2 ESC and BCU Alarms**

**Battery Pack Communication of Rack Controller Abnormal**

 Possible Cause: The rack controller fails to communicate with the battery pack.

 Suggestion:

a. Determine the positions of the input and output circuit breakers of the ESC and the
AC input power switch of the PSU corresponding to [ESR-CabinetNo
ESM-SlotNo]

b. Issue a hibernation command to all ESRs, and turn off the switch on the battery side,
the switch on the bus side, and the AC input power switch of the PSU. Then wait
for 5 minutes.

c. Check whether the communications cable and the [ESR-CabinetNo ESM-SlotNo]
communications cable are securely connected

d. Turn on the AC input power switch of the PSU, the switch on the battery side, and
the switch on the bus side in sequence, and issue a running command.

e. If the alarm persists, contact the vendor or technical support.

**Rack Controller Temperature High**

 Possible Cause:

a. The installation position of the battery power control module is not well ventilated.

b. The ambient temperature is too high.

c. The battery power control module is abnormal.

d. The fan in the battery power control module is abnormal.

 Suggestion:

a. Determine the positions of the input and output circuit breakers associated with

[ESC-No] and the AC input power switch of the PSU.

b. Issue a hibernation command to all ESRs, and turn off the switch on the battery side,
the switch on the bus side, and the AC input power switch of the PSU. Then wait
for 5 minutes.

c. Check the ventilation of [ESC-No] and whether the ambient temperature exceeds
the upper threshold.

d. If the ventilation is poor or the ambient temperature is too high, improve the
ventilation and heat dissipation.

e. If an indoor fan fault alarm is generated and cannot be cleared after the fan is
restarted, contact the vendor or technical support.

f. Check whether any outdoor fan for rack controllers is faulty.

g. If the ventilation, ambient temperature, and outdoor fans are normal and the alarm
persists, contact the vendor or technical support.

**8.2.3 BMU Alarms**

**Optimization Unit of Battery Pack Abnormal**

 Possible Cause: A major fault has occurred in the circuit inside the optimization unit of
the battery pack.

 Suggestion:

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 56

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 8 Maintenance

a. Locate the input and output circuit breakers and PSU output DC switch of the ESC
equipment associated with [ESR-CabinetNo ESM-SlotNo].

b. Issue a shutdown command to the ESC associated with this ESR, turn off the switch
on the battery side, the switch on the bus side and the PSU output DC switch in turn,
and wait for 5 minutes.

c. Turn on the PSU output DC switch, the switch on the battery side and the switch on
the bus side in turn, and issue a running command.

d. If the alarm persists, contact your dealer or technical support.

**Battery Pack Temperature High**

 Possible Cause:

a. The installation position of the battery module is not well ventilated.

b. The air conditioner/fan is not running properly.

 Suggestion:

a. Determine the positions of the input and output circuit breakers of the ESC and the
DC output power switch of the PSU corresponding to [ESR-CabinetNo
ESM-SlotNo].

b. Issue a hibernation command to the ESR corresponding to the ESC, and turn off the
switch on the battery side, the switch on the bus side, and the DC output switch of
the PSU. Then wait for 5 minutes.

c. Check whether any air conditioner or fan alarm is generated. If yes, check whether
the air intake vent of the air conditioner is blocked. If yes, clear the air intake vent
and improve the ventilation and heat dissipation.

d. Check whether the copper bar connection of the battery pack meets the torque
requirements by referring to the quick guide of the product.

e. Turn on the DC output switch of the PSU, the switch on the battery side, and the
switch on the bus side in sequence, and issue a running command.

f. If the alarm persists, contact the vendor or technical support.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 57

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 9 Emergency Handling

# 9 Emer enc Handlin

**g** **y** **g**

If an accident (including but not limited to the following) occurs on the site, ensure the safety
of onsite personnel first and contact the Company's service engineers.

**Battery Falling or Strong Impact**

 If a battery has obvious damage or abnormal odor, smoke, or fire occurs, evacuate the
personnel immediately, call emergency services, and contact the professionals. The
professionals shall use fire extinguishing facilities to extinguish the fire under safety
protection.

 If the appearance is not deformed or damaged, and there is no obvious abnormal odor,
smoke, or fire, ensure safety and perform the following operations:

−
Warehouse: Evacuate personnel, transfer the battery to an open and safe place by
professionals using mechanical tools, and contact the Company's service engineers.
Leave the battery for an hour and ensure that the battery temperature is within the
room temperature range (tolerance: ±10°C) before handling.

−
ESS onsite: Evacuate personnel, close the doors of the ESS, transfer the battery to
an open and safe place by professionals using mechanical tools, and contact the
Company's service engineers. Leave the battery for an hour before handling.

**Flood**

 Power off the system if it is safe to do so.

 If any part of the batteries is submerged in water, do not touch the batteries to avoid
electric shock.

 Do not use batteries that have been soaked in water. Contact a battery recycling company
for disposal.

**Fire Alarm Horn/Strobe**

When the alarm indicator on the equipment blinks or buzzes:

 Do not approach.

 Do not open the door.

 Stay away immediately.

 Cut off the power supply remotely only when your safety is guaranteed.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 58

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 9 Emergency Handling

**Gas Exhaust**

 Onsite personal protection: Do not directly face the exhaust vents.

 Post-disaster product maintenance: Contact the Company's service engineers for
evaluation.

**Extinguishant Release or Fire**

 Suggestions for onsite O&M personnel:

a. When a fire occurs, evacuate from the building or equipment area, press the fire
alarm bell, and immediately call the fire emergency service. Notify the professional
firefighters and provide them with relevant product information, including but not
limited to battery pack types, ESS capacity, and battery pack location and
distribution.

b. Do not enter the affected building or equipment area under any circumstances, and
do not open the doors of the ESS. Isolate and monitor the site. Keep irrelevant
personnel away from the site.

c. After calling the fire emergency service, remotely power off the system (such as the
Smart Transformer Station, Smart PCS, auxiliary power supply devices, and
combiner box power supply) while ensuring your own safety.

d. After professional firefighters arrive, provide relevant product information,
including but not limited to battery pack types, ESS capacity, battery pack location
and distribution, and user manuals.

e. After the fire is extinguished, the site must be handled by professionals in
accordance with local laws and regulations. Do not open the doors of the ESS
without permission.

f. Post-disaster product maintenance: Contact the Company's service engineers for
evaluation.

 Suggestions for professional firefighters:

a. For product information, see the information provided by O&M personnel,
including but not limited to battery pack types, ESS capacity, battery pack location
and distribution, and user manuals.

b. Do not open the doors of the ESS before it is deemed safe by professionals.

c. Follow local fire fighting regulations.

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 59

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 10 Technical Specifications

# 10 Technical S ecifications

**p**

**Table 10-1** Battery Container

<!-- INICIO TABLA 10-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- # 10 Technical S ecifications **p** -->

**Tabla 10-1: ** Battery Container**

| Technical Specifications | LUNA2000-4.5MWH-2H1 |
| --- | --- |
| Rated voltage at the DCDC<br>bus side | 1331.2 V |
| Maximum voltage at the<br>DCDC bus side | 1500 V |
| Nominal power (kW) | 2236 kW |
| Battery capacity per container<br>(kWh) | 4472 kWh |
| Charge & Discharge rate | ≤0.5C |
| Container dimensions (W x H<br>x D) | 6058 mm x 2896 mm x 2438 mm |
| Weight | ≤ 41 t |
| Operating temperature range | -30°C to +55°C |
| Storage temperature range | -40°C to +60°C |
| Operating humidity range | 0~100% (No condensing) |
| Cooling Method | Liquid Cooling |
| Fire suppression system | Water Sprinkler, Novec 1230 (Optional) |
| Communication Interface | Ethernet / SFP |
| System communications<br>protocol | Modbus TCP |
| Protection Degree | IP55 |
| Anti-corrosion level | C5-Medium |
| Standards compliance | RoHS, IEC62477-1, IEC62040-1, IEC61000-6-2,<br>EN55011, UL9540A, IEC62619, UN3536, etc. |

<!-- Estadísticas: 17 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Issue Draft B (2024-01-23) -->
<!-- FIN TABLA 10-1 -->


|Technical Specifications|LUNA2000-4.5MWH-2H1|
|---|---|
|Rated voltage at the DCDC<br>bus side|1331.2 V|
|Maximum voltage at the<br>DCDC bus side|1500 V|
|Nominal power (kW)|2236 kW|
|Battery capacity per container<br>(kWh)|4472 kWh|
|Charge & Discharge rate|≤0.5C|
|Container dimensions (W x H<br>x D)|6058 mm x 2896 mm x 2438 mm|
|Weight|≤ 41 t|
|Operating temperature range|-30°C to +55°C|
|Storage temperature range|-40°C to +60°C|
|Operating humidity range|0~100% (No condensing)|
|Cooling Method|Liquid Cooling|
|Fire suppression system|Water Sprinkler, Novec 1230 (Optional)|
|Communication Interface|Ethernet / SFP|
|System communications<br>protocol|Modbus TCP|
|Protection Degree|IP55|
|Anti-corrosion level|C5-Medium|
|Standards compliance|RoHS, IEC62477-1, IEC62040-1, IEC61000-6-2,<br>EN55011, UL9540A, IEC62619, UN3536, etc.|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 60

LUNA2000-4.5MWH-2H1 Smart String ESS
User Manual 10 Technical Specifications

**Table 10-2** Battery Pack

<!-- INICIO TABLA 10-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Copyright © Huawei Digital Power Technologies Co., Ltd. 60 LUNA2000-4.5MWH-2H1 Smart String ESS User Manual 10 Technical Specifications -->

**Tabla 10-2: ** Battery Pack**

| Technical Specifications | Battery Pack |
| --- | --- |
| Cell Material | LFP |
| Number of Cell | 104 |
| Nominal Capacity | 280 Ah / 93.18 kWh |
| Protection Degree | IP65 |

<!-- Estadísticas: 4 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Issue Draft B (2024-01-23) -->
<!-- FIN TABLA 10-2 -->


|Technical Specifications|Battery Pack|
|---|---|
|Cell Material|LFP|
|Number of Cell|104|
|Nominal Capacity|280 Ah / 93.18 kWh|
|Protection Degree|IP65|

Issue Draft B

(2024-01-23)

Copyright © Huawei Digital Power Technologies Co., Ltd. 61