import socket

host='127.0.0.1'
port=8080

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("The modular inverse does not exist")
    else:
        return x % m


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


# ElGamal encryption
def elgamal_encrypt(q, a, ya, m, k):
    c1 = pow(a, k, q)
    c2 = (m * pow(ya, k, q)) % q
    return c1, c2


q = int(input("CLIENT]> Enter the prime modulus (Q): "))
a = int(input("[CLIENT]> Enter the generator (G): "))
m = int(input("[CLIENT]> Enter plain text : "))
k = int(input("[CLIENT]> Enter the Random key value:"))


client.send(str(q).encode())
client.send(str(a).encode())



ya = int(client.recv(1024).decode())
print("[SERVER]> Public Key : ", ya)

c1, c2 = elgamal_encrypt(q, a, ya, m, k)
print(f"[CLIENT]> Cipher : {c1,c2}")

client.send(str(c1).encode())
client.send(str(c2).encode())

reply=client.recv(1024).decode()
print(f"[SERVER]> Decrypted text : {reply}")
client.close()