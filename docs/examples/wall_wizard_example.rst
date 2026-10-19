Wall Wizard Example
===================

Runs the multi-segment wall wizard
(:meth:`~rswall.Wall.Wall.generateMultiSegmentWall`). Requires a project that
exposes wall units via
:meth:`~rswall.Wall.Wall.getAvailableWallWizardUnits` (typically MSE/gabion).

Code Snippet: Generate Multi-Segment Wall
-----------------------------------------

::

   from rswall.RSWallModeler import RSWallModeler
   import os
   import inspect

   current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))
   model_path = os.path.join(current_dir, "example_models", "ExampleModel.rswall")

   modeler = RSWallModeler(port=60067)
   wall = modeler.openFile(model_path)

   units = wall.getAvailableWallWizardUnits()
   print(units)
   if not units:
       raise RuntimeError("No wall wizard units available in this project")

   result = wall.generateMultiSegmentWall(
       plan_points=[
           {"plan": {"x": 0, "y": 0}, "elevation": {"top": 2.0, "bottom": 0.0}},
           {"plan": {"x": 12, "y": 0}, "elevation": {"top": 2.0, "bottom": 0.0}},
           {"plan": {"x": 12, "y": 5}, "elevation": {"top": 2.4, "bottom": 0.0}},
       ],
       wall_unit_name=units[0],
       wall_name="Scripted Wizard Wall",
   )
   print(result.wallName, len(result.segments), result.appliedRequirements)

   wall.save()
   wall.close()
