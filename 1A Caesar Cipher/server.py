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
                if ord(char)-ord('A')-key<0:
                    plain[len(plain)-1]+=chr()
            elif char.islower():
                plain+=chr((ord(char)-ord('a')-key)%26 + ord('a'))
                if ord(char)-ord('a')-key<0:
                    plain[len(plain)-1]+=26    
    return plain

while True:
    conn,addr=server.accept()
    print("[SERVER]> Connection established from ",addr," on port ",port)
    cipher=conn.recv(1024).decode()
    print("[CLIENT]> ",cipher)
    key=int(input("[SERVER]> Enter key to decode : "))
    plain=decrypt(cipher,key)
    print("[SERVER]> Decrypted plain text : ",plain)
    conn.send(plain.encode())
    print("[SERVER]> Message Sent !")
    conn.close()
