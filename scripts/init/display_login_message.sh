TXTWIDTH=100
FONTFILE="/usr/share/figlet/pagga.tlf"

figlet -f $FONTFILE -c -w $TXTWIDTH -p < $SCRIPTSDIR/init/login_message.txt
echo
figlet -f $FONTFILE -c -w $TXTWIDTH "Date           : `date "+%d/%m/%y"`   "
figlet -f $FONTFILE -c -w $TXTWIDTH "Local Time: `date "+%H:%M:%S"`   "

IFS="="; read -a fields <<< "`cmd-mgr display_temp`"
TEMPSTR="${fields[1]}"
figlet -f $FONTFILE -c -w $TXTWIDTH "CPU Temp    : $TEMPSTR        "
