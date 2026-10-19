Modeler Script Example
======================

This example launches RSWall (if needed), connects, and either opens a file or
attaches to the active GUI project.

Code Snippet: Launch and Connect
--------------------------------

::

   from rswall.RSWallModeler import RSWallModeler
   import os
   import inspect

   current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))
   model_path = os.path.join(current_dir, "example_models", "ExampleModel.rswall")

   # Launch RSWall with the scripting server (skip if already running)
   RSWallModeler.startApplication(port=60067)

   modeler = RSWallModeler(port=60067)

   # Option A: open a file
   wall = modeler.openFile(model_path)

   # Option B: attach to the project already open in the GUI
   # wall = modeler.attachActiveProject()

   print(wall.listWalls())
   wall.close(saveProject=False)
