# Author: Katherina Cortes
# Date: March 3, 2022
# Purpose: Make de bruijn graph with reads


# make de bruijn graph nodes are of length fixLen and edges are the reads
# @param kmers: list of reads
# @returns graph: dictionary
def makeDeBruijnGraph(kmers,fixLen=10):
    graph = {}
    startNs = []
    for m in kmers:
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
