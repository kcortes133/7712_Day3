# Author: Katherina Cortes
# Date: Feburary 25, 2022
# Purpose: String reconstruction from next generation sequencing reads and query sequence searching

import argparse, random, time
import numpy as np

import matplotlib.pyplot as plt

import graphCreation, graphTraversal, dataExploration, Edges, Nodes
import sys

import querySearch

sys.setrecursionlimit(3000)



parser = argparse.ArgumentParser(description='Reconstruct sequence from reads and query for substring')
parser.add_argument('readsFile', metavar='reads', type=str, default='READS.fasta', help='input file of reads')
parser.add_argument('queryFile', metavar='query', type=str, default='QUERY.fasta', help='input file containing'
                                                                                        'the query string')
parser.add_argument('--kmerSize', metavar='kmer', type=int, default=10, help='length of node string')
parser.add_argument('--allowedError', metavar='error', type=int, default=0, help='number of mismatches allowed')

args = parser.parse_args()

def main():
    start = time.time()
    # get reads from file and determine spread
    chroms = dataExploration.getReadsChromInfo(args.readsFile)
    query = dataExploration.getQuery(args.queryFile)
    # get reads, make graph, get contigs for all chromosomes
    #chroms = {'A':{ 'thecatissuperfat':'A123:1', 'thecatisrunning':'A123:2', 'thecatisstupid':'A123:3', 'thefishisblue':'A123:4', 'fishies':'A123:5', 'thecatisfishing':'A123:1'}}
    #chroms = {'A':[ 'thecatissuperfat', 'thecatisred']}
    #chroms = {'A':{'thecatissuperfat':'A123:123', 'thecatisred': 'A:1231:435'}}
    for c in chroms:

        #reads = graphCreation.makeKmers(chroms[c], args.kmerSize)
        #reads = graphCreation.makeInfoKmers(chroms[c], args.kmerSize)
        subset = {k: chroms[c][k] for k in sorted(chroms[c].keys())[:4]}

        #reads = graphCreation.makeInfoKmers(chroms[c], args.kmerSize)
        #reads = graphCreation.makeInfoKmers(subset, args.kmerSize)
        #reads, nodes = graphCreation.makeNodes(chroms[c], args.kmerSize)
        reads, nodes = graphCreation.makeNodes(subset, args.kmerSize)
        #print('Number of reads on ', c, len(chroms[c]))
        #dataExploration.plotHist(chroms[c], c+ ' Read Lengths')

        #g, startNs = graphCreation.makeDeBruijnGraph(reads, args.kmerSize-1)
        g, startNs = graphCreation.makeClassesDeBruijnGraph(reads, nodes, args.kmerSize-1)

        #contigs = graphTraversal.graphTraverse(g,startNs)
        contigs = graphTraversal.graphTraverseIter(g, startNs)
        #dataExploration.plotHist(contigs, c+ ' Contig Lengths')
        print(len(contigs))

        query = 'CACTT'
        #query = 'cat'
        matches = querySearch.querySearch(query, contigs, 0, args.kmerSize)
        print(len(matches))
        print(time.time() - start)
        break
        # TODO - get query
        # TODO - make output file
        # TODO - comments/README
        # TODO - writeup

    print(time.time() - start)
    return


main()

