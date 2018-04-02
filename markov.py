import numpy as np

np.random.seed(10)
initial_seed='1010101010'
iterations=10000000
k=10

transition_probabilities=np.random.uniform(0,1,int(2**k))

transition_matrix=np.vstack([transition_probabilities,1-transition_probabilities])


print(transition_matrix)

with open('data.txt','w') as f:
	f.write(initial_seed)



f=open('data.txt','w')

print(int(str(initial_seed),2))
current_state=initial_seed
for i in range(iterations):
	index=int(str(current_state),2)
	if np.random.uniform()<transition_matrix[0][index]:
		current_state=current_state[1:]+'0'
		f.write('0')
	else:
		current_state=current_state[1:]+'1'
		f.write('1')
