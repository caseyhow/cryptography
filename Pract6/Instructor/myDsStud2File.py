#!/usr/bin/env python3
#ST2504 - ACG Practical - myDsStud2File.py
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
# This sample code demonstrates the File storage operations with the key pair. 
# main program starts here
argc = len(sys.argv)
header="""A Simple Program using RSA to sign and verify a sha256 hashed message.
The message can be entered by the user or can be retrieve from a file. 
"""
print(header)
message=""
if argc == 1:
    message = input("Type in a message please =>")
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

# At this point, the key pair is ready for file operation.
secretcode = input("Pass phrase of your secret key =>")
encrypted_priv_key=rsakey_pair.exportKey(format='DER', passphrase=secretcode,pkcs=8)
pub_key=rsakey_pair.publickey().export_key() # default format is PEM
open("private.der","wb").write(encrypted_priv_key) # save the encrypted key in bytes.
open("public.pem","wb").write(pub_key)  # save the public key . 
digest=SHA256.new(message.encode())
print("digest:")
for b in digest.digest():
    print("{0:02x}".format(b),end="")
print("\n")

# Try to retrive the private key from the 'private.der'
# and use it for the signing.
key_bytes=open("private.der","rb").read()
priv_key = RSA.import_key(key_bytes,passphrase=secretcode)
signer = pkcs1_15.new(priv_key)
signature=signer.sign(digest)
print("Signature:")
for b in signature:
    print("{0:02x}".format(b),end="")
print("\n")
print("Verifying the Signature of the phrase with the public key of the RSA key pair")
# Try to retrive the public key from the 'public.pem'
# and use it for the verification.
pu_bytes=open("public.pem","rb").read()
pu_key=RSA.import_key(pu_bytes)
verifier = pkcs1_15.new(pu_key)
#release the line below to trigger a invalid signature case.
#digest=SHA256.new("wrongmess".encode())
try:
    verifier.verify(digest,signature)
    print("The signature is valid")
except:
    print("The signature is not valid")
