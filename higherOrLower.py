#initialize random number
import random 

actualNumber = random.randint(0, 100)

def main():
    #input of number
    guessedNumber = int(input('What is your guessed number?: '))

    #checking
    if(guessedNumber > actualNumber):
        print('A little above!')
    elif(guessedNumber < actualNumber ):
        print('A little under!')

main()
tryAgain = input('Wanna try again?: ')
if(tryAgain == 'Yes'):
    main()
else:
    exit
    
