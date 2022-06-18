


""" def my_function():
    result = 3*2
    return result
print(my_function()) """


                                                                #code challenge
""" def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "YOu didn't provide valid inputs."
    return f"Result: {f_name.title()} {l_name.title()}"
print(format_name("NITIN",'sharma'))                #or can do it the other way
print(format_name(input("What's your first name? "),input("What's your last name? "))) """

                                                #code challengen 10.1
""" def is_leap(year):
    if year%4==0:
        if year%100!=0 or year%100==0:
            if year%400== 0 or year%400!=0:
                return True 
    else:
        return False
        

def days_in_month(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]   
    if is_leap(year)==False:
        return f"number of days in the month : {month_days[month-1]}"        
    else:
        if month==2:
            days=29                      
            return days
            

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year,month)
print(is_leap(year))
print(days) """

                    #docstrings
                                                            #final coding challenge
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return    n1*n2
def divide(n1,n2):
    return n1/n2

operations = {"+":add,
    "-":subtract,
    "*":multiply,
    "/": divide
    
    
}                    


""" fuction= operations["*"]
print(fuction(2,3)) """

def calculator():
    num1= float(input("What's your first number? "))

    for symbol in operations:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol = input("Pick an operation:  ")
        num2= float(input("What's your next number? " ))

        calculation_function = operations[operation_symbol]
        answer=calculation_function(num1,num2)
                                                                                            
        print(f"{num1} {operation_symbol} {num2}= {answer}")

        """ operation_symbol= input("Pick an operation: ")
        num3= int(input("What's the next number?: "))
        calculation_function=operations[operation_symbol]
        second_answer = calculation_function(calculation_function(num1,num2),num3)
        print(f"{answer} {operation_symbol} {num3}= {second_answer}") """
        choice= input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start again.: ")
        if choice =="y":
            
            num1= answer
        else:
            should_continue=False
            
calculator()





















