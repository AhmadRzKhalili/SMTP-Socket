import socket       
import colorama
from colorama import Fore     

#who should close

def stablish_connection():
    s.connect((IP, PORT))
 
PORT = 25  
IP = '127.0.0.1'
SIZE = 1024
s = socket.socket()

stablish_connection()

while True:
    print(Fore.RED + "C: " ,  end = "")
    req = input()
    s.send(data.encode())
    
    if  req == '.':
        s.close()
        print(Fore.WHITE + "", end = "")
        break

 