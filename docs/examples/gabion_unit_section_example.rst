Gabion Wall Unit and Section Profile Example
============================================

Use a **gabion** ``.rswall`` project when available. Library create methods
mirror the MSE pattern.

Code Snippet: Gabion Unit and Section Profile
---------------------------------------------

::

   from rswall.RSWallModeler import RSWallModeler
   from rswall.GabionWallUnit import SHEAR_TYPE_CONSTANT
   import os
   import inspect

   current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))
   model_path = os.path.join(current_dir, "example_models", "ExampleModel.rswall")

   modeler = RSWallModeler(port=60067)
   wall = modeler.openFile(model_path)

   unit = wall.createGabionWallUnit("Scripted Gabion Unit")
   unit.setInterlayerShearStrengthType(SHEAR_TYPE_CONSTANT)
   print(unit.getUnitDetails())

   profile = wall.createGabionSectionProfile("Scripted Gabion Section")
   profile.setBatterAngleMode(3.0)
   print(profile.getProfileDetails())

   wall.save()
   wall.close()
