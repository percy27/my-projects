import math
import random
import socket
so = socket.socket()
host = socket.gethostname()
port =1234
so.connect((host,port))

msg_p_q = so.recv(1024).decode()

p_s,q_s = msg_p_q.split(' ')
p = int(p_s)
q = int(q_s)

print("p",p)
print("q",q)


b = random.randint(30,50)
S = pow(q,b,p)

r_s = so.recv(1024).decode()
R = int(r_s)

S_s = str(S)
so.send(S_s.encode())


key = pow(R,b,p)
print("key",key)

so.close()