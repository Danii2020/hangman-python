from loader import load_game_variables
from utils import print_word

def run_game():
    word_to_guess, remaining_word, word_list, user_won = load_game_variables("example.txt")
    while not user_won:
        user_letter = input("Type a word: ").lower()
        if not user_letter in remaining_word:
            print("The letter is not in the word, try again ")
        else:
            remaining_word = remaining_word.replace(user_letter, "")
        print_word(word_list, word_to_guess, user_letter)
        if not remaining_word:
            print("You won!")
            user_won = True

if __name__ == '__main__':
    run_game()