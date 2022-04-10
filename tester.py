import graphCreation

reads = ['ABD', 'AC', 'EG']
g, startNodes = graphCreation.makeDeBruijnGraph(reads, 1)

read = ['thecatisfat', 'the ']
reads = graphCreation.makeKmers(read, 5)
print(reads)
graph, s = graphCreation.makeDeBruijnGraph(reads, 4)
print(graph)
