import random
random_int = random.randint(1,10)
print(random_int)

import my_moduleday4
print(my_moduleday4.pi)

random_float =random.random()
print(random_float)


print(random_float*5)

love_score = random.randint(1,100)
print(f"your love score is {love_score}")
                                                                    #code challenge
import random
coin = random.randint(0,1)
if coin ==1:
    print("head")
else:
    print("tail")

statesofamerica = ['delware','pennsylvania']
print(statesofamerica[0])
statesofamerica[1]='pencilcania'
print(statesofamerica)


statesofamerica.append('angelaland')
print(statesofamerica)

statesofamerica.extend(['angela land','jack bauer land'])
print(statesofamerica)

                                                                        #code challenge
""" names = input("Give me everybody's name separated by a comma: ")
list = names.split(", ")
payer = random.randint(0,len(list)-1)
print(f"{list[payer].title()} is going to buy the meal today {list[payer]}") """

#nested list



                                                                        #code challenge

""" row1= ['p','p','p']                                                                        
row2= ['p','p','p']
row3= ['p','p','p']
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
i= int(input("tell me the horizontal coordinate:"))
j=int(input("tell me the vertical coordinate: "))
map[i-1][j-1] = 'x'
print(f"{row1}\n{row2}\n{row3}") """

                                                                #final project   fucking amazing

game = ['rock','paper','scissors']                                                            
me= int(input("tell me your input, 0 for rock,1 for paper, 2 for scissors: "))
if me >2 or me<0:
    print("you typed an invalid number  and here you lose!")


else:
    print(game[me])
    logic = random.randint(0,2)
    print(f"computer:  {game[logic]}")


    if me == logic:
        print("draw!")
    elif me== 0 and logic== 2:
        print("you won computer lose! ")
    elif logic== 0 and me== 2:
        print("computer won and you lose!")
    elif me<logic:
        print("you lose!")
    elif me>logic:
        print("you won!")





























