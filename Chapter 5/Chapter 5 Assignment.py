#Imports the packages
import random
import turtle
import math
import my_graphics as gfx


def sales_tax(): #Exercise 2
    userInput()

def userInput():
    
    #Prompts the user for the saleAmmount and calls calculation
    saleAmount = int(input('Enter the sale amount: '))
    
    #Determines if the input is valid
    if saleAmount >= 0:
        calculation(saleAmount)
    else:
        print('Error, enter a valid number')

def calculation(saleAmount):
    
    #Calculates the Tax
    stateTax = saleAmount * .05
    countyTax = saleAmount * .025
    totalTax = stateTax + countyTax
    totalSale = saleAmount + totalTax
    saleOutput(stateTax, countyTax, totalTax, totalSale)
    
def saleOutput(stateTax, countyTax, totalTax, totalSale):
    
    #Prints the output
    print('Your purchase price was: $', totalSale, sep='')
    print('Your state tax ammount is: $', stateTax, sep='')
    print('Your county tax ammount is: $', countyTax, sep='')
    print('Your total tax is: $', totalTax, sep='')
    print('Your total sale is: $', totalSale, sep='')
    
#---------------------------------------------------------------------------------------------#

#Starts the main program, Exercise 6
def calories():
    caloriesInput()

#Takes the carb + fat input from the user
def caloriesInput():
    carbs = int(input('How many grams of carbs did you consume?: '))
    fat = int(input('How many grams of fat did you consume?: '))
    calorieCalc(carbs, fat)

#Caluclates the carb and fat consumption
def calorieCalc(carbs, fat):
    carbCons = carbs * 9
    fatCons = fat * 5
    caloriesOutput(carbCons, fatCons)

#Outputs to the user their results
def caloriesOutput(carbCons, fatCons):
    print('Here is your calorie intake for the day')
    print('You consumed ', carbCons, 'calories worth of carbs today. Nice Work...')
    print('You consumed ', fatCons, 'calories worth of fat today. Nice Work...')
    
#----------------------------------------------------------------------------------------------------------#

#Starts the main program, Exercise 7
def stadium_seating():
    userStadiumInput()

#Takes the input from the user
def userStadiumInput():
    AInput = int(input('Enter the number of class A tickets sold: '))
    BInput = int(input('Enter the number of class B tickets sold: '))
    CInput = int(input('Enter the number of class C tickets sold: '))
    
    #Validates the input
    if AInput >= 0 and BInput >= 0 and CInput >= 0:
        stadiumCalc(AInput, BInput, CInput)
    else:
        print('Error, enter a number greater than 0')
        
#Calculates the total revenue
def stadiumCalc(AInput, BInput, CInput):
    ARevenue = AInput * 20
    BRevenue = BInput * 15
    CRevenue = CInput * 10
    totalRevenue = ARevenue + BRevenue + CRevenue
    
    stadiumOutput(totalRevenue)
    
#Outputs the result
def stadiumOutput(totalRevenue):
    print('The total income sales from tickets is: ', totalRevenue)
    
#----------------------------------------------------------------------------------------------#

#Starts the program, Exercise 8
def paint_estimator():
    paintInput()

#Gets the input from the user
def paintInput():
    paintedInput = int(input('Please enter the total square feet to be painted: '))
    costOfPaint = int(input('How much is each gallon of paint: '))
    if paintedInput and costOfPaint >= 0:
        paintCalc(paintedInput, costOfPaint)

#Calculates the cost of paint
def paintCalc(paintedInput, costOfPaint):
    totalCostOfPaint = (paintedInput / 112) * 10
    totalCostOfPaint = round(totalCostOfPaint, 2)
    laborCost = (paintedInput / 112) * 8 * 35
    totalPaintCost = totalCostOfPaint + laborCost
    paintOutput(paintedInput, totalCostOfPaint, laborCost, totalPaintCost)

#Prints the output to the user
def paintOutput(paintedInput, totalCostOfPaint, laborCost, totalPaintCost):
    print('The cost breakdown to paint', paintedInput, 'square feet is: ')
    print('-----------------------------------------------')
    print('The total cost of paint is: $', totalCostOfPaint)
    print('Total labor cost: $', laborCost)
    print('Total cost of the job is: $', totalPaintCost)
    
#-------------------------------------------------------------------------------------------#

#Starts the program, Exercise 11
def math_quiz():
    getNumbers()

#Calculates the random numbers
def getNumbers():
    num1 = random.randint(1, 200)
    num2 = random.randint(1, 200)
    answer = num1 + num2
    numPrompt(num1, num2, answer)

#Starts the loop and asks the user for their answer
def numPrompt(num1, num2, answer):
    numStart = input('Do want to answer a math problem? (y/n): ')
    
    #Starts the loop which prompts the user to answer the expression
    while numStart == 'y':
        print('What is the solution to this equation' , num1, '+', num2, '?', end='')
        userAnswer = int(input(': '))
        if userAnswer == answer:
            print('Correct')
        else:
            print('Incorrect, the answer is', answer)
        
        #Prompts the user to stat the loop again
        numStart = input('Do you want to answer another probelm? (y/n): ')
        
#--------------------------------------------------------------------------------------------------------------#

#Starts the main program, Exercise 13
def timeLoop():
    secondsInput = int(input('How many seconds do you want the object to fall: '))
    secondsOutput(secondsInput)
   
def secondsOutput(secondsInput):
    seconds = 0
    print('Here is the acceleration of an object  due to gravity for', secondsInput, 'seconds')
    print('-----------------------------------------------------------------------')
    
    #starts the loop that prints the seconds and distance
    for loop in range(secondsInput):
        seconds += 1
        print(seconds, 'sec ', '        ', end='', sep='')
        distance = (9.8 * seconds**2) / 2
        distance = round(distance, 2)
        print(distance, 'm', sep='')
        
#---------------------------------------------------------------------------------------------------------------#

#Starts the game program
def game():
    compChoice()

#Defines the computer's choice
def compChoice():
    compNum = random.randint(1, 5)
    if compNum == 1:
        compInput = 'rock'
    elif compNum == 2:
        compInput = 'paper'
    elif compNum == 3:
        compInput = 'scissors'
    elif compNum == 4:
        compInput = 'lizard'
    elif compNum == 5:
        compInput = 'spock'
    userInput(compInput)

def userInput(compInput):
    #Starts the game
    gameStart = input('Would you like to play?: ')
    
    #Starts the loop
    while gameStart.lower() == 'y':
        compInput = compInput
        
        #Prompts the user for their choice
        userChoice = input('Type your weapon of choice (rock, paper, scissors, lizard, spock): ')
        userChoice = userChoice.lower()
        
        #Calls the main game
        MainGame(compInput, userChoice)
        
        #Asks the user if they would like to play again.
        gameStart = input('Would you like to play again?: ')
            
#Starts the main process
def MainGame(compInput, userChoice): #Tells the user what the computer chose
    print('You choose ... ', userChoice)
    print('The computer chose ... ', compInput)
        
    #Determines the winner from all of the possible inputs
    if compInput == userInput:
        print('You tied!')
            
    elif compInput == 'rock' and userChoice == 'paper':
        gameWin()
            
    elif compInput == 'rock' and userChoice == 'scissors':
        gameLose()
        
    elif compInput == 'rock' and userChoice == 'lizard':
        gameLose()
            
    elif compInput == 'rock' and userChoice == 'spock':
        gameWin()
            
    elif compInput == 'paper' and userChoice == 'rock':
        gameLose()
        
    elif compInput == 'paper' and userChoice == 'scissors':
        gameWin()
        
    elif compInput == 'paper' and userChoice == 'lizard':
        gameWin()
            
    elif compInput == 'paper' and userChoice == 'spock':
        gameLose()
            
    elif compInput == 'scissors' and userChoice == 'rock':
        gameWin()
            
    elif compInput == 'scissors' and userChoice == 'paper':
        gameLose()
        
    elif compInput == 'scissors' and userChoice == 'lizard':
        gameLose()
            
    elif compInput == 'scissors' and userChoice == 'spock':
        gameWin()
            
    elif compInput == 'lizard' and userChoice == 'rock':
        gameWin()
            
    elif compInput == 'lizard' and userChoice == 'paper':
        gameLose()
            
    elif compInput == 'lizard' and userChoice == 'scissors':
        gameWin()
            
    elif compInput == 'lizard' and userChoice == 'spock':
        gameLose()
            
    elif compInput == 'spock' and userChoice == 'rock':
        gameLose()
            
    elif compInput == 'spock' and userChoice == 'paper':
        gameWin()
            
    elif compInput == 'spock' and userChoice == 'scissors':
        gameLose()
        
    elif compInput == 'spock' and userChoice == 'lizard':
        gameWin()
        
    elif userChoice != 'rock' or 'paper' or 'scissors' or 'lizard' or 'spock':
        print('The computer wins! You entered an invalid weapon. Cheater!')

#Tells the user that they have won
def gameWin():
    print('You win!')

#Tells the user that they have lost
def gameLose():
    print('You lose!')
            
#----------------------------------------------------------------------------------------------------------#

#Calls all the functions to draw a snowman
def drawSnowman():
    turtle.hideturtle()
    turtle.speed(0)
    drawBase()
    midSection()
    drawHead()
    drawArms()
    drawFace()
    drawHat()
    turtle.done()

#Draws the base
def drawBase():
    gfx.circle(0, -150, 100, 'blue')

#Draws the midsection
def midSection():
    gfx.circle(0, 25, 75, 'blue')

#Draws the arms
def drawArms():
    #Draws left arm
    gfx.line(-75, 25, -100, 100, 'black')
    gfx.line(-100, 100, -175, 125, 'black')
    gfx.line(-175, 125, -180, 150, 'black')
    gfx.line(-175, 125, -200, 110, 'black')
    
    #Draws right arm
    gfx.line(75, 25, 175, 125, 'black')
    gfx.line(175, 125, 180, 150, 'black')
    gfx.line(175, 125, 200, 110, 'black')

#Draws the head
def drawHead():
    gfx.circle(0, 150, 50, 'blue')

#Draws the face
def drawFace():
    #Draws the mouth and eyes
    gfx.line(-30, 125, 30, 125, 'black')
    gfx.circle(-30, 170, 5, 'black')
    gfx.circle(30, 170, 5, 'black')
    
    #Draws the pipe
    turtle.fillcolor('brown')
    gfx.line(15, 125, 50, 100, 'brown')
    turtle.begin_fill()
    gfx.line(50, 100, 55, 105, 'brown')
    gfx.line(55, 105, 50, 110, 'brown')
    gfx.line(50, 110, 45, 105, 'brown')
    turtle.end_fill()
    
    #Draws the smoke
    gfx.circle(60, 120, 10, 'gray')
    gfx.circle(70, 130, 5, 'gray')
    
def drawHat():
    #Draws the main part
    gfx.square(-40, 200, 75, 'red')
    
    #Draws the brim
    turtle.begin_fill()
    gfx.line(-70, 200, 70, 200, 'red')
    gfx.line(70, 200, 70, 220, 'red')
    gfx.line(70, 220, -70, 220, 'red')
    gfx.line(-70, 220, -70, 200, 'red')
    turtle.end_fill()
    
#-------------------------------------------------------------------------------#

#Exercise 25
def checkerBoard():
    
    #Defines the variables
    XCor = -200
    YCor = -200
    colorNum = 1
    
    #Starts the loop for the columns
    for column in range(5):
        
        #Starts the loop for the rows
        for row in range(5):
            if colorNum % 2:
                color = 'black'
            else:
                color = 'white'
            gfx.square(XCor, YCor, 50, color)
            XCor += 50
            colorNum += 1
        
        #Resets the x variable and increases the y variable
        XCor = -200
        YCor += 50
            
        