# Author: Katherina Cortes
# Date: March 10, 2022
# Purpose: Output details about where the query was found

# @param queryInfo: info to write to file as matrix
# @param file: file name to write to
def outputQueryInfo(queryInfo,file):
    with open(file, 'w') as outF:
        outF.write('sseqid\tqseqid\tsstart\tsend\tqstart\tqend\n')
        for q in queryInfo:
            outF.write(q[0]+ '\t' + q[1]+ '\t' + q[2]+ '\t' + q[3]+ '\t' + q[4]+ '\t' + q[5] + '\n')

    return


# @param contigs: contigs containing queries to write to file
# @param file: file name to write to
def outputContigs(contigs, file):
    with open(file, 'w') as f:
        for c in contigs:
            f.write('>' + c + '\n' + contigs[c] + '\n')

    return