import matplotlib.pyplot as plt
import pickle as pkl

with open('entropies.pkl','rb') as f:
	entropies=pkl.load(f)

fig = plt.figure()

for i in range(len(entropies)):
	entropies[i]=entropies[i]/(i+1.0)

plt.plot(range(1,len(entropies)+1),entropies)
plt.xlabel("Block size")
plt.ylabel("Entropy rate")
plt.title("Entropy Rate vs Bock size")
plt.show()
fig.savefig('plot.png',dpi=fig.dpi)
