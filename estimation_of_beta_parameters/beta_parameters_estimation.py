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

# x = np.linspace(beta.ppf(0.01, ALPHA, BETA),
#  				beta.ppf(0.99, ALPHA, BETA), 100)


a = max(zip(beta.pdf(x, ALPHA+n1, BETA+n-n1),x))[1]
print(a)
print(n1/n)
plt.plot(x, beta.pdf(x, ALPHA+n1, BETA+n-n1))
plt.plot(x, beta.pdf(x, ALPHA, BETA), 'r-')
plt.show()