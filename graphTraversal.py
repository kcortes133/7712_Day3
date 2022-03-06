# Author: Katherina Cortes
# Date: March 3, 2022
# Purpose: traverse through graph to get contigs

import math


# depth first search that searches all paths
# @param graph: dictionary of graph of reads
# @param currNode: current node in traversal
# @param contigs: list of completed contigs
# @param explored: explored edges list
# @param currContig: current string contig being build
# @param startNs: list of nodes to start traversal at, dont have input edges
# @returns contigs: list of contigs made from graph
def depthFirstSearch(graph, currNode, contigs, explored, currContig):
    # start nodes not explored
    # no more edges
    if len(graph[currNode]) == 0:
        #if startNs:
        #    newStart = startNs.pop()
        #    explored = []
        #    depthFirstSearch(graph, newStart, contigs, explored, newStart, startNs)
        contigs.append(currContig)
        return contigs

    # get next nodes
    for neighbor in graph[currNode]:
        edge = graph[currNode][neighbor]
        fixLen = int(math.ceil(len(edge)/2))
        # append next part of contig
        #//TODO make sure this is correct and getting all of edge after currNode
        newContig = currContig + edge[len(currNode):]

        # make sure edge hasnt been explored
        # ensures no infinite loops
        if edge not in explored:
            explored.append(edge)
            depthFirstSearch(graph, neighbor, contigs, explored, newContig)
    return contigs

# get nodes with no input edges to start traversal at
# @param graph: dictionary of de bruijn graph made from reads
# @returns startNs: list of nodes with no input edges
def getStartNodes(graph):
    startNs = []
    count = 0
    for node in graph:
        if count%1000 == 0:
            print(count)
        exists = False
        #for node2 in graph:
        #    if node in graph[node2]:
        #        exists = True
        exists = any(node in d.values() for d in graph.values())
        if not exists:
            startNs.append(node)
        count+=1
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
    #startNs = getStartNodes(graph)
    #start = startNs.pop(0)
    allContigs = []
    for start in startNs:
        print(start)
        contigs = depthFirstSearch(graph, start, [], [], start)
        allContigs.extend(contigs)

    return allContigs
