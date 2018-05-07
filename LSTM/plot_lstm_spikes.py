import csv
import sys
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print("Enter csv file with probabilities")
    exit()

file_name = sys.argv[1]
file = open(file_name, "r")

data = file.read()
data_list = []
for char in data:
	data_list.append(int(char))

plt.plot(range(len(data_list)), data_list)
print(sum(data_list))
plt.xlabel("Time")
plt.ylabel("Spike")
plt.title("Spike Train")
plt.savefig("realspikes.png")
plt.show()