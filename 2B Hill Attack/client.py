import socket
import numpy as np

host='127.0.0.1'
port=8080

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def encrypt(plain,key):
    n=len(key[0])
    fill='_'
    while(len(plain)%n!=0):
        plain+=fill 
    
    cipher=""
    for i in range(0,len(plain),n):
        block=[ord(c)-65 for c in plain[i:i+n]]
        enc_block=np.dot(block,key)%26
        for i in enc_block:
            cipher+= (chr(i+65))
    return cipher


plain=input("[CLIENT]> Enter plain text : ")
n = int(input("[CLIENT]> Enter order of encryption key matrix : "))
enc_key = []
print("[CLIENT]> Enter the values: ")

for i in range(n):
    r = []
    for j in range(n):
        r.append(int(input()))
    enc_key.append(r)

cipher=encrypt(plain,enc_key)
print("[CLIENT]> Encrypted plain text / Cipher : ",cipher)

client.send(cipher.encode())
print("[CLIENT]> Message Sent successfully !")

client.close()