# Author: Katherina Cortes
# Date: Feburary 25, 2022
# Purpose: String reconstruction from next generation sequencing reads and query sequence searching

import argparse, random, time
import numpy as np

import matplotlib.pyplot as plt

import graphCreation, graphTraversal, dataExploration


parser = argparse.ArgumentParser(description='')
parser.add_argument('kmer size')


def main():
    # get reads from file and determine spread
    readsFile = 'READS.fasta'
    reads = dataExploration.getReads(readsFile)
    chroms = dataExploration.getReadsChrom(readsFile)

    # make graph
    g, startNs = graphCreation.makeDeBruijnGraph(reads)

    contigs = graphTraversal.graphTraverse(g,startNs)

    print(contigs)
    print(len(contigs))

    return


main()

