#!/usr/bin/env python3
#ST2504 - ACG Practical - myAesEcb.py
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad
## Extra function to be called by main program
## if num = 8,16,32 return true, false otherwise
def chk_eight(num):
    num1 = num % 8
    if not num1 : return True
    return False

BLOCK_SIZE = 16  #  AES data block size 128 bits (16 bytes)
keysize = 16  # 16 bytes -> 128 bits, 32 bytes -> 256 bits
original_text='change_me'
text_in_bytes = original_text.encode()  # convert UTF 8 encoded string to bytes
print("Generating a " + str(keysize*8) +  "-bits AES key ...")
key=get_random_bytes(keysize) # generate randmom bytes array
print("The key is generated.")
print("AES key :",end=" ")
# --------> Your code here -----------
# The "key" object is an array, use a for..loop to print
# Use end="" in the print to define the end-of-line character
# Use format(b, '02x') to print byte in hex string as 2 places.


print("\n\nPlaintext:")
ct=0
for b in text_in_bytes:
    print(format(b, '3d'),end=" ")
    ct=ct+1
    if chk_eight(ct): print()
print("\n") # print a newline
cipher = AES.new(key, AES.MODE_ECB)  # new AES cipher using key generated
cipher_text_bytes = cipher.encrypt(pad(text_in_bytes,BLOCK_SIZE)) # encrypt data
# data is bytes (text_in_bytes), not strings
print("Ciphertext (in base 10 - Decimal):")
ct=0
for b in cipher_text_bytes:
    print(format(b, '3d'),end=" ")
    ct=ct+1
    if chk_eight(ct): print()
print("\n")
print("Ciphertext (in base 16 - Hex):")
ct=0
for b in cipher_text_bytes:
    print("", format(b, '02x'),end="")
    ct=ct+1
    if chk_eight(ct): print()
print("\n")
# ** Decrypt message here *********

# create a new AES cipher object with the same key and mode
my_cipher = AES.new(key,AES.MODE_ECB)
# Now decrypt the text using your new cipher
decrypted_text_bytes = unpad(my_cipher.decrypt(cipher_text_bytes),BLOCK_SIZE)
# Print the message in UTF8 (normal readable way
decrypted_text = decrypted_text_bytes.decode()
print("Decrypted text: " ,  decrypted_text)
