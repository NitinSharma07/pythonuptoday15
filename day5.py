fruits =["apple",'peach','pear']
for fruit in fruits:
    print(fruit)
                                                                #average height exercise
""" student_heights = input("input a list of student heights ").split()
for n in range(0,len(student_heights)):
    student_heights[n]= int(student_heights[n])                                                     
print(student_heights)
total_height = 0
for height in student_heights:
    total_height+=height 
print(total_height)


number_of_students =0
for student in student_heights:

    number_of_students+=1
print(number_of_students)
average_height  = round(total_height/number_of_students,2)
print(average_height)"""


                                                                        #code challenge
""" student_scores = input("Input the list of student scores: ").split()                                 

for n in range(0,len(student_scores)):
    student_scores[n]= int(student_scores[n])
print(student_scores)
highest_score= 0
for score in student_scores:
    if score>highest_score:
        highest_score =score
print(f"the highest score in the class is: {highest_score}") """



for number in range(0,4):
    print(number)

sum= 0
for number in range(1,101):
    sum +=number
print(sum)
                                                        #coding challenge
sum =0                                                        
for number in range(1,101):
    if number%2==0:
        sum+=number
print(sum)


#or


                                                                                    #same coding challenge
sum = 0
for number in range(0,101,2):
    sum+=number
print(sum)


                                                                                #interview coding challenge
for number in range(1,101):
    if number%15==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")                                                                                
    elif number%5==0:
        print("Buzz")
    
    else:
        print(number)

                                                                            #final project
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']                                                                        
symbols = ['!','#','$','%','^','&','*','(',')']
print("welcome to the password generator!")
nr_letters = int(input("how many letters would you like in your password:\n"))
nr_numbers = int(input("how many numbers would you like?\n"))
nr_symbols = int(input("how many symbols would you like?\n"))
#eazy level
""" password =""           

for char in range(1,nr_letters+1):

    random_char = random.choice(letters)
    password+= random.choice(letters)
for char in range(1,nr_symbols+1):
    password+=random.choice(symbols)
for char in range(1,nr_numbers+1):
    password+=random.choice(numbers)
print(password)
 """

#hard level
password_list =[]
for char in range(1,nr_letters+1):

    random_char = random.choice(letters)
    password_list+= random.choice(letters)
for char in range(1,nr_symbols+1):
    password_list+=random.choice(symbols)
for char in range(1,nr_numbers+1):
    password_list+=random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password= ''
for char in password_list:
    password+=char


print(f"your password is: {password}")








    























                                                                          