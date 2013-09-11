#!/usr/bin/python

import subprocess as sp
import os
import re
import glob
import string
import sys
from math import *

'''
Script for clearing intermediate .dat files from immediate sub directories.
Also takes a regex command line argument to filter sub directories.
'''

regx = re.compile('([0-9]+)_')

def get_immediate_subdirectories(direc):
    return [name for name in os.listdir(direc) if os.path.isdir(os.path.join(direc, name))]

for direc in get_immediate_subdirectories('.'):

    if len(sys.argv)>1:
        if re.match(sys.argv[1],direc) is None:
            continue

    print direc
    
    flist = glob.glob(direc+'/*.dat')

    #keep last files for checkpointing
    nums = []
    for f in flist:
        nums.append( int(regx.findall(f)[-1]) )

    maxnum = max(nums)
    print 'Keeping output %d' % maxnum

    for f,num in zip(flist,nums):
        if num!=maxnum:
            os.remove(f)
