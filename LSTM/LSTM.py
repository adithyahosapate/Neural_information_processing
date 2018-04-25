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

today = datetime.date.today()

#layer Lstm with fully connect layer at the end


warnings.filterwarnings("ignore")


def build_model(layers):
    model = Sequential()

    model.add(LSTM(
        input_dim=layers[0],
        output_dim=layers[1],
        return_sequences=True))
    model.add(Dropout(0.2))

    model.add(LSTM(
        layers[2],
        return_sequences=False))
    model.add(Dropout(0.2))

    model.add(Dense(
        output_dim=layers[3]))
    model.add(Activation("softmax"))

    start = time.time()
    model.compile(loss="categorical_crossentropy", optimizer="adam")
    print("Compilation Time : ", time.time() - start)
    return model


def load_data(path,length,stride):
    mat=scipy.io.loadmat(path)
    bitstring=mat['spike_bitstring']
    bitstring=bitstring.reshape([-1])
    data_array=[]
    label_array=[]
    one_hot_dict={0:np.array([1.0,0.0]),1:np.array([0.0,1.0])}
    for i in range(0,bitstring.shape[0]-length,stride):
        if sum(bitstring[i:i+length])<=6 and np.random.normal()<0.9:
            continue
        else:    
            data=[one_hot_dict[num] for num in bitstring[i:i+length]]
            data_array.append(np.array(data))
            label_array.append(one_hot_dict[bitstring[i+length]])


    print(np.array(data_array),np.array(label_array))
    return (np.array(data_array),np.array(label_array))





#Hyperparameters
layers=[2,50,100,2]    
batch_size=10
data_stride=1
Backprop_length=10
####################

parser = argparse.ArgumentParser(description='Train A Neural Net')
parser.add_argument('-weights', action="store",dest="weights",
                    help='Retrain using specified weights(if not specified, trains from scratch)',default="None")
parser.add_argument('-epochs', action="store",dest="epochs",default=100
                    ,help='Number of epochs',type=int)
parser.add_argument('-data',action="store",dest="path",required=True)

print(parser.parse_args())

data_path=parser.parse_args().path
epochs=parser.parse_args().epochs
weights=parser.parse_args().weights

if weights!="None":
    model=load_model(weights)
else:
    model=build_model(layers)

X_train,Y_train=load_data(data_path,Backprop_length,data_stride)
model.fit(
    X_train,
    Y_train,
    batch_size=batch_size,
    epochs=epochs)

model.save('trained_{}.h5'.format("now"))
