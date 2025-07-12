import time
import cflib.crtp
from cflib.crazyflie import Crazyflie

cflib.crtp.init_drivers(enable_debug_driver=False)
cf = Crazyflie()
cf.open_link("radio://0/80/2M")  # Connect to Crazyflie

def execute_command(command):
    if "takeoff" in command:
        cf.commander.send_hover_setpoint(0, 0, 0, 0.5)
    elif "wait" in command:
        time.sleep(float(command.split()[1]))
    elif "fly" in command:
        _, direction, value = command.split()
        move = {"F": (1, 0, 0), "B": (-1, 0, 0), "L": (0, -1, 0), "R": (0, 1, 0), "U": (0, 0, 1), "D": (0, 0, -1)}
        x, y, z = move[direction]
        cf.commander.send_hover_setpoint(x * float(value), y * float(value), 0, z * float(value))
    elif "land" in command:
        cf.commander.send_hover_setpoint(0, 0, 0, 0)

