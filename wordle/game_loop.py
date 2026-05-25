from rich import print

from config.settings import settings
from wordle.game import WordleGame
from wordle.word_ingestion import request_api

color_tags = {
    "GREEN": "black on green",
    "YELLOW": "black on yellow",
    "GRAY": "black on grey37",
}

while True:
    random_word_model = request_api(settings.api_url)
    if random_word_model is not None:
        random_word = random_word_model.word
    else:
        break

    no_of_tries = 5

    Game = WordleGame(random_word)

    print(f"Guess a word with {len(Game.secret_word)} letters!")
    while no_of_tries > 0:
        guess = input("Enter your guess: ")

        (status, err) = Game.guess_word(guess)

        if status == "error":
            print(f"Error! {err}\n")
            continue

        if status == "correct":
            print("You got it right!")
            break

        if status == "valid":
            output_blocks = [
                f"[{color_tags.get(state, 'black on grey37')}] {Game.guess[i].upper()} [/]"
                for i, state in enumerate(Game.current_solution)
            ]

            print(" ".join(output_blocks))

        no_of_tries -= 1
        print(f"\nTries left: {no_of_tries}\n")

    print(f"The correct word was: {Game.secret_word}")

    break
