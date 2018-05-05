import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
import sys
import scipy.io

if len(sys.argv) != 4:
	print("Enter dataset, alpha, beta")
	exit()

dataset = sys.argv[1]

# ALPHA
ALPHA = int(sys.argv[2])

# BETA
BETA = int(sys.argv[3])

# count length of dataset
mat = scipy.io.loadmat(dataset)
bitstring = mat['spike_bitstring']
bitstring = bitstring.reshape([-1])	
n1 = np.sum(bitstring)
n = bitstring.shape[0]

x = np.linspace(beta.ppf(0.01, ALPHA+n1, BETA+n-n1),
 				beta.ppf(0.99, ALPHA+n1, BETA+n-n1), 100)
# x = np.linspace(0, 1, 500)
# x = np.linspace(beta.ppf(0.01, ALPHA, BETA),
#  				beta.ppf(0.99, ALPHA, BETA), 100)


a = max(zip(beta.pdf(x, ALPHA+n1, BETA+n-n1),x))[1]
print(a)
print(n1 / n)

# to plot pdf uncomment following & comment all after plt.show()
""" post_plot, = plt.plot(x, beta.pdf(x, ALPHA+n1, BETA+n-n1), label="Posterior PDF")
prior_plot, = plt.plot(x, beta.pdf(x, ALPHA, BETA), 'r-', label="Prior PDF")
plt.xlabel("Bernoulli Variable ${\Theta}$")
plt.ylabel("Probability Density")
plt.title("PDF of Posterior & Prior")
plt.legend(bbox_to_anchor=(0.66, 1), loc=2, borderaxespad=0.)
plt.savefig("pdf_zoomed.png")
plt.show() """


""" To plot Spikes """
plt.plot(range(700), np.random.binomial(size=700, n=1, p=a))
plt.xlabel("Time")
plt.ylabel("Spike")
plt.title("Spikes using Bernoulli model with Beta as Prior")
plt.savefig("spikes_using_estimated_from_beta.png")
plt.show()