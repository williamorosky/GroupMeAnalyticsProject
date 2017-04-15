import os
from random import randint


def encrypt(token):
	shift= token[0]
	token_shift = map(lambda x: x+int(shift),map(ord,token[1:]))
	encrypt_string = map(chr,token_shift)
	encrypt_string.insert(0,shift)
	return "".join(encrypt_string)

def decrypt(token):
    shift= token[0]
    token_shift = map(lambda x: x-int(shift),map(ord,token[1:]))
    encrypt_string = map(chr,token_shift)
    encrypt_string.insert(0,shift)
    return "".join(encrypt_string)

def encrypt_handler(token):
    return str(randint(1,9))+token

def decrypt_handler(token):
    return token[1:]

def to_file(token):
    file = open("key.txt","w+")
    file.write(encrypt(encrypt_handler(token)))
    file.close()

def from_file():
    if os.path.isfile("key.txt"):
        file= open("key.txt","r")
        str = file.read()
        if(str == ""):
            to_file(raw_input("Enter your GroupMe developer API token: "))
            from_file()
        file.close()
        return decrypt_handler(decrypt(str))
    else:
        to_file(raw_input("Enter your GroupMe developer API token: "))
        from_file()


class EncryptionHandler():

    def __init__(self):
    	self.token = from_file()