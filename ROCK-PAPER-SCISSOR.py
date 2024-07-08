print("Enter The World Of: \n               'ROCK-PAPER-SCISSOR'\n")

a=int(input("Enter 1 To Continue \nEnter 0 To Leave \n\nPlease Enter Your Choice: "))
print("***We Are Working On Your Choice*** \n")
if(a==0):
    print("Thank You, Come Back Later")
else:
    print("You Are Welcome :) \n")

import random
computer=random.randint(0,2)

user=int(input("Please Select Your Choice: \n For ROCK Press 0\n For PAPER Press 1\n For SCISSOR Press 2 \n\nEnter Your Choice: "))
if(user==0):
    print("You Select ROCK!!\n")
elif(user==1):
    print("You Select PAPER!!\n")
else:
    print("You Select SCISSOR!!\n")

def check(computer,user):
    if(computer==user):
        return 0
    elif(computer==0 and user==2):
        return -1
    elif(computer==1 and user==0):
        return -1
    elif(computer==2 and user==1):
        return -1
    else:
        return 1

score=check(computer,user)
print("You: ",user)
print("Com: ",computer)

if(score==0):
    print("It's A Draw")
elif(score==-1):
    print("You Lose \nBetter Luck Next Time!!")
else:
    print("Congratulations!! You Won")

