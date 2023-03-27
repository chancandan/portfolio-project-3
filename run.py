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


