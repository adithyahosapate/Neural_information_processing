import numpy as np
import matplotlib.pyplot as plt
#base distribution is standard gaussian 
alpha=1
epsillon=1e-4
remaining_length=1
points=[]
weights=[]

while remaining_length>epsillon:
	sampled_point=np.random.normal()
	print(sampled_point)
	points.append(sampled_point)
	fraction=np.random.beta(1,alpha)
	weights.append(fraction*remaining_length)
	remaining_length=remaining_length*(1-fraction)

plt.stem(points,weights)

x=np.linspace(-5,5,1000)
pdf=np.exp(-x**2)*1/np.sqrt(2*np.pi)
plt.plot(x,pdf)

plt.show()