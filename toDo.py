#imports


#list

toDo = []

def main(toDo):
    
    remAdd = input("Would you rather add or remove something from the list?: ")
    
    if(remAdd == 'Add'):
        #add item to list
        
        i=0
        amount = int(input("How many thing do you have to do?: "))
        while i < amount:
                
            addList = input("What would you like to add to your list?: ")
            
            toDo.append(addList) 
                        
            i += 1
            
        print("To Do List: ")
        
        for item in toDo:
            print(item)
            
    #work on: 12/23/22
    elif(remAdd == 'Remove'):
        #remove item from list 
        removeList = input("What would you like to remove from your list?: ")


        i=0
        
        amount = int(input("What item do you want to remove?: "))
        
        addList = input("What would you like to add to your list?: ")
        
        toDo.remove(addList) 
                
        i += 1
        
            
        print("To Do List: ")
        
        for item in toDo:
            print(item)

main(toDo)
#constantly display list / (maybe another window using AI)

