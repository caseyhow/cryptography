#!/usr/bin/env python3
#ST2504 - ACG Practical -myCertContent.py
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509 import oid
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec
import sys

def to_lines(line,brkAt=80):
    #break a single long line into multpile lines.
    ans=""
    c = 0
    for ch in line:
        ans=ans+ch
        c=c+1
        if c >= brkAt:
            ans=ans+"\n"
            c=0
    return ans
def get_pubkey_id(pubkey_object):
    if isinstance(pubkey_object, rsa.RSAPublicKey):
        return "RSA"
    elif isinstance(pubkey_object, ec.EllipticCurvePublicKey ):
        return "ECC"
    elif isinstance(pubkey_object, dsa.DSAPublicKey ):
        return "DSA"
    else:
        return None
    
def getNameStr(subj):
  
    ans=[]
    l= [('CN', NameOID.COMMON_NAME )]
    l.append(('OU',NameOID.ORGANIZATIONAL_UNIT_NAME))
    l.append(('O',NameOID.ORGANIZATION_NAME))
    l.append(('L',NameOID.LOCALITY_NAME))
    l.append(('ST',NameOID.STATE_OR_PROVINCE_NAME))
    l.append(('C',NameOID.COUNTRY_NAME))
    for e in l:
        att = subj.get_attributes_for_oid(e[1])
        if att:
            ans.append("{0}={1}".format(e[0],att[0].value))
    return ",".join(ans)

#main program starts here
argc = len(sys.argv)
if argc == 1:
    fn = 'cert.cer'
elif argc == 2:
    fn = sys.argv[1]
else:
    print("Usage {0} [cert_file_name]".format(sys.argv[0]))
    exit(-1)
try:
    st_cert=open(fn,'rb').read()
except:
    print("Failed to open file: {0}".format(fn))
    exit(-2)
st_cert=open(fn,'rb').read()
print("Loading certificate from {0}".format(fn))
cert=x509.load_der_x509_certificate(st_cert,default_backend())
 
print("Version: {0}".format(str(cert.version)))
print("Serial No: {0:x}".format(cert.serial_number))
subjStr=getNameStr(cert.subject)
print("Subject: {0}".format(subjStr))
issuerStr=getNameStr(cert.issuer)
print("Issuer: {0}".format(issuerStr))
print("Validity:")
print("From: {0}".format(cert.not_valid_before.strftime("%a %b %d %H:%M:%S %Y")))
print("To: {0}".format(cert.not_valid_after.strftime("%a %b %d %H:%M:%S %Y")))

signature_algo_oid = cert.signature_algorithm_oid
print("Signature Algorithm: {0} OID= {1}".format(oid._OID_NAMES[signature_algo_oid],signature_algo_oid.dotted_string)) 
print("Signature")
print(to_lines(cert.signature.hex()))
pkey = cert.public_key() 
print("Key {0} public key, {1} bits".format(get_pubkey_id(pkey),pkey.key_size))
pp=cert.public_key().public_bytes(Encoding.PEM,PublicFormat.PKCS1) 
print(pp.decode())




