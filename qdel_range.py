#!/usr/bin/python

'''
Script to qdel many jobs which are numbered sequentially
within a certain range specified to the script. Useful
for clearing up jobs automatically submitted by scripts
which for some reason are no longer needed or wanted.
[Range is inclusive]
'''

import sys
import subprocess as sp

job_suffix = '.cx1b'

if len(sys.argv)<3:
    print("Usage: qdel_range START STOP [STEP]")
    exit(1)

start = int(sys.argv[1])
stop  = int(sys.argv[2])
if len(sys.argv)>=4:
    step = int(sys.argv[3])
else:
    step = 1

for job in range(start,stop+1,step):
    job_str = str(job) + job_suffix
    sp.call(['qdel',job_str])

print('Deleted PBS jobs '+str(start)+job_suffix+' - '+str(stop)+job_suffix)
