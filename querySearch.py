# Author: Katherina Cortes
# Date: March 3, 2022
# Purpose:


def querySearch(query, contigs, error, kLen):
    matches = {}

    for c in contigs:
        info = contigs[c]
        match = searchContig(query, c, info, error, kLen)
        if match[1] != -1:
            matches[c] = match
            print(match)

    return matches


def searchContig(query, contig, info, error, kLen):
    exists = False
    cLen = len(query)
    c = 0

    while c < len(contig)-cLen:
        subString = contig[c: c+cLen]

        hDist = hammingDist(query, subString)
        if hDist <= error:
            exists = True
            if c > kLen:
                return info[c-kLen][0]
            else:
                return (info[0][0][0], c)
        c+=1

    return ('', -1)


def hammingDist(string1, string2):
    score = 0
    for s in range(len(string1)):

        if string1[s] != string2[s]:
            score+=1
    return score


