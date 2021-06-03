#!/usr/bin/env python3

from pydsfapi.connections import CommandConnection


class Mcode:
    def __init__(self, code, param=False, timeout=4, desc="missing"):
        self.code = code
        self.param = param
        self.desc = desc

    def print(self):
        print("M{code} '{desc}' ".format(code=self.code, desc=self.desc))

    def send(self, conn):
        return conn.perform_simple_code("M{}".format(self.code))


mcodes = [
    Mcode(code=0, desc="Stop"),
    Mcode(code=1, desc="Sleep"),
    Mcode(code=3, desc="Spin spindle clockwise"),
    Mcode(code=4, desc="Spin spindle counter clockwise"),
    Mcode(code=5, desc="Spindle motor off"),
    Mcode(code=17, desc="Motors on"),
    Mcode(code=18, desc="Motors off"),
    Mcode(code=20, desc="List files on SD card"),
    Mcode(code=21, desc="Initialise SD card"),
    Mcode(code=22, desc="Release SD card"),
    Mcode(code=23, desc="Set file to print"),
    Mcode(code=24, desc="Print/resume-printing the selected file"),
    Mcode(code=25, desc="Pause the print"),
    Mcode(code=26, desc="Set SD position"),
    Mcode(code=27, desc="Report print status - Deprecated"),
    Mcode(code=28, desc="Write to file"),
    Mcode(code=29, desc="End of file being written; should be intercepted before getting here"),
    Mcode(code=30, desc="Delete file"),
    Mcode(code=32, desc="Select file and start SD print"),
    Mcode(code=36, desc="Return file information"),
    Mcode(code=37, desc="Simulation mode on/off, or simulate a whole file"),
    Mcode(code=38, desc="Report SHA1 of file"),
    Mcode(code=39, desc="Return SD card info"),
    Mcode(code=42, desc="Turn an output pin on or off"),
    Mcode(code=73, desc="Slicer-inserted print time values"),
    Mcode(code=80, desc="ATX power on"),
    Mcode(code=81, desc="ATX power off"),
    Mcode(code=82, desc="Use absolute extruder positioning"),
    Mcode(code=83, desc="Use relative extruder positioning"),
    Mcode(code=84),
    Mcode(code=85, desc="Set inactive time"),
    Mcode(code=92, desc="Set/report steps/mm for some axes"),
    Mcode(code=98, desc="Call Macro/Subprogram"),
    Mcode(code=99, desc="Return from Macro/Subprogram"),
    Mcode(code=101, desc="Un-retract, generated by S3D if 'Include M101/101/103' is enabled"),
    Mcode(code=102),
    Mcode(code=103, desc="Retract, generated by S3D if 'Include M101/101/103' is enabled"),
    Mcode(code=104),
    Mcode(code=105, desc="Get temperatures"),
    Mcode(code=106, desc="Set/report fan values"),
    Mcode(code=107, desc="Fan off - deprecated"),
    Mcode(code=108, desc="Cancel waiting for temperature"),
    Mcode(code=109, desc="Deprecated in RRF, but widely generated by slicers"),
    Mcode(code=110, desc="Set line numbers"),
    Mcode(code=111, desc="Debug level"),
    Mcode(code=112, desc="Emergency stop - acted upon in Webserver, but also here in case it comes from USB etc."),
    Mcode(code=114),
    Mcode(code=115, desc="Print firmware version or set hardware type"),
    Mcode(code=116, desc="Wait for set temperatures"),
    Mcode(code=117, desc="Display message"),
    Mcode(code=118, desc="Echo message on host"),
    Mcode(code=119),
    Mcode(code=120),
    Mcode(code=121),
    Mcode(code=122),
    Mcode(code=140, desc="Bed temperature"),
    Mcode(code=141, desc="Chamber temperature"),
    Mcode(code=143, desc="Configure heater protection"),
    Mcode(code=144, desc="Set bed to standby, or to active if S1 parameter given"),
    Mcode(code=150),
    Mcode(code=190, desc="Set bed temperature and wait"),
    Mcode(code=191, desc="Set chamber temperature and wait"),
    Mcode(code=200, desc="Set filament diameter for volumetric extrusion and enable/disable volumetric extrusion"),
    Mcode(code=201, desc="Set/print axis accelerations"),
    Mcode(code=203, desc="Set/print minimum/maximum feedrates"),
    Mcode(code=204, desc="Set max travel and printing accelerations"),
    Mcode(code=205, desc="Set/print maximum jerk speeds in mm/sec"),
    Mcode(code=206, desc="Offset axes"),
    Mcode(code=207, desc="Set firmware retraction details"),
    Mcode(code=208, desc="Set/print maximum axis lengths. If there is an S parameter with value 1 then we set the min value, else we set the max value."),
    Mcode(code=220, desc="Set/report speed factor override percentage"),
    Mcode(code=221, desc="Set/report extrusion factor override percentage"),
    Mcode(code=226, desc="Synchronous pause, normally initiated from within the file being printed"),
    Mcode(code=260, desc="I2C send"),
    Mcode(code=261, desc="I2C send"),
    Mcode(code=280, desc="Servos"),
    Mcode(code=290, desc="Baby stepping"),
    Mcode(code=291, desc="Display message, optionally wait for acknowledgement"),
    Mcode(code=292, desc="Acknowledge message"),
    Mcode(code=300, desc="Beep"),
    Mcode(code=301, desc="Set/report hot end PID values"),
    Mcode(code=302, desc="Allow, deny or report cold extrudes and configure minimum extrusion/retraction temps"),
    Mcode(code=303, desc="Run PID tuning"),
    Mcode(code=304, desc="Set/report heated bed PID values"),
    Mcode(code=305, desc="Set/report specific heater parameters"),
    Mcode(code=307, desc="Set heater process model parameters"),
    Mcode(code=308),
    Mcode(code=350, desc="Set/report microstepping"),
    Mcode(code=374, desc="Save grid and height map to file"),
    Mcode(code=375, desc="Load grid and height map from file and enable compensation"),
    Mcode(code=376, desc="Set taper height"),
    Mcode(code=400, desc="Wait for current moves to finish"),
    Mcode(code=401, desc="Deploy Z probe"),
    Mcode(code=402, desc="Retract Z probe"),
    Mcode(code=404, desc="Filament width and nozzle diameter"),
    Mcode(code=408, desc="Get status in JSON format"),
    Mcode(code=409, desc="Get object model values in JSON format"),
    Mcode(code=450, desc="Report printer mode"),
    Mcode(code=451, desc="Select FFF printer mode"),
    Mcode(code=452, desc="Select laser mode"),
    Mcode(code=453, desc="Select CNC mode"),
    Mcode(code=470, desc="mkdir"),
    Mcode(code=471, desc="move/rename file/directory"),
    Mcode(code=486, desc="number object or cancel object"),
    Mcode(code=500, desc="Store parameters in config-override.g"),
    Mcode(code=501, desc="Load parameters from config-override.g"),
    Mcode(code=502, desc="Revert to default 'factory settings' ignoring values in config-override.g"),
    Mcode(code=503, desc="List variable settings"),
    Mcode(code=505, desc="set sys folder"),
    Mcode(code=540, desc="Set/report MAC address"),
    Mcode(code=550, desc="Set/report machine name"),
    Mcode(code=551, desc="Set password (no option to report it)"),
    Mcode(code=552, desc="Enable/Disable network and/or Set/Get IP address"),
    Mcode(code=553, desc="Set/Get netmask"),
    Mcode(code=554, desc="Set/Get gateway"),
    Mcode(code=555, desc="Set/report firmware type to emulate"),
    Mcode(code=556, desc="Axis compensation (we support only X, Y, Z)"),
    Mcode(code=557, desc="Set/report Z probe point coordinates"),
    Mcode(code=558, desc="Set or report Z probe type and for which axes it is used"),
    Mcode(code=559),
    Mcode(code=560, desc="Binary writing"),
    Mcode(code=561, desc="Set identity transform and disable height map"),
    Mcode(code=562, desc="Reset temperature fault - use with great caution"),
    Mcode(code=563, desc="Define tool"),
    Mcode(code=564, desc="Think outside the box?"),
    Mcode(code=566, desc="Set/print maximum jerk speeds in mm/min"),
    Mcode(code=567, desc="Set/report tool mix ratios"),
    Mcode(code=568, desc="Tool Settings"),
    Mcode(code=569, desc="Set/report axis direction"),
    Mcode(code=570, desc="Set/report heater monitoring"),
    Mcode(code=571, desc="Set output on extrude"),
    Mcode(code=572, desc="Set/report pressure advance"),
    Mcode(code=573, desc="Report heater average PWM"),
    Mcode(code=574, desc="Set endstop configuration"),
    Mcode(code=575, desc="Set communications parameters"),
    Mcode(code=577, desc="Wait until endstop input is triggered"),
    Mcode(code=578, desc="Fire Inkjet bits"),
    Mcode(code=579, desc="Scale Cartesian axes (mostly for Delta configurations)"),
    Mcode(code=580, desc="(De)Select Roland mill"),
    Mcode(code=581, desc="Configure external trigger"),
    Mcode(code=582, desc="Check external trigger"),
    Mcode(code=584, desc="Set axis/extruder to stepper driver(s) mapping"),
    Mcode(code=585, desc="Probe Tool"),
    Mcode(code=586, desc="Configure network protocols"),
    Mcode(code=587, desc="Add WiFi network or list remembered networks"),
    Mcode(code=588, desc="Forget WiFi network"),
    Mcode(code=589, desc="Configure access point"),
    Mcode(code=591, desc="Configure filament sensor"),
    Mcode(code=592, desc="Configure nonlinear extrusion"),
    Mcode(code=593, desc="Configure dynamic ringing cancellation"),
    Mcode(code=594, desc="Enter or leave height following mode"),
    Mcode(code=595, desc="Configure movement queue s")
]


def list_all():
    for entry in mcodes:
        entry.print()


def send_all():
    conn = CommandConnection(debug=True)
    conn.connect()
    print("opened connection")

    for entry in mcodes:
        try:
            entry.send(conn)
        except TimeoutError as error:
            print("Warning: {}".format(error))
            break
        except Exception as error:
            print("Error: {}".format(error))
            break

    conn.close()
    print("closed connection")


if __name__ == "__main__":
    list_all()
    send_all()
