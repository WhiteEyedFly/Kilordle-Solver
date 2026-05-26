import copy
import numpy as np

from words import WORDS, WORDLES
from kilordleInitialSolver import isValidCover, findLetterPositions, reduce

"""
Main idea:

Speed up kilordleInitialSolver by shrinking the data set
"""

def findSmallSolutions(wordList, letterPositions):
  
  return [[]]

def main():
  letterPositions  = findLetterPositions(WORDLES, 5)
  
  smallSolutions = findSmallSolutions(WORDS, letterPositions)
  
  optimalSolutions = []
  
  for solution in smallSolutions:
    optimalSolutions.append(reduce(solution))
  
  print(optimalSolutions)

 
main()