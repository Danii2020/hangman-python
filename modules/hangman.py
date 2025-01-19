import os
from .utils import (
    get_random_word,
    print_hangman,
    print_word,
    load_phrases_file
)

class HangmanGame:
    def __init__(self, phrase_file):
        self.__phrase_file = phrase_file
        self.__word_to_guess = None
        self.__remaining_word = None
        self.__word_list = []
        self.__user_won = False
        self.__hangman_stage = 0

    def __initialize_game(self):
        self.__word_to_guess = get_random_word(
            load_phrases_file(self.__phrase_file)
        )
        self.__remaining_word = self.__word_to_guess.replace(" ", "")
        self.__word_list = ['_' if letter != " " else " " for letter in self.__word_to_guess]
        self.__user_won = False
        self.__attempts = 10
        self.__hangman_stage = 0

    def __check_win_condition(self):
        return not self.__remaining_word

    def __process_attempt(self, user_letter):
        if user_letter not in self.__remaining_word:
            print_hangman(self.__hangman_stage)
            self.__hangman_stage += 1
            print("The letter is not in the word, try again.")
        else:
            self.__remaining_word = self.__remaining_word.replace(user_letter, "")

    def play(self):
        self.__initialize_game()
        while not self.__user_won:
            try:
                user_letter = input("Type a letter: ").lower()
                os.system('clear')
                self.__process_attempt(user_letter)
                print_hangman(self.__hangman_stage)
                print_word(self.__word_list, self.__word_to_guess, user_letter)
                self.__user_won = self.__check_win_condition()
                if self.__user_won:
                    print("You won!")
            except IndexError:
                print_hangman(-1)
                print("Sorry, you lose")
                break
