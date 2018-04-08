import sys

def calculateProb():
    # prob(1) given s = phi
    p1_s_phi = (count_dictionary["1"] / (alpha + N)) + (alpha / (alpha + N))*p_phi
    
    for s in combinations:
        if len(s) > k:
            break

        c_s1 = count_dictionary[s+"1"]
        c_s = count_dictionary[s]
        
        if len(s) == 1:
            p = (c_s1 / (alpha + c_s)) + (alpha / (alpha + c_s))*p1_s_phi
        else:
            p = (c_s1 / (alpha + c_s)) + (alpha / (alpha + c_s))*prob_dictionary[s[1:]]

        prob_dictionary[s] = p


def saveCombinations():
    # generate all combinations of string of length <= k + 1
    for length in range(1, k + 2):
        for sInDecimal in range(0, 2 ** length):
            string = decimalToBinary(length, sInDecimal)
            combinations.append(string)

   
def decimalToBinary(length, sInDecimal):
    s = bin(sInDecimal)[2:]
    while len(s) < length:
        s = "0" + s    
    return s


def countOccurence():
    # count how much time each string of length <= k+1 appears in dataset & store in dict
    for s in combinations:
        count_dictionary[s] = count(s)


def count(s):
    count = 0
    # open the data file
    f = open(dataset, "r")

    # read first chars of length |s|
    data = f.read(len(s))
    if s == data:
        count += 1

    char = f.read(1)
    while char:
        # append char to data remove first character 
        data = data[1:] + char
        
        if s == data:
            count += 1
        char = f.read(1)

    f.close()
    return count


if __name__ == '__main__':
    # dataset file require as a command line argument
    if len(sys.argv) != 2:
        print("Give dataset as a command line argument")
        exit()
    
    # dataset name
    dataset = sys.argv[1]

    # k'th order markov chain
    k = 4

    # length of data string
    f = open(dataset, "r")
    N = len(f.read())
    f.close()
    
    # all combinations of string of length <= k + 1
    combinations = []
    saveCombinations()
    
    # dictionary to store how many times string is present in data as a substring
    count_dictionary = {}
    countOccurence()

    # prior prob of 1  
    p_phi = 0.5
    
    # alpha parameter
    alpha = 0.3

    # dictionary to store prob of 1 after certain string
    prob_dictionary = {}
    calculateProb()

    # write results in csv format file
    f = open("result-test.csv", "w")
    f.write("string,occurance,result,prob\n")
    for s in combinations:
        if len(s) > k:
            f.write("\'" + s + "\'" + "," + str(count_dictionary[s]) + "\n")
        else:    
            f.write("\'" + s + "\'" + "," + str(count_dictionary[s]) + "," + "p(1|" + s + ")," + str(prob_dictionary[s]) + "\n")
    f.close()