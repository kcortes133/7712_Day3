# Author: Katherina Cortes
# Date: March 3, 2022
# Purpose:

def depthFirstSearch(graph, currNode, contigs, notExplored=[], currContig='', startNs=''):
    # start nodes not explored
    # no more edges
    if len(graph[currNode]) == 0:
        if startNs:
            newStart = startNs.pop()
            depthFirstSearch(graph, newStart, contigs, notExplored, newStart, startNs)

        contigs.append(currContig)
        return contigs

    for neighbor in graph[currNode]:
        newContig = currContig + neighbor
        if neighbor in notExplored:
            notExplored.remove(neighbor)
        depthFirstSearch(graph, neighbor, contigs, notExplored, newContig, startNs)
    return contigs


def getStartNodes(graph):
    startNs = []
    for node in graph:
        exists = False
        for node2 in graph:
            if node in graph[node2]:
                exists = True
        if not exists:
            startNs.append(node)
    return startNs