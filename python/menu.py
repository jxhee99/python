import os
helpmsg = """
!		      debug		    mdir		  sendport	site
$		      dir		      mget		  put		    size
account		disconnect	mkdir		  pwd		    status
append		exit		    mls		    quit		  struct
ascii		  form		    mode		  quote		  system
bell		  get	      	modtime		recv		  sunique
binary		glob	    	mput	  	reget		  tenex
bye		    hash	    	newer	  	rstatus		tick
case		  help		    nmap		  rhelp		  trace
cd		    idle	    	nlist		  rename		type
cdup	  	image		    ntrans	 	reset		  user
chmod		  lcd		      open		  restart		umask
close		  ls	      	prompt		rmdir		  verbose
cr		    macdef		  passive		runique		?
delete		mdelete		  proxy		  send
"""
def help():
  print(helpmsg)

def pwd():
  print(os.getcwd())

def error():
  print('?Invalid command')

### main ###
while True:
  cmd = input('ftp> ')

  if cmd == 'help':
    help()
  elif cmd == 'pwd':
    pwd()
  elif cmd == '':
    continue
  elif cmd == 'quit':
    break
  else:
    error()
