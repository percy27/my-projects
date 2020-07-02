import math
import random
import socket

def generator(a,b,n):
	if(4*(a**3)+27*(b**2)!=0):
		x = 1
		while True:
			rhs = (x**3 + a*x + b)%n
			y = int(math.sqrt(rhs))
			lhs = (y**2)%n
			if(lhs == rhs):
				return [x,y]
			else:
				x+=1
	else:
		print("Enter other ")






so = socket.socket()
host = socket.gethostname()
port = 1234
so.bind((host,port))
so.listen(1)
client,addr = so.accept()
print("Connected with ",addr)


a = int(input("Enter a: "))
b = int(input("Enter b: "))
n = int(input("Enter n: "))


gen = generator(a,b,n)
print("gen",gen)

n_str = str(n)
client.send(n_str.encode())

g_s_x = str(gen[0])
g_s_y = str(gen[1])

g_str = g_s_x +' '+ g_s_y
client.send(g_str.encode())

#private_A = random.randint(1,25)
#public_A = [private_A*gen[0],private_A*gen[1]]
#print("public_A ",public_A)
public_b_str = client.recv(1024).decode()

p_b_x ,p_b_y = public_b_str.split(' ')
public_B = [int(p_b_x),int(p_b_y)]
print("public_B ",public_B)


#str_p_a = str(public_A[0]) +' '+ str(public_A[1])
#client.send(str_p_a.encode())

m = int(input("Enter msg "))
x = random.randint(1,50)


c1 = (x*(gen[0]+gen[1]))%n
c2 = (m + x*(public_B[0]+public_B[1]))%n

cipher = [c1,c2]
print("cipher",cipher)

c_str = str(c1)+' '+str(c2)
client.send(c_str.encode())


so.close()


