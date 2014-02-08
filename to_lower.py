#!/usr/bin/python

'''
Renames all files and subfolders in a directory to lower case.
'''

import os
import glob

flist = glob.glob('*')

for fname in flist:
    if not os.path.exists(fname.lower()):
        os.rename(fname,fname.lower())
    elif fname!=fname.lower():
        print "Cannot move %s, file with name %s already exists." % (fname,fname.lower())
        
