import matplotlib.pyplot as plt
import math
import numpy as np

k = 3
data = {
	
	(2,4):'y',
    (4,2):'y',
    (4,4):'b',
    (4,6):'y',
    (6,2):'b',
    (6,4):'y'

}

votes = {
	
	'y':0 , 'b':0
}

#print(len(data.keys()))

points = data.keys()
values = data.values()
points = np.array(list(points))
colors = np.array(list(values))
#print(colors)


ex = int(input("x: " ))
ey = int(input("y: "))

dist = []

for  i in range(len(data.keys())):
	dist.append(math.sqrt( (ex-points[i][0])*(ex-points[i][0]) + (ey-points[i][1])*(ey-points[i][1]) ))

dist = np.array(dist)
dist_i = np.argsort(dist)


nearest = [0]*len(data.keys())

c = 0 
for ind in dist_i:
	nearest[ind] = 1
	votes[colors[ind]]+=1
	c +=1
	if(c==k):
		break



winner = ''
maxi = -1
for key in votes.keys():
	if (maxi < votes[key]):
		winner = key
		maxi = votes[key]

	


for i in range(len(data.keys())):
	if(nearest[i]==1):
		plt.scatter(points[i][0],points[i][1],c=colors[i],marker='*',s=100)
	else :
		plt.scatter(points[i][0],points[i][1],c=colors[i])	

plt.scatter(ex,ey,c=winner,marker='*',s=1000)
plt.grid()
plt.show()	