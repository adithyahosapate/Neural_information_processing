import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import pickle
mat=scipy.io.loadmat('Cell_23_Fluo4gabba_baclofen_10uM_frame240_well_1_5_6_2011_Adthreshold_3STD.mat')
bitstring=mat['spike_bitstring']
bitstring=bitstring.reshape([-1])
string=""
for bit in bitstring:
	string+=str(bit)


# plt.stem(range(0,len(bitstring)),bitstring)
# plt.show()
with open('real_data.txt','w') as f:
	f.write(string)