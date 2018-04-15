import sys

# calculates probability according to formula given in paper
def calculateProb():
    # length of data string
    f = open(dataset, "r")
    N = len(f.read())
    f.close()
    
    if "1" not in freq.keys():
        freq["1"] = 0 

    # prob(1) given s = phi
    p1_s_phi = (freq["1"] / (alpha + N)) + (alpha / (alpha + N))*p_phi

    for s in combinations:
        if len(s) > k:
            break

        c_s1 = 0    
        if s+"1" in freq.keys():
            c_s1 = freq[s + "1"]

        c_s = 0
        if s in freq.keys():
            c_s = freq[s]

        if len(s) == 1:
            p = (c_s1 / (alpha + c_s)) + (alpha / (alpha + c_s))*p1_s_phi
        else:
            p = (c_s1 / (alpha + c_s)) + (alpha / (alpha + c_s))*prob_dictionary[s[1:]]

        prob_dictionary[s] = p


# generate all combinations of binary string of length <= n
def saveCombinations(n):
    for length in range(1, n+1):
        for sInDecimal in range(0, 2 ** length):
            string = decimalToBinary(length, sInDecimal)
            combinations.append(string)


# converts given decimal number to binary in string of length=length
def decimalToBinary(length, sInDecimal):
    s = bin(sInDecimal)[2:]
    while len(s) < length:
        s = "0" + s
    return s


# optimally calculate occarances of length < DIGIT
def optimal_count():
    # store first DIGIT characters
    f = open(dataset, "r")
    data = f.read(DIGIT)
    f.close()

    # last index = 2^DIGIT-3  (2^1 + 2^2 + 2^2 + ... + 2^(DIGIT-1)) - 1 (for 0 indexing)
    for i in range((2**DIGIT)-3, -1, -1):
        count = 0
        s = combinations[i]

        if "0" + s in freq.keys():
            count += freq["0"+s]
        if "1" + s in freq.keys():
            count += freq["1"+s]
        if s == data[:len(s)]:
            count += 1
        
        if count > 0:
            freq[s] = count


# calculate occurance of all string of length = DIGIT
def normal_cal(length):
    for sInDecimal in range(0, 2**length):
        string = decimalToBinary(length, sInDecimal)

        c = count(string)
        if c > 0:
            freq[string] = c    

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


if __name__ == "__main__":
    # dataset file require as a command line argument
    if len(sys.argv) != 2:
        print("Give dataset as a command line argument")
        exit()
    
    # dataset name
    dataset = sys.argv[1]

    # k'th order markov chain
    k = 30

    # calculate occarances of all strings of length <= DIGIT
    DIGIT = k + 1
    
    freq = {}
    
    # save all combinations of binary string of length <= DIGIT 
    combinations = []
    saveCombinations(DIGIT)
    
    # calculate occurance of all string of length = DIGIT
    normal_cal(DIGIT)

    # optimally calculate occarances of length < DIGIT
    optimal_count()

    # prior prob of 1
    p_phi = 0.5

    # alpha parameter
    alpha = 0.3

    # dictionary to store prob of 1 after certain string
    prob_dictionary = {}
    calculateProb()

    # write results in csv format file
    f = open("result1.csv", "w")
    f.write("string,occurance,result,prob\n")
    for s in combinations:
        if len(s) > k:
            if s in freq.keys():
                f.write("\'" + s + "\'" + "," + str(freq[s]) + "\n")
            else:
                f.write("\'" + s + "\'" + "," + "0" + "\n")
        else:
            if s in freq.keys():
                f.write("\'" + s + "\'" + "," + str(freq[s]) + "," + "p(1|" + s + ")," + str(prob_dictionary[s]) + "\n")
            else:
                f.write("\'" + s + "\'" + "," + "0" + "\n")
    f.close()
