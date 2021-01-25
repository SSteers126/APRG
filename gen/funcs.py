import os, sys
import math
# import direct.directbase.DirectStart
from panda3d.core import Filename

def rel_path(path="/src"):
    # Get the location of the 'py' file I'm running:
    mydir = os.path.abspath(sys.path[0])

    # Convert that to panda's unix-style notation.
    mydir = Filename.fromOsSpecific(mydir).getFullpath()

    return mydir + path

def maxsteercalc(wheelbase, turncircle, carwidth):
    return math.atan(wheelbase / (turncircle - carwidth))

def clamp(i, mn=0, mx=1):
    return min(max(i, mn), mx)

def smootherstep(x):
    clampx = clamp(x)
    return clampx * clampx * clampx * (clampx * (clampx * 6 - 15) + 10)

def steeringMultiplier(cur_speed=99, top_speed=100, max_turn=40, min_val=0.05):
    return clamp((((clamp(smootherstep(clamp(1-cur_speed/top_speed)), -max_turn, max_turn))*top_speed)/100), min_val, 1)

print(steeringMultiplier())

# print(maxsteercalc(2.46888, (10.39368/2), 1.8542))