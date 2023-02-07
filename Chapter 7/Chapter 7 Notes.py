import turtle
import random
import math

#Program 7-1
def salesList():
    #Defines the variables
    numDays = 5
    day = 1
    sales = [] * numDays
    print('Enter the sales for each day')
    
    #Starts the loop
    for loop in range(numDays):
        print('Day #', day, end='', sep='')
        userInput = input(': ')
        day += 1
        sales += userInput
    
    #Prints to the user the values they entered
    print('Here are the values you entered')
    print(sales[0])
    print(sales[1])
    print(sales[2])
    print(sales[3])
    print(sales[4])

#-----------------------------------------------------------------------------#

#Program 7-2
def inList():
    #Defines the part numbers
    list = ['V45', 'VF750', 'VFR1100', 'VTX1300']
    userInput = input('Enter a string to search for: ')
    
    #Determines if the part was found
    if userInput in list:
        print('Part number', userInput, 'was found in the list of part numbers')
    else:
        print('Part number not found')
        
#-----------------------------------------------------------------------------#
        
#Program 7-3
def listAppend():
    start = 'y'
    list = []
    
    #Starts a loop to ask the user for names
    while start == 'y':
        userInput = input('Enter a name: ')
        list.append(userInput)
        start = input('Enter another name?(y/n): ')
    print('You entered the following names')
    
    #Prints the names
    for loop in list:
        print(loop)
        
#-----------------------------------------------------------------------------#

#Program 7-4 (Broken)
def listIndex():
    list = ['Fries', 'Pizza', 'Hotdog']
    userInput = input('Enter the string to search for: ')
    
    if userInput in list:
        newItem = input('Item found. Enter a new food item: ')
        list.insert(userInput, newItem)
    else:
        print(userInput, 'was not found in the list. Check your spelling and try again.')
        
#-----------------------------------------------------------------------------#

#Program 7-5
def listInsert():
    list = ['Bruce', 'Steve', 'Tony']
    print('Here is the list before the insert method', list)
    list.insert(2, 'Sam')
    print('Here is the list after the insert method', list)
    
#-----------------------------------------------------------------------------#

#Program 7-6
def listRemove():
    list = ['Fries', 'Pizza', 'Hotdog']
    userInput = input('Enter the string to search for: ')
    
    if userInput in list:
        list.remove(userInput)
    else:
        print(userInput, 'was not found in the list. Check your spelling and try again.')

    print('Item removed.')
    print('Here is the list', list)
    
#-----------------------------------------------------------------------------#

#Program 7-7
def baristaPay():
    numEmployee = int(input('How many emploeees do you want to calculate pay for?: '))
    employee = 0
    hrs = [0] * numEmployee
    
    for index in range(numEmployee):
        print('Enter the hours worked by employee ', index +1, end='')
        hrs[index] = int(input(': '))
    
    hrlyRate = input('Enter the hourly rate for all employees: ')
    
    for index in range(numEmployee):
        pay = hrs[index] * hrlyRate
        print(pay)
        
#-----------------------------------------------------------------------------#
        
#Program 7-8
def listTotal():
    list = [2, 4, 6, 8, 10]
    total = 0
    index = 0
    for loop in list:
        total += list[index]
        index += 1
    print('The sum of the numbers', list, 'is:', total)
    
    
#Program 7-9
def listAvg():
    list = [2.5, 7.3, 6.5, 4.0, 5.2]
    index = 0
    total = 0
    for loop in list:
        total += list[index]
        index += 1
    avg = total / len(list)
    print('The average of the numbers', list, 'is:', avg)

#-------------------------------------------------------------------------#

#Program 7-10
def listFunction():
    list = [2, 4, 6, 8, 10]
    print('The total is:', getTotal(list))
    
def getTotal(list):
    total = 0
    for loop in list:
        total += loop
    return total

#-------------------------------------------------------------------------#

#Program 7-11
def listReturn():
    print('You entered the numbers: ', getValues())
    
def getValues():
    list = []
    start = 'y'
    while start.lower() == 'y':
        userInput = input('Input a number: ')
        list.append(userInput)
        start = input('Would you like to enter another value? (y/n) ')
    return list
        
#--------------------------------------------------------------------------#
#Program 7-12
def testCalc():
    try:
        start = 'y'
        scores = []
        total = 0
        amt = 0
        
        #Starts the loop which prompts the user for the scores
        while start.lower() == 'y':
            userScores = int(input('Enter a score: '))
            start = input('Enter another score?: ')
            scores.append(userScores)
            total += userScores
            amt += 1
        
        #Sorts then drops the lowest value
        scores.sort()
        drop = scores[0]
        
        #Calculates the average
        average = (total - drop) / amt
        
        #Prints the output
        print('The average score, with', drop, 'dropped from the scores, is:', average)
    
    except Exception as err:
        print('An error has occured, make sure to enter the correct input')

#---------------------------------------------------------------------------------------#

#Program 7-13
def listWriteLines():
    cities = ['Kansas City', 'Lawrence', 'Wichita', 'Manhattan']
    try:
        outfile = open('cities.txt', 'w')
        outfile.writelines(cities)
        print('All data written to cities.txt')
        outfile.close()
    except Exception as err:
        print(err)
        
#---------------------------------------------------------------------------------------#

#Program 7-14
def listWrite():
    cities = ['Kansas City', 'Lawrence', 'Wichita', 'Manhattan']
    try:
        outfile = open('cities.txt', 'w')
        
        for city in cities:
            outfile.write(city + '\n')
            
        print('All data written to cities.txt')
        outfile.close()
        
    except Exception as err:
        print(err)
        
#---------------------------------------------------------------------------------------#

#Program 7-15 (Broken)
def listRead():
    try:
        infile = open('cities.txt', 'r')
        cities = infile.readline()
        infile.close()
    except:
        print('Error reading from the file.')
        
    index = 0
    
    while index < len(cities):
#         cities[index] = cities[index].rstrip('\n')
        index += 1
    print('Here is the information read from cities.txt')
    print(cities)
    
#--------------------------------------------------------------------------------------#

#Program 6-16
def listWriteNumbers():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    outfile = open('numberlist.txt', 'w')
    
    for number in numbers:
        outfile.write(str(number) + '\n')

    outfile.close()
    print('All numbers saved to numberlist.txt')
    
#---------------------------------------------------------------------------------------#

#Program 6-17
def listReadNumbers():
    numbers = []
    try:
        infile = open('numberlist.txt', 'r')
        for num in infile:
            numbers.append(int(num.rstrip('\n')))
        infile.close()
    except Exception as err:
        print(err)
    print('Here is the list created from numberlist.txt:')
    print(numbers)
    
#---------------------------------------------------------------------------------------#
    
# students = [['Joe', 'Kim'],
#             ['Sam', 'Sue'],
#             ['Kelly', 'Chris']]
# print(students[0][0])

def randomNumbers():
    ROWS = 3
    COLS = 4
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    for row in range(ROWS):
        for col in range(COLS):
            values[row][col] = random.randint(1, 100)
    print(values)