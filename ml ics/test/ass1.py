
import numpy as np
import matplotlib.pyplot as plt
x = np.array([10,9,2,15,10,16,11,16])
y = np.array([95,80,10,50,45,98,38,93])

x_bar = np.mean(x)
y_bar = np.mean(y)

nume = 0
for i in range(len(x)):
	nume+= (x[i]-x_bar)*(y[i]-y_bar)

deno = 0 
for i in range(len(x)):
	deno+= (x[i]-x_bar)*(x[i]-x_bar)

b1 = nume/deno
b0 = y_bar - b1 * x_bar

y_pred = b1 * x  + b0

mse = 0
for i in range(len(y)):
	mse+= (y[i]-y_pred[i])**2

print(mse)

plt.scatter(x,y,color='blue')
plt.scatter(x_bar,y_bar,color='orange',marker='*',s=100)
plt.plot(x,y_pred,color='green')
plt.grid()
plt.show()





