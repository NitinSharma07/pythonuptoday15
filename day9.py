                                #coding exercise
from turtle import clear
from winreg import KEY_WOW64_32KEY


""" student_scores= {
    "Harry": 81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}                                
student_grades= {}
for key in student_scores:
    print(key)
    student_score = student_scores[key]
    print(student_score)
    if student_score>=91:
        student_grades[key]= "Outstanding"
    elif student_score>=81 and student_score<=90:
        student_grades[key]="Exceeds Expectations"
    elif student_score>=71 and student_score<=80:
        student_grades[key]="Acceptable"
    elif student_score<=70:
        student_grades[key]= "Fail"
print(student_grades)
for key in student_scores:
    student_scores[key]+=1
print(student_scores) """




                                                            #nesting
                                                            
""" capitals = {
    "France":"Paris",
    "Germany":"Berlin"
}                                                            
print(capitals)
travel_log = {
    "France": ["Paris","Lille",'"Dijon'],
    "Germany":['Berlin',"Hanburg","Stutgart"]
}
print(travel_log)

travel_log = {
    "France": {"cities_visited":["Paris","Lille",'"Dijon'],"total_visits":12},
    "Germany":{"cities_visited":['Berlin',"Hanburg","Stutgart"],"total_visits":32}
}
print(travel_log)


travel_log= [
    {"country":"France","cities_visited":["Paris","Lille",'"Dijon'],"total_visits":12},
    {"country":"Germany","cities_visited":["Paris","Lille",'"Dijon'],"total_visits":32}
]

for travel in travel_log:
    for key in travel:
        print(f"{key}:{travel[key]}")


def add_new_country(country,cities_visited,total_visits):
    new_country = {"country":country,'cities_visited':cities_visited,"total_visits":total_visits}
    travel_log.append(new_country)
    print(f"you've visited {country} {total_visits} times. ")
    print(travel_log)
add_new_country("Russia",['Moscow','Saint Petersburg'],2)



                                                            #day challenge
                                                            #here i did a mistake aur bht vahiyad code likha meine

print("welcome to secret auction program.")
name= input("What is your name: ")                                                            
price = int(input("What is your bid: $"))
go_on = input("Do you want to continue(Yes or No): ")
auctions =[]
bidfinish =False
while bidfinish:
    auction = {}
    auction['name']= name
    auction['bid']= bid
    auctions.append(auction)
if go_on=="No" :
    bidfinish= True
    for i in range(len(auctions)):
        maxi = max(auctions[i]['bid'])"""


bids ={}
bidding_finish =False


def find_highest_bidder(bidding_record):
    highest_bid= 0
    winner = ""
    for bidder in bidding_record:
        bid_amount= bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid= bid_amount
            winner =bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not  bidding_finish:
    name =input("What's your name? ")
    prices = int(input("What's your bid? $"))
    bids[name] =prices
    should_continue = input("Are there any other bidders? Type yes or No: ")
    if should_continue=="no":
        bidding_finish= True
        find_highest_bidder(bids)
    elif should_continue=="yes":
        clear()  









    





