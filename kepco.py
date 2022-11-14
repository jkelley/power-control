#!/usr/bin/python
#
# Kepco KLN series mini-SCPI interface
#

from scpi import SCPI

class KepcoException(Exception):
    pass

class Kepco(SCPI):
    # FIX ME determine this dynamically
    MAX_VOLTAGE = 80

    def __init__(self, hostname, port):
        super().__init__(hostname, port)
        # Put unit in remote mode
        self._cmd("SYST:REM")
        # Reprobe for unit ID
        self._probe()

