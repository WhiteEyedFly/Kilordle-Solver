import os
import copy
import numpy as np
import random as rand

from words import WORDS, WORDLES
from tooSlow.kilordleInitialSolver import findLetterPositions

"""
General idea:
Make 1000 random covers
Find the most common word in all covers, select it and make 1000 more covers including it
Repeat until you get a cover without random generation
"""

def isValidCover(cover, letterPositions):
    lPs = copy.deepcopy(letterPositions[0])
    numLetterPositions = letterPositions[1]
    
    for word in range(len(cover)):
        for letter in range(len(cover[word])):
            if lPs[cover[word][letter]][letter] != 0:
                lPs[cover[word][letter]][letter] = 0
    
    sum = 0
    
    for letter in lPs:
        for position in lPs[letter]:
            sum += position

    if sum == 0:
        return True
    return False

def findMostCommonWord(solutions, exempt):
    words = {}
    
    for solution in solutions:
        for word in solution:
            if word not in exempt:
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
            else:
                words[word] = 0
    
    maxV = 0
    maxW = []
    
    for word in words:
        if words[word] > maxV:
            maxW = [word]
            maxV = words[word]
        elif words[word] == maxV:
            maxW.append(word)
    
    print(str(maxW) + " occured " + str(maxV) + " times")
    
    return [maxW[0]]

def findRandSolution(wordList, letterPositions, start):
    start = copy.deepcopy(start)
    
    # Add random words until you find a cover
    while not isValidCover(start, letterPositions):
        R = rand.randint(0, len(wordList) - 1)
        
        start.append(wordList[R])
        wordList = restrictWordList(wordList, start)
    
    return start

def findRandSolutions(repeat, wordList, letterPositions, startingList):
    # Make repeat solutions
    solsList = []
    start = copy.copy(startingList)
    
    for j in range(repeat):
        solsList = solsList + [findRandSolution(wordList, letterPositions, start)]
    
    return solsList

def restrictWordList(wordList, solution):
    copyList = copy.copy(wordList)
            
    for word in wordList:
        if isValidCover(solution, findLetterPositions([word], 5)):
            copyList.remove(word)
    
    return copyList

def main():
    finalSolution = ["pzazz"]
    wordsLeft = restrictWordList(WORDS, finalSolution)
    
    lPs = findLetterPositions(WORDLES, 5)
    i = 1
    
    while not isValidCover(finalSolution, lPs):
        # Speed up by adding every one that occurs the most times
        # restrict wordle list
        letterPositions = findLetterPositions(wordsLeft, 5)
        solutions = findRandSolutions(5, wordsLeft, letterPositions, finalSolution)
        mostCommonWords = findMostCommonWord(solutions, finalSolution)
        finalSolution = finalSolution + mostCommonWords
        wordsLeft = restrictWordList(wordsLeft, finalSolution)
        print(str(i) + ". " + str(mostCommonWords) + " was added")
        print(finalSolution)
        print(" ")
        
        i += 1
    
    print("We found the following " + str(i) + " solution:")
    print(finalSolution)

# 65 solution
main()