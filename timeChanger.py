#import datetime library 
from datetime import datetime, timedelta
from telnetlib import NEW_ENVIRON

timeDEST = 0
timeDPST = -3
timeDUTC = 5
timeDAST = 1
timeDCST = -1
timeDMST = -2

#function that analyzes what timezone you are in and correlates it with the conversion

class RelativeTime(): 
    
    def __init__(self, timeDEST, timeDPST, timeDUTC, timeDAST, timeDCST, timeDMST):
        
        self.timeDEST = timeDEST
        self.timeDPST = timeDPST
        self.timeDUTC = timeDUTC
        self.timeDAST = timeDAST
        self.timeDCST = timeDCST
        self.timeDMST = timeDMST

    def time_change(self, converted_text):
        if(converted_text == PST):
            self.timeDEST = 3
            self.timeDPST = 0
            self.timeDUTC = -4
            self.timeDAST = 4
            self.timeDCST = 2
            self.timeDMST = 1
            
        elif (converted_text == EST):
            self.timeDEST = -5
            self.timeDPST = -8
            self.timeDUTC = 0
            self.timeDAST = -4
            self.timeDCST = 6
            self.timeDMST = 5
            
        elif (converted_text == UTC):
            self.timeDEST = -5
            self.timeDPST = -8
            self.timeDUTC = 0
            self.timeDAST = -4
            self.timeDCST = 6
            self.timeDMST = 5
        elif (converted_text == AST): #Work on it later i wanna start something new
            self.timeDEST = -5
            self.timeDPST = -8
            self.timeDUTC = 0
            self.timeDAST = -4
            self.timeDCST = 6
            self.timeDMST = 5


def amPM(newTime, nowTime):
    if newTime.hour <= 12:
        print("%s AM" % newTime)
    else:
        print("%s PM" % newTime)

def timeCheck(times, timeInput):
    # Get the current timezone.
    current_timezone = datetime.now().astimezone().tzinfo
    
    textConvert(current_timezone, times, timeInput)

#change text to the first letter of each word     
def textConvert(current_timezone, times, timeInput):
    text_input = str(current_timezone)

    # Take the first letter of each word in string, make it capitalized and join together. 
    converted_text = ''.join([word[0].upper() for word in text_input.split()])
    
    #maybe say its the timezone you're in right now 
    print("Current Timezone: %s (%s)" % (converted_text, text_input))
    
    #return converted_text
    if converted_text == timeInput: 
        for i in times:
                if i == converted_text:
                    print('%s is the timezone you are in right now silly' % converted_text)
                    break
    else:
        print("You are not in %s" % timeInput)

# reverses timeInput into name of function, and if function is in program it will
# call it, and if not it will output that it did not return the inputted function
def callFunction(timeInput, times):
    func = globals().get(timeInput)
    if func:
        return func(timeInput, times)
    else:
        print("Didn't return function %s" % timeInput)

#main function that is run on startup
def main():
    
    
    #gets current time 
    nowTime = datetime.now()

    #prints current date/time
    print("Current date and time:")
    print("Date:",nowTime.date())
    print("Time:",nowTime.time())

    #asks for time zone conversion 
    print("Options: EST, PST, UTC, AST, CST, MST")
    timeInput = input("What do you want to convert to?: ")
    #array of availabe time zones 
    times = ["EST", "PST", "UTC", "AST", "CST", "MST"]
  
    # go through times array, and if one of the time zones in the list is equal to the timeInput, say its available and call the function 
    for i in times:
        if i == timeInput:
            print('%s is an available option' % timeInput)
            callFunction(timeInput, times)
"""         else:
            print('%s is not an available option' % timeInput)
            break """                

#EST Conversion Function         
def EST(self, timeInput, times, converted_text):
    #check if the timezone is the one the user is in
    timeCheck(times, timeInput)
    #Gets current time, adds a certain amount of time to current time, and prints output
    nowTime = datetime.now()
    RelativeTime.EST(converted_text, timeDEST, timeDPST, timeDUTC, timeDAST, timeDCST, timeDMST)
    #function that decides which conversion to use     

    newTime = nowTime + timedelta(hours= self.time_change.timeDEST)
    print("Time/Date in %s:" % timeInput)
    amPM(newTime, nowTime)

#PST Conversion Function         
def PST(timeInput, times):
    #check if the timezone is the one the user is in
    timeCheck(times, timeInput)
    #Gets current time, adds a certain amount of time to current time, and prints output
    nowTime = datetime.now()
    
    #function that decides which conversion to use     

    newTime = nowTime + timedelta(hours= timeDPST)
    print("Time/Date in %s:" % timeInput)
    amPM(newTime, nowTime)

#UTC Conversion Function         
def UTC(timeInput, times):
    #check if the timezone is the one the user is in
    timeCheck(times, timeInput)
    #Gets current time, adds a certain amount of time to current time, and prints output
    nowTime = datetime.now()
    
    #function that decides which conversion to use     
    
    newTime = nowTime + timedelta(hours= timeDUTC)
    print("Time/Date in %s:" % timeInput)
    amPM(newTime, nowTime)

#AST Conversion Function         
def AST(timeInput, times):
    #check if the timezone is the one the user is in
    timeCheck(times, timeInput)
    #Gets current time, adds a certain amount of time to current time, and prints output
    nowTime = datetime.now()
    
    #function that decides which conversion to use     
    
    newTime = nowTime + timedelta(hours= timeDAST)
    print("Time/Date in %s:" % timeInput)
    amPM(newTime, nowTime)

#CST Conversion Function         
def CST(timeInput, times):
    #check if the timezone is the one the user is in
    timeCheck(times, timeInput)
    #Gets current time, adds a certain amount of time to current time, and prints output
    nowTime = datetime.now()
    
    #function that decides which conversion to use     
    
    newTime = nowTime + timedelta(hours= timeDCST)
    print("Time/Date in %s:" % timeInput)
    amPM(newTime, nowTime)

#MST Conversion Function         
def MST(timeInput, times):
    #check if the timezone is the one the user is in
    timeCheck(times, timeInput)
    #Gets current time, adds a certain amount of time to current time, and prints output
    nowTime = datetime.now()
    
    #function that decides which conversion to use     
    
    newTime = nowTime + timedelta(hours= timeDMST)
    str(newTime)
    print("Time/Date in %s:" % timeInput)
    amPM(newTime, nowTime)

#starts program 
main()
