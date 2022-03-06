# Author: Katherina Cortes
# Date: Feburary 25, 2022
# Purpose: String reconstruction from next generation sequencing reads and query sequence searching

import argparse, random, time
import numpy as np

import matplotlib.pyplot as plt

import graphCreation, graphTraversal, dataExploration


parser = argparse.ArgumentParser(description='Reconstruct sequence from reads and query for substring')
parser.add_argument('readsFile', metavar='reads', type=str, default='READS.fasta', help='input file of reads')
parser.add_argument('queryFile', metavar='query', type=str, default='QUERY.fasta', help='input file containing'
                                                                                        'the query string')
parser.add_argument('--kmerSize', metavar='kmer', type=int, default=10, help='length of node string')

args = parser.parse_args()
def main():
    # get reads from file and determine spread
    chroms = dataExploration.getReadsChrom(args.readsFile)

    # get reads, make graph, get contigs for all chromosomes
    for c in chroms:
        print('Number of reads on ', c, len(chroms[c]))
        dataExploration.plotHist(chroms[c], c+ ' Read Lengths')
        g, startNs = graphCreation.makeDeBruijnGraph(chroms[c])

        print('Number of start nodes: ', len(startNs))
        contigs = graphTraversal.graphTraverse(g,startNs)
        dataExploration.plotHist(contigs, c+ ' Contig Lengths')
        print('Number of contigs', c, len(contigs))


    return


main()

