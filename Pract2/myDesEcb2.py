#!/usr/bin/env python3
#ST2504 - ACG Practical - myDesEcb.py
from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad  
## Extra function to be called by main program
## if num = 8,16,32 return true, false otherwise
def chk_eight(num):
    num1 = num % 8
    if not num1 : return True
    return False

BLOCK_SIZE = 32  # Size of DES cipher data block size
original_text='Hello123Hello123Hello123'
text_in_bytes = original_text.encode()  # convert UTF 8 encoded string to bytes
print("Generating a 56-bit DES key ...")
key=get_random_bytes(8) # generate randmom bytes for DES key
print("The key is generated.\n")
print("Plaintext:")
ct=0
for b in text_in_bytes:
    print(format(b, '3d'),end=" ")
    ct=ct+1
    if chk_eight(ct): print()
print("\n") # print a newline
cipher = DES.new(key, DES.MODE_ECB)  # new DES cipher using key generated
cipher_text_bytes = cipher.encrypt(pad(text_in_bytes,BLOCK_SIZE)) # encrypt data
# data is bytes (text_in_bytes), not strings
print("Ciphertext (in base 10 - Decimal):")
ct=0
for b in cipher_text_bytes:
    print(format(b, '08b'),end=" ")
    ct=ct+1
    if chk_eight(ct): print()
print("\n")
print("Ciphertext (in base 16 - Hex):")
ct=0
for b in cipher_text_bytes:
    print(format(b, '02X'),end=" ")
    ct=ct+1
    if chk_eight(ct): print()
print("\n")

# ** Decrypt message here *********

# create a new DES cipher object with the same key and mode  
my_cipher = DES.new(key,DES.MODE_ECB)
# Now decrypt the text using your new cipher
decrypted_text_bytes = unpad(my_cipher.decrypt(cipher_text_bytes),BLOCK_SIZE)
# Print the message in UTF8 (normal readable way
decrypted_text = decrypted_text_bytes.decode()
print("Decrypted text: " ,  decrypted_text)


