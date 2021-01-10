## These run an old rendering version - should not be needed, but are here incase it is required for some functionality etc
# import direct.directbase.DirectStart
# from direct.showbase.DirectObject import DirectObject

# Libraries for backend path conversion
import sys,os

from direct.showbase.ShowBaseGlobal import globalClock
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import Filename
from pathlib import Path

# import panda3d

# Basic imports required for the window, materials on objects, and HUD
from direct.showbase.ShowBase import ShowBase
from panda3d.core import PerspectiveLens
from panda3d.core import NodePath
from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import PointLight, Spotlight
from panda3d.core import AlphaTestAttrib, RenderAttrib, TransparencyAttrib
from panda3d.core import TextNode
from panda3d.core import Material
from panda3d.core import LVector3, Vec3
from direct.gui.OnscreenText import OnscreenText

# Libraries that will probably be used for manipulation of objects
import math
import sys
import colorsys
# Libraries for animated objects

from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence

# Physics engine and other libraries for cars/maps
from panda3d.core import Point3
from panda3d.bullet import BulletBoxShape, BulletRigidBodyNode, BulletVehicle, BulletWorld, ZUp
from panda3d.core import TransformState

# Threading similar to standard pythonic threading
from panda3d.core import Thread
print(Thread.isThreadingSupported())

# from gen.funcs import rel_path

# Simple function to keep a value in a given range (by default 0 to 1)
def clamp(i, mn=0, mx=1):
    return min(max(i, mn), mx)


class MainWindow(ShowBase):

    def rel_path(self, path="/src"):
        # Get the location of the 'py' file I'm running:
        dir = os.path.abspath(sys.path[0])

        # Convert that to panda's unix-style notation.
        dir = Filename.fromOsSpecific(dir).getFullpath()

        return dir + path

    # Macro-like function to reduce the amount of code needed to create the
    # onscreen instructions
    def makeStatusLabel(self, i):
        return OnscreenText(
            parent=base.a2dTopLeft, align=TextNode.ALeft,
            style=1, fg=(1, 1, 0, 1), shadow=(0, 0, 0, .4),
            pos=(0.06, -0.1 -(.06 * i)), scale=.05, mayChange=True)
    
    def convZUp(self, x, y, z):
        return (x, -z, y)

    def addWheel(self, pos, isfrontwheel, np):
        wheel = self.vehicle.createWheel()

        wheel.setNode(np.node())
        wheel.setChassisConnectionPointCs(pos)
        wheel.setFrontWheel(isfrontwheel)

        wheel.setWheelDirectionCs(Vec3(0, 0, -1))
        wheel.setWheelAxleCs(Vec3(1, 0, 0))
        wheel.setWheelRadius(0.25)
        wheel.setMaxSuspensionTravelCm(10.0)

        wheel.setSuspensionStiffness(40.0)
        wheel.setWheelsDampingRelaxation(2.3)
        wheel.setWheelsDampingCompression(4.4)
        wheel.setFrictionSlip(100.0)
        wheel.setRollInfluence(0.1)

    def __init__(self):
        # Initialize the ShowBase class from which we inherit, which will
        # create a window and set up everything we need for rendering into it.
        ShowBase.__init__(self)
        dir_path = Path(sys.path[0])

        # Directional light 02
        directionalLight = DirectionalLight('directionalLight')
        directionalLight.setColorTemperature(6250)
        # directionalLight.setColor((0.2, 0.2, 0.8, 1))
        directionalLightNP = render.attachNewNode(directionalLight)
        # This light is facing forwards, away from the camera.
        directionalLightNP.setHpr(0, -20, 0)
        render.setLight(directionalLightNP)

        self.lowPassFilter = AlphaTestAttrib.make(TransparencyAttrib.MDual, 0.5)

        self.world = BulletWorld()
        # Chassis body
        # shape = BulletBoxShape(Vec3(0.7, 1.5, 0.5))
        self.shape = BulletBoxShape(Vec3(1.65, 1.29, 4.0))
        self.ts = TransformState.makePos(Point3(0, 0, 0.5))

        self.chassisNP = render.attachNewNode(BulletRigidBodyNode('Car'))
        self.chassisNP.node().addShape(self.shape, self.ts)
        self.chassisNP.setPos(0, 0, 0)
        self.chassisNP.node().setMass(1520.0)
        self.chassisNP.node().setDeactivationEnabled(False)

        self.world.attachRigidBody(self.chassisNP.node())

        # Chassis geometry
        loader.loadModel(self.rel_path("/src/models/cars/Supra Body ReScale.bam")).reparentTo(self.chassisNP)

        # Vehicle
        self.vehicle = BulletVehicle(self.world, self.chassisNP.node())
        self.vehicle.setCoordinateSystem(ZUp)
        self.world.attachVehicle(self.vehicle)

        self.LFwheelNP = loader.loadModel(self.rel_path("/src/models/cars/Supra Wheel LF ReScale.bam"))
        self.LFwheelNP.reparentTo(render)

        self.RFwheelNP = loader.loadModel(self.rel_path("/src/models/cars/Supra Wheel RF ReScale.bam"))
        self.RFwheelNP.reparentTo(render)

        self.LBwheelNP = loader.loadModel(self.rel_path("/src/models/cars/Supra Wheel LB ReScale.bam"))
        self.LBwheelNP.reparentTo(render)

        self.RBwheelNP = loader.loadModel(self.rel_path("/src/models/cars/Supra Wheel RB ReScale.bam"))
        self.RBwheelNP.reparentTo(render)
        # (0.79, -1.35, 0)
        self.LFwheel = self.addWheel(Point3(0, 0, 0.35), True, self.LFwheelNP)
        self.RFwheel = self.addWheel(Point3(0, 0, 0.35), True, self.RFwheelNP)
        self.LBwheel = self.addWheel(Point3(0, 0, 0.35), False, self.LBwheelNP)
        self.RBwheel = self.addWheel(Point3(0, 0, 0.35), False, self.RBwheelNP)

        ## TODO: coord system - xpositive = right, ypositive = back, zpositive = up
        # self.LFwheel = self.vehicle.createWheel()
        # self.LFwheel.setNode(self.LFwheelNP.node())
        # self.LFwheel.setChassisConnectionPointCs(Point3(0, 0, 0.4))
        # self.LFwheel.setFrontWheel(True)
        #
        # self.LFwheel.setWheelDirectionCs(Vec3(0, 0, -1))
        # self.LFwheel.setWheelAxleCs(Vec3(1, 0, 0))
        # self.LFwheel.setWheelRadius(0.25)
        # self.LFwheel.setMaxSuspensionTravelCm(10.0)
        #
        # self.LFwheel.setSuspensionStiffness(40.0)
        # self.LFwheel.setWheelsDampingRelaxation(2.3)
        # self.LFwheel.setWheelsDampingCompression(4.4)
        # self.LFwheel.setFrictionSlip(100.0)
        # self.LFwheel.setRollInfluence(0.1)

        # Use a 512x512 resolution shadow map
        directionalLight.setShadowCaster(True, 512, 512)
        # Enable the shader generator for the receiving nodes
        render.setShaderAuto()

        # Update
        def update(task):
            dt = globalClock.getDt()
            self.world.doPhysics(dt)
            return task.cont

        taskMgr.add(update, 'update')


if __name__ == '__main__':
    # Make an instance of our class and run the demo
    app = MainWindow()
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
