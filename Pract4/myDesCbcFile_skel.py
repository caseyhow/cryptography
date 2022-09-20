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
# Generating a random DES Key and (IV) value
# <============ Write your code here ============ 
print("... Key generated. ")
print("... IV generated. ")
if key == b"00000000":
    print("\n*** You use WEAK KEY and IV - generate one yourself !! ***\n")
# Create a DES cipher object with the specific key and CBC Mode and IV
# <============ Write your code here ============ 

outf = open(out_file,'w')  # Define out_file, encrypted.txt
# prompt for the file name
infname = input("File (path &) name of secret message :")
if "." not in infname:
    infname = in_file
    print("... Default file" , in_file , "used" )
#Now encrypt the text file and write the output to encrypted.txt
print("\n--- Content in" , infname ,  "---")
counter = 0
with open(infname) as f:
    for ln in f:
        print("->" , ln.strip()) 
        # encrypt the line read 
        #  <============ Write your code here ============     
        # encrypted_bytes =   # do pad then encrypt 
        # enc_line =          # encrypted bytes array is base64 encoded
        print("Working on it ..",file=outf)  # For testing only, replace next line when done
        # print(enc_line,file=outf)  # Print (write) encrypted string to file 
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
        # decrypt the line read 
        #  <============ Write your code here ============  
        # encrypted_bytes =      # strip, then base64 decode
        # decrypted_bytes =      # decrypt then unpad
        # print                  # decrypted_bytes need to decode
        print("Working on it ..")
f.close()

