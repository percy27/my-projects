import math 
import numpy as np
import matplotlib.pyplot as plt
x_points = [0.1,0.15,0.08,0.16,0.2,0.25,0.24,0.3]
y_points = [0.6,0.71,0.9,0.85,0.3,0.5,0.1,0.2]

for i in range(len(x_points)):
	plt.scatter(x_points[i],y_points[i],color='b')

plt.axis('equal')
plt.grid()
plt.show()	

c0 = np.array([x_points[0],y_points[0]])
c1 = np.array([x_points[7],y_points[7]])


old_c0_x =-1
old_c0_y =-1
old_c1_x =-1
old_c1_y =-1


while True:
	c0_cl = []
	c1_cl = []
	for i in range(len(x_points)):
		dist0 = math.sqrt((c0[0]-x_points[i])**2 + (c0[1]-y_points[i])**2)
		dist1 = math.sqrt((c1[0]-x_points[i])**2 + (c1[1]-y_points[i])**2)
		if dist0 < dist1:
			c0_cl.append(i)
		else :
			c1_cl.append(i)

	su_x = 0 
	su_y = 0 		
	for items in c0_cl:
		su_x += x_points[items]
		su_y += y_points[items]

	su_x = su_x/len(c0_cl)
	su_y = su_y/len(c0_cl)
	c0 = np.array([su_x,su_y])

	su_x = 0 
	su_y = 0 		
	for items in c1_cl:
		su_x += x_points[items]
		su_y += y_points[items]

	su_x = su_x/len(c1_cl)
	su_y = su_y/len(c1_cl)
	c1 = np.array([su_x,su_y])


	for items in c0_cl:
		plt.scatter(x_points[items],y_points[items],color='r')

	for items in c1_cl:
		plt.scatter(x_points[items],y_points[items],color='g')

	plt.scatter(c0[0],c0[1],color='r',marker='*',s=100)
	plt.scatter(c1[0],c1[1],color='g',marker='*',s=100)
	plt.axis('equal')
	plt.show()

	if(old_c0_x == c0[0] and old_c0_y == c0[1] and old_c1_x == c1[0] and old_c1_y == c1[1]):
		break
	else :
		old_c0_x = c0[0]  
		old_c0_y = c0[1]  
		old_c1_x = c1[0]  
		old_c1_y = c1[1]
			

		
for items in c0_cl:
	plt.scatter(x_points[items],y_points[items],color='r')

for items in c1_cl:
	plt.scatter(x_points[items],y_points[items],color='g')

plt.axis('equal')
plt.grid()
plt.show()