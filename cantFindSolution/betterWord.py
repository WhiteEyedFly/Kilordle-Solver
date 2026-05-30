import copy
from words import WORDS, WORDLES
from tooSlow.kilordleInitialSolver import findLetterPositions, isValidCover

def has_n_new_letters(word, limit, solution):
    # Find a base list
    new_letters_real = 5
    comparison_word = "a"
    for chosen_word in solution:
        new_letters = 0

        for i in range(5):
            if is_new(word, chosen_word, i):
                new_letters += 1
            else:
                word = replace_i(word, i)

        if new_letters < new_letters_real:
            new_letters_real = new_letters
            comparison_word = chosen_word

    if new_letters_real >= 5 - limit:
        return True
    return False

def is_new(word, chosen_word, i):
    if word[i] != chosen_word[i]:
        if word[i] != "1":
            if letterPositions[word[i]][i] > 0:
                return True
    return False

def replace_i(word, i):
    if i == 0:
        word = "1" + word[1:]
    elif i == 4:
        word = word[:4] + "1"
    else:
        word = word[:i] + "1" + word[i+1:]
    return word

def makeListNew(WORDS, WORDLES, startingWords, letterPositions):
    chosen_words = startingWords
    remaining_words = WORDS
    
    limit = 5

    while not isValidCover(chosen_words, lPs):
        print(chosen_words)
        acceptableWords = []
        
        if limit == 0:
            break
        
        for word in WORDS:
            if has_n_new_letters(word, limit, chosen_words):
                acceptableWords.append(word)
        
        if acceptableWords ==[]:
            limit -= 1
        
        else:
            best = bestWord(acceptableWords, letterPositions)
            
            chosen_words.append(best)

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
        
    for word in word_values:
        if word_values[word] == 0:
            word_values[word] = 1000

    x = min(word_values, key=word_values.get)

    return x
    
lPs = findLetterPositions(WORDLES, 5)
letterPositions = findLetterPositions(WORDLES, 5)[0]
print(letterPositions)
print(makeListNew(WORDS, WORDLES, [], letterPositions))