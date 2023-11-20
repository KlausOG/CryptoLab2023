import socket 
import math

host='127.0.0.1'
port=8080
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server is listening...")


def decrypt(cipher,key):
	plain = ""

	# Track key indices
	k_indx = 0

	# Track msg indices
	msg_indx = 0
	msg_len = float(len(cipher))
	msg_lst = list(cipher)

	# Calculate column of the matrix
	col = len(key)
	
	# Calculate maximum row of the matrix
	row = int(math.ceil(msg_len / col))

	# Convert key into list and sort alphabetically so we can access each character by its alphabetical position.
	key_lst = sorted(list(key))

	# Create an empty matrix to store deciphered message
	dec_cipher = []
	for _ in range(row):
		dec_cipher += [[None] * col]

	# Arrange the matrix column wise according to permutation order by adding into new matrix
	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])

		for j in range(row):
			dec_cipher[j][curr_idx] = msg_lst[msg_indx]
			msg_indx += 1
		k_indx += 1

	# Convert decrypted msg matrix into a string
	plain = ''.join(sum(dec_cipher, []))
	
	null_count = plain.count('_')

	if null_count > 0:
		return plain[: -null_count]

	return plain


while True:
    conn,addr=server.accept()
    print("[SERVER]> Connection established from ",addr," on port ",port)
    cipher=conn.recv(1024).decode()
    print("[CLIENT]> ",cipher)
    key=input("[SERVER]> Enter key to decode : ")
    plain=decrypt(cipher,key)
    print("[SERVER]> Decrypted plain text : ",plain)
    conn.send(plain.encode())
    print("[SERVER]> Message Sent !")
    conn.close()
