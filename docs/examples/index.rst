Python Script Examples
======================

These pages are **tutorial code snippets**, separate from the
:doc:`/api/index` API reference.

RSWall models used in the examples can be found here:
:download:`ExampleModel.rswall <../example_models/ExampleModel.rswall>`
(also copied to the site root as ``ExampleModel.rswall`` when the docs are
built).

The seeded model is a line-load sample project with wall/segment names
``Wall 1`` / ``Segment 1``. Examples that require MSE/gabion-only library
features say so explicitly and create library entries through the API where
possible.

Before running any example, start RSWall with scripting enabled
(``RSWall.exe -startScriptingServer 60067``) or call
``RSWallModeler.startApplication(port=60067)``.

.. toctree::
   :maxdepth: 1

   model_script_example
   modeler_script_example
   materials_example
   gravity_wall_profile_example
   loads_example
   soil_assignment_topography_example
   groundwater_example
   mse_unit_section_example
   gabion_unit_section_example
   reinforcement_layout_example
   leveling_pad_base_strength_example
   wall_geometry_example
   analysis_example
   wall_wizard_example
