import socket		
import re
import os.path
from os import path	
import colorama
from colorama import Fore  
#who should close
#how is the connection? new connection each time or one connection?

step = 1
status_code = 250
domain_name = 'domain'

def parse_request(req):
    global step 
    global domain_name
    global status_code
    if step == 1:
        req_pattern = '^HELO'
        if re.search(req_pattern, req):
            domain = req[5:]            #regex
            if check_domain(domain):
                step = step + 1
                status_code = 250
                domain_name = domain
                return str(status_code) + ' Hello ' + domain + ', pleased to meet you'
            else:
                return 'Invalid email address' #email add or domain
        else:
            return 'Invalid request'
    elif step == 2:
        req_pattern = '^MAIL FROM:'
        if re.search(req_pattern, req):
            email = parse_email(req)
            if email != None:
                if check_email(email.group(0)):
                    step = step + 1
                    status_code = 250
                    return str(status_code) + " " + email.group(0) + "... Sender ok"
                else:
                    return "Invalid sender email address"
            else:
                return "No email address found in your request!"
        else:
            return 'Invalid request'
    



def check_domain(domain):
    domainArr = domain.split(".")
    domain_str = './'
    for d in reversed(domainArr):
        domain_str = domain_str + d + '/'
    return path.isdir(domain_str)

def parse_email(req):
    email = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', req)
    return email

def check_email(email):
    global domain_name
    email_arr = email.split("@")
    print(email_arr[1])
    print(domain_name)
    if email_arr[1] == domain_name:
        email_domain_arr = email_arr[1].split(".")
        email_str = "./"
        for ed in reversed(email_domain_arr):
            email_str = email_str + ed + '/'
        email_str = email_str + email_arr[0]
        print(email_str)
        return path.isdir(email_str)
    else:
        return False

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

res = 'response'

while True:
    req = c.recv(SIZE).decode()
    print(req)
    print(step)
    if req == '.':
        c.close()
        break
    else:
        res = parse_request(req)
        c.send(res.encode())
        

    
