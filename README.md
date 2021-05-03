# Laser-Tripwire
A Laser Tripwire Security System using Raspberry Pi.

## Abstract:
We have made a laser tripwire with Python and Raspberry Pi. This can be used as an easy-to-implement security system for our homes. The system uses a laser and LDR sensor. If the laser line is broken, the buzzer is sounded, a warning LED flashes and an alert is displayed. This is a cost effective security measure that can be applied by minimal requirements and a short snipper of code.

## Equipment Used:
* A Raspberry Pi (any model will do, but wiring may vary)
* A Laser Pointer
* A Breadboard
* Female-Male and Female-Female Jumper leads
* A Piezo Buzzer
* An LDR
* A LED
* A 1μF Capacitor

## Setting up the Circuit:
- [x] Place an LDR into the breadboard.
- [x] Now place a capacitor in series with the LDR. As the capacitor is a polar component, we must make sure the long leg is on the same track as the LDR leg.
- [x] Finally add jumper leads to connect the two components to the Raspberry Pi.
- [x] The Piezo buzzer is a polar component, like the capacitor. Place it into the breadboard and connect the longer leg to GPIO 17 and the shorter leg into one of the ground pins.
- [ ] The LED is a polar component as well. Place it into the breadboard and connect the longer leg to GPIO 18 and the shorter leg into one of the ground pins.
