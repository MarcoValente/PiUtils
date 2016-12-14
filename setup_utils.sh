CURRENTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

CMDMGRDIR=$CURRENTDIR/cmd-mgr
COMMONDIR=$CURRENTDIR/common

export PYTHONPATH="${PYTHONPATH}:$COMMONDIR"


#alias definitions
alias cmd-mgr='python $CMDMGRDIR/cmd-mgr.py'
#Setting up autocompletition python script

