#!/apps/python/2.7.3/bin/python
import subprocess as sp
import os
import re
import glob
import string
import sys


flist = glob.glob('*.dat')

# regex for finding correct .dats
regx = re.compile('([0-9]+)_')

#keep last files for checkpointing
nums = []
for f in flist:
	nums.append( int(regx.findall(f)[-1]) )

nums = list(set(nums)) # remove duplicates
nums.sort()

def list_consise(ints):

	if len(ints)<2:
		print '[%d]'&ints[0]

	ranges = []	
	prev_start = ints[0]
	for i,num in enumerate(ints[1:]):
		if num-ints[i] > 1:
			ranges.append( (prev_start,ints[i]) )
			prev_start = num

	ranges.append( (prev_start,ints[-1]) )
	

	outstr = '['
	for (x,y) in ranges[:-1]:
		if x==y:
			outstr += '%d,' % x
		else:
			outstr += '%d-%d,' % (x,y)
	(x,y) = ranges[-1]
	if x==y:
		outstr += '%d' % x
	else:
		outstr += '%d-%d' % (x,y)

	outstr += ']'
	return outstr

	
print ".dat numbers "+list_consise(nums)
