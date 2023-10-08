import random
import os
import hangman_art
import hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(hangman_art.logo)

#Create blanks
display = []
for letter in range(word_length):
    display.append("_") #can also do display += '_'

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    
    if guess in display:
        print(f"You have already guessed {guess}.")

    #Check guessed letter
    for position in range(word_length):
        # correct_letter = chosen_word.find(guess, letter, letter + 1)
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    
    if guess not in chosen_word:
        print("That letter is not in the word. You lose a life.")
        lives -= 1
        print(hangman_art.stages[lives])
    
    #Join all the elements in the list and turn it into a String and display the hangman.
    print(f"{' '.join(display)}")
    
    #Check if user has got all letters or lost game.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif lives == 0:
        end_of_game = True
        print(f"The word was {chosen_word}")
        print("You lose.")
        os.system('pause')