import sys
import numpy as np
from pylab import *
import matplotlib.pyplot as plt

# n: number of columns
def readRegret(filename, n, mag):
    data = [0] * n
    with open(filename, 'r') as fin:
        num_line = 0
        for line in fin:
            #data.append(map(float, line.split(' ')))
            line = line.split(' ')
            num_line += 1
            for i in range(n):
                data[i] += float(line[i])*float(mag)
    return [d/num_line for d in data]


# round number : number of columns, 10000:37, 100000:55
def plotRegret():
    roundNum = [1]
    r = 1
    while r < 10000:
        r += pow(10, floor(log10(r)))
        roundNum.append(r)
    #print roundNum, len(roundNum)
    regret1 = readRegret("AvSGD_regret", 37, 1)
    regret2 = readRegret("AvAccSGD_regret", 37, 1)
    regret3 = readRegret("AccSGD_regret", 37, 1)
    baseline1 = [pow(t, -1.0) for t in roundNum]
    baseline2 = [pow(t, -2.0) for t in roundNum]

    fig, ax = plt.subplots()
    
    ax.plot(log10(roundNum), log10(regret1), label = "AvSGD")
    ax.plot(log10(roundNum), log10(regret2), label = "AvAccSGD")
    ax.plot(log10(roundNum), log10(regret3), label = "AccSGD")
    #ax.plot(log10(roundNum), log10(baseline1), label = "T^{-1}")
    #ax.plot(log10(roundNum), log10(baseline2), label = "T^{-2}")
    #ax.set_title('new loss, for each T, init=0, epsilon = T^{-1/3}')
    ax.legend(loc=0)
    ax.set_xlabel('round number T (log)')
    ax.set_ylabel('Average Regret (log)')
    
    show()


    
if __name__ == '__main__':
    #readRegret("try.txt", 3)
    plotRegret()
    
