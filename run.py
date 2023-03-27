import random

def game_word(difficulty):
    if difficulty == "easy":
        word_list = ["cat", "dog", "hat", "car", "tree", "book", "door", "cake", "bird", "pen"]
    elif difficulty == "medium":
        word_list = ["computer", "python", "jacket", "sunflower", "television", "guitar", "popcorn", "giraffe", "restaurant", "hamster"]
    elif difficulty == "hard":
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





username = input("Please enter your username: ")
print("Welcome to Hangman!")


