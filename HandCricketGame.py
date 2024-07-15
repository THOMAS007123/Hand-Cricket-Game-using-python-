import random

player = input("Enter your Name :")



playerscore = 0
computerscore = 0
def playerbat():
    global playerscore
    while True:
        run = int(input("Enter your run : "))
        if run > 6:
            print("Not Valid")
            continue
        compbowl = random.randint(1,6)
        print("Computer bowled : ",compbowl)
        if run == compbowl:
            break
        else:
            playerscore = playerscore + run
        print("Player Score is:",playerscore)

def playerbowl():
    global computerscore
    while True:
        run = int(input("Enter your bowl"))
        if run > 6:
            print("Not Valid")
            continue
        compbat = random.randint(1,6)
        print("Computer batted : ",compbat)
        if run == compbat:
            break
        else:
            computerscore = computerscore + compbat
        print("Computer Score is:",computerscore)    

replay = 1
while (replay != 0):
    choice = int(input("Enter 1 to bat first or Enter 2 to ball first"))
    if(choice == 1):
        playerbat()
        print("\033[1mPLAYER OUT\033[0m")
        playerbowl()
    elif (choice == 2):
        playerbowl()
        print("\033[1mCOMPUTER OUT\033[0m")
        playerbat()
    else:
        print("Invalid Choice")
    print("\033[1mComputer Score is:\033[0m",computerscore)
    print(player,"\033[1m Score is:\033[0m",playerscore)
    if playerscore > computerscore:
        print(player,"\033[1mWINS\033[0m")
    elif playerscore < computerscore:
        print("Computer \033[1mWINS\033[0m")
    else:
        print("Its a draw")

    replay = int(input("Enter 0 to exit else enter any number to continue"))
    if replay != 0:
        print("\033[1m---Next Game Begins---\033[0m")
        playerscore = 0
        computerscore = 0