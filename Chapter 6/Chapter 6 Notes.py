import os


def example():
    #open a file named solocups.txt
    #file_object = open('filename.exe', 'r')

    outfile = open('solocups.txt', 'w')
    #write something to the
    
    outfile.write('2')
    print('All information saved to solocups.txt')
    outfile.close()


#Program 6-1
def fileWrite():
    
    #Opens the file
    fileWritefile = open('lotr.txt', 'w')
    
    #Writes to the file
    fileWritefile.write('Frodo Baggins\n')
    fileWritefile.write('Gandalf\n')
    fileWritefile.write('Aragorn\n')
    
    print('All info saved to lotr.txt')
    fileWritefile.close()


#Program 6-2
def fileRead():
    #Opens the file
    fileRead = open('lotr.txt', 'r')
    
    #Defines the contents
    contents = fileRead.read()
    
    #Closes the file and prints the contents
    fileRead.close()
    print(contents)
    print('All information read')
    
    
#Program 6-3
def fileRead2():
    #Opens the file
    fileRead = open('lotr.txt', 'r')
    
    #Defines the contents
    line1 = fileRead.readline()
    line2 = fileRead.readline()
    line3 = fileRead.readline()
    
    #Closes the file and prints the contents
    fileRead.close()
    print(line1)
    print(line2)
    print(line3)
    print('All information read...')
    
#Program 6-4   
def writeNames():
    #Prompts the user for their friends
    print('Please enter the names of three friends.')
    name1 = str(input('Friend 1: '))
    name2 = str(input('Friend 2: '))
    name3 = str(input('Friend 3: '))
    
    #Writes the names to a file
    nameFile = open('NameOfFriends.txt', 'w')
    nameFile.write(name1 + '\n')
    nameFile.write(name2 + '\n')
    nameFile.write(name3 + '\n')
    
    
def stripNewLine():
    fileRead = open('lotr.txt', 'r')
    
    #Defines the contents
    line1 = fileRead.readline()
    line2 = fileRead.readline()
    line3 = fileRead.readline()
    
    #Strips the \n
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    
    #Closes the file and prints the contents
    fileRead.close()
    print(line1)
    print(line2)
    print(line3)
    
    
#Program 6-5
def writeNames2():
    #Prompts the user for their friends
    print('Please enter the names of three friends.')
    name1 = str(input('Friend 1: '))
    name2 = str(input('Friend 2: '))
    name3 = str(input('Friend 3: '))
    
    #Writes the names to a file
    nameFile = open('NameOfFriends.txt', 'a')
    nameFile.write(name1 + '\n')
    nameFile.write(name2 + '\n')
    nameFile.write(name3 + '\n')
    

#Program 6-6
def writeNumbers():
    num1 = int(input('Please enter a number: '))
    num2 = int(input('Please enter a number: '))
    num3 = int(input('Please enter a number: '))
    
    infile = open('numbers.txt', 'w')
    
    infile.write(str(num1 + '\n'))
    infile.write(str(num2 + '\n'))
    infile.write(str(num3 + '\n'))
    
    
def readNumbers():
    outfile = open('numbers.txt', 'r')
    
    line1 = int(outfile.readline())
    line2 = int(outfile.readline())
    line3 = int(outfile.readline())

    outfile.close()
    
    print(line1)
    print(line2)
    print(line3)


#Program 6-8
def writeSales():
    #Takes input from the user
    numDays = int(input('How many days do you want to enter sales for? '))
    
    #Opens the file
    numFile = open('sales.txt', 'w')
    
    #Starts the loop
    for day in range(1, numDays + 1):
        sales = float(input('Enter the sales for day #' + str(day) + ': '))
        numFile.write(str(sales) + '\n')
    
    #Closes the file and outputs to the user that the data has been saved
    numFile.close()
    print('All data has been saved to sales.txt.')
    

#Program 6-9
def readSales():
    numFile = open('sales.txt', 'r')
    line = numFile.readline()
    
    while line != '':
        ammount = float(line)
        print(format(ammount, ',.2f'))
        line = numFile.readline()
        
    numFile.close()
    
#Might be broken
def readSales2():
    numFile = open('sales.txt', 'r')
    
    for line in numFile:
        amount = float(line)
        print(format(amount, ',.2f'))

    numFile.close()
    
    
#Program 6-11
def writeVideoTime():
    numVids = int(input('How many videos are in the project?: '))
    videoTimes = open('video_times.txt', 'w')
    
    for loop in range(1, numVids + 1):
        length = float(input('Enter the sales for day #' + str(loop) + ': '))
        videoTimes.write(str(length) + '\n')
    
    videoTimes.close()
    print('The times have been saved to video_times.txt')
    

#Program 6-12
def readVideoTimes():
    videoTimes = open('video_times.txt', 'r')
    total = 0
    counter = 0
    
    #Starts the loop to read all the lines
    for time in videoTimes:
        runningTime = float(time.rstrip('\n'))
        print('Video #' + str(counter) + ' time:', runningTime, 'seconds')
        counter += 1
        total += runningTime
        
    print('The total running time of all videos is: ', total, 'seconds')

#Program 6-13
def saveEmpRecords():
    numEmploy = int(input('How many employee records are there?: '))
    employee = open('employees.txt', 'w')
    
    for loop in range(1, numEmploy + 1):
        print('Enter data for employee #', str(loop) + ' :')
        name = input('Name: ')
        idNum = input('Id_Num: ')
        department = input('Department: ')
        
        employee.write(name + '\n')
        employee.write(idNum + '\n')
        employee.write(department + '\n')
        
#Program 6-14       
def readEmpRecords():
    employee = open('employees.txt', 'r')
    
    count = 1
    name = employee.readline()
    
    while name != '':
        idNum = employee.readline()
        department = employee.readline()
        
        name = name.rstrip('\n')
        idNum = idNum.rstrip('\n')
        department = department.rstrip('\n')
        
        print('\nRecord for employee #' + str(count))
        print('Name:', name)
        print('ID Number:', idNum)
        print('Department:', department)
        
        name = employee.readline()
        count += 1

    employee.close()
    
    print('\n' + str(count-1), 'records retrieved.')
    
#Program 6-15    
def writeCoffee():
    another = 'y'
    coffeeFile = open('coffee.txt', 'a')
    
    while another.lower() == 'y':
        print('Enter the following coffee data: \n')
        desc = input('Description: ')
        pounds = input('Quantity (in pounds): ')
        
        coffeeFile.write(desc + '\n')
        coffeeFile.write(pounds + '\n')
        
        another = input('\nDo you wish to enter another coffee?(y to continue): ')
        
    coffeeFile.close()
    print('\nAll data appended to coffee.txt.')
        
#Program 6-16
def readCoffee():
    
    #Opens the file
    coffeeFile = open('coffee.txt', 'r')
    desc = coffeeFile.readline()
    
    #Starts the loop to read the txt
    while desc != '':
        pounds = coffeeFile.readline()
        desc = desc.rstrip('\n')
        pounds = pounds.rstrip('\n')
        
        print('\nDescription:', desc)
        print('Quantity (in pounds):', pounds)
        
        desc = coffeeFile.readline()
    
    #Closes the file
    coffeeFile.close()
    print('\nAll records retrieved.')
    

#Program 17
def searchCoffee():
    found = False
    
    search = input('Enter a coffee description to search for: ')
    
    coffeeFile = open('coffee.txt', 'r')
    
    desc = coffeeFile.readline()
    
    while desc != '':
        pounds = coffeeFile.readline()
        
        desc = desc.rstrip('\n')
        
        if desc.lower() == search.lower():
            print('\nRecord found!\n')
            print('Description:', desc)
            print('Quantity (in pounds):', pounds)
            found = True
            
        desc = coffeeFile.readline()
        
    coffeeFile.close()
    
    if not found:
        print('\nThe record was not found.')
        

#Program 18
def modifyCoffee():
    found = False
    
    search = input('Enter the coffee description to modify: ')
    newQty = input('Enter the new quantity: ')
    
    coffeeFile = open('coffee.txt', 'r')
    tempFile = open('temp.txt', 'w')
    
    desc = coffeeFile.readline()
    
    while desc != '':
        qty = coffeeFile.readline()
        
        desc = desc.rstrip('\n')
        qty = qty.rstrip('\n')
        
        if search.lower() == desc.lower():
            
            tempFile.write(desc + '\n')
            tempFile.write(qty + '\n')
            found = True
            
        else:
            tempFile.write(desc + '\n')
            tempFile.write(qty + '\n')
            
        desc = coffeeFile.readline()
        
    coffeeFile.close()
    tempFile.close()
    
    os.remove('coffee.txt')
    
    os.rename('temp.txt', 'coffee.txt')
    
    if found == False:
        print('\nRecord not found.')
    else:
        print('The quantity for', search, 'has been updated to', newQty, 'pounds.')
        
#Program 19
def coffeeDelete():
    found = False
    
    search = input('Enter the coffee description to modify: ')
    newQty = input('Enter the new quantity: ')
    
    coffeeFile = open('coffee.txt', 'r')
    tempFile = open('temp.txt', 'w')
    
    desc = coffeeFile.readline()
    
    while desc != '':
        qty = coffeeFile.readline()
        
        desc = desc.rstrip('\n')
        qty = qty.rstrip('\n')
        
        if search.lower() != desc.lower():
            
            tempFile.write(desc + '\n')
            tempFile.write(qty + '\n')
            
        else:
            found = True
            
        desc = coffeeFile.readline()
        
    coffeeFile.close()
    tempFile.close()
    
    os.remove('coffee.txt')
    
    os.rename('temp.txt', 'coffee.txt')
    
    if found == False:
        print('\nRecord not found.')
    else:
        print('The quantity for', search, 'has been updated to', newQty, 'pounds.')
        
#-----------------------------------------------------------------------------------------------------------------------------#


def coffeeShop():
    coffeeShopMenu()
    
def coffeeShopMenu():
    print('Welcome to Caffeine Overload Inventory Control System. Please choose an inventory option')
    print('1) Add a record')
    print('2) Modify a record')
    print('3) Delete a record')
    print('4) Display all saved records')
    print('5) Exit')
    userInput = input('Inventory option:')
    
    if userInput == '1':
        addRecord()
    
    if userInput == '2':
        modifyRecord()
    
    if userInput == '3':
        deleteRecord()
    
    if userInput == '4':
        displayRecord()
    
    if userInput == '5':
        exit()
        
def addRecord():
    coffeeShopFile = open('coffeeShop.txt', 'a')
    another = 'y'
    
    while another.lower() == 'y':
        print('Enter the following coffee data: \n')
        desc = input('Description: ')
        pounds = input('Quantity (in pounds): ')
        
        coffeeShopFile.write(desc + '\n')
        coffeeShopFile.write(pounds + '\n')
        
        another = input('\nDo you wish to enter another coffee?(y to continue): ')
        
    coffeeShopFile.close()
    print('\nAll data appended to coffee.txt.')
    

def modifyRecord():
    found = False
    
    search = input('Enter the coffee description to modify: ')
    newQty = input('Enter the new quantity: ')
    
    coffeeShopFile = open('coffeeShop.txt', 'r')
    tempFile = open('temp.txt', 'w')
    
    desc = coffeeShopFile.readline()
    
    while desc != '':
        qty = coffeeShopFile.readline()
        
        desc = desc.rstrip('\n')
        qty = qty.rstrip('\n')
        
        if search.lower() == desc.lower():
            
            tempFile.write(desc + '\n')
            tempFile.write(qty + '\n')
            found = True
            
        else:
            tempFile.write(desc + '\n')
            tempFile.write(qty + '\n')
            
        desc = coffeeShopFile.readline()
        
    coffeeShopFile.close()
    tempFile.close()
    
    os.remove('coffeeShop.txt')
    
    os.rename('temp.txt', 'coffeeShop.txt')
    
    if found == False:
        print('\nRecord not found.')
    else:
        print('The quantity for', search, 'has been updated to', newQty, 'pounds.')
        
        
def deleteRecord():
    found = False
    
    search = input('Enter the coffee description to modify: ')
    newQty = input('Enter the new quantity: ')
    
    coffeeShopFile = open('coffeeShop.txt', 'r')
    tempFile = open('temp.txt', 'w')
    
    desc = coffeeShopFile.readline()
    
    while desc != '':
        qty = coffeeShopFile.readline()
        
        desc = desc.rstrip('\n')
        qty = qty.rstrip('\n')
        
        if search.lower() != desc.lower():
            
            tempFile.write(desc + '\n')
            tempFile.write(qty + '\n')
            
        else:
            found = True
        desc = coffeeShopFile.readline()
        
    coffeeShopFile.close()
    tempFile.close()
    
    os.remove('coffeeShop.txt')
    
    os.rename('temp.txt', 'coffeeShop.txt')
    
    if found == False:
        print('\nRecord not found.')
    else:
        print('The quantity for', search, 'has been updated to', newQty, 'pounds.')
    


#---------------------------------------------------------------------------------------#

#Program 6-21
def division():
    
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a seconds number: '))
    
    if num2 != 0:
        result = num1 / num2
        print(num1, 'divided by', num2, 'is', result)
    else:
        print('Cannot divide by 0.')
        

#Program 6-22
def grossPay1():
    hours = int(input('Enter the number of hours worked: '))
    rate = float(input('Enter the pay rate: '))
        
    pay = hours * rate
        
    print('Gross pay: $', format(pay, ',.2f'), sep='')
    
    
#Program 6-23
def grossPay2():
    try:
        hours = int(input('Enter the number of hours worked: '))
        rate = float(input('Enter the pay rate: '))
            
        pay = hours * rate
            
        print('Gross pay: $', format(pay, ',.2f'), sep='')
        
    except Exception as err:
        print('An error as occured')

def displayFile1():
    filename = input('Enter a filename to open: ')
    infile = open(filename, 'r')
    contents = infile.read()
    print(contents)
    infile.close()


#Program 6-24
def displayFile2():
    try:
        #Inputs to the user to open a file
        filename = input('Enter a filename to open: ')
        infile = open(filename, 'r')
        
        contents = infile.read()
        print(contents)
        infile.close()
        
    except IOError as err:
        print('File does not exist')


def writeFile():
    infile = open('salesData.txt', 'w')
    infile.write('1')


#Program 6-25
def salesReport1():
    infile = open('salesData.txt', 'r')
    readline = infile.readline()
    while readline != '':
        qty = infile.readline()
    print(qty)
    infile.close()
    
    