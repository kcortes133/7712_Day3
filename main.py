# Author: Katherina Cortes
# Date: Feburary 25, 2022
# Purpose: String reconstruction from next generation sequencing reads and query sequence searching

import argparse, random, time
import numpy as np

import matplotlib.pyplot as plt

import graphCreation, graphTraversal, dataExploration
import sys

sys.setrecursionlimit(4000)



parser = argparse.ArgumentParser(description='Reconstruct sequence from reads and query for substring')
parser.add_argument('readsFile', metavar='reads', type=str, default='READS.fasta', help='input file of reads')
parser.add_argument('queryFile', metavar='query', type=str, default='QUERY.fasta', help='input file containing'
                                                                                        'the query string')
parser.add_argument('--kmerSize', metavar='kmer', type=int, default=10, help='length of node string')

args = parser.parse_args()
print(args)

def main():
    start = time.time()
    # get reads from file and determine spread
    chroms = dataExploration.getReadsChrom(args.readsFile)
    print(chroms.keys())
    # get reads, make graph, get contigs for all chromosomes
    #chroms = {'A':[ 'thecatissuperfat', 'thecatisrunning', 'thecatisstupid', 'thefishisblue', 'fishies', 'kitties']}
    for c in chroms:
        reads = graphCreation.makeKmers(chroms[c], args.kmerSize)
        #print('Number of reads on ', c, len(chroms[c]))
        #dataExploration.plotHist(chroms[c], c+ ' Read Lengths')
        print(len(reads))
        print(len(chroms[c]))
        g, startNs = graphCreation.makeDeBruijnGraph(reads, args.kmerSize-1)
        print(time.time()-start)
        print(len(g))

        print('Number of start nodes: ', len(startNs))
        print('wtf is happening')
        contigs = graphTraversal.graphTraverse(g,startNs)
        print(len(contigs))
        #dataExploration.plotHist(contigs, c+ ' Contig Lengths')

    print(time.time() - start)
    return


main()

