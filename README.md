# Reassembling the Genome and Sequence Query 

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
while traversing the graph and returned as a library to search for the query through.Library is searched for query, 
option for error allowance in string matching. 

Output is two files, a fasta file and a tab delimited file. The fasta file contains the longest contig query was 
found in and contig name. The tab delimited file contains information about where in the contig the query was found
and information about the original read the query can be found in. 

## Install
- matplotlib.pyplot
- numpy
- math 

## Usage
#### Python Usage

```python

from src import graphCreation, graphTraversal, dataExploration, querySearch, outputFile


def main():
   # get reads from file and determine spread
   readsFile = 'READS.fasta'
   queryFile = 'QUERY.fasta'
   kmerSize = 25
   allowedError =0
   topContigs = 1
   
   chroms = dataExploration.getReadsChromInfo(readsFile)
   query = dataExploration.getQuery(queryFile)
   # get reads, make graph, get contigs for all chromosomes
   output = []
   topContigs = {}

   for c in chroms:
      reads, nodes = graphCreation.makeNodes(chroms[c], kmerSize)

      print('Number of reads on ', c, len(chroms[c]))
      dataExploration.plotHist(chroms[c], c + ' Read Lengths', 'Reads')

      g, startNs = graphCreation.makeClassesDeBruijnGraph(reads, nodes, kmerSize - 1)
      contigs = graphTraversal.graphTraverseIter(g, startNs)

      print('Number of contigs on ', c, len(contigs))
      dataExploration.plotHist(list(contigs.keys()), c + ' Contig Lengths', 'Contigs')

      num = 0
      for q in query:
         # matchID  contigID  readStart readEnd  matchStart matchEnd
         matches = querySearch.querySearch(query[q], contigs, allowedError, kmerSize, topContigs)
         revMatches = querySearch.querySearch(query[q][::-1], contigs, allowedError, kmerSize, topContigs)

         # sort matches by length of key
         matches = sorted(list(matches.items()), key=lambda key:len(key[0]), reverse=True)
         revMatches = sorted(list(revMatches.items()), key=lambda key:len(key[0]), reverse=True)

         revTopMatches = revMatches[0:topContigs]
         topMatches = matches[0:topContigs]

         # get info for matches
         for m in topMatches:
            contigID = 'contig'+ str(num+1)
            topContigs[contigID] = m[0]
            matchInfo = m[1][0], contigID, str(m[1][1]), str(m[1][1]+len(query[q])), str(m[1][2]), str(m[1][2]+len(query[q]))
            output.append(matchInfo)
            num+=1

         # get reverse matches info
         for m in revTopMatches:
            contigID = 'contig'+ str(num+1)
            topContigs[contigID] = m[0]
            matchInfo = m[1][0], contigID, str(m[1][1]), str(m[1][1]-len(query[q])), str(m[1][2]), str(m[1][2]-len(query[q]))
            output.append(matchInfo)
            num+=1


   # write to output Files
   outputFile.outputQueryInfo(output, outFile)
   outputFile.outputContigs(topContigs, outFasta)
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
#### General Info about reads, start nodes and contigs
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

####Files

ALLELES.fasta
- fasta file
- each two lines gives information about longest contig containing query and contig

ALLELES.aln
- tab delimited file
- describes alignment of query to longest contig
- sseqid   qseqid  sstart  send  qstart  qend
- sseqid : name of sequence read
- qseqid : name of contig 
- sstart : start coord of query in sequence read
- send : end coord of query in sequence read
- qstart : start coord of query in contig
- qend: end coord of query in contig




