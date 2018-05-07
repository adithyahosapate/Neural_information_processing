import warnings
import argparse
import numpy as np
import keras
from keras.models import load_model
import sys
import time
import scipy.io
import datetime

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(description='Test the Neural Net')
parser.add_argument('-weights', action="store", dest="weights",
	help='Generate Bit_string', default="None")
parser.add_argument('-d', action="store", dest="test_data",default="None",
	help='Dataset to test the network(in .mat)')


weights = parser.parse_args().weights
test_data = parser.parse_args().test_data

if weights != "None":
	model = load_model(weights)
else:
	print("weights are required")
	exit()

stride=1
length=10

def create_test_dataset(raw_data):
	data_array=[]
	label_array=[]
	one_hot_dict={0:np.array([1.0,0.0]),1:np.array([0.0,1.0])}
	for i in range(0,raw_data.shape[0]-length,stride):
		data=[one_hot_dict[num] for num in raw_data[i:i+length]]
		data_array.append(np.array(data))
		label_array.append(one_hot_dict[raw_data[i+length]])
	# print(np.array(data_array))	
	return (np.array(data_array),np.array(label_array))

mat=scipy.io.loadmat(test_data)
bitstring=mat['spike_bitstring']
bitstring=bitstring.reshape([-1])

features,labels=create_test_dataset(bitstring)

predicted_labels=model.predict(features)
predicted_labels=np.argmax(predicted_labels,axis=1)
labels=np.argmax(labels,axis=1)
# print(predicted_labels)
# print(labels)

correct=0
for i in range(labels.shape[0]):
	if(labels[i]==predicted_labels[i]):
		correct+=1
print("Accuracy:{}".format(correct/(labels.shape[0]+0.0)))		







