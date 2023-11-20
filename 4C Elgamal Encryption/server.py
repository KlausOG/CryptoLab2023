import socket 

host='127.0.0.1'
port=8080
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server is listening...")

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("The modular inverse does not exist")
    else:
        return x % m
def elgamal_keygen(q, a, xa):
    ya = pow(a, xa, q) 
    return q, a, xa, ya

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


def elgamal_decrypt(q, xa, c1, c2):
    k_inverse = mod_inverse(c1 ** xa, q)
    m = (c2 * k_inverse) % q
    return m

while True:
    conn,addr=server.accept()
    print("[SERVER]> Connection established from ",addr," on port ",port)
    q=int(conn.recv(1024).decode())
    a=int(conn.recv(1024).decode())


    xa = int(input("[SERVER]> Enter the Server's private key : "))
    q, a, xa, ya = elgamal_keygen(q, a, xa)

  
    conn.send(str(ya).encode())

   
    c1 = int(conn.recv(1024).decode())
    c2 = int(conn.recv(1024).decode())
    print(f"[CLIENT]> Ciphertext components from Client: (c1,c2) -> ({c1},{c2})")

   
    decrypted_message = elgamal_decrypt(q, xa, c1, c2)
    print("[SERVER]> Decrypted text:", decrypted_message)

    conn.send(str(decrypted_message).encode())
    conn.close()



'''
Idea of ElGamal cryptosystem: 

Suppose Alice wants to communicate with Bob.  

Bob generates public and private keys: 
    Bob chooses a very large number q and a cyclic group Fq.
    From the cyclic group Fq, he choose any element g and
    an element a such that gcd(a, q) = 1.
    Then he computes h = g^a.
    Bob publishes F, h = g^a, q, and g as his public key and retains a as private key.

Alice encrypts data using Bob’s public key : 
    Alice selects an element k from cyclic group F 
    such that gcd(k, q) = 1.
    Then she computes p = g^k and s = h^k = g^ak.
    She multiples s with M.
    Then she sends (p, M*s) = (g^k, M*s).

Bob decrypts the message : 
    Bob calculates s′ = p^a = g^ak.
    He divides M*s by s′ to obtain M as s = s′.
'''