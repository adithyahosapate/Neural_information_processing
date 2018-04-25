import warnings
import argparse
import numpy as np
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import matplotlib.pyplot as plt
from keras.models import load_model
import sys
import time
import scipy.io
import datetime

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(description='Test A Neural Net')
parser.add_argument('-weights', action="store",dest="weights",
                    help='Generate Bit_string',default="None")
parser.add_argument('-length', action="store",dest="length",default=100
                    ,help='length',type=int)



weights=parser.parse_args().weights
length=parser.parse_args().length
f=open('lstm_data.txt',"w")

initial_seed=[0,0,0,0,0,0,0,0,0,0]
if weights!="None":
    model=load_model(weights)
curr=initial_seed    
one_hot_dict={0:np.array([1.0,0.0]),1:np.array([0.0,1.0])}
for i in range(length):
    data=[one_hot_dict[num] for num in curr]
    prediction=model.predict(np.array([data]))
    if np.random.uniform()<prediction[0][0]:
    	f.write("0")
    	curr=curr[1:]
    	curr.append(0)

    else:
    	f.write("1")
    	curr=curr[1:]
    	curr.append(1)
f.close()    		
       