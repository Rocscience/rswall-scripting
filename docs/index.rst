RSWall Scripting Reference Manual
=================================

**Version:** |version|

Prerequisites
-------------

Before you begin, ensure you have the **RSWall** application installed on
Windows. Python scripting communicates with a running RSWall instance over
gRPC (default port ``60067``).

Python Environment
------------------

There are two methods to run a script, which differ in the Python environment
used:

1. **Running in RocScript Editor**

   * Opens from RSWall (**Scripting → RocScript**).
   * Suitable for interactive editing and running scripts against a live
     RSWall session.

2. **Running in your own Python environment**

   * Requires installing the ``RSWallScripting`` Python package (see below).
   * Suitable for automation, CI, and advanced workflows.

Install RSWall Python API Library
---------------------------------

pip installation::

   pip install RSWallScripting

If you are not using the latest release of RSWall, pin a library version that
matches your product release. For example::

   pip install "RSWallScripting==1.006"

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2

   getting_started/index
   api/index
   examples/index
