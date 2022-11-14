# keysight-power

Basic control and status readout for a network-connected Keysight
N5700-series or Kepco KLN power supply.  Uses telnetlib to issue 
SCPI command for control of power output and voltage setting / readout.

Control library:
* `scpi.py` underlying power supply object for control/readout
* `keysight.py` Keysight-specific protocol tweaks
* `kepco.py` Kepco-specific protocol tweaks

Example scripts:
* `off / on` turn supply output off/on
* `status` report supply status and voltage
* `voltage` change supply output voltage

