# power-control

Basic output control and status readout for a network-connected power supply
using
[SCPI](https://en.wikipedia.org/wiki/Standard_Commands_for_Programmable_Instruments)
commands. 

Currently explicity supported types are the Keysight N5700-series or Kepco
KLN power supply.  Other power supplies may work using the default
SCPI interface, but this is not guaranteed.

## Usage

The networked power supply is controlled using the `power` script:
```
$ ./power -H drts-pwr1 -t kepco status
Connected to drts-pwr1:5025
KEPCO KLN 80-9.5E
Power supply output is ON.
Voltage: 60.0 V
Current: 0.050 A
```

Basic output control, voltage control, and status have shortcut
commands. Raw SCPI commands can also be issued.  See `./power -h` for full
usage. 

## Site Configuration

For static site configuration, it may be more convenient to specify the
power supply paramters in a configuration file.  An example file is
provided in `example.conf`.  The supply type, hostname, and (optionally)
port can be customized:

```
[supply]
type=Kepco
hostname=drts-pwr1
port=5025
```

The `power` script will automatically look for a file name *supply.conf*,
or one can be specified on the command line. To support multiple power
supplies, create a config file for each one and switch between them with
the command-line argument.

## Script customization

New power supply types can be supported by adding new types in
`power_supply.py`. The supply type can be added to the factory function
`PowerSupply()`, and then the appropriate subclass can contain any
vendor-specific customizations (special prompts, default port, etc.).  
