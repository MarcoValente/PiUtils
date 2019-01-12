TXTWIDTH=100

figlet -f /usr/share/figlet/pagga.tlf -c -w $TXTWIDTH -p < $SCRIPTSDIR/init/login_message.txt
echo
figlet -f /usr/share/figlet/pagga.tlf -c -w $TXTWIDTH "Date           : `date "+%d/%m/%y"`"
figlet -f /usr/share/figlet/pagga.tlf -c -w $TXTWIDTH "Local Time: `date "+%H:%M:%S"`"
