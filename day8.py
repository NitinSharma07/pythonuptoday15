""" def greet():
    print("hello")
    print("how are you?")
    print("are you ok")

greet()



def greet_with_name(name):
    print(f"hello {name.title()}")
    print(f"how do you do {name.title()}")


greet_with_name("nitin")
greet_with_name("billie")
 """





""" def greet_with(name,location):
    print(f"My name is {name} and i live in {location} city.")
greet_with("Nitin",'Hamirpur')
greet_with(location="Hamirpur",name='Nitin') """



                                                        #code challlenge
#paint area calculator
""" import math
def paint_calc(height,width,cover): 
    number_of_cans =math.floor((height*width)/cover)
    return (f"number of cans requires will be {number_of_cans}")
test_h = int(input("height of the wall: " )  )                                                        
test_w =int(input("width of the wall : "))
coverage = 5

print(paint_calc(test_h,test_w,coverage)) """

                                                #code challenge 
                                                #prime number checker
""" def prime_checker(number):
    is_prime =True
    for i in range(2,number):
        if number%i==0:
            is_prime= False
    if is_prime:
        print("it is a prime number")
    else:
        print("it is not a prime number.")

            
prime_checker(3)
prime_checker(7)
prime_checker(10)
prime_checker(13)
prime_checker(16)
 """

                                        #final project


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]       

def ceaser(start_text,shift_amount,cipher_direction):
    end_text =""
    if cipher_direction== 'decode':
            shift_amount*=-1
    for char in start_text:
        if char in alphabet:

            position =alphabet.index(char)
            
            new_position =position+shift_amount
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(f"the {cipher_direction}d text is {end_text}")
should_continue =True
while should_continue:                                
    direction =input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("type your message: \n").lower()
    shift =int(input("type the shift number: \n"))
    shift= shift%26


    ceaser(text,shift,direction)
    result= input("type 'yes' if you want to go again. Othewise typw 'no'.\n")
    if result=="no":
        should_continue=False
        print("goodbye!")
        


""" if direction=='decode':
    def decrypt(plain_text,shift_amount):
        cipher_text =""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position- shift_amount
            new_letter= alphabet[new_position]
            cipher_text+= new_letter
        print(f"the decoded text is {cipher_text}")
    decrypt(text,shift)
elif direction=='encode':
    def encrypt(plain_text,shift_amount):
        cipher_text =""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position+ shift_amount
            new_letter= alphabet[new_position]
            cipher_text+= new_letter
        print(f"the incoded text is {cipher_text}")
    encrypt(text,shift) """


    
    
    







