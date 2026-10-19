Reinforcement and Layout Example
================================

Requires an **MSE/SRW** project that already has at least one wall segment
and (preferably) a reinforcement library entry. Create a reinforcement through
the API if the project has none.

Code Snippet: Reinforcement Layout by Course
--------------------------------------------

::

   from rswall.RSWallModeler import RSWallModeler
   from rswall.Reinforcement import TYPE_GEOGRID
   import os
   import inspect

   current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))
   model_path = os.path.join(current_dir, "example_models", "ExampleModel.rswall")

   modeler = RSWallModeler(port=60067)
   wall = modeler.openFile(model_path)

   reinforcements = wall.getAllReinforcements()
   if reinforcements:
       reinf = reinforcements[0]
   else:
       reinf = wall.createReinforcement("Scripted Strip")
       reinf.setReinforcementType(TYPE_GEOGRID)

   walls = wall.listWalls()
   wall_name = walls[0]["wallName"]
   segment_name = wall.getWallDetails(wall_name)["segments"][0]["segmentName"]

   # Irregular per-layer courses: set apply_uniform_placement=False
   # (default is True to match the Reinforcement Layout dialog)
   wall.setReinforcementLayout(
       wall_name,
       segment_name,
       layout_length=5.0,
       default_reinforcement_name=reinf.name,
       layer_placement_type="BY_COURSE",
       layers=[
           {"reinforcementName": reinf.name, "length": 5.0, "numCoursesBelow": 0},
           {"reinforcementName": reinf.name, "length": 5.0, "numCoursesBelow": 2},
       ],
       apply_uniform_placement=False,
   )
   print(wall.getReinforcementLayoutDetails(wall_name, segment_name))

   wall.save()
   wall.close()
