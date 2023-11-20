import socket
import numpy as np

host='127.0.0.1'
port=8080

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

fl='X' #Filler Letter

def encrypt(plain,key):
    n = len(key[0])
    plain = plain.upper().replace(" ", "")
    while len(plain) % n != 0:
        plain += fl
    cipher = ""
    for i in range(0, len(plain), n):
        block = [ord(c) - ord('A') for c in plain[i:i+n]]
        encrypted_block = np.dot(key, block) % 26
        cipher += ''.join(chr(b + ord('A')) for b in encrypted_block)
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

reply=client.recv(1024).decode()
print("[SERVER]> Decrypted Text : ",reply)

client.close()