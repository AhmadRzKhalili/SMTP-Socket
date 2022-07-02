import socket		
import re
import os.path
from os import path	
import colorama
from colorama import Fore  
#who should close
#how is the connection? new connection each time or one connection?

def parse_request(req, step):
    if (step == 1):
        pattern = '^HELO'
        if (re.search(pattern, req)):
            step = step + 1
            domain = req[5:]
            if (parse_domain(domain)):
                status_code = 250
                return str(status_code) + ' Hello ' + domain + ', pleased to meet you'
            else:
                return 'Invalid email address'
        else:
            return 'Invalid request'


def parse_domain(domain):
    domainArr = domain.split(".")
    domain_str = './'
    for d in reversed(domainArr):
        domain_str = domain_str + d + '/'
    return path.isdir(domain_str)


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

step = 1
status_code = 250
res = 'response'

while True:
    req = c.recv(SIZE).decode()
    print(req)

    if req == '.':
        c.close()
        break
    else:
        res = parse_request(req, step)
        c.send(res.encode())
        

    
