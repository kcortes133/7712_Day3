# Author: Katherina Cortes
# Date: March 3, 2022
# Purpose: Make de bruijn graph with reads

from src.Edges import Edge
from src.Nodes import Node

# make de bruijn graph edges are of length fixLen and edges are the reads
# nodes are length fixLen-1
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


# make graph using edges and nodes classes
# classes contain information about origin of reads
# param reads: dictionary of kmers to be used as edges with read info
# param nodes: dictionary of nodes
# param fixLen: kmer length
# returns graph: dictionary of created graph
# returns startNs: dictionary of start nodes, nodes with no input edges
def makeClassesDeBruijnGraph(reads, nodes, fixLen=10):
    graph = {}
    startNs = {}
    c = 0
    for m in reads:
        node1 = m[:fixLen]
        node2 = m[-(fixLen):]
        nodeS = nodes[node1]
        nodeE = nodes[node2]

        # create edges
        for readID in reads[m]:
            edge = Edge(m, readID, reads[m][readID])
        nodeS.addEdge(edge, nodeE)

        if nodeS not in graph:
            startNs[nodeS] = 0
            graph[nodeS] = {nodeE: edge}
        else:
            graph[nodeS][nodeE] = edge

        if nodeE not in graph:
            graph[nodeE] = {}
        elif nodeE in startNs:
            del startNs[nodeE]
        c+=1
    return graph, startNs


# makes edges of length kLen from reads
# param reads: list of reads from file
# param kLen: int of size of kmer
# returns kmers: dictionary of kmers and number of times they appear
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


# makes edges of length kLen from reads
# edges have info about origin of read
# param reads: list of reads from file
# param kLen: int of size of kmer
# returns: dictionary of kmers and where kmer begins in read
def makeInfoKmers(reads, kLen):
    kmers = {}

    for read in reads:
        for r in range(len(read)):
            if r+kLen < len(read)+1:
                kmer = read[r:r+kLen]
                if kmer not in kmers:
                    kmers[read[r:r+kLen]] = {reads[read]: r}
                else:
                    kmers[read[r:r+kLen]][reads[read]] = r
    return kmers


# makes edges and nodes
# edges are of length kLen from reads
# edges have info about origin of read
# param reads: list of reads from file
# param kLen: int of size of kmer
# returns kmers: dictionary of kmers, read info and where kmer begins in read
# returns nodes: dictionary of all nodes in graph
def makeNodes(reads, kLen):
    kmers = {}
    nodes = {}

    for read in reads:
        for r in range(len(read)):
            if r+kLen < len(read)+1:
                kmer = read[r:r+kLen]
                if kmer not in kmers:
                    kmers[read[r:r+kLen]] = {reads[read]: r+kLen}
                    label1 = read[r:r+kLen-1]
                    label2 = read[r+1:r+kLen]
                    if label1 not in nodes:
                        nodes[label1] = Node(label1, False)
                    else:
                        nodes[label1].isLeaf = False
                    if label2 not in nodes:
                        nodes[label2] = Node(label2, True)
                    else:
                        nodes[label2].isLeaf = False
                else:
                    kmers[read[r:r+kLen]][reads[read]] = r+kLen

    return kmers, nodes
