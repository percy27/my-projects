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

def isCoprime(a,b):
	if(math.gcd(a,b)==1):
		return True
	else:
		return False	

while(True):
	a= random.randint(2,25)
	if(isPrime(a)):
		break


while(True):
	b = random.randint(25,40)
	if(isPrime(b)):
		break


		

print("a",a)
print("b",b)

msg_a_b = str(a)+' '+str(b)
client.send(msg_a_b.encode())

n = a*b
phi = (a-1)*(b-1)

e_lst = []
for i in range(2,30):
	if(isCoprime(i,phi)):
		e_lst.append(i)

ind = random.randint(0,len(e_lst))
e = e_lst[ind]

str_e = str(e)
print("e",e)
client.send(str_e.encode())

m = int(input("enter msg: "))
cipher = pow(m,e,n)
print("cipher",cipher)
str_c = str(cipher)

client.send(str_c.encode())


so.close()