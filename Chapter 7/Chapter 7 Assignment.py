import random
import math
import turtle

#Exercise 2
def lottery():
    print('Generating lottery numbers...')
    list = []
    
    #Generates the numbers
    for loop in range(9):
        num = random.randint(0, 9)
        list.append(num)
    
    #Prints the numbers
    print('Your lotto numbers are...')
    for printNames in list:
        print(printNames)
    
#---------------------------------------------------------------------------#