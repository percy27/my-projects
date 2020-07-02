import math
import random
import socket

so = socket.socket()
host = socket.gethostname()
port = 1234
so.connect((host,port))

n = int(so.recv(1024).decode())
print('n',n)
g = so.recv(1024).decode()

g_x_s,g_y_s = g.split(' ')


gen = [int(g_x_s),int(g_y_s)]
print("gen",gen)

private_B = random.randint(26,50)
public_B = [private_B*gen[0],private_B*gen[1]]
print("public_B ",public_B)
str_p_b = str(public_B[0]) +' '+ str(public_B[1])
so.send(str_p_b.encode())

#public_a_str = so.recv(1024).decode()

#p_a_x ,p_a_y = public_a_str.split(' ')
#public_A = [int(p_a_x),int(p_a_y)]
#print("public_A ",public_A)


c_str = so.recv(1024).decode()
c_x ,c_y = c_str.split(' ')
cipher = [int(c_x),int(c_y)]
print("cipher",cipher)

r = (private_B*cipher[0])%n

msg = ((cipher[1] -r)%n+n)%n
print("decryp",msg)


so.close()