

"""
General Idea:
Take a solution from a previous example and select n items, check if there is a set of n-1 words that covers those n items
If there is, replace
Continue until there are no such sets
"""

# A 36 solution
baseSolution = ["abyss", "crown", "gleam", "magma", "pzazz", "toxic", "adobe", "dizzy", "haiku", "ninja", "quick", "using", 
                "aglow", "enjoy", "ivory", "often", "redux", "verge", "amble", "epoxy", "joker", "oxide", "scoff", "wowed", 
                "awful", "ethyl", "khaki", "pesto", "skimp", "yacht", "bevvy", "fjord", "lymph", "pique", "squab", "zippy"]

# Value each word in the cover based on the number of non-repeated letters
# Take the words with the least value and look for smaller covers of those letters

def valueWords(words):
    # Order by number of repeated letters
    for word in words:
        for letter in words:

def main():
    # Find all words that have only 1 non-shared letter
    # Find the smallest cover of those words
    wordValues = valueWords(baseSolution)
    pass

main()