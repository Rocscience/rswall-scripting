Soil Assignment and Topography Example
======================================

Download the :download:`ExampleModel.rswall <../example_models/ExampleModel.rswall>`
for this example. Wall / segment names: ``Wall 1`` / ``Segment 1``.

Code Snippet: Soil Regions and Backslope Topography
---------------------------------------------------

::

   from rswall.RSWallModeler import RSWallModeler
   from rswall.SoilTopography import infinite_topography, broken_topography
   import os
   import inspect

   current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))
   model_path = os.path.join(current_dir, "example_models", "ExampleModel.rswall")

   modeler = RSWallModeler(port=60067)
   wall = modeler.openFile(model_path)

   wall_name = "Wall 1"
   segment_name = "Segment 1"

   regions = wall.getValidSoilRegionNames(wall_name, segment_name)
   print("Regions:", regions)
   print(wall.getSegmentSoilAssignments(wall_name, segment_name))

   materials = wall.getAllMaterials()
   if materials and regions:
       wall.assignSoilToRegion(wall_name, segment_name, regions[0], materials[0])

   wall.setBackslopeTopography(
       wall_name, segment_name, infinite_topography(10.0)
   )
   print(wall.getBackslopeTopography(wall_name, segment_name))

   wall.setBackslopeTopography(
       wall_name, segment_name, broken_topography(2.0, 2.0, slope_angle_degrees=20.0)
   )
   print(wall.getBackslopeTopography(wall_name, segment_name)["terrainType"])

   wall.save()
   wall.close()
