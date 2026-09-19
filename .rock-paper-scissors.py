'''
1 is for Rock
-1 is for paper
0 is for scissor

'''
import random
computer = random.choice([1 , -1 , 0])
userstr = input("Enter your choice : ")
userdict = {"r" : 1 , "p" : -1 , "s" : 0}
reversedict = {1 : "rock" , -1 : "paper" , 0 : "scissor"}

user = userdict[userstr]

print(f"you chose {reversedict[user]}\ncomputer chose {reversedict[computer]}")

if(computer==user):
    print("Its a Draw")

else:
    if(computer==1 and user ==-1): #2
        print("You win!")

    elif(computer==1 and user ==0): #1
        print("You lose!")

    elif(computer==-1 and user ==1): #-2
      print("You lose!")

    elif(computer==-1 and user ==0): #-1
        print("You win!")

    elif(computer==0 and user ==1): #-1
       print("You win!")

    elif(computer==0 and user ==-1): #1
        print("You lose!")

    else:
        print("Something went wrong")


