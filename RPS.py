import random
print("Winning rules for the game \n" + "Rock vs Paper: Paper wins \n" + "Rock vs Scissors: Rock wins \n" + "Paper vs Scissors: Scissor wins \n")
while True:
    print("Enter your user value \n 1 for rock \n 2 for paper \n 3 for scissor")
    user = int(input("Users choice: "))
    while user>3 or user<1:
        user = int(input("Please enter a valid input: "))
    if user == 1:
        user_value = "rock"
    elif user == 2:
        user_value = "paper"
    else:
        user_value = "scissor"
    print("Value chosen by the user: \n" + user_value)
    comp = random.randint(1,3)
    if comp == 1:
        comp_value = 'rock'
    elif comp == 2:
        comp_value = 'paper'
    else:
        comp_value = 'scissor'

    print("Value chosen by the computer: \n" + comp_value)
    if(user == comp):
        result="tie"
    elif((user_value == "paper" and comp_value == "rock")or(user_value == "rock" and comp_value == "paper")):
        print("paper wins over rock")
        result = "paper"
    elif((user_value == "rock" and comp_value == "scissor")or(user_value == "rock" and comp_value == "scissor")):
        print("rock wins over scissor")
        result = "rock"
    else:
        print("scissor wins over paper")
        result = "scissor"
    if result == "tie":
        print("it is a tie")
    elif result == user_value:
        print("User wins !!")
    else:
        print("Computer wins !!")
    print("Do you want to play again?(y/n)")
    ans = input()
    if ans == 'n' or ans == 'N':
        break
print("Thanks for playing the game!!")