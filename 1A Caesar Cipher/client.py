import socket

host='127.0.0.1'
port=8080

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def encrypt(plain,key):
    cipher=''
    for char in plain:
        if char.isalpha():
            if char.isupper():
                cipher+=chr((ord(char)-ord('A')+key)%26 + ord('A'))
            else:
                cipher+=chr((ord(char)-ord('a')+key)%26 + ord('a'))
    return cipher

plain=input("[CLIENT]> Enter plain text : ")
key=int(input("[CLIENT]> Enter key to encrypt : "))
cipher=encrypt(plain,key)
print("[CLIENT]> Encrypted plain text / Cipher : ",cipher)
client.send(cipher.encode())
print("[CLIENT]> Message Sent successfully !")
reply=client.recv(1024).decode()
print("[SERVER]> Decrypted Text : ",reply)
client.close()