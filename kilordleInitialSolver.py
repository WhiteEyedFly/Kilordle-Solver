import copy
import numpy as np

from words import WORDS, WORDLES

"""
Main idea:

Define a cover with the wordles
DFS for a minimal cover
Backtrack for all such minimal covers
Choose an optimal one
"""

coversFound = 0

def findLetterPositions(answers, wordLength):
    letterPositions = {}
    numLetterPositions = 0
    
    for letter in "abcdefghijklmnopqrstuvwxyz":
        letterPositions.update({letter:[0,0,0,0,0]})

    for word in answers:
        for i in range(wordLength):
            if letterPositions[word[i]][i] == 0:
                numLetterPositions += 1
                
            letterPositions[word[i]][i] += 1
            
    return [letterPositions, numLetterPositions]

def isValidCover(cover, letterPositions):
    global coversFound
    
    if cover is None:
        return False
    
    lPs = copy.deepcopy(letterPositions[0])
    numLetterPositions = letterPositions[1]
    
    sum = 0
    
    for word in range(len(cover)):
        for letter in range(len(cover[word])):
            if lPs[cover[word][letter]][letter] != 0:
                sum += 1
                lPs[cover[word][letter]][letter] = 0

                if sum == numLetterPositions:
                    coversFound += 1
                    
                    if coversFound // 1000 == coversFound / 1000:
                        print(str(coversFound) + " covers have been found")
                    
                    return True
    return False

def addNewMinCovers(coversChecked, coversToCheck, newCoversToCheck):
    # Else, add any subcovers (that haven't yet been checked) covers to check
    for subcov in newCoversToCheck:
        if subcov not in coversChecked:
            coversToCheck.append(subcov)
    
    return coversToCheck

def reduce(cover, coversChecked, coversToCheck, minimumCovers, letterPositions):
    # If we know it's a minimum cover or we've already checked it, ignore
    if cover in minimumCovers or cover in coversChecked:
        return minimumCovers
    
    # Find all subcovers of the cover
    newCoversToCheck = []
    
    for word in range(len(cover)):
        subcover = cover[:word] + cover[word+1:]
        
        # If the subcover produced is valid
        if isValidCover(subcover, letterPositions):
            # Queue it for checking
            subcover.sort()
            if subcover not in newCoversToCheck:
                newCoversToCheck.append(subcover)
    
    # If there were no subcovers then it's a new minimum cover so add it
    if newCoversToCheck == []:
        minimumCovers.append(cover)
    else:
        simplifiedCovers = []
        
        for cov in range(len(newCoversToCheck)):
            if newCoversToCheck[cov].sort() not in coversToCheck:
                simplifiedCovers.append(newCoversToCheck[cov])
    
        # Add any subcovers (that haven't yet been checked) to check
        coversToCheck = addNewMinCovers(coversChecked, coversToCheck, simplifiedCovers)
                
    if coversToCheck == []:
        # If we've exhausted all possible covers, return the minimum covers
        return minimumCovers
    else:
        # Else, check next cover
        coversChecked = coversChecked + [cover]
        return reduce(coversToCheck[0], coversChecked, coversToCheck[1:], minimumCovers, letterPositions)


def main():
    # Test
    letterPositions  = findLetterPositions(["able", "cain", "cale", "vein"], 4) 
    possibleMinimumCovers = reduce(["able", "cain", "cale", "veil"], [], [], [], letterPositions)
    print(possibleMinimumCovers)
    
    # Kilordle inputs
    letterPositions  = findLetterPositions(WORDLES, 5) 
    possibleMinimumCovers = reduce(WORDS, [], [], [], letterPositions)
    print(possibleMinimumCovers)
 
main()