import random

WORDS = [
    ("python", [
        "It's related to computers.",
        "It's a programming language.",
        "It shares its name with a type of snake.",
        "It starts with 'p' and ends with 'n'.",
    ]),
    ("banana", [
        "It's something you can eat.",
        "It's a fruit.",
        "It's yellow and curved.",
        "Monkeys love it. It starts with 'b'.",
    ]),
    ("guitar", [
        "You can hear it at a concert.",
        "It's a musical instrument.",
        "It has strings and you strum it.",
        "It starts with 'g' and can be acoustic or electric.",
    ]),
    ("planet", [
        "You'd find it in space.",
        "It orbits a star.",
        "Mars and Venus are examples.",
        "It starts with 'p'. Earth is one.",
    ]),
    ("window", [
        "You find it in buildings.",
        "It's made of glass.",
        "You look through it and can open or close it.",
        "It starts with 'w'. It's found in a wall.",
    ]),
]
MAX_WRONG = 6


def show_status(word, hints, guessed, wrong_count):
    
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)

    
    hints_to_show = min(wrong_count + 1, len(hints))
    print("Hints:")
    for i in range(hints_to_show):
        print(f"  {i + 1}. {hints[i]}")

    print("Guessed letters:", " ".join(sorted(guessed)) if guessed else "none")
    print(f"Wrong guesses left: {MAX_WRONG - wrong_count}")


def play():
    word, hints = random.choice(WORDS)
    guessed = []
    wrong_count = 0

    print("=== HANGMAN ===")
    print(f"Guess the {len(word)}-letter word. You can miss {MAX_WRONG} times.")
    print("Each wrong guess unlocks another hint!")

    while wrong_count < MAX_WRONG:
        show_status(word, hints, guessed, wrong_count)

       
        all_found = True
        for letter in word:
            if letter not in guessed:
                all_found = False
        if all_found:
            print(f"\nYou won! The word was '{word}'.")
            return

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed:
            print("You already guessed that letter.")
        elif guess in word:
            guessed.append(guess)
            print("Good guess!")
        else:
            guessed.append(guess)
            wrong_count += 1
            print("Wrong! Here comes another hint...")

    print(f"\nGame over! The word was '{word}'.")


play()