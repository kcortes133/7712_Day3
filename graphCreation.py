# Author: Katherina Cortes
# Date: March 3, 2022
# Purpose: Make de bruijn graph with reads

from Edges import Edge
from Nodes import Node

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


# make graph using edges and nodes classes
def makeClassesDeBruijnGraph(reads, nodes, fixLen=10):
    graph = {}
    startNs = {}
    c = 0
    for m in reads:
        edgeTemp = m
        node1 = m[:fixLen]
        node2 = m[-(fixLen):]
        nodeS = nodes[node1]
        nodeE = nodes[node2]

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


# TODO make nodes here will be easier
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


def makeNodes(reads, kLen):
    kmers = {}
    nodes = {}

    for read in reads:
        for r in range(len(read)):
            if r+kLen < len(read)+1:
                kmer = read[r:r+kLen]
                if kmer not in kmers:
                    kmers[read[r:r+kLen]] = {reads[read]: r+kLen-1}
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
                    kmers[read[r:r+kLen]][reads[read]] = r+kLen-1

    return kmers, nodes
