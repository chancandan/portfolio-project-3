import random

def game_word(level):
    word_dict = {
        "easy": ["cat", "name", "dog", "hat", "car", "tree", "book", "door",\
        "cake", "bird", "pen", "slip", "card", "game", "coin"],
        "medium": ["soccer", "computer", "python", "jacket", "sunflower",\
        "television", "guitar", "popcorn", "giraffe", "restaurant",\
        "hamster", "basket", "ticket", "packet"],
        "hard": ["qualifier", "xylophone", "juxtaposition", "quagmire",\
        "mnemonic", "haphazard", "furtive", "belligerent", "ubiquitous",\
        "zeitgeist", "quintessential", "terminal"]
    }
    if level not in word_dict:
        print("That's not a valid difficulty level. Please choose from\
            either: easy, medium or hard.")
        return None
    return random.choice(word_dict[level])


def play_hangman(difficulty, username):
    print("\033[32m" + f"Welcome {username}. Let's play some Hangman!\n" + "\033[0m")
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

    # ASCII art of the hangman
    hangman = [
        "   _________",
        "   |        |",
        "   |        O",
        "   |       /|\\",
        "   |        |",
        "   |       / \\",
        "___|___"
    ]
    # Print the initial hangman
    print("\n".join(hangman[:lives]))

    while lives > 0 and "_" in secret_word:
        print(" ".join(secret_word))
        print(f"Remaining Lives: {lives}")
        guess = input("Guess a letter: \n").lower()

        # Validate the user's input when they guess a letter.
        while len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter just a single letter.")
            guess = input("Guess a letter: \n").lower()

        if guess in guessed_letters:
            print("You've already used that letter. Try another.")
        elif guess in word:
            print("\033[32m" + "Correct" + "\033[0m")
            for i in range(len(word)):
                if word[i] == guess:
                    secret_word[i] = guess
        else:
            print("\033[31m" + "Incorrect" + "\033[0m")
            lives -= 1

        guessed_letters.append(guess)

        # Print the updated hangman
        print("\n".join(hangman[:lives]))

    if lives == 0:
        print("\033[31m" + "Game Over! " + "\033[0m"
              "You lost. The answer was: " + word.capitalize())
    else:
        print("\033[32m" + "You win! " + "\033[0m" + 
              "You guessed the word, well done!")

    play_again = input("Would you like to play again? (y/n/)").lower()
    if play_again == "y":
        play_hangman(difficulty, username)
    else:
        print("Thanks for playing, come back soon!")


print("\033[32m" + """
 _    _                                   
| |  | |                                       
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                     
                    |___/                      

""" + "\033[0m" + "Welcome to Hangman!\n")
username = input("Please enter your username: ")

while True:
    print("Please select an option:")
    print("1 - Play the game")
    print("2 - Read the game instructions")
    print("3 - View game high scores")
    print("4 - Exit the game")
    choice = input("Enter your choice (1, 2, 3, or 4): ")
    print("")

    if choice == "1":
        print("Choose a difficulty level:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        difficulty_choice = input("Enter your choice (1, 2, or 3): ")
        print("")
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
        