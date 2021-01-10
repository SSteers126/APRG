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