#!/usr/bin/python
#
# Keysight Series N5700
#

import telnetlib

class Keysight:

    def __init__(self, hostname, port):

        self.hostname = hostname
        self.port = port
        self.telnet = telnetlib.Telnet(hostname, port)
        self.telnet.read_until("SCPI>")

    def getCurrent(self):
        self.telnet.write("MEAS:CURR?\n")
        resp = self.telnet.read_until("SCPI>")
        return float(resp.split("\n")[0])

    def getVoltage(self):
        self.telnet.write("MEAS:VOLT?\n")
        resp = self.telnet.read_until("SCPI>")
        return float(resp.split("\n")[0])

    def setVoltage(self, v):
        self.telnet.write("VOLT %f\n" % v)
        self.telnet.read_until("SCPI>")
        
    def off(self):
        self.telnet.write("OUTP OFF\n")
        self.telnet.read_until("SCPI>")

    def on(self):
        self.telnet.write("OUTP ON\n")
        self.telnet.read_until("SCPI>")

    def isOn(self):
        self.telnet.write("OUTP?\n")
        resp = self.telnet.read_until("SCPI>")
        return (int(resp.split("\n")[0]) == 1)
