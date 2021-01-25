import sys, os
from panda3d.core import Filename

PlayerCar = None

carObjects = []

startLine = None
checkpointObjects = []
lapNum = 0

AIThrottle = 0
AITurning = 0
AIBraking = 0

AITime = 0

currentGate = 0
currentLap = 0

AIResetCall = False


def rel_path(self, path="/src"):
    # Get the location of the 'py' file I'm running:
    dir = os.path.abspath(sys.path[0])

    # Convert that to panda's unix-style notation.
    dir = Filename.fromOsSpecific(dir).getFullpath()

    return dir + path