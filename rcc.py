import socket
import os
try:
	import pyfiglet
except Exception as e:
	os.system("pip install pyfiglet")


# result = pyfiglet.figlet_format("wellcome") 
# print(result)

os.system("clear || cls")
def connect():
    s = socket.socket() 
    s.connect(('192.168.29.246', 8080))
    result = pyfiglet.figlet_format("WELLCOME TO THE VOID")
    print(result)
    while True:
    	# msg = s.recv(1204)
    	# print msg
    	smasg = raw_input("NOSYSTEMISSAFE$")
    	s.send(smasg)
    	# print "SENDING..."
connect()