import socket		
import os.path	
import colorama
from colorama import Fore  
#who should close
#how is the connection? new connection each time or one connection?

s = socket.socket()		
print("[CREATED] Socket successfully created.")

PORT = 25
NUM_CLINETS = 5
SIZE = 1024

s.bind(('', PORT))
print("[BINDED] socket binded to %s" % (PORT))

s.listen(NUM_CLINETS)	
print("[LISTENING] socket is listening")	


c, addr = s.accept()
print('[NEW CONNECTION] Got connection from', addr)

while True:
    data = c.recv(SIZE).decode()
    print(data)
    if data == '.':
        c.close()
        break

    
