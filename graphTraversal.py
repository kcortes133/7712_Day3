# Author: Katherina Cortes
# Date: March 3, 2022
# Purpose: traverse through graph to get contigs


# depth first search that searches all paths
# @param graph: dictionary of graph of reads
# @param currNode: current node in traversal
# @param contigs: list of completed contigs
# @param explored: explored edges list
# @param currContig: current string contig being build
# @param startNs: list of nodes to start traversal at, dont have input edges
# @returns contigs: list of contigs made from graph
from collections import deque


def depthFirstSearch(graph, currNode, contigs, explored, currContig):
    # start nodes not explored
    # no more edges
    if len(graph[currNode]) == 0:
        contigs.append(currContig)
        return contigs

    # get next nodes
    if len(graph[currNode]) == 1:
        print('exit here')
        # TODO
        # return current node and contig
    for neighbor in graph[currNode]:

        edge = graph[currNode][neighbor]
        # append next part of contig
        newContig = currContig + edge[len(currNode):]

        # make sure edge hasnt been explored
        # ensures no infinite loops
        if edge not in explored:
            explored.append(edge)
            depthFirstSearch(graph, neighbor, contigs, explored, newContig)
    return contigs


# @param graph:
# @param startN:
# @param explored:
# @param contigs:
# @returns contigs:
def dFSIter(graph, startN):
    explored = {}
    stack = {startN: startN.label}
    contigs = []

    while stack:
        print('-----------')
        currN, currContig = stack.popitem()

        # get neighbors through Node class
        for neighbor in graph[currN]:
            edge = graph[currN][neighbor].label
            if edge not in explored:
                stack[neighbor] = currContig + edge[-1]
                explored[edge] = True
            # if current node is a leaf
        if len(graph[currN]) == 0:
            contigs.append(currContig)

    return contigs



    return


# @param graph:
# @param startN:
# @param explored:
# @param contigs:
# @returns contigs:
def dFSIterClasses(graph, startN):
    explored = {}
    stack = {startN: (startN.label, [])}
    contigs = {}

    while stack:
        currN, contig = stack.popitem()
        currContig = contig[0]

        # get neighbors through Node class
        for neighbor in graph[currN]:
            info = contig[1].copy()
            edge = graph[currN][neighbor].label
            edgeInfo = graph[currN][neighbor].readIDs
            if edge not in explored:
                newContig = currContig + edge[-1]
                info.append(edgeInfo)
                stack[neighbor] = (newContig, info)
                explored[edge] = True
            else: newContig = currContig
            # if current node is a leaf
            if len(graph[neighbor]) == 0:
                contigs[newContig] = info


    return contigs



    return


# get nodes with no input edges to start traversal at
# @param graph: dictionary of de bruijn graph made from reads
# @returns startNs: list of nodes with no input edges
def getStartNodes(graph):
    startNs = []
    for node in graph:
        exists = any(node in d.values() for d in graph.values())
        if not exists:
            startNs.append(node)
    return startNs


def getLeaves(graph):
    ls = []
    for node in graph:
        if not graph[node]:
            ls.append(node)
    return ls




# gets start nodes and traverses graph
# @param graph: dictionary of reads
# @returns contigs: list of contigs generated from graph traversal
def graphTraverse(graph,startNs):
    allContigs = []
    for start in startNs:
        contigs = depthFirstSearch(graph, start, [], [], start)
        allContigs.extend(contigs)

    return allContigs


def graphTraverseIter(graph, startNs):
    allContigs = {}
    c = 0

    for start in startNs:

        contigs = dFSIterClasses(graph, start)
        allContigs.update(contigs)

    return allContigs
