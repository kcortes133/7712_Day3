# Author: Katherina Cortes
# Date:
# Purpose:

import numpy as np

def makeDeBruijnGraph(kmers):
    graph = {}
    for m in kmers:
        edgeTemp = m
        node1 = m[:len(m)/2]
        node2 = m[len(m)/2:]

        if node1 in graph:
            graph[node1] = {node2:edgeTemp}
        else:
            graph[node1][node2] = edgeTemp

    return graph


def readsToKmers(reads, kSize):
    newReads = []
    for r in reads:
        if len(r) < kSize*1.5:
            newReads.append(r)
        else:
            num = len(r)/kSize
            newReads.append(r[:len(r)/2])
            newReads.append(r[:len(r)/2])
    return newReads