Connect and open a project
==========================

Import from submodules (recommended)::

   from rswall.RSWallModeler import RSWallModeler

   modeler = RSWallModeler(port=60067)

   # Open a file on disk
   wall = modeler.openFile(r"C:\path\to\project.rswall")

   # Or attach to the project already open in the GUI
   # wall = modeler.attachActiveProject()

   units = wall.getProjectUnits()
   print(units["unitSystem"], units["lengthUnit"], units["unitWeightUnit"])

   wall.save()
   wall.close()

``Wall`` is the **open project session**, not a single wall definition. Wall
definitions inside the project are identified by name (see
``wall.listWalls()``).

Import classes from their submodules (module names match class names, so
``from rswall import Wall`` loads the *module*, not the class).

All numeric values use the **project's native unit system**. After opening or
attaching a project, call ``wall.getProjectUnits()`` for unit labels. The client
does not convert values. Some parameter names retain historical ``*KPa`` /
``*Meters`` suffixes; those values are still project-native.
