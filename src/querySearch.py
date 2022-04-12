# Author: Katherina Cortes
# Date: March 3, 2022
# Purpose: search contigs to return information about read origin and query matching


# @param
# @param
# @param
# @param
# @param
# @returns matches:
def querySearch(query, contigs, error, kLen, topContigs):
    matches = {}
    minHD = 70000

    for c in contigs:
        info = contigs[c]
        match = searchContig(query, c, info, error, kLen)
        if match[1] != -1:
            matches[c] = match
        else:
            minHD = min(match[2], minHD)

    return matches


# @param
# @param
# @param
# @param
# @param
# returns info: tuple
def searchContig(query, contig, info, error, kLen):
    cLen = len(query)
    c = 0
    minHD = 70000

    while c < len(contig)-cLen:
        subString = contig[c: c+cLen]
        hDist = hammingDist(query, subString, int(len(query)/2))
        minHD = min(hDist, minHD)
        if hDist <= error:
            if c > kLen:
                return (info[c-kLen][0][0],  info[c-kLen][0][1], c)
            else:
                return (info[0][0][0], c, c)
        c+=1

    return ('', -1, minHD)


# gives hamming distance
# hamming distance - number of mismatches in two strings of the same length
# @param string1: string to compare to
# @param string2: string to compare to
# @returns score: number of mismatches
def hammingDist(string1, string2, maxS=100):
    score = 0
    for s in range(len(string1)):
        if string1[s] != string2[s]:
            score+=1
        if score > maxS: break
    return score


