Materials Example
=================

Download the :download:`ExampleModel.rswall <../example_models/ExampleModel.rswall>`
for this example.

Code Snippet: Material Properties
---------------------------------

::

   from rswall.RSWallModeler import RSWallModeler
   import os
   import inspect

   current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))
   model_path = os.path.join(current_dir, "example_models", "ExampleModel.rswall")

   modeler = RSWallModeler(port=60067)
   wall = modeler.openFile(model_path)

   units = wall.getProjectUnits()
   uw = units["unitWeightUnit"]
   stress = units["stressUnit"]

   materials = wall.getAllMaterials()
   for mat in materials:
       print(f"{mat.name}: {mat.getUnitWeight()} {uw}")

   if materials:
       mat = materials[0]
       mat.setUnitWeight(19.5)
       mat.setFrictionAngle(32.0)
       # Parameter is named cohesionKPa historically; value is project-native stress
       mat.setCohesion(5.0)
       print(mat.getUnitWeight(), uw, mat.getCohesion(), stress)

   new_mat = wall.createMaterial("Scripted Fill")
   new_mat.setUnitWeight(18.0)
   print(new_mat.name, new_mat.getUnitWeight())

   wall.save()
   wall.close()
