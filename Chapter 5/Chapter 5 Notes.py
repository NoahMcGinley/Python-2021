import turtle
import random
import time
import math


def message(): #Program 5-1
    print("I am Iron Man.")
    

def program5_2_main(): #Program 5-2-main
    print('I am inevitable')
    message()
    print('Only one way to win...')
    
#-------------------------------------------------------------------------------
    
def acme_dryer(): 
        greeting()

def greeting():
    userInput = int(input('Enter a number 0-5: '))
    if userInput > 0 and userInput <= 5:
        
        if userInput == 1:
            step1()
        elif userInput == 2:
            step2()
        elif userInput == 3:
            step3()
        elif userInput == 4:
            step4()
        elif userInput == 5:
            step5()
        elif userInput == 0:
            goodbye()
    else:
        print('Error, enter a number 0-5')
        
def step1():
    print('Unplug the dryer and move it away from the wall.')
    goodbye()

def step2():
    print('Remove the six screws from the back of the dryer')
    goodbye()
    
def step3():
    print('Remove the back panel')
    goodbye()
    
def step4():
    print('Pull the top of the dryer straight up')
    goodbye()
    
def step5():
    print('Pull the front of the dryer off')
    goodbye()
    
def goodbye():
    print('Goodbye')

#---------------------------------------------------------------------#
    
def bad_scope():
    get_name()
    print('Hello', name)
    
def get_name():
    name = input('Enter your name: ')
    
#---------------------------------------------------------------------#
    
def bird_calculator():
    texas()
    kansas()
    
def texas():
    birds = 5000
    print('Texas has', birds, 'birds')
    
def kansas():
    birds = 8000
    print('Kansas has', birds, 'birds')
    
#---------------------------------------------------------------------#
    
def pass_arg():
    value = 5
    show_double(value)
    
def show_double(number):
    result = number * 2
    print(number, '* 2 =', result)
    
#---------------------------------------------------------------------#

def volume_conversion():
    intro()
    userInput = float(input('Please enter the number of cups to convert to ounces: 2'))
    cups_to_ounces(userInput)

def intro():
    print('Welcome to the cups to fluid ounces conversion program.')
    print('For your reference, 1 cup = 8 fluid ounces.')
    
def cups_to_ounces(cups):
    ounces = cups * 8
    print(ounces)
   
#---------------------------------------------------------------------#
    
def show_sum():
    print('The sum of 12 and 45 is ', end = '')
    num1 = 12
    num2 = 45
    sum_of_numbers(num1, num2)
    
def sum_of_numbers(num1, num2):
    sum = num1 + num2
    print(sum)
    
#---------------------------------------------------------------------#
    
def getName():
    firstName = str(input('Please enter your first name: '))
    lastName = str(input('Please enter your last name: '))
    reverse_name(firstName, lastName)
    
def reverse_name(first, last):
    print(last, first)
    
#---------------------------------------------------------------------#
    
def get_value():
    value = 99
    print('I just assigned the variable value: ', value)
    change_me(value)
    print('The value in the function get_value is still: ', value)
    
def change_me(value):
    value = 0
    print('The value in the function change_me has been changed to: ', value)
    
#---------------------------------------------------------------------#
    
def set_args():
    show_interest(rate = 0.01, periods = 10, principal = 10000.0)
    
def show_interest(periods, principal, rate):
    interest = principal * rate * periods
    print('The simple interest will be $', format(interest, '.2f'), sep='')
    
#---------------------------------------------------------------------#
    
my_value = 10 #Global variable

def show_value():
    print('The value of the global variable my_value is', my_value)
    
#---------------------------------------------------------------------#
    
number = 0

def change_global():
    global number
    number = int(input('What do you want to change the global to?: '))
    global_variables_are_bad()
    
def global_variables_are_bad():
    rint('The value of the global variable number was changed in ', end='')
    print('change_global to the value of: ', number)
    
#---------------------------------------------------------------------#
    
CONTRIBUTION_RATE = 0.05

def payMe():
    grossPay = int(input('Enter the amount for gross pay: '))
    bonus = int(input('Enter the amount of bonuses: '))
    showPay(grossPay)
    showBonus(bonus)
    
def showPay(grossPay):
    contribution = grossPay * CONTRIBUTION_RATE
    print('Contribution for gross pay: ', contribution)

def showBonus(bonus):
    contribution = bonus * CONTRIBUTION_RATE
    print('Contribution for bonus pay: ', contribution)
    
#----------------------------------------------------------------------#
    
def random_numbers():
    ranNum = random.randint(1,10)
    print('The random number is: ', ranNum)

def random_numbers2():
    for count in range(5):
        ranNum = random.randint(1, 100)
        print(ranNum)

def random_numbers3():
    for count in range(5):
        print(random.randint(1, 100))
        
#----------------------------------------------------------------------#
        
def dice():
    question = input('Do you want to roll the dice?: ')
    while question == 'y':
        print('Rolling your dice...')
        time.sleep(1)
        ranNum1 = random.randint(1, 6)
        ranNum2 = random.randint(1, 6)
        print('Your two rolls are', ranNum1, 'and', ranNum2)
        question = input('Do you want to roll the dice again?: ')
        
def coin_toss():
    for count in range(10):
        toss = random.randint(1,2)
        if toss == 1:
            print('Heads!')
        else:
            print('Tails!')
            
#-----------------------------------------------------------------------#
     
def total_ages():
    age1 = int(input('Please enter your age: '))
    age2 = int(input('Please enter the age of your best friend: '))
    total = calculate_ages(age1, age2)
    print('\nTogether your are', total, 'years old')
    
def calculate_ages(age1, age2):
    total_ages = age1 + age2
    return total_ages

#-----------------------------------------------------------------------#

DISCOUNT_PERCENT = .2

def sale_price():
    regPrice = get_regular_price()
    get_regular_price()
    salePrice = regPrice - discount(regPrice)
    print(salePrice)
    
def get_regular_price():
    regPrice = int(input('Please enter the regular price of the item: '))
    discount(regPrice)
    
def discount(regPrice):
    discountPrice = regPrice * DISCOUNT_PERCENT
    
#-----------------------------------------------------------------------#

def comissionRate():
    getSales()
    getAdvancedPay()
    
    
def getSales():
    monthlySales = int(input('Please enter the ammount of sales for the month: '))
    determineCommRate(monthlySales)
    
def getAdvancedPay():
    advancedPay = int(input('Please enter any advanced pay you recieved (0 for none): '))
    output(advancedPay)
    
def determineCommRate(monthlySales):
    if monthlySales < 10000:
        commRate = monthlySales * .1
    elif monthlySales < 15000 and monthlySales > 9999:
        commRate = monthlySales * .12
    elif monthlySales < 18000 and monthlySales > 14999:
        commRate = monthlySales * .14
    elif monthlySales < 22000 and monthlySales > 17999:
        commRate = monthlySales * .16
    elif monthlySales >= 22000:
        commRate = monthlySales * .18
    output(commRate, monthlySales)
    
def output(commRate, monthlySales, advancedPay):
    commAmmount = commRate * monthlyAmmount
    total = commAmmount + advancedPay
    print(total)
    
#-----------------------------------------------------------------------------------#

def is_valid(validation):
    if validation > 0:
       return true
    else:
        return false
    
def get_name():
    firstName = input('Please enter your first name: ')
    lastName = input('Please enter your last name: ')
    print(firstName, lastName)

def validate_even(num):
    if (num % 2) == 0:
        return True
    else:
        return False
    
#-------------------------------------------------------------------------------------#
    
def square_root():
    num = int(input('Enter a number: '))
    output = math.sqrt(num)
    print('The square root of the number you entered is', output)
    
def hypotenuse():
    sideA = int(input('Enter the length of side A: '))
    sideB = int(input('Enter the length of side B: '))
    hypotenuse = math.hypot(sideA, sideB)
    print('The hypotenuse of the two entered numbers is: ', hypotenuse)