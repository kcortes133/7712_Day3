# Author: Katherina Cortes
# Date: Feburary 28, 2022
# Purpose: unit tests for all methods

import unittest
import winreg

import graphCreation, graphTraversal, dataExploration

class GraphCreation(unittest.TestCase):
    def testGCreation(self):
        reads = ['theca', 'ecati', 'atisf', 'isfat']
        graph, s = graphCreation.makeDeBruijnGraph(reads, 3)
        self.assertEqual(graph, {'the': {'eca': 'theca'}, 'eca': {'ati': 'ecati'}, 'ati': {'isf': 'atisf'}, 'isf': {'fat': 'isfat'}, 'fat':{}})


class TestTraversal(unittest.TestCase):
    def testStartNodes(self):
        reads = ['AB', 'AC', 'BD', 'EG']
        g, startNodes = graphCreation.makeDeBruijnGraph(reads, 1)
        self.assertEqual(startNodes, ['A', 'E'])

    def testDFS(self):
        g = {'A': {'B': 'AB', 'C': 'AC'}, 'B': {'D': 'BD', 'G': 'BG'}, 'D': {'C': 'DC'}, 'C': {}, 'G': {}}
        startNs = ['A']
        contigs = graphTraversal.graphTraverse(g, startNs)
        self.assertEqual(contigs, ['ABDC', 'ABG', 'AC'])

    def testDFSDisconnected(self):
        g1 = {'A': {'B': 'AB', 'C': 'AC'}, 'B': {'D': 'BD'}, 'E': {'G': 'EG'}, 'D': {}, 'C': {}, 'G': {}}
        startNs = ['A', 'E']
        contigs = graphTraversal.graphTraverse(g1, startNs)
        self.assertEqual(contigs, ['ABD', 'AC', 'EG'])

    def testDFSMultiStarts(self):
        g = {'A': {'B': 'AB', 'C': 'AC'}, 'B': {'D': 'BD', 'G': 'BG'}, 'D': {'C': 'DC'}, 'C': {}, 'G': {}, 'F':{'B':'FB'}}
        startNs = ['A', 'F']
        contigs = graphTraversal.graphTraverse(g, startNs)
        self.assertEqual(contigs, ['ABDC', 'ABG', 'AC', 'FBDC', 'FBG'])

    def testNoInfinLoop(self):
        g = {'A': {'B': 'AB'}, 'B': {'D': 'BD', 'G': 'BG'}, 'D': {'C': 'DC'}, 'C': {'B':'CB'}, 'G': {}}
        startNs = ['A']
        contigs = graphTraversal.graphTraverse(g, startNs)
        self.assertEqual(contigs, ['ABDCBG'])


if __name__ == '__main__':
    unittest.main()

