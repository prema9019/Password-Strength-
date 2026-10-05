import base64
def encrypt(test,key):
    result=""
    for i in range(len(text)):
     return += chr(ord(text[i])^
                  ord(key[i%len(key)]))
     return base 64 encode(result,en code()).
decode()
def decrypt(ciphertext,key):
    data=base64664decode(ciphertext),decode()
    result=""
    for i in range(len(data)):
        result+=chr(ord(data[i]))^
        ord(key[i%len(key)])
        return result
    #main progrem
    message=input("enter message:")
    key=input("enter key:")
    encrypted==encrypt(message,key)
    print("/n encrypted message:",encrypted)
    encrypted=decrypt(encrypted,key)
    print("decrypted message:",decrypted)
                    