#!/usr/bin/env python3
#ST2504 - ACG Practical - myDesEcbFile_Skel.py
from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad
'''
This program handle user inputs. (use "Enter" for default)
This program is incomplete as it did not do encryption
'''
# default settings
BLOCK_SIZE = 8
default_key = "1234abcd" 
in_file = "secretMap.bmp"
out_file = "secret.bmp"
out1_file = "secret_ori_header.bmp"

# main program starts here
user_key = input("Enter a key (>7 char) please : ")
if len(user_key)<8:
    user_key=default_key
    print("...Invalid input, DEFAULT key used")
key=user_key.encode()[:8] # Use on first 8 bytes for key

plain_file = input("File (path &) name to encrypted : ")
if "." not in plain_file:
    plain_file = in_file
try:
    f=open(plain_file,"rb")
    ofile=open( out_file ,"wb")
    ofile1=open( out1_file ,"wb")
except:
    print("Error, invalid file ", plain_file)
    exit(-1)
# Create a DES cipher object with the specific key and ECB Mode
# ====== Write your code here ========

while True:
    inputblock=f.read() # read all data at once b'cos DES will write 16 bytes, if you process by blocks of 8 bytes
    if inputblock == b'': # until end of file
        break
    # extract the 0-54 bytes (BMP header) from the orginal file
    bmpHeader = inputblock[0:54]
    # Encrypt the whole inputblock and write to cipherbytes
    # ====== Write your code here ========
    cipherbytes = inputblock   # ==For demo use (no encryption), replace this line

    ofile.write( cipherbytes  )
    print ("Created  (" , out_file , ") with encrypted header of size (in bytes)  ", len(cipherbytes) )   

    # The final encrpted map will include orignal header + encrypted RGB values for each pixels
    cipherbytes = bmpHeader  + cipherbytes[54: len(cipherbytes)]
    ofile1.write( cipherbytes  )
    print ("Created  (" , out1_file , ") with original header of size (in bytes)  ", len(cipherbytes) )   

# Finally, close the input and output files 
f.close()
ofile.close()
ofile1.close()
 
