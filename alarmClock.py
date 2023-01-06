#toDO's:
# 1. develop system so that any text can fit within the assigned box without messing up the box 
# 2. 


#imports
import time 
import os

class DataStorage:
    
    def __init__(self, time, input):
        self.time = time
        self.input= input




#empty box
empty_box = " ______________________________________________________________\n|                                                              |\n|                                                              |\n|                                                              |\n|                                                              |\n|                                                              |\n|                                                              |\n|                                                              |\n|                                                              |\n|                                                              |\n|______________________________________________________________|"

main_box = " ______________________________________________________________\n|                                                              |\n|                                                              |\n|                                                              |\n|                                                              |\n|                          main box                            |\n|                                                              |\n|                                                              |\n|                                                              |\n|                                                              |\n|______________________________________________________________|"
#plays "Hello Andrew" opening screen
def openingScreen():
    # text blink function for startup 
    def blink(hello_andrew):
        os.system("cls")
        while True:
            print(hello_andrew)
            time.sleep(0.92)
            os.system("cls")
            print(empty_box)
            time.sleep(0.92)
            os.system("cls")
            break
            
    

    #initializes alarm clock interface with hello andrew 
    hello_andrew = " ______________________________________________________________ \n|                                                              |\n|                                                              |\n|                                                              |\n|   █  █ █▀▀ █   █   █▀▀█       █▀▀█ █▀▀▄ █▀▀▄ █▀▀█ █▀▀ █   █  |\n|   █▀▀█ █▀▀ █   █   █  █ ▄▄    █▄▄█ █  █ █  █ █▄▄▀ █▀▀ █▄█▄█  |\n|   █  █ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀  █    █  █ ▀  ▀ ▀▀▀  ▀ ▀▀ ▀▀▀ ─▀─▀─  |\n|                                                              |\n|                                                              |\n|                                                              |\n|______________________________________________________________|\n"
    blink(hello_andrew)

    #repeats blink function 
    end_time = time.time() + 3  # Calculate the end time
    while time.time() < end_time:
        blink(hello_andrew)  # Run the function
        time.sleep(0)  # Wait 0.92 seconds


def mainScreen():
    print("You have entered the main screen")
    print(main_box)
    

#running sequence 
openingScreen()
time.sleep(1)
mainScreen()

