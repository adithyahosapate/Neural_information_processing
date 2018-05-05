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
for char in data[4205:4905]:
	data_list.append(int(char))

plt.plot(range(len(data_list)), data_list)
plt.xlabel("Time")
plt.ylabel("Spike")
plt.title("Spikes using LSTM")
plt.savefig("spikes_using_lstm.png")
plt.show()