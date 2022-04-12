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
import time


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


# depth first search iteratively, not using classes
# @param graph: dictionary of graph from reads
# @param startN: dictionary of start nodes, nodes without incoming edges
# @returns contigs: dictionary of contigs and read origin info
def dFSIter(graph, startN):
    explored = {}
    stack = {startN: startN.label}
    contigs = []

    while stack:
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


# depth first search iteratively and account for bubbles
# @param graph: dictionary of graph from reads
# @param startN: dictionary of start nodes, nodes without incoming edges
# @returns contigs: dictionary of contigs and read origin info
def dFSIterClassesAllPaths(graph, startN):
    stack = {startN: {'contig':startN.label, 'explored': {}, 'info':[]}}
    contigs = {}

    while stack:
        currN, traverseInfo = stack.popitem()
        currContig = traverseInfo['contig']

        # get neighbors through Node class
        for neighbor in graph[currN]:
            info = traverseInfo['info'].copy()
            currExplored = traverseInfo['explored'].copy()
            edge = graph[currN][neighbor].label
            edgeInfo = graph[currN][neighbor].readIDs
            if edge not in currExplored:
                newContig = currContig + edge[-1]
                info.append(edgeInfo)
                currExplored[edge] = True
                stack[neighbor] = {}
                stack[neighbor]['contig'] = newContig
                stack[neighbor]['info'] = info.copy()
                stack[neighbor]['explored'] = currExplored.copy()
            else: newContig = currContig
            # if current node is a leaf
            if len(graph[neighbor]) == 0:
                contigs[newContig] = info

    return contigs


# depth first search iteratively only traverse each edge once
# @param graph: dictionary of graph from reads
# @param startN: dictionary of start nodes, nodes without incoming edges
# @returns contigs: dictionary of contigs and read origin info
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


# get nodes without outgoing edges
# param graph: dictionary of graph
# returns ls: list of leaves
def getLeaves(graph):
    ls = []
    for node in graph:
        if not graph[node]:
            ls.append(node)
    return ls


# given start nodes, traverses graph and gives all contigs
# @param graph: dictionary of reads
# @param startNs: list of start nodes
# @returns allContigs: list of contigs generated from graph traversal
def graphTraverse(graph, startNs):
    allContigs = []
    for start in startNs:
        contigs = depthFirstSearch(graph, start, [], [], start)
        allContigs.extend(contigs)

    return allContigs


# given start nodes, traverses graph and gives all contigs
# @param graph: dictionary of reads
# @param startNs: list of start nodes
# @returns allContigs: dictionary of contigs generated from graph traversal with read info
def graphTraverseIter(graph, startNs):
    allContigs = {}

    print(len(startNs))
    c =0
    s = time.time()
    for start in startNs:
        contigs = dFSIterClasses(graph, start)
        allContigs.update(contigs)
        print(c)
        print(time.time()-s)
        c+=1

    return allContigs
