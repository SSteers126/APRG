## These run an old rendering version - should not be needed, but are here incase it is required for some functionality etc
# import direct.directbase.DirectStart
# from direct.showbase.DirectObject import DirectObject

# Libraries for backend path conversion
import sys,os

from direct.showbase.InputStateGlobal import inputState
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
from panda3d.bullet import BulletDebugNode, BulletBoxShape, BulletRigidBodyNode, BulletVehicle, BulletWorld, ZUp, \
    BulletPlaneShape
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


    def update(self, task):
        dt = globalClock.getDt()
        self.world.doPhysics(dt, 10, 0.008)
        return task.cont

    def accelerate(self):
        self.vehicle.applyEngineForce(1000, 1)
        self.vehicle.applyEngineForce(1000, 0)

    def noaccelerate(self):
        self.vehicle.applyEngineForce(0, 1)
        self.vehicle.applyEngineForce(0, 0)

    def brake(self):
        self.vehicle.setBrake(100, 0)
        self.vehicle.setBrake(100, 1)
        self.vehicle.setBrake(100, 2)
        self.vehicle.setBrake(100, 3)

    def nobrake(self):
        self.vehicle.setBrake(0, 0)
        self.vehicle.setBrake(0, 1)
        self.vehicle.setBrake(0, 2)
        self.vehicle.setBrake(0, 3)

    def turnleft(self):
        self.steering += globalClock.getDt() * self.steeringIncrement
        self.steering = min(self.steering, self.steeringClamp)
        self.vehicle.setSteeringValue(self.steering, 2)
        self.vehicle.setSteeringValue(self.steering, 3)


    def turnright(self):
        self.steering -= globalClock.getDt() * self.steeringIncrement
        self.steering = max(self.steering, -self.steeringClamp)
        self.vehicle.setSteeringValue(self.steering, 2)
        self.vehicle.setSteeringValue(self.steering, 3)

    def __init__(self):
        # Initialize the ShowBase class from which we inherit, which will
        # create a window and set up everything we need for rendering into it.
        ShowBase.__init__(self)
        dir_path = Path(sys.path[0])

        # Plane
        self.worldNP = render.attachNewNode('World')
        shape = BulletPlaneShape(Vec3(0, 0, 1), 0)

        np = self.worldNP.attachNewNode(BulletRigidBodyNode('Ground'))
        np.node().addShape(shape)
        np.setPos(0, 0, -1)

        # np.setCollideMask(BitMask32.allOn())

        # Steering info
        self.steering = 0.0  # degrees
        self.steeringClamp = 45.0  # degrees
        self.steeringIncrement = 120.0  # degrees per second

        base.cam.setPos(0, -10, 4)
        base.cam.lookAt(0, 0, 0)

        # Directional light 02
        directionalLight = DirectionalLight('directionalLight')
        directionalLight.setColorTemperature(6250)
        # directionalLight.setColor((0.2, 0.2, 0.8, 1))
        directionalLightNP = render.attachNewNode(directionalLight)
        # This light is facing forwards, away from the camera.
        directionalLightNP.setHpr(0, -20, 0)
        render.setLight(directionalLightNP)

        self.lowPassFilter = AlphaTestAttrib.make(TransparencyAttrib.MDual, 0.5)

        self.debugNP = self.worldNP.attachNewNode(BulletDebugNode('Debug'))
        self.debugNP.show()
        self.world = BulletWorld()
        self.world.setDebugNode(self.debugNP.node())
        self.world.attachRigidBody(np.node())
        self.world.setGravity(Vec3(0, 0, -9.81))
        # Chassis body
        # shape = BulletBoxShape(Vec3(0.7, 1.5, 0.5))
        self.shape = BulletBoxShape(Vec3(1, 2.2, 0.55))
        self.ts = TransformState.makePos(Point3(0, 0, 0.75))

        self.chassisNP = render.attachNewNode(BulletRigidBodyNode('Car'))
        self.chassisNP.node().addShape(self.shape, self.ts)
        self.chassisNP.setPos(0, 0, 0)
        self.chassisNP.node().setMass(1520.0)
        self.chassisNP.node().setDeactivationEnabled(False)

        self.world.attachRigidBody(self.chassisNP.node())

        # Chassis geometry
        loader.loadModel(self.rel_path("/src/models/cars/Supra Body ReScale rotate.bam")).reparentTo(self.chassisNP)

        # Vehicle
        self.vehicle = BulletVehicle(self.world, self.chassisNP.node())
        self.vehicle.setCoordinateSystem(ZUp)
        self.world.attachVehicle(self.vehicle)

        self.LFwheelNP = loader.loadModel(self.rel_path("/src/models/cars/Supra Wheel L RS.bam"))
        self.LFwheelNP.reparentTo(render)

        self.RFwheelNP = loader.loadModel(self.rel_path("/src/models/cars/Supra Wheel R RS.bam"))
        self.RFwheelNP.reparentTo(render)

        self.LBwheelNP = loader.loadModel(self.rel_path("/src/models/cars/Supra Wheel L RS.bam"))
        self.LBwheelNP.reparentTo(render)

        self.RBwheelNP = loader.loadModel(self.rel_path("/src/models/cars/Supra Wheel R RS.bam"))
        self.RBwheelNP.reparentTo(render)
        # (0.79, -1.35, 0)
        # Vec3(1, 2.2, 0.55)
        self.LFwheel = self.addWheel(Point3(0.9, -1.35, 0.65), True, self.LFwheelNP)
        self.RFwheel = self.addWheel(Point3(-0.9, -1.35, 0.65), True, self.RFwheelNP)
        self.LBwheel = self.addWheel(Point3(0.9, 1.35, 0.65), False, self.LBwheelNP)
        self.RBwheel = self.addWheel(Point3(-0.9, 1.35, 0.65), False, self.RBwheelNP)

        # debugNode = BulletDebugNode('Debug')
        # debugNode.showWireframe(True)
        # debugNode.showConstraints(True)
        # debugNode.showBoundingBoxes(False)
        # debugNode.showNormals(False)
        # debugNP = render.attachNewNode(debugNode)
        # debugNP.show()

        # world = BulletWorld()
        # world.setGravity(Vec3(0, 0, -9.81))
        # self.world.setDebugNode(debugNP.node())

        ## TODO: coord system - xpositive = right, ypositive = back, zpositive = up

        self.accept("w-repeat", self.accelerate)
        self.accept("w", self.accelerate)
        self.accept("w-up", self.noaccelerate)
        self.accept("s-repeat", self.brake)
        self.accept("s", self.brake)
        self.accept("s-up", self.nobrake)
        self.accept("a-repeat", self.turnleft)
        self.accept("a", self.turnleft)
        # self.accept("a-up", self.nobrake)
        self.accept("d-repeat", self.turnright)
        self.accept("d", self.turnright)
        # self.accept("d-up", self.nobrake)

        # Use a 512x512 resolution shadow map
        directionalLight.setShadowCaster(True, 512, 512)
        # Enable the shader generator for the receiving nodes
        render.setShaderAuto()


        # Update


        taskMgr.add(self.update, 'update')


if __name__ == '__main__':
    # Make an instance of our class and run the demo
    app = MainWindow()
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
