from irc import irc

MyIRC=irc.IRC_Object( )
MyConn=MyIRC.new_connection( )

MyConn.nick="Wellow"
MyConn.ident="wellow"
MyConn.server=("irc.freenode.net", 6667)
MyConn.realname="Wellow his bot"

while 1:
    MyIRC.main_loop( )
