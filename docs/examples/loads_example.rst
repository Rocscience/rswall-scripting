Loads Example
=============

Download the :download:`ExampleModel.rswall <../example_models/ExampleModel.rswall>`
for this example. Wall / segment names in that file: ``Wall 1`` / ``Segment 1``.

Code Snippet: Line, Uniform, and Point Loads
--------------------------------------------

::

   from rswall.RSWallModeler import RSWallModeler
   import os
   import inspect

   current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))
   model_path = os.path.join(current_dir, "example_models", "ExampleModel.rswall")

   modeler = RSWallModeler(port=60067)
   wall = modeler.openFile(model_path)

   print(wall.getValidLoadDirections())
   print(wall.getValidLoadClassifications())

   line = wall.createLineLoad("Scripted Line Load")
   directions = wall.getValidLoadDirections()
   classifications = wall.getValidLoadClassifications()
   if directions:
       line.setDirection(directions[0])
   if classifications:
       line.setClassification(classifications[0])
   line.setMagnitude(10.0)
   line.setDepth(0.0)
   line.setHorizontalDistance(1.0)
   line.assignToSegment("Wall 1", "Segment 1")

   uniform = wall.createUniformLoad("Scripted Uniform Load")
   uniform.setMagnitude(5.0)

   point = wall.createPointLoad("Scripted Point Load")
   point.setMagnitude(25.0)

   for load in wall.getLoads():
       print(load.name, type(load).__name__)

   wall.save()
   wall.close()
