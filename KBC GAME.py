print("Welcome To The Game Of Fun And Earn \n\n-------One And Only The KBC--------\n")
a=int(input("Enter 1 To Continue \nEnter 0 To Leave \n\nPlease Enter Your Choice: "))
print("***We Are Working On Your Choice***")
if(a==1):
    print("\nThanks For Continue, So Let's Start The Game\n")
else:
    print("Thank You For Connecting With Us, See You Later\n")
b=input("Please Enter Your Full Name: ")
print("Thank You",b)
print("\nNote: \na. You Have To Answer Only Three Questions \nb. Each Correct Answer: 25Lakhs \nc. Wrong Answer: Out Of The Game \nSo Be Careful While Answering \nAll The Best!!")
print("\nAre You Ready??\n")
c=input("If Yes Then Write YES (Otherwise NO): ")
if(c=="YES"):
    print("-----Your First Question Is On The Screen-----\n")
else:
    print("Wait And Continue....")
qs="Who is our Prime Minister?\n a. Narendra Modi\n b. Sahrukh Khan\n c. Sachin Tendulkar\n d. Mamata Banerjee\n"
print(qs)
d=input("Plese Select Your Answer: ")
if(d=="a"):
    print("\nCongratulations, Correct Answer.\nYou Won 25Lakh rs!!\n")
else:
    print("Sorry, Wrong Answer.\nBetter Luck Next Time.\n")
e=int(input("Enter 0 To Continue \nEnter 1 To Withdraw \nPlease Enter Your Choice: "))
if(e==0):
    print("----Your Second Question Is On The Screen----\n")
else:
    print("Thank You.\nYour Transaction Is On Process, Please Wait...")
qs1="Which One Is The National Bird Of India?\n a. Crow\n b. Peacock\n c. Parrot\n d. Owl"
print(qs1)
f=input("Plese Select Your Answer: ")
if(f=="b"):
        print("\nCongratulations, Correct Answer.\nYou Won 25Lakh rs!!\nNow, Your Amount Is 50Lakhs, Nice!!\n")
else:
    print("Sorry, Wrong Answer.\nBetter Luck Next Time.\n")
g=int(input("Enter 0 To Continue \nEnter 1 To Withdraw \nPlease Enter Your Choice: "))
if(g==0):
    print("----Your Final Question Is On The Screen----\n")
else:
    print("Thank You.\nYour Transaction Is On Process, Please Wait...")
qs2="Which One Is The National Game Of India?\n a. Cricket\n b. Football\n c. Hockey\n d. Kabaddi"
print(qs2)
h=input("Plese Select Your Answer: ")
if(h=="d"):
        print("\nCongratulations, Correct Answer.\nYou Won 25Lakh rs!!\n\nNow, Your Amount Total Is 75Lakhs And Also You Get +25Lakhs On Bonus.\nHureeehhhhh!!! You Are A Champion\nYou Won 1 Corer.\n")
else:
    print("Sorry, Wrong Answer.\nIt Was A Great Game,\nBetter Luck Next Time.\n")
i=int(input("Enter 0 To Back \nEnter 1 To Withdraw \nPlease Enter Your Choice: "))
if(i==0):
    print("----Thank You----\n")
else:
    print("Congrats!!!.\nYour Transaction Is On Process, Please Wait...")
