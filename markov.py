import numpy as np


y_1x_1=0.5
y_1x_0=0.5
y_0x_0=0.5
y_0x_1=0.5



initial= 0
print(initial,end=" ")
current_state=initial
for i in range(100):
	if current_state==1:
		if (np.random.uniform()<y_0x_1):
			current_state=0
		else:
			current_state=1
	else:
		if (np.random.uniform()<y_0x_0):
			current_state=0
		else:
			current_state=1
	print(current_state,end=" ")			




				




