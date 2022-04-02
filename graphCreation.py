# Author: Katherina Cortes
# Date: March 3, 2022
# Purpose: Make de bruijn graph with reads


# make de bruijn graph nodes are of length fixLen and edges are the reads
# @param kmers: list of reads
# @returns graph: dictionary
def makeDeBruijnGraph(kmers, fixLen=10):
    graph = {}
    startNs = {}
    c = 0
    for m in kmers:
        edgeTemp = m
        node1 = m[:fixLen]
        node2 = m[-(fixLen):]

        if node1 not in graph:
            startNs[node1] = 0
            graph[node1] = {node2: edgeTemp}
        else:
            graph[node1][node2] = edgeTemp

        if node2 not in graph:
            graph[node2] = {}
        elif node2 in startNs:
            del startNs[node2]
        c+=1


    return graph, startNs


def makeKmers(reads, kLen):
    kmers = {}

    for read in reads:
        for r in range(len(read)):
            if r+kLen < len(read)+1:
                kmer = read[r:r+kLen]
                if kmer not in kmers:
                    kmers[read[r:r+kLen]] = 1
                else:
                    kmers[read[r:r+kLen]] +=1


    return kmers


