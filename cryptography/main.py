import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

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
    key = getKey()
    print(key)
    message_to_encrypt = b'hola'
    f = Fernet(key)
    message_encrypt = f.encrypt(message_to_encrypt)

    print(message_to_encrypt)
    print(message_encrypt.decode("UTF-8"))

def anotherMain():
    password = b"password"
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    _kdf = kdf.derive(password)
    generateKey = Fernet().generate_key()
    key = base64.urlsafe_b64encode(_kdf)
    # decodekey = base64.urlsafe_b64decode(_kdf)
    f = Fernet(key)
    token = f.encrypt(b"Secret message!")
    print('salt', salt)
    print('generateKey', generateKey)
    print('key', key.decode('UTF-8'))
    print(len(key.decode('UTF-8')))
    print('kdf', kdf)
    print('_kdf', _kdf)
    # print('decodekey', decodekey)
    print(token.decode('UTF-8'))



if __name__ == "__main__":
    main()