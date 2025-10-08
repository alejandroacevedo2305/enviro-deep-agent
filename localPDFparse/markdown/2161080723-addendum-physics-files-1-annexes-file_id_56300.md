---
title: ISO 9613-2.pdf
author: Héctor Saavedra
date: D:20241015164545-03'00'
language: en
type: legal
pages: 7
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 7.4 Screening (A bar )
-->

AR-INTERIM-CM (C ONTRACT : B4-3040/2001/329750/MAR/C1)
A DAPTATION AND REVISION OF THE INTERIM NOISE COMPUTATION METHODS FOR THE PURPOSE OF STRATEGIC NOISE MAPPING

WP 3.4.1: Industrial noise - Description of the calculation method

d is the distance from the source to receiver, in metres.

The mean height h m may be evaluated by the method shown in figure 3. Negative values for A gr from

equation (10) shall be replaced by zeros.

NOTE 12 For short distances d, equation (10) predicts no attenuation and equation (9) may be more

accurate.

When the ground attenuation is calculated using equation (10), the directivity correction D c in

equation (3) shall include a term D Ω, in decibels, to account for the apparent increase in sound power

level of the source due to reflections from the ground near the source.

where

h s is the height of the source above the ground, in metres;

h r is the height of the receiver above the ground, in metres;

d p is the source-to-receiver distance projected onto the ground plane, in metres.

# 7.4 Screening (A bar )

An object shall be taken into account as a screening obstacle (often called a barrier) if it meets the

following requirements:

-- the surface density is at least 10 kg/m [2] ;

-- the object has a closed surface without large cracks or gaps (consequently process

installations in chemical plants, for example, are ignored);

-- the horizontal dimension of the object normal to the source-receiver line is larger than the

acoustic wavelength λ at the nominal rnidband frequency for the octave band of interest; in

other words l l + l r - λ (see figure 4).

Each object that fulfils these requirements shall be represented by a barrier with vertical edges. The

top edge of the barrier is a straight line that may be sloping.

Project
team:

Wölfel Meßsysteme · Software GmbH & Co (main contractor) - AIB-Vinçotte EcoSafer - AKRON n.v.-s.a. LABEIN Technological Centre S.L. - Honorar-Professor Dipl.-Ing. Dr. techn. Judith LANG - LÄRMKONTOR GmbH

Page 19 of 49

AR-INTERIM-CM (C ONTRACT : B4-3040/2001/329750/MAR/C1)
A DAPTATION AND REVISION OF THE INTERIM NOISE COMPUTATION METHODS FOR THE PURPOSE OF STRATEGIC NOISE MAPPING

WP 3.4.1: Industrial noise - Description of the calculation method

h m = F/d, where F is the area

Figure 3 -- Method for evaluating the mean height h m

NOTE -- An object is only considered to be a screening obstacle when its horizontal dimension

perpendicular to the source-receiver line SR is larger than the wavelength: (l l + l r ) > λ

Figure 4 -- Plan view of two obstacles between the source (S) and the receiver (R)

Project
team:

Wölfel Meßsysteme · Software GmbH & Co (main contractor) - AIB-Vinçotte EcoSafer - AKRON n.v.-s.a. LABEIN Technological Centre S.L. - Honorar-Professor Dipl.-Ing. Dr. techn. Judith LANG - LÄRMKONTOR GmbH

Page 20 of 49

AR-INTERIM-CM (C ONTRACT : B4-3040/2001/329750/MAR/C1)
A DAPTATION AND REVISION OF THE INTERIM NOISE COMPUTATION METHODS FOR THE PURPOSE OF STRATEGIC NOISE MAPPING

WP 3.4.1: Industrial noise - Description of the calculation method

For the purposes of this part of ISO 9613, the attenuation by a barrier, A bar, shall be given by the

insertion loss. Diffraction over the top edge and around a vertical edge of a barrier may both be

important. (See fig-ure 5.) For downwind sound propagation, the effect of diffraction (in decibels)

over the top edge shall be calculated by

and for diffraction around a vertical edge by

where

D z is the barrier attenuation for each octave band [see equation (14)];

A gr is the ground attenuation in the absence of the barrier (i.e. with the screening obstacle

removed) (see 7.3).

Figure 5 -- Different sound propagation paths at a barrier

NOTES

Project
team:

Wölfel Meßsysteme · Software GmbH & Co (main contractor) - AIB-Vinçotte EcoSafer - AKRON n.v.-s.a. LABEIN Technological Centre S.L. - Honorar-Professor Dipl.-Ing. Dr. techn. Judith LANG - LÄRMKONTOR GmbH

Page 21 of 49

AR-INTERIM-CM (C ONTRACT : B4-3040/2001/329750/MAR/C1)
A DAPTATION AND REVISION OF THE INTERIM NOISE COMPUTATION METHODS FOR THE PURPOSE OF STRATEGIC NOISE MAPPING

WP 3.4.1: Industrial noise - Description of the calculation method

13 When A bar as defined by equation (12) is substituted in equation (4) to find the total

attenuation A, the two A gr, terms in equation (4) will cancel. The barrier attenuation D z in

equation (12) then includes the effect of the ground in the presence of the barrier.

14 For large distances and high barriers, the insertion loss calculated by equation (12) is not

sufficiently confirmed by measurements.

15 In calculation of the insertion loss for multisource industrial plants by high buildings (more

than 10 m above the ground), and also for high-noise sources within the plant, equation

(13) should be used in both cases for determining the long-term average sound pressure

level [using equation (6)].

16 For sound from a depressed highway, there may be attenuation in addition to that indicated

by equation (12) along a ground surface outside the depression, due to that ground surface.

To calculate the barrier attenuation D z, assume that only one significant sound-propagation path exists

from the sound source to the receiver. If this assumption is not valid, separate calculations are required

for other propagation paths (as illustrated in figure 5) and the contributions from the various paths to

the squared sound pressure at the receiver are summed.

The barrier attenuation D z, in decibels, shall be calculated for this path by equation (14):

where

C 2 is equal to 20, and includes the effect of ground reflections; if in special cases ground

reflections are taken into account separately by image sources, C 2 = 40;

C 3 is equal to 1 for single diffraction (see figure 6);

for double diffraction (see figure 7);

λ is the wavelength of sound at the nominal midband frequency of the octave band, in metres;

z is the difference between the pathlengths of diffracted and direct sound, as calculated by

equations (16) and (17), in metres;

K met is the correction factor for meteorological effects, given by equation (18);

Project
team:

Wölfel Meßsysteme · Software GmbH & Co (main contractor) - AIB-Vinçotte EcoSafer - AKRON n.v.-s.a. LABEIN Technological Centre S.L. - Honorar-Professor Dipl.-Ing. Dr. techn. Judith LANG - LÄRMKONTOR GmbH

Page 22 of 49

AR-INTERIM-CM (C ONTRACT : B4-3040/2001/329750/MAR/C1)
A DAPTATION AND REVISION OF THE INTERIM NOISE COMPUTATION METHODS FOR THE PURPOSE OF STRATEGIC NOISE MAPPING

WP 3.4.1: Industrial noise - Description of the calculation method

e is the distance between the two diffraction edges in the case of double diffraction (see

figure 7).

For single diffraction, as shown in figure 6, the path-length difference z shall be calculated by means

of equation (16):

where

d ss is the distance from the source to the (first) diffraction edge, in metres;

d sr is the distance from the (second) diffraction edge to the receiver, in metres;

a is the component distance parallel to the barrier edge between source and receiver, in

metres.

Project
team:

Wölfel Meßsysteme · Software GmbH & Co (main contractor) - AIB-Vinçotte EcoSafer - AKRON n.v.-s.a. LABEIN Technological Centre S.L. - Honorar-Professor Dipl.-Ing. Dr. techn. Judith LANG - LÄRMKONTOR GmbH

Page 23 of 49

AR-INTERIM-CM (C ONTRACT : B4-3040/2001/329750/MAR/C1)
A DAPTATION AND REVISION OF THE INTERIM NOISE COMPUTATION METHODS FOR THE PURPOSE OF STRATEGIC NOISE MAPPING

WP 3.4.1: Industrial noise - Description of the calculation method

Figure 6 -- Geometrical quantities for determining the pathlength difference for single

diffraction

Figure 7 -- Geometrical quantities for determining the pathlength difference for double

diffraction

Project
team:

Wölfel Meßsysteme · Software GmbH & Co (main contractor) - AIB-Vinçotte EcoSafer - AKRON n.v.-s.a. LABEIN Technological Centre S.L. - Honorar-Professor Dipl.-Ing. Dr. techn. Judith LANG - LÄRMKONTOR GmbH

Page 24 of 49

AR-INTERIM-CM (C ONTRACT : B4-3040/2001/329750/MAR/C1)
A DAPTATION AND REVISION OF THE INTERIM NOISE COMPUTATION METHODS FOR THE PURPOSE OF STRATEGIC NOISE MAPPING

WP 3.4.1: Industrial noise - Description of the calculation method

If the line of sight between the source S and receiver R passes above the top edge of the barrier, z is

given a negative sign.

For double diffraction, as shown in figure 7, the path-length difference z shall be calculated by

The correction factor K met for meteorological conditions in equation (14) shall be calculated using

equation (18):

For lateral diffraction around obstacles, it shall be assumed that K met = 1 (see figure 5).

NOTES

17 For source-to-receiver distances less than 100m, the calculation using equation (14) shows

that K met may be assumed equal to 1, to an accuracy of 1 dB.

18 Equation (15) provides a continuous transition from the case of single diffraction (e = 0)

where C3 = 1, to that of a well-separated double diffraction (e >> λ ) where C3 = 3.

19 A barrier may be less effective than calculated by equations (12) to (18) as a result of

reflections from other acoustically hard surfaces near the sound path from the source to the

receiver or by multiple reflections between an acoustically hard barrier and the source.

The barrier attenuation D z, in any octave band, should not be taken to be greater than 20 dB in the case

of single diffraction (i.e. thin barriers) and 25 dB in the case of double diffraction (i.e. thick barriers).

The barrier attenuation for two barriers is calculated using equation (14) for double diffraction, as

indicated in the lower part of figure 7. The barrier attenuation for more than two barriers may also be

calculated approximately using equation (14), by choosing the two most effective barriers, neglecting

the effects of the others.

Project
team:

Wölfel Meßsysteme · Software GmbH & Co (main contractor) - AIB-Vinçotte EcoSafer - AKRON n.v.-s.a. LABEIN Technological Centre S.L. - Honorar-Professor Dipl.-Ing. Dr. techn. Judith LANG - LÄRMKONTOR GmbH

Page 25 of 49