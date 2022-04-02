# Author: Katherina Cortes
# Date: April 2, 2022
# Purpose:

class Edges:
    def __init__(self, label, prevNodes, nextNodes):
        self.label = label
        self.prevNodes = prevNodes
        self.nextNodes = nextNodes

    def getLabel(self):
        return self.label

    def getPrevNodes(self):
        return self.prevNodes

    def getNewNodes(self):
        return self.nextNodes
