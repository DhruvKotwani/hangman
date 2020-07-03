import random
import os

def play_again():
    print("DO YOU WANT TO PLAY THE GAME AGAIN??")
    print("YES or NO")
    answer=input("ENTER YOUR CHOICE=").lower()
    if answer=="y" or answer=="yes":
        play_game()
    elif answer=='n' or answer=='no':
        pass
    else:
        print("ERROR!!! INVALID INPUT")
def get_word():
    print("PLAYER 1")
    word=input("ENTER THE WORD FOR THE OPPONENT=").lower()
    return word
def play_game():
    os.system('cls')
    word=get_word()
    os.system('cls')
    print("PLAYER 2")
    guessed=False
    tries=5
    guessed_letter=[]
    alphabet="abcdefghijklmnopqrstuvwxyz"
    print("THERE ARE {} LETTER IN THE WORD".format(len(word)))
    for i in range(len(word)):
        print("_",end=" ")
    while guessed==False and tries>0:
        print("")
        print("YOU NOW HAVE {} TRIES".format(tries))
        guess=input("enter the letter that you think exists in the word=").lower()
        if guess not in alphabet:
            print("ERROR!! YOU HAVE NOT ENTERED THE VALID LETTER")
        else:
            if len(guess)!=1:
                print("ERROR! YOU MUST ENTER ONLY ONE LETTER")
            elif guess in guessed_letter:
                print("YOU HAVE ALREADY USED THIS LETTER FOR GUESSING TRY ANOTHER LETTER")
            else:
                if guess in word:
                    print("GOOD!!! THE LETTER YOU ENTERED EXISTS IN THE WORD")
                    guessed_letter.append(guess)
                else:
                    print("HARD LUCK!! THE LETTER YOU ENTERED DOES NOT EXISTS IN THE WORD")
                    guessed_letter.append(guess)
                    tries=tries-1
        status=""
        for letter in word:
            if letter in guessed_letter:
                status=status+letter
            else:
                status=status+"_ "
        print(status)
        if status==word:
            print("WELL DONE! YOU HAVE GUESSED THE WORD RIGHT")
            guessed=True
        if tries==0:
            print("HARD LUCK !!!! YOU ARE OUT OF TRIES")
            print("THE WORD WAS '{}'".format(word))
    play_again()
                
play_game()
