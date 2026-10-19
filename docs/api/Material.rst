Material
========

Soil material library entry. Numeric strength and unit-weight values use
**project-native** units from :meth:`~rswall.Wall.Wall.getProjectUnits`.
The cohesion setter parameter is named ``cohesionKPa`` for historical wire
reasons; pass the value in the project's native stress unit, not necessarily
kilopascals.

.. autoclass:: rswall.Material.Material
   :members:
   :undoc-members: False
   :show-inheritance:
