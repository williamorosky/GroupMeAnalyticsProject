#objective: to encrpyt an api token and save it to a file
			#check file, decrypt the api for reuse
#Purpose: so that we dont have to keep searching for the api key everytime

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
    from random import randint
    return str(randint(1,9))+token
def decrypt_handler(token):
    return token[1:]
def to_file(token):
    file = open("key.txt","w+")
    file.write(encrypt(encrypt_handler(token)))
    file.close()
def from_file():
    import os
    if os.path.isfile("key.txt"):
        file= open("key.txt","r")
        str = file.read()
        if(str == ""):
            print("enter api key: ")
            to_file(raw_input())
            from_file()
        file.close()
        return decrypt_handler(decrypt(str))
    else:
        to_file(raw_input("enter api key: "))
        from_file()
    
def execute_api_key():
    print(from_file())



def main():
    execute_api_key()
if __name__ == "__main__":
    main()
    
