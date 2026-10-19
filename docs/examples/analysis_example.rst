Analysis Example
================

Download the :download:`ExampleModel.rswall <../example_models/ExampleModel.rswall>`
for this example (or any computable project). Analysis methods live on
:class:`~rswall.Wall.Wall` — there is no separate interpreter package.

Code Snippet: Compute and Factors of Safety
-------------------------------------------

::

   from rswall.RSWallModeler import RSWallModeler
   import os
   import inspect

   current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))
   model_path = os.path.join(current_dir, "example_models", "ExampleModel.rswall")

   modeler = RSWallModeler(port=60067)
   wall = modeler.openFile(model_path)

   print(wall.getComputableSegments())
   print(wall.getResultsStatus())

   result = wall.computeAll()
   print(result)

   walls = wall.listWalls()
   if walls:
       wall_name = walls[0]["wallName"]
       segment_name = wall.getWallDetails(wall_name)["segments"][0]["segmentName"]
       print(wall.getFactorsOfSafety(wall_name, segment_name))
       print(wall.getCriticalFactorOfSafety(wall_name, segment_name))
       print(wall.getAnalysisIssues(wall_name, segment_name))
       print(wall.getRelevantSymbols(wall_name, segment_name))

   wall.close(saveProject=False)
