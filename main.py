# Author: Katherina Cortes
# Date: February 25, 2022
# Purpose: String reconstruction from next generation sequencing reads and query sequence searching

import argparse, time
from src import graphCreation, graphTraversal, dataExploration, querySearch
import sys
from src import outputFile

sys.setrecursionlimit(3000)



parser = argparse.ArgumentParser(description='Reconstruct sequence from reads and query for substring')
parser.add_argument('readsFile', metavar='reads', type=str, default='READS.fasta', help='input file of reads')
parser.add_argument('queryFile', metavar='query', type=str, default='QUERY.fasta', help='input file containing'
                                                                                        'the query string')
parser.add_argument('--kmerSize', metavar='kmer', type=int, default=10, help='length of node string')
parser.add_argument('--allowedError', metavar='error', type=int, default=0, help='number of mismatches allowed')
parser.add_argument('--outFile', metavar='outputFile', type=str, default='.\\Outputs\\ALLELES.aln', help='name of file to write '
                                                                                              'alignment output to')
parser.add_argument('--outFasta', metavar='outFasta', type=str, default='.\\Outputs\\ALLELES.fasta', help='name of file to write '
                                                                                               'longest contig')
parser.add_argument('--topContigs', metavar='topContigs', type=int, default=1, help='number of contigs to return')

args = parser.parse_args()

def main():
    start = time.time()
    # get reads from file and determine spread
    chroms = dataExploration.getReadsChromInfo(args.readsFile)
    query = dataExploration.getQuery(args.queryFile)
    # get reads, make graph, get contigs for all chromosomes
    output = []
    topContigs = {}
    count = 0
    #chroms = {'A':{ 'thecatisfishinsuperfat':'A123:1', 'thecatisgiganticallysuperfat':'A123:1','thecapissuperfat':'A123:1',
    #                'thecatisfish':'A123:2', 'thecatisstupid':'A123:3', 'thefishisblue':'A123:4', 'tisfishies':'A123:5',
    #                'tisfishing':'A123:1'}}
    #query = {'initial':'cat'}

    for c in chroms:
        reads, nodes = graphCreation.makeNodes(chroms[c], args.kmerSize)

        print('Number of reads on ', c, len(chroms[c]))
        #dataExploration.plotHist(chroms[c], c + ' Read Lengths', 'Reads')

        g, startNs = graphCreation.makeClassesDeBruijnGraph(reads, nodes, args.kmerSize - 1)
        contigs = graphTraversal.graphTraverseIter(g, startNs)
        print(contigs.keys())

        print('Number of contigs on ', c, len(contigs))
        dataExploration.plotHist(list(contigs.keys()), c + ' Contig Lengths', 'Contigs')

        num = 0
        for q in query:
            # matchID  contigID  readStart readEnd  matchStart matchEnd
            matches = querySearch.querySearch(query[q], contigs, args.allowedError, args.kmerSize, args.topContigs)
            revMatches = querySearch.querySearch(query[q][::-1], contigs, args.allowedError, args.kmerSize, args.topContigs)

            # sort matches by length of key
            matches = sorted(list(matches.items()), key=lambda key:len(key[0]), reverse=True)
            revMatches = sorted(list(revMatches.items()), key=lambda key:len(key[0]), reverse=True)

            revTopMatches = revMatches[0:args.topContigs]
            topMatches = matches[0:args.topContigs]

            # get info for matches
            for m in topMatches:
                contigID = 'contig'+ str(num+1)
                topContigs[contigID] = m[0]
                matchInfo = m[1][0], contigID, str(m[1][1]), str(m[1][1]+len(query[q])), str(m[1][2]), str(m[1][2]+len(query[q]))
                output.append(matchInfo)
                num+=1

            # get reverse matches info
            for m in revTopMatches:
                contigID = 'contig'+ str(num+1)
                topContigs[contigID] = m[0]
                matchInfo = m[1][0], contigID, str(m[1][1]), str(m[1][1]-len(query[q])), str(m[1][2]), str(m[1][2]-len(query[q]))
                output.append(matchInfo)
                num+=1


    # write to output Files
    outputFile.outputQueryInfo(output, args.outFile)
    outputFile.outputContigs(topContigs, args.outFasta)
    return


main()

