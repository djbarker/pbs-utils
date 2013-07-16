#PBS Utilities
*pbs-utils*

A collection of short python scripts to aid submission of of multiple simulations to the PBS queuing system. 

These scripts use spud_set to update xml configuration files (see: https://launchpad.net/spud) and then update a PBS (bash) script where the configuration file is specified as an environmental variable `WLDNAME`.

They are written to fit into my workflow and if you wish to use them they will almost certainly need tayloring but perhaps they might be useful to some.