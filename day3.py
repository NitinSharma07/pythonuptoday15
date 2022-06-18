""" height = int(input("tell me your height in cm: "))
if height>=120:
    print("you can have the roller coaster ride.")
else:
    print("sorry!you have to grow taller before you have the roller coaster ride") """
                                                                    #code challenge
""" num = int(input("tell me the number i'll tell you if it is odd or even: "))                                                                
if num%2==0:
    print("the given number is even.")
else:
    print("you number is odd.")
 """
                                                                    #code challenge
""" height = int(input("tell me your height in cm: "))
age = int(input("tell me your age: "))
if height>=120:
    if age <12:
        print("your ticket cost will be $5.")
    elif age<=18:
        print("you can have the roller coaster ride and your ticket cost will be $7")
    else:
        print("your ticket cost will be $12.")
else:
    print("sorry!you have to grow taller before you have the roller coaster ride") """

""" height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight/height**2
print(round(bmi,2))
if bmi<18.5:
    print("you are underweight.")
elif bmi>=18.5 and bmi<25:
    print("you have the normal weight.")
elif bmi>=25 and bmi<30:
    print("you are overweight.")
elif bmi>=30 and bmi<35:
    print("you are overweight.")
elif bmi>=35:
    print("you are clinically obese.") """

""" year =int(input("tell me the year, i'll tell you if it is leap or not: "))

if year%100==0 or year%100!=0:
    if year%400==0 or year%400!=0:
        if year%4==0:
            print("it is a leap year")
        else:
            print("it's not a leap year.") """

""" height = int(input("tell me your height in cm: "))
age = int(input("tell me your age: "))
bill =0 
if height>=120:
    if age <12:
        bill =5
        print(f"your ticket cost will be ${bill}.")
    elif age<=18:
        bill = 7
        print(f"you can have the roller coaster ride and your ticket cost will be ${bill}")
    else:
        bill =12
        print(f"your ticket cost will be ${bill}.")
    photo = input("do you want a photo? type Y for yes  or N for no: ")
    if photo =="Y":
        print(f"you have to pay {bill+3}")
    else:
        print("your total bill is {bill}")
else:
    print("sorry!you have to grow taller before you have the roller coaster ride") """



                                                                #code challenge
""" print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S,M or L: ")
add_pepperoni = input("Do you want to add pepperoni? Y or N?: ")
extra_cheese = input("Do you want to add extra cheese? Y or N: ")
if size== "S" or "s":
    bill = 15
    print(f"you bill is ${bill}.")
elif size =="M" :
    bill = 20
    print(f"you bill is ${bill}.")
elif size=="L" :
    bill = 25
    print(f"you bill is ${bill}")
if add_pepperoni =="Y":
    if size=="S":
        topp_cost = 2
        print(f"your pizza cost is ${bill+topp_cost}")
    elif size=="M" or size == "L":
        topp_cost = 3
        print(f"your  pizza cost is ${bill+topp_cost}")
elif add_pepperoni=="N":
    topp_cost =0
    print(f"your pizza cost is ${bill+topp_cost}")
    
if extra_cheese =="Y":
    ec = 1
    if add_pepperoni=="Y":
        print(f"your pizza cost is ${bill+topp_cost+ec}")
else:
    print(f"your final pizza cost is ${bill+topp_cost}") """ 
                                                                        #code challenge
""" height = int(input("tell me your height in cm: "))
age = int(input("tell me your age: "))
bill =0 
if height>=120:
    if age <12:
        bill =5
        print(f"your ticket cost will be ${bill}.")
    elif age<=18:
        bill = 7
        print(f"you can have the roller coaster ride and your ticket cost will be ${bill}")
    elif age>=45 and age<=55:
        print(f"you are going to have the ride at the cost of ${bill}")
    else:
        bill =12
        print(f"your ticket cost will be ${bill}.")
    photo = input("do you want a photo? type Y for yes  or N for no: ")
    if photo =="Y":
        print(f"you have to pay {bill+3}")
    else:
        print("your total bill is {bill}")
else:
    print("sorry!you have to grow taller before you have the roller coaster ride")                                              """                       


                                                                    #code challenge
""" print("welcome to the love calculator")
name1= input("what is your name? \n")
name2= input("what is their name? \n ")
combined_string = name1+name2
lower_case_string = combined_string.lower()
t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")

true = t+r+u+e
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l+o+v+e
lovescore = int(str(true) + str(love))

print(type(lovescore))
if lovescore<10 or lovescore>90:
    print(f"your love score is {lovescore},you go like coke and mentos.")
elif (lovescore>=40) and lovescore<=50:
    print(f"your love score is {lovescore} and you are alright together.")
else:
    print(f"your love score is {lovescore}. ") """
                                                                        #final project
print("Welcome to the treasure island and your mission is to find the treasure.")
direction = input("in which direction do you want to go? left or right: \n")
if direction=="right":
    print("game over") 
else:
    action = input("do you want to swim or wait? \n")
    if action== 'swim':
        print("game over")
    else:
        door = input("to which door do you want to get into? red,blue or yellow: \n")
        if door =='red':
            print("game over")
        elif door =='blue':
            print("game over")
        elif door== 'yellow':
            print("you win!")






   
















    

