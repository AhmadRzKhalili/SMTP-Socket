import socket       
import colorama
import re
from colorama import Fore     

def stablish_connection():
    s.connect((IP, PORT))

def input_data():
    data_str = ''
    while True:
        data = input('>>> ')
        if data == '.':
            break
        else:
            data_str = data_str + data + '\n'
    return data_str
        
 
PORT = 25  
IP = '127.0.0.1'
SIZE = 1024
s = socket.socket()

stablish_connection()


buffer = False
data = ''
while True:
    if not buffer:
        print(Fore.RED + "C: " ,  end = "")
        req = input()
    else:
        req = data
        buffer = False

    if  req == 'QUIT':
        s.send(req.encode())
        s.close()
        print(Fore.WHITE + "", end = "")
        break
        
    s.send(req.encode())
    res = s.recv(SIZE).decode()
    print(Fore.BLUE + "S: " + res)
    if re.search(r'^354 ', res):
        print(Fore.RED, end = "")
        data = input_data()
        buffer = True

    

 