Model Script Example
====================

Download the :download:`ExampleModel.rswall <../example_models/ExampleModel.rswall>`
for this example.

Code Snippet: Model Manipulation
--------------------------------

::

   from rswall.RSWallModeler import RSWallModeler
   import os
   import inspect

   current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))
   model_path = os.path.join(current_dir, "example_models", "ExampleModel.rswall")

   modeler = RSWallModeler(port=60067)
   wall = modeler.openFile(model_path)

   units = wall.getProjectUnits()
   print(units["unitSystem"], units["unitWeightUnit"])

   materials = wall.getAllMaterials()
   if materials:
       materials[0].setName("Silty Sand")

   wall.save()
   wall.close()
