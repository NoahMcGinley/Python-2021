import random

#Exercise 3
def line_numbers():
    #Opens the file and defines the variables
    try:
        userFile = input('Enter a file to open: ')
        inFile = open(userFile, 'r')
        numcolon = 1
        
        #Starts the loop that reads the file
        for line in inFile:
            amount = str(line)
            amount = amount.rstrip('\n')
            print(numcolon, ': ', end='', sep='')
            print(amount)
            numcolon += 1
        
        #Closes the file
        inFile.close()
    
    #Prints an error if an exception occurs
    except Exception as err:
        print('An error as occured, enter a valid file name')

#---------------------------------------------------------------#

#Exercise 4
def line_counter():
    #Opens the file and defines the variables
    try:
        userFile = input('Enter a file name to read: ')
        inFile = open(userFile, 'r')
        lineAmount = 0
        nameAmount = 0
        
        #Starts the loop to read the file
        for line in inFile:
            lineAmount += 1
            inFileLine = inFile.readline()
            #Detects if a line has data in it
            if inFileLine != '':
                nameAmount += 1
        
        #Prints the results
        print('There are', lineAmount, 'lines of text')
        print('There are', nameAmount, 'lines of content')
        
    except Exception as err:
        print('An error has occured, enter a valid file name')
    
#---------------------------------------------------------------------------#
    
#Exercise 6
def average_of_numbers():
    try:
        #Opens the files and defines the variables
        userFile = input('Enter the name of a file to read: ')
        inFile = open(userFile, 'r')
        total = 0
        lineTotal = 0
        
        #Starts the loop to read the file
        for line in inFile:
            lineAmount = int(line)
            total += lineAmount
            lineTotal += 1
        average = total / lineTotal
        print('There were', lineTotal, 'items with an average value of', average,)
    
    #Catches errors
    except ValueError as valErr:
        print('Invalid characters inside of the file')
    except FileNotFoundError as fileErr:
        print('File not found')

#-----------------------------------------------------------------------------------------#

#Exercise 7
def ran_num_writer():
    #Opens the file
    try:
        userFile = input('Enter the name of the file you want to create: ')
        userNum = int(input('Enter the amount of numbers you want to write to the file: '))
        inFile = open(userFile, 'w')
        
        #Starts the loop to write to the file
        for line in range(userNum):
            ranNum = random.randint(1, 500)
            inFile.write(str(ranNum,))
            inFile.write('\n')
        
        #Confirms that the items have been written to the file
        print('All numbers written to:', userFile)
    except Exception as err:
        print('An error as occured')
    
#-----------------------------------------------------------------------------------------#
    
#Exercise 8
def ran_num_reader():
    try:
        #Defines the variables and opens the file
        userFile = input('Enter a file to read: ')
        inFile = open(userFile, 'r')
        total = 0
        lineTotal = 0
        
        #Starts the loop to read the file
        for line in inFile:
            lineContent = int(line)
            total += lineContent
            lineTotal+= 1
            print(lineContent)
            
        print('The total of the', lineTotal,  'random numbers is:', total)
    except Exception as err:
        print('An error has occured')
    
#------------------------------------------------------------------------------------------#
    
#Exercise 10
def golf_main():
    golf_menu()


#Prompts the user
def golf_menu():
    try:
        print('Welcome to Hole in Twelve golf management system')
        print('Please choose from the following commands...')
        print('1) Read golf data')
        print('2) Append golf data')
        print('3) Exit')
        userChoice = input('Menu choice: ')
        
        if userChoice == '1':
            golf_read()
        if userChoice == '2':
            golf_write()
        if userChoice == '3':
            print('Thank you for using Hole in Twelve golf management system. Have a great day!')
    except Exception as err:
        print('An error has occured')


#Writes to the file
def golf_write():
    #Prevents the program from crashing
    try:
        inFile = open('golf.txt', 'a')
        start = 'y'
        
        #Prompts the user to enter the data
        while start == 'y':
            golfName = input("Golfer's name: ")
            golfScore = input('Score: ')
            inFile.write(golfName)
            inFile.write('\n')
            inFile.write(golfScore)
            inFile.write('\n')
            inFile.write('\n')
            start = input('Add another golfer?(y/n): ')
        
        #Closes the file
        inFile.close()
        
    except Exception as err:
        print('An error has occured')


#Reads the file
def golf_read():
    #Sees if there is an error
    try:
        #Opens the file
        inFile = open('golf.txt', 'r')
        
        #Starts the loop to read the file
        for line in inFile:
            contents = str(line)
            contents = contents.rstrip('\n')
            print(contents)
        
        #Confirms that that the items have been read and closes the file
        print('All records successfully read!')
        inFile.close()
        
    except Exception as err:
        print('An error has occured')

#-------------------------------------------------------------------------------------------------#
        
#Exercise 11
def webpageCreator():
    infile = open('webpage.html', 'w')
    test = '''
    <html>
    <head>
    </head>
    <body>
        <center>
            <hi>Test<hi>
        </center>
        <hr />
        Description
        <hr />
    </body>
    </html>
    '''
    
    #Writes to the file then closes the file
    infile.write(test)
    infile.close()
    
#--------------------------------------------------------------------------------------------------#
    #Exercise 12
def avg_steps():
    inFile = open('steps.txt', 'r')
    daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ['january', 'febuary', 'march', 'april', 'may', 'june',
              'august', 'september', 'october', 'september', 'december']
    
    monthNum = 0
    
    for month in months:
        monthNum += 1
        for days in daysPerMonth:
            contents = inFile.readline()
            contents = contents.rstrip('\n')
            print(month, contents)
            
            
            
            
            
            
# january = daysPerMonth[0]
#     feburary = daysPerMonth[1]
#     march = daysPerMonth[2]
#     april = daysPerMonth[3]
#     may = daysPerMonth[4]
#     june = daysPerMonth[5]
#     july = daysPerMonth[6]
#     august = daysPerMonth[7]
#     september = daysPerMonth[8]
#     october = daysPerMonth[9]
#     november = daysPerMonth[10]
#     december = daysPerMonth[11]       
            
            
            
            
            
            
            
            
            
            
            
#         
#         for febuary in inFile:
#             contents = str(febuary)
#             contents = contents.rstrip('\n')
#             print(contents)
#             
#         for march in inFile:
#             contents = str(febuary)
#             contents = contents.rstrip('\n')
#             print(contents)
# 
#         for april in inFile:
#             contents = str(march)
#             contents = contents.rstrip('\n')
#             print(contents)
#             
#         for may in inFile:
#             contents = str(may)
#             contents = contents.rstrip('\n')
#             print(contents)
#     