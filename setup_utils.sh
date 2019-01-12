CURRENTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export CMDMGRDIR=$CURRENTDIR/cmd-mgr
export COMMONDIR=$CURRENTDIR/common
export SCRIPTSDIR=$CURRENTDIR/scripts

bash $SCRIPTSDIR/init/display_login_message.sh

export PYTHONPATH="${PYTHONPATH}:$COMMONDIR"

#alias definitions
alias cmd-mgr='python $CMDMGRDIR/cmd-mgr.py'
#Setting up autocompletition python script

