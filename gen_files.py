#!/usr/bin/python

import subprocess as sp
import os
import sys
from math import *

'''
Uses spud_set to edit an XML based configuration file to change the specified paramters.
The paramters to change and their values are loaded from a csv file of the form

  /path/to/outdir; /path/to/opt1; /path/to/opt2; ...
  outdir1;         val_opt1;      val_opt2; ...
  outdir2;         val_opt1_2;    val_opt2_2; ...
  ...

Usage: gen_files [CONFIG] [PARAMS]
            CONFIG - The xml file containing the base simulation paramters
            PARAMS - CSV file specifying the paramters to set and their values

For info about spud_set see https://bugs.launchpad.net/spud.

'''

if len(sys.argv)<3:
    print "Not enough arguments specified."
    exit()
elif len(sys.argv)>4:
    print "Unexpected arguments. Ignoring."

# path to spud_set
spud_set = '/groupvol/sjn/common/spud/bin/spud-set'

# read parameters and values
fin = open(sys.argv[2])
params = fin.readline().split(';')
vals = [ list([]) for _ in xrange(len(params)) ]
for line in fin.readlines():
    data = line.split(';')
    for i,val in enumerate(data):
        vals[i].append(val)

fin.close()

# generate the new configuration files
i=0
for sim in vals:

    ## create simulation output directory
    print('Doing '+sim[0])
    sp.call(['mkdir',sim[0]])

    ## create config file and set parameter values
    fname = "inputs/"+sys.argv[1]+"_"+str(i)+".xml"
    sp.call(["cp",sys.argv[1],fname])

    for j,param in enumerate(params):
        sp.call([spud_set,fname,param,sim[j]])

    i += 1
