import random

word_list = ["apple", "python", "laptop", "school", "mobile"]

secret_word = random.choice(word_list)

guessed = []
chances = 6

print("================================")
print("       HANGMAN GAME")
print("================================")

while chances > 0:

    display = ""

    for letter in secret_word:
        if letter in guessed:
            display = display + letter + " "
        else:
            display = display + "_ "

    print("\nWord :", display)

    if "_" not in display:
        print("\nCongratulations! You Won.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("You already entered this letter.")
        continue

    guessed.append(guess)

    if guess in secret_word:
        print("Correct Guess")
    else:
        chances = chances - 1
        print("Wrong Guess")
        print("Remaining Chances:", chances)

if chances == 0:
    print("\nGame Over!")
    print("Correct Word was:", secret_word)

print("\nThank You For Playing.")