import numpy as np

np.random.seed(10)
initial_seed = '0110'
iterations = 10000
k = len(initial_seed)

# generate 2^k uniform random number in [0,1)
transition_probabilities = np.random.uniform(0, 1, int(2 ** k))

# 2 x 2^k matrix
# whose (i, j) entry defines probability of getting i which is 0/1 after known string j (in binary)
transition_matrix = np.vstack([transition_probabilities, 1-transition_probabilities])

f = open('small-data.txt', 'w')
f.write(initial_seed)

current_state = initial_seed

# generate data
for i in range(iterations):
	# set index to decimal version of current_state
	index = int(str(current_state), 2)

	# generate number & change state according to transition_matrix defined earlier
	if np.random.uniform() < transition_matrix[0][index]:
		# remove first element of current state & append 0 to the current state
		current_state = current_state[1:] + '0'
		f.write('0')
	else:
		# remove first element of current state & append 1 to the current state
		current_state = current_state[1:] + '1'
		f.write('1')