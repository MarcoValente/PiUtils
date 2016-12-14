import subprocess
import sys
import os
import interface

def ExecuteAndStore(command,dry_run=False,shell=True):
    interface.VerboseMessage('Executing command \''+command+'\'')
    if command != '' and not dry_run:
        proc = subprocess.Popen(command if shell else command.split(' '), stdout=subprocess.PIPE, shell=shell)
        (out, err) = proc.communicate()
        return out[:-1]

def ExecuteInBackgound(command=''):
    if command != '':
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        return proc

def ExecuteAndStop(command,stopstring,showOutput=True):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,preexec_fn=os.setsid)
    # Poll process for new output until finished
    while True:
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() is not None:
            break
        if showOutput:
            sys.stdout.write(nextline)
            sys.stdout.flush()
        if stopstring in nextline:
            # process.terminate()
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
            break
    print 'All done'

def CheckIfEnvironVariableExists(name):
    return name in os.environ
