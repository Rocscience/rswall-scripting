Gravity Wall Profile Example
============================

Download the :download:`ExampleModel.rswall <../example_models/ExampleModel.rswall>`
for this example (or any project that accepts gravity section profiles).

Code Snippet: Gravity Profile Library
-------------------------------------

::

   from rswall.RSWallModeler import RSWallModeler
   from rswall.GravityWallProfile import GRAVITY_DIMENSION_NAMES
   import os
   import inspect

   current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))
   model_path = os.path.join(current_dir, "example_models", "ExampleModel.rswall")

   modeler = RSWallModeler(port=60067)
   wall = modeler.openFile(model_path)

   profile = wall.createGravityWallProfile("Scripted Gravity Profile")
   print(GRAVITY_DIMENSION_NAMES)

   profile.setUnitWeight(21.5)
   profile.setElevationAtToe(0.5)
   profile.setDimension("b1", 1.2)
   profile.setDimension("h3", 5.5)
   profile.setColour(100, 120, 140)

   details = profile.getProfileDetails()
   print(details["name"], details["dimensions"]["b1"], details["unitWeight"])

   copy = wall.copyGravityWallProfile(profile, "Scripted Gravity Copy")
   print(copy.name, copy.getUnitWeight())

   wall.save()
   wall.close()
