rswall package
==============

The ``rswall`` package is the Python API for RSWall scripting. There is no
separate ``modeler`` / ``interpreter`` package split: connect with
:class:`~rswall.RSWallModeler.RSWallModeler`, then use
:class:`~rswall.Wall.Wall` for project editing, compute, and results.

**Import rule:** always import classes from their submodules::

   from rswall.RSWallModeler import RSWallModeler
   from rswall.Wall import Wall
   from rswall.Material import Material

``from rswall import Wall`` resolves the *module* ``rswall.Wall`` because module
names match class names. Attribute access such as ``rswall.Wall`` (via lazy
``__getattr__``) does resolve the class.

String options (reinforcement types, shear types, layer placement modes, and
similar) are **plain strings**, not Python ``Enum`` types. Prefer module-level
constants where provided (for example
:data:`~rswall.Reinforcement.TYPE_GEOGRID`), or the values returned by
``getValid*`` helpers on ``Wall``.

.. toctree::
   :maxdepth: 1

   RSWallModeler
   ApplicationManager
   Wall
   Material
   GravityWallProfile
   CantileverWallProfile
   AbutmentWallProfile
   MSEWallUnit
   GabionWallUnit
   MSESectionProfile
   GabionSectionProfile
   Reinforcement
   LineLoad
   UniformLoad
   PointLoad
   WizardWallResult
   WizardSegment
   SoilTopography
   wizard_plan_points
   wizard_requirements
