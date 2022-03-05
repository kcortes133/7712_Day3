# Author: Katherina Cortes
# Date: Feburary 28, 2022
# Purpose:

import unittest
import winreg

import graphCreation, graphTraversal, dataExploration


class TestTraversal(unittest.TestCase):
    def testStartNodes(self):
        g1 = {'A': {'B': 'AB', 'C': 'AC'}, 'B': {'D': 'BD'}, 'E': {'G': 'EG'}, 'D': {}, 'C': {}, 'G': {}}
        startNodes = graphTraversal.getStartNodes(g1)
        self.assertEqual(startNodes, ['A', 'E'])

    def testDFS(self):
        g = {'A': {'B': 'AB', 'C': 'AC'}, 'B': {'D': 'BD', 'G': 'BG'}, 'D': {'C': 'DC'}, 'C': {}, 'G': {}}
        startNs = graphTraversal.getStartNodes(g)
        e = list(g.keys())
        e.remove('A')
        startNs.remove('A')
        contigs = graphTraversal.depthFirstSearch(g, 'A', [], e, 'A', startNs)
        self.assertEqual(contigs, ['ABDC', 'ABG', 'AC'])

    def testDFSDisconnected(self):
        g1 = {'A': {'B': 'AB', 'C': 'AC'}, 'B': {'D': 'BD'}, 'E': {'G': 'EG'}, 'D': {}, 'C': {}, 'G': {}}
        startNs = graphTraversal.getStartNodes(g1)
        e = list(g1.keys())
        e.remove('A')
        startNs.remove('A')
        contigs = graphTraversal.depthFirstSearch(g1, 'A', [], e, 'A', startNs)
        self.assertEqual(contigs, ['EG', 'ABD', 'AC'])

    def testDFSMultiStarts(self):
        g = {'A': {'B': 'AB', 'C': 'AC'}, 'B': {'D': 'BD', 'G': 'BG'}, 'D': {'C': 'DC'}, 'C': {}, 'G': {}, 'F':{'B':'FB'}}
        startNs = graphTraversal.getStartNodes(g)
        e = list(g.keys())
        e.remove('A')
        startNs.remove('A')
        contigs = graphTraversal.depthFirstSearch(g, 'A', [], e, 'A', startNs)
        self.assertEqual(contigs, ['FBDC', 'FBG', 'ABDC', 'ABG', 'AC'])


if __name__ == '__main__':
    unittest.main()

