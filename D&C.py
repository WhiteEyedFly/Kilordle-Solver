import os
import copy
import numpy as np
import random as rand
from itertools import chain

from words import WORDS, WORDLES
from tooSlow.kilordleInitialSolver import isValidCover, findLetterPositions, reduce

def splitList(wordList):
    # Given an input list, return it as 2 output lists split in the middle
    # If of odd length, the second output should be one longer
    
    length = len(wordList)
    halfLength = length // 2
    
    return [wordList[:halfLength]] + [wordList[halfLength:]]

def leastValuableWord(wordList):
    # Given a list of words, find the least valuable one and return it
    
    letterPositions = findLetterPositions(WORDLES, 5)[0]
    wordDict = {}
    
    for word in wordList:
        sum = 0
        for position in range(len(word)):
            sum += letterPositions[word[position]][position]
            
        wordDict[word] = sum
    
    minVal = max(wordDict.values())
    minWords = [k for k, v in wordDict.items() if v == minVal]
    
    return minWords[0]

def findMinCover(cover1, cover2):
    maxCover = list(set(chain(cover1, cover2)))
    
    if len(maxCover) == 2:
        return maxCover
    
    # Find all possible covers of the words contained within maxCover
    coveredWords = {}
    
    tracker = True
    
    while tracker:
        removableWords = []
        
        for word in maxCover:
            tempCover = copy.copy(maxCover)
            tempCover.remove(word)
            #print(maxCover, tempCover, word)
            
            if isValidCover(tempCover, findLetterPositions([word], 5)):
                removableWords.append(word)
        
        if removableWords == []:
            tracker = False
        else:
            maxCover.remove(leastValuableWord(removableWords))
    
    return maxCover

def divideAndConquer(wordList):
    # Base case
    if len(wordList) == 1:
        return wordList

    # Divider
    split = splitList(wordList)
    
    cover1 = divideAndConquer(split[0])
    cover2 = divideAndConquer(split[1])
    result = findMinCover(cover1, cover2)
    
    #print(cover1, cover2, result)
    
    return result

def main():
    
    solution = WORDS
    i = 1
    
    while len(solution) > 45:
        print("Attempt: " + str(i))
        solution = divideAndConquer(WORDS)
        i += 1
        print(solution)
        print("Is a " + str(len(solution)) + " solution")
        print(" ")
    
main()


"""
Next Steps:
Find where you're losing information
Remove any words from WORDS that have letterpositions that aren't in WORDLES
Swap out 
"""