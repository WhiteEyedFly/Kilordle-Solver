import os
import copy
import numpy as np
import random as rand

from words import WORDS, WORDLES
from tooSlow.kilordleInitialSolver import findLetterPositions

def coversWord(cover, word):
    covers = 0
    
    for coverLetter in range(5):
        for coverWord in cover:
            if coverWord[coverLetter] == word[coverLetter]:
                word = word[:coverLetter] + " " + word[coverLetter+1:]

    if word == "     ":
        return True
    return False

def valuePosition2(position, wordList):
    return sum([1 for word in wordList if coversWord(position, word)])

def findWordsRemaining(cover, wordList):
    return [word for word in wordList if not coversWord(cover, word)]
    
def swapper(words, toCover, chooseFrom):
    newPos = words
    choiceList = copy.deepcopy(chooseFrom)
    posVal = valuePosition2(words, toCover)
    bestVal = posVal
    swapFrom, swapTo = "", ""
    
    
    for chosenWord in words:
        rubbishWords = []
        
        for word in choiceList:
            checkAgainst = copy.deepcopy(words)
            checkAgainst.remove(chosenWord)
            checkAgainst.append(word)
            
            checkVal = valuePosition2(checkAgainst, toCover)
            
            if checkVal > bestVal:
                swapFrom = chosenWord
                swapTo = word
                newPos = checkAgainst
                bestVal = checkVal
            # Filter off the worst performing words in the early stages to speed up the algorithm
            elif posVal < 2100:
                if checkVal < bestVal - 50:
                    rubbishWords.append(word)
        
        for word in rubbishWords:
            choiceList.remove(word)
    
    if bestVal > posVal:
        print("We swapped '{}' to '{}' to cover {} more words".format(swapFrom, swapTo, bestVal - posVal))
    else:
        print("No better position could be found from here; we have reached a local maximum.")
    
    return [newPos, bestVal]

def findWordValues(words, letterPositions):
    wordValues = {}

    for i in range(len(words)):
        summand = 0
        for letter in range(len(words[i])):
            summand += letterPositions[words[i][letter]][letter]
        wordValues.update({words[i]: summand})
        
    for word in wordValues:
        if wordValues[word] == 0:
            wordValues[word] = 1000
            
    return wordValues

def randomisePosition(numWords, chooseFrom):
    solution = []
    UB = len(chooseFrom)
    
    for n in range(numWords):
        solution.append(chooseFrom[rand.randint(0, UB)])
        
    return solution
   
def partRandomisePosition(numWords, chooseFrom, wordList):
    wordList[:5] = randomisePosition(numWords, chooseFrom)
    
    return wordList
    
def solver(start, toCover, chooseFrom):
    toCoverLength = len(toCover)
    solVal = valuePosition2(start, toCover)
    solution = start
    wordsRemaining = findWordsRemaining(solution, chooseFrom)
    
    record = start
    recordVal = solVal
    i = 1
    
    print("We started at position: " + str(start))
    print("This covers: {} of {} words! ({}%)".format(solVal, toCoverLength, round(100*solVal/toCoverLength, 2)))
    print("There are {} of {} words remaining to select from. ({}%)".format(len(wordsRemaining), len(chooseFrom), round(100*len(wordsRemaining)/len(chooseFrom), 2)))
    print(" ")
    
    while solVal < toCoverLength:
        initSolVal = solVal
        
        solutionAndValue = swapper(solution, toCover, wordsRemaining)
        solution = solutionAndValue[0]
        solVal = solutionAndValue[1]
        
        print("Iteration: {}".format(i))
        
        if initSolVal == solVal:
            solution = partRandomisePosition(5, chooseFrom, solution)
            print("We randomised the first 5 words to position: " + str(solution))
        else:
            print("We found position: " + str(solution))
            
        wordsRemaining = findWordsRemaining(solution, chooseFrom)
        
        print("This covers: {} of {} words! ({}%)".format(solVal, toCoverLength, round(100*solVal/toCoverLength, 2)))
        print("There are {} of {} words remaining to select from. ({}%)".format(len(wordsRemaining), len(chooseFrom), round(100*len(wordsRemaining)/len(chooseFrom), 2)))
        
        if solVal > recordVal:
            recordVal = solVal
            record = solution
        
        print("Our current record is: {}".format(recordVal))
        print(record)
        print(" ")
        
        i += 1
    
    print("We found an optimal position in 30!! See below: ")
    print(solution)
    print(" ")
    
    with open("answer.txt", "a") as f:
        f.write(str(solution))
        f.write("\n")

def main():
    start = ['chace', 'lieve', 'jivey', 'begem', 'clags', 'ducky', 'hexed', 'rewan', 'giust', 'twank', 
             'synth', 'astir', 'indol', 'appro', 'etyma', 'misdo', 'embog', 'viffs', 'wushu', 'kohls', 
             'naric', 'scowp', 'quaff', 'ablow', 'oribi', 'adsum', 'uveal', 'yampy', 'pakka', 'fezzy']
    
    solver(start, WORDLES, WORDS)
        
main()

"""
Improvements:
Only randomise some items
"""