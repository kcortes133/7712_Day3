# Reassembling the Genome

## Goal
Assemble contigs from next-generation sequencing reads and return the largest contig that contains
given query sequence.
 
## Description
Input is two fasta files, the reads file and the query file. The reads file contains reads 
of various length from different chromosomes. The query file contains the query to search in the
assembled contigs. 

A de bruijn graph is constructed from the reads file where nodes are of kmer defined length and
the edges are the reads. Once constructed, a depth first search algorithm is run to get all possible
contigs starting from nodes with no input edges and iterating over all edges. Contigs are assembled 
while traversing the graph and returned as a library to search for the query through.

## Install
- matplotlib.pyplot
- numpy
- math 

## Usage
#### Python Usage
```python

import dataExploration, graphTraversal, graphCreation, querySearch

def main():
   readsFile = 'READS.fasta'
   queryFile = 'Query.fasta'
   # get reads from file and determine spread
   chroms = dataExploration.getReadsChrom(readsFile)
   query = dataExploration.getQuery(queryFile)

   allContigs = []
   # get reads, make graph, get contigs for all chromosomes
   for c in chroms:
      print('Number of reads on ', c, len(chroms[c]))
      
      # Histogram of read lengths
      dataExploration.plotHist(chroms[c], c+ ' Read Lengths')
      
      g, startNs = graphCreation.makeDeBruijnGraph(chroms[c])
      print('Number of start nodes: ', len(startNs))
      
      contigs = graphTraversal.graphTraverse(g,startNs)
      
      # Histogram of contig lengths created from graph traversal
      dataExploration.plotHist(contigs, c+ ' Contig Lengths')
      print('Number of contigs', c, len(contigs))

   querySearch.searchQuery(query, contigs)

   return


main()
```
#### Command Line Usage
```commandline
default, specify reads and query input
$ python .\main.py READS.fasta QUERY.fasta

specify kmer length of nodes overlap
$ python .\main.py READS.fasta QUERY.fasta --kmerSize=10


```

## Input
1. READS.fasta
   - fasta file
   - each two lines gives where the read is from and the read

2. QUERY.fasta
   - fasta file
   - each two lines give information about query and query

## Output
General Info about reads, start nodes and contigs
- Number of reads on  2S43D 62278
- Number of start nodes:  48052
- Number of contigs 2S43D 58199

![chrom 1 read lengths](https://user-images.githubusercontent.com/22487858/156932731-e288538a-9d61-4ebc-b478-5e124324bc0e.png)

![chrom 1 contig lengs](https://user-images.githubusercontent.com/22487858/156932740-017ca5ba-a813-4899-9f48-e0239ca51c43.png)

- Number of reads on  2G5Z3 62242
- Number of start nodes:  47905
- Number of contigs 2G5Z3 58180

![chrom2 read lengths](https://user-images.githubusercontent.com/22487858/156932749-3f5a0a8b-9699-46b3-a75f-e9221a390edd.png)

![chrom 2 contig lengths](https://user-images.githubusercontent.com/22487858/156932755-295e6669-66e2-45ee-bea7-8b8da10a2b82.png)


