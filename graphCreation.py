# Author: Katherina Cortes
# Date: March 3, 2022
# Purpose: Make de bruijn graph with reads


import math


# @param kmers: list of reads
# @returns graph: dictionary
def makeDeBruijnGraph(kmers,fixLen=10):
    graph = {}
    startNs = []
    count = 0
    for m in kmers:
        if count%1000 == 0  and count>1:
            print(count, len(startNs))
        count+=1
        edgeTemp = m

        node1 = m[:fixLen]
        node2 = m[-(fixLen):]

        if node1 not in graph:
            startNs.append(node1)
            graph[node1] = {node2:edgeTemp}
        else:
            graph[node1][node2] = edgeTemp

        if node2 in startNs:
            startNs.remove(node2)
        if node2 not in graph:
            graph[node2] = {}

    return graph, startNs


def readsToKmers(reads, kSize):
    newReads = []
    for r in reads:
        parts = [r[i:i+kSize] for i in range(0,len(r),kSize)]
        newReads.extend(parts)
    return newReads

def splitStr(s, num):
    r = len(s)%num
    num = int(len(s)/num)

