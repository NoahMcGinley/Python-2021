def bug_collecter(): #Exercise 1
    
    #Primes the variables
    bugs = 0
    dayNumber = 1
    
    #Runs the loop
    for days in range(5):
        print('How many bugs did you collect on day' , dayNumber, '?', end='')
        bugs += int(input(': '))
        dayNumber += 1
        if bugs < 0:
            print('Error, do not enter a negative number')
    
    #Prints the total
    print('Great job, you collected', bugs, 
          'bugs, Your the bug master!')
    
#----------------------------------------------------------------------------------------

def distance_traveled(): #Exercise 4
    
    #Prompts the user for their time and speed
    speed = int(input('Enter your speed in MPH: '))
    time = int(input('Enter how long you were driving (in hours): '))
    
    #Prints the heading
    print('Hour            Distance Traveled')
    print('-----------------------------------')
    
    hours = 0
    
    for loop in range(time):
        hours += 1
        distance = hours * speed
        print(hours, '                ', distance)
        
#-----------------------------------------------------------------------------------------
        
def pennies(): #Exercise 7
    
    #Promts the user for the ammount of days
    iterations = int(input('How many days do you want to accure pennies?: '))
    
    #Primes the variable
    pennies = .01
    day = 1
    
    #Prints the heading
    print('Day        Salary')
    print('----------------------')
    
    #Runs the loop
    for loop in range(iterations):
    
        day += 1
        
        pennies *= 2
        print(day, '        ', '$', pennies, sep='')
        
#------------------------------------------------------------------------------
        
def hogwarts_tuition(): #Exercise 10
    
    #Primes the variables
    year = 1
    tuitionCost = 16480
    
    #Prints the heading
    print('Year       Tuition Cost')
    print('-----------------------')
    
    #Runs the loop
    for loop in range(5):
        print(year, '           $', tuitionCost, sep='')
        year += 1
        tuitionCost = tuitionCost + (tuitionCost * .03)
        tuitionCost = round(tuitionCost, 2)

#------------------------------------------------------------------------------
        
def population(): #Exercise 13
            
    #Recieves input from the user
    startingPop = int(input('Enter the starting population: '))
    dailyGrowth = int(input('Enter the percent of daily growth: '))
    daysToRun = int(input('Enter the number of days to simulate: '))
    
    #Primes the variable
    dailyGrowth *= .01
    projectedPop = startingPop
    day = 1
     
    #Prints the heading
    print('Day         Projected Population')
    print('------------------------------------')
    
    #Runs the loop
    for loop in range(daysToRun):
        print(day, '         ', projectedPop)
        day += 1
        projectedPop = projectedPop + (projectedPop * dailyGrowth)
        
#---------------------------------------------------------------------------------
        
def reverse_triangle(): # Exercise 14
      
    # Receives the input from the user
    baseSize = int(input('Enter the base size of the triangle: '))
      
    #Runs the loop
    for loop in range(baseSize):
        print('*', end='')
        baseSize -= 1

        print('*', end='')

#---------------------------------------------------------------------------------
        
def stair_pattern2(): #Exercise 15
    
    #Takes the input
    numSteps = int(input('Enter the number of stairs: '))
    print()
    
    #Runs the loop
    for stairs in range(numSteps):
        for step in range(stairs):
            print(" ", end='')
        print('@')
        
#---------------------------------------------------------------------------------
        
def repeating_squares(): # Exercise 16
     
    # Takes the input from the user
    numSquares = int(input('Enter the number of squares that you want: '))
    
    # Imports the turtle and sets the variables
    import turtle
    turtle.speed(0)
    side = 10
    
    # Runs the loop
    for loop in range(numSquares * 4):
        turtle.setheading(0)
        turtle.forward(side)
        turtle.setheading(90)
        turtle.forward(side)
        turtle.setheading(180)
        turtle.forward(side)
        turtle.setheading(270)
        turtle.forward(side)
        turtle.setheading(0)
         
        # Increases the sides of the square
        side += 5
        
#---------------------------------------------------------------------------------
        
def hypnotic_pattern(): # Exercise 18
     
    #Takes the input from the user
    numSquares = int(input('Enter the ammount of patterns: '))
     
    #Imports turtle and defines variables
    import turtle
    side = 5
    turtle.setheading(0)
    turtle.speed(0)
     
    #Runs the loop
    for loop in range(numSquares):
        
        turtle.forward(side)
        turtle.left(90)
        side += 5
        