Start RSWall with the scripting server
======================================

RSWall must be running with the scripting server enabled before Python can
connect.

**Option A — launch from Python** (installed product)::

   from rswall.RSWallModeler import RSWallModeler

   RSWallModeler.startApplication(port=60067)
   modeler = RSWallModeler(port=60067)

``startApplication`` locates ``RSWall.exe`` from the Windows registry key
``SOFTWARE\\Rocscience\\RSWall 1.0``, or you can pass
``overridePathToExecutable``.

**Option B — start RSWall yourself** with the scripting flag, then connect::

   RSWall.exe -startScriptingServer 60067
