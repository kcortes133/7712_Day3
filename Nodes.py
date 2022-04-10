# Author: Katherina Cortes
# Date: April 2, 2022
# Purpose:


class Node:
    def __init__(self, label, isLeaf):
        self.label = label
        self.edges = {}
        self.contigs = []
        self.isLeaf = isLeaf

    def getEdges(self):
        return self.edges

    def getLabel(self):
        return self.edges

    def getContigs(self):
        return self.contigs

    def addContigs(self, contig):
        self.contigs.append(contig)

    def addEdge(self, edge, node):
        self.edges[edge] = node
