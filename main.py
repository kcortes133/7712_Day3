# Author: Katherina Cortes
# Date: Feburary 25, 2022
# Purpose:

import argparse, random, time
import graphCreation, graphTraversal, dataExploration


parser = argparse.ArgumentParser(description='')
parser.add_argument('kmer size')


def main():
    readsFile = 'READS.fasta'
    dataExploration.getReads(readsFile)

    g1 = {'A':{'B': 'AB', 'C':'AC'}, 'B': {'D': 'BD'}, 'E':{'G': 'EG'}, 'D':{}, 'C':{}, 'G':{}}
    g = {'A':{'B': 'AB', 'C':'AC'}, 'B': {'D': 'BD', 'G': 'BG'}, 'D':{'C': 'DC'}, 'C':{}, 'G': {}}
    g1 = {'A':{'B': 'AB', 'C':'AC'}, 'B': {'D': 'BD', 'G': 'BG'}, 'D':{'C': 'DC'}, 'C':{}, 'G': {}, 'F':{'B': 'FB'}}

    startNs = graphTraversal.getStartNodes(g)
    print(startNs)

    e = list(g.keys())
    e.remove('A')
    startNs.remove('A')
    contigs = graphTraversal.depthFirstSearch(g, 'A', [], e, 'A', startNs)
    print(contigs)

    contigs1 = graphTraversal.depthFirstSearch(g1, 'A', [], e, 'A', startNs)
    print(contigs1)


    return


main()

