def process_attempt(remaining_word, user_letter, attempts):
    if user_letter not in remaining_word:
        attempts -= 1
        print("The letter is not in the word, try again.")
    else:
        attempts -= 1
        remaining_word = remaining_word.replace(user_letter, "")
    return remaining_word, attempts
