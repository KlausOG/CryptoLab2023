import math

rotate_by = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
			 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
			 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
			 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
constants = [int(abs(math.sin(i+1)) * 4294967296) & 0xFFFFFFFF for i in range(64)]
init_MDBuffer = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

def pad(msg):
	msg_len_in_bits = (8*len(msg)) & 0xffffffffffffffff
	msg.append(0x80)
	while len(msg)%64 != 56:
		msg.append(0)
	msg += msg_len_in_bits.to_bytes(8, byteorder='little') 
	return msg

def leftRotate(x, amount):
	x &= 0xFFFFFFFF
	return (x << amount | x >> (32-amount)) & 0xFFFFFFFF

def processMessage(msg):
	init_temp = init_MDBuffer[:]
	for offset in range(0, len(msg), 64):
		A, B, C, D = init_temp 
		block = msg[offset : offset+64] 
		for i in range(64): 
			if i < 16:
				func = lambda b, c, d: (b & c) | (~b & d)
				index_func = lambda i: i
			elif i >= 16 and i < 32:
				func = lambda b, c, d: (d & b) | (~d & c)
				index_func = lambda i: (5*i + 1)%16
			elif i >= 32 and i < 48:
				func = lambda b, c, d: b ^ c ^ d
				index_func = lambda i: (3*i + 5)%16
			elif i >= 48 and i < 64:
				func = lambda b, c, d: c ^ (b | ~d)
				index_func = lambda i: (7*i)%16
			F = func(B, C, D) 
			G = index_func(i) 
			to_rotate = A + F + constants[i] + int.from_bytes(block[4*G : 4*G + 4], byteorder='little')
			newB = (B + leftRotate(to_rotate, rotate_by[i])) & 0xFFFFFFFF
			A, B, C, D = D, newB, B, C
		for i, val in enumerate([A, B, C, D]):
			init_temp[i] += val
			init_temp[i] &= 0xFFFFFFFF
	return sum(buffer_content<<(32*i) for i, buffer_content in enumerate(init_temp))

def mdToHex(digest):
	raw = digest.to_bytes(16, byteorder='little')
	return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))

def md5(msg):
	msg = bytearray(msg, 'ascii') 
	msg = pad(msg)
	processed_msg = processMessage(msg)
	message_hash = mdToHex(processed_msg)
	print("MD5 Hash : ", message_hash)

if __name__ == '__main__':
	message = input("Enter message to generate hash : ")
	md5(message)


'''
MD5 algorithm follows the following steps 

1. 	Append Padding Bits: In the first step, we add padding bits in the original message in such a way that the total length of the message is 64 bits less than the exact multiple of 512. 
	Suppose we are given a message of 1000 bits. Now we have to add padding bits to the original message. Here we will add 472 padding bits to the original message.  After adding the padding bits the size of the original message/output of the first step will be 1472 i.e. 64 bits less than an exact multiple of 512 (i.e. 512*3 = 1536).

	Length(original message + padding bits) =  512 * i – 64 where i = 1,2,3 . . . 

2. Append Length Bits: In this step, we add the length bit in the output of the first step in such a way that the total number of the bits is the perfect multiple of 512. Simply, here we add the 64-bit as a length bit in the output of the first step. 
i.e. output of first step = 512 * n – 64 
	length bits = 64. 

	After adding both we will get 512 * n i.e. the exact multiple of 512.

3. Initialize MD buffer: Here, we use the 4 buffers i.e. J, K, L, and M. The size of each buffer is 32 bits.
 	- J = 0x67425301
    - K = 0xEDFCBA45
    - L = 0x98CBADFE
    - M = 0x13DCE476

4. Process Each 512-bit Block: This is the most important step of the MD5 algorithm. Here, a total of 64 operations are performed in 4 rounds. In the 1st round, 16 operations will be performed, 2nd round 16 operations will be performed, 3rd round 16 operations will be performed, and in the 4th round, 16 operations will be performed. We apply a different function on each round i.e. for the 1st round we apply the F function, for the 2nd G function, 3rd for the H function, and 4th for the I function. 
We perform OR, AND, XOR, and NOT (basically these are logic gates) for calculating functions. We use 3 buffers for each function i.e. K, L, M.

     - F(K,L,M) = (K AND L) OR (NOT K  AND M)
     - G(K,L,M) = (K AND L) OR (L AND NOT M)
     - H(K,L,M) = K XOR L XOR M
     - I(K,L,M) = L XOR (K OR NOT M)

After applying the function now we perform an operation on each block. For performing operations we need 

add modulo 2^32
M[i] – 32 bit message.
K[i] – 32-bit constant.
<<<n – Left shift by n bits.
Now take input as initialize MD buffer i.e. J, K, L, M. Output of  K will be fed in L, L will be fed into M, and M will be fed into J. After doing this now we perform some operations to find the output for J.

In the first step, Outputs of K, L, and M are taken and then the function F is applied to them. We will add modulo 232  bits for the output of this with J.
In the second step, we add the M[i] bit message with the output of the first step.
Then add 32 bits constant i.e. K[i] to the output of the second step. 
At last, we do left shift operation by n (can be any value of n) and addition modulo by 232.
After all steps, the result of J will be fed into K. Now same steps will be used for all functions G, H, and I. After performing all 64 operations we will get our message digest.

Output:

After all, rounds have been performed, the buffer J, K, L, and M contains the MD5 output starting with the lower bit J and ending with Higher bits M. 	 
'''