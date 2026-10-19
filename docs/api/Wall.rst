Wall
====

.. important::

   :class:`~rswall.Wall.Wall` represents an **open RSWall project session**,
   not a single wall definition. Named walls inside the project come from
   :meth:`~rswall.Wall.Wall.listWalls` / :meth:`~rswall.Wall.Wall.getWallDetails`.

The class is the project facade: materials, section profiles, MSE/gabion
libraries, loads, geometry, soil and topography, leveling pad, reinforcement
layout, analysis, and the wall wizard. Compute and factor-of-safety results
live on this same object (there is no separate interpreter package).

Method groups (by source order in the class):

* Session / units / project summary — ``save``, ``close``, ``getProjectUnits``, …
* Materials — ``getAllMaterials``, ``createMaterial``, …
* Gravity / cantilever / abutment section profiles
* MSE and gabion wall units and section profiles
* Reinforcement library
* Wall geometry and segments — ``listWalls``, ``createSingleSegmentWall``, …
* Base strength
* Loads — ``createLineLoad``, ``createUniformLoad``, ``createPointLoad``, …
* Soil, topography, groundwater
* Leveling pad
* Reinforcement layout — ``setReinforcementLayout``, …
* Analysis — ``computeSegment``, ``computeWall``, ``computeAll``, FoS helpers
* Wall wizard — ``generateMultiSegmentWall``, ``getAvailableWallWizardUnits``

Layer placement strings for reinforcement layout are
``"BY_COURSE"``, ``"BY_ELEVATION"``, and ``"BY_HEIGHT_FROM_BOTTOM"`` (see
:meth:`~rswall.Wall.Wall.setReinforcementLayout`).

Topography payloads can be built with helpers in
:mod:`rswall.SoilTopography` (see :doc:`SoilTopography`).

.. autoclass:: rswall.Wall.Wall
   :members:
   :undoc-members: False
   :show-inheritance:
   :special-members: __enter__, __exit__
