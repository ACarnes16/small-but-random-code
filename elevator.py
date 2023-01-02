oldFloor = 1


def main(oldFloor, newFloor):

    #get input on the floor the user wants to travel to
    newFloor = int(input("floor #: ")) 
       
    #gets the total distance inbetween floors needed to travel 
    floorDifference = abs(newFloor - oldFloor)
    
    #determines if the inputted floor is above or below the current floor 
    if newFloor > oldFloor:
        
        for i in range(floorDifference):
            print("Floor %s" % i)
            i = i+1
    elif newFloor < oldFloor:
            for i in range(floorDifference):
                i = i-1
                print("Floor %s" % i)
                
    #outputs text when new floor is successfully reached 
    print("you have reached floor %s" % newFloor)
    
    #the floor the user is newly on will becomes the current/old floor
    oldFloor = newFloor
    
    #asks user for the desired floor to travel to
    newFloor = int(input("floor #: ")) 
    
    #determines if inputted floor is the same floor they are currently on 
    if newFloor != oldFloor:
        main(oldFloor, newFloor)
    else:
        print("youre on this floor")
                
#beginning sequence 
print("Select Desired Floor: ")
print("9 8 7 6 5 4 3 2 1")
#oldFloor = int(input("floor to start on: "))
main(oldFloor)
