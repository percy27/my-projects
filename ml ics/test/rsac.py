import math
import random
import socket
so = socket.socket()
host = socket.gethostname()
port =1234
so.connect((host,port))

msg_a_b = so.recv(1024).decode()

a_s,b_s = msg_a_b.split(' ')
a = int(a_s)
b = int(b_s)



print("a",a)
print("b",b)

phi = (a-1)*(b-1)
n = a*b

str_e = so.recv(1024).decode()
e = int(str_e)
print("e",e)


d = 0 

for i in range(1,1000000):
	x = (phi*i+1)
	if (x%e) ==0:
		print("i",i)
		d = x/e
		break

d = int(d)
print("d",d)


str_c = so.recv(1024).decode()
c = int(str_c)
print("cipher ",c)

plain = pow(c,d,n)
print("plain ",plain)	


so.close()