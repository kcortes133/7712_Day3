# Author: Katherina Cortes
# Date: Feburary 25, 2022
# Purpose:

import matplotlib.pyplot as plt
import numpy as np


def getReads(readF):
    readLengths = []

    with open(readF, 'r') as f:
        lines = f.readlines()

    c = 0
    for line in lines:
        line = line.strip()
        if not line.startswith('>'):
            readLengths.append(len(line))

    plt.hist(readLengths, rwidth=0.9)
    plt.title('Read Lengths')
    plt.show()

    u, c = np.unique(readLengths, return_counts=True)
    print(u)
    print(c)

    return

def getQueries():

    return