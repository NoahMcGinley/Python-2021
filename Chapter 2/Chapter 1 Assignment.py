
def personal_info(): #Exercise 1 - Displays personal info
    name = input(str('What is your name?: '))
    address = input(str('What is your address?: '))
    phone_number = input(str('What is your phone number?: '))
    college_major = input(str('What is your projected college major: '))
    print('Name: ', name)
    print('Address: ', address)
    print('Phone Number: ', phone_number)
    print('Projected College Major: ', college_major)
    
    
def total_purchase(): #Exercise 4 - Prints the total cost of an item
    first = float(input('Please enter a price for your first item: '))
    second = float(input('Please enter a price for your second item: '))
    third = float(input('Please enter a price for your third item: '))
    fourth = float(input('Please enter a price for your fourth item: '))
    fifth = float(input('Please enter a price for your fifth item: '))
    subtotal = (first + second + third + fourth + fifth)
    print('Subtotal: $',
    format(subtotal, '.2f'))
    tax = subtotal * .07
    print('Tax:      $',
    format(tax, '.2f'))
    total = tax + subtotal
    print('Total:    $',
    format(total, '.2f'))


def distance_traveled(): #Exercise 5 - Ouputs how far you will travel going a certain speed
    speed = float(input('How fast are you drving?: '))
    distance6 = speed * 6
    distance10 = speed * 10
    distance15 = speed * 15
    print('At', speed, 'miles per hour you will travel', distance6, 'miles in 6 hours.')
    print('At', speed, 'miles per hour you will travel', distance10, 'miles in 10 hours.')
    print('At', speed, 'miles per hour you will travel', distance15, 'miles in 15 hours.')
 
 
def sales_tax(): #Ecercise 6 - Outputs the total tax of an item
    sale_amount = float(input("Enter the sale ammount: "))
    state_tax = sale_amount * .05
    county_tax = sale_amount * .025
    total_tax = state_tax + county_tax
    total_sale = sale_amount + total_tax
    print('Your purchase price was:    $',
    format(total_sale, '.2f'))
    print('Your state tax amount is:   $',
    format(state_tax, '.2f'))
    print('Your county tax amount is:  $',
    format(county_tax, '.2f'))
    print('Your total tax is:          $',
    format(total_tax, '.2f'))
    print('Your total sale is:         $',
    format(total_sale, '.2f'))
    
    
def tip_tax_total(): #Exercise 8 - Outputs the total bill of a meal
    sale_amount = float(input('Please enter the sale amount: '))
    tip = 18
    tax = sale_amount * .07
    bill = sale_amount + tip + tax
    print('The sale was:            $',
    format(sale_amount, '.2f'))
    print('The tip amount is:       $',
    format(tip, '.2f'))
    print('The sales tax amount is: $',
    format(tax, '.2f'))
    print('The total bill is:       $',
    format(bill, '.2f'))


def temp_convertor(): #Exercise 9 - Converts Celsius to Fahrenheit
    celsius = float(input('Please enter the degrees Celsius: '))
    fahrenheit = 9/5 * celsius + 32
    print(celsius, 'degrees celsius is', fahrenheit, 'degrees fahrenheit.')
    
    
def cookie_monster():
    cookie_amount = float(input('How many cookies do you want to make: '))
                          
    sugar_ounces = cookie_amount * .5
    print(
        #Remove round if you want more accuracy with decimals
        round(sugar_ounces // 8), 'cup(s)',
        round(sugar_ounces%8), 'ounces of sugar.'
    )
    
    butter_ounces = cookie_amount * .3333
    print(
        round(butter_ounces // 8), 'cup(s)',
        round(butter_ounces%8), 'ounces of butter.'
    )
    
    flour_ounces = cookie_amount * .9166 
    print(
        round(flour_ounces // 8), 'cup(s)',
        round(flour_ounces%8), 'ounces of flour.'
    )
  
  
def class_demographics():
    female_amount = float(input('Enter the number of females: '))
    male_amount = float(input('Enter the number of males: '))
    
    total = male_amount + female_amount
    
    female_percentage = female_amount / total
    male_percentage = male_amount / total
    
    print(
        'The class consists of',
        format(female_percentage, '.0%'),
        'females and',
        format(male_percentage, '.0%'),
        'males.'
    )
        
    
          
def tortuga_1(): #Exercise 15 - Draws the Oylimpic logo
    import turtle
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    turtle.pencolor('blue')
    turtle.circle(50)
    turtle.penup()
    turtle.goto(-150, -50)
    turtle.pendown()
    turtle.pencolor('yellow')
    turtle.circle(50)
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.circle(50)
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()
    turtle.pencolor('green')
    turtle.circle(50)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pencolor('red')
    turtle.pendown()
    turtle.circle(50)
    
    
def tortuga_2(): #Exercise 15 - Draws a compass
    import turtle
    turtle.penup()
    turtle.goto(0, 200)
    turtle.pendown()
    turtle.goto(0, -200)
    turtle.penup()
    turtle.goto(0, -220)
    turtle.pendown()
    turtle.write('S')
    turtle.penup()
    turtle.goto(200, 0)
    turtle.pendown()
    turtle.goto(-200, 0)
    turtle.penup
    turtle.goto(220, 0)
    turtle.pendown()
    turtle.write('E')
    turtle.penup()
    turtle.goto(-220, 0)
    turtle.pendown()
    turtle.write('W')
    turtle.penup()
    turtle.goto(0, 200)
    turtle.pendown()
    turtle.write('N')
    turtle.penup()
    turtle.goto(100, 100)
    turtle.pendown()
    turtle.goto(-100, -100)
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()
    turtle.goto(100, -100)