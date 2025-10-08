---
title: Catalog Sheet 001-0269: Intelligent Photoelectric Smoke Detector
author: Desconocido
date: D:19991208125738Z
language: en
type: report
pages: 4
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Features
  - Description
  - - Self-diagnostics and History Log, Automatic Device Mapping,
-->

**EDWARDS SYSTEMS TECHNOLOGY**

TM **INTERNATIONAL**
**ANALOG ADDRESSABLE INITIATING DEVICES**

Intelligent Photoelectric
Smoke Detector

Model SIGA-PS

_**Note:**_ _Some features described here may not be supported by all_
_control systems. Check your control panel’s Installation and_
_Operation Guide for details._

# Features

**!** **Integral microprocessor**

**!** **Non-volatile memory**

**!** **Automatic mapping device**

**!** **Electronic addressing**

**!** **Environmental compensation**

**!** **Intelligent detector**

**!** **Wide 0.67% to 3.77%/ft. sensitivity range**

**!** **Twenty pre-alarm sensitivity values, set in 5% increments1**

**!** **Identification of dirty or defective detectors**

**!** **Automatic day/night sensitivity adjustment**

**!** **Twin RED/GREEN status LEDs**

**!** **Standard, relay, fault isolator, and audible mounting bases**

**!** **Designed and manufactured to ISO 9001 standards**

# Description

EST’s Signature Series Model SIGA-PS Intelligent Photoelectric
Smoke Detector gathers analog information from its smoke sensing
element and converts it into digital signals. The detector’s onboard microprocessor measures and analyzes these signals. It
compares the information to historical readings and time patterns
to make an alarm decision. Digital filters remove signal patterns
that are not typical of fires. Unwanted alarms are virtually eliminated.

The microprocessor in each detector provides four additional benefits
# - Self-diagnostics and History Log, Automatic Device Mapping,

**Stand-alone Operation and Fast, Stable Communication** .

**Self-diagnostics and History Log** - Each Signature Series detector
constantly runs self-checks to provide important maintenance
information. The results of the self-check are automatically updated
and permanently stored in the detector’s non-volatile memory.
This information is accessible for review any time at the control
panel, PC, or by using the SIGA-PRO Signature Program/Service
Tool.

Application Notes
Available

The information stored in the detector’s memory includes:

 - detector type, serial number, and address

 - date of manufacture, hours of operation, and last maintenance date2

 - current detector sensitivity and environmental compensation
values

 - original detector sensitivity values upon manufacturing2

 - number of recorded alarms and troubles2

 - time and date of last alarm1

 - analog signal patterns just before the last alarm1

 - most recent trouble code logged by the detector -- 32 possible
trouble codes may be used to diagnose faults.

In the unlikely event that an unwanted alarm does take place, the
control panel’s history file can be called up to help isolate the
problem and prevent it from happening again.

**Automatic Device Mapping** - The loop controller learns where
each device’s serial number address is installed relative to other
devices on the circuit. The mapping feature provides supervision
of each device’s installed location to prevent a detector from
being reinstalled (after cleaning etc.) in a different location from
where it was originally. The history log for the detector remains
relevant and intact regardless of its new location.

The Signature Series Data Entry Program also uses the mapping
feature. With interactive menus and graphic support, the wired
circuits between each device can be examined. Layout or “as-built”
drawing information showing wire branches (T-taps), device types
and their address are stored on disk for printing hard copy. This
takes the mystery out of the installation. The preparation of “as-built”
drawings is fast and efficient.

Device mapping allows the Signature loop controller to discover:

 - unexpected additional device addresses

 - missing device addresses

1 EST3 V.2 only.
2 Retrievable with SIGA-PRO programming tool. - changes to the wiring in the circuit.

EST I NTERNATIONAL

**201 CITY CENTRE DRIVE SUITE 500, MISSISSAUGA, ONTARIO, CANADA L5B 2T4**
**PHONE:** (001) 905-270-1711 - **FAX:** (001) 905-270-9553 - **WORLD WIDE WEB:** WWW.ESTINTERNATIONAL.COM
**U.S. SALES:** SARASOTA, FL; PHONE 941-739-4638; FAX 941-727-1214 - **CANADA SALES:** OWEN SOUND, ON; PHONE 519-376-2430; FAX 519-376-7258

**Issue 5** **Literature Sheet #85001-0269** **Page 1 of 4**
**Not to be used for installation purposes.**

**Stand-alone Operation:** A decentralized alarm decision by the
detector is guaranteed. On-board intelligence permits the detector
to operate in stand-alone mode. If loop controller CPU communications fail for more than four seconds, all devices on that circuit
go into stand-alone mode. The circuit acts like a conventional alarm
receiving circuit. Each detector on the circuit continues to collect
and analyze information from its surroundings. The detector alarms
if the preset smoke obscuration level is reached. If the detector is
mounted to a relay base, the relay operates. Similarly, if it is
mounted to an audible base, the on-board horn sounds.

**Fast Stable Communication:** On-board intelligence means less
information needs to be sent between the detector and the loop
controller. Other than regular supervisory polling response, the
detector only needs to communicate with the loop controller when
it has something new to report. This provides very fast response
time and allows a lower baud rate (speed) to be used for
communication on the loop. The lower baud rate offers several
advantages including:

 - less sensitivity to circuit wire characteristics

 - less sensitivity to noise glitches on the cable

 - less emitted noise from the data wiring

 - twisted or shielded wiring is not required.

**Electronic Addressing:** The loop controller electronically addresses each detector, saving valuable time during system
commissioning. Setting complicated switches or dials is not
required. Each detector has its own unique serial number stored in
its “on-board memory”. The loop controller identifies each device
on the circuit and assigns a “soft” address to that device’s serial
number. If desired, detectors can be addressed using the SIGAPRO Signature Program/Service Tool.

**Environmental Compensation:** Detection sensitivity is virtually
independent of its installed environment and its physical condition.
Environmental compensation means the sensing element adapts to
long-term changes caused by dirt, humidity, aging etc. It even compensates for small amounts of normal ambient smoke. Approximately
six times every hour the detector adjusts and updates the sensitivity
(% obscuration) baseline for its sensing element. Approximately
once every hour this information is written to its permanent memory.
The detector’s “learned” baseline is not lost, even when the detector
is removed for cleaning. _Signature Series environmental_
_compenstion is so reliable that it meets NFPA72 field sensitivity_
_testing requirements -- without the need for external meters._

The detector’s sensitivity setting selected by the installer floats up
or down to remain constant relative to the changing baseline. This
is called differential sensing.

**Sensitivity Range:** The SIGA-PS Photoelectric Detector has a
sensitivity range or window of 0.67% to 3.77%. The installer
selects the detector’s ALARM sensitivity level from five available
settings within the range.

**Pre-Alarm:** The detector stores one of 20 pre-alarm sensitivity values
to alert local personnel prior to the sensor reaching a full evacuation
sensitivity. Sensitivity values can be set in 5% increments. [1]

**Automatic Day/Night Sensitivity Selection:** Signature Series
detectors may be programmed for different sensitivities during day
and night periods. This allows the detector to be more sensitive
during unoccupied periods when lower ambient background
conditions are expected.

**Stability:** The SIGA-PS detector’s sensitivity remains stable in wind
velocities up to 5,000 ft/min (25.3 m/sec). Ambient temperature has
very little affect on the detector. The detector may be installed in
rooms with ambient temperatures up to 120 [o] F (49 [o] C).

**Status LEDs:** Twin LEDs are visible from any direction. A flashing
GREEN LED shows normal system polling from the loop
controller. A flashing RED LED means the detector is in alarm
state. Both LEDs on steady shows alarm state - stand-alone mode.
Normal GREEN LED activity is not distracting to building occupants,
but can be quickly spotted by a maintenance technician.

**Quality and Reliability:** EST detectors are manufactured in North
America to strict international ISO 9001 standards. All electronics
utilize surface mount technology (SMT) for smaller size and greater
immunity to RF noise. A conformal coating is used for humidity
and corrosion resistance. All critical contacts are gold plated.




Signature Series detectors mount to North American 1-gang
boxes, 3-1/2 inch or 4 inch octagon boxes, and to 4 inch square
electrical boxes 1-1/2 inches (38 mm) deep. They mount to
European BESA and 1-gang boxes with 60.3 mm fixing centers.





Each detector automatically identifies when it is dirty or defective
and causes a “dirty detector” message. The detector’s sensitivity
measurement can also be transmitted to the loop controller. A
sensitivity report can be printed to satisfy NFPA sensitivity measurements which must be conducted at the end of the first year and
every two years thereafter.

The user-friendly maintenance program shows the current state of
each detector and other pertinent messages. Single detectors may
be turned off temporarily from the control panel. Availability of
maintenance features is dependent on the fire alarm system used.
Scheduled maintenance (Regular or Selected) for proper detector
operation should be planned to meet the requirements of the
Authority Having Jurisdiction (AHJ). Refer to current NFPA 72 and
ULC CAN/ULC 536 standards.


!

The SIGA-PS detectors are compatible only with EST’s Signature
Loop Controller.

1 EST3 V.2 only.



 




 
  





Although photoelectric detectors have a wide range of fire sensing capabilities they are best suited for detecting slow, smoldering fires.
The table below shows six standard test fires used to rate the sensitivity of smoke and heat detectors. The table indicates that no single
sensing element is suited for all test fires.

EST recommends that this detector be installed according to latest recognized edition of national and local fire alarm codes.

|Test Fire|Type of Detector|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Test Fire|SIGA-IS Ion|SIGA-PS Photo|SIGA-HRS and<br>SIGA-HFS Rate-of<br>-Rise/Fixed Temp.|SIGA-PHS<br>Photo/Heat 3D|SIGA-IPHS<br>Ion/Photo/Heat 4D|
|Open Wood|optimum|unsuitable|optimum|very suitable|optimum|
|Wood Pyrolysis|suitable|optimum|unsuitable|optimum|optimum|
|Smouldering Cotton|very suitable|optimum|unsuitable|optimum|optimum|
|Poly Urethane Foam|very suitable|very suitable|suitable|very suitable|optimum|
|n-Heptane|optimum|very suitable|very suitable|optimum|optimum|
|Liquid Fire without<br>Smoke|unsuitable|unsuitable|optimum|very suitable|very suitable|

!



The detector mounting bases accept #18 AWG (0.75mm [2] ), #16 (1.0mm [2] ), #14 AWG (1.5mm [2] ), and #12 AWG (2.5mm2) wire sizes.

Note: Sizes #16 AWG (1.0mm [2] ) and #18 AWG (0.75mm [2] ) are preferred for ease of installation. See Signature Loop Controller catalog
sheet for detailed wiring requirement specifications.

**Standard Detector Base, SIGA-SB, SIGA-SB4**

**Relay Detector Base, SIGA-RB, SIGA-RB4**

**Isolator Detector Base, SIGA-IB, SIGA-IB4**

**Audible Detector Base, SIGA-AB4**

Jumper JW1
OUT = Low Volume
IN = High Volume

From Power Supply
or Previous Sounder Base

Jumper JW2
OUT = Steady Tone
IN = Temporal Tone

To Next Sounder Base or
E-O-L Relay

24 VDC IN (+) 24 VDC OUT (+)

24 VDC IN (-) 24 VDC OUT (-)

DATA OUT (-)

DATA IN (-)

DATA IN (+)

To Next Signature Device

DATA OUT (+)

From Signature Controller
or Previous Device



 




 
  






All detector mounting bases have wiring terminals that are
accessible from the “room-side” after mounting the base to the
electrical box. The bases mount to North American 1-gang boxes
and to 31⁄2 inch or 4 inch octagon boxes, 11⁄2 inches (38 mm) deep.
They also mount to European BESA and 1-gang boxes with 60.3
mm fixing centers. The SIGA-SB4, SIGA-RB4, and SIGA-IB4 mount
to North American 4 inch sq. electrical boxes in addition to the
above boxes. They include the SIGA-TS4 Trim Skirt which is used
to cover the “mounting ears” on the base.

**SIGA-AB4** **SIGA-SB** **SIGA-IB** **SIGA-RB** **SIGA-LED**
**Audible Base** **Standard Base** **Isolator Base** **Relay Base** **Remote LED**

**Standard Base SIGA-SB, SIGA-SB4** - This is the basic mounting
base for EST Signature Series detectors. The SIGA-LED Remote
LED is supported by the Standard Base.

**Relay Base SIGA-RB, SIGA-RB4** - This base includes a relay.
Normally open or closed operation is selected during installation.
The dry contact is rated for 1 amp (pilot duty) @ 30 Vdc. The relay’s
position is supervised to avoid accidentally jarring it out of position.
The SIGA-RB can be operated as a control relay if programmed to
do so at the control panel (EST3 V.2 only). The relay base does not
support the SIGA-LED Remote LED.

**Audible Base SIGA-AB4 -** This base is designed for use where
localized or group alarm signaling is required. When the detector
senses an alarm condition, the audible base emits a local alarm
signal. The optional SIGA-CRR Polarity Reversal Relay can be used
for sounding to other audible bases on the same 24 Vdc circuit.

Relay and Audible Bases operate as follows:

 - at system power-up or reset, the relay is de-energized

 - when a detector is installed in the base with the power
on, the relay energizes for four seconds, then de-energizes

 - when a detector is removed from a base with the power on,
the relay is de-energized

 - when the detector enters the alarm state, the relay is energized.

**Isolator Base SIGA-IB, SIGA-IB4** - This base includes a built-in line
fault isolator for use on Class A circuits. A detector must be
installed for it to operate. The isolator base does not support the
SIGA-LED Remote LED.

The isolator operates as follows:

 - a short on the line causes all isolators to open within 23 msec

 - at 10 msec intervals, beginning on one side of the Class A
circuit nearest the loop controller, the isolators close to
provide the next isolator down the line with power

 - when the isolator next to the short closes, reopens within 10 msec.

The process repeats beginning on the other side of the loop
controller.

**Remote LED SIGA-LED** - The remote LED connects to the SIGA-SB
or SIGA-SB4 Standard Base only. It features a North American size
1-gang plastic faceplate with a white finish and red alarm LED.

**SIGA-TS4 Trim Skirt** - Supplied with 4 inch bases, it can also be
ordered separately to use with the other bases to help hide surface
imperfections not covered by the smaller bases.



 

This detector will not operate without electrical power. As fires
frequently cause power interruption, we suggest you discuss further
safeguards with your fire protection specialist.

This detector will NOT sense fires that start in areas where smoke

cannot reach the detector. Smoke from fires in walls, roofs, or on the
opposite side of closed doors may not reach the detector to alarm it.



|Catalog Number|SIGA-PS|
|---|---|
|Sensing Element|Photoelectric - Light Scattering Principle|
|Storage &<br>Operating<br>Environment|Air Velocity Range: 0 to 5,000 ft/min (0 to 25.39 m/s);<br>Humidity: 0 to 93% RH, Non-Condensing<br>Operating Temp: 32oF to 120oF (0oC to 49oC);<br>Storage Temp: -4oF to 140oF (-20oCto 60oC)|
|Sensitivity Range|ULI/ULC - 0.67% to 3.77% obscuration/foot|
|User Selected<br>Alarm Sensitivity<br>Settings|Most Sensitive: 1.0%/ft.; More Sensitive: 2.0%/ft.;<br>Normal: 2.5%/ft.;<br>Less Sensitive: 3.0%/ft.; Least Sensitive: 3.5%/ft.|
|Pre-alarm Sensitivity|5% increments, allowing up to 20 pre-alarm settings|
|Operating Voltage|15.2 to 19.95 Vdc (19 Vdc nominal)|
|Operating Current|Quiescent: 45μA @ 19 V; Alarm: 45μA @ 19 V<br>Emergency Stand-alone Alarm Mode: 18mA<br>Pulse Current: 100 μA (100 msec);<br>During Communication: 9 mA max.|
|Construction & Finish|High Impact Engineering Polymer - White|
|Compatible<br>Mounting Bases|SIGA-SB Standard Base, SIGA-RB Relay Base,<br>SIGA-IB Isolator Base, SIGA-AB Audible Base|
|LED Operation|On-board Green LED - Flashes when polled;<br>On-board Red LED - Flashes when in alarm<br>Both LEDs - Glow steady when in alarm (stand-alone)<br>Compatible Remote Red LED (model SIGA-LED)<br>Flashes when in alarm|
|Compatibility|Use With: SIGNATURE Loop Controller|
|Address Requirements|Uses one Device Address|
|Agency Listings|UL, ULC, MEA, CSFM|
|UL Listed Spacing|30 ft|


 


|Catalog<br>Number|Description|Ship Wt.<br>lbs (kg)|
|---|---|---|
|SIGA-PS|Intelligent Photoelectric Detector<br>- UL/ULC Listed|.5 (.23)|
|Accessories|Accessories|Accessories|
|SIGA-SB|Detector Mounting Base - Standard|.2 (.09)|
|SIGA-SB4|4-inch Detector Mounting Base<br>c/w SIGA-TS4 Trim Skirt|4-inch Detector Mounting Base<br>c/w SIGA-TS4 Trim Skirt|
|SIGA-RB|Detector Mounting Base w/Relay|Detector Mounting Base w/Relay|
|SIGA-RB4|4-inch Detector Mounting Base w/Relay,<br>c/w SIGA-TS4 Trim Skirt|4-inch Detector Mounting Base w/Relay,<br>c/w SIGA-TS4 Trim Skirt|
|SIGA-IB|Detector Mounting Base<br>w/Fault Isolator|Detector Mounting Base<br>w/Fault Isolator|
|SIGA-IB4|4-inch Detector Mounting Base<br>w/ Fault Isolator, c/w SIGA-TS4 Trim Skirt|4-inch Detector Mounting Base<br>w/ Fault Isolator, c/w SIGA-TS4 Trim Skirt|
|SIGA-LED|Remote Alarm LED|Remote Alarm LED|
|SIGA-AB4|Audible (Sounder) Base|.3 (0.15)|
|SIGA-TS4|Trim Skirt (supplied with 4-inch bases)|.1 (.04)|



 




It is our intention to keep the product information current and accurate. We can not cover specific applications or anticipate all requirements.
All specifications are subject to change without notice. For more information or questions relative to this Specification Sheet, contact EST International.

Printed in Canada
© 1999 EST
 
  