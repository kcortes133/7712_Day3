# Author: Katherina Cortes
# Date: Feburary 25, 2022
# Purpose: read in files

import matplotlib.pyplot as plt
import numpy as np

# get read lengths from input file
# @params readF: input file name
# @displays: histogram of read lengths
def getReadLens(readF):
    readLengths = []

    with open(readF, 'r') as f:
        lines = f.readlines()

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


# get query from input file
# @params queryF: file name containing query string
# @returns query: query string
def getQuery(queryF):

    return


# get reads from file
# @param readF: file name containing reads
# @returns reads: list of reads from file
def getReads(readF):
    reads = []

    with open(readF, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line.startswith('>'):
            reads.append(line)
    return reads


# get reads from each chromosome
# @params readF: file name containing reads
# @returns reads: dictionary of reads from each chromosome
def getReadsChrom(readF):
    reads = {}

    with open(readF, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith('>'):

            info = line.strip('>').split(':')
            chrom = info[0]
        else:
            if chrom in reads:
                reads[chrom].append(line)
            else:
                reads[chrom] = [line]
    return reads


# plot histogram of lengths
# @param strings: list of strings
# @param title: title for histogram
# @displays: histogram of string lengths
def plotHist(strings, title):
    slen = []
    for s in strings:
        slen.append(len(s))
    plt.hist(slen, rwidth=0.9)
    plt.title(title)
    plt.show()

