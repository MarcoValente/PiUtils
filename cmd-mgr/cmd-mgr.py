import command_dic
import interface
import terminal
from optparse import OptionParser
#import argcomplete

def LoadOptions():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage=usage)
    parser.add_option("-v", "--verbose", default=False, action="store_true",help="Print debug information.")
    parser.add_option(      "--sudo",    default=False, action="store_true",help="Set sudo rights.")
    parser.add_option("-d", "--dryRun",  default=False, action="store_true",help="Dry run flag.")
    (options, args) = parser.parse_args()

    if options.verbose: interface.verbose=True
    if len(args) != 1:
        parser.print_usage()
        print 'arguments :',sorted(command_dic.command_dic.keys())
        exit(1)

    options = {
               'verbose': options.verbose,
               'dry-run': options.dryRun,
               'sudo':    options.sudo,
              }

    arguments = {
                 'arg1':args[0]
                }

    return {'options':options,'arguments':arguments}

def ExecuteCommand(command):
    if opt['options']['dry-run']: print command_dic.command_dic[command]
    command_to_exec=command_dic.command_dic[command]
    if opt['options']['sudo']: command_to_exec = 'sudo '+command_to_exec
    resp = terminal.ExecuteAndStore(command_to_exec,dry_run=opt['options']['dry-run'])
    if not opt['options']['dry-run']: print resp

def main():
    global opt
    opt = LoadOptions()
    ExecuteCommand(command=opt['arguments']['arg1'])

if __name__ == "__main__":
    main()
