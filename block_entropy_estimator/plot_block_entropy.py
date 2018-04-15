import matplotlib.pyplot as plt
import pickle as pkl
import sys

if len(sys.argv) != 3:
        print("Give data & output image name with format as a command line argument")
        exit()

data = sys.argv[1]
save_as = sys.argv[2]

with open(data,'rb') as f:
	entropies = pkl.load(f)

for i in range(len(entropies)):
	entropies[i] = entropies[i] / (i+1.0)

fig = plt.figure()
plt.plot(range(1,len(entropies)+1), entropies)
plt.xlabel("Block size")
plt.ylabel("Entropy rate")
plt.title("Entropy Rate vs Bock size")
plt.show()
fig.savefig(save_as, dpi=fig.dpi)