#!/usr/bin/env python3
#ST2504 - ACG Practical - myMacSha256Stud.py
# take in a file name or an input phrase 
from Cryptodome.Random import get_random_bytes
import hmac
import base64
import sys
# main program starts here
argc = len(sys.argv)
content=""
if argc > 2:
    print("Usage : {0} [file name]".format(sys.argv[0]))
    exit(-1)
elif argc == 2:
    try:
     with open(sys.argv[1]) as f:
        content=f.read()
    except:
        print("Invalid file argument!")
        exit(-1)
else:
    content=input("Your input please =>")
try:    
    print("A simple Program on HmacSHA1")
    keysize=hmac.HMAC.blocksize
    print("key size {0}".format(keysize))
    key=get_random_bytes(keysize)
    print("key : {0}".format(base64.b64encode(key).decode()))
    hma = hmac.new(key,digestmod="sha256")
    hma.update(content.encode())
    print("MAC: {0}".format(base64.b64encode(hma.digest()).decode()))
except:
    print("Invalid file argument!")
