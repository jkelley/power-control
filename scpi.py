#!/usr/bin/python
#
# General SCPI power supply control
# through telnet.
#

import time
import telnetlib

class SCPIException(Exception):
    pass

class SCPI:
    CMD_DELAY_SEC = 0.2
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        try:
            self.telnet = telnetlib.Telnet(hostname, port)
        except ConnectionRefusedError:
            raise SCPIException("Connection to %s:%d refused" % (hostname, port))
        self._remote_init()
        self._probe()

    def __str__(self):
        return("%s:%d -- %s %s #%s" % (self.hostname, self.port,
                                       self.manufacturer, self.model, self.serial))

    def _cmd(self, scpi_cmd):
        self.telnet.write((scpi_cmd + "\n").encode())
        time.sleep(self.CMD_DELAY_SEC)
        return self.telnet.read_eager().decode().strip()

    def _remote_init(self):
        return

    def _probe(self):        
        resp = self._cmd("*IDN?")
        # Keysight jams both fwvers and hwvers together in fourth field
        (self.manufacturer, self.model, self.serial, self.fwvers) = resp.split(",", 3)
        
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

