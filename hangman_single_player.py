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
    words=['dhruv','aakash','kewal','divya','kotwani']
    return random.choice(words)

def play_game():
    word=get_word()
    guessed=False
    tries=10
    guessed_letter=[]
    alphabet="abcdefghijklmnopqrstuvwxyz"
    print("THERE ARE {} LETTER IN THE WORD".format(len(word)))
    for i in range(len(word)):
        print("_",end=" ")
    while guessed==False and tries>0:
        os.system("cls")
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
