Groundwater Example
===================

Download the :download:`ExampleModel.rswall <../example_models/ExampleModel.rswall>`
for this example. Wall / segment names: ``Wall 1`` / ``Segment 1``.

Code Snippet: Segment Groundwater
---------------------------------

::

   from rswall.RSWallModeler import RSWallModeler
   import os
   import inspect

   current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))
   model_path = os.path.join(current_dir, "example_models", "ExampleModel.rswall")

   modeler = RSWallModeler(port=60067)
   wall = modeler.openFile(model_path)

   wall_name = "Wall 1"
   segment_name = "Segment 1"

   before = wall.getGroundwater(wall_name, segment_name)
   print(before)

   # Payload keys use project-native length; *Meters wire names are historical aliases
   wall.setGroundwater(
       wall_name,
       segment_name,
       {
           "isGroundwaterEnabled": True,
           "isFrontFaceWtDefined": False,
           "elevWtConstantMeters": 1.0,
       },
   )
   print(wall.getGroundwater(wall_name, segment_name))

   wall.save()
   wall.close()
