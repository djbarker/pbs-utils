#!/usr/bin/python

'''
Script uses the std output of the qstat command to delete either, all pbs jobs,
only queued pbs jobs or only running pbs jobs.
'''

import sys
import subprocess as sp

def query_yesno(question):
    valid_yes = ['yes','y']
    valid_no  = ['no','n']
    
    while True:
        sys.stdout.write(question + ' [yes/no]: ') #no newline
        answer = raw_input().lower()
        if (answer in valid_yes) or (answer in valid_no):
            return (answer in valid_yes)
        print('Please enter \'yes\' or \'no\'.')

# Delete all, queued or running?
jtypes = {'all':'all','a':'all','queued':'queued','q':'queued','running':'running','r':'running'}
jtype = 'all' # default
if len(sys.argv)==2:
    jtype = jtypes[sys.argv[1].lower()]
elif len(sys.argv)>2:
    print('Usage: qdel_all [JOBTYPE=all]')
    print('   where JOBTYPE is either \'all\' (a),\'queued\' (q) or \'running\' (r)')

jtypestr = ''
if jtype=='queued':
    jtypestr = 'queued '
elif jtype=='running':
    jtypestr = 'running '

# Safety check before continuing
q_string = 'This will delete all '+jtypestr+'PBS jobs. Do you wish to continue?'
if not query_yesno(q_string):
    exit(0)

# Get info on PBS jobs
qstat = sp.Popen(['qstat','-a'],stdout=sp.PIPE)

# Clear header and info lines
for line in qstat.stdout:
    if line[0]!='-':
        del line
    else:
        del line
        break

# Get job id
for line in qstat.stdout:
    data = line.split()
    jobid = data[0]
    jobstate = data[9]
    if jtype=='all' or (jtype=='queued' and jobstate=='Q') or (jtype=='running' and jobstate=='R'):
        sp.call(['qdel',data[0]])

# Print final message
print('Deleted all '+jtypestr+'PBS jobs.')
