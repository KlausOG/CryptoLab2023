import socket
import math

host='127.0.0.1'
port=8080

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def gcd(a, h):
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp

p = 3
q = 7
n = p*q
e = 2
phi = (p-1)*(q-1)

while (e < phi):
	if(gcd(e, phi) == 1):
		break
	else:
		e = e+1

k = 2
d = (1 + (k*phi))/e

def encrypt(plain):
	cipher = ""
	for character in plain:
		val = ord(character) - ord('a')
		c = pow(val, e)
		c = math.fmod(c, n)
		cipher += chr(int(c) + ord('a'))
	return cipher

plain=input("[CLIENT]> Enter plain text : ")
cipher=encrypt(plain)
print(f"[CLIENT]> Encrypting with public key (n,e) : [{n},{e}]")
print("[CLIENT]> Encrypted plain text / Cipher : ",cipher)
client.send(cipher.encode())
print("[CLIENT]> Message Sent successfully !")
reply=client.recv(1024).decode()
print("[SERVER]> Decrypted Text : ",reply)
client.close()