#!/usr/bin/env python3
#ST2504 - ACG Practical - myDsStud.py
from Cryptodome.Random import get_random_bytes
from Cryptodome.Signature import pkcs1_15 
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256
import sys
# RKCS1_15 Digital Signature Scheme is based on RSA - it is described in Section 8.2 of RFC8017
# 
# Signing requires the private key of the key pair
# verifying requires the public key of the key pair
# Also need a hashing scheme to digest the message
# We will use sha256 in this sample 
# main program starts here
argc = len(sys.argv)
header="""A Simple Program using RSA to sign and verify a sha256 hashed message.
The message can be entered by the user or can be retrieve from a file. 
"""
print(header)
message=""
if argc == 1:
    message = input("Type in a phrase please =>")
elif argc == 2:
    #assumming the command line argument contains a valid file name
    with open(sys.argv[1]) as f:
        message = f.read()
    f.close()
else:
    print("Usage: {0} [file name]".format(sys.argv[0]))
    exit(-1)
print("Generating an RSA key pair...")
rsakey_pair=RSA.generate(2048)  
print("Done generating the key pair.")
print("Signing the sha256 digest of the phrase with the private key of the RSA key pair")
digest=SHA256.new(message.encode())
print("digest:")
for b in digest.digest():
    print("{0:02x}".format(b),end="")
print("\n")
signer = pkcs1_15.new(rsakey_pair)
signature=signer.sign(digest)
print("Signature:")
for b in signature:
    print("{0:02x}".format(b),end="")
print("\n")
print("Verifying the Signature of the phrase with the public key of the RSA key pair")
verifier = pkcs1_15.new(rsakey_pair.publickey())
#release the line below to trigger a invalid signature case.
#digest=SHA256.new("wrongmess".encode())
try:
    verifier.verify(digest,signature)
    print("The signature is valid")
except:
    print("The signature is not valid")
