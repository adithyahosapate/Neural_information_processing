import numpy as np
import matplotlib.pyplot as plt
import pickle
def block_entropy_estimator(k,data):
	frequency_dict={}

	N=len(data)
	#print(N)
	for i in range(N-k):
		string=data[i:i+k]
		if string in frequency_dict.keys():
			frequency_dict[string]+=1
		else:
			frequency_dict[string]=1	
	entropy_sum=0		
	for v in frequency_dict.values():	
		if v==0:
			continue
		else:
			entropy_sum+=-v/N*np.log(v/N)
	return entropy_sum		


with open('../data.txt','r') as f:
	data=f.read()

entropies=[]

for k in range(1,50):
	entropy_k=block_entropy_estimator(k,data)
	entropies.append(entropy_k)
	print(entropy_k)

with open('entropies.pkl','wb') as f:
	pickle.dump(entropies,f)