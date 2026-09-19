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

elif((computer - user)== 1 or (computer - user)==-2):
    print("You Lose!")

else:
    print("You Win")