import os
import copy
import numpy as np
import random as rand

from words import WORDS, WORDLES
from tooSlow.kilordleInitialSolver import isValidCover, findLetterPositions, reduce
#from kilordleSuperSolver import unpacker, wordFinder

def makeListNew(WORDS, WORDLES, startingWords, letterPositions):
    chosen_words = startingWords
    remaining_words = WORDS

    while True:
        best = bestWord(remaining_words, letterPositions)
        
        if best == "STOP":
            break
        else:
            chosen_words.append(best)
            remaining_words.remove(best)

        for i in range(len(best)):
            letterPositions[best[i]][i] = 0

    return chosen_words

def bestWord(words, letterPositions):
    word_values = {}

    for i in range(len(words)):
        summand = 0
        for letter in range(len(words[i])):
            summand += letterPositions[words[i][letter]][letter]
        word_values.update({words[i]: summand})

    x = max(word_values, key=word_values.get)

    if word_values[x] == 0:
        return "STOP"
    else:
        return x

def unpacker(letterPositions, answers, wordList):
    # Outputs a list of all words that cover the letterposition that occurs least
    copyPositions = copy.deepcopy(letterPositions)
    
    minOccurrences = 10000
    minLetterPositions = []
    
    # Create a list of the letter-positions that appear least in letterPositions
    for letter in copyPositions:
        for position in range(len(copyPositions[letter])):
            if copyPositions[letter][position] < minOccurrences:
                if copyPositions[letter][position] > 0:
                    minOccurrences = copyPositions[letter][position]
                    minLetterPositions = [[letter, position]]
            elif copyPositions[letter][position] == minOccurrences:
                minLetterPositions = minLetterPositions + [[letter, position]]
            else:
                pass
    
    if minOccurrences == 10000:
        return []
    
    acceptableChoices = []
    
    for minimum in range(len(minLetterPositions)):
        words = wordFinder(minLetterPositions[minimum], wordList)
        
        for word in words:
            if word not in acceptableChoices:
                acceptableChoices.append(word)
        
    return acceptableChoices
    
def wordFinder(letterPosition, wordList):
    # Outputs a list of all words that cover the letter position
    letter = letterPosition[0]
    position = letterPosition[1]
    
    acceptableWords = []
    
    for word in wordList:
        if word[position] == letter:
            acceptableWords.append(word)
    
    return acceptableWords

def reducer(acceptableWords, answers, wordList, letterPositions, solution, solutions, setsChecked):
    # Outputs all minimum solutions given a set of starting words
    # Works recursively using currCover
    
    # After the first 6 words are chosen, resort to greedy
    if len(solution) == 6:
        print(solution)
        return makeListNew(answers, wordList, solution, letterPositions)
    
    R = rand.randint(0, len(acceptableWords)-1)
    word = acceptableWords[R]
    
    solver = solution + [word]
    solver.sort()
    
    if solver not in setsChecked[len(solver)]:
        setsChecked[len(solver)] = setsChecked[len(solver)] + [solver]
        
        copyPositions = copy.deepcopy(letterPositions)
        
        for position in range(len(word)):
            copyPositions[word[position]][position] = 0
        
        nextWords = unpacker(copyPositions, answers, wordList)
        
        if nextWords == []:
            solutions = solutions + [solver]
        else:
            solutions = reducer(nextWords, answers, wordList, copyPositions, solver, solutions, setsChecked)
    
    return solutions
            

def main():
    sets = [[] for i in range(100)]
    #letterPositions = findLetterPositions(["able", "cain", "veil"], 4)[0]
    #starterWords = unpacker(letterPositions, ["able", "cain", "veil", "cant"], ["able", "cain", "veil"])
    #solutions = reducer(starterWords, ["able", "cain", "veil", "cant"], ["able", "cain", "veil"], letterPositions, [], [], sets)
    
    letterPositions = findLetterPositions(WORDLES, 5)[0]
    starterWords = unpacker(letterPositions, WORDS, WORDLES)
    solution = reducer(starterWords, WORDS, WORDLES, letterPositions, [], [], sets)
    
    print(solution)

main()
