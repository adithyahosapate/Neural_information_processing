# https://en.wikipedia.org/wiki/Dirichlet_process#The_stick-breaking_process

import numpy as np
import matplotlib.pyplot as plt

# note: standard gaussian as a base distribution

alpha = 0.5
epsillon = 1e-4
remaining_length = 1
points = []
weights = []

while remaining_length > epsillon:
	# sample point from base distribution, which is gaussian in this case
	sampled_point = np.random.normal()
	points.append(sampled_point)
	print(sampled_point)
	
	# braking-off fraction of total stick, fraction choosen according to BETA distribution 
	fraction = np.random.beta(1,alpha)
	# store broken-off piece
	weights.append(fraction*remaining_length)
	remaining_length = remaining_length*(1-fraction)

# plot PMF of this Dirichlet Process
plt.stem(points, weights)

# plot base distribution, which is gaussian in this case
x = np.linspace(-5, 5, 1000)
pdf = np.exp(-x**2)*1/np.sqrt(2*np.pi)
plt.plot(x, pdf)

plt.show()