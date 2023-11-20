import socket 

host='127.0.0.1'
port=8080
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def gcd(n1,n2):
    if(n1 == 0): 
        return n2
    elif(n2 == 0): 
        return n1
    elif(n1 == n2): 
        return n1
    elif(n1 > n2): 
        return gcd(n2,n1 % n2)
    return gcd(n1,n2 % n1)

def encrypt(plain,a,b):
    cipher=''
    for char in plain:
        if char.isalpha():
            if char.isupper():
                cipher += chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
            else:
                cipher += chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
        else:
            cipher += char
    return cipher

plain=input("[CLIENT]> Enter plain text : ")
a=int(input("[CLIENT]> Enter key 'a' to encrypt : "))

if(gcd(a,26)==1):
    b=int(input("[CLIENT]> Enter key 'b' to encrypt : "))
else:
    print("[CLIENT]> 'a' should be relatively prime to 26 ! Choose another value for 'a' ... ")

cipher=encrypt(plain,a,b)
print("[CLIENT]> Encrypted plain text / Cipher : ",cipher)
client.send(cipher.encode())
print("[CLIENT]> Message Sent successfully !")
reply=client.recv(1024).decode()
print("[SERVER]> Found text for key : ",reply)
client.close()