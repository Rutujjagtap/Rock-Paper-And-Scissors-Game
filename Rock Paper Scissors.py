#First asking the user to choose between Rock, Paper and Scissors

while True:
    user = int(input("Select an object (1-Rock 2-Paper 3-Scissors) :\n"))

    if user<0 or user>3:
        raise Exception("Enter a valid number")

    import random

    compt = random.randint(1,3)

    if user == 1:
        if compt == 1:
            print("Its a Tie")
        elif compt == 2:
            print('You selected Rock, Computer selected Paper: Computer Won!!!')
        else:
            print('You selected Rock, Computer selected Scissors: You Won!!!')

    if user == 2:
        if compt == 2:
            print("Its a Tie")
        elif compt == 1:
            print('You selected Paper, Computer selected Rock: You Won!!!')
        else:
            print('You selected Paper, Computer selected Scissors: Computer Won!!!')

    if user == 3:
        if compt == 3:
            print("Its a Tie")
        elif compt == 1:
            print('You selected Scissors, Computer selected Rock: Computer Won!!!')
        else:
            print('You selected Scissors, Computer selected Paper: You Won!!!')

    if user == 0:
        print("Thank you for playing")
        break
