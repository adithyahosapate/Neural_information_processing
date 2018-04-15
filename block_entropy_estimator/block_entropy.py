import numpy as np
import matplotlib.pyplot as plt
import pickle
import sys

def block_entropy_estimator(k,data):
	frequency_dict = {}

	N = len(data)
	for i in range(N-k):
		string = data[i:i+k]
		if string in frequency_dict.keys():
			frequency_dict[string] += 1
		else:
			frequency_dict[string] = 1	
	entropy_sum = 0		
	
	for v in frequency_dict.values():	
		entropy_sum += -v/N*np.log(v/N)
	
	return entropy_sum		


if len(sys.argv) != 3:
        print("Give dataset & output file name as a command line argument")
        exit()

dataset = sys.argv[1]
save_name = sys.argv[2] + ".pkl"

with open(dataset,'r') as f:
	data = f.read()

entropies = []

for k in range(0,100):
	entropy_k = block_entropy_estimator(k,data)
	entropies.append(entropy_k)
	print(entropy_k)

with open(save_name,'wb') as f:
	pickle.dump(entropies,f)