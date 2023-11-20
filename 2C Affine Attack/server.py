import socket 

host='127.0.0.1'
port=8080
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server is listening...")
def mod_inverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
    return -1

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

def decrypt(cipher,a,b):
    plain=''
    for char in cipher:
        if char.isalpha():
            if char.isupper():
                plain += chr(((ord(char) - ord('A') - b) * mod_inverse(a, 26)) % 26 + ord('A'))
            else:
                plain += chr(((ord(char) - ord('a') - b) * mod_inverse(a, 26)) % 26 + ord('a'))
        else:
            plain += char
    return plain

def Attack(plain,cipher):
    for a in range(1,26):
        for b in range(26):
            possiblePlain=decrypt(cipher,a,b)
            if possiblePlain==plain:
                return a,b
    return None
while True :
    conn, addr=server.accept()
    print("[SERVER]> Connection established from ",addr," on port ",port)
    cipher=conn.recv(1024).decode()
    print("[CLIENT]> ",cipher)
    plain=input("[SERVER]> Enter known plain text : ")
    a,b=Attack(plain,cipher)
    print(f"[SERVER]> The possible key pair is : [{a},{b}]")
    conn.send(f"{a},{b}".encode())
    print("[SERVER]> Message Sent !")
    conn.close()