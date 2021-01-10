import os, sys
import direct.directbase.DirectStart
from panda3d.core import Filename

def rel_path(path="/src"):
    # Get the location of the 'py' file I'm running:
    mydir = os.path.abspath(sys.path[0])

    # Convert that to panda's unix-style notation.
    mydir = Filename.fromOsSpecific(mydir).getFullpath()

    return mydir + path