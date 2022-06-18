print("hello")
num_char= len("hello")
print(num_char)



def my_func():
    print("hello")
    print("bye")
my_func()



                                                                            #game challenge 
                                                                            #reeborg's world
"""def turnright():
    turnleft()
    turnleft()
    turnleft()
def jump():
    move()
    turnleft()
    move()
    turnright()
    move()
    turnright()
    move()
    turnleft()

for step in range(6):
    jump()

"""             



                                                                        #for loop
                                                                        #again the above code challenge but at this point we'll be using the while loop
"""
nummber_of_hurdles = 6
while number_of_hurdles>0:
    jump()
    number_of_hurdles-=1    #we'll get the output
 """                                                                         
                                                                        #for random flagpost 
"""
while not at_goal():
    jump()
"""            

                                                                            #code challenge
"""
def jump():
    
    turnleft()
    move()
    turnright()
    move()
    turnleft()
    move()
    turnleft()
while not at_goal():
    if fornt_is_clear():
        move()
    if wall_in_front():
        jump()
    
"""                                                                            

                                                                #final hurdle challenge
"""
def jump():
    turnleft()
    while wall_on_right():
        move()
    turnright()
    move()
    turnright()
    while front_is_clear():
        move()
    turnleft()
while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()

"""            

                                                                        #maze- final project
"""

while not at_goal():
     while front_is_clear():
        move()
    turnleft()
    if wall_in_front():
        turnleft()
    if right_is_clear():
        turnright()
        move()    
"""