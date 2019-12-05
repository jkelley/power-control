# keysight-power

Basic control and status readout for a network-connected Keysight
N5700-series power supply.  Uses telnetlib to issue Keysight commands for
control of power output and voltage setting / readout.

Control library:
* `keysight.py` underlying power supply object for control/readout

Example scripts:
* `off / on` turn supply output off/on
* `status` report supply status and voltage
* `voltage` change supply output voltage

