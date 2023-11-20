import socket 
import math

host='127.0.0.1'
port=8080
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server is listening...")

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

def decrypt(cipher):
	cipher = cipher[2:-1]
	plain = ""
	for character in cipher:
		c = ord(character) - ord('a')
		m = pow(c, d)
		m = math.fmod(m, n)
		m = int(m)
		plain += chr(m + ord('a'))
	return plain


while True:
    conn,addr=server.accept()
    print("[SERVER]> Connection established from ",addr," on port ",port)
    cipher=conn.recv(1024)
    print("[CLIENT]> ",cipher)
    print(f"[SERVER]> Decrypting with private key (n,d) : [{n},{int(d)}]")
    plain=decrypt(str(cipher))
    print("[SERVER]> Decrypted plain text : ",plain)
    conn.send(plain.encode())
    print("[SERVER]> Message Sent !")
    conn.close()



'''
Select two prime no's. Suppose P = 53 and Q = 59.
Now First part of the Public key  : n = P*Q = 3127.
 We also need a small exponent say e : 
But e Must be 
An integer.
Not be a factor of Φ(n). 
1 < e < Φ(n) [Φ(n) is discussed below], 
Let us now consider it to be equal to 3.
    Our Public Key is made of n and e

>> Generating Private Key: 

We need to calculate Φ(n) :
Such that Φ(n) = (P-1)(Q-1)     
      so,  Φ(n) = 3016
    Now calculate Private Key, d : 
d = (k*Φ(n) + 1) / e for some integer k
For k = 2, value of d is 2011.

Now we are ready with our – Public Key ( n = 3127 and e = 3) and Private Key(d = 2011) Now we will encrypt “HI”:

Convert letters to numbers : H  = 8 and I = 9
    Thus Encrypted Data c = (89^e)mod n 
Thus our Encrypted Data comes out to be 1394
Now we will decrypt 1394 : 
    Decrypted Data = (c^d)mod n
Thus our Encrypted Data comes out to be 89
8 = H and I = 9 i.e. "HI".
'''