#!/usr/bin/env python3
#ST2504 - ACG Practical - myMd5Stud.py
import sys
import hashlib
# main program starts here
argc = len(sys.argv)
if argc != 2:
    print("Usage : {0} <file name>".format(sys.argv[0]))
    exit(-1)
try:
    with open(sys.argv[1],"r") as f:
        content = f.read()
        hash = hashlib.new("sha256")
        hash.update(content.encode())
        print("A Simple Program on Sha256")
        print("MD5 Hex => {0}".format(hash.hexdigest()))
        print("End of Program")
    f.close()
except:
    print("Invalid file argument!")

