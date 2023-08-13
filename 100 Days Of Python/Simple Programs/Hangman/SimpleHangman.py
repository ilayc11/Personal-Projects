import random

import hangman_art
import hangman_words

stages = hangman_art.stages
def checkUnderscore(display):
    if "_" in display:
        return True
    return False

chosen_word=random.choice(hangman_words.word_list)
display=[]
lives=6
print(hangman_art.logo+"\n")
print(f'Pssst, the solution is {chosen_word}.')
for letter in chosen_word:
    display.append("_")
while checkUnderscore(display)==True:
    guess = input("guess a letter\n").lower()
    if guess in display:
        print ("You've already guessed that letter!\n")
    elif guess in chosen_word:
        print("Right")
        for letter,i in zip(chosen_word,range(0,len(chosen_word))):
            if guess == letter:
                display[i]=guess
        print(f"{' '.join(display)}")
    else:
        print("Wrong")
        lives -= 1
        print (stages[lives])
        if lives==0:
            print ("You Lost!")
            break
if lives!=0:
    print ("You Won!")



