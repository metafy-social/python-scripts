import rsa

##this function generates the keys
def generate_keys():
    (pubKey, privKey) = rsa.newkeys(1024)
    with open('keys/pubkey.pem', 'wb') as f:
        f.write(pubKey.save_pkcs1('PEM'))

    with open('keys/privkey.pem', 'wb') as f:
        f.write(privKey.save_pkcs1('PEM'))

##Loads the keys from the .pem files to pubkey and privkey variables
def load_keys():
    with open('keys/pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    with open('keys/privkey.pem', 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey

##encrypts the messages using the public key
def encrypt(msg, key):
    return rsa.encrypt(msg.encode('ascii'), key)

##decrypts the encrypted message or ciphertext using the privatekey
def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

##the sha is generated for the message and key
def sign_sha1(msg, key):
    return rsa.sign(msg.encode('ascii'), key, 'SHA-1')

##this function verifies the sha
def verify_sha1(msg, signature, key):
    try:
        return rsa.verify(msg.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False

##generates keys
generate_keys()

##loads keys
pubKey, privKey = load_keys()

##Takes in the message and encrypts it
message = input('Enter a message:')
ciphertext = encrypt(message, pubKey)

signature = sign_sha1(message, privKey)

##It then decrypts the message.
plaintext = decrypt(ciphertext, privKey)

##the sgnature of the message is displayed
print(f'Signature: {signature}')
##the cipher of the message is displayed
print(f'Cipher text: {ciphertext}')

##the decrypted message is displayed
if plaintext:
    print(f'Plain text: {plaintext}')
else:
    print('Could not decrypt the message.')

if verify_sha1(plaintext, signature, pubKey):
    print('great the signature is verified')
else:
    print('Could not verify the message signature.')
