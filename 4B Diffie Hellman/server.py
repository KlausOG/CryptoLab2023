import socket 
import math

host='127.0.0.1'
port=8080
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server is listening...")

def prime_checker(p):
    if p < 2:
        return False
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False
    return True

def primitive_check(g, p):
    L = [pow(g, i, p) for i in range(1, p)]
    return len(set(L)) == p - 1

def calculate_shared_key(y, x, p):
    return pow(y, x, p)

while True:
    conn,addr=server.accept()
    print("[SERVER]> Connection established from ",addr," on port ",port)
    P = int(input("[SERVER]> Enter P: "))
    G = int(input(f"[SERVER]> Enter the Primitive Root of {P}: "))

    if not (prime_checker(P) and primitive_check(G, P)):
        print("[SERVER]> Invalid values for P and G. Please try again.")
        continue

    conn.send(str(P).encode())
    conn.send(str(G).encode())

    x2 = int(input("[SERVER]> Enter the Server's Private Key: "))
    y2 = pow(G, x2, P)
    print(f"[SERVER]> Computed Public Component : {y2}")
    conn.send(str(y2).encode())

    y1 = int(conn.recv(1024).decode())
    print(f"[CLIENT]> Client's Public Component : {y1} ")

    
    K2 = calculate_shared_key(y1, x2, P)

    print("[SERVER]> Key Generated -> K2:",K2)
    

    K1=int(conn.recv(1024).decode())

    if(K1==K2):
        print("[SERVER]> Keys have been exchanged successfully")
    else:
        print("[SERVER]> keys have not been exchanged succesfully")
    conn.close()


'''
Step 1: Alice and Bob get public numbers P = 23, G = 9

Step 2: Alice selected a private key a = 4 and
        Bob selected a private key b = 3

Step 3: Alice and Bob compute public values
Alice:    x =(9^4 mod 23) = (6561 mod 23) = 6
        Bob:    y = (9^3 mod 23) = (729 mod 23)  = 16

Step 4: Alice and Bob exchange public numbers

Step 5: Alice receives public key y =16 and
        Bob receives public key x = 6

Step 6: Alice and Bob compute symmetric keys
        Alice:  ka = y^a mod p = 65536 mod 23 = 9
        Bob:    kb = x^b mod p = 216 mod 23 = 9

Step 7: 9 is the shared secret.

'''