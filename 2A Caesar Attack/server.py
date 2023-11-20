import socket 

host='127.0.0.1'
port=8080
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server is listening...")

def decrypt(cipher,key):
    plain=''
    for char in cipher:
        if char.isalpha():
            if char.isupper():
                plain+=chr((ord(char)-ord('A')-key)%26 + ord('A'))
            elif char.islower():
                plain+=chr((ord(char)-ord('a')-key)%26 + ord('a'))
                   
    return plain

def Attack():
    for key in range(26):
        possiblePlain=decrypt(cipher,key)
        print(f"Key : {key} -> {possiblePlain}")
        

while True:
    conn,addr=server.accept()
    print("[SERVER]> Connection established from ",addr," on port ",port)
    cipher=conn.recv(1024).decode()
    print("[CLIENT]> ",cipher)
    
    print("[SERVER]> Decrypting ...")
    Attack()
    conn.close()
