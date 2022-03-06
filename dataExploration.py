# Author: Katherina Cortes
# Date: Feburary 25, 2022
# Purpose: look at distribution of read lengths

import matplotlib.pyplot as plt
import numpy as np


def getReadLens(readF):
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

def getQuery():

    return

def getReads(readF):
    reads = []

    with open(readF, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line.startswith('>'):
            reads.append(line)
    return reads


def getReadsChrom(readF):
    reads = {}

    with open(readF, 'r') as f:
        lines = f.readlines()

    c = 0
    for line in lines:
        line = line.strip()
        if line.startswith('>'):
            info = line.split(':')
            chrom = info[0]
        else:
            if chrom in reads:
                reads[chrom].append(line)
            else:
                reads[chrom] = [line]
    return reads

