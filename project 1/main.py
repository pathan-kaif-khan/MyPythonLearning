#project 1
#Snake Water Gun Game
'''
1  for Snake
-1 for Water
0  for Gun
'''

import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice:")
youDict = {"s":1 ,"w":-1,"g":0}
reverseDict = {1:"Snake",-1: "Water",0 : "Gun"}

you = youDict[youstr]

# by now we have two numbers (variables),ie you and comp
print(f"you chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")
 #reverseDict is printing the value you and comp entered 
 # suppose you chose s->1 ->"Snake" which is in reverseDict

if computer==you:
    print("it's a draw")

else:
    if (computer==1 and you==-1):
        print("You Lose!")
    elif(computer==1 and you==0):
        print("You Win!")
    elif(computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You Lose!")
    elif(computer==0 and you==-1):
        print("You Win!")
    elif(computer==0 and you==1):
        print("You Lose!")
    else:
        print("something went Wrong")