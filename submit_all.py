#!/usr/bin/python

'''
Script to submit a list of simulation files to PBS using a specified
PBS script. The script must contain the line beginning with WLDNAME
which will be replaced with WLDNAME=fname where is each file specified.

Usage: submit_all [PBS Script] [Configs...]
            PBS Script - The pbs script which uses $WLDNAME as the simulation
                         input. Defaults to 'sph_nq.pbs'.
            Configs... - The simulation configuration files. If none are 
                         specified the script uses all .sphml files in the 
                         working directory.
'''

import subprocess as sp
import os
import re
import glob
import string
import sys
from math import *

# what pbs script to use
if len(sys.argv)==0:
    pbs = 'sph_nq.pbs'
else:
    pbs = sys.argv[1]

# check pbs script exists
if not os.path.exists(pbs):
    print "PBS script %s does not exist!" % pbs
    exit()

# what .sphml files to submit
if len(sys.argv)<=2:                 # get all .sphml files in the direc
    flist = glob.glob('*.sphml')
else:                                # only specified .sphmls
    flist = []
    for arg in sys.argv[2:]:
        flist.append(arg)

if len(flist)==0:
    print "No configuration files found."
    exit()

# do the submitting
for f in flist:
    
    # create copy of pbs script with the correct sphml file as WLDNAME
    pbsf = open(pbs)
    newpbsf = open(pbs+'~','w')
    for line in pbsf.readlines():
        if string.find(line,'WLDNAME')==0:
            newpbsf.write('WLDNAME='+f)
        else:
            newpbsf.write(line)

    # close files
    pbsf.close()
    newpbsf.close()

    # submit the newly creates pbs script
    sp.call(['qsub',pbs+'~'])

    # delete the temporary file
    os.remove(pbs+'~')
