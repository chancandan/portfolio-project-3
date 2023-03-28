import random

def game_word(level):
    if level == "easy":
        word_list = ["cat", "dog", "hat", "car", "tree", "book", "door", "cake", "bird", "pen"]
    elif level == "medium":
        word_list = ["computer", "python", "jacket", "sunflower", "television", "guitar", "popcorn", "giraffe", "restaurant", "hamster"]
    elif level == "hard":
        word_list = ["xylophone", "juxtaposition", "quagmire", "mnemonic", "haphazard", "furtive", "belligerent", "ubiquitous", "zeitgeist", "quintessential"]
    else:
        print("That's not a valid difficulty level. Please choose from either easy, medium or hard.")
        return None

    word = random.choice(word_list)
    return word


def play_hangman(difficulty, username):
    print(f"Welcome {username}. Let's play some Hangman!\n")
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
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already used that letter. Try another.")
        elif len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter just a single letter.")
        elif guess in word:
            print("Correct")
            for i in range(len(word)):
                if word[i] == guess:
                    secret_word[i] = guess
        else:
            print("Incorrect")
            lives -= 1

        guessed_letters.append(guess)
        print("")

    if lives == 0:
        print("Game Over! You lost. The answer was: " + word.capitalize())
    else:
        print("You guessed the word, well done!")

    play_again = input("Would you like to play again? (y/n/)").lower()
    if play_again == "y":
        play_hangman(difficulty, username)
    else:
        print("Thanks for playing, come back soon!")

username = input("Please enter your username: ")
print("Welcome to Hangman!")
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
        print("If you guess a correct letter, it will be revealed in the word.")
        print("If you guess an incorrect letter, you will lose a life.")
        print("You have 6 lives to start with.")
        print("Good luck!\n")
    elif choice == "3":
        print("High scores:")
        print("1. Player 1 - 1000 points")
        print("2. Player 2 - 750 points")
        print("3. Player 3 - 500 points")
    elif choice == "4":
        print("Thanks for playing Hangman!")
        break
    else:
        print("Invalid input. Please enter 1, 2, 3, or 4.")


