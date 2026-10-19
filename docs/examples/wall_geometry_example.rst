Wall Geometry Example
=====================

Download the :download:`ExampleModel.rswall <../example_models/ExampleModel.rswall>`
for this example.

Code Snippet: List Walls and Segments
-------------------------------------

::

   from rswall.RSWallModeler import RSWallModeler
   import os
   import inspect

   current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))
   model_path = os.path.join(current_dir, "example_models", "ExampleModel.rswall")

   modeler = RSWallModeler(port=60067)
   wall = modeler.openFile(model_path)

   for entry in wall.listWalls():
       name = entry["wallName"]
       details = wall.getWallDetails(name)
       print(name, details.get("segments"))

   # Create a single-segment gravity wall when a gravity profile exists
   profiles = wall.getAllGravityWallProfiles()
   if profiles:
       created = wall.createSingleSegmentWall(profiles[0].name, "Scripted Wall")
       print(created)
       wall.setSegmentTopElevation(
           created["wallName"], created["segmentName"], 3.0
       )

   wall.save()
   wall.close()
