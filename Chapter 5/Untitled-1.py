
import random

def diceRoller():
    
    AISpot = 0
    UserSpot = 0
    
    start = str(input('Would you like to play the game?: '))
    if start == 'y':
        
        rollAgain = input('Would you like to roll?: ')
        
        while rollAgain == 'y':
            AIRoll = random.randint(2, 13)
            UserRoll = random.randint(2, 13)

            AISpot += AIRoll
            UserSpot += UserRoll

            print('You rolled a', UserRoll, 'Your position is now at ', UserSpot)
            print('The AI rolled a', AIRoll, "The AI's posistion is now at ", AISpot, "\n")

            if AISpot >= 100:
                print('You lose!')
                break

            if UserSpot >= 100:
                print('You win!')
                break

            rollAgain = str(input('Would you like to roll again?: '))

diceRoller()

