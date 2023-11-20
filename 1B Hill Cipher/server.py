import socket 
import numpy as np

host='127.0.0.1'
port=8080
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server is listening...")

fl = 'X'  # Filler letter

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def decrypt(cipher,key):
    n = len(key[0])
    decryption_matrix = np.linalg.inv(key)
    det = int(round(np.linalg.det(key)))
    mod_inv = mod_inverse(det % 26, 26)
    if mod_inv is None:
        raise ValueError("Cannot find modular inverse of the determinant.")
    decryption_matrix = (mod_inv * det * decryption_matrix) % 26
    plain = ""
    for i in range(0, len(cipher), n):
        block = [ord(c) - ord('A') for c in cipher[i:i+n]]
        decrypted_block = np.dot(decryption_matrix.astype(int), block) % 26
        plain += ''.join(chr(b + ord('A')) for b in decrypted_block)
    return plain

while True:
    conn,addr=server.accept()
    print("[SERVER]> Connection established from ",addr," on port ",port)
    cipher=conn.recv(1024).decode()
    print("[CLIENT]> ",cipher)
    n = int(input("[SERVER]> Enter order of decryption key matrix : "))
    dec_key = []
    print("[SERVER]> Enter the values: ")
    for i in range(n):
        r = []
        for j in range(n):
            r.append(int(input()))
        dec_key.append(r)
    plain=decrypt(cipher,dec_key)
    print("[SERVER]> Decrypted plain text : ",plain)
    conn.send(plain.encode())
    print("[SERVER]> Message Sent !")
    conn.close()
