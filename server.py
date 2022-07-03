import socket		
import re
import datetime
import uuid

import os.path
from os import path	

import colorama
from colorama import Fore  

step = 1
status_code = 250
domain_name = 'domain'
sender_email = 'sender'
recipient_email = 'recipient'
recipient_email_path = 'recipient path'
data = 'data'

def parse_request(req):
    global step 
    global domain_name
    global status_code
    global sender_email
    global recipient_email
    global data

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

                if check_sender_email(email.group(0)):
                    sender_email = email.group(0)
                    step = step + 1
                    status_code = 250
                    return str(status_code) + " " + email.group(0) + "... Sender ok"

                else:
                    return "Invalid sender email address"

            else:
                return "No email address found in your request!"

        else:
            return 'Invalid request'

    elif step == 3:
        req_pattern = '^RCPT TO:'

        if re.search(req_pattern, req):
            email = parse_email(req)

            if email != None:

                if check_recipient_email(email.group(0)):
                    recipient_email = email.group(0)
                    step = step + 1
                    status_code = 250
                    return str(status_code) + " " + email.group(0) + "... Recipient ok"

                else:
                    return "Invalid recipient email address"

            else:
                return "No email address found in your request!"

        else:
            return 'Invalid request'

    elif step == 4:
        req_pattern = 'DATA'

        if re.search(req_pattern, req):
            step = step + 1
            status_code = 354
            return str(status_code) + " Enter mail, end with \".\" on a line by itself"

    elif step == 5:
        data = req
        status_code = 250
        step = step + 1
        return str(status_code) + " Message accepted for delivery"

    elif step == 6:
        req_pattern = 'SEND'

        if re.search(req_pattern, req):
            send_mail(data)
            status_code = 250
            step = 3
            return str(status_code) + " Email sent"

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



def check_sender_email(email):
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



def check_recipient_email(email):
    global recipient_email_path

    email_arr = email.split("@")
    email_domain_arr = email_arr[1].split(".")
    email_str = "./"

    for ed in reversed(email_domain_arr):
        email_str = email_str + ed + '/'

    email_str = email_str + email_arr[0]
    print(email_str)

    if path.isdir(email_str):
        recipient_email_path = email_str + "/inbox"
        return True

    else:
        return False

def send_mail(data):
    global sender_email
    global recipient_email
    global recipient_email_path

    sender_address = '<email_from>' + sender_email + '</email_from>\n'
    recipient_adress = '<email_to>' + recipient_email + '</email_to>\n'
    data = '<email_data>\n' + data + '\n</email_data>'

    email_data = sender_address + recipient_adress + data
    file_name = str(datetime.datetime.now().date()) + " - " + str(uuid.uuid1())

    try:
        with open(recipient_email_path + '/' + file_name + '.txt', 'w') as f:
            f.write(email_data)
    except FileNotFoundError:
        print("Email address does not exist")




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
    if req == 'QUIT':
        c.close()
        break
    else:
        res = parse_request(req)
        c.send(res.encode())
        

    
