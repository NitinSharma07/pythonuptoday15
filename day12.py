""" enemies = 1
print(enemies)
def increase_enemies():
    enemies= 2
    
    print(f'enemies inside function: {enemies}')

increase_enemies()
print(f"enemies outside function: {enemies}")

def drink_potion():
    potion_strength=  2
    print(potion_strength)

drink_potion()

#global scope
player_health = 10
def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

#modifying global scope
enemies = 1
print(enemies)
def increase_enemies():
    global enemies
    enemies+=1
    
    print(f'enemies inside function: {enemies}')

increase_enemies()
print(f"enemies outside function: {enemies}")



                                        #final code challenge
import random                                        
print("Welcome to the Number Guessing Gamae!")                                        
print("I'm thinking of a number between 1 and 100.")
num = random.randint(1,100)
print(num)
level_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
game_over = False
def game():
    guess=  int(input("Make a guess: "))
    attempts-=1
    if guess == num or attempts== 0:
        print("You made the right guess and here you win.")
        game_over= True
    else:
        if guess>num:
            print("It's too high")
            game()
        else:
            print("Too low!")
            game()

    
if level_choice=='easy':
    attempts = 10
    print(f"You have {attempts}  attempts remaining to guess the number. ")
    attempts= 10
    game()
        
elif level_choice=='hard':
    attempts= 5
    game() """

import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0     

def check_answer(guess,answer,turns):
    if guess>answer:
        print("Too high.")
        return turns-1
    elif guess<answer:
        print("Too low!")
        return turns-1
    else:
        print(f"You got it: the answer  is {answer}")


def set_difficulty():
    level = input("Choose a difficulty easy or hard: ")
    if level == "easy":
        
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


           
def game():
    print("Welcome to the guessing game: ")
    print("I'm thinking a number between 1 and 100")
    answer = random.randint(1,100)
    print(answer)
    turns = set_difficulty()
    
    guess = 0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number ")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer,turns)
        if turns==0:
            print("You've run out of guesses, You lose!")
            return
        elif guess != answer:
            print("Guess again")
            
game()







    




    

