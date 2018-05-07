# https://en.wikipedia.org/wiki/Dirichlet_process#The_stick-breaking_process

import numpy as np
import matplotlib.pyplot as plt

# note: standard gaussian as a base distribution

alpha = 0.5

def sample(alpha):
	epsillon = 1e-4
	remaining_length = 1
	points = []
	weights = []
	while remaining_length > epsillon:
		# sample point from base distribution, which is gaussian in this case
		sampled_point = np.random.normal()
		points.append(sampled_point)
		#print(sampled_point)
		
		# braking-off fraction of total stick, fraction choosen according to BETA distribution 
		fraction = np.random.beta(1,alpha)
		# store broken-off piece
		weights.append(fraction*remaining_length)
		remaining_length = remaining_length*(1-fraction)

	# plot PMF of this Dirichlet Process
	# plt.stem(points, weights)
	return (points,weights)

# plot base distribution, which is gaussian in this case

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
points,weights=sample(0.5)
ax1.stem(points,weights)
ax1.set_title("alpha 0.5")
points,weights=sample(5)
ax2.stem(points,weights)
ax2.set_title("alpha 5")

points,weights=sample(10)
ax3.stem(points,weights)
ax3.set_title("alpha 10")

points,weights=sample(30)
ax4.stem(points,weights)
ax4.set_title("alpha 30")


x = np.linspace(-5, 5, 1000)
pdf = np.exp(-x**2)*1/np.sqrt(2*np.pi)
ax1.plot(x, pdf)
ax2.plot(x, pdf)
ax3.plot(x, pdf)
ax4.plot(x, pdf)


plt.show()