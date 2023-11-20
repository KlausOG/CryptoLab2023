import socket
import math

host='127.0.0.1'
port=8080

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

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

P = int(client.recv(1024).decode())
G = int(client.recv(1024).decode())

if not (prime_checker(P) and primitive_check(G, P)):
    print("[CLIENT]> Invalid values for P and G received from server.")
    client.close()

x1 = int(input("[CLIENT]> Enter the Client's Private Key: "))
y1 = pow(G, x1, P)
print(f"[CLIENT]> Computed Public Component : {y1}")
client.send(str(y1).encode())

y2 = int(client.recv(1024).decode())
print(f"[SERVER]> Server's Public Component : {y2}")

K1 = calculate_shared_key(y2, x1, P)

print("[CLIENT]> Key Generated -> K1:",K1)

client.send(str(K1).encode())
client.close()