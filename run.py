import os
import random


def clear_terminal():
    """
    Clears the terminal window for clearer screen readability.
    Found this method on Stackoverflow:
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def game_word(level):
    """
    This function selects a random word from a dictionary based
    on the given level of difficulty. It validates that user must
    chose from the available options.
    """
    word_dict = {
        "easy": ["cat", "name", "cup", "dog", "hat", "car", "tree", "book",
                 "door", "cake", "bird", "pen", "slip", "card", "game", "coin",
                 "pole"],
        "medium": ["soccer", "computer", "python", "jacket", "sunflower",
                   "television", "guitar", "popcorn", "giraffe", "restaurant",
                   "hamster", "basket", "ticket", "packet", "laptop"],
        "hard": ["qualifier", "xylophone", "juxtaposition", "quagmire",
                 "mnemonic", "haphazard", "furtive", "belligerent",
                 "ubiquitous", "zeitgeist", "quintessential", "terminal",
                 "calculator"]
    }
    if level not in word_dict:
        print("That's not a valid difficulty level. Please choose from\
            either: easy, medium or hard.")
        return None
    return random.choice(word_dict[level])


def is_valid_guess(guess, guessed_letters):
    """
    This function validates the user's input when they guess a letter.
    Checks if the letter has already been guessed by the user and if
    the guess is a single alphabetical character.
    """
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter just a single letter.")
        return False
    elif guess in guessed_letters:
        print("You've already used that letter. Try another.")
        return False
    else:
        return True


def print_hangman(lives):
    """
    This function prints the ASCII art of the hangman and its state
    for the given number of remaining lives.
    """
    hangman = [
        "   _________",
        "   |        |",
        "   |        O",
        "   |       /|\\",
        "   |        |",
        "   |       / \\",
        "___|___"
    ]
    print("\n".join(hangman[:7-lives]))


def is_game_over(lives, secret_word, word):
    """
    Function checks the state of the game and whether the game is
    over or not based on the numbe rof remaining lives left.
    """
    if lives == 0:
        print("\033[31mGame Over! You lost. The answer was: "
              f"{word.capitalize()}\033[0m")
        return True
    elif "_" not in secret_word:
        print("\033[32mYou win! You guessed the word, well done!\033[0m")
        return True
    else:
        return False


def play_hangman(difficulty, username):
    """
    This function will play a game of hangman based on the chosen user
    difficulty and their given username. It will also print the
    instructions and initializes game variables. It then enters a
    loop that prompts the player to guess letters until the
    game is over. It checks if the letter is valid and updates the
    game state. If the player guesses the secret word, they win the game.
    Otherwise, after 6 incorrect guesses they lose. Game ends with a
    won or lost message.
    """
    print(f"\033[32mWelcome {username}. Let's play some Hangman!\n\033[0m")
    print("Game instructions:")
    print("Guess the secret word one letter at a time.")
    print("Correct guessed letters will be revealed in the word.")
    print("You will lose a life for each letter guessed that is wrong.")
    print("You start out with 6 lives.")
    print("Good luck!\n")

    word = game_word(difficulty)
    if word is None:
        return

    secret_word = ["_"] * len(word)
    guessed_letters = []
    lives = 6

    print_hangman(lives)

    while not is_game_over(lives, secret_word, word):
        """
        Loop runs until game is over. Prompts players to guess a letter,
        checks if valid, then updates game state. Correctly guessed letters
        are revleaed in the secret word. Players lose a life if guesses are
        incorrect. When the game is over the loop ends.
        """
        print(" ".join(secret_word))
        print(f"Remaining Lives: {lives}")
        guess = input("Guess a letter: ").lower()

        if is_valid_guess(guess, guessed_letters):
            if guess in word:
                print("\033[32mCorrect\033[0m")
                for i, letter in enumerate(word):
                    if letter == guess:
                        secret_word[i] = guess
            else:
                clear_terminal()
                print("\033[31mIncorrect\033[0m")
                lives -= 1

            guessed_letters.append(guess)
            print_hangman(lives)

    play_again = input("Would you like to play again? (y/n/)").lower()
    if play_again == "y":
        play_hangman(difficulty, username)
    else:
        print("Thanks for playing, come back soon!")


print("\033[32m" +
      " _    _     \n" +
      "| |  | |    \n" +
      "| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  \n" +
      "|  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ \n" +
      "| |  | | (_| | | | | (_| | | | | | | (_| | | | |\n" +
      "|_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|\n" +
      "                     __/ |                      \n" +
      "                    |___/                       \n" +
      "\033[0m" +
      "Welcome to Hangman!\n")

username = input("Please enter your username: ")

while True:
    print("\nPlease select an option:\n")
    print("1 - Play the game")
    print("2 - Read the game instructions")
    print("3 - View game high scores")
    print("4 - Exit the game\n")
    choice = input("Enter your choice (1, 2, 3, or 4): ")
    print("")
    clear_terminal()
    if choice == "1":
        print("Choose a difficulty level:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        difficulty_choice = input("Enter your choice (1, 2, or 3): ")
        print("")
        clear_terminal()
        if difficulty_choice == "1":
            play_hangman("easy", username)
        elif difficulty_choice == "2":
            play_hangman("medium", username)
        elif difficulty_choice == "3":
            play_hangman("hard", username)
        else:
            print("Invalid input. Please enter 1, 2, or 3.")
    elif choice == "2":
        print("Instructions:")
        print("Try to guess the secret word one letter at a time.")
        print("If you guess a correct letter, it will be revealed in the \
            word.")
        print("If you guess an incorrect letter, you will lose a life.")
        print("You have 6 lives to start with.")
        print("Good luck!\n")
    elif choice == "3":
        print("High scores:")
        print("1. Player 1 - 1000 points")
        print("2. Player 2 - 750 points")
        print("3. Player 3 - 500 points\n")
    elif choice == "4":
        print("Thanks for playing Hangman!")
        break
    else:
        print("Invalid input. Please enter 1, 2, 3, or 4.")
