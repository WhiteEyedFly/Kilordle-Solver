import os
import copy
import numpy as np
import random as rand

from words import WORDS, WORDLES
from tooSlow.kilordleInitialSolver import isValidCover, findLetterPositions, reduce

"""
Main idea:

Speed up kilordleInitialSolver by randomly shrinking the data set
"""

def findSmallSolutions(repeat, number, wordList, letterPositions):
  solsList = []
  for j in range(repeat):
    solution = []
    
    for i in range(number):
      upperBound = len(wordList) - 1
      
      R = rand.randint(0, upperBound)
      
      if wordList[R] not in solution:
        solution.append(wordList[R])
      
    if isValidCover(solution, letterPositions):
      solsList = solsList + [solution]
  
  return solsList

def main():
  optimalSolutions = []
  
  letterPositions  = findLetterPositions(WORDLES, 5)
  smallSolutions = findSmallSolutions(1000, 800, WORDS, letterPositions)
  
  # Find most common words
  print(letterPositions)
  
  smallerSolutions = []
  smallestSolutions = []
  
  print(str(len(smallSolutions)) + " small solutions found")
  
  for solution in smallSolutions[0:len(smallSolutions)-1]:
    smallerSolutions = smallerSolutions + [findSmallSolutions(1000, 500, WORDS, letterPositions)]
    
  os.remove("answer.txt")
  with open("answer.txt", "a") as f:
    for solar in smallSolutions[0]:
      f.write(solar)
      f.write("\n")
    
  print(str(len(smallerSolutions)) + " smaller solutions found")
  
  print(reduce(smallSolutions[0], [], [], [], letterPositions))
    
  for solution in smallerSolutions:
    smallestSolutions = smallestSolutions + [findSmallSolutions(1000, 30, WORDS, letterPositions)]


#main()