from modules.hangman import HangmanGame

if __name__ == "__main__":
    hangman_game = HangmanGame("data.txt")
    print("Welcome to the hangman game!")
    hangman_game.play()