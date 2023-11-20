import socket 
import numpy as np

host='127.0.0.1'
port=8080
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server is listening...")

def modInverse(a):
    for i in range(1,26):
        if(a*i%26==1):
            return i 
    return None

def Attack(cipher,plain,n):
    
    pt_block=plain[:n*n]
    ct_block=cipher[:n*n]
    
    pt_matrix= np.array([ord(c)-65 for c in pt_block]).reshape(n,n)
    ct_matrix= np.array([ord(c)-65 for c in ct_block]).reshape(n,n)
    
    pt_inv= np.linalg.inv(pt_matrix)
    det=int(round(np.linalg.det(pt_matrix)))
    a_inv=modInverse(det%26)
    
    if(a_inv is None):
        print("No inverse exists !")
    
    pt_inv=(a_inv*det*pt_inv)%26
    
    keyMatrix=np.dot(pt_inv,ct_matrix)%26
    
    return keyMatrix


while True:
    conn,addr=server.accept()
    print("[SERVER]> Connection established from ",addr," on port ",port)
    c=conn.recv(1024).decode()
    print(f"[CLIENT]> {c}")
    p=input("[SERVER]> Enter known plain text : ")
    n = int(input("[SERVER]> Enter order of decryption key matrix : "))
    keyMat=Attack(c,p,n)
    print("[SERVER]> Possible Key Matrix : ",keyMat)
   
    conn.close()
