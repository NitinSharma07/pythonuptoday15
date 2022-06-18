stages = ['6','5','4','3','2','1']
import random
word_list = ['ardvark',"baboon",'camel']
chosen_word =random.choice(word_list)
print(chosen_word)
lives = 6
display= []
for i in range(len(chosen_word)):
    display+="_" 
print(display)
end_of_game =False
while not end_of_game:
    guess= input("guess a letter! ").lower()
    print(guess)
    if guess in display:
        print(f"you've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter =chosen_word[position]
        if letter ==guess:
            display[position]=guess
    if guess not in chosen_word:
        print(f"you guessed {guess},that's not in the word. You lose a life.")
        lives-= 1
        print(stages[lives])
        
    print(display)
    print(guess)
    
    if lives==0:
        end_of_game=True
        print("you lose!")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game= True
        print("you win!") 
    






    







