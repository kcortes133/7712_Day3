# Author: Katherina Cortes
# Date: April 2, 2022
# Purpose:


class Nodes:
    def __init__(self, label, edges):
        self.label = label
        self.edges = edges

    def getEdges(self):
        return self.edges

    def getLabel(self):
        return self.edges