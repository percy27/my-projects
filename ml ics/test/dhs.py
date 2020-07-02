import math
import random
import socket
so = socket.socket()
host = socket.gethostname()
port =1234
so.bind((host,port))
so.listen(1)
client,addr = so.accept()

def isPrime(num):
	if(num==2):
		return True
	else:
		for i in range(2,num-1):
			if num%i==0:
				return False	
		return True


while(True):
	p = random.randint(2,25)
	if(isPrime(p)):
		break


while(True):
	q = random.randint(25,50)
	if(isPrime(q)):
		break

print("p",p)
print("q",q)

msg_p_q = str(p)+' '+str(q)
client.send(msg_p_q.encode())		

a = random.randint(1,30)

R = pow(q,a,p)
r_s = str(R)
client.send(r_s.encode())

s_s = client.recv(1024).decode()
S = int(s_s)

key = pow(S,a,p)
print("key",key)


so.close()