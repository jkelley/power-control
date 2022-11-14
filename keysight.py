#
# Keysight Series N5700
#

from scpi import SCPI

class Keysight:
    DEFAULT_PORT = 5024
    # FIX ME
    MAX_VOLTAGE = 600
    def __init__(self, hostname, port=DEFAULT_PORT):
        super().__init__(hostname, port)
    
    def _cmd(self, scpi_cmd):
        self.telnet.write((scpi_cmd + "\n").encode())
        return self.telnet.read_until("SCPI>").decode().strip()
