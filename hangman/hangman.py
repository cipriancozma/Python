import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
lives = 6
print(logo)
print(f"the solution is {chosen_word}")
display = []
for item in chosen_word:
    display.append("_")

while '_' in display:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")

    for idx in range(len(chosen_word)):
        if chosen_word[idx] == guess:
            display[idx] = guess

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"Your letter is {guess} and it's not in the word. You lose a life")
        if lives == 0:
            print("You lose")
            break

if "_" not in display:
    print("You win")

print(display)