from .utils import get_random_word

def load_words_file(text_file):
    words = []
    with open(text_file) as f:
        for word in f.read().split():
            if word.isalpha() and len(word) >= 4 and len(word) <= 10:
                words.append(word.lower())
    return words

def load_game_variables(file_name):
    global word_to_guess
    global remaining_word
    global word_list
    global user_won
    global attempts

    word_to_guess = get_random_word(load_words_file(file_name))
    remaining_word = word_to_guess
    word_list = ['_' for _ in word_to_guess]
    user_won = False
    attempts = 10
    return word_to_guess, remaining_word, word_list, user_won, attempts
