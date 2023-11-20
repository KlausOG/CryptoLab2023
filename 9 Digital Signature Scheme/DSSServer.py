import socket
host = "127.0.0.1"
port = 5842
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen()
client_socket,addr = server_socket.accept()
msg = client_socket.recv(1024).decode()
[p,q,s,hash_val,r,g,y] = map(int,msg.split(" "))
print("Verifying...")
w = pow(s,-1,q)
u1= (hash_val*w) % q
u2 = (r*w) % q
v = ((pow(g,u1)*pow(y,u2))%p)%q
print(f"v={v}\nr={r}")
if(v==r):   
    print("Verification Successful")