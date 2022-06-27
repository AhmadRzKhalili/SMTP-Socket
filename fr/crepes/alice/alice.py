import socket            
 
def stablish_connection():
    s = socket.socket()
    s.connect((IP, PORT))
 
PORT = 25  
IP = '127.0.0.1'

if __name__ == '__main__':
    stablish_connection()
 