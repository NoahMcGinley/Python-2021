def number_guesser(): #A user has to guess a number 1 - 10, if they get it right, they win
    
    #Takes the user's input
    user_guess = float(input("Enter a number 1-10: "))
    
    #Generates a random number
    number_table = [1,2,3,4,5,6,7,8,9,10]
    import random
    number = (random.choice(number_table))
    
    #Prints the user's score
    if number == user_guess:
        print('You picked the right number!')
    else:
        print('You picked the wrong number!')
        print('The correct number was', number)


def math_quiz():
    
    number_correct = 5
    
    question1 = int(input('What is 5 + 5? '))
    if question1 == 10:
        print("Correct")
    else:
        print('Incorrect')
        number_correct = number_correct - 1
        
    question2 = int(input('What is 10/2? '))
    if question2 == 5:
        print("Correct")
    else:
        print('Incorrect')
        number_correct = number_correct - 1
        
    question3 = int(input('What is 6 * 5? '))
    if question3 == 30:
        print("Correct")
    else:
        print('Incorrect')
        number_correct = number_correct - 1
        
    question4 = int(input('What is 60 / 6? '))
    if question4 == 10:
        print("Correct")
    else:
        print('Incorrect')
        number_correct = number_correct - 1
        
    question5 = int(input('What is 3^2? '))
    if question5 == 9:
        print("Correct")
    else:
        print('Incorrect')
        number_correct = number_correct - 1
    
    print('You got ', number_correct, '/5 questions correct.', sep = '')


    