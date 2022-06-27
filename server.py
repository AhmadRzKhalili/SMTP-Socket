import socket			

s = socket.socket()		
print("[CREATED] Socket successfully created.")

PORT = 25
NUM_CLINETS = 5

s.bind(('', PORT))
print("[BINDED] socket binded to %s" % (PORT))

s.listen(NUM_CLINETS)	
print("[LISTENING] socket is listening")	


while True:

    c, addr = s.accept()
    print("")
    print('[NEW CONNECTION] Got connection from', addr)

    
