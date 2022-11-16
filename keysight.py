#
# Keysight Series N5700
#

from scpi import SCPI

class Keysight(SCPI):
    DEFAULT_PORT = 5024
    # FIX ME
    MAX_VOLTAGE = 600
    def __init__(self, hostname, port=DEFAULT_PORT):
        super().__init__(hostname, port)

    def _remote_init(self):
        # Read header and initial prompt
        self.telnet.read_until("SCPI>".encode())

    def _cmd(self, scpi_cmd):
        self.telnet.write((scpi_cmd + "\n").encode())
        resp = self.telnet.read_until("SCPI>".encode()).decode()
        # Response includes newline and prompt, remove them
        resp = resp.split("\n")[0].strip()
        return resp
