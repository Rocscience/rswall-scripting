Leveling Pad and Base Strength Example
======================================

Leveling pad APIs are typically used on MSE/SRW segments. Base strength APIs
apply to gravity (and related) segments. Adjust the project type as needed.

Code Snippet: Leveling Pad and Bearing Capacity
-----------------------------------------------

::

   from rswall.RSWallModeler import RSWallModeler
   import os
   import inspect

   current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))
   model_path = os.path.join(current_dir, "example_models", "ExampleModel.rswall")

   modeler = RSWallModeler(port=60067)
   wall = modeler.openFile(model_path)

   walls = wall.listWalls()
   wall_name = walls[0]["wallName"]
   segment_name = wall.getWallDetails(wall_name)["segments"][0]["segmentName"]

   # Leveling pad (MSE/SRW segments)
   wall.setLevelingPadEnabled(wall_name, segment_name, True)
   wall.setLevelingPadDepth(wall_name, segment_name, 0.15)
   wall.setLevelingPadWidth(wall_name, segment_name, 0.6)
   wall.setLevelingPadSetback(wall_name, segment_name, 0.08)
   print(wall.getLevelingPadDetails(wall_name, segment_name))

   # Base strength — value is project-native stress (parameter name is historical)
   wall.setUserSpecifiedBearingCapacity(wall_name, segment_name, 275.0)
   print(wall.getSegmentBaseStrength(wall_name, segment_name))
   print(wall.getValidBaseStrengthOptions())

   wall.save()
   wall.close()
