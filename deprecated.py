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