MSE Wall Unit and Section Profile Example
=========================================

Use an **MSE/SRW** ``.rswall`` project (or open
:download:`ExampleModel.rswall <../example_models/ExampleModel.rswall>` and
create library entries if your build allows MSE libraries on that project).

Code Snippet: MSE Unit and Section Profile
------------------------------------------

::

   from rswall.RSWallModeler import RSWallModeler
   from rswall.MSEWallUnit import UNIT_TYPE_MODULAR, SHEAR_TYPE_LINEAR
   import os
   import inspect

   current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))
   # Prefer an MSE project path when available
   model_path = os.path.join(current_dir, "example_models", "ExampleModel.rswall")

   modeler = RSWallModeler(port=60067)
   wall = modeler.openFile(model_path)

   unit = wall.createMseWallUnit("Scripted MSE Unit")
   unit.setUnitType(UNIT_TYPE_MODULAR)
   unit.setInterlayerShearStrengthType(SHEAR_TYPE_LINEAR)
   print(unit.getUnitDetails())

   profile = wall.createMseSectionProfile("Scripted MSE Section")
   # Prefer setBatterAngleMode to switch mode and set the angle together
   profile.setBatterAngleMode(5.0)
   print(profile.getProfileDetails())

   wall.save()
   wall.close()
