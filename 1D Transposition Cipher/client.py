import socket
import math

host='127.0.0.1'
port=8080

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def encrypt(plain,key):
    cipher = ""

    # Track key indices
    k_indx = 0

    msg_len = float(len(plain))
    msg_lst = list(plain)
    key_lst = sorted(list(key))

    # Calculate column of the matrix
    col = len(key)

    # Calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # Add the padding character '_' in empty cell of the matix
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    # Create Matrix and insert message and padding characters row-wise
    matrix = [msg_lst[i: i + col]
            for i in range(0, len(msg_lst), col)]

    # Read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1

    return cipher

plain=input("[CLIENT]> Enter plain text : ")
key=input("[CLIENT]> Enter key to encrypt : ")
cipher=encrypt(plain,key)
print("[CLIENT]> Encrypted plain text / Cipher : ",cipher)
client.send(cipher.encode())
print("[CLIENT]> Message Sent successfully !")
reply=client.recv(1024).decode()
print("[SERVER]> Decrypted Text : ",reply)
client.close()