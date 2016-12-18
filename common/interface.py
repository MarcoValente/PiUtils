verbose=False

msg_colors={'green':'\033[92m',
            'blue':'\033[94m',
            'red':'\033[31m',
            'yellow':'\033[33m',
            'magenta':'\e[35m',
            'cyan':'\e[36m',
            'black':'\e[30m',
            'default':'\033[0m'
           }

########
#Message functions
########

def GetColorString(text,color='default'):
    if color in msg_colors.keys():
        string = msg_colors[color]+text+msg_colors['default']
    else:
        string = text
        if verbose: print ' --- ERROR: color ' + color + ' not found!'
    return string

def ColorMessage(message,color='default'):
    print GetColorString(message,color)

def VerboseMessage(message):
    if verbose: ColorMessage('VERBOSE: '+message,color='yellow')

def ErrorMessage(message):
    ColorMessage('ERROR: '+message,color='green')
    raise message

########
# Miscellaneous
########

def AddLastSlash(string):
    ret = string
    if string[len(string)-1] != '/':
        ret += '/'
    return ret

def RemoveLastSlash(string):
    ret = string
    if string[len(string)-1] == '/':
        ret = string[:len(string)-1]
    return ret

def CreateDirectory(directory,verb=False):
    import os
    if not (os.path.exists(directory) or directory == ''):
        if verb: print ' --- Creating the directory',directory
        os.makedirs(directory)
    else:
        if verb: print ' --- The directory',directory,'already exists'
    pass
