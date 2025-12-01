# -*- coding: utf-8 -*-
"""
@author: Purple Sami Nybakk

Wordlist is from:
https://python.sdv.u-paris.fr/data-files/english-common-words.txt

Insanity Word Guessing Game:
- Reads words, picks difficulty
- Selects a secret word at random
- Player guesses until solved or out of tries
- Can use other wordlists
- Tracks history
- Interactive
"""

from random import randint

# Track history of each completed game
game_history = []


def give_hint(secret, display):
    """
    Cool option:
    - Provides a hint by revealing one random hidden letter.
    - Finds all indices in display still set to "_".
    - Picks one index at random from those hidden positions.
    - Reveals that letter and show its alphabetic neighbors.
    """
    hidden = [i for i, c in enumerate(display) if c == "_"]
    if not hidden:
        return
    pos = hidden[randint(0, len(hidden) - 1)]
    letter = secret[pos]
    prev_char = chr(ord(letter) - 1) if letter > "a" else letter
    next_char = chr(ord(letter) + 1) if letter < "z" else letter
    print(
        f"\nHint: the letter at position {pos+1} is between "
        f"'{prev_char}' and '{next_char}'."
    )

#   1) Read words from file


words = []
try:
    input_file = open("words.txt", "r")
except FileNotFoundError:
    print(
        "ERROR: words.txt not found! Please place it in the same folder."
    )
    exit(1)

for line in input_file:
    w = line.strip()
    if w:
        words.append(w.lower())
input_file.close()

# Main loop for multiple rounds
while True:
    #   2) Choose difficulty
    print("\nWelcome to Purple Team's Insanity Word Guessing Game!\n")
    print("Choose your difficulty level:\n")
    print("  1. Easy   = words < 5 letters")
    print("  2. Medium = words 6-8 letters")
    print("  3. Hard   = words > 9 letters")
    while True:
        choice = input("\nChoose wisely... [1/2/3]: ").strip()
        if choice in ("1", "2", "3"):
            break
        print("Oh! Invalid choice. Choose 1, 2 or 3.")

    # Filter words by chosen length
    candidates = []
    for w in words:
        ln = len(w)
        if (choice == "1" and ln <= 5) or \
           (choice == "2" and 6 <= ln <= 8) or \
           (choice == "3" and ln >= 9):
            candidates.append(w)
    if not candidates:
        candidates = words.copy()

    #   3) Select a random word
    secret = candidates[randint(0, len(candidates) - 1)]

    #   4) Initialize game state
    display = ["_"] * len(secret)
    max_wrong = len(secret)
    wrong = 0
    guessed = set()
    hint_used = False

    #   5) Show initial word
    print(f"\nToday's word has {len(secret)} letters.")
    print("Word to guess:", *display, "\n")

    #   6) Main game loop
    while wrong < max_wrong and "_" in display:
        if wrong == max_wrong - 1 and not hint_used:
            rem = max_wrong - wrong
            answer = input(
                f"You have {rem} wrong guess left. "
                "Would you like a hint?"
                "\n(yes/no)"
            ).strip().lower()
            if answer.startswith("y"):
                give_hint(secret, display)
                hint_used = True
            print("\nCurrent word:", *display, "\n")

        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (A-Z).\n")
            continue
        if guess in guessed:
            print(f"Oops! You already guessed '{guess}'.\n")
            continue

        guessed.add(guess)
        if guess in secret:
            for i, ch in enumerate(secret):
                if ch == guess:
                    display[i] = guess
            remaining = display.count("_")
            print("Good guess!")
            print(f"Letters remaining: {remaining}")
        else:
            wrong += 1
            left = max_wrong - wrong
            print(
                f"Sorry, '{guess}' is not in the word. "
                f"{left} wrong guesses left."
            )

        print("Current word:", *display)
        if guessed:
            print("Guessed letters:", *sorted(guessed), "\n")

    #   7) End of the game
    if "_" not in display:
        print("Congratulations! You guessed the word:", secret)
        solved = True
    else:
        print("Oh no! Game over! The word was:", secret)
        solved = False

    #   8) Record this round
    game_history.append({
        "word": secret,
        "solved": solved,
        "wrong_guesses": wrong,
        "total_guesses": len(guessed)
    })

    #   9) Auto-display history
    print("\nGame History:")
    for i, record in enumerate(game_history, 1):
        status = "solved" if record["solved"] else "lost"
        print(
            f"\nGame {i}: '{record['word']}' was {status}, "
            f"{record['wrong_guesses']} wrong guesses out of "
            f"{record['total_guesses']} total guesses."
        )

    #   10) Play again?
    again = input("\nPlay another round? (yes/no): ").strip().lower()
    if not again.startswith("y"):
        print("\nThank you for playing Purple Team's Insanity Word Guesser!")
        break

"""
References:

Fuchs, P., & Poulain, P. (2024, November 13). English common words [Data set]. Retrieved May 25, 2025, from  
https://python.sdv.u-paris.fr/data-files/english-common-words.txt

Horstmann, C. S., & Necaise, R. D. (2016). Python for everyone (2nd ed., Pocket ed.). John Wiley & Sons.

Python Software Foundation. (2025). random — Generate pseudo-random numbers. In Python 3.13.3 Library Reference.
https://docs.python.org/3/library/random.html

Zahmatkesh, H. (2025). Lecture 2 - Programming with numbers and strings [PDF slides]. Kristiania University College.
https://kristiania.instructure.com/courses/12805/files/1541437?module_item_id=528037

Zahmatkesh, H. (2025). Lecture 3 - Decisions [PDF slides]. Kristiania University College.
https://kristiania.instructure.com/courses/12805/files/1549608?module_item_id=533242

Zahmatkesh, H. (2025). Lecture 4 - Loops [PDF slides]. Kristiania University College.
https://kristiania.instructure.com/courses/12805/files/1555668?module_item_id=536006

Zahmatkesh, H. (2025). Lecture 6 - Lists & tuples [PDF slides]. Kristiania University College.
https://kristiania.instructure.com/courses/12805/files/1568739?module_item_id=540168

Zahmatkesh, H. (2025). Lecture 7 - Sets & dictionaries [PDF slides]. Kristiania University College.
https://kristiania.instructure.com/courses/12805/files/1568795?module_item_id=540195

Zahmatkesh, H. (2025). Lecture 8 - Files & exceptions [PDF slides]. Kristiania University College.
https://kristiania.instructure.com/courses/12805/files/1585135?module_item_id=543707
"""
