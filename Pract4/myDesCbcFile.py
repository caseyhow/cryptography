#!/usr/bin/env python3
#ST2504 - ACG Practical - myDesCbcFile.py
from base64 import b64encode,b64decode 
from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

# default settings
BLOCK_SIZE = 8
in_file = "plaintext.txt"
out_file = "encrypted.txt"
key = b"00000000"
myIV = b"00000000"

# main program starts here
print("Generating a 56-bit DES key and IV.")
# Generating a valid random DES Key and store it to key
key=get_random_bytes(8)
print("... Key generated. ")
# Generating a valid random or static Initial Vector (IV) value
myIV=get_random_bytes(8)
print("... IV generated. ")
if key == b"00000000":
    print("\n*** You use WEAK KEY and IV - generate one yourself !! ***\n")
# Create a DES cipher object with the specific key and CBC Mode and IV
cipher = DES.new(key, DES.MODE_CBC,myIV)
# prepare the outfile, encrypted.txt
outf = open(out_file,'w')
# prompt for the file name
infname = input("File (path &) name of secret message :")
if "." not in infname:
    infname = in_file
    print("... Default file" , in_file , "used" )
# Encrypt the text file and write the output to encrypted.txt
print("\n--- Content in" , infname ,  "---")
counter = 0
with open(infname) as f:
    for ln in f:
        print("->" , ln.strip()) 
        # encrypt the line read        
        encrypted_bytes = cipher.encrypt(pad(ln.strip().encode(),BLOCK_SIZE))
        enc_line = b64encode(encrypted_bytes).decode()
        print(enc_line,file=outf)
        counter= counter + 1
f.close()
outf.close()
print("\n<-" , counter, "lines saved to", out_file)

# create a new DES cipher object with the same key and cbc mode and IV  
cipher2 = DES.new(key, DES.MODE_CBC,myIV)
print("\n--- Printing encrypted content (in", out_file ,") ---" )
# Read encrypted.txt and print on screen line-by-line
with open("encrypted.txt","r") as f:
    for ln in f:
        print("->", ln.strip())
f.close()

print("\n--- Read", out_file , "and decrypt into plain text ---")
# Read file, decrypt and print
with open(out_file,"r") as f:
    for ln in f:
        encrypted_bytes = b64decode(ln.strip().encode())
        decrypted_bytes = unpad(cipher2.decrypt(encrypted_bytes),BLOCK_SIZE)
        print(decrypted_bytes.decode())
f.close()
 
