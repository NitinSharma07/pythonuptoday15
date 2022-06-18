print(len("hello"))
print("hello"[0])    #subscript
print("hello"[-4])


""" num_char  = len(input("what is your name?"))
print("your name has " + str(num_char) + " characters.")          #or


num_char  = len(input("what is your name?"))
new_num_char = str(num_char)
print("your name has " + new_num_char + " characters.")
 """



a= 123
print(type(a))


print(70 + float("100.5"))      #here we are converting a string 100.5 into the float number and then adding it to the integer
print(str(70) + str(100.5))     #here it will convert this int and float statement into str and going to give you the string


                                                        #project
""" num =input("tell me the two digit  number: ")
print(type(num))

print(int(num[0]) + int(num[1])) """

                                                            #project2
""" height  = (input("tell me your height in meters: "))
weight = (input("tell me your weight in kg: "))                 

print(type(height))
print(type(weight))

bmi = float(weight)/float(height)**2
print(int(bmi)) """

#rounding off the numbers
print(round(8/3))
(round(8/3,2))




result = 3/2
result/=2
print(result)


#using f string
score =0 
height = 1.8
pp = True
print(f"yourscore is {score} and your height is {height} and you are winning is {pp}")



                                                    #project
""" age  =  input("what is your current age: ")
age = int(age)
month = 90*12-age*12
days = 90*365- age*365
weeks = 90*52 - age*52
print(f"you have {month} month, {days}days and {weeks}weeks left ")    """                                         

                                                        #day 2 final project
print("welcome to the tip calculator.")                                                        
totalbill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12 or 15?"))
split = int(input("how many people to split the bill? "))
print(f"each person should pay: {round((totalbill+tip%totalbill)/split,2)}")




