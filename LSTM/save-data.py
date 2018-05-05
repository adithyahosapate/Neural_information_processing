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
import csv


def decimalToBinary(length, sInDecimal):
    s = bin(sInDecimal)[2:]
    while len(s) < length:
        s = "0" + s
    return s


warnings.filterwarnings("ignore")
parser = argparse.ArgumentParser(description='Test A Neural Net')
parser.add_argument('-weights', action="store", dest="weights",
                    help='Generate Bit_string', default="None")
parser.add_argument('-length', action="store", dest="length",default=100,
                    help='length', type=int)

weights = parser.parse_args().weights
length = parser.parse_args().length

if weights == "None":
    print("First Train model")
    exit()

model = load_model(weights)
csv_file = open("prob.csv", "w")
csv_writer = csv.writer(csv_file)
one_hot_dict = {0: np.array([1.0, 0.0]), 1: np.array([0.0, 1.0])}

l = length
for sInDecimal in range(0, 2 ** l):
    string = decimalToBinary(l, sInDecimal)
    string_char_list = [int(string[i],10) for i in range(len(string))] 
    data = [one_hot_dict[num] for num in string_char_list]
    prediction = model.predict(np.array([data]))
    csv_writer.writerow(["p(1|" + string + ")", prediction[0][1]])
csv_file.close()