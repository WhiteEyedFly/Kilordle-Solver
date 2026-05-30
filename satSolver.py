"""

"""

import os
import copy
import numpy as np
import random as rand

from words import WORDS, WORDLES
from tooSlow.kilordleInitialSolver import isValidCover, findLetterPositions, reduce

def transpose(wordList, wordForm=True):
    if wordForm:
        wordListNew = ["", "", "", "", ""]
        for word in range(len(wordList)):
            for letter in range(len(wordList[word])):
                wordListNew[letter] = wordListNew[letter] + wordList[word][letter]
    else:
        wordListNew = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        for word in range(len(wordList)):
            for position in range(len(wordList[word])):
                wordListNew[position] = wordListNew[position] + wordList[word][position]
    
    return wordListNew

def valuePosition(solution):
    # Solution in word form
    copySol = transpose(copy.deepcopy(solution))
    optimal = ["abcdefghijklmnopqrstuvwyz", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnoprstuvwxyz", "abcdefghiklmnoprstuwxyz"]
    
    sumA = 0
    
    for position in range(len(optimal)):
        sumA += sum([1 for letter in optimal[position] if letter in copySol[position]])
    
    return sumA

def valuePosition2(solution, wordList):
    sumA = sum([1 for word in wordList if isValidCover(solution, findLetterPositions([word], 5))])
    #print(sumA)
    return sumA

def swapper(words):
    # Takes in wordList in word form and outputs in word form
    wordList = copy.deepcopy(words)
    posVal = valuePosition2(wordList, WORDLES)
    
    #if posVal == 125:
    #    print("This position is already optimal")
    #    return wordList
    
    for chosenWord in range(len(wordList)):
        for word in WORDS:
            checkAgainst = copy.deepcopy(wordList)
            checkAgainst[chosenWord] = word
            newVal = valuePosition2(checkAgainst, WORDLES)
            
            if posVal < newVal:
                posVal = newVal
                wordList = checkAgainst
                break
            #elif posVal <= newVal: 
            #    if rand.random() < 0.5:
            #        wordList = checkAgainst
    return wordList

def findWordValues(words, letterPositions):
    word_values = {}

    for i in range(len(words)):
        summand = 0
        for letter in range(len(words[i])):
            summand += letterPositions[words[i][letter]][letter]
        word_values.update({words[i]: summand})
        
    for word in word_values:
        if word_values[word] == 0:
            word_values[word] = 1000

    return word_values

def restrictWordsByValue(value, words, letterPositions):
    wordsRemaining = []
    wordValues = findWordValues(words, letterPositions)
    
    for word in wordValues:
        if wordValues[word] < value:
            wordsRemaining.append(word)
    
    print(len(wordsRemaining))
    return wordsRemaining
    
def main():
    solution = ['zesty', 'ydrad', 'whiff', 'vuggs', 'usque', 'twixt', 'squib', 'schwa', 'rowdy', 'qajaq', 
                'pzazz', 'optic', 'nkosi', 'mekka', 'luvvy', 'kvell', 'jambu', 'itchy', 'hydro', 'glyph', 
                'fixer', 'expel', 'enzym', 'embog', 'djinn', 'crump', 'banjo', 'aglow', 'affix', 'aback']
    solution = ["zesty"] * 30

    while valuePosition2(solution, WORDLES) < len(WORDLES):
            solution = swapper(solution)
            
            print("We found position: " + str(solution))
            print("This has value: " + str(valuePosition2(solution, WORDLES)))
            print(" ")
    
    print("We found an optimal position in 30!! See below: ")
    print(solution)
    print(" ")
    
    """
    for i in range(10):
        while valuePosition(solution) < 125:
            solution = swapper(solution)
            
            print("We found position: " + str(solution))
            print("This has value: " + str(valuePosition(solution)))
            print(" ")
        
        solution.pop(1)
        
        print("We found an optimal position in " + str(40-i) + "!! See below: ")
        print(solution)
        print(" ")
    """
    
    with open("answer.txt", "a") as f:
        f.write(str(solution))
        f.write("\n")
"""
wordsRemaining = restrictWordsByValue(1200, WORDS, findLetterPositions(WORDLES, 5)[0])
main()
"""