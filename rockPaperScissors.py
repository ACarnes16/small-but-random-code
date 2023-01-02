#define rock paper and scissors
from random import random
import random

#defines rock, paper. and scissors as int values
rock = 1
paper = 2
scissors = 3

#computes outcome
def decide(rock, personPlay, paper, scissors, computerPlay):
    if computerPlay == rock and personPlay == rock:
        print("It's a draw!")
    elif computerPlay == rock and personPlay == paper:
        print('You Win!')
    elif computerPlay == rock and personPlay == scissors:
        print("The Computer Wins :(")
    elif computerPlay == paper and personPlay == rock:
        print("The Computer Wins :(")
    elif computerPlay == paper and personPlay == paper:
        print("It's a draw!")
    elif computerPlay == paper and personPlay == scissors:
        print("You Win!")
    elif computerPlay == scissors and personPlay == rock:
     print("You Win!")
    elif computerPlay == scissors and personPlay == paper:
        print("The Computer Wins :(")
    elif computerPlay == scissors and personPlay == scissors:
        print("It's a draw!")

#main function
def main():
    #get computers play
    computerPlay = int(random.randint(1,3))
    if(computerPlay == 1):
        cName = 'rock'
    elif(computerPlay == 2):
        cName = 'paper'
    elif(computerPlay == 3):
        cName = 'scissors'

    #get persons play
    personPlay = str(input('Rock Paper or Scissors?: '))
    if(personPlay == 'Rock'):
        personPlay = rock
        name = 'rock'
    elif(personPlay == 'Paper'):
        personPlay = paper
        name = 'paper'
    elif(personPlay == 'Scissors'):
        personPlay = scissors
        name = 'scissors'
        
    #output what person plays
    print('Person plays %s' % name)
    print('Computer plays %s' % cName)
    decide(rock, personPlay, paper, scissors, computerPlay)
    
    #ask if user wants to play again
    again = input('Want to play again? (Y/N): ')
    if (again == 'Y'):
        main()
    else:
        exit

#runs main function
main()