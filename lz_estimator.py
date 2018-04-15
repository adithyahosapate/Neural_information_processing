import sys
import numpy as np
import matplotlib.pyplot as plt
# C: blocks_discovered
# u: last_partition
# v: current_block_length
# vmax: max_length_discovered

def lz_complexity(s):
    n = len(s)
    # just to make it 1 indexed, LOL
    s = "p" + s
    i = 0
    blocks_discovered = 1
    last_partition = 1
    current_block_length = 1
    max_length_discovered = 1

    while last_partition + current_block_length <= n:
        #print(last_partition)
        # print("i={} u={} v={}".format(i, last_partition, current_block_length))
        """ if current block part is matching with already discovered, then increment current block length    """
        if s[i + current_block_length] == s[last_partition + current_block_length]:
            current_block_length += 1
        else:
            max_length_discovered = max(current_block_length, max_length_discovered)

            """ current block doesn't match whole discovered part,
                so we change starting position of discovered part to check if larger substring exist """
            i += 1

            # if i = last_partition, then we have computed all possible combinations
            if i == last_partition:
                # increment blocks discovered
                blocks_discovered += 1

                # put new partition at max length discovered
                last_partition += max_length_discovered

                # reset parameters
                i = 0
                current_block_length = 1
                max_length_discovered = 1
            # else we see from starting of undiscovered part
            else:
                current_block_length = 1
                
    # if we stopped, but last block is still remain uncounted
    if current_block_length != 1:
        blocks_discovered += 1
    
    return blocks_discovered

if __name__ == "__main__":
    # print("input: {}".format(sys.argv[1]))
    f = open(sys.argv[1], "r")
    dataset=f.read()
    entropies_list=[]
    for i in range(1000,10000,1000):
        entropies_list.append(lz_complexity(dataset[:i])/(i+0.0)*np.log(i))
    plt.semilogx(range(1000, 10000, 1000), entropies_list)
    plt.xlabel("Data Length")
    plt.ylabel("Entropy Rate")
    plt.title("Entropy Rate VS Data Length using LZ complexity")
    plt.show()