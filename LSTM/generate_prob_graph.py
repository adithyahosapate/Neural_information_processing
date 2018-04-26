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

for row in csv_reader:
    weights.append(row[1])
plt.plot(range(len(weights)), weights, 'o')
plt.show()