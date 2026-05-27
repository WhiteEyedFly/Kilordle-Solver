from words import WORDS, WORDLES

letter_positions = {}
final_list = ["aahed"]

def find_letter_positions(answers):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        letter_positions.update({letter:[0,0,0,0,0]})

    for word in answers:
        for i in range(5):
            letter_positions[word[i]][i] += 1

def make_list(dict, answers, final_list):
    find_letter_positions(answers)

    # Make base list
    for i in range(5):
        for word in dict:
            if has_n_new_letters(word, 5 - i):
                final_list.append(word)

    print(final_list)

    for i in range(len(final_list)):
        final_list[i] = final_list[i][:5]

    #order_list(final_list)
    print(len(final_list))
    
def has_n_new_letters(word, limit):
    # Find a base list
    new_letters_real = 5
    comparison_word = "a"
    for chosen_word in final_list:
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
            if letter_positions[word[i]][i] > 0:
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

def order_list(final_list):
    ordered_list = []
    word_values = {}

    for i in range(len(final_list)):
        summand = 0
        for letter in range(len(final_list[i])):
            summand += letter_positions[final_list[i][letter]][letter]
        word_values.update({final_list[i]: summand})
    
    for i in range(len(final_list)):
        #print(max(word_values, key=word_values.get), )
        ordered_list.append(max(word_values, key=word_values.get))
        word_values.pop(max(word_values, key=word_values.get))

    return print(ordered_list)

def make_list_new(WORDS, WORDLES):
    find_letter_positions(WORDLES)

    chosen_words = []
    remaining_words = WORDS

    while True:
        best = best_word(remaining_words)
        if best == "STOP":
            break
        else:
            chosen_words.append(best_word(remaining_words))
            remaining_words.remove(best)

        for i in range(len(best)):
            letter_positions[best[i]][i] = 0

    x = make_list_new(chosen_words, WORDLES)

    if len(x) < len(chosen_words):
        return x
    else:
        print(chosen_words)
        print(len(chosen_words))
        return chosen_words

def best_word(words):
    word_values = {}

    for i in range(len(words)):
        summand = 0
        for letter in range(len(words[i])):
            summand += letter_positions[words[i][letter]][letter]
        word_values.update({words[i]: summand})

    x = max(word_values, key=word_values.get)

    if word_values[x] == 0:
        return "STOP"
    else:
        return x


#make_list(WORDS, WORDLES, final_list)
make_list_new(WORDS, WORDLES)
