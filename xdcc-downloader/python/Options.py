import interface

class Options:
    def __init__(self,configfile):
        interface.VerboseMessage('(Options) Initialising Options object...')
        self._options = {}
        self.ParseConfigFile(configfile)
        
    def ParseConfigFile(self,configfile):
        interface.VerboseMessage('(Options) File to parse: '+configfile)
        for line in open(configfile,'r'):
            line = line[:-1] #Removing \n
            if line == '' or line[0] == '#': continue
            line = line.replace(' ','') #Removing spaces
            line = line.replace('\t','') #Removing tabs
            interface.VerboseMessage('(Options) Parsing option: %s = %s' % (line.split('=')[0],line.split('=')[1]))
            self._options.update({line.split('=')[0]:line.split('=')[1]})

    def GetKeys(self):
        return self._options.keys()

    def GetOption(self,optname):
        return self._options[optname]

    def GetString(self,optname):
        return str(self.GetOption(optname))

    def GetInt(self,optname):
        return int(self.GetOption(optname))

    def GetFloat(self,optname):
        return float(self.GetOption(optname))

    def GetBool(self,optname):
        return bool(self.GetOption(optname))

    def Print(self):
        print 'Options object:'
        for optname,opt in self._options.iteritems():
            print '    - %s : %s' % (optname,opt)
