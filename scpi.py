#!/usr/bin/python
#
# General SCPI power supply control
# through telnet.
#

import time
import telnetlib

class SCPI:
    CMD_DELAY_SEC = 0.2
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.telnet = telnetlib.Telnet(hostname, port)
        self._probe()

    def _cmd(self, scpi_cmd):
        self.telnet.write((scpi_cmd + "\n").encode())
        time.sleep(self.CMD_DELAY_SEC)
        return self.telnet.read_eager().decode().strip()

    def _probe(self):        
        resp = self._cmd("*IDN?")
        (self.manufacturer, self.model, self.serial, self.fwvers) = resp.split(",")
        
    def getCurrent(self):
        return float(self._cmd("MEAS:CURR?"))

    def getVoltage(self):
        return float(self._cmd("MEAS:VOLT?"))

    def setVoltage(self, v):
        self._cmd("SOUR:VOLT %f" % v)

    def off(self):
        self._cmd("OUTP OFF")

    def on(self):
        self._cmd("OUTP ON")

    def isOn(self):
        resp = self._cmd("OUTP?")
        return (int(resp) == 1)

    def isOff(self):
        resp = self._cmd("OUTP?")
        return (int(resp) == 0)

