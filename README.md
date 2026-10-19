# Introduction 
This repo contains the reference manual for the RSWall scripting library. The RSWall scripting library is used to interact with the RSWall application through python scripts.   

Release notes for the library are kept here:
https://www.rocscience.com/support/rswall/release-notes

RSWall can be downloaded here:
https://www.rocscience.com/support/program-downloads

The library itself is hosted on PyPi here:
https://pypi.org/project/RSWallScripting/

## Goal
Each function exposed corresponds to an equivalent operation you could have done through the UI.  
Using this idea, the user should be able to edit models and get results without having to go through the UI at all.
A large set of functionalities have been exposed. Please see [Capabilities](#capabilities) for current limitations.

## Python UI equivalents
Events and workflows done in the UI will have equivalents in the python library.  
Wherever a dialog is shown in the UI, there will be an equivalent class with methods that mimick the dialog's behavior.  
Wherever a warning or error dialog is displayed, an exception will be thrown, or a warning will be displayed in python instead.  
Wherever you can select and manipulate an entity, identifiers can be used in the library to get references to those entities in python and objects will be constructed to help you interface with them.  

## How it works
Each function in the library is a wrapper to make an api call to the Application.  
Objects retrieved through function calls will often not contain any data themselves, but will instead be proxies, allowing you to get information from the objects in the application.  
For this reason, debugging will sometimes be tricky, as not all data will always be available for you to inspect unless you get it and assign it to a variable yourself.  

# Capabilities
Supported
- Project management: Open an existing .rswall file, attach to a project already open in RSWall, save changes, and close the project.
- Project data: Read and edit soils/materials, line/uniform/point loads, and Project Summary metadata.
- Wall profiles: Create, copy, delete, and configure gravity, cantilever, and abutment wall profiles, including dimensions and unit weight.
- MSE/SRW walls: Configure wall units, section profiles, manufacturer library presets, reinforcement properties and layouts, and leveling pads.
- Gabion walls: Configure wall units, section profiles, manufacturer library presets, basket counts, and basket tilt.
- Site and design conditions: Assign soil regions and configure backslope/front-face topography, groundwater, and base-strength options for the current design standard.
- Wall generation: Generate multi-segment MSE/SRW and gabion walls using the Wall Wizard.
- Analysis and results: Run analysis for individual segments, walls, or the full project, and read result status, factors of safety (including the critical value), analysis issues, and relevant symbols.

Not Supported
- Project settings: Creating a new RSWall project through File > New, or changing the project's wall type or design standard. Direct UI compute workflow automation.
- Multilayer and Support Designer: Dedicated support for Multilayer and Support Designer workflows is not currently supported.
- CAD/CSV import/export: Dedicated import/export of wall geometry is not currently supported.

# Getting Started

**Overview Page**
https://www.rocscience.com/help/rswall/documentation/scripting/scripting-overview

**Getting started tutorial guide**  
https://www.rocscience.com/help/rswall/tutorials/tutorials-overview/10-getting-started-with-rswall-python-scripting