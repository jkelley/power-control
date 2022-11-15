#!/usr/bin/python
#
# Kepco KLN series mini-SCPI interface
#

from scpi import SCPI

class KepcoException(Exception):
    pass

class Kepco(SCPI):
    DEFAULT_PORT = 5025
    # FIX ME determine this dynamically
    MAX_VOLTAGE = 80

    def __init__(self, hostname, port=DEFAULT_PORT):
        super().__init__(hostname, port)

    def _remote_init(self):
        # Put unit in remote mode
        self._cmd("SYST:REM")

