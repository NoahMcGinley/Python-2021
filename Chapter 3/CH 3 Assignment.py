def day_converter(): #Exercise 1
    userInput = int(input("Enter a day of the week(1-7): "))
    if userInput == 1:
        print('Lunes')
    elif userInput == 2:
        print('Martes')
    elif userInput == 3:
        print('Miercoles')
    elif userInput == 4:
        print('Jueves')
    elif userInput == 5:
        print('Viernes')
    elif userInput == 6:
        print('Sabado')
    elif userInput == 7:
        print('Domingo')
    else:
        print('Error, enter a number 1-7')
        

def roman_numerals(): #Exercise 4
    number = float(input('Enter a number 1-10: '))
    if number == 1:
        print('I')
    elif number == 2:
        print('II')
    elif number == 3:
        print('III')
    elif number == 4:
        print('IV')
    elif number == 5:
        print('V')
    elif number == 6:
        print('VI')
    elif number == 7:
        print('VII')
    elif number == 8:
        print('VIII')
    elif number == 9:
        print('IX')
    elif number == 10:
        print('X')
    else:
        print('Error, enter a number 1-10')
        

def color_mixer(): #Exercise 7
    color1 = input('Enter the first primary color: ')
    color2 = input('Enter the second primary color: ')
    if color1 == 'red' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'red':
        print('Orange')
    elif color1 == 'blue' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'blue':
        print('Green')
    elif color1 == 'blue' and color2 == 'red' or color1 == 'red' and color2 == 'blue':
        print('Purple')
    else:
        print('Error')
        

def hot_dog(): #Exercise 8
    peopleInput = float(input('Enter the number of people attending the party: '))
    hotdogsPerPersonInput = float(input('Enter the number of hotdogs each person will eat: '))
    
    totalHotdogs = hotdogsPerPersonInput * peopleInput
    
    hotdogPackages = totalHotdogs // 10
    hotdogsLeftover = totalHotdogs % 10
    if hotdogsPerPersonInput < 10:
       hotdogPackages += 1
       
    totalbuns = hotdogsPerPersonInput * peopleInput
    
    bunPackages = totalHotdogs // 8
    bunsLeftover = totalHotdogs % 8
    if hotdogsPerPersonInput < 8:
       bunPackages += 1

    print('You need', hotdogPackages, 'packages of hotdogs')
    print('You will have', hotdogsLeftover, 'hotdogs left over')
    
    print('You need', bunPackages, 'packages of buns')
    print('You will have', bunsLeftover, 'buns left over')
    
    
def time_calculator(): #Exercise 15
    seconds = float(input('Enter the number of seconds: '))
    minutes = seconds // 60
    hours = seconds // 3600
    days = seconds // 86400
    if seconds >= 0 and seconds < 60:
        print(seconds, 'seconds')
    elif seconds >= 60 and seconds < 3600:
        seconds = seconds % 60
        print(minutes, 'minutes', seconds, 'seconds')
    elif seconds >= 3600 and seconds < 86400:
        seconds = seconds % 60
        minutes = minutes % 60
        print(hours, 'hours', minutes, 'minutes', seconds, 'seconds')
    elif seconds >= 86400:
        seconds = seconds % 60
        minutes = minutes % 60
        hours = hours % 60
        print(days, 'days', hours, 'hours', minutes, 'minutes', seconds, 'seconds')
    
    
def leap_year(): #Exercise 16
    year = float(input('Enter a year: '))
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(year, 'is a leap year, there are 29 days in the month of Feburuary')
            else:
                print('is not a leap year, there are 28 days in the month of Feburuary')
        else:
            print('is a leap year, there are 29 days in the month of Feburuary')
    else:
        print('is not a leap year, there are 28 days in the month of Feburuary')
            

def sir_fix_alot(): #Exercise 17
    print('Reboot computer and try to connect')
    response1 = str(input('Did that fix the problem?: '))
    if response1 == 'yes':
        print('Netflix and chill')
    else:
        print('Reboot router and try to connect')
        response2 = str(input('Did that fix the problem?: '))
        if response2 == 'yes':
            print('Netflix and chill')
        else:
            print('Verify cables are firmly attached')
            response3 = str(input('Did that fix the problem?: '))
            if response3 == 'yes':
                print('Netflix and chill')
            else:
                print('Move router to a better location')
                response4 = str(input('Did that fix the problem?: '))
                if response4 == 'yes':
                    print('Netflix and chill')
                else:
                    print('Get a new router')

def can_we_just_eat(): #Exercise 18
    vegetarian_status = str(input('Is anyone in your party a vegetarian? (yes/no): '))
    vegan_status = str(input('Is anyone in your party a vegetarian? (yes/no): '))
    gluten_status = str(input('Is anyone in your party a vegetarian? (yes/no): '))
    if vegetarian_status == 'yes' and vegan_status == 'yes' and gluten_status == 'yes': #YYY
        print('Here are your restaurant choices: ')
        print('Corner Cafe')
        print("Chef's Kitchen")
        
    if vegetarian_status == 'no' and vegan_status == 'yes' and gluten_status == 'yes': #NYY
        print('Here are your restaurant choices: ')
        print('Corner Cafe')
        print("Chef's Kitchen")
        
    if vegetarian_status == 'yes' and vegan_status == 'no' and gluten_status == 'no': #YNY
        print('Here are your restaurant choices: ')
        print('Corner Cafe')
        print("Chef's Kitchen")
        print('Main Street Pizza Company')
        
    if vegetarian_status == 'yes' and vegan_status == 'yes' and gluten_status == 'no': #YYN
        print('Here are your restaurant choices: ')
        print('Corner Cafe')
        print("Chef's Kitchen")
        
    if vegetarian_status == 'no' and vegan_status == 'no' and gluten_status == 'no': #NNN
        print('Here are your restaurant choices: ')
        print('Corner Cafe')
        print("Chef's Kitchen")
        print("Joe's Gourmet Burgers")
        print("Mama's fine Italian")
        
    if vegetarian_status == 'yes' and vegan_status == 'no' and gluten_status == 'no': #YNN
        print('Here are your restaurant choices: ')
        print('Corner Cafe')
        print("Chef's Kitchen")
        print("Main Street Pizza Company")
        print("Mama's fine Italian")
        
    if vegetarian_status == 'no' and vegan_status == 'yes' and gluten_status == 'no': #NYN
        print('Here are your restaurant choices: ')
        print('Corner Cafe')
        print("Chef's Kitchen")
        
    if vegetarian_status == 'no' and vegan_status == 'no' and gluten_status == 'yes': #NNY
        print('Here are your restaurant choices: ')
        print('Corner Cafe')
        print("Chef's Kitchen")
        print("Main Street Pizza company")
        
def hit_the_target():
    import turtle

    angle = float(input('Enter the angle: '))
    power = float(input('Enter the power: '))

    #Defines the target
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    TARGET_LLEFT_X = 100
    TARGET_LLEFT_Y = 250
    TARGET_WIDTH = 25
    FORCE_FACTOR = 30
    PROJECTILE_SPEED = 1
    NORTH = 90
    SOUTH = 270
    EAST = 0
    WEST = 180
    
    #Draws the target
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
    turtle.pendown()
    turtle.setheading(EAST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(NORTH)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(WEST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(SOUTH)
    turtle.forward(TARGET_WIDTH)
    turtle.penup()
    turtle.showturtle()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.setheading(angle)
    turtle.forward(power)
    
    
    if (turtle.xcor() >= TARGET_LLEFT_X and
        turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
        #Makes sure the turtle is within the target
        turtle.ycor() >= TARGET_LLEFT_Y and
        turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('The arrow has hit the target!')
    #Gives the user a hint
    if power < 270:
        print('You need more power')
    if power > 300:
        print('You need less power')
    if angle < 60:
        print('You need a greater angle')
    if angle > 80:
        print('You need a lesser angle')