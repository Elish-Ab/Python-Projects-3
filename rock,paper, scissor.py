import random


user_win = 0
computer_win = 0

options = ["scissor", 'paper', "rock"]

while True:
    user_pick = input(" Type scissor/paper/rock or Q to quit ").lower()
    if user_pick == "q":
        break
    if user_pick not in options:
        continue

    random_num = random.randint(0, 2)

    computer_pick = options[random_num]
    print('Computer picked', computer_pick, '.')

    if user_pick == "rock" and computer_pick == "scissor":
        print("You won!")
        user_win += 1

    elif user_pick == "paper" and computer_pick == "rock":
        print("You won!")
        user_win += 1

    elif user_pick == "scissor" and computer_pick == "paper":
        print("You won!")
        user_win += 1
    else:
        print('Computer won!')
        computer_win += 1


print("You won", user_win, ".")
print("Computer won", computer_win, ".")
print("Goodbye")
