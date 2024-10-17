from modules import (
    load_game_variables,
    process_attempt,
    print_word,
    check_win_condition
)

def run_game():
    (
        word_to_guess,
        remaining_word,
        word_list,
        user_won,
        attempts
    ) = load_game_variables("data.txt")
    while not user_won:
        print(f"You have {attempts} attempts")
        user_letter = input("Type a word: ").lower()
        remaining_word, attempts = process_attempt(remaining_word, user_letter, attempts)
        print_word(word_list, word_to_guess, user_letter)
        user_won = check_win_condition(remaining_word)
        if user_won:
            print("You won!")
        elif attempts == 0:
            print("Sorry, you loose")
            break


if __name__ == '__main__':
    run_game()