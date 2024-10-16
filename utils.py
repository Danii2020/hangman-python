import random

def get_random_word(words):
    return random.choice(words)

def print_word(word_list, word_to_guess, guessed_letter):
    for index in range(len(word_to_guess)):
        if word_to_guess[index] == guessed_letter:
            word_list[index] = guessed_letter
    print(" ".join(word_list))