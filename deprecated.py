# # car = loader.loadModel(str(dir_path) + "\\" + str(Path("src/models/cars/Zonda R.bam")))
# self.car = loader.loadModel(self.rel_path("/src/models/cars/Supra obj WT custom glass.bam"))
# self.car.setTwoSided(True)
# self.car.setHpr(90, 0, 0)
# # windowmat = self.car.findMaterial("Object Glass | Colored")
# # windowmat.set_alpha_scale(.5)
# # car = loader.loadModel(("/d/P3d/NP/src/models/cars/Zonda R.egg"))
# posInterval1 = self.car.posInterval(5,
#                                     Point3(0, -10, 0),
#                                     startPos=Point3(0, 10, 0))
# posInterval2 = self.car.posInterval(5,
#                                     Point3(0, 10, 0),
#                                     startPos=Point3(0, -10, 0))
# hprInterval1 = self.car.hprInterval(1,
#                                     Point3(270, 0, 0),
#                                     startHpr=Point3(90, 0, 0))
# hprInterval2 = self.car.hprInterval(1,
#                                     Point3(90, 0, 0),
#                                     startHpr=Point3(270, 0, 0))
#
# # Create and play the sequence that coordinates the intervals.
# self.carloop = Sequence(posInterval1, hprInterval1,
#                         posInterval2, hprInterval2,
#                         name="pandaPace")
# self.carloop.loop()
#
# # self.car.setAttrib(self.lowPassFilter)
# self.car.reparentTo(render)

<<<<<<< Updated upstream
# self.accept("w", self.accelerate)
# self.accept("w-repeat", self.accelerate)
# self.accept("w-up", self.noaccelerate)
#
# self.accept("s", self.brake)
# self.accept("s-repeat", self.brake)
# self.accept("s-up", self.nobrake)
#
# self.accept("a", self.turnleft)
# self.accept("a-repeat", self.turnleft)
# self.accept("a-up", self.nosteermethod)
#
# self.accept("d", self.turnright)
# self.accept("d-repeat", self.turnright)
# self.accept("d-up", self.nosteermethod)
#
# self.accept(".", self.doExit)


# debugNode = BulletDebugNode('Debug')
# debugNode.showWireframe(True)
# debugNode.showConstraints(True)
# debugNode.showBoundingBoxes(False)
# debugNode.showNormals(False)
# debugNP = render.attachNewNode(debugNode)
# debugNP.show()
#
# world = BulletWorld()
# world.setGravity(Vec3(0, 0, -9.81))
# self.world.setDebugNode(debugNP.node())


# Chassis body
# shape = BulletBoxShape(Vec3(0.7, 1.5, 0.5))
=======

# self.forward_button = forward_button
# self.left_button = left_button
# self.right_button = right_button
# self.brake_button = brake_button
# self.reverse_button = reverse_button

# self.hitbox_shape = BulletBoxShape(Vec3(1, 2.2, 0.55))
# self.ts = TransformState.makePos(Point3(0, 0, 0.75))

# self.chassisNP = render.attachNewNode(BulletRigidBodyNode("Car"))
# self.chassisNP.node().addShape(self.hitbox_shape, self.ts)
# self.chassisNP.setPos(0, 0, 0)
# self.chassisNP.node().setMass(1520)
# self.chassisNP.node().setDeactivationEnabled(False)
# self.world.attachRigidBody(self.chassisNP.node())

# Chassis geometry
# loader.loadModel(globals.rel_path(None, path="/src/models/cars/Supra Body ReScale rotate Nglass.bam")).reparentTo(
#     self.chassisNP)

# Vehicle

# self.vehicle = BulletVehicle(self.world, self.chassisNP.node())
# self.vehicle.setCoordinateSystem(ZUp)
# self.world.attachVehicle(self.vehicle)
# globals.carObjects.append(self.vehicle)

# self.LFwheelNP = loader.loadModel(globals.rel_path(None, "/src/models/cars/Supra Wheel L RS.bam"))
# self.LFwheelNP.reparentTo(render)

# self.RFwheelNP = loader.loadModel(globals.rel_path(None, "/src/models/cars/Supra Wheel R RS.bam"))
# self.RFwheelNP.reparentTo(render)

# self.LBwheelNP = loader.loadModel(globals.rel_path(None, "/src/models/cars/Supra Wheel L RS.bam"))
# self.LBwheelNP.reparentTo(render)

# self.RBwheelNP = loader.loadModel(globals.rel_path(None, "/src/models/cars/Supra Wheel R RS.bam"))
# self.RBwheelNP.reparentTo(render)

# front_wheel_distance = (0.9, 1.35, 0.65)
# rear_wheel_distance = (0.9, 1.25, 0.65)
#
# self.LFwheel = self.addWheel(Point3(0.9, 1.35, 0.65), True, self.LFwheelNP)
# self.RFwheel = self.addWheel(Point3(-0.9, 1.35, 0.65), True, self.RFwheelNP)
# self.LBwheel = self.addWheel(Point3(0.9, -1.25, 0.65), False, self.LBwheelNP)
# self.RBwheel = self.addWheel(Point3(-0.9, -1.25, 0.65), False, self.RBwheelNP)

# self.LFwheel = self.addWheel(Point3(front_wheel_distance[0]+.05, front_wheel_distance[1], front_wheel_distance[2]), True, self.LFwheelNP)
# self.RFwheel = self.addWheel(Point3(-front_wheel_distance[0], front_wheel_distance[1], front_wheel_distance[2]), True, self.RFwheelNP)
# self.LBwheel = self.addWheel(Point3(rear_wheel_distance[0]+.05, -rear_wheel_distance[1], rear_wheel_distance[2]), False, self.LBwheelNP)
# self.RBwheel = self.addWheel(Point3(-rear_wheel_distance[0], -rear_wheel_distance[1], rear_wheel_distance[2]), False, self.RBwheelNP)


# self.trackNP.set
# visNP
# self.trackNP.node().setIntoCollideMask(BitMask32(0x0))

# bodyNPs = BulletHelper.fromCollisionSolids(visNP, True)
# print(bodyNPs)
# print(type(bodyNPs))
# self.ballNP = bodyNPs[0]


# self.world.attachRigidBody(self.trackNP)

# self.ghostShape = BulletBoxShape(Vec3(1, 1, 1))
#
# self.ghost = BulletGhostNode('Ghost')
# self.ghost.addShape(self.ghostShape)
#
# self.ghostNP = render.attachNewNode(self.ghost)
# self.ghostNP.setPos(0, 10, 0.5)
# self.ghostNP.setCollideMask(BitMask32(0x0f))
#
# self.world.attachGhost(self.ghost)

# # Directional light 02
# directionalLight = DirectionalLight("HeadlightL")
# directionalLight.setColorTemperature(6250)
# # directionalLight.setColor((0.2, 0.2, 0.8, 1))
# directionalLightNP = render.attachNewNode(directionalLight)
# # This light is facing forwards, away from the camera.
# directionalLightNP.setHpr(0, -20, 0)
# render.setLight(directionalLightNP)
>>>>>>> Stashed changes
