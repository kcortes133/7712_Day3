# Author: Katherina Cortes
# Date: Feburary 28, 2022
# Purpose: unit tests for all methods
import sys
import os
cur_path=os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path+"/..")

import unittest
from src import graphCreation, graphTraversal, dataExploration, querySearch

class GraphCreation(unittest.TestCase):
    def testGCreation(self):
        reads = ['theca', 'ecati', 'atisf', 'isfat']
        graph, s = graphCreation.makeDeBruijnGraph(reads, 3)
        self.assertEqual(graph, {'the': {'eca': 'theca'}, 'eca': {'ati': 'ecati'}, 'ati': {'isf': 'atisf'}, 'isf': {'fat': 'isfat'}, 'fat':{}})

    def testGCreationKmers(self):
        read = ['thecatisfat']
        reads = graphCreation.makeKmers(read, 5)
        graph, s = graphCreation.makeDeBruijnGraph(reads, 4)
        self.assertEqual(graph, {'thec': {'heca': 'theca'}, 'heca': {'ecat': 'hecat'}, 'ecat': {'cati': 'ecati'}, 'cati': {'atis': 'catis'}, 'atis': {'tisf': 'atisf'}, 'tisf': {'isfa':
 'tisfa'}, 'isfa': {'sfat': 'isfat'}, 'sfat': {}})

class TestTraversal(unittest.TestCase):
    def testStartNodes(self):
        reads = ['AB', 'AC', 'BD', 'EG']
        g, startNodes = graphCreation.makeDeBruijnGraph(reads, 1)
        self.assertEqual(startNodes, {'A':0, 'E':0})

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

class TestQuerySearch(unittest.TestCase):
    def testSmallQuery(self):
        chroms = {'A':{ 'thecatissuperfat':'A123:1', 'thecatisgiganticallysuperfat':'A123:1','thecapissuperfat':'A123:1',
                        'thecatisrunning':'A123:2', 'thecatisstupid':'A123:3', 'thefishisblue':'A123:4', 'fishies':'A123:5',
                        'thecatisfishing':'A123:1', 'gnihsifsitaceht':'A123:1'}}
        query = {'initial':'cat'}
        allowedError = 0
        kmerSize = 6
        topContigs = 1
        for c in chroms:
            reads, nodes = graphCreation.makeNodes(chroms[c], kmerSize)

            g, startNs = graphCreation.makeClassesDeBruijnGraph(reads, nodes, kmerSize - 1)
            contigs = graphTraversal.graphTraverseIter(g, startNs)
            for q in query:
                # matchID  contigID  readStart readEnd  matchStart matchEnd
                matches = querySearch.querySearch(query[q], contigs, allowedError, kmerSize, topContigs)
                revMatches = querySearch.querySearch(query[q][::-1], contigs, allowedError, kmerSize, topContigs)
                print(matches)
                print(revMatches)




if __name__ == '__main__':
    unittest.main()

