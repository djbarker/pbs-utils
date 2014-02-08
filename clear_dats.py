#!/apps/python/2.7.3/bin/python

import subprocess as sp
import os
import re
import glob
import string
import sys
import time
from math import *
import argparse

'''
Script for clearing intermediate .dat files from immediate sub directories.
It will by default keep the last file for checkpoint continuation. For full
usage type `clear_dats.py -h'.
'''

parser = argparse.ArgumentParser()
parser.add_argument("-f","--filter",help="A regex for matching which directories to clear.")
parser.add_argument("-a","--all",help="Clear all .dats without leaving the last for checkpointing. (Not recommended)")
parser.add_argument("-k","--keep",help="Which .dats to keep, 0 for last, 1 for penultimate, etc.",type=int,default=0)
args = parser.parse_args()

# regex for finding correct .dats
regx = re.compile('([0-9]+)_')

def get_immediate_subdirectories(direc):
    return [name for name in os.listdir(direc) if os.path.isdir(os.path.join(direc, name))]

fout = open('clear_dats.out','a+')
fout.write(time.strftime("%d/%m/%Y [%H:%M:%S]"))

for direc in get_immediate_subdirectories('.'):

    if args.filter:
        if re.match(args.filter,direc) is None:
            continue

    print direc
    fout.write(str(direc))
    
    flist = glob.glob(direc+'/*.dat')

    if len(flist)==0:
        continue

    #keep last files for checkpointing
    nums = []
    for f in flist:
        nums.append( int(regx.findall(f)[-1]) )

    if len(nums)==0:
	continue;

    if args.all:
        maxnum = -1
    else:
	nums = list(set(nums)) # remove duplicates
	nums.sort()
        maxnum = nums[max(-1-args.keep,-len(nums))]
        print 'Keeping output %d' % maxnum
        fout.write('Keeping output %d' % maxnum)

    for f,num in zip(flist,nums):
        if num!=maxnum:
            os.remove(f)

fout.close()
