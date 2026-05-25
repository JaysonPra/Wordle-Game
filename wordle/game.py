from typing import Literal

type GuessStatus = Literal["error", "valid", "correct"]


class WordleGame:
    def __init__(self, secret_word: str) -> None:
        self.secret_word = secret_word.lower()
        self.current_solution: list[str] = []
        self.guess = ""

    def validate_guess(self) -> tuple[bool, str]:
        if self.guess == "":
            return (False, "Empty guess! Please enter a word!")
        if len(self.guess) != len(self.secret_word):
            return (
                False,
                f"Incorrect length of guess. Secret word length: {len(self.secret_word)}, your guess word length: {len(self.guess)}",
            )
        return (True, "")

    def evaluate_guess(self) -> None:
        self.current_solution = ["GRAY" for _ in self.secret_word]

        # Green Pass
        for i, guess_letter in enumerate(self.guess):
            if guess_letter == self.secret_word[i]:
                self.current_solution[i] = "GREEN"

        # Yellow Pass
        for i in range(len(self.guess)):
            if self.current_solution[i] == "GREEN":
                continue
            if self.guess[i] in self.secret_word:
                self.current_solution[i] = "YELLOW"

    def guess_word(self, guess: str) -> tuple[GuessStatus, str]:
        self.guess = guess.lower()

        (is_valid, error) = self.validate_guess()
        if not is_valid:
            return ("error", error)

        self.evaluate_guess()

        if all(status == "GREEN" for status in self.current_solution):
            return ("correct", "")

        return ("valid", "")
