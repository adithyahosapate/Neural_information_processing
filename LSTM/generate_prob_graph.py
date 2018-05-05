import csv
import sys
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print("Enter csv file with probabilities")
    exit()

file_name = sys.argv[1] 
csv_file = open(file_name, "r")
csv_reader = csv.reader(csv_file)
weights = []
# data = csv_file.read()
# data_list = []
# for char in data[4205:4905]:
# 	data_list.append(int(char))


# plt.plot(range(len(data_list)), data_list)
# plt.show()
for row in csv_reader:
    weights.append(row[1])
plt.plot(range(len(weights)), weights, 'o')
plt.xlabel("Decimal Representation of binary string s")
plt.ylabel("p(1|s)")
plt.title("Transition Probabilities using LSTM")
plt.savefig("transition-probabilities.png")
plt.show()
