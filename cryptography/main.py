import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# cryptoDome
from Crypto.PublicKey import RSA


keyPath = r'key.txt'

def getKey():
    if os.path.exists(keyPath):
        f = open(keyPath, 'r')
        key = bytes(f.read(),"UTF-8")
    else:
        f = open(keyPath, 'w')
        key = Fernet.generate_key()
        f.write(key.decode("UTF-8"))
    f.close()
    return key

def main():
    key = base64.urlsafe_b64encode(getKey())
    # decodeKey = base64.urlsafe_b64decode(key)
    lengthKey = len(key)
    # lengthKeyDecode = len(decodeKey)
    random = os.urandom(32)
    # print('decodeKey', decodeKey)
    print('key', key)
    print('length Key', lengthKey)
    # print('length decodeKey', lengthKeyDecode)
    print('random', random)

    message_to_encrypt = b'hola'
    f = Fernet(key)
    message_encrypt = f.encrypt(message_to_encrypt)

    print(message_to_encrypt)
    print(message_encrypt.decode("UTF-8"))

def FernetEncryipt():
    password = b"password"
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=10000,
    )
    _kdf = kdf.derive(password)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=10000,
    )
    valid_kdf = kdf.verify(b'password',_kdf)
    # generateKey = Fernet().generate_key()
    key = base64.urlsafe_b64encode(_kdf)
    decodekey = base64.urlsafe_b64decode(key)
    f = Fernet(key)
    token = f.encrypt(b"Secret message!")
    print('salt', salt)
    print('salt Encode', base64.urlsafe_b64encode(salt))
    print('valid_kdf', valid_kdf)
    # print('generateKey', generateKey)
    print('key', key.decode('UTF-8'))
    print(len(key.decode('UTF-8')))
    print('kdf', kdf)
    print('_kdf', _kdf)
    print('encode_kdf', base64.urlsafe_b64encode(_kdf))
    print('length decode _kdf', len(_kdf))
    print('decodekey', decodekey)
    print('=== decode key length:{0}==='.format(len(decodekey)))
    for x in decodekey:
        print(hex(x))
    print('==================')
    print('signing key:', decodekey[:16])
    print('signing encode key:', base64.urlsafe_b64encode(decodekey[:16]))
    print('encryption key:', decodekey[16:])
    print('encryption encode key:', base64.urlsafe_b64encode(decodekey[16:]))
    print('encrypyted message', token.decode('UTF-8'))


def cryptoDome():
    pass

if __name__ == "__main__":
    # main()
    FernetEncryipt()