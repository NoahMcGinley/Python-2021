def test_average():
    first_score = int(input('Enter the first score: '))
    second_score  = int(input('Enter the second score: '))
    third_score = int(input('Enter the third score: '))
    average = (first_score + second_score + third_score) / 3
    print('The average score is: ',
    format(average, '.2f'))
    if average >= 95:
        print('Congratulations')
        print('That is a high score!')
    else:
        print('Study harder!')
        
        
def program3_2():
    hours_worked = int(input('Enter the number of hours worked: '))
    hourly_wage = int(input('Enter the hourly pay rate: '))
    
    if hours_worked > 40:
        gross_pay = hours_worked * hourly_wage
        
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_wage * 1.5
        print('You have earned an overtime salary of: $', overtime_pay + gross_pay)
    else:
        gross_pay = hours_worked * hourly_wage
        print('You have earned: $', gross_pay)
        
        
def password_verifier():
    user_input = string(input('Enter the password: '))
    if user_input == 'prospero':
        print('Password accepted')
    else:
        print('password is invalid')
        
        
def program3_4():
    firstName = input("Enter the first name (last, first): ")
    secondName = input("Enter the second name (last, first): ")
    
    print('Here are the names, sorted alphabetically')
    
    if firstName > secondName:
        print(firstName)
        print(secondName)
    else:
        print(secondName)
        print(firstName)
        
        
def program3_5():
    salary = float(input('Enter your salary: '))
    if salary >= 30000:
        years_on_job = float(input('Enter the ammount of years on the job: '))
        if years_on_job >= 2:
            print('You qualify for the loan')
        else:
            print('You must have been on your current job for at least two years to qualify.')
    else:
        print('You must earn at least $30,000 per year to qualify'),
        
                        
def grader():
    testScore = float(input('Enter your test score'))
    if testScore >= 90:
        print('Your grade is A.')
    else:
        if testscore >= 80:
            print('Your grade is B.')
        else:
             if testscore >= 70:
                print('Your grade is c.')
             else:
                if testscore >= 60:
                    print('Your grade is D.')
                
                      
def graderv2():
    testScore = float(input('Enter your test score'))
    if testScore >= 90:
        print('Your grade is A.')
    else:
        if testscore >= 80:
            print('Your grade is B.')
        else:
             if testscore >= 70:
                print('Your grade is c.')
             else:
                if testscore >= 60:
                    print('Your grade is D.')
                
               
def loan_qualifer_v2():
    salary = float(input('Enter your salary: '))
    years_on_job = float(input('Enter the ammount of years on the job: '))
    if salary >= 30000 and years_on_job >= 2:
        print('You qualify for the loan.')
    else:
        print('You do not qualify for the loan.')
        
                        
def loan_qualifer_v3():
    salary = float(input('Enter your salary: '))
    years_on_job = float(input('Enter the ammount of years on the job: '))
    if salary >= 30000 or years_on_job >= 2:
        print('You qualify for the loan.')
    else:
        print('You do not qualify for the loan.')
        
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
