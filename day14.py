data = [
    {'name':'Instagram',
    'follower_count': 346,
    'description':'Social media platform',
    'country':"United States"

},
{'name':"Cristiano Ronaldo",
'follower_count':215,
"description":"footballer",
'country':'Portugal'

},
{'name':"Ariana Grande",
'follower_count':183,
"description":"Musician and actress",
'country':'United States'

},
{'name':"Dwayne Johnson",
'follower_count':181,
"description":"Actor and professional wrestler",
'country':'United States'
}
]


import random

""" chance = 0



    

def comparison(answer,winner):
    if answer== winner:
        return 'here you win!'
    else:

    
    element1 = generate()
    
    print("Who does have more followers: ")
    
    
    print(max(a,b))
    
    A=print(f"Compare A: {element1['name']},a {element1['description']}, from {element1['country']}")
    answer_right = True
    while answer_right:
        
        B=print(f"Compare B: {element2['name']},a {element2['description']}, from {element2['country']}")

        answer = input("Tell me who have greater number of followers a or b: ")
        great= greater(a,b)
        
        if answer == great:
            print("good!")
            A = answer
            B= element2
        elif answer!=great:
            print("You lose!")
            answer_right=False


comparison()

 """
winner = {}
chances =1

def generate():
    info = random.choice(data)
    return info

def greater(a,b):
    if a>b:
        return "a" 
    elif b>a:
        return "b"
element1  =generate()

def greater_dictionary(dict1,dict2):
    if dict1['follower_count']>dict2['follower_count']:
        winner= dict1
    elif dict2['follower_count']>dict1['follower_count']:
        winner= dict2
    return winner

answer_right =True
while answer_right:
    print(f"{element1['name'].title()}, a {element1['description']}, from {element1['country']}")
    element2  =generate()
    if element1==element2:
        element2 = generate()
    print(f"{element2['name'].title()}, a {element2['description']}, from {element2['country']}")
    a= element1['follower_count']
    # print(a)
    b= element2['follower_count']
    # print(b)
    
    answer = input("Who do you think does have the greater number of followers(a or b): ")
    if answer == greater(a,b):
        element1 = greater_dictionary(element1,element2)
        chances+=1
    else:
        print(f"you lose! and you used {chances} chance.")
        answer_right =False

    






    
    