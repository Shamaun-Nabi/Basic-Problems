import myfriendschoices

CommonChoices=myfriendschoices.generateCommonChoices("friend1.txt","friend2.txt")
# print(CommonChoices)
finalRides=open("FinalRides.txt",'a')
while True:
    
    userInput=input("Enter a rides Name \n ")
    if userInput=="That will be All":
        break
    if userInput in CommonChoices:
       
        finalRides.writelines(userInput+"\n")
    else:
        print("Sorry! We don’t want to take that ride")
        
