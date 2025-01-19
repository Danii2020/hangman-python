import random

def get_random_word(words):
    return random.choice(words)

def print_word(word_list, word_to_guess, guessed_letter):
    for index in range(len(word_to_guess)):
        if word_to_guess[index] == guessed_letter:
            word_list[index] = guessed_letter
    print(" ".join(word_list))


def load_phrases_file(text_file):
    phrases = []
    with open(text_file, encoding='utf-8') as f:
        for line in f:
            phrase = line.strip()
            if phrase and all(word.isalpha() or word.isspace() for word in phrase):
                phrases.append(phrase.lower())
    return phrases


def print_hangman(hangman_stage):
    stages = [
        """
           ------
                |
                |
                |
                |
                |
        ---------
        """,
        """
           ------
           |    |
                |
                |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\   |
          /     |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        ---------
        """
    ]
    print(stages[hangman_stage])