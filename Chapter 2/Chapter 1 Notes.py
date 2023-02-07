def comment_example():
    #Comment example recieves no arguments
    #It explains how to create a function header
    #find outputs or return 'hellow world'
    print ("Hello World")
    
def program2_2(): #apostrophe output
    print ('Kate Austen')
    print ('123 Full Circle Drive')
    print ('Asheville, Nc 28899')
    
def program2_3():
    print ("Don't fear!")
    print ("I'm here!")
    
def program2_4(): #display quote
    print ('Your assignment is to read "Hamlet" by tomorrow.')
    
def program2_5(): #This function displays a person's name and address
    print ('Kate Austen')
    print ('123 Full Circle Drive')
    print ('Asheville, Nc 28899')
    
def program2_6():
    #Display the Name
    #Display the address
    #Display the city, state, and ZIP
    print ('Kate Austen')
    print ('123 Full Circle Drive')
    print ('Asheville, Nc 28899')
    
def program2_7(): #variable demo 1
    #This program demonstrates a variable
    room = 503
    print('I am staying in room number')
    print(room)
    
def program2_8():
    top_speed = 160
    Distance = 300
    print('The top speed is')
    print(top_speed)
    print('The distance traveled is')
    print(Distance)
    
def program2_9():
    room = 503
    print('I am staying in room number',room)
    
def program2_10():
    value1 = 2.75
    print('I have' , value1, 'in my account.')
    value1 = 99.95
    print('But now I have' , value1, 'in my account')
    
def program2_11(): #string variable
    first_name = 'Kathryn'
    last_name = 'Marino'
    print(first_name, last_name)
    
def program2_12():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print("Hello" , first_name, last_name)
    
def program2_13():
    name = input('What is your name?: ')
    age = input('What is your age?: ')
    income = float(input('What is your income?: '))
    #Displays the data
    print("Here is the info you entered:")
    print("Name: " , name)
    print("Age: ", age)
    print("Income: ", income)
    
def program2_14():
    salary = int(input('What is your salary?: '))
    bonus = int(input('What is your bonus: '))
    pay = salary + bonus
    print(pay)

def program2_15():
    price = float(input("Enter the item's original price: "))
    discount = price * .2
    sale_price = price - discount
    print('The sale price is: ', sale_price)
    
def program2_16():
    firstscore = float(input("Enter the first test score: "))
    secondscore = float(input("Enter the second test score: "))
    thirdscore = float(input("Enter the third test score: "))
    average = (firstscore + secondscore + thirdscore) / 3
    print('The average score is: ', average)
    
def program2_17():
    inputseconds = float(input("Enter the  number of seconds: "))
    hours = inputseconds // 3600
    minutes = (inputseconds // 60) % 60
    seconds = inputseconds % 60
    print('Here is the time in hours, minutes, and seconds:')
    print('Hours: ' , hours)
    print('Minutes: ' , minutes)
    print('Seconds: ' , seconds)
          
def program2_18():
    futurevalue = float(input('Enter the desired furture value: '))
    interestrate = float(input('Enter the annual interest rate: '))
    numberofyears = float(input('Enter  the number of years the money will grow: '))
    output = futurevalue / (1 + interestrate) ** numberofyears
    print(output)
    
def program2_19():
    amount_due = 5000
    monthly_payment = amount_due / 12
    print("The monthly payment is", monthly_payment)

def program2_20():
    amount_due = 5000
    monthly_payment = amount_due / 12
    print("The monthly payment is",
          format(monthly_payment, '.2f'))

def program2_21():
    monthly_pay = 5000
    annual_pay = monthly_pay / 12
    print('Your annual pay is $',
          format(annual_pay, '.2f'),
          sep='')
    
def program1_22():
    futurevalue = float(input('Enter the desired furture value: '))
    interestrate = float(input('Enter the annual interest rate: '))
    numberofyears = float(input('Enter  the number of years the money will grow: '))
    output = futurevalue / (1 + interestrate) ** numberofyears
    print('You will need to deposit $',
    format(output, sep=''))
    
def program2_22():
    num1 = 127.90
    num2 = 3465.15
    num3 = 3.78
    num4 = 264.82
    num5 = 88.08
    num6 = 800.00
    print (format(num1, '7.2f'))
    print (format(num2, '7.2f'))
    print (format(num3, '7.2f'))
    print (format(num4, '7.2f'))
    print (format(num5, '7.2f'))
    print (format(num6, '7.2f'))
    
import turtle
turtle.dot()
turtle.pencolor("red")
pensize(5)
turtle.circle(100)
turtle.penup()
turtle.pendown()
turtle.hideturtle()


