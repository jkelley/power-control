#
# Keysight Series N5700
#

from scpi import SCPI

class Keysight:

    def _cmd(self, scpi_cmd):
        self.telnet.write((scpi_cmd + "\n").encode())
        return self.telnet.read_until("SCPI>").decode().strip()
