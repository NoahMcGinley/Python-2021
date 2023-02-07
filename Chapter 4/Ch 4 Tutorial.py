# counter = 1
# 
# while counter <= 10:
#     print(counter)
#     counter = counter + 1
# print("The loop is done")


def commission():
    keep_going = str(input('Do you want to preform the calculation (y/n): '))
    while keep_going == 'y':
        saleAmount = float(input('Enter the sale amount: '))
        commissionRate = float(input('Enter the commission rate: '))
        commission = saleAmount * commissionRate
        print('The commission is $', commission, sep = '')
        keep_going = str(input('Do you want to preform the calculation (y/n): '))
        
        
        
def temperature():
    maxTemp = 102.5
    tempInput = float(input('Please enter the current substance temperature in degrees celcius: '))
    while tempInput > 102.5:
        print('turn the thermostat down and wait for it to cool')
        print('Then wait 5 seconds and measure again')
        tempInput = float(input('Please enter the current substance temperature in degrees celcius: '))
        
        
def simple_loop1():
    for num in range(1, 11, 2):
        print(num)
        
        
def simple_loop3():
    for name in ['Steve', 'Tony', 'Thor', 'Wands']:
        print(name)
        
        
def while_example():
    counter = 0
    while counter < 5:
        print('Hello World!')
        counter = counter + 1
        

def for_example6():
    total = 0
    for num in range(1, 11):
        total = total + num
        print('The total is', total)

def squares():
    print('Number Square')
    for num in range(1,11):
        print(num,'    ', num ** 2)
        
        
def speed_converter():
    print('KPH/MPH')
    for KPH in range(60, 140, 10):
        MPH = KPH * .6421
        print(KPH, MPH)
        

def user_squares1():
    print('This program will display a list of numbers')
    print('(starting at 1) and their squares.')
    end = int(input('How many squares?'))
    for num in range(1, end):
        square = num ** 2
        print(num, square)
        
def user_squares2():
    print('This program will display a list of numbers')
    print('(starting at 1) and their squares.')
    start = int(input('What is the first square number?: '))
    end = int(input('What is the last square number?: '))
    print('Number', 'Square')
    print('-----------------')
    for num in range(start, end):
        square = num ** 2
        print(num,'      ', square)

def sum_numbers():
    total = 0
    print('This program calculates the sum of 5 numbers you will enter.')
    for num in range(1, 6):
        userInput = int(input('Please enter a number: '))
        total += userInput
    print('The total of your 5 numbers is: ',total)


def property_tax():
    
    propertyTax = .0065
    lot = float(input('Please enter a lot number (enter 0 to end): '))
    while lot != 0:
        value = float(input('Please eter the property value'))
        
        
def concentric_circles():
    num_circles = int(input('Enter the number of circles: '))
    starting_radius = 20
    offset = 10
    animation_speed = 0
    
    import turtle
    
    radius = 20
    
    for circle in range(num_circles):
        turtle.circle(radius)
        
        radius += 10
        
        xcor = turtle.xcor()
        ycor = turtle.ycor()
        
        turtle.penup()
        turtle.goto(xcor, ycor)
        turtle.pendown()
        
        
def spiral_circles():
    numCircles = 36
    radius = 100
    angle = 10
    
    import turtle
    turtle.speed(0)
    
    for x in range(numCircles):
        turtle.circle(radius)
        turtle.left(angle)
        

def starburst():
    startX = -200
    startZ = 0
    numLines = 36
    lineLength = 400
    angle = 170
    
    import turtle
    
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(startX, startZ)
    turtle.pendown()
    
    for x in range(numLines):
        turtle.forward(lineLength)
        turtle.left(angle)
        
    
        

    