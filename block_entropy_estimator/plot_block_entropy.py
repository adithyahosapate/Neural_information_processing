import matplotlib.pyplot as plt
import pickle as pkl

with open('entropies.pkl','rb') as f:
	entropies=pkl.load(f)

for i in range(len(entropies)):
	entropies[i]=entropies[i]/(i+1.0)

plt.plot(range(1,len(entropies)+1),entropies)
plt.show()