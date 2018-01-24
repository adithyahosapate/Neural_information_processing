import numpy as np
import matplotlib.pyplot as plt

dt=0.5
desired_output=50
initial_value=0

coeff=1e-3
input_variable=0

R=60

kp=0.01
ki=0.0001
kd=0.0001

Time_min=0
Time_max=100

error_sum=0
output_var=initial_value

Time=np.linspace(0,100,(Time_max-Time_min)/dt)

output=[]
error_previous=desired_output-initial_value

for T in Time:
	#R=R_initial+coeff*np.max((output_var-37),0)
	output_var=input_variable**2*R+np.random.normal(0,0.2)
	error=output_var-desired_output
	error_sum=error_sum+error
	error_differential=(error-error_previous)/dt
	input_variable=input_variable-kp*error-kd*error_differential-ki*error_sum
	if input_variable<0:
		input_variable=0
	if input_variable>1:
		input_variable=1	
	output.append(output_var)
	error_previous=error
	print(error,error_sum,error_differential)
output=np.array(output)
plt.plot(Time,output)
plt.show()

print(np.var(output))
print(np.mean(output))