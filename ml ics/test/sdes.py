import math

p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
p8 = [6, 3, 7, 4, 8, 5, 10, 9]
ip = [2, 6, 3, 1, 4,8 ,5, 7]
ep = [4, 1, 2, 3, 2, 3, 4, 1]
sb0 = ['01', '00', '11', '10', '11', '10', '01', '00', '00', '10', '01', '11', '11', '01', '11', '10']
sb1 = ['00', '01', '10', '11', '10', '00', '01', '11', '11', '00', '01', '00', '10', '01', '00', '11']
p4 = [2, 4, 3, 1]
ipi = [4, 1, 3, 5, 7, 2, 8, 6]

def permute(inp,type_perm,size):
	arr = [0]*size
	for i in range(size):
		arr[i] = inp[type_perm[i]-1]
	return arr

def shift(inp,val):
	arr = inp[val:] + inp[:val]
	return arr

def join(inp1,inp2):
	size = len(inp1)+len(inp2)
	sz = size//2
	arr = [0]*size
	arr[:sz] = inp1
	arr[sz:] = inp2
	return arr

def split(inp):
	size = len(inp)
	sz = size//2
	arr1 = inp[:sz]
	arr2 = inp[sz:]
	return arr1,arr2

def xor_bits(inp1,inp2):
	size = len(inp1)
	arr = [0]*size
	for i in range(size):
		arr[i] = inp1[i]^inp2[i]
	return arr

def sb_ind(inp):
	row = inp[0]*2 + inp[3]
	col = inp[1]*2 + inp[2]
	return row*4 + col

def sbox(inp,type_s):
	ind = sb_ind(inp)
	arr = [0]*2
	arr[0] = int(type_s[ind][0])
	arr[1] = int(type_s[ind][1])
	return arr	



def doall(inp,key,rnd):
	phase2_1,phase2_2 = split(inp)
	phase3 = permute(phase2_2,ep,8)
	phase4 = xor_bits(phase3,key)
	phase5_1,phase5_2 = split(phase4)
	phase6_1 = sbox(phase5_1,sb0)
	phase6_2 = sbox(phase5_2,sb1)
	phase7 = permute(join(phase6_1,phase6_2),p4,4)
	phase8 = xor_bits(phase7,phase2_1)
	if rnd ==1:
		phase9 = join(phase2_2,phase8)
	else:
		phase9 = join(phase8,phase2_2)
	return phase9
	
def encryp(inp,key1,key2):
	phase1 = permute(inp,ip,8)
	phase2 = doall(phase1,key1,1)
	phase3 = doall(phase2,key2,2)
	phase4 = permute(phase3,ipi,8)
	return phase4

def decrypt(inp,key1,key2):
	phase1 = permute(inp,ip,8)
	phase2 = doall(phase1,key2,1)
	phase3 = doall(phase2,key1,2)
	phase4 = permute(phase3,ipi,8)
	return phase4	



if __name__ == '__main__':
	key = [1,1,1,1,1,1,1,1,1,0]
	temp_key = permute(key,p10,10)
	key_half1,key_half2 = split(temp_key)
	key_half1 = shift(key_half1,1)
	key_half2 = shift(key_half2,1)
	key1 = permute(join(key_half1,key_half2),p8,8)
	key_half1 = shift(key_half1,2)
	key_half2 = shift(key_half2,2)
	key2 = permute(join(key_half1,key_half2),p8,8)

	print("key1",key1)
	print("key2",key2)

	msg = [1,1,1,1,0,0,0,1]
	crypt = encryp(msg,key1,key2)
	print("cryp",crypt)
	decryp = decrypt(crypt,key1,key2)
	print("decrypt",decryp)	
