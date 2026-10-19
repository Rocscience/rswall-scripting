MSESectionProfile
=================

MSE/SRW section profile library entry.

For batter vs setback distance: calling ``setUniformAngleBatter`` without
switching mode can appear to succeed while geometry stays in distance mode.
Use ``setUseLayerSetbackDistance(False)`` first, or ``setBatterAngleMode(...)``.

.. automodule:: rswall.MSESectionProfile
   :members:
   :undoc-members: False
   :exclude-members: _colour_type
