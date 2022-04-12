# Author: Katherina Cortes
# Date: April 2, 2022
# Purpose: edge class creation

class Edge:
    def __init__(self, label, readID, start):
        self.label = label
        self.prevNodes = {}
        self.nextNodes = {}
        self.readIDs = [(readID, start)]


    def getLabel(self):
        return self.label

    def getPrevNodes(self):
        return self.prevNodes

    def getNewNodes(self):
        return self.nextNodes

    def addPrev(self, node, edge):
        self.prevNodes[node] = edge

    def addNext(self, node, edge):
        self.nextNodes[node] = edge

    def addReadID(self, readID, start):
        self.readIDs.append(readID, start)
